---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Memori runtime baseline: Python and TypeScript interception, service-dependent augmentation, and shipped agent-host memory routes."
run-id: AAS-2026-10-17-memori-fd4a0418c09b-01
reviewed-boundary: 574b1ea3e876f100ef82c37817d603eb7e258e59
---

# Memori runtime report

## Runtime account

### Evidence and consequential work

Memori surrounds model or agent-host invocations with memory production and consumption. It does not take ownership of the enclosing agent's task loop. The ordinary SDK path automatically retrieves context before a registered model call and captures the response afterwards. Shipped host integrations instead expose agent-selected recall, completed-turn capture and post-compaction restoration. These are different decision owners, not interchangeable implementations of an unconditional memory guarantee. See [RT-RTE-python-invocation](#rt-rte-python-invocation), [RT-RTE-typescript-hooks](#rt-rte-typescript-hooks), [RT-RTE-hermes-provider](#rt-rte-hermes-provider), [RT-RTE-claude-skill](#rt-rte-claude-skill) and [RT-RTE-openclaw-hooks](#rt-rte-openclaw-hooks).

All source evidence here is SRC-1 at the boundary's revision. Newly inspected coverage includes invocation and iterator implementations, conversation replay, Python writer and augmentation manager/registry, TypeScript recall/persistence engines and integration base, Rust augmentation and worker implementation, embedding loaders, and Claude Code, Hermes and OpenClaw integration paths cited below. These supply implementation and, for prompts/comments, doctrine/design evidence. No target execution, provider call, test or example was run. No supplied execution evidence was established. Activation, operational reliability and benefit therefore remain unobserved. Hosted extraction, hosted storage policy and provider internals retain the access limits in [boundary](boundary.md#boundary-and-evidence).

### Ordinary invocation: SQLite and a registered OpenAI client

The shipped caller creates a SQLAlchemy SQLite session factory, registers an OpenAI client, sets entity `user-123` and process `my-app`, and builds storage. It then makes three separate `gpt-4o-mini` calls before waiting for augmentation. This establishes the intended producer-to-consumer sequence, not a recorded successful recall. In particular, the wait is after the queries: the example does not synchronize the first turn's derived facts before the second turn (SRC-1: `examples/sqlite/main.py`).

> mem = Memori(conn=Session).llm.register(client)
> mem.attribution(entity_id="user-123", process_id="my-app")
> mem.config.storage.build()
> --- `examples/sqlite/main.py`

The principal is the calling application. It supplies credentials, attribution, model and messages. `Memori` owns mutable configuration, session UUID and caches; an explicit connection selects non-cloud mode. Registration replaces selected methods on the supplied client. OpenAI chat completions, beta parse and Responses create receive wrappers; original methods remain reachable on private-looking attributes. An unrelated client or a caller using a saved original is not intercepted (SRC-1: `memori/__init__.py`, `memori/llm/clients/direct.py`).

The wrapper first configures streaming usage and retrieves facts using the extracted user query. Entity and storage availability gate local retrieval. Cloud mode delegates recall to a service; BYODB selects the configured native adapter or Python recall. A relevance threshold filters facts before formatting. Fact content and associated summaries become natural-language context in provider-specific system/instruction channels. Conversation replay then adds stored history. The next-step owner is the original provider method, followed by the enclosing application's consumer of the returned response; Memori does not select subsequent agent actions (SRC-1: `memori/llm/invoke/invoke.py`, `memori/llm/pipelines/recall_injection.py`, `memori/llm/pipelines/conversation_injection.py`).

> kwargs = inject_conversation_messages(
>     self,
>     inject_recalled_facts(self, self.configure_for_streaming_usage(kwargs)),
> )
> --- `memori/llm/invoke/invoke.py:28-31`

After a non-streaming response, request formatting records the injected-history count for adapter consumption, constructs conversation messages through the provider adapter, and invokes the memory manager. The adapter-specific completeness and removal behavior are not uniformly established here (SRC-1: `memori/llm/helpers/serialization.py`, `memori/memory/_conversation_messages.py`). That manager removes system-role messages from its `messages` list and selects local writer or cloud persistence. The local writer creates/resolves entity, process, session and conversation identifiers, appends messages, flushes and commits through the adapter. Its limited transaction-restart retry is not a general retry of the model call. The cloud manager requires a 201 response after configured retry attempts, then optionally mirrors messages locally. Persistence exceptions can prevent return even after inference has succeeded (SRC-1: `memori/llm/pipelines/post_invoke.py`, `memori/memory/_manager.py`, `memori/memory/_writer.py`).

Augmentation is a separate follow-on dispatch. The returned provider answer is not a receipt proving that facts have been derived or stored. Python cloud dispatch uses a thread-pool task when configured, logging background failures. BYODB selects native submission or Python augmentation. The latter runs enabled registered classes under a semaphore, then schedules accumulated writes for a database writer. Service-dependent derivation remains present even in BYODB: both Python advanced augmentation and Rust's non-mock augmentation call a Memori API. Local storage is not local derivation (SRC-1: `memori/memory/augmentation/_handler.py`, `memori/memory/augmentation/_manager.py`, `memori/memory/augmentation/augmentations/memori/_augmentation.py`, `core/src/augmentation/pipeline.rs`). See [RT-RTE-augmentation-admission](#rt-rte-augmentation-admission).

