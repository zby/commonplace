# Phase 6: Ack provenance

**Status: planned.** Phase 6 removes review-less acceptance events from the write path by making ack carry forward an existing completed review pair. The first version keeps legacy nullable rows readable and defers the `NOT NULL` migration.

## Purpose

Ack means a previous completed review remains valid for the current note/gate snapshots. The acceptance event should point to the review evidence being carried forward.

The current nullable `accepted_review_pair_id` allowed ack rows to omit that provenance. Existing readers compensate by looking through null ack rows to the latest completed pair. This phase makes that implicit behavior explicit in stored data.

## Lookup rule

Ack lookup is path-keyed, not content-hash-keyed. To ack `(note_path, gate_path, model_partition)`, find the latest completed review pair for exactly those paths and that model partition. Content hashes and snapshots are not used to choose the carried-forward review pair.

The ack event still captures current note/gate snapshots. Those snapshot IDs and hashes are the new freshness baseline, not the lookup key.

## Scope

In scope:

- change ack to find the existing completed review pair for `(note_path, gate_path, model_partition)`;
- store that pair id on the new acceptance event;
- keep accepted note/gate snapshot ids as the current snapshots at ack time;
- fail ack when no completed review pair exists.

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

1. For each null `accepted_review_pair_id`, compute the same latest completed pair that current readers would resolve for `(note_path, gate_path, model_partition)`.
2. Backfill the null with that pair id.
3. If any null row has no resolvable completed pair, stop and report `acceptance_event_id`, `note_path`, `gate_path`, and `model_partition`.
4. After all rows are resolved, rebuild `acceptance_events` with `accepted_review_pair_id INTEGER NOT NULL`.
5. Remove read-through fallback code only after the constraint holds.

The operator repairs unresolved rows by re-reviewing or explicit manual repair, then reruns the migration. This migration is intentionally deferred because it is data-integrity sensitive and not required to stop new review-less ack writes.

## Tests

- ack after a note-only trivial change carries forward the old review pair and new note snapshot;
- ack after gate-only accepted change carries forward the old review pair and new gate snapshot;
- ack with no completed review fails;
- ack lookup ignores content hashes and uses `(note_path, gate_path, model_partition)`;
- legacy null ack rows remain readable through existing fallback logic;
- warning selection can still load accepted review text;
- new ack writes have non-null `accepted_review_pair_id`.

## Done when

Phase 6 is done when every new ack acceptance points to review evidence and ack fails without existing review evidence. Legacy null ack cleanup and the `NOT NULL` constraint are a later hardening step.
