---
description: Index for context-engineering notes about selecting, scoping, and maintaining task-relevant knowledge under bounded context
type: kb/types/tag-readme.md
index_source: tag
index_key: context-engineering
---

# Context engineering

Context engineering is the machinery for getting the right knowledge into a bounded context at the right time. Use this index for notes about routing, loading, scoping, scheduling, and maintenance practices that make agent-operated KBs usable under context limits.

## Core Claims

- [Designing a Memory System for LLM-Based Agents](./designing-agent-memory-systems.md) - applies context-engineering pressure to memory-system design
- [Design for the first-time human, except on access cost](./design-for-the-first-time-human-except-on-access-cost.md) - explains why human-facing materializations and agent-facing query paths can share a source of truth while following different access modes
- [semantic sub-goals that exceed one context window become scheduling problems](./semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md) - explains when context limits force orchestration instead of a single larger prompt
- [stateful tools recover control by becoming hidden schedulers](./stateful-tools-recover-control-by-becoming-hidden-schedulers.md) - shows how runtime state can relocate context control behind the tool boundary
- [Addressability grain, not compression ratio, decides whether a summary layer helps](./addressability-grain-not-compression-ratio-decides-whether-a.md) - gives the condition under which materializing for a model reader pays: the materialized form must be selectable at a finer grain than the path it replaces
- [Human recompute is dear and rare; agent recompute is cheap and constant](./human-recompute-is-dear-and-rare-agent-recompute-is-cheap-and-constant.md) - why a stateless reader and a retaining one price the same cache differently, and why neither property settles the question alone
- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) - names when a recomputable value is safe to inline for context economy: only when a validator can re-derive and check it, otherwise it must stay a live read

## Adjacent Indexes

- [Computational model](./computational-model-README.md) - explains the bounded-call substrate context engineering operates on
- [Tool loop](./tool-loop-README.md) - covers framework-owned loops and when scheduling must become explicit
- [Learning theory](./learning-theory-README.md) - covers how context machinery contributes to deploy-time learning
