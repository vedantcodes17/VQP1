"""
concept_generator.py

Generates the canonical concept schema directly from raw teacher notes,
using the prompt defined in prompt.py.

For each chapter's teacher_notes/<chapter>.txt file:
    1. get_concept_prompt() supplies the full instructions + output schema.
    2. The teacher notes are appended as the input to work from.
    3. The complete prompt is sent to the local LLM in one call.
    4. The response is validated and saved to concepts/<chapter>.json.

Usage:
    python concept_generator.py              # every chapter in teacher_notes/
    python concept_generator.py Solutions     # just teacher_notes/Solutions.txt
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

import utils
from prompt import get_concept_prompt

LOGGER = utils.setup_logger("concept_generator")

RELATIONSHIP_TYPES = {"is_subtopic_of", "requires", "commonly_confused_with"}

REQUIRED_FIELDS = [
    "concept_id",
    "concept_name",
    "definition",
    "aliases_and_keywords",
    "learning_outcomes",
    "common_mistakes",
    "relationships",
    "assessment_hint",
    "retrieval",
]


def build_user_prompt(notes: str) -> str:
    return (
        f"Teacher Notes:\n\n{notes}\n\n"
        f"Extract EVERY distinct concept mentioned in the notes above as its "
        f"own separate entry in the output array. Do not merge multiple "
        f"distinct concepts (e.g. Molarity, Molality, Raoult's Law, Osmotic "
        f"Pressure would each be their own entry) into a single entry."
    )


def make_validator():
    def validator(parsed: Any) -> None:
        if not isinstance(parsed, list) or not parsed:
            raise ValueError("Response is not a non-empty JSON array")

        seen_ids: Set[str] = set()
        for i, item in enumerate(parsed):
            if not isinstance(item, dict):
                raise ValueError(f"item[{i}] is not an object")

            cid = item.get("concept_id")
            if not isinstance(cid, str) or not cid.strip():
                raise ValueError(f"item[{i}] missing/invalid concept_id")
            if cid in seen_ids:
                raise ValueError(f"duplicate concept_id '{cid}' in response")
            seen_ids.add(cid)

            missing = [f for f in REQUIRED_FIELDS if f not in item]
            if missing:
                raise ValueError(f"item '{cid}' missing field(s): {missing}")

    return validator


def sanitize_str_list(value: Any) -> List[str]:
    if not isinstance(value, list):
        return []
    return [v for v in value if isinstance(v, str) and v.strip()]


def sanitize_learning_outcomes(value: Any) -> List[Dict[str, str]]:
    if not isinstance(value, list):
        return []
    outcomes = []
    for lo in value:
        if isinstance(lo, dict) and isinstance(lo.get("verb"), str) and isinstance(lo.get("object"), str):
            outcomes.append({"verb": lo["verb"], "object": lo["object"]})
    return outcomes


def sanitize_relationships(value: Any) -> List[Dict[str, str]]:
    if not isinstance(value, list):
        return []
    relationships = []
    for r in value:
        if isinstance(r, dict) and r.get("type") in RELATIONSHIP_TYPES and isinstance(r.get("target"), str):
            relationships.append({"type": r["type"], "target": r["target"]})
    return relationships


def sanitize_concept(item: Dict[str, Any]) -> Dict[str, Any]:
    aliases_and_keywords = item.get("aliases_and_keywords") or {}
    assessment_hint = item.get("assessment_hint") or {}
    retrieval = item.get("retrieval") or {}

    return {
        "concept_id": item["concept_id"],
        "concept_name": item.get("concept_name", ""),
        "definition": item.get("definition", ""),
        "aliases_and_keywords": {
            "aliases": sanitize_str_list(aliases_and_keywords.get("aliases")),
            "keywords": sanitize_str_list(aliases_and_keywords.get("keywords")),
        },
        "learning_outcomes": sanitize_learning_outcomes(item.get("learning_outcomes")),
        "common_mistakes": sanitize_str_list(item.get("common_mistakes")),
        "relationships": sanitize_relationships(item.get("relationships")),
        "assessment_hint": {
            "preferred_question_types": sanitize_str_list(assessment_hint.get("preferred_question_types")),
            "recommended_marks": [m for m in (assessment_hint.get("recommended_marks") or []) if isinstance(m, (int, float))],
            "blooms_levels": sanitize_str_list(assessment_hint.get("blooms_levels")),
        },
        "retrieval": {
            "chunk_ids": sanitize_str_list(retrieval.get("chunk_ids")),
            "pyq_ids": sanitize_str_list(retrieval.get("pyq_ids")),
        },
    }


def generate_concepts(notes: str) -> List[Dict[str, Any]]:
    parsed = utils.call_llm_json(
        system_prompt=get_concept_prompt(),
        user_prompt=build_user_prompt(notes),
        logger=LOGGER,
        validator=make_validator(),
        raw_dump_filename="concept_generator_raw_output.txt",
    )

    concepts = [sanitize_concept(item) for item in parsed]

    # A relationship can only point at a concept_id this same chapter
    # actually produced -- drop anything the LLM invented beyond that.
    known_ids = {c["concept_id"] for c in concepts}
    for c in concepts:
        c["relationships"] = [r for r in c["relationships"] if r["target"] in known_ids]

    return concepts


def process_chapter(notes_path: Path) -> Optional[Path]:
    chapter = utils.chapter_key(notes_path)
    LOGGER.info(f"=== Concept generation: {chapter} ===")

    notes = utils.read_text(notes_path)

    try:
        concepts = generate_concepts(notes)
    except Exception as e:
        LOGGER.error(f"Concept generation failed for '{chapter}': {e}")
        return None

    out_path = utils.CONCEPTS_DIR / f"{chapter}.json"
    utils.save_json(concepts, out_path)
    LOGGER.info(f"Saved {len(concepts)} concept(s) to {out_path}")
    return out_path


def main() -> None:
    chapter_arg = sys.argv[1] if len(sys.argv) > 1 else None
    notes_files = utils.resolve_chapters(chapter_arg)

    LOGGER.info("=" * 80)
    LOGGER.info(f"CONCEPT GENERATOR -- {len(notes_files)} chapter(s)")
    LOGGER.info("=" * 80)

    for notes_path in notes_files:
        process_chapter(notes_path)


if __name__ == "__main__":
    main()
