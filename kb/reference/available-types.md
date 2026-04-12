---
description: Catalog of the types shipped by commonplace — the global base types, the global `definition` type, and the directory-scoped specialised types delivered with the framework scaffold
type: note
tags: []
status: current
---

# Available Types

The shipped commonplace scaffold installs one small set of global types plus a handful of directory-scoped specialised types under the collections it ships. This page lists them and says where each type's contract files live. For the mechanism that loads those files at authoring or validation time, see [type-loading](./type-loading.md).

A document has exactly one type. [text](../types/text.md) has no frontmatter and no requirements. Every other shipped type extends [note](../types/note.md), which defines the shared fields (`description`, `status`, `traits`, `tags`) that structured documents carry.

The `type:` frontmatter field is a free-form string — it is not validated against an enum, so consuming projects can add new types locally by dropping a template, instructions, and schema into the owning collection's `types/` directory. This page documents only the types the scaffold itself ships.

## Global types (`kb/types/`)

| Type | Files | Purpose |
|---|---|---|
| `text` | `text.md` | No frontmatter — raw capture, always valid. The root of the type ladder. |
| `note` | `note.md`, `note.template.md`, `note.schema.yaml`, `note-base.schema.yaml` | Base structured type. Requires a non-empty `description`; carries shared `status`, `traits`, `tags`. Every specialised type inherits its frontmatter shape from here. |
| `definition` | `definition.template.md`, `definition.instructions.md`, `definition.schema.yaml` | Vocabulary note with `Scope`, `Exclusions`, and `Misuse Cases` sections. |
| `index` | `index.template.md`, `index.instructions.md`, `index.schema.yaml` | Navigation hub: directory listings or curated tag indexes with generated tails. |

`text` and `note` are the maturity-ladder base types that every [collection](./definitions/collection.md) depends on. `definition` and `index` are also global because they can occur in any collection — duplicating the template and schema into each collection's local `types/` would buy nothing.

Per [ADR-002](./adr/002-inline-global-types-in-writing-guide.md), the `note` template is inlined into each collection's `COLLECTION.md` so that agents writing ordinary notes get the template in the same context hop as the writing conventions.

## Directory-scoped types

Each shipped collection owns its own specialised types under a local `types/` directory. Directory-scoped types are only loaded when the agent is working in that collection.

### `kb/reference/types/` — shipped-system documentation

| Type | Files | Structural contract |
|---|---|---|
| `adr` | template + instructions + schema | Architecture decision record: `Context`, `Decision`, `Consequences` |

### `kb/sources/types/` — ingested sources

| Type | Files | Structural contract |
|---|---|---|
| `source-review` | template + instructions + schema | Structured extraction and evaluation of an external source |
| `ingest-report` | template + instructions + schema | Ingest workflow report: classification, summary, connections, extractable value, limitations |

### `kb/reports/types/` — generated snapshots

| Type | Files | Structural contract |
|---|---|---|
| `connect-report` | template + instructions + schema | Connection report: discovery trace, connections found, flags |

The other shipped collections — `kb/instructions/` and `kb/work/` — carry no specialised types of their own. `kb/instructions/` holds imperative how-to content, and `kb/work/` is a workshop layer for temporal, work-in-flight documents where type extensions are expected to be defined locally per workshop as needed.

## Types versus traits

Traits are a separate axis from type. They do not define structure; they declare semantic review expectations. See [note base type](../types/note.md) for the shipped trait vocabulary, and [ADR-012](./adr/012-types-for-structure-traits-for-review.md) for the reasoning behind the split.

---

Relevant Notes:

- [type-loading](./type-loading.md) — how these type definitions are resolved at authoring and validation time
- [note base type](../types/note.md) — defines the global fields, status ladder, traits, and design principles
- [text root type](../types/text.md) — the empty root type: no frontmatter, always valid
- [013-skills-first-delivery-with-core-local-type-split](./adr/013-skills-first-delivery-with-core-local-type-split.md) — decision: framework types and local example types have different packaging roles
- [012-types-for-structure-traits-for-review](./adr/012-types-for-structure-traits-for-review.md) — decision: structural types and review traits are separate axes
- [015-standardize-authored-type-definitions-on-json-schema](./adr/015-standardize-authored-type-definitions-on-json-schema.md) — decision: the current authored type-definition format
