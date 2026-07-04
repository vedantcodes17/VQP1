"""
final_refinement.py

Final enrichment pass of the Concept Intelligence Engine.

Input:
    output/chapter_kb_final.json   (Pass 6 output -- read-only source of truth)

The concepts (their ids, names and hierarchy) are FINAL -- this pass never
adds/renames/removes/merges a concept and never touches relationships or
question text. Within each concept node it:

    - DROPS the free-text "learning_objective" field (superseded by the
      structured "learning_outcomes" this pass adds)
    - ADDS "definition", "formulae", "examples", "related_concepts"
      (Knowledge fields)
    - REPLACES "concept_category" with a value from a fixed, subject-
      agnostic enum (Core Concept, Law, Principle, Process, Definition,
      Formula, Application, Measurement, Phenomenon)
    - CORRECTS "is_grouping_node" -- upgrades false->true only for nodes
      that are purely organisational topic headers with >=2 children and
      no independent definition of their own (e.g. "Colligative
      Properties"); never downgrades an existing true
    - ADDS "learning_outcomes" (structured {verb, object} pairs)
    - ADDS "assessment" (preferred_question_types, recommended_marks,
      blooms_levels, competencies, board_frequency)
    - ADDS "retrieval" (keywords, chunk_ids, formula_ids, example_ids,
      pyq_ids -- the id arrays are always left empty, no ids are invented)

Role played by the LLM: Senior NCERT Curriculum Designer / CBSE Paper
Setter / Educational Knowledge Graph Architect / Assessment Expert.

Output:
    output/chapter_kb_enriched.json
"""

from __future__ import annotations

from typing import Any, Dict, List, Set

import utils

LOGGER = utils.setup_logger("final_refinement")

BATCH_SIZE = 4
MAX_RECONCILE_ROUNDS = 2

BLOOMS_CANONICAL = {
    "remember": "Remember",
    "understand": "Understand",
    "apply": "Apply",
    "analyze": "Analyze",
    "analyse": "Analyze",
    "evaluate": "Evaluate",
    "create": "Create",
}
ALLOWED_MARKS = {1, 2, 3, 4, 5}
BOARD_FREQ_LEVELS = {"high", "medium", "low"}

CONCEPT_CATEGORIES = {
    "core concept": "Core Concept",
    "law": "Law",
    "principle": "Principle",
    "process": "Process",
    "definition": "Definition",
    "formula": "Formula",
    "application": "Application",
    "measurement": "Measurement",
    "phenomenon": "Phenomenon",
}

# Fallback mapping from the OLD concept_category values (Pass 4) to the new
# enum, used only if the LLM fails outright for a concept.
OLD_CATEGORY_FALLBACK = {
    "law/formula": "Law",
    "definition": "Definition",
    "core concept": "Core Concept",
}

MIN_CHILDREN_FOR_GROUPING = 2

