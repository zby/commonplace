---
description: How Commonplace is structured and installed — repo layout, two-tree split, control-plane design, file-based storage
type: kb/types/index.md
index_source: tag
index_key: architecture
status: current
---

# Architecture

How Commonplace is structured and installed. Repo layout, the two-tree split between user content and framework, control-plane design, and the file-based storage decision.

For current-state subsystem documentation and ADR navigation, start at [../reference/README.md](../reference/README.md).

## Notes

- [reference overview](../reference/README.md) — entry point for current-state docs and architecture decisions
- [commonplace-architecture](../reference/architecture.md) — the Commonplace repo structure: KB collections, packaged runtime, shipped skills, and operational surfaces
- [006-two-tree-installation-layout](../reference/adr/006-two-tree-installation-layout.md) — how Commonplace installs into projects: two-tree layout, copy-vs-reference boundary, design rationale
- [010-review state should move to sqlite once reviews leave git and accumulate operational metadata](../reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) — review storage crosses the files-first boundary once reviews are gitignored operational state keyed by `(note, gate, model)`
- [kb-goals-in-always-loaded-context-guide-inclusion-decisions](./kb-goals-in-always-loaded-context-guide-inclusion-decisions.md) — installed KBs need explicit domain goals in the control-plane file
- [control-plane-goals](../reference/control-plane-goals.md) — current-state: how Commonplace realises KB goals in `AGENTS.md`, the scaffold template, and the install-time fill-in flow
- [files-not-database](./files-not-database.md) — files with git beat a database: universal interface, free versioning, zero infrastructure
- [storage-architecture](../reference/storage-architecture.md) — current-state: how Commonplace lays out files as source of truth, regenerable indexes, and the scoped SQLite review-state exception
- [agents-md-should-be-organized-as-a-control-plane](./agents-md-should-be-organized-as-a-control-plane.md) — theory for AGENTS.md as a control plane: invariants, routing, escalation boundaries
- [instruction-specificity-should-match-loading-frequency](./instruction-specificity-should-match-loading-frequency.md) — CLAUDE.md should be a slim router; match instruction specificity to loading frequency
- [generate-instructions-at-build-time](./generate-instructions-at-build-time.md) — generate CLAUDE.md and routing tables at build time rather than maintaining them by hand
- [instruction-generation](../reference/instruction-generation.md) — current-state: the Commonplace `commonplace-init` build step, scaffold trees, and substitution points that implement build-time generation today
- [scenario-decomposition-drives-architecture](./scenario-decomposition-drives-architecture.md) — concrete use cases decomposed into step-by-step context needs
- [scenario-architecture](../reference/scenario-architecture.md) — current-state: the two-tree split, the escalation path to `commonplace/kb/`, the `AGENTS.md` fragment contract, and the `test/scenarios/` measurement surface
