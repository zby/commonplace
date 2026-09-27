---
description: "Weco's product overview documents metric-driven code search, traceable experiments and human steering, while leaving criticism and recursive improvement unestablished."
source: https://docs.weco.ai/
captured: "2026-09-27"
capture: trafilatura
capture_scope: full-source
genre: official-statement
snapshot_sha256: 3bf630902aa0858f6d59d091343900d29b101608b9cefe8452ad9833f10264c2
ingested: "2026-09-27"
occasion: "Prepare source evidence for adding Weco/AIDE² to which-existing-self-improving-systems-are-theory-builders.md, examining reflective improvement, fixed-model learning, outer/inner loops, criticism, evaluation and compounding without presupposing theory-builder membership."
type: types/ingest-report.md
domains: [agentic-systems, code-optimization, evaluation]
learning_claims: true
---

# Ingest: Weco documentation overview

## Classification

An official product overview describing the advertised workflow, prerequisites and controls. It supplies a first-party account of intended behavior, not an empirical evaluation.
Author: Weco AI, the product developer.

## Summary

Weco describes a code optimization service using LLMs and AIDE tree search. Users supply code and an evaluation script that prints a numeric metric. Weco proposes changes, executes evaluations on the user's hardware, retains improvements and returns the best code found. Its dashboard exposes a tree of experiments and scores; users can steer a running search with natural-language instructions and branch to explore competing ideas. Listed applications include agent scaffolds, prompts, ML models and GPU kernels. The overview makes a measurable objective the main prerequisite, but supplies no measured outcomes, comparison with alternatives or detailed account of how feedback informs proposals.

## Quotes

No source quotes have been retained yet.

## Connections Found

For the requested Weco/AIDE² case, this is evidence about product controls and the division of work between users and automation. Compared with the [theory-builder definition](../notes/definitions/theory-builder.md), it documents retained code variants, execution and iterative selection, while leaving content-directed criticism unresolved. The [AIDE2 review](../agentic-systems/reviews/aide2.md) concerns nested harness improvement; this overview instead describes the general product and links the earlier AIDE algorithm. It does not independently establish that the advertised service implements AIDE²'s research configuration. The [oracle strength spectrum](../notes/oracle-strength-spectrum.md) supplies a useful comparison: requiring a number establishes an optimization interface, not the number's fidelity to the user's actual objective.

## Learning Claims (our opinion)

The described adaptation changes code through repeated proposal, execution, scoring and retention. The immediate signal is the supplied evaluation metric; the user can add instructions during search. A traceable experiment tree is available to the user, but the overview does not specify which parts of that history condition subsequent LLM calls.

Against the four theory-builder conditions, the evidence has different strengths. **Localized content:** code variants provide identifiable formal artifacts, although the overview does not show separately stated conjectures or rationales. **Consumption:** variants are executed, so their content governs evaluated behavior. **Criticism:** comparison by score is documented; stated reasons that identify errors in what a variant says are not. Human steering could provide such reasons, but its availability does not establish their use. **Iteration:** the account explicitly says that the system keeps improvements and builds on them, supporting feedback-dependent rounds within a run. Whether those rounds satisfy criticism, rather than selection alone, remains open.

The final code is retained and the dashboard exposes experiments. Reuse of criticism across runs or problems is unspecified. In Commonplace's terms, actual improved capacity for future action remains a separate empirical question: the page describes a plausible mechanism but supplies no result demonstrating it. No weight-update mechanism is described, but that absence does not establish that the base model remains fixed throughout every run.

The distinction in [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) applies to the documented scope: candidate code changes against a user-supplied evaluator; autonomous revision of the objective, evaluator or search procedure is not described. Optimizing an agent scaffold could change another agent's method, but this alone establishes neither reflection by the optimizer nor nested self-improvement. Human contributions belong inside a proposed builder boundary when they supply conjectures or criticism. The page establishes no compounding effect, such as a method change making later improvement more effective.

## Extractable Value

1. **A bounded product-level source for the Weco/AIDE² case.** Use the documented metric prerequisite, experiment tree and mid-run human steering to identify what the product exposes and who may perform internal operations. Keep AIDE²'s nested research loop attributed to its own evidence. [quick-win]
2. **A concrete limit on classification from product language.** Traceability and branching support inspection and comparison; neither demonstrates stated criticism of code content. This makes the overview useful for delimiting what remains to establish before calling the system a theory builder. [quick-win]
3. **An evaluation-interface example.** Numeric feedback is an explicit product prerequisite, while its relationship to real utility remains outside the account. This is a context-bound illustration of the distinction between having a metric and having a trustworthy evaluator. [just-a-reference]

## Limitations (our opinion)

This developer-authored overview has a promotional purpose. It contains no execution traces, benchmark results, implementation inspection or failure analysis. The broad language and hardware compatibility claim is not tested here. It cannot establish how the proposer diagnoses failure, which histories it consumes, whether evaluation can be exploited, or how accurately numeric gains represent useful improvement. The linked conceptual, example and research pages are outside this observation; their mechanisms and results cannot be imported into it. No runtime experiments were performed for this ingest.

## Recommended Next Action

Use this overview's product-boundary evidence in the Weco/AIDE² case in `which-existing-self-improving-systems-are-theory-builders.md`, keeping criticism, fixed-model operation and nested self-improvement dependent on separate supporting evidence.
