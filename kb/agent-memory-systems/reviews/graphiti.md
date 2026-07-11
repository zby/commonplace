---
description: "Graphiti review: temporal graph memory with episode provenance, LLM extraction, fact invalidation, hybrid retrieval, MCP tools, and pull-only activation"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
last-checked: "2026-06-04"
---

# Graphiti

Graphiti, by Zep Software, is an open-source temporal context graph engine for AI agent memory. At the reviewed commit it stores raw episodes, extracts entity nodes and factual edges with LLMs, tracks fact validity windows and provenance, resolves duplicates and contradictions, searches across graph/vector/full-text signals, and exposes SDK, FastAPI service, and MCP server surfaces for adding and querying memory.

**Repository:** https://github.com/getzep/graphiti

**Reviewed commit:** [34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6](https://github.com/getzep/graphiti/commit/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6)

**Last checked:** 2026-06-04

## Core Ideas

**The retained memory unit is a temporal graph, not a flat transcript.** Episodes persist raw text, JSON, or message content with `source_description`, `valid_at`, and extracted edge ids; entity nodes carry names, labels, summaries, attributes, and name embeddings; factual edges carry relation names, fact text, episode provenance, embeddings, and `valid_at`/`invalid_at` windows ([graphiti_core/nodes.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/nodes.py), [graphiti_core/edges.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/edges.py)).

**Ingestion is an LLM extraction and resolution pipeline.** `add_episode()` retrieves recent episodes for context, creates or loads the episodic node, extracts nodes, resolves them against existing graph candidates, extracts factual edges, resolves duplicates and contradictions, extracts node attributes/summaries, saves graph state, and optionally updates communities ([graphiti_core/graphiti.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/graphiti.py), [graphiti_core/utils/maintenance/node_operations.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/utils/maintenance/node_operations.py), [graphiti_core/utils/maintenance/edge_operations.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/utils/maintenance/edge_operations.py)).

**Contradictions are retained as temporal invalidation, not simple overwrite.** Edge resolution asks the LLM to identify duplicate and contradicted facts, then `resolve_edge_contradictions()` sets `invalid_at` and `expired_at` on older facts when the new fact supersedes them in time. The old edge remains part of the graph's history ([graphiti_core/utils/maintenance/edge_operations.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/utils/maintenance/edge_operations.py)).

**Context efficiency is retrieval-first and graph-scoped.** Search embeds the query only when needed, searches configured scopes in parallel, overfetches candidates at `2 * limit`, then reranks and truncates to the configured limit. The default advanced recipe combines edge/node/community BM25, embedding similarity, graph BFS, and cross-encoder reranking; the simpler `search()` returns edge facts only ([graphiti_core/search/search.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/search/search.py), [graphiti_core/search/search_config.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/search/search_config.py), [graphiti_core/search/search_config_recipes.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/search/search_config_recipes.py)). Complexity can still be high because returned context may include fact edges, entity summaries, episodes, communities, graph-neighborhood expansion, and temporal filters.

**The MCP server turns the library into an agent memory tool surface.** It exposes `add_memory`, `search_nodes`, `search_memory_facts`, `get_entity_edge`, `get_episodes`, delete tools, `clear_graph`, and `get_status`, with a persistent configured graph and per-`group_id` queues for sequential episode ingestion ([mcp_server/src/graphiti_mcp_server.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/mcp_server/src/graphiti_mcp_server.py), [mcp_server/src/services/queue_service.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/mcp_server/src/services/queue_service.py)). The MCP instructions tell clients to search and write memory, but the server does not itself inject memory into a model prompt.

**Adoption affordances are strong for service builders, weaker for file-native governance.** Graphiti supports Neo4j, FalkorDB, Kuzu, and Neptune-style graph backends, configurable LLM/embedder/reranker clients, Pydantic ontology types, OpenTelemetry spans, FastAPI endpoints, and Dockerized MCP deployment ([graphiti_core/graphiti.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/graphiti.py), [mcp_server/README.md](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/mcp_server/README.md), [server/graph_service](https://github.com/getzep/graphiti/tree/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/server/graph_service)). The tradeoff is that semantic state lives in databases and generated properties, not in git-diffable authored artifacts.

## Artifact analysis

- **Storage substrate:** `graph` — The primary behavior-shaping retained state persists as graph nodes and relationships in a configured graph driver; embeddings, full-text indexes, service queues, and API objects support access, but the durable memory object is the temporal context graph.
- **Representational form:** `prose` `symbolic` `parametric` — Episode bodies, fact text, entity/community/saga summaries, and source descriptions are prose; nodes, edges, labels, group ids, timestamps, entity/edge type schemas, filters, and tool schemas are symbolic; name/fact embeddings, vector similarity, cross-encoder scores, and graph-distance rerankers provide parametric or learned ranking signals.
- **Lineage:** `imported` `trace-extracted` — Text/JSON/message episodes are imported source material; message episodes and server `/messages` payloads can be conversation traces; entity nodes, edges, summaries, timestamps, duplicate resolutions, contradiction decisions, and communities are derived views extracted from those episodes and existing graph context.
- **Behavioral authority:** `knowledge` `routing` `validation` `ranking` `learning` — Retrieved facts/nodes/episodes advise as knowledge; group ids, graph partitions, filters, labels, schemas, queues, MCP tools, and API routes direct access; Pydantic models, label validation, group validation, config factories, and driver constraints validate; BM25, embeddings, BFS, MMR, RRF, node-distance, episode-mention, and cross-encoder paths rank; ingestion and maintenance update retained graph state.

**Episodes.** Storage substrate: graph `Episodic` nodes. Representational form: prose or serialized JSON content plus symbolic source, source description, group id, entity-edge list, and valid time. Lineage: imported user/application data or trace-extracted conversation messages. Behavioral authority: source evidence and provenance for later extracted nodes and facts.

**Entity nodes and factual edges.** Storage substrate: graph `Entity` nodes and `RELATES_TO` edges, with Kuzu using intermediate relation nodes. Representational form: symbolic graph topology plus prose summaries/facts and embeddings. Lineage: LLM-extracted from episodes, deduplicated against candidate graph state, and linked back to episodes. Behavioral authority: knowledge when returned, ranking when indexed, and learning input when later episodes update summaries or invalidate facts.

**Temporal validity and provenance fields.** Storage substrate: symbolic properties on edges and episodes. Representational form: timestamps, episode uuid lists, `reference_time`, `valid_at`, `invalid_at`, and `expired_at`. Lineage: derived from episode timestamps and LLM timestamp extraction. Behavioral authority: routing and validation for temporal queries; invalidation also carries truth-maintenance authority over old facts.

**Search configurations and indexes.** Storage substrate: graph/full-text/vector indexes and runtime `SearchConfig` recipes. Representational form: symbolic search-method/reranker configs and parametric embeddings/scores. Lineage: authored config plus derived embeddings and indexes. Behavioral authority: ranking and routing for what reaches the caller's context.

**MCP/server tools.** Storage substrate: repository code and runtime service objects. Representational form: symbolic tool/API schemas plus prose instructions. Lineage: authored integration surface. Behavioral authority: routing for agent and application access; the MCP server affords read/write memory operations but does not enforce that a host agent uses search before acting.

Promotion path: Graphiti can move raw episode material into extracted nodes and facts, attach embeddings and validity windows, reuse or invalidate existing facts, and optionally consolidate graph regions into community summaries. This strengthens durability and retrieval authority, but there is no retained proposal/review artifact for the extraction or invalidation judgment.

## Comparison with Our System

| Dimension | Graphiti | Commonplace |
|---|---|---|
| Primary purpose | Runtime temporal context graph for applications and agents | Git-native methodology KB for agents and maintainers |
| Canonical artifact | Episode, entity node, fact edge, summary, index, or MCP tool | Typed Markdown artifact with frontmatter, citations, links, and validation |
| Source of truth | Graph database plus derived embeddings/full-text indexes | Repository files plus generated indexes and reports |
| Write path | Episode ingestion, LLM extraction, dedupe, invalidation, summary/community maintenance | Authored edits, snapshots, validation, semantic review, index refresh |
| Read-back | Pull SDK/API/MCP search and retrieval tools | Mostly pull through `rg`, indexes, links, skills, and loaded instructions |
| Governance | Driver constraints, Pydantic validation, group scoping, timestamps, tests | Collection contracts, type specs, git diffs, citations, semantic gates |

Graphiti is stronger where applications need low-friction runtime memory over changing facts. It keeps raw episodes, extracted facts, temporal validity, and hybrid search in one operational substrate. Commonplace is stronger where the memory is methodology or design knowledge that should be reviewable: the durable unit has explicit authorship, citations, file history, and schema/review gates.

The main tradeoff is hidden epistemic authority. Graphiti's LLM extraction and contradiction resolution can change what the graph treats as current without leaving a human-readable change proposal. Commonplace would normally force that kind of change through a visible note edit or review gate.

### Borrowable Ideas

**Make invalidation a first-class relation to time.** Ready as vocabulary. Commonplace already has statuses and replacements, but Graphiti's explicit `valid_at`/`invalid_at` distinction is useful for claims whose truth changes rather than merely becoming stale.

**Keep raw source episodes linked to derived facts.** Ready now. Review artifacts already cite sources; a stronger derived-claim workflow could preserve the exact source bundle that produced each generated note or index entry.

**Use group ids as operational scopes.** Ready for tooling language. Graphiti's `group_id` maps cleanly to project/workshop/scoped-memory partitions, especially for temporary work that should not leak into a global context.

**Borrow hybrid retrieval only after preserving provenance.** Needs a concrete serving surface. Graphiti's BM25 + embedding + graph traversal recipe is attractive, but Commonplace should expose source paths, quote anchors, and artifact types with every served result.

**Do not borrow silent contradiction resolution for durable notes.** Ready as a constraint. Graphiti's invalidation is useful in a graph memory layer; methodology claims need a retained rationale, reviewer-visible diff, and validation before replacement.

## Write side

**Write agency:** `manual` `automatic` — Manual writes come from SDK/API/MCP calls such as `add_episode`, `add_episode_bulk`, `add_triplet`, `add_memory`, entity-node save endpoints, and delete/clear tools; automatic writes include LLM extraction, node/edge deduplication, edge contradiction invalidation, timestamp extraction, attribute/summary updates, embedding/index updates, saga episode links, sequential MCP queue processing, and optional community construction.

**Curation operations:** `consolidate` `dedup` `evolve` `invalidate` — Community and saga summaries consolidate stored graph material into shorter derived surfaces; node and edge resolution deduplicate extracted entities/facts against existing graph state; node summaries, attributes, embeddings, episode links, saga watermarks, and community summaries evolve existing entries; contradiction resolution invalidates older facts by setting `invalid_at` and `expired_at` while retaining history.

### Trace-derived learning

**Trace source:** `session-logs` `event-streams` — `EpisodeType.message`, FastAPI `/messages`, and MCP `add_memory` can ingest conversation-style messages and interaction-derived memory events; Graphiti also ingests text/JSON application events, but it does not capture tool traces automatically in the reviewed code.

**Learning scope:** `per-project` `cross-task` — `group_id` partitions the graph into domains; a persisted episode-derived graph can affect later searches across tasks in the same group, and host applications can use one group as a user/project memory scope.

**Learning timing:** `online` `staged` — MCP writes are queued and processed asynchronously per group; SDK/API ingestion can run during application operation or as a background task; community building and index/constraint setup are explicit staged operations.

**Distilled form:** `prose` `symbolic` `parametric` — Message and event traces become prose facts/summaries, symbolic nodes/edges/timestamps/provenance links, and parametric embeddings or reranker scores.

**Extraction.** The raw trace is an episode body with source metadata and reference time. The extraction oracle is primarily the configured LLM client, constrained by Pydantic response models and optional custom entity/edge types; dedupe and contradiction decisions also use LLM calls after candidate retrieval.

**Scope and timing.** The durable scope is `group_id`; episode sequences can also be linked into sagas. The write that affects future action is not the raw message alone, but the derived graph state saved after extraction, resolution, embedding, and optional invalidation.

**Survey fit.** Graphiti fits the trace-to-temporal-graph family: transcripts or interaction events become graph facts with provenance and validity windows. It strengthens the survey's point that trace-derived memory can be symbolic and temporal, not only vector/prose recall.

## Read-back

**Read-back:** `pull` — The implemented repo serves memory through SDK `search`/`search_`/`retrieve_episodes`, FastAPI `/search` and `/get-memory`, and MCP `search_nodes`/`search_memory_facts`/`get_episodes` tools, all of which require a caller or host agent to request memory; I did not find a repository-wired hook that automatically injects retained Graphiti memory into a model prompt before invocation.

MCP documentation and cursor rules can instruct a host assistant to search first and capture preferences, but that is host policy riding on pull tools, not an implemented push path in Graphiti itself ([mcp_server/docs/cursor_rules.md](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/mcp_server/docs/cursor_rules.md), [mcp_server/src/graphiti_mcp_server.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/mcp_server/src/graphiti_mcp_server.py)).

Selection is still strongly engineered for read-back once called. Pull search can filter by group ids, node labels, edge types, edge uuids, temporal fields, creation/expiration fields, and arbitrary properties; it can combine full-text, embedding, BFS expansion, cross-encoder reranking, RRF/MMR, node-distance reranking, and episode-mention ranking ([graphiti_core/search/search_filters.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/search/search_filters.py), [graphiti_core/search/search.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/search/search.py)).

The consumption authority is advisory unless the host application upgrades it. SDK/API/MCP results are facts, nodes, episodes, or summaries returned to the caller; they become instruction-like only if a host agent places them in a prompt or treats them as policy. Effective faithfulness is not verified from code: I found search and integration plumbing, but not with/without ablation tests showing that retrieved memory changes downstream model behavior correctly.

## Curiosity Pass

**The README's "continuous" framing depends on callers.** Graphiti can incrementally update a graph whenever episodes arrive, but the repository does not automatically observe all user/agent interactions. A host must submit those episodes.

**Fact invalidation is more concrete than most memory systems.** The code has a real `invalid_at`/`expired_at` mutation path rather than simply overwriting memories, which makes history queryable if callers preserve the relevant timestamps.

**The graph can be both source record and generated model output.** Episodes preserve imported material, while entities, facts, timestamps, and contradiction judgments are LLM-derived. Treating all graph state as equally authoritative would blur that lineage.

**MCP instructions are not activation.** The MCP server tells clients how to use memory, but the actual read-back remains tool invocation. This is a useful boundary case for systems that market as agent memory.

**Community summaries are optional and lossy.** They can reduce graph complexity, but they are generated from existing summaries and graph clusters, so they need provenance and review before carrying high authority.

## What to Watch

- Whether Graphiti or the MCP server adds pre-prompt hooks for Claude/Cursor/LangGraph; that would change the read-back verdict from pull-only to both.
- Whether contradiction resolution starts retaining rationale artifacts; that would make temporal invalidation more reviewable and more applicable to Commonplace.
- Whether `group_id` evolves into richer ACL/governance state; that would affect the authority of cross-user or cross-project memory boundaries.
- Whether community/saga summaries become a default read path; that would shift context efficiency toward hierarchical compaction rather than only top-k retrieval.
- Whether tool/action traces are ingested as first-class episodes; that would broaden the trace-derived classification beyond conversation/message memory.

## Related Systems

- [ReframeWeb](./ReframeWeb.md) - compares-with: both classify their storage substrate as `graph`, but ReframeWeb's "graph memory" is a shallow root→child tree a relational store would serve identically, while Graphiti actually exploits graph structure — BFS expansion, communities, multi-hop, hybrid BM25+embedding+traversal. Same substrate label, opposite answer to "does the graph earn its keep?"

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Graphiti extracts durable temporal graph facts from message/event episodes.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Graphiti stores rich memory, but activation is explicit SDK/API/MCP pull unless a host adds its own hook.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: episodes, graph facts, embeddings, summaries, search configs, and MCP tools differ by substrate, form, lineage, and authority.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: message traces can be distilled into durable graph nodes and facts for later recall.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: retrieved facts, entity summaries, episodes, and community summaries advise later actions.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: search configs, filters, schemas, queues, and MCP tool definitions route and constrain memory behavior.
