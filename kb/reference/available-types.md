---
description: Catalog of the types shipped by commonplace — global base and utility types plus directory-scoped specialised types delivered with the framework scaffold
type: kb/types/note.md
tags: []
status: current
---

# Available types

The shipped commonplace scaffold installs global type specs under `kb/types/` and a small set of collection-local type specs for generated or specialized artifacts. Artifacts store the path to the selected type spec in `type:`.

## Global Types

| Type | Path | Use |
|---|---|---|
| `note` | `kb/types/note.md` | Base structured note with description, status, traits, and tags. |
| `instruction` | `kb/types/instruction.md` | Procedures, promoted skill bodies, wrapper prompts, work packets handed to sub-agents. |
| `review-gate` | `kb/types/review-gate.md` | A single quality check the review system applies to KB artifacts. |
| `definition` | `kb/types/definition.md` | Operational vocabulary definitions. |
| `index` | `kb/types/index.md` | Navigation hubs and generated directory or tag indexes. |
| `type-spec` | `kb/types/type-spec.md` | Metadata contract for type-spec docs themselves. |

`kb/types/text.md` documents the implicit no-frontmatter text case. It is not an explicit type spec and should not be used as a `type:` value.

## Collection-Local Types

| Type | Path | Use |
|---|---|---|
| `adr` | `kb/reference/types/adr.md` | Architecture decision records. |
| `structured-claim` | `kb/notes/types/structured-claim.md` | Developed arguments with Evidence and Reasoning sections. |
| `agent-memory-system-review` | `kb/agent-memory-systems/types/agent-memory-system-review.md` | Code-grounded external system reviews. |
| `snapshot` | `kb/sources/types/snapshot.md` | Captured external source copies. |
| `ingest-report` | `kb/sources/types/ingest-report.md` | Source ingestion analysis artifacts. |
| `source-review` | `kb/sources/types/source-review.md` | Structured source extraction notes. |
| `connect-report` | `kb/reports/types/connect-report.md` | Generated connection discovery reports. |

Task type specs also exist under `kb/tasks/types/` for existing task workflows, but tasks are not currently a normal `cp-skill-write` target.

## Related

- [type-loading](./type-loading.md) - resolution mechanics
- [collections-and-types](./collections-and-types.md) - collection/type composition
- [note](../types/note.md) - base note authoring contract
- [text](../types/text.md) - implicit no-frontmatter capture state
