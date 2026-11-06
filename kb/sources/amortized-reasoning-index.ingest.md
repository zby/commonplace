---
description: "ARI reports persistent test-time retriever training from reasoning-model rankings, with held-out retrieval gains but agent-memory benefits still untested."
source: https://dianetc.com/musings/ari/
captured: "2026-11-06"
capture: trafilatura-with-resolved-links-and-image-alt
capture_scope: partial-source
genre: practitioner-report
snapshot_sha256: 1b0831ee1b2209bfb15b69189e707f1ebbafffd270f001ccc2ca1890532d43a9
ingested: "2026-11-06"
type: types/ingest-report.md
domains: [test-time-training, relevance-feedback, cross-encoder-retrieval]
learning_claims: true
---

# Ingest: Amortized Reasoning Index

## Classification

A first-party research blog reporting an implemented retrieval method and preliminary experiments, rather than a captured scientific paper. Authors Diane Tchuindjo, Devavrat Shah, and Omar Khattab describe their own system, experimental choices, and proposed agent-memory application. That direct implementation experience is the main author signal; the report is not independent verification.

## Summary

The Amortized Reasoning Index (ARI) trains a small retriever during search so that reasoning-model judgments can improve retrieval beyond the documents that model sees. In the reported implementation, an Ettin-0.4B cross-encoder retrieves its top 100 documents, Kimi-K3 ranks them in groups, and Bradley–Terry preference fitting supplies pairs for RankNet gradient updates. Three rounds per batch of 20 queries, with revisiting of earlier queries, produce weights retained for later batches. Within this cross-encoder and preference-training setup, the authors report 3.2–7× improvements in held-out Recall@100 across three tasks, without reasoning-model calls on evaluation queries. Two tasks guided development; BRIGHT AoPS was held out from development apart from adapting judge instructions. The authors also report substantial speedups from deep first-stage candidate filtering. These results concern retrieval on related query distributions, not general retrieval competence or demonstrated improvements in agent task outcomes; persistent agent memory remains a proposed application.

## Quotes

> In each experiment, ARI learns from a stream of unlabeled queries, and we score it with relevance labels on held-out queries, on which the retrieval system cannot invoke the reasoning model anymore.
> --- `kb/sources/.snapshots/amortized-reasoning-index.md` @ `sha256:1b0831ee1b2209bfb15b69189e707f1ebbafffd270f001ccc2ca1890532d43a9` — Preliminary Results, evaluation setup

> After 100 unlabeled queries (60 on BRIGHT AoPS), ARI’s Recall@100 on held-out queries grows 3.2× to 7×.
> --- `kb/sources/.snapshots/amortized-reasoning-index.md` @ `sha256:1b0831ee1b2209bfb15b69189e707f1ebbafffd270f001ccc2ca1890532d43a9` — Preliminary Results, Takeaway 1

> Going forward, we’re excited about turning ARI into a persistent memory for agents. Due to their limited context window, today’s agents go through redundant reasoning and issue similar queries each session. With ARI, each investigation by an agent over your data should leave the retriever better prepared to guide the next session.
> --- `kb/sources/.snapshots/amortized-reasoning-index.md` @ `sha256:1b0831ee1b2209bfb15b69189e707f1ebbafffd270f001ccc2ca1890532d43a9` — Introduction, proposed agent-memory application

## Connections Found

