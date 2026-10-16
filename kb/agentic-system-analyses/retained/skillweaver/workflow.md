---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "SkillWeaver workflow account: bounded website practice through success judgment, skill synthesis and iteration checkpoint delivery."
run-id: AAS-2026-10-14-skillweaver-c921cc7a5ed0-01
reviewed-boundary: f2a63d65d0f6ff46ac30e817cede8797f8f25b97
---

# SkillWeaver workflow report

## Workflow account

The representative workflow is one website-exploration iteration, launched through `python -m skillweaver.explore reddit <out_dir>`, and its handoff to subsequent iterations. It was selected because it connects SkillWeaver's defining responsibilities: choosing practice, executing browser actions, judging the attempt, constructing reusable functions and delivering a checkpoint. This is an implementation trace through SRC-1, not an observed execution. The frozen source and external-dependency limits are in [boundary](boundary.md#source-register); no supplied run establishes successful delivery or improved task performance.

**1. Caller to scheduler.** The caller selects the website, output directory, iteration budget, model names, schedule, recovery/retrieval settings, worker count and optional initial library. The CLI applies browser patches, loads that library if supplied, obtains site containers and login state for supported benchmark sites, then invokes `explore`. Each worker receives its own browser and base URL, while all workers share the library and decision-model clients. A semaphore assigns available workers; library locks serialize task selection and update sections. They do not isolate a browser attempt from another worker's library mutation. These are asynchronous coroutines, not independently sandboxed delegated agents. See [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice), SRC-1, `skillweaver/explore.py`.

**2. Scheduler to task proposer.** The worker observes its browser before choosing a task. Under the library lock, software uses the configured schedule and the availability of untested functions to choose between test and exploration. A test function is sampled using practice-utility scores; the agent model receives its source/schema and current tree/screenshot to supply arguments. Exploration instead asks the model for a useful website task using existing function names, semantic text and the current browser observation. The task handoff is either a named function plus arguments or a natural-language task, accompanied by saved selection metadata. This is a bounded curriculum, not an externally scored experiment. No human chooses or approves each task in this route. See [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice), SRC-1, `skillweaver/explore.py`.

**3. Task driver to action model and executor.** `attempt_task` gets the task, browser, shared library, artifact directory and a ten-step limit. It starts fresh state/action lists and disabled-function names, retrieves or constructs skill descriptions once, then repeatedly asks the agent model for Python or a terminal result. Current observation and formatted previous actions reach the action model; generated Python reaches the host executor with the library code available. This handoff is not limited to invoking the advertised retrieved functions. Checker feedback can cause bounded regeneration, but the final response is returned after exhaustion rather than invariably rejected. The executor's results and exceptions enter subsequent action context. The driver stops on terminal text, step exhaustion, or a test shortcut: the generated source contains a matching named-call AST node, and the action result records no exception or recovery attempt. This syntactic named-call plus result-field shortcut does not establish that the named function executed. It returns states/actions, not a revised library. See [RT-RTE-native-task](runtime.md#rt-rte-native-task), SRC-1, `skillweaver/attempt_task.py`, `skillweaver/agent.py`.

**4. Returned attempt to success judgment.** The builder converts states/actions into a trajectory string. Its default conversion includes the initial state and actions, but excludes intermediate state renderings and explicit recovery annotations. The success-check call receives the task string, that trajectory and the final screenshot. Synthesis later receives the same trajectory but no separate final screenshot. Thus raw browser artifacts are not synonymous with the evidence delivered to either consumer. The builder also overwrites the task driver's more detailed `trajectory_pretty.txt` with its default rendering. See the workflow annotation on [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice), SRC-1, `skillweaver/explore.py`, `skillweaver/agent.py`, `skillweaver/attempt_task.py`, `skillweaver/knowledge_base/check_success.py`.

Under the library lock, the builder repeats that syntactic named-call plus result-field shortcut on the last action. A passing predicate increments the named function's test counter and bypasses success judgment and synthesis; it establishes neither dynamic execution of that function nor the intended website outcome. For example, `async def act(page):\n    if False:\n        await target(page)` contains the matching AST call without executing `target`; with no recorded exception or recovery attempt, it can pass the shortcut. This is an implementation deduction, not an observed run. The inspected predicate and countercase are also retained in [EPI-RTE-test-check](epistemic.md#epi-rte-test-check). Every attempt that does not pass the shortcut is handed to the success model. A false boolean leaves the library without a synthesized update and still proceeds to checkpoint saving; a true boolean authorizes synthesis. Model judgment is not an independent answer oracle. The benchmark evaluator is a different workflow and does not gate this admission. See [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice), [RT-RTE-benchmark-evaluation](runtime.md#rt-rte-benchmark-evaluation), SRC-1, `skillweaver/explore.py`.

**5. Success judgment to synthesis and merge.** The synthesis model receives task JSON, the formatted trajectory, semantic text, update instructions and filtered function bodies. The filter includes tested functions and the target function for a test, rather than every stored body. The builder does not supply `additional_used_functions` here. Prompt guidance requests generalized automation and documentation of unexpected behavior; this establishes a request, not compliance. Candidate checker violations are fed back for up to ten synthesis responses. A clean candidate ends the retry loop, but exhaustion still reaches `_apply`. The checks can delay a proposal, not supply an invariant final veto. Parsing/formatting failures can instead raise. The merge replaces functions by name and resets changed functions' test counts. No per-function human approval or automatic rollback to a best prior candidate is wired in this path. See [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), SRC-1, `skillweaver/knowledge_base/knowledge_base.py`.

