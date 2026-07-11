---
description: "Navigation hub for concrete agent-memory requirements extracted from the memory-system design synthesis"
type: kb/types/note.md
traits: [synthesis]
tags: [agent-memory, context-engineering]
---

# Agent Memory Requirements

This directory expands the requirements inventory derived in [Designing a Memory System for LLM-Based Agents](../designing-agent-memory-systems.md). Each note describes one requirement in a form an agent can load independently while designing, reviewing, or comparing memory systems.

The requirements are organized by operation, not by implementation layer. A system may satisfy them through files, databases, runtime services, prompts, skills, review workflows, or learned policies. The point is to make the needed capability and failure mode explicit.

## Requirements

1. [Create memory directly](./create-memory-directly.md) - write useful memory artifacts while understanding, provenance, and caveats are still live.
2. [Import external knowledge into internal form](./import-external-knowledge.md) - transform existing project knowledge into typed, linked, trusted system artifacts.
3. [Preserve evidence without loading history](./preserve-evidence-without-loading-history.md) - keep traces for extraction and audit without making history the default context.
4. [Use trace-derived extraction as meta-learning](./use-trace-derived-extraction.md) - mine traces after the fact while respecting signal quality and review.
5. [Serve multiple consumers](./serve-multiple-consumers.md) - expose different surfaces for acting, scheduling, review, learning, governance, and active work.
6. [Activate behavior-changing memory](./activate-behavior-changing-memory.md) - fire relevant lessons before repeated mistakes or high-risk actions.
7. [Promote only when value exceeds cost](./promote-only-when-value-exceeds-cost.md) - move candidates into durable artifacts only when future value justifies maintenance.
8. [Keep compiled views aligned](./keep-compiled-views-aligned.md) - prevent cues, prompt files, indexes, and generated surfaces from drifting into independent authority.
9. [Retire, redact, supersede, and relax memory](./retire-redact-supersede-relax.md) - manage forgetting, revision, sensitivity, staleness, and temporal validity.
10. [Make authority explicit](./make-authority-explicit.md) - define who can read, write, promote, activate, enforce, revise, and retire memory.
11. [Evaluate memory by effects](./evaluate-memory-by-effects.md) - test whether memory changes future tasks, artifacts, answers, and behavior.

## Use

Use the synthesis note when you need the derivation. Use these notes when you need to inspect, implement, or score one capability.
