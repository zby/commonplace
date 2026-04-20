# Plan — path-valued types: whole-KB migration

## Context

The workshop's initial direction was `commonplace-resolve-type`, a CLI that reassembled (template + instructions + schema) for a `(type, collection)` pair at write time. That direction is dropped. See [`README.md`](./README.md) for the shape we landed on instead: `type:` becomes a path to a hand-authored instructions doc; the write skill composes ordinary repository files at read time; no resolver CLI, no compiler, no generated write-context packet.

This is no longer an `adr` pilot. The implementation should move the repo from enum-valued types to path-valued types in one migration bundle. Git is the rollback mechanism: if the migration fails, revert the bundle rather than carrying old and new type mechanisms side by side.

## Migration scope

- Every explicit frontmatter `type:` value in `kb/**/*.md` is rewritten from an enum string to a path.
- Every current type contract in `kb/**/types/` is represented as a `*.md` type instruction doc.
- `*.template.md` and `*.instructions.md` sidecars are absorbed and removed; `*.schema.yaml` files remain.
- `cp-skill-write`, validation, and reference docs are updated in the same migration bundle.

## Decisions fixed before implementation

- No committed mixed state. Implementation may use local mechanical phases, but the committed result should switch type docs, corpus frontmatter, validator behavior, and write-skill instructions together.
- No enum-to-path redirect table. After the migration, explicit `type:` values are paths. Enum values such as `type: adr`, `type: note`, or `type: snapshot` are validation errors.
- `type:` paths are repo-relative markdown paths under `kb/`: they must start with `kb/`, end with `.md`, must not contain `..`, and must not be absolute paths or URLs.
- Schema remains separate from authoring prose. Every type instruction doc must declare a `schema:` frontmatter field. The value is a repo-relative path to the schema file, or `null` when the type has no schema.
- `*.template.md` and `*.instructions.md` sidecars are absorbed into `*.md` type instruction docs. No old template/instruction sidecar mechanism remains after the migration.
- Collection type offerings use a readable, regular section in `COLLECTION.md`:

```markdown
## Types

- `adr` -> `kb/reference/types/adr.md`
  Use for architecture decision records.
```

## Implementation policy addendum

These policies are fixed before implementation so the migration does not invent behavior mid-flight.

- Note frontmatter does not gain new fields. A typed note carries a single explicit pointer:

```yaml
type: kb/reference/types/adr.md
```

- Type instruction docs carry type metadata:

```yaml
---
type: kb/types/type-instructions.md
name: adr
description: Architecture decision record for accepted or proposed system decisions
schema: kb/reference/types/adr.schema.yaml
---
```

- `schema:` is required on every type instruction doc. Use `schema: null` for types with no schema.
- The resolver loads the note's `type:` path, parses the type instruction doc, and derives all runtime metadata from that doc. Internally it may expose the note's type path, the type doc path, the type doc `name`, and the declared schema path, but none of those become note-frontmatter fields.
- The internal `TypeProfile` should distinguish storage identity and validation target. Expected fields are:
  - `type_path`: repo-relative path stored in note frontmatter, for example `kb/reference/types/adr.md`
  - `type_doc_path`: resolved filesystem path to the type instruction doc
  - `type_name`: name from the type instruction doc frontmatter, for example `adr`
  - `schema_path`: resolved filesystem path to the declared schema, or `None` when `schema: null`
  - `schema`: loaded schema mapping, or `None`
