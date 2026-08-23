# Decide the home of text-contract vocabulary

## Status

Complete 2026-08-23. Option A was selected and implemented under [ADR 071](../../../reference/adr/071-text-contract-is-part-of-the-collection-definition.md): **text contract** is a facet of collection, so the [collection definition](../../../reference/definitions/collection.md#text-contract) is its canonical reference owner. The duplicate theory definition was retired after its content was extracted.

## Decision

Fold the term into `kb/reference/definitions/collection.md`. A text contract has no independent proposition beyond being the complete local authoring declaration of a collection. A standalone file would duplicate that definition, while the collection/type composition page has a broader job. The slightly larger retrieval target is accepted because it gives the term and its type-contract boundary together.

## Question

The question was whether Commonplace should retain a standalone definition of **text contract**, and if so, which reference artifact should own it.

The answer must start from the user's correction: `text contract` describes chosen Commonplace machinery. It is not a definition required to state a theory merely because its meaning is stable.

## Current ownership

- The retired theory-collection definition contained only the text-contract remainder after profile extraction.
- [The reference collection definition](../../../reference/definitions/collection.md) now owns that remainder and says that `COLLECTION.md` is a collection's complete local authoring contract.
- [Collections and types](../../../reference/collections-and-types.md) already explains how the containing `COLLECTION.md` supplies the text-level contract independently of the artifact's type contract.
- [ADR 042](../../../reference/adr/042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) owns the historical decision that introduced `text contract`; its profile decision is superseded separately without rewriting that history.
- Each live `COLLECTION.md` owns the binding contract actually applied to its subtree.
- `AGENTS.md` carries an always-loaded text-contract gloss for operators; its profile half retires in the preceding task.

Before profile extraction, the definition had 30 direct Markdown backlinks from 22 files, including six live collection contracts. That was migration cost and evidence of a shared term; it did not establish theoretical placement or the need for a separate file. A resolved-link recount on 2026-08-23 found 16 direct backlink files: 11 active library surfaces, one frozen proposal archive, one generated connect report, and three files in this workshop. The active library links and `AGENTS.md` glossary reference now point to the collection definition. The archive was changed only for link integrity, and the generated report remains generated rather than hand-edited.

## History

- Commit `7eb616d584d86bbc3a5f6198a888a3c8aa2189d2` (2026-04-12) added `kb/notes/definitions/register.md` while stripping universal mechanics out of collection contracts.
- Commit `1ac2171dd38d2cc0e661e348ae546cfc2d8fbd31` (2026-07-09) replaced it with a `text-contract` definition, added ADR 042 and the profile catalogue, and demoted theoretical/descriptive/prescriptive from an exhaustive taxonomy to default profiles.
- ADR 042 says invariant “theory” should remain in the definition while changing system state belongs in the catalogue. The workshop now contests the word *theory*: invariant system vocabulary and mutable system state can both belong in reference while still benefiting from separate maintenance surfaces.

## Settled boundary from profile retirement

A text contract and a collection prototype attach at different times:

- The text contract is the current, binding declaration in a collection's own `COLLECTION.md`.
- A collection prototype is optional creation-time material. A project may copy it when authoring a new local contract.
- Copying creates no continuing relationship. The destination project owns and maintains its contract; Commonplace does not synchronize it, apply prototype updates to it, or treat it as conforming to the prototype.

The prototype catalogue may repeat a short text-contract gloss for local readability, but it is not a candidate for the canonical definition. An existing collection must be understandable and operable without loading the creation-time prototype it may once have copied.

## Considered options

### A. Fold the term into the collection definition

Extend `kb/reference/definitions/collection.md` with the minimal text-contract definition and its boundary from type contracts. Retarget consumers there and retire the theory definition.

This is the most economical definition surface: a text contract exists only as the local authoring contract of a collection. The cost is that consumers seeking the term must load the broader collection definition.

### B. Keep a small reference definition

Create a standalone `text-contract` definition under `kb/reference/definitions/` containing only the canonical distinction:

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

## Migration completed

- [x] Classified and retargeted the active-library backlinks and `AGENTS.md` glossary reference.
- [x] Folded the text-contract content into the collection definition before retirement.
- [x] Repaired live consumers that still used `register` for the local authoring contract; historical ADR wording remains historical.
- [x] Kept collection prototypes creation-only and non-authoritative for existing collections.
- [x] Added ADR 071 and a current-placement pointer to ADR 042 without changing its historical decision.
- [x] Authorized reference definitions as `defined-in` targets in the notes and reference collection contracts.
- [x] Updated reference navigation; no generated reference-definition index exists.
- [x] Added direct redirects for both the retired text-contract path and its earlier register path, retired freshness state where present, and ran backlink, redirect, and artifact validation.

## Completion condition

Met. One reference owner is selected under the workshop's collection-placement rule, the post-profile backlink set was enumerated and migrated, and neither a theory artifact nor a creation-time prototype is canonical documentation for the binding text contract.
