---
description: "REM review: episodic memory service with parsed episodes, vector/graph retrieval, LLM consolidation, and LangChain memory injection"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-02"
---

# REM

REM, from satyammistari, is an open-source "Recursive Episodic Memory" service for AI agents. At the reviewed commit it is a multi-service memory stack: a Go API writes structured episodes into Postgres, Qdrant, Neo4j, and Redis-backed queues; a Python worker parses, embeds, and consolidates episodes with OpenAI calls; a Python SDK exposes write/retrieve calls plus LangChain and AutoGen integrations; and a Next.js dashboard/marketing app presents the product surface. The implemented core is a write/retrieve episodic memory service with partial semantic consolidation wiring.

**Repository:** https://github.com/satyammistari/REM

**Reviewed commit:** [935e8be0a1fca5b23dbabfe16c48b562c1cd24cc](https://github.com/satyammistari/REM/commit/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc)

**Last checked:** 2026-06-02

## Core Ideas

**Episodes are the primary write artifact.** `POST /api/v1/episodes` validates `agent_id`, `user_id`, and content length, then `WriteService.WriteEpisode()` creates an `Episode`, parses the text through the Python worker when available, embeds the raw content, stores the episode row in Postgres, upserts an episode vector in Qdrant, creates an episode node in Neo4j, links it to the previous episode with `FOLLOWED_BY`, and publishes a Redis consolidation job ([episodes.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/api/handlers/episodes.go), [write_service.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/services/write_service.go), [episode.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/domain/episode.go)).

**The episode schema is a structured trace record.** Episodes retain raw content plus parsed entities, intent, outcome, domain, emotion signal, importance score, retrieval counters, consolidation flags, timestamps, and a `consolidated_into` pointer ([001_initial.sql](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/db/postgres/migrations/001_initial.sql), [episodes.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/db/postgres/episodes.go)). The Python parser prompt extracts intent, entities, domain, emotion, and importance from each episode, so the stored trace is partly raw and partly LLM-derived metadata ([parse_service.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/python-worker/services/parse_service.py)).

**Retrieval combines vector search, temporal graph expansion, recency, and use history.** `RetrieveService.Retrieve()` embeds the query, searches Qdrant episode vectors filtered by `agent_id`, optionally searches semantic memories, expands the top three episode hits through one-hop Neo4j temporal neighbors, reranks episodes by vector score, recency, and retrieval count, caps `top_k` at 20, increments retrieval counters asynchronously, and builds an `injection_prompt` ([retrieve_service.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/services/retrieve_service.go), [qdrant/client.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/db/qdrant/client.go), [neo4j/client.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/db/neo4j/client.go)). Context efficiency is retrieval-time bounding: `top_k`, `top_k*2` over-fetch, semantic inclusion, one-hop graph expansion, and a flat prompt builder; there is no prompt token budget or progressive disclosure layer.

**Semantic consolidation is designed but not fully API-wired.** The Python consolidation engine groups unconsolidated episodes by domain and intent keywords, asks `gpt-4o` to extract durable facts, attaches confidence, fact type, domain, evidence count, and source episode ids, and the Celery task embeds each fact and attempts to store it through `POST /api/v1/semantic` ([engine.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/python-worker/services/consolidation/engine.py), [tasks.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/python-worker/workers/tasks.py)). The Go API has `InsertSemanticMemory()` and Qdrant/Neo4j semantic-memory methods, but the router registers only `GET /api/v1/semantic`, not the POST endpoint or episode-consolidated PATCH used by the worker ([semantic.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/api/handlers/semantic.go), [router.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/api/router.go), [postgres/semantic.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/db/postgres/semantic.go)).

**The read-back surface is both explicit API and host integration.** The SDK exposes `retrieve()` and returns `result.injection_prompt` for caller-managed insertion into a model prompt ([client.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/sdk/python/rem_memory/client.py)). The LangChain integration is stronger: `REMMemory.load_memory_variables()` runs before LLM invocation, derives the query from the chain input, calls `retrieve_sync()`, and returns the prompt as `relevant_memories`; `save_context()` writes the user/assistant turn afterward ([langchain.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/sdk/python/rem_memory/integrations/langchain.py)). AutoGen support exposes helper methods to fetch context and build a system prefix, but the caller still decides how to wire it ([autogen.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/sdk/python/rem_memory/integrations/autogen.py)).

**Some product claims outrun implementation.** The README and dashboard present recursive consolidation, graph reasoning, and dashboards as product-level capabilities, but the source shows uneven maturity: graph neighbor expansion is used in retrieval, while `GetAgentGraphData()` currently returns empty nodes and edges after querying Neo4j; benchmark adapters call reset/delete endpoints that are not registered by the Go router; and consolidation worker storage calls target missing routes ([README.md](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/README.md), [graph.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/api/handlers/graph.go), [neo4j/client.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/db/neo4j/client.go), [rem_adapter.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/benchmarks/adapters/rem_adapter.py)).

## Artifact analysis

- **Storage substrate:** `graph` — Postgres `episodes` rows, Qdrant `episodes` vectors, Neo4j `Episode` nodes, and Redis-published consolidation jobs
- **Representational form:** `prose` `symbolic` `parametric` — raw prose traces and facts, symbolic metadata/schemas/prompts/routes, and distributed-parametric embeddings
- **Lineage:** `authored` `imported` `trace-extracted` — authored policies and wrappers, imported episode inputs from agents/integrations, and trace-derived parsed/consolidated memories
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — records advise as knowledge, prompts and wrappers instruct, routes select paths, schemas validate, retrieval scores rank, and consolidation learns semantic facts

**Episode records.** Storage substrate: Postgres `episodes` rows, Qdrant `episodes` vectors, Neo4j `Episode` nodes, and Redis-published consolidation jobs. Representational form: mixed raw prose trace, symbolic metadata, and distributed-parametric embeddings. Lineage: imported from an agent or integration after a task, enriched by LLM parsing and embedding, linked to prior episodes by insertion order, and later marked consolidated when the intended consolidation path succeeds. Behavioral authority: knowledge artifact when listed, retrieved, or used as source evidence; ranking artifact through vector similarity, recency, retrieval count, graph adjacency, and consolidation state.

**Semantic memory records.** Storage substrate: Postgres `semantic_memories`, Qdrant `semantic_memories`, and intended Neo4j `SemanticMemory` nodes. Representational form: prose fact plus symbolic fact type, confidence, evidence count, domain, source episode ids, active/superseded flags, and embedding. Lineage: LLM-distilled from clusters of unconsolidated episodes, with source episode ids as evidence pointers; invalidation is intended through active/superseded/contradicted fields, but I did not find implemented mutation routes for those states. Behavioral authority: knowledge artifact when returned by retrieval; advisory context when included in the injection prompt; ranking authority through semantic vector scores and filters.

**Parsing, consolidation, embedding, and retrieval policies.** Storage substrate: Go and Python source code, prompts, service configuration, model names, queue configuration, and database schema. Representational form: prose prompts plus symbolic schemas, thresholds, limits, routing code, Redis task schedules, and vector/graph query parameters. Lineage: authored system-definition artifacts; changes to prompts, model choices, top-k caps, graph depth, route registration, or scoring weights regenerate different retained artifacts and different read-back sets. Behavioral authority: instruction, validation, extraction, routing, ranking, and scheduling authority over what is retained and what reaches a future prompt.

**Integration memory wrappers.** Storage substrate: SDK package files and host framework configuration. Representational form: Python classes and assembled prose prompt strings. Lineage: authored wrappers around the REM API; each read-back output is ephemeral and derived from current input plus stored REM records. Behavioral authority: `REMClient.retrieve()` is pull-only until the caller inserts the prompt; LangChain `REMMemory` becomes a pre-action system-definition artifact for the chain because it automatically supplies `relevant_memories` before invocation and writes a new episode after response.

**Dashboard and benchmark artifacts.** Storage substrate: Next.js source, static product configuration, benchmark scripts, result directories when generated. Representational form: marketing prose, UI components, synthetic test data, metric scripts, and JSON output. Lineage: authored demos and evaluation harnesses; some endpoint assumptions do not match the registered Go API. Behavioral authority: adoption and evaluation evidence, not runtime memory authority.

Promotion path: REM has an intended raw-to-distilled path from interaction episode to parsed metadata, embedding, graph node, semantic fact, and prompt injection. It does not have a governed promotion ladder from candidate memory to reviewed rule, skill, validator, or instruction; higher authority comes from host integrations that decide to inject REM output.

## Comparison with Our System

| Dimension | REM | Commonplace |
|---|---|---|
| Primary purpose | Runtime memory service for agents and apps | Git-native methodology KB for agent operation |
| Canonical retained artifact | Structured episode plus optional semantic memory fact | Typed Markdown notes, instructions, reviews, sources, indexes, reports |
| Storage substrate | Postgres, Qdrant, Neo4j, Redis, SDK/dashboard code | Repository files plus generated indexes and validation/review reports |
| Write path | API writes, LLM parsing, embeddings, graph insertion, queued consolidation | Human/agent-authored artifacts, source snapshots, explicit review and validation |
| Read-back | Pull API/SDK plus LangChain pre-invoke memory injection | Mostly explicit pull through `rg`, indexes, links, skills, and loaded instructions |
| Governance | API validation, route auth, prompts, schema fields, benchmarks | Collection contracts, type specs, git diffs, validators, semantic gates, replacement archives |

REM is stronger than Commonplace as a service-shaped runtime substrate. It has API authentication, vector and graph stores, a Python SDK, host-framework wrappers, background workers, and benchmark scripts. Commonplace is stronger as a governed, inspectable knowledge system: artifacts are readable files with type contracts, citations, review state, validation, and git history.

The largest design difference is the authority boundary. REM can put memory back into a model call quickly, especially through LangChain memory variables. Commonplace makes behavioral authority more explicit: instructions, collection contracts, validators, and review gates are intentionally authored or promoted system-definition artifacts. REM's extracted semantic memories are useful advisory context, but the code does not show a review step that decides when a distilled fact should become a rule or enforcement mechanism.

**Read-back:** `both` — The API and SDK are pull surfaces, while LangChain `REMMemory.load_memory_variables()` is an instance-targeted, embedding-selected pre-invoke memory push from the receiving chain's perspective

### Borrowable Ideas

**Keep retrieval output as a named injection artifact.** Ready now as vocabulary. REM's `injection_prompt` is a useful boundary: the retrieval service returns a concrete prompt artifact instead of leaving every caller to format records from scratch.

**Use retrieval counters as part of memory aging.** Needs a concrete search layer. REM increments episode retrieval counts and folds them into reranking. Commonplace could use access evidence to prioritize review or indexing work, but should not let frequency become semantic authority by itself.

**Borrow explicit raw-to-distilled source ids, not automatic promotion.** Ready for trace-heavy workshops. REM's semantic memories carry `source_episode_ids`; Commonplace should preserve source snapshots or trace ids when deriving notes, while still requiring review before any instruction-like promotion.

**Keep host integration separate from the storage substrate.** Ready now. REM's SDK shows that write/retrieve storage can remain stable while LangChain and AutoGen wrappers decide activation. Commonplace should preserve the same separation between retained artifacts and agent-specific loading paths.

**Do not borrow multi-store complexity without an operational need.** REM's Postgres+Qdrant+Neo4j+Redis stack gives runtime affordances but increases deployment and consistency burden. Commonplace should only add such substrates for high-volume ingestion or retrieval problems that files and deterministic indexes cannot solve.

## Trace-derived learning placement

- **Trace source:** `session-logs` `trajectories` — REM stores agent episodes and LangChain human/assistant turns after tasks or framework turns
- **Learning scope:** `per-task` `cross-task` — episodes are written per task or turn and retained under agent/user/session identifiers for later retrieval
- **Learning timing:** `online` `staged` — write-path parsing and embedding happen synchronously, while consolidation is queued or scheduled
- **Distilled form:** `prose` `symbolic` `parametric` — semantic memories are prose facts with symbolic metadata/source ids and embeddings

**Trace source.** REM qualifies as trace-derived. The core trace is an agent episode: content submitted after a task or framework turn through `write()`, `save_context()`, or the episodes API. LangChain `save_context()` stores a combined human/assistant turn after model output, and the worker's scheduled tasks fetch unconsolidated episodes for consolidation ([langchain.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/sdk/python/rem_memory/integrations/langchain.py), [tasks.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/python-worker/workers/tasks.py)).

**Extraction.** The raw episode first gets parsed into intent, entities, domain, emotion, and importance. Consolidation then groups unconsolidated episodes by domain and overlapping intent keywords, limits cluster size, prompts an LLM for 1-5 durable facts, and records confidence, fact type, domain, evidence count, and source episode ids. The extraction oracle is the configured OpenAI chat model plus parser/compressor prompts; there is no reviewer acceptance gate in the code.

**Four fields.** The raw stage is episode records: mixed prose-symbolic-distributed artifacts in Postgres/Qdrant/Neo4j, lineage from agent traces plus parser/embedding derivations, and knowledge/audit authority until retrieved. The distilled stage is semantic memory facts: mixed prose fact, symbolic metadata, source ids, and embeddings, with advisory read-back authority and ranking/filtering authority. The system-definition layer is the prompt, clustering, route, queue, and scoring code that decides what becomes memory.

**Scope and timing.** Scope is by `agent_id`, `user_id`, session id, domain, and optional metadata at write time; retrieval filters primarily by `agent_id`. Timing is mixed: episodes are written per task or turn, parsing and embedding happen synchronously in the write path, consolidation is fire-and-forget or scheduled, and read-back happens before a caller's next task or before a LangChain invocation.

**Survey placement.** REM belongs in the trace-to-episode and trace-to-semantic-fact families. It strengthens the survey distinction between raw traces and distilled behavior-shaping artifacts, while also showing a common implementation hazard: the distillation loop can be designed in worker code before the API surface needed to persist and govern the distilled artifacts is fully wired.

## Read-back placement

**Read-back:** `both` — Direct API/SDK retrieval is pull. LangChain memory injection is push to the receiving chain because the framework calls `load_memory_variables()` before the LLM invocation and supplies returned retained episodes and semantic memories as `relevant_memories`.

**Read-back signal:** `identifier` `inferred / embedding` — LangChain push uses the configured `agent_id` as an identifier filter and embeds the current invocation input for Qdrant episode and semantic-memory retrieval.

**Read-back timing:** `pre-action` `post-action` — LangChain memory loading runs before model invocation, while `save_context()` writes the completed turn afterward for later retrieval.

**Faithfulness tested:** `no` — tests and benchmarks inspect retrieval and `injection_prompt` contents, but the review found no with/without-memory behavior ablation.

**Targeting and signal.** Pull retrieval triggers on `POST /api/v1/retrieve` or `REMClient.retrieve()`. LangChain push targets the current invocation instance: the framework's pre-invoke memory loading step derives a query from the current `input`, `question`, or `human_input`, uses the configured `agent_id` as an identifier filter, and sends the resulting prompt to that chain call. The final relevance selector is `inferred / embedding`: REM embeds the current query, searches Qdrant episode and semantic-memory collections under the `agent_id` filter, then uses graph-neighbor expansion, recency, retrieval count, and `top_k` to shape the returned set. Precision, recall, and context dilution are not verified from code.

**Timing relative to action.** Retrieval and LangChain memory loading happen before model response and can change the next action. Episode writes and consolidation happen after a task/turn or in background jobs, so they affect later retrievals rather than the current response.

**Selection, scope, and complexity.** Selection is bounded by `top_k` with a hard cap of 20, semantic-memory inclusion, one-hop graph expansion from at most three episode hits, and reranking. Scope is mostly agent-level; user/session metadata exists in episode records but is not a first-class retrieval filter in the reviewed retrieve request. Complexity is low to moderate: the injection prompt is a flat text block of memory snippets and learned facts, not a nested graph or multi-step navigation plan.

**Authority at consumption.** The API returns advisory context. LangChain's `relevant_memories` variable has stronger practical authority only if the chain prompt template actually uses that variable; the code can show availability, not prompt faithfulness. AutoGen helpers produce a system-prefix string, but host code must choose to prepend it.

**Faithfulness.** The repository includes integration tests for write/retrieve and benchmark scripts measuring whether expected answers appear in `injection_prompt` ([integration_test.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/tests/integration_test.go), [convomem.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/benchmarks/convomem.py)). I did not find a with/without-memory agent-behavior ablation proving that injected context changes downstream actions reliably.

**Other consumers.** Human operators can inspect agents, episodes, semantic memories, graph endpoints, dashboards, and benchmark outputs. At the reviewed commit, those surfaces are partly aspirational because several dashboard and graph claims depend on endpoints or graph data assembly that are incomplete.

## Curiosity Pass

**The strongest implemented loop is episodic retrieval, not recursive semantic memory.** The episode write and retrieve paths are concrete. Semantic consolidation logic exists, but persistence and status-update routes are missing from the Go API registration.

**Graph reasoning is narrower than the README suggests.** Retrieval uses Neo4j for one-hop temporal neighbor expansion, which is useful. The public graph endpoint's data assembly currently returns empty graph data, so "graph reasoning" should be read as partial implementation.

**The route surface is a useful maturity test.** Several code paths assume endpoints for semantic writes, consolidation status patches, or benchmark resets that the router does not expose. For Commonplace reviews, this is a good reminder to check integration seams, not just domain models.

**REM has good adoption affordances.** The SDK, LangChain wrapper, AutoGen helper, Docker compose, Makefile, and dashboard make the system approachable even though the backend is multi-store and operationally heavy.

**Prompt authority is easy to overstate.** Returning `injection_prompt` or `relevant_memories` makes memory available; whether it constrains the model depends on host prompt construction and runtime behavior.

## What to Watch

- Whether `POST /api/v1/semantic` and episode-consolidated PATCH routes are added and wired to Postgres, Qdrant, and Neo4j; that determines whether semantic consolidation is operational rather than worker-local.
- Whether retrieval adds user/session/domain filters and token budgets; without them, multi-user or long-running agents may get context that is relevant but too broad.
- Whether graph data assembly starts returning real nodes and edges and whether retrieval expands beyond temporal adjacency into semantic/causal relationships.
- Whether semantic memories gain review, expiry, contradiction, or confidence-update workflows; the schema has fields for governance, but the behavioral loop is not implemented.
- Whether benchmarks move from `injection_prompt` hit rate to downstream with/without-memory task behavior.

## Bottom Line

REM is a real episodic-memory service with trace-derived parsing, vector retrieval, temporal graph expansion, and host-framework read-back. Its strongest code-grounded contribution is the combination of structured episode traces with a named prompt injection artifact and a LangChain pre-invoke memory wrapper. Its semantic consolidation and graph-dashboard story are less complete at the reviewed commit, so Commonplace should treat it as evidence for runtime episodic read-back patterns, not as a finished governed learning system.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: REM derives parsed episodes and intended semantic facts from agent interaction traces.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: REM stores episodes in several substrates, but behavior changes only through retrieval and host injection.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: REM requires separating episodes, semantic facts, prompts, embeddings, graph links, SDK wrappers, and benchmarks by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: REM episodes, semantic facts, graph neighbors, and benchmark outputs mostly advise as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: REM parsing prompts, consolidation prompts, route handlers, retrieval scoring, SDK integrations, and validation code constrain future behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: REM turns task and conversation traces into retrievable episode records and intended semantic memories.
