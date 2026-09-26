# Tag review workshop

**Opened:** 2026-09-26, the day after ADR 089 and 090 landed.

**Posed by:** the operator: "we still should make a review of the current tags".

**State:** findings recorded; actions await the operator's selection.

## What was reviewed

The 22 heads in `kb/tags/` against the head contract in `kb/tags/COLLECTION.md`
and `kb/types/tag-readme.md`: does the opening say what the tag gathers in a
reader's words, is the defining note named, is the boundary against the
confusable neighbour stated, do the members fit, what is stale, and would the
tag be better split, merged, or retired. Two independent scouts each read
eleven heads and about ten members per head; their reports are
[heads-a-to-f.md](./heads-a-to-f.md) and [heads-f-to-t.md](./heads-f-to-t.md).

## Mechanical facts (2026-09-26)

| tag | members | outside notes | head bytes | complete | member links | linked heads |
|---|---|---|---|---|---|---|
| agent-memory | 40 | 5 | 5875 | | 20 | 3 |
| architecture | 12 | 2 | 3518 | | 5 | 0 |
| artifact-analysis | 30 | 1 | 8094 | yes | 30 | 1 |
| computational-model | 92 | 9 | 8191 | | 23 | 6 |
| constraining | 35 | 1 | 3740 | | 14 | 2 |
| context-engineering | 69 | 8 | 2908 | | 8 | 3 |
| deploy-time-learning | 12 | 0 | 4328 | yes | 12 | 4 |
| discovery | 18 | 0 | 5931 | yes | 19 | 1 |
| document-system | 31 | 2 | 5651 | | 13 | 3 |
| evaluation | 35 | 4 | 1614 | | 4 | 0 |
| failure-modes | 9 | 0 | 2008 | | 5 | 2 |
| foundations | 118 | 4 | 6308 | | 17 | 1 |
| kb-maintenance | 50 | 19 | 5058 | | 15 | 3 |
| learning-theory | 136 | 1 | 5529 | yes | 18 | 9 |
| links | 11 | 1 | 5260 | | 8 | 1 |
| llm-reliability | 31 | 0 | 7932 | | 18 | 4 |
| methodology | 6 | 0 | 2774 | yes | 6 | 3 |
| observability | 11 | 3 | 3340 | | 7 | 5 |
| self-improving-systems | 124 | 7 | 8181 | | 34 | 4 |
| tool-loop | 22 | 9 | 7631 | | 13 | 0 |
| trace-learning | 105 | 105 | 2767 | | 6 | 3 |
| type-system | 15 | 3 | 3821 | | 11 | 3 |

Heavy overlaps (share of the smaller tag's members): computational-model ⊃
tool-loop 86%; foundations ∩ self-improving-systems 81 members (69% of
foundations); agent-memory ∩ context-engineering 70%; kb-maintenance ∩
observability 73%; foundations ⊃ methodology 100%. Children of
learning-theory (constraining, discovery, deploy-time-learning) overlap it by
design.

Untagged participating artifacts: 89 ADRs (by type convention), 55
agent-memory-systems reviews without a trace-learning loop (by type rule), 36
agentic-systems reviews, 35 instruction files, 23 notes, 21 reference pages.

## Closure

Close when the operator's selected actions are applied and validated, and any
resulting tag additions, splits, or retirements are recorded in the
implementing commits. The reports are consumed, not retained.
