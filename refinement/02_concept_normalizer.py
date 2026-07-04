"""
02_concept_normalizer.py

Pass 2 of the Concept Intelligence Engine.

Adds search/alias metadata to every concept from Pass 1's hierarchy
(official_name, aliases, search_terms, abbreviations). Never touches the
hierarchy itself -- the LLM is only ever asked for concept_id plus the four
new fields, never for concept_name/parent_concept, so there is no way for
it to corrupt the hierarchy even accidentally.

Role played by the LLM: Educational Taxonomy Expert.

Input:
    output/chapter_concepts_hierarchy.json  (Pass 1)
    ../output/chapter_kb.json                (Phase 1, read-only -- definitions for context)

Output:
    output/chapter_concepts_normalized.json
"""

from __future__ import annotations

from typing import Any, Dict, List, Set

import utils

LOGGER = utils.setup_logger("02_concept_normalizer")

MAX_RECONCILE_ROUNDS = 2

SYSTEM_PROMPT = """You are an Educational Taxonomy Expert building search/alias metadata for
a chapter's concept knowledge graph.

You are given a fixed list of concepts (concept_id + concept_name), already
finalised, with definitions for context.

RULES

1. Use ONLY the concepts given to you. Do not add, rename, split, or merge
   concepts.
2. You MUST return exactly one entry for every concept_id given to you, no
   more, no fewer.
3. official_name: the standard NCERT/CBSE textbook name for the concept
   (usually the same as concept_name, corrected only if concept_name is a
   shorthand or has a typo).
4. aliases: alternative names/phrasings a teacher or textbook might use for
   the same concept.
5. search_terms: short keywords a student might search for this concept
   with.
6. abbreviations: standard abbreviations/symbols for the concept, if the
   subject uses one (chemistry concepts very often do: M, m, Kf, Kb, KH,
   ppm, i, alpha, pi, etc.).
7. Most exam-relevant science concepts DO have at least one useful alias,
   search term, or symbol -- do not default to empty lists out of caution.
   Only use an empty list when nothing plausible genuinely applies (e.g. a
   purely structural/organisational concept).
8. Never invent facts not implied by the concept name/definition given.
9. Return ONLY valid JSON. No markdown. No explanation. No code fences.

Worked example (this is the level of detail expected):

Concept: "Henry's Law"
{
    "concept_id": "CHE_SOL_028",
    "official_name": "Henry's Law",
    "aliases": ["Henry Law", "Gas Solubility Law"],
    "search_terms": ["Henry constant", "gas solubility", "partial pressure law"],
    "abbreviations": ["KH"]
}

Output schema:

{
    "concept_tree": [
        {
            "concept_id": "",
            "official_name": "",
            "aliases": [],
            "search_terms": [],
            "abbreviations": []
        }
    ]
}
"""

USER_PROMPT_TEMPLATE = """Concepts to normalise (you MUST cover every one of these, using the exact
concept_id values):

{concept_list}
"""


def format_concept_list(concepts: List[Dict[str, Any]], nodes_by_id: Dict[str, Dict[str, Any]]) -> str:
    lines = []
    for c in concepts:
        node = nodes_by_id.get(c["concept_id"], {})
        definition = node.get("definition", "").strip()
        lines.append(f"- {c['concept_id']}: {c['concept_name']}")
        if definition:
            lines.append(f"  Definition: {definition}")
    return "\n".join(lines)


def build_user_prompt(concepts: List[Dict[str, Any]], nodes_by_id: Dict[str, Dict[str, Any]]) -> str:
    return USER_PROMPT_TEMPLATE.format(concept_list=format_concept_list(concepts, nodes_by_id))


