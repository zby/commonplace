---
description: "Frames discoverable, composable, trusted remembered knowledge as the minimal artifact-quality basis for agent memory under bounded context."
type: kb/types/note.md
traits: [title-as-claim]
tags: [agent-memory, context-engineering, learning-theory]
status: seedling
---

# Agent memory needs discoverable, composable, trusted knowledge under bounded context

Agent memory is not valuable because something was stored after a session. A durable fact, claim, preference, procedure, rationale, example, or learned constraint counts as useful memory only when it can change future agent work. The success criterion is [contextual competence](./claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md): the agent's ability to answer, classify, plan, communicate, edit, and choose behavior appropriately under bounded context.

That makes memory broader than retrieval but narrower than "anything persistent." A memory can be retrieved and still fail if it cannot be used. It can be stored and still fail if the agent never encounters it. It can be true and still fail if the agent cannot tell when to rely on it. Remembered knowledge earns its place by improving future action capacity, not by existing in a store or matching a query.

This note is about remembered knowledge, not the whole memory system. Capture, activation, provenance, authority, lifecycle, evaluation, and governance are necessary machinery around memory. The first-order quality test for the remembered material itself is simpler: it must at least be discoverable, composable, and trusted. These are a minimal basis for artifact quality, not an exhaustive ontology of every property a memory system must maintain.

## Three properties of useful agent memory

**Discoverable** means the agent or context engine can find the remembered material when it matters without scanning everything. The failure mode is inert memory: the system has a relevant lesson, preference, rule, or rationale, but it never enters the working context where it could change the outcome. Discoverability can come from titles, descriptions, tags, indexes, retrieval keys, activation cues, source metadata, or placement in an always-loaded control plane. The common requirement is not a particular retrieval method but a usable handle from future situations to the remembered material.

**Composable** means the remembered material can combine with task context and other memories to support new reasoning or action, or can be applied as a coherent unit where direct reuse is the point. The failure mode is isolated memory: a fragment is retrievable, but the agent cannot tell its scope, relation, priority, consequence, or application conditions, so it cannot use the fragment as a premise or apply it as a unit. Composable memory has enough shape to answer "what does this apply to?", "what does it depend on?", and "what should change if I believe or use it?" A stored preference, a source-derived claim, a reusable template, a test, a skill, and an architectural decision all need different shapes, but each must be usable with other remembered material rather than trapped as a disconnected fact.

**Trusted** means the agent can rely on the remembered material at the right level of confidence without redoing the original work every time. The failure mode is memory as noise: the agent either ignores the memory because its authority is unclear, or over-applies it because its provenance, currency, and scope are missing. Trust is not the same as truth. It is calibrated reliance: enough rationale, source connection, status, validation, ownership, or review signal for the memory's role. A tentative observation can be trusted as tentative; a validated rule can be trusted as a rule.

These properties are interdependent. Composability depends on discoverability because unavailable memory cannot participate in reasoning. Composability also depends on trust because unreliable premises poison downstream conclusions. Trust depends on discoverability because memory that cannot be found cannot be challenged, corrected, reviewed, or retired. Discoverability is therefore the entry condition, but it is not sufficient: memory that is findable but unusable or untrusted still does not improve contextual competence.

## Other memory requirements operate around this basis

Discoverability, composability, and trust do not exhaust the requirements for a working memory system. They name the minimum artifact-quality basis: if remembered material lacks one of them, it cannot reliably improve future action. Other requirements become peer properties only if remembered material can satisfy the triad yet still fail *as remembered material*. Otherwise, they operate around the basis by preserving it, operationalizing it, or deciding when it should matter.

Context economy is one example. Useful memory must be economical enough to load or compile into the future situation where it matters. A memory can be nominally discoverable but too noisy to select, nominally composable but too bulky to combine, or nominally trusted but too expensive to verify or carry. Activation, lifecycle, governance, evaluation, provenance, authority, and capture play similar surrounding roles: they are not additional peer properties of the remembered material, but system-level mechanisms that keep the artifact-quality basis useful under bounded context.

---

Relevant Notes:

- [Claw learning loops must improve action capacity not just retrieval](./claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) — grounds: contextual competence is the success criterion for learned material, not retrieval accuracy
- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — grounds: bounded context and context-scarcity costs are the constraint that makes memory artifact quality matter operationally
- [Raw accumulation does not create usable memory](./raw-accumulation-does-not-create-usable-memory.md) — extends: explains how ingress work turns accumulated material into discoverable, composable, trusted memory
- [Knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md) — grounds: stored memory has not helped unless it reaches the right context strongly enough to affect behavior
- [Agent memory is a crosscutting concern, not a separable niche](./agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — grounds: full memory systems include storage, retrieval/activation, and learning machinery beyond remembered material itself
- [Designing a Memory System for LLM-Based Agents](./designing-agent-memory-systems.md) — extends: derives full memory-system requirements from contextual competence, consumer failure modes, artifact governance, and retrieval's limits
