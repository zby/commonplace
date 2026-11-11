# Report state

Operational state of Commonplace workflows. The main repository ignores every
payload here to keep it out of the library's record: a failed candidate would
look like an ingest to search, presence in the main tree would read as
endorsement, and every run would dirty the tree and mix with library history.
Being ignored does not make the material disposable or local to one machine.
Each producing workflow owns authority, integrity and cleanup for its
directory; Git ignore status never licenses deletion. The
[reports collection](../COLLECTION.md) sets the class rules.

## What a reader should assume

Everything here is unreviewed model output or workflow bookkeeping, kept so
that work can continue and be inspected. Presence does not endorse content.
Expect failed candidates, stopped runs and records from methods that have
since changed. No library file in the main repository depends on anything
here, and nothing here records which main-repository commit it belongs to.

## Directories

| Directory | Owner | Holds | Lifetime |
|---|---|---|---|
| `review/results/` | `commonplace-review` | one result per reviewed (note, criterion) pair: the judgment and the hashes of the exact texts judged | until a later review of the pair replaces it or it is removed as orphaned; deleting one makes the pair eligible for review again |
| `review/packets/` | `commonplace-review` | each note's current full-pass packet with its disposition and the resolution of a pending hand-back | until a later pass replaces it; preserve while work is unresolved |
| `review/runs/` | `commonplace-review` | one directory per sweep (`<UTC stamp>/`) or per full pass and revision (`<workflow>/<note path>/<start-hash prefix>/`): call records, operator answers and accepted artifacts | replay inside the run; a run continues only from a checkout at the path its records name. Freshness never reads runs, so check continuation needs before removing one |
| `fixes/` | the [fix system](../../instructions/FIX-SYSTEM.md) | one `<note-stem>.fix-report.md` per fixed note, mapping each warning to its disposition | until the fix system retires the report |
| `ingest/` | `commonplace-ingest-handoff` | one working directory per open ingest: the handoff record and the candidate of its last drafting run; a record without an outcome marks a run that stopped midway | `prune` deletes published runs; keeping finished runs is provisional, see the [workshop case](../../work/decision-lifecycle-evidence/ingest-working-directory.md) |

Details of the review state and its freshness rules are in the
[review architecture](../../reference/review-architecture.md) and the
[review system](../../reference/README-REVIEW-SYSTEM.md).

## Leftovers without a current producer

- `revise-autoreason/`: two runs from 2026-04-13. The skill now works under
  `kb/work/revise-autoreason/` and removes its runs.
- `tag-placement/`: one tag-placement sweep from 2026-09-26 by a pipeline that
  no longer exists.

Neither is read by current code. They stay until the operator removes them;
removal loses only those runs' records.

## Material moved out of this directory

On 2026-11-11 the following went to `../commonplace-archive/kb/reports/state/`,
outside the checkout, keeping their names: the SQLite review stores and their
backups with `review-jobs/`, `reviews/`, `bundle-reviews/` and `full-pass/`
(the system ADR 127 replaced); the 96 run directories of the retired
agentic-analysis method (`agentic-system-analysis/`, minus the source
extractions three runs had made, which were deleted); and the meta-analyser
pilot traces (`meta-analyser-pilot-20261021/`), whose adjudication ADR 121
records. The X likes inbox and its sync state moved to the private snapshots
repository under `kb/sources/.snapshots/x-likes/`, because they hold other
people's posts.

Agentic-system analysis does not use this directory. Each analysis runs in a
dedicated worktree and keeps its state there; accepted results integrate into
tracked `retained/` sets. The eight runs under
`kb/agentic-systems/reports/state/` are from an earlier layout and cannot
resume under the current method.
