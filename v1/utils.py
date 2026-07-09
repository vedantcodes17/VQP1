"""
Shared utilities for the v1 knowledge-graph schema pipeline.

Provides:
    - logging setup
    - LM Studio chat-completion client with retries + truncation escalation
    - robust JSON extraction / validation (object- or array-rooted)
    - JSON save/load helpers
"""

from __future__ import annotations

import json
import logging
import re
import sys
import time
from pathlib import Path
from typing import Any, Callable, List, Optional

import requests

# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"

TEACHER_NOTES_DIR = BASE_DIR / "teacher_notes"
CONCEPTS_DIR = BASE_DIR / "concepts"
FORMULAS_DIR = BASE_DIR / "formulas"
REPORTS_DIR = BASE_DIR / "reports"

# ==========================================================
# LLM CONFIGURATION
# ==========================================================

LMSTUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"
MODEL = "qwen2.5-vl-7b-instruct"
TEMPERATURE = 0.1
MAX_TOKENS = 8192
REQUEST_TIMEOUT = 600
MAX_RETRIES = 3
RETRY_BACKOFF_SECONDS = 3


# ==========================================================
# LOGGING
# ==========================================================

def setup_logger(name: str) -> logging.Logger:
    """Create (or fetch) a module-level logger with a consistent format."""
    ensure_log_dir()

    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Chapter content routinely contains non-ASCII symbols (pi, curly
    # quotes, subscripts). Windows consoles often default to a narrow
    # codepage that can't encode them, so force UTF-8 on stdout rather than
    # letting a stray log message crash the pipeline.
    stdout = sys.stdout
    try:
        stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

    stream_handler = logging.StreamHandler(stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    file_handler = logging.FileHandler(LOG_DIR / "pipeline.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.propagate = False
    return logger


# ==========================================================
# FILESYSTEM HELPERS
# ==========================================================

def ensure_log_dir() -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)


def save_json(data: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(f"Required JSON file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_raw_response(text: str, filename: str) -> Path:
    ensure_log_dir()
    path = LOG_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Required text file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# ==========================================================
# CHAPTER RESOLUTION
#
# A "chapter" is identified by the lowercased stem of its teacher_notes
# file (e.g. teacher_notes/Solutions.txt -> "solutions"). Every stage of
# the pipeline (concepts/, formulas/, reports/) uses this same key so
# outputs for a chapter always line up.
# ==========================================================

def chapter_key(notes_path: Path) -> str:
    return notes_path.stem.lower()


def list_teacher_notes() -> List[Path]:
    return sorted(TEACHER_NOTES_DIR.glob("*.txt"))


def resolve_chapters(arg: Optional[str]) -> List[Path]:
    """Resolves a CLI argument to the teacher_notes file(s) to process.

    No argument -> every .txt file in teacher_notes/ (folder processing).
    An argument -> the single matching file, looked up by stem (case
    insensitive, with or without the .txt extension).
    """
    if arg is None:
        notes = list_teacher_notes()
        if not notes:
            raise FileNotFoundError(f"No .txt files found in {TEACHER_NOTES_DIR}")
        return notes

    target = Path(arg).stem.lower()
    for notes_path in list_teacher_notes():
        if chapter_key(notes_path) == target:
            return [notes_path]

    raise FileNotFoundError(f"No teacher notes matching '{arg}' found in {TEACHER_NOTES_DIR}")


# ==========================================================
# JSON EXTRACTION
# ==========================================================

def extract_json_candidate(text: str) -> str:
    """Strip markdown fences / stray prose and isolate the JSON body.

    Handles both object-rooted ({...}) and array-rooted ([...]) responses,
    picking whichever bracket kind opens first in the cleaned text.
    """
    cleaned = text.strip()

    cleaned = re.sub(r"^```(?:json)?", "", cleaned, flags=re.IGNORECASE).strip()
    cleaned = re.sub(r"```$", "", cleaned).strip()

    first_obj = cleaned.find("{")
    first_arr = cleaned.find("[")

    if first_arr != -1 and (first_obj == -1 or first_arr < first_obj):
        start, end = first_arr, cleaned.rfind("]")
    else:
        start, end = first_obj, cleaned.rfind("}")

    if start != -1 and end != -1 and end > start:
        return cleaned[start:end + 1]

    return cleaned


def parse_json_response(text: str) -> Any:
    """Raises ValueError with a useful message if parsing fails."""
    candidate = extract_json_candidate(text)
    try:
        return json.loads(candidate)
    except json.JSONDecodeError as e:
        raise ValueError(f"Could not parse JSON: {e}") from e


def validate_json(data: Any, required_fields: List[str]) -> None:
    """Generic top-level shape check: data is a dict containing every field."""
    if not isinstance(data, dict):
        raise ValueError("Response is not a JSON object")
    missing = [f for f in required_fields if f not in data]
    if missing:
        raise ValueError(f"Missing required field(s): {missing}")


# ==========================================================
# LLM CLIENT
# ==========================================================

def call_llm(
    system_prompt: str,
    user_prompt: str,
    logger: logging.Logger,
    model: str = MODEL,
    temperature: float = TEMPERATURE,
    url: str = LMSTUDIO_URL,
    timeout: int = REQUEST_TIMEOUT,
    max_tokens: int = MAX_TOKENS,
) -> str:
    """Single call to the LM Studio chat-completions endpoint. Returns raw content string."""
    payload = {
        "model": model,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    }

    response = requests.post(url, json=payload, timeout=timeout)
    response.raise_for_status()

    result = response.json()
    choice = result["choices"][0]
    content = choice["message"]["content"]

    if choice.get("finish_reason") == "length":
        logger.warning(
            f"Response was truncated at max_tokens={max_tokens} (finish_reason=length)"
        )

    return content


def retry_request(
    func: Callable[[], Any],
    logger: logging.Logger,
    max_retries: int = MAX_RETRIES,
    backoff_seconds: float = RETRY_BACKOFF_SECONDS,
    description: str = "request",
) -> Any:
    """Generic retry wrapper for any zero-arg callable that may raise."""
    last_error: Optional[Exception] = None

    for attempt in range(1, max_retries + 1):
        try:
            return func()
        except Exception as e:
            last_error = e
            logger.warning(f"{description} attempt {attempt}/{max_retries} failed: {e}")
            if attempt < max_retries:
                time.sleep(backoff_seconds)

    raise RuntimeError(f"{description} failed after {max_retries} attempts: {last_error}")


def call_llm_json(
    system_prompt: str,
    user_prompt: str,
    logger: logging.Logger,
    validator: Optional[Callable[[Any], None]] = None,
    max_retries: int = MAX_RETRIES,
    model: str = MODEL,
    temperature: float = TEMPERATURE,
    url: str = LMSTUDIO_URL,
    timeout: int = REQUEST_TIMEOUT,
    max_tokens: int = MAX_TOKENS,
    raw_dump_filename: str = "raw_output.txt",
) -> Any:
    """
    Calls the LLM and parses a JSON value (object or array) from the
    response, retrying on parse/validation failure. On the final failure the
    raw response is saved to logs/<raw_dump_filename> and the exception is
    re-raised.

    `validator`, if given, receives the parsed value and must raise
    ValueError if it is structurally/semantically invalid.
    """
    last_error: Optional[Exception] = None
    last_raw: str = ""
    current_user_prompt = user_prompt
    current_max_tokens = max_tokens

    for attempt in range(1, max_retries + 1):
        logger.info(f"LLM call attempt {attempt}/{max_retries} (max_tokens={current_max_tokens})")

        try:
            raw = call_llm(
                system_prompt=system_prompt,
                user_prompt=current_user_prompt,
                logger=logger,
                model=model,
                temperature=temperature,
                url=url,
                timeout=timeout,
                max_tokens=current_max_tokens,
            )
            last_raw = raw

            parsed = parse_json_response(raw)

            if validator is not None:
                validator(parsed)

            logger.info("LLM response parsed and validated successfully")
            return parsed

        except Exception as e:
            last_error = e
            logger.warning(f"Attempt {attempt} failed: {e}")

            current_user_prompt = (
                f"{user_prompt}\n\n"
                f"IMPORTANT: Your previous response was invalid ({e}). "
                f"Return ONLY a single valid JSON value matching the required schema. "
                f"No markdown, no explanation, no code fences."
            )

            # A likely cause of parse failure is truncation; give the next
            # attempt more headroom regardless of the exact error.
            current_max_tokens = min(current_max_tokens * 2, 32768)

            if attempt < max_retries:
                time.sleep(RETRY_BACKOFF_SECONDS)

    logger.error(f"All {max_retries} attempts failed. Saving raw response for inspection.")
    if last_raw:
        dump_path = save_raw_response(last_raw, raw_dump_filename)
        logger.error(f"Raw response saved to {dump_path}")

    raise RuntimeError(f"LLM call failed after {max_retries} attempts: {last_error}")


# ==========================================================
# TEXT NORMALISATION HELPERS
# ==========================================================

def normalize_name(name: str) -> str:
    """Lower-case, whitespace-collapsed key used for de-duplication/matching."""
    return re.sub(r"\s+", " ", name.strip().lower())
