---
description: Agent orchestration is not ordered along a single ladder — scheduler placement, persistence, coordination, and return artifacts vary along separable dimensions across architectures
type: note
traits: [has-external-sources]
tags: [computational-model]
status: seedling
---

# Agent orchestration occupies a multi-dimensional design space

Agent orchestration architectures are often discussed as if they sit on a single progression: raw chat loop, better chat loop, symbolic scheduler, versioned infrastructure. That framing is useful locally, but it collapses several independent design choices into one axis. The result is unstable taxonomies where every new system seems to require "adding a fourth point" or "a fifth point" to a list that was never one-dimensional to begin with.

The better picture is a design space with multiple separable dimensions. New systems can occupy new combinations without forcing the taxonomy itself to be rewritten.

## Scheduler placement

The first dimension is **where the scheduler lives**:

- in the LLM conversation itself ([LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md))
- in symbolic code or an external runtime ([bounded-context orchestration model](./bounded-context-orchestration-model.md))

This dimension captures the main architectural distinction behind the clean-model / degraded-model split: whether bookkeeping and recursion run on exact state or inside bounded stochastic context. [RLM achieves the clean scheduler model but opts out of accumulation](./rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation.md) is a boundary case *within* the external category: the scheduler still lives on an exact substrate outside chat even when the model authors some of that scheduler code.

## Persistence horizon

The second dimension is **how long orchestration knowledge persists**:

- per-step only (purely conversational agent loops)
- per-session (Slate's episodes retained by the orchestrator across a task)
- cross-session (versioned scheduler logic or reusable workflow artifacts)

This is the dimension the RLM note actually cares about. RLM externalises the loop but keeps the resulting scheduler ephemeral. Versioned orchestration pushes the same pattern into durable infrastructure. Slate appears to occupy an intermediate point: compressed orchestration products persist within the session without yet becoming long-term code or repo artifacts.

## Coordination primitive

The third dimension is **how bounded contexts coordinate**:

- direct prompt assembly
- back-and-forth conversation
- prompt refinement
- shared-state / blackboard coordination
- context cloning / forking

[Conversation vs prompt refinement in agent-to-agent coordination](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) already shows that conversation, refinement, and forking are not reducible to one another. Shared-state patterns add another edge case: bounded workers can coordinate through a common symbolic substrate without directly talking to one another. These are different ways bounded contexts influence one another, and they can combine with many scheduler placements.

## Boundary-return artifact

The fourth dimension is **what comes back from a bounded execution**:

- raw natural-language output
- structured extraction
- compressed episode / branch summary
- symbolic code or control program

This matters because the return artifact determines what the next stage can do cheaply. A compressed episode supports orchestration differently from a raw transcript; code supports exact re-execution differently from a prose summary. The [Slate ingest](../sources/slate-moving-beyond-react-and-rlm.ingest.md) and the [execution-boundary compression](../log.md) observation both point at this as a distinct pattern rather than a side detail.

## Why this matters

This reframing explains why the RLM design-space section became unstable. The list mixed at least two different questions:

- where the scheduler lives
- how long its products persist

Slate adds a new combination because it changes persistence horizon and boundary-return artifact simultaneously. voooooogel's [forking](../sources/voooooogel-multi-agent-future.ingest.md) changes coordination without necessarily changing scheduler placement. Treating both as "extra points on one line" obscures what each system is actually varying.

The value of the multi-dimensional framing is not taxonomy for its own sake. It lets the KB ask sharper questions:

- Which dimensions are structural and likely to survive scaling?
- Which are temporary scaffolds or vision features?
- Which dimensions interact, and which can vary independently?
- Where do current systems cluster, and which regions of the space are still unexplored?

This should stay an open map, not a closed classification. The current dimensions are salient, not final.

---

Relevant Notes:

- [bounded-context orchestration model](./bounded-context-orchestration-model.md) — foundation: the clean model supplies one important dimension, scheduler placement
- [LLM-mediated schedulers are a degraded variant of the clean model](./llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — one region of the space: scheduling inside conversation
- [RLM achieves the clean scheduler model but opts out of accumulation](./rlm-achieves-the-clean-scheduler-model-but-opts-out-of-accumulation.md) — boundary case: model-authored external scheduler with ephemeral persistence
- [LLM frameworks should expose the loop](./llm-frameworks-should-expose-the-loop.md) — consequence: framework design concerns one dimension of the larger space
- [conversation vs prompt refinement in agent-to-agent coordination](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — grounds: coordination primitives vary independently of scheduler placement
- [Ingest: Slate: Moving Beyond ReAct and RLM](../sources/slate-moving-beyond-react-and-rlm.ingest.md) — extends: episodes and thread-weaving add combinations the one-axis framing cannot represent cleanly
- [What Survives in Multi-Agent Systems](../sources/voooooogel-multi-agent-future.ingest.md) — extends: forking is better treated as a coordination/scoping primitive than as another point on a single scheduler ladder
