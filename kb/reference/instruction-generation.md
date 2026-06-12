---
description: Commonplace's shipped build-time instruction generation flow — scaffold trees, template substitution, the `commonplace-init` entry point, and the specific generated artifacts
type: kb/types/note.md
tags: []
status: current
---

# Instruction generation

How Commonplace instantiates build-time generation over runtime parameterisation in the shipped system. This note describes the scaffold, template substitution, and install entry point.

## The entry point

`commonplace-init` is the single build/install step. It creates the project directory structure, copies scaffold trees verbatim, and resolves a small set of templates with per-project values. Everything a new Commonplace project needs is produced by this one command.

There are no runtime variables in the generated artifacts. `AGENTS.md`, skill definitions, and configuration files contain literal paths and names by the time an agent sees them.

## Substitution points

`init_project` resolves three placeholder kinds during template processing:

| Placeholder | Replaced with | Source |
|---|---|---|
| `<your-project>` | Project directory name (or `--name` override) | CLI argument or `root.name` |
| `{{project_name}}` | Same | same |
| `/PATH/TO/COMMONPLACE/` | Absolute path to the project root, with trailing slash | `root` resolved to absolute path |

Substitution is a flat string replace in `_write_template`. Templates that don't need substitution (scaffold trees) are copied byte-for-byte instead.

## Generated artifacts

`commonplace-init` produces four kinds of output:

**Directories** (from `DEFAULT_DIRS`) — empty directory shells the practitioner fills in:

- `kb/types/` — shared global types
- `kb/notes/`, `kb/notes/types/` — user's notes collection
- `kb/reference/`, `kb/reference/types/` — user's reference collection
- `kb/instructions/` — user's instructions collection
- `kb/sources/`, `kb/sources/types/` — user's source captures
- `kb/tasks/backlog/`, `kb/tasks/active/`, `kb/tasks/completed/` — user's task lifecycle
- `kb/work/`, `kb/reports/`, `kb/reports/connect/`, `kb/reports/types/` — user's workshops and reports

**Scaffold trees** — copied from scaffold sources. In a built wheel these sources live under packaged `commonplace/_data/`; in an editable source checkout `commonplace-init` falls back to the canonical repo paths:

- `kb/commonplace/notes/` — shipped methodology library (from our `kb/notes/`)
- `kb/commonplace/reference/` — shipped-system documentation and ADRs
- `kb/commonplace/instructions/` — shipped procedures and `cp-skill-*` skills
- `kb/commonplace/agent-memory-systems/` — shipped reviews of external systems
- `kb/types/` — shared global types (`text`, `note`, `instruction`, `definition`, `index`)
- `kb/reports/types/`, `kb/sources/types/` — collection-local type definitions for user-space collections

**Scaffold files** — individual files copied into the user's collections:

- `kb/notes/COLLECTION.md` — minimal theoretical/descriptive/prescriptive template
- `kb/reference/COLLECTION.md` — minimal template
- `kb/instructions/COLLECTION.md` — minimal template

Each template invites the practitioner to pick a register, state a quality goal, and declare outbound link rules, with pointers to the shipped `kb/commonplace/<collection>/COLLECTION.md` as a worked example.

**Resolved templates** — read, substituted, written:

- `AGENTS.md.template` → `AGENTS.md.template` in the target root (practitioner then copies or renames to `AGENTS.md`)
- `.envrc.template` → `.envrc`

Both flow through the same `_write_template` helper with the same replacements dictionary.

## Scaffold source resolution

The source tree does not keep symlinked copies of the shipped KB under `src/commonplace/_data/`. Instead, `init_project` resolves each scaffold input by checking two locations:

1. `commonplace/_data/<path>` — packaged wheel data, populated by Hatch `force-include` entries from canonical repo paths. The sdist also explicitly includes those canonical inputs so wheels built from sdists have the same scaffold source.
2. The canonical repo path — used in editable source checkouts, so edits to `kb/notes/`, `kb/reference/`, `kb/instructions/`, and the root templates are picked up without duplicating files.

The exception is `src/commonplace/_data/templates/`, which contains real scaffold-only files for the user's empty `COLLECTION.md` templates. Those files have no canonical counterpart elsewhere in the KB.

## Skill projection

In addition to copying the instructions tree under `kb/commonplace/instructions/`, `init_project` projects a selected subset of skills (`write`, `validate`, `connect`, `convert`, `health-check`, `ingest`, `snapshot-web`, `revise-iterative`, `revise-autoreason`) into two known runtime discovery layouts:

- `.claude/skills/cp-skill-<skill>/`
- `.agents/skills/cp-skill-<skill>/`

Each generated projection is a **symlink** pointing at `kb/commonplace/instructions/cp-skill-<skill>/`. This keeps skill discovery working for those runtimes while the canonical skill content stays in one place inside the shipped library.

The canonical contract is the source directory, not the two generated layouts. Agent runtimes and IDEs that use another skill surface must link, copy, register, or import the same `kb/commonplace/instructions/cp-skill-*` directories according to their own rules.

## Re-running init

`init_project` is idempotent-ish. Existing files are classified into three groups by `_record_existing`:

- **Identical to scaffold** — silently preserved
- **Different from scaffold** — preserved without overwriting, reported as "preserved existing files differing from current scaffold output" so the operator can decide whether to diff and update manually
- **Missing** — created fresh

The rule is "never clobber a practitioner edit." Updating an installed project to a newer Commonplace release is a manual diff-and-merge step, not a re-run.

## What's not generated

A short list of things that are still authored by hand rather than generated:

- Static-site navigation configuration, if a project publishes the KB as a site
- Per-project customisation of the `## KB Goals and Scope` section in a generated `AGENTS.md` — the template carries placeholder prose; the practitioner fills in real values

These could all move to generated form later, but the current build-time step covers the cases where runtime parameterisation would have cost the most interpretation overhead: paths in promoted skills and the project name stamped into the control-plane template.

---

Relevant Notes:

- [014-scripts-as-python-package-one-tree-model](./adr/014-scripts-as-python-package-one-tree-model.md) — decision: shipping scripts as an installable Python package and consolidating scaffold into one tree
- [027-package-scaffold-assets-without-source-tree-symlinks](./adr/027-package-scaffold-assets-without-source-tree-symlinks.md) — decision: package scaffold assets with explicit wheel includes and source-checkout fallback instead of source-tree symlinks
- [013-skills-first-delivery-with-core-local-type-split](./adr/013-skills-first-delivery-with-core-local-type-split.md) — decision: the skills-first delivery model and the core/local type split that `SCAFFOLD_TREES` and `PROMOTED_SKILLS` implement
- [006-two-tree-installation-layout](./adr/006-two-tree-installation-layout.md) — decision: the installation layout that `commonplace-init` produces
- [architecture](./architecture.md) — shipped architecture: where the generation pipeline sits inside the installed surface
- [control-plane-goals](./control-plane-goals.md) — how the generated `AGENTS.md.template` carries the `## KB Goals and Scope` section for practitioners to fill in
