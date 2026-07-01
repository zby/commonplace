# Phase 4 - public surface and closeout

## Position

Fourth phase. Revise this file after phase 3 lands; docs and ADR wording should describe the actual implemented behavior, not the initial forecast.

## Prerequisite

Phase 3 complete:

- derived paths are implemented
- finalization-time provenance is implemented with optional `commonplace-finalize-review-job --runner`, `--model`, and `--effort`
- `commonplace-claim-review-job` is removed
- job statuses are exactly `queued`, `completed`, and `failed`
- `review_pairs.pair_status` is removed; pair display status is computed from parent job status at render time
- `review_pairs.decision` stores only `pass`, `warn`, `fail`, or `error`; live `unknown` is gone
- all-or-nothing finalization is implemented
- strict live parsing accepts exactly one final `## Result: PASS|WARN|FAIL|ERROR` line per pair block
- `current_gate_acceptances` filters acceptance evidence through completed jobs with non-null pair decisions
- result-file write failures are fatal evidence failures; manifest refresh failures after DB completion are non-fatal finalize warnings
- review tests pass

## Purpose

Remove dead maintenance surface, update public documentation, record the architecture decision, and close the workshop with measured results.

## Tasks

### Dead Maintenance Surface

If phase 1 inventory confirms no current workflow depends on it, delete:

- `src/commonplace/cli/review/migrations/repair_model_partitions.py`
- related pyproject entry point
- related tests
- related command docs

If current review stores still need a one-time cleanup, document and run it before deletion, then remove the command.

### Documentation

Update:

- [review system](../../reference/REVIEW-SYSTEM.md)
- [review architecture](../../reference/review-architecture.md)
- [commands](../../reference/commands.md)
- [run review batches](../../instructions/run-review-batches.md)

Required doc changes:

- no mandatory claim step
- no claim command
- finalization-time provenance flags on `commonplace-finalize-review-job`: optional `--runner`, optional `--model`, optional `--effort` requiring `--model`
- status values `queued`, `completed`, and `failed`
- derived artifact paths
- no persisted path fields
- no persisted pair-status field
- decision enum `pass|warn|fail|error`; no live `unknown`
- all-or-nothing finalization
- strict live result footer
- result-file failure vs manifest-refresh warning behavior
- optional `warnings` array in finalize JSON
- `current_gate_acceptances` ignores events from non-completed jobs and pairs with null decisions
- schema-current policy for incompatible stores

### ADR

Write a superseding ADR for ADR 034, or amend it if repo convention permits amendments.

The ADR should cover:

- why queued/running/claim was reduced
- why artifact paths are derived
- why partial salvage was removed
- why strict live parsing replaces permissive inference
- why acceptance evidence is guarded by completed-job/non-null-decision view filtering
- why manifest refresh is non-fatal after DB completion while result-file writes remain fatal
- what remains deferred: selector/create consolidation, structured output, manifest retention

### Tests and Validation

- Update tests that assert public entry points.
- Run `pytest test/commonplace/review`.
- Run full `pytest`.
- Run `commonplace-validate` on touched KB docs.
- Run `rg "claim-review-job|running|pair_status|prompt_path|bundle_output_path|result_path|repair-model-partitions|partial salvage|missing pairs"` and verify remaining references are intentional historical notes or deferred discussion.
- Run a scoped `unknown` sweep over review decision/parser/schema/docs surfaces and remove live-decision leftovers. Ignore explicit model-placeholder uses such as `unknown-model` after verifying they are not decision values.

### Final Cleanup Gate

- Run the broad stale-name sweep from the tests section and remove every accidental leftover.
- Sweep stale reference surfaces beyond the main docs: `kb/reference/storage-architecture.md`, review proposals, and ADRs 029/030/031/033/034. Remove obsolete current-state claims or label them historical/superseded so agents do not treat claim/running/salvage as live.
- Remove stale workshop instructions that no longer match the implemented system.
- Delete tracked empty directories and obsolete fixtures created by earlier phases. Ignore untracked cache directories unless they interfere with validation or packaging.
- Ensure pyproject entry points, command docs, instruction docs, architecture docs, tests, and ADR all describe the same public surface, including no `pair_status` in job pair payloads and optional finalize `warnings`.
- If any old name remains for historical context, label it as historical in prose so later agents do not treat it as live.

### Workshop Closeout

- Record final production/test line counts against the baseline.
- Update this workshop with final deltas and any retained complexity.
- Extract durable conclusions into the correct library artifact if the implementation produced a reusable design insight.
- Remove or close this workshop according to `kb/work/COLLECTION.md` once durable artifacts exist.

## Expected Delta

Mostly documentation and ADR churn, plus possible repair-command deletion. The main production simplification already landed in phase 3.

## Phase 4 Implementation Notes

Implemented on 2026-07-01.

Public surface updated:

- `commonplace-repair-model-partitions` was deleted with its entry point, migration module, package marker, and dedicated test.
- `commonplace-claim-review-job` remains deleted and is asserted absent from public scripts.
- `commonplace-finalize-review-job` is the provenance boundary: optional `--runner`, optional `--model`, and `--effort` requiring `--model`.
- Public docs now describe statuses as `queued`, `completed`, and `failed`; decisions as `pass`, `warn`, `fail`, and `error`; artifact paths as derived; and finalization as all-or-nothing.
- ADR 035 records the current architecture and supersedes ADR 034 for claim/running, persisted paths, partial salvage, and permissive parsing.
- ADRs 029, 030, 031, 033, and 034 were updated so old claim/running/salvage language is historical or explicitly superseded.

Final measured deltas against the workshop baseline:

- Production review Python: **5,039 lines** across **31 files**, down from 5,345 lines across ~40 files (**-306 lines**, about **-5.7%**).
- Review tests: **4,054 lines** across **13 files**, down from 4,322 lines across 14 files (**-268 lines**, about **-6.2%**).

Retained complexity:

- `MANIFEST.json` remains as a display/debug artifact.
- Selector JSON followed by create jobs remains a two-command workflow.
- Strict markdown parsing remains the live codec; structured output is still deferred.

Stale-name sweep result:

- Remaining old names in `phase-1-*`, `phase-2-*`, `phase-3-*`, and the workshop plan are historical phase records, not live instructions.
- Remaining old names in ADRs 029, 030, 031, 033, and 034 are explicitly superseded by ADR 035.
- Remaining `claim-review-job`, `repair-model-partitions`, `started_at`, and `pair_status` hits in tests assert removed commands or removed DB columns are absent.
- Remaining `prompt_path`, `bundle_output_path`, and `result_path` hits describe derived paths, payload fields, manifest fields, or result-file frontmatter; they are not persisted DB fields.

Remaining follow-up:

- Decide whether selector/create consolidation is worth a new convenience command.
- Revisit `MANIFEST.json` retention or shrinking after more live use.
- Revisit a structured-output codec when a review-capable harness exposes schema-validated output at the right boundary.

## Verification

- `pytest`
- `commonplace-validate` on all touched KB docs
- `git diff --check`

## Exit Criteria

- Public docs describe the implemented workflow accurately.
- ADR captures the revised architecture.
- Dead repair/migration command is gone or explicitly justified.
- Final line deltas are recorded.
- Final cleanup gate is complete; stale names are either gone or explicitly historical/deferred.
- Workshop is either closed or left with a small explicit follow-up list.
