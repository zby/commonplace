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
- [semantic sub-goals that exceed one context window become scheduling problems](./semantic-sub-goals-that-exceed-one-context-window-become-scheduling-problems.md) - explains when context limits force orchestration instead of a single larger prompt
- [stateful tools recover control by becoming hidden schedulers](./stateful-tools-recover-control-by-becoming-hidden-schedulers.md) - shows how runtime state can relocate context control behind the tool boundary

## Adjacent Indexes

- [Computational model](./computational-model-index.md) - explains the bounded-call substrate context engineering operates on
- [Tool loop](./tool-loop-index.md) - covers framework-owned loops and when scheduling must become explicit
- [Learning theory](./learning-theory-index.md) - covers how context machinery contributes to deploy-time learning

## Other tagged notes <!-- generated -->

- [Brainstorming: how to test whether pairwise comparison can harden soft oracles](./brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles.md) - Staged test plan for whether pairwise comparison improves soft-oracle properties (discrimination, stability, calibration) in LLM evaluation loops
- [Codified scheduling patterns can turn tools into hidden schedulers](./codified-scheduling-patterns-can-turn-tools-into-hidden-schedulers.md) - As agent behavior matures, deterministic next-step policies need explicit control logic; if the framework offers only tools, scheduling patterns end up there and the tools become hidden schedulers
- [Evolving understanding needs re-distillation, not composition](./evolving-understanding-needs-re-distillation-not-composition.md) - When understanding evolves, reconciling fragments into a coherent picture can exceed effective context; a pre-distilled narrative keeps the whole picture within feasible bounds
- [Selector-loaded review gates could let review-revise learn from accepted edits](./selector-loaded-review-gates-could-let-review-revise-learn-from-accepted-edits.md) - Brainstorm on learning reusable review gates from accepted note edits: mine candidate gates from before/after diffs, store them atomically, and load a bounded subset into future reviews
- [Subtasks that need different tools force loop exposure in agent frameworks](./subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md) - When decomposition creates child tasks with different tool surfaces, the parent must construct fresh calls for each child, so a framework-owned loop is no longer the right control surface
