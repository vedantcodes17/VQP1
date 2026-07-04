# Chapter-KB Pipeline Comparison


## Execution time
- Teacher-Note Approach: 2026-07-03 06:04:38 -> 2026-07-04 00:01:32  (~64614s, 29 concepts, full chapter run)
- New Approach: 2026-07-04 08:36:14 -> 2026-07-04 08:40:25  (~251s, 4 concepts, LIMIT_CHUNKS=5 smoke test)
- NOTE: these two runs are not apples-to-apples -- the teacher-note run processed the full chapter (~530 chunks) while the new-approach run was capped at 5 chunks for testing. Compare per-concept/per-chunk rate, not raw totals.


## Field-by-field comparison


| Section | Schema Field | Teacher-Note Approach | New Approach | Confidence/Accuracy |
|---|---|---|---|---|
| top_level | chapter | 100.0% populated (1 records) | 100.0% populated (1 records) | High - Complete coverage |
| top_level | chapter_id | N/A (field absent) | 100.0% populated (1 records) | Low - Field absent |
| top_level | subject | N/A (field absent) | 100.0% populated (1 records) | Low - Field absent |
| top_level | grade | N/A (field absent) | 100.0% populated (1 records) | Low - Field absent |
| concept_tree | concept_id | 100.0% populated (29 records) | 100.0% populated (4 records) | High - Complete coverage |
| concept_tree | concept_name | 100.0% populated (29 records) | 100.0% populated (4 records) | High - Complete coverage |
| concept_tree | parent_concept | 34.5% populated (29 records) | 0.0% populated (4 records) | Low - Low populated |
| concept_tree | definition | 100.0% populated (29 records) | 100.0% populated (4 records) | High - Complete coverage |
| concept_tree | aliases | 13.8% populated (29 records) | 50.0% populated (4 records) | Medium - Moderate populated |
| concept_tree | formulae | 20.7% populated (29 records) | 25.0% populated (4 records) | Medium - Moderate populated |
| concept_tree | examples | 100.0% populated (29 records) | 75.0% populated (4 records) | High - Complete coverage |
| concept_tree | related_concepts | 86.2% populated (29 records) | 100.0% populated (4 records) | High - Complete coverage |
| concept_tree | prerequisites | 27.6% populated (29 records) | 0.0% populated (4 records) | Low - Field absent |
| concept_tree | learning_outcomes | 100.0% populated (29 records) | 100.0% populated (4 records) | High - Complete coverage |
| concept_tree | assessment | 100.0% populated (29 records) | 100.0% populated (4 records) | High - Complete coverage |
| concept_tree | retrieval.keywords | 100.0% populated (29 records) | 100.0% populated (4 records) | High - Complete coverage |
| concept_tree | retrieval.chunk_ids | 0.0% populated (29 records) | 100.0% populated (4 records) | Low - Field absent |
| concept_tree | source_chunks (traceability) | N/A (field absent) | 100.0% populated (4 records) | Medium - Moderate populated |
| question_bank | question_id | 100.0% populated (33 records) | 100.0% populated (2 records) | High - Complete coverage |
| question_bank | question | 100.0% populated (33 records) | 100.0% populated (2 records) | High - Complete coverage |
| question_bank | answer | 30.3% populated (33 records) | 50.0% populated (2 records) | Low - Low populated |
| question_bank | type | 100.0% populated (33 records) | 100.0% populated (2 records) | High - Complete coverage |
| question_bank | linked_concepts | 100.0% populated (33 records) | 100.0% populated (2 records) | High - Complete coverage |
| question_bank | source_chunk (traceability) | 100.0% populated (33 records) | 100.0% populated (2 records) | High - Complete coverage |
| relationships | source_concept | 100.0% populated (14 records) | 100.0% populated (3 records) | High - Complete coverage |
| relationships | target_concept | 100.0% populated (14 records) | 100.0% populated (3 records) | High - Complete coverage |
| relationships | relationship | 100.0% populated (14 records) | 100.0% populated (3 records) | High - Complete coverage |


## Overall verdict (LLM)


The Teacher-Note Approach is more usable overall due to its comprehensive and consistent population of fields, providing a richer dataset for analysis.