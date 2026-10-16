---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Halo runtime baseline: shipped trace diagnosis, delegation, bounded execution, desktop follow-ups and improvement handoff at b7f8509745d67b499b4e80efe20ea37c03426a74."
run-id: AAS-2026-10-14-halo-c4ed89d7f99f-01
reviewed-boundary: b7f8509745d67b499b4e80efe20ea37c03426a74
---

# Halo runtime report

## Runtime account

### Work and evidence basis

Halo answers questions about captured harness executions and hands findings to a separate coding actor. The frozen boundary includes the desktop caller, not just the engine. It ends before the receiving coding agent edits and deploys an arbitrary harness. The boundary's partial-loop classification remains necessary: source wiring establishes diagnostic and handoff capacity, not autonomous production improvement (SRC-1, `engine/main.py`, `app/src/desktop/commands.ts`, `skills/claude/SKILL.md`).

All findings below use SRC-1 at the boundary's pin. Added implementation coverage includes `engine/engine_config.py`, `engine/agents/{agent_config,openai_agent_runner}.py`, `engine/tools/{synthesis_tool,run_code_tool}.py`, `engine/traces/trace_store.py`, `engine/sandbox/sandbox.py`, `engine/code/{code_repo,_paths}.py`, and `engine/git/git_repo.py`, with bounded reads of the consequential methods. Additional desktop coverage includes install/update, bridge result selection, queue cancellation/persistence, history filtering and report rendering. Runtime prompts and the skill's diagnosis/edit/remeasurement procedure supply doctrine/design. No target code or tests were executed. No source-native execution artifact was inspected for this report. Exercise, reliable compliance, provider behavior and benefit remain unobserved; this does not negate implementation capacity.

### Ordinary invocation

The packaged CLI constructs an `EngineConfig` from the user's trace path, question, model/provider settings and resource limits, then calls `stream_engine_async`. The public synchronous, asynchronous, collected-output and output-only APIs converge on the same implementation. Output-only wrappers discard text deltas; they do not create a separate decision loop (SRC-1, `halo_cli/main.py`, `engine/main.py`).

