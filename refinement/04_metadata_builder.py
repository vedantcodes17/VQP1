"""
04_metadata_builder.py

Pass 4 of the Concept Intelligence Engine.

Generates educational metadata for every real (non-grouping) concept:
importance, chapter_weightage, concept_category, concept_type,
learning_objective, prerequisites, difficulty_hint.

Deliberately excluded (deferred to a later phase, per spec): Bloom levels,
PYQs, diagram detection.

Structural grouping nodes introduced in Pass 1 are not real teachable
units, so they get lightweight programmatic defaults instead of being sent
to the LLM.

Role played by the LLM: Senior Chemistry Teacher.

Input:
    output/chapter_concepts_normalized.json  (Pass 2)
    output/chapter_relationships.json        (Pass 3 -- grounds 'prerequisites')
    ../output/chapter_kb.json                 (Phase 1, read-only -- question counts)

Output:
    output/chapter_metadata.json
"""

from __future__ import annotations

from typing import Any, Dict, List, Set

import utils

LOGGER = utils.setup_logger("04_metadata_builder")

MAX_RECONCILE_ROUNDS = 2
BATCH_SIZE = 8

IMPORTANCE_LEVELS = {"high", "medium", "low"}
DIFFICULTY_LEVELS = {"easy", "medium", "hard"}

SYSTEM_PROMPT = """You are a Senior Chemistry Teacher assigning exam-relevant metadata to
each concept in one chapter, for use by a question-paper generation system.

You are given a fixed list of real (non-structural) concepts, their
definitions, how many chapter questions reference each one, and any known
prerequisite relationships.

RULES

1. Use ONLY the concept_id values given to you. Do not add, rename, or
   invent concepts.
2. You MUST return exactly one metadata entry per concept_id given to you.
3. importance: one of "high", "medium", "low" -- how central this concept
   is to the chapter as a whole.
4. chapter_weightage: one of "high", "medium", "low" -- how often this
   concept is likely to be examined, informed by the given question count.
5. concept_category: a short label such as "Core Concept", "Law/Formula",
   "Definition", "Property/Classification", or "Application".
6. concept_type: a short label such as "Conceptual", "Numerical",
   "Factual", or "Law".
7. learning_objective: one sentence starting "Students should be able to...".
8. prerequisites: concept_id values (from the given list ONLY) that a
   student should understand before this concept. Empty list if none.
9. difficulty_hint: one of "easy", "medium", "hard" -- a lightweight
   difficulty signal only (do NOT produce a formal Bloom's taxonomy level).
10. Never invent facts not implied by the given definitions.
11. Return ONLY valid JSON. No markdown. No explanation. No code fences.

Output schema:

{
    "concept_metadata": [
        {
            "concept_id": "",
            "importance": "",
            "chapter_weightage": "",
            "concept_category": "",
            "concept_type": "",
            "learning_objective": "",
            "prerequisites": [],
            "difficulty_hint": ""
        }
    ]
}
"""

USER_PROMPT_TEMPLATE = """Concepts to assign metadata to (you MUST cover every one of these, using
the exact concept_id values):

{concept_list}
"""


