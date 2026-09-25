---
type: note
description: Tardigrade derives model progression from event history and separates
  compaction and schema repair from host durability
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-25-tardigrade-01
source-identity: https://github.com/clavia-labs/tardigrade
reviewed-revision: 1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-tardigrade-01/result.md
analysis-result-sha256: 4adb6ca61ca273e24354be9c0e2f192ba196f8f11e0bd79f869068c0e128ac2d
---

# Tardigrade inference and compaction

Evidence basis: source and shipped documentation at `1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267`, inspected 2026-09-25. No runtime or provider experiment was performed.

This analysis covers Tardigrade's embedded inference, conversation projection, compaction and output-correction subsystem. Its physical hosts, actor transport, custom tool effects, CLI/UI and actor optimization tooling are excluded. The subsystem derives work from retained events and returns transitions/results to an enclosing executor; platform crash safety is a separate claim.

An assembly supplies instructions, tools, conversation and output policy. Infer rejects conflicting views, waits for outstanding tools, resolves a permitted model and records each attempt. The model bridge returns tool-call, completion or failure events. Recorded retry timing and fallback choices control later attempts, while repeated unanswered marks can exhaust the crash bound. These mechanisms are wired in the [inference machine](https://github.com/clavia-labs/tardigrade/blob/1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267/packages/agent/src/component/infer/machine.ts#L244-L543); physical persistence remains an external service contract.

Compaction proposes a safe boundary that preserves complete tool exchanges. Infer selects the proposal against the active model's estimated capacity; the cut retains a fraction of current visible history. A separately selected summary model receives prior summary and the new span. Completed nonempty text without tool calls becomes a checkpoint, later supplied alongside the suffix. That gate checks completion, not factual preservation. The empty-span branch reuses the previous summary while moving the boundary. See [compaction](https://github.com/clavia-labs/tardigrade/blob/1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267/packages/agent/src/component/compact/index.ts#L127-L279).

Output handling distinguishes native/validate-once failure, bounded repair and delegated correction. Schema errors and modes persist, so later attempts receive reasons for correction. Successful projectable repair hides its rejection/feedback exchange from later context while raw events remain. Schema validity licenses conformance to the declared shape, not truth of its values. The behavior is explicit in [completion validation](https://github.com/clavia-labs/tardigrade/blob/1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267/packages/agent/src/component/infer/machine.ts#L101-L163) and [transcript projection](https://github.com/clavia-labs/tardigrade/blob/1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267/packages/agent/src/projection/transcript.ts#L83-L134).

The model and runtime consume different retained parts: the model receives selected conversation/summary/feedback, while code uses identities, policies and schedules. Attachment bytes are explicitly requested from ObjectStorage. Compatible provider continuation can replace readable reconstructed messages; the gate compares provider, protocol and model, but not the retained endpoint. Opaque bytes and continuation prevent a complete text-only memory classification. External producers also leave overall lineage and write agency uncertain. See [continuation replay](https://github.com/clavia-labs/tardigrade/blob/1c4f4efaab2aaeec0bc482bc38e8ddf3be6f8267/packages/agent/src/model/execution/continuation.ts#L5-L14).

Summary and diagnostic/control transformations are wired trace-fed memory writes. They do not establish conjectural learning or self-improvement. Narrow reflection is wired where represented attempt/context state affects subsequent control; a reflective theory builder and improved task capacity are uninspected. Runtime traces, summary-fidelity checks and interventions on recalled content would strengthen those separate claims. Thread and turn boundaries alone do not establish a task horizon.

- [Exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-tardigrade-01/result.md) — see-also: canonical records, quote evidence and comparison fields.
- [Reflective system](../../notes/definitions/reflective-system.md) — defined-in: the bounded control-state mapping.
- [Conjectural learning](../../notes/definitions/conjectural-learning.md) — defined-in: the stronger capacity claim not established by retained corrections.
