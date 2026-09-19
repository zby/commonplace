# Workshop: the first downstream run

## Goal

Run the first externally assessed episode of Commonplace as a KB-producing
[theory builder](../../notes/definitions/theory-builder.md): a consuming
project receives a versioned KB release, its agents do real tasks, its judges
accept or reject the outputs, and the builder revises the product and, when
a failure exposes a machinery limit, its own methodology, with later matched
tasks assessed against the frozen seed. The
[evidence protocol](./commonplace-evidence-protocol.md) is the design; the
[three episodes](./main-path-episodes.md) are constructed cases that show
the vocabulary can describe such a run. Neither is a result.

Posed by the operator on 2026-09-17 when the theory-builder workshop's
conclusions were adopted. Its definitions and article reframes are now in the
library. This workshop owns the assessment of the adopted hypotheses below;
the original adoption record remains in git commit `28a2ea8d`.

## Two layers

Early use in an enterprise showed that a run can assess Commonplace at two
layers, and an episode must say which.

- **Builder layer.** A project's people and agents use the framework to
  build their own KB. The product is the framework release, and the outcome
  is whether they reach an accepted KB and what it costs them in their own
  work.
- **Product layer.** A project's agents use a finished KB on their tasks,
  and judges accept or reject that work. The goal statement above and the
  [three episodes](./main-path-episodes.md) describe this layer.

The enterprise's first finding is at the builder layer: the framework is
complex and asks the operator to learn a great deal. The current tool work
responds to it. The [first experiment](./first-experiment.md) measures that
response on one real task with a matched comparison, and is the smallest
run that meets this workshop's records requirements. The product layer
comes after it.

The enterprise's records are confidential. The protocol's
[disclosure rules](./commonplace-evidence-protocol.md#confidential-consuming-projects)
keep raw records inside the enterprise and publish only the declaration,
computed measurements, and automatic summaries from a
[pinned prompt](./summary-prompt.md) and a pinned model.

## Adopted hypotheses

> **Sufficiency hypothesis.** A training methodology expressed in
> natural-language and symbolic form is
> [actionable](../../notes/definitions/actionable-methodology.md) for a
> computational operator using fixed weights from currently public models.
> Without people performing its internal theory-building roles or designing
> a new learning method for each area, the builder develops, retains, and
> uses theories and procedures across declared practical areas. Its later
> work meets a reliability target under a stated budget and external
> assessment protocol. An area is a consuming project's domain with an
> interface that can be declared and observed.

> **Comparative hypothesis.** Under matched demands and declared resources,
> this methodology produces useful capability gains over the frozen seed
> and a baseline that searches the raw records without the learned
> methodology. Its downstream reliability is comparable to a human-staffed
> builder's under a margin set before assessment. The computational
> comparisons use the same fixed-model constraint and account for both
> adaptation and task costs.

> **Reflection hypothesis.** A builder whose machinery changes pass through
> a causally connected self-theory acquires extensions that a matched
> builder without one does not, under the same demands, budget, and
> external assessment. Better downstream outcomes alone do not test this;
> the records of a [reflective episode](./main-path-episodes.md#2-reflective-machinery-revision)
> and a matched builder that retains content without a self-theory do.

None of the hypotheses promises success on every problem or within every
budget. The [protocol](./commonplace-evidence-protocol.md) records the
project, reliability target, comparison margin, task population, and budgets
that must be fixed before a run. No run is reported here. A result on one
project supports that assessed scope; breadth requires multiple declared
areas and evidence about transfer between them.

For this conjecture, “currently publicly available” means available as of
2026-09-17. An assessment must declare the model versions it uses and keep
their weights fixed. Public availability includes hosted models; it does not
require open weights. Model-weight updates and later model releases are
excluded from the assessment. The particular models remain to be selected;
this is a constraint on the research target, not on the general definition
of a theory builder.

## What closes the workshop

1. The protocol's freeze table is filled: consuming project and area,
   product assessed, seed, models, task supply, outcome contract, budget,
   horizon, reliability target, feedback, acquisition mode, and disclosure.
   The operator proposed an enterprise deployment as the first consuming
   project on 2026-09-19; it is settled when the enterprise agrees to the
   disclosure rules.
2. The [first experiment](./first-experiment.md) has been run and recorded,
   or replaced by a simpler one that still has a matched comparison.
3. At least one product-revision episode and one reflective episode have
   been run and recorded with the release, consumption, outcome, and
   feedback records the protocol requires, including the matched-ablation
   baseline and the control runs.
4. The recorded episodes are assessed against the
   [externally tested](../../notes/definitions/externally-tested-theory-builder.md)
   and [reflective](../../notes/definitions/reflective-theory-builder.md)
   definitions, and whatever the run broke in those definitions is returned
   to the library as a revision, not patched here.
5. The exact run records are retained under `kb/reports/retained/`, or,
   for a confidential project, the published part of them is: the
   declaration, measurements, summaries, prompt, and hashes. Any
   transferable finding becomes a note. The protocol either becomes an
   instruction, if a second run is wanted, or is retained with the records.

## Evaluation boundary

Evidence is the protocol and episodes as moved here, the library definitions
they cite, and the records the run produces. The
[boundary-case assessment](../../reports/retained/theory-builder-boundary-cases-20260917.md)
records how prior systems fare on the four deployment questions the run
must answer for Commonplace. No measurement exists yet; the protocol's own
statement that it is not evidence of a completed run stands until closing
condition 2 is met. The enterprise's early reports are development
feedback: they motivated the current fixes and are not assessment evidence.

## Coordination

- [explanatory-theories-deployment-time-learning](../explanatory-theories-deployment-time-learning/README.md)
  owns component-comparison experiment designs; this workshop runs the
  downstream comparison and does not redesign those.
- A definition the run breaks is revised in the library, with the run record
  retained as evidence. Retention thresholds and whether warranted revisions
  compose remain open in the
  [general-case obligations](../../notes/a-claim-without-external-assessment-carries-three-obligations.md).
  Whether reflection lowers total extension cost remains an empirical question
  for matched runs, including the cost of theory maintenance.

Write scope while open: this directory, plus `kb/reports/retained/` for
exact run records. Confidential raw records are never written to this
repository.
