"""
services/question_regenerator.py

STEP 6 -- Regenerator.
LLM persona: Senior Examiner.

Input : flagged questions (from validation_report.json) + the SAME concept
Output: final_questions.json (flagged questions replaced in place)
"""

import sys
from pathlib import Path
from typing import Any, Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import utils
from prompts.regenerator_prompt import REGENERATOR_SYSTEM_PROMPT, REGENERATOR_USER_TEMPLATE

LOGGER = utils.get_logger("question_regenerator")


def make_regen_validator():
    def validator(parsed: Any) -> None:
        if not isinstance(parsed, dict):
            raise ValueError("Response is not a JSON object")
        for field in ("question", "answer", "marks", "difficulty", "bloom", "type", "concept_id"):
            if field not in parsed:
                raise ValueError(f"missing '{field}'")
        if not str(parsed["question"]).strip():
            raise ValueError("'question' is empty")
    return validator


def regenerate_one(question: Dict[str, Any], reasons: List[str], slot: Dict[str, Any],
                    concept: Dict[str, Any]) -> Dict[str, Any]:
    concept_view = {
        "concept_id": concept["concept_id"],
        "concept_name": concept["concept_name"],
        "aliases": concept.get("aliases", []),
        "definition": concept.get("definition", ""),
        "formulae": concept.get("formulae", []),
        "examples": concept.get("examples", []),
    }
    user_prompt = REGENERATOR_USER_TEMPLATE.format(
        flagged_question=utils.json.dumps({"question": question["question"], "answer": question.get("answer", "")}, indent=2),
        reason="; ".join(reasons),
        slot=utils.json.dumps(slot, indent=2),
        concept=utils.json.dumps(concept_view, indent=2),
    )

    parsed = utils.call_llm_json(
        system_prompt=REGENERATOR_SYSTEM_PROMPT,
        user_prompt=user_prompt,
        validator=make_regen_validator(),
        logger=LOGGER,
    )

    return {
        "id": question["id"],
        "slot_id": question["slot_id"],
        "question": str(parsed["question"]).strip(),
        "answer": str(parsed.get("answer", "")).strip(),
        "marks": slot["marks"],
        "difficulty": slot["difficulty"],
        "bloom": str(parsed.get("bloom", "")).strip() or (slot.get("bloom_levels") or [""])[0],
        "type": slot["question_type"],
        "concept_id": concept["concept_id"],
        "requires_diagram": False,
    }


def regenerate_flagged(questions: List[Dict[str, Any]], validation_report: Dict[str, Any],
                        blueprint: Dict[str, Any], chapter_kb: Dict[str, Any]) -> List[Dict[str, Any]]:
    slots_by_id = {s["slot_id"]: s for s in blueprint["slots"]}
    concepts_by_id = {c["concept_id"]: c for c in chapter_kb["concept_tree"]}
    questions_by_id = {q["id"]: q for q in questions}

    flagged_ids = {f["question_id"]: f["reasons"] for f in validation_report.get("flagged", [])}
    if not flagged_ids:
        LOGGER.info("No flagged questions to regenerate")
        return list(questions)

    result = list(questions)
    for i, q in enumerate(result):
        if q["id"] not in flagged_ids:
            continue
        reasons = flagged_ids[q["id"]]
        slot = slots_by_id.get(q["slot_id"])
        concept = concepts_by_id.get(q["concept_id"])
        if slot is None or concept is None:
            LOGGER.error(f"Cannot regenerate {q['id']}: missing slot or concept, leaving as-is")
            continue

        LOGGER.info(f"Regenerating {q['id']} (slot={q['slot_id']}, reasons={reasons})")
        try:
            result[i] = regenerate_one(q, reasons, slot, concept)
        except Exception as e:
            LOGGER.error(f"Regeneration failed for {q['id']}, keeping original flagged question: {e}")

    LOGGER.info(f"Regeneration complete: {len(flagged_ids)} question(s) replaced")
    return result


if __name__ == "__main__":
    questions = utils.load_json(utils.QUESTIONS_WITH_DIAGRAM_FILE)
    validation_report = utils.load_json(utils.VALIDATION_REPORT_FILE)
    blueprint = utils.load_json(utils.BLUEPRINT_FILE)
    chapter_kb = utils.load_json(utils.CHAPTER_KB_FILE)
    final_questions = regenerate_flagged(questions, validation_report, blueprint, chapter_kb)
    utils.save_json(final_questions, utils.FINAL_QUESTIONS_FILE)
    print(f"Saved: {utils.FINAL_QUESTIONS_FILE}")
