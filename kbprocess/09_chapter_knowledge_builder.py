import json
import re
import requests
from pathlib import Path

# ==========================================================
# CONFIGURATION
# ==========================================================

INPUT_FILE = r"data\solution.txt"

OUTPUT_FILE = "chapter_kb.json"

LMSTUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"

MODEL = "qwen2.5-vl-7b-instruct"

TEMPERATURE = 0.1

# ==========================================================
# LOAD FILE
# ==========================================================

print("=" * 80)
print("CHAPTER KNOWLEDGE BUILDER")
print("=" * 80)

text = Path(INPUT_FILE).read_text(
    encoding="utf-8",
    errors="ignore"
)

print(f"\nOriginal Length : {len(text):,} characters")

# ==========================================================
# PREPROCESS
# ==========================================================

print("\nPreprocessing...")

# normalize newlines
text = text.replace("\r\n", "\n")

# remove multiple blank lines
text = re.sub(r"\n{3,}", "\n\n", text)

# remove repeated spaces
text = re.sub(r"[ \t]+", " ", text)

# strip line endings
text = "\n".join(line.rstrip() for line in text.splitlines())

print(f"Clean Length : {len(text):,} characters")

# ==========================================================
# SYSTEM PROMPT
# ==========================================================

SYSTEM_PROMPT = """
You are a senior NCERT textbook author,
CBSE curriculum designer,
and experienced Class 12 teacher.

You are building the canonical chapter knowledge base.

The input is teacher notes.

The notes may contain:

• Concepts
• Definitions
• Formulae
• Relationships
• Examples
• Important Questions
• Short Answer Questions
• Numerical Questions
• Self Assessment

Your task is to organise the chapter into structured knowledge.

RULES

1. Use ONLY information present in the notes.

2. Never invent concepts.

3. Merge duplicate concepts.

4. Use official educational terminology.

5. Preserve all formulae.

6. Preserve all definitions.

7. Every question must belong to one or more concepts.

8. Build parent-child relationships wherever applicable.

9. Return ONLY valid JSON.

Output Schema

{
    "chapter":"",

    "concept_tree":[
        {
            "concept_name":"",
            "parent_concept":""
        }
    ],

    "knowledge_nodes":[
        {
            "concept_name":"",
            "definition":"",
            "formulae":[],
            "important_points":[],
            "related_concepts":[]
        }
    ],

    "question_bank":[
        {
            "question":"",
            "question_type":"",
            "linked_concepts":[]
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
Build the canonical knowledge base for this chapter.

Teacher Notes

{text}
"""

# ==========================================================
# API REQUEST
# ==========================================================

payload = {

    "model": MODEL,

    "temperature": TEMPERATURE,

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

    timeout=600

)

response.raise_for_status()

result = response.json()

output = result["choices"][0]["message"]["content"]

# ==========================================================
# SAVE RAW OUTPUT
# ==========================================================

print("=" * 80)
print("MODEL RESPONSE")
print("=" * 80)

print(output[:2500])

# ==========================================================
# JSON VALIDATION
# ==========================================================

print("\nValidating JSON...")

try:

    parsed = json.loads(output)

    print("✅ Valid JSON")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

        json.dump(parsed, f, indent=2, ensure_ascii=False)

    print(f"\nSaved : {OUTPUT_FILE}")

    print("\nSummary")

    print("-" * 40)

    print("Concept Tree      :", len(parsed.get("concept_tree", [])))

    print("Knowledge Nodes   :", len(parsed.get("knowledge_nodes", [])))

    print("Question Bank     :", len(parsed.get("question_bank", [])))

except Exception as e:

    print("❌ Invalid JSON")

    with open("raw_output.txt","w",encoding="utf-8") as f:

        f.write(output)

    print("Raw response saved as raw_output.txt")

    print(e)