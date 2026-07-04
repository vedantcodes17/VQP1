import json
import requests

# ==========================================================
# CONFIGURATION
# ==========================================================

FILE_PATH = "education_knowledge_base.json"

LMSTUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"

MODEL = "qwen2.5-vl-7b-instruct"

CHAPTER_NAME = "Unit 1: Solutions"

CURRENT_CHUNK_INDEX = 5

WINDOW_SIZE = 1

TEMPERATURE = 0.1

# ==========================================================
# LOAD KNOWLEDGE BASE
# ==========================================================

print("=" * 80)
print("LOADING KNOWLEDGE BASE")
print("=" * 80)

with open(FILE_PATH, "r", encoding="utf-8") as f:
    kb = json.load(f)

chapter_chunks = []

for item in kb:

    payload = item.get("payload", {})

    if payload.get("chapter") == CHAPTER_NAME:
        chapter_chunks.append(payload)

print(f"Loaded {len(chapter_chunks)} chunks from '{CHAPTER_NAME}'")

# ==========================================================
# VALIDATE INDEX
# ==========================================================

if CURRENT_CHUNK_INDEX >= len(chapter_chunks):
    raise Exception("Invalid CURRENT_CHUNK_INDEX")

# ==========================================================
# GET CHUNKS
# ==========================================================

previous_chunk = ""

current_chunk = ""

next_chunk = ""

if CURRENT_CHUNK_INDEX > 0:
    previous_chunk = chapter_chunks[CURRENT_CHUNK_INDEX - 1].get("document", "")

current_chunk = chapter_chunks[CURRENT_CHUNK_INDEX].get("document", "")

if CURRENT_CHUNK_INDEX < len(chapter_chunks) - 1:
    next_chunk = chapter_chunks[CURRENT_CHUNK_INDEX + 1].get("document", "")

current_payload = chapter_chunks[CURRENT_CHUNK_INDEX]

print("\nCurrent Chunk Information\n")

print(f"Topic        : {current_payload.get('topic')}")
print(f"Context      : {current_payload.get('context')}")
print(f"Content Type : {current_payload.get('content_type')}")
print(f"Source       : {current_payload.get('source')}")

# ==========================================================
# SYSTEM PROMPT
# ==========================================================

SYSTEM_PROMPT = """
You are a senior NCERT textbook author,
CBSE curriculum designer,
and an experienced Class 12 teacher.

You are the Concept Extraction Engine.

Imagine that you have just finished teaching ONLY the CURRENT chunk in today's classroom.

Your task is to write down ONLY the concepts that students should have learned from THIS lesson.

The Previous and Next chunks are provided ONLY to understand continuity.

Never extract concepts from the Previous or Next chunks.

------------------------------------------------------------

STRICT RULES

1. Analyze ONLY the CURRENT chunk.

2. Ignore concepts that appear only in the Previous or Next chunk.

3. Extract concepts ONLY if they are:

• introduced

OR

• formally defined

OR

• substantially explained

inside the CURRENT chunk.

4. Ignore:

- Questions
- Exercises
- Numerical problems
- Solved examples
- Exercise headers
- Section titles
- Answer keys

unless they actually introduce a new concept.

5. Never invent concept names.

6. Never rename concepts.

7. Never merge concepts.

8. Never create aliases.

9. Use the exact terminology found in the CURRENT chunk.

10. If the chunk does not introduce any new concept,

return

{
    "concepts":[]
}

------------------------------------------------------------

Return ONLY valid JSON.

Schema

{
    "concepts":[

        {

            "name":"",

            "introduced":true,

            "evidence":"Short sentence from CURRENT chunk showing why this concept was extracted."

        }

    ]
}

No markdown.

No explanation.

Only JSON.
"""

# ==========================================================
# USER PROMPT
# ==========================================================

USER_PROMPT = f"""
REFERENCE CHUNK (PREVIOUS)
------------------------------------------------------------

{previous_chunk}

============================================================

CURRENT CHUNK (ONLY THIS CHUNK SHOULD BE ANALYZED)

Topic:
{current_payload.get("topic")}

Context:
{current_payload.get("context")}

Content Type:
{current_payload.get("content_type")}

Content:

{current_chunk}

============================================================

REFERENCE CHUNK (NEXT)

------------------------------------------------------------

{next_chunk}

IMPORTANT

Extract concepts ONLY from the CURRENT CHUNK.

The surrounding chunks are provided ONLY to understand context.
"""

# ==========================================================
# REQUEST
# ==========================================================

payload = {

    "model": MODEL,

    "temperature": TEMPERATURE,

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

print("\n")
print("=" * 80)
print("CALLING LOCAL LLM")
print("=" * 80)

response = requests.post(

    LMSTUDIO_URL,

    json=payload,

    timeout=300

)

response.raise_for_status()

result = response.json()

output = result["choices"][0]["message"]["content"]

print("\n")
print("=" * 80)
print("CONCEPT EXTRACTION RESULT")
print("=" * 80)

print(output)

# ==========================================================
# OPTIONAL JSON VALIDATION
# ==========================================================

print("\n")
print("=" * 80)
print("JSON VALIDATION")
print("=" * 80)

try:

    parsed = json.loads(output)

    print("✅ Valid JSON")

    print(f"Extracted Concepts : {len(parsed.get('concepts', []))}")

except Exception as e:

    print("❌ Invalid JSON")
    print(e)