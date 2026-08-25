---
description: "Ship Commonplace library content under kb/commonplace/ so user collections at kb/notes/, kb/reference/, kb/instructions/ stay user-owned while the shipped library sits alongside as a read-only dependency."
type: ../types/adr.md
tags: []
status: accepted
---

# 021-Ship library content under kb/commonplace

**Status:** accepted
**Date:** 2026-04-23
**Relates to:** [ADR-014](./014-scripts-as-python-package-one-tree-model.md) (refines its one-tree model with a namespace within `kb/`)
**Superseded (in part) by:** [ADR 068](./068-collection-contracts-stop-enumerating-available-types.md) (type-offerings placeholders)

## Context

Under the one-tree model `commonplace-init` copies our `kb/notes/`, `kb/reference/`, and `kb/instructions/` trees verbatim into the user's project at the same paths, so shipped content and the user's own content share the same collection namespace. Three problems follow:

1. A user has no empty collection to write into — their `kb/notes/` is pre-populated with our 195 methodology notes.
2. Shipped content and user content are indistinguishable by path; a user editing "their" `kb/notes/foo.md` may be editing our library without realizing it.
3. `commonplace-init` re-runs overwrite or collide with user-authored files in ambiguous ways, and there's no way to detect that shipped content has been locally modified before an upgrade.

Users will rarely want to connect their own notes to our methodology library — their KBs are about different domains. The dominant need is **isolation with read access**, not cross-linking. But skills (`cp-skill-connect`, `cp-skill-write`, etc.) still need to read shipped content for conventions, type specs, and link-target candidates.

The design question: how to ship library content in a way that isolates it from user content while leaving it structurally visible and inexpensive to reference.

### Options considered

Six namespacing shapes were considered: no change (shared paths, user/library collision); a `.commonplace` marker at each shipped root with the same paths (provenance without isolation); a file-level `cp-` prefix (rewrites every link, isolates neither `COLLECTION.md` nor types); a directory prefix per collection; a single namespace directory; and a separate vault beside `kb/` (strongest isolation, most skill and config rework). Two were serious candidates:

- **Option D** — `cp-` directory prefix: `kb/cp-notes/`, `kb/cp-reference/`, `kb/cp-instructions/`.
- **Option E** — single namespace directory: `kb/commonplace/{notes,reference,instructions,agent-memory-systems}/`.

Both options isolate the shipped content from user content. The deciding question was translation cost — how many hardcoded path references in shipped content would need rewriting at ship time.

### Translation-cost finding

A path audit of the 1013 path-bearing sites in shipped content found: about half are generic prose references that resolve correctly to the user's own collection in either option; frontmatter `type:` pointers to shared `kb/types/` need no translation if `kb/types/` stays top-level; pointers to collection-local types (28 sites) need either ship-time translation or file-relative paths under either option; sibling-relative markdown links (`../notes/...`) are invariant under E because `kb/commonplace/<collection>/` preserves the sibling relationship, but would all need rewriting under D. **Net result: Option E has strictly lower translation cost than Option D.**

### Type-resolver feasibility

File-relative `type:` paths require the type resolver to accept them, which it then rejected. Relaxing this is a small change with established precedent (JSON-schema `$ref` resolution already uses file-relative paths).

## Decision

Ship library content under `kb/commonplace/` in a user's installed project. The user's own collections (`kb/notes/`, `kb/reference/`, `kb/instructions/`) are scaffolded empty with minimal `COLLECTION.md` templates. Shared types stay at top-level `kb/types/`.

### Layout in an installed project

`kb/commonplace/{notes,reference,instructions,agent-memory-systems}/` is the read-only library, with a `.commonplace` marker at its root; `kb/types/` is shared and extended by both library and user; every other `kb/` collection and file (`notes/`, `reference/`, `instructions/`, `sources/`, `reports/`, `tasks/`, `work/`, `log.md`) is user-owned and scaffolded empty.

### Bundle scope

Ship git-tracked content from our `kb/notes/`, `kb/reference/`, `kb/instructions/`, `kb/agent-memory-systems/` under `kb/commonplace/`, plus shared `kb/types/`. Omit:

- `kb/sources/` — captured external material, raising bulk and copyright concerns (redistributing third-party captures).
- `kb/work/` — workshop layer, temporary by design.
- `kb/tasks/` content — our operational state, not library.
- `kb/log.md` content — our operational log, not library.

### Path invariance rules

