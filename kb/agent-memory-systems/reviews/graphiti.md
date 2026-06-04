---
description: "Graphiti review: temporal context graph engine with episode provenance, LLM fact extraction, hybrid retrieval, MCP/API pull surfaces"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-06-02"
---

# Graphiti

Graphiti, from getzep, is an open-source temporal context graph engine for AI-agent memory and evolving enterprise context. At the reviewed commit, the core system ingests episodes, extracts entity nodes and relationship facts with LLM prompts, resolves duplicates and contradictions, stores temporal/provenance-bearing graph artifacts, and exposes hybrid search through a Python library, a FastAPI graph service, and an MCP server.

**Repository:** https://github.com/getzep/graphiti

**Reviewed commit:** [34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6](https://github.com/getzep/graphiti/commit/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6)

**Last checked:** 2026-06-02

## Core Ideas

**Episodes are the provenance root.** The central write path is `Graphiti.add_episode()`: it accepts message, JSON, text, or fact-triple episodes; retrieves recent prior episodes for context; creates or reuses an `EpisodicNode`; extracts entity nodes and entity edges; saves episode, mention edges, entities, and facts; and optionally updates communities ([graphiti.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/graphiti.py), [nodes.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/nodes.py)). The episode node carries source type, source description, raw content unless disabled, `valid_at`, group id, and the edge ids derived from it.

**Facts are temporal relationship edges, not flat memories.** `EntityEdge` stores a relation name, natural-language fact, fact embedding, source episode ids, `valid_at`, `invalid_at`, `expired_at`, `reference_time`, and custom attributes ([edges.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/edges.py)). This makes the durable memory unit a graph fact with temporal bounds and provenance pointers, while entity nodes hold names, summaries, labels, attributes, and name embeddings.

**LLM prompts are the extraction and reconciliation policy.** Node extraction and edge extraction are prompt-driven, with Pydantic response schemas and defensive validation of entity labels, relation endpoints, timestamps, and custom attributes ([node operations](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/utils/maintenance/node_operations.py), [edge operations](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/utils/maintenance/edge_operations.py), [extract node prompts](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/prompts/extract_nodes.py), [extract edge prompts](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/prompts/extract_edges.py)). Edge resolution uses a separate dedupe prompt that returns duplicate and contradicted fact indexes, after which code applies timestamp-based invalidation rather than deleting old facts ([dedupe edge prompt](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/prompts/dedupe_edges.py)).

**Ontology is partly prescribed and partly learned.** Developers can pass Pydantic entity and edge type definitions plus an edge type map into `add_episode()`, while the default path extracts generic `Entity` nodes and derives relation names from text ([graphiti.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/graphiti.py), [extract edge prompts](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/prompts/extract_edges.py)). The resulting operative part is mixed: authored symbolic schemas constrain extraction, while prompt-mediated extraction can mint relation labels and summaries from episodes.

**Storage is graph-first with pluggable providers and embedded/full-text indexes.** The package defaults to Neo4j but includes driver providers for Neo4j, FalkorDB, Kuzu, and Neptune; the project dependencies and extras expose those backends plus optional OpenSearch support for Neptune ([driver.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/driver/driver.py), [pyproject.toml](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/pyproject.toml)). The graph stores episodes, entities, edges, communities, embeddings, temporal fields, and group partitions.

**Context efficiency happens at retrieval time, not by loading the graph.** The core read path is `search()` / `search_()`, which uses bounded `SearchConfig.limit`, group filters, date/property filters, semantic embeddings, BM25/full-text, graph BFS, node-distance reranking, reciprocal rank fusion, MMR, or cross-encoder reranking depending on the chosen recipe ([graphiti.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/graphiti.py), [search.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/search/search.py), [search config](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/search/search_config.py), [recipes](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/search/search_config_recipes.py), [filters](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/search/search_filters.py)). It constrains context volume by returning top-k graph objects, but the complexity of returned nodes, facts, communities, and episode provenance remains a host-assembly problem.

**Integration surfaces are library, service, and MCP pull tools.** The FastAPI service queues `/messages` ingestion and exposes `/search` and `/get-memory`; the MCP server exposes `add_memory`, `search_nodes`, and `search_memory_facts` tools with configuration-backed group scoping ([ingest router](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/server/graph_service/routers/ingest.py), [retrieve router](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/server/graph_service/routers/retrieve.py), [MCP server](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/mcp_server/src/graphiti_mcp_server.py)). The documented Cursor rules tell an agent to search before tasks, but that is an always-loaded instruction surface, not an implemented relevance-gated push mechanism ([cursor rules](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/mcp_server/docs/cursor_rules.md)).

## Artifact analysis

- **Storage substrate:** `graph` — Graph database nodes under provider-specific graph storage
- **Representational form:** `prose` `symbolic` `parametric` — prose episodes/facts/summaries, symbolic graph labels/metadata/timestamps/schemas, and embeddings/full-text indexes
- **Lineage:** `authored` `imported` `trace-extracted` — episodes can be supplied directly, imported from structured/text enterprise data, or derived from conversational/message traces before LLM extraction
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — graph objects advise as knowledge; prompts/schemas instruct and validate extraction; temporal filters enforce currentness; recipes route/rank retrieval; extraction learns graph state

**Episode nodes.** Storage substrate: graph database nodes under provider-specific graph storage. Representational form: mixed structured metadata plus prose or JSON content. Lineage: authored/imported trace records supplied through `add_episode()`, `/messages`, or the MCP `add_memory` tool; if `store_raw_episode_content` is disabled, the source content is intentionally dropped after extraction. Behavioral authority: knowledge artifacts as evidence and provenance; they shape behavior only when retrieved or used as extraction context.

**Entity nodes and summaries.** Storage substrate: graph database nodes with labels, attributes, summaries, and name embeddings. Representational form: mixed prose summaries, symbolic labels/attributes, and distributed-parametric embeddings. Lineage: LLM-extracted or deduplicated from episodes, optionally constrained by developer-provided entity type schemas. Behavioral authority: knowledge artifacts during read-back; schema labels and embeddings also have ranking/routing authority in search.

**Entity edges / facts.** Storage substrate: graph relationships or provider-specific relation nodes, with embeddings and temporal fields. Representational form: mixed natural-language facts, symbolic relation names, timestamps, source episode ids, custom attributes, and distributed-parametric fact embeddings. Lineage: LLM-extracted from episodes, resolved against existing candidate facts, and invalidated by later contradictory facts. Behavioral authority: knowledge artifacts when returned as context; the temporal fields and invalidation state become system-definition artifacts for filtering, ranking, and deciding which fact is current.

**Extraction prompts, schemas, and search recipes.** Storage substrate: repository Python modules and prompt functions. Representational form: prose prompts plus symbolic Pydantic schemas, enums, limits, filters, and recipes. Lineage: authored system-definition artifacts in the codebase; changes to prompt text, response models, search recipes, or driver queries regenerate different graph artifacts and retrieval sets. Behavioral authority: instruction, validation, routing, ranking, and write-policy authority over what gets retained and what later returns.

**MCP/API configuration and instruction docs.** Storage substrate: repository server code, config, and docs. Representational form: symbolic tool definitions plus prose usage instructions. Lineage: authored integration layer over the core graph engine. Behavioral authority: MCP tools expose pull access; docs such as Cursor rules have instruction-like force only when a host loads them.

There is a promotion path, but it is not a Commonplace-style review ladder. Raw episodes can become extracted facts; facts can be deduplicated, timestamped, invalidated, summarized into entity/community context, and retrieved through stronger ranking surfaces. They do not automatically become reviewed rules, validators, or authored procedures unless a host application adds that governance layer.

## Comparison with Our System

| Dimension | Graphiti | Commonplace |
|---|---|---|
| Primary purpose | Build and query temporal context graphs for agents and applications | Maintain a git-native methodology KB for agent operation |
| Canonical retained artifact | Episodes, entity nodes, relationship facts, summaries, communities | Typed Markdown notes, instructions, ADRs, reviews, source snapshots, indexes |
| Storage substrate | Graph database plus embeddings/full-text indexes | Repository files plus deterministic generated indexes and reports |
| Representational form | Mixed graph objects, prose facts/summaries, symbolic timestamps/types, embeddings | Mostly prose and frontmatter, with schemas, scripts, links, and validation |
| Lineage | Episode ids, source descriptions, temporal fields, and edge episode lists | Source citations, git history, replacement archives, type contracts, review gates |
| Activation | Host/API/MCP search over graph memory | `rg`, indexes, authored links, skills, instructions, validation/review commands |
| Authority | Extraction prompts, schemas, graph queries, rankings, and returned facts | Collection contracts, type specs, skills, instructions, validators, review gates |

Graphiti is stronger than Commonplace as an application memory substrate. It can ingest live interaction streams, preserve temporal history, invalidate older facts without deleting them, and query across embeddings, keywords, graph neighborhoods, and temporal filters. Commonplace is stronger as a governed knowledge library: artifacts are inspectable in git, typed by collection contracts, cited to sources, validated, reviewed, and intentionally promoted.

The most important divergence is source-of-truth shape. Graphiti turns traces into a queryable graph where the durable memory is extracted and stored as graph state. Commonplace keeps durable methodology in authored text and treats generated or derived artifacts as reviewable support. Graphiti's lineage is good for "which episode produced this fact?" but weaker for "which exact source span, model, prompt version, and reviewer accepted this behavioral rule?"

Graphiti's context model is also runtime-first. It assumes a host application will call search, choose a recipe, decide how many graph objects to load, and assemble them into prompt context. Commonplace uses pre-authored navigation and deterministic validation so agents can inspect and justify why a particular note, instruction, or review is loaded.

**Read-back:** `pull` — Graphiti's implemented memory reaches agents through explicit library/API/MCP search calls or host-written instructions to search; I did not find a code-grounded relevance-gated pre-action push path in the reviewed source

### Borrowable Ideas

**Represent facts as temporally bounded claims.** Ready to borrow conceptually. Commonplace notes and reviews already have status and dates, but Graphiti's `valid_at` / `invalid_at` split is useful for source claims whose truth changes over time. In Commonplace this should appear as authored or generated metadata only where the temporal boundary is actually meaningful.

**Keep raw episode provenance attached to derived facts.** Ready for trace-heavy workflows. Commonplace should preserve source snapshots and trace excerpts separately from distilled notes; Graphiti's edge-to-episode pointers are a compact version of that lineage.

**Use graph-distance or entity-neighborhood reranking as a search layer, not as canonical meaning.** Needs a concrete search use case. If Commonplace grows a graph or vector search layer, neighborhood reranking could help agents find adjacent notes, but authored links and collection contracts should remain the source of semantics.

**Make extraction policy inspectable.** Ready now. Graphiti's prompts and Pydantic schemas make the write policy visible. Commonplace should continue treating extraction prompts, classifiers, and validators as system-definition artifacts that deserve review.

**Do not borrow automatic fact extraction as automatic authority promotion.** Graphiti is persuasive as a memory graph, not as a governed KB learning loop. Extracted facts can advise future work; they should not become Commonplace instructions without source review and promotion.

## Trace-derived learning placement

**Trace source:** `session-logs` `event-streams` — conversational messages and other host-submitted episode streams feed durable graph extraction.

**Learning scope:** `cross-task` — graph partitions and `group_id` retain episode-derived facts for later host queries beyond a single immediate task.

**Learning timing:** `online` `staged` — add operations process episodes during ingestion, while service and MCP layers queue episode processing for ordered group writes.

**Distilled form:** `prose` `symbolic` `parametric` — extracted facts/summaries, temporal graph structure and schemas, and embeddings/full-text indexes are the durable distilled surfaces.

**Trace source.** Graphiti qualifies as trace-derived because the implemented ingestion path derives durable graph artifacts from episodes, including conversational messages submitted through the Python API, FastAPI `/messages`, or MCP `add_memory` tool ([graphiti.py](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/graphiti_core/graphiti.py), [ingest router](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/server/graph_service/routers/ingest.py), [MCP server](https://github.com/getzep/graphiti/blob/34f56e65e0fe2096132c8d16f3a1a4ac9300a5f6/mcp_server/src/graphiti_mcp_server.py)). The trace source is not limited to agent transcripts; it can also be structured JSON, text documents, enterprise data, or direct fact triples.

**Extraction.** Extraction is staged: recent episodes are retrieved as context; an LLM extracts entity nodes; another LLM prompt extracts fact triples with temporal fields and episode attribution; dedupe and contradiction prompts compare new facts to existing candidates; code assigns embeddings, updates summaries, saves provenance links, and invalidates superseded edges. Developer-provided entity and edge schemas can constrain the extraction surface.

**Four fields.** The raw stage is graph-stored episodes: mixed trace content and symbolic metadata, lineage from submitted messages/data, and knowledge-artifact authority as evidence. The distilled stage is entity nodes, facts, summaries, communities, embeddings, and invalidation metadata: graph/database substrate, mixed prose-symbolic-distributed representation, LLM-and-code-derived lineage from episodes, and advisory/ranking/filtering behavioral authority when read back.

**Scope and timing.** Scope is set mostly by `group_id`, database/graph partition, optional saga links, and host-provided filters. Timing is online or queued: add operations run per episode or batch, with the service and MCP layers explicitly queueing episode processing to avoid concurrent writes for the same group.

**Survey placement.** Graphiti belongs in the trace-to-temporal-knowledge-graph family. It strengthens the survey axis where raw interaction/data traces become durable knowledge artifacts with provenance and temporal invalidation. It does not, by itself, cross into trace-derived rules, tests, skills, or high-authority instructions.

## Curiosity Pass

**The graph is not the prompt.** Graphiti gives the host a rich retrieval substrate, but the host still decides which query to issue, which recipe to use, and how returned facts enter the model's context.

**Temporal invalidation is stronger than ordinary memory update/delete.** Instead of overwriting old facts, Graphiti can preserve the previous fact and mark when it stopped being valid. That is useful for agent memory, but it depends on extraction and contradiction prompts getting the temporal semantics right.

**The extraction prompts are very operational.** The code has many concrete prompt rules for excluding vague entities, preserving detail, validating endpoints, extracting timestamps, and rejecting duplicate facts. The reviewable policy is more in these prompts than in the graph database itself.

**Raw provenance can be intentionally weakened.** `store_raw_episode_content=False` clears episode content before saving. That may be useful for privacy or cost, but it changes the artifact from source evidence to provenance metadata plus derived facts.

**MCP docs sound more proactive than the implemented loop.** The Cursor rules say to always search first and save new information, but that is host instruction, not a built-in matcher that injects memories before action.

## What to Watch

- Whether Graphiti adds source spans, prompt/model versions, or extraction audit records for each derived fact.
- Whether MCP or host integrations grow a relevance-gated push hook that searches automatically before actions and measures context usefulness.
- Whether temporal contradiction handling becomes evaluated against known update cases rather than relying mainly on LLM duplicate/contradiction judgment.
- Whether community summaries become a major read-back surface, and whether their lineage back to episodes and facts remains reviewable.
- Whether graph backends diverge in search semantics, especially around embeddings, full-text indexes, Kuzu relation-node encoding, and Neptune/OpenSearch behavior.

## Bottom Line

Graphiti is a real trace-derived temporal context graph engine: raw episodes feed LLM extraction, dedupe, temporal invalidation, entity summaries, embeddings, and hybrid graph retrieval. It is strong evidence for graph-shaped, temporally aware agent memory, but weak evidence for automatic governance or high-authority instruction learning. Commonplace should borrow its provenance-aware temporal fact model and inspectable extraction policy, while keeping stronger review and promotion controls before derived facts become durable methodology.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Graphiti derives temporal graph facts, entity summaries, and retrieval state from episodes and message traces.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Graphiti requires separating episodes, entity nodes, facts, prompts, schemas, embeddings, and MCP/API tools by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: episodes, nodes, facts, summaries, and returned search results mostly advise future behavior as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: extraction prompts, schemas, search recipes, filters, graph queries, queues, and MCP tool definitions constrain or route behavior.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Graphiti stores rich memory, but read-back still depends on explicit host/API/MCP search.
- [Automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md) - contrasts: Graphiti automates extraction and invalidation of graph facts, not reviewed promotion into Commonplace-style notes or instructions.
