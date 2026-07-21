---
description: "Petrovska, Erjiage, and Kugele's systematic review quantifies the definition gap in self-adaptive-systems research and identifies uncertainty and goal semantics as missing formal dimensions."
source_snapshot: "defining-self-adaptive-systems-systematic-literature-review.md"
ingested: "2026-07-21"
type: kb/sources/types/ingest-report.md
domains: [self-adaptation, definitions, systematic-review, uncertainty]
---

# Ingest: Defining Self-adaptive Systems: A Systematic Literature Review

Source: defining-self-adaptive-systems-systematic-literature-review.md
Captured: 2026-07-21
From: https://arxiv.org/pdf/2505.17798

## Classification

Genre: scientific-paper -- a systematic literature review with explicit search, selection, voting, threats-to-validity, and reproducibility procedures.
Domains: self-adaptation, definitions, systematic-review, uncertainty
Author: Ana Petrovska, Guan Erjiage, and Stefan Kugele provide a recent multi-author review; its claims are bounded by the selected corpus and review protocol.

## Summary

The review searches 1,493 papers, selects 314 relevant papers, and finds only nine primary studies whose objective is to define self-adaptive systems formally. Only one formally defines adaptation itself; two specify adaptive behaviour implicitly; two specify MAPE behaviour while assuming adaptation follows. Context and system state are common formal dimensions, but none of the nine studies includes uncertainty, even though uncertainty motivates the field. Four studies include adaptation goals and only one distinguishes domain goals from adaptation goals. The authors conclude that MAPE-K is an engineering reference model lacking sufficient semantics for membership, and propose that future definitions distinguish adaptation from ordinary function, model uncertainty, and remain independent of collaboration/decentralisation.

## Connections Found

This source is direct evidence for [a proposal-selection loop requires search, evaluation, and retention](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), which already uses this review to caution that loop architecture does not settle category membership. It also reinforces [a self-improving system needs a profile, not a ladder](../notes/a-self-improving-system-needs-a-profile-not-a-ladder.md): the review's missing dimensions (uncertainty, domain versus adaptation goals, context, system state) are precisely reasons to report a multidimensional pathway profile. The review is a limitation/negative-result anchor rather than a replacement definition.

## Extractable Value

1. **Quantified definition gap (9/1,493 primary definition studies)** -- turns the intuition that the field lacks a settled definition into a citable systematic-review result. [quick-win]
2. **MAPE-K is not a semantic membership test** -- supports keeping proposal-selection architecture separate from self-improving-system category membership. [quick-win]
3. **Uncertainty is absent from all nine formal studies** -- a sharp warning for any Commonplace profile that claims adaptation without stating its uncertainty model or boundary. [quick-win]
4. **Domain goals versus adaptation goals** -- provides vocabulary for distinguishing what the managed artifact is for from what the updater is trying to optimise. [quick-win]
5. **Context and system state are indispensable dimensions** -- suggests that future self-ontology work must represent both the environment and the object being adapted. [deep-dive]
6. **Reproducible review protocol and threats** -- offers a method for auditing future definitional claims: complete-pool analysis, iterative query refinement, multi-reviewer voting, and explicit validity limits. [just-a-reference]

## Limitations (our opinion)

The review's conclusions depend on metadata queries, inclusion criteria, and the authors' interpretation of informal definitions; relevant work omitted the “self-adapt*” term may be missed. Nine primary studies are too few to establish that no useful definition exists outside the search boundary. The paper elicits requirements but does not validate a unified definition, so its result is a gap map and design constraint rather than a settled ontology. The corpus is software/systems engineering and may not transfer directly to organizational or biological notions of adaptation.

The source snapshot was refreshed from the user's full converted Markdown capture; the classification, connections, and recommended action remain supported. No inbound KB links to this ingest report required updating.

## Recommended Next Action

Update [a self-improving system needs a profile, not a ladder](../notes/a-self-improving-system-needs-a-profile-not-a-ladder.md) with the review's explicit uncertainty and domain-goal dimensions, keeping them as profile fields and not as a new single membership criterion.
