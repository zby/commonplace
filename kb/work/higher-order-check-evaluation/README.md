# Higher-order check evaluation

## Goal

Evaluate, alone and before any composition relies on it, the check that the
[one improvement procedure](../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md)
runs first: does this note need a change to what it is (a split, a merge, a
rehome, a rejection, a different claim), and with what force. Produce a
calibrated check, or the finding that no cheap check can do this job.

The operator opened this workshop on 2026-11-13. The procedure's default
composition stops on a strong proposal and proceeds past a weak one or none,
so this one judgment decides whether lower-order edits run at all. The
proposal names the rule higher-order concerns before lower-order concerns;
this check is the one on the higher-order concerns. It is also the
hardest judgment in the procedure: on 2026-11-12 the full improvement pass,
at several dollars for one short note, proposed three narrower claims where
the operator's answer was deletion.

## Start here

This workshop stands alone. It needs no decision from any other workshop
or proposal, and nothing below waits on the improvement procedure being
built. The one design rule it works under is atomicity:

- The check is one operation on one note. Its inputs are files: the note,
  and whatever fixed context the check's own text names. It reads no
  conversation, no other operation's unrecorded output and no run state.
- Its output is one stored result per note that a batch run can keep and a
  later reader can interpret without the session that produced it.
- It can therefore be run by itself on one note, on a labelled set, or on a
  whole collection, and rerun after its wording changes.

A check that only works inside a composed improvement run fails this rule,
and that is a finding to report, not something to work around.

The existing shape fits without new code. A review gate is a criterion file
under `kb/instructions/review-gates/` with the fields the
[review-gate type](../../types/review-gate.md) lists, run with
`commonplace-review run gates <notes> --criteria <gate id>`, with results,
freshness, profiles and cost as the
[review system](../../reference/README-REVIEW-SYSTEM.md) describes. Its
three outcomes map onto what this check returns: `pass` for no proposal,
`warn` for a weak proposal, `fail` for a strong one, with the kind and the
grounds in the findings. Start with that mapping and report where it
strains. Draft wordings can live in this workshop until one is worth
placing in the catalog; say how you ran a draft that is not yet there.

Where state goes: the check's results are ordinary review results in the
shared store under `kb/reports/state/review/results/`, keyed by note and
criterion, exactly as they would be if an improvement run had asked for
them. Nothing is filed under this workshop's name there. The store keeps
one result per note and criterion, so give each wording of the check its
own criterion id; otherwise a rerun overwrites the wording it is to be
compared with. Labels, operator judgments and comparisons are this
workshop's own and stay in this directory.

Two practical matters to settle early and write down here:

- **Historical texts.** A labelled positive must be judged on its text from
  before the change. The batch command reviews files in the checkout, so
  decide how the old text is supplied (a worktree at the earlier commit, or
  copies under this workshop) and keep the outcome out of the worker's view,
  including the note's later path, its redirect and any log entry about it.
- **Spend.** Run one note, then the labelled set, before the collection.
  State the profile and the cost of each run, and ask the operator before a
  run over all of `kb/theory/`.

## What is being tested

One atomic review operation, written as an instruction that a batch run can
apply to one note at a time and that returns: no proposal, or a proposal with
its kind, its force (strong or weak) and its grounds. The check must run
through the existing batch machinery (`commonplace-review run gates` over a
directory with one criterion), so that it can be applied to every note in
`kb/theory/` and its results kept as ordinary review results. If the current
gate shape cannot carry a kind and a force, say what it lacks; that is a
finding for the procedure proposal's atom type.

## Questions

1. **Does it find the known cases?** Notes that were later split, merged,
   rehomed, retitled to a different claim or deleted are labelled positives.
   Git history and `kb/log.md` name them. The check runs on each note's text
   as it stood before the change. The two episodes of 2026-11-12 are the
   first two: the note deleted in commit bbc5ef0a4, and the note retitled in
   765cbcb8b. The check must not be shown the outcome
   ([calibrating semantic gates against labelled fixtures](../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md)
   requires non-leaking known cases).
2. **How often does it propose something on the collection as it stands?**
   Run it on all of `kb/theory/`. The procedure assumes that most notes get no
   proposal. Record the rate of none, weak and strong.
3. **Are its strong proposals right?** The operator judges a sample of the
   strong proposals from question 2, with a reason each. Those answers are
   the first labelled set made for this check rather than recovered from
   history.
4. **Is weak used as an escape?** A check under uncertainty can label
   everything weak, since weak never stops a run. Compare the weak share on
   known positives with the weak share on the collection.
5. **What does a run cost?** Per note and for the whole collection, by
   worker profile. The check runs first on every improvement run, so its
   cost is paid every time.
6. **Does a stated criterion beat free judgment?** Compare at least two
   wordings of the check, for example one that asks for the note's claim and
   which neighbours own it, against one that asks the question directly.

## Fixed boundaries

- The check proposes; it never edits. Every claim-level change stays with
  the author under ADR 080.
- Evaluate this operation alone. Do not measure it through a composed
  improvement run.
- Results are review results in the state tree. Labels and operator
  judgments made here are kept in this workshop until they are extracted.
- No statistic from this workshop lowers any authority grade. That decision
  belongs to
  [authority grades and learning from operator decisions](../../reference/proposals/authority-grades-and-learning-from-operator-decisions.md).

## How to advance the work

1. Collect the labelled positives from history, with the commit that holds
   each note's text before its change, and a matched set of notes that were
   reviewed and kept.
2. Write the first wording of the check as a review criterion.
3. Run it on the labelled set, then on all of `kb/theory/`.
4. Take the operator's judgments on a sample of strong proposals.
5. Revise the wording and repeat on fresh notes, keeping every wording and
   its results.

## Completion

Close when one of these holds:

- a wording of the check finds the known cases, proposes nothing on most of
  the collection, and has an operator-judged sample of its strong proposals;
  it is then extracted as an atom under `kb/instructions/` with its
  evaluation recorded;
- the evidence shows no wording at acceptable cost can do this, and the
  procedure proposal is revised to say what runs first instead.
