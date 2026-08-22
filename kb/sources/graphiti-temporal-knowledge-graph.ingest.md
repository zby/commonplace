---
description: "Graphiti design summary: raw episodes, LLM-derived temporal graph facts, hybrid retrieval, and an unresolved clean-store replay boundary"
source: https://github.com/getzep/graphiti
captured: "2026-03-05"
capture: manual
genre: design-proposal
snapshot_sha256: c2327d5a49dfea8ba9492ee1f71c3a4227cac6d91b5109f5f92ebc87c3b685c2
ingested: "2026-03-09"
type: kb/sources/types/ingest-report.md
domains: [agent-memory, knowledge-graphs, temporal-data, retrieval-systems]
---

# Ingest: Graphiti: Temporal Knowledge Graph for AI Agents

## Classification

The snapshot describes and advocates an implemented architecture for agent memory: a temporal knowledge graph with a defined node-and-edge model, graph-database backends, and an LLM-driven ingestion pipeline. A later [code-grounded review](../agent-memory-systems/reviews/graphiti.md) is the stronger local account of what the pinned implementation does.

Author: Zep publishes Graphiti as the open-source core behind its commercial context-engineering product. That gives the authors direct implementation knowledge and a commercial interest in the graph-first framing; this snapshot provides no independent deployment or outcome evidence.

## Summary

Graphiti accepts text, JSON, and message episodes, extracts entities and factual relationships with LLMs, resolves them against existing graph state, attaches provenance and validity intervals, and serves the result through semantic, keyword, and graph retrieval. Its useful distinction is between episodes that preserve imported or trace material and generated facts, summaries, embeddings, duplicate resolutions, and invalidation judgments. Those state classes coexist in a graph database but do not thereby have the same lineage or authority. Graphiti demonstrates temporal graph operations and a path for reprocessing retained episodes; the available evidence does not establish either that its generated graph is irrebuildable or that clean reprocessing reproduces equivalent graph state.

## Connections Found

The later [Graphiti review](../agent-memory-systems/reviews/graphiti.md) is now the primary technical companion to this snapshot. At pinned commit `34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6`, it classifies episodes as imported or trace-extracted source material and entities, facts, timestamps, summaries, duplicate resolutions, contradiction decisions, and communities as generated views. The implementation's bulk path accepts retained raw episodes and constructs nodes, edges, provenance, and invalidations from them. This supports reprocessing, but not a deterministic replay contract: outputs can depend on the configured LLM, embedder, ontology, prompts, ordering, and graph context.

Graphiti therefore compares with [canonical files deferring a shared schema while database authority remains a separate commitment](../notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md), rather than supplying a database-forcing boundary. A graph database can contain source records, generated views, and accepted judgments at once; substrate alone does not classify them. The note now omits Graphiti because the evidence does not decide which generated assertions, if any, are accepted commitments that retained inputs and a declared replay rule cannot determine. The sharper contrast is [kgai](../agent-memory-systems/reviews/kgai.md), whose append-only source log, deterministic replay, throwaway graph, and canonical digest explicitly establish a rebuild contract that Graphiti does not document.

Graphiti remains a concrete case for [temporal memory as a lifecycle capability](../notes/agent-memory-requirements/retire-redact-supersede-relax.md): validity and invalidation timestamps support current and point-in-time queries while retaining superseded facts. Across the [agent-memory systems comparison](../agent-memory-systems/agentic-memory-systems-comparative-review.md), that capability is one design axis among lineage, curation, activation, and verification; it is not evidence that graph storage determines those other properties.

## Extractable Value

1. **Classify mixed graph state per state class.** Episodes, extracted facts, embeddings, summaries, and invalidation judgments share a database while carrying different lineage and authority. Treating the whole graph as either canonical or derived erases the distinction the implementation itself exposes. [just-a-reference]

2. **Separate reprocessing from reproducible rebuild.** A bulk ingestion path from retained episodes defeats an absolute claim of irrebuildability. It does not show that a fresh store will reproduce the same entities, edges, validity intervals, deduplication decisions, summaries, or search behavior. [experiment]

3. **Temporal invalidation is an implemented lifecycle mechanism.** Graphiti retains superseded facts with validity windows instead of simply overwriting them, giving point-in-time queries a concrete data model. This supports the existing lifecycle note without deciding the canonical substrate for other KB state. [just-a-reference]

4. **LLM resolution introduces judgment-bearing state.** Entity resolution, edge deduplication, contradiction detection, timestamp extraction, and summaries can add decisions not mechanically entailed by episode text. Such outputs need declared model and prompt inputs, retained rationale or evidence, and an acceptance policy before they carry durable epistemic authority. [deep-dive]

5. **A graph earns its operational role through workload-specific capabilities.** Hybrid retrieval, multi-hop traversal, group scoping, provenance links, and temporal filtering are concrete reasons to operate Graphiti. They justify evaluating a graph implementation for those workloads, not inferring canonical authority from graph topology or database use. [just-a-reference]

## Limitations (our opinion)

This snapshot is a manually written architectural summary, not a verbatim repository capture, benchmark, or independent deployment report. It is useful for orientation but should not override the later code-grounded review. The snapshot describes capabilities without measuring retrieval quality, temporal-query value, extraction error, latency, cost, or behavior change. Zep's commercial interest also favors the graph-first framing.

The rebuild question remains open in both directions. The pinned implementation can clear a store and process `RawEpisode` inputs, but the inspected material does not provide a supported export-and-rebuild contract or compare two clean ingestions. Reproducing an episode corpus would also require retaining its identifiers, reference times, source metadata, group and saga scope, entity and edge schemas, extraction instructions, model and embedder versions, prompts, ordering, and any other context that affects resolution. Even with those inputs pinned, stochastic or provider-level variation may change generated state. Conversely, the absence of an equivalence test cannot support the old absolute claim that rebuilding is impossible.

Graphiti's own terminology is broader than Commonplace's narrow use of derivation. Calling a fact "derived" records source lineage, but an LLM extraction or contradiction judgment may add a resolution the episodes do not determine. Whether that resolution is a disposable generated view, a retained candidate, or accepted ground truth depends on the system's replay and acceptance contract, which this snapshot does not specify.

## Recommended Next Action

Run one clean-store replay experiment at the pinned Graphiti commit: ingest the same retained `RawEpisode` corpus twice with identifiers, timestamps, ordering, ontology, extraction instructions, LLM, embedder, and prompts pinned; compare episodes, entities, edges, validity and provenance fields, summaries, and representative search results; then record the result in the [code-grounded Graphiti review](../agent-memory-systems/reviews/graphiti.md) before classifying any generated graph state as reproducibly derived.
