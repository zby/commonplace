---
description: Decision to ship operational scripts as an installable Python package (llm-commonplace), replace the two-tree layout with a one-tree init model, and use scaffold symlinks for zero-duplication seeding
type: ../types/adr.md
tags: []
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

Beyond the two-tree problems, the plugin-based skill delivery model ([ADR-013](./013-skills-first-delivery-with-core-local-type-split.md)) had its own friction:

5. **Plugin installation differs per runtime.** Claude Code uses `claude plugin install <path>`, Codex uses a marketplace JSON file. Two manifests to maintain (`.claude-plugin/`, `.codex-plugin/`), two install procedures to document.
6. **Plugins still require a local path.** There is no pip-installable plugin delivery. The Python package eliminates the checkout dependency for operational code, but plugins reintroduce it for skills.
7. **Global installs create environment coupling.** Installing the package globally or into a shared venv means all projects share the same version. Project-local venvs are cleaner but require the venv to be activated or its `bin/` to be on PATH.

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

Consuming projects no longer need a `commonplace/` framework subtree. After `pip install llm-commonplace`, the user runs `commonplace-init --name <project>` to create the local project structure. The init command:

- copies seed files (instructions, review gates, type definitions) from the installed package
- installs skills directly into `.claude/skills/` and `.agents/skills/` with a `commonplace-` prefix (e.g., `commonplace-write`, `commonplace-validate`)
- resolves templates with the project name: `.envrc`, `AGENTS.md.template`, `qmd-collections.yml`

No separate plugin installation is needed. Skills are project-local files, not plugin-delivered. This eliminates the per-runtime plugin installation divergence — the same init command works regardless of whether the consumer uses Claude Code, Codex, or another runtime that reads skills from a directory.

The `commonplace-` prefix on skill names avoids collisions with a project's own skills. A project can have its own `/write` skill without conflicting with `/commonplace-write`.

The user's repo contains only their own content. Framework code lives in the installed package, accessed through CLI commands and `importlib.resources`.

### 3. Scaffold via symlinks

An earlier design proposed a `scaffold/` directory containing copies of instruction files and type definitions. This was rejected because it creates a maintenance burden — every change to an instruction file must be mirrored in scaffold. Symlinks eliminate the duplication: the scaffold directory is just a view over the repo's live files.

The `src/commonplace/scaffold/` directory contains symlinks to the repo's canonical files:

- `kb/instructions` -> `../../../../kb/instructions`
- `kb/reference` -> `../../../../kb/reference`
- `kb/reports` -> `../../../../kb/reports`
- `kb/types` -> `../../../../kb/types`
- `kb/work` -> `../../../../kb/work`
- `AGENTS.md.template` -> `../../../AGENTS.md.template`
- `.envrc.template` -> `../../../.envrc.template`

During development, `importlib.resources` follows the symlinks — edits to instruction files are immediately available without a sync step. During wheel builds, hatchling dereferences the symlinks and embeds the actual file contents. The wheel is self-contained.

### 4. Skills invoke commands, not paths

Before: `python3 commonplace/scripts/validate_notes.py "$ARGUMENTS"`
After: `commonplace-validate "$ARGUMENTS"`

Skills depend on command names, not filesystem layout. Missing commands are setup errors, not path-resolution failures.

### 5. direnv for project-scoped environment

Agent runtimes (Claude Code, Codex) spawn shell processes that don't inherit a manually activated venv. The commands need to be on PATH without the user running `source .venv/bin/activate` first. Two approaches were considered:

- **`uv run` prefix** — forces every skill and instruction to invoke commands as `uv run commonplace-validate` instead of `commonplace-validate`. Couples the skill layer to a specific Python packaging tool.
- **direnv + `.envrc`** — automatically sets PATH, environment variables, and venv activation when entering the project directory. Agent runtimes inherit the environment. Skills invoke commands by name. Project-scoped — deactivates when you leave the directory.

direnv is the recommended approach. Init generates a ready-to-use `.envrc` so the user only needs `direnv allow`.

### 6. Init resolves templates

Templates with manual placeholders are a common source of setup errors — users forget to edit them, or edit them inconsistently across files. The init command resolves all placeholders from a single `--name` argument.

`commonplace-init --name <project>` fills in project-specific placeholders:

- `.envrc` — PATH (adds `.venv/bin` for venv-free command access), UV_CACHE_DIR (avoids permission issues in sandboxed runtimes like Codex), COMMONPLACE_QMD_INDEX (lets skills find the project's qmd index without hardcoding)
- `AGENTS.md.template` — project name in heading
- `qmd-collections.yml` — project name and absolute paths to KB directories

The `--name` flag defaults to the directory name if omitted.

### 7. Init is idempotent and non-destructive

`commonplace-init` creates directories, copies scaffold files, resolves templates, and installs skills. It never overwrites existing files. Rerunning after a package upgrade picks up new scaffold files without disturbing user modifications.

## Consequences

**Easier:**
- Installation is `pip install` + `commonplace-init`. No cloning, no submodules, no gitignored checkouts.
- Skills are decoupled from filesystem layout. They invoke stable command names.
- Skills install directly into `.claude/skills/` and `.agents/skills/` — no plugin manifests, no runtime-specific install commands.
- Template resolution means no manual placeholder editing — `.envrc`, qmd config, and AGENTS template are ready to use.
- The review system works reliably across project boundaries — proper imports, package data for schema loading, no `sys.path` manipulation.
- Updating is `pip install --upgrade` + rerun `commonplace-init`.
- Scaffold symlinks eliminate file duplication in the repo. One canonical copy of each instruction file.

**Harder:**
- Two names to know: `llm-commonplace` (PyPI distribution) vs `commonplace` (Python import). The name `commonplace` was already claimed on PyPI by an unrelated project. `llm-commonplace` was chosen to be clearly distinct and avoid PyPI's similar-name rejection rules.
- Scaffold files are snapshots at init time. After seeding, the user's copies diverge from the package. There is no automatic sync mechanism — rerunning init only adds new files, it does not update existing ones.
- Skills are copied at init time, not symlinked. Editing a skill in the framework repo requires rerunning init in consuming projects to pick up changes.
- Contributors must remember that scaffold symlinks point to live repo files. Adding a new instruction file requires no scaffold update, but removing or renaming one does.

**Supersedes:** [ADR-006 (two-tree installation layout)](./006-two-tree-installation-layout.md). The two-tree model is replaced by one-tree-plus-package. ADR-006's `commonplace/` subtree no longer exists in consuming projects.

**Refines:** [ADR-008 (stdlib-only core scripts)](./008-stdlib-only-core-scripts.md). The stdlib-only constraint remains for core operations, but scripts are now invoked as installed commands rather than by direct path. The "no venv needed" benefit is replaced by "standard pip install".

**Refines:** [ADR-013 (skills-first delivery)](./013-skills-first-delivery-with-core-local-type-split.md). Skills-first delivery remains the model. The change is in how the operational backend is packaged — installed Python package rather than scripts in a framework checkout.

---

Relevant Notes:

- [ADR-006: two-tree installation layout](./006-two-tree-installation-layout.md) — superseded: the two-tree model this replaces
- [ADR-008: stdlib-only core scripts](./008-stdlib-only-core-scripts.md) — refined: scripts are still stdlib-only but now installed as a package
- [ADR-013: skills-first delivery](./013-skills-first-delivery-with-core-local-type-split.md) — refined: skills-first model unchanged, backend packaging updated
