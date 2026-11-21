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
   of the learning loop. A judgment by one fixed measure is the special case.
3. **Open to criticism.** The judgment is held as a conjecture. Later rounds
   of the same loop can bring evidence against that particular judgment and
   find it wrong. The system then corrects: it undoes the change where that
   is possible, and otherwise makes a further change.

The conditions apply to a named system and the store it changes. They are
checked on the outermost loop that the system runs itself.

The KB needs the term to put all the learning that happens in Commonplace
under one name.

A system that learns this way is a **deliberative learner**.

Deliberative learning is **single-loop** when the system cannot question the
measure it judges by, and **double-loop** when a loop inside the system can
criticize and revise that measure. Both are deliberative learning.

The term names a way of learning. It has no success condition. A system whose
retained changes do not improve its later work is still doing deliberative
learning, as a reinforcement learning run that learns nothing is still
reinforcement learning. Whether a particular change was learned is a separate
claim, defined below.

### The system, the store and the loop

A claim of deliberative learning names a system and the store it changes.
Systems have loops inside loops, and the answer depends on the loop.

- **A team that trains models runs two loops.** Gradient training keeps its
  changes in weights, which are not a legible store, and fails the first
  condition. The
  researchers change code, configurations and papers by their own judgment of
  what worked, and meet it. So the research is deliberative learning done by
  people, and the training inside it is not.
- **A loop with a fixed measure may sit inside one that revises the
  measure.** Both are deliberative learning if each meets the three
  conditions. Which one a claim is about depends on the named system. In
  Commonplace the loop that writes and revises validators is part of the
  system.
- **Who judges is not fixed.** People, language models or both can make and
  criticize the judgments. A human engineering team does deliberative
  learning. In Commonplace's bootstrap, people make some of the judgments.
- **The autonomous claim is about the outermost loop.** It says that a
  language model can run that loop, so that no person is needed inside the
  system's boundary. For Commonplace's work no adequate fixed measure is
  known, so the claim is about double-loop learning: the judge must read the
  store and judge on balance with no measure given to it. Whether a language model's judgments are good
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
  balance whether a new model version is better. That judgment does not
  decide which weight updates are kept, so it is outside the training loop.
- **A fixed measure is the special case.** When the system treats one
  measure as the only one, the on-balance judgment reduces to that measure.
  A change kept because a validator passed meets the condition. So does a
  rule kept because one formula scored it above zero. The operator's reason:
  the definition should be general and continuous, so that a small change
  to how a system judges does not move it out of the term.
- **Single-loop and double-loop name a property, not a condition.** A
  single-loop learner applies a measure it cannot examine. A double-loop
  learner can ask whether the measure is right for the work, change it, or
  judge without one. A system moves from the first kind to the second by
  gaining a loop that revises the measure. How well it then uses that loop
  is a matter of degree.
- **The words are Argyris's, used more narrowly.** In
  [his account](../../sources/argyris-organizational-learning-and-mis-1977.ingest.md)
  single-loop learning corrects errors while "the underlying program is not
  questioned", and double-loop learning questions "the underlying objectives
  and policies". Here double-loop requires only that the measures, gates and
  checks that decide retention can be questioned. The declared objective
  they serve may stay fixed.
- **Two nested loops are not double-loop learning.** A training run inside a
  search over its settings has two loops. It is single-loop if the search
  keeps settings by a score that nothing in the system can question.

**Open to criticism.**

- **Later evidence must be able to count against the kept change.** A loop
  that replaces a prompt whenever a new variant scores higher overwrites its
  earlier choice. It does not find that choice wrong. PRODIGY does: it
  revises its estimate of one retained rule from later use and drops the
  rule when the estimate turns negative. A gate that admits a change once
  and never looks at it again fails this condition. So does a system that
  keeps everything.
- **The condition is about the judgment, not the change.** It does not
  require that a change can be undone. Commonplace deletes things, and a
  deletion cannot always be restored. The condition requires that the
  judgment can still be found wrong. The system can then record the error and
  change what it does next.
- **Reversibility enters the judgment in condition 2.** Suppose a new routing
  instruction saves searches but sometimes sends an agent to the wrong note.
  Removing the instruction cannot recover time already lost. If the system
  can recognize the mistake and remove the instruction, fewer later tasks
  need suffer it. That prospect can tip the judgment in favour of keeping
  the instruction now. It is not evidence that the instruction has improved
  later work. See [how reversibility limits future loss](../../theory/reversibility-can-favor-a-change-by-limiting-future-loss.md).

### When a change was learned

A retained change was **learned** when the system that has it is better, on
balance, at its future work than the system without it. "On balance" has the
meaning given in the on-balance note: for every reasonable measure of that
capacity, the system with the change scores higher. No measure is selected.

Report the comparison for one change:

- **Learned.** Every reasonable measure favors the system with the change.
- **Made worse.** Every reasonable measure favors the system without it.
- **Tie.** Every reasonable measure rates the two systems equally. There is
  no gain for the declared work, but no loss either.
- **Better on some measures, tied on the rest.** Report the gain and its
  limit, not that the change was learned. Likewise report a loss on some
  measures with ties on the rest without implying a loss on all measures.
- **Open.** Some measures favor each system, or the evidence has not arrived.
  Say which.

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
- **Retention without a judgment.** A change kept by default, with no
  judgment that could later be found wrong, is outside the term. A log that
  appends every interaction is an example.
- **A claim about what Commonplace adds.** Symbolic learners that kept rules
  by a fixed formula, and corrected those judgments from use, were
  single-loop deliberative learners. Commonplace's conjecture is about
  capability: that a language model can run double-loop deliberative
  learning for work where no fixed measure is adequate.
- **A claim of success.** Calling a system's learning deliberative does not
  say the system has learned anything.

### Misuse

- Citing the name as evidence that a system improves.
- Reporting a kept change as learned while its verdict is open.
- Using "deliberative learning" for the system. The system is a
  deliberative learner.
- Calling a system double-loop because it has two nested loops.
- Reading "double-loop" as Argyris's full sense, in which the objective
  itself is questioned.
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
- **The deliberative learner and the deliberative agent.** In agent
  architectures a deliberative agent has an explicitly represented, symbolic
  model of the world and decides by logical reasoning over it
  ([Wooldridge and Jennings](../../sources/wooldridge-jennings-intelligent-agents.ingest.md)).
  The two terms are contrasted on what is known so far:
  - the agent deliberates about which action to take, and the learner about
    which changes to its own store to keep;
  - the agent's representation is symbolic, and the learner's store is
    legible prose, structured text and code;
  - the agent's model is a world model, and the learner's store holds partial
    theories, procedures and constraints, with most knowledge of the world
    in a language model's weights.

  Whether a deliberative learner is a deliberative agent is left open. The
  contrast rests on one survey. That tradition may hold work closer to
  Commonplace than the survey shows: it mentions an architecture, IRMA, with
  a "deliberation process" that chooses between options with no stated
  criterion, and Soar and PRODIGY were deliberative in its sense and learned.
- **The closest symbolic precedent.** PRODIGY kept a learned rule only while
  its estimated utility was positive, and revised the estimate from use
  ([Minton](../../sources/minton-utility-of-ebl-aaai88.ingest.md)). It had a
  judgment of improvement inside its loop and was a single-loop deliberative
  learner: one formula, with no way to ask whether time was the only thing
  that mattered. Minton chose and revised the formula, so PRODIGY together
  with Minton was a double-loop learner.
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

The open questions about this draft are listed in
[the workshop README](./README.md#open-questions-about-the-definition).
[The comparison of earlier systems](./precedents.md) extends the background
above with five more ingests.
