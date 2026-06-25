# Minimal review snapshot design

This is the first implementation step of the broader lineage mechanism, kept deliberately narrow so the general lineage workshop can use review as a clean precedent.

It covers only the current review subsystem. It has two goals:

1. remove Git from review correctness;
2. split freshness selection from batch/run execution.

Everything in this design is intentionally narrow. Review inputs are KB files identified by path. There are no generic input kinds, resolver types, lineage targets, or polymorphic event tables.

The part meant to generalize is the shape: a freshness target is keyed by file-path inputs plus a partition, the database owns accepted input snapshots, and execution consumes stale targets without being part of freshness state.

## Goal

Make review freshness self-contained in the review database.

Users and agents may still use Git however they want. The review system should not require:

- a Git checkout;
- committed notes;
- committed review gates;
- retained Git history;
- Git blob hashes as the version vocabulary.

The review database should contain enough information to know exactly what was reviewed and whether the current files still match the accepted baseline.

Also split review into two surfaces:

- freshness answers which `(note_path, gate_path, model_partition)` pairs need attention and why;
- execution decides which prompt, batch, runner, packing shape, or process should refresh those pairs.

## Non-Goals

Do not solve the general lineage system in this step.

Do not add:

- input kinds;
- resolver kinds;
- generic target tables;
- package asset lineage;
- external source lineage;
- polymorphic event input tables;
- general diff infrastructure.

Do not redesign runners, prompt protocol, parsing, warning selection, or pruning. The change is a boundary: batch commands consume stale pairs from freshness; freshness does not know how batches are run.

## Review Identity

Use file paths as the review input identities:

```text
note_path x gate_path x model_partition
```

`gate_path` is the repo-relative path of the gate markdown file, for example:

```text
kb/instructions/review-gates/prose/source-residue.md
```

Some current commands and reports may still accept or display a shorthand such as:

```text
prose/source-residue
```

That shorthand is derived from the path. It is not a separate identity dimension. Freshness code should resolve it to `gate_path` before reading or writing state.

The post-migration review store uses `gate_path`, not `gate_id`, in `review_pairs`, `acceptance_events`, current-acceptance views, indexes, and freshness APIs. Existing `gate_id` columns are migration inputs only: resolve each old shorthand through the current gate catalog to a repo-relative `gate_path`, then drop or rename the stored column so the final schema has no gate-id freshness key. If an old shorthand cannot be resolved, the stopped-operation migration should fail loudly or require manual repair before the legacy column is dropped; do not retain `gate_id` as a fallback freshness key. Human-facing protocols and reports may still display a shorthand field, but it is derived from `gate_path` and is not persisted as freshness identity.

One review pair has exactly two file inputs:

```text
note_path
gate_path
```

The input key is always the path. There is no input type field.

That makes review the first path-keyed lineage target kind rather than a special gate-id subsystem. Future target kinds can add typed inputs when they need them; this first step proves the file-input case.

`model_partition` is frozen at run creation from the declared CLI value. It can be exact when the caller knows the exact model, or coarse when the caller only knows the harness/session class, for example `codex` or `claude-code`. The name is intentionally model-related because the partition is about model-side review behavior, but it is not named `model_id` because it may later include temperature, reasoning effort, harness, or any other model-side parameter the operator wants to make freshness-distinct. It is also not `model_params`, because the value is a declared partition string, not necessarily a literal structured parameter record. Post-run telemetry is evidence only and must not re-key the review.

Freshness treats `model_partition` as an opaque string. A value may coincide with a runner or harness label such as `codex`, but freshness must not interpret it as a runner name or depend on runner semantics.

The migration should rename the physical review-state columns to `model_partition` in the same window as the semantic change. Keeping `model_id` in the schema while teaching the system that it is not necessarily a model id would preserve the confusion this change is meant to remove.

## Boundary

Freshness surface:

- stores reviewed note/gate snapshots;
- stores accepted baselines;
- reads current note/gate files;
- reports stale or missing `(note_path, gate_path, model_partition)` pairs;
- appends ack/full-review acceptance events;
- optionally produces diffs from stored snapshots.

Execution surface:

- decides how selected pairs are grouped;
- creates review runs;
- renders prompts;
- invokes runners or hands prompts to agents;
- ingests model output;
- writes readable review artifacts.

The freshness surface must not depend on `review_runs`, prompt paths, runner names, batch sizes, or packing. The execution surface may depend on freshness by asking for stale pairs and by accepting completed pairs.

## Snapshot Table

