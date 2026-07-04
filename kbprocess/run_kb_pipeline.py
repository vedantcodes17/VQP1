"""
run_kb_pipeline.py

Runs the full Chapter Knowledge Base pipeline in order:

    09a_concept_tree_builder.py
        -> output/chapter_concepts.json
    09b_knowledge_node_builder.py
        -> output/chapter_nodes.json
    09c_question_bank_builder.py
        -> output/chapter_questions.json
    09d_merge_kb.py
        -> output/chapter_kb.json

Each stage is run as a subprocess (module filenames start with a digit and
are not valid Python import names). The pipeline stops immediately if any
stage fails.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import List

import utils

LOGGER = utils.setup_logger("run_kb_pipeline")

BASE_DIR = Path(__file__).resolve().parent

PIPELINE_STAGES: List[str] = [
    "09a_concept_tree_builder.py",
    "09b_knowledge_node_builder.py",
    "09c_question_bank_builder.py",
    "09d_merge_kb.py",
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


def main() -> None:
    LOGGER.info("=" * 80)
    LOGGER.info("CHAPTER KNOWLEDGE BASE PIPELINE")
    LOGGER.info("=" * 80)

    for stage in PIPELINE_STAGES:
        try:
            run_stage(stage)
        except Exception as e:
            LOGGER.error(f"Pipeline aborted at stage '{stage}': {e}")
            sys.exit(1)

    LOGGER.info("=" * 80)
    LOGGER.info("PIPELINE COMPLETE")
    LOGGER.info(f"Final output: {utils.KB_FILE}")
    LOGGER.info("=" * 80)


if __name__ == "__main__":
    main()
