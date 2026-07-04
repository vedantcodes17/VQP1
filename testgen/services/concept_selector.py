"""
services/concept_selector.py

STEP 2 -- Concept Planner.
LLM persona: Curriculum Planner.

Input : chapter_kb_enriched.json + blueprint.json
Output: selected_concepts.json (one concept_id per slot_id)

The LLM proposes assignments based on importance, chapter_weightage,
learning outcomes, assessment metadata and retrieval keywords. Code then
deterministically (a) fills in any slot the LLM missed and (b) de-dupes
repeated concepts where an unused alternative exists, since a small local
model is not reliable at exact bookkeeping across a whole table.
"""

import sys
from pathlib import Path
from typing import Any, Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import utils
from prompts.concept_selector_prompt import CONCEPT_SELECTOR_SYSTEM_PROMPT, CONCEPT_SELECTOR_USER_TEMPLATE

LOGGER = utils.get_logger("concept_selector")

IMPORTANCE_RANK = {"high": 0, "medium": 1, "low": 2}


def examinable_concepts(chapter_kb: Dict[str, Any]) -> List[Dict[str, Any]]:
    return [c for c in chapter_kb["concept_tree"] if not c.get("is_grouping_node")]


def format_concept_list(concepts: List[Dict[str, Any]]) -> str:
    lines = []
    for c in concepts:
        assessment = c.get("assessment", {})
        keywords = c.get("retrieval", {}).get("keywords", [])[:5]
        outcomes = ", ".join(f"{lo.get('verb', '')} {lo.get('object', '')}".strip() for lo in c.get("learning_outcomes", [])[:2])
        lines.append(
            f"- {c['concept_id']}: {c['concept_name']} | importance={c.get('importance')} | "
            f"weightage={c.get('chapter_weightage')} | difficulty_hint={c.get('difficulty_hint')} | "
            f"preferred_types={assessment.get('preferred_question_types', [])} | "
            f"blooms={assessment.get('blooms_levels', [])} | keywords={keywords} | "
            f"learning_outcomes=[{outcomes}]"
        )
    return "\n".join(lines)


def format_slot_list(slots: List[Dict[str, Any]]) -> str:
    lines = []
    for s in slots:
        lines.append(
            f"- {s['slot_id']}: marks={s['marks']} | difficulty={s['difficulty']} | "
            f"question_type={s['question_type']} | bloom_levels={s.get('bloom_levels', [])}"
        )
    return "\n".join(lines)


def make_selector_validator(valid_slot_ids: set, valid_concept_ids: set):
    def validator(parsed: Any) -> None:
        if not isinstance(parsed, dict) or not isinstance(parsed.get("assignments"), list):
            raise ValueError("Missing/invalid 'assignments'")
        for i, a in enumerate(parsed["assignments"]):
            if not isinstance(a, dict) or a.get("slot_id") not in valid_slot_ids:
                raise ValueError(f"assignments[{i}] missing/unknown slot_id")
            if a.get("concept_id") not in valid_concept_ids:
                raise ValueError(f"assignments[{i}] missing/unknown concept_id")
    return validator


def concept_score(c: Dict[str, Any], slot: Dict[str, Any]) -> tuple:
    assessment = c.get("assessment", {})
    difficulty_match = 0 if c.get("difficulty_hint") == slot["difficulty"] else 1
    bloom_match = 0 if set(assessment.get("blooms_levels", [])) & set(slot.get("bloom_levels", [])) else 1
    type_match = 0 if slot["question_type"] in assessment.get("preferred_question_types", []) else 1
    importance_rank = IMPORTANCE_RANK.get(c.get("importance", "medium"), 1)
    return (difficulty_match, bloom_match, type_match, importance_rank)


