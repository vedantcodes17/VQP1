import json

# ==========================================================
# CONFIGURATION
# ==========================================================

INPUT_FILE = "unit1_solutions_preprocessed.json"
OUTPUT_FILE = "unit1_learning_blocks.json"

MAX_BLOCK_LENGTH = 2500

COMPATIBLE_TYPES = {
    "definition": ["text", "formula", "example"],
    "text": ["definition", "formula", "example", "derivation"],
    "formula": ["text", "example"],
    "example": ["formula", "text", "derivation"],
    "derivation": ["text", "example"]
}

# ==========================================================
# LOAD PREPROCESSED DATA
# ==========================================================

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    chunks = json.load(f)

print("=" * 80)
print("LEARNING BLOCK BUILDER")
print("=" * 80)
print(f"Input Chunks : {len(chunks)}")

# ==========================================================
# BUILD BLOCKS
# ==========================================================

learning_blocks = []

current_block = None

block_id = 1

for chunk in chunks:

    text = chunk.get("document", "").strip()

    topic = chunk.get("topic")
    context = chunk.get("context")
    source = chunk.get("source")
    ctype = chunk.get("content_type")

    # ------------------------------------------------------
    # START FIRST BLOCK
    # ------------------------------------------------------

    if current_block is None:

        current_block = {
            "block_id": block_id,
            "topic": topic,
            "context": context,
            "source": source,
            "content_types": [ctype],
            "chunks": [chunk],
            "combined_text": text
        }

        continue

    # ------------------------------------------------------
    # CHECK IF MERGE POSSIBLE
    # ------------------------------------------------------

    same_topic = topic == current_block["topic"]

    same_source = source == current_block["source"]

    compatible = (
        current_block["content_types"][-1] in COMPATIBLE_TYPES
        and ctype in COMPATIBLE_TYPES[current_block["content_types"][-1]]
    )

    size_ok = (
        len(current_block["combined_text"]) + len(text)
        <= MAX_BLOCK_LENGTH
    )

    # Don't merge questions
    if ctype == "question":
        compatible = False

    # ------------------------------------------------------
    # MERGE
    # ------------------------------------------------------

    if same_topic and same_source and compatible and size_ok:

        current_block["chunks"].append(chunk)
        current_block["content_types"].append(ctype)

        current_block["combined_text"] += "\n\n" + text

    else:

        learning_blocks.append(current_block)

        block_id += 1

        current_block = {
            "block_id": block_id,
            "topic": topic,
            "context": context,
            "source": source,
            "content_types": [ctype],
            "chunks": [chunk],
            "combined_text": text
        }

# ==========================================================
# SAVE LAST BLOCK
# ==========================================================

if current_block is not None:
    learning_blocks.append(current_block)

# ==========================================================
# SAVE
# ==========================================================

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(learning_blocks, f, indent=2, ensure_ascii=False)

# ==========================================================
# REPORT
# ==========================================================

print("\n")
print("=" * 80)
print("REPORT")
print("=" * 80)

print(f"Learning Blocks : {len(learning_blocks)}")

avg_chunks = sum(len(b["chunks"]) for b in learning_blocks) / len(learning_blocks)
avg_chars = sum(len(b["combined_text"]) for b in learning_blocks) / len(learning_blocks)

print(f"Average Chunks per Block : {avg_chunks:.2f}")
print(f"Average Characters       : {avg_chars:.0f}")

print("\nTop 10 Blocks\n")

for block in learning_blocks[:10]:

    print(
        f"Block {block['block_id']:3} | "
        f"Chunks: {len(block['chunks']):2} | "
        f"Topic: {block['topic']} | "
        f"Types: {', '.join(block['content_types'])}"
    )

print("\nSaved:", OUTPUT_FILE)
print("=" * 80)