---
description: "Review workers receive only a generated prompt path, write one transport output, and may label an optional self-reported model without conversational bookkeeping"
type: ../types/adr.md
tags: []
status: accepted
---

# 067-Review workers read one prompt and write one output

**Status:** accepted
**Date:** 2026-08-20

## Context

[ADR 035](./035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md)
made review workers judgment-only file transducers while the parent owns job
creation and finalization. The operating procedure accumulated a second,
dispatch-time contract around the generated prompt that repeated its rules and
asked for a conversational result summary and a model report. Two instruction
surfaces for the same rules drift.

The finalizer consumes the job output file, not the worker's conversational
response. Job ids identify parent-owned state. Harness-supplied model and effort
provenance comes from launch configuration or telemetry when the harness exposes
them. A reviewer may nevertheless know its concrete model when the harness does
not expose it to the parent; discarding that claim is unnecessary, but recording
it as ordinary `runner_model` would hide its source.

The job output itself is a transport artifact, not a canonical review report.
Finalization parses it into per-pair evidence and freshness state. A downstream
workflow may retain a copy of finalized evidence for its own packet, but that is
parent-owned retention work, not part of review judgment.

## Decision

The generated `prompt.md` is the complete and sole job-specific task contract
presented to a review worker. The worker starts in a fresh context with parent
conversation inheritance disabled. Ambient system, developer, and repository
governance remains in force, but the parent's task and execution trace do not
cross the boundary. Dispatch passes only the prompt path.

The prompt owns all worker-relevant details: captured inputs, permitted reading
scope, the exact job-owned output filename, write isolation, the sentinel
protocol, and the requested pairs. The worker writes that one output file and
does not create directories, copy artifacts, edit library state, or run review
bookkeeping commands.

When its environment explicitly states the exact model ID, the worker may add
one optional `self-reported-model` line to the output; it omits the line when
the model is unavailable and never guesses or infers it. Finalization carries
the value into finalized result metadata only: it does not populate
`runner_model`, validate `model_partition`, or enter freshness identity.

Do not add a dispatch wrapper that repeats the job id, output path, restrictions,
or expected pair results. Do not impose a machine-consumed conversational return
shape. Worker completion is a lifecycle signal; the written output file is the
only review result the parent verifies and finalizes.

Do not add a model question to the dispatch wrapper or require the optional field.
The parent passes concrete provenance to finalization only when the harness
supplies it as launch metadata or execution telemetry. Unknown harness provenance
remains null even when `self-reported-model` is present. The selected
`model_partition` still has to be known before job creation; when known concrete
harness metadata is supplied at finalization, its derived partition must match
the job.

Review job ids remain parent-facing state and are not shown to the worker; they
do not change the judgment or distinguish pairs inside a job.

This decision is operative through the generated prompt renderer and the binding
[`run-review-batches`](../../instructions/run-review-batches.md) procedure.

## Considered alternatives

**Keep the defensive dispatch wrapper.** Repeating restrictions near worker
launch looked safer, but it made the reviewer reconcile two contracts and invited
the wrapper to lag behind prompt changes. The prompt is generated, tested, and
already contains the output and isolation rules.

**Pass both prompt and output paths.** This saves the worker one lookup but creates
a second authority for the destination. Passing only the prompt path makes any
disagreement impossible: the prompt names the file it expects.

**Use the worker's conversational response for summaries and model disclosure.**
This creates a parallel result channel that finalization does not consume. The
optional file field retains the useful disclosure beside the judgment while its
name preserves the weaker evidence source.

**Promote the self-report to `runner_model`.** This would make it participate in
partition validation and persist in the job row, but it would erase the
difference between a worker claim and harness-supplied execution metadata.

**Let workers write finalized per-pair evidence directly.** That would bypass the
strict all-or-nothing parser and the single transaction that advances freshness.
The job-owned output remains the transport boundary; deterministic finalization
remains parent-owned.

## Consequences

- Review workers inherit no parent conversation and spend their context on the assay rather than job bookkeeping.
- The prompt renderer is the single authority for output ownership and isolation.
- Parent orchestration checks one file and does not parse or preserve a duplicate
  conversational result.
- Concrete `runner_model` and effort fields remain absent when the harness cannot
  supply them. An optional `self-reported-model` remains visibly separate.
- Finalized result files and finalizer JSON preserve a known self-report without
  requiring a review-store schema change or making it freshness identity.
- Job directories, transport output, finalized evidence, and workflow retention
  copies may still coexist because they serve different consumers, but only the
  transport filename crosses the reviewer boundary through the generated prompt.
- Future harness integrations must preserve the one-prompt dispatch boundary;
  richer lifecycle or telemetry support belongs outside the reviewer task.

---

Relevant Notes:

- [035-Review jobs finalize all-or-nothing with derived artifacts](./035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md) — part-of: retains its parent-owned dispatch and deterministic finalization boundary while narrowing the worker-facing contract
- [Review system architecture](../review-architecture.md) — implemented-by: the prompt renderer and finalization path that enforce the decision
- [Harness sub-agent model selection regression](../harness-sub-agent-model-selection-regression.md) — evidenced-by: shows why a worker claim can be useful contradiction evidence while remaining distinct from harness-observed execution provenance
- [Run review batches](../../instructions/run-review-batches.md) — procedure: the binding orchestration procedure that dispatches the generated prompt
