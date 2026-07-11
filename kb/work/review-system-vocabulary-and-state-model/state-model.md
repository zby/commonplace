# Adopted review state model

This file fixes the semantic model before the target SQL and mechanical rename
pass. The model is independent of whether SQLite remains the source of truth or
becomes a derived index.

## Distinct facts

The subsystem records five different kinds of fact:

1. A **review job** groups requested pairs for one execution.
2. A **review pair** identifies one requested `(note, criterion)` assay.
3. Pair **completion** records that the pair produced the result required by
   its protocol.
4. A verdict **outcome** records a substantive `pass`, `warn`, or `fail`.
5. A **freshness baseline** records the input snapshots through which completed
   evidence remains applicable for one model partition.

Execution failure is not a sixth assay outcome. It is the inability of a job to
produce its contracted set of completed pair results.

## Job states

| state | required facts | forbidden facts | transitions |
|---|---|---|---|
| `queued` | creation time, grouping, model partition, requested pairs | job completion time, failure reason, pair completion, baselines produced by the job | to `completed` or `failed` |
| `completed` | job completion time; every requested pair is complete | failure reason, incomplete requested pairs | terminal |
| `failed` | job completion time and failure reason | pair completion and baselines produced by the failed attempt | terminal |

Finalization remains all-or-nothing. Parsing, provenance, coverage, protocol,
or artifact-write failure fails the job and leaves every requested pair
incomplete. The attempt may retain diagnostic output, but that output is not
completed assay evidence.

## Pair completion and result protocols

A requested pair begins incomplete: `completed_at` and `outcome` are null.
There is no persisted pair-level failed state under the all-or-nothing job
model.

| `result_kind` | completion marker accepted from worker | completed state |
|---|---|---|
| `verdict` | `PASS`, `WARN`, or `FAIL` | `completed_at` is set and `outcome` is `pass`, `warn`, or `fail` |
| `report` | `REPORT` | `completed_at` is set and `outcome` is null |

`ERROR` means the worker could not produce the contracted result. Encountering
it fails the job; it does not set pair completion, store an outcome, or create a
freshness baseline. Other malformed or missing completion markers have the same
state consequence.

The pair timestamp is named `completed_at`, not `reviewed_at`, because verdict
and report protocols share it. Flattened output that includes both job and pair
completion timestamps uses `pair_completed_at` and `job_completed_at` to avoid
ambiguity.

## Freshness baselines

There is at most one current freshness baseline for:

```text
(note_path, criterion_path, model_partition)
```

It records:

- `evidence_review_pair_id`: the completed pair that supplied the substantive
  verdict or report;
- `baseline_note_snapshot_id`: the latest note snapshot through which that
  evidence is considered applicable;
- `baseline_criterion_snapshot_id`: the latest criterion snapshot through
  which that evidence is considered applicable;
- `baseline_updated_at`: when the baseline was created or advanced.

Successful review finalization creates or replaces the baseline. Its baseline
snapshots initially equal the evidence pair's reviewed snapshots.

Acknowledgement is a separate operation over an existing baseline. It records
the operator claim that the same evidence remains applicable to current input
snapshots, so it advances one or both baseline snapshots and
`baseline_updated_at` while preserving `evidence_review_pair_id`. It creates no
job, pair, result, or new substantive evidence. The established CLI term
`commonplace-ack-review` remains.

This distinction is intentional:

- reviewed snapshots say what the assay actually evaluated;
- baseline snapshots say through which inputs that evidence remains fresh;
- the evidence pair says where the retained verdict or report originated.

## Freshness and integrity

The selector has three ordinary stale reasons:

| condition | result |
|---|---|
| no baseline exists for the selected key | `missing-baseline` |
| current criterion differs from the baseline criterion snapshot | `criterion-changed` |
| current note differs from the baseline note snapshot | `note-changed` |

A baseline is valid only when:

- its evidence pair exists and is complete;
- the evidence pair has the same note path and criterion path;
- the evidence pair's job has the same model partition;
- both baseline snapshot references are non-null and resolve;
- both referenced snapshots retain their source text and match the baseline
  paths.

Violation of any of these conditions is review-store corruption. Initialization
or the query boundary must raise an integrity error; selectors must not convert
it into `missing-baseline` or another actionable stale reason.

## Naming consequences

- Use `grouping`, not `packing`, for the job-construction axis.
- Reserve `bundle` for authored gate-catalog bundles; execution produces a job
  output under a review-job artifact directory.
- Use `outcome` only for substantive verdict values.
- Use `completed_at` for completion within a scoped job or pair record.
- Use `freshness_baseline`, `baseline_*`, and
  `current_freshness_baselines` for current freshness state.
- Keep `ack` as the name of the operator action that advances a baseline.
- Use `conformance` in helpers that distinguish type or collection conformance
  criteria.

## Storage sequencing

The source-of-truth decision in the neighboring
[src architecture alternatives](../src-architecture-alternatives/README.md)
workshop does not change these semantics. It does affect whether the target SQL
is canonical storage or a rebuildable projection. Fix that sequencing before
adopting the target SQL and preservation mechanism; do not make a second
SQLite-as-source-of-truth schema accidentally decide the neighboring question.
