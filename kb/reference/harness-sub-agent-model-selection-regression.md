---
description: "Observed Codex multi-agent regression that removed per-worker model selection and allowed Sol review executions to be persisted as Luna"
type: kb/types/note.md
---

# Harness sub-agent model selection regression

## Current state (as of 2026-07-17)

Codex's `multi_agent_v1` spawn surface accepted an explicit `model` and `reasoning_effort`. Two retained session traces show workers launched through that surface with `model: gpt-5.6-luna`; their child `turn_context` records `gpt-5.6-luna` at low and medium effort.

The later `multi_agent_v2` collaboration surface accepts task identity, context-forking, and message fields but no model field. Its workers inherit the parent model. A direct `codex exec --model luna` call is not an available fallback under the observed ChatGPT account: the backend rejects Luna as unsupported.

| Surface | Per-worker model selection | Observed result |
|---|---|---|
| `multi_agent_v1` | Explicit `model` field | Luna workers ran as requested |
| `multi_agent_v2` | No model field | Workers inherited `gpt-5.6-sol` |
| `codex exec --model luna` | CLI flag exists | Backend rejected the model for the account |

This is a harness regression, not model selection performed by Commonplace. The [review system](./README-REVIEW-SYSTEM.md) uses `model_partition` as review identity and freshness scope; selecting a partition does not cause the harness to dispatch that model.

## The regression produced false review provenance

Review jobs 6677–6717 were created under the `luna` partition for seven notes: 41 jobs containing 268 review pairs. Every retained child trace for those jobs records `gpt-5.6-sol` at maximum effort. The parent nevertheless finalized each job with `--model luna`, so all 268 generated pair results record both `model_partition: luna` and `runner_model: luna`.

The stored provenance therefore contradicts the execution traces. Those results may be read as Sol judgments, but they are not Luna review evidence and must not satisfy a Luna freshness claim. Snapshot freshness cannot repair incorrect execution provenance.

The incident exposed the parent-trust boundary described by [ADR 034](./adr/034-queued-review-jobs-and-execution-provenance.md): finalization validates the model string supplied by the parent against the selected partition, but it does not establish that the worker actually ran that model.

## Operational consequence

A model-specific sweep is not executable through the observed `multi_agent_v2` surface unless the parent itself runs the required model or the harness restores explicit per-worker selection. A worker label, task name, requested partition, or intended model is not execution evidence. When a trace is available, `turn_context.payload.model` is the concrete execution record to compare with persisted `runner_model`.

Until the regression is fixed, jobs whose required partition differs from the inherited worker model should remain unfinalized. Existing jobs 6677–6717 require replacement by genuine Luna executions or explicit retirement of their misattributed Luna evidence.

---

Relevant Notes:

- [Run review batches](../instructions/run-review-batches.md) — procedure: dispatch and provenance rules affected by this harness regression
