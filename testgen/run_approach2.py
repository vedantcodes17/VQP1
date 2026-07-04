"""
run_approach2.py

Runs the EXACT SAME agentic pipeline as main.py (same services, same
prompts, same teacher input, same model) but against the "new approach"
knowledge base (approach2_output/chapter_kb.json) instead of the
teacher-note KB (chapter_kb_enriched.json), saving all artifacts under
Approach2_op/ so the two resulting question papers can be compared
side by side without overwriting each other.

NOTE: chapter_kb_approach2.json currently has only 4 concepts (it was
built from a 5-chunk smoke test of approach2.py), versus 29 concepts in
the teacher-note KB. The 14-slot blueprint will therefore reuse those 4
concepts heavily -- that's a scale artifact of the input data, not a
pipeline bug. Re-run approach2.py without LIMIT_CHUNKS for a fair
concept-for-concept comparison.
"""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import utils
from services import blueprint_service, concept_selector, question_generator, diagram_injector, \
    question_validator, question_regenerator, paper_builder

LOGGER = utils.get_logger("run_approach2")

CHAPTER_KB_FILE = utils.INPUT_DIR / "chapter_kb_approach2.json"

OUTPUT_DIR = utils.BASE_DIR / "Approach2_op"
BLUEPRINT_FILE = OUTPUT_DIR / "blueprint.json"
SELECTED_CONCEPTS_FILE = OUTPUT_DIR / "selected_concepts.json"
GENERATED_QUESTIONS_FILE = OUTPUT_DIR / "generated_questions.json"
QUESTIONS_WITH_DIAGRAM_FILE = OUTPUT_DIR / "questions_with_diagram.json"
VALIDATION_REPORT_FILE = OUTPUT_DIR / "validation_report.json"
FINAL_QUESTIONS_FILE = OUTPUT_DIR / "final_questions.json"
QUESTION_PAPER_FILE = OUTPUT_DIR / "question_paper.json"


def main() -> None:
    t0 = time.time()

    print("Loading KB (Approach2)...")
    chapter_kb = utils.load_json(CHAPTER_KB_FILE)
    extra_questions = utils.load_json(utils.EXTRA_QUESTIONS_FILE)
    LOGGER.info(f"Loaded {len(chapter_kb['concept_tree'])} concept(s) from {CHAPTER_KB_FILE.name}")

    print("Generating Blueprint...")
    blueprint = blueprint_service.generate_blueprint(utils.TEACHER_INPUT, chapter_kb)
    utils.save_json(blueprint, BLUEPRINT_FILE)

    print("Selecting Concepts...")
    selected_concepts = concept_selector.select_concepts(blueprint, chapter_kb)
    utils.save_json(selected_concepts, SELECTED_CONCEPTS_FILE)

    print("Generating Questions...")
    generated_questions = question_generator.generate_all_questions(blueprint, selected_concepts, chapter_kb)
    utils.save_json(generated_questions, GENERATED_QUESTIONS_FILE)

    print("Injecting Diagram Question...")
    questions_with_diagram, injected_id = diagram_injector.inject_diagram_question(generated_questions, extra_questions)
    utils.save_json(questions_with_diagram, QUESTIONS_WITH_DIAGRAM_FILE)

    print("Validating...")
    validation_report = question_validator.validate(questions_with_diagram, blueprint)
    utils.save_json(validation_report, VALIDATION_REPORT_FILE)
    print(f"{validation_report['flagged_count']} Question(s) Flagged")

    if validation_report["flagged_count"] > 0:
        print("Regenerating...")
        final_questions = question_regenerator.regenerate_flagged(
            questions_with_diagram, validation_report, blueprint, chapter_kb
        )
    else:
        final_questions = questions_with_diagram
    utils.save_json(final_questions, FINAL_QUESTIONS_FILE)

    print("Building Paper...")
    paper = paper_builder.build_paper(final_questions, blueprint, utils.TEACHER_INPUT)
    utils.save_json(paper, QUESTION_PAPER_FILE)

    elapsed = time.time() - t0
    print("Done.")
    print(f"\nQuestion paper saved to: {QUESTION_PAPER_FILE}")
    print(f"Total time: {elapsed:.1f}s")
    LOGGER.info(f"Approach2 pipeline complete in {elapsed:.1f}s")


if __name__ == "__main__":
    main()
