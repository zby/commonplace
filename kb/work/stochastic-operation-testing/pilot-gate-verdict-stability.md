# Pilot: gate verdict stability on unchanged text

Drafted 2026-11-14 and run the same day on the operator's approval. The [results](./pilot-gate-verdict-stability-results.md) record the outcome and where this protocol proved wrong: the per-trial estimate was low (44 launches and about 5.2 USD), the prior sweep was not comparable because its profile and prompt wrapper differed, and the `--force` fallback below was withdrawn before the run because the main checkout no longer held the fixture text.

## Question

When one (note, criterion) pair is reviewed again on unchanged inputs, how often does the outcome change, and which gates account for the changes?

The [first run](https://github.com/zby/commonplace/blob/142bff37aeaf7728a0c5cf9f3cd1c225598ba565/kb/work/decision-lifecycle-evidence/first-run.md) of the fix-findings variant prompted the question. Its re-review moved verdicts on passages the run had not edited, so one re-review could not separate the effect of a fix from run-to-run variation.

## Operator assumption this pilot works under

Set by the operator on 2026-11-14: review verdicts can be made stable, and the improvement procedure is designed on that assumption even if present stability is mediocre.

The pilot therefore does not decide whether re-review stays in the procedure. It measures the present gap and locates it. A poor result is a work list for stabilizing gates, not a reason to redesign the variant.

Two limits stay attached to the assumption. A stable verdict is not thereby a correct one; this pilot measures agreement between repeated runs, not agreement with an operator. And a stabilizing method that multiplies launches, such as voting over repeated runs, changes the cost of every re-review, so the method chosen matters to the design even when stability itself is assumed.

## Free evidence checked first

The 152 retained run directories under `kb/reports/state/review/runs/` hold 613 answered jobs and no repeat of one job on identical inputs. This follows from the freshness rule: a pair whose hashed inputs are unchanged is skipped. Of 395 distinct jobs, 178 were reviewed more than once, each time on changed text. Those repeats mix variation with the effect of the edit and cannot answer the question. Controlled trials are needed.

## Fixture

- **Note:** `kb/theory/two-context-boundaries-govern-operations-on-read-together-note-sets.md` at the first run's start text, commit `8786a9aeb`, sha256 `d30b10db…`.
- **Environment:** a detached `git worktree` at that commit, created outside the repository, one per trial. This fixes the note, its linked context and the gate criteria as committed. Each worktree starts with an empty state tree, so every pair is eligible and no trial reads another's results.
- **Not fixed:** the hosted model behind the profile, and the `commonplace-review` code, which runs from the main checkout's editable install. Record the model id each result reports and the main checkout's commit and dirty state at launch.
- **To verify before the first paid launch:** that `commonplace-review` run inside the worktree reads and writes that worktree's files. If it does not, fall back to `--force` in the main checkout on the committed text and take each trial's results from its run directory, since the shared store keeps only the last.

## Trials

- **Operation:** `commonplace-review run gates <note> --all-gates`, default profile, pair grouping.
- **Count:** four new trials. With the sweep that preceded the first run, each pair has five observations on the same text if that sweep's inputs match the fixture hashes; check this, and run a fifth trial if they do not.
- **Budget:** about 41 launches and 4.8 USD per trial by the first run's figure, so about 164 launches and 19 USD, or 24 USD with a fifth trial. Stop at the fixed count. Do not add trials because a result looks interesting.
- **Accounting:** record launches, infrastructure failures, retries and problem files separately. A pair with a failed launch is reported with its smaller denominator, not dropped.

## Measures

1. **Outcome agreement per pair:** the pair's outcomes across trials. A pair is stable when all agree.
2. **Finding agreement for warning pairs:** whether repeated warnings name the same passage and defect. Two warnings on different sentences count as agreement on outcome and disagreement on finding. An agent reads and matches the findings; the matching is recorded per pair so the operator can check it.
3. **Per gate:** which criteria hold the unstable pairs.

No rate is reported beyond these counts. One note cannot estimate stability across the collection, and the note was selected because its re-review looked unstable.

## What the result changes

- **Unstable gates** become the work list for stabilization. The inspected launches for each are kept as the diagnostic cases.
- **Finding-level disagreement under stable outcomes** means the outcome can be trusted before the finding can. The variant keys pending items to findings, so this would bear on how an item is matched to a later review.
- **Until stability is reached,** the variant states that one re-review is weak evidence about a fix. The first run already observed this; the pilot gives it a count.
- **A stable result** on this note would mean the first run's movement came from the edits or from context, and the next question is which.

## Retention

Each trial's worktree state tree is copied whole into `kb/reports/state/` under a directory for this pilot before the worktree is removed: results, run records, prompts, inputs and outputs. A summary with the per-pair table comes back to this workshop.