Add one table:

```sql
CREATE TABLE review_file_snapshots (
    snapshot_id INTEGER PRIMARY KEY,
    path TEXT NOT NULL,
    content_sha256 TEXT NOT NULL,
    content_text TEXT,
    captured_at TEXT NOT NULL,
    UNIQUE (path, content_sha256)
);
```

Rules:

- `path` is repo-relative and normalized with `/`.
- `content_text`, when present, is the exact UTF-8 markdown text read from disk.
- `content_sha256` is SHA-256 over the exact stored UTF-8 bytes.
- snapshots are content-addressed per path.
- the table is role-neutral: note files and gate files are stored identically.
- no Git commit, blob SHA, resolver type, input type, or provenance mode is required.

New snapshots store `content_text`. Later content GC may null it only for snapshots that are no longer reachable from current acceptances or in-flight review pairs; the hash and path remain the identity baseline.

Snapshot insertion must be a rehydrating upsert. `snapshot_review_file(path)` reads the current file text first, computes the SHA-256 from that exact UTF-8 text, and then inserts or reuses the `(path, content_sha256)` row. If the row already exists with `content_text IS NULL` because earlier GC reduced it to hash-only, the helper updates that row with the newly read text before returning. The helper must return the text it just read and must leave the returned snapshot row with non-null `content_text`, because prompt construction may immediately depend on it. Reusing a hash-only row without restoring text is a bug.

This table gives review a self-contained baseline. The note/gate role lives in the foreign-key column that points at a snapshot, not in the snapshot row itself.

## Review Pair Columns

Add snapshot references to `review_pairs`:

```sql
ALTER TABLE review_pairs ADD COLUMN reviewed_note_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id);
ALTER TABLE review_pairs ADD COLUMN reviewed_gate_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id);
ALTER TABLE review_pairs ADD COLUMN result_path TEXT;
```

For new rows these columns are required by application logic. Both columns reference the same snapshot table; there is no note-specific or gate-specific snapshot store.

The post-migration pair key is `(review_run_id, note_path, gate_path)`, and freshness indexes use `(note_path, gate_path, model_partition)`. The existing `gate_id` and `model_id` columns are not compatibility fields; they are renamed or replaced during migration.

`result_path` is the repo-relative path to the per-pair review artifact. It replaces DB storage of the review body. Commands that need the rationale text, such as warning selection or human display, load the file from `result_path` and may print it in full. The DB keeps the pair's decision and artifact pointer, not the pair's rationale body.

The legacy fields are migration inputs only:

```text
reviewed_note_sha
reviewed_note_commit
gate_sha
rationale_markdown
evidence_json
```

During migration, copy what can be reconstructed into snapshot references and artifact paths, then drop these columns. The final schema should not keep compatibility SHA, commit, rationale-body, or unused evidence-body fields.

## Acceptance Event Columns

Add snapshot references to `acceptance_events`:

```sql
ALTER TABLE acceptance_events ADD COLUMN accepted_note_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id);
ALTER TABLE acceptance_events ADD COLUMN accepted_gate_snapshot_id INTEGER REFERENCES review_file_snapshots(snapshot_id);
```

For full reviews, the acceptance event copies snapshot IDs from the accepted review pair. The copied note and gate snapshots remain rows in the same role-neutral table.

For trivial acks, the freshness layer snapshots the current note and current gate, then appends an acceptance event with those snapshot IDs and no accepted review pair.

The legacy fields are migration inputs only:

```text
accepted_note_sha
accepted_note_commit
accepted_gate_sha
```

During migration, copy still-fresh accepted baselines into snapshot references, then drop these columns. The final schema should not keep compatibility SHA or commit fields.

The post-migration acceptance key is `(note_path, gate_path, model_partition)`. As with review pairs, `gate_id` and `model_id` are migration inputs only.

## Hashing

Use SHA-256 over the exact stored UTF-8 bytes.

Do not use `git hash-object`.

The system may later decide to normalize line endings, but the minimal design should not hide transformations. Read file text, encode it as UTF-8, hash those bytes, and store the same text.

## Freshness API

Expose a small review-specific freshness API.

```text
select_review_pairs(note_paths, gate_paths, model_partition) -> list[ReviewRefreshTarget]
ack_review_pairs(targets) -> acceptance events
accept_review_pair(review_pair_id) -> acceptance event
snapshot_review_file(path) -> snapshot id + hash + text
```

`snapshot_review_file` is used for both `note_path` and `gate_path`. It does not receive or infer a role.

