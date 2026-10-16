---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "SkillWeaver runtime baseline: website exploration, Python skill admission, native execution and alternate consumers at the frozen Git revision."
run-id: AAS-2026-10-14-skillweaver-c921cc7a5ed0-01
reviewed-boundary: f2a63d65d0f6ff46ac30e817cede8797f8f25b97
---

# SkillWeaver runtime report

## Runtime account

SkillWeaver's consequential work is to turn browser practice into reusable Python functions and make those functions available during later tasks. The inspected builder connects task proposal, task execution, success judgment, synthesis, replacement and checkpointing. This is implementation evidence, not evidence that a deployed agent improved. The sole source is SRC-1 at the [boundary](boundary.md#source-register). No execution trace or causal experiment was supplied.

An ordinary shipped builder invocation is `python -m skillweaver.explore reddit <out_dir>`. Its CLI constructs separate agent, success-check and synthesis `LM` objects; defaults are `gpt-4o`, `gpt-4o` and `o3-mini`. It applies browser patches, optionally reloads an initial library, obtains website containers and login storage state, and creates browser contexts. Each worker owns a browser wrapper; workers share one knowledge base. A semaphore limits worker occupancy and a knowledge-base lock serializes task choice and admission, not the entire task attempt. Browser actions can therefore overlap with another worker's update. These are asyncio workers in one Python process, not independently isolated agents (SRC-1, `skillweaver/explore.py`).

