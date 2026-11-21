# Draft: deliberative learning

A workshop draft by an agent (claude-fable-5-2), revised with Neon and Astra
from the operator's rulings of 2026-11-21. Its destination would be
`kb/theory/definitions/deliberative-learning.md`. The history of the wording
is in [the rulings](./rulings.md) and not in this file.

---

## Deliberative learning

**Deliberative learning** is learning that meets two conditions:

1. **Legible, addressable store.** What is learned is held in the contents
   of a store that can be read and pointed at: prose, structured text and
   code. The store is the system's own: its later work consumes those
   contents. The system learns by changing them.
2. **Decision in the loop.** A change to the store is proposed, judged and
   can be rejected. The judgment is an
   [on-balance judgment](../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md),
   on the evidence the system has, of whether it will do its later work
   better with the change than without it. The judgment is a step of the
   learning loop. A judgment that applies one fixed criterion is the special
   case.

A system that learns this way is a **deliberative learner**.

A **change** is an edit to the store's contents: adding, revising, removing
or moving something, including an edit to what later work loads or selects.
The store holds contents, not changes. A proposal or a diff kept in the
store is a document about a change.

A **criterion** is what a judgment applies to decide. It may be one measure,
a gate, a check, or the open set of considerations a judge weighs.

### What a claim names

A claim of deliberative learning names four things:

- **The system**, including which people and programs are inside it.
- **The store** it changes.
- **The class of changes** the claim is about. A system can make some
  changes by decision and others automatically. The conditions are checked
  for the named class, on the loop that makes those changes.
- **The horizon** over which later work is counted.

The claim is about a capacity unless it says otherwise. To claim that a
system did deliberative learning in a particular episode, show the proposal,
the judgment and the later use.

### Kinds and properties

A learner is **single-loop** for a class of changes when it decides those
changes under a criterion it cannot revise. It is **double-loop** when it can
also revise that criterion, so that a different criterion governs later
decisions of that kind. Both are deliberative learning.

Two properties are reported for a learner. They are not conditions.

- **Correction from later evidence.** Can evidence from later use change
  what the system does about an earlier change? If it can, can the system
  identify the responsible change, or only reverse everything since a
  baseline? The answers are *none*, *bundle* and *targeted*.
- **Displacement.** Can a newer alternative replace an earlier change by
  doing better under the same criterion, with no new evidence about the
  earlier change? This is independent of correction. A system can have
  either without the other.

A later change can correct an earlier one when the loop can write such an
edit and whatever consumes the store gives it effect. An addressable store
makes that possible. It does not guarantee it.

### Place among the KB's terms

A deliberative learner is a
[self-improving system](../../theory/definitions/self-improving-system.md)
that works by
[proposal and selection](../../theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md)
over a legible, addressable store. The term adds four things to that
description:

- the selection may be an on-balance judgment with no single measure;
- the kinds single-loop and double-loop, and the properties of correction
  and displacement;
- the verdict "learned" for one change, defined below;
- the inclusion of changes to what later work loads or selects.

The term names a way of learning. It has no success condition. A system
whose changes do not improve its later work is still doing deliberative
learning, as a reinforcement learning run that improves nothing is still
reinforcement learning.

## Notes

### The store

- **Any kind of change counts.** Adding a theory to a note, revising an
  instruction, a type or a validator, changing code, deleting a note and
  changing what agents load are all covered.
- **Legibility and addressability do different work.** Legibility lets a
  judge read what is in the store. Being
  [addressable](../../theory/definitions/addressable-theory.md) lets a later
  change point at what an earlier change put there, trace its use, and
  alter it or tell later work to disregard it, without undoing unrelated
  changes. In an opaque store, correction can only roll back a whole bundle
  or replace the model.
- **The store is not the product.** The definition of
  [behavior-determining organization](../../theory/definitions/behavior-determining-organization.md)
  gives the test: the contents count when the system's own later operation
  consumes them. An output that is delivered and not used again by the
  system does not count. A program that repairs links in documents which
  only readers use has no store of its own in those documents.
