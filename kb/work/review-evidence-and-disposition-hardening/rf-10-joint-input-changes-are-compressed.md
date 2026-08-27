# RF-10 — Joint note and criterion changes are compressed to one reason

**State:** fixed 2026-08-27
**Repair shape:** selector payload and test change  
**Severity:** medium

## Finding

When both registered inputs changed, the review selector reports
`criterion-changed` because criterion comparison precedes note comparison in an
`if`/`elif`. Note diff generation then does not run. A caller can see one change
while the later acknowledgement transition accepts both live inputs.

## Evidence

- [`resolve_review_targets()`](../../../src/commonplace/review/review_target_selector.py)
  gives criterion change priority and emits a note diff only for
  `note-changed`.
- [`ack_pairs()`](../../../src/commonplace/review/acknowledgement.py) repins both
  current inputs.

## Why it matters

The selector output is the operator's candidate for acknowledgement. Hiding one
changed input lets the later transition extend old evidence across bytes the
operator was never prompted to inspect.

## Provisional repair direction

Represent changed inputs as a set or structured list rather than one priority
reason. Return enough old/new identity and diff information for the operator to
inspect every input that acknowledgement would advance.

## Done when

- A joint edit reports both `note` and `criterion` changes.
- Requested diffs are available for both applicable inputs.
- Existing single-change filtering remains expressible without hiding joint
  changes.
- Tests cover note-only, criterion-only, and joint edits.

## Resolution

Review selector records now carry a `reasons` tuple, the accepted baseline
revision, and role-labelled `changed_inputs` with accepted and current hashes.
JSON includes a diff on every changed input. A joint edit retains both note and
criterion observations, and `--reason` matches membership without removing the
other observation. Regression tests cover note-only, criterion-only, joint, and
both joint-filter views.