- **Sibling-relative markdown links stay unchanged.** `../notes/foo.md` from `kb/instructions/bar.md` works in our repo; `../notes/foo.md` from `kb/commonplace/instructions/bar.md` works in a user's install because `kb/commonplace/notes/foo.md` is the sibling.
- **Absolute `kb/types/...` frontmatter stays unchanged.** Shared `kb/types/` is at top level in both trees.
- **Collection-local types use file-relative paths.** `type: ./types/structured-claim.md` (for notes at collection root) or `type: ../types/adr.md` (for notes one level deep).
- **Long-relative (`../kb/...`) and absolute-URL (`[...](kb/...)`) links become sibling-relative.**

### Type resolver extension

The type resolver accepts file-relative `type:` paths (`./`, `../`, resolved against the source file's directory) alongside repo-relative `kb/` paths, keeping the "resolved path must stay under `kb/`" boundary check in both cases.

### Read-only convention

A `.commonplace` marker file at `kb/commonplace/` root records the shipped version. On re-run, `commonplace-init` overwrites the library when its content matches the recorded state and refuses (with a diff summary) when it has drifted. No filesystem permissions; no git submodule. Convention + drift check only.

### Skill root resolution

Skills detect library root by presence check: if `kb/commonplace/` exists alongside the user's collections, it is the library root and skills include it when scanning for link targets, loading conventions, and resolving types. If absent, skills operate single-root (user-only). No config file.

### User `COLLECTION.md` scaffolding

`commonplace-init` scaffolds a minimal `COLLECTION.md` into each user collection (`kb/notes/`, `kb/reference/`, `kb/instructions/`) with explicit register prompts ("theoretical / descriptive / prescriptive — pick one") and placeholder sections (title conventions, outbound link rules, type offerings). Shipped `kb/commonplace/<collection>/COLLECTION.md` files remain authoritative for the library.

### Source link migration (linking principle)

Shipped notes cited local source digests (`[Title](../sources/foo.ingest.md)`) as their primary reference. Since `kb/sources/` is not shipped, those links (283 across 94 files) would dangle.

Adopt a new linking principle: **a note's primary citation is the external source (URL, DOI, paper); the local ingest is supplementary, not primary.** The external URL is the link target, with an optional `— [ingest](../sources/foo.ingest.md)` where the ingest adds value.

This principle is worth extracting as a library note in its own right (citation hygiene applies beyond this shipping decision).

## Consequences

**Easier:**
- User tree is clean on init — user's `kb/notes/` starts empty, ready for their own content.
- Shipped content has a single boundary (`kb/commonplace/`) for read-only conventions, re-sync, and provenance.
- Library re-sync is one-directory-tree operation; drift detection is exact via the marker.
- Sibling-relative links work invariantly across source and ship — no wholesale path rewriting needed.
- User collections are peers of library collections in the file tree, so `cp-skill-connect` can scan both with one presence-check convention.

**Harder:**
- The repo is no longer paths-identical to a user's install. Our `kb/notes/` becomes their `kb/commonplace/notes/`. Mitigation: a ship-preview tool (deferred) could package the tree into a temp dir matching a user's layout for testing. In practice, generic prose references (dominant) make this divergence mostly invisible.
- `commonplace-init` gains complexity: writes marker, scaffolds user-collection `COLLECTION.md` templates, checks for drift.
- Type resolver gains file-relative support.

**Rejected alternatives:**
- **Option D (`cp-` prefix).** Rejected because sibling-relative links (`../notes/...`) would all require rewriting to `../cp-notes/...`, whereas E leaves them invariant. Translation cost under D is strictly higher than E.
- **Flatten collection-local types to shared `kb/types/`.** Contradicts the existing principle that directory-scoped types are cheaper than global types ([kb/notes/directory-scoped-types-are-cheaper-than-global-types.md](../../notes/directory-scoped-types-are-cheaper-than-global-types.md)).
- **Ship-time frontmatter translation (B2a).** Dropped because file-relative frontmatter (B2b) is a small type-resolver change and avoids source-vs-ship divergence in frontmatter.

## Open questions (non-blocking)

- Symlink patterns for users who want to bridge their collections to the library — separate instructions file or a section in shipped `kb/commonplace/README.md`.
- Versioning the library in a user's tree (submodule or version field in `.commonplace`) — deferred until user re-sync becomes a real workflow concern.

---

Relevant Notes:

- [kb/notes/directory-scoped-types-are-cheaper-than-global-types.md](../../notes/directory-scoped-types-are-cheaper-than-global-types.md) — grounds the B2d rejection
