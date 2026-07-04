import json
import requests

# ============================================================
# CONFIG
# ============================================================

LMSTUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"

FILE_PATH = "education_knowledge_base.json"

CHAPTER = "Unit 1: Solutions"

# Select which chunk to test
CHUNK_INDEX = 0

MODEL = "qwen2.5-vl-7b-instruct"

# ============================================================
# LOAD DATA
# ============================================================

with open(FILE_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

chapter_chunks = []

for item in data:

    payload = item.get("payload", {})

    if payload.get("chapter") == CHAPTER:
        chapter_chunks.append(payload)

print(f"Found {len(chapter_chunks)} chunks")

chunk = chapter_chunks[CHUNK_INDEX]

print("\nUsing Chunk\n")
print("=" * 80)

print("Topic   :", chunk.get("topic"))
print("Type    :", chunk.get("content_type"))
print("Context :", chunk.get("context"))
print("Source  :", chunk.get("source"))

print("=" * 80)

DOCUMENT = chunk.get("document", "")

# ============================================================
# PROMPT
# ============================================================

SYSTEM_PROMPT = """
You are an experienced CBSE Class 12 Chemistry teacher and NCERT textbook reviewer.

Your job is NOT to extract concepts.

Your first responsibility is to determine whether the given chunk introduces or explains one or more academic concepts.

A concept means a topic that should appear in a teacher's lesson plan.

Ignore the following:

- Practice questions
- Exercise headers
- Numerical problems
- Answer keys
- Section titles
- Repeated solved examples that introduce no new learning

If the chunk mainly teaches, defines, explains or introduces an idea, then it is concept rich.

Return ONLY valid JSON.

{
    "concept_rich": true,
    "chunk_type": "definition/theory/example/question/formula/header/solution/etc",
    "confidence": 0.95,
    "reason": "Short explanation",
    "primary_learning_objective": "One sentence"
}

Do not return markdown.

Do not explain anything.

Return JSON only.
"""

USER_PROMPT = f"""
Analyze the following chunk.

Subject: {chunk.get('subject')}
Chapter: {chunk.get('chapter')}
Topic: {chunk.get('topic')}
Context: {chunk.get('context')}
Content Type: {chunk.get('content_type')}

Chunk:

{DOCUMENT}
"""

# ============================================================
# API CALL
# ============================================================

payload = {
    "model": MODEL,
    "temperature": 0.1,
    "messages": [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": USER_PROMPT
        }
    ]
}

print("\nSending request to Local LLM...\n")

response = requests.post(
    LMSTUDIO_URL,
    json=payload,
    timeout=120
)

response.raise_for_status()

result = response.json()

print("=" * 80)
print("MODEL RESPONSE")
print("=" * 80)

print(result["choices"][0]["message"]["content"])