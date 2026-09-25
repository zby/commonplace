---
description: "Testing supplement: show that a theory builder's retained revisions causally improve later capacity; seven tests, task families with seed, matched baseline, evidence interface, and controls, human-decision accounting, compounding, three hypotheses"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/theory-builder.md
  - kb/notes/definitions/operative-change.md
  - kb/notes/definitions/actionable-methodology.md
  - kb/notes/a-complete-theory-path-does-not-establish-improved-capacity.md
  - kb/notes/an-action-model-matters-only-through-its-consumption-path.md
  - kb/notes/retained-theory-intervention-isolates-one-explicit-surface.md
  - kb/notes/retained-theories-may-improve-sample-efficiency.md
  - kb/notes/a-claim-without-external-assessment-carries-three-obligations.md
  - kb/notes/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md
  - kb/notes/improvements-can-accumulate-without-compounding.md
  - kb/notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md
  - kb/notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md
  - kb/notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md
---

# Testing Whether a Theory Builder Learns

> **Draft.** The claims and structure of this article may change. Comments
> and counterexamples are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

We are only starting to
[build theory builders from today's language models](./building-a-theory-builder-from-todays-llms.md).
A [theory builder](../notes/definitions/theory-builder.md) states its
theories in text, acts on them, criticizes what they say, and lets the
result of criticism shape its next conjecture. Whether a system that meets
the definition learns, in the sense of improving its capacity for later
work, is left to testing. The first testing goal should be modest. Before
asking whether theory builders can learn broadly or indefinitely, we need to
show that retained revisions cause later improvement at all.

## What we need to show

A system has learned only if experience produces a durable change in
retained state that affects later capacity. The
[lead article](./building-a-theory-builder-from-todays-llms.md) gives the
causal structure:

> K(t) → conjecture and criticism → K(t+1) → different later behaviour

where K is the retained state. The middle step is what makes this theory
building rather than caching: the new retained state is a theory that was
proposed and is held open to criticism, not a stored answer.

Different later behaviour is not yet better later behaviour, and task
success is not learning. A system can solve a task without learning
anything, or learn something useful while the current task still fails. It
can also retain and faithfully apply a bad rule: showing that a theory was
formulated, criticized, revised, and used
[does not by itself establish improved capacity](../notes/a-complete-theory-path-does-not-establish-improved-capacity.md).
The quantity to measure is the change in future capacity caused by retained
state.

A failed outcome also does not say where the fault lies. Deriving
predictions from a theory, identifying candidate faults, and assessing
revisions are acts of interpretation inside the builder, so a failure may
come from the theory or from its interpretation. An outcome comparison
records the failure; a claim about its cause needs its own evidence. The
builder's approval of its own revision establishes neither the outcome nor
the cause.

Attributing a change in capacity to a revision requires fixing everything
else. Model weights are held fixed, which rules out weight updates as the
source of improvement. The other fixed state must be named too, because
[an intervention isolates the contribution of the state it varies](../notes/retained-theory-intervention-isolates-one-explicit-surface.md);
other records, code, or people may still carry the lesson.

## First tests

The first experiments should make the causal role of a revision easy to
observe. Each test answers a separate question. Installing a revision is not
evidence that later work used it, and use is not evidence that it caused an
improvement: a retained revision
[matters only through its consumption path](../notes/an-action-model-matters-only-through-its-consumption-path.md).

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
  [persistence conjecture](../notes/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md#three-conjectures)
  in testable form.
- **transfer** — does the revision help on new cases rather than only
  replaying the original one? This is the
  [sample-efficiency conjecture](../notes/retained-theories-may-improve-sample-efficiency.md)
  in testable form.
- **revision** — can later evidence change the revision when it turns out
  to be wrong?

Run the tests on the same revision. Retention shown for one revision and
transfer shown for another do not show that any revision
[changed later work through one causal path](../notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md).

## Start with controlled task families

Early experiments should be small enough that causal attribution is
possible. A simple pattern is:

1. declare the builder's **seed**: its starting knowledge and machinery,
   the instructions, tools, and orchestration that do its theory-building
   work;
2. give it a family of tasks with some learnable regularity, whose answers
   are fixed outside the builder before the run;
3. let it meet failures and retain its own revisions;
4. run the revised builder and the seed on the same fresh instances under
   matched conditions.

The baseline in step 4 is the seed on the same later demand. Comparing
against the seed's earlier performance on earlier tasks would confound the
revision with task drift, model variance, and scoring noise. The outcome is
the externally fixed answer. A claim tested without such an answer
[carries obligations it must discharge for itself](../notes/a-claim-without-external-assessment-carries-three-obligations.md).

Once the revised builder beats the seed, the first tests isolate a single
revision's contribution. For each comparison, name the state being varied.
Matched conditions hold the model, tools, evidence, task conditions, and
resource limits fixed. Repeat each comparison across tasks and runs to
separate an effect from sampling variation.

Controls bound the alternative explanations of a gain. Run the same task
with the retained state removed, with a distractor that resembles it, with a
stale version of it, and with a different mechanism able to supply the
answer. Before the task runs, state which artifact should be written and
read, and score consumption against that expectation.
[PAST-Bench](../sources/past-bench-personal-agents-pdf.ingest.md) does both;
scoring against an expected pathway measures use. Removing retained state
usually removes information the task needs, so a with-and-without
comparison measures benefit, not harm. Measuring harm needs current
authoritative evidence held available while the retained state varies, as
[The Memory Trust Gap](../sources/the-memory-trust-gap.ingest.md) does in
separate benefit and safety suites.

The reconstruction test compares total cost: acquiring, maintaining,
reconstructing, and using the revision. Reconstruction can match retention
at comparable total cost. Both systems have then learned, but explicit
retention offered no advantage under those conditions.

### Declare how evidence reaches the builder

Each assessment declares the builder's boundary (which people, models,
tools, and texts do its theory-building work), its seed, and its evidence
interface. The evidence interface is a versioned record of how cases,
consequences, and acceptance judgments reach the builder: where tasks come
from, who judges consequences, which records show consumption, what
feedback returns, and how evidence is exposed, reserved, and renewed. It
says which claims each judgment can assess, and says so where a judgment is
made inside the builder or a claim has no assessment. A finite evaluation
supports a claim bounded by its tasks, period, interface, and budget.

An external judge does not by itself keep the builder aimed at the intended
objective. The
[Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md)
is assessed on an external benchmark with held-out test tasks, yet one of
its agents raised its score by deleting the tool-use markers its evaluator
depended on. At the other end is note review in Commonplace, a knowledge
base currently maintained by people and agents together. There the operator,
the person who maintains the knowledge base, reviews and accepts notes. That
review is evaluation inside the builder: its verdicts assess the note, not
how the note performs when used. The arrangement
[this research program](../notes/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md#research-program-and-development-path)
tests sits between them: Commonplace producing a
knowledge base for a consuming project, whose failing tests, rejected
releases, and bug reports reach the builder from outside it.

### Protect the assessment evidence

The protocol states how development evidence is kept apart from assessment
evidence, and what prior exposure the builder had. Reserve final assessment
evidence until a candidate is frozen. Feedback used to construct or select
a successor becomes development evidence for that successor. A fixed
benchmark the builder can adapt to supplies independent assessment only if
its reuse follows a protocol with a specified information-release
mechanism, sampling assumptions, and an enforced budget;
[generalization in adaptive data analysis](../sources/generalization-adaptive-data-analysis-holdout-reuse.ingest.md)
supplies these. Renewing the task stream helps but does not keep the
objective fixed: new users can repeat the same misleading acceptance proxy,
and a changing task mix can move a score.

## Record what people contribute

People will be inside the early experiments. The builder's
[boundary](../notes/definitions/theory-builder.md#boundary) follows the
operation, not the person. Someone who proposes a theory, criticizes it,
chooses what to blame, produces a revision, selects what to keep, or changes
the machinery is inside the builder for that act. Someone who supplies
problems or judges products against the task contract is outside. The same
person can do both, so record the acts separately. An operator-written
revision can contribute to learning by the combined human–computational
builder, but it does not show that computation could have produced it; that
would take an
[autonomous](../notes/definitions/theory-builder.md#qualifiers) builder, in
which computation performs every operation inside the boundary.

For each completed improvement, record the decisions a person supplied,
classified as noticing, diagnosis, choice, or acceptance. Supplying the task
family and its fixed answers is outside the builder and does not count.
Record the seed, including how it was constructed, separately from
interventions during the run. An intervention is a change installed from
outside the builder's own criticism and revision; the builder gets no credit
for what it produces, and an intervention that replaces the machinery
wholesale starts a new seed. This count of human decisions is the measure
the [bootstrap supplement](./bootstrapping-an-autonomous-theory-builder.md)
uses: its conjecture fails if the count grows with the system instead of
falling.

## Then test accumulation and compounding

A builder that learns must eventually hold many revisions without becoming
incoherent, overfitting to recent cases, or keeping obsolete revisions.
Long-horizon tests will matter, but only after the basic causal mechanism
is established.

They also reach a question the first tests cannot. The first tests ask
whether a revision changes later task work. The bootstrap supplement's
loop, from learning to better learning machinery, needs revisions that
change later improvement work. Improvements
[accumulate](../notes/improvements-can-accumulate-without-compounding.md)
when a later improvement builds on an earlier retained revision. They
compound when the earlier revision makes the later improvement cheaper, more
reliable, or dependent on fewer human decisions. The loop requires
compounding.

[Compounding is measured in the later improvement episode](../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md),
not by the check that accepted the earlier revision: a passing validator
shows that the revision met its target, not that the next diagnosis became
easier.
Replay the later episode with the retained state frozen at the earlier
snapshot, and trace how it used the earlier revision. Without that trace, a
cheaper later episode could come from an easier problem or a more
experienced operator.

## The hypotheses

The first tests are component tests. They do not substitute for the three
whole-program hypotheses the research program adopted on 2026-09-17, quoted
here as adopted. The hypotheses were written against an earlier definition,
in which a builder was the persistent system responsible for developing and
revising theories. Read against the current
[definition](../notes/definitions/theory-builder.md), "builder" means a
theory builder, and "capability" is what this article calls capacity.

In the sufficiency hypothesis, "internal theory-building roles" are the
operations inside the builder's boundary, so the hypothesis is about an
autonomous theory builder. "Currently public" means available as of the
adoption date. "Training" means retained changes to the builder's
instructions, knowledge, tools, and orchestration, not changes to model
weights.

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

In the comparative hypothesis, a frozen seed is the seed retained unchanged.

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

The reflection hypothesis needs two more terms. A **self-theory** is the
builder's theory of how its own theory-building machinery works. For
example, it might assume that searching note titles is enough to retrieve
relevant knowledge. Missed notes could prompt it to revise that assumption,
make retrieval search descriptions too, and test whether the change
improves later work. A builder "whose machinery changes pass through a
causally connected self-theory" is a
[reflective](../notes/definitions/theory-builder.md#qualifiers) one.

An **extension** is a retained machinery change that shows a capacity gain
over the seed on a stated demand under a stated budget, through later work
that consumes the change and against the matched baseline. It is a bounded
comparative claim, not a proof that the seed could never have supplied that
capacity. Reflection and extension are separate claims: a reflective
revision can fail to improve capacity, and a capacity gain can come from a
change that no self-theory guided.

The builder's own records can show that it is reflective: machinery changes
that updated the self-theory, and self-theory revisions that changed the
machinery. Whether a reflective episode paid off is a further claim, and it
needs one connected path. Externally assessed work exposes a possible
machinery limitation. Diagnosis, using evidence about how the machinery
actually operated, revises an identified commitment in the self-theory.
That revision guides a machinery change, and the installed change updates
the self-theory in turn. Later work uses the changed machinery, and its
product is tested under the declared protocol. The record keeps the
versions, consumption traces, predicted effects, and outcomes that connect
these steps. Matched interventions on the revised commitment, or on its
consumption path, strengthen the attribution. A machinery change followed
by better outcomes does not establish it alone.

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
