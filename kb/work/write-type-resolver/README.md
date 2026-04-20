# Workshop: write-type-resolver

## Question

Should Commonplace migrate `type:` from an enum-string (`type: adr`) to a path-valued pointer (`type: kb/reference/types/adr.md`) that addresses a single hand-authored instructions doc per type?

## Why this workshop exists

The validator has Python type-resolution logic that checks the owning collection's `types/` directory first, then falls back to global `kb/types/`. The write skill currently mirrors that behavior in prose and expects the agent to discover `{type}.template.md` and `{type}.instructions.md` files through filesystem tools.

That arrangement is workable but brittle. The new global `instruction` type exposed the weakness: global types are loadable from `kb/types/`, but they do not choose a destination collection. The write skill now carries a special default (`instruction` → `kb/instructions/`), and future global types may need similar routing decisions.

**Initial direction (dropped).** A `commonplace-resolve-type` CLI that reassembled the (template + instructions + schema) triple for a requested (type, collection) pair. The CLI direction dissolved over the course of this workshop — when `type:` points directly at a hand-authored instructions doc, the resolver's runtime job disappears. This doc records the flip; the old plan is preserved in git history at commit before revision.

## Current behavior

`cp-skill-write` currently has these defaults and rules:

- new writes default to collection `notes` and type `note`
- `type: instruction` with no explicit collection defaults to collection `instructions`
- `note` uses an inlined template in the write skill
- non-default types are discovered by matching `{type}.template.md`
- collection-local templates can infer a collection when exactly one match exists
- global types in `kb/types/` do not infer collection
- missing `COLLECTION.md` is a hard failure

The validator's schema resolver lives in `src/commonplace/lib/type_resolver.py`. The write skill does not call a resolver command today.

## Proposed shape

**Path-valued types.** Every note's `type:` field holds the path of its instructions doc:

```yaml
type: kb/reference/types/adr.md
```

The field name stays `type:` — the semantic role ("what kind of artifact is this") is unchanged; only the encoding shifts from enum to path. Keeping the name communicates the role honestly and preserves habit.

Valid type paths are repository-relative markdown paths under `kb/`: they start with `kb/`, end with `.md`, contain no `..`, and are not absolute paths or URLs.

**Hand-authored instructions docs.** The pointed-at doc is self-contained. Body is authoring prose; template is an inlined fenced block (use `~~~markdown` or a longer backtick run so nested fences inside the template don't collide). Template sidecars are not preserved as an alternate authoring mechanism.

**Schema stays separate.** Writers don't need the schema. Validator schema lookup uses the sibling convention: `kb/reference/types/adr.md` maps to `kb/reference/types/adr.schema.yaml` when that file exists. Broader schema wiring remains a future validator workshop.

**No resolver CLI.** The write skill reads the path named by `type:` (in the note being edited) or the path named in the target collection's `COLLECTION.md` (for a new write). Ambiguity dissolves — paths are lexical. No `--collection` flag, no three-shape JSON contract, no `status: ambiguous` branch.

Collections declare offered types in a regular section:

```markdown
## Types

- `adr` -> `kb/reference/types/adr.md`
  Use for architecture decision records.
```

**No compiler.** Linking conventions are not injected into type docs. The write skill composes three inputs at read time: the skill's linking-vocabulary section (global, from ADR 009 + ADR 018), the type instructions doc (artifact shape), and the target collection's `COLLECTION.md` (register conventions, per-edge label rules). Composition happens in the agent, not on disk.

**Global types survive.** `note` (at `kb/types/note.md`) and `instruction` (at `kb/types/instruction.md`) live once and are pointed at from any collection. Per-collection linking rules stay where they already live in `COLLECTION.md`.

**Self-referential root.** `kb/types/type-spec.md` has `type: kb/types/type-spec.md` — its own spec. Validators terminate on path-equals-self.

## Migration shape

This is a whole-KB migration, not a pilot. The repo should not carry old and new type mechanisms side by side. See [`plan.md`](./plan.md) for the concrete steps.

Implementation moves all explicit frontmatter `type:` values to paths, creates/fuses all type instruction docs, removes template/instruction sidecars, updates the write skill and validator, and validates the migrated corpus. Git revert is the rollback path if the migration does not hold.

## What `write-type-resolver` no longer builds

- `commonplace-resolve-type` CLI.
- `AuthoringContract` / `AmbiguousType` / `UnresolvedType` dataclasses.
- `--list --json` enumeration command. Glob over `kb/**/types/*.md` plus `COLLECTION.md` listings suffice.

The note-template reconciliation between `kb/types/note.template.md` and `cp-skill-write/SKILL.md` happens inside the migration. `cp-skill-write` stops inlining the note template once `kb/types/note.md` is the canonical type instruction doc.

## Remaining checks

1. **Template-inlining limits.** Audit existing `*.template.md` files before migration. If any are too large or awkward to inline, revise the type-doc format before migrating rather than preserving template sidecars.
2. **Independence from the link-label workshop.** The two workshops share exactly one integration point (`cp-skill-write/SKILL.md`). Confirm they don't otherwise couple so they can land in either order.

## Relation to other work

- [link-label audit](../link-label-audit/) — shares the write skill as integration point only. Independent decisions.
- [ADR 018 (proposed) — types are path references to instruction docs](./adr-018-draft.md) — the types-as-paths decision. Drafted in this workshop; narrates current → pain points → resolver-CLI considered → path-reference accepted.
- [ADR 016 — custom types use template/instruction pairs](../../reference/adr/016-custom-types-use-template-instruction-pairs.md) — the three-file split this workshop proposes collapsing. This workshop's outcome (if accepted) extends or supersedes ADR 016.
- [ADR 015 — standardize authored type definitions on JSON schema](../../reference/adr/015-standardize-authored-type-definitions-on-json-schema.md) — schema-side decision; untouched by this workshop (schema stays separate).
- [ADR 002 — inline global types in writing guide](../../reference/adr/002-inline-global-types-in-writing-guide.md) — the `note`-inlined-template decision; this workshop retires it as part of the whole-KB migration.

## Closure criteria

This workshop closes when:

- The whole-KB migration lands end-to-end: type docs authored, corpus migrated, skill updated, validator handles path `type:`, tests and validation pass.
- [`adr-018-draft.md`](./adr-018-draft.md) moves to `kb/reference/adr/` and flips `status: proposed` → `accepted`.
