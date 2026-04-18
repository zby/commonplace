---
description: Commonplace's shipped build-time instruction generation flow — scaffold trees, template substitution, the `commonplace-init` entry point, and the specific generated artifacts
type: note
tags: []
status: current
---

# Instruction generation

How commonplace instantiates build-time generation over runtime parameterisation in the shipped system. This note describes the scaffold, template substitution, and install entry point.

## The entry point

`commonplace-init` is the single build/install step. It creates the project directory structure, copies scaffold trees verbatim, and resolves a small set of templates with per-project values. Everything a new commonplace project needs is produced by this one command.

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

`commonplace-init` produces three kinds of output:

**Directories** (from `DEFAULT_DIRS`) — empty directory shells that practitioners fill in:

- `kb/types/`, `kb/notes/`, `kb/notes/types/`, `kb/sources/`, `kb/sources/types/`
- `kb/tasks/backlog/`, `kb/tasks/active/`, `kb/tasks/completed/`
- `kb/work/`, `kb/instructions/`, `kb/reports/`
- `kb/reference/`, `kb/reference/types/` (added when the reference collection shipped)

**Scaffold trees** — copied from packaged scaffold assets:

- `kb/instructions/` — skill definitions and procedural guidance
- `kb/types/` — global types (`text`, `note`, `instruction`, `definition`, `index`)
- `kb/reference/` — the reference collection's type definitions and reference docs

**Resolved templates** — read, substituted, written:

- `AGENTS.md.template` → `AGENTS.md.template` in the target root (practitioner then copies or renames to `AGENTS.md`)
- `.envrc.template` → `.envrc`
- packaged qmd collections template → `qmd-collections.yml` with `/PATH/TO/COMMONPLACE/` resolved to the actual root path

The two template sources live in different package subdirectories (`scaffold/` for the KB-facing templates, `assets/` for tooling config) but both flow through the same `_write_template` helper with the same replacements dictionary.

## Skill promotion

In addition to copying the instructions tree, `init_project` promotes a selected subset of skills (`write`, `validate`, `connect`, `convert`, `ingest`, `snapshot-web`, `revise-iterative`) into runtime discovery directories for multiple harnesses:

- `.claude/skills/cp-skill-<skill>/`
- `.agents/skills/cp-skill-<skill>/`

The promotion is a recursive file copy, not a symlink. Each destination gets an independent copy with the `cp-skill-` prefix applied to the skill name. This keeps skill discovery working in each runtime without relying on a shared live directory.

## Re-running init

`init_project` is idempotent-ish. Existing files are classified into three groups by `_record_existing`:

- **Identical to scaffold** — silently preserved
- **Different from scaffold** — preserved without overwriting, reported as "preserved existing files differing from current scaffold output" so the operator can decide whether to diff and update manually
- **Missing** — created fresh

The rule is "never clobber a practitioner edit." Updating an installed project to a newer commonplace release is a manual diff-and-merge step, not a re-run.

## What's not generated

A short list of things that are still authored by hand rather than generated:

- Static-site navigation configuration, if a project publishes the KB as a site
- Per-project customisation of the `## KB Goals` section in a generated `AGENTS.md` — the template carries placeholder prose; the practitioner fills in real values

These could all move to generated form later, but the current build-time step covers the cases where runtime parameterisation would have cost the most interpretation overhead: paths in skills, qmd collection roots, and the project name stamped across multiple files.

---

Relevant Notes:

- [014-scripts-as-python-package-one-tree-model](./adr/014-scripts-as-python-package-one-tree-model.md) — decision: shipping scripts as an installable Python package and consolidating scaffold into one tree
- [013-skills-first-delivery-with-core-local-type-split](./adr/013-skills-first-delivery-with-core-local-type-split.md) — decision: the skills-first delivery model and the core/local type split that `SCAFFOLD_TREES` and `PROMOTED_SKILLS` implement
- [006-two-tree-installation-layout](./adr/006-two-tree-installation-layout.md) — decision: the installation layout that `commonplace-init` produces
- [architecture](./architecture.md) — shipped architecture: where the generation pipeline sits inside the installed surface
- [control-plane-goals](./control-plane-goals.md) — how the generated `AGENTS.md.template` carries the `## KB Goals` section for practitioners to fill in
