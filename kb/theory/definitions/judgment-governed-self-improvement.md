---
description: "Definition — judgment-governed self-improvement is learning in which each proposed change to what a system retains is judged and can be rejected; a fixed criterion is the degenerate case of the on-balance judgment"
type: types/definition.md
tags: [self-improving-systems, learning-theory, judgment-governed-self-improvement]
---

# Judgment-governed self-improvement

<!-- Maintenance: when changing this definition, please apply the checks in
[judgment-governed-self-improvement-checks.md](./judgment-governed-self-improvement-checks.md).
This term was named "deliberative learning" until 2026-11-22. -->

A team weighing whether to add a routing rule to its handbook, a team
agreeing without writing anything down to change how it hands work over, and
an agent deciding whether to revise a validator in its own codebase are all
doing **judgment-governed self-improvement**. It is learning in which each
change is decided by a judgment:

> A change to what the system retains for its later work is proposed, judged
> in the learning loop, and can be rejected.

- **The change** is to the system's own
  [behavior-determining organization](./behavior-determining-organization.md),
  and its later work consumes it: the change is
  [operative](./operative-change.md). It may add, revise or delete, or
  change what later work loads or selects. The definition does not restrict
  where the change is held: a handbook, code, a team's working habits and a
  model checkpoint all qualify.
- **Proposing and judging are separate steps.** Something evaluates the
  proposed change itself, and that judgment controls whether the change is
  made. A change written automatically or on a trigger is not judged.
- **The judgment is a decision**, made on the evidence the system has, that
  later work is expected to go better with the change than without it. Its
  general form is the
  [on-balance judgment](../on-balance-judgments-can-guide-improvement-without-a-global-measure.md):
  the change is favored when every reasonable measure of the work favors
  it, and the decision stays open when the measures disagree. What the
  judgment applies to decide is its **criterion**.
- **A fixed criterion is the degenerate judgment.** A validator, a gate, a
  formula or a proof admits exactly one measure. With one measure nothing is
  weighed and no decision stays open: passing settles the matter. Whoever
  fixed the criterion chose that one measure in advance. Elsewhere in this
  note, "on-balance judgment" means the case with more than one reasonable
  measure.

The team that agrees a practice without writing it down already meets the
definition. When it starts writing its rules down, it stops relying on its
members' fallible memory: the rule that later work follows is
the rule that was agreed, a judge can read what a proposed change says, and
a later change can point at one rule and correct it. A store that can be
read and pointed at makes the learning more reliable. It is not required.

A system that learns this way is a **judgment-governed self-improving
system**. Two splits place it in the KB's existing vocabulary:

- **How a change is made.** A
  [self-improving system](./self-improving-system.md) is the general case.
  It makes a change either by an update that the evidence determines
  directly, or by a
  [proposal-selection improvement loop](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md).
  Judgment-governed self-improvement is the second. The two terms cover the
  same systems: proposal-selection names the architecture, and
  judgment-governed names what decides a change, in the same way a
  [Gödel machine is proof-governed](../goedel-machines-are-a-proof-governed-case-of-self-modification.md).
- **What the judgment admits.** The judgment is a fixed criterion or an
  on-balance judgment. Proof-governed and formula-governed systems are the
  fixed-criterion case.

Machine learning usually works with one given performance measure, on both
sides of the first split. Gradient training updates directly. Evolutionary
search, checkpoint selection and hyperparameter search propose and reject
candidates, so they are judgment-governed self-improvement with a fixed
criterion. The second split is the one that leaves that setting: an on-balance judgment
decides changes where no single measure is adequate.

Like reinforcement learning, the term names a process and not a successful
outcome. "Self-improvement" here means change directed at improvement, as in
the self-improving system definition: a system whose changes fail to improve
its later work still meets this definition. Whether one particular change
made the system better is a separate question, answered by an
[on-balance comparison](../on-balance-judgments-can-guide-improvement-without-a-global-measure.md)
of the system with and without that change.

## Scope

The definition separates rejectable decisions from updates that skip judging
the proposed change:

- **Direct updates (outside).** A nightly job that raises an article's rank
  whenever it is clicked, a value table updated by tabular reinforcement
  learning, and a gradient step under a fixed loss all write directly from
  their input. No change is proposed and none can be rejected. All three are
  learning, and none is judgment-governed.
