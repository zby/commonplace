# Phase 4 - public surface and closeout

## Position

Fourth phase. Revise this file after phase 3 lands; docs and ADR wording should describe the actual implemented behavior, not the initial forecast.

## Prerequisite

Phase 3 complete:

- derived paths are implemented
- finalization-time provenance is implemented
- claim/running behavior is removed or explicitly retained with justification
- all-or-nothing finalization is implemented
- strict live parsing is implemented
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
- finalization-time provenance flags
- derived artifact paths
- no persisted path fields
- all-or-nothing finalization
- strict live result footer
- schema-current policy for incompatible stores

### ADR

Write a superseding ADR for ADR 034, or amend it if repo convention permits amendments.

The ADR should cover:

- why queued/running/claim was reduced
- why artifact paths are derived
- why partial salvage was removed
- why strict live parsing replaces permissive inference
- what remains deferred: selector/create consolidation, structured output, manifest retention

### Tests and Validation

- Update tests that assert public entry points.
- Run `pytest test/commonplace/review`.
- Run full `pytest`.
- Run `commonplace-validate` on touched KB docs.
- Run `rg "claim-review-job|running|prompt_path|bundle_output_path|result_path|repair-model-partitions"` and verify remaining references are intentional historical notes or deferred discussion.

### Final Cleanup Gate

- Run the broad stale-name sweep from the tests section and remove every accidental leftover.
- Remove stale workshop instructions that no longer match the implemented system.
- Delete empty directories and obsolete fixtures created by earlier phases.
- Ensure pyproject entry points, command docs, instruction docs, architecture docs, tests, and ADR all describe the same public surface.
- If any old name remains for historical context, label it as historical in prose so later agents do not treat it as live.

### Workshop Closeout

- Record final production/test line counts against the baseline.
- Update this workshop with final deltas and any retained complexity.
- Extract durable conclusions into the correct library artifact if the implementation produced a reusable design insight.
- Remove or close this workshop according to `kb/work/COLLECTION.md` once durable artifacts exist.

## Expected Delta

Around 100 production lines plus tests/docs if the repair command is deleted, plus documentation churn.

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
