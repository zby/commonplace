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

A system that learns this way is a **deliberative learner**. Like
reinforcement learning, the term names a process rather than a successful
outcome: a system whose changes fail to improve its later work is still
doing deliberative learning. Whether a change improved the system is a
separate verdict (*learned*, defined below).

Two terms run through the definition:

- A **change** is an edit to the store's contents: adding a note, revising a
  validator, deleting a rule, or changing what later work loads or selects.
  The store holds contents rather than edits—a saved proposal or diff is a
  document in the store, not the edit itself.
- A **criterion** is what a judgment applies to decide: a single measure, a
  gate, a check, or an open set of considerations weighed together.

### What a claim names

Every claim of deliberative learning fixes four things: **the system**
(which people and programs are inside it), **the store** it changes, **the
class of changes** covered (checked on the loop that makes changes of that
class), and **the horizon** over which later work is counted. By default, a
claim states a standing capacity; claiming that deliberative learning
occurred in one episode requires showing the proposal, the judgment and the
later use.

## How the two conditions work

### The store

Any edit to the store's contents counts—theories in notes, instructions,
types, validators, code, deletions, or selection lists. In systems that
never delete, moving an instruction out of what agents load or lowering an
archived entry's selection weight is still an edit to the store's contents,
judged like any other.

**Legibility** and **addressability** do different work. In a KB, legibility
lets a judge read a routing instruction, while
[addressability](../../theory/definitions/addressable-theory.md) lets a
later edit point to that specific rule, trace its use, and revise or
countermand it while keeping the rest of the file. In neural network
weights, by contrast, neither holds: you cannot point to one learned lesson
without retraining or replacing the checkpoint. A deployment file that names
which checkpoint to run sits in between—it is a readable store for
*deployment choices*, not for what was learned inside the weights.

The store belongs to the system's own
[behavior-determining organization](../../theory/definitions/behavior-determining-organization.md),
not its external output. A program that repairs broken links in documents
only outside readers view has no store of its own in those documents;
Commonplace's notes and instructions count because Commonplace's own later
tasks use them. Merely loading a file is not enough for an episode claim: an
agent can load a memory file on every run and ignore every lesson in it. A
capacity claim states how later work reads the store; an episode claim shows
what the system did differently because of an entry.

### The decision

Condition 2 separates rejectable decisions from direct or automatic updates:

- **Direct updates (outside).** A nightly job that bumps an article's rank
  whenever it is clicked, or a readable value table updated by tabular
  reinforcement learning, writes directly from input with no proposal and no
  rejection. Both learn; neither is deliberative.
- **Automatic storage (outside).** In Commonplace, appending an observation
  to `kb/log.md` is deliberative because an agent decides it is worth
  recording; logging every session trace is automatic. Deciding to introduce
  automatic trace logging is itself a deliberative change, while the traces
  the logger later writes are outside the term.
- **Fixed criterion (inside, special case).** Keeping a patch because a
  validator passed, or keeping a rule because a utility formula scored it
  above zero, still proposes and can reject the change. Admitting a single
  criterion keeps the definition continuous across small shifts in how a
  system judges.

The judgment must be the step that edits the store, whoever makes it—people,
language models, programs or a mix. A research team that edits code and
configurations by judgment does deliberative learning; the same team
deciding whether to release a trained model sits outside the gradient
training loop because its judgment does not decide which weight updates are
made.

A trial and its later review are two separate judgments. Suppose a team
tries a routing rule for a week and reviews it on Friday: Monday's judgment
compares trying the rule against doing nothing, and Friday's compares
keeping it against removing it. Both judgments can be sound even if Friday
removes the rule, because the week's evidence counts against letting the
change stand, not against having tried it.
[Reversibility](../../theory/reversibility-can-favor-a-change-by-limiting-future-loss.md)
enters Monday's judgment by bounding future harm: removing a bad rule cannot
recover time already lost, but knowing the system can spot and remove it
limits losses on later tasks and can tip the balance toward trying it.

### Horizons and nested loops

Following [self-improving system](../../theory/definitions/self-improving-system.md)
and [operative change](../../theory/definitions/operative-change.md),
learning is read against a declared horizon. Commonplace's claims span
tasks, so a library note, instruction or validator counts while a workshop
draft or single-task plan does not.

Systems often nest loops inside loops: a gradient training run inside a
research team's workflow, or a validator-gated repair loop inside a team
that rewrites validators. Each loop is assessed on its own named system and
class of changes.

## Single-loop and double-loop

For a named class of changes, a deliberative learner is **single-loop** when
it judges those changes under a criterion it cannot revise, and
**double-loop** when it can revise that criterion so a different criterion
governs later decisions of that kind. Both are deliberative learning.

Contrasting examples make the boundary concrete:

- **Applying or speeding up versus revising.** Dropping an instruction
  because a validator rejects it applies the existing criterion, and making
  the validator run faster checks the same criterion sooner. Revising what
  the validator accepts—because instructions that passed it kept misrouting
  agents—changes the criterion for later instructions.
- **Scoped to one class.** A team paired with a link repairer is double-loop
  for *link repairs* when it can revise the repairer's validator; whether it
  can also revise how it judges *validator edits* is a separate question.
