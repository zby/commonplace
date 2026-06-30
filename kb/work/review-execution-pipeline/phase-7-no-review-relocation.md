# Phase 7: No review relocation

**Status: planned.** Phase 7 removes automatic review-state rekeying from note relocation flows.

## Purpose

Review identity is path-keyed. A moved note should need review under the new path rather than pretending old path-keyed evidence automatically transfers.

This simplifies relocation and avoids preserving a misleading review lineage when a move is paired with content change.

## Scope

In scope:

- remove review DB rekeying from relocation hooks;
- keep old path-keyed review history as historical evidence;
- make selector report the moved path as needing review unless separately reviewed;
- update relocation docs/tests to describe review state as not relocated.

Out of scope:

- adding a `review_targets` table;
- content-hash/event-log source-of-truth redesign;
- migrating historical records;
- changing file relocation behavior outside review state.

## Tests

- relocating a note does not mutate `review_pairs`;
- relocating a note does not mutate `acceptance_events`;
- selector reports the moved path as missing/stale review under the new path;
- old path-keyed review records remain queryable as historical rows;
- relocation command output warns or reports that review state was not moved if current UX needs that visibility.

## Done when

Phase 7 is done when relocation leaves review state untouched and review freshness for the moved path is established only by a new review or explicit later workflow.
