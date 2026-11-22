---
description: "Definition — for a named class of changes, a system that learns by a proposal-selection loop is single-loop when it cannot revise the criterion that decides them and double-loop when it can; narrower than Argyris's sense"
type: types/definition.md
tags: [self-improving-systems, learning-theory, improvement-loop]
---

# Single-loop and double-loop learning

A system that learns by a
[proposal-selection improvement loop](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md)
decides each proposed change by a criterion: a single measure, a gate, a
check, a formula, or a comparison across several measures. For a named class of
changes, the learner is **single-loop** when it decides those changes under
a criterion it cannot revise, and **double-loop** when it can revise that
criterion so that a different criterion governs later decisions of that
class. Such a system is a
[selection-based learner](./selection-based-learning.md) that does its own
selecting, and the distinction applies whether its criterion is one measure
or several.

The distinction matters because a single-loop learner cannot recover from a
misleading criterion. It keeps applying the criterion however often changes
that passed it turn out badly.

## Scope

- **Applying or speeding up versus revising.** Dropping an instruction
  because a validator rejects it applies the existing criterion. Making the
  validator run faster checks the same criterion sooner. Revising what the
  validator accepts, because instructions that passed it kept misrouting
  agents, changes the criterion for later instructions.
- **Several measures.** A learner that compares across several measures
  can count a new one in any single decision. It is
  double-loop only when a change
  in what counts, or how much, is retained and governs later decisions of
  that class. A team deciding that context cost now counts against every
  routing rule is an example. A team that happens to mention context cost
  in one decision is not.
- **Scoped to one class.** A team paired with a link repairer is double-loop
  for *link repairs* when it can revise the repairer's validator. Whether it
  can also revise how it judges *validator edits* is a separate question.
- **Depends on the named system.**
  [PRODIGY](../../sources/minton-utility-of-ebl-aaai88.ingest.md) alone was
  single-loop: it kept or dropped rules by a utility formula it could not
  change. PRODIGY together with Minton, who chose and revised that formula,
  was double-loop.

A claim of double-loop capacity says what can bring the criterion into
question, what considers it, and what change to the criterion can follow.

## Exclusions

- **Nested loops.** A hyperparameter search wrapped around a training run
  has two nested loops and stays single-loop if one fixed validation score
  governs every pick.
- **A different verdict under the same criterion.** In
  [EURISKO](../../sources/eurisko-learns-new-heuristics-and-domain-concepts.ingest.md),
  dropping one badly generalized heuristic changes one item and is
  single-loop. Retaining a restriction that penalizes future generalizations
  of that shape before they run revises the criterion and is double-loop.
- **A successor that ranks nothing differently.** In
  [Schmidhuber's Gödel machine](../../sources/goedel-machines-schmidhuber.ingest.md),
  proving under the current utility function that a successor utility
  function should be installed is double-loop only when that successor ranks
  later alternatives differently.
- **Argyris's full sense.** The terms are borrowed from
  [Argyris](../../sources/argyris-organizational-learning-and-mis-1977.ingest.md)
  and used more narrowly. In his account, single-loop learning corrects
  errors while "the underlying program is not questioned", and double-loop
  learning questions "the underlying objectives and policies". Here
  double-loop requires only that the working criterion can be revised. A
  learner can keep its declared objective fixed while revising the gates and
  validators that serve it, because
  [revising the objective itself needs a licence from outside it](../revising-an-improvement-objective-is-licensed-from-outside-it.md).

## Misuse Cases

- Using either term without naming the class of changes.
- Reading *double-loop* in Argyris's full sense, as questioning the terminal
  objective.
- Calling a learner double-loop because it has two loops, or because it
  reversed one earlier decision.
- Calling a system double-loop when the criterion is revised only by people
  outside the named system.

---

Relevant Notes:

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: the loops these two kinds divide
- [Selection-based learning](./selection-based-learning.md) — defined-in: the learning these two kinds divide
- [Revising an improvement objective is licensed from outside it or is not improvement](../revising-an-improvement-objective-is-licensed-from-outside-it.md) — grounds: why double-loop revision stops at the working criterion
