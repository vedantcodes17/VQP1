"""
09c_question_bank_builder.py

Reads teacher notes (data/solution.txt) and the concept tree produced by
09a (output/chapter_concepts.json), then extracts every question in the
notes and links each one to the concept(s) it tests.

Role played by the LLM: CBSE Examiner.
Goal: extract and classify ALL questions (Important Questions, Short
Answer Questions, Numerical Questions, Self Assessment Questions) and link
each to one or more existing concept IDs.

Output: output/chapter_questions.json
"""

from __future__ import annotations

from typing import Any, Dict, List, Set

import utils

LOGGER = utils.setup_logger("09c_question_bank_builder")

QUESTION_ID_PREFIX = "TN_Q"

VALID_TYPES = {
    "important_question",
    "short_answer",
    "numerical",
    "self_assessment",
}

SYSTEM_PROMPT = """You are a CBSE Examiner extracting and classifying every question found
in a teacher's notes for one chapter.

You are given:
1. A fixed list of concepts (concept_id + concept_name), already finalised.
2. The original teacher notes, which contain Important Questions, Short
   Answer Questions, Numerical Questions and Self Assessment Questions.

RULES

1. Extract EVERY question present in the notes. Do not skip, merge, or
   summarise questions. Preserve the original question wording as closely
   as possible (you may lightly clean up OCR/formatting noise).
2. Do not invent new questions.
3. Classify each question's "type" as exactly one of:
   - "important_question"
   - "short_answer"
   - "numerical"
   - "self_assessment"
   Use the section the question appeared under in the notes as the primary
   signal for classification.
4. Every question must be linked to one or more concept_id values FROM THE
   GIVEN LIST ONLY. Never invent a concept_id.
5. Read each question individually and link it to the SPECIFIC concept(s)
   it actually tests. Do NOT default every question to the same concept —
   each question in the notes tests a different idea (e.g. a question about
   Henry's Law links to the Henry's Law / gas solubility concept, a question
   about freezing point depression links to that concept, etc). Identical
   linked_concepts across many unrelated questions is a mistake.
6. Return ONLY valid JSON. No markdown. No explanation. No code fences.

Output schema:

{
    "question_bank": [
        {
            "question": "",
            "type": "",
            "linked_concepts": ["CHE_SOL_001"]
        }
    ]
}
"""

USER_PROMPT_TEMPLATE = """Concepts available for linking (use ONLY these concept_id values):

{concept_list}

Teacher Notes:

{text}
"""


def format_concept_list(concepts: List[Dict[str, Any]]) -> str:
    return "\n".join(f"- {c['concept_id']}: {c['concept_name']}" for c in concepts)


def build_user_prompt(text: str, concepts: List[Dict[str, Any]]) -> str:
    return USER_PROMPT_TEMPLATE.format(
        concept_list=format_concept_list(concepts),
        text=text,
    )


def validate_raw_questions(parsed: Any) -> None:
    if not isinstance(parsed, dict):
        raise ValueError("Response is not a JSON object")

    if "question_bank" not in parsed or not isinstance(parsed["question_bank"], list):
        raise ValueError("Missing or invalid 'question_bank' field")

    if not parsed["question_bank"]:
        raise ValueError("'question_bank' is empty")

    for i, item in enumerate(parsed["question_bank"]):
        if not isinstance(item, dict):
            raise ValueError(f"question_bank[{i}] is not an object")
        if "question" not in item or not isinstance(item["question"], str) or not item["question"].strip():
            raise ValueError(f"question_bank[{i}] missing/invalid 'question'")
        if "type" not in item or not isinstance(item["type"], str):
            raise ValueError(f"question_bank[{i}] missing/invalid 'type'")
        if "linked_concepts" not in item or not isinstance(item["linked_concepts"], list):
            raise ValueError(f"question_bank[{i}] missing/invalid 'linked_concepts'")

    # Sanity check: if every question (or nearly every question) was linked
    # to the exact same single concept, the model almost certainly defaulted
    # instead of reasoning per-question. Force a retry in that case.
    questions = parsed["question_bank"]
    if len(questions) >= 5:
        signatures = [tuple(sorted(item["linked_concepts"])) for item in questions]
        most_common_count = max((signatures.count(sig) for sig in set(signatures)), default=0)
        if most_common_count / len(signatures) > 0.8:
            raise ValueError(
                "linked_concepts look defaulted: over 80% of questions share the "
                "exact same concept linkage. Re-read each question individually."
            )


