import json
import hashlib

# ==========================================================
# CONFIGURATION
# ==========================================================

INPUT_FILE = "education_knowledge_base.json"

OUTPUT_FILE = "unit1_solutions_preprocessed.json"

CHAPTER_NAME = "Unit 1: Solutions"

MIN_CONTENT_LENGTH = 120

HEADER_PATTERNS = [

    "section-",
    "section ",
    "exercise",
    "part-i",
    "part-ii",
    "part iii",
    "part-iii",
    "objective",
    "subjective",
    "matching list",
    "multiple choice",
    "fill in the blanks",
    "true or false",
    "only one correct",
    "numerical value type",
    "paragraph for questions"

]

# ==========================================================
# LOAD DATA
# ==========================================================

print("=" * 80)
print("LOADING KNOWLEDGE BASE")
print("=" * 80)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    kb = json.load(f)

print(f"Total Records : {len(kb)}")

# ==========================================================
# FILTER CHAPTER
# ==========================================================

chapter_chunks = []

for record in kb:

    payload = record.get("payload", {})

    if payload.get("chapter") == CHAPTER_NAME:
        chapter_chunks.append(payload)

print(f"Chapter Chunks : {len(chapter_chunks)}")

# ==========================================================
# PREPROCESSING
# ==========================================================

seen_hashes = set()

clean_chunks = []

stats = {
    "duplicates": 0,
    "empty": 0,
    "headers": 0,
    "short": 0,
    "kept": 0
}

for chunk in chapter_chunks:

    text = chunk.get("document", "").strip()

    # ------------------------------------------------------
    # Empty
    # ------------------------------------------------------

    if not text:

        stats["empty"] += 1
        continue

    # ------------------------------------------------------
    # Duplicate
    # ------------------------------------------------------

    text_hash = hashlib.md5(text.encode("utf-8")).hexdigest()

    if text_hash in seen_hashes:

        stats["duplicates"] += 1
        continue

    seen_hashes.add(text_hash)

    # ------------------------------------------------------
    # Too Short
    # ------------------------------------------------------

    if len(text) < MIN_CONTENT_LENGTH:

        stats["short"] += 1
        continue

    # ------------------------------------------------------
    # Header Detection
    # ------------------------------------------------------

    lower = text.lower()

    is_header = False

    for pattern in HEADER_PATTERNS:

        if pattern in lower[:300]:

            is_header = True
            break

    if is_header:

        stats["headers"] += 1
        continue

    # ------------------------------------------------------
    # Keep
    # ------------------------------------------------------

    clean_chunks.append(chunk)

    stats["kept"] += 1

# ==========================================================
# SAVE
# ==========================================================

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

    json.dump(clean_chunks, f, indent=2, ensure_ascii=False)

# ==========================================================
# REPORT
# ==========================================================

print("\n")

print("=" * 80)
print("PREPROCESSING REPORT")
print("=" * 80)

print(f"Original Chunks        : {len(chapter_chunks)}")
print(f"Duplicates Removed     : {stats['duplicates']}")
print(f"Empty Removed          : {stats['empty']}")
print(f"Headers Removed        : {stats['headers']}")
print(f"Short Chunks Removed   : {stats['short']}")
print(f"Final Chunks           : {stats['kept']}")

print("\nSaved File")

print(OUTPUT_FILE)

print("=" * 80)