"""
03_relationship_builder.py

Pass 3 of the Concept Intelligence Engine.

Builds semantic graph relationships between concepts -- distinct from the
parent-child hierarchy already established in Pass 1. These are cross-tree
edges (e.g. "Raoult's Law" depends_on "Vapour Pressure" even though they
sit in different branches of the hierarchy).

Role played by the LLM: Knowledge Graph Engineer.

Input:
    output/chapter_concepts_normalized.json  (Pass 2)

Output:
    output/chapter_relationships.json
"""

from __future__ import annotations

from typing import Any, Dict, List, Set, Tuple

import utils

LOGGER = utils.setup_logger("03_relationship_builder")

SUPPORTED_RELATIONSHIP_TYPES = {
    "depends_on",
    "prerequisite",
    "related_to",
    "used_in",
    "part_of",
    "contains",
    "example_of",
}

SYSTEM_PROMPT = """You are a Knowledge Graph Engineer building semantic relationships between
the concepts of one chapter.

You are given a fixed list of concepts (concept_id + concept_name +
definition) and each concept's CURRENT parent in the hierarchy tree.

RULES

1. Use ONLY the concept_id values given to you as source_concept_id and
   target_concept_id. Never invent a concept_id.
2. Do NOT restate the existing parent-child hierarchy as relationships --
   only add semantic edges that are NOT already implied by the given
   parent links.
3. relationship_type must be exactly one of:
   - "depends_on"   (understanding source requires target)
   - "prerequisite" (target must be learned before source)
   - "related_to"   (conceptually connected, no strict dependency)
   - "used_in"      (source is applied/used within target)
   - "part_of"      (source is a component of target, outside the tree)
   - "contains"      (source contains target, outside the tree)
   - "example_of"   (source is a specific example/instance of target)
4. A relationship must connect two DIFFERENT concepts. Never link a concept
   to itself.
5. Only propose relationships that are actually supported by the given
   definitions -- never invent connections with no basis in the text.
6. Be thorough. A chapter like this typically has 2-4 relationships PER
   CONCEPT once you consider dependencies, applications, and examples --
   a sparse handful of edges for the whole chapter is almost always
   under-generation, not a genuinely simple chapter. Systematically check
   each concept against every other concept's definition for a plausible
   connection before finishing.
7. Return ONLY valid JSON. No markdown. No explanation. No code fences.

Worked example of the level of thoroughness expected (illustrative concept
IDs only, not this chapter's real ones):

{
    "relationships": [
        {"source_concept_id": "X_014", "relationship_type": "depends_on", "target_concept_id": "X_012"},
        {"source_concept_id": "X_014", "relationship_type": "used_in", "target_concept_id": "X_017"},
        {"source_concept_id": "X_016", "relationship_type": "example_of", "target_concept_id": "X_015"},
        {"source_concept_id": "X_022", "relationship_type": "related_to", "target_concept_id": "X_023"},
        {"source_concept_id": "X_021", "relationship_type": "contains", "target_concept_id": "X_022"}
    ]
}

Output schema:

{
    "relationships": [
        {
            "source_concept_id": "",
            "relationship_type": "",
            "target_concept_id": ""
        }
    ]
}
"""

USER_PROMPT_TEMPLATE = """Concepts (with current hierarchy parent, for context only -- do not restate
these as relationships):

{concept_list}

Propose semantic relationships between these concepts using ONLY the
concept_id values shown above.
"""


def format_concept_list(concepts: List[Dict[str, Any]], nodes_by_id: Dict[str, Dict[str, Any]]) -> str:
    lines = []
    for c in concepts:
        node = nodes_by_id.get(c["concept_id"], {})
        definition = node.get("definition", "").strip()
        parent = c.get("parent_concept", "")
        lines.append(f"- {c['concept_id']}: {c['concept_name']} (parent: {parent or 'none'})")
        if definition:
            lines.append(f"  Definition: {definition}")
    return "\n".join(lines)


def build_user_prompt(concepts: List[Dict[str, Any]], nodes_by_id: Dict[str, Dict[str, Any]]) -> str:
    return USER_PROMPT_TEMPLATE.format(concept_list=format_concept_list(concepts, nodes_by_id))


