# Deeplearning4j: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** high on category, not current feature set

## Remembered model

Deeplearning4j is remembered as a JVM-oriented deep-learning library and ecosystem, not as a cognitive architecture in the same explanatory sense as ACT-R or Soar. It supplies implementation machinery for neural models: layers or computation graphs, tensors, optimization, data pipelines, serialization, and deployment or distributed-training support. Its presence in the triggering comparison appears to be a category mismatch.

That mismatch is more valuable to this workshop than an attempt to extract a theory of cognition from library APIs.

## Provisional ontology

- **Theory:** claims about what cognitive capacities require and why a mechanism produces them.
- **Architecture:** an organized set of state types, processes, and interfaces intended to realize a range of cognitive functions.
- **Model:** a configured computational system trained or specified for some behavior.
- **Framework/library:** reusable implementation primitives from which models can be built.
- **Runtime substrate:** the environment that executes a model or architecture.
- **Application:** a deployed system solving a task.

One artifact can span categories, but comparison must say which role is under discussion. A library's support for online learning does not itself provide an ontology of goals, memory, attention, or action.

## Transfer candidates

- **`DL4J-1` — type comparison subjects before comparing features.** Add a "level of analysis" field to external-system surveys: theory, architecture, mechanism, framework, product, or application. Refuse absence-based comparisons across mismatched types.
- **`DL4J-2` — distinguish affordance from commitment.** A framework may make recurrence, graphs, or distributed training possible without requiring any of them. Architecture claims concern configured and behaviorally operative structure, not the menu of available primitives.
- **`DL4J-3` — evaluate implementation frameworks operationally.** Portability, observability, reproducibility, serialization, upgrade behavior, and deployment cost are legitimate comparison axes, but they answer engineering questions rather than cognitive-theory questions.
- **`DL4J-4` — prevent substrate vocabulary from colonizing methodology.** "Layer," "memory," "attention," and "graph" can denote implementation objects or functional roles. Reviews should identify which before drawing methodological conclusions.

This supports the existing separation among [storage substrate, representational form, lineage, and behavioral authority](../../notes/axes-of-artifact-analysis.md): implementation location and cognitive role are independent axes.

## Method worth borrowing

The main method is a type check at survey construction time. Before filling a feature matrix, write one sentence stating what kind of thing each row denotes and what evidence could establish each column. If rows require radically different evidence—paper argument for one, API documentation for another, benchmark for a third—the matrix probably collapses levels.

## Non-transfer and failure modes

- Rejecting Deeplearning4j as a cognitive architecture does not make software substrate irrelevant to cognition; implementation constraints can shape attainable behavior.
- "Framework" and "architecture" are not globally exclusive words. The operational question is what claims the comparison makes about the item.
- This memory-only scan should not assert anything about Deeplearning4j's current maintenance status or exact capabilities.

## Grounding questions

1. Why was Deeplearning4j added to the comparison, and was a particular cognitive system built with it intended?
2. Does the project itself ever claim to be a cognitive architecture?
3. Which current components belong to the core library versus its wider ecosystem?
4. What comparison schema would keep implementation affordances useful without treating them as cognitive commitments?