- Schema `frontmatter.type.const` values must be migrated to path constants when the schema validates typed frontmatter. Example: `const: adr` becomes `const: kb/reference/types/adr.md`.
- Type-gated review metadata such as `requires-type:` must migrate to path values too. Example: `requires-type: definition` becomes `requires-type: kb/types/definition.md`.
- Explicit `type: text` is invalid after migration. `text` remains the implicit no-frontmatter case only. Existing explicit text-typed files must either lose frontmatter if they are truly raw text, or migrate to a real type path if they carry metadata.
- Frontmatter-bearing artifacts must have an explicit path-valued `type:`. A file with YAML frontmatter but no `type:` is invalid after migration; only files with no frontmatter at all remain implicit `text`.
- The current explicit `type: text` source file (`kb/sources/psychology-solves-ai-memory-identity-construction-2025307030651871631.md`) carries metadata and should migrate to `type: kb/sources/types/snapshot.md`.
- `kb/types/text.md` remains documentation for the implicit no-frontmatter type. It is not an explicit type instruction doc, is not listed in collection `## Types`, and `type: kb/types/text.md` is invalid in artifact frontmatter.
- Source artifacts now use the reduced source type set. `snapshot`, `ingest-report`, and `source-review` get type instruction docs under `kb/sources/types/`, with schemas where present and `schema: null` only when no real schema exists.
- `kb/sources/` and `kb/reports/` are generated artifact areas, not normal `cp-skill-write` targets. They still need type docs for validation, but they do not need `COLLECTION.md` type-offering sections unless their authoring workflow changes.
- `kb/tasks/` is not part of the shipped scaffold today, but it has existing task type sidecars. Migrate those contracts too: create `task-active`, `task-backlog`, and `task-recurring` type instruction docs under `kb/tasks/types/` with `schema: null` unless real schemas are added in the same bundle. Do not add `kb/tasks/COLLECTION.md` unless tasks become a normal `cp-skill-write` target in this migration.
- The shipped scaffold and init tests migrate in the same bundle. Newly initialized projects must ship type instruction docs, not absorbed `*.template.md` / `*.instructions.md` sidecars.
- Type instruction docs are first-class validation targets even though ordinary batch note discovery currently skips `types/` directories. The migration must add an explicit type-doc validation path, or widen batch validation deliberately, so malformed `kb/**/types/*.md` files cannot pass unnoticed.
- Type-aware readers must compare path-valued type identities. Any code that currently does `frontmatter["type"] == "index"` or similar must either compare against the canonical path (`kb/types/index.md`) or resolve through `TypeProfile`; do not leave enum comparisons in active behavior.

## Step 1: Inventory all current types

Pre-action gate: save the inventory in the PR/workshop notes before editing.

- Use the frontmatter parser, not raw grep, to list every explicit `type:` value in `kb/**/*.md`.
- Use the filesystem to list every existing type sidecar in `kb/**/types/`: `*.template.md`, `*.instructions.md`, and `*.schema.yaml`.
- Build the complete enum-to-path migration table from those two sources.
- Save the preflight inventory as a workshop artifact before editing. It must include:
  - every explicit frontmatter type value and the number of files using it
  - the target type instruction doc path for each value
  - the target schema path or `null`
  - whether the type has existing template/instructions sidecars, schema-only support, no sidecar, or is implicit text
  - the migration action for explicit `type: text` files
  - generated or non-write-target classifications, especially source artifact types
- The inventory from 2026-04-20 has 13 explicit frontmatter type values: `adr`, `agent-memory-system-review`, `connect-report`, `definition`, `index`, `ingest-report`, `instruction`, `note`, `snapshot`, `source-review`, `spec`, `structured-claim`, `text`.

## Step 2: Create the root type-instructions doc

Pre-action gate: review before applying the full migration.

- Create `kb/types/type-instructions.md`.
- Frontmatter: `type: kb/types/type-instructions.md` (self-reference); `name: type-instructions`; `description: …`; `schema: null`.
- Body: what makes a valid type-instructions doc — required frontmatter fields (`type`, `name`, `description`, `schema`), body expectations (authoring prose plus an inlined template or an explicit "no dedicated template" statement), and relationship to declared schema files.
- Include a short template for new type docs as an inlined fence.
- This file is the validator's terminator: when resolution reaches path-equals-self, stop.

## Step 2.5: Reconcile decision docs with schema-pointer policy

Pre-action gate: no validator work until the workshop docs agree on schema lookup policy.

- Update [`README.md`](./README.md) and [`adr-018-draft.md`](./adr-018-draft.md) so they match this plan's explicit `schema:` policy.
- Remove or revise sibling-schema language such as "`kb/reference/types/adr.md` maps to `kb/reference/types/adr.schema.yaml` when that file exists."
- State the final rule consistently: the type instruction doc declares `schema:`; the validator uses that field; sibling naming is only a convention authors may choose, not a resolver fallback.
- Keep `schema: null` as the only way to declare a type instruction doc with no schema validation.

