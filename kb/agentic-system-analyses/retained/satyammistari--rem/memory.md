---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "REM episode retention, semantic candidate generation and context read-back, including disconnected admission and withdrawal paths."
run-id: AAS-2026-10-14-rem-a81fdc774400-01
source-identity: https://github.com/satyammistari/REM
reviewed-boundary: "935e8be0a1fca5b23dbabfe16c48b562c1cd24cc"
---

# REM memory report

## Boundary and evidence

REM retains caller-supplied episode descriptions and offers query-selected context to a later host invocation. Its semantic extraction machinery can compute candidate facts, but the shipped worker-to-store connection is incomplete. Retained episodes, derived metadata, access feedback, numerical indexes, semantic candidates and intended semantic stores must therefore be assessed separately. The boundary is SRC-1 at the revision above, as registered in [boundary](boundary.md#source-register). Evidence is implementation inspection and attributed design only. No service, target test, provider call or benchmark was executed.

Included surfaces are Go episode admission, listing, retrieval and graph operations; Python parsing, embedding, both consolidation implementations and Celery maintenance; SDK and host adapters; seed, initialization and benchmark drivers. The enclosing host's task execution, provider internals and deployed store contents are outside the frozen evidence. This prevents downstream compliance, actual persistence, extraction accuracy and benefit conclusions, not source-level wiring conclusions. No source access gap was encountered.

The previous report's direct inspection coverage is preserved in the following table. This correction directly rechecked SDK types/client, both integration adapters, Go episode/semantic domain structs, episode/semantic handlers and the complete retrieval service; remaining direct-read entries describe carried inspection, not new reads in this attempt. Supplied runtime findings are identified separately rather than treated as fresh execution evidence. The inventory covers memory responsibilities, not every build or presentation file.

| Entry point or memory operation | Source paths in SRC-1 | Coverage and limits |
|---|---|---|
| SDK/direct episode POST; parse and sequential persistence | `go-api/internal/services/write_service.go`, `go-api/internal/api/handlers/episodes.go`, `go-api/internal/domain/episode.go`, `python-worker/services/parse_service.py` | Direct reads; annotations on [RT-OBJ-episode](runtime.md#rt-obj-episode), [RT-RTE-episode-write](runtime.md#rt-rte-episode-write); parts below |
| Query-selected episode and semantic context | `go-api/internal/services/retrieve_service.go`, `go-api/internal/db/qdrant/client.go`, `go-api/internal/db/neo4j/client.go`, `go-api/internal/api/handlers/retrieve.go` | Direct reads; [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve), [MEM-OBJ-retrieval-count](#mem-obj-retrieval-count), [MEM-OBJ-semantic-control](#mem-obj-semantic-control) |
| Episode and semantic listing / direct ID reload | `go-api/internal/db/postgres/episodes.go`, `go-api/internal/db/postgres/semantic.go`, `go-api/internal/api/handlers/semantic.go`, `sdk/python/rem_memory/client.py` | Direct reads; [MEM-RTE-memory-listing](#mem-rte-memory-listing); no hypothetical API caller counted as a deployed host |
| Redis publication, task/beat and write-back | `go-api/internal/db/redis/client.go`, `python-worker/workers/tasks.py`, `python-worker/workers/celery_app.py`, `go-api/internal/api/router.go`, `Makefile` | Direct reads; supplied [RT-ABS-worker-bridge](runtime.md#rt-abs-worker-bridge) and [RT-ABS-writeback-routes](runtime.md#rt-abs-writeback-routes); no end-to-end automatic semantic admission credited |
| Direct candidate computation | `python-worker/main.py`, `python-worker/api/router.py`, `python-worker/api/handlers/consolidate.py`, `python-worker/services/consolidation/engine.py` | Direct reads; [RT-RTE-direct-consolidation](runtime.md#rt-rte-direct-consolidation), [MEM-OBJ-semantic-candidate](#mem-obj-semantic-candidate) |
| Alternative clusterer/compressor and embedding batch operation | `python-worker/services/consolidation/clusterer.py`, `python-worker/services/consolidation/compressor.py`, `python-worker/services/embed_service.py` | Direct reads plus scoped caller search; [MEM-CMP-clusterer](#mem-cmp-clusterer), [MEM-CMP-compressor](#mem-cmp-compressor), [MEM-OBJ-memory-vector](#mem-obj-memory-vector). Library affordances are not additional wired maintenance routes |
| Host before/after hooks | `sdk/python/rem_memory/integrations/langchain.py`, `sdk/python/rem_memory/integrations/autogen.py`, `sdk/python/rem_memory/client.py` | Direct reads; annotation on [RT-RTE-host-integration](runtime.md#rt-rte-host-integration). External host invocation remains unobserved |
| Demo and store initialization | `scripts/seed_demo.py`, `scripts/init_qdrant.py`, `scripts/init_neo4j.py` | Direct reads of seed setup/consolidation and email-driver bodies, both initialization files; supplied boundary covers remaining demo strings. [MEM-OBJ-memory-vector](#mem-obj-memory-vector), [MEM-OBJ-memory-graph](#mem-obj-memory-graph). Schema creation is not retained experience |
| Evaluation and attempted reset | `benchmarks/adapters/rem_adapter.py`, `benchmarks/longmemeval.py`, `benchmarks/locomo.py`, `benchmarks/convomem.py`, `benchmarks/run_all.py` | Adapter/runner complete direct reads, scoring/run bodies of three evaluators; [MEM-RTE-benchmark-evaluation](#mem-rte-benchmark-evaluation). Sample definitions not exhaustively reread; no official-dataset coverage or scores inferred |
| Authentication, documentation and frontend claims | `go-api/internal/api/router.go`, `README.md`, `docs/quickstart.md`, `dashboard/src/app/page.tsx` | Router directly read; supplied runtime owns auth findings, supplied boundary owns presentation/documentation inspection. No frontend memory editor inferred; detailed UI and deployment behavior uninspected |

## Core ideas

1. **Content and access machinery are different retained parts.** Raw episode text enters the server-built context string; direct HTTP can expose it, but nonempty ordinary Go results fail SDK conversion before adapter prompt delivery. Parser metadata helps organize processing; vectors select IDs; temporal edges widen candidates; retrieval counts influence future ranking. Only the first is a raw trace, and a count is not a learned explanatory fact. See [MEM-OBJ-raw-content](#mem-obj-raw-content), [MEM-OBJ-episode-interpretation](#mem-obj-episode-interpretation), [MEM-OBJ-retrieval-count](#mem-obj-retrieval-count).
2. **Extraction is not durable admission.** The active engine asks for reusable facts and attaches source IDs, but its caller attempts unregistered write-back endpoints. Direct Python calls return candidates without storing them. Independently supplied lowercase episode dictionaries are a counterexample to a blanket claim that extraction cannot run; they do not repair persistence. See [RT-RTE-worker-consolidation](runtime.md#rt-rte-worker-consolidation), [RT-RTE-direct-consolidation](runtime.md#rt-rte-direct-consolidation).
3. **Returned confidence is not retained justification.** The model receives a bounded text sample, while attached evidence counts cover the full cluster. Later learned-fact text omits even those source links and counts. Source truth and task success are not independently verified by this pipeline. See [MEM-OBJ-semantic-candidate](#mem-obj-semantic-candidate), [MEM-OBJ-semantic-lineage](#mem-obj-semantic-lineage), [RT-BAP-context-injection](runtime.md#rt-bap-context-injection).
4. **Retrieval is host-requested context construction.** Count limits govern selected episodes, not the total prompt's tokens. A host may load this material into a new invocation; REM does not itself trim the host's accumulated window or guarantee that the host uses the supplied string. See [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve).

## Shared records

### Components

#### MEM-CMP-clusterer
Label: Clusterer alternative implementation

Source-native identity: `Clusterer` in SRC-1, `python-worker/services/consolidation/clusterer.py`. Symbolic Python rules in a static source file, not provider weights or retained experience. It groups by domain, extracts words from intent plus raw content, admits a shared keyword, requires two episodes by default and chunks at twenty. This differs from the active engine's three-episode/two-intent-token rules in [RT-RTE-worker-consolidation](runtime.md#rt-rte-worker-consolidation); it is not another name for that route's selector. No counterpart in supplied component records. Repository search for `Clusterer` and imports in worker entry points/tasks found its definition but no shipped caller. The default active route must not inherit its thresholds. This supports a library capability, not observed use.

> MIN_CLUSTER_SIZE = 2
> --- `python-worker/services/consolidation/clusterer.py`

> if kw_i & kw_j:  # non-empty intersection
> --- `python-worker/services/consolidation/clusterer.py`

#### MEM-CMP-compressor
Label: Compressor alternative implementation

Source-native identity: `Compressor` in SRC-1, `python-worker/services/consolidation/compressor.py`. Local natural-language system/user instructions plus symbolic validation code are stored in the source file. Its remote distributed-parametric chat model defaults to mutable alias `gpt-4o`; exact provider revision and weights are opaque and unpinned, and no local parameter update is implemented. It is a separate caller from [RT-CMP-consolidation-engine](runtime.md#rt-cmp-consolidation-engine), not a duplicate of the engine instance: search for `Compressor` and imports across worker source found only this implementation and descriptive references, while main/tasks instantiate the engine.

The callable capability converts supplied clusters to one to three requested facts using 300-character previews. It returns `content`, normalized fact type/outcome, clamped scores and clipped text, with no IDs or persistence. These checks are not implemented by the active engine simply because both perform compression. Generic library caller authorship, initialization and later use are unresolved; no shipped durable consumer of these alternate outputs was found. No per-content human approval or expected-answer oracle is implemented in this callable. It is an open computation, not a bounded improvement experiment. Model/API exceptions raise; malformed JSON and empty content reject outputs. Static guidance persists in source, not a reasoned history of individual facts.

> "content": content[:300],
> --- `python-worker/services/consolidation/compressor.py`

> "content_preview": (ep.get("raw_content") or "")[:300],
> --- `python-worker/services/consolidation/compressor.py`

### Operative objects

#### MEM-OBJ-raw-content
Label: RawContent retained trace
Part of: [RT-OBJ-episode](runtime.md#rt-obj-episode)

Source-native identity: `Episode.RawContent` / SQL `raw_content`, natural-language content in PostgreSQL. It is caller text, not a reconstructed execution trace. LangChain/AutoGen serialize human/user and assistant strings; seed and benchmarks supply authored examples; a generic API caller's original authorship and relation to real behavior remain unresolved. Go preserves the admitted content after handler trimming. The parser consumes the full description during writing, retrieval displays it, and intended consolidation sees only a prefix. Later model authority is contextual text through [RT-BAP-context-injection](runtime.md#rt-bap-context-injection), not execution privilege. SRC-1: `go-api/internal/domain/episode.go`, `go-api/internal/api/handlers/episodes.go`, `go-api/internal/services/retrieve_service.go`, both SDK integration files.

> RawContent:      req.Content,
> --- `go-api/internal/domain/episode.go`

#### MEM-OBJ-episode-interpretation
Label: Episode parsed interpretation
Part of: [RT-OBJ-episode](runtime.md#rt-obj-episode)

Source-native parts: `Intent`, `ParsedEntities`, `Domain`, `EmotionSignal`, `ImportanceScore`; PostgreSQL text, JSON and numeric fields. Intent/domain/emotion labels include model-interpreted language; entities and scores have symbolic field-level handling. The fixed parser requests extraction, not replacement of the raw description; defaults survive failure. The Go service accepts nonempty interpretation fields, nonnil entities and an importance score in range. Thus software/model admission differs from caller authorship and does not supply content approval by a human. Domain/intent affect intended clustering; domain labels enter the displayed context; the inspected ranking does not use importance or emotion. This is automatic trace-derived metadata with a later selector/display consumer, not evidence of improved task capacity. SRC-1: `python-worker/services/parse_service.py`, `go-api/internal/services/write_service.go`, `python-worker/services/consolidation/engine.py`, `go-api/internal/services/retrieve_service.go`.

> if parsed.ImportanceScore >= 0 && parsed.ImportanceScore <= 1 {
> 	episode.ImportanceScore = parsed.ImportanceScore
> }
> --- `go-api/internal/services/write_service.go`

#### MEM-OBJ-retrieval-count
Label: RetrievalCount access feedback
Part of: [RT-OBJ-episode](runtime.md#rt-obj-episode)

Source-native identity: `RetrievalCount` and `LastRetrievedAt`, symbolic PostgreSQL access metadata, separate from episode claims and parse judgments. Code asynchronously increments counts for selected results; future retrieval computes a capped bonus from the retained count. This is a wired use-fed durable update whose consumer is the ranking function. It is not model training, semantic abstraction, or an independent outcome assessment. Updates may fail silently; no actual feedback effect is observed. SRC-1: `go-api/internal/db/postgres/episodes.go`, `go-api/internal/services/retrieve_service.go`; closest supplied route [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve).

> SET retrieval_count=retrieval_count+1,
>     last_retrieved_at=NOW()
> --- `go-api/internal/db/postgres/episodes.go`

#### MEM-OBJ-memory-vector
Label: Episode and semantic search vectors

Source-native identities: Qdrant point vectors in `episodes` and `semantic_memories`, and Redis `rem:embed:` cached vectors. These are dense numerical/distributed representations, not readable natural-language summaries; IDs and payload fields are separate symbolic access material. Episode vectors derive from normalized caller content through [RT-CMP-embed-service](runtime.md#rt-cmp-embed-service); intended semantic vectors derive from generated fact text. Storage is Qdrant and Redis, not changed provider weights. Episode lineage is wired through the write service; initial semantic vector admission is not established by the registered HTTP route. Search operations consume these vectors for similarity, not as model instructions. Cached query embeddings can serve later calls for 24 hours; query text is not thereby an episode.

Distinct from the model component and [RT-OBJ-episode](runtime.md#rt-obj-episode): this record owns numerical selection state rather than weights or the SQL envelope. SRC-1: `python-worker/services/embed_service.py`, `go-api/internal/db/redis/client.go`, `go-api/internal/db/qdrant/client.go`, `go-api/internal/services/write_service.go`, `python-worker/workers/tasks.py`. The batch embed helper is callable and caches results but is not registered as another HTTP route in `python-worker/api/router.py`; main/tasks use the single-text path.

Go creates both collections at 1536 dimensions; the provider request omits an explicit dimensions parameter. The standalone initializer instead defaults to `rem_episodes` and a separately configurable model/dimension map. It does not configure the Go collection names or Python model. This additional setup path is not evidence that the advertised setup resolves vector compatibility. Actual deployed contents and dimensions remain uninspected. SRC-1: `scripts/init_qdrant.py`.

> COLLECTION = os.getenv("QDRANT_COLLECTION", "rem_episodes")
> --- `scripts/init_qdrant.py`

#### MEM-OBJ-memory-graph
Label: Temporal and compression graph

Source-native identities: Neo4j `Episode` / `SemanticMemory` nodes, `FOLLOWED_BY` and `COMPRESSED_INTO` edges. Symbolic identity/topology stored in Neo4j, not raw episode text. The active write path creates episode nodes and best-effort predecessor edges; retrieval requests undirected one-hop temporal neighbors. Semantic-node/link and GraphService methods expose capabilities without a registered semantic admission caller. Distinct from [RT-OBJ-episode](runtime.md#rt-obj-episode)'s SQL envelope; its graph reference is the closest supplied overlap, not a second SQL object. SRC-1: `go-api/internal/db/neo4j/client.go`, `go-api/internal/services/graph_service.go`, `go-api/internal/services/write_service.go`.

The display method executes a graph query but returns empty nodes/edges even with a result; it cannot substantiate a live displayed provenance graph. The standalone initializer uses camelCase properties such as `episodeId`, while Go uses `episode_id`; those schema paths are not interchangeable. Actual semantic graph population remains unknown, without suppressing the known episode transformation and temporal consumer. SRC-1: `scripts/init_neo4j.py`.

> MERGE (a)-[:FOLLOWED_BY]->(b)
> --- `go-api/internal/db/neo4j/client.go`

> // Minimal graph: weâ€™ll expand/normalize in Day 3+.
> return &GraphData{Nodes: []GraphNode{}, Edges: []GraphEdge{}}, nil
> --- `go-api/internal/db/neo4j/client.go`

#### MEM-OBJ-semantic-candidate
Label: Semantic candidate fact

Source-native identity: engine output dictionaries' `fact`, `confidence`, `fact_type`, `domain`. Natural-language proposed fact plus symbolic scores/labels in request-local Python objects; the direct handler returns JSON. No durable substrate is established for this candidate on the shipped route. Closest supplied records [RT-RTE-worker-consolidation](runtime.md#rt-rte-worker-consolidation) and [RT-RTE-direct-consolidation](runtime.md#rt-rte-direct-consolidation) are producer routes, not duplicate objects. It is also distinct from [MEM-OBJ-semantic-control](#mem-obj-semantic-control)'s intended stored row.

SRC-1: `python-worker/services/consolidation/engine.py`. The engine groups by lowercased domain and seed-intent token overlap, then uses at most fifteen episodes and 500 content characters each. Prompt text requests one to five facts of at most 200 characters; actual postprocessing only skips empty facts and converts confidence numerically, without enforcing length, enum membership, confidence bounds or independent truth. JSON/model errors return an empty list inside the protected request/parse block; malformed items after that block can still raise. This contrasts with the separate compressor's stricter checks.

> limited_eps = episodes[: self.max_cluster_size]
> --- `python-worker/services/consolidation/engine.py`

> JSON only, no explanation.
> --- `python-worker/services/consolidation/engine.py`

Reasons are neither requested nor retained as a candidate field. Candidate authority is a proposal to the task's storage caller, not yet knowledge consumed by another agent. Original trace origin is whatever the caller supplied; adapter labels do not authenticate it.

#### MEM-OBJ-semantic-lineage
Label: Semantic source episode metadata

Source-native identity: `source_episode_ids` / `evidence_count` attached by the active engine and columns in the intended SQL representation. Symbolic lists/counts, request-local first and PostgreSQL-capable later; no shipped durable admission established. Distinct from candidate fact content: this part is computed by code after model generation, not a model rationale. It overlaps the output of [RT-RTE-worker-consolidation](runtime.md#rt-rte-worker-consolidation), without duplicating the route.

The list covers the full cluster, not just the bounded prefix shown to the model. Go's PascalCase envelope can also produce empty IDs at this lowercase lookup. Retrieval's semantic result omits source IDs; the injection line omits evidence count too. The intended raw-to-derived-to-host chain therefore loses source-specific support at the actual prompt consumer, even if semantic storage is populated externally. GET listing can expose SQL source IDs to a direct HTTP caller, but the SDK `SemanticMemory` conversion does not carry them. SRC-1: `python-worker/services/consolidation/engine.py`, `python-worker/workers/tasks.py`, `go-api/internal/domain/episode.go`, `go-api/internal/domain/semantic_memory.go`, `sdk/python/rem_memory/client.py`, `go-api/internal/services/retrieve_service.go`.

> source_ids = [str(ep.get("episode_id") or "") for ep in episodes]
> --- `python-worker/services/consolidation/engine.py`

#### MEM-OBJ-semantic-control
Label: SemanticMemory retained representation

Source-native identity: PostgreSQL `SemanticMemory` / `semantic_memories`, including fact text, confidence, provenance and `active`, `contradicted_by`, `superseded` fields. Natural-language fact is mixed with symbolic access/lifecycle fields. Separate Qdrant payloads supply the actual fact text to the retrieval service. No corresponding supplied object exists; [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve) and [RT-ABS-writeback-routes](runtime.md#rt-abs-writeback-routes) describe consumer and missing admission respectively.

SRC-1: `go-api/internal/domain/semantic_memory.go`, `go-api/internal/db/postgres/semantic.go`, `go-api/internal/db/qdrant/client.go`, `go-api/internal/services/retrieve_service.go`. SQL insert/upsert library capabilities are not proof of the worker's admitted candidates or a synchronized semantic population. Initial contents, administrative control and actual provenance are uninspected. Known read transformations remain assessable: listing filters only agent ID; active-only filtering occurs in statistics, not listing. Retrieval reads Qdrant payload directly and its search filter contains only agent ID, not active/superseded/contradicted status. Changing a SQL lifecycle field alone is therefore not a wired withdrawal from the prompt consumer.

> WHERE agent_id = $1 AND active = TRUE
> --- `go-api/internal/db/postgres/semantic.go`

That predicate belongs to statistics. Contrast the listing query:

> FROM semantic_memories
> WHERE agent_id = $1
> ORDER BY created_at DESC
> --- `go-api/internal/db/postgres/semantic.go`

### Routes

#### MEM-RTE-memory-listing
Label: Memory listing and reload

Endpoint/progression: SDK or direct caller → protected Go episode list/get or semantic list → SQL rows → JSON → optional SDK conversion. Go handlers/database own selection; caller owns any later prompt use. Distinct from [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve): these paths reload by identity/chronology rather than query-vector ranking. Worker and reset clients overlap the callers of [RT-RTE-worker-consolidation](runtime.md#rt-rte-worker-consolidation) and [MEM-RTE-benchmark-evaluation](#mem-rte-benchmark-evaluation), not duplicate routes. SRC-1: `go-api/internal/api/handlers/episodes.go`, `go-api/internal/api/handlers/semantic.go`, `go-api/internal/db/postgres/episodes.go`, `go-api/internal/db/postgres/semantic.go`, `sdk/python/rem_memory/client.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Direct HTTP returns an episode page plus total/limit/offset, an episode by ID, or semantic items plus limit. Nonempty ordinary Go episode/semantic lists fail SDK typed conversion rather than returning defaulted objects; empty compatible arrays can return empty typed lists.
- Later read-back: Direct HTTP reload exposes SQL retained content to a later caller; task fetch is a concrete supplied consumer. SDK list_episodes and get_semantic_memory reject nonempty Go lists before delivering typed material, while arbitrary listing-to-prompt use is only an exposed capability.
- Delegated visibility: Direct HTTP exposes exported fields, including raw text and SQL semantic source IDs. Go emits PascalCase CreatedAt; SDK looks up created_at, supplies None and fails the required datetime constructor for both EpisodeResult and SemanticMemory. Defaults for other fields do not rescue delivery.
- Selection predicate: Agent ID and descending creation time, episode pagination capped at 100; direct episode ID lookup; semantic limit resets to 50 outside 1–200. Domain/outcome/consolidated query parameters supplied by clients do not filter these handlers.
- Invalidation or expiry: No expiry assigned by these reads; semantic listing does not filter active or superseded state.
- Activation or effect: Returns retained material, without evidence that a caller acts on it; no retrieval-count increment on ordinary list/get.
- Evidence limits: Static source; no actual SQL population or external caller behavior inspected. Typed reload failure is a source-level finding, not an observed exception. Direct HTTP remains available; SDK/host delivery cannot be assumed merely from a listing method.

Both constructors require non-null timestamps. The SDK supplies the lowercase lookup in retrieval and listing before returning typed results. SRC-1: `sdk/python/rem_memory/types.py`, `sdk/python/rem_memory/client.py`, `go-api/internal/domain/episode.go`, `go-api/internal/domain/semantic_memory.go`.

> consolidated: bool
> created_at: datetime
> score: float  # retrieval relevance score
> --- `sdk/python/rem_memory/types.py`

> fact_type: str  # "preference" | "rule" | "pattern" | "skill" | "fact"
> created_at: datetime
> score: Optional[float] = None  # if retrieved, has relevance score
> --- `sdk/python/rem_memory/types.py`

> created_at=ep.get("created_at"),
> score=0.0,
> retrieval_source="episodes",
> --- `sdk/python/rem_memory/client.py`

> return c.JSON(ep)
> --- `go-api/internal/api/handlers/episodes.go`

#### MEM-RTE-benchmark-evaluation
Label: Benchmark evaluation and reset

Endpoint/progression: CLI runner → selected benchmark → adapter episode POSTs → retrieval response/injection string → reference comparison → result JSON → best-effort reset; combined runner aggregates summaries. Python drivers own sequence and scoring; Go owns ordinary admission/retrieval. No counterpart in supplied route declarations; [RT-RTE-episode-write](runtime.md#rt-rte-episode-write) and [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve) are invoked subroutes, not this evaluator. SRC-1: `benchmarks/run_all.py`, `benchmarks/adapters/rem_adapter.py`, `benchmarks/longmemeval.py`, `benchmarks/locomo.py`, `benchmarks/convomem.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Summary dictionaries, terminal reports and per-benchmark JSON; combined runner writes combined JSON.
- Later read-back: Retrieval consumes episodes written earlier in the driver; combined runner reads returned summaries. No inspected consumer feeds score JSON back into memory admission, prompt revision or model training.
- Delegated visibility: Scorers see injection strings or response fields; optional LongMemEval model judge sees question, expected answer and retrieved context, not an independently generated host answer.
- Selection predicate: CLI chooses suite; supplied/default sample sets provide reference answers. Query requests top five. LongMemEval/LoCoMo use answer containment and set-token F1; ConvoMem uses injection containment and snippet precision.
- Invalidation or expiry: Reset tries list/delete and suppresses exceptions; Go has no registered DELETE and the helper looks for lowercase IDs, so fresh memory per conversation is not established. Random suite agent IDs do not isolate ConvoMem samples sharing that suite ID.
- Activation or effect: Adds synthetic episodes and access-count feedback, writes evaluation reports, attempts cleanup; no score-based content veto or revision is implemented.
- Evidence limits: No runs or result files admitted. The supplied runtime's migration and benchmark-driver inspection additionally withholds fresh-install readiness and default benchmark executability: the unapplied SQL migration creates the same episode trigger twice and fails transactionally before Go listens; default benchmarks generate agent IDs without creating rows required by the episode foreign key. Prepared migration state or caller-supplied registered agents are different conditions, not demonstrated setup. Adapter omits include_semantic (Go bool defaults false); this tests episode context rather than proving semantic consolidation. ConvoMem reads memories while Go returns episodes, preventing its precision calculation from assessing those snippets on this response shape.

Operating mode: bounded source-authored evaluation examples, with answers provided by the sample dictionaries. Optional `gpt-4o-mini` judge applies a supplied answer, not an oracle created by confidence alone. Source-authored references are an evaluation oracle in this driver, not a production write gate. Adapter software pads short content and clips at 10000, while Go rejects length exactly 10000; metadata session labels do not become a stored field through `NewEpisode`. No per-content human approval occurs during the driver; prior sample authorship is separate. Failure raises on write/retrieve or is suppressed during reset. No automatic rollback or quality-driven improvement follows the scores.

> prediction = retrieve_prompt(s["question"], agent_id=agent_id, top_k=5)
> --- `benchmarks/longmemeval.py`

> memories  = result.get("memories", [])
> --- `benchmarks/convomem.py`

### Claims

none declared in this member

### Evidenced absences

#### MEM-ABS-memory-withdrawal
Label: Consumer effective memory withdrawal

- implementation conclusion status: absent

Bounded absence at SRC-1's frozen revision: no shipped consumer-effective episode deletion or semantic contradiction/supersession maintenance loop was found. Search over `go-api`, `python-worker`, `sdk`, `benchmarks`, `scripts`, `docs`, `README.md` and `Makefile` for `contradict`, `supersed`, `delete`, `reset`, semantic insert/upsert and consolidation update names, followed by complete router, semantic DB, retrieval service, Qdrant client and task reads, found schema flags, attempted reset, unused storage capabilities and the known missing HTTP endpoints, but no path coordinating withdrawal through later retrieval. Closest supplied absence [RT-ABS-writeback-routes](runtime.md#rt-abs-writeback-routes) concerns exact endpoint registration; this record additionally concerns lifecycle flags at their later consumers. Possible overlap is intentional and not a proposed replacement.

SRC-1: `go-api/internal/api/router.go`, `go-api/internal/db/postgres/semantic.go`, `go-api/internal/db/qdrant/client.go`, `go-api/internal/services/retrieve_service.go`, `benchmarks/adapters/rem_adapter.py`. Direct administrative mutation and operator-added services are outside this absence. It supports a source-level lifecycle gap, not a claim that stored data can never be removed externally.

> """Delete all episodes for an agent (best-effort)."""
> --- `benchmarks/adapters/rem_adapter.py`

The helper's intent is not implementation of its accepting endpoint. Semantic lifecycle fields likewise do not prove contradiction detection or prompt exclusion.

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-episode](runtime.md#rt-obj-episode)

Memory parts are [MEM-OBJ-raw-content](#mem-obj-raw-content), [MEM-OBJ-episode-interpretation](#mem-obj-episode-interpretation) and [MEM-OBJ-retrieval-count](#mem-obj-retrieval-count). Symbolic IDs, timestamps, consolidation flags and outcome remain envelope metadata. Outcome is caller-provided (default unknown; host adapters commonly use success), not measured task success. Request metadata is not copied into `NewEpisode`; a benchmark session in metadata is not a persisted session ID. SRC-1: `go-api/internal/domain/episode.go`, `sdk/python/rem_memory/integrations/langchain.py`, `benchmarks/adapters/rem_adapter.py`.

#### On [RT-RTE-episode-write](runtime.md#rt-rte-episode-write)

Acquisition retains trimmed caller prose alongside separately derived fields. Caller-origin admission is structural; parser output supplies interpretation rather than approval. The write's physical store sequence has no cross-store rollback, so visible SQL history may outlive a failed later store operation. The raw-to-parser-to-metadata transformation is wired even though downstream semantic admission is not. SRC-1: `go-api/internal/api/handlers/episodes.go`, `go-api/internal/services/write_service.go`; supporting passages in the part records and supplied route.

#### On [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve)

Read-back trigger is a host query, not a memory-initiated push. Go builds the string before returning HTTP JSON. SDK retrieve constructs EpisodeResult and SemanticMemory before RetrieveResult: PascalCase episode CreatedAt fails the lowercase created_at lookup, and Go SemanticResult has no timestamp at all. Either nonempty result kind therefore causes required datetime validation to fail before injection_prompt reaches LangChain or AutoGen. A null semantic array independently fails SDK iteration. Direct HTTP can bypass these conversions; server string construction is not adapter delivery. SRC-1: `sdk/python/rem_memory/client.py`, `sdk/python/rem_memory/types.py`, `go-api/internal/domain/episode.go`; supporting passages in [MEM-RTE-memory-listing](#mem-rte-memory-listing) and the supplied runtime route. Selector inputs are query vector, agent ID, retained vectors, graph IDs, timestamps and retrieval counts. Episode candidate budget is twice top_k plus graph neighbors; final episode count is top_k capped at twenty. Semantic budget is twice top_k, separately, without final episode truncation. The builder includes full raw descriptions; neither token nor aggregate character budget governs the resulting injection string. Selected material remains available in stores when not selected; later server queries or direct HTTP list/get can reload it, without establishing successful SDK typed reload. No host conversation compaction, verbatim-tail checkpoint or replacement of current host state is wired here. SRC-1: `go-api/internal/services/retrieve_service.go`, `go-api/internal/db/qdrant/client.go`.

Semantic read-back uses payload text, not a PostgreSQL lifecycle recheck. Integer Qdrant payload values decode as int64 but retrieval asserts float64 for evidence_count, so a count inserted as an integer through the client can display as zero. This is another reason not to infer support from the response label. SRC-1: `go-api/internal/db/qdrant/client.go`, `go-api/internal/services/retrieve_service.go`.

> evidence, _ := payload["evidence_count"].(float64)
> --- `go-api/internal/services/retrieve_service.go`

#### On [RT-RTE-worker-consolidation](runtime.md#rt-rte-worker-consolidation)

The intended trace-fed chain is SQL episodes → cluster sample → candidate fact plus source metadata → embedded fact → attempted semantic storage → later semantic search → host context. The chain breaks before admitted semantic persistence on the registered API. The engine does not retrieve existing semantic memories, compare contradictions or revise its extraction instructions; it generates from episode inputs. Even if storage were added, marking sources consolidated is not deletion, and the current episode list ignores consolidated=false. Raw evidence could remain query-reachable, but no displayed-fact provenance-following route is supplied. SRC-1: `python-worker/workers/tasks.py`, `python-worker/services/consolidation/engine.py`, `go-api/internal/api/handlers/episodes.go`, `go-api/internal/api/router.go`.

#### On [RT-RTE-direct-consolidation](runtime.md#rt-rte-direct-consolidation)

Selected inputs are isolated in a separate model request, with only candidate dictionaries returned: a bounded computation frame, not a host context-window summary checkpoint. Lowercase caller inputs can exercise known extraction logic without Go episode serialization; the seed's direct request still neither authenticates its preceding fetch nor persists returned facts. No alternative durable checkpoint form is established by this route. SRC-1: `python-worker/api/handlers/consolidate.py`, `python-worker/services/consolidation/engine.py`, `scripts/seed_demo.py`.

#### On [RT-RTE-host-integration](runtime.md#rt-rte-host-integration)

LangChain's before hook requests five episodes plus semantic facts; after hook serializes human/assistant content with outcome success. AutoGen exposes explicit get/save/system-prefix helpers, not an inspected automatic registration into an agent event loop. Neither provides an independent outcome test. LangChain clear does not withdraw retained data. Both before-hook paths first require successful SDK typed retrieval, which nonempty ordinary Go episode or semantic results fail. Neither catches that constructor failure or falls back to the raw HTTP string. AutoGen's formatter, reached only after a successful typed result with an empty injection string, uses at most three episode intents rather than full raw text, and semantic fact/confidence or joined facts; it otherwise prefers the server string. Those formatting branches are conditional capabilities, not alternate delivery around the constructor failure. SRC-1: both SDK integration files; no deployed hook execution observed.

#### On [RT-BAP-context-injection](runtime.md#rt-bap-context-injection)

Memory authority at a direct HTTP prompt consumer is natural-language context, including unverified caller claims or derived candidates if externally populated. SDK-mediated authority is not reached for nonempty ordinary Go results because typed conversion fails before adapter delivery. Neither provenance pointers nor derivation reasons accompany displayed learned facts. Host system-prompt placement is an SDK instruction/AutoGen affordance, not an enforced privilege of stored text. Delivery does not establish changed behavior or improved capacity. SRC-1: `go-api/internal/services/retrieve_service.go`, `sdk/python/rem_memory/client.py`, `sdk/python/rem_memory/integrations/autogen.py`.

## Write side

Admission control is mechanism-specific. Open API callers choose episode content; Go gates structure and dependencies, and the parser automatically supplies metadata. Human authorship or approval of generic requests is unresolved. Adapters choose which exchange fields to serialize; seed and benchmark authors supply synthetic text. These are raw retention and metadata derivation, not evidence that the system evaluated its own performance. References: [RT-RTE-episode-write](runtime.md#rt-rte-episode-write), [MEM-OBJ-episode-interpretation](#mem-obj-episode-interpretation), [MEM-RTE-benchmark-evaluation](#mem-rte-benchmark-evaluation).

Semantic candidate admission is software clustering plus model extraction and minimal output filtering, followed by attempted HTTP storage. Fixed guidance asks for recurring preferences, errors, skills and rules while skipping transient events. It does not ask for retained derivation reasons or a critique of the method. A candidate may contain a rule, but no actual candidate contents or content-directed criticism are supplied, so a general theory-builder classification is not established from the label semantic memory. Separate compressor validation is a different capability, not an active safeguard. References: [MEM-OBJ-semantic-candidate](#mem-obj-semantic-candidate), [MEM-CMP-compressor](#mem-cmp-compressor), [RT-RTE-worker-consolidation](runtime.md#rt-rte-worker-consolidation).

Curation limits are concrete: parsing enriches metadata; clustering filters proposed inputs; compression requests abstraction; retrieval reranks access. Neither rejection of malformed output nor an evaluator score supplies warranted truth. The known durable use-fed behavioral update is the retrieval count, which alters later selection without assessing success. Semantic trace-fed abstraction has an intended later consumer but no completed durable admission path. Model parameters remain provider-owned and unmodified by inspected REM operations. References: [MEM-OBJ-retrieval-count](#mem-obj-retrieval-count), [RT-CMP-consolidation-engine](runtime.md#rt-cmp-consolidation-engine), [MEM-OBJ-semantic-control](#mem-obj-semantic-control).

Maintenance/rejection does not establish withdrawal: task errors may retry; empty clusters/candidates produce nothing; no semantic replacement transaction, contradiction test or consumer-effective reset is wired. SQL lifecycle flags, consolidation marking helpers and graph link helpers must remain capabilities/representations rather than credited maintenance. Actual externally initialized semantic state and its human/software control are unknown. References: [MEM-ABS-memory-withdrawal](#mem-abs-memory-withdrawal), [MEM-OBJ-semantic-control](#mem-obj-semantic-control).

## Read-back

The main route is requested retrieval with automatic selection inside that request, not independent unsolicited supply. The server returns selected raw text and, if present, semantic payload facts/confidence in its context string to direct HTTP callers. SDK constructors reject nonempty ordinary Go results before returning that string to an adapter. Numerical indexes and graph links select context but are not themselves displayed reasons. Count feedback affects later ranking; recency decay does not erase old records. Listing/get is an alternative reload channel, with supplied worker and benchmark consumers as well as a generic SDK affordance. References: [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve), [MEM-RTE-memory-listing](#mem-rte-memory-listing).

The host adapters expose before/after reuse hooks, but nonempty ordinary Go results fail SDK typed conversion before the before-hook context handoff; their separate save hooks are not invalidated by that failure. Framework invocation and downstream model use are also unobserved. The window receives memory by value, not a dereferenceable heap pointer; retained SQL source IDs do not let the host model follow provenance unless a host adds a tool. Extraction isolates selected history in a separate request and returns proposed facts; it does not evict a host window, promise a summary checkpoint or preserve a verbatim tail. Count/character limits are source-supported, but host token fit is unknown. References: [RT-RTE-host-integration](runtime.md#rt-rte-host-integration), [RT-RTE-direct-consolidation](runtime.md#rt-rte-direct-consolidation), [MEM-OBJ-semantic-lineage](#mem-obj-semantic-lineage).

Evaluator JSON is retained outside the memory stores for reporting; the combined runner consumes summaries, not per-example criticisms to change production memory. A score report is therefore not a memory revision route. Cleanup attempts neither reset Qdrant/Neo4j nor reach a registered episode deletion handler. Reference: [MEM-RTE-benchmark-evaluation](#mem-rte-benchmark-evaluation).

## Integration issues

- No supplied fact is withdrawn. Fresh reads confirm the queue, serialization and missing write-back limits of [RT-ABS-worker-bridge](runtime.md#rt-abs-worker-bridge), [RT-ABS-writeback-routes](runtime.md#rt-abs-writeback-routes), [RT-RTE-worker-consolidation](runtime.md#rt-rte-worker-consolidation). Direct lowercase-input extraction remains a material alternative, not a repair of those connections.
- Possible overlap: [MEM-ABS-memory-withdrawal](#mem-abs-memory-withdrawal) includes the missing DELETE observation of [RT-ABS-writeback-routes](runtime.md#rt-abs-writeback-routes), but adds lifecycle filtering and lack of consumer-effective withdrawal. Retain or connect these findings; do not treat them as contradictory or automatically supersede one.
- Envelope parts [MEM-OBJ-raw-content](#mem-obj-raw-content), [MEM-OBJ-episode-interpretation](#mem-obj-episode-interpretation), [MEM-OBJ-retrieval-count](#mem-obj-retrieval-count) explicitly belong to [RT-OBJ-episode](runtime.md#rt-obj-episode). Numerical and graph records overlap that envelope's mentions of derived stores but are distinct artifacts, with different consumers and admission failure boundaries.
- Corrected compatibility consequences: [MEM-RTE-memory-listing](#mem-rte-memory-listing) now identifies failed typed reload, not defaulted/lossy objects. Annotations on [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve), [RT-RTE-host-integration](runtime.md#rt-rte-host-integration) and [RT-BAP-context-injection](runtime.md#rt-bap-context-injection) distinguish server strings/direct HTTP from blocked SDK delivery. SRC-1 `sdk/python/rem_memory/types.py` and `sdk/python/rem_memory/client.py` require timestamps missing from the SDK lookups or response shape. This agrees with the corrected supplied runtime, superseding the older fragments in the refusal, not changing peer records. The retrieval annotation also retains int64/float64 evidence-count loss. Actual exceptions, stored contents and displayed values remain unobserved.
- Alternative implementations and setup must not be merged into the active route: [MEM-CMP-clusterer](#mem-cmp-clusterer), [MEM-CMP-compressor](#mem-cmp-compressor), [MEM-OBJ-memory-vector](#mem-obj-memory-vector), [MEM-OBJ-memory-graph](#mem-obj-memory-graph) retain differing thresholds, formats, collection names and schema properties. Provider vector compatibility and deployed initialization remain unresolved; no functioning setup is inferred.
- Evaluation qualifications in [MEM-RTE-benchmark-evaluation](#mem-rte-benchmark-evaluation): the supplied [runtime account](runtime.md#runtime-account) identifies duplicate-trigger migration failure and default benchmark agent foreign-key admission limits; no fresh-install readiness or default benchmark executability is inferred. SRC-1 `go-api/internal/db/postgres/migrations/001_initial.sql`, `go-api/internal/db/postgres/client.go`, `go-api/cmd/api/main.go` and the three benchmark drivers. Existing storage/ranking/checker mechanisms remain source-grounded. Expected answers score retrieved context rather than a task agent's answer, semantic inclusion is omitted, ConvoMem expects the wrong snippet key, and reset is not effective on registered routes. No observed scores or causal memory benefit are available.
- Reasons and lineage are different: [MEM-OBJ-semantic-lineage](#mem-obj-semantic-lineage) attaches full-cluster references even when model input is truncated; [MEM-OBJ-semantic-candidate](#mem-obj-semantic-candidate) retains no reasons. Actual fact correctness, source adequacy and downstream reliance are unresolved, not inferred from confidence or evidence_count.

## Limitations and checks

Correction checks traced producer structs through HTTP handlers and SDK constructors to both adapters. Empty compatible list responses and direct HTTP are countercases to blanket reload failure; neither repairs nonempty ordinary SDK retrieval/listing. No source alias or timestamp transformation was found on the inspected paths. The source checkout's HEAD was rechecked as 935e8be0a1fca5b23dbabfe16c48b562c1cd24cc with a clean working tree. Source identity matches the supplied boundary. Governing job, member types, collection, worker rules and complete record contract were read; truncated/ranged invocation inputs were recovered before analysis. No additional source, prior analysis or target execution was used.

Coverage is static and scoped as above. No externally loaded semantic data, actual caller identity, provider output, live index dimension, deployed host prompt or benchmark artifact is supplied. These prevent operational success, activation and improvement conclusions. They do not erase implemented parsing, raw retention, access feedback and context construction. Invocation-specific `commonplace-run validate-output` passed: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” This establishes content-check compliance, including quotation occurrence, not analytical acceptance.
