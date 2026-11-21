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
2. **Judgment in the loop.** Whether later work relies on a change is
   decided by an
   [on-balance judgment](../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md)
   that relying on it improves the system's future work. The judgment is a
   step of the learning loop. A judgment by one fixed measure is the special
   case.
3. **Open to criticism.** Continued reliance is held as a conjecture.
   Evidence from later use can count against continuing to rely on a change,
   reducing or ending reliance on it rather than merely displacing it when a
   higher-scoring alternative appears. The system then corrects: it reduces
   reliance or undoes the change where that is possible, and otherwise makes
   a further change.

The conditions apply to a named system and the store it changes. They are
checked on the outermost loop that the system runs itself.

The KB needs the term to put all the learning that happens in Commonplace
under one name.

A system that learns this way is a **deliberative learner**.

A **single-loop** learner revises reliance on changes under a criterion it
cannot revise. A **double-loop** learner can also revise the criterion that
governs reliance on those changes. Name the class of changes: the test is
whether a different standard can govern later decisions of that kind. Both
are deliberative learning. This is a capacity, not a claim about every run.

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
  known. The conjecture is that a language model can recognize and revise
  misleading criteria well enough without a person making that judgment.

### Notes on the conditions

**Legible store.**

- **Any kind of change counts.** A theory in a note, an instruction, a type,
  a validator, a code change and a deletion are all covered.
- **Legibility enables targeted criticism.** Later evidence indicts an
  operating state, not one line in isolation. In an opaque store, correction
  can only roll back a whole bundle or replace the model. A legible and
  [addressable](../../theory/definitions/addressable-theory.md) store lets
  later rounds point at a particular change, trace its use, and reduce
  reliance on it without undoing unrelated changes.

**Judgment in the loop.**

- **The judgment must be the step that decides reliance.** People also judge
  on balance whether a new model version is better. That judgment does not
  decide which weight updates are kept, so it is outside the training loop.
  Admission, reliance and continued storage are distinct: a change can remain
  archived in the store while later work stops relying on it.
- **A fixed measure is the special case.** When the system treats one
  measure as the only one, the on-balance judgment reduces to that measure.
  A change kept because a validator passed meets the condition. So does a
  rule kept because one formula scored it above zero. The operator's reason:
  the definition should be general and continuous, so that a small change
  to how a system judges does not move it out of the term.
- **Distinguish the criterion from its implementation.** Dropping an
  instruction because it fails a validator applies the existing criterion.
  Revising what the validator accepts because passing instructions hurt
  later work changes the criterion. Making the same test faster does not.
  Neither a proof nor an LLM judgment decides the kind by itself.
- **The words are Argyris's, used more narrowly.** In
  [his account](../../sources/argyris-organizational-learning-and-mis-1977.ingest.md)
  single-loop learning corrects errors while "the underlying program is not
  questioned", and double-loop learning questions "the underlying objectives
  and policies". Here double-loop requires only that the measures, gates and
  checks that decide retention can be questioned. The declared objective
  they serve may stay fixed.
- **Authorization is not the successor criterion.** Evidence can show a
  proxy fails its objective. It cannot by itself declare a new ultimate end
  ([objective revision](../../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md)).
  But the old criterion can authorize installing a different one. Ask what
  standard governs subsequent choices, not whether the switch needed approval.
- **The classical Gödel machine is double-loop capable.** In
  [Schmidhuber's construction](../../sources/goedel-machines-schmidhuber.ingest.md)
  (§6.1 items 2 and 4; §6.7 FAQ 7), new observations can end a trial, and
  the current utility function can license rewriting that function and the
  target theorem. A rewrite that changes how future alternatives rank is a
  criterion revision. Speeding up proof search for the same ranking is not.
  The construction permits the first kind without requiring a separate
  policy-level gate or showing that a particular run found the required proof.
- **Two nested loops are not double-loop learning.** A training run inside a
  search over its settings has two loops. It is single-loop if the search
  keeps settings by a score that nothing in the system can question.

**Open to criticism.**

- **Later evidence must be able to count against continued reliance.** A loop
  that replaces a prompt whenever a new variant scores higher on a fixed test
  only displaces its earlier choice; no post-admission evidence indicts the
  kept variant. Likewise, an archive whose entries keep a fixed admission
  score and lose selection weight only through dilution as new challengers
  arrive fails this condition. PRODIGY passes: it revises its estimate of one
  retained rule from later use and drops the rule when the estimate turns
  negative. So does a system that reduces reliance on an admitted variant
  when its descendants perform poorly. A gate that admits a change once and
  never lets later evidence count against it fails this condition. So does a
  system that keeps and relies on everything unconditionally.
- **Correction targets continued reliance, not necessarily the original
  decision.** A reversible trial that turns out poorly was not necessarily a
  mistake given what was known at admission. The condition requires that
  later evidence can end reliance on the change, not that the system condemn
  its earlier decision to try it. The evidence need not come from re-running
  the admission test; downstream task failures or descendant outcomes also
  count.
- **Attribution is graded.** At the minimum, later evidence can indict a
  retained state and roll back a bundle or stack of changes since a baseline
  (as in Schmidhuber's incremental self-improvement). Pinning the loss to one
  particular change while keeping the rest is a graded capability enabled by
  an addressable store (condition 1).
- **The condition is about reliance and judgment, not undoability.** It does
  not require that a change can be undone. Commonplace deletes things, and a
  deletion cannot always be restored. The condition requires that later
  evidence can still show that continuing to rely on the change, or on the
  rule that produced it, is wrong, so the system can record the error and
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
- Calling a learner double-loop merely because it has nested loops, rewrites
  code or judges in prose; calling it single-loop merely because it uses a
  proof or the old criterion authorizes its replacement.
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
above with eight more ingests.