## Step 3: Fuse every existing type contract

Pre-action gate: review representative fused docs from each family before applying the full mechanical pass.

- For every existing `{type}.template.md` / `{type}.instructions.md` pair, create `{type}.md` in the same type directory:
  - frontmatter: `type: kb/types/type-instructions.md`, `name: <type>`, `description: …`, `schema: <repo-relative schema path or null>`
  - body: existing instructions prose
  - template: existing template in an inline `~~~markdown` fence
- For schema-only types, create a minimal type-instructions doc that explains the type and states whether it has no dedicated authoring template.
- For frontmatter type values that currently have no sidecar, create minimal type-instructions docs in the owning collection's `types/` directory. Source artifact types live under `kb/sources/types/`.
- For task sidecar-only types under `kb/tasks/types/`, create type instruction docs and absorb their templates/instructions even though no task artifacts currently declare those types in frontmatter.
- Delete absorbed `*.template.md` and `*.instructions.md` sidecars in the same migration. Leave sibling `*.schema.yaml` files in place.
- Existing global types become `kb/types/<type>.md`; collection-local types remain under `kb/<collection>/types/<type>.md`.
- Existing `kb/types/note.md` is not kept as an old-style note about notes. It becomes the canonical `note` type instruction doc with `type: kb/types/type-instructions.md`, `name: note`, and `schema: kb/types/note.schema.yaml`.
- Existing `kb/types/text.md` remains documentation for the implicit no-frontmatter type. Do not convert it into an explicit type instruction doc, and do not allow `type: kb/types/text.md` in artifact frontmatter.

## Step 4: Declare offered types in collection conventions

Pre-action gate: review each `COLLECTION.md` type section before applying the full migration.

- Add or update `## Types` sections in collections that accept writes: `kb/notes/COLLECTION.md`, `kb/reference/COLLECTION.md`, `kb/instructions/COLLECTION.md`, `kb/agent-memory-systems/COLLECTION.md`, and `kb/work/COLLECTION.md`.
- List global types when the collection offers them for new writes, for example `note`, `index`, `definition`, and `instruction`.
- List collection-local types where relevant, for example `structured-claim`, `adr`, and `agent-memory-system-review`.
- Do not add `COLLECTION.md` type-offering sections for `kb/sources/` or `kb/reports/` in this migration. They are generated artifact areas with validation type docs, not normal `cp-skill-write` targets.
- Do not add `kb/tasks/COLLECTION.md` in this migration unless task writing is deliberately brought under `cp-skill-write`.

## Step 5: Rewrite all corpus frontmatter

Pre-action gate: show the exact enum-to-path replacement table and the count of files affected per type.

- Rewrite every explicit frontmatter `type:` enum to its path-valued type doc.
- Rewrite only YAML frontmatter, not examples, code fences, templates embedded in prose, or historical discussion.
- Treat explicit `type: text` as invalid input to resolve during migration. The one current explicit text-typed source carries metadata and should migrate to `type: kb/sources/types/snapshot.md`.
- Examples:
  - `type: note` -> `type: kb/types/note.md`
  - `type: instruction` -> `type: kb/types/instruction.md`
  - `type: adr` -> `type: kb/reference/types/adr.md`
  - `type: structured-claim` -> `type: kb/notes/types/structured-claim.md`
  - `type: snapshot` -> `type: kb/sources/types/snapshot.md`
- After this step, no explicit frontmatter `type:` value in `kb/**/*.md` should be a bare enum.

## Step 6: Update `cp-skill-write/SKILL.md`

Pre-action gate: review the rewritten skill before applying the full migration.

- Replace Step 1 type-discovery prose with file-native instructions: read the path named by `type:` in edit mode, or read the target collection's `## Types` section in new-write mode, then open the selected type instruction file.
- Remove the inline default `note` template. `note` is now a normal global type instruction doc at `kb/types/note.md`.
- Do not document or implement legacy enum fallback.
- Keep the hard-fail rule for missing `COLLECTION.md`.
- Keep search and validation procedural; the type file supplies artifact shape, not search policy.

