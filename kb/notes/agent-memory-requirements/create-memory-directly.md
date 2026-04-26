---
description: "Direct memory creation preserves live understanding by writing useful artifacts before later trace extraction loses structure"
type: kb/types/note.md
tags: [agent-memory, context-engineering]
status: current
---

# Create Memory Directly

Direct memory creation is the context-efficient path when understanding is already available during work. When current work reveals a stable claim, procedure, policy, index entry, validation rule, or tool extension, the natural operation is to write the useful artifact while the relevant context, provenance, and caveats are still live. Forcing the lesson through later trace extraction spends future context on rediscovery and risks losing structure the agent already had.

Direct creation is not blank-page writing. The memory system should help the agent choose the right artifact shape and satisfy that artifact's quality contract at write time. Memory destinations should expose their creation contract, not just accept content after the fact.

## Methods

- Notes and decision records for claims, rationales, alternatives, and negative results.
- Instructions, skills, checklists, and runbooks for repeated work patterns.
- Indexes and link maintenance for navigation and context discovery.
- Tests, validators, scripts, plugins, and runtime extensions for deterministic learned behavior.
- Governed learned artifacts embedded in work surfaces when that surface is the authoritative destination.
- Routing cues, type-specific templates, quality requirements, validators, preview checks, and conversion helpers loaded before writing.

## Failure Modes

Direct memory fails when it becomes generic capture rather than a role-specific artifact. A note can be accurate but hard to find. An instruction can steer behavior incorrectly. A check can fossilize a temporary workaround. A generated work-surface update can blur the boundary between ordinary operational state and learned memory. Direct memory is good only when it becomes useful future context or useful future behavior.

## Evaluation Questions

- Did the system preserve context, provenance, caveats, and intended use while understanding was live?
- Did it route the material into the right artifact class and role?
- Did validation or review catch malformed or low-quality memory before promotion?
- Can a future agent find and apply the artifact without replaying the original session?

---

Relevant Notes:

- [Designing a Memory System for LLM-Based Agents](../designing-agent-memory-systems.md) - derives this requirement from contextual competence and artifact roles
- [Axes of artifact analysis](../axes-of-artifact-analysis.md) - grounds the artifact class and role distinction
