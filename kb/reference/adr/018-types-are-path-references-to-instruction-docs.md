---
description: "Replaces the enum `type:` field with a path reference to a single hand-authored instructions doc per type. Collapses the three-file-per-type layout (template / instructions / schema) into one authoring doc plus a sibling schema, and dissolves the filesystem-discovery, cross-collection ambiguity, and special-case routing problems that the current enum scheme forces onto the write skill."
type: ../types/adr.md
tags: []
status: accepted
---

# 018-Types are path references to instruction docs

**Status:** accepted
**Date:** 2026-04-19
**Supersedes (in part):** [ADR 016 — custom types use template/instruction pairs](./016-custom-types-use-template-instruction-pairs.md). Affects [ADR 002 — inline global types in writing guide](./002-inline-global-types-in-writing-guide.md) at the `note` migration step.
**Related:** [write-type-resolver workshop](../../work/write-type-resolver/README.md), [ADR 009](./009-link-relationship-semantics.md).

## Context

### Current type system

`commonplace-validate` and `cp-skill-write` treat `type:` as an enum. A note carries:

```yaml
type: adr
```

The name is resolved by probing the filesystem:

- `kb/<collection>/types/{type}.template.md` (collection-local)
- `kb/types/{type}.template.md` (global fallback)

Per [ADR 016](./016-custom-types-use-template-instruction-pairs.md), each type is expressed as a triple of sidecars:

- `{type}.template.md` — the body skeleton agents fill in
- `{type}.instructions.md` — authoring prose
- `{type}.schema.yaml` — validator schema

The validator has a Python resolver (`src/commonplace/lib/type_resolver.py`). The write skill does not call the resolver; it mirrors the same discovery logic in natural-language prose so the agent can probe the filesystem. Special cases live in the skill prose: `instruction` → `kb/instructions/`, `note` inlined in [ADR 002](./002-inline-global-types-in-writing-guide.md) style.

### Pain points

1. **Brittle filesystem discovery.** The write skill's type resolution is encoded as prose: Glob a template, infer collection from a unique match, fall back to global. Small mismatches between the prose and the validator's Python logic are silent failures.

2. **Cross-collection ambiguity.** Types like `review` exist in multiple collections (`kb/sources/types/review.template.md`, `kb/agent-memory-systems/types/review.template.md`). The write skill must ask the user to disambiguate, or guess from context. The prose-encoded rules don't handle this cleanly.

3. **Special-case routing for global types.** Global types in `kb/types/` don't name a destination collection. The skill carries a hardcoded default `instruction` → `kb/instructions/`. Future global types need similar entries, and the pattern doesn't generalize — every new global type is a skill edit.

4. **Three-file drift.** Template, instructions, and schema are separate files maintained by separate edits. `kb/types/note.template.md` has already drifted from the `note` template inlined in `cp-skill-write/SKILL.md` (different status value, different title hint, different "Open Questions" wording). Nothing structurally enforces consistency.

5. **Adding a new type is a tooling change.** Each new global default needs a skill edit; collection-local types require the collection to have a `types/` directory with the right filenames.

### Considered: a type-resolver CLI

The [write-type-resolver workshop](../../work/write-type-resolver/README.md) first proposed `commonplace-resolve-type --type X [--collection Y] --json`, which would:

- Discover the triple for `(type, collection)` at runtime.
- Return JSON shapes for resolved / ambiguous / not-found cases.
- Move type resolution out of skill prose into a single codepath shared with the validator.

This addresses pain point 1 (brittle prose) by collapsing the skill and validator onto one resolver, but leaves the others in place: ambiguity still needs a `--collection` flag and user disambiguation, the three-file layout still drifts, global-type routing still needs a lookup table baked into the CLI, and adding a type is still a filesystem-layout change plus (for globals) a tooling change. The CLI is a better interface to the same design — not a fix to the design.

It also makes the authoring interface less native to current coding agents. Claude Code, Codex, and similar IDE-based agents are strongest when instructions are expressed as files they can read, cache, cite, and follow. They already have robust primitives for "open this file, apply these instructions, edit these files, run this command." A JSON resolver response can tell an agent which files matter, but it still requires the skill prose to explain how to interpret the response. For authoring work, a direct file pointer is the simpler contract: the artifact names the instruction file; the agent reads it.

