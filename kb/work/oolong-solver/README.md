# Oolong solver workshop

Phase-1 empirical test of the KB's computational-model cluster: build an Oolong solver that applies every applicable mechanism from the library — symbolic scheduling, judgment routing, frontloading, decomposition heuristics, voting — and test whether it beats the published state of the art.

## Why Oolong

Oolong ([Bertsch et al., 2025](https://arxiv.org/abs/2511.02817)) tasks decompose into per-chunk atomic analysis (classification, extraction — semantic judgment) followed by aggregation (counting, argmax, temporal/user relations — bookkeeping). That is precisely the split the [error-correction asymmetry](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) claim is about, so the benchmark is a near-ideal instrument for the cluster's central predictions.

The strongest baseline is already in the KB: [Coding Agents are Effective Long-Context Processors](../../sources/coding-agents-are-effective-long-context-processors.md) (Cao et al., 2026) sets SOTA on both splits with *off-the-shelf* coding agents — in our vocabulary, an [LLM-mediated scheduler, the degraded variant](../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) with emergent strategy. Their published Oolong trace shows the agent codifying semantic classification into regex heuristics — the over-codification mistake named in [codify-versus-llm decision heuristics](../../notes/codify-versus-llm-decision-heuristics.md). The clean model predicts a designed scheduler that routes judgment correctly gains accuracy exactly there. Oolong-Real SOTA is ~37: large headroom.

## Shape of the test

**Phase 1 (this workshop): kitchen-sink.** Apply everything at once and try to beat SOTA. If the maximal designed system cannot beat an emergent coding agent at matched backbone and cost, no ablation is worth running — and that outcome is itself evidence on the [codification/relaxing boundary](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md).

**Phase 2 (later, separate): ablations.** Remove one mechanism at a time so each KB claim is tested in isolation. Pre-registered in the design doc but not built here.

The chunk/batch-size sweep in phase 1 doubles as measurement of the soft-degradation curve — the empirical input the [agent-complexity-theory workshop](../agent-complexity-theory/README.md) needs for its tradeoff/reliability theorem family. This workshop is the empirical leg of that program.

## Files

- [solver-design.md](./solver-design.md) — benchmark facts, pre-registered predictions, architecture, mechanism map, protocol, risks

## What closes this workshop

The solver has been run on both Oolong splits against a same-backbone coding-agent baseline, the prediction register in `solver-design.md` is graded, and the durable conclusions are extracted to `kb/notes/` (either evidence that designed orchestration beats emergent orchestration, or evidence locating the bitter-lesson boundary — both outcomes are extractable). Then delete the directory.

Blocking precondition before building: ingest and position against [the λ-calculus Y-combinator paper](https://arxiv.org/abs/2603.20105), which appears to do planned map-reduce with bounded calls on Oolong. If it already implements the designed-scheduler comparison, the contribution narrows to judgment routing and the theory link — see risks in the design doc.
