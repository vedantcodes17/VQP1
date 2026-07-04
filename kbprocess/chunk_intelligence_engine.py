import json
import requests

# ==========================================================
# CONFIG
# ==========================================================

FILE_PATH = "education_knowledge_base.json"

LMSTUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"

MODEL = "qwen2.5-vl-7b-instruct"

CHAPTER = "Unit 1: Solutions"

CHUNK_INDEX = 0

WINDOW = 1        # Previous + Current + Next

# ==========================================================
# LOAD KB
# ==========================================================

with open(FILE_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

chapter_chunks = []

for item in data:

    payload = item.get("payload", {})

    if payload.get("chapter") == CHAPTER:
        chapter_chunks.append(payload)

print(f"Loaded {len(chapter_chunks)} chunks")

# ==========================================================
# BUILD SLIDING WINDOW
# ==========================================================

start = max(0, CHUNK_INDEX - WINDOW)
end = min(len(chapter_chunks), CHUNK_INDEX + WINDOW + 1)

context = ""

for i in range(start, end):

    c = chapter_chunks[i]

    context += f"""

===============================
CHUNK {i}
===============================

Topic:
{c.get("topic")}

Context:
{c.get("context")}

Type:
{c.get("content_type")}

Content:

{c.get("document")}
"""

# ==========================================================
# SYSTEM PROMPT
# ==========================================================

SYSTEM_PROMPT = """
You are a senior NCERT textbook author,
CBSE curriculum designer,
and Class 12 Chemistry teacher.

You are NOT extracting concepts.

Your job is to understand the educational purpose of the CURRENT chunk.

The surrounding chunks are only for context.

Determine:

• What educational role does the CURRENT chunk play?

• Should a concept extraction engine process it?

• Or should it simply be linked with concepts extracted elsewhere?

Return ONLY JSON.

Schema:

{
    "chunk_category":"",
    "action":"",
    "concept_rich":true,
    "confidence":0.98,
    "reason":"",
    "learning_objective":"",
    "educational_role":"",
    "contains":{

        "definition":false,
        "theory":false,
        "formula":false,
        "example":false,
        "question":false,
        "diagram_reference":false

    }
}

Allowed actions:

extract_concepts

link_existing_concepts

ignore

Rules:

Definitions usually introduce concepts.

Theory introduces concepts.

Examples usually reinforce concepts.

Questions usually reinforce concepts.

Exercise headers should be ignored.

Return JSON only.
"""

USER_PROMPT = f"""
CURRENT CHUNK INDEX:

{CHUNK_INDEX}

Analyze ONLY the CURRENT chunk.

Neighbouring chunks are given only for context.

{context}
"""

# ==========================================================
# CALL MODEL
# ==========================================================

payload = {

    "model": MODEL,

    "temperature": 0.1,

    "messages":[

        {
            "role":"system",
            "content":SYSTEM_PROMPT
        },

        {
            "role":"user",
            "content":USER_PROMPT
        }

    ]
}

print("\nCalling Local LLM...\n")

response = requests.post(

    LMSTUDIO_URL,

    json=payload,

    timeout=180

)

response.raise_for_status()

result = response.json()

print("="*80)
print("MODEL OUTPUT")
print("="*80)

print(result["choices"][0]["message"]["content"])