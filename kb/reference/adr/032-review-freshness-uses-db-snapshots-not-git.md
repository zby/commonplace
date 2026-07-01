---
description: "Review freshness is based on SQLite-owned note and gate snapshots, separated from Git and from review execution; the model-side review key is a frozen model_partition"
type: ../types/adr.md
tags: []
status: accepted
---

# 032-Review freshness uses DB snapshots, not Git

**Status:** accepted
**Date:** 2026-06-24

## Context

[ADR 010](./010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) made review state a scoped SQLite exception once review artifacts stopped behaving like authored markdown. [ADR 031](./031-review-state-uses-run-owned-review-pairs.md) then made the persistent unit of review work an invocation-owned note/gate pair.

Freshness still depended on Git. The selector compared current files to accepted Git-style SHAs, batch paths checked committed gate state, and diffs relied on repository history. That coupling was tolerable inside this repo, where operators share a disciplined commit workflow, but it is wrong for installed systems:

- users and agents may use Git in different ways, or not have the same commit cadence;
- requiring committed review gates makes review correctness depend on a source-control workflow outside the review subsystem;
- a local Git history is an awkward storage backend for "what exact input text was reviewed";
- batch execution and freshness state were still too entangled, making it harder to reuse freshness from another runner or future automation.

The model key also needed correction. The system currently stores and queries a `model_id`, but live agents cannot reliably know the exact model before a run. Exact model telemetry is often available only after execution, from logs. Mutating review identity after the run based on telemetry creates mutable keys and can move accepted state between partitions after the fact.

## Decision

Review freshness is owned by the review database, not by Git.

The database stores content snapshots for reviewed KB files. A new snapshot records the repo-relative path, the exact UTF-8 markdown text read from disk, and a SHA-256 over those stored bytes. The snapshot table is shared by note files and gate files; the note/gate distinction is the role of the foreign-key column that points to a snapshot. Review pairs reference the note and gate snapshots used for prompt rendering. Acceptance events reference the snapshots that were accepted. Snapshot text may later be garbage-collected only after the snapshot is no longer needed for current acceptance diffs or in-flight prompt rendering; the path and hash remain as the identity baseline.

Freshness compares the current filesystem text of the note and gate against the accepted snapshot hashes. Git commits, Git blob hashes, and committed-gate preconditions are not part of review correctness. Diffs, when shown, are a review UX over stored snapshot text and current file text; they are not a state dependency.

Freshness and execution are separate subsystem surfaces:

- freshness owns snapshots, accepted baselines, stale/missing selection, ack, and full-review acceptance;
- execution owns job creation, prompt rendering, batch grouping, finalization, and readable artifacts.

Execution may ask freshness which review pairs need attention and may record completed acceptance through freshness APIs. Freshness does not know about runners, prompt paths, packing, batch sizes, retries, or orchestration.

The review identity remains:

```text
note_path x gate_path x model_partition
```

`gate_path` is the repo-relative path of the gate markdown file. Existing `gate_id` storage is migrated to `gate_path`; a CLI or report may still display a shorthand such as `prose/source-residue`, but that shorthand is derived from the path and is not the freshness key. The gate note path is the gate identifier for freshness state.

`model_partition` replaces `model_id` as the architectural concept. It is a declared, frozen model-side freshness partition chosen at run creation. It may be exact when the caller knows the concrete model, or coarse when the caller only knows the harness/session class, such as `codex` or `claude-code`. It may later encode model-side parameters such as reasoning effort or temperature if the operator wants those to split freshness.

Freshness treats `model_partition` as opaque. A partition value may coincide with a runner or harness label, but freshness does not interpret it as a runner name.

Telemetry is evidence, not identity. Post-review model telemetry may be stored and inspected, and mismatches may warn, but telemetry must not re-key `review_jobs`, `review_pairs`, or `acceptance_events`.

This decision is the first concrete step toward a more universal lineage system, but the implementation remains current-review-only. The universal part is the shape: file-path inputs, DB-owned accepted baselines, a stable target partition, a selector that emits stale targets, and execution kept outside freshness state. It does not introduce a generic lineage schema, polymorphic input tables, package asset lineage, source/report lineage, or generic diff infrastructure.

## Consequences

Easier:

- Installed Commonplace review no longer requires users to commit notes and gates in the same way this repo does.
- Review freshness has one local source of truth: accepted DB snapshots versus current file contents.
- Prompt rendering and acceptance can refer to the exact text that was reviewed, closing races where a file changes between selection, prompt creation, and acceptance.
- Review rationale text remains a filesystem artifact. The database stores decisions and derives artifact paths instead of duplicating full review bodies.
- Review becomes the first lineage-backed file-input target kind: two KB file paths plus a model partition, not a review-only gate-id exception.
- Parent-dispatched workflows and future automation can share the same freshness selector without being encoded into freshness state.
- Model-side review partitions stop being mutable keys. A run is accepted under the partition the caller declared before execution.
- The schema uses the same name as the concept, avoiding an ambiguous era where `model_id` means "not necessarily a model id."
- Coarse live-agent partitions such as `codex` are honest: they say what the system knows before the run, instead of pretending to know a literal model id.

Harder / accepted costs:

- The review database stores duplicated note and gate text for accepted baselines, so it grows with review history. This is accepted because review state already crossed the SQLite boundary, and the stored text is what makes Git independence possible.
- Exact historical diffs are available only when the accepted snapshot text is retained. If old snapshot bodies are garbage-collected, freshness can still compare hashes but diff text may be unavailable.
- `model_partition` is less precise than `model_id` by name. That imprecision is deliberate: the value is a freshness partition, not necessarily a literal observed model.
- The current implementation is schema-current only. Old stores whose accepted baselines cannot be represented as DB-owned snapshots must be recreated; they do not provide valid freshness baselines.
- Review remains a scoped SQLite exception while authored notes, gates, instructions, and source material remain markdown files. The database stores operational review state and accepted baselines, not primary KB content.

---

Relevant Notes:

- [010-review state should move to sqlite once reviews leave git and accumulate operational metadata](./010-review-state-should-move-to-sqlite-once-reviews-leave-git-and.md) — supersedes: preserves the SQLite boundary but replaces Git-derived freshness baselines with DB-owned snapshots
- [031-review state uses run-owned review pairs](./031-review-state-uses-run-owned-review-pairs.md) — see-also: the pair storage model whose reviewed inputs now point at snapshots
- [033-honest review state behind a versioned migration substrate](./033-honest-review-run-state.md) — see-also: the next review-store refinement, adding queued state
- [035-review jobs finalize all-or-nothing with derived artifacts](./035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md) — extends: derives artifact paths and guards accepted evidence through completed jobs
- [030-Harness-facing seams: batch prepare/ingest endpoints and runner adapters](./030-harness-facing-seams-batch-endpoints-and-runner-adapters.md) — historical: an intermediate execution seam that remained a consumer of freshness rather than part of freshness state
- [storage](../storage-architecture.md) — part-of: the broader storage boundary for authored markdown, derived reports, and SQLite-backed review state
