"""
01_hierarchy_refiner.py

Pass 1 of the Concept Intelligence Engine.

Improves ONLY the parent-child hierarchy of the concepts already extracted
in Phase 1. This pass never renames, deletes, or invents real domain
concepts. The one narrow exception: it may introduce a small number of
structural "grouping nodes" (standard NCERT/CBSE umbrella terms, e.g.
"Expression of Concentration") purely to organise flat sibling concepts --
these carry no new domain facts and are explicitly flagged
is_grouping_node=true so downstream consumers can tell them apart from
real extracted concepts.

Role played by the LLM: Senior NCERT Curriculum Designer.

Input:
    ../output/chapter_concepts.json   (Phase 1, read-only)
    ../output/chapter_kb.json         (Phase 1, read-only -- definitions for context)

Output:
    output/chapter_concepts_hierarchy.json
"""

from __future__ import annotations

import re
from typing import Any, Dict, List

import utils

LOGGER = utils.setup_logger("01_hierarchy_refiner")

MIN_ACCEPTABLE_FRACTION = 0.8  # reject a response that dropped >20% of concepts

SYSTEM_PROMPT = """You are a Senior NCERT Curriculum Designer restructuring the concept
hierarchy for one chapter's knowledge graph.

You are given the chapter's existing concepts (flat or partially organised)
and their definitions for context.

RULES

1. Never rename an existing concept. Reuse concept_name values EXACTLY as
   given.
2. Never delete an existing concept. Every concept given to you must appear
   in your output.
3. Never invent new domain facts, definitions, or real concepts.
4. You MAY introduce a small number of purely structural "grouping" parent
   nodes -- standard NCERT/CBSE umbrella terms (e.g. "Expression of
   Concentration", "Colligative Properties") -- ONLY to organise existing
   sibling concepts that are flat but clearly belong under a common,
   well-established heading. A grouping node adds no new knowledge, only
   organisation. Mark every such node with "is_grouping_node": true.
5. Every existing concept must be marked "is_grouping_node": false.
6. Every existing concept is given a reference number like [12]. When your
   output entry corresponds to an existing concept, you MUST include that
   exact number as "concept_ref". For a new grouping node you introduce,
   set "concept_ref" to null.
7. Assign parent_concept using EXACT concept_name values (either an existing
   concept's name or a grouping node's name you introduced). Use an empty
   string if a concept has no parent.
8. Do not create deep hierarchies -- 2-3 levels is normal for a single
   chapter. Do not introduce a grouping node for a single child; only group
   when there are multiple flat siblings that clearly share a category.
9. Return ONLY valid JSON. No markdown. No explanation. No code fences.

Output schema:

{
    "concept_tree": [
        {
            "concept_ref": 1,
            "concept_name": "",
            "parent_concept": "",
            "is_grouping_node": false
        }
    ]
}
"""

USER_PROMPT_TEMPLATE = """Existing concepts and their definitions:

{concept_context}

Restructure the hierarchy following the rules. Every one of the {count}
existing concepts listed above must appear in your output, carrying its
concept_ref number unchanged.
"""


def format_concept_context(concept_tree: List[Dict[str, Any]], nodes_by_id: Dict[str, Dict[str, Any]]) -> str:
    lines = []
    for i, c in enumerate(concept_tree, start=1):
        node = nodes_by_id.get(c["concept_id"], {})
        definition = node.get("definition", "").strip()
        if definition:
            lines.append(f"[{i}] {c['concept_name']}: {definition}")
        else:
            lines.append(f"[{i}] {c['concept_name']}")
    return "\n".join(lines)


def build_user_prompt(concept_tree: List[Dict[str, Any]], nodes_by_id: Dict[str, Dict[str, Any]]) -> str:
    return USER_PROMPT_TEMPLATE.format(
        concept_context=format_concept_context(concept_tree, nodes_by_id),
        count=len(concept_tree),
    )


