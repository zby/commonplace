---
description: "Ordinary notes drop the fused global lifecycle enum and expose only optional committed human verification, while specialized local statuses remain type-owned"
type: ../types/adr.md
tags: []
status: accepted
---

# 044-User verification replaces global note status

**Status:** accepted  
**Date:** 2026-07-11

## Context

The base note type used one `status` enum for maturity (`seedling`), acceptance (`current`), assertion force (`speculative`), and currency (`outdated`). Those meanings were neither one axis nor mechanically checkable. The field also failed at the presentation boundary: repository readers could not distinguish a human-attested artifact from one merely accepted by a local review workflow.

Review acceptance and freshness are criterion-specific local state. They cannot supply a universal note verdict, and specialized artifacts such as ADRs still need coherent type-local lifecycle fields.

## Decision

Ordinary note-family artifacts have no global `status`. Their schemas explicitly reject the field. `note-base` instead exposes one optional property:

```yaml
user-verified: true
```

The only valid value is `true`. Presence means a human user explicitly attests that the artifact's current substantive contents have been verified. Absence means only that no current attestation is committed; it says nothing about truth, maturity, currency, conjecture, or semantic-review history.

Creation, conversion, validation, and review never add verification. A substantive edit removes it. An existing attestation may survive only a mechanical change covered by an explicit human-authorized trivial-change workflow. Git history is the initial audit trail; verifier identity, time, and content hashes are deferred until a demonstrated need exists.

The review selector selects on the committed field exactly, with no alias and no derivation from review freshness. The site renderer labels it and continues to render intentional specialized `status` values. ADR status remains `accepted`, `superseded`, or `deprecated`; review-job execution status is unchanged.

Hypotheses carry their conjectural force in titles or prose. Retired and replaced artifacts carry supersession in prose, links, filenames, or a coherent type-local field.

## Considered alternatives

- **Retaining a smaller lifecycle enum** — rejected: preserves a global axis with no single coherent meaning.
- **Splitting the field into lifecycle plus contract-declared assertion force** — rejected. This was the developed alternative: keep a structural lifecycle enum in the type, and let each collection's `COLLECTION.md` declare what commitment `current` expresses (first-person endorsement, attribution, capture), so an attributed claim could be marked current without asserting belief in it. It failed on two counts. The residual "lifecycle" is not one clean axis either — `status` read as a diagonal through maturity, currency, and endorsement, with a promotion flavor smeared into `seedling`, so the split leaves a fused field behind. And the motivating case needs endorsement to be *inapplicable*, not re-valued: a casebook note asserts nothing in its own voice, and redefining what a label means per collection cannot express an axis that does not apply. Axis decomposition with per-collection axis selection was the successor candidate; deleting the field achieves the same outcome without designing a mechanism ahead of a worked case, and a collection that later needs an explicit axis can define a type-local field.
- **Computing verification from review acceptance or freshness** — rejected: collapses criterion-specific evidence into a universal claim.
- **Converting every former `current` note** — rejected: prior lifecycle metadata is not proof of human attestation, so conversion manufactures attestations.
- **Adding verifier identity, timestamps, or hashes now** — rejected: expands the contract without an exercised requirement.

Deciding forces: the field failed at the presentation boundary (file-only renderers could not distinguish human attestation from workflow acceptance); review acceptance and freshness are criterion-specific and cannot supply a universal verdict; and the fused axes were not mechanically checkable in any combination. Deletion was preferred to relativization on the same grounds the frontmatter-semantics boundary sets: a field's meaning stays type-owned, so a field that cannot hold one meaning globally should not exist globally.

## Consequences

GitHub and other file-only renderers can expose committed human verification without access to the local review database. Selectors and site presentation share the same source of truth. Ordinary notes can be conjectural, retired, reviewed, or immature without forcing those independent properties into one enum.

Human verification is deliberately costly and revocable. Substantive editing workflows must remove it, and a repository may initially contain no verified artifacts. Specialized types remain responsible for defining and documenting any local `status` they retain.

The change is breaking: old note statuses are rejected rather than aliased.

---

Relevant Notes:

- [Review system](../README-REVIEW-SYSTEM.md) — implemented-by: selector semantics and criterion-specific freshness boundary
- [Note type](../../types/note.md) — implemented-by: authoring and revocation contract
- [Representational form](../../notes/definitions/representational-form.md) — rests-on: committed metadata is the portable representation consumed by file-only renderers
