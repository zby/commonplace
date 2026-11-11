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
- `ingest/` — one working directory per ingest, holding its last drafting run: the handoff record with every handoff check and the run's outcome, and the candidate of an open or closed run. A record without an outcome marks a run that stopped midway. `commonplace-ingest-handoff prune` deletes published runs. Keeping finished runs is provisional: the records exist to decide whether the ingest skill keeps its repair round, and are dropped after that decision (see the [workshop case](../../work/decision-lifecycle-evidence/ingest-working-directory.md));
- `agentic-system-transfer/` — interest-conditioned transfer scans until every candidate is promoted, recorded as `no action`, or explicitly discarded;
- revise-autoreason runs.

Abandoned review data that nothing reads and that may be deleted:
`commonplace-store.sqlite` and its backups, `review-jobs/`, `reviews/`,
`bundle-reviews/` and `full-pass/`.

Do not delete this subtree as a cache. Follow the owning workflow's completion
or retirement rule for each payload class.

Agentic analysis now owns working runs under
`kb/agentic-systems/reports/state/`. The 96 run directories of the retired
method (`agentic-system-analysis/`, 2026-09-03 to 2026-10-01) were moved out of
the checkout on 2026-11-11 to `../commonplace-archive/kb/reports/state/`, after
deleting the source extractions three runs had made into their scratch
directories. Their outputs are in the tracked retained-archive; the runs were
never resumable under the current method.