### Forcing cases and alternate paths

Four forcing comparisons constrain this baseline:

1. **Streaming is not the non-streaming completion path.** The generic Python iterator persists the accumulated response only on iterator exhaustion. Neither its exhaustion handler nor context-manager exit calls `handle_post_response`; the inspected generic iterator therefore does not dispatch that function's augmentation. Early stop has no exhaustion write in this implementation. This does not cover every framework-specific stream wrapper (SRC-1: `memori/llm/invoke/iterator.py`, `memori/llm/invoke/invoke.py`). See [RT-RTE-stream-exhaustion](#rt-rte-stream-exhaustion).
2. **A successful SDK answer is not a successful memory operation.** TypeScript recall catches failure and returns the original request; persistence catches failure and returns the response; cloud augmentation is fire-and-forget. Even its BYODB persistence implementation writes a batch, despite the file comment saying it is skipped. The executable branch controls this account (SRC-1: `memori-ts/src/engines/recall.ts`, `memori-ts/src/engines/persistence.ts`, `memori-ts/src/engines/augmentation.ts`).
3. **Host recall is not universally automatic.** Hermes `prefetch` returns an empty string and its prompt asks for intentional tool use. Claude Code's skill instead asks for recall on essentially every non-trivial turn, via Bash. Neither instruction text proves the foreground agent complied. OpenClaw installs prompt-building and end hooks, but conversation access gates capture, not every memory tool (SRC-1: `integrations/hermes/src/memori_hermes/__init__.py`, `integrations/claude-code/SKILL.md`, `integrations/openclaw/src/index.ts`).
4. **Flush completion is not semantic or durable success.** Rust jobs return unit after logging service or storage failures. `wait_for_augmentation` maps runtime drain to a boolean, not individual write outcomes. Furthermore, `submit` sends the job before incrementing `outstanding`; the inspected ordering does not by itself establish a race-free accounting invariant under a fast handler. No failure was executed or observed (SRC-1: `core/src/lib.rs`, `core/src/runtime/worker.rs`).

