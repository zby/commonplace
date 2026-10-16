---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "ReasoningBank runtime baseline: shipped web and coding task loops, automatic memory admission and forcing routes."
run-id: AAS-2026-10-14-reasoning-bank-f0bedcab086c-01
reviewed-boundary: ed80611788292ea739f1effd31f16c53823b8a0d
---

# ReasoningBank runtime report

## Runtime account

ReasoningBank's consequential work is a task-to-memory-to-task loop, not model-weight training. The shipped drivers own retrieval, task execution, feedback, induction and persistence. This account uses SRC-1 implementation and shipped instruction text at the boundary revision. No execution trace or experiment was supplied. Wiring does not establish successful operation, use of delivered advice or benefit.

### Ordinary WebArena invocation

An operator invokes `WebArena/pipeline_memory.py` with a website, model, result directory and task slice. Code sorts numbered task configurations, selects matching sites and skips IDs at or below `prev_id`. For each task the parent launches `run.py`, waits, launches autoevaluation, waits, and launches induction unless memory mode is `no_memory`. The parent owns scheduling; subprocesses own their respective effects. Waiting orders completion, but the ordinary pipeline does not reject nonzero child return codes ([RT-RTE-web-pipeline](#rt-rte-web-pipeline)).

`WebArena/run.py` derives a website-specific JSONL bank from the memory text path, reloads records and queries the selector with the task intent. Selection appends the current query embedding to a cache and ranks the *previously loaded* cache; top-one cached task ID is matched to the first bank record with that ID. All memory-item strings from that record are flattened into a text file, or the file is emptied. No match fallback after a top ID lacking a bank record is implemented in the inspected selector. The current query is embedded even for an initially empty cache (SRC-1, `WebArena/run.py`, `WebArena/memory_management.py`). This is a similarity selector over prior queries, not model judgment of memory truth.

The runner constructs BrowserGym `EnvArgs` and `GenericAgentArgs`, prepares an experiment, runs it and renames its result directory to the task name, deleting an existing destination. The generic agent maintains observations, actions, scratchpad fields and thoughts in per-episode Python lists. At each step it constructs a task/history prompt, applies best-effort shrinking, reads the memory text into the system message, asks the model and parses an action. Parse failures can prompt model retries; exhausted retries return a null action with error metadata. BrowserGym executes the returned action and owns browser effects, task stopping and serialized experiment artifacts. Its installed execution machinery and live websites are external dependencies; the adapter's action delivery is inspected, not their operation. The declared runner limit is 30 steps by default (SRC-1, `WebArena/run.py`, `WebArena/agents/legacy/agent.py`).

The action capability surface includes high-level browser and Python action-set flags. The ordinary runner uses the `Flags` default `bid`, chat enabled and multi-actions enabled; notably, its parsed `--action_space` value is not passed into `Flags`. This is not an authorization or deployed sandbox proof. Browser/session credentials, site permissions and installed BrowserGym enforcement remain uncaptured. The memory instruction asks the task model to discuss relevance; code does not inspect that discussion or enforce compliance ([RT-BAP-system-memory](#rt-bap-system-memory)).

Aut evaluation reloads saved steps, derives final user response from the last `send_msg_to_user` action, truncates page observations to 40,000 characters each and supplies at most the last five page captions alongside think/action history to its text evaluator. Model output is parsed into thoughts and status, and status equality to `success` supplies `rm`; evaluator errors produce null feedback. Induction's default `autoeval` route treats only reward equal to 1 as success. Its `gt` alternate reads `summary_info.json` cumulative reward. Neither a model verdict nor a benchmark-reward label proves correctness. The default evaluator does not use an expected answer oracle in the inspected model prompt construction; benchmark reward is saved separately (SRC-1, `WebArena/autoeval/evaluate_trajectory.py`, `WebArena/autoeval/evaluator.py`, `WebArena/induce_memory.py`).

Induction reconstructs think/action pairs, skipping unreadable steps and steps without actions. It supplies task, trajectory and available evaluator explanation to a separate model call, with success or failure instruction. It splits returned text on blank lines and appends a JSONL record. The next task reloads that bank. This admission is computational; initiating the pipeline is not per-item human approval. It updates retained advice, not runtime source or weights ([RT-RTE-web-admission](#rt-rte-web-admission)). Memory-item internals and revision analysis belong to the memory analyst.

### Coding task invocation

`SWE-Bench/run.sh` enters `third_party` and requests `mini-extra swebench`, Gemini Flash, verified/test tasks and one worker. The batch driver selects dataset instances, loads YAML configuration and creates a model/environment per instance. Task identity is the SWE-Bench instance ID; bank/cache identity is the configured model name. `process_instance` removes stale prediction/trajectory entries, reloads a bank and selects one prior query's record before entering its agent-execution try block. Consequently retrieval/setup errors before that block do not get the same trajectory-saving recovery ([RT-RTE-swe-task](#rt-rte-swe-task)).

`DefaultAgent.run` clears messages and builds a fresh system/user context for each task. Selected memory is appended to the system message. The model owns command choice; code owns querying, extracting exactly one bash block, execution and return. The supplied YAML asks for edits only to regular non-test files, but the parser checks bash-block count rather than command safety, file permissions or semantic compliance. A command can contain arbitrary shell operations. The default executor runs `bash -lc` through Docker in `/testbed`; submission is detected from the first output line matching a marker, not from a correctness test. The terminal returned string is stored as a model patch even for non-submission exits. Cost/step checks occur before task-model queries, using the adapter's reported counters. The YAML's observation template retains the first and last 5,000 characters for long command outputs; the shell can retain full output in files for explicit later reads (SRC-1, `third_party/src/minisweagent/agents/default.py`, `third_party/src/minisweagent/config/extra/swebench.yaml`, `third_party/src/minisweagent/environments/docker.py`).

In the finally block, the driver saves the trajectory, updates predictions and progress, then builds a non-system message transcript for a direct Google GenAI judging call. A response containing `success` chooses the success induction prompt; otherwise failure guidance is used. Another direct call generates advice, which is appended to the bank. No external SWE-Bench test outcome gates this admission. These direct calls do not pass through `DefaultAgent.query` or its per-agent limits. An adapter-selected task model therefore does not ensure that the same name is supported by the direct Google client ([RT-RTE-swe-admission](#rt-rte-swe-admission)).

Prediction writes have an in-process lock. The inspected memory/cache writes do not share that lock. One worker in the launcher avoids overlapping instance threads there; the CLI affords multiple workers, with bank/cache snapshots and appends no longer serially coordinated. This limits consistency claims, rather than proving corrupt execution. Failures during finally-block judging/induction can leave predictions and trajectories without corresponding advice. Future exceptions are logged; no transactional rollback of bank, cache and prediction state is implemented in these inspected routes (SRC-1, `third_party/src/minisweagent/run/extra/swebench.py`).

### Forcing cases and bounded guarantees

Four source-level cases challenge ordinary-path generalizations; none was executed:

1. **No memory and nondefault modes.** `no_memory` still runs web inference/evaluation but omits retrieval and induction. `awm` and `synapse` induction assign output only on success, yet append uses that variable regardless. Pipeline model choices exceed induction's argparse choices. Thus the pipeline's advertised choice surface does not establish a working loop for every choice (SRC-1, `WebArena/pipeline_memory.py`, `WebArena/induce_memory.py`; [RT-RTE-web-pipeline](#rt-rte-web-pipeline)).
2. **Scaling is not verified multi-trajectory admission.** The scaling launcher sends only the final trial's directory to induction; induction repeatedly reads that same directory. It does not launch autoevaluation, does not forward the chosen model to induction, labels reward zero as success, and takes a client class without instantiation before calling its instance method. All trials also share the memory text/cache paths. These are inspected wiring discrepancies, not observed failures ([RT-RTE-web-scaling](#rt-rte-web-scaling)).
3. **Shell isolation is a chosen executor, not a universal invariant.** Docker is the coding default, but `--environment-class` can select local execution or an imported class. Local execution uses a host shell. Model and environment factories accept full import paths. This is operator-configured extension of trusted host code, not model-authored plugin admission in the inspected driver. Docker flags, images, host privileges and remote adapters' isolation are not frozen ([RT-RTE-client-selection](#rt-rte-client-selection)).
4. **Limits and shrinking have narrower coverage than their labels.** Coding step/cost checks cover calls through `DefaultAgent.query`, not direct judges, induction or embeddings. Web prompt shrinking operates on the main prompt before memory system-message injection, returns without fitting for Claude-prefixed names and returns an oversized prompt after iteration exhaustion. It is best effort, not a complete model-input token invariant ([RT-RTE-context-control](#rt-rte-context-control)).

The parser's one-bash-block rule is a local invariant of `DefaultAgent.parse_action` on this path; it requires response text compatible with the regex and does not constrain how many shell commands the block executes. Its owner is `DefaultAgent`; the executor is a separate trust boundary. Prompt restrictions are policies owned by shipped YAML and require model compliance. Docker execution is a configured isolation affordance whose deployment strength depends on the external daemon, image and operator flags. Browser restrictions depend on installed BrowserGym and site/session permissions. These distinctions separate capability surface, current configuration and deployed isolation. No source-level guarantee is promoted to observed operation.

Additional coverage under SRC-1: inspected coding Docker/local executors, environment/model factories, SWE-Bench YAML, both induction and scaling drivers, web prompt shrinking/history, autoevaluation construction and client dispatch. These extend the boundary's initial inspection within the same registered commit. Other provider-native tool adapters, remote executors, interactive runners and installed host callbacks remain uninspected here; conclusions about enforcement are explicitly restricted to the traced drivers and agents. No universal all-entry-point safety or resource guarantee is asserted.

## Shared records

### Components

#### RT-CMP-task-model
Label: Configured task model and generative service calls

Source-native identity: `chat_llm`, coding `model`, and direct GenAI generation clients. Representational form: distributed-parametric model computation; natural-language inputs/outputs are separate from weights. Storage substrate: external provider/model infrastructure; internal storage uninspected. Task, evaluation and induction roles may use the same model name but have separate calls and contexts. Inspected routes do not update model parameters. Exact weights/service version are not pinned: a dated model name still supplies no weight digest or frozen endpoint contract, and mutable service resolution can change behavior. Provider internals and training remain uninspected. SRC-1, `WebArena/agents/legacy/agent.py`, `WebArena/utils/clients.py`, `third_party/src/minisweagent/models/__init__.py`, `third_party/src/minisweagent/run/extra/swebench.py`.

> model_class = get_model_class(resolved_model_name, config.pop("model_class", ""))
> --- `third_party/src/minisweagent/models/__init__.py`

#### RT-CMP-gemini-embedding
Label: Gemini embedding selector component

Source-native identity: `gemini-embedding-001`. Representational form: distributed-parametric model and dense output vectors. Substrate: external Vertex service, tensors in host RAM and embedding JSONL. No parameter update is implemented in the inspected embedding route; cached vectors change by append. Exact service weights/version are not pinned; endpoint resolution can change. SRC-1, `WebArena/memory_management.py`, `third_party/src/minisweagent/memory/memory_management.py`.

> model_name = "gemini-embedding-001"
> model = TextEmbeddingModel.from_pretrained(model_name)
> text_input = TextEmbeddingInput(query, "RETRIEVAL_DOCUMENT")
> --- `WebArena/memory_management.py`

#### RT-CMP-qwen-embedding
Label: Optional Qwen embedding component

Source-native identity: `Qwen/Qwen3-Embedding-8B`. Distributed-parametric pretrained model loaded from a model repository into CPU/GPU memory; output is a dense tensor. The inspected call uses `torch.no_grad`, not weight training. `from_pretrained` supplies no revision pin; a mutable model repository can resolve to different weights. Ordinary shipped callers prefer Gemini. The Qwen option changes the initial query-cache vector, but instruction-query scoring still invokes Gemini, so dimensional/model compatibility is not guaranteed by that preference switch. SRC-1, `WebArena/memory_management.py`.

> model = AutoModel.from_pretrained('Qwen/Qwen3-Embedding-8B')
> --- `WebArena/memory_management.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-web-pipeline
Label: Sequential WebArena task pipeline

Operator CLI → task configurations → inference subprocess → evaluator subprocess → induction subprocess. Owner: parent Python driver; symbolic task/site predicates and process sequencing, natural-language task policies. Browser state and task artifacts belong to the experiment; retained bank/cache feed later invocations. Default operating mode is a bounded benchmark slice, not an open-ended self-selected curriculum. Code selects tasks; models choose task actions and feedback; the operator supplies bounds and can stop the process. No per-output approval is wired. SRC-1, `WebArena/pipeline_memory.py`, `WebArena/run.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: completed child processes and per-task result directories; parent has no aggregated answer.
- Later read-back: the next task reloads the JSONL bank and embedding cache when memory mode is enabled.
- Delegated visibility: subprocesses receive task/model/path arguments; the browser agent receives selected text and task observations, not the full bank.
- Selection predicate: sorted task IDs matching site and slice, above prev_id; similarity-ranked prior query for retained advice.
- Invalidation or expiry: prior task destination is deleted before rename; bank/cache have no expiry in this path.
- Activation or effect: task actions are delivered to BrowserGym; advice compliance and task success remain unobserved.
- Evidence limits: child waiting does not establish child success; nondefault mode/model incompatibilities limit path coverage.

> process = Popen(run_cmd)
> process.wait()
> --- `WebArena/pipeline_memory.py`

#### RT-RTE-web-admission
Label: Web trajectory advice admission

Saved trajectory and feedback → induction model → blank-line split → JSONL append → later selector and task model. Owner: `induce_memory.py`. Trigger: completed task in a memory-enabled pipeline, or direct induction CLI. Proposed change: new natural-language advice associated with a task query. The model proposes; code chooses success/failure guidance and admits all returned blocks without semantic review. Human contribution is workflow configuration, not item editing/approval. Rejection ability: call/parse/I/O failure can prevent append, but no per-item quality veto is inspected. Rollback/recovery: no automatic rollback here; trajectory extraction silently skips unreadable steps. Mode: bounded task sequence; default feedback is model evaluation, not an answer oracle. `gt` instead reads benchmark cumulative reward from the saved summary, requiring the external evaluator contract. SRC-1, `WebArena/induce_memory.py`, `WebArena/prompts/memory_instruction.py`.

Guidance requests reusable procedures, avoidance of literal task strings and at most three items. The returned formulation is not checked against those requirements. Task query, think/action lists, outcome label and generated blocks persist. This route can formulate procedural accounts; no supplied generated artifact establishes their actual content. Theory-builder conditions 1–4: (1) afforded — instructions request whole localized statements; (2) uninspected — delivery does not establish decision dependence; (3) uninspected — failure reflection is requested, not evidence of claim-specific criticism and resulting revision; (4) uninspected — accumulated advice does not establish criticism-guided iteration. Addressability: item/block boundaries afforded, finer assumptions uninspected. Persistence: cross-task bank reload wired. Learning: improved future capacity and attribution uninspected. Reflection: trace-to-advice-to-agent feedback pathway wired, actual representation-mediated effects uninspected. Reflective/autonomous theory-builder status remains uninspected; automatic I/O does not establish every theory-building operation. Dispositional improvement-directed self-change is afforded through retained instructions; exercised self-improvement is unestablished because later behavioral dependence and outcome attribution are not observed.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: appended JSONL record containing generated memory blocks and trajectory metadata.
- Later read-back: runner reloads the bank on later tasks and injects a selected record's memory items.
- Delegated visibility: induction receives task, extracted think/action pairs and available evaluator thoughts, not complete browser state.
- Selection predicate: success prompt when reward equals 1; failure otherwise; reasoningbank mode admits both outcomes.
- Invalidation or expiry: inapplicable — append route defines no replacement or expiry.
- Activation or effect: bank mutation and later injection wired; behavior changes from the content unobserved.
- Evidence limits: no generated advice or run evidence; requested criticism and item count are not validated.

> generated_memory_item, _ = llm_client.one_step_chat(trajectory, system_msg=FAILED_SI, temperature=1.0)
> --- `WebArena/induce_memory.py`

> "memory_items": generated_memory_item.split("\n\n"),
> --- `WebArena/induce_memory.py`

#### RT-RTE-swe-task
Label: Coding task shell loop

Dataset instance → selected prior advice → `ProgressTrackingAgent`/`DefaultAgent` → model response → bash-block parser → environment executor → message observation → next query or terminating exception. Owner: batch driver for instance scheduling, agent for turns, selected environment for effects. Fresh per-task messages isolate contexts; shell filesystem persists during the environment lifetime. Thread-pool workers return completion/errors to the batch coordinator. SRC-1, `third_party/src/minisweagent/run/extra/swebench.py`, `third_party/src/minisweagent/agents/default.py`, `third_party/src/minisweagent/environments/docker.py`.

Guarantee owner/enforcement: agent regex admits exactly one bash block (local invariant), but not one command or safe edits. Step/cost pre-query checks are a local limit protocol, requiring adapter counters, not a universal budget. Alternate direct GenAI/embedding calls are outside that enforcement. The Docker grant is shell execution in the selected container; deployed isolation depends on external Docker and configured arguments.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: exit-status/result tuple, trajectory and prediction entry; result is not necessarily a correct patch.
- Later read-back: finally-block admission consumes saved non-system messages; later tasks reload generated advice.
- Delegated visibility: model gets task, selected advice and formatted command observations; environment gets executable command text.
- Selection predicate: dataset filter/slice/optional deterministic shuffle, existing predictions skipped unless redo; one prior query selected by similarity.
- Invalidation or expiry: stale prediction/trajectory removed at instance start; agent messages reset at task start; container cleanup attempted on destruction.
- Activation or effect: arbitrary selected shell commands reach environment.execute; actual execution and adherence to file-edit policy unobserved.
- Evidence limits: installed containers, datasets and provider behavior uncaptured; pre-try retrieval errors bypass agent recovery.

> actions = re.findall(r"```bash\n(.*?)\n```", response["content"], re.DOTALL)
> if len(actions) == 1:
>     return {"action": actions[0].strip(), **response}
> --- `third_party/src/minisweagent/agents/default.py`

> cmd.extend([self.container_id, "bash", "-lc", command])
> --- `third_party/src/minisweagent/environments/docker.py`

#### RT-RTE-swe-admission
Label: Coding trajectory advice admission

Saved non-system messages → direct GenAI judge → success/failure instruction → direct GenAI generation → model-named JSONL append. Owner: `process_instance` finally block. Trigger: agent execution exits or raises after entering try. The judge decides a label by substring matching; generator proposes text; host code splits and admits it. No per-item human contribution/veto or benchmark answer oracle is wired. Operating mode: bounded benchmark instances, one worker in shipped launcher, multiple threads afforded by CLI. Recovery: future errors are logged, but admission is not transactional with saved predictions. Proposed change and persisted guidance: coding reasoning advice under success/failure templates, plus task ID, query and model outcome label. Source changes, capabilities and runtime machinery are not admitted by this route. SRC-1, `third_party/src/minisweagent/run/extra/swebench.py`, `third_party/src/minisweagent/memory/instruction.py`.

Theory account: requests extraction and reflection under unchanged shipped guidance, not demonstrated criticism/revision of a specific theory. Theory-builder conditions 1–4 separately: (1) afforded — localized item content requested; (2) uninspected — later decision dependence not shown; (3) uninspected — no generated criticism artifact; (4) uninspected — no criticism-shaped next round supplied. Item-level addressability is afforded, finer structure uninspected. Cross-problem persistence is wired. Learning and benefit are uninspected. Reflection has a wired trace/advice feedback route but unobserved downstream causal effect. Autonomous/reflective theory-building and exercised self-improvement remain uninspected for those independent missing links, not disproved by opacity.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: generated blocks appended to the bank after trajectory/prediction writes.
- Later read-back: subsequent process_instance calls reload the model-named bank and select advice for system injection.
- Delegated visibility: judge/generator receive non-system transcript and task; selected prior advice is omitted as a system message.
- Selection predicate: substring success selects SUCCESSFUL_SI; other judge text selects FAILED_SI; no item-quality rejection.
- Invalidation or expiry: inapplicable — appended items have no automatic invalidation in this driver.
- Activation or effect: retained advice supply wired; effects on subsequent command choice unobserved.
- Evidence limits: direct Google calls bypass task-adapter limits and may not support arbitrary adapter model names; bank/cache writes lack the prediction lock.

> if "success" in response:
>     return True
> else:
>     return False
> --- `third_party/src/minisweagent/run/extra/swebench.py`

> trajectory = "\n".join([m["content"] for m in messages if m["role"] != "system"])
> --- `third_party/src/minisweagent/run/extra/swebench.py`

#### RT-RTE-web-scaling
Label: Parallel WebArena scaling admission

Task → concurrent browser trials → waits → induction subprocess → intended bank append. Parent owns trial launches; induction owns proposal/admission. Operator specifies trial count and distinct site ports, but all trials share text/cache paths. Proposed change is combined-trajectory advice under PARALLEL_SI, requesting comparison of success/failure patterns and at most five items. There is no per-content human veto. Default feedback uses summary reward; that is a benchmark outcome source, not a captured expected-answer oracle. The actual repeated input directory prevents treating this wiring as distinct candidate comparison. Rollback/recovery: parent warns about trial exits and proceeds; no transaction/rollback is inspected. SRC-1, `WebArena/pipeline_scaling.py`, `WebArena/induce_scaling.py`, `WebArena/prompts/memory_instruction.py`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: intended JSONL append, but uninstantiated client instance-method invocation prevents asserting a complete executable admission chain.
- Later read-back: if appended, the scaling bank is reloaded through ordinary run.py retrieval.
- Delegated visibility: each trial receives the same task and memory path; induction repeatedly receives the final trial directory's saved messages.
- Selection predicate: task site's first entry and task slice; no implemented distinct-successor choice shown.
- Invalidation or expiry: inapplicable — no scaling advice replacement/expiry in the inspected append path.
- Activation or effect: concurrent trial launches are wired; successful combined-advice induction and behavioral activation are unobserved.
- Evidence limits: repeated directory, reward-label inversion, omitted model forwarding, shared cache/text and class-versus-instance call limit claimed self-contrast operation.

> "--result_dir", f"{args.output_dir}/results_{i}",
> --- `WebArena/pipeline_scaling.py`

> res_dir = args.result_dir
> cur_task = os.path.join(res_dir, args.task)
> --- `WebArena/induce_scaling.py`

> client = CLIENT_DICT[args.model]
> --- `WebArena/induce_scaling.py`

#### RT-RTE-client-selection
Label: Configured provider and executor selection

CLI/YAML → factory → imported model/environment class → instance. Symbolic import dispatch on host; capabilities can change with operator-provided class path. This is configuration admission before work, not evidence-responsive automatic machinery revision. Human/operator configuration proposes and code imports; errors reject resolution, no review gate or automatic rollback is inspected. Mode: chosen task-run configuration; no improvement trigger or answer oracle. Docker is the default, local and remote variants are selectable. SRC-1, `third_party/src/minisweagent/models/__init__.py`, `third_party/src/minisweagent/environments/__init__.py`, `third_party/src/minisweagent/environments/local.py`, `third_party/src/minisweagent/run/extra/swebench.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: initialized implementation object or import/configuration error.
- Later read-back: inapplicable — factory dispatch does not retain experience-derived material.
- Delegated visibility: imported trusted code receives configuration and subsequent model messages/commands according to its interface.
- Selection predicate: supplied class spec or registered shortcut; model-name heuristic when model class omitted.
- Invalidation or expiry: inapplicable — implementation selection lasts for instantiated object; no revision mechanism here.
- Activation or effect: changes executor/provider path, including host-shell execution for local selection.
- Evidence limits: custom classes and remote adapters not exhaustively inspected; current deployed choice/privileges unobserved.

> module_name, class_name = full_path.rsplit(".", 1)
> module = importlib.import_module(module_name)
> return getattr(module, class_name)
> --- `third_party/src/minisweagent/environments/__init__.py`

> command,
> shell=True,
> text=True,
> cwd=cwd,
> env=os.environ | self.config.env,
> --- `third_party/src/minisweagent/environments/local.py`

#### RT-RTE-context-control
Label: Model-visible working-context control

Web observations/history → MainPrompt → fit_tokens → message construction; coding shell output → observation template → accumulated messages. Code rules, not model-directed compaction, decide omissions. Web shrink truncates observation/history elements while original episode lists remain reachable by prompt reconstruction; coding output formatting preserves head/tail and warns the model to use narrower reads or files. Each coding task starts a separate message frame; judge/induction get a derived non-system transcript in separate calls, with only verdict/advice crossing back into host processing. Frame analogy applies to these separate calls, but messages are passed by value and no context-window pointer restores omitted text. No semantic summary is produced by these controls. SRC-1, `WebArena/agents/legacy/agent.py`, `WebArena/agents/legacy/dynamic_prompting.py`, `third_party/src/minisweagent/agents/default.py`, `third_party/src/minisweagent/config/extra/swebench.yaml`.

Guarantee owner: prompt-fitting code; strength: best effort. Coverage: MainPrompt only. Alternate paths: Claude prefix bypass, exhausted iteration, added system memory, and direct evaluator/induction calls. External contract: provider limits and tokenizer/model compatibility. The code affords reducing context, not ensuring the entire request fits.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: formatted model input with possible truncated web elements or shell-output head/tail.
- Later read-back: inapplicable — these controls do not themselves write retained advice; separate admission routes do.
- Delegated visibility: model sees formatted inputs, not necessarily full observation or command output.
- Selection predicate: token estimate and shrink iterations for web; shell output length below 10,000 characters for full coding observation.
- Invalidation or expiry: coding messages clear at task start; web histories are per-episode; omitted view text is not necessarily erased from source state/files.
- Activation or effect: code changes delivered context; effect on model choices unobserved.
- Evidence limits: Claude bypass and memory outside fit prevent complete budget claims; file-backed reload requires a later shell action rather than automatic restoration.

> if model_name.startswith("claude"):
>     return prompt
> --- `WebArena/agents/legacy/dynamic_prompting.py`

> self.extra_template_vars |= {"task": task, **kwargs}
> self.messages = []
> --- `third_party/src/minisweagent/agents/default.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-system-memory
Label: Selected advice in task-agent system message

Consumer: web `chat_llm` and coding task model. Channel: selected natural-language bank content appended to the system message. Force: advisory model-mediated instruction, not a symbolic execution rule; shipped wording permits relevance judgment and requests explicit discussion. Horizon: repeated web steps and coding turns for the task, with bank reload supporting later problems. The injection is wired, but behavioral dependence, reliability and benefit are unobserved. SRC-1, `WebArena/agents/legacy/agent.py`, `third_party/src/minisweagent/agents/default.py`.

> sys_msg += '\n\n' + open(self.flags.memory_path).read().strip()
> --- `WebArena/agents/legacy/agent.py`

> self.add_message("system", system_message)
> --- `third_party/src/minisweagent/agents/default.py`

## Annotations

none
