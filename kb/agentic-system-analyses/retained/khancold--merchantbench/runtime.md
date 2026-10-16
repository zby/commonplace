---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "MerchantBench runtime baseline tracing the shipped ReAct/store loop, HTTP controls, alternate clients, hosted evaluation and Hermes launch boundary."
run-id: AAS-2026-10-15-merchantbench-d2f4d78dbe37-01
reviewed-boundary: d9e5bd7519ab100193c21778aecfb59e30f24651
---

# MerchantBench runtime report

## Runtime account

### Evidence and consequential work

MerchantBench runs a simulated store and evaluates its operator, rather than supplying a general-purpose agent operating system. The frozen workflow includes the operator clients, simulation scheduler, persistence and terminal metric extraction. The [boundary](boundary.md) supplies SRC-1 and the evidence limits. All findings here are implementation inspection or attributed source design, not observed execution. No target code, tests, examples, containers or providers were executed. Activation of model guidance and improvements in store performance remain unobserved.

Additional implementation inspection at SRC-1 covered `env/web/auth.py`, `env/tools/dispatch.py`, `env/tools/registry.py`, `env/web/templates/_human_playground_script.html`, `env/web/app.py`, manual dashboard control routes, Hermes profile preparation/spawning, SDK retry and step headers, ReAct context/recovery branches, simulator idempotency and rehydration, `agent/baselines/auto_seed.py` and batch creation. These extend initial boundary coverage without adding sources. Provider internals, external Hermes behavior, arbitrary submitted agents and private-data performance remain outside the evidence.

### Ordinary shipped invocation

