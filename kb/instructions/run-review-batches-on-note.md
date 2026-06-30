---
description: Run explicit review gates on one note by creating review-job batches and delegating each batch to a sub-agent
type: kb/types/instruction.md
---

# Run review batches on one note

Review a specific note against an explicit list of gates from inside the current agent harness. The parent agent coordinates; sub-agents perform review judgment.

Inputs:

- first argument: `{note-path}` — repository-relative note path, for example `kb/notes/linking-theory.md`
- remaining arguments: `{gate-or-bundle}...` — one or more gate ids or bundle names, for example `semantic/grounding-alignment`, `prose/source-residue`, or `prose` (= all prose gates)

Do not run stale selection to choose gates. Use the selector only in requested mode to normalize the provided execution set.

If the harness cannot launch sub-agents or workers, stop and report that review-batch delegation is unavailable. Do not review the batches locally unless the user explicitly authorizes a local fallback for this run.

## Live agent path

### 1. Select requested pairs and create review jobs

```bash
commonplace-review-target-selector --mode requested --model {model-partition} {gate-or-bundle}... --note {note-path} --json \
  | commonplace-create-review-jobs --input - --grouping note
```

The selector emits the explicitly requested applicable `(note, gate)` pairs. The creator consumes that JSON, groups the pairs by bundle/lens, creates queued review jobs, writes canonical prompts, and returns a JSON object with `jobs`. Creation is runner-agnostic; runner provenance stays null until a later execution path records it. Capture each job object, especially:

- `review_job_id`
- `prompt_path`
- `bundle_output_path`
- each pair's `gate_id` and `gate_path`

Each returned job is one review batch for this procedure. Do not invent, merge, or reorder jobs. Use exactly the job grouping and pair list the helper resolves.

### 2. Delegate each job to a sub-agent

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

### 3. Finalize each completed batch

```bash
commonplace-finalize-review-job --review-job-id {review-job-id}
```

Run finalization once per completed sub-agent output. This reads the job-owned `bundle_output_path`, parses the bundle with the same parser used by `commonplace-run-review-bundles`, records the per-pair reviews, and finalizes the review job.

After finalization, `MANIFEST.json` at `manifest_path` is refreshed for inspection with pair statuses and per-gate `result_path` files. Treat database paths as pipeline state; do not read `MANIFEST.json` to decide what to finalize. For this single-note path, parsed review files are named by the gate leaf, for example `clause-packing.md`.

### 4. Verify the requested set

After all jobs finalize, check the same note and requested gate set under the same model partition:

```bash
commonplace-review-target-selector --model {model-partition} {gate-or-bundle}... --note {note-path} --json
```

An output object with `"targets": []` means the requested pairs are fresh for that model partition.

## Do not

- Do not run stale selection to choose gates before reviewing. This instruction is for explicit execution.
- Do not let the parent agent perform the review judgment when sub-agent delegation is available.
- Do not invoke retired manual review-writing or ingest commands; use `commonplace-finalize-review-job`.
- Do not skip a requested gate block in the bundle output.
- Do not ask sub-agents to run finalization or any other bookkeeping command.
- Do not combine multiple jobs into one output file.