SYSTEM_PROMPT = """You are a Senior NCERT Curriculum Designer, CBSE Paper Setter, Educational
Knowledge Graph Architect, and Assessment Expert.

You are given an already finalised list of concepts from one NCERT chapter.
The concepts themselves are FINAL -- you are not designing curriculum, you
are annotating each concept with knowledge, assessment and retrieval
metadata for a question-paper generation system.

STRICT RULES

1. Use ONLY the concept_id values given to you. Never add, rename, merge,
   split, or invent concepts.
2. You MUST return exactly one enrichment entry per concept_id given to you.
3. definition: a precise, NCERT-accurate 1-2 sentence definition of the
   concept, in the context of this chapter.
4. formulae: any standard mathematical formula(s)/equations directly
   associated with this concept, as plain strings (e.g. "M = n_solute / V_solution (L)").
   Return an empty list if no formula applies to this concept.
5. examples: 2-4 short, concrete real-world or textbook examples/instances
   of this concept. Return an empty list only if truly not applicable.
6. concept_category: choose EXACTLY ONE from this fixed list only:
   "Core Concept", "Law", "Principle", "Process", "Definition", "Formula",
   "Application", "Measurement", "Phenomenon".
   Do NOT default everything to "Core Concept" -- pick the most specific
   fitting category. Guidance with examples (do not limit yourself to
   these, they illustrate the intended granularity):
     - "Measurement": a way of quantifying/expressing an amount, e.g.
       Molarity, Molality, Mole Fraction, Mass Percentage, ppm.
     - "Law": a named, formally stated scientific law, e.g. Henry's Law,
       Raoult's Law.
     - "Process": a dynamic mechanism/action, e.g. Osmosis, Diffusion,
       Dissociation, Association.
     - "Phenomenon": an observed effect/behaviour, e.g. Osmotic Pressure,
       Colligative Properties, Azeotrope formation.
     - "Application": a practical/real-world use, e.g. Reverse Osmosis.
     - "Principle": a general explanatory idea broader than one law.
     - "Definition": a term whose entire content is its definition, with
       no deeper mechanism/formula of its own.
     - "Formula": the concept's identity IS a named formula/quantity
       itself (distinct from "Measurement", which is a *method* of
       expressing an amount).
     - "Core Concept": only for foundational ideas that genuinely do not
       fit any category above (e.g. Solution, Ideal Solution).
7. is_grouping_node: true ONLY if this concept is a purely organisational
   topic header whose own content is fully carried by its listed child
   concepts (it has no independent definition/formula/example of its own),
   e.g. "Colligative Properties" grouping "Elevation in Boiling Point",
   "Depression in Freezing Point", etc. If the concept has no children
   listed, this MUST be false. If the concept is itself independently
   definable/measurable (even if it happens to have children), this MUST
   be false.
8. learning_outcomes: 1-3 structured outcomes, each a {"verb","object"}
   pair. "verb" is a single measurable action verb (e.g. "Explain",
   "Define", "Apply", "Differentiate", "Calculate", "State"). "object" is
   the short phrase it acts on.
9. preferred_question_types: choose from typical CBSE question formats,
   e.g. "MCQ", "Very Short Answer", "Short Answer", "Long Answer",
   "Numerical", "Assertion-Reason", "Case-Based", "HOTS". Pick 1-3 that
   best fit this concept.
10. recommended_marks: integers from {1, 2, 3, 4, 5} -- typical CBSE mark
    weightage for a question on this concept. Pick 1-2 values.
11. blooms_levels: choose 1-2 from exactly: "Remember", "Understand",
    "Apply", "Analyze", "Evaluate", "Create".
12. competencies: short labels such as "Conceptual Understanding",
    "Problem Solving", "Application", "Analytical Thinking",
    "Critical Thinking". Pick 1-2.
13. keywords: 3-6 meaningful retrieval search terms/synonyms for this
    concept (do not just repeat the concept_id).
14. Do NOT invent facts not implied by the given information.
15. Do NOT estimate NCERT/exemplar/PYQ board-frequency -- that is computed
    separately, do not include it.
16. Return ONLY valid JSON. No markdown. No explanation. No code fences.

Output schema:

{
    "enrichment": [
        {
            "concept_id": "",
            "definition": "",
            "formulae": [],
            "examples": [],
            "concept_category": "",
            "is_grouping_node": false,
            "learning_outcomes": [
                {"verb": "", "object": ""}
            ],
            "preferred_question_types": [],
            "recommended_marks": [],
            "blooms_levels": [],
            "competencies": [],
            "keywords": []
        }
    ]
}
"""

USER_PROMPT_TEMPLATE = """Chapter: {chapter}

Concepts to enrich (you MUST cover every one of these, using the exact
concept_id values):

{concept_list}
"""


# ==========================================================
# DETERMINISTIC PRE-COMPUTATION (no LLM -- derived from data already present)
# ==========================================================

def compute_children_map(concept_tree: List[Dict[str, Any]]) -> Dict[str, List[str]]:
    children: Dict[str, List[str]] = {}
    for c in concept_tree:
        parent = c.get("parent_concept", "")
        if parent:
            children.setdefault(parent, []).append(c["concept_name"])
    return children


