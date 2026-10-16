---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Hermes Agent runtime baseline: one-shot invocation, tool-effect controls, delegation, executable extensions and Codex alternate runtime at the frozen commit."
run-id: AAS-2026-10-14-hermes-agent-bfb4bdc54d37-01
reviewed-boundary: "0e427d788d253630d38a3a51cd76849e73cd6925"
---

# Hermes Agent runtime report

## Runtime account

Hermes performs model-directed work through a shipped caller, an agent turn loop and effectful tools. Its declared work also includes session recall, skill creation, scheduled automation and messaging-platform delivery. The learning and self-improvement descriptions are product claims, not demonstrated results here ([RT-CLM-product-work](#rt-clm-product-work)). The [boundary](boundary.md) remains a complete artifact with partial loop inspection. All findings below use SRC-1 at the reviewed commit. No target execution, supplied execution trace or causal experiment supports operation, activation or benefit.

### Ordinary invocation

The selected ordinary path is the shipped non-interactive `hermes -z` caller, not a minimal library example. [RT-RTE-oneshot-turn](#rt-rte-oneshot-turn) traces prompt admission to terminal output. `run_oneshot` validates explicit provider/toolset choices, configures a finite stateless channel, suppresses progress output and builds an `AIAgent`. `_run_agent` opens a session store, resolves optional resumed history and its stored model route before resolving provider credentials, waits for MCP discovery, and supplies toolsets, reasoning configuration and optional preloaded skill text. Resolution-time fallback can select a different model before construction (SRC-1 `hermes_cli/oneshot.py`).

Turn setup copies supplied history, appends the current user message, binds task and turn identities, restores the primary runtime and refreshes MCP tools. The system prompt is restored or built and cached; the session row is created before turn-start compaction. A task ID is caller-supplied or a UUID; the turn ID combines session/task identity with another suffix, and API request IDs extend the turn ID. Gateway callers can reuse an agent across turns; per-turn compression and failure flags are reset (SRC-1 `agent/turn_context.py`, `agent/conversation_loop.py`).

Code owns the phase order, retries, iteration budget and termination conditions. The model owns the next content/tool proposal within the supplied context and schemas. The loop assembles a request, runs preflight controls, builds provider arguments, calls through LLM execution middleware, checks and normalizes the response, then chooses tool execution or text finalization. [RT-CMP-inference-model](#rt-cmp-inference-model) describes the numerical decision component. Provider transport modes and plugins can alter request/response handling; they are not evidence that all providers share one operational contract (SRC-1 `agent/turn_api_call.py`, `agent/transports/__init__.py`).

[RT-RTE-tool-dispatch](#rt-rte-tool-dispatch) covers generic tool rounds. The round validates names, expands local batches, caps/deduplicates calls and stages the assistant/tool-call row. It attempts a canonical append before executing. Singleton calls use sequential execution; larger batches are planned as parallel segments separated by sequential barriers. Dispatch distinguishes live-agent inline tools, delegation, context-engine tools, memory-provider tools and registry tools (SRC-1 `agent/turn_tool_round.py`, `run_agent.py`, `agent/tool_executor.py`). The capability surface is wider than the current grant set: selected toolsets and valid names constrain normal dispatch, while configured providers/backends and installed plugins determine available implementations. No deployment configuration is supplied, so the actual grant set and isolation envelope are unobserved.

A tool's raw result is not necessarily what the next model receives. Commit code can spill oversized content, transform multimodal text, append subdirectory hints, adapt content to the active model and append a tool row. It flushes before projecting completion; a reported append failure stops later model use of process-only results. These are source-wired handling steps, not guarantees of complete or truthful tool output (SRC-1 `agent/tool_executor.py`). Finalization shapes the transcript tail, applies output transforms, optionally micro-compacts, persists, syncs external memory and may schedule review. The wrapper exports the turn boundary after history changes. One-shot then prints final text, writes an optional usage report and runs bounded/best-effort cleanup of background completions, lifecycle, memory provider, agent and session store (SRC-1 `agent/turn_finalizer.py`, `agent/conversation_loop.py`, `hermes_cli/oneshot.py`).

### Controls and forcing cases

Four source cases bound the tempting claim that all consequential effects pass through one approval/durability gate:

1. **Finite one-shot approval:** the shipped caller itself sets YOLO and hook acceptance. Recoverable approval is not a mandatory human veto in this path. Terminal guards still have separate floors, but isolated-backend fast paths skip most command guards and retain user deny checks ([RT-RTE-command-approval](#rt-rte-command-approval)).
2. **Arbitrary Python:** `execute_code` admits a whole script, with local or remote execution and a persistent local kernel. RPC tools have an allowlist and call budget; direct Python subprocess/file operations do not become terminal tool calls. The tool's own documentation explicitly distinguishes its security envelope from an isolation jail ([RT-RTE-code-execution](#rt-rte-code-execution)).
3. **Delegated work:** child contexts, sessions and budgets differ from the parent. The parent's top-level background request becomes synchronous when finite-session delivery is unsupported; durable-capable clients can instead receive a later stored completion without a model wake ([RT-RTE-child-delegation](#rt-rte-child-delegation)). Context isolation is not filesystem or OS isolation.
4. **Codex app-server:** an opt-in mode hands the whole turn to a subprocess before the generic tool loop. Native command/file operations follow Codex's policy and Hermes request callbacks, while transcript rows are projected afterwards. Generic persist-before-tool ordering therefore does not cover these native effects ([RT-RTE-codex-turn](#rt-rte-codex-turn)).

The generic durability fence is an implementation invariant **conditional on an enabled working session store and dispatch through `run_tool_round`**. Its owner is Hermes' tool-round code; the enforcement point is the flush result tested before `_execute_tool_calls`. Its external contract is the session store's successful canonical append and underlying SQLite/storage durability. It does not promise an atomic transaction spanning transcript and external effects, exactly-once effects after recovery, or durability when persistence is disabled. The flush helper returns `None` for no store or persistence-isolated agents; the round aborts specifically on `False`, so the source disproves an unconditional durability interpretation. Codex native effects and in-script RPC calls are materially different alternate paths (SRC-1 `agent/session_persistence.py`, `agent/turn_tool_round.py`, `tools/code_execution_rpc.py`, `agent/codex_runtime.py`).

- generic durability implementation conclusion status: wired
- generic durability operation conclusion status: uninspected
- generic durability guarantee strength: invariant

Approval is a configurable **policy**, not a deployed isolation guarantee. Its owner is Hermes approval code plus the caller-provided human transport; its enforcement points are terminal/script entry guards and plugin escalation. Coverage depends on backend classification, configured bypasses, caller presence and per-session/permanent decisions. Source-enforced vetoes on these routes do not sandbox arbitrary extension code, direct subprocesses inside approved Python, or external native tools. External backends must supply the isolation they advertise; no actual mount, credentials or remote sandbox configuration is available (SRC-1 `tools/approval.py`, `tools/code_execution_tool.py`, `hermes_cli/plugins_loader.py`).

- approval implementation conclusion status: wired
- approval operation conclusion status: uninspected
- approval guarantee strength: policy

### Other shipped paths and change admission

Interactive CLI, legacy CLI, gateway, ACP and scheduler are shipped target entry paths, not excluded host applications. The boundary establishes script routing. Additional inspection found gateway code binding a per-session notification callback around the conversation call and ACP code binding interactive/edit-approval context and passing its managed history into the same API (SRC-1 `gateway/run_turn_runner.py`, `acp_adapter/server.py`). Search also located CLI and cron callers. Their complete admission, inbound authorization, resume, scheduler delivery and cleanup paths remain uninspected; this prevents cross-frontend equivalence and whole-system security claims.

Executable capability admission is not limited to selecting preinstalled tools. Plugin manifest gating, loading, registration and failure cleanup admit tool/hook/provider implementations ([RT-RTE-plugin-admission](#rt-rte-plugin-admission)); [RT-BAP-plugin-handler](#rt-bap-plugin-handler) describes their force. Configuration contributes the enable/disable decision and override grant; code imports and registers the selected plugin, with an optional separate plugin-host process. Human authorship or per-content human approval of a configuration change is not established merely by reading that config. Shell/Python/file access can also modify product or production files reachable in the selected backend. Such edits are admitted as ordinary effects, not by an inspected product-quality successor selector. Repository update/install mechanisms and plugin-host internals are not traced here, preventing an exhaustive account of production-machinery change.

Retained knowledge/skill changes can be requested in the foreground tool loop or by post-turn review. [RT-RTE-review-handoff](#rt-rte-review-handoff) establishes the trigger and handoff, not the revisions, write safeguards or later consumption. Those belong to the memory analyst. The review trigger is not itself an answer oracle, formulated criticism, learning result or exercised self-improvement. No theory route is classified in this report.

Working-context control is visible at the runtime seams: copied caller history, cached system prompts, refreshed tool schemas, pre-API pressure gating, post-tool compression and post-turn micro-compaction. Preflight compares assembled request pressure including request-only injections and schemas, not just transcript size; it can stop ineffective proactive passes while leaving provider-overflow recovery eligible. Exact summary retention, preferential removal, reload and model compliance remain for specialist inspection (SRC-1 `agent/turn_context.py`, `agent/turn_preflight_gate.py`, `agent/turn_tool_round.py`, `agent/turn_finalizer.py`). Delegation supplies a clearer frame-like mechanism: a separate child receives selected goal/context rather than the parent's full live window, and a result crosses back. The analogy stops at OS effects and retained child sessions, which do not disappear merely when the parent's context drops the child result.

Added coverage is implementation-level bounded inspection of the files cited in this member: one-shot construction/cleanup; turn setup, phase dispatch and finalization; tool-round validation/flush and executor dispatch/result commit; approval guards; Python/RPC/kernel admission; delegation construction, dispatch and child waiting; plugin gating/loading/registration; Codex session/persistence/MCP bridge; gateway and ACP conversation-call segments. README passages supply doctrine/design only. Native provider endpoints, actual grant sets, plugin-host internals, complete compression transformations, inbound platform authorization, full scheduling/evaluation loops and update/install routes remain uninspected or external as specified above. Available but uninspected code is not an evidenced absence.

## Shared records

### Components

#### RT-CMP-inference-model
Label: Configured inference model

The source-native identity is the configured provider/model pair used by `AIAgent`, with credentials, base URL and API mode selecting its consumer endpoint. Its representational form is distributed-parametric; weights/storage are provider-owned or in a configured local model service, not stored in the inspected request loop. SRC-1 `hermes_cli/oneshot.py`, `agent/turn_api_call.py`, `agent/conversation_loop.py` wire foreground inference; delegation can select another provider/model pair through `tools/delegate_tool.py`.

Parameters changing during operation: uninspected — these files request inference and do not expose provider training/internal state. Exact model version pinned: not established; model strings/configuration are selections, not frozen numerical checkpoints. Mutable endpoint resolving to another model: possible through endpoint administration, and explicitly through configured fallback/child routing. The provider's resolution of one alias remains uninspected. Foreground, delegated, review and compression calls must not be assumed to use one exact set of weights.

> runtime, fallback_entry = resolve_runtime_with_fallback(
>     cfg,
>     requested=choice.provider,
>     target_model=choice.model or None,
>     explicit_base_url=choice.base_url,
>     explicit_api_key=choice.api_key,
> )
> --- `hermes_cli/oneshot.py`

### Operative objects

#### RT-OBJ-tool-call
Label: Tool-call control envelope

Identity: normalized assistant tool-call entries with names, arguments and call IDs. Representational form: symbolic control envelope consumed by fixed name/dispatch rules; argument bodies such as scripts or task text have their own consumers described in the corresponding routes. Substrate: in-process response/message structures and serialized session rows when enabled. SRC-1 `agent/turn_tool_round.py` and `agent/tool_executor.py` establish staging and execution.

> assistant_msg, duplicate_previous_interim = stage_tool_call_message(
>     agent, assistant_message=assistant_message, finish_reason=finish_reason, messages=messages
> )
> append_message(messages, assistant_msg)
> --- `agent/turn_tool_round.py`

#### RT-OBJ-session-messages
Label: Session message control structure

Identity: the `messages` list and its persisted role/call-ID/metadata structure. Representational form: symbolic envelope defining turn order and tool-result association; natural-language content inside it is interpreted by the model and is not a fixed-rule correctness certificate. Substrate: process list plus SQLite session rows when configured. This record concerns runtime coordination, not a complete retained-content inventory. SRC-1 `agent/session_persistence.py`, `agent/turn_context.py` establish copy, append and persistence-marker handling.

> if getattr(self, "_persist_disabled", False) or not self._session_db:
>     return None
> --- `agent/session_persistence.py`

### Routes

#### RT-RTE-oneshot-turn
Label: One-shot conversation turn

Endpoint/progression: user prompt → shipped `run_oneshot` → `_run_agent` → `AIAgent.run_conversation` → generic loop or Codex branch → result → stdout/exit code. Owner: one-shot caller for admission/cleanup; phase code for budgets and recovery; configured model for next content/tool proposals. Natural-language task/prompt guidance and numerical model interpretation produce symbolic calls. Session/task/turn/API-request identities coordinate effects and logs. No answer oracle is supplied for this open-request mode. Configuration and explicit caller arguments decide provider/toolsets; who authored config is unresolved. Evidence: SRC-1 `hermes_cli/oneshot.py`, `agent/conversation_loop.py`, `agent/turn_context.py`, `agent/turn_api_call.py`.

- Immediate return: final_response and result dict internally; final text, optional usage JSON and success/failure exit code externally.
- Later read-back: optional resume loads session history and stored runtime before the new turn; complete retention semantics are not established here.
- Delegated visibility: selected child input and aggregated results, not automatic transfer of the complete parent context; see [RT-RTE-child-delegation](#rt-rte-child-delegation).
- Selection predicate: explicit options, ambient configuration and optional resume metadata; response tool calls select the next phase.
- Invalidation or expiry: iteration/retry budgets, interrupts and typed failure results terminate a turn; cleanup closes caller resources.
- Activation or effect: wired provider requests, possible tool effects and final output; no exercised behavior observed.
- Evidence limits: actual provider result, grants, isolation and operational cleanup success are unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> os.environ["HERMES_YOLO_MODE"] = "1"
> os.environ["HERMES_ACCEPT_HOOKS"] = "1"
> --- `hermes_cli/oneshot.py`

#### RT-RTE-tool-dispatch
Label: Generic tool-round dispatch

Endpoint/progression: normalized calls → validation/capping/staging → pre-effect flush → sequential/segmented/concurrent executor → scope/plugin/pruned-argument/guardrail policy → live-agent or registry implementation → result commit/flush → next model request. Owner: Hermes code; the model proposes calls, installed hooks can modify/block, and some backend guards request human decisions. Tool policy is symbolic code/config, not model compliance. Effects occur in the selected tool/backend; result delivery is transformed, not necessarily full raw output. Evidence: SRC-1 `agent/turn_tool_round.py`, `agent/tool_executor.py`, `run_agent.py`.

- Immediate return: tool result messages or controlled blocked/error results; reported canonical-append failure ends the turn.
- Later read-back: persisted call/result rows can reach resumed conversations; oversized results may become previews/pointers rather than full content.
- Delegated visibility: dispatch treats delegate/context-engine/memory-provider implementations separately; it does not itself copy the foreground history to every executor.
- Selection predicate: valid tool names, tool-search scope where applicable, parsed arguments, segment plan and guardrail decisions.
- Invalidation or expiry: interrupts, execution deadlines, guardrail halt and persistence failure; no atomic rollback of already committed external effects is established.
- Activation or effect: wired backend dispatch after covered checks; actual invocation/result correctness unobserved.
- Evidence limits: guarantees cover this executor path only; direct Python RPC and Codex native operations differ. No-store/persistence-disabled flush skips the durability fence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if _tool_turn_persisted is False:
>     # Canonical append failed: never project the row or run tools from process-only
>     # state; break rather than retry. No recorded cause means genuinely unknown.
> --- `agent/turn_tool_round.py`

> if state.dispatched:
>     raise RuntimeError("Hermes tool execution callback invoked more than once")
> --- `agent/tool_executor.py`

That callback invariant prevents repeated dispatch through the same middleware callback. It does not establish exactly-once behavior across retries, resumptions, plugins' independent effects or external systems.

#### RT-RTE-command-approval
Label: Terminal command approval policy

Endpoint/progression: terminal command guard → backend fast-path or floors → bypass/cache/allowlist → unattended policy or human/smart decision → approved/blocked verdict. Owner: `tools.approval`; caller provides presence and human transport. Model proposes command; code detects patterns and interprets config; humans can grant once/session/permanent or deny when a prompt is reached. Smart decisions are not correctness oracles. Operating modes include attended decisions, bypass and unattended configured policies. Trigger/proposed change: a command may mutate reachable files/processes. Admission is command policy, not per-file product-quality review. Recovery is tool-specific, not a universal rollback. SRC-1 `tools/approval.py`; one-shot bypass in `hermes_cli/oneshot.py`; gateway callback in `gateway/run_turn_runner.py`.

- Immediate return: approved/blocked decision supplied to the tool.
- Later read-back: session and permanent approvals can affect later matching decisions; once grants do not persist.
- Delegated visibility: child workers install separate non-interactive approval callbacks; shared human presence must not be assumed.
- Selection predicate: environment/backend host access, detected floors/patterns, deny rules, approval mode, presence and cached choices.
- Invalidation or expiry: once/session/permanent scopes differ; revocation and session cleanup are caller/policy responsibilities, not observed here.
- Activation or effect: wired authorization of a covered command; backend isolation and actual command effects unobserved.
- Evidence limits: recoverable approval can be bypassed; container fast paths retain deny checks but skip other floors/pattern prompts. This is not an OS security boundary.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if _should_skip_container_guards(env_type, has_host_access=has_host_access):
>     return _user_deny_block(command) or _approved()
> --- `tools/approval.py:1128-1180`

#### RT-RTE-code-execution
Label: Persistent Python execution and tool RPC

Endpoint/progression: model script proposal → terminal-policy/lifecycle/whole-script guard → local persistent kernel or remote backend → optional allowed RPC calls → JSON result. Owner: code tool and kernel/RPC server; script determines internal actions. Python is symbolic executable content; RPC tool arguments can carry model-interpreted text. Admission can allow the script without a human in local CLI/bypass/approved unattended modes, or require a gateway/ask decision. Proposal guidance is the tool schema and supplied task. The change is arbitrary reachable file/process work; no independent answer oracle or product successor evaluator is established. Reset retires a kernel, not necessarily its file effects. SRC-1 `tools/code_execution_tool.py`, `tools/approval.py`, `tools/code_execution_rpc.py`, `tools/code_kernel.py`.

- Immediate return: JSON execution result, bounded output and RPC error accounting rather than every internal intermediate value.
- Later read-back: local kernel state can survive later cells; file effects can survive independently; full retained-memory treatment is outside this route account.
- Delegated visibility: execution is a separate process/backend; allowed RPC results reach script state and selected output returns to the foreground model.
- Selection predicate: backend, configured execution mode, script guard, RPC allowlist/call budget and active cell authority.
- Invalidation or expiry: reset, timeout/interrupt, cell authority retirement and session kernel cleanup; persistent external effects have no general rollback.
- Activation or effect: wired execution and permitted RPC; direct subprocess/file operations are possible outside terminal command-string checks.
- Evidence limits: execution backend internals and deployed permissions are not established; tool allowlisting is not confinement of arbitrary Python.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> """Run Python in the session's persistent kernel (local) or on the remote terminal backend,
> with RPC access to a subset of Hermes tools; returns the JSON result string. "Sandbox" means
> the security envelope (env scrubbing, tool whitelist + call budget, output redaction), not an
> isolation jail: default `project` mode runs in the session's cwd with the project venv.
> --- `tools/code_execution_tool.py`

> if tool_name not in allowed_tools:
>     return tool_error(f"Tool '{tool_name}' is not available in execute_code. "
>                       f"Available: {', '.join(sorted(allowed_tools))}")
> --- `tools/code_execution_rpc.py`

RPC dispatch reaches `model_tools.handle_function_call`, not the foreground `run_tool_round` for every inner operation. That changes the scope of the per-round transcript fence without proving absence of all inner-tool checks.

#### RT-RTE-child-delegation
Label: Child delegation with finite-session fallback

Endpoint/progression: foreground delegate proposal → pause/depth/task/budget checks → child construction → synchronous or async unit admission → child conversation → result aggregation. Owner: delegation code for role/depth/routing and scheduling; child model for local task decisions. Child identity includes subagent ID, separate session, parent session linkage and task identity. Child prompt carries goal/context; construction skips context files and memory and grants resolved child toolsets, with a fresh iteration budget. The model cannot override the authoritative configured iteration cap. Optional schema checking provides a structural output reference and at most one correction turn, not an expected factual answer. Open-request mode; human config, computational routing and schema checks contribute distinct controls. SRC-1 `tools/delegate_tool.py`, `tools/delegate_tool_dispatch.py`, `tools/delegate_tool_child_run.py`, `run_agent.py`.

- Immediate return: synchronous aggregate in finite one-shot/nested modes; background-capable admission returns unit handles, possibly with inline results.
- Later read-back: detached API completion can target server history for the next client turn without waking a model; complete durable-delivery implementation is uninspected here.
- Delegated visibility: selected goal/context, optional images/prefill and child prompt; parent receives result entries rather than the full child working context by default.
- Selection predicate: spawn pause, depth-derived role, task normalization, authoritative budgets, delivery support and async pool capacity.
- Invalidation or expiry: parent stop propagation for attached children, list/steer/stop control, inactivity handling and child cleanup; detached units deliberately change cancellation ownership.
- Activation or effect: wired child model/tool work and aggregation; no benefit or successful delivery observed.
- Evidence limits: filesystem isolation/worktree seeding and complete durable completion consumer are not traced; separate model contexts do not prove effect isolation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> skip_context_files=True, skip_memory=True, clarify_callback=None,
> --- `tools/delegate_tool.py`

> if get_session_env("HERMES_SINGLE_QUERY_SESSION") == "1":
>     return None
> --- `tools/delegate_tool_dispatch.py`

> if wake_sid is None:
>     logger.info("delegate_task: async delivery unsupported on this session runtime; running the batch synchronously instead.")
>     return _run_sync_with_note(batch, "no_async")
> --- `tools/delegate_tool_dispatch.py`

#### RT-RTE-codex-turn
Label: Codex app-server alternate turn

Endpoint/progression: `api_mode` branch → lazy subprocess session/thread start or resume → turn protocol/native tool events and approval requests → event projection → Hermes result/persistence. Owner: Hermes integration for prompt/routing/callback/projection; external Codex runtime for internal next-step policy and native execution. Prompt composition becomes developer instructions; a fresh thread may receive prior-history seed. Thread ID is separate from Hermes session identity. Native commands/file changes do not dispatch through the generic foreground executor. Permission escalations are declined; exec/patch requests can auto-approve on explicit bypass or ask a callback, otherwise decline. No answer oracle. Open requests can mutate files through native tools; admission depends on external sandbox policy and callbacks, not generic toolset selection. SRC-1 `agent/conversation_loop.py`, `agent/codex_runtime.py`, `agent/transports/codex_app_server_session.py`, `agent/transports/hermes_tools_mcp_server.py`.

- Immediate return: final text, usage/error/interrupt state and projected messages in a Hermes result; some failures can activate generic-loop fallback.
- Later read-back: stored thread binding permits resume; projected messages are flushed after the turn. Failed projection persistence can leave delivered content missing on restart.
- Delegated visibility: Codex receives developer instructions/history seed and its native context; a fixed Hermes MCP subset supplies selected extra tools, not the running agent's entire stateful surface.
- Selection predicate: opt-in API mode, provider/model, thread binding/prompt composition and explicit approval bypass.
- Invalidation or expiry: prompt/provider changes can retire the session; interrupt/close and failed-resume handling apply; native compaction is externally owned.
- Activation or effect: wired external runtime protocol and result bridge; actual Codex actions and isolation unobserved.
- Evidence limits: subprocess/provider internals are external; generic persist-before-execute and per-call tool guardrails do not cover its native operations.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if agent.api_mode == "codex_app_server" and (codex_result := _codex_app_server_turn(agent, s)) is not None:
>     return codex_result
> --- `agent/conversation_loop.py`

> if auto_approve:
>     return "accept"
> if self._approval_callback is None:
>     return "decline"
> --- `agent/transports/codex_app_server_session.py`

The MCP bridge's explicit `EXPOSED_TOOLS` omits terminal/file/process and stateful delegate/memory/session-search/todo tools, despite broader server instruction prose. Its handlers call `model_tools.handle_function_call` in the bridge process. Delivery labels alone must not expand this inspected subset.

#### RT-RTE-plugin-admission
Label: Executable plugin capability admission

Endpoint/progression: discovered manifest → config/category/source gating → version compatibility check → directory/entry-point import or plugin-host load → `register(ctx)` → scoped tool/hook/provider registration. Owner: plugin manager and registry; selected plugin supplies executable content. Trigger: discovery or reload after installed/configured capabilities change. Proposed change: new/replaced execution handlers and prompt/context providers. Configuration can veto loading or built-in override; software validates/gates, and plugin code performs registration. Human content approval is unresolved; enabling is not evidence that a human reviewed each handler. Open capability installation, not an inspected improvement experiment; no answer oracle. Failed loading disposes owned registrations/subscriptions; override leases preserve previous entries. This rollback concerns managed registration, not all arbitrary import-time effects. SRC-1 `hermes_cli/plugins_discovery.py`, `hermes_cli/plugins_loader.py`, `hermes_cli/plugins.py`.

- Immediate return: enabled/error plugin state and registered runtime capabilities, not necessarily a user-facing answer.
- Later read-back: installed code/config is rediscovered later; runtime registrations persist for the manager/load lifetime.
- Delegated visibility: host mode routes non-bundled Python plugins into a profile-owned plugin process; its full RPC/security envelope is uninspected.
- Selection predicate: explicit disable, kind-specific ownership, bundled defaults, enabled set, catalog removal checks, version compatibility and override grants.
- Invalidation or expiry: unload/failure registration disposal and replacement leases; timed-out loaders have late managed registrations refused.
- Activation or effect: wired import/registration and later callable execution; installed code and actual grants not frozen.
- Evidence limits: process separation is not established OS confinement; arbitrary plugin effects, update/install acquisition and host internals remain uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if enabled is None or not names & enabled:
>     return _placeholder(
>         f"not enabled in config (run `hermes plugins enable {lookup_key}` to activate)", logging.DEBUG,
>         "Skipping '%s' (not in plugins.enabled)",
>     )
> --- `hermes_cli/plugins_discovery.py`

> if override and not self._tool_override_allowed(name):
>     raise PluginToolOverrideError(
> --- `hermes_cli/plugins.py`

> return manifest.source != "bundled" and isolation_mode() == ISOLATION_HOST
> --- `hermes_cli/plugins_loader.py`

#### RT-RTE-review-handoff
Label: Post-turn retained-content review handoff

Endpoint/progression: turn counters/tool availability → completed-turn snapshot → `_spawn_background_review`. Owner: finalizer for selection; review implementation/model for any downstream proposal, selection or writes. Trigger: memory or skill interval predicate with final response and no interrupt; generic path also respects `skip_background_review`. Proposed change is memory/skill retention, but this record establishes the handoff only. Exact downstream admission, veto, rollback, guidance and retained result require memory analysis and are uninspected here. No answer oracle established; open heuristic review, not a bounded causal evaluation. SRC-1 `agent/turn_finalizer.py`, `agent/turn_context.py`, `agent/codex_runtime.py`.

- Immediate return: best-effort scheduling; foreground response remains the turn result.
- Later read-back: uninspected — specialist must trace actual writes and subsequent consumers rather than infer them from the hook name.
- Delegated visibility: conversation snapshot and memory/skill review flags cross the handoff; downstream transformation and isolation are not established here.
- Selection predicate: review counters/intervals, skill tool availability, final response, interrupt state and generic skip flag.
- Invalidation or expiry: spawn exceptions are suppressed; review lifecycle and store rollback are uninspected.
- Activation or effect: wired review request, not evidence of a retained update or changed later behavior.
- Evidence limits: trigger/request only; the Codex finalizer has its own predicate, so generic skip behavior must not be generalized to that branch.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> agent._spawn_background_review(
>     messages_snapshot=list(messages), review_memory=_should_review_memory,
>     review_skills=_should_review_skills,
> )
> --- `agent/turn_finalizer.py`

### Claims

#### RT-CLM-product-work
Label: Product's learning and delegated-work claims

Claimed operation: experience-derived skill creation/improvement, knowledge persistence and cross-session user modeling; delegated isolated work and Python tool RPC. Source: SRC-1 `README.md`, doctrine/design. Isolation is qualified by the runtime cases above; learning/self-improvement requires separate pathway evidence, not the product label.

> It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions.
> --- `README.md`

> <tr><td><b>Delegates and parallelizes</b></td><td>Spawn isolated subagents for parallel workstreams. Write Python scripts that call tools via RPC, collapsing multi-step pipelines into zero-context-cost turns.</td></tr>
> --- `README.md`

- doctrine conclusion status: claimed
- operation conclusion status: uninspected

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-task-prompt
Label: Task and instruction model-input authority

Consumer: configured foreground/child inference model. Channel: user/system/developer messages assembled from caller input, restored prompts and selected context. Force: natural-language guidance interpreted by the model, with symbolic runtime rules controlling calls and budgets; delivery is not guaranteed compliance. Horizon: current request/turn, potentially later turns when session/context is reused. Evidence: SRC-1 `agent/turn_context.py`, `agent/conversation_loop.py`, `tools/delegate_tool.py`, `agent/codex_runtime.py`; [RT-RTE-oneshot-turn](#rt-rte-oneshot-turn) and [RT-RTE-codex-turn](#rt-rte-codex-turn) identify distinct channels.

> active_system_prompt = agent._cached_system_prompt
> --- `agent/turn_context.py`

#### RT-BAP-plugin-handler
Label: Plugin handler executable authority

Consumer: scoped registry/executor or hook dispatcher. Channel: registered Python callable/schema/provider implementations. Force: executable control/effects rather than advisory model text; prompt-section registrations have a separate model-input consumption path. Horizon: manager/load lifetime and later discoveries from installed code/config. Evidence: SRC-1 `hermes_cli/plugins.py`, `hermes_cli/plugins_loader.py`; [RT-RTE-plugin-admission](#rt-rte-plugin-admission) bounds configuration and override admission. Registration rollback does not imply rollback of arbitrary plugin I/O.

> register_fn(ctx)
> return True
> --- `hermes_cli/plugins_loader.py`

## Annotations

none
