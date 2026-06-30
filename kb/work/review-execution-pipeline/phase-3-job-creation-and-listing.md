# Phase 3: Job creation and listing

**Status: ready to implement.** Phase 3 starts after the mechanical run→job rename lands. It turns job creation into the public queued-job entry point while keeping execution and finalization behavior unchanged.

## Purpose

Make `commonplace-create-review-jobs` create queued review jobs from selector output, and add enough listing/plan loading support that operators and later commands can inspect what was created.

This phase completes the "create and inspect" half of the queued-job pipeline. It does not execute jobs and does not finalize output.

## Scope

In scope:

- stabilize `commonplace-review-target-selector --json` as an object-shaped public handoff into job creation, replacing the current bare array shape;
- require selector JSON used for job creation to carry a concrete top-level `model_partition`;
- require each selector target to carry both `gate_path` and `gate_id`;
- leave model-agnostic "missing under any model" coverage as a selector/reporting mode, not as input to job creation;
- extend `commonplace-create-review-jobs` beyond the Phase 2 renamed single-note command shape;
- accept selector JSON from `--input` or stdin;
- add a direct requested-pair input source that bypasses stale selection and creates jobs for requested pairs even when they are already fresh;
- support two grouping values, each choosing the partition axis and resolving to a persisted `packing`:
  - `note` -> one job per note/bundle group, `packing = note`;
  - `gate` -> one job per gate, chunking note targets by `--batch-size`, `packing = gate`;
- note grouping deliberately preserves the existing bundle-focused prompt split: same-note targets that span bundles create multiple note-packed jobs, not one merged note job;
- do not add an `explicit` grouping or `explicit` packing value; every input source must resolve through `--grouping note` or `--grouping gate`;
- remove `commonplace-prepare-review-batch` only after `commonplace-create-review-jobs` can express its direct same-axis pair inputs through those two grouping values;
- do not require or record a runner at creation time; runner choice belongs to later execution;
- make `review_jobs.runner` nullable execution provenance instead of creation-time intent;
- add nullable `runner_model` and `runner_effort` execution-provenance columns, but leave them null at job creation;
- adopt the v1 simplified model layout: drop `review_pairs.model_partition`, keeping `model_partition` on `review_jobs` and `acceptance_events`; a completed pair inherits its model through its job;
- land the readers and tooling the drop requires (the `latest_review_pairs` CTE, the pair index, `create_review_pairs`, `rekey_model_partition`, model-partition repair, and superseded-review pruning) in the same migration;
- introduce a shared `ReviewJobPlan` loader API used by job creation, listing, later finalization, and later subprocess execution;
- render prompt and manifest during creation;
- store DB-backed `prompt_path`, `bundle_output_path`, and per-pair `result_path`;
- keep per-pair result filenames short and axis-local: note-packed jobs name result files from the gate leaf, gate-packed jobs name result files from the note filename, and no v1 result filename combines note and gate names because persisted `packing` is always `note` or `gate`;
- keep `MANIFEST.json` as a written human/debug artifact, not pipeline state; do not put `manifest_path` or `artifact_dir` in the core job plan or DB schema;
- update the operational docs and instructions that agents follow in this phase, especially [run-review-batches-on-note.md](../../instructions/run-review-batches-on-note.md), [commands.md](../../reference/commands.md), [REVIEW-SYSTEM.md](../../reference/REVIEW-SYSTEM.md), and [review-architecture.md](../../reference/review-architecture.md), so they do not describe stale `--runner` creation flags or `commonplace-prepare-review-batch` as current;
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
commonplace-create-review-jobs --model {model-partition} --note kb/notes/example.md {bundle-or-gate...} --grouping note
commonplace-create-review-jobs --model {model-partition} --pair kb/notes/a.md::prose/source-residue --pair kb/notes/b.md::prose/source-residue --grouping gate
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
- it is an object with `targets`, not the current bare array;
- each target carries `note_path`, `gate_path`, `gate_id`, and `reason`;
- job creation rejects missing or null `model_partition`;
- model-agnostic selector output may still exist for coverage/reporting, but it is not a job-creation input in the first version.

