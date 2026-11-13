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
