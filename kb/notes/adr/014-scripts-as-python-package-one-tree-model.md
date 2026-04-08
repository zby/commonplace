---
description: Decision to ship operational scripts as an installable Python package (llm-commonplace), replace the two-tree layout with a one-tree init model, and use scaffold symlinks for zero-duplication seeding
type: adr
tags: [architecture]
status: accepted
---

# 014-scripts-as-python-package-one-tree-model

**Status:** accepted
**Date:** 2026-04-08

## Context

The two-tree installation model ([ADR-006](./006-two-tree-installation-layout.md)) required a vendored `commonplace/` subtree in every consuming project — either as a submodule or gitignored clone. Skills invoked scripts by path (`python3 commonplace/scripts/validate_notes.py`), which coupled skill definitions to filesystem layout and required the framework checkout to be present at runtime.

This created several problems:

1. **Installation friction.** Users had to clone the repo, manage a submodule or gitignored checkout, and keep it updated separately from their project. There was no `pip install`.
2. **Fragile invocation.** Skills referenced relative script paths. Moving a script or restructuring the repo broke skills in consuming projects.
3. **No real packaging.** Scripts imported siblings via `sys.path` manipulation. There was no dependency resolution, no entry points, no standard Python packaging.
4. **Duplication of concerns.** Operational artifacts (types, instructions) were copied from the framework tree into the user tree at install time, but the framework tree still had to exist for scripts and methodology.

The review system — with its DB helpers, schema loading, metadata models, and multi-script pipelines — was the forcing function. It could not be reliably invoked from a sibling-import script layout across project boundaries.

## Decision

### 1. Scripts become a Python package

All operational Python code moves into an installable package (`llm-commonplace` on PyPI, `import commonplace` in Python). The package uses src layout (`src/commonplace/`) with subpackages:

- `cli/` — user-facing commands (validate, snapshot, index generation, init)
- `review/` — review system (DB, metadata, runners, gates, sweeps)
- `lib/` — shared libraries (frontmatter parser, type resolver)
- `scaffold/` — seed assets for project initialization
- `migrations/` — one-off migration scripts

Each command gets a `main()` entry point and a `[project.scripts]` entry, producing stable `commonplace-*` CLI commands.

### 2. One-tree model replaces two-tree

Consuming projects no longer need a `commonplace/` framework subtree. After `pip install llm-commonplace`, the user runs `commonplace-init` to create the local project structure. The init command copies seed files (instructions, review gates, type definitions, AGENTS.md.template) from the installed package into the project root.

The user's repo contains only their own content. Framework code lives in the installed package, accessed through CLI commands and `importlib.resources`.

### 3. Scaffold via symlinks

The `src/commonplace/scaffold/` directory contains symlinks to the repo's canonical files rather than copies:

- `kb/instructions` -> `../../../../kb/instructions`
- `types` -> `../../../types`
- `AGENTS.md.template` -> `../../../AGENTS.md.template`

During development, `importlib.resources` follows the symlinks — edits to instruction files are immediately available without a sync step. During wheel builds, hatchling dereferences the symlinks and embeds the actual file contents. The wheel is self-contained.

### 4. Skills invoke commands, not paths

Before: `python3 commonplace/scripts/validate_notes.py "$ARGUMENTS"`
After: `commonplace-validate-notes "$ARGUMENTS"`

Skills depend on command names, not filesystem layout. Missing commands are setup errors, not path-resolution failures.

### 5. Init is idempotent and non-destructive

`commonplace-init` creates directories and copies scaffold files. It never overwrites existing files. Rerunning after a package upgrade picks up new scaffold files without disturbing user modifications.

## Consequences

**Easier:**
- Installation is `pip install` + `commonplace-init`. No cloning, no submodules, no gitignored checkouts.
- Skills are decoupled from filesystem layout. They invoke stable command names.
- The review system works reliably across project boundaries — proper imports, package data for schema loading, no `sys.path` manipulation.
- Updating is `pip install --upgrade` + rerun `commonplace-init`.
- Scaffold symlinks eliminate file duplication in the repo. One canonical copy of each instruction file.

**Harder:**
- Two names to know: `llm-commonplace` (PyPI distribution) vs `commonplace` (Python import). This is a PyPI naming constraint — `commonplace` is taken.
- Scaffold files are snapshots at init time. After seeding, the user's copies diverge from the package. There is no automatic sync mechanism — rerunning init only adds new files, it does not update existing ones.
- Plugin distribution still requires a local path. The Python package handles operational code, but the skill plugin (`.claude-plugin/`, `.codex-plugin/`) has no pip-installable delivery mechanism yet.
- Contributors must remember that scaffold symlinks point to live repo files. Adding a new instruction file requires no scaffold update, but removing or renaming one does.

**Supersedes:** [ADR-006 (two-tree installation layout)](./006-two-tree-installation-layout.md). The two-tree model is replaced by one-tree-plus-package. ADR-006's `commonplace/` subtree no longer exists in consuming projects.

**Refines:** [ADR-008 (stdlib-only core scripts)](./008-stdlib-only-core-scripts.md). The stdlib-only constraint remains for core operations, but scripts are now invoked as installed commands rather than by direct path. The "no venv needed" benefit is replaced by "standard pip install".

**Refines:** [ADR-013 (skills-first delivery)](./013-skills-first-delivery-with-core-local-type-split.md). Skills-first delivery remains the model. The change is in how the operational backend is packaged — installed Python package rather than scripts in a framework checkout.

---

Relevant Notes:

- [ADR-006: two-tree installation layout](./006-two-tree-installation-layout.md) — superseded: the two-tree model this replaces
- [ADR-008: stdlib-only core scripts](./008-stdlib-only-core-scripts.md) — refined: scripts are still stdlib-only but now installed as a package
- [ADR-013: skills-first delivery](./013-skills-first-delivery-with-core-local-type-split.md) — refined: skills-first model unchanged, backend packaging updated
