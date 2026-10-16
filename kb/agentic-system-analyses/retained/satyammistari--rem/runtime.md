---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "REM runtime baseline tracing API admission, context retrieval, worker scheduling and consolidation gaps at the frozen revision."
run-id: AAS-2026-10-14-rem-a81fdc774400-01
reviewed-boundary: "935e8be0a1fca5b23dbabfe16c48b562c1cd24cc"
---

# REM runtime report

## Runtime account

REM supplies agent memory infrastructure, not the enclosing task executor. Its declared work is writing interaction descriptions, extracting durable patterns, and returning selected context before another task. The implementation contains each stage, but the shipped connections do not establish a functioning automatic end-to-end consolidation loop. In particular, the write-side Redis list is not the Celery dispatch interface, and the task's semantic write-back endpoints are not registered. These are implementation findings, not failed execution observations. See [RT-CLM-memory-loop](#rt-clm-memory-loop), [RT-RTE-episode-write](#rt-rte-episode-write), [RT-RTE-context-retrieve](#rt-rte-context-retrieve), and [RT-RTE-worker-consolidation](#rt-rte-worker-consolidation).

Evidence is SRC-1 at the boundary's commit. All findings below are implementation inspection or attributed design. No target program, service, test, benchmark or provider call was executed; operation, actual activation and benefit remain unobserved. Added detailed inspection beyond the boundary's initial coverage includes auth middleware and handlers, agent/episode/retrieval/semantic handlers, domain serialization, PostgreSQL episode methods, complete Qdrant and Neo4j clients, Python route wiring and direct consolidation handler, embedding service, complete SDK HTTP layer and both integration adapters, SDK result types, migration file and transactional migration runner, Makefile, seed driver and benchmark adapter. These paths belong to the already registered source; no additional source identity is introduced.

### Ordinary invocation and ownership

Conditional on a running service with prepared schema and a registered agent, a caller supplies an API key, agent identity, user identity and a description of a completed task. The SDK constructs HTTP JSON; Go owns request progression after admission. It validates required fields and a trimmed content byte length strictly greater than 50 and less than 10000, creates a UUID episode, looks up the preceding episode for that agent, requests parsing from Python best-effort, obtains an embedding from cache or Python, then writes PostgreSQL, Qdrant and Neo4j sequentially. Python delegates parsing and embedding to OpenAI, not to another task-performing agent. Failed parsing preserves defaults; a failed embedding prevents the first durable write. Later storage failure returns an error after earlier effects may already exist. On success the API returns 201 with an episode ID and `stored`, while a detached goroutine attempts queue publication. This return does not certify consolidation. SRC-1: `sdk/python/rem_memory/client.py`, `go-api/internal/api/handlers/episodes.go`, `go-api/internal/services/write_service.go`, `go-api/internal/domain/episode.go`.

Before a later task the host supplies a query and agent ID. Go obtains an embedding, concurrently searches episode vectors and optionally semantic vectors, reloads episode text from PostgreSQL, expands one-hop temporal neighbors of the first three vector hits, reranks episodes and returns JSON plus an injection string. Selection, not a model, decides which retained episodes enter that string. The host owns actual prompt placement and subsequent action. A detached retrieval-count update can influence future rankings. The SDK attempts typed response conversion before returning any injection string. Nonempty Go episode or semantic results fail that conversion as detailed below, so the server's available string does not reach LangChain's memory variable or AutoGen's context helper through those ordinary SDK paths. Neither adapter grants REM control of host tools or guarantees obedience to the returned content. SRC-1: `go-api/internal/services/retrieve_service.go`, `sdk/python/rem_memory/client.py`, `sdk/python/rem_memory/integrations/langchain.py`, `sdk/python/rem_memory/integrations/autogen.py`. See [RT-BAP-context-injection](#rt-bap-context-injection).

