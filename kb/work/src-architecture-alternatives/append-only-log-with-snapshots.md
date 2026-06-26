# Append-only log as source of truth, with acks that keep their snapshots

The active thread from [alternatives-survey.md](./alternatives-survey.md) Axis 1+3. Premise: make an append-only event log the review store's source of truth, demote SQLite to a rebuildable index over it.

## The snapshot rule

**An acceptance event must carry the exact note and gate bytes it accepted** (inline or via a content-addressed pointer it owns). It may not depend on Git, or on the working-tree file still being unchanged, to recover what was reviewed.

Why this is forced now, not optional:

- The previous review system leaned on Git as a retrieval store for committed files (`git show <commit>:<path>`, `git cat-file`). [ADR 032](../../reference/adr/032-review-freshness-uses-db-snapshots-not-git.md) removed that dependency.
- The dirty-file case already exposes the gap: a dirty baseline records a blob-shaped fingerprint but `git hash-object` (without `-w`) never stores the blob, so prior content is *not* retrievable. Committed and dirty baselines sit in the same fields and hide the difference.
- Once Git is gone as the oracle, the only thing that can answer "what bytes did this OK actually describe?" is the event itself. So the snapshot stops being an optimization and becomes part of the event's identity.

This is the difference between an edge and a cached value (the [files-vs-db-churn](../files-vs-db-churn/files-vs-db.md) framing): a verdict is a value derived over its inputs, so the inputs have to travel with it or it can't be trusted or recomputed.

Note: the current SQLite schema already does the right thing internally — `review_file_snapshots` holds `content_text`, and `acceptance_events` reference snapshot IDs. The work is preserving that self-sufficiency when the source of truth moves from a SQLite table (where a foreign key rehydrates the bytes) into a log line (where nothing rehydrates unless the event or a sibling artifact holds the bytes).

## Two ways to keep the bytes

1. **Inline** — each acceptance event embeds the full note and gate text.
   - simplest; one self-contained record.
   - cost: a gate accepted against 176 notes stores that gate's bytes 176 times; the log grows with content, not just events. The current payload tallies (`pure-file-review-store-design.md`: ~11.5 MB rationale, ~5.5 MB raw bundle) suggest this is tolerable but not free.

2. **Content-addressed blob store** (recommended) — events stay small and reference `blobs/<sha256>`; a sibling `blobs/` directory (sharded by hash prefix) holds each distinct note/gate text once.
   - automatic dedup: the gate's bytes are stored once regardless of how many notes it was run against; the note's bytes once per distinct version.
   - this is Git's own object model — we are replacing "lean on Git's object store" with "own a tiny content-addressed object store," which keeps the dedup property we were getting from Git for free while dropping the dependency.
   - the blob hash *is* the content key from Axis 3, so the same value does identity and retrieval.
   - cost: two artifacts (log + blobs) must stay consistent; blob GC needs a reachability pass from live events.

Recommendation: content-addressed blobs. It aligns the snapshot store with the content-key identity (Axis 3), keeps the log diffable and small, and dedups the gate-over-many-notes fan-out that is the worst case for inlining.

## What an acceptance event carries

Working sketch, to be refined:

- `accepted_at` — timestamp (provenance only, not identity)
- `model_partition` — model + reasoning effort
- `note_key` = `sha256(note_bytes)` → `blobs/<note_key>`
- `gate_key` = `sha256(gate_bytes)` → `blobs/<gate_key>`
- `note_path`, `gate_path` — display/retrieval handles, **not** identity (identity is the content keys)
- `decision`, `rationale` (or a `rationale_key` blob pointer if rationale markdown is large)
- `review_run` provenance pointer (which run produced it)

Staleness then is a pure inequality: recompute `sha256` of the current file, compare to the accepted `note_key`/`gate_key`. No diff-from-Git, no commit boundary.

## Does the log still earn itself? (separate the two decisions)

The "outside Git" decision forces a clean split between two things this thread had bundled:

1. **Git-decoupling (required).** Reviews must not depend on Git as a content oracle, and the store lives outside Git. **This is satisfied within the current SQLite-as-store design** — `review_file_snapshots.content_text` holds the reviewed bytes, freshness hashes canonical bytes with SHA-256, and selectors trust the stored snapshot text. That is exactly the [ADR 032](../../reference/adr/032-review-freshness-uses-db-snapshots-not-git.md) fix. It needs **no event log**.

2. **Event-log + derived index (optional refinement).** A separate bet, to be judged on its own merits now that Git-survivability is off the table. The reasons that survive being outside Git:
   - **Plain-text source of truth.** A JSONL log + `blobs/` is readable with `rg`/`grep` and writable by an agent without SQLite tooling — the llm-wiki "files as dual human/LLM interface" property, which a binary `.sqlite` source of truth gives up. (Holds even when gitignored.)
   - **Disposable, rebuildable index.** If the log is truth, a corrupt or schema-stale `.sqlite` is just deleted and rebuilt. With SQLite-as-store the blob *is* the truth — corruption is unrecoverable and schema changes are migrations, not rebuilds.
   - **Content-addressed ledger alignment (Axis 3).** Events reference `blobs/<sha256>`; identity = content hash. Falls out naturally from a log; bolted onto SQLite-as-store it's just more columns.

   Against: two artifacts (log + index) to keep consistent; SQLite-as-store is fewer moving parts and already exists.

So the workshop's first real decision is **#2 in isolation** — #1 is happening regardless. Don't let the log ride in on the Git-decoupling mandate; it has to win on plain-text-truth + rebuildable-index or it shouldn't displace the working SQLite store.

## Open questions

- **Log granularity.** One append-only JSONL for acceptances, or per-event files in a sharded tree? JSONL diffs and merges cleanly and is one open-fd append; per-event files avoid line-level merge conflicts but multiply inodes (`pure-file-review-store-design.md` has the filesystem numbers).
- **Where the log lives — DECIDED: outside Git.** Review state, including the new log and its blobs, stays out of Git (gitignored under `kb/reports/`, continuous with ADR-010's "reviews leave Git" and ADR-007's gitignored reports). This is coherent with the snapshot rule: the store depends on Git in *neither* direction — it doesn't read prior content from Git, and it isn't committed to Git. The log + blobs are a self-contained, local, rebuildable review store.

  Consequence to keep honest: with the store outside Git, "the SQLite blob churns Git" and "the log is Git-survivable/diffable" are both moot — neither is committed. Those were two of the stated reasons for preferring a log over SQLite-as-store; they no longer apply. The log must now justify itself on the reasons that survive — see *Does the log still earn itself?* below.
- **Index rebuild trigger.** On-demand (detect log newer than `.sqlite`), explicit `commonplace-*` command, or both. Must be deterministic so a dropped `.sqlite` is always recoverable.
- **Runs/pairs vs acceptances.** Acceptances are the durable ledger (Axis 3). Do `review_runs`/`review_pairs` also become log events, or stay as transient execution records that only the *accepted* outcome graduates into the log? Leaning: only acceptances are durable truth; runs/pairs are execution scaffolding that can live in the rebuildable index.
- **Migration.** Backfill events from the current SQLite store (its `content_text` snapshots are already self-sufficient), then make the log authoritative. This is now a follow-on migration after the ADR 032 snapshot cutover, not part of the Git-decoupling prerequisite.
</content>
