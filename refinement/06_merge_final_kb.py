"""
06_merge_final_kb.py

Pass 6 (final) of the Concept Intelligence Engine.

Pure Python merge -- no LLM. Combines every prior pass's output into the
final canonical chapter knowledge base:

    Pass 2 (hierarchy + normalization) + Pass 4 (metadata)
        -> merged concept_tree
    Pass 3 (relationships)
        -> relationships
    Pass 5 (refined questions)
        -> question_bank

Output:
    output/chapter_kb_final.json
"""

from __future__ import annotations

from typing import Any, Dict, List

import utils

LOGGER = utils.setup_logger("06_merge_final_kb")


def merge_concept_tree(
    normalized_tree: List[Dict[str, Any]],
    metadata_list: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    metadata_by_id = {m["concept_id"]: m for m in metadata_list}

    normalized_ids = {c["concept_id"] for c in normalized_tree}
    metadata_ids = set(metadata_by_id.keys())

    missing_metadata = normalized_ids - metadata_ids
    if missing_metadata:
        LOGGER.warning(f"{len(missing_metadata)} concept(s) have no metadata entry: {sorted(missing_metadata)}")

    extra_metadata = metadata_ids - normalized_ids
    if extra_metadata:
        LOGGER.warning(f"Metadata references unknown concept_id(s), ignoring: {sorted(extra_metadata)}")

    merged = []
    for concept in normalized_tree:
        metadata = metadata_by_id.get(concept["concept_id"], {})
        merged.append({
            "concept_id": concept["concept_id"],
            "concept_name": concept["concept_name"],
            "parent_concept": concept["parent_concept"],
            "is_grouping_node": concept["is_grouping_node"],
            "official_name": concept.get("official_name", concept["concept_name"]),
            "aliases": concept.get("aliases", []),
            "search_terms": concept.get("search_terms", []),
            "abbreviations": concept.get("abbreviations", []),
            "importance": metadata.get("importance", "medium"),
            "chapter_weightage": metadata.get("chapter_weightage", "medium"),
            "concept_category": metadata.get("concept_category", ""),
            "concept_type": metadata.get("concept_type", ""),
            "learning_objective": metadata.get("learning_objective", ""),
            "prerequisites": metadata.get("prerequisites", []),
            "difficulty_hint": metadata.get("difficulty_hint", ""),
        })

    return merged


def cross_check(
    concept_tree: List[Dict[str, Any]],
    relationships: List[Dict[str, Any]],
    question_bank: List[Dict[str, Any]],
) -> None:
    valid_ids = {c["concept_id"] for c in concept_tree}

    bad_relationships = [
        r for r in relationships
        if r["source_concept_id"] not in valid_ids or r["target_concept_id"] not in valid_ids
    ]
    if bad_relationships:
        LOGGER.warning(f"{len(bad_relationships)} relationship(s) reference unknown concept_id(s)")

    for question in question_bank:
        unknown = [cid for cid in question.get("linked_concepts", []) if cid not in valid_ids]
        if unknown:
            LOGGER.warning(f"{question['question_id']} links to unknown concept_id(s): {unknown}")

    unanswered = sum(1 for q in question_bank if not q.get("answer"))
    if unanswered:
        LOGGER.info(f"{unanswered}/{len(question_bank)} refined question(s) have no answer text available")


def merge_final_kb() -> Dict[str, Any]:
    normalized_doc = utils.load_json(utils.NORMALIZED_FILE)
    metadata_doc = utils.load_json(utils.METADATA_FILE)
    relationships_doc = utils.load_json(utils.RELATIONSHIPS_FILE)
    questions_doc = utils.load_json(utils.QUESTIONS_REFINED_FILE)

    concept_tree = merge_concept_tree(normalized_doc["concept_tree"], metadata_doc["concept_metadata"])
    relationships = relationships_doc["relationships"]
    question_bank = questions_doc["question_bank"]

    cross_check(concept_tree, relationships, question_bank)

    return {
        "chapter": normalized_doc.get("chapter", ""),
        "concept_tree": concept_tree,
        "relationships": relationships,
        "question_bank": question_bank,
    }


def main() -> None:
    LOGGER.info("=" * 80)
    LOGGER.info("MERGE FINAL KNOWLEDGE BASE (PASS 6)")
    LOGGER.info("=" * 80)

    result = merge_final_kb()

    utils.save_json(result, utils.FINAL_KB_FILE)
    LOGGER.info(f"Saved: {utils.FINAL_KB_FILE}")

    LOGGER.info("Summary")
    LOGGER.info(f"  Chapter       : {result['chapter']}")
    LOGGER.info(f"  Concept Tree  : {len(result['concept_tree'])}")
    LOGGER.info(f"  Relationships : {len(result['relationships'])}")
    LOGGER.info(f"  Question Bank : {len(result['question_bank'])}")


if __name__ == "__main__":
    main()
