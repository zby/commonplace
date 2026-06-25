# Review snapshot and rationalization plan

This sequences two efforts that share one migration window:

1. the DB-owned snapshot design in [minimal-review-snapshot-design.md](./minimal-review-snapshot-design.md) — remove Git from review correctness and split freshness from execution;
2. a review-subsystem rationalization — drop write-only and dead state, rename the freshness partition concept from `model_id` to `model_partition`, and finish the migration abstraction.

They land together because both are schema migrations on the same store, and the cleanups are cheapest while the snapshot work already has the schema open. Scope stays current-review-only; nothing here touches the general lineage system.

## Guiding Principle

Store only what a selector, a command, or a human-read artifact consumes. Everything else is a file, or it is nothing.

One deliberate exception this cycle: `telemetry_json` is **kept** even though nothing reads it yet — it is retained for planned future use.

## Migration Window

Assume a stopped-operation migration window. While the migration runs, no review selectors, review creation, batch runs, finalization, ack commands, warning selection, or pruning jobs are active against the review database.

That assumption removes the need for mixed live behavior. The system does not need to keep selectors correct in an intermediate state where schema has snapshot columns but current accepted rows still carry only legacy Git-blob SHA fields. The migration can treat schema changes, data backfill, reader flip, and legacy-column removal as one offline cutover.

The remaining hard ordering rule is data preservation: consume the legacy SHA/commit fields before deleting them. During the window, read the legacy columns, backfill snapshots for every still-fresh current acceptance, update code and views to use snapshots, and then drop the legacy columns. Rows that cannot be backfilled because the current file no longer matches the legacy accepted hash become stale with diff unavailable.

Every schema change is still a versioned migration, so the migration runner (Prerequisite 2) must exist before the first `ALTER`.

Intermediate phases are implementation checkpoints, not supported production states. Keep `pytest` green at checkpoints, but do not add compatibility readers or dual-write paths only to support live operation during the migration.

## Prerequisites

- **Back up `review-store.sqlite`.** It holds ~10k pairs of irreplaceable acceptance history, and several steps are destructive (column drops, content GC). Copy the file first; this DB cannot be dropped and recreated.
- **Finish the migration abstraction.** `review_schema_migrations` exists but has no runner. Wire a minimal one: ordered, version-stamped, idempotent migrations applied at open; each stamps its version on success. Every schema change below is expressed as a numbered migration. This is the "finish the abstraction, don't leave it half-built" item — do it before any other schema change.
- **Preflight legacy gate IDs before schema changes.** List every distinct `gate_id` in `review_pairs` and `acceptance_events`, resolve it through the current gate catalog, and stop if any shorthand is unresolved. Current known offender: `structural/broken-link-path` is present in the existing review store but no longer has a gate file. Repair must be explicit before migration: restore/map the gate file, update legacy rows to a resolvable shorthand, or retire/delete the affected rows only under the backed-up, stopped-operation migration. Do not retain unresolved `gate_id` values as compatibility keys.
- **Verify "no readers" before each deletion.** The column and enum drops rest on grep evidence that nothing reads them after the migration step that consumes them. Run a confirming `rg` for each (`debug_log`, `raw_bundle_markdown`, `rationale_markdown`, `evidence_json`, legacy SHA/commit fields, the dead `acceptance_kind` values, `review_kind`) immediately before dropping it. For `raw_bundle_markdown`, first switch readers to `bundle_output_path`; for `rationale_markdown`, first switch readers to per-pair `result_path`.
- **VACUUM after the destructive phase.** The store is ~50% freelist (96 MB file, ~46 MB live). After the Phase 4 deletions and content GC, run `PRAGMA VACUUM` to compact it (roughly halves the file). Housekeeping, not correctness — run it last.

## Phase 0 — Foundations

The migration runner exists (Prerequisite 2). Add the snapshot schema. Because operation is stopped, this is an implementation checkpoint rather than a live mixed-schema state.

