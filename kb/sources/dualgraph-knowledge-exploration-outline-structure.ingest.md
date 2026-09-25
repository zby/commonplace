---
description: "DualGraph separates research gaps from report structure; controlled ablations improve report quality while leaving total-cost, grounding and persistent-KB transfer questions open."
source: https://arxiv.org/abs/2602.13830
captured: "2026-09-24"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: af1be8dc4a43f9245e273237037413ef88c48b7d170c0cfca82481a51a09aabc
ingested: "2026-09-25"
type: kb/sources/types/ingest-report.md
domains: [agent-memory, knowledge-graphs, deep-research, context-engineering]
learning_claims: true
---

# Ingest: DualGraph separates knowledge exploration from outline structure

## Classification

A research preprint presenting an architecture, four benchmark evaluations, controlled ablations, cost measurements and extraction audits. The captured paper is arXiv v3, dated August 25, 2026. Authors Zhuofan Shi, Ming Ma, Zekun Yao and colleagues are affiliated with Microsoft, the Chinese Academy of Sciences and South China University of Technology. They evaluate their own system; this is reported experimental evidence, not an independent replication.

## Summary

[DualGraph](https://arxiv.org/abs/2602.13830) maintains a knowledge graph of evidence-linked entities, concepts and relations separately from an evolving report outline. Weakly supported relations and plausible missing links generate search candidates; an LLM selects queries using both the graph and outline, while supplementary outline queries can reach topics absent from the graph. A shared evidence bank supplies both structures and section-specific writing. Against an outline-only variant with identical initial outlines, queries and retrieved results, adding the graph raises GPT-5 report-quality RACE from 51.17 to 53.08 on DeepResearch Bench. This supports the combined graph-guided controller within the paper's fixed evidence-extraction and section-writing workflow, rather than establishing that two graphs are universally preferable. Mean refinement rounds fall from 3.88 to 3.23, but a separate twenty-case cost study reports more tokens and runtime. Effective citation counts rise while per-citation accuracy falls, so improved exploration should not be equated with uniformly improved grounding.

## Quotes

No source quotes have been retained yet.

## Connections Found

The strongest connection is a concrete experimental comparison for [Brainstorming how to enrich web search](../notes/brainstorming-how-to-enrich-web-search.md). DualGraph operationalizes the proposed temporary research graph's search-and-redirect role: relations across retrieved evidence expose questions that an outline alone may omit. Its controlled ablations support that role within a shared evidence-bank and section-writing workflow. They do not evaluate Commonplace's connection method or the brainstorming note's subsequent bridge into a persistent KB.

The paper also makes the distinction in [Context efficiency is the central design concern in agent systems](../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) concrete. Section writers receive selected evidence rather than the entire research history, yet the full workflow spends more aggregate tokens. Fewer refinement rounds therefore do not establish lower cost, and the paper does not isolate a per-window capability benefit from selective loading.

## Learning Claims (our opinion)

DualGraph adapts its research state within a task: new evidence adds relations, merges concepts, changes the outline and redirects subsequent searches. The authors also report correction or deletion of contradicted relations, including a reversed causal edge corrected after further retrieval in Appendix F. The graph's separately named relations provide the localization associated with [addressable theory](../notes/definitions/addressable-theory.md), and their contents influence later query generation. Missing-edge candidates are hypotheses to investigate, however, rather than supported relations merely awaiting insertion.

Against the four conditions of a [theory builder](../notes/definitions/theory-builder.md), conditions 1 and 2 are met: graph relations are stated claims, and their content steers query generation. Condition 3 (criticism) is met only at the strength of one reported example: a reversed causal edge is corrected after further retrieval contradicts it, which is criticism aimed at what a relation says; the extraction audit checks first-iteration triplets, not later corrections. Condition 4 (iteration) is met: the corrected graph and outline steer the next round of searches, across three to five refinement rounds until an outline rubric or round cap ends the run. DualGraph as evaluated is therefore a theory builder at the strength of one reported example, and condition 3 is the weak point. Persistence reaches the rounds of one run: the graph serves one report on one research question and is not carried into later tasks. Learning is a separate claim: the benchmark gains establish improvement for the compound controller, not that criticism of claims caused improved later capacity.

The mutable graph and outline sit inside a fixed entity/concept representation, extraction policy, search-chain rules and writing interface. As [learning inside a fixed decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) predicts, successful adaptation inside those choices does not establish their general adequacy. Outline-driven queries provide an additional route beyond the current graph; consequently, graph omissions alone do not establish that a topic is unreachable by the whole system. The source supports investigating editable research state, while leaving the broader representation choice unsettled.

## Extractable Value

1. **Use research relations to choose the next question independently of report organization.** The knowledge graph stores shared relations once, while outline sections reference evidence for presentation. Same-initialization comparisons support adding this controller to the paper's existing evidence-bank workflow. This is a concrete design comparison for the web-search brainstorming note, not evidence that Commonplace should adopt the exact graph schema. [quick-win]
2. **Distinguish strengthening a claim from investigating a possible relation.** Enrich ranks existing edges with sparse evidence; Explore proposes missing links using semantic similarity, community statistics and bridges between communities. An LLM filters these candidates and supplements them from the outline. The distinction is reusable for research planning, but evidence counts and topology remain prioritization cues, not truth tests. [experiment]
3. **Measure workflow cost and claim support separately from round count and citation volume.** The twenty-case cost comparison rises from 1.798 to 2.490 million tokens and from 30.68 to 36.75 minutes with the graph. On GPT-5, effective citations increase from 66.06 to 79.65 while per-citation accuracy declines from 61.15 to 57.55. These measurements bound reuse of the reported quality gains; an equal-budget comparison remains necessary for an efficiency claim. [quick-win]

## Limitations (our opinion)

**The ablations vary a bounded architecture.** All share initialization. The finer ablations disable early stopping and evaluate five rounds of intermediate outlines and accumulated search/evidence quality. Removing Enrich or Explore supports their contribution in this configuration. The entity-relation-only variant tests the additional topology signals as a group; it does not establish each signal's necessity. Substituting LightRAG's graph construction tests that module inside DualGraph, not LightRAG as a complete system. Alternative non-graph knowledge representations and equal-total-budget controllers are not compared.

**Evaluation gives narrower support than universal superiority or reliable grounding.** Most outcomes use model judges, without reported repeated-run uncertainty. Some proprietary outputs come from earlier work. DualGraph's DeepResearch Bench II total is 41.48, below Gemini's 45.89. A twenty-case joint-citation check gives near-equal accuracy for DualGraph and its outline-only variant, supporting a possible measurement-granularity explanation for the per-citation decline without proving every defect is an evaluation artifact. The human study asks annotators to assess already-shown model judgments over ten reports; it is not blind independent scoring of all benchmark outputs.

**Traceability and stopping do not establish completeness.** Persisting citation IDs through outline edits preserves references, not necessarily support for the revised claims. The 2.4% extraction anomaly rate concerns 6,014 first-iteration triplets; it does not audit every later edge or final claim. Later verification of an initially unsupported relation does not make its initial extraction grounded. Appendix D's shrinking-search-space argument assumes resolved gaps stay resolved, although graph growth and corrections can change the candidate space. An outline rubric threshold or five-round cap ends a run without proving knowledge completeness. No implementation was inspected or executed for this ingest.

## Recommended Next Action

Update [Brainstorming how to enrich web search](../notes/brainstorming-how-to-enrich-web-search.md) with DualGraph as a bounded comparison for temporary-graph query generation, preserving the untested persistent-KB bridge and the equal-budget evaluation gap.
