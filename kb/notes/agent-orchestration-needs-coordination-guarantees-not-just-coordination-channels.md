---
description: Coordination channels say how bounded contexts interact, but the missing discriminator is which guarantee prevents contamination, inconsistency, or amplification on the shared substrate
type: note
tags: [computational-model]
status: seedling
---

# Agent orchestration needs coordination guarantees, not just coordination channels

Architectures are often compared by coordination channel: conversation, prompt refinement, forking, shared memory, synthesis. Two systems can use the same channel and have very different reliability properties, because the harder question is not *how* bounded contexts interact but *what guarantee* governs that interaction. When multiple computations contribute to a shared semantic substrate, what prevents one contribution from corrupting, diverging from, or amplifying another?

Several notes in this KB exhibit the same structural deficit — multiple bounded computations contributing to one shared substrate, with no explicit primitive matched to that composition mode — but the resulting failures differ because the substrates and operations differ.

## Failure modes by composition

### Contamination within context

In [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md), the shared substrate is the flat accumulated context. The composition operation is simple accumulation: system prompt, prior turns, tool outputs, and instructions all remain globally visible. Without a scoping or isolation primitive, local work contaminates later work.

This produces the pathologies named in that note: spooky action at a distance, name collision, and inability to reason locally. The failure mode here is **contamination** or **interference**. Information that should have been frame-local remains live in the global substrate.

### Inconsistency across agents

In [Multi-Agent Memory from a Computer Architecture Perspective](../sources/multi-agent-memory-computer-architecture-perspective.ingest.md), the shared substrate is multi-agent memory. The composition operation is concurrent reading and writing by multiple agents. Without visibility rules, ownership rules, or conflict-resolution protocols, the system cannot ensure that different agents are operating over a coherent view.

The failure mode here is **inconsistency**. Different agents diverge because the architecture does not specify when writes become visible, who is allowed to overwrite what, or how semantic conflicts are reconciled.

### Amplification across outputs

In [Synthesis is not error correction](./synthesis-is-not-error-correction.md), the shared substrate is the combined output artifact. The composition operation is aggregation: multiple agent outputs are merged into one result. Without an adjudication primitive such as voting, verification, or an oracle-backed selector, bad contributions are preserved rather than discarded.

The failure mode here is **amplification**. The system does not merely retain an error; it gives the error another path to survive by folding it into the merged result.

## The design implication

These are not three names for one bug. They are three manifestations of one failure schema — **uncoordinated composition over a shared substrate** — but each requires a different primitive:

| Composition mode | Missing primitive | Failure mode |
|---|---|---|
| Flat context accumulation | Scoping / isolation | Contamination |
| Shared mutable memory | Consistency / ownership / visibility | Inconsistency |
| Output aggregation | Adjudication / verification / voting | Amplification |

This is why [agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md) needs to distinguish **coordination form** from **coordination guarantee**. Labels like `conversation`, `forking`, and `shared-state` tell you the channel. They do not tell you which failure modes have actually been addressed.

The unification claim is limited but useful: these cases do not share one remedy, but they share one architectural question. Whenever multiple computations contribute to one shared semantic substrate, ask what coordination guarantee matches that composition mode.

---

Relevant Notes:

- [agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md) — extends: splits coordination into form and guarantee because the same channel can support or omit very different protections
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — evidence: flat inherited context fails by contamination when there is no isolation primitive
- [synthesis is not error correction](./synthesis-is-not-error-correction.md) — evidence: output aggregation fails by amplification when there is no adjudication primitive
- [Ingest: Multi-Agent Memory from a Computer Architecture Perspective](../sources/multi-agent-memory-computer-architecture-perspective.ingest.md) — evidence: shared multi-agent memory fails by inconsistency when there is no consistency protocol
- [session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md) — extends: execution-boundary design is one place where coordination guarantees determine what survives
