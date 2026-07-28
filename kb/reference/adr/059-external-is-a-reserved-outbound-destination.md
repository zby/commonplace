---
description: External is a reserved outbound destination that a source collection must explicitly authorize, without making the open web a collection or a connect-search surface
type: ../types/adr.md
tags: []
status: accepted
---

# 059-External is a reserved outbound destination

**Status:** accepted
**Date:** 2026-07-28
**Extends:** [ADR-019](./019-collection-owned-link-vocabulary.md)
**Amends:** [ADR-023](./023-quote-anchored-citations-for-code-grounded-reviews.md)

## Context

ADR 019 makes the source collection's `COLLECTION.md` the authority for outbound links, but models every destination as another collection. The corpus also contains intentionally authored links to external evidence, code, papers, and editorial sources. Treating those links as outside the collection contract lets a type or local convention broaden the link surface without the source collection authorizing it.

## Decision

Add `external` as a reserved outbound destination. A destination is now either a local collection or `external`; the latter denotes targets outside the KB and is not itself a collection.

The source collection remains the sole authorization boundary:

- `external` must be authorized by name or through the destination wildcard `any` before authors may add external links. The absence of both means external links are not authorized.
- A declaration states the permitted reader need and link surface. It may delegate type-specific citation shape, pinning, or validation to a type contract, but a type cannot independently authorize external targets.
- `any` means every destination, including `external`; choosing the wildcard is itself an explicit collection-level authorization.
- Formal labelled external edges use labels authorized for `external`. A collection may instead authorize an inline citation or editorial surface that does not render a formal identifier.

`cp-skill-connect` does not prospect `external`: its discovery surface remains the local repository. It may evaluate an external target already supplied by the user or already present in loaded context, but authorization alone never licenses open-web discovery. `cp-skill-write` applies the same already-in-hand rule it uses for other links.

This decision adds an authorization class, not a general external-link policy. Retention, snapshot preference, source quality, and link-rot policy remain collection-local or future work.

## Consequences

- Existing collection ownership now covers external links instead of treating them as a type-level exception.
- Collections opt in independently; no global permission is introduced.
- External targets do not need fake collection identities, local indexes, backlinks, or connect prospecting.
- Current external links in collections without an `external` declaration become visible contract debt rather than silently sanctioned precedent.

## Relevant Notes

- [ADR-019: collection-owned link vocabulary](./019-collection-owned-link-vocabulary.md) — foundation: keeps authorization at the source collection
- [ADR-023: quote-anchored citations](./023-quote-anchored-citations-for-code-grounded-reviews.md) — amended: the collection authorizes external targets while the type still owns citation shape
- [Link vocabulary](../link-vocabulary.md) — implements: authoring rules for the reserved destination
