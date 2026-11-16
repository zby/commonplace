# Design: grouping the atoms into three procedures

## Status

Written on 2026-11-16 at the operator's request, as a design for approval.
Nothing in it is built. It follows
[edit operations and stops as atoms](./edit-and-stop-atoms-plan.md), whose
three changes are on main: review operations (ADR 132), edit operations
(ADR 133) and stops (ADR 134) each run alone, and review and edit
operations declare `depth` on one
[scale](../../reference/README-REVIEW-SYSTEM.md#order-of-concerns).

The operator's direction is three procedures: a full pass, a faster quick
pass, and a focused pass in which the operator names one defect and one
operation is applied. The operator chooses by the time available and by
what they see in the note.

## The main finding

The revise workflow is already the runner all three procedures need. It
executes a plan: a list of edit operations in depth order, each through
the same route as `commonplace-review run edit`. It stops on the typed
answers file of a per-item operation, stops again for approval of the
exact final text, and publishes once. Its run directory resumes and
replays.

Two of the three procedures already exist as ways of producing its plan:

- **Focused.** A plan that lists one operation. The first operator session
  through both stops, on 2026-11-16, was this: plain-wording alone on the
  links note.
- **Quick.** `--assess`: one assessor reads the note and chooses the
  operations from the closed list.

The full pass is the same thing with reviews first: run the review
operations, then let their findings choose the edits.

So the design is one runner and three ways to make its plan. The plan is
data, so the grouping can change without a code change. This is the
variable layer that the
[procedure proposal](../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md)
wanted to keep out of Python.

## The three procedures

| | Focused | Quick | Full |
|---|---|---|---|
| Operator supplies | the operation, or a finding | the purpose | the purpose |
| New review launches | none | none | every review operation with a `depth` |
| What chooses the edits | the operator | the assessor, from the note and any fresh stored findings | the assessor, from the note and the new findings |
| Can stop before editing | no | no | yes, on a depth 1 proposal |
| Stops for the operator | per-item answers, publication | per-item answers, publication | depth 1 proposal, per-item answers, publication |

### Focused

The operator names one edit operation, or one review finding. The plan
holds that one entry. Nothing is assessed and nothing is reviewed.

- A named operation runs on the whole note.
- A named finding runs
  [fix a finding by a named strategy](../../instructions/fix-warnings/fix-strategy-taxonomy.md)
  with that result file as its `finding` input. That operation changes
  only the passage the finding names.

The shorthand is `--pass NAME`, which writes the one-entry plan. A lookup
from a defect description to an operation is not built: only one edit
operation declares `responds-to` today, so there is no data to build it
from. The operator picks from the list, whose `description` fields each
start with "Use when".

### Quick

Today's `--assess`, with one addition: the assessor also receives the
note's fresh `warn` and `fail` results from the store, when any exist. It
launches no review. A note that has never been reviewed gets exactly what
`--assess` gives now.

This changes my earlier suggestion that the quick pass be defined by
which depths it keeps. Defining it by what it skips is simpler: it skips
all new review launches, which were 41 of the launches in the
[first run](./first-run.md) and most of its duration.

### Full

1. **Review.** Run every review operation that declares a `depth` on the
   note: the catalog gates, the compression checks and their synthesis,
   critique, composition friction and premise decomposition. Results go to
   the shared store as they do from a sweep. Fresh results are reused, as
   the sweep already does.
2. **Assess with the findings.** The assessor reads the note, the `warn`
   and `fail` results and the depth 1 reports, and writes the plan.
3. **Stop on a depth 1 proposal.** If a depth 1 report proposes changing
   what the note is (a split, a merge, a different claim, a rejection),
   the assessor sets the plan's `stop` with that proposal. The run ends
   with nothing edited. The operator either acts on the proposal outside
   the run or replaces the plan with `--plan` to go on. Both mechanisms
   exist today.
4. **Edit in depth order,** as the runner does now. A finding whose
   criterion is named in an operation's `responds-to` becomes a plan
   entry for that operation with the finding as input, placed at the
   criterion's depth.
5. **Publish** through the publication stop.

The full pass does not re-review the candidate. The first run showed that
one re-review is weak evidence about a fix: verdicts moved on passages
nobody had edited. After publication the results for the changed parts
are stale, and the next sweep refreshes them.

## What the assessor decides, and what code decides

Findings choose the edits, but through the assessor, not through a table
in code. Code cannot map a finding to an operation, because `responds-to`
is declared on one operation. The shared `depth` scale gives the assessor
a default: a finding at depth *n* points at the edit operation at depth
*n*. As `responds-to` declarations are added from runs, the mapping moves
from the assessor's judgment into the declarations.

Code keeps what it checks today: the plan lists known operations in
increasing depth, narrow-overclaims runs only with a `defend` list, each
edit stays within its bounds, and publication needs answers that approve
the exact candidate.

## What is retired

The cutover is one change with no compatibility layer.

- **The full-pass workflow:** its editor, copyedit, packet, closing cycle
  and single repair, with `commonplace-review run full-pass`,
  `commonplace-review packet` and the two full-pass instructions.
- **The fix procedure:** the fix-warnings instructions other than the
  strategy taxonomy, the fix report, and `FIX-SYSTEM.md`. Its use case is
  the focused pass with a finding.
- **The shelved drafts here:** the improvement-run directory types and the
  first variant. The revise run directory is the run record.

The six review method families stay; they are the review operations.

## What this gives up

- **No check that an edit fixed its finding.** The closing cycle did
  this, weakly. The replacement is the candidate already recorded in the
  [workshop README](./README.md#candidate-for-the-later-edit-operation-work-check-a-proposed-fix):
  a review operation whose target is a candidate text with its input. It
  is not part of this design.
- **No hand-back disposition.** The full pass's packet could hand a note
  back with a judgment for the whole pass. The depth 1 stop replaces it
  with a proposal and no typed states.
- **The fix report's per-finding record.** A finding fixed by the focused
  pass leaves an edit result and a publication decision. A finding the
  operator rejects as spurious leaves nothing unless a stop asks.

## Build order

1. **Findings into the assessment, and `--pass`.** The assessor accepts
   review results as inputs; `--pass NAME` and `--finding RESULT` write
   one-entry plans; the fix operation joins the closed list. After this
   step the focused and quick passes are complete.
2. **The review step.** `--full` runs the review operations before
   assessment and enables the depth 1 stop.
3. **Retirement.** Remove the full-pass workflow and the fix procedure,
   and rewrite the review-system reference around the three procedures.

Each step is tested as the atoms were: unit tests on the plan and the
stop, then one live run of the procedure on one note.

## Choices for the operator

1. **Names.** Recommended: keep `revise` as the command and name the
   procedures by flag (`--pass`, `--assess`, `--full`). The alternative
   renames the workflow, for example to `improve`, in the cutover.
2. **Old decisions.** `commonplace-review decisions` reads existing
   packets and fix reports. Recommended: keep those two readers until the
   operator says the old records are dispensable, because removing them
   hides recorded operator decisions. This is the one place the design
   keeps old code.
3. **What makes a depth 1 proposal stop the run.** Recommended: the
   assessor's judgment, with the proposal and its source report named in
   the plan's `stop`. The alternative is a stated criterion per review
   operation, which needs run data that does not exist.
4. **INFO-level findings.** Recommended: the assessor does not receive
   them. The first run read about a dozen and acted on none.
5. **Split out a treatment.** It writes a second file and is not an edit
   operation. Recommended: it stays a session instruction that the
   assessor can recommend in a depth 1 stop, and no procedure runs it.

## What is not known

- Whether the assessor chooses well from findings. It has only chosen
  from the note alone, and those choices have not been judged.
- How often depth 1 reports propose a change. If they propose on most
  notes, the full pass stops on most notes and the default has to change.
  The [higher-order check evaluation workshop](../higher-order-check-evaluation/README.md)
  holds this question.
- Whether the `depth` values are right. They are a first guess on both
  kinds of operation.
- How long a full pass takes. No cost is declared; the operator sees it
  on the first run.