1. Migration: add role-neutral `review_file_snapshots` (content-addressed per path, `UNIQUE (path, content_sha256)`) for both notes and gates.
2. Migration: add nullable snapshot columns to `review_pairs` (`reviewed_note_snapshot_id`, `reviewed_gate_snapshot_id`) and `acceptance_events` (`accepted_note_snapshot_id`, `accepted_gate_snapshot_id`).
3. Migration: extend `current_gate_acceptances` to surface the accepted snapshot ids and their hashes for the new snapshot-only reader path.
4. Add `snapshot_file(repo_root, path) -> (snapshot_id, content_text, content_sha256)`: read file text, encode UTF-8, hash those exact bytes with SHA-256, insert-or-reuse the `(path, content_sha256)` row. Use the same helper for `note_path` and `gate_path`; the role is only the column that references the snapshot. This helper is a rehydrating upsert: if the matching row exists with `content_text IS NULL` because content GC reduced it to hash-only, update that same row with the newly read text before returning. The returned snapshot must have non-null text for prompt construction.

Checkpoint: schema applies through the runner; tests pass.

## Phase 1 — Review partition rationalization

Do this before the write path so new pairs and acceptances use the stable review-partition semantics.

5. **Rename identity columns.** The freshness key is `note_path x gate_path x model_partition`. Replace stored `gate_id` freshness columns with `gate_path` in `review_pairs`, `acceptance_events`, indexes, and current-acceptance views. Resolve existing `gate_id` values through the current gate catalog to repo-relative paths during migration; unresolved shorthands fail the migration or require manual repair, not a retained compatibility key. Human-facing protocols may still display a shorthand such as `prose/source-residue`, but freshness state stores the path. Rename the model concept and columns to `model_partition`: it is model-related but not necessarily a literal model. It is the declared partition under which a review is accepted. Today it may be an exact model string (`gpt-5.4-high`) or a coarse live-agent bucket (`codex`, `claude-code`). Later it may encode other model-side parameters such as temperature or reasoning effort. Use `model_partition` in new APIs, documentation, and DB columns; avoid `model_params` because the value is a declared partition string, not necessarily a literal structured parameter record. Rename the physical `model_id` columns in `review_runs`, `review_pairs`, `acceptance_events`, and current-acceptance views during this phase, in the same migration window as the semantic change.
6. **Immutable declared partition key.** Freeze the partition at run creation from the declared CLI value, and remove the telemetry-driven rewrite that previously rekeyed completed runs from post-run model telemetry. The declared value is the freshness partition. Telemetry may disagree; that should never move rows between partitions.
7. **No automatic effort dimension.** Do not append reasoning effort as a separate field. If the caller wants effort to affect freshness, the caller encodes it in the declared partition string. This avoids a mandatory re-key migration and avoids pretending we can infer the current live-agent effort before the run.
8. **Telemetry as evidence, not identity.** Keep `telemetry_json`. If telemetry reports a concrete model or reasoning effort after execution, store it there and optionally emit a warning when it differs from the declared partition. Do not mutate `review_runs`, `review_pairs`, or `acceptance_events` from telemetry.
9. **Alias repair stays separate.** Keep or retire `repair_model_partitions.py` only as a cleanup of known legacy aliases. It is not part of the snapshot migration, and there is no effort re-key migration in this plan.

Checkpoint: every creation path normalizes the declared partition string once, new code and DB schema use `model_partition` terminology, no path mutates the partition post-hoc, and tests pass.

## Phase 2 — Snapshot write path

Implement the post-migration write path. Operation is still stopped, so this is not a live cutover point. When operation resumes, every new review and ack populates snapshots and no new code writes legacy SHA or commit fields.

