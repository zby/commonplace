---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Virtual Context runtime baseline tracing shipped chat, proxy, paging, import, administration and engagement paths at the frozen repository revision."
run-id: AAS-2026-10-14-virtual-context-bbd06cc3ac95-01
reviewed-boundary: "74ccc570c40bb551820fcd330c42e0dfc0588f05"
---

# Virtual Context runtime report

## Runtime account

Virtual Context assembles context and maintains conversation-derived memory; it is not the enclosing agent that owns arbitrary user tasks. The shipped chat and proxy drivers do own model invocation and completion delivery. MCP and the OpenClaw hook instead return material to another runtime. These differences determine where a context-control guarantee can apply.

This report uses SRC-1 at the boundary's frozen commit. All findings below are implementation findings unless explicitly called design. No target, test, model or external service was executed. Wiring does not establish successful operation, activation of delivered text or benefit. Added inspection covers the headless driver and chat provider; engine API and checkpoint saving; retrieval filtering; compaction dispatch and summarizer rejection; tool-query orchestration, tool execution and repetition guard; proxy preparation and tag dispatch; MCP recall/compact; bundled OpenClaw hooks; import; record editing; engagement selection/posting and destination lists; embedding loading; and SQLite fence-mode handling. These are additional inspected portions of SRC-1, not additional sources.

### Ordinary invocation and accumulated state

