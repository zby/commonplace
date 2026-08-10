# Continual Harness governance experiment

## Goal

Determine whether Commonplace's existing theory of artifact-mediated
self-improvement can generate a controlled, falsifiable extension to Continual
Harness's reset-free online adaptation loop. The experiment should test whether
selected governance mechanisms improve the reliability of harness adaptation
without erasing the latency and task-performance advantages the original loop
is designed to provide.

This workshop does not assume that proposal selection is superior to direct
update. Continual Harness uses a direct Refiner-mediated update law: trajectory
evidence determines edits that enter the next step without a separately
rejectable candidate. The first obligation is therefore to describe and test
governance appropriate to that architecture. A reject-capable arm is one
possible comparison, not the definition of governance or a foregone design.

## Evaluation boundary

- The target phenomenon is reset-free online harness adaptation within the
  task episode. Whether a first experiment also includes weight updates remains
  a protocol choice; harness-only and model–harness co-learning answer
  different questions and must not be silently combined.
- Judge an intervention against matched task performance, failure-to-repair
  latency, harmful changes, recovery, and retained-artifact use and growth.
  Added machinery must pay for its own execution, context, and evaluation cost.
- Do not make a compounding claim. Cross-run transfer and evidence that an
  earlier improvement improves a later improvement are separate experiments.
- Keep controlled reach, improvement warrant, and bounded permission to
  experiment distinct. A conforming edit may be harmful; an uncertain edit may
  be safe enough to try; evidence for a process over a trajectory need not
  warrant every individual successor.
- Apply the fixed-decomposition lens. Results inside a fixed observation and
  action interface, harness partition, Refiner protocol, reward design, and
  task family do not validate those choices. An arm that revises the
  decomposition tests a different question from one that governs edits within
  it.

## Questions the design must settle

1. Which parts of Commonplace's theory become experimental interventions rather
   than post-hoc descriptions, and what observable result could disconfirm each
   intervention's expected value?
2. What is the minimum governed-direct-update condition: a declared write
   envelope, evidence-to-edit provenance, activation ordering, monitoring,
   bounded exposure, recovery, or some smaller combination?
3. Which checks can run before an edit becomes operative, and which claims can
   only be assessed from later execution? Do not call a check an acceptance
   gate unless its result can prevent activation or continued retention.
4. How should the experiment distinguish artifact creation, installation,
   invocation, behavioral effect, repair, supersession, and retirement? The
   paper's unused-skill and sparse-memory-use tails make write counts
   insufficient.
5. Which comparison isolates the governance mechanism under matched models,
   task states, trajectory evidence, budgets, and Refiner opportunities? A
   proposal-selection arm may be informative, but it also changes the update
   architecture.
6. What adverse result would make Commonplace narrow or reject the proposed
   intervention rather than explain the result away as an implementation
   failure?

## What closes this workshop

The workshop closes when it produces one of two dispositions:

1. a finished comparative design with a falsifiable question, justified arms,
   matched controls, outcome measures, cost accounting, confounds, and a named
   decision each possible result would change; or
2. a documented reason that the proposed application cannot isolate a useful
   test or would not earn its experimental cost.

If the design survives, promote it to the appropriate durable proposal or
research artifact. Extract any independently durable theoretical correction
into `kb/notes/`. Then delete this workshop and remove it from the active list;
the workshop itself is not a permanent research record.

## Bookkeeping

- Keep design alternatives, theory-to-intervention mappings, protocol drafts,
  criticism, and any trial material in this directory.
- Treat the Continual Harness snapshot and ingest as the source record. Do not
  annotate the immutable snapshot.
- Record experimental results only after a protocol identifies the run,
  conditions, evidence boundary, and deviations. Do not let a design sketch
  read as an observed result.
- Library artifacts may be cited from here, but library artifacts must not link
  back into this temporary workshop.

## Starting context

- [Ingest: Continual Harness](../../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) — source analysis, empirical bounds, direct-update classification, and artifact-use findings
- [Self-revision design-space discriminating tests](../self-revision-design-space/discriminating-tests.md) — distinguishes controlled reach, improvement warrant, and bounded-experiment authorization for direct updates
- [An omitted loop function and a frozen one need different repairs](../../notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md) — prevents treating Continual Harness's absent rejection stage as an omitted universal function
- [Learning inside a fixed decomposition inherits its mistakes](../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — bounds what improvement within the supplied update space can establish
- [Diagnostic richness constrains outer-loop learning quality](../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — grounds interventions on the evidence surface available to the Refiner
- [The readable-artifact loop is the tractable unit for continual learning](../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — supplies the validation-radius and artifact-form rationale
- [Choosing what to learn requires both validity and learning-value gates](../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) — candidate hypothesis for separating trustworthy updates from useful retained artifacts, without presupposing where those checks belong in a direct path