10. Extract a review freshness module owning selection, snapshot comparison, ack, and acceptance-event append. Dependency direction is set now: batch and runner code call the freshness module, never the reverse.
11. Review creation consumes selected or explicit pairs from the module, snapshots the note and gate through the same table/helper, stores both snapshot ids on `review_pairs`, and renders the prompt from the snapshotted text — not by rereading files. Full note text, stripped note body used for link extraction, stripped gate body, and gate metadata shown or recorded by the run are all derived from the snapshots. (Closes the create→render race.)
12. Finalization copies the accepted pair's snapshot ids onto the `full-review` acceptance event rather than re-snapshotting. (Closes the render→accept race.)
13. Ack snapshots the current note and gate through the module and references those ids on the acceptance event, with no accepted review pair.
14. **Storage shape.** Stop storing review text bodies in the DB. Store `review_runs.bundle_output_path` as a repo-relative pointer to the run's `bundle-output.md`, and store `review_pairs.result_path` as a repo-relative pointer to each per-pair result file. Move `debug_log` out of the DB to a `debug.log` file in the run dir. Drop `raw_bundle_markdown`, `rationale_markdown`, and `evidence_json` once readers use those paths. **Keep `telemetry_json` in the DB** (retained for planned future use).
15. **Ack qualification from snapshots.** `ack_trivial_note_changes` compares current note parts against `review_file_snapshots.content_text` for the accepted note snapshot. If the accepted snapshot text is unavailable, the pair is not auto-ackable. Remove the Git-history fallback from this path.
16. **Warn gate freshness from snapshots.** `warn_selector` compares current gate file SHA-256 values against the gate snapshot hash recorded on the effective review/acceptance. Warning candidates with unavailable gate snapshot baselines are skipped or reported as stale, but the command no longer calls `git hash-object` or requires committed gate files.
17. **Rationale text from result files.** `warn_selector` and any human-facing rationale display load review text from `review_pairs.result_path`. The DB keeps the parsed `decision` and the artifact path, not the rationale body. If the result file is missing, rationale text is unavailable; do not preserve `rationale_markdown` as a fallback.

Checkpoint: new reviews/acks carry snapshots in tests; new rows no longer depend on Git-blob SHAs or commit fields.

## Phase 3 — Backfill, flip, and drop legacy freshness columns

This is the offline cutover. It consumes the old accepted baselines, switches the system to snapshot-only freshness, and removes the legacy fields before operation resumes.

18. For every current acceptance row lacking snapshots:
    - compute the Git-style blob hash of the current note/gate content **in pure Python** (sha1 of `blob <len>\0` + bytes), without invoking Git;
    - if it matches the stored accepted SHA, snapshot the current note and gate through the same table/helper and attach the snapshot ids to the acceptance (and to the accepted pair where one exists);
    - if it does not match, leave the snapshot id null — the file changed since acceptance, so the pair genuinely needs attention.
19. Backfill `review_pairs.result_path` from the run artifact layout or from existing `MANIFEST.json` where available. Historical rows whose result file cannot be found keep null `result_path`; they remain audit rows but cannot provide rationale text.
20. Selector compares current SHA-256 against the accepted snapshot hash. Keep emitting `note-changed` / `gate-changed` / `missing-review` as reasons. For a row whose comparison needs a snapshot that is null (changed-since-acceptance during backfill), report `missing-review` with diff unavailable. After the legacy SHAs are dropped, those migrated rows lose note/gate change attribution because the system no longer has a valid accepted baseline to compare against; this is an accepted cost of the conservative backfill.
21. Diff code compares accepted-snapshot text against current filesystem text; where no snapshot exists the diff is unavailable but the pair is still reported.
22. Remove the Git-blob and committed-file calls from the selector, batch, gate-sweep, ack-qualification, and warn-selection paths, and remove the hard gate-commit precondition. Gates are now snapshotted by content like notes; no commit boundary is required for correctness.
23. Drop the legacy SHA and commit columns after the backfill has consumed them and code no longer reads them: `reviewed_note_sha`, `reviewed_note_commit`, `gate_sha`, `accepted_note_sha`, `accepted_note_commit`, `accepted_gate_sha`.

This reconstructs no historical versions. A changed-since-acceptance row has no valid accepted snapshot after the legacy columns are dropped, so it reports as needing attention with diff unavailable. Optional one-time tooling may import historical blobs from Git where available before the drop, but the migrated system must not depend on that path.

Checkpoint: every still-fresh current acceptance has a snapshot; no review path shells out to Git; legacy SHA/commit columns are gone; operation can resume on the snapshot-only system.

## Phase 4 — Cleanup and reclaim

Destructive. Runs after the backup (Prerequisite) and after the flip proves snapshots are authoritative. Each column/enum drop is its own migration, each preceded by a no-reader `rg`.

