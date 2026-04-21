---
description: Shipped commonplace architecture — installed project layout, packaged runtime, scaffolded KB surface, promoted skills, and the boundary between framework-provided artifacts and practitioner-authored content
type: kb/types/note.md
traits: []
tags: []
status: current
---

# Commonplace architecture

This note describes the architecture commonplace ships into projects: the installed `kb/` tree, the package-provided command surface, and the runtime skill-discovery layer.

## Installed project layout

```text
project/
    kb/
      types/                         ← global types (`text`, `note`, `instruction`, ...)
      notes/
        types/
        *.md
      reference/
        adr/
        types/
        *.md
      sources/
        types/
        *.md
      tasks/
        types/
        backlog/
        active/
        completed/
        recurring/
      work/
      reports/
      instructions/
      log.md
    .claude/skills/cp-skill-*/    ← promoted framework skills
    .agents/skills/cp-skill-*/    ← promoted framework skills
    AGENTS.md                        ← project control-plane file
    .envrc                           ← project environment for local commands
```

The installed project is a one-tree KB surface. The framework implementation itself is not vendored into the project as a sibling checkout; it is provided by the installed Python package and exposed through `commonplace-*` commands.

## Surface by role

| Area | Role |
|------|------|
| `kb/notes/` | Project-authored transferable claims, theory, and methodology |
| `kb/reference/` | Framework reference docs plus ADR history, extended locally when needed |
| `kb/instructions/` | Framework-shipped procedures, promoted skills, and operator guidance |
| `kb/types/` | Global type contracts shared across collections |
| `kb/*/types/` | Collection-local structural contracts for specialised documents |
| `kb/sources/` | Ingested external sources and source reviews |
| `kb/tasks/` | Task lifecycle artifacts |
| `kb/work/` | Temporal workshop material and explorations |
| `kb/reports/` | Generated operational artifacts rather than curated knowledge |
| `.claude/skills/`, `.agents/skills/` | Runtime discovery copies of the shipped skill set |

## How the shipped surface is produced

`commonplace-init` is the install step that materialises the KB surface inside a project.

It does three things:

1. Creates the directory shell under `kb/`.
2. Copies scaffolded framework artifacts into the project: `kb/instructions/`, `kb/types/`, `kb/reference/`, and the collection-local `types/` directories.
3. Promotes selected skills into `.claude/skills/cp-skill-*/` and `.agents/skills/cp-skill-*/`, and resolves project-specific templates such as `AGENTS.md` and `.envrc`.

The result is that the agent's hot path stays inside the project tree. It reads `AGENTS.md`, the target collection's `COLLECTION.md`, and the relevant type files directly from the installed KB rather than jumping out to a separate framework checkout.

## Boundary between framework and authored content

The shipped system deliberately mixes two classes of files inside one `kb/` tree:

- **Framework-provided starting points** — `kb/instructions/`, `kb/types/`, `kb/reference/`, and collection-local `types/` directories.
- **Project-authored content** — notes, sources, tasks, workshop material, reports, and any local extensions or edits the project adds.

This is a practical boundary, not a hard filesystem fence. The project owns the whole tree once installed. The important distinction is update semantics:

- Re-running `commonplace-init` can add newly shipped files.
- Existing project files are preserved rather than overwritten.
- Local adaptations to shipped files therefore become part of the project's own system description.

## Why `kb/reference/` is part of the shipped surface

The old two-tree design treated framework explanation as something that lived outside the installed KB. The shipped one-tree model no longer has that escape hatch. If the installed system needs reference documentation about how its own architecture works, that documentation must ship into the same tree the agent already searches.

That is why `kb/reference/` belongs to the shipped surface alongside `kb/instructions/` and `kb/types/`: it is the explanatory layer for the installed system itself.

---

Relevant Notes:

- [Reference](./README.md) — overview of the shipped reference collection and operator guide
- [014-scripts-as-python-package-one-tree-model](./adr/014-scripts-as-python-package-one-tree-model.md) — decision: the package-and-init model this architecture describes
- [013-skills-first-delivery-with-core-local-type-split](./adr/013-skills-first-delivery-with-core-local-type-split.md) — decision: the skills-first model and the core/local type split
- [type-loading](./type-loading.md) — how the shipped type definitions are discovered within this architecture
