---
description: "Distinguishes three necessary tests for remembered knowledge—discoverability, composability, and calibrated trust—from broader concerns such as activation and loadability."
type: kb/types/note.md
traits: [title-as-claim]
tags: [agent-memory, context-engineering, learning-theory]
---

# Agent memory needs discoverable, composable, trusted knowledge under bounded context

Agent memory improves future work only when remembered knowledge can change what an agent does within bounded context—the limited working material available for a task. Merely storing or retrieving a durable fact, claim, preference, procedure, rationale, example, or learned constraint does not meet that standard. The knowledge must improve [contextual competence](./claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md): the agent's ability to answer, classify, plan, communicate, edit, and choose behavior appropriately.

Remembered knowledge can still fail after storage. It may remain undiscovered when relevant. It may enter context without enough structure to guide reasoning or action. Or it may provide no basis for deciding how strongly to rely on it. These failure modes yield three necessary artifact-quality tests: remembered knowledge must be discoverable, composable, and trusted. The tests are not a complete account of memory quality or system requirements; they evaluate remembered material, not the whole memory system.

## Three tests for remembered knowledge

**Discoverable** means remembered knowledge has a usable route from a future situation into working context. An agent or context engine—the component that selects remembered material for working context—can locate it when relevant without scanning the entire store. The failure is inert memory: the system contains a relevant lesson, preference, rule, or rationale, but the knowledge never becomes available where it could change the outcome. Titles, descriptions, tags, indexes, retrieval keys, activation cues, source metadata, and placement in an always-loaded control plane can all provide discoverability. The requirement is not a particular retrieval method but a usable handle connecting future situations to the remembered material.

**Composable** means remembered knowledge has enough structure to combine with task context and other memories in reasoning or action. Where direct reuse is the point, it can instead be applied as a coherent unit within a larger operation. The failure is isolated memory: a fragment is retrievable, but the agent cannot determine its scope, relationships, priority, consequences, or conditions of application. Composable knowledge has enough shape to answer: "What does this apply to?", "What does it depend on?", and "What should change if I use it?" A stored preference, a source-derived claim, a reusable template, a test, a skill, and an architectural decision require different shapes, but each must be usable as part of a larger task rather than remain an isolated artifact.

**Trusted** means remembered knowledge carries enough evidence about its role and status for the agent to rely on it at the right level of confidence without redoing the original work every time. The failure is memory as noise: the agent must ignore or reverify the knowledge, or risk relying on it too strongly. Trust is not the same as truth. It is calibrated reliance, supported by the rationale, source connection, status, validation, ownership, or review signal appropriate to the memory's role. A tentative observation can be trusted as tentative; a validated rule can be trusted as a rule.

At use time, the three properties form a sequence. Discoverability makes relevant knowledge reachable. Composability lets it participate in the current task. Trust determines how much weight it should receive. A failure at any point breaks the path from storage to contextual competence. The properties also interact: missing scope can make knowledge both hard to compose and hard to trust, while discoverability allows knowledge to be found for correction, review, and retirement as well as use.

## The triad is necessary, not exhaustive

Discoverability, composability, and trust form a failure-oriented diagnostic, not a complete decomposition of memory quality. Remembered material can satisfy all three and still be too large or expensive to place in bounded context. When that cost follows from the material's size or representation, loadability is a separate artifact-level property. When the material provides usable retrieval handles but a scheduler fails to select it, activation is a system-level failure. Discoverability concerns whether remembered knowledge provides a usable route into context; activation concerns whether the system follows that route.

Capture, provenance, authority, lifecycle, governance, and evaluation can create, preserve, or test these properties, but they are not reducible to the triad. The useful boundary is causal: ask whether a failure lies in the remembered material, in the machinery that moves it into context, or in their interaction. The triad identifies three necessary artifact-quality tests within that broader analysis.

---

Relevant Notes:

- [Claw learning loops must improve action capacity not just retrieval](./claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) — grounds: contextual competence is the success criterion for learned material, not retrieval accuracy
- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: bounded context and context-scarcity costs are the constraint that makes memory artifact quality matter operationally
- [Raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md) — extends: explains how ingress work turns accumulated material into discoverable, composable, trusted memory
- [Knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — grounds: stored memory has not helped unless it reaches the right context strongly enough to affect behavior
- [Agent memory is a crosscutting concern, not a separable niche](./agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — grounds: full memory systems include storage, retrieval/activation, and learning machinery beyond remembered material itself
- [Designing a Memory System for LLM-Based Agents](./designing-agent-memory-systems.md) — extends: derives full memory-system requirements from contextual competence, consumer failure modes, artifact governance, and retrieval's limits
