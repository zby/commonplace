---
description: "Definition — selection-based learning is learning in which each change to what a system retains is proposed, evaluated and can be rejected; it contrasts with updates that evidence determines directly"
type: types/definition.md
tags: [self-improving-systems, learning-theory, improvement-loop]
---

# Selection-based learning

<!-- Maintenance: when changing this definition, please apply the checks in
[selection-based-learning-checks.md](./selection-based-learning-checks.md).
This term was named "deliberative learning" until 2026-11-22 and
"judgment-governed self-improvement" on that day. -->

**Selection-based learning** is learning in which each change is selected:

> A change to what the system retains for its later work is proposed,
> evaluated, and can be rejected.

[AlphaGo Zero](https://www.nature.com/articles/nature24270) is a well-known
case. Each newly trained network played the current best one and replaced
it only if it won by a margin of 55%. Its successor
[AlphaZero](../../sources/alphazero-chess-shogi-self-play.ingest.md) dropped that step and updated
a single network continually, so it no longer selected among networks.

A system that learns this way is a **selection-based learner**. The loop
that does it is a
[proposal-selection improvement loop](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md),
and that note gives its anatomy. The contrast is a direct update, in which
the evidence determines the change and nothing is proposed or rejected. Both
are learning in
[Simon's sense](../learning-is-not-only-about-generality.md).

- **The change** is to something the learner retains and its later work
  uses. A proposal is information that describes a change, and it can be
  stored, as a patch can. Storing it is already a change to the system's
  durable state, and a different one from the change it describes. It is
  usually cheap and made directly, but it is still a decision. The
  described change is not stored. The system changes, and what it retains
  afterwards is different. Where that is held
  does not matter. A handbook,
  code, a team's working habits and a model checkpoint all qualify, so a
  store that can be read is not required.
- **Evaluation is causally distinct from proposing.** It need not be a
  separate stage or a separate actor. Its result decides whether the change
  is made, or undone if it was already made, and a rejection is its own
  event: it does not consist in the next candidate arriving. A change
  written automatically or on a trigger is not selected.
- **Evaluation needs a comparison, not a value function.** It can apply one
  fixed measure, such as a validator, a formula, a score or a proof. It can
  also compare the system with and without the change across several
  measures, as in a
  [robust comparison](../necessary-preference-can-guide-improvement-without-a-global-measure.md).

Like reinforcement learning, the term names a process and not a successful
outcome. Whether a selected change improved the system is a separate
question, answered by comparing the system with and without it.

## Scope

- **Direct updates (outside).** Pre-training by gradient descent is told
  the right output for each input, and the error fixes the update. A
  nightly job that raises an article's rank whenever it is clicked writes
  directly from its input in the same way. Nothing is tried, so nothing
  can be rejected.
- **Triggers and automatic storage (outside).** A bot that adds a review
  rule whenever a class of bug has been reported five times is set off by a
  count. A logger that stores every session trace evaluates none of them.
  Each is inside only if what was drafted is evaluated and can be
  rejected.
- **One fixed measure (inside).** Keeping a patch because a validator
  passed, deploying the checkpoint with the best validation score, and
  keeping a mutation in an evolutionary search all evaluate a candidate and
  can reject it. The gradient steps that produced each checkpoint stay
  outside.
- **Several measures (inside).** A team that looks at a test score and can
  still reject the change for a reason the score does not capture.

A claim of selection-based learning names the system and the class of
changes it covers. A wiki that imports pages automatically and lets editors
delete wrong ones is outside for imports and inside for deletions. Natural
selection shows why the system must be named. A population learns by
selection: variants arise, some are eliminated, and the rest are what the
population retains. An individual organism in it does not, because nothing
it retains is selected.

## The term and the system boundary

The system named in a claim has to be the one that changes. Who does the
selecting does not matter for the term. It matters for two further
questions, and each moves one more function inside the system. Take a model whose deployed checkpoint is
picked by a validation score:

1. **Learning.** The system is what changes. The model alone learns by
   selection that others perform on it.
2. **Self-improvement by selection.** The system also does the selecting. The model
   together with the selection script is a
   [self-improving system](./self-improving-system.md).
3. **Double-loop.** The system can also revise what it selects by. The
   model, the script and the engineers who can change the score are
   [double-loop](./single-loop-and-double-loop-learning.md).

A breeder's herd learns by selection and does not improve itself. A team
that maintains its own handbook does all three. Proposals may come from
outside the boundary. Selection is the step that has to be inside for
self-improvement by selection.

## Misuse Cases

- Citing the term as evidence that the system improved or corrects itself.
- Restricting the term to readable stores or to prose.
- Using the term for a system because it reasons carefully about its work.
  The term applies to how changes to what the system retains are decided.
- Omitting the class of changes.

---

Relevant Notes:

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — grounds: the anatomy of the loop and its boundary cases
- [Necessary preference can guide improvement without a global measure](../necessary-preference-can-guide-improvement-without-a-global-measure.md) — grounds: the comparison across compatible measures, and what a claim of improvement asserts
- [Learning is not only about generality](../learning-is-not-only-about-generality.md) — grounds: the sense of learning the term uses
- [Self-improving system](./self-improving-system.md) — defined-in: the second step of the ladder, where selection lies inside the declared boundary
- [Single-loop and double-loop learning](./single-loop-and-double-loop-learning.md) — defined-in: the third step, where the learner can revise the criterion that decides its changes
