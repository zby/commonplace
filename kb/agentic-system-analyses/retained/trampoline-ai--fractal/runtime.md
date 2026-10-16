---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Fractal runtime baseline: CLI admission, direct workspace delegation, durable turns, interruption and configuration at the frozen revision."
run-id: AAS-2026-10-14-fractal-ee03010af4c2-01
reviewed-boundary: "6a226e7d539e229b5c7cc9ffa3b05ab1c8f00385"
---

# Fractal runtime report

## Runtime account

Fractal is a runtime client for a delegated coding computation. Its shipped CLI resolves model configuration, chooses host directories, creates an SBX interpreter, records a turn, and calls PredictRLM. PredictRLM owns the model/code loop; Fractal converts its result, records outcome and trace information, and presents a terminal or JSON response. This division is implementation evidence, not evidence that any invocation ran successfully (SRC-1, `pyproject.toml`, `src/fractal/cli.py`, `src/fractal/runtime.py`, `src/fractal/agent/service.py`). No command, example, test or model service was executed for this report. Operation, isolation and benefit remain unobserved.

The ordinary invocation is `fractal -p "request" --workspace DIRECTORY`, represented by [RT-RTE-headless-turn](#rt-rte-headless-turn). The principal is whoever invokes the CLI; a human and a calling agent can use the same interface. The process does not establish that identity as human approval of each edit. `main` dispatches `-p` to the headless driver. That driver reads explicit stdin, or conditionally appends piped context; it rejects stdin over 10 MiB and skips an empty request before creating a runtime. Explicit `--lm` bypasses layered provider configuration. Otherwise global, project and environment settings select DSPy main and sub LMs and retries. The normal budget is 30 unless the CLI or configuration overrides it (SRC-1, `src/fractal/cli.py`, `src/fractal/runtime_lms.py`, `src/fractal/config.py`).

The runtime's workspace identity is a resolved host path. Session state is keyed by that workspace and a session ID, while reusable sandbox identity is a hash of the resolved workspace and sorted additional mounts. A fresh process starts a new session unless `--resume` is supplied; sandbox reuse and session resumption are independent. `--fresh` removes the named reusable sandbox; `--ephemeral` requests a nonreused sandbox. Neither flag rolls back workspace edits or discards global session files. The interactive driver explicitly prewarms; the headless driver proceeds to submission without that call (SRC-1, `src/fractal/cli.py`, `src/fractal/runtime.py`, `src/fractal/session.py`, `src/fractal/agent/service.py`).

Submission allocates a turn UUID, appends a pending user turn, and saves it before calling the agent. The per-turn signature combines static coding guidance, root `AGENTS.md`, and rendered structured session summary. The main workspace, extra workspaces, current request and bounded detailed history are passed as predictor inputs. The signature makes the summary always-visible instruction text and tells the model to inspect detailed history from Python. History is limited to the last 20 turns; the rendered summary still iterates all summary turns. Consequently Fractal's history cap does not establish a fixed bound on always-visible prompt text. Inner-loop context summarization and recursive frame behavior are dependency responsibilities and remain uninspected (SRC-1, `src/fractal/runtime.py`, `src/fractal/session.py`, `src/fractal/agent/signature.py`). See [RT-OBJ-edit-workspace](#rt-obj-edit-workspace), [RT-OBJ-session-state](#rt-obj-session-state), and [RT-BAP-workspace-guidance](#rt-bap-workspace-guidance).

The next-step owner after `predictor.acall` is PredictRLM, configured with main/sub model adapters, filesystem and document skills, iteration budget and interpreter. The computation can use mutable direct workspaces. Fractal's filesystem instructions include Python syscalls and subprocess search. The grant set for an invocation comprises the primary workspace and explicitly included directories; it is not a list of individually approved writes or commands. The full capability surface also includes a caller-supplied interpreter and models at the Python API. Actual isolation, networking, recursive scheduling, provider-native capabilities and underlying tool enforcement require external PredictRLM, SBX and DSPy contracts. They are not established by naming the backend a sandbox (SRC-1, `src/fractal/agent/service.py`, `src/fractal/agent/skills.py`, `src/fractal/runtime_lms.py`). [RT-RTE-direct-agent](#rt-rte-direct-agent) tests the scope of CLI controls.

On normal return, the adapter checks output types, not semantic success or agreement between changed-file names and filesystem effects. Fractal saves response, changed-file information, trace-derived usage and available hook observations. Headless output is either response text or a single-turn JSON envelope; budget exhaustion exits 2, ordinary success 0, caught failures 1, and KeyboardInterrupt 130. Interactive presentation renders recorded turns and resumes its prompt. The summary status `succeeded` means a returned result outside the recognized budget-exhaustion branch, not verified task completion (SRC-1, `src/fractal/agent/service.py`, `src/fractal/runtime.py`, `src/fractal/cli.py`, `src/fractal/session.py`). See [RT-CLM-result-contract](#rt-clm-result-contract) and [RT-RTE-budget-exhaustion](#rt-rte-budget-exhaustion).

Four forcing cases bound the ordinary trace: interactive user cancellation, returned budget exhaustion, direct Python construction bypassing CLI/session controls, and configuration changes affecting a later launch. The cancellation branch distinguishes user interruption from model/tool failure only when the caller supplies an interruption predicate. Headless submission does not supply it. The UI may still report KeyboardInterrupt as interrupted while runtime cancellation does not finalize that turn through the interactive interruption branch. Fractal's comment relies on external cancellation-safe execution to leave the interpreter reusable. No workspace transaction or restoration is performed by the inspected runtime on either failure or interruption (SRC-1, `src/fractal/runtime.py`, `src/fractal/cli.py`, `src/fractal/tui/app.py`). See [RT-RTE-interactive-interrupt](#rt-rte-interactive-interrupt).

### Load-bearing controls and their limits

| Control | Owner and enforcement point | Strength and covered paths | Alternate path or required contract | Separate conclusion statuses |
| --- | --- | --- | --- | --- |
| Pending turn saved before model work | Fractal, `FractalRuntime.submit` | protocol; both shipped drivers use it | Direct agent calls bypass it; `on_pending` and pre-call failures lie outside the agent-call exception handler; save is ordinary `write_text`, not an atomic transaction | implementation conclusion status: wired; operation conclusion status: uninspected |
| Rooted editing and task-focused changes | Signature and filesystem skill, interpreted by model | policy; configured PredictRLM invocations receive the guidance | Subprocesses and raw Python are material execution alternatives; SBX mount/isolation enforcement is external, and prompt rules alone do not constrain them | implementation conclusion status: wired; operation conclusion status: uninspected |
| Additional mount admission | CLI `include_path` | invariant for parser-admitted extra paths at check time: reject a symlink, nonexistent path or nondirectory | Python constructors merely resolve included paths; primary `--workspace` uses `Path`, not this validator; no protection against later filesystem changes established | implementation conclusion status: wired; operation conclusion status: uninspected |
| Typed response envelope | `_prediction_to_result` | invariant on adapter return: string response, list of strings, optional RunTrace | It does not validate the filesystem diff or answer; direct custom runtime agents are not checked through this adapter | implementation conclusion status: wired; operation conclusion status: uninspected |
| User-interrupt persistence and reusable interpreter | Runtime branch plus TUI cancellation predicate | protocol for predicate-recognized cancellation | Unrecognized cancellation is re-raised; interpreter quiescence requires PredictRLM cancellation behavior stated in a comment, not inspected dependency code | implementation conclusion status: wired; operation conclusion status: uninspected |
| File/command accounting | PredictRLM hooks and Fractal event reducer | best effort; registered hook targets and callbacks | Import failure yields no hooks; observer failures are suppressed; callbacks are observations, not an approval barrier or complete filesystem audit | implementation conclusion status: wired; operation conclusion status: uninspected |

These controls are supported by SRC-1, `src/fractal/runtime.py`, `src/fractal/agent/service.py`, `src/fractal/agent/signature.py`, `src/fractal/agent/skills.py`, `src/fractal/cli.py`, `src/fractal/events.py`, and `src/fractal/session.py`. They do not establish a deployment guarantee. The deployed container, host access, provider resolution and external service behavior are uninspected.

Change admission occurs in several distinct planes. Workspace changes are effected inside the delegated computation under task guidance, not staged for a Fractal approval dialog. Root `AGENTS.md` can itself be workspace content and is reread on a later agent call; changing it can alter subsequent prompt guidance, but no trace here establishes such an update or reliable compliance. Model/provider/default configuration is changed through validated config commands or interactive setup, with current runtime changes sometimes preceding the persistent write. Package production is a separate tag-triggered release workflow, not an online agent self-update. These mechanisms are distinguished in [RT-RTE-headless-turn](#rt-rte-headless-turn), [RT-RTE-config-change](#rt-rte-config-change), [RT-RTE-package-release](#rt-rte-package-release), and [RT-BAP-workspace-guidance](#rt-bap-workspace-guidance). Model judgment is not an answer oracle; none of these inspected runtime routes wires a reference answer to task-result admission (SRC-1, `src/fractal/agent/signature.py`, `src/fractal/agent/service.py`, `src/fractal/config_commands.py`, `src/fractal/tui/app.py`, `.github/workflows/release.yml`).

Added implementation coverage under SRC-1 includes the bounded cancellation and model-setup bodies in `src/fractal/tui/app.py`, hook construction in `src/fractal/events.py`, config set/unset in `src/fractal/config_commands.py`, config atomic replacement in `src/fractal/config.py`, provider dispatch in `src/fractal/providers.py`, the full filesystem skill in `src/fractal/agent/skills.py`, and the release workflow in `.github/workflows/release.yml`. The principal CLI, runtime, session, signature and agent paths were read across admission and return. This adds implementation anchors, not a source or evidence layer. Provider adapter internals, onboarding details, installation automation and exact dependency resolution were not exhaustively traced; no claim of exhaustive operational or security coverage is made.

## Shared records

### Components

#### RT-CMP-main-lm
Label: Main LM

Source-native identity: `lm` on FractalAgent, constructed as a DSPy LM by runtime configuration or supplied by the caller. Representational form: distributed-parametric model computation behind a symbolic adapter. Storage substrate: external model service or caller-selected backend; weights are not present in Fractal source. Fractal changes adapter selection, not weights. Parameter change during operation: uninspected inside the provider; no weight-update operation is exposed in the inspected Fractal call path. Exact version pin: not enforced by Fractal; a model string can name an alias. Mutable endpoint resolution: possible through configured base URL/provider/model selection or a supplied adapter; exact remote resolution is uninspected. Evidence: SRC-1, `src/fractal/runtime_lms.py`, `src/fractal/providers.py`, `src/fractal/runtime.py`, `src/fractal/agent/service.py`.

> return dspy.LM(model=lm)
> --- `src/fractal/runtime_lms.py`

> "lm": self.lm,
> "sub_lm": self.sub_lm,
> --- `src/fractal/agent/service.py`

#### RT-CMP-sub-lm
Label: Sub LM

Source-native identity: `sub_lm` on FractalAgent. It follows the main LM by default or is separately selected by CLI/configuration, potentially on another provider. It is a distinct decision role even when the adapter object is shared. Representational form: distributed-parametric model computation behind a symbolic adapter. Storage substrate: external or caller-selected provider, uninspected weights. Parameter change during operation: provider-internal and uninspected; Fractal's visible mechanism replaces adapters rather than training weights. Exact version pin: not enforced. Mutable endpoint resolution: possible as for the main LM, with an independently chosen provider/model. Actual subordinate invocation policy and context are owned by PredictRLM and uninspected. Evidence: SRC-1, `src/fractal/runtime_lms.py`, `src/fractal/runtime.py`, `src/fractal/agent/service.py`.

> lm = coerce_lm(args.lm)
> lm.num_retries = num_retries
> sub_lm = lm if args.sub_lm is None else coerce_lm(args.sub_lm)
> --- `src/fractal/runtime_lms.py`

### Operative objects

#### RT-OBJ-edit-workspace
Label: EditWorkspaceWithSession signature

Source-native identity: per-turn `EditWorkspaceWithSession` DSPy signature. Its operative instruction body is natural-language content; typed input/output field declarations are symbolic interface metadata. Storage substrate: shipped Python source and a dynamically constructed in-process class; rendered summary and loaded root guidance enter its docstring. The body requests focused editing, current-request precedence over workspace instructions, and explicit history inspection for exact recall. It does not supply an executor-level write policy. Evidence: SRC-1, `src/fractal/agent/signature.py`, `src/fractal/agent/service.py`.

> The workspace contains an AGENTS.md file with project-specific guidance from
> the user. Follow it when working in this workspace; the current `user_message`
> takes precedence if they conflict.
> --- `src/fractal/agent/signature.py`

> The summary above is compressed structured trajectory context and is always
> visible. It preserves prior user messages and compressed agent results. For
> exact prior REPL reasoning, code, outputs, tool calls, or predict calls, inspect
> `session_history` from Python.
> --- `src/fractal/agent/signature.py`

#### RT-OBJ-session-state
Label: SessionState runtime checkpoint

Source-native identity: `SessionState`, containing session ID, structured summary turns and detailed history turns. Representational form: symbolic schema/status/counters and natural-language user messages, responses and error text, with externally defined RunTrace content. Storage substrate: JSON under workspace-keyed global state and in-memory Pydantic models. This record establishes the runtime checkpoint container, not a complete account of its memory transformations. A pending turn precedes execution; result, failure, budget or recognized interruption updates the matching turn. Later explicit resume loads it and later submission supplies summary/history to the model. Evidence: SRC-1, `src/fractal/session.py`, `src/fractal/runtime.py`.

> payload = self.state.model_dump(mode="json")
> path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
> --- `src/fractal/session.py`

> self.state.history = self.state.history[-MAX_HISTORY_TURNS:]
> --- `src/fractal/session.py`

### Routes

#### RT-RTE-headless-turn
Label: Headless turn submission

Endpoints and progression: CLI caller → stdin/request preparation → LM resolution → runtime construction/resume → pending save → FractalAgent → PredictRLM → typed result conversion → terminal-state save → text/JSON output and exit. Fractal owns admission and persistence; PredictRLM owns inner next-step selection. Context includes current message, root guidance, rendered summary and history. Action effects include direct workspace mutation; state effects include the turn checkpoint. Coordination is one awaited delegated call in this driver, not a Fractal-owned worker scheduler. Evidence: SRC-1, `src/fractal/cli.py`, `src/fractal/runtime.py`, `src/fractal/agent/service.py`, `src/fractal/session.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: response and changed-file list, optionally JSON status and trace-derived usage; normal 0, failure 1, budget 2 and KeyboardInterrupt 130 exit codes.
- Later read-back: saved turn summary/history reaches a later submit in the session, or explicit workspace/session-ID resume in a later process; workspace edits can be inspected by subsequent delegated work.
- Delegated visibility: workspace and optional extra Workspace objects, user message and session_history are predictor inputs; summary/root instructions are signature text; exact inner prompt transformation is external.
- Selection predicate: `-p` selects headless mode; explicit resume selects a session, otherwise a new session is made; main/sub LM selection follows explicit arguments or layered configuration.
- Invalidation or expiry: detailed history is limited to 20 turns; no summary-turn cap is applied by the inspected renderer; sandbox fresh/ephemeral policies are distinct from session retention.
- Activation or effect: direct workspace and session writes are wired; model adherence and task success are unobserved.
- Evidence limits: source-only path; model, execution backend and actual files changed are not observed.

Admission account: trigger is an open request. The caller proposes the task and selects mounts; delegated model/code proposes and effects file edits under natural-language guidance. Fractal checks returned types, not each edit's correctness. No per-edit human veto occurs between submission and the inspected predictor call. A caller can interrupt, but that is not rollback. Recovery records errors/traces and closes the interpreter; already applied host-file edits are not restored by this route. Guidance comes from [RT-OBJ-edit-workspace](#rt-obj-edit-workspace), filesystem skill and root AGENTS.md; file edits and checkpoint data persist. The requested verification of important edits is not a supplied answer oracle. Operating mode is open-ended coding under an iteration budget, not a bounded comparison experiment. Retained knowledge revision details belong to the memory analysis.

> turn_id = self.session.add_user_message(user_message)
> self.session.save(self.workspace_path)
> --- `src/fractal/runtime.py`

> await predictor.acall(
>     workspace=workspace,
>     included_paths=included_workspaces or None,
>     user_message=user_message,
>     session_history=session_history or [],
> ),
> --- `src/fractal/agent/service.py`

#### RT-RTE-interactive-interrupt
Label: Interactive interrupted turn

Endpoints and progression: TUI request → asynchronous submit task → signal handler sets interruption flag and cancels task → runtime records interrupted turn → save → UI renders and returns to prompt. It otherwise shares ordinary submission, mounting and model selection with [RT-RTE-headless-turn](#rt-rte-headless-turn). Fractal's signal/UI/runtime code owns this outer recovery decision, while dependency execution owns cancellation of the in-flight cell. Evidence: SRC-1, `src/fractal/tui/app.py`, `src/fractal/runtime.py`, `src/fractal/cli.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: recognized TUI cancellation yields no normal FractalResult and renders the recorded interruption; the UI returns to prompt.
- Later read-back: saved interrupted status, available trace and error become later session context; workspace changes already applied remain available.
- Delegated visibility: cancellation propagates into the in-flight agent call; exact interpreter interruption and cleanup are uninspected dependency behavior.
- Selection predicate: TUI signal handler in turn mode sets the flag; runtime interruption handling requires the supplied predicate to be true.
- Invalidation or expiry: active submit task is cleared after completion; retained history follows the ordinary history cap; no edit undo is performed.
- Activation or effect: cancellation request and interrupted checkpoint are wired, not evidence of actual quiescent execution or consistent external effects.
- Evidence limits: headless driver does not provide the interruption predicate; unrecognized CancelledError is re-raised without this finalization branch. Pending-save and on_pending failures also precede the guarded agent call.

Decision roles: user signal requests stopping; signal handler and runtime code decide the branch. No answer oracle or candidate comparison is used. Operating mode is recovery within an open request. Interruption can stop further computation under the external contract, not reject or revert an already executed edit. Guarantee strength: protocol. Owner/enforcement point: FractalRuntime cancellation branch for durable status; PredictRLM for cell quiescence, whose implementation is outside this boundary.

> if interrupt_requested is None or not interrupt_requested():
>     raise
> --- `src/fractal/runtime.py`

> self._turn_interrupt_requested = True
> self._show_interrupting_status()
> task = self._active_submit_task
> if task is not None and not task.done():
>     task.cancel()
> --- `src/fractal/tui/app.py`

#### RT-RTE-budget-exhaustion
Label: Iteration budget fallback

Endpoints and progression: PredictRLM returns a FractalResult with trace status `max_iterations` → runtime stores response but uses the distinct status/error → CLI outputs fallback and exits 2. Decision owner is Fractal's trace-status branch; dependency policy produces the fallback. Context and direct-write scope are the same as ordinary submission. Evidence: SRC-1, `src/fractal/runtime.py`, `src/fractal/cli.py`, `src/fractal/session.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: fallback response and changed_files remain available; headless status is max_iterations and exit code is 2.
- Later read-back: response, budget error and available trace persist for a later turn/resume; applied workspace changes remain.
- Delegated visibility: inner loop receives max_iterations through predictor configuration; fallback extraction implementation is uninspected.
- Selection predicate: returned trace is non-null and its status equals max_iterations; otherwise runtime records succeeded after a normal return.
- Invalidation or expiry: each turn has a newly constructed predictor/budget; checkpoint retention follows session policy.
- Activation or effect: wired distinction between recognized incomplete fallback and ordinary return, not a proof of task completion on the other branch.
- Evidence limits: absent trace or unrecognized status cannot establish that SUBMIT was reached; actual iteration enforcement is external.

Decision roles: dependency provides result/trace; Fractal code classifies status; caller judges whether to continue. No expected-answer oracle is present. Operating mode is a budgeted open request, not optimization by task-result comparison. The fallback checkpoint is automatic admission, with no separate human approval and no edit rollback.

> if result.trace is not None and result.trace.status == "max_iterations":
> --- `src/fractal/runtime.py`

#### RT-RTE-direct-agent
Label: Direct Python agent invocation

Endpoints and progression: Python caller constructs FractalAgent with optional interpreter/models → calls aforward with caller-provided workspace/history/summary/mounts → PredictRLM → typed FractalResult. This is the same adapter used by shipped drivers, with client controls not forced by the adapter. Evidence: SRC-1, `src/fractal/agent/service.py`, `src/fractal/runtime.py`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: typed FractalResult; caller owns its presentation and persistence.
- Later read-back: uninspected — a direct caller can persist workspace changes or supply history, but the adapter itself does not save/load a session checkpoint.
- Delegated visibility: caller-provided summary/history, workspace paths and selected model/interpreter reach the predictor configuration and inputs.
- Selection predicate: caller invokes the Python API rather than CLI parsing/runtime.submit; an absent interpreter selects sandbox_backend sbx, otherwise the supplied interpreter is used.
- Invalidation or expiry: caller controls agent lifecycle and close; included paths are resolved without CLI include_path validation.
- Activation or effect: mutable DIRECT workspaces and arbitrary supplied interpreter are afforded by construction; exercised effects are unobserved.
- Evidence limits: no additional direct caller was executed or supplied; exposed construction does not establish deployed use or enforcement of external backends.

Admission account: open caller-controlled invocation. Caller proposes grants and task; dependency/model performs execution. Fractal's adapter offers no per-edit veto or rollback; supplied executor semantics determine effects. The same source guidance is built, but session checkpoint protocol and parser path checks are not universal. No answer oracle is wired here. This route is a counterexample to attributing CLI controls to every Fractal invocation.

> if self.interpreter is None:
>     predictor_kwargs["sandbox_backend"] = "sbx"
> else:
>     predictor_kwargs["interpreter"] = self.interpreter
> --- `src/fractal/agent/service.py`

#### RT-RTE-config-change
Label: Provider and default configuration change

Endpoints and progression: config command edits a dotted key → Pydantic validation and applicable model-catalog checks → TOML write through temporary file and replace → later layered-config resolution. TUI setup instead prompts for selection, applies adapters to the current runtime, then writes configuration. Fractal owns these transitions, while the operator supplies the proposed selection. Evidence: SRC-1, `src/fractal/config_commands.py`, `src/fractal/config.py`, `src/fractal/runtime_lms.py`, `src/fractal/runtime.py`, `src/fractal/tui/app.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: command reports target path or error; interactive setup can change current runtime adapters before persistent write completes.
- Later read-back: global/project TOML and environment overlays determine future LM/default resolution; project settings can override saved global defaults on next launch.
- Delegated visibility: selected adapters and defaults become predictor configuration; config file text is not itself passed as model instruction.
- Selection predicate: command/setup chooses provider, model or defaults; config precedence is global then project then environment; explicit --lm bypasses layered resolution.
- Invalidation or expiry: unset/reset/replacement can change persisted values; no automatic version pin or config revision archive is established by the inspected writers.
- Activation or effect: current adapters are replaced by apply_provider_selection; future launches read saved settings. Actual provider resolution and changed behavior are unobserved.
- Evidence limits: current mutation and persistent write are not one transaction; a write failure does not automatically undo the already applied runtime selection. Direct LM construction bypasses provider registry checks.

Admission account: operator commands/prompts propose capability configuration; schema, model-selection and readiness code can reject invalid values. Human judgment is selecting settings, not evaluating every downstream model response. Operating mode is manual configuration, not an improvement curriculum. No task answer oracle is involved; catalog checks constrain model identifiers rather than grade answers. Recovery includes correcting or unsetting values and re-running setup; no automatic rollback of current model swaps is implemented in the inspected sequence. Guidance shaping the proposal is the configuration/setup interface; what persists is TOML, not trained model parameters.

> self.runtime.apply_provider_selection(
>     selection, sub_selection=sub_selection
> )
> path = write_config(config, path=result.path)
> --- `src/fractal/tui/app.py`

> os.replace(tmp_path, config_path)
> _chmod_posix(config_path, 0o600)
> --- `src/fractal/config.py`

#### RT-RTE-package-release
Label: Tag-triggered package release

Endpoints and progression: pushed version tag → validation job → GitHub release → package build → artifact transfer → PyPI publication. This is production package admission, not an online model-generated successor selection. GitHub Actions owns execution; the tag-pushing principal is not authenticated as human by source alone. Evidence: SRC-1, `.github/workflows/release.yml`, `pyproject.toml`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: configured release/build/publication artifacts; actual artifacts and CI success are not supplied.
- Later read-back: inapplicable — the workflow publishes a package rather than retaining per-invocation experience for a later model call; installation can change subsequent deployed code.
- Delegated visibility: inapplicable — this workflow has no model call.
- Selection predicate: push of v*.*.* tags; version must match pyproject; stable tags require main ancestry, prerelease tags skip that check.
- Invalidation or expiry: package replacement/rollback policy is uninspected; this workflow does not automatically revert a prior release.
- Activation or effect: publication is configured; installation or use of the published artifact is not evidenced.
- Evidence limits: GitHub environment protection, remote credentials and actual execution are external; no test job is a dependency in this release workflow.

Admission account: repository changes/tag supply the proposed package; shell checks can reject ancestry/version mismatches, and failed job dependencies prevent later stages. `environment: release` is wired but does not prove a human approval rule. Operating mode is release automation; version equality is a symbolic gate, not a model-answer oracle or demonstrated quality improvement. There is no agent revision trigger in the inspected workflow. Recovery requires maintainer action; no automatic rollback is shown.

> # Skip ancestry check for prerelease tags (e.g., v1.2.3-rc.1)
> if [[ "$TAG" == *"-"* ]]; then
> --- `.github/workflows/release.yml`

> publish:
>     needs: build
>     runs-on: ubuntu-latest
>     environment: release
> --- `.github/workflows/release.yml`

### Claims

#### RT-CLM-result-contract
Label: Result conversion checks structure, not edit correctness

Claimed operation: adapter requires response string, changed_files list[str] and optional RunTrace before making FractalResult. This is inspected implementation, not a product claim of semantic verification. Changing files occurs through delegated DIRECT workspace execution, so successful conversion does not commit or validate a filesystem transaction. Evidence: SRC-1, `src/fractal/agent/service.py`, `src/fractal/agent/signature.py`. Guarantee strength: invariant for returned adapter structure; no claimed guarantee for content correctness. implementation conclusion status: wired. operation conclusion status: uninspected.

> response = prediction.response
> if not isinstance(response, str):
>     raise TypeError("PredictRLM response must be a string.")
> --- `src/fractal/agent/service.py`

> if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
>     raise TypeError(f"{field_name} must be list[str].")
> --- `src/fractal/agent/service.py`

#### RT-CLM-hook-accounting
Label: Runtime hooks provide best-effort accounting

Claimed operation: Fractal configures file and subprocess hook targets, normalizes events and accumulates observations for persisted turn accounting and display. It does not use these callbacks as an edit approval gate. Missing RuntimeHook import returns an empty list, and callback exceptions are suppressed. Thus counters/traces do not establish complete auditing of all execution mechanisms, subprocess descendants or remote model actions. Evidence: SRC-1, `src/fractal/events.py`, `src/fractal/runtime.py`, `src/fractal/agent/service.py`. Guarantee strength: best effort. implementation conclusion status: wired. operation conclusion status: uninspected.

> try:
>     from predict_rlm import RuntimeHook
> except ImportError:
>     return []
> --- `src/fractal/events.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-workspace-guidance
Label: Root workspace instructions influence later turns

Consumer: PredictRLM's model-facing signature constructed by FractalAgent. Channel: root workspace `AGENTS.md` text inserted into natural-language signature instructions, alongside static guidance and rendered session summary. Force: model-interpreted instruction policy, expressly subordinated to the current user message; not an enforced filesystem permission rule. Horizon: each agent invocation rereads root instructions, including later turns/sessions if the file persists. Loader silently omits unreadable/undecodable content and truncates above 20,000 characters with a request to read the full file. Model compliance and full-file reload are not observed. Evidence: SRC-1, `src/fractal/agent/service.py`, `src/fractal/agent/signature.py`.

> if len(text) > _MAX_WORKSPACE_INSTRUCTIONS_CHARS:
>     text = (
>         text[:_MAX_WORKSPACE_INSTRUCTIONS_CHARS]
>         + "\n\n[AGENTS.md truncated — read the full file from the workspace.]"
>     )
> --- `src/fractal/agent/service.py`

Workspace edits can change this later guidance because the workspace is mutable, but the ordinary coding path does not itself establish a dedicated theory-revision procedure, improved capacity or exercised self-improvement. The live consumption path is established; evidence-responsive update and subsequent behavior depending on the update are not. The static instruction body requests conduct, not reliable content-directed criticism of its own method. No theory-builder claim is made for that path.

## Annotations

none
