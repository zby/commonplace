---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Agent Workflow Memory runtime baseline: benchmark callers, model action paths and workflow admission at the frozen source revision."
run-id: AAS-2026-10-12-agent-workflow-memory-cb2da079273e-01
reviewed-boundary: "8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1"
---

# Agent Workflow Memory runtime report

## Runtime account

AWM ships two different agent consumers, not one browser execution engine. Mind2Web predicts actions against annotated observations and scores them; WebArena supplies actions to an external BrowserGym experiment. Both admit reusable workflow text into later model inputs. Static implementation supports these connections, not successful execution or improvement. The source boundary supplies no observed runs or causal experiments (SRC-1, `mind2web/memory.py`, `webarena/run.py`; [boundary](boundary.md#boundary-and-evidence)).

### Ordinary WebArena invocation

The operator selects a website and task range in `webarena/pipeline.py`. The driver loads numeric task configuration files, selects by the first site, and sequentially launches inference, trajectory evaluation, and neural induction. Each child owns its next stage; the parent only waits. It does not test child return codes before proceeding. The inference command uses `--task`, while the consumer defines `--task_name`; default argparse abbreviation can resolve this prefix, so that spelling alone is not evidence of failure (SRC-1, `webarena/pipeline.py`, `webarena/run.py`).

`run.py` constructs an environment identity such as `webarena.0`, step budget, browser presentation options, provider/model configuration and legacy agent flags. A missing workflow file is created empty. BrowserGym owns experiment scheduling, action execution, environment observations and trace persistence through `ExpArgs.prepare` and `ExpArgs.run`. AWM then renames the experiment directory to the task identity. This is a benchmark caller, not an isolation implementation. The operator's environment and credentials determine actual website access (SRC-1, `webarena/run.py`).

For each observation, the legacy agent flattens DOM and accessibility-tree data, stores observation history and assembles a dynamic prompt with the task, history, action descriptions and optional thoughts. It computes a prompt budget and shrinks the main prompt. It separately reads the workflow file and appends it to the system message. The remote chat model chooses the action. The parser checks required answer tags and calls the configured action set's conversion method. Invalid answers produce model retry messages. Successful output updates action, thought and optional scratchpad histories and returns an action plus diagnostic metadata to BrowserGym; exhausted parsing yields `action: None` with error details. There is no inference-time subagent handoff in this traced path (SRC-1, `webarena/agents/legacy/agent.py`, `webarena/agents/legacy/dynamic_prompting.py`, `webarena/agents/legacy/utils/llm_utils.py`; [RT-RTE-browser-action](#rt-rte-browser-action)).

After a task, the evaluator reads the experiment log, task intent, final response, screenshots and summary reward. Text evaluation uses the last thought/caption and action history; vision evaluation uses the last screenshot and action history. A model-generated `success` label becomes a Boolean admission signal. The induction driver selects admitted histories, groups by task template, samples, prompts for abstract subroutines and overwrites the workflow file. A later agent action call rereads that file. Ground-truth reward selection and rule-based/manual admission are separate alternatives; none proves that an induced workflow is correct (SRC-1, `webarena/autoeval/evaluate_trajectory.py`, `webarena/autoeval/evaluator.py`, `webarena/induce_prompt.py`, `webarena/induce_rule.py`; [RT-RTE-neural-admission](#rt-rte-neural-admission), [RT-RTE-rule-admission](#rt-rte-rule-admission)).

### Mind2Web invocation and effect boundary

The driver filters downloaded benchmark tasks by website, adds candidate-ranking scores and invokes `eval_sample`. Workflow text is a user-message exemplar, followed by sampled concrete examples. Per annotated step the agent receives cleaned candidate HTML and previous *ground-truth* actions, not a page reached by executing its own predictions. Missing target candidates or oversized base context become failed steps. The model returns a textual CLICK/TYPE/SELECT prediction, which is parsed and compared to annotations. JSON conversations and metrics are the terminal effect; no browser action is executed here. Online induction later reads saved model input/output pairs. Offline induction instead reads annotated training examples (SRC-1, `mind2web/run_mind2web.py`, `mind2web/memory.py`, `mind2web/online_induction.py`, `mind2web/offline_induction.py`; [RT-RTE-benchmark-action](#rt-rte-benchmark-action), [RT-RTE-mind-admission](#rt-rte-mind-admission)).

### Forcing cases and coverage of controls

1. **Oversized workflow:** WebArena fits only the main prompt before appending workflow text. Moreover the shrinker returns an oversized prompt after exhausting iterations. Thus context fitting is best effort, not a whole-request token invariant. Mind2Web checks each added exemplar and can omit workflow text when it does not fit; it also skips oversized base queries. Delivery therefore differs between the consumers (SRC-1, `webarena/agents/legacy/agent.py`, `webarena/agents/legacy/dynamic_prompting.py`, `mind2web/memory.py`; [RT-CLM-context-budget](#rt-clm-context-budget)).
2. **Equivalent action routes:** Legacy high-level actions pass a conversion check; direct programmatic flags can select Python actions. The CLI declares `--action_space` but does not forward it into `Flags`, so the shipped `run.py` path retains the default `bid` action space. The basic demo returns raw provider text directly and bypasses the legacy parser/retry mechanism. BrowserGym's downstream action parsing and execution remain external. Conversion is not authorization, approval or sandboxing (SRC-1, `webarena/run.py`, `webarena/agents/legacy/dynamic_prompting.py`, `webarena/agents/basic/agent.py`; [RT-RTE-basic-action](#rt-rte-basic-action)).
3. **Induction as a local execution boundary:** Neural and rule induction, and trajectory evaluation, use Python `eval` on strings taken from logs. This route is outside the legacy action parser. For example neural induction evaluates a fill argument without a protective try block. Consequently a restriction inferred solely from the browser action set would omit an executable log-consumption path. Actual exposure depends on supplied log contents and host permissions; no malicious execution is observed (SRC-1, `webarena/induce_prompt.py`, `webarena/induce_rule.py`, `webarena/autoeval/evaluate_trajectory.py`).
4. **Pipeline configuration and provider mismatch:** Mind2Web's offline pipeline passes `--model`, which can abbreviate `--model_name`, but its inference child defaults independently to `gpt-4`. That model is accepted by `get_mode` and has a token-budget entry, yet is omitted from `num_tokens_from_messages`' supported set, so the default consumer can raise `NotImplementedError`. Website-matching exemplar filters also require non-null domain/subdomain strings, which the offline pipeline does not pass to inference. Online induction zips unsorted result-directory entries with samples without an identity join or success filter. WebArena evaluation defaults to `gpt-3.5-turbo` filenames whereas neural induction looks for `gpt-4o_autoeval.json`; default pipeline execution therefore does not establish successful evidence handoff. These are static obstacles/risks, not tested failures (SRC-1, `mind2web/pipeline.py`, `mind2web/run_mind2web.py`, `mind2web/memory.py`, `mind2web/utils/llm.py`, `mind2web/online_induction.py`, `webarena/autoeval/evaluate_trajectory.py`, `webarena/induce_prompt.py`).

The capability surface includes high-level browser actions, a programmatic Python action alternative, provider calls, local subprocess drivers and executable log parsing. The shipped WebArena caller grants the default `bid` plus chat subsets and multiple actions, with `is_strict=False`; this says nothing about deployed OS isolation or website credentials. There is no basis to promote the parser to a universal security guarantee. BrowserGym conversion semantics, external executor containment, provider-internal tools and service recovery are uninspected dependencies, not proven absent mechanisms (SRC-1, `webarena/run.py`, `webarena/agents/legacy/dynamic_prompting.py`).

Added implementation coverage beyond the boundary's initial helper searches comprises legacy action-set selection/answer parsing, retry, chat-model construction, context fitting, the basic demo, and the complete retrieval CLI. The retrieval CLI is not called by the default pipelines. Its random mode writes selected workflow blocks; semantic mode requests dense embeddings, but `build_memory` returns metadata instead of the FAISS object later queried. A non-null workflow suffix also references undefined `args.suffix`. These defects prevent attributing successful semantic retrieval to the inspected wiring (SRC-1, `mind2web/workflow/retrieve.py`; [RT-CMP-openai-embeddings](#rt-cmp-openai-embeddings)). All coverage here is implementation or prompt doctrine, never observed activation.

## Shared records

### Components

#### RT-CMP-chat-model
Label: Legacy chat model

Source-native identity: `ChatModelArgs.make_chat_model`, configured by `run.py`. Distributed-parametric model weights reside at the provider or configured Hugging Face backend; prompts and results are text. The constructor selects OpenAI by name prefix or a Hugging Face wrapper, including optional remote URL/hosted configuration. No parameter update is implemented by the inspected caller. Exact model revision is not pinned; default `openai/gpt-4o` is a service name, and mutable provider/URL endpoints can resolve to different weights. Provider internals and parameter changes there are uninspected (SRC-1, `webarena/agents/legacy/utils/chat_api.py`, `webarena/run.py`).

> if self.model_name.startswith("openai"):
> --- `webarena/agents/legacy/utils/chat_api.py`

#### RT-CMP-openai-client
Label: OpenAI acting, induction and evaluation clients

Source-native identity: OpenAI clients used by Mind2Web prediction/induction, WebArena neural induction, evaluation and the basic demo. These are distributed-parametric service computations, with text outputs; weights are external. Inspected code performs inference requests, not training or parameter writes. Model names are configurable aliases, not exact weight/version pins; mutable endpoints may change resolution. Evaluation and induction need not use the same model as acting. Provider-internal updates remain uninspected (SRC-1, `mind2web/utils/llm.py`, `mind2web/offline_induction.py`, `mind2web/online_induction.py`, `webarena/induce_prompt.py`, `webarena/autoeval/clients.py`, `webarena/agents/basic/agent.py`).

> response = client.chat.completions.create(
>             model=args.model_name,
>             messages=[{"role": "user", "content": prompt}],
>             temperature=args.temperature,
> --- `mind2web/online_induction.py`

#### RT-CMP-openai-embeddings
Label: OpenAI embeddings in optional retrieval

Source-native identity: `OpenAIEmbeddings(model="text-embedding-ada-002")` in the retrieval CLI. Distributed-parametric service produces dense vectors consumed by FAISS; the index can be saved on local disk. No embedding-weight update is implemented. The service name does not pin exact parameters and can resolve through a mutable endpoint; provider internals are uninspected. This is an optional retrieval component, not the default exemplar selector. Semantic retrieval contains the metadata-return defect described above (SRC-1, `mind2web/workflow/retrieve.py`).

> embedding = OpenAIEmbeddings(model="text-embedding-ada-002")
> metadatas = [{"name": i} for i in range(len(workflows))]
> --- `mind2web/workflow/retrieve.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-browser-action
Label: Legacy browser action decision

Endpoints/progression: BrowserGym observation → legacy prompt and workflow read → chat model → answer parser/retry → action and metadata → BrowserGym executor. AWM owns prompt assembly and parsing; BrowserGym owns environment effects and terminal task outcome. The principal is the configured task agent; task identity and episode histories are local state. Policy is the natural-language task/system/workflow content plus symbolic action-set configuration. Model proposes and selects actions; parser can reject malformed ones, not certify task success. Operating modes are benchmark tasks and the caller's interactive openended task; no answer oracle is consulted in action selection (SRC-1, `webarena/run.py`, `webarena/agents/legacy/agent.py`, `webarena/agents/legacy/dynamic_prompting.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Action string plus parsed thoughts, retry count, chat messages and model configuration; parse exhaustion returns a null action with diagnostics.
- Later read-back: Updated workflow files are reread on subsequent calls; ordinary episode action/thought histories also enter subsequent decisions, without proving persistent scratchpad use.
- Delegated visibility: Provider receives assembled messages; BrowserGym receives action/metadata. OS, executor and service internals are outside the frozen implementation.
- Selection predicate: Caller task/flags, current observation/history, and the exact workflow path; no per-task workflow retrieval in this consumer.
- Invalidation or expiry: Episode histories reset at construction; workflow text is read anew rather than cached. No file expiry is checked here.
- Activation or effect: Action dispatch and workflow-message delivery are wired; behavioral dependence on particular workflow content is unobserved.
- Evidence limits: No run trace; external action conversion/execution semantics and website permissions are not frozen.

> # just check if action can be mapped to python code but keep action as is
> # the environment will be responsible for mapping it to python
> self.action_space.to_python_code(ans_dict["action"])
> --- `webarena/agents/legacy/dynamic_prompting.py`

Guarantee owner: legacy parser; enforcement point: `ActionSpace._parse_answer`; guarantee strength: best effort. Covered path: legacy agent answer conversion and retry. Alternate paths: basic demo, programmatic Python action set, executable induction/evaluation parsing. Required external contract: action-set conversion accepts only what its external implementation permits and BrowserGym uses the intended set. The invariant is not independently established; successful conversion is not a permissions decision.

#### RT-RTE-benchmark-action
Label: Mind2Web annotated-step prediction

Endpoints/progression: benchmark/scores → `eval_sample` → exemplar/query assembly → OpenAI → text parsing → annotation scoring → JSON conversation. Owner: Mind2Web driver and consumer; model chooses prediction, scorer supplies a reference comparison. Operating mode: bounded benchmark replay; answer oracle: dataset target actions and positive element annotations, supplied by the external benchmark, used for metrics and previous-step context. Actual previous predictions do not determine future observations (SRC-1, `mind2web/run_mind2web.py`, `mind2web/memory.py`, `mind2web/utils/llm.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Conversation and element/action/step/task metrics written per task; no live browser effect.
- Later read-back: Saved input/output conversations feed online induction; workflow output can enter later prediction calls.
- Delegated visibility: OpenAI sees retained exemplars, task, cleaned HTML and annotated prior actions; no remote worker handoff is shown.
- Selection predicate: Website task filter, candidate ranks, exemplar tag filtering/random sampling, and sequential context-budget checks.
- Invalidation or expiry: Per-task prediction state starts fresh; oversized queries become failed steps and exemplars may be omitted. No expiry policy for workflow file.
- Activation or effect: Prediction/scoring/persistence are implemented; workflow-dependent behavior and improved accuracy are unobserved.
- Evidence limits: Downloaded benchmark and ranking scores are missing; default model/token-counter mismatch limits end-to-end confidence.

> prev_actions.append("Action: `" + target_act + "` (" + act_repr + ")")
> conversation.append("The ground truth element is not in cleaned html")
> --- `mind2web/memory.py`

#### RT-RTE-mind-admission
Label: Mind2Web workflow admission

Endpoints/progression: offline annotated examples or online saved conversations → instruction/one-shot prompt → OpenAI-generated workflow → textual filter → overwrite workflow file → later benchmark consumer. Owner: the induction scripts. Trigger: offline operator request or pipeline's interleaved induction stage; proposed change: replace workflow text. Model proposes content, symbolic filter removes website/delta blocks; software writes without per-content approval. Offline interactive mode selects a split and asks whether to stop, not whether to approve generated content. Online inputs have no success predicate and are paired by directory order. Rejection ability is limited to filtering or operator intervention outside the automatic route; no backup/rollback transaction is provided in these write functions. Read/parse/provider errors are not given a recovery loop (SRC-1, `mind2web/offline_induction.py`, `mind2web/online_induction.py`, `mind2web/utils/data.py`, `mind2web/pipeline.py`).

Guidance: shipped natural-language extraction instruction asks for common, non-overlapping subroutines of at least two steps; one-shot text supplies demonstrations. What persists is returned workflow text, not an inspectable model reasoning or criticism record. Mode: offline training induction and online benchmark induction. Answer oracle: offline annotated training trajectories guide proposals; online target task text guides formatting, but no reference outcome gate admits the write. Internal model processing is opaque; these files establish recipe extraction under fixed guidance, not an observed formulated-theory criticism loop. Memory revisions and recipe properties remain for the memory specialist.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Filtered workflow text overwrites the selected output file.
- Later read-back: `get_exemplars` reloads the workflow path in later prediction invocations.
- Delegated visibility: Provider receives instructions, one-shot and formatted examples; online examples expose last user input and model output, not full preceding messages.
- Selection predicate: Offline domain/subdomain/website; online website and unsorted result entries paired with samples; website/delta textual output filter.
- Invalidation or expiry: Whole-file overwrite; no versioned rollback or expiry in the inspected writer.
- Activation or effect: Durable context change and later message-supply path are wired; exercised use and benefit are unobserved.
- Evidence limits: Default-driver defects, unavailable benchmark data and absent runs prevent operation claims; order pairing does not establish correct trace/task identity.

> with open(args.output_path, 'w') as fw:
>     fw.write(response)
> --- `mind2web/online_induction.py`

#### RT-RTE-neural-admission
Label: WebArena evaluated neural admission

Endpoints/progression: experiment artifacts → model evaluator or summary reward predicate → accepted trace grouping/sampling → induction prompt/model → whole-file workflow write → legacy agent system-message read. Owner: evaluator and neural induction scripts; pipeline schedules them. Trigger: completed task stage or direct induction CLI. Model evaluator decides apparent success under autoeval; summary reward decides under `gt`; induction model proposes abstraction; software writes. No per-content human approval or generated-workflow test is present in this inspected writer. Parse failures skip candidate traces; no transactional backup/rollback is implemented (SRC-1, `webarena/autoeval/evaluate_trajectory.py`, `webarena/autoeval/evaluator.py`, `webarena/induce_prompt.py`).

Mode: bounded benchmark trace selection/induction. Answer oracle: `gt` uses BrowserGym `cum_reward` as external reference outcome; autoeval uses a model's status judgment, not an independent expected-answer oracle. Model judgment can reject a trace, but does not validate the generated workflow. Guidance asks for recurrent subroutines, descriptive variables and invariant element values; the returned text plus fixed action reminders persists. It does not retain a content-directed criticism of previous workflow claims. Internal model cognition and whether it produces explanatory theories are unobserved; the observable route is fixed-instruction derivation rather than an established theory-builder loop.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Evaluation JSON and rewritten workflow file, with fixed click/select reminders appended.
- Later read-back: Legacy agent appends that workflow file to its system message on subsequent calls.
- Delegated visibility: Evaluator receives final caption or image, intent, actions and response; induction receives selected query/thought/action trajectories, not all original observations.
- Selection predicate: Truthy `cum_reward` or existing model-named JSON with `record[0]["rm"]`; parseable logs grouped by intent template and randomly sampled.
- Invalidation or expiry: Whole-file replacement; existing workflow is not a proposal input, and no expiry/versioned rollback is shown in this writer.
- Activation or effect: Model-based admission and later system-message delivery are wired; changed behavior or improvement is not observed.
- Evidence limits: Default evaluator/inducer filename mismatch; external reward semantics; no actual trajectories supplied. Neural trace selection does not filter all entries by website.

> record = json.load(open(record_path))
> if record[0]["rm"]:
>     file_dirs.append(os.path.join(res_dir, f))
> --- `webarena/induce_prompt.py`

> workflows += "\n\nclick('id') # input string id value for all actions\n\nselect_option('id', 'value') # for dropdown menu"
> --- `webarena/induce_prompt.py`

#### RT-RTE-rule-admission
Label: WebArena rule and manual admission

Endpoints/progression: reward-selected experiment traces → template sampling → abstract-action deduplication → optional human accept/reject → concrete workflow text file. Owner: `induce_rule.py`; model evaluator or external reward supplies candidate signal, deterministic transformations group candidates, and human decides each selected item unless `--auto` assigns acceptance. Trigger: direct CLI request; change: replace retained concrete-example workflow text. Human veto is explicit in manual mode and bypassed in automatic mode. Rejection drops an item; parse failures skip traces; whole-file writing supplies no built-in rollback (SRC-1, `webarena/induce_rule.py`).

Mode: bounded trace curation, manual or automatic. Answer oracle: external `cum_reward` in `gt`, model status signal in autoeval; neither checks final retained content against an expected answer. Guidance is procedural extraction/deduplication plus the human review question. What persists is selected query/thought/action text, not review reasons or changed induction rules. The manual route must not be conflated with fully computational admission.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Concrete-example workflow file containing accepted items.
- Later read-back: The legacy agent can consume that file through its workflow-path hook.
- Delegated visibility: Manual operator sees formatted query, thoughts and actions; later provider sees accepted text, not rejection decisions.
- Selection predicate: Reward signal, parseable trajectory, one random item per template, abstract-trajectory deduplication and exact human `y` unless auto mode.
- Invalidation or expiry: Whole-file overwrite; no durable approval rationale or expiry mechanism in this route.
- Activation or effect: Manual/automatic curation and downstream delivery are wired; activation and benefit unobserved.
- Evidence limits: No execution artifacts or human decisions supplied; default model naming may not match evaluator files.

> if args.auto:
>     to_add = 'y'
> else:
>     to_add = input("Workflow: \n" + w + "\n\nAdd? (y/n): ")
> if to_add == 'y':
>     manual_workflows.append(w)
> --- `webarena/induce_rule.py`

#### RT-RTE-basic-action
Label: Auxiliary basic-agent action

Endpoints/progression: BrowserGym goal/accessibility tree → direct OpenAI chat call → raw content returned to BrowserGym. Owner: `DemoAgent`; model decides, external host executes. Natural-language task/action descriptions guide decision; local model/client fields are state. This separately shipped demo has no workflow-path integration, not an alternate memory admission mechanism. Mode: fixed MiniWoB demonstration; no answer oracle used by this agent (SRC-1, `webarena/agents/basic/agent.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Raw model content and empty metadata dictionary to host.
- Later read-back: inapplicable — this caller does not accumulate or reload changed workflow material.
- Delegated visibility: Provider receives current goal/accessibility tree and action descriptions; BrowserGym receives raw response.
- Selection predicate: Current observation and configured model; fixed chat/bid high-level action set.
- Invalidation or expiry: inapplicable — no durable workflow update in this caller.
- Activation or effect: Raw-response dispatch is wired without the legacy pre-return conversion/retry check; execution is host-dependent and unobserved.
- Evidence limits: BrowserGym remains external; comments suggesting a Python action set do not activate it.

> action = response.choices[0].message.content
>
> return action, {}
> --- `webarena/agents/basic/agent.py`

### Claims

#### RT-CLM-context-budget
Label: Context budget is best effort

Claimed operation: fit the WebArena main prompt to a token budget. Owner/enforcement: `fit_tokens`; guarantee strength: best effort. It excludes workflow/system additions and can return an oversized main prompt after twenty shrink iterations. Required external contract: tokenizer estimate and provider limits agree. Thus no whole-request bound follows; Mind2Web's separate exemplar checks cover only its own prediction path (SRC-1, `webarena/agents/legacy/dynamic_prompting.py`, `webarena/agents/legacy/agent.py`, `mind2web/memory.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected

> After {max_iterations} shrink iterations, the prompt is still
> {count_tokens(prompt_str)} tokens (greater than {max_prompt_tokens}). Returning the prompt as is.
> --- `webarena/agents/legacy/dynamic_prompting.py`

> if self.flags.workflow_path is not None:
>     sys_msg += '\n\n' + open(self.flags.workflow_path).read()
> --- `webarena/agents/legacy/agent.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-workflow-system
Label: Workflow system-message supply

Consumer: legacy chat model. Channel: workflow text appended to the system message. Force: natural-language guidance interpreted by the model, not executable subroutine dispatch or a guaranteed instruction precedence outcome. Horizon: subsequent action calls and task runs reading the same or overwritten file. Admission through [RT-RTE-neural-admission](#rt-rte-neural-admission) or [RT-RTE-rule-admission](#rt-rte-rule-admission) can change later supplied instructions; actual dependence remains unobserved (SRC-1, `webarena/agents/legacy/agent.py`; [RT-CLM-context-budget](#rt-clm-context-budget)).

#### RT-BAP-workflow-exemplar
Label: Workflow user-message supply

Consumer: Mind2Web prediction model. Channel: workflow file packaged as a user-message exemplar, optionally followed by concrete demonstrations. Force: interpreted natural-language guidance; predictions are independently parsed/scored, not execution of the workflow as a graph. Horizon: later sample invocations after file admission. Context limits can omit supplied exemplars, so mere file existence does not imply delivery (SRC-1, `mind2web/memory.py`; [RT-RTE-benchmark-action](#rt-rte-benchmark-action)).

> if len(workflow_text):
>     memory = [[{"role": "user", "content": workflow_text}]]
> --- `mind2web/memory.py`

## Annotations

none
