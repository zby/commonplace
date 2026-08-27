# RF-09 — Result prose is unbound mutable state

**State:** open  
**Repair shape:** storage/integrity design and migration  
**Severity:** high

## Finding

SQLite retains canonical outcome and completion state but not the result body or
its hash. The sole rationale/report copy is an ordinary derived Markdown file.
Warn selection trusts its current bytes and silently ignores a missing or
unreadable file.

## Evidence

- [`store-schema.sql`](../../../src/commonplace/store-schema.sql) has no result
  content or integrity field.
- [`write_pair_result_files_to_derived_paths()`](../../../src/commonplace/review/artifacts.py)
  writes plain files.
- [`_load_review_text()`](../../../src/commonplace/review/warn_selector.py)
  reads those files and returns `None` on any `OSError`.
- The tamper intervention in [the evidence boundary](./evidence-boundary.md)
  changed warning read-back while leaving the DB outcome unchanged.

## Why it matters

The prose that actually guides a fix has weaker integrity than the symbolic
outcome. Accidental editing, deletion, partial writes, or corruption can change
or erase disposition work without changing canonical review state.

## Provisional repair direction

Choose one canonical result-body substrate: store the body in SQLite, or retain
a mandatory content hash and verify the file before every read. Derived files
should be regenerable from canonical state. Missing or mismatched evidence must
be a health error, not an empty queue.

## Done when

- The canonical outcome and rationale cannot silently diverge.
- Store health reports missing, altered, or malformed result evidence.
- Warn/report consumers reject or visibly quarantine integrity failures.
- Migration behavior for existing result files is specified and tested.
