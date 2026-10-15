---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "MemPalace runtime baseline: live capture, later recall, MCP control boundaries, setup admission and delegated task delivery at the frozen commit."
run-id: AAS-2026-10-14-mempalace-ed71875aea5a-01
reviewed-boundary: "1392e1810c3ca67776bd7fe3e198788a96dbd6d1"
---

# MemPalace runtime report

## Runtime account

### Claimed work and evidence basis

MemPalace retains conversation and project material for later agent recall. Its source-native unit is a drawer, organized by wing and room; retrieval returns selected text, not an independently verified answer. Shipped recall guidance asks the foreground agent to search before answering about prior work and to quote stored words. The executable mechanisms supply material and accept writes; the external host owns generative answering and agent compliance. See [RT-CLM-recall-protocol](#rt-clm-recall-protocol) and [RT-BAP-agent-context](#rt-bap-agent-context). SRC-1: `skills/mempalace-recall/SKILL.md`, `mempalace/searcher/query.py`.

This account uses implementation and doctrine/design from SRC-1 at the boundary's exact commit. No target, tests, evaluator or provider was executed. Wiring is inspectable; exercise, activation, benefit, production durability and latency remain unobserved. Retained source comments about incidents are attributed design rationale, not supplied traces. Added inspection covers the MCP fragments (`protocol.py`, `_guards.py`, `tools_read.py`, `tools_write.py`, `tools_coord.py`, `http.py`), `searcher/candidates.py`, `embedding.py`, `embeddinggemma2.py`, backend registration, setup/entity admission, task envelopes, logstream patch delivery, Hermes lifecycle and DSH recall. All are implementation evidence under the existing SRC-1, not new sources.

### An ordinary invocation: completed turn to later recall

Take an initialized Hermes session as the ordinary shipped state-production-to-consumption path. The host calls `initialize(session_id, ...)`. Code excludes cron/flush contexts, resolves the palace and configured collection name, loads identity and wing configuration, opens a Chroma collection, starts one background filing worker if ready, and refreshes a wake-up cache. Failed backend initialization leaves the provider inactive rather than claiming persistence. The adapter uses a direct `ChromaBackend` open, not the public collection wrapper; wrapper-wide claims therefore cannot automatically cover this path. SRC-1: `mempalace/integrations/hermes/__init__.py`.

The host calls `sync_turn` after a completed turn. Code normalizes user and assistant contents and enqueues a payload containing both texts and the session identity. A worker, not the model, owns the next step. It labels the text `User:` and `Assistant:`, classifies a wing, and calls `file_conversation_exchange` under a collection lock. That function strips outer whitespace, validates wing/room with fallback names, derives an exchange ID including filing time, attaches source/session/date/ingest metadata, and upserts the drawer. Neither queueing nor this automatic write asks for per-content human approval. The host controls whether lifecycle callbacks happen at all. See [RT-RTE-hermes-capture](#rt-rte-hermes-capture). SRC-1: `mempalace/integrations/hermes/__init__.py`, `mempalace/convo_miner.py`.

At a later invocation the host can ask `prefetch(query)`. Code searches the palace, limits the hit count, extracts each returned `text`, prepends wing/room tags, and returns a natural-language context block. Separately `system_prompt_block()` returns identity plus cached wake-up material. The adapter does not itself run the answer model. Delivery into its host-facing return is wired; actual host insertion and subsequent model dependence were not observed. See [RT-RTE-palace-recall](#rt-rte-palace-recall). SRC-1: `mempalace/integrations/hermes/__init__.py`.

The search chain opens drawers, constructs filters and a candidate pool, queries the embedding-backed collection, and ranks candidates. Closets are a boost, not the exclusive access gate. Closet-boosted hits can be replaced by a lexical best passage plus neighboring chunks; oversized hydration is truncated with an instruction to fetch full content. The final pool is reranked/deduplicated, may be widened, and becomes a result envelope. Thus a durable verbatim drawer does not imply that every later search returns its full contents or that a no-hit result proves absence. SRC-1: `mempalace/searcher/query.py`, `mempalace/searcher/candidates.py`.

The representational parts differ: conversation and identity text receives consequences through agent interpretation; metadata and routing rules have fixed software consumers; embedding models and vectors are distributed-parametric. The model choices are separate components, not one globally pinned model: [RT-CMP-minilm](#rt-cmp-minilm), [RT-CMP-embeddinggemma](#rt-cmp-embeddinggemma), [RT-CMP-embeddinggemma2](#rt-cmp-embeddinggemma2), [RT-CMP-openai-compat](#rt-cmp-openai-compat). No training step is established in this inspected invocation. That does not exclude behavioral change through retained content.

### Entry paths and material alternates

The installed CLI dispatches mining by project/conversation/format/source mode and can route a job to a daemon or HTTP hub rather than mine locally. Source adapters and dry-run are distinct branches. The full MCP entry point is a proxy: a plain stdio invocation can forward to a discovered hub; otherwise it loads the full server. The light server consolidates tools into `palace_query`, `palace_exec` and `palace_coordinate`, parses PQL, maps to underlying handlers and applies preflight gates. Shipped shell hooks invoke the CLI; host adapters also call APIs directly. These paths matter because a single MCP permission gate is not the whole system's write policy. SRC-1: `mempalace/cli/cmd_mine.py`, `mempalace/mcp_proxy.py`, `mempalace/mcp_light_server.py`, `mempalace/hooks_cli.py`, `mempalace/integrations/hermes/__init__.py`.

DSH is an unsolicited context-supply alternate: session start runs `wake-up`, removes the CLI banner and unavailable-layer hints, and registers agent-local prompt variable/section providers. One first prompt assembly waits within a configured time budget; a slow read may arrive only on later assemblies. Disposing the agent unwinds its registrations. This is host-context scoping, not a MemPalace implementation of host compaction or child-agent isolation. Hermes's pre-compression callback intentionally returns no hint; its delegation callback files only the task/result pair into the parent session. The external host determines the isolated child context and actual compressed window. SRC-1: `.dsh-plugin/lib/recall.js`, `mempalace/integrations/hermes/__init__.py`.

### Four forcing cases and guarantees

1. **A client calls a write tool despite a hidden tool list.** Full dispatch rejects names in the read-only refused set; light dispatch classifies the underlying operation before checking it, including coordination. This supports a server-owned protocol guarantee, not a filesystem invariant. `reconnect` is deliberately allowed despite possible disk effects. Plugin collection backends can lose the `read_only` option through compatibility fallback. Direct CLI, Python callbacks and backend code do not inherit an MCP server's flag. The capability surface includes write tools, settings and coordination; the grant set depends on server flags and configuration; no actual deployed isolation envelope was supplied. See [RT-RTE-mcp-dispatch](#rt-rte-mcp-dispatch), [RT-CLM-readonly-boundary](#rt-clm-readonly-boundary). SRC-1: `mempalace/mcp_server/protocol.py`, `mempalace/mcp_server/_guards.py`, `mempalace/palace/collection.py`.

2. **A hub may have executed a mutation but its reply is lost.** The proxy refuses local replay when the exception is an HTTP error or the request is classified mutating; eligible reads can fall back locally with degraded diagnostics. This is a routing invariant conditional on correct classification, not exactly-once execution or proof of remote success. Light stdio also translates to underlying names and leaves writer-lease ownership to the destination. See [RT-RTE-hub-fallback](#rt-rte-hub-fallback). SRC-1: `mempalace/mcp_proxy.py`, `mempalace/mcp_light_server.py`.

3. **Capture pressure exceeds a bounded queue, or shutdown cannot drain it.** Hermes logs and drops a turn on queue saturation; it joins the daemon worker for five seconds at shutdown and warns if still alive. Filing errors are logged, not durable retries. Automatic capture is therefore best effort, notwithstanding verbatim-recall intent. Hooks have a different recovery policy: after daemon submission failure they do not fall back and risk double-mining; direct capture instead starts the CLI with a per-target process guard. See [RT-RTE-hermes-capture](#rt-rte-hermes-capture), [RT-RTE-hook-ingest](#rt-rte-hook-ingest). SRC-1: `mempalace/integrations/hermes/__init__.py`, `mempalace/hooks_cli.py`.

4. **A stored task is launched from the wrong or dirty workspace.** The controlled CLI launcher rejects branch/commit mismatch, dirty Git state, ambiguous stored requests and incompatible addressed runner suffixes. It starts Codex or Claude with an argument list, releases its logstream handle, waits for the subprocess and propagates nonzero exit. This checks launch state; it neither proves the child follows the task nor constrains its eventual shell/filesystem capabilities. Manual paste of the handoff is an alternate path outside that launch enforcement. Patch delivery stores an artifact and event; it is not product installation. See [RT-RTE-task-launch](#rt-rte-task-launch), [RT-RTE-patch-delivery](#rt-rte-patch-delivery). SRC-1: `mempalace/cli/cmd_coord.py`, `mempalace/tasks.py`, `mempalace/logstream.py`.

Additional load-bearing controls are limited by their owners. MCP preflight orders explicit read-only, SQLite integrity, stale library, diverged vector index and peer-writer checks. The peer-writer check exempts independent logstream and some KG writes; the diverged-index check targets vector writes, not all state. The collection wrapper rejects unexpected collection names unless maintenance bypass flags are supplied. Embedder identity checking raises detected mismatches, but legacy unrecorded models can warn and continue, metadata-read failures can return without checking, server embedding reports its own identity, and repair can override it. These are compatibility-sensitive checks, not proof of universal embedding-space equivalence. SRC-1: `mempalace/mcp_server/protocol.py`, `mempalace/mcp_server/_guards.py`, `mempalace/palace/collection.py`.

HTTP adds Host/Origin checks and optional bearer authentication. Non-loopback binding requires a token unless an explicit insecure override delegates access control to a trusted fronting layer. That is a setup/transport policy, not authentication for local Python or shell writes, and the source alone cannot establish a production deployment guarantee. SRC-1: `mempalace/mcp_server/http.py`.

> if require_auth and srv.auth_token:
>     provided = handler.headers.get("Authorization", "")
>     if not hmac.compare_digest(provided, f"Bearer {srv.auth_token}"):
> --- `mempalace/mcp_server/http.py`

### Change admission and remaining scope

Content can enter through foreground tools, imported sources, automatic host turns, hooks and host memory-write mirroring. Setup additionally admits detected entities and origin classifications. People/projects can be edited interactively, `--yes` auto-accepts, and topics pass through without that interactive review. These are different admission mechanisms, not one human approval gate. See [RT-RTE-mcp-dispatch](#rt-rte-mcp-dispatch), [RT-RTE-init-detection](#rt-rte-init-detection). Memory transformations and revision policy remain the memory analyst's responsibility.

Backend registration admits executable capability changes through Python classes and installed entry points. Patch artifacts admit proposed changes into coordination state, not into the running product. See [RT-RTE-backend-registration](#rt-rte-backend-registration), [RT-RTE-patch-delivery](#rt-rte-patch-delivery). No exercised self-improvement claim follows from these pathways; proposal delivery does not establish installation or causally dependent subsequent operation.

This is a selective runtime baseline, not verification of all included implementations. Native Rust execution, non-Chroma storage engines and server-side embedders, media/code retrieval, replication, backup/repair internals, every legacy shell-hook variant and evaluator implementation remain available but not traced end to end here. Their backend-specific isolation, recovery, exact model identity and performance cannot be inferred from the Chroma/Hermes path. The boundary includes them; this report does not declare their behavior absent. Shipped evaluator existence is not live-loop evidence. SRC-1: `crates/README.md`, `mempalace/searcher/query.py`, `mempalace/backends/registry.py`, `mempalace/cli/cmd_mine.py`; boundary coverage supplies the broader inventory.

## Shared records

### Components

#### RT-CMP-minilm
Label: MiniLM embedding function

Source-native identity: the factory's `minilm` branch builds a subclass of Chroma's ONNX embedding function. Representational form: distributed-parametric pretrained model weights; wrapper configuration is symbolic. Storage substrate: dependency-managed ONNX artifacts and an in-process function/session cache. Parameters do not change through a training operation in the inspected factory/search/capture path. Exact external weight version is not established by the inspected wrapper; dependency internals are outside the supplied source. This branch is local, not a mutable network endpoint; changing config or external artifacts can change a later process's model. SRC-1: `mempalace/embedding.py`.

> ef_cls = _build_ef_class()
> ef = ef_cls(preferred_providers=providers, intra_op_num_threads=threads)
> --- `mempalace/embedding.py`

#### RT-CMP-embeddinggemma
Label: EmbeddingGemma ONNX

Source-native identity: `EmbeddinggemmaONNX`, selected by `embeddinggemma`. Representational form: distributed-parametric weights; numerical vectors are derived outputs, not training updates. Storage substrate: downloaded Hugging Face files, ONNX runtime session, process cache. The loader performs inference and can patch an ONNX computation graph; this is not evidence of learned parameter change during use. Download calls do not pin a revision, so exact weight version is not fixed by those calls. The repository endpoint can resolve changed artifacts on later acquisition. SRC-1: `mempalace/embedding.py`.

> model_path = hf_hub_download(
>     _EMBEDDINGGEMMA_REPO, subfolder="onnx", filename=_EMBEDDINGGEMMA_ONNX
> )
> --- `mempalace/embedding.py`

#### RT-CMP-embeddinggemma2
Label: EmbeddingGemma 2

Source-native identity: `EmbeddingGemma2EmbeddingFunction`. Representational form: distributed-parametric model; symbolic identity includes revision/dimension/modality configuration. Storage substrate: lazily loaded SentenceTransformer and local model artifacts. Default revision is an immutable model pin, but the user-configurable revision can differ; no actual installed model was supplied. The inspected model-load/encode path does not train weights. A mutable configured revision or external endpoint/artifact resolution remains distinct from the pinned default. SRC-1: `mempalace/embeddinggemma2.py`, `mempalace/embedding.py`.

> MODEL_ID = "google/embeddinggemma-2"
> DEFAULT_REVISION = "914f7f89142e33e77833254d9c9b90c3cef7303b"
> --- `mempalace/embeddinggemma2.py`

#### RT-CMP-openai-compat
Label: OpenAI-compatible embedding endpoint

Source-native identity: `OpenAICompatEmbeddingFunction` selected by `openai-compat`. Representational form: provider-owned distributed-parametric model, with symbolic URL/model/key configuration. Storage substrate: opaque provider weights/state; local object cache keyed by URL, model and key fingerprint. Parameter changes during provider operation are uninspected; this client requests embeddings, not training. Exact weight revision is not pinned by a model string. A mutable endpoint can serve another model under the same identifier, and equal vector dimension does not establish equivalence. SRC-1: `mempalace/embedding.py`.

> payload = {"model": self._model, "input": batch, "encoding_format": "float"}
> --- `mempalace/embedding.py`

#### RT-CMP-llm-provider
Label: Setup LLM provider

Source-native identity: `LLMProvider` and Ollama/OpenAI-compatible/Anthropic classifiers used by setup. Representational form: distributed-parametric generation behind symbolic provider/model settings. Storage substrate: external service or local provider-owned model; MemPalace stores request/response data rather than weights. No client-side weight update is wired in the inspected classifier; provider parameter changes are uninspected. Exact weights are not pinned by model names. OpenAI-compatible `auto` explicitly resolves to the first served model and can follow endpoint swaps. These are setup classifiers, not the external foreground agent model. SRC-1: `mempalace/llm_client.py`, `mempalace/cli/cmd_init.py`.

> if self.model == "auto":
>     if not models:
>         return False, f"{self.endpoint} lists no models to pick from"
>     self.model = models[0]
> --- `mempalace/llm_client.py`

### Operative objects

#### RT-OBJ-task-request
Label: Task request body

Source-native identity: `task.request` goal/definition-of-done/delivery body. Representational form: natural-language content interpreted by the addressed worker; branch, base commit and correlation metadata are separate symbolic routing/control fields. Storage substrate: logstream SQLite event body. The launcher supplies a pointer prompt rather than the full body, so successful task reload and compliance depend on the runner's MemPalace access. SRC-1: `mempalace/tasks.py`, `mempalace/cli/cmd_coord.py`, `mempalace/logstream.py`.

> "Open MemPalace task {correlation_id} as {agent}. "
> "Claim it, follow its exact definition of done, and deliver through the logstream."
> --- `mempalace/tasks.py`

#### RT-OBJ-patch-artifact
Label: Patch artifact

Source-native identity: logstream artifact of kind `patch`. Representational form: symbolic diff for a patch consumer, stored without application here; accompanying event body is natural-language coordination. Storage substrate: SQLite artifacts and linked events. `patch.ready` indicates a delivered proposal, not accepted or installed production code. SRC-1: `mempalace/logstream.py`, `mempalace/mcp_server/tools_coord.py`.

> artifact = self.put_artifact(
>     kind="patch",
>     content=content,
>     created_by=from_agent,
>     metadata=metadata,
> )
> --- `mempalace/logstream.py`

### Routes

#### RT-RTE-hermes-capture
Label: Hermes turn capture

Endpoints/progression: initialized host callback → bounded worker queue → `_file_turn` → `file_conversation_exchange` → Chroma drawer. Principal: external host session; identities include session ID, source `hermes-session:...`, agent `hermes`, wing/room and time-derived drawer ID. Code owns enqueue, classification and execution; the foreground model does not decide admission for each completed turn. Context/state/effects: user plus assistant text becomes durable conversation material; worker state is in-process, not a durable spool. Source/native metadata and the collection lock coordinate this adapter's scans/writes, not all external processes. SRC-1: `mempalace/integrations/hermes/__init__.py`, `mempalace/convo_miner.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `sync_turn` returns no persistence acknowledgement; filing later returns an ID internally.
- Later read-back: stored turns can reach later search/prefetch and wake-up consumers through the same configured collection.
- Delegated visibility: `on_delegation` queues the task/result pair under the parent session, not the entire child context.
- Selection predicate: initialized non-cron provider and nonempty normalized user/assistant content; wing classification uses adapter configuration.
- Invalidation or expiry: no automatic retention expiry in this inspected callback; session switches repoint subsequent writes; external memory maintenance is a separate route.
- Activation or effect: drawer upsert is wired; later behavioral dependence on the turn is unobserved.
- Evidence limits: no supplied host callback trace, queue drain trace or successful backend write; saturation and logged filing errors prevent a lossless-capture conclusion.

Admission: trigger is a host-completed turn or delegation callback. The host supplies content; software admits it without per-content human veto. Cron/flush skipping, readiness and queue bounds can reject it. This is open session operation, not a curriculum or candidate-improvement experiment; no answer oracle is used. Recovery is best effort: worker drains while stopping but shutdown joins only five seconds. Starting/configuring the integration is not human approval of every retained turn. The guidance applied here is procedural filing/routing, not a theory criticism/revision loop.

> except queue.Full:
>     # Loud, not silent: the verbatim invariant is what mempalace sells.
>     # If the queue saturates we want operators to see it.
>     logger.warning(
>         "MemPalace worker queue full (maxsize=%d) — turn dropped; "
>         "writes likely stalled on disk or ChromaDB",
>         self.WORKER_QUEUE_MAX,
>     )
> --- `mempalace/integrations/hermes/__init__.py`

> collection.upsert(ids=[drawer_id], documents=[text], metadatas=[metadata])
> return drawer_id
> --- `mempalace/convo_miner.py`

#### RT-RTE-palace-recall
Label: Palace search and context delivery

Endpoints/progression: agent query through MCP or host prefetch → search handler → filtered/ranked drawers → result envelope → JSON tool text or host context string. Principal: foreground caller or host; next-step owner is deterministic retrieval code until the result returns, then the host/agent. Selection uses query embeddings plus symbolic filters and lexical/closet scoring, not a generative answer model or answer oracle. Direct API/CLI search and DSH startup `wake-up` are materially different consumption paths; startup supply is not request-driven semantic selection. SRC-1: `mempalace/mcp_server/tools_read.py`, `mempalace/searcher/query.py`, `mempalace/searcher/candidates.py`, `mempalace/mcp_light_server.py`, `mempalace/integrations/hermes/__init__.py`, `.dsh-plugin/lib/recall.js`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: selected text/metadata in a search result, serialized to MCP text; Hermes prefetch renders returned text with wing/room tags.
- Later read-back: selects previously retained drawers; DSH startup also supplies wake-up text and reload guidance across sessions.
- Delegated visibility: inapplicable — retrieval alone launches no child; downstream visibility depends on the host or separate task route.
- Selection predicate: query, result limit, wing/room/source/date/distance controls and candidate strategy; closets boost direct drawer candidates, hydration selects lexical matches and neighbors.
- Invalidation or expiry: returned results are current-invocation values; DSH keeps a session cache until agent disposal, while Hermes refreshes wake-up state asynchronously for later sessions.
- Activation or effect: result/context delivery is implemented; external model compliance and answer benefit are unobserved.
- Evidence limits: no supplied search execution or answer trace; result text can be a selected/truncated passage rather than a full drawer, and server/provider/backend variants remain distinct.

Working-context control: requested retrieval brings retained text into a later invocation; prefetch is a host-requested anticipatory supply. DSH independently reads at session start, registers agent-local cached context and waits once within a time budget. It neither promises first-call delivery after timeout nor owns host compaction. Hermes `on_pre_compress` is a no-op, not an implemented summary/removal mechanism. The frame analogy applies only to DSH agent-local registrations unwinding; no source evidence establishes MemPalace control of an external child model window.

Recovery: search can retry a transient index error once after cache reset; unusable vectors can route to lexical fallback, but media/code searches refuse that state. Absent closets degrade to drawer-only search. These are result-availability mechanisms, not guarantees of correct answers. The light wrapper adds confidence/recency and tunnel suggestions without reordering the searcher's hits. SRC-1: `mempalace/mcp_server/tools_read.py`, `mempalace/searcher/query.py`, `mempalace/mcp_light_server.py`.

> result = search_memories(
>     query,
>     palace_path=self._palace_path,
>     n_results=n,
> )
> --- `mempalace/integrations/hermes/__init__.py`

> hit["text"] = expanded
> hit["drawer_index"] = best_index
> hit["total_drawers"] = len(ordered_docs)
> --- `mempalace/searcher/candidates.py`

> memory.pending !== undefined && !memory.waited && settings.firstAssemblyBudgetMs > 0 && !signal?.aborted
> --- `.dsh-plugin/lib/recall.js`

#### RT-RTE-mcp-dispatch
Label: MCP request dispatch and content admission

Endpoints/progression: JSON-RPC client → tool lookup/PQL classification → preflight gates → named handler → backend/coordination effect → text response. Owner: server code; the client chooses operation/content, possibly under model or human control. Symbolic dispatch/rules differ from natural-language supplied drawer content. The full and local light server gate explicit read-only and other refusal conditions; light hub forwarding skips only the local writer competition because the destination owns the lease. SRC-1: `mempalace/mcp_server/protocol.py`, `mempalace/mcp_server/_guards.py`, `mempalace/mcp_light_server.py`, `mempalace/mcp_server/tools_write.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON-RPC refusal or serialized handler result; drawer addition returns IDs/chunk counts or a failure/already-existing result.
- Later read-back: successful drawer writes are readable through search/direct drawer tools; coordination/configuration writes have their own later consumers.
- Delegated visibility: coordination can publish addressed events/artifacts; ordinary drawer writes do not launch or isolate a worker.
- Selection predicate: tool name and parsed operation plus server read-only, integrity, library/index and writer state; handler-specific content/name validation follows.
- Invalidation or expiry: tool-call state ends with its response; durable content persists until explicit update/delete or other maintenance; server caches can be invalidated after writes/reconnect.
- Activation or effect: validated handlers perform writes or return reads; MCP delivery does not establish model obedience or deployment isolation.
- Evidence limits: no current grant configuration or deployment supplied; local APIs/CLI/callbacks and plugins are outside this server-name gate, and read-only permits recovery disk effects.

Admission roles/mode: the caller proposes a write in an open request; code admits or rejects structurally and by runtime state. Caller identity alone does not establish human authorship or approval. `tool_add_drawer` sanitizes, computes content identity, checks prior IDs, chunks large content, upserts and probes read-back; these are storage checks, not truth assessment. No answer oracle or human confirmation step is shown in that handler. Updates/deletes are separate explicit operations, not automatic rollback of a mistaken belief. Backend atomicity and read visibility are required external contracts; a probe of an ID does not prove vector recall completeness. SRC-1: `mempalace/mcp_server/tools_write.py`.

> underlying_name = _classify_underlying_tool(tool_name, arguments)
> refusal = mcp_server._mcp_tool_preflight_refusal(req_id, underlying_name)
> if refusal is not None:
>     return refusal
> --- `mempalace/mcp_light_server.py`

> col.upsert(
>     ids=[drawer_id],
>     documents=[content],
>     metadatas=[{**base_meta, "chunk_index": 0}],
> )
> inserted = col.get(ids=[drawer_id], include=[])
> --- `mempalace/mcp_server/tools_write.py`

#### RT-RTE-hub-fallback
Label: Hub forwarding and fallback

Endpoints/progression: plain stdio proxy → discovered hub HTTP endpoint → reply; selected failures → local server or explicit error. Owner: proxy code. State includes the request ID, palace path, hub target and lazy local module. Effects occur at the selected destination; the proxy does not know whether a failed remote mutation already committed. SRC-1: `mempalace/mcp_proxy.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: forwarded reply, local reply marked degraded, or proxy error.
- Later read-back: inapplicable — routing itself creates no retained knowledge; the forwarded handler may write/read persistent state.
- Delegated visibility: request crosses into a separate hub process; this is transport delegation, not a separately instructed agent.
- Selection predicate: live hub target first; on failure, HTTP errors or classified mutations disallow replay, while eligible reads may use the local server.
- Invalidation or expiry: hub selection is resolved per request; local server is loaded lazily and kept within the proxy process.
- Activation or effect: wired destination selection and refusal to replay potentially executed writes; exactly-once success is not established.
- Evidence limits: remote deployment and failure traces were not supplied; request classification and remote storage semantics bound the guarantee.

Guarantee owner/enforcement: `_handle` controls fallback. Guarantee strength: invariant, conditional on the mutating classifier. Covered paths: this proxy's caught hub errors; alternates include direct full server, HTTP callers and local API writes. Required external contract: classification correctly identifies state-changing calls. This controls replay, not human approval or authentication.

> if isinstance(exc, urllib.error.HTTPError) or module._request_is_mutating(request):
>     return _proxy_error(request, base_url, exc)
> --- `mempalace/mcp_proxy.py`

#### RT-RTE-hook-ingest
Label: Hook transcript ingest

Endpoints/progression: host Stop/PreCompact/end hook → validated transcript path/config → chosen routing → daemon mine job or detached CLI mine → retained conversations. Principal: host lifecycle; code owns path validation, routing and spawn/submission; miner performs normalization/chunking and storage. This differs from a synchronous confirmed save. SRC-1: `mempalace/hooks_cli.py`, `mempalace/cli/cmd_mine.py`, `mempalace/write_routing.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: hook log/output after submission or spawn, not a verified final retained transcript.
- Later read-back: successful conversation mining supplies later palace search; mere subprocess launch does not establish it.
- Delegated visibility: daemon job or subprocess receives source path, mode and wing, not an isolated model task.
- Selection predicate: acceptable file/path/size/config, hook lifecycle policy and direct/prefer/require routing; daemon submissions use a source/mode dedupe key.
- Invalidation or expiry: direct spawning uses a per-target process guard; routine transcript state is separately tracked; detailed miner invalidation belongs to memory analysis.
- Activation or effect: mine submission/spawn is implemented, final persistence and later behavioral effect unobserved.
- Evidence limits: no supplied hook/daemon execution; all host shell variants were not individually traced and this route cannot guarantee capture completion.

Admission/recovery: software admits source-derived content after a host trigger; no per-content human decision is shown. `require` chooses blocked rather than direct when a daemon is unavailable and cannot start; `prefer` can fall back before submission. Once the daemon path is chosen, its submission-error branch logs and returns without direct retry. The shared routing module alone does not prove every caller adopts it; this hook and CLI mine visibly do. Open capture mode, no answer oracle; routing guidance controls executor choice, not truth or revision selection. SRC-1: `mempalace/write_routing.py`, `mempalace/hooks_cli.py`, `mempalace/cli/cmd_mine.py`.

> except Exception as exc:
>     # Daemon accepted context — don't fall back (would double-mine).
>     _log(f"Daemon transcript ingest failed: {exc}")
> return
> --- `mempalace/hooks_cli.py`

#### RT-RTE-init-detection
Label: Setup origin and entity admission

Endpoints/progression: CLI init → heuristic samples plus optional LLM classification → merged origin data → entity discovery/confirmation → project file and global registry. Principal: CLI caller. Code preserves heuristic dialogue/confidence while adding LLM persona/platform/user fields; humans can edit people/projects interactively, and the `yes` flag bypasses that review. Topics follow a different automatic admission rule. SRC-1: `mempalace/cli/cmd_init.py`, `mempalace/cli/_common.py`, `mempalace/entity_detector.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: setup messages, detection/confirmation results and filesystem writes or warnings.
- Later read-back: origin is persisted in `.mempalace/origin.json`; confirmed entities are saved to project `entities.json` and merged into the miner's known-entity registry.
- Delegated visibility: optional provider receives sampled corpus context; provider state retention is external and uninspected.
- Selection predicate: readable corpus samples, provider availability/configuration and consent conditions; human review applies to people/projects, not all detected fields.
- Invalidation or expiry: explicit redetect-origin can overwrite origin state; files can be inspected/edited; automatic rollback of erroneous classifications is not established in this trace.
- Activation or effect: origin result enters the current entity-discovery call and entity registry supplies later mining; accuracy/benefit unobserved.
- Evidence limits: provider implementation and output accuracy uninspected; origin write failure still returns an in-memory result, so persistence must not be inferred from detection alone.

Admission roles/oracle/mode: heuristic/model propose classified fields, code merges them, user can edit people/projects or auto-accept via `--yes`. Topics pass through. This is open setup over a user's corpus, not an oracle-scored improvement experiment; model judgment is not an answer oracle. External-provider consent is conditional on provider/key provenance, with explicit flags able to opt in; it is neither universal per-content review nor a rule for embedding APIs. Guidance consists of fixed classifier/merge policy. This inspected route does not formulate and iteratively criticize a method theory; classification output is not evidence of such a loop. SRC-1: `mempalace/cli/cmd_init.py`, `mempalace/cli/_common.py`, `mempalace/entity_detector.py`.

> Topics are not surfaced for interactive review — they come from the
> LLM-refined ``TOPIC`` bucket and are passed through verbatim.
> --- `mempalace/entity_detector.py`

#### RT-RTE-task-launch
Label: Controlled task launch

Endpoints/progression: task event/file → validation of addressed identity and clean workspace → pointer handoff → external runner subprocess → exit. Principal: launching CLI caller; symbolic validation is code-owned, task goal/done/delivery are interpreted by the external agent. Correlation ID, addressed agent, branch and base commit link task and workspace. The launcher closes its SQLite handle before starting the child. SRC-1: `mempalace/cli/cmd_coord.py`, `mempalace/tasks.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: launch banner followed by subprocess lifetime/exit; nonzero child exit propagates.
- Later read-back: runner is instructed to reload the stored task by correlation ID; actual reload/compliance was not observed.
- Delegated visibility: subprocess receives a pointer prompt and workspace, not the entire parent's conversation; external host owns its model context, tools and shell grants.
- Selection predicate: unique valid task, concrete compatible agent identity, existing workspace, exact task branch/resolved commit and clean Git status.
- Invalidation or expiry: inapplicable — launch validates starting state but establishes no task expiry or cancellation protocol in this inspected command.
- Activation or effect: external process starts only after validation; this does not enforce definition-of-done compliance or install its result.
- Evidence limits: no runner execution, sandbox configuration or task completion trace; manual paste bypasses this controlled launch check.

Admission/decisions: caller supplies the goal, expected completion criterion and launch request; code can veto structural/workspace errors; external runner determines execution steps. Definition of done is guidance, not necessarily an answer oracle; no reference-answer comparator is shown here. Operating mode is an open task. A proposed patch crosses back through [RT-RTE-patch-delivery](#rt-rte-patch-delivery), not through an automatic product-update gate. Guarantee owner: CLI validator; enforcement point: before `subprocess.run`; guarantee strength: protocol for the controlled launch path. Required external contracts: Git resolves the commit/status correctly, executable resolution finds the intended runner, and the runner can access the logstream.

> if git("status", "--porcelain"):
>     raise ValueError(
>         "workspace has uncommitted changes; controlled launch requires a clean checkout"
>     )
> --- `mempalace/cli/cmd_coord.py`

#### RT-RTE-patch-delivery
Label: Patch proposal delivery

Endpoints/progression: worker/client patch content → artifact storage → linked `patch.ready` event → later recipient event/artifact read. Code owns structural persistence; recipient owns any later decision to apply or reject. SRC-1: `mempalace/mcp_server/tools_coord.py`, `mempalace/logstream.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: success with artifact and event, or validation error.
- Later read-back: event/artifact APIs return the addressed proposal and exact stored content to later callers.
- Delegated visibility: stream, room, destination and correlation fields route the proposal; actual recipient polling/consumption is unobserved.
- Selection predicate: valid routing/event fields and stored referenced artifact; event insertion checks artifact existence.
- Invalidation or expiry: inapplicable — inspected submission does not apply a patch, replace product code or establish an expiry policy.
- Activation or effect: proposal becomes coordination state; installation and subsequent behavior are unestablished.
- Evidence limits: two sequential writes are not evidence of one atomic install; external reviewer/application path and executed outcome were not supplied.

Admission: client proposes a code change, software admits its artifact/event to the logstream, not the product. The recipient can decide later but no built-in application/veto/rollback mechanism is established by these functions. Source guidance asks workers to deliver patches or blocked/failed evidence. Mode: open delegated work; no answer oracle in submission. Artifact existence prevents a dangling ready event, not an incorrect patch. A stored proposal is recoverable by artifact read; product rollback remains external to this inspected delivery route.

> event = self.append_event(
>     type="patch.ready",
> --- `mempalace/logstream.py`

#### RT-RTE-backend-registration
Label: Backend capability registration

Endpoints/progression: explicit Python class registration or installed backend entry point → registry → cached backend selection → collection implementation. Owner: process code/installation operator; class methods execute as Python capability code, not interpreted natural-language guidance. SRC-1: `mempalace/backends/registry.py`, `mempalace/palace/collection.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: registration alters the registry; subsequent backend selection can return an instance of that class.
- Later read-back: inapplicable — process registry/cache is capability state, not use-accumulated knowledge; installed entry points are rediscovered on a later process.
- Delegated visibility: backend methods receive palace and collection arguments in-process; plugin external effects depend on their implementation.
- Selection predicate: explicit registration takes precedence; discovery loads entry points once and accepts BaseBackend subclasses.
- Invalidation or expiry: registration invalidates an existing cached instance; process restart reloads installed capability definitions.
- Activation or effect: selected class supplies storage behavior; no deployed plugin or exercised effect was supplied.
- Evidence limits: class-shape checking does not establish isolation, trustworthiness or backend contract correctness; arbitrary plugin internals are not in SRC-1.

Admission roles/mode: installers or callers supply code; registry decides loadability/type and precedence, not semantic safety; no per-content human approval or answer oracle. Failed entry-point load is logged/skipped. Unregister/re-register provides process-level replacement, not rollback of backend data effects. Required external contract: each backend implements compatible collection/embedding/transaction behavior. The collection wrapper can drop unsupported `options`, so a third-party backend must not inherit a claimed genuine storage read-only guarantee merely from the requested flag.

> cls = ep.load()
> --- `mempalace/backends/registry.py`

> if not isinstance(cls, type) or not issubclass(cls, BaseBackend):
> --- `mempalace/backends/registry.py`

### Claims

#### RT-CLM-recall-protocol
Label: Search before answer and quote exactly

Claimed operation: the shipped skill asks an agent to search relevant memory before answering prior-work questions, avoid greenfield reflex searches, quote rather than paraphrase and record session continuity. Source: SRC-1 `skills/mempalace-recall/SKILL.md`; doctrine/design, not an observed agent trace. Guarantee strength: policy. Owner/enforcement: foreground agent under host skill loading; compliance is not enforced by the storage/search handler. Doctrine conclusion status: claimed. Operation conclusion status: uninspected. The queue-drop and search-truncation witnesses prevent promoting this policy into lossless capture, complete retrieval or reliable verbatim answering.

> 4. Return the drawer's **verbatim** text. Never summarize or paraphrase
>    stored content — quoting the exact words is the point of the system.
> --- `skills/mempalace-recall/SKILL.md`

#### RT-CLM-readonly-boundary
Label: MCP read-only capability boundary

Claimed operation: an operator-set server mode rejects state-changing tool requests at dispatch, not just discovery. Source: SRC-1 `mempalace/mcp_server/protocol.py`, `mempalace/mcp_server/_guards.py`, `mempalace/mcp_light_server.py`. Guarantee owner: MCP dispatcher; enforcement: refused-name set after underlying light-tool classification. Guarantee strength: protocol. Implementation conclusion status: wired. Operation conclusion status: uninspected. Covered paths: local MCP tool calls and the light translation's local preflight; remote destination has its own configuration. Alternates: direct APIs, CLI, callback writes, extensions and repair. Required external contract: accurate tool classification and backend behavior. The stronger claim that read-only prevents every disk mutation is contradicted by the explicit recovery exception and compatibility fallback.

> if not _READ_ONLY or tool_name not in _READ_ONLY_REFUSED_TOOLS:
>     return None
> --- `mempalace/mcp_server/protocol.py`

> # stale index. This set means "refuse what a client asked to change", not
> # "nothing past here touches the disk" -- opening the palace or the knowledge
> # graph materialises files on its own, which no name-based gate can express.
> --- `mempalace/mcp_server/_guards.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-agent-context
Label: Retained text into host model context

Consumer: external foreground agent; channel: Hermes system prompt/prefetch return, DSH agent-local system-prompt providers, or MCP tool-result text. Force: supplied context and imperative recall instructions, not an executable truth gate or demonstrated compliance. Horizon: previously retained material can reach later turns/sessions; DSH cached section lives with its agent context. Content and instructions can shape answers if consumed, but provider methods returning strings alone do not prove host insertion or causal activation. SRC-1: `mempalace/integrations/hermes/__init__.py`, `.dsh-plugin/lib/recall.js`, `mempalace/mcp_server/protocol.py`, `skills/mempalace-recall/SKILL.md`.

> parts = ["# MemPalace context"]
> if self._identity:
>     parts.append(self._identity)
> if self._wake_up_cache:
>     parts.append(self._wake_up_cache)
> return "\n\n".join(parts)
> --- `mempalace/integrations/hermes/__init__.py`

#### RT-BAP-task-handoff
Label: Stored task into external worker instructions

Consumer: Codex/Claude worker invoked by the controlled launcher, or manually addressed agent. Channel: one-line handoff pointing to a stored task; worker must reload task body. Force: natural-language goal, definition of done and delivery request; symbolic branch/commit checks constrain controlled startup but not future model actions. Horizon: task and proposal persist across invocations in the logstream. This is a behavioral request and subprocess capability, not evidence that stored task content was loaded, obeyed, or that the patch entered production. SRC-1: `mempalace/tasks.py`, `mempalace/cli/cmd_coord.py`.

> return ["codex", "exec", "--cd", str(workspace), prompt], {}
> --- `mempalace/cli/cmd_coord.py`

## Annotations

none
