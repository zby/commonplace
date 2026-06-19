---
description: "Cortex review: local RDF/SQLite cognitive knowledge service with ontology, hybrid retrieval, MCP tools, reasoning, and access-derived tier learning"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# Cortex

Cortex, by Abbacus Group's `abbacusgroup/cortex` repository, is a local Python knowledge system for AI agents. It stores typed knowledge objects in an Oxigraph RDF graph and a SQLite content database, runs classify/link/enrich/reason stages over captured objects, serves retrieval and graph views through CLI, MCP, REST, and dashboard clients, and uses query/read/feedback traces to update access state and memory tiers. At the reviewed commit, Cortex is best understood as a local graph-backed intelligence service rather than a file-vault memory layer: retained knowledge is database state, and the main agent-facing interface is MCP tool calls.

**Repository:** https://github.com/abbacusgroup/cortex

**Reviewed commit:** [a51c2209eb6d26812c19c97aaade3cb64ccfc23c](https://github.com/abbacusgroup/cortex/commit/a51c2209eb6d26812c19c97aaade3cb64ccfc23c)

**Last checked:** 2026-06-04

## Core Ideas

**A dual store separates graph semantics from content retrieval.** The root README describes Cortex as Oxigraph plus SQLite, and the implementation makes that split concrete: `Store.create()` writes a new object to the RDF graph first, then to SQLite, rolling the graph write back if the SQLite insert fails ([README.md](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/README.md), [src/cortex/db/store.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/db/store.py)). SQLite is content-authoritative for document rows, raw markdown, FTS5, embeddings, config, and query logs; Oxigraph owns RDF object/entity/relationship structure and SPARQL reasoning ([src/cortex/db/content_store.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/db/content_store.py), [src/cortex/db/graph_store.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/db/graph_store.py)).

**The ontology is an executable system contract.** `ontology/cortex.ttl` defines knowledge-object classes, entity classes, relationship properties, provenance fields, temporal fields, tiers, and pipeline-stage fields. The reason stage applies authored SPARQL `CONSTRUCT` rules for symmetric `contradicts`, inverse `causedBy`/`ledTo`, and transitive `supersedes`, then writes inferred triples back to the graph ([ontology/cortex.ttl](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/ontology/cortex.ttl), [src/cortex/pipeline/reason.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/pipeline/reason.py)). That gives Cortex more symbolic authority than a vector-memory SDK: relationship labels are not just search metadata.

**Capture runs through a resilient intelligence pipeline.** `PipelineOrchestrator.capture()` ingests the object, optionally applies a template, then runs normalization, linking, enrichment, and reasoning stages; `run_pipeline()` records individual stage failures without aborting later stages ([src/cortex/pipeline/orchestrator.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/pipeline/orchestrator.py)). Normalization can ask the configured LLM for type, summary, tags, project, entities, confidence, and type-specific properties, but it also preserves caller-provided classification and degrades when embeddings or the LLM are unavailable ([src/cortex/pipeline/normalize.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/pipeline/normalize.py), [src/cortex/services/llm.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/services/llm.py)).

**Context efficiency is presenter-shaped pull retrieval.** Hybrid search combines SQLite FTS/BM25, optional embedding similarity, graph connectivity, and recency, then returns bounded results with score breakdowns ([src/cortex/retrieval/engine.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/retrieval/engine.py)). `cortex_context` renders those results through `BriefingPresenter`, returning ids, titles, types, tags, projects, summaries, tiers, and scores; `cortex_read` returns full document detail; dossier, synthesis, graph, and alert presenters shape larger views for specific use cases ([src/cortex/retrieval/presenters.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/retrieval/presenters.py), [src/cortex/transport/mcp/server.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/transport/mcp/server.py)). Volume is bounded by `limit` and presenter choice. Complexity is less bounded: dossiers and graph views can traverse entities, contradictions, timelines, and related entities without a progressive source-reading ladder.

**MCP is the canonical agent integration surface.** The MCP server constructs the store, pipeline, retrieval engine, graph queries, and learning loop, then exposes public tools for search, context, dossier, read, capture, link, feedback, graph, list, classify, and pipeline; localhost/admin mode adds status, synthesis, delete/update, reason, query trail, graph data, safety check, export, debug, and import tools ([src/cortex/transport/mcp/server.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/transport/mcp/server.py), [llms.txt](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/llms.txt)). The CLI routes ordinary commands through the running MCP HTTP server by default, while REST and dashboard surfaces are thin clients of that server so one process owns the graph database lock ([src/cortex/cli/main.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/cli/main.py), [src/cortex/transport/api/server.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/transport/api/server.py), [src/cortex/dashboard/server.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/dashboard/server.py)).

**Learning is narrow but durable.** `RetrievalEngine.search()` logs every hybrid search and result id list. `cortex_read`, direct CLI `read`, and positive `cortex_feedback` call `LearningLoop.record_access()`, which persists per-object access counts and last-access timestamps in SQLite config; after ten accesses it promotes the object to `reflex` tier ([src/cortex/retrieval/engine.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/retrieval/engine.py), [src/cortex/retrieval/learner.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/retrieval/learner.py), [src/cortex/transport/mcp/server.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/transport/mcp/server.py), [src/cortex/cli/main.py](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/cli/main.py)). Miss detection and ranking-weight persistence exist as library methods, but I did not find a deployed loop that converts miss signals into automatic weight updates.

## Artifact analysis

- **Storage substrate:** `graph` — Behavior-shaping state lives primarily in Oxigraph `graph.db` plus SQLite `cortex.db`; authored ontology, service files, setup config, dashboard templates, and MCP/CLI code are file-backed; the running MCP HTTP server is a service object that owns graph access for other clients.
- **Representational form:** `prose` `symbolic` `parametric` — Captured content, summaries, dossiers, syntheses, and tool descriptions are prose; RDF/OWL classes, SPARQL rules, SQLite schemas, FTS tables, tool schemas, tiers, query logs, config keys, and service boundaries are symbolic; embeddings are retained parametric vectors when the embedding provider is installed.
- **Lineage:** `authored` `imported` `trace-extracted` — Ontology, tool surfaces, templates, and setup code are authored; knowledge can be imported from Cortex v1 or Obsidian; query logs, access counters, last-access timestamps, tier changes, embeddings, inferred triples, and pipeline metadata are derived from captures or use traces.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Stored objects and presentations advise future work; MCP tool descriptions and `llms.txt` instruct agents; local/admin tool gating and graph locks enforce operational boundaries; ontology, tool schemas, pipeline stages, graph links, and indexes route access; validators and allowed vocabularies check structure; hybrid weights, tiers, graph boosts, and recency rank results; query/read/feedback traces update later tier state.

**Knowledge objects.** Storage substrate is dual-written Oxigraph triples plus SQLite `documents` rows carrying title, content, raw markdown, type, project, tags, summary, tier, pipeline stage, confidence, provenance, and timestamps. Representational form is prose content plus symbolic metadata. Lineage is authored through CLI/MCP/REST/dashboard capture, imported from V1/Obsidian, or enriched by template, caller-supplied, LLM-derived, and deterministic pipeline output. Behavioral authority is knowledge when searched/read as evidence or context, and system-definition authority when type, tier, confidence, relationships, and pipeline stage affect ranking, reasoning, alerts, or classification.

**Ontology, relationship graph, entities, and inferred triples.** Storage substrate is authored TTL plus Oxigraph graph persistence. Representational form is symbolic RDF/OWL/SPARQL. Lineage is authored ontology, captured or pipeline-derived object/entity triples, LLM-suggested relationships, and SPARQL-inferred triples. Behavioral authority covers routing, validation, ranking, and reasoning: relationship labels drive graph navigation, contradiction views, staleness checks, dossier assembly, and inference.

**SQLite FTS, embeddings, config, and query logs.** Storage substrate is SQLite tables and virtual tables. Representational form is symbolic rows/indexes/config plus parametric embedding blobs. Lineage is derived from document title/content/tags, optional embedding generation, query execution, and feedback/access events. Behavioral authority is ranking and learning: indexes and weights select what appears first, query logs give audit evidence, and access counters promote frequently read objects.

**Pipeline outputs and presenters.** Storage substrate is updated database rows/triples plus runtime presenter result objects. Representational form is prose summaries/narratives and symbolic result shapes, scores, relationship lists, entity neighborhoods, alerts, and source ids. Lineage is compiled from captured objects, relationship graph, optional LLM calls, and reasoning rules. Behavioral authority is knowledge presentation and routing: the same store can be served as a brief, full document, dossier, synthesis, graph, or alert set.

**MCP/CLI/REST/dashboard/service artifacts.** Storage substrate is package code, generated user config under `~/.cortex`, launchd/systemd service files, logs, and runtime server state. Representational form is symbolic API/tool/route/service definitions plus prose tool descriptions and setup prompts. Lineage is project-authored and setup-generated. Behavioral authority is instruction, routing, and enforcement because these surfaces decide which client can call capture/search/delete/reason/import tools and whether admin tools are exposed only on trusted local transports.

Promotion path: raw captured content can become normalized, linked, enriched, reasoned, embedded, and presented; repeated reads or positive feedback can promote an object to `reflex`; manual classify/link/pipeline/admin calls can strengthen metadata and graph structure. What Cortex does not provide at this commit is a review-grade promotion boundary from "frequently accessed" to "trusted instruction." Access-derived `reflex` status is salience/lifecycle metadata, not epistemic validation.

## Comparison with Our System

| Dimension | Cortex | Commonplace |
|---|---|---|
| Primary purpose | Local cognitive knowledge service for agents, with graph reasoning and MCP serving | Git-native methodology KB with typed artifacts, validation, review, and generated indexes |
| Main substrate | Oxigraph RDF graph plus SQLite content, FTS, embeddings, config, and logs | Git-tracked Markdown notes, instructions, ADRs, reviews, source snapshots, schemas, and indexes |
| Retrieval | Hybrid BM25 + embeddings + graph + recency, exposed through MCP/CLI/API | `rg`, curated indexes, descriptions, links, skills, validation/review workflows |
| Context strategy | Top-k search, summary briefing, full read, dossier/synthesis/presenter modes | Collection routing, progressive lexical search, authored links, generated indexes, review reports |
| Governance | Ontology, relationship vocabulary, local admin-tool gating, diagnostics, backup/restore | Collection contracts, type specs, schemas, deterministic validation, semantic review, archive lifecycle |
| Learning loop | Query/read/feedback traces update access state and tiers | Mostly explicit authoring/review/promotion; traces are captured only when operators decide to retain them |

Cortex and Commonplace both reject "just a vector store" memory. Cortex makes that rejection database-native: OWL classes, RDF relationships, SPARQL inference, FTS, embeddings, query logs, and MCP tool schemas are first-class state. Commonplace makes the same move in a repo-native direction: Markdown artifacts, schemas, collection contracts, generated indexes, and review workflows remain inspectable in git.

The strongest divergence is trust. Cortex can classify, link, infer, and retrieve more automatically, but much of that authority comes from LLM outputs, repeated access, and database-side state. Commonplace makes fewer automatic inferences but keeps source lineage, review status, replacement history, and validation failures more visible. For an agent-memory system, Cortex is stronger at live service integration and graph intelligence; Commonplace is stronger at source-readable governance and artifact lifecycle.

### Borrowable Ideas

**Make controlled relationships executable where they already have semantics.** Cortex's OWL/RDF layer is heavier than Commonplace needs for ordinary prose notes, but the SPARQL-rule pattern is worth borrowing selectively. If a Commonplace link label declares inverse, symmetric, or transitive semantics, high-value labels could be checked or materialized by validation. Ready only for labels where automation would prevent real review mistakes.

**Expose brief/context/read/dossier as named read surfaces.** Commonplace already has search snippets, descriptions, indexes, and full files, but Cortex's presenter names make the intended context budget easy for an agent to choose. A future Commonplace command could expose `brief`, `read`, and `dossier` modes over notes without changing the Markdown substrate. Needs a concrete agent-facing CLI use case.

**Centralize multi-client writes behind one local owner process when storage demands it.** Cortex's MCP HTTP server owns the graph store so CLI, REST, and dashboard clients do not fight over the database lock. Commonplace's git/file substrate does not need a daemon for normal writing, but a future local index or review service could borrow the single-owner/thin-client shape once there is an actual storage bottleneck.

**Treat query logs as maintenance signals, not truth.** Cortex's query logs and access counters are useful for finding what agents actually consult. Commonplace could record repeated failed searches or repeated note reads as coverage-pressure reports, but durable promotion should remain behind review.

**Do not borrow access-count trust.** Cortex's `reflex` promotion is operationally sensible as salience, but Commonplace should not treat repeated reads as evidence that a note is correct or instruction-worthy. Usage can prioritize review; it should not replace review.

## Write side

**Write agency:** `manual` `automatic` — Humans and agents can write by CLI, MCP, REST/dashboard, import, classify, link, update, delete, pipeline, and admin tools; automatic writes include FTS trigger upkeep, normalization updates, embeddings, entity mentions, relationship discovery, enrichment/tier updates, SPARQL inference, query logging, access counters, last-access timestamps, and access-derived tier changes.

**Curation operations:** `evolve` `synthesize` `invalidate` `decay` `promote` — The pipeline evolves existing object metadata, summaries, tags, entities, relationships, tier, and pipeline stage; synthesis presenters generate cross-document narrative views and captured `synthesis` objects can be retained; `supersedes`/contradiction/staleness reasoning can mark or surface invalidation pressure without deleting history; recency and tier adjustment down-weight or demote older/reflex memories; repeated access and explicit feedback promote objects to `reflex`.

### Trace-derived learning

**Trace source:** `tool-traces` `event-streams` — Cortex consumes search calls, read calls, and explicit relevance feedback events; it does not consume full chat transcripts or action trajectories in the reviewed implementation.

**Learning scope:** `per-project` `cross-task` — The loop is local to a Cortex data directory and can be filtered by project metadata, while query logs and access-derived tiers can affect later searches across tasks in that store.

**Learning timing:** `online` — Query logging, read access counting, feedback recording, and threshold promotion happen during normal CLI/MCP/dashboard use; demotion through `adjust_tiers()` requires an explicit call path.

**Distilled form:** `symbolic` — Trace-derived state is retained as query-log rows, config counters, timestamps, and tier values rather than prose lessons, tool rules, model weights, or adapters.

The qualifying raw traces are small and tool-level: query text with parameters and result ids, full-object reads, and positive feedback on object usefulness. Extraction is deterministic. Search writes a `query_log` row; read and feedback increment `access_count:{obj_id}`, update `last_access:{obj_id}`, and promote after ten accesses. `detect_miss()` recognizes a "searched, then read something outside the results" signal, and `update_weights()` can persist ranking weights, but I did not find code that automatically connects those methods into live reranking.

Cortex fits the survey branch where traces alter ranking/lifecycle state rather than producing prose lessons or executable procedures. It usefully separates raw trace knowledge from distilled behavior-shaping state: query logs are mostly audit knowledge, while access-derived tier changes carry ranking and lifecycle authority.

## Read-back

**Read-back:** `pull` — Retained Cortex memory reaches an agent, CLI user, dashboard, or REST client when that consumer explicitly calls `cortex_search`, `cortex_context`, `cortex_dossier`, `cortex_read`, `cortex_graph`, `cortex_list`, `cortex_synthesize`, status/alert, query-trail, or graph-data tools. I found no code path that injects accumulated Cortex memories into every future model call without a lookup.

There is no push signal to classify for accumulated memory at this commit. Static MCP tool descriptions and `llms.txt` best practices are baseline instructions, not retained memory read-back; alert presenters and status responses can surface contradictions, patterns, and staleness, but only when a caller requests them. Because there is no push read-back path, push faithfulness testing is not applicable.

Selection is hybrid and bounded on the pull path. Search uses keyword, optional embedding, graph, and recency signals with a `limit`; briefing mode narrows returned fields for token efficiency; read mode returns the full object; dossier and graph modes expand through entities and relationships. Effective retrieval precision, context dilution, and whether agents faithfully act on returned memories are not verified from static code.

Authority at consumption depends on the tool result and host prompt. A retrieved object or dossier is advisory knowledge unless the receiving agent treats it as instruction. The ontology, pipeline state, tiers, and retrieval scores influence which knowledge is presented first, but Cortex itself does not hard-gate downstream agent actions based on the returned memory.

## Curiosity Pass

**`reflex` is a Cortex tier, not automatic prompt injection.** The name suggests active memory, but at this commit a reflex object is more privileged inside Cortex's store and retrieval/lifecycle metadata; it is still served through pull tools.

**MCP capture deliberately shifts classification work to the caller.** `cortex_capture` tells the MCP caller that "YOU (Claude) are the classifier" and accepts summary, entities, and type-specific properties directly, while direct pipeline normalization can use Cortex's configured LLM. That reduces provider dependency for MCP use, but it also moves semantic quality into the host agent without adding a verification layer.

**The graph service has real operational cost.** The graph store includes PID marker files, stale lock recovery, process-command matching to defend against PID reuse, and `--direct` escape hatches. Those details are the price of moving from file-first memory to a single-owner local graph service.

**Advanced reasoning is mostly structural.** The module advertises semantic contradictions, but `detect_contradictions()` currently delegates to structural contradiction checks. Pattern and gap detection are useful, but they are deterministic graph/database heuristics rather than verified semantic judgment.

**Obsidian import is ingestion, not an Obsidian-compatible substrate.** Imported vault notes become Cortex database objects and graph triples. After import, the source of truth is Cortex state, not editable Markdown files.

## What to Watch

- Whether `detect_miss()` and persisted retrieval weights become wired into actual feedback-driven reranking; that would make the trace-derived loop more than access-tier promotion.
- Whether `reflex` starts affecting prompt assembly or automatic memory injection; that would change the read-back verdict from pull-only to push or both.
- Whether semantic contradiction detection becomes implemented rather than comment-level; that would strengthen Cortex's graph-intelligence claim.
- Whether MCP capture gains source/proof fields or review states for agent-supplied classifications; without that, classification lineage remains weak.
- Whether non-localhost MCP deployments keep enough authentication and admin-tool separation for multi-agent or shared-machine use.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Cortex stores and ranks memory, but accumulated memory is still pulled through tools rather than pushed before every action.
- [Use trace-derived extraction as meta-learning](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - compares: Cortex derives symbolic tier and audit state from tool traces, not prose lessons from conversations.
- [Trace-derived learning techniques in related systems](../../trace-derived-learning-techniques-in-related-systems.md) - places: Cortex belongs in the trace-to-ranking/lifecycle branch.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: database rows, graph triples, ontology rules, embeddings, logs, counters, and tool surfaces carry different forms and authorities.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: captured objects, query logs, dossiers, syntheses, and alerts advise future work when read.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: ontology, SPARQL rules, retrieval indexes, tiers, MCP schemas, and service boundaries shape or validate behavior.
