---
type: kb/types/instruction.md
description: Workshop review gate for checking clause packing during review-revise experiments
gate_id: sentence/clause-packing
name: Clause packing
lens: sentence
watches: [body]
staleness: changed
---

## Failure mode

A sentence chains too many subordinate clauses, qualifiers, or contrastive phrases. Each clause may be clear on its own, but the sentence as a whole requires the reader to hold too many pieces in working memory.

## Test

For each sentence longer than roughly 40 words, count the distinct clauses or ideas. If the sentence packs more than 2-3 independent concepts and could be split or shortened without losing meaning, it is overloaded. Report all instances.

Watch especially for sentences that grew during revision — a fix for one problem (ambiguity, missing context) can bloat a sentence by adding qualifiers that belong in a separate sentence or don't need to be stated at all.

## Example (fail)

"Storing a trace is fine — the mistake is letting a session runtime decide that stored history should automatically become the next call's context instead of letting a deliberate selection step choose what the next call should see."

Five clauses. The contrastive "instead of letting..." restates the point the prior clause already implies.

## Example (pass)

"Storing a trace is fine — the mistake is letting stored history automatically become the next call's context."

Same meaning, two clauses.
