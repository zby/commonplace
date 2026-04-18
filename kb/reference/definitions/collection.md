---
description: Top-level kb/ subdirectory that groups authored artifacts sharing a domain, owns or inherits a type contract, and is the unit at which operational context-budgeting decisions (validation, areas, boundary reasoning) are made
type: definition
tags: []
status: seedling
---

# Collection

A **collection** in commonplace is a top-level subdirectory of `kb/` that groups authored artifacts sharing a domain, owns or inherits a type contract, and is the unit at which operational context-budgeting decisions (validation, areas, boundary reasoning) are made. The current collections include `kb/notes/`, `kb/reference/`, `kb/instructions/`, `kb/agent-memory-systems/`, `kb/sources/`, `kb/tasks/`, `kb/work/`, and `kb/reports/`. The term sharpens ordinary directory talk by naming the level at which those responsibilities line up.

## Scope

A directory is a collection when three properties co-occur:

1. **Top-level placement under `kb/`.** Sub-directories inside a collection (e.g. `kb/notes/related-systems/`, `kb/notes/definitions/`) are *areas*, not collections — they inherit the collection's type contract and participate in its context boundaries rather than defining their own.
2. **Type contract.** A collection owns or inherits a type contract. Typically this is a `types/` directory at `kb/<collection>/types/` holding directory-scoped type definitions per [ADR-012](../adr/012-types-for-structure-traits-for-review.md); a collection may also satisfy the property by inheriting directly from the global `kb/types/` layer via fallback. The type resolver walks from an artifact's path through the collection's `types/` and finally to the global `kb/types/`; a collection is the level at which that walk first looks for specialised definitions.
3. **Operational unit for context budgeting.** A collection is the unit at which operational context-budget decisions are made — orientation, `/connect` discovery, area splits. For note collections, this is made concrete by the full-text boundary and index boundary described in [two-context-boundaries-govern-collection-operations](../../notes/two-context-boundaries-govern-collection-operations.md); the same framing extends by analogy to other collections whose operational budgets differ in shape but are still reasoned about at the collection level.

## Exclusions

- **Workshops (`kb/work/<workshop>/`)** are not collections. A workshop is a named temporal workspace for work-in-flight artifacts whose value is consumed rather than accumulated. Only directories under `kb/work/` count as workshops in the sense excluded here; `kb/tasks/` remains a library collection even though its contents have workshop-like lifecycles. Workshops can own their own `types/` directory through the same scoped-lookup mechanism and therefore sit on one of the three properties above, but their lifecycle and boundary behaviour differ — library-collection boundary analysis does not transfer to them. See [a functioning KB needs a workshop layer not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md).
- **Framework type surface (`kb/types/`)** is not a collection. It holds global type contracts, not authored notes subject to collection-level validation or boundary reasoning.
- **Areas within a collection** are not themselves collections. `kb/notes/related-systems/` and `kb/notes/definitions/` are areas inside the notes collection; they share its type contract and count against its boundaries.
- **Arbitrary top-level directories.** Creating an empty directory under `kb/` does not make it a collection. The three properties above have to hold in practice — authored content, a local type contract (or inheritance from the global layer via fallback), and recognition as a unit for boundary reasoning.

## Misuse Cases

- Treating `kb/work/<workshop>/` as a collection and applying library-collection boundary analysis to it. Workshops have expiring content and produce library artifacts; their full-text/index ratios are not load-bearing the way a library collection's are.
- Calling `kb/notes/definitions/` "the definitions collection." It is an area inside the notes collection. Its notes validate against the notes collection's (now globally-resolved) `definition` type, and they count against the notes collection's context boundaries.
- Using "collection" interchangeably with "directory." Every collection is a directory; not every directory is a collection. The term carries the implication that the three properties hold.
- Listing `kb/types/` in an enumeration of collections because it sits at the same level under `kb/`. It is a framework type surface — name it explicitly as such, not as a collection.

---

Relevant Notes:

- [type-loading](../type-loading.md) — extends: describes the type contract each collection owns and how the resolver walks from a collection's `types/` to the global layer
- [available-types](../available-types.md) — extends: the shipped type inventory that collections instantiate
- [two-context-boundaries-govern-collection-operations](../../notes/two-context-boundaries-govern-collection-operations.md) — grounds: the full-text/index boundary analysis for note collections that the "operational unit for context budgeting" property generalizes from
- [a functioning KB needs a workshop layer not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — contrasts: library collections vs workshop directories
- [why directories despite their costs](../../notes/why-directories-despite-their-costs.md) — grounds: the general argument for directory-based organisation that collections make load-bearing
