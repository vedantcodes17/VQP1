"""
05_question_refiner.py

Pass 5 of the Concept Intelligence Engine.

Phase 1's question extraction left questions and their answers as separate
question_bank entries (and the pairing is inconsistent -- some answers are
missing, some are misattributed to the wrong question, some are empty
"Ans." placeholders for self-assessment items). This pass merges each
question with its answer and reclassifies it into a finer 6-type taxonomy.

To avoid the LLM hallucinating or drifting question/answer text, it is
NEVER asked to retype question or answer content. It only groups existing
question_bank IDs together (question_source_ids / answer_source_ids) and
assigns a question_type; the actual text is spliced programmatically from
the untouched Phase 1 originals. This makes full-coverage, no-duplication
a hard, mechanically checkable invariant rather than something we have to
trust the model to get right.

Role played by the LLM: CBSE Examiner.

Input:
    ../output/chapter_kb.json  (Phase 1, read-only)

Output:
    output/chapter_questions_refined.json
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Set

import utils

LOGGER = utils.setup_logger("05_question_refiner")

MAX_RECONCILE_ROUNDS = 2
BATCH_SIZE = 15

QUESTION_TYPES = {
    "important",
    "short_answer",
    "long_answer",
    "numerical",
    "case_study",
    "self_assessment",
}

# Maps Phase 1's coarse types to a sane default if reconciliation ever has
# to fall back to a purely programmatic grouping.
LEGACY_TYPE_FALLBACK = {
    "important_question": "important",
    "short_answer": "short_answer",
    "self_assessment": "self_assessment",
    "numerical": "numerical",
}

ANSWER_PREFIX_PATTERN = re.compile(r"^\s*(ans\.?:?|answer\.?:?|hint\.?:?)\s*", re.IGNORECASE)

SYSTEM_PROMPT = """You are a CBSE Examiner reorganising a chapter's raw question bank into
clean question/answer pairs.

You are given the ORIGINAL question_bank entries, in their original order,
each with an id, its text, and Phase 1's coarse type tag. Consecutive
entries are very often a question immediately followed by its answer (an
entry starting with "Ans." or "Hint:"), but this is NOT always reliable --
some questions have no answer entry at all, some answers are empty
placeholders, and a few answers were misattributed to the wrong question by
the earlier extraction. Use the actual text to judge real pairings, not
just position.

RULES

1. Do NOT retype, rephrase, summarise, or invent question or answer text.
   You are only grouping existing ids -- the text itself is handled
   separately.
2. Every original id must be used in EXACTLY ONE group, either as a
   question_source_id or an answer_source_id. Never use an id twice. Never
   drop an id.
