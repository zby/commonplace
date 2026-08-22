---
description: COLLECTION.md-bearing subtree under kb/ whose local authoring contract governs its artifacts; top-level collections also provide a README landing
type: kb/types/definition.md
tags: []
---

# Collection

A **collection** in a Commonplace KB is a subtree under `kb/` whose root contains `COLLECTION.md`. `COLLECTION.md` is the local authoring contract for artifacts in that subtree. It usually defines the collection's purpose, register or content mode, quality goal, type guidance, and outbound-link policy.

A collection directly under `kb/` also has a `README.md` as its curated reader landing. The README routes readers but does not replace the binding `COLLECTION.md` contract. It must not coexist with a sibling `index.md`, because both render to the same directory URL and `index.md` shadows the README. `commonplace-validate landings` enforces this invariant for collection roots that are direct children of `kb/`; ordinary area directories still inherit their enclosing collection's contract and need no landing of their own.

Collections can also have local type specs. When present, they live in a `types/` subdirectory at the collection root. Type specs are structural authoring contracts: they define artifact shape through schema, frontmatter requirements, required sections, and written guidance for filling that shape. `COLLECTION.md` can guide authors to both global type specs in `kb/types/` and local type specs in the collection's own `types/` directory; see [collections and types](../collections-and-types.md) for their use and resolution.

A descendant directory with no `COLLECTION.md` of its own is an area of the enclosing collection and inherits its contract, such as `kb/notes/definitions/`. A `COLLECTION.md` inside a non-collection namespace, such as `kb/commonplace/notes/` under `kb/commonplace/`, is an ordinary collection rather than a nested collection; a `COLLECTION.md` inside another collection is invalid.

Tools may also treat collections as operational units, but those roles vary by tool and remain secondary to the local authoring contract.

The current top-level source-repo collections are `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/articles/`, `kb/instructions/`, `kb/notes/`, `kb/reference/`, `kb/sources/`, `kb/types/`, and `kb/work/`. `kb/types/` is both the global type layer and a collection: its `COLLECTION.md` governs authoring and outbound links, while its type specs and schemas govern artifact structure and semantics. Installed projects expose selected shipped source collections under the `kb/commonplace/` namespace, such as `kb/commonplace/notes/`.

## Exclusions

These are not exceptions to the definition; they are common near-misses that do not have their own `COLLECTION.md`.

- `kb/commonplace/` is a namespace for shipped collections, not a collection.
- `kb/work/<workshop>/` directories are areas inside the `kb/work/` collection, governed by `kb/work/COLLECTION.md`.

## Misuse Cases

None recorded yet.

---

Relevant Notes:

- [Collections and types](../collections-and-types.md) — extends: describes path-valued type resolution and how collection-local type specs remain separate from collection authoring contracts
- [two-context-boundaries-govern-collection-operations](../../notes/two-context-boundaries-govern-collection-operations.md) — example: one operational role that collection boundaries can play for note collections
- [a functioning KB needs a workshop layer not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — contrasts: library collections vs workshop directories
- [why directories despite their costs](../../notes/why-directories-despite-their-costs.md) — rests-on: the general argument for directory-based organisation that collections make load-bearing