def compute_related_concepts(
    concept_tree: List[Dict[str, Any]],
    relationships: List[Dict[str, Any]],
) -> Dict[str, List[str]]:
    """Related concepts are derived purely from the relationships already
    produced by Pass 3 -- no ids are invented. A concept's own prerequisites
    (already a distinct field) are excluded here to avoid duplication."""
    related: Dict[str, List[str]] = {c["concept_id"]: [] for c in concept_tree}
    prereqs_by_id = {c["concept_id"]: set(c.get("prerequisites", [])) for c in concept_tree}

    for rel in relationships:
        src, tgt = rel.get("source_concept_id"), rel.get("target_concept_id")
        if src not in related or tgt not in related:
            continue

        if tgt not in prereqs_by_id.get(src, set()) and tgt not in related[src]:
            related[src].append(tgt)
        if src not in prereqs_by_id.get(tgt, set()) and src not in related[tgt]:
            related[tgt].append(src)

    return related


# ==========================================================
# CONTEXT FORMATTING
# ==========================================================

def format_concept_list(concepts: List[Dict[str, Any]], children_map: Dict[str, List[str]]) -> str:
    lines = []
    for c in concepts:
        lines.append(f"- {c['concept_id']}: {c['concept_name']}")
        if c.get("official_name") and c["official_name"] != c["concept_name"]:
            lines.append(f"  Official name: {c['official_name']}")
        if c.get("aliases"):
            lines.append(f"  Aliases: {', '.join(c['aliases'])}")
        if c.get("learning_objective"):
            lines.append(f"  Prior learning objective (for reference only): {c['learning_objective']}")

        children = children_map.get(c["concept_name"], [])
        if children:
            lines.append(f"  Children (sub-concepts nested under this one): {', '.join(children)}")
        else:
            lines.append("  Children: none")

        lines.append(
            f"  Old category: {c.get('concept_category', '')} | "
            f"Type: {c.get('concept_type', '')} | "
            f"Importance: {c.get('importance', '')} | "
            f"Difficulty: {c.get('difficulty_hint', '')}"
        )
    return "\n".join(lines)


def build_user_prompt(chapter: str, concepts: List[Dict[str, Any]], children_map: Dict[str, List[str]]) -> str:
    return USER_PROMPT_TEMPLATE.format(chapter=chapter, concept_list=format_concept_list(concepts, children_map))


# ==========================================================
# VALIDATION
# ==========================================================

def make_validator(valid_ids: Set[str]):
    def validator(parsed: Any) -> None:
        utils.validate_json(parsed, ["enrichment"])

        if not isinstance(parsed["enrichment"], list):
            raise ValueError("'enrichment' is not a list")

        for i, item in enumerate(parsed["enrichment"]):
            if not isinstance(item, dict):
                raise ValueError(f"enrichment[{i}] is not an object")

            if "concept_id" not in item or item["concept_id"] not in valid_ids:
                raise ValueError(f"enrichment[{i}] missing/unknown 'concept_id'")

            if "definition" not in item or not isinstance(item["definition"], str):
                raise ValueError(f"enrichment[{i}] missing/invalid 'definition'")

            if "concept_category" not in item or not isinstance(item["concept_category"], str):
                raise ValueError(f"enrichment[{i}] missing/invalid 'concept_category'")

            for field in ("formulae", "examples", "learning_outcomes",
                          "preferred_question_types", "recommended_marks",
                          "blooms_levels", "competencies", "keywords"):
                if field not in item or not isinstance(item[field], list):
                    raise ValueError(f"enrichment[{i}] missing/invalid '{field}'")

    return validator


# ==========================================================
# NORMALIZATION / FALLBACKS
# ==========================================================

MEASUREMENT_NAME_HINTS = (
    "percentage", "percent", "fraction", "molarity", "molality",
    "ppm", "parts per million", "concentration",
)


