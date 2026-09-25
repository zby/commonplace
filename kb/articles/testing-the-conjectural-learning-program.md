---
description: "Testing supplement: a modest first goal, showing that retained revisions causally improve later capacity and stay revisable; seven controlled tests, a task-family design, a compounding test, and the three adopted whole-program hypotheses"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/conjectural-learning.md
  - kb/notes/definitions/operative-change.md
  - kb/notes/definitions/externally-tested-theory-builder.md
  - kb/notes/definitions/actionable-methodology.md
  - kb/notes/definitions/theory-builder.md
  - kb/notes/definitions/reflective-theory-builder.md
  - kb/notes/a-complete-theory-path-does-not-establish-improved-capacity.md
  - kb/notes/retained-theory-intervention-isolates-one-explicit-surface.md
  - kb/notes/retained-theories-may-improve-sample-efficiency.md
  - kb/notes/a-claim-without-external-assessment-carries-three-obligations.md
  - kb/notes/commonplace-studies-conjectural-learning-through-retained-theories.md
  - kb/notes/improvements-can-accumulate-without-compounding.md
  - kb/notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md
  - kb/notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md
  - kb/notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md
  - kb/notes/definitions/autonomous-theory-builder.md
---

# Testing Conjectural Learning

> **Draft.** The claims and structure of this article may change. Comments
> and counterexamples are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

We are only starting to build
[conjectural learners](./conjectural-learning-with-fixed-models.md), so the
first testing goal should be modest. Before asking whether such systems can
learn broadly or indefinitely, we need to show that retained revisions cause
later improvement at all.

## What we need to show

A system has learned only if experience produces a durable change in
retained state that affects later capacity. Writing notes, reflections, or
revised rules is not learning until the retained revision changes later
work. The lead article gives the causal structure:

> K(t) → conjecture and criticism → K(t+1) → different later behaviour

where K is the retained tentative knowledge. The middle step is what makes
this conjectural learning rather than caching: the new retained state is a
theory that was proposed and is held open to criticism, not a stored answer.

Different later behaviour is not yet better later behaviour, and neither is
task success. A system can solve a task without learning anything. It can
also learn something useful while the current task still fails. And it can
retain and faithfully apply a bad rule: showing that a theory was
formulated, criticized, revised, and used
[does not by itself establish improved capacity](../notes/a-complete-theory-path-does-not-establish-improved-capacity.md).
The quantity to measure is therefore not current task performance but the
change in future capacity caused by retained knowledge.

Attributing that change to a revision requires fixing everything else.
Model weights are held fixed, ruling out weight updates as the source of
improvement. The other state that stays fixed must be named too, because
[an intervention isolates the contribution of the state it varies](../notes/retained-theory-intervention-isolates-one-explicit-surface.md);
other records, code, or people may still carry the lesson.

## First tests

The first experiments should make the causal role of a revision easy to
observe. Useful tests include:

- **retention** — does the revision survive into later work?
- **use** — does the record of later work show the revision was read and
  applied? A decision record that cites the revision is
  [cheap evidence that it was read](../notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md),
  but not that it carried the decision.
- **withholding** — does behaviour change when the retained revision is
  hidden? A change that passes this test is what the knowledge base calls
  [operative](../notes/definitions/operative-change.md).
- **perturbation** — does replacing it with a wrong alternative change
  behaviour in the predicted direction?
