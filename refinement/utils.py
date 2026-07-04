"""
Shared utilities for the Concept Intelligence Engine (refinement pipeline).

Provides:
    - logging setup
    - LM Studio chat-completion client with retries + truncation escalation
    - robust JSON extraction / validation
    - JSON save/load helpers
    - hierarchy cycle detection (shared by the validator and hierarchy refiner)
"""

from __future__ import annotations

import json
import logging
import re
import sys
import time
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Set, Tuple

import requests

# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"

# Phase 1 (kbprocess/output) is the read-only source of truth for this
# pipeline's inputs. The refinement pipeline never writes there.
PHASE1_OUTPUT_DIR = BASE_DIR.parent / "output"
CONCEPTS_INPUT_FILE = PHASE1_OUTPUT_DIR / "chapter_concepts.json"
KB_INPUT_FILE = PHASE1_OUTPUT_DIR / "chapter_kb.json"

VALIDATION_REPORT_FILE = OUTPUT_DIR / "validation_report.json"
HIERARCHY_FILE = OUTPUT_DIR / "chapter_concepts_hierarchy.json"
NORMALIZED_FILE = OUTPUT_DIR / "chapter_concepts_normalized.json"
RELATIONSHIPS_FILE = OUTPUT_DIR / "chapter_relationships.json"
METADATA_FILE = OUTPUT_DIR / "chapter_metadata.json"
QUESTIONS_REFINED_FILE = OUTPUT_DIR / "chapter_questions_refined.json"
FINAL_KB_FILE = OUTPUT_DIR / "chapter_kb_final.json"
ENRICHED_KB_FILE = OUTPUT_DIR / "chapter_kb_enriched.json"

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
    ensure_output_dir()

    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    file_handler = logging.FileHandler(OUTPUT_DIR / "pipeline.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.propagate = False
    return logger


# ==========================================================
# FILESYSTEM HELPERS
# ==========================================================

def ensure_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def save_json(data: Any, path: Path) -> None:
    ensure_output_dir()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(f"Required JSON file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_raw_response(text: str, filename: str) -> Path:
    ensure_output_dir()
    path = OUTPUT_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def load_phase1_inputs() -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Loads the two read-only Phase 1 artefacts this pipeline is built on."""
    concepts_doc = load_json(CONCEPTS_INPUT_FILE)
    kb_doc = load_json(KB_INPUT_FILE)
    return concepts_doc, kb_doc


# ==========================================================
# JSON EXTRACTION
# ==========================================================

def extract_json_candidate(text: str) -> str:
    """Strip markdown fences / stray prose and isolate the {...} JSON body."""
    cleaned = text.strip()

    cleaned = re.sub(r"^```(?:json)?", "", cleaned, flags=re.IGNORECASE).strip()
    cleaned = re.sub(r"```$", "", cleaned).strip()

    start = cleaned.find("{")
    end = cleaned.rfind("}")

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
    Calls the LLM and parses a JSON object from the response, retrying on
    parse/validation failure. On the final failure the raw response is saved
    to output/<raw_dump_filename> and the exception is re-raised.

    `validator`, if given, receives the parsed object and must raise
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
                f"Return ONLY a single valid JSON object matching the required schema. "
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


# ==========================================================
# HIERARCHY HELPERS
# ==========================================================

def find_hierarchy_cycles(concept_tree: List[Dict[str, Any]]) -> List[List[str]]:
    """
    Walks each concept's parent chain looking for cycles.

    Returns a list of cycles, each expressed as a list of concept_names
    forming the loop (e.g. ["A", "B", "C", "A"]).
    """
    name_to_parent = {c["concept_name"]: c.get("parent_concept", "") for c in concept_tree}
    cycles: List[List[str]] = []
    seen_cycle_keys: Set[frozenset] = set()

    for start_name in name_to_parent:
        path: List[str] = []
        visited_in_path: Set[str] = set()
        current = start_name

        while current:
            if current in visited_in_path:
                cycle_start_index = path.index(current)
                cycle = path[cycle_start_index:] + [current]
                key = frozenset(cycle)
                if key not in seen_cycle_keys:
                    seen_cycle_keys.add(key)
                    cycles.append(cycle)
                break

            visited_in_path.add(current)
            path.append(current)
            current = name_to_parent.get(current, "")

            if len(path) > len(name_to_parent) + 1:
                # Safety valve; should be unreachable given the cycle check above.
                break

    return cycles
