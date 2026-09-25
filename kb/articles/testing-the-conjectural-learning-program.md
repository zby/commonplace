---
description: "Testing supplement: show that a theory builder's retained revisions causally improve later capacity and stay revisable; seven tests, task families with an evidence interface and controls, per-role human accounting, compounding, three hypotheses"
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
  - kb/notes/commonplace-studies-conjectural-learning-through-retained-theories.md
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
[build theory builders from today's language models](./conjectural-learning-with-fixed-models.md).
A [theory builder](../notes/definitions/theory-builder.md) states its
theories in text, acts on them, criticizes what they say, and lets the
result of criticism shape its next conjecture. How far that result persists,
within a run or across later problems, is graded. Meeting that definition does not show that a
system learns, in the sense of improving its capacity for later work; the
definition leaves that question to testing. The first testing goal should be
modest. Before asking whether theory builders can learn broadly or
indefinitely, we need to show that retained revisions cause later
improvement at all.

## What we need to show

A system has learned only if experience produces a durable change in
retained state that affects later capacity. Writing notes, reflections, or
revised rules is not learning until the retained revision changes later
work. The lead article gives the causal structure:

> K(t) → conjecture and criticism → K(t+1) → different later behaviour

where K is the retained tentative knowledge. The middle step is what makes
this theory building rather than caching: the new retained state is a
theory that was proposed and is held open to criticism, not a stored answer.

Different later behaviour is not yet better later behaviour, and neither is
task success. A system can solve a task without learning anything. It can
also learn something useful while the current task still fails. And it can
retain and faithfully apply a bad rule: showing that a theory was
formulated, criticized, revised, and used
[does not by itself establish improved capacity](../notes/a-complete-theory-path-does-not-establish-improved-capacity.md).
The quantity to measure is therefore not current task performance but the
change in future capacity caused by retained knowledge.

Three claims about later work are easy to run together. Outcome performance
says the work succeeded. Interpretive fidelity says the builder correctly
derived what its theories imply. The causal effect of a retained theory says
the theory made the difference. An outcome success establishes only the
first, and the builder's approval of its own revision establishes none of
them. Interpretation, meaning deriving predictions from a theory,
identifying candidate faults, and assessing revisions, is work done inside
the builder. So a failed outcome does not by itself say whether the theory
or its interpretation was wrong. An outcome comparison records the failure;
a claim about its cause needs its own evidence.

Attributing a change in capacity to a revision requires fixing everything
else. Model weights are held fixed, ruling out weight updates as the source
of improvement. The other state that stays fixed must be named too, because
[an intervention isolates the contribution of the state it varies](../notes/retained-theory-intervention-isolates-one-explicit-surface.md);
other records, code, or people may still carry the lesson.

## First tests

The first experiments should make the causal role of a revision easy to
observe. Each test answers a separate question, because installing a
revision is not evidence that later work used it, and use is not evidence
that it caused an improvement: a retained theory
[matters only through its consumption path](../notes/an-action-model-matters-only-through-its-consumption-path.md).
Useful tests include:

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
  [persistence conjecture](../notes/commonplace-studies-conjectural-learning-through-retained-theories.md#three-conjectures)
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
externally fixed answer is. A claim tested without such an answer
[carries obligations it must discharge for itself](../notes/a-claim-without-external-assessment-carries-three-obligations.md).

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

### Declare how evidence reaches the builder

Each assessment declares the builder's boundary, meaning which people,
models, tools, and texts do its theory-building work; its seed, the
starting state defined below; and its evidence interface. The evidence
interface says how cases, consequences, and acceptance judgments reach the
builder, which claims they can assess, and under which assumptions. Keep it
as a versioned record. It covers the claim and its scope, where tasks come
from and how the builder acquires them, who judges consequences, which
records show consumption, what feedback returns, and how evidence is
exposed, reserved, and renewed. Where a judgment is made inside the
builder, or no assessment exists for a claim, the declaration says so. A
finite evaluation supports a claim bounded by its tasks, period, interface,
and budget.

Three cases show what an evidence interface does and does not supply.
Commonplace's note-review loop, in which the operator reviews and accepts
notes, assesses the note itself: its verdicts do not assess how the note
performs when used, and the operator's acceptance is evaluation inside the
builder. Commonplace producing a knowledge base for a consuming project
would get its falsifier and its objective from task outcomes the consumer
judges, once release, consumption, and outcome records exist. The
[Darwin Gödel Machine](../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md)
is assessed on an external benchmark, reusing validation tasks and holding
test tasks out. One of its agents still raised its score by deleting the
tool-use markers its evaluator depended on. An external benchmark does not
by itself keep the builder aimed at the intended objective rather than at a
proxy.

### Protect the assessment evidence

The protocol states how development evidence is kept apart from assessment
evidence, and what prior exposure the builder had. Reserve final assessment
evidence until a candidate is frozen. Feedback used to construct or select
a successor becomes development evidence for that successor. A fixed
benchmark that the builder can adapt to does not supply independent
assessment unless its reuse follows a protocol with a specified
information-release mechanism, sampling assumptions, and an enforced
budget; [generalization in adaptive data analysis](../sources/generalization-adaptive-data-analysis-holdout-reuse.ingest.md)
supplies these. Renewing the task stream helps, but it does not keep the
objective fixed: new users can repeat the same misleading acceptance proxy,
and a changing task mix can move a score.

Controls bound the alternative explanations of a gain. Run the same task
with the retained state removed, with a distractor that resembles it, with a
stale version of it, and with a different mechanism able to supply the
answer. Before the task runs, state which artifact should be written and
read, and score consumption against that expectation.
[PAST-Bench](../sources/past-bench-personal-agents-pdf.ingest.md) does
both, with the qualification that following an expected pathway is evidence
of use, not of causal necessity.

Each with-and-without comparison also declares what the no-retention
condition knows. Removing retained content usually removes information the
task needs, so the comparison measures benefit, not harm. Measuring harm
needs current authoritative evidence held available while the retained
content varies. [The Memory Trust Gap](../sources/the-memory-trust-gap.ingest.md)
makes this split between its benefit and safety suites.

## Record what people contribute

People will be inside the early experiments. The builder's
[boundary](../notes/definitions/theory-builder.md#boundary) follows the
operation, not the person. Someone who proposes a theory, criticizes it,
chooses what to blame, produces a revision, selects what to keep, or changes
the machinery is inside the builder for that act. Someone who supplies
problems or judges the products against the task contract is outside. The
same person can do both in different interactions, so record the acts
separately. An operator-written revision can contribute to learning by the
combined human–computational builder, but it does not show that the
computational part acquired the revision itself. That would be an
[autonomous](../notes/definitions/theory-builder.md#qualifiers) builder, in
which computation performs every operation inside the boundary.

For each consequential operation, report whether a person, computation, or
both performed it. The record should list, for each completed improvement,
the decisions a person supplied, classified as noticing, diagnosis, choice,
or acceptance. Supplying the task family and its fixed answers is outside
the builder and does not count. Declare the seed, including how it was
constructed, separately from interventions during the run. An intervention
is a change installed from outside the builder's own process of criticism
and revision. Record it as one, and do not credit the builder with what it
produces; an intervention that replaces the machinery wholesale starts a
new seed.

This count of human decisions is the measure the
[bootstrap supplement](./bootstrapping-an-autonomous-theory-builder.md)
uses: its conjecture fails if the count grows with the system instead of
falling.

## Then test accumulation and compounding

A builder that learns must eventually hold many revisions without becoming
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
adopted. They were written against an earlier definition, in which a
builder was the persistent system responsible for developing and revising
theories. Read against the current
[definition](../notes/definitions/theory-builder.md), "builder" means a
theory builder. "Internal theory-building roles" are the operations inside
the builder's boundary, so the sufficiency hypothesis is about an
autonomous theory builder. A builder "whose machinery changes pass through a
causally connected self-theory" is a
[reflective](../notes/definitions/theory-builder.md#qualifiers) one.

A builder's **seed** is its starting knowledge and machinery, declared at
the start of an assessment; a frozen seed retains that starting state. An
**extension** is a retained machinery change that demonstrates a capability
gain over the seed on a stated demand under a stated budget, shown by later
work that consumes the change. The baseline is the same later demand run
without the retained change under matched conditions. It is not the seed's
earlier performance on an earlier demand, because a gain between episodes
confounds the change with task drift, model variance, and scoring noise.
[PAST-Bench](../sources/past-bench-personal-agents-pdf.ingest.md) builds its
evaluation on this matched ablation. An extension is a bounded comparative
claim, not a proof that the seed could never have supplied the capability.
"Currently public" means available as of the adoption date; "training"
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
test whether the change improves later work. This illustrates reflection:
criticism of the self-theory guides a machinery change whose results can
further correct the self-theory.

The builder's own records can show reflection itself: machinery changes
that updated the self-theory, and self-theory revisions that changed the
machinery. Whether a reflective episode paid off is a further claim. It is
evidenced by one connected path. Externally assessed work exposes a
possible machinery limitation, though the outcome signal alone does not
locate the fault. Diagnosis revises an identified commitment in the
self-theory, using evidence about how the machinery actually operated. That
revision guides a machinery change, and the installed change updates or
corrects the self-theory in turn. Later work uses the changed machinery, and
its product is tested under the declared protocol. The record keeps the
versions, consumption traces, predicted effects, and outcomes that connect
these steps. Matched interventions on the revised commitment, or on its
consumption path, strengthen the attribution that the self-theory guided
the change; a machinery change followed by better outcomes does not
establish it alone. Reflection and extension are also separate claims: a
reflective revision can fail to improve capability, and a capability gain
can come from a change that no self-theory guided.

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
