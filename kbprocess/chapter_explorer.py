import json
from collections import Counter

FILE_PATH = "education_knowledge_base.json"

# Change this whenever you want another chapter
CHAPTER_NAME = "Unit 1: Solutions"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

records = []

for item in data:
    payload = item.get("payload", {})

    if payload.get("chapter") == CHAPTER_NAME:
        records.append(payload)

print("=" * 80)
print("CHAPTER ANALYSIS")
print("=" * 80)

print(f"Chapter : {CHAPTER_NAME}")
print(f"Total Chunks : {len(records)}")

print("\nSources")
print("-" * 40)
print(Counter(r.get("source") for r in records))

print("\nContent Types")
print("-" * 40)
print(Counter(r.get("content_type") for r in records))

print("\nTopics")
print("-" * 40)

topics = Counter(r.get("topic") for r in records)

for topic, count in topics.items():
    print(f"{count:3}  {topic}")

print("\nSample Chunk")
print("-" * 80)

sample = records[0]

print("Topic :", sample.get("topic"))
print("Type  :", sample.get("content_type"))
print("Source:", sample.get("source"))

print("\nContent Preview:\n")

text = sample.get("document", "")
print(text[:2500])