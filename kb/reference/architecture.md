---
description: Current repo layout and operational surface — authored KB content, packaged runtime, shipped skills, and the boundary between commonplace itself and installed projects
type: note
traits: []
tags: [architecture]
status: current
---

# Commonplace architecture

The commonplace repo is itself a knowledge base and the framework implementation that ships into other projects. This note describes the repo as it exists today, distinct from the [two-tree installation layout](./adr/006-two-tree-installation-layout.md) that appears when commonplace is installed elsewhere.

## Current layout

```text
commonplace/
    kb/
      types/                         ← global base types (`text`, `note`)
      notes/                         ← transferable theory and methodology
        types/
        definitions/
        related-systems/
        research/
        *.md
      reference/                     ← current-state docs + ADRs for this repo
        adr/
        types/
        *.md
      sources/                       ← source snapshots and source-review notes
        types/
        *.md
      tasks/                         ← task artifacts; status encoded by directory
        types/
        backlog/
        active/
        completed/
        recurring/
      work/                          ← workshop material and design explorations
      reports/                       ← generated review and fix artifacts
      instructions/                  ← searchable procedures and promoted skills
      log.md                         ← improvement log
    src/commonplace/                 ← packaged CLI, library, review system, assets, scaffold
    skills/                          ← shipped framework skill source files
    test/                            ← CLI/lib/review tests
    related-systems/                 ← checked-out external repos for review work
    AGENTS.md                        ← project control-plane file
    README.md                        ← external project overview
```

## Repo surface by role

| Area | Role |
|------|------|
| `kb/notes/` | Transferable claims, theory, and methodology |
| `kb/reference/` | Current-state docs and decision history for the live commonplace system |
| `kb/instructions/` | Procedures, skills, and operator guidance |
| `kb/work/` | Temporal workshop material and exploratory design work |
| `kb/reports/` | Generated operational artifacts rather than curated knowledge |
| `src/commonplace/` | Packaged implementation of the CLI, library, review system, and scaffold |
| `skills/` | Framework skill sources that get installed into agent environments |

## Global types live under kb/types/

Installed projects keep Commonplace's structural surface inside `kb/`, rather than adding extra top-level directories. That keeps instructions, global base types, directory-local types, and authored artifacts in one subtree.

The distinction still matters:

- **Collection types** (`notes/types/`, `sources/types/`, `tasks/types/`) define concrete structural templates the agent reads when creating a specific document kind.
- **Global types** (`kb/types/`) define the shared base layer: the `text`/`note` maturity boundary plus the shared `note` schema and template.

The tradeoff is one extra directory under `kb/`, but it avoids a more intrusive top-level `types/` directory in installed projects. That is the better default for installation ergonomics.

## Commonplace versus installed projects

The commonplace repo carries both methodology content and the framework implementation. Installed projects get the framework surface plus empty or project-local content areas.

- Installed projects get scaffolded `kb/`, shipped skills, and generated control-plane files.
- They do not inherit commonplace's theory library, workshop history, or review artifacts as their own authored content.
- `kb/reference/` is now part of the installed collection contract: practitioners can document their own current system there and keep ADRs in the same collection.

---

Relevant Notes:

- [Reference](./README.md) — entry point for the current-state docs and ADR collection
- [006-two-tree-installation-layout](./adr/006-two-tree-installation-layout.md) — the two-tree design for installed projects; this note covers the repo's own layout
- [directory-scoped types are cheaper than global types](../notes/directory-scoped-types-are-cheaper-than-global-types.md) — foundation: why collection-level types/ directories work but a global types/ directory is overhead
- [instruction specificity should match loading frequency](../notes/instruction-specificity-should-match-loading-frequency.md) — constrains: what goes in the control plane versus on-demand docs
