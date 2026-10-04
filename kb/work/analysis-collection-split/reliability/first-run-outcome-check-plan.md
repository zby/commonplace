# First run outcome check: plan

## Commission

Agent draft, written on 2026-10-04 at the operator's request. It prepares the
first analysis run after the collection split, the profile job, named record
IDs and the analyst acceptance check. This file alone starts nothing. The
operator's launch is the authority for the run and for the audit after it.

Four decision records name this run as their outcome check:
[ADR 102](../../../reference/adr/102-separate-the-analysis-collection-and-publish-stable-system-paths.md),
[ADR 103](../../../reference/adr/103-classify-memory-profiles-after-record-verification.md),
[ADR 104](../../../reference/adr/104-name-analysis-records-with-stable-short-handles.md) and
[ADR 105](../../../reference/adr/105-let-analysts-run-their-acceptance-check-before-submission.md).

## Intent

Find out whether analysts under the new method submit fewer refused outputs,
and whether they use the acceptance check to get there. Fixtures showed that
the check behaves as specified. Only a run shows what analysts do with it.

The run changes four things at once against the audited runs. It cannot
attribute a difference to one of them. Record the result as an observation
per job and per rule, not as a verdict on a decision.

## What is run

- **System:** Dynamic Cheatsheet, source identity
  `https://github.com/suzgunmirac/dynamic-cheatsheet`, with
  `source-revision=5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`. This is the
  revision of both audited runs, so the source is held constant. The checkout
  `related-systems/suzgunmirac--dynamic-cheatsheet/` is clean at that commit.
  **Operator's choice before launch.** The alternative is Graphiti, a larger
  source with one stopped run and no completed baseline.
- **Method:** the committed `HEAD` at launch. Commit any intended method change before preparing the
  worktree; change nothing afterwards.
- **Procedure:** the `analyse-agentic-system` skill, unmodified. It prepares
  its own worktree with `commonplace-workflow prepare-analysis` and continues
  there in the same session.
- **Harness and model:** the operator's choice. Record both. The audited runs
  are the comparison basis only if the harness and model match theirs; if
  they differ, say so in the result.

## Baseline

The second audited run, `AAS-2026-10-03-dynamic-cheatsheet-02`, from its
[audit](../../analyse-agentic-system-amendments/second-run-audit.md):

| Measure | Second run |
|---|---|
| Accepted jobs | 14 |
| Worker sessions | 17 |
| Jobs needing a second handout | 3: `memory-0` (altered quotation), `reconcile-1` and `synthesize` (record ranges) |
| Substantive correction cycles | 2 |
| Environment blocks | 1 (source fetch inside the sandbox) |
| Wall time, open to publication | about 54 minutes |
| Final quotations | 14, all matching the frozen source |

The new workflow has two more jobs, profile and profile verification, so job
and session totals are not directly comparable. Compare refusals per job and
by rule.

## Preflight

All of these hold before the run opens. A failed item stops the launch.

1. `git status` in the originating checkout is clean, or its only changes are
   unrelated to startup instructions and `--allow-dirty-origin` is passed. On
   2026-10-04 one note under `kb/notes/` is modified by another session.
2. `uv run pytest -q` and `uv run ruff check .` pass at the method commit.
3. The session that invokes the skill starts in the originating checkout at
   the current `main`, not in a harness-made worktree at an older commit. The
   skill then prepares the worktree and continues in the same session;
   preparation refuses a `HEAD` behind `main`.
4. Code refuses a run's command that runs another checkout's code, so a
   worker that drops the worktree's command directory is stopped, not silently
   mixed. Count such refusals; they are evidence about the handover.
5. Network approval is requested for the first `step`, since source
   acquisition fetches. The second run lost one block to this.
6. `kb/agentic-system-analyses/retained/` holds no `dynamic-cheatsheet/`
   set. It is empty on 2026-10-04, so publication archives nothing.

## Boundaries

- **The coordinator receives only the skill invocation.** Do not give it
  this plan, the audits or the revisit conditions. Workers receive only their
  prompt files. Nobody in the run is told that use of the check is observed.
- **No method, code or instruction change during the run.** A defect found
  mid-run is recorded, not repaired.
- **The run loop's rules hold.** The coordinator does not write a job's
  output, read outputs to judge them, or work around a block.
- **A stopped run is a result.** Do not resume it under a changed method and
  do not reopen it to improve the counts.
- **Evidence is collected before cleanup.** Run state and scratch logs live
  in the worktree under an ignored directory. Removing the worktree deletes
  them.
- **Merging the published set back** into the originating checkout, and any
  commit of it, needs the operator's separate authorization, as the skill
  states. Comparisons under `kb/agentic-systems/comparisons/` become stale and
  are not rebuilt here.
- **Frozen sets and the historical reports are not edited.**

## What to collect

Before the worktree is removed, retain under
`kb/reports/retained/` or this directory, by the operator's choice at audit:

- the run directory's engine records: accepted and refused outputs, blocks,
  repair and stop reports;
- every `jobs/<job>/scratch/acceptance-checks.jsonl`;
- the coordinator's and every worker's harness trace, with hashes, as the
  earlier audits did;
- the method commit, source revision, harness, model, and open and
  publication times.

## What to count

Per job, with the rule each failure concerns:

- handouts, and refusals at acceptance by rule;
- check runs before submission, and their refusals by rule, from the scratch
  log; a job with no log line did not run the check;
- refusals at acceptance that the check would have reported — the direct
  sign that an analyst did not run it or did not act on it;
- the same rule failing in more than one check run of a job;
- quotations written in the accepted member; quotations not found and
  ambiguous per check run; attribution lines pasted from a proposal; ranges
  or revisions written by hand;
- unresolved or misspelled record names, IDs that extend another ID, range
  or group phrases refused, and attempts to rename an ID;
- failed reads of supplied or derived paths, and wrong-path source reads;
- verifier rejections and correction cycles, for records and for the profile;
- lapses in which a worker read a rule and did not apply it, counted
  separately;
- any statement by an analyst that a passing check shows its findings are
  correct.

Also record coverage and acceptance of the set, wall time, and whether the
accepted overview serves a reader as the review, which the
[collection design](../collection-design.md) asks the first run to check.

## Return to the operator

Stop and report when:

- a preflight item fails;
- the run stops, blocks without a permitted repair, or reports `uncertain`;
- publication leaves public state uncertain;
- a defect appears whose repair would change the method mid-run.

## Records

- **Audit result:** one file in this directory, in the form of the
  [second-run audit](../../analyse-agentic-system-amendments/second-run-audit.md):
  evidence and limits, the counts above against the baseline, recovered
  failures with causes, and what the traces cannot show.
- **Revisit conditions:** state for each `TODO` in ADR 102, 104 and 105 what this
  run observed, and for ADR 103 how the profile job and its verification went. One run does not close a marker; the operator
  decides.
- **Failure register:** the audit's failure rows are the first input to the
  register proposed in [remaining code checks](./remaining-code-checks-proposal.md),
  if that proposal is adopted.
