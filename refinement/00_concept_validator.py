"""
00_concept_validator.py

Pass 0 of the Concept Intelligence Engine.

Validates the Phase 1 outputs (chapter_concepts.json, chapter_kb.json)
structurally. This pass NEVER modifies data -- it only detects problems
and writes a validation report. No LLM is used: every check here is a
deterministic, verifiable structural rule, which is exactly the kind of
check an LLM should not be trusted to perform.

Checks performed:
    - schema validation (required fields, correct types)
    - duplicate concept_id values
    - duplicate concept_name values (case/whitespace-insensitive)
    - dangling parent references (parent_concept not in the concept list)
    - circular hierarchy (a parent chain that loops back on itself)
    - orphan concepts (root concepts that are neither a parent of anything
      nor referenced anywhere in knowledge_nodes/question_bank)
    - cross-reference issues against chapter_kb.json (knowledge_nodes /
      question_bank pointing at unknown concept_ids, or concepts with no
      knowledge_node)

Output: output/validation_report.json
"""

from __future__ import annotations

from typing import Any, Dict, List, Set

import utils

LOGGER = utils.setup_logger("00_concept_validator")


def validate_schema(concept_tree: List[Dict[str, Any]]) -> List[str]:
    errors = []
    seen_ids: Set[str] = set()

    for i, concept in enumerate(concept_tree):
        if not isinstance(concept, dict):
            errors.append(f"concept_tree[{i}] is not an object")
            continue

        for field in ("concept_id", "concept_name", "parent_concept"):
            if field not in concept:
                errors.append(f"concept_tree[{i}] missing required field '{field}'")
            elif not isinstance(concept[field], str):
                errors.append(f"concept_tree[{i}].{field} is not a string")

        concept_id = concept.get("concept_id", "")
        if concept_id:
            if concept_id in seen_ids:
                pass  # captured by find_duplicate_ids
            seen_ids.add(concept_id)

        if not concept.get("concept_name", "").strip():
            errors.append(f"concept_tree[{i}] has empty concept_name")

    return errors