def make_validator(min_expected: int):
    def validator(parsed: Any) -> None:
        utils.validate_json(parsed, ["relationships"])

        if not isinstance(parsed["relationships"], list):
            raise ValueError("'relationships' is not a list")

        for i, item in enumerate(parsed["relationships"]):
            if not isinstance(item, dict):
                raise ValueError(f"relationships[{i}] is not an object")
            for field in ("source_concept_id", "relationship_type", "target_concept_id"):
                if field not in item or not isinstance(item[field], str):
                    raise ValueError(f"relationships[{i}] missing/invalid '{field}'")

        if len(parsed["relationships"]) < min_expected:
            raise ValueError(
                f"Only {len(parsed['relationships'])} relationship(s) returned; "
                f"expected at least {min_expected} for this many concepts. "
                f"Be more thorough -- check every concept pair for a plausible connection."
            )

    return validator


def clean_relationships(
    raw_relationships: List[Dict[str, Any]],
    valid_ids: Set[str],
) -> Tuple[List[Dict[str, Any]], int]:
    seen: Set[Tuple[str, str, str]] = set()
    cleaned = []
    dropped = 0

    for item in raw_relationships:
        source = item["source_concept_id"]
        target = item["target_concept_id"]
        rel_type = item["relationship_type"].strip().lower().replace(" ", "_").replace("-", "_")

        if source not in valid_ids or target not in valid_ids:
            dropped += 1
            continue
        if rel_type not in SUPPORTED_RELATIONSHIP_TYPES:
            dropped += 1
            continue
        if source == target:
            dropped += 1
            continue

        key = (source, rel_type, target)
        if key in seen:
            dropped += 1
            continue
        seen.add(key)

        cleaned.append({
            "source_concept_id": source,
            "relationship_type": rel_type,
            "target_concept_id": target,
        })

    return cleaned, dropped


def build_relationships() -> Dict[str, Any]:
    normalized_doc = utils.load_json(utils.NORMALIZED_FILE)
    concept_tree = normalized_doc["concept_tree"]
    valid_ids = {c["concept_id"] for c in concept_tree}
    LOGGER.info(f"{len(concept_tree)} concepts loaded from Pass 2 normalization")

    _, kb_doc = utils.load_phase1_inputs()
    nodes_by_id = {n["concept_id"]: n for n in kb_doc.get("knowledge_nodes", [])}

    user_prompt = build_user_prompt(concept_tree, nodes_by_id)
    # A floor that catches genuine under-generation (e.g. a handful of edges
    # for the whole chapter) without demanding more than a local 7B model
    # can realistically sustain across retries.
    min_expected = max(10, len(concept_tree) // 2)

    LOGGER.info("Calling LLM to build relationships...")
    parsed = utils.call_llm_json(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=user_prompt,
        logger=LOGGER,
        validator=make_validator(min_expected),
        raw_dump_filename="03_raw_output.txt",
    )

    cleaned, dropped = clean_relationships(parsed["relationships"], valid_ids)
    if dropped:
        LOGGER.warning(f"Dropped {dropped} invalid/duplicate/self-referencing relationship(s)")

    return {
        "chapter": normalized_doc.get("chapter", ""),
        "relationships": cleaned,
    }


def main() -> None:
    LOGGER.info("=" * 80)
    LOGGER.info("RELATIONSHIP BUILDER (PASS 3)")
    LOGGER.info("=" * 80)

    result = build_relationships()

    utils.save_json(result, utils.RELATIONSHIPS_FILE)
    LOGGER.info(f"Saved: {utils.RELATIONSHIPS_FILE}")

    LOGGER.info("Summary")
    LOGGER.info(f"  Relationships : {len(result['relationships'])}")

    type_counts: Dict[str, int] = {}
    for r in result["relationships"]:
        type_counts[r["relationship_type"]] = type_counts.get(r["relationship_type"], 0) + 1
    for rel_type, count in sorted(type_counts.items()):
        LOGGER.info(f"    {rel_type:15s} : {count}")


if __name__ == "__main__":
    main()