- **Loading is not consuming.** A claim about capacity says how later work
  reads the store. A claim about an episode shows what the system did
  differently because of an entry. An agent can load a memory file on every
  task and ignore every lesson in it.
- **A change in what is used is a change to the store.** Some systems never
  delete. An instruction can be moved out of what agents load, and an
  archive can lower how often an entry is selected. Each is an edit to the
  store's contents and is judged like any other.
- **A readable pointer to an opaque thing is a thin store.** A file that
  selects which model checkpoint is deployed is legible. What the checkpoint
  holds is not. A claim about that file covers the selections and not what
  was learned inside the weights.

### The decision

- **There must be something that could be rejected.** A proposed change is
  judged, and the judgment can go against it. A rule that updates the store
  directly from an input has no proposal and no rejection. A nightly job
  that raises an article's rank when it is clicked is of that kind, and so
  is a table of values updated by reinforcement learning, even when the
  table can be read. Both are learning. Neither is deliberative.
- **Automatic storage is not a decision.** In Commonplace, adding an entry
  to `kb/log.md` is made by a decision: an agent judges that an observation
  is worth recording. Storing session traces is not: every session is
  stored. Introducing such automatic storage is itself a change that can be
  proposed, judged and later revisited. What it then writes is outside the
  term.
- **A fixed criterion is the special case.** When the system treats one
  criterion as settling whether a change is for the better, the judgment
  reduces to applying it. A repair kept because a validator passed meets
  the condition. So does a rule kept because one formula scored it above
  zero. The definition is meant to be continuous here: a small change to
  how a system judges should not move it out of the term.
- **The judgment must be the step that makes the change.** People also judge
  on balance whether a new model version is better. That judgment does not
  decide which weight updates are made, so it is outside the training loop.
- **Who judges is not fixed.** People, language models, programs or a mix
  can make the judgments. A human engineering team does deliberative
  learning.
- **A trial and its review are two judgments.** A team tries a routing rule
  for a week, with a review on Friday. The first judgment compares trying
  the rule with carrying on as before. On Friday the second compares keeping
  the rule with removing it. Both can be sound when the second goes against
  the rule: the evidence counts against letting the change stand, not
  against having made it.
- **Reversibility enters the judgment.** Suppose a new routing instruction
  saves searches but sometimes sends an agent to the wrong note. Removing
  the instruction cannot recover time already lost. If the system can
  recognize the mistake and remove the instruction, fewer later tasks need
  suffer it. That prospect can tip the judgment in favour of keeping the
  instruction now. It is not evidence that the instruction has improved
  later work. See
  [how reversibility limits future loss](../../theory/reversibility-can-favor-a-change-by-limiting-future-loss.md).

### The horizon and the loop

- **Learning is relative to a declared horizon.** The definitions of a
  [self-improving system](../../theory/definitions/self-improving-system.md)
  and of an [operative change](../../theory/definitions/operative-change.md)
  read a change against a declared horizon, and this definition follows
  them. Claims about Commonplace use a horizon that spans tasks. A library
  note, an instruction or a validator counts there. A workshop draft or a
  task plan does not.
- **A team that trains models runs two loops.** Gradient training changes
  weights, which are not a legible store, and fails the first condition.
  The researchers change code, configurations and papers by their own
  judgment of what worked, and meet both conditions. So the research is
  deliberative learning done by people, and the training inside it is not.
- **One loop may sit inside another.** A loop that applies a fixed criterion
  may sit inside a loop that revises the criterion. Each is deliberative
  learning if it meets the two conditions. Which one a claim is about
  depends on the named system and class of changes.

### Single-loop and double-loop

- **The criterion is not its implementation.** Dropping an instruction
  because it fails a validator applies the existing criterion. Revising what
  the validator accepts, because instructions that passed hurt later work,
  changes the criterion. Making the same test faster does not.
- **It is a capacity for a named class.** A team with a link repairer is
  double-loop for link repairs if it can change the validator. Whether it
  can change how it judges validator changes is a further question.
