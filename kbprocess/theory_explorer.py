import json

FILE_PATH = "education_knowledge_base.json"
CHAPTER = "Unit 1: Solutions"

GOOD_TYPES = {
    "text",
    "definition",
    "formula",
    "example",
    "derivation",
    "summary",
    "theory"
}

with open(FILE_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

records = []

for item in data:
    payload = item["payload"]

    if (
        payload.get("chapter") == CHAPTER
        and payload.get("content_type") in GOOD_TYPES
    ):
        records.append(payload)

print(f"\nFound {len(records)} informative chunks.\n")

for i, r in enumerate(records[:10], 1):

    print("=" * 100)
    print(f"Chunk {i}")
    print("=" * 100)

    print("Topic :", r.get("topic"))
    print("Type  :", r.get("content_type"))
    print("Source:", r.get("source"))

    print("\n")

    text = r.get("document", "")

    print(text[:1800])

    print("\n\n")