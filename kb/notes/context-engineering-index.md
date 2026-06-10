---
description: Index for context-engineering notes about selecting, scoping, and maintaining task-relevant knowledge under bounded context
type: kb/types/index.md
index_source: tag
index_key: context-engineering
status: current
---

# Context engineering

Context engineering is the machinery for getting the right knowledge into a bounded context at the right time. Use this index for notes about routing, loading, scoping, scheduling, and maintenance practices that make agent-operated KBs usable under context limits.

## Core Claims

- [Designing a Memory System for LLM-Based Agents](./designing-agent-memory-systems.md) - applies context-engineering pressure to memory-system design
- [semantic sub-goals that exceed one context window become scheduling problems](./semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md) - explains when context limits force orchestration instead of a single larger prompt
- [stateful tools recover control by becoming hidden schedulers](./stateful-tools-recover-control-by-becoming-hidden-schedulers.md) - shows how runtime state can relocate context control behind the tool boundary

## Adjacent Indexes

- [Computational model](./computational-model-index.md) - explains the bounded-call substrate context engineering operates on
- [Tool loop](./tool-loop-index.md) - covers framework-owned loops and when scheduling must become explicit
- [Learning theory](./learning-theory-index.md) - covers how context machinery contributes to deploy-time learning
