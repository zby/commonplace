---
description: "Methodological closure tracks whether a retained method settles consequential decisions; computational closure tracks whether those decisions require a human actor"
type: kb/types/note.md
traits: [title-as-claim, synthesis]
tags: [foundations, self-improving-systems]
---

# Methodological and computational closure track different changes

An improvement pathway can stop depending on improvised judgment without stopping its dependence on a human actor, and it can stop depending on a human actor while continuing to improvise. Those are different architectural changes and need different readings of **closure**.

**Methodological closure** asks whether the retained methodology settles the consequential decisions that the pathway raises. A method is less closed where it merely says “use judgment,” names an approver, or leaves a meta-decision to be reconstructed from scratch.

**Computational closure** asks who supplies the decision. A function is computationally closed when its execution needs no human decision; a whole pathway is computationally closed only when every required function meets that condition.

Computational closure and machine autonomy therefore read the same actor allocation: human, computational, or joint for each pathway function. “More computationally autonomous” describes movement in that allocation; “more computationally closed” describes the resulting reduction in functions that still require a human decision.

## Human-inclusive boundaries make allocation load-bearing

A [reflective system](./definitions/reflective-system.md) may include established human processes. Put a maintainer with a standing causal role inside the boundary of a maintained system with readable source, and reflective attribution becomes cheap: the maintainer inspects the source as a representation, edits it, and the build carries the edit into operation. The attribution can be true while saying little about machine performance.

Actor allocation restores the missing discrimination. Under a fixed human-inclusive boundary, report each consequential function as human, computational, or joint; computational closure is the no-human endpoint of that profile. Do not replace the profile with a percentage: functions differ in decomposition, authority, and stakes, and cross-system comparison remains [an open measurement problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md).

## Four concrete combinations

| Improvement decision | Methodologically closed? | Computationally closed? | Why |
|---|---:|---:|---|
| A maintainer manually applies an exact checklist before accepting a patch | Yes | No | The criterion is settled, but a human supplies the verdict. |
| A validator accepts an artifact only when an exact structural predicate holds | Yes | Yes | The criterion and its execution are both explicit and computational. |
| An unattended coding agent is told to inspect failures and “improve the repository” using its own judgment | No | Yes | No human intervenes, but consequential choices remain improvised. |
| A maintainer and agent jointly judge a theory note against “is this good?” | No | No | The criterion is unsettled and a human participates in the verdict. |

**TODO:** Decide whether stable but tacit human expertise counts as retained methodology. If the maintainer in the last row applies a repeatable internal criterion that has never been externalized, its methodological-closure reading may differ from the table.

**TODO:** Reconcile the third row with literal boundary closure. A hosted model can execute without a human while depending on inference infrastructure and a provider outside the selected computational subsystem; the current definition counts only the human dependency.

## When the two changes advance together

A recurring human decision becomes easier to allocate computationally after its inputs, criterion, and failure response have been made explicit. The conversion usually has three parts:

1. **Representation** — the relevant inputs and commitments become available to the deciding process, [since reflection buys addressability](./reflection-buys-addressability.md).
2. **Settlement** — the methodology supplies the criterion or determines the result instead of merely naming a decider, [since a methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md).
3. **Warranted execution** — a computational procedure or oracle implements the criterion with evidence adequate to the case, [since warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md).

These are engineering dependencies, not definitions of one another. A settled gate can remain human-executed; an agent can read explicit commitments yet improvise how to apply them; and a computational procedure can encode a poor proxy. Moving evaluation to a model changes allocation without establishing that its acceptances are trustworthy.

The [Commonplace reference case](../reference/commonplace-as-a-reflective-system.md) applies this conversion to ADR 026 and keeps the trace-specific facts in one place.

## Reflection is a separate question

Reflectivity does not require methodological closure. It requires a causally connected representation of the system's own behavior that processes inside the declared frame can read and change. A reflective pathway may expose its rules for criticism while leaving the next revision to open-ended judgment. Conversely, a fixed pipeline may settle every operational choice without representing or revising itself.

The properties reinforce each other when the represented object is the improvement methodology itself: an addressable criterion can be revised, then a settled and warranted version can be executed computationally. That is a trajectory through a [multi-part profile](./a-self-improving-system-needs-a-profile-not-a-ladder.md), not one scale of reflectivity or closure.

## Scope

- Both closure readings are per decision and per pathway, so mixed profiles are normal: exact validators can coexist with joint review, and settled acceptance rules with improvised objective-setting.
- A loop instance **completes** when search, evaluation, and operative retention occur. Calling that event closure would conflate completion with architecture.
- Both readings require a declared frame. A whole-system closure claim without named decisions and pathways hides the mixed architecture.
- Comparing allocation profiles across releases or systems inherits the open commensurability problem: [measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md).

## Open Questions

- When an initial human instruction makes a downstream agent-performed function joint rather than computational; counting every instruction hides agent performance, while counting none hides decision content supplied up front.
- Whether objective-setting can become methodologically closed without freezing the improvement objective rather than improving it.
- How much representational explicitness computational internalization requires when learned components can execute a decision without exposing its criterion.
- How to distinguish a computational implementation of a settled method from a proxy that silently changes what the method decides.

---

Relevant Notes:

- [A self-improving system needs a profile, not a ladder](./a-self-improving-system-needs-a-profile-not-a-ladder.md) — grounds: locates the two closure readings under governance and actor allocation
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: supplies the pathway functions over which both properties are reported
- [Reflection buys addressability](./reflection-buys-addressability.md) — mechanism: makes retained inputs and criteria available to later deciding processes
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — grounds: supplies the methodological reading of closure
- [Reflective system](./definitions/reflective-system.md) — grounds: the boundary-relative criterion that makes human-inclusive reflection possible
- [Measuring autonomy well enough to see it improve is an open problem](./measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — extends: explains why allocation remains a profile rather than a percentage
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: explains why computational allocation does not by itself justify unattended action
- [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](./increasing-computational-autonomy-relocates-human-effort.md) — extends: states the human-side consequence when computational allocation advances
- [Commonplace as a reflective system](../reference/commonplace-as-a-reflective-system.md) — evidence: applies both closure readings to one observed improvement pathway
- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — contrasts: states why computational allocation stalls where warranted checking is expensive