The [RT-RTE-explore-practice](#rt-rte-explore-practice) selects an untested function using a configured test/explore schedule and a softmax over interaction count minus version, or asks the agent model to propose a useful website task. Test arguments are model-generated from a schema, function source and current browser observation. The native [RT-RTE-native-task](#rt-rte-native-task) retrieves task-relevant function descriptions once, then runs at most ten generated actions in exploration. Each step gets the latest accessibility tree, title, URL and screenshot, plus formatted earlier actions and the selected library descriptions. Earlier screenshots and intermediate accessibility trees are not all replayed into the action prompt. This is code-directed context selection, not a persisted summary or model-controlled compaction. Task-local states, actions and disabled names are fresh per attempt; only returned trajectories and the shared library cross back into the builder (SRC-1, `skillweaver/agent.py`, `skillweaver/attempt_task.py`).

The model proposes Python `act(page)` code or a terminal result. The generator requests structured output and tries to repair sanity-check errors up to five times. The caller reformats the code, writes a module containing the entire library unless reference-only mode is active, imports it into the host Python process and awaits `act(page)`. Results, warnings, captured stdout and exceptions become the next action context. Observation retries cover a particular navigation-destroyed-context error. Locator recovery is optional and narrower: the [RT-RTE-locator-recovery](#rt-rte-locator-recovery) can replace a failed locator and retry its original operation. Task termination is a model result, a syntactic named-call plus result-field test shortcut, or exhaustion of the step count. The shortcut requires a matching call node somewhere in the generated source, no recorded exception and no recorded recovery attempt; it does not establish that the named skill ran. The API returns states and actions; the CLI principally emits logs, action modules, state artifacts and trajectory text (SRC-1, `skillweaver/agent.py`, `skillweaver/attempt_task.py`, `skillweaver/environment/browser.py`).

After a test whose last action source contains a matching named-call node and whose result records no exception or recovery attempt, the builder increments a test counter. This metadata update does not establish dynamic execution of the named skill. Otherwise a success-check model reads the task, formatted trajectory and final screenshot. Its boolean can trigger the [RT-RTE-skill-admission](#rt-rte-skill-admission). Admission asks a synthesis model for new or replacement function definitions, checks them, merges definitions by name, resets changed functions' test counts and saves code, metadata and semantic text. The success model is not an independent answer oracle. The test shortcut checks syntactic named-call occurrence and recorded result fields, not dynamic execution of the named skill or the intended website outcome (SRC-1, `skillweaver/explore.py`, `skillweaver/knowledge_base/knowledge_base.py`).

### Controls and forcing cases

The capability surface is host-process Python plus a Playwright page and loaded skill bodies, not just a finite list of advertised tools. Current function visibility is a caller-selected presentation/filtering set; it is not a runtime capability grant. The actual deployed OS credentials, filesystem restrictions, network policy and website permissions are uninspected. Browser cookies grant website access according to an external website contract. Chromium sandbox configuration depends on `DOCKER`; it does not isolate imported Python action modules (SRC-1, `skillweaver/environment/browser.py`, `skillweaver/agent.py`).

Four source-supported forcing cases bound the controls:

1. **Repeated invalid proposals:** both generation and skill synthesis have bounded retries, but their last response still proceeds after exhaustion. The synthesis path unconditionally calls `_apply` after its loop. Static checks are therefore best-effort repair, not an invariant admission gate. A parseable last candidate can still carry checker violations; a syntactically invalid one can instead fail during parsing. See [RT-RTE-skill-admission](#rt-rte-skill-admission).
2. **Advertised versus executable functions:** native retrieval supplies descriptions of selected functions, but module assembly includes all library code. Hiding unverified functions affects `get_functions`, not this assembly. Reference-only mode really omits library code, but does not sandbox the newly generated action. See [RT-RTE-native-task](#rt-rte-native-task).
3. **Recovery bypass of the ordinary action-generation route:** recovery uses model-produced locator expressions, `eval`, locator type/count checks and element identity comparison before invoking the failed operation. Its check is a local consistency check against the model-selected element, not proof of user intent. Unsupported exceptions or exhausted recovery are re-raised. See [RT-RTE-locator-recovery](#rt-rte-locator-recovery).
4. **Alternate consumer and benchmark entry:** Browser-Use gets controller callbacks constructed with `exec`, not the native generator's sanity-check loop. Benchmark tasks run in subprocesses but still use host Python execution. The benchmark source also imports a missing computer-use module unconditionally, preventing a clean-source end-to-end claim for that driver. See [RT-RTE-browser-use](#rt-rte-browser-use), [RT-RTE-benchmark-evaluation](#rt-rte-benchmark-evaluation) and [RT-ABS-cua-module](#rt-abs-cua-module).

Load-bearing control ownership and strength are local. The generation owner is `codegen_generate`; its enforcement point is a retry decision and its guarantee strength is **best effort**. The synthesis owner is `KnowledgeBase.update`; its enforcement point is likewise a retry decision, not final acceptance. Both have implementation conclusion status **wired**, operation conclusion status **uninspected**. They require external provider responses and static-checking dependencies; neither establishes safety, correct website outcomes or human approval. The recovery owner is the locator wrapper: selected expression/type/count/identity checks are a local **protocol**, wired but operation uninspected, covering patched locator methods only. Direct Python, Browser-Use callbacks and other exceptions are alternate paths outside that protocol. The evaluation caller's `hide_unverified` setting is a visibility **policy**, wired but operation uninspected, and does not constrain all executable library definitions (SRC-1, `skillweaver/agent.py`, `skillweaver/knowledge_base/knowledge_base.py`, `skillweaver/environment/patches.py`).

There is no per-content human decision in the inspected automatic admission route. The human or caller supplies entry arguments, credentials and an optional initial library; starting exploration is not approval of each synthesized function. Retained skills are live symbolic execution material through [RT-BAP-library-execution](#rt-bap-library-execution); docstrings additionally supply model-interpreted guidance. No target-owned model weight update is wired in these inspected paths. Endpoint fixity is separately recorded below, not inferred from skill persistence.

Additional SRC-1 implementation coverage beyond the boundary's initial inventory includes complete action generation/execution, task selection helpers, synthesis retry exhaustion, controller construction, browser configuration, recovery expression checking and continuation, and benchmark failure interfaces. Doctrine coverage includes the full procedural-update base/single templates and README. Evaluator bodies, all shipped skill bodies, container internals and provider/Browser-Use internals were not exhaustively inspected; no completeness, reliability, safety or performance conclusion is drawn for them. The missing computer-use implementation is an absent shipped reference, not a reason to change the frozen functional boundary.

## Shared records

### Components

#### RT-CMP-lm
Label: LM provider-backed decision components

Source-native identity: `LM` instances for agent generation/retrieval, task proposals, test arguments, success judgment, synthesis and optional recovery. Representational form: distributed-parametric models behind OpenAI/Azure services. Storage substrate: external provider parameters; local Python clients and model-name strings. These roles can use separate instances and different names; shared wrapper identity does not mean shared model parameters.

Parameter changes during operation: no target-owned weight mutation in inspected `LM` calls; provider-side changes are uninspected. Exact versions are not necessarily pinned: CLI defaults are aliases. Mutable endpoint resolution to a different model is possible under externally configured Azure/OpenAI contracts, which are uninspected. The Browser-Use agent separately receives `AzureChatOpenAI`; its planning internals and version resolution are uninspected. SRC-1, `skillweaver/lm.py`, `skillweaver/explore.py`, `skillweaver/attempt_task_browser_use.py`.

> self.model = model
> self.max_concurrency = max_concurrency
> self.semaphore = asyncio.Semaphore(max_concurrency)
> self.client = _get_openai_client(model)
> --- `skillweaver/lm.py`

The common completion path uses five retries with exponential backoff, JSON parsing and timing/token logging. Its semaphore bounds concurrency per instance. `LM.json` calls the provider parse API directly rather than this retry/semaphore path; no inspected main builder caller uses that alternative. These mechanisms do not establish provider availability or valid task judgments.

#### RT-CMP-embed
Label: Optional embedding model

Source-native identity: `embed` calling `text-embedding-3-small`. Representational form: distributed-parametric model and dense vectors. Storage substrate: provider weights and an in-process `_embed_cache` keyed by input string. Parameters do not change through target-owned calls; provider updates are uninspected. Exact weights/version are not pinned; the alias endpoint may resolve differently under the external service contract. SRC-1, `skillweaver/knowledge_base/knowledge_base.py`.

> result = await oai.embeddings.create(input=string, model="text-embedding-3-small")
> embed = np.array(result.data[0].embedding)
> _embed_cache[string] = embed
> --- `skillweaver/knowledge_base/knowledge_base.py`

This helper affords top-five dot-product similarity selection; the inspected native task path instead calls model-mediated `retrieve`. Embedding selection is not assumed active in those invocations.

### Operative objects

none declared in this member

### Routes

#### RT-RTE-native-task
Label: Native task generation and execution

Endpoints and owner: caller task/browser/library → `attempt_task` → `codegen_generate` → `codegen_do` → states/actions. Principal: configured caller with its website session and host process permissions. Symbolic code rules assemble context; a distributed-parametric model selects actions from natural-language task/library guidance and browser observations. The host executes symbolic Python and Playwright effects. SRC-1, `skillweaver/attempt_task.py`, `skillweaver/agent.py`, `skillweaver/create_skill_library_prompt.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: states and actions, including outputs, exceptions and terminal text; the CLI writes artifacts.
- Later read-back: a caller can reload a persisted library before a later attempt; this function itself does not revise that library.
- Delegated visibility: the action model receives selected skill descriptions, current screenshot/tree and formatted earlier actions; host execution receives all library code unless reference-only.
- Selection predicate: production tasks always call model-mediated retrieval; exploration/test retrieval is configurable; fallback test context includes verified functions and the target function.
- Invalidation or expiry: task-local disabled function names last for the attempt; retrieval occurs once before the loop; module cache entries are removed before import.
- Activation or effect: wired Python execution and website actions; actual invocation and dependence on a particular retrieved function remain unobserved.
- Evidence limits: no supplied target run; selected descriptions do not prove selected-only execution, correctness or sandboxing.

Decision roles: caller supplies task and limits; model proposes next action or termination; code retries checker failures, but has no final veto after five responses. In test mode, code also terminates early when the generated source contains a matching `ast.Name` call node and the result records no exception or recovery attempt. This is a syntactic named-call plus result-field shortcut, not evidence that the skill executed. Answer oracle: none for ordinary production tasks; model terminal text and the test shortcut are not reference outcomes. Operating mode: open user tasks or builder-supplied bounded practice. Recovery captures exceptions and optionally invokes the separate recovery route; arbitrary Python effects are not rolled back.

> for _ in range(5):
> --- `skillweaver/agent.py`

> else:
>     errors = "You did not provide any Python code, but you also did not provide a result for `terminate_with_result`. Please provide one or the other."
>
> return response
> --- `skillweaver/agent.py`

> kb_code = knowledge_base.code if not as_reference_only else ""
> --- `skillweaver/agent.py`

> module = importlib.__import__(module_name)
> output = await module.act(page)
> --- `skillweaver/agent.py`

> for node in ast.walk(tree):
>     if isinstance(node, ast.Call):
>         if isinstance(node.func, ast.Name) and node.func.id == function_name:
>             return True
> --- `skillweaver/attempt_task.py`

The test-mode early-termination branch uses this AST predicate on `action["python_code"]` after the action executor returns. For example, `async def act(page):\n    if False:\n        await target(page)` contains a matching call node but never executes `target`. If the result records no exception and no recovery attempt, the shortcut can still terminate the attempt and the builder can increment the test counter. This is a deduction from inspected implementation, not an observed run (SRC-1, `skillweaver/attempt_task.py`, `skillweaver/explore.py`).

#### RT-RTE-explore-practice
Label: Scheduled exploration and practice

Endpoints and owner: exploration CLI → worker/browser iteration → native task attempt → test-count update or success-judged synthesis → iteration checkpoint. `explore` owns scheduling and `_run_explore_iteration` owns progression. Shared library locks protect selection/admission sections, while a worker semaphore controls parallel occupancy. Context is current observation, existing function names/semantic text for proposals, or selected function source/schema for test arguments. SRC-1, `skillweaver/explore.py`, `skillweaver/knowledge_base/check_success.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: iteration artifacts, success-check/update diagnostics and checkpoint; the orchestration coroutine finishes after gathered iterations.
- Later read-back: shared updated library reaches later iterations; saved prefixes support later CLI reload.
- Delegated visibility: separate success-check call gets task, trajectory and final screenshot; synthesis gets its own update prompt, not the full browser worker context.
- Selection predicate: schedule and nonempty untested set select testing; otherwise model task proposal; softmax selects test function.
- Invalidation or expiry: worker availability resets after iteration; configured navigation returns browsers home; task frames end while library state persists.
- Activation or effect: wired browser practice, counters and conditional synthesis; actual exercised practice and resulting benefit unobserved.
- Evidence limits: syntactic named-call occurrence plus passing result fields establishes neither dynamic execution of the named skill nor outcome verification; success-model judgment is not an independent oracle; no complete execution trace supplied.

Decision roles: model proposes tasks/arguments; software samples tests and applies the syntactic named-call plus result-field predicate; a passing predicate increments the named function's test counter without establishing its execution. Another model judges attempts that do not pass this shortcut. Human contribution is configuration/initial content, not per-update veto. Operating mode is bounded curriculum controlled by iteration count and schedule. Answer oracle: no expected answer/reference outcome supplied to the exploration success checker. The shortcut triggers test-counter bookkeeping, not synthesis. Synthesis is triggered by the success-check model's positive judgment on an attempt that did not pass the shortcut; neither branch establishes an independently verified website outcome.

> return last_has_call_to_test_function and not (
>     last_has_exception or last_has_recovery_attempts
> )
> --- `skillweaver/explore.py`

> knowledge_base.save(f"{iter_dir}/kb_post")
> --- `skillweaver/explore.py`

Iteration exceptions write `error.txt` and tracing is stopped in `finally`; this is diagnostic recovery, not transaction rollback. The CLI finally calls `os._exit(0)`, so process success alone is not a reliable successful-exploration signal (SRC-1, `skillweaver/explore.py`).

#### RT-RTE-skill-admission
Label: Procedural skill synthesis and merge

Endpoints and owner: successful-attempt task/trajectory → `KnowledgeBase.update` → candidate Python → checker retries → `_apply` → checkpoint. Model proposal is shaped by existing verified or specially included function source, semantic text and update instructions. Symbolic checker/merge code governs local mutations. SRC-1, `skillweaver/knowledge_base/knowledge_base.py`, `skillweaver/knowledge_base/code_verification.py`, `skillweaver/templates/kb_procedural_update_base.md`, `skillweaver/templates/kb_procedural_update_single.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: procedural attempts, violations, reasoning and instructions; semantic diagnostics remain `None` in this implementation.
- Later read-back: merged function code/docstrings and metadata are available to subsequent task selection, retrieval and execution; saved prefixes can be reloaded.
- Delegated visibility: synthesis sees filtered function bodies and formatted trajectory rather than every stored action artifact; checker sees candidate plus existing code context.
- Selection predicate: builder success judgment triggers synthesis; checker violations trigger retry up to ten attempts, not a final rejection gate.
- Invalidation or expiry: same-name function replacement resets test count and advances version; other function definitions remain; changed candidates supersede bodies in memory.
- Activation or effect: wired mutation of executable library; later execution is possible but no run establishes activation or improvement.
- Evidence limits: static checks are not behavioral verification; exhausted retries can still apply a violating candidate; no retained run proves reliable synthesis.

Trigger/proposed change: successful task attempt licenses new generalized automation or modification/documentation of existing skills. Proposer: synthesis model. Decider: software loop and unconditional merge; human veto is not wired here. Rejection ability: checker can delay a candidate via retry; parse/format errors can raise; no final checker veto. Recovery/rollback: earlier checkpoint prefixes can be supplied manually to later invocations, but no automatic transaction rollback or selection of a best prior candidate is shown. What persists: function definitions/docstrings plus metadata, not model parameters; diagnostic reasoning is separately logged. The active template requests usage logs, documentation of unexpected behavior and generalization, but requested semantics are not guaranteed.

> while len(procedures_update_diagnostics["attempts"]) < 10:
> --- `skillweaver/knowledge_base/knowledge_base.py`

> self._apply(updated_code, reference)
> --- `skillweaver/knowledge_base/knowledge_base.py`

> updated_functions[node.name] = node
> --- `skillweaver/knowledge_base/knowledge_base.py`

> If you used an existing function and the result was unexpected, make sure to update the documentation for that function to ensure that it can be used correctly in the future. Unexpected results should be documented if they occur. You may also want to provide examples of successful usage too.
> --- `skillweaver/templates/kb_procedural_update_base.md`

Operating mode: trace-fed synthesis after bounded practice, with checker-driven repair. Answer oracle: static rules supply coding constraints; they are not an expected website result. The checker prohibits selected constructs and requires docstrings and a `page.goto` occurrence, but does not prove first-command placement or safe behavior. Runtime account here establishes a change-admission mechanism, not a theory-builder classification: the prompt's generalized procedure and documentation request alone do not establish content-directed criticism of a formulated theory.

Self-improvement attribution: within SkillWeaver's builder-plus-consumer boundary, horizon later iterations/tasks, objective reusable website-task automation, this is an improvement-directed dispositional self-change path. Evidence can shape synthesis, merged skills alter its own later action machinery, and the native/controller consumers give that result behavioral authority. No supplied execution establishes the four exercised causal links, especially subsequent behavior causally depending on a change. Successful improvement and learning are not established by persistence or admission.

#### RT-RTE-locator-recovery
Label: Model-assisted locator recovery

Endpoints and owner: patched locator exception → execution-context handler → model choice/expression → checked locator → original action retry. Trigger scope is timeout, strict-mode or invalid-selector errors in mapped functions. The wrapper identifies the failed source line, current locals and accessibility candidates; a per-handler visited-locator map prevents repeatedly handling the same location. SRC-1, `skillweaver/environment/patches.py`, `skillweaver/agent.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: result of retrying the original locator method, or raised original exception; recovery records join action results.
- Later read-back: successful recovery annotations can enter formatted trajectories; the inspected builder initially serializes trajectories without enabling recovery inclusion, so durable repair through that particular update input is not established.
- Delegated visibility: recovery model receives failed source, filtered/truncated locals and current tree, then failures of its prior proposals; no screenshot is supplied in this prompt.
- Selection predicate: matching exception categories, active execution-context handler and previously unvisited filename/line; model selects a candidate element.
- Invalidation or expiry: handler is removed and execution context reset after action execution; failed library names remain disabled for the current task only.
- Activation or effect: checked replacement locator can perform the original website operation; no observed successful recovery supplied.
- Evidence limits: count/identity checks verify agreement with the model-selected candidate, not intended outcome; nonpatched effects and arbitrary Python are outside the protocol.

Decision roles: model proposes locator/element; software vetoes malformed expressions, action substrings, wrong type/count or mismatched element, at most five attempts. No human approval is requested. Answer oracle: accessibility candidate identity is a consistency reference, not an independent intended-target oracle. Operating mode: bounded repair on an execution exception. It repairs an immediate action, not library code directly; durable admission remains separate. Failed recovery re-raises, and previous website effects are not rolled back.

> locator = eval(locator_code, None, locals_)
> --- `skillweaver/environment/patches.py`

> return await getattr(locator, action_name)(*locator_args, **locator_kwargs)
> --- `skillweaver/environment/patches.py`

#### RT-RTE-browser-use
Label: Browser-Use skill-controller adapter

Endpoints and owner: adapter CLI → library retrieval → controller construction → external `Agent.run`; registered callback → current page → captured skill function. SkillWeaver owns retrieval/wrappers, while the external agent owns next-step planning and termination. SRC-1, `skillweaver/attempt_task_browser_use.py`, `skillweaver/knowledge_base/knowledge_base.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: controller object to the caller; external agent runs with conversation logging.
- Later read-back: saved library is loaded for a new adapter invocation; this path does not revise it.
- Delegated visibility: retrieved skill callbacks/docstrings are supplied to the external controller; exact downstream provider context is uninspected.
- Selection predicate: model retrieval names the exposed functions; controller checks names exist and captures those function objects after executing library code.
- Invalidation or expiry: controller is constructed per invocation; no native disabled-name or recovery-record protocol applies to its callbacks.
- Activation or effect: registered callbacks can execute skills against the external browser's current page; exercise unobserved.
- Evidence limits: external Browser-Use implementation/compatibility is not frozen; callback generation using `exec` is not an isolation envelope.

> exec(CODE, globals(), {"functions": function_objects})
> --- `skillweaver/knowledge_base/knowledge_base.py`

> NOTE: Exception tracking cannot be done with Browser Use controller.
> --- `skillweaver/knowledge_base/knowledge_base.py`

This alternate route bypasses the native action-generation checker. It expands an external action space rather than transferring ownership of the external agent's controls to SkillWeaver.

#### RT-RTE-benchmark-evaluation
Label: Benchmark subprocess and scoring path

Endpoints and owner: benchmark selection → subprocess per task → single-task browser attempt → evaluator → `eval.json`/aggregate result. SRC-1, `skillweaver/evaluation/evaluate_benchmark.py`, `skillweaver/evaluation/evaluate_single_task.py`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: per-task cost/status/length and benchmark artifacts, contingent on successful subprocess execution.
- Later read-back: source library is reloaded per task; existing task directories are reused/skipped and result files read; no automatic score-fed library update is shown in these drivers.
- Delegated visibility: subprocess receives task/config/library prefix and caller options; native attempt sees the configured task and filtered function descriptions.
- Selection predicate: requested task IDs/site/set or reduced intent templates; `enable_unverified` changes description visibility; model name selects the native versus referenced computer-use branch.
- Invalidation or expiry: changed benchmark metadata causes an output-directory mismatch error; existing task folders are skipped, not automatically invalidated.
- Activation or effect: source supplies scoring and result collection wiring, but a missing unconditional import and argument mismatch prevent assuming the shipped entry executes cleanly.
- Evidence limits: no benchmark run or scores supplied; evaluator bodies not exhaustively inspected; the computer-use implementation is absent from the pin.

Decision roles: caller selects set/options; code chooses tasks and evaluator; the evaluator judges the returned trajectory/final page against task configuration. Answer oracle: benchmark task configuration/reference checks, unlike exploration's model-only success judgment; exact evaluator-specific rules remain uninspected here. Operating mode: fixed benchmark, optionally reduced or explicitly selected. No score-driven admission or rollback occurs in these inspected drivers.

> from skillweaver.openai_cua.attempt_task import attempt_task as attempt_task_cua
> --- `skillweaver/evaluation/evaluate_single_task.py`

> if lm.model == "computer-use-preview":
> --- `skillweaver/evaluation/evaluate_single_task.py`

The absent import is unconditional, so even a non-computer-use choice depends on resolving it. Additionally the benchmark forwards `agent_type`, but the inspected single-task CLI parser does not declare that option. The README names `skillweaver.evaluate_benchmark`, whereas the tracked implementation is under `skillweaver/evaluation/`. These are source-level reproducibility limits, not experimentally observed failures. A caller supplying missing environment code or manually invoking another path could change the result; that is not established by this pin.

### Claims

#### RT-CLM-self-improvement
Label: Claimed autonomous skill-based improvement

Claimed operation and source: SRC-1, `README.md`, describes autonomous discovery/practice/distillation and enhanced capacity.

> SkillWeaver is a skill-centric framework enabling agents to self-improve by autonomously synthesizing reusable skills as APIs.
> --- `README.md`

- doctrine conclusion status: claimed
- implementation conclusion status: wired
- benefit conclusion status: uninspected

The implementation supports the connected builder/consumer disposition described in [RT-RTE-skill-admission](#rt-rte-skill-admission), not achieved robustness, improved capacity or exercised causal self-improvement. The quote reports project intent; no registered experiment supports its benefit claim.

### Evidenced absences

#### RT-ABS-cua-module
Label: Missing computer-use implementation at the reviewed pin

- implementation conclusion status: absent

Searched boundary: SRC-1 Git tracked tree at `f2a63d65d0f6ff46ac30e817cede8797f8f25b97`; query `git ls-tree -r --name-only HEAD skillweaver/openai_cua` returned no entries, while `skillweaver/evaluation/evaluate_single_task.py` imports that package. Evidence is the unconditional import quoted in [RT-RTE-benchmark-evaluation](#rt-rte-benchmark-evaluation). Supported conclusion: this registered source does not supply the referenced implementation, preventing source-only reconstruction of its computer-use branch and a clean-tree single-task evaluation entry. It does not establish that no external installation can supply it or that computer-use behavior never occurs.

### Behavioral-authority paths

#### RT-BAP-library-execution
Label: Retained library into later behavior

Consumer: native imported action module and Browser-Use captured callback. Channel: library code is inserted into generated modules or executed while building a controller. Force: symbolic Python definitions can perform website/host effects when invoked; retrieved docstrings separately guide model interpretation but do not force invocation. Horizon: later iterations and later tasks/sessions after save/reload. SRC-1, `skillweaver/agent.py`, `skillweaver/knowledge_base/knowledge_base.py`. Minimum passages are retained in [RT-RTE-native-task](#rt-rte-native-task) and [RT-RTE-browser-use](#rt-rte-browser-use). Delivery and executable availability are wired; observed activation, reliable compliance and benefit are uninspected.

## Annotations

none