def dedupe_assignments(assignments: List[Dict[str, Any]], slots: List[Dict[str, Any]],
                        concepts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Reassign duplicate concept_id picks to an unused concept when one is
    available, so the same concept isn't tested twice unless unavoidable."""
    concepts_by_id = {c["concept_id"]: c for c in concepts}
    slots_by_id = {s["slot_id"]: s for s in slots}
    by_slot = {a["slot_id"]: dict(a) for a in assignments}

    used_count: Dict[str, int] = {}
    for a in by_slot.values():
        used_count[a["concept_id"]] = used_count.get(a["concept_id"], 0) + 1

    ordered_slot_ids = [s["slot_id"] for s in slots]
    seen_once: set = set()
    for slot_id in ordered_slot_ids:
        a = by_slot.get(slot_id)
        if a is None:
            continue
        cid = a["concept_id"]
        if cid not in seen_once:
            seen_once.add(cid)
            continue
        # this slot's concept was already used by an earlier slot -- try to swap
        unused = [c for c in concepts if c["concept_id"] not in seen_once]
        if not unused:
            continue
        slot = slots_by_id[slot_id]
        best = min(unused, key=lambda c: concept_score(c, slot))
        LOGGER.info(f"Slot {slot_id}: reassigning duplicate concept {cid!r} -> {best['concept_id']!r}")
        a["concept_id"] = best["concept_id"]
        a["concept_name"] = best["concept_name"]
        a["rationale"] = (a.get("rationale", "") + " (de-duplicated)").strip()
        seen_once.add(best["concept_id"])

    return [by_slot[slot_id] for slot_id in ordered_slot_ids if slot_id in by_slot]


def select_concepts(blueprint: Dict[str, Any], chapter_kb: Dict[str, Any]) -> List[Dict[str, Any]]:
    concepts = examinable_concepts(chapter_kb)
    slots = blueprint["slots"]

    valid_slot_ids = {s["slot_id"] for s in slots}
    valid_concept_ids = {c["concept_id"] for c in concepts}

    user_prompt = CONCEPT_SELECTOR_USER_TEMPLATE.format(
        slot_count=len(slots),
        slot_list=format_slot_list(slots),
        concept_count=len(concepts),
        concept_list=format_concept_list(concepts),
    )

    LOGGER.info("Requesting concept assignments from LLM...")
    parsed = utils.call_llm_json(
        system_prompt=CONCEPT_SELECTOR_SYSTEM_PROMPT,
        user_prompt=user_prompt,
        validator=make_selector_validator(valid_slot_ids, valid_concept_ids),
        logger=LOGGER,
        max_tokens=6144,
    )

    concepts_by_id = {c["concept_id"]: c for c in concepts}
    assignments = []
    for a in parsed["assignments"]:
        cid = a["concept_id"]
        assignments.append({
            "slot_id": a["slot_id"],
            "concept_id": cid,
            "concept_name": concepts_by_id[cid]["concept_name"],
            "rationale": str(a.get("rationale", "")).strip(),
        })

    # Fill any slot the LLM skipped with the best-scoring unused concept.
    assigned_slot_ids = {a["slot_id"] for a in assignments}
    used_ids = {a["concept_id"] for a in assignments}
    for slot in slots:
        if slot["slot_id"] in assigned_slot_ids:
            continue
        unused = [c for c in concepts if c["concept_id"] not in used_ids] or concepts
        best = min(unused, key=lambda c: concept_score(c, slot))
        LOGGER.warning(f"Slot {slot['slot_id']} had no LLM assignment; filled with {best['concept_id']!r}")
        assignments.append({
            "slot_id": slot["slot_id"],
            "concept_id": best["concept_id"],
            "concept_name": best["concept_name"],
            "rationale": "auto-filled (LLM did not assign this slot)",
        })
        used_ids.add(best["concept_id"])

    assignments = dedupe_assignments(assignments, slots, concepts)
    LOGGER.info(f"Concept selection complete: {len(assignments)} assignment(s), "
                f"{len(set(a['concept_id'] for a in assignments))} distinct concept(s)")
    return assignments


if __name__ == "__main__":
    chapter_kb = utils.load_json(utils.CHAPTER_KB_FILE)
    blueprint = utils.load_json(utils.BLUEPRINT_FILE)
    selected = select_concepts(blueprint, chapter_kb)
    utils.save_json(selected, utils.SELECTED_CONCEPTS_FILE)
    print(f"Saved: {utils.SELECTED_CONCEPTS_FILE}")
