---
description: "Accepted decision to define text contract as part of collection, retire the duplicate theory definition, and keep each COLLECTION.md as the only binding local contract"
type: ../types/adr.md
tags: []
status: accepted
---

# 071-Text contract is part of the collection definition

**Status:** accepted
**Date:** 2026-08-23
**Extends:** [ADR 042](./042-register-becomes-a-default-profile-under-open-ended-text-contracts.md), [ADR 069](./069-collection-contract-bundles-become-one-time-prototypes.md), [ADR 070](./070-notes-bind-choices-reference-records-selections-and-state.md)

## Context

ADR 042 introduced **text contract** as the name for the binding local
declaration in a collection's `COLLECTION.md`; after ADR 069 retired the
profile model, only the destination's local contract binds.

The remaining text-contract definition lived in `kb/notes/definitions/`, but
its intended contribution was Commonplace's selected collection machinery. It
did not state an independent claim about the design space after that choice was
bound. Under ADR 070, its canonical description therefore belongs in
`kb/reference/`.

Three reference surfaces already covered the concept. The collection
definition named `COLLECTION.md` as the local authoring contract;
`collections-and-types.md` explained how collection and type contracts compose;
and each live `COLLECTION.md` contained the contract that actually applies.
Keeping another standalone definition would repeat those boundaries and create
another surface to synchronize.

## Decision

Fold **text contract** into the existing
[collection definition](../definitions/collection.md#text-contract). A text
contract exists only as the complete local authoring declaration of a
collection, so the collection definition is its canonical reference owner.
`collections-and-types.md` may restate the collection/type distinction for
local readability, and `AGENTS.md` may keep its short operational gloss, but
both point to the collection definition.

Retire the duplicate theory definition; its published path and the earlier
`register` definition path redirect directly to the collection definition,
without redirect chains.

Reference definitions are valid `defined-in` targets. The notes and reference
collection contracts therefore authorize `defined-in` links to both
`notes/definitions` and `reference/definitions`; the structural `definition`
type remains independent of collection placement.

## Considered alternatives

**Keep a standalone reference definition.** This would preserve the cheapest
term-only retrieval target. Rejected because the file would add no proposition
beyond the collection definition and would have to stay synchronized with it.

**Make `collections-and-types.md` canonical.** This would put the term beside
the composition model most authors need. Rejected because text contract is a
facet of collection, while the composition page has the broader job of
explaining two independent contracts and their path resolution.

**Leave the definition in theory.** This would avoid migration. Rejected
because stable vocabulary is not automatically theoretical: removing
Commonplace's chosen `COLLECTION.md` architecture removes this definition's
intended contribution.

## Consequences

There is one descriptive owner for collection and text-contract vocabulary.
Term lookup is slightly less granular, but an agent loads the boundary and its
type-contract exclusion together, which is the distinction most likely to
matter during authoring or relocation.

**Operativity path.** This definition is descriptive, not itself binding.
Writing, connection, review, and validation resolve the nearest
`COLLECTION.md`; that local file supplies the operative rules with its existing
contract force. No authoring or runtime consumer reads the retired theory path.
The reference definition tells maintainers what that consumed surface means,
while each collection remains complete without it.

Future edits to text-contract semantics change the collection definition and any affected
live `COLLECTION.md` contracts; they do not require synchronizing a standalone
glossary artifact.

---

Relevant Notes:

- [Collection and text contract](../definitions/collection.md) — implemented-by: owns the current definition and the boundary from type contracts
- [Collections and types](../collections-and-types.md) — see-also: explains how the two independent contracts compose during authoring and validation
- [ADR 042: Register becomes a default profile under open-ended text contracts](./042-register-becomes-a-default-profile-under-open-ended-text-contracts.md) — supersedes: replaces only its theory-definition placement while retaining its historical rename and local-contract decision
- [ADR 070: Notes bind choices; reference records selections and state](./070-notes-bind-choices-reference-records-selections-and-state.md) — see-also: supplies the collection-placement rule applied here
