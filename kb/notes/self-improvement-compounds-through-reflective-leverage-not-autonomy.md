---
description: "Compounding requires accepted changes that improve the improvement machinery itself — search, evaluation, or retention — a target restriction on cumulativity that is independent of computational autonomy and of reflection"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Self-improvement compounds through reflective leverage, not autonomy

A change has **reflective leverage** when it improves machinery that participates in producing, evaluating, or retaining subsequent improvements. Better retrieval helps later agents diagnose later failures; a better evaluator improves later selection; a lesson about a recurring error reduces the human correction later episodes need. Each of these lands on the improvement pathway itself rather than only on the task the system performs.

Leverage is the property that makes the positive feedback loop available — better improvement machinery yields better improvements, which can again improve the machinery. A loop compounds when a nonzero fraction of its accepted changes carry leverage. It does not compound merely because it repeats, and it does not compound because it runs unattended.

"Reflective" here means *turned back on the improvement pathway*, and is deliberately weaker than [a reflective system's causally connected self-representation](./definitions/reflective-system.md). Leverage is about what a change targets, not about how the changed thing is represented.

## Leverage narrows cumulativity by target

[Cumulativity counts dependence through the retained result](./accumulation-counts-dependence-through-the-retained-result.md): substitute a different earlier retained result, hold the later episode's new evidence fixed, and ask whether the later improvement changes. Leverage adds a restriction on *where* that dependence lands. Cumulativity asks whether a later episode depends on what the earlier one retained; leverage asks whether the dependence runs through a function of the improvement pathway — [search, evaluation, or operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — rather than only through task behavior.

The two readings come apart in one direction and coincide in the other. A change can be cumulative without leverage: a retained parameter that later updates are computed at, feeding only the task policy, satisfies the substitution test while leaving search, evaluation, and retention exactly as they were. Leverage without cumulativity is not available, because a change that improves how later episodes search, evaluate, or retain is by construction a retained result later improvement depends on. Leverage is therefore a proper narrowing, and it inherits cumulativity's indexing: the reading is relative to a declared boundary, horizon, and [objective](./self-improvement-is-relative-to-a-declared-objective.md).

Many changes hit both targets at once. A retained domain theory improves current task performance *and* the diagnosis available to the next failure. Leverage is a property a change has, not a category of change it belongs to, so the same artifact can carry a task effect and a pathway effect and be read for either.

## The loop closes under a human-inclusive boundary

The feedback loop requires no computational autonomy. It runs complete where a maintainer supplies the decisions the pathway needs, [since the interesting transition is an intra-category reallocation of decision-bearing functions rather than a category crossing](./computationally-directed-self-improvement-is-a-reallocation.md). What the loop requires is that some accepted changes improve the machinery; who decided to accept them is a separate reading of the same pathway.

The question that decides compounding is therefore not *did the system originate this change without a human* but *did this change improve a mechanism that participates causally in producing later improvements*. A maintainer who writes a validator, corrects a search recipe, or records a recurring-error lesson has added leverage to a pathway they remain a cut set of. A fully unattended loop that only ever tunes task behavior has added none.

## Leverage does not require reflection either

Leverage is architecture-neutral in the same way the rest of this cluster is. A learned optimizer improves improvement machinery — the update rule is the machinery — with no self-representation anywhere in the pathway, and nothing inside it can state what was improved. The leverage is real and the compounding is real.

What routing the leveraged machinery through a self-representation adds is that the machinery becomes **addressable**: inspectable, criticizable, selectively revisable, transferable to a different problem, exactly as [reflection buys addressability](./reflection-buys-addressability.md) argues for retention in general. Applied to the pathway's own functions, addressability is what lets a bad evaluator be found and fixed rather than only trained over or rolled back wholesale. It changes what can be done about leveraged machinery, not whether leverage exists.

## Two independent axes of progress

Separating leverage from autonomy leaves two things a self-improving system can get better at, and they move independently.

**Improvement capability** — how good the joint human-plus-computational system is at improving itself. This is what the leverage fraction tracks.

**Computational internalization** — how much of the pathway runs without human decisions. This is what boundary contraction tracks.

Each can move without the other. A system gains capability without autonomy when better representations, better retrieval, and better agent assistance make each maintainer-governed episode cheaper and more reliable while the maintainer still supplies every acceptance. A system gains autonomy without capability when it accepts weak changes unattended — bare autonomy is free, and [warranted autonomy is bounded by the domain its oracles can assess](./warranted-autonomy-is-bounded-by-oracle-domain.md), so an unattended gate outside that domain buys internalization at the cost of the acceptances it makes.

Compounding tracks the leverage fraction, not the autonomy profile. Reading a system's progress off its autonomy profile alone therefore misprices both cases: it credits the second and misses the first.

## The empirical signature is testable

The claim predicts an observable difference between a leveraged loop and repeated maintenance. A loop exhibits leverage when earlier accepted changes make later improvement episodes cheaper, broader in reach, more reliable, or less dependent on human judgment — the effect appears in the *next* episode's cost or quality, not only in the task metric the change was accepted against. The null alternative is a loop whose episodes cost what they always cost: real maintenance, producing real improvements, with no term that decreases.

The distinction is measurable in principle without solving the aggregation problem, because it compares successive episodes of one pathway rather than scoring systems against each other.

The [tag-readme episode](../reference/commonplace-as-a-reflective-system.md) supplies a worked case with both signatures. The coverage-mark validator improves future verification: later readers can trust a mark instead of re-running a search, and later candidates face a check that did not exist. The corrected search recipe improves future retrieval: the natural-language procedure that had missed a tagged member now finds it. Both changes landed on pathway functions rather than only on the artifacts under revision, and both were accepted under human governance — the maintainer chose the problem, judged the candidate, and adopted the result.

## Scope

- Leverage does not guarantee compounding. A change to improvement machinery compounds whatever it does, so a worse evaluator or a corrupted retrieval path degrades every later episode that consumes it. Leverage names where a change lands, not whether the landing helps — the same scope limit cumulativity carries.
- The leverage fraction is a reading over named episodes under a declared boundary and horizon, not a quantity asserted of a system. Aggregating per-episode readings into a rate inherits the commensurability difficulty that blocks summing per-function profiles.
- Leverage is defined against the improvement pathway a system actually has. Where the pathway is a direct evidence-driven update rather than a proposal-selection loop, the target functions are the update rule and its retention rather than search and evaluation, and the reading is the same.

## Open Questions

- Whether the leverage fraction of a real pathway can be estimated from repository history, by classifying accepted changes as pathway-targeting or task-targeting and checking whether the classification predicts later-episode cost.
- Whether leveraged and non-leveraged changes trade off — whether pathway investment displaces task improvement at a rate that makes a high leverage fraction bad policy over a bounded horizon.
- Whether leverage in the evaluation function has a different compounding profile than leverage in search or retention, given that a bad evaluator is [delivered exhaustively](./oracle-accumulation-improves-the-selection-environment.md) while a bad retrieval recipe fails best-effort.

---

Relevant Notes:

- [Accumulation counts dependence through the retained result, not through the evidence it caused](./accumulation-counts-dependence-through-the-retained-result.md) — extends: leverage adds a target restriction to the same substitution test, asking where the counted dependence lands
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: names the pathway functions a leveraged change has to land on
- [Computationally directed self-improvement is a fixed-boundary reallocation ending in contraction](./computationally-directed-self-improvement-is-a-reallocation.md) — contrasts: the internalization axis this note holds independent of the capability axis
- [Reflection buys addressability](./reflection-buys-addressability.md) — extends: applies the addressability affordance to the pathway's own machinery, which is what reflection adds on top of leverage
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — contrasts: the case of autonomy gained without capability, where an unattended gate runs outside its oracle's domain
- [Oracle accumulation improves selection for later candidates in its maintained domain](./oracle-accumulation-improves-the-selection-environment.md) — mechanism: the worked case of leverage in the evaluation function, including the exhaustive-delivery wire that makes it compound
- [Retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md) — mechanism: why leverage in the retrieval path compounds only best-effort
- [Self-improving system](./definitions/self-improving-system.md) — defined-in: the boundary-, horizon-, and objective-relative membership this reading is indexed to
- [Reflective system](./definitions/reflective-system.md) — defined-in: the stronger sense of "reflective" this term is deliberately weaker than
- [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) — evidenced-by: the tag-readme episode, where a validator and a corrected search recipe both leveraged pathway functions under human governance
