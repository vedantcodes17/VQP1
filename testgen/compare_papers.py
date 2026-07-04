"""
compare_papers.py

Quick comparison of the two question papers produced by the SAME testgen
pipeline against two different knowledge bases:
    - Teacher-Note paper : output/question_paper.json          (29-concept KB)
    - Approach2 paper    : Approach2_op/question_paper.json     (4-concept KB)

Deterministic metrics (question/marks counts, duplicate questions,
distinct concepts tested, validator flags, execution time) are computed
in code. The LLM is only asked for a Confidence/Accuracy verdict per
metric plus an overall verdict on which paper is the better exam paper --
same lean pattern as ../compare.py (build the table locally, don't make
the model reproduce it).

Run: python compare_papers.py
Output: printed table + papers_comparison.md
"""

import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))

import utils

TEACHER_PAPER_FILE = utils.OUTPUT_DIR / "question_paper.json"
TEACHER_VALIDATION_FILE = utils.OUTPUT_DIR / "validation_report.json"
TEACHER_KB_FILE = utils.CHAPTER_KB_FILE

APPROACH2_DIR = utils.BASE_DIR / "Approach2_op"
APPROACH2_PAPER_FILE = APPROACH2_DIR / "question_paper.json"
APPROACH2_VALIDATION_FILE = APPROACH2_DIR / "validation_report.json"
APPROACH2_KB_FILE = utils.INPUT_DIR / "chapter_kb_approach2.json"

LOG_FILE = utils.OUTPUT_DIR / "testgen.log"
REPORT_FILE = utils.BASE_DIR / "papers_comparison.md"


def all_questions(paper: Dict[str, Any]) -> List[Dict[str, Any]]:
    return [q for sec in paper["sections"] for q in sec["questions"]]


def compute_metrics(paper: Dict[str, Any], validation_report: Optional[Dict[str, Any]], kb: Dict[str, Any]) -> Dict[str, Any]:
    qs = all_questions(paper)
    texts = [utils.normalize_text(q["question"]) for q in qs]
    dup_count = len(texts) - len(set(texts))
    concept_ids = [q.get("concept_id", "") for q in qs]
    distinct_concepts = len(set(cid for cid in concept_ids if cid))
    kb_pool_size = sum(1 for c in kb["concept_tree"] if not c.get("is_grouping_node"))
    return {
        "total_questions": len(qs),
        "total_marks": sum(q["marks"] for q in qs),
        "distinct_concepts_tested": distinct_concepts,
        "kb_concept_pool_size": kb_pool_size,
        "duplicate_question_count": dup_count,
        "flagged_count": validation_report.get("flagged_count") if validation_report else "N/A",
    }


def parse_duration(log_text: str, pattern: str) -> Optional[float]:
    m = re.search(pattern, log_text)
    return float(m.group(1)) if m else None


def build_rows(tn: Dict[str, Any], na: Dict[str, Any], tn_time: Optional[float], na_time: Optional[float]) -> List[Dict[str, str]]:
    def row(label: str, tn_val: Any, na_val: Any) -> Dict[str, str]:
        return {"metric": label, "teacher_note": str(tn_val), "new_approach": str(na_val)}

    return [
        row("Total questions", tn["total_questions"], na["total_questions"]),
        row("Total marks", tn["total_marks"], na["total_marks"]),
        row("Source KB concept pool size", tn["kb_concept_pool_size"], na["kb_concept_pool_size"]),
        row("Distinct concepts tested in paper", tn["distinct_concepts_tested"], na["distinct_concepts_tested"]),
        row("Duplicate/near-duplicate questions", tn["duplicate_question_count"], na["duplicate_question_count"]),
        row("Questions flagged by validator", tn["flagged_count"], na["flagged_count"]),
        row("Pipeline execution time", f"{tn_time:.1f}s" if tn_time else "N/A", f"{na_time:.1f}s" if na_time else "N/A"),
    ]


def extract_json(text: str) -> Any:
    cleaned = re.sub(r"^```(?:json)?", "", text.strip(), flags=re.IGNORECASE)
    cleaned = re.sub(r"```$", "", cleaned.strip())
    start, end = cleaned.find("{"), cleaned.rfind("}")
    return utils.json.loads(cleaned[start:end + 1])


def format_paper_qas(paper: Dict[str, Any]) -> str:
    lines = []
    for q in all_questions(paper):
        lines.append(f"- [{q['marks']}m, {q['difficulty']}, concept={q.get('concept_id', '')}] "
                     f"Q: {q['question']}")
    return "\n".join(lines)


