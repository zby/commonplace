---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "LACP runtime baseline: native model/tool execution, host wrappers, sandbox gates, orchestration and change admission at e31f134b689afd6a71d94b0420682d1f528d6fa1."
run-id: AAS-2026-10-14-lacp-91efd16f7a35-01
reviewed-boundary: e31f134b689afd6a71d94b0420682d1f528d6fa1
---

# LACP runtime report

## Runtime account

LACP has two materially different execution owners. Its native REPL owns a provider conversation and dispatches model-selected tools. Its wrappers configure or gate the launch of another coding-agent host; that host owns its subsequent model/tool loop. The [boundary](boundary.md#boundary-and-evidence) includes both. SRC-1 supplies implementation and doctrine/design evidence, not an observed invocation. All operation, activation and benefit conclusions below remain uninspected.

### Ordinary invocation: native REPL

A no-argument `lacp` launches `tui/repl.py`; `--model` is another direct REPL entry (SRC-1, `bin/lacp`). A user enters task text. The input handler appends a user message and starts a background streaming worker. The default `sonnet` alias resolves to Anthropic `claude-sonnet-4-6`, not an external Claude CLI. The REPL constructs a system prompt from identity, a selected focus section capped at 200 characters, Git branch and working directory. Its title says “identity + focus + memory,” but this function does not inject the keyed memory store. Memory tools are a separate demand-driven interface (SRC-1, `tui/repl.py`, `tui/providers.py`, `tui/tools.py`). See [RT-RTE-native-turn](#rt-rte-native-turn), [RT-CMP-anthropic-provider](#rt-cmp-anthropic-provider) and [RT-BAP-mode-prompt](#rt-bap-mode-prompt).

The worker combines registered built-in definitions with live MCP definitions. Only an Anthropic provider receives this tool list at the REPL call site. The API receives conversation messages, the constructed system prompt, model identifier and an 8192-token output cap. Text is streamed to the UI; tool events become pending calls. Calls execute serially in the local worker, without a central approval callback. Built-in calls dispatch through the registry; names beginning `mcp_` dispatch to the MCP manager. Tool identifiers connect tool-use blocks to results, whose content is capped at 50,000 characters before the next model invocation. The next-step policy is thus distributed: the model proposes the tool/name/input; code chooses the executor and continues the conversation. A text-only turn appends the assistant response, saves JSONL and terminates. Twenty iterations bound the worker loop, not total cost or subprocess effects (SRC-1, `tui/repl.py`, `tui/providers.py`).

Native shell, write and edit handlers act with the Python process's OS privileges and current directory. Bash uses `shell=True` and a substring blacklist; write checks selected textual system-directory prefixes; edit has no corresponding prefix check. Neither a shell timeout nor output truncation is isolation. The current installed grant set consists of registry tools plus tools advertised by successfully started configured MCP servers; the repository does not supply a deployed server list or OS isolation envelope. PLAN, THINKING and YOLO change prompt text, not the executor's gate. This distinction is consequential: a normal or plan-mode prompt cannot make the dispatch route enforce approval (SRC-1, `tui/tools.py`, `tui/repl.py`; [RT-CLM-control-scope](#rt-clm-control-scope)).

Errors produce text/JSON error results. Rate/auth/quota errors can refresh credentials, retry with 5/10/20-second backoff and switch to Haiku after three retries. This is model substitution, not proof of equivalent task behavior. The 20-turn exhaustion path has no separate terminal-result or save block in the inspected loop. Saving occurs on a no-tool turn and on quit; this does not establish crash-safe durability. `/resume` replaces the current conversation with loaded JSONL messages and session identity, but does not restore provider/model from the metadata in that command. Working context is bounded at supply points by focus, skill and tool-result truncation, and removable wholesale by `/clear`; the inspected streaming loop otherwise accumulates messages rather than compacting them. The session module's size constant does not implement compaction (SRC-1, `tui/repl.py`, `tui/sessions.py`, `tui/tools.py`).

### Host launch, policy gate and coordination

Adoption installs shims for Claude/Codex by default, with Hermes/Grok opt-in. A managed shim launches `lacp run`, declares an interactive task and defaults repository trust to trusted; `LACP_BYPASS=1` launches the native binary instead. `lacp-stream` is a different entry: it resolves a host, maps flags, optionally applies hook profiles, sets context-mode/evaluation environment and directly execs the selected CLI. It does not itself invoke the sandbox gate. Therefore entry-point equivalence is false even before considering provider-native work ([RT-RTE-host-launch](#rt-rte-host-launch); SRC-1, `bin/lacp-adopt-local`, `bin/lacp-stream`). Host prompt/history/tool semantics remain external contracts, not LACP-native guarantees.

`lacp run` dispatches to `lacp-sandbox-run`. Routing uses task keywords and caller flags for trust, internet, external code, sensitive data, compute and duration. Gates validate selected input/context contracts, optional session fingerprint, critical confirmation, estimated budget and review approval TTL. They then select trusted-local direct execution, a local runner or a remote runner. No configured local runner means direct fallback, despite the `local_sandbox` route label. External remote execution is default-disabled in the shared library and requires explicit permission; Daytona/E2B are adapters to dependencies. Gate records retain decisions and execution exit status under the knowledge root (SRC-1, `bin/lacp`, `bin/lacp-route`, `bin/lacp-sandbox-run`, `scripts/lacp-lib.sh`; [RT-RTE-sandbox-launch](#rt-rte-sandbox-launch)).

This is a prelaunch policy, not a complete monitor of the launched host. Context detection looks at the command's first executable and selected arguments. A shell-wrapped mutating command is not classified from its body by `command_is_mutating`. Orchestration passes the runner executable to the gate while keeping the actual command in environment. The reviewed gate also uses an `elif` chain: an over-budget estimate with `--confirm-budget true` enters the budget branch, leaves the execution code at zero, and does not subsequently test review TTL. This is a static forcing case against a universal review-approval guarantee, not an observed exploit (SRC-1, `bin/lacp-sandbox-run`).

Orchestration selects tmux, dmux or Claude worktree runner, forwards routing arguments, and uses a runtime-pressure check. tmux starts a detached session; its launch success is not task completion. Optional result collection changes later visibility. dmux and Claude-worktree use configurable shell templates; their real behavior depends on those trusted templates and hosts. Swarm launch produces a batch and invokes orchestration; the command help's “all gates remain active” means traversal of the launch gate, not guaranteed isolation of every descendant effect. The workflow command is a separate durable state machine: ordered roles, a planner-issued token for developer, and verifier/tester/reviewer decisions. Caller-supplied role strings and an optional `--allow-unplanned` override do not authenticate principals or prove that work was performed. These routes coordinate different things rather than composing automatically into one execution loop (SRC-1, `bin/lacp-orchestrate`, `scripts/runners/tmux-runner.sh`, `scripts/runners/dmux-runner.sh`, `scripts/runners/claude-worktree-runner.sh`, `bin/lacp-swarm`, `bin/lacp-workflow-run`; [RT-RTE-orchestrated-run](#rt-rte-orchestrated-run), [RT-RTE-workflow-advance](#rt-rte-workflow-advance)).

The harness adds actual runner completion checks: each task attempt calls the sandbox gate, runs verification after runner success, and writes hashed attempt receipts. Runner stdout/stderr are tails, not complete evidence. The inspected searches show dependency/input checks, profile-dependent retries, stronger-model retry labels and quality verification. This supports a bounded evidence-producing execution route, not proof that its verification commands are an independent correctness oracle (SRC-1, `bin/lacp-harness-run`; [RT-RTE-harness-attempt](#rt-rte-harness-attempt)).

### Forcing cases and guarantee envelope

Four source-level challenges constrain the claimed execution contract:

1. **Native tool execution versus wrapper approval:** REPL calls the registry/MCP manager directly. PLAN is a request to the model, not an executor check. This defeats a system-wide mandatory-approval interpretation.
2. **`local_sandbox` with no runner:** the gate deliberately executes directly. Routing is not a deployed isolation guarantee.
3. **Review route with over-budget override:** the budget `elif` suppresses the later review-TTL branch. A configured review policy is not unconditional enforcement in that gate.
4. **Delegation/provider-native subprocess:** native delegation sets `LACP_BYPASS=1`; OpenAI OAuth delegates the last user string to Codex with the same bypass. It changes both the control path and model-visible context.

Each case is grounded in the route records below. No target command or test was executed. Equivalent alternatives inspected include Anthropic API/tool calls, OpenAI direct SDK and OAuth CLI paths, registry file/shell execution, MCP subprocesses, installed wrappers and bypasses, stream launches, orchestration runners and manual workflow control. Hermes/Ollama provider internals, remote-service isolation, every harness policy variant and all maintenance/admission families are not exhaustively traced here; their source remains available. This prevents universal claims about all configured providers, scheduler reliability or end-to-end task quality. Memory store revisions and the full learning-event/brain lifecycle are left to the memory member, not declared absent.

| Guarantee or contract | Owner and enforcement point | Strength and covered paths | Alternate paths / required external contract | Implementation conclusion status | Operation conclusion status |
|---|---|---|---|---|---|
| Risk/contract/budget launch checks | LACP shell gate before execution | policy; only callers traversing the active checks | Native REPL, stream, native binary and recursion guard bypass; caller flags and trusted policy/state must be truthful and protected | wired | uninspected |
| Local isolation | Configured runner/OS, not route name | no claimed guarantee for direct fallback | Actual runner implementation and deployed OS privileges required; no local runner supplied by this report | afforded | uninspected |
| Host pre-tool blocking | Host invokes installed `pretool_guard.py` and honors exit 2 | best effort; configured Bash and Write/Edit events | Other tool channels, encoded shell operations, native REPL and disabled profiles differ; external host hook contract required | wired | uninspected |
| Stop quality check | Host Stop hook plus LACP heuristic/test/Ollama code | best effort; non-skipped evaluated attempts | Fast path, loop guard, circuit breaker, unavailable evaluator and Ralph cooperation; host must honor emitted hook protocol | wired | uninspected |
| Ordered workflow/token | Workflow command's state transition code | protocol; writes through `advance` | Direct state writes, supplied actor names and `allow-unplanned`; trusted filesystem required | wired | uninspected |

The host pre-tool guard itself labels exfiltration matching as bypassable and not a security boundary. Its optional Ollama classifier fails open. Stop quality evaluation is likewise selective: trivial/loop/circuit cases return early, heuristic fast path skips tests/evaluation, unavailable Ollama allows, and Ralph cooperation can turn a block into feedback. The plugin's pre-tool and stop scripts have identical SHA-256 values to root copies at this commit, but the session-start copies differ; no general plugin parity is inferred (SRC-1, `hooks/pretool_guard.py`, `hooks/stop_quality_gate.py`, `plugin/hooks/hooks.json`, `plugin/hooks/scripts/pretool_guard.py`, `plugin/hooks/scripts/stop_quality_gate.py`, `plugin/hooks/scripts/session_start.py`; [RT-RTE-host-hook](#rt-rte-host-hook)).

### Change admission and model mutability

The native model can propose and immediately admit file edits through built-in handlers. The shell can modify product files and invoke additional programs. Installed skills are read as text and returned to the model; MCP tool schemas are dynamically discovered and added to its capability surface. Their admission rests on filesystem/configuration control and interpretation, not a separate signed extension sandbox (SRC-1, `tui/tools.py`, `tui/mcp.py`; [RT-RTE-extension-load](#rt-rte-extension-load)).

The idle improvement driver is more specific: a user enables it or starts an experiment; idle time triggers a background host agent; a natural-language program proposes small TUI changes; a health score decides keep/discard. It requests commits and reverts `tui/` on a reduced score. The code does not enforce the prompt's edit scope, line limit or protected auth area. It does not check the delegated subprocess return code before score selection. Failed metrics return zero, so two failures can satisfy `new_score >= baseline_score`. Checkout does not undo a committed experiment, and branch creation/main switching return codes are not verified. The route retains logs/results and changed source but does not hot-reload already imported Python code. Thus it is an implemented improvement-directed self-change pathway with incomplete recovery and no exercised-benefit evidence, not demonstrated autonomous improvement ([RT-RTE-idle-experiment](#rt-rte-idle-experiment); SRC-1, `tui/idle_agent.py`, `config/autoresearch-program.md`, `tui/autoresearch_metrics.py`).

Cross-CLI learning promotion separately aggregates metric, evidence-file, approver-name and provenance checks, writes `promotion-state.json` to enforce mode, and offers rollback to shadow. Two distinct strings are not authenticated human approvals; nonempty evidence is not verification of its conclusion. The implementation warns that the state file is a trusted-write boundary. This report establishes state admission, not downstream enforce-mode activation ([RT-RTE-learning-promotion](#rt-rte-learning-promotion); SRC-1, `bin/lacp-learn-promote`, `bin/lacp-learn-rollback`). Skill-factory lifecycle is an external-script adapter at `~/.agents/skills/auto-skill-factory`; the requested scripts are not furnished by this repository path. Its internal proposal/admission/revalidation rules remain opaque here, while LACP's dispatch is inspectable (SRC-1, `bin/lacp-skill-factory`).

No inspected provider route updates weights. Exact weight revisions are not frozen by model names; provider endpoints can resolve differently, and the foreground user/fallback logic can replace the model. The optional local command classifier is another distributed-parametric component with an environment-selected endpoint/model. Product/prompt changes and retained-state changes are independent of parameter training ([RT-CMP-anthropic-provider](#rt-cmp-anthropic-provider), [RT-CMP-openai-provider](#rt-cmp-openai-provider), [RT-CMP-ollama-classifier](#rt-cmp-ollama-classifier)).

Additional SRC-1 coverage in this member is implementation inspection of native worker, tool handlers, providers, sessions, MCP manager, idle agent and score weights; wrapper generation/stream flag mapping; gate branch and mutation detection; orchestration adapters, workflow transitions and harness attempts; root guard/stop pipeline and plugin event map/copy hashes; promotion gates and skill-factory adapter. The autoresearch program supplies doctrine/design. Source-authored descriptions are not runtime instructions for this analysis.

## Shared records

### Components

#### RT-CMP-anthropic-provider
Label: AnthropicProvider

Source-native Python API adapter in `tui/providers.py`; numerical model state is distributed-parametric at the remote provider, while adapter/request schemas are symbolic Python/dicts on the local filesystem/in memory. The default alias requests `claude-sonnet-4-6`. Parameters changing during operation: uninspected — API service internals are outside SRC-1; no training/update request occurs in the inspected stream method. Exact parameter version pinned: no; a request name is not a frozen weight digest. Mutable endpoint resolution: possible, not independently established for the deployed service. User switching and quota fallback also substitute the requested model. Evidence: SRC-1, `tui/providers.py`, `tui/repl.py`.

> kwargs: dict[str, Any] = {
>     "model": self.model,
>     "max_tokens": 8192,
>     "messages": messages,
> }
> --- `tui/providers.py`

#### RT-CMP-openai-provider
Label: OpenAIProvider

Python adapter has symbolic code/request objects locally; remote numerical state is distributed-parametric and opaque. API-key mode uses OpenAI SDK; ChatGPT OAuth uses a Codex subprocess. Parameters changing during operation: uninspected — neither provider nor Codex internals is frozen; inspected adapter requests generation, not training. Exact parameter revision pinned: no. Mutable endpoint can resolve another model: unresolved externally; `self.model` is caller-selectable. Evidence: SRC-1, `tui/providers.py`.

> # ChatGPT OAuth tokens can't be used with the standard SDK
> # (they require model.request scope which is ChatGPT-internal).
> # Delegate to codex CLI instead.
> --- `tui/providers.py`

#### RT-CMP-ollama-classifier
Label: Optional pre-tool Ollama classifier

Symbolic Python rule selects commands needing review, then natural-language text reaches a distributed-parametric model via HTTP. Model substrate/weights are external to SRC-1. Parameters changing during operation: uninspected; the request supplies inference options, not updates. Exact version pinned: no; default `llama3.1:8b` is an identifier and environment overrides exist. Mutable endpoint resolution is unresolved; URL/model configuration can change between deployments. Consumer returns allow/block from parsed JSON, failing open on errors. Evidence: SRC-1, `hooks/pretool_guard.py`.

> ollama_url = os.getenv("LACP_QUALITY_GATE_URL", "http://localhost:11434/api/chat")
> ollama_model = os.getenv("LACP_QUALITY_GATE_MODEL", "llama3.1:8b")
> --- `hooks/pretool_guard.py`

### Operative objects

#### RT-OBJ-messages
Label: Native REPL messages

Source-native `self.messages` list contains natural-language user/assistant/tool text in symbolic role/type/id envelopes. The operative parts have different consumers: provider interprets text, while code routes role and tool-use identifiers. Storage is RAM during the run and JSONL under `~/.lacp/sessions/repl/` after save. Model input does not include all saved metadata. Evidence: SRC-1, `tui/repl.py`, `tui/sessions.py`.

> # First line: metadata
> f.write(json.dumps({"_meta": meta}) + "\n")
> # Subsequent lines: messages
> for msg in messages:
>     f.write(json.dumps(msg) + "\n")
> --- `tui/sessions.py`

#### RT-OBJ-autoresearch-program
Label: Autoresearch program

Natural-language guidance in `config/autoresearch-program.md`, stored as Markdown on disk and read/reconstructed into every experiment prompt. It states the health objective, TUI scope, small-change constraint, auth protection and score-based acceptance/revert method. Its behavioral force is interpretive, not enforced edit capability restriction. Evidence: SRC-1, `config/autoresearch-program.md`, `tui/idle_agent.py`.

> 1. **Only modify** files in `tui/` directory
> 2. Every change MUST improve or maintain the health score
> 3. Do NOT modify `tui/providers.py` auth code (OAuth is fragile)
> 4. Do NOT add new dependencies
> 5. Keep changes small (< 30 lines diff per experiment)
> 6. Commit each experiment separately with descriptive message
> --- `config/autoresearch-program.md`

### Routes

#### RT-RTE-native-turn
Label: Native model/tool turn

Endpoints: foreground task input → provider → tool executor → provider → displayed assistant response and saved messages. REPL code owns loop continuation; model proposes content/actions. Representation is natural-language task/system/tool-result text plus symbolic event and tool envelopes. Local process owns effects, with per-handler restrictions rather than sandbox delegation. Source: SRC-1, `tui/repl.py`, `tui/providers.py`, `tui/tools.py`, `tui/sessions.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: streamed text, tool progress and terminal no-tool response; errors can be displayed as responses.
- Later read-back: auto-saved messages reload via startup resume or `/resume` and become a later provider's conversation; keyed memory is a separate tool route.
- Delegated visibility: provider receives messages/system and, for Anthropic, definitions; tool handlers receive their input dictionaries, not the whole transcript.
- Selection predicate: ordinary non-slash task text; model selects returned tool names and inputs; code uses registry lookup or `mcp_` prefix; only nonempty tool inputs enter pending calls at the inspected event handler.
- Invalidation or expiry: `/clear` removes current conversation; tool text capped at 50,000 characters; no automatic old-turn eviction in inspected worker.
- Activation or effect: tool dispatch can change files/run shell; delivery of results and saved conversation is wired, but behavioral dependence on that content is unobserved.
- Evidence limits: static source only; empty/invalid tool JSON and 20-turn exhaustion differ from the ordinary successful route; no host or API run supplied.

Decision roles: user supplies open task; model proposes next actions; code checks tool identity and executes; local human approval is not requested by the dispatcher. Answer oracle: none supplied by this generation route; tool exit codes are execution results, not correctness references. Operating mode: open requests, with interpretive mode prompts. Admission: model-selected write/edit or shell operation immediately admits file changes subject to handler checks; executor can reject missing inputs, selected paths, ambiguous edits or dangerous substrings. Recovery: error JSON/timeouts, credential retries/model fallback; no transactional file rollback. Persisted changed source/files can influence later operation if subsequently loaded; such activation is not observed.

> if tool_name.startswith("mcp_") and self.mcp_manager:
>     result = self.mcp_manager.call_tool(tool_name, tool_input)
> else:
>     result = execute_tool(tool_name, tool_input)
> --- `tui/repl.py`

> result = subprocess.run(
>     command,
>     shell=True,
>     capture_output=True,
>     text=True,
>     timeout=timeout,
>     cwd=os.getcwd(),
> )
> --- `tui/tools.py`

#### RT-RTE-host-launch
Label: Host launch and native delegation

Endpoints: adopted CLI shim → sandbox launch → native host, or stream/delegate/provider-OAuth → native host directly. LACP owns launch arguments; host owns model/tool decisions. Identity is CLI name/binary plus task/current directory; `LACP_BYPASS` avoids a managed shim. Source: SRC-1, `bin/lacp-adopt-local`, `bin/lacp-stream`, `tui/tools.py`, `tui/providers.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: stream replaces launcher with host; delegate captures exit code/output; OAuth provider renders Codex output as text.
- Later read-back: uninspected — host session persistence is external; LACP may save returned text in REPL messages, but host internals are not frozen.
- Delegated visibility: explicit task string for built-in delegate; last user string only for OpenAI OAuth, omitting REPL system and preceding turns; stream forwards selected flags/prompt arguments/environment.
- Selection predicate: named or auto-detected installed CLI; native backup preferred by delegation; OAuth selected when credentials are non-API-key tokens.
- Invalidation or expiry: delegate capped at 300-second timeout and truncated output; OAuth subprocess at 120 seconds; host context/expiry uninspected.
- Activation or effect: host runs with local inherited environment/cwd and can exercise its own capabilities; no observed host operation or context compliance.
- Evidence limits: wrappers, stream, delegate and provider paths are not interchangeable; host settings and OS isolation were not supplied.

Scope guarantee: policy at adopted shim's sandbox launch only; bypass/direct paths do not enforce that policy. This route creates a separate host context, resembling a per-task frame: explicit task crosses in and captured output crosses back. It is not heap-style reference sharing, and host durable side effects survive outside the return. OpenAI direct SDK mode instead sends system plus message list to chat completion; the REPL does not supply native tool definitions to that provider.

> env={**os.environ, "LACP_BYPASS": "1"},  # skip LACP wrapper
> --- `tui/tools.py`

> ["codex", "exec", "-m", self.model, last_msg],
> capture_output=True, text=True, timeout=120,
> env={**os.environ, "LACP_BYPASS": "1"},
> --- `tui/providers.py`

#### RT-RTE-sandbox-launch
Label: Routed sandbox launch

Endpoints: command/task/profile → deterministic route/risk → gates → executor/runner → sandbox-run record and status. Owner is LACP shell code; caller proposes command and flags, code decides whether the launch occurs. Representation is symbolic shell arguments, JSON policy/contracts and recorded route; task keywords are matched text. Source: SRC-1, `bin/lacp-route`, `bin/lacp-sandbox-run`, `scripts/lacp-lib.sh`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: command output and exit status, or gate refusal, with optional structured summary.
- Later read-back: records under knowledge-root `data/sandbox-runs`; later runtime use of their contents uninspected in this route.
- Delegated visibility: selected runner receives command after `--` and inherited environment; remote dependency internals uninspected.
- Selection predicate: caller flags/task keywords determine route and risk; non-dry-run checks depend on configuration and command detection.
- Invalidation or expiry: review approval has expiry time; fingerprint binds selected runtime coordinates; confirmation and estimated budget are invocation inputs.
- Activation or effect: code dispatches direct/local/remote execution; dry-run does not execute; deployed containment depends on actual runner/host.
- Evidence limits: first-executable detection does not inspect shell bodies or orchestration environment; budget override branch can skip review TTL; no actual runner isolation tested.

Decision/admission roles: caller supplies task/risk declarations and confirmation booleans; code validates gates; origin/authentication of these values is not a human approval proof. Answer oracle: none; schema/context equality and estimates are preconditions. Operating mode: bounded command launch/dry-run. Recovery is refusal before launch or exit-code recording after launch; no general reversal of command effects. Guarantee owner/enforcement: active gate branches provide a policy at launch, requiring trusted writable policy/approval files and accurate declarations. Covered path is traversal through that gate; direct native calls and the recursion guard are alternatives.

> elif [[ "${RISK_TIER}" == "review" && "${ROUTE}" != "trusted_local" ]]; then
>   APPROVAL_JSON="$(approval_state_json)"
> --- `bin/lacp-sandbox-run`

> if [[ "${CONFIRM_BUDGET}" != "true" ]]; then
>   EXEC_RC=10
>   ERROR_MSG="blocked by budget gate: estimated_cost_usd=${ESTIMATED_COST_USD} exceeds ceiling=${COST_CEILING_USD} for risk_tier=${RISK_TIER}; pass --confirm-budget true to override"
> fi
> --- `bin/lacp-sandbox-run`

> RUNNER_TYPE="direct_fallback"
> log "WARN: LACP_LOCAL_SANDBOX_RUNNER is unset; falling back to direct execution"
> run_direct "${CMD[@]-}" || EXEC_RC=$?
> EXECUTED=1
> --- `bin/lacp-sandbox-run`

#### RT-RTE-orchestrated-run
Label: Orchestration and swarm launch

Endpoints: command/session or batch/swarm manifest → capacity check → sandbox gate → tmux/dmux/Claude-worktree adapter. Caller owns task partitioning; code owns launch progression; host owns task execution. Symbolic JSON manifests/environment select runners; command/prompt text is interpreted by shell or host. Source: SRC-1, `bin/lacp-orchestrate`, `bin/lacp-swarm`, `scripts/runners/tmux-runner.sh`, `scripts/runners/dmux-runner.sh`, `scripts/runners/claude-worktree-runner.sh`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: backend launch result and batch counts; detached tmux success means session started, not task completed.
- Later read-back: swarm launch artifact persists; optional result collector permits completion records; default launch route does not prove result collection.
- Delegated visibility: exported command/session/backend/role hints and prefix reach adapter; host context is separate, not a shared REPL transcript.
- Selection predicate: backend argument/default and manifest jobs; pressure check can refuse; batch continues only under configured continue-on-error policy.
- Invalidation or expiry: source help declares 30-minute reservation locks, but launch enforcement of all reservation variants is uninspected; backend/session termination is host-owned.
- Activation or effect: adapters start sessions or execute rendered templates; actual completion/isolation unobserved.
- Evidence limits: trusted template, environment and backend availability required; gate sees runner path, not all commands/effects; reservation helpers were not fully traced.

Coordination isolates work in separate host contexts/worktrees only to the extent the selected backend implements it. Returned launch records are not model summaries or proof of shared-context consumption. Recovery: batch reports failures; backend missing/template missing fails; no cross-backend transactional rollback established.

> "${ROOT}/bin/lacp-sandbox-run" "${run_args[@]}" -- "${runner}"
> --- `bin/lacp-orchestrate`

> tmux new-session -d -s "${session}" -- "${command_text}"
> --- `scripts/runners/tmux-runner.sh`

#### RT-RTE-workflow-advance
Label: Workflow state advance

Endpoints: initialized `state.json` → caller stage/actor/decision/token → role/order/token checks → persisted transition. Code owns state progression, not performance of developer work. Symbolic JSON state is on disk under knowledge-root workflows; shared context/note text is natural language. Source: SRC-1, `bin/lacp-workflow-run`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: stage/run status and planner token; reject writes blocked state and exits nonzero.
- Later read-back: status/advance reload saved workflow state; token/history govern subsequent transition checks.
- Delegated visibility: inapplicable — command does not launch role agents; external participants must arrange context delivery.
- Selection predicate: current stage must equal requested stage and supplied actor must equal owner-role string; developer token required unless override.
- Invalidation or expiry: rejection blocks the stored stage; no token expiry/authenticated-principal boundary inspected.
- Activation or effect: deterministic status/token/history write; actual task execution and approval quality unobserved.
- Evidence limits: filesystem is trusted-write state; role names authenticate no person/process and order checks constrain only this API.

Admission roles: caller proposes approve/reject and optional note; code admits transition, checks exact role string and token; `--allow-unplanned` deliberately weakens developer token requirement. Human contribution is unresolved, not guaranteed by role labels. Answer oracle: none; decisions are supplied values, not checked against expected task outputs. Operating mode: manually driven staged workflow. Recovery: rejected stage remains current and can be addressed by a later command; no product rollback performed.

> if actor != stage["owner_role"]:
>     raise SystemExit(f"actor role mismatch: expected {stage['owner_role']}, got {actor}")
> --- `bin/lacp-workflow-run`

> if required and not allow_unplanned:
> --- `bin/lacp-workflow-run`

#### RT-RTE-harness-attempt
Label: Harness task attempt and verification

Endpoints: task runner command/profile → gated subprocess → verification checks → attempt JSON/hash receipt. Harness code owns admission to task-success and retry progression; runner/verification commands supply effects and evidence. Symbolic task/policy/receipt data persists on disk; stdout/stderr are text tails. Source: SRC-1, `bin/lacp-harness-run`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: attempt success iff runner status is zero and verification passes; task summary contains attempt outcomes.
- Later read-back: receipt/task-output registry supports subsequent dependency checks and replay artifacts; exact model use of those records is uninspected.
- Delegated visibility: runner gets selected workdir, task/stage environment and configured environment overrides; verification gets workdir.
- Selection predicate: task dependency/input readiness and profile/policy choose execution, retries and verification; verification runs after runner success.
- Invalidation or expiry: failed attempts persist as evidence; profile retry policy limits recurrence; no general output expiry established.
- Activation or effect: runner changes workdir artifacts; verification determines accepted success and receipts; hashes do not establish truth.
- Evidence limits: no task executed; configured verifier commands may share errors with runner and evidence tails omit earlier output.

Admission roles: manifest/runner author proposes task work; code decides success from status and checks, can reject and retry. Human participation is unresolved at per-result level. Answer oracle: verification checks are configured tests/reference constraints, not necessarily expected-answer data; independence and correctness unresolved. Operating mode: bounded task/policy execution rather than an open conversational loop. Recovery: retry/replay affords further attempts; ordinary verification does not undo prior effects.

> ok = run_cp.returncode == 0 and verify_ok
> --- `bin/lacp-harness-run`

> "stdout": run_cp.stdout[-4000:],
> "stderr": run_cp.stderr[-4000:],
> --- `bin/lacp-harness-run`

#### RT-RTE-host-hook
Label: Host guard and stop feedback

Endpoints: configured host events → Python guard/stop pipeline → exit/JSON decision → external host continuation or blocking. Code/optional Ollama decides selected safety/quality checks; host owns enforcement of the returned protocol. Source: SRC-1, `hooks/pretool_guard.py`, `hooks/stop_quality_gate.py`, `bin/lacp-claude-hooks`, `plugin/hooks/hooks.json`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: guard exit 2 on matched block; Stop JSON block reason or allow/systemMessage, sometimes no output on early return.
- Later read-back: Stop writes handoff/SMS before heuristic evaluation and retains circuit/telemetry state; full downstream memory revisions belong to memory analysis.
- Delegated visibility: hook payload carries tool input or session/transcript fields; classifier receives command/cwd rather than assistant persuasion text; host must deliver and honor feedback.
- Selection predicate: configured event matchers, regex/work/heuristic predicates, optional classifier flag, Stop loop/trivial/circuit fast exits.
- Invalidation or expiry: circuit breaker permits termination after repeated blocks; optional classifier unavailable/error allows; hooks can be reconfigured by installation/profile changes.
- Activation or effect: matching commands can be refused and selected stop attempts can request correction; feedback compliance and improved work unobserved.
- Evidence limits: native REPL does not traverse these host events; regex guard is explicitly bypassable; plugin session-start copy differs; actual installed settings unknown.

Diagnosis roles: software selects whether to evaluate; tests supply exit results; Ollama supplies model judgment; host/user can disable configuration. Answer oracle: selected repository tests provide constraints, Ollama judgment alone supplies none. Operating mode: selective post-task evaluation and optional pre-action classification. Guarantee strength is best effort, requiring host event semantics and installed configuration; not a system-wide isolation invariant.

> Returns 0 (allow) or 2 (block). Fail-open on any error.
> --- `hooks/pretool_guard.py`

> # Ollama approved or unavailable — allow
> --- `hooks/stop_quality_gate.py`

#### RT-RTE-extension-load
Label: MCP and skill capability supply

Endpoints: local settings/SKILL files → server initialize/list or skill read → model-visible definitions/text → selected tool invocation. Operator/filesystem controls configuration admission; code discovers available material; model selects use. MCP config/tool schemas are symbolic; skill descriptions/bodies are natural language. Source: SRC-1, `tui/mcp.py`, `tui/tools.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: live tool definitions or skill text, with skill body capped at 10,000 characters; calls return MCP text content/JSON.
- Later read-back: installed config and skill files are reloaded in future sessions/calls; this route does not itself revise their contents.
- Delegated visibility: MCP gets named tool and input dictionary; skill body goes into foreground tool-result context, not a newly isolated context.
- Selection predicate: local settings precede global settings; stdio command required and HTTP-only configs skipped; running servers advertise tools; skill name selects file/fallback.
- Invalidation or expiry: failed/stopped servers excluded from definitions; manager stop terminates processes; source changes affect later reads but no version pinning is established.
- Activation or effect: executable server can act with inherited OS environment; returned skill text requests behavior, not reliable compliance.
- Evidence limits: actual configs/servers/skills external to frozen checkout; no server privileges, per-tool grant restriction or skill-authenticity guarantee established.

Capability admission: trusted configuration supplies server command/args/env and software starts/discovers it; no separate per-tool human approval in this route. Proposer/editor identity is unresolved for installed files. Rejection/recovery: missing or invalid config skipped, launch error returns failure, stop/kill terminates server. Answer oracle: none. Mode: dynamic capability discovery and on-demand instruction loading. The separate skill-factory command dispatches to external lifecycle/revalidation scripts and cannot establish their internal admission rule from SRC-1.

> env = {**os.environ, **server.env}
> --- `tui/mcp.py`

> if skill_file.exists():
>     return skill_file.read_text(encoding="utf-8")[:10000]
> --- `tui/tools.py`

#### RT-RTE-idle-experiment
Label: Idle autoresearch experiment

Endpoints: user enable/start or idle trigger → score baseline → external agent with program → new score → keep/discard → result TSV and source tree. Local thread owns iteration/score selection; delegated host/model proposes edits. Objective is independently stated health score; assessment boundary is LACP TUI source and later LACP operation, across experiments/sessions. Source: SRC-1, `tui/idle_agent.py`, `config/autoresearch-program.md`, `tui/autoresearch_metrics.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: background status/log messages and experiment summary; foreground may continue separately.
- Later read-back: history TSV reload sets experiment count; program/source reread for later experiments; changed Python source can reach later process imports, not proven live reload.
- Delegated visibility: baseline plus reconstructed program and one-experiment request; no automatic full foreground conversation delivery.
- Selection predicate: enabled idle threshold or explicit start; experiment-count limit; numeric `new_score >= baseline_score` selects keep.
- Invalidation or expiry: stop flag limits monitoring; subprocess timeout marks crash; score decrease checks out `tui/`; branch and checkout successes not enforced.
- Activation or effect: host is asked to modify/commit TUI source; score selects disposition; installed/live use and causal benefit unobserved.
- Evidence limits: failing metrics yield zero; subprocess status ignored before selection; prompt scope is not executor restriction; committed failures are not necessarily undone; no intervention/result trace supplied.

Admission roles: user starts/enables process, not per-content approval; model/host proposes edits; code selects numeric disposition and can attempt rejection; host is instructed to commit/revert. Answer oracle: no expected task-answer oracle; health proxy combines import, tool count, startup, tests, CSS and lint. Mode: bounded score experiments initiated by idle time or explicit command, with a program that also requests continuous iteration. Guidance is [RT-OBJ-autoresearch-program](#rt-obj-autoresearch-program); source/commits, result summaries and logs persist. The code does not systematically feed prior criticisms into the prompt.

Theory account: the program formulates an objective and acceptance method, but the inspected driver does not criticize or revise that method. Theory-builder conditions 1–4: (1) implementation conclusion status: wired — localized program states constraints/method; (2) implementation conclusion status: wired — driver reads it into proposal guidance and code uses its score criterion, but model compliance remains unobserved; (3) implementation conclusion status: uninspected — scalar decrease/revert is not content-directed criticism of a challenged theory with blame assignment, and host reasoning is opaque; (4) implementation conclusion status: uninspected — retained results/count support recurrence, not established criticism-fed theory iteration. Addressability: program sections/rules are individually editable text; no claim of automatic localized revision. Persistence: method across sessions, numeric outcomes/logs across experiments, source changes potentially across runs. Learning: uninspected — improved future task capacity not established by proxy score or keep state. Reflection: limited implemented self-representation through TUI health metrics, whose value can respond to source changes and guide subsequent source edits; accuracy/activation unobserved. Reflective theory builder: uninspected — no demonstrated method criticism loop. Autonomous theory builder: uninspected — computation drives experiment proposal/selection, but content-directed theory criticism and iteration are unresolved.

Self-improvement: afforded as an improvement-directed pathway modifying its own TUI organization. Link 1 is wired at baseline/new-score selection; link 2 is afforded through delegated edits, not observed; link 3 is afforded through later source import/model prompt construction; link 4 is uninspected — no subsequent operation trace causally depending on retained changes. No exercised self-improvement or successful improvement attribution.

> if new_score >= baseline_score:
>     # Get latest commit
> --- `tui/idle_agent.py`

> ["git", "checkout", "--", "tui/"],
> --- `tui/idle_agent.py`

#### RT-RTE-learning-promotion
Label: Cross-CLI learning enforce-state promotion

Endpoints: metric gate/evidence/approver arguments/provenance → aggregate decision → hashed promotion record and enforce state; rollback clears active promotion and returns shadow. Owner is promotion/rollback code; operator or caller supplies manual-gate inputs. Symbolic JSON state is stored under learning root; verifier evidence is file content but the gate checks nonemptiness, not its truth. Source: SRC-1, `bin/lacp-learn-promote`, `bin/lacp-learn-rollback`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: GO/NO-GO details or applied state/record; failed gate leaves mode unchanged.
- Later read-back: status/re-promotion/rollback read promotion state; downstream agent consumption of enforce mode uninspected in this runtime trace.
- Delegated visibility: inapplicable — promotion command does not delegate to an agent; it invokes metric/provenance checks.
- Selection predicate: aggregate all applicable gates; real apply forbids forced provenance and refuses already-enforced state.
- Invalidation or expiry: explicit rollback to shadow/null active promotion; event history is retained rather than erased.
- Activation or effect: writes enforce-mode state, not evidence of a later host enforcing learned guidance.
- Evidence limits: trusted filesystem, caller identities and metric/evidence validity are external assumptions; no authenticated two-person signature or causal benefit established.

Admission roles: caller supplies nonempty evidence path and distinct names; software computes metric/provenance gate results and admits/refuses state. Source labels these manual gates, but human contribution per input is unresolved. Answer oracle: metric thresholds/reference checks are delegated to eval; expected task-answer validity is not established here. Mode: explicit guarded promotion rather than each task's autonomous revision. Recovery resets mode/active record, not learning-event history. Knowledge-content revisions remain the memory analyst's responsibility.

> # Manual gate: verifier evidence file must exist and be non-empty.
> evidence_ok=false
> if [[ -n "${EVIDENCE}" && -s "${EVIDENCE}" ]]; then evidence_ok=true; fi
> --- `bin/lacp-learn-promote`

### Claims

#### RT-CLM-control-scope
Label: Run contract versus all effect paths

The declared contract assigns LACP authority over execution location, risk, approval, evidence and recovery. The boundary retains its minimum README passage. This report scopes the claim to the actual paths: wrapper launch policy, selective host hooks and separate native tool handlers, not a universal mediation invariant. Source: SRC-1, `README.md`, `tui/repl.py`, `tui/tools.py`, `bin/lacp-sandbox-run`; evidence passage: [boundary](boundary.md#boundary-and-evidence). Native route and direct-fallback counterexamples are retained in [RT-RTE-native-turn](#rt-rte-native-turn) and [RT-RTE-sandbox-launch](#rt-rte-sandbox-launch).

- doctrine conclusion status: claimed
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-CLM-idle-improvement
Label: Idle self-improvement claim

The source describes a background agent experimenting on its own codebase and following modify/test/keep/discard/repeat. Wiring supports this requested and score-selected organization change; it does not establish robust rollback, theory criticism or improved future performance. Source: SRC-1, `tui/idle_agent.py`; assessment: [RT-RTE-idle-experiment](#rt-rte-idle-experiment).

> Follows Karpathy's autoresearch pattern: modify → test → keep/discard → repeat.
> --- `tui/idle_agent.py`

- doctrine conclusion status: claimed
- implementation conclusion status: wired
- operation conclusion status: uninspected

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-mode-prompt
Label: Native mode prompt authority

Consumer: foreground provider/model. Channel: REPL `system` string built from focus/context and mode suffix. Force: natural-language instruction, not executable permission enforcement. Horizon: current session/model invocations; rebuilt on mode selection. A retained focus file can supply a future session's instruction. Effect depends on model interpretation; no observed compliance. Source: SRC-1, `tui/repl.py`.

> "\nAlways present your plan before executing tools."
> --- `tui/repl.py`

#### RT-BAP-autoresearch-code
Label: Autoresearch source authority

Consumer: later Python process loading changed TUI functions, including system-prompt/tool implementations. Channel: executable source files modified by delegated host, plus experiment program consumed at proposal time. Force: symbolic executable code at import/execution and natural-language guidance at proposal; these are distinct consumers, not weight mutation. Horizon: later experiments/process starts if changed source remains installed; branch switching and lack of hot reload constrain current-process reach. Source: SRC-1, `tui/idle_agent.py`, `config/autoresearch-program.md`; admission and unestablished live activation are in [RT-RTE-idle-experiment](#rt-rte-idle-experiment).

> program = _load_program()
> --- `tui/idle_agent.py`

## Annotations

none
