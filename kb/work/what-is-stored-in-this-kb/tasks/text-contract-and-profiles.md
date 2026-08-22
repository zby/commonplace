# Decide the home of text-contract vocabulary

## Status

Open, but narrowed. The previously proposed relocation was deliberately stopped before editing library artifacts so it could be decided under the workshop's general content model. Retiring `profile` in favour of one-time-copy [collection prototypes](./retire-profiles-for-collection-prototypes.md) is complete under [ADR 069](../../../reference/adr/069-collection-contract-bundles-become-one-time-prototypes.md). That migration removed profile content from the current definition in place without moving, renaming, or deleting the file; this task now decides only the home of the text-contract remainder.

## Question

Should Commonplace retain a standalone definition of **text contract**, and if so, which reference artifact should own it?

The answer must start from the user's correction: `text contract` describes chosen Commonplace machinery. It is not a definition required to state a theory merely because its meaning is stable.

## Current ownership

- [The theory-collection definition](../../../notes/definitions/text-contract.md) now contains only the text-contract definition, preserved at the same path for this decision.
- [The reference collection definition](../../../reference/definitions/collection.md) already says that `COLLECTION.md` is a collection's local authoring contract.
- [Collections and types](../../../reference/collections-and-types.md) already explains how the containing `COLLECTION.md` supplies the text-level contract independently of the artifact's type contract.
- [ADR 042](../../../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) owns the historical decision that introduced `text contract`; its profile decision is superseded separately without rewriting that history.
- Each live `COLLECTION.md` owns the binding contract actually applied to its subtree.
- `AGENTS.md` carries an always-loaded text-contract gloss for operators; its profile half retires in the preceding task.

Before profile extraction, the definition had 30 direct Markdown backlinks from 22 files, including six live collection contracts. That was migration cost and evidence of a shared term; it did not establish theoretical placement or the need for a separate file. The post-migration exact-path sweep still finds 22 files, but the composition changed: 13 active library surfaces (including four ADRs), one frozen proposal archive, and eight workshop files. None of the seven live collection contracts links to the definition now. Use that residual set, not the coincidentally equal pre-migration file count, as the move set for this decision.

## History

- Commit `7eb616d584d86bbc3a5f6198a888a3c8aa2189d2` (2026-04-12) added `kb/notes/definitions/register.md` while stripping universal mechanics out of collection contracts.
- Commit `1ac2171dd38d2cc0e661e348ae546cfc2d8fbd31` (2026-07-09) replaced it with `text-contract.md`, added ADR 042 and the profile catalogue, and demoted theoretical/descriptive/prescriptive from an exhaustive taxonomy to default profiles.
- ADR 042 says invariant “theory” should remain in the definition while changing system state belongs in the catalogue. The workshop now contests the word *theory*: invariant system vocabulary and mutable system state can both belong in reference while still benefiting from separate maintenance surfaces.

## Settled boundary from profile retirement

A text contract and a collection prototype attach at different times:

- The text contract is the current, binding declaration in a collection's own `COLLECTION.md`.
- A collection prototype is optional creation-time material. A project may copy it when authoring a new local contract.
- Copying creates no continuing relationship. The destination project owns and maintains its contract; Commonplace does not synchronize it, apply prototype updates to it, or treat it as conforming to the prototype.

The prototype catalogue may repeat a short text-contract gloss for local readability, but it is not a candidate for the canonical definition. An existing collection must be understandable and operable without loading the creation-time prototype it may once have copied.

## Live options

### A. Fold the term into the collection definition

Extend `kb/reference/definitions/collection.md` with the minimal text-contract definition and its boundary from type contracts. Retarget consumers there and retire the theory definition.

This is the most economical definition surface: a text contract exists only as the local authoring contract of a collection. The cost is that consumers seeking the term must load the broader collection definition.

### B. Keep a small reference definition

Create `kb/reference/definitions/text-contract.md` containing only the canonical distinction:

- text contract: the binding local declaration;
- it states purpose and scope, quality goal, title and description conventions, attribution requirements where applicable, maintenance semantics, and outbound link grammar;
- it is independent from the artifact's type contract;
- it is not a collection prototype, content kind, production relation, or behavioral-authority classification.

This preserves a cheap glossary target but costs another surface synchronized with the collection definition and `collections-and-types.md`.

### C. Let the composition document own the term

Make `kb/reference/collections-and-types.md` canonical for `text contract`, expanding its opening only as needed and retiring the standalone theory definition. This puts the term where agents already learn how the two applicable contracts compose, but makes a general architecture page carry glossary duty.

## Decision tests

- Does a consumer need the term without loading the broader collection or collection/type composition model?
- Would a standalone definition carry any proposition not already owned by `definitions/collection.md`, `collections-and-types.md`, or live collection contracts?
- Which target makes the text-contract/type-contract boundary easiest to retrieve without duplicating it?
- Is the term important enough for an always-loaded `AGENTS.md` gloss after the profile half is removed?
- Which option leaves one canonical reference owner while allowing other pages to use a one-sentence local restatement?

## Required migration work after selection

- Classify the 13 active-library backlinks by whether they still need a standalone text-contract definition; the exact-path recount is complete.
- Move or fold the text-contract-only content into the selected reference owner and retarget those residual consumers plus the `AGENTS.md` vocabulary entry.
- Repair stale consumers that still call the local authoring contract `register`.
- Do not make the prototype catalogue authoritative for existing collections or introduce a maintenance link from a prototype to a copied contract.
- Record the later placement change without falsifying ADR 042's historical decision; add a supersession pointer rather than rewriting what it originally decided.
- Reconcile link labels with each source collection's authorized vocabulary.
- Update collection headings, reference navigation, and any generated definition index.
- If the old theory path retires, follow the library-artifact retirement/redirect procedure, validate every touched artifact, and run a backlink plus broken-link sweep confirming it is no longer canonical.

## Completion condition

One reference owner is selected under the workshop's collection-placement rule, the post-profile backlink set is enumerated, and the implementation can be executed atomically without leaving a theory artifact or a creation-time prototype as canonical documentation for the binding text contract.