- **Neither a proof nor a language model decides the kind.** Ask whether a
  different criterion can govern later decisions, not how the judgment is
  carried out.
- **The words are Argyris's, used more narrowly.** In
  [his account](../../sources/argyris-organizational-learning-and-mis-1977.ingest.md)
  single-loop learning corrects errors while "the underlying program is not
  questioned", and double-loop learning questions "the underlying objectives
  and policies". Here double-loop requires only that the criterion by which
  changes are judged can be revised. The declared objective it serves may
  stay fixed.
- **Authorization is not the successor criterion.** Evidence can show that a
  criterion fails the objective it serves. It cannot by itself declare a new
  ultimate end
  ([objective revision](../../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md)).
  The old criterion can authorize installing a different one. Ask which
  criterion governs later choices, not whether the switch needed approval.
- **Two nested loops are not double-loop learning.** A training run inside a
  search over its settings has two loops. The search is single-loop if it
  keeps settings by a score that nothing in the system can revise.

### Correction and displacement

- **Correction: none.** A gate that admits a change once and never lets
  later evidence count against it. A memory file whose lessons are chosen by
  decision and never revised. A store whose reader always uses the first
  instruction stored under a key: a later entry can name that instruction
  exactly and say "disregard it", and the first one still governs.
- **Correction: bundle.** Later evidence counts against a state of the
  store, and the system reverses all the changes made since a baseline.
- **Correction: targeted.** A learner revises its estimate of one rule from
  later use and removes the rule when the estimate turns negative. A system
  chooses an archived variant less often when its descendants perform
  poorly. The evidence need not come from running the first test again.
  Failures in later tasks and the results of descendants count.
- **Displacement without correction.** A loop that replaces a prompt
  whenever a new variant scores higher on a fixed test displaces its earlier
  choice. No evidence from after the change bears on the variant it
  installed.
- **The grain follows the named class of changes.** Rolling back one
  deployment is targeted when the class is deployments. It is a bundle when
  the class is what changed inside the deployed model.
- **A claim about capacity needs an account, and a claim about an episode
  needs the episode.** To say that a system can correct from later evidence,
  say what brings the evidence back, who or what considers it, and which
  edit can follow. To say that it happened in a particular case, show that
  sequence.
- **Correction does not require undoing.** Commonplace deletes things, and a
  deletion cannot always be restored. Later evidence can still show the
  change, or the rule that produced it, to have been for the worse, so that
  the system records the error and changes what it does next.

## When a change was learned

A change to the store was **learned** when the system is better, on balance,
at its later work with the change than without it.

The comparison is fixed as
[the on-balance note](../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md)
requires:

- **The alternative** is the system as it now is with that one change taken
  out and everything else left as it is. This is not the system as it stood
  before the change, which also lacks every later change.
- **The work, and whose gains and losses count,** are declared.
- **The period** is the declared horizon.

"On balance" has the meaning given in that note: every reasonable measure of
the declared work scores the system with the change higher. No measure is
selected.

Report the comparison for one change:

- **Learned.** Every reasonable measure favors the system with the change.
- **Made worse.** Every reasonable measure favors the system without it.
- **Tie.** Every reasonable measure rates the two systems equally.
- **Better on some measures, tied on the rest.** Report the gain and its
  limit, not that the change was learned. Report a loss on some measures
  with ties on the rest in the same way.
- **Open.** Some measures favor each system, or the evidence has not
  arrived. Say which.

Three points govern use of the verdicts.

- **"Open" is the usual verdict for a recent change.** The work in question
  is not yet done, so the evidence comes from later episodes.
  [Compounding is tested the same way](../../theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md).
- **Letting a change stand is not the same as having learned it.** A system
  may let a change stand while its verdict is open, most safely when the
  change can be undone. That is a decision, and it is reported as a decision
  until the verdict is in.
- **The claim is about one change in a declared area of work.** "This system
  learns" is a summary of such claims, and is no stronger than they are.

## What the term does not cover

