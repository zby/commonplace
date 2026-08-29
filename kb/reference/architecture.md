---
description: "Architecture boundaries of an installed Commonplace project: user KB, shipped library, command runtime, skill projections, and path invariance"
type: kb/types/note.md
traits: []
tags: []
---

# Commonplace architecture

An installed Commonplace project puts the user's KB and a read-only shipped
library in one project tree, while the Python command runtime remains a
user-level tool. This page records the boundaries among those surfaces. The
live `commonplace.scaffold_manifest` is the exact installed inventory, and
`commonplace.cli.init_project` owns materialization behavior; locate both from
an installed project with `commonplace-source`.

## Installed topology

```text
project/
  AGENTS.md.template                 practitioner integrates into the runtime control plane
  kb/
    commonplace/
      notes/                         shipped methodology
      reference/                     shipped system reference and ADRs
      instructions/                  shipped procedures and canonical cp-skill-* skills
    types/                           shared global contracts
    notes/ reference/ instructions/  user-owned library collections
    sources/ reports/                user-owned source and report collections
    tasks/ work/                     user-owned operating surfaces
    log.md                           user-owned operational log
  .agents/skills/ .claude/skills/    copied projections of selected shipped skills

user-level uv tool                   commonplace-* command runtime for every project
```

This is an orientation map, not a file manifest. `commonplace-init` output and
`commonplace.scaffold_manifest` own the exact directories, scaffold files, and
promoted-skill set. The operator decides whether to rename the generated
control-plane template to `AGENTS.md` or `CLAUDE.md`, merge it into an existing
file, or import it through another runtime mechanism.

## Ownership boundaries

The structural boundary is `kb/commonplace/`:

- `kb/commonplace/{notes,reference,instructions}/` is the framework library.
  The project reads it as a dependency and treats it as read-only by
  convention.
- Top-level `kb/notes/`, `kb/reference/`, `kb/instructions/`, `kb/sources/`,
  and `kb/reports/` are the project's own collections. Tasks, workshop
  material, and the log are also project-owned operating surfaces.
- `kb/types/` is shared ground. Commonplace installs the global contracts there
  and the project may extend them, so both library and user artifacts can keep
  the same absolute type identities.

The Python implementation is not vendored into the project. A user-level uv
tool installation supplies the active `commonplace-*` commands to every
project for that OS user. Project environments remain free to carry their own
application and development dependencies. [ADR 064](./adr/064-install-commonplace-commands-as-a-user-level-uv-tool.md)
owns that runtime choice; [commands](./commands.md) routes into the live command
surface.

## Materialization and skill projection

`commonplace-init` materializes the project-facing surfaces from one scaffold
manifest. Built distributions carry the canonical KB trees as package data;
an editable source checkout resolves the repository's canonical files instead
of maintaining a second authored scaffold copy. Existing project files are
preserved rather than synchronized automatically. Exact creation,
classification, and package-source behavior belongs to the live manifest and
init implementation.

Canonical skill definitions remain under
`kb/commonplace/instructions/cp-skill-*/`. Init copies the selected promoted
skills into the two known runtime discovery layouts. Those projections are not
another authoring authority. A runtime with a different discovery convention
must expose the same canonical directories through its own copy, registration,
or import mechanism.

This separation keeps the agent's normal read and write path inside the
project, while executable behavior still comes from the installed package.
The scaffold does not create a Commonplace-specific project environment.

## Path invariance across source and install

Commonplace authors its library at top-level collection paths in this source
repository, then installs those collections together under `kb/commonplace/`.
Three rules let the same artifacts work in both positions:

- sibling-relative Markdown links remain valid because the library collections
  move under one common wrapper;
- shared global type pointers remain absolute `kb/types/...` paths because
  that directory stays at top level; and
- collection-local type pointers remain file-relative, preserving the
  file-to-contract relationship after wrapping.

These are the stable architecture rules. Exact resolver branches and scaffold
path pairs belong to the implementation. [ADR 021](./adr/021-ship-library-content-under-kb-commonplace.md)
records why the namespace boundary and these path forms were selected.

## Maintenance scope

Review this page when library/user ownership, command-runtime placement,
canonical skill ownership, projection semantics, or the path-invariance rules
change. A new scaffold directory, template, promoted skill, package-data
mapping, installer step, or command does not by itself require an edit; its
live owner remains the manifest, source, package metadata, or command help.

## See also

- [Instruction generation](./instruction-generation.md) — current scaffold and template flow
- [Storage](./storage-architecture.md) — authority and lifecycle after artifacts are installed
- [Scenario architecture](./scenario-architecture.md) — the common agent path through the installed surfaces
- [ADR 027](./adr/027-package-scaffold-assets-without-source-tree-symlinks.md) — package-data and editable-source boundary
- [Collections and types](./collections-and-types.md) — exact type identity and resolution contract
