---
description: "Autonomous selection-based learning with fixed weights requires a base LLM capable of five loop competences: operative rule consumption, causal diagnosis, candidate synthesis, local judgment, and store-level maintenance"
type: types/note.md
traits: [title-as-claim]
tags: [self-improving-systems, improvement-loop, continual-learning, learning-theory]
---

# Autonomous selection-based learning requires five base LLM competences

Holding model weights fixed while updating a store of procedures, hypotheses, and code does not remove dependence on the base model's weights. For an autonomous [selection-based learning](./definitions/selection-based-learning.md) loop to close without a person supplying the decisive steps, the frozen LLM must already supply the competences that run the loop itself. Below that floor, edits to prompts, notes, or tools cannot substitute for capabilities the loop needs to read, diagnose, propose, or select changes.

Each part of a reflective loop—acting on what is retained, diagnosing a failure, proposing a fix, judging it, and keeping the store healthy over time—places a distinct demand on the frozen model:

1. **Following retained rules in operation.** The model must read retained instructions, contracts, hypotheses, and tool specs and let them change its behavior, rather than loading a file and ignoring it or dropping constraints under realistic context loads ([operative change](./definitions/operative-change.md)).
2. **Diagnosing failures through traces and tools.** It must inspect execution traces, logs, and repositories, pick targeted checks whose answers could flip a decision, and respect coverage gaps instead of treating absent records as proof of safety ([diagnostic richness](./diagnostic-richness-constrains-outer-loop-learning-quality.md)).
3. **Synthesizing reusable candidates across text and code.** It must formulate reusable procedures, testable hypotheses, discriminating checks, and executable scripts—not only narrow one-off exceptions.
4. **Making local comparative judgments without a scalar score.** It must weigh competing consequences against standing commitments among the alternatives reached, leave genuinely contested or under-evidenced comparisons open, and scope bounded reversible trials ([on-balance judgment with an LLM](./on-balance-judgment-with-an-llm.md)).
5. **Maintaining the store and revising its criteria.** It must notice when accumulated entries conflict, bloat context, or pass a misleading check—and prune, refactor, or revise the working criterion ([double-loop learning](./definitions/single-loop-and-double-loop-learning.md)) rather than append another workaround.

These five competences fail independently and sit at different capability thresholds. A model can follow clear instructions or draft local patches while still misreading noisy traces, overclaiming certainty on incomplete logs, or leaving conflicting rules unpruned. Separating them lets a human-assisted bootstrap identify which competence currently binds: people temporarily supply the missing step while transfer tests measure each kind of decision on its own.

A bounded empirical illustration appears in [Harness Evolution Hits a Ceiling](../sources/harness-evolution-ceiling-weight-training.ingest.md), where the three weakest tested models produced no held-out gains under the same harness-evolution loop that improved stronger models. Even inside one benchmark and loop, a base-model capability floor can block outer-loop learning before the store itself saturates.

## Scope

- This note states necessary base competences for operating a selection-based loop autonomously; clearing all five does not by itself guarantee sustained continual learning.
- The list reflects the loop's current operating demands and stays open to concrete limits established by later evidence.

## Open Questions

- Which of the five competences binds first on current frontier models in real software and knowledge-base maintenance?
- For each competence, how much can better tooling, replay harnesses, or structured interfaces lower the required model floor—and which competences (such as resisting false confidence on incomplete records or pruning interdependent stores) remain gated primarily by base model capability?

---

Relevant Notes:

- [Selection-based learning](./definitions/selection-based-learning.md) — defined-in: the loop whose autonomous operation requires these five competences
- [On-balance judgment with an LLM](./on-balance-judgment-with-an-llm.md) — extends: develops competence 4 and how to test an LLM selector
- [Single-loop and double-loop learning](./definitions/single-loop-and-double-loop-learning.md) — defined-in: the criterion-revision capability required by competence 5
- [Operative change](./definitions/operative-change.md) — defined-in: why loading a retained artifact without behavioral dependence fails competence 1
- [Diagnostic richness constrains outer-loop learning quality](./diagnostic-richness-constrains-outer-loop-learning-quality.md) — extends: how the evidence interface interacts with competence 2
- [Harness Evolution Hits a Ceiling](../sources/harness-evolution-ceiling-weight-training.ingest.md) — evidenced-by: weak-model lines produced no held-out harness gains under a loop that lifted stronger models (bounded to one benchmark and loop)
