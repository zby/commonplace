---
description: Run explicit review gates on one note by creating review-job batches and delegating each batch to a sub-agent
type: kb/types/instruction.md
---

# Run review batches on one note

Review a specific note against an explicit list of gates from inside the current agent harness. The parent agent coordinates; sub-agents perform review judgment.

Inputs:

- first argument: `{note-path}` — repository-relative note path, for example `kb/notes/linking-theory.md`
- remaining arguments: `{gate-or-bundle}...` — one or more gate ids or bundle names, for example `semantic/grounding-alignment`, `prose/source-residue`, or `prose` (= all prose gates)

Do not run the selector to choose gates. Treat the provided list as the exact execution set.

If the harness cannot launch sub-agents or workers, stop and report that review-batch delegation is unavailable. Do not review the batches locally unless the user explicitly authorizes a local fallback for this run.

## Live agent path

### 1. Create review jobs and canonical prompts

```bash
commonplace-create-review-jobs --runner {codex|claude-code|live-agent} --model {model-partition} {note-path} {gate-or-bundle}...
```

The helper groups the requested gates by bundle/lens and returns a JSON object with `jobs`. Capture each job object, especially:

- `review_job_id`
- `prompt_path`
- `bundle_output_path`
- `manifest_path`
- `gate_ids`
- `gate_paths`

Each returned job is one review batch for this procedure. Do not invent, merge, or reorder jobs. Use exactly the job grouping and `gate_ids` the helper resolves.

### 2. Delegate each job to a sub-agent

Launch one sub-agent per returned job, subject to the harness's concurrency limit. If there are more jobs than available workers, queue the remaining jobs and launch them as workers finish.

Give each sub-agent exactly one job object and this task:

```text
Review job {review_job_id}.

Read {prompt_path} and follow it exactly. It is the authoritative reviewer instruction for this job.
Write the complete sentinel-bracketed review output to {bundle_output_path}.

Do not edit the reviewed note, review gates, manifests, indexes, or any library artifact.
Do not run commonplace-* commands.
Do not ingest the output.
Return the gates reviewed and their PASS/WARN/FAIL/ERROR decisions.
```

The sub-agent owns only its `bundle_output_path`. The parent owns job creation, worker scheduling, ingest, verification, and reporting.

### 3. Ingest each completed batch

```bash
commonplace-ingest-bundle-output --review-job-id {review-job-id} --input-file {bundle-output-path}
```

Run ingest once per completed sub-agent output. This parses the bundle with the same parser used by `commonplace-run-review-bundles`, records the per-pair reviews, and finalizes the review job.

After ingest, `MANIFEST.json` at `manifest_path` is refreshed with pair statuses and per-gate `result_path` files. For this single-note path, parsed review files are named by gate id, for example `sentence__clause-packing.md`.

### 4. Verify the requested set

After all jobs ingest, check the same note and requested gate set under the same model partition:

```bash
commonplace-review-target-selector --model {model-partition} {gate-or-bundle}... --note {note-path} --json
```

An empty array means the requested pairs are fresh for that model partition.

## Do not

- Do not run the selector to choose gates before reviewing. This instruction is for explicit execution.
- Do not let the parent agent perform the review judgment when sub-agent delegation is available.
- Do not invoke retired manual review-writing commands; use `commonplace-ingest-bundle-output`.
- Do not skip a requested gate block in the bundle output.
- Do not ask sub-agents to run ingest or any other bookkeeping command.
- Do not combine multiple jobs into one output file.
