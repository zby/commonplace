# Draft: deliberative learning

Workshop draft targeting `kb/theory/definitions/deliberative-learning.md`.
Rulings and wording history live in [rulings.md](./rulings.md).

---

## Deliberative learning

A team weighing whether to add a routing rule to its handbook, or an agent
deciding whether to revise a validator in its own codebase, is doing
**deliberative learning**. It is learning that meets two conditions:

1. **Legible, addressable store.** What the system retains is held in the
   contents of a store that can be read and pointed at: prose, structured
   text and code. The store is the system's own: its later work consumes
   those contents. The system learns by changing them.
2. **Decision in the loop.** A change to the store is proposed, judged in
   the learning loop, and can be rejected. Proposing and judging are
   separate steps: something evaluates the proposed change itself rather
   than writing automatically or on a trigger. The judgment is a decision,
   made on the evidence the system has, in the expectation that later work
   will go better with the change than without it—weighing considerations in
   the manner of an
   [on-balance judgment](../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md).
   Treating one fixed criterion as settling the matter is the special case.

A system that learns this way is a **deliberative learner**. Like
reinforcement learning, the term names a process rather than a successful
outcome: a system whose changes fail to improve its later work is still
doing deliberative learning.

Two terms run through the definition:

- A **change** is an edit to the store's contents: adding a note, revising a
  validator, deleting a rule, or changing what later work loads or selects
  (such as moving an instruction out of an agent's load list or lowering an
  archived entry's selection weight in a system that never deletes). The
  store holds contents rather than edits; a saved proposal or diff is a
  document in the store, not the edit itself.
- A **criterion** is what a judgment applies to decide: a single measure, a
  gate, a check, or an open set of considerations weighed together.

## When a change was learned

Whether a particular change improved the system is a separate verdict. A
change to the store was **learned** when the system is better, on balance,
at its later work with the change than without it.

[The on-balance note](../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md)
fixes a comparison with three choices. Because that note compares a
successor with its predecessor when deciding a step, while this verdict is
given afterwards to isolate one change, the alternative differs:

- **The alternative** is the system as it now is with that one change taken
  out and everything else left intact—not the earlier system before the
  change, which also lacks every later edit. Edits that depend on the change
  go with it, and the claim says which. Taking out a deletion means
  restoring what was deleted.
- **The work, and whose gains and losses count,** are declared.
- **The period** is the declared horizon (the span of later work under
  evaluation).

"On balance" keeps its meaning from that note: every reasonable measure of
the declared work must agree, with no single measure selected. Report the
verdict for one change as **Learned** (every reasonable measure favors the
system with the change), **Made worse** (every reasonable measure favors the
system without it), **Tie** (every reasonable measure rates them equally),
**Better on some measures, tied on the rest** (report the gain and its
limit—and the converse for losses—rather than calling the change learned),
or **Open** (some measures favor each system, or the evidence has not
arrived; say which).

Because the work lies in the future, **Open** is the usual verdict for a
recent change; evidence arrives in later episodes, just as
[compounding is tested in later improvement](../../theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md).
Letting a change stand while its verdict is open is a decision, and is
reported as a decision until the verdict is in. Each verdict attaches to one
change in a declared area of work; *"this system has learned"* is only a
summary of those verdicts.

## How the two conditions work

### The store

**Legibility** and **addressability** do different work. In a KB, legibility
lets a judge read a routing instruction, while
[addressability](../../theory/definitions/addressable-theory.md) lets a
later edit point to that specific rule, trace its use, and revise or
countermand it while keeping the rest of the file. In neural network
weights, neither holds: you cannot point to one retained lesson without
retraining or replacing the checkpoint. A deployment file that names which
checkpoint to run sits in between—it is a readable store for *deployment
choices*, not for what training changed inside the weights.

The store belongs to the system's own
[behavior-determining organization](../../theory/definitions/behavior-determining-organization.md),
not its external output. A program that repairs broken links in documents
only outside readers view has no store of its own in those documents;
Commonplace's notes and instructions count because Commonplace's own later
tasks use them.

### The decision

Condition 2 separates rejectable decisions from updates that skip judging
the proposed change:

- **Direct updates (outside).** A nightly job that bumps an article's rank
  whenever it is clicked, or a readable value table updated by tabular
  reinforcement learning, writes directly from input with no proposal and no
  rejection. Both tables can be read and pointed at, so they pass condition
  1; both are learning, and neither is deliberative.
- **Triggers (outside).** A rule that says *when* to write is not a judgment
  of *what* is written. A bot that adds a review rule whenever a class of
  bug has been reported five times, or rewrites an answer after three
  unhelpful marks, is set off by a count. It is inside only if a separate
  step then evaluates the drafted rule or rewrite and can reject it.
- **Automatic storage (outside).** In Commonplace, appending an observation
  to `kb/log.md` is deliberative because an agent judges that the
  observation is worth recording; logging every session trace is automatic.
  Deciding to introduce automatic trace logging is itself a deliberative
  change, while the traces the logger later writes are outside the term.
- **Fixed criterion (inside, special case).** Keeping a patch because a
  validator passed, or keeping a rule because a utility formula scored it
  above zero, still separates proposing from judging: the validator or
  formula evaluates a change another step produced and can reject it. Such a
  system does not weigh competing considerations; it qualifies as the
  special case of condition 2 because it treats one fixed criterion as
  settling whether the change is for the better.

Whoever judges—people, language models, programs or a mix—the judgment must
be the step that edits the store. A research team that edits code and
configurations by judgment does deliberative learning; the same team
deciding whether to release a trained model sits outside the gradient
training loop because its judgment does not decide which weight updates are
made.

## What a claim names

Every claim of deliberative learning fixes four parameters:

- **The system**, including which people and programs are inside it.
- **The store** it changes.
- **The class of changes** covered, with both conditions checked on the loop
  that makes changes of that class. A wiki that imports pages automatically
  and lets editors delete wrong ones is outside for imports and inside for
  deletions. Systems also nest loops inside loops—such as gradient training
  inside a research team's workflow, or a validator-gated repairer inside a
  team that rewrites validators—and each loop is assessed on its own named
  system and class.
- **The horizon** over which later work is counted, following
  [self-improving system](../../theory/definitions/self-improving-system.md)
  and [operative change](../../theory/definitions/operative-change.md). The
  horizon works through condition 1: contents count when later work within
  the horizon consumes them. Commonplace's claims span tasks, so a library
  note, instruction or validator counts while a workshop draft or
  single-task plan does not.

By default, a claim states a **standing capacity**: how later work reads the
store and how changes are proposed and judged. A claim that also asserts
correction from later evidence says what brings the evidence back, what
considers it, and what edit can follow.

Claiming an **episode** requires showing the concrete sequence: the
proposal, the judgment, and what the system did differently on later work.
Loading alone does not show consumption. An agent can load a memory file on
every run and ignore every lesson in it.

## Single-loop and double-loop

For a named class of changes, a deliberative learner is **single-loop** when
it decides those changes under a criterion it cannot revise, and
**double-loop** when it can revise that criterion so a different criterion
governs later decisions of that kind. Both are deliberative learning.

Contrasting examples make the boundary concrete:

- **Applying or speeding up versus revising.** Dropping an instruction
  because a validator rejects it applies the existing criterion, and making
  the validator run faster checks the same criterion sooner. Revising what
  the validator accepts—because instructions that passed it kept misrouting
  agents—changes the criterion for later instructions.
- **Open considerations.** When the criterion is an open set of
  considerations, revising it means changing what counts, or how much, for
  later decisions of that class—for example, a team deciding that context
  cost now counts against every routing rule.
- **Scoped to one class.** A team paired with a link repairer, on documents
  the team's own later work uses, is double-loop for *link repairs* when it
  can revise the repairer's validator; whether it can also revise how it
  judges *validator edits* is a separate question.
- **Nested loops versus criterion revision.** A hyperparameter search
  wrapped around a training run has two nested loops yet stays single-loop
  if one fixed validation score governs every pick. Conversely, in
  [EURISKO](../../sources/eurisko-learns-new-heuristics-and-domain-concepts.ingest.md),
  dropping one badly generalized heuristic changes one item (single-loop),
  while retaining a restriction that penalizes future generalizations of
  that shape before they run revises the criterion (double-loop). In
  [Schmidhuber's Gödel machine](../../sources/goedel-machines-schmidhuber.ingest.md),
  proving under the current utility function that a successor utility
  function should be installed is double-loop whenever that successor ranks
  later alternatives differently.

The terms borrow from
[Argyris](../../sources/argyris-organizational-learning-and-mis-1977.ingest.md),
used more narrowly. In his account, single-loop learning corrects errors
while "the underlying program is not questioned", and double-loop learning
questions "the underlying objectives and policies". Here double-loop
requires only that the working criterion can be revised; Commonplace can
keep its declared objective fixed while revising the gates and validators
that serve it
([objective revision](../../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md)).

## Correction and displacement

Two independent properties describe what happens after a change is made.
Neither is a membership condition, and a learner can have either without the
other.

**Correction from later evidence** tracks whether evidence from later use
can change what the system does about an earlier edit, and at what grain:

- *None.* A one-shot admission gate, a coding agent that decides which
  lessons to append to a memory file without ever revising them, or a
  first-write-wins key-value reader where a later `"disregard X"` entry has
  no effect. An addressable store makes correction possible only when the
  loop can write a correcting edit and the consumer gives it effect.
- *Bundle.* Later evidence counts against an operating state, and the system
  reverses every edit since a baseline—for example, a team returning its
  instructions folder to last week's commit after a batch of edits proves
  harmful, or Schmidhuber's incremental self-improvement popping a stack of
  modifications in an opaque store when payoff drops.
- *Targeted.* Later evidence pins the loss on one change while keeping the
  rest—for example,
  [PRODIGY](../../sources/minton-utility-of-ebl-aaai88.ingest.md) lowering a
  rule's utility estimate from later use and dropping it when the estimate
  turns negative, the Huxley-Gödel Machine lowering an archived ancestor's
  selection weight when its descendants perform poorly, or a team reverting
  one faulty routing rule while keeping the week's other edits. Grain
  follows the named class: rolling back a five-edit release is *bundle* for
  individual edits and *targeted* when the class is releases. As the
  descendant case shows, the evidence need not come from rerunning the first
  test. And correction need not restore deleted files: if a deletion in
  Commonplace proves harmful, the system can record the error and decide
  later deletions differently (which is also a double-loop revision if it
  revises the criterion).

**Displacement** is separate: a newer alternative replaces an earlier one by
scoring higher on the same criterion, with no new evidence about the earlier
one—as in a prompt search that overwrites the incumbent whenever a new
mutant scores higher on a fixed benchmark, or an archive whose entries keep
static admission scores.

## Place in the KB and Commonplace's conjecture

In the KB's existing vocabulary, a deliberative learner is a
[self-improving system](../../theory/definitions/self-improving-system.md)
that works by
[proposal and selection](../../theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md)
over a legible, addressable store—adding on-balance selection with no single
criterion, the single-loop and double-loop kinds, the correction and
displacement properties, and the verdict *learned*.

The definition covers symbolic programs, people and language models alike:
PRODIGY alone was single-loop with targeted correction, and PRODIGY together
with Minton (who chose and revised its utility formula) was double-loop.
**Commonplace's conjecture** is about capability within this space: that a
language model can run double-loop deliberative learning, with targeted
correction, for work where no fixed criterion is adequate and with no person
inside the system making those judgments—spotting when a criterion is
misleading and deciding what should replace it.

## Exclusions and misuse

Deliberative learning is one kind of learning in
[Simon's sense](../../theory/learning-is-not-only-about-generality.md),
alongside opaque weight updates and unjudged store updates. Membership also
excludes edits to external work products that the system's own later work
does not consume, and implies neither correction from later evidence (a
separate property) nor improvement (the separate verdict *learned*).

Avoid four recurring misuses of the vocabulary:

- Using *deliberative learning* for the system (the system is a
  *deliberative learner*), or citing the name as evidence that the system
  improved or corrects itself.
- Reporting a change as *learned* while its verdict is open, or using
  *learned* for any retained change rather than that verdict.
- Reading *double-loop* in Argyris's full sense (questioning the terminal
  objective rather than the working criterion).
- Restricting the term to prose theories (excluding code or validators), or
  omitting the class of changes and horizon.

## Background

The definition above stands without this section.

- **The word.** "Deliberate" comes from Latin *deliberare*, which
  [Merriam-Webster](https://www.merriam-webster.com/dictionary/deliberate)
  derives, with a "perhaps", from *librare* ("to balance") and *libra* ("a
  pair of scales"). The KB uses "on balance" for the verdict and
  "deliberation" for the process that reaches it.
- **Deliberation.** In
  [practical reason](../../sources/sep-practical-reason.ingest.md) and
  [deliberative democracy](../../sources/fishkin-mansbridge-deliberative-democracy-intro.ingest.md),
  deliberation is weighing considerations for and against alternatives, by
  one agent or a group. Keeping the outcome in a store is what "learning"
  adds; revising it from later evidence is the property of correction.
- **Deliberative learner versus deliberative agent.** In agent
  architectures, a deliberative agent holds an explicit symbolic world model
  and decides actions by logical reasoning over it
  ([Wooldridge and Jennings](../../sources/wooldridge-jennings-intelligent-agents.ingest.md)).
  The agent deliberates over which action to take; the learner deliberates
  over which changes to make to its own store. Whether a deliberative
  learner is a deliberative agent is left open.
- **Why symbolic systems needed a fixed criterion.** The same definition of
  "learned" would serve a symbolic system, but applying it without a fixed
  criterion would be unworkable: choosing reasonable measures takes
  judgment, and even scoring a single case would demand an enormous array of
  explicit tests.

---

## Workshop notes

Not part of the definition. Open questions are in
[the workshop README](./README.md#open-questions-about-the-definition).
[The checks](./definition-checks.md) apply the definition to cases, and
[the comparison of earlier systems](./precedents.md) extends the background.
