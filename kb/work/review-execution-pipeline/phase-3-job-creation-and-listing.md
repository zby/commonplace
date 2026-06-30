# Phase 3: Job creation and listing

**Status: planned.** Phase 3 starts after the mechanical run→job rename lands. It turns job creation into the public queued-job entry point while keeping execution and finalization behavior unchanged.

## Purpose

Make `commonplace-create-review-jobs` create queued review jobs from selector output, and add enough listing/plan loading support that operators and later commands can inspect what was created.

This phase completes the "create and inspect" half of the queued-job pipeline. It does not execute jobs and does not finalize output.

## Scope

In scope:

- stabilize `commonplace-review-target-selector --json` as the public handoff into job creation;
- require selector JSON used for job creation to carry a concrete top-level `model_partition`;
- leave model-agnostic "missing under any model" coverage as a selector/reporting mode, not as input to job creation;
- extend `commonplace-create-review-jobs` beyond the Phase 2 renamed single-note command shape;
- accept selector JSON from `--input` or stdin;
- support two grouping values, each choosing the partition axis and resolving to a persisted `packing`:
  - `note` -> one job per note/bundle group, `packing = note`;
  - `gate` -> one job per gate, chunked by `--batch-size`, `packing = gate`;
- remove `commonplace-prepare-review-batch`; no dedicated `explicit` grouping is added, because its same-axis batches are already expressible — a single-note input under `--grouping note` and a single-gate input under `--grouping gate` each yield exactly one job, which is all `prepare_review_batch` ever produced (it already rejects anything that is not single-note or single-gate);
- do not require or record a runner at creation time; runner choice belongs to later execution;
- make `review_jobs.runner` nullable execution provenance instead of creation-time intent;
- do not add `runner_model`; the first version can pass `model_partition` to subprocess runners if they need a model argument;
- adopt the v1 simplified model layout: drop `review_pairs.model_partition`, keeping `model_partition` on `review_jobs` and `acceptance_events`; a completed pair inherits its model through its job;
- land the readers and tooling the drop requires (the `latest_review_pairs` CTE, the pair index, `create_review_pairs`, and `rekey_model_partition`) in the same migration;
- introduce a shared `ReviewJobPlan` / `PreparedReviewJob` loader used by job creation, listing, later finalization, and later subprocess execution;
- render prompt and manifest during creation;
- store/return `prompt_path`, `bundle_output_path`, and per-pair `result_path`;
- add `commonplace-review-job-list`.

Out of scope:

- finalizing job output;
- claiming jobs;
- running subprocess workers;
- writing `model_partition` into generated per-pair result frontmatter (that belongs to the finalization phase, which writes those files);
- changing ack semantics;
- removing old ingest commands.

## Command shape

```bash
commonplace-review-target-selector --json --model {model-partition} {bundle-or-gate...} --note kb/notes/example.md
commonplace-create-review-jobs --input targets.json --grouping note
commonplace-create-review-jobs --input targets.json --grouping gate --batch-size 5
commonplace-review-job-list --status queued --json
commonplace-review-job-list --model {model-partition}
```

Selector JSON:

```json
{
  "model_partition": "claude-opus-4-6",
  "targets": [
    {
      "note_path": "kb/notes/example.md",
      "gate_path": "kb/instructions/review-gates/prose/source-residue.md",
      "gate_id": "prose/source-residue",
      "reason": "missing-review"
    }
  ]
}
```

Selector JSON for job creation is model-specific:

- it carries a concrete top-level `model_partition`;
- job creation rejects missing or null `model_partition`;
- model-agnostic selector output may still exist for coverage/reporting, but it is not a job-creation input in the first version.

`commonplace-create-review-jobs` always creates jobs under the selector's concrete `model_partition`. `--model` is optional and, when supplied, must match the input partition after normalization. Do not silently let a flag override a selector's declared concrete partition.

## Schema change

Migration version 3 makes two coordinated changes on the existing v2 store.

**`review_jobs`:** change `runner` from `NOT NULL` to nullable execution provenance, and add `prompt_path`:

```sql
-- runner is nullable because queued jobs are runner-agnostic until an execution phase claims or performs them.
ALTER TABLE review_jobs ADD COLUMN prompt_path TEXT;
```