3. Most groups will be one question id + zero or one answer id. Only use
   multiple question_source_ids when several ids are clearly sub-parts of
   the same single question (e.g. an id that is just "(b) ..." continuing
   the previous id's "(a) ...").
4. If an "Ans."/"Hint:" entry's content clearly does not answer the
   preceding question (e.g. it repeats an unrelated earlier answer), do NOT
   pair them -- put the question in its own group with no answer, and give
   the mismatched answer its own group (as an answer-only group is not
   possible, so instead attach it to whichever question id it actually
   answers, or if genuinely orphaned, group it as answer_source_ids with an
   empty question_source_ids only if truly unavoidable).
5. Classify each group's question_type as exactly one of:
   - "important"       (marked important / high-value in the source)
   - "short_answer"     (brief conceptual answer, 1-2 sentences)
   - "long_answer"      (multi-part or extended explanation)
   - "numerical"        (requires a calculation)
   - "case_study"       (a scenario/passage followed by sub-questions)
   - "self_assessment"  (open-ended, no answer key provided)
6. Return ONLY valid JSON. No markdown. No explanation. No code fences.

Output schema:

{
    "refined_questions": [
        {
            "question_source_ids": ["TN_Q005"],
            "answer_source_ids": ["TN_Q006"],
            "question_type": "short_answer"
        }
    ]
}
"""

USER_PROMPT_TEMPLATE = """Original question_bank entries, in order:

{entries}

Group every id above into question/answer pairs and classify each group's
question_type. Every id must appear in exactly one group.
"""


def format_entries(questions: List[Dict[str, Any]]) -> str:
    lines = []
    for q in questions:
        lines.append(f"[{q['question_id']}] (type hint: {q['type']}) {q['question']}")
    return "\n".join(lines)


def build_user_prompt(questions: List[Dict[str, Any]]) -> str:
    return USER_PROMPT_TEMPLATE.format(entries=format_entries(questions))


def make_validator(valid_ids: Set[str]):
    def validator(parsed: Any) -> None:
        utils.validate_json(parsed, ["refined_questions"])

        if not isinstance(parsed["refined_questions"], list) or not parsed["refined_questions"]:
            raise ValueError("'refined_questions' is missing or empty")

        used_ids: Set[str] = set()

        for i, item in enumerate(parsed["refined_questions"]):
            if not isinstance(item, dict):
                raise ValueError(f"refined_questions[{i}] is not an object")

            if "question_source_ids" not in item or not isinstance(item["question_source_ids"], list):
                raise ValueError(f"refined_questions[{i}] missing/invalid 'question_source_ids'")
            if "answer_source_ids" not in item or not isinstance(item["answer_source_ids"], list):
                raise ValueError(f"refined_questions[{i}] missing/invalid 'answer_source_ids'")
            if "question_type" not in item or not isinstance(item["question_type"], str):
                raise ValueError(f"refined_questions[{i}] missing/invalid 'question_type'")

            group_ids = list(item["question_source_ids"]) + list(item["answer_source_ids"])
            if not group_ids:
                raise ValueError(f"refined_questions[{i}] has no source ids at all")

            for gid in group_ids:
                if not isinstance(gid, str) or gid not in valid_ids:
                    raise ValueError(f"refined_questions[{i}] references unknown id '{gid}'")
                if gid in used_ids:
                    raise ValueError(f"id '{gid}' is used in more than one group")
                used_ids.add(gid)

    return validator


def normalize_type(raw_type: str, fallback_hint: str) -> str:
    key = raw_type.strip().lower().replace(" ", "_").replace("-", "_")
    if key in QUESTION_TYPES:
        return key

    if "numer" in key or "calculat" in key:
        return "numerical"
    if "case" in key:
        return "case_study"
    if "self" in key:
        return "self_assessment"
    if "long" in key:
        return "long_answer"
    if "short" in key:
        return "short_answer"
    if "important" in key:
        return "important"

    return LEGACY_TYPE_FALLBACK.get(fallback_hint, "short_answer")


def clean_answer_text(raw_text: str) -> str:
    stripped = ANSWER_PREFIX_PATTERN.sub("", raw_text).strip()
    # A bare "Ans." with nothing meaningful left over is not a real answer
    # (this is exactly what Phase 1 produced for unanswered self-assessment
    # questions).
    if len(stripped) <= 1:
        return ""
    return stripped


def splice_group(
    group: Dict[str, Any],
    originals_by_id: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    question_ids = group["question_source_ids"]
    answer_ids = group["answer_source_ids"]

    question_text = " ".join(originals_by_id[qid]["question"].strip() for qid in question_ids).strip()
    raw_answer_text = " ".join(originals_by_id[aid]["question"].strip() for aid in answer_ids).strip()
    answer_text = clean_answer_text(raw_answer_text)

    linked_concepts: List[str] = []
    for sid in question_ids + answer_ids:
        for cid in originals_by_id[sid].get("linked_concepts", []):
            if cid not in linked_concepts:
                linked_concepts.append(cid)

    fallback_hint = originals_by_id[question_ids[0]]["type"] if question_ids else originals_by_id[answer_ids[0]]["type"]
    question_type = normalize_type(group["question_type"], fallback_hint)

    sort_key = min(
        int(re.search(r"(\d+)$", sid).group(1)) if re.search(r"(\d+)$", sid) else 0
        for sid in (question_ids + answer_ids)
    )

    return {
        "question": question_text,
        "answer": answer_text,
        "question_type": question_type,
        "linked_concepts": linked_concepts,
        "source_question_ids": question_ids + answer_ids,
        "_sort_key": sort_key,
    }


def refine_questions() -> Dict[str, Any]:
    _, kb_doc = utils.load_phase1_inputs()
    questions = kb_doc["question_bank"]
    originals_by_id = {q["question_id"]: q for q in questions}
    valid_ids = set(originals_by_id.keys())
    LOGGER.info(f"{len(questions)} original question_bank entries loaded")

    groups: List[Dict[str, Any]] = []

    batches = [
        questions[i:i + BATCH_SIZE]
        for i in range(0, len(questions), BATCH_SIZE)
    ]
    LOGGER.info(f"Processing {len(questions)} entries in {len(batches)} batch(es) of up to {BATCH_SIZE}")

    for batch_num, batch in enumerate(batches, start=1):
        batch_ids = {q["question_id"] for q in batch}
        remaining_ids = set(batch_ids)
        round_num = 0

        while remaining_ids and round_num <= MAX_RECONCILE_ROUNDS:
            round_num += 1
            remaining_questions = [q for q in batch if q["question_id"] in remaining_ids]
            LOGGER.info(
                f"Batch {batch_num}/{len(batches)}, round {round_num}: "
                f"requesting grouping for {len(remaining_questions)} entries"
            )

            user_prompt = build_user_prompt(remaining_questions)
            validator = make_validator(remaining_ids)

            try:
                parsed = utils.call_llm_json(
                    system_prompt=SYSTEM_PROMPT,
                    user_prompt=user_prompt,
                    logger=LOGGER,
                    validator=validator,
                    raw_dump_filename=f"05_raw_output_batch{batch_num}_round{round_num}.txt",
                )
            except Exception as e:
                LOGGER.warning(f"Batch {batch_num}, round {round_num} failed entirely, will retry/fallback: {e}")
                continue

            for item in parsed["refined_questions"]:
                groups.append(item)
                for gid in item["question_source_ids"] + item["answer_source_ids"]:
                    remaining_ids.discard(gid)

            if remaining_ids:
                LOGGER.warning(
                    f"Batch {batch_num}: {len(remaining_ids)} id(s) still ungrouped after round {round_num}: "
                    f"{sorted(remaining_ids)}"
                )

        if remaining_ids:
            LOGGER.warning(
                f"Batch {batch_num}: wrapping {len(remaining_ids)} leftover id(s) as standalone groups after "
                f"{MAX_RECONCILE_ROUNDS} reconciliation round(s)"
            )
            for qid in sorted(remaining_ids):
                groups.append({
                    "question_source_ids": [qid],
                    "answer_source_ids": [],
                    "question_type": originals_by_id[qid]["type"],
                })

    spliced = [splice_group(g, originals_by_id) for g in groups]
    spliced.sort(key=lambda s: s["_sort_key"])

    refined_questions = []
    for i, s in enumerate(spliced, start=1):
        refined_questions.append({
            "question_id": f"RQ{i:03d}",
            "question": s["question"],
            "answer": s["answer"],
            "question_type": s["question_type"],
            "linked_concepts": s["linked_concepts"],
            "source_question_ids": s["source_question_ids"],
        })

    return {
        "chapter": kb_doc.get("chapter", ""),
        "question_bank": refined_questions,
    }


def main() -> None:
    LOGGER.info("=" * 80)
    LOGGER.info("QUESTION REFINER (PASS 5)")
    LOGGER.info("=" * 80)

    result = refine_questions()

    utils.save_json(result, utils.QUESTIONS_REFINED_FILE)
    LOGGER.info(f"Saved: {utils.QUESTIONS_REFINED_FILE}")

    LOGGER.info("Summary")
    LOGGER.info(f"  Refined questions : {len(result['question_bank'])}")
    with_answer = sum(1 for q in result["question_bank"] if q["answer"])
    LOGGER.info(f"  With an answer     : {with_answer}")

    type_counts: Dict[str, int] = {}
    for q in result["question_bank"]:
        type_counts[q["question_type"]] = type_counts.get(q["question_type"], 0) + 1
    for q_type, count in sorted(type_counts.items()):
        LOGGER.info(f"    {q_type:16s} : {count}")


if __name__ == "__main__":
    main()
