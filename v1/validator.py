"""
validator.py

Validates one chapter's generated concepts/formulas in two parts:

    Part 1 - Static Validation (pure Python, no LLM)
        Concept checks, formula checks, and cross-file reference checks.

    Part 2 - LLM Educational Audit
        Compares Teacher Notes against Concept JSON and Formula JSON to
        flag missing content and weak/generic fields. Read-only: it never
        modifies concepts or formulas, it only reports.

Output: reports/<chapter>_validation.json

Usage:
    python validator.py              # every chapter with concepts+formulas
    python validator.py Solutions    # just the "solutions" chapter
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Set

import utils

LOGGER = utils.setup_logger("validator")

RELATIONSHIP_TYPES = {"is_subtopic_of", "requires", "commonly_confused_with"}

AUDIT_SYSTEM_PROMPT = """You are a Senior NCERT Curriculum Reviewer performing an educational
quality audit.

You are given:
- Teacher Notes (the original raw chapter source)
- Concept JSON (already extracted concepts)
- Formula JSON (already extracted formulas)

Compare them and identify ONLY:

- missing_concepts: concept names clearly present in the Teacher Notes but
  absent from Concept JSON.
- missing_formulas: formulas clearly present in the Teacher Notes but
  absent from Formula JSON.
- incorrect_relationships: concept_id/relationship pairs in Concept JSON
  that look wrong given the Teacher Notes.
- weak_learning_outcomes: concept_ids whose learning_outcomes are too
  generic or don't match the Teacher Notes content.
- weak_common_mistakes: concept_ids whose common_mistakes are generic
  (e.g. "students don't study") rather than concept-specific.
- weak_aliases: concept_ids whose aliases are too broad/generic (e.g. a
  subject name rather than an alternate term for the concept itself).

Do NOT modify or regenerate any concept or formula. Only report findings,
each as a short string.

Return ONLY

{
    "missing_concepts": ["string"],
    "missing_formulas": ["string"],
    "incorrect_relationships": ["string"],
    "weak_learning_outcomes": ["string"],
    "weak_common_mistakes": ["string"],
    "weak_aliases": ["string"]
}

