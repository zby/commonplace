---
description: How commonplace is structured and installed — repo layout, two-tree split, control-plane design, file-based storage
type: index
index_source: tag
index_key: architecture
status: current
---

# Architecture

How commonplace is structured and installed. Repo layout, the two-tree split between user content and framework, control-plane design, and the file-based storage decision.

## Notes

- [commonplace-architecture](../reference/architecture.md) — the commonplace repo structure: kb/, scripts/, and how they compose
- [006-two-tree-installation-layout](../reference/adr/006-two-tree-installation-layout.md) — how commonplace installs into projects: two-tree layout, copy-vs-reference boundary, design rationale
- [010-review state should move to sqlite once reviews leave git and accumulate operational metadata](../reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and-accumulate-operational-metadata.md) — review storage crosses the files-first boundary once reviews are gitignored operational state keyed by `(note, gate, model)`
- [kb-goals-in-always-loaded-context-guide-inclusion-decisions](./kb-goals-in-always-loaded-context-guide-inclusion-decisions.md) — installed KBs need explicit domain goals in the control-plane file
- [files-not-database](./files-not-database.md) — files with git beat a database: universal interface, free versioning, zero infrastructure
- [agents-md-should-be-organized-as-a-control-plane](./agents-md-should-be-organized-as-a-control-plane.md) — theory for AGENTS.md as a control plane: invariants, routing, escalation boundaries
- [instruction-specificity-should-match-loading-frequency](./instruction-specificity-should-match-loading-frequency.md) — CLAUDE.md should be a slim router; match instruction specificity to loading frequency
- [generate-instructions-at-build-time](./generate-instructions-at-build-time.md) — generate CLAUDE.md and routing tables at build time rather than maintaining them by hand
- [scenario-decomposition-drives-architecture](./scenario-decomposition-drives-architecture.md) — concrete use cases decomposed into step-by-step context needs

## Other tagged notes <!-- generated -->

- [Agent runtimes decompose into scheduler context engine and execution substrate](./agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) — Practitioner runtime taxonomies converge on three separable components — scheduler, context engine, and execution substrate — because each solves a different class of model limitation
- [Always-loaded context mechanisms in agent harnesses](./always-loaded-context-mechanisms-in-agent-harnesses.md) — Survey of always-loaded context mechanisms across agent harnesses — system prompt files, capability descriptions, memory, and configuration injection — cataloguing what each carries, how write policies differ, and where the gaps are
