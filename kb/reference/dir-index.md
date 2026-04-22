---
description: Auto-generated directory - run commonplace-refresh-indexes to rebuild
type: kb/types/index.md
index_source: directory
---

# Reference Directory

← [Parent](../index.md)

## Subdirectories

- [adr/](./adr/dir-index.md)
- [definitions/](./definitions/dir-index.md)

## Files

- [Available types](./available-types.md) *(note)* - Catalog of the types shipped by commonplace — global base and utility types plus directory-scoped specialised types delivered with the framework scaffold
- [Collections and types](./collections-and-types.md) *(note)* - How collections and types compose in commonplace - collections own register conventions and link rules, types own structural contracts declared in type-spec docs, and the two meet through path-valued type pointers listed in COLLECTION.md; covers the COLLECTION.md surface, the compiled collection-topology used by the connect skill, and the compile-collections skill that produces it
- [Commonplace architecture](./architecture.md) *(note)* - Shipped commonplace architecture — installed project layout, packaged runtime, scaffolded KB surface, promoted skills, and the boundary between framework-provided artifacts and practitioner-authored content
- [Commonplace CLI commands](./commands.md) *(note)* - Reference for the commonplace-* CLI commands shipped by llm-commonplace - project setup, validation, indexing, snapshots, note operations, and the review system
- [Commonplace library (`commonplace.lib`)](./lib-modules.md) *(note)* - Internal API reference for commonplace.lib - frontmatter, naming, note_parser, type_resolver, validation, and relocation modules used by CLI commands and the review system
- [Control-plane goals](./control-plane-goals.md) *(note)* - How commonplace ships KB goals in always-loaded context — the AGENTS.md layout, the scaffolded AGENTS.md.template, and the install-time fill-in contract
- [Instruction generation](./instruction-generation.md) *(note)* - Commonplace's shipped build-time instruction generation flow — scaffold trees, template substitution, the `commonplace-init` entry point, and the specific generated artifacts
- [Review system architecture (`commonplace.review` + `commonplace.cli.review`)](./review-architecture.md) *(note)* - Code architecture for commonplace.review and commonplace.cli.review - package layout, data model, single-note bundle execution, targeting, prompt format, and repair utilities
- [Scenario architecture](./scenario-architecture.md) *(note)* - Scenario-derived shipped architecture — one-tree installed KB, package-provided commands, promoted skills, and a measurable scenario decomposition
- [Storage](./storage-architecture.md) *(note)* - Where commonplace stores data — authored markdown under kb/, derived indexes rebuilt from those files, and the review subsystem's local SQLite database
- [Type loading](./type-loading.md) *(note)* - How commonplace resolves a note's type contract at authoring and validation time - collection-scoped lookup, collection conventions, and skill-driven on-demand loading
- [Writing conventions for kb/reference/ (descriptive register)](./COLLECTION.md)