Two representation boundaries limit that account. Go's `Episode` struct has exported PascalCase fields without JSON tags; list/get and nested retrieval responses therefore do not match consumers looking for lowercase underscore keys. Although the SDK defaults several missing episode fields, it also passes `ep.get("created_at")`, which is None for Go's `CreatedAt`, into the required non-null datetime field of `EpisodeResult`. Nonempty ordinary Go episode results therefore fail typed conversion in retrieve and list_episodes; they do not return blank/defaulted episode objects. Independently, Go's `SemanticResult` has no created_at field, while SDK `SemanticMemory` requires a datetime and receives `sm.get("created_at")`; nonempty semantic retrieval fails that constructor even without episode hits. Both loops precede construction of `RetrieveResult` and handoff of its injection_prompt. The server-built string can contain raw content and remain available to a direct HTTP consumer, but that does not establish SDK or adapter delivery. A nil semantic result slice serialized as null is another independent failure at SDK iteration. The consolidation engine separately reads lowercase keys and can receive Go episodes as `Domain`, `Intent`, `RawContent`: domain defaults to general and intent defaults empty, preventing intended intent-overlap clustering. These are deterministic source-level compatibility findings, not observed executions. SRC-1: `go-api/internal/domain/episode.go`, `go-api/internal/api/handlers/episodes.go`, `go-api/internal/services/retrieve_service.go`, `sdk/python/rem_memory/client.py`, `sdk/python/rem_memory/types.py`, `python-worker/services/consolidation/engine.py`. See [RT-OBJ-episode](#rt-obj-episode) and [RT-RTE-context-retrieve](#rt-rte-context-retrieve).

### Four forcing cases and bounded guarantees

1. **Partial write / caller retry.** After PostgreSQL insert, a Qdrant or Neo4j error returns failure without compensating prior stores. SDK connection/timeout retries repeat POST; each service invocation generates a fresh UUID. Thus the write service offers sequential multi-store writes, not atomic exactly-once admission. Owner: Go write service. Enforcement point: individual calls and error returns. Guarantee strength: best effort. Implementation conclusion status: wired. Operation conclusion status: uninspected. Required external contracts: successful store responses, provider availability and compatible vectors. Covered path: SDK and direct Go episode POST. Alternate paths: retries and direct database administration are not a cross-store transaction. SRC-1: `go-api/internal/services/write_service.go`, `go-api/internal/domain/episode.go`, `sdk/python/rem_memory/client.py`.

2. **Cached authentication / alternate resource access.** Cold API-key lookup verifies bcrypt, but a cache hit uses only the first 12 characters and bypasses full-key comparison. Episode and retrieval handlers use supplied IDs without matching the authenticated user; agent get/list do enforce user scoping, so that narrower protection cannot be generalized to memory endpoints. Public key issuance additionally accepts a user ID without a proof-of-possession step. Owner: Go middleware and handlers. Enforcement point: protected route group, cache/database branch and individual handlers. Guarantee strength: best effort, not an invariant of tenant isolation. Implementation conclusion status: wired. Operation conclusion status: uninspected. Required external contracts: trustworthy cache/database plus separately imposed network/identity restrictions. Covered path: Go `/api/v1` protected routes; alternate worker HTTP paths lack this middleware. Current valid keys, grants and deployed isolation are uninspected, not inferred from examples. SRC-1: `go-api/internal/api/router.go`, `go-api/internal/api/middleware/auth.go`, `go-api/internal/api/handlers/auth.go`, `go-api/internal/api/handlers/agents.go`, `go-api/internal/api/handlers/episodes.go`, `go-api/internal/api/handlers/retrieve.go`.

3. **Background publication versus explicit dispatch.** Go pushes plain JSON to `rem:jobs:consolidation`; inspected worker wiring uses Celery's named tasks and `consolidation` queue, with no reader bridging the list. Celery beat is a distinct six-hour route, not proof that write publication triggers processing. Its eligibility heuristic uses stored agent totals; the write path explicitly leaves stats updates as a no-op. Even explicit task dispatch meets the lowercase-episode mismatch and missing write-back endpoints. Owner: Redis publisher / Celery scheduler and task. Guarantee strength: no claimed guarantee for completed consolidation from a successful episode return. Implementation conclusion status: afforded for the full loop, wired for the individual publication/task mechanisms. Operation conclusion status: uninspected. SRC-1: `go-api/internal/db/redis/client.go`, `python-worker/workers/celery_app.py`, `python-worker/workers/tasks.py`, `go-api/internal/services/write_service.go`. See [RT-ABS-worker-bridge](#rt-abs-worker-bridge) and [RT-ABS-writeback-routes](#rt-abs-writeback-routes).

4. **Direct model-dependent computation versus persistence.** A caller can POST supplied episode dictionaries to Python `/consolidate` and receive model-produced candidates without any Go auth middleware or durable write-back. This route can avoid the Go serialization mismatch if the caller supplies the engine's lowercase keys; it does not repair missing semantic admission. The seed driver calls this route but omits the API key on its preceding protected episode fetch and does not store returned semantic candidates. Owner: Python request handler and model engine, caller for inputs. Enforcement point: Pydantic request checks and engine candidate filters. Guarantee strength: protocol for response shape, not semantic truth or persistence. Implementation conclusion status: wired. Operation conclusion status: uninspected. External contract: OpenAI responses and accessible configured worker. SRC-1: `python-worker/main.py`, `python-worker/api/router.py`, `python-worker/api/handlers/consolidate.py`, `python-worker/services/consolidation/engine.py`, `scripts/seed_demo.py`. See [RT-RTE-direct-consolidation](#rt-rte-direct-consolidation).