Model-agnostic selector JSON uses the same object envelope with `"model_partition": null` and `targets`. It is valid selector/reporting output, but `commonplace-create-review-jobs` rejects it because queued jobs need a concrete freshness key.

`commonplace-create-review-jobs` always creates jobs under the selector's concrete `model_partition`. `--model` is optional and, when supplied, must match the input partition after normalization. Do not silently let a flag override a selector's declared concrete partition.

Direct requested-pair creation is an input source, not a grouping or packing mode. It preserves the current one-note QA workflow from [run-review-batches-on-note.md](../../instructions/run-review-batches-on-note.md): provided gates are the exact execution request, even if the selector would consider them fresh. It also replaces `commonplace-prepare-review-batch` by accepting `NOTE::GATE` pair inputs for same-axis batches. Those inputs still require `--grouping note` or `--grouping gate`; the stored `packing` remains only `note` or `gate`. The replacement preserves the ability to request explicit same-axis pairs, not `prepare_review_batch`'s incidental one-job cardinality for every same-note pair set: under `--grouping note`, cross-bundle same-note inputs split into one job per note/bundle group. Direct requested-pair input also requires `--model`, because there is no selector payload to supply the job's `model_partition`. The command still applies the existing applicability filter and reports skipped pairs, but it must not call stale selection to choose or omit requested gates.

### `commonplace-create-review-jobs` argument contract

`--grouping {note,gate}` is required in every mode. For `--grouping gate`, `--batch-size` limits the number of note targets per gate-packed job and defaults to 5. `--grouping note` does not use `--batch-size`; it groups gates by bundle/lens and does not chunk within a bundle in v1. Passing `--batch-size` with `--grouping note` is a CLI error.

The command has three mutually exclusive input modes. The table lists mode-specific flags only; `--grouping` is common to every mode, and `--batch-size` is a common option only when `--grouping gate`.

| Mode | Required | Optional | Forbidden |
|---|---|---|---|
| selector input | `--input PATH` / `--input -`, or no direct input flags and JSON on stdin | `--model` as a validation-only check | `--note`, `--pair`, positional gate/bundle arguments |
| direct note input | `--model`, `--note NOTE`, one or more gate/bundle arguments | none | `--input`, `--pair` |
| direct pair input | `--model`, one or more `--pair NOTE::GATE` flags | none | `--input`, `--note`, positional gate/bundle arguments |

Selector input reads the object-shaped selector JSON. `--input -` means stdin. If `--input`, `--note`, and `--pair` are all absent, the command reads selector JSON from stdin. A missing or mismatched model partition is an input error, not a successful no-op.

Direct note input accepts one note path plus gate IDs, full review-gate paths, or bundle names. Bundle names expand to gates before grouping.

Direct pair input accepts arbitrary same-axis or mixed note/gate pairs under either grouping. `NOTE` is a repo-relative note path. `GATE` may be a gate ID such as `prose/source-residue` or a repo-relative review-gate path such as `kb/instructions/review-gates/prose/source-residue.md`; bundle names are not valid inside `NOTE::GATE` because a pair names exactly one gate.

After normalization, duplicate `(note_path, gate_path)` pairs are dropped before grouping, preserving the first occurrence. Later duplicates are reported in `skipped_pairs` with `reason: "duplicate"`. Unknown notes, unknown gates, malformed `NOTE::GATE` values, invalid mode combinations, and invalid grouping values are CLI errors.

### JSON output contracts

`commonplace-create-review-jobs` prints one JSON object on successful creation or successful no-op:

