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

The review selector uses `--user-verified` and reads committed frontmatter exactly. There is no `--current` alias and no derivation from review freshness. ProperDocs renders a User verified label from that field, while continuing to render intentional specialized `status` values. ADR status remains `accepted`, `superseded`, or `deprecated`; review-job execution status is unchanged.

Hypotheses carry their conjectural force in titles or prose. Retired and replaced artifacts carry supersession in prose, links, filenames, or a coherent type-local field. The former `current` cohort is not automatically converted: prior lifecycle metadata is not proof of human attestation.

Rejected alternatives:

- Retaining a smaller lifecycle enum would preserve a global axis with no single coherent meaning.
- Computing verification from review acceptance or freshness would collapse criterion-specific evidence into a universal claim.
- Converting every former `current` note would manufacture human attestations.
- Adding verifier identity, timestamps, or hashes now would expand the contract without an exercised requirement.

## Consequences

GitHub and other file-only renderers can expose committed human verification without access to the local review database. Selectors and site presentation share the same source of truth. Ordinary notes can be conjectural, retired, reviewed, or immature without forcing those independent properties into one enum.

Human verification is deliberately costly and revocable. Substantive editing workflows must remove it, and a repository may initially contain no verified artifacts. Specialized types remain responsible for defining and documenting any local `status` they retain.

The change is breaking: old note statuses and `--current` are rejected rather than aliased.

---

Relevant Notes:

- [Review system](../README-REVIEW-SYSTEM.md) — implemented-by: selector semantics and criterion-specific freshness boundary
- [Note type](../../types/note.md) — implemented-by: authoring and revocation contract
- [Representational form](../../notes/definitions/representational-form.md) — rationale: committed metadata is the portable representation consumed by file-only renderers
