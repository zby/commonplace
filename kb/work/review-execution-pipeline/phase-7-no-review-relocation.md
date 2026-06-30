# Phase 7: No review relocation

**Status: partially implemented.** The review relocation hook and review DB rekey helper API have been removed. Remaining work is to tighten verification around unchanged review rows, directory relocation, selector behavior, and stale tests/docs.

## Purpose

Review identity is path-keyed. A moved note should need review under the new path rather than pretending old path-keyed evidence automatically transfers.

This simplifies relocation and avoids preserving a misleading review lineage when a move is paired with content change.

## Scope

In scope:

- keep `commonplace-relocate-note` and `commonplace-relocate-directory` free of review-system hooks;
- do not keep a no-op review relocation hook;
- keep the review DB API free of note-path rekey helpers such as `count_note_path_records` and `rekey_note_path`;
- leave `review_jobs` rows and artifact paths untouched;
- leave `review_pairs` and `acceptance_events` rows untouched;
- keep old path-keyed review history as historical evidence;
- make selector report the moved path as needing review unless separately reviewed;
- update relocation docs/tests to describe review state as not relocated;
- clean up the tests from testing obsolete or backcompat paths.

## Implementation baseline

The first implementation slice removed:

- `ReviewRelocationHook`;
- `ReviewRelocationPlan`;
- relocation CLI imports and hook wiring;
- `NotePathUpdateCounts`;
- `count_note_path_records`;
- `rekey_note_path`;
- tests whose only purpose was to assert review-state rekeying.

Do not reintroduce those as compatibility shims. If a future workflow wants to relate old-path and new-path review history, it should be an explicit review-history or target-identity design, not automatic relocation rekeying.

Out of scope:

- adding a `review_targets` table;
- content-hash/event-log source-of-truth redesign;
- migrating historical records;
- changing file relocation behavior outside review state.

## Tests

- note relocation leaves `review_jobs`, `review_pairs`, and `acceptance_events` unchanged row-for-row, not just count-for-count;
- note relocation does not rewrite stored `prompt_path`, `bundle_output_path`, or per-pair `result_path`;
- directory relocation leaves `review_jobs`, `review_pairs`, and `acceptance_events` unchanged row-for-row for every moved markdown file;
- directory relocation does not rewrite stored prompt/output/result artifact paths;
- selector reports the moved path as missing/stale review under the new path;
- old path-keyed review records remain queryable as historical rows under the old path;
- relocation command output no longer reports review DB rekeys or review DB updates;
- tests do not assert legacy hook behavior, legacy rekey helper behavior, or backcompat with the removed review relocation API.

## Done when

Phase 7 is done when relocation leaves review state untouched and review freshness for the moved path is established only by a new review or explicit later workflow.
