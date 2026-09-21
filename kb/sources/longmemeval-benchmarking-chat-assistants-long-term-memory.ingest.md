---
description: "LongMemEval supplies a scalable chat-memory benchmark and bounded evidence that retrieval, representation, temporal selection, and reading fail independently."
source: https://arxiv.org/abs/2410.10813
captured: "2026-09-17"
capture: pdftotext
capture_scope: full-source
doi: "10.48550/arXiv.2410.10813"
genre: scientific-paper
snapshot_sha256: 4ed592b43f1ff88d548d536a67f0bc4b8165c79ef2cf5416226c4f3ecdb7ee5b
ingested: "2026-09-17"
type: kb/sources/types/ingest-report.md
domains: [agent-memory, context-engineering, memory-evaluation, retrieval]
learning_claims: true
---

# Ingest: LongMemEval and long-term interactive memory

## Classification

This is a peer-reviewed scientific paper that contributes both a benchmark and controlled design experiments for long-term chat memory. Author: a UCLA, Tencent AI Lab Seattle, and UC San Diego research team; the paper was published at ICLR 2025 and reports extensive human curation and a public benchmark and code release.

## Summary

LongMemEval evaluates whether chat assistants can extract information, combine evidence across sessions, reason about time, update user knowledge, and abstain when a premise is unsupported. Its 500 human-curated questions can be embedded in configurable histories, with released settings near 115,000 tokens or 500 sessions and 1.5 million tokens. The paper separates memory operation into indexing, retrieval, and reading, then tests value granularity, key expansion, temporal query expansion, and reading strategy. The most useful decision is not to adopt one reported configuration wholesale, but to evaluate each access-path stage separately: full-history readers lose substantial accuracy relative to evidence-only inputs, fact-augmented keys improve the tested retrieval pipeline, time filtering helps only when time-range inference is reliable, and answer generation still fails under oracle retrieval.

## Quotes

No source quotes have been retained yet.

## Connections Found

LongMemEval is a technical basis for [evaluating knowledge-access architecture end to end](../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md): it reports retrieval and downstream answer quality separately and varies reading strategy under oracle retrieval. It also supplies bounded evidence that [raw accumulation does not create usable memory](../notes/raw-accumulation-does-not-create-usable-memory.md), because long-context models receive histories containing the evidence yet perform substantially worse than when given only evidence sessions. Its value-representation results support the task-relative qualification in [an insufficient summary precedes the source rather than replacing it](../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md): fact-only or summary-only values usually lose answer-relevant detail, although fact decomposition helps the multi-session subset. Finally, its temporal-query ablation illustrates why [context selection needs an adequate signal](../notes/rule-based-context-selection-needs-a-pre-existing-signal.md): inferred ranges help when GPT-4o resolves the temporal cue, while a weaker extractor can invent a range and exclude relevant history. These are bounded conversational-QA effects, not evidence for the broader activation, lineage, governance, or lifecycle dimensions in [effects-based memory evaluation](../notes/agent-memory-requirements/evaluate-memory-by-effects.md).

## Learning Claims (our opinion)

The source's adaptive mechanism is online memory-state construction rather than conjectural learning. Interaction sessions and timestamps are converted into retrievable key-value items; learned extractors may derive facts and dated events, a retriever maps the current question to stored items, and a reader maps the selected history to an answer. This is accumulation plus learned transformation and selection. It does not revise an explicit, criticizable theory in response to failed cases, so it does not meet the KB's definition of [conjectural learning](../notes/definitions/conjectural-learning.md).

The effective update space is narrow and differs by experimental condition. The available signals are the sequential chat sessions, their timestamps, the question, and the question date. The available operations are fixed variants of session or round storage, LLM extraction, dense or sparse ranking, optional temporal filtering, top-k loading, and prompted reading. The extractors, retrievers, and reader models can express rich mappings within those inputs and operations, but the benchmark ontology, question types, evidence annotations, indexing/retrieval/reading partition, candidate memory representations, prompts, retrieval budgets, and model assignments remain outside the system's update space. The reported improvements therefore support local contrasts within this decomposition. They do not establish that the decomposition is necessary or better than a different context-operation interface, as warned by [learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).

The ablations nevertheless refine the KB's account of adaptation by showing that memory quality is jointly conditioned by representation, selection, and consumption. An ablation should be attributed only to the choice it changes: fact-augmented keys support that indexing contrast in the tested pipeline; temporal filtering supports query-time narrowing only with adequate range inference; Chain-of-Note plus JSON supports that reading treatment under oracle retrieval. None alone shows that stored memory changed behavior beyond benchmark answers or that errors drove a persistent revision of the memory design.

## Extractable Value

1. **Use separate retrieval and answer metrics for memory evaluations.** LongMemEval exposes recall, oracle-retrieval reading, and end-to-end QA, making it possible to locate failure before or after retrieval instead of treating retrieval as the outcome. [quick-win]
2. **Adopt the five-ability task matrix as a benchmark-design checklist, not as a complete memory definition.** Information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention cover important chat-memory failures while leaving activation, provenance, governance, maintenance, and non-QA behavior untested. [just-a-reference]
3. **Treat compression and memory granularity as task-relative choices.** Round-level values preserve detail better overall in the reported experiments, while fact decomposition helps multi-session aggregation; a single compressed representation should not be assumed to dominate across tasks. [experiment]
4. **Test selectors for harmful false-positive narrowing.** Time-range filtering improves recall with a strong range extractor, but the weaker extractor sometimes invents ranges for questions without usable temporal cues and prunes relevant history. [experiment]
5. **Keep fixed architectural choices outside an ablation's conclusion.** The experiments compare options inside an indexing/retrieval/reading pipeline; they do not test whether that partition or its supplied operation set is the right general decomposition of memory access. [deep-dive]

## Limitations (our opinion)

The benchmark is carefully curated but synthetic-heavy: its evidence conversations begin with LLM-generated user backgrounds and self-chat, then receive substantial human editing, while distractor histories mix simulated sessions with ShareGPT and UltraChat. Results therefore establish performance on this constructed personal-assistant QA regime, not on naturally evolving users, organizational knowledge, or open-ended agent work. The 500 questions offer broad ability coverage but limited evidence about subgroup variation, privacy-sensitive retention, deletion, provenance, conflicting sources, maintenance, or behavioral activation.

The commercial-system study is especially narrow and time-bound. It uses 97 questions, only three to six sessions per history, manual interaction during August 2024, and excludes assistant-side recall, abstention, and some temporal questions. Those results should not characterize current products or the full benchmark.

The design experiments also leave several causal boundaries open. Many settings keep the retriever, extraction model, prompts, top-k budgets, sorting, Chain-of-Note, and JSON formatting fixed; reported gains therefore identify only their tested contrasts, not a generally optimal memory architecture. Effects vary by reader, retriever, value granularity, and range-extraction model, and the paper does not compare its fixed three-stage interface with broader context-operation interfaces. Its LLM judge has strong but small per-category meta-evaluations, not exhaustive human validation. The benchmark and code were not independently executed for this ingest, so the reported outcomes remain paper evidence rather than a reproduction.

## Recommended Next Action

Update [Knowledge-access architecture must be evaluated end to end, not by retrieval alone](../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md) with LongMemEval as a bounded empirical case that separates retrieval from reading and answer quality, while stating that it does not evaluate activation, upkeep, or alternative context-operation interfaces.
