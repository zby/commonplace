---
description: Index for agent-memory notes about memory as a crosscutting concern in agent architecture
type: kb/types/index.md
index_source: tag
index_key: agent-memory
status: current
---

# Agent memory

Agent memory notes treat memory as part of agent architecture, not just storage. Use this index for claims about what memory must do for agents, how it interacts with context engineering, and where memory-system comparisons reveal broader KB design constraints.

## Notes

- [Designing a Memory System for LLM-Based Agents](./designing-agent-memory-systems.md) - starting point: frames the design pressures around agent memory as context engineering, retrieval, and learning problems rather than a single database choice

## Related Tags

- [Learning theory](./learning-theory-index.md) - memory only matters when retained artifacts change future behavior
- [Computational model](./computational-model-index.md) - agent memory is loaded through bounded calls and scheduling decisions
- [Related systems](../agent-memory-systems/README.md) - external implementations and comparisons that expose memory-system design tradeoffs

## Other tagged notes <!-- generated -->

- [Activate Behavior-Changing Memory Before The Mistake](./agent-memory-requirements/activate-behavior-changing-memory.md) - Behavior-changing memory must activate before relevant actions rather than waiting for explicit retrospective search
- [Agent memory needs discoverable, composable, trusted knowledge under bounded context](./agent-memory-needs-discoverable-composable-trusted-knowledge-under-bounded-context.md) - Frames discoverable, composable, trusted remembered knowledge as the minimal artifact-quality basis for agent memory under bounded context.
- [Agent Memory Requirements](./agent-memory-requirements/README.md) - Navigation hub for concrete agent-memory requirements extracted from the memory-system design synthesis
- [Create Memory Directly](./agent-memory-requirements/create-memory-directly.md) - Direct memory creation preserves live understanding by writing useful artifacts before later trace extraction loses structure
- [Evaluate Memory By Effects, Not By Existence](./agent-memory-requirements/evaluate-memory-by-effects.md) - Memory should be evaluated by downstream effects on tasks, artifacts, answers, behavior, context efficiency, and source alignment
- [Import External Knowledge Into Internal Form](./agent-memory-requirements/import-external-knowledge.md) - Agent memory systems need import paths when authoritative project knowledge already exists outside the memory substrate
- [Keep Memory Roles And Compiled Views From Drifting](./agent-memory-requirements/keep-compiled-views-aligned.md) - Generated cues, prompt files, indexes, and assistant-specific views need source-of-truth rules so they do not drift into authority
- [Make Authority Explicit](./agent-memory-requirements/make-authority-explicit.md) - Memory architecture must state who can read, write, promote, activate, enforce, revise, and retire memory across risk levels
- [Preserve Evidence Without Making History The Next Context](./agent-memory-requirements/preserve-evidence-without-loading-history.md) - Trace retention should preserve evidence for audit and extraction without making raw history the agent's default context
- [Promote Only When Future Value Exceeds Maintenance Cost](./agent-memory-requirements/promote-only-when-value-exceeds-cost.md) - Candidate memory should become durable only when future retrieval or activation value exceeds review and maintenance cost
- [Raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md) - Accumulation preserves material, but usable agent memory requires ingress work that adds handles, scope, relationships, provenance, trust signals, and lifecycle pressure.
- [Retire, Redact, Supersede, And Relax Memory](./agent-memory-requirements/retire-redact-supersede-relax.md) - Memory systems need lifecycle operations for redaction, decay, supersession, retirement, relaxation, and temporal validity
- [Serve Multiple Consumers, Not One Retrieval Interface](./agent-memory-requirements/serve-multiple-consumers.md) - Memory systems need multiple surfaces because acting, scheduling, review, learning, governance, and active work consume memory differently
- [The adaptation survey corroborates memory requirements but misses artifact-role governance](./agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md) - The agentic-adaptation survey supports the memory requirements map by treating memory and skills as adaptive tools, but it needs artifact-role governance to become design guidance
- [Use Trace-Derived Extraction As Meta-Learning](./agent-memory-requirements/use-trace-derived-extraction.md) - Trace-derived extraction is an after-the-fact learning path that must respect signal quality, review, and artifact versus weight-learning boundaries
