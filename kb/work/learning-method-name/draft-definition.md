# Draft: deliberative learning

Drafted 2026-11-21 by an agent (claude-fable-5-2) from the operator's rulings
of that day, recorded in [the workshop framing](./README.md). It is a
workshop draft. Its destination would be
`kb/theory/definitions/deliberative-learning.md`. On the operator's
instruction, the sources are kept as short background and the definition
does not depend on them.

---

## Deliberative learning

**Deliberative learning** is learning that meets three conditions:

1. **Legible store.** What is learned is kept as changes to a store that can
   be read: prose, structured text and code.
2. **Judgment in the loop.** Each change is kept or dropped by an
   [on-balance judgment](../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md)
   that the change improves the system's future work. The judgment is a step
   of the learning loop. It is not bound to one measure fixed beforehand.
3. **Open to criticism.** The judgment is held as a conjecture. Later rounds
   of the same loop can criticize it and find it wrong. The system then
   corrects: it undoes the change where that is possible, and otherwise makes
   a further change.

The conditions apply to a named system and the store it changes. They are
checked on the outermost loop that the system runs itself.

The KB needs the term to put all the learning that happens in Commonplace
under one name.

The term names a way of learning. It has no success condition. A system whose
retained changes do not improve its later work is still doing deliberative
learning, as a reinforcement learning run that learns nothing is still
reinforcement learning. Whether a particular change was learned is a separate
claim, defined below.

### The system, the store and the loop

A claim of deliberative learning names a system and the store it changes.
Systems have loops inside loops, and the answer depends on the loop.

- **A team that trains models runs two loops.** Gradient training changes
  weights under a loss chosen beforehand, and fails the definition. The
  researchers change code, configurations and papers by their own judgment of
  what worked, and meet it. So the research is deliberative learning done by
  people, and the training inside it is not.
- **A loop with a fixed measure may sit inside a deliberative one.** What
  matters is whether the named system runs the outer loop itself. In
  Commonplace the loop that writes and revises validators is part of the
  system.
- **Who judges is not fixed.** People, language models or both can make and
  criticize the judgments. A human engineering team does deliberative
  learning. In Commonplace's bootstrap, people make some of the judgments.
- **The autonomous claim is about the outermost loop.** It says that a
  language model can run that loop, so that no person is needed inside the
  system's boundary. The judge must then read the store and judge on balance
  with no measure given to it. Whether a language model's judgments are good
  enough is the conjecture under test.

### Notes on the conditions

**Legible store.**

- **Any kind of change counts.** A theory in a note, an instruction, a type,
  a validator, a code change and a deletion are all covered.
- **Legibility makes the second condition possible.** A judgment about one
  change can be made and contested only if the change can be read and pointed
  at. In weights, only the whole model can be judged.

**Judgment in the loop.**

- **The judgment must be the step that retains.** People also judge on
  balance whether a new model version is better. That judgment is outside the
  training loop, which retains whatever lowers its loss.
- **A deterministic check is a degenerate on-balance judgment.** Where one
  measure is the only reasonable one for a question, such as whether a link
  resolves, the on-balance judgment reduces to that measure. So a change kept
  because a validator passed meets the condition. What must stay open is the
  claim that this one measure is enough for the question.

**Open to criticism.**

- **The condition is about the judgment, not the change.** It does not
  require that a change can be undone. Commonplace deletes things, and a
  deletion cannot always be restored. The condition requires that the
  judgment can still be found wrong. The system can then record the error and
  change what it does next.
