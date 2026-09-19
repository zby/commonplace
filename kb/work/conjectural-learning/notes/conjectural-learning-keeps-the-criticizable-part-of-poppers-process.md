---
description: "Why conjectural learning narrows Popper's process to formulated, addressable theories under addressed criticism, what a fixed interpreter changes, and the two conjectures the narrowing bets on with their baselines"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [foundations, learning-theory, self-improving-systems]
---

# Conjectural learning keeps the criticizable part of Popper's process

[Conjectural learning](../definitions/conjectural-learning.md) covers less
than the learning Popper describes. The definition says when the term
applies. This note argues for drawing it there: the reason for each
narrowing, what a fixed interpreter changes, and the two conjectures the
narrowing bets on.

## Popper runs one schema at two levels

Without language, the tentative theories are inborn expectations,
dispositions, and habits, and error elimination acts on the carrier itself:
the organism perishes or is changed together with its theory. With language,
a formulated theory can be criticized and discarded while its holder
survives. Scientists "try to let [their false theories] die in their stead"
([Popper 1968](../../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md#quotes),
§4, p. 347).

A system built on a language model has both levels. The weights hold
dispositions formed by training, a process that changes the carrier. The
articulated part, which is prose, prompts, and code, holds formulated
theories. The model that reads them links the two: "all our actions in the
first world are influenced by our second-world grasp of the third world" (§9,
p. 371). Mapping the weights onto Popper's lower level is our reading, not
his claim.

The KB does not deny learning at the lower level. It studies the level where a
theory can be criticized, replaced, and inspected one at a time, and where a
change in behavior can be attributed to a change in text.

## Why each narrowing

- **Carrier: theories formulated in language.** This is Popper's own point
  about rational criticism, though not about learning in general. A
  descriptive language developed outside the body gives critical discussion
  its object, and informal argument is criticized before it is formalized
  (1968, §4 and §6).
- **Structure: addressable theories.** Criticism needs a part to aim at. A
  theory that can only be replaced whole is still tentative, but it offers
  none.
- **Elimination: criticism of what the theory says.** Popper's schema "works
  through error elimination, and on the scientific level through conscious
  criticism" (1968, §5.2, p. 351). Selecting among variants by outcome alone
  applies the lower-level mechanism to formulated text: the text is treated
  as a genome, not as a claim. This is not criticism against selection. For
  Popper all learning is selection and none is instruction; the difference is
  whether a score eliminates whole variants or an argument eliminates claims.
