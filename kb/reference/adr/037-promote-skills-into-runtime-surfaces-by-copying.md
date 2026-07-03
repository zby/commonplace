---
description: Replaces symlink and Windows-junction skill projections with real copied directories in commonplace-init, migrating legacy links to copies on re-init
type: ../types/adr.md
tags: []
status: accepted
---

# 037-Promote skills into runtime surfaces by copying

**Status:** accepted
**Date:** 2026-07-03

## Context

Since ADR 006, `commonplace-init` promoted shipped skills into the known runtime discovery surfaces (`.claude/skills/`, `.agents/skills/`) as symlinks into the canonical `kb/commonplace/instructions/<name>/` directories, keeping one authoritative copy of each skill. On Windows, where real symlinks require admin rights or Developer Mode, the installer fell back to directory junctions created through the stdlib `_winapi.CreateJunction`.

The link-based projection kept producing Windows problems. Symlink creation fails without elevated privileges; junctions require an absolute target on a local volume, so they break when a project moves and are skipped entirely on network volumes and sandboxed filesystems; and tools vary in how they treat reparse points, so a projection that exists on disk still may not resolve for a given runtime. The projection step was the one part of install that could partially fail, which forced a skip-and-report path in the installer, extra Windows warnings, and manual recovery instructions in INSTALL.md.

ADR 027 already removed symlinks from the packaging side for the same reason: Unix filesystem affordances are the wrong dependency for install correctness once Windows matters.

## Decision

`commonplace-init` copies each promoted skill directory from `kb/commonplace/instructions/<name>/` into every runtime skills directory as regular files. Projected files go through the same per-file `_record_existing` classification as the rest of the scaffold: missing files are created, identical files are preserved silently, and differing files are preserved and reported.

A symlink or junction found at a projection destination — left by an install from an earlier version — is removed and replaced with a copy on re-init. The junction fallback and the skipped-projection reporting are deleted; copying works on every platform, so there is no partial-failure path left.

The canonical contract stays the source directory under `kb/commonplace/instructions/`. The Commonplace source repo keeps its committed relative symlinks under `.claude/skills/` and `.agents/skills/` — those are repo-local development conveniences on platforms that support them, not installer output.

## Consequences

Easier:
- Install behaves identically on every platform and filesystem; no privilege, Developer Mode, volume, or reparse-point conditions to document or diagnose.
- The installer loses its only partial-failure path (skipped projections), along with the Windows-specific warning about them.
- Runtime surfaces contain plain directories that every tool reads without following links.

Harder:
- Skill content is duplicated: one canonical copy plus one copy per runtime surface. Edits made to a projected copy drift silently until a re-init reports them.
- Upgrades no longer propagate through a link. Re-running `commonplace-init` reports projected copies that differ from the canonical source but never overwrites them; reconciling is a manual diff-and-merge, consistent with the scaffold-wide "never clobber a practitioner edit" rule.

Risks:
- Users may edit a runtime copy instead of the canonical source and lose the edit's authority; the re-init drift report is the only signal.

## Links

- [006-two-tree-installation-layout](./006-two-tree-installation-layout.md) — refines: replaces the symlinked skill promotion that layout introduced
- [014-scripts-as-python-package-one-tree-model](./014-scripts-as-python-package-one-tree-model.md) — refines: keeps the package-and-init model while changing the projection mechanism
- [021-ship-library-content-under-kb-commonplace](./021-ship-library-content-under-kb-commonplace.md) — implements: projects from the `kb/commonplace/instructions/` source path that decision fixed
- [027-package-scaffold-assets-without-source-tree-symlinks](./027-package-scaffold-assets-without-source-tree-symlinks.md) — extends: removes the remaining install-time symlink dependency after packaging-time symlinks were removed
- [instruction-generation](../instruction-generation.md) — implemented-by: skill projection section describing the copy behavior
