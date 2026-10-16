---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Mem0 runtime baseline: Python memory and answer loops, direct-write and API controls, hosted delegation and OpenClaw context delivery at the frozen revision."
run-id: AAS-2026-10-14-mem0-5b642a1731b4-01
reviewed-boundary: "0724291bd864cf807e88ee8981c8226644e8fb42"
---

# Mem0 runtime report

## Runtime account

Mem0's consequential work in this boundary is to turn supplied conversations into retained text and numerical indexes, then select retained text for later extraction or answer generation. It is not the owner of a general agent execution loop. The local engine owns extraction, persistence calls and search; shipped drivers and hooks own delivery to answer-producing models or hosts. The hosted clients own HTTP request construction, not the unavailable service's internal decisions. All findings below use SRC-1 at the frozen revision. Implementation is inspected source, not observed execution. No target, model, test, example or service was run; activation and benefit remain unobserved.

### Ordinary invocation and owners

The README's `chat_with_memories` is a small, shipped end-to-end consumer: a caller supplies a message and `user_id`; code asks `Memory.search` for three scoped memories; it reduces returned objects to memory text, places that text in a system message, calls OpenAI for an answer, appends that answer, and calls `Memory.add` before returning the answer. The exact next-step owner is the driver, not an autonomous Mem0 scheduler. A failed addition can prevent the already-generated answer from being returned because this example has no recovery wrapper. See [RT-RTE-chat-memories](#rt-rte-chat-memories), [RT-RTE-extract-add](#rt-rte-extract-add) and [RT-BAP-answer-context](#rt-bap-answer-context) (SRC-1, `README.md`, `mem0/memory/main.py`).

> relevant_memories = memory.search(query=message, filters={"user_id": user_id}, top_k=3)
> memories_str = "\n".join(f"- {entry['memory']}" for entry in relevant_memories["results"])
> --- `README.md`

> messages.append({"role": "assistant", "content": assistant_response})
>     memory.add(messages, user_id=user_id)
>
>     return assistant_response
> --- `README.md`

For that driver's default local engine, construction uses configurable factories for the embedder, vector store and language model, plus a SQLite history/message manager. The numerical components are separately described in [RT-CMP-openai-llm](#rt-cmp-openai-llm) and [RT-CMP-openai-embedding](#rt-cmp-openai-embedding). They are external inference dependencies, not inspected trainable internals. `custom_instructions` are copied from configuration. An optional reranker changes search ordering, but its provider internals and other model adapters are not characterized here (SRC-1, `mem0/memory/main.py`, `mem0/configs/base.py`).

For ordinary inferred addition, code normalizes message shape and identity metadata, rejects unsupported OSS `timestamp`, loads ten recent messages for the identity-derived session scope, embeds the new messages and retrieves ten existing memories. It maps existing UUIDs to local numeric strings, then constructs a system extraction instruction and a user prompt containing current messages, previous messages and retrieved text. The model proposes text; Python parsing, embeddings, hash checks and persistence calls determine which proposals are emitted as ADD results. This is software/model admission without a per-item human approval gate. The actual pipeline is additive; the `add` docstring's broader promise of choosing add/update/delete must not be substituted for the inspected implementation. Explicit update/delete and procedural summary routes remain different branches (SRC-1, `mem0/memory/main.py`, `mem0/configs/prompts.py`).

> You are a Memory Extractor — a precise, evidence-bound processor responsible for extracting rich, contextual memories from conversations. Your sole operation is ADD: identify every piece of memorable information and produce self-contained, contextually rich factual statements.
> --- `mem0/configs/prompts.py`

Existing context is advisory language to the model, not a proof checker. Hash deduplication checks hashes from the retrieved candidate set and current batch, not a complete global uniqueness index. Parsing errors can collapse into no extractions while messages are still saved. Extraction-provider exceptions instead become `LLMError`, allowing the caller to distinguish failure from an empty successful extraction. Batch embedding and insertion have per-item fallbacks. History and entity-link failures can be logged without undoing a vector insertion. Consequently, the ordinary write is not an atomic transaction spanning all stores (SRC-1, `mem0/memory/main.py`).

