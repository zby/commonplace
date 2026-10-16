---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Reflexion's task-specific attempt, evaluation and reflection workflows, including alternate strategies and incomplete dependency paths."
run-id: AAS-2026-10-14-reflexion-19159b69b712-01
reviewed-boundary: "218cf0ef1df84b05ce379dd4a8e47f17766733a0"
---

# Reflexion runtime report

## Runtime account

Reflexion ships experiment drivers, not one enclosing agent runtime. The declared work is repeated reasoning, environment interaction and program generation with prior-attempt information. The [boundary](boundary.md) fixes four task families and the missing UCS and LeetCode dependencies. All evidence here is SRC-1 implementation or attributed design. No target was executed; saved results and notebook output cells were not examined as run evidence. Wiring below does not establish exercised reflection, improved answers or causal benefit.

### Ordinary invocation: programming

The shipped `programming_runs/run_reflexion.sh` invokes `main.py` with HumanEval Python, GPT-4, one pass and two iterations. The operator selects dataset, language, model, strategy and budgets; the driver owns subsequent progression. It reads JSONL, constructs generator/model/executor, and iterates dataset items not skipped by the output-line count. A task carries `prompt`, `entry_point` and reference `test`. The model proposes internal tests and an implementation; the executor produces Boolean outcomes and textual feedback. On failure, a separate model call requests an explanation, and the generator supplies the previous implementation, feedback and explanation to a successor call. The scheduler, not the model, decides when another call happens. See [RT-RTE-program-attempt](#rt-rte-program-attempt) and [RT-RTE-code-execution](#rt-rte-code-execution) (SRC-1, `programming_runs/run_reflexion.sh`, `programming_runs/main.py`, `programming_runs/reflexion.py`).

Natural-language instructions and feedback are interpreted by the model. In this ordinary Python path, generated code and tests are symbolic material consumed by execution facilities. The Rust executor can consume supplied Rust source independently, but the shipped Rust generator cannot complete its implementation call: it omits a required helper argument, as established in [RT-RTE-program-attempt](#rt-rte-program-attempt). A passing internal test set triggers reference evaluation; the final permitted iteration also triggers it even without internal success. `is_solved` follows that evaluator. The last implementation is written as `solution` even when unsolved: persisted output is not synonymous with an accepted correct program. The driver appends task fields, implementations, feedback and reflections to JSONL and returns no program object. Resume skips completed rows rather than reconstructing their reflection context. Success counters are not reconstructed from the result file (SRC-1, `programming_runs/reflexion.py`, `programming_runs/utils.py`).

This is a Python implementation trace conditional on dependencies, not a claim that the supplied checkout launches. Rust generation has a separate parent-code defect; acquiring missing dependencies alone would not repair it. `main.py` unconditionally imports the UCS module, which imports unavailable `lazzzy.ucs`, before strategy selection. Even a simple or ordinary Reflexion CLI invocation therefore has an import dependency on missing UCS code. Calling `run_reflexion` directly avoids that particular CLI import, but does not turn the unavailable search implementation into inspected evidence (SRC-1, `programming_runs/main.py`, `programming_runs/reflexion_ucs.py`).

### Material task routes

- **ALFWorld:** `main.py` initializes or reloads index-addressed environment configurations, runs sequential trials, optionally updates failed-task plans, and writes JSON snapshots. The environment is reset once per configuration, task-name prefixes select static examples, and the action model receives task, examples, at most three plans and current action/observation history. Text actions go to `env.step`; the host checks termination, repeated actions and a 49-step budget. Plans are generated after a whole trial, not through an agent tool. See [RT-RTE-alfworld-trial](#rt-rte-alfworld-trial) (SRC-1, `alfworld_runs/main.py`, `alfworld_runs/alfworld_trial.py`, `alfworld_runs/env_history.py`, `alfworld_runs/generate_reflections.py`).
- **HotPotQA:** three notebooks instantiate one agent per dataset question, run five rounds over agents not marked correct, log summaries and serialize agents. CoT receives either supporting paragraphs assembled from dataset annotations or no supporting context. ReAct instead gets Search/Lookup access through Wikipedia's explorer. Both produce an answer checked against a dataset key, then can request a failure diagnosis before resetting the attempt scratchpad. See [RT-RTE-hotpotqa-attempt](#rt-rte-hotpotqa-attempt) (SRC-1, `hotpotqa_runs/notebooks/CotQA_context.ipynb`, `hotpotqa_runs/notebooks/CotQA_no_context.ipynb`, `hotpotqa_runs/notebooks/ReactQA.ipynb`, `hotpotqa_runs/agents.py`, `hotpotqa_runs/util.py`).
- **WebShop:** `main.py` uses repeated fixed session IDs, JSON configurations and failure-triggered reflection updates. The client translates action strings into page-state changes and HTTP GET requests. Despite placing plans in `EnvironmentHistory`, the actual action-model call uses a separate string with no such plans. See [RT-RTE-webshop-trial](#rt-rte-webshop-trial). This is a forcing counterexample to a system-wide claim that persisted reflections reach the action model (SRC-1, `webshop_runs/main.py`, `webshop_runs/webshop_trial.py`, `webshop_runs/env_history.py`, `webshop_runs/generate_reflections.py`).

The model calls are ordinary text generation, not provider-native tool calls. Within these inspected loops, host code parses or forwards generated text and owns effects. No workers or approval protocol participate in the traced progression. This is a scoped control description, not an exhaustive absence claim about opaque provider or environment internals. Provider identities and unpinned local model loading are recorded under Components.

### Forcing cases and guarantees

Four source-inspected cases qualify the ordinary story; none was experimentally exercised.

1. **A candidate passes internal tests but fails reference tests.** The initial-pass branch breaks the outer pass loop even on reference failure. It does not request diagnosis of the reference failure. An empty generated test set also yields initial internal success in Python. Internal success is thus neither correctness nor a universal retry trigger (SRC-1, `programming_runs/reflexion.py`, `programming_runs/executors/py_executor.py`).
2. **Reflection without execution feedback.** Immediate-reflexion supplies `Test cases omitted`; immediate-refinement supplies `No self-reflection`. UCS delegates scheduling to missing search code. See [RT-RTE-program-variants](#rt-rte-program-variants). These paths prevent attributing one common evidence-responsive decision rule to every dispatched strategy.
3. **Stored WebShop plans omitted from action input.** The logger and reflection producer see a history representation that the action call does not use. Delivery to a log is not delivery to the action model (SRC-1, `webshop_runs/webshop_trial.py`).
4. **Timeouts and success signals have narrower coverage than their labels.** Python timeout handling does not terminate its worker thread; failure-output inspection executes generated definitions outside that timeout. ALFWorld returns success on `done`, although it reads `info['won']` into a different variable. HotPotQA compares normalized answer and key, which can ignore case, punctuation and articles but cannot establish factual correctness beyond the supplied key. These are distinct enforcement points, not interchangeable correctness or isolation guarantees (SRC-1, `programming_runs/executors/executor_utils.py`, `programming_runs/executors/py_executor.py`, `alfworld_runs/alfworld_trial.py`, `hotpotqa_runs/agents.py`, `hotpotqa_runs/environment.py`).

**Attempt-budget guarantee.** Owner: task driver. Enforcement: Python loop counters and ReAct halt checks. Strength: protocol. Covered paths: ALFWorld's 49 iterations; WebShop's 15 loop iterations; notebook's five rounds; ordinary programming's pass/iteration counters. Alternate paths: UCS scheduling is outside inspected parent code; direct calls can choose other budgets; `reset=False` changes HotPotQA reset behavior. External contract: calls to provider, environment and executor must return for counters to advance. This is not a wall-clock termination invariant.

- implementation conclusion status: wired
- operation conclusion status: uninspected

**Correctness labeling guarantee.** Owner: each family's host evaluator. Enforcement: reference-test execution, key comparison, `done` or full WebShop reward. Strength: best effort. Covered paths and exceptions are in the route records. Required external contracts: test validity, dependency execution semantics, authoritative dataset keys and environment/server terminal signals. Alternate Python/Rust/LeetCode evaluators have different effect and error boundaries; no universal correctness guarantee follows.

- implementation conclusion status: wired
- operation conclusion status: uninspected

**Generated-code isolation.** Owner: deployment operator, not these executor wrappers. Strength: no claimed guarantee. Python grants `exec`/`eval` access to host globals; Rust grants compilation and shell-launched execution in temporary directories. Capability surface includes arbitrary generated program effects reachable through those facilities. The current grant set is what the host process credentials and environment permit; these are not supplied. The deployed isolation envelope is uninspected. Timeouts and temporary paths do not demonstrate containment. See [RT-BAP-executable-code](#rt-bap-executable-code).

- implementation conclusion status: afforded
- deployment conclusion status: uninspected

### Change admission and coverage limits

Changes admitted by these loops are candidate programs and task-specific textual plans, not patches to the shipped scheduler or provider weights. Models propose; host conditions decide evaluation, replacement, append and later delivery. Starting an experiment is not human approval of each generated candidate. Per-content human intervention is not established in the shipped drivers; history labels that can represent a human edit do not constitute a driven approval route. Failed programs can remain the final logged product. ALFWorld and HotPotQA provide later model-input channels; WebShop's inspected action channel does not consume its plans. Detailed retained-memory revisions belong to the memory member; runtime records below establish the control and delivery paths without treating generated explanations as validated knowledge (SRC-1, `programming_runs/reflexion.py`, `alfworld_runs/generate_reflections.py`, `hotpotqa_runs/agents.py`, `webshop_runs/webshop_trial.py`).

Added inspection beyond the boundary's initial coverage: complete programming ordinary/simple/immediate/UCS/test-accuracy drivers, generator factory/model/Python generator/shared generation utilities, Python/Rust/LeetCode executor wrappers and timeout helpers; complete HotPotQA alternate agent/environment, prompt/adaptor/util modules and all notebook code cells; ALFWorld and WebShop history/provider helpers and full trial/reflection drivers. These remain SRC-1 implementation; README is attributed doctrine/design. The Rust implementation-call boundary was additionally inspected in this correction, along with the Python caller and shared helper signature; it supplies implementation evidence of an argument mismatch, not execution evidence. Rust prompt details beyond that call, vendored HumanEval evaluator, standalone validation/evaluation scripts, dataset utilities and retained result contents were not traced here. They prevent a complete account of offline result auditing and every language-specific prompt. The bounded programming progression reported here is Python-scoped; independently callable Rust executor machinery remains in scope, but complete Rust generation-to-execution progression is not wired. Missing dependency internals retain the boundary's limits on UCS search and remote LeetCode grading. Live provider, retrieval, environment and HTTP-server operation remains unobserved.

## Shared records

### Components

#### RT-CMP-gpt4
Label: GPT-4 generation endpoint

Source-native identity: `gpt-4`, selected in programming factory and ALFWorld CLI. Form: distributed-parametric model behind provider API; storage substrate: inaccessible provider weights. Parameters changing during operation: uninspected provider internals; inspected clients perform generation, not training. Exact version: not pinned beyond alias. Mutable endpoint may resolve to another model: unresolved provider contract; alias does not establish immutable weights. SRC-1, `programming_runs/generators/model.py`, `programming_runs/generators/factory.py`, `alfworld_runs/utils.py`.

> super().__init__("gpt-4")
> --- `programming_runs/generators/model.py`

#### RT-CMP-gpt35
Label: GPT-3.5 Turbo generation endpoint

Source-native identity: `gpt-3.5-turbo`, used by programming and HotPotQA defaults and afforded by ALFWorld. Form: distributed-parametric; storage: provider-side weights. Parameter change during operation: uninspected provider internals, no client training in inspected paths. Exact version: unpinned alias. Mutable endpoint substitution: uninspected; not excluded by alias. SRC-1, `programming_runs/generators/model.py`, `hotpotqa_runs/agents.py`, `hotpotqa_runs/llm.py`, `alfworld_runs/utils.py`.

> super().__init__("gpt-3.5-turbo")
> --- `programming_runs/generators/model.py`

#### RT-CMP-text-davinci
Label: Davinci completion endpoints

Source-native identities: `text-davinci-003` for ALFWorld/WebShop reflection and alternate HotPotQA; `text-davinci-002` for WebShop actions; programming accepts `text-davinci`-prefixed names. These are separately named endpoints within the same adapter family, not asserted identical models. Form: distributed-parametric; storage: provider weights. Parameter change: uninspected provider internals, generation-only inspected clients. Exact versions: aliases rather than immutable snapshots. Endpoint substitution: unresolved provider contract. SRC-1, `alfworld_runs/utils.py`, `webshop_runs/utils.py`, `webshop_runs/webshop_trial.py`, `hotpotqa_runs/react.py`, `programming_runs/generators/factory.py`.

> model="text-davinci-002",
> --- `webshop_runs/webshop_trial.py`

> model='text-davinci-003',
> --- `webshop_runs/utils.py`

#### RT-CMP-star-chat
Label: StarChat local generation model

Source-native identity: `StarChat`, `HuggingFaceH4/starchat-beta`. Form: distributed-parametric weights; storage: Hugging Face acquired local tensors, with tokenizer as symbolic preprocessing. Parameter change: inspected route invokes `.generate`, not training or optimizer updates; library internals uninspected. Exact version: no model revision argument. Mutable loading identity can resolve to different repository contents on later acquisition; already-loaded tensors do not thereby change. SRC-1, `programming_runs/generators/model.py`.

> model = AutoModelForCausalLM.from_pretrained(
>     "HuggingFaceH4/starchat-beta",
>     torch_dtype=torch.bfloat16,
>     device_map="auto",
> )
> --- `programming_runs/generators/model.py`

#### RT-CMP-code-llama
Label: CodeLlama local generation models

Source-native identity: `CodeLlama`, selectable 34b/13b/7b variants loaded as `codellama/CodeLlama-{version}-Instruct-hf`. Each selected variant has distributed-parametric tensors; substrate: acquired local model weights. Parameter change: generation only in inspected adapter, external library internals uninspected. Exact version: no revision pin for any variant. Mutable loading identity may resolve to other weights on later acquisition, not evidence of live tensor mutation. SRC-1, `programming_runs/generators/model.py`, `programming_runs/generators/factory.py`.

> model = AutoModelForCausalLM.from_pretrained(
>     f"codellama/CodeLlama-{version}-Instruct-hf",
>     torch_dtype=torch.bfloat16,
>     device_map="auto",
> )
> --- `programming_runs/generators/model.py`

### Operative objects

#### RT-OBJ-cur-func-impl
Label: Current generated implementation

Source-native identity: `cur_func_impl`. Form: symbolic Python/Rust source when executed; text when supplied back to a model. Substrate: process string, later task JSONL field `solution`. The same candidate crosses two consumers with different force: semantic guidance at the generator and executable effects at the executor. Its final persistence does not require reference success. SRC-1, `programming_runs/reflexion.py`, `programming_runs/generators/generator_utils.py`.

> item["solution"] = cur_func_impl
> write_jsonl(log_path, [item], append=True)
> --- `programming_runs/reflexion.py`

### Routes

#### RT-RTE-program-attempt
Label: Ordinary program attempt and successor selection

Operator CLI → task driver → Python generator/model → local or LeetCode executor → host branch → successor or JSONL. The implemented driver also selects Rust, but its Rust generator call fails before implementation generation; the complete progression described here is Python-scoped. Owner: `run_reflexion`. State: current candidate, fixed internal tests for a pass, textual feedback, reflection list, counters. Model proposes program and diagnosis; software decides execution and successor scheduling. Operator chooses bounded benchmark and budgets, but has no per-candidate veto in this loop. Answer oracle: generated assertions are provisional model-authored expectations; dataset `test` is the reference supplied by the benchmark; LeetCode uses visible tests then remote evaluator semantics unavailable here. A reference rejection sets failure, not necessarily another retry.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Driver returns `None`; each generation yields text, execution yields outcome and feedback, final item is appended to JSONL.
- Later read-back: Previous candidate, current feedback and latest reflection reach the next generation in the same task; result-file resume counts rows, not restored reflection contents.
- Delegated visibility: Provider receives assembled textual/code messages; local executor receives program plus selected tests; no separate agent delegation in this route.
- Selection predicate: Unprocessed dataset row; internal failure enters diagnosis, while internal success or final iteration triggers reference evaluation.
- Invalidation or expiry: Latest candidate/feedback replace current values; internal tests are regenerated on a new pass; item-local state resets for a new problem.
- Activation or effect: In the Python path, parsed candidate is executed and test booleans control branches; model behavioral dependence on delivered reflection is unobserved. Rust implementation generation is blocked before a candidate can reach execution through this route.
- Evidence limits: The wired implementation status covers Python driver/helper progression, conditional on external dependencies, not Rust generation-to-execution. Rust's missing required helper argument is an inspected parent-code defect independent of the unavailable UCS/LeetCode dependencies. Code trace only; model compliance, valid tests, successful dependency import and causal improvement unobserved.

Admission: model proposes replacement; host installs it as current candidate before tests. It can reject the correctness label but does not prevent execution of a bad candidate. Previous candidates are logged, not automatically restored. Static language-writing instructions, examples and feedback shape proposals. Persisted program is an external task product; retained hints can shape the next model call without modifying weights or scheduler. SRC-1, `programming_runs/reflexion.py`, `programming_runs/generators/generator_utils.py`, `programming_runs/generators/py_generate.py`, `programming_runs/utils.py`.

> # apply self-reflection in the next attempt
> cur_func_impl = gen.func_impl(
>     func_sig=item["prompt"],
>     model=model,
>     strategy="reflexion",
>     prev_func_impl=cur_func_impl,
>     feedback=cur_feedback,
>     self_reflection=reflection,
> )
> --- `programming_runs/reflexion.py`

> if is_passing:
>     is_passing = exe.evaluate(
>         item["entry_point"], cur_func_impl, item["test"], timeout=10)
>     is_solved = is_passing
>     num_success += int(is_passing)
>     break
> --- `programming_runs/reflexion.py`

Rust forcing case (SRC-1, `programming_runs/generators/rs_generate.py`, `programming_runs/generators/generator_utils.py`, `programming_runs/generators/py_generate.py`): `RsGenerator.func_impl` omits required `code_block_instruction`, with no helper default. Python supplies it. Python argument binding therefore raises `TypeError` on the Rust call before the helper can generate an implementation. This is source-established failure, not an observed run. It blocks initial and successor Rust implementation calls; missing dependencies returning would not fix it. Independent Rust executor/auditor code and visible UCS callbacks are not invalidated by this generation defect.

> reflexion_few_shot=RS_REFLEXION_FEW_SHOT_ADD,
> parse_code_block=lambda x: parse_code_block(x, "rust"),
> add_code_block=lambda x: add_code_block(x, "rust"),
> )
> --- `programming_runs/generators/rs_generate.py`

> code_block_instruction: str,
> --- `programming_runs/generators/generator_utils.py`

> code_block_instruction=USE_PYTHON_CODEBLOCK_INSTRUCTION,
> --- `programming_runs/generators/py_generate.py`

Theory account: in the Python progression, the model is asked for a localized explanation of why an implementation failed and a hint for revision; actual generated explanations were not inspected. The following delivery and reflection-wiring assessments cover Python, not a completed Rust attempt. Shipped examples demonstrate the requested genre, not exercised criticism. What persists is candidate code, reflection text and feedback, not an independently validated theory. Theory-builder conditions 1–4: (1) claimed for generated localized explanation; actual content uninspected; (2) afforded through the next-generation prompt, semantic dependence uninspected; (3) claimed by the diagnostic instruction, exercised blame placement uninspected; (4) wired as iterative delivery, content-directed iteration uninspected. Addressability: whole hints can be inspected/replaced, no inspected proposition-level editor. Persistence horizon: rounds on one task; JSONL retention does not establish later cross-problem use. Learning: improved future capacity and attribution uninspected. Reflection: trace→diagnosis→later input is wired, both directions of exercised behavioral causation uninspected. Autonomous theory builder: computational scheduling and proposals wired, theory conditions unresolved; no autonomous-builder conclusion. Reflective theory builder: method-text criticism not established by this candidate-program loop.

#### RT-RTE-code-execution
Label: Generated code execution and evaluation

Program/test strings → Python `exec` or Rust cargo harness → feedback/reference Boolean. Owner: executor wrapper. Form: symbolic code and assertions; errors become natural-language feedback. Python uses shared module globals in worker threads; Rust writes a temporary project, launches cargo through shell, parses compiler JSON and stderr, and removes temporary files. Capability grant follows host process authority, not a per-action permission policy. SRC-1, `programming_runs/executors/py_executor.py`, `programming_runs/executors/executor_utils.py`, `programming_runs/executors/rs_executor.py`, `programming_runs/executors/leet_executor.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ExecuteResult contains pass Boolean, text feedback and per-test tuple; reference evaluation returns Boolean or remote reward.
- Later read-back: Feedback reaches a later generator invocation through the calling strategy; execution globals may retain definitions but are not a planned reflection store.
- Delegated visibility: Generated source reaches Python host execution or cargo subprocess; LeetCode wrapper formats and submits source to external environment.
- Selection predicate: Caller-selected language, test list and `is_leetcode`; each local assertion is combined with the same candidate.
- Invalidation or expiry: Rust temporary directories are cleaned on handled paths; Python globals and live timeout threads are not rolled back by a failed test.
- Activation or effect: Generated code can cause host-process or subprocess effects; wrapper parses resulting errors to decide pass/fail.
- Evidence limits: This wired executor machinery can be called with supplied Python or Rust source; it does not establish a wired Rust generation-to-execution chain, which is blocked upstream as shown in [RT-RTE-program-attempt](#rt-rte-program-attempt). No deployment isolation supplied; provider/dependency/runtime behavior and actual process effects unobserved. Rust stderr parsing is not a general proof of successful exit.

Decision roles: model supplies candidates and sometimes tests; wrapper decides test outcome; benchmark supplies reference tests. Operating mode: caller-driven bounded evaluation. Rejection ability: exception/outcome may reject label after execution, not veto arbitrary effects. Rollback: no general effect rollback in inspected wrapper. Python failure reporting contains an additional execution path outside the thread timeout:

> exec(f"from typing import *\n{func}", globals())
> --- `programming_runs/executors/py_executor.py`

> thread = PropagatingThread(target=wrapper)
> thread.start()
> thread.join(timeout)
>
> if thread.is_alive():
>     raise TimeoutError()
> else:
>     return result_container[0]
> --- `programming_runs/executors/executor_utils.py`

The timeout rejects the caller's wait but does not kill the thread. This limits any termination or sandbox interpretation. Rust uses a different subprocess boundary:

> p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
>                      stderr=subprocess.PIPE, cwd=tmp_cargo_path)
> --- `programming_runs/executors/rs_executor.py`

LeetCode executes internal tests locally, while final evaluation enters the unavailable dependency. Its factory passes formatter classes, while the constructor asserts a formatter instance; compatibility is unresolved without the dependency (SRC-1, `programming_runs/executors/factory.py`, `programming_runs/executors/leet_executor.py`).

#### RT-RTE-program-variants
Label: Alternate programming strategies

CLI dispatch → selected strategy → Python model/executor → logged task. Owner: each strategy function; operating mode: bounded benchmark. The strategy bodies and UCS callbacks are implemented, but Rust implementation generation in these variants shares the missing-helper-argument defect established in [RT-RTE-program-attempt](#rt-rte-program-attempt). Complete generation progression below is Python-scoped, not a claim that selecting Rust wires a complete variant. Simple generates and reference-evaluates with no reflection. Immediate-reflexion repeatedly diagnoses without executed feedback and reference-evaluates only after the pass loop. Immediate-refinement executes tests but supplies a constant in place of reflection. UCS generates multiple successors, executes them, assigns failing-test costs, and delegates search to `ucs`. Test-accuracy intends to evaluate generated tests against canonical code but its `model` argument does not match CLI `model_name`, so the shipped dispatch is not established runnable. SRC-1, `programming_runs/main.py`, `programming_runs/simple.py`, `programming_runs/immediate_reflexion.py`, `programming_runs/immediate_refinement.py`, `programming_runs/reflexion_ucs.py`, `programming_runs/test_acc.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Strategies append result rows and return `None`; UCS callback returns successor states and numeric costs.
- Later read-back: Immediate variants pass latest code/hint/feedback within the task; UCS uses state-specific code, feedback and reflection; result-row counting skips completed items.
- Delegated visibility: UCS dependency receives State objects and callbacks; provider receives candidate context; executor receives source/tests.
- Selection predicate: CLI strategy; UCS goal is all internal tests passing, fallback is fewest failures, state identity encodes test-outcome bits.
- Invalidation or expiry: Task-local candidates replace current code; no content rollback protocol; external search eviction/termination uninspected.
- Activation or effect: Python calls and language-independent callback rules are implemented; missing dependency prevents full UCS progression account. Rust implementation-generation calls fail at helper argument binding, independently of search scheduling. Variants do not share the ordinary diagnostic evidence rule.
- Evidence limits: Wired status covers Python strategy bodies and visible UCS callbacks, not complete Rust variant generation or unavailable UCS search. None executed; test-accuracy argument mismatch and unconditional missing UCS import prevent treating CLI dispatch as demonstrated execution. Restoring dependencies alone cannot repair the Rust generator's required-argument omission.

Proposal/admission: computational candidate replacement; software test outcomes determine correctness labels, no per-candidate human veto. Answer oracles: benchmark reference tests, generated internal tests, or canonical solution for intended test-accuracy; immediate-reflexion has no feedback oracle during revision. No method or production-machinery edits occur in inspected strategy bodies. UCS can select `best.code` for evaluation but final `solution` is overwritten with `cur_func_impl`, so the logged artifact need not be the selected best candidate (SRC-1, `programming_runs/reflexion_ucs.py`).

> feedback = "Test cases omitted"
> --- `programming_runs/immediate_reflexion.py`

> self_reflection="No self-reflection"
> --- `programming_runs/immediate_refinement.py`

> best = ucs(
>     start=start,
>     expand=expand,
>     is_goal=lambda x: x.is_goal(),
>     # NOTE: this way we reduce our search space significantly
>     # the maximum number of nodes is 2^num_tests,
>     # which is 2^5 = 32
>     get_unique_id=lambda x: x.get_unique_id(),
>     when_none=when_none
> )
> --- `programming_runs/reflexion_ucs.py`

Theory account: immediate/UCS diagnosis requests share the explanation producer of [RT-RTE-program-attempt](#rt-rte-program-attempt); feedback omission changes warrant. The following iterative-delivery assessment covers Python immediate strategy bodies and visible UCS prompt construction only; Rust implementation generation cannot complete the initial/successor calls, so no complete Rust diagnosis-to-successor delivery loop is established. Theory-builder conditions 1–4: (1) claimed localized generated explanation, actual text uninspected; (2) afforded semantic use through model input; (3) uninspected content-directed criticism, with executed evidence omitted in immediate-reflexion; (4) wired iterative delivery in immediate strategy, external UCS iteration uninspected. Persistence: task rounds and result log. Addressability: whole text/candidate state; no demonstrated fine-grained theory editing. Learning and exercised reflection: uninspected; no benefit attributed. Autonomous/reflective theory-builder conclusions remain unestablished; these bodies do not establish criticism of their own method texts.

#### RT-RTE-alfworld-trial
Label: ALFWorld trial and plan admission

Operator → main trial driver → environment reset/task examples → action model → `env.step` → logs → reflection producer → next trial. Principal: local experiment process with provider credentials. Identity: config index paired to successive environment resets; resume reloads previous trial JSON by requested number. Owner: driver for trials, `alfworld_run` for steps. Operating mode: fixed out-of-distribution environment split and configured trial count. Model proposes actions and plans; host appends plan without correctness or human approval gate. Environment supplies observations/terminal signals, not a complete answer key. SRC-1, `alfworld_runs/main.py`, `alfworld_runs/alfworld_trial.py`, `alfworld_runs/generate_reflections.py`, `alfworld_runs/env_history.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Attempt returns history and success Boolean; driver writes trial/world logs and updated JSON configurations.
- Later read-back: Last three plans for the same indexed task enter the next action prompt; resumed configurations restore plans and success flags.
- Delegated visibility: Action provider gets examples, task, selected plans and current history; reflection provider gets extracted failed scenario and selected past plans.
- Selection predicate: Skip already-successful configs; update plans only when not successful and not `skip`; task prefix selects examples.
- Invalidation or expiry: Old plans remain in config but only tail three are delivered; attempt history resets each environment run; success suppresses later attempts.
- Activation or effect: Text action reaches environment; returned `done` sets success; admitted plans enter later model input but changed action choice remains unobserved.
- Evidence limits: Environment enumeration stability, `done` meaning and plan quality are external/unobserved; no target execution.

Recovery: explicit resume reads `resume_dir` but trial output paths use `run_name`; different values can separate input and output directories. Provider wrapper retries calls, but fatal action-call exception exits process; this is not transactional recovery. Rejection/rollback: config flags suppress plan admission, no semantic plan veto or automatic prior-plan restoration. Guidance asks for specific mistaken actions and a new plan; all admitted outputs append to task memory. Detailed store analysis belongs to memory.

> observation, reward, done = process_ob(observation[0]), info['won'][0], done[0]
> if action.startswith('think:'):
>     observation = 'OK.'
> --- `alfworld_runs/alfworld_trial.py`

> if done:
>     return env_history, True
> elif env_history.check_is_exhausted():
>     return env_history, False
> --- `alfworld_runs/alfworld_trial.py`

> reflection: str = get_completion(reflection_query) # type: ignore
> env_configs[i]['memory'] += [reflection]
> --- `alfworld_runs/generate_reflections.py`

Theory account: requested plan is a natural-language whole unit about prior failure, not guaranteed formulated explanation. Conditions 1–4: (1) claimed localized plan, actual generated content uninspected; (2) afforded through next-trial input, semantic dependence uninspected; (3) claimed mistake-directed diagnosis by prompt, actual criticism uninspected; (4) wired retention/delivery across trials, exercised content-directed iteration uninspected. Addressability: task-indexed whole plans. Persistence: trials and explicit resume on same tasks. Learning: improvement/attribution uninspected. Reflection: failure history can update representation, representation can reach action input; actual bidirectional behavioral dependence uninspected. Computational proposing/admission wired; autonomous theory-builder status unresolved. Method criticism is not established, so no reflective theory-builder attribution. Dispositional improvement-directed plan change is supported only for the delivered pathway; exercised self-improvement and successful improvement are unestablished.

#### RT-RTE-hotpotqa-attempt
Label: HotPotQA answer and reflection rounds

Notebook → dataset agents → thought/action calls → finish or retrieval → correctness check → subsequent reflection/reset → logs/joblib. Owner: notebook for five rounds; agent for steps; model proposes answer/diagnosis. Operating mode: bounded dataset questions, with dataset answer as oracle. CoT supporting-context mode additionally selects annotated supporting paragraphs. Software decides whether to retry/skip and admits diagnosis directly. Humans choose strategy, not each diagnosis. SRC-1, `hotpotqa_runs/agents.py`, `hotpotqa_runs/prompts.py`, `hotpotqa_runs/util.py`, the three notebooks under `hotpotqa_runs/notebooks/`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `run` updates agent state and returns `None`; notebook prints summaries, writes trial log and serializes agents.
- Later read-back: Reflection strings or last-attempt trace enter subsequent calls for the same question. Serialization alone supplies no inspected reload invocation.
- Delegated visibility: Action/diagnosis provider gets separately built prompts; Wikipedia explorer receives Search/Lookup arguments, not a delegated agent task.
- Selection predicate: Notebook retries agents not correct; CoT reflects after prior incorrect step unless NONE; ReAct reflects on finished/halted incorrect state. Strategy selects last trace, accumulated reflections or both.
- Invalidation or expiry: Reset discards current scratchpad; LAST_ATTEMPT replaces retained trace, REFLEXION accumulates texts, combined mode replaces reflection list with one latest reflection; no general semantic veto.
- Activation or effect: Finish sets answer and outcome text; retrieval appends observations; later model input includes retained strategy material, dependence unobserved.
- Evidence limits: Provider/retrieval behavior unobserved; normalized exact match is bounded by the supplied key; malformed action can raise before host error handling in main agents.

Working-context control: main ReAct halts when prompt exceeds 3896 encoded tokens or step limit. Reflection/last-attempt formatting reduces a copy to 1600 tokens by replacing largest Wikipedia observations, retaining thoughts/actions and placeholders; reset clears the attempt frame. This is selective deletion, not a semantic summary. If insufficient removable observations remain, its pop can fail. CoT reset clears scratchpad but no equivalent prompt-budget guard was traced. Alternate `react.py`/`environment.py` changes this: it trims longest lines regardless of type and delegates action dispatch to QAEnv; both implementations normalize answer and key. No model-native tool or remote-agent isolation is established (SRC-1, `hotpotqa_runs/agents.py`, `hotpotqa_runs/react.py`, `hotpotqa_runs/environment.py`).

> return normalize_answer(answer) == normalize_answer(key)
> --- `hotpotqa_runs/agents.py`

> return normalize_answer(answer) == normalize_answer(key)
> --- `hotpotqa_runs/environment.py`

> return self.agent_prompt.format(
>                             examples = self.cot_examples,
>                             reflections = self.reflections_str,
>                             context = self.context,
>                             question = self.question,
>                             scratchpad = self.scratchpad)
> --- `hotpotqa_runs/agents.py`

> lines[ind] = largest_observation.split(':')[0] + ': [truncated wikipedia excerpt]'
> --- `hotpotqa_runs/agents.py`

Theory account: prompts request possible failure diagnosis and a new high-level plan, including possible phrasing discrepancy. Actual outputs uninspected. Conditions 1–4: (1) claimed localized diagnosis/plan; (2) afforded semantic use via prompt header; (3) claimed content-directed diagnosis, exercised blame placement uninspected; (4) wired subsequent-round delivery, exercised theory iteration uninspected. Whole reflection addressability and same-question-round persistence are implemented; cross-question use is not established by `set_qa` alone. Learning benefit/attribution uninspected. Reflection's representational feedback channel is wired, exercised bidirectional effect uninspected. Computational proposal/scheduling does not establish autonomous theory building without the unresolved content properties; method-text criticism is unestablished. No exercised self-improvement claimed.

#### RT-RTE-webshop-trial
Label: WebShop trial and undelivered action plans

Operator → trial driver → session client → action model/HTTP pages → score/step stop → trial log → reflection model → config snapshot. Owner: host drivers and `webshopEnv`. Identity: `fixed_{z}` session per indexed configuration. Model proposes text commands; symbolic client branches assert permitted page transitions. HTML observations filter page content and expose at most three product-link texts, while retaining ASIN metadata. Full reward `1.0` determines success at terminal page; server supplies score, not inspected grading semantics. Operating mode: repeated fixed shopping tasks, configured trial count. SRC-1, `webshop_runs/main.py`, `webshop_runs/webshop_trial.py`, `webshop_runs/generate_reflections.py`, `webshop_runs/env_history.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Attempt returns history and Boolean; host writes trial/world logs and config JSON; action model returns next text command.
- Later read-back: Config plans are restored and passed into history; reflection queries consume recent plans. The separate action-model prompt does not consume those plans.
- Delegated visibility: Action provider receives static base prompt and bounded current observation/action text; reflection provider receives extracted failure scenario and past plans; HTTP server receives translated session/page requests.
- Selection predicate: Skip successful config; failure admits one new reflection; last three plans enter history/reflection context but not action context.
- Invalidation or expiry: Attempt prompt rebuilt from empty string, then character-tail sliced; history reset; snapshots retain accumulated plans; success stops future task trials.
- Activation or effect: Action changes client session/page state and issues HTTP GET; plans change log/reflection input, not the inspected action-model input.
- Evidence limits: Server correctness, HTTP availability and reflection-generation behavior unobserved; no action benefit attributed to stored plans.

Admission/recovery: failure-triggered generated plan appends without per-content approval or quality rejection; `--use_memory` controls update. Resume follows the same differing `resume_dir`/`run_name` input/output issue as ALFWorld. Invalid asserted transitions become `Invalid action!` in the step loop; other errors are not covered by that handler. No transaction rollback for HTTP effects. Model short-output retry has six attempts; provider exception exits process. Context control keeps base prompt and a character-budget suffix of current interaction, not tokenizer-bounded history or semantic summary.

> init_prompt = base_prompt
> prompt = ''
> --- `webshop_runs/webshop_trial.py`

> action = llm(init_prompt + prompt[-(6400-len(init_prompt)):], stop=['\n']).lstrip(' ')
> --- `webshop_runs/webshop_trial.py`

> if res[2]:
>     print(res)
>     return env_history, res[1] == 1.0
> --- `webshop_runs/webshop_trial.py`

Theory account: requested failure-derived plans remain whole natural-language units. Conditions 1–4: (1) claimed localized generated plan, text uninspected; (2) afforded consumption by subsequent reflection model, absent delivery to action model in this inspected function; (3) claimed diagnosis, actual criticism uninspected; (4) wired reflection-to-reflection delivery, not action-guidance iteration. Addressability: whole indexed plans; persistence: task trials/resume. Learning and exercised reflection benefit uninspected. The representation updates from traces, but action-side causal direction through retained plans is not established here. Autonomous/reflective theory-builder conclusions unresolved; action-oriented self-improvement through plan delivery is not supported by this wiring.

### Claims

#### RT-CLM-persisting-memory
Label: Persisting self-reflection intent

Claimed operation: ALFWorld run parameters permit persisting memory to store self-reflections, disabled for baseline. Source is author documentation, not measured operation. The runtime supports that path in ALFWorld; it does not extend it to WebShop's distinct action-input implementation. SRC-1, `README.md`.

> `use_memory`: use persisting memory to store self-reflections (turn off to run a baseline run)
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-plan-guidance
Label: Retained plan as model guidance

Consumer: ALFWorld action model and HotPotQA action/reasoning model. Channel: selected plan/reflection text inside rebuilt input. Force: natural-language recommendation interpreted by model, not executable permission or guaranteed compliance. Horizon: later attempts on same task, with ALFWorld resume afforded. WebShop's inspected action caller is not covered. SRC-1, `alfworld_runs/env_history.py`, `hotpotqa_runs/prompts.py`, `webshop_runs/webshop_trial.py`; routes [RT-RTE-alfworld-trial](#rt-rte-alfworld-trial), [RT-RTE-hotpotqa-attempt](#rt-rte-hotpotqa-attempt), [RT-RTE-webshop-trial](#rt-rte-webshop-trial).

> query += '\n\nYour memory for the task below:'
> for i, m in enumerate(memory):
>     query += f'\nTrial {i}:\n{m.strip()}'
> --- `alfworld_runs/env_history.py`

#### RT-BAP-executable-code
Label: Generated code as host-executed instructions

Consumer: Python interpreter or Rust compilation/execution facilities. Channel: assembled program/test strings or temporary source file. Force: executable instructions under host authority; test gating occurs after candidate execution. Horizon: current evaluation; effects can outlast a rejected label or timeout. Retained `solution` does not itself establish future execution. SRC-1, `programming_runs/executors/py_executor.py`, `programming_runs/executors/rs_executor.py`; [RT-RTE-code-execution](#rt-rte-code-execution).

> function_with_timeout(exec, (func_test_list[i], globals()), timeout)
> --- `programming_runs/executors/py_executor.py`

## Annotations

none