The returned text is the authoritative text for that capture. Callers that need prompt text, stripped note text, stripped gate text, or gate metadata use this returned text or load the same snapshot row; they do not reread the note or gate file after snapshotting.

`ReviewRefreshTarget` is still review-specific:

```text
note_path
gate_path
model_partition
reason
current_note_hash
accepted_note_hash
current_gate_hash
accepted_gate_hash
diff, optional
```

It must not include:

- review run ID;
- prompt path;
- runner;
- batch ID;
- packing mode;
- concurrency or retry hints.

## Execution Use

When creating a review run:

1. Get selected pairs from the freshness API, or accept explicit pairs from the caller.
2. Resolve `note_path` and `gate_path`.
3. If the caller used a gate shorthand, convert it to `gate_path` before creating freshness state.
4. Ask freshness to snapshot both files.
5. Create `review_pairs` with the note and gate snapshot IDs.
6. Render the prompt from the snapshotted text, not by rereading files.

That last rule prevents races. If a file changes while a review is running, the accepted review still refers to the exact input text sent to the model.

All prompt inputs derived from the reviewed note or gate must come from the snapshots. That includes the full note text, the frontmatter-stripped note body used for link extraction, the stripped gate body shown to the model, and gate metadata shown or recorded by the review run. Link parsing uses the note snapshot text; checking whether linked target files currently exist may still touch the filesystem, but prompt construction must not reread the reviewed note or gate after snapshotting.

When ingesting completed output:

1. Complete `review_pairs` as today.
2. Write the per-pair result files and store each pair's `result_path`.
3. For every completed accepted pair, ask freshness to append an acceptance event.
4. The acceptance event references the same note and gate snapshots as the accepted pair.

When acknowledging trivial changes:

1. Freshness reads the current note file and gate file.
2. Freshness inserts or reuses snapshots for both files.
3. Freshness appends an acceptance event with those snapshot IDs.

No command needs to check Git status.

Trivial-change qualification must also use snapshot-owned baselines. The old ack helper compared current note parts against text recovered from Git provenance. After this migration, it loads the accepted note snapshot text from `review_file_snapshots.content_text`, compares it with the current note file, and declines to auto-ack if the accepted snapshot text is unavailable. It must not fall back to Git history or Git blob text.

Warn selection must also stop using Git for gate freshness. When deciding whether a warning-bearing review is stale because its gate changed, it compares the current gate file's SHA-256 with the reviewed or accepted gate snapshot hash. It should skip or mark stale warning candidates whose required gate snapshot is unavailable, but it must not compute `git hash-object` or require committed gate files.

Warn selection must also stop reading review text from `review_pairs.rationale_markdown`. It loads the pair's `result_path`, parses the review text from that file, and reports the artifact path with the warning entry. If the file is missing, the warning text is unavailable; the DB should not retain a hidden rationale fallback.

## Freshness Internals

For each `(note_path, gate_path, model_partition)`:

1. Find the current acceptance event.
2. Load `accepted_note_snapshot_id` and `accepted_gate_snapshot_id`.
3. Read the current note file and gate file.
4. Hash both with SHA-256.
5. Compare current hashes with the hashes on the accepted snapshots.

Reasons:

| condition | reason |
|---|---|
| no current acceptance | `missing-review` |
| note snapshot missing on current acceptance | `missing-review` with diff unavailable |
| gate snapshot missing on current acceptance | `missing-review` with diff unavailable |
| current note and gate hashes both differ | `gate-changed` |
| current note hash differs | `note-changed` |
| current gate hash differs | `gate-changed` |
| both match | fresh |

The selector keeps one public reason per target. Missing accepted snapshots take precedence over hash comparisons and report `missing-review`. When both current note and gate hashes differ, preserve the current single-reason behavior by reporting `gate-changed`; do not introduce multi-reason output in this migration. Migration tooling may log that a baseline snapshot is unavailable, but selector output should not add a public `baseline-unavailable` reason.

## Diffs

Diffing is review UX, not freshness.

But this design makes review diffs independent of Git:

- previous note or gate text comes from `review_file_snapshots.content_text`;
- current note or gate text comes from the filesystem;
- the diff is ordinary text diff over whichever role changed.

Because only the accepted baseline is ever diffed against the current file, `content_text` is required only for snapshots reachable from a current acceptance. Snapshots that obsoleted reviews left behind can be reduced to hash-only — keep the row and `content_sha256` for identity and dedup, drop the text. The plan's content-GC step does this in `prune_superseded_reviews`.