def compute_question_counts(kb_doc: Dict[str, Any]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for question in kb_doc.get("question_bank", []):
        for cid in question.get("linked_concepts", []):
            counts[cid] = counts.get(cid, 0) + 1
    return counts


def compute_known_prerequisites(relationships: List[Dict[str, Any]]) -> Dict[str, List[str]]:
    prereqs: Dict[str, List[str]] = {}
    for rel in relationships:
        if rel["relationship_type"] in ("prerequisite", "depends_on"):
            prereqs.setdefault(rel["source_concept_id"], []).append(rel["target_concept_id"])
    return prereqs


def format_concept_list(
    concepts: List[Dict[str, Any]],
    nodes_by_id: Dict[str, Dict[str, Any]],
    question_counts: Dict[str, int],
    known_prereqs: Dict[str, List[str]],
) -> str:
    lines = []
    for c in concepts:
        node = nodes_by_id.get(c["concept_id"], {})
        definition = node.get("definition", "").strip()
        q_count = question_counts.get(c["concept_id"], 0)
        prereq_hint = known_prereqs.get(c["concept_id"], [])

        lines.append(f"- {c['concept_id']}: {c['concept_name']} (questions referencing this: {q_count})")
        if definition:
            lines.append(f"  Definition: {definition}")
        if prereq_hint:
            lines.append(f"  Known prerequisite links: {', '.join(prereq_hint)}")

    return "\n".join(lines)


def build_user_prompt(
    concepts: List[Dict[str, Any]],
    nodes_by_id: Dict[str, Dict[str, Any]],
    question_counts: Dict[str, int],
    known_prereqs: Dict[str, List[str]],
) -> str:
    return USER_PROMPT_TEMPLATE.format(
        concept_list=format_concept_list(concepts, nodes_by_id, question_counts, known_prereqs)
    )


def normalize_enum(value: str, allowed: Set[str], default: str) -> str:
    key = value.strip().lower()
    return key if key in allowed else default


def make_validator(valid_ids: Set[str]):
    def validator(parsed: Any) -> None:
        utils.validate_json(parsed, ["concept_metadata"])

        if not isinstance(parsed["concept_metadata"], list):
            raise ValueError("'concept_metadata' is not a list")

        for i, item in enumerate(parsed["concept_metadata"]):
            if not isinstance(item, dict):
                raise ValueError(f"concept_metadata[{i}] is not an object")

            if "concept_id" not in item or item["concept_id"] not in valid_ids:
                raise ValueError(f"concept_metadata[{i}] missing/unknown 'concept_id'")

            for field in (
                "importance", "chapter_weightage", "concept_category",
                "concept_type", "learning_objective", "difficulty_hint",
            ):
                if field not in item or not isinstance(item[field], str):
                    raise ValueError(f"concept_metadata[{i}] missing/invalid '{field}'")

            if "prerequisites" not in item or not isinstance(item["prerequisites"], list):
                raise ValueError(f"concept_metadata[{i}] missing/invalid 'prerequisites'")

    return validator


def default_metadata(concept: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "concept_id": concept["concept_id"],
        "importance": "medium",
        "chapter_weightage": "medium",
        "concept_category": "Core Concept",
        "concept_type": "Conceptual",
        "learning_objective": f"Students should be able to explain {concept['concept_name']}.",
        "prerequisites": [],
        "difficulty_hint": "medium",
    }


def grouping_node_metadata(concept: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "concept_id": concept["concept_id"],
        "concept_name": concept["concept_name"],
        "importance": "medium",
        "chapter_weightage": "low",
        "concept_category": "Grouping / Organisational Node",
        "concept_type": "Category",
        "learning_objective": "",
        "prerequisites": [],
        "difficulty_hint": "",
    }


def build_metadata() -> Dict[str, Any]:
    normalized_doc = utils.load_json(utils.NORMALIZED_FILE)
    concept_tree = normalized_doc["concept_tree"]
    valid_ids = {c["concept_id"] for c in concept_tree}

    real_concepts = [c for c in concept_tree if not c.get("is_grouping_node")]
    grouping_concepts = [c for c in concept_tree if c.get("is_grouping_node")]
    LOGGER.info(f"{len(real_concepts)} real concepts, {len(grouping_concepts)} grouping node(s)")

    _, kb_doc = utils.load_phase1_inputs()
    nodes_by_id = {n["concept_id"]: n for n in kb_doc.get("knowledge_nodes", [])}
    question_counts = compute_question_counts(kb_doc)

    relationships_doc = utils.load_json(utils.RELATIONSHIPS_FILE)
    known_prereqs = compute_known_prerequisites(relationships_doc.get("relationships", []))

    metadata_by_id: Dict[str, Dict[str, Any]] = {}

    batches = [
        real_concepts[i:i + BATCH_SIZE]
        for i in range(0, len(real_concepts), BATCH_SIZE)
    ]
    LOGGER.info(f"Processing {len(real_concepts)} concept(s) in {len(batches)} batch(es) of up to {BATCH_SIZE}")

    for batch_num, batch in enumerate(batches, start=1):
        remaining = list(batch)
        round_num = 0

        while remaining and round_num <= MAX_RECONCILE_ROUNDS:
            round_num += 1
            LOGGER.info(
                f"Batch {batch_num}/{len(batches)}, round {round_num}: "
                f"requesting metadata for {len(remaining)} concept(s)"
            )

            user_prompt = build_user_prompt(remaining, nodes_by_id, question_counts, known_prereqs)
            validator = make_validator(valid_ids)

            parsed = utils.call_llm_json(
                system_prompt=SYSTEM_PROMPT,
                user_prompt=user_prompt,
                logger=LOGGER,
                validator=validator,
                raw_dump_filename=f"04_raw_output_batch{batch_num}_round{round_num}.txt",
            )

            for item in parsed["concept_metadata"]:
                item["importance"] = normalize_enum(item["importance"], IMPORTANCE_LEVELS, "medium")
                item["chapter_weightage"] = normalize_enum(item["chapter_weightage"], IMPORTANCE_LEVELS, "medium")
                item["difficulty_hint"] = normalize_enum(item["difficulty_hint"], DIFFICULTY_LEVELS, "medium")
                item["prerequisites"] = [p for p in item["prerequisites"] if isinstance(p, str) and p in valid_ids]
                metadata_by_id[item["concept_id"]] = item

            remaining = [c for c in batch if c["concept_id"] not in metadata_by_id]

            if remaining:
                LOGGER.warning(
                    f"Batch {batch_num}: {len(remaining)} concept(s) still missing after round {round_num}: "
                    f"{[c['concept_id'] for c in remaining]}"
                )

        if remaining:
            LOGGER.warning(
                f"Batch {batch_num}: filling {len(remaining)} concept(s) with default metadata after "
                f"{MAX_RECONCILE_ROUNDS} reconciliation round(s)"
            )
            for concept in remaining:
                metadata_by_id[concept["concept_id"]] = default_metadata(concept)

    concept_metadata = []
    for concept in concept_tree:
        if concept.get("is_grouping_node"):
            concept_metadata.append(grouping_node_metadata(concept))
        else:
            entry = dict(metadata_by_id[concept["concept_id"]])
            entry["concept_name"] = concept["concept_name"]
            concept_metadata.append(entry)

    return {
        "chapter": normalized_doc.get("chapter", ""),
        "concept_metadata": concept_metadata,
    }


def main() -> None:
    LOGGER.info("=" * 80)
    LOGGER.info("METADATA BUILDER (PASS 4)")
    LOGGER.info("=" * 80)

    result = build_metadata()

    utils.save_json(result, utils.METADATA_FILE)
    LOGGER.info(f"Saved: {utils.METADATA_FILE}")

    LOGGER.info("Summary")
    LOGGER.info(f"  Concepts with metadata : {len(result['concept_metadata'])}")

    importance_counts: Dict[str, int] = {}
    for m in result["concept_metadata"]:
        importance_counts[m["importance"]] = importance_counts.get(m["importance"], 0) + 1
    for level, count in sorted(importance_counts.items()):
        LOGGER.info(f"    importance={level:8s} : {count}")


if __name__ == "__main__":
    main()