The root lifecycle is [RT-RTE-trace-diagnosis](#rt-rte-trace-diagnosis). The caller supplies the question and grant configuration. Code resolves a per-run OpenAI-compatible client, sandbox availability, sidecar indexes and a union trace store. Optional repository resolution happens before the first analysis model call. A root execution receives a UUID-derived identity, depth zero and no parent. The root context combines engine guidance with caller messages and optional dataset/repository guidance. The SDK model chooses the next tool or answer; code implements the tool, maps events into local context and emits interleaved sequence-numbered events. Runtime execution identities are distinct from the telemetry grouping identity `halo`, which intentionally groups root and children (SRC-1, `engine/main.py`, `engine/tools/subagent_tool_factory.py`).

The root is advised to delegate, but has the leaf tools itself. [RT-RTE-subagent-call](#rt-rte-subagent-call) constructs a fresh child context from a child system prompt and the parent's delegated text, not a copy of the parent transcript. The child shares trace/repository access and the provider client. Each execution has its own context and retry accounting; the shared output bus exposes child activity to the host, while the parent receives a JSON answer, child identity, sequence interval and usage counters. Nested delegation uses the same construction until the depth cap. This resembles a separate work frame: selected inputs enter and an answer escapes. It is not a heap of model-followable references; the parent's answer does not automatically recover the child's original conversation (SRC-1, `engine/tools/subagent_tool_factory.py`).

Root termination is mediated by `final_answer` and SDK `StopAtTools`; children instead return their last non-tool assistant text. Recovery retries transient stream errors from locally reconstructed Responses-API input. It trims incomplete trailing tool turns, retains completed work and cannot retract bus events. Root max-turn exhaustion or a plain-message ending may trigger a separate final-answer reprompt. Thus the cap is per SDK invocation, not a whole-run spend cap, and retries do not promise exactly-once effects (SRC-1, `engine/agents/openai_agent_runner.py`, `engine/tools/subagent_tool_factory.py`).

### Material alternate and forcing routes

Four inspected cases qualify seemingly stronger descriptions:

1. **Depth zero or direct root exploration.** Root leaf tools remain registered even when prompts advise delegation. Depth enforcement limits child creation, not root investigation. Per-depth semaphores limit active children at each depth, not all agents together (SRC-1, `engine/tools/subagent_tool_factory.py`; [RT-RTE-subagent-call](#rt-rte-subagent-call)).
2. **Synthesis is a direct model call.** It bypasses the SDK agent turn loop and receives rendered trace metadata rather than all raw attributes. `render_trace` calls `view_trace`; an oversized trace produces no spans, so synthesis can receive `spans: 0` without the oversized summary's explanation. Its budget uses Python string length despite a bytes-oriented docstring. This prevents treating a synthesis result as a complete account of the selected traces (SRC-1, `engine/tools/synthesis_tool.py`, `engine/traces/trace_store.py`; [RT-RTE-trace-synthesis](#rt-rte-trace-synthesis)).
3. **Checkpoint configuration changes compaction reachability.** Despite general compaction documentation, the inspected runner compacts only at successful root completion when checkpoints are enabled. Ordinary CLI and desktop configurations leave them disabled. This is not ongoing mid-analysis context control. The emitted checkpoint affords a host resume path, but this desktop bridge does not handle checkpoint events or request them (SRC-1, `engine/agents/openai_agent_runner.py`, `app/scripts/halo-local-runner.py`; [RT-RTE-checkpoint-emission](#rt-rte-checkpoint-emission)).
4. **Desktop completion differs from engine finalization.** The bridge falls back to the last assistant item if no final-flagged answer exists. It does not restrict that fallback to root items. Any non-empty selected answer produces a desktop `completed` event. A stored completed run therefore does not prove successful root `final_answer`, much less diagnostic correctness (SRC-1, `app/scripts/halo-local-runner.py`; [RT-RTE-desktop-analysis](#rt-rte-desktop-analysis)).

Other material effect routes are sandbox Python, optional code/Git inspection, external coding handoff and host engine installation. They have different enforcement owners. The factory builds local function tools; the inspected registration list does not add provider-native tools or a general shell tool. This is a bounded registration observation, not a claim about provider internals, arbitrary callers, extensions or a deployed isolation envelope (SRC-1, `engine/tools/subagent_tool_factory.py`).

### Controls and guarantee coverage

| Guarantee and owner | Enforcement, strength and covered path | Counterpaths, external contract and conclusion limits |
| --- | --- | --- |
| Child depth/concurrency, engine factory | Structural omission plus runtime depth check; per-depth `asyncio.Semaphore`; invariant on the shipped child route | Root is ungated; separate depth pools and separate runs are not a global cap. Depends on SDK dispatch reaching the wrapper. Implementation conclusion status: wired. Operation conclusion status: uninspected. |
| Turn cap, SDK caller | `max_turns` on root/child SDK invocations; protocol relying on SDK enforcement | Retries and root salvage start another invocation. Synthesis/compaction use direct calls. No whole-run token/cost bound is established. Implementation conclusion status: wired. Operation conclusion status: uninspected. |
| Sandbox host restrictions, sandbox launcher | Enumerated Deno read grants and `--no-prompt`, timeout and process shutdown; protocol | Covers model-supplied `run_code`, not Python host setup, provider calls, Git subprocesses, imports, report writes or engine installation. Depends on Deno/Pyodide enforcing restrictions; deployed security is uninspected. Implementation conclusion status: wired. Operation conclusion status: uninspected. |
| Read-only repository inspection, code/Git views | Resolved-path confinement, file reads, fixed Git subcommands, guarded refs and cleaned redirect environment; protocol | Not OS isolation of the engine. Git user config remains intact; external Git behavior is not frozen. The host installer deliberately pulls code. Implementation conclusion status: wired. Operation conclusion status: uninspected. |
| Reliable final output, root runner/desktop bridge | Root termination tool and bounded reprompt; best effort | Child failures return ordinary JSON failure answers; desktop accepts last-assistant fallback; model truth is unchecked. Implementation conclusion status: wired. Operation conclusion status: uninspected. |
| Evidence-first exploration, prompts | Model-readable guidance; policy | Root can directly use leaf tools; tool registration does not enforce the requested first tool or prior-ID discovery order. Provider compliance is unobserved. Implementation conclusion status: wired. Operation conclusion status: uninspected. |

Evidence for this table is retained in the linked route records and their quotations. Capability surface and current grants differ: sandbox tools depend on availability; code tools on a configured repository; Git tools additionally on a Git worktree and executable. The desktop bridge supplies neither repository access nor checkpoints. The engine's Python host still has ordinary host I/O privileges. No source inspection establishes the user's deployed containment, credentials or approval arrangements (SRC-1, `engine/main.py`, `engine/tools/subagent_tool_factory.py`, `app/scripts/halo-local-runner.py`).

### Durable caller and change admission

The desktop queue exports filtered telemetry, rejects an empty export and writes a runner config. Bun launches a Python bridge in the installed engine directory, streams JSON-line events, updates run/turn state and materializes a report. Follow-ups reuse the export if it exists and rebuild messages from retained earlier user/assistant turns; tool transcripts and child execution contexts are not included by that history builder. Cancellation kills the bridge process; queue failure states and user retry/follow-up provide host-level recovery. These mechanisms are [RT-RTE-desktop-analysis](#rt-rte-desktop-analysis), not engine-owned durable sessions (SRC-1, `app/src/server/halo/runQueue.ts`, `app/src/server/halo/storage.ts`, `app/src/server/halo/report.ts`). The memory analyst owns detailed retained-object and revision findings.

The report enters an external coding tool by path-bearing deep link, not an automatic patch executor. [RT-RTE-report-handoff](#rt-rte-report-handoff) separates initiation/confirmation from subsequent content approval. The shipped skill prescribes baseline, claim verification, minimal edit and remeasurement; newer repository tools contradict its blanket trace-only description. The mismatch must not erase either route. [RT-RTE-engine-install](#rt-rte-engine-install) separately admits changes to Halo's own installed production machinery through host Git/uv commands. It is not trace-responsive self-revision (SRC-1, `skills/claude/SKILL.md`, `engine/tools/subagent_tool_factory.py`, `app/src/server/halo/engine.ts`).

## Shared records

### Components

#### RT-CMP-root-agent
Label: Root agent model binding

Source-native identity: `EngineConfig.root_agent.model`. Distributed-parametric computation through a configured remote model service; weights and provider substrate are outside the checkout. Local symbolic `ModelConfig` names/settings are in memory. Inspected code issues inference, not parameter updates. Exact model version is not required to be immutable; a configured name at a mutable provider endpoint may resolve differently. Provider internal adaptation is uninspected. Evidence: SRC-1, `engine/main.py`, `engine/engine_config.py`.

> model=engine_config.root_agent.model.name,
> model_settings=engine_config.root_agent.model.to_sdk_model_settings(),
> --- `engine/tools/subagent_tool_factory.py`

#### RT-CMP-subagent
Label: Subagent model binding

Source-native identity: `EngineConfig.subagent.model`. Distributed-parametric model computation on the provider substrate, with a distinct configurable local name/settings binding. No parameter update is implemented in the inspected child execution route; provider internals remain uninspected. An exact immutable model revision is not required; the mutable endpoint/name can resolve to another model. The CLI chooses the root model name for children but the library config permits a separate binding. Evidence: SRC-1, `halo_cli/main.py`, `engine/engine_config.py`.

> model=engine_config.subagent.model.name,
> model_settings=engine_config.subagent.model.to_sdk_model_settings(),
> tools=[],
> --- `engine/tools/subagent_tool_factory.py`

#### RT-CMP-synthesis-model
Label: Synthesis model binding

Source-native identity: `EngineConfig.synthesis_model`. Distributed-parametric computation remotely served; local configuration is symbolic, returned summary is natural language. No parameter update is implemented by this inference call. Exact version is caller-dependent rather than necessarily pinned; endpoint/name resolution can change. Provider storage and adaptation are uninspected. Evidence: SRC-1, `engine/tools/synthesis_tool.py`, `engine/engine_config.py`.

> lambda: self._client.chat.completions.create(
>     model=self._model.name,
> --- `engine/tools/synthesis_tool.py`

#### RT-CMP-compaction-model
Label: Compaction model binding

Source-native identity: `EngineConfig.compaction_model`. Distributed-parametric inference remotely served, controlled by a local symbolic binding; summaries are natural language. Inspected calls do not update weights. No immutable exact version requirement is imposed; a mutable provider endpoint can resolve another model. Provider internals are uninspected. Evidence: SRC-1, `engine/agents/compactor.py`, `engine/engine_config.py`.

> lambda: client.chat.completions.create(
>     model=compaction_model.name,
> --- `engine/agents/compactor.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-trace-diagnosis
Label: Model-directed trace diagnosis

Caller question/configuration and JSONL files → index/store resolution → root SDK agent → local function tools and event bus → final answer or failure. Code owns lifecycle and dispatch; the root model owns investigation/answer choices under natural-language prompts. Local symbolic indexes, execution identities and context items support the loop. Caller model/provider settings, turn/depth limits, optional repository and dataset description govern the grant/context. Diagnosis mode is an open question, not a bounded curriculum. The model proposes interpretations and decides its answer; the caller can cancel or reject it. No independent expected-answer oracle is supplied by this route; telemetry status/error markers are evidence, not a correctness oracle. It persists sidecar indexes and optional telemetry, while ordinary local context ends with the run (SRC-1, `engine/main.py`, `engine/agents/openai_agent_runner.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Streamed text deltas and sequenced root/child output items; collecting wrappers return durable items only.
- Later read-back: Completed local context is reconstructed for retries/reprompts; durable later-session consumption is supplied by the desktop route, not these wrappers.
- Delegated visibility: Children get a delegated question and their own prompt, not the whole root context; host sees interleaved child events.
- Selection predicate: Model tool choices; index-backed query/filter selection; prompts request overview first and source IDs already discovered.
- Invalidation or expiry: Context lifetime is the execution; failed partial tool tails are removed before retry, but emitted events remain visible.
- Activation or effect: Dispatch reads trace data and returns evidence to the model; final-answer call stops the root SDK run. Behavioral reliance and answer quality are unobserved.
- Evidence limits: SDK/provider implementations and actual executions are not supplied; source wiring does not establish successful diagnosis or global cost bounds.

> return Runner.run_streamed(
>     starting_agent=agent,
>     input=input,
>     context=context,
>     max_turns=engine_config.root_agent.maximum_turns,
>     run_config=run_config,
> )
> --- `engine/main.py`

The load-bearing terminal mechanism is SDK `StopAtTools` (protocol); recovery is best effort. Incomplete-tool trimming is not an exactly-once transaction:

> Output items already emitted to the bus cannot be retracted — consumers
> may see a trimmed turn followed by its regenerated equivalent, which is
> the accepted tradeoff versus failing a long run outright. Each retry
> sleeps with full-jitter exponential backoff.
> --- `engine/agents/openai_agent_runner.py`

#### RT-RTE-subagent-call
Label: Fresh-context bounded delegation

Parent `call_subagent` arguments → guarded wrapper → depth semaphore → child context/SDK agent → JSON result. Parent model proposes the focused question; code decides admission through depth and schema checks, not human per-call approval. Child model chooses its own tools/answer. Open delegated diagnostic mode; no expected-answer oracle. Shared store/client/tools permit trace/code investigation without copying the parent's accumulated conversation. Child execution IDs retain parent agent/tool-call lineage; semaphores coordinate active work separately at each depth. Model components: [RT-CMP-subagent](#rt-cmp-subagent) and [RT-CMP-root-agent](#rt-cmp-root-agent). Evidence: SRC-1, `engine/tools/subagent_tool_factory.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON `SubagentToolResult` containing last assistant answer or recoverable failure text, sequence bounds, child ID and counters.
- Later read-back: Result is retained in parent current-run history and can enter retry input; a subsequent persistent child session is not created here.
- Delegated visibility: Only child system prompt/delegated text enters its initial context; shared trace/repository grants remain available at every eligible depth.
- Selection predicate: Parent model selects the question; factory omits child spawning at maximum depth and wrapper repeats the depth check.
- Invalidation or expiry: Fresh context per invocation; child execution ends on return/failure and releases its depth slot.
- Activation or effect: Runs another model/tool loop and returns its answer. Parent reliance is not observed.
- Evidence limits: Depth/concurrency enforcement is visible, but SDK dispatch and exercised isolation are not observed; the cap is per depth, not globally across all work.

> if depth >= engine_config.maximum_depth:
>     return leaf_tools
> --- `engine/tools/subagent_tool_factory.py`

> items=[
>     AgentContextItem(
>         item_id="sys-0", role="system", content=subagent_system_prompt
>     ),
>     AgentContextItem(item_id="in-0", role="user", content=delegated_input),
> ],
> --- `engine/tools/subagent_tool_factory.py`

#### RT-RTE-trace-synthesis
Label: Direct trace synthesis call

Agent-selected trace IDs/focus → `render_trace` → direct Chat Completions request → summary tool result. Agent proposes the selection; tool code constructs the reduced input; [RT-CMP-synthesis-model](#rt-cmp-synthesis-model) decides summary content without a human admission gate. Open diagnostic mode, no answer oracle. It is not another SDK agent and carries no SDK delegation depth or turn budget of its own. Evidence: SRC-1, `engine/tools/synthesis_tool.py`, `engine/traces/trace_store.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Stripped model reply in `SynthesizeTracesResult.summary`.
- Later read-back: Tool result can enter the calling agent's later requests/retries; durable cross-session treatment belongs to the memory report.
- Delegated visibility: Summary model receives synthesis instructions, IDs, optional focus and bounded rendered trace metadata, not the calling agent's transcript or raw payloads.
- Selection predicate: Calling model supplies trace IDs; rendering obtains the bounded `view_trace` result and includes selected metadata fields.
- Invalidation or expiry: Fresh request per tool call; no summary cache/writeback is implemented in this tool.
- Activation or effect: Sends a separate provider inference request and delivers summary text; reliance is unobserved.
- Evidence limits: Truncation and oversized-span omission prevent completeness claims; summary truth and benefit are unobserved.

> rendered = store.render_trace(tid, budget=8_000)
> user_text_parts.append(rendered)
> --- `engine/tools/synthesis_tool.py`

> return TraceView(trace_id=trace_id, spans=[], oversized=summary)
> --- `engine/traces/trace_store.py:344-344`

> view = self.view_trace(trace_id)
> lines: list[str] = [f"trace_id: {trace_id}", f"spans: {len(view.spans)}"]
> for s in view.spans:
> --- `engine/traces/trace_store.py`

#### RT-RTE-sandbox-python
Label: Model-supplied sandbox Python

Agent code argument → `RunCodeTool` → resolved sandbox → fresh Deno/Pyodide process with mounted trace/index files → typed execution result. Agent chooses Python text; launcher code decides current grants and timeout. Symbolic executable code consumes symbolic trace data. Host trace/index paths are enumerated read grants; temporary virtual filesystem state is distinct from host persistence. The sandbox availability check controls whether the capability is registered. Evidence: SRC-1, `engine/tools/run_code_tool.py`, `engine/sandbox/sandbox.py`, `engine/tools/subagent_tool_factory.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `CodeExecutionResult` with output/error/exit/timeout fields, including failures the model can reason about.
- Later read-back: Result enters the caller's context; this route does not preserve a sandbox process between invocations.
- Delegated visibility: Executing code receives the mounted dataset and preloaded trace-store/numerical-analysis environment, not the parent's conversation.
- Selection predicate: Calling model supplies code; tool supplies all active store sources to the sandbox.
- Invalidation or expiry: Session shuts down after the call; timeout or cancellation invokes hard process stop.
- Activation or effect: Executes Python in the WASM runtime; host permission restrictions depend on Deno enforcement.
- Evidence limits: No escape test or deployed isolation evidence; Python-side setup and other host routes are outside this permission envelope.

> return [
>     str(self.deno_executable),
>     "run",
>     "--no-prompt",
>     f"--allow-read={allow_read}",
>     str(self.runner_path),
> ]
> --- `engine/sandbox/sandbox.py`

#### RT-RTE-repository-inspection
Label: Optional code and Git inspection

Configured `repo_path` → startup resolution → conditional leaf registration → model-selected search/read/history arguments → host file/ripgrep/Git operations → bounded tool results. Model chooses inspection targets; code owns path/ref confinement and fixed command construction. Capability admission is caller configuration, not per-content human approval. Repository text is interpreted natural language or executable source supplied as evidence; path/ref/query fields are symbolic. Current grant is omitted without the corresponding resolved view. Evidence: SRC-1, `engine/main.py`, `engine/tools/subagent_tool_factory.py`, `engine/code/code_repo.py`, `engine/code/_paths.py`, `engine/git/git_repo.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: File windows, discovery matches or Git history/blame/diff results; bad paths/refs surface errors.
- Later read-back: Results enter agent history; this route does not write a new checkout or repository knowledge base.
- Delegated visibility: Root and children inherit the same registered views, but only their chosen results enter their individual contexts.
- Selection predicate: Config enables views; model selects query/path/ref/window. Code resolves symlinks before containment; Git rejects leading-option refs and restricts subcommands.
- Invalidation or expiry: Views last for the engine run; caller checkout and Git refs are not frozen by this route.
- Activation or effect: Reads host repository evidence. No mutating command is offered by the inspected tool factory; downstream fix execution is a different route.
- Evidence limits: Read-only tool APIs are not whole-host confinement. Git user configuration remains intact; external executable behavior and arbitrary caller code are uninspected.

> resolved = candidate.resolve()
> if resolved != root and root not in resolved.parents:
> --- `engine/code/_paths.py`

> assert tail and tail[0] in _ALLOWED_SUBCOMMANDS, f"refusing non-read-only git: {tail[:1]}"
> argv = [self._git_executable, "-C", str(self._root), "--no-pager", *tail]
> --- `engine/git/git_repo.py`

#### RT-RTE-checkpoint-emission
Label: Optional terminal compaction and checkpoint

Successful root ending with `emit_run_checkpoints` enabled → age-based context selection → direct summarizer calls → atomic per-unit summary replacement → `RunCheckpoint` event. Code triggers/selects; [RT-CMP-compaction-model](#rt-cmp-compaction-model) authors summaries; code admits successful complete units without human content review. Proposed change is compressed replay context, not model parameters or source machinery. System messages remain; text/tool retention thresholds preserve recent units. Failed units remain original. Guidance asks the model to preserve tool names, argument shapes and key facts; original local items retain fields. Evidence: SRC-1, `engine/agents/openai_agent_runner.py`, `engine/agents/agent_context.py`, `engine/agents/compactor.py`, `engine/engine_config.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Sequenced `RunCheckpoint` carrying rendered messages and execution counters, in addition to ordinary output events.
- Later read-back: Afforded to an external host that persists and re-supplies messages; this desktop bridge neither enables nor consumes checkpoints.
- Delegated visibility: Compactor receives each selected item's rendered text, not the whole transcript; no child checkpoint is emitted by this runner branch.
- Selection predicate: Successful root plus checkpoint flag; independent keep-last thresholds on non-system text and grouped tool turns.
- Invalidation or expiry: Local originals remain reachable in context items; ordinary exceptions leave a failed unit unchanged; persistence/expiry after host receipt is host-dependent.
- Activation or effect: Summary rendering changes emitted replay material. No inspected live resume invocation establishes later behavioral activation.
- Evidence limits: This is terminal checkpoint preparation, not mid-run compaction; host persistence/resume and semantic preservation are unobserved.

> if is_root and self._emit_run_checkpoints:
>     # Compact first, so the checkpoint carries the smaller history
>     # a resumed run would actually replay.
>     await agent_context.compact_old_items(self._client)
> --- `engine/agents/openai_agent_runner.py`

> self.items[idx] = item.model_copy(
>     update={"is_compacted": True, "compaction_summary": summary}
> )
> self._index[item.item_id] = self.items[idx]
> --- `engine/agents/agent_context.py`

#### RT-RTE-desktop-analysis
Label: Desktop queued analysis and follow-up

User-created run/follow-up → Bun queue → selected telemetry export/config file → Python bridge → engine stream → SQLite run/turn/event state plus result/report files. Host owns scheduling, cancellation, export selection and persistence. Engine models choose diagnosis; bridge code selects the persisted answer. Human starts/questions the analysis but does not approve each model-authored answer before software retention. Follow-ups are open requests, with no supplied correctness oracle; the user may reject findings or retry/cancel a run. Evidence: SRC-1, `app/src/server/halo/runQueue.ts`, `app/scripts/halo-local-runner.py`, `app/src/server/halo/storage.ts`, `app/src/server/halo/report.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Live events and terminal completed/incomplete/failed state with selected answer.
- Later read-back: Earlier user/non-empty assistant turns are reconstructed into bridge input; later follow-up reuses the export if the path exists, otherwise re-exports current matching telemetry. Report rendering consumes retained turns.
- Delegated visibility: Bridge emits interleaved agent events to host storage; follow-up message construction carries role/content turns, not child tool histories.
- Selection predicate: Run target/filters select export; turn index selects prior turns; final-flagged assistant answer wins, otherwise reverse-scanned last assistant item is used.
- Invalidation or expiry: Cancel kills the bridge; terminal failure/retry/follow-up operate at the queue layer; missing export triggers rebuilding. Report file is rewritten when missing/stale.
- Activation or effect: Software retains model-authored answer and later supplies it as conversation content; later behavioral reliance and diagnostic benefit are unobserved.
- Evidence limits: A non-empty fallback is considered completed, even without root finalization; bridge has no checkpoint handling or repo grant at this pin. Remote import mapping and deployed engine revision are not established here.

> if final_answer is None:
>     for item in reversed(items):
>         message = item.get("item") or {}
>         if message.get("role") == "assistant":
>             final_answer = content_to_text(message.get("content"))
>             final_answer_source = "last_assistant"
>             break
> --- `app/scripts/halo-local-runner.py`

> has_answer = bool((final_answer or "").strip())
> emit(
>     "completed" if has_answer else "incomplete",
> --- `app/scripts/halo-local-runner.py`

> turn.turnIndex < upToTurnIndex &&
> (turn.role === "user" || turn.content.trim().length > 0),
> --- `app/src/server/halo/storage.ts`

#### RT-RTE-report-handoff
Label: Report-to-coding-tool improvement handoff

Retained report → path-bearing prefilled deep link → user confirmation in external tool → intended verification/edit/remeasurement of a harness. Desktop code proposes acting on findings; the receiving coding actor proposes actual edits. User confirmation can stop initiation; per-edit approval, rejection and rollback depend on the external coding tool and are outside this frozen loop. The shipped skill prescribes baseline evaluation, verifying diagnostic claims against code, minimal edits and repeated evaluation. Open requests can initiate this workflow; comparative remeasurement is prescribed rather than demonstrated. Expected/reference outcomes, evaluator/provider and veto/rollback implementation depend on the harness; no universal answer oracle is provided by Halo. Persisted Halo material is the report/conversation, not an installed harness patch. Evidence: SRC-1, `app/src/desktop/commands.ts`, `skills/claude/SKILL.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Deep link carrying a prompt to read the on-disk report and act, not a completed code modification.
- Later read-back: Report path affords a coding actor later access; the skill prescribes returning with new traces/results. Actual receiving execution is outside the boundary.
- Delegated visibility: Receiving tool gets a short path-based instruction rather than an inline full report; successful file access is an external contract.
- Selection predicate: User-selected run/report and coding tool; receiving actor chooses findings, edit targets and validation.
- Invalidation or expiry: Report freshness follows materialization; skill prescribes returning to diagnosis if improvement fails. Patch rollback is uninspected — receiving executor is outside the source boundary.
- Activation or effect: Prefills a coding-tool request; actual edit/admission/deployment and production effects are unobserved.
- Evidence limits: Guidance and links do not close the improvement loop or establish autonomous/self-improving Halo operation.

> `Read the HALO trace-analysis report at ${reportPath} and act on its findings ` +
> `in this codebase: fix the identified failures and implement the recommended improvements.`
> --- `app/src/desktop/commands.ts`

> * None of them auto-run; the user confirms inside the tool.
> --- `app/src/desktop/commands.ts`

> Re-run the harness, capture new traces, ask the same diagnostic question to compare. Look at the eval delta numerically; look at whether the cited error pattern reduced in frequency.
>
> If it did, ship. If it didn't, you misread the evidence — go back to step 2 with a sharper question.
> --- `skills/claude/SKILL.md`

Theory account, limited to this prescribed hypothesis/edit pathway: guidance requests a hypothesis grounded in verified evidence, tests it against remeasurement and retains changed harness code externally. A whole hypothesis/edit is potentially localized; precise claims, scope assumptions and content-directed criticism are not constrained by a schema. The skill's trace-only assumptions disagree with the optional repository route. Method text is inspectable, but this is not evidence that Halo revises that method from its own operation.

- theory-builder conditions 1–4: assessed separately below for the prescribed pathway, not inferred from the presence of a report.
- Condition 1 conclusion status: claimed
  The skill requests forming a hypothesis; no executed whole hypothesis was inspected.
- Condition 2 conclusion status: claimed
  The skill directs the coding actor to choose an edit based on verified evidence; dependency in actual decisions is unobserved.
- Condition 3 conclusion status: claimed
  Failed remeasurement is assigned to misread evidence and sharper diagnosis, but no actual criticism/revision episode was inspected.
- Condition 4 conclusion status: claimed
  Repeated diagnosis/remeasurement is prescribed; no retained sequence of criticism shaping the next round was inspected.
- Addressability: Method steps and edit targets are individually inspectable; the specificity/addressability of model-authored hypotheses is uninspected.
- Persistence: Halo retains conversation/report; external code edits would persist in a harness checkout. Actual criticism retention and later reader are uninspected.
- learning: Improved future capacity is unestablished; no intervention comparison was inspected, and prescribed remeasurement alone cannot establish benefit or attribution.
- Reflection: The route represents a selected harness through traces and proposes representation-mediated changes; the external edit/redeployment direction is not closed by inspected Halo implementation. Reflection of Halo's own machinery is unestablished on this route.
- Reflective theory builder: uninspected — no criticism and revision of Halo method texts from its own operating records was inspected.
- Autonomous theory builder: uninspected — computational performance of every internal operation is not established; external coding execution and human confirmation remain consequential.
- Self-improvement attribution: Assessment boundary is shipped Halo, horizon subsequent analysis sessions, objective better trace-grounded diagnosis. This report handoff primarily targets an external harness. Trace-bearing findings reach a proposal, but changes to Halo's own organization, subsequent behavioral-authority entry and exercised causal dependence are unestablished. This does not exclude an external harness learning/improvement pathway; it prevents attributing exercised Halo self-improvement here.

#### RT-RTE-engine-install
Label: Host installation and update admission

Settings install/update request, or queue readiness check → host `git clone`/`pull --ff-only` → `uv sync` → engine import check → persisted installed/error settings with commit SHA. Repository content proposes the update; host software admits it by command/import success. Human settings invocation can initiate it, but queue setup can also trigger installation. Per-content human approval is not a gate shown by the inspected function. Concurrent installs are coalesced per database. Proposed change is executable engine/dependencies used by later bridge invocations, not trace-derived findings. Evidence: SRC-1, `app/src/server/halo/engine.ts`, `app/src/server/halo/runQueue.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Installed/error engine settings and status; import validation and recorded commit on successful install.
- Later read-back: Queue launches subsequent bridges in the configured installed engine path; recorded SHA reports what was installed but is not an immutable update requirement.
- Delegated visibility: Host commands receive repository URL/path and inherited execution environment; no analysis-agent context is needed.
- Selection predicate: Existing Git directory selects fast-forward pull, otherwise clone; queue checks installed/importable status before running analysis.
- Invalidation or expiry: Failure records error and throws; no transactional rollback to prior checkout/dependencies is shown in this installer. Next install request can retry.
- Activation or effect: Host code updates executable machinery and dependencies available to later analysis; deployed exercise of changed code is unobserved.
- Evidence limits: Importability is not behavioral correctness or security; mutable remote content/dependency implementations and live installation are outside this pin's evidence.

> await runCommand(["git", "-C", installPath, "pull", "--ff-only"]);
> --- `app/src/server/halo/engine.ts`

> setPhase("Installing Python dependencies…");
> await runCommand(["uv", "sync"], { cwd: installPath, timeoutMs: 240_000 });
> --- `app/src/server/halo/engine.ts`

Admission mode is host maintenance, not a trace-driven experiment. The import check supplies an importability test, not an expected diagnosis oracle. Fast-forward failure/import failure can reject successful completion but prior mutations need not be rolled back. No evidence-responsive self-change is attributed to this route.

### Claims

#### RT-CLM-delegation-policy
Label: Root delegation policy versus grant surface

Claimed operation: root should delegate exploration and reserve its own calls for delegation/finalization. This is natural-language guidance rather than a restricted root tool grant: the root factory calls the same leaf builder at depth zero. Evidence: SRC-1, `engine/agents/prompt_templates.py`, `engine/tools/subagent_tool_factory.py`; [RT-RTE-subagent-call](#rt-rte-subagent-call).

> - If maximum_depth>0, prefer to spawn subagents rather than exploring the trace data
>   yourself. Delegate trace exploration to subagents via the "call_subagent" tool;
>   besides `call_subagent`, the only tool you should call yourself is `final_answer`
>   (see the output rules below).
> --- `engine/agents/prompt_templates.py`

#### RT-CLM-trace-only
Label: Skill's trace-only diagnosis description

Claimed operation: the coding actor should verify findings because the engine cannot see code. That blanket capability description is contradicted by optional repository grants at this pin; its verification discipline remains a prescribed policy, not an execution guarantee. Evidence: SRC-1, `skills/claude/SKILL.md`, `engine/tools/subagent_tool_factory.py`; [RT-RTE-repository-inspection](#rt-rte-repository-inspection).

> Treat its output as **trace evidence**, not as a directive. It can identify patterns, cite trace_ids, surface error strings, count failure modes — that's what it's for. It cannot see your code; if it names a file path or claims a constraint is missing, **verify before acting**.
> --- `skills/claude/SKILL.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-engine-guidance
Label: Engine prompt authority over investigation

Consumer: root/child analysis models. Channel: generated system message containing usage policy, budget/depth guidance and optional caller-supplied dataset/repository sections. Force: model-interpreted policy, not dispatcher-enforced ordering or truth. Horizon: each constructed invocation/context, including replay while retained locally. Source-native text is natural language; delivery is wired but compliance is unobserved. Evidence: SRC-1, `engine/agents/prompt_templates.py`, `engine/agents/agent_context.py`, `engine/tools/subagent_tool_factory.py`; [RT-RTE-trace-diagnosis](#rt-rte-trace-diagnosis).

> "11. If depth<maximum_depth, delegate well defined multi-turn subtasks to "
> "subagents using the `call_subagent` tool rather than exploring the trace data "
> "yourself."
> --- `engine/agents/prompt_templates.py`

#### RT-BAP-report-prompt
Label: Retained report supplied to coding actor

Consumer: external coding actor and confirming user. Channel: prefilled natural-language request pointing to a Markdown report. Force: an invitation/directive to act, subject to user confirmation and receiving-tool execution/approval arrangements; not direct engine code authority. Horizon: later coding session after report retention. Actual reading and action remain unobserved. Evidence: SRC-1, `app/src/desktop/commands.ts`; [RT-RTE-report-handoff](#rt-rte-report-handoff).

> const prompt = encodeURIComponent(buildCodingToolPrompt(reportPath));
> --- `app/src/desktop/commands.ts`

## Annotations

none