- **Same mechanism, different kind; different mechanism, same kind.** A
  hyperparameter search wrapped around a training run has two nested loops
  yet stays single-loop if one fixed validation score governs every pick.
  Conversely, in
  [EURISKO](../../sources/eurisko-learns-new-heuristics-and-domain-concepts.ingest.md),
  dropping one badly generalized heuristic changes one item (single-loop),
  while retaining a new restriction that penalizes future generalizations of
  that shape before they run revises the criterion (double-loop). Similarly,
  in [Schmidhuber's Gödel machine](../../sources/goedel-machines-schmidhuber.ingest.md),
  a proof under the current utility function can authorize installing a
  successor utility function that ranks later alternatives differently; what
  matters is that a different criterion governs subsequent choices, not
  whether the old criterion approved the switch or whether the judge used a
  proof instead of a language model.

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
  reverses every edit since a baseline—for example, Schmidhuber's
  incremental self-improvement popping a whole stack of modifications when
  payoff drops, or rolling back an entire model deployment when the named
  class is the edits inside the model.
- *Targeted.* Later evidence pins the loss on one change while keeping the
  rest—for example,
  [PRODIGY](../../sources/minton-utility-of-ebl-aaai88.ingest.md) lowering a
  rule's utility estimate from later use and dropping it when the estimate
  turns negative, the Huxley-Gödel Machine lowering an archived ancestor's
  selection weight when its descendants perform poorly, or rolling back one
  deployment when the named class is deployments. As the descendant case
  shows, the evidence need not come from rerunning the first test. And
  correction need not restore deleted files: if a deletion in Commonplace
  proves harmful, the system can record the error and change the rule that
  triggered it.

**Displacement** is separate: a newer alternative replaces an earlier one by
scoring higher on the same criterion, with no new evidence about the earlier
one—as in a prompt search that overwrites the incumbent whenever a new
mutant scores higher on a fixed benchmark, or an archive whose entries keep
static admission scores.

Claiming a capacity for correction requires naming what brings evidence
back, what considers it, and what edit can follow; claiming an episode
requires showing that sequence.

## When a change was learned

A change to the store was **learned** when the system is better, on balance,
at its later work with the change than without it. Following
[the on-balance note](../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md),
three choices fix the comparison:

- **The alternative** is the system as it now is with that one change taken
  out and everything else left intact—not the earlier system before the
  change, which also lacks every later edit.
- **The work, and whose gains and losses count,** are declared.
- **The period** is the declared horizon.

"On balance" keeps its meaning from that note: every reasonable measure of
the declared work scores the system with the change higher, with no single
measure selected. Report the comparison for one change as one of five
verdicts:

- **Learned.** Every reasonable measure favors the system with the change.
- **Made worse.** Every reasonable measure favors the system without it.
- **Tie.** Every reasonable measure rates the two systems equally.
- **Better on some measures, tied on the rest.** Report the gain and its
  limit rather than calling the change learned; report a loss on some
  measures with ties on the rest in the same way.
- **Open.** Some measures favor each system, or the evidence has not
  arrived. Say which.

Because the work lies in the future, **Open** is the usual verdict for a
recent change; evidence arrives in later episodes, just as
[compounding is tested in later improvement](../../theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md).
Letting a change stand while its verdict is open—safest when the change can
be undone—is a decision, and is reported as a decision until the verdict is
in. Each verdict attaches to one change in a declared area of work; *"this
system learns"* is only a summary of those verdicts.

## Place in the KB and Commonplace's conjecture

In the KB's existing vocabulary, a deliberative learner is a
[self-improving system](../../theory/definitions/self-improving-system.md)
that works by
[proposal and selection](../../theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md)
over a legible, addressable store. The term adds four specifics: selection
may be an on-balance judgment with no single measure; learners are further
classified by single-loop versus double-loop capacity and by correction and
displacement; each change carries the verdict *learned*; and edits to what
later work loads or selects count as changes to the store.

The definition covers symbolic programs, people and language models alike;
PRODIGY, with its fixed utility formula, was a single-loop deliberative
learner with targeted correction (and double-loop together with Minton, who
revised the formula). **Commonplace's conjecture** is about capability
within this space: that a language model can run double-loop deliberative
learning, with targeted correction, for work where no fixed criterion is
adequate and with no person inside the system making those judgments—spotting
when a criterion is misleading and deciding what should replace it.

## Exclusions and misuse

The term does **not** cover learning in general
([Simon's sense](../../theory/learning-is-not-only-about-generality.md),
which includes gradient training, automatic session logging, and direct
input-driven updates), edits to external work products that the system's own
later work does not consume, self-correction (a separate property), or
actual improvement (a separate verdict).

Avoid four recurring misuses of the vocabulary:

- Using *deliberative learning* for the system (the system is a
  *deliberative learner*), or citing the name as evidence that the system
  improved or corrects itself.
- Reporting a change as *learned* while its verdict is open.
- Reading *double-loop* in Argyris's full sense (questioning the terminal
  objective rather than the working criterion).
- Restricting the term to prose theories (excluding code, validators, or
  load-selection edits), or omitting the class of changes and horizon.

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