The CLI dispatches headless chat to `HeadlessRunner`. A prompt becomes a user `Message`; the driver waits for its preceding completion future, calls inbound assembly, filters history and sends assembled text as the Anthropic system input. The foreground provider emits text chunks, which become the assistant message and a `TurnRecord`. The driver submits an immutable-list snapshot of history for background completion, waits before the next retrieval, and saves the session after the final completion. This is an ordinary shipped path, not merely an illustrative SDK caller: [RT-RTE-headless-chat](#rt-rte-headless-chat).

The engine delegates inbound work to its retrieval assembler. History filtering has a configurable pre-compaction mode, protected recent pairs, a compaction watermark, and a conservative inclusion branch when tag data is missing. Older pairs without tag overlap can be excluded, but `rule`-tagged pairs survive. This is selective removal from an accumulated context, not a new isolated agent frame. Compaction makes old material reachable through summaries and retrieval rather than preserving it verbatim in every model window. Model-selected paging can restore more detail: [RT-RTE-paging-loop](#rt-rte-paging-loop).

Completed turns pass through tagging and, when signaled, compaction. The compaction pipeline reads canonical stored rows outside the protected zone rather than blindly summarizing whatever payload a caller supplies. Its output is admitted to retained memory without a per-summary human approval requirement. Model responses are parsed and can be rejected or replaced by fallbacks; requesting a faithful summary is not a fidelity guarantee. The route and its admission boundary are [RT-RTE-memory-maintenance](#rt-rte-memory-maintenance). The detailed memory transformations and revisions remain for the memory member.

Engine state includes conversation identity, generation, checkpoint version, compacted/flushed prefixes, indexed/completed turns, tag-index entries and paging working set. Default saves write a store snapshot and optionally a Redis cache; provider mode delegates durable saving to the caller. Thus engine method return is not universally a durable-commit acknowledgement: [RT-OBJ-engine-state](#rt-obj-engine-state).

### Material alternates and forcing cases

**Proxy instead of headless.** The proxy prepares provider-specific payloads, derives request roles and speaker authority, assembles with that context, then adopts the roster snapshot returned by assembly. Streaming and non-streaming handlers forward responses and feed completed work into proxy state. Tagging and compaction are split, allowing compaction to run later. The proxy also has manual/restoration/indexing passthrough branches, budget handling and a bloat fallback. An engine exception explicitly forwards unmodified. Consequently, enrichment is conditional, and headless's wait-for-full-completion rule cannot be attributed to every proxy request. See [RT-RTE-proxy-request](#rt-rte-proxy-request), SRC-1 `virtual_context/proxy/server.py`, `virtual_context/proxy/handlers.py`, `virtual_context/proxy/state.py`.

**Tool loop instead of direct answer.** `query_with_tools` injects tools when paging and flushed history permit, or when forced. Provider-native tool schemas do not grant arbitrary executor access: the synchronous loop executes recognized VC tools and returns mixed VC/non-VC calls as-is. Extra tool definitions are a capability advertisement, not an implementation of those tools. A restore tool additionally requires a request-body runtime supplied by the caller. The repetition guard is process-local and fails open; it is not an approval or cost ceiling. The bounded continuation loop is a separate control. See [RT-RTE-paging-loop](#rt-rte-paging-loop).

**Host hooks and MCP instead of a driver-owned model call.** OpenClaw uses a synchronous subprocess for `transform` and an asynchronous subprocess for `compact`. The inserted object is actually a user-role message, despite a nearby comment saying system message; its `<system-reminder>` text is not a transport-level system role. Hook errors do not block the host model call. MCP returns recall text or compaction reports and has a distinct stateless recall path, expressly avoiding the legacy transform convenience path where request audience proof is unavailable. Neither integration establishes that a host consumes the return or delivers every completion. See [RT-RTE-openclaw-hooks](#rt-rte-openclaw-hooks) and [RT-RTE-mcp-tools](#rt-rte-mcp-tools).

**Administrative and batch admission instead of live conversation.** Import iterates adapter-produced conversations, sets each conversation ID, ingests history and optionally compacts repeatedly. Record editing synchronously changes canonical records and audits them; a host must subsequently run the rebuild processor. These routes can alter later answers without a foreground conversational turn and do not inherit an inference-tool approval policy. See [RT-RTE-import-history](#rt-rte-import-history) and [RT-RTE-record-edits](#rt-rte-record-edits).

**Optional outward action.** Engagement is a separate caller-triggered selection/draft/verification workflow. Its callable sender is an outward effect boundary. Source validation and model fidelity judgment precede it, but fidelity rejection is type-dependent: `apply_fidelity_outcome` checks verdicts only for `personal` outcomes. The bundled qualifier can emit `timed`; a nonempty timed draft with a negative fidelity verdict can reach staging when the independent posting controls pass. The poster does not recheck fidelity. These judgments are not an expected-answer oracle. Posting is default-off at the runner argument, and current posting implementation admits staging destinations only. Source comments describe an owner-approved publication path; this report establishes the inspected staging path, not an implemented end-to-end owner approval service. See [RT-RTE-engagement-stage](#rt-rte-engagement-stage).

These forcing cases challenge three tempting generalizations: that all requests receive enrichment, that all routes await full maintenance before retrieval, and that tool limits or posting checks constrain every capability available to an enclosing host. None holds system-wide. A fourth forcing check concerns stale compaction writes: SQLite has active, observe and off modes. Active mode can reject a fenced mismatch; observe/off intentionally weaken that enforcement. The current deployed mode and credentials are not supplied. This does not establish a deployment-wide concurrency invariant.

### Guarantees and their owners

| Scoped guarantee | Owner and enforcement point | Strength and covered paths | Alternate paths and external contract | Conclusion statuses |
|---|---|---|---|---|
| A headless next turn waits for preceding maintenance | `HeadlessRunner._wait_for_complete`, called before retrieval | protocol; sequential headless execution | Proxy splits tagging/compaction; OpenClaw compact is asynchronous. Completion catches errors, so waiting is not successful maintenance. Requires executor/future delivery. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Known VC-only calls are handled within bounded continuations | `run_tool_loop`, `range(max_loops)` and mixed-call bailout | protocol; synchronous query tool path | Direct chat has no VC loop; proxy continuation is separate; arbitrary tools remain host-owned. Requires provider response compatibility. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Repeated guarded searches can be replaced by synthetic results | `guard_tool_execution` before tool dispatch | best effort; enabled, identified calls in one process | Disabled settings, malformed identity/config and internal errors execute normally; other workers do not share this in-memory guard. | implementation conclusion status: wired; operation conclusion status: uninspected |
| A stale fenced mutation is rejected when active enforcement detects mismatch | SQLite `_enforce_or_observe_mismatch`; operation-owned compaction calls | policy; inspected active-mode fence rejection and compaction dispatch | Observe logs; off ignores. Optional operation IDs and uninspected mutation sites prevent a universal fence claim. Requires backend transaction and lease contract; PostgreSQL equivalence not audited here. | implementation conclusion status: wired; operation conclusion status: uninspected |
| The inspected compose/post path does not select a community publish destination | `post_question`, staging allowlist guard; disjoint-list assertion | invariant within this function and unchanged shipped lists | Caller-supplied sender can ignore the requested destination; another host sender or modified code is outside this control. No global sandbox or credential restriction follows. | implementation conclusion status: wired; operation conclusion status: uninspected |

The capability surface includes provider HTTP calls, store writes, optional Redis, local embedding loading, hook subprocesses, host-supplied tools and the engagement sender. Current grants are selected by caller configuration, API keys, request authority and supplied callables. The deployed isolation envelope is unobserved. No authorization or OS confinement conclusion follows from a conversation ID or from an `actor` audit string. SRC-1 `virtual_context/tui/chat_provider.py`, `virtual_context/engine.py`, `virtual_context/core/tool_query.py`, `virtual_context/openclaw/virtual-context.mjs`, `virtual_context/core/engagement/runner.py`, `virtual_context/core/record_editing.py` support these distinctions.

### Changes, models and evaluator limits

The inspected operational change mechanisms admit retained conversation-derived material, imported history, canonical edits/fact verdicts and engagement ledger state. They do not by themselves modify model weights or ship a successor product. Configured providers and caller-supplied callables can change effective capability at construction/invocation time; this is host configuration, not evidence of autonomous capability acquisition. Source-native prompts, provider selection and parsing rules shape proposals; their deployed versions are not inferred from the source pin. Distributed-parametric consumers are recorded separately below.

The boundary also includes evaluators and dated repair scripts. In SRC-1 `benchmarks/longmemeval/vc_runner.py`, inspected call sites ingest, loop over manual compaction, require cache checkpoint success, assemble a question and invoke the reader with tools. This is a bounded evaluation mode with dataset questions, distinct from open chat. Reader-visible expected-answer handling, judgment reliability and measured scores were not traced here; no answer-oracle or benchmark-performance finding is established from those call sites. Other boundary-listed evaluator families, repair application bodies, community maintenance internals and release workflows remain uninspected in this runtime member. They are not claimed absent or inaccessible; this report does not establish their end-to-end correctness, all change-admission gates or performance. The specialists may inspect those available portions at the same pin.

## Shared records

### Components

#### RT-CMP-chat-provider
Label: ChatProvider

Source-native identity: `ChatProvider` and the provider-adapted reader endpoint. Representational form: distributed-parametric model processing; requests/responses are separate natural-language and symbolic interface objects. Substrate: remote provider service, not weights in the repository. SRC-1 `virtual_context/tui/chat_provider.py`, `virtual_context/core/tool_query.py`.

Parameters changing during operation: no parameter-write interface is exercised by these inspected consumers; provider internals and service updates are uninspected. Exact version pinned: no universal pin; constructor defaults and caller model strings are not a frozen parameter artifact. Mutable endpoint resolving another model: possible through configurable model/URL and remote provider resolution. Chat sends to the Anthropic Messages endpoint; tool-query adapters permit other providers and endpoint override.

> payload = {
>     "model": self.model,
>     "max_tokens": max_tokens,
>     "stream": True,
>     "messages": messages,
> }
> --- `virtual_context/tui/chat_provider.py`

#### RT-CMP-llm-provider
Label: llm_provider for tagging and compaction

Source-native identity: configured tag generator `llm` and compactor `llm_provider`; these are roles that may share or differ in endpoint, not an assertion of two distinct weight sets. Form: distributed-parametric inference; substrate: configured provider service. SRC-1 `virtual_context/core/tag_generator.py`, `virtual_context/core/compactor.py`, `virtual_context/engine.py`.

Parameters changing during operation: the inspected path calls completion, not training; provider internals are uninspected. Exact version pinned: no, configurable provider/model names. Mutable endpoint resolving another model: possible; engine accepts base URL and model configuration. Completion can change durable summaries and tags without changing weights.

> response_text, usage = self.llm.complete(
>     system=system,
>     user=prompt,
>     max_tokens=self.config.max_summary_tokens + self.config.llm_token_overhead,
> )
> --- `virtual_context/core/compactor.py:1739-1743`

#### RT-CMP-embedding-provider
Label: EmbeddingProvider

Source-native identity: shared embedding callable loaded by model name, or injected embedding provider. Form: distributed-parametric encoder; output vectors are dense representations distinct from the encoder weights. Substrate: local SentenceTransformer in process/cache, or injected provider. SRC-1 `virtual_context/core/embedding_provider.py`, `virtual_context/core/semantic_search.py`.

Parameters changing during operation: local path is inference-only; injected provider internals uninspected. Exact version pinned: no, local load uses a model name without revision argument. Mutable endpoint resolving another model: model-name resolution or injected provider can vary between installations; the process caches a successfully loaded callable. Failure can disable semantic search rather than preventing all operation.

> model = SentenceTransformer(model_name, device="cpu")
> --- `virtual_context/core/embedding_provider.py`

> return model.encode(
>     texts, convert_to_numpy=True, show_progress_bar=False,
> ).tolist()
> --- `virtual_context/core/embedding_provider.py`

#### RT-CMP-engagement-models
Label: engagement qualifier and drafter

Source-native identity: caller-supplied `qualifier` and `drafter`, the latter returning draft and fidelity verdict. Form: model-backed natural-language decisions over candidates, with symbolic result structures; exact model parameter substrate opaque to the runner. SRC-1 `virtual_context/core/engagement/runner.py`. Parameters changing during operation: uninspected behind supplied callables. Exact version pinned: not by this interface. Mutable endpoint resolving another model: uninspected, caller-controlled. Do not attribute the chat model's identity or fixity to these callables.

> qualified, qualify_rejections = qualifier(verified, now=now)
> --- `virtual_context/core/engagement/runner.py`

> attempt_draft, attempt_verdict = drafter(candidate)
> --- `virtual_context/core/engagement/runner.py`

### Operative objects

#### RT-OBJ-engine-state
Label: EngineStateSnapshot

Source-native identity: checkpoint of a conversation's engine state, not the complete content store. Form: symbolic counters, identities, lists and paging metadata; substrate: memory plus configured store snapshot and optional Redis cache. Natural-language history/cache content is a separate content payload, not a numerical weight update. SRC-1 `virtual_context/engine.py`.

The save constructs state, writes it through the store and attempts a cache snapshot. Stale saves return false; other save failures log and return false. Provider mode deliberately skips direct durable writes, so the host owns persistence in that mode. Recovery horizons depend on which owner actually saves. Read-back uses engine restoration; Redis history may be suffix-capped. A checkpoint is not evidence that every summary or canonical row is correct.

> if self._session_state_provider is not None:
>     # Provider mode: caller manages saves. Don't write to store/Redis directly.
> --- `virtual_context/engine.py`

> self._store.save_engine_state(snapshot)
> --- `virtual_context/engine.py`

### Routes

#### RT-RTE-headless-chat
Label: Headless chat turn

Endpoints/progression: CLI chat dispatch → `HeadlessRunner.run` → `_execute_turn` → engine inbound assembly/filter → `ChatProvider.stream_message` → assistant history and `TurnRecord` → completion future → saved session. Principal: caller supplying prompts/config/API credential. Identities: engine conversation ID and driver turn number; no separate delegated agent identity. Owner of next step: driver code; answer content: remote model under the assembled system text, filtered history and optional brief-mode instruction. SRC-1 `virtual_context/cli/main.py`, `virtual_context/tui/headless.py`, `virtual_context/tui/chat_provider.py`.

- Immediate return: collected turn records; streamed chunks become assistant text; session path is printed after final completion wait.
- Later read-back: maintained tags/summaries and state can affect subsequent engine assembly; session export separately retains user/assistant records, not a guarantee of lossless engine restoration.
- Delegated visibility: provider receives system text and filtered role/content messages, not every omitted history pair or the entire store.
- Selection predicate: current tags and protected recent window select history; brief mode appends a two-line request to the last user message.
- Invalidation or expiry: original history remains in driver memory; filtering returns a new list; compaction watermarks govern later payload inclusion.
- Activation or effect: provider HTTP request and assistant/history append are wired; behavioral compliance with memory or brief instructions is unobserved.
- Evidence limits: no run supplied; stream errors can leave partial or empty assistant text; engine initialization/assembly can fail without stopping plain chat.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operating mode: open prompts or replayed prompt sequence, no answer oracle in this driver. No per-answer approval gate is present in the inspected sequence; the caller chooses inputs, not every output. Error recovery logs failures, and completion exceptions are caught inside the background task; a resolved future therefore need not mean successful memory maintenance.

> assembled = self.engine.on_message_inbound(
>     user_message, self._conversation_history
> )
> --- `virtual_context/tui/headless.py`

> system_text = assembled.prepend_text
> --- `virtual_context/tui/headless.py`

> for chunk in self.provider.stream_message(
>     system=system_text, messages=api_messages
> ):
>     full_response.append(chunk)
> --- `virtual_context/tui/headless.py`

#### RT-RTE-memory-maintenance
Label: Completed-turn tagging and compaction

Endpoints/progression: completed history → `tag_turn` → optional `CompactionSignal` → `compact_if_needed` → canonical-row load → compactor → stored derivatives and checkpoint. Principal: driver or API caller; scope: bound conversation and operation identity where supplied. Owner: tagging/compaction pipeline code, with model proposals for content and software gates on admission. SRC-1 `virtual_context/engine.py`, `virtual_context/core/tagging_pipeline.py`, `virtual_context/core/compaction_pipeline.py`, `virtual_context/core/compactor.py`.

- Immediate return: optional compaction report; no signal, provider or eligible rows can yield no report.
- Later read-back: derived memory, tag index and compacted-prefix state influence future assembly and paging; default checkpoint path persists state.
- Delegated visibility: summarizer receives constructed segment prompt, not unlimited storage authority; pipeline executes writes.
- Selection predicate: threshold signal for automatic route; manual route bypasses threshold but still loads eligible canonical rows outside protection/watermark.
- Invalidation or expiry: later compaction, edits and rebuilds may replace derivatives; recovery insertion mode disables specified replacement passes.
- Activation or effect: implementation writes future-consumable memory and updates state; observed changes to later answers are uninspected.
- Evidence limits: no maintenance run or quality experiment; complete store-wide fencing and all replacement transformations not audited here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: model proposes tags/summary text; code normalizes/parses, applies rejection checks and persists admitted results. Humans supply conversation/configuration, not necessarily per-content decisions. The compactor can veto malformed or judged-invalid results; a short-source overshoot branch uses source-text fallback. Guidance: constructed system/prompt and summary token constraints; retained result is conversation-derived content, not necessarily the prompt or rationale. Trigger is completed-turn pressure or manual request. Recovery includes rerun/rebuild and fenced operation ownership; this is not transactional rollback of every derivative. No expected-answer oracle is established; the source transcript is an evidentiary reference, not a supplied correct answer to every future question. Operating mode: open conversation maintenance and explicit manual/batch maintenance. No formulated explanatory-theory revision is established by this route; detailed epistemic content remains for the epistemic analyst.

> signal = self.tag_turn(conversation_history, payload_tokens)
> if signal is None:
>     return None
> return self.compact_if_needed(conversation_history, signal)
> --- `virtual_context/engine.py`

> if not compact_messages:
>     logger.info(
>         "Compaction skipped: no uncompacted canonical turns outside protected zone "
>         "(history=%d msgs, protected=%d turns, compacted_prefix_messages=%d)",
> --- `virtual_context/core/compaction_pipeline.py`

#### RT-RTE-proxy-request
Label: Proxy prepare and completion

Endpoints/progression: host POST → `prepare_payload` → session routing and optional inbound assembly → provider forwarding/continuation → response → state tag phase and later compaction. Principal: external client and configured upstream credential; identities include conversation, reserved logical turn/hash, request roster snapshot and compaction operation. SRC-1 `virtual_context/proxy/server.py`, `virtual_context/proxy/handlers.py`, `virtual_context/proxy/state.py`.

- Immediate return: prepared provider payload at the preparation API, or streaming/non-streaming provider response through handlers.
- Later read-back: proxy-managed completed history, tag/index checkpoints and compaction products can feed subsequent requests.
- Delegated visibility: upstream sees transformed payload; passthrough can omit enrichment; speaker context is request-owned authority rather than tool-supplied permission.
- Selection predicate: manual override, restored/indexed session state and payload preparation choose active versus passthrough; active assembly uses current user and live history.
- Invalidation or expiry: request roster is snapshot-bound; duplicate indexed logical turns are skipped, including divergent duplicate protection; compaction runs under separate lifecycle.
- Activation or effect: payload changes, upstream requests and completion scheduling are wired; no observed response quality or delivery reliability supplied.
- Evidence limits: external host authorization and completion transport are outside the boundary; asynchronous races, all provider-specific continuations and deployed worker behavior are not observed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Code owns routing; model owns answer/tool choice. Open client requests are the operating mode; no answer oracle. Current request audience authority is explicitly forwarded and the returned snapshot adopted. This is narrower than a universal tenant-isolation guarantee. Recovery can forward an unmodified request on assembly failure. Compare the stronger local headless wait protocol with the split proxy maintenance path rather than assuming one common sequencing guarantee.

> if assembled.speaker_context is not None:
>     _speaker_context = assembled.speaker_context
> _roster_snapshot = assembled.speaker_roster_snapshot
> --- `virtual_context/proxy/server.py`

> except Exception as e:
>     logger.error("Engine error (forwarding unmodified): %s", e)
> --- `virtual_context/proxy/server.py`

#### RT-RTE-paging-loop
Label: Provider-adapted VC paging loop

Endpoints/progression: `query_with_tools` builds a request → provider tool calls → VC-only executor → results and optional reassembled context → continuation → final text/usage/tool records. Principal: caller supplying model, endpoint, messages and optional runtime; model selects tool names/arguments from schemas. SRC-1 `virtual_context/core/tool_query.py`, `virtual_context/core/tool_loop.py`, `virtual_context/core/tool_guard.py`.

- Immediate return: `ToolLoopResult` with text, calls, usage and raw request/response records; mixed non-VC calls are returned without executing that mixed batch.
- Later read-back: retained store content is searched/expanded into a later model invocation; working-set changes can reassemble context. Raw loop logs alone do not establish learning.
- Delegated visibility: model gets schema and selected results; `vc_restore_tool` requires the host's request-body runtime and restorable stubs.
- Selection predicate: paging plus flushed prefix, or force flag, advertises tools; model selects operations; executor checks recognized names and request-bound speaker context.
- Invalidation or expiry: per-loop presented-reference sets suppress repeated deliveries; repetition guard spans a configured process-local window; request roster liveness constrains speaker selection.
- Activation or effect: executor can change working-set depth and restore request payload, then send results/context to a continuation; use in the resulting answer is unobserved.
- Evidence limits: provider compliance and live tool correctness unobserved; bounded rounds do not bound all host tools, aggregate cost or distributed repetitions.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operating mode: open reader requests, including evaluator calls. No expected-answer oracle in this loop. Code decides schema grants and termination; model proposes calls; executor rejects/returns errors or synthetic guard results. Non-VC tool definitions do not confer execution on this loop. `require_tools` modifies provider tool policy, but Anthropic extended-thinking compatibility can reset an `any` choice to `auto`. Thus a tool-required setting is not an unconditional observed-use guarantee. No product-change admission occurs here.

> if non_vc_tools:
>     logger.warning("Mixed VC + non-VC tools in response — returning as-is")
>     result.stop_reason = stop_reason
>     return result
> --- `virtual_context/core/tool_loop.py`

> for loop_i in range(max_loops):
> --- `virtual_context/core/tool_loop.py`

> The guard fails open: disabled config, missing conversation
> identity, malformed knobs, or internal errors all execute the tool.
> --- `virtual_context/core/tool_guard.py`

#### RT-RTE-openclaw-hooks
Label: Bundled OpenClaw context hooks

Endpoints/progression: `before_context_send` → synchronous `transform` subprocess → injected reminder message; `agent_end` → temporary JSON → asynchronous `compact` subprocess → unlink callback. Principal: host event/config; identities use configured command/config and compact input, with no extra host authorization established. SRC-1 `virtual_context/openclaw/virtual-context.mjs`.

- Immediate return: replacement message array for a successful nonempty transform; no return modification on failure; completion hook starts a subprocess.
- Later read-back: compacted store content can be selected by a future transform if host configuration addresses the same state.
- Delegated visibility: CLI sees last user text for retrieval and serialized event messages for compact; host receives a user-role reminder, not a new system-role grant.
- Selection predicate: latest user message; nonempty transform output; completion requires nonempty event messages.
- Invalidation or expiry: temporary file removed after callback; hook delivery/restart behavior belongs to external host; memory expiry uninspected on this path.
- Activation or effect: code inserts selected context at array position one and launches maintenance; host consumption is unobserved.
- Evidence limits: subprocess timeouts and silently caught retrieval failure permit unenriched calls; no guarantee asynchronous compact completes before the next host call.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Direct `execFile` avoids shell interpolation but still grants execution of a configured binary. It is not evidence of a sandbox for host extensions. Host owns next-step scheduling and foreground answer policy; the plugin owns only these transformations. No answer oracle or human per-summary approval is introduced by the hooks.

> const injected = {
>   role: "user",
>   content: `<system-reminder>\n${stdout}\n</system-reminder>`,
>   timestamp: Date.now(),
> };
> --- `virtual_context/openclaw/virtual-context.mjs`

#### RT-RTE-mcp-tools
Label: MCP recall and compact tools

Endpoints/progression: host MCP call → lazy engine → retrieve/format or manual compact → text/JSON returned. Principal: external MCP caller; engine conversation/config are local identity; host owns later model invocation. SRC-1 `virtual_context/mcp/server.py`.

- Immediate return: assembled tag sections, empty recall, or compact report/no-compaction JSON.
- Later read-back: retrieval reads stored summaries; successful manual maintenance can affect future retrieval; no automatic completion-delivery loop is established by this server.
- Delegated visibility: host receives returned text; stateless recall has no validated audience and preserves opaque refs while routing through tag-section formatting.
- Selection predicate: caller message and active tags select recall; manual compact uses engine eligibility rules, not merely arbitrary submitted text.
- Invalidation or expiry: engine/store lifecycle applies; host-held result expiry is uninspected.
- Activation or effect: server returns model-facing material or invokes compaction; actual host incorporation is unobserved.
- Evidence limits: no MCP session trace; other MCP tool bodies not exhaustively audited; stateless refusal of legacy transform is not proof of universal audience safety.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Open tool-request mode; no answer oracle. Maintenance admission is the engine route, not an MCP human approval decision. The inspected recall implementation explicitly distinguishes itself from legacy transform:

> MCP carries no validated request audience. Do not call ``transform``:
> --- `virtual_context/mcp/server.py`

#### RT-RTE-import-history
Label: Import adapter history admission

Endpoints/progression: CLI input path/provider adapter → conversation/message iterator → bound engine → `ingest_history` → optional repeated `compact_manual`. Principal: CLI caller selecting file and configuration; identity is adapter-produced conversation ID. SRC-1 `virtual_context/cli/import_cmd.py`.

- Immediate return: printed progress/counts and CLI exit code.
- Later read-back: ingested canonical history and optional derivatives become available to later engine consumers in the same storage/conversation.
- Delegated visibility: engine sees adapter-normalized messages, not necessarily original export bytes or full provenance.
- Selection predicate: adapter choice and input path; empty message conversations skipped; compact flag enables maintenance loop.
- Invalidation or expiry: no general import rollback in this inspected driver; canonical editor/repair mechanisms are separate routes.
- Activation or effect: persisted ingestion and optional compaction are wired; later answer effects unobserved.
- Evidence limits: adapter fidelity and malformed-input coverage not audited; progress counts are not semantic validation or a quality oracle.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller authorizes batch source selection, adapter supplies content, engine admits through ingestion. This does not establish a human decision approving every normalized turn. Operating mode: batch history import, not a curriculum. Guidance is selected adapter/configuration and engine policies; retained content is imported conversation-derived material. Missing file or unknown adapter can reject the operation before ingestion. Partial failure recovery beyond existing engine mechanisms is uninspected.

> base_config.conversation_id = conversation_id
> engine = VirtualContextEngine(config=base_config)
> --- `virtual_context/cli/import_cmd.py`

> while engine.compact_manual(messages):
>     compact_count += 1
> --- `virtual_context/cli/import_cmd.py`

#### RT-RTE-record-edits
Label: RecordEditor canonical edits and fact verdicts

Endpoints/progression: host/admin call → synchronous edit/remove/forget or fact verdict → audit and index refresh → host-scheduled `process` rebuild. Principal: caller-provided `actor`; engine binds conversation. SRC-1 `virtual_context/core/record_editing.py`.

- Immediate return: operation/report or verdict result; derived rebuild is separately scheduled.
- Later read-back: edited canonical turns, fact rejection/restoration and rebuilt derivatives can alter later retrieval.
- Delegated visibility: editor receives turn IDs/content, tags or fact IDs; host decides who may call; actor is audit data rather than authentication proof.
- Selection predicate: conversation-bound turn/fact ID, resolved topic aliases, or an operation's rebuild worklist.
- Invalidation or expiry: index refresh removes canonical turns or forgotten tags; process resumes interrupted derived rebuild; fact restore can lift rejection.
- Activation or effect: canonical/source and verdict writes are wired; no observed full rebuild or downstream answer supplied.
- Evidence limits: synchronization of every consumer during an unfinished rebuild and complete backend authorization not established by this editor.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: host caller proposes exact replacement/removal or verdict; software performs it. Human contribution is unresolved for generic API callers, though the fact-review method is intended for admins. No independent content-approval gate or correct-answer oracle is established in this class. Guidance: supplied edit/reason and source-backed review display; edits and audit records persist. Recovery is idempotent rebuild and explicit restore/re-edit, not an automatic proof of reversal. Operating mode: explicit administration. This is knowledge revision, not sufficient evidence of improved capacity or theory criticism.

> Who may call these operations is the host's decision; the engine records the
> ``actor`` it is given.
> --- `virtual_context/core/record_editing.py`

> ``process`` is idempotent: rerunning an interrupted operation
> finishes the segments it had not reached.
> --- `virtual_context/core/record_editing.py`

#### RT-RTE-engagement-stage
Label: Engagement selection and staging

Endpoints/progression: externally invoked `run_once` → collect/verify/qualify → repetition filtering/ranking → up to three drafts with live source verification → fidelity outcome → dry report or staging sender → history ledger. Principal: caller supplying source data, time, callables and optional post intent. Conversation, source message, actor and destination identify scope. SRC-1 `virtual_context/core/engagement/runner.py`, `virtual_context/core/engagement/poster.py`, `virtual_context/core/engagement/allowlist.py`.

- Immediate return: report and optional staged message identity, or refusal/rejection reasons.
- Later read-back: posting history feeds repetition and daily-claim decisions; retained ledger affects later candidate admission.
- Delegated visibility: qualifier sees verified candidates; drafter sees selected candidate; sender receives requested destination, body and reply/mention metadata, not an engine-owned credential.
- Selection predicate: allowlist, source verification, qualification, history rules, rank, live verification, no re-paste request or question-similarity rejection, nonempty draft text and non-skip outcome. Fidelity verdict rejection applies only to `personal` outcomes; a `timed` outcome bypasses that veto. Posting additionally requires explicit intent and the poster's staging/source/day controls.
- Invalidation or expiry: repetition windows/day policy govern later eligibility; a pending day claim survives ambiguous send failure, preferring missed delivery to duplicate attempt.
- Activation or effect: dry run is default; enabled post path calls sender only after checks and a ledger claim; actual transport destination and receipt depend on supplied sender.
- Evidence limits: external scheduler, credentials, sender behavior and live source truth unobserved; inspected code establishes staging, not a complete publication approval service. The timed-type fidelity bypass is wired, not evidence of an actual unfaithful staged message or its deployment incidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Who proposes/decides/vetoes: qualifier and drafter propose; runner code rejects repetitions and re-paste requests. `apply_fidelity_outcome` converts a `personal` outcome to skip when no verdict is faithful, but returns every non-`personal` outcome before inspecting verdicts. The bundled qualifier emits `timed` for eligible timed follow-ups. Runner acceptance checks non-skip outcome and nonempty text, not fidelity independently; it records the verdict in the report. The poster receives no fidelity verdict and performs no later fidelity check. Live verifier and poster preconditions can independently veto. SRC-1 `virtual_context/core/engagement/select.py`, `virtual_context/core/engagement/continuation.py`, `virtual_context/core/engagement/runner.py`, `virtual_context/core/engagement/poster.py`. Caller can decline posting; unchanged code owns staging grants. Source verification checks source identity, not an answer oracle. Operating mode: externally scheduled bounded candidate walk with at most three draft attempts; no autonomous scheduling installed. Guidance: source evidence and eligibility/fidelity policies; report, rejection reasons and history persist according to supplied owners. Change admission is to the outward-action ledger and staged message, not to model weights. Claim-before-send is a recovery policy, not atomicity across database and transport.

> if outcome.kind != "personal":
>     return outcome
> if any(getattr(v, "faithful", False) for v in (verdicts or [])):
>     return outcome
> --- `virtual_context/core/engagement/select.py`

> question_type = "timed"
> hook_kind = ""
> hook_evidence = ""
> if not timed_ok:
> --- `virtual_context/core/engagement/continuation.py`

> if attempt_outcome.kind != "skip" and (attempt_draft.text or "").strip():
>     chosen = candidate
>     draft, verdict, outcome = (
>         attempt_draft, attempt_verdict, attempt_outcome,
>     )
>     break
> --- `virtual_context/core/engagement/runner.py`

> DRAFT_ATTEMPT_CAP = 3
> --- `virtual_context/core/engagement/runner.py`

> if channel_id not in STAGING_CHANNEL_IDS:
> --- `virtual_context/core/engagement/poster.py`

> if not message_id:
>     # The claim stands. The send may or may not have landed, and the day
>     # stays taken precisely because we cannot tell.
>     raise PostRefused("the send returned no message id; treating as failed")
> --- `virtual_context/core/engagement/poster.py`

### Claims

#### RT-CLM-compaction-fence
Label: Conditional stale-write fencing

Claimed operation: operation-owned compaction writes reject stale ownership, rather than silently inserting. SRC-1 `virtual_context/core/compaction_pipeline.py` documents the intended guard; inspected SQLite enforcement has an explicit mode-dependent countercase. This supports a conditional control, not a guarantee that every store write is fenced in every deployment.

> At ACTIVE
> raises ``CompactionLeaseLost``; at OBSERVE logs
> ``COMPACTION_FENCE_OBSERVED_MISMATCH`` without raising; at
> OFF silently no-ops so the env-var-driven rollback is a
> single-line configuration change.
> --- `virtual_context/storage/sqlite.py`

- implementation conclusion status: wired
- operation conclusion status: uninspected

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-assembled-context
Label: Assembled context to answer model

Consumer: chat/reader model. Channel: headless system text, provider-adapted continuation context or host-returned recall text, depending on route. Force: natural-language guidance/evidence interpreted by the model, not code-enforced truth or compliance. Horizon: current model invocation; repeated retention/retrieval can extend across conversation turns and sessions where state is saved. SRC-1 `virtual_context/tui/headless.py`, `virtual_context/core/tool_loop.py`, `virtual_context/mcp/server.py`. [RT-RTE-headless-chat](#rt-rte-headless-chat) and [RT-RTE-paging-loop](#rt-rte-paging-loop) retain delivery evidence; neither establishes activation or benefit. The OpenClaw route is specifically user-role text and must not be conflated with the headless system channel.

#### RT-BAP-engine-watermarks
Label: Engine state to payload selection

Consumer: retrieval assembler and compaction pipeline. Channel: symbolic checkpoint/index fields and current configuration. Force: code rules determine history offset/protected window and eligibility, rather than asking a model to honor a deletion instruction. Horizon: subsequent requests and restored checkpoints. SRC-1 `virtual_context/core/retrieval_assembler.py`, `virtual_context/core/compaction_pipeline.py`, `virtual_context/engine.py`. State persistence is conditional on [RT-OBJ-engine-state](#rt-obj-engine-state)'s save owner.

> elif "rule" in entry.tags or set(entry.tags) & current_tag_set:
>     filtered.extend(pair)
> --- `virtual_context/core/retrieval_assembler.py`

## Annotations

none
