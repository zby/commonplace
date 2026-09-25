---
description: "A machinery improvement is paid for once and reused by every later learning episode, so over a long horizon its return can exceed immediate learning; where it does, an optimal strategy diverts effort to the machinery."
type: note
traits: [title-as-claim]
tags: [learning-theory, self-improving-systems]
---

# An optimal long-run learning strategy invests in its own machinery

A learning strategy allocates effort between learning now and improving the
machinery that learns. An improvement to the machinery is paid for once and
then used by every later learning episode, so its return grows with the
horizon and with how often the machinery runs. Over a long horizon this
asymmetry can make **reflective investment** — using current learning to
improve the productivity of future learning — return more capability than
spending the same effort on immediate learning. Where it does, a strategy that
spends everything on immediate learning is suboptimal. The Bitter Lesson says
which machinery improvements to look for: those that let the system turn
additional computation into capability.

## Computation is the lever the machinery should exploit

Consider a learning system that combines automated computation with functions
supplied by an operator. [Sutton's Bitter
Lesson](../sources/sutton-the-bitter-lesson-original-essay.ingest.md) favors
general search and learning because these methods continue to scale with
increased computation. In the combined system, operator-supplied knowledge may
give a substantial initial advantage. As computational resources grow, further
gains depend on the methods that convert those resources into capability. The
scaling advantage belongs to those methods, not to everything performed
automatically.

A [reflective](./definitions/reflective-system.md) system adds a feedback
path. It retains knowledge about its own learning machinery, uses that
knowledge to change the machinery, and revises the knowledge in light of the
resulting behavior. By testing candidate changes and keeping those that improve
later learning, it closes a loop:

> learning → improved learning machinery → greater future learning capacity → further learning

The loop acts on learning productivity: how much useful capability the system
acquires per unit of effort. One successful change raises productivity;
repeated changes can keep raising it. Judging either requires a measure of
capability that stays comparable across the period studied, which the system
may not have.

## Why the return favors the machinery

A machinery improvement benefits the later learning that uses it. Immediate
learning yields one result; a machinery improvement yields a stream of
results, one per later episode, for as long as the improvement persists and
the machinery is used. The stream is what makes the expected return of a
lasting improvement exceed, over a long horizon, the return of running the
existing learner for the same effort, even after the cost of finding, testing,
and maintaining the improvement.

Where this holds, an optimal allocation includes reflective investment for as
long as its expected marginal net return exceeds that of competing uses of
effort. The allocation is not fixed. It follows the returns as the system, its
horizon, and its problems change.

How the automated subsystem grows into functions the operator once supplied,
and what the Bitter Lesson requires of that growth, is the subject of [the
bootstrap compatibility
condition](./a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).

## Scope

The claim is conditional on three things: useful machinery improvements can be
found and their effect assessed; their benefit persists over the chosen
horizon; and their expected net return exceeds competing uses of effort. The
Bitter Lesson motivates looking for such improvements. Whether they exist for
a particular learner is an empirical question.

Harder problems, resource limits, and maintenance costs can erode the return.
When they do, the optimal allocation shifts back toward immediate learning.

For a [reflective](./definitions/theory-builder.md#qualifiers) theory
builder, the machinery is its theory-building machinery. That the builder
can become autonomous, with computation performing every internal operation,
is a further conjecture: some internal functions may keep requiring an
operator, and expanding the system's responsibilities can create new
operator work. Even an autonomous builder leaves users supplying problems and
judging products.

---

Relevant Notes:

- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](./a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) — grounds: supplies the compatibility condition on how operator-supplied functions are displaced, which this note's investment argument assumes rather than argues
- [The bitter lesson selects production methods, not representational forms](./the-bitter-lesson-selects-production-methods-not-representational.md) — grounds: locates the scaling advantage in how capability is produced rather than in automation or the form of retained knowledge
- [Theory builder](./definitions/theory-builder.md#qualifiers) — defined-in: the reflective builder whose machinery the argument applies to, with membership separated from successful learning