def find_duplicate_ids(concept_tree: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    seen: Dict[str, int] = {}
    duplicates = []

    for concept in concept_tree:
        cid = concept.get("concept_id", "")
        seen[cid] = seen.get(cid, 0) + 1

    for cid, count in seen.items():
        if count > 1:
            duplicates.append({"concept_id": cid, "occurrences": count})

    return duplicates


def find_duplicate_concepts(concept_tree: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    by_key: Dict[str, List[str]] = {}

    for concept in concept_tree:
        key = utils.normalize_name(concept.get("concept_name", ""))
        by_key.setdefault(key, []).append(concept.get("concept_id", ""))

    return [
        {"concept_name_key": key, "concept_ids": ids}
        for key, ids in by_key.items()
        if len(ids) > 1
    ]


def find_dangling_parents(concept_tree: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    known_names = {utils.normalize_name(c.get("concept_name", "")) for c in concept_tree}
    dangling = []

    for concept in concept_tree:
        parent = concept.get("parent_concept", "").strip()
        if parent and utils.normalize_name(parent) not in known_names:
            dangling.append({
                "concept_id": concept.get("concept_id", ""),
                "concept_name": concept.get("concept_name", ""),
                "dangling_parent": parent,
            })

    return dangling


def find_orphan_concepts(
    concept_tree: List[Dict[str, Any]],
    kb_doc: Dict[str, Any],
) -> List[Dict[str, Any]]:
    """
    A concept is flagged as an orphan if it has no parent AND is not used as
    a parent by any other concept AND is never referenced by a knowledge
    node or question -- i.e. it is fully disconnected from the rest of the
    knowledge base.
    """
    parent_names_used = {
        utils.normalize_name(c["parent_concept"])
        for c in concept_tree
        if c.get("parent_concept", "").strip()
    }

    referenced_ids: Set[str] = set()
    for node in kb_doc.get("knowledge_nodes", []):
        referenced_ids.add(node.get("concept_id", ""))
    for question in kb_doc.get("question_bank", []):
        referenced_ids.update(question.get("linked_concepts", []))

    orphans = []
    for concept in concept_tree:
        has_no_parent = not concept.get("parent_concept", "").strip()
        is_not_a_parent = utils.normalize_name(concept.get("concept_name", "")) not in parent_names_used
        is_unreferenced = concept.get("concept_id", "") not in referenced_ids

        if has_no_parent and is_not_a_parent and is_unreferenced:
            orphans.append({
                "concept_id": concept.get("concept_id", ""),
                "concept_name": concept.get("concept_name", ""),
            })

    return orphans


def find_cross_reference_issues(
    concept_tree: List[Dict[str, Any]],
    kb_doc: Dict[str, Any],
) -> Dict[str, Any]:
    valid_ids = {c["concept_id"] for c in concept_tree}

    node_ids = {n.get("concept_id", "") for n in kb_doc.get("knowledge_nodes", [])}
    concepts_missing_nodes = sorted(valid_ids - node_ids)
    nodes_with_unknown_ids = sorted(node_ids - valid_ids)

    unknown_question_links = []
    for question in kb_doc.get("question_bank", []):
        unknown = [cid for cid in question.get("linked_concepts", []) if cid not in valid_ids]
        if unknown:
            unknown_question_links.append({
                "question_id": question.get("question_id", ""),
                "unknown_concept_ids": unknown,
            })

    unlinked_questions = [
        q.get("question_id", "")
        for q in kb_doc.get("question_bank", [])
        if not q.get("linked_concepts")
    ]

    return {
        "concepts_missing_knowledge_nodes": concepts_missing_nodes,
        "knowledge_nodes_with_unknown_concept_id": nodes_with_unknown_ids,
        "questions_linking_unknown_concepts": unknown_question_links,
        "questions_with_no_linked_concepts": unlinked_questions,
    }


def build_validation_report(
    concepts_doc: Dict[str, Any],
    kb_doc: Dict[str, Any],
) -> Dict[str, Any]:
    concept_tree = concepts_doc.get("concept_tree", [])

    schema_errors = validate_schema(concept_tree)
    duplicate_ids = find_duplicate_ids(concept_tree)
    duplicate_concepts = find_duplicate_concepts(concept_tree)
    dangling_parents = find_dangling_parents(concept_tree)
    cycles = utils.find_hierarchy_cycles(concept_tree)
    orphans = find_orphan_concepts(concept_tree, kb_doc)
    cross_reference_issues = find_cross_reference_issues(concept_tree, kb_doc)

    total_issues = (
        len(schema_errors)
        + len(duplicate_ids)
        + len(duplicate_concepts)
        + len(dangling_parents)
        + len(cycles)
        + len(cross_reference_issues["knowledge_nodes_with_unknown_concept_id"])
        + len(cross_reference_issues["questions_linking_unknown_concepts"])
    )

    status = "PASS" if total_issues == 0 else "PASS_WITH_WARNINGS"
    # Schema errors, duplicate IDs, and circular hierarchy are hard failures --
    # everything downstream depends on structural soundness.
    if schema_errors or duplicate_ids or cycles:
        status = "FAIL"

    return {
        "chapter": concepts_doc.get("chapter", ""),
        "status": status,
        "summary": {
            "total_concepts": len(concept_tree),
            "schema_errors": len(schema_errors),
            "duplicate_ids": len(duplicate_ids),
            "duplicate_concepts": len(duplicate_concepts),
            "dangling_parents": len(dangling_parents),
            "circular_hierarchies": len(cycles),
            "orphan_concepts": len(orphans),
            "concepts_missing_knowledge_nodes": len(cross_reference_issues["concepts_missing_knowledge_nodes"]),
            "questions_with_no_linked_concepts": len(cross_reference_issues["questions_with_no_linked_concepts"]),
        },
        "schema_errors": schema_errors,
        "duplicate_ids": duplicate_ids,
        "duplicate_concepts": duplicate_concepts,
        "dangling_parents": dangling_parents,
        "circular_hierarchies": cycles,
        "orphan_concepts": orphans,
        "cross_reference_issues": cross_reference_issues,
    }


def main() -> None:
    LOGGER.info("=" * 80)
    LOGGER.info("CONCEPT VALIDATOR (PASS 0)")
    LOGGER.info("=" * 80)

    concepts_doc, kb_doc = utils.load_phase1_inputs()

    report = build_validation_report(concepts_doc, kb_doc)

    utils.save_json(report, utils.VALIDATION_REPORT_FILE)
    LOGGER.info(f"Saved: {utils.VALIDATION_REPORT_FILE}")

    LOGGER.info("Summary")
    LOGGER.info(f"  Status : {report['status']}")
    for key, value in report["summary"].items():
        LOGGER.info(f"  {key:38s}: {value}")

    if report["status"] == "FAIL":
        LOGGER.error(
            "Validation FAILED (structural defects found). "
            "Downstream passes may produce unreliable results until this is fixed."
        )


if __name__ == "__main__":
    main()
