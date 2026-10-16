---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Hindsight runtime baseline: HTTP reflection, bounded retrieval and synthesis, asynchronous retention, Claude Code hooks and configuration admission at the frozen commit."
run-id: AAS-2026-10-14-hindsight-34c2ca821edf-01
reviewed-boundary: "610c135b6f2d0d8b972da94146ae635943f36271"
---

# Hindsight runtime report

## Runtime account

### Work and inspected scope

Hindsight supplies memory production and retrieval, plus an inner model-driven answer loop. It does not own the external host's complete task execution. The boundary identifies packaged service and worker entry points, HTTP/MCP composition and the Claude Code caller ([boundary](boundary.md#boundary-and-evidence)). This report adds implementation inspection of the HTTP reflect handler, engine authentication and operation hooks, reflect dispatch and synthesis, retain orchestration, worker terminal handling, Claude Code transcript submission/context delivery, extension loading and bank configuration persistence. All new evidence belongs to SRC-1 at the frozen commit; no additional source or execution evidence is introduced.

The ordinary invocation traced here is a caller's HTTP `POST /v1/default/banks/{bank_id}/reflect`. The handler accepts a query, retrieval controls and output controls; it forwards them through a cancellable request to the engine. The engine authenticates, optionally validates the operation, obtains the bank identity/configuration, selects directives and binds bank-scoped retrieval callbacks. Code requests initial retrieval stages; the model subsequently proposes calls or completion. Hindsight dispatches the actual retrieval and returns tool results to its own next model invocation. Completion becomes a `ReflectResult`, then an HTTP response with text and optional supporting facts/traces. See [RT-RTE-reflect-request](#rt-rte-reflect-request) and [RT-CMP-reflect-llm](#rt-cmp-reflect-llm).

Three forcing cases test stronger readings of this path:

1. Context/iteration exhaustion replaces continued tool use with standalone synthesis, including parallel compression and reduction for large evidence sets. A successful answer therefore need not have completed every nominal retrieval step. See [RT-RTE-context-synthesis](#rt-rte-context-synthesis).
2. The Claude Code provider is an SDK/subprocess adaptation, not simply a native HTTP tool API. It suppresses built-in tools and host plugins and uses placeholder MCP handlers to collect proposed calls. The real retrieval executor remains Hindsight. Named tool choice is partly prompt-mediated on this provider. See [RT-RTE-provider-round](#rt-rte-provider-round).
3. Authentication is not a universal credential check: default tenancy passes requests, and trusted internal/MCP-marked contexts bypass tenant revalidation. This prevents interpreting an engine authentication call as a deployed security guarantee. See [RT-CLM-tenant-check](#rt-clm-tenant-check).

A separate write-and-later-consume path is shipped: Claude Code Stop hooks select transcript suffixes/windows and submit retention; UserPromptSubmit hooks query memories and emit `additionalContext`. The asynchronous worker and synchronous retain routes have different immediate returns and concurrency controls. See [RT-RTE-retain-work](#rt-rte-retain-work) and [RT-RTE-claude-hooks](#rt-rte-claude-hooks). Detailed memory revisions, consolidation judgments and epistemic warrant are left to the specialists; scheduling maintenance does not establish its successful execution.

### Ownership, controls and persistence

The requesting principal selects a bank/query and exposed options. No inspected route establishes whether that principal is human. The HTTP handler owns transport admission and disconnect handling; the engine owns tenant context and callbacks; reflect code owns the next-step protocol and hard dispatch surface; the configured model owns query wording, discretionary retrieval and answer formulation. Decisions combine symbolic code and natural-language instructions interpreted by distributed-parametric models. The immediate effect boundary is database retrieval plus provider calls, not arbitrary host task execution. Separate extension code has broader in-process authority ([RT-RTE-extension-load](#rt-rte-extension-load)).

Bank ID and tenant schema carry storage identity. Reflect also creates a logging identity; request context supplies cancellation and authentication state. Tool results and messages are current-run working state ([RT-OBJ-context-history](#rt-obj-context-history)). Facts, directives, mental models and configuration are later-readable database state; their distinct memory admission mechanisms are not collapsed into the runtime context object. Reflection's inspected request path returns an answer rather than demonstrating automatic retention of that answer (SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`).

Runtime-client controls include budget-derived iteration count, maximum context size, tool token ceilings, requested output length/schema, tag groups, fact-type and mental-model exclusions, and optional facts/traces in the HTTP return. Directive loading defaults to scoped active directives, while `apply_all_directives` asks the engine to load all active directives through its authorized listing method. This is not evidence that the model obeys them. Configuration changes can affect subsequent calls ([RT-RTE-config-update](#rt-rte-config-update)); startup environment can replace extension implementations. Current deployment grants, configured providers, credentials, filesystem/network isolation and host policies were not supplied.

Coordination is asynchronous Python orchestration, database-backed operation identity and worker execution. Expensive model calls do not require keeping a database connection open for the whole reflect. Parallel synthesis and queued retention move work across distinct executor paths, not independent autonomous agents with authority to launch arbitrary tasks (SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, `hindsight-api-slim/hindsight_api/engine/reflect/agent.py`, `hindsight-api-slim/hindsight_api/worker/poller.py`).

### Load-bearing guarantees and countercases

| Guarantee or policy | Owner and enforcement | Strength and covered paths | Countercase, external contract and conclusion |
|---|---|---|---|
| Only recognized, enabled retrieval tools reach reflect callbacks | Reflect dispatcher checks `enabled_tools` and dispatches named branches | invariant at this dispatcher; normal reflect model-call results | Does not sandbox extension code or provider implementation. Provider/SDK and callback code must honor their own contracts. implementation conclusion status: wired; operation conclusion status: uninspected. [RT-RTE-reflect-request](#rt-rte-reflect-request) |
| Gather evidence before completion | Forced tool-choice sequence plus feedback when early `done` lacks evidence IDs | policy; ordinary loop before its terminal iteration | Last-iteration synthesis and provider-mediated tool choice prevent a universal evidence-grounding invariant. Gathered IDs also do not prove answer correctness. implementation conclusion status: wired; operation conclusion status: uninspected. [RT-RTE-context-synthesis](#rt-rte-context-synthesis), [RT-RTE-provider-round](#rt-rte-provider-round) |
| Limit abandoned/overlong work | HTTP disconnect wrapper, cancellation checkpoints and engine `wait_for` | best effort; HTTP reflect and cooperative nested operations | Direct engine callers must supply cancellation state; provider/network cancellation behavior is external. No deployed latency bound or cost bound established. implementation conclusion status: wired; operation conclusion status: uninspected. [RT-RTE-reflect-request](#rt-rte-reflect-request) |
| Authenticate tenant and select schema | Engine context variable and configured tenant extension | protocol, not default credential enforcement | Internal, MCP-authenticated and memoized contexts avoid fresh validation; default extension does not authenticate. Caller trust and deployment configuration are necessary. implementation conclusion status: wired; operation conclusion status: uninspected. [RT-CLM-tenant-check](#rt-clm-tenant-check) |
| Track deferred/failed/completed worker operations | Poller terminal writes, backoff and restart/recovery path | best effort; queued operations handled by this poller | Requires database availability and actual restart. Completion metrics are not authoritative success evidence for every executor-handled failure; use stored status. Not an exactly-once whole-pipeline claim. implementation conclusion status: wired; operation conclusion status: uninspected. [RT-RTE-retain-work](#rt-rte-retain-work) |
| Admit consistent configuration writes | Engine authorization and resolver transaction locking the bank row | invariant for the inspected persistence transaction, protocol for caller authorization | Startup configuration and arbitrary Python extensions are alternate authority paths. Database transaction semantics and trusted internal helpers remain required. implementation conclusion status: wired; operation conclusion status: uninspected. [RT-RTE-config-update](#rt-rte-config-update) |

Each scope is implementation-local. No trace establishes exercised operation, activation of supplied knowledge or benefit. Uninspected material includes the full MCP transport/tool implementation, most SDK/CLI and embedded launch paths, other integrations, recall ranking/reranking internals, complete consolidation and mental-model refresh admission, UI mutations, deployment configuration and evaluators. They remain available evidence, not absences or access failures. This report does not upgrade the boundary to whole-system coverage.

## Shared records

### Components

#### RT-CMP-reflect-llm
Label: Configured reflection model

Source-native identity is `_reflect_llm_config`, built from `LLMConfig(provider=reflect_provider, ... model=reflect_model)` and resolved configuration for a bank/operation. Representational form is distributed-parametric; parameters reside in provider-managed models or the selected local serving system, not in the configuration row. The configuration handle is symbolic. SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py` establishes construction and use.

> model=reflect_model,
> reasoning_effort=config.reflect_llm_reasoning_effort or config.llm_reasoning_effort,
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

Parameters changing during operation: provider-internal behavior is uninspected; the inspected request route performs inference/configuration, not a visible parameter-training step. Exact version pinned: no immutable weight identity is established by this configurable model name. Mutable endpoint resolving to another model: possible through configured provider/base URL and provider-side resolution; a frozen repository does not freeze serving weights. Operation and output quality are uninspected. The same configured reflection machinery supplies the final synthesis route; separate compression calls do not establish independent training.

#### RT-CMP-retain-llm
Label: Configured retention model

Identity is `_retain_llm_config.with_config(resolved_config, bank_id=bank_id, operation="retain")`. Distributed-parametric model state is provider/local-server substrate; the engine supplies extracted content and configuration, and the orchestrator extracts facts before embedding. This is a distinct operation configuration from the reflection model even when they resolve to the same underlying provider model. SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, `hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py`.

> retain_llm = self._retain_llm_config.with_config(resolved_config, bank_id=bank_id, operation="retain")
> result = await self._retain_batch_with_append_retry(
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

Parameters changing during operation: provider internals uninspected; visible route requests inference, not training. Exact version pinned: unestablished, because runtime configuration supplies model selection. Mutable endpoint substitution: possible for remote/configurable providers; actual endpoint and model identity uninspected. This route establishes a transformation request and storage capacity, not accurate extraction or improved future action.

#### RT-CMP-embeddings
Label: Configured embeddings implementation

Identity is the engine's `embeddings` implementation supplied explicitly or created from configuration. Distributed-parametric model state is local model files or a remote embedding service; generated vectors are dense numerical outputs, not those weights. The factory includes local SentenceTransformer, ONNX and remote variants. Newly inspected scope is the factory selection and OpenAI-compatible configuration, not all providers. SRC-1, `hindsight-api-slim/hindsight_api/engine/embeddings.py`.

> provider = config.embeddings_provider.lower()
> --- `hindsight-api-slim/hindsight_api/engine/embeddings.py`

> self.model = model
> self.base_url = base_url
> self.batch_size = batch_size
> --- `hindsight-api-slim/hindsight_api/engine/embeddings.py`

Parameters changing during operation: inference is the inspected consumption path; local model initialization/remote internal updates are not fully inspected. Exact version pinned: unestablished for the configured deployment, including local artifact revision. Mutable endpoint substitution: remote base URLs/model names can resolve to changed serving state; local factory alternatives have no remote endpoint requirement. These alternatives are opaque at the deployed-instance level, not assumed equivalent. Retain embeds augmented fact text; reflection mental-model search embeds its query (SRC-1, `hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py`, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`). Reranker model identity and mutability remain uninspected; no all-model inventory is claimed.

### Operative objects

#### RT-OBJ-context-history
Label: Reflection working context

Source-native identities are `messages` and `context_history`. Both are current-invocation Python lists containing natural-language evidence and symbolic role/tool-call envelopes; they are not assumed cross-invocation retained memory. Model-visible tool results can be blanked while the full history remains available to synthesis. These operative parts differ in consumer but share the current request lifetime. SRC-1, `hindsight-api-slim/hindsight_api/engine/reflect/agent.py`; evidence and transformation are retained in [RT-RTE-context-synthesis](#rt-rte-context-synthesis).

#### RT-OBJ-bank-config
Label: Bank configuration overrides

Source-native identity is the bank row's `config` JSON mapping. Representational form is symbolic for field names/values consumed by fixed resolver rules; any prompt-bearing text has natural-language authority at its later model consumer, not at the JSON merge itself. Storage is the database `banks.config` column. This runtime record covers configuration admission, not the memory specialist's individual retained-content objects. SRC-1, `hindsight-api-slim/hindsight_api/config_resolver.py`; [RT-RTE-config-update](#rt-rte-config-update) retains the write evidence.

### Routes

#### RT-RTE-reflect-request
Label: HTTP reflection request

Endpoints are HTTP caller → handler → `reflect_async` → `run_reflect_agent` → configured model and scoped retrieval callbacks → `ReflectResult` → HTTP response. The caller supplies bank/query and exposed controls. Handler dependencies perform precheck/admission; the engine authenticates and optionally validates, binds scope, loads identity/directives and resolves configuration. Code owns forced initial search selection and dispatch; the model proposes queries and optional later calls. JSON call envelopes are symbolic; query, identity and retrieved content are natural-language model inputs. [RT-CMP-reflect-llm](#rt-cmp-reflect-llm) and [RT-CMP-embeddings](#rt-cmp-embeddings) supply numerical computation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Answer text, structured output/error and usage; supporting facts and tool/LLM traces are conditionally included by HTTP request controls.
- Later read-back: Stored bank facts, mental models and directives can reach this later invocation; no automatic storage of the returned answer is established by this request path.
- Delegated visibility: Scoped callbacks receive bank, request context and selection controls; providers receive assembled model messages, not arbitrary database access from the model tool name alone.
- Selection predicate: Code-derived forced sequence depends on enabled mental-model/observation/recall tools; discretionary calls use model-generated queries; callbacks apply tags/groups, fact-type and date controls where supplied.
- Invalidation or expiry: Cancellation checkpoints and wall timeout bound request lifetime; durable content invalidation is outside this route's inspected write scope.
- Activation or effect: Retrieval supplies evidence to subsequent model calls and answer construction; actual reliance and changed external-host behavior are unobserved.
- Evidence limits: Static implementation only; full recall ranking, all callback internals, MCP/embedded equivalence and deployed grant set are uninspected.

Operating mode: open query answering, not a bounded experiment/curriculum. Proposal role: model proposes retrieval/answer. Decision/veto roles: code restricts enabled tools, validators can reject the operation and the caller can cancel; no per-answer human approval gate is established. Answer oracle: none identified in the inspected answer path; model judgment and cited facts are not reference outcomes.

SRC-1, `hindsight-api-slim/hindsight_api/api/http.py`, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, `hindsight-api-slim/hindsight_api/engine/reflect/agent.py`.

> core_result = await run_cancellable_on_disconnect(
>     http_request,
>     request_context,
>     app.state.memory.reflect_async(
> --- `hindsight-api-slim/hindsight_api/api/http.py`

> if enabled_tools is not None and tool_name not in enabled_tools and tool_name != "done":
>     return {"error": f"Tool '{tool_name}' is not available. Use only the tools provided to you."}
> --- `hindsight-api-slim/hindsight_api/engine/reflect/agent.py`

> await self._validate_operation(self._operation_validator.validate_reflect(ctx))
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

HTTP maps no-answer/tool failures to explicit failures rather than successful placeholder answers. Optional `based_on` is a formatted selection of retrieved/declaratively used material, not independent evidence of causal reliance. The engine prefers mental-model read contents over search snippets where available (SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`).

#### RT-RTE-context-synthesis
Label: Budget-triggered final synthesis

Endpoints are the ordinary reflect loop → working-message compaction or budget termination → standalone final prompt → optional parallel map calls → reduce call → length/schema postprocessing → answer. Code, not the foreground agent or user, triggers this change in working context. Earlier tool-result bodies are blanked oldest-first when a required retrieval step must fit; full current-run history remains reachable by the final synthesizer. This resembles removing values from a window while retaining a separate backing copy, not popping an independent sub-agent task frame. Each compression model invocation has a selected evidence slice; its prose result crosses into reduction, so raw evidence is not guaranteed to survive unchanged.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Final synthesized answer or a no-answer exception; no further retrieval on the terminal iteration.
- Later read-back: inapplicable — working-history fallback belongs to this invocation, not accumulated cross-invocation state.
- Delegated visibility: Parallel map calls receive separate evidence chunks and the query; the reduce call receives generated claim sections rather than necessarily every original evidence byte.
- Selection predicate: Iteration limit, context-budget checks and prior compaction determine the branch; `split_context_history` partitions evidence for synthesis.
- Invalidation or expiry: Current-run messages/history expire with the request; cancellation and engine timeout still bound the enclosing operation.
- Activation or effect: Different prompts and evidence transformations feed the final model; preservation of every relevant claim and answer benefit remain unobserved.
- Evidence limits: Splitter and all prompt builders were located but not exhaustively inspected; comments saying SPLIT rather than truncated do not establish lossless semantic preservation.

Operating mode remains open-request answering. Code selects branch and partitioning; the model performs compression and synthesis. No expected-answer oracle or per-compression human approval is established. This is evidence compression, not an independently established theory-criticism loop. SRC-1, `hindsight-api-slim/hindsight_api/engine/reflect/agent.py`.

> if is_last:
>     # Out of iterations: no more retrieval, just the answer.
>     return await (_forced_final_synthesis if compacted else _finish)(iteration + 1)
> --- `hindsight-api-slim/hindsight_api/engine/reflect/agent.py`

> if message.get("role") == "tool":
>     messages[index] = {**message, "content": _COMPACTED_TOOL_RESULT}
>     compacted = True
>     estimated_tokens = _count_messages_tokens(messages)
> --- `hindsight-api-slim/hindsight_api/engine/reflect/agent.py`

> prompt = build_reduce_prompt(
>     query,
>     list(claim_sections),
>     bank_profile,
>     context,
>     max_tokens=max_tokens,
>     llm_output_language=llm_output_language,
> )
> --- `hindsight-api-slim/hindsight_api/engine/reflect/agent.py`

#### RT-RTE-provider-round
Label: Claude Code provider round

Endpoints are Hindsight messages/tool definitions → Claude Agent SDK options and isolated CLI environment → collected proposed tool calls → Hindsight reflect dispatcher. Provider code registers placeholder SDK MCP handlers; these are not the memory retrieval callbacks. Hindsight owns subsequent real execution. Message roles are flattened into system/user text, including prior assistant and tool-result content, which changes representation from provider-native conversational envelopes. SRC-1, `hindsight-api-slim/hindsight_api/engine/providers/claude_code_llm.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Model text/tool proposals and usage to the enclosing Hindsight loop.
- Later read-back: inapplicable — this adapter round handles current messages; isolated CLI plugin configuration is static operational state, not an experience write.
- Delegated visibility: SDK model sees flattened messages and selected MCP tool schemas; built-in CLI tools are disabled in supplied options.
- Selection predicate: `tool_choice` filters allowed MCP names and adds instructions for required/named calls; SDK round limit is one.
- Invalidation or expiry: Per-call SDK client closes after receipt; isolated configuration directory is process-lifetime state.
- Activation or effect: Proposed calls are returned for Hindsight dispatch; compliance with prompt-mediated forced choice and actual CLI isolation are not observed.
- Evidence limits: External SDK/CLI implementation, other provider adapters, remote endpoint behavior and deployment filesystem isolation are outside this inspection.

> options = ClaudeAgentOptions(
>     system_prompt=system_prompt if system_prompt else None,
>     tools=[],  # Disable built-in tools so MCP tools load eagerly
>     max_turns=1,  # One round: propose tool calls (or answer); caller drives the loop
>     mcp_servers=mcp_servers_config,
>     allowed_tools=allowed_tool_names,
> --- `hindsight-api-slim/hindsight_api/engine/providers/claude_code_llm.py`

> _isolated_claude_env = {
>     "CLAUDE_CONFIG_DIR": path,
>     "CLAUDE_SECURESTORAGE_CONFIG_DIR": "",
> }
> --- `hindsight-api-slim/hindsight_api/engine/providers/claude_code_llm.py`

This suppresses a recursive host-plugin retention route by supplying separate CLI configuration. It is not an OS sandbox or proof that all installed extension code lacks shell/network access. Named tool-choice requests on this provider have policy/protocol strength, not a reliable model-compliance invariant.

#### RT-RTE-retain-work
Label: Synchronous and queued retention

Endpoints are caller content → synchronous `retain_batch_async` or `submit_async_retain` → validated contents → extraction/embedding/storage → post-insert maintenance scheduling. Queued calls add durable operation payloads, worker claim/execution and terminal status. Caller supplies proposed source content, identities/tags and strategy; optional operation validator can reject or replace content. The model proposes extracted facts; code processes representations and storage. Extraction and storage are not per-content human approval. [RT-CMP-retain-llm](#rt-cmp-retain-llm) and [RT-CMP-embeddings](#rt-cmp-embeddings) are distinct computational stages.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Synchronous path returns unit IDs/usage as requested; queued path returns operation acknowledgement/status rather than proof of completed memory production.
- Later read-back: Inserted facts and retrieval links can be consumed by later recall/reflect; observations/graph/index maintenance is separately scheduled and can fail without failing the producing operation.
- Delegated visibility: Workers receive task payload, bank and schema; extraction models receive selected content/configuration; full provider-visible prompt construction is not exhaustively inspected.
- Selection predicate: Retain input, document IDs, update mode and strategy control ingestion; queued duplicate document IDs are rejected while synchronous same-document inputs can be folded sequentially.
- Invalidation or expiry: Append conflicts trigger bounded in-process redo and worker deferral; failed/finished/deferred operation states are persisted. Detailed deletion and memory expiry remain for specialist inspection.
- Activation or effect: Model extraction, embedding and database writes are wired; storage truth, subsequent use and benefit are not execution observations.
- Evidence limits: Storage-owned alternatives, complete extraction/defense admission, consolidation revisions and full worker claim/recovery implementation remain partially inspected; no universal whole-document atomicity or exactly-once guarantee.

Change admission: source content triggers model-derived knowledge proposals under extraction configuration; optional validators can replace/reject ingress, and code/storage checks can reject invalid state. Rollback/recovery is local to transactional storage and append/worker handling, not an established semantic restoration of all prior knowledge. Operating mode: open ingestion, with queued maintenance; no inspected answer oracle. Human authorship/control of submitted content remains unresolved.

SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, `hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py`, `hindsight-api-slim/hindsight_api/worker/poller.py`.

> if result and result.contents is not None:
>     contents = cast(list[RetainContentDict], result.contents)
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

> extraction = await fact_extraction.extract_facts_from_contents(
>     contents,
>     llm_config,
>     config,
>     pool,
>     operation_id,
>     schema,
>     attachment_loader=attachment_loader,
>     vlm_config=vlm_config,
> )
> --- `hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py`

> unit_ids = await fact_storage.insert_facts_batch(conn, bank_id, processed_facts, ops=ops)
> --- `hindsight-api-slim/hindsight_api/engine/retain/orchestrator.py`

> if config.enable_observations and config.enable_auto_consolidation:
>     try:
>         await self.submit_async_consolidation(bank_id=bank_id, request_context=request_context)
>     except Exception as e:
>         logger.warning(f"Failed to submit consolidation task for bank {bank_id}: {e}")
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

> except RetryTaskAt as e:
>     # Retry is not a terminal outcome — do not record a completion.
>     retry = e
>     await self._write_terminal(
>         task, "retry", lambda: self._schedule_retry_all(task, retry.retry_at, str(retry))
>     )
> --- `hindsight-api-slim/hindsight_api/worker/poller.py`

Terminal DB writes retry with backoff and request process shutdown on deadline so recovery can occur on restart. Metrics can count executor-handled failures as success; database status is the stronger completion signal. Caller-supplied operation UUID supports submission replay handling, but that scoped mechanism does not prove exactly-once effects across the entire pipeline.

#### RT-RTE-claude-hooks
Label: Claude Code transcript and context hooks

Endpoints are host Stop transcript → retention selector/formatter → client retain → later host UserPromptSubmit → recall query → score filtering/formatting → stdout `additionalContext`. Host event scheduling supplies the trigger; shipped code selects content and bank. Chunked retention uses turn windows/overlap; full-session mode submits a not-yet-retained suffix under distinct document identities and commits local progress after the client call returns. An empty formatted transcript also commits progress without submission. The hook configuration declares asynchronous Stop execution. Local progress is therefore neither proof of submission in every branch nor proof of completed server ingestion.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Retain produces diagnostic output; recall emits JSON context to the host when results survive filtering.
- Later read-back: Retained transcript-derived facts may be requested on a subsequent prompt; the recall hook also saves its last formatted context in local state for diagnostics.
- Delegated visibility: Server receives formatted selected transcript, metadata/tags/document identity; external Claude Code receives formatted recall text, not necessarily the original complete transcript.
- Selection predicate: Retention role/tool-call settings and suffix/window logic; recall prompt length/context-turn cap, query/bank filters, optional extra banks and numeric score floors.
- Invalidation or expiry: Local progress avoids resending prior full-session prefixes; config controls hook disabling. Complete local-state collision/cleanup and server deletion behavior are uninspected.
- Activation or effect: Hook output supplies a context channel to the external model; actual host loading, reliance and improvement are unobserved.
- Evidence limits: Client transport and state-helper internals are not fully traced; all other integrations and SessionStart/SessionEnd script responsibilities remain uninspected.

Automatic trace-fed write: user/assistant transcript content and optionally tool-call content enter retention without per-submission human content approval. The later consumer receives formatter output after score filtering, rather than every retained item. This is a standing behavioral-input path, not evidence of exercised self-improvement. The host's own context compaction/isolation is outside Hindsight's inspected responsibilities.

Operating mode: recurring event-driven open use. Proposer: host transcript plus code selection and server extraction. Decider/veto: hook settings/selectors, client failure and server admission; user control is configuration-level, not a demonstrated human judgment of each retained fact. No answer oracle is identified. Recovery: errors are reported or degrade silently according to debug behavior; no guarantee of retry until completion.

SRC-1, `hindsight-integrations/claude-code/hooks/hooks.json`, `hindsight-integrations/claude-code/scripts/retain.py`, `hindsight-integrations/claude-code/scripts/recall.py`.

> if retention_progress is not None:
>     commit_retention(session_id, len(all_messages), retention_progress.chunk_index)
> debug_log(config, f"Retain response: {json.dumps(response)[:200]}")
> --- `hindsight-integrations/claude-code/scripts/retain.py`

> results = filter_by_min_scores(results, config.get("recallMinScores") or {}, config)
> --- `hindsight-integrations/claude-code/scripts/recall.py`

> output = {
>     "hookSpecificOutput": {
>         "hookEventName": "UserPromptSubmit",
>         "additionalContext": context_message,
>     }
> }
> json.dump(output, sys.stdout)
> --- `hindsight-integrations/claude-code/scripts/recall.py`

#### RT-RTE-config-update
Label: Bank configuration admission

Endpoints are engine update/reset call → authentication and scoped-caller refusal → optional bank-write validator → field/policy validation → serialized bank-row JSON update → later resolved operational configuration. The caller proposes the mapping; human versus software authorship is unresolved. Code and configured permission/validator hooks decide/reject; no model proposes this inspected config update. Configuration affects behavior, so persistence is not merely telemetry.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Current bank configuration state after update/reset or a validation/authorization error.
- Later read-back: Resolver supplies persisted overrides to future bank operations including configured model calls.
- Delegated visibility: Tenant hooks receive request/bank context; resolver consumes validated fields, not unrestricted arbitrary Python from this mapping.
- Selection predicate: Requested keys, configurable-field/type/cross-field rules and tenant allowed-field controls; scoped callers cannot perform bank-wide config edits.
- Invalidation or expiry: Reset removes overrides; explicit subsequent update can replace fields. Full history-based rollback and cache invalidation implementation are uninspected.
- Activation or effect: Resolver output is supplied to retain/reflect call configuration; actual changed calls in a deployed instance are unobserved.
- Evidence limits: Preauthorized-update branch exists; its token production was not fully traced. No universal guarantee against trusted helper/extension/database mutation is asserted.

Admission trigger is a caller update/reset request; persisted result is JSON overrides. Guidance is fixed configuration validation and permission policy, not an evaluated improvement proposal. Human content approval and expected-answer oracle are not established. Operating mode is open administrative mutation. Recovery includes rejected validation before bank creation and transaction failure rather than a scored rollback policy.

SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, `hindsight-api-slim/hindsight_api/config_resolver.py`.

> await self._authenticate_tenant(request_context)
> await self._refuse_bank_wide_if_scoped(bank_id, request_context, "change the bank's config")
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

> SELECT config FROM {fq_table("banks")} WHERE bank_id = $1 FOR UPDATE
> --- `hindsight-api-slim/hindsight_api/config_resolver.py`

> UPDATE {fq_table("banks")}
> SET config = COALESCE(config, '{{}}'::jsonb) || $1::jsonb,
>     updated_at = now()
> WHERE bank_id = $2
> --- `hindsight-api-slim/hindsight_api/config_resolver.py`

#### RT-RTE-extension-load
Label: Environment-configured extension admission

Endpoints are startup environment `module.path:ClassName` → Python import → subclass validation → constructor → optional extension context → in-process hooks or mounted HTTP routers. Environment-setting principal proposes the replacement; loader validates shape but does not prove safe implementation. This admits capabilities/control policy, distinct from model-selected reflect tools.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Extension instance or load error; none when no extension is configured.
- Later read-back: inapplicable — this inspected route loads startup configuration/code rather than experience accumulated through use.
- Delegated visibility: Extension receives configuration and optionally engine system context; HTTP extensions can mount routers with the memory engine.
- Selection predicate: Environment prefix selects import path; class must inherit the requested base class.
- Invalidation or expiry: Process/configuration reload can select another implementation; hot reload and automatic rollback are uninspected.
- Activation or effect: Imported Python and constructor run in the service process; optional HTTP router is mounted by API construction.
- Evidence limits: Actual configured extensions, operator review, package supply chain and OS isolation are uninspected; subclass checks do not restrict filesystem/network effects.

Admission trigger: environment configuration at loading. Proposed change: executable extension implementation and config. Decision/rejection: loader rejects malformed paths, imports/class mismatch and construction failure; it has no inspected semantic safety approval. Human approval and rollback are unresolved. Persisted guidance is operator/package configuration, not an automatic theory revision or outcome-scored experiment. Operating mode: configurable startup extension. Answer oracle: inapplicable to loading code.

SRC-1, `hindsight-api-slim/hindsight_api/extensions/loader.py`, `hindsight-api-slim/hindsight_api/api/http.py`.

> module = importlib.import_module(module_path)
> --- `hindsight-api-slim/hindsight_api/extensions/loader.py`

> extension = ext_class(config)
> --- `hindsight-api-slim/hindsight_api/extensions/loader.py`

> extension_router = http_extension.get_router(memory)
> --- `hindsight-api-slim/hindsight_api/api/http.py`

### Claims

#### RT-CLM-tenant-check
Label: Tenant authentication is configuration-dependent

Claimed operation: engine authentication selects a tenant schema through an extension, but is not universal credential enforcement. Default implementation is no-auth; internal/MCP-authenticated request contexts bypass extension revalidation. SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, `hindsight-api-slim/hindsight_api/extensions/builtin/tenant.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> if request_context.internal:
>     return _current_schema.get()
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

> if request_context.mcp_authenticated:
>     return _current_schema.get()
> --- `hindsight-api-slim/hindsight_api/engine/memory_engine.py`

> async def authenticate(self, context: RequestContext) -> TenantContext:
>     """Return configured schema without any authentication."""
>     return TenantContext(schema_name=self._schema)
> --- `hindsight-api-slim/hindsight_api/extensions/builtin/tenant.py`

ApiKeyTenantExtension adds equality-check rejection when configured. This does not establish deployed credentials, MCP transport verification or resistance to malicious in-process callers constructing trusted contexts. The strongest warranted conclusion is a wired configurable protocol, with a necessary trust boundary around internal Python callers and authenticated transport marking.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-hook-context
Label: Retrieved memories in external host context

Consumer: external Claude Code model/runtime. Channel: hook `additionalContext` containing formatted recall results after query and score selection. Force: natural-language information and configured preamble interpreted by the host model, not a fixed-rule instruction-enforcement gate. Horizon: later prompt invocations, potentially across sessions through server retention; actual deployed horizon is unobserved. Evidence is [RT-RTE-claude-hooks](#rt-rte-claude-hooks), SRC-1, `hindsight-integrations/claude-code/scripts/recall.py`. Delivery is wired; activation and benefit remain uninspected.

#### RT-BAP-config-consumer
Label: Configuration in later operation selection

Consumer: engine/configuration resolver and provider construction/call configuration. Channel: persisted bank overrides resolved before retain/reflect. Force: symbolic field rules select runtime settings; any text ultimately supplied to models has interpretive rather than invariant compliance strength. Horizon: later operations until reset/replacement. Evidence is [RT-RTE-config-update](#rt-rte-config-update), [RT-CMP-reflect-llm](#rt-cmp-reflect-llm), [RT-CMP-retain-llm](#rt-cmp-retain-llm), SRC-1, `hindsight-api-slim/hindsight_api/engine/memory_engine.py`, `hindsight-api-slim/hindsight_api/config_resolver.py`. Wiring does not prove exercised improvement.

## Annotations

none