def looks_like_measurement(concept: Dict[str, Any]) -> bool:
    """Concentration-expression concepts (Molarity, Mole Fraction, ppm, ...)
    are a small, well-known, closed set the local model repeatedly
    mis-buckets as the generic 'Core Concept' fallback despite explicit
    prompt examples -- this catches that one specific, unambiguous pattern
    deterministically rather than trusting a weak 7B model's judgment call."""
    haystack = " ".join([concept.get("concept_name", ""), *concept.get("aliases", [])]).lower()
    return any(hint in haystack for hint in MEASUREMENT_NAME_HINTS)


def normalize_category(raw: str, concept: Dict[str, Any]) -> str:
    key = str(raw).strip().lower()
    category = CONCEPT_CATEGORIES.get(key) or fallback_category(concept)

    if category == "Core Concept" and looks_like_measurement(concept):
        return "Measurement"

    return category


def fallback_category(concept: Dict[str, Any]) -> str:
    old = str(concept.get("concept_category", "")).strip().lower()
    return OLD_CATEGORY_FALLBACK.get(old, "Core Concept")


def normalize_is_grouping_node(raw: Any, concept: Dict[str, Any], children_map: Dict[str, List[str]]) -> bool:
    if concept.get("is_grouping_node"):
        return True  # never downgrade a prior structural pass's decision

    children = children_map.get(concept["concept_name"], [])
    if len(children) < MIN_CHILDREN_FOR_GROUPING:
        return False

    return bool(raw is True)


def normalize_learning_outcomes(raw: List[Any], fallback_objective: str) -> List[Dict[str, str]]:
    outcomes = []
    for item in raw:
        if not isinstance(item, dict):
            continue
        verb = str(item.get("verb", "")).strip()
        obj = str(item.get("object", "")).strip()
        if verb and obj:
            outcomes.append({"verb": verb.capitalize(), "object": obj})

    if outcomes:
        return outcomes

    return derive_fallback_learning_outcomes(fallback_objective)


def derive_fallback_learning_outcomes(objective: str) -> List[Dict[str, str]]:
    text = objective.strip()
    prefix = "students should be able to "
    if text.lower().startswith(prefix):
        text = text[len(prefix):]
    text = text.rstrip(".").strip()

    if not text:
        return []

    words = text.split(" ", 1)
    verb = words[0].capitalize()
    obj = words[1] if len(words) > 1 else ""
    if not obj:
        return []
    return [{"verb": verb, "object": obj}]


def derive_fallback_definition(concept: Dict[str, Any], category: str) -> str:
    objective = concept.get("learning_objective", "").strip()
    if objective:
        return objective
    return f"{concept.get('official_name', concept['concept_name'])} ({category.lower()}) -- see chapter material for full definition."


def normalize_blooms(raw: List[Any], default: List[str]) -> List[str]:
    result = []
    for item in raw:
        key = str(item).strip().lower()
        if key in BLOOMS_CANONICAL and BLOOMS_CANONICAL[key] not in result:
            result.append(BLOOMS_CANONICAL[key])
    return result if result else list(default)


def normalize_marks(raw: List[Any], default: List[int]) -> List[int]:
    result = []
    for item in raw:
        try:
            value = int(item)
        except (TypeError, ValueError):
            continue
        if value in ALLOWED_MARKS and value not in result:
            result.append(value)
    return sorted(result) if result else list(default)


def normalize_string_list(raw: List[Any], default: List[str], max_items: int = 5) -> List[str]:
    result = []
    seen = set()
    for item in raw:
        text = str(item).strip()
        key = text.lower()
        if text and key not in seen:
            seen.add(key)
            result.append(text)
    result = result[:max_items]
    return result if result else list(default)


def normalize_formulae_or_examples(raw: List[Any], max_items: int = 6) -> List[str]:
    result = []
    seen = set()
    for item in raw:
        text = str(item).strip()
        key = text.lower()
        if text and key not in seen:
            seen.add(key)
            result.append(text)
    return result[:max_items]


