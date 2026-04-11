---
description: Commonplace's shipped type loading mechanism — global base types in `kb/types/`, directory-scoped types in `kb/*/types/`, WRITING.md inlining, and how validation discovers definitions
type: note
tags: [type-system]
status: current
---

# Type loading

How commonplace splits the shipped type system across a thin global layer and directory-scoped type directories. This note describes which types live where, how they load, and how `commonplace-validate-notes` looks them up.

## The two layers today

**Global base types (`kb/types/`)**

| Type | File | Purpose |
|---|---|---|
| `text` | `kb/types/text.md` | No frontmatter — raw capture, always valid |
| `note` | `kb/types/note.md` + `note.template.md` + `note.schema.yaml` + `note-base.schema.yaml` | Has frontmatter with description — searchable, connectable, validatable |

These are the only types that cross every collection. `text` is the no-frontmatter root; `note` is the base for every structured document. Per [ADR-002](./adr/002-inline-global-types-in-writing-guide.md), the `note` template is inlined into `kb/instructions/WRITING.md` so that agents writing ordinary notes get the template in the same context hop as the writing conventions. This covers the majority of writes.

**Directory-scoped types (`types/` under collection or workshop directories)**

Each collection or workshop can own its own specialised types:

- `kb/notes/types/` — `structured-claim`, `adr` (being moved), `related-system`, `review`, `spec`, `index`
- `kb/sources/types/` — `source-review`, `ingest-report`
- `kb/reference/types/` — `adr` (after the sub-effort 1 move lands)
- `kb/tasks/types/` — `task-backlog`, `task-active`, `task-recurring`
- `kb/reports/types/` — `connect-report`

Each type ships as three files: `{type}.template.md` (prose template), `{type}.instructions.md` (how to fill it in), and `{type}.schema.yaml` (machine-readable schema). Directory-local types only get loaded when the routing table points to them — the agent doesn't carry every specialised type in context on every invocation.

## Where structural affordances currently live

The thick structural expectations — what sections to write, what metadata to include — come from directory-local templates, not from the global type field:

| Structural expectation | Currently defined in | Global `type:` says |
|---|---|---|
| Core Ideas / Comparison / Borrowable Ideas | `related-systems/` template + schema | `related-system` |
| Context / Decision / Consequences | `adr/` template + schema | `adr` |
| Goal / Tasks checklist / Current State | `tasks/` type templates | `task-active` etc. |
| Classification / Summary / Connections Found / Extractable Value / Limitations | `sources/` ingest-report template + schema | `ingest-report` |
| Evidence / Reasoning / Caveats | `structured-claim` template | `structured-claim` |
| Discovery Trace / Connections Found / Flags | `reports/` connect-report template + schema | `connect-report` |

The `type:` field is authoritative for artifact identity, but the structural contract for each type is carried by the template and schema in the collection's `types/` directory, not by a global definition.

## How validation looks up definitions

`commonplace-validate-notes` resolves a note's type by reading the `type:` frontmatter and then finding the matching schema in the owning collection's `types/` directory. Per [ADR-015](./adr/015-standardize-authored-type-definitions-on-json-schema.md), schemas are authored JSON Schema in YAML. Per [ADR-012](./adr/012-types-for-structure-traits-for-review.md), the validator reads these schemas rather than carrying a hard-coded type-profile map — adding a new type is an authoring step, not a code change.

Collection-scoped lookup means a type name is scoped by where the note lives. Bare type names stay unambiguous as long as no two collections define the same type name with incompatible structure; qualified canonical ids were considered and deferred.

## The inlining exception

`note` is the one type whose template is inlined into always-loaded context (`kb/instructions/WRITING.md`) rather than loaded on demand. The rationale is frequency: most writes are plain notes, so the marginal cost of inlining the small template beats the cost of an extra tool call per write. `structured-claim` is the other candidate for inlining because its template is short and it's the second most common type, though this is not finalised.

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
