# Sigma: transferable scan

**Status:** memory-first and source-ungrounded
**Recall confidence:** medium-high

## Remembered model

Sigma, associated with Paul Rosenbloom, is remembered as a hybrid or broadly unified cognitive architecture built on graphical models, especially factor-graph-style computation. Predicate-like symbolic structures compile into a graph where local functions and message passing support a range of capabilities, including uncertain reasoning, memory, learning, perception, and decision. The architectural wager is that one graphical substrate can provide both symbolic structure and probabilistic or numeric processing.

The exact language, compilation path, and supported capabilities need checking. The interesting question is methodological: when does a common formal substrate produce real integration rather than merely encode everything in the same notation?

## Provisional ontology

- **Predicate/relational structure:** the higher-level symbolic description of variables and relations.
- **Variable:** a quantity or symbolic choice whose value is inferred.
- **Factor/function:** a local constraint or compatibility relation over variables.
- **Factor graph:** a network connecting variables through local functions.
- **Message passing:** local propagation used to combine distributed constraints.
- **Working-memory state:** currently instantiated relational content.
- **Learning:** adjustment or construction of functions from experience.
- **Decision:** selection under the combined constraints and utilities represented in the graph.

This ontology suggests a spectrum between hard validation and soft evidence rather than a forced choice. Some factors can be absolute constraints, others graded preferences, likelihoods, or costs.

## Transfer candidates

- **`SIGMA-1` — represent hard and soft constraints distinctly but composably.** Schema validity, source authority, relevance, recency, and maintenance cost should not all become booleans or all become scores. A selection process can combine typed contributions while preserving their semantics.
- **`SIGMA-2` — test unification through translation removal.** A shared substrate is justified when it eliminates duplicated state, inconsistent adapters, or incompatible intermediate representations across real consumers.
- **`SIGMA-3` — prefer local update propagation for dependent state.** When one artifact or assumption changes, update only the affected constraints and consumers where dependencies permit, instead of reconstructing a monolithic global judgment.
- **`SIGMA-4` — make the compiled form inspectable.** If natural-language or symbolic declarations become a graph, expose the generated variables, factors, and messages so incorrect semantics can be diagnosed.
- **`SIGMA-5` — use conflict as information.** Inconsistent signals from evidence, authority, and utility should remain visible rather than disappearing into one aggregate score.

## Method worth borrowing

Pick one workflow currently crossing several representations—such as target selection using type validity, freshness, priority, and review history. Implement or simulate both the existing staged process and a unified constraint model. Compare semantic clarity, incremental update cost, explanation quality, and failure localization. The experiment should be allowed to show that unification is worse.

## Non-transfer and failure modes

- A common mathematical substrate can hide rather than resolve incompatible meanings.
- Probabilities or factor weights may be unjustified for qualitative judgments.
- Compilation creates a derived artifact whose lineage and correctness need validation.
- Generality can impose a heavy abstraction tax on simple deterministic operations.
- The remembered feature set may conflate demonstrated Sigma capabilities with roadmap aspirations.

## Grounding questions

1. What is Sigma's canonical source language and how is it compiled into graphical structure?
2. Which cognitive capabilities have been demonstrated in one integrated model?
3. How are symbolic, probabilistic, and decision-theoretic semantics combined?
4. What comparisons show an advantage from the unified substrate rather than its individual algorithms?
