---
description: Commonplace's build-time instruction generation — template substitution, the project files `commonplace-init` creates once, and the machine-specific pointers into the installed library it rewrites on every run
type: note
tags: []
---

# Instruction generation

How Commonplace instantiates build-time generation over runtime parameterisation in the shipped system. This note describes the scaffold, template substitution, the pointers into the installed library, and the install entry point.

## The entry point

`commonplace-init` is the single project-setup step. It creates the project directory structure, copies the project's own scaffold files, resolves a small set of templates with per-project values, and writes machine-specific pointers into the installed Commonplace library. Command installation is separate and user-level: uv installs the Python package, which also carries the library, before this command runs. The library itself is not copied into the project; see [architecture](./architecture.md).

There are no runtime variables in the generated artifacts. `AGENTS.md`, the skill stubs, `.commonplace/library.md`, and configuration files contain literal paths and names by the time an agent sees them.

## Substitution points

`init_project` resolves three placeholder kinds during template processing:

| Placeholder | Replaced with | Source |
|---|---|---|
| `<your-project>` | Project directory name (or `--name` override) | CLI argument or `root.name` |
| `{{project_name}}` | Same | same |
| `/PATH/TO/COMMONPLACE/` | Absolute path to the project root, with trailing slash | `root` resolved to absolute path |

Substitution is a flat string replace in `_write_template`. Files that don't need substitution (scaffold trees and files) are copied byte-for-byte instead.

## Project files created once

These outputs belong to the project. Init creates each one only when it is missing.

**Directories** (from `MANIFEST.directories`) — empty directory shells the practitioner fills in:

- `kb/notes/`, `kb/notes/types/` — user's notes collection
- `kb/reference/`, `kb/reference/types/` — user's reference collection
- `kb/instructions/` — user's instructions collection
- `kb/sources/`, `kb/sources/types/` — user's tracked source records and local-capture type contracts
- `kb/tasks/backlog/`, `kb/tasks/active/`, `kb/tasks/completed/` — user's task lifecycle
- `kb/work/` — user's workshop surface
- `kb/reports/`, its `cache/`, `state/`, and `retained/` policy areas, and `kb/reports/types/` — user's reports collection

**Scaffold trees** — copied from scaffold sources. In a built wheel these sources live under packaged `commonplace/_data/`; in an editable source checkout `commonplace-init` falls back to the canonical repo paths:

- `kb/reports/types/`, `kb/sources/types/` — collection-local type definitions for user-space collections. Their schemas build on global schemas through `commonplace:types/...` references, which resolve in the installed library.

**Scaffold files** — individual files copied into the user's collections:

- `kb/reports/COLLECTION.md`, `README.md`, policy-area READMEs, `.gitignore`,
  and validation-ignore markers — the report retention contract and local
  output boundaries
- `kb/sources/.gitignore` — ignores the local `.snapshots/` materialization directory
- `kb/sources/COLLECTION.md` — generic tracked-source and local-capture contract
- `kb/sources/README.md` — curated empty-state landing
- `kb/notes/COLLECTION.md` — minimal theoretical/descriptive/prescriptive template
- `kb/notes/README.md` — curated empty-state landing
- `kb/reference/COLLECTION.md` — minimal template
- `kb/reference/README.md` — curated empty-state landing
- `kb/instructions/COLLECTION.md` — minimal template
- `kb/instructions/README.md` — curated empty-state landing
- `kb/work/COLLECTION.md` — workshop-layer contract: structure, closing, and loose linking
- `kb/work/README.md` — active-workshops landing

The notes, reference, and instructions `COLLECTION.md` templates invite the practitioner to state the collection's purpose, intended contribution, quality goal, and outbound link rules; the library's own `COLLECTION.md` files serve as worked examples. The sources contract instead supplies generic rules for tracked source analyses and ignored immutable captures. The reports contract supplies cache, state, retained, and local-type policies. Each `README.md` supplies the collection's stable reader landing, points authors to its local contract, and states the collection's initial contents.

**Resolved templates** — read, substituted, written:

- `AGENTS.md.template` → `AGENTS.md.template` in the target root (practitioner then renames it to `AGENTS.md` or merges it into an existing file)
- `CLAUDE.md.template` → `CLAUDE.md.template` in the target root; it imports `AGENTS.md` and `.commonplace/library.md`, so Claude Code has the library paths in context from the start of a session

The templates flow through `_write_template` with the replacements dictionary. The committed control-plane files name no machine path; they point to `.commonplace/library.md`. The scaffold creates no `.envrc` or Commonplace-specific project venv; command discovery belongs to the user-level uv tool installation.

## Pointers into the library, rewritten on every run

These outputs name paths on one machine, so init rewrites them on every run and adds them to `.gitignore`:

- **Skill stubs.** For each promoted skill in `MANIFEST.promoted_skills`, and for the router skill `cp-skill-library`, init writes `.claude/skills/<skill>/SKILL.md` and `.agents/skills/<skill>/SKILL.md`. A stub copies the real skill's frontmatter, so the harness applies its name, description, and execution settings, and tells the agent to read the real `SKILL.md` by absolute path and follow it, resolving relative links against that file. A marker file beside the stub records that init wrote it. Init removes marked stubs for skills the package no longer has. It does not write a stub into a skill directory without the marker; it reports that directory instead.
- **`.commonplace/library.md`.** The library root, the library's entry points, and a skill index giving each skill's name, description, and `SKILL.md` path. A runtime without a skills mechanism uses this index in place of the stubs.
- **The Claude Code read rule.** A `Read(//<library root>/**)` allow rule in `.claude/settings.local.json`. Init records the rule it wrote in `.commonplace/read-rule`, so a rerun for a new root replaces its own earlier rule and leaves other entries alone.

The canonical skill is the directory under the library's `instructions/`, not the stubs. A runtime that discovers skills elsewhere has no stubs from init; its agents use the skill index in `.commonplace/library.md`.

## Scaffold source resolution

The source tree does not keep symlinked copies of the project scaffold under `src/commonplace/_data/`. Instead, `init_project` resolves each scaffold input by checking two locations:

1. `commonplace/_data/<path>` — packaged wheel data, populated by Hatch `force-include` entries from canonical repo paths. The sdist also explicitly includes those canonical inputs so wheels built from sdists have the same scaffold source.
2. The canonical repo path — used in editable source checkouts, so edits to `kb/reports/types/`, `kb/sources/types/`, and the root templates are picked up without duplicating files.

The exception is `src/commonplace/_data/templates/`, which contains real scaffold-only files for the user collections' starter `COLLECTION.md` contracts and `README.md` landings and for the `CLAUDE.md` template. Those files have no canonical counterpart elsewhere in the KB.

The library is not a scaffold input. The wheel installs it as shared data under `<tool environment>/share/commonplace/`, and an editable install reads the source checkout's `kb/`.

## Re-running init

Init treats its two kinds of output differently.

The project's own files are never overwritten. Existing files are classified into three groups by `_record_existing`:

- **Identical to scaffold** — silently preserved
- **Different from scaffold** — preserved without overwriting, reported as "preserved existing files differing from current scaffold output" so the operator can decide whether to diff and update manually
- **Missing** — created fresh

The pointers into the library are rewritten whenever they differ from what init would write now, and reported as refreshed. `commonplace-init --check` compares them without writing, and every `commonplace-*` command runs the same comparison and warns when they are stale.

A rerun also migrates library copies left by earlier releases. Init removes each copied file that matches the installed library and keeps and lists each one that differs, because it may carry a local change. It retires, once, the review baselines whose criteria were files in the copy.

`.envrc` is outside the current manifest, so re-running init neither inspects nor changes it.

## What's not generated

A short list of things that are still authored by hand rather than generated:

- Static-site navigation configuration, if a project publishes the KB as a site
- Per-project customisation of the `## KB Goals and Scope` section in a generated `AGENTS.md` — the template carries placeholder prose; the practitioner fills in real values

These could all move to generated form later, but the current build-time step covers the cases where runtime parameterisation would have cost the most interpretation overhead: the library paths in skill stubs, the routing file, and the read rule, and the project name stamped into the control-plane template.

---

Relevant Notes:

- [014-scripts-as-python-package-one-tree-model](./adr/014-scripts-as-python-package-one-tree-model.md) — decision: shipping scripts as an installable Python package and consolidating scaffold into one tree
- [027-package-scaffold-assets-without-source-tree-symlinks](./adr/027-package-scaffold-assets-without-source-tree-symlinks.md) — decision: package scaffold assets with explicit wheel includes and source-checkout fallback instead of source-tree symlinks
- [064-install-commonplace-commands-as-a-user-level-uv-tool](./adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md) — decision: user-level command installation and removal of project command-environment scaffolding
- [013-skills-first-delivery-with-core-local-type-split](./adr/013-skills-first-delivery-with-core-local-type-split.md) — decision: the skills-first delivery model and the core/local type split that `MANIFEST.trees` and `MANIFEST.promoted_skills` implement
- [006-two-tree-installation-layout](./adr/006-two-tree-installation-layout.md) — decision: the installation layout that `commonplace-init` produces
- [architecture](./architecture.md) — shipped architecture: where the generation pipeline sits inside the installed surface
- [control-plane-goals](./control-plane-goals.md) — how the generated `AGENTS.md.template` carries the `## KB Goals and Scope` section for practitioners to fill in