**Column and enum drops:**

24. Drop the `raw_bundle_markdown`, `rationale_markdown`, `evidence_json`, and `debug_log` content columns after readers have switched to `bundle_output_path`, `result_path`, and the run-dir `debug.log` file.
25. `acceptance_kind`: collapse the CHECK to the two produced values (`full-review`, `trivial-change-ack`); `gate-migration`, `migration-import`, and `manual-override` are unreachable. The distinction is also derivable from `accepted_review_pair_id` being NULL, so dropping the column entirely is defensible if no human-read artifact shows it — decide when touching the schema.
26. Drop `review_kind` (single value `'full-review'`).

**Filesystem:**

27. Delete the legacy `kb/reports/reviews/` tree (its README says it is not a runtime source of truth).
28. Stop writing `MANIFEST.json` — fully denormalized from DB rows, never read by live code. Run-dir filenames already encode the gate→result mapping, and `bundle_output_path` / `result_path` / `debug.log` remain for forensics.

**Snapshot content GC (drop full content for obsoleted reviews):**

29. `content_text` is only needed to diff an accepted baseline against the current file. Retain `content_text` only for snapshots reachable from a current acceptance (`current_gate_acceptances`) or referenced by a non-completed review pair (in-flight prompt render). For every other snapshot, null `content_text` but keep the row and its `content_sha256` (identity and dedup key). Fold this into `prune_superseded_reviews` so it runs with the existing cleanup. Future calls to `snapshot_file` must rehydrate a hash-only row when that same `(path, content_sha256)` is captured again.

**Reclaim:**

30. `PRAGMA VACUUM` (Prerequisite housekeeping) to compact the freelist.

Checkpoint: the schema carries only consumed state plus the retained `telemetry_json`; the DB file is compacted; tests pass.

## Acceptance Tests

Add explicit tests before treating the design as implemented:

- snapshot insertion de-duplicates on `(path, content_sha256)` and hashes exact UTF-8 bytes;
- snapshot insertion rehydrates an existing `(path, content_sha256)` row whose `content_text` was nulled by GC;
- selector works without a `.git` repository and does not call Git for note or gate freshness;
- dirty/uncommitted gate files are allowed because gates are snapshotted by content;
- review creation closes the create-render race by rendering from stored note and gate snapshots;
- prompt-derived inputs come from snapshots: full note text, stripped note body, link extraction, stripped gate body, and gate metadata shown or recorded by the run;
- finalization copies the accepted pair's note and gate snapshot IDs onto the acceptance event;
- trivial ack snapshots the current note and gate through the same snapshot table;
- trivial-change ack qualification uses accepted snapshot text and does not fall back to Git history;
- warn selection uses gate snapshot hashes and does not call Git for gate freshness;
- warn selection loads review text from `result_path`, not `rationale_markdown`;
- completed review pairs store `result_path`, and completed runs store `bundle_output_path`;
- migration preflight fails before schema mutation when a legacy `gate_id` cannot resolve to a current gate path;
- migration preserves still-fresh current acceptances and attaches the same snapshots to their accepted review pairs where such pairs exist;
- migration backfills `result_path` for historical pair artifacts where files exist;
- migrated changed-since-acceptance rows with missing snapshots report `missing-review` with diff unavailable;
- if both accepted snapshots exist and both current files changed, the selector preserves single-reason gate precedence by reporting `gate-changed`.

## What This Plan Leaves Alone

No change to batching, prompt packing, review parsing, warning selection, or pruning beyond the content-GC hook. The sweeps confirmed several things earn their keep and stay untouched: the two selectors (stale-pairs vs warn-findings — different output), both packing modes (note-packed and gate-packed both live), both runners (codex and claude-code both reachable; runner-specific telemetry justifies the adapter), and the stratified CLI surface.

The only structural change is the dependency direction: batch and runner code call freshness selection and acceptance APIs; freshness code never calls batch or runner code. It also does not decide how a future general lineage system represents sources, external repositories, generated reports, or package assets — that stays in [`kb/work/lineage-mechanisms/`](../lineage-mechanisms/general-lineage-refresh-state-design.md).
