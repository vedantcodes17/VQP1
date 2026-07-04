"""
main.py

STEP 8 -- orchestrates the full agentic pipeline end-to-end:

    Blueprint -> Concept Selection -> Question Generation ->
    Diagram Injection -> Validation -> Regeneration -> Paper Builder

Teacher inputs are hardcoded in utils.TEACHER_INPUT. Everything else is
file-based; no DB, no retrieval, no APIs other than local LM Studio.
"""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import utils
from services import blueprint_service, concept_selector, question_generator, diagram_injector, \
    question_validator, question_regenerator, paper_builder

LOGGER = utils.get_logger("main")


def main() -> None:
    t0 = time.time()

    print("Loading KB...")
    chapter_kb = utils.load_json(utils.CHAPTER_KB_FILE)
    extra_questions = utils.load_json(utils.EXTRA_QUESTIONS_FILE)

    print("Generating Blueprint...")
    blueprint = blueprint_service.generate_blueprint(utils.TEACHER_INPUT, chapter_kb)
    utils.save_json(blueprint, utils.BLUEPRINT_FILE)

    print("Selecting Concepts...")
    selected_concepts = concept_selector.select_concepts(blueprint, chapter_kb)
    utils.save_json(selected_concepts, utils.SELECTED_CONCEPTS_FILE)

    print("Generating Questions...")
    generated_questions = question_generator.generate_all_questions(blueprint, selected_concepts, chapter_kb)
    utils.save_json(generated_questions, utils.GENERATED_QUESTIONS_FILE)

    print("Injecting Diagram Question...")
    questions_with_diagram, injected_id = diagram_injector.inject_diagram_question(generated_questions, extra_questions)
    utils.save_json(questions_with_diagram, utils.QUESTIONS_WITH_DIAGRAM_FILE)

    print("Validating...")
    validation_report = question_validator.validate(questions_with_diagram, blueprint)
    utils.save_json(validation_report, utils.VALIDATION_REPORT_FILE)
    print(f"{validation_report['flagged_count']} Question(s) Flagged")

    if validation_report["flagged_count"] > 0:
        print("Regenerating...")
        final_questions = question_regenerator.regenerate_flagged(
            questions_with_diagram, validation_report, blueprint, chapter_kb
        )
    else:
        final_questions = questions_with_diagram
    utils.save_json(final_questions, utils.FINAL_QUESTIONS_FILE)

    print("Building Paper...")
    paper = paper_builder.build_paper(final_questions, blueprint, utils.TEACHER_INPUT)
    utils.save_json(paper, utils.QUESTION_PAPER_FILE)

    elapsed = time.time() - t0
    print("Done.")
    print(f"\nQuestion paper saved to: {utils.QUESTION_PAPER_FILE}")
    print(f"Total time: {elapsed:.1f}s")
    LOGGER.info(f"Pipeline complete in {elapsed:.1f}s")


if __name__ == "__main__":
    main()