```json
{
  "input_mode": "selector",
  "model_partition": "claude-opus-4-6",
  "grouping": "note",
  "created_count": 1,
  "skipped_count": 0,
  "jobs": [
    {
      "review_job_id": 42,
      "status": "queued",
      "model_partition": "claude-opus-4-6",
      "runner": null,
      "runner_model": null,
      "runner_effort": null,
      "packing": "note",
      "prompt_path": "kb/reports/bundle-reviews/review-job-42/prompt.md",
      "bundle_output_path": "kb/reports/bundle-reviews/review-job-42/bundle-output.md",
      "manifest_path": "kb/reports/bundle-reviews/review-job-42/MANIFEST.json",
      "pair_count": 1,
      "pairs": [
        {
          "review_pair_id": 101,
          "note_path": "kb/notes/example.md",
          "gate_path": "kb/instructions/review-gates/prose/source-residue.md",
          "gate_id": "prose/source-residue",
          "pair_ordinal": 1,
          "pair_status": "pending",
          "decision": null,
          "result_path": "kb/reports/bundle-reviews/review-job-42/source-residue.md"
        }
      ]
    }
  ],
  "skipped_pairs": []
}
```

`input_mode` is one of `selector`, `direct-note`, or `direct-pair`. `jobs` are sorted by `review_job_id`; pairs are sorted by `pair_ordinal`. `manifest_path` is a derived display/debug path, not stored pipeline state.

For newly created Phase 3 jobs, `prompt_path`, `bundle_output_path`, and each included `result_path` are non-null. `runner`, `runner_model`, and `runner_effort` are null until an execution path claims or dispatches the job. `decision` is null until finalization. `skipped_pairs` entries carry normalized `note_path`, `gate_path`, `gate_id` when available, and a `reason`.

A valid no-op, such as selector input with zero stale targets, exits 0 and uses the same shape with `created_count: 0`, `jobs: []`, and any duplicate or inapplicable valid inputs listed under `skipped_pairs`. Invalid input exits non-zero through the normal CLI error path and must not be represented as a successful empty `jobs` response.

A direct input whose pairs parse and resolve successfully but are all filtered out as inapplicable is also a valid no-op. It exits 0 with `created_count: 0`, `jobs: []`, and every inapplicable pair listed under `skipped_pairs`. This deliberately replaces `prepare_review_batch`'s old `no applicable pairs to prepare` failure at the public queued-job creation boundary. Unknown notes, unknown gates, malformed pairs, and invalid mode combinations remain CLI errors.

`commonplace-review-job-list --json` prints:

```json
{
  "filters": {
    "status": "queued",
    "model_partition": "claude-opus-4-6"
  },
  "count": 1,
  "jobs": [
    {
      "review_job_id": 42,
      "status": "queued",
      "model_partition": "claude-opus-4-6",
      "runner": null,
      "runner_model": null,
      "runner_effort": null,
      "packing": "note",
      "created_at": "2026-06-30T05:30:00+00:00",
      "started_at": null,
      "completed_at": null,
      "failure_reason": null,
      "prompt_path": "kb/reports/bundle-reviews/review-job-42/prompt.md",
      "bundle_output_path": "kb/reports/bundle-reviews/review-job-42/bundle-output.md",
      "manifest_path": "kb/reports/bundle-reviews/review-job-42/MANIFEST.json",
      "pair_count": 1,
      "pairs": [
        {
          "review_pair_id": 101,
          "note_path": "kb/notes/example.md",
          "gate_path": "kb/instructions/review-gates/prose/source-residue.md",
          "gate_id": "prose/source-residue",
          "pair_ordinal": 1,
          "pair_status": "pending",
          "decision": null,
          "result_path": "kb/reports/bundle-reviews/review-job-42/source-residue.md",
          "reviewed_at": null
        }
      ]
    }
  ]
}
```

JSON listing includes all pair rows for each job, including `pending`, `completed`, and `missing`. Jobs sort by `created_at ASC, review_job_id ASC`; pairs sort by `pair_ordinal ASC`. Table output may render a human age column, but JSON carries timestamps rather than a computed age.

In list JSON, `filters` always contains `status` and `model_partition`, each either a string or null. `runner`, `runner_model`, `runner_effort`, `started_at`, `completed_at`, `failure_reason`, `decision`, `result_path`, and `reviewed_at` are nullable. `prompt_path` and `bundle_output_path` are non-null for jobs created after this phase; migrated older rows may show null and are not executable until repaired or recreated.

