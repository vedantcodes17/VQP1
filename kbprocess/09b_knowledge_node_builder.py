"""
09b_knowledge_node_builder.py

Reads teacher notes (data/solution.txt) and the concept tree produced by
09a (output/chapter_concepts.json), then enriches every concept with a
definition, formulae, important points and related concepts.

Role played by the LLM: Senior Chemistry Teacher.
Goal: enrich EXISTING concepts only. Never create new concepts.

Output: output/chapter_nodes.json
"""

from __future__ import annotations

from typing import Any, Dict, List, Set

import utils

LOGGER = utils.setup_logger("09b_knowledge_node_builder")

MAX_RECONCILE_ROUNDS = 2

SYSTEM_PROMPT = """You are a Senior Chemistry Teacher writing enrichment notes for a
canonical chapter knowledge base.

You are given:
1. A fixed list of concepts (concept_id + concept_name), already finalised.
2. The original teacher notes.

RULES

1. Use ONLY the concepts given to you. Do not add, rename, split or merge
   concepts.
2. You MUST return exactly one knowledge node for every concept_id given to
   you, no more, no fewer.
3. Every knowledge node must reuse the exact concept_id and concept_name
   given to you.
4. definition: a clear, exam-ready definition drawn from the notes.
5. formulae: list every formula/equation associated with the concept, exactly
   as written in the notes (as strings). Use an empty list if none apply.
6. important_points: bullet-style facts, rules, conditions or examples tied
   to the concept, taken from the notes.
7. related_concepts: names of OTHER concepts from the given list that are
   directly related (empty list if none).
8. Never invent facts that are not supported by the notes.
9. Return ONLY valid JSON. No markdown. No explanation. No code fences.

Output schema:

{
    "knowledge_nodes": [
        {
            "concept_id": "",
            "concept_name": "",
            "definition": "",
            "formulae": [],
            "important_points": [],
            "related_concepts": []
        }
    ]
}
"""

USER_PROMPT_TEMPLATE = """Concepts to enrich (you MUST cover every one of these, using these exact
concept_id and concept_name values):

{concept_list}

Teacher Notes:

{text}
"""


def format_concept_list(concepts: List[Dict[str, Any]]) -> str:
    lines = []
    for c in concepts:
        parent = f" (parent: {c['parent_concept']})" if c.get("parent_concept") else ""
        lines.append(f"- {c['concept_id']}: {c['concept_name']}{parent}")
    return "\n".join(lines)


def build_user_prompt(text: str, concepts: List[Dict[str, Any]]) -> str:
    return USER_PROMPT_TEMPLATE.format(
        concept_list=format_concept_list(concepts),
        text=text,
    )


def make_validator(valid_ids: Set[str]):
    def validator(parsed: Any) -> None:
        if not isinstance(parsed, dict):
            raise ValueError("Response is not a JSON object")

        if "knowledge_nodes" not in parsed or not isinstance(parsed["knowledge_nodes"], list):
            raise ValueError("Missing or invalid 'knowledge_nodes' field")

        for i, node in enumerate(parsed["knowledge_nodes"]):
            if not isinstance(node, dict):
                raise ValueError(f"knowledge_nodes[{i}] is not an object")

            for field in ("concept_id", "concept_name", "definition"):
                if field not in node or not isinstance(node[field], str):
                    raise ValueError(f"knowledge_nodes[{i}] missing/invalid '{field}'")

            for field in ("formulae", "important_points", "related_concepts"):
                if field not in node or not isinstance(node[field], list):
                    raise ValueError(f"knowledge_nodes[{i}] missing/invalid '{field}'")

            if node["concept_id"] not in valid_ids:
                raise ValueError(
                    f"knowledge_nodes[{i}] has unknown concept_id '{node['concept_id']}'"
                )

    return validator


def empty_node(concept: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "concept_id": concept["concept_id"],
        "concept_name": concept["concept_name"],
        "definition": "",
        "formulae": [],
        "important_points": [],
        "related_concepts": [],
    }


def build_knowledge_nodes() -> Dict[str, Any]:
    LOGGER.info(f"Loading concept tree: {utils.CONCEPTS_FILE}")
    concepts_doc = utils.load_json(utils.CONCEPTS_FILE)
    concept_tree = concepts_doc["concept_tree"]
    valid_ids = {c["concept_id"] for c in concept_tree}
    canonical_name_by_id = {c["concept_id"]: c["concept_name"] for c in concept_tree}
    LOGGER.info(f"{len(concept_tree)} concepts loaded")

    LOGGER.info(f"Loading input file: {utils.SOLUTION_FILE}")
    raw_text = utils.load_text_file(utils.SOLUTION_FILE)
    text = utils.preprocess_text(raw_text)
    LOGGER.info(f"Preprocessed to {len(text):,} characters")

    nodes_by_id: Dict[str, Dict[str, Any]] = {}
    remaining = list(concept_tree)
    round_num = 0

    while remaining and round_num <= MAX_RECONCILE_ROUNDS:
        round_num += 1
        LOGGER.info(f"Round {round_num}: requesting {len(remaining)} concept(s)")

        user_prompt = build_user_prompt(text, remaining)
        validator = make_validator(valid_ids)

        parsed = utils.call_llm_json(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=user_prompt,
            logger=LOGGER,
            validator=validator,
            raw_dump_filename=f"09b_raw_output_round{round_num}.txt",
        )

        for node in parsed["knowledge_nodes"]:
            # The LLM's concept_name is never trusted verbatim -- it sometimes
            # echoes prompt formatting (e.g. the "(parent: ...)" hint). The
            # canonical name from the concept tree is always authoritative.
            node["concept_name"] = canonical_name_by_id[node["concept_id"]]
            nodes_by_id[node["concept_id"]] = node

        remaining = [c for c in concept_tree if c["concept_id"] not in nodes_by_id]

        if remaining:
            LOGGER.warning(
                f"{len(remaining)} concept(s) still missing after round {round_num}: "
                f"{[c['concept_id'] for c in remaining]}"
            )

    if remaining:
        LOGGER.warning(
            f"Filling {len(remaining)} concept(s) with empty nodes after "
            f"{MAX_RECONCILE_ROUNDS} reconciliation round(s)"
        )
        for concept in remaining:
            nodes_by_id[concept["concept_id"]] = empty_node(concept)

    ordered_nodes = [nodes_by_id[c["concept_id"]] for c in concept_tree]

    return {"knowledge_nodes": ordered_nodes}


def main() -> None:
    LOGGER.info("=" * 80)
    LOGGER.info("KNOWLEDGE NODE BUILDER")
    LOGGER.info("=" * 80)

    result = build_knowledge_nodes()

    utils.save_json(result, utils.NODES_FILE)
    LOGGER.info(f"Saved: {utils.NODES_FILE}")

    LOGGER.info("Summary")
    LOGGER.info(f"  Knowledge Nodes : {len(result['knowledge_nodes'])}")


if __name__ == "__main__":
    main()