def validate_raw_hierarchy(parsed: Any, original_count: int) -> None:
    """Cheap structural check -- catches garbage/truncated JSON early.
    Precise reconciliation against the original concept list happens
    afterwards in Python, not here.
    """
    utils.validate_json(parsed, ["concept_tree"])

    if not isinstance(parsed["concept_tree"], list) or not parsed["concept_tree"]:
        raise ValueError("'concept_tree' is missing or empty")

    for i, item in enumerate(parsed["concept_tree"]):
        if not isinstance(item, dict):
            raise ValueError(f"concept_tree[{i}] is not an object")
        if "concept_name" not in item or not isinstance(item["concept_name"], str) or not item["concept_name"].strip():
            raise ValueError(f"concept_tree[{i}] missing/invalid 'concept_name'")
        if "parent_concept" not in item:
            raise ValueError(f"concept_tree[{i}] missing 'parent_concept'")

    if len(parsed["concept_tree"]) < original_count * MIN_ACCEPTABLE_FRACTION:
        raise ValueError(
            f"Response only contains {len(parsed['concept_tree'])} entries, "
            f"expected at least {int(original_count * MIN_ACCEPTABLE_FRACTION)} "
            f"of the {original_count} original concepts"
        )


def derive_grouping_prefix(concept_tree: List[Dict[str, Any]]) -> str:
    """Derives e.g. 'CHE_SOL' from 'CHE_SOL_014' so grouping-node IDs stay
    in the same family but in a visually distinct, never-colliding lane."""
    sample_id = concept_tree[0]["concept_id"]
    match = re.match(r"^(.*)_\d+$", sample_id)
    prefix = match.group(1) if match else sample_id
    return f"{prefix}_GRP"


def reconcile_hierarchy(
    original_concept_tree: List[Dict[str, Any]],
    llm_concept_tree: List[Dict[str, Any]],
) -> Dict[str, Any]:
    original_by_key = {utils.normalize_name(c["concept_name"]): c for c in original_concept_tree}
    ref_to_original = {i: c for i, c in enumerate(original_concept_tree, start=1)}
    grouping_prefix = derive_grouping_prefix(original_concept_tree)

    # 1. Resolve every LLM entry: either it matches an original concept --
    #    preferably via its concept_ref index (immune to the LLM echoing
    #    prompt-formatting text into concept_name), falling back to
    #    normalized-name matching -- or it is a proposed new grouping node
    #    (accepted only if explicitly flagged).
    resolved_by_key: Dict[str, Dict[str, Any]] = {}
    grouping_nodes: Dict[str, Dict[str, Any]] = {}
    next_grouping_index = 1
    dropped_inventions = []

    for item in llm_concept_tree:
        key = utils.normalize_name(item["concept_name"])
        is_grouping = bool(item.get("is_grouping_node", False))
        ref = item.get("concept_ref")

        original = None
        if isinstance(ref, (int, float)) and int(ref) in ref_to_original:
            original = ref_to_original[int(ref)]
        elif key in original_by_key:
            original = original_by_key[key]

        if original is not None:
            original_key = utils.normalize_name(original["concept_name"])
            resolved_by_key[original_key] = {
                "concept_id": original["concept_id"],
                "concept_name": original["concept_name"],  # never trust LLM rewording
                "parent_concept_raw": (item.get("parent_concept") or "").strip(),
                "is_grouping_node": False,
            }
        elif is_grouping:
            if key not in grouping_nodes:
                grouping_id = f"{grouping_prefix}_{next_grouping_index:03d}"
                next_grouping_index += 1
                grouping_nodes[key] = {
                    "concept_id": grouping_id,
                    "concept_name": item["concept_name"].strip(),
                    "parent_concept_raw": (item.get("parent_concept") or "").strip(),
                    "is_grouping_node": True,
                }
        else:
            dropped_inventions.append(item["concept_name"])

    if dropped_inventions:
        LOGGER.warning(
            f"Dropped {len(dropped_inventions)} unflagged new concept(s) the model "
            f"tried to invent: {dropped_inventions}"
        )

    # 2. Any original concept the LLM silently dropped is restored with its
    #    original parent -- never deleted, per rule 2.
    missing = [
        original for key, original in original_by_key.items()
        if key not in resolved_by_key
    ]
    for original in missing:
        resolved_by_key[utils.normalize_name(original["concept_name"])] = {
            "concept_id": original["concept_id"],
            "concept_name": original["concept_name"],
            "parent_concept_raw": original.get("parent_concept", ""),
            "is_grouping_node": False,
        }
    if missing:
        LOGGER.warning(
            f"Restored {len(missing)} concept(s) the model dropped: "
            f"{[o['concept_name'] for o in missing]}"
        )

    # 3. Build the full name->entry lookup (originals + accepted grouping
    #    nodes) so parent references can be resolved to canonical names.
    all_entries = list(resolved_by_key.values()) + list(grouping_nodes.values())
    name_lookup = {utils.normalize_name(e["concept_name"]): e["concept_name"] for e in all_entries}

    concept_tree = []
    for entry in all_entries:
        parent_key = utils.normalize_name(entry["parent_concept_raw"]) if entry["parent_concept_raw"] else ""
        if parent_key and parent_key != utils.normalize_name(entry["concept_name"]) and parent_key in name_lookup:
            parent_concept = name_lookup[parent_key]
        else:
            parent_concept = ""

        concept_tree.append({
            "concept_id": entry["concept_id"],
            "concept_name": entry["concept_name"],
            "parent_concept": parent_concept,
            "is_grouping_node": entry["is_grouping_node"],
        })

    # 4. Break any cycles the reorganisation introduced by cutting the
    #    weakest link (the last edge that closes the loop).
    cycles = utils.find_hierarchy_cycles(concept_tree)
    if cycles:
        by_name = {c["concept_name"]: c for c in concept_tree}
        for cycle in cycles:
            offending_name = cycle[-2]  # the node whose parent link closes the loop
            LOGGER.warning(
                f"Breaking circular hierarchy {' -> '.join(cycle)}: "
                f"clearing parent of '{offending_name}'"
            )
            by_name[offending_name]["parent_concept"] = ""

    # Order: original concepts first (in original order), then grouping nodes.
    original_order = [utils.normalize_name(c["concept_name"]) for c in original_concept_tree]
    ordered = [resolved_by_key[key] for key in original_order]
    ordered_ids = {e["concept_id"] for e in ordered}
    final_tree = [c for c in concept_tree if c["concept_id"] in ordered_ids]
    final_tree += [c for c in concept_tree if c["concept_id"] not in ordered_ids]

    hierarchy_changes = []
    for original in original_concept_tree:
        updated = next(c for c in final_tree if c["concept_id"] == original["concept_id"])
        if utils.normalize_name(updated["parent_concept"]) != utils.normalize_name(original.get("parent_concept", "")):
            hierarchy_changes.append({
                "concept_id": original["concept_id"],
                "concept_name": original["concept_name"],
                "old_parent": original.get("parent_concept", ""),
                "new_parent": updated["parent_concept"],
            })

    return {
        "concept_tree": final_tree,
        "hierarchy_changes": hierarchy_changes,
        "grouping_nodes_added": len(grouping_nodes),
    }


