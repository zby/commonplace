---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Graphiti runtime baseline tracing episode ingestion, retrieval, shipped consumers, service queues and alternate admission paths at the frozen commit."
run-id: AAS-2026-10-12-graphiti-1d535ca565a4-01
reviewed-boundary: "964bb11d1e7020e3cc67fab244268b0736b6c219"
---

# Graphiti runtime report

## Runtime account

### Evidence and principal work

Graphiti turns caller-supplied episodes into retained graph content and retrieves selected content for later callers. The Python library owns extraction, entity resolution, fact resolution, attribute/summary generation, embedding and persistence orchestration. Its REST and MCP servers own additional request admission and queueing. The shipped LangGraph notebook owns an enclosing conversation loop that both consumes facts and records conversation content. Those are different owners: the core library does not itself choose an assistant's next task or enforce an MCP host's tool permissions. The [boundary](boundary.md) fixes SRC-1, its full revision and external dependencies.

This account uses inspected implementation and shipped doctrine, not observed runs. All runtime operation remains uninspected; no target, model, database, example or evaluator was executed. Additional implementation coverage beyond the initial boundary reads includes `graphiti_core/graphiti_types.py`, `graphiti_core/llm_client/llm_runtime.py`, `graphiti_core/llm_client/client.py`, `graphiti_core/llm_client/openai_client.py`, `graphiti_core/llm_client/openai_base_client.py`, `graphiti_core/llm_client/gliner2_client.py`, `graphiti_core/prompts/lib.py`, `graphiti_core/utils/bulk_utils.py`, `graphiti_core/utils/maintenance/edge_operations.py`, `graphiti_core/search/search.py`, `graphiti_core/embedder/openai.py`, `graphiti_core/cross_encoder/openai_reranker_client.py`, and service retrieval/admission implementations. All are SRC-1 at the frozen revision. Reading these files does not establish cross-provider or cross-backend parity.

### Ordinary episode invocation

A library caller initiates `Graphiti.add_episode`, supplying content, name, source type, event time and optional group, UUID, schemas, custom instructions and saga association. The principal is the caller; whether a human supplies or approves each episode is not determined by the API. Graphiti validates schema configuration and resolves a request-local driver/client bundle. A missing group uses the provider default; another group may clone the driver with a different database target. It retrieves earlier episodes by reference time, group and source, unless explicit UUIDs replace that selection. A supplied episode UUID loads an existing episode rather than unconditionally replacing its body. Identity is carried by episode, entity and edge UUIDs plus group IDs. SRC-1: `graphiti_core/graphiti.py`.

