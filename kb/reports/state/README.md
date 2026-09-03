# Report state

Local operational evidence and state. Payloads in this directory are ignored
because they are machine-local, not because they are safe to discard. Each
producer owns authority, integrity, and cleanup rules.

Current state includes:

- `commonplace-store.sqlite` — canonical freshness and review execution state;
- `review-jobs/`, `reviews/`, and `bundle-reviews/` — prompts, worker outputs,
  and retained judgment bodies;
- [`full-pass/`](./full-pass/README.md) — guarded captures and actionable pass
  dispositions;
- `fixes/` — warning dispositions;
- `agentic-system-analysis/<run-id>/` — checked phase state, frozen runtime
  baseline, immutable lens packets and returns, diagnostics, and validation
  receipt for one analysis. The analysis workflow owns cleanup. It may remove a
  handoff-ready run only after every declared exact-result consumer completes
  or is explicitly disposed and no unresolved transfer or projection state
  remains;
- `agentic-system-transfer/` — interest-conditioned transfer scans until every candidate is promoted, recorded as `no action`, or explicitly discarded;
- legacy review stores, backups, and revise-autoreason runs.

Do not delete this subtree as a cache. Follow the owning workflow's completion
or retirement rule for each payload class.