These cases challenge atomic storage, identity isolation, automatic maintenance and the equivalence of generated candidates with retained memories. They do not establish deployed exploitability, actual provider output, benchmark scores or all possible service failure combinations.

### Execution envelope, context and change admission

`make dev` starts Go, Uvicorn and the frontend, not a Celery worker or beat process. The Go entry point initializes stores and schemas before listening, adds panic recovery and request IDs, logs requests and shuts down on signal. Python requires an OpenAI key, performs a nonfatal startup embedding check, and installs three HTTP routes. The unapplied initial SQL file creates trg_episodes_set_updated_at twice without dropping it before the second creation. The migration runner executes the whole file transactionally and returns the error; main treats migration failure as fatal before listening. Thus this startup inventory does not establish fresh-install readiness; an externally prepared/applied migration state is a different condition. Default benchmark drivers also generate agent IDs without creating corresponding agent rows, while episodes.agent_id is a foreign key, so default benchmark executability is not established. Caller-supplied registered agents are a different condition. SRC-1: `go-api/internal/db/postgres/migrations/001_initial.sql`, `go-api/internal/db/postgres/client.go`, `go-api/cmd/api/main.go`, `benchmarks/longmemeval.py`, `benchmarks/locomo.py`, `benchmarks/convomem.py`, `benchmarks/adapters/rem_adapter.py`.

> if _, err := tx.Exec(ctx, string(sqlBytes)); err != nil {
> 	_ = tx.Rollback(ctx)
> 	return fmt.Errorf("apply migration %s: %w", name, err)
> }
> --- `go-api/internal/db/postgres/client.go`

> if err := db.RunMigrations(ctx); err != nil {
> 	logger.Fatal("postgres migrations failed", zap.Error(err))
> }
> --- `go-api/cmd/api/main.go`

Neither inspected entry point establishes a deployed sandbox or tenant boundary. Capability surface includes store writes and remote model calls; actual process/network grants and deployed isolation remain unknown. CORS configuration does not replace request authentication. SRC-1: `Makefile`, `go-api/cmd/api/main.go`, `python-worker/main.py`.