If no snapshot exists because the row is old and unmigrated, the diff is unavailable. The selector can still report the target as needing attention.

## Current View

The existing `current_gate_acceptances` view can be kept and extended:

```text
accepted_note_snapshot_id
accepted_gate_snapshot_id
accepted_note_hash
accepted_gate_hash
```

The old SHA columns are not part of the post-migration view. They are read during the migration, copied into snapshot references where possible, and then dropped.

The public selector output does not need to mention snapshots. It still reports:

```text
note_path
gate_path
reason
diff, optionally
```

## Migration

Migration can be conservative.

For existing current acceptance rows:

1. Preflight every distinct legacy `gate_id` in `review_pairs` and `acceptance_events` against the current gate catalog. Every legacy shorthand must resolve to exactly one repo-relative `gate_path`.
2. If any legacy `gate_id` cannot be resolved, stop before changing schema. Manual repair must either restore/map the gate file, update the legacy rows to a resolvable shorthand, or explicitly retire/delete those rows under a backed-up, operator-approved migration. Do not carry the unresolved shorthand into the post-migration schema.
3. Compute the old Git-style blob hash for the current note/gate content in Python, without invoking Git.
4. If both current hashes match the stored accepted hashes, snapshot the current note and gate and attach those snapshots to the acceptance.
5. If the current acceptance points at an accepted review pair, attach the same snapshot IDs to that accepted pair.
6. If either current hash does not match, leave the relevant snapshot id null and let the selector report the pair as `missing-review` with diff unavailable.
7. Backfill `review_pairs.result_path` from the existing run artifact layout or `MANIFEST.json` where available. If a historical pair's per-pair artifact cannot be found, keep the row as audit history with null `result_path`; it cannot supply rationale text through the DB.
8. Drop the legacy SHA, commit, rationale, and evidence columns after backfill. Rows that could not be snapshotted keep their historical event record, but no longer provide a valid freshness baseline.

This preserves fresh current rows without requiring Git. It does not try to reconstruct old file versions.

Only current acceptances and the accepted pairs they point to are backfilled. Historical review pairs that are not referenced by a current acceptance may keep null snapshot references after the legacy columns are dropped; they are audit history, not freshness baselines.

The conservative backfill loses note/gate change attribution for changed-since-acceptance migrated rows. Once the legacy SHAs are dropped, a row with a missing accepted snapshot can no longer prove which input moved, so the selector collapses it to `missing-review` rather than `note-changed` or `gate-changed`.

Optional one-time tooling may use Git to import historical old blobs when available, but the migrated review system must not depend on that path.

New reviews and acks should use snapshots immediately after the schema lands and should never write the legacy SHA/commit columns. New completed reviews should write per-pair result files and store `result_path` instead of `rationale_markdown` or `evidence_json`.

## Storage Estimate

Current data suggests the extra DB storage is acceptable.

From the current review DB:

| measure | value |
|---|---:|
| review pairs | 10,479 |
| distinct reviewed note blobs retrievable from Git | 594 |
| distinct reviewed gate blobs retrievable from Git | 131 |
| known unique note+gate text | about 7.3 MB |
| known naive per-pair note+gate text | about 90 MB |
| current review DB file | 96 MB decimal / 92 MiB on disk |
| current review DB live pages after freelist | about 46 MB decimal |

The numbers are approximate because some old hashes are not retrievable from Git. The file/live split is because the current SQLite file has a large freelist; the migration plan's final `VACUUM` reclaims that space. That uncertainty strengthens the case for DB-owned snapshots.

With `(path, content_sha256)` de-duplication, input snapshots should add modest storage at current scale. Even a naive design would not be catastrophic, but de-duplication is easy enough to include.

## Implementation Plan

The sequenced steps live in [review-snapshot-and-rationalization-plan.md](./review-snapshot-and-rationalization-plan.md), which also folds in the review-subsystem rationalization (dead-state cleanup, immutable declared `model_partition`, finished migration runner). That plan assumes a stopped-operation migration window. The system does not need live compatibility between legacy SHA fields and snapshot fields; it only needs to consume the legacy fields for backfill before dropping them.

## What This Leaves Alone

This does not redesign batching, runners, prompt packing, review parsing, warning selection, or pruning.

It does change dependency direction. Batch and runner code should call freshness selection and acceptance APIs. Freshness code should not call batch or runner code.

It also does not decide how a future general lineage system should represent sources, external repositories, generated reports, or package assets. This is a minimal review repair.
