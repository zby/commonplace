# Report state

Local operational evidence and state. Payloads in this directory are ignored
because they are machine-local, not because they are safe to discard. Each
producer owns authority, integrity, and cleanup rules.

Current state includes:

- `commonplace-store.sqlite` — canonical freshness and review execution state;
- `review-jobs/`, `reviews/`, and `bundle-reviews/` — prompts, worker outputs,
  and retained judgment bodies;
- `review/` — `commonplace-review` result files, run directories, and each
  note's current full-pass packet under `review/packets/`;
- [`full-pass/`](./full-pass/README.md) — abandoned packets of the agent-run
  full pass, which nothing reads;
- `fixes/` — warning dispositions;
- `agentic-system-transfer/` — interest-conditioned transfer scans until every candidate is promoted, recorded as `no action`, or explicitly discarded;
- legacy review stores, backups, and revise-autoreason runs.

Do not delete this subtree as a cache. Follow the owning workflow's completion
or retirement rule for each payload class.

Agentic analysis now owns working runs under
`kb/agentic-systems/reports/state/`. Old ignored `agentic-system-analysis/`
directories remain recovery evidence under their original method; the layout
migration does not delete them or make unfinished runs resumable.