The next-step owner is the Python coroutine, not an autonomous planner. It requests entities from the configured extraction path, resolves them against existing state, extracts and resolves edges, merges any newly materialized endpoint nodes, remaps edge pointers, then generates attributes and summaries using new rather than duplicate facts. Entity/fact text and prompt instructions are natural-language inputs; UUIDs, schema classes, pointer maps and timestamps have fixed programmatic consumers. Models propose content and comparison judgments; executable code interprets returned indices, remaps identities and applies temporal invalidation. Not every comparison calls a model: exact matching fact text and endpoints can reuse an edge immediately. The persistence step adds episode-to-entity edges, updates episode edge references, optionally removes raw content, and calls the bulk write helper. Optional saga association and community updates occur after that helper. The return is `AddEpisodeResults`; errors are traced and re-raised. See [RT-RTE-episode-ingestion](#rt-rte-episode-ingestion). SRC-1: `graphiti_core/graphiti.py`, `graphiti_core/utils/maintenance/edge_operations.py`, `graphiti_core/utils/bulk_utils.py`.

The external effect boundary includes model/embedding API calls and graph-driver writes. The library is already running in its caller's Python process. Its configurable clients, drivers and prompt builders are executable Python dependencies, not a demonstrated sandbox. Current provider credentials, database grants, host tool grants and deployed isolation remain uninspected. The capability surface includes read/write/delete/rebuild APIs and shipped service tools; the existence of those APIs does not establish a particular assistant's grant set. Model-controlled extraction is also not evidence of model-controlled shell execution. No such shell route is inferred here.

### Read and later consumer invocation

A caller's search text and optional center node/group/filter/config drive graph selection. Basic `search` uses hybrid edge retrieval with reciprocal-rank fusion or node-distance reranking. Advanced `search_` can retrieve other graph layers and use a cross-encoder. The search implementation computes a query embedding only for recipes requiring it, accepts a supplied query vector, and normalizes empty group scope to an unrestricted selector rather than an authorization denial. REST `/get-memory` composes message text into a query and returns formatted facts. MCP node and fact searches apply their own defaults and filters before formatting results. Retrieval is a return path, not proof of behavioral activation. See [RT-RTE-context-retrieval](#rt-rte-context-retrieval). SRC-1: `graphiti_core/graphiti.py`, `graphiti_core/search/search.py`, `server/graph_service/routers/retrieve.py`, `mcp_server/src/graphiti_mcp_server.py`.

In the shipped notebook, the `chatbot` function queries facts using the latest message and a user center node, formats only `edge.fact` strings, inserts them in a system message, and calls a tool-bound ChatOpenAI model. The LangGraph scheduler sends tool calls to a `ToolNode`; its shoe-search tool returns another facts string. A no-tool response terminates the graph. After every successful model response, including a tool-call response, the notebook unconditionally schedules asynchronous ingestion of the latest state message object and `response.content`, rather than awaiting durable memory before returning. The latest state message can be a human message on entry or a tool result after the tools-to-agent edge; state may also carry model messages. The episode body prefixes the latest message with the user name regardless of its actual origin. That prefix is not evidence that the recorded material came from a human. Thus the automatic trace-fed curation path can receive human-, model- and tool-derived material, and is not limited to one write per completed user turn. Conversation messages also live in a `MemorySaver` checkpointer keyed by thread ID; that external framework state is not identical to Graphiti graph memory. Notebook source establishes the delivery and requested influence of selected facts, not their correctness, successful storage, assistant compliance or benefit. See [RT-RTE-conversation-loop](#rt-rte-conversation-loop) and [RT-BAP-facts-context](#rt-bap-facts-context). SRC-1: `examples/langgraph-agent/agent.ipynb`.

### Alternate and forcing routes

Four forcing cases challenge seemingly global guarantees:

1. **Queued service acceptance versus completed persistence.** MCP `add_memory` validates the timestamp and returns queue acceptance; its worker logs failures and continues. REST `/messages` also returns acceptance, but its worker catches cancellation rather than ordinary job exceptions. Both queues are process-local. REST closes a request-scoped client after the dependency yield, while queued work captures that client; successful background use is not established by the request response. MCP's worker-running flag is set inside the scheduled worker, after scheduling: concurrent admissions before that task starts are not guarded by an atomic worker claim. The code therefore supports a sequential-processing design, not a global serialization invariant. Direct library calls and notebook tasks bypass both queues. See [RT-RTE-service-admission](#rt-rte-service-admission) and [RT-CLM-queue-completion](#rt-clm-queue-completion). SRC-1: `server/graph_service/routers/ingest.py`, `server/graph_service/zep_graphiti.py`, `mcp_server/src/services/queue_service.py`, `mcp_server/src/graphiti_mcp_server.py`.
2. **Bulk versus single-episode completion.** Bulk ingestion first persists episodes, then retrieves their context and extracts/deduplicates graph content, with combined extraction enabled by default. It later writes resolved entities/edges. A failed model stage can therefore follow an already persisted episode. In ordinary ingestion, saga writes and optional community updates follow the core bulk persistence call. One helper's transaction-shaped interface does not make either whole invocation atomic. See [RT-RTE-bulk-ingestion](#rt-rte-bulk-ingestion) and [RT-CLM-write-envelope](#rt-clm-write-envelope). SRC-1: `graphiti_core/graphiti.py`, `graphiti_core/utils/bulk_utils.py`.
3. **Model-routed prompts versus direct calls and bypasses.** The instance-scoped `LLMRuntime` chooses exact-prompt, then group, then default models and resolves builder overrides. Its built-in registry refuses replacement of fixed response schemas. The legacy helper without routing calls the client directly; custom clients can implement their own behavior. The cross-encoder calls an SDK separately, and the notebook's agent model is outside core prompt routing. GLiNER2 uses local or API entity extraction and delegates other operations to a required general-purpose LLM. No single model-routing or response-schema guarantee covers all these paths. See [RT-RTE-prompt-routing](#rt-rte-prompt-routing) and [RT-CLM-schema-boundary](#rt-clm-schema-boundary). SRC-1: `graphiti_core/graphiti_types.py`, `graphiti_core/llm_client/llm_runtime.py`, `graphiti_core/prompts/lib.py`, `graphiti_core/llm_client/gliner2_client.py`, `graphiti_core/cross_encoder/openai_reranker_client.py`, `examples/langgraph-agent/agent.ipynb`.
4. **Episode processing versus supplied writes and maintenance.** Triplet insertion bypasses episode extraction but still resolves endpoints, duplicate facts and potential invalidation. REST entity creation embeds and saves supplied names/summaries without episode extraction. Direct namespace/node/edge writes are a further capability surface. Community rebuild removes old community state before generating and saving replacements. Saga summary updates persist both text and watermarks; deletion/clear APIs can erase state. REST episode deletion directly deletes the episode node, whereas MCP invokes core `remove_episode` cleanup. That core implementation selects edges by first episode reference, not by sole support, and nodes by mention count; the service paths therefore do not have equivalent withdrawal effects. Thus the episode extraction policy is not a universal admission gate, and graph clearing is not a rollback history. See [RT-RTE-maintenance-writes](#rt-rte-maintenance-writes). SRC-1: `graphiti_core/graphiti.py`, `server/graph_service/zep_graphiti.py`, `server/graph_service/routers/ingest.py`, `mcp_server/src/graphiti_mcp_server.py`.

The smallest inspected forcing set is these four cases, not a complete security or backend audit. Provider-native structured output, local extraction, direct SDK reranking, executable prompt builders, direct graph mutation and durable graph variants are materially different control paths. Database engine transactions, retry/idempotence of every backend, external host approvals, all provider overrides, other example loops and deployment isolation remain unresolved; none is treated as absent.

### Change admission and evaluation

Retained knowledge changes are admitted by extraction/resolution software, caller-supplied direct writes, maintenance calls and deletions. Prompt libraries, model routes, custom schemas, clients and drivers are supplied by the configuring caller; configuration can change production behavior without a per-content approval gate. The inspected code does not show runtime model-weight training. Provider internals are inaccessible here, and model-name configuration is not a weight digest. Components below separately state fixity limits.

The graph-building evaluator is a bounded comparison route, not a production admission mechanism. It builds a model-produced baseline, serializes and reloads results, builds a candidate graph from the same selected message dataset and requests model judgments. The reference outcome is baseline graph output, not independently certified truth. Its context assembly indexes a message string as `episodes[0]` and `episodes[1:]`, so the judge receives the first character and the remaining substring under message/previous-message labels rather than the full contextual sequence those names suggest. This limits interpreting its score even before execution. No automatic installation of a winning client, prompt or graph is established by this evaluator. See [RT-RTE-evaluation-comparison](#rt-rte-evaluation-comparison). SRC-1: `tests/evals/eval_e2e_graph_building.py`.

## Shared records

### Components

#### RT-CMP-openai-client
Label: OpenAIClient language-model transport

Source-native identity: `OpenAIClient` and its `BaseOpenAIClient` implementation, optionally replaced by caller-supplied clients or selected through `LLMRuntime`. Representational form: distributed-parametric provider model; local symbolic client/configuration objects and natural-language messages are separate from its weights. Storage substrate: external provider infrastructure; API client/configuration in process memory. Default large/small model names are `gpt-5.5` and `gpt-4.1-nano`. Exact weights/version are not pinned by those names. Mutable configured endpoints or provider aliases can resolve to a different model. The inspected adapter requests inference, not operational parameter updates; provider-side parameter changes remain uninspected. It supports response-schema requests, JSON decoding, retry and tracing, not guaranteed truth. SRC-1: `graphiti_core/llm_client/openai_client.py`, `graphiti_core/llm_client/openai_base_client.py`, `graphiti_core/llm_client/client.py`.

> response = await self.client.responses.parse(**request_kwargs)
> --- `graphiti_core/llm_client/openai_client.py`

#### RT-CMP-openai-embedder
Label: OpenAIEmbedder numerical encoding

Source-native identity: `OpenAIEmbedder`, default `text-embedding-3-small`. Representational form: distributed-parametric model and dense vector output, distinct from the input text and local API configuration. Storage substrate: remote model; returned vectors in process memory and graph properties after persistence. This adapter performs inference without a weight-update operation. Exact model version/weights are not pinned; base URL, injected client and mutable provider endpoint permit different implementations. Provider internals are uninspected. Generated vector changes are not model-parameter training. SRC-1: `graphiti_core/embedder/openai.py`, `graphiti_core/utils/bulk_utils.py`.

> result = await self.client.embeddings.create(
>     input=input_data, model=self.config.embedding_model
> )
> --- `graphiti_core/embedder/openai.py`

#### RT-CMP-openai-reranker-client
Label: OpenAIRerankerClient relevance classifier

Source-native identity: `OpenAIRerankerClient`, default `gpt-4.1-nano`. Representational form: distributed-parametric model used to classify query/passage pairs; the symbolic consumer converts log probabilities to scores and sorts. Storage substrate: provider model, transient local scores. Exact weights/version are not pinned; configured model, base URL or client can change resolution. The inspected path requests inference and does not update parameters; provider changes remain uninspected. It directly invokes the SDK, so `LLMRuntime` prompt routing and core response schemas do not govern it. SRC-1: `graphiti_core/cross_encoder/openai_reranker_client.py`.

> results = [(passage, score) for passage, score in zip(passages, scores, strict=True)]
> results.sort(reverse=True, key=lambda x: x[1])
> return results
> --- `graphiti_core/cross_encoder/openai_reranker_client.py`

#### RT-CMP-gliner2-client
Label: GLiNER2Client alternative entity extractor

Source-native identity: `GLiNER2Client`. Representational form: distributed-parametric extractor, plus a separately required general-purpose LLM delegate. Storage substrate: locally loaded model objects or external API; local config and outputs in memory. Local models are loaded by model ID without a revision argument in the inspected constructor; exact weights are not pinned. Loaded local objects are stable for that instance barring caller mutation; subsequent loads or API endpoint resolution can differ. The adapter requests extraction, not training; API-side parameter changes are uninspected. Non-entity-extraction requests delegate to the wrapped client rather than becoming local GLiNER2 decisions. SRC-1: `graphiti_core/llm_client/gliner2_client.py`.

> self._model = GLiNER2.from_pretrained(model_id)
> --- `graphiti_core/llm_client/gliner2_client.py`

#### RT-CMP-chat-openai
Label: Notebook ChatOpenAI agent model

Source-native identity: notebook `llm`, configured as tool-bound ChatOpenAI `gpt-4.1-mini`. Representational form: distributed-parametric remote model. Storage substrate: external provider; SDK wrapper in notebook process. Exact weights/version are not pinned, and provider/host configuration can change endpoint resolution. The notebook requests inference, with no training operation inspected; external model updates remain uninspected. Its responses determine whether the scheduler executes the bound shoe-search tool. Framework internals are outside the frozen source. SRC-1: `examples/langgraph-agent/agent.ipynb`.

> "llm = ChatOpenAI(model='gpt-4.1-mini', temperature=0).bind_tools(tools)"
> --- `examples/langgraph-agent/agent.ipynb`

### Operative objects

none declared in this member. Graph object content and revision semantics are left to the memory analyst; this report identifies their runtime consumers and write envelopes without redeclaring their parts.

### Routes

#### RT-RTE-episode-ingestion
Label: Single episode knowledge admission

Endpoints/progression: caller episode arguments → request-scoped client bundle → prior episode retrieval → entity extraction/resolution → edge extraction/resolution → node attributes/summaries → graph persistence → optional saga/community work → `AddEpisodeResults`. Owner: `Graphiti.add_episode`. Trigger: caller invocation. Proposed change: extracted graph entities, facts, attributes and associations. Model/software propose and decide; caller schemas, source, exclusions, custom instructions and prior UUIDs shape the proposal. Human per-content decision or veto is unresolved. Software may reject invalid schema configuration or fail model/database processing; there is no demonstrated factual-truth veto. Operating mode: open caller requests, not a bounded experiment. Answer oracle: inapplicable — existing graph candidates and episode text are evidence inputs, not certified expected outcomes. Recovery: exceptions re-raised; explicit deletes/clear can change state but no whole-invocation rollback is established. What persists: graph content and optionally episode text, plus saga/community state when requested. SRC-1: `graphiti_core/graphiti.py`, `graphiti_core/utils/maintenance/edge_operations.py`.

- Immediate return: `AddEpisodeResults` after the awaited processing path, or a propagated exception.
- Later read-back: saved graph content feeds later extraction context and searches; successful persistence is not observed here.
- Delegated visibility: configured model/embedding providers receive selected context/text; database driver receives serialized graph data.
- Selection predicate: caller group/source/time or explicit prior episode UUIDs; graph candidate searches and model comparisons select resolutions.
- Invalidation or expiry: edge resolution can mark existing facts temporally invalid; caller deletion paths can remove content.
- Activation or effect: implementation writes graph content and requests model processing; downstream behavior change remains unobserved.
- Evidence limits: no invocation trace, model accuracy measurement, external transaction proof or human-approval evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not self.store_raw_episode_content:
>     ep.content = ''
> --- `graphiti_core/graphiti.py`

> # Fast path: if the fact text and endpoints already exist verbatim, reuse the matching edge.
> normalized_fact = _normalize_string_exact(extracted_edge.fact)
> --- `graphiti_core/utils/maintenance/edge_operations.py`

#### RT-RTE-context-retrieval
Label: Query to selected graph context

Endpoints/progression: library/REST/MCP query → hybrid search and selected reranker → graph results → caller or formatted service response. Owner: core search, with service-specific default/filter/formatting owners. Context/state: query, optional vectors, groups, center node, filters and stored graph. Decision policy: symbolic recipe dispatch/ranking plus numerical embedding and optional model relevance scoring. No graph admission is established by reads. SRC-1: `graphiti_core/graphiti.py`, `graphiti_core/search/search.py`, `server/graph_service/routers/retrieve.py`, `mcp_server/src/graphiti_mcp_server.py`.

- Immediate return: edges or `SearchResults`; REST/MCP format selected graph parts as facts/nodes.
- Later read-back: retained graph material from earlier writes is selected for each caller invocation.
- Delegated visibility: embedding provider receives query text when needed; cross-encoder receives query and passages when selected.
- Selection predicate: query similarity/full text, recipe, result limit, center-node distance, labels/date filters and requested group scope; empty scope can normalize to unrestricted.
- Invalidation or expiry: inapplicable — this route reads; temporal filtering and removal depend on retained graph state and caller filters.
- Activation or effect: delivery is wired; recipient compliance, decision change and benefit are unobserved.
- Evidence limits: ranking quality, formatting completeness across every service/backend and actual recipient use are not measured.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # if group_ids is empty, set it to None
> group_ids = group_ids if group_ids and group_ids != [''] else None
> --- `graphiti_core/search/search.py`

#### RT-RTE-conversation-loop
Label: Notebook memory-informed conversation

Endpoints/progression: latest message in conversation state → Graphiti search → facts string/system message → tool-bound model → unconditional async episode-ingestion scheduling → response returned to scheduler → tool execution and return to agent, or graph end. Episode input combines the string representation of the latest state message object with `response.content`. Owner: notebook glue and external LangGraph scheduler. Trigger/principal: user invocation initiates the loop; model tool-call output and the tools-to-agent edge trigger further chatbot invocations without a new human message. Identities: user name/node UUID and checkpointer thread ID; graph episodes use library identities. Policy/form: natural-language sales instructions and facts interpreted by the model; symbolic tool-call and conditional graph-edge consumers. Context/state: system message plus accumulated messages, checkpoint state and selected graph facts. Grant surface: one bound shoe-search tool in this notebook; deployment isolation is uninspected. Knowledge admission is automatically scheduled by notebook code after each successful `llm.ainvoke`, including responses with tool calls, with no per-response human veto shown. Trace origin: episode input includes the latest state message (human input on entry, tool result after tool execution, or model message when that is latest in supplied state) plus the newly generated model response content. A tool result can itself contain retrieved graph facts. The unconditional user-name prefix on the latest message does not establish human origin; no origin validation at this scheduling site is shown. This is an automatic trace-fed curation route, not proof of completed ingestion or changed assistant behavior. Operating mode: open conversation. Answer oracle: inapplicable — no expected answer supplied to this loop. Recovery: ingestion task completion is not awaited or tied to graph success; widget caller displays graph exceptions. SRC-1: `examples/langgraph-agent/agent.ipynb`.

- Immediate return: updated response messages from chatbot; graph terminates when no tool call is present.
- Later read-back: subsequently retrieved facts can derive from earlier conversation episodes; asynchronous completion makes availability timing unresolved.
- Delegated visibility: ChatOpenAI receives selected facts and accumulated conversation; bound tool receives model query; if the scheduled ingestion runs, extraction receives the serialized latest state message and new response content, which can include tool/model-derived material mislabeled by a user-name prefix.
- Selection predicate: last-message-derived query, user center node and five results; shoe tool uses product center node and ten results.
- Invalidation or expiry: ingestion follows core temporal handling; notebook initialization clears the graph, while checkpointer lifecycle belongs to its host.
- Activation or effect: facts enter system-message context and tool results; compliant assistant behavior and improved sales assistance are unobserved.
- Evidence limits: notebook code is implementation evidence, not its historical outputs; dependency compatibility, task completion and checkpoint durability are not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "    messages = [system_message] + state['messages']\n",
> --- `examples/langgraph-agent/agent.ipynb`

> "    asyncio.create_task(\n",
> "        client.add_episode(\n",
> "            name='Chatbot Response',\n",
> "            episode_body=f'{state[\"user_name\"]}: {state[\"messages\"][-1]}\\nSalesBot: {response.content}',\n",
> --- `examples/langgraph-agent/agent.ipynb`

> "graph_builder.add_conditional_edges('agent', should_continue, {'continue': 'tools', 'end': END})\n",
> "graph_builder.add_edge('tools', 'agent')\n",
> --- `examples/langgraph-agent/agent.ipynb`

#### RT-RTE-service-admission
Label: REST and MCP queued episode admission

Endpoints/progression: REST `/messages` or MCP `add_memory` → process-local queue → worker → core `add_episode`. Owners: REST `AsyncWorker`; MCP `QueueService`. Trigger/principal: HTTP caller or MCP host tool caller. Proposed change: conversation/episode graph content admitted through the core pipeline. Caller supplies content; service checks and extraction software decide processing. Host approvals and human per-content veto remain uninspected. MCP forwards source/schema/custom instructions/saga options and validates timestamp before admission. Operating mode: open service requests. Answer oracle: inapplicable — queue admission checks inputs, not truth. Recovery: MCP catches/logs per-job exceptions and marks tasks done; REST worker catches cancellation only. Queues and worker flags are in-memory, with no durable retry result demonstrated. Different lifecycle and concurrency controls make these alternate paths, not equivalent durability guarantees. SRC-1: `server/graph_service/routers/ingest.py`, `server/graph_service/zep_graphiti.py`, `mcp_server/src/services/queue_service.py`, `mcp_server/src/graphiti_mcp_server.py`.

- Immediate return: queue-acceptance success (HTTP 202 for messages), not a committed graph result; malformed MCP timestamp can return error before queueing.
- Later read-back: successfully processed jobs enter ordinary graph retrieval; queued or failed jobs have no proven read-back.
- Delegated visibility: worker receives captured parameters/client and invokes the same providers/database as core processing.
- Selection predicate: all admitted messages; MCP organizes queues by effective group ID.
- Invalidation or expiry: REST shutdown drains remaining queue entries; process loss discards process-local queue state; completed graph state follows core controls.
- Activation or effect: worker execution is wired; actual completion, serialization under concurrent admissions and provider reliability are unobserved.
- Evidence limits: no persistent queue, background-client lifecycle test or deployment trace supplied; no global ordering claim across direct/API/other-process writers.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not self._queue_workers.get(group_id, False):
>     asyncio.create_task(self._process_episode_queue(group_id))
> --- `mcp_server/src/services/queue_service.py`

> try:
>     print(f'Got a job: (size of remaining queue: {self.queue.qsize()})')
>     job = await self.queue.get()
>     await job()
> except asyncio.CancelledError:
>     break
> --- `server/graph_service/routers/ingest.py`

#### RT-RTE-bulk-ingestion
Label: Bulk episode admission with staged writes

Endpoints/progression: caller batch → request scope → initial episode persistence → prior context retrieval → combined or separate extraction/deduplication → existing-graph resolution → final graph write and optional saga operations. Owner: `Graphiti.add_episode_bulk`. Decision policy/form: symbolic batching and remapping, model-generated natural-language graph content and numerical embeddings. Trigger: caller batch request. Proposed change: episodes and their graph entities/facts. Caller instructions/schema and software/model processing shape admission; no per-content human gate established. Operating mode: caller-selected bulk ingestion. Answer oracle: inapplicable — graph resolution candidates are not expected answers. Rejection: validation/provider/database exceptions can interrupt stages. Recovery: error tracing/rethrow does not reverse the initial episode write. SRC-1: `graphiti_core/graphiti.py`, `graphiti_core/utils/bulk_utils.py`.

- Immediate return: bulk results after final processing, or exception after possible earlier persistence.
- Later read-back: episodes are written before extraction; final entities/edges feed later searches and ingestion context.
- Delegated visibility: extraction clients see batch episode context; driver sees initial and later graph writes.
- Selection predicate: supplied batch, retrieved prior context and dedupe candidates; `use_combined_extraction` selects a material processing variant.
- Invalidation or expiry: resolved and invalidated edges are persisted together; later deletion/clear remain explicit controls.
- Activation or effect: staged graph writes and model calls are wired, not observed.
- Evidence limits: no all-or-nothing batch guarantee, equivalence of combined/separate model results, concurrent-writer safety or performance measured.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # Save all episodes
> await add_nodes_and_edges_bulk(
>     driver=driver,
>     episodic_nodes=episodes,
>     episodic_edges=[],
>     entity_nodes=[],
>     entity_edges=[],
>     embedder=clients.embedder,
> )
> --- `graphiti_core/graphiti.py`

#### RT-RTE-prompt-routing
Label: Configured prompt and model selection

Endpoints/progression: named prompt/context → routing/builder/schema resolution → client generation → returned dict. Owners: `GraphitiClients`, `LLMRuntime`, caller configuring the instance and concrete client. This is a runtime-client control path rather than an enclosing agent planner. Trigger: core model request; proposed production-behavior change: configuring another model, builder, client or prompt library. Caller chooses configuration; fixed built-in schemas can veto incompatible overrides on the routed path, while direct legacy calls are a separate path. Human authorship/approval of configuration is unresolved. Guidance: shipped prompt builders and configured overrides; they persist as instance configuration/source code, not automatically learned replacements. Operating mode: fixed configured dispatch within open processing requests. Answer oracle: inapplicable — response schemas constrain representation, not expected truth. Recovery: change configuration/recreate instance; no deployment rollback is established. SRC-1: `graphiti_core/graphiti_types.py`, `graphiti_core/llm_client/llm_runtime.py`, `graphiti_core/prompts/lib.py`.

- Immediate return: client response after exact-prompt/group/default model resolution; errors can propagate.
- Later read-back: inapplicable — static prompt/configuration supply is not accumulated use-dependent memory in this route.
- Delegated visibility: selected transport gets builder messages and resolved schema; executable overrides run in caller process.
- Selection predicate: exact prompt route before group route before default model; model override before general override before library builder.
- Invalidation or expiry: caller can replace configuration; no automatic prompt revision/expiry established by this path.
- Activation or effect: changed configuration controls model requests; successful compliance with requested semantics remains unobserved.
- Evidence limits: direct SDK reranking, legacy clients, custom subclasses and notebook model bypass this scope; external provider internals are uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> override = model.flat_overrides.get(prompt_name)
> if override is None:
>     override = self.prompt_overrides.get(prompt_name)
> if override is not None:
>     return _wrap_builder(override, prompt_name)
> return get_prompt_builder(self.library, prompt_name)
> --- `graphiti_core/llm_client/llm_runtime.py`

#### RT-RTE-maintenance-writes
Label: Supplied graph writes and derived-state maintenance

Endpoints/progression: caller triplet/direct node/maintenance request → corresponding core or service operation → graph mutations → result. Owners: `Graphiti.add_triplet`, `build_communities`, `summarize_saga`, deletion APIs and service wrappers. These are related admission mechanisms, not identical semantic checks. Triplets supply graph text directly, then resolve endpoints/facts; REST entity save embeds supplied name and saves supplied summary. Community rebuild clears scoped old communities before model-derived replacement; saga summary combines existing truncated summary and selected new episodes and saves text/watermarks. Deletion/clear issue graph mutations without rebuilding an earlier version. REST `/episode/{uuid}` invokes `delete_episodic_node`, which directly deletes the episode node. MCP `delete_episode` instead invokes core `remove_episode`: it deletes referenced entity edges when `edge.episodes[0]` equals the removed episode UUID, even if other episode references remain, and deletes entity nodes with a mention count of one. The MCP docstring's sole-support description is therefore stronger than the inspected edge predicate; REST does not invoke this core cleanup at all. Trigger: explicit caller/tool invocation. Proposers: caller for supplied graph content, model/software for derived summaries. Admission/rejection: executable validation and write operations, with errors propagated or converted by wrappers; model-generated summaries have no demonstrated factual oracle or per-content human veto. Guidance: configured summary/resolution prompts and caller arguments. Operating mode: caller-triggered maintenance, not self-directed product improvement. Answer oracle: inapplicable — no certified desired graph/summary supplied. Recovery: explicit repair/delete/rebuild; destructive clear and staged replacements are not rollback history. Persistence: graph text, structure, embeddings and summary watermarks. SRC-1: `graphiti_core/graphiti.py`, `server/graph_service/zep_graphiti.py`, `server/graph_service/routers/ingest.py`, `mcp_server/src/graphiti_mcp_server.py`.

- Immediate return: triplet nodes/edges, community nodes/edges, updated saga or wrapper success/error according to invoked operation.
- Later read-back: saved supplied content and derived summaries can enter later graph reads; saga summary also feeds its next summarization invocation.
- Delegated visibility: model/embedding clients receive selected content for applicable operations; database receives direct and derived updates.
- Selection predicate: supplied UUIDs/triplet endpoints, requested groups/community clustering, or saga ID with ingestion watermark and prompt budget.
- Invalidation or expiry: fact temporal resolution, explicit removal and clear; REST direct episode-node deletion differs from MCP core first-reference edge cleanup and single-mention node cleanup; neither establishes global retraction of derived content. Community rebuild removes old communities before replacements.
- Activation or effect: maintenance changes graph state and future summarizer inputs; actual behavior change remains unobserved.
- Evidence limits: all backend deletion semantics and every namespace operation not deeply inspected; no complete transactional repair or summary-losslessness guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # Clear existing communities (scoped: only the groups being rebuilt)
> await remove_communities(driver, group_ids=group_ids)
> --- `graphiti_core/graphiti.py`

> saga.summary = summary
> --- `graphiti_core/graphiti.py`

> async def delete_episodic_node(self, uuid: str):
>     try:
>         episode = await EpisodicNode.get_by_uuid(self.driver, uuid)
>         await episode.delete(self.driver)
> --- `server/graph_service/zep_graphiti.py`

> await scoped_client.remove_episode(uuid)
> --- `mcp_server/src/graphiti_mcp_server.py`

> for edge in edges:
>     if edge.episodes and edge.episodes[0] == episode.uuid:
>         edges_to_delete.append(edge)
> --- `graphiti_core/graphiti.py`

#### RT-RTE-evaluation-comparison
Label: Graph-building baseline and candidate comparison

Endpoints/progression: selected dataset sessions/messages → baseline graph build/JSON export → candidate graph build/export → reload baseline → model judgment → numeric score. Owner: evaluation script/caller. Proposer: configured candidate model/client; computational judge decides `candidate_is_worse`, software aggregates scores. Human role: chooses invocation/settings/client; no human per-result judgment shown. Trigger: explicit evaluation, not automatic runtime improvement. Proposed change/admission: candidate graph is written for evaluation, but score does not install a production successor. Oracle/reference: baseline results generated by `gpt-4.1-mini`, not independent expected graph truth. Operating mode: bounded dataset experiment, limited by selected counts/length and comparison context construction. Guidance: shipped evaluation prompt; results persist in JSON and graph state, not revised evaluator instructions. Rejection ability: judge can lower score; no production veto wired here. Recovery: rebuild/rerun by caller, not automatic rollback. SRC-1: `tests/evals/eval_e2e_graph_building.py`.

- Immediate return: averaged score; script prints model judgments.
- Later read-back: baseline JSON is reloaded as typed results for candidate judgments; exported candidate results permit later inspection, not demonstrated automatic successor selection.
- Delegated visibility: judge receives baseline/candidate records with embeddings removed from exported results and character-sliced message context.
- Selection predicate: dataset prefix counts, session-length cap, zipped corresponding baseline/candidate results; default evaluator client is also used for candidate construction.
- Invalidation or expiry: caller can overwrite result files and rebuild graphs; no result freshness/production replacement policy established.
- Activation or effect: judgment/aggregation wiring is inspected; measured scores, improved capacity and causal component attribution are unobserved.
- Evidence limits: no execution; baseline is model-produced; message-string indexing weakens intended contextual comparison; no production admission link established by this function.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> context = {
>     'baseline': baseline_result,
>     'candidate': add_episode_result,
>     'message': episodes[0],
>     'previous_messages': episodes[1:],
> }
> --- `tests/evals/eval_e2e_graph_building.py`

### Claims

#### RT-CLM-queue-completion
Label: Service acceptance is not completion

Claimed operation/source: MCP response declares queueing; REST returns acceptance. Guarantee owner/enforcement: service admission and process-local workers. Guarantee strength: best effort. Covered paths: these queued entry points only. Alternate paths: direct library, notebook tasks, triplets and other processes are outside these queues. Required external contract: process survival, valid client lifetime and functioning providers/database. Worker exception handling and delayed worker flag setting bound reliability; the intended sequential design is not proven global serialization. See [RT-RTE-service-admission](#rt-rte-service-admission). SRC-1: `mcp_server/src/graphiti_mcp_server.py`, `mcp_server/src/services/queue_service.py`, `server/graph_service/routers/ingest.py`, `server/graph_service/zep_graphiti.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> message=f"Episode '{name}' queued for processing in group '{effective_group_id}'"
> --- `mcp_server/src/graphiti_mcp_server.py`

#### RT-CLM-write-envelope
Label: Bulk helper is not whole-invocation atomicity

Claimed operation/source: the helper submits graph objects through a session write operation. Owner/enforcement: `add_nodes_and_edges_bulk` and selected driver's session implementation. Guarantee strength: protocol. Covered path: one helper invocation requests transactional-shaped writes and closes its session. Required external contract: concrete driver/database execution and transaction semantics; these are not inferred from the common interface. Alternate paths: bulk prewrites, saga association, community updates and direct saves cross separate boundaries. Whole-invocation rollback/durability is not established. See [RT-RTE-episode-ingestion](#rt-rte-episode-ingestion), [RT-RTE-bulk-ingestion](#rt-rte-bulk-ingestion) and [RT-RTE-maintenance-writes](#rt-rte-maintenance-writes). SRC-1: `graphiti_core/utils/bulk_utils.py`, `graphiti_core/graphiti.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> await session.execute_write(
>     add_nodes_and_edges_bulk_tx,
>     episodic_nodes,
>     episodic_edges,
>     entity_nodes,
>     entity_edges,
>     embedder,
>     driver=driver,
> )
> --- `graphiti_core/utils/bulk_utils.py`

#### RT-CLM-schema-boundary
Label: Fixed schema dispatch is not factual correctness

Claimed operation/source: routed built-in prompt dispatch rejects incompatible schema replacement. Owner/enforcement: `resolve_response_model` called before generation by routed clients/runtime. Guarantee strength: invariant, conditional on invoking this resolver without modifying the registry/code. Covered paths: instance-routed named prompts using the built-in registry; dynamic schemas explicitly require caller response models. Required external contract: concrete clients honor structured-output requests; semantic correctness is not part of schema identity enforcement. Alternate paths: legacy direct helper/client calls, reranker SDK, notebook agent model, custom client internals. The attribute-extraction preamble is natural-language policy, not a type-level proof that returned values are genuine. SRC-1: `graphiti_core/prompts/lib.py`, `graphiti_core/graphiti_types.py`, `graphiti_core/llm_client/client.py`. See [RT-RTE-prompt-routing](#rt-rte-prompt-routing).

- implementation conclusion status: wired
- operation conclusion status: uninspected

> if response_model is not None and response_model is not spec.response_model:
>     raise ValueError(
>         f'Prompt schema overrides are not allowed for {prompt_name}: '
>         f'got {response_model.__name__}, expected '
>         f'{spec.response_model.__name__ if spec.response_model else None}'
>     )
> return spec.response_model
> --- `graphiti_core/prompts/lib.py`

### Evidenced absences

none declared in this member. Uninspected provider/deployment behavior, model reasoning and alternate backend details are limits, not bounded absences.

### Behavioral-authority paths

#### RT-BAP-facts-context
Label: Retrieved facts in notebook model context

Consumer: tool-bound notebook ChatOpenAI model. Channel: formatted `edge.fact` text in a system message and shoe-search tool returns. Force: requested natural-language influence, not executable constraint or observed compliance. Horizon: each conversation step, potentially across later steps after graph ingestion; async completion and host/database lifecycle bound availability. Retrieval discards other edge fields from the facts string, so source metadata and temporal fields do not accompany the facts through this formatting path. See [RT-RTE-conversation-loop](#rt-rte-conversation-loop). SRC-1: `examples/langgraph-agent/agent.ipynb`.

> "        {facts_string or 'No facts about the user and their conversation'}\"\"\"\n",
> --- `examples/langgraph-agent/agent.ipynb`

#### RT-BAP-memory-instructions
Label: Shipped MCP memory-use instructions

Consumer: external assistant/host that loads the shipped Cursor rules. Channel: natural-language instructions to search, retain requirements/preferences/procedures and apply retrieved material. Force: policy requested of the assistant; the service cannot prove host loading or compliance. Horizon: tasks/sessions while host supplies the rules and memory persists. These instructions establish intended knowledge and procedural influence; model-dependent activation is not observed. Their `search_facts` naming should not be assumed identical to every tool name at this revision without host mapping. SRC-1: `mcp_server/docs/cursor_rules.md`, `mcp_server/src/graphiti_mcp_server.py`.

> - **Follow procedures exactly:** If you find a procedure for your current task, follow it step by step.
> --- `mcp_server/docs/cursor_rules.md`

## Annotations

none
