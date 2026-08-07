---
description: "Explains why an instruction generated from model weights can still add KB value: testing selects a procedure under a criterion and retention makes that choice reusable."
type: kb/types/note.md
traits: [title-as-claim]
tags: [context-engineering]
---

# A retained instruction preserves what testing selected

A model may generate every candidate instruction from knowledge already in its weights. The test still establishes something the weights alone do not: which candidate met a stated criterion on the tested cases. Retaining the winner commits that evaluated choice for reuse. The instruction's value need not be new domain knowledge; it can be the selected procedure.

Reuse avoids repeating candidate generation and evaluation. Why the selected procedure works, how broadly it transfers, and whether additional inference effort could rediscover it remain empirical questions.

---

Relevant Notes:

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: testing and retention supply two distinct functions in the selection claim
- [Commitment, not derivation, creates new ground truth](./commitment-not-derivation-creates-new-ground-truth.md) — mechanism: accepting one underdetermined candidate commits a choice that its precursor does not determine
- [LLM recompute cost inverts the store-vs-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — extends: reusing the selected procedure avoids repeating an expensive generation-and-evaluation step