def build_keywords(concept: Dict[str, Any], llm_keywords: List[Any]) -> List[str]:
    """Merge LLM-suggested keywords with the concept's own existing name/alias
    fields, so retrieval keywords stay consistent with fields already present
    on the concept (a name change or alias upstream is automatically
    reflected here without re-inventing anything)."""
    candidates = [
        concept.get("concept_name", ""),
        concept.get("official_name", ""),
        *concept.get("aliases", []),
        *concept.get("search_terms", []),
        *concept.get("abbreviations", []),
        *[str(k) for k in llm_keywords],
    ]

    result = []
    seen = set()
    for text in candidates:
        text = str(text).strip()
        key = text.lower()
        if text and key not in seen:
            seen.add(key)
            result.append(text)
    return result[:12]


def type_based_defaults(category: str) -> Dict[str, Any]:
    """Fallback assessment defaults derived from the (new-enum) concept_category,
    used only when the LLM omits or invalidates a field."""
    if category in ("Law", "Formula", "Measurement"):
        return {
            "preferred_question_types": ["Numerical", "Short Answer"],
            "recommended_marks": [2, 3],
            "blooms_levels": ["Apply", "Analyze"],
            "competencies": ["Problem Solving", "Application"],
        }
    if category == "Definition":
        return {
            "preferred_question_types": ["Very Short Answer", "MCQ"],
            "recommended_marks": [1, 2],
            "blooms_levels": ["Remember", "Understand"],
            "competencies": ["Conceptual Understanding"],
        }
    return {
        "preferred_question_types": ["Short Answer"],
        "recommended_marks": [2, 3],
        "blooms_levels": ["Understand", "Apply"],
        "competencies": ["Conceptual Understanding", "Analytical Thinking"],
    }


def board_frequency_for(concept: Dict[str, Any]) -> Dict[str, str]:
    """NCERT emphasis is estimated from this chapter's own data -- reuse the
    chapter_weightage already assigned to this concept during metadata
    building (Pass 4), rather than asking the LLM to re-guess it from a bare
    concept name with no chapter text in front of it."""
    ncert = str(concept.get("chapter_weightage", "medium")).strip().lower()
    if ncert not in BOARD_FREQ_LEVELS:
        ncert = "medium"
    return {"ncert": ncert, "exemplar": "NA", "pyq": "NA"}


def default_enrichment(concept: Dict[str, Any], children_map: Dict[str, List[str]]) -> Dict[str, Any]:
    category = fallback_category(concept)
    if category == "Core Concept" and looks_like_measurement(concept):
        category = "Measurement"
    defaults = type_based_defaults(category)
    return {
        "definition": derive_fallback_definition(concept, category),
        "formulae": [],
        "examples": [],
        "concept_category": category,
        "is_grouping_node": normalize_is_grouping_node(False, concept, children_map),
        "learning_outcomes": derive_fallback_learning_outcomes(concept.get("learning_objective", "")),
        "assessment": {
            "preferred_question_types": defaults["preferred_question_types"],
            "recommended_marks": defaults["recommended_marks"],
            "blooms_levels": defaults["blooms_levels"],
            "competencies": defaults["competencies"],
            "board_frequency": board_frequency_for(concept),
        },
        "retrieval": {
            "keywords": build_keywords(concept, []),
            "chunk_ids": [],
            "formula_ids": [],
            "example_ids": [],
            "pyq_ids": [],
        },
    }


def apply_enrichment_item(concept: Dict[str, Any], item: Dict[str, Any], children_map: Dict[str, List[str]]) -> Dict[str, Any]:
    category = normalize_category(item.get("concept_category", ""), concept)
    defaults = type_based_defaults(category)

    definition = str(item.get("definition", "")).strip() or derive_fallback_definition(concept, category)
    formulae = normalize_formulae_or_examples(item.get("formulae", []))
    examples = normalize_formulae_or_examples(item.get("examples", []))
    is_grouping_node = normalize_is_grouping_node(item.get("is_grouping_node"), concept, children_map)

    learning_outcomes = normalize_learning_outcomes(
        item.get("learning_outcomes", []), concept.get("learning_objective", "")
    )
    preferred_question_types = normalize_string_list(
        item.get("preferred_question_types", []), defaults["preferred_question_types"]
    )
    recommended_marks = normalize_marks(item.get("recommended_marks", []), defaults["recommended_marks"])
    blooms_levels = normalize_blooms(item.get("blooms_levels", []), defaults["blooms_levels"])
    competencies = normalize_string_list(item.get("competencies", []), defaults["competencies"])
    keywords = build_keywords(concept, item.get("keywords", []))

    return {
        "definition": definition,
        "formulae": formulae,
        "examples": examples,
        "concept_category": category,
        "is_grouping_node": is_grouping_node,
        "learning_outcomes": learning_outcomes,
        "assessment": {
            "preferred_question_types": preferred_question_types,
            "recommended_marks": recommended_marks,
            "blooms_levels": blooms_levels,
            "competencies": competencies,
            "board_frequency": board_frequency_for(concept),
        },
        "retrieval": {
            "keywords": keywords,
            "chunk_ids": [],
            "formula_ids": [],
            "example_ids": [],
            "pyq_ids": [],
        },
    }


