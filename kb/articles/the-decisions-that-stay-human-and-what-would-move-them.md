---
description: "Why hard programming decisions stay with people: decisions transfer with warrant where premises, settled criteria, and defeating checks exist, so the residue is enriched for the opposite; what would move each class, and why closure is not quality"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md
  - kb/notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md
  - kb/notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md
  - kb/notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md
---

# The decisions that stay human, and what would move them

> **Draft.** This article is circulating for comments; its claims, structure, and central thesis may still change. Counterexamples, rival mechanisms, and disputed experimental controls are welcome through [the repository's issue tracker](https://github.com/zby/commonplace/issues).

Automating parts of software work does not leave a random residue behind. A
decision moves out of human hands most easily when the automatic process has the
premises it needs, a criterion settled enough to apply, and a check that can
reject a plausible but harmful candidate. If those are the conditions that make
transfer possible with warrant, then the decisions that stay human are enriched
for the opposite properties: missing premises, unsettled criteria, and no
independent check strong enough to defeat a wrong answer.

This article develops that selection argument, sets out what would have to grow
for each class of residual decision to move, and separates the argument from two
things it is easily confused with — whether a path is computationally closed,
and whether the system doing the work is any good.

## Why difficult decisions remain human

Take the boundary question directly: why has a given hard modification decision
not yet moved out of the human part of the system? Five answers cover the cases,
and each names a different thing that would have to grow before the decision
could move.

| Why the decision remains human | What would have to grow |
|---|---|
| A required premise is unavailable | Representation, retrieval, or acquisition |
| The objective, commitment, criterion, or authority does not settle acceptance | Methodological settlement or a represented grant of authority |
| No sufficiently independent check can defeat the candidate | Verification, decorrelated criticism, delayed exposure, or accepted error tolerance |
| The decision arises after the automatic path stops | Persistent state, scheduling, and later reactivation |
| Transfer is possible but too expensive | No new capacity; the transfer is currently uneconomic |

This is a conditional selection argument, not yet a prevalence result. Real
systems may automate whatever is cheap rather than what is warrantable. A direct
test needs before-and-after histories under a stable boundary, objective,
horizon, and workload.

The bearer and transfer questions meet at open-ended modification but do not
collapse into one. The [bearer
question](./a-research-program-for-learning-software-factories.md) asks
whether the composite can sustain coherent, theory-guided search and recovery. The transfer question asks whether
the required premises, authority, correction, and continuity are sufficiently
inside the declared boundary for the decision to move with warrant.

## Closure is not evaluator quality

Computational closure should be stated only for a declared task selection,
objective, boundary, permitted exogenous inputs, horizon, resources, and
coverage rule. Conditional on those declarations, a path is structurally closed
when every required decision and transition occurs inside the automatic system.

That says where decisions happen, not whether they are good. A no-op loop, a bad
objective, or a captured evaluator can be computationally closed. A warranted,
non-degenerate result additionally needs a capability floor, consequential
revision reach, reject-capable evaluation, continuity, explicit boundary
accounting, and measured outcomes.

The remote-programmer benchmark is another coordinate. It asks whether a system
performs at least as well as a competent remote programmer given the same brief,
repository, tools, permissions, and feedback. It deliberately holds the client
fixed, so task choice, missing premises, feedback, and final acceptance remain
outside the worker. Passing it does not close those decisions.

## Where to go next

The selection argument is stated as a transferable claim in [warranted transfer
leaves people the hardest-to-warrant
decisions](../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md),
and the reason the residual classes need different mechanisms rather than one is
developed in [residue classes need different
mechanisms](../notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md).
The separation of usefulness, autonomy, warrant, and system power into
[independent progress
dimensions](../notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md)
is what keeps a closure claim from being read as a quality claim, and the
[fixed-client limit of the remote-programmer
benchmark](../notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md)
gives the benchmark argument its detail.
