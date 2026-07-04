"""
services/paper_builder.py

STEP 7 -- Paper Builder.

Purely deterministic formatting/assembly (not one of the LLM-driven
steps) -- takes final_questions.json + blueprint.json and produces the
student-facing paper plus a separate answer key.

Output: question_paper.json
"""

import sys
from pathlib import Path
from typing import Any, Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import utils

LOGGER = utils.get_logger("paper_builder")


def build_instructions(teacher_input: Dict[str, Any], blueprint: Dict[str, Any]) -> List[str]:
    lines = ["All questions are compulsory.", "Marks for each question are indicated against it."]
    for s in blueprint["sections"]:
        lines.append(
            f"Section {s['section']} consists of {s['num_questions']} question(s) of "
            f"{s['marks_each']} mark(s) each ({s['question_type']})."
        )
    return lines


def build_paper(final_questions: List[Dict[str, Any]], blueprint: Dict[str, Any],
                 teacher_input: Dict[str, Any]) -> Dict[str, Any]:
    questions_by_slot = {q["slot_id"]: q for q in final_questions}

    sections_out = []
    answer_key = []
    q_no = 1
    for s in blueprint["sections"]:
        section_letter = str(s["section"]).strip()
        slot_ids = [f"{section_letter}{i}" for i in range(1, int(s["num_questions"]) + 1)]
        section_questions = []
        for slot_id in slot_ids:
            q = questions_by_slot.get(slot_id)
            if q is None:
                LOGGER.warning(f"No final question for slot {slot_id}, skipping in paper")
                continue
            section_questions.append({
                "q_no": q_no,
                "question": q["question"],
                "marks": q["marks"],
                "type": q["type"],
                "difficulty": q["difficulty"],
                "concept_id": q.get("concept_id", ""),
            })
            answer_key.append({"q_no": q_no, "answer": q.get("answer", "")})
            q_no += 1

        sections_out.append({
            "section": section_letter,
            "marks_per_question": s["marks_each"],
            "question_type": s["question_type"],
            "questions": section_questions,
        })

    paper = {
        "subject": teacher_input["subject"],
        "class": teacher_input["class"],
        "chapter": teacher_input["chapter"],
        "total_marks": teacher_input["total_marks"],
        "instructions": build_instructions(teacher_input, blueprint),
        "sections": sections_out,
        "answer_key": answer_key,
    }
    LOGGER.info(f"Paper built: {len(sections_out)} section(s), {q_no - 1} question(s), "
                f"{sum(sec['marks_per_question'] * len(sec['questions']) for sec in sections_out)} marks")
    return paper


if __name__ == "__main__":
    final_questions = utils.load_json(utils.FINAL_QUESTIONS_FILE)
    blueprint = utils.load_json(utils.BLUEPRINT_FILE)
    paper = build_paper(final_questions, blueprint, utils.TEACHER_INPUT)
    utils.save_json(paper, utils.QUESTION_PAPER_FILE)
    print(f"Saved: {utils.QUESTION_PAPER_FILE}")
