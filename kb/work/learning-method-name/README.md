# Defining the learning process

Posed 2026-11-21 by the operator. Written by an agent (claude-fable-5-2) from
one day's conversation with the operator. This page states the current
position. The directory name comes from the workshop's first goal, which was
to choose a name.

## Settled: double-loop means the learner can revise its criterion

A single-loop learner can change **which changes it relies on**. A double-loop
learner can also change **what counts in favor of relying on them**. Name the
class of changes and the criterion that governs them. Neither using a formal
proof nor using a language model decides the classification.

**The classical Gödel machine is double-loop capable.** Its current utility
function can license a successor that ranks future alternatives differently.
A faster proof searcher using the same criterion is not a double-loop episode.
No separate validator is required; no particular run is guaranteed to change
the criterion. Commonplace's question is whether a language model can make
such revisions reliably when no adequate formal test is known in advance.

This [ruling](./rulings.md#settled-double-loop-ruling) governs this workshop,
including [case 15](./definition-checks.md#cases-1316--reliance-graded-attribution-and-the-gödel-machine-line).
The rest of the definition is still a draft.

## Goal

Set by the operator: define the learning process we are working on. The
definition has to say what the process is, cover all the learning that
happens in Commonplace, and separate the process from the claim that a
particular change was learned.

## Result so far

[The draft definition](./draft-definition.md) defines **deliberative
learning** by three conditions:

1. **Legible store.** What is learned is kept as changes to a store that can
   be read.
2. **Judgment in the loop.** Whether later work relies on a change is decided
   by an on-balance judgment, made as a step of the learning loop. A judgment
   by one fixed measure is the special case.
3. **Open to criticism.** Continued reliance is held as a conjecture.
   Evidence from later use can count against continuing to rely on a change,
   reducing or ending reliance on it rather than merely displacing it when a
   higher-scoring alternative appears.

The operator clarified that keeping a reversible change is not an exception to
condition 2. The judge still expects the change to improve future work, but
can count less future harm if the system can detect and correct a mistake.

The term has no success condition. "Learned" is a separate claim about one
retained change. A gain on some measures with ties on the rest is reported
as such, not as a gain on every reasonable measure.

The on-balance note was updated on 2026-11-21 to state the definition of
improvement that the draft relies on. The accompanying notes explain how to
examine a disputed judgment and how reversibility can limit future loss.

## Next stage

The operator proposed that deliberative learning replace the theory builder
as Commonplace's central definition, with the theory builder kept in notes
and articles for some time.
[The assessment and plan](./theory-builder-demotion.md) separate two questions:
which definition should lead the research program, and whether every theory
builder is a deliberative learner. Moving the emphasis does not require a yes
to the second question. The operator ruled on 2026-11-21 that the theory
builder is demoted without deciding the second question: "I think we can
demote theory builder without deciding if it is a special case". The relation
and the order of work remain open. The system's name is ruled: deliberative
learner.

## Where things stand

- **The definition has been tested, not adopted.**
  [Boundary cases and three surveyed systems](./definition-checks.md)
  were placed against it, and
  [an independent reader](./positions/step-1-independent-reading.md) read it.
  Neither changed the wording.
- **[A review by ChatGPT](./positions/chatgpt-review.md)** supports the
  concept and the name, and objects to two parts of the definition.
- **[Earlier systems](./precedents.md)** from two rounds of ingests are compared
  against the three conditions.
- **A fixed measure is no longer excluded.** The operator ruled on
  2026-11-21 that the definition should be general, with the fixed measure
  as a special case. The two kinds are named single-loop and double-loop.
  PRODIGY alone is a single-loop deliberative learner. The draft is revised.
  [The checks](./definition-checks.md) list which of their placements
  change, and [the discussion](./positions/fixed-measure-discussion.md)
  records how the ruling was reached.
- **Conditions 2 and 3 revised around reliance, graded attribution, and the
  Gödel-machine line.** Following
  [what later evidence can overturn](./what-later-evidence-can-overturn.md),
  the draft separates evidence against continued reliance from displacement by
  a challenger and distinguishes bundle rollback from localized blame. Cases
  13–16 place DGM outside on C, HGM inside as single-loop for archive parent
  selection, the classical Gödel machine inside as double-loop capable,
  and Schmidhuber's incremental self-improvement (outside on S, passes C at
  coarse attribution minimum).
- **[The rulings](./rulings.md)** record what the operator decided and how
  the definition was reached.

## Open questions about the definition

These are for the operator. The first five change the wording of the draft.

1. **Is condition 3 now strict enough?** It carries the exclusion that
   condition 2 used to carry. The reliance wording and cases 9–11 and 13–16
   separate post-admission evidence from challenger displacement (DGM, static
   benchmarks) and place HGM and re-scored searches inside as single-loop.
   Whether this boundary holds up under an independent reading is still open.
2. **What separates learning from replanning?**
   [Case 12 of the checks](./definition-checks.md) shows that a sequencer
   which drops a schedule when it becomes infeasible would pass all three
   conditions if the current schedule were named as the store. The
   definition needs to say that the kept change carries into later work.
3. **What does the judgment in condition 2 compare?** The independent reader
   holds that deciding to keep a change is not judging that it improves
   future work. The operator's ruling stands: keeping a reversible trial is
   itself judged better for future work than not trying it. The wording
   should name both comparisons so they are not confused.
4. **Which writes does "each change" cover?** One surveyed system logs every
   attempt and selects distilled claims. The condition should say whether it
   covers candidate learning changes or all writes to the named store.
5. **What starts a later round in condition 3?** The draft says later rounds
   can criticize a judgment. It does not say whether the possibility is
   enough or whether the system must have something that starts
   reconsideration. Doyle's memo supplies the distinction.
6. **Is the strict meaning of "learned" intended?** The independent reader
   accepted it. ChatGPT finds it too strict, partly because it read
   "measure" as one dimension and not as a whole way of scoring the work.
   The on-balance note should say what a measure is. The stricter question
   is whether a defended trade-off that some reasonable measure opposes is
   an improvement or a decision. The note says a decision.
7. **Where "learned" lives.** It is a section of the draft. It could be a
   section of the on-balance note.

The two earlier wording fixes (replacing the overstatement about weights and
linking legibility to
[addressability](../../theory/definitions/addressable-theory.md)) and the
question of what later evidence can overturn are now applied in the draft.

## Other open work

- **A boundary case for EURISKO**, the nearest program to condition 2.
- **Quotes.** Only the Argyris ingest has retained quotes.
- **The conjecture itself.** That a language model can make on-balance
  judgments well enough is not established. The
  [Python change judgment probe](../../reports/retained/python-change-judgment-probe-2026-11-20/README.md)
  was designed to test it.

## Evaluation boundary

Until the operator adopts the draft, do not edit these to introduce the term:

- `kb/theory/definitions/theory-builder.md` and its checks;
- `kb/theory/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md`;
- the articles under `kb/articles/`, including the lead article's "distinct
  learning paradigm" section;
- the vocabulary table in `AGENTS.md` and the
  [collision ledger](../../reference/vocabulary-collision-ledger.md), which
  has no entry for "deliberative".

The September retirement of "conjectural learning" stands, so the redirects
in `properdocs.yml` need no change.

## What closes the workshop

- The operator adopts the draft, or a revision of it.
- The definition of "learned" has an independent reader's acceptance or a
  recorded disagreement. Done: the reader accepted it.
- The open questions above are ruled on.
- The definition is in the library under `kb/theory/definitions/`, and the
  term is in the `AGENTS.md` vocabulary table.
- The collision ledger has an entry for "deliberative" that separates this
  sense from the group sense and from the agent-architecture sense, and an
  entry for "double-loop" that separates this sense from Argyris's.
- The consumers in the evaluation boundary are listed and either edited or
  deferred with a reason.
- The next stage is either carried out or moved to a workshop of its own.

Then delete this directory and remove its entry from `kb/work/README.md`.

## Bookkeeping

Commits carry `Workshop: kb/work/learning-method-name`. Positions from other
agents go in `positions/`, one file each, marked with who wrote them and
whether the author confirmed the file.
