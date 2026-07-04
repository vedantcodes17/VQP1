"""
services/question_validator.py

STEP 5 -- Validator.
LLM persona: CBSE Moderator (qualitative pass only).

Deterministic checks (duplicate questions, duplicate concepts, marks
mismatch, blueprint mismatch, requires_diagram) are done in code -- exact
matching/arithmetic is not something a small local LLM should be trusted
with. The LLM is then used for a second, qualitative moderation pass that
code cannot do (factual consistency, question/mark mismatch "by feel").

Output: validation_report.json
"""

import sys
from pathlib import Path
from typing import Any, Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import utils
from prompts.validator_prompt import VALIDATOR_SYSTEM_PROMPT, VALIDATOR_USER_TEMPLATE

LOGGER = utils.get_logger("question_validator")


def deterministic_checks(questions: List[Dict[str, Any]], blueprint: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
    slots_by_id = {s["slot_id"]: s for s in blueprint["slots"]}
    flags: Dict[str, List[str]] = {}

    def flag(question_id: str, reason: str) -> None:
        flags.setdefault(question_id, [])
        if reason not in flags[question_id]:
            flags[question_id].append(reason)

    # duplicate question text
    seen_text: Dict[str, str] = {}
    for q in questions:
        key = utils.normalize_text(q["question"])
        if key in seen_text:
            flag(q["id"], f"Duplicate question text (same as {seen_text[key]})")
            flag(seen_text[key], f"Duplicate question text (same as {q['id']})")
        else:
            seen_text[key] = q["id"]

    # duplicate concept usage
    seen_concept: Dict[str, List[str]] = {}
    for q in questions:
        seen_concept.setdefault(q.get("concept_id", ""), []).append(q["id"])
    for concept_id, qids in seen_concept.items():
        if concept_id and len(qids) > 1:
            for qid in qids:
                flag(qid, f"Concept {concept_id!r} reused across questions {qids}")

    # marks / blueprint mismatch against the slot, and diagram flag
    for q in questions:
        slot = slots_by_id.get(q.get("slot_id", ""))
        if slot is None:
            flag(q["id"], f"Unknown slot_id {q.get('slot_id')!r} (blueprint mismatch)")
        else:
            if q.get("marks") != slot["marks"]:
                flag(q["id"], f"Marks mismatch: question={q.get('marks')} vs blueprint slot={slot['marks']}")
            if q.get("type") != slot["question_type"]:
                flag(q["id"], f"Type mismatch: question={q.get('type')} vs blueprint slot={slot['question_type']}")
            if q.get("difficulty") != slot["difficulty"]:
                flag(q["id"], f"Difficulty mismatch: question={q.get('difficulty')} vs blueprint slot={slot['difficulty']}")

        if q.get("requires_diagram"):
            flag(q["id"], "Diagram generation unavailable.")

    return flags


def format_question_list(questions: List[Dict[str, Any]]) -> str:
    lines = []
    for q in questions:
        lines.append(f"- {q['id']}: [{q.get('marks')}m] {q['question']} || answer: {q.get('answer', '')[:200]}")
    return "\n".join(lines)


def run_llm_quality_pass(questions: List[Dict[str, Any]], deterministic_flags: Dict[str, List[str]]) -> Dict[str, List[str]]:
    summary = f"{len(deterministic_flags)} question(s) already flagged deterministically out of {len(questions)} total."
    user_prompt = VALIDATOR_USER_TEMPLATE.format(
        deterministic_summary=summary,
        question_list=format_question_list(questions),
    )

    def validator(parsed: Any) -> None:
        if not isinstance(parsed, dict) or not isinstance(parsed.get("quality_flags"), list):
            raise ValueError("Missing/invalid 'quality_flags'")

    try:
        parsed = utils.call_llm_json(
            system_prompt=VALIDATOR_SYSTEM_PROMPT,
            user_prompt=user_prompt,
            validator=validator,
            logger=LOGGER,
            max_tokens=2048,
        )
    except Exception as e:
        LOGGER.warning(f"LLM quality pass failed, continuing with deterministic checks only: {e}")
        return {}

    valid_ids = {q["id"] for q in questions}
    quality_flags: Dict[str, List[str]] = {}
    for item in parsed.get("quality_flags", []):
        qid = item.get("question_id")
        reason = str(item.get("reason", "")).strip()
        if qid in valid_ids and reason:
            quality_flags.setdefault(qid, []).append(f"[Moderator] {reason}")
    return quality_flags


def validate(questions: List[Dict[str, Any]], blueprint: Dict[str, Any]) -> Dict[str, Any]:
    flags = deterministic_checks(questions, blueprint)
    LOGGER.info(f"Deterministic checks: {len(flags)} question(s) flagged")

    quality_flags = run_llm_quality_pass(questions, flags)
    for qid, reasons in quality_flags.items():
        flags.setdefault(qid, []).extend(reasons)

    flagged = [{"question_id": qid, "reasons": reasons} for qid, reasons in flags.items()]

    report = {
        "total_questions": len(questions),
        "flagged_count": len(flagged),
        "flagged": flagged,
    }
    LOGGER.info(f"Validation complete: {len(flagged)}/{len(questions)} question(s) flagged")
    return report


if __name__ == "__main__":
    questions = utils.load_json(utils.QUESTIONS_WITH_DIAGRAM_FILE)
    blueprint = utils.load_json(utils.BLUEPRINT_FILE)
    report = validate(questions, blueprint)
    utils.save_json(report, utils.VALIDATION_REPORT_FILE)
    print(f"Saved: {utils.VALIDATION_REPORT_FILE}")