- **reconstruction** — does retaining the revision reduce total cost at
  comparable decision quality relative to re-deriving it from the episode
  records each time? This is the
  [efficiency conjecture](../notes/commonplace-studies-conjectural-learning-through-retained-theories.md#three-conjectures)
  in testable form.
- **transfer** — does the revision help on new cases rather than only
  replaying the original one? This is the
  [sample-efficiency conjecture](../notes/retained-theories-may-improve-sample-efficiency.md)
  in testable form.
- **revision** — can later evidence change retained knowledge when it turns
  out to be wrong?

Run the tests on the same revision. Retention shown for one revision and
transfer shown for another do not show that any revision
[changed later work through one causal path](../notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md).

## Start with controlled task families

Early experiments should be small enough that causal attribution is
possible. A simple pattern is:

1. give the system a family of tasks with some learnable regularity;
2. let it encounter failures and retain its own revisions;
3. test it on fresh instances;
4. compare the revised state with the pre-learning state on matched fresh
   instances to test whether the experience improved later capacity.

The answers in the task family are fixed outside the system before the run.
The system's approval of its own revision is not the outcome; the
[externally fixed answer](../notes/definitions/externally-tested-theory-builder.md)
is.

Once the revised state beats the pre-learning state, the tests above
isolate a single revision's contribution: withhold or perturb it, and
compare retaining it with reconstructing it from the same episode records.
Reconstruction can match retention at comparable total cost. Both systems
have then learned, but explicit retention offered no advantage under those
conditions. Count the costs of acquiring, maintaining, reconstructing, and
using the knowledge.

For each comparison, name the state being varied and hold the remaining
model, tools, evidence, task conditions, and resource limits fixed. Repeat
the comparison across tasks and runs to distinguish an effect from sampling
variation.

## Record what people contribute

People will be inside the early experiments. Declare whether the assessed
learning system includes them, and record their contributions separately
from computational work. An operator-written revision can contribute to
learning by the combined human–computational system, but it does not
establish autonomous acquisition by the computational components.

The record should list, for each completed improvement, the decisions a
person supplied, classified as noticing, diagnosis, choice, or acceptance.
Supplying the task family and its fixed answers is an
[external role](../notes/definitions/autonomous-theory-builder.md) and does
not count. This count is the measure the
[bootstrap supplement](./bootstrapping-an-autonomous-theory-builder.md)
uses: its conjecture fails if the count grows with the system instead of
falling.

## Then test accumulation and compounding

A useful learner must eventually hold many revisions without becoming
incoherent, overfitting to recent cases, or retaining obsolete knowledge.
Long-horizon tests will therefore matter, but only after the basic causal
mechanism is established.

Long-horizon tests also reach a question the first tests cannot. The first
tests ask whether a revision changes later task work. The bootstrap
supplement's loop, from learning to better learning machinery, needs
revisions that change later improvement work. Improvements
[accumulate](../notes/improvements-can-accumulate-without-compounding.md)
when a later improvement builds on an earlier retained result. They
compound when the earlier result makes the later improvement cheaper, more
reliable, or dependent on fewer human decisions. The loop requires
compounding.

[Compounding is measured in the later improvement episode](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md),
with a different quantity from the check that accepted the earlier change.
A validator that passes shows that the change met its target, not that the
next diagnosis became easier. Replay the later episode with the retained
knowledge frozen at the earlier snapshot, and trace how the later episode
used the earlier change. Without that trace, a cheaper later episode could
come from an easier problem or a more experienced operator.

## The hypotheses

The first tests are component tests. They do not substitute for the three
whole-program hypotheses the program adopted on 2026-09-17, quoted here as
adopted.

A [builder](../notes/definitions/theory-builder.md) is the persistent
system responsible for developing and revising theories. Its **seed** is its
starting knowledge and machinery; a frozen seed retains that starting state.
An **extension** is a retained machinery change that demonstrates a
capability gain over the seed. "Currently public" means available as of that
date; "training" means retained changes to the builder's instructions,
knowledge, tools, and orchestration, not changes to model weights.

> **Sufficiency hypothesis.** A training methodology expressed in
> natural-language and symbolic form is
> [actionable](../notes/definitions/actionable-methodology.md) for a
> computational operator using fixed weights from currently public models.
> Without people performing its internal theory-building roles or designing
> a new learning method for each area, the builder develops, retains, and
> uses theories and procedures across declared practical areas. Its later
> work meets a reliability target under a stated budget and external
> assessment protocol. An area is a consuming project's domain with an
> interface that can be declared and observed.

Refuted, for the assessed areas and budget, by a builder that reaches the
target only with a person in an internal role, or only after a new learning
method is designed for an area, or that fails to reach it. Such a result
does not rule out other methodologies.

> **Comparative hypothesis.** Under matched demands and declared resources,
> this methodology produces useful capability gains over the frozen seed
> and a baseline that searches the raw records without the learned
> methodology. Its downstream reliability is comparable to a human-staffed
> builder's under a margin set before assessment. The computational
> comparisons use the same fixed-model constraint and account for both
> adaptation and task costs.

Refuted by matched runs in which the frozen seed or the raw-record baseline
does as well at comparable cost, or in which the human-staffed builder
exceeds the preset margin. The reconstruction test above is this control at
component scale.

A **self-theory** is the builder's theory of how its own theory-building
machinery works. For example, it might assume that searching a note's title
is enough to retrieve relevant knowledge. Missed notes could prompt it to
revise that assumption and make retrieval search descriptions too, then
test whether the change improves later work. This illustrates
[reflection](../notes/definitions/reflective-theory-builder.md): criticism
of the self-theory guides a machinery change whose results can further
correct the self-theory.

> **Reflection hypothesis.** A builder whose machinery changes pass through
> a causally connected self-theory acquires extensions that a matched
> builder without one does not, under the same demands, budget, and
> external assessment. Better downstream outcomes alone do not test this;
> the records of a reflective episode and a matched builder that retains
> content without a self-theory do.

Refuted by a matched builder without a self-theory that acquires the same
extensions under the same conditions, or by reflective episodes whose
records show the machinery changes did not pass through the self-theory.
The second case refutes the claim that this builder is reflective; it does
not by itself say whether reflection would have helped.

No run has been performed. Our first goal is simpler than any of the three:

> **Show under controlled conditions that retained revisions causally
> improve later capacity and remain revisable when they turn out to be
> wrong.**
