# Refresh batch 01, rerun: Agent-S, MemoryOS and Basic Memory

The operator commissioned this handoff on 2026-09-28 for execution in a new
session. Its purpose is to rerun the first refresh batch under the current
method. The first run of batch 01 (branch `refresh-batch-01`, commit
`a39ba9be`, record `kb/work/agentic-memory-refresh/batch-01-2026-09-28.md`
on that branch) published all three sets, but in the layout that preceded
the directory-artifact output, and its friction led to fixes the method now
carries: worktree library resolution, line ranges only in quote
attributions, no Run identity section, no trailing whitespace in generated
quotes, a member lookup table, and finalization rules for merged and
rejected proposals. Its sets are superseded, not migrated; that branch is
not merged. This rerun analyses the same three systems afresh, two at a
time, each producing a retained analysis set and a fresh public review. No
analysis of this rerun has been started.

## Command for the next session

Paste this instruction into a fresh session at the Commonplace repository
root:

```text
Run the refresh batch 01 rerun described in
kb/work/agentic-memory-refresh/batch-01-rerun-handoff.md. Act as the batch
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
git worktree add -b refresh-batch-01-rerun ../commonplace-refresh-batch-01-rerun HEAD
```

Every analysis, verification and write happens inside
`../commonplace-refresh-batch-01-rerun`. Its base commit is every run's
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
| Agent-S | https://github.com/simular-ai/Agent-S | `<main checkout>/related-systems/simular-ai--Agent-S` | `kb/agent-memory-systems/reviews/Agent-S.md` (legacy revision `73ea1722…`) | agent harness with experience memory |
| MemoryOS | https://github.com/BAI-LAB/MemoryOS | `<main checkout>/related-systems/BAI-LAB--MemoryOS` | `kb/agent-memory-systems/reviews/MemoryOS.md` (legacy revision `1d717060…`) | memory/knowledge/context-engineering system |
| Basic Memory | https://github.com/basicmachines-co/basic-memory | `<main checkout>/related-systems/basicmachines-co--basic-memory` | `kb/agent-memory-systems/reviews/basic-memory.md` (legacy revision `fc2ee070…`) | memory/knowledge/context-engineering system |

This is a refresh: each coordinator fetches the current default branch of
its origin, resolves it to a full commit, and freezes that commit as the
run's source. Record it in the batch record. The legacy revisions are
inventory metadata, not the analysis boundary.

The functional scope is fixed with the source: each analysis covers the
whole shipped system at that commit, `boundary-kind: whole-system`, naming
every excluded subsystem with the conclusion its exclusion prevents. A
coordinator that finds the whole system infeasible stops and reports; the
batch coordinator decides whether to accept `subsystem-only` and records
the decision.

Public destinations are `kb/agentic-systems/reviews/agent-s.md`,
`kb/agentic-systems/reviews/memoryos.md` and
`kb/agentic-systems/reviews/basic-memory.md`. None exists on main; archived
reviews under `reviews-archive/` and the first run's sets on the
`refresh-batch-01` branch are not incumbents and are not to be read. Allocate fresh run IDs using the execution date.

## Execution and isolation

Follow the current analysis skill and its contracts. Each analysis is one
fresh coordinator plus its fresh memory specialist. Create each coordinator
with fresh context (for the collaboration tool, `fork_turns="none"`).
Supply only its source identity, absolute checkout path, public
destination, fresh run ownership, the whole-system scope rule, and the
current method instructions; supply repository doctrine explicitly if the
runtime does not load it. Do not give any worker this document, the legacy
review, the archived reviews, the first run's branch or record, or another
system's run.

Run two systems at a time: two coordinators with their two specialists fit
four worker slots. Start Agent-S and MemoryOS; start Basic Memory when a
slot pair frees. If capacity is smaller, run sequentially and say so. Use
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

Write `batch-01-rerun-<date>.md` in this workshop, linked from its README, and
answer: did every set validate and publish first time after preparation;
which of the first run's friction points recurred and which are new; and
the failed-validation, failed-prepare and correction counts per run beside
the first run's (Agent-S 1 failed prepare and 2 corrections, MemoryOS 1 and
1, Basic Memory 1 failed prepare, 1 failed memory validation and 3
corrections). Trace hashes, per-turn telemetry and worker
minutes are not required this time; report elapsed wall time for the batch.

Commit the batch on `refresh-batch-01-rerun`, staging by explicit path: three
reviews, three retained sets, three inventory rows, the batch record and
its README link. Do not merge, push or remove the worktree; the operator
does.

This commission covers three analyses, their publication, the bounded
downstream checks, three inventory rows, the batch record and the branch
commit. It does not touch the archive or batch 01's branch, change the
method, merge or delete the first run's branch, or commit anywhere else. Finish with the answers, the branch and
commit hash, or concrete blockers.
