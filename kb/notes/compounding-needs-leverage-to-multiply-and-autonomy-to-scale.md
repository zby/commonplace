---
description: "Accumulation grows a stock of retained improvements at constant productivity; compounding grows the pathway's own productivity — and needs leveraged changes to multiply plus warranted computational evaluation to carry the growing test load"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Compounding self-improvement needs leverage to multiply and autonomy to scale

Two growth shapes get called "improvement building on improvement", and they need to be held apart. **Accumulation** is a growing stock: retained results persist and later episodes consume them, [counted by dependence through the retained result](./accumulation-counts-dependence-through-the-retained-result.md). The stock grows while each episode's productivity stays roughly what it was. **Compounding** is growth that feeds growth: earlier improvements raise the productivity of later improvement episodes, so what grows is the pathway's capacity, not only its output. An agent that retains a lesson per failure accumulates; an agent whose retained lessons make the next failure cheaper to diagnose compounds. The claim here is that compounding has two separately necessary ingredients — a multiplier and a capacity — and neither substitutes for the other.

## Leverage is the multiplier

A change has **reflective leverage** when it improves machinery that participates in producing, evaluating, or retaining subsequent improvements. Better retrieval helps later agents diagnose later failures; a better evaluator improves later selection; a lesson about a recurring error reduces the correction later episodes need. "Reflective" here means *turned back on the improvement pathway*, deliberately weaker than [a reflective system's causally connected self-representation](./definitions/reflective-system.md): leverage is about what a change targets, not how the changed thing is represented.

Leverage narrows cumulativity by target, and the narrowing is exactly the accumulation/compounding boundary. [Cumulativity's substitution test](./accumulation-counts-dependence-through-the-retained-result.md) asks whether a later episode depends on the earlier retained result; leverage asks whether that dependence lands on a function of the improvement pathway — [search, evaluation, or operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — rather than only in task behavior. Dependence landing only in task behavior accumulates: the test passes, the stock grows, productivity does not move. Dependence landing on a pathway function is what makes the accumulated result raise later productivity. Leverage without cumulativity is not available — a change that improves how later episodes search, evaluate, or retain is by construction a retained result later improvement depends on — so leverage is a proper narrowing, and it inherits cumulativity's indexing to a declared boundary, horizon, and [objective](./self-improvement-is-relative-to-a-declared-objective.md).

Many changes hit both targets at once: a retained domain theory improves current task performance *and* the diagnosis available to the next failure. Leverage is a property a change has, not a category it belongs to.

## Autonomy is the capacity

A leveraged loop can begin fully human-governed. The feedback exists with a maintainer supplying every decision, [since the human-inclusive pathway is already a complete member and the transition is a reallocation inside it](./computationally-directed-self-improvement-is-a-reallocation.md), and each leveraged change raises what one human judgment buys. What decides whether a change contributes is not *did the system originate it without a human* but *did it improve a mechanism that participates causally in producing later improvements*.

But the loop cannot keep compounding there. Compounding raises volume: more candidates worth generating, more changes worth trying, and — non-negotiably — more testing, because every accepted change still passes evaluation and [an unevaluated acceptance becomes operative error](./false-positive-generation-is-filtered-before-retention.md). Human decision capacity does not grow with the loop. A leveraged pathway whose evaluation stays human therefore saturates at its human cut set: improvements per human judgment keep rising while the total rate flattens against fixed attention — the regime in which [computational autonomy relocates human effort rather than reducing it](./increasing-computational-autonomy-relocates-human-effort.md). Sustained compounding requires the growing load — above all the at-scale testing — to run computationally.

The capacity ingredient carries the warrant bound. Handing evaluation to an oracle outside [the domain it can assess](./warranted-autonomy-is-bounded-by-oracle-domain.md) does not extend compounding; it compounds errors at exactly the scale that made the handover attractive. The second ingredient is therefore not bare autonomy but warranted computational evaluation — and [oracle accumulation](./oracle-accumulation-improves-the-selection-environment.md) is where the two ingredients meet: a new validator is a leveraged change whose specific effect is to widen the domain over which the loop may run unattended. That is one accepted change advancing the multiplier and the capacity together.

Neither ingredient substitutes for the other. Autonomy without leverage runs faster without gaining — an unattended loop that only tunes task behavior repeats at scale. Leverage without autonomy gains until the bottleneck binds — real capability growth, visible as a rising ratio and a flat rate.

## Reflection is not a third precondition

Leverage is architecture-neutral in the same way the rest of this cluster is. A learned optimizer improves improvement machinery — the update rule is the machinery — with no self-representation anywhere in the pathway, and nothing inside it can state what was improved. What routing the leveraged machinery through a self-representation adds is that the machinery becomes **addressable**: inspectable, criticizable, selectively revisable, [as reflection buys addressability](./reflection-buys-addressability.md) argues for retention in general. Applied to the pathway's own functions, addressability is what lets a bad evaluator be found and fixed rather than only trained over or rolled back wholesale — it changes what can be done about leveraged machinery, not whether leverage exists.

## The signature separates three regimes

The two-ingredient claim predicts three observable regimes, comparable across successive episodes of one pathway without any cross-system aggregation.

- **Accumulation only.** The stock of retained results grows; each episode costs what it always cost. Real maintenance, real retention, no term that decreases.
- **Leveraged but clamped.** Earlier accepted changes make later episodes cheaper, broader, more reliable, or less dependent on human judgment — the effect shows in the *next* episode's cost, not only in the metric the change was accepted against — but total throughput plateaus at the human cut set. The ratio rises; the rate does not.
- **Compounding.** The ratio rises *and* the rate rises, because the added load lands on functions that scale — warranted computational evaluation above all.

The [tag-readme episode](../reference/commonplace-as-a-reflective-system.md) supplies a worked case of the ingredients advancing together under human governance. The corrected search recipe is a leveraged change to retrieval; the coverage-mark validator is a leveraged change to evaluation that is *also* a capacity change — a check that now runs without a human, so later candidates face it at computational scale. The maintainer chose the problem, judged the candidates, and adopted the results: the loop that accepted these changes remains clamped, and the changes themselves moved both ingredients.

## Scope

- Leverage names where a change lands, not whether the landing helps: worse machinery degrades every later episode that consumes it. Capacity shares the symmetry: unwarranted at-scale evaluation compounds errors faster. The two failure modes multiply the same way the two ingredients do.
- The ceiling argument's premise is that human decision capacity is fixed within the frame. Adding maintainers moves the ceiling without removing it; the bound is the cut set's size, not its current occupants.
- Both readings are over named episodes under a declared boundary and horizon, not quantities asserted of a system. Aggregating a leverage fraction across episodes inherits the commensurability difficulty that blocks summing per-function profiles.
- Where the pathway is a direct evidence-driven update rather than proposal-selection, the leverage targets are the update rule and its retention, and the ceiling argument applies wherever a human decision sits in the loop at all.

## Open Questions

- Whether the leverage fraction of a real pathway can be estimated from repository history, by classifying accepted changes as pathway-targeting or task-targeting and checking whether the classification predicts later-episode cost.
- Whether the leveraged-but-clamped regime is observable in Commonplace's own history — a rising improvements-per-judgment ratio at a roughly flat acceptance rate would be the predicted signature.
- Whether leveraged and non-leveraged changes trade off — whether pathway investment displaces task improvement at a rate that makes a high leverage fraction bad policy over a bounded horizon.

---

Relevant Notes:

- [Accumulation counts dependence through the retained result, not through the evidence it caused](./accumulation-counts-dependence-through-the-retained-result.md) — extends: leverage adds a target restriction to the same substitution test, and the restriction is the accumulation/compounding boundary
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: names the pathway functions a leveraged change has to land on
- [Computationally directed self-improvement is a fixed-boundary reallocation ending in contraction](./computationally-directed-self-improvement-is-a-reallocation.md) — extends: the internalization the capacity ingredient consists of, and the human-inclusive starting point the loop compounds away from
- [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](./increasing-computational-autonomy-relocates-human-effort.md) — mechanism: the saturation regime — fixed human attention, rising improvements per judgment — a leveraged loop is clamped into without the capacity ingredient
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: the bound that makes the capacity ingredient warranted evaluation rather than bare autonomy
- [False-positive generation is filtered; false-positive acceptance becomes operative](./false-positive-generation-is-filtered-before-retention.md) — grounds: why the growing test load cannot be skipped — evaluation is the terminal filter
- [Oracle accumulation improves selection for later candidates in its maintained domain](./oracle-accumulation-improves-the-selection-environment.md) — mechanism: the meeting point — a leveraged change to evaluation that widens the warranted unattended domain
- [Reflection buys addressability](./reflection-buys-addressability.md) — extends: what representation adds on top of leverage — the leveraged machinery becomes addressable
- [Retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md) — mechanism: why leverage in the retrieval path delivers only best-effort
- [Self-improving system](./definitions/self-improving-system.md) — defined-in: the boundary-, horizon-, and objective-relative membership both readings are indexed to
- [Reflective system](./definitions/reflective-system.md) — defined-in: the stronger sense of "reflective" the leverage term is deliberately weaker than
- [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) — evidenced-by: the tag-readme episode, where one accepted change was leveraged retrieval repair and another moved multiplier and capacity at once
