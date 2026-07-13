---
description: Replaces per-path git check-ignore visibility and git-mv relocation with a package-owned name-based visibility contract; commonplace commands never invoke the git binary
type: ../types/adr.md
tags: []
status: accepted
---

# 039-Tool visibility is package-owned and git is never invoked

**Status:** accepted
**Date:** 2026-07-05

## Context

Which files the tools could see was delegated to git: `project_paths.is_git_ignored` spawned one `git check-ignore --no-index` subprocess per file and directory, and every tree enumeration — validation, tag collection, dir-index generation, relocation link rewriting, the mkdocs build hooks — sat on top of it. Relocation additionally preferred `git mv` for moves, silently falling back to `Path.rename`.

This coupling had three costs. Enumerating the Commonplace repo's ~1,000 notes spawned ~2,300 subprocesses and took about five seconds before any file was read. Behavior differed by environment: in a plain directory or a vendored install without git, the filter silently vanished and the tools saw *more* files than in a git checkout. And `--no-index` applies ignore *patterns* where git applies ignore *semantics*: a directory that was tracked in git but matched by a later-added `.gitignore` rule (`kb/work/agent-memory-design/`) was committed KB content that the KB's own tools could not see, while real `git check-ignore` reported it as not ignored.

An inventory of what gitignore filtering actually excluded showed the delegation was overweight. Almost every exclusion the tools need is structural and already expressed by name in code — `types/`, `COLLECTION.md`, `.replaced.*` archives, nested git repos — or is a build/vendor tree (`.venv/`, `site/`, `tmp/`) that only the repository-wide relocation walk ever encounters. ADR 032 had already removed git from review freshness for the same class of reason: users and agents use git differently, and correctness should not depend on how.

## Decision

Visibility is a package-owned contract and the `commonplace-*` commands never invoke the git binary.

The contract, implemented in `project_paths.walk_visible`: hidden (dot-prefixed) entries and nested git repositories are invisible to every markdown walk; repository-wide walks (relocation's `find_repo_markdown_files`) additionally skip a fixed set of build/vendor artifact directory names (`build`, `dist`, `node_modules`, `site`, `tmp`, `__pycache__`). Collection walks exclude structural metadata and archives at the caller, but otherwise treat every visible Markdown file as content. Gitignore rules have no effect on what the tools see. Nested repositories are detected by the presence of a `.git` entry — a filesystem layout check, not a git invocation.

There is no mechanism for declaring collection content local-only. Everything visible under a collection is KB content; content that must not be swept lives outside collections, in hidden directories, or does not exist in the working tree. If a declaration mechanism is ever needed, it will be an explicit package-owned one, not gitignore.

Relocation moves files with `Path.rename` (creating destination parents first). Git detects renames on commit; the `git mv` path and its silent strategy degradation are deleted.

## Consequences

Easier:

- Tree enumeration drops from seconds of subprocess churn to a plain filesystem walk, in every command and in the mkdocs build.
- Behavior is identical with or without git, in checkouts, plain directories, and vendored installs.
- Committed KB content can no longer be hidden from the tools by an ignore pattern; the tracked-but-pattern-matched divergence is gone by construction.
- Relocation has one move path instead of two strategies chosen by environment.

Harder:

- Gitignoring a file inside a collection no longer hides it from sweeps. Local scratch under a collection (for example gitignored subtrees of `kb/work/`) now appears in validation and local site builds; fresh-clone CI is unchanged because such files do not exist there. Keeping something out of sweeps now means keeping it out of collections.
- The repo-wide walk no longer descends hidden directories, so links inside `.claude/skills/` and `.agents/skills/` copies are not rewritten on relocation; the canonical sources under `kb/` still are, and runtime copies are refreshed by re-init (ADR 037).

Risks:

- The artifact name set is a blunt instrument: a knowledge directory named `site` or `tmp` at any depth is invisible to the repository-wide walk (collection walks are unaffected). The names are documented on `REPO_ARTIFACT_DIR_NAMES`.

## Links

- [032-review-freshness-uses-db-snapshots-not-git](./032-review-freshness-uses-db-snapshots-not-git.md) — extends: removes the remaining git dependencies from the non-review commands after review correctness left git
- [025-complete-generated-indexes-are-build-time-only](./025-complete-generated-indexes-are-build-time-only.md) — see-also: generated directory indexes do not normally exist in the working tree
- [lib-modules](../lib-modules.md) — implemented-by: `project_paths` and `relocation` sections describe the visibility walker and plain-rename move