# ==========================================================
# CONSISTENCY CHECK (log-only -- never mutates data)
# ==========================================================

def run_consistency_checks(concept_tree: List[Dict[str, Any]]) -> None:
    for c in concept_tree:
        if c.get("is_grouping_node"):
            continue
        cid = c["concept_id"]
        name = c.get("concept_name", "")

        if not c.get("learning_objective", "").strip():
            LOGGER.warning(f"Consistency: {cid} ({name}) has an empty learning_objective")
        if not c.get("concept_category", "").strip():
            LOGGER.warning(f"Consistency: {cid} ({name}) has an empty concept_category")
        if not c.get("concept_type", "").strip():
            LOGGER.warning(f"Consistency: {cid} ({name}) has an empty concept_type")
        if not c.get("aliases") and not c.get("search_terms"):
            LOGGER.info(f"Consistency: {cid} ({name}) has no aliases or search_terms -- retrieval keywords will rely on the concept name alone")


# ==========================================================
# FINAL FIELD ORDERING (Identity / Knowledge / Educational / Assessment / Retrieval)
# ==========================================================

def assemble_concept(concept: Dict[str, Any], enrichment: Dict[str, Any]) -> Dict[str, Any]:
    return {
        # Identity
        "concept_id": concept["concept_id"],
        "concept_name": concept["concept_name"],
        "parent_concept": concept.get("parent_concept", ""),
        "is_grouping_node": enrichment["is_grouping_node"],
        "official_name": concept.get("official_name", concept["concept_name"]),
        "aliases": concept.get("aliases", []),
        "search_terms": concept.get("search_terms", []),
        "abbreviations": concept.get("abbreviations", []),
        # Knowledge
        "definition": enrichment["definition"],
        "formulae": enrichment["formulae"],
        "examples": enrichment["examples"],
        "related_concepts": concept.get("related_concepts", []),
        # Educational Metadata
        "importance": concept.get("importance", "medium"),
        "chapter_weightage": concept.get("chapter_weightage", "medium"),
        "concept_category": enrichment["concept_category"],
        "concept_type": concept.get("concept_type", ""),
        "prerequisites": concept.get("prerequisites", []),
        "difficulty_hint": concept.get("difficulty_hint", ""),
        "learning_outcomes": enrichment["learning_outcomes"],
        # Assessment Metadata
        "assessment": enrichment["assessment"],
        # Retrieval Metadata
        "retrieval": enrichment["retrieval"],
    }


# ==========================================================
# MAIN ENRICHMENT
# ==========================================================

