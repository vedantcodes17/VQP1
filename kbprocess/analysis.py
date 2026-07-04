import json
from collections import Counter

# ==========================
# CONFIG
# ==========================

FILE_PATH = "education_knowledge_base.json"

# ==========================
# LOAD DATA
# ==========================

with open(FILE_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print(f"\nTotal Records : {len(data)}")

# ==========================
# COUNTERS
# ==========================

subjects = Counter()
grades = Counter()
chapters = Counter()
topics = Counter()
sources = Counter()
content_types = Counter()

for record in data:

    payload = record.get("payload", {})

    subjects[payload.get("subject", "Unknown")] += 1
    grades[payload.get("grade", "Unknown")] += 1
    chapters[payload.get("chapter", "Unknown")] += 1
    topics[payload.get("topic", "Unknown")] += 1
    sources[payload.get("source", "Unknown")] += 1
    content_types[payload.get("content_type", "Unknown")] += 1

# ==========================
# PRINT RESULTS
# ==========================

def print_counter(title, counter, top=20):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    for item, count in counter.most_common(top):
        print(f"{item:<45} {count}")

print_counter("SUBJECTS", subjects)
print_counter("GRADES", grades)
print_counter("SOURCES", sources)
print_counter("CONTENT TYPES", content_types)

print("\n" + "=" * 60)
print(f"Unique Chapters : {len(chapters)}")
print(f"Unique Topics   : {len(topics)}")
print("=" * 60)