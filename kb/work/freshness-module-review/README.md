# Freshness module code review

Code review of `src/commonplace/freshness/` (~1250 lines, 11 modules) for bugs, inconsistencies, and overengineering. Requested 2026-07-14; findings in [findings.md](./findings.md).

The module was read in full against its callers (`review/review_db.py`, `review/acknowledgement.py`, `cli/freshness_*.py`), the schema (`src/commonplace/store-schema.sql`), and the live store (`kb/reports/commonplace-store.sqlite`, 262 baselines). All 18 tests in `tests/commonplace/freshness/` pass — every finding is latent rather than currently breaking.

## What closes this workshop

Each finding is either fixed, or written down as a design proposal (`kb/reference/proposals/`) if it needs a decision rather than a patch. The generic-accept question is the one that plausibly needs a decision; the rest are patches.

Whether any of this generalises into a note is an open question — the disabled-feature-left-in-tree pattern (finding 1) may be the only transferable one, and only if it recurs.
