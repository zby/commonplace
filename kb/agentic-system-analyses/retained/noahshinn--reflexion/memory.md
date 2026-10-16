---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Reflexion's task-indexed plans, prior-attempt traces, program hints and checkpoint consumers across four shipped experiment families."
run-id: AAS-2026-10-14-reflexion-19159b69b712-01
source-identity: "https://github.com/noahshinn/reflexion"
reviewed-boundary: "218cf0ef1df84b05ce379dd4a8e47f17766733a0"
---

# Reflexion memory report

## Boundary and evidence

The memory boundary includes the four experiment families in [boundary](boundary.md): ALFWorld and WebShop configuration plans and resume; HotPotQA prior-attempt retention, reflection, formatting and serialization; programming candidate/feedback/hint retention, alternate strategies, result resume and offline result consumers. Static examples and current-attempt windows are included as context-control surfaces, not automatically classified as read-back. The source is SRC-1 at the frozen commit. The account distinguishes directly inspected implementation below from supplied runtime findings. No target code, provider, environment, tests or examples were executed.

Provider-side state is opaque; its model components and fixity limits are supplied in [RT-CMP-gpt4](runtime.md#rt-cmp-gpt4), [RT-CMP-gpt35](runtime.md#rt-cmp-gpt35), [RT-CMP-text-davinci](runtime.md#rt-cmp-text-davinci), [RT-CMP-star-chat](runtime.md#rt-cmp-star-chat) and [RT-CMP-code-llama](runtime.md#rt-cmp-code-llama). This report does not infer either training or absence of all provider-side memory. Git-linked UCS search and LeetCode grading/formatting internals are unavailable as stated in boundary; parent callbacks and consumers remain included. Live Wikipedia, environment and server contents are outside frozen evidence. Their correctness and behavioral effects cannot be established here.

| Entry point or operation | SRC-1 paths and inspection basis | Covering records or local limit |
|---|---|---|
| Programming CLI dispatch and ordinary attempt | Direct: `programming_runs/main.py`, `programming_runs/reflexion.py`, `programming_runs/utils.py`, `programming_runs/generators/generator_utils.py` | [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt), [MEM-OBJ-reflections](#mem-obj-reflections), [MEM-OBJ-test-feedback](#mem-obj-test-feedback), [MEM-OBJ-program-results](#mem-obj-program-results). Six dispatch branches checked; unconditional UCS import remains a launch limit. |
| Simple, immediate-reflexion, immediate-refinement, test-accuracy | Supplied runtime plus bounded direct searches: `programming_runs/simple.py`, `programming_runs/immediate_reflexion.py`, `programming_runs/immediate_refinement.py`, `programming_runs/test_acc.py` | [RT-RTE-program-variants](runtime.md#rt-rte-program-variants). Different hint/feedback rules are retained in annotations. Test-accuracy dispatch mismatch limits runnable-path claims. |
| UCS state expansion, selection and final logging | Direct: `programming_runs/reflexion_ucs.py` | [MEM-OBJ-state](#mem-obj-state), [RT-RTE-program-variants](runtime.md#rt-rte-program-variants). Missing `lazzzy` internals prevent eviction, search horizon and selected-state persistence conclusions. |
| Local execution, cleanup and feedback generation | Supplied runtime: `programming_runs/executors/py_executor.py`, `programming_runs/executors/rs_executor.py`, `programming_runs/executors/executor_utils.py` | [RT-RTE-code-execution](runtime.md#rt-rte-code-execution); rejection does not roll back Python globals or kill timeout threads. Rust temporary-file cleanup is not memory curation. |
| Python/Rust offline result checks | Direct: `programming_runs/validate_py_results.py`, `programming_runs/validate_rs_results.py` | [MEM-RTE-result-validation](#mem-rte-result-validation); separate persisted-program consumer, not an agent-reflection route. |
| LeetCode offline evaluation | Direct: `programming_runs/evaluate_leet_results.py`, `programming_runs/evaluate_rs_leet_results.py` | [MEM-RTE-leet-evaluation](#mem-rte-leet-evaluation); latter file is empty. Argument assertion, implementation/task-ID mismatch and missing dependency prevent an end-to-end evaluated output claim. |
| ALFWorld initialize, reload, update, task window and logs | Direct: `alfworld_runs/main.py`, `alfworld_runs/alfworld_trial.py`, `alfworld_runs/generate_reflections.py`, `alfworld_runs/env_history.py` | [MEM-OBJ-alfworld-memory](#mem-obj-alfworld-memory), [MEM-OBJ-alfworld-logs](#mem-obj-alfworld-logs), [RT-RTE-alfworld-trial](runtime.md#rt-rte-alfworld-trial). Stable environment enumeration is an external requirement. |
| WebShop initialize, reload, reflection, logger and action window | Direct: `webshop_runs/generate_reflections.py`, `webshop_runs/webshop_trial.py`; supplied runtime and bounded search: `webshop_runs/main.py`, `webshop_runs/env_history.py` | [MEM-OBJ-webshop-memory](#mem-obj-webshop-memory), [MEM-OBJ-webshop-logs](#mem-obj-webshop-logs), [RT-RTE-webshop-trial](runtime.md#rt-rte-webshop-trial). Log consumption differs from action consumption. |
| HotPotQA CoT/ReAct, three notebooks and checkpoint | Direct: `hotpotqa_runs/agents.py`, `hotpotqa_runs/util.py`; supplied runtime plus bounded notebook search: `hotpotqa_runs/notebooks/CotQA_context.ipynb`, `hotpotqa_runs/notebooks/CotQA_no_context.ipynb`, `hotpotqa_runs/notebooks/ReactQA.ipynb` | [MEM-OBJ-hotpotqa-reflections](#mem-obj-hotpotqa-reflections), [MEM-OBJ-last-attempt](#mem-obj-last-attempt), [MEM-OBJ-hotpotqa-checkpoints](#mem-obj-hotpotqa-checkpoints), [RT-RTE-hotpotqa-attempt](runtime.md#rt-rte-hotpotqa-attempt). Notebook loads found by search load dataset, not saved agents. |
| Alternate HotPotQA agent and QAEnv | Direct: `hotpotqa_runs/react.py`; supplied runtime: `hotpotqa_runs/environment.py` | [RT-RTE-hotpotqa-attempt](runtime.md#rt-rte-hotpotqa-attempt). Alternate line trimming has different deletion rules. |
| Language prompt and static-example context | Direct generic generator; bounded search `programming_runs/generators/rs_generate.py`; supplied runtime `programming_runs/generators/py_generate.py`, `hotpotqa_runs/prompts.py`; direct ALFWorld reflection instruction | No acquired examples are asserted to be learned memory. Full static-example contents were not audited; this prevents an account of every pedagogical assertion, not the established retention selectors. |
| Saved result corpora, datasets and vendored evaluator | Available but not inspected as run evidence: task-family result directories, benchmark data, `programming_runs/human-eval/` | No observed activation, performance or causal-learning conclusion. Serialization payload contents and historical trial quality remain uninspected. Dataset preparation utilities are not traced as memory writers; initial dataset provenance is unresolved locally. |

The shipped dispatch and callable agent methods were checked against runtime routes; no provider-native registered memory tool or hook is presumed from those ordinary function calls. This is a bounded inspection, not an exhaustive repository-wide absence claim.

## Core ideas

Retention is principally **same-task retry input**, not a shared retrieval library. ALFWorld selects plans by environment index and recency; HotPotQA retains state on each question's agent; programming supplies the latest candidate/feedback/hint or a UCS node. Persisting an entire list does not mean the consumer sees the list. See [MEM-OBJ-alfworld-memory](#mem-obj-alfworld-memory), [MEM-OBJ-hotpotqa-reflections](#mem-obj-hotpotqa-reflections), [MEM-OBJ-reflections](#mem-obj-reflections) and [MEM-OBJ-state](#mem-obj-state).

WebShop is the important counterexample: retained plans reach subsequent reflection calls and logger histories, but the action-model input is separately assembled without them. The action window instead slices a character tail. This supports a reflection-to-reflection route, not action guidance through stored plans; see [RT-RTE-webshop-trial](runtime.md#rt-rte-webshop-trial) and [MEM-OBJ-webshop-memory](#mem-obj-webshop-memory).

A second distinction is **raw evidence versus derived instructions**. HotPotQA can preserve a reduced prior attempt without generating a diagnosis; its truncator deletes observations rather than summarizing meaning. ALFWorld and WebShop instead ask a model for a new plan after failure; programming asks for a localized failure explanation. Software admits these outputs without verifying their reasoning. Environment outcomes, dataset keys and test results gate scheduling/correctness, not the truth of admitted diagnoses. See the supplied theory accounts in [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt), [RT-RTE-alfworld-trial](runtime.md#rt-rte-alfworld-trial), [RT-RTE-hotpotqa-attempt](runtime.md#rt-rte-hotpotqa-attempt) and [RT-RTE-webshop-trial](runtime.md#rt-rte-webshop-trial).

Checkpoint consumers have different authority. Configuration JSON restores plans **and success flags**, which suppress later trials. Programming resume only counts rows, while offline validators execute saved programs. Joblib agent serialization is a retention capability without an inspected saved-agent reload caller. These are not interchangeable durable-memory guarantees; see [MEM-OBJ-program-results](#mem-obj-program-results), [MEM-OBJ-hotpotqa-checkpoints](#mem-obj-hotpotqa-checkpoints) and [MEM-RTE-result-validation](#mem-rte-result-validation).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-alfworld-memory
Label: ALFWorld task plan list

Part of: [RT-RTE-alfworld-trial](runtime.md#rt-rte-alfworld-trial)

This object is the retained-state part of that route, not another declaration of its progression. Source-native identity: `env_configs[i]['memory']`. Natural-language plan strings live in process lists and per-trial JSON configuration snapshots. New configurations start empty; explicit resume loads previous-trial JSON. Initial resumed content is caller-selected and not independently authenticated. Subsequent lineage is known: failed trial log scenario plus static examples plus up to three past plans → completion output → append. The task index selects the list, not semantic similarity. The last three plans reach action input and reflection input; the full list remains on disk. Content is advice interpreted by a model; JSON success/skip fields instead have fixed host branching rules. There is no semantic plan-quality gate in the inspected updater. Source: SRC-1, `alfworld_runs/main.py`, `alfworld_runs/generate_reflections.py`, `alfworld_runs/alfworld_trial.py`, `alfworld_runs/env_history.py`; closest supplied route above and guidance [RT-BAP-plan-guidance](runtime.md#rt-bap-plan-guidance).

> if not env['is_success'] and not env['skip']:
> --- `alfworld_runs/generate_reflections.py`

> env_configs[i]['memory'] += [reflection]
> --- `alfworld_runs/generate_reflections.py`

> if len(memory) > 3:
>     env_history = EnvironmentHistory(base_prompt, ob, memory[-3:], [])
> else:
>     env_history = EnvironmentHistory(base_prompt, ob, memory, [])
> --- `alfworld_runs/alfworld_trial.py`

#### MEM-OBJ-alfworld-logs
Label: ALFWorld trial evidence logs

Part of: [RT-RTE-alfworld-trial](runtime.md#rt-rte-alfworld-trial)

Source-native identities: `trial_log_path`, `world_log_path`. Files contain model actions, processed environment observations, rendered task context and host status/summary text. Encoding: natural-language trace plus symbolic delimiters and status fields. These are not just plans or access metadata: the updater splits the trial file by delimiters and uses each failed task's scenario. The reflection extractor removes the prefix before the last `Here is the task:`; in the normal rendered history this excludes old memory from the scenario, after which past plans are separately added. World logs are accounting output, not the updater's source. Raw here means uncondensed attempt trace, not an unmodified environment stream: `process_ob` strips location prefix and think observations become `OK.`. Source: SRC-1, `alfworld_runs/alfworld_trial.py`, `alfworld_runs/generate_reflections.py`. Distinct material input part of the supplied route, with a different consumer from its derived plan.

> return s.split("Here is the task:")[-1].strip()
> --- `alfworld_runs/generate_reflections.py`

> env_logs: List[str] = full_log.split('#####\n\n#####')
> --- `alfworld_runs/generate_reflections.py`

#### MEM-OBJ-webshop-memory
Label: WebShop task plan list

Part of: [RT-RTE-webshop-trial](runtime.md#rt-rte-webshop-trial)

Source-native identity: `env_configs[i]['memory']`. Natural-language strings in process lists and JSON snapshots. Empty initialization and explicit configuration resume follow the shipped driver described in the supplied route. Failure log, reflection examples and last three plans produce an appended completion. Its admission predicate checks `is_success`, unlike ALFWorld's additional `skip`. The reflection model is an actual later consumer. The history renderer also receives plans, but its display is not the action-model prompt. This is distinct from ALFWorld's list despite similar names and schema. SRC-1, `webshop_runs/main.py`, `webshop_runs/generate_reflections.py`, `webshop_runs/webshop_trial.py`; supplied route carries the decisive omitted-action-input quotation.

> if not env['is_success']:
> --- `webshop_runs/generate_reflections.py`

> reflection_query: str = _generate_reflection_query(env_logs[i], memory)
> reflection: str = get_completion(reflection_query) # type: ignore
> env_configs[i]['memory'] += [reflection]
> --- `webshop_runs/generate_reflections.py`

#### MEM-OBJ-webshop-logs
Label: WebShop trial evidence logs

Part of: [RT-RTE-webshop-trial](runtime.md#rt-rte-webshop-trial)

Source-native identities: `trial_log_path`, `world_log_path`. File text combines rendered base context, plans, actions, processed HTTP observations and host status. It is an evidence input to plan production, not proof that the action model received that same text. The extractor selects text after the last `Instruction:`. Assertion-failure cases can produce only `Assertion Error` plus failure status, so not every admitted plan has a full interaction trace. Delimiter/index alignment is asserted; semantic correspondence is not checked. Natural-language scenario is interpreted by the reflection model; delimiters are symbolic parser input. SRC-1, `webshop_runs/webshop_trial.py`, `webshop_runs/generate_reflections.py`. Distinct raw-input part from [MEM-OBJ-webshop-memory](#mem-obj-webshop-memory).

> return s.split("Instruction:")[-1].strip()
> --- `webshop_runs/generate_reflections.py`

> wf.write(f'\n#####\n\nEnvironment #{z}:\nAssertion Error\n\nSTATUS: FAIL\n\n#####\n')
> --- `webshop_runs/webshop_trial.py`

#### MEM-OBJ-hotpotqa-reflections
Label: HotPotQA derived reflection texts

Part of: [RT-RTE-hotpotqa-attempt](runtime.md#rt-rte-hotpotqa-attempt)

Source-native identities: `self.reflections`, `self.reflections_str` in derived-reflection modes. Natural-language output is stored as agent list/string and later inside joblib checkpoints. Lineage: question, prior scratchpad, reflection examples and CoT supporting context when provided → model diagnosis → newline-stripped text → formatted input. REFLEXION appends all diagnoses; combined mode replaces the list with one latest diagnosis and includes the prior attempt separately. The action/reasoning model receives the formatted result as advisory text. The main ReAct reflection producer receives a truncated current scratchpad, not the accumulated reflection list directly; accumulated reflections reach the next action prompt. CoT's reflection producer likewise uses current scratchpad/context. Actual behavioral reliance is unobserved. SRC-1, `hotpotqa_runs/agents.py`; closest supplied route above. The alternate implementation in `hotpotqa_runs/react.py` appends diagnoses and uses different trace deletion, as annotated below.

> elif strategy == ReflexionStrategy.REFLEXION:
>     self.reflections += [self.prompt_reflection()]
>     self.reflections_str = format_reflections(self.reflections)
> --- `hotpotqa_runs/agents.py:112-114`

#### MEM-OBJ-last-attempt
Label: HotPotQA retained prior attempt

Part of: [RT-RTE-hotpotqa-attempt](runtime.md#rt-rte-hotpotqa-attempt)

Source-native identities: `self.scratchpad`, `format_last_attempt`, the LAST_ATTEMPT value of `self.reflections`. This part is not the generated diagnosis above, even though the variable can hold either. Natural-language thought/action/observation trace lives in agent state; actions were separately parsed symbolically in the attempt. LAST_ATTEMPT replaces the list with the previous scratchpad and delivers a truncated formatted copy to the next action model. Combined mode keeps this copy in `reflections_str` alongside one new diagnosis. Raw scratchpad can remain in the list in LAST_ATTEMPT mode while the display omits long observations. The formatted display is a lossy excerpt, not a semantic summary. It preserves causal reasons only to the extent surviving thoughts/actions/observations express them; deleted excerpts are not recoverable through a model tool supplied here. SRC-1, `hotpotqa_runs/agents.py`. Distinct retained-input part of the supplied route, with a direct trace-read-back alternative to diagnosis.

> if strategy == ReflexionStrategy.LAST_ATTEMPT:
>     self.reflections = [self.scratchpad]
>     self.reflections_str = format_last_attempt(self.question , self.reflections[0])
> --- `hotpotqa_runs/agents.py`

> lines[ind] = largest_observation.split(':')[0] + ': [truncated wikipedia excerpt]'
> --- `hotpotqa_runs/agents.py`

#### MEM-OBJ-hotpotqa-checkpoints
Label: HotPotQA logs and serialized agents

Part of: [RT-RTE-hotpotqa-attempt](runtime.md#rt-rte-hotpotqa-attempt)

Source-native identities: `save_agents`, `log_trial`, `log_react_trial`. Joblib files serialize whole agent objects; their actual frozen payloads were not decoded. The implemented writer is known, but complete payload composition, library object internals and initial dataset provenance are unresolved. The readable trial logs are independently constructed summaries, not verified displays of every serialized field. They omit few-shot examples and append dataset correct answers, so they are not identical to model inputs and may contain answer keys not delivered to the agent. Logs are natural-language display plus summary fields; the joblib envelope is symbolic serialization with embedded text/state, not distributed-parametric memory merely because binary. Notebook searches found dataset loading and agent saving, not a saved-agent reload caller. Therefore serialization alone does not establish cross-run agent read-back. SRC-1, `hotpotqa_runs/util.py`, notebook paths in coverage; closest supplied route above.

> for i, agent in enumerate(agents):
>     joblib.dump(agent, os.path.join(dir, f'{i}.joblib'))
> --- `hotpotqa_runs/util.py`

> log += remove_fewshot(agent._build_agent_prompt()) + f'\nCorrect answer: {agent.key}\n\n'
> --- `hotpotqa_runs/util.py:26-26`

#### MEM-OBJ-reflections
Label: Programming task reflection hints

Part of: [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt)

Source-native identities: `reflection`, `reflections`, result field `reflections`. Natural-language explanations are strings and a task-local list later copied into JSONL. Lineage: current implementation plus executor feedback and language-specific static instruction/examples → model explanation. The next ordinary generator receives the latest explanation, not the entire accumulated list. Failure explanations and feedback are separate materials: the explanation asks why and how to revise; it is not the test outcome itself. No semantic correctness gate validates a hint before delivery. Failed or misleading hints can persist in the result file. SRC-1, `programming_runs/reflexion.py`, `programming_runs/generators/generator_utils.py`; supplied route provides the successor call quotation. Distinct hint part, not [RT-OBJ-cur-func-impl](runtime.md#rt-obj-cur-func-impl).

> reflections += [reflection]
> --- `programming_runs/reflexion.py`

> item["reflections"] = reflections
> --- `programming_runs/reflexion.py`

#### MEM-OBJ-test-feedback
Label: Programming retained test feedback

Part of: [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt)

Source-native identities: `cur_feedback`, `test_feedback`, `tests_i`. Executor outcome descriptions, errors and test displays become natural-language evidence at diagnosis and successor calls; assertion strings are symbolic at the executor. Storage: process values and the ordinary result's `test_feedback` list. Generated internal tests or supplied visible tests are reused during a pass; new passes can regenerate tests. The result records feedback but does not assign `tests_i` as its own field in the ordinary strategy, so persistence of the exact test suite cannot be inferred solely from that list. It may appear in feedback text, whose retained corpora were not inspected. Reference-test rejection is a Boolean correctness decision, not automatically a new detailed diagnosis input. SRC-1, `programming_runs/reflexion.py`; feedback-production details are supplied by [RT-RTE-code-execution](runtime.md#rt-rte-code-execution). Distinct evidence part from explanation and candidate.

> test_feedback.append(cur_feedback)
> --- `programming_runs/reflexion.py`

#### MEM-OBJ-program-results
Label: Programming task result rows

Part of: [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt)

Source-native identity: `item` appended to `log_path`. JSONL container includes task fields, `solution`, `is_solved`, reflections, implementations and test feedback in ordinary Reflexion. Embedded hints/feedback are natural language; code/tests become symbolic only at execution consumers; JSON keys and correctness flags have fixed host rules. The existing current candidate remains [RT-OBJ-cur-func-impl](runtime.md#rt-obj-cur-func-impl), not a new declaration here. The container adds archived candidates and accounting fields with distinct consumers. Final writing does not require `is_solved`; later resume counts every row and suppresses that dataset prefix regardless of success. Offline validators instead select solved rows and execute their persisted solution. Neither route reloads reflection content into a new problem's model context. SRC-1, `programming_runs/reflexion.py`, `programming_runs/utils.py`, validator paths in [MEM-RTE-result-validation](#mem-rte-result-validation).

> item["implementations"] = implementations
> item["test_feedback"] = test_feedback
> item["solution"] = cur_func_impl
> write_jsonl(log_path, [item], append=True)
> --- `programming_runs/reflexion.py`

> if i < count:
>     continue
> yield i, item
> --- `programming_runs/utils.py`

#### MEM-OBJ-state
Label: Programming UCS candidate state

Part of: [RT-RTE-program-variants](runtime.md#rt-rte-program-variants)

Source-native identity: `State(code, feedback, reflection, state)`. In-memory Python object holds code, natural-language feedback/reflection and symbolic Boolean test tuple. Each node supplies its own candidate/hint/feedback to expansion, unlike ordinary latest-value replacement. Outcome-bit identity is handed to the search dependency; this can equate candidates with different source or explanations. Search merging/eviction behavior is uninspected because the dependency is missing. Parent code logs accumulated reflections and a final `solution`, but does not serialize complete node graph or selected-node lineage. `best.code` can be evaluated then overwritten in the output by the original `cur_func_impl`. Therefore a solved label is not sufficient evidence that the persisted program was the selected passing node. SRC-1, `programming_runs/reflexion_ucs.py`; distinct state part of the supplied variants route, whose quotation establishes the external search call.

> res += self.state[i] * (2**i)
> --- `programming_runs/reflexion_ucs.py`

> item["is_solved"] = is_solved
> item["reflections"] = reflections
> item["solution"] = cur_func_impl
> write_jsonl(log_path, [item], append=True)
> --- `programming_runs/reflexion_ucs.py`

### Routes

#### MEM-RTE-result-validation
Label: Persisted program result validation

Distinct later file-to-executor route, with no identical supplied record. It extends the retained-product horizon of [RT-OBJ-cur-func-impl](runtime.md#rt-obj-cur-func-impl) and uses execution facilities related to [RT-RTE-code-execution](runtime.md#rt-rte-code-execution), but is not the attempt driver's evaluation call. Operator invokes standalone Python/Rust validator with result file; validator reads rows, selects `is_solved`, reconstructs Python test code or invokes `RsExecutor.evaluate`, and prints rechecked success counts. Owner: validation script. State/effects: result rows and host execution; no persisted correction or rollback of source rows. Source: SRC-1, `programming_runs/validate_py_results.py`, `programming_runs/validate_rs_results.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Printed per-row pass/fail and aggregate accuracy; no revised result file.
- Later read-back: Saved solution and reference tests reach execution on a later standalone invocation; saved hints do not reach a model.
- Delegated visibility: Python receives reconstructed source/tests; Rust executor receives solution and reference test strings.
- Selection predicate: Operator-selected file; each row's `is_solved` gates actual re-execution, while unsolved rows print failure.
- Invalidation or expiry: Recheck failures alter printed totals, not original `is_solved` or archived code; no automatic retry or withdrawal of rows.
- Activation or effect: Saved code is executed under host authority; actual validation runs and resulting effects were not observed.
- Evidence limits: Input compatibility, isolation and evaluator correctness remain external or untested; printed failure does not establish durable correction.

Admission/comparison: software, not a human per-row decision, selects and judges against the row's reference tests. Human supplies the file and launches the bounded audit. Oracle: persisted benchmark tests, not independent verification of their validity. No proposal of a new program, hint or scheduler change occurs; this is evaluation of retained product, not theory revision.

> if item["is_solved"]:
>     func_impl = item["solution"]
>     code = f'{item["prompt"]}{func_impl}\n\n{item["test"]}\n\ncheck({item["entry_point"]})'
> --- `programming_runs/validate_py_results.py`

> res = rs_executor.evaluate(item["entry_point"], func_impl, item["test"])
> --- `programming_runs/validate_rs_results.py`

#### MEM-RTE-leet-evaluation
Label: Intended retained implementation submission

Distinct offline consumer scaffold, related to [RT-RTE-code-execution](runtime.md#rt-rte-code-execution) but not the shipped attempt call. The evaluator intends to read a result file's `implementations`, format each candidate and submit it, accumulating `evaluations` in memory. Owner: evaluation script; external grader dependencies are unavailable. SRC-1, `programming_runs/evaluate_leet_results.py`; `programming_runs/evaluate_rs_leet_results.py` is empty and supplies no alternate implementation.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Intended in-memory evaluation list; no output-file write implemented in the inspected script.
- Later read-back: Intended saved implementation-list read and external submission, but complete executable delivery is not established.
- Delegated visibility: Intended formatter and LeetCode environment receive candidate code and task identity; dependency internals uninspected.
- Selection predicate: CLI input file and each `implementations` element, rather than only `is_solved` rows.
- Invalidation or expiry: `evaluations` is initialized empty per row; `env.reset()` follows each submission; no source-result withdrawal or durable corrected file.
- Activation or effect: External grading request is the intended effect; argument and record-shape defects prevent treating it as a wired end-to-end consumer.
- Evidence limits: Script asserts three argv elements but accesses element three; ordinary implementation entries are strings yet task identity is indexed on each entry; missing dependencies prevent grading/formatting verification.

Human supplies launch arguments; software iterates and external environment would decide outcome. Oracle is external LeetCode grading, whose implementation is not present. This does not validate admitted reflection content. No candidate improvement/rollback loop is supplied.

> assert len(sys.argv) == 3, "Provide a language [py, rs], input and output log file"
> --- `programming_runs/evaluate_leet_results.py`

> output_log_path = sys.argv[3]
> --- `programming_runs/evaluate_leet_results.py`

> question_slug=impl["task_id"],
> --- `programming_runs/evaluate_leet_results.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-program-attempt](runtime.md#rt-rte-program-attempt)

Memory selection is an automatic retry push: internal failure triggers diagnosis; current implementation and current feedback determine the producer input; the successor receives those values and **one latest** reflection. Earlier list entries persist for logging, not complete-history delivery. Generic chat generation inserts the previous code and reflection as assistant messages, with feedback as user text; completion generation labels the explanation a hint. This formatting grants interpretive influence, not verified truth or enforced compliance. No generic token-aware trimming occurs in the inspected assembly. Each new task isolates local arrays; new pass generates another initial candidate without rebuilding a prompt from old list entries. SRC-1, `programming_runs/reflexion.py`, `programming_runs/generators/generator_utils.py`.

> content=self_reflection,
> --- `programming_runs/generators/generator_utils.py`

The explanation's requested rationale is retained verbatim as generated text, alongside feedback and archived implementations in ordinary JSONL. Later generator receives rationale plus evidence in the same task. Actual rationale quality and content-dependent revision remain uninspected, consistent with the supplied independent theory-builder, learning and reflection limits.

#### On [RT-RTE-program-variants](runtime.md#rt-rte-program-variants)

Immediate-reflexion pushes the latest explanation but supplies constant `Test cases omitted`; its derivation is candidate-fed, not executed-test-trace-fed during revision. Immediate-refinement pushes latest feedback and code with constant `No self-reflection`; its result's reflection list is not evidence of a produced explanation. Simple has no hint revision; intended test-accuracy produces test assertions rather than a reflection store. These alternatives are supplied runtime findings corroborated by bounded searches at SRC-1, `programming_runs/immediate_reflexion.py`, `programming_runs/immediate_refinement.py`, `programming_runs/simple.py`, `programming_runs/test_acc.py`. UCS is state-targeted selection and delivery, with its missing search semantics kept local in [MEM-OBJ-state](#mem-obj-state). No cross-problem learned-memory consumer is inferred from result files.

#### On [RT-RTE-alfworld-trial](runtime.md#rt-rte-alfworld-trial)

Read-back is driver-triggered push on retry and explicit reload on resume. Code selects the indexed task list and last three entries; there is no query-driven relevance ranking or token budget for plans. Static task-prefix examples and a fresh attempt history form the working context; only plans cross attempts. Constructor stores the plan-rendered base query; `reset` clears history, not that base. The reflection producer separately receives scenario plus last three plans. This preserves some generated reasons if present, but does not retain provenance links from each plan to a checked mistake. Model proposals are admitted automatically under failure/skip gates; `human_edit` is a renderer label marked unsupported, not a driven human approval path. JSON success flags suppress future action and update routes; skipping is not content withdrawal. SRC-1, `alfworld_runs/env_history.py`, `alfworld_runs/alfworld_trial.py`, `alfworld_runs/generate_reflections.py`, `alfworld_runs/main.py`.

> def reset(self) -> None:
>     self._history = []
> --- `alfworld_runs/env_history.py`

Resume restores both hints and accounting state from previous-trial JSON. A caller supplying/editing that file could change content, but the driver provides no inspected per-plan edit/adoption workflow; initial human control of resumed payload is unresolved. Output trial paths use `run_name` while input uses `resume_dir`; persistence requires those destinations to be usable and intended. No general transaction recovery is established.

#### On [RT-RTE-hotpotqa-attempt](runtime.md#rt-rte-hotpotqa-attempt)

Per-question agent state isolates different tasks in the notebooks. Retry automatically pushes a formatted last trace, accumulated diagnoses, or latest trace plus latest diagnosis according to strategy. There is no agent request to search a shared store. Main ReAct truncation preferentially deletes largest observation lines from a **copy** until 1600 tokens; thoughts/actions remain, and removed evidence has placeholders. Selection is by line size/type, not relevance or truth. That reduced copy reaches both reflection generation and formatted last-attempt delivery. Agent-window 3896-token checks halt rather than semantically compacting the active attempt. Accumulated reflections themselves are not capped by the 1600-token trace helper. CoT uses the same last-attempt formatter but its ordinary reflection prompt uses untrimmed scratchpad/context. SRC-1, `hotpotqa_runs/agents.py`.

> observations = filter(lambda x: x.startswith('Observation'), lines)
> observations_by_tokens = sorted(observations, key=lambda x: len(tokenizer.encode(x)))
> --- `hotpotqa_runs/agents.py`

If remaining non-observation text exceeds the budget after all observations are removed, `pop(-1)` can fail; the nominal target is not an unconditional compaction guarantee. Original scratchpad survives until reset, and LAST_ATTEMPT can retain it in the list, but no inspected tool retrieves deleted excerpts into the active prompt. Alternate `react.py` deletes longest lines regardless of whether thought, action or observation; it retains diagnoses across resets but does not supply the main agent's LAST_ATTEMPT modes. SRC-1, `hotpotqa_runs/react.py`.

> lines[ind]  = line.split(':')[0] + ': ...'
> --- `hotpotqa_runs/react.py`

Admission is automatic model-output append/replacement, with correctness/halt as triggers. Dataset key determines retry/correctness but the reflection prompt does not receive the key as an expected answer in the inspected builders; logs independently append it. No semantic diagnosis veto, historical-version rollback or human content approval is wired in these methods. `set_qa` changes question/key without clearing retained reflections; arbitrary library reuse could carry hints to a different question. This does not demonstrate cross-question use in shipped notebooks and prevents treating per-agent state as inherently safe task-scoped storage.

#### On [RT-RTE-webshop-trial](runtime.md#rt-rte-webshop-trial)

Configuration reload and updater selection are similar to ALFWorld, but failure admission does not test `skip`. Last three plans reach history construction and later reflection queries. The action model receives static base prompt plus character-sliced current interaction, not the history-rendered plans. This omission survives resume: reload is not action adoption. Character trimming preferentially removes old interaction prefix, preserves base prompt, and can lose the task instruction from the rolling tail; it is neither token-aware nor a retained summary. The fuller history remains available for trial logging and reflection even when excluded from action input. SRC-1, `webshop_runs/webshop_trial.py`, `webshop_runs/generate_reflections.py`; decisive action expression is quoted in the supplied route. Current HTTP HTML filtering and product-display limits are supplied context controls, not learned retained summaries.

#### On [RT-OBJ-cur-func-impl](runtime.md#rt-obj-cur-func-impl)

The durable `solution` can later acquire executable authority through [MEM-RTE-result-validation](#mem-rte-result-validation), independently of same-task model guidance. Offline validation selects solved rows; unsolved persisted programs remain archived without that validator executing them. The intended LeetCode consumer has separate limits in [MEM-RTE-leet-evaluation](#mem-rte-leet-evaluation). This annotation extends consumers without changing the supplied object's identity or claiming execution occurred.

## Write side

The trace-to-derived-memory chains are explicit, not inferred from names. ALFWorld failure log → scenario extraction → model plan → indexed list append → next trial's action input is wired. WebShop failure log → extraction → plan append → next reflection input is wired, while its action route omits plans. HotPotQA current scratchpad → optional observation deletion → diagnosis text or direct last-attempt excerpt → next reasoning/action input is wired. Programming candidate/test feedback → explanation → successor generator input is wired. Immediate-reflexion is the countercase without executed feedback; immediate-refinement delivers trace feedback without a diagnosis. Objects and route annotations above retain the different lineages and consumers.

Admission has three separate roles: models author content, host code appends/replaces it and writes files, and failure/outcome predicates determine when that happens. Operator launch flags choose the experiment and enable memory; they do not approve each generated hint. Loaded configuration/dataset content has unresolved initial authorship/control. Known automatic subsequent transformations remain established despite that uncertainty. ALFWorld failure plus not-skip, WebShop failure, HotPotQA incorrect prior attempt and ordinary programming internal failure are scheduling/admission conditions, not semantic criticism quality checks. No updater revalidates that a plan accurately describes its evidence. Sources: SRC-1, updater/agent/strategy paths cited in the corresponding records.

Curation is limited and source-native: append, latest-value replacement, last-three delivery, trace extraction, line deletion and history reset. No inspected operation merges all past plans into a validated consolidated theory. Generated hints may express reasons and stay available to the next same-task model invocation; historical logs remain separate evidence, with no automatic plan-to-source citation reconstruction. Content withdrawal is not established by recency filtering: old entries remain on disk. Correctness rejection can stop retry, suppress later tasks or merely produce an unsolved logged program. Offline validation reports a discrepancy without rewriting the old correctness label. Rust cleanup and Python timeout do not undo retained plans or arbitrary generated-code effects; see [RT-RTE-code-execution](runtime.md#rt-rte-code-execution).

## Read-back

The principal routes are automatic supply, not agent-requested retrieval. The driver or agent method rebuilds a prompt from host-selected retained values. Selection inputs are task index, agent instance, latest candidate or UCS node, strategy and list recency. Budgets differ: ALFWorld three plans without token cap; HotPotQA 1600-token trace deletion and ReAct 3896-token halt; WebShop 6400-character base-plus-tail construction without action-plan inclusion; programming no memory-specific token trimming in the inspected generic assembly. Provider output limits are separate from retained-input selection.

ALFWorld and WebShop resume are explicit caller-requested configuration loads; only ALFWorld establishes action-plan delivery. Programming resume asks the file only how many rows exist, so durable output affects task selection rather than reconstructing a model context. HotPotQA joblib files provide a whole-object checkpoint but no inspected saved-agent reload route. Standalone Python/Rust validation supplies a later saved-program execution route. The intended LeetCode evaluator remains an incomplete afforded path. These distinctions and source passages are retained in object records and [MEM-RTE-result-validation](#mem-rte-result-validation), [MEM-RTE-leet-evaluation](#mem-rte-leet-evaluation).

Working contexts resemble task-local frames in the narrow sense that selected task inputs enter and attempts reset; plans, traces or hints deliberately escape to later frames. There are no nested delegated agents in the supplied routes. The analogy does not imply a live pointer back to discarded evidence: model inputs receive rendered values, not references the model can dereference. HotPotQA placeholders and WebShop tail slicing do not supply reload operations for omitted text. External logs remain physical evidence but are not automatically reachable through a model-visible tool here.

Authority is consumer-relative. A generated plan/hint influences a model through natural-language interpretation; it is not an executable instruction or permission. A stored success flag controls host skipping by fixed rules. A saved code string becomes executable under host credentials only at a code consumer. Delivered reflection alone proves neither changed choices nor improved future capacity. The supplied routes separately retain claimed formulation, uninspected semantic dependence/content criticism, wired delivery and unobserved theory iteration/learning benefits; this report does not collapse those properties into a general success or failure verdict.

## Integration issues

1. **Additional later program consumer, not a correction of the candidate identity.** [RT-OBJ-cur-func-impl](runtime.md#rt-obj-cur-func-impl) says retention alone does not establish future execution. [MEM-RTE-result-validation](#mem-rte-result-validation) adds a source-wired consumer conditional on solved row selection. Its relation to [RT-RTE-code-execution](runtime.md#rt-rte-code-execution) is shared execution machinery, not route identity. Consequence: product persistence has a later executable consumer distinct from reflection read-back.
2. **Qualified incomplete offline LeetCode path.** [MEM-RTE-leet-evaluation](#mem-rte-leet-evaluation) adds an afforded scaffold with parent-code defects beyond the dependency limit in [RT-RTE-code-execution](runtime.md#rt-rte-code-execution). No output write exists, argv assertion conflicts with indexing, and implementations are used as both code and task dictionaries. Consequence: do not classify a durable re-evaluation output or complete later consumer from the script name.
3. **HotPotQA ownership does not enforce task reset on API reassignment.** SRC-1, `hotpotqa_runs/agents.py` changes question/key in `set_qa` without resetting reflections. [RT-RTE-hotpotqa-attempt](runtime.md#rt-rte-hotpotqa-attempt)'s shipped same-question account remains valid; reuse of an agent across questions is an exposed alternative whose actual caller is uninspected. Consequence: no universal task-isolation guarantee or demonstrated cross-question learning. [MEM-OBJ-hotpotqa-reflections](#mem-obj-hotpotqa-reflections) carries the actual retained content.
4. **Checkpoint and initial-provenance unknowns.** [MEM-OBJ-hotpotqa-checkpoints](#mem-obj-hotpotqa-checkpoints) retains unknown serialized internals and no inspected reload; [MEM-OBJ-alfworld-memory](#mem-obj-alfworld-memory) and [MEM-OBJ-webshop-memory](#mem-obj-webshop-memory) retain caller-selected resume content and required task/session identity stability. Missing facts prevent authenticated lineage and cross-run operational claims, not known subsequent writes/delivery.
5. **UCS persisted candidate mismatch.** [MEM-OBJ-state](#mem-obj-state) agrees with [RT-RTE-program-variants](runtime.md#rt-rte-program-variants) on `best.code` versus final `cur_func_impl`. Missing search internals additionally prevent full node eviction and rationale retention conclusions. A result's solved label cannot resolve which candidate was archived.

No supplied factual correction or possible duplicate is asserted. New objects are explicit material parts of supplied route containers; their shared field names do not identify the same object across task families. The two new routes have no counterpart after comparison with supplied routes. Supported qualifications and justified unknowns above remain for reconciliation rather than being erased by overall coverage.

## Limitations and checks

Source identity was rechecked with the acquired checkout's HEAD: `218cf0ef1df84b05ce379dd4a8e47f17766733a0`. Method worktree HEAD read during this attempt was `a568c6dc489ad546374536b642c3889ce23149a8`; this is a local method check, not a new evidence source. All source claims remain implementation or attributed design under SRC-1. The report used complete supplied invocation, types, members and records-contract reads, with range continuations. It did not inspect other workers, prior analyses or mutable engine state.

Uninspected historical result bodies, binary datasets/checkpoints and live providers prevent observed activation, authentic historical lineage, reproduced performance and causal learning attribution. Missing dependencies prevent full UCS search and remote grading conclusions. Static prompt/example contents and dataset-preparation lineage are not exhaustively audited; no claim of complete pedagogical or initial-content authority coverage is made. No proposed rationale was treated as validated knowledge. The WebShop omitted-plan input, immediate feedback omission, unbounded reflection accumulation and offline result defects were retained as source-supported countercases rather than generalized away.

Deterministic validation: invocation-specific `commonplace-run validate-output` passed after disambiguating the repeated HotPotQA reflection-append quotation with the validator's supplied source range. This establishes structural and quotation checks, not semantic acceptance or observed target operation.
