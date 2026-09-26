---
description: How Commonplace is structured and installed — repo layout, two-tree split, control-plane design, file-based storage
type: types/tag-readme.md
---

# Architecture

How Commonplace is structured and installed: the repository layout, the user's KB living in the project while the library is read in place from the installed package (ADR 086), the control plane in `AGENTS.md`, and the file-based storage decision. Nearby but different: [computational-model](./computational-model-README.md) is about what runs, not where it lives.

For current-state subsystem documentation and ADR navigation, start at [../reference/README.md](../reference/README.md).

## Notes

- [reference overview](../reference/README.md) — entry point for current-state docs and architecture decisions
- [commonplace-architecture](../reference/architecture.md) — the Commonplace repo structure: KB collections, packaged runtime, shipped skills, and operational surfaces
- [086-projects read the library from the installed package](../reference/adr/086-projects-read-the-library-from-the-installed-package.md) — how Commonplace installs into projects today: no copy, init-written stubs and a routing file pointing at the installed library; supersedes the two-tree layout of ADR 006 and the one-tree model of ADR 014
- [010-review state should move to sqlite once reviews leave git and accumulate operational metadata](../reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) — review operational state crosses a deliberate authority boundary once acknowledgements and indexed transitions keyed by `(note, criterion, model_partition)` become database-owned
- [kb-goals-in-always-loaded-context-guide-inclusion-decisions](../notes/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md) — installed KBs need explicit domain goals in the control-plane file
- [control-plane-goals](../reference/control-plane-goals.md) — current-state: how Commonplace realises KB goals in `AGENTS.md`, the scaffold template, and the install-time fill-in flow
- [files-defer-centralized-schema-commitment-until-invariants-stabilize](../notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md) — canonical files can defer a shared schema while meanings remain unsettled; database authority is a separate commitment made through an operative write path, not a consequence of invariant shape or unowned state
- [storage-architecture](../reference/storage-architecture.md) — current-state: how Commonplace lays out files as source of truth, regenerable indexes, and the scoped SQLite review-state exception
- [agents-md-should-be-organized-as-a-control-plane](../notes/agents-md-should-be-organized-as-a-control-plane.md) — theory for AGENTS.md as a control plane: invariants, routing, escalation boundaries
- [instruction-specificity-should-match-loading-frequency](../notes/instruction-specificity-should-match-loading-frequency.md) — CLAUDE.md should be a slim router; match instruction specificity to loading frequency
- [generate-instructions-at-build-time](../notes/generate-instructions-at-build-time.md) — generate CLAUDE.md and routing tables at build time rather than maintaining them by hand
- [instruction-generation](../reference/instruction-generation.md) — current-state: the Commonplace `commonplace-init` build step, scaffold trees, and substitution points that implement build-time generation today
- [scenario-decomposition-drives-architecture](../notes/scenario-decomposition-drives-architecture.md) — concrete use cases decomposed into step-by-step context needs
- [scenario-architecture](../reference/scenario-architecture.md) — current-state: the scenario-derived shipped architecture, the user's KB in the project with the library read from the package, package commands, promoted skills, and the `tests/scenarios/` measurement surface