def refine_hierarchy() -> Dict[str, Any]:
    concepts_doc, kb_doc = utils.load_phase1_inputs()
    concept_tree = concepts_doc["concept_tree"]
    nodes_by_id = {n["concept_id"]: n for n in kb_doc.get("knowledge_nodes", [])}

    LOGGER.info(f"{len(concept_tree)} concepts loaded from Phase 1")

    user_prompt = build_user_prompt(concept_tree, nodes_by_id)

    def validator(parsed):
        validate_raw_hierarchy(parsed, len(concept_tree))

    LOGGER.info("Calling LLM to refine hierarchy...")
    parsed = utils.call_llm_json(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=user_prompt,
        logger=LOGGER,
        validator=validator,
        raw_dump_filename="01_raw_output.txt",
    )

    result = reconcile_hierarchy(concept_tree, parsed["concept_tree"])
    result["chapter"] = concepts_doc.get("chapter", "")

    return result


def main() -> None:
    LOGGER.info("=" * 80)
    LOGGER.info("HIERARCHY REFINER (PASS 1)")
    LOGGER.info("=" * 80)

    result = refine_hierarchy()

    output = {
        "chapter": result["chapter"],
        "concept_tree": result["concept_tree"],
        "hierarchy_changes": result["hierarchy_changes"],
    }

    utils.save_json(output, utils.HIERARCHY_FILE)
    LOGGER.info(f"Saved: {utils.HIERARCHY_FILE}")

    LOGGER.info("Summary")
    LOGGER.info(f"  Total concepts (incl. grouping) : {len(result['concept_tree'])}")
    LOGGER.info(f"  Grouping nodes added             : {result['grouping_nodes_added']}")
    LOGGER.info(f"  Parent changes                    : {len(result['hierarchy_changes'])}")


if __name__ == "__main__":
    main()
