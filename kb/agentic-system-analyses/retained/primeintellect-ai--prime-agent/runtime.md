---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Prime Agent's Rust model/tool loop, Python execution boundary, delegation and change-admission routes at the frozen commit."
run-id: AAS-2026-10-14-prime-agent-8ec59ae12476-01
reviewed-boundary: "33da15a2c15c4e903c372f69ae8e1156d77d53da"
---

# Prime Agent runtime report

## Runtime account

Prime Agent conducts coding and research work through a Rust-owned assistant/tool loop and a persistent Python namespace. The model chooses text and Python calls; code owns admission, execution, event delivery and the decision to request another turn. The continual harness is an editable artifact layer around that loop, not model-weight training. This report uses SRC-1 implementation and doctrine/design only. No execution trace, provider response, test result or causal experiment was supplied or produced. All operation and benefit conclusions remain uninspected. [SRC-1: `README.md`, `crates/pa-agent/src/agent_loop/run.rs`, `prime-agent-runtime/src/rlm/repl.py`, `crates/pa-core/src/refinement/planner.rs`]

### Ordinary invocation: headless prompt to answer

For an ordinary print invocation, the CLI dispatches PrintRuntime, selects a fresh/opened/forked persistent session or an in-memory no-session manager, and retains the opened file lease. It creates an inline child-session root and builds the core engine with resolved model/authentication, settings, resources, host handlers and Python provisioner. The initial prompt, or successive CLI messages, is the human/caller's task; an explicitly classified slash command instead runs a host command without creating that model turn. The principal for local effects is the OS user running the process. Session IDs identify persistence and semantic-edge ledgers; tool-call IDs identify returned results. Model choice uses a provider/model selector, not a frozen weight identity. [RT-RTE-print-prompt](#rt-rte-print-prompt), [RT-CMP-provider-model](#rt-cmp-provider-model).

The engine builds model-visible system instructions and tools, restores available session context, and supplies harness digest context separately. Both daemon and print configurations initially supply no extra model tools; core assembly adds the kernel-backed Python tool. The model returns an assistant message containing text and/or tool calls. Rust looks up each tool, prepares and executes calls, emits results and appends them to context. Sequential tools force sequential batches; the generic agent library also supports parallel dispatch. Thus an outer tool list of one Python entry does not imply a single narrow effect capability: Python can call shell commands, imported skills, MCP clients and typed host callbacks. [SRC-1: `crates/pa-cli/src/print_runtime.rs`, `crates/pa-core/src/session_engine/engine.rs`, `crates/pa-agent/src/agent_loop/tools.rs`, `crates/pa-core/src/session_engine/runtime_wiring.rs`]

The next-step owner alternates: model inference chooses a proposed action; Rust executes the accepted call and controls another request. Tool results, steering inputs and follow-up inputs are symbolic message envelopes containing natural-language output or structured values. The Python executor retains variables in its own process. Session history is separate from that live namespace; only artifact-backed provisioners receive a revivable snapshot directory. Errors and aborts end or interrupt the run through explicit loop branches; interruption is not transaction rollback of external file or shell effects. A normal no-tool answer ends only if no steering, follow-up, goal or autonomous continuation remains. Print mode waits for idle and runs settled-turn boundaries, then emits text or JSON events and disposes inline descendants on exit. [SRC-1: `crates/pa-agent/src/agent_loop/run.rs`, `crates/pa-cli/src/print_runtime.rs`, `crates/pa-core/src/session_engine/runtime_wiring.rs`]

> let message =
>     stream_assistant_response(current_context, config, signal, emit, stream_fn).await?;
> new_messages.push(AgentMessage::from(message.clone()));
> --- `crates/pa-agent/src/agent_loop/run.rs`

### Shipped alternate paths and forcing cases

