---
description: "A rule is a first principle iff inherited from a boundary the framework cannot choose (currently: consumer, substrate, domain, machinery coherence); design choices demote to defaults, these cannot"
type: kb/types/note.md
traits: [title-as-claim]
tags: [document-system, foundations]
status: seedling
---

# First principles are inherited constraints, not design choices

A companion note shows which rules a universal framework *cannot* keep as universals: first-order content taxonomies [demote to guarded defaults](./a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) because they are not universal — the next kind of KB breaks them. This note is the other half: the rules that genuinely constrain the design space and therefore cannot demote.

The membership test: **a rule is a first principle iff it is inherited from something the framework cannot choose.** Concretely, removing the rule would force a change to one of the framework's boundary conditions — the *consumer* it serves, the *substrate* it is built on, the *domain* it commits to (knowledge), or the coherence of the *machinery* it runs. These are the boundary conditions currently visible; the list is open, like the list of principles itself. Machinery coherence sits apart from the external three because it binds only *after* the framework has built machinery of a given kind. But it is inherited in the sense that counts: given that construction, the rule has no working rival. And that is the line between principle and design choice throughout — a design choice has a rival that works under the very same commitments; an inherited principle does not.

The two halves are therefore not symmetric. Design choices are *positions within* the design space: a rival can be swapped in and the framework still works, so a framework aiming at universality can offer several and let a collection pick — they demote to guarded defaults. First principles are *boundaries of* the design space: there is no rival position to demote to, and changing one is not reconfiguration but a different framework.

## The principles that currently pass the test

Each is named with the boundary it inherits from. The list is what passes today, not a closed set.

1. **Bounded context / context economy** — inherited from the *consumer's architecture*. The reader attends to one finite window in which everything competes (since [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md)), and the binding pressure is silent degradation before any hard limit (since [agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md)). Specific length norms are *local strategies* serving this economy; the economy itself cannot be opted out of while the consumer is an LLM.

2. **Composability / co-loading** — inherited from *how the consumer ingests artifacts*: files load as whole units into one shared window, so an artifact's usefulness is decided by what it does when co-present with others (see [short composable notes maximize combinatorial discovery](./short-composable-notes-maximize-combinatorial-discovery.md)). The inherited form is weak — every artifact must stay usable when loaded alone, without dragging in unrelated claims. The stronger "citable as a bare premise" rule is a theoretical-register design choice layered on top, not the principle.

3. **Substrate asymmetry** — inherited from the *file substrate*. Directory placement is total (every file has exactly one location, no opt-out) while frontmatter classification is partial and opt-in, so location contracts and type contracts encode different guarantees and cannot substitute for each other (because [directory placement is total, frontmatter classification is partial](./directory-placement-is-total-frontmatter-classification-is-partial.md)). On files this asymmetry is not negotiable.

4. **Answerability** — inherited from the *domain commitment* to knowledge. Every artifact must answer to something outside itself and can therefore be wrong or stale; a collection that cannot state what its artifacts answer to and what makes one stale is not holding knowledge (see [the complement note's scope test](./a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md), which states the answerability property; the [knowledge-artifact](./definitions/knowledge-artifact.md) definition supplies the artifact class this commitment quantifies over). Which relation an artifact bears — to the world, a system, an outcome, a source — is local; *having* one is not.

5. **Declaration obligation** — inherited from *machinery coherence*. Every writable collection must carry a loadable contract, because the machinery routes and validates by reading that contract; a collection without one is an operational defect regardless of content. The complement note treats this as the surviving second-order universal (its shipped instance is ADR 017's `COLLECTION.md`).

6. **Admission discipline** — inherited from *machinery coherence*. Once taxonomies are opened into extensible sets, some admission brake is required: without one, the open sets proliferate until no convention is shared — which is the other way to stop being a framework. As with composability, the inherited form is weak — *an* admission discipline must exist — while the specific worked-case guard (entries admitted only after surviving use in a real collection, never from anticipation) is the discipline this framework chose, layered on top. The complement note identifies that guard as the load-bearing piece that lets closed taxonomies safely open.

7. **Derived-copy rule** — inherited from *machinery coherence*. A copy of information recomputable from a ground-truth source must be machine-checked against that source or not exist; a hand-maintained-and-trusted copy is a trap (because [a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)). Any framework that caches recomputable values inherits this, since a silently stale trusted cache corrupts the consumers that trust it.

## Contrast: rules that look like principles but demote

The membership test earns its keep by *excluding* rules that feel foundational but are positions the framework chose and could re-choose. Each of these demotes to a guarded default per the complement note:

- The **three [registers](./definitions/register.md)** (theoretical / descriptive / prescriptive) — a proven bundle, but a new kind of KB can need a fourth; they demote to default text-contract profiles.
- **Link-label sets** — `extends`, `grounds`, `contradicts`, and the rest are a collection-owned selection from a shared catalogue, not a universal vocabulary.
- **Type sets** — open and collection-local; the framework fixes that types *exist* and are path-valued (machinery), not *which* types there are (choice).
- **Spending the directory tree on content-area** rather than on kind — a routing decision a given KB makes, reversible without touching the framework.
- **Status / lifecycle enums** — the existence of a lifecycle is machinery; the specific values, and whether status fuses structural state with first-person endorsement, are a choice sitting one level too high.

The tell in every case: you can name a rival that also works *under the same boundary commitments*. When no rival exists — because the only alternative is to change the consumer, substrate, or domain, or to break the machinery — the rule is inherited, and the list above collects the ones currently visible.

## Caveats

The durable content is the *test*, not the enumeration: a later principle may be recognized as inherited, or one of these may turn out to be a disguised choice with an unnoticed rival, and neither outcome would touch the test itself. The test defines first-principle status rather than deciding it — the rival-hunt is how the test is applied, and application is fallible in both directions. And "inherited" is always relative to a framework's own boundary commitments: a framework that changed consumer or substrate would inherit a different set. So these are first principles *of this framework*, not of knowledge bases in general.

---

Relevant Notes:

- [A universal knowledge framework demotes content taxonomies to defaults and keeps answerability](./a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) — extends: supplies the stable complement to its demotion claim and generalizes its answerability test by adding the consumer, substrate, and machinery as further inheritance sources
- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: why the context economy is consumer-inherited and cannot be opted out of
- [Agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — grounds: the binding form of the context bound the economy answers to
- [Short composable notes maximize combinatorial discovery](./short-composable-notes-maximize-combinatorial-discovery.md) — grounds: co-loading is why composability is inherited from how the consumer ingests artifacts
- [Directory placement is total, frontmatter classification is partial](./directory-placement-is-total-frontmatter-classification-is-partial.md) — grounds: the substrate asymmetry that location and type contracts inherit
- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — grounds: the derived-copy rule inherited from machinery coherence
- [Knowledge artifact](./definitions/knowledge-artifact.md) — defined-in: the artifact class the domain commitment's answerability requirement quantifies over
- [First-principles reasoning selects for explanatory reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — contrasts: anchors "first principle" on a different axis — an epistemic filter selecting explanations for reach, where this note gives a structural test for which framework rules are undemotable
