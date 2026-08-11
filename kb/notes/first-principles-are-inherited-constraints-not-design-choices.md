---
description: "A rule is inherited only if it follows from independently stated boundary invariants; a rival that preserves them exposes the rule as a design choice"
type: kb/types/note.md
traits: [title-as-claim]
tags: [document-system, foundations]
---

# First principles are inherited constraints, not design choices

A framework's first principles are constraints inherited from its boundary commitments, not choices made within those boundaries. This note gives a discipline for catching choices that pose as first principles; it does not certify that a rule is inherited. The discipline cuts reliably in one direction only: if a rival design preserves the invariants the framework holds fixed while dropping the rule, the rule is a design choice, not an inherited constraint. It does not run the other way on its own. Failing to find a rival leaves a rule undemoted, not proven inherited, because the rival may exist outside the current implementation, and because "follows from invariants" means something only against invariants stated independently of the rule. Use the rival hunt to demote the rules that are really choices; certifying a constraint as inherited still needs a positive derivation from those independent invariants.

The commitments themselves are chosen. Commonplace's currently visible commitments are its *consumer architecture*, *substrate semantics*, *domain*, and *machinery interfaces*. Inheritance begins only after their invariants have been stated independently of the candidate rule, as observable interfaces or guarantees. Otherwise, declaring the rule to be part of the boundary would make the test circular.

Choosing files for ubiquity and tooling, for example, does not make every file-handling policy an inherited constraint. A parser or adapter that changes a policy while preserving the declared file guarantees demonstrates a choice within the design space. An adapter that changes a loading or identity guarantee changes the boundary contract instead.

An inherited constraint can also follow from several commitments acting together. A file store, parser, and consumer may jointly require an encoding protocol that none requires in isolation. What matters is that the rule follows from the combined invariants, not that it can be assigned to a single source.

The discipline therefore separates positions *within* a design space from its boundaries. A design choice has a working rival under the same invariants and can demote to a guarded default; finding that rival is the reliable half of the test. A candidate with no rival found yet is only undemoted, not inherited, and still owes the positive derivation before it counts as a boundary constraint. [First-principles analysis maps the design space and then searches for those rivals](./first-principles-analysis-maps-design-space-before-selection.md). The companion note applies the other side of this test: first-order content taxonomies [demote to guarded defaults](./a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) when another kind of KB supplies a viable rival.

## Worked candidates: rules that resist demotion so far

These are worked examples, not settled classifications. Each entry names a boundary source, the weakest consequence it plausibly supports, and the stronger choices that remain local. Each has so far resisted the rival hunt under Commonplace's current boundary contract — which reliably demotes a rule that *has* a rival but does not by itself certify the survivors. Each still owes a positive derivation from independently stated invariants, and composability (2) already has a candidate rival in field- or chunk-level retrieval. The list is open.

1. **Bounded context / context economy** — The *consumer architecture* gives each LLM inference a finite context, and quality degrades before the hard limit (since [agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md)). Retrieval and external state can change what enters a call, but they do not remove the need to spend that call's context deliberately. The context economy is inherited; specific length and selection policies are local strategies for serving it (since [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md)).

2. **Composability / co-loading** — Commonplace's *artifact-loading interface* loads authored artifacts as whole units into shared prompt contexts. Consumers therefore pay for every claim in a selected artifact, so each artifact must be useful as a unit without pulling unrelated claims into context (see [short composable notes maximize combinatorial discovery](./short-composable-notes-maximize-combinatorial-discovery.md)). Verified field- or chunk-level retrieval would change the interface and therefore the inherited requirement. The stronger rule that every artifact be citable as a bare premise remains a theoretical-profile design choice.

3. **Substrate asymmetry** — The *file substrate* gives every artifact a physical location without extra machinery, whereas classification in file-header metadata (frontmatter) becomes total only when the *validation interface* requires it. Location and metadata can both carry policy, but their guarantees come from different sources: placement is substrate-native, while classification totality is machinery-enforced (because [directory placement is total, frontmatter classification is partial](./directory-placement-is-total-frontmatter-classification-is-partial.md)).

