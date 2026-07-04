"""
approach2.py

Builds ONE canonical chapter knowledge base directly from raw educational
chunks (Resonance / NCERT theory, definitions, formulae, examples,
questions, tables) -- in contrast to kbprocess/refinement/, which starts
from an already-extracted concept list. Nothing here is invented: every
concept, formula, example and question must trace back to chunk text.

The final OUTPUT is a single JSON document matching the exact schema
given (chapter / concept_tree / relationships / question_bank). Internally
it still runs as several passes, because the input is ~530 chunks
(~940 KB) -- far more than a local 7B model's context window can take in
one call -- so concepts are discovered and merged INCREMENTALLY, chunk
batch by chunk batch. That is what makes rules 3/4/5 (merge duplicates,
merge synonyms, never duplicate) hold at chapter scale.

Pipeline stages (each checkpointed to disk -- safe to Ctrl-C and rerun):

    1. Load chunks, batch them by cumulative text size
    2. Streaming concept discovery + merge (LLM, one call per chunk batch,
       always compared against the FULL running canonical list so cross-
       topic duplicates get caught too)
    3. Deterministic hierarchy resolution: validate parent references,
       break cycles, decide is_grouping_node, assign stable IDs (CH01_001, ...)
    4. Per-concept enrichment: assessment + retrieval metadata (LLM)
    5. Question bank extraction from content_type=="question" chunks (LLM)
    6. Relationships: hierarchy-derived "part_of" (deterministic) +
       semantic depends_on/related_to/application_of/example_of (LLM)
    7. Quality gate: dedupe / orphan / cycle / linkage / keyword checks,
       with fixes applied and logged

Model: qwen2.5-vl-7b-instruct via LM Studio at http://127.0.0.1:1234

Output:
    approach2_output/chapter_kb.json            -- final canonical KB
    approach2_output/checkpoints/*.json          -- resumable stage state
    approach2_output/approach2.log
"""

from __future__ import annotations

import json
import logging
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

import requests

# ==========================================================
# PATHS
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "kbprocess" / "unit1_solutions_preprocessed.json"

OUTPUT_DIR = BASE_DIR / "approach2_output"
CHECKPOINT_DIR = OUTPUT_DIR / "checkpoints"
FINAL_OUTPUT_FILE = OUTPUT_DIR / "chapter_kb.json"

CANONICAL_CHECKPOINT = CHECKPOINT_DIR / "01_canonical_concepts.json"
HIERARCHY_CHECKPOINT = CHECKPOINT_DIR / "02_concept_tree.json"
ENRICHED_CHECKPOINT = CHECKPOINT_DIR / "03_concept_tree_enriched.json"
QUESTIONS_CHECKPOINT = CHECKPOINT_DIR / "04_question_bank.json"
RELATIONSHIPS_CHECKPOINT = CHECKPOINT_DIR / "05_relationships.json"

# Optional cap for smoke-testing (None = process every chunk).
LIMIT_CHUNKS: Optional[int] = 5

# ==========================================================
# CHAPTER IDENTITY
# ==========================================================

CHAPTER_ID = "CH01"
SUBJECT = "CHEMISTRY"
GRADE = "CLASS-12"

# ==========================================================
# LLM CONFIGURATION
# ==========================================================

LMSTUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"
MODEL = "qwen2.5-vl-7b-instruct"
TEMPERATURE = 0.1
MAX_TOKENS = 4096
REQUEST_TIMEOUT = 600
MAX_RETRIES = 3
RETRY_BACKOFF_SECONDS = 3

# ==========================================================
# BATCHING
# ==========================================================

DISCOVERY_MAX_CHUNKS_PER_BATCH = 8
DISCOVERY_MAX_CHARS_PER_BATCH = 4000

ENRICHMENT_BATCH_SIZE = 5
QUESTION_BATCH_MAX_CHUNKS = 5
QUESTION_BATCH_MAX_CHARS = 4500
RELATIONSHIP_BATCH_SIZE = 12

MIN_CHILDREN_FOR_GROUPING = 1

BLOOMS_CANONICAL = {
    "remember": "Remember", "understand": "Understand", "apply": "Apply",
    "analyze": "Analyze", "analyse": "Analyze", "evaluate": "Evaluate", "create": "Create",
}
ALLOWED_MARKS = {1, 2, 3, 4, 5}
IMPORTANCE_LEVELS = {"high", "medium", "low"}
DIFFICULTY_LEVELS = {"easy", "medium", "hard"}
RELATIONSHIP_TYPES = {"depends_on", "related_to", "contains", "part_of", "application_of", "example_of"}


# ==========================================================
# LOGGING
# ==========================================================