- **Localization: criticism aimed at a part.** Popper allows a failed test to
  implicate a whole theoretical system and holds only that some cases
  identify the responsible hypotheses
  ([Conjectures and Refutations, Chapter 10, section XVI](../../../sources/popper-conjectures-and-refutations.ingest.md#quotes)).
  The KB keeps the addressed case on practical grounds: a failure that blames
  nothing leaves the successor unconstrained, so little is learned from it.
  The other case can occur; we do not study it.
- **Result: a persisting effect, actually used.** In Popper's schema
  criticism results "as a rule" in a new problem, and a text that could be
  understood is already objective knowledge, read or not. A system's learning
  shows in its later decisions, so the KB requires an effect that persists
  across a declared horizon and a theory on the causal path of decisions.

Two clarifications keep the last narrowing from being misread. Locating what
was learned in later decisions is not instrumentalism, the view that theories
are mere instruments for prediction, which Popper criticizes (*Conjectures
and Refutations*, Chapter 3). Criticism bears on what the theory says, and
whether a theory deserves its scope is judged separately, by
[reach-assessment](../../../notes/definitions/reach-assessment.md).

In one respect the definition asks less than Popper. He counts competing
theories and mutual criticism by argument among the indispensable means of
scientific growth (1968, §4, p. 347). The definition lets the same model
propose and criticize, and that model shares its blind spots with itself.
Independent assessment is a separate condition, described in
[externally tested theory builder](../../../notes/definitions/externally-tested-theory-builder.md).

## A fixed interpreter departs from Popper's scientist

Popper's scientist changes along with the theories: objective knowledge feeds
back on the mind that grasps it. With fixed weights that channel is closed,
and each episode reads the theory afresh. Two consequences follow.

- The articulated part must carry all of the learning, including what a
  person would absorb as tacit skill. Attribution becomes clean, and reliable
  interpretation of prose becomes the central empirical risk.
- Background knowledge held in the weights cannot be revised during the
  interval, where Popper holds any background assumption open to challenge.
  It can be criticized only through a retained theory about the interpreter,
  which is the reflective case.

Coevolution of weights, prompts, and code reopens the channel. Content from
criticized theories may be trained into the weights, and changed weights
read, apply, and criticize the theories differently. The KB admits this as an
extension of the term and does not pursue it; its experiments hold the
weights fixed. Whether the content of criticism, and not only the form of the
training intervention, transfers into weights is open. One placebo-controlled
adapter comparison found no content-specific effect
([PoPE](../../../sources/form-not-content-placebo-controlled-self-repair.ingest.md)).

## The narrowing bets on two conjectures

Each conjecture has a baseline among the definition's separate comparisons,
and either baseline may match or beat a conjectural learner. That is what the
experiments measure.

**The content conjecture: criticism of what a theory says learns more from
each failure than selection by outcome.** A score carries few bits. A
criticism says which claim failed and why, so one failure can rule out a
family of variants, and the reason is retained with the survivor. The
baseline is black-box optimization of articulated text, as in score-driven
prompt optimizers and evolutionary program search; the
[Meta-Agent Challenge](../../../sources/meta-agent-challenge-autonomous-agent-development.ingest.md)
is an instance that requires no explicit conjecture. The evidence so far does
not favor the conjecture. Controlled studies of code models have not
separated content from form: error content in prompts and in trained adapters
showed no advantage over placebo content (PoPE), and a full Popperian
procedure showed none over its labels alone
([Scaffold, Not Vocabulary?](../../../sources/scaffold-not-vocabulary-popperian-code-generation-skill.ingest.md)).
Neither study tested equivalence, or a retained theory reused across tasks.

**The efficiency conjecture: persisting more of the work of conjecture and
criticism costs less at comparable decision quality.** Three arrangements
differ in what persists.

| Arrangement | Persists | Each episode redoes |
|---|---|---|
| Raw records | Evidence only | The criticism and the theory |
| Retained criticisms | The eliminations | Assembling the theory |
| Retained theory | The assembled result | Nothing, but the theory needs maintenance and can go stale |

The conjecture is that cost falls down the table, because the earlier
arrangements repeat interpretive and inferential work, and that bounded
context widens the gaps, because the relevant records may not fit together
and must first be retrieved, selected, or summarized.

The two reconstruction baselines answer different questions. Against raw
records: does formulated, persisted criticism buy anything? This is the
primary comparison, because regeneration from raw records is widely used and
needs no criticism step: records are stored, retrieved, and handed to the
model. Against retained criticisms: does keeping the assembled theory buy
anything more? Compare by cost at comparable decision quality and by quality
under matched budgets, counting maintenance, and vary context capacity or
record volume to test the claimed widening.

## Open Questions

- Can the middle arrangement be kept distinct in practice? A record that says
  why a claim failed often already contains the revised claim.
- Should independent criticism enter the definition, or stay a separate
  condition?
- How dominant is regeneration from raw records among current agent memory
  systems? The KB has not established this.

---

Relevant Notes:

- [Conjectural learning](../definitions/conjectural-learning.md) — defined-in: the term whose boundary this note argues for
- [Addressable theory](../definitions/addressable-theory.md) — defined-in: the structural property the second narrowing requires
- [An experiment identifies only the contrast it actually runs](../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — grounds: why withholding a theory does not test its content
- [Learning by theory refinement may improve sample efficiency under structured shifts](../../../notes/learning-by-theory-refinement-may-improve-sample-efficiency.md) — see-also: the payoff conjecture under structured shifts, a different axis from the two stated here
- [Popper, Epistemology without a knowing subject](../../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md) — evidenced-by: the two levels, conscious criticism, and mutual criticism
- [Popper, Conjectures and Refutations](../../../sources/popper-conjectures-and-refutations.ingest.md) — evidenced-by: tests that implicate a whole system, and the criticism of instrumentalism