4. **Answerability** — The *domain commitment* to knowledge requires a [knowledge artifact](./definitions/knowledge-artifact.md) to answer to a world state, system, outcome, or source. It can therefore be wrong or stale. To claim that a [collection](../reference/definitions/collection.md) holds knowledge is to claim that this relation and its staleness condition can be identified (see [the companion note's scope test](./a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md)). The specific relation is local; the existence of one is inherited.

5. **Declaration obligation** — *Machinery coherence* requires routing and validation to resolve a loadable contract for every writable collection. The inherited requirement is resolvability, not where the contract lives. Commonplace chooses a local `COLLECTION.md`; [ADR 017 records that design and its alternatives](../reference/adr/017-collection-md-is-the-register-convention-boundary.md).

6. **Admission discipline** — *Shared identifier semantics* require some governance to prevent incompatible meanings from occupying the same shared slot. Namespaced or purely local extensions need no global admission. Commonplace's worked-case guard — admitting a shared entry only after it survives use in a real collection — is one chosen discipline, not the inherited minimum.

7. **Derived-copy rule** — *Trust semantics* and *machinery coherence* require a load-bearing copy of information recomputable from ground truth to be machine-checked against that source or omitted (because [a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)). An explicitly advisory cache that consumers may ignore or recompute falls outside the rule. The constraint begins when machinery invites consumers to trust the copy as current.

## Rules that fail the test

These rules look foundational but have working rivals under the same boundary invariants:

- The **three [text-contract profiles](./definitions/text-contract.md)** (theoretical, descriptive, and prescriptive) are a proven bundle, but a new kind of KB may require a fourth. The profile set therefore demotes to defaults.
- **Link-label sets** such as `extends`, `grounds`, and `contradicts` are collection-owned selections from a shared catalogue. Another selection can preserve the same linking interface.
- **Type sets** are open and collection-local. The machinery requires type identifiers to point to type-spec paths, but another set of types preserves that requirement.
- **Spending the directory tree on content area rather than kind** is one routing choice. A kind-based tree can preserve the framework's other boundary guarantees.
- **Status and lifecycle enums** may use different values or separate structural state from first-person endorsement without removing lifecycle machinery.

To assess a candidate, first state the boundary invariants independently of it. Then propose the strongest rival. If the rival preserves the invariants, demote the rule. If the rival changes them, it belongs to a different boundary contract. If the comparison does not establish which happened, first-principle status remains unproven.

## Caveats

The discipline is more durable than the enumeration: a later candidate may qualify, and a listed one may demote when a rival exposes an implementation choice.

Boundary declarations can be gamed by naming the candidate rule as an invariant, which is why the invariants must be stated independently of the rule under test. “Inherited” is therefore always relative to an explicit, independently justified framework boundary, not to knowledge bases in general.

---

Relevant Notes:

- [A universal knowledge framework demotes content taxonomies to defaults and keeps answerability](./a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) — extends: supplies the stable complement to its demotion claim and generalizes its answerability test by adding the consumer, substrate, and machinery as further inheritance sources
- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: why the context economy is consumer-inherited and cannot be opted out of
- [Agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — grounds: the binding form of the context bound the economy answers to
- [Short composable notes maximize combinatorial discovery](./short-composable-notes-maximize-combinatorial-discovery.md) — grounds: co-loading is why composability is inherited from how the consumer ingests artifacts
- [Directory placement is total, frontmatter classification is partial](./directory-placement-is-total-frontmatter-classification-is-partial.md) — grounds: the substrate asymmetry that location and type contracts inherit
- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — grounds: the derived-copy rule inherited from machinery coherence
- [First-principles analysis maps a design space before selecting within it](./first-principles-analysis-maps-design-space-before-selection.md) — mechanism: fixes boundary commitments, maps the remaining choice axes, and challenges the map with rival decompositions
- [First-principles reasoning selects for explanatory-reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — contrasts: anchors "first principle" on a different axis — an epistemic filter selecting explanations for explanatory-reach, where this note gives a structural test for which framework rules are undemotable
