# Refresh batch 01: three new systems under the member-set producer

The operator commissioned this handoff on 2026-09-28 for execution in a
new session. Its purpose is the first bounded batch of the corpus refresh
after the retained corpus was archived: three systems not analysed before
under the current method, run in parallel where the runtime allows, each
producing a retained member set and a fresh public review. This document
prepares the batch; no analysis has been started.

## Command for the next session

Paste this instruction into a fresh session at the Commonplace repository root:

```text
Run refresh batch 01 described in
kb/work/agentic-memory-refresh/batch-01-handoff.md. Act as the batch
coordinator: create the batch worktree, check the preconditions inside it,
launch one fresh source-only analysis
coordinator per system, each with its mandatory fresh memory specialist,
in parallel if capacity allows; verify each completed set and review; run
the bounded downstream checks; update the three inventory rows; record the
batch in the workshop; and commit the batch on its branch. Follow the fixed
inputs and boundaries in that file.
```

## Batch worktree

The batch runs in its own git worktree so that no other session's edits in
the main checkout can block or contaminate it. From the main checkout, whose
worktree must be clean:

```bash
git worktree add -b refresh-batch-01 ../commonplace-refresh-batch-01 HEAD
```

Every analysis, verification and write of this batch happens inside
`../commonplace-refresh-batch-01`; nothing is written in the main checkout.
Record the worktree's base commit: it is every run's `inputs-commit`.

The `commonplace-*` commands are an editable install of the main checkout,
so inside the worktree they execute the main checkout's `src/commonplace/`.
Publication refuses when that source differs from `inputs-commit`, so the
main checkout's `src/commonplace/` must stay at the base commit for the
whole batch; if it moves, stop and report rather than reinstalling.

Source checkouts stay where they are: pass each coordinator the absolute
path of its checkout under the main checkout's `related-systems/` (below),
which the run state records by absolute path. Do not create
`related-systems/` inside the worktree. Run state under
`kb/reports/state/` is ignored and lives in the worktree.

## Preconditions

This batch runs under the member-set producer, not the archived
single-file result. Inside the batch worktree, before launching anything,
confirm all of the following and stop with a report if any fails:

- `kb/types/agentic-system-analysis-overview.md` exists and
  `kb/instructions/analyse-agentic-system/SKILL.md` step 7 writes
  `overview.md`, `runtime.md`, `memory.md` and `epistemic.md`. If the skill
  still writes `result.md`, the transition in
  `kb/work/agentic-analysis-output-documents/transition-plan.md` has not
  landed; do not run the batch under the old producer.
- `kb/reports/retained/agentic-system-analysis/` holds no single-file
  results; the archived corpus is under
  `kb/reports/retained/agentic-system-analysis-archive/`.
- `commonplace-quote --help` shows `--selections`.
- Each source checkout named below has the origin named below.
- The batch worktree is clean, and the main checkout's `src/commonplace/`
  has no difference from the worktree's base commit. Publication enforces
  both, together with unchanged method paths since `inputs-commit`; sibling
  runs' uncommitted publications do not block one another.

At startup record HEAD, the SHA-256 of the five governing files (the
skill, the memory instruction, the epistemic instruction, the overview type
and the memory report type), working-tree status, and the actual worker
models.

## Fixed inputs

Three systems of different target classes, chosen from the pending
inventory so that the runtime member dominates in at least one set:

| System | Repository | Checkout | Legacy artifact | Expected class |
|---|---|---|---|---|
| Agent-S | https://github.com/simular-ai/Agent-S | `<main checkout>/related-systems/simular-ai--Agent-S` | `kb/agent-memory-systems/reviews/Agent-S.md` (legacy revision `73ea1722…`) | agent harness with experience memory |
| MemoryOS | https://github.com/BAI-LAB/MemoryOS | `<main checkout>/related-systems/BAI-LAB--MemoryOS` | `kb/agent-memory-systems/reviews/MemoryOS.md` (legacy revision `1d717060…`) | memory/knowledge/context-engineering system |
| basic-memory | https://github.com/basicmachines-co/basic-memory | `<main checkout>/related-systems/basicmachines-co--basic-memory` | `kb/agent-memory-systems/reviews/basic-memory.md` (legacy revision `fc2ee070…`) | extension or tool mechanism over local files |