Model decision policy is static shipped prompt text plus ordinary code; numerical models are separately characterized in [RT-CMP-parse-service](#rt-cmp-parse-service), [RT-CMP-consolidation-engine](#rt-cmp-consolidation-engine), and [RT-CMP-embed-service](#rt-cmp-embed-service). No inspected request supplies provider-native tools, shell commands, dynamic extension code or remote task-performing subagents. That bounded request-shape observation does not describe an excluded host's capabilities or provider internals. The model chooses parse fields and candidate facts; software owns clustering, retrieval ranking and HTTP/persistence progression. There is no answer oracle in these runtime routes; model confidence and host-supplied outcome labels are not reference answers.

Working-context control consists of selecting retained context for a later invocation and limiting consolidation input: at most 15 episodes per cluster and 500 raw-content characters per included episode. Source IDs and evidence counts nevertheless cover the full cluster, including episodes not supplied in that model request. This is selective input construction, not proof that removed host conversation turns can be recovered verbatim. A separate worker request resembles a computation frame with selected inputs and a returned candidate list; the model window is not a reference-following heap. Host trimming, host context lifetime and whether injected context fits its window are outside the supplied integration machinery. SRC-1: `python-worker/services/consolidation/engine.py`, `go-api/internal/services/retrieve_service.go`, `sdk/python/rem_memory/integrations/langchain.py`.

Runtime knowledge admission is caller-origin episode storage and attempted software/model semantic admission, not per-content human approval. Generic API caller identity leaves human authorship unresolved. Source product changes are instead developer fork/branch/PR contributions, with no inspected model-driven installation path; the README's contribution procedure and Makefile build targets are design/development surfaces, not an autonomous product successor selector. Memory revision semantics remain for the memory analyst. SRC-1: `README.md`, `Makefile`, `python-worker/workers/tasks.py`.

## Shared records

### Components

#### RT-CMP-parse-service
Label: ParseService model

Source-native identity: `ParseService.model = "gpt-4o-mini"`; distributed-parametric remote chat model, with natural-language prompts and symbolic JSON response handling in client code. Storage substrate: provider-owned weights, opaque here; no local weights. Parameters do not change through any inspected REM training operation. Exact version is not pinned: the alias can resolve to another provider model revision. Provider internals and actual resolution are uninspected. This component supplies structured interpretation for [RT-RTE-episode-write](#rt-rte-episode-write), with error fallback rather than a truth guarantee. SRC-1: `python-worker/services/parse_service.py`.

> self.model = "gpt-4o-mini"
> --- `python-worker/services/parse_service.py`

#### RT-CMP-consolidation-engine
Label: ConsolidationEngine model

Source-native identity: engine's `gpt-4o` chat model. Representational form: distributed-parametric; storage substrate: opaque provider weights. No inspected REM parameter update is wired. Exact model version is not pinned, and the mutable provider alias can resolve differently. Natural-language extraction instructions and JSON parsing are local, separately inspectable control material. Used by [RT-RTE-worker-consolidation](#rt-rte-worker-consolidation) and [RT-RTE-direct-consolidation](#rt-rte-direct-consolidation). SRC-1: `python-worker/services/consolidation/engine.py`.

> self.model = "gpt-4o"
> --- `python-worker/services/consolidation/engine.py`

#### RT-CMP-embed-service
Label: EmbedService model

Source-native identity: `text-embedding-3-large`. Representational form: distributed-parametric model producing dense vectors. Storage substrate: provider weights plus returned vectors cached in Redis and stored in Qdrant. The inspected service calls embeddings, not parameter updates. Exact model version is not pinned; endpoint alias resolution and provider internals remain opaque. The service declares `dimensions = 1536`, and Qdrant collections are created for 1536 dimensions, but the embedding request does not pass that dimension argument. Compatibility is an external-contract dependency, not established by the attribute. SRC-1: `python-worker/services/embed_service.py`, `go-api/internal/db/qdrant/client.go`.

> resp = await self.client.embeddings.create(
>     model=self.model,
>     input=normalized,
> )
> --- `python-worker/services/embed_service.py`

### Operative objects

#### RT-OBJ-episode
Label: Episode runtime envelope

Identity: Go `domain.Episode`, distinct from its derived vector and graph node. Natural-language part: raw description and interpreted intent; symbolic part: UUIDs, timestamps, outcome labels, parsed entities, consolidation flags and retrieval counts. Storage substrate: PostgreSQL row; Qdrant holds separately derived numerical vectors and symbolic payload, Neo4j temporal node/edges. This record identifies the envelope and serialization, not a complete memory-revision assessment. SRC-1: `go-api/internal/domain/episode.go`, `go-api/internal/db/postgres/episodes.go`, `go-api/internal/services/write_service.go`.

> type Episode struct {
> 	EpisodeID              string
> 	AgentID                string
> 	UserID                 string
> 	SessionID              string
> 	TeamID                 string
> 	RawContent             string
> --- `go-api/internal/domain/episode.go`

The absence of JSON tags in the full inspected struct is consequential: consumers asking for lowercase underscore keys do not receive matching episode fields without another transformation. The inspected handlers return this struct directly, and no such transformation appears on those paths. In particular, Go emits CreatedAt; the SDK asks for created_at and passes None to a required datetime. This rejects nonempty episode retrieval/list conversion before a typed result or injection string is returned, rather than silently producing defaulted episode objects. SRC-1: `sdk/python/rem_memory/client.py`, `sdk/python/rem_memory/types.py`.

> created_at=ep.get("created_at"),
> score=float(item.get("score", 0.0)),
> --- `sdk/python/rem_memory/client.py`

> consolidated: bool
> created_at: datetime
> score: float  # retrieval relevance score
> --- `sdk/python/rem_memory/types.py`

### Routes

#### RT-RTE-episode-write
Label: Episode write admission

Endpoints and progression: caller SDK or direct HTTP → protected Go POST `/api/v1/episodes` → best-effort Python parse → mandatory cached/remote embedding → PostgreSQL insert → Qdrant upsert → Neo4j node and best-effort temporal edge → detached Redis publication → 201. Owner: Go service after handler validation; OpenAI interprets only parsing and embeddings. Caller supplies agent/user/session IDs, raw text and outcome; UUID and timestamps are software-generated. SRC-1: `go-api/internal/api/router.go`, `go-api/internal/api/handlers/episodes.go`, `go-api/internal/services/write_service.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Episode ID, agent ID, timestamp and stored status after sequential store calls; failures return errors, possibly after durable effects.
- Later read-back: Episode rows can be listed, fetched or selected through retrieval in later calls; vectors seed retrieval and temporal IDs support expansion.
- Delegated visibility: Parser sees full content; embedder sees normalized content; stores receive the row or derived parts, not a delegated task mandate.
- Selection predicate: Required nonempty agent/user/content and strict handler length bounds; embedding success and store success govern completion, not content truth.
- Invalidation or expiry: Embedding cache has 24-hour TTL; this write route does not assign an episode expiry or rollback prior stores.
- Activation or effect: Inserts retained episode, vector and graph node; publication attempts later maintenance. Actual later behavioral use is unobserved.
- Evidence limits: Static implementation only; successful multi-store operation and full consolidation are not observed. Fresh startup is blocked by the duplicate trigger in the unapplied migration; episode admission additionally requires an existing agent row under its foreign key. A running prepared deployment is a separate condition.

Admission: open caller writes, not a bounded experiment. The caller proposes content; Go decides structural acceptance and can reject missing/short/long input or failed dependencies. Python model proposes parse metadata; Go admits nonempty fields and range-checks importance. There is no per-content human approval or independent answer oracle; human contribution is unresolved for a generic caller. Trigger is a caller invocation, proposed change is a new episode, and guidance is the parser's fixed extraction prompt. Raw input plus admitted parse fields persist. Recovery is error return/logging, not a cross-store transaction; SDK retries connections/timeouts without a request idempotency key. SRC-1: `python-worker/services/parse_service.py`, `sdk/python/rem_memory/client.py`.

> // Step 7: Queue consolidation job (fire-and-forget)
> --- `go-api/internal/services/write_service.go`

> if err := s.qdrant.UpsertEpisode(ctx, episode.EpisodeID, embedding, payload); err != nil {
> 	return nil, fmt.Errorf("qdrant upsert: %w", err)
> }
> --- `go-api/internal/services/write_service.go`

#### RT-RTE-context-retrieve
Label: Selected context return

Endpoints: SDK/direct POST `/api/v1/retrieve` → embedding → agent-filtered Qdrant searches → PostgreSQL rehydration and Neo4j neighbors → code reranking → injection text and JSON return. Owner: Go retrieval service; host owns subsequent model invocation. State includes retained episodes, semantic payload if present and retrieval counts. SRC-1: `go-api/internal/services/retrieve_service.go`, `go-api/internal/db/qdrant/client.go`, `go-api/internal/db/neo4j/client.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Go HTTP response contains ranked episode results, semantic payload results, formatted injection prompt and latency. SDK typed conversion fails on nonempty Go episode or semantic results before returning RetrieveResult or its string.
- Later read-back: Each query reloads retained rows/vectors; asynchronous count increments can change future rankings.
- Delegated visibility: Embedding provider sees the normalized query. A direct HTTP consumer can receive selected raw episode text and semantic fact/confidence text in the server-built string, not all storage metadata. The SDK-mediated host handoff is blocked by typed conversion for nonempty ordinary Go results.
- Selection predicate: Query vector and agent_id filter select up to twice top_k candidates in each selected collection; expand one-hop neighbors of top three episode hits; rank episodes by 0.6 similarity, 0.25 recency and 0.15 capped retrieval bonus; cap episode count at top_k, itself at most 20. Semantic results are not subjected to that final episode truncation.
- Invalidation or expiry: Embedding cache expires after 24 hours; recency lowers score but does not delete content. No token-budget eviction is applied to the injection string here.
- Activation or effect: Formats context and attempts retrieval-count increments; downstream model compliance or improved decisions are unobserved.
- Evidence limits: Search and graph failures are logged and can yield partial output; model-compatible vector size and deployed store contents are not established. SDK non-null datetime requirements reject nonempty Go episode/semantic results; null semantic arrays independently fail iteration. No successful adapter delivery is observed.

Decision policy is symbolic ranking, not an answer oracle or candidate truth test. Go builds the string before HTTP return, but SDK result constructors run before RetrieveResult construction. Episode CreatedAt does not satisfy the SDK's created_at lookup; independently, SemanticResult omits created_at entirely and SDK SemanticMemory requires it. A direct HTTP caller can bypass these SDK conversions; that alternate path does not repair the shipped adapters. Ordinary requesting hosts choose when retrieval occurs; this is not independent unsolicited delivery. SRC-1: `sdk/python/rem_memory/client.py`, `sdk/python/rem_memory/types.py`, `go-api/internal/domain/episode.go`.

> Domain        string  `json:"domain"`
> EvidenceCount int     `json:"evidence_count"`
> Score         float64 `json:"score"`
> }
> --- `go-api/internal/domain/episode.go`

> fact_type: str  # "preference" | "rule" | "pattern" | "skill" | "fact"
> created_at: datetime
> score: Optional[float] = None  # if retrieved, has relevance score
> --- `sdk/python/rem_memory/types.py`

> finalScore := er.Score*0.6 + recencyScore*0.25 + retrievalBonus*0.15
> --- `go-api/internal/services/retrieve_service.go`

> fmt.Sprintf("[Learned Fact]: %s (confidence: %.0f%%)\n",
> 	sm.Fact, sm.Confidence*100),
> --- `go-api/internal/services/retrieve_service.go`

#### RT-RTE-worker-consolidation
Label: Scheduled semantic admission attempt

Endpoints: explicit Celery task dispatch, or beat → agent enumeration/heuristic → `run_consolidation_for_agent` → Go episode GET → engine clustering/model extraction → Python embedding → attempted Go semantic POST and episode PATCH. Owner: Celery/Python code; internal API key supplies Go principal, scoped agent listing follows that key's user rather than a global maintenance authority. SRC-1: `python-worker/workers/celery_app.py`, `python-worker/workers/tasks.py`, `go-api/internal/api/handlers/agents.go`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Celery result reports processed/created counts if completed; task failures request retry. Go write publication is separate and does not await this result.
- Later read-back: Task requests latest 50 episodes for the agent; durable semantic read-back is not completed by the inspected router, which has no accepting POST endpoint.
- Delegated visibility: Model receives truncated raw text and intent from selected lowercase-key episodes, not full histories; embedding service sees proposed fact text.
- Selection predicate: Scheduled heuristic total_episodes minus total_semantic_memories at least three; engine requires at least three per domain/intent cluster, two shared intent tokens relative to the seed, and supplies at most 15 members to compression. Go list handler ignores the task's consolidated=false parameter.
- Invalidation or expiry: Intended episode marking is an unregistered PATCH path; embedding cache TTL is 24 hours. Task retry limits/timeouts do not implement semantic rollback.
- Activation or effect: Model can produce candidates and task attempts persistence; registered API paths do not implement durable admission of those candidates.
- Evidence limits: No run; queue bridge, serialization and write-back gaps prevent crediting automatic durable semantic maintenance. Independent manual data loading is not evidence that this task works.

Trigger and admission: machine scheduling or explicit task call; computational clustering and model propose facts; nonempty fact filtering and numeric conversions govern candidate admission, followed by HTTP/storage success. Human per-content control is not wired in this task. No independent expected answer is supplied. Fixed guidance asks for durable preferences, patterns, errors, skills and recurring rules, skipping transient material; this is extraction under an unchanged method, not evidence of content-directed criticism of that method. Rejection occurs for insufficient clusters, empty/failed generation or failed HTTP. LLM/JSON errors inside the engine return no memories; other task exceptions request retry. Proposed persistent material is fact text, confidence/type/domain, source IDs and embedding; intended episode flags cannot be updated through the registered router. Detailed theory/learning assessments of semantic revision are not established here. SRC-1: `python-worker/services/consolidation/engine.py`, `python-worker/workers/tasks.py`, `go-api/internal/api/router.go`.

> This relies on a future Go API endpoint; errors are logged and ignored.
> --- `python-worker/workers/tasks.py`

> url = f"{GO_API_BASE_URL.rstrip('/')}/api/v1/semantic"
> --- `python-worker/workers/tasks.py`

> task_routes={
>     "consolidation.*": {"queue": "consolidation"},
> },
> --- `python-worker/workers/celery_app.py`

#### RT-RTE-direct-consolidation
Label: Direct candidate computation

Endpoints: caller POST Python `/consolidate` with arbitrary episode dictionaries and agent_id → shared engine → candidate list return. Owner: Python HTTP handler and model; caller owns any subsequent persistence. This is returning computation, not an autonomous memory admission loop. SRC-1: `python-worker/api/router.py`, `python-worker/api/handlers/consolidate.py`, `python-worker/services/consolidation/engine.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON semantic_memories array, or HTTP error; no database write in handler.
- Later read-back: inapplicable — this route retains no returned candidates; caller must arrange durable admission elsewhere.
- Delegated visibility: Model sees selected/truncated episode text, intent and labels; full source IDs are attached by code afterward.
- Selection predicate: Request must contain episodes and nonempty agent_id; engine domain/intent overlap thresholds and candidate fact presence govern returned candidates.
- Invalidation or expiry: inapplicable — request-local candidates have no retained lifetime assigned by this handler.
- Activation or effect: Consumes provider computation and returns proposed facts; no downstream action or semantic persistence is established.
- Evidence limits: Direct calls can supply correctly shaped lowercase-key inputs but do not resolve task scheduling or Go write-back gaps.

Operating mode: open request; caller supplies inputs, software clusters, model proposes facts and software filters, with no human veto step or answer oracle. Same fixed extraction guidance as the worker task; only candidate output, not method revision, is returned. Failure can return empty memories or HTTP 500, and there is no durable rollback requirement within this computation. The seed caller's unauthenticated Go fetch can fail before reaching this route, and the driver discards the returned candidate body even when computation succeeds. SRC-1: `scripts/seed_demo.py`.

> return ConsolidateResponse(semantic_memories=memories)
> --- `python-worker/api/handlers/consolidate.py`

#### RT-RTE-host-integration
Label: Host before and after hooks

Endpoints: LangChain load/save memory hooks or explicitly invoked AutoGen store helpers → SDK retrieve/write → host prompt/response lifecycle. Owner: external host for task progression; adapter for HTTP construction and string handoff. SRC-1: `sdk/python/rem_memory/integrations/langchain.py`, `sdk/python/rem_memory/integrations/autogen.py`, `sdk/python/rem_memory/client.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Intended LangChain memory-key mapping or AutoGen context string only after successful SDK conversion; nonempty ordinary Go episode/semantic results raise during typed conversion before that handoff. Saving returns after the write SDK call rather than returning a task result.
- Later read-back: Stored human/assistant or user/assistant turn descriptions are eligible for later query selection under the configured agent ID.
- Delegated visibility: Host injection text requires SDK success, which the nonempty Go result shapes prevent. On the separate save path REM receives serialized human/assistant exchange, not necessarily all host tools, outcomes or task state.
- Selection predicate: LangChain chooses input/question/human_input and response/output/text fields; retrieves five episodes with semantic inclusion. AutoGen host chooses when to call, query, top_k and semantic flag.
- Invalidation or expiry: LangChain clear is explicitly a no-op; no host-window trimming or retained deletion follows from that hook.
- Activation or effect: Software attempts context handoff and persists selected exchanges through the separate write mechanism; nonempty Go retrieval results fail before adapter context delivery. Actual prompt use, model compliance and successful integration startup remain unobserved.
- Evidence limits: Imported framework behavior is not frozen; SDK required datetime validation prevents nonempty Go episode/semantic handoff, independently of null-array iteration failure. Neither adapter catches that constructor failure or returns the server's raw string as fallback. Adapter existence does not establish a running enclosing agent.

Admission is the episode write mechanism above, not an independent human approval gate. The host initiates use; adapters serialize exchanges and default outcome to success without an independent outcome oracle. That default is not evidence of task success. SRC-1: `sdk/python/rem_memory/integrations/langchain.py`, `sdk/python/rem_memory/integrations/autogen.py`.

> content = f"Human: {human_input}\nAssistant: {ai_output}"
> --- `sdk/python/rem_memory/integrations/langchain.py`

> def clear(self) -> None:
>     """REM memories persist. This is intentional."""
>     return
> --- `sdk/python/rem_memory/integrations/langchain.py`

#### RT-RTE-key-admission
Label: API key admission and use

Endpoints: public register → user ID → public API-key creation by user ID → protected Go route group. Owner: Go handlers and middleware; user identity is attached as request local. Key material is symbolic capability-like bearer data; hashed key/prefix persist in PostgreSQL and positive prefix lookup in Redis. SRC-1: `go-api/internal/api/router.go`, `go-api/internal/api/handlers/auth.go`, `go-api/internal/api/middleware/auth.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Public key issuance returns newly generated bearer secret; middleware permits continuation or returns authentication error.
- Later read-back: Subsequent API requests read database key metadata or Redis prefix cache.
- Delegated visibility: Go handlers receive user_id in request locals; worker internal requests use configured INTERNAL_API_KEY if present.
- Selection predicate: Public creation requires an existing active user ID, without another possession proof in this handler; cold use checks prefix, active user and bcrypt, cached use accepts matching prefix.
- Invalidation or expiry: Cached positive identity lasts five minutes; key update replaces database hash/prefix without explicit old-prefix cache invalidation in the inspected issuer.
- Activation or effect: Changes which requests can pass Go middleware; does not itself enforce ownership of every requested episode/agent identifier.
- Evidence limits: Actual issued keys, adversarial requests and deployed network access are unobserved. Python direct routes do not pass this middleware.

Admission of a key changes API access capability: caller proposes a user ID, software admits an active existing user and generates a key; no independent human approval or answer oracle. Caller human identity remains unresolved. Errors reject issuance; replacing the stored key is available, but cache lifetime limits immediate revocation assumptions. Operating mode is open API request, not improvement experiment.

> if cachedUserID, ok, _ := redis.GetCache(ctx, cacheKey); ok && cachedUserID != "" {
> 	c.Locals("user_id", cachedUserID)
> 	return c.Next()
> }
> --- `go-api/internal/api/middleware/auth.go`

### Claims

#### RT-CLM-memory-loop
Label: Write consolidate retrieve claim

Claimed operation: automatic consolidation connects stored episodes to durable semantic context for later tasks. Source layer: doctrine/design, not observed operation. Implementation supplies pieces but the runtime gaps above prevent treating this as an established end-to-end loop. SRC-1: `README.md`.

> Persistent episodic storage, automatic consolidation, instant retrieval.
> --- `README.md`

> REM runs a simple but powerful loop: **Write → Consolidate → Retrieve**.
> --- `README.md`

### Evidenced absences

#### RT-ABS-worker-bridge
Label: Write queue consumer bridge

- implementation conclusion status: absent

Bounded absence: no inspected shipped consumer translates Go's `rem:jobs:consolidation` JSON list into Celery task dispatch. At the frozen revision, search across `go-api`, `python-worker`, `docs`, `README.md` and `Makefile` for `rem:jobs:consolidation`, blocking/list pop spellings, `consolidation.run` and `celery`, then complete publisher, scheduler, tasks and entry-point reads, found the list producer and named Celery task routes but no bridge. This supports absence of that source-level connection, not absence of an operator-added external consumer. SRC-1: `go-api/internal/db/redis/client.go`, `python-worker/workers/celery_app.py`, `python-worker/workers/tasks.py`, `Makefile`.

> return r.client.LPush(ctx, key, string(b)).Err()
> --- `go-api/internal/db/redis/client.go`

Conclusion prevented: a successful episode write cannot be credited as wired automatic Celery execution merely from these shipped components.

#### RT-ABS-writeback-routes
Label: Semantic write back route registration

- implementation conclusion status: absent

Bounded absence: complete inspection of Go `Setup` at the frozen revision shows GET-only semantic routing and no consolidated episode PATCH or episode DELETE. The worker proposes POST `/api/v1/semantic` and PATCH `/api/v1/episodes/{eid}/consolidated`; the benchmark reset helper proposes episode DELETE. Database update/helper methods do not register these endpoints. SRC-1: `go-api/internal/api/router.go`, `python-worker/workers/tasks.py`, `go-api/internal/db/postgres/episodes.go`, `benchmarks/adapters/rem_adapter.py`.

> // Semantic memories
> v1.Get("/semantic", handlers.ListSemantic(deps))
> --- `go-api/internal/api/router.go`

Conclusion supported: those exact HTTP consumers have no accepting shipped handler here. Conclusion prevented: durable semantic write-back, consolidated flag maintenance or benchmark memory reset cannot be assumed from their calling code. This does not deny direct administrative database access.

### Behavioral-authority paths

#### RT-BAP-context-injection
Label: Retrieved content to host prompt

Consumer: external agent model through host prompt construction. Channel: server-returned injection string; intended LangChain memory variable or AutoGen system-prefix helper is conditional on SDK conversion, which nonempty ordinary Go results fail. Force: natural-language context labelled relevant memories/learned facts; neither enforced instruction hierarchy nor reliable compliance. Horizon: later host task/session if retained state is successfully selected and supplied. Go's selected raw content and semantic fact/confidence are what the string consumer receives; source episode IDs and evidence counts are not included in the displayed learned-fact line. SRC-1: `go-api/internal/services/retrieve_service.go`, `sdk/python/rem_memory/integrations/langchain.py`, `sdk/python/rem_memory/integrations/autogen.py`.

> return {self.memory_key: result.injection_prompt}
> --- `sdk/python/rem_memory/integrations/langchain.py`

Server string construction is wired; SDK-mediated delivery is not established by that string's presence. Required datetime validation prevents the nonempty ordinary Go result handoff before either adapter can expose injection_prompt. A direct HTTP consumer can bypass that conversion boundary. Activation and benefit remain unobserved. Host-supplied content can reach a later model as text only if a consumer supplies it; this is not a grant of shell/tool authority and does not establish that malicious or mistaken content is followed. SRC-1: `sdk/python/rem_memory/client.py`, `sdk/python/rem_memory/types.py`.

## Annotations

none
