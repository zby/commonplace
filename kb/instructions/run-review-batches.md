---
description: Run review gates by selecting target pairs, creating grouped review jobs, delegating each job, and finalizing results
type: kb/types/instruction.md
---

# Run review batches

Review selected `(note, gate)` pairs from inside the current agent harness. The parent agent coordinates selection, job creation, claiming, finalization, verification, and reporting. Sub-agents perform review judgment.

Use this procedure for either:

- explicit review of requested gates, even if they are already fresh
- stale review selected from accepted review state

Inputs:

- `{model-partition}` — review model partition, for example `claude-opus` or `codex`
- `{gate-or-bundle}...` or `--all-gates` — gate ids or bundle names, for example `semantic/grounding-alignment`, `prose/source-residue`, or `prose`
- note scope — `--note {note-or-dir}...` or `--current`
- selector mode — `requested` for explicit execution, or default stale selection
- grouping — `note` or `gate`

Always create jobs from selector JSON. The job creator has no direct note or pair mode.

If the harness cannot launch sub-agents or workers, stop and report that review-batch delegation is unavailable. Do not review the batches locally unless the user explicitly authorizes a local fallback for this run.

## Select and create jobs

### Explicit requested review

Use requested mode when the user has provided the exact gates or bundles to run and freshness should not skip already-reviewed pairs.

```bash
commonplace-review-target-selector --mode requested --model {model-partition} {gate-or-bundle}... --note {note-path} --json \
  | commonplace-create-review-jobs --input - --grouping {note|gate} [--batch-size {n}]
```

For a current-status sweep over explicit gates:

```bash
commonplace-review-target-selector --mode requested --model {model-partition} {gate-or-bundle}... --current --json \
  | commonplace-create-review-jobs --input - --grouping {note|gate} [--batch-size {n}]
```

### Stale review

Use default stale mode when the review store should decide which applicable pairs need review.

```bash
commonplace-review-target-selector --model {model-partition} {gate-or-bundle}... --note {note-or-dir}... --json \
  | commonplace-create-review-jobs --input - --grouping {note|gate} [--batch-size {n}]
```

For all gates over current notes:

```bash
commonplace-review-target-selector --model {model-partition} --all-gates --current --json \
  | commonplace-create-review-jobs --input - --grouping {note|gate} [--batch-size {n}]
```

Add `--reason {missing-review|gate-changed|note-changed}` to the selector only when the user asks for that stale subset.

### Choose grouping

- Use `--grouping note` for note-centric review. Jobs are grouped by note and bundle/lens; use this for one note with several gates, or when each worker should focus on one note.
- Use `--grouping gate` for gate-centric review. Jobs are grouped by gate and chunked by `--batch-size`; use this when many notes need the same gate reviewed.
- `--batch-size` is valid only with `--grouping gate`.

The selector emits applicable `(note, gate)` pairs. The creator consumes that JSON, creates queued review jobs, writes canonical prompts, and returns a JSON object with `jobs`. Creation is runner-agnostic; runner provenance stays null until a later execution path records it. Capture each job object, especially:

- `review_job_id`
- `prompt_path`
- `bundle_output_path`
- each pair's `gate_id` and `gate_path`

Each returned job is one review batch for this procedure. Do not invent, merge, split, or reorder jobs. Use exactly the job grouping and pair list the creator returns.

## Delegate jobs

Launch one sub-agent per returned job, subject to the harness's concurrency limit. If there are more jobs than available workers, queue the remaining jobs and launch them as workers finish.

Before launching a worker for a job, claim it from the parent session:

```bash
commonplace-claim-review-job --review-job-id {review-job-id} --runner {worker} --model {model-partition}
```

If the concrete worker model and partition differ, pass the concrete worker model to `--model`. If the worker uses an explicit reasoning effort, also pass `--effort {low|medium|high|xhigh}`. The claim records dispatch provenance only; it does not run the worker.

Give each sub-agent exactly one job object and this task:

```text
Review job {review_job_id}.

Read {prompt_path} and follow it exactly. It is the authoritative reviewer instruction for this job.
Write the complete sentinel-bracketed review output to {bundle_output_path}.

Do not edit the reviewed note, review gates, manifests, indexes, or any library artifact.
Do not run commonplace-* commands.
Do not finalize the output.
Return the gates reviewed and their PASS/WARN/FAIL/ERROR decisions.
```

The sub-agent owns only its `bundle_output_path`. The parent owns job creation, claim/dispatch bookkeeping, worker scheduling, finalization, verification, and reporting.

## Finalize completed jobs

```bash
commonplace-finalize-review-job --review-job-id {review-job-id}
```

Run finalization once per completed sub-agent output. This reads the job-owned `bundle_output_path`, parses the sentinel-bracketed pair bundle, records per-pair reviews, writes result files, appends acceptance events for completed pairs, and finalizes the review job.

After finalization, `MANIFEST.json` in the job artifact directory is refreshed for inspection with pair statuses and `result_path` files. Treat database paths as pipeline state; do not read `MANIFEST.json` to decide what to finalize.

## Verify

After all jobs finalize, verify that the intended pairs are no longer stale under the same model partition.

For requested-mode runs, rerun the same gate and note scope without `--mode requested`:

```bash
commonplace-review-target-selector --model {model-partition} {gate-or-bundle}... --note {note-or-dir}... --json
```

For stale-mode runs, rerun the same selector command used for selection. An output object with `"targets": []` means the selected pairs are fresh for that model partition.

## Do not

- Do not bypass selector JSON when creating jobs.
- Do not let the parent agent perform the review judgment when sub-agent delegation is available.
- Do not invoke retired manual review-writing or ingest commands; use `commonplace-finalize-review-job`.
- Do not skip a requested gate block in the bundle output.
- Do not ask sub-agents to run finalization or any other bookkeeping command.
- Do not combine multiple jobs into one output file.
