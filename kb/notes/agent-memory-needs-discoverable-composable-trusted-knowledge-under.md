---
description: "Distinguishes four use-time requirements for remembered knowledge—discoverability, loadability, composability, and calibrated trust—from system-level activation."
type: kb/types/note.md
traits: [title-as-claim]
tags: [agent-memory, context-engineering, learning-theory]
---

# Agent memory needs discoverable, loadable, composable, trusted knowledge under bounded context

Agent memory improves future work only when remembered knowledge can change what an agent does within bounded context—the limited working material available for a task. Merely storing or retrieving a durable fact, claim, preference, procedure, rationale, example, or learned constraint does not meet that standard. The knowledge must improve [contextual competence](./claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md): the agent's ability to answer, classify, plan, communicate, edit, and choose behavior appropriately.

Remembered knowledge can still fail after storage. It may remain undiscovered when relevant. It may be found but cost too much to bring into context at useful fidelity. It may enter context without enough structure to guide reasoning or action. Or it may provide no basis for deciding how strongly to rely on it. These failure modes yield four necessary use-time tests: remembered knowledge must be discoverable, loadable, composable, and trusted. The tests evaluate the path from retained material to use in a particular consumption setting, not the whole memory system.

## Four tests for remembered knowledge

**Discoverable** means a future consumer can identify remembered knowledge as relevant without exceeding the task's search budget. The failure is inert memory: the system contains a relevant lesson, preference, rule, or rationale, but no affordable route exposes it where it could change the outcome. Titles, descriptions, tags, indexes, retrieval keys, activation cues, source metadata, and placement in an always-loaded control plane can all provide discoverability. A small store that can be scanned whole is also discoverable. The requirement is not a particular retrieval method but a usable route from a future situation to the remembered material. Locating the material completes discovery; bringing enough of its payload into working context is the separate loadability test.

**Loadable** means a decision-relevant representation of identified knowledge can fit within the task's context budget without displacing more valuable material. The failure is stranded memory: the system can locate an artifact, but its useful content is too large or expensive to include, or compression removes what the current use depends on. The whole artifact need not fit. Concision, chunking, layered summaries, symbolic representations, and task-specific views can provide a smaller usable form, provided that form preserves the claim, conditions, or procedure needed for the task.

**Composable** means a loaded representation has enough structure to combine with task context and other memories in reasoning or action. Where direct reuse is the point, it can instead be applied as a coherent unit within a larger operation. The failure is isolated memory: a fragment is present, but the agent cannot determine its scope, relationships, priority, consequences, or conditions of application. Composable knowledge has enough shape to answer: "What does this apply to?", "What does it depend on?", and "What should change if I use it?" A stored preference, a source-derived claim, a reusable template, a test, a skill, and an architectural decision require different shapes, but each must be usable as part of a larger task rather than remain an isolated artifact.

**Trusted** means the consumer has enough evidence about remembered knowledge's role and status to calibrate reliance under the current evidence and stakes. The failure is memory as an undifferentiated assertion: the agent must ignore it, accept it blindly, or reconstruct its status before deciding how to use it. Trust is not the same as truth. It is calibrated reliance, supported by the rationale, source connection, status, validation, ownership, or review signal appropriate to the memory's role. A tentative hunch can be trusted as a hunch and tested before use; a validated rule can be trusted as a rule.

At use time, the four properties form a sequence. Discoverability identifies relevant knowledge. Loadability supplies a usable representation within the context budget. Composability lets that representation participate in the current task. Trust informs how much weight it should receive. If the system repairs a missing property at use time—for example, by summarizing an oversized artifact—the repaired representation must still pass the later tests.

## The four tests do not describe the whole memory system

Remembered material can satisfy all four tests and still go unused because a scheduler does not select it. Activation is that system-level event: the system follows a discovery route and allocates context budget to the resulting representation. Discoverability asks whether an affordable route exists. Loadability asks whether a usable representation can fit. Activation asks whether the system actually brings it in.

The tests describe remembered material relative to a consuming task and system, not as context-free attributes of stored bytes. The same artifact may be loadable under one context budget but not another, composable for one consumer but opaque to another, or trustworthy for a low-stakes task but insufficient for a high-stakes one. Capture, provenance, authority, lifecycle, governance, and evaluation can create, preserve, or test the four properties, but they are not reducible to them. The useful boundary is causal: ask whether a failure lies in the remembered representation and metadata, in the machinery that moves it into context, or in their interaction.

---

Relevant Notes:

- [Claw learning loops must improve action capacity not just retrieval](./claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) — grounds: contextual competence is the success criterion for learned material, not retrieval accuracy
- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: context scarcity makes loadability a separate requirement rather than part of discoverability
- [Raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md) — extends: explains how ingress work creates discoverability, composability, and trust instead of merely retaining material
- [Knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — grounds: stored memory has not helped unless it reaches the right context strongly enough to affect behavior
- [Agent memory is a crosscutting concern, not a separable niche](./agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — grounds: full memory systems include storage, retrieval/activation, and learning machinery beyond remembered material itself
- [Designing a Memory System for LLM-Based Agents](./designing-agent-memory-systems.md) — extends: derives full memory-system requirements from contextual competence, consumer failure modes, artifact governance, and retrieval's limits