Revisions are not fixed in advance: this is a refresh, so each
coordinator fetches the current default branch of its origin, resolves it
to a full commit, and freezes that commit as the run's source. Record the
resolved commit in the batch record. The legacy revisions above are
inventory metadata for the comparison, not the analysis boundary.

The functional scope is fixed alongside the source: each analysis covers
the whole shipped system at that commit, with `boundary-kind:
whole-system`, and names every excluded subsystem with the conclusion its
exclusion prevents. A coordinator that finds the whole system infeasible
in one run stops and reports rather than narrowing silently; the batch
coordinator decides whether to accept a `subsystem-only` boundary and
records the decision.

Public destinations are `kb/agentic-systems/reviews/agent-s.md`,
`kb/agentic-systems/reviews/memoryos.md` and
`kb/agentic-systems/reviews/basic-memory.md`. None exists today; the
archived reviews under `reviews-archive/` are not incumbents and are not to
be read. Allocate fresh run IDs using the execution date.

## Execution and isolation

Follow the current analysis skill and its contracts. Each analysis is one
fresh coordinator plus its fresh memory specialist, as in the pilots.
Create each coordinator with fresh context (for the collaboration tool,
`fork_turns="none"`). Supply only its source identity, checkout, public
destination, fresh run ownership, the whole-system scope rule above, and
the current method instructions. Explicitly supply repository doctrine if
the runtime does not load it. Do not give any worker this document, the
legacy review, the archived reviews, or another system's run.

Parallelism: the three runs have disjoint run directories and review
destinations, so they may run concurrently. Launch all three only if the
runtime can hold six workers at once with capacity reserved for each
specialist; otherwise run them in sequence and say so. Do not launch a
second writer for any output while the first is unresolved. Use
completion events and owned output paths, not agent-status listings.
Prior-analysis exposure in any worker follows the skill's failure rule:
abandon that run and replace it with a fresh coordinator and run ID.

Do not edit the governing files, the producer, or the validators during
the batch. Record a discovered defect with its affected run and let the
run continue if the worker can complete it under the contracts; stop
dependent work only if the defect prevents valid completion.

## Evidence and acceptance

Defer every write of your own outside the run directories until all three
runs have published: the inventory update, the batch record, the cache
directory, and any note. An untracked or modified file under `kb/` outside
the two output locations blocks a later run's publication.

After each run, independently run the handoff command and the run-state
verification, which checks the pin chain (run state, overview manifest,
member hashes and types, review pin), `run-id` and `reviewed-boundary`
agreement across members, the memory member's `finalized-from` against the
local report and its input hash, each member's own validation, and anchor
resolution on every member and the review. Cross-member identifier
resolution and the finalization derivation are deliberately not checked
until `kb/work/directory-artifacts` lands; read each set for an ID
referenced in one member and declared in none, and record any you find.
Retain traces, hashes and model identities in a new
dated cache directory under `kb/reports/cache/agentic-memory-refresh/`.
Report inaccessible trace portions as audit gaps.

For each run record: the resolved commit; the boundary chosen and any
exclusion; member word counts and record counts per kind; quote counts
per member; every gap, question or invented value a worker
produced, with the quoted instruction text; truncation and retries; and
the fourteen profile assessments.

Run the bounded matrix, table and statistics checks against exactly the
three new reviews into a fresh cache output directory and verify their
identities. Update only the three inventory rows in `inventory.csv`
(status, new run, review, result) after validated publication.

Write `batch-01-<date>.md` in this workshop and link it from its README.
Answer separately: did every set validate and publish; did the runtime
member dominate for Agent-S; did any worker meet a gap in the member-set
contracts; and what the batch cost in worker time and retries, as a basis
for scheduling the remaining 156 entries.

When every run has published, commit the batch on `refresh-batch-01` in
the worktree, staging by explicit path: the three reviews, the three
retained sets, the three inventory rows and the batch record, with the
README link. Do not merge into main, push, or remove the worktree; the
operator merges the branch and removes the worktree after reviewing it.

This commission covers three analyses, their publication, bounded
consumer checks, three inventory rows, the batch record and the batch
commit on its branch. It does not touch the archive, migrate any old
result, change the method, or commit anywhere but the batch branch.
Finish with the evidence-backed answers, the branch and commit hash, or
concrete blockers.
