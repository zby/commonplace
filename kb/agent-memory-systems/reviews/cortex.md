---
description: "Cortex review: local RDF/SQLite cognitive knowledge system with ontology, hybrid retrieval, MCP serving, reasoning, and trace-derived tier learning"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-06-03"
---

# Cortex

Cortex, by Abbacus Group's `abbacusgroup/cortex` repository, is a local Python knowledge system for AI agents. It stores typed knowledge objects in an Oxigraph RDF graph and a SQLite content database, runs a classify/link/enrich/reason pipeline, exposes the result through CLI, MCP, REST, and dashboard surfaces, and uses access/feedback traces to adjust memory tiers. At the reviewed commit, it is closer to a local graph intelligence service than to a file-vault memory layer: retained knowledge is database state, and the main agent interface is MCP tool calls.

**Repository:** https://github.com/abbacusgroup/cortex

**Reviewed commit:** [a51c2209eb6d26812c19c97aaade3cb64ccfc23c](https://github.com/abbacusgroup/cortex/commit/a51c2209eb6d26812c19c97aaade3cb64ccfc23c)

**Last checked:** 2026-06-03

## Core Ideas

**A dual store separates graph semantics from retrieval content.** The README describes Oxigraph plus SQLite as the storage pair, and the code makes `Store.create()` dual-write every knowledge object into `GraphStore` and `ContentStore`, rolling back the graph write if SQLite insert fails ([README.md](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/README.md), [src/cortex/db/store.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/db/store.py)). SQLite is content-authoritative for document reads, FTS5, embeddings, config, and query logs; Oxigraph owns RDF object/entity/relationship structure and SPARQL reasoning ([src/cortex/db/content_store.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/db/content_store.py), [src/cortex/db/graph_store.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/db/graph_store.py)).

**The ontology is an actual system contract.** `ontology/cortex.ttl` defines eight knowledge-object classes, entity classes, relationship properties, provenance fields, temporal fields, tiers, and pipeline-stage fields. The reasoner applies authored SPARQL `CONSTRUCT` rules for symmetric contradictions, causedBy/ledTo inverses, and transitive supersedes closure, writing inferred triples back to the graph ([ontology/cortex.ttl](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/ontology/cortex.ttl), [src/cortex/pipeline/reason.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/pipeline/reason.py)). This gives Cortex more symbolic authority than a plain vector-memory SDK: relationship labels are not just prose labels.

**Capture runs through an intelligence pipeline with graceful degradation.** `PipelineOrchestrator.capture()` ingests the object, optionally renders a typed template, then runs normalization, linking, enrichment, and reasoning as independent stages that can fail without aborting the whole pipeline ([src/cortex/pipeline/orchestrator.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/pipeline/orchestrator.py)). Normalization uses an LLM for type, summary, tags, project, entities, confidence, and type-specific properties when configured, but falls back to a low-confidence idea rather than requiring a model ([src/cortex/pipeline/normalize.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/pipeline/normalize.py), [src/cortex/services/llm.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/services/llm.py)).

**Context efficiency is handled by retrieval mode and presentation shape, not by file navigation.** Search combines SQLite FTS5/BM25, optional embedding similarity, graph connectivity, and recency, then returns a bounded result list with score breakdowns ([src/cortex/retrieval/engine.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/retrieval/engine.py)). `cortex_context` wraps search in `BriefingPresenter`, which returns only ids, titles, types, tags, projects, summaries, tiers, and scores; `cortex_read` returns the full document; dossier, synthesis, graph, and alert presenters shape larger views for specific use cases ([src/cortex/retrieval/presenters.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/retrieval/presenters.py), [src/cortex/transport/mcp/server.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/transport/mcp/server.py)). The volume bound is mostly top-k and presenter choice. The complexity bound is weaker: a dossier can traverse entities, contradictions, and timelines, but the system does not expose a progressive file tree or source-grounded reading ladder.

**MCP is the canonical agent integration surface.** The MCP server constructs the store, pipeline, retrieval engine, graph queries, and learning loop, then exposes public tools for search, context, dossier, read, capture, link, feedback, graph, list, classify, and pipeline; localhost/admin surfaces add status, synthesis, delete, reason, query trail, graph data, safety check, export, and debug tools ([src/cortex/transport/mcp/server.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/transport/mcp/server.py), [llms.txt](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/llms.txt)). The CLI now routes ordinary commands through the running MCP HTTP server by default, and REST/dashboard surfaces are also thin clients of that server, so one process owns the graph database lock ([src/cortex/cli/main.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/cli/main.py), [src/cortex/transport/api/server.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/transport/api/server.py)).

**Learning is small but real.** `RetrievalEngine.search()` logs queries and result ids. `cortex_read`, direct CLI `read`, and positive `cortex_feedback` call `LearningLoop.record_access()`, which persists per-object access counts and last-access timestamps in the SQLite config table; after ten accesses it promotes the object to `reflex` tier ([src/cortex/retrieval/engine.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/retrieval/engine.py), [src/cortex/retrieval/learner.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/retrieval/learner.py), [src/cortex/transport/mcp/server.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/transport/mcp/server.py), [src/cortex/cli/main.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/cli/main.py)). Miss detection and ranking-weight persistence exist as library methods, but I did not find deployed code that turns misses into automatic weight updates.

## Artifact analysis

- **Storage substrate:** `graph` — The lead substrate is Oxigraph/RocksDB graph storage at `graph.db`, paired with SQLite/WAL content, FTS, embedding, config, and log storage at `cortex.db`; generated service config under `~/.cortex/.env` and process/service files support deployment.
- **Representational form:** `prose` `symbolic` `parametric` — Central artifacts combine prose object content and summaries, symbolic RDF triples/OWL classes/SPARQL rules/SQLite rows/tool schemas, and distributed-parametric embedding vectors when embeddings are installed.
- **Lineage:** `authored` `imported` `trace-extracted` — Knowledge arrives through authored captures, V1/Obsidian imports, pipeline-derived graph/index state, and query/read/feedback traces that update logs, counters, and tiers.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Stored objects and query logs advise future work; ontology, tool schemas, service boundaries, pipeline stages, retrieval indexes, tiers, and feedback-derived access state shape classification, retrieval, presentation, and lifecycle behavior.

**Knowledge objects.** Storage substrate: dual-written Oxigraph triples plus SQLite `documents` rows, with `raw_markdown`, content, type, project, tags, summary, tier, pipeline stage, confidence, provenance, and timestamps in SQLite. Representational form: mixed prose and symbolic metadata. Lineage: captured through CLI, MCP, REST/dashboard, V1 import, Obsidian import, or templates; LLM or agent-supplied classification can derive summaries, tags, entities, and properties. Behavioral authority: knowledge artifact when searched/read as evidence or context; system-definition artifact when its type, tier, confidence, relationships, and pipeline stage affect ranking, reasoning, alerts, or downstream classification.

**Ontology, relationship graph, entities, and inferred triples.** Storage substrate: authored TTL ontology plus Oxigraph graph database. Representational form: symbolic RDF/OWL/SPARQL. Lineage: ontology is package-authored; object/entity triples are captured or pipeline-derived; inferred triples are generated by reasoner rules from existing relationships. Behavioral authority: system-definition artifact for classification vocabulary, relationship legality, graph navigation, inference, contradiction/staleness detection, and dossier assembly.

**SQLite FTS index, embeddings, and retrieval weights.** Storage substrate: SQLite FTS5 virtual table and triggers, `embeddings` table, and config keys such as `retrieval_weights`. Representational form: mixed symbolic index/config plus distributed-parametric vectors. Lineage: FTS is regenerated from document title/content/tags; embeddings are derived from title plus truncated content; weights default from code or are persisted by `LearningLoop.update_weights()`. Behavioral authority: ranking authority over which memories an agent sees first. Retrieval quality and calibration are not verified from static code.

**Query logs and access-derived tier state.** Storage substrate: SQLite `query_log` rows and config key-value records for `access_count:{id}` and `last_access:{id}`. Representational form: symbolic JSON and counters. Lineage: trace-derived from searches, reads, and explicit positive feedback. Behavioral authority: query logs are mostly audit/diagnostic knowledge artifacts; access counts and last-access records become system-definition artifacts when they promote objects to `reflex` or demote inactive reflex memories back to `recall`.

**Pipeline outputs.** Storage substrate: updates in SQLite documents, Oxigraph triples, entity nodes, mention edges, relationship triples, embeddings, and inferred triples. Representational form: mixed prose summaries plus symbolic object/entity/relationship state and optional embedding vectors. Lineage: derived from raw capture content, caller-supplied MCP classification, LLM classification/relationship prompts, deterministic enrichment rules, and SPARQL inference rules. Behavioral authority: routing, ranking, reasoning, alert, dossier, and context-briefing authority; these outputs decide what is found, how it is framed, and whether stale/contradictory/gap alerts are produced.

**MCP, CLI, REST, dashboard, setup, and service artifacts.** Storage substrate: package code, installed MCP config in Claude Code settings, launchd/systemd service files, `.env`, logs, and dashboard templates. Representational form: symbolic tool schemas/API routes/service definitions plus prose tool descriptions and setup prompts. Lineage: authored by the project and generated by setup/install/register commands. Behavioral authority: system-definition artifact authority, because these surfaces decide who can call capture/search/delete/reason tools, whether admin tools are localhost-only, and whether agents are instructed to use Cortex through MCP.

The promotion path is explicit but narrow: raw captured content can become a normalized, linked, enriched, reasoned object; repeated reads or positive feedback can promote the object to `reflex`; manual classify/link/pipeline calls can strengthen metadata and relationships. What Cortex does not yet provide is a review-grade promotion boundary from "frequently accessed" to "trusted instruction." Access-derived reflex status is useful activation metadata, not epistemic validation.

## Comparison with Our System

| Dimension | Cortex | Commonplace |
|---|---|---|
| Primary purpose | Local cognitive knowledge service for agents, with graph reasoning and MCP serving | Git-native methodology KB with typed artifacts, validation, review, and generated indexes |
| Main substrate | Oxigraph RDF graph plus SQLite content/FTS/embedding/log database | Git-tracked Markdown notes, instructions, ADRs, reviews, source snapshots, schemas, and indexes |
| Retrieval | Hybrid BM25 + embeddings + graph + recency, exposed through MCP/CLI/API | `rg`, curated indexes, descriptions, links, skills, validation/review workflows |
| Context strategy | Top-k search, summary briefing, full read, dossier/synthesis/presenter modes | Collection routing, progressive lexical search, authored links, generated indexes, review reports |
| Governance | Ontology, relationship vocabulary, local admin-tool gating, diagnostics, backup/restore | Collection contracts, type specs, schemas, deterministic validation, semantic review, archive lifecycle |
| Learning loop | Query/read/feedback traces update access state and tiers | Mostly explicit authoring/review/promotion; traces are captured only when operators decide to retain them |

Cortex and Commonplace both reject "just a vector store" memory. Cortex makes that rejection database-native: OWL classes, RDF relationships, SPARQL inference, FTS, embeddings, query logs, and MCP tool schemas are all first-class state. Commonplace makes the same move in a repo-native direction: Markdown artifacts, schemas, collection contracts, generated indexes, and review workflows remain inspectable in git.

The strongest divergence is trust. Cortex can classify, link, infer, and retrieve more automatically, but much of that authority is derived from LLM outputs, repeated access, and database-side state. Commonplace makes fewer automatic inferences but keeps source lineage and review status more visible. For an agent-memory system, Cortex is stronger at live service integration and graph intelligence; Commonplace is stronger at source-readable governance and artifact lifecycle.

**Read-back:** `pull` — Retained memory reaches an agent when the agent, CLI, dashboard, REST route, or user explicitly calls `cortex_search`, `cortex_context`, `cortex_dossier`, `cortex_read`, graph, list, or synthesis tools; shipped MCP descriptions and `llms.txt` best practices are baseline instructions, not accumulated memory push.

### Borrowable Ideas

**Make relationship vocabularies executable where they are already controlled.** Cortex's OWL/RDF layer is heavier than Commonplace needs for prose notes, but the SPARQL-rule pattern is a useful reminder: if a relationship vocabulary declares transitive, inverse, or symmetric semantics, some of those semantics can be checked or materialized. Ready only for high-value link labels; otherwise it is infrastructure before need.

**Expose "briefing" and "document" as different read surfaces.** Commonplace has search snippets, descriptions, indexes, and full files, but Cortex's named presenter split is easy for agents to choose. A Commonplace command could expose `brief`, `dossier`, and `read` modes over notes without changing the underlying Markdown. Ready when there is a concrete agent-facing CLI use case.

**Centralize multi-client writes behind one local owner process.** Cortex's MCP HTTP server owns the graph store so CLI, dashboard, and REST do not fight the database lock. Commonplace's git/file substrate does not need a daemon for normal writing, but a future high-volume index or review service might borrow the "single writer, thin clients" shape. Needs a storage bottleneck first.

**Keep query logs as maintenance signals, not automatic truth.** Cortex query logs and access counts are useful for finding what agents actually consult. Commonplace could record failed searches or repeated lookups as coverage-pressure reports, but should keep promotion to durable claims behind review.

**Do not borrow access-count trust.** Cortex's `reflex` promotion is operationally sensible, but Commonplace should not treat repeated reads as evidence that a note is correct or instruction-worthy. Usage can prioritize review; it should not replace review.

## Trace-derived learning placement

**Trace source:** `tool-traces` `event-streams` — Cortex consumes query/search calls, object reads, and explicit feedback events rather than full conversation transcripts.

**Learning scope:** `per-project` `cross-task` — The loop is local to a Cortex data directory and object/project metadata, while accumulated access state can affect later searches across tasks in that store.

**Learning timing:** `online` — Query logging, read access counting, positive feedback, and tier promotion happen during normal MCP/CLI use.

**Distilled form:** `symbolic` — Trace-derived state is retained as query-log rows, JSON/counter config records, timestamps, and tier values rather than prose lessons or model weights.

**Trace source.** Cortex consumes search traces through `query_log`, read traces through `record_access()`, and explicit relevance traces through `cortex_feedback`. The trace boundary is small and tool-level: query text/result ids/duration/session id, object reads, and positive feedback events, not full conversation transcripts.

**Extraction.** Extraction is deterministic. Search writes a query log entry with parameters and result ids; read and feedback increment `access_count:{obj_id}`, write `last_access:{obj_id}`, and trigger promotion after ten accesses. `adjust_tiers()` can later promote frequently accessed objects or demote inactive reflex objects. `detect_miss()` exists as a recognizer for "searched, then read an object not in results," but I did not find a deployed path that uses it to tune retrieval.

**Scope and timing.** The loop is local to a Cortex data directory and runs online during normal MCP/CLI use. Query logs are retained for dashboard/admin inspection. Access counts immediately affect tier promotion at read/feedback time; demotion requires an explicit adjustment call.

**Survey placement.** Cortex belongs in the trace-to-ranking/lifecycle branch of the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md). It strengthens the survey's distinction between raw trace artifacts and distilled behavior-shaping artifacts: raw queries are mostly audit knowledge, while access-derived tier state changes future retrieval and presentation authority. It is not transcript distillation and does not generate new rules, tools, or prose lessons from sessions.

