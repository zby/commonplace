---
description: Replaces per-path git check-ignore visibility and git-mv relocation with a package-owned name-based visibility contract; commonplace commands never invoke the git binary
type: ../types/adr.md
tags: []
status: accepted
---

# 039-Tool visibility is package-owned and git is never invoked

**Status:** accepted
**Date:** 2026-07-05
**Amended:** 2026-07-27 — collection-scoped validation exclusion; 2026-07-13 by [ADR 047](./047-type-specifications-use-normal-deterministic-validation.md) (`types/` visibility)

## Context

Which files the tools could see was delegated to git: one `git check-ignore --no-index` subprocess per file and directory underlay every tree enumeration — validation, tag collection, dir-index generation, relocation link rewriting, the ProperDocs build hooks — and relocation preferred `git mv` for moves with a silent fallback to a plain rename.

This coupling had three costs. Enumerating the Commonplace repo's ~1,000 notes spawned ~2,300 subprocesses and took about five seconds before any file was read. Behavior differed by environment: in a plain directory or a vendored install without git, the filter silently vanished and the tools saw *more* files than in a git checkout. And `--no-index` applies ignore *patterns* where git applies ignore *semantics*: a directory that was tracked in git but matched by a later-added `.gitignore` rule was committed KB content that the KB's own tools could not see, while real `git check-ignore` reported it as not ignored.

An inventory of what gitignore filtering actually excluded showed the delegation was overweight. Almost every exclusion the tools need is structural and already expressed by name in code — `types/`, `COLLECTION.md`, `.replaced.*` archives, nested git repos — or is a build/vendor tree (`.venv/`, `site/`, `tmp/`) that only the repository-wide relocation walk ever encounters. ADR 032 had already removed git from review freshness for the same class of reason: users and agents use git differently, and correctness should not depend on how.

## Decision

Visibility is a package-owned contract and the `commonplace-*` commands never invoke the git binary.

The contract: hidden (dot-prefixed) entries and nested git repositories are invisible to every markdown walk; repository-wide walks additionally skip a fixed set of build/vendor artifact directory names. Collection walks exclude structural metadata and archives at the caller, but otherwise treat every visible Markdown file as content. Gitignore rules have no effect on what the tools see. Nested repositories are detected by the presence of a `.git` entry — a filesystem layout check, not a git invocation.

General content visibility has no mechanism for declaring collection content
local-only. Everything visible under a collection remains KB content to search,
index, and repository-wide tools. Collection-scoped validation has one narrower
projection: a directory containing `.commonplace-validation-ignore` and all of
its descendants are omitted from the validation target and reported in batch
output. This supports tracked or local-only Markdown-bearing experiment and
fixture data whose validity is intentionally controlled by another protocol.
Explicit file validation bypasses the marker. The marker does not affect
general discovery, and gitignore remains irrelevant to every package-owned
visibility decision.

Relocation moves files with a plain filesystem rename; git detects renames on commit.

## Consequences

Easier:

- Tree enumeration drops from seconds of subprocess churn to a plain filesystem walk, in every command and in the ProperDocs build.
- Behavior is identical with or without git, in checkouts, plain directories, and vendored installs.
- Committed KB content can no longer be hidden from the tools by an ignore pattern; the tracked-but-pattern-matched divergence is gone by construction.
- Experimental and fixture subtrees can remain searchable while collection validation excludes them through one explicit package-owned declaration.
- Relocation has one move path instead of two strategies chosen by environment.

Harder:

- Gitignoring a file inside a collection no longer hides it from sweeps. Local scratch under a collection (for example gitignored subtrees of `kb/work/`) now appears in validation and local site builds; fresh-clone CI is unchanged because such files do not exist there. Keeping something out of sweeps now means keeping it out of collections.
- The repo-wide walk no longer descends hidden directories, so links inside `.claude/skills/` and `.agents/skills/` copies are not rewritten on relocation; the canonical sources under `kb/` still are, and runtime copies are refreshed by re-init (ADR 037).

Risks:

- The artifact name set is a blunt instrument: a knowledge directory named `site` or `tmp` at any depth is invisible to the repository-wide walk (collection walks are unaffected).

## Links

- [032-review-freshness-uses-db-snapshots-not-git](./032-review-freshness-uses-db-snapshots-not-git.md) — extends: removes the remaining git dependencies from the non-review commands after review correctness left git
- [025-complete-generated-indexes-are-build-time-only](./025-complete-generated-indexes-are-build-time-only.md) — see-also: generated directory indexes do not normally exist in the working tree
