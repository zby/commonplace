# Phase 6: Ack provenance

**Status: ready to implement.** Phase 6 removes review-less acceptance events from the write path by making ack carry forward an existing completed review pair. The first version keeps legacy nullable rows readable and defers the `NOT NULL` migration.

## Purpose

Ack means a previous completed review remains valid for the current note/gate snapshots. The acceptance event should point to the review evidence being carried forward.

The current nullable `accepted_review_pair_id` allowed ack rows to omit that provenance. Existing readers compensate by looking through null ack rows to the latest completed pair. This phase makes that implicit behavior explicit in stored data.

## Lookup rule

Ack lookup is path-keyed, not content-hash-keyed. To ack `(note_path, gate_path, model_partition)`, find the latest completed review pair for exactly those paths and that model partition. Since Phase 3 removes `review_pairs.model_partition`, this lookup joins `review_pairs` through `review_jobs` and filters on `review_jobs.model_partition`. Content hashes and snapshots are not used to choose the carried-forward review pair.

The ack event still captures current note/gate snapshots. Those snapshot IDs and hashes are the new freshness baseline, not the lookup key.

## Scope

In scope:

- change ack to find the existing completed review pair for `(note_path, gate_path, model_partition)`;
- update `ack_pairs` to call `load_latest_completed_review_pair(...)` and pass the returned `review_pair_id` to `append_acceptance_event`;
- update ack and accepted-review loaders so every same-model pair lookup gets model partition through the parent job, not from `review_pairs`;
- make multi-pair ack all-or-nothing: if any requested pair has no completed review to carry forward, write no acceptance events for any requested pair;
- normalize, dedupe, validate, and preflight every requested pair before snapshotting current note/gate text;
- store that pair id on the new acceptance event;
- keep accepted note/gate snapshot ids as the current snapshots at ack time;
- fail ack when no completed review pair exists;
- apply the same behavior through every public ack entry point: `commonplace-ack-gate-review`, `commonplace-ack-trivial-note-changes`, and `commonplace-review-target-selector --ack`;
- clean up the tests from testing obsolete or backcompat paths.

## Implementation contract

`ack_pairs` is the single write path for all public ack commands. It should:

1. Normalize the model partition and requested pairs.
2. Dedupe normalized `(note_path, gate_path)` pairs while preserving first occurrence.
3. Validate that every note and gate exists.
4. Preflight every pair by calling `load_latest_completed_review_pair(conn, note_path=..., gate_path=..., model_partition=...)`.
5. If any pair has no completed review, raise a clear error and write no snapshots or acceptance events for the batch.
6. After preflight succeeds, snapshot current note/gate text and append one acceptance event per pair, each with the carried-forward `accepted_review_pair_id`.
7. Commit the batch as one transaction.

This all-or-nothing rule matters because ack changes freshness baselines. A partially acked batch would leave operators with mixed current/stale state that did not correspond to one intentional decision.

Out of scope:

- backfilling existing null `accepted_review_pair_id` rows in the first version;
- making `accepted_review_pair_id` `NOT NULL` in the first version;
- removing read-through-to-latest fallback logic in the first version;
- adding a waiver/suppression workflow;
- changing review decisions;
- changing model partition identity;
- changing relocation behavior.

## Deferred hardening migration

After the first version has run with the stricter write path, a later hardening migration can remove legacy nulls:

1. For each null `accepted_review_pair_id`, compute the same latest completed pair that current readers would resolve for `(note_path, gate_path, model_partition)` by joining pairs through jobs.
2. Backfill the null with that pair id.
3. If any null row has no resolvable completed pair, stop and report `acceptance_event_id`, `note_path`, `gate_path`, and `model_partition`.
4. After all rows are resolved, rebuild `acceptance_events` with `accepted_review_pair_id INTEGER NOT NULL` and change the foreign key away from `ON DELETE SET NULL` to default `NO ACTION` / restrict-style semantics, so pruning cannot delete still-accepted review evidence.
5. Remove read-through fallback code only after the constraint holds.

The operator repairs unresolved rows by re-reviewing or explicit manual repair, then reruns the migration. This migration is intentionally deferred because it is data-integrity sensitive and not required to stop new review-less ack writes.

## Tests

- ack after a note-only trivial change carries forward the old review pair and new note snapshot;
- ack after gate-only accepted change carries forward the old review pair and new gate snapshot;
- ack with no completed review fails;
- multi-pair ack is all-or-nothing: one missing completed review writes no acceptance events for any requested pair;
- failed preflight writes no snapshots or acceptance events;
- ack lookup ignores content hashes and uses `(note_path, gate_path, model_partition)`;
- ack lookup joins `review_pairs` through `review_jobs` for model partition;
- duplicate requested pairs are deduped before writing acceptance events;
- legacy null ack rows remain readable through existing fallback logic;
- legacy null fallback logic also joins through jobs for model partition;
- warning selection can still load accepted review text;
- new ack writes have non-null `accepted_review_pair_id`;
- `commonplace-ack-gate-review` writes non-null `accepted_review_pair_id`;
- `commonplace-ack-trivial-note-changes` writes non-null `accepted_review_pair_id`;
- `commonplace-review-target-selector --ack` writes non-null `accepted_review_pair_id`.

## Done when

Phase 6 is done when every new ack acceptance from every public ack entry point points to review evidence, multi-pair ack is all-or-nothing, and ack fails without existing review evidence. Legacy null ack cleanup and the `NOT NULL` constraint are a later hardening step.