## Step 6.5: Update other writers, readers, and type-aware skills

Pre-action gate: inventory every non-validator code path and skill that writes, reads, or compares `type:`.

- Update artifact-generating commands that currently emit enum frontmatter:
  - `src/commonplace/cli/github_snapshot.py`: `type: snapshot` -> `type: kb/sources/types/snapshot.md`
  - `src/commonplace/cli/x_snapshot.py`: `type: snapshot` -> `type: kb/sources/types/snapshot.md`
  - `src/commonplace/lib/index_directory.py`: `type: index` -> `type: kb/types/index.md`
- Search `src/` for generated markdown frontmatter and migrate any additional `type:` literals found during implementation.
- Search `src/` for type-value consumers, not just writers. Update direct enum comparisons and filters, including:
  - `src/commonplace/lib/index_generated.py`: `fm.get("type") == "index"` and `fm.get("type") != "index"` must use the path-valued index type or a path-aware helper.
  - `src/commonplace/docs/mkdocs_hooks.py`: tag-index discovery must recognize `type: kb/types/index.md`.
  - any additional `get("type")`, `note_type`, `resolved_type`, or `definition_path` usage discovered during implementation.
- Update non-write skills and instructions that point at absorbed sidecars:
  - `cp-skill-connect`: read `kb/reports/types/connect-report.md`, not `.template.md`
  - `cp-skill-ingest`: read `kb/sources/types/ingest-report.md`, not `.template.md` / `.instructions.md`
  - `cp-skill-convert`: verify and write path-valued note/structured-claim types, not enum values
  - `cp-skill-snapshot-web`: emit or describe `kb/sources/types/snapshot.md`
  - any other instruction discovered by searching for `.template.md`, `.instructions.md`, `type: note`, `type: snapshot`, or `type: structured-claim`
- Keep historical prose in ADRs and theory notes only when it is clearly describing pre-migration behavior; update operational procedures and examples.

## Step 7: Update validation and docs

Pre-action gate: show the validator diff and tests before applying the full migration.

- `commonplace-validate` treats explicit `type:` values as paths.
- A valid type path must exist, point under `kb/`, end with `.md`, and resolve to a type-instructions doc.
- A type-instructions doc is valid when its own `type:` points to `kb/types/type-instructions.md`, except the root doc, which points to itself.
- A type-instructions doc must include `name`, `description`, and `schema`. `schema` must be either `null` or a valid repo-relative path under `kb/` to an existing `.schema.yaml` file.
- The validator loads schemas from the type instruction doc's `schema:` field. Missing `schema:` is a validation error for the type instruction doc; `schema: null` means no schema validation for artifacts of that type.
- Schema constants for `frontmatter.type` must match path-valued type references, not old enum names.
- Frontmatter with no `type:` is a validation error. Preserve implicit `text` only for files with no frontmatter.
- Remove enum fallback behavior from validation for explicit frontmatter `type:` values.
- Remove collection-scoped enum lookup from explicit frontmatter validation. The note's path chooses the type doc directly; the collection no longer participates in resolving an explicit type.
- Keep collection/type uniqueness checks only if they still prove something useful in the path-valued system. Otherwise replace them with checks that type doc paths are valid.
- Preserve the existing behavior that a file with no frontmatter is `text` if that behavior is still needed for raw text artifacts; this is not an enum fallback. Explicit frontmatter `type: text` fails.
- Add explicit validation coverage for type instruction docs under `kb/**/types/*.md`. Current note discovery skips `types/` directories; either introduce a separate `validate_type_instruction_docs` pass or deliberately include type docs in batch validation with clear filtering for non-artifact side files.
- Update review type gates (`requires-type`) to path values or equivalent path-aware matching; do not leave enum matching against note frontmatter.
- Update active type-aware readers such as generated-index syncing and MkDocs tag-index discovery so they recognize path-valued type references.
- Update reference docs: commands, type loading, available types, collections/types, and any ADR/reference page that describes enum-valued types or three-file type contracts.
- Update scaffold/init expectations so `commonplace-init` seeds type instruction docs and no absorbed template/instruction sidecars.
- Migrate test helpers and fixtures that create typed markdown so they use path-valued frontmatter unless the test is explicitly asserting that a bare enum fails.
- Tests: path-valued type resolves; declared schema is used; `schema: null` skips schema validation; missing `schema` fails for type docs; type docs under `kb/**/types/*.md` are validated; missing type file fails; invalid type path fails; self-reference terminates; missing `type:` in frontmatter fails; bare enum frontmatter fails; explicit `type: text` fails; unknown explicit type no longer falls back to `note`; collection-local enum lookup is gone for explicit frontmatter; generated snapshot and index commands emit path-valued types; generated-index syncing and MkDocs tag-index discovery recognize path-valued `index`; review `requires-type` matching works with paths; init/scaffold tests assert type instruction docs are seeded and absorbed sidecars are absent.