def setup_logger() -> logging.Logger:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("approach2")
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter(fmt="%(asctime)s | %(levelname)-8s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(fmt)
    logger.addHandler(sh)
    fh = logging.FileHandler(OUTPUT_DIR / "approach2.log", encoding="utf-8")
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    logger.propagate = False
    return logger


LOGGER = setup_logger()


# ==========================================================
# JSON / FILESYSTEM HELPERS
# ==========================================================

def save_json(data: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_json_candidate(text: str) -> str:
    cleaned = text.strip()
    cleaned = re.sub(r"^```(?:json)?", "", cleaned, flags=re.IGNORECASE).strip()
    cleaned = re.sub(r"```$", "", cleaned).strip()
    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start != -1 and end != -1 and end > start:
        return cleaned[start:end + 1]
    return cleaned


JSON_BACKSLASH_SANITIZE_PATTERN = re.compile(r'\\(?!["\\/]|u[0-9a-fA-F]{4}|[bfnrt](?![a-zA-Z]))')


def sanitize_json_backslashes(text: str) -> str:
    """Source chunks are full of raw LaTeX (\\frac{...}, \\times, \\Delta, ...).
    The model routinely echoes that LaTeX straight into JSON string values
    without escaping the backslash. A naive "escape anything not in
    [\"\\/bfnrtu]" fix still corrupts \\frac/\\times/\\right etc. (json.loads
    happily consumes "\\f"/"\\t"/"\\r" as a real escape char and silently
    swallows the rest of the LaTeX word), so a real JSON escape is only
    recognised as \\b \\f \\n \\r \\t when NOT immediately followed by
    another letter (a genuine control-char escape is never glued to more
    letters; a LaTeX command always is). Everything else gets doubled."""
    return JSON_BACKSLASH_SANITIZE_PATTERN.sub(r"\\\\", text)


def parse_json_response(text: str) -> Any:
    candidate = extract_json_candidate(text)
    try:
        return json.loads(candidate)
    except json.JSONDecodeError:
        pass
    try:
        return json.loads(sanitize_json_backslashes(candidate))
    except json.JSONDecodeError as e:
        raise ValueError(f"Could not parse JSON: {e}") from e


def normalize_name(name: str) -> str:
    return re.sub(r"\s+", " ", str(name).strip().lower())


# ==========================================================
# LLM CLIENT
# ==========================================================

def call_llm(system_prompt: str, user_prompt: str, max_tokens: int = MAX_TOKENS) -> Tuple[str, str]:
    payload = {
        "model": MODEL,
        "temperature": TEMPERATURE,
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
    validator=None,
    max_retries: int = MAX_RETRIES,
    max_tokens: int = MAX_TOKENS,
    raw_dump_name: str = "raw_output.txt",
) -> Any:
    last_error: Optional[Exception] = None
    last_raw = ""
    current_prompt = user_prompt
    current_max_tokens = max_tokens

    for attempt in range(1, max_retries + 1):
        try:
            raw, finish_reason = call_llm(system_prompt, current_prompt, current_max_tokens)
            last_raw = raw
            if finish_reason == "length":
                LOGGER.warning(f"Response truncated at max_tokens={current_max_tokens}")
            parsed = parse_json_response(raw)
            if validator is not None:
                validator(parsed)
            return parsed
        except Exception as e:
            last_error = e
            LOGGER.warning(f"LLM call attempt {attempt}/{max_retries} failed: {e}")
            current_prompt = (
                f"{user_prompt}\n\nIMPORTANT: Your previous response was invalid ({e}). "
                f"Return ONLY a single valid JSON object matching the required schema. "
                f"No markdown, no explanation, no code fences."
            )
            current_max_tokens = min(current_max_tokens * 2, 32768)
            if attempt < max_retries:
                time.sleep(RETRY_BACKOFF_SECONDS)

    if last_raw:
        dump_path = CHECKPOINT_DIR / raw_dump_name
        dump_path.parent.mkdir(parents=True, exist_ok=True)
        with open(dump_path, "w", encoding="utf-8") as f:
            f.write(last_raw)
        LOGGER.error(f"Raw response saved to {dump_path}")

    raise RuntimeError(f"LLM call failed after {max_retries} attempts: {last_error}")


# ==========================================================
# STAGE 0 -- LOAD & BATCH CHUNKS
# ==========================================================

def load_chunks() -> List[Dict[str, Any]]:
    chunks = load_json(INPUT_FILE)
    if LIMIT_CHUNKS:
        chunks = chunks[:LIMIT_CHUNKS]
    LOGGER.info(f"Loaded {len(chunks)} chunk(s) from {INPUT_FILE.name}")
    return chunks


def batch_chunks(chunks: List[Dict[str, Any]]) -> List[List[Dict[str, Any]]]:
    batches: List[List[Dict[str, Any]]] = []
    current: List[Dict[str, Any]] = []
    current_chars = 0

    for c in chunks:
        text_len = len(c.get("document", ""))
        if current and (
            len(current) >= DISCOVERY_MAX_CHUNKS_PER_BATCH
            or current_chars + text_len > DISCOVERY_MAX_CHARS_PER_BATCH
        ):
            batches.append(current)
            current, current_chars = [], 0
        current.append(c)
        current_chars += text_len

    if current:
        batches.append(current)
    return batches


# ==========================================================
# STAGE 1 -- STREAMING CONCEPT DISCOVERY + MERGE
# ==========================================================

DISCOVERY_SYSTEM_PROMPT = """You are a Senior NCERT Curriculum Designer, CBSE Question Paper Setter,
Educational Knowledge Graph Architect, and Subject Matter Expert in Chemistry.

You are building ONE canonical chapter knowledge base incrementally, chunk
batch by chunk batch. You are shown the CURRENT running list of canonical
concepts already discovered, and a NEW batch of source chunks to read.

STRICT RULES

1. Use ONLY information present in the given chunks. Never invent concepts,
   formulae, or examples.
2. For each idea you find in the new chunks, decide:
   - "merge": it is the SAME concept as one already in the canonical list
     (including synonyms -- e.g. "Molar Concentration" and "Molarity" are
     the SAME concept; "Henry Constant", "Henry's Constant", "Henry Law",
     "Henry's Law" are all the SAME concept -- prefer the standard NCERT
     name as canonical and keep the others as aliases). Use the EXACT
     target_name string as it appears in the canonical list.
   - "new": it is a genuinely new concept not yet in the canonical list.
3. Never propose the same new concept twice across your own output.
4. concept_name for "new" entries should be the standard NCERT/textbook
   name (e.g. "Henry's Law", not "Henry Law" or "Henry's Constant Law").
5. suggested_parent: the name of another concept (existing canonical name,
   or a "new" concept_name you are ALSO proposing in this same batch) that
   this concept should nest under in a teacher-style hierarchy (e.g.
   "Molarity" -> parent "Expression of Concentration" -> parent
   "Solutions"). Empty string if this is a top-level chapter concept.
6. is_grouping_node_hint: true only if this concept is a broad
   organisational topic header (e.g. "Solutions", "Colligative
   Properties", "Expression of Concentration") rather than an
   independently examinable idea.
7. source_chunk_indices: the numeric index/indices (as given in the
   "New chunks" list below, e.g. 1, 2, 3) that this update's information
   came from.
8. Do not repeat information already captured -- only add genuinely new
   detail (new alias, new formula, new example, extra definition detail).
9. Return ONLY valid JSON. No markdown. No explanation. No code fences.

Output schema:

{
    "updates": [
        {
            "action": "merge",
            "target_name": "",
            "new_aliases": [],
            "definition_addition": "",
            "formulae_addition": [],
            "examples_addition": [],
            "source_chunk_indices": []
        },
        {
            "action": "new",
            "concept_name": "",
            "aliases": [],
            "definition": "",
            "formulae": [],
            "examples": [],
            "suggested_parent": "",
            "is_grouping_node_hint": false,
            "category_hint": "",
            "topic": "",
            "source_chunk_indices": []
        }
    ]
}
"""

DISCOVERY_USER_TEMPLATE = """Chapter: {chapter}

CURRENT canonical concept list ({count} concept(s) so far):
{canonical_list}

NEW chunks to read (extract/merge concepts from these):
{chunk_list}
"""


def format_canonical_list_compact(canonical: Dict[str, Dict[str, Any]]) -> str:
    if not canonical:
        return "(empty -- this is the first batch)"
    lines = []
    for entry in canonical.values():
        alias_part = f" [aliases: {', '.join(entry['aliases'])}]" if entry["aliases"] else ""
        parent_part = f" (parent: {entry['parent_hint']})" if entry["parent_hint"] else ""
        lines.append(f"- {entry['concept_name']}{alias_part}{parent_part}")
    return "\n".join(lines)


def format_chunk_list(chunks: List[Dict[str, Any]]) -> str:
    lines = []
    for i, c in enumerate(chunks, start=1):
        lines.append(
            f"[{i}] topic={c.get('topic', '')} | type={c.get('content_type', '')} | context={c.get('context', '')}\n"
            f"{c.get('document', '').strip()}\n"
        )
    return "\n".join(lines)


def make_discovery_validator():
    def validator(parsed: Any) -> None:
        if not isinstance(parsed, dict) or "updates" not in parsed:
            raise ValueError("Missing 'updates'")
        if not isinstance(parsed["updates"], list):
            raise ValueError("'updates' is not a list")
        for i, u in enumerate(parsed["updates"]):
            if not isinstance(u, dict):
                raise ValueError(f"updates[{i}] is not an object")
            if u.get("action") not in ("merge", "new"):
                raise ValueError(f"updates[{i}] invalid 'action'")
            if u["action"] == "merge" and not str(u.get("target_name", "")).strip():
                raise ValueError(f"updates[{i}] merge missing 'target_name'")
            if u["action"] == "new" and not str(u.get("concept_name", "")).strip():
                raise ValueError(f"updates[{i}] new missing 'concept_name'")
    return validator


def new_canonical_entry(concept_name: str) -> Dict[str, Any]:
    return {
        "concept_name": concept_name,
        "aliases": [],
        "definition": "",
        "formulae": [],
        "examples": [],
        "parent_hint": "",
        "is_grouping_node_hint": False,
        "category_hint": "",
        "topic": "",
        "source_chunk_ids": [],
    }


def dedup_extend(target: List[str], new_items: List[Any]) -> None:
    seen = {normalize_name(x) for x in target}
    for item in new_items:
        text = str(item).strip()
        if text and normalize_name(text) not in seen:
            target.append(text)
            seen.add(normalize_name(text))


def apply_update(canonical: Dict[str, Dict[str, Any]], update: Dict[str, Any], chunk_ids_by_index: Dict[int, str]) -> None:
    src_ids = [chunk_ids_by_index[i] for i in update.get("source_chunk_indices", []) if i in chunk_ids_by_index]

    if update["action"] == "merge":
        key = normalize_name(update["target_name"])
        if key not in canonical:
            # LLM referenced a target that doesn't exist -- fall back to treating it as new,
            # never silently drop information from the chunks.
            LOGGER.warning(f"Merge target not found, creating new concept instead: {update['target_name']!r}")
            entry = new_canonical_entry(update["target_name"])
            canonical[key] = entry
        entry = canonical[key]
        dedup_extend(entry["aliases"], update.get("new_aliases", []))
        addition = str(update.get("definition_addition", "")).strip()
        if addition and addition.lower() not in entry["definition"].lower():
            entry["definition"] = (entry["definition"] + " " + addition).strip() if entry["definition"] else addition
        dedup_extend(entry["formulae"], update.get("formulae_addition", []))
        dedup_extend(entry["examples"], update.get("examples_addition", []))
        for cid in src_ids:
            if cid not in entry["source_chunk_ids"]:
                entry["source_chunk_ids"].append(cid)
        return

    # action == "new"
    key = normalize_name(update["concept_name"])
    if key in canonical:
        # Model proposed "new" for something already canonical -- treat as merge.
        apply_update(canonical, {**update, "action": "merge", "target_name": canonical[key]["concept_name"]}, chunk_ids_by_index)
        return

    entry = new_canonical_entry(str(update["concept_name"]).strip())
    dedup_extend(entry["aliases"], update.get("aliases", []))
    entry["definition"] = str(update.get("definition", "")).strip()
    dedup_extend(entry["formulae"], update.get("formulae", []))
    dedup_extend(entry["examples"], update.get("examples", []))
    entry["parent_hint"] = str(update.get("suggested_parent", "")).strip()
    entry["is_grouping_node_hint"] = bool(update.get("is_grouping_node_hint", False))
    entry["category_hint"] = str(update.get("category_hint", "")).strip()
    entry["topic"] = str(update.get("topic", "")).strip()
    entry["source_chunk_ids"] = list(dict.fromkeys(src_ids))
    canonical[key] = entry


def load_discovery_checkpoint() -> Tuple[Dict[str, Dict[str, Any]], int]:
    if CANONICAL_CHECKPOINT.exists():
        data = load_json(CANONICAL_CHECKPOINT)
        canonical = {normalize_name(v["concept_name"]): v for v in data["canonical"]}
        LOGGER.info(f"Resuming discovery from checkpoint: batch {data['next_batch_index']}, {len(canonical)} concept(s) so far")
        return canonical, data["next_batch_index"]
    return {}, 0


def save_discovery_checkpoint(canonical: Dict[str, Dict[str, Any]], next_batch_index: int) -> None:
    save_json({"next_batch_index": next_batch_index, "canonical": list(canonical.values())}, CANONICAL_CHECKPOINT)


def run_discovery(chapter: str, chunks: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    batches = batch_chunks(chunks)
    LOGGER.info(f"Stage 1: discovery over {len(chunks)} chunk(s) in {len(batches)} batch(es)")

    canonical, start_index = load_discovery_checkpoint()

    for batch_num in range(start_index, len(batches)):
        batch = batches[batch_num]
        chunk_ids_by_index = {i: c.get("original_id", f"unknown_{i}") for i, c in enumerate(batch, start=1)}

        LOGGER.info(f"Discovery batch {batch_num + 1}/{len(batches)} ({len(batch)} chunk(s), {len(canonical)} canonical concept(s) so far)")

        user_prompt = DISCOVERY_USER_TEMPLATE.format(
            chapter=chapter,
            count=len(canonical),
            canonical_list=format_canonical_list_compact(canonical),
            chunk_list=format_chunk_list(batch),
        )

        try:
            parsed = call_llm_json(
                system_prompt=DISCOVERY_SYSTEM_PROMPT,
                user_prompt=user_prompt,
                validator=make_discovery_validator(),
                raw_dump_name=f"discovery_batch{batch_num + 1}_raw.txt",
            )
            for update in parsed["updates"]:
                apply_update(canonical, update, chunk_ids_by_index)
        except Exception as e:
            LOGGER.error(f"Discovery batch {batch_num + 1} failed permanently, skipping (chunks preserved for manual review): {e}")

        save_discovery_checkpoint(canonical, batch_num + 1)

    LOGGER.info(f"Stage 1 complete: {len(canonical)} canonical concept(s) discovered")
    return canonical


# ==========================================================
# STAGE 2 -- DETERMINISTIC HIERARCHY RESOLUTION + STABLE IDS
# ==========================================================

def resolve_hierarchy(canonical: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    name_by_key = {k: v["concept_name"] for k, v in canonical.items()}

    # 1) Resolve parent_hint -> a validated parent_concept name (or "" if dangling/self).
    parent_of: Dict[str, str] = {}
    for key, entry in canonical.items():
        hint_key = normalize_name(entry["parent_hint"])
        if hint_key and hint_key in canonical and hint_key != key:
            parent_of[key] = name_by_key[hint_key]
        else:
            if entry["parent_hint"]:
                LOGGER.warning(f"Dropping dangling/self parent hint for {entry['concept_name']!r}: {entry['parent_hint']!r}")
            parent_of[key] = ""

    # 2) Break cycles.
    for start_key in list(canonical.keys()):
        path: List[str] = []
        visited: Set[str] = set()
        current = start_key
        while current:
            if current in visited:
                cut_key = path[-1]
                LOGGER.warning(f"Cycle detected involving {canonical[cut_key]['concept_name']!r}; detaching to top-level")
                parent_of[cut_key] = ""
                break
            visited.add(current)
            path.append(current)
            nxt = parent_of.get(current, "")
            current = normalize_name(nxt) if nxt else ""
            if len(path) > len(canonical) + 1:
                break

    # 3) Children counts -> is_grouping_node.
    children_count: Dict[str, int] = {}
    for key in canonical:
        p = parent_of.get(key, "")
        if p:
            children_count[normalize_name(p)] = children_count.get(normalize_name(p), 0) + 1

    # 4) Stable ID assignment in teacher-taught (BFS, first-discovery) order.
    children_by_parent: Dict[str, List[str]] = {}
    roots: List[str] = []
    for key in canonical:  # dict preserves first-discovery insertion order
        p = parent_of.get(key, "")
        if p:
            children_by_parent.setdefault(normalize_name(p), []).append(key)
        else:
            roots.append(key)

    ordered_keys: List[str] = []

    def visit(key: str) -> None:
        if key in ordered_keys:
            return
        ordered_keys.append(key)
        for child_key in children_by_parent.get(key, []):
            visit(child_key)

    for root_key in roots:
        visit(root_key)
    for key in canonical:  # safety net for anything unreachable (shouldn't happen)
        if key not in ordered_keys:
            visit(key)

    concept_tree: List[Dict[str, Any]] = []
    id_by_key: Dict[str, str] = {}
    for i, key in enumerate(ordered_keys, start=1):
        id_by_key[key] = f"{CHAPTER_ID}_{i:03d}"

    for key in ordered_keys:
        entry = canonical[key]
        has_children = children_count.get(key, 0) >= MIN_CHILDREN_FOR_GROUPING
        parent_name = parent_of.get(key, "")
        concept_tree.append({
            "concept_id": id_by_key[key],
            "concept_name": entry["concept_name"],
            "parent_concept": parent_name,
            "is_grouping_node": bool(entry["is_grouping_node_hint"] and has_children),
            "official_name": entry["concept_name"],
            "aliases": entry["aliases"],
            "search_terms": [],
            "abbreviations": [a for a in entry["aliases"] if len(a) <= 6 and a.isupper()],
            "definition": entry["definition"],
            "formulae": entry["formulae"],
            "examples": entry["examples"],
            "related_concepts": [],
            "importance": "",
            "chapter_weightage": "",
            "concept_category": "",
            "concept_type": "",
            "prerequisites": [],
            "difficulty_hint": "",
            "learning_outcomes": [],
            "_category_hint": entry["category_hint"],
            "_topic": entry["topic"],
            "_source_chunk_ids": entry["source_chunk_ids"],
        })

    LOGGER.info(f"Stage 2 complete: {len(concept_tree)} concept(s), {len(roots)} top-level, "
                f"{sum(1 for c in concept_tree if c['is_grouping_node'])} grouping node(s)")
    return concept_tree


# ==========================================================
# STAGE 3 -- ENRICHMENT (assessment + retrieval metadata)
# ==========================================================

ENRICHMENT_SYSTEM_PROMPT = """You are a Senior NCERT Curriculum Designer, CBSE Paper Setter, Educational
Knowledge Graph Architect, and Assessment Expert in Chemistry.

You are given a fixed list of already-finalised concepts (with their
definitions) from one NCERT chapter. Annotate each with exam-assessment
and retrieval metadata for a question-paper generation system.

RULES

1. Use ONLY the concept_id values given. Never add/rename/invent concepts.
2. Return exactly one entry per concept_id given.
3. importance: "high"/"medium"/"low" -- how central this concept is to the
   chapter overall.
4. chapter_weightage: "high"/"medium"/"low" -- how often this concept is
   likely to be examined (grouping/organisational nodes are typically low).
5. concept_category: one of "Core Concept", "Law", "Principle", "Process",
   "Definition", "Formula", "Application", "Measurement", "Phenomenon".
   Prefer the most specific fit -- do not default everything to
   "Core Concept". "Measurement" = a way of expressing/quantifying an
   amount (e.g. Molarity, Normality, ppm). "Law" = a named formal law
   (e.g. Henry's Law). "Process" = a mechanism/action (e.g. Osmosis).
6. concept_type: "Conceptual", "Numerical", "Factual", or "Law".
7. prerequisites: concept_id values (from the given list ONLY) a student
   should understand first. Empty list if none.
8. difficulty_hint: "easy"/"medium"/"hard".
9. learning_outcomes: 1-3 {"verb","object"} pairs, e.g.
   {"verb":"Explain","object":"Henry's Law"}.
10. preferred_question_types: 1-3 of "MCQ", "Very Short Answer",
    "Short Answer", "Long Answer", "Numerical", "Assertion-Reason",
    "Case-Based", "HOTS".
11. recommended_marks: 1-2 integers from {1,2,3,4,5}.
12. blooms_levels: 1-2 of "Remember","Understand","Apply","Analyze",
    "Evaluate","Create".
13. competencies: 1-2 short labels, e.g. "Conceptual Understanding",
    "Problem Solving", "Application", "Analytical Thinking".
14. keywords: 3-6 retrieval search terms/synonyms.
15. Do NOT invent facts. Do NOT estimate PYQ/exemplar frequency.
16. Return ONLY valid JSON. No markdown, no explanation, no code fences.

Output schema:

{
    "enrichment": [
        {
            "concept_id": "",
            "importance": "",
            "chapter_weightage": "",
            "concept_category": "",
            "concept_type": "",
            "prerequisites": [],
            "difficulty_hint": "",
            "learning_outcomes": [{"verb": "", "object": ""}],
            "preferred_question_types": [],
            "recommended_marks": [],
            "blooms_levels": [],
            "competencies": [],
            "keywords": []
        }
    ]
}
"""

ENRICHMENT_USER_TEMPLATE = """Chapter: {chapter}

Concepts to annotate:
{concept_list}
"""


def format_enrichment_concept_list(concepts: List[Dict[str, Any]]) -> str:
    lines = []
    for c in concepts:
        lines.append(f"- {c['concept_id']}: {c['concept_name']}" + (" [grouping/topic header]" if c["is_grouping_node"] else ""))
        if c.get("definition"):
            lines.append(f"  Definition: {c['definition']}")
        if c.get("formulae"):
            lines.append(f"  Formulae: {', '.join(c['formulae'])}")
        if c.get("parent_concept"):
            lines.append(f"  Parent: {c['parent_concept']}")
        if c.get("_category_hint"):
            lines.append(f"  Category hint: {c['_category_hint']}")
    return "\n".join(lines)


def make_enrichment_validator(valid_ids: Set[str]):
    def validator(parsed: Any) -> None:
        if not isinstance(parsed, dict) or "enrichment" not in parsed or not isinstance(parsed["enrichment"], list):
            raise ValueError("Missing/invalid 'enrichment'")
        for i, item in enumerate(parsed["enrichment"]):
            if not isinstance(item, dict) or item.get("concept_id") not in valid_ids:
                raise ValueError(f"enrichment[{i}] missing/unknown concept_id")
            for field in ("importance", "chapter_weightage", "concept_category", "concept_type", "difficulty_hint"):
                if not isinstance(item.get(field), str):
                    raise ValueError(f"enrichment[{i}] missing/invalid '{field}'")
            for field in ("prerequisites", "learning_outcomes", "preferred_question_types",
                          "recommended_marks", "blooms_levels", "competencies", "keywords"):
                if not isinstance(item.get(field), list):
                    raise ValueError(f"enrichment[{i}] missing/invalid '{field}'")
    return validator


def normalize_enum(value: str, allowed: Set[str], default: str) -> str:
    key = str(value).strip().lower()
    return key if key in allowed else default


CONCEPT_CATEGORIES = {
    "core concept": "Core Concept", "law": "Law", "principle": "Principle", "process": "Process",
    "definition": "Definition", "formula": "Formula", "application": "Application",
    "measurement": "Measurement", "phenomenon": "Phenomenon",
}


def default_assessment_for(category: str) -> Dict[str, Any]:
    if category in ("Law", "Formula", "Measurement"):
        return {"preferred_question_types": ["Numerical", "Short Answer"], "recommended_marks": [2, 3],
                "blooms_levels": ["Apply", "Analyze"], "competencies": ["Problem Solving", "Application"]}
    if category == "Definition":
        return {"preferred_question_types": ["Very Short Answer", "MCQ"], "recommended_marks": [1, 2],
                "blooms_levels": ["Remember", "Understand"], "competencies": ["Conceptual Understanding"]}
    return {"preferred_question_types": ["Short Answer"], "recommended_marks": [2, 3],
            "blooms_levels": ["Understand", "Apply"], "competencies": ["Conceptual Understanding", "Analytical Thinking"]}


def build_keywords(concept: Dict[str, Any], llm_keywords: List[Any]) -> List[str]:
    candidates = [concept["concept_name"], *concept.get("aliases", []), *[str(k) for k in llm_keywords]]
    result, seen = [], set()
    for text in candidates:
        text = str(text).strip()
        key = text.lower()
        if text and key not in seen:
            seen.add(key)
            result.append(text)
    return result[:12]


def run_enrichment(chapter: str, concept_tree: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    if ENRICHED_CHECKPOINT.exists():
        LOGGER.info("Stage 3: resuming from checkpoint")
        return load_json(ENRICHED_CHECKPOINT)

    valid_ids = {c["concept_id"] for c in concept_tree}
    enriched_by_id: Dict[str, Dict[str, Any]] = {}

    batches = [concept_tree[i:i + ENRICHMENT_BATCH_SIZE] for i in range(0, len(concept_tree), ENRICHMENT_BATCH_SIZE)]
    LOGGER.info(f"Stage 3: enrichment in {len(batches)} batch(es)")

    for batch_num, batch in enumerate(batches, start=1):
        LOGGER.info(f"Enrichment batch {batch_num}/{len(batches)} ({len(batch)} concept(s))")
        user_prompt = ENRICHMENT_USER_TEMPLATE.format(chapter=chapter, concept_list=format_enrichment_concept_list(batch))
        try:
            parsed = call_llm_json(
                system_prompt=ENRICHMENT_SYSTEM_PROMPT,
                user_prompt=user_prompt,
                validator=make_enrichment_validator(valid_ids),
                raw_dump_name=f"enrichment_batch{batch_num}_raw.txt",
            )
            for item in parsed["enrichment"]:
                enriched_by_id[item["concept_id"]] = item
        except Exception as e:
            LOGGER.error(f"Enrichment batch {batch_num} failed permanently, defaulting its concepts: {e}")

    concept_tree_out = []
    for c in concept_tree:
        item = enriched_by_id.get(c["concept_id"], {})
        category = normalize_enum(item.get("concept_category", ""), set(CONCEPT_CATEGORIES), "")
        category = CONCEPT_CATEGORIES.get(category, "") or CONCEPT_CATEGORIES.get(
            normalize_enum(c.get("_category_hint", ""), set(CONCEPT_CATEGORIES), "core concept"), "Core Concept"
        )
        defaults = default_assessment_for(category)

        importance = normalize_enum(item.get("importance", ""), IMPORTANCE_LEVELS, "low" if c["is_grouping_node"] else "medium")
        weightage = normalize_enum(item.get("chapter_weightage", ""), IMPORTANCE_LEVELS, "low" if c["is_grouping_node"] else "medium")
        difficulty = normalize_enum(item.get("difficulty_hint", ""), DIFFICULTY_LEVELS, "medium")
        concept_type = str(item.get("concept_type", "")).strip() or ("Category" if c["is_grouping_node"] else "Conceptual")

        prerequisites = [p for p in item.get("prerequisites", []) if isinstance(p, str) and p in valid_ids and p != c["concept_id"]]

        learning_outcomes = []
        for lo in item.get("learning_outcomes", []):
            if isinstance(lo, dict) and str(lo.get("verb", "")).strip() and str(lo.get("object", "")).strip():
                learning_outcomes.append({"verb": str(lo["verb"]).strip().capitalize(), "object": str(lo["object"]).strip()})
        if not learning_outcomes and not c["is_grouping_node"]:
            learning_outcomes = [{"verb": "Explain", "object": c["concept_name"]}]

        pqt = [str(x).strip() for x in item.get("preferred_question_types", []) if str(x).strip()] or (defaults["preferred_question_types"] if not c["is_grouping_node"] else [])
        marks = sorted({int(x) for x in item.get("recommended_marks", []) if str(x).isdigit() and int(x) in ALLOWED_MARKS}) or (defaults["recommended_marks"] if not c["is_grouping_node"] else [])
        blooms = [BLOOMS_CANONICAL[str(x).strip().lower()] for x in item.get("blooms_levels", []) if str(x).strip().lower() in BLOOMS_CANONICAL]
        blooms = list(dict.fromkeys(blooms)) or (defaults["blooms_levels"] if not c["is_grouping_node"] else [])
        competencies = [str(x).strip() for x in item.get("competencies", []) if str(x).strip()] or (defaults["competencies"] if not c["is_grouping_node"] else [])
        keywords = build_keywords(c, item.get("keywords", []))

        new_c = dict(c)
        new_c.pop("_category_hint", None)
        topic = new_c.pop("_topic", "")
        source_chunk_ids = new_c.pop("_source_chunk_ids", [])
        new_c.update({
            "importance": importance,
            "chapter_weightage": weightage,
            "concept_category": category,
            "concept_type": concept_type,
            "prerequisites": prerequisites,
            "difficulty_hint": difficulty,
            "learning_outcomes": learning_outcomes,
            "assessment": {
                "preferred_question_types": pqt,
                "recommended_marks": marks,
                "blooms_levels": blooms,
                "competencies": competencies,
                "board_frequency": {"ncert": weightage, "exemplar": "NA", "pyq": "NA"},
            },
            "retrieval": {
                "keywords": keywords,
                "chunk_ids": list(source_chunk_ids),
                "formula_ids": [],
                "example_ids": [],
                "pyq_ids": [],
            },
        })
        new_c["_topic"] = topic
        new_c["_source_chunk_ids"] = source_chunk_ids
        concept_tree_out.append(new_c)

    save_json(concept_tree_out, ENRICHED_CHECKPOINT)
    LOGGER.info(f"Stage 3 complete: {len(concept_tree_out)} concept(s) enriched")
    return concept_tree_out


# ==========================================================
# STAGE 4 -- QUESTION BANK
# ==========================================================

QUESTION_SYSTEM_PROMPT = """You are a CBSE Question Paper Setter. You are given raw source chunks that
each contain a question (and usually its worked solution inline, e.g.
after "Sol."). Turn each chunk into ONE clean question+answer object and
link it to the concept(s) it tests.

RULES

1. Use ONLY the text given. Do not invent a question or answer that is
   not present in the chunk.
2. question: the clean question stem (keep options inline for MCQs).
3. answer: the final answer and/or key solution steps/working already
   present in the chunk. If genuinely no solution/answer text is present,
   return "".
4. type: one of "MCQ", "Very Short Answer", "Short Answer", "Long Answer",
   "Numerical", "Assertion-Reason".
5. linked_concepts: one or more concept_id values chosen ONLY from the
   given concept reference list, for the concept(s) this question
   actually tests. Never invent a concept_id.
6. Return exactly one entry per chunk index given.
7. Return ONLY valid JSON. No markdown, no explanation, no code fences.

Output schema:

{
    "questions": [
        {"chunk_index": 1, "question": "", "answer": "", "type": "", "linked_concepts": []}
    ]
}
"""

QUESTION_USER_TEMPLATE = """Chapter: {chapter}

Concept reference list (id: name):
{concept_ref_list}

Question chunks:
{chunk_list}
"""


def is_question_chunk(chunk: Dict[str, Any]) -> bool:
    return "question" in str(chunk.get("content_type", "")).lower()


def batch_question_chunks(chunks: List[Dict[str, Any]]) -> List[List[Dict[str, Any]]]:
    batches: List[List[Dict[str, Any]]] = []
    current: List[Dict[str, Any]] = []
    current_chars = 0
    for c in chunks:
        text_len = len(c.get("document", ""))
        if current and (len(current) >= QUESTION_BATCH_MAX_CHUNKS or current_chars + text_len > QUESTION_BATCH_MAX_CHARS):
            batches.append(current)
            current, current_chars = [], 0
        current.append(c)
        current_chars += text_len
    if current:
        batches.append(current)
    return batches


def concept_ref_list_for_topic(concept_tree: List[Dict[str, Any]], topic: str, limit: int = 40) -> List[Dict[str, Any]]:
    same_topic = [c for c in concept_tree if not c["is_grouping_node"] and c.get("_topic") == topic]
    others = [c for c in concept_tree if not c["is_grouping_node"] and c.get("_topic") != topic]
    others_sorted = sorted(others, key=lambda c: -len(c.get("_source_chunk_ids", [])))
    combined = same_topic + others_sorted
    return combined[:limit] if len(combined) > limit else combined


def make_question_validator(valid_indices: Set[int]):
    def validator(parsed: Any) -> None:
        if not isinstance(parsed, dict) or not isinstance(parsed.get("questions"), list):
            raise ValueError("Missing/invalid 'questions'")
        for i, q in enumerate(parsed["questions"]):
            if not isinstance(q, dict) or "chunk_index" not in q:
                raise ValueError(f"questions[{i}] missing 'chunk_index'")
            if not isinstance(q.get("question"), str) or not isinstance(q.get("answer"), str):
                raise ValueError(f"questions[{i}] missing/invalid question/answer text")
            if not isinstance(q.get("linked_concepts"), list):
                raise ValueError(f"questions[{i}] missing/invalid 'linked_concepts'")
    return validator


def keyword_fallback_concept(question_text: str, candidates: List[Dict[str, Any]]) -> Optional[str]:
    words = set(re.findall(r"[a-zA-Z]{4,}", question_text.lower()))
    best_id, best_score = None, 0
    for c in candidates:
        name_words = set(re.findall(r"[a-zA-Z]{4,}", c["concept_name"].lower()))
        score = len(words & name_words)
        if score > best_score:
            best_id, best_score = c["concept_id"], score
    return best_id


def run_question_extraction(chapter: str, chunks: List[Dict[str, Any]], concept_tree: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    if QUESTIONS_CHECKPOINT.exists():
        LOGGER.info("Stage 4: resuming from checkpoint")
        return load_json(QUESTIONS_CHECKPOINT)

    question_chunks = [c for c in chunks if is_question_chunk(c)]
    LOGGER.info(f"Stage 4: {len(question_chunks)} question chunk(s) out of {len(chunks)} total")

    valid_ids = {c["concept_id"] for c in concept_tree}
    batches = batch_question_chunks(question_chunks)
    LOGGER.info(f"Stage 4: extracting questions in {len(batches)} batch(es)")

    all_questions: List[Dict[str, Any]] = []

    for batch_num, batch in enumerate(batches, start=1):
        LOGGER.info(f"Question batch {batch_num}/{len(batches)} ({len(batch)} chunk(s))")
        topic = batch[0].get("topic", "")
        ref_concepts = concept_ref_list_for_topic(concept_tree, topic)
        ref_list_text = "\n".join(f"- {c['concept_id']}: {c['concept_name']}" for c in ref_concepts)
        chunk_list_text = "\n".join(
            f"[{i}] {c.get('document', '').strip()}\n" for i, c in enumerate(batch, start=1)
        )
        user_prompt = QUESTION_USER_TEMPLATE.format(chapter=chapter, concept_ref_list=ref_list_text, chunk_list=chunk_list_text)

        try:
            parsed = call_llm_json(
                system_prompt=QUESTION_SYSTEM_PROMPT,
                user_prompt=user_prompt,
                validator=make_question_validator(set(range(1, len(batch) + 1))),
                raw_dump_name=f"questions_batch{batch_num}_raw.txt",
            )
            by_index = {int(q["chunk_index"]): q for q in parsed["questions"] if str(q.get("chunk_index", "")).lstrip("-").isdigit()}
        except Exception as e:
            LOGGER.error(f"Question batch {batch_num} failed permanently, using raw chunk text as fallback: {e}")
            by_index = {}

        for i, chunk in enumerate(batch, start=1):
            q = by_index.get(i)
            if q is None:
                question_text = chunk.get("document", "").strip()
                answer_text = ""
                q_type = "Short Answer"
                linked = []
            else:
                question_text = str(q.get("question", "")).strip() or chunk.get("document", "").strip()
                answer_text = str(q.get("answer", "")).strip()
                q_type = str(q.get("type", "")).strip() or "Short Answer"
                linked = [cid for cid in q.get("linked_concepts", []) if isinstance(cid, str) and cid in valid_ids]

            if not linked:
                fallback_id = keyword_fallback_concept(question_text, ref_concepts) or keyword_fallback_concept(question_text, concept_tree)
                if fallback_id:
                    linked = [fallback_id]
                    LOGGER.info(f"Question from chunk {chunk.get('original_id')} had no linked concept; keyword-matched to {fallback_id}")

            all_questions.append({
                "question": question_text,
                "answer": answer_text,
                "type": q_type,
                "linked_concepts": linked,
                "_source_chunk_id": chunk.get("original_id", ""),
            })

        save_json(all_questions, QUESTIONS_CHECKPOINT)

    LOGGER.info(f"Stage 4 complete: {len(all_questions)} question(s) extracted")
    return all_questions


# ==========================================================
# STAGE 5 -- RELATIONSHIPS
# ==========================================================

RELATIONSHIP_SYSTEM_PROMPT = """You are a Chemistry Knowledge Graph Architect. Given a list of concepts
(with definitions) from one NCERT chapter, propose semantic relationships
between them.

RULES

1. Use ONLY the concept_id values given. Never invent a concept.
2. Use ONLY these relationship types: "depends_on", "related_to",
   "application_of", "example_of".
   (Hierarchical "part_of"/"contains" relationships are handled
   separately -- do not produce those here.)
3. Only propose a relationship if it is clearly implied by the given
   definitions -- do not force connections.
4. Avoid duplicates and avoid a concept relating to itself.
5. Propose at most 15 relationships.
6. Return ONLY valid JSON. No markdown, no explanation, no code fences.

Output schema:

{
    "relationships": [
        {"source_concept": "", "target_concept": "", "relationship": ""}
    ]
}
"""

RELATIONSHIP_USER_TEMPLATE = """Chapter: {chapter}

Concepts:
{concept_list}
"""


def make_relationship_validator(valid_ids: Set[str]):
    def validator(parsed: Any) -> None:
        if not isinstance(parsed, dict) or not isinstance(parsed.get("relationships"), list):
            raise ValueError("Missing/invalid 'relationships'")
        for i, r in enumerate(parsed["relationships"]):
            if not isinstance(r, dict):
                raise ValueError(f"relationships[{i}] is not an object")
            if r.get("source_concept") not in valid_ids or r.get("target_concept") not in valid_ids:
                raise ValueError(f"relationships[{i}] references unknown concept_id")
            if r.get("relationship") not in RELATIONSHIP_TYPES - {"contains", "part_of"}:
                raise ValueError(f"relationships[{i}] invalid relationship type")
    return validator


def deterministic_hierarchy_relationships(concept_tree: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    name_to_id = {c["concept_name"]: c["concept_id"] for c in concept_tree}
    rels = []
    for c in concept_tree:
        if c["parent_concept"] and c["parent_concept"] in name_to_id:
            rels.append({
                "source_concept": c["concept_id"],
                "target_concept": name_to_id[c["parent_concept"]],
                "relationship": "part_of",
            })
    return rels


def run_relationships(chapter: str, concept_tree: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    if RELATIONSHIPS_CHECKPOINT.exists():
        LOGGER.info("Stage 5: resuming from checkpoint")
        return load_json(RELATIONSHIPS_CHECKPOINT)

    relationships = deterministic_hierarchy_relationships(concept_tree)
    LOGGER.info(f"Stage 5: {len(relationships)} deterministic part_of relationship(s)")

    valid_ids = {c["concept_id"] for c in concept_tree}
    real_concepts = [c for c in concept_tree if not c["is_grouping_node"]]

    by_topic: Dict[str, List[Dict[str, Any]]] = {}
    for c in real_concepts:
        by_topic.setdefault(c.get("_topic", ""), []).append(c)

    seen_triples: Set[Tuple[str, str, str]] = {(r["source_concept"], r["target_concept"], r["relationship"]) for r in relationships}

    for topic, topic_concepts in by_topic.items():
        batches = [topic_concepts[i:i + RELATIONSHIP_BATCH_SIZE] for i in range(0, len(topic_concepts), RELATIONSHIP_BATCH_SIZE)]
        for batch_num, batch in enumerate(batches, start=1):
            if len(batch) < 2:
                continue
            LOGGER.info(f"Relationship batch (topic={topic!r}) {batch_num}/{len(batches)} ({len(batch)} concept(s))")
            concept_list_text = "\n".join(f"- {c['concept_id']}: {c['concept_name']} -- {c.get('definition', '')}" for c in batch)
            user_prompt = RELATIONSHIP_USER_TEMPLATE.format(chapter=chapter, concept_list=concept_list_text)
            try:
                parsed = call_llm_json(
                    system_prompt=RELATIONSHIP_SYSTEM_PROMPT,
                    user_prompt=user_prompt,
                    validator=make_relationship_validator(valid_ids),
                    raw_dump_name=f"relationships_{normalize_name(topic)[:20]}_batch{batch_num}_raw.txt",
                )
                for r in parsed["relationships"]:
                    if r["source_concept"] == r["target_concept"]:
                        continue
                    triple = (r["source_concept"], r["target_concept"], r["relationship"])
                    if triple not in seen_triples:
                        relationships.append(r)
                        seen_triples.add(triple)
            except Exception as e:
                LOGGER.error(f"Relationship batch failed permanently for topic {topic!r}, skipping: {e}")

    save_json(relationships, RELATIONSHIPS_CHECKPOINT)
    LOGGER.info(f"Stage 5 complete: {len(relationships)} relationship(s) total")
    return relationships


# ==========================================================
# STAGE 6 -- QUALITY GATE
# ==========================================================

def quality_gate(concept_tree: List[Dict[str, Any]], relationships: List[Dict[str, Any]], question_bank: List[Dict[str, Any]]) -> None:
    ids = [c["concept_id"] for c in concept_tree]
    assert len(ids) == len(set(ids)), "Duplicate concept_id detected"

    names_seen: Dict[str, str] = {}
    for c in concept_tree:
        key = normalize_name(c["concept_name"])
        if key in names_seen:
            LOGGER.warning(f"Duplicate concept name survived: {c['concept_name']!r} ({c['concept_id']} / {names_seen[key]})")
        names_seen[key] = c["concept_id"]

    valid_names = {c["concept_name"] for c in concept_tree}
    for c in concept_tree:
        if c["parent_concept"] and c["parent_concept"] not in valid_names:
            LOGGER.warning(f"Orphan parent reference on {c['concept_id']}: {c['parent_concept']!r} -- clearing")
            c["parent_concept"] = ""

    children_count: Dict[str, int] = {}
    for c in concept_tree:
        if c["parent_concept"]:
            children_count[c["parent_concept"]] = children_count.get(c["parent_concept"], 0) + 1
    for c in concept_tree:
        if c["is_grouping_node"] and children_count.get(c["concept_name"], 0) == 0:
            LOGGER.warning(f"Grouping node with no children, downgrading: {c['concept_name']!r}")
            c["is_grouping_node"] = False

    for c in concept_tree:
        if not c["retrieval"]["keywords"]:
            c["retrieval"]["keywords"] = build_keywords(c, [])
            LOGGER.warning(f"Concept had no retrieval keywords, backfilled: {c['concept_id']}")

    valid_ids = set(ids)
    non_grouping = [c for c in concept_tree if not c["is_grouping_node"]]
    fallback_ref_id = max(non_grouping, key=lambda c: len(c.get("_source_chunk_ids", [])))["concept_id"] if non_grouping else (ids[0] if ids else None)

    for q in question_bank:
        q["linked_concepts"] = [cid for cid in q["linked_concepts"] if cid in valid_ids]
        if not q["linked_concepts"]:
            keyword_match = keyword_fallback_concept(q["question"], non_grouping)
            if keyword_match:
                q["linked_concepts"] = [keyword_match]
                LOGGER.warning(f"Question '{q['question'][:60]}...' had no linked concept; last-resort keyword-matched to {keyword_match}")
            elif fallback_ref_id:
                q["linked_concepts"] = [fallback_ref_id]
                LOGGER.warning(f"Question '{q['question'][:60]}...' had no keyword match either; attached to most-referenced concept {fallback_ref_id}")

    bad = [r for r in relationships if r["source_concept"] not in valid_ids or r["target_concept"] not in valid_ids]
    if bad:
        LOGGER.warning(f"{len(bad)} relationship(s) reference unknown concept_id(s), removing")
    relationships[:] = [r for r in relationships if r["source_concept"] in valid_ids and r["target_concept"] in valid_ids]

    LOGGER.info("Stage 6 (quality gate) complete")


# ==========================================================
# ASSEMBLE FINAL OUTPUT
# ==========================================================

def assemble_final_concept(c: Dict[str, Any], chunks_by_id: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    source_chunk_ids = c.get("_source_chunk_ids", [])
    return {
        "concept_id": c["concept_id"],
        "concept_name": c["concept_name"],
        "parent_concept": c["parent_concept"],
        "is_grouping_node": c["is_grouping_node"],
        "official_name": c["official_name"],
        "aliases": c["aliases"],
        "search_terms": c["search_terms"],
        "abbreviations": c["abbreviations"],
        "definition": c["definition"],
        "formulae": c["formulae"],
        "examples": c["examples"],
        "related_concepts": c["related_concepts"],
        "importance": c["importance"],
        "chapter_weightage": c["chapter_weightage"],
        "concept_category": c["concept_category"],
        "concept_type": c["concept_type"],
        "prerequisites": c["prerequisites"],
        "difficulty_hint": c["difficulty_hint"],
        "learning_outcomes": c["learning_outcomes"],
        "assessment": c["assessment"],
        "retrieval": c["retrieval"],
        "source_chunk_ids": source_chunk_ids,
        "source_chunks": [chunks_by_id[cid] for cid in source_chunk_ids if cid in chunks_by_id],
    }


def compute_related_concepts(concept_tree: List[Dict[str, Any]], relationships: List[Dict[str, Any]]) -> None:
    related: Dict[str, List[str]] = {c["concept_id"]: [] for c in concept_tree}
    for r in relationships:
        if r["relationship"] == "part_of":
            continue  # already reflected via parent_concept
        src, tgt = r["source_concept"], r["target_concept"]
        if tgt not in related[src]:
            related[src].append(tgt)
        if src not in related[tgt]:
            related[tgt].append(src)
    for c in concept_tree:
        c["related_concepts"] = related.get(c["concept_id"], [])


def main() -> None:
    LOGGER.info("=" * 80)
    LOGGER.info("APPROACH 2 -- CHUNK-TO-CANONICAL-KB PIPELINE")
    LOGGER.info("=" * 80)

    chunks = load_chunks()
    chapter = chunks[0].get("chapter", "") if chunks else ""

    canonical = run_discovery(chapter, chunks)

    if HIERARCHY_CHECKPOINT.exists():
        LOGGER.info("Stage 2: resuming from checkpoint")
        concept_tree = load_json(HIERARCHY_CHECKPOINT)
    else:
        concept_tree = resolve_hierarchy(canonical)
        save_json(concept_tree, HIERARCHY_CHECKPOINT)

    concept_tree = run_enrichment(chapter, concept_tree)
    question_bank_raw = run_question_extraction(chapter, chunks, concept_tree)
    relationships = run_relationships(chapter, concept_tree)

    compute_related_concepts(concept_tree, relationships)

    chunks_by_id = {c.get("original_id"): c for c in chunks if c.get("original_id")}

    question_bank = []
    for i, q in enumerate(question_bank_raw, start=1):
        source_chunk_id = q.get("_source_chunk_id", "")
        question_bank.append({
            "question_id": f"Q{i:03d}",
            "question": q["question"],
            "answer": q["answer"],
            "type": q["type"],
            "linked_concepts": q["linked_concepts"],
            "source_chunk_id": source_chunk_id,
            "source_chunk": chunks_by_id.get(source_chunk_id),
        })

    quality_gate(concept_tree, relationships, question_bank)

    final_concept_tree = [assemble_final_concept(c, chunks_by_id) for c in concept_tree]
    final_relationships = [{"source_concept": r["source_concept"], "target_concept": r["target_concept"], "relationship": r["relationship"]} for r in relationships]

    result = {
        "chapter": chapter,
        "chapter_id": CHAPTER_ID,
        "subject": SUBJECT,
        "grade": GRADE,
        "concept_tree": final_concept_tree,
        "relationships": final_relationships,
        "question_bank": question_bank,
    }

    save_json(result, FINAL_OUTPUT_FILE)
    LOGGER.info(f"Saved: {FINAL_OUTPUT_FILE}")

    LOGGER.info("Summary")
    LOGGER.info(f"  Concepts       : {len(final_concept_tree)}")
    LOGGER.info(f"  Grouping nodes : {sum(1 for c in final_concept_tree if c['is_grouping_node'])}")
    LOGGER.info(f"  Relationships  : {len(final_relationships)}")
    LOGGER.info(f"  Questions      : {len(question_bank)}")


if __name__ == "__main__":
    main()
