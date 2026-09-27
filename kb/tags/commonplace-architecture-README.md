---
description: "How Commonplace is structured and installed: repository and package layout, control-plane organization, storage authority, subsystem boundaries, and proposed architectural changes"
type: types/tag-readme.md
---

# Commonplace architecture

How Commonplace itself is structured and installed. Assign this tag when an artifact substantively explains or proposes a Commonplace-specific arrangement: repository or package layout, installation, control-plane organization, storage authority, subsystem responsibilities, or interfaces. A worked Commonplace case can qualify within a broader argument. A general design principle does not qualify merely because Commonplace uses it or a footer links to its implementation.

This is a child of [architecture](./architecture-README.md); members keep both tags. The parent covers structural questions across agent-operated KBs and agent runtimes. This head also routes to current-state documentation and ADRs, which remain untagged under their collection rules. A tag on a proposal indicates its subject, not adoption.

## Current structure and decisions

- [Reference overview](../reference/README.md) — entry point for current-state documentation and architecture decisions
- [Commonplace architecture](../reference/architecture.md) — collections, packaged runtime, shipped skills, and operational surfaces
- [Projects read the library from the installed package](../reference/adr/086-projects-read-the-library-from-the-installed-package.md) — the user's KB stays in the project while the library is read from the installed package
- [Control-plane goals](../reference/control-plane-goals.md) — how AGENTS.md, the scaffold template, and installation supply KB goals
- [Instruction generation](../reference/instruction-generation.md) — the shipped build step and substitution points
- [Scenario architecture](../reference/scenario-architecture.md) — how the shipped architecture meets the requirements derived from user scenarios
- [Storage architecture](../reference/storage-architecture.md) — canonical files, derived indexes, and database-owned operational state
- [Review state in SQLite](../reference/adr/010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) — the authority decision that made review operational state database-owned

## Worked cases

- [Canonical files and database authority](../notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md) — Commonplace's review subsystem illustrates an explicit authority transfer for one state class
- [Edge ownership and storage choice](../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) — the freshness store supplies a bounded example of workload requirements and a separate database authority decision
- [Runtime structure and governance](../notes/runtime-structure-determines-governance-control-surfaces.md) — the Commonplace matrix identifies the governance surfaces it owns and the harness scheduler it does not
- [Always-loaded context mechanisms](../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) — configuration injection uses Commonplace's installation mechanism as a worked case

## Proposed changes

- [Checked inline blocks](../reference/proposals/checked-inline-blocks-for-shared-instruction-text.md) — proposed source/copy control for shared authoring instructions
- [Channel-compiled instruction artifacts](../reference/proposals/channel-compiled-instruction-artifacts.md) — proposed installation-time resolution of shell-specific instruction forms
