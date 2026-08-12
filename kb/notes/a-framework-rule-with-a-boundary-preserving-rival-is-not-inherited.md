---
description: "A rival design that preserves a framework's boundary invariants while dropping a rule demotes the rule to a design choice; finding no rival certifies nothing — the test cuts one way only"
type: kb/types/note.md
traits: [title-as-claim]
tags: [document-system, foundations]
---

# A framework rule with a boundary-preserving rival is not an inherited constraint

A framework's inherited constraints follow from its boundary commitments; everything else its rules assert is chosen within those commitments. This note gives a heuristic for telling the two apart, and the heuristic cuts in one direction only. Propose the strongest rival design that drops the rule. If the rival preserves the invariants the framework holds fixed, the rule is a design choice, not an inherited constraint. If no rival is found, the rule is only undemoted — not proven inherited — because the rival may exist outside the current implementation, and because certifying inheritance would take a positive derivation from the invariants, which this test does not supply.

The invariants must be stated independently of the rule under test, as observable interfaces or guarantees. Otherwise declaring the rule to be part of the boundary would immunize it and make the test circular. The commitments themselves are chosen — for Commonplace, its consumer architecture, substrate semantics, domain, and machinery interfaces — so "inherited" is always relative to an explicit, independently stated boundary, not to knowledge frameworks in general.

Choosing files for ubiquity and tooling, for example, does not make every file-handling policy an inherited constraint. A parser or adapter that changes a policy while preserving the declared file guarantees demonstrates a choice within the design space. An adapter that changes a loading or identity guarantee changes the boundary contract instead — a rival of that kind belongs to a different framework, not to the same design space, and demotes nothing.

[First-principles analysis maps the design space and then searches for those rivals](./first-principles-analysis-maps-design-space-before-selection.md). The companion note applies the test at scale: first-order content taxonomies [demote to guarded defaults](./a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) when another kind of KB supplies a viable rival.

## Rules that fail the test

Applying the test to Commonplace demotes rules that look foundational but have working rivals under the same boundary invariants:

- The **three [text-contract profiles](./definitions/text-contract.md)** (theoretical, descriptive, and prescriptive) are a proven bundle, but a new kind of KB may require a fourth. The profile set therefore demotes to defaults.
- **Link-label sets** such as `extends`, `grounds`, and `contradicts` are collection-owned selections from a shared catalogue. Another selection can preserve the same linking interface.
- **Type sets** are open and collection-local. The machinery requires type identifiers to point to type-spec paths, but another set of types preserves that requirement.
- **Spending the directory tree on content area rather than kind** is one routing choice. A kind-based tree can preserve the framework's other boundary guarantees.
- **Status and lifecycle enums** may use different values or separate structural state from first-person endorsement without removing lifecycle machinery.

To assess a candidate, state the boundary invariants independently of it, then propose the strongest rival. A rival that preserves the invariants demotes the rule. A rival that changes them belongs to a different boundary contract. An inconclusive comparison leaves the rule where it was.

## Scope

- The test demotes; it does not certify. A rule that has survived the rival hunt so far is at best a candidate inherited constraint, and stays contestable until someone derives it from the independently stated invariants — machinery this note does not provide.
- The demoted list is open in both directions: a later rival can demote a rule not listed here, and no listing is permanent.

---

Relevant Notes:

- [A universal knowledge framework demotes content taxonomies to defaults](./a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) — extends: applies the demotion side to content taxonomies, with a rival kind of KB as the demoting witness
- [First-principles analysis maps a design space before selecting within it](./first-principles-analysis-maps-design-space-before-selection.md) — mechanism: fixes boundary commitments, maps the remaining choice axes, and hunts the rivals this test consumes
- [First-principles reasoning selects for explanatory-reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — contrasts: anchors "first principle" on a different axis — an epistemic filter on explanations, where this note demotes framework rules that have boundary-preserving rivals
