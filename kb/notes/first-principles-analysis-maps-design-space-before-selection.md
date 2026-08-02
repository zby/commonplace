---
description: "Why deriving independent choice dimensions from boundary constraints exposes rival designs that inherited solution categories hide"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, artifact-analysis]
---

# First-principles analysis maps a design space before selecting within it

First-principles analysis does not only justify or reject a proposed design. It first constructs the space in which designs can differ. It separates inherited constraints from choices, derives dimensions whose values have different consequences, and makes the resulting alternatives visible before one configuration becomes load-bearing. Selection comes second: requirements and evidence rule out regions of the map or favor one position within it.

Starting from familiar solution categories reverses that order. Labels such as prompt, database, memory, workflow, or weights package several decisions together, so comparing instances of those packages explores only the alternatives their inherited boundaries admit. A later explanation may justify the selected package without exposing a rival decomposition. Since [first principles are inherited constraints, not design choices](./first-principles-are-inherited-constraints-not-design-choices.md), the constraints should bound the map; they should not silently supply the positions within it.

## A design space is generated rather than catalogued

A catalogue starts from designs that happen to exist and groups them by resemblance. A first-principles map starts from questions whose answers can vary independently and whose variation changes a design consequence. Crossing those questions generates candidate regions, including combinations for which no familiar implementation yet exists.

This makes the map useful for design rather than only classification. It can reveal that two conventional alternatives differ on several dimensions, that an apparent alternative changes only packaging, or that a region has been overlooked because existing systems cluster elsewhere. An empty cell remains visible as unoccupied, impossible under a named constraint, or unresolved; it is not silently removed merely because practice supplies no example.

The map is exhaustive only relative to its axes. First-principles analysis therefore does not prove that it has enumerated every possible design. It gives a criticizable completeness claim: if the axes are adequate, their combinations span the relevant options. A design that fits no cell, or two cells with supposedly different consequences that cannot be distinguished, is evidence against the map.

## Representational form demonstrates the method

[Representational form](./definitions/representational-form.md) does not begin with prompts, programs, and weights as three received artifact classes. It asks two prior questions about an artifact's operative part: whether a defined consumer assigns its consequences or consumption interprets them, and whether the content is localized in an identifiable unit or distributed. Their cross-product generates natural-language, symbolic, and distributed-parametric forms, plus a distributed form with assigned consequences that is currently unoccupied in this domain rather than declared impossible.

The generated categories name options available to a designer. Behavior-shaping content can be retained in an interpreted and locally revisable unit, in a localized unit checked against consequences assigned by machinery, in distributed numerical state inspected through behavior, or in a mixed artifact whose operative parts occupy different positions. The same derivation predicts the default evidence each choice admits: read natural-language content, test symbolic content, and probe distributed-parametric content. The map therefore connects positions to review and revision consequences instead of merely giving artifacts new labels.

The example also shows why one map is not the whole design space. [Axes of artifact analysis](./axes-of-artifact-analysis.md) separates representational form from storage substrate, lineage, and behavioral authority because each answers a different design question. A Markdown file can carry natural-language and symbolic parts; a database can store multiple forms; a prompt is a consumption path; and the same retained content can advise in one path and enforce in another. Treating any package as the primary option would collapse dimensions that designers can vary independently.

## Exploration over decompositions must precede optimization within one

Every design-space map is itself a decomposition: it declares which differences are independent, which instances belong together, and which alternatives count as positions on the same dimension. The countermeasure to premature decomposition is therefore not to avoid decomposition, but to keep it at the level of a revisable proposal until rival maps and positions have been exposed.

Once a decomposition becomes fixed, downstream search can improve only the choices it makes reachable. [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) develops this for signals, actions, and hypothesis classes, but the mechanism is not limited to learning. Implementation, tuning, debugging, and workflow repair also search within the distinctions and operations their architecture admits. They can polish a selected region without discovering that the needed correction occupies an excluded one.

First-principles exploration counters this failure by moving search outward before moving it inward. For each consequential design decision:

- identify the boundary commitments and the constraint packets they bring;
- derive questions whose answers change observable consequences;
- generate materially different positions, including unfamiliar and empty ones;
- compare alternative seams rather than only implementations behind one seam;
- apply requirements and discriminating evidence to select among the remaining positions;
- keep choices not fixed by constraints or evidence cheap to replace.

This is not a demand to enumerate a combinatorial universe before prototyping. Prototypes are often how missing axes become visible. Exploration must precede *closure*: the point at which a decomposition becomes authoritative, expensive to revise, or excluded from the system's own repair process.

## Derivation must expose rivals, not rationalize a favorite

Calling an axis first-principled does not make it so. A post-hoc analysis can choose axes that reproduce an already preferred taxonomy, just as it can choose premises broad enough to justify several incompatible practices. [First-principles reasoning selects for explanatory-reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) supplies the negative test: a derivation should rule out a plausible rival, identify the premise that does so, or predict how the conclusion changes when a premise changes.

Applied to a design-space map, that test asks whether changing an axis value predicts a different review method, failure mode, cost, or capability; whether removing an axis collapses cases that behave differently; and whether adding a counterexample forces the map to change. Axes that merely rename familiar packages provide no protection against premature closure.

Even a valid derivation gives conditional rather than universal coverage. As [only derivation and inheritance warrant a decomposition's scope claim](./only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md), the map holds while its generating constraints and distinctions remain operative. First-principles analysis makes that condition explicit so later evidence can revise the map instead of being forced into it.

## Scope

- The claim concerns consequential design dimensions. Enumerating variations that change no relevant behavior, evidence, cost, or failure mode creates taxonomy without expanding the effective design space.
- Independent-looking axes can interact. Factoring the space makes choices visible but does not establish that every cross-product cell is feasible or that dimensions can be selected independently in implementation.
- No map escapes fallibility or regress. The axes are a decomposition subject to rival derivations and counterexamples; first-principles analysis earns value by making that decomposition criticizable, not by terminating criticism.
- Constraint-derived exploration complements empirical search. Derivation exposes candidates and predicts consequences; refutation-capable comparisons determine whether the distinctions matter in use.

## Open Questions

- What evidence is sufficient to treat two design questions as independent axes rather than coupled descriptions of one choice?
- How should a designer decide that the materially different regions have been covered well enough to permit closure?
- Which other Commonplace classifications generate designer options from primitive axes, and which merely catalogue existing practice?

---

Relevant Notes:

- [Representational form](./definitions/representational-form.md) — evidenced-by: its assigned-consequences and localization axes generate current forms, an empty cell, and distinct inspection regimes
- [Axes of artifact analysis](./axes-of-artifact-analysis.md) — extends: applies the same separation discipline across form, substrate, lineage, and behavioral authority
- [First principles are inherited constraints, not design choices](./first-principles-are-inherited-constraints-not-design-choices.md) — grounds: distinguishes boundaries of a design space from replaceable positions within it
- [First-principles reasoning selects for explanatory-reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: requires derivations to rule out rivals or predict changes rather than rationalize an adopted practice
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — mechanism: shows why search within fixed distinctions and operations cannot reach every correction
- [Only derivation and inheritance warrant a decomposition's scope claim; discriminating use earns it](./only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md) — grounds: limits a generated map's initial warrant to the constraints from which its axes derive