The ordinary model-calling path is [RT-RTE-react-loop](#rt-rte-react-loop). An operator starts `env/run.py`, which loads local configuration and builds the threaded Flask application. `env/web/app.py` installs one registry, optional authorization and agent/dashboard blueprints. A caller creates a run through `POST /runs`, supplying a scenario or selecting a scenario file, seed and optional bootstrap agent. API creation does not auto-start unless requested. The dashboard, batch driver or evaluator can request automatic progression; a separate ReAct process can also attach by run ID and agent ID. These are all shipped responsibilities, not external enclosing applications (SRC-1, `env/run.py`, `env/web/app.py`, `env/web/routes_dashboard.py`, `scripts/run_batch.py`, `eval/run_eval.py`).

The worker owns simulation progression. `env/web/run_worker.py` selects active versus draining phases and invokes `Environment.step`. The simulator advances demand/orders/suppliers and commits the transition before exposing the decision hook. Hooks occur according to scenario activation settings, not necessarily on every hourly transition. The frozen default has `activation_period: 12`, `max_turns_per_step: 30`, and a denylist containing `market_brief` and `hot_search_terms`, but not memory tools (SRC-1, `env/core/simulator.py`, `env/scenarios/default.yaml`).

The SDK fetches available tool schemas, registers client metadata and long-polls observation. On the first served observation for an agent, the server includes a composed brief. The baseline keeps that brief as its system prompt and appends rendered observation text to local history. The model receives the prompt, selected recent history and function schemas; the server's full structured observation packet is not passed wholesale. For Claude-named models the client moves the system prompt to provider-specific `extra_body` configuration and adds cache breakpoints. Both request forms converge on the same OpenAI-compatible completion call; neither is evidence that the provider follows the prompt (SRC-1, `agent/sdk/merchantbench_tool_client.py`, `env/web/routes_agent.py`, `env/tools/observation.py`, `agent/baselines/react_160k_compact_30k.py`).

The model proposes store operations. The client does not implement those function bodies: it serializes assistant tool calls into `/act`. The server distinguishes environment calls requiring execution from native/historical calls recorded for continuity. Under the environment lock it checks liveness, optional step header, hook state, quota, tool grants and arguments, then invokes registered Python handlers. Results re-enter baseline history as tool messages. Listing, delisting and repricing change the simulated store, not MerchantBench source code. Admission is software-controlled after the model proposes an action, without a human approving each action. The control route and its limits are [RT-RTE-act-gate](#rt-rte-act-gate) (SRC-1, `env/web/routes_agent.py`, `env/tools/dispatch.py`, `env/tools/tools.py`).

`end_of_step` marks that agent done; multi-agent HTTP completion releases the hook only once the active live agents are done. The worker can also time out. Missing tool calls, provider errors or exhausted hop budgets cause the baseline to attempt a synthetic end-of-step request rather than wait forever for another model answer. Once the hook closes, the simulator persists trace/idempotency artifacts, marks the durable hook closed, reloads listings, writes delta snapshots and periodic checkpoints, finalizes clock/cost state and clears turn buffers. At the operating horizon or store termination, draining resolves outstanding orders without reopening the ordinary agent loop. HTTP 410 ends the baseline. The hosted evaluator then extracts final merchant metrics, including net assets (SRC-1, `agent/baselines/react_160k_compact_30k.py`, `env/core/simulator.py`, `env/web/run_worker.py`, `eval/scoring.py`).

### Forcing cases and scope of guarantees

Three forcing cases challenge stronger readings of this loop.

1. **A model requests an unadvertised denied tool.** Schema omission alone would not enforce denial. `/act` also supplies the denylist to dispatch; dispatch rejects denied names and validates arguments before handler invocation. A direct HTTP client therefore does not gain a denied environment tool just by fabricating its name. However, a Python caller invoking a handler directly is outside this HTTP enforcement point, and an external agent's native tools are not intercepted. The capability surface is the registry; the current grant set is the scenario-filtered subset; neither describes process isolation. See [RT-CLM-http-controls](#rt-clm-http-controls).
2. **An action arrives late or is replayed.** The SDK sends `X-Agent-Step`; the server checks it twice, including under lock. But the header is optional, so stale-observation rejection is not universal across arbitrary HTTP clients. Mutating calls receive an agent/step/call-ID cache key with an argument fingerprint. Same-key/same-fingerprint replay can return a cached result; a conflicting fingerprint produces 409. Fresh call IDs and later steps are distinct operations. This is not a blanket exactly-once guarantee across arbitrary crashes or direct handler calls (SRC-1, `agent/sdk/merchantbench_tool_client.py`, `env/web/routes_agent.py`, `env/core/simulator.py`).
3. **Work occurs outside the environment executor.** Hermes is launched as a subprocess using an external adapter and a run-local profile; hosted evaluation launches a submitter's container. Native tools, shell work or internal callbacks in those agents do not pass through MerchantBench dispatch. `/act` records non-environment origins without executing them. Local subprocess launch inherits host environment and is not a sandbox. Hosted Docker separation and bearer tokens are a different envelope, not a property of every run. See [RT-RTE-hermes-launch](#rt-rte-hermes-launch) and [RT-RTE-hosted-eval](#rt-rte-hosted-eval).

Authorization is owned by Flask's before-request hook. When enabled, an admin token bypasses route restrictions; per-agent tokens permit only designated agent endpoints and matching identities. When disabled, the hook returns without checking a token. Hosted evaluation enables tokens and keeps the admin token on the harness side. The guarantee is a conditional HTTP protocol boundary requiring correct configuration, token secrecy and trusted environment server/Docker host. It is not a guarantee about native tool behavior, remote provider processing or production deployment (SRC-1, `env/web/auth.py`, `env/web/app.py`, `eval/run_eval.py`).

Recovery is likewise scoped. Persisted simulator state can be rehydrated from SQLite/scenario/listings and reconstructed ratings; pending transition/hook markers avoid simply repeating the whole committed transition. Successful mutation results are persisted in the idempotency cache before return. These are implementation recovery mechanisms, not demonstrated crash-consistency outcomes. Database and filesystem writes are distinct operations, and ReAct's Python history is not restored by simulator rehydration. The baseline retries selected provider failures, specially redacts the last tool turn on one Forbidden retry, trims history, and discards a newly accumulated decision turn after HTTP 425. These changes affect subsequent model input but establish neither recovery of every lost action nor correctness of the next decision (SRC-1, `env/web/runner.py`, `env/core/simulator.py`, `agent/baselines/react_160k_compact_30k.py`).

### Alternate clients, context and change admission

[RT-RTE-other-clients](#rt-rte-other-clients) covers deterministic and human clients plus manual stepping. Their decision policy differs while environment effects converge on the same server route. The browser has additional local restrictions, such as reserving a turn for end-of-step and requiring minimum step residence. Those are not server invariants. Batch execution supplies scenario, seed, bootstrap framework and model in run-creation requests, then polls completion; it is not an automatic agent-code improvement process (SRC-1, `env/web/templates/_human_playground_script.html`, `agent/baselines/auto_seed.py`, `scripts/run_batch.py`).

The ReAct context-control route is [RT-RTE-context-trim](#rt-rte-context-trim). It removes old turns rather than generating a summary. With memory writes available, it first asks the foreground model to save important details; that request is not a mandatory successful save. Without the tool it trims immediately. Runtime declares this trigger and continuation path; detailed memory-document revisions and consumers are left to the memory analyst. Hermes profile initialization copies externally supplied skills and sets compression configuration, but the external runtime's later selection, admission and skill evolution cannot be inferred from that copy or from a reported `skills_evolutions` metric. The distributed-parametric provider component is [RT-CMP-openai-model](#rt-cmp-openai-model); no pin or local parameter update is enforced on this inspected baseline path.

## Shared records

### Components

#### RT-CMP-openai-model
Label: OpenAI-compatible model endpoint

The baseline's `self.openai` and `self.model` identify a remote completion service. Its operative representation is distributed-parametric; provider-side weight/storage substrate and provenance are uninspected. Configuration uses `OPENAI_API_KEY`, `OPENAI_BASE_URL` and `MODEL_NAME` (default `qwen3.5-27b`), with a 120-second client timeout. Requests send messages and tool schemas, not a local model file (SRC-1, `agent/baselines/react_160k_compact_30k.py`).

Parameters changing during operation: no baseline-side parameter update is wired in the inspected completion route; provider-side changes are uninspected. Exact version pinned: no immutable model revision is required by the baseline. Mutable endpoint resolving to another model: possible; the caller supplies a URL/model string without a weight digest or immutable provider revision check. External Hermes may have additional model clients; their internals are not frozen.

> model = os.environ.get("MODEL_NAME", "qwen3.5-27b")
> --- `agent/baselines/react_160k_compact_30k.py`

### Operative objects

#### RT-OBJ-system-brief
Label: Scenario-derived system brief

`compose_system_brief` combines shipped role/goals and scenario rules into natural-language English or Chinese guidance, with structured metadata alongside it. The text is computed in server memory, transmitted in the first brief packet and retained as the baseline's Python `system_prompt`; observation logging also records it as a system message. The natural-language text is interpreted by the model, while symbolic scenario values separately govern simulator/handler behavior. Those are distinct consumers: prompt delivery does not enforce a platform rule (SRC-1, `env/tools/observation.py`, `env/web/routes_agent.py`, `agent/baselines/react_160k_compact_30k.py`).

> base_prompt = brief.get("system_prompt", "") or ""
> self.system_prompt = base_prompt
> --- `agent/baselines/react_160k_compact_30k.py`

#### RT-OBJ-tool-registry
Label: Environment tool registry and grants

`REGISTRY`/`_BY_NAME` hold symbolic Python ToolSpec objects linking fixed names, JSON parameter schemas and callable handlers. The SDK receives serialized schemas, not callable code; Python server memory holds the executable bindings. `all_specs` filters grants using the scenario denylist. `append` supports import-time registration of observation tools and ignores duplicate names; this is an extension API for Python code, not a model-exposed code installation tool (SRC-1, `env/tools/registry.py`, `env/tools/observation.py`, `env/web/routes_agent.py`).

> if spec.name in _BY_NAME:
>     return
> REGISTRY.append(spec)
> _BY_NAME[spec.name] = spec
> --- `env/tools/registry.py`

### Routes

#### RT-RTE-react-loop
Label: ReAct observation to store action loop

The principal is a registered agent identified by run ID/agent ID, driven by the baseline process and its remote model. Worker code owns simulation steps; model judgment selects tools; the client and server own progression/validation. Context is [RT-OBJ-system-brief](#rt-obj-system-brief), rendered observation, retained local history and [RT-OBJ-tool-registry](#rt-obj-tool-registry) schemas, consumed by [RT-CMP-openai-model](#rt-cmp-openai-model). OpenAI-format tool calls return through the SDK to [RT-RTE-act-gate](#rt-rte-act-gate). Source: SRC-1, `agent/baselines/react_160k_compact_30k.py`, `agent/sdk/merchantbench_tool_client.py`, `env/web/routes_agent.py`, `env/core/simulator.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Completion produces assistant text/tool proposals; `/act` returns tool results, turn index and step/hook completion flags.
- Later read-back: Tool results and retained assistant text reach later model invocations through Python history; compaction can remove them. Simulator state reaches later observations. Explicit document persistence is a separate tool capability.
- Delegated visibility: The provider receives selected history and schemas; it does not receive server Python objects. No sub-agent delegation is implemented by this baseline route.
- Selection predicate: Code observes an open hook and iterates up to max_hops_per_step; model chooses function names/arguments. HTTP 410 or max_steps terminates the client.
- Invalidation or expiry: End-of-step, timeout, death or terminal phase ends a decision window; HTTP 425 discards this turn's accumulated history, and context trimming removes old messages.
- Activation or effect: Validated handlers can mutate store state and release the hook. Semantic compliance with goals and improved decisions remain unobserved.
- Evidence limits: Source wiring only; no provider behavior, run trace or benefit evidence. Server recovery does not restore the baseline's lost in-process history.

Operating mode: bounded store benchmark under scenario/seed/horizon; model chooses actions within that task rather than executing a supplied expected action sequence. Proposer: model; admission/veto: server handlers; human contribution: launch/configuration, not per-action approval. Answer oracle: no expected-action oracle in this loop; simulator outcomes are feedback and hosted scoring evaluates final wealth rather than matching a correct answer.

> return self.openai.chat.completions.create(**request)
> --- `agent/baselines/react_160k_compact_30k.py`

> self._force_end_of_step("[fallback] hop budget exhausted — release hook")
> --- `agent/baselines/react_160k_compact_30k.py`

#### RT-RTE-act-gate
Label: HTTP environment action admission

Endpoints are agent `/act` and registered Python handlers. Owner: Flask route and dispatch, under the environment lock. The route normalizes messages/tool origins, executes only outstanding environment-origin calls, validates grants/schema and supplies agent identity. Handler effects include database-backed listings and agent-local document writes; trace-only native calls are not executed by this server. Source: SRC-1, `env/web/routes_agent.py`, `env/tools/dispatch.py`, `env/tools/tools.py`, `env/core/simulator.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON tool-result content or HTTP/protocol errors; a turn may contain multiple sequential tool results.
- Later read-back: Successful store mutations influence subsequent observations/simulation; recorded traces and cached successful mutation results support inspection/replay. Memory tools can separately write/read a run-local Markdown document.
- Delegated visibility: Handler receives environment/agent identity and selected arguments; native tool messages are logged without invoking native executors.
- Selection predicate: Environment-origin call lacking a later supplied historical result; agent alive, matching step if declared, hook open unless pure EOS, quota available, tool allowed, arguments valid.
- Invalidation or expiry: Hook closure invalidates ordinary actions; cache scope is agent/step/call ID within the per-run cache. New IDs do not deduplicate previous decisions.
- Activation or effect: Code-enforced mutations and step completion are wired; no evidence of actual calls or downstream model reliance is supplied.
- Evidence limits: No universal shell/native-tool interception, no mandatory step header, no whole-batch rollback and no demonstrated exactly-once crash behavior.

Admission trigger: an HTTP action proposes named tool arguments. The client/model, deterministic policy or human supplies content; dispatch and handlers decide acceptance. A human need not approve each change. Listing handlers can reject unknown/unavailable products, invalid prices or capacity violations. Batches report per-item outcomes, so overall failure need not undo successful items. Guidance shaping a model proposal is the scenario brief, observations and history; deterministic/human policies differ. Store mutations persist for later transitions and can be changed through later repricing/delisting; this is not generic transactional rollback. Memory overwrite accepts string content up to 256 KiB and appends history after writing; the runtime gate does not validate the truth or usefulness of that content. Detailed retained-memory interpretation is reserved for the memory report. No evidence here establishes product-code or production-machinery self-modification. Operating mode/oracle: benchmark task, software validity checks rather than a correct-action oracle.

> if denylist and tool_name in denylist:
>     return {"ok": False, "error": f"tool '{tool_name}' is not available in this scenario"}
> --- `env/tools/dispatch.py`

> declared = request.headers.get("X-Agent-Step")
> if declared is None:
>     return None
> --- `env/web/routes_agent.py`

> if origin == ENV_TOOL_ORIGIN and not has_recorded_result:
>     env_tool_calls.append((message_idx, tc))
> --- `env/web/routes_agent.py`

#### RT-RTE-context-trim
Label: ReAct context maintenance and continuation

Owner: foreground client code, not an independent summarizer. Threshold uses last reported prompt tokens or a character-based history estimate. Input is local history; output is a recent-message suffix plus notice/reminder. `_build_llm_messages` also trims history for each request and sanitizes tool-call argument JSON. Source: SRC-1, `agent/baselines/react_160k_compact_30k.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Local history is trimmed immediately if write_memory_doc is unavailable; otherwise a reminder is appended before the next model call and pending compaction runs after successful `/act`.
- Later read-back: Kept history and notice/reminder reach later calls. A document save is merely requested; any later read depends on use of the read tool, not automatic reinjection by this baseline.
- Delegated visibility: Same foreground provider receives the maintained context; no isolated sub-agent frame or summary-model call occurs in this branch.
- Selection predicate: Configured trigger threshold reached, no pending compaction, then availability of write_memory_doc determines reminder versus immediate trim.
- Invalidation or expiry: Old turns are dropped from local context; leading orphan tool messages are removed from the retained suffix. Existing external document state is not deleted by trimming.
- Activation or effect: Code changes the next request's context. A useful save or preservation of important facts is not established by the reminder.
- Evidence limits: Token sizes are estimates; the trimming routine admits at least one message, so it is not a hard provider-token bound. No run confirms semantic retention.

This is removal from accumulated context, not creation of a distinct task frame. The suffix remains by value; a tool can bring document text back, but removed turns are not automatically dereferenced like pointers. Admission of optional retained content is decided by the foreground model proposing a write and the handler accepting its size/type, with no semantic reviewer or compulsory save. Trigger/guidance says to save important details before trimming; overwrite/history persist if invoked. Rejection/recovery are the write handler's size rejection and later replacement, not an automatic restoration of discarded history. No formulated theory, content-directed criticism or learning result is established by this context-maintenance mechanism.

> "Call write_memory_doc now if important details should be kept."
> --- `agent/baselines/react_160k_compact_30k.py`

> while kept and kept[0].get("role") == "tool":
>     kept.pop(0)
> return kept
> --- `agent/baselines/react_160k_compact_30k.py`

#### RT-RTE-other-clients
Label: Deterministic human and manual drivers

The rule-based/auto-seed client builds assistant-format tool calls without a model, and the human browser builds them from interface operations. Both call the same `/act` endpoint. Dashboard `step`/`auto_step` instead control simulation progression through the registry, converging on `env.step` with a hook blocker; they are not model actions. Source: SRC-1, `agent/baselines/rule_based.py`, `agent/baselines/auto_seed.py`, `env/web/templates/_human_playground_script.html`, `env/web/routes_dashboard.py`, `env/web/runner.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Parsed tool results to the deterministic client, UI result rendering to the human, or step payloads to manual-control callers.
- Later read-back: Store mutations feed future observations; client/UI state persists only as implemented in each process, not as a shared model history.
- Delegated visibility: No remote model call is needed for these action proposals; the HTTP server receives assistant-shaped messages regardless of the originating decision maker.
- Selection predicate: Rule-based CLI selects daily_report or random sourcing mode and seed; human chooses interface operations; manual caller chooses step count.
- Invalidation or expiry: Server hook/quota controls remain applicable to `/act`; UI imposes additional local busy, minimum-duration and reserved-turn restrictions.
- Activation or effect: Same environment handlers can act on deterministic or human proposals; manual progression may end by EOS or timeout.
- Evidence limits: Source confirms alternate decision owners, not their performance or deployment usage. UI-only restrictions do not bind arbitrary clients.

Proposer/decider: deterministic code or human, with server validity veto for tool actions; manual-control caller directs progression. Operating mode: same bounded store task, not an improvement curriculum. Answer oracle: no expected correct decision; deterministic heuristics and visible environment outcomes are not answer keys. Action admission and persistence follow [RT-RTE-act-gate](#rt-rte-act-gate), not a separate approval system.

> resp = self.client.act(assistant_msg, token_usage=token_usage)
> --- `agent/baselines/auto_seed.py`

> const response = await fetch(PLAYGROUND_CONFIG.actUrl, {
> --- `env/web/templates/_human_playground_script.html`

#### RT-RTE-hermes-launch
Label: External Hermes profile and subprocess launch

MerchantBench's registry discovers an installed external adapter, prepares run-local home/workspace/configuration and starts it with run/agent identities and a 30-hop launch budget. The initial profile copies external skills. Consumer and executor beyond that boundary are not frozen. Source: SRC-1, `env/web/runner.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Launcher tracks a subprocess and logs; setup failures are logged and return without launching.
- Later read-back: Existing run-local home is reused with configuration rewritten; what external Hermes actually loads or retains is uninspected.
- Delegated visibility: Child inherits parent environment plus SDK path, agent token, HERMES_HOME and TERMINAL_CWD. MerchantBench can inspect external-format traces but does not define native execution semantics.
- Selection predicate: Hermes bootstrap selected, adapter module found, and no live bootstrap process already registered for the run.
- Invalidation or expiry: Existing live process prevents duplicate launch; temporary profile is removed on setup failure. Existing home skips initial skill recopy.
- Activation or effect: Profile/configuration creation and process launch are wired; actual skill use, compression and evolution remain unobserved and externally implemented.
- Evidence limits: Copied directory names and runtime-health counters do not establish capability activation, isolation, learning or a content-admission policy inside Hermes.

Admission mechanism: at first profile creation, software copies the installed skills directory; no per-skill semantic approval or comparison gate appears in this setup. It writes context/compression configuration, explicitly requesting auxiliary compression provider `auto` and removing separate endpoint/model credentials from that configuration. The registry determines setup and can reject malformed profile config; operator-installed external files supply the initial content. Preparation persists a run-local home/manifest; temporary-directory cleanup handles setup failure, not reversal of an external agent's later changes. This route establishes admission of initial capability material to a launch profile, not model-authored capability improvement. Operating mode: bounded benchmark adapter launch; no answer oracle used in profile selection.

> if os.path.exists(paths["home"]):
>     self._write_hermes_profile_config(paths["home"])
>     return paths
> --- `env/web/runner.py`

> shutil.copytree(
>     skills_source,
>     skills_target,
>     ignore=self._hermes_copy_ignore,
> )
> --- `env/web/runner.py`

> env["HERMES_HOME"] = profile_paths["home"]
> env["TERMINAL_CWD"] = profile_paths["workspace"]
> --- `env/web/runner.py`

#### RT-RTE-hosted-eval
Label: Hosted container evaluation and scoring

The host harness pins scenario seed, requires locally available images, creates a Docker bridge, starts an authenticated environment and a separate agent container, waits for terminal status, fetches merchant-section state and computes result metrics. The agent receives an agent token/model credentials, while the harness retains the admin token. Source: SRC-1, `eval/run_eval.py`, `eval/scoring.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Evaluation result includes image/scenario/seed/run/agent identity, terminal status, wealth/profit/rating/survival metrics and agent log tail; main writes result JSON.
- Later read-back: Result artifacts can be consumed by operators; this harness does not feed a selected successor policy back into the agent.
- Delegated visibility: Agent container receives environment URL and scoped token; environment may receive private data mount. Docker host/provider remain external contracts.
- Selection predicate: Operator supplies images/scenario/seed; images must exist locally. Completion poll or timeout controls termination.
- Invalidation or expiry: Finally block stops/removes containers and network unless keep_containers is set; timeouts fail rather than report a completed successful run.
- Activation or effect: Starts benchmark processes and extracts final wealth; no execution or result from this route was supplied.
- Evidence limits: Bridge/container separation is not demonstrated adversarial isolation. No network-egress prohibition or provider safety guarantee follows from this setup; arbitrary submitter internals are uninspected.

Decision roles: operator chooses the candidate image; deterministic code calculates scores; no model or human selects improved successors here. Operating mode: bounded seeded benchmark. Answer oracle: simulated terminal outcome supplied by the environment, not a correct-action reference. Score uses the last net_assets series value, falling back to current cash components if absent. This can return a metric even on early failure; terminal status and n_steps must accompany interpretation. The evaluator does not constitute evidence of agent learning or efficacy merely because it can calculate a score.

> "score": round(float(net), 2),
> "final_net_assets": round(float(net), 2),
> --- `eval/scoring.py`

### Claims

#### RT-CLM-http-controls
Label: Conditional HTTP enforcement boundary

Claimed operation: optional hosted bearer authorization, scenario tool denial, schema validation and mutation replay support are executable controls, but their owners and coverage differ. Authorization owner is the app hook; tool/grant owner is `/act`/dispatch; replay owner is simulator cache. Guarantee strength: protocol. Covered paths: HTTP requests passing those enforcement points; alternate paths are host Python calls, subprocess/native execution, provider internals and administrator override. Required external contract: trusted server/host, correct token configuration and secret handling. Sources: SRC-1, `env/web/auth.py`, `env/web/app.py`, `env/tools/dispatch.py`, `env/web/routes_agent.py`, `env/core/simulator.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not require_tokens:
>     return None
> --- `env/web/auth.py`

Replay strength is limited to the implemented key/cache boundary, not a universal invariant. The simulator documents persistence before acknowledgement, and the code calls persist_idem after successful mutation. That sequence is not execution evidence of atomicity across all filesystem/database failures.

> Successful mutations are persisted before their result is returned.
> --- `env/core/simulator.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-brief-guidance
Label: Brief to foreground model guidance

Consumer: remote foreground completion model. Channel: system message or Claude-specific provider system payload, alongside observations/history. Force: natural-language instruction interpreted by the model, not a server permission grant. Horizon: later calls in the same baseline process after first brief receipt. Source: SRC-1, `agent/baselines/react_160k_compact_30k.py`, `env/tools/observation.py`. Model compliance and persistence through client restart remain unobserved.

> if system_prompt and not exclude_system:
>     messages.append({"role": "system", "content": system_prompt})
> --- `agent/baselines/react_160k_compact_30k.py`

#### RT-BAP-handler-binding
Label: Registry to executable environment handler

Consumer: dispatch. Channel: symbolic tool name lookup and callable binding. Force: accepted calls invoke Python with server-selected environment/agent identity after validation; model-supplied names do not install executable code. Horizon: the server process/run grant configuration; mutations can outlast the individual call in database/files. Source: SRC-1, `env/tools/dispatch.py`, `env/tools/registry.py`. Direct host code has authority outside this gate.

> if "agent_id" in params:
>     result = handler(env, agent_id, **kwargs)
> else:
>     result = handler(env, **kwargs)
> --- `env/tools/dispatch.py`

## Annotations

none