SQLite cannot drop a `NOT NULL` constraint with a plain `ALTER TABLE`, so use the existing migration rebuild helper for `review_jobs` if Phase 2 left `runner TEXT NOT NULL` in place. The fresh `review-schema.sql` model should carry a short comment beside nullable `runner` explaining that runner is execution provenance, not job-creation intent.

**`review_pairs` — the v1 simplified model layout:** drop `review_pairs.model_partition`. `model_partition` stays on `review_jobs` and `acceptance_events`; a completed pair inherits its model through its job. This is not a lone column drop — it must land with its readers and tooling in the same migration, or the store breaks:

- rebuild `review_pairs` without `model_partition` via the migration rebuild helper (the column is indexed, so a plain `DROP COLUMN` is not used here), preserving the `acceptance_events.accepted_review_pair_id` foreign key;
- replace `idx_review_pairs_note_gate_model_partition` with `idx_review_pairs_note_gate` on `(note_path, gate_path)`; model filtering now joins through `review_jobs`;
- rewrite the `latest_review_pairs` CTE (`review_db.py`) to join `review_pairs` to `review_jobs` and `PARTITION BY rp.note_path, rp.gate_path, j.model_partition` instead of `rp.model_partition`;
- stop `create_review_pairs` from writing `model_partition`;
- drop `review_pairs` from `rekey_model_partition`, which then updates only `review_jobs` and `acceptance_events`.

The fresh `review-schema.sql` omits `review_pairs.model_partition`.

`bundle_output_path` already exists. `result_path` already lives on `review_pairs`. `acceptance_events.model_partition` stays — it is part of the acceptance freshness key `(note_path, gate_path, model_partition)`, even though completed pairs now inherit model through their job. `runner_model` is intentionally absent from the first version; add it later only if persisted runner-model provenance becomes necessary.

## Shared job plan

The shared plan object should contain:

- `review_job_id`;
- job row metadata: status, nullable runner, model partition, packing, artifact paths;
- pending/completed `ReviewPairRow` rows;
- prompt path;
- bundle output path;
- per-pair result paths.

Do not let creation, listing, finalization, and runner code rediscover artifact paths independently.

## Tests

- selector JSON used for job creation includes concrete top-level `model_partition`;
- create jobs rejects selector JSON with missing or null `model_partition`;
- create jobs rejects a mismatched `--model`;
- create jobs stores null `runner`;
- create jobs stores `prompt_path` and `bundle_output_path`;
- note grouping creates one job per note/bundle group;
- gate grouping chunks by `--batch-size`;
- a single-note input under `--grouping note` and a single-gate input under `--grouping gate` each yield exactly one job (the former `prepare-review-batch` cases);
- creation does not accept `--runner` or `--runner-model`;
- all created jobs are `queued` with null runner provenance;
- `commonplace-prepare-review-batch` is gone;
- after migration v3, `review_pairs` has no `model_partition` column, and `idx_review_pairs_note_gate` replaces `idx_review_pairs_note_gate_model_partition`;
- effective-review/freshness queries return the same results with model joined through `review_jobs` as they did partitioning by `review_pairs.model_partition`;
- `rekey_model_partition` updates `review_jobs` and `acceptance_events` only, and end-to-end model rekey behavior is unchanged;
- created pairs do not store `model_partition`; the job's `model_partition` is authoritative;
- inapplicable pairs are skipped consistently with existing prepare behavior;
- job list shows job id, status, prompt path, output path, pair count, packing, runner, model partition, age, and failure reason;
- existing single-note live-agent workflow remains available through the new command shape.

## Done when

Phase 3 is done when queued review jobs can be created from concrete model-specific selector JSON through `note` or `gate` grouping, inspected with `commonplace-review-job-list`, and loaded through one shared job-plan object; the v1 simplified model layout is in place (`review_pairs.model_partition` dropped, model inherited through the job, readers and `rekey_model_partition` updated); `commonplace-prepare-review-batch` is removed (its same-axis batches expressed as single-group `note`/`gate` inputs); and execution and finalization semantics are unchanged.
