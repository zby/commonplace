---
description: "REM review: episodic memory service with trace-learning episodes, vector/graph retrieval, LangChain injection, and partially wired consolidation"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-06-04"
---

# REM

REM, from satyammistari, is an open-source Recursive Episodic Memory service for AI agents. At the reviewed commit it is a multi-service memory stack: a Go API accepts episode writes and retrieval requests, Postgres stores structured episodes and intended semantic memories, Qdrant indexes episode and semantic-memory embeddings, Neo4j stores temporal episode links, Redis caches embeddings and publishes consolidation jobs, a Python worker parses and embeds content, and a Python SDK exposes API, LangChain, and AutoGen integration surfaces. The strongest implemented loop is trace-extracted episode storage plus vector/graph retrieval; the recursive semantic consolidation path exists in worker code but is only partly wired through the Go API.

**Repository:** https://github.com/satyammistari/REM

**Reviewed commit:** [935e8be0a1fca5b23dbabfe16c48b562c1cd24cc](https://github.com/satyammistari/REM/commit/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc)

**Last checked:** 2026-06-04

## Core Ideas

**Episodes are the primary durable memory unit.** `POST /api/v1/episodes` validates `agent_id`, `user_id`, and content length, then `WriteService.WriteEpisode()` creates an episode, asks the Python worker to parse the raw text when available, embeds the raw content, stores the episode row in Postgres, upserts an episode vector in Qdrant, creates a Neo4j episode node, links it to the previous episode with `FOLLOWED_BY`, and publishes a Redis consolidation job ([episodes.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/api/handlers/episodes.go), [write_service.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/services/write_service.go), [episode.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/domain/episode.go)).

**The trace record is partly raw and partly LLM-derived.** The episode table keeps raw content, parsed entities, intent, outcome, domain, emotion signal, importance score, retrieval counters, consolidation flags, timestamps, and a `consolidated_into` pointer ([001_initial.sql](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/db/postgres/migrations/001_initial.sql), [episodes.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/db/postgres/episodes.go)). The parser prompt extracts intent, entities, domain, emotion, and importance from each episode with `gpt-4o-mini`, so the retained episode is not just a transcript; it is a parsed trace artifact ([parse_service.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/python-worker/services/parse_service.py)).

**Retrieval combines identifier scoping, embedding similarity, temporal graph expansion, and use history.** `RetrieveService.Retrieve()` embeds the query, searches Qdrant episode vectors under `agent_id`, optionally searches semantic-memory vectors, expands the top three episode hits through one-hop Neo4j temporal neighbors, reranks episodes by vector score, recency, and retrieval count, caps `top_k` at 20, increments retrieval counters asynchronously, and returns an `injection_prompt` ([retrieve_service.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/services/retrieve_service.go), [qdrant/client.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/db/qdrant/client.go), [neo4j/client.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/db/neo4j/client.go)). Context efficiency is retrieval-time bounding rather than deep context management: top-k, `top_k*2` over-fetch, optional semantic inclusion, one-hop graph expansion, and a flat prompt builder. There is no token-budgeting, progressive disclosure, or multi-step navigation plan.

**Semantic consolidation is implemented in the worker but not fully registered in the API.** The Python consolidation engine clusters unconsolidated episodes by domain and intent-token overlap, asks `gpt-4o` to extract durable facts, and attaches confidence, fact type, domain, evidence count, and source episode ids ([engine.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/python-worker/services/consolidation/engine.py)). The Celery task embeds each fact, posts it to `POST /api/v1/semantic`, and patches source episodes via `/api/v1/episodes/{id}/consolidated` ([tasks.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/python-worker/workers/tasks.py)). The Go API has Postgres insertion helpers and Neo4j/Qdrant semantic methods, but the router registers only `GET /api/v1/semantic`, ordinary episode routes, and `POST /api/v1/retrieve`; it does not register the semantic-write or consolidated-status routes the worker calls ([semantic.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/api/handlers/semantic.go), [router.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/api/router.go), [postgres/semantic.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/db/postgres/semantic.go)).

**Read-back is exposed as both API retrieval and host-framework memory injection.** The SDK exposes `retrieve()` and returns `result.injection_prompt` for caller-managed insertion ([client.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/sdk/python/rem_memory/client.py)). The LangChain wrapper is stronger: `REMMemory.load_memory_variables()` runs before LLM invocation, derives the retrieval query from the chain input, calls `retrieve_sync()`, and returns the prompt under `relevant_memories`; `save_context()` writes the human/assistant turn after the response ([langchain.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/sdk/python/rem_memory/integrations/langchain.py)). The AutoGen helper returns context strings and system prefixes, but the caller still chooses how to wire them ([autogen.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/sdk/python/rem_memory/integrations/autogen.py)).

**Some product claims outrun the current implementation.** The README presents recursive consolidation, graph reasoning, dashboards, and forgetting policy as first-class capabilities ([README.md](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/README.md)). The source shows real episode write/retrieve mechanics, but graph use is currently one-hop temporal neighbor expansion, `GetAgentGraphData()` returns empty nodes and edges after querying Neo4j, benchmark reset calls try unregistered delete routes, and consolidation storage calls target missing API routes ([graph.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/api/handlers/graph.go), [neo4j/client.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/internal/db/neo4j/client.go), [rem_adapter.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/benchmarks/adapters/rem_adapter.py)).

## Artifact analysis

- **Storage substrate:** `rdbms` `vector` `graph` `kv` `service-object` — Episodes persist as Postgres rows, Qdrant vectors, Neo4j episode nodes, Redis queue/cache state, and SDK/API service objects that assemble memory for host frameworks.
- **Representational form:** `prose` `symbolic` `parametric` — Raw episode text and semantic facts are prose; schemas, route handlers, prompts, metadata, graph edges, counters, and API wrappers are symbolic; embeddings in Qdrant are distributed-parametric selectors.
- **Lineage:** `authored` `imported` `trace-extracted` — API, prompts, schemas, retrieval policy, and integrations are authored; episode inputs are imported from agents and host applications; parser metadata, embeddings, retrieval counters, and intended semantic facts are extracted from use traces.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Stored memories advise as context, injection prompts and integration wrappers instruct host calls, routes and graph expansion choose paths, request/schema checks validate, Qdrant/reranking shape selection, and parser/consolidation worker code learns derived fields and intended facts.

**Episode records.** Storage substrate: Postgres `episodes`, Qdrant `episodes`, Neo4j `Episode` nodes, and Redis-published consolidation jobs. Representational form: raw prose trace plus symbolic metadata, counters, timestamps, consolidation flags, graph links, and embedding vectors. Lineage: imported from an agent task or framework turn, then enriched by LLM parsing and embedding. Behavioral authority: knowledge artifact when listed or returned as memory context; ranking artifact through vector similarity, recency, retrieval count, graph adjacency, and `top_k`.

**Semantic-memory records.** Storage substrate: Postgres `semantic_memories`, Qdrant `semantic_memories`, and intended Neo4j `SemanticMemory` nodes. Representational form: prose fact plus symbolic fact type, confidence, evidence count, source episode ids, active/superseded fields, and embedding. Lineage: intended LLM distillation from clusters of unconsolidated episodes. Behavioral authority: advisory knowledge when listed or included in an injection prompt, plus ranking authority through vector score and filters. At this commit, the worker's route assumptions prevent the semantic-write loop from being a complete operational path.

**Parsing, consolidation, embedding, and retrieval policies.** Storage substrate: Go and Python source code, prompts, model names, API routes, queue configuration, and database/vector/graph schemas. Representational form: authored prose prompts plus symbolic service code, thresholds, limits, queue names, and vector/graph query parameters. Lineage: authored system-definition artifacts; changing these policies regenerates parsed fields, embeddings, candidate clusters, selected memories, and assembled prompts. Behavioral authority: instruction, validation, routing, ranking, and learning authority over what gets retained and what reaches future calls.

**Integration wrappers.** Storage substrate: SDK files and host-framework configuration. Representational form: Python classes plus assembled prompt strings. Lineage: authored wrappers around the REM API; each read-back output is ephemeral and derived from the current input plus stored REM records. Behavioral authority: `REMClient.retrieve()` is pull-only until a caller inserts the returned prompt, while LangChain `REMMemory` becomes a pre-invocation memory supplier for a chain when its prompt template consumes `relevant_memories`.

**Promotion path.** REM has a raw-to-derived path from interaction episode to parsed metadata, embedding, temporal graph node, intended semantic fact, and prompt injection. It does not have a governed promotion ladder from candidate memory to reviewed rule, skill, validator, or enforced instruction. Retrieval-count increments operationally promote frequently retrieved episodes in ranking; semantic consolidation would promote clusters of episodes into higher-level facts once the missing write/status routes are registered.

## Comparison with Our System

| Dimension | REM | Commonplace |
|---|---|---|
| Primary purpose | Runtime episodic memory service for agents and applications | Git-native methodology KB for agent operation |
| Canonical retained artifact | Structured episode plus intended semantic memory fact | Typed Markdown notes, instructions, reviews, sources, indexes, reports |
| Storage substrate | Postgres, Qdrant, Neo4j, Redis, API/SDK code | Repository files plus generated indexes and validation/review reports |
| Write path | API writes, LLM parsing, embeddings, graph insertion, queued consolidation attempt | Human/agent-authored artifacts, source snapshots, explicit review and validation |
| Read-back | Pull API/SDK plus LangChain pre-invocation memory loading | Mostly explicit pull through `rg`, indexes, links, skills, and loaded instructions |
| Governance | API validation, auth, schema fields, prompts, and tests | Collection contracts, type specs, git diffs, validators, semantic gates, replacement archives |

REM is stronger than Commonplace as service infrastructure. It has authentication, vector and graph stores, a Python SDK, host-framework wrappers, background workers, and benchmark adapters. Commonplace is stronger as a governed, inspectable knowledge system: artifacts are readable files with type contracts, citations, review state, validation, and git history.

The largest design difference is the authority boundary. REM can put remembered context back into a model call quickly, especially through LangChain memory variables. Commonplace makes behavioral authority more explicit: instructions, collection contracts, validators, and review gates are intentionally authored or promoted system-definition artifacts. REM's extracted memories are useful advisory context, but the code does not show a review step that decides when a distilled fact should become a rule or enforcement mechanism.

### Borrowable Ideas

**Keep retrieval output as a named injection artifact.** Ready now as vocabulary. REM's `injection_prompt` is a useful boundary: the retrieval service returns a concrete prompt artifact instead of leaving every caller to format records from scratch.

**Use access counters as salience evidence without granting truth authority.** Needs a concrete activation workflow. REM increments retrieval counts and folds them into ranking. Commonplace could use access evidence to prioritize review or indexing work, but frequency should not make a claim truer or more authoritative.

**Preserve raw-to-distilled source ids.** Ready for trace-heavy workshops. REM's intended semantic memories carry source episode ids; Commonplace should preserve source snapshots, trace ids, or run ids when deriving notes from workshop traces.

**Separate storage substrate from host integration.** Ready now. REM's API can remain stable while LangChain and AutoGen wrappers decide how remembered material reaches a host prompt. Commonplace should keep the same distinction between retained artifacts and agent-specific loading paths.

**Do not borrow multi-store complexity before the operational need is real.** REM's Postgres+Qdrant+Neo4j+Redis stack gives runtime affordances but creates consistency and route-surface burdens. Commonplace should add such substrates only for high-volume ingestion or retrieval problems that files and deterministic indexes cannot solve.

## Write side

**Write agency:** `automatic` `manual` — Automatic writes come through API/SDK episodes, parser enrichment, embeddings, graph nodes, retrieval-counter updates, Redis consolidation jobs, and the worker's attempted semantic-memory loop. Manual agency exists through callers choosing what episode content to write and through API/dashboard inspection surfaces, but the reviewed memory loop is primarily automatic.

**Curation operations:** `promote` — Retrieval increments existing episode counters and the reranker uses those counters as a bounded salience bonus. The worker contains consolidation/synthesis logic, but because the semantic POST and episode consolidated PATCH routes are not registered at this commit, I am not counting those as operational store-changing curation tokens.

### Trace-learning

**Trace source:** `session-logs` `trajectories` — REM stores after-task episode descriptions and LangChain human/assistant turns as durable traces.

**Learning scope:** `per-task` `cross-task` — Episodes are written per task or turn and retained under agent/user/session identifiers for later retrieval across future tasks for that agent.

**Learning timing:** `online` `staged` — Parsing, embedding, and episode storage happen during the write path; consolidation is queued or scheduled and would run later when enough unconsolidated episodes exist.

**Distilled form:** `prose` `symbolic` `parametric` — Durable outputs include prose traces/facts, symbolic metadata/counters/source ids/routes, and embeddings.

**Trace source.** REM qualifies as trace-learning. The core trace is an agent episode written after a task or framework turn through `write()`, `save_context()`, or the episodes API. LangChain `save_context()` stores a combined human/assistant turn after model output; scheduled and triggered worker tasks fetch unconsolidated episodes for consolidation ([client.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/sdk/python/rem_memory/client.py), [langchain.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/sdk/python/rem_memory/integrations/langchain.py), [tasks.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/python-worker/workers/tasks.py)).

**Extraction.** The raw episode first gets parsed into intent, entities, domain, emotion, and importance. The intended consolidation stage then groups unconsolidated episodes by domain and overlapping intent tokens, limits cluster size, prompts an LLM for one to five durable facts, and records confidence, fact type, domain, evidence count, and source episode ids. The extraction oracle is the configured OpenAI chat model plus authored parser/consolidation prompts; there is no reviewer acceptance gate in the code.

**Scope and timing.** Scope is mainly by `agent_id`, with user/session metadata available in episode records but not central to retrieval filtering. Timing is mixed: episodes are written per task or turn, parsing and embedding happen synchronously in the write path, consolidation is fire-and-forget or scheduled, and read-back happens before a caller's future task or before a LangChain invocation.

**Survey position.** REM belongs in the trace-to-episode and intended trace-to-semantic-fact families. It strengthens the survey distinction between raw trace retention and distilled behavior-shaping artifacts, while also showing a common implementation hazard: a distillation loop can be present in worker code before the route surface needed to persist and govern the distilled artifacts is complete.

## Read-back

**Read-back:** `both` — Direct API/SDK retrieval is pull. LangChain memory loading is push to the receiving chain because the framework calls `load_memory_variables()` before LLM invocation and supplies returned memory as `relevant_memories`.

**Read-back signal:** `identifier` `inferred / embedding` — The pre-invocation LangChain path uses the configured `agent_id` as an identifier filter and embeds the current input for Qdrant episode and semantic-memory retrieval.

**Faithfulness tested:** `no` — The repository tests write/retrieve plumbing and prompt contents, but I did not find a with/without-memory behavior ablation showing that loaded memory changes downstream agent actions reliably.

**Targeting and signal.** Pull retrieval triggers on `POST /api/v1/retrieve` or `REMClient.retrieve()`. LangChain read-back targets the current invocation instance: the wrapper derives a query from the current `input`, `question`, or `human_input`, filters by the configured `agent_id`, and returns an injection prompt for that chain call. The final selector is embedding-based, then shaped by temporal graph neighbors, recency, retrieval counts, semantic inclusion, and `top_k`. Precision, recall, and context dilution are not verified from code.

**Injection point.** Retrieval and LangChain memory loading happen before model response and can change the next action if the host prompt consumes the memory variable. Episode writes and consolidation attempts happen after a task/turn or in background jobs, so they affect later retrievals rather than the current response.

**Selection, scope, and complexity.** Selection is bounded by `top_k` with a hard cap of 20, optional semantic-memory inclusion, one-hop graph expansion from at most three episode hits, and reranking. Scope is mostly agent-level; user/session metadata exists in episode records but is not a first-class retrieval filter in the reviewed request type. Complexity is moderate: the injection prompt is a flat text block of snippets and learned facts, not a nested graph or multi-step navigation plan.

**Authority at consumption.** The API returns advisory context. LangChain's `relevant_memories` variable has practical instruction/context authority only if the chain prompt template actually uses that variable. AutoGen helpers produce a system-prefix string, but host code must choose to prepend it.

**Faithfulness.** The repository includes integration tests for write/retrieve and benchmark scripts measuring returned `injection_prompt` content ([integration_test.go](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/go-api/tests/integration_test.go), [convomem.py](https://github.com/satyammistari/REM/blob/935e8be0a1fca5b23dbabfe16c48b562c1cd24cc/benchmarks/convomem.py)). I did not find an agent-behavior ablation that compares downstream actions with and without retrieved REM context.

**Other consumers.** Human operators can inspect episodes, semantic-memory listings, graph endpoints, dashboard surfaces, and benchmark outputs. At the reviewed commit, some of those surfaces are partially aspirational because dashboard and graph claims depend on endpoints or graph assembly that are incomplete.

## Curiosity Pass

**The implemented loop is episodic retrieval more than recursive semantic memory.** Episode write and retrieve paths are concrete. Semantic consolidation logic exists, but persistence and source-episode status updates depend on missing routes.

**Graph reasoning is narrower than the README suggests.** Retrieval uses Neo4j for one-hop temporal neighbor expansion, which is useful. The public graph endpoint's data assembly currently returns empty graph data.

**Route registration is the best maturity test here.** The domain model and database helpers are richer than the exposed API. For Commonplace reviews, REM is a reminder to check the route or command surface, not just internal service code.

**Prompt availability is easy to overstate.** Returning `injection_prompt` or `relevant_memories` makes memory available; whether it constrains the model depends on host prompt construction and runtime behavior.

## What to Watch

- Whether `POST /api/v1/semantic` and `/api/v1/episodes/{id}/consolidated` are registered and wired through Postgres, Qdrant, and Neo4j. That determines whether semantic consolidation is operational rather than worker-local.
- Whether retrieval adds user/session/domain filters and token budgets. Without them, long-running or multi-user agents may get context that is relevant but too broad.
- Whether graph data assembly starts returning real nodes and edges, and whether retrieval expands beyond temporal adjacency into semantic or causal relationships.
- Whether semantic memories gain review, expiry, contradiction, or confidence-update workflows. The schema has governance fields, but the behavioral loop is not implemented.
- Whether benchmarks move from prompt hit rate to downstream with/without-memory task behavior.

Relevant Notes:

- [Trace-learning techniques in related systems](../trace-learning-techniques-in-related-systems.md) - places: REM derives parsed episodes and intended semantic facts from agent interaction traces.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: REM stores episodes in several substrates, but behavior changes only through retrieval and host injection.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: REM requires separating episodes, semantic facts, prompts, embeddings, graph links, SDK wrappers, and benchmarks by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: REM episodes, semantic facts, graph neighbors, and benchmark outputs mostly advise as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: REM parsing prompts, consolidation prompts, route handlers, retrieval scoring, SDK integrations, and validation code constrain future behavior.
- [Use trace extraction](../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) - exemplifies: REM turns task and conversation traces into retrievable episode records and intended semantic memories.
