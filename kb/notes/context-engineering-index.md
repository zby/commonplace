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

- [Activate Behavior-Changing Memory Before The Mistake](./agent-memory-requirements/activate-behavior-changing-memory.md) - Behavior-changing memory must activate before relevant actions rather than waiting for explicit retrospective search
- [Agent memory needs discoverable, composable, trusted knowledge under bounded context](./agent-memory-needs-discoverable-composable-trusted-knowledge-under-bounded-context.md) - Frames discoverable, composable, trusted remembered knowledge as the minimal artifact-quality basis for agent memory under bounded context.
- [Agent Memory Requirements](./agent-memory-requirements/README.md) - Navigation hub for concrete agent-memory requirements extracted from the memory-system design synthesis
- [Brainstorming: how to test whether pairwise comparison can harden soft oracles](./brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles.md) - Staged test plan for whether pairwise comparison improves soft-oracle properties (discrimination, stability, calibration) in LLM evaluation loops
- [Codified scheduling patterns can turn tools into hidden schedulers](./codified-scheduling-patterns-can-turn-tools-into-hidden-schedulers.md) - As agent behavior matures, deterministic next-step policies need explicit control logic; if the framework offers only tools, scheduling patterns end up there and the tools become hidden schedulers
- [Create Memory Directly](./agent-memory-requirements/create-memory-directly.md) - Direct memory creation preserves live understanding by writing useful artifacts before later trace extraction loses structure
- [Evaluate Memory By Effects, Not By Existence](./agent-memory-requirements/evaluate-memory-by-effects.md) - Memory should be evaluated by downstream effects on tasks, artifacts, answers, behavior, context efficiency, and source alignment
- [Evolving understanding needs re-distillation, not composition](./evolving-understanding-needs-re-distillation-not-composition.md) - When understanding evolves, reconciling fragments into a coherent picture can exceed effective context; a pre-distilled narrative keeps the whole picture within feasible bounds
- [Import External Knowledge Into Internal Form](./agent-memory-requirements/import-external-knowledge.md) - Agent memory systems need import paths when authoritative project knowledge already exists outside the memory substrate
- [Keep Memory Roles And Compiled Views From Drifting](./agent-memory-requirements/keep-compiled-views-aligned.md) - Generated cues, prompt files, indexes, and assistant-specific views need source-of-truth rules so they do not drift into authority
- [Make Authority Explicit](./agent-memory-requirements/make-authority-explicit.md) - Memory architecture must state who can read, write, promote, activate, enforce, revise, and retire memory across risk levels
- [Memory design adds operational axes to artifact analysis](./memory-design-adds-operational-axes-to-artifact-analysis.md) - Seedling bridge note that names the memory-specific operational axes around artifact class, backend, and role: capture, derivation, activation, authority, lifecycle, and evaluation
- [Preserve Evidence Without Making History The Next Context](./agent-memory-requirements/preserve-evidence-without-loading-history.md) - Trace retention should preserve evidence for audit and extraction without making raw history the agent's default context
- [Promote Only When Future Value Exceeds Maintenance Cost](./agent-memory-requirements/promote-only-when-value-exceeds-cost.md) - Candidate memory should become durable only when future retrieval or activation value exceeds review and maintenance cost
- [Raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md) - Accumulation preserves material, but usable agent memory requires ingress work that adds handles, scope, relationships, provenance, trust signals, and lifecycle pressure.
- [Retire, Redact, Supersede, And Relax Memory](./agent-memory-requirements/retire-redact-supersede-relax.md) - Memory systems need lifecycle operations for redaction, decay, supersession, retirement, relaxation, and temporal validity
- [Selector-loaded review gates could let review-revise learn from accepted edits](./selector-loaded-review-gates-could-let-review-revise-learn-from-accepted-edits.md) - Brainstorm on learning reusable review gates from accepted note edits: mine candidate gates from before/after diffs, store them atomically, and load a bounded subset into future reviews
- [Serve Multiple Consumers, Not One Retrieval Interface](./agent-memory-requirements/serve-multiple-consumers.md) - Memory systems need multiple surfaces because acting, scheduling, review, learning, governance, and active work consume memory differently
- [Subtasks that need different tools force loop exposure in agent frameworks](./subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md) - When decomposition creates child tasks with different tool surfaces, the parent must construct fresh calls for each child, so a framework-owned loop is no longer the right control surface
- [The adaptation survey corroborates memory requirements but misses artifact-role governance](./agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md) - The agentic-adaptation survey supports the memory requirements map by treating memory and skills as adaptive tools, but it needs artifact-role governance to become design guidance
- [Use Trace-Derived Extraction As Meta-Learning](./agent-memory-requirements/use-trace-derived-extraction.md) - Trace-derived extraction is an after-the-fact learning path that must respect signal quality, review, and artifact versus weight-learning boundaries
