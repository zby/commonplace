---
description: "Ship Commonplace library content under kb/commonplace/ so user collections at kb/notes/, kb/reference/, kb/instructions/ stay user-owned while the shipped library sits alongside as a read-only dependency."
type: ../types/adr.md
tags: []
status: accepted
---

# 021-Ship library content under kb/commonplace

**Status:** accepted
**Date:** 2026-04-23
**Relates to:** [ADR-014](./014-scripts-as-python-package-one-tree-model.md) (the one-tree model that placed shipped content at user-collection paths — this ADR refines that model by introducing a namespace within `kb/`)

## Context

Today `commonplace-init` copies our `kb/notes/`, `kb/reference/`, and `kb/instructions/` trees verbatim into the user's project at the same paths (see `SCAFFOLD_TREES` in `src/commonplace/cli/init_project.py`). Our shipped content and the user's own content share the same collection namespace. Three problems follow:

1. A user has no empty collection to write into — their `kb/notes/` is pre-populated with our 195 methodology notes.
2. Shipped content and user content are indistinguishable by path; a user editing "their" `kb/notes/foo.md` may be editing our library without realizing it.
3. `commonplace-init` re-runs overwrite or collide with user-authored files in ambiguous ways, and there's no way to detect that shipped content has been locally modified before an upgrade.

Users will rarely want to connect their own notes to our methodology library — their KBs are about different domains. The dominant need is **isolation with read access**, not cross-linking. But skills (`cp-skill-connect`, `cp-skill-write`, etc.) still need to read shipped content for conventions, type specs, and link-target candidates.

The design question: how to ship library content in a way that isolates it from user content while leaving it structurally visible and inexpensive to reference.

### Options considered

See [the shipped-content namespacing design space](./021-shipping-model-design-space.md) for the full enumeration. Six namespacing shapes were considered, of which two were serious candidates:

- **Option D** — `cp-` directory prefix: `kb/cp-notes/`, `kb/cp-reference/`, `kb/cp-instructions/`.
- **Option E** — single namespace directory: `kb/commonplace/{notes,reference,instructions,agent-memory-systems}/`.

Both options isolate the shipped content from user content. The deciding question was translation cost — how many hardcoded path references in shipped content would need rewriting at ship time.

### Translation-cost finding

A path audit ([ADR 021 Option E path audit](./021-shipping-model-path-audit-option-e.md)) categorized all 1013 path-bearing sites in shipped content (713 body references + 300 frontmatter `type:` pointers) into six patterns with distinct E-compatibility:

- **Pattern A** — generic prose references like "`kb/notes/` holds transferable claims" — resolve correctly to the user's own collection in a user's install. ~50% of references. No translation.
- **Pattern B1** — frontmatter `type:` pointers to shared global types (`kb/types/note.md` etc.). 270 sites. No translation if `kb/types/` stays at top level (not wrapped under `kb/commonplace/`).
- **Pattern B2** — frontmatter `type:` pointers to collection-local types (`kb/reference/types/adr.md`, `kb/notes/types/structured-claim.md`). 28 sites in shipped content. Need either ship-time translation or migration to file-relative paths.
- **Pattern D** — markdown links using sibling-relative URLs (`../notes/definitions/register.md`). Invariant under E because `kb/commonplace/<collection>/` preserves the sibling relationship. Would all require rewriting under D (from `../notes/` to `../cp-notes/`).
- **Patterns E, F** — long-relative and absolute-URL links. Small population (≤10 sites). One-pass rewrite needed for both options.
- **Pattern C** — cosmetic code-formatted path strings in prose. Small population. Either rewrite display text at ship time or accept cosmetic drift.

**Net result: Option E has strictly lower translation cost than Option D.** E preserves sibling-relative links (Pattern D) intact; D requires rewriting all of them. Frontmatter pointers have equivalent cost in both options.

### Type-resolver feasibility

Pattern B2 migration to file-relative paths (`type: ./types/adr.md` or `type: ../types/adr.md`) requires the type resolver in `src/commonplace/lib/type_resolver.py` to accept file-relative paths. Currently it explicitly rejects them (lines 55-62). Verified 2026-04-23: relaxing this is a ~30-line, 1–2-hour change with established precedent (JSON-schema `$ref` resolution already uses file-relative paths at line 165).

## Decision

Ship library content under `kb/commonplace/` in a user's installed project. The user's own collections (`kb/notes/`, `kb/reference/`, `kb/instructions/`) are scaffolded empty with minimal `COLLECTION.md` templates. Shared types stay at top-level `kb/types/`.

### Layout in an installed project

