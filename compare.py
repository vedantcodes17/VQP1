"""
compare.py

Quick comparison of the two chapter-KB pipelines:
    - Teacher-note approach : refinement/output/chapter_kb_enriched.json
    - New approach          : approach2_output/chapter_kb.json

For every schema field (concept_tree / question_bank / relationships,
handling the differing field names between the two pipelines) it computes
a deterministic "% populated" coverage number for each approach, then
sends that table + a few sample records to the local LLM and asks it ONLY
to judge Confidence/Accuracy (column 4) and give a final verdict on which
KB is more usable. Also reports wall-clock execution time pulled from each
pipeline's log file.

Run: python compare.py
Output: printed table + compare_output.md
"""

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests

BASE_DIR = Path(__file__).resolve().parent

TEACHER_NOTE_FILE = BASE_DIR / "refinement" / "output" / "chapter_kb_enriched.json"
TEACHER_NOTE_LOG = BASE_DIR / "refinement" / "output" / "pipeline.log"

NEW_APPROACH_FILE = BASE_DIR / "approach2_output" / "chapter_kb.json"
NEW_APPROACH_LOG = BASE_DIR / "approach2_output" / "approach2.log"

OUTPUT_FILE = BASE_DIR / "compare_output.md"

LMSTUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"
MODEL = "qwen2.5-vl-7b-instruct"

# canonical_field -> (path in teacher-note record, path in new-approach record)
# path = dotted string; None = field doesn't exist in that schema
CONCEPT_FIELDS = [
    ("concept_id", "concept_id", "concept_id"),
    ("concept_name", "concept_name", "concept_name"),
    ("parent_concept", "parent_concept", "parent_concept"),
    ("definition", "definition", "definition"),
    ("aliases", "aliases", "aliases"),
    ("formulae", "formulae", "formulae"),
    ("examples", "examples", "examples"),
    ("related_concepts", "related_concepts", "related_concepts"),
    ("prerequisites", "prerequisites", "prerequisites"),
    ("learning_outcomes", "learning_outcomes", "learning_outcomes"),
    ("assessment", "assessment", "assessment"),
    ("retrieval.keywords", "retrieval.keywords", "retrieval.keywords"),
    ("retrieval.chunk_ids", "retrieval.chunk_ids", "retrieval.chunk_ids"),
    ("source_chunks (traceability)", None, "source_chunks"),
]

QUESTION_FIELDS = [
    ("question_id", "question_id", "question_id"),
    ("question", "question", "question"),
    ("answer", "answer", "answer"),
    ("type", "question_type", "type"),
    ("linked_concepts", "linked_concepts", "linked_concepts"),
    ("source_chunk (traceability)", "source_question_ids", "source_chunk"),
]

RELATIONSHIP_FIELDS = [
    ("source_concept", "source_concept_id", "source_concept"),
    ("target_concept", "target_concept_id", "target_concept"),
    ("relationship", "relationship_type", "relationship"),
]

TOP_LEVEL_FIELDS = [
    ("chapter", "chapter", "chapter"),
    ("chapter_id", None, "chapter_id"),
    ("subject", None, "subject"),
    ("grade", None, "grade"),
]


