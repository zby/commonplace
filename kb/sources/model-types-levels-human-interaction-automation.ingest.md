---
description: "Parasuraman, Sheridan, and Wickens provide a human-centered function-allocation matrix: four automation stages crossed with manual-to-autonomous levels and evaluated by performance consequences."
source_snapshot: "model-types-levels-human-interaction-automation.md"
ingested: "2026-07-21"
type: kb/sources/types/ingest-report.md
domains: [human-automation, autonomy, function-allocation, evaluation]
---

# Ingest: A Model for Types and Levels of Human Interaction with Automation

Source: model-types-levels-human-interaction-automation.md
Captured: 2026-07-21
From: https://www.cs.uml.edu/~holly/91.550/papers/sheridan-autonomy.pdf

## Classification

Genre: scientific-paper -- a foundational human-factors model with a conceptual taxonomy and design criteria, illustrated by system examples rather than a single controlled experiment.
Domains: human-automation, autonomy, function-allocation, evaluation
Author: Raja Parasuraman, Thomas B. Sheridan, and Christopher D. Wickens are established human-factors researchers; the model is influential but explicitly qualitative and incomplete for newer automation stages.

## Summary

The paper argues that automation changes human work and coordination rather than simply replacing it. It decomposes automation into four stages—information acquisition, information analysis, decision/action selection, and action implementation—and lets each stage take a different level from fully manual to fully automatic. Designers choose candidate levels, evaluate workload, situation awareness, complacency, error, performance, reliability, consequences, cost, and liability, then iterate. The framework is deliberately non-prescriptive: high technical capability does not by itself justify high automation, and full automation can still leave a human role. The result is a multidimensional allocation profile, not a scalar autonomy ladder.

## Connections Found

The source supplies a concrete external precedent for [a self-improving system needs a profile, not a ladder](../notes/a-self-improving-system-needs-a-profile-not-a-ladder.md): autonomy is reported per function and level, while evaluation criteria and human authority remain separate. It also grounds [warranted autonomy is bounded by oracle domain](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md): moving a function toward automation is conditional on evidence about its failure costs and recovery, not on capability alone. No current note cites this specific human-factors matrix, so the connection is a transfer-of-vocabulary candidate rather than a settled Commonplace definition.

## Extractable Value

1. **Four-stage allocation matrix** -- a ready-made profile schema for recording who or what senses, analyses, selects, and executes in an improvement loop. [quick-win]
2. **Manual-to-full-automation continuum with intermediate veto/recommendation levels** -- supplies more precise vocabulary than “human-in/out of the loop.” [quick-win]
3. **Human-performance consequences as primary oracle** -- makes workload, situation awareness, complacency, and error explicit acceptance dimensions alongside task performance. [experiment]
4. **Reliability and consequence costs as secondary criteria** -- supports risk-weighted authority decisions and argues against capability-only automation. [quick-win]
5. **Adaptive automation can change levels at runtime** -- a useful distinction between static allocation and a system that reassigns functions as context or operator state changes. [deep-dive]
6. **Unresolved stage-specific scales and criterion weighting** -- a caution that a profile may be partial or incomparable across functions; do not force a single number where the paper leaves dimensions open. [just-a-reference]

## Limitations (our opinion)

The model is qualitative and primarily grounded in aviation, process control, and other human-machine systems; it does not test LLM or knowledge-base workflows. The ten-level scale is explicit mainly for decision/action selection, while other stages lack a validated level count. Criteria such as workload, situation awareness, and reliability can conflict, and the paper does not provide a universal weighting or quantitative decision rule. Treat the matrix as a transfer vocabulary and design heuristic, not evidence that a particular Commonplace allocation is safe.

The source snapshot was refreshed from the user's full converted Markdown capture; the classification, connections, and recommended action remain supported. No inbound KB links to this ingest report required updating.

## Recommended Next Action

Add the four-stage allocation vocabulary as an optional, explicitly human-inclusive sub-profile in [a self-improving system needs a profile, not a ladder](../notes/a-self-improving-system-needs-a-profile-not-a-ladder.md), preserving partial/unknown levels and keeping warranted autonomy as a separate evidence question.
