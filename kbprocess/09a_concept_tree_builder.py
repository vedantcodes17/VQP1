"""
09a_concept_tree_builder.py

Reads teacher notes (data/solution.txt) and produces the canonical
concept tree for the chapter: output/chapter_concepts.json

Role played by the LLM: Senior NCERT textbook author / CBSE curriculum designer.
Goal: extract ONLY the concepts that already exist in the notes, organised
into a parent-child hierarchy, with duplicates merged.

Concept IDs are NOT trusted to the LLM. They are assigned deterministically
in this script so they stay stable across re-runs.
"""

from __future__ import annotations

from typing import Any, Dict, List

import utils

LOGGER = utils.setup_logger("09a_concept_tree_builder")

CONCEPT_ID_PREFIX = "CHE_SOL"

SYSTEM_PROMPT = """You are a Senior NCERT Textbook Author and CBSE Curriculum Designer.

You are building the canonical concept tree for one chapter, using ONLY the
teacher notes given to you.

RULES

1. Use ONLY concepts that are explicitly present in the notes.
2. Never invent concepts that are not supported by the text.
3. Scan the ENTIRE notes, not just the opening definitions paragraph.
   Concepts are often introduced only inside an answer to a question (e.g.
   Henry's Law, Van't Hoff factor, abnormal molar mass, degree of
   association/dissociation, isotonic/hypertonic/hypotonic solutions). If a
   named law, factor, or property is defined or used anywhere in the notes
   -- including inside Important Questions, Short Answers, or Numericals --
   it is a concept and must be included.
4. Merge duplicate or near-duplicate concepts into a single canonical entry.
5. Use official educational terminology (the standard NCERT/CBSE term for
   the idea), even if the notes use a shorthand or informal phrasing.
6. Organise concepts into a parent-child hierarchy wherever the notes imply
   one (e.g. "Colligative Properties" is a parent of "Elevation in Boiling
   Point"). If a concept has no parent, set parent_concept to an empty string.
7. Do not assign IDs. Only provide concept_name and parent_concept.
8. Return ONLY valid JSON. No markdown. No explanation. No code fences.

Output schema:

{
    "chapter": "<short chapter title inferred from the notes>",
    "concept_tree": [
        {
            "concept_name": "",
            "parent_concept": ""
        }
    ]
}
"""

USER_PROMPT_TEMPLATE = """Build the canonical concept tree for this chapter.

Teacher Notes:

{text}
"""


def build_user_prompt(text: str) -> str:
    return USER_PROMPT_TEMPLATE.format(text=text)


def validate_raw_concepts(parsed: Any) -> None:
    if not isinstance(parsed, dict):
        raise ValueError("Response is not a JSON object")

    if "chapter" not in parsed or not isinstance(parsed["chapter"], str):
        raise ValueError("Missing or invalid 'chapter' field")

    if "concept_tree" not in parsed or not isinstance(parsed["concept_tree"], list):
        raise ValueError("Missing or invalid 'concept_tree' field")

    for i, item in enumerate(parsed["concept_tree"]):
        if not isinstance(item, dict):
            raise ValueError(f"concept_tree[{i}] is not an object")
        if "concept_name" not in item or not isinstance(item["concept_name"], str):
            raise ValueError(f"concept_tree[{i}] missing 'concept_name'")
        if not item["concept_name"].strip():
            raise ValueError(f"concept_tree[{i}] has empty 'concept_name'")
        if "parent_concept" not in item:
            raise ValueError(f"concept_tree[{i}] missing 'parent_concept'")


def dedupe_and_assign_ids(chapter: str, raw_concepts: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Merge duplicate concept names (case/whitespace-insensitive), preserve
    first-seen order, resolve parent references to canonical names, and
    assign stable sequential concept IDs.
    """
    canonical_by_key: Dict[str, str] = {}
    ordered_names: List[str] = []
    parent_by_name: Dict[str, str] = {}

    for item in raw_concepts:
        name = item["concept_name"].strip()
        key = utils.normalize_name(name)

        if key not in canonical_by_key:
            canonical_by_key[key] = name
            ordered_names.append(name)
            parent_by_name[name] = ""

        canonical_name = canonical_by_key[key]

        parent_raw = (item.get("parent_concept") or "").strip()
        if parent_raw and not parent_by_name.get(canonical_name):
            parent_by_name[canonical_name] = parent_raw

    # Resolve parents to canonical names; drop parents that do not match any
    # known concept (never invent new concepts, including as parents).
    name_lookup = {utils.normalize_name(n): n for n in ordered_names}

    concept_tree = []
    for index, name in enumerate(ordered_names, start=1):
        concept_id = f"{CONCEPT_ID_PREFIX}_{index:03d}"

        parent_raw = parent_by_name.get(name, "")
        parent_key = utils.normalize_name(parent_raw) if parent_raw else ""

        if parent_key and parent_key != utils.normalize_name(name) and parent_key in name_lookup:
            parent_concept = name_lookup[parent_key]
        else:
            parent_concept = ""

        concept_tree.append({
            "concept_id": concept_id,
            "concept_name": name,
            "parent_concept": parent_concept,
        })

    return {
        "chapter": chapter,
        "concept_tree": concept_tree,
    }


def build_concept_tree() -> Dict[str, Any]:
    LOGGER.info(f"Loading input file: {utils.SOLUTION_FILE}")
    raw_text = utils.load_text_file(utils.SOLUTION_FILE)
    LOGGER.info(f"Loaded {len(raw_text):,} characters")

    text = utils.preprocess_text(raw_text)
    LOGGER.info(f"Preprocessed to {len(text):,} characters")

    user_prompt = build_user_prompt(text)

    LOGGER.info("Calling LLM to extract concept tree...")
    parsed = utils.call_llm_json(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=user_prompt,
        logger=LOGGER,
        validator=validate_raw_concepts,
        raw_dump_filename="09a_raw_output.txt",
    )

    LOGGER.info(f"Received {len(parsed['concept_tree'])} raw concept entries; deduping...")
    result = dedupe_and_assign_ids(parsed["chapter"], parsed["concept_tree"])
    LOGGER.info(f"Final concept count after dedupe: {len(result['concept_tree'])}")

    return result


def main() -> None:
    LOGGER.info("=" * 80)
    LOGGER.info("CONCEPT TREE BUILDER")
    LOGGER.info("=" * 80)

    result = build_concept_tree()

    utils.save_json(result, utils.CONCEPTS_FILE)
    LOGGER.info(f"Saved: {utils.CONCEPTS_FILE}")

    LOGGER.info("Summary")
    LOGGER.info(f"  Chapter        : {result['chapter']}")
    LOGGER.info(f"  Concept Count  : {len(result['concept_tree'])}")


if __name__ == "__main__":
    main()
