# Question Paper Comparison (Teacher-Note vs Approach2)


| Metric | Teacher-Note Paper | Approach2 Paper | Confidence/Accuracy |
|---|---|---|---|
| Total questions | 14 | 14 | High - both have same number |
| Total marks | 30 | 30 | High - both have same total marks |
| Source KB concept pool size | 28 | 4 | Low - teacher-note has larger KB pool size |
| Distinct concepts tested in paper | 14 | 4 | Medium - teacher-note tests more distinct concepts |
| Duplicate/near-duplicate questions | 0 | 1 | High - teacher-note has no duplicates |
| Questions flagged by validator | 2 | 14 | Low - teacher-note has fewer flagged questions |
| Pipeline execution time | 316.7s | 437.6s | Medium - teacher-note is faster to execute |


*Caveat: the Approach2 KB currently has only 4 concepts vs 28 for the Teacher-Note KB (approach2.py was smoke-tested on 5 chunks only) -- concept-reuse related metrics reflect that data-scale gap, not a pipeline difference.*


## Overall verdict (LLM)


The Teacher-Note paper is better as it tests a wider range of distinct concepts, avoids duplicates, and executes more efficiently. The questions are also more varied in difficulty levels.