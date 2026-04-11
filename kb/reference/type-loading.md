---
description: Commonplace's shipped type loading mechanism — global types in `kb/types/` (base types plus the cross-collection `definition` type), directory-scoped types in `kb/*/types/`, WRITING.md inlining, and how validation resolves type schemas
type: note
tags: [type-system]
status: current
---

# Type loading

How commonplace splits the shipped type system across a thin global layer and directory-scoped type directories. This note describes which types live where, how they load, and how `commonplace-validate-notes` looks them up.

## The two layers today

**Global types (`kb/types/`)**

| Type | File | Purpose |
|---|---|---|
| `text` | `kb/types/text.md` | No frontmatter — raw capture, always valid |
| `note` | `kb/types/note.md` + `note.template.md` + `note.schema.yaml` + `note-base.schema.yaml` | Has frontmatter with description — searchable, connectable, validatable |
| `definition` | `kb/types/definition.template.md` + `definition.instructions.md` + `definition.schema.yaml` | KB vocabulary note with Scope / Exclusions / Misuse Cases — authored from any collection that accumulates vocabulary |

`text` and `note` are the maturity-ladder base types that every [collection](./definitions/collection.md) (a top-level `kb/` subdirectory that owns its own type contract) depends on. `definition` lives globally for a different reason: it is a specialised type, but its authoring needs recur across collections — `kb/notes/definitions/` holds methodology vocabulary and `kb/reference/definitions/` holds shipped-system vocabulary — so duplicating the template and schema into each collection's local `types/` would buy nothing. Per [ADR-002](./adr/002-inline-global-types-in-writing-guide.md), only the `note` template is inlined into `kb/instructions/WRITING.md` so that agents writing ordinary notes get the template in the same context hop as the writing conventions. This covers the majority of writes.

**Directory-scoped types (`types/` under collection or workshop directories)**

Each collection or workshop can own its own specialised types:

- `kb/notes/types/` — `structured-claim`, `related-system`, `review`, `spec`, `index`
- `kb/sources/types/` — `source-review`, `ingest-report`
- `kb/reference/types/` — `adr`
- `kb/tasks/types/` — `task-backlog`, `task-active`, `task-recurring`
- `kb/reports/types/` — `connect-report`

Most types ship as three files: `{type}.template.md` (prose template), `{type}.instructions.md` (how to fill it in), and `{type}.schema.yaml` (machine-readable schema). A few still ship a subset — `review` and `spec` in `kb/notes/types/` currently have only the schema; the task types in `kb/tasks/types/` have templates and instructions without schemas. The direction of travel is the full three-file shape. Directory-local types only get loaded when the routing table points to them — the agent doesn't carry every specialised type in context on every invocation.

## Where structural expectations currently live

The thick structural expectations — what sections to write, what metadata to include — come from template and schema files, not from the type name in frontmatter alone:

| Structural expectation | Currently defined in | `type:` says |
|---|---|---|
| Core Ideas / Comparison / Borrowable Ideas | `kb/notes/types/related-system.*` | `related-system` |
| Context / Decision / Consequences | `kb/reference/types/adr.*` | `adr` |
| Goal / Tasks checklist / Current State | `kb/tasks/types/task-*.{template,instructions}.md` | `task-active` etc. |
| Classification / Summary / Connections Found / Extractable Value / Limitations | `kb/sources/types/ingest-report.*` | `ingest-report` |
| Evidence / Reasoning / Caveats | `kb/notes/types/structured-claim.*` | `structured-claim` |
| Scope / Exclusions / Misuse Cases | `kb/types/definition.*` | `definition` |
| Discovery Trace / Connections Found / Flags | `kb/reports/types/connect-report.*` | `connect-report` |

The `type:` field is authoritative for artifact identity, but the structural contract for each type is carried by its template and schema — most of them in a collection's `types/` directory, one (`definition`) in the global `kb/types/`. The name is a pointer; the files are the contract.

## How validation looks up definitions

`commonplace-validate-notes` resolves a note's type by reading the `type:` frontmatter and then finding the matching schema in the owning collection's `types/` directory. Per [ADR-015](./adr/015-standardize-authored-type-definitions-on-json-schema.md), schemas are authored JSON Schema in YAML. Per [ADR-012](./adr/012-types-for-structure-traits-for-review.md), the validator reads these schemas rather than carrying a hard-coded type-profile map — adding a new type is an authoring step, not a code change.

Collection-scoped lookup means a type name is scoped by where the note lives. Bare type names stay unambiguous as long as no two collections define the same type name with incompatible structure; qualified canonical ids were considered and deferred.

## The inlining exception

`note` is the one type whose template is inlined into always-loaded context (`kb/instructions/WRITING.md`) rather than loaded on demand. The rationale is frequency: most writes are plain notes, so the marginal cost of inlining the small template beats the cost of an extra tool call per write. [ADR-002](./adr/002-inline-global-types-in-writing-guide.md) also accepted inlining `structured-claim` for the same reason — its template is short and it's the second most common type — but `kb/instructions/WRITING.md` currently only contains the `note` template. The `structured-claim` side of that decision has not yet landed in the file.

Every other specialised type stays in its collection's `types/` directory and loads only when an agent is explicitly writing one. A skill or routing table line points at the specific template file (e.g., `kb/reference/types/adr.template.md`) rather than relying on the agent to remember every type definition.

## Open questions about current loading

- How should `/validate` surface directory-local expectations that aren't captured in the schema yet? A machine-readable schema in the directory is the current answer, but some conventions (e.g., tasks lifecycle) still live in prose READMEs.
- Does the `type:` frontmatter field stay useful as a search filter once directory scoping becomes load-bearing? `rg '^type: note'` still works today, but adding more directory-local type names could fragment the filter.
- Should `structured-claim` be formalised as a global type on the strength of its inlining, or stay a directory-local specialisation of `note`?

---

Relevant Notes:

- [type-system](./type-system.md) — the full type inventory and classification this note complements with loading-mechanism detail
- [002-inline-global-types-in-writing-guide](./adr/002-inline-global-types-in-writing-guide.md) — decision: inlining `note` into WRITING.md
- [012-types-for-structure-traits-for-review](./adr/012-types-for-structure-traits-for-review.md) — decision: types define structural requirements; directory-local `types/` scope definition lookup
- [015-standardize-authored-type-definitions-on-json-schema](./adr/015-standardize-authored-type-definitions-on-json-schema.md) — decision: JSON Schema in YAML as the authoring form for type definitions
- [016-custom-types-use-template-instruction-pairs](./adr/016-custom-types-use-template-instruction-pairs.md) — decision: specialised types use template + instructions files, with WRITING.md as the generic always-loaded guide
- [architecture](./architecture.md) — shipped architecture: where the type loading mechanism sits inside the installed surface