Enumerated alternate surfaces are registered direct clients and framework models, sync/async invocations, generic iterator and other streaming wrappers, explicit recall/capture APIs, TypeScript middleware and synthetic integration payloads, host tool callbacks, and the Claude Code shell CLI. The OpenAI wrapper retains original methods, so Memori cannot enforce universal mediation of provider calls. Provider-native tool execution, shell execution beyond the shipped CLI, host sub-agent scheduling, remote workers and manual host context manipulation remain enclosing-runtime responsibilities, not established Memori controls. The native `execute` entry point accepts `ping` and rejects other commands; its name does not establish arbitrary shell access (SRC-1: `memori/__init__.py`, `memori/llm/clients/direct.py`, `memori/llm/invoke/invoke.py`, `memori-ts/src/integrations/base.ts`, `integrations/claude-code/index.ts`, `core/src/lib.rs`). Framework-specific wrappers, native binding conversions, database drivers and evaluators are available but not exhaustively traced here; no uniform guarantee across those paths is inferred. The documented hosted MCP surface has a separate intentional-use and durable-only admission policy, unlike the Claude Code ambient-capture skill. Its server implementation is unavailable: [RT-RTE-mcp-guidance](#rt-rte-mcp-guidance) establishes the requested client policy, not server enforcement.

### Control, working context and guarantees

**Relevance-controlled delivery.** Owner: SDK recall pipeline. Enforcement: explicit query/entity gates, score threshold and construction of the provider request. Strength: protocol for the inspected request-building branch; the text asking the model to use context only when relevant is policy, not an invariant of model behavior. Covered paths: Python invocation and TypeScript before hook. Alternate paths: manual recall returns data without this same injection step; host tool recall uses host prompts and tool results. External contract: provider or Axon accepts and transmits the constructed context. Implementation conclusion status: wired. Operation conclusion status: uninspected. See [RT-BAP-recalled-context](#rt-bap-recalled-context) and the route records.

**Background completion.** Owner: augmentation managers and native worker. Enforcement: queue admission, semaphore, outstanding-job accounting and wait helpers. Strength: best effort as an end-to-end memory guarantee. Rust admission validates nonempty entity and message/content, uses a bounded channel and returns QueueFull/not-running errors. Queue capacity is 512 and concurrency is 2 for the augmentation runtime, but the SDK also has outer dispatch layers. Cloud fire-and-forget, iterator non-dispatch and swallowed worker failures defeat a stronger all-path promise. Required contracts: process remains alive, handlers and storage complete, accounting remains correct, service accepts requests. Implementation conclusion status: wired. Operation conclusion status: uninspected (SRC-1: `core/src/lib.rs`, `core/src/runtime/worker.rs`, `memori/memory/augmentation/_handler.py`, `memori/memory/augmentation/_manager.py`).

> match tx.try_send(job) {
>     Ok(()) => {
>         drop(job_tx);
>         self.inner.outstanding.fetch_add(1, Ordering::SeqCst);
>         Ok(())
>     }
> --- `core/src/runtime/worker.rs`

**Namespace and access controls.** Owner: application attribution plus hosted authentication/host grants. Local enforcement inspected here validates identifier shape and sends identifiers to retrieval/storage; it does not prove authorization between tenants. OpenClaw checks configured API key/entity and a version-sensitive `allowConversationAccess` setting before installing capture. Capability surface includes recall, compaction, capture and feedback tools; the actual grant set depends on host configuration, credentials and registration. The deployed isolation envelope is uninspected. Strength: no claimed deployment guarantee from these client checks. Implementation conclusion status: wired. Operation conclusion status: uninspected. Neither process isolation nor a Memori-wide approval gate follows from API-key presence (SRC-1: `memori/__init__.py`, `integrations/openclaw/src/index.ts`, `integrations/hermes/src/memori_hermes/__init__.py`).

Working-context control is concrete but bounded: code brings facts and history into model requests, filters by score, drops malformed replayed tool sequences and normalizes roles. Python OpenAI-compatible replay omits tool messages and empty assistant messages because tool-call linkage was not retained in those rows. The retained history is not equivalent to the original execution trace. Agent compaction tools request a service-generated resume representation and recent-message tail after host context loss; the inspected clients do not themselves pop host contexts or prove compaction happened. Host sub-agent frame isolation and model-window trimming remain uninspected. This is selective restoration by value, not a pointer that the model can automatically dereference (SRC-1: `memori/llm/pipelines/conversation_injection.py`, `memori-ts/src/engines/recall.ts`, `integrations/openclaw/src/tools/memori-compaction.ts`).

### Change admission and model boundary

The material automatic change route is admission of service-derived memory for later recall, not SDK self-rewriting. [RT-RTE-augmentation-admission](#rt-rte-augmentation-admission) records who proposes, who writes, the lack of an inspected per-item human approval step, and the service-policy gap. Python's augmentation registry also admits executable classes chosen by application imports; the manager instantiates and runs enabled entries. That is an in-process extension surface, not evidence that an agent dynamically installs its own capabilities. Product/build/deployment change admission is not traced beyond this surface; CI configuration was not inspected, so no automatic production-improvement claim is made (SRC-1: `memori/memory/augmentation/_registry.py`, `memori/memory/augmentation/_manager.py`). See [RT-RTE-augmentation-extension](#rt-rte-augmentation-extension).

The model boundaries are separate: caller-selected inference, native embedding, optional remote embedding, and opaque hosted derivation. Their parameter fixity and endpoint limitations are recorded separately below. Retained text changing later context is not evidence that any model weights were updated. No answer oracle or bounded improvement curriculum is established by these open application-turn routes. Reported benchmark claims are not used as causal evidence here.

## Shared records

### Components

#### RT-CMP-provider-model
Label: Caller-selected provider inference

Source-native identity: model argument on the registered client, for example `gpt-4o-mini` in the SQLite caller. Representational form: distributed-parametric. Storage substrate: external provider infrastructure, inaccessible here. Parameters changing during operation: uninspected provider internals; the inspected wrapper requests inference and exposes no training step. Exact version pinned: no immutable weights/version identity is established by the example's model string. Mutable endpoint resolving to another model: possible through provider model aliases and caller/client configuration; actual resolution is uninspected. Source and evidence: SRC-1, `examples/sqlite/main.py`, `memori/llm/invoke/invoke.py`, `memori/llm/clients/direct.py` (implementation).

> raw_response = self._method(**kwargs)
> --- `memori/llm/invoke/invoke.py`

#### RT-CMP-sentence-transformers-embedder
Label: Native SentenceTransformersEmbedder

Source-native identity: Rust `SentenceTransformersEmbedder`. Representational form: distributed-parametric weights consumed by ONNX inference. Storage substrate: downloaded model/cache files and lazy in-process `TextEmbedding`. Parameters changing during operation: no weight-update operation in the inspected loader/embed methods; mutable inference state is not evidence of training. Exact version pinned: model enum/name is selected, but this loader supplies no immutable model artifact digest or repository revision. Mutable endpoint resolving to another model: loader obtains model files through model-code lookup and cache; different configurations or upstream artifacts can alter loaded weights. This is not a live remote inference endpoint. SRC-1: `core/src/embeddings/models.rs` (implementation).

> let embedding_model: EmbeddingModel = match model_name {
>     Some(name) => name.parse().map_err(|e: String| anyhow!("{e}"))?,
>     None => EmbeddingModel::AllMiniLML6V2,
> };
> --- `core/src/embeddings/models.rs`

#### RT-CMP-tei-embeddings
Label: Optional TEI embedding service

Source-native identity: Python `TEI` supplied to embedding API. Representational form: distributed-parametric computation behind a JSON API; returned vectors are numerical representations. Storage substrate: external endpoint, implementation inaccessible; URL/headers/timeout are local configuration. Parameters changing during operation: uninspected. Exact version pinned: no, request model string is not an immutable artifact identity. Mutable endpoint resolving to another model: yes, the configured URL and service-side model resolution can change independently of this source. This is an available alternative, not established as active in the SQLite example. SRC-1: `memori/embeddings/_api.py`, `memori/embeddings/_tei.py` (implementation).

> json={"input": inputs, "model": model},
> --- `memori/embeddings/_tei.py`

#### RT-CMP-augmentation-service
Label: Opaque Memori augmentation service

Source-native identity: service called by `augmentation_async` / `augmentation_raw_async` and cloud/agent collector endpoints. Representational form: client protocol is symbolic JSON with natural-language messages; any distributed-parametric derivation component behind it is opaque, not established merely by the endpoint name. Storage substrate: external service infrastructure, unavailable here. For any service-side model: parameters changing during operation, exact pinned version and mutable model resolution are all uninspected. The lack of a server model identity prevents attributing a particular model or fixity to extracted memories. SRC-1: `memori/memory/augmentation/augmentations/memori/_augmentation.py`, `core/src/augmentation/pipeline.rs`, `memori-ts/src/engines/augmentation.ts` (client implementation).

> let raw_response = client.augmentation_raw_async(&payload).await?;
> --- `core/src/augmentation/pipeline.rs`

### Operative objects

#### RT-OBJ-recall-context
Label: Formatted model-visible recall context

Source-native identity: `recall_context` / `recallContext`. Representational form: natural-language facts and summaries with relevance guidance; provider role and message envelopes are symbolic transport, not a new memory store. Storage substrate: transient request kwargs/messages. Producer: recall formatting after threshold selection; consumer: provider input. This record is distinct from durable fact rows and embeddings, which are not inventoried here. SRC-1: `memori/llm/pipelines/recall_injection.py`, `memori-ts/src/engines/recall.ts` (implementation).

> context_body = "Relevant context about the user:\n" + "\n".join(fact_lines)
> --- `memori/llm/pipelines/recall_injection.py`

### Routes

#### RT-RTE-python-invocation
Label: Python wrapped non-streaming invocation

Endpoints/progression: registered client method → recall and history injection → original inference method → payload formatting → memory manager → augmentation dispatch → original response. Owner: application selects input/model/identity; SDK code selects branch and context; external provider computes answer. Decision policy is symbolic branching plus score filtering; inferred response is parametric and context is natural language. State includes config, session UUID and cached database identifiers. Executor/effect boundary: same Python process, external provider/service and configured database adapter. SRC-1: `memori/__init__.py`, `memori/llm/clients/direct.py`, `memori/llm/invoke/invoke.py`, `memori/llm/pipelines/post_invoke.py`, `memori/memory/_manager.py`, `memori/memory/_writer.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: original provider response after synchronous post-response work; persistence errors may instead propagate.
- Later read-back: replayed conversation messages and selected derived facts/summaries can reach subsequent registered invocations.
- Delegated visibility: provider receives constructed context; persistence and augmentation receive formatted conversation material, not unrestricted access to host state.
- Selection predicate: supported registered method; recall additionally needs extracted query and attribution/storage prerequisites; relevant facts meet configured score threshold.
- Invalidation or expiry: new_session resets UUID and caches; explicit set_session changes session; BYODB deletion API exists for entity memories, not a general host-context revocation.
- Activation or effect: construction, model-input delivery and persistence dispatch are wired; changed model behavior is unobserved.
- Evidence limits: Python recall algorithm, driver semantics and every framework adapter were not exhaustively inspected; no all-provider or successful-operation inference.

Controls include API/base URL, connection, native-core selection, attribution, session, model kwargs and explicit manual recall/capture methods. No content-level human approval is added by this wrapper. Model boundary: [RT-CMP-provider-model](#rt-cmp-provider-model). Follow-on admission: [RT-RTE-augmentation-admission](#rt-rte-augmentation-admission).

> handle_post_response(self, kwargs, start, raw_response)
> return raw_response
> --- `memori/llm/invoke/invoke.py:64-65`

#### RT-RTE-stream-exhaustion
Label: Generic Python iterator persistence

Endpoints/progression: wrapped inference returns source iterator → wrapper yields each chunk while accumulating response → StopIteration/StopAsyncIteration triggers memory manager → exhaustion propagates. Owner: caller controls consumption; wrapper owns chunk accumulation and terminal persistence. State is transient accumulated response, original kwargs and start time. SRC-1: `memori/llm/invoke/invoke.py`, `memori/llm/invoke/iterator.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: iterator/chunks, rather than an augmentation receipt; normal exhaustion performs persistence.
- Later read-back: persisted conversation material may be replayed by later calls; no generic-iterator augmentation dispatch is shown.
- Delegated visibility: original provider receives pre-injected request; memory manager receives formatted accumulated output on exhaustion.
- Selection predicate: source response matches iterator/async iterator branch and caller drives it to exhaustion.
- Invalidation or expiry: transient wrapper state ends with iterator lifetime; early termination does not execute the inspected exhaustion branch.
- Activation or effect: chunk delivery and exhaustion-triggered persistence are wired, not observed.
- Evidence limits: Bedrock iterable/body and framework-specific streaming wrappers have separate implementations; this finding is limited to the generic iterator file.

The handler calls MemoryManager directly, not the augmentation-dispatching post-response function. Context exit forwards to the source without an added persistence action. This challenges a claim that all wrapped completions have identical capture/augmentation semantics.

> except StopIteration:
>     MemoryManager(self.config).execute(
>         format_payload(
> --- `memori/llm/invoke/iterator.py`

#### RT-RTE-augmentation-admission
Label: Automatic service-derived memory admission

Endpoints/progression: completed-turn payload → cloud collector, or BYODB native/Python processing → service response → local write operations → storage bridge/database writer. Owner: SDK routes and writes; hosted service proposes derived content under inaccessible policy. Python selects recent user/assistant messages when an existing summary exists; Rust payload currently supplies summary None. Client processing maps service facts/triples, process attributes and conversation summary into writes. SRC-1: `memori/memory/augmentation/_handler.py`, `memori/memory/augmentation/_manager.py`, `memori/memory/augmentation/augmentations/memori/_augmentation.py`, `core/src/augmentation/pipeline.rs`, `core/src/lib.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: enqueue/submission result, native job identifier, or background dispatch; not proof of semantic or durable success.
- Later read-back: accepted facts/summaries are intended to supply later recall and conversation context; exact storage revision policy belongs to the memory analysis.
- Delegated visibility: service receives selected conversation text, metadata and attribution representation; native storage bridge receives derived write batches.
- Selection predicate: attribution/content prerequisites; active manager/enabled augmentations or native branch; service response fields and client parsing determine write operations.
- Invalidation or expiry: failures can skip writes; Python quota errors disable its augmentation manager; native drain/shutdown and Python wait address lifetime, not semantic rollback. Per-item rollback/expiry is uninspected.
- Activation or effect: write scheduling, native embedding attachment and bridge writes are wired; later changed behavior and benefit are unobserved.
- Evidence limits: hosted proposal/admission criteria are unavailable, cloud writes are opaque, and local database transaction/revision behavior is not exhaustively traced.

Admission: trigger is ordinary completed interaction, not an improvement experiment. Proposed changes are facts, triples, process attributes and summaries. Computation makes local scheduling decisions; no per-content human review is visible in these inspected handlers. A caller can withhold capture/configuration or disable augmentation, but this is not evidence of a human deciding each memory item. Service rejection ability and internal guidance are uninspected. Client gates reject malformed/missing input and skip empty/error responses; those gates do not judge truth. No answer oracle is established. Operating mode: open application traffic; no inspected curriculum or success-triggered capability update.

Recovery: Python logs most errors, separately latches quota failure, and waits on futures/queues; native handlers log service/write failures and end. There is no established end-to-end transaction across inference, conversation persistence, remote derivation and fact storage. Guidance shaping proposals is unavailable beyond transmitted conversation/summary/metadata. What persists is derived content and conversation state, not an established criticizable extraction theory. No inference of formulated criticism, learning benefit or exercised self-improvement follows from this admission route. Model boundaries: [RT-CMP-sentence-transformers-embedder](#rt-cmp-sentence-transformers-embedder), [RT-CMP-augmentation-service](#rt-cmp-augmentation-service).

> memories = await self._process_api_response(api_response)
>
> ctx.data["memories"] = memories
>
> await self._schedule_entity_writes(ctx, driver, memories)
> self._schedule_process_writes(ctx, driver, memories)
> self._schedule_conversation_writes(ctx, memories)
> --- `memori/memory/augmentation/augmentations/memori/_augmentation.py`

#### RT-RTE-typescript-hooks
Label: TypeScript Axon hooks and synthetic capture

Endpoints/progression: register client with Axon → before recall hook → inference → persistence and augmentation after hooks. Synthetic integration payloads enter the same engines without requiring this wrapper to execute inference. Owner: Memori registers handlers; external Axon owns middleware invocation; application/host owns task progression. Context/state: local entity/process, session/project and constructed request; executor uses native engine with storage or remote APIs. SRC-1: `memori-ts/src/memori.ts`, `memori-ts/src/engines/recall.ts`, `memori-ts/src/engines/persistence.ts`, `memori-ts/src/engines/augmentation.ts`, `memori-ts/src/integrations/base.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: request enriched by recall, then original LLMResponse; caught memory failures generally leave request/response available.
- Later read-back: local or cloud facts/summaries and sanitized history are supplied before later calls; manual recall returns facts rather than forcing their use.
- Delegated visibility: Axon/provider receive the transformed request; native bridge/cloud receive last-user and assistant content; agent mode additionally sends supplied trace/summary in cloud payloads.
- Selection predicate: session and last user message; BYODB recall also requires entity; score threshold gates fact context, not history replay.
- Invalidation or expiry: resetSession/setSession change session selection; no general injected-context revocation is established by these handlers.
- Activation or effect: hook wiring, history/fact injection, explicit local conversation write batch and asynchronous augmentation submission are implemented; invocation/compliance are unobserved.
- Evidence limits: external Axon implementation and all native binding conversions are not frozen/fully traced; returned responses do not establish successful memory writes.

Agent capture first posts an agent conversation turn, aborts agent augmentation if that post fails, and then fires collector augmentation without waiting for completion. Native agent capture uses native submission and does not transmit its cloud-only trace/summary payload. The source supports different payload coverage, not equivalent agent-learning inputs across modes. Admission roles/oracle: same open-traffic software/service split as [RT-RTE-augmentation-admission](#rt-rte-augmentation-admission); no per-item human approval or answer oracle is established. Client can configure attribution, session, connection and embedding model. `forRequest` is offered for independent attribution/session scopes, but its internals and deployed isolation are not assessed here.

> this.axon.hook.before(this.recallEngine.handleRecall.bind(this.recallEngine));
> this.axon.hook.after(this.persistenceEngine.handlePersistence.bind(this.persistenceEngine));
> this.axon.hook.after(this.augmentationEngine.handleAugmentation.bind(this.augmentationEngine));
> --- `memori-ts/src/memori.ts:263-265`

#### RT-RTE-hermes-provider
Label: Hermes intentional recall and turn sync

Endpoints/progression: host registers MemoryProvider → initialize from file/environment and host session → system prompt/tool schemas → host-selected tool callback → JSON service result; completed turns independently call sync_turn → daemon thread → client.capture_turn. Owner: Hermes foreground agent selects recall; provider code derives trace from current-turn messages and schedules capture. State: entity/process config, project derived from configuration or host identity/workspace, current session and latest sync thread. SRC-1: `integrations/hermes/src/memori_hermes/__init__.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: prefetch returns empty string; tools return JSON or JSON error; sync_turn starts a background thread.
- Later read-back: explicit recall, summary or compaction calls request retained material with project defaults; server selection and derivation remain opaque.
- Delegated visibility: capture includes completed user/assistant text and current-turn tool names/args/results paired by tool-call ID; no general host memory or remote-worker visibility is established.
- Selection predicate: configured provider; foreground agent chooses tool and filters; capture occurs when the host invokes sync_turn with completed-turn material.
- Invalidation or expiry: session switch changes local session; shutdown/session end joins latest sync thread for up to five seconds, not a durable completion guarantee.
- Activation or effect: callback dispatch, prompt supply and background capture are wired; intentional recall and obeying contextual-evidence instructions are unobserved.
- Evidence limits: Hermes runtime and the service internals are outside the inspected implementation; only provider-owned transformation and dispatch are established.

Admission roles/oracle: host supplies trace, service proposes retained derivations, client automatically submits; no per-content human approval, answer oracle or bounded curriculum is established. The foreground agent can decline tools in practice; prompt asks it to recall only when history matters. Tool failures return errors; capture failure logs a warning. Prompt guidance says not to invent memory and not to let recall override current user instructions. These are behavioral requests, not a code-level precedence guarantee.

> def prefetch(self, query: str, *, session_id: str = "") -> str:
>     del query, session_id
>     return ""
> --- `integrations/hermes/src/memori_hermes/__init__.py`

#### RT-RTE-claude-skill
Label: Claude Code Bash memory lifecycle

Endpoints/progression: shipped skill asks foreground agent to invoke Bun CLI through Bash → CLI validates flags/credentials → GET recall or compaction; after drafting, CLI posts conversation turn then augmentation. Owner: foreground agent controls whether/when commands run and what trace/text to submit; CLI applies symbolic request checks; remote service owns derivation. State: environment/settings credentials and namespace, project basename default, write-session default from host environment. SRC-1: `integrations/claude-code/SKILL.md` (doctrine/design), `integrations/claude-code/index.ts` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON stdout and success exit, or stderr/failure exit. Augmentation collector failure is logged as non-fatal after turn persistence and still returns success.
- Later read-back: project-scoped recall/summary intentionally omit default session restriction; explicit session/date/source/signal filters narrow requests; compaction restores service-produced resume data.
- Delegated visibility: shell subprocess receives environment and flags; service receives submitted user/assistant content and supplied trace, which may be summarized or omitted.
- Selection predicate: skill asks for essentially every non-trivial turn and before external lookup; CLI recall rejects query and requires valid paired source/signal categories when provided.
- Invalidation or expiry: no server retention/revocation policy inspected; host context loss does not itself delete service memory; explicit read-session filter differs from default write-session identity.
- Activation or effect: CLI request paths are wired; skill invocation and obedience are not observed.
- Evidence limits: the shell/skill host's grants, instruction loading and execution are external; the printed augmentation flag is not proof of collector success.

Change admission: the foreground agent constructs submitted content under the skill's capture guidance; no per-item user approval is required by the CLI. User opt-out is a skill instruction, not a CLI enforcement branch. Turn persistence is awaited; collector errors do not roll it back. Service rejection/policy and downstream memory revisions are opaque. Operating mode: open user work; no answer oracle or improvement experiment. Static guidance persists as a shipped skill; captured content persists through service-dependent mechanisms.

> } catch (e) {
>   console.error(`[memori] collector augmentation failed (non-fatal): ${(e as Error).message}`);
> }
>
> return { success: true, augmentation: true };
> --- `integrations/claude-code/index.ts`

#### RT-RTE-openclaw-hooks
Label: OpenClaw prompt supply and completed-turn capture

Endpoints/progression: plugin register → credential/namespace checks → static skills/config in before_prompt_build → conditional agent_end capture → bounded recent-message parsing → synthetic agent augmentation; authenticated tools offer requested recall/compaction. Owner: host runs lifecycle hooks and foreground agent selects tools; plugin code parses completed turn; service supplies retained results. SRC-1: `integrations/openclaw/src/index.ts`, `integrations/openclaw/src/handlers/augmentation.ts`, `memori-ts/src/integrations/base.ts`, `integrations/openclaw/src/tools/memori-compaction.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: prompt context additions, tool text results or completed hook; errors are logged or returned as tool error objects.
- Later read-back: recall/summary and post-compaction tool results request service-retained context; compaction description requests resume-state use, not a local context-trimming implementation.
- Delegated visibility: parser bounds messages, extracts last completed turn and tool-call trace, cleans text, and can substitute a synthetic response for pure-tool execution; whole raw history is not established as delivered.
- Selection predicate: configured API key/entity; version-sensitive conversation-access grant for agent_end; successful event with enough messages and parsed non-system user/assistant pair; foreground agent selects compaction and project scope.
- Invalidation or expiry: disabling/missing host access prevents capture registration on affected versions; retention expiry and host-window eviction are uninspected.
- Activation or effect: hook/tool registration and submission are wired; host execution, compaction fidelity and instruction compliance remain unobserved.
- Evidence limits: external host permission enforcement and hosted compaction generation are unavailable; tool prompt's list of output fields is design, not observed output.

Admission roles/oracle: automatic software capture following host completion; service-dependent proposal/admission, no inspected per-item human approval or answer oracle. Capture failures do not trigger a demonstrated replay/recovery protocol. Compaction allows explicit model-supplied project override of configured default. That is a selector, not a proof of authorization. This route does not grant arbitrary shell execution; enclosing host tool grants are separate.

> if (hasConversationAccess) {
>   api.on('agent_end', (event: unknown, ctx: unknown) =>
>     handleAugmentation(event as OpenClawEvent, ctx as OpenClawContext, config, logger)
>   );
> }
> --- `integrations/openclaw/src/index.ts`

#### RT-RTE-mcp-guidance
Label: Documented MCP intentional memory lifecycle

Endpoints/progression: MCP client supplies API-key/entity headers to hosted stateless HTTP endpoint → foreground agent chooses recall/summary/compaction → service returns memory → agent may explicitly augment durable content after drafting. Owner: agent selects calls and proposed turn content under shipped skill guidance; hosted server owns actual tool execution and derivation. Context/state: authenticated namespace from headers, optionally exposed project/session/date/source/signal fields, and returned resume state. SRC-1: `docs/memori-cloud/mcp/overview.mdx`, `docs/memori-cloud/mcp/skills/memori-mcp/SKILL.md` (doctrine/design, not server implementation).

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected
- Immediate return: claimed structured tool responses; failures should be explained without fabricated memory.
- Later read-back: claimed cross-session durable memory, summaries and post-compaction brief with recent-message tail.
- Delegated visibility: requested user/assistant turn and optional safe trace/summary; tool availability and scope depend on active client schema.
- Selection predicate: intentional recall when history matters; augmentation only for information useful weeks later; avoid routine progress, raw outputs, secrets and ephemeral facts.
- Invalidation or expiry: user storage opt-out requests skipping augmentation; actual server deletion, expiry and rollback are uninspected.
- Activation or effect: prompts request later contextual and resume-state use; neither client execution nor model compliance is observed.
- Evidence limits: hosted implementation is unavailable; documented headers/session derivation and tool parameters are contracts, not inspected enforcement. The skill permits query-based recall, unlike the inspected Claude Code CLI.

Admission roles: foreground agent proposes and decides whether content is durable enough to submit; user may veto storage by explicit opt-out; server admission/rejection is opaque. No per-content human confirmation is requested. Guidance shaping proposal is explicit durable-only classification plus privacy exclusions; claimed retained result is durable user/project content, not ordinary session logs. Recovery is graceful degradation on tool failure, not rollback. Mode: open user work, not bounded optimization. No operational answer oracle is established; the skill's suggested fresh-session verification is a test procedure without supplied results. No claim of extraction-quality improvement follows from its feedback instruction.

> Through MCP, durable memory is stored explicitly with `memori_advanced_augmentation` after you draft a response.
>
> Use `memori_advanced_augmentation` only when the turn reveals durable information that would still be useful weeks from now in another conversation.
> --- `docs/memori-cloud/mcp/skills/memori-mcp/SKILL.md`

#### RT-RTE-augmentation-extension
Label: In-process augmentation class registration

Endpoints/progression: application-imported decorator adds/replaces registry class by name → manager instantiates current registry entries with config → enabled classes process augmentation context → context writes are queued. Owner: application/package code supplies classes; manager invokes them. Representational form: symbolic executable Python; storage substrate: process-global class dictionary and source files, not a remotely fetched skill store. SRC-1: `memori/memory/augmentation/_registry.py`, `memori/memory/augmentation/_manager.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: registration decorator returns class; manager construction captures instances; processing returns accumulated context.
- Later read-back: inapplicable — registry selection is executable configuration, not trace-accumulated retained content. Any extension-produced durable writes require their own admission assessment.
- Delegated visibility: instantiated class receives config, augmentation context and database driver in the same process.
- Selection predicate: class registered before manager construction, then aug.enabled at processing time.
- Invalidation or expiry: name registration replaces dictionary entry; existing managers already hold instances; hot replacement/reload and durable rollback are not established.
- Activation or effect: manager calls enabled processors; arbitrary deployed extensions and their effects are unobserved.
- Evidence limits: this surface establishes callable extension authority, not agent-driven installation, sandboxing or self-modification.

Admission: application author/import proposes class; dictionary assignment admits it without an inspected signature/human approval gate. Caller can omit registration or disable an instance; processing errors are logged except quota escalation. Recovery does not undo arbitrary extension side effects. Guidance is class code; persisted artifact is package/application source outside this runtime route. Operating mode: application configuration and normal traffic, not an improvement curriculum. No answer oracle is established.

> cls._augmentations[name] = augmentation_class
> return augmentation_class
> --- `memori/memory/augmentation/_registry.py`

### Claims

#### RT-CLM-ambient-lifecycle
Label: Claude Code mandatory ambient memory lifecycle

Claimed operation: recall before substantive responses and external lookup, augmentation after final drafting, with narrow skip cases and explicit opt-out. Source: SRC-1, `integrations/claude-code/SKILL.md` (doctrine/design). This is a policy claim about agent conduct, not proof of execution. The implementation only acts when invoked, as recorded in [RT-RTE-claude-skill](#rt-rte-claude-skill).

> Always fire before external lookups (WebSearch/WebFetch) and
> before answering any question about preferences, prior decisions,
> constraints, project history, status, past work, or any non-trivial
> coding/research task.
> --- `integrations/claude-code/SKILL.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-recalled-context
Label: Recalled text entering provider context

Consumer: caller-selected provider model. Channel: Python system/instructions/Google-system field or TypeScript system message, plus replayed conversation messages. Force: supplied model context with a relevance instruction, not a code-enforced command or verified precedence rule. Horizon: immediate inference; recurrence depends on later retrieval from durable state. Source: SRC-1, `memori/llm/pipelines/recall_injection.py`, `memori/llm/pipelines/conversation_injection.py`, `memori-ts/src/engines/recall.ts` (implementation). See [RT-OBJ-recall-context](#rt-obj-recall-context). Delivery is wired; activation is unobserved.

> existing_instructions = kwargs.get("instructions", "") or ""
> kwargs["instructions"] = existing_instructions + recall_context
> --- `memori/llm/pipelines/recall_injection.py`

#### RT-BAP-host-memory-guidance
Label: Host skill and resume-state guidance

Consumer: foreground host agent. Channel: shipped skill/system prompt and tool-result JSON/text. Force: natural-language instruction to recall and treat retrieved state as contextual/resume evidence; actual obedience and resistance to stale or adversarial content are unobserved. Horizon: host turns and later sessions when loaded/recalled. SRC-1: `integrations/claude-code/SKILL.md`, `integrations/hermes/src/memori_hermes/__init__.py`, `integrations/openclaw/src/index.ts`, `integrations/openclaw/src/tools/memori-compaction.ts` (doctrine/design plus wiring). Hermes requests current-user priority; OpenClaw compaction asks for standing orders and continuation while warning about stale state. These are consequential behavioral channels, not only passive factual lookup.

> The compaction result should guide continuation, not override explicit user instructions. Before acting on operational details, verify any state that may have changed since compaction.
> --- `integrations/openclaw/src/tools/memori-compaction.ts`

## Annotations

none
