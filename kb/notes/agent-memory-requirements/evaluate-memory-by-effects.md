---
description: "Memory should be evaluated by downstream effects on tasks, artifacts, answers, behavior, context efficiency, and lineage alignment"
type: kb/types/note.md
traits: [has-external-sources]
tags: [agent-memory, context-engineering, learning-theory]
---

# Evaluate Memory By Effects, Not By Existence

The system should not count "memory written" as learning. It should evaluate whether memory improved the future task, answer, artifact, or behavior. This requirement intentionally recaps the others as effects: each requirement should leave an observable evaluation surface rather than merely adding another stored object.

## Evaluation Dimensions

- Direct retrieval: can the system answer the question that motivated storage?
- Navigability: can an agent or human follow links and provenance to understand why an answer is trustworthy?
- Contract fitness: does the artifact satisfy the quality goal for its intended form and authority path?
- Activation: does relevant policy fire before the action where it matters?
- Behavioral uptake: does the fired memory change the downstream plan, tool use, or artifact in the intended direction?
- Context efficiency: does the memory earn the tokens, latency, and attention it consumes?
- Lineage alignment: do generated indexes, reminders, rules, and assistant-specific views match their authoritative sources and derivation rules?
- Evidence sufficiency: does retrieval expose when coverage, confidence, diversity, or agreement is too weak to support the requested answer or action?
- Temporal correctness: can the system distinguish what is current from what was true at a previous time when that distinction matters?
- Work-surface fit: does the memory live where the acting agent or human will naturally encounter and maintain it?
- Lifecycle health: are stale, duplicate, low-value, sensitive, or superseded memories retired or demoted?
- Promotion economics: do durable artifacts get reused enough to justify their maintenance burden?

These dimensions are separable. QA-style retrieval tests can pass while activation fails. A cue can fire while behavior remains unchanged. A note can be accurate but too hard to find. A policy can become harmful after the domain changes.

## Methods

- Held-out retrieval tests for known questions.
- WITH/WITHOUT activation comparisons for behavior-changing cues.
- Lineage-alignment checks for compiled views.
- Link and provenance audits for navigability.
- Lifecycle reviews for stale, duplicate, sensitive, or superseded memory.
- Evidence-sufficiency gates that warn when retrieval is too thin to support action.
- Temporal tests when the domain requires point-in-time recall.

## Evaluation Questions

- What future capacity was supposed to change?
- Can that change be observed in answers, actions, artifacts, or behavior?
- Did the memory earn the context budget it consumed?
- Can the system detect when memory exists but is unused, stale, misleading, or too weakly supported?

---

Relevant Notes:

- [Large Language Model Agents are not Always Faithful Self-Evolvers](../../sources/llm-agents-are-not-always-faithful-self-evolvers.md) - evidence: shows why written memory must be evaluated for behavioral influence rather than assumed effective
- [Designing a Memory System for LLM-Based Agents](../designing-agent-memory-systems.md) - derives evaluation as the closure condition for all memory requirements
