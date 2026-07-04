"""
run_concept_pipeline.py

Runs the full Concept Intelligence Engine in order:

    00_concept_validator.py     -> output/validation_report.json
    01_hierarchy_refiner.py     -> output/chapter_concepts_hierarchy.json
    02_concept_normalizer.py    -> output/chapter_concepts_normalized.json
    03_relationship_builder.py  -> output/chapter_relationships.json
    04_metadata_builder.py      -> output/chapter_metadata.json
    05_question_refiner.py      -> output/chapter_questions_refined.json
    06_merge_final_kb.py        -> output/chapter_kb_final.json

Each stage is run as a subprocess (module filenames start with a digit and
are not valid Python import names). The pipeline stops immediately if any
stage fails. It also aborts after Pass 0 if validation finds hard
structural defects (status == "FAIL"), since every later pass assumes a
structurally sound concept tree.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import List

import utils

LOGGER = utils.setup_logger("run_concept_pipeline")

BASE_DIR = Path(__file__).resolve().parent

PIPELINE_STAGES: List[str] = [
    "00_concept_validator.py",
    "01_hierarchy_refiner.py",
    "02_concept_normalizer.py",
    "03_relationship_builder.py",
    "04_metadata_builder.py",
    "05_question_refiner.py",
    "06_merge_final_kb.py",
]


def run_stage(script_name: str) -> None:
    script_path = BASE_DIR / script_name

    if not script_path.exists():
        raise FileNotFoundError(f"Pipeline stage not found: {script_path}")

    LOGGER.info("-" * 80)
    LOGGER.info(f"RUNNING STAGE: {script_name}")
    LOGGER.info("-" * 80)

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=str(BASE_DIR),
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"Stage '{script_name}' failed with exit code {result.returncode}"
        )

    LOGGER.info(f"Stage complete: {script_name}")


def check_validation_gate() -> None:
    report = utils.load_json(utils.VALIDATION_REPORT_FILE)
    status = report.get("status", "UNKNOWN")

    if status == "FAIL":
        raise RuntimeError(
            "Validation report status is FAIL (hard structural defects in the "
            "extracted concepts). Fix the underlying Phase 1 data before "
            "running the refinement pipeline."
        )

    if status == "PASS_WITH_WARNINGS":
        LOGGER.warning("Validation passed with warnings -- continuing, but review validation_report.json")


def main() -> None:
    LOGGER.info("=" * 80)
    LOGGER.info("CONCEPT INTELLIGENCE ENGINE PIPELINE")
    LOGGER.info("=" * 80)

    for stage in PIPELINE_STAGES:
        try:
            run_stage(stage)
        except Exception as e:
            LOGGER.error(f"Pipeline aborted at stage '{stage}': {e}")
            sys.exit(1)

        if stage == "00_concept_validator.py":
            try:
                check_validation_gate()
            except Exception as e:
                LOGGER.error(f"Pipeline aborted after validation: {e}")
                sys.exit(1)

    LOGGER.info("=" * 80)
    LOGGER.info("PIPELINE COMPLETE")
    LOGGER.info(f"Final output: {utils.FINAL_KB_FILE}")
    LOGGER.info("=" * 80)


if __name__ == "__main__":
    main()
