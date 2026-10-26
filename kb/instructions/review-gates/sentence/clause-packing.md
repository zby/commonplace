---
gate_id: sentence/clause-packing
name: Clause packing
description: 'A sentence chains enough subordinate clauses, qualifiers, or contrasts that its overall relation becomes hard to retain.'
type: types/review-gate.md
lens: sentence
watches: [body]
staleness: changed
---

## Failure mode

A sentence chains too many subordinate clauses, qualifiers, or contrastive phrases. Each clause may be clear on its own, but the sentence as a whole requires the reader to hold too many pieces in working memory.

## Test

For each sentence longer than roughly 40 words, count the distinct clauses or ideas. If the sentence packs more than 2-3 independent concepts and could be split or shortened without losing meaning, it is overloaded. Report all instances.

Watch especially for sentences that grew during revision — a fix for one problem (ambiguity, missing context) can bloat a sentence by adding qualifiers that belong in a separate sentence or don't need to be stated at all.

Also check distance, not only count. A sentence under the word threshold still overloads the reader when a long clause or list separates its subject from its verb or its verb from its object, or when two long unresolved dependencies are open at once. One long dependency on its own is tolerable; do not flag it. For a finding of either kind, prefer a reordering that keeps every word and relation: move the interrupting material before the subject or after the object, or put the shorter phrase first after a verb or noun. Recommend a split only when no reordering reads naturally.

## Example (fail)

"Storing a trace is fine — the mistake is letting a session runtime decide that stored history should automatically become the next call's context instead of letting a deliberate selection step choose what the next call should see."

Five clauses. The contrastive "instead of letting..." restates the point the prior clause already implies.

## Example (pass)

"Storing a trace is fine — the mistake is letting stored history automatically become the next call's context."

Same meaning, two clauses.

---

Relevant Notes:

- [Dependency locality supports ordering heuristics, not a reading-cost rule](../../../theory/dependency-locality-supports-ordering-heuristics-not-a-reading-cost.md) — rests-on: the ordering heuristics this gate recommends, and the reason it checks peak load rather than sentence length or a dependency-length metric
