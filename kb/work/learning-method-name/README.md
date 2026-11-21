# Defining the learning process

Posed 2026-11-21 by the operator. Written by an agent (claude-fable-5-2) from
one day's conversation with the operator. This page states the current
position. The directory name comes from the workshop's first goal, which was
to choose a name.

## Settled: double-loop means the learner can revise its criterion

A single-loop learner can make and reverse **changes to its store**. A
double-loop learner can also change **what counts in favor of a change**. Name the
class of changes and the criterion that governs them. Neither using a formal
proof nor using a language model decides the classification.

**The classical Gödel machine is double-loop capable.** Its current utility
function can license a successor that ranks future alternatives differently.
A faster proof searcher using the same criterion is not a double-loop episode.
No separate validator is required; no particular run is guaranteed to change
the criterion. Commonplace's question is whether a language model can make
such revisions reliably when no adequate formal test is known in advance.

This [ruling](./rulings.md#settled-double-loop-ruling) governs this workshop,
including [case 15](./definition-checks.md#cases-1316--later-evidence-graded-attribution-and-the-gödel-machine-line).
The rest of the definition is still a draft.

## Commonplace and the Gödel-machine idea

> Commonplace is an attempt to make Gödel-machine-style self-improvement practical by replacing proof that a rewrite is worthwhile with an on-balance judgment about whether to make it.

This describes the research aim, not a guarantee. An [on-balance judgment](../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md) weighs reasons for and against the rewrite. It need not reproduce the verdict of any particular Gödel machine.

## Goal

Set by the operator: define the learning process we are working on. The
definition has to say what the process is, cover all the learning that
happens in Commonplace, and separate the process from the claim that a
particular change was learned.

## Result so far

[The draft definition](./draft-definition.md) defines **deliberative
learning** by two conditions:

1. **Legible, addressable store.** What is learned is held in the contents
   of a store that can be read and pointed at. The store is the system's
   own: its later work consumes those contents.
2. **Decision in the loop.** A change to the store is proposed, judged on
   the evidence the system has, and can be rejected. The judgment is an
   on-balance judgment of whether later work will go better with the change
   than without it. A judgment that applies one fixed criterion is the
   special case. A rule that updates the store directly from an input is
   not a decision.

A claim names the system, the store, the class of changes and the horizon.

Being open to criticism was a third condition until 2026-11-21. The operator
ruled it out after [a proposal that Neon and Astra amended](./positions/proposal-two-conditions.md).
Two properties are reported in its place: correction from later evidence
(none, bundle or targeted) and displacement. A deliberative learner is, in
the KB's existing terms, a self-improving system that works by proposal and
selection over a legible, addressable store.

The draft was rewritten on 2026-11-21 after three outside readings. The
rewrite removed workshop history, settled on "criterion" as the one word for
what a judgment applies, and stated Commonplace's conjecture in a section of
its own.

A change is an edit to the store's contents, including an edit to what
later work loads or selects. The operator ruled on 2026-11-21 that the
store holds contents and not changes, and that putting something into the
store is the change that does the learning. This replaced the wording in
terms of reliance; see
[the note to Neon and Astra](./positions/changes-to-the-store-not-reliance.md).

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
  against the definition.
- **A fixed measure is no longer excluded.** The operator ruled on
  2026-11-21 that the definition should be general, with the fixed measure
  as a special case. The two kinds are named single-loop and double-loop.
  PRODIGY alone is a single-loop deliberative learner. The draft is revised.
  [The checks](./definition-checks.md) list which of their placements
  change, and [the discussion](./positions/fixed-measure-discussion.md)
  records how the ruling was reached.
- **The Gödel-machine line is placed.** After the ruling for two
  conditions, [the checks](./definition-checks.md) place the Darwin Gödel
  Machine inside with displacement and no correction, the Huxley-Gödel
  Machine inside as single-loop with targeted correction, and the classical
  Gödel machine inside as double-loop capable. Schmidhuber's incremental
  self-improvement stays outside on the store.
  [What later evidence can overturn](./what-later-evidence-can-overturn.md)
  gives the background.
- **Two more outside readings were made of the two-condition draft:**
  [one launched by Astra](./positions/step-3-outside-reading.md) and
  [one on Claude Opus](./positions/step-3-outside-reading-opus.md).
- **[The rulings](./rulings.md)** record what the operator decided and how
  the definition was reached.

## Open questions about the definition

One question is open. The others were ruled on or closed on 2026-11-21 and
are listed with their answers.

1. **Does the rewritten draft hold up under a further outside reading?**
   Three outside readings were made:
   [of the three-condition draft](./positions/step-2-outside-reading.md),
   and of the two-condition draft by
   [a reader Astra launched](./positions/step-3-outside-reading.md) and by
   [a reader on Claude Opus](./positions/step-3-outside-reading-opus.md).
   Their findings are applied. No reader has seen the rewrite.

Closed:

- **Learning against replanning.** A claim declares its horizon. Claims
  about Commonplace use a horizon that spans tasks.
- **What the judgment in condition 2 compares.** The system with the change
  against the system without it. A trial and its review are two judgments
  with different alternatives, and the draft gives an example.
- **Which edits count.** Those made by a decision. Automatic storage is
  learning and not deliberative. Introducing it is a change that can be
  deliberated.
- **What starts a later round.** A claim about a system's capacity gives an
  account of what brings the evidence back, who or what considers it, and
  which edit can follow. A claim about an episode shows that sequence.
- **The strict meaning of "learned".** Kept. The on-balance note now says
  that a measure is a whole way of scoring the work and not one dimension.
- **Where "learned" lives.** In the definition file.
- **A decision against a direct update.** A change must be proposed and
  able to be rejected. A rule that updates the store directly from an input
  is outside, which removes the click-ranking job that two readers found
  the worst fit for the name.
- **"Each change" against a named class.** A claim is made for a named
  class of changes.
- **What the two conditions had lost.** Judgment on evidence and the
  exclusion of a work product are back in the conditions.
- **"Without the change".** The system as it now is with that one change
  taken out, not the system as it stood before the change.

## Other open work

- **Source support.** [Case 17](./definition-checks.md#case-17--eurisko-changes-how-it-judges-heuristic-generalizations) now grounds EURISKO's criterion revision in Lenat's H12′ episode. The [Gödel-machine ingest](../../sources/goedel-machines-schmidhuber.ingest.md#quotes) retains §6.1 item 4 on utility-function revision. Other historical placements should be grounded individually if used in the library.
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