## Step 8: Validate the migrated repo

Pre-action gate: no commit until the validation result is understood.

- Run `uv run pytest`.
- Run the KB validator over the migrated corpus.
- Search for remaining bare enum frontmatter values with the same parser used in Step 1.
- Search for schema `frontmatter.type.const` values that still reference bare enum names.
- Search for `requires-type:` values that still reference bare enum names.
- Search for remaining `*.template.md` and `*.instructions.md` files under `kb/**/types/`; none should remain unless explicitly justified as non-type historical material.
- Search operational code and promoted skills for stale sidecar references and enum-writing examples:
  - `rg -n "\.template\.md|\.instructions\.md|type: (note|index|definition|instruction|adr|structured-claim|agent-memory-system-review|connect-report|snapshot|ingest-report|source-review|spec|text)\b|requires-type: (note|index|definition|instruction|adr|structured-claim|agent-memory-system-review|connect-report|snapshot|ingest-report|source-review|spec|text)\b|get\(\"type\"\).*==|get\(\"type\"\).*!=" src test kb AGENTS.md README.md`
- Treat historical ADR/theory prose as acceptable only when it clearly describes pre-migration behavior. Active instructions, reference docs, root control-plane docs, scaffolded files, tests, generated examples, and scenario docs must not retain stale operational sidecar paths or enum-valued examples.
- Search active code for direct enum type comparisons and path-model field names that should have changed:
  - `rg -n "get\(\"type\"\)|note_type|resolved_type|definition_path|check_type_uniqueness|discover_all_types" src test`
- Run or update `commonplace-init` scaffold tests to prove new projects receive the migrated type-doc surface.
- If the migrated state fails, fix forward in the same migration bundle or revert the bundle. Do not introduce a compatibility layer.

## Not changing

- Canonical sources of authoring contracts stay hand-authored. No compiler, no build step.
- Schema files stay separate from authoring prose, but their paths are declared in type instruction frontmatter.
- Linking conventions stay in `cp-skill-write/SKILL.md` (global) + `COLLECTION.md` (per-collection). They are not injected into type docs.
- `COLLECTION.md` hard-fail rule stays.

## Deferred / out of scope

- A `commonplace-mv-type` command that rewrites every pointer when a type doc moves. Worth building when the first rename happens; not needed for the migration.
- A compiled type-index doc (`kb/types/index.md`) for discoverability. Optional; globbing over `kb/**/types/*.md` plus `COLLECTION.md` listings suffices for now.
- Broader schema metadata beyond the required `schema:` pointer.

## Success criteria

- Every explicit frontmatter `type:` in the KB is a valid path to a type instruction doc.
- No authoring type contract remains split across `*.template.md` and `*.instructions.md`.
- `cp-skill-write` can author a note, instruction, ADR, and structured claim by reading ordinary repository files rather than running a resolver or following filesystem-discovery prose.
- The full test suite and KB validation pass.

## Closure

This workshop closes when:

- The whole-KB migration lands.
- [`adr-018-draft.md`](./adr-018-draft.md) moves to `kb/reference/adr/` and flips `status: proposed` -> `accepted`.
- Any follow-up work is limited to refinements, not compatibility with enum-valued `type:`.