- **Reversibility decides how much support a judgment needs.** A change that
  can be undone may be kept while its verdict is open. A change that cannot
  be undone needs more support first, as
  [the irreversible-step case](../bounding-omitted-effects/further-cases.md#case-d--a-step-that-cannot-be-undone)
  argues. So reversibility belongs to the practice of deliberation and is not
  a condition of the term.

### When a change was learned

A retained change was **learned** when the system that has it is better, on
balance, at its future work than the system without it. "On balance" has the
meaning given in the on-balance note: for every reasonable measure of that
capacity, the system with the change scores higher. No measure is selected.

Three verdicts are possible for one change:

- **Learned.** Every reasonable measure favours the system with the change.
- **Not learned.** Every reasonable measure favours the system without it.
- **Open.** Reasonable measures disagree, or the evidence has not arrived.

Three points govern use of the verdicts.

- **"Open" is the usual verdict for a recent change.** The capacity in
  question is for work not yet done, so the evidence comes from later
  episodes.
  [Compounding is tested the same way](../../theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md).
- **Keeping a change is not the same as having learned it.** A system may
  keep a change whose verdict is open, most safely when the change can be
  undone. That is a decision. It is reported as a decision until the verdict
  is in.
- **The claim is about one change in a declared area of work.** "This system
  learns" is a summary of such claims, and is no stronger than they are.

### What the term does not cover

- **Learning in general.** Learning in
  [Simon's sense](../../theory/learning-is-not-only-about-generality.md) is
  any lasting change in capacity. Gradient training produces it under a fixed
  loss. Deliberative learning is one way of learning among several.
- **Retention bound to a fixed measure.** A system that keeps or drops
  changes by one formula, and cannot question whether that formula is the
  right one, fails the second condition, even if it revises its estimates
  from use.
- **Retention without a judgment.** A change kept by default, with no
  judgment that could later be found wrong, is outside the term.
- **A claim of success.** Calling a system's learning deliberative does not
  say the system has learned anything.

### Misuse

- Citing the name as evidence that a system improves.
- Reporting a kept change as learned while its verdict is open.
- Using the term for the system. The system is a
  [theory builder](../../theory/definitions/theory-builder.md).
- Using the term only for theories stored in language.

### Background

The definition above stands without this section. The four sources are
ingests with no retained quotes yet.

- **The word.** "Deliberate" comes from Latin *deliberare*, which
  [Merriam-Webster](https://www.merriam-webster.com/dictionary/deliberate)
  derives, with a "perhaps", from *librare*, "to balance", and *libra*, "a
  pair of scales". So "deliberative" and "on balance" share an image. The KB
  uses "on balance" for the verdict and "deliberation" for the process that
  reaches it.
- **Deliberation.** The ordinary concept is the weighing of considerations
  for and against alternatives, by
  [one agent](../../sources/sep-practical-reason.ingest.md) or
  [a group](../../sources/fishkin-mansbridge-deliberative-democracy-intro.ingest.md).
  Neither source covers keeping the outcome or revising it from later
  evidence. Those are the first and third conditions, and they are what
  "learning" adds.
- **Not the deliberative agent.** In agent architectures the term means an
  agent that plans over a symbolic model of the world
  ([Wooldridge and Jennings](../../sources/wooldridge-jennings-intelligent-agents.ingest.md)).
  The term here is not taken from that use. Commonplace's store is not
  symbolic and is not a world model.
- **The closest symbolic precedent.** PRODIGY kept a learned rule only while
  its estimated utility was positive, and revised the estimate from use
  ([Minton](../../sources/minton-utility-of-ebl-aaai88.ingest.md)). It had a
  judgment of improvement inside its loop. Taken alone it fails the second
  condition: it was bound to one formula, and could not ask whether time was
  the only thing that mattered. Taken together with Minton, who chose and
  revised the formula, it was deliberative learning.
- **Why symbolic systems needed a fixed measure.** The operator's account:
  the same definition of "learned" would serve for a symbolic system, but
  applying it would be unworkable. Choosing reasonable measures takes
  judgment, and so does scoring a single case, where a symbolic system would
  need an enormous array of explicit tests.
- **The earlier name.** "Conjectural learning" was dropped because it could
  be read as saying that knowledge is stored as conjectures. The intended
  sense, that the judgments of improvement are conjectures, is now the third
  condition.

---

## Notes for the operator

- **One file or two.** "Learned" is drafted as a section of this definition.
  It could instead be a section of the on-balance note.
- **Consumers not yet listed.** The theory-builder definition, the research
  companion, the lead article's "distinct learning paradigm" section, the
  `AGENTS.md` vocabulary table and the collision ledger, which has no entry
  for "deliberative".
