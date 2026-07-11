# Candidate refactor inventory

This file is the decision ledger. The adopted semantics are expanded in
[state-model.md](./state-model.md); implementation names below are fixed unless
the target-schema pass exposes a contradiction with an invariant.

## Lexical alignment

| current surface | observed mismatch | candidate target | decision |
|---|---|---|---|
| CLI `grouping`; DB/API/manifest `packing` | One job axis has two names and the same values (`note`, `criterion`). | Use `grouping` throughout. | **Adopted.** The axis groups requested pairs into jobs; it does not describe prompt quality or a stored package. |
| catalog `bundle`; `bundle_output_path`, `bundle-output.md`, `bundle_artifact_dir`, `ParsedPairBundle` | `bundle` means both a gate-catalog lens and a job-output container. | Reserve `bundle` for the catalog; use `job_output_path`, `job-output.md`, `review_job_artifact_dir`, and `ParsedJobOutput` for execution. Consider `kb/reports/review-jobs/` as the artifact root. | **Adopted.** Use the proposed execution names and `kb/reports/review-jobs/`; `bundle` remains only the authored catalog lens. |
| `TYPE_GATE_LENS`, `COLLECTION_GATE_LENS`, `is_*_gate_request` | These helpers identify conformance criterion sources; the gate type is true but not the discriminating concept. | Use `TYPE_CONFORMANCE_LENS`, `COLLECTION_CONFORMANCE_LENS`, and `is_*_conformance_request`. | **Adopted.** Conformance is the behavior these helpers discriminate; the generic assay axis remains criterion. |

## Semantic alignment

| current surface | question to resolve | candidate options | decision |
|---|---|---|---|
| `acceptance`, `AcceptanceState`, `accepted_*`, `current_criterion_acceptances` | Does the row mean approval, or only the current snapshot-pinned freshness baseline? | Prefer `freshness_baselines`, `FreshnessBaseline`, and `baseline_*`; decide whether a current-state view is still useful. | **Adopted.** Use `freshness_baselines`, `FreshnessBaseline`, and `baseline_*`. Keep an enriched `current_freshness_baselines` query view over the current-state table and its evidence/snapshots. |
| `commonplace-ack-review`, acknowledgement APIs | Is “ack” sufficiently clear once the stored concept becomes a freshness baseline? | Keep the concise operator term and define it, or rename toward `carry-forward-review` / `advance-review-baseline`. | **Adopted.** Keep `ack` for the operator action and command. Baseline storage APIs use baseline vocabulary; acknowledgement APIs use `ack_*`. Ack advances an existing baseline without creating evidence or changing its evidence-pair identity. |
| pair `reviewed_at` | Is this a review timestamp or the completion fact shared by verdict and report protocols? | Prefer `pair_completed_at` (or `completed_at` where unambiguous). | **Adopted.** Use `completed_at` on the pair where its scope is explicit; qualify it as `pair_completed_at` only in a flattened surface that also exposes job completion. |
| `decision IN (pass, warn, fail, error)` | Is `ERROR` a substantive verdict, an inability to judge, or an execution failure? | Rename `decision` to `outcome`; or restrict verdicts to `pass/warn/fail` and represent inability/failure separately. Fix the worker result marker and finalization invariant accordingly. | **Adopted.** Rename the substantive field to `outcome`, restricted to `pass`, `warn`, or `fail` for verdict pairs. `ERROR` reports inability to produce a result and fails the all-or-nothing job; it never completes a pair or creates a baseline. |
| `missing-review` for absent acceptance and incomplete accepted snapshots | Are absence and corrupted/incomplete baseline state the same operator condition? | Split into `unreviewed` / `missing-baseline` and `baseline-incomplete`, or make incomplete baseline an integrity failure rather than a stale reason. | **Adopted.** No row is `missing-baseline`. A present but incomplete or inconsistent baseline is an integrity failure, not a stale reason. The remaining stale reasons are `note-changed` and `criterion-changed`. |

## Cross-cutting consequences to check

Every adopted choice must be traced through:

- `review-schema.sql`, schema version checks, indexes, and views;
- review DB row dataclasses, queries, pruning, acknowledgement, and finalization;
- selector reasons and model-agnostic coverage;
- protocol result markers, parser records, prompt instructions, and failure semantics;
- job creation/list/finalize/ack CLI JSON and text output;
- derived artifact directory, filenames, manifest fields, and result frontmatter;
- relocation and pruning behavior that derives artifact paths;
- the retained v5 store and its direct evidence-preservation route to the adopted target;
- tests, fixtures, helper names, current reference docs, instructions, and active vocabulary.

## Decisions that are already fixed

Do not reopen these without new evidence:

- `criterion_path` and `criterion_id` name the generic assay axis.
- `gate` names the closed-ended, verdict-kind criterion subset.
- authored gate metadata remains `gate_id` under `review-gates/`.
- `--all-gates` selects applicable verdict criteria and excludes report assays.
- `result_kind = verdict | report` separates persisted completion protocols.
- model-side freshness identity remains `model_partition`.
- freshness compares DB-owned snapshots rather than Git state.
- finalization is all-or-nothing per job.
