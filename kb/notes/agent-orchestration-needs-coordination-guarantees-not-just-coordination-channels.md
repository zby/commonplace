---
description: Coordination channels say how bounded contexts interact, but the missing discriminator is which guarantee prevents contamination, inconsistency, amplification, or liability diffusion across the composed system
type: kb/types/note.md
traits: [title-as-claim]
tags: [computational-model]
status: seedling
---

# Agent orchestration needs coordination guarantees, not just coordination channels

Architectures are often compared by coordination channel: conversation, prompt refinement, forking, shared memory, synthesis. Two systems can use the same channel and have very different reliability properties, because the harder question is not *how* bounded contexts interact but *what guarantee* governs that interaction. When multiple computations compose into one larger system, what prevents one step from corrupting shared meaning, diverging from peers, amplifying a bad result, or diffusing responsibility downstream?

## Failure modes by composition

### Contamination within context

In [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md), the shared substrate is the flat accumulated context. System prompt, prior turns, tool outputs, and instructions all remain globally visible. Without a scoping or isolation primitive, local work contaminates later work — producing spooky action at a distance, name collision, and inability to reason locally. The failure mode is **contamination**: information that should have been frame-local remains live in the global substrate.

### Inconsistency across agents

In [Multi-Agent Memory from a Computer Architecture Perspective](https://arxiv.org/html/2603.10062v1), the shared substrate is multi-agent memory, composed by concurrent reads and writes from multiple agents. Without visibility rules, ownership rules, or conflict-resolution protocols, agents diverge. The failure mode is **inconsistency**: the architecture does not specify when writes become visible, who may overwrite what, or how semantic conflicts are reconciled.

### Amplification across outputs

In [Synthesis is not error correction](./synthesis-is-not-error-correction.md), the shared substrate is the combined output artifact. Multiple agent outputs are merged into one result. Without an adjudication primitive — voting, verification, or an oracle-backed selector — bad contributions are preserved rather than discarded. The failure mode is **amplification**: the system does not merely retain an error; it gives the error another path to survive by folding it into the merged result.

## The design implication

These are not four names for one bug. They are manifestations of one failure schema — **uncoordinated composition** — but each requires a different primitive:

| Composition mode | Missing primitive | Failure mode | Example |
|---|---|---|---|
| Flat context accumulation | Scoping / isolation | Contamination | Single-agent inherited context |
| Shared mutable memory | Consistency / ownership / visibility | Inconsistency | Tracecraft's shared S3 JSON state |
| Output aggregation | Adjudication / verification / voting | Amplification | Multi-agent synthesis without selection |
| Delegation chain / authority transfer | Liability firebreaks / authority refresh | Accountability vacuum | Transitive delegation chains |

The first three rows are failures over shared semantic substrates. The fourth is a governance failure over the authority/liability path: a chain can avoid all three semantic failures yet still lose a clearly attributable owner for downstream actions.

### Accountability vacuum in delegation chains

[Intelligent AI Delegation](https://arxiv.org/pdf/2602.11865) calls this the **accountability vacuum**: in a chain `X → A → B → C → … → Y`, intermediaries pass authority onward without necessarily retaining liability for what follows. The bad outcome is not "the system believes false things" or "the merged artifact contains an error" but "no one in the chain is clearly answerable for the error." This can arise even when every handoff is locally legible and no combined output exists — it is a governance failure, not a semantic one.

The proposed remedy is a **liability firebreak**: at certain points in a delegation chain, an intermediate node must either assume full, non-transitive liability for downstream actions or halt and request a fresh transfer of authority from the human principal. That primitive plays the same architectural role as scoping, consistency protocols, and adjudication in the first three cases — it does not make the action correct, but it makes the chain answerable.

This connects to [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md). Where verification is strong, a node can plausibly accept downstream liability because it can audit what follows. Where verification is weak, liability becomes hard to price and enforce, so the safe move shifts from "delegate and insure" to "stop and escalate." Verification is not the whole story — legal authority, organizational policy, and social trust also matter — but it determines whether accountability stays local or must be refreshed from a human principal.

## The shared question

This is why [agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md) needs to distinguish **coordination form** from **coordination guarantee**. Labels like `conversation`, `forking`, and `shared-state` tell you the channel. They do not tell you which failure modes have been addressed.

The unification claim is limited but useful: these cases do not share one remedy, but they share one architectural question. Whenever multiple computations compose into one larger system, ask what coordination guarantee matches that composition mode.

---

Relevant Notes:

- [agent orchestration occupies a multi-dimensional design space](./agent-orchestration-occupies-a-multi-dimensional-design-space.md) — extends: splits coordination into form and guarantee because the same channel can support or omit very different protections
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — evidence: flat inherited context fails by contamination when there is no isolation primitive
- [synthesis is not error correction](./synthesis-is-not-error-correction.md) — evidence: output aggregation fails by amplification when there is no adjudication primitive
- [Ingest: Multi-Agent Memory from a Computer Architecture Perspective](https://arxiv.org/html/2603.10062v1) — evidence: shared multi-agent memory fails by inconsistency when there is no consistency protocol
- [Intelligent AI Delegation](https://arxiv.org/pdf/2602.11865) — evidence: source of the accountability-vacuum and liability-firebreak vocabulary
- [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: verification cost determines whether accountability stays local or must be refreshed from the principal
- [session history should not be the default next context](./session-history-should-not-be-the-default-next-context.md) — extends: execution-boundary design is one place where coordination guarantees determine what survives
- [topology, isolation, and verification form a causal chain for reliable agent scaling](./topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling.md) — extends: argues the four failure modes map to what breaks when elements of a dependency chain (topology → isolation → verification) are missing
- [Tracecraft](../agent-memory-systems/reviews/tracecraft.md) — exemplifies: provides all five coordination channels but guarantees for almost none; non-atomic task claiming is a textbook case of the channel/guarantee gap