ARI is a concrete comparison case for [feedback-trained memory management's dependence on an evaluative signal](../theory/memory-management-policy-is-learnable-but-oracle-dependent.md): it replaces supplied relevance labels with reasoning-model preferences, not with an absence of supervision. Its signal concerns relative relevance rather than downstream task success. It also illustrates the boundary in [end-to-end knowledge-access evaluation](../theory/knowledge-access-architecture-must-be-evaluated-end-to-end.md). Held-out discovery improves within the tested cross-encoder training setup, but successful context construction, behavioral uptake, agent outcomes, and upkeep remain outside the reported tests. The source therefore supplies a retrieval-learning example and a limit on memory claims, not evidence that Commonplace should adopt this architecture.

## Learning Claims (our opinion)

On the source's terms, learning means persistent weight updates from relative relevance judgments. The retriever can generalize those preferences to unseen queries and unjudged documents; it need not store a separate textual lesson for each judgment. The accessible training history includes current candidates and revisited earlier queries, sometimes with fresh judgments. The reported held-out gains support improved future retrieval capacity on the tested distributions. They do not establish improvement on unrelated workloads or across changing corpora.

Against the [theory-builder definition](../theory/definitions/theory-builder.md), the described retrieval-adaptation loop has distinct strengths and boundaries:

- **Localized content:** query–document preferences are identifiable judgments, but the retained ranking policy is distributed across weights. The report does not show localized statements carrying that policy's content.
- **Consumption:** updated weights demonstrably guide later rankings according to the reported results. This supports operational influence, not consumption of a stated theory through what it says.
- **Content-directed criticism:** the judge compares documents, and training penalizes disagreement with those preferences. The described loop does not criticize stated explanations of relevance or reconsider the judge, loss, or training recipe through argument. Preference correction is not evidence of this condition.
- **Iteration:** successive searches use updated weights within a batch and later batches inherit them. This establishes retained adaptation, but not retention of the result of content-directed criticism, which has not been shown.

Persistence is reported across queries and batches in a task stream; persistence across independent sessions is envisioned rather than demonstrated here. Thus ARI is evidence for learning without the described loop qualifying as a theory builder. It does not challenge a definition that already separates those claims.

The [fixed-decomposition boundary](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) also matters. Weight updates change the cross-encoder's query–document scoring function, while the judge, grouping and preference conversion, loss, and training schedule remain supplied choices. The results show improvement inside that arrangement, not that it is preferable to alternative learning architectures. The serving experiment varies candidate-pool depth; its latency–quality trade-off does not isolate the necessity of weight updates, replay, or any other fixed training component.

## Extractable Value

1. **A concrete mechanism for retaining search judgments beyond a session's context.** Relative rankings become persistent retriever weights and reportedly improve held-out retrieval, including retrieval of documents never judged. Within the tested cross-encoder setup, this is useful evidence that reusable search experience need not take the form of retained prose. Its value is discovery improvement, not yet improved agent work. [quick-win]
2. **A discriminating test for relevance feedback versus outcome feedback.** ARI supplies a candidate for comparing preference-trained retrieval with retrieval trained from downstream task success. A Commonplace experiment would need fixed tasks and budgets, held-out queries, and downstream outcomes to establish whether the cheaper proxy preserves useful distinctions. The post does not run that comparison. [experiment]
3. **Separate coarse coverage from fine ranking.** In the reported Twitter-Conflict serving configuration, Qwen3-Embedding-4B's top 10,000 candidates retain 90% of the relevant tweets that full-scan ARI places in its top 100, despite its weaker final ranking. This is a context-bound example of a weak ranker being a useful deep filter, not a guarantee that a shallow retrieval stage preserves ARI's gains. [just-a-reference]

## Limitations (our opinion)

The capture is partial: main text, captions, and image alt text are available, but rendered plots, underlying data, and the separately linked appendix are not. It cannot establish the complete training recipe, uncertainty in the plotted results, or the detailed serving comparisons. No implementation was inspected or executed, and no result was reproduced.

The strongest comparison is the reported trajectory from the initial retriever to the adapted retriever within one supplied training arrangement. The embedding models are reference points with different architectures, training histories, and speed–quality trade-offs; they are not matched tests of learning versus no learning. The retained text supplies no controlled ablations isolating replay, preference conversion, judge quality, or weight adaptation against query-only feedback. Improvement therefore supports the compound recipe, not a causal attribution to each part or superiority over alternative decompositions.

Two tasks guided development, and the third still uses task-specific judge instructions. Twitter-Conflict evaluation uses pooled judgments from another LLM, leaving relevance measurement dependent on model judgments even though the evaluation judge differs from the training judge. Large multiplicative gains from weak starts do not establish broad retrieval competence; on BRIGHT AoPS, the source itself reports a remaining disadvantage to larger reference models in geometric-mean relevant-document rank. Long-term forgetting, changing corpora, misleading teacher preferences, and total adaptation costs are not established by the retained evidence. As the end-to-end evaluation note makes explicit, retrieval gains alone do not settle the proposed agent-memory benefit.

## Recommended Next Action

Review `kb/theory/knowledge-access-architecture-must-be-evaluated-end-to-end.md` for adding ARI as a bounded example of improved held-out discovery with agent-outcome benefits still untested.
