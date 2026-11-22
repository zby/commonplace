---
description: "Costly search reaches only a few candidate changes, so selection-based learning needs only a comparison among the alternatives at hand; a value function is one convenient way to supply it, not a requirement"
type: types/note.md
traits: [title-as-claim]
tags: [self-improving-systems, learning-theory, improvement-loop]
---

# Selection-based learning needs only a local comparison

People often picture selection as choosing the best state from all possible states, guided by a global value function that assigns every state a number and orders every pair. In [selection-based learning](./definitions/selection-based-learning.md), search is costly and reaches only a few candidate changes at a time. Evaluation therefore never has to rank the whole space of possible systems; it needs only to compare the alternatives at hand—typically one proposed change against leaving the system as it is, or a small batch of candidates against each other and the current state.

A global value function—a scalar loss, reward, or scoring formula—is a convenient way to supply that comparison whenever one formula captures the work. Giving every candidate a number turns any local comparison into checking which number is higher, which is often the cheapest and cleanest route when an adequate formula exists. Selection-based learning works directly with such a function, but it does not require one.

When gains and losses fall on different tasks and no single scalar weighting is fixed, a local comparison can still decide among the candidates reached. A [robust comparison](./necessary-preference-can-guide-improvement-without-a-global-measure.md) accepts a change when every weighting compatible with the purpose favors it, and leaves contested trade-offs open; where a comparison stays open, [reversibility can favor a bounded trial](./reversibility-can-favor-a-change-by-limiting-future-loss.md) by limiting future loss until later evidence arrives. Direct updates such as gradient steps look different because they compute each update directly from an explicit numerical error or reward signal, which makes a scalar objective seem necessary for learning in general even though selection among the candidates at hand does not require one.

Every selection step does imply a binary gate on the proposed change—adopt or reject—but that gate is a decision predicate on transitions, not a scalar value function on states. Calling any yes/no gate a binary value function collapses the distinction between making a decision and scoring every state on one common scale. Suppose the judge prefers B to A but leaves C incomparable with both. Could it reproduce those judgments by adopting a change exactly when the destination has a higher score? B would have to score higher than A. Yet C would have to tie with A, or the score would favor one over the other. For the same reason, C would have to tie with B. No assignment of scores satisfies all three comparisons.

## Scope

- A syntax check can decide whether to admit a candidate for later use. Passing it shows that the candidate meets the admission criterion, not that admitting it improved the system. Choosing between working versions instead calls for a local comparison.
- A local comparison does not by itself prevent cycles across successive selections: an evaluator that accepts a change and later accepts its reversal on the same evidence will not converge. Consistency across decisions (no cycles, and transitivity where the comparison decides) is a separate requirement on the evaluator.
- Costly search narrows both what evaluation must compare and what learning can find: [evaluation cannot select a candidate that search never reaches](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md).
- This claim fixes what selection-based learning requires of evaluation. It does not establish that any particular evaluator—such as a fixed-weight language model—can perform reliable local comparisons without a single score.

---

Relevant Notes:

- [Selection-based learning](./definitions/selection-based-learning.md) — defined-in: the learning process whose evaluation requirement this note bounds
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: why search reaches only a limited set of candidates and evaluation decides only among them
- [Necessary preference can guide improvement without a global measure](./necessary-preference-can-guide-improvement-without-a-global-measure.md) — mechanism: how a comparison across compatible measures decides without collapsing trade-offs into one score
- [Reversibility can favor a change by limiting future loss](./reversibility-can-favor-a-change-by-limiting-future-loss.md) — extends: how bounded trials handle candidates whose local comparison stays open
