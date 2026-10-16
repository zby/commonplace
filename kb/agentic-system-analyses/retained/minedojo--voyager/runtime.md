---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Voyager runtime baseline tracing Minecraft learning, inference, manual decisions and direct JavaScript execution at the frozen commit."
run-id: AAS-2026-10-14-voyager-f16a44a0cfe3-01
reviewed-boundary: "55e45a880755d0c8c66ca7fb5fe7962ac8974f89"
---

# Voyager runtime report

## Runtime account

### Scope and evidence

Voyager is a Python-controlled Minecraft agent that proposes tasks, generates JavaScript, executes it through a Node/Mineflayer bridge, judges task completion, and admits successful programs for later use. The shipped entry paths are `Voyager.learn()`, checkpoint resume, `decompose_task()` and `inference()`, and public `reset`/`step`/`rollout` operations (SRC-1, `README.md`, `voyager/voyager.py`). The ordinary learning loop is [RT-RTE-learning-loop](#rt-rte-learning-loop); the executor is [RT-RTE-environment-step](#rt-rte-environment-step). These are nested sequential loops, not independently delegated worker agents. The caller controls configuration and initial world access; Python owns progression, model calls own the requested decisions, and Node executes effects.

All findings below use SRC-1 at the boundary revision. Source inspection establishes wiring, not actual activation, successful operation, safety or performance. No target execution, model request or experiment was performed. Added inspection beyond the boundary's initial scope includes the complete action, curriculum and critic implementations, the complete bridge and execution server, `voyager/control_primitives/mineBlock.js`, `voyager/control_primitives/__init__.py`, `voyager/env/mineflayer/lib/observation/base.js`, `voyager/utils/record_utils.py`, `voyager/env/mineflayer/package.json` and complete action, critic and skill prompt bodies. These supply implementation or doctrine/design evidence only. The bundled collection plugin's internal algorithms and other concrete primitives were not exhaustively traced; this prevents a guarantee about all individual Minecraft operations, not identification of the executor's authority.

### Ordinary invocation and context boundary

The README supplies `Voyager(azure_login=..., openai_api_key=...).learn()`. A caller can instead supply an existing Minecraft port. Constructor configuration defaults the action, curriculum and critic roles to `gpt-4`, and QA and description generation to `gpt-3.5-turbo`; it creates separate chat clients, stores the API key in the Python environment, creates the bridge, and initializes checkpoint-backed agents and recorder (SRC-1, `README.md`, `voyager/voyager.py`). The model roles and their parameter/version limits are [RT-CMP-action-llm](#rt-cmp-action-llm), [RT-CMP-curriculum-llm](#rt-cmp-curriculum-llm), [RT-CMP-qa-llm](#rt-cmp-qa-llm), [RT-CMP-critic-llm](#rt-cmp-critic-llm), [RT-CMP-skill-llm](#rt-cmp-skill-llm) and [RT-CMP-openai-embeddings](#rt-cmp-openai-embeddings).

Fresh learning hard-resets inventory; resume soft-resets it. An empty environment step establishes `last_events`. The curriculum chooses task/context; initially auto mode hardcodes “Mine 1 wood log.” Inventory pressure can force chest-management tasks before model/manual dispatch. Otherwise auto mode requests and parses a task, then obtains task context from the QA cache or QA model. Manual mode asks a human for task/context confirmation (SRC-1, `voyager/agents/curriculum.py`). Thus even manual curriculum mode does not exclusively determine every task. See [RT-RTE-task-selection](#rt-rte-task-selection).

Each rollout resets its iteration counter, task, context and conversation diagnostics; optionally soft-resets the environment; issues time/difficulty commands; retrieves skill code by context; and renders one system message plus one human observation message. Each valid action response is parsed into function declarations and an invocation of the last async function taking `bot`. The parser does not admit arbitrary top-level statements from the response, but function bodies remain unrestricted JavaScript (SRC-1, `voyager/voyager.py`, `voyager/agents/action.py`). The operative result is [RT-OBJ-program-code](#rt-obj-program-code).

The action model does not receive an accumulating transcript. After an executed action, Python replaces both messages with a newly rendered system message and a human message containing current observations, last program code, context and critic feedback. `conversations` retains diagnostic triples but is not the next action call's message list. Parse failures keep the prior messages. Skill retrieval is refreshed using task context plus a code-rule extraction of unmet crafting/mining requirements from chat, not a general model summary (SRC-1, `voyager/voyager.py`, `voyager/agents/action.py`).

> self.last_events = copy.deepcopy(events)
> self.messages = [system_message, human_message]
> --- `voyager/voyager.py`

The curriculum separately filters inventory by a core-item regex during warmup, reveals observation categories at progress thresholds, probabilistically includes some categories thereafter, and caps included QA pairs at five after filtering selected unsuitable answers. Critic and skill-description calls are separate short contexts, not action history continuations. These are code-selected contexts: full action transcripts and most raw event detail remain outside model windows; current observations, last code and critique escape into the next action frame. Durable skill, QA and chest data have reload paths, whereas old action turns have no automatic transcript-reload path in the inspected driver. This resembles separate call frames with selected returns, but the model receives copied text rather than executable references to out-of-window content (SRC-1, `voyager/agents/action.py`, `voyager/agents/curriculum.py`, `voyager/agents/critic.py`, `voyager/agents/skill.py`).

### Execution, judgment and admission

Python posts code and **all** loaded skill code plus primitives to Node. The retrieved top-k subset controls prompt supply, not the executable library. Node evaluates the combined strings in the server process, with the bot, imports and local helpers in scope; observations accumulate events and return a JSON string, which the bridge decodes. Node also performs its own recovery/assistance actions, including unsticking by teleport and recovering crafting tables/furnaces or giving selected items. Thus the final game state is not exclusively a generated program's unaided accomplishment (SRC-1, `voyager/agents/skill.py`, `voyager/env/bridge.py`, `voyager/env/mineflayer/index.js`, `voyager/env/mineflayer/lib/observation/base.js`).

> await eval("(async () => {" + programs + "\n" + code + "})()");
> --- `voyager/env/mineflayer/index.js`

Python records events, updates chest memory, and calls the critic. Auto critic receives a selected final-state observation, task/context and chest description, not the program or a trusted expected-result file. An `onError` event makes its human-message renderer return `None`; auto critic then returns false without a model judgment. Otherwise it parses `success` and `critique`, retrying malformed replies and eventually returning failure. Manual critic instead asks a human and can approve even when the rendered message was `None` (SRC-1, `voyager/agents/critic.py`). This falsifies a system-wide claim that execution errors always veto success. See [RT-RTE-task-judgment](#rt-rte-task-judgment).

The loop retries until success or the configured action-attempt limit. A successful learning rollout supplies program name/code for skill admission; the manager generates a description, embeds it, and writes code, description, JSON and vector state. It skips deposit tasks. Name collisions overwrite the active map/index entry while saving version-suffixed text files. There is no per-skill human approval in this auto learning branch. `inference()` shares rollout and progress updates but does not call `add_new_skill()` (SRC-1, `voyager/voyager.py`, `voyager/agents/skill.py`). See [RT-RTE-skill-admission](#rt-rte-skill-admission) and [RT-BAP-skill-execution](#rt-bap-skill-execution). Memory revisions and detailed retained-state provenance belong to the memory analyst; this account identifies runtime admission and consumer boundaries.

### Alternate and forcing routes

Four source-inspected cases bound the conclusions; these are static forcing cases, not executed tests.

1. **Manual decisions:** task and critic modes are independently configurable. Hardcoded curriculum overrides precede manual dispatch; human critic confirmation replaces automatic judgment. This narrows any assertion of fully model-controlled task selection or universal auto-critic error rejection (SRC-1, `voyager/agents/curriculum.py`, `voyager/agents/critic.py`).
2. **Inference with a supplied library:** caller-selected `skill_library_dir` forces skill-manager reload independently of `resume`, allowing distributed learned state into action prompts and execution. Decomposition calls the curriculum model, or the caller directly supplies subgoals. The inference loop has neither the learning loop's global recorder limit nor its enclosing rollout-exception recovery. Since progress is the count of unique completed task strings, repeated failure need not advance it, and duplicate subgoals can also prevent advancement. There is no unconditional inference termination guarantee (SRC-1, `voyager/voyager.py`, `voyager/agents/curriculum.py`). See [RT-RTE-task-inference](#rt-rte-task-inference).
3. **Direct environment invocation:** `VoyagerEnv.step(code, programs)` and Node `/step` accept strings without the action parser, curriculum or critic. They can execute code even when no model-generated action or skill-admission decision occurs. The server has a single global bot, no visible request principal/authorization middleware in this file, and `app.listen(PORT, ...)` does not specify a loopback bind address. Python's default destination is loopback, which does not itself isolate the listener. Deployment network restrictions are not evidenced here (SRC-1, `voyager/env/bridge.py`, `voyager/env/mineflayer/index.js`).
4. **Direct API versus prescribed primitives:** the prompt forbids direct digging/crafting, infinite loops and event listeners. The parser checks syntax/function shape, not these prohibitions. Direct bot APIs or Node capabilities inside accepted function bodies bypass primitive-specific checks. For example, `mineBlock` has its own 32-block search and missing-block failure count, but neither protects arbitrary generated functions nor the direct endpoint (SRC-1, `voyager/prompts/action_template.txt`, `voyager/agents/action.py`, `voyager/control_primitives/mineBlock.js`, `voyager/env/mineflayer/index.js`).

### Guarantees and recovery envelope

The strongest localized invariant is the **action parser's output shape**, owned by `ActionAgent.process_ai_message`: successful parse results consist of generated function declarations and a call to an async single-`bot` main. Its implementation conclusion status is wired; operation conclusion status is uninspected. The guarantee strength is invariant for this transformation, not for valid behavior. It relies on Babel parsing/generation and the Python–JavaScript integration contract. It does not cover direct bridge requests, arbitrary function-body effects, retained-library contents or runtime completion (SRC-1, `voyager/agents/action.py`).

> program_code = "\n\n".join(function["body"] for function in functions)
> exec_code = f"await {main_function['name']}(bot);"
> --- `voyager/agents/action.py`

The **learning skill-admission condition** is a protocol owned by the learning driver: `info['success']` gates its call to the manager. It guarantees conditional invocation, not truthful success, artifact safety or successful future reuse. Manual judgment and direct calls to the public manager are alternate paths; the manager itself does not inspect `info['success']`. Required external contracts include trustworthy observations and the selected critic's task judgment. Implementation conclusion status: wired. Operation conclusion status: uninspected (SRC-1, `voyager/voyager.py`, `voyager/agents/skill.py`).

The **bounded action retry policy**, owned by `Voyager.step`, stops on success or `action_agent_task_max_retries` after completed steps. Guarantee strength: protocol. Implementation conclusion status: wired. Operation conclusion status: uninspected. It does not bound a hanging action/model request, curriculum retries outside rollout, repeated inference rollouts or all recovery paths. The bridge supplies HTTP timeouts, but timeout is not proof of cancellation of running JavaScript. `learn()` catches rollout exceptions, waits, resets using last inventory/equipment/position, marks the task failed and continues. Optional failed-placement recovery restores selected placement-related state, not an atomic world rollback. Skill admission and curriculum proposal occur outside that rollout try block. `check_process()` initializes a retry counter without incrementing it, so its apparent restart limit does not establish bounded restart attempts (SRC-1, `voyager/voyager.py`, `voyager/env/bridge.py`).

Even the parse-failure path has a limit: it records an empty event list, while `EventRecorder.record` indexes the first event if `init_position` is unset. A first parse failure can therefore throw rather than merely consume an action retry. This is a source-supported countercase to unconditional graceful retry, not an observed failure (SRC-1, `voyager/voyager.py`, `voyager/utils/record_utils.py`).

The **primitive-use/no-infinite-loop instructions** have policy strength only; compliance is unobserved. They are owned by the action prompt, with no equivalent enforcement in the inspected parser/evaluator. The capability surface includes Node lexical/process facilities, bot APIs, loaded plugins and game commands; the current grant set depends on reachable server interfaces, bot/game permissions and host process permissions. No explicit sandbox or capability reduction is applied around the inspected `eval`. Deployed isolation is uninspected, not proved absent: external OS/network containment could exist. The README asks users to enable cheats, and the shipped server issues `/give`, `/tp` and gamerule commands. A realistic effect boundary therefore includes privileged game assistance and potentially host-process resources, not just the six advertised primitive functions (SRC-1, `README.md`, `voyager/prompts/action_template.txt`, `voyager/env/mineflayer/index.js`).

> 9) Do not write infinite loops or recursive functions.
> --- `voyager/prompts/action_template.txt`

Packaging fixes the analyzed source but not provider weights or every dependency version. The Node manifest includes the local collection plugin and version ranges for Mineflayer/plugins. No per-transaction audit principal, concurrency scheduler or durable execution queue is established by the inspected single-bot HTTP handler. Console logs, stored event JSON and diagnostic conversations expose some execution evidence, but do not supply an independently observed run here (SRC-1, `voyager/env/mineflayer/package.json`, `voyager/env/mineflayer/index.js`, `voyager/utils/record_utils.py`).

## Shared records

### Components

#### RT-CMP-action-llm
Label: ActionAgent.llm

Source-native identity: `ActionAgent.llm`, configured through `action_agent_model_name` (default `gpt-4`). Representational form: distributed-parametric. Storage substrate: external OpenAI model service behind LangChain `ChatOpenAI`; client object in Python memory. Proposes program text from the two-message action context. Parameters changing during operation: no weight-update operation is wired in this client; provider internals uninspected. Exact version pinned: no immutable weight/version identity is supplied. Mutable endpoint: configurable model-name resolution may change externally. Evidence: SRC-1, `voyager/agents/action.py`, `voyager/voyager.py`.

> self.llm = ChatOpenAI(
>     model_name=model_name,
>     temperature=temperature,
>     request_timeout=request_timout,
> )
> --- `voyager/agents/action.py`

#### RT-CMP-curriculum-llm
Label: CurriculumAgent.llm

Source-native identity: `CurriculumAgent.llm`, default `gpt-4` through the driver. Representational form: distributed-parametric. Storage substrate: external OpenAI service with a Python ChatOpenAI client. Proposes tasks and decompositions. Parameter mutation: no weight-update path in the inspected client; internals uninspected. Exact version pinned: no. Mutable endpoint: model-name service resolution can change, and callers can configure the name. Evidence: SRC-1, `voyager/agents/curriculum.py`, `voyager/voyager.py`.

#### RT-CMP-qa-llm
Label: CurriculumAgent.qa_llm

Source-native identity: `CurriculumAgent.qa_llm`, driver default `gpt-3.5-turbo`. Representational form: distributed-parametric. Storage substrate: external OpenAI service; Python client. Generates questions and answers, not independently verified answer keys. Parameter mutation: no client weight update; provider internals uninspected. Exact version pinned: no. Mutable endpoint: configurable alias can resolve differently. Evidence: SRC-1, `voyager/agents/curriculum.py`, `voyager/voyager.py`.

#### RT-CMP-critic-llm
Label: CriticAgent.llm

Source-native identity: `CriticAgent.llm`, driver default `gpt-4`. Representational form: distributed-parametric. Storage substrate: external OpenAI service; Python client. Supplies automatic success/critique judgment. Parameter mutation: no client weight-update operation; internals uninspected. Exact version pinned: no. Mutable endpoint: configurable alias can resolve differently. Evidence: SRC-1, `voyager/agents/critic.py`, `voyager/voyager.py`.

#### RT-CMP-skill-llm
Label: SkillManager.llm

Source-native identity: `SkillManager.llm`, driver default `gpt-3.5-turbo`. Representational form: distributed-parametric. Storage substrate: external OpenAI service; Python client. Generates skill descriptions. Parameter mutation: no client weight-update path; internals uninspected. Exact version pinned: no. Mutable endpoint: configurable model-name resolution can change. Evidence: SRC-1, `voyager/agents/skill.py`, `voyager/voyager.py`.

#### RT-CMP-openai-embeddings
Label: OpenAIEmbeddings

Source-native identity: `OpenAIEmbeddings()` instances used by skill and curriculum Chroma stores. Representational form: distributed-parametric. Storage substrate: external embedding service through LangChain; derived vectors persisted by Chroma locally. Parameter mutation: no training/update request wired here; service internals uninspected. Exact version pinned: not by these constructors. Mutable endpoint: external defaults/version resolution remain uninspected, so substitution cannot be excluded. This is distinct from the retained vectors produced by the service. Evidence: SRC-1, `voyager/agents/skill.py`, `voyager/agents/curriculum.py`.

> embedding_function=OpenAIEmbeddings(),
> persist_directory=f"{ckpt_dir}/skill/vectordb",
> --- `voyager/agents/skill.py`

### Operative objects

#### RT-OBJ-program-code
Label: program_code

Source-native identity: action-parser `program_code`, joined generated function declarations; not the model's explanatory prose or its whole fenced response. Representational form: symbolic JavaScript under Babel and Node rules. Storage substrate: Python strings, HTTP JSON, Node strings; successful learning admission later stores a copy in the skill library. The distinct `exec_code` calls the selected main function. Its consumer and selection are [RT-RTE-environment-step](#rt-rte-environment-step); admission is [RT-RTE-skill-admission](#rt-rte-skill-admission). Evidence: SRC-1, `voyager/agents/action.py`, `voyager/voyager.py`; the parser quote in the runtime account supplies the retained passage.

#### RT-OBJ-control-primitives
Label: control_primitives

Source-native identity: JavaScript files loaded by `load_control_primitives()`. Representational form: symbolic executable code. Storage substrate: package files loaded into Python strings and supplied to Node. These are not the separately loaded natural-language/API context descriptions used in the action prompt. The loader defaults to all `.js` files in the primitive directory, including assistance helpers not in the six-function base prompt list. The sampled `mineBlock` delegates collection to the bundled collection plugin; its bounds do not constrain all callers. Evidence: SRC-1, `voyager/control_primitives/__init__.py`, `voyager/control_primitives/mineBlock.js`, `voyager/agents/action.py`, `voyager/agents/skill.py`.

> await bot.collectBlock.collect(targets, {
>     ignoreNoPath: true,
>     count: count,
> });
> --- `voyager/control_primitives/mineBlock.js`

### Routes

#### RT-RTE-learning-loop
Label: Learning driver loop

Endpoints/progression/owner: caller → `Voyager.learn` → curriculum → rollout → success-conditioned admission → progress update → next task. Python owns continuation; the caller chooses configuration and can terminate the process. It runs an open-ended exploration curriculum bounded by a recorder iteration check, not an externally supplied answer sequence. State/effects include world actions, checkpoint updates and event logs. Proposal/decision/veto roles are expanded in the task-selection, judgment and admission records. No external answer oracle is supplied by this driver. Evidence: SRC-1, `voyager/voyager.py`.

- Immediate return: on iteration-limit exit, a mapping of completed tasks, failed tasks and active skills.
- Later read-back: resumed agents load checkpoint state; future curriculum and action calls consume changed progress/context and skill state.
- Delegated visibility: separate model calls receive selected messages; Node receives complete execution strings rather than all Python state.
- Selection predicate: loop continues while recorder iteration has not exceeded max_iterations; successful rollouts call admission.
- Invalidation or expiry: per-task messages/conversations reset at rollout reset; checkpoint state has no general TTL in this driver.
- Activation or effect: code wires repeated game execution and admission; actual execution and benefit are unobserved.
- Evidence limits: no supplied end-to-end run; exceptions outside the rollout try block can terminate learning.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if info["success"]:
>     self.skill_manager.add_new_skill(info)
> --- `voyager/voyager.py`

#### RT-RTE-task-selection
Label: Curriculum task selection

Endpoints/progression/owner: observations/progress → hardcoded override or auto/manual curriculum → task/context → rollout. Driver and curriculum own ordering. Auto model proposes; code parses a nonempty `Task:` line and can reject/retry malformed output. Manual human proposes and confirms, except earlier hardcoded branches. Context comes from caller/manual text, hardcoded guidance, or QA/cache. Operating mode: bounded curriculum episodes inside open exploration; inference can instead supply explicit subgoals. No trusted expected-answer oracle is supplied; QA model answers are guidance, not validation. This route selects work, not changes to production machinery. Evidence: SRC-1, `voyager/agents/curriculum.py`.

- Immediate return: task string and context string.
- Later read-back: task success/failure histories and QA cache feed subsequent selection; detailed write mechanisms left to memory analysis.
- Delegated visibility: curriculum gets warmup/probability-filtered observations and selected QA, action gets task/context.
- Selection predicate: initial auto task first; inventory pressure next; then configured auto/manual dispatch.
- Invalidation or expiry: task is replaced per rollout; completed tasks are deduplicated and removed from failed history.
- Activation or effect: returned task/context determine requested actions; model compliance and task quality unobserved.
- Evidence limits: model reasoning and operational quality uninspected; manual mode does not suppress hardcoded inventory branches.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if self.progress == 0 and self.mode == "auto":
>     task = "Mine 1 wood log"
>     context = "You can mine one of oak, birch, spruce, jungle, acacia, dark oak, or mangrove logs."
>     return task, context
> --- `voyager/agents/curriculum.py`

#### RT-RTE-environment-step
Label: Environment execution step

Endpoints/progression/owner: caller or parsed action → Python HTTP bridge → Node `/step` → eval → Mineflayer/game → event observations → Python. Node owns evaluation and response assembly; Python owns subsequent interpretation. No per-action approval is applied here. Executable forms are symbolic code/program strings; effect scope includes host-process context and game APIs, with external deployment permissions unresolved. Evidence: SRC-1, `voyager/env/bridge.py`, `voyager/env/mineflayer/index.js`, `voyager/env/mineflayer/lib/observation/base.js`; eval quote in account.

- Immediate return: accumulated observation events, decoded by the bridge after HTTP response; execution errors can be emitted as events.
- Later read-back: Python recorder persists returned events and action/chest/skill mechanisms may retain derived state; Node clears its cumulative observation buffer per response/step.
- Delegated visibility: Node receives all supplied programs and code; models later receive selected rendered observations, not the full Node lexical environment.
- Selection predicate: any environment step after reset; direct endpoint does not require parser or critic approval.
- Invalidation or expiry: per-request observations reset; bot state survives until resets/disconnect; world effects need not be undone.
- Activation or effect: wired eval and privileged game assistance can change world and host-visible state; no observed exercise claimed.
- Evidence limits: no sandbox test, endpoint security test, external plugin correctness proof or real game trace; an HTTP timeout is not a cancellation proof.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-task-judgment
Label: Task success judgment

Endpoints/progression/owner: events/task/context/chest observation → critic renderer → auto model/parse or human confirmation → success/critique → retry or completion. Proposer is the action model; success decision is the auto critic or human. Auto code can veto on onError, malformed response or exhausted retries. Manual human has final confirmation in its mode. Operating modes: task-level assessment in learning and inference. Answer oracle: no independent expected-answer service/dataset is provided; the task and prompt's examples/heuristics guide judgment of observed state. Human judgment is not an independently supplied reference answer. Evidence: SRC-1, `voyager/agents/critic.py`, `voyager/prompts/critic.txt`.

- Immediate return: success boolean and critique text.
- Later read-back: critique enters the next action message within the task; success shapes progress and, only in learn, skill admission.
- Delegated visibility: auto critic sees selected final-state fields, not action code or arbitrary full execution history; human prompt requests success and critique.
- Selection predicate: invoked after a parsed program executes; manual/auto dispatch follows configured mode.
- Invalidation or expiry: new judgment replaces prior feedback each executed attempt; no independent durable critique store is established here.
- Activation or effect: success ends rollout and can enable admission; critique is delivered as revision guidance, not enforced compliance.
- Evidence limits: no observed truthfulness or calibration; prompt heuristics may treat inventory or nearby blocks as sufficient without proving action causality.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if messages[1] is None:
>     return False, ""
> --- `voyager/agents/critic.py`

> if self.mode == "manual":
>     return self.human_check_task_success()
> --- `voyager/agents/critic.py`

#### RT-RTE-skill-admission
Label: Successful program admission

Endpoints/progression/owner: learning success info → SkillManager → description model → embedding/index and file writes → future prompt retrieval/execution. Trigger: success branch in learning; caller may also invoke manager directly. Proposed change: new or replacement skill code plus description. Proposal guidance: action prompt requests reusable inventory-aware functions; description prompt requests a short main-function description excluding chat/helper detail. Code proposes the admission after critic/human success; the manager skips deposit tasks but does not independently test safety/success. No additional human content approval is required by this mechanism. A caller can supply a library through constructor configuration; that is not evidence of a human authoring/approving every library entry. Operating mode: task-success-conditioned capability retention. Answer oracle: only the prior task judgment, not an independent regression test. Rejection/recovery: exceptions can interrupt writes; duplicate names replace active map/index entries and preserve versioned text files, but no transactional rollback or automatic regression reversion is wired. Evidence: SRC-1, `voyager/voyager.py`, `voyager/agents/skill.py`, `voyager/prompts/action_template.txt`, `voyager/prompts/skill.txt`.

- Immediate return: no substantive return value; manager state and persistent files/index change.
- Later read-back: future retrieval delivers selected code to the action model; all loaded skills enter the executable programs string; resume or skill_library_dir reloads them.
- Delegated visibility: description model sees program code and main name; embedding service receives description text; executor receives skill code.
- Selection predicate: learning success except deposit-task prefix; same-name entries replace active code/description/index membership.
- Invalidation or expiry: active same-name replacement; no TTL or automatic failed-transfer invalidation established by manager.
- Activation or effect: wired durable capability admission and later code supply; invocation-dependent use and improvement remain unobserved.
- Evidence limits: persistence/count assertions do not establish semantic consistency, atomicity, safety or benefit; distributed skill files do not prove their learning history.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> self.skills[program_name] = {
>     "code": program_code,
>     "description": skill_description,
> }
> --- `voyager/agents/skill.py`

This is an implemented improvement-directed retention path, not a demonstrated learning gain. No claim that these task programs formulate explanatory theories is made: their content and exposed assumptions would need separate assessment rather than classification from their `.js` encoding. Likewise critic feedback requests action revision but does not itself demonstrate content-directed theory criticism. No theory-builder classification is inferred here. For any exercised self-improvement attribution over later tasks, the unestablished link is subsequent operation causally depending on the admitted change; no such run is supplied. The wiring supports only a dispositional path from task evidence through retained code to later behavioral authority, with successful improvement independently unestablished.

#### RT-RTE-task-inference
Label: Learned-library task inference

Endpoints/progression/owner: caller task or subgoals → optional curriculum-model decomposition → sequential subgoal rollouts → progress updates. Caller may inspect/replace decomposition as README suggests; no mandatory approval gate. Model proposes decomposition; parser accepts JSON; caller can bypass decomposition with subgoals. Operating mode: caller-specified task execution, not automatic exploration. No trusted answer oracle beyond the configured task critic. Evidence: SRC-1, `README.md`, `voyager/voyager.py`, `voyager/agents/curriculum.py`.

- Immediate return: inference has no explicit result mapping; terminal state/progress, logs and recorded events remain.
- Later read-back: loaded skill library is consumed; QA/chest/progress and events can still change, but inference does not admit newly successful skills through add_new_skill.
- Delegated visibility: decomposition model receives task and rendered current observations; action and critic see each selected subgoal and context.
- Selection predicate: sub_goals supplied by caller, otherwise decomposition; next index is curriculum progress, the unique completed-task count.
- Invalidation or expiry: inference clears in-memory completed/failed lists at start; subsequent progress persists through curriculum updates.
- Activation or effect: shares real execution route and critic loop; no inference activation or success observed here.
- Evidence limits: repeated failure or duplicate subgoals can prevent progress; no global inference iteration bound or enclosing learning-style recovery block.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> while self.curriculum_agent.progress < len(sub_goals):
>     next_task = sub_goals[self.curriculum_agent.progress]
> --- `voyager/voyager.py`

### Claims

#### RT-CLM-lifelong-learning
Label: Lifelong learning entry claim

Claimed operation: the shipped README labels `voyager.learn()` as the start of lifelong learning. Source: SRC-1, `README.md`. The source-grounded realization is task-conditioned retained executable skills and later model/executor supply, not client-side model weight training. Future capacity improvement and exercised causal dependence remain unestablished by this source-only analysis.

> # start lifelong learning
> voyager.learn()
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-execution
Label: Retained skill execution authority

Consumer: Node eval and generated functions calling retained functions. Channel: `SkillManager.programs` concatenates every active skill code string plus control primitives into the HTTP programs field. Force: symbolic executable definitions, not advisory prose; actual invocation depends on program references and JavaScript evaluation semantics. Horizon: later action attempts/tasks and resumed or externally supplied libraries. Distinct from prompt retrieval: top-k selection limits model-visible code, not executable definitions. Evidence: SRC-1, `voyager/agents/skill.py`, `voyager/voyager.py`, `voyager/env/mineflayer/index.js`.

> for skill_name, entry in self.skills.items():
>     programs += f"{entry['code']}\n\n"
> --- `voyager/agents/skill.py`

#### RT-BAP-action-guidance
Label: Action prompt behavioral guidance

Consumer: action model. Channel: system message containing shipped action instructions, primitive context and retrieved skill code, plus human message containing task/context, last code, observations and critique. Force: natural-language behavioral direction and interpreted code examples, not an executor access-control rule. Horizon: current action invocation, refreshed on the next successful execution path; retained skills may re-enter later invocations. Evidence: SRC-1, `voyager/prompts/action_template.txt`, `voyager/agents/action.py`, `voyager/voyager.py`.

> 2) Reuse the above useful programs as much as possible.
> --- `voyager/prompts/action_template.txt`

## Annotations

none
