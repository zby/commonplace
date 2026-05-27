---
description: COLLECTION.md-bearing subtree under kb/ whose local authoring and routing contract tells agents how to write, connect, validate, and maintain artifacts in that subtree
type: kb/types/definition.md
tags: []
status: seedling
---

# Collection

A **collection** in a Commonplace KB is a subtree under `kb/` whose root contains `COLLECTION.md`. `COLLECTION.md` is the local authoring contract for that subtree: agents read it before writing, connecting, or maintaining the artifacts inside.

The contract usually defines the collection's purpose, register or content mode, quality goal, type guidance, and outbound-link policy. `cp-skill-write` uses this contract to draft and connect new artifacts. `cp-skill-connect` uses it to decide which destinations to prospect and which labels are authorised.

Collections can also have local type specs. When present, they live in a `types/` subdirectory at the collection root. Type specs are structural authoring contracts: they define artifact shape through schema, frontmatter requirements, required sections, and written guidance for filling that shape. `COLLECTION.md` can guide authors to both global type specs in `kb/types/` and local type specs in the collection's own `types/` directory; see [type-loading](../type-loading.md) for the resolution mechanics.

Descendant directories are normally areas inside the collection and inherit its contract. A descendant directory that also carries `COLLECTION.md` is outside the current collection model; nested collection semantics are reserved until deliberately designed.

The current source-repo collections include `kb/notes/`, `kb/reference/`, `kb/instructions/`, `kb/agent-memory-systems/`, `kb/sources/`, and `kb/work/`. Installed projects expose selected shipped source collections under the `kb/commonplace/` namespace, such as `kb/commonplace/notes/`.

## Exclusions

These are not exceptions to the definition; they are common near-misses that do not have their own `COLLECTION.md`.

- `kb/commonplace/` is a namespace for shipped collections, not a collection.
- `kb/types/` is the global type surface, not a collection.
- `kb/work/<workshop>/` directories are areas inside the `kb/work/` collection, governed by `kb/work/COLLECTION.md`.

## Misuse Cases

None recorded yet.

---

Relevant Notes:

- [type-loading](../type-loading.md) — extends: describes path-valued type resolution and how collection-local type specs remain separate from collection authoring contracts
- [available-types](../available-types.md) — extends: the shipped type inventory that collections instantiate
- [two-context-boundaries-govern-collection-operations](../../notes/two-context-boundaries-govern-collection-operations.md) — grounds: the full-text/index boundary analysis for note collections that the "operational unit for context budgeting" property generalizes from
- [a functioning KB needs a workshop layer not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — contrasts: library collections vs workshop directories
- [why directories despite their costs](../../notes/why-directories-despite-their-costs.md) — grounds: the general argument for directory-based organisation that collections make load-bearing
