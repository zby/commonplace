---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "OS-Copilot runtime baseline tracing FRIDAY task execution, repair, capability admission and shipped alternate loops at the frozen revision."
run-id: AAS-2026-10-16-os-copilot-7cef03148c53-01
reviewed-boundary: "f720af8807e49a92dda64572d2c6bc6c0ac7ee7e"
---

# OS-Copilot runtime report

## Runtime account

### Evidence and claimed work

OS-Copilot ships an enclosing runtime for computer-operating tasks. FRIDAY owns decomposition, sequential execution, model evaluation, code repair and graph expansion. Its package describes itself as self-improving; this report establishes implemented routes, not successful automation or improvement. All source findings below are SRC-1 at the revision in [boundary](boundary.md). No target execution, tests, provider requests or experiments were performed. Implementation, requested model behavior and attributed outcomes remain distinct. Activation, operation and benefit are unobserved in this report.

The claimed product work includes changing files and applications, retrieving external information and answering questions. The planner prompt names Python, Shell, AppleScript, API and QA node types (SRC-1, `oscopilot/prompts/friday_pt.py`). The deployment-level self-improvement claim is recorded separately in [RT-CLM-agent-improvement](#rt-clm-agent-improvement).

Added implementation inspection beyond the boundary's initial coverage includes the Python kernel launch and step path, subprocess launch/write/retry path, the two-message prompt helper, retry decorator, JSON merge helper, image/audio model adapters, OCR adapter, agent exports and differences in the alternative agent file. These remain the same registered source, not new evidence sources. Detailed environment preprocessing, provider internals, all service internals, dependency behavior and full test semantics remain uninspected. The source supplies no observed run for these paths.

### Shipped entry paths and ordinary invocation

The direct script `quick_start.py` parses configuration, wraps the query and optional attachment path into task text, constructs FridayAgent with FridayPlanner, FridayRetriever, FridayExecutor and ToolManager, then calls `agent.run`. The ordinary default request copies text files containing “agent” into an “agents” folder. This is a concrete shipped request, not an observed execution. Configuration exposes working directory, generated-tool repository, repair limit (default three), retention score (default eight), query/file and logging settings (SRC-1, `quick_start.py`, `oscopilot/utils/config.py`).

The Electron-capable UI is a caller of that same script, not another agent controller. It creates a query ID and log prefix, builds a shell command using query and attachment arguments, starts it with `child_process.exec`, polls prefixed logs every 100 ms, and maps planner/subtask/result records into UI callbacks. Completion resolves stdout or rejects stderr/process error; a green subtask display is based on the logged error field, not an independent correctness oracle (SRC-1, `fronted/src/interface/api.js`, `fronted/src/interface/constant.js`). The console entry declared in `setup.py` targets `quick_start:main`, but `quick_start.py` has only top-level statements. Installation or console-entry success therefore cannot be assumed from metadata.

The normal code path is [RT-RTE-task-execution](#rt-rte-task-execution):

1. **Trigger and principal:** the caller supplies task text and configuration under its host credentials. Agent identity is an in-process FridayAgent instance; subtasks are model-produced string keys, not separate authenticated principals. ToolManager loads local metadata and Chroma state. There is no delegated worker in this path.
2. **Context selection:** task-text similarity retrieves up to ten tool descriptions for planning. Python subtask descriptions separately retrieve up to three tools' code for generation. Tool descriptions are natural language; code is delivered as text to a generator, not automatically invoked as a retrieved function. The model components are [RT-CMP-chat-model](#rt-cmp-chat-model) and [RT-CMP-tool-embeddings](#rt-cmp-tool-embeddings).
3. **Next-step policy:** the planner receives task, OS version, working-directory listing, retrieved descriptions and API descriptions. It returns JSON whose descriptions/types/dependencies become [RT-OBJ-tool-graph](#rt-obj-tool-graph). Python code topologically orders incomplete nodes. The agent pops one node at a time. The model chooses the plan and code; fixed code chooses graph traversal and type dispatch.
4. **Execution context and effects:** direct prerequisites' descriptions and return values become JSON for the next generator or QA call. Python generation additionally receives selected prior code. The executor extracts a fenced program and, for Python, an invocation. It appends `result=` plus that invocation and return-print markers. Env dispatches the program to Jupyter, a shell or AppleScript. These execute on host facilities, with inherited environment; they are not a documented per-operation privilege boundary.
5. **Feedback and continuation:** Python/Shell/AppleScript results go to a model judge with code, task, errors, directory information and successor requirements. Judge output selects completion, amendment or replanning. [RT-RTE-feedback-repair](#rt-rte-feedback-repair) owns those branches. Completion updates the graph node and `inner_monologue.result`; eligible Python code may enter [RT-RTE-tool-admission](#rt-rte-tool-admission).
6. **Terminal result and recovery:** `run` has no explicit return value. Effects, printed/logged results and `inner_monologue.result` are the product surfaces. Exhausted repair, an exception, or graph exhaustion ends the loop; this is not a uniform typed success/failure contract. Replanning can add tasks repeatedly without a global replan bound. Ordinary exceptions are printed and break the task loop; planner missing-JSON handling can call `sys.exit`, outside `except Exception` (SRC-1, `oscopilot/agents/friday_agent.py`, `oscopilot/modules/planner/friday_planner.py`).

The working-context policy is explicit assembly rather than a persistent conversational transcript. `send_chat_prompts` constructs one system and one user message for each main-module call. Prior full model responses do not automatically cross to the next call. Prerequisite summaries, selected tools and explicit critique/state fields cross instead. The judge preferentially cuts long program output to the first 999 characters when length exceeds 1000; repair receives the full `state.result`. `run` resets graph and inner monologue. This resembles selected-input call frames, but it is not a sub-agent stack: no independent worker returns, and selected values are copied into prompts rather than dereferenced by the model. Tool retrieval supplies an explicit reload route for retained code/descriptions. Kernel teardown removes Python interpreter state after an ordinary Env step, not host files or installed packages (SRC-1, `oscopilot/utils/utils.py`, `oscopilot/modules/executor/friday_executor.py`, `oscopilot/agents/friday_agent.py`, `oscopilot/environments/env.py`).

### Controls, guarantees and counterexamples

The capability surface is arbitrary generated Python, shell and AppleScript plus service calls and QA. The current grant set depends on caller OS permissions, credentials, packages, network and applications. No live deployment grant set or isolation envelope was supplied. An environment's configured `working_dir` and its listings are context, not proof of filesystem confinement. Python kernels and subprocesses inherit environment variables. The inspected executor/Env/launch chain contains no intervening per-content human approval step. This bounded chain supports direct execution authority, not a whole-repository security audit (SRC-1, `oscopilot/modules/executor/friday_executor.py`, `oscopilot/environments/env.py`, `oscopilot/environments/py_jupyter_env.py`, `oscopilot/environments/subprocess_env.py`).

> self.km.start_kernel(env=os.environ.copy())
> --- `oscopilot/environments/py_jupyter_env.py`

> state = self.environment.step(node_type, code)  # node_type
> --- `oscopilot/modules/executor/friday_executor.py`

| Load-bearing control | Owner and enforcement point | Strength, coverage and external contract | Separate conclusions |
| --- | --- | --- | --- |
| Repair-attempt ceiling | FridayAgent.repairing tests trial count against executor.max_iter | invariant for that local loop's entry count; not a task-time or replan bound. Provider/OS termination remains external. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Completion decision | executor.judge_tool requests structured model evaluation; agent branches on status | best effort semantic judgment, not verified task correctness. API/QA take another completion path. Requires model fidelity and useful output/errors. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Python automatic-retention gate | self_refining checks node type, completion flag and score | policy on this call site only. Manual manager writes bypass it; repaired verdict can be paired with original code. Requires parseable truthful model score; no approval oracle. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Metadata/index agreement | ToolManager constructor/add checks collection count equals metadata length | invariant only for equality at assertion points with assertions enabled; not content equality, atomicity or crash recovery. Requires Chroma semantics and filesystem writes. | implementation conclusion status: wired; operation conclusion status: uninspected |

Four forcing cases challenge a stronger account:

- **Repair succeeds, wrong candidate retained:** repair assigns new code locally and returns it in RepairingResult, but self_refining updates score/result without replacing its outer `code`. It can store the original failed candidate under the repaired score. Thus “only the successfully tested code is retained” is not established; the visible data flow contradicts it ([RT-RTE-tool-admission](#rt-rte-tool-admission)).
- **Type changes the evaluation path:** QA prints a model answer and is marked complete without the code judge. API generates Python and reaches PythonJupyterEnv through its `API` alias, but does not receive Python's invocation/result-print wrapper and skips the code judge. Thus the completion policy is not a universal check on all host-executed programs ([RT-RTE-api-qa](#rt-rte-api-qa)).
- **A writer is not the agent gate:** manual add directly calls ToolManager.add_new_tool, which can overwrite an existing name without score or execution. Count assertions do not validate code semantics. This defeats a repository-wide interpretation of the automatic gate ([RT-RTE-manual-maintenance](#rt-rte-manual-maintenance)).
- **Another shipped loop has different policy:** LightFriday and the vision example call the model and Env directly, grow message histories and use response substring termination. They do not pass through FridayAgent's repair/retention policy ([RT-RTE-example-loops](#rt-rte-example-loops)). Course learning changes triggers but invokes the ordinary agent, retaining its limitations ([RT-RTE-course-learning](#rt-rte-course-learning)).

Direct SDK module calls, direct ToolManager writes, shell subprocesses and local API clients therefore cannot inherit guarantees attached only to FridayAgent. Provider-native tool execution is not used by the inspected chat adapters: they submit messages and receive text. Host effects can still occur through generated programs and external services. The exported agent is `friday_agent.py`; the similarly named `friday2_agent.py` differs by lacking the task-loop exception wrapper, not by adding another approval boundary (SRC-1, `oscopilot/utils/llms.py`, `oscopilot/agents/__init__.py`, `oscopilot/agents/friday2_agent.py`). No remote-worker orchestration was established in these inspected routes. This is an inspection limit, not a global absence claim.

## Shared records

### Components

#### RT-CMP-chat-model
Label: Configured chat model

Source-native identity: BaseModule's OpenAI or OLLAMA adapter chosen by MODEL_TYPE; MODEL_NAME identifies the requested model. Representational form: distributed-parametric inference behind a text-message API. Substrate: external OpenAI-compatible service or Ollama server, not model weights in this repository. The runtime sends inference requests; no parameter-update operation is present in these adapters. Actual provider-side mutability remains uninspected. Exact weights/version are not pinned by environment-selected names; a mutable configured service can resolve a name differently. OpenAI accepts a logging prefix, whereas OLLAMA.chat lacks the prefix keyword that the shared helper always passes, so selection alone does not establish working interchangeability. Evidence: SRC-1, `oscopilot/modules/base_module.py`, `oscopilot/utils/llms.py`, `oscopilot/utils/utils.py`.

> return llm.chat(message, prefix=prefix)
> --- `oscopilot/utils/utils.py`

> def chat(self, messages, temperature=0):
> --- `oscopilot/utils/llms.py`

#### RT-CMP-tool-embeddings
Label: Tool description embedding model

Source-native identity: ToolManager's OpenAIEmbeddings or OllamaEmbeddings. Form: distributed-parametric embedding inference; substrate: provider/server weights with derived vectors persisted in Chroma. No weight update is requested by ToolManager; provider internals are uninspected. OpenAI model selection is left to the dependency default (the source comment names text-embedding-ada-002); Ollama uses the same MODEL_NAME environment variable as chat. Neither exact weights nor server resolution is immutable here. Mutable endpoints and dependency defaults can change results without a repository change. Evidence: SRC-1, `oscopilot/tool_repository/manager/tool_manager.py`.

> embedding_function = OllamaEmbeddings(model=EMBED_MODEL_NAME)
> --- `oscopilot/tool_repository/manager/tool_manager.py`

#### RT-CMP-image-caption
Label: ImageCaptionTool model

Source-native identity: ImageCaptionTool's `gpt-4-vision-preview` OpenAI request. Form: distributed-parametric; substrate: remote provider. Adapter performs inference only, not parameter updates; provider-side changes are uninspected. A literal preview model name is not an immutable weights pin and mutable provider resolution remains possible. Receives image URL/data and query; returns text, with max_tokens 300. Evidence: SRC-1, `oscopilot/tool_repository/api_tools/image_caption/gpt4v_caption.py`.

> model="gpt-4-vision-preview",
> --- `oscopilot/tool_repository/api_tools/image_caption/gpt4v_caption.py`

#### RT-CMP-audio2text
Label: Audio2TextTool model

Source-native identity: Audio2TextTool's `whisper-1` transcription request. Form: distributed-parametric; substrate: remote provider. No weight update is requested. Exact weight revision is not pinned; provider endpoint resolution and internal mutability remain uninspected. The adapter returns `response.texts`; external response compatibility is not established. Evidence: SRC-1, `oscopilot/tool_repository/api_tools/audio2text/audio2text.py`.

> response = self.client.audio.transcriptions.create(
>     model="whisper-1",
>     file=audio_file
> )
> --- `oscopilot/tool_repository/api_tools/audio2text/audio2text.py`

#### RT-CMP-ocr-service
Label: Vision example OCR service

Source-native identity: Baidu general OCR HTTP endpoint used by `ocr`. Form: opaque external recognition computation; any distributed-parametric internals are uninspected, not assumed from its name. Substrate: external service; derived images are local PNGs and returned coordinates are in-process dictionaries. The client requests recognition, not parameter updates; exact model version, provider-side changes and endpoint model substitution are uninspected and unpinned. This prevents characterizing model fixity or recognition quality. Evidence: SRC-1, `examples/friday_vision/friday_vision.py`.

### Operative objects

#### RT-OBJ-tool-graph
Label: FridayPlanner task graph

Source-native identity: tool_node, tool_graph and sub_task_list. Symbolic keys, dependencies, type strings, status flags and order live in Python dictionaries/lists/deques; natural-language descriptions and result text are copied to model prompts. These are distinct consumption paths: fixed graph traversal versus model interpretation. State is reset per agent.run, updated on completion, and expanded on replan. It is current-run coordination state, not evidence of durable retained experience. Evidence: SRC-1, `oscopilot/modules/planner/friday_planner.py`, `oscopilot/agents/friday_agent.py`.

> sub_task = self.planner.sub_task_list.pop(0)
> execution_state = self.executing(sub_task, task)
> isTaskCompleted, isReplan = self.self_refining(sub_task, execution_state)
> --- `oscopilot/agents/friday_agent.py`

#### RT-OBJ-friday-prompts
Label: FRIDAY method prompts

Source-native identity: prompt dictionaries in friday_pt.py, supplied to planner, retriever, executor and learner. Form: natural-language instructions and examples interpreted by models, with embedded output-format conventions parsed by code. Substrate: shipped Python string literals, copied into transient API messages. These texts request decomposition, generalizable code, judgment, repair and curricula; the inspected loop does not revise the method texts. Code candidates and courses persist through other routes, not as mutations of these prompts. Evidence: SRC-1, `oscopilot/prompts/friday_pt.py`, `oscopilot/agents/friday_agent.py`.

### Routes

#### RT-RTE-task-execution
Label: Task planning and host execution

Caller task → description retrieval → model plan → graph order → model code/invocation → Env → state → feedback route. FridayAgent owns progression; planner model chooses nodes/dependencies, executor model proposes code, Python dispatch chooses executor. Human contribution is the initiating request/configuration, not per-program approval. Open-request mode; expected answers are not supplied as an answer oracle. Evidence: SRC-1, `quick_start.py`, `oscopilot/agents/friday_agent.py`, `oscopilot/modules/planner/friday_planner.py`, `oscopilot/modules/executor/friday_executor.py`, `oscopilot/environments/env.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: EnvState holds program output/error plus working-directory information; agent.run itself returns no explicit product.
- Later read-back: selected retained descriptions/code reach later planning/generation; ordinary graph state is current-run only.
- Delegated visibility: inapplicable — no agent delegation in this path; generated programs receive their code and inherited host environment, not the full planner object.
- Selection predicate: initial task retrieves at most ten descriptions; Python node description retrieves at most three code candidates; graph dependencies choose predecessor results.
- Invalidation or expiry: next run resets graph and inner monologue; ordinary Python Env steps terminate their kernel; external effects and retained tools are not thereby undone.
- Activation or effect: generated code is passed to host interpreters; successful OS effects and influence of retrieved material remain unobserved.
- Evidence limits: source wiring only; provider compatibility, model compliance, host grants, task success and global termination are not established.

> code = code + '\nresult=' + invoke + info
> --- `oscopilot/modules/executor/friday_executor.py`

> lang = self.get_language(language)()  # 输入planner的节点类型即可
> --- `oscopilot/environments/env.py`

#### RT-RTE-feedback-repair
Label: Judgment repair and replanning

ExecutionState → model judgment → completion, model repair/re-execution, or model graph expansion. FridayAgent decides branches using returned status. The executor model proposes code and judges results; planner model proposes added tasks; fixed code limits amendment iterations and applies dependencies. No explicit human veto occurs between proposal and execution. Open-request and curriculum tasks use the same mechanism. Answer oracle: none supplied; task requirements, observed program text output/error and directory listings are evidence inputs, not a reference answer. Improvement trigger is a returned Amend/Replan status or execution error in the repair loop. Evidence: SRC-1, `oscopilot/agents/friday_agent.py`, `oscopilot/modules/executor/friday_executor.py`, `oscopilot/prompts/friday_pt.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JudgementResult or RepairingResult controls completion/replan; successful result updates graph and inner monologue.
- Later read-back: critique, revised code and execution state shape another repair within this run; durable capability admission is separately recorded below.
- Delegated visibility: inapplicable — separate model calls receive assembled fields, not delegated agent sessions.
- Selection predicate: only Python/Shell/AppleScript use this judge; Amend repairs, Replan inserts prerequisites, other initial statuses mark completion.
- Invalidation or expiry: loop-local candidate is replaced by each amendment; retry count bounds repair only; completed node status excludes it from later ordering.
- Activation or effect: amended code is executed before the next decision; replanning changes the work queue. No observed execution supplied.
- Evidence limits: initial status handling is permissive outside Amend/Replan; substring-based error extraction and truncated judge output limit evidence fidelity; no independent correctness check or whole-task time bound.

Guidance requests comparing code/task/feedback and generality, then proposing repairs or environment work. Rejection ability is computational: judge can withhold completion, iteration exhaustion stops the task, exceptions can abort it. There is no transactional rollback of files, package installations or prior actions. Decorated generation/judgment calls retry exceptions up to three attempts; retries are not proof of idempotent effects (SRC-1, `oscopilot/utils/utils.py`).

> while (trial_times < self.executor.max_iter and status == 'Amend'):
> --- `oscopilot/agents/friday_agent.py`

> code_output=state.result[:999] if len(state.result) > 1000 else state.result,
> --- `oscopilot/modules/executor/friday_executor.py`

> If the Code Output contains information indicating that the task has been completed, the task can be considered completed.
> --- `oscopilot/prompts/friday_pt.py`

These are candidate-program revisions guided by static method instructions. This report does not classify arbitrary generated program bodies as formulated explanatory theories. Whether a particular run formulates claims, locates blame and revises them is uninspected without candidates and criticisms. The code structurally supplies feedback and iteration, but that alone does not establish theory-builder conditions 1–4, learning, or a reflective theory builder. The static method texts themselves are not criticized/revised by this route. Localized candidate code is inspectable; finer addressability of a formulated theory remains uninspected.

#### RT-RTE-tool-admission
Label: Automatic Python tool admission

Python completion/score decision → executor.store_tool → ToolManager.add_new_tool → local metadata, code/description files and persistent vector index → later retrieval. Owner: agent gate and executor/manager. Model generates code and generality score; software compares score and checks name existence. Human starts the task but does not approve each retained candidate. Answer oracle: none. Mode: open task or lesson; trigger: completed Python node meeting configured threshold. Objective requested by judge is reusable/generalizable code, independently of any one candidate. Evidence: SRC-1, `oscopilot/agents/friday_agent.py`, `oscopilot/modules/executor/friday_executor.py`, `oscopilot/tool_repository/manager/tool_manager.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: store side effects and printed notification; existing names are skipped by executor.store_tool.
- Later read-back: manager reloads generated_tools.json and persistent Chroma; subsequent task/subtask retrieval delivers descriptions/code to models.
- Delegated visibility: inapplicable — same-process manager write and subsequent model-context delivery, not a delegated agent.
- Selection predicate: exact node type Python, completion flag, score >= configured threshold; executor rejects existing names; future retrieval uses description embeddings and top-k names.
- Invalidation or expiry: no automatic expiry in inspected path; manual maintenance can remove/replace entries. No versioned rollback or atomic multi-store recovery established.
- Activation or effect: durable code/descriptions become eligible model context; delivery is wired, behavior change and improved outcomes are unobserved.
- Evidence limits: a repaired score can authorize original code; assertions check counts, not semantics; no supplied retained-tool execution establishes activation or benefit.

> if node_type == 'Python' and isTaskCompleted and score >= self.score:
>     self.executor.store_tool(tool_name, code)
> --- `oscopilot/agents/friday_agent.py`

> score = repairing_result.score
> result = repairing_result.result
> --- `oscopilot/agents/friday_agent.py`

> return RepairingResult(status, code, critique, score, result)
> --- `oscopilot/agents/friday_agent.py`

The original code remains in self_refining's local variable: the repaired code is returned but not assigned there. Proposed change is a durable reusable tool, guided by generation prompts and the judge's generality rubric. Rejection occurs through completion/threshold/name predicates; after the manager writes, the route has no validation-driven automatic rollback. The persisted description is extracted from code's first matching docstring sentence, not a retained explanation of the judge's decision (SRC-1, `oscopilot/modules/executor/friday_executor.py`). Detailed memory transformations remain the memory analyst's responsibility.

For self-improvement attribution, boundary is FRIDAY plus retained tool state; horizon is later tasks/sessions; objective is future reusable computer-operating capability. The implementation connects task feedback to an admission decision, durable state and a later context-delivery path, with the candidate-identity defect above. This supports an improvement-directed dispositional pathway, not exercised self-improvement. Causal link 4—later operation depending on the admitted change—is unestablished, as is successful improvement. Under learning, no capacity/outcome comparison or attribution evidence is supplied. These limits do not negate the implemented retention path.

#### RT-RTE-api-qa
Label: API and QA alternate nodes

Planner type → QA model answer, or API-path extraction → reduced OpenAPI schema → model-generated Python → Env dispatch with type API. FridayAgent owns progression; model chooses answer/request code. Services, if directly invoked, are independent HTTP consumers: API server mounts Bing, audio2text and image_caption routers; Wolfram is imported/listed but not included in server_list. Image/audio adapters have separate model components above. Open-request mode; no expected-answer oracle or human per-response approval. Evidence: SRC-1, `oscopilot/agents/friday_agent.py`, `oscopilot/modules/executor/friday_executor.py`, `oscopilot/environments/env.py`, `oscopilot/tool_repository/manager/api_server.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: QA text is printed/logged; API programs return EnvState through the Python environment's API alias, with output determined by the generated program.
- Later read-back: inapplicable — this route declares no durable admission; successful node results would be current-run prerequisite context.
- Delegated visibility: service requests expose request payloads to local/remote services; exact payload is generated at runtime and unobserved.
- Selection predicate: model plan chooses QA/API; API path regex chooses first path; reduced schema chooses its operation/components.
- Invalidation or expiry: per-run graph resets; service temporary files can be deleted on normal audio completion; external service retention is uninspected.
- Activation or effect: QA calls model directly; API code executes in PythonJupyterEnv through the API alias. Independent service endpoints can also be called by other generated Python or external clients.
- Evidence limits: API execution is wired but not supplied with a runtime trace; live services, provider response compatibility and external persistence are unobserved.

> if node_type in ['Python', 'Shell', 'AppleScript']:
> --- `oscopilot/agents/friday_agent.py`

> name = "Python"
> aliases = ["py", "API"]
> --- `oscopilot/environments/py_jupyter_env.py`

The completion policy is branch-specific: QA/API do not enter code self-refinement. This does not establish their outputs are correct. Likewise the prompt's “only listed APIs” instruction is model-facing policy, not a restriction on Python networking or subprocess capability (SRC-1, `oscopilot/prompts/friday_pt.py`, `oscopilot/modules/executor/friday_executor.py`).

#### RT-RTE-course-learning
Label: Course design and lesson execution

course_learning.py → SelfLearning.continuous_learning → prior course/demo extraction → SelfLearner.design_course → lessons through agent.run → save_json → next curriculum. Owner: SelfLearning while-loop; model proposes curriculum, code admits parsed course and invokes each lesson. Human supplies software/package/demo; no per-lesson approval is present. Bounded subject curriculum with an unbounded driver; objective is proficiency in operating software via a chosen package. Answer oracle: course Input/Output fields describe desired interfaces, not supplied correct outcomes. Guidance requests progressive, generalizable, nonduplicated lessons based on prior courses. Evidence: SRC-1, `course_learning.py`, `oscopilot/agents/self_learning.py`, `oscopilot/modules/learner/self_learner.py`, `oscopilot/prompts/friday_pt.py`, `oscopilot/tool_repository/basic_tools/text_extractor.py`, `oscopilot/utils/utils.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: no explicit final result from continuous_learning; each lesson invokes the task agent and can change files/tools.
- Later read-back: course JSON is read at initialization; in-process course dictionary supplies up to the last fifty entries to later curriculum design. save_json merges dictionary entries on disk.
- Delegated visibility: inapplicable — same agent is called synchronously; optional TextExtractor invokes that agent and reads the last planner node's return_val.
- Selection predicate: software/package selects course filename; recent dictionary entries select curriculum context; new_course.items selects executed lessons.
- Invalidation or expiry: in-memory curriculum context cuts to last fifty entries when longer; older course content remains on disk; overlapping lesson keys update entries. No success-conditioned rollback in this driver.
- Activation or effect: model-designed lessons become direct agent tasks; admitted tools can enter the ordinary retained-tool path. Successful learning or behavioral dependence on prior course content is unobserved.
- Evidence limits: course progression receives prior lesson text, not checked pass/fail records. Agent.run can catch failure and return normally; saving afterward therefore is not evidence that the course was mastered.

> new_course = self.learner.design_course(software_name, package_name, demo_file_path, file_content, prior_course)
> self.course.update(new_course)
> self.learn_course(new_course)
> save_json(prior_course_path, new_course)
> --- `oscopilot/agents/self_learning.py`

Admission is software/model-driven: parser output becomes curriculum without an independent lesson-success gate. Parse/call failures can stop progress, but there is no designed rollback of prior host effects. One-stage self_learning also saves a newly designed course after lesson calls; unlike continuous_learning it does not update self.course before execution. Persistent memory details and curriculum-record semantics are left to the memory member. No claim is made that curriculum text constitutes a revised explanatory theory or that the fixed course-design method improves itself.

#### RT-RTE-manual-maintenance
Label: Manual tool maintenance

Caller-selected file/name → add_tool extracts description → add_new_tool overwrites/adds; or caller-selected name → delete_tool removes index/JSON/code/description. Owner: caller and ToolManager. A human following the tutorial can supply content by selecting/editing the file; the API itself also admits programmatic callers, so human authorship/approval is not intrinsic. Mode: maintenance, not automatic candidate comparison. Answer oracle: none. Evidence: SRC-1, `oscopilot/tool_repository/manager/tool_manager.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: write/delete side effects and console messages.
- Later read-back: new manager reloads metadata/index; retained descriptions/code enter ordinary retrieval and generation.
- Delegated visibility: inapplicable — no agent delegation; file contents enter the manager directly.
- Selection predicate: caller supplies exact tool name/path; description regex must match for add; existing name selects replacement.
- Invalidation or expiry: explicit delete/overwrite; no version history or transactional recovery in inspected functions. delete_tool updates disk/index but does not delete the in-memory generated_tools entry.
- Activation or effect: maintenance changes future eligible context, not automatic execution of the supplied file; runtime behavioral effect remains unobserved.
- Evidence limits: no score, execution test or semantic safety gate on direct manager add; deletion may leave stale current-instance code metadata.

> toolManager.add_new_tool(info)
> print(f"Successfully add the tool: {tool_name} with path: {tool_path}")
> --- `oscopilot/tool_repository/manager/tool_manager.py`

> if program_name in self.generated_tools:
>     print(f"\033[33mTool {program_name} already exists. Rewriting!\033[0m")
>     self.vectordb._collection.delete(ids=[program_name])
> --- `oscopilot/tool_repository/manager/tool_manager.py`

Proposal guidance is the caller's code and matching docstring, not the runtime judge. Rejection can follow missing description, invalid I/O or assertion failure, not quality comparison. Recovery requires caller repair/replacement; deleting a previous index entry before subsequent writes is not rollback. This is a distinct admission mechanism from the automatic new-name gate.

#### RT-RTE-example-loops
Label: Light and vision execution loops

Example caller → fresh message list → model response → first fenced block → Env → appended response/result → repeat until response includes a terminal phrase. Vision additionally captures/resizes/saves screenshots, calls OCR, and appends image plus coordinate text before each decision. Owner: LightFriday's while-loop; model chooses next program and completion phrase. Human supplies initial task/configuration. Mode: open requests with prompt-defined desktop constraints, not controlled experiments. Answer oracle: none; screenshots and OCR are observations, not reference outcomes. Evidence: SRC-1, `examples/light_friday/light_friday.py`, `examples/friday_vision/friday_vision.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: printed model text and Env result/error strings; loop returns after terminal substring detection.
- Later read-back: inapplicable — these loops do not declare a retained-tool admission/read-back path; their message lists are ordinary current-task history. Vision PNGs are saved but no later-session reload path was established.
- Delegated visibility: OCR receives screenshot bytes; chat receives accumulated history and, in vision, screenshot image/coordinate text; generated programs execute via shared Env.
- Selection predicate: regex selects first fenced code block; model selects actions; substring Execution Complete or Execution Interrupted stops after processing response.
- Invalidation or expiry: message list is rebuilt per run; inspected loop does not compact growing turns/images or bound iteration count.
- Activation or effect: code goes directly to Env without FridayAgent judge/repair gate; vision requests mouse/keyboard operation. Actual desktop effects are unobserved.
- Evidence limits: prompt permission and restrictions are not deployed grants or enforcement. OCR key is an empty placeholder; endpoint/model compatibility and task success are untested.

> message.append({"role": "system", "content": response})
> --- `examples/light_friday/light_friday.py`

> if 'Execution Complete' in response or 'Execution Interrupted' in response:
>     break
> --- `examples/light_friday/light_friday.py`

These routes replace neither production prompts nor weights; ordinary program/host effects may persist. Failures are fed back as text, not guaranteed rollback. The vision prompt's instruction to use screenshots and check every step is a requested policy, not an execution restriction.

### Claims

#### RT-CLM-agent-improvement
Label: Claimed self-improving agent

Claimed operation: operating-system-integrated agents improve themselves while automating tasks. Evidence layer: doctrine/design, SRC-1, `setup.py`; it is not an observed result. The runtime's concrete improvement-directed mechanisms are tool admission and curriculum-generated practice. [RT-RTE-tool-admission](#rt-rte-tool-admission) bounds dispositional versus exercised self-improvement; [RT-RTE-course-learning](#rt-rte-course-learning) does not equate saved lessons with learned capacity.

> description="An self-improving embodied conversational agents seamlessly integrated into the operating system to automate our daily tasks.",
> --- `setup.py`

The shipped GAIA driver has an external answer oracle in benchmark mode: task["Final answer"] is copied to groundtruth and compared to a postprocessed model answer using exact string equality. That oracle is not used to admit retained tools or repair candidates. The single-task branch comments out agent.run and supplies a literal result; the batch branch calls agent.run and appends result rows with an empty reasoning_trace. Consequently neither branch's existence demonstrates benchmark performance. Evidence: SRC-1, `examples/GAIA/run_GAIA.py`.

> if result == task["Final answer"]:
>     correct += 1
> --- `examples/GAIA/run_GAIA.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-method-instructions
Label: Method prompt authority

Consumer: planner/executor/judge/learner model calls. Channel: system/user messages assembled from shipped prompt strings and task/state fields. Force: model-interpreted instructions; parser/branch consumers then give selected outputs control over host execution and graph progression. Horizon: each invocation and consequent rounds/tasks; prompts themselves remain shipped code, not learned weights. Evidence: SRC-1, `oscopilot/utils/utils.py`, `oscopilot/prompts/friday_pt.py`, `oscopilot/modules/executor/friday_executor.py`. Authority depends on model interpretation and downstream parsing, not reliable compliance.

#### RT-BAP-tool-context
Label: Retained tool context authority

Consumer: planner and Python code-generation model. Channel: retrieved descriptions for decomposition, selected retained code serialized into relevant_code for generation. Force: contextual guidance/examples that can shape newly generated code; not an unconditional direct invocation of stored code. Horizon: later tasks and manager instances sharing retained state. The automatic and manual writer routes above both reach this channel. Evidence: SRC-1, `oscopilot/agents/friday_agent.py`, `oscopilot/modules/retriever/vector_retriever.py`, `oscopilot/tool_repository/manager/tool_manager.py`, `oscopilot/modules/executor/friday_executor.py`.

> relevant_code = self.retriever.retrieve_tool_code_pair(retrieve_name)
> --- `oscopilot/agents/friday_agent.py`

> relevant_code=relevant_code
> --- `oscopilot/modules/executor/friday_executor.py`

#### RT-BAP-course-tasks
Label: Curriculum task authority

Consumer: the reused FridayAgent and next SelfLearner course-design call. Channel: each lesson string becomes agent.run input; recent prior-course JSON becomes model context. Force: lesson text supplies the operative user task; prior course guides requested progression. Horizon: curriculum rounds and subsequent sessions that reload course JSON. This authority does not authenticate successful lesson completion. Evidence: SRC-1, `oscopilot/agents/self_learning.py`, `oscopilot/modules/learner/self_learner.py`.

> self.agent.run(lesson)
> --- `oscopilot/agents/self_learning.py`

## Annotations

none
