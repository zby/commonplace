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
- `agentic-system-analysis/<run-id>/` — one exact analysis result, temporary
  publication candidates, and minimal `running`/`complete`/`failed` state. A
  failed run is not resumed; a later run repeats it. The analysis workflow owns
  cleanup after the requesting operator has consumed or disposed the result;
- `agentic-system-transfer/` — interest-conditioned transfer scans until every candidate is promoted, recorded as `no action`, or explicitly discarded;
- legacy review stores, backups, and revise-autoreason runs.

Do not delete this subtree as a cache. Follow the owning workflow's completion
or retirement rule for each payload class.
