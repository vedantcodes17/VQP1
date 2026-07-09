"""
formula_generator.py

Generates the canonical formula schema from teacher notes + the chapter's
concepts.json, using the prompt defined in prompt.py. Runs in two stages:

    Stage 1 - Generation
        Input:  teacher notes + concepts/<chapter>.json
        Output: formulas/<chapter>.json
        Every formula must link to a concept_id that actually exists.

    Stage 2 - Formula Coverage Audit
        Immediately re-reads the teacher notes against the formulas Stage 1
        just wrote, asks the LLM to spot formulas the notes clearly contain
        but Stage 1 missed (plus duplicates / bad links, which are only
        logged -- never auto-edited). Only the missing formulas are
        appended to formulas/<chapter>.json; nothing already there is
        regenerated or modified.

Usage:
    python formula_generator.py              # every chapter with a concepts/ file
    python formula_generator.py Solutions    # just the "solutions" chapter
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

import utils
from prompt import get_formula_prompt

LOGGER = utils.setup_logger("formula_generator")

FORMULA_TYPES = {"Law", "Definition", "Relation", "Derived", "Empirical"}

REQUIRED_FIELDS = [
    "formula_id",
    "formula_name",
    "formula_type",
    "expression",
    "latex",
    "description",
    "variables",
    "linked_concepts",
    "derived_from",
    "common_mistakes",
    "retrieval",
]

AUDIT_INSTRUCTIONS = """
==================================================
FORMULA COVERAGE AUDIT
==================================================

You are now auditing formula coverage, not generating from scratch.

You are given the Teacher Notes again, plus the CURRENT FORMULAS already
extracted from them (in the schema above).

Identify

- missing_formulas: formulas clearly present in the Teacher Notes that are
  ABSENT from CURRENT FORMULAS. Produce these in the exact schema above,
  each linked to existing concept_ids only.

- duplicate_formulas: formula_id values in CURRENT FORMULAS that express
  the same relationship as another formula_id already in the list.

- incorrect_concept_links: CURRENT FORMULAS whose linked_concepts look
  wrong given the Teacher Notes.

Do NOT include any formula from CURRENT FORMULAS inside missing_formulas.

Do NOT modify CURRENT FORMULAS.

Return ONLY

{
    "missing_formulas": [],
    "duplicate_formulas": ["formula_id"],
    "incorrect_concept_links": [
        {"formula_id": "string", "issue": "string"}
    ]
}

