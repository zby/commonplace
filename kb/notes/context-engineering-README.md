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
- [Addressability grain, not compression ratio, sets a matched selective-read floor](./addressability-grain-sets-a-matched-selective-read-floor.md) - isolates the retrieval-floor condition for a known question that maps to one discriminating unit on each path, while leaving fan-out, sufficiency, reliability, and net value separate
- [Opposed recompute factors do not decide documentation segmentation](./opposed-recompute-factors-do-not-decide-documentation-segmentation.md) - why crossed savings and recurrence rankings do not order cache value, and why cache value alone does not decide whether a second content layer pays
- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) - names when a recomputable value is safe to inline for context economy: only when a validator can re-derive and check it, otherwise it must stay a live read

## Adjacent Indexes

- [Computational model](./computational-model-README.md) - explains the bounded-call substrate context engineering operates on
- [Tool loop](./tool-loop-README.md) - covers framework-owned loops and when scheduling must become explicit
- [Learning theory](./learning-theory-README.md) - covers how context machinery contributes to deploy-time learning
