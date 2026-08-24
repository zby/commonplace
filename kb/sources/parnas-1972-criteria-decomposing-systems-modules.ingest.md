---
description: "Parnas's KWIC comparison anchors why module boundaries should hide likely changes rather than mirror processing steps, while leaving downstream validation costs unproven."
source: https://www.win.tue.nl/~wstomv/edu/2ip30/references/criteria_for_modularization.pdf
captured: "2026-07-27"
capture: pdf-read
genre: scientific-paper
snapshot_sha256: 04374212e510279659911a6f60e80be529b0a932c2a7b492bb3fa506c65d0c2d
ingested: "2026-08-24"
type: kb/sources/types/ingest-report.md
domains: [software-architecture, modularity, information-hiding]
---

# Ingest: On the Criteria To Be Used in Decomposing Systems into Modules

## Classification

This is a peer-reviewed software-design paper that develops a decomposition criterion through two worked modularizations of the same KWIC system and a smaller compiler/interpreter example. Author: D. L. Parnas, then at Carnegie-Mellon University, writing in *Communications of the ACM* as the originator of the information-hiding criterion examined here.

## Summary

Parnas argues that dividing a system by its processing steps produces interfaces that expose shared representations and other design decisions, so later changes spread across modules. His alternative treats a module as a responsibility assignment: identify difficult or likely-to-change decisions, assign each to a module, and expose an interface that reveals as little of that decision as practical. The paired KWIC designs matter because both can execute identically while differing in independent development, change localization, comprehension, and reuse; runtime success therefore cannot decide whether the decomposition is good. For KB design, the paper is most useful as a primary anchor for choosing retained boundaries around change-bearing decisions, not as proof that any such boundary automatically limits every downstream validation cost.

## Claims

No claims have been grounded yet.
## Connections Found

The paper is a primary technical anchor for [Use tests a decomposition locally; retained rationale is what makes transfer testable](../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md): the two working KWIC decompositions show that execution can establish local adequacy without revealing which seam preserves the reason for transfer. It is also inherited evidence for [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md), specifically for matching boundaries to anticipated change, while not establishing that dependency closure or regression validation will remain bounded. The rival decompositions provide a concrete basis for [First-principles analysis maps a design space before selecting within it](../notes/first-principles-analysis-maps-design-space-before-selection.md), because comparison exposes design axes and consequences that the conventional flow-oriented decomposition alone does not reveal.

## Extractable Value

1. **Runnable equivalence underdetermines decomposition quality** -- The KWIC designs can yield the same assembled behavior while assigning knowledge and change responsibility differently, giving the transfer-testing note a primary example of why use tests alone cannot warrant a seam. [quick-win]
2. **Boundaries should follow volatile decisions, not execution order** -- The paper supplies the canonical mechanism behind change-localized retention: conceal representations, sequencing choices, and other likely changes behind narrow interfaces. [quick-win]
3. **Alternative decompositions reveal otherwise hidden design axes** -- Comparing flow-oriented and information-hiding modularizations operationalizes design-space mapping with consequences for independent work, comprehension, and reuse. [quick-win]
4. **A module is a responsibility assignment, not necessarily a subroutine** -- This distinction prevents a useful conceptual boundary from being rejected merely because a literal procedure call would add overhead; implementation and retained responsibility can use different representations. [just-a-reference]
5. **Change localization does not imply bounded validation** -- The source supports containing knowledge of a decision, but it does not analyze the full downstream dependency or regression-test radius, preserving the stronger note's stated boundary. [just-a-reference]

## Limitations (our opinion)

The central comparison is a worked design argument, not a controlled evaluation: the KWIC system is deliberately small, the author asks readers to treat it as if it were large, and the reported class-project use provides no comparative measures of development time, defect rate, modification cost, or comprehension. The proposed change scenarios are plausible but author-selected, and the claim that the second decomposition is easier to understand is explicitly subjective. The paper also sketches away possible runtime overhead through tooling rather than evaluating an implementation across realistic constraints. Most importantly for this KB, it supports aligning boundaries with anticipated change but does not show that doing so bounds downstream dependency closure or validation effort, as distinguished in [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md).

## Recommended Next Action

Update [Use tests a decomposition locally; retained rationale is what makes transfer testable](../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) to use this ingest as its local analytical source for the paired-KWIC example.
