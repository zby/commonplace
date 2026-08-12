---
description: "Why deriving independent choice dimensions from boundary constraints exposes rival designs that inherited solution categories hide"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, artifact-analysis]
---

# First-principles analysis maps a design space before selecting within it

First-principles analysis does more than justify or reject a proposed design. Before a decomposition becomes load-bearing, it constructs a revisable space in which designs can differ. It separates inherited constraints from open choices, derives candidate dimensions whose values predict distinct consequences, and exposes alternatives before requirements and evidence select a position. Prototypes and empirical contrasts can revise the map as it develops. The ordering claim is that exploration across positions and decompositions precedes closure, not that derivation precedes every empirical move.

Starting from familiar solution categories can reverse that order when their seams are treated as fixed. Labels such as prompt, database, memory, workflow, or weights bundle several decisions. These packages preserve useful engineering experience as priors, but comparing instances without unpacking them explores only the alternatives their seams admit. A later explanation may justify the selected package without ever exposing a rival decomposition. Since [a framework rule with a boundary-preserving rival is not an inherited constraint](./a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md), constraints should bound the map; inherited packages should not silently determine the positions within it.

## A design space is generated rather than catalogued

A catalogue starts from existing designs and groups them by resemblance. A first-principles map starts from boundary constraints and asks which questions would change distinct design consequences. Each question becomes a candidate axis. The axes are independent only in this analytic sense; their values may still interact or fail to combine freely in an implementation. Crossing their values generates analytic regions, including combinations for which no familiar implementation exists. A region becomes an available design option only when a witness or feasibility argument shows that the governing constraints permit it.

This makes the map useful for design rather than only classification. It can show that two conventional alternatives differ on several dimensions, that an apparent alternative changes only the packaging, or that existing systems have left a region unexplored. An empty cell remains visible as unoccupied, impossible under a named constraint, or unresolved. The absence of a familiar example does not silently remove it from consideration.

The map is exhaustive only relative to its axes. It therefore offers a criticizable completeness claim rather than proof that every possible design has been enumerated: if the axes are adequate, their permitted combinations span the relevant options. A design that fits no cell is evidence against the map. So are two supposedly distinct cells whose consequences cannot be distinguished. The scheduler-and-rebuilder grid in [Build Systems à la Carte](../sources/build-systems-a-la-carte.ingest.md) demonstrates the method: separating two choices exposes both occupied implementations and empty but buildable regions.

## Representational form demonstrates the method

[Representational form](./definitions/representational-form.md)—how retained content is encoded and consumed—demonstrates this method. It does not accept prompts, programs, and weights as primitive artifact classes. Instead, it asks two questions: does a defined consumer assign consequences to the operative content, or is that content reinterpreted at each use? And is the content localized in an identifiable unit or distributed? Their cross-product produces three observed forms—natural-language, symbolic, and distributed-parametric—plus a fourth analytic cell for which this KB identifies no current agent-system example. That cell remains unresolved rather than impossible.

The same axes predict the default evidence each form admits: read natural-language content, test symbolic content, and probe distributed-parametric content. A mixed artifact can occupy more than one position. Yet representational form is only one slice of the wider design space. [Axes of artifact analysis](./axes-of-artifact-analysis.md) separates it from storage substrate, lineage, and behavioral authority. A file or database can carry multiple forms, while a prompt names a consumption path. Package labels collapse distinctions that designers can vary separately.

## Exploration over decompositions must precede optimization within one

Every design-space map is itself a decomposition. It declares which differences are independent, which instances belong together, and which alternatives count as positions on the same dimension. A map can therefore cause the same premature closure it is meant to prevent. The answer is not to avoid decomposition, but to keep each map revisable until rival positions and rival maps have been exposed.

Once a decomposition becomes fixed, downstream search can improve only the choices it makes reachable. [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) develops this problem for signals, actions, and hypothesis classes, but the mechanism extends beyond learning. Implementation, tuning, debugging, and workflow repair also search within the distinctions and operations admitted by the system's architecture. They can polish a selected region without discovering that the needed correction lies in an excluded one.

First-principles exploration counters this failure by moving search outward across decompositions before moving it inward within one. For a consequential design decision, that order is:

- Fix the boundary commitments and the constraints they bring.
- Derive candidate questions and positions, then use prototypes and empirical contrasts to split, merge, or reject them.
- Challenge the map with counterexamples and a materially different derivation under the same boundary commitments.
- Apply requirements and discriminating evidence to select among the remaining positions, while keeping choices not fixed by constraints or evidence cheap to replace.

This order does not require enumerating a combinatorial universe before prototyping. Prototypes are often how missing axes become visible. Exploration must precede *closure*: the point at which a decomposition becomes authoritative, expensive to revise, or excluded from the system's own repair process.

## Derivation must expose rivals, not rationalize a favorite

Calling an axis first-principled does not make it so. A post-hoc analysis can choose axes that reproduce an already preferred taxonomy. [First-principles reasoning selects for explanatory-reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md)—the ability of an explanation to keep working beyond the cases that produced it—supplies a negative test. A derivation should rule out a plausible rival and identify the premise that does so, or predict how the conclusion changes when a premise changes.

For a design-space map, this means asking whether changing an axis value predicts a different review method, failure mode, cost, or capability; whether removing an axis collapses cases that behave differently; and whether a counterexample forces the map to change. Axes that merely rename familiar packages provide no protection against premature closure.

A single derivation cannot certify its own axes. Hold the problem boundary and inherited commitments fixed, then derive a rival map from a materially different formulation—for example, causal obligations instead of familiar components, or temporal transitions instead of stored objects. Compare which requirements and consequences survive rather than which vocabulary recurs. The two working KWIC decompositions in [Parnas's module-criteria case](../sources/parnas-1972-criteria-decomposing-systems-modules.md) produced the same immediate output, yet predicted different change, comprehension, and interface consequences once their criteria were exposed.

Agreement across rival maps is corroboration, not proof, because the derivations may share a hidden premise. Disagreement focuses investigation on their points of divergence but does not show which map is wrong. Nor does surviving several maps make a requirement an inherited constraint; only derivation from a boundary commitment gives that status. As [only derivation and inheritance warrant a decomposition's scope claim](./only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md), even a valid map holds only while its generating constraints and distinctions remain operative.

## Scope

- Analytically independent axes can interact. Factoring the space makes choices visible but does not establish that every cross-product cell is feasible or that dimensions can be selected independently in implementation.
- Constraint-derived exploration complements empirical search. Derivation exposes candidates and predicts consequences; refutation-capable comparisons determine whether the distinctions matter in use.

## Open Questions

- What evidence is sufficient to treat two design questions as independent axes rather than coupled descriptions of one choice?
- How different must two formulations be before their agreement counts as independent corroboration rather than a shared hidden premise?
- How should a designer decide that the materially different regions have been covered well enough to permit closure?
- Which other classifications in the Commonplace knowledge-base framework generate designer options from primitive axes, and which merely catalogue existing practice?

---

Operationalized into:

- [Invert solution-shaped requests](../instructions/invert-solution-shaped-requests.md) — recovers the problem, tests inherited assumptions, generates rival framings, and delays implementation commitment
