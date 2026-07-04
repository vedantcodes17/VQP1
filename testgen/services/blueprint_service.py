"""
services/blueprint_service.py

STEP 1 -- Blueprint Service.
LLM persona: Senior CBSE Paper Setter.

Input : teacher_input (hardcoded) + chapter_kb_enriched.json
Output: blueprint.json (sections + flattened per-question slots)

The LLM designs the SECTION structure (num_questions, marks_each,
question_type, difficulty, bloom_levels, concept_count) and marks totals
are validated deterministically (retried against the LLM if they don't
add up). Flattening sections into individually addressable slot_ids
(A1, A2, ... ) is a deterministic bookkeeping step done in code.
"""

import sys
from pathlib import Path
from typing import Any, Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import utils
from prompts.blueprint_prompt import BLUEPRINT_SYSTEM_PROMPT, BLUEPRINT_USER_TEMPLATE

LOGGER = utils.get_logger("blueprint_service")

ALLOWED_DIFFICULTIES = {"easy", "medium", "hard"}

# Fixed section layout for the hardcoded 30-mark teacher input (matches the
# CBSE example given in the spec: 5x1 + 5x2 + 3x3 + 1x6 = 30). A 7B local
# model is not reliable at freely inventing a layout that sums exactly to
# total_marks, so the layout is fixed deterministically and the LLM only
# decides the pedagogical attributes (question_type/difficulty/bloom/
# concept_count) for each section.
SECTION_SHAPE_BY_TOTAL_MARKS = {
    30: [
        {"section": "A", "num_questions": 5, "marks_each": 1},
        {"section": "B", "num_questions": 5, "marks_each": 2},
        {"section": "C", "num_questions": 3, "marks_each": 3},
        {"section": "D", "num_questions": 1, "marks_each": 6},
    ],
}


def get_section_shape(total_marks: int) -> List[Dict[str, Any]]:
    shape = SECTION_SHAPE_BY_TOTAL_MARKS.get(total_marks)
    if shape is None:
        raise NotImplementedError(
            f"No fixed section layout defined for total_marks={total_marks}. "
            f"Add one to SECTION_SHAPE_BY_TOTAL_MARKS."
        )
    return shape


def format_concept_summary(chapter_kb: Dict[str, Any]) -> str:
    lines = []
    for c in chapter_kb["concept_tree"]:
        if c.get("is_grouping_node"):
            continue
        lines.append(
            f"- {c['concept_name']} | importance={c.get('importance')} | "
            f"weightage={c.get('chapter_weightage')} | category={c.get('concept_category')}"
        )
    return "\n".join(lines)


def make_blueprint_validator(section_shape: List[Dict[str, Any]], allowed_types: List[str]):
    shape_by_section = {s["section"]: s for s in section_shape}

    def validator(parsed: Any) -> None:
        if not isinstance(parsed, dict) or not isinstance(parsed.get("sections"), list) or not parsed["sections"]:
            raise ValueError("Missing/empty 'sections'")
        if len(parsed["sections"]) != len(section_shape):
            raise ValueError(f"Expected {len(section_shape)} section(s), got {len(parsed['sections'])}")
        for i, s in enumerate(parsed["sections"]):
            for field in ("section", "question_type", "difficulty"):
                if field not in s:
                    raise ValueError(f"sections[{i}] missing '{field}'")
            if s["section"] not in shape_by_section:
                raise ValueError(f"sections[{i}] unknown section {s['section']!r}")
            if s["question_type"] not in allowed_types:
                raise ValueError(f"sections[{i}] invalid question_type {s['question_type']!r}")
            if str(s["difficulty"]).lower() not in ALLOWED_DIFFICULTIES:
                raise ValueError(f"sections[{i}] invalid difficulty {s['difficulty']!r}")
    return validator


def flatten_to_slots(sections: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    slots = []
    for s in sections:
        section_letter = str(s["section"]).strip()
        for i in range(1, int(s["num_questions"]) + 1):
            slots.append({
                "slot_id": f"{section_letter}{i}",
                "section": section_letter,
                "marks": int(s["marks_each"]),
                "difficulty": str(s["difficulty"]).lower(),
                "question_type": s["question_type"],
                "bloom_levels": s.get("bloom_levels", []),
            })
    return slots


def generate_blueprint(teacher_input: Dict[str, Any], chapter_kb: Dict[str, Any]) -> Dict[str, Any]:
    section_shape = get_section_shape(teacher_input["total_marks"])
    shape_by_section = {s["section"]: s for s in section_shape}

    concept_summary = format_concept_summary(chapter_kb)
    concept_count = sum(1 for c in chapter_kb["concept_tree"] if not c.get("is_grouping_node"))

    user_prompt = BLUEPRINT_USER_TEMPLATE.format(
        teacher_input=utils.json.dumps(teacher_input, indent=2),
        section_shape=utils.json.dumps(section_shape, indent=2),
        concept_count=concept_count,
        concept_summary=concept_summary,
    )

    LOGGER.info("Requesting blueprint from LLM...")
    parsed = utils.call_llm_json(
        system_prompt=BLUEPRINT_SYSTEM_PROMPT,
        user_prompt=user_prompt,
        validator=make_blueprint_validator(section_shape, teacher_input["question_types"]),
        logger=LOGGER,
    )

    sections = parsed["sections"]
    for s in sections:
        # Trust the fixed layout over the LLM's echo -- these are never allowed to drift.
        fixed = shape_by_section[s["section"]]
        s["num_questions"] = fixed["num_questions"]
        s["marks_each"] = fixed["marks_each"]
        s["difficulty"] = str(s["difficulty"]).lower()
        s.setdefault("concept_count", s["num_questions"])

    slots = flatten_to_slots(sections)

    blueprint = {
        "chapter": teacher_input["chapter"],
        "total_marks": teacher_input["total_marks"],
        "sections": sections,
        "slots": slots,
    }
    LOGGER.info(f"Blueprint ready: {len(sections)} section(s), {len(slots)} slot(s), "
                f"{sum(s['num_questions'] * s['marks_each'] for s in sections)} marks total")
    return blueprint


if __name__ == "__main__":
    chapter_kb = utils.load_json(utils.CHAPTER_KB_FILE)
    blueprint = generate_blueprint(utils.TEACHER_INPUT, chapter_kb)
    utils.save_json(blueprint, utils.BLUEPRINT_FILE)
    print(f"Saved: {utils.BLUEPRINT_FILE}")
