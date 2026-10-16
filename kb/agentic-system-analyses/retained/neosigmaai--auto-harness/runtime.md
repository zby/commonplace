---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "auto-harness runtime baseline: coding-agent improvement loop, three benchmark routes and conditional admission at the frozen Git revision."
run-id: AAS-2026-10-15-auto-harness-92303e444cb2-01
reviewed-boundary: "52360dbbeb8cea8886d90778e634a145c51da735"
---

# auto-harness runtime report

## Runtime account

### Scope and ordinary invocation

This is an improvement plane, not the enclosing coding-agent runtime. The frozen source supplies executable benchmark adapters and candidate templates plus a natural-language program for an external coding agent. All source findings below use SRC-1 at the boundary revision. Evidence layers are implementation for Python/configuration behavior and doctrine/design for requested coding-agent conduct. No execution trace or experiment was supplied; operation, actual activation and benefit remain uninspected. The source coverage used here is `prepare.py`, `benchmark.py`, `gating.py`, `record.py`, all three candidate templates, the BIRD service/runtime/setup helpers, all four program templates, `pyproject.toml` and `docker-compose.yml`. These are within the registered source's existing functional coverage, not additional sources.

The claimed work is explicit:

> You are an autonomous coding agent optimizing `agent/agent.py` to perform better on a benchmark. You run a tight loop:
> --- `program_templates/base.md`

