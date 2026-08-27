# RF-08 — Warning selection ignores live note staleness

**State:** open  
**Repair shape:** small policy decision and local patch  
**Severity:** medium

## Finding

Warn selection confirms that the current criterion still matches its baseline,
but it does not compare the live note with the accepted note snapshot. A warning
can therefore be queued after the note has changed enough to make the finding
obsolete or misleading.

## Evidence

- [`scan_reviews()`](../../../src/commonplace/review/warn_selector.py) loads the
  baseline and checks only `baseline_criterion_hash` against the live criterion.
- The general freshness selector already has the note comparison needed to
  classify the pair.

## Why it matters

The output is presented as actionable review text for the current note. Applying
a stale finding can undo a repair, address text that no longer exists, or cause
the fix agent to reinterpret the reviewer beyond its evidence.

## Provisional repair direction

Decide whether note-stale warnings should be suppressed or returned in a
separate explicitly stale advisory section. Do not silently present them as
current.

## Done when

- The selector's output distinguishes current-note findings from stale residue.
- A note-only edit has a specified, tested result.
- Criterion-stale and note-stale behavior use consistent terminology.