- **Triggers (outside).** A rule that says *when* to write is not a judgment
  of *what* is written. A bot that adds a review rule whenever a class of
  bug has been reported five times is set off by a count. It is inside only
  if a separate step then evaluates the drafted rule and can reject it.
- **Automatic storage (outside).** Logging every session trace is automatic:
  nothing judges an individual trace. Appending an observation to
  Commonplace's `kb/log.md` is inside, because an agent judges that
  the observation is worth recording. Deciding to introduce automatic trace
  logging is itself a judged change, while the traces the logger later
  writes are outside the term.
- **Fixed criterion (inside, degenerate case).** Keeping a patch because a
  validator passed, keeping a rule because a utility formula scored it above
  zero, deploying the checkpoint with the best validation score, and
  switching to a rewrite because a target theorem was proved all evaluate a
  change another step produced and can reject it.
- **A score as one consideration (inside).** A team that looks at a test
  score and can still reject the change for a reason the score does not
  capture is making an on-balance judgment.
- **Contents nobody can read (inside).** The checkpoint choice above, and a
  team weighing whether to release a trained checkpoint, are inside for the
  class *checkpoint choices*, although nobody can read the weights. The
  gradient steps that produced the checkpoints stay outside.

Whoever judges—people, language models, programs or a mix—the judgment
counts only where it controls the change. The definition also does not ask
how well the judge weighs: a judge that weighs badly is still weighing.

## What a claim names

A claim of judgment-governed self-improvement names three things:

- **The system**, including which people and programs are inside it.
- **The class of changes** covered, with the definition checked on the loop
  that makes changes of that class. A wiki that imports pages automatically
  and lets editors delete wrong ones is outside for imports and inside for
  deletions. Loops also nest, such as gradient training inside a research
  team's workflow, and each loop is assessed on its own named system and
  class.
- **The horizon** over which later work is counted, following
  [operative change](./operative-change.md). Commonplace's claims span
  tasks, so a library note, instruction or validator counts while a
  workshop draft or single-task plan does not.

By default a claim states a standing capacity: how changes are proposed and
judged, and how later work consumes them. Claiming an episode requires
showing the proposal, the judgment, and what the system did differently on
later work. Loading alone does not show consumption: an agent can load a
memory file on every run and ignore every lesson in it.

## Exclusions

Judgment-governed self-improvement is one kind of learning in
[Simon's sense](../learning-is-not-only-about-generality.md), alongside
learning by directly determined updates. Membership excludes edits to
external work products that the system's own later work does not consume.

Membership does not imply any of these:

- **Improvement.** A judged change can make later work worse.
- **Correction.** Membership does not require that later evidence can count
  against an earlier change. A learner that judges every change and never
  revisits one is still a judgment-governed self-improving system.
- **Weighing.** A learner with a fixed criterion weighs nothing. A claim
  about weighing must say the judgment is on balance.
- **Criterion revision.** Whether the learner can revise its own criterion
  is the distinction between
  [single-loop and double-loop learning](./single-loop-and-double-loop-learning.md).

## Misuse Cases

- Using *judgment-governed self-improvement* for the system (the system is a
  *judgment-governed self-improving system*).
- Citing the name as evidence that the system improved or corrects itself.
- Reading the name as a claim that the system weighs considerations,
  without saying the judgment is on balance.
- Using the term for a system because it reasons carefully about its work.
  The term applies to how changes to what the system retains are decided.
- Restricting the term to prose theories, or to readable stores.
- Crediting an automated loop with judgments its designers make outside the
  named system.
- Omitting the class of changes or the horizon.

---

Relevant Notes:

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: the architecture the definition requires, and its contrast with a directly determined update
- [On-balance judgments can guide improvement without a global measure](../on-balance-judgments-can-guide-improvement-without-a-global-measure.md) — grounds: the general form of the judgment, of which a fixed criterion admits one measure, and the comparison that says whether a change made the system better
- [Self-improving system](./self-improving-system.md) — defined-in: the wider class, with its declared boundary, horizon and objective
- [Behavior-determining organization](./behavior-determining-organization.md) — defined-in: why the change must be to the system's own retained structure and a work product is excluded
- [Operative change](./operative-change.md) — defined-in: the declared horizon and the consumption path a change needs
- [Single-loop and double-loop learning](./single-loop-and-double-loop-learning.md) — defined-in: whether a proposal-selection learner can revise the criterion that decides its changes
- [Theory builder](./theory-builder.md) — contrasts: requires criticism of what a stated theory says, which judgment-governed self-improvement does not
