---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Agent S runtime baseline: S3 desktop and coding execution, historical hierarchy, experience admission and offline rollout selection."
run-id: AAS-2026-10-16-agent-s-db6fee212353-01
reviewed-boundary: "15776a8dc659658b1963816ea006f7af1978e595"
---

# Agent S runtime report

## Runtime account

### Evidence and consequential work

Agent S turns a task and desktop observations into model-selected actions. The installed `agent_s` command selects S3; its driver closes the observation/action loop rather than merely returning a prediction. The SDK returns actions to a caller. Historical S1/S2 add manager/worker planning and persistent experience; S2.5 and S3 use a single worker architecture. Offline S3 scripts record rollouts, produce captions and select among completed trajectories. These are distinct control paths, not one uniformly hierarchical or continually learning runtime. SRC-1: `setup.py`, `gui_agents/s3/agents/agent_s.py`, `gui_agents/s2_5/agents/agent_s.py`, `gui_agents/s1/core/AgentS.py`, `gui_agents/s2/agents/agent_s.py`, `osworld_setup/s3/bbon/run_judge.py`.

> "agent_s=gui_agents.s3.cli_app:main",
> --- `setup.py`

All findings below are implementation or doctrine/design readings of SRC-1 at the frozen revision in [boundary](boundary.md). No supplied run, provider response, installed environment or causal experiment was inspected. Wiring establishes possible execution and actual code dependencies, not exercised behavior, accuracy, activation of advice or benefit. Added detailed coverage beyond the boundary's initial inspection includes S3 formatting/evaluation helpers, local controller, provider request construction, historical manager/worker handoffs, S2 embedding retrieval, and the caption/selection pipeline. All remain SRC-1, not new sources.

### Ordinary installed invocation

A human supplies `--task` or an interactive query and provider/grounding configuration. CLI construction creates an `OSWorldACI` object, optionally a `LocalEnv`, and `AgentS3`. The driver resets the agent for each query, obtains and resizes a local screenshot, encodes PNG bytes, then calls `predict`. Worker construction and prompt generation determine the available advertised methods. The natural-language policy asks for screenshot analysis, previous-action verification and one grounded method call. The model, not a symbolic planner, chooses the next action. Task identity is the instruction string and current worker state; there is no inspected per-action authorization identity distinct from the Python process and its desktop privileges. SRC-1: `gui_agents/s3/cli_app.py`, `gui_agents/s3/agents/worker.py`, `gui_agents/s3/memory/procedural_memory.py`.

