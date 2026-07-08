---
description: "A framework rule is a first principle iff inherited from what the framework cannot choose — consumer, substrate, domain, or machinery coherence; unlike design choices, these cannot demote to defaults"
type: kb/types/note.md
traits: [title-as-claim]
tags: [document-system, foundations]
status: seedling
---

# First principles are inherited constraints, not design choices

A companion note shows which rules a universal framework *cannot* keep as universals: first-order content taxonomies demote to guarded defaults, because they are [distilled](./definitions/distillation.md) from too few knowledge bases and the next kind of KB breaks them (see [a universal knowledge framework demotes content taxonomies to defaults](./a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md)). This note is the other half: which rules genuinely constrain the design space and therefore cannot demote.

The membership test: **a rule is a first principle iff it is inherited from something the framework cannot choose.** Concretely, removing it would force a change to one of the framework's boundary conditions — the *consumer* it serves, the *substrate* it is built on, the *domain* it commits to (knowledge), or the coherence of the *second-order machinery* it runs. A design choice can be swapped for a rival and the framework still works; a first principle cannot be dropped without moving one of those boundaries.

This is why the two halves are not symmetric. Design choices are *positions within* the design space, so a framework aiming at universality can offer several and let a collection pick — they demote to guarded defaults. First principles are *boundaries of* the design space, so there is no rival position to demote to; changing one is not reconfiguration but a different framework. The test generalizes the complement note's answerability test by naming the full set of inheritance sources rather than the domain alone: answerability is the domain-inherited principle, and the others are inherited from the consumer, the substrate, and the machinery.

## The principles that currently pass the test

Each is named with the boundary it inherits from. The list is what passes today, not a closed set.

1. **Bounded context / context economy** — inherited from the *consumer's architecture*. The reader attends to one finite window in which everything competes (since [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md)), and the binding pressure is silent degradation before any hard limit (since [agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md)). Specific length norms — "keep notes short" — are *local strategies* serving this economy and can be traded for others; the economy itself cannot be opted out of while the consumer is an LLM.

2. **Composability / co-loading** — inherited from *how the consumer ingests artifacts*: files load as whole units into one shared window, so an artifact's usefulness is decided by what it does when co-present with others (see [short composable notes maximize combinatorial discovery](./short-composable-notes-maximize-combinatorial-discovery.md)). The universal form is weak: every artifact must remain usable when loaded alone, without dragging in unrelated claims. The strong form — a note must be citable as a bare premise — is a theoretical-register profile feature, a design choice layered on top, not the principle.

3. **Substrate asymmetry** — inherited from the *file substrate*. Directory placement is total (every file has exactly one location, no opt-out) while frontmatter classification is partial and opt-in, so location contracts and type contracts encode different guarantees and cannot substitute for each other (because [directory placement is total, frontmatter classification is partial](./directory-placement-is-total-frontmatter-classification-is-partial.md)). A framework on a different substrate would inherit a different asymmetry, but on files this one is not negotiable.

4. **Answerability** — inherited from the *domain commitment* to knowledge. Every artifact must answer to something outside itself and can therefore be wrong or stale; a collection that cannot state what its artifacts answer to and what makes one stale is not holding knowledge (see the [knowledge-artifact](./definitions/knowledge-artifact.md) definition, and the complement note's scope test). Which relation an artifact bears — to the world, a system, an outcome, a source — is local; *having* one is not.

5. **Declaration obligation** — inherited from the *second-order machinery* itself. Every writable collection must carry a loadable contract, because the machinery routes and validates by reading that contract; a collection without one is an operational defect regardless of content. The complement note treats this as the surviving second-order universal (its shipped instance is ADR 017's `COLLECTION.md`).

6. **Worked-case guard** — inherited from *machinery coherence*. Once taxonomies are opened into extensible sets, entries may be admitted only after surviving use in a real collection, never from anticipation. Without this admission discipline the open sets proliferate until no convention is shared — which is the other way to stop being a framework. The complement note identifies this guard as the load-bearing piece that lets closed taxonomies safely open.

7. **Derived-copy rule** — inherited from *machinery coherence*. A copy of information recomputable from a ground-truth source must be machine-checked against that source or not exist; a hand-maintained-and-trusted copy is a trap (because [a derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md)). Any framework that caches recomputable values inherits this, since a silently stale trusted cache corrupts the consumers that trust it.

## Contrast: rules that look like principles but demote

The membership test earns its keep by *excluding* rules that feel foundational but are positions the framework chose and could re-choose. Each of these demotes to a guarded default per the complement note:

- The **three [registers](./definitions/register.md)** (theoretical / descriptive / prescriptive) — a proven bundle, but a new kind of KB can need a fourth; they demote to default text-contract profiles.
- **Link-label sets** — `extends`, `grounds`, `contradicts`, and the rest are a collection-owned selection from a shared catalogue, not a universal vocabulary.
- **Type sets** — open and collection-local; the framework fixes that types *exist* and are path-valued (machinery), not *which* types there are (choice).
- **Spending the directory tree on content-area** rather than on kind — a routing decision a given KB makes, reversible without touching the framework.
- **Status / lifecycle enums** — the existence of a lifecycle is machinery; the specific values, and whether status fuses structural state with first-person endorsement, are a choice sitting one level too high.

The tell in every case: you can name a rival that also works. When no rival exists because the alternative is "change the consumer, substrate, domain, or break the machinery," the rule is inherited, and the list above collects the ones currently visible.

## Caveats

The list is open, like everything the complement note governs. It is what passes the test today; a later principle may be recognized as inherited, or one of these may turn out to be a disguised choice with an unnoticed rival. No exhaustiveness is claimed and no principle here is the "only" thing that stays fixed — the durable content is the *test*, not the enumeration. And "inherited" is relative to a framework's own boundary commitments: a framework that changed consumer or substrate would inherit a different set, so these are first principles *of this framework*, not of knowledge bases in general.

---

Relevant Notes:

- [A universal knowledge framework demotes content taxonomies to defaults and keeps answerability](./a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) — extends: supplies the stable complement to its demotion claim and generalizes its answerability test by adding the consumer, substrate, and machinery as further inheritance sources
- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: why the context economy is consumer-inherited and cannot be opted out of
- [Agent context is constrained by soft degradation, not hard token limits](./agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — grounds: the binding form of the context bound the economy answers to
- [Short composable notes maximize combinatorial discovery](./short-composable-notes-maximize-combinatorial-discovery.md) — grounds: co-loading is why composability is inherited from how the consumer ingests artifacts
- [Directory placement is total, frontmatter classification is partial](./directory-placement-is-total-frontmatter-classification-is-partial.md) — grounds: the substrate asymmetry that location and type contracts inherit
- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — grounds: the derived-copy rule inherited from machinery coherence
- [Knowledge artifact](./definitions/knowledge-artifact.md) — defined-in: the answerability boundary that makes the domain-inherited principle a knowledge principle
