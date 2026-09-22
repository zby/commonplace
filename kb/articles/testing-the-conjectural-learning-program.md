---
description: "Testing supplement: a modest first goal, showing that retained revisions causally improve later capacity and stay revisable; seven controlled tests, a task-family design, and the three adopted whole-program hypotheses"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/conjectural-learning.md
  - kb/notes/definitions/operative-change.md
  - kb/notes/definitions/externally-tested-theory-builder.md
  - kb/notes/definitions/actionable-methodology.md
  - kb/notes/a-complete-theory-path-does-not-establish-improved-capacity.md
  - kb/notes/retained-theory-intervention-isolates-one-explicit-surface.md
  - kb/notes/retained-theories-may-improve-sample-efficiency.md
  - kb/notes/a-claim-without-external-assessment-carries-three-obligations.md
  - kb/notes/commonplace-studies-conjectural-learning-through-retained-theories.md
---

# Testing Conjectural Learning

> **Draft.** The claims and structure of this article may change. Comments
> and counterexamples are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

We are only starting to build
[conjectural learners](./conjectural-learning-with-fixed-models.md), so the
first testing goal should be modest. We do not yet need to show that such
systems can learn broadly or indefinitely. We first need to show that
retained revisions actually cause later improvement.

## What we need to show

A system has learned only if experience produces a durable change in
retained state that affects later capacity. The lead article gives the
causal structure:

> K(t) → conjecture and criticism → K(t+1) → different later behaviour

where K is the retained tentative knowledge. The middle step is what makes
this conjectural learning rather than caching: the new retained state is a
theory that was proposed and criticized, not a stored answer.

Model weights are held fixed. That is what makes the tests below clean:
apart from the context of a single run, the retained state is the only place
the learning can live, so
[an intervention on it isolates its causal contribution](../notes/retained-theory-intervention-isolates-one-explicit-surface.md).

Writing notes, reflections, or revised rules is not enough. The retained
revision must matter later.

## First tests

The first experiments should make that causal role easy to observe. Useful
tests include:

- **retention** — does the revision survive into later work?
- **use** — does the record of later work show the revision was read and
  applied?
- **withholding** — does behaviour change when the retained revision is
  hidden? A change that passes this test is what the knowledge base calls
  [operative](../notes/definitions/operative-change.md).
- **perturbation** — does replacing it with a wrong alternative change
  behaviour in the predicted direction?
- **reconstruction** — does the retained revision beat re-deriving it from
  the episode records each time? This is the
  [efficiency conjecture](../notes/retained-theories-may-improve-sample-efficiency.md)
  in testable form.
- **transfer** — does the revision help on new cases rather than only
  replaying the original one?
- **revision** — can later evidence change retained knowledge when it turns
  out to be wrong?

These tests are more informative than measuring whether the system solved
the task.

## Separate task success from learning

A system can solve a task without learning anything. It can also learn
something useful while the current task still fails. And it can retain and
faithfully apply a bad rule: showing that a theory was formulated,
criticized, revised, and used
[does not by itself establish improved capacity](../notes/a-complete-theory-path-does-not-establish-improved-capacity.md).

We should therefore distinguish current task performance from the change in
future capacity caused by retained knowledge. The second is the central
quantity for testing learning.

## Start with controlled task families

Early experiments should be small enough that causal attribution is
possible. A simple pattern is:

1. give the system a family of tasks with some learnable regularity;
2. let it encounter failures and retain its own revisions;
3. test it on fresh instances;
4. compare normal retained knowledge with withheld, reset, or corrupted
   versions, keeping the episode records available so the reconstruction
   control can re-derive from them.

The answers in the task family are fixed outside the system before the run.
The system's approval of its own revision is not the outcome; the
[external outcome](../notes/definitions/externally-tested-theory-builder.md)
is.

People will be inside the early experiments. Their contributions are
recorded and not credited to computation. In particular, a revision written
by the operator tests whether retained knowledge is used, not whether the
system learned.

This lets us test whether later improvement is actually mediated by the
retained state.

## Then test accumulation

Single-step learning is only the beginning. A useful learner must eventually
accumulate many revisions without becoming incoherent, overfitting to recent
cases, or retaining obsolete knowledge. Long-horizon tests will therefore
matter, but only after the basic causal mechanism is established.

## The hypotheses

The first tests are component tests. They do not substitute for the three
whole-program hypotheses the program adopted on 2026-09-17, quoted here as
adopted. "Currently public" means available as of that date; "training"
means retained changes to the builder's instructions, knowledge, tools, and
orchestration, not changes to model weights.

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

Refuted by a builder that reaches the target only with a person in an
internal role, or only after a new learning method is designed for an area,
or that fails to reach it.

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

> **Reflection hypothesis.** A builder whose machinery changes pass through
> a causally connected self-theory acquires extensions that a matched
> builder without one does not, under the same demands, budget, and
> external assessment. Better downstream outcomes alone do not test this;
> the records of a reflective episode and a matched builder that retains
> content without a self-theory do.

Refuted by a matched builder without a self-theory that acquires the same
extensions, or by reflective episodes whose records show the machinery
changes did not pass through the self-theory.

No run has been performed. Our first goal is simpler than any of the three:

> **Show under controlled conditions that retained revisions causally
> improve later capacity and remain revisable when they turn out to be
> wrong.**