[RT-RTE-desktop-loop](#rt-rte-desktop-loop) follows that invocation end to end. `AgentS3.predict` delegates to `Worker.generate_next_action`. The worker assigns the screenshot and original task to ACI, substitutes the task into its system prompt on the first turn, optionally obtains reflection on later turns, adds the text buffer and any code-agent return, and calls the generator. The response is appended to history. The last fenced code block is evaluated against the live ACI object. A click, for example, calls the grounding model with the referring expression and screenshot, parses two integers, rescales coordinates, and returns Python for the driver to execute. OCR/text-span grounding is another action translation path. The CLI then observes the screen again. SRC-1: `gui_agents/s3/agents/agent_s.py`, `gui_agents/s3/agents/worker.py`, `gui_agents/s3/agents/grounding.py`, `gui_agents/s3/utils/common_utils.py`.

The outer CLI is bounded to 15 prediction iterations. It recognizes done/fail, next and wait using substring tests on the returned string; done and fail both produce a completion dialog and break. Other returned code reaches `exec`. SIGINT offers pause/resume/exit, not per-action approval or undo. The API itself has no outer 15-step bound. Final output is desktop state plus streamed/logged plans and a terminal sentinel, not a separately verified task-result object. SRC-1: `gui_agents/s3/cli_app.py`.

### Controls, forcing cases and guarantee limits

Four forcing cases were selected because each changes where effects occur or what a reported result warrants. They are static source counterexamples, not executed exploits.

1. **Validation can execute the proposed action.** `CODE_VALID_FORMATTER` tests code by invoking `create_pyautogui_code`, whose implementation uses unrestricted `eval`. After formatting, the worker evaluates the accepted code again. An ACI method with immediate effects, such as `save_to_knowledge` or `call_code_agent`, can therefore run during checking and again during action creation. The single-action check is a regex count, not an AST capability restriction. Formatting retries can execute unsuccessful proposals too. See [RT-RTE-action-check](#rt-rte-action-check).
2. **Opt-in coding has an earlier effect boundary than outer GUI execution.** When a controller exists, `call_code_agent` synchronously executes model-produced Python/Bash through that controller before returning a sleep string. The optional local environment is disabled by default in the CLI, but OSWorld construction passes an environment with a controller. Local subprocesses inherit the ordinary host execution context; the Python branch has no timeout argument. See [RT-RTE-code-delegation](#rt-rte-code-delegation).
3. **A wrapper's success does not prove task success.** OpenClaw maps subprocess exit zero to success. Its `max_steps` becomes a history-length argument, not the CLI's fixed loop bound, and omitting the reflection flag cannot negate the CLI's default true value. See [RT-RTE-openclaw-bridge](#rt-rte-openclaw-bridge).
4. **Selection is not an online successor policy update.** Offline comparison uses saved captions and initial/final screenshots, selects a result directory, and records that choice. Benchmark result files determine which tasks enter the variance subset; model comparison itself receives no expected-answer oracle. See [RT-RTE-rollout-selection](#rt-rte-rollout-selection).

The capability surface includes GUI effects, application/file opening, spreadsheet modification, Python expression evaluation, and optional Python/Bash delegation. The current grant set is caller-specific: local coding requires `--enable_local_env` in the installed CLI, while OSWorld supplies a controller directly. Advertising fewer methods does not revoke Python evaluation capabilities. Actual OS permissions, service permissions, VM isolation, credentials and resource quotas belong to the deployed envelope and are not frozen. SRC-1: `gui_agents/s3/cli_app.py`, `gui_agents/s3/agents/worker.py`, `gui_agents/s3/agents/grounding.py`, `gui_agents/s3/utils/local_env.py`, `osworld_setup/s3/run.py`.

Load-bearing controls have different owners and strengths:

| Control | Owner and enforcement | Strength and coverage | External contract and limit | Status fields |
|---|---|---|---|---|
| One advertised API action | Prompt author plus formatter; regex count and trial evaluation | best effort; generator route only, not a capability sandbox; exhausted retries return the last response | Model compliance is needed; Python evaluation and controller calls are alternate effect paths | implementation conclusion status: wired; operation conclusion status: uninspected |
| GUI verification after coding | Prompt author requests reopening applications and checking results | policy; applies to the worker's decisions, not an enforced postcondition on `done` | Model must actually inspect the relevant artifact; no observed verification supplied | implementation conclusion status: wired; operation conclusion status: uninspected |
| 15 outer iterations | CLI `for` loop | invariant for loop iterations in this driver, not runtime duration or inner inference/execution count | Provider calls and delegated scripts must return; SDK and OSWorld callers have different bounds | implementation conclusion status: wired; operation conclusion status: uninspected |
| Permission dialog | Helper exists, but the execution branch calls `exec` directly | no claimed guarantee from the inspected call path; comment is not enforcement | Host permission mechanisms may constrain effects but are outside the capture | implementation conclusion status: wired; operation conclusion status: uninspected |
| Coding budget and subprocess timeout | CodeAgent loop and LocalController Bash call | protocol for coding rounds; 30-second Bash timeout is not a Python timeout or undo | Controller must implement execution/result contract; OSWorld controller internals are external | implementation conclusion status: wired; operation conclusion status: uninspected |

SRC-1: `gui_agents/s3/memory/procedural_memory.py`, `gui_agents/s3/utils/formatters.py`, `gui_agents/s3/utils/common_utils.py`, `gui_agents/s3/cli_app.py`, `gui_agents/s3/agents/code_agent.py`, `gui_agents/s3/utils/local_env.py`. Supporting passages are retained in the route records.

Recovery is local and partial. Model helpers retry provider exceptions three times; formatter feedback also retries three times but returns the last response after exhaustion. Worker action conversion errors become a sleep action. Code-controller exceptions become result dictionaries; there is no corresponding transaction rollback in those implementations. The driver does not thereby guarantee eventual completion or safe partial effects. Model versions and mutable endpoint limits are recorded separately in the components. SRC-1: `gui_agents/s3/utils/common_utils.py`, `gui_agents/s3/agents/worker.py`, `gui_agents/s3/agents/code_agent.py`, `gui_agents/s3/utils/local_env.py`.

### Material alternate loops and admission

[RT-RTE-osworld-driver](#rt-rte-osworld-driver) replaces local `exec` with external `env.step`, persists observations and trajectories, and calls an external evaluator. Its queue/process coordination and per-task exception handling are not human action approval. Historical S1/S2 interpose manager planning and worker subtask execution; S1 generally advances an existing queue on success and replans on failure, whereas S2 sets replanning on subtask completion too. A terminal subtask marker can be consumed internally without being sent to the environment. S2.5 is a nonhierarchical predecessor, not proof that historical manager behavior carries into S3. SRC-1: `osworld_setup/s3/run.py`, `osworld_setup/s3/lib_run_single.py`, `gui_agents/s1/core/AgentS.py`, `gui_agents/s2/agents/agent_s.py`, `gui_agents/s2_5/agents/agent_s.py`.

[RT-RTE-historical-experience](#rt-rte-historical-experience) identifies the S2 CLI admission mechanism and later consumers without replacing the memory analyst's inventory. The human supplies a task, not individual experience approvals. Model summaries are admitted by JSON key/branch rules, not a demonstrated factual validator. [RT-RTE-kb-bootstrap](#rt-rte-kb-bootstrap) is a separate initial-content admission route from release archives. The offline caption pipeline similarly admits model text into files for a later judge, not into worker weights. Product-source changes and provider-side model training are outside the traced automatic admission mechanisms; optional arbitrary code can change local files, but the inspected code route does not establish a designed self-modification/redeployment cycle. SRC-1: `gui_agents/s2/cli_app.py`, `gui_agents/s2/agents/agent_s.py`, `gui_agents/s2/agents/manager.py`, `gui_agents/utils.py`, `osworld_setup/s3/bbon/generate_facts.py`.

No observed benefit or exercised self-improvement is inferred from reflection, experience writing or selection. Task plans, captions and procedural instructions are described in their source-native roles here; this report does not establish a route that formulates and criticizes explanatory theories. Detailed memory revision and theory assessments remain for the specialists. Unobserved areas include endpoint internals, downloaded KB contents, actual controller deployments, provider-native capabilities not exercised by these text-call sites, and realized desktop/retrieval/selection outcomes.

## Shared records

### Components

#### RT-CMP-lmm-agent
Label: LMMAgent generation instances

Source-native identity: S3 `LMMAgent` instances backing worker generation, trajectory reflection, code generation/summary, text-span interpretation, behavior narration and comparative judgment. Their Python objects are symbolic client wrappers; the model component they call is distributed-parametric, stored at external model services, not in this repository. These roles may share engine parameters but have separate message contexts. Historical managers/workers likewise use generation services, with generation-specific wrappers. SRC-1: `gui_agents/s3/core/mllm.py`, `gui_agents/s3/core/engine.py`, `gui_agents/s3/agents/worker.py`, `gui_agents/s3/agents/code_agent.py`, `gui_agents/s3/agents/grounding.py`, `gui_agents/s3/bbon/behavior_narrator.py`, `gui_agents/s3/bbon/comparative_judge.py`, `gui_agents/s2/agents/manager.py`.

Parameter change during operation: no parameter-update request is present in the inspected generation calls; remote internal changes are uninspected. Exact version pinned: no immutable weights/digest; the CLI defaults to the dated model name `gpt-5-2025-08-07`, but callers can replace provider, name, URL and credentials. Mutable endpoint resolving to another model: possible; the client contract does not authenticate weights or fixed endpoint behavior. Provider internals and service retention are uninspected.

> self.llm_client.chat.completions.create(
>                 model=self.model,
>                 messages=messages,
> --- `gui_agents/s3/core/engine.py:57-59`

#### RT-CMP-grounding-model
Label: OSWorldACI grounding model

Source-native identity: `OSWorldACI.grounding_model`, a separately configured `LMMAgent`. Distributed-parametric service model; symbolic Python configuration and messages live in process memory, numerical weights remain external. Input is a screenshot and referring expression; output digits become coordinates. Parameter change during operation: no training/update operation in the inspected grounding route; endpoint internals uninspected. Exact version pinned: no, grounding model and URL are caller arguments. Mutable endpoint resolving to another model: possible; notably the HuggingFace adapter sends `model="tgi"`, so the configured display name does not pin the served model. SRC-1: `gui_agents/s3/agents/grounding.py`, `gui_agents/s3/cli_app.py`, `gui_agents/s3/core/engine.py`.

> self.llm_client.chat.completions.create(
>                 model="tgi",
>                 messages=messages,
> --- `gui_agents/s3/core/engine.py`

#### RT-CMP-embedding-engine
Label: Historical embedding engines

Source-native identity: S2 OpenAI/Gemini/Azure embedding engines selected during `AgentS2` construction. Distributed-parametric external encoders produce dense numerical representations cached in `embeddings.pkl`; cache creation is not model training. Parameter change during operation: no model-update request in inspected `get_embeddings` methods; provider internals uninspected. Exact version pinned: no weight identity; defaults are service names such as `text-embedding-3-small` and `text-embedding-004`, with configurable Azure endpoint/deployment. Mutable endpoint resolving to another model: not excluded by these clients. SRC-1: `gui_agents/s2/agents/agent_s.py`, `gui_agents/s2/core/engine.py`, `gui_agents/s2/core/knowledge.py`.

> response = client.embeddings.create(model=self.model, input=text)
> return np.array([data.embedding for data in response.data])
> --- `gui_agents/s2/core/engine.py`

### Operative objects

#### RT-OBJ-procedural-memory
Label: S3 PROCEDURAL_MEMORY worker policy

Source-native identity: `PROCEDURAL_MEMORY.construct_simple_worker_procedural_memory` and referenced reflection/code prompts. Natural-language instructions stored in shipped Python string literals and instantiated system messages. Method introspection supplies a symbolic API inventory whose signatures/docstrings are rendered into the natural-language policy. The policy shapes model decisions; the listing is not execution authorization. SRC-1: `gui_agents/s3/memory/procedural_memory.py`, `gui_agents/s3/agents/worker.py`.

> - ALWAYS verify code agent results with GUI actions before using agent.done(); NEVER trust code agent output alone. If verification or the code agent fails, use GUI actions to finish the task and only use agent.done() if results match expectations.
> --- `gui_agents/s3/memory/procedural_memory.py`

### Routes

#### RT-RTE-desktop-loop
Label: Installed S3 desktop task loop

Endpoints/progression: CLI task/query → screenshot → AgentS3 → Worker model decision → grounded code → local driver execution → next screenshot. The human admits the task; the model proposes/chooses the action; driver code chooses sentinel handling and execution. No answer oracle is supplied in this open-request mode. Decision policy is natural-language procedural guidance plus symbolic parsing/control flow. State includes worker/reflection histories, turn count, screenshots and ACI buffer; desktop effects belong to the process's GUI privileges. SRC-1: `gui_agents/s3/cli_app.py`, `gui_agents/s3/agents/agent_s.py`, `gui_agents/s3/agents/worker.py`, `gui_agents/s3/agents/grounding.py`.

- Immediate return: predict returns info and a list containing one executable string or sentinel; CLI streams execution and eventually returns without a verified success object.
- Later read-back: inapplicable — this route's ordinary histories are current-run state; separate code-result and experience routes describe retained delivery.
- Delegated visibility: grounding receives a screenshot/referring expression; reflector receives task and trajectory; neither receives an independent authorization principal.
- Selection predicate: worker model selects the next action; driver tests substrings for done/fail, next and wait before executing other code.
- Invalidation or expiry: agent reset replaces the Worker; 15 CLI iterations end the outer loop. ACI is constructed outside query resets, so its notes are not shown cleared by that reset.
- Activation or effect: code wires model output to desktop effects through eval/exec; actual actions and compliance are unobserved.
- Evidence limits: no session trace, model output or desktop permission configuration supplied; no task-success inference.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # Ask for permission before executing
> exec(code[0])
> time.sleep(1.0)
> --- `gui_agents/s3/cli_app.py`

Working-context control: `flush_messages` chooses by engine type. For anthropic/openai/gemini it removes older image content beyond the image budget while retaining text; other engines pop old generator user/assistant turns and old reflector user turns. System prompts and surviving tails remain. Removed content has no reload path in this function, though `worker_history` and `screenshot_inputs` still accumulate separately; they are not automatically model-visible simply because retained in RAM. Grounding resets per request. These are code-owned context controls, not a summarizing memory policy. SRC-1: `gui_agents/s3/agents/worker.py`, `gui_agents/s3/agents/grounding.py`.

> # Flush strategy for long-context models: keep all text, only keep latest images
> if engine_type in ["anthropic", "openai", "gemini"]:
> --- `gui_agents/s3/agents/worker.py`

#### RT-RTE-action-check
Label: Formatting and action evaluation

Endpoints/progression: generator response → single-action regex check and code-validity check → feedback retries → last response → worker action creation. The formatter owns acceptance attempts; the model proposes replacement content. This is formatting repair in open task execution, not an outcome oracle or bounded learning experiment. SRC-1: `gui_agents/s3/utils/formatters.py`, `gui_agents/s3/utils/common_utils.py`, `gui_agents/s3/agents/worker.py`.

- Immediate return: last response, including when formatting retries exhaust; action conversion returns evaluated ACI output or worker fallback sleep on error.
- Later read-back: inapplicable — temporary feedback messages are retry context, not a durable instruction revision.
- Delegated visibility: generator gets failed response and formatting feedback; trial evaluation has the live ACI and screenshot.
- Selection predicate: regex finds one agent call; trial evaluation must return non-None. These are not syntactic or semantic confinement checks.
- Invalidation or expiry: maximum three formatting attempts; no rollback of effects from trial evaluation.
- Activation or effect: validity checking itself evaluates Python; the worker evaluates again after response selection. Immediate ACI side effects can repeat before driver execution.
- Evidence limits: repetition follows call structure; exact count depends on retries/errors/model response. No target execution performed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> agent.assign_screenshot(obs)  # Necessary for grounding
> exec_code = eval(code)
> return exec_code
> --- `gui_agents/s3/utils/common_utils.py`

> def _attempt_code_creation(agent, code, obs):
>     """Attempts to create a pyautogui code snippet from the response code"""
>     try:
>         return create_pyautogui_code(agent, code, obs)
> --- `gui_agents/s3/utils/formatters.py`

Guarantee owner/enforcement: formatter functions, not the model provider. Guarantee strength: best effort. Covered path: worker generation. Alternate paths: arbitrary Python expressions in eval, effectful ACI methods, direct SDK/controller callers. Required external contract: generator must obey the advertised API for intended behavior. Implementation conclusion status is wired; operation conclusion status is uninspected. No safety invariant follows.

#### RT-RTE-code-delegation
Label: S3 controller-backed coding delegation

Endpoints/progression: worker's `call_code_agent` expression → ACI chooses explicit subtask or original task → reset CodeAgent context → model Python/Bash → controller execution/results → repeated model rounds → summary/history → ACI cached return → next worker invocation. CodeAgent owns next coding round, the model chooses scripts and DONE/FAIL, and the worker owns subsequent GUI verification/continuation. Open-request mode; controller status/stdout/stderr are feedback, not an expected-answer oracle. SRC-1: `gui_agents/s3/agents/grounding.py`, `gui_agents/s3/agents/code_agent.py`, `gui_agents/s3/utils/local_env.py`, `gui_agents/s3/agents/worker.py`.

- Immediate return: ACI returns a sleep string after coding effects already occurred; structured cached result includes summary, action/thought history, budget and completion reason.
- Later read-back: next worker turn receives the cached summary and action history, then clears the cached field. This is within-task cross-invocation delivery, not a cross-session store.
- Delegated visibility: initial task/subtask and screenshot enter a fresh coding context; execution results remain there for follow-up rounds. The outer worker gets action history and summary, not the complete controller-result dialogue.
- Selection predicate: model calls coding action; explicit task overrides original only by a non-None test, not semantic proof that it is a subtask.
- Invalidation or expiry: each execute resets coding context; budget defaults to 20 rounds; DONE/FAIL or exhaustion terminates; cached outer return is consumed once.
- Activation or effect: scripts execute through supplied controller; local Bash uses /bin/bash -lc and Python uses sys.executable -c. Files, packages and system configuration are within capability, subject to host permissions.
- Evidence limits: code summary is built from action/thought history, not the saved controller outputs; prompt requests about outputs do not establish faithful reporting. No observed script, successful verification or isolation evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> result = self.code_agent.execute(
>     task_to_execute, screenshot, self.env.controller
> )
> --- `gui_agents/s3/agents/grounding.py`

> if code_type == "bash":
>     result = env_controller.run_bash_script(code, timeout=30)
> elif code_type == "python":
>     result = env_controller.run_python_script(code)
> --- `gui_agents/s3/agents/code_agent.py`

Admission: task/delegation triggers a model-proposed script; software immediately admits recognized fenced Python/Bash to the controller. Human opt-in supplies local coding capability, not per-script review. Missing/unknown code and execution errors yield feedback or skip; model can stop/revise. No implemented file rollback is provided by this route. Procedural guidance requests original full-task fidelity and GUI verification; executed files persist in the environment. This can change external work products or arbitrary accessible files, but a system-specific self-redeployment route is not established.

Context isolation resembles a separate task frame: only selected inputs enter, and selected outputs escape. Unlike a pure frame, scripts mutate shared external files and desktop state; those effects survive context reset, and detailed execution feedback is omitted from the returned action history. SRC-1: `gui_agents/s3/agents/code_agent.py`, `gui_agents/s3/agents/worker.py`.

#### RT-RTE-openclaw-bridge
Label: OpenClaw subprocess bridge

Endpoints/progression: wrapper task argument → configured executable and CLI argv → subprocess → status dictionary/JSON or terminal message. Wrapper owns invocation, CLI owns task execution; OpenClaw orchestration is external. SRC-1: `integrations/openclaw/agent_s_wrapper.py`, `gui_agents/s3/cli_app.py`.

- Immediate return: wrapper status derives from process return code, executable lookup failure, exception or 600-second timeout.
- Later read-back: inapplicable — wrapper does not load retained agent knowledge.
- Delegated visibility: child process receives task, provider/model and optional grounding configuration; output streams rather than returning as captured task evidence.
- Selection predicate: AGENT_S_PATH or PATH executable; local-env flag is forwarded; max_steps is passed as max_trajectory_length.
- Invalidation or expiry: subprocess timeout is ten minutes; CLI retains its fixed 15 outer iterations regardless of wrapper max_steps.
- Activation or effect: subprocess inherits desktop access and executes CLI effects; zero exit is labelled success even though CLI fail/budget completion is not separately tested.
- Evidence limits: process completion is not task correctness; default missing grounding URL omits CLI-required grounding arguments. Wrapper no-reflection only omits a flag whose CLI default is true.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "--max_trajectory_length", str(max_steps),
> "--task", task,
> --- `integrations/openclaw/agent_s_wrapper.py`

#### RT-RTE-osworld-driver
Label: OSWorld environment task loop

Endpoints/progression: process task queue/config instruction → DesktopEnv reset/observation → AgentS3 predict → env.step → trajectory/screenshot storage → env.evaluate/result.txt. Driver owns coordination, environment owns actual action execution and evaluator semantics, worker owns next action. Benchmark mode uses externally defined tasks, not open interactive queries. Evaluation outcome is supplied by external env.evaluate; its reference conditions are not captured. SRC-1: `osworld_setup/s3/run.py`, `osworld_setup/s3/lib_run_single.py`.

- Immediate return: updated observation/reward/done per action; final evaluation score appended to shared scores and result.txt.
- Later read-back: recorded screenshots/traj.jsonl feed the offline caption/selection route; ordinary worker prediction does not automatically ingest these files.
- Delegated visibility: worker receives instruction and observation; controller is available via ACI independently of env.step.
- Selection predicate: queued domain/task identifier loads a config; done or max_steps bounds outer loop.
- Invalidation or expiry: env.reset per task; agent reset recreates worker. Process-level task exceptions are logged and appended to trajectory; they do not restore completed actions.
- Activation or effect: env.step executes returned strings; coding delegation can execute controller operations earlier in predict.
- Evidence limits: external DesktopEnv/VM/provider/evaluation internals and actual rollout directories unavailable; no deployed isolation or score correctness conclusion.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> obs, reward, done, info = env.step(action, args.sleep_after_execution)
> --- `osworld_setup/s3/lib_run_single.py`

> result = env.evaluate()
> logger.info("Result: %.2f", result)
> scores.append(result)
> --- `osworld_setup/s3/lib_run_single.py`

#### RT-RTE-historical-experience
Label: S2 hierarchical execution and experience admission

Endpoints/progression: S2 CLI → manager queue/replanning → worker subtask → GUI driver → trajectory update → model summary → JSON → later manager/worker retrieval. Manager proposes subtask decomposition; agent control code advances/replans on worker DONE/FAIL. S1 has the related but different completion policy described above. SRC-1: `gui_agents/s2/cli_app.py`, `gui_agents/s2/agents/agent_s.py`, `gui_agents/s2/agents/manager.py`, `gui_agents/s2/agents/worker.py`, `gui_agents/s1/core/AgentS.py`.

- Immediate return: executable actions and metadata, plus updated subtask trajectory string from the episodic updater.
- Later read-back: narrative JSON is retrieved for initial planning; episodic JSON is retrieved when subtask experience is enabled at worker initialization. S2 cosine-similarity retrieval ranks embedded keys and deliberately skips a top key identical to the query.
- Delegated visibility: subtask worker gets original task, subtask description, future/completed tasks and selected experience; reset discards its prior frame. Manager receives completed/failed/remaining subtask state.
- Selection predicate: CLI calls narrative update on done/fail branch; episodic updates follow ordinary executed actions and use Start/Done boundaries. Writes add only previously unseen search/subtask keys. Retrieval is dense-key similarity, not demonstrated truth checking.
- Invalidation or expiry: JSON survives worker resets; existing keys are reused rather than revised by these updater branches. Filesystem replacement/deletion and exceptions constrain persistence; no per-content expiry here.
- Activation or effect: summaries are appended to later system-prompt instructions as optional guidance; delivery is wired, reliance and improvement are not observed.
- Evidence limits: source establishes caller/update/consumer chain, not correctness of unseen summaries, actual recall, useful learning or exhaustive memory inventory. The memory analyst owns detailed store/revision findings.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if self.search_query not in reflections:
>     reflection = self.planner.summarize_narrative(trajectory)
>     reflections[self.search_query] = reflection
> --- `gui_agents/s2/agents/agent_s.py`

> instruction += f"\nYou may refer to some retrieved knowledge if you think they are useful.{integrated_knowledge}"
> --- `gui_agents/s2/agents/manager.py`

Admission account: observed-task trajectory is supplied by the CLI; manager summary model proposes text under summarization prompts; key-existence tests admit/reuse content and JSON writes persist it. Humans supply tasks, not per-summary approval. Model or software can fail to produce/write a summary; there is no separate rejection gate for truth or task success in these updater branches. Existing key preservation prevents replacement here, not corruption elsewhere. No transactional rollback/experience revision is established. Operating mode is ordinary task execution with retrospective summarization; no expected answer is supplied to summary admission. SRC-1: `gui_agents/s2/cli_app.py`, `gui_agents/s2/agents/agent_s.py`, `gui_agents/s2/agents/manager.py`.

#### RT-RTE-kb-bootstrap
Label: Historical default KB bootstrap

Endpoints/progression: use_default_kb plus missing platform directory → release URL → HTTP response → ZIP extraction → historical KB consumers. Caller selects release/version/platform; repository release content supplies initial knowledge. SRC-1: `gui_agents/s2/agents/agent_s.py`, `gui_agents/utils.py`.

- Immediate return: extraction creates files under local_kb_path, or HTTP/platform failure raises.
- Later read-back: historical knowledge loaders can consume the extracted stores; precise initial contents are unavailable.
- Delegated visibility: downloader receives version/release/platform/path, not an agent dialogue or per-entry human judgment.
- Selection predicate: bootstrap requested and platform KB directory missing; asset name combines generation and OS.
- Invalidation or expiry: existing directory skips download; source message instructs deletion for re-download, which wipes local experience.
- Activation or effect: external archive contents become available to historical KB loading; particular instructions and effects uninspected.
- Evidence limits: release assets are outside frozen contents; extraction is not an authenticated content/quality assessment.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> with zipfile.ZipFile(zip_data, "r") as zip_ref:
>     zip_ref.extractall(download_dir)
> --- `gui_agents/utils.py`

Admission: caller requests a named bundle; HTTP 200 and ZIP parsing admit it. No model proposes this initial text in the inspected downloader; bundle authorship is external. Rejection covers unsupported OS, non-200 and parse failures, not semantic validity. Recovery is manual deletion/re-download, not versioned content rollback. No answer oracle or improvement experiment is involved.

#### RT-RTE-rollout-selection
Label: Offline caption generation and comparative rollout selection

Endpoints/progression: saved screenshot pairs and exec_code → BehaviorNarrator → fact_captions.jsonl → fact_answer loading plus initial/final screenshots → ComparativeJudge → range-checked result directory → output JSON and comparative evaluation. Script code owns candidate/task selection and persistence; narrator proposes captions; judge model chooses among trajectories; integer/range handling can yield no selection. SRC-1: `osworld_setup/s3/bbon/generate_facts.py`, `gui_agents/s3/bbon/behavior_narrator.py`, `osworld_setup/s3/bbon/utils.py`, `gui_agents/s3/bbon/comparative_judge.py`, `osworld_setup/s3/bbon/run_judge.py`.

- Immediate return: narrator fact/thought fields and comparative answer/thoughts/selected directory; completed selection records persist in output JSON.
- Later read-back: load_facts reads only fact_answer from saved JSONL; run_judge loads prior output and skips recorded tasks. Generated captions are consumed by a later judge, not automatically by the GUI worker.
- Delegated visibility: narrator gets before/after images, action and optional marked/zoomed views; judge gets caption answers and available initial/final screenshot pairs, not full narrator thought records or every screenshot/action/result.
- Selection predicate: tasks common to result directories with differing parsed result.txt values form the variance set; model answer must parse to integer within candidate range. Existing selection entries are skipped.
- Invalidation or expiry: missing/invalid data can omit captions, image pairs or tasks; failed captions are skipped and only successful results saved. No semantic invalidation/expiry of prior recorded judgments is shown.
- Activation or effect: writes model-produced descriptions and selects a completed rollout for scoring/reporting; no online policy install, action replay or weight update in the inspected route.
- Evidence limits: actual files and external evaluator criteria unavailable; captions labelled facts remain model interpretations. Selection correctness and performance advantage unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if 1 <= judge_choice <= num_trajectories:
>     selected_trajectory = result_dirs[judge_choice - 1]
> else:
>     selected_trajectory = None
> --- `gui_agents/s3/bbon/comparative_judge.py`

> # classification
> if all(r == results[0] for r in results):
>     constant_tasks.append(domain_task)
>     constant_tasks_scores.append(results[0])
> else:
>     variance_tasks.append(domain_task)
> --- `osworld_setup/s3/bbon/utils.py`

Admission and oracle account: source prompts guide captions and comparative judgment. Successful narrator responses are admitted automatically; caption exceptions are omitted, not reviewed for truth. DONE/FAIL actions produce fixed captions stating that the agent indicated completion/failure. Comparative caller persists model choice after integer parsing, without human per-choice veto. The external evaluator's result.txt outcomes act as reference outcomes for variance filtering and retrospective scoring, not as supplied expected answers inside the comparative model messages. Mode is offline multiple-rollout comparison, not a live self-improvement curriculum. Existing outputs can be manually replaced, but no automatic rollback/revision loop is established. SRC-1: `gui_agents/s3/bbon/behavior_narrator.py`, `gui_agents/s3/bbon/comparative_judge.py`, `osworld_setup/s3/bbon/run_judge.py`, `osworld_setup/s3/bbon/utils.py`.

### Claims

#### RT-CLM-gui-verification
Label: Required GUI verification after code execution

Claimed operation: worker instructions require GUI verification and reopening the application before declaring completion after coding. This is an instruction claim, not an enforced postcondition. Its passage is retained in [RT-OBJ-procedural-memory](#rt-obj-procedural-memory). The direct `done` method returns DONE without checking that history. SRC-1: `gui_agents/s3/memory/procedural_memory.py`, `gui_agents/s3/agents/grounding.py`.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-worker-policy
Label: Worker procedural guidance to action choice

Consumer: generator model. Channel: system prompt assembled from shipped instructions, task and advertised methods. Force: natural-language policy requesting behavior, backed by partial formatting checks rather than compliance proof. Horizon: current Worker lifetime; shipped source persists across tasks, instantiated context is reset. [RT-OBJ-procedural-memory](#rt-obj-procedural-memory) supplies the policy passage; [RT-RTE-desktop-loop](#rt-rte-desktop-loop) supplies execution routing. SRC-1: `gui_agents/s3/agents/worker.py`, `gui_agents/s3/memory/procedural_memory.py`.

#### RT-BAP-code-return
Label: Code-agent return to next worker decision

Consumer: worker generator model. Channel: next user message with completion reason, summary and action history. Force: advisory evidence for subsequent GUI action selection; no enforced acceptance or truth guarantee. Horizon: next invocation then accumulated worker text history, subject to context policy/reset. Source passage establishes one-shot delivery, not successful verification. SRC-1: `gui_agents/s3/agents/worker.py`.

> # Reset the code agent result after adding it to context
> self.grounding_agent.last_code_agent_result = None
> --- `gui_agents/s3/agents/worker.py`

## Annotations

none
