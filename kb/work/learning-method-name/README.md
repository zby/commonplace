# Defining the learning process

Posed 2026-11-21 by the operator. Written by an agent (claude-fable-5-2) from
one day's conversation with the operator. This page states the current
position. The directory name comes from the workshop's first goal, which was
to choose a name.

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
2. **Judgment in the loop.** Each change is kept or dropped by an on-balance
   judgment, made as a step of the learning loop. A judgment by one fixed
   measure is the special case.
3. **Open to criticism.** The judgment is held as a conjecture and can later
   be found wrong.

The operator clarified that keeping a reversible change is not an exception to
condition 2. The judge still expects the change to improve future work, but
can count less future harm if the system can detect and correct a mistake.

Deliberative learning is single-loop when the system cannot question its
measure and double-loop when a loop inside the system can revise it.

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
  [Eight boundary cases and three surveyed systems](./definition-checks.md)
  were placed against it, and
  [an independent reader](./positions/step-1-independent-reading.md) read it.
  Neither changed the wording.
- **[A review by ChatGPT](./positions/chatgpt-review.md)** supports the
  concept and the name, and objects to two parts of the definition.
- **[Earlier systems](./precedents.md)** from nine ingests are compared
  against the three conditions.
- **A fixed measure is no longer excluded.** The operator ruled on
  2026-11-21 that the definition should be general, with the fixed measure
  as a special case. The two kinds are named single-loop and double-loop.
  PRODIGY alone is a single-loop deliberative learner. The draft is revised.
  [The checks](./definition-checks.md) list which of their placements
  change, and [the discussion](./positions/fixed-measure-discussion.md)
  records how the ruling was reached.
- **[The rulings](./rulings.md)** record what the operator decided and how
  the definition was reached.

## Open questions about the definition

These are for the operator. The first four change the wording of the draft.

1. **Is condition 3 now strict enough?** It carries the exclusion that
   condition 2 used to carry. The draft requires that later evidence can
   count against a particular kept change. Whether a score-gated search that
   re-scores its kept variants meets that is not yet checked.
2. **What does the judgment in condition 2 compare?** The independent reader
   holds that deciding to keep a change is not judging that it improves
   future work. The operator's ruling stands: keeping a reversible trial is
   itself judged better for future work than not trying it. The wording
   should name both comparisons so they are not confused.
3. **Which writes does "each change" cover?** One surveyed system logs every
   attempt and selects distilled claims. The condition should say whether it
   covers candidate learning changes or all writes to the named store.
4. **What starts a later round in condition 3?** The draft says later rounds
   can criticize a judgment. It does not say whether the possibility is
   enough or whether the system must have something that starts
   reconsideration. Doyle's memo supplies the distinction.
5. **Is the strict meaning of "learned" intended?** The independent reader
   accepted it. ChatGPT finds it too strict, partly because it read
   "measure" as one dimension and not as a whole way of scoring the work.
   The on-balance note should say what a measure is. The stricter question
   is whether a defended trade-off that some reasonable measure opposes is
   an improvement or a decision. The note says a decision.
6. **Where "learned" lives.** It is a section of the draft. It could be a
   section of the on-balance note.

Two wording fixes need no ruling: the claim that in weights only the whole
model can be judged is too strong, and legibility should be related to
[addressability](../../theory/definitions/addressable-theory.md).

## Other open work

- **A boundary case for EURISKO**, the nearest program to condition 2.
- **Quotes.** Only the Argyris ingest has retained quotes.
- **A second round of ingests**, run by another agent: Rao and Georgeff,
  Aamodt and Plaza, and Minton and Carbonell.
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
  sense from the group sense and from the agent-architecture sense.
- The consumers in the evaluation boundary are listed and either edited or
  deferred with a reason.
- The next stage is either carried out or moved to a workshop of its own.

Then delete this directory and remove its entry from `kb/work/README.md`.

## Bookkeeping

Commits carry `Workshop: kb/work/learning-method-name`. Positions from other
agents go in `positions/`, one file each, marked with who wrote them and
whether the author confirmed the file.
