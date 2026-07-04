"""
services/diagram_injector.py

STEP 4 (separated per plan) -- Diagram Injector.

Purely mechanical -- no LLM. Randomly swaps ONE eligible generated
question for a manually authored diagram question from
extra_questions.json, so the validator downstream has something real to
catch (requires_diagram == true -> "Diagram generation unavailable.").

Eligibility: skip MCQ slots (a hand-drawn diagram doesn't fit a 1-mark
MCQ format) so the swap is at least structurally plausible.
"""

import random
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import utils

LOGGER = utils.get_logger("diagram_injector")


def inject_diagram_question(questions: List[Dict[str, Any]],
                             extra_questions: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], Optional[str]]:
    if not extra_questions:
        LOGGER.warning("No extra_questions available, skipping injection")
        return questions, None

    eligible_indices = [i for i, q in enumerate(questions) if q.get("type") != "MCQ"]
    if not eligible_indices:
        LOGGER.warning("No eligible (non-MCQ) slot to inject a diagram question into, skipping")
        return questions, None

    idx = random.choice(eligible_indices)
    extra = random.choice(extra_questions)
    original = questions[idx]

    injected = dict(original)
    injected["question"] = extra["question"]
    injected["answer"] = extra["answer"]
    injected["requires_diagram"] = True
    injected["concept_id"] = original["concept_id"]  # keep it traceable to a real KB concept
    injected["_injected_from"] = extra["id"]

    questions = list(questions)
    questions[idx] = injected

    LOGGER.info(f"Injected diagram question {extra['id']!r} into slot {original['slot_id']} "
                f"(question {original['id']})")
    return questions, injected["id"]


if __name__ == "__main__":
    questions = utils.load_json(utils.GENERATED_QUESTIONS_FILE)
    extra_questions = utils.load_json(utils.EXTRA_QUESTIONS_FILE)
    updated, injected_id = inject_diagram_question(questions, extra_questions)
    utils.save_json(updated, utils.QUESTIONS_WITH_DIAGRAM_FILE)
    print(f"Saved: {utils.QUESTIONS_WITH_DIAGRAM_FILE} (injected into {injected_id})")
