---
description: "Why conjectural learning narrows Popper's process to formulated theories criticized for what they say, why it adds a knowing subject, what a fixed interpreter changes, and the three conjectures it bets on"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [foundations, learning-theory, self-improving-systems]
---

# Conjectural learning keeps the criticizable part of Popper's process

Popper describes learning as conjecture followed by attempted error
elimination, in every organism and at every level.
[Conjectural learning](../definitions/conjectural-learning.md) keeps one part
of that process: the part where theories are written down in language, used
in decisions, and criticized for what they say, with the result carried into
later work. It sets aside learning that needs no written
criticism: a model that regenerates what it needs from raw records each time,
or text that is selected by score alone. The KB bets that the kept part pays
in three ways: a system that criticizes what a theory says learns more from
each failure than one that selects by outcome, criticism that can name a part
of the theory learns more than criticism of the whole, and carrying the
results forward costs less than redoing the work. No bet is established.

The definition says when the term applies. This note gives the reason for
each narrowing and for the one addition, says what changes when the model
that reads the theories cannot itself change, and states the three bets with
the comparisons that would test them.

## Popper applies one schema at two levels

Without language, the tentative theories are inborn expectations,
dispositions, and habits, and error elimination acts on the carrier itself:
the organism dies or is changed together with its theory. With language, a
formulated theory can be criticized and discarded while its holder survives.
Scientists "try to let [their false theories] die in their stead"
([Popper 1968](../../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md#quotes),
§4, p. 347).

A system built on a language model has both levels. The weights hold
dispositions formed by training, a process that changes the carrier. The
formulated part, which is prose, prompts, and code, holds the theories. The
model that reads them, the interpreter, links the two. In Popper's terms the
physical world is the first, the mind the second, and formulated knowledge
the third, and "all our actions in the first world are influenced by our
second-world grasp of the third world" (1968, §9, p. 371). Mapping the
weights onto Popper's lower level is the KB's reading. Both levels are inside
the learning system: the formulated part is outside the model weights, not
outside the system.

The KB does not deny learning at the lower level. It studies the level where a
theory can be criticized, replaced, and inspected one at a time, and where a
change in behavior can be attributed to a change in text.

## Why each narrowing

The two labels are the rows of the definition's table.

- **Form: theories formulated in language.** This is Popper's own point about
  rational criticism, though not about learning in general. A descriptive
  language developed outside the body gives critical discussion something to
  criticize. Informal argument is criticized before it is formalized (1968,
  §4 and §6).
- **Elimination: criticism of what the theory says.** Popper's schema "works
  through error elimination, and on the scientific level through conscious
  criticism" (1968, §5.2, p. 351). Selecting among variants by outcome alone
  applies the lower-level mechanism to formulated text: the text is treated
  as a genome, not as a claim. Both are selection in Popper's sense. The
  difference is whether a score eliminates whole variants or an argument
  eliminates claims.

In one respect the definition asks less than Popper. He counts competing
theories and mutual criticism by argument among the indispensable means of
scientific growth (1968, §4, p. 347). The definition lets the same model
propose and criticize, and the same blind spots affect it in both roles.
Independent assessment is a separate condition, described in
[externally tested theory builder](../../../notes/definitions/externally-tested-theory-builder.md).

## The KB adds a knowing subject

Popper's essay is titled *Epistemology Without a Knowing Subject*, and the
omission is deliberate. Knowledge in his objective sense does not depend on
anyone holding it: a book belongs to it if it could in principle be
understood, and he admits no further requirement (1968, §3, p. 342).
Criticism results "as a rule" in a new problem, whether or not anyone takes
the problem up.

A definition of a system's learning has to put the subject back. It names the
system whose decisions the theory guides, requires that the system actually
uses the theory, and requires that the effect of criticism persists for that
system across a declared horizon. These are additions of a different kind
from the narrowings. The narrowings select among the cases Popper's process
covers; the additions tie the process to one system.

Locating what was learned in the system's later decisions is not
instrumentalism, the view that theories are mere instruments for prediction,
which Popper criticizes (*Conjectures and Refutations*, Chapter 3).
Criticism still bears on what the theory says, and whether a theory deserves its scope is
judged separately, by
[reach-assessment](../../../notes/definitions/reach-assessment.md).

## A fixed interpreter departs from Popper's scientist

Popper's scientist changes along with the theories: objective knowledge feeds
back on the mind that grasps it. With fixed weights that channel is closed,
and each episode reads the theory from scratch. Two consequences follow.

- The formulated part must carry all of the learning, including what a
  person would absorb as tacit skill. Attributing a change in behavior to a
  change in text becomes more reliable, since parameter updates are ruled out
  as a source of change. Whether the model interprets prose reliably becomes
  the central empirical risk.
- Background knowledge in the weights cannot be revised while the weights
  stay fixed, whereas Popper treats any background assumption as open to
  challenge. It can be criticized only through a retained theory about the
  interpreter, which is the reflective case.

Coevolution of weights, prompts, and code reopens the channel. Content from
criticized theories may be trained into the weights, and changed weights
read, apply, and criticize the theories differently. Such a system is still
inside the term, but the KB's experiments hold the weights fixed. It is
open whether what transfers into the weights is the content of the criticism
and not only the form of the training intervention. One placebo-controlled
adapter comparison found no content-specific effect
([PoPE](../../../sources/form-not-content-placebo-controlled-self-repair.ingest.md)).

## The narrowing bets on three conjectures

The content and efficiency conjectures are tested against some of the
definition's separate comparisons, the arrangements that fail one of its two
conditions. The addressability conjecture compares two arrangements that both
meet them. The split follows one rule: a condition is part of the definition
when removing it changes which mechanism does the learning, and it is a
conjecture when removing it changes only how well the learning works. In an experiment the arrangement compared against is a baseline, and a baseline may match or
outperform a conjectural learner. That comparison is what the experiments
measure.

**The content conjecture: a system that criticizes what a theory says learns
more from each failure than one that selects by outcome.** The reasoning is
that a score carries few bits, while a criticism says which claim failed and
why, so one failure can rule out a family of variants, and the reason is
retained with the survivor. The baseline is black-box optimization of prompts
and programs, as in score-driven prompt optimizers and evolutionary program
search. The
[Meta-Agent Challenge](../../../sources/meta-agent-challenge-autonomous-agent-development.ingest.md)
is one such optimizer, and it requires no explicit conjecture.

The evidence so far does not favor the conjecture. Controlled studies of code
models have not separated content from form: error content in prompts and in
trained adapters showed no advantage over placebo content (PoPE), and a full
Popperian procedure showed none over its labels alone
([Scaffold, Not Vocabulary?](../../../sources/scaffold-not-vocabulary-popperian-code-generation-skill.ingest.md)).
Neither study tested equivalence, and neither tested a retained theory reused
across tasks.

**The addressability conjecture: criticism that can name a part of the theory
learns more from each failure than criticism of the whole.** An
[addressable theory](../definitions/addressable-theory.md) has assumptions,
scope, and parts that can be inspected and revised individually. Popper allows
a failed test to implicate a whole theoretical system and holds only that
some cases identify the responsible hypotheses
([Conjectures and Refutations, Chapter 10, section XVI](../../../sources/popper-conjectures-and-refutations.ingest.md#quotes)).
The reasoning is that a failure which names no part leaves the successor
unconstrained, while a named part lets the revision keep what still works.
The named part is a candidate. The baseline is unaddressed revision: a
failure is read, and may be described, but the theory is rewritten or
regenerated whole. That arrangement is conjectural learning too, so this
comparison is between two implementations of the paradigm. The definition
does not require addressability; the KB builds for it on this conjecture.

**The efficiency conjecture: persisting more of the work of conjecture and
criticism costs less at comparable decision quality.** Three arrangements
differ in what persists.

| Arrangement | Persists | Each episode redoes |
|---|---|---|
| Raw records | Evidence only | The criticism and the theory |
| Retained criticisms | The eliminations | Assembling the theory |
| Retained theory | The assembled result | Nothing (but the theory needs maintenance and can go stale) |

The conjecture is that cost falls down the table, because the earlier
arrangements repeat interpretive and inferential work. It also says that
bounded context widens the cost differences between the arrangements, because
the relevant records may not all fit in context at once and must first be
retrieved, selected, or summarized.

The two reconstruction baselines answer different questions. Against raw
records: does formulated, persisted criticism buy anything? This is the
primary comparison, because regeneration from raw records needs no criticism
step: records are stored, retrieved, and handed to the model. The operator
takes regeneration from raw records to be the dominant approach today, but
the KB has not established that. Against retained criticisms: does keeping
the assembled theory buy anything more?

Compare the arrangements by cost at comparable decision quality and by
quality under matched budgets, counting maintenance cost. Vary context
capacity or record volume to test whether bounded context widens the
differences.

## Open Questions

- Can the middle arrangement be kept distinct in practice? A record that says
  why a claim failed often already contains the revised claim.
- Should independent criticism be part of the definition, or stay a separate
  condition?
- How dominant is regeneration from raw records among current agent memory
  systems?

---

Relevant Notes:

- [Conjectural learning](../definitions/conjectural-learning.md) — defined-in: the term whose boundary this note argues for
- [Addressable theory](../definitions/addressable-theory.md) — defined-in: the structural property the addressability conjecture is about
- [An experiment identifies only the contrast it actually runs](../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — grounds: why withholding a theory does not test its content
- [Learning by theory refinement may improve sample efficiency under structured shifts](../../../notes/learning-by-theory-refinement-may-improve-sample-efficiency.md) — see-also: the payoff conjecture under structured shifts, a different question from the two stated here
- [Popper, Epistemology without a knowing subject](../../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md) — evidenced-by: the two levels, conscious criticism, mutual criticism, and knowledge that needs no holder
- [Popper, Conjectures and Refutations](../../../sources/popper-conjectures-and-refutations.ingest.md) — evidenced-by: tests that implicate a whole system, and the criticism of instrumentalism
