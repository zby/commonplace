---
description: "Curated head for the agent-memory tag — how agents retain, recall, and govern knowledge across sessions: memory-system requirements, activation, trace extraction, lifecycle, and comparisons of external memory systems"
type: types/tag-readme.md
---

# Agent memory

This tag gathers what agents retain across sessions and how that retention becomes useful: persistence and storage, recall and activation, extracting memory from traces, authority over what is kept, lifecycle operations such as retiring and superseding, and comparisons of external agent memory systems. The anchor is [Designing a Memory System for LLM-Based Agents](../notes/designing-agent-memory-systems.md), the synthesis from which the memory-system requirements are derived. Members span `kb/notes/`, the external memory-system comparisons in `kb/agent-memory-systems/`, and system analyses in `kb/agentic-systems/`. Nearby but different: [context-engineering](./context-engineering-README.md) covers getting knowledge into any bounded call; a note belongs here when its question is what is retained between sessions and under what authority, not only how a call is assembled. This head is selective; use a scoped tag search for full membership.

## Core Frame

- [Designing a Memory System for LLM-Based Agents](../notes/designing-agent-memory-systems.md) — the anchor synthesis: derives the memory-system requirements from bounded context, consumer needs, artifact governance, and retrieval's limits
- [Agent memory needs discoverable, composable, trusted knowledge under bounded context](../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) — minimal artifact-quality frame for remembered knowledge that must improve future action
- [Agent memory is a crosscutting concern, not a separable niche](../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — decomposes memory into storage, retrieval/activation, and learning rather than treating it as one pluggable subsystem
- [Raw accumulation does not create usable memory](../notes/raw-accumulation-does-not-create-usable-memory.md) — separates preserving material from making it searchable, scoped, trustworthy, and lifecycle-managed
- [Memory design adds operational axes to artifact analysis](../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) — extends artifact analysis with capture, derivation, activation, authority assignment, lifecycle, and evaluation policies

## Requirements Map

- [Agent Memory Requirements](../notes/agent-memory-requirements/README.md) — navigation hub for concrete requirements extracted from the memory-system design synthesis
- [Activate Behavior-Changing Memory Before The Mistake](../notes/agent-memory-requirements/activate-behavior-changing-memory.md) — memory must reach the operative context before the relevant action, not only after explicit search
- [Make Authority Explicit](../notes/agent-memory-requirements/make-authority-explicit.md) — governance rule for who can read, write, promote, activate, enforce, revise, and retire memory
- [Keep Lineage And Compiled Views From Drifting](../notes/agent-memory-requirements/keep-compiled-views-aligned.md) — generated cues, prompt files, indexes, and assistant-specific views need provenance and staleness checks
- [Evaluate Memory By Effects, Not By Existence](../notes/agent-memory-requirements/evaluate-memory-by-effects.md) — memory succeeds when downstream tasks, behavior, context efficiency, or lineage improve
- [Retire, Redact, Supersede, And Relax Memory](../notes/agent-memory-requirements/retire-redact-supersede-relax.md) — lifecycle operations for changing, invalid, sensitive, or over-constrained memory

## Boundaries And Failure Modes

- [Active work state is not retrospective memory or chat history](../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) — separates live task state from retained retrospective memory
- [A context-operation interface bounds the projections its policy can realize](../notes/context-operation-interface-bounds-context-policy.md) — separates retained substrate, available projection operations, controller policy, and active-context exposure
- [Preserve Evidence Without Making History The Next Context](../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) — keeps trace evidence available for audit and extraction without loading raw history by default
- [Flat memory predicts specific cross-contamination failures that are empirically testable](../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are.md) — predicts search pollution, identity scatter, and insight trapping when memory roles collapse
- [Trace-extracted memory earns authority per operation, not at capture](../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) — trace-extracted records become knowledge only after operations such as verification, abstraction, and consultation
- [Bottom-up structure inference needs capture at the decision surface, not the state](../notes/structure-inference-needs-capture-at-the-decision-surface.md) — relation inference works only when capture preserves the decision-shaped "why"

## External Checks

- [The adaptation survey corroborates memory requirements but misses artifact governance](../notes/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md) — compares external agentic-adaptation taxonomy against the memory requirements map
- [Memory management policy is learnable but oracle-dependent](../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — AgeMem shows memory policy can be learned when task-completion oracles exist
- [Three-space agent memory echoes Tulving's taxonomy but the analogy may be decorative](../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md) — tests whether knowledge, self, and operational memory earn separate lifecycle treatment

## Memory-System Comparisons

- [Agentic memory systems: comparative review](../agent-memory-systems/agentic-memory-systems-comparative-review.md) — cross-system findings from the code-grounded reviews: storage choices, read-back, trace learning, and how rarely lifecycle curation appears
- [Systems table](../agent-memory-systems/systems-table.md) — one row per reviewed memory system across storage, read-back, targeting, trace learning, and enforcement
- [Review framework design](../agent-memory-systems/review-framework-design.md) — why the comparison matrix has the columns it has
- The full catalogue of reviewed systems is the [agent-memory-systems index](../agent-memory-systems/README.md)

## Related Tags

- [Learning theory](./learning-theory-README.md) — memory only matters when retained artifacts change future behavior
- [Context engineering](./context-engineering-README.md) — the wider area: retained memory becomes useful only through selection and activation into bounded context; most requirements notes carry both tags
- [Computational model](./computational-model-README.md) — agent memory is loaded through bounded calls and scheduling decisions
