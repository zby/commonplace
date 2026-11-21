---
description: "Curated head for the deliberative-learning tag — learning by proposed, judged, rejectable changes to a system's own readable store: the definition, the judgment that decides a change, the proof-governed precedent, and the Bitter Lesson"
type: types/tag-readme.md
complete: true
---

# Deliberative learning

[Deliberative learning](../theory/definitions/deliberative-learning.md) is learning in which a system changes its own legible, addressable store, and each change is proposed, judged and can be rejected. Assign this tag to work on that process: the store and the decision that define it, the judgment that decides a change when no single criterion settles it, the single-loop and double-loop kinds, correction from later evidence, the verdict that one change was learned, or the claim that a fully automated deliberative learner is a machine learning paradigm. Work on a system that only retains readable artifacts is insufficient. The subject must be how a change to the store is decided, how that decision is judged later, or whether an automated deliberative loop scales as a learning paradigm. Tagging an analysis does not certify that the analyzed system learns.

The draft article [Deliberative Learning: Judgment in Place of a Value Function](../articles/deliberative-learning-judgment-in-place-of-a-value-function.md) argues the thesis for outside readers. Commonplace's bet is that a language model with fixed weights can make the judgment with no person judging. No end-to-end test of the bet has been run.

Three neighbors are close. [Improvement-loop](./improvement-loop-README.md) covers proposal and selection whatever form the retained result takes; this tag covers the case where the result is a readable store, and the judgment itself. [Continual-learning](./continual-learning-README.md) covers learning outside model weights whether or not a decision admits each change. [Theory-builder](./theory-builder-README.md) covers stated theories that are criticized for what they say; how the two definitions relate is not settled. A note that meets two conditions can carry both tags. This tag is a child of [self-improving-systems](./self-improving-systems-README.md).

## Definition

- [Deliberative learning](../theory/definitions/deliberative-learning.md) — the two conditions, what a claim names, the single-loop and double-loop kinds, correction and displacement, and "learned" as a separate verdict on one change

## The judgment that decides a change

- [On-balance judgments can guide improvement without a global measure](../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md) — what the judgment asserts when gains and losses fall on different tasks, and when the verdict stays open
- [An objection can show where to split an on-balance judgment](../theory/an-objection-can-show-where-to-split-an-on-balance-judgment.md) — how to examine a disputed judgment
- [Reversibility can favor a change by limiting future loss](../theory/reversibility-can-favor-a-change-by-limiting-future-loss.md) — why a change that can be corrected may be kept on weaker evidence
- [Revising an improvement objective is licensed from outside it](../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md) — the limit on double-loop revision: a learner can revise its criterion, and the objective the criterion serves stays fixed

## Precedent and the scaling argument

- [Gödel machines are a proof-governed case of reflective self-modification](../theory/goedel-machines-are-a-proof-governed-case-of-self-modification.md) — the case where a proof decides each rewrite; Commonplace replaces the proof with an on-balance judgment
- [The Bitter Lesson selects production methods, not representational forms](../theory/the-bitter-lesson-selects-production-methods-not-representational.md) — why a store of prose and code is compatible with the lesson when computation produces its contents
- [A bootstrap fits the Bitter Lesson only if learning outgrows it](../theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) — the condition a hand-written starting state has to meet

## Related Tags

- [self-improving-systems](./self-improving-systems-README.md) — the parent: a deliberative learner is a self-improving system that works by proposal and selection over a legible, addressable store
- [improvement-loop](./improvement-loop-README.md) — search, evaluation and retention in general, including false-positive acceptance
- [continual-learning](./continual-learning-README.md) — learning that persists outside model weights, and the unit of learning as the deployed system
- [reflection](./reflection-README.md) — when a learner represents its own criteria in the store, double-loop revision runs through reflection
- [evaluation](./evaluation-README.md) — the wider work on judging whether a change helped
- [theory-builder](./theory-builder-README.md) — the earlier definition, scoped to stated theories criticized for what they say
