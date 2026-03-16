---
description: Agent orchestration is not ordered along a single ladder — scheduler placement, persistence, coordination form, coordination guarantees, and return artifacts vary independently across architectures
type: note
traits: [has-external-sources]
tags: [computational-model]
status: seedling
---

# Agent orchestration occupies a multi-dimensional design space

Agent orchestration architectures are often discussed as if they sit on a single progression: raw chat loop, better chat loop, symbolic scheduler, versioned infrastructure. That framing collapses several independent design choices into one axis. The result is unstable taxonomies where every new system requires "adding another point" to a list that was never one-dimensional to begin with. The better picture is a design space with separable dimensions, so new systems can occupy new combinations without rewriting the taxonomy.

## Scheduler placement

**Where the scheduler lives** — in the LLM conversation itself ([LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md)) or in symbolic code / an external runtime ([bounded-context orchestration model](./bounded-context-orchestration-model.md)). This is the clean-model / degraded-model split: whether bookkeeping and recursion run on exact state or inside bounded stochastic context. [RLM](./rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation.md) is a boundary case — the scheduler lives on an exact substrate outside chat even when the model authors some of that scheduler code.

## Persistence horizon

**How long orchestration knowledge persists** — per-step only (conversational loops), per-session (Slate's episodes retained across a task), or cross-session (versioned scheduler logic, reusable workflow artifacts). RLM externalises the loop but keeps the scheduler ephemeral; versioned orchestration pushes the same pattern into durable infrastructure; Slate occupies an intermediate point where compressed products persist within the session without becoming long-term artifacts.

## Coordination form

**How bounded contexts coordinate** — direct prompt assembly, back-and-forth conversation, prompt refinement, shared-state / blackboard, or context cloning / forking. [Conversation vs prompt refinement](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) shows these are not reducible to one another and can combine with any scheduler placement.

## Coordination guarantee

**What failure mode the architecture prevents when coordination happens.** The form of coordination does not tell you whether the architecture is safe — a shared substrate can exist with or without the guarantee matched to its composition mode. [Agent orchestration needs coordination guarantees, not just coordination channels](./agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md) develops this in detail. The three main guarantee families:

- **Isolation / scoping** — prevents contamination
- **Consistency / ownership / visibility** — prevents inconsistency in shared state
- **Adjudication / verification / voting** — prevents error amplification in combined outputs

## Boundary-return artifact

**What comes back from a bounded execution** — raw natural-language output, structured extraction, compressed episode / branch summary, or symbolic code / control program. The return artifact determines what the next stage can do cheaply: a compressed episode supports orchestration differently from a raw transcript; code supports exact re-execution differently from a prose summary.

## Why this matters

The multi-dimensional framing explains why single-axis taxonomies keep breaking. Slate adds a new combination because it changes persistence horizon and boundary-return artifact simultaneously. [Forking](../sources/voooooogel-multi-agent-future.ingest.md) changes coordination form without changing scheduler placement. Treating both as "extra points on one line" obscures what each system actually varies.

The value is not taxonomy for its own sake but sharper questions:

- Which dimensions are structural and likely to survive scaling?
- Which dimensions interact, and which vary independently?
- Where do current systems cluster, and which regions are unexplored?

This should stay an open map, not a closed classification. The current dimensions are salient, not final.

---

Relevant Notes:

- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: the clean model supplies one important dimension, scheduler placement
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — one region of the space: scheduling inside conversation
- [RLM achieves the clean scheduler model but opts out of accumulation](./rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation.md) — boundary case: model-authored external scheduler with ephemeral persistence
- [LLM frameworks should expose the loop](./llm-frameworks-should-expose-the-loop.md) — consequence: framework design concerns one dimension of the larger space
- [conversation vs prompt refinement in agent-to-agent coordination](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — grounds: coordination forms vary independently of scheduler placement
- [agent orchestration needs coordination guarantees, not just coordination channels](./agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md) — sharpens: coordination form and coordination guarantee are separate dimensions because different shared substrates fail in different ways
- [Ingest: Slate: Moving Beyond ReAct and RLM](../sources/slate-moving-beyond-react-and-rlm.ingest.md) — extends: episodes and thread-weaving add combinations the one-axis framing cannot represent cleanly
- [What Survives in Multi-Agent Systems](../sources/voooooogel-multi-agent-future.ingest.md) — extends: forking is better treated as a coordination/scoping primitive than as another point on a single scheduler ladder
