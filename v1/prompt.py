"""
Central Prompt Repository

Every LLM prompt is stored here.

Generator scripts simply call

get_concept_prompt()

or

get_formula_prompt()
"""


def get_concept_prompt():

    return f"""
You are a Senior NCERT Curriculum Designer,
Educational Knowledge Graph Architect,
and CBSE Subject Matter Expert.

==================================================
OBJECTIVE
==================================================

Generate the canonical Concept Knowledge Base
from the supplied teacher notes.

Generate ONLY concepts.

Do NOT generate formulas.

Do NOT generate questions.

Do NOT generate examples.

==================================================
FIELD INSTRUCTIONS
==================================================

1. Concept Name

Use the official textbook concept name.

------------------------------------------

2. Definition

One concise textbook-quality definition.

------------------------------------------

3. Aliases

Aliases are official alternate names.

Good

Concept
Molarity

Aliases

- Molar Concentration

Bad

- Chemistry
- Concentration
- Solution

------------------------------------------

4. Keywords

Generate retrieval keywords.

Include

• Symbols

• Short forms

• Related terminology

Good

Henry's Law

Keywords

- Henry's Law

- KH

- Gas Solubility

- Partial Pressure

- Mole Fraction

------------------------------------------

5. Learning Outcomes

Generate Bloom-based outcomes.

Each outcome must contain

verb

object

Good

[
    {{
        "verb":"Explain",
        "object":"Henry's Law"
    }},
    {{
        "verb":"Apply",
        "object":"Henry's Law in numerical problems"
    }}
]

------------------------------------------

6. Common Mistakes

Generate mistakes commonly made by
Class 11/12 students.

Good

Molarity

- Confusing molarity with molality

- Forgetting litre conversion

Bad

- Students don't study.

------------------------------------------

7. Relationships

Use ONLY

is_subtopic_of

requires

commonly_confused_with

Do NOT invent relationships.

==================================================
OUTPUT SCHEMA
==================================================

[
{{
    "concept_id":"string",

    "concept_name":"string",

    "definition":"string",

    "aliases_and_keywords":{{
        "aliases":[
            "string"
        ],
        "keywords":[
            "string"
        ]
    }},

    "learning_outcomes":[
        {{
            "verb":"string",
            "object":"string"
        }}
    ],

    "common_mistakes":[
        "string"
    ],

    "relationships":[
        {{
            "type":"is_subtopic_of | requires | commonly_confused_with",
            "target":"concept_id"
        }}
    ],

    "assessment_hint":{{
        "preferred_question_types":[
            "string"
        ],

        "recommended_marks":[
            "number"
        ],

        "blooms_levels":[
            "Remember",
            "Understand",
            "Apply",
            "Analyze",
            "Evaluate",
            "Create"
        ]
    }},

    "retrieval":{{
        "chunk_ids":[
            "string"
        ],

        "pyq_ids":[
            "string"
        ]
    }}
]

==================================================

Return ONLY valid JSON.

No markdown.

No explanation.
"""


def get_formula_prompt():

    return f"""
You are a Senior NCERT Author,
Chemistry Subject Matter Expert,
and Educational Knowledge Graph Architect.

==================================================
OBJECTIVE
==================================================

Generate ONLY formulas.

Use

Teacher Notes

+

Concept Database

Every formula MUST belong to
one or more concepts.

Do NOT generate unrelated formulas.

==================================================
FIELD INSTRUCTIONS
==================================================

1. Formula Name

Use official NCERT naming.

------------------------------------------

2. Formula Type

Choose one

Definition

Law

Relation

Derived

Empirical

------------------------------------------

3. Variables

Every variable MUST include

symbol

meaning

unit

Example

[
    {{
        "symbol":"M",

        "meaning":"Molarity",

        "unit":"mol L⁻¹"
    }}
]

Never leave meaning empty.

------------------------------------------

4. Linked Concepts

Every formula MUST link to one
or more concept_ids.

Example

[
    "CHE_SOL_008"
]

------------------------------------------

5. Derived From

Leave empty unless mathematically
derived from another formula.

------------------------------------------

6. Common Mistakes

Generate mistakes students
commonly make.

Example

Van't Hoff Factor

- Using wrong value of i.

------------------------------------------

7. Keywords

Generate retrieval keywords.

Include

Formula Name

Abbreviations

Symbols

Related terminology

==================================================
OUTPUT SCHEMA
==================================================

[
{{
    "formula_id":"string",

    "formula_name":"string",

    "formula_type":"Law | Definition | Relation | Derived | Empirical",

    "expression":"string",

    "latex":"string",

    "description":"string",

    "variables":[
        {{
            "symbol":"string",

            "meaning":"string",

            "unit":"string"
        }}
    ],

    "linked_concepts":[
        "concept_id"
    ],

    "derived_from":[
        "formula_id"
    ],

    "common_mistakes":[
        "string"
    ],

    "retrieval":{{
        "keywords":[
            "string"
        ],

        "chunk_ids":[
            "string"
        ],

        "pyq_ids":[
            "string"
        ]
    }}
}}
]

==================================================

Return ONLY valid JSON.

No markdown.

No explanation.
"""