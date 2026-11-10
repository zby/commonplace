---
description: "Observed July Codex regression that let 268 Sol review results be persisted as Luna, plus the August partial restoration of per-worker model overrides"
type: types/note.md
---

# Harness sub-agent model selection regression

## Observed regression (2026-07-17)

Codex's `multi_agent_v1` spawn surface accepted an explicit `model` and `reasoning_effort`. Two retained session traces show workers launched through that surface with `model: gpt-5.6-luna`; their child `turn_context` records `gpt-5.6-luna` at low and medium effort.

The later `multi_agent_v2` collaboration surface accepts task identity, context-forking, and message fields but no model field. Its workers inherit the parent model. A direct `codex exec --model luna` call is not an available fallback under the observed ChatGPT account: the backend rejects Luna as unsupported.

| Surface | Per-worker model selection | Observed result |
|---|---|---|
| `multi_agent_v1` | Explicit `model` field | Luna workers ran as requested |
| `multi_agent_v2` | No model field | Workers inherited `gpt-5.6-sol` |
| `codex exec --model luna` | CLI flag exists | Backend rejected the model for the account |

This is a harness regression, not model selection performed by Commonplace. The review system of the time used `model_partition` as review identity and freshness scope; selecting a partition did not cause the harness to dispatch that model. The current [review system](./README-REVIEW-SYSTEM.md) has no partitions and records the model each harness reports.

## Current collaboration surface (2026-08-23)

The current Codex collaboration tool again accepts explicit `model` and
`reasoning_effort` overrides for a worker, but only when `fork_turns` is `none`
or a positive turn count. A full-history fork inherits the parent model and
cannot override it. This restores a model-specific dispatch path when the
parent can supply bounded context; it does not restore arbitrary model choice
for a worker that needs the full parent history.

This local collaboration surface is distinct from the public Responses API
multi-agent feature. The [official OpenAI documentation](https://developers.openai.com/api/docs/guides/responses-multi-agent)
states that Responses API subagents share the request's model. Neither surface
makes a requested model string proof of the model that executed, so retained
execution provenance remains necessary.

## The regression produced false review provenance

Review jobs 6677–6717 were created under the `luna` partition for seven notes: 41 jobs containing 268 review pairs. Every retained child trace for those jobs records `gpt-5.6-sol` at maximum effort. The parent nevertheless finalized each job with `--model luna`, so all 268 generated pair results record both `model_partition: luna` and `runner_model: luna`.

The stored provenance therefore contradicts the execution traces. Those results may be read as Sol judgments, but they are not Luna review evidence and must not satisfy a Luna freshness claim. Snapshot freshness cannot repair incorrect execution provenance.

The incident exposed the parent-trust boundary described by [ADR 034](./adr/034-queued-review-jobs-and-execution-provenance.md): finalization validates the model string supplied by the parent against the selected partition, but it does not establish that the worker actually ran that model.

## Operational consequence

A model-specific sweep is now executable through the current collaboration
surface when the required model is available and the worker can run from a
bounded fork. A full-history worker still inherits the parent model. In either
case, a worker label, task name, requested partition, or intended model is not
execution evidence. When a trace is available, `turn_context.payload.model` is
the concrete execution record; `commonplace-review` reads a codex worker's
model from that record rather than from a parent-supplied string.

The restored request field does not repair prior evidence. Jobs 6677–6717 and
their misattributed Luna evidence were in the review store that
[ADR 127](./adr/127-review-runs-as-workflows-over-result-files.md) abandoned
without migration, so no current result rests on them.

---

Relevant Notes:

- [Run review batches](../instructions/run-review-batches.md) — procedure: dispatch and provenance rules affected by this harness regression
- [OpenAI Responses API multi-agent documentation](https://developers.openai.com/api/docs/guides/responses-multi-agent) — see-also: documents the separate public surface whose subagents share the request model
