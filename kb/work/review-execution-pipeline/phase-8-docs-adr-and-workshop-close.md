# Phase 8: Docs, ADR, and workshop close

**Status: ready to implement.** Phase 8 promotes the durable decisions and closes the workshop after the queued-job pipeline behavior has landed.

## Purpose

Turn the implementation into durable reference knowledge and remove workshop scaffolding that should not become a permanent navigation surface.

## Scope

In scope:

- promote [adr-draft-034-queued-review-jobs-and-execution-provenance.md](./adr-draft-034-queued-review-jobs-and-execution-provenance.md) into `kb/reference/adr/034-queued-review-jobs-and-execution-provenance.md`, unless another ADR has already taken 034;
- adjust the promoted ADR links so it supersedes-in-part ADR 031 and extends ADR 029, ADR 030, ADR 032, and ADR 033;
- update the concrete durable docs named below;
- audit that docs updated in earlier phases stayed current; command-surface changes should not wait until Phase 8 if agents need those docs during implementation;
- classify command wrappers as retired or retained convenience wrappers, then remove only wrappers that survived solely for removed command surfaces;
- clean up the tests from testing obsolete or backcompat paths;
- remove obsolete workshop files or promote remaining future-work designs to proposals;
- close the workshop by promoting durable artifacts and deleting the work folder if no active design remains.

Out of scope:

- changing implementation behavior;
- adding new queue features;
- adopting the model partition registry proposal;
- adopting the content-hash/event-log source-of-truth alternative.

## ADR handling

The ADR decision text lives in [adr-draft-034-queued-review-jobs-and-execution-provenance.md](./adr-draft-034-queued-review-jobs-and-execution-provenance.md). Phase 8 should move that draft into the reference collection after implementation and avoid duplicating ADR content in the phase plan.

Promotion mechanics:

1. Move the draft to `kb/reference/adr/034-queued-review-jobs-and-execution-provenance.md` if 034 is still the next available ADR number; otherwise use the next available number and update the filename/title accordingly.
2. Change frontmatter to the reference ADR shape: `type: ../types/adr.md` and `status: accepted`.
3. Change the title from `DRAFT 034-...` to `034-...`.
4. Keep the status line as `**Status:** accepted`.
5. Fix relative links from `../../reference/adr/...` to `./...`.
6. Fix the model partition registry proposal link to `../proposals/model-partition-registry.md`.
7. Preserve the ADR relationship labels: supersedes-in-part ADR 031; extends ADR 029, ADR 030, ADR 032, and ADR 033; defers the model partition registry proposal.
8. Delete the workshop draft after the promoted ADR validates.

## Documentation targets

Update or audit these live docs:

- `kb/reference/commands.md`;
- `kb/reference/REVIEW-SYSTEM.md`;
- `kb/reference/review-architecture.md`;
- `kb/reference/storage-architecture.md`;
- `kb/reference/README.md`;
- `kb/instructions/run-review-batches-on-note.md`;
- `kb/instructions/review-sweep.md`;
- `kb/work/review-execution-pipeline/README.md`.

Known stale statements to remove or correct:

- `review_pairs.model_partition` is not stored state; pair rows derive model partition through `review_jobs`;
- new ack writes do not use `accepted_review_pair_id = NULL`; ack carries forward an existing completed review pair;
- legacy nullable ack fallback remains only as a reader compatibility path until the hardening migration, not as current write behavior;
- `MANIFEST.json` is human/debug output and may be displayed or refreshed, but no pipeline command reads it as state;
- job creation is runner-agnostic and does not accept `--runner`;
- execution provenance (`runner`, `runner_model`, nullable `runner_effort`, optional telemetry) is set at claim/run time;
- orchestrator workers are file transducers from `prompt_path` to `bundle_output_path` and do not run `commonplace-*` commands;
- relocation does not rekey review state;
- retired prepare/ingest commands are not documented as current command surfaces.

## Command wrappers

Classify every review command exposed in `pyproject.toml` and the CLI docs before deleting anything.

Retire only wrappers that exist solely for removed command surfaces, such as old prepare/ingest/finalize-run compatibility commands if any remain.

Retain convenience commands that remain user-facing and compose the queued-job stages, provided their implementations are queue-backed and docs say they are convenience wrappers:

- `commonplace-review-sweep`;
- `commonplace-run-review-bundles`;
- `commonplace-run-gate-sweep`.

Verify that `pyproject.toml` entry points match the intended final command surface.

## Workshop closure

After the ADR and reference docs are promoted:

1. Delete phase plans and design sketches whose decisions are fully represented by the promoted ADR and durable docs.
2. Promote any remaining future-work design that should persist, such as registry or source-of-truth alternatives, to `kb/reference/proposals/`.
3. Keep `kb/work/review-execution-pipeline/` only if it has named active work and a trimmed README pointing only to that work.
4. Otherwise delete the workshop directory.

Do not leave workshop files as a shadow reference collection.

## Test cleanup boundary

Remove tests for obsolete command surfaces, removed compatibility shims, and backcompat paths that no longer exist.

Keep tests for deliberately supported legacy readers until their hardening migrations land. In particular, keep Phase 6 legacy nullable ack fallback tests until the deferred migration backfills old nulls, makes `accepted_review_pair_id` non-null, and removes the fallback.

## Tests and validation

- full `pytest`;
- `commonplace-validate` on updated docs;
- command reference examples match actual CLI flags;
- `pyproject.toml` command entry points match the intended current command surface;
- no live docs describe removed command surfaces as current;
- no live docs tell agents to pass `--runner` to `commonplace-create-review-jobs`, use `commonplace-prepare-review-batch`, use ingest commands for job-owned finalization, or treat `MANIFEST.json` as pipeline state;
- workshop README points only to remaining active work, or the workshop is deleted.

## Done when

Phase 8 is done when the shipped system is described in durable reference docs and ADRs, old command surfaces are no longer documented as current, and the workshop has either closed or been reduced to explicitly remaining future work.