def normalize_type(raw_type: str) -> str:
    key = raw_type.strip().lower().replace(" ", "_").replace("-", "_")
    if key in VALID_TYPES:
        return key

    if "numerical" in key:
        return "numerical"
    if "self" in key:
        return "self_assessment"
    if "short" in key:
        return "short_answer"
    if "important" in key:
        return "important_question"

    return "important_question"


def resolve_linked_concepts(
    raw_ids: List[str],
    question_text: str,
    valid_ids: Set[str],
    concepts: List[Dict[str, Any]],
) -> List[str]:
    resolved = [cid for cid in raw_ids if isinstance(cid, str) and cid in valid_ids]

    # Always cross-check against concept names that literally appear in the
    # question text -- this catches cases where the model's own linking
    # missed an obvious match, and provides a full fallback if it gave none.
    q_key = utils.normalize_name(question_text)
    name_matches = [
        c["concept_id"]
        for c in concepts
        if utils.normalize_name(c["concept_name"]) in q_key
    ]

    return list(dict.fromkeys(resolved + name_matches))


def build_question_bank() -> Dict[str, Any]:
    LOGGER.info(f"Loading concept tree: {utils.CONCEPTS_FILE}")
    concepts_doc = utils.load_json(utils.CONCEPTS_FILE)
    concept_tree = concepts_doc["concept_tree"]
    valid_ids = {c["concept_id"] for c in concept_tree}
    LOGGER.info(f"{len(concept_tree)} concepts loaded")

    LOGGER.info(f"Loading input file: {utils.SOLUTION_FILE}")
    raw_text = utils.load_text_file(utils.SOLUTION_FILE)
    text = utils.preprocess_text(raw_text)
    LOGGER.info(f"Preprocessed to {len(text):,} characters")

    user_prompt = build_user_prompt(text, concept_tree)

    LOGGER.info("Calling LLM to extract question bank...")
    parsed = utils.call_llm_json(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=user_prompt,
        logger=LOGGER,
        validator=validate_raw_questions,
        raw_dump_filename="09c_raw_output.txt",
    )

    question_bank = []
    unresolved_count = 0

    for index, item in enumerate(parsed["question_bank"], start=1):
        question_id = f"{QUESTION_ID_PREFIX}{index:03d}"
        q_type = normalize_type(item["type"])
        linked_concepts = resolve_linked_concepts(
            item["linked_concepts"], item["question"], valid_ids, concept_tree
        )

        if not linked_concepts:
            unresolved_count += 1
            LOGGER.warning(
                f"{question_id} could not be linked to any known concept: "
                f"{item['question'][:80]!r}"
            )

        question_bank.append({
            "question_id": question_id,
            "question": item["question"].strip(),
            "type": q_type,
            "linked_concepts": linked_concepts,
        })

    if unresolved_count:
        LOGGER.warning(f"{unresolved_count} question(s) have no linked concepts")

    return {"question_bank": question_bank}


def main() -> None:
    LOGGER.info("=" * 80)
    LOGGER.info("QUESTION BANK BUILDER")
    LOGGER.info("=" * 80)

    result = build_question_bank()

    utils.save_json(result, utils.QUESTIONS_FILE)
    LOGGER.info(f"Saved: {utils.QUESTIONS_FILE}")

    LOGGER.info("Summary")
    LOGGER.info(f"  Total Questions : {len(result['question_bank'])}")

    type_counts: Dict[str, int] = {}
    for q in result["question_bank"]:
        type_counts[q["type"]] = type_counts.get(q["type"], 0) + 1
    for q_type, count in sorted(type_counts.items()):
        LOGGER.info(f"    {q_type:20s} : {count}")


if __name__ == "__main__":
    main()