def call_llm_evaluation(rows: List[Dict[str, str]], teacher_paper: Dict[str, Any],
                         approach2_paper: Dict[str, Any]) -> Tuple[Dict[str, str], str]:
    metric_list_text = "\n".join(f"{i+1}. {r['metric']} -- teacher-note: {r['teacher_note']} | approach2: {r['new_approach']}"
                                 for i, r in enumerate(rows))

    system_prompt = (
        "You are a Senior CBSE Paper Setter comparing two auto-generated Class 12 "
        "Chemistry question papers on the same chapter, produced by the same generation "
        "pipeline but from two different knowledge bases (one richer than the other). "
        "You are given a numbered list of deterministic metrics (already computed and "
        "final -- do not recompute) plus the full question lists from both papers.\n"
        "For EVERY numbered metric, output one confidence_accuracy verdict: "
        "'High/Medium/Low - <reason under 10 words>' judging which paper is actually "
        "better on that metric (not just which number is bigger -- inspect the real "
        "questions for repetition/quality).\n"
        "Also give one overall_verdict: 3-4 sentences on which paper is the better, more "
        "usable exam paper overall and why.\n"
        "Return ONLY valid JSON, no markdown, no code fences, matching exactly:\n"
        '{"evaluations": [{"n": 1, "confidence_accuracy": "..."}, ...], "overall_verdict": "..."}\n'
        "Include one evaluations entry per numbered metric, in order, n=1.." + str(len(rows)) + "."
    )

    user_prompt = f"""Numbered metrics:
{metric_list_text}

Teacher-Note paper -- full question list:
{format_paper_qas(teacher_paper)}

Approach2 paper -- full question list:
{format_paper_qas(approach2_paper)}

Return the JSON now."""

    payload = {
        "model": utils.MODEL,
        "temperature": 0.1,
        "max_tokens": 4096,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    }
    import requests
    response = requests.post(utils.LMSTUDIO_URL, json=payload, timeout=utils.REQUEST_TIMEOUT)
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

    confidence_by_metric = {r["metric"]: confidence_by_n.get(i + 1, "N/A - no LLM verdict") for i, r in enumerate(rows)}
    return confidence_by_metric, overall_verdict


def main() -> None:
    teacher_paper = utils.load_json(TEACHER_PAPER_FILE)
    teacher_validation = utils.load_json(TEACHER_VALIDATION_FILE) if TEACHER_VALIDATION_FILE.exists() else None
    teacher_kb = utils.load_json(TEACHER_KB_FILE)

    approach2_paper = utils.load_json(APPROACH2_PAPER_FILE)
    approach2_validation = utils.load_json(APPROACH2_VALIDATION_FILE) if APPROACH2_VALIDATION_FILE.exists() else None
    approach2_kb = utils.load_json(APPROACH2_KB_FILE)

    tn_metrics = compute_metrics(teacher_paper, teacher_validation, teacher_kb)
    na_metrics = compute_metrics(approach2_paper, approach2_validation, approach2_kb)

    log_text = LOG_FILE.read_text(encoding="utf-8", errors="ignore") if LOG_FILE.exists() else ""
    tn_time = parse_duration(log_text, r"testgen\.main \| Pipeline complete in ([\d.]+)s")
    na_time = parse_duration(log_text, r"testgen\.run_approach2 \| Approach2 pipeline complete in ([\d.]+)s")

    rows = build_rows(tn_metrics, na_metrics, tn_time, na_time)

    print("Calling local LLM for Confidence/Accuracy evaluation...")
    confidence_by_metric, overall_verdict = call_llm_evaluation(rows, teacher_paper, approach2_paper)

    table_lines = ["| Metric | Teacher-Note Paper | Approach2 Paper | Confidence/Accuracy |",
                   "|---|---|---|---|"]
    for r in rows:
        conf = confidence_by_metric.get(r["metric"], "N/A")
        table_lines.append(f"| {r['metric']} | {r['teacher_note']} | {r['new_approach']} | {conf} |")
    table_md = "\n".join(table_lines)

    caveat = ("\n*Caveat: the Approach2 KB currently has only "
              f"{na_metrics['kb_concept_pool_size']} concepts vs "
              f"{tn_metrics['kb_concept_pool_size']} for the Teacher-Note KB "
              "(approach2.py was smoke-tested on 5 chunks only) -- concept-reuse "
              "related metrics reflect that data-scale gap, not a pipeline difference.*")

    out = [
        "# Question Paper Comparison (Teacher-Note vs Approach2)\n",
        table_md,
        caveat,
        "\n## Overall verdict (LLM)\n",
        overall_verdict,
    ]
    REPORT_FILE.write_text("\n\n".join(out), encoding="utf-8")

    print(table_md)
    print(caveat)
    print()
    print(overall_verdict)
    print(f"\nSaved: {REPORT_FILE}")


if __name__ == "__main__":
    main()
