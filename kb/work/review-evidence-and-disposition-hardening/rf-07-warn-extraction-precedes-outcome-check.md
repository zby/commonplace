# RF-07 — Warning extraction precedes the canonical outcome check

**State:** fixed 2026-08-27  
**Repair shape:** small local bug fix  
**Severity:** high for contract correctness, low implementation cost

## Finding

`extract_warns()` extracts explicit `- warn:` items before it checks whether the
canonical outcome is `warn`. PASS- or FAIL-shaped result prose can therefore
produce actionable warning text even though the fix contract says the selector
consumes WARN pairs.

## Evidence

- [`extract_warns()`](../../../src/commonplace/review/warn_selector.py) returns
  actionable findings before its `outcome != "warn"` guard.
- [The fix procedure](../../instructions/fix-warnings/fix-review-warnings.md)
  specifies current baseline-backed WARN pairs.
- Direct execution observed PASS-shaped input returning an explicit warning; see
  [the evidence boundary](./evidence-boundary.md).

## Why it matters

The canonical outcome is supposed to determine whether a verdict enters the fix
queue. Letting prose override that field makes protocol state and operational
behavior disagree and can trigger work the reviewer explicitly classified as a
PASS or FAIL instead.

## Provisional repair direction

Return immediately when `outcome != "warn"`, before parsing findings. Keep any
future cross-outcome informational finding feature separate from the fix queue.

## Done when

- PASS and FAIL bodies containing `- warn:` produce no warn-selector entries.
- WARN retains explicit-finding, summary, and fallback behavior.
- A full stored-pair test exercises the scanner, not only the helper.

## Resolution

`extract_warns()` now returns before parsing result prose unless the canonical
outcome is `warn`. Parameterized regression tests cover PASS and FAIL at both
the helper boundary and through stored-pair scanning. The complete test suite
passes (`591 passed`).