- **Learning in general.** Learning in
  [Simon's sense](../../theory/learning-is-not-only-about-generality.md) is
  any lasting change in capacity. Gradient training, automatic storage and
  direct update rules all produce it. Deliberative learning is one way of
  learning among several.
- **All the learning in Commonplace.** Commonplace stores session traces
  automatically. The term covers what Commonplace learns by decision.
- **A change that nothing could have rejected.** A log that appends every
  interaction, and a rule that updates a table directly from its input.
- **A claim that the system corrects itself.** A deliberative learner can
  have no correction from later evidence.
- **A claim of success.** Calling a system's learning deliberative does not
  say the system has learned anything.

## Misuse

- Citing the name as evidence that a system improves.
- Reporting a change as learned while its verdict is open.
- Using "deliberative learning" for the system. The system is a
  deliberative learner.
- Expecting every deliberative learner to deliberate in the ordinary sense.
  A single-loop learner with one fixed criterion applies it and weighs
  nothing.
- Calling a learner double-loop because it has nested loops, rewrites code
  or judges in prose. Calling it single-loop because it uses a proof or
  because the old criterion authorizes its replacement.
- Reading "double-loop" in Argyris's full sense, in which the objective
  itself is questioned.
- Calling a learner self-correcting because its store can be edited.
- Using the term only for theories stored in language.
- Making a claim without naming the class of changes or the horizon.

## Commonplace's conjecture

The definition admits symbolic programs, people and language models as
judges. Symbolic learners that kept rules by a fixed formula were
single-loop deliberative learners. What Commonplace tests is a claim about
capability: that a language model can do double-loop deliberative learning,
with targeted correction, for work where no fixed criterion is adequate, and
with no person inside the system making those judgments. For that work the
judge has to recognize that a criterion is misleading and say what should
replace it.

## Background

The definition above stands without this section.

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
  evidence. Keeping the outcome in a store is what "learning" adds.
  Revising it from later evidence is the property of correction.
- **The deliberative learner and the deliberative agent.** In agent
  architectures a deliberative agent has an explicitly represented, symbolic
  model of the world and decides by logical reasoning over it
  ([Wooldridge and Jennings](../../sources/wooldridge-jennings-intelligent-agents.ingest.md)).
  The agent deliberates about which action to take, and the learner about
  which changes to make to its own store. Whether a deliberative learner is
  a deliberative agent is left open.
- **Single-loop and double-loop in one episode.** In an episode
  [Lenat reports](../../sources/eurisko-learns-new-heuristics-and-domain-concepts.ingest.md),
  EURISKO dropped a heuristic that had been generalized badly. That changed
  the fate of one heuristic. It also kept a restriction against that kind of
  generalization. That changed how the next proposed generalization would be
  judged, before it had any record of its own.
- **The closest symbolic precedent.** PRODIGY kept a learned rule only while
  its estimated utility was positive, and revised the estimate from use
  ([Minton](../../sources/minton-utility-of-ebl-aaai88.ingest.md)). It was a
  single-loop deliberative learner with targeted correction: one formula,
  with no way to ask whether time was the only thing that mattered. Minton
  chose and revised the formula, so PRODIGY together with Minton was
  double-loop.
- **The proof-governed case.** In
  [Schmidhuber's Gödel machine](../../sources/goedel-machines-schmidhuber.ingest.md)
  a rewrite is admitted by proof that it has higher expected utility. New
  observations can end a trial, and the current utility function can license
  rewriting that function. A rewrite that changes how later alternatives
  rank revises the criterion, so the construction is double-loop capable.
  Commonplace replaces the proof with an on-balance judgment.
- **Why symbolic systems needed a fixed criterion.** The same definition of
  "learned" would serve for a symbolic system, but applying it would be
  unworkable. Choosing reasonable measures takes judgment, and so does
  scoring a single case, where a symbolic system would need an enormous
  array of explicit tests.

---

## Workshop notes

Not part of the definition. Open questions are in
[the workshop README](./README.md#open-questions-about-the-definition).
[The checks](./definition-checks.md) apply the definition to cases, and
[the comparison of earlier systems](./precedents.md) extends the background.
