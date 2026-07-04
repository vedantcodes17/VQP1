"""
utils.py

Shared plumbing for every testgen service: LM Studio client, JSON
load/save, retrying LLM-JSON calls, and logging. Nothing chapter- or
prompt-specific lives here -- that stays in prompts/ and each service.
"""

from __future__ import annotations

import json
import logging
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

import requests

# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"
PROMPTS_DIR = BASE_DIR / "prompts"

CHAPTER_KB_FILE = INPUT_DIR / "chapter_kb_enriched.json"
EXTRA_QUESTIONS_FILE = BASE_DIR / "extra_questions.json"

BLUEPRINT_FILE = OUTPUT_DIR / "blueprint.json"
SELECTED_CONCEPTS_FILE = OUTPUT_DIR / "selected_concepts.json"
GENERATED_QUESTIONS_FILE = OUTPUT_DIR / "generated_questions.json"
QUESTIONS_WITH_DIAGRAM_FILE = OUTPUT_DIR / "questions_with_diagram.json"
VALIDATION_REPORT_FILE = OUTPUT_DIR / "validation_report.json"
FINAL_QUESTIONS_FILE = OUTPUT_DIR / "final_questions.json"
QUESTION_PAPER_FILE = OUTPUT_DIR / "question_paper.json"

# ==========================================================
# HARDCODED TEACHER INPUT (Step 0 -- no UI yet)
# ==========================================================

TEACHER_INPUT: Dict[str, Any] = {
    "subject": "Chemistry",
    "class": "12",
    "chapter": "Solutions",
    "total_marks": 30,
    "difficulty_distribution": {"easy": 0.30, "medium": 0.50, "hard": 0.20},
    "question_types": ["MCQ", "Short Answer", "Long Answer", "Numerical"],
}

# ==========================================================
# LLM CONFIGURATION
# ==========================================================

LMSTUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"
MODEL = "qwen2.5-vl-7b-instruct"
TEMPERATURE = 0.2
MAX_TOKENS = 4096
REQUEST_TIMEOUT = 600
MAX_RETRIES = 3
RETRY_BACKOFF_SECONDS = 3

# ==========================================================
# LOGGING
# ==========================================================

def get_logger(name: str) -> logging.Logger:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger(f"testgen.{name}")
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter(fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s", datefmt="%H:%M:%S")
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    logger.addHandler(sh)
    fh = logging.FileHandler(OUTPUT_DIR / "testgen.log", encoding="utf-8")
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    logger.propagate = False
    return logger


LOGGER = get_logger("utils")

# ==========================================================
# JSON HELPERS
# ==========================================================

def load_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def extract_json_candidate(text: str) -> str:
    cleaned = text.strip()
    cleaned = re.sub(r"^```(?:json)?", "", cleaned, flags=re.IGNORECASE).strip()
    cleaned = re.sub(r"```$", "", cleaned).strip()
    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start != -1 and end != -1 and end > start:
        return cleaned[start:end + 1]
    start = cleaned.find("[")
    end = cleaned.rfind("]")
    if start != -1 and end != -1 and end > start:
        return cleaned[start:end + 1]
    return cleaned


_BACKSLASH_SANITIZE = re.compile(r'\\(?!["\\/]|u[0-9a-fA-F]{4}|[bfnrt](?![a-zA-Z]))')


def sanitize_json_backslashes(text: str) -> str:
    """Chemistry answers routinely contain raw LaTeX (\\times, \\Delta, ...) that the
    model echoes unescaped. Only real JSON escapes (\\b\\f\\n\\r\\t not glued to more
    letters) survive; everything else gets doubled so json.loads doesn't choke."""
    return _BACKSLASH_SANITIZE.sub(r"\\\\", text)


def parse_json_response(text: str) -> Any:
    candidate = extract_json_candidate(text)
    try:
        return json.loads(candidate)
    except json.JSONDecodeError:
        pass
    return json.loads(sanitize_json_backslashes(candidate))


# ==========================================================
# LLM CLIENT
# ==========================================================

def call_llm(system_prompt: str, user_prompt: str, max_tokens: int = MAX_TOKENS,
             temperature: float = TEMPERATURE) -> Tuple[str, str]:
    payload = {
        "model": MODEL,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    }
    response = requests.post(LMSTUDIO_URL, json=payload, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    result = response.json()
    choice = result["choices"][0]
    return choice["message"]["content"], choice.get("finish_reason", "")


def call_llm_json(
    system_prompt: str,
    user_prompt: str,
    validator: Optional[Any] = None,
    max_retries: int = MAX_RETRIES,
    max_tokens: int = MAX_TOKENS,
    temperature: float = TEMPERATURE,
    logger: Optional[logging.Logger] = None,
) -> Any:
    log = logger or LOGGER
    last_error: Optional[Exception] = None
    current_prompt = user_prompt
    current_max_tokens = max_tokens

    for attempt in range(1, max_retries + 1):
        try:
            raw, finish_reason = call_llm(system_prompt, current_prompt, current_max_tokens, temperature)
            if finish_reason == "length":
                log.warning(f"Response truncated at max_tokens={current_max_tokens}")
            parsed = parse_json_response(raw)
            if validator is not None:
                validator(parsed)
            return parsed
        except Exception as e:
            last_error = e
            log.warning(f"LLM call attempt {attempt}/{max_retries} failed: {e}")
            current_prompt = (
                f"{user_prompt}\n\nIMPORTANT: Your previous response was invalid ({e}). "
                f"Return ONLY valid JSON matching the required schema. No markdown, no "
                f"explanation, no code fences."
            )
            current_max_tokens = min(current_max_tokens * 2, 16384)
            if attempt < max_retries:
                time.sleep(RETRY_BACKOFF_SECONDS)

    raise RuntimeError(f"LLM call failed after {max_retries} attempts: {last_error}")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", str(text).strip().lower())