def make_validator(valid_ids: Set[str]):
    def validator(parsed: Any) -> None:
        utils.validate_json(parsed, ["concept_tree"])

        if not isinstance(parsed["concept_tree"], list):
            raise ValueError("'concept_tree' is not a list")

        for i, item in enumerate(parsed["concept_tree"]):
            if not isinstance(item, dict):
                raise ValueError(f"concept_tree[{i}] is not an object")

            if "concept_id" not in item or not isinstance(item["concept_id"], str):
                raise ValueError(f"concept_tree[{i}] missing/invalid 'concept_id'")

            if item["concept_id"] not in valid_ids:
                raise ValueError(f"concept_tree[{i}] has unknown concept_id '{item['concept_id']}'")

            if "official_name" not in item or not isinstance(item["official_name"], str):
                raise ValueError(f"concept_tree[{i}] missing/invalid 'official_name'")

            for field in ("aliases", "search_terms", "abbreviations"):
                if field not in item or not isinstance(item[field], list):
                    raise ValueError(f"concept_tree[{i}] missing/invalid '{field}'")

    return validator


def default_normalization(concept: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "concept_id": concept["concept_id"],
        "official_name": concept["concept_name"],
        "aliases": [],
        "search_terms": [],
        "abbreviations": [],
    }


def normalize_concepts() -> Dict[str, Any]:
    hierarchy_doc = utils.load_json(utils.HIERARCHY_FILE)
    concept_tree = hierarchy_doc["concept_tree"]
    valid_ids = {c["concept_id"] for c in concept_tree}
    LOGGER.info(f"{len(concept_tree)} concepts loaded from Pass 1 hierarchy")

    _, kb_doc = utils.load_phase1_inputs()
    nodes_by_id = {n["concept_id"]: n for n in kb_doc.get("knowledge_nodes", [])}

    enrichment_by_id: Dict[str, Dict[str, Any]] = {}
    remaining = list(concept_tree)
    round_num = 0

    while remaining and round_num <= MAX_RECONCILE_ROUNDS:
        round_num += 1
        LOGGER.info(f"Round {round_num}: requesting normalization for {len(remaining)} concept(s)")

        user_prompt = build_user_prompt(remaining, nodes_by_id)
        validator = make_validator(valid_ids)

        parsed = utils.call_llm_json(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=user_prompt,
            logger=LOGGER,
            validator=validator,
            raw_dump_filename=f"02_raw_output_round{round_num}.txt",
        )

        for item in parsed["concept_tree"]:
            enrichment_by_id[item["concept_id"]] = item

        remaining = [c for c in concept_tree if c["concept_id"] not in enrichment_by_id]

        if remaining:
            LOGGER.warning(
                f"{len(remaining)} concept(s) still missing after round {round_num}: "
                f"{[c['concept_id'] for c in remaining]}"
            )

    if remaining:
        LOGGER.warning(
            f"Filling {len(remaining)} concept(s) with default normalization after "
            f"{MAX_RECONCILE_ROUNDS} reconciliation round(s)"
        )
        for concept in remaining:
            enrichment_by_id[concept["concept_id"]] = default_normalization(concept)

    normalized_tree = []
    for concept in concept_tree:
        enrichment = enrichment_by_id[concept["concept_id"]]
        normalized_tree.append({
            "concept_id": concept["concept_id"],
            "concept_name": concept["concept_name"],
            "parent_concept": concept["parent_concept"],
            "is_grouping_node": concept["is_grouping_node"],
            "official_name": enrichment["official_name"],
            "aliases": enrichment["aliases"],
            "search_terms": enrichment["search_terms"],
            "abbreviations": enrichment["abbreviations"],
        })

    return {
        "chapter": hierarchy_doc.get("chapter", ""),
        "concept_tree": normalized_tree,
    }


def main() -> None:
    LOGGER.info("=" * 80)
    LOGGER.info("CONCEPT NORMALIZER (PASS 2)")
    LOGGER.info("=" * 80)

    result = normalize_concepts()

    utils.save_json(result, utils.NORMALIZED_FILE)
    LOGGER.info(f"Saved: {utils.NORMALIZED_FILE}")

    LOGGER.info("Summary")
    LOGGER.info(f"  Normalized concepts : {len(result['concept_tree'])}")


if __name__ == "__main__":
    main()