## Schema change

Migration version 3 makes two coordinated changes on the existing v2 store.

**`review_jobs`:** change `runner` from `NOT NULL` to nullable execution provenance, add nullable concrete execution-provenance fields, and add `prompt_path`. The following are only the simple column additions; the final migration still rebuilds the table if `runner` needs its `NOT NULL` constraint relaxed:

```sql
-- runner is nullable because queued jobs are runner-agnostic until an execution phase claims or performs them.
ALTER TABLE review_jobs ADD COLUMN prompt_path TEXT;
ALTER TABLE review_jobs ADD COLUMN runner_model TEXT;
ALTER TABLE review_jobs ADD COLUMN runner_effort TEXT;
```

The final v3 `review_jobs` shape is:

```sql
review_jobs (
    review_job_id INTEGER PRIMARY KEY,
    model_partition TEXT NOT NULL,
    runner TEXT,
    runner_model TEXT,
    runner_effort TEXT,
    created_at TEXT NOT NULL,
    started_at TEXT,
    completed_at TEXT,
    status TEXT NOT NULL CHECK (status IN ('queued', 'running', 'completed', 'failed')),
    failure_reason TEXT,
    telemetry_json TEXT,
    prompt_path TEXT,
    bundle_output_path TEXT,
    packing TEXT NOT NULL CHECK (packing IN ('note', 'gate'))
)
```

SQLite cannot drop a `NOT NULL` constraint with a plain `ALTER TABLE`, and there is no generic rebuild helper today. Hand-code the `review_jobs` rebuild with the same discipline as the v1 `review_runs_new` migration: capture row counts, disable foreign keys around the swap, `BEGIN IMMEDIATE`, create the new table, `INSERT ... SELECT`, verify row counts, drop/rename, recreate indexes/views, set `user_version`, run foreign-key/schema integrity checks, roll back on error, and re-enable foreign keys in `finally`. Extract a small rebuild helper only if it preserves this exact discipline and is tested in the same phase. The fresh `review-schema.sql` model should carry short comments explaining that `runner` is the execution adapter/medium, while `runner_model` and `runner_effort` are nullable concrete execution provenance.

**`review_pairs` — the v1 simplified model layout:** drop `review_pairs.model_partition`. `model_partition` stays on `review_jobs` and `acceptance_events`; a completed pair inherits its model through its job. This is not a lone column drop — it must land with its readers and tooling in the same migration, or the store breaks:

- rebuild `review_pairs` without `model_partition` using the same hand-coded rebuild discipline as `review_jobs` (the column is indexed, so a plain `DROP COLUMN` is not used here), preserving the `acceptance_events.accepted_review_pair_id` foreign key;
- replace `idx_review_pairs_note_gate_model_partition` with `idx_review_pairs_note_gate` on `(note_path, gate_path)`; model filtering now joins through `review_jobs`;
- rewrite the `latest_review_pairs` CTE (`review_db.py`) to join `review_pairs` to `review_jobs` and `PARTITION BY rp.note_path, rp.gate_path, j.model_partition` instead of `rp.model_partition`;
- stop `create_review_pairs` from writing `model_partition`;
- drop `review_pairs` from `rekey_model_partition` and `count_model_partition_records`, which then update/count only `review_jobs` and `acceptance_events`;
- update `commonplace-repair-model-partitions` so partition discovery, dry-run reporting, write reporting, totals, and printed table counts no longer enumerate `review_pairs` as a model-partition table.
- update `commonplace-prune-superseded-reviews` so every same-model pair comparison joins `review_pairs` through `review_jobs` instead of reading `review_pairs.model_partition`; preserve its current acceptance-retention behavior, including nullable legacy ack rows that fall back to the latest completed pair for the same `(note_path, gate_path, model_partition)`.