def enrich_concepts(
    chapter: str,
    concept_tree: List[Dict[str, Any]],
    related_by_id: Dict[str, List[str]],
) -> List[Dict[str, Any]]:
    valid_ids = {c["concept_id"] for c in concept_tree}
    children_map = compute_children_map(concept_tree)

    enrichment_by_id: Dict[str, Dict[str, Any]] = {}

    batches = [concept_tree[i:i + BATCH_SIZE] for i in range(0, len(concept_tree), BATCH_SIZE)]
    LOGGER.info(f"Processing {len(concept_tree)} concept(s) in {len(batches)} batch(es) of up to {BATCH_SIZE}")

    for batch_num, batch in enumerate(batches, start=1):
        remaining = list(batch)
        round_num = 0

        while remaining and round_num <= MAX_RECONCILE_ROUNDS:
            round_num += 1
            LOGGER.info(
                f"Batch {batch_num}/{len(batches)}, round {round_num}: "
                f"requesting enrichment for {len(remaining)} concept(s)"
            )

            user_prompt = build_user_prompt(chapter, remaining, children_map)
            validator = make_validator(valid_ids)

            parsed = utils.call_llm_json(
                system_prompt=SYSTEM_PROMPT,
                user_prompt=user_prompt,
                logger=LOGGER,
                validator=validator,
                raw_dump_filename=f"final_refinement_raw_output_batch{batch_num}_round{round_num}.txt",
            )

            concepts_by_id = {c["concept_id"]: c for c in remaining}
            for item in parsed["enrichment"]:
                cid = item["concept_id"]
                concept = concepts_by_id.get(cid)
                if concept is None:
                    continue
                enrichment_by_id[cid] = apply_enrichment_item(concept, item, children_map)

            remaining = [c for c in batch if c["concept_id"] not in enrichment_by_id]

            if remaining:
                LOGGER.warning(
                    f"Batch {batch_num}: {len(remaining)} concept(s) still missing after round {round_num}: "
                    f"{[c['concept_id'] for c in remaining]}"
                )

        if remaining:
            LOGGER.warning(
                f"Batch {batch_num}: filling {len(remaining)} concept(s) with default enrichment after "
                f"{MAX_RECONCILE_ROUNDS} reconciliation round(s)"
            )
            for concept in remaining:
                enrichment_by_id[concept["concept_id"]] = default_enrichment(concept, children_map)

    enriched_tree = []
    for concept in concept_tree:
        concept_with_related = dict(concept)
        concept_with_related["related_concepts"] = related_by_id.get(concept["concept_id"], [])
        enriched_tree.append(assemble_concept(concept_with_related, enrichment_by_id[concept["concept_id"]]))

    return enriched_tree


def main() -> None:
    LOGGER.info("=" * 80)
    LOGGER.info("FINAL REFINEMENT -- KNOWLEDGE, ASSESSMENT & RETRIEVAL ENRICHMENT")
    LOGGER.info("=" * 80)

    kb_doc = utils.load_json(utils.FINAL_KB_FILE)
    chapter = kb_doc.get("chapter", "")
    concept_tree = kb_doc["concept_tree"]
    relationships = kb_doc.get("relationships", [])

    run_consistency_checks(concept_tree)

    related_by_id = compute_related_concepts(concept_tree, relationships)
    enriched_tree = enrich_concepts(chapter, concept_tree, related_by_id)

    result = {
        "chapter": chapter,
        "concept_tree": enriched_tree,
        "relationships": relationships,
        "question_bank": kb_doc.get("question_bank", []),
    }

    utils.save_json(result, utils.ENRICHED_KB_FILE)
    LOGGER.info(f"Saved: {utils.ENRICHED_KB_FILE}")

    LOGGER.info("Summary")
    LOGGER.info(f"  Concepts enriched : {len(enriched_tree)}")

    grouping_count = sum(1 for c in enriched_tree if c["is_grouping_node"])
    LOGGER.info(f"  Grouping nodes    : {grouping_count} -- {[c['concept_name'] for c in enriched_tree if c['is_grouping_node']]}")

    category_counts: Dict[str, int] = {}
    for c in enriched_tree:
        category_counts[c["concept_category"]] = category_counts.get(c["concept_category"], 0) + 1
    for category, count in sorted(category_counts.items()):
        LOGGER.info(f"    concept_category={category:14s} : {count}")

    ncert_counts: Dict[str, int] = {}
    for c in enriched_tree:
        level = c["assessment"]["board_frequency"]["ncert"]
        ncert_counts[level] = ncert_counts.get(level, 0) + 1
    for level, count in sorted(ncert_counts.items()):
        LOGGER.info(f"    ncert_emphasis={level:8s} : {count}")


if __name__ == "__main__":
    main()