| Path | Category | Content |
|---|---|---|
| `kb/commonplace/notes/` | library (read-only) | shipped methodology notes |
| `kb/commonplace/reference/` | library (read-only) | shipped reference + ADRs |
| `kb/commonplace/instructions/` | library (read-only) | shipped methodology procedures and cp-skill-* |
| `kb/commonplace/agent-memory-systems/` | library (read-only) | shipped reviews of external systems |
| `kb/commonplace/.commonplace` | library marker | records shipped version; drift-check on init |
| `kb/types/` | shared | global types; library and user both extend |
| `kb/notes/` | user | starts empty; user's own notes + minimal `COLLECTION.md` |
| `kb/reference/` | user | starts empty; user's own reference + minimal `COLLECTION.md` |
| `kb/instructions/` | user | starts empty; user's own procedures + minimal `COLLECTION.md` |
| `kb/sources/` | user | scaffolded empty (library omits captured sources) |
| `kb/reports/` | user | scaffolded empty (library's reports are operational, not library content) |
| `kb/tasks/` | user | scaffolded empty |
| `kb/work/` | user | scaffolded empty (library's workshop content is temporary) |
| `kb/log.md` | user | scaffolded empty |

### Bundle scope

Ship git-tracked content from our `kb/notes/`, `kb/reference/`, `kb/instructions/`, `kb/agent-memory-systems/` under `kb/commonplace/`, plus shared `kb/types/`. Omit:

- `kb/sources/` — 4.2M of captured external material, raising bulk and copyright concerns (redistributing third-party captures).
- `kb/work/` — workshop layer, temporary by design.
- `kb/tasks/` content — our operational state, not library.
- `kb/log.md` content — our operational log, not library.

Bundle size: ~440 files, ~4.5M. Roughly 1.5× the current shipped footprint.

### Path invariance rules

- **Sibling-relative markdown links stay unchanged.** `../notes/foo.md` from `kb/instructions/bar.md` works in our repo; `../notes/foo.md` from `kb/commonplace/instructions/bar.md` works in a user's install because `kb/commonplace/notes/foo.md` is the sibling.
- **Absolute `kb/types/...` frontmatter stays unchanged** (Pattern B1). Shared `kb/types/` is at top level in both trees.
- **Collection-local types (Pattern B2) migrate to file-relative paths.** `type: ./types/structured-claim.md` (for notes at collection root) or `type: ../types/adr.md` (for notes one level deep). 28 edits in shipped content.
- **Long-relative (`../kb/...`) and absolute-URL (`[...](kb/...)`) links migrate to sibling-relative Pattern D.** One-pass rewrite, small population.

### Type resolver extension

Extend `src/commonplace/lib/type_resolver.py` to accept file-relative paths in addition to repo-relative:

- If `type:` value starts with `./` or `../`: resolve against the source file's directory.
- If `type:` value starts with `kb/`: resolve against the workspace root (current behavior).
- In both cases, preserve the existing "resolved path must stay under `kb/`" boundary check.

### Read-only convention

A `.commonplace` marker file at `kb/commonplace/` root records the shipped version. On `commonplace-init` re-run:

- If no marker exists: fresh install, copy shipped tree.
- If marker exists and content matches recorded state: safe to overwrite with new version.
- If marker exists and content has drifted: refuse to overwrite; print a diff summary; require user acknowledgement.

No filesystem permissions; no git submodule. Convention + drift check only.

### Skill root resolution

Skills detect library root by presence check: if `kb/commonplace/` exists alongside the user's collections, it is the library root and skills include it when scanning for link targets, loading conventions, and resolving types. If absent, skills operate single-root (user-only). No config file.

### User `COLLECTION.md` scaffolding

`commonplace-init` scaffolds a minimal `COLLECTION.md` into each user collection (`kb/notes/`, `kb/reference/`, `kb/instructions/`) with explicit register prompts ("theoretical / descriptive / prescriptive — pick one") and placeholder sections (title conventions, outbound link rules, type offerings). Shipped `kb/commonplace/<collection>/COLLECTION.md` files remain authoritative for the library.

### Source link migration (linking principle)

Current shipped notes cite local source digests (`[Title](../sources/foo.ingest.md)`) as their primary reference. Since `kb/sources/` is not shipped, those 283 links across 94 files would dangle.

Adopt a new linking principle: **a note's primary citation is the external source (URL, DOI, paper); the local ingest is supplementary, not primary.** Rewrite the 283 links to `[Title](https://external.url)` as primary, with optional `— [ingest](../sources/foo.ingest.md)` where the ingest adds value.

This principle is worth extracting as a library note in its own right (citation hygiene applies beyond this shipping decision).

## Consequences

**Easier:**
- User tree is clean on init — user's `kb/notes/` starts empty, ready for their own content.
- Shipped content has a single boundary (`kb/commonplace/`) for read-only conventions, re-sync, and provenance.
- Library re-sync is one-directory-tree operation; drift detection is exact via the marker.
- Sibling-relative links work invariantly across source and ship — no wholesale path rewriting needed.
- User collections are peers of library collections in the file tree, so `cp-skill-connect` can scan both with one presence-check convention.

**Harder:**
- The repo is no longer paths-identical to a user's install. Our `kb/notes/` becomes their `kb/commonplace/notes/`. Mitigation: `commonplace-ship-preview` (future tool) can package the tree into a temp dir matching a user's layout for testing. In practice, Pattern A references (dominant) make this divergence mostly invisible.
- 28 frontmatter B2 pointers must be migrated to file-relative style. One-pass mechanical edit.
- 283 `../sources/...` links must be rewritten to use external URLs primarily. Non-trivial — each requires pulling the URL from the ingest's frontmatter — but mechanical-ish.
- `commonplace-init` gains complexity: writes marker, scaffolds user-collection `COLLECTION.md` templates, checks for drift.
- Type resolver gains file-relative support. Small, contained change.
- `PROMOTED_SKILLS` symlink source in `init_project.py` updates from `kb/instructions/<name>/` to `kb/commonplace/instructions/<name>/`.

**Rejected alternatives:**
- **Option D (`cp-` prefix).** Rejected because sibling-relative links (`../notes/...`) would all require rewriting to `../cp-notes/...`, whereas E leaves them invariant. Translation cost under D is strictly higher than E.
- **Flatten collection-local types to shared `kb/types/`.** Contradicts the existing principle that directory-scoped types are cheaper than global types ([kb/notes/directory-scoped-types-are-cheaper-than-global-types.md](../../notes/directory-scoped-types-are-cheaper-than-global-types.md)).
- **Ship-time frontmatter translation (B2a).** Dropped because file-relative frontmatter (B2b) is a ~1–2h type-resolver change and avoids source-vs-ship divergence in frontmatter.

## Migration plan

1. **Type-resolver extension** — relax `_validate_repo_relative_kb_path` in `src/commonplace/lib/type_resolver.py` to accept file-relative paths; thread `file_path` from `resolve_type` through to the validator. Add tests in `test/commonplace/lib/test_type_resolver.py` covering file-relative `type:` values and boundary escapes.
2. **Frontmatter migration** — one-pass rewrite of 28 Pattern-B2 frontmatter pointers to file-relative form.
3. **Link-pattern cleanup** — rewrite the small population of Pattern E/F links to Pattern D sibling-relative form.
4. **Source-link migration** — rewrite 283 `../sources/...` links across 94 files to external URL as primary, supplementary ingest link optional.
5. **Scaffold changes** in `src/commonplace/cli/init_project.py` — update `SCAFFOLD_TREES`, `DEFAULT_DIRS`, `PROMOTED_SKILLS` symlink source path; add `.commonplace` marker write; add drift check on re-init; add user-collection `COLLECTION.md` scaffolding.
6. **`AGENTS.md.template` update** — rewrite its three specific references to shipped content (`kb/reference/commands.md`, `kb/instructions/REVIEW-SYSTEM.md`, `kb/instructions/FIX-SYSTEM.md`) to `kb/commonplace/...`.
7. **Ship-preview tool (optional, deferred)** — `commonplace-ship-preview` packages the tree into a temp dir with translations applied, so shipped instructions can be tested against a realistic user tree.

## Open questions (non-blocking)

- Symlink patterns for users who want to bridge their collections to the library — separate instructions file or a section in shipped `kb/commonplace/README.md`.
- Versioning the library in a user's tree (submodule or version field in `.commonplace`) — deferred until user re-sync becomes a real workflow concern.
- Source-link migration automation — can the external URL be mechanically extracted from each ingest's frontmatter, or does each need a human pass?

---

Relevant Notes:

- [kb/notes/directory-scoped-types-are-cheaper-than-global-types.md](../../notes/directory-scoped-types-are-cheaper-than-global-types.md) — grounds the B2d rejection
- [ADR 021 shipped-content namespacing design space](./021-shipping-model-design-space.md) — option inventory behind the decision
- [ADR 021 Option E path audit](./021-shipping-model-path-audit-option-e.md) — path-compatibility audit behind the Option E choice
