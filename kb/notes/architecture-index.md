---
description: How commonplace is structured and installed — repo layout, two-tree split, control-plane design, file-based storage
type: index
status: current
---

# Architecture

How commonplace is structured and installed. Repo layout, the two-tree split between user content and framework, control-plane design, and the file-based storage decision.

## Notes

- [commonplace-architecture](./commonplace-architecture.md) — the commonplace repo structure: kb/, scripts/, and how they compose
- [commonplace-installation-architecture](./commonplace-installation-architecture.md) — how commonplace installs into projects: symlinks, CLAUDE.md generation, directory layout
- [kb-goals-in-always-loaded-context-guide-inclusion-decisions](./kb-goals-in-always-loaded-context-guide-inclusion-decisions.md) — installed KBs need explicit domain goals in the control-plane file
- [files-not-database](./files-not-database.md) — files with git beat a database: universal interface, free versioning, zero infrastructure
- [agents-md-should-be-organized-as-a-control-plane](./agents-md-should-be-organized-as-a-control-plane.md) — theory for AGENTS.md as a control plane: invariants, routing, escalation boundaries
- [instruction-specificity-should-match-loading-frequency](./instruction-specificity-should-match-loading-frequency.md) — CLAUDE.md should be a slim router; match instruction specificity to loading frequency
- [generate-instructions-at-build-time](./generate-instructions-at-build-time.md) — generate CLAUDE.md and routing tables at build time rather than maintaining them by hand
- [scenarios](./scenarios.md) — concrete use cases the knowledge system must serve

## Other tagged notes <!-- generated -->

- [Agent runtimes decompose into scheduler context engine and execution substrate](./agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) — Practitioner runtime taxonomies converge on three separable components — scheduler, context engine, and execution substrate — because each solves a different class of model limitation
