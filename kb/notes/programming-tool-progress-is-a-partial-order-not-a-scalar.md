---
description: "Fixes the outcome-per-effort side of tool progress: forward means no worse accepted outcomes at no more total human effort, counting configuration, review, recovery, and repair — a partial order entailing no percentage or hours-saved scalar"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Programming-tool progress is a partial order on accepted outcomes per human effort, not a scalar

Claims that a programming tool has advanced usually reach for a number: a percentage of the work automated, a share of the code written by a model, hours saved per developer. Each number presupposes a scale that the underlying comparison does not supply. The comparison supplies an order, and that order is partial.

## The comparison frame

Fix three things before comparing two states of one programming tool: the **task class** being attempted, the **acceptance threshold** that decides which outputs count as done, and the boundary over which **human effort** is counted. Against that frame, a change is *forward* when it produces no worse accepted outcomes, requires no more total human programming effort, and strictly improves at least one of those two terms. The breadth form is the same relation read the other way: the accepted task set grows while the human-effort budget is held fixed. Throughout, *effort* means that total across every stage, which the next section spells out.

Holding the frame fixed is what makes the comparison mean anything, the same discipline that makes an autonomy comparison meaningful [since computationally directed self-improvement is a fixed-boundary reallocation](./computationally-directed-self-improvement-is-a-reallocation.md). Let the task class, the threshold, or the effort boundary move during the comparison and a forward step can be manufactured in either direction.

## Total effort has to include the work the tool displaces

"Total human programming effort" means every stage a person must still supply to reach an accepted result: specifying and configuring, reviewing what the tool produced, recovering when it went wrong, and repairing what it left behind. Leave any of those stages outside the count and displaced work looks like saved work.

The failure is not hypothetical. Cheap generation lowers production cost without lowering verification cost, so [text volume stops evidencing author effort and can instead warn that the reviewer inherits unperformed checking](./cheap-generation-breaks-text-volume-as-an-effort-signal.md). A tool that emits more output per prompt and moves the checking to a person has moved effort, not removed it. Whether that move is nonetheless forward depends on the relative size of the two effects — which is precisely what a full effort count measures and a partial one hides. The displaced stages are also the ones least likely to shrink on their own, [since the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md): review and repair sit where verification is expensive, so they are the residue a further tool improvement has the hardest time removing.

## Two independent sources of partiality

**Outcomes are not a single quantity.** Within one task class, a change can improve results on some tasks and worsen them on others. Comparing those outcome profiles componentwise leaves pairs where neither dominates, and collapsing the profile into one number requires a weighting across tasks that the tool comparison does not contain.

**Outcomes, effort, and warrant trade against each other.** A change that cuts review effort by weakening the checking that decides acceptance has bought effort with warrant. Warrant belongs in the comparison as its own term, because the acceptance threshold is applied by some checking process whose reliability can fall while the threshold's wording stays the same, and [warranted autonomy extends only as far as an oracle can assess the candidates](./warranted-autonomy-is-bounded-by-oracle-domain.md).

Ranking either kind of trade needs a weighting. A weighting is a declared objective rather than a fact about the tool, and [an improvement attribution stays elliptical until its objective is named](./self-improvement-is-relative-to-a-declared-objective.md). Two operators with different objectives can rank the same trade differently without either being wrong about the tool. So no unique scalar follows from the order. A percentage automated or an hours-saved figure can be reported as a chosen summary under a stated weighting; it cannot be read off the comparison itself.

## What the partial order still does

**Bounded mechanisms count.** A change whose mechanism can remove only one narrow responsibility — a formatter, a validator, a codified check — is forward under this order when it removes that responsibility and adds no effort elsewhere. The order asks whether this step improved a term, not whether the mechanism behind the step can keep going.

**Forward steps do not compose into convergence.** Each mechanism takes what lies inside its reach and stops, and [stacking bounded automation mechanisms does not approach an empty human cut set asymptotically](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md), because the decisions each mechanism leaves behind are the ones no similar mechanism will take. A chain of forward steps can therefore terminate well short of no human effort. Reading the order as a trajectory toward zero adds an assumption the order does not carry.

## Relation to per-judgment measures

[Measuring improvements per human judgment rather than per human hour](./increasing-computational-autonomy-relocates-human-effort.md) answers the same worry from the allocation side: where the backlog is elastic, falling hours is the wrong signal, because attention freed from routine work moves to harder work instead of being banked. This note fixes the other side.

The two readings hold different things fixed. The allocation reading holds the pathway's function list fixed and watches which actor supplies each decision. The order here holds the task class and acceptance threshold fixed and watches accepted outcomes against total effort. They agree in refusing total hours as the headline signal, and they are complementary rather than redundant: a tool can move a decision to a computational actor without improving accepted outcomes per unit of effort, and it can improve outcomes per unit of effort with the allocation unchanged.

## Scope

- The order compares two states of one tool on one named task class. Comparing different tools, or the same tool across task classes, needs commensurable task classes and effort counts, and inherits the difficulty that [measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md).
- Quality and warrant losses are recorded as losses, not netted against effort savings. Netting is what lets a change that merely bought effort with something else appear forward. A netted summary can be computed after a weighting is declared; the order does not perform that netting on its own.
- Effort has to be *compared*, not necessarily measured on a cardinal scale. The relation needs only "no more than", which ordinal or bounded-interval evidence can sometimes supply. Where even that comparison is unavailable, the two states are incomparable, not equal.
- A moving acceptance threshold voids the comparison. When a tool makes cheap output plentiful and people start accepting results they would previously have rejected, the apparent improvement is a relaxation of the threshold, and the frame has to be restated before the order applies.
- The order rates a step, not the mechanism behind it. Two equally forward changes can differ entirely in whether their mechanism has further reach, which is why an automation envelope has to be assessed separately.

## Open Questions

- Whether total human effort can be recovered from repository and session history well enough to test forwardness retrospectively, given that configuration, review, recovery, and repair are recorded in different places or not recorded at all.
- Whether warrant is better treated as a third term in the order or as a condition on the acceptance threshold. As a term it admits explicit warrant-for-effort trades; as a condition it forbids them, at the cost of making every warrant change void the frame.
- Whether any weighting of outcomes against effort can be defended beyond stipulation for a particular operator, or whether the choice of summary scalar is irreducibly a matter of declared objective.

---

Relevant Notes:

- [Computationally directed self-improvement is a fixed-boundary reallocation ending in contraction](./computationally-directed-self-improvement-is-a-reallocation.md) — grounds: the fixed-frame discipline this order borrows, and the prior refusal to sum a per-function profile into a percentage
- [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](./increasing-computational-autonomy-relocates-human-effort.md) — contrasts: the allocation-side per-judgment measure that serves the same purpose while holding the function list rather than the task class fixed
- [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](./warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md) — grounds: why a chain of bounded forward steps need not converge, and why leverage can rise while the remaining decisions get harder
- [Measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — extends: the cross-system commensurability problem that bounds this order to states of one tool
- [Self-improvement is relative to a declared objective](./self-improvement-is-relative-to-a-declared-objective.md) — grounds: the declared objective any weighting of outcomes against effort requires
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: why warrant is a term that can be traded away rather than a property acceptance guarantees
- [Cheap generation breaks text volume as an effort signal](./cheap-generation-breaks-text-volume-as-an-effort-signal.md) — mechanism: how lowered production cost with unchanged verification cost displaces effort onto the reviewer
- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: why review and repair are the effort stages least likely to shrink, making a partial effort count systematically flattering
