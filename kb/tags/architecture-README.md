---
description: "System structure in agent-operated KBs and agent runtimes: responsibility boundaries, state and storage, control planes, interfaces, and the consequences of their arrangement"
type: types/tag-readme.md
---

# Architecture

System structure in agent-operated KBs and agent runtimes: how responsibilities, state, authority, and interfaces are divided, and how those arrangements constrain behavior. Assign this tag when an artifact explains, compares, or proposes structural choices such as component boundaries, storage ownership, instruction layers, installation, or where control and enforcement reside. A list of components or an incidental reference to a system is insufficient without an explanation of their relationships or consequences.

[Commonplace architecture](./commonplace-architecture-README.md) is the child for Commonplace-specific arrangements, worked cases, and design proposals. Its members keep architecture as the parent tag. General architectural claims belong here even when they were developed through work on Commonplace.

[Computational-model](./computational-model-README.md) focuses on how LLM-based programs execute; architecture focuses on the arrangement and boundaries of the system that executes them. [Context-engineering](./context-engineering-README.md) focuses on what reaches a bounded call. A note that explains both a structural choice and an execution or loading mechanism may carry both tags.

## Runtime boundaries

- [A context-operation interface bounds the projections its policy can realize](../notes/context-operation-interface-bounds-context-policy.md) — operation vocabulary, controller placement, and exposure boundaries determine which context views can be constructed
- [Cross-task transition policy remains scheduling behind a tool interface](../notes/cross-task-transition-policy-remains-scheduling-behind-tools.md) — transition authority and intervention points determine the scheduler boundary
- [Stateful tools recover control by becoming hidden schedulers](../notes/stateful-tools-recover-control-by-becoming-hidden-schedulers.md) — orchestration state relocates control into a tool-owned runtime

- [Separate scheduling, context assembly, and external state](../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) — assigns distinct diagnostic responsibilities without requiring separate implementation modules
- [Runtime structure determines governance control surfaces](../notes/runtime-structure-determines-governance-control-surfaces.md) — exposed decisions and state determine where governance can inspect and intervene
- [Skill discovery re-fires in worker contexts](../notes/skill-discovery-re-fires-in-every-sub-agent-context.md) — harness-owned discovery crosses the context boundary a parent tried to establish

## Control planes and instruction placement

- [AGENTS.md as a control plane](../notes/agents-md-should-be-organized-as-a-control-plane.md) — layers invariants, routing, and escalation by function and scope
- [Instruction specificity and loading frequency](../notes/instruction-specificity-should-match-loading-frequency.md) — divides guidance between always-loaded and on-demand surfaces
- [KB goals in always-loaded context](../notes/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md) — places domain scope in the control plane while separating installation-specific inputs from framework defaults
- [Generate KB skills at build time](../notes/generate-instructions-at-build-time.md) — assigns installation-known binding to setup rather than model execution
- [Always-loaded context mechanisms](../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) — compares prompt files, capability descriptions, memory, and configuration as distinct surfaces
- [Scenario decomposition drives architecture](../notes/scenario-decomposition-drives-architecture.md) — derives placement and routing requirements from the context needed at each step of a user story

## Storage and authority

- [Canonical files and database authority](../notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md) — separates schema timing, storage substrate, and authority over accepted state
- [Edge ownership and storage choice](../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) — complete edge identity determines the key; workload requirements determine the storage comparison