Return ONLY valid JSON. No markdown. No explanation.
"""


def build_generation_prompt(notes: str, concepts: List[Dict[str, Any]]) -> str:
    concept_summary = [
        {"concept_id": c["concept_id"], "concept_name": c["concept_name"], "definition": c["definition"]}
        for c in concepts
    ]
    return (
        f"Teacher Notes:\n\n{notes}\n\n"
        f"Concept Database (JSON):\n{json.dumps(concept_summary, indent=2, ensure_ascii=False)}\n\n"
        f"Generate formulas linked to these concept_ids only."
    )


def build_audit_prompt(notes: str, formulas: List[Dict[str, Any]]) -> str:
    return (
        f"Teacher Notes:\n\n{notes}\n\n"
        f"Current Formulas (JSON):\n{json.dumps(formulas, indent=2, ensure_ascii=False)}\n\n"
        f"Perform the Formula Coverage Audit now."
    )


def validate_formula_item(item: Any, known_ids: Set[str]) -> None:
    if not isinstance(item, dict):
        raise ValueError("formula item is not an object")
    missing = [f for f in REQUIRED_FIELDS if f not in item]
    if missing:
        raise ValueError(f"formula item missing field(s): {missing}")
    if item["formula_id"] in known_ids:
        raise ValueError(f"duplicate formula_id '{item['formula_id']}' in response")


def make_generation_validator(concept_ids: Set[str]):
    def validator(parsed: Any) -> None:
        if not isinstance(parsed, list) or not parsed:
            raise ValueError("Response is not a non-empty JSON array")
        seen: Set[str] = set()
        for item in parsed:
            validate_formula_item(item, seen)
            seen.add(item["formula_id"])
    return validator


def make_audit_validator(existing_ids: Set[str]):
    def validator(parsed: Any) -> None:
        utils.validate_json(parsed, ["missing_formulas", "duplicate_formulas", "incorrect_concept_links"])
        if not isinstance(parsed["missing_formulas"], list):
            raise ValueError("'missing_formulas' is not a list")
        seen: Set[str] = set()
        for item in parsed["missing_formulas"]:
            validate_formula_item(item, seen)
            seen.add(item["formula_id"])
    return validator


def sanitize_str_list(value: Any) -> List[str]:
    if not isinstance(value, list):
        return []
    return [v for v in value if isinstance(v, str) and v.strip()]


def sanitize_variables(value: Any) -> List[Dict[str, str]]:
    if not isinstance(value, list):
        return []
    variables = []
    for v in value:
        if isinstance(v, dict) and isinstance(v.get("symbol"), str) and v["symbol"].strip():
            variables.append({
                "symbol": v["symbol"].strip(),
                "meaning": v.get("meaning") if isinstance(v.get("meaning"), str) else "",
                "unit": v.get("unit") if isinstance(v.get("unit"), str) else "",
            })
    return variables


def sanitize_formula(item: Dict[str, Any], known_concept_ids: Set[str]) -> Optional[Dict[str, Any]]:
    retrieval = item.get("retrieval") or {}
    linked_concepts = [c for c in sanitize_str_list(item.get("linked_concepts")) if c in known_concept_ids]

    if not linked_concepts:
        LOGGER.warning(f"Dropping formula '{item.get('formula_id')}': no valid linked_concepts")
        return None

    formula_type = item.get("formula_type")
    if formula_type not in FORMULA_TYPES:
        formula_type = "Relation"

    return {
        "formula_id": item["formula_id"],
        "formula_name": item.get("formula_name", ""),
        "formula_type": formula_type,
        "expression": item.get("expression", ""),
        "latex": item.get("latex", ""),
        "description": item.get("description", ""),
        "variables": sanitize_variables(item.get("variables")),
        "linked_concepts": linked_concepts,
        "derived_from": sanitize_str_list(item.get("derived_from")),
        "common_mistakes": sanitize_str_list(item.get("common_mistakes")),
        "retrieval": {
            "keywords": sanitize_str_list(retrieval.get("keywords")),
            "chunk_ids": sanitize_str_list(retrieval.get("chunk_ids")),
            "pyq_ids": sanitize_str_list(retrieval.get("pyq_ids")),
        },
    }


def normalize_expression(expression: str) -> str:
    return re.sub(r"\s+", "", expression or "")


def unique_formula_id(candidate: str, taken_ids: Set[str]) -> str:
    if candidate not in taken_ids:
        return candidate
    suffix = 2
    while f"{candidate}_{suffix}" in taken_ids:
        suffix += 1
    return f"{candidate}_{suffix}"


def run_stage1(notes: str, concepts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    concept_ids = {c["concept_id"] for c in concepts}

    parsed = utils.call_llm_json(
        system_prompt=get_formula_prompt(),
        user_prompt=build_generation_prompt(notes, concepts),
        logger=LOGGER,
        validator=make_generation_validator(concept_ids),
        raw_dump_filename="formula_generator_stage1_raw_output.txt",
    )

    formulas = []
    for item in parsed:
        sanitized = sanitize_formula(item, concept_ids)
        if sanitized:
            formulas.append(sanitized)
    return formulas


def run_stage2(notes: str, concepts: List[Dict[str, Any]], formulas: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    concept_ids = {c["concept_id"] for c in concepts}
    existing_ids = {f["formula_id"] for f in formulas}
    existing_expressions = {normalize_expression(f["expression"]) for f in formulas}

    system_prompt = get_formula_prompt() + AUDIT_INSTRUCTIONS

    try:
        parsed = utils.call_llm_json(
            system_prompt=system_prompt,
            user_prompt=build_audit_prompt(notes, formulas),
            logger=LOGGER,
            validator=make_audit_validator(existing_ids),
            raw_dump_filename="formula_generator_stage2_raw_output.txt",
        )
    except Exception as e:
        LOGGER.warning(f"Formula coverage audit failed, keeping Stage 1 output only: {e}")
        return formulas

    for fid in parsed.get("duplicate_formulas", []):
        LOGGER.warning(f"Audit flagged possible duplicate formula: {fid}")
    for issue in parsed.get("incorrect_concept_links", []):
        LOGGER.warning(f"Audit flagged incorrect concept link: {issue}")

    added = 0
    for item in parsed["missing_formulas"]:
        sanitized = sanitize_formula(item, concept_ids)
        if not sanitized:
            continue
        if normalize_expression(sanitized["expression"]) in existing_expressions:
            LOGGER.warning(f"Skipping audit formula '{sanitized['formula_id']}': expression already covered")
            continue

        sanitized["formula_id"] = unique_formula_id(sanitized["formula_id"], existing_ids)
        existing_ids.add(sanitized["formula_id"])
        existing_expressions.add(normalize_expression(sanitized["expression"]))
        formulas.append(sanitized)
        added += 1

    LOGGER.info(f"Coverage audit appended {added} missing formula(s)")
    return formulas


def process_chapter(notes_path: Path) -> Optional[Path]:
    chapter = utils.chapter_key(notes_path)
    LOGGER.info(f"=== Formula generation: {chapter} ===")

    concepts_path = utils.CONCEPTS_DIR / f"{chapter}.json"
    if not concepts_path.exists():
        LOGGER.error(f"Skipping '{chapter}': {concepts_path} not found (run concept_generator.py first)")
        return None

    notes = utils.read_text(notes_path)
    concepts = utils.load_json(concepts_path)

    try:
        formulas = run_stage1(notes, concepts)
    except Exception as e:
        LOGGER.error(f"Formula generation (Stage 1) failed for '{chapter}': {e}")
        return None

    LOGGER.info(f"Stage 1 produced {len(formulas)} formula(s)")

    formulas = run_stage2(notes, concepts, formulas)

    out_path = utils.FORMULAS_DIR / f"{chapter}.json"
    utils.save_json(formulas, out_path)
    LOGGER.info(f"Saved {len(formulas)} formula(s) to {out_path}")
    return out_path


def main() -> None:
    chapter_arg = sys.argv[1] if len(sys.argv) > 1 else None
    notes_files = utils.resolve_chapters(chapter_arg)

    LOGGER.info("=" * 80)
    LOGGER.info(f"FORMULA GENERATOR -- {len(notes_files)} chapter(s)")
    LOGGER.info("=" * 80)

    for notes_path in notes_files:
        process_chapter(notes_path)


if __name__ == "__main__":
    main()