def load_json(path: Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_path(record: Any, path: Optional[str]) -> Any:
    if path is None or record is None:
        return None
    cur = record
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur


def is_populated(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return value.strip() != ""
    if isinstance(value, (list, dict)):
        return len(value) > 0
    return True


def coverage_pct(records: List[Any], path: Optional[str]) -> Tuple[float, int]:
    if path is None or not records:
        return 0.0, 0
    populated = sum(1 for r in records if is_populated(get_path(r, path)))
    return round(100 * populated / len(records), 1), len(records)


def build_section_rows(label: str, fields: List[Tuple[str, Optional[str], Optional[str]]],
                        teacher_records: List[Any], new_records: List[Any]) -> List[Dict[str, str]]:
    rows = []
    for canonical, tn_path, na_path in fields:
        tn_pct, tn_n = coverage_pct(teacher_records, tn_path)
        na_pct, na_n = coverage_pct(new_records, na_path)
        tn_display = "N/A (field absent)" if tn_path is None else f"{tn_pct}% populated ({tn_n} records)"
        na_display = "N/A (field absent)" if na_path is None else f"{na_pct}% populated ({na_n} records)"
        rows.append({
            "section": label,
            "field": canonical,
            "teacher_note": tn_display,
            "new_approach": na_display,
        })
    return rows


def parse_log_span(path: Path, ts_regex: str) -> Optional[Tuple[str, str]]:
    if not path.exists():
        return None
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    timestamps = []
    for line in lines:
        m = re.match(ts_regex, line)
        if m:
            timestamps.append(m.group(1))
    if not timestamps:
        return None
    return timestamps[0], timestamps[-1]


def duration_seconds(start: str, end: str) -> Optional[float]:
    from datetime import datetime
    fmt = "%Y-%m-%d %H:%M:%S"
    try:
        return (datetime.strptime(end, fmt) - datetime.strptime(start, fmt)).total_seconds()
    except ValueError:
        return None


def trim(rec: Any, max_doc_chars: int = 200) -> Any:
    """Shrink long nested text (esp. source_chunks[].document) to keep the prompt small."""
    if isinstance(rec, dict):
        return {k: (v[:max_doc_chars] + " ...[truncated]" if k == "document" and isinstance(v, str) and len(v) > max_doc_chars
                     else trim(v, max_doc_chars)) for k, v in rec.items()}
    if isinstance(rec, list):
        return [trim(x, max_doc_chars) for x in rec]
    return rec


def extract_json(text: str) -> Any:
    cleaned = re.sub(r"^```(?:json)?", "", text.strip(), flags=re.IGNORECASE)
    cleaned = re.sub(r"```$", "", cleaned.strip())
    start, end = cleaned.find("{"), cleaned.rfind("}")
    return json.loads(cleaned[start:end + 1])


def call_llm_evaluation(rows: List[Dict[str, str]], teacher_kb: Dict[str, Any], new_kb: Dict[str, Any]) -> Tuple[Dict[str, str], str]:
    """Ask the LLM ONLY for the Confidence/Accuracy column (short verdict per field)
    plus one overall verdict -- the table itself (columns 1-3) is already built
    deterministically by this script, so the LLM never has to reproduce it."""
    field_list_text = "\n".join(f"{i+1}. [{r['section']}] {r['field']} -- teacher-note: {r['teacher_note']} | new-approach: {r['new_approach']}"
                                 for i, r in enumerate(rows))

    sample_teacher_concept = json.dumps(trim(teacher_kb["concept_tree"][0]), ensure_ascii=False)
    sample_new_concept = json.dumps(trim(new_kb["concept_tree"][0]), ensure_ascii=False)
    sample_teacher_question = json.dumps(trim(teacher_kb["question_bank"][0]), ensure_ascii=False) if teacher_kb.get("question_bank") else "(none)"
    sample_new_question = json.dumps(trim(new_kb["question_bank"][0]), ensure_ascii=False) if new_kb.get("question_bank") else "(none)"

    system_prompt = (
        "You are a Senior Educational Knowledge-Graph QA Reviewer comparing two chapter "
        "knowledge-base pipelines. You are given a numbered list of schema fields with "
        "their deterministic coverage % for each pipeline (already computed and final -- "
        "do not recompute), plus one sample concept and one sample question record from "
        "each pipeline's real output for quality context.\n"
        "For EVERY numbered field, output one confidence_accuracy verdict: "
        "'High/Medium/Low - <reason under 8 words>', judging actual usefulness/accuracy "
        "(not just the raw %). Be extremely terse.\n"
        "Also give one overall_verdict: 2-3 sentences on which pipeline is more usable "
        "overall.\n"
        "Return ONLY valid JSON, no markdown, no code fences, matching exactly:\n"
        '{"evaluations": [{"n": 1, "confidence_accuracy": "..."}, ...], "overall_verdict": "..."}\n'
        "You MUST include one evaluations entry per numbered field, in order, n=1.." + str(len(rows)) + "."
    )

    user_prompt = f"""Numbered schema fields with coverage:
{field_list_text}

Sample concept -- Teacher-Note Approach:
{sample_teacher_concept}

Sample concept -- New Approach:
{sample_new_concept}

Sample question -- Teacher-Note Approach:
{sample_teacher_question}

Sample question -- New Approach:
{sample_new_question}

Return the JSON now."""

    payload = {
        "model": MODEL,
        "temperature": 0.1,
        "max_tokens": 4096,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    }
    response = requests.post(LMSTUDIO_URL, json=payload, timeout=600)
    response.raise_for_status()
    choice = response.json()["choices"][0]
    if choice.get("finish_reason") == "length":
        print("WARNING: LLM response was truncated (hit max_tokens) -- some verdicts may be missing.")

    confidence_by_n: Dict[int, str] = {}
    overall_verdict = "(LLM evaluation unavailable -- JSON parse failed)"
    try:
        parsed = extract_json(choice["message"]["content"])
        for item in parsed.get("evaluations", []):
            if isinstance(item, dict) and "n" in item:
                confidence_by_n[int(item["n"])] = str(item.get("confidence_accuracy", "")).strip()
        overall_verdict = str(parsed.get("overall_verdict", overall_verdict)).strip()
    except Exception as e:
        print(f"WARNING: could not parse LLM JSON response ({e}); confidence column will show 'N/A'.")

    confidence_by_field = {}
    for i, r in enumerate(rows):
        confidence_by_field[(r["section"], r["field"])] = confidence_by_n.get(i + 1, "N/A - no LLM verdict")
    return confidence_by_field, overall_verdict


def main() -> None:
    teacher_kb = load_json(TEACHER_NOTE_FILE)
    new_kb = load_json(NEW_APPROACH_FILE)

    rows: List[Dict[str, str]] = []
    rows += build_section_rows("top_level", TOP_LEVEL_FIELDS, [teacher_kb], [new_kb])
    rows += build_section_rows("concept_tree", CONCEPT_FIELDS, teacher_kb["concept_tree"], new_kb["concept_tree"])
    rows += build_section_rows("question_bank", QUESTION_FIELDS, teacher_kb.get("question_bank", []), new_kb.get("question_bank", []))
    rows += build_section_rows("relationships", RELATIONSHIP_FIELDS, teacher_kb.get("relationships", []), new_kb.get("relationships", []))

    ts_regex = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})"
    tn_span = parse_log_span(TEACHER_NOTE_LOG, ts_regex)
    na_span = parse_log_span(NEW_APPROACH_LOG, ts_regex)

    lines = ["## Execution time"]
    if tn_span:
        dur = duration_seconds(*tn_span)
        lines.append(f"- Teacher-Note Approach: {tn_span[0]} -> {tn_span[1]}  (~{dur:.0f}s, "
                      f"{len(teacher_kb['concept_tree'])} concepts, full chapter run)")
    if na_span:
        dur = duration_seconds(*na_span)
        lines.append(f"- New Approach: {na_span[0]} -> {na_span[1]}  (~{dur:.0f}s, "
                      f"{len(new_kb['concept_tree'])} concepts, LIMIT_CHUNKS=5 smoke test)")
    lines.append("- NOTE: these two runs are not apples-to-apples -- the teacher-note run "
                 "processed the full chapter (~530 chunks) while the new-approach run was "
                 "capped at 5 chunks for testing. Compare per-concept/per-chunk rate, not raw totals.")
    timing_note = "\n".join(lines)

    print("Calling local LLM for Confidence/Accuracy evaluation...")
    confidence_by_field, overall_verdict = call_llm_evaluation(rows, teacher_kb, new_kb)

    table_lines = ["| Section | Schema Field | Teacher-Note Approach | New Approach | Confidence/Accuracy |",
                   "|---|---|---|---|---|"]
    for r in rows:
        conf = confidence_by_field.get((r["section"], r["field"]), "N/A")
        table_lines.append(f"| {r['section']} | {r['field']} | {r['teacher_note']} | {r['new_approach']} | {conf} |")
    table_md = "\n".join(table_lines)

    out = [
        "# Chapter-KB Pipeline Comparison\n",
        timing_note,
        "\n## Field-by-field comparison\n",
        table_md,
        "\n## Overall verdict (LLM)\n",
        overall_verdict,
    ]
    OUTPUT_FILE.write_text("\n\n".join(out), encoding="utf-8")

    print(timing_note)
    print()
    print(table_md)
    print()
    print(overall_verdict)
    print(f"\nSaved: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
