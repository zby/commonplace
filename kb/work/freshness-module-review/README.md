# Freshness module code review

Code review of `src/commonplace/freshness/` (~1250 lines, 11 modules) for bugs, inconsistencies, and overengineering. Requested 2026-07-14; findings in [findings.md](./findings.md).

The module was read in full against its callers (`review/review_db.py`, `review/acknowledgement.py`, `cli/freshness_*.py`), the schema (`src/commonplace/store-schema.sql`), and the live store (`kb/reports/state/commonplace-store.sqlite`, 262 baselines). The findings record that dated review. Finding 1 was resolved on 2026-08-19 by deleting the unusable generic accept command and transition under [ADR 065](../../reference/adr/065-publish-only-supported-freshness-transitions.md); the remaining findings are still open.

## What closes this workshop

Each remaining finding is either fixed, or written down as a design proposal (`kb/reference/proposals/`) if it needs a decision rather than a patch. The generic-accept question has been decided and removed; the rest are patches.

Whether any of this generalises into a note is an open question — the disabled-feature-left-in-tree pattern (finding 1) may be the only transferable one, and only if it recurs.
