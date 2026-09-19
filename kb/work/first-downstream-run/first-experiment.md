# The first experiment: operator interventions on one KB-building task

> **Status:** Proposed design, 2026-09-19. Nothing has been run. It follows
> the [downstream protocol](./commonplace-evidence-protocol.md), including
> its rules for a confidential consuming project.

## Why this one first

Early use of Commonplace in an enterprise produced one clear finding: the
framework is complex, and using it well asks the operator to learn a great
deal. The current work responds to that finding. It removes
inconsistencies, improves Windows support, and moves decisions from the
operator to the agent, so that the agent understands the options and the
operator does not have to.

That finding sits at the builder layer (see the
[README](./README.md#two-layers)): the product is the framework release,
and its consumer is a team building a KB with it. The first experiment
measures the thing the current work is trying to change, on one real task,
with the smallest design that still has a matched comparison. It needs no
production traffic, no long horizon, and no confidential data outside the
enterprise.

## The claim

On a KB-building task taken from the enterprise's real work, an agent using
the revised framework release needs fewer operator interventions to produce
an accepted KB than the same agent using the release the early trials used,
at comparable cost.

This is a product-revision episode in the protocol's terms: release A was
used, outside feedback reported a failure, the builder revised the product,
and release B is assessed on a later task against release A. It measures
how much internal human work the methodology needs, which the sufficiency
hypothesis depends on. It does not test that hypothesis, because people
made the revisions between A and B.

## Design

- **Task.** One KB-building task chosen by the enterprise colleague from
  real work: set up a KB in a fresh project and bring a given set of
  sources to an accepted state. She chooses it after release B is frozen,
  and it must not be a task whose failure guided the fixes.
- **Conditions.** Release A, the framework version the early trials used,
  and release B, the version after the current fixes. Both are pinned by
  commit. The agent harness, model version and settings, task inputs,
  operating system, and resource ceilings are the same in both.
- **Operator.** A scripted minimal operator. It hands over the task,
  answers questions about the task's subject matter from a fixed brief,
  and answers every question about the framework with "use your judgment".
  A person may play it, following the script.
- **Repeats.** Several runs per condition, to separate the release's effect
  from run-to-run variation. The number is declared before the first run.
- **Judge.** The colleague, or someone she names, accepts or rejects each
  resulting KB against criteria written before any run, without being told
  which release produced it.

## Declared before the first run

The task and its inputs; the two release commits; the model and settings;
the operator script and subject-matter brief; the acceptance criteria; the
number of repeats; the ceilings on time and tokens; what counts as an
intervention; and the disclosure fields the protocol requires (summarizer
model, prompt, and redaction rule).

## Measurements

Computed by code or counted by rule, not written by a model:

- framework questions the agent asked the operator;
- points where the run stopped and needed a person to continue;
- whether the KB was accepted, and the criterion behind each rejection;
- validator failures remaining at the end;
- elapsed time and tokens;
- for release B, which framework artifacts the agent read before each
  consequential decision, where the harness records it.

## What leaves the enterprise

The declaration, the measurements above, and one automatic summary per run
produced by the [pinned summarizer](./summary-prompt.md). Task inputs, KB
contents, agent transcripts, and the judge's free-text reasons stay inside.
Hashes of the raw records are published with the summaries.

## What it would and would not establish

A lower intervention count under B with no loss of acceptance supports the
claim for this task, this model, and this operating system. It does not
show that the KB helps the enterprise's own agents on their tasks, which is
the product layer's question. It does not attribute the difference to any
particular fix; that needs a run with the one fix removed. And one task is
one task: a second task of a different kind is the natural next step.

If B is no better, the record of where its runs stopped is the most useful
output, because it says what the agent still could not decide without a
person.

## Left open

The harness, the exact intervention rule, and whether a person or a program
plays the operator are for whoever runs it to choose, within the matched
conditions above. Windows is the enterprise's setting and is preferred; if
the two releases cannot both run there, say so and report the setting used.