Search validates query, limits and scope filters; combines semantic candidates with keyword scores and entity boosts; filters expired payloads unless requested otherwise; ranks and formats text-bearing results; and optionally reranks with fallback to the original results. Keyword results supply scores to semantic candidates rather than independently enlarging the candidate set in the inspected Python method. The driver consumes only the selected `memory` fields; it does not pass IDs, provenance or score explanations to the answer model. Provider-specific search semantics and ranking accuracy remain external or untested (SRC-1, `mem0/memory/main.py`).

### Four forcing cases and alternate paths

1. **Bypass inferred admission.** `infer=False` embeds and inserts non-system messages directly. Explicit update/delete work by memory ID, while `agent_id` plus procedural memory type selects an LLM summary branch before ordinary extraction. Thus model-based extraction is neither a universal write gate nor the only retained representation. [RT-RTE-direct-write](#rt-rte-direct-write) records these alternate grants (SRC-1, `mem0/memory/main.py`).
2. **Distinguish authentication from isolation.** The server authenticates normal memory endpoints and requires admin for configuration, bulk deletion and reset. But the inspected handlers forward caller-supplied identity filters or memory IDs, not an authenticated-user-derived memory scope. Library calls and configured provider code do not traverse HTTP auth at all. `AUTH_DISABLED` is a documented implementation escape hatch. [RT-RTE-server-access](#rt-rte-server-access) therefore supports endpoint authentication, not a system-wide tenant-isolation guarantee (SRC-1, `server/main.py`, `server/auth.py`).
3. **Challenge a shipped consumer against the current API.** The proxy's recall passes top-level identity arguments that current local and hosted Python search reject; its hosted formatter also iterates the returned object as if it were a list, whereas current hosted search returns a dictionary. Its daemon addition runs independently of recall. The proxy's intended answer loop is present but cannot be described as a coherent current successful path without qualification. [RT-RTE-proxy-chat](#rt-rte-proxy-chat) captures the source-visible incompatibility rather than extrapolating from its wrapper name (SRC-1, `mem0/proxy/main.py`, `mem0/memory/main.py`, `mem0/client/main.py`).
4. **Change the owner of memory decisions.** OpenClaw skills mode injects a protocol and recalled context but explicitly skips legacy auto-capture. The foreground host agent instead chooses `memory_add`; that tool submits inferred facts with `infer:false`. Legacy mode has a distinct filtered, fire-and-forget post-turn capture path. Subagent recall and write restrictions are plugin-local, not a host-wide sandbox. [RT-RTE-openclaw-hooks](#rt-rte-openclaw-hooks) and [RT-RTE-openclaw-add](#rt-rte-openclaw-add) retain that difference (SRC-1, `integrations/openclaw/index.ts`, `integrations/openclaw/tools/memory-add.ts`).

### Guarantees, grants and changes

**ADD result accounting:** owner is the local engine; enforcement is the `persisted_records` list after vector-store insertion. Strength is **protocol**, conditional on the adapter returning successfully only when insertion succeeded. The inferred batch route returns only those records; alternate raw and procedural branches use `_create_memory` and propagate insertion/history errors differently. A partially successful batch followed by an exception and retry may already have effects; no cross-store rollback or global exactly-once guarantee follows. Implementation conclusion status: wired. Operation conclusion status: uninspected (SRC-1, `mem0/memory/main.py`).

> # Only records confirmed to be stored make it into history, entity
>         # links, and the returned results — a record the store rejected must
>         # never be reported back as a successful ADD.
> --- `mem0/memory/main.py:1052-1054`

**Scope validation and expiry visibility:** owner is the Python method's code, with **invariant** strength for requiring scope-key presence in `search`, but only **protocol** strength for the database adapter actually applying filters. It is caller-selected scope, not authentication. Expiry hiding is a search/get-all visibility rule, not erasure or universal read denial: direct `get(memory_id)` returns the payload without an expiry check; server admin all-memory listing is intentionally raw. `show_expired=True` is another explicit alternate. Implementation conclusion status: wired. Operation conclusion status: uninspected (SRC-1, `mem0/memory/main.py`, `server/main.py`).

> if not any(key in effective_filters for key in ("user_id", "agent_id", "run_id")):
>             raise ValueError(
>                 "filters must contain at least one of: user_id, agent_id, run_id. "
>                 "Example: filters={'user_id': 'u1'}"
>             )
> --- `mem0/memory/main.py:1471-1475`

**API access:** owner is FastAPI dependencies; enforcement points are `verify_auth` and `require_admin`, with **policy** strength. Covered paths are the inspected memory/config endpoints. Direct SDK calls, server-internal vector-store access, hosted backend behavior, trusted extension imports and disabled-auth deployments are not covered. Required external contracts include token/key validation, secrets, database and deployment configuration. Neither a deployed isolation envelope nor an actual grant set was supplied. Implementation conclusion status: wired. Operation conclusion status: uninspected. [RT-RTE-server-access](#rt-rte-server-access) provides the counterpaths.

**Context budgets and subagent restrictions:** OpenClaw recall offers **best effort** limits, not a hard token invariant. Its estimate counts memory characters at roughly four per token; identity/configuration items may exceed the budget, and formatting adds overhead. It does not trim the host's accumulated window or control host compaction. Tool-side subagent blocking depends on shared session state; protocol text alone cannot enforce compliance. Implementation conclusion status: wired. Operation conclusion status: uninspected (SRC-1, `integrations/openclaw/recall.ts`, `integrations/openclaw/index.ts`, `integrations/openclaw/tools/memory-add.ts`).

Changes to retained knowledge enter through extraction, direct insertion, explicit mutation, procedural summaries or host-selected facts; revision semantics belong to the memory analysis. Changes to production machinery and extraction guidance enter through server configuration replacement and trusted Python provider registration, recorded in [RT-RTE-runtime-config](#rt-rte-runtime-config). The server can generate proposed instructions, but that endpoint returns a proposal; it does not itself install them. The caller must later submit configuration. Repository code or static prompt changes require an external development/release action; this report does not infer a runtime product self-modifier from their being editable files (SRC-1, `server/main.py`, `server/server_state.py`, `mem0/utils/factory.py`).

### Coverage and unresolved alternatives

Added SRC-1 implementation coverage beyond the boundary's initial inspection includes the synchronous Python addition, search, direct mutation and procedural bodies; SQLite message retention; default OpenAI adapters; provider registration; server auth, configuration and memory handlers; hosted Python add/search contracts; proxy; TypeScript extraction phase; and OpenClaw recall/capture/tools. Prompt and README passages supply doctrine/design as well as call-site context. No new source or evidence layer was acquired.

The inspected async Python extraction dispatches provider/store work through `asyncio.to_thread`, including its model call and persistence; this is a concurrency variant, not evidence of a durable worker service. TypeScript has its own inferred and raw branches, retrieves prior messages only if its storage supports that method, and tolerates prior-message load failure. It uses additive extraction, but this does not establish all Python validation, storage or failure semantics in TypeScript. Hosted Python add/search perform `/v3/` HTTP requests and return JSON; they do not expose the remote model/admission implementation. See [RT-RTE-hosted-client](#rt-rte-hosted-client) (SRC-1, `mem0/memory/main.py`, `mem0-ts/src/oss/src/memory/index.ts`, `mem0/client/main.py`).

Other providers, optional reranker internals, TypeScript post-extraction persistence and search, additional framework integrations, CLI commands, dashboard request flows and most test/evaluator sources remain available but uninspected in this runtime baseline. They are not claimed absent or equivalent. Their independent end-to-end guarantees and instruction-admission behavior are unresolved here. The hosted backend and evaluation submodule remain unavailable as declared by the boundary. Performance-related batching, candidate over-fetch and fire-and-forget calls are inspected mechanisms, not measurements of speed or quality. No claim of exercised learning, reliable criticism, benefit or self-improvement is made.

## Shared records

### Components

#### RT-CMP-openai-llm
Label: OpenAILLM default inference component

Source-native identity: `OpenAILLM`, selected through `LlmFactory` by the local Python engine. Representational form: distributed-parametric model, invoked through symbolic API parameters and natural-language messages; model weights/storage reside at an external endpoint, not the SQLite/vector store. Default model identifier is `gpt-5-mini`. Mem0's inspected adapter requests completions and does not change parameters through training; provider-side parameter changes are uninspected. Exact numerical version is not pinned by that alias. Configurable base URLs, OpenRouter routing and provider-owned aliases can resolve to other model implementations. This component also admits a configured response callback executing trusted host code, not model-sandboxed code. SRC-1, `mem0/llms/openai.py`, `mem0/utils/factory.py`, `mem0/memory/main.py`.

> if not self.config.model:
>             self.config.model = "gpt-5-mini"
> --- `mem0/llms/openai.py`

> if self.config.response_callback:
>             try:
>                 self.config.response_callback(self, response, params)
> --- `mem0/llms/openai.py`

#### RT-CMP-openai-embedding
Label: OpenAIEmbedding default numerical encoder

Source-native identity: `OpenAIEmbedding`, selected by the embedder factory. Representational form: distributed-parametric encoder, producing dense float arrays stored by the configured vector-store adapter. Provider weights remain externally stored and uninspected. The adapter requests embeddings and does not train or mutate weights; exact version is not pinned, and configurable endpoint/model aliases can resolve differently. Stored embedding values change when texts are added or updated; that is not a claim of model-weight learning. SRC-1, `mem0/embeddings/openai.py`, `mem0/memory/main.py`.

> self.config.model = self.config.model or "text-embedding-3-small"
> --- `mem0/embeddings/openai.py`

### Operative objects

#### RT-OBJ-custom-instructions
Label: Custom extraction instructions

Identity: `MemoryConfig.custom_instructions`, copied to `Memory.custom_instructions`; per-call `prompt` overrides it on ordinary inferred addition. Natural-language representational form, held in Python configuration/instance memory and optionally persisted as server configuration overrides in a Settings row. It reaches the extraction model as a custom-instructions section rather than executable policy. Model compliance is unobserved. SRC-1, `mem0/configs/base.py`, `mem0/memory/main.py`, `mem0/configs/prompts.py`, `server/server_state.py`.

> if custom_instructions:
>         sections.append(f"## Custom Instructions\n{custom_instructions}")
> --- `mem0/configs/prompts.py`

#### RT-OBJ-config-overrides
Label: Server configuration overrides

Identity: Settings key `config_overrides`. Symbolic JSON mapping stored in the server database; the mapping includes a separately interpreted natural-language custom-instructions value described by [RT-OBJ-custom-instructions](#rt-obj-custom-instructions). Startup merges overrides with defaults. Live replacement reconstructs the engine. Credentials, provider choices and store configuration can change, not only text. Database persistence failure is logged and swallowed, so a live change need not survive restart. SRC-1, `server/server_state.py`.

> overrides = _load_overrides()
>         if overrides:
>             _current_config = _merge_config(_current_config, overrides)
>         _memory_instance = Memory.from_config(_current_config)
> --- `server/server_state.py`

### Routes

#### RT-RTE-chat-memories
Label: README chat with memories

Caller message and `user_id` → scoped search → text-only system context → OpenAI answer → conversation addition → returned answer. The driver owns progression and the return boundary; the external answer model proposes prose, not Mem0 tool actions. Context excludes full historical conversation except the selected memory strings and current message. State spans configured stores through subsequent additions. Code selects top three and delegates semantic relevance to search. No per-answer human approval, reference-answer oracle or automatic quality comparison appears in this driver; operating mode is open interactive requests. SRC-1, `README.md`, `mem0/memory/main.py`; source passages in the Runtime account.

- Immediate return: Assistant text after synchronous memory addition returns.
- Later read-back: Conversation-derived retained text can enter the next scoped search and the next extraction's previous-message context.
- Delegated visibility: Answer provider receives selected memory text and current message; extraction provider receives the appended conversation under its separate prompt.
- Selection predicate: `user_id`, current-message query and `top_k=3`; only returned memory strings are forwarded.
- Invalidation or expiry: Search can omit expired/deleted content; this driver has no independent invalidation mechanism.
- Activation or effect: Code wires memory text into answer input; changed answer behavior is unobserved.
- Evidence limits: Shipped example source, not an observed chat; external inference and store contracts remain dependencies.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-extract-add
Label: Inferred Python addition

`Memory.add` → prior-message and existing-memory retrieval → one extraction-model call → parsed text → embeddings/hash checks → vector inserts → history/entity attempts → message save → ADD results. Caller supplies identities and initial content; model proposes facts; code decides storage eligibility and can skip malformed, empty, duplicate or unembeddable items. Human authorship of individual inputs is unresolved, and there is no mandatory human item-by-item approval here. Operating mode is an open addition request, not a bounded experiment or curriculum. Answer oracle: none established; model judgment and duplicate context are not expected-answer references. Guidance is the static additive prompt plus agent suffix and optional custom instructions; proposed text persists, not a separately required justification. Rejection is procedural/structural, not a truth-validation guarantee. Rollback is not cross-store atomic; caller retries or later explicit deletion/update are separate recovery actions. SRC-1, `mem0/memory/main.py`, `mem0/configs/prompts.py`, `mem0/memory/storage.py`.

> custom_instr = prompt or self.custom_instructions
> --- `mem0/memory/main.py:948-948`

> except Exception as e:
>             # Re-raise so callers can implement provider fallback / retry.
> --- `mem0/memory/main.py`

- Immediate return: `results` containing confirmed-by-adapter ADD records; parsing/no-fact outcomes can return an empty list; provider or total insertion failure raises.
- Later read-back: Inserted text is available to search and later extraction; SQLite messages are saved and the most recent ten per scope are reloaded for future inferred additions.
- Delegated visibility: Extraction provider receives new messages, last messages and retrieved text; embedding provider receives new or proposed texts; vector store receives vectors and payloads.
- Selection predicate: At least one caller identity; extraction retrieves ten scoped vector matches; model selects facts; code skips duplicate hashes among retrieved records and the batch.
- Invalidation or expiry: Explicit mutations and expiry affect later search; SQLite evicts messages outside its recent-ten scope window.
- Activation or effect: Store mutation and later model-input delivery are implemented; exercised effects on answers are unobserved.
- Evidence limits: Adapter success is trusted; no atomic vector/history/entity commit, semantic completeness or truthful extraction result is established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-direct-write
Label: Direct and procedural Python writes

Alternate entry paths in `Memory`: `infer=False` stores non-system messages without extraction; `update` embeds replacement text and mutates an ID; `delete` removes an ID and writes history; agent-scoped procedural addition first summarizes messages with a model and stores a procedural-memory payload. The caller owns direct proposals and invocation; the procedural model owns summary proposal. Code checks shape/existence and calls adapters; no mandatory human confirmation or correctness oracle is established. Operating modes are explicit mutation and open procedural summarization. Static procedural guidance or a caller prompt shapes the summary; retained result is summary text plus metadata, not necessarily the derivation. Recovery uses history inspection and separate mutation; history is not an automatic rollback mechanism. This record establishes alternate runtime gates, not detailed memory-revision findings. SRC-1, `mem0/memory/main.py`.

> if agent_id is not None and memory_type == MemoryType.PROCEDURAL.value:
>             results = self._create_procedural_memory(messages, metadata=processed_metadata, prompt=prompt)
> --- `mem0/memory/main.py`

> msg_content = message_dict["content"]
>                 msg_embeddings = self.embedding_model.embed(msg_content, "add")
>                 mem_id = self._create_memory(msg_content, {msg_content: msg_embeddings}, per_msg_meta)
> --- `mem0/memory/main.py`

- Immediate return: Added record IDs/events, mutation success messages, or raised errors; procedural branch returns its summary ADD result.
- Later read-back: Stored raw/replacement/summary text can be returned by later scoped search or ID lookup; deleted IDs no longer resolve through the store.
- Delegated visibility: Embedding/store providers see supplied text; procedural inference additionally sees the conversation and summarization instruction.
- Selection predicate: Raw path skips system messages; update/delete target a memory ID; procedural branch requires agent ID and procedural memory type.
- Invalidation or expiry: Explicit delete/update, optional expiry metadata and reset; direct ID lookup is not universally expiry-filtered.
- Activation or effect: Code directly changes retained state without the ordinary extraction-model gate.
- Evidence limits: No universal human admission, tenant ownership or summary quality follows; per-method and adapter failure semantics apply.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-server-access
Label: Self-hosted server access controls

HTTP caller → FastAPI auth dependency → method handler → current shared Memory instance → JSON/error response. `verify_auth` uses bearer JWT, API key, legacy admin key or explicit disabled-auth mode. `require_admin` gates configuration, bulk delete and reset. The authenticated principal is not converted into a memory namespace by the inspected memory handlers; single-memory operations take caller IDs. Endpoint auth therefore does not establish per-memory authorization. Capability surface includes CRUD, all-memory admin listing and reset; deployed credentials and process/network isolation are unobserved. SRC-1, `server/auth.py`, `server/main.py`.

> if AUTH_DISABLED:
>         _mark_auth_type(request, "disabled")
>         return None
> --- `server/auth.py`

> def get_memory(memory_id: str, _auth=Depends(verify_auth)):
>     """Retrieve a specific memory by ID."""
>     try:
>         return get_memory_instance().get(memory_id)
> --- `server/main.py`

- Immediate return: JSON method results, authentication/authorization failures, client-validation errors or upstream errors.
- Later read-back: Mutations reach the shared engine and its later readers; raw admin listing can expose stored expired content.
- Delegated visibility: Current engine/providers see forwarded request content; authenticated identity itself is not the inspected selector for memory ownership.
- Selection predicate: Credential validation and role for privileged endpoints; caller-provided identity filters or memory IDs select content.
- Invalidation or expiry: Auth/key invalidation internals beyond the inspected dependency body are uninspected; memory expiry remains an engine visibility rule.
- Activation or effect: Dependencies gate HTTP method execution, not direct SDK/provider calls.
- Evidence limits: No observed deployment, universal tenant isolation, network sandbox or hosted-service authorization conclusion.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-runtime-config
Label: Runtime configuration and provider admission

Admin configuration POST → bundled-provider validation → locked merge and engine reconstruction → attempted persistence of overrides. The admin/caller proposes configuration and can choose custom extraction instructions and providers; code validates and constructs, but no model-based evaluation or answer oracle decides installation. `/generate-instructions` instead asks the existing LLM for instruction/test-message text and returns it without installation: the generated test message is a proposed input, not an independently correct answer. Operating modes are explicit configuration and optional proposal generation. Rejection can occur at validation or construction; `_current_config` is assigned before constructing the replacement, so construction failure is not shown to restore old config. Persistence failure is swallowed. No automatic rollback is implemented in the inspected update routine. Trusted Python code can separately call `LlmFactory.register_provider`; this is in-process class registration and import authority, not a sandboxed model capability grant. SRC-1, `server/main.py`, `server/server_state.py`, `mem0/utils/factory.py`.

> next_config = _merge_config(_current_config, updates)
>         _current_config = next_config
>         _memory_instance = Memory.from_config(next_config)
> --- `server/server_state.py`

> if config_class is None:
>             config_class = BaseLlmConfig
>         cls.provider_to_class[name] = (class_path, config_class)
> --- `mem0/utils/factory.py`

- Immediate return: Configuration success after replacement/persistence attempt, generated proposal text, or validation/construction error.
- Later read-back: Current instance uses new configuration; restart reloads persisted overrides; registered provider mappings affect later constructions in the process.
- Delegated visibility: Generated use-case instructions go to the configured LLM; imported provider classes execute with host-process authority.
- Selection predicate: Admin role and bundled-provider validation for HTTP installation; trusted Python invocation for class registration.
- Invalidation or expiry: Explicit later reconfiguration/restart; override persistence is best effort and provider registration is process-local.
- Activation or effect: Configuration reconstructs the live engine; custom instructions are consumed by subsequent additions; generated proposals alone have no installed force.
- Evidence limits: No successful reconfiguration or release pipeline was observed; no evidence-responsive automatic product improvement established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-hosted-client
Label: Hosted Python request delegation

Application → `MemoryClient.add/search` → normalized HTTP payload → remote `/v3/` endpoint → status check and JSON return. The caller selects inputs/scope, and local code owns validation; remote service owns actual extraction, admission and storage, which are unavailable. Human per-content control and remote veto/rollback policies are uninspected. Operating mode is open API requests. No answer oracle or remote evaluation mechanism is established by these wrappers. SRC-1, `mem0/client/main.py`.

> response = self.client.post("/v3/memories/add/", json=payload)
>         response.raise_for_status()
> --- `mem0/client/main.py`

> response = self.client.post("/v3/memories/search/", json=payload)
>         response.raise_for_status()
> --- `mem0/client/main.py`

- Immediate return: Parsed service JSON or mapped HTTP/network error.
- Later read-back: Client affords later search/get of service-held material; remote persistence and visibility implementation remain uninspected.
- Delegated visibility: Configured remote service receives messages/query, scope and requested options.
- Selection predicate: Caller-provided parameters and local request validation; remote selection is opaque.
- Invalidation or expiry: uninspected — remote mutation/expiry semantics are not supplied by these request bodies.
- Activation or effect: HTTP delegation is implemented; service operation and downstream behavior are unobserved.
- Evidence limits: Request affordance does not establish OSS parity, remote synchronous completion or hosted performance.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-proxy-chat
Label: Proxy completion attempt

Caller → local/hosted backend selection → daemon addition and recall → memory formatting → LiteLLM completion. The intended owner is proxy code; caller can supply model, tools, function controls and provider routing. The proxy forwards these to completion rather than implementing a tool-execution/approval loop. No host shell grant or model-native tool execution guarantee follows from accepting the parameters. SRC-1, `mem0/proxy/main.py`, `mem0/memory/main.py`, `mem0/client/main.py`.

> threading.Thread(target=add_task, daemon=True).start()
> --- `mem0/proxy/main.py`

> return self.mem0_client.search(
>             query="\n".join(message_input),
>             user_id=user_id,
>             agent_id=agent_id,
>             run_id=run_id,
>             filters=filters,
>             top_k=top_k,
>         )
> --- `mem0/proxy/main.py`

- Immediate return: Intended LiteLLM response; current last-user-message branch instead encounters search-argument rejection before completion on the inspected Python backends.
- Later read-back: Background addition can mutate storage independently; completion return does not certify addition finished or persisted.
- Delegated visibility: Addition receives original messages; recall query uses last six message strings; completion would receive original context with the last content replaced by formatted recall.
- Selection predicate: Last prepared message must be user for recall/add; user/agent/run ID required; backend chosen by API-key presence.
- Invalidation or expiry: Backend-specific; daemon work has no joined durable recovery or completion acknowledgement in this wrapper.
- Activation or effect: Intended delivery is source-wired but blocked by inspected API mismatch on this branch; other branches may call LiteLLM without recall.
- Evidence limits: No execution; incompatibility follows from caller/callee source. Hosted formatter additionally assumes a list despite current dictionary response.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-openclaw-hooks
Label: OpenClaw recall and capture hooks

Host prompt-build callback → trigger/session guards → provider search → selected memory formatting → returned context channels. Skills mode supplies static triage protocol as system context and recalled text as ordinary prepend context; manual strategy skips automatic recall. Legacy mode instead filters/caps score-ranked search results and supplies `<relevant-memories>` context. On successful main interactive completion, legacy capture filters message roles/noise, selects recent material plus summary-pattern messages and starts provider addition without waiting. Skills mode returns before legacy registration and its agent-end callback does not capture. Host controls hook execution and subsequent model invocation. SRC-1, `integrations/openclaw/index.ts`, `integrations/openclaw/recall.ts`.

> return {
>         prependSystemContext: systemContext, // cached by provider
>         prependContext: recallContext, // per-turn dynamic
>       };
> --- `integrations/openclaw/index.ts`

> return; // Skip legacy hook registration
> --- `integrations/openclaw/index.ts`

- Immediate return: Context fragments to the host; legacy capture schedules an asynchronous addition and logs eventual success/failure.
- Later read-back: Provider-stored captured text can enter future recall; skills protocol itself is static shipped guidance, not an accumulated memory update.
- Delegated visibility: Subagents can receive parent-user recall; legacy subagent capture is skipped. The host decides how returned channels enter model context.
- Selection predicate: Interactive/long-enough non-bootstrap prompt, session-derived scope and configured strategy; skills recall ranks categories/importance/relevance and budgets selected text; legacy recall applies thresholds and topK.
- Invalidation or expiry: Provider-specific; recall failure degrades to missing context, and legacy recall races a timeout without establishing cancellation of the underlying search.
- Activation or effect: Plugin returns memory/protocol channels and initiates capture; host compliance and answer changes are unobserved.
- Evidence limits: No host trace, hard token bound or host-wide subagent isolation; capture comments about consolidated subagent output do not prove host delivery.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Capture admission: host success is a trigger, not a human content approval. Plugin code selects/filter/redacts messages; backend extraction can further select text. Model/host computation and software carry admission; explicit memory-tool use can suppress duplicate auto-capture. No reference-answer oracle is established. Guidance asks for durable facts with a date preamble. Recovery logs failures; no durable capture retry queue is shown in the inspected callback. Operating modes are skills-driven explicit tools versus legacy automatic capture, not a single universal policy.

#### RT-RTE-openclaw-add
Label: OpenClaw foreground memory tool

Host agent proposes facts via `memory_add` → noise filtering/session check → provider add → text and details to host. Skills-active branch supplies `infer:false` and `deduced_memories`; legacy tool branch delegates inference through normal add options. The agent proposes and selects content; code can reject missing facts, noise or recognized subagent session. No mandatory human approval or independent expected-answer oracle appears in this tool. Operating mode is foreground agent-controlled admission. Persisted content is proposed fact text plus category/importance metadata, not required reasoning or criticism. Delete/update tools are separate capabilities, not automatic rollback here. SRC-1, `integrations/openclaw/tools/memory-add.ts`.

> const addOpts: AddOptions = {
>             user_id: uid, source: "OPENCLAW", infer: false,
>             deduced_memories: allFacts, metadata: parsedMetadata ?? {},
>           };
> --- `integrations/openclaw/tools/memory-add.ts`

- Immediate return: Tool text/details or caught error; skills text reports requested fact count while details carry actual provider results.
- Later read-back: Accepted provider facts can reach later recall; exact provider persistence semantics remain separate.
- Delegated visibility: Provider receives cleaned fact strings, identity/scope and metadata; host receives tool output, not a private worker context.
- Selection predicate: Foreground fact choice, nonempty/non-noise content and shared current-session subagent check; long-term defaults true.
- Invalidation or expiry: Separate provider mutation controls; no automatic fact expiry or rollback is established in this tool body.
- Activation or effect: Direct admission request bypasses backend extraction in skills mode; later behavioral effect remains unobserved.
- Evidence limits: Host's actual tool grants/session scheduling and provider implementation determine enforcement; requesting storage is not proof of activation or benefit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-answer-context
Label: Memory text to answer generation

Consumer: README answer model. Channel: selected memory strings interpolated into a system message. Force: natural-language instruction/context interpreted by an external model, not a code invariant or verified fact. Horizon: future chat invocations after retained additions. Source evidence is [RT-RTE-chat-memories](#rt-rte-chat-memories), SRC-1, `README.md`. Delivery is implemented; compliance, improved answers and causal activation are unobserved.

> system_prompt = f"You are a helpful AI. Answer the question based on query and memories.\nUser Memories:\n{memories_str}"
> --- `README.md`

#### RT-BAP-extraction-context
Label: Prior text to extraction decisions

Consumer: configured extraction model. Channel: generated user prompt combines prior messages, existing memories, new messages and optional custom instructions under the additive system instruction. Force: requested deduplication, attribution and extraction policy through model interpretation; subsequent code enforces storage shape/hash conditions, not truth. Horizon: later additions in the same identity scope, potentially across process restarts if configured storage survives. [RT-RTE-extract-add](#rt-rte-extract-add) and [RT-OBJ-custom-instructions](#rt-obj-custom-instructions) identify delivery and authority boundaries. SRC-1, `mem0/configs/prompts.py`, `mem0/memory/main.py`.

> Use these ONLY for deduplication and linking — do NOT extract new memories from Existing Memories. Your extractions must come exclusively from New Messages. If new information in New Messages is semantically equivalent to an Existing Memory with no meaningful new context, skip it.
> --- `mem0/configs/prompts.py`

## Annotations

none
