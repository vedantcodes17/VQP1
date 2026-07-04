"""
services/question_generator.py

STEP 3 -- Question Generator.
LLM persona: Chemistry Teacher.

Input : blueprint slot + selected concept + knowledge node (chapter_kb concept)
Output: generated_questions.json

Generates ONE question at a time (one LLM call per slot), in blueprint
slot order.
"""

import sys
from pathlib import Path
from typing import Any, Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import utils
from prompts.question_generator_prompt import QUESTION_GENERATOR_SYSTEM_PROMPT, QUESTION_GENERATOR_USER_TEMPLATE

LOGGER = utils.get_logger("question_generator")


def make_question_validator():
    def validator(parsed: Any) -> None:
        if not isinstance(parsed, dict):
            raise ValueError("Response is not a JSON object")
        for field in ("question", "answer", "marks", "difficulty", "bloom", "type", "concept_id"):
            if field not in parsed:
                raise ValueError(f"missing '{field}'")
        if not str(parsed["question"]).strip():
            raise ValueError("'question' is empty")
    return validator


def generate_one_question(slot: Dict[str, Any], concept: Dict[str, Any]) -> Dict[str, Any]:
    concept_view = {
        "concept_id": concept["concept_id"],
        "concept_name": concept["concept_name"],
        "aliases": concept.get("aliases", []),
        "definition": concept.get("definition", ""),
        "formulae": concept.get("formulae", []),
        "examples": concept.get("examples", []),
    }
    user_prompt = QUESTION_GENERATOR_USER_TEMPLATE.format(
        slot=utils.json.dumps(slot, indent=2),
        concept=utils.json.dumps(concept_view, indent=2),
    )

    parsed = utils.call_llm_json(
        system_prompt=QUESTION_GENERATOR_SYSTEM_PROMPT,
        user_prompt=user_prompt,
        validator=make_question_validator(),
        logger=LOGGER,
    )

    return {
        "question": str(parsed["question"]).strip(),
        "answer": str(parsed.get("answer", "")).strip(),
        "marks": slot["marks"],  # trust blueprint over LLM echo
        "difficulty": slot["difficulty"],
        "bloom": str(parsed.get("bloom", "")).strip() or (slot.get("bloom_levels") or [""])[0],
        "type": slot["question_type"],
        "concept_id": concept["concept_id"],
        "requires_diagram": False,
    }


def generate_all_questions(blueprint: Dict[str, Any], selected_concepts: List[Dict[str, Any]],
                            chapter_kb: Dict[str, Any]) -> List[Dict[str, Any]]:
    concepts_by_id = {c["concept_id"]: c for c in chapter_kb["concept_tree"]}
    concept_for_slot = {a["slot_id"]: a["concept_id"] for a in selected_concepts}

    questions = []
    for i, slot in enumerate(blueprint["slots"], start=1):
        concept_id = concept_for_slot.get(slot["slot_id"])
        concept = concepts_by_id.get(concept_id)
        if concept is None:
            LOGGER.error(f"Slot {slot['slot_id']}: no concept assigned/found, skipping")
            continue

        LOGGER.info(f"Generating question {i}/{len(blueprint['slots'])} "
                    f"(slot={slot['slot_id']}, concept={concept['concept_name']!r})")
        q = generate_one_question(slot, concept)
        q["id"] = f"Q{i:03d}"
        q["slot_id"] = slot["slot_id"]
        questions.append(q)

    LOGGER.info(f"Generated {len(questions)} question(s)")
    return questions


if __name__ == "__main__":
    chapter_kb = utils.load_json(utils.CHAPTER_KB_FILE)
    blueprint = utils.load_json(utils.BLUEPRINT_FILE)
    selected_concepts = utils.load_json(utils.SELECTED_CONCEPTS_FILE)
    questions = generate_all_questions(blueprint, selected_concepts, chapter_kb)
    utils.save_json(questions, utils.GENERATED_QUESTIONS_FILE)
    print(f"Saved: {utils.GENERATED_QUESTIONS_FILE}")
