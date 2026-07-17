---
description: "Cerebras practitioner report on an internal enterprise knowledge base: source-native ingestion, Slack/code retrieval, MCP tools, project scoping, and multi-consumer activation"
source_snapshot: "how-we-built-our-knowledge-base-2077822555159945507.md"
ingested: "2026-07-17"
type: kb/sources/types/ingest-report.md
domains: [agent-memory, context-engineering, enterprise-ai, retrieval]
---

# Ingest: How we built our knowledge base

Source: [how-we-built-our-knowledge-base-2077822555159945507.md](./how-we-built-our-knowledge-base-2077822555159945507.md)
Captured: 2026-07-17T11:11:46.803761+00:00
From: https://x.com/cerebras/status/2077822555159945507

## Classification

Genre: practitioner-report -- Cerebras reports how it built and operates an internal knowledge base, including architecture choices, retrieval strategies, and adoption signals.
Domains: agent-memory, context-engineering, enterprise-ai, retrieval
Author: Official Cerebras post with named authors @hi_im_isaac_, @learnwdaniel, and @gaozenghao; high signal as a builder account, but vendor-positioned and not independently audited.

## Summary

Cerebras describes Cerebras Knowledge, an internal knowledge base used by employees, automations, and agents. The system rejects a single-platform "source of truth" migration and instead ingests information where it already lives: Slack, docs, code repositories, Jira-like metadata, and custom team databases. It stores embeddings, summaries, and metadata in a common Postgres-backed interface, uses specialized ingestion for Slack threads and code repositories, combines lexical, vector, IDF, recency, RRF, reranking, and context expansion at retrieval time, exposes low-level MCP retrieval tools to agents, and runs a fuller planner/executor/synthesizer path in the web UI. Projects and default scopes keep search relevant for teams and new employees.

## Connections Found

This source is a production enterprise-memory case for the KB's agent-memory and context-engineering notes. It corroborates that [agent memory is crosscutting](../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md): storage, ingress, retrieval, activation, governance, and action surfaces all matter. It also supports [raw accumulation does not create usable memory](../notes/raw-accumulation-does-not-create-usable-memory.md), [knowledge storage does not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md), [import external knowledge into internal form](../notes/agent-memory-requirements/import-external-knowledge.md), and [serve multiple consumers, not one retrieval interface](../notes/agent-memory-requirements/serve-multiple-consumers.md). The closest comparisons are [CocoIndex](../agent-memory-systems/reviews/cocoindex.md), because Cerebras reports using it for code indexing, and [Databricks memory scaling](./databricks-memory-scaling-ai-agents.ingest.md), another enterprise memory practitioner report.

## Extractable Value

1. **Source-native ingress beats forced platform consolidation** -- Cerebras gives a concrete enterprise example of importing Slack, docs, code, and custom databases without changing team behavior. This is direct evidence for import-as-distillation rather than "put everything in one app." [quick-win]
2. **Slack memory needs thread-level and subthread-level shaping** -- The report combines whole-thread refetch, LLM-extracted searchable questions/summaries/resolutions, and burst embeddings for high-signal message runs. This is a useful worked example for chat-derived memory beyond raw transcript indexing. [experiment]
3. **Hybrid retrieval is a bundle, not a slogan** -- Full-text search, embeddings, IDF, age decay, RRF, reranking, duplicate merge, per-file caps, and neighbor-section expansion each address a specific failure mode. That makes the source useful as a retrieval-design checklist, not just evidence that "vector + keyword" works. [quick-win]
4. **CocoIndex has a reported production deployment in code memory** -- Cerebras uses CocoIndex to incrementally update code embeddings and avoid reprocessing whole repositories, adding deployment evidence to the existing code-grounded [CocoIndex](../agent-memory-systems/reviews/cocoindex.md) review. [just-a-reference]
5. **MCP and web UI split retrieval authority differently** -- The MCP surface exposes simple, mostly LLM-free retrieval primitives, while the web UI owns planning, fan-out, normalization, synthesis, and citations. This cleanly illustrates multiple consumer surfaces over one substrate. [experiment]
6. **Project defaults are activation infrastructure** -- Default projects scope sources before a user asks a question, helping new employees get high-signal answers without knowing which channels, repos, or databases matter. This is a practical symbolic-scoping pattern for enterprise memory. [experiment]
7. **Authorization, auditing, and analytics belong in the memory platform** -- Cerebras treats auth/audit as one of the system's three core layers, which is a useful enterprise counterweight to memory designs that discuss retrieval without access control. [deep-dive]

## Limitations (our opinion)

This is an official practitioner report, not a paper or code-grounded review. The source reports adoption and architecture but does not expose implementation code, evaluation data, query sets, failure cases, latency/cost numbers, access-control details, deletion semantics, or ablations separating each retrieval component's contribution.

The visible claims are plausible but selected. "15,000 questions every day" signals adoption, not answer quality. The retrieval stack may work because the corpus and organizational vocabulary are unusually suited to the chosen source/project model. The report also does not show how stale, private, contradicted, or low-quality source material is detected and retired after ingestion.

The snapshot includes the linked article body, but the capture contains hidden or mojibake-like characters around some embedded material. The substantive prose is readable enough for ingestion; do not treat exact formatting or references as a clean canonical copy without checking the original blog.

## Recommended Next Action

Write a doc-grounded lightweight review at `kb/agent-memory-systems/lightweight/cerebras-knowledge.md`, using this snapshot as the source and classifying Cerebras Knowledge on the existing memory-system axes: storage substrate, representational form, read-back direction, read-back signal, write agency, curation operations, governance, and borrowable ideas.
