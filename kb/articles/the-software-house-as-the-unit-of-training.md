---
description: "Fixed-model training of the software house through retained theory and machinery, with a checking-policy example and experiments separating causal influence, transfer, and learning cost"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md
  - kb/notes/continual-learning-requires-governing-behaviour-changing-writes.md
  - kb/notes/definitions/behavior-determining-organization.md
  - kb/notes/definitions/representational-form.md
  - kb/notes/definitions/software-house.md
  - kb/notes/definitions/theory-refinement.md
  - kb/notes/ephemeral-computation-prevents-accumulation.md
  - kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md
  - kb/notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md
  - kb/notes/retained-theory-intervention-isolates-one-explicit-surface.md
  - kb/notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md
  - kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md
  - kb/notes/theory-refinement-may-improve-sample-efficiency-under-shifts.md
---
# The Automated Software House as the Unit of Training

*A fixed-model training regime for theory refinement*

> **Draft.** This article may change. Comments and counterexamples are welcome
> on [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

**TL;DR.** A [software house](../notes/definitions/software-house.md) is the
complete persistent system that keeps changing software for its users. Assume
an automated one exists. The proposed *fixed-model training regime* trains
the house through production: experience revises the retained knowledge and
machinery that affect later work, while the models stay fixed. The object
that experience refines and later decisions consult is an *explicit project
theory*: a written account of the house's *program theory*,
its understanding of the software's purpose, organization, and how to handle
new requests, stated as design commitments, causal assumptions, and
invariants. Training the house is therefore *theory refinement*: production
evidence revises the theory, and the revised theory guides later work.

The regime is attractive on three counts, each still a conjecture. What the
house learns is retained and usable at the next request, so learning is
continual. A correct theory may say which new cases matter, so adaptation may
need fewer observations. And each learned assumption, rule, or test can be
inspected, challenged, and rolled back on its own. Whether these gains cover
the regime's costs, and whether an explicit theory does better than other uses
of the same evidence, are the article's empirical hypotheses.

## The fixed-model premise

The [companion article](./automated-software-houses-with-fixed-llms.md)
conjectures that an automated software house can operate practically with
distributed-parametric models available by the conjecture's cutoff, 2026-09-02,
and held fixed. Here that house is the starting point. Computation performs
every internal production role, including implementation, diagnosis, and
choosing which revisions take effect. Users supply requirements, facts,
feedback, and acceptance judgments about visible behaviour from outside the
production boundary; the [conjecture article's boundary
section](./automated-software-houses-with-fixed-llms.md#the-boundary) says
which acts fall on which side.

The house may begin from a human-built seed or emerge from the
[bootstrap program](./bootstrapping-the-first-automated-software-house.md).
Training changes its surrounding state and machinery. The rule is by
representational form: the house may revise both the natural-language and the
symbolic forms of its own definition; only its distributed-parametric models
are pinned. That pins the parameters of LLMs, embedding models, and parametric
routers and critics, including their adapters.

The experiments below do not wait for a complete automated house. They test
its learning mechanisms in bounded components.

## What is trained: the whole house

In this article *training* names the regime — what production is arranged to
do to the house — and *learning* names the retained change in capacity that
results. Both have the same unit. [The deployed system, not the model alone,
is the unit of
learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md)
because several components jointly determine its behaviour. Retrieval selects
the evidence a model sees, scheduling determines which calls happen and what
state survives, and validators determine which changes can take effect.
Revising any of them can change the result while the model stays fixed.

For coherent product evolution, the unit's boundary must include the current
product, retained project knowledge, production machinery, and every
computational role on which later evolution depends. The mutable part of this
[behaviour-determining organization](../notes/definitions/behavior-determining-organization.md)
is the trainable state. It includes theories, code, schemas, tests, tools,
evaluators, context assembly, and the update process itself.

Much of the learning may be product-specific: which dependencies make a
Markdown edit require product checks, or where tenant identity must be
represented to preserve isolation. A lesson can be stated in a theory,
enforced by tests, compiled into a tool, or embodied in product code.

Production can expose failures in both retained knowledge and executable
machinery, so the regime trains a house that can revise both. When existing
operations cannot apply, check, or revise a new theory reliably, [the house
must supply the missing
capacity](../notes/a-fixed-model-house-must-write-the-procedures-for-each-new-theory.md),
and with models pinned that capacity must persist outside their parameters.

## Why this is theory refinement

That the regime is theory refinement is easiest to show on a concrete case.
Consider a hypothetical release exporter. It builds a deployment manifest
listing service identifiers and ports for an installer. Duplicate identifiers
make the manifest invalid. Initially, the exporter reads only configuration
files, so Markdown edits receive syntax checks and are exempt from manifest
checks. The relevant part of the project theory, called the retained
explanation below, says that checks follow executable consumers and assumes
the configured input list includes every file that can affect the manifest.

When the exporter starts reading service definitions from named Markdown files,
the explanation directs the house to revoke their exemptions. This applies an
existing explanation to new facts. Now suppose the exporter gains support for
included Markdown snippets containing more service definitions. The old
checking policy still treats the configured input list as exhaustive. An
edit to an unlisted snippet passes its syntax check, but a later release
contains an invalid manifest. The local check missed an indirect dependency.

The proposed mechanism has three steps: the explanation directs diagnosis
toward the consumer path; the failure challenges the assumption that the input
list is exhaustive; and a revised account identifies other files that need
checks. Testing a second, untouched snippet asks whether that revision guides
a later decision. These are claims about how the house produces its updates,
and they can be tested separately from the outcome: two houses can both end up
modifying coherently while only one got there by revising an explanation.

The learning loop is:

> **production experience → explicit project theory revision → changes guided
> by the theory → later production → further evidence**

This loop is [theory
refinement](../sources/recap-early-work-theory-knowledge-refinement.ingest.md)
in the established sense: a fallible explicit theory guides inference,
empirical failure localizes a defect, and the theory itself is revised rather
than only the answer. The regime changes the setting: the theory is about a
product the house keeps changing, and its evidence is the consequences of
production rather than a labeled training set. It also departs from the
classical loop in three ways:

- **The theory is partly normative.** The commitment to tenant isolation is
  not a hypothesis about the product but a rule the house keeps true. A
  failure may therefore be resolved by changing the product to fit the theory
  as well as by revising the theory to fit the evidence, and the house must
  decide which.
- **Acceptance prefers reach.** Among revisions that fit the evidence, the
  house prefers those with more explanatory reach, those that would also
  handle cases the failure did not exhibit. That is why the example prefers a
  revised dependency account over an exception for the failing filename.
- **The refinement machinery is itself revisable.** The next paragraph says
  when that is needed.

LLMs are the condition that makes this practical rather than part of the
claim. They are the first interpreter that can apply and revise theories that
have not been formalized, and their reliability in doing so is an empirical
question.

The theory need not be about the house itself. A product failure, such as a
broken assumption about tenant identity, is handled by a theory of the
product. The house must hold and refine a theory of its own production path
only when the defect or the missing capacity lies there, which happens in four
situations:

- A new product theory needs a check the house cannot yet perform, so the
  house must build one.
- A failure could be due to the product theory, the evaluator that admitted
  the change, the retrieval that never surfaced the theory, or the check that
  was skipped, so diagnosis must tell them apart.
- A revision to an evaluator or admission rule would change how later evidence
  is read, so the house must reason about what the evaluator does.
- The theory was present but never found or never applied, which is a failure
  of the house's consumption path rather than of its content.

The checking policy above is such a case: the refined object is part of the
house's production machinery, and the same loop revises the producer as well
as the product. This second-order learning is what the [bootstrap
article](./bootstrapping-the-first-automated-software-house.md#two-kinds-of-transfer)
calls learning transfer, and a house that must outgrow its seed cannot do
without it.

## What counts as training

Production implements current requirements, and each episode of it supplies
evidence: operating consequences and retained history. Episodes may also be
replayed, simulated, or augmented. Evidence of training requires more than a
change that persists — every product edit changes the starting conditions of
later work. It requires experience to cause a retained change in the house's
capacity on later requirements.

The instrument for showing that is a *continuation*: a copy of the house that resumes
work from a product snapshot. Two continuations from the same snapshot, one
keeping a revision and one with it restored, show what the revision taught on
work the failure did not touch.

Learning can also be embodied in product code: a patch is then both
production and training. To measure what it taught, compare implementations
that currently behave the same but embody different lessons, on later
maintenance tasks. The acquired capability can remain specific to one product;
the comparison identifies what it contributes to later work.

## Why the fixed-model training regime can be general

Here *general* means that training is not restricted in advance to a predefined
family of changes, ontology, list of skills, or kind of retained update.
A learner's [permitted updates](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md)
bound what it can repair, including what it can express by composing existing
tools and calls. Lacking a dedicated tool alone does not establish a missing
capacity.

The house can instead construct project-specific representations, tools,
workflows, tests, evaluators, and update machinery as requests require them.
This opens a wider search space; it does not establish that the available
models and computation will find adequate changes.

Generality does not mean everything is trainable: some objectives, authority
boundaries, hard dependencies, runtimes, and trusted kernels may remain fixed.
Evidence for generality comes from adapting as the house takes on new kinds of
work, including changes to its initial responsibilities; evaluations must
report the work and period examined. Repeated dependence on people to supply
a missing ontology, decomposition, or evaluator counts against the proposed
learning capacity.

## Governing retained changes

The attractions named in the summary come from [retained artifacts changing
later behaviour](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md)
without a training cycle. They must cover the costs of discovery, retrieval,
validation, coordination, and maintenance; the experiments below ask whether
they do, and this section says where those costs concentrate. [Continual
learning requires governing behaviour-changing
writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md):
the house must evaluate a revision, decide which later behaviour it may
control, coordinate affected components, and retain or reject it.

A fact that fits the current theory is the cheap case: it is written to the
retained store and takes effect at the next request. A fact that contradicts
the current theory forces reconciliation: the house must decide which
commitment gives way, revise it, and re-check what depended on it.
Reconciliation is this regime's counterpart of retraining. It is local to the
affected theory and its dependents rather than global, and it should be rare,
but it is where the governing costs concentrate.

Two functions do the governing. **Admission** decides which changes take
effect. **Credit assignment** decides
which earlier theory, test, tool, or policy a later consequence supports or
counts against. In the checking example, the house must trace the invalid
manifest back to the incomplete dependency account, then judge a replacement
policy. Intervening changes make that diagnosis harder.

Revising an evaluator or admission rule also changes how later evidence is
interpreted. A wrong revision can therefore cause further errors to accumulate.
Independent checks, versioning, regression control, and rollback must remain
capable of exposing and repairing those errors.

## Bitter Lesson compatibility

AI researcher Rich Sutton's Bitter Lesson raises an objection: general methods
that scale with computation outperform methods built from human knowledge, so
are readable theories and programs merely hand-crafted structure? The answer
turns on [how that structure is produced, not the form in which it is
retained](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).

In this regime, computation forms and revises theories, searches over programs
and tools, constructs evaluators, and selects changes from production
evidence. These artifacts are learned products. Compatibility is assessed over
the *training lineage*, the history of retained changes made while the models
stay pinned; the seed may be human-built, but subsequent project-specific
structure must be produced or revised by computation.

This is structural compatibility, not evidence of a scaling advantage. Search,
validation, and credit assignment over artifacts may scale poorly, or weight
adaptation may reach the same competence at lower total cost. Those comparisons
remain necessary.

## Testable hypotheses

The checking experiment separates three questions: whether retained theory
influences decisions, whether it improves transfer and recovery, and whether
it reduces the observations needed to learn.

Use paired continuations with the same starting product, fixed models, tools,
request sequence, and resource ceilings, and the same *source observations*:
the facts observed before the continuations start, which each treatment
retains in its own form. Vary that retained form, then let each continuation
learn from its own actions and observations. Compare four treatments:

| Retained treatment | What the comparison tests |
|---|---|
| An explicit theory with assumptions and scope | Whether a revisable explanation guides useful inference and later updates |
| Raw records of the same source observations | Whether synthesis helps beyond reconstructing an account when needed |
| A descriptive summary of those observations | Whether the explanatory account helps beyond compact access to the facts |
| A plausible wrong theory | Whether a specified mistaken premise produces its predicted errors and is corrected after contrary evidence |

During learning, the raw-record treatment appends observations; the summary
treatment revises factual summaries; the two theory treatments may revise
their explanations. All may revise executable machinery and its tests. In any
treatment the model can still build an explanation while reasoning; no
treatment forbids thinking in theories. What differs is what survives to the
next decision: the comparison concerns what each treatment retains, not what
the model can construct in the moment.

Construct the summary from an inventory of observed facts supplied to every
treatment. Keep names, examples, access to source records, and context allowance
comparable; omit the general dependency claim and its inferred consequences.
For the wrong theory, replace a named inference while preserving the observed
facts. Publish the treatment texts, retained revisions, and inventory so a
reader can inspect the differences and compliance with the retention rules.
This controls the supplied observations and presentation without guaranteeing
that a model extracts identical information from each text.

Test two kinds of change separately, each as its own request history. In the
first history, adding another configured exporter input preserves the initial
account of direct inputs. In the second, adding indirect includes breaks its
assumption that the list is exhaustive. Include unaffected files in both
histories, and reserve later edits to different files for testing transfer.
The [bootstrap article](./bootstrapping-the-first-automated-software-house.md#a-possible-early-trial-learning-which-checks-a-markdown-edit-needs)
illustrates how this comparison could inform an early transfer trial. A concrete
protocol should match workloads within repetitions, vary cases and model sampling
between repetitions, and set its resource limits and decision rules before
scored runs. Analyse each history separately and publish every run, including
timeouts and interventions.

**Causal contribution.** A [retained-theory
intervention](../notes/retained-theory-intervention-isolates-one-explicit-surface.md)
at a selected decision holds the model, selector, other state, available
evidence, and budget fixed while varying the designated theory text. It
should change search, diagnosis, or recovery as predicted. A wrong theory
should add a specific error pattern beyond the controls' existing biases.
That establishes influence, but influence alone is not explanatory guidance:
a model that merely followed the text as an instruction would produce the
same errors. Evidence of useful explanatory guidance additionally requires
correct handling of consequences the text does not state, and appropriate
revision when evidence contradicts it.

**The explicit-project-theory advantage hypothesis.** The theory treatment
should improve later check selection and recovery when changes preserve its
account, without unnecessary changes to unaffected files. Its initial advantage
may disappear or reverse when assumptions break: the theory then misdirects
the house. Measure that misdirection separately from recovery after revision,
because rapid recovery can erase the initial loss in a whole-run score.

**The sample-efficiency hypothesis.** Correct theory may [reduce the new
observations needed to adapt](../notes/theory-refinement-may-improve-sample-efficiency-under-shifts.md)
by letting one discovered dependency change checking decisions for several
files. Count inspected new cases and feedback used in recovery, alongside
missed defects, unnecessary checks, collateral regressions, rollback, and total
cost. Report model input and output tokens, check-execution CPU seconds,
end-to-end elapsed seconds, and monetary cost at declared model and compute
prices. Separate operating cost from reference evaluation; include theory
construction, retrieval, validation, and maintenance in operating cost. Fewer
observations need not mean a cheaper method.

For each treatment and history, report completion and defect counts, the median
and range of resource use, and all paired differences. Give exact binomial 95%
intervals for run pass rates and the fraction of matched repetitions favouring
each treatment. Small samples leave wide uncertainty even if every run passes.
For a larger confirmatory trial, use pilot variability to choose the repetition
count for a declared minimum effect and interval precision. For paired cost
differences, resample whole matched repetitions, keeping histories separate;
decisions within a history are not independent replications.
Predeclare which comparisons are primary and account for testing several controls. Model-weight
adaptation on the same evidence is a further comparison with another training
regime, beyond this component trial.

## Future work: exemplars instead of theories

An alternative retains worked cases rather than a general explanation: the
request, the accepted change, and the evidence and judgment behind acceptance.
The fixed model may infer an explanation from those cases at use time; the
comparison concerns what is retained, not what the model may reason about.
Each form has a cost the other avoids. An explanation reconstructed and
discarded is [ephemeral
work](../notes/ephemeral-computation-prevents-accumulation.md) repeated on
every use, while a retained theory can omit a relevant detail or keep
activating a mistaken abstraction, and [retained cases preserve the evidence
for re-examining
it](../notes/retaining-the-episode-keeps-a-distilled-rule-re-derivable.md).

A fifth treatment could retain a curated set of worked cases, rather than the
raw-record treatment's uncurated history. Compare it with explicit theory under
the same source observations and resource ceilings, across both
assumption-preserving and assumption-breaking changes. Count case selection
and reconstruction alongside theory construction, retrieval, validation, and
revision. The question is whether retaining an explanation saves enough useful
work to outweigh its maintenance costs and the errors it can carry forward.

## Limits

A null intervention result does not show that the house lacks program theory:
it may reconstruct the same understanding from other retained state. With
sufficient precision, the comparison can still count against an incremental
benefit from the designated text. If the controls repeatedly match the theory
treatment at lower total cost, its advantage hypothesis fails in that regime.
Neither result settles whether a house can exist or learn with fixed models:
learning through tests, tools, and search is also learning by the house.

Even successful component tests leave the whole-house proposal dependent on
reliable theory use, credit assignment, validation, and admission working
together. Retained theory and machinery persist outside a model checkpoint,
but their effective use may still depend on the model, so replacing the model
requires revalidation and starts a new training lineage. Parametric and hybrid
regimes remain alternatives.

The [comparison supplement](./nearest-existing-constructions-to-a-witness-house.md#the-test-for-explicit-project-theory-from-the-training-article)
distinguishes existing evidence for program-theory use from this proposed test
of a written carrier. The [bootstrap program](./bootstrapping-the-first-automated-software-house.md)
turns the learning proposal into a first trial and a sequence of bounded transfers.
