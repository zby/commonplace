---
description: "Architecture boundaries of the Commonplace review subsystem: parent-owned dispatch, canonical state, derived artifacts, atomic finalization, and freshness hashing"
type: kb/types/note.md
tags: []
---

# Review system architecture (`commonplace.review` + `commonplace.cli.review`)

The review subsystem is deterministic coordination around externally dispatched
judgment. Commonplace selects `(note, criterion)` pairs, snapshots their inputs,
creates jobs and prompts, validates worker output, and persists completion and
freshness. The parent agent or harness launches workers; Commonplace does not
launch reviewer models. The persisted generic assay field remains named
`criterion_path`.

For operation, see [the review-system guide](./README-REVIEW-SYSTEM.md) and
[run review batches](../instructions/run-review-batches.md). Exact behavior
belongs to the executing `commonplace.review` and `commonplace.cli.review`
source.

## Execution and ownership

```
target selector  -> selector JSON
job creation     -> queued job + pair rows + captured prompt
external worker  -> job-owned output file
finalization     -> parsed results + completion + freshness baselines
```

Ordinary review CLI job creation takes selector JSON. A job groups pairs by
note or by criterion for prompt sharing, but every pair remains an independent
unit of output and freshness, and every job uses one persisted result kind.

The agentic-analysis publication operation is the one specialized preparation
path. It may supply candidate note text while retaining the intended public
`note_path`. The ordinary pair still snapshots exactly note text and criterion
text, and finalization still creates the ordinary freshness baseline. Until the
candidate is published, that baseline is current for the candidate snapshot
and stale relative to the incumbent file.

The parent owns dispatch and concurrency. Each review worker starts without the
parent's task conversation, reads one generated prompt path, and writes only the
job-owned output named there. It does not mutate notes, criteria, manifests, or
the store. [ADR 067](./adr/067-review-workers-read-one-prompt-and-write-one-output.md)
owns that worker boundary; the generated prompt is its executable instance.

## Canonical state and artifacts

SQLite is canonical for job and pair protocol state, execution provenance, and
freshness. [Storage architecture](./storage-architecture.md) places that state
among Commonplace's other storage roles; live schema, location, and query
behavior remain in `commonplace.store` and `commonplace.review.review_db`.

Review artifacts have narrower roles:

- the prompt is generated job input carrying the captured review task;
- `job-output.md` is the worker-to-finalizer transport;
- per-pair result files retain the review body, which is evidence not stored in
  SQLite; and
- `MANIFEST.json` is a reconstructable inspection surface.

Artifact paths are derived from store state rather than persisted as another
authority. `MANIFEST.json` is never pipeline state. A worker's optional
self-reported model remains a labelled artifact claim; it does not become
harness provenance or freshness identity. Review identity is
`(note_path, criterion_path, model_partition)`; missing runner telemetry is
normal.

The output transport also carries one soft, per-pair report of which pre-resolved
linked artifacts the worker opened and whether budget or evidential sufficiency
stopped inspection. Finalization removes that bookkeeping from the retained
review body and joins it with code-generated available cost in job telemetry.
Missing, partial, malformed, or unpriced bookkeeping remains measurement state;
it cannot change a result, completion, freshness, or review identity.

## Finalization boundary

Finalization accepts only queued jobs and is all-or-nothing across every pair in
the job. It validates provenance, output structure, pair coverage, and each
pair's persisted result contract before advancing state. Success completes all
pairs, creates or replaces their freshness baselines, and prunes superseded
evidence. Failure completes none and advances no baseline. [ADR 035](./adr/035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md)
owns this transaction boundary.

The artifact failure policy follows the state boundary. A per-pair result-file
write failure prevents DB completion because that file carries review evidence.
A later manifest refresh failure is only a warning because the manifest is
reconstructable from completed state.

## Freshness hash boundary

A review baseline pins exactly two source files: the note and the persisted
criterion. The criterion may be a catalog gate, type spec, collection contract,
or critique instruction. Selector applicability and `missing-baseline`
discovery remain review-specific; registered-target status belongs to
[freshness architecture](./freshness-architecture.md).

Prompt scaffolding is deliberately outside the freshness hash. This includes
the worker instructions, output protocol, reading scope, prompt assembly, and
the mechanical wrappers that present type specs or collection contracts as
criteria. Therefore judgment-bearing particulars must live in the hashed note
or criterion files. A wrapper may say how to apply a dependency document,
never supply the case-specific judgment itself. A scaffolding change that shifts
judgments is a system upgrade requiring deliberate corpus-wide re-review or
acknowledgement rather than ordinary file-triggered staleness.

The live comments in
[`freshness.py`](../../src/commonplace/review/freshness.py) and
[`protocol/prompt.py`](../../src/commonplace/review/protocol/prompt.py) place
this rule in both change loops. [ADRs 038](./adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)
and [041](./adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md)
apply it to type and collection criteria.

Semantic gates may follow the target note's pre-resolved links. The linked
files are reading context, not freshness inputs. In particular,
`semantic/grounding-alignment` reads an ingest's append-only Quotes or an exact
snapshot declared by the link text. [ADR 073](./adr/073-untracked-source-snapshots-require-ingest-grounding.md)
owns that source-specific mutation and availability boundary; it does not
widen the review pair.

## Maintenance scope

Review this page when execution ownership, canonical-state roles, the
finalization transaction, or the two-file freshness boundary changes. Module
additions, function signatures, table columns, command arguments, and protocol
fields do not by themselves require an edit; their live owners remain source,
schema, or command help.

## See also

- [ADR 030](./adr/030-harness-facing-seams-batch-endpoints-and-runner-adapters.md) — parent-owned orchestration around deterministic endpoints
- [ADR 043](./adr/043-review-state-separates-completion-outcomes-and-freshness-baselines.md) — completion, outcome, and freshness are separate state dimensions
- [ADR 052](./adr/052-general-freshness-store-review-first-migration.md) — generic freshness store and review adapter boundary