**6. Merge to delivered result.** After either counter increment, success-false decision or completed synthesis, the worker saves `kb_post` code, metadata and semantic text under its iteration directory. Selection metadata, actions/states, success judgments and update diagnostics provide accompanying evidence where their branches run. The shared in-memory library is immediately available to other/later workers; saved prefixes permit later CLI reload and task consumption. Delivery means reaching these mutation/checkpoint interfaces, not proof that a later action invoked a changed skill. Native execution and the alternate Browser-Use consumer supply the later behavioral channels recorded in [RT-BAP-library-execution](runtime.md#rt-bap-library-execution). No run evidence establishes their activation for a particular update. SRC-1, `skillweaver/explore.py`, `skillweaver/knowledge_base/knowledge_base.py`.

**Failure and recovery boundary.** An action exception can be returned as context for the next model action, with optional local locator recovery; the recovery route can retry a checked replacement locator or re-raise. It does not roll back preceding website effects or directly rewrite the library. A nonempty recovery record on the last test action excludes it from the counter-only shortcut and instead sends it to the success-judgment branch. Recovery recorded only on earlier actions does not by itself exclude a passing last action. The default builder trajectory nevertheless omits explicit recovery annotations, so this branch cannot be described as guaranteed admission of a detailed repair trace. See [RT-RTE-locator-recovery](runtime.md#rt-rte-locator-recovery), SRC-1, `skillweaver/explore.py`, `skillweaver/agent.py`.

Iteration exceptions inside the attempt/update region produce `error.txt`; tracing stops in `finally`. Exceptions can occur before checkpoint saving, leaving no delivered `kb_post` for that iteration. Task observation/selection precedes this local `try`, and trace stopping/home navigation can themselves escape it: the handler is not universal recovery for all iteration stages. Worker availability is restored in an outer `finally`; browsers are closed by the orchestration's cleanup. The CLI's outer handler logs errors, and its final `os._exit(0)` prevents interpreting a zero process exit as proof of successful exploration. Previously saved prefixes afford manual restart, not automatic transactional recovery. These boundaries are source wiring, not experimentally observed failures. See [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice), SRC-1, `skillweaver/explore.py`.

Additional inspected implementation coverage for this member: complete `skillweaver/explore.py`; the task loop/return in `skillweaver/attempt_task.py`; trajectory formatting in `skillweaver/agent.py`; `skillweaver/knowledge_base/check_success.py`; and update/save in `skillweaver/knowledge_base/knowledge_base.py`. Provider operation, live website/container state, successful checkpoint production and later dependence on changed skills remain unobserved. The workflow supports a bounded request-to-checkpoint account, not an end-to-end reliability or benefit claim.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-explore-practice](runtime.md#rt-rte-explore-practice)

Workflow handoff: the builder regenerates and overwrites the readable trajectory after `attempt_task` returns. Its invocation uses formatter defaults; the success checker receives that reduced string plus the final screenshot, while synthesis receives the reduced string without a separate screenshot. SRC-1 implementation, `skillweaver/explore.py`, `skillweaver/agent.py`, `skillweaver/attempt_task.py`, `skillweaver/knowledge_base/check_success.py`.

> trajectory_string = codegen_trajectory_to_string(states, actions)
>
> with open(iter_dir + "/trajectory_pretty.txt", "w") as f:
>     f.write(trajectory_string)
> --- `skillweaver/explore.py`

> def codegen_trajectory_to_string(
>     states: list[State],
>     actions: list[dict],
>     only_initial=True,
>     include_recoveries=False,
> ) -> str:
> --- `skillweaver/agent.py`

The task driver's earlier rendering explicitly requests both intermediate states and recovery annotations:

> string = codegen_trajectory_to_string(
>     states,
>     actions,
>     only_initial=False,
>     include_recoveries=True,
> )
> --- `skillweaver/attempt_task.py`

Workflow rejection/delivery: the success boolean controls entry to synthesis, not whether the iteration writes a checkpoint. Failure before saving can prevent checkpoint delivery. The following contiguous passage establishes the true branch and the save outside it:

> if success_check["success"]:
>     await aprint("Successful attempt! Updating knowledge base...")
>     update_diagnostics = await knowledge_base.update(
>         api_synthesis_lm,
>         task,
>         trajectory_string,
>         f"iter_{iteration}",
>     )
>     with open(f"{iter_dir}/kb_update_diagnostics.json", "w") as f:
>         json.dump(update_diagnostics, f, indent=2)
>
> knowledge_base.save(f"{iter_dir}/kb_post")
> --- `skillweaver/explore.py`

The local exception handler records diagnostics; it does not encompass the preceding task-selection stage or guarantee rollback:

> except Exception as e:
>     await aprint(f"Error in iteration {iteration}: {e}")
>     await aprint(traceback.format_exc())
>
>     with open(f"{iter_dir}/error.txt", "w") as f:
>         f.write(traceback.format_exc())
>
> finally:
>     await browser.context.tracing.stop(path=f"{iter_dir}/trace.zip")
> --- `skillweaver/explore.py`
