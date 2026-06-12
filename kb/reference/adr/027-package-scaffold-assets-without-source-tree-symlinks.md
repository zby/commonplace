---
description: Replaces source-tree scaffold symlinks with explicit Hatch wheel force-includes plus source-checkout fallback resolution for Commonplace packaged scaffold assets
type: ../types/adr.md
tags: []
status: accepted
---

# 027-Package scaffold assets without source-tree symlinks

**Status:** accepted
**Date:** 2026-06-11

## Context

ADR 014 used symlinks under `src/commonplace/_data/` to expose canonical repo files (`kb/notes`, `kb/reference`, `kb/instructions`, shared types, templates) as package data. That avoided duplicated scaffold copies, and Hatch dereferenced the links when building wheels.

The symlink farm became the wrong boundary once Windows installation mattered. It made the source tree depend on Unix filesystem affordances, obscured which files were truly package data, and made packaging correctness depend on build-backend symlink behavior rather than an explicit include map. We still need the same invariant ADR 014 protected: the repo must keep one canonical authored copy of every shipped KB artifact.

## Decision

Remove the tracked scaffold symlinks from `src/commonplace/_data/`.

Package built distributions with explicit Hatch include mappings. The sdist includes the canonical scaffold inputs, including promoted `cp-skill-*` directories. The wheel maps those canonical paths into `commonplace/_data/...` with `force-include`:

- `kb/notes` -> `commonplace/_data/kb/notes`
- `kb/reference` -> `commonplace/_data/kb/reference`
- `kb/instructions` -> `commonplace/_data/kb/instructions`
- `kb/agent-memory-systems` -> `commonplace/_data/kb/agent-memory-systems`
- shared type and user-space type directories under their matching `_data/kb/...` targets
- root templates (`AGENTS.md.template`, `.envrc.template`) under `_data/`

Teach `commonplace-init` to resolve scaffold inputs in two steps:

1. Prefer packaged data under `commonplace/_data/` when it exists (the wheel/install case).
2. Fall back to the canonical repository path when running from an editable source checkout.

Keep the small user-collection `COLLECTION.md` templates as real files under `src/commonplace/_data/templates/`, because those files are scaffold-only assets rather than canonical KB library artifacts.

This refines ADR 014's packaging mechanism without changing the installed project layout from ADR 021.

## Consequences

Easier:
- The source tree no longer needs symlink support to represent package scaffold inputs.
- Wheel contents are declared explicitly in `pyproject.toml`, so packaging review can inspect the shipped surface without chasing symlinks.
- Editable source checkouts still read the canonical KB files directly, preserving the no-duplicated-scaffold invariant.

Harder:
- The Hatch include maps become maintained lists. Adding a new top-level scaffold tree or promoted skill directory requires updating `pyproject.toml`.
- Source and wheel modes now have a small resolver branch in `commonplace-init`; tests must cover both the no-symlink source path and wheel package-data path.

Risks:
- A missing `force-include` entry can pass source-checkout tests but fail in a built wheel. Packaging verification should build a wheel and run `commonplace-init` from it before publishing.

## Links

- [014-scripts-as-python-package-one-tree-model](./014-scripts-as-python-package-one-tree-model.md) — refines: replaces the scaffold symlink packaging mechanism while keeping the package-and-init model
- [021-ship-library-content-under-kb-commonplace](./021-ship-library-content-under-kb-commonplace.md) — implements: preserves the installed `kb/commonplace/` library/user boundary
- [architecture](../architecture.md) — implemented-by: current shipped layout and package/init surface
- [instruction-generation](../instruction-generation.md) — implemented-by: scaffold source resolution and generated artifact flow
