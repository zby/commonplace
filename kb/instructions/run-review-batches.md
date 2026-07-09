---
description: Run review gates by selecting target pairs, creating grouped review jobs, delegating each job, and finalizing results
type: kb/types/instruction.md
---

# Run review batches

Review selected `(note, gate)` pairs from inside the current agent harness. The parent agent coordinates selection, job creation, worker scheduling, finalization, verification, and reporting. Sub-agents perform review judgment.

Use this procedure for either:

- explicit review of requested gates, even if they are already fresh
- stale review selected from accepted review state

Inputs:

- `{model-partition}` — review model partition, for example `claude-opus` or `codex`. Derive it from the orchestrator's own model (see below), not a guessed default.
- which gates to select — `{gate-or-bundle}...` (gate ids, bundle names, or type-conformance requests, for example `semantic/grounding-alignment`, `prose/source-residue`, `prose`, or `type`), or `--all-gates` to select every applicable review criterion (all catalog gates plus each typed note's type-conformance pair). `--all-gates` chooses pairs only; the run still proceeds through the create-jobs → delegate → finalize steps below
- note scope — `--note {note-or-dir}...` or `--current`
- selector mode — `requested` for explicit execution, or default stale selection
- grouping — `note` or `gate`

The partition is fixed at selection, before any worker runs, so the orchestrator must choose it up front. Sub-agents inherit the orchestrator's model unless explicitly overridden, so read the orchestrator's own exact model ID from its environment context and pick the partition that `build_model_partition` maps it to (the registry is `MODEL_PARTITION_REGISTRY` in `src/commonplace/review/review_model.py`). Use that partition for the selector `--model-partition`. The worker still reports the model it actually ran, and the orchestrator finalizes with that exact reported model; if the reported model maps to a different partition than the job's, the inheritance assumption broke — re-run under the correct partition rather than forcing the finalize.

Two model flags, two meanings: every partition-valued flag in the review CLI is named `--model-partition` and takes a partition name (`claude-opus`, `claude-opus-4.8`, `codex`). The one exception is `commonplace-finalize-review-job --model`, which takes the *concrete* model the worker reported (for example `claude-fable-5`) — finalization derives its partition and validates it against the job's. Never pass a partition name to finalize's `--model`, and never pass a concrete model where a `--model-partition` flag expects a partition (aliases normalize, but the JSON output and DB then record the canonical partition, not what you typed).

Always create jobs from selector JSON. The job creator has no direct note or pair mode.

If the harness cannot launch sub-agents or workers, stop and report that review-batch delegation is unavailable. Do not review the batches locally unless the user explicitly authorizes a local fallback for this run.

## Select and create jobs

### Explicit requested review

Use requested mode when the user has provided the exact gates or bundles to run and freshness should not skip already-reviewed pairs.

```bash
commonplace-review-target-selector --mode requested --model-partition {model-partition} {gate-or-bundle}... --note {note-path} --json \
  | commonplace-create-review-jobs --input - --grouping {note|gate} [--batch-size {n}]
```

For a current-status sweep over explicit gates:

```bash
commonplace-review-target-selector --mode requested --model-partition {model-partition} {gate-or-bundle}... --current --json \
  | commonplace-create-review-jobs --input - --grouping {note|gate} [--batch-size {n}]
```

### Stale review

Use default stale mode when the review store should decide which applicable pairs need review.

```bash
commonplace-review-target-selector --model-partition {model-partition} {gate-or-bundle}... --note {note-or-dir}... --json \
  | commonplace-create-review-jobs --input - --grouping {note|gate} [--batch-size {n}]
```

For all gates over current notes:

```bash
commonplace-review-target-selector --model-partition {model-partition} --all-gates --current --json \
  | commonplace-create-review-jobs --input - --grouping {note|gate} [--batch-size {n}]
```

Add `--reason {missing-review|gate-changed|note-changed}` to the selector only when the user asks for that stale subset.

### Choose grouping

- Use `--grouping note` for note-centric review. Jobs are grouped by note and bundle/lens; use this for one note with several gates, or when each worker should focus on one note.
- Use `--grouping gate` for gate-centric review. Jobs are grouped by gate and chunked by `--batch-size`; use this when many notes need the same gate reviewed.
- `--batch-size` is valid only with `--grouping gate`.

The selector emits applicable `(note, gate)` pairs. The creator consumes that JSON, creates queued review jobs, writes canonical prompts, and returns a JSON object with `jobs`. Creation is runner-agnostic; runner provenance stays null until finalization records it. Capture each job object, especially:

- `review_job_id`
- derived `prompt_path`
- derived `bundle_output_path`
- each pair's `gate_id` and `gate_path`

Each returned job is one review batch for this procedure. Do not invent, merge, split, or reorder jobs. Use exactly the job grouping and pair list the creator returns.

## Delegate jobs

Launch one sub-agent per returned job, subject to the harness's concurrency limit. If there are more jobs than available workers, queue the remaining jobs and launch them as workers finish.

Launch workers on the inherited orchestrator model (do not override it), so the model actually run matches the partition chosen at selection. The parent cannot observe which concrete model a sub-agent ran, so it must not record provenance from its own inference: require each worker to report its own exact model ID and reasoning effort when the environment states them, and finalize the job with the reported values. `build_model_partition(reported_model, reported_effort)` must equal the job's `model_partition`; a mismatch means inheritance did not hold. The worker only reports these; it never runs finalization or any other bookkeeping command. If a worker cannot report a concrete model, mark the model as unknown for that job and finalize with only `--runner`.

Give each sub-agent exactly one job object and this task:

```text
Review job {review_job_id}.

Read {prompt_path} and follow it exactly. It is the authoritative reviewer instruction for this job.
Write the complete sentinel-bracketed review output to {bundle_output_path}.

Do not edit the reviewed note, review gates, manifests, indexes, or any library artifact.
Do not run commonplace-* commands.
Do not finalize the output.
Return the gates reviewed and their PASS/WARN/FAIL/ERROR decisions.
Also return your exact model ID and reasoning effort, copied verbatim from the explicit model-ID line in your environment context. Do not guess or infer them.
```

The sub-agent owns only its `bundle_output_path`. The parent owns job creation, dispatch bookkeeping, worker scheduling, finalization, verification, and reporting.

## Finalize completed jobs

```bash
commonplace-finalize-review-job --review-job-id {review-job-id} --runner {worker} --model {worker-model}
```

Pass the model the worker reported to `--model`; finalization validates `build_model_partition(--model, --effort)` against the job's `model_partition` before mutating state. If the worker reported an explicit reasoning effort, also pass `--effort {low|medium|high|xhigh}`. Pass only `--runner` when the worker could not report a concrete model. If the harness exposes opaque execution telemetry, pass it with `--telemetry-json`.

Run finalization once per completed sub-agent output. This reads the job-owned derived `bundle_output_path`, strictly parses the sentinel-bracketed pair bundle, records provenance and per-pair decisions, writes result files, appends acceptance events, and finalizes the review job. Finalization is all-or-nothing: a missing or malformed pair block fails the whole job and records no pair decisions or acceptance events.

After finalization, `MANIFEST.json` in the job artifact directory is refreshed for inspection with job-derived pair display status and derived `result_path` files. Treat the returned job payload and derived job paths as pipeline state; do not read `MANIFEST.json` to decide what to finalize.

## Verify

After all jobs finalize, verify that the intended pairs are no longer stale under the same model partition.

For requested-mode runs, rerun the same gate and note scope without `--mode requested`:

```bash
commonplace-review-target-selector --model-partition {model-partition} {gate-or-bundle}... --note {note-or-dir}... --json
```

For stale-mode runs, rerun the same selector command used for selection. An output object with `"targets": []` means the selected pairs are fresh for that model partition.

## Do not

- Do not bypass selector JSON when creating jobs.
- Do not let the parent agent perform the review judgment when sub-agent delegation is available.
- Do not invoke retired manual review-writing or ingest commands; use `commonplace-finalize-review-job`.
- Do not skip a requested gate block in the bundle output.
- Do not ask sub-agents to run finalization or any other bookkeeping command.
- Do not combine multiple jobs into one output file.