Return ONLY valid JSON. No markdown. No explanation.
"""

AUDIT_FIELDS = [
    "missing_concepts",
    "missing_formulas",
    "incorrect_relationships",
    "weak_learning_outcomes",
    "weak_common_mistakes",
    "weak_aliases",
]


# ==========================================================
# PART 1 -- STATIC VALIDATION
# ==========================================================

def find_duplicates(values: List[str]) -> List[str]:
    return sorted({v for v in values if values.count(v) > 1})


def validate_concepts_static(concepts: List[Dict[str, Any]]) -> Dict[str, Any]:
    ids = [c.get("concept_id", "") for c in concepts]
    names = [c.get("concept_name", "") for c in concepts]
    known_ids = set(ids)

    invalid_relationships = []
    for c in concepts:
        for r in c.get("relationships", []):
            if r.get("type") not in RELATIONSHIP_TYPES or r.get("target") not in known_ids:
                invalid_relationships.append({"concept_id": c.get("concept_id"), "relationship": r})

    return {
        "duplicate_ids": find_duplicates(ids),
        "duplicate_names": find_duplicates(names),
        "missing_definition": [c["concept_id"] for c in concepts if not (c.get("definition") or "").strip()],
        "missing_aliases": [c["concept_id"] for c in concepts if not (c.get("aliases_and_keywords") or {}).get("aliases")],
        "missing_keywords": [c["concept_id"] for c in concepts if not (c.get("aliases_and_keywords") or {}).get("keywords")],
        "missing_learning_outcomes": [c["concept_id"] for c in concepts if not c.get("learning_outcomes")],
        "missing_common_mistakes": [c["concept_id"] for c in concepts if not c.get("common_mistakes")],
        "invalid_relationships": invalid_relationships,
    }


def is_valid_latex(latex: str) -> bool:
    if not (latex or "").strip():
        return False
    if latex.count("{") != latex.count("}"):
        return False
    if latex.count("$") % 2 != 0:
        return False
    return True


def validate_formulas_static(formulas: List[Dict[str, Any]], known_concept_ids: Set[str]) -> Dict[str, Any]:
    ids = [f.get("formula_id", "") for f in formulas]
    names = [f.get("formula_name", "") for f in formulas]

    missing_variable_meanings = []
    missing_units = []
    for f in formulas:
        for v in f.get("variables", []):
            if not (v.get("meaning") or "").strip():
                missing_variable_meanings.append({"formula_id": f.get("formula_id"), "symbol": v.get("symbol")})
            if not (v.get("unit") or "").strip():
                missing_units.append({"formula_id": f.get("formula_id"), "symbol": v.get("symbol")})

    invalid_linked_concepts = [
        {"formula_id": f.get("formula_id"), "concept_id": cid}
        for f in formulas
        for cid in f.get("linked_concepts", [])
        if cid not in known_concept_ids
    ]

    invalid_latex = [f["formula_id"] for f in formulas if not is_valid_latex(f.get("latex", ""))]

    expression_groups: Dict[str, List[str]] = {}
    for f in formulas:
        key = re.sub(r"\s+", "", f.get("expression", ""))
        expression_groups.setdefault(key, []).append(f.get("formula_id"))
    duplicate_expressions = [group for group in expression_groups.values() if len(group) > 1]

    return {
        "duplicate_ids": find_duplicates(ids),
        "duplicate_names": find_duplicates(names),
        "missing_variable_meanings": missing_variable_meanings,
        "missing_units": missing_units,
        "invalid_linked_concepts": invalid_linked_concepts,
        "invalid_latex": invalid_latex,
        "duplicate_expressions": duplicate_expressions,
    }


def cross_validate(concepts: List[Dict[str, Any]], formulas: List[Dict[str, Any]]) -> Dict[str, Any]:
    known_concept_ids = {c.get("concept_id") for c in concepts}
    known_formula_ids = {f.get("formula_id") for f in formulas}

    relationship_targets_missing = [
        {"concept_id": c.get("concept_id"), "target": r.get("target")}
        for c in concepts
        for r in c.get("relationships", [])
        if r.get("target") not in known_concept_ids
    ]

    linked_concepts_missing = [
        {"formula_id": f.get("formula_id"), "concept_id": cid}
        for f in formulas
        for cid in f.get("linked_concepts", [])
        if cid not in known_concept_ids
    ]

    derived_from_missing = [
        {"formula_id": f.get("formula_id"), "derived_from": did}
        for f in formulas
        for did in f.get("derived_from", [])
        if did not in known_formula_ids
    ]

    return {
        "relationship_targets_missing": relationship_targets_missing,
        "linked_concepts_missing": linked_concepts_missing,
        "derived_from_missing": derived_from_missing,
    }


def run_static_validation(concepts: List[Dict[str, Any]], formulas: List[Dict[str, Any]]) -> Dict[str, Any]:
    known_concept_ids = {c.get("concept_id") for c in concepts}
    return {
        "concept_validation": validate_concepts_static(concepts),
        "formula_validation": validate_formulas_static(formulas, known_concept_ids),
        "cross_validation": cross_validate(concepts, formulas),
    }


# ==========================================================
# PART 2 -- LLM EDUCATIONAL AUDIT
# ==========================================================

def build_audit_prompt(notes: str, concepts: List[Dict[str, Any]], formulas: List[Dict[str, Any]]) -> str:
    return (
        f"Teacher Notes:\n\n{notes}\n\n"
        f"Concept JSON:\n{json.dumps(concepts, indent=2, ensure_ascii=False)}\n\n"
        f"Formula JSON:\n{json.dumps(formulas, indent=2, ensure_ascii=False)}\n\n"
        f"Perform the educational audit now."
    )


def make_audit_validator():
    def validator(parsed: Any) -> None:
        utils.validate_json(parsed, AUDIT_FIELDS)
        for field in AUDIT_FIELDS:
            if not isinstance(parsed[field], list) or not all(isinstance(v, str) for v in parsed[field]):
                raise ValueError(f"'{field}' must be a list of strings")
    return validator


def run_llm_audit(notes: str, concepts: List[Dict[str, Any]], formulas: List[Dict[str, Any]]) -> Dict[str, Any]:
    try:
        return utils.call_llm_json(
            system_prompt=AUDIT_SYSTEM_PROMPT,
            user_prompt=build_audit_prompt(notes, concepts, formulas),
            logger=LOGGER,
            validator=make_audit_validator(),
            raw_dump_filename="validator_llm_audit_raw_output.txt",
        )
    except Exception as e:
        LOGGER.warning(f"LLM educational audit failed: {e}")
        return {field: [] for field in AUDIT_FIELDS} | {"error": str(e)}


# ==========================================================
# PIPELINE
# ==========================================================

def process_chapter(notes_path: Path) -> None:
    chapter = utils.chapter_key(notes_path)
    LOGGER.info(f"=== Validation: {chapter} ===")

    concepts_path = utils.CONCEPTS_DIR / f"{chapter}.json"
    formulas_path = utils.FORMULAS_DIR / f"{chapter}.json"

    if not concepts_path.exists() or not formulas_path.exists():
        LOGGER.error(f"Skipping '{chapter}': missing {concepts_path.name} or {formulas_path.name}")
        return

    notes = utils.read_text(notes_path)
    concepts = utils.load_json(concepts_path)
    formulas = utils.load_json(formulas_path)

    static_validation = run_static_validation(concepts, formulas)
    llm_audit = run_llm_audit(notes, concepts, formulas)

    report = {
        "chapter": chapter,
        "static_validation": static_validation,
        "llm_audit": llm_audit,
    }

    out_path = utils.REPORTS_DIR / f"{chapter}_validation.json"
    utils.save_json(report, out_path)
    LOGGER.info(f"Saved validation report to {out_path}")


def main() -> None:
    chapter_arg = sys.argv[1] if len(sys.argv) > 1 else None
    notes_files = utils.resolve_chapters(chapter_arg)

    LOGGER.info("=" * 80)
    LOGGER.info(f"VALIDATOR -- {len(notes_files)} chapter(s)")
    LOGGER.info("=" * 80)

    for notes_path in notes_files:
        process_chapter(notes_path)


if __name__ == "__main__":
    main()