Python row/API consequence: keep `ReviewPairRow.model_partition` in the first version, but make it a derived field supplied by loaders that join `review_pairs` to `review_jobs`. Every query feeding `_review_pair_from_row` must select `j.model_partition AS model_partition` (or an equivalent coalesced model partition for accepted/latest rows). Do not leave direct `SELECT rp.*` loaders that expect `review_pairs.model_partition` to exist. This keeps caller code stable while removing the physical duplication.

The fresh `review-schema.sql` omits `review_pairs.model_partition`.

`prompt_path` is stored on `review_jobs` in this phase. `bundle_output_path` already exists on `review_jobs`. `result_path` already lives on `review_pairs`. `manifest_path` and `artifact_dir` are not new DB columns and are not core `ReviewJobPlan` fields; derive them only for human/debug display if needed. No pipeline command should read `MANIFEST.json` as state. `acceptance_events.model_partition` stays — it is part of the acceptance freshness key `(note_path, gate_path, model_partition)`, even though completed pairs now inherit model through their job. `runner_model` and `runner_effort` are intentionally null at creation and are set only by execution/dispatch paths when known.

Per-pair result filenames are derived from the varying axis of the packed job. For `packing = note`, all pairs share one note and one bundle/lens, so result files use the gate leaf filename, such as `source-residue.md`. For `packing = gate`, all pairs share one gate, so result files use the note filename, disambiguating duplicate note basenames with encoded note paths only when needed. Do not keep or introduce a mixed fallback filename that combines note and gate names in v1; unsupported packing values should fail rather than produce long hybrid names.

## Shared job plan

Add a concrete loader API:

```python
def load_review_job_plan(
    conn: sqlite3.Connection,
    *,
    review_job_id: int,
    require_paths: bool = False,
) -> ReviewJobPlan | None: ...

def list_review_job_plans(
    conn: sqlite3.Connection,
    *,
    status: str | None = None,
    model_partition: str | None = None,
    require_paths: bool = False,
) -> list[ReviewJobPlan]: ...
```

`load_review_job_plan` returns `None` when the job id does not exist. `require_paths=False` is for listing and migration-tolerant inspection; it allows nullable `prompt_path`, `bundle_output_path`, and `result_path` on older rows. Later execution/finalization paths call with `require_paths=True` and fail with a clear error if a load-bearing path is missing.

The shared plan object contains:

- `review_job_id`;
- job row metadata: status, nullable runner, nullable runner model/effort, model partition, packing, artifact paths;
- all `ReviewPairRow` rows, including `pending`, `completed`, and `missing`;
- prompt path;
- bundle output path;
- per-pair result paths.

Do not let creation, listing, finalization, and runner code rediscover load-bearing artifact paths independently. `MANIFEST.json`, `manifest_path`, and `artifact_dir` are outside this object in v1 because the pipeline writes the manifest for inspection but does not read it back.

## Tests