## Curiosity Pass

The project calls the tiers `archive`, `recall`, and `reflex`, but the implementation makes `reflex` a retrieval/lifecycle tier, not automatic behavioral injection. A reflex object is more privileged inside Cortex state; it is not necessarily pushed into every agent prompt.

The LLM contract is split in an interesting way. Direct pipeline normalization can ask Cortex's configured LLM to classify, but the MCP `cortex_capture` tool tells the calling agent "YOU (Claude) are the classifier" and accepts summary/entities/properties as inputs ([src/cortex/transport/mcp/server.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/transport/mcp/server.py)). That reduces provider dependency for MCP use, but it also moves semantic quality into the host agent without adding a verification layer.

The graph store is more operationally complex than the review surface suggests. The code includes PID marker files, stale lock recovery, command-line matching to defend against PID reuse, and direct-mode escape hatches ([src/cortex/db/graph_store.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/db/graph_store.py), [src/cortex/cli/main.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/cli/main.py)). That is a real cost of moving from file-first memory to a local graph service.

The "advanced reasoning" layer is mostly deterministic structural analysis at this commit. It detects stale dependencies, repeated entity patterns, project/entity gaps, and structural contradictions; semantic contradiction detection is described in comments but not implemented in `detect_contradictions()` beyond structural checks ([src/cortex/pipeline/advanced_reason.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/pipeline/advanced_reason.py)).

