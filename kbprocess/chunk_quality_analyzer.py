import json
from collections import Counter

FILE_PATH = "education_knowledge_base.json"
CHAPTER = "Unit 1: Solutions"

# Words indicating useful concept-rich content
POSITIVE_KEYWORDS = [
    "definition",
    "is called",
    "refers to",
    "defined as",
    "introduction",
    "concept",
    "principle",
    "law",
    "theory",
    "property",
    "formula",
    "equation",
    "relationship",
    "process",
    "measurement",
    "explanation",
    "means"
]

# Words indicating practice/solution content
NEGATIVE_KEYWORDS = [
    "exercise",
    "question",
    "objective",
    "subjective",
    "solution",
    "answer",
    "section",
    "calculate",
    "find",
    "mcq",
    "choose",
    "correct option",
    "paragraph for questions",
    "numerical"
]

with open(FILE_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

concept_chunks = []
non_concept_chunks = []

for item in data:

    payload = item.get("payload", {})

    if payload.get("chapter") != CHAPTER:
        continue

    text = payload.get("document", "").lower()

    positive = sum(k in text for k in POSITIVE_KEYWORDS)
    negative = sum(k in text for k in NEGATIVE_KEYWORDS)

    if positive >= negative:
        concept_chunks.append(payload)
    else:
        non_concept_chunks.append(payload)

print("="*70)
print("CHUNK QUALITY ANALYSIS")
print("="*70)

print(f"\nTotal Chunks           : {len(concept_chunks)+len(non_concept_chunks)}")
print(f"Concept Rich Chunks    : {len(concept_chunks)}")
print(f"Practice/Other Chunks  : {len(non_concept_chunks)}")

print("\n" + "="*70)
print("TOP CONCEPT CHUNKS")
print("="*70)

for i, chunk in enumerate(concept_chunks[:5], 1):
    print(f"\n[{i}]")
    print("Source :", chunk.get("source"))
    print("Type   :", chunk.get("content_type"))
    print("Topic  :", chunk.get("topic"))
    print("Context:", chunk.get("context"))
    print("-"*70)
    print(chunk.get("document", "")[:700])

print("\n" + "="*70)
print("TOP NON-CONCEPT CHUNKS")
print("="*70)

for i, chunk in enumerate(non_concept_chunks[:5], 1):
    print(f"\n[{i}]")
    print("Source :", chunk.get("source"))
    print("Type   :", chunk.get("content_type"))
    print("Topic  :", chunk.get("topic"))
    print("Context:", chunk.get("context"))
    print("-"*70)
    print(chunk.get("document", "")[:700])