### Considered: a write-context resolver

The follow-on workshop direction broadened the resolver into `commonplace-write-context`: one command that would answer "what do I need to write this artifact correctly?" Instead of only resolving a type, it would return a structured authoring packet: collection conventions, type contract, linking context, search scope, validation context, and explicit unresolved states.

That shape is a better software abstraction than `commonplace-resolve-type`. It names the real job, keeps type resolution as a subroutine, and would let the write skill replace scattered prose with one CLI call.

It is still the wrong primary interface for current authoring agents. If the command returns JSON, the skill must teach the agent to interpret a machine-readable context object: which returned paths are mandatory, which warnings are soft, when to read topology, how to search, and how to combine those inputs. If the command instead generates markdown, the surface is friendlier but still nonstandard: the agent is reading a synthesized instruction artifact that is not a normal repository file, may not participate in IDE file caches the same way, and may diverge from the affordances IDE authors optimize for.

The file-reference design keeps the software's path-management role but changes the agent-facing contract. Instead of asking the agent to execute an authoring-context protocol or consume generated instructions, the system stores direct pointers to the canonical instruction files. The software validates those pointers and can support complete batch migrations; the agent reads ordinary repository files and follows prose. This matches normal IDE usage, file-based workflows, and caching behavior of coding agents more closely than either a JSON context packet or a generated markdown packet.

## Decision

Replace the enum `type:` field with a path reference to a single hand-authored instructions document per type.

### Shape

Every note's `type:` field holds the path of its instructions doc:

```yaml
type: ../types/adr.md
```

The field name stays `type:` — the semantic role ("what kind of artifact is this") is unchanged; only the encoding shifts from enum to path. Keeping the name preserves existing habit and captures the honest observation that the path *is* the richer form of the type's name.

The pointed-at file is self-contained:

- **Frontmatter** — `type:` (self-referential or pointing at a root spec), `name:`, `description:`.
- **Body** — authoring prose: when to use the type, what each section is for, what the artifact is for.
- **Template** — inlined fenced block (use `~~~markdown` or a longer backtick run so the template's own fences nest cleanly). Template sidecars are not preserved as an alternate authoring mechanism.

### What moves where

- **Template and instructions fuse into the pointed-at doc.** [ADR 016](./016-custom-types-use-template-instruction-pairs.md)'s three-file layout collapses to one authored file. `{type}.template.md` and `{type}.instructions.md` go away.
- **Schema stays separate.** Writers don't need the schema. Each type-spec doc declares its schema explicitly in frontmatter (`schema: <path>` or `schema: null`); the validator reads that field. Sibling filenames remain only an author-chosen convention, not a resolver fallback. Broader schema wiring remains a future validator workshop.
- **Global types live once.** `kb/types/<name>.md` is the authoritative location for a global type. Collection-local types live at `kb/<collection>/types/<name>.md`. Which collection hosts a given write comes from user intent or from the target collection's `COLLECTION.md` listing — not from a hardcoded special-case table in the skill.
- **Self-referential root.** `kb/types/type-spec.md` has `type: kb/types/type-spec.md` — its own spec. Validators terminate on path-equals-self.
- **Paths are under `kb/`.** Valid `type:` paths are either repository-relative (`kb/...`) or file-relative (`./...` or `../...`), end with `.md`, resolve under `kb/`, and are not absolute paths or URLs.

### No resolver CLI; no compile step

The write skill reads the path named by `type:` (for edits) or the path named in the target collection's `COLLECTION.md` (for new writes). Three inputs compose at read time in the agent's context: skill-embedded linking vocabulary, the type instructions doc, and the target collection's `COLLECTION.md`. No runtime resolver CLI; no build step fusing canonical sources into compiled artifacts.

This deliberately keeps the authoring surface file-native. The software may still validate paths, support complete type migrations, and eventually provide a type-move command, but the agent-facing instruction remains "read this file and follow it." That shape works with editor file caches, tool affordances, and the way coding agents preserve context across a task. The system pays a small amount of path-management complexity so the LLM does not have to execute a resolution protocol before it can start writing.

## How this resolves the pain points

1. **Filesystem discovery gone.** The path is lexical; the write skill opens it directly. No prose rules to keep in sync with validator Python.
2. **Ambiguity gone.** A path names exactly one doc. The `review`-in-two-collections case becomes a normal disambiguation: the author writes the specific path.
3. **Special-case routing gone.** Destination collection comes from user intent or `COLLECTION.md`, not from a hardcoded table in the skill.
4. **Three-file drift gone.** Template and authoring prose share a file. Schema is orthogonal (validator concern, not writer concern) and stays separate for that reason.
5. **Adding a new type is one markdown file.** No skill edit, no tooling change. Global types go to `kb/types/`; collection-local types go to `kb/<collection>/types/`.
6. **Agent instructions get shorter.** The write skill no longer teaches a lookup algorithm or JSON interpretation protocol. It tells the agent which canonical files to read.

## Consequences

### Easier

- Adding or editing a type is a single edit to a single hand-authored file. No build step; no stale compiled cache; no registry update.
- Changing linking conventions updates one place (`SKILL.md` or `COLLECTION.md`) and takes effect on the next write. No fan-out to per-type docs.
- Drift between template and instructions is structurally impossible because they are the same file.
- Type instructions participate in the same file-based workflow as the rest of the KB: agents can open them directly, keep them in context, and use normal editor/search affordances instead of treating type resolution as a separate API interaction.

### Harder

- `type:` values are longer strings (`kb/reference/types/adr.md` vs. `adr`). Minor authoring friction for humans; no meaningful cost for LLM authors.
- Paths are load-bearing. Renaming a type doc moves every binding. Needs `commonplace-mv-type` tooling when the first rename happens; cheap to build, not needed for the initial migration.
- Agents must correctly compose three inputs at every write. The skill has to name all three explicitly; that discipline is the enforcement point.
- Discoverability of available types is a filesystem glob over `kb/**/types/*.md` or a per-collection `COLLECTION.md` listing, rather than a compiled index. Acceptable at the current type count.
- No build-time check that (for example) a template is consistent with its schema. Consistency becomes runtime (validator) or manual.

### Scope

- Does **not** change `cp-skill-compile-collections` (the cross-register topology compile skill at the time this ADR was authored — later retired by ADR 019, which moved the connect/write skills to live per-destination reads of `COLLECTION.md`).
- Does **not** fully redesign schema storage or validator behavior. The migration requires every type-spec doc to declare its schema explicitly in frontmatter (`schema: <path>` or `schema: null`); broader schema wiring remains a future validator workshop.
- Retires the `note` inlining from [ADR 002](./002-inline-global-types-in-writing-guide.md) as part of the whole-KB migration.

### Migration

This decision lands as a whole-KB migration, not an `adr` pilot and not a per-type rollout. See [`plan.md`](../../work/write-type-resolver/plan.md) for concrete steps.

The implementation creates/fuses all type instruction docs, rewrites all explicit frontmatter `type:` values to paths, updates `cp-skill-write`, updates validation, and validates the corpus in one migration bundle. There is no enum-to-path redirect period and no compatibility table. If the migrated state fails, revert the bundle from git instead of carrying two type mechanisms.

### Trigger conditions for revisiting

- If the type × collection product grows past the point where read-time composition becomes a context-budget problem, reconsider a compile step.
- If linking conventions fragment per-type (not per-collection), per-type pre-fusion may become necessary.
- If path fragility becomes painful at scale, reconsider keeping a stable ID alongside the path or canonicalising through a narrow resolver.

---

Relevant Notes:

- [ADR 009 — link relationship semantics](../../reference/adr/009-link-relationship-semantics.md) — grounds: the linking vocabulary embedded in `cp-skill-write/SKILL.md`; unchanged by this ADR.
- [ADR 016 — custom types use template/instruction pairs](./016-custom-types-use-template-instruction-pairs.md) — partially superseded: the three-file split fuses to one authoring file plus a sibling schema.
- [ADR 002 — inline global types in writing guide](./002-inline-global-types-in-writing-guide.md) — affected at `note` migration.
- [linking-theory](../../notes/linking-theory.md) — grounds: decision-cost model for keeping context reads cheap.