Obsidian import is a one-way ingestion path into Cortex's database model, not an Obsidian-compatible storage substrate. Once imported, notes are governed by Cortex rows/triples rather than by editable Markdown files ([src/cortex/pipeline/importer.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/pipeline/importer.py)).

## What to Watch

- Whether `detect_miss()` and persisted retrieval weights become wired into actual feedback-driven reranking; that would make Cortex's trace-derived loop more than access-tier promotion.
- Whether `reflex` tier changes retrieval weighting, briefing priority, or prompt injection beyond being stored and displayed; that determines whether the tier is activation policy or only metadata.
- Whether semantic contradiction detection becomes implemented rather than comment-level; that would strengthen Cortex's claim to graph intelligence.
- Whether MCP capture gains source/proof fields or review states for agent-supplied classifications; without that, classification lineage remains weak.
- Whether non-localhost MCP deployments keep enough admin-tool separation and authentication for multi-agent or shared-machine use.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - classifies: Cortex turns query/read/feedback traces into tier and audit state rather than into prose lessons or model weights.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Cortex separates database rows, graph triples, ontology rules, embeddings, query logs, access counters, and tool surfaces by substrate, form, lineage, and authority.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Cortex stores and ranks memory, but retained memory is still pulled through tools rather than pushed before every action.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: captured objects, query logs, and dossiers advise future work when read back.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: ontology, SPARQL rules, retrieval indexes, tiers, MCP schemas, and service boundaries carry behavioral authority.
