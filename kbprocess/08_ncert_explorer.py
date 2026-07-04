import json
from collections import Counter, defaultdict

# ==========================================================
# CONFIGURATION
# ==========================================================

INPUT_FILE = "education_knowledge_base.json"

SOURCE = "NCERT_Textbooks"

CHAPTER_NAME = "Unit 1: Solutions"

SHOW_CONTEXT_PREVIEW = True
SHOW_SAMPLE_CHUNKS = True
SAMPLE_PER_CONTEXT = 2

# ==========================================================
# LOAD DATA
# ==========================================================

print("=" * 90)
print("NCERT EXPLORER")
print("=" * 90)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    kb = json.load(f)

# ==========================================================
# FILTER NCERT CHUNKS
# ==========================================================

chunks = []

for record in kb:

    payload = record.get("payload", {})

    if (
        payload.get("source") == SOURCE
        and payload.get("chapter") == CHAPTER_NAME
    ):
        chunks.append(payload)

print(f"\nNCERT Chunks Found : {len(chunks)}")

if len(chunks) == 0:
    print("\nNo NCERT chunks found.")
    exit()

# ==========================================================
# BASIC ANALYSIS
# ==========================================================

content_type_counter = Counter()
topic_counter = Counter()
context_counter = Counter()

context_groups = defaultdict(list)

for chunk in chunks:

    content_type_counter[chunk.get("content_type")] += 1
    topic_counter[chunk.get("topic")] += 1
    context_counter[chunk.get("context")] += 1

    context_groups[chunk.get("context")].append(chunk)

# ==========================================================
# CONTENT TYPES
# ==========================================================

print("\n" + "=" * 90)
print("CONTENT TYPES")
print("=" * 90)

for k, v in content_type_counter.most_common():
    print(f"{str(k):35} {v}")

# ==========================================================
# TOPICS
# ==========================================================

print("\n" + "=" * 90)
print("TOPICS")
print("=" * 90)

for k, v in topic_counter.most_common():
    print(f"{str(k):50} {v}")

# ==========================================================
# CONTEXT ANALYSIS
# ==========================================================

print("\n" + "=" * 90)
print("TOP CONTEXTS")
print("=" * 90)

for context, count in context_counter.most_common(20):

    print(f"\nContext : {context}")
    print(f"Chunks  : {count}")

# ==========================================================
# CONTEXT PREVIEW
# ==========================================================

if SHOW_CONTEXT_PREVIEW:

    print("\n")
    print("=" * 90)
    print("CONTEXT PREVIEW")
    print("=" * 90)

    sorted_contexts = sorted(
        context_groups.items(),
        key=lambda x: len(x[1]),
        reverse=True
    )

    for context, group in sorted_contexts[:10]:

        print("\n")
        print("-" * 90)
        print(f"Context : {context}")
        print(f"Chunks  : {len(group)}")
        print("-" * 90)

        for chunk in group[:SAMPLE_PER_CONTEXT]:

            print(f"\nType : {chunk.get('content_type')}")
            print(f"Topic: {chunk.get('topic')}")

            preview = chunk.get("document", "")[:500]

            print("\nPreview:\n")
            print(preview)
            print()

# ==========================================================
# SAMPLE CHUNKS
# ==========================================================

if SHOW_SAMPLE_CHUNKS:

    print("\n")
    print("=" * 90)
    print("FIRST 10 NCERT CHUNKS")
    print("=" * 90)

    for i, chunk in enumerate(chunks[:10]):

        print("\n")
        print("-" * 90)

        print(f"Chunk Index : {i}")
        print(f"Topic       : {chunk.get('topic')}")
        print(f"Context     : {chunk.get('context')}")
        print(f"Type        : {chunk.get('content_type')}")

        print("\nPreview:\n")

        print(chunk.get("document", "")[:600])

# ==========================================================
# FINAL REPORT
# ==========================================================

print("\n")
print("=" * 90)
print("SUMMARY")
print("=" * 90)

print(f"Total NCERT Chunks     : {len(chunks)}")
print(f"Unique Topics          : {len(topic_counter)}")
print(f"Unique Contexts        : {len(context_counter)}")

multi_contexts = sum(
    1 for c in context_counter.values() if c > 1
)

print(f"Contexts with >1 Chunk : {multi_contexts}")

largest = max(context_counter.values())

print(f"Largest Context Size   : {largest}")

print("=" * 90)