---
description: Run snapshot-anchored verdict or report assays by selecting pairs, creating homogeneous jobs, delegating each job, and finalizing results
type: kb/types/instruction.md
---

# Run review batches

Run selected `(note, criterion)` pairs from inside the current agent harness. The schema and CLI use `(note_path, criterion_path)` names. The parent coordinates selection, job creation, worker scheduling, finalization, verification, and reporting; sub-agents perform the assay.

Use this procedure for either:

- explicit execution of requested gates or report assays, even if already fresh
- stale execution selected from freshness-baseline state

Inputs:

- `{model-partition}` — review model partition, for example `claude-sonnet-5` or `codex`. Required: Commonplace designates no default review model or partition, so choose one that maps to a model the current harness can actually run.
- which criteria to select — gate ids, bundle names, conformance requests (`type`, `collection`, or a narrowed virtual id), or `critique`. `--all-gates` selects the applicable verdict-kind catalog and conformance gates; report assays remain explicit opt-ins
- note scope — `--note {note-or-dir}...` or `--user-verified`
- selector mode — `requested` for explicit execution, or default stale selection
- grouping — `note` or `criterion`

The partition is fixed at selection, before any worker runs, so the orchestrator must choose it up front. Commonplace designates no default review model or partition. If the harness exposes model selection, choose an available concrete model and select with the partition `build_model_partition` maps it to (registry: `MODEL_PARTITION_REGISTRY` in `src/commonplace/review/review_model.py`). If the harness does not expose model selection, use the partition of the model its workers are documented to inherit or receive. If that partition cannot be known before selection, stop rather than create jobs under a guessed partition. No per-gate requirements are currently declared; a gate's criterion file may later declare a required partition, and selection then splits by partition.

Concrete execution provenance is separate and optional. Pass model and effort to finalization only when the harness supplies their exact values through launch configuration or execution telemetry. Do not infer them. A worker may include the generated prompt's optional `self-reported-model` field, but that claim stays separate from harness provenance and does not replace `--model`. If known harness metadata maps to a different partition than the job's, the selected or inherited model did not hold — re-run under the correct partition rather than forcing finalization. When the harness supplies no concrete model, finalize with only `--runner`.

Two model flags, two meanings: every partition-valued flag in the review CLI is named `--model-partition` and takes a partition name (`claude-sonnet-5`, `claude-opus-4.8`, `codex`). The one exception is `commonplace-finalize-review-job --model`, which takes a concrete model supplied by the harness (for example `claude-fable-5`) — finalization derives its partition and validates it against the job's. Never pass a partition name to finalize's `--model`, and never pass a concrete model where a `--model-partition` flag expects a partition (aliases normalize, but the JSON output and DB then record the canonical partition, not what you typed).

Always create jobs from selector JSON. The job creator has no direct note or pair mode.

Selector JSON carries `result_kind`. Grouping never mixes result kinds: verdict pairs and report pairs always become separate jobs. Do not infer a result contract from live criterion text at finalization time.

If the harness cannot launch sub-agents or workers, stop and report that review-batch delegation is unavailable. Do not review the batches locally unless the user explicitly authorizes a local fallback for this run.

## Select and create jobs

### Explicit requested review

Use requested mode when the user has provided the exact gates or bundles to run and freshness should not skip already-reviewed pairs.

```bash
commonplace-review-target-selector --mode requested --model-partition {model-partition} {gate-or-bundle}... --note {note-path} --json \
  | commonplace-create-review-jobs --input - --grouping {note|criterion} [--batch-size {n}]
```

For a user-verified sweep over explicit gates:

```bash
commonplace-review-target-selector --mode requested --model-partition {model-partition} {gate-or-bundle}... --user-verified --json \
  | commonplace-create-review-jobs --input - --grouping {note|criterion} [--batch-size {n}]
```

### Stale review

Use default stale mode when the review store should decide which applicable pairs need review.

```bash
commonplace-review-target-selector --model-partition {model-partition} {gate-or-bundle}... --note {note-or-dir}... --json \
  | commonplace-create-review-jobs --input - --grouping {note|criterion} [--batch-size {n}]
```

For all gates over user-verified notes:

```bash
commonplace-review-target-selector --model-partition {model-partition} --all-gates --user-verified --json \
  | commonplace-create-review-jobs --input - --grouping {note|criterion} [--batch-size {n}]
```

Add `--reason {missing-baseline|criterion-changed|note-changed}` to the selector only when the user asks for that stale subset.

### Choose grouping

- Use `--grouping note` for note-centric work. Jobs are grouped by note and bundle/lens.
- Use `--grouping criterion` for criterion-centric work. Jobs are grouped by criterion and chunked by `--batch-size`.
- `--batch-size` is valid only with `--grouping criterion`.

The selector emits applicable pairs with their persisted result kinds. The creator consumes that JSON, creates queued homogeneous jobs, writes canonical prompts, and returns `jobs`. The parent captures especially:

- `review_job_id`
- derived `prompt_path`
- derived `job_output_path`
- each pair's `criterion_id` and `criterion_path`

Each returned job is one review batch for this procedure. Do not invent, merge, split, or reorder jobs. Use exactly the job grouping and pair list the creator returns.

## Delegate jobs

Launch one sub-agent per returned job, subject to the harness's concurrency limit. If there are more jobs than available workers, queue the remaining jobs and launch them as workers finish and are closed.

Start every worker in a fresh context that does not inherit the parent conversation. In Codex, pass `fork_turns="none"` to `spawn_agent`; use the equivalent no-history launch option in another harness. Ambient system, developer, and repository instructions still apply. If the harness cannot suppress parent-turn inheritance, stop and report that isolated review delegation is unavailable.

When the harness supports explicit model selection, launch each worker with an available model that maps to the job's selected partition. Otherwise, use the harness's inherited or assigned worker model only when its partition was known at selection. Capture concrete model, effort, and telemetry only from harness-provided launch or execution metadata. The worker's optional `self-reported-model` is a separately labelled claim, not harness provenance. If the harness exposes no concrete model, leave `runner_model` unknown and finalize with only `--runner`.

Give each fresh sub-agent only this task:

```text
Read {prompt_path} and follow it exactly.
```

The generated prompt is the complete reviewer contract. It contains the captured inputs, reading scope, exact job output filename, write isolation, result protocol, and an optional `self-reported-model: <model-id>` line for workers whose environment states their exact model. Do not prepend the job id or output path, and do not request a conversational result summary or execution provenance. The sub-agent owns only the output file named by the prompt. The parent owns job creation, dispatch bookkeeping, worker scheduling, finalization, verification, and reporting.

After a worker signals completion, ignore its conversational response and verify that the parent-held `job_output_path` exists and is non-empty. Finalization returns any parsed self-report as `self_reported_model`; the parent does not need to scrape the file. Then close, terminate, or release that worker with the harness's lifecycle operation before scheduling another worker. If the harness exposes stop/interrupt rather than close, use it after the output is safely on disk. Workers are single-use contexts: do not send follow-up tasks or retain them for later jobs.

## Finalize completed jobs

```bash
commonplace-finalize-review-job --review-job-id {review-job-id} --runner {worker}
commonplace-finalize-review-job --review-job-id {review-job-id} --runner {worker} --model {worker-model} [--effort {low|medium|high|xhigh}]
```

Use the second form only when the harness supplied the concrete model; finalization validates `build_model_partition(--model, --effort)` against the job's `model_partition` before mutating state. Include `--effort` only when the harness supplied it. If the harness exposes opaque execution telemetry, pass it with `--telemetry-json`. Never fill missing provenance from reviewer prose, inference, or `self-reported-model`; finalization preserves that optional field separately.

Run finalization once per completed sub-agent output. It reads job-owned output, parses each block against the pair's persisted result kind, records provenance and per-kind completion, writes result files, creates or replaces current freshness baselines, prunes superseded evidence, and marks the job completed. Finalization is all-or-nothing: malformed or incomplete output fails the job and writes no freshness baseline.

`ERROR` means the worker could not produce a contracted result. It follows the same all-or-nothing failure path: no pair completes and no freshness baseline advances.

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
- Do not skip a requested pair block in job output.
- Do not ask sub-agents to run finalization or any other bookkeeping command.
- Do not ask sub-agents to repeat job metadata, result markers, or execution provenance in conversation.
- Do not combine multiple jobs into one output file.