- selector JSON used for job creation includes concrete top-level `model_partition`;
- selector JSON output is object-shaped, includes `targets`, includes per-target `gate_id`, and no longer emits the old bare array shape for `--json`;
- model-agnostic selector JSON uses `"model_partition": null`, and create jobs rejects it as job input;
- create jobs rejects selector JSON with missing or null `model_partition`;
- create jobs rejects a mismatched `--model`;
- create jobs accepts selector JSON from `--input PATH`, `--input -`, and stdin when no direct input flags are present;
- create jobs rejects mixed input modes, including `--input` with `--note`, `--input` with `--pair`, and `--note` with `--pair`;
- direct `--note` input without `--model` is rejected;
- direct `--pair` input without `--model` is rejected;
- direct `--pair NOTE::GATE` accepts gate IDs and full gate paths, but rejects bundle names and malformed pair syntax;
- direct arbitrary pairs work under both `--grouping note` and `--grouping gate`;
- duplicate normalized pairs are dropped before grouping and reported as skipped duplicates;
- selector input with zero targets succeeds with `created_count: 0` and `jobs: []`;
- direct note and direct pair inputs whose valid pairs are all inapplicable succeed with `created_count: 0`, `jobs: []`, and the inapplicable pairs in `skipped_pairs`;
- direct one-note creation reviews requested gates even when selector output would be empty because the pair is fresh;
- direct `NOTE::GATE` pair input can replace `commonplace-prepare-review-batch` for same-axis batches while still using `--grouping note` or `--grouping gate`;
- create jobs JSON output matches the documented success/no-op schema;
- create jobs stores null `runner`;
- create jobs stores null `runner_model` and `runner_effort`;
- create jobs stores DB-backed `prompt_path`, `bundle_output_path`, and per-pair `result_path`;
- per-pair result filenames are short and axis-local, with no note-plus-gate hybrid filename under v1 `note`/`gate` packing;
- create jobs writes `MANIFEST.json` for inspection but does not store `manifest_path` or `artifact_dir`;
- shared job-plan loading does not depend on reading `MANIFEST.json`;
- note grouping creates one job per note/bundle group;
- gate grouping chunks note targets by `--batch-size`;
- `--grouping note` rejects `--batch-size` and does not chunk same-bundle gates by count;
- a single-note input under `--grouping note` with all requested gates in one bundle yields exactly one job;
- a single-note input under `--grouping note` with requested gates spanning multiple bundles yields one note-packed job per bundle, not one merged job;
- a single-gate input under `--grouping gate` with target count no larger than `--batch-size` yields exactly one job;
- direct requested-pair input rejects any attempt to use an `explicit` grouping or persist `packing = explicit`;
- creation does not accept `--runner` or `--runner-model`;
- creation does not accept runner effort;
- all created jobs are `queued` with null runner provenance;
- `commonplace-prepare-review-batch` is gone;
- after migration v3, `review_pairs` has no `model_partition` column, and `idx_review_pairs_note_gate` replaces `idx_review_pairs_note_gate_model_partition`;
- effective-review/freshness queries return the same results with model joined through `review_jobs` as they did partitioning by `review_pairs.model_partition`;
- every `ReviewPairRow` loader still populates `model_partition` by joining through `review_jobs`;
- `rekey_model_partition` updates `review_jobs` and `acceptance_events` only, and end-to-end model rekey behavior is unchanged;
- `count_model_partition_records` counts `review_jobs` and `acceptance_events` only;
- `commonplace-repair-model-partitions` no longer queries, totals, or reports `review_pairs` as a model-partition table;
- `commonplace-prune-superseded-reviews` no longer reads `review_pairs.model_partition` and still retains the correct current pairs, including the nullable-ack fallback case;
- created pairs do not store `model_partition`; the job's `model_partition` is authoritative;
- inapplicable pairs are skipped consistently with existing prepare behavior;
- job list shows job id, status, prompt path, output path, pair count, packing, runner, model partition, age, and failure reason;
- job list JSON output matches the documented schema, includes all pair rows, and sorts jobs and pairs deterministically;
- `load_review_job_plan` returns all pair rows, tolerates nullable paths for listing, and rejects nullable load-bearing paths when `require_paths=True`;
- existing single-note live-agent workflow remains available through the new command shape;
- operational docs and instructions no longer tell agents to pass `--runner` to `commonplace-create-review-jobs` or to use `commonplace-prepare-review-batch` as a current command.

## Done when

Phase 3 is done when queued review jobs can be created from concrete model-specific selector JSON or direct requested pairs through `note` or `gate` grouping, inspected with `commonplace-review-job-list`, and loaded through one shared job-plan object; the v1 simplified model layout is in place (`review_pairs.model_partition` dropped, `ReviewPairRow.model_partition` populated through job joins, readers, pruning, repair, and `rekey_model_partition` updated); `commonplace-prepare-review-batch` is removed only after its direct same-axis pair workflow is covered by `commonplace-create-review-jobs` without adding `explicit` packing; the operational docs that agents follow have moved to the new command surface; and execution and finalization semantics are unchanged.
