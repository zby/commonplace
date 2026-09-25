---
description: "Architecture boundaries of an installed Commonplace project: the user KB, the library read in place from the installed package, init's machine-specific pointers into it, the command runtime, and path invariance"
type: types/note.md
traits: []
tags: []
---

# Commonplace architecture

An installed Commonplace project holds only the user's KB. The Commonplace
library and the Python command runtime both come from one user-level tool
installation, and the project reads the library in place. This page records
the boundaries among those surfaces. The live `commonplace.scaffold_manifest`
is the exact inventory of what init writes, `commonplace.cli.init_project`
owns that behavior, and `commonplace.lib.library` locates the library; find
them from an installed project with `commonplace-source`.

In this page, *the library* means everything Commonplace owns and a project
only reads: the notes, reference, and instructions collections, the global
types and their schemas, the review gates, the critique instruction, and the
promoted skills.

## Installed topology

```text
project/
  AGENTS.md CLAUDE.md                committed control plane, from init's templates
  kb/
    notes/ reference/ instructions/  user-owned collections
    sources/ reports/                user-owned collections, with their local types
    tasks/ work/                     user-owned operating surfaces
    log.md                           user-owned operational log
  .claude/skills/ .agents/skills/    skill stubs pointing into the library (uncommitted)
  .commonplace/library.md            library root, entry points, skill index (uncommitted)
  .claude/settings.local.json        Claude Code read rule for the library root (uncommitted)

user-level uv tool
  commonplace-* commands             command runtime for every project
  share/commonplace/                 the library, laid out like the source repository's kb/:
    instructions/ notes/ reference/ types/
```

This is an orientation map, not a file manifest. `commonplace-init` output and
`commonplace.scaffold_manifest` own the exact directories, scaffold files, and
promoted-skill set. The operator decides whether to rename the generated
control-plane templates to `AGENTS.md` and `CLAUDE.md`, merge them into
existing files, or carry their content through another runtime mechanism.

## Ownership boundaries

The structural boundary is the project root:

- Everything under the project's `kb/` belongs to the project: the notes,
  reference, instructions, sources, and reports collections with their
  collection-local types, and the tasks, workshop, and log surfaces.
- The library lives in the tool installation, outside every project. The
  project never holds a copy, so the library cannot diverge from the commands
  that read it, and project searches and `git status` show only project files.
- The files init writes into the project to reach the library (stubs,
  `.commonplace/library.md`, the read rule) name paths on one machine. They are
  gitignored and rewritten by init; they are pointers, not library content.

The Python implementation is not vendored into the project either. A
user-level uv tool installation supplies the active `commonplace-*` commands
and the library to every project for that OS user. Project environments remain
free to carry their own application and development dependencies. [ADR 064](./adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md)
owns that runtime choice; [commands](./commands.md) routes into the live command
surface.

## Where the library is read

A built wheel installs the library as shared data under
`<tool environment>/share/commonplace/`. That path does not change with the
tool's Python version or on upgrade. An editable install reads the source
checkout's `kb/` instead, because shared data is copied at install time. The
environment variable `COMMONPLACE_LIBRARY_ROOT` overrides both; tests use it.

Commands read gates, the critique instruction, and global types from the
library root. Agents reach it by two routes, both written by `commonplace-init`:

- **Base layer, for every runtime.** `.commonplace/library.md` gives the
  library root, its entry points, and an index of the skills with each
  `SKILL.md` path. The committed `AGENTS.md` tells agents to read it, and the
  committed `CLAUDE.md` imports it so Claude Code has the paths in context from
  the start of a session. An agent in a runtime without a skills mechanism
  uses the skill index in place of native skills.
- **Skills layer, where the runtime discovers Agent Skills.** Init writes a
  stub `SKILL.md` for each promoted skill and for the router skill
  `cp-skill-library` into `.claude/skills/` and `.agents/skills/`. The stub
  carries the real skill's frontmatter, so the harness applies it, and tells
  the agent to read the real `SKILL.md` by absolute path and follow it. The
  skill therefore runs in place in the library.

In Claude Code, reading outside the project needs a permission rule, so init
also writes a `Read(//<library root>/**)` allow rule into
`.claude/settings.local.json`. Codex's default sandbox allows the reads.

## Keeping init's outputs current

No hook refreshes init's outputs, so the system detects staleness and names
the repair. Every `commonplace-*` command recomputes what init would write for
the current project and warns when a stub is missing, extra, or stale, when
`.commonplace/library.md` is stale, or when the read rule names another root.
`commonplace-init --check` reports the same states without writing. Rerunning
`commonplace-init` rewrites the outputs; it never overwrites the project's own
files.

The check runs when a command runs, not when an agent reads a file. After a
switch between an editable and a normal install, the library root moves, and
an agent can read the old root until init reruns. That is why the install
procedure says to rerun init immediately after such a switch.

## Path invariance across source and install

Commonplace authors its library at top-level collection paths in this source
repository, and the installed library mirrors that `kb/` layout. Two rules
let the same artifacts work in both places:

- relative Markdown links resolve the same way in both trees, including links
  from a skill to its own files, to other instructions, and to types, because
  an agent reads a skill at its real location rather than through a copy;
- a type value is the spec's path under a KB root, such as `type: types/note.md`
  or `type: reference/types/adr.md`, found on a search path of the library root
  (global `types/<name>.md` only) and the artifact's KB root; in the source
  repository both roots are `kb/`.

Review criteria follow the same split. A criterion file inside the repository
is identified by its repository-relative path; a criterion file in the
installed library is identified relative to the library root, such as
`commonplace:instructions/review-gates/prose/source-residue.md`. The identity
contains no version and no machine path, so it survives upgrades and moves of
the installation.

These are the stable architecture rules. Exact resolver branches and scaffold
entries belong to the implementation. [Collections and types](./collections-and-types.md)
states the type-resolution contract.

## Maintenance scope

Review this page when library/user ownership, command-runtime placement, where
the library is read, the stub and routing-file mechanism, or the
path-invariance rules change. A new scaffold directory, template, promoted
skill, package-data mapping, installer step, or command does not by itself
require an edit; its live owner remains the manifest, source, package
metadata, or command help.

## See also

- [Instruction generation](./instruction-generation.md) — what `commonplace-init` writes and how templates are resolved
- [Storage](./storage-architecture.md) — authority and lifecycle after artifacts are installed
- [Scenario architecture](./scenario-architecture.md) — the common agent path through the installed surfaces
- [ADR 027](./adr/027-package-scaffold-assets-without-source-tree-symlinks.md) — package-data and editable-source boundary
- [Collections and types](./collections-and-types.md) — exact type identity and resolution contract