Interactive/TUI and ACP are daemon clients rather than separately implemented Python/model loops. The daemon worker builds a core engine with a supervisor child host, MCP settings, session directory and conversation-log path. Its core SessionManager deliberately stays in memory because the worker owns the durable file. The serving provider target is live: changing the model can update the stream without rebuilding the session. RPC is another shipped headless embedding, but its print-runtime assembly supplies no inline child host; the default core host has no-children behavior. These differences prevent a blanket claim that every CLI transport has the same delegation or durable-state grant. [RT-RTE-daemon-session](#rt-rte-daemon-session); SRC-1: `crates/pa-cli/src/print_runtime.rs`, `crates/pa-core/src/session_engine/runtime_wiring.rs`.

Four selected forcing cases challenge otherwise plausible runtime-wide guarantees:

1. **Python to shell or extension code.** The REPL evaluates compiled cells in its namespace, and bash launches the configured shell with the current working directory and child environment. Installed Python skills are pre-imported through provisioner wiring. Neither the outer tool schema nor process separation confines those local effects. The product expressly disclaims a security sandbox. [RT-RTE-python-effects](#rt-rte-python-effects), [RT-CLM-user-permissions](#rt-clm-user-permissions).
2. **Spawn admission versus completed child result.** `rlm.spawn` immediately returns a handle after task admission, not the answer. Both inline and daemon hosts gate recursive depth and sibling names, but daemon depth-zero code also exposes resident session creation, which inline print rejects. A depth gate is therefore a protocol bound on recursive children, not a universal limit on processes, new root sessions or provider calls reachable through Python. [RT-RTE-child-spawn](#rt-rte-child-spawn).
3. **Compaction with a surviving kernel.** Context replacement removes old messages from the model window without itself resetting the Python process or erasing all durable session entries. The complete path then attempts to prune live variables above the per-variable snapshot limit before listing remaining names and delivering a persistence notice. Process survival therefore does not guarantee preservation of every value. Remaining namespace state is independent of the model window; a compacted window is not a clean execution environment. [RT-RTE-context-compact](#rt-rte-context-compact).
4. **Refinement amid a concurrent kernel write.** Refinement captures a baseline before its slow model request, then reloads and updates the target store under a lock. A changed entry is rejected rather than overwritten. Factory enablement is re-read at apply time. However, Python harness writes and direct filesystem edits are alternate paths; the refiner's special protections do not govern every write possible with user permissions. Factory deletion also remains possible while its authoring gate is disabled. [RT-RTE-harness-refine](#rt-rte-harness-refine), [RT-RTE-python-effects](#rt-rte-python-effects).

No live forcing experiment was run. Provider-native tool execution beyond the inspected client path, all third-party MCP server internals, arbitrary user extensions and shell subprocess internals remain uninspected. The capability surface is broad local execution; the current configured credentials, enabled servers, skill packages and depth limits are session grants; the deployed isolation envelope is an external operator responsibility. No actual deployment envelope is established by this repository. [SRC-1: `README.md`, `crates/pa-daemon/src/agent_engine/lifecycle.rs`, `crates/pa-core/src/session_engine/runtime_wiring.rs`]

### Continuations, orchestration and admission

Goals and autonomous work can keep the ordinary invocation alive after an answer. In print mode the natural-turn-end hook gives the goal arm priority and autonomous policy the fall-through; both defer behind unsettled inline child work. A threshold compaction can end the current run and hold the next continuation for a boundary drive. The code policy, not an independent model oracle, owns this scheduling decision; task execution remains model-driven. Scheduled daemon wake-ups and heartbeat bindings use live and durable session identities, with an embedding-owned store replacing the private default. Their wiring is inspected, but the full scheduler and all recovery branches were not traced here. [SRC-1: `crates/pa-cli/src/print_autonomous.rs`, `crates/pa-core/src/session_engine/runtime_wiring.rs`]

Factory execution adds a symbolic state-machine controller around isolated child agent contexts. Stored specs and library machine files share validation/canonicalization and subagent resolution before admission. Kernel memory owns the run registry; the supervisor owns child sessions. Losing the kernel loses factory-run control state, while daemon-owned children can remain running and discoverable. These are separate recovery domains, not durable workflow replay. [RT-RTE-factory-run](#rt-rte-factory-run).

Changes enter three distinct channels: model/software-admitted harness edits; filesystem-written skill/instruction packages discovered at startup or reload; and operator-invoked release activation with a detached coordinator. Harness admission is not a test of improved behavior. Skill discovery is not content approval. Release probes and checksums are not evidence of task quality or independently trusted release origin. The records below distinguish these owners and limits. [RT-RTE-harness-refine](#rt-rte-harness-refine), [RT-RTE-skill-install](#rt-rte-skill-install), [RT-RTE-release-update](#rt-rte-release-update).

### Enforcement scope

| Guarantee and owner | Enforcement, strength and covered paths | Alternate paths / external contract | Separate conclusions |
|---|---|---|---|
| Recursive child depth and sibling-name uniqueness; child host | `spawn` checks depth before admission; inline spawn gate and daemon name reservation cover their recursive host requests. Protocol. | Root-session creation, arbitrary Python subprocesses and remote clients are not recursive-child admissions. Requires truthful host identity/configuration and cooperating supervisor. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Preserve concurrently changed harness entries; refiner and state store | Baseline comparison and locked reload/apply/save cover the inspected refinement route; cooperating Python helpers lock too. Protocol. | Direct writes can bypass the lock; filesystem/lock ownership and atomic-write contracts are required. No all-writers invariant. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Base prompt not editable by refinement; planner | Reserved `base_system_prompt` prompt entry is rejected; proposal doctrine also forbids source edits. Protocol for the entry check, policy for model compliance. | Custom system prompt at construction, new skills and arbitrary source/file modification are different channels. No OS enforcement of prompt immutability. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Factory authoring/execution opt-in; kernel namespace and refiner | Public namespace calls `require_factory_enabled`; refiner checks apply-time enablement. Create/update rejection, not delete rejection. Protocol scoped to supported APIs. | File tampering or calling private implementation from unrestricted Python is not a sandboxed path. Requires shared settings path. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Process lifecycle isolation; product/OS | Kernel and worker processes have lifecycle and restoration seams. No claimed security guarantee. | Host OS user permissions are the effect boundary; external sandbox is required for untrusted code. | implementation conclusion status: wired; operation conclusion status: uninspected |

Evidence: SRC-1 `crates/pa-cli/src/print_rlm.rs`, `crates/pa-daemon/src/rlm_children/host.rs`, `crates/pa-core/src/refinement/planner.rs`, `crates/pa-core/src/refinement/mod.rs`, `prime-agent-runtime/src/rlm/harness.py`, `prime-agent-runtime/src/rlm/factory.py`, `README.md`. Supporting minimum passages appear in the corresponding records.

Added source coverage beyond the boundary's initial inspection includes the tool-batch dispatcher; engine assembly; print prompt admission, inline child admission and continuation hook; daemon child admission; REPL evaluation and shell launching; Python harness upsert/locking; factory validation/run-machine launch; refiner baseline validation and apply-time gate; context replacement and post-compaction pruning/namespace notice (`crates/pa-core/src/session_engine/ipython_state.rs`, `crates/pa-core/src/kernel/provisioner.rs`, `prime-agent-runtime/src/rlm/repl.py`); bundled skill-creator instructions; and the release-update command. All are SRC-1 implementation except skill instructions and product risk disclosure, which are doctrine/design. Broad included modules not read in depth remain available, not absent: all provider retry variants, scheduler recovery, built-in machine internals, installer platform parity and coordinated successor restart were not exhaustively established.

## Shared records

### Components

#### RT-CMP-provider-model
Label: Provider-selected models

Source-native identity: the selected `Model` and serving `ProviderTarget` in engine construction; child selectors can choose another provider/model, and refinement receives a Model/refiner call. Representational form: distributed-parametric remote inference. Storage substrate: provider infrastructure; local registry/settings hold symbolic selectors, not weights. No inspected route changes those parameters during operation. Whether a provider updates them behind an endpoint is uninspected. Exact weights/version are not pinned by this Git revision. A mutable provider endpoint or live model target can resolve to another model; daemon `set_model` changes the live target without session rebuild. Internal provider caching, adaptation and weight provenance remain uninspected. [SRC-1: `crates/pa-daemon/src/agent_engine/lifecycle.rs`, `crates/pa-cli/src/print_runtime.rs`, `prime-agent-runtime/src/rlm/__init__.py`, `crates/pa-core/src/session_engine/refine.rs`]

> let stream_fn = switchable_stream_fn(std::sync::Arc::clone(&self.provider_target));
> --- `crates/pa-daemon/src/agent_engine/lifecycle.rs`

#### RT-CMP-repl-kernel
Label: Persistent Python kernel

Source-native identity: `rlm.repl`, provisioned per session with typed host handlers and Python skills. Representational form: symbolic executable Python and protocol frames. Storage substrate: process namespace; optional session-artifact snapshots. A surviving process retains an independent namespace, but the post-compaction path can delete oversized live variables; process persistence is not unconditional value preservation. Shell commands and imported packages extend its effects; a process boundary is not a security boundary. [SRC-1: `prime-agent-runtime/src/rlm/repl.py`, `crates/pa-core/src/session_engine/runtime_wiring.rs`]

> Cells execute with top-level await in one persistent
> ``__main__`` namespace on a single asyncio event loop.
> --- `prime-agent-runtime/src/rlm/repl.py`

### Operative objects

#### RT-OBJ-session-context
Label: AgentContext and session entries

Source-native identity: `AgentContext` and SessionManager's retained session entries. Representational form: symbolic message/event envelopes, with natural-language text interpreted by models. Storage substrate: Rust memory and session files when persisted; daemon worker owns its durable file while the built core manager stays in memory. A session file, active session ID and live Python namespace are not interchangeable identities. Restoration rebuilds model context from session entries, including compaction-aware reconstruction. [SRC-1: `crates/pa-agent/src/agent_loop/run.rs`, `crates/pa-daemon/src/agent_engine/lifecycle.rs`, `crates/pa-core/src/session_engine/engine.rs`]

> let initial_messages = if existing_messages.is_empty() {
>     None
> } else {
> --- `crates/pa-core/src/session_engine/engine.rs`

#### RT-OBJ-factory-machine
Label: Factory machine specification

Source-native identity: factory `arguments.machine`, DAG sugar compiled to machine form, or library `MachineFile.spec`. Representational form: symbolic states, transitions, guards and bounds, separately containing model-interpreted task templates. Storage substrate: harness JSON or library files; canonicalized spec and run state reside in Python memory. Template text supplies instructions to children; symbolic guards decide progression. The stored spec is not the live run registry. [SRC-1: `prime-agent-runtime/src/rlm/factory.py`]

> canonical = canonicalize_factory_spec(machine.spec)
> harness = self._resolve_harness()
> resolved, reference_errors = self._resolve_subagents(harness, canonical)
> --- `prime-agent-runtime/src/rlm/factory.py`

### Routes

#### RT-RTE-print-prompt
Label: Print prompt invocation

Endpoints: CLI task to core engine, provider, Python tool and terminal. Owner: PrintRuntime/SessionEngine and Rust agent loop; foreground model proposes next actions. Context/state effects: constructs/restores model messages and kernel wiring, appends assistant/tool results and caller input, runs boundary hooks. Operating mode: open requests, with optional goals/autonomous gates, not a bounded curriculum. No built-in expected-answer oracle is established by this route.

- Immediate return: terminal text or JSON events and process exit after prompt/boundary driving; Python tool returns execution results inside the invocation.
- Later read-back: persistent session selection restores retained context; no-session uses an in-memory manager and does not supply the ordinary file-backed history path.
- Delegated visibility: an inline root hosts child sessions; each child receives its task and assembled context, not automatic access to every parent turn.
- Selection predicate: CLI mode/session flags and initial/later messages; slash commands are intercepted before a model turn.
- Invalidation or expiry: abort/error/normal completion ends the loop; print exit disposes descendants. External effects are not reversed by this disposal.
- Activation or effect: configured provider requests and Python execution are wired; task success and compliance are unobserved.
- Evidence limits: implementation only; all terminal-result semantics and provider success remain untested here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

[SRC-1: `crates/pa-cli/src/print_runtime.rs`, `crates/pa-agent/src/agent_loop/run.rs`, `crates/pa-agent/src/agent_loop/tools.rs`]

> engine.session.agent().wait_for_idle().await;
> --- `crates/pa-cli/src/print_runtime.rs`

#### RT-RTE-daemon-session
Label: Daemon-backed session invocation

Endpoints: interactive/ACP client through supervisor/worker to core engine and provider/kernel; return through client transport. Owner: worker engine and shared loop, not the UI. Identity/state: durable session file, active session ID, cwd and serving ProviderTarget; supervisor supplies child host. MCP settings are re-read by resolver closures. Client configuration supplies model, instructions and resources; the current external credentials/servers are not frozen.

- Immediate return: streamed session events and result over the client connection; ACP startup errors return nonzero before its first frame.
- Later read-back: worker-owned session files seed/adopt core context; core itself is deliberately non-persisted in this embedding.
- Delegated visibility: supervisor-owned child sessions and usage attribution rather than print's inline tree.
- Selection predicate: client session-create/open request and engine model/resource configuration.
- Invalidation or expiry: worker/session lifecycle and model/reload controls; quota/goal restoration seams exist, but complete recovery coverage is uninspected.
- Activation or effect: core model/tool loop with live model target and kernel is wired; successful reattachment is not observed.
- Evidence limits: transport/engine construction inspected, not every RPC command or supervisor scheduler failure mode.
- implementation conclusion status: wired
- operation conclusion status: uninspected

[SRC-1: `crates/pa-cli/src/print_runtime.rs`, `crates/pa-daemon/src/agent_engine/lifecycle.rs`, `crates/pa-core/src/session_engine/runtime_wiring.rs`]

> // The engine session stays non-persisted (the worker owns the
> // durable file); the configured session dir leads, the file's
> // parent is the fallback.
> --- `crates/pa-daemon/src/agent_engine/lifecycle.rs`

#### RT-RTE-python-effects
Label: Python effect and direct admission path

Endpoints: model Python cell to REPL eval, shell/imports/MCP or typed host callback. Owner: kernel executor for evaluation, specific host handler for typed requests, OS for access enforcement. Code and structured requests are symbolic; outputs cross back as tool results. Imported skill instructions may guide the proposing model, but do not constrain arbitrary Python semantics. Direct harness `upsert` is an alternate admission path: model/caller supplies content; Python shape checks and locked write admit it without the refiner's diagnosis pass or per-content human approval. File writes can also change project code, instructions or capability packages. Reject/rollback rights on these unconstrained filesystem effects depend on the caller/OS and external version control, not a universal Prime Agent gate.

- Immediate return: execution stdout/stderr/result, error or host reply; bash starts with a live handle that can be awaited.
- Later read-back: Python variables persist while kernel survives; artifact-backed snapshots may revive state; filesystem and harness edits reach their later loaders.
- Delegated visibility: host-request frames carry typed data and correlation IDs; subprocess visibility follows inherited environment/cwd, not parent model-window sharing.
- Selection predicate: model-generated code, imported helpers and caller-selected APIs; configured host handlers determine accepted typed callbacks.
- Invalidation or expiry: interrupts/process teardown and optional restore; abort does not undo shell/file effects, and arbitrary code can bypass helper protocols.
- Activation or effect: executable eval and shell calls can mutate local state under user permissions; actual edits and later behavioral dependence are unobserved.
- Evidence limits: no deployed sandbox/grant set inspected; third-party MCP/provider internals and user extensions are opaque to this account.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Operating mode: open task execution. Proposed changes are supplied by the foreground model or caller; software executes or validates the chosen helper, and humans may review resulting changes but an obligatory per-edit veto is not established by these inspected paths. No expected-answer oracle is inherent in eval or upsert. Memory-specific mutation semantics are left to the memory analyst. [SRC-1: `prime-agent-runtime/src/rlm/repl.py`, `prime-agent-runtime/src/rlm/bash.py`, `prime-agent-runtime/src/rlm/harness.py`, `crates/pa-core/src/session_engine/runtime_wiring.rs`]

> value = eval(code_obj, ns)  # noqa: S307 - executing the model's cell is the runtime's job
> --- `prime-agent-runtime/src/rlm/repl.py`

> with self._locked():
>     return self._upsert(
>         kind,
>         title,
>         content,
> --- `prime-agent-runtime/src/rlm/harness.py`

#### RT-RTE-child-spawn
Label: Recursive child admission and collection

Endpoints: parent Python `rlm.spawn` through `rlm.run` host request to inline or supervisor child; later collect/messages/files to parent. Owner: parent model proposes task/model/name; child host decides admission; child has its own next-step model/tool loop. Representational forms: natural-language task plus symbolic selector/handle/roster/result. Context isolation keeps the child's working turns out of the parent's window; only explicitly delivered results/messages/files cross back. Unlike a simple stack frame, children can remain resident and accept follow-ups, and collect does not delete their result state.

- Immediate return: admitted child's handle with identity/name/session directory/model, not completed task answer.
- Later read-back: collect can re-read retained child results; persisted child session state depends on embedding and session directory.
- Delegated visibility: direct-child roster and explicit messages/files/results; no automatic whole-parent-transcript inheritance is established here.
- Selection predicate: requested task, unique sibling name and provider/model/thinking selectors; host depth and model admission checks.
- Invalidation or expiry: explicit delete, abort/disposal or lifecycle end; inline descendants cannot outlive print cleanup, unlike supervisor-owned daemon children.
- Activation or effect: admitted child runs an independent core loop; answer accuracy and coordination success are unobserved.
- Evidence limits: inspected both host admission gates and API contract; not all child watch/delete/recovery branches.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/selection: model proposes; host can reject depth, name or model/thinking incompatibility. An initial human task is not per-child approval. Operating mode: open delegated tasks. No expected-answer/reference oracle is inherent in collect. Depth-zero daemon `create_session` is a distinct root-session route; inline host returns a daemonless error and daemon rejects nonzero depth. [SRC-1: `prime-agent-runtime/src/rlm/__init__.py`, `crates/pa-cli/src/print_rlm.rs`, `crates/pa-daemon/src/rlm_children/host.rs`]

> if node.depth >= node.max_depth {
>     return Err(rlm_depth_limit_error(node.depth, node.max_depth));
> }
> --- `crates/pa-cli/src/print_rlm.rs`

> if identity.rlm_depth >= identity.rlm_max_depth {
>     bail!(rlm_depth_limit_error(
>         identity.rlm_depth,
>         identity.rlm_max_depth
>     ));
> }
> --- `crates/pa-daemon/src/rlm_children/host.rs`

#### RT-RTE-factory-run
Label: Factory machine execution

Endpoints: stored factory ID or library machine to validator/canonicalizer, resolved subagent tasks and background run controller. Owner: FactoryExecutor for symbolic state progression, child models for task execution, supervisor for children. It resolves all subagent references before launch. Guards/joins and max-parallel constraints are code decisions; prompt templates are model-interpreted guidance. This is bounded orchestration, not by itself a theory-revision or improvement experiment.

- Immediate return: run ID/spec/name/node counts and started/pending states after entry admission; a background task continues execution.
- Later read-back: stored spec is loaded for another run; live status is read from kernel run registry, which is not durable across restart.
- Delegated visibility: child prompts receive resolved state inputs; collect returns selected child outputs to the machine; parent receives status/graph output.
- Selection predicate: requested stored ID or library machine; validation/canonicalization, resolved references, ready states and transition guards.
- Invalidation or expiry: stop/delete, budget/policy pause, terminal completion or kernel loss; supervisor children may outlive lost factory registry.
- Activation or effect: launches children through the shared spawn protocol and advances the machine; completed workflow/product quality is unobserved.
- Evidence limits: run and library launch inspected; all guard evaluator variants and bundled builder/PR-manager/review-sweep internal tasks are not inspected in depth.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not factory_enabled():
>     raise ValueError(FACTORY_DISABLED_MESSAGE)
> --- `prime-agent-runtime/src/rlm/factory.py`

Human/software roles: user enables factory; model/caller chooses spec and can author inputs; validator rejects malformed machines or unresolved references; code schedules and handles policy states. Resuming an escalate-paused run is exposed, not proof that every pause receives a human decision. Expected-answer oracle: no general oracle established; symbolic output/guard tests assess declared conditions, not necessarily task truth. [SRC-1: `prime-agent-runtime/src/rlm/factory.py`]

> if reference_errors:
>     raise ValueError("; ".join(reference_errors))
> run = self._create_run(entry.id, canonical, resolved, name=name)
> return await self._launch_run(run)
> --- `prime-agent-runtime/src/rlm/factory.py`

#### RT-RTE-context-compact
Label: Model-window compaction

Endpoints: manual/threshold compaction request through summarization and commit to reconstructed loop messages. Owner: code chooses cut/threshold and serializes context replacement; runtime model produces summary under the fixed summarization prompt. Natural-language summary replaces part of current model context; retained symbolic session entries support reconstruction. Instructions ask for goals, constraints, progress, decisions, next steps and exact names; this is a request for faithful compression, not enforced semantic equivalence.

- Immediate return: ran/skipped/error outcome and rebuilt loop context after successful compaction.
- Later read-back: compaction summary reaches later model invocations and session reconstruction; older retained entries are not necessarily erased from disk.
- Delegated visibility: inapplicable — this route replaces the current session window rather than spawning a separate task context.
- Selection predicate: manual request or token/usage threshold; code selects a valid pre-cut prefix and preserved tail.
- Invalidation or expiry: further compaction/rebuild replaces window material; after context replacement, post-compaction pruning can delete live variables above the per-variable snapshot limit. Remaining namespace state stays independently available and the host reports pruning/remaining names in a persistence notice when the kernel is still running.
- Activation or effect: `set_messages` replaces model-visible context; the subsequent host prune call can remove oversized names from the live namespace after snapshot payload and manifest replacement. Factual fidelity and subsequent behavioral benefit are unobserved.
- Evidence limits: compaction decision/replacement and post-compaction prune/notice inspected; pruning requires a running kernel and snapshot target, and failed artifact replacement can withhold deletion. All summarization retries and retained-history recovery branches are not audited.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Mode: working-context compression during open requests. Code may skip or retry; the summarizer proposes text, software commits it, and no per-summary human approval or expected-answer oracle is established. This resembles freeing window content while keeping a summary and retained history; the Python namespace is a separate state domain, not a model-window pointer that automatically reloads lost messages. [SRC-1: `crates/pa-core/src/session_engine/compaction.rs`, `crates/pa-core/src/session_engine/compaction_arms.rs`, `crates/pa-core/src/session_engine/ipython_state.rs`, `crates/pa-core/src/kernel/provisioner.rs`, `prime-agent-runtime/src/rlm/repl.py`]

> let pruned = probe.prune_oversized_variables().await;
> --- `crates/pa-core/src/session_engine/ipython_state.rs`

> for name in pruned:
>     ns.pop(name, None)
> --- `prime-agent-runtime/src/rlm/repl.py`

> let loop_messages: Vec<AgentMessage> = rebuilt_loop_messages(rebuilt);
> let rebuilt_message_count = loop_messages.len();
> self.agent.set_messages(loop_messages).await;
> --- `crates/pa-core/src/session_engine/compaction_arms.rs`

#### RT-RTE-harness-refine
Label: Trajectory-fed harness refinement

Endpoints: user `/refine`, queued kernel skill request or automatic review checkpoint to refiner proposal, locked store application, audit/outcome/notice and subsequent harness consumption. Owner: host schedules and applies; model proposes content and automatic review judgment; parser/validator/conflict checks decide admissibility. User can request scope/instructions or rollback; no obligatory per-proposal human approval is established. Local is default and requires a session directory; explicit global request targets cross-session material. The planner sees trajectory, harness state and refinement history. Guidance asks for small evidence-backed edits and rollback/replacement of faulty entries; it requests rationale and expected outcome, but has no independent reference-answer oracle.

- Immediate return: kernel `refine.run` schedules and returns immediately; host execution later returns applied/rejected edit records and appends audit/outcome plus notice when an edit applied.
- Later read-back: persisted local/global harness state is merged and ranked for model-facing digest; audit/history feed later planning. Memory-specific entry/digest semantics are left to the memory member.
- Delegated visibility: refiner receives selected transcript/state/history, not a delegated foreground child; notices expose outcomes to the current model.
- Selection predicate: manual/queued request or model automatic-review decision; requested scope and baseline comparisons select permissible edits.
- Invalidation or expiry: update/delete or explicit rollback changes entries; baseline conflict rejects stale edits; no global benefit expiry is inferred.
- Activation or effect: store mutation and notice/digest delivery are wired; reliable compliance, exercised improvement and capacity gain remain unobserved.
- Evidence limits: implementation of planning/application and guards inspected; source model instructions establish requested criticism, not actual content-directed criticism or improved behavior.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/recovery: model JSON is normalized, validated per edit and applied against reloaded state under lock; application can reject individual edits. Reserved base prompt entry is protected within this mechanism. Factory create/update uses apply-time opt-in while delete remains cleanup. Baseline guards reject entries changed during planning. Result history retains before/after edits for rollback; audit append can fail after state mutation, so this is not one atomic transaction spanning state, global history and session rows. All-writer synchronization requires cooperating helpers and filesystem guarantees. Direct Python upsert and arbitrary file writes are separate channels. [SRC-1: `skills/refine/SKILL.md`, `crates/pa-core/src/refinement/planner.rs`, `crates/pa-core/src/refinement/mod.rs`, `crates/pa-core/src/session_engine/refine.rs`, `crates/pa-core/src/session_engine/compaction_arms.rs`, `crates/pa-core/src/session_engine/harness_digest.rs`]

> if kind == RefinementKind::Prompt
>     && (edit.id.as_deref() == Some("base_system_prompt")
>         || computed_id == Some("base_system_prompt"))
> {
>     return Some("base system prompt is not editable".to_string());
> }
> --- `crates/pa-core/src/refinement/planner.rs`

> if options.baseline_state.is_some()
>     && !proposal_modified_keys.contains(&entry_key)
>     && serde_json::to_value(&before).ok() != serde_json::to_value(&baseline).ok()
> {
> --- `crates/pa-core/src/refinement/planner.rs`

> if kind == RefinementKind::Factory
>     && action != RefinementAction::Delete
>     && !options.factory_enabled
> {
> --- `crates/pa-core/src/refinement/planner.rs`

> lock.ensure_owned()?;
> let written = save_harness_state(harness_state_dir, &state)?;
> Ok((result, written))
> --- `crates/pa-core/src/refinement/mod.rs`

#### RT-RTE-skill-install
Label: Skill package admission

Endpoints: authored skill directory to discovered instructions and optional Python package bootstrap. Owner: foreground model/human writes files; resource loader discovers; kernel bootstrap installs/pre-imports Python skill modules. Representational parts: natural-language SKILL.md body and description, symbolic frontmatter and Python program. Storage: project/global/package files, not model weights. Guidance shapes proposal by asking for kind/location, concise routing description and verification. Loading/reload is capability admission, not approval of content safety or quality.

- Immediate return: filesystem write/command results from authoring; startup/reload yields available skill resources or diagnostics.
- Later read-back: later session startup or explicit reload discovers changed skill text/package; model can request body on demand.
- Delegated visibility: available skills are assembled per session; no automatic sharing of all authoring conversation with another session.
- Selection predicate: configured paths and precedence; names/descriptions route on-demand interpretation, explicit skill invocation selects a named body.
- Invalidation or expiry: file edit/removal, collision precedence or reload changes discovered resources; rollback is filesystem/version-control responsibility, not a uniform skill admission transaction.
- Activation or effect: body supplies model instructions; Python modules can add executable local capabilities. Actual invocation/compliance is unobserved.
- Evidence limits: bundled skill-creator contract and kernel module wiring inspected; full resource-loader precedence implementation and package-install rejection branches not audited.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Proposal/admission roles: humans can choose/edit location/content; model may author and verify files in an open request; software discovery/bootstrap supplies later consumers. No mandatory per-content human veto or expected-answer oracle is established by the inspected instruction. This route is distinct from a harness skill entry referencing an already installed Python callable. [SRC-1: `skills/skill-creator/SKILL.md`, `crates/pa-core/src/session_engine/runtime_wiring.rs`, `crates/pa-core/src/session_engine/engine.rs`]

> In an interactive session, `/reload` picks up new skills without a restart; other sessions pick them up on start.
> --- `skills/skill-creator/SKILL.md`

#### RT-RTE-release-update
Label: Release activation admission

Endpoints: `prime-agent update` options to managed-install plan, download/direct candidate/rollback, staged candidate and detached coordinator/status result. Owner: invoking CLI and coordinator, not foreground model judgment. Proposed change is a release binary/payload; user selects channel, force, rollback or direct archive/source. Code can refuse an unmanaged install, failed download/stage/probe or plan. Release version and archive checksum are symbolic checks, not a task answer oracle.

- Immediate return: terminal update status/report and exit code after status tail; concurrent invocation may join existing update status.
- Later read-back: candidate becomes installation machinery for later launches through coordinated activation; status persists for monitoring/recovery.
- Delegated visibility: detached coordinator receives staged candidate/installation intent, not model task context.
- Selection predicate: managed install, channel/version/options or supplied direct payload; acquisition lock, stage validation and version probe.
- Invalidation or expiry: planning/staging failure keeps installed release; rollback chooses previous release; complete coordinated restart/recovery behavior remains uninspected here.
- Activation or effect: download/stage/probe/coordinator handoff is wired; successful live version transition is unobserved.
- Evidence limits: command front-half inspected; swap/coordinator/successor internals and independent release-origin trust were not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Mode: operator-invoked deployment change, not trajectory-fed learning. Guidance is release/install configuration and update options; staged binaries and status are retained, not theories or criticisms. Humans initiate/select source; software validates and activates; no per-task behavioral evaluator is established. Digest checking requires a trusted expected checksum source and does not itself authenticate that source. [SRC-1: `crates/pa-cli/src/update_flow/update_command.rs`]

> super::swap::validate_candidate(&release_dir.join("prime-agent"), &version).await?;
> --- `crates/pa-cli/src/update_flow/update_command.rs`

### Claims

#### RT-CLM-user-permissions
Label: User-permission execution disclosure

Claimed operation: local model-generated Python and commands run with user permissions; worker/kernel separation is not security sandboxing. Doctrine agrees with inspected eval/shell wiring. This establishes a product disclosure and executable capability, not an actual deployment's containment. [SRC-1: `README.md`, `prime-agent-runtime/src/rlm/repl.py`, `prime-agent-runtime/src/rlm/bash.py`]

> Prime Agent executes model-generated Python and project commands with your user permissions. Its worker and kernel processes improve lifecycle isolation and recovery; they are **not** a security sandbox.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-harness-digest
Label: Harness digest to foreground model

Consumer: foreground session model. Channel: merged/ranked harness digest custom prompt row converted to a user turn, separate from the base system prompt. Force: model-interpreted guidance/data, not deterministic enforcement or proof of compliance. Horizon: later turns and local/global later session use according to retained scope. Relevance terms come from active goal and recent text; digest is a selected rendering, not unconditional full-store delivery. This supplies the downstream channel for refinement without establishing later behavior causally depended on an edit. [SRC-1: `crates/pa-core/src/session_engine/harness_digest.rs`, `crates/pa-core/src/session_engine/engine.rs`]

> /// The digest as the loop's custom prompt row: it rides the run's prompt
> /// messages and converts to a user turn at the loop's LLM boundary.
> --- `crates/pa-core/src/session_engine/harness_digest.rs`

#### RT-BAP-machine-guards
Label: Factory guards to state progression

Consumer: FactoryExecutor. Channel: validated canonical machine with symbolic transitions/guards and resolved child outputs. Force: code-controlled state admission; the task prompt's natural-language body has a separate model-interpreted force. Horizon: one kernel-resident run; stored specs can initiate later runs, but registry loss prevents claiming durable replay. [SRC-1: `prime-agent-runtime/src/rlm/factory.py`]

> self._runs[run.run_id] = run
> self._event(
>     run, "run_started", detail=f"{len(run.states)} states, max_parallel {run.max_parallel}"
> )
> --- `prime-agent-runtime/src/rlm/factory.py`

## Annotations

none
