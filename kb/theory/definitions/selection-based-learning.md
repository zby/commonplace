---
description: "Definition — selection-based learning is learning in which each change to what a system retains is proposed, evaluated on whether it makes that work better, and can be rejected; it contrasts with direct updates"
type: types/definition.md
tags: [self-improving-systems, learning-theory, improvement-loop]
---

# Selection-based learning

<!-- Maintenance: when changing this definition, please apply the checks in
[selection-based-learning-checks.md](./selection-based-learning-checks.md).
This term was named "deliberative learning" until 2026-11-22 and
"judgment-governed self-improvement" on that day. -->

**Selection-based learning** is learning in which each change is selected:

> A change to what the system retains for its later work is proposed,
> evaluated on whether it makes that work better, and can be rejected.

[AlphaGo Zero](https://www.nature.com/articles/nature24270) illustrates the boundary. Each newly trained network played the current best one and replaced it only if it won by a margin of 55%. Its successor, [AlphaZero](../../sources/alphazero-chess-shogi-self-play.ingest.md), dropped that evaluation gate and updated a single network continually by gradient descent—moving from network-level selection to direct updates alone.

That contrast divides learning in [Simon's sense](../learning-is-not-only-about-generality.md)—changes that alter what a system can do on later occasions, rather than one-off plans for the current task—into two modes. In a **direct update**, evidence determines the change directly and nothing is proposed or rejected. In **selection-based learning**, a **selection-based learner** operates through a [proposal-selection improvement loop](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md) with two requirements:

- **Retained change.** The change alters something the learner keeps and draws on in later work. Where that retained content lives does not matter: a handbook, code, a team's working habits, and a model checkpoint all qualify, so a readable store is not required.
- **Reject-capable evaluation.** Evaluation is causally distinct from proposing, though it need not be a separate stage or actor and may be automatic. Its verdict decides whether the change is made—or undone if already made—and rejection is its own event rather than the arrival of the next candidate.

Like reinforcement learning, the term names a process rather than a successful outcome. Whether a selected change actually improved the system is a separate question, answered by comparing the system with and without it.

## Scope

- **Direct updates (outside).** Gradient steps under a fixed loss and rules that write directly from inputs (such as raising an article's rank on each click) try no candidate and reject nothing.
- **Triggers and automatic storage (outside).** A rule written automatically on a count trigger and a logger that saves every trace evaluate nothing. Either enters scope only when an evaluation step checks the candidate and can reject it.
- **One fixed measure (inside).** Keeping a patch that passes a validator, deploying the checkpoint with the best validation score, or keeping a mutation in evolutionary search all evaluate a candidate and can reject it. The gradient steps that produced each checkpoint stay outside.
- **Several measures (inside).** A team or judge that weighs a score alongside other considerations and can reject a change even when the score rises.

## System boundary and class of changes

Every claim of selection-based learning names the **system** that changes and the **class of changes** it covers. A wiki that imports pages automatically and lets editors delete wrong ones is outside for imports and inside for deletions.

Who performs the selection does not affect membership, but it separates three levels. Take a deployed model whose checkpoint is picked by a validation score:

1. **Learning.** Only the deployed model sits inside the boundary; it changes which checkpoint it uses, learning by selection that others perform on it.
2. **Self-improvement by selection.** The selection script sits inside the boundary too; the model and script together form a [self-improving system](./self-improving-system.md).
3. **Double-loop.** The engineers who can revise the validation score also sit inside; the combined system can change what it selects by and is [double-loop](./single-loop-and-double-loop-learning.md).

Proposals may come from outside the boundary; selection is the step that must sit inside for self-improvement by selection.

## Misuse Cases

- Citing the term as evidence that the system improved or corrects itself.
- Restricting the term to readable stores or to prose.
- Applying the term to a system because it reasons carefully about its work; it applies only to how retained changes are decided.
- Omitting the system or the class of changes.

---

Relevant Notes:

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: the anatomy of the loop and its boundary cases
- [Selection-based learning needs only a local comparison](../selection-based-learning-needs-only-a-local-comparison.md) — extends: why evaluation needs only a local comparison among reached candidates, with or without a global value function
- [Necessary preference can guide improvement without a global measure](../necessary-preference-can-guide-improvement-without-a-global-measure.md) — grounds: the comparison across compatible measures, and what a claim of improvement asserts
- [Learning is not only about generality](../learning-is-not-only-about-generality.md) — grounds: the sense of learning the term uses
- [Self-improving system](./self-improving-system.md) — defined-in: the second step of the ladder, where selection lies inside the declared boundary
- [Single-loop and double-loop learning](./single-loop-and-double-loop-learning.md) — defined-in: the third step, where the learner can revise the criterion that decides its changes
