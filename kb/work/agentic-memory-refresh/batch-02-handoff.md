# Refresh batch 02: OS-Copilot, A-mem and HippoRAG

The operator commissioned this handoff on 2026-09-28 for execution in a new
session. Its purpose is the second bounded batch of the corpus refresh:
three pending systems analysed under the current method, two at a time,
each producing a retained analysis set and a fresh public review. It runs
after the [batch 01 rerun](./batch-01-rerun-handoff.md) has been merged,
from a worktree based on that merge, and follows the same method. This document prepares the batch; no
analysis has been started.

## Command for the next session

Paste this instruction into a fresh session at the Commonplace repository
root:

```text
Run refresh batch 02 described in
kb/work/agentic-memory-refresh/batch-02-handoff.md. Act as the batch
coordinator: create the batch worktree, check the preconditions inside it,
run the three analyses two at a time, each with one fresh source-only
coordinator and its fresh memory specialist; verify each published set;
run the bounded downstream checks; update the three inventory rows; write
the batch record; and commit the batch on its branch. Follow the fixed
inputs and boundaries in that file.
```

## Batch worktree

The batch runs in its own git worktree so that other sessions' edits in
the main checkout cannot block or contaminate it. From the main checkout:

```bash
git worktree add -b refresh-batch-02 ../commonplace-refresh-batch-02 HEAD
```

Every analysis, verification and write happens inside
`../commonplace-refresh-batch-02`. Its base commit is every run's
`inputs-commit`. The installed `commonplace-*` commands execute the main
checkout's `src/commonplace/`, which must stay at the base commit for the
whole batch; publication refuses otherwise, so if it moves, stop and
report. Commands run inside the worktree use the worktree's `kb/` as the
library without any override.

Source checkouts stay under the main checkout's `related-systems/` and are
passed to coordinators by absolute path. Run state under
`kb/reports/state/` is ignored and lives in the worktree.

## Preconditions

Inside the batch worktree, confirm the following and stop with a report if
any fails:

- `kb/reports/types/agentic-system-analysis-set.md` exists, and skill step 7
  writes `output/overview.md`, `output/runtime.md`, `output/memory.md`,
  `output/epistemic.md` and `output/ARTIFACT.yaml`.
- `commonplace-quote --help` shows `--selections`.
- Each source checkout below has the origin named below.
- The worktree is clean, and the main checkout's `src/commonplace/` has no
  difference from the worktree's base commit.

At startup record HEAD and the worker models.

## Fixed inputs

| System | Repository | Checkout | Legacy artifact | Expected class |
|---|---|---|---|---|
| OS-Copilot | https://github.com/OS-Copilot/OS-Copilot | `<main checkout>/related-systems/OS-Copilot--OS-Copilot` | `kb/agent-memory-systems/reviews/OS-Copilot.md` (legacy revision `f720af88…`) | agent runtime with tool-creation memory |
| A-mem | https://github.com/WujiangXu/A-mem-sys | `<main checkout>/related-systems/WujiangXu--A-mem-sys` | `kb/agent-memory-systems/reviews/a-mem.md` (legacy revision `f303dfc7…`) | memory/knowledge/context-engineering system |
| HippoRAG | https://github.com/OSU-NLP-Group/HippoRAG | `<main checkout>/related-systems/OSU-NLP-Group--HippoRAG` | `kb/agent-memory-systems/reviews/HippoRAG.md` (legacy revision `d437bfb1…`) | document-ingest retrieval memory |

This is a refresh: each coordinator fetches the current default branch of
its origin, resolves it to a full commit, and freezes that commit as the
run's source. Record it in the batch record. The legacy revisions are
inventory metadata, not the analysis boundary.

The functional scope is fixed with the source: each analysis covers the
whole shipped system at that commit, `boundary-kind: whole-system`, naming
every excluded subsystem with the conclusion its exclusion prevents. A
coordinator that finds the whole system infeasible stops and reports; the
batch coordinator decides whether to accept `subsystem-only` and records
the decision. OS-Copilot is the batch's candidate for a runtime-dominated
set; do not narrow its boundary to its memory to save effort.

Public destinations are `kb/agentic-systems/reviews/os-copilot.md`,
`kb/agentic-systems/reviews/a-mem.md` and `kb/agentic-systems/reviews/hipporag.md`.
None exists; archived reviews under `reviews-archive/` are not incumbents
and are not to be read. Allocate fresh run IDs using the execution date.

## Execution and isolation

Follow the current analysis skill and its contracts. Each analysis is one
fresh coordinator plus its fresh memory specialist. Create each coordinator
with fresh context (for the collaboration tool, `fork_turns="none"`).
Supply only its source identity, absolute checkout path, public
destination, fresh run ownership, the whole-system scope rule, and the
current method instructions; supply repository doctrine explicitly if the
runtime does not load it. Do not give any worker this document, the legacy
review, the archived reviews, earlier batches' records, or another system's
run.

Run two systems at a time: two coordinators with their two specialists fit
four worker slots. Start OS-Copilot and A-mem; start HippoRAG when a slot
pair frees. If capacity is smaller, run sequentially and say so. Use
completion events and owned output paths, not agent-status listings. Prior
exposure to earlier analyses follows the skill's failure rule.

Do not edit governing files, the producer or the validators during the
batch. Record a discovered defect with its run and let the run continue if
it can complete under the contracts.

Defer every write of your own outside the run directories until all three
runs have published: inventory, batch record, cache directory.

## Acceptance

After each run, run the handoff command and `commonplace-validate
kb/reports/state/agentic-system-analysis/<run-id>/output --full`, which
validates the whole set including cross-member references, the profile's
record references and the finalized memory member. Then:

- **Record per run:** the resolved source commit; the boundary and its
  exclusions; body words and records per kind for each member; each failed
  validation or prepare with its first diagnostic; specialist correction
  turns; and every question, gap or invented value a worker produced, with
  the instruction text it was working from.
- **Downstream:** run the matrix builder, table renderer and statistics
  script with exactly the three new reviews as `--review` arguments, into a
  fresh directory under `kb/reports/cache/agentic-memory-refresh/`, and
  confirm each exits 0.
- **Inventory:** update only the three rows: `status`, `new_run`,
  `new_review`, and `new_result` pointing at the retained manifest
  `kb/reports/retained/agentic-system-analysis/<run-id>/ARTIFACT.yaml`, the
  file the review pins.

Write `batch-02-<date>.md` in this workshop, linked from its README, and
answer: did every set validate and publish first time after preparation;
did the runtime member dominate for OS-Copilot; which friction points
recurred from earlier batches and which are new; and the failed-validation and
correction counts per run. Trace hashes, per-turn telemetry and worker
minutes are not required this time; report elapsed wall time for the batch.

Commit the batch on `refresh-batch-02`, staging by explicit path: three
reviews, three retained sets, three inventory rows, the batch record and
its README link. Do not merge, push or remove the worktree; the operator
does.

This commission covers three analyses, their publication, the bounded
downstream checks, three inventory rows, the batch record and the branch
commit. It does not touch the archive or batch 01's branch, change the
method, or commit anywhere else. Finish with the answers, the branch and
commit hash, or concrete blockers.
