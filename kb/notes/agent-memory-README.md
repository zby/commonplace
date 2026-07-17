---
description: "Curated head for agent-memory notes — memory as crosscutting architecture, requirements, activation, lifecycle, and evaluation"
type: kb/types/tag-readme.md
index_source: tag
index_key: agent-memory
---

# Agent memory

Agent memory notes treat memory as part of agent architecture, not just storage. Use this curated head for claims about what memory must do for agents, how it interacts with context engineering, and where memory-system comparisons reveal broader KB design constraints. It is selective by design; use a scoped tag search for full membership.

## Core Frame

- [Designing a Memory System for LLM-Based Agents](./designing-agent-memory-systems.md) — starting point: derives the memory-system requirements from bounded context, consumer needs, artifact governance, and retrieval's limits
- [Agent memory needs discoverable, composable, trusted knowledge under bounded context](./agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) — minimal artifact-quality frame for remembered knowledge that must improve future action
- [Agent memory is a crosscutting concern, not a separable niche](./agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — decomposes memory into storage, retrieval/activation, and learning rather than treating it as one pluggable subsystem
- [Raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md) — separates preserving material from making it searchable, scoped, trustworthy, and lifecycle-managed
- [Memory design adds operational axes to artifact analysis](./memory-design-adds-operational-axes-to-artifact-analysis.md) — extends artifact analysis with capture, derivation, activation, authority assignment, lifecycle, and evaluation policies

## Requirements Map

- [Agent Memory Requirements](./agent-memory-requirements/README.md) — navigation hub for concrete requirements extracted from the memory-system design synthesis
- [Activate Behavior-Changing Memory Before The Mistake](./agent-memory-requirements/activate-behavior-changing-memory.md) — memory must reach the operative context before the relevant action, not only after explicit search
- [Make Authority Explicit](./agent-memory-requirements/make-authority-explicit.md) — governance rule for who can read, write, promote, activate, enforce, revise, and retire memory
- [Keep Lineage And Compiled Views From Drifting](./agent-memory-requirements/keep-compiled-views-aligned.md) — generated cues, prompt files, indexes, and assistant-specific views need provenance and staleness checks
- [Evaluate Memory By Effects, Not By Existence](./agent-memory-requirements/evaluate-memory-by-effects.md) — memory succeeds when downstream tasks, behavior, context efficiency, or lineage improve
- [Retire, Redact, Supersede, And Relax Memory](./agent-memory-requirements/retire-redact-supersede-relax.md) — lifecycle operations for changing, invalid, sensitive, or over-constrained memory

## Boundaries And Failure Modes

- [Active work state is not retrospective memory or chat history](./active-work-state-is-not-retrospective-memory-or-chat-history.md) — separates live task state from retained retrospective memory
- [Preserve Evidence Without Making History The Next Context](./agent-memory-requirements/preserve-evidence-without-loading-history.md) — keeps trace evidence available for audit and extraction without loading raw history by default
- [Flat memory predicts specific cross-contamination failures that are empirically testable](./flat-memory-predicts-specific-cross-contamination-failures-that-are.md) — predicts search pollution, identity scatter, and insight trapping when memory roles collapse
- [Trace-extracted memory earns authority per operation, not at capture](./trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) — trace-extracted records become knowledge only after operations such as verification, abstraction, and consultation
- [Bottom-up structure inference needs capture at the decision surface, not the state](./structure-inference-needs-capture-at-the-decision-surface.md) — relation inference works only when capture preserves the decision-shaped "why"

## External Checks

- [The adaptation survey corroborates memory requirements but misses artifact governance](./agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md) — compares external agentic-adaptation taxonomy against the memory requirements map
- [Memory management policy is learnable but oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — AgeMem shows memory policy can be learned when task-completion oracles exist
- [Three-space agent memory echoes Tulving's taxonomy but the analogy may be decorative](./three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md) — tests whether knowledge, self, and operational memory earn separate lifecycle treatment

## Related Tags

- [Learning theory](./learning-theory-README.md) — memory only matters when retained artifacts change future behavior
- [Context engineering](./context-engineering-README.md) — memory becomes useful only through selection and activation into bounded context
- [Computational model](./computational-model-README.md) — agent memory is loaded through bounded calls and scheduling decisions
- [Related systems](../agent-memory-systems/README.md) — external implementations and comparisons that expose memory-system design tradeoffs