An ordinary Terminal-Bench invocation begins with configured preparation, then an external coding agent follows the generated program. [RT-RTE-prepare-baseline](#rt-rte-prepare-baseline) initializes state, installs the candidate template and establishes a baseline/split. The coding agent calls `benchmark.py` on train tasks; [RT-RTE-terminal-task](#rt-rte-terminal-task) hands task execution to Harbor and the selected environment. A fresh task conversation requests bash calls, executes them, feeds back bounded outputs and terminates on text-only completion, a model exception or the step limit. Harbor's verifier result becomes a task reward. The CLI prints rewards and persists the returned result mapping. The coding agent diagnoses train failures and edits the candidate under [RT-RTE-candidate-revision](#rt-rte-candidate-revision), then invokes [RT-RTE-gate-admission](#rt-rte-gate-admission). On success it is instructed to commit and call [RT-RTE-iteration-record](#rt-rte-iteration-record), append learnings and repeat; on failure it is instructed to revert. The last terminal product is a changed candidate file/commit, score history and learnings, followed by an operator summary after five non-improving iterations. The outer scheduler, actual reads, edits, commits, reverts and stopping behavior belong to the external coding agent and are not implemented by these scripts (SRC-1, `program_templates/base.md`).

The two other material task paths are [RT-RTE-tau-task](#rt-rte-tau-task), which registers a Python agent factory and returns next messages to tau2, and [RT-RTE-bird-session](#rt-rte-bird-session), which runs a harness-owned HTTP/ADK adapter beside external simulator/database services. Neither is reducible to the Terminal bash-tool loop. Their different tool owners, state frames and oracle dependencies are retained below. Model mutability is separated in [RT-CMP-candidate-model](#rt-cmp-candidate-model), [RT-CMP-user-model](#rt-cmp-user-model) and [RT-CMP-coding-model](#rt-cmp-coding-model).

### Effect boundaries, authority and isolation

There are three distinct authority levels. The outer coding agent is requested to edit only two files, but the supplied program is interpreted instruction, not an OS permission grant. The candidate file is executable Python: changing it can change instructions, tools, context processing or the task loop. The task tools then act within externally supplied benchmark environments. Terminal exposes one bash schema, tau receives domain tools from tau2, and BIRD receives ADK tools/callbacks from external modules. A schema or callback registration is not proof of effective sandboxing or reliable compliance (SRC-1, `program_templates/base.md`, `agent/templates/terminal_bench.py`, `agent/templates/tau_bench.py`, `agent/templates/bird_interact.py`).

The capability surface is consequently broader than the default tool list: edited candidate Python, direct model calls, imported external callbacks and spawned benchmark/service processes all matter. The current grant set is unresolved because no actual configuration, keys, host privileges or sandbox instance was supplied. The deployed isolation envelope is likewise unobserved. Compose mounts agent, workspace, configuration, infrastructure scripts and data read-write by default; it does not make the infrastructure instruction a filesystem boundary (SRC-1, `docker-compose.yml`). BIRD's runner binds its services to loopback, while directly running the service module binds `0.0.0.0`; the inspected HTTP handlers have no local authentication check. This is a deployment distinction, not evidence that a service was publicly reachable (SRC-1, `benchmark.py`, `agent/helpers/bird_interact/bird_service.py`).

### Load-bearing guarantees and forcing cases

**File-edit guard.** Owner: gate and recorder. Enforcement: Git path comparisons against `ALLOWED_AGENT_FILES`; recorder additionally inspects the last commit. Strength: best effort, not an invariant or an execution sandbox. Covered paths are calls to these scripts with the guard enabled and Git checks functioning. Alternate paths include direct benchmark calls, candidate Python effects, ignored files, configuration disabling, and an external coding agent bypassing the procedure. External contract: trustworthy Git/configuration and an operator/runtime that actually uses the gate. It does not intercept writes at the time they happen. The allowlist includes generated `PROGRAM.md`, despite the narrower requested edit targets.

> ALLOWED_AGENT_FILES = frozenset({"agent/agent.py", "PROGRAM.md"})
> --- `gating.py`

> If git is unavailable or we're not in a git repo, prints a one-time
> warning to stderr and returns ``[]`` (treated as no violations) so the
> rest of the gate can still run in degraded mode rather than failing
> confusingly mid-pipeline.
> --- `gating.py`

- implementation conclusion status: wired
- operation conclusion status: uninspected

**Regression/nondecreasing-score gate.** Owner: `run_gate`; enforcement: suite pass fraction versus threshold and returned test mean versus maximum recorded score. Strength: protocol. Given returned results, the arithmetic checks are executable; they do not establish complete evaluation, oracle validity or statistically improved performance. Missing suite tasks count against the requested-task denominator. Empty suite skips that check. Test scoring uses the returned mapping, not an independently verified complete task inventory. External contract: benchmark/verifier fidelity, complete task coverage and trustworthy prior records (SRC-1, `gating.py`, `benchmark.py`). [RT-RTE-gate-admission](#rt-rte-gate-admission) contains the admission details.

> test_passed = best is None or val >= best
> --- `gating.py`

- implementation conclusion status: wired
- operation conclusion status: uninspected

**Train-only diagnosis.** Owner: outer coding agent under the program; local trace controls are owned by the Terminal adapter/template and BIRD copier. Strength: policy, with partial implementation support. Non-train Terminal runs set `HARNESS_SAVE_TRACE=0`, and the stock candidate respects it; BIRD copies only train traces to the designated diagnosis directory. This does not block the outer agent from other files or prove external framework logs lack test information. The Terminal program explicitly warns that raw jobs contain train and test data. Tau's local adapter does not implement a comparable trace filter; external trace behavior is uninspected. External contract: coding-agent compliance, default candidate behavior and external logging discipline (SRC-1, `benchmark.py`, `agent/templates/terminal_bench.py`, `program_templates/tau_bench.md`).

> **Only read traces in `workspace/traces/latest/`.** Do not look in `workspace/tbench_jobs/` — it contains both train and test data.
> --- `program_templates/terminal_bench.md`

- implementation conclusion status: wired
- operation conclusion status: uninspected

Four source-only forcing cases qualify stronger interpretations:

1. **Committed forbidden edit / unavailable Git.** The recorder's `check_last_commit=True` catches a forbidden change committed before recording, but only the immediate parent diff is added. Git unavailability yields no violations, and config can disable checking. Thus neither the gate nor recorder proves lifetime edit confinement (SRC-1, `gating.py`, `record.py`).
2. **No verifier output / missing task.** Existing `None` entries count as zero. Terminal/BIRD successful parse paths fill selected missing IDs with `None`; early no-output paths return `{}` before that fill. `val_score({})` is zero. With an empty suite and best score zero or no prior score, zero can satisfy the gate without a successful evaluation. Tau returns only simulations received, so a dropped task is not independently restored to the full-test denominator. The guard against silently dropped suite tasks does not generalize to every score path (SRC-1, `benchmark.py`, `gating.py`).
3. **Record without successful gate.** `record()` takes numerical caller arguments, checks file paths and appends. It does not consume a gate certificate or rerun scoring. The instructed gate→commit→record sequence is not a transactional admission barrier (SRC-1, `record.py`, `program_templates/base.md`).
4. **Alternate runtime/trace paths.** Terminal directly calls LiteLLM and executes bash through Harbor; tau delegates model transport/tool execution; BIRD delegates callbacks/tools and ADK scheduling, with separate HTTP session control. Candidate edits may change the stock trace behavior. Baseline preparation excludes `None` tasks from generated Terminal/BIRD splits, a distinct selection path from later timeout-as-zero scoring. Thus the timeout rule is not an all-lifecycle invariant, nor trace suppression an information-flow guarantee (SRC-1, `prepare.py`, `benchmark.py`, all three candidate templates).

These inspections establish counterexamples in control flow, not observed incidents. Provider-native execution internals, actual shell grants, external callback decisions, verifier correctness and concrete benchmark coverage remain unobserved.

## Shared records

### Components

#### RT-CMP-candidate-model
Label: Candidate task model

Source-native identity: tau `llm`/`AGENT_MODEL`, Terminal `model_name`/`MODEL`, and BIRD `settings.system_agent_model` resolved through external `build_adk_model`. Representational form: distributed-parametric. Storage substrate: external provider/model deployment, not repository files. Parameters are not changed by the inspected local inference routes; no local weight-update operation is present in those routes. Provider-side updates are uninspected. Exact model versions are not pinned by the templates: runtime configuration/environment supplies names, with a Terminal/runner default of `gpt-5.4`. A mutable endpoint or alias can resolve to another model; endpoint policy is external and uninspected. Changing the candidate's prompt or Python does not itself establish changed parameters (SRC-1, `benchmark.py`, `agent/templates/tau_bench.py`, `agent/templates/terminal_bench.py`, `agent/templates/bird_interact.py`).

> model = self.model_name or MODEL
> --- `agent/templates/terminal_bench.py`

#### RT-CMP-user-model
Label: Benchmark user simulator model

Source-native identity: tau `llm_user` and BIRD `USER_SIM_MODEL`. Representational form: distributed-parametric; storage substrate: external model service. Tau defaults the user model to the candidate model; BIRD passes an override when configured. The inspected adapters do not update parameters, pin a model snapshot or constrain provider alias resolution. Whether an endpoint changes underlying models is uninspected. The simulator supplies interactions, not automatically an authoritative expected answer (SRC-1, `benchmark.py`).

> self.user_model = user_model or self.agent_model
> --- `benchmark.py`

#### RT-CMP-coding-model
Label: External coding-agent model

Source-native identity: the autonomous coding agent addressed by `PROGRAM.md`. Representational form: distributed-parametric for its model, with an uninspected enclosing runtime. Storage substrate, exact model/version, parameter mutability during operation and endpoint resolution are uninspected: this repository does not select or implement that model. Its documented role is proposal, diagnosis and procedural execution, not an independently supplied run (SRC-1, `program_templates/base.md`; see the quoted claimed work above).

### Operative objects

#### RT-OBJ-agent-code
Label: Candidate Python implementation

Source-native identity: `agent/agent.py`, overwritten from the selected `agent/templates/` file during preparation and later edited by the coding agent. Representational form: symbolic executable Python; storage substrate: local file and, under the prescribed loop, Git commits. Imports/builders execute it in benchmark processes, so its admission is consequential beyond text delivery. Natural-language instruction constants inside it have a different consumer and are separately described in [RT-OBJ-agent-instructions](#rt-obj-agent-instructions). Evidence: SRC-1, `prepare.py`, `benchmark.py`, `agent/helpers/bird_interact/bird_adk_runtime.py`.

> shutil.copy2(template, "agent/agent.py")
> --- `prepare.py`

#### RT-OBJ-agent-instructions
Label: Candidate instruction constants

Part of: [RT-OBJ-agent-code](#rt-obj-agent-code)

Source-native identity: tau/Terminal `AGENT_INSTRUCTION` and BIRD `AINTERACT_INSTRUCTION`/`CINTERACT_INSTRUCTION`. Representational form: natural language consumed by a task model; storage substrate: Python string literals in the candidate file and commit. Delivery paths construct system messages or ADK agents. These instructions request policy compliance, efficient tools or task completion; they do not enforce those behaviors. Evidence: SRC-1, all three `agent/templates/` paths named in the account.

> - When you are done, send a final text message (no tool call) summarizing what you did.
> --- `agent/templates/terminal_bench.py`

#### RT-OBJ-program
Label: Generated improvement program

Source-native identity: `PROGRAM.md`, composed from `program_templates/base.md` and the selected benchmark supplement. Representational form: natural language, including command examples interpreted by the external coding agent. Storage substrate: local Markdown file. It supplies the outer decision procedure, edit restrictions, rollback, learning-log request and stopping policy; the scripts do not interpret the prose themselves. Evidence: SRC-1, `prepare.py`, `program_templates/base.md`.

> f.write(base.rstrip("\n") + "\n\n" + benchmark_content)
> --- `prepare.py`

### Routes

#### RT-RTE-prepare-baseline
Label: Prepare candidate and baseline

Endpoints/progression: caller → `prepare.py` → configuration and dependency/data checks → workspace initialization → selected candidate copy and composed program → baseline runner → score row and, for first Terminal/BIRD setup, stratified split. Owner: deterministic preparation code after caller selection of benchmark/configuration. This is a bounded benchmark mode, not an open task request. The caller's human/computational identity is unresolved. Baseline's oracle is the selected external benchmark reward, not an independently inspected reference answer (SRC-1, `prepare.py`).

Admission: preparation replaces candidate code and program without per-content human approval. Existing workspace files are preserved, and a prior result row skips the baseline, but template copying happens before that skip. Re-running preparation can therefore overwrite an optimized candidate without resetting historical scores. New Terminal/BIRD splits use seed 42, stratify passing/failing returned tasks at 70/30 and exclude `None` results; tau relies on external named splits. Recovery instructions for excluded timeout tasks require deleting the split and rerunning preparation. BIRD provisioning may clone external code/data, create a venv/install requirements and start Postgres; these are production-machinery admissions triggered by setup, not iterative score-gated candidate changes. Existing paths/interpreter overrides can be reused. The helper uses shallow clones without a fixed revision; external content and compatibility are not established by this source pin (SRC-1, `prepare.py`, `agent/helpers/bird_interact/setup.py`).

> subprocess.run(["git", "clone", "--depth", "1", BIRD_INTERACT_REPO, tmp], check=True)
> --- `agent/helpers/bird_interact/setup.py`

- Immediate return: printed readiness/baseline, or environment failure and process exit.
- Later read-back: suite, history and split files are consumed by later benchmark/gate invocations; candidate/program files govern subsequent task and coding-agent work.
- Delegated visibility: runners receive selected configuration/tasks; external provisioning receives credentials/environment. Exact downstream visibility is uninspected.
- Selection predicate: configured benchmark, file existence, prior result rows, baseline reward and seed-based split.
- Invalidation or expiry: candidate/program overwritten on preparation; baseline skipped when rows exist; splits reused unless removed; external installations reused on sentinel checks.
- Activation or effect: executable copy/configuration and baseline writes are wired; actual later behavior and successful provisioning are unobserved.
- Evidence limits: no generated workspace or dependency installation supplied; BIRD gold check accepts any nonempty `sol_sql`, not dataset-wide gold correctness.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-terminal-task
Label: Terminal benchmark task loop

Endpoints/progression: `TerminalBenchRunner.run` → `harbor run` subprocess → imported `HarnessAgent` → LiteLLM → bash through `environment.exec` → Harbor verifier → parsed result mapping and train trace copies. Principal: benchmark caller; task identity comes from split/task IDs, trial result supplies task name. Harbor owns concurrency/environment/verifier; stock candidate owns next model call and tool dispatch. Candidate context starts fresh with system instruction and task; messages then accumulate locally. Tool-output filtering keeps first/last halves at an 8000-character limit with an omission marker. Middle output is not delivered to the model or the saved message trace; files in the task environment could be reread through bash, but there is no automatic omitted-output retrieval pointer. This is code-directed context filtering, not model summarization (SRC-1, `benchmark.py`, `agent/templates/terminal_bench.py`).

> result = await environment.exec(command, timeout_sec=120)
> --- `agent/templates/terminal_bench.py`

> output = _truncate(output)
> --- `agent/templates/terminal_bench.py`

The default task loop is at most 80 model steps. Unknown tools and malformed JSON are returned as tool messages; model-call exceptions break the loop. Other execution exceptions are not locally caught around `environment.exec`. Text without tool calls means declared completion, not verified success. Runtime-client controls include model, environment provider, concurrency, timeout multiplier, import path and optional environment reasoning effort. The stock Terminal template does not read `AGENT_REASONING_EFFORT` in its LiteLLM call, so exporting it does not by itself demonstrate applied reasoning configuration. Reward extraction uses verifier `rewards.reward`; no verifier means `None`, while a missing reward key inside a verifier mapping defaults to zero. Subprocess timeouts are warned about and parsing may continue. Output discovery uses recently modified job directories; this is a freshness heuristic, not authenticated invocation/result pairing. Old jobs are pruned after parsing (SRC-1, same paths).

Decision roles/oracle: the model chooses commands/completion; Python dispatches; Harbor's external verifier decides reward against uninspected task references. No human approval is locally required for each bash call. Mode: bounded benchmark task. No product-change admission occurs in this task loop; its evidence feeds the separate coding-agent revision route.

- Immediate return: candidate populates token counts and optionally trace; runner returns task reward mapping, CLI prints mean and per-task results.
- Later read-back: train trace/result copies and CLI result mapping support subsequent diagnosis/gating; raw result preservation alone establishes no improvement.
- Delegated visibility: task model sees task, prompt and accumulated filtered tool messages; bash receives commands; provider/environment internals are uninspected.
- Selection predicate: explicit IDs override split lookup; `split=None` runs all; parsing chooses newest sufficiently recent job directory.
- Invalidation or expiry: task messages end with invocation; latest traces overwrite per-task files, first per-task baseline is preserved; old raw job directories pruned.
- Activation or effect: tool dispatch and result extraction are wired; actual sandbox effects, model behavior and verifier correctness are unobserved.
- Evidence limits: external Harbor/environment/provider not frozen; no run; local trace can omit middle tool output and suppress non-train candidate traces without suppressing all external logs.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-tau-task
Label: Tau benchmark message loop

Endpoints/progression: runner imports candidate → registers `custom_agent` factory under a process lock → constructs `TextRunConfig` → external `run_domain` → candidate `generate_next_message` → external `generate` with tools → next assistant message and state → simulation rewards. Principal: caller selecting domain/split/IDs; tau2 supplies tools, domain policy and input history. The candidate checks initial history types, copies it, appends incoming messages (expanding multi-tool results), prepends policy-bearing system text, and appends the returned assistant message. It has no local trimming/summarization or task executor: external tau2 advances tools/simulator/termination (SRC-1, `benchmark.py`, `agent/templates/tau_bench.py`).

> messages=[system, *state.messages],
> --- `agent/templates/tau_bench.py`

Decision roles/oracle: model chooses next message/tool calls; external tau2 executes and evaluates; `reward_info.reward` is consumed when present, otherwise zero. Expected domain outcomes/verifier implementation are uninspected. Mode: bounded named benchmark tasks. Concurrency/seed/model/user model are runtime-client inputs. Reasoning effort is read from environment, then `llm_args` can override generated kwargs. The registry lock covers factory registration only, not task isolation. In repeated in-process uses the registered factory is not replaced if already present; CLI/process usage avoids assuming a module hot-reload guarantee. No per-task human approval is implemented locally (SRC-1, same paths).

- Immediate return: assistant message plus mutable `HarnessState` per candidate call; task reward mapping per runner call.
- Later read-back: CLI persists returned mapping for later gate use; candidate history is ordinary task state, not a demonstrated cross-task learned store.
- Delegated visibility: tau2 gets configuration/candidate; model gets domain policy, full current message list and injected tool schemas.
- Selection predicate: configured domain, split and optional task IDs passed to `TextRunConfig`.
- Invalidation or expiry: local state lifetime follows external tau task lifecycle; external trace expiry/session retention uninspected.
- Activation or effect: next-message generation wiring is inspected; external tool effects and policy compliance unobserved.
- Evidence limits: external tau2 scheduler, tools, simulator and verifier not frozen; returned simulation set is not independently reconciled against requested full-test tasks.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-bird-session
Label: BIRD HTTP and ADK session loop

Endpoints/progression: BIRD runner selects JSONL tasks → starts harness system-agent, external user simulator and database HTTP services → waits for health → external orchestrator subprocess → `/init_session` and `/run_session` → ADK runner/model/tools → session response/state → orchestrator results → reward mapping. Owner: local code owns service lifecycle, session adapter and parsing; external orchestrator/ADK own scheduling and tool execution. User/task principal is caller-supplied `task_id`; session refs are keyed by `(mode, task_id)`, user ID becomes `user_{task_id}`, runners are cached per mode. Initialization is protected by an asyncio lock, but turn execution has no corresponding per-session lock in the wrapper. This establishes neither safe concurrent turns on one task nor cross-principal authorization (SRC-1, `benchmark.py`, `agent/helpers/bird_interact/bird_service.py`, `agent/helpers/bird_interact/bird_adk_runtime.py`).

> key = (mode, task_id)
> --- `agent/helpers/bird_interact/bird_adk_runtime.py:180-207`

State is supplied at initialization and held through ADK in-memory sessions. Reset creates a new reference; no local durable session backend or deletion of the superseded session is established. Each turn sends user content to `run_async`, serializes events, extracts final/fallback text and returns the session state. `_preview` truncates logged text/function responses; this affects returned diagnostic events, not evidence of trimming the model window. ADK's actual context assembly and external callbacks remain uninspected. In c-interact the wrapper resets `_submitted_this_phase` via an event before each turn (SRC-1, `agent/helpers/bird_interact/bird_adk_runtime.py`).

Mode a-interact registers externally provided SQL/schema/knowledge/clarification tools plus before/after callbacks. C-interact registers `ask_user` and `submit_sql` with separate callbacks. Budget/turn restrictions appear in instruction text, but local enforcement is delegated to those external callbacks. No local evidence establishes correct coin accounting or submission gating. Model configuration is built from external settings, omitting explicit zero temperature for GPT-5 names. Mode is selected by configuration/request, not model self-selection (SRC-1, `agent/templates/bird_interact.py`).

> tools=[FunctionTool(ask_user), FunctionTool(submit_sql)],
> --- `agent/templates/bird_interact.py`

Decision roles/oracle: model selects tools/SQL, simulator supplies user interaction, external evaluator produces `total_reward`; BIRD setup requires merged `sol_sql` somewhere in data. Gold SQL/test cases are externally obtained and absent here, so valid answer-oracle operation cannot be independently established. Mode: bounded SQL benchmark, with autonomous-tool and clarification-first variants. Services are stopped in `finally` after orchestrator execution, with terminate/kill fallback; startup failures stop already-started services. Orchestrator timeout may still yield parsable partial output. Error items map to `None`; selected missing IDs are filled only after successful output parsing (SRC-1, `benchmark.py`, `agent/helpers/bird_interact/setup.py`).

- Immediate return: HTTP session identity or turn response/state; runner returns parsed task rewards or empty mapping on no/invalid output.
- Later read-back: session state reaches later turns while service lives; train result/event copies reach outer diagnosis. Session persistence across service restart is not wired locally.
- Delegated visibility: orchestrator gets selected raw dataset tasks, services inherit configured environment; ADK receives candidate and user messages; external callbacks' complete context is uninspected.
- Selection predicate: explicit IDs or split; membership checked against `instance_id`, requested order restored; mode/task pair selects session.
- Invalidation or expiry: reset replaces session ref; service stop loses local in-memory session access; temporary input/output files cleaned on normal parse/error paths, stale temp files pruned later.
- Activation or effect: HTTP/ADK wiring, callback registration and score parsing inspected; actual SQL effects, budgets and correct outcomes unobserved.
- Evidence limits: external ADK/BIRD runtime, callback code, database and gold answers not frozen; logged event previews are not full model-visible transcripts.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-candidate-revision
Label: Failure-guided candidate revision

Endpoints/progression: train results/traces → coding-agent diagnosis → proposed edit to `agent/agent.py` and appended learnings → gate → requested commit or revert. Owner/proposer: external coding agent interpreting the program; human role: supplies setup/problem and may receive requests the agent cannot handle. Per-edit human approval is not required by the program, but the external coding-agent permission runtime is uninspected. Mode: bounded benchmark improvement; trigger: failing task evidence and repeated iteration. The guidance says inspect failures for prompt/tool causes, make one focused change, abandon a hypothesis after three failures and stop after five non-improving iterations. Terminal supplement proposes planning/bootstrap/verification techniques and numerical benefit estimates; these remain attributed design guidance, not measured results in this run (SRC-1, `program_templates/base.md`, `program_templates/terminal_bench.md`).

> Make one focused change per iteration. Smaller changes are easier to gate and easier to revert.
> --- `program_templates/base.md`

Proposed changes can alter the entire candidate implementation, including instructions, tool definitions, loop/setup and output processing; capability changes are therefore included, not only prompt tuning. Admission/rejection: software gate can return failure; external agent must then perform the requested revert, or commit/record on success. No atomic install, automatic code rollback or per-change human veto is implemented in the supplied scripts. The task reward is the external answer oracle; coding-model diagnosis is not itself an oracle. Persistent products are code/commits and requested natural-language learnings (SRC-1, `program_templates/base.md`, `program_templates/terminal_bench.md`).

Theory account: the shipped guidance formulates strategies and scope restrictions; the requested learnings include hypotheses, failure patterns and what worked. Code and localized instruction constants are inspectable/revisable, while model internals and actual diagnostic reasoning remain opaque. The program requests evidence-directed diagnosis, but it does not supply an observed formulated criticism identifying a challenged claim, adverse result, blame and resulting revision. Scores selecting candidates alone do not establish that richer criticism.

Theory-builder conditions 1–4:

- theory-builder condition 1 conclusion status: afforded

Whole instruction/rule units are localized and replaceable in candidate/program text; newly formulated hypothesis content is not supplied.

- theory-builder condition 2 conclusion status: claimed

The program requests content-guided editing; actual external coding-agent decisions depending on theory content are unobserved.

- theory-builder condition 3 conclusion status: claimed

Failure diagnosis and hypothesis revision are requested, but no actual content-directed criticism is supplied.

- theory-builder condition 4 conclusion status: claimed

Repeated attempts and append-only learnings are requested; criticism shaping a later round is unobserved.
- Addressability: instructions, Python functions and named constants can be edited separately; the assessment does not extend to distributed parameters or hidden coding-agent rationale.
- Persistence: code/commits and requested learnings can span iterations and restarts; their actual later consumption is unobserved.
- learning: uninspected — improved future capacity and attribution require outcome evidence beyond editable code, reward history and a proposed loop.
- Reflection: afforded — candidate behavior generates traces which the prescribed outer agent can interpret to revise the candidate; this is a dispositional representation-mediated feedback path, not demonstrated trace use.
- Reflective theory builder: uninspected — method texts are supplied but criticism/revision of the improvement method against its own operation is not demonstrated; ordinary candidate tuning does not establish it.
- Autonomous theory builder: claimed — the program assigns iterative operations to computation, but complete autonomous theory criticism and retained use are not established from a supplied run or the excluded runtime.
- Self-improvement: afforded — within the bounded improvement plane, over later benchmark iterations, objective is independently specifiable benchmark reward. Trace evidence can shape code changes, those changes can alter its candidate organization, and imports can give them live authority. These are standing pathways, not exercised causal links. Link 4 (subsequent behavior causally depending on the update) is unestablished, as is successful reward improvement; no exercised self-improvement attribution is made.

- Immediate return: proposed code change and natural-language diagnosis/learnings under the instructed procedure; exact external-agent return is uninspected.
- Later read-back: candidate imported by later benchmark invocation; program calls learnings the agent's memory, but actual later reads are unobserved.
- Delegated visibility: coding agent is directed to train evidence only; its actual filesystem/context access is unresolved.
- Selection predicate: train failures and recurring patterns under the program, with one hypothesis per iteration requested.
- Invalidation or expiry: failed gate requests `git checkout agent/agent.py`; three failed hypotheses request abandonment; five non-improving iterations request stop. These are not automatic script actions.
- Activation or effect: editable candidate-to-import path is wired; evidence-responsive edits and later behavioral change remain unobserved.
- Evidence limits: program supplies policy, not an executed optimizer; no learned revision, retained criticism, run trace or benefit comparison supplied.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

#### RT-RTE-gate-admission
Label: Regression gate and suite promotion

Endpoints/progression: `gating.py` → optional file guard → suite task rerun → full gate split rerun → compare prior best → rerun prior failing non-suite train tasks → promote new passes. Owner/decider: deterministic gate code; candidate proposals originate in [RT-RTE-candidate-revision](#rt-rte-candidate-revision). Configuration supplies threshold, benchmark and splits. Computational checks veto successful gate return; no per-task human decision is wired. Human versus software authorship of configuration is unresolved. Mode: bounded benchmark candidate comparison; triggers are explicit caller invocation and stored failing train tasks. Oracle: external runner rewards, pass threshold `>=0.5`; history supplies previous score, not independent ground truth (SRC-1, `gating.py`).

Suite accounting uses requested IDs as denominator and saves `last_results` even before final admission. Full test runs even after suite failure. Both checks must pass before promotion. Promotion reads last CLI results, identifies failing/non-suite tasks, reruns those on the train runner and adds passing returned IDs to a sorted suite set. This admits changed future evaluation coverage, not just an output log. Its software admission predicate is distinct from the coding agent's code proposal. There is no local suite demotion/rollback transaction; candidate rollback remains an external-agent instruction (SRC-1, `gating.py`).

> newly_fixed = sorted(tid for tid, r in recheck.items() if r is not None and r >= 0.5)
> --- `gating.py`

> suite["tasks"] = sorted(suite_set | set(newly_fixed))
> --- `gating.py`

The CLI writes `workspace/train_results.json` regardless of requested `--split`. The loader ignores its `split` metadata and consumes only `results`. Explicit task IDs can bypass split lookup in Terminal/BIRD runners. Thus the intended provenance of promotion seeds as full train results is a procedural contract, not a loader-enforced invariant. A mismatched result file can seed a different task set; external train task lookup may then fail or differ by benchmark (SRC-1, `benchmark.py`, `gating.py`).

- Immediate return: printed suite/test scores and exit 0 after all checks/promotion, or exit 1 for check failure; dependency exceptions can terminate outside those normal returns.
- Later read-back: saved suite tasks/last results shape later gate invocations; score history supplies maximum previous validation score.
- Delegated visibility: train/gate runners get selected task configuration; stdout exposes aggregate gate score to the coding agent even under the train-only diagnosis policy.
- Selection predicate: suite membership, configured threshold, best recorded score; promotion targets prior results below 0.5 or `None`, excluding suite members.
- Invalidation or expiry: suite membership grows on promotion; saved last results overwritten; candidate recovery requested externally, not performed by gate.
- Activation or effect: deterministic comparison and suite mutation wired; complete/valid benchmark evaluation and successful candidate installation unobserved.
- Evidence limits: externally defined rewards, mutable local history/configuration, possible empty results and unenforced result split provenance limit safety claims.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-iteration-record
Label: Commit-linked iteration append

Endpoints/progression: caller-supplied scores → `record.py` file guard including latest commit → current short commit lookup → append TSV row. Owner: recorder code; caller supplies numerical claims and is instructed to call only after passing gate and committing. It proposes no candidate itself. Admission/rejection: file guard can reject; numerical gate success, clean candidate state and exact evaluated revision are not independently verified. Caller/human approval is unresolved and no explicit human review is required. Mode: benchmark iteration accounting; oracle: none within recorder, because it trusts supplied numbers (SRC-1, `record.py`).

> def record(val_score: float, evals_passed: int, evals_total: int) -> int:
> --- `record.py`

> with open(RESULTS_FILE, "a") as f:
>         f.write(row)
> --- `record.py`

The row is behaviorally consequential because later gating computes its best score from this file. Guard failure returns 1; commit lookup failure gives `unknown`. There is no authenticated gate artifact, score recomputation, append rollback or local coordination lock. The row's timestamp/commit string is bookkeeping evidence, not execution authentication. Failed gate rollback and learnings updates remain outside recorder (SRC-1, `record.py`, `gating.py`).

- Immediate return: appended-row summary and success, or guard failure.
- Later read-back: `best_val_score()` reads nonempty score cells and uses maximum to constrain subsequent gate comparisons.
- Delegated visibility: no worker delegation; printed row is visible to caller, stored row to later gate.
- Selection predicate: explicit invocation with required CLI numerical arguments; optional file guard and last-commit diff.
- Invalidation or expiry: append-only implementation on normal use; no lifetime immutability or rollback enforcement for the file.
- Activation or effect: later best-score dependency is wired; trustworthy score provenance and actual future reads unobserved.
- Evidence limits: numerical arguments and Git label do not prove a completed gate, causal improvement or correspondence to the evaluated file contents.
- implementation conclusion status: wired
- operation conclusion status: uninspected

### Claims

#### RT-CLM-timeout-failure
Label: Timeout failure rule

Claimed operation: the program says every task without a verifier result within `per_task_timeout` counts as zero. Source: SRC-1, `program_templates/base.md`.

> **Per-task timeouts count as failures** — any task that does not produce a verifier result within `per_task_timeout` scores `0.0` in `val_score`.
> --- `program_templates/base.md`

Implementation scope: `None` values already present in result mappings score zero; this does not restore absent entries on every early-return path. First Terminal/BIRD split construction deliberately excludes `None` tasks. The claim is therefore supported as a scoring rule over returned mappings, not a complete-lifecycle timeout inclusion guarantee (SRC-1, `benchmark.py`, `prepare.py`; forcing case 2 and [RT-RTE-prepare-baseline](#rt-rte-prepare-baseline)).

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-program-coder
Label: Program to coding agent

Consumer: external coding agent. Channel: generated `PROGRAM.md` read as instructions. Force: requested procedure, edit scope, diagnosis policy, retry and stop rules; compliance depends on the external runtime/model, not local enforcement. Horizon: improvement iterations until requested stop, with actual reads/activation unobserved. Evidence: SRC-1, `prepare.py`, `program_templates/base.md`; [RT-OBJ-program](#rt-obj-program), [RT-RTE-candidate-revision](#rt-rte-candidate-revision).

#### RT-BAP-candidate-runtime
Label: Candidate to benchmark execution

Consumer: tau2 factory, Harbor imported agent, or BIRD adapter's `build_agent`. Channel: executable import of `agent.agent`, plus natural-language candidate instructions delivered to task models. Force: Python determines local loop/tool/context behavior; model-directed instructions request task behavior. Horizon: next benchmark processes/imports; BIRD caches built runners within service lifetime and tau imports/registry can retain in-process objects, so file edits alone do not guarantee hot replacement. Evidence: SRC-1, `benchmark.py`, `agent/helpers/bird_interact/bird_adk_runtime.py`, all three candidate templates; [RT-OBJ-agent-code](#rt-obj-agent-code) and [RT-OBJ-agent-instructions](#rt-obj-agent-instructions).

#### RT-BAP-history-gate
Label: Retained evaluation state to gate

Consumer: `run_gate` and its helper loaders. Channel: symbolic JSON suite/last CLI results and TSV score history. Force: fixed predicates choose reruns, promotion and pass/fail. Horizon: later invocations while files persist; reads do not authenticate provenance or mean reward correctness. Evidence: SRC-1, `gating.py`, `record.py`, `benchmark.py`; [RT-RTE-gate-admission](#rt-rte-gate-admission), [RT-RTE-iteration-record](#rt-rte-iteration-record). This is distinct from the instruction channel and from model interpretation of traces/learnings.

## Annotations

none
