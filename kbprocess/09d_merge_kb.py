"""
09d_merge_kb.py

Merges the three intermediate artefacts produced by 09a/09b/09c into the
final canonical Chapter Knowledge Base.

Input:
    output/chapter_concepts.json
    output/chapter_nodes.json
    output/chapter_questions.json

Output:
    output/chapter_kb.json
"""

from __future__ import annotations

from typing import Any, Dict

import utils

LOGGER = utils.setup_logger("09d_merge_kb")


def validate_concepts_doc(doc: Any) -> None:
    if not isinstance(doc, dict) or "chapter" not in doc or "concept_tree" not in doc:
        raise ValueError(f"{utils.CONCEPTS_FILE} is missing required fields")


def validate_nodes_doc(doc: Any) -> None:
    if not isinstance(doc, dict) or "knowledge_nodes" not in doc:
        raise ValueError(f"{utils.NODES_FILE} is missing required fields")


def validate_questions_doc(doc: Any) -> None:
    if not isinstance(doc, dict) or "question_bank" not in doc:
        raise ValueError(f"{utils.QUESTIONS_FILE} is missing required fields")


def cross_check_concept_ids(concepts_doc: Dict[str, Any], nodes_doc: Dict[str, Any], questions_doc: Dict[str, Any]) -> None:
    valid_ids = {c["concept_id"] for c in concepts_doc["concept_tree"]}

    node_ids = {n["concept_id"] for n in nodes_doc["knowledge_nodes"]}
    missing_nodes = valid_ids - node_ids
    if missing_nodes:
        LOGGER.warning(f"{len(missing_nodes)} concept(s) have no knowledge node: {sorted(missing_nodes)}")

    extra_nodes = node_ids - valid_ids
    if extra_nodes:
        LOGGER.warning(f"{len(extra_nodes)} knowledge node(s) reference unknown concept_id(s): {sorted(extra_nodes)}")

    for q in questions_doc["question_bank"]:
        unknown = [cid for cid in q["linked_concepts"] if cid not in valid_ids]
        if unknown:
            LOGGER.warning(f"{q['question_id']} links to unknown concept_id(s): {unknown}")


def merge_kb() -> Dict[str, Any]:
    LOGGER.info(f"Loading {utils.CONCEPTS_FILE}")
    concepts_doc = utils.load_json(utils.CONCEPTS_FILE)
    validate_concepts_doc(concepts_doc)

    LOGGER.info(f"Loading {utils.NODES_FILE}")
    nodes_doc = utils.load_json(utils.NODES_FILE)
    validate_nodes_doc(nodes_doc)

    LOGGER.info(f"Loading {utils.QUESTIONS_FILE}")
    questions_doc = utils.load_json(utils.QUESTIONS_FILE)
    validate_questions_doc(questions_doc)

    cross_check_concept_ids(concepts_doc, nodes_doc, questions_doc)

    return {
        "chapter": concepts_doc["chapter"],
        "concept_tree": concepts_doc["concept_tree"],
        "knowledge_nodes": nodes_doc["knowledge_nodes"],
        "question_bank": questions_doc["question_bank"],
    }


def main() -> None:
    LOGGER.info("=" * 80)
    LOGGER.info("MERGE KNOWLEDGE BASE")
    LOGGER.info("=" * 80)

    result = merge_kb()

    utils.save_json(result, utils.KB_FILE)
    LOGGER.info(f"Saved: {utils.KB_FILE}")

    LOGGER.info("Summary")
    LOGGER.info(f"  Chapter         : {result['chapter']}")
    LOGGER.info(f"  Concept Tree    : {len(result['concept_tree'])}")
    LOGGER.info(f"  Knowledge Nodes : {len(result['knowledge_nodes'])}")
    LOGGER.info(f"  Question Bank   : {len(result['question_bank'])}")


if __name__ == "__main__":
    main()
