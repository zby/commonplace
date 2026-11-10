# Report state

Local operational evidence and state. Payloads in this directory are ignored
because they are machine-local, not because they are safe to discard. Each
producer owns authority, integrity, and cleanup rules.

Current state includes:

- `review/` — `commonplace-review` state: `results/` holds one result file per
  reviewed (note, criterion) pair, `packets/` each note's current full-pass
  packet, and `runs/` one directory per review run with its call records and
  artifacts. See the [review system](../../reference/README-REVIEW-SYSTEM.md);
- `fixes/` — warning dispositions;
- `agentic-system-transfer/` — interest-conditioned transfer scans until every candidate is promoted, recorded as `no action`, or explicitly discarded;
- revise-autoreason runs.

Abandoned review data that nothing reads and that may be deleted:
`commonplace-store.sqlite` and its backups, `review-jobs/`, `reviews/`,
`bundle-reviews/` and `full-pass/`.

Do not delete this subtree as a cache. Follow the owning workflow's completion
or retirement rule for each payload class.

Agentic analysis now owns working runs under
`kb/agentic-systems/reports/state/`. Old ignored `agentic-system-analysis/`
directories remain recovery evidence under their original method; the layout
migration does not delete them or make unfinished runs resumable.
