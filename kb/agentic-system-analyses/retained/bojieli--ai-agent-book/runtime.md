---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "AI Agents in Depth runtime baseline: context-agent invocation, ablation and executor counterpaths, and bounded retry-policy change admission."
run-id: AAS-2026-10-12-ai-agent-book-d56e8121d636-01
reviewed-boundary: "dbc046eb896ac4e39aa19c7774c8bf49583b89a6"
---

# AI Agents in Depth runtime report

## Runtime account

### Evidence and selected loops

This is a baseline of selected shipped workflows, not a unified production runtime. The [boundary](boundary.md#boundary-and-evidence) defines the suite and its partial reproduction loop. The ordinary trace below is the context agent's single-task CLI. Three forcing cases challenge conclusions drawn from it: context ablation changes the actual request; the adjacent code executor does not inherit calculator restrictions; and the self-modifying-agent workflow admits a candidate artifact without installing it into stable operation. All findings below use SRC-1 at the frozen commit. No target code, tests, examples, provider calls or Docker commands were executed.

Additional implementation inspection covers `chapter1/context/agent.py` completely, selected driver ranges in `chapter1/context/main.py` (single task, ablation test construction, interactive control and CLI dispatch), `chapter1/context/calc_sandbox.py` completely, provider resolution in `agentbook/providers/resolution.py` completely, and the provider import/configuration portion of `chapter1/context/config.py`. Change-plane coverage adds complete `chapter9/self-modifying-agent/demo.py`, `evolution.py`, `candidate_sandbox.py`, `sandbox_runner.py`, `llm_generator.py`, `stable/retry_policy.py`, and candidate-generation/admission ranges in `run_experiment_9_6.py`. These are implementation evidence, not observed-run evidence. The remainder of the campaign report writer, Dockerfile contents, other chapter runtimes, retained validation artifacts, external-host skills, training loops, collaboration and memory variants remain uninspected here. Their existence or names do not supply suite-wide guarantees, deployed isolation, successful reproduction or measured benefit.

### Ordinary invocation: caller task to serialized result

A human launches `chapter1/context/main.py --mode single --task ...`, optionally selecting provider, model, context mode and output path. The CLI resolves credentials before dispatch; `run_single_task` constructs a `ContextAwareAgent` and calls `execute_task`. The CLI default provider is Doubao; the agent constructor's Python default is SiliconFlow. Direct Python callers can invoke `execute_task` or its string-returning `process` wrapper without the CLI. These paths share the agent loop, not the CLI's result-file writer. SRC-1: `chapter1/context/main.py`, `chapter1/context/agent.py`.

The principal is the local process running under the launcher's OS grants. The user task and shipped system instruction are natural-language inputs. The instruction requests step-by-step problem solving with tools and a `FINAL ANSWER:` marker; it is model guidance, not an enforced correctness condition. Function descriptions are delivered alongside symbolic tool schemas. The model proposes the next action, but local Python owns progression and dispatch. Tool-call IDs associate responses with requests; there is no separate worker identity in this loop. See [RT-RTE-context-task](#rt-rte-context-task), [RT-BAP-system-prompt](#rt-bap-system-prompt) and [RT-CMP-context-model](#rt-cmp-context-model).

> Your task is to solve the given problems using the available tools. Think step by step and use tools as needed.
> --- `chapter1/context/agent.py`

The local loop appends the task to `conversation_history`, assembles mode-specific API messages, and issues a synchronous OpenAI-compatible chat completion with model ID, tool definitions, automatic tool choice, token limit and a 180-second request timeout. The caller/configuration sets the iteration ceiling, defaulting through `Config.MAX_ITERATIONS` to ten. In full mode the accumulated history goes to the next call. The runtime records detached request/response snapshots, reasoning text when exposed by the provider, and tool-call results. These observations are wired capture capacity, not supplied evidence of an actual call. SRC-1: `chapter1/context/agent.py`, `chapter1/context/config.py`.

Local dispatch maps four names to methods: PDF parsing, static-rate currency conversion, calculator and Python code interpreter. Invalid tool-argument JSON is converted to a tool error message and the loop can continue. Unknown names return an error. Known names receive unpacked arguments without a separate schema-validation or per-call approval step. The advertised conversion description says current rates, but the implementation uses a fixed dictionary; this prevents attributing live financial accuracy. PDF paths can be local or remote URLs; the process reads files or makes HTTP requests. The calculator validates an AST; the code interpreter executes Python in the host process with a reduced builtins dictionary. Neither provider-native execution nor a remote worker is used by the inspected context dispatcher. Other suite paths are not covered by that observation. SRC-1: `chapter1/context/agent.py`.

> tool_map = {
>             "parse_pdf": self.tools.parse_pdf,
>             "convert_currency": self.tools.convert_currency,
>             "calculate": self.tools.calculate,
>             "code_interpreter": self.tools.code_interpreter
>         }
> --- `chapter1/context/agent.py`

A nonempty text-only reply terminates normally whether or not it contains the marker. A reply with tool calls is executed first; a marker in that same reply can then terminate. Exhausting the ceiling can return no final answer. `completed` tests terminal text presence; `task_success` remains unknown on normal return. `run_single_task` prints the result and serializes answer, errors, trajectory, backend identity and mode to caller-selected JSON. It does not reload that JSON into future decisions. The same live object can retain earlier conversations across subsequent `execute_task` calls, notably in interactive mode, until reset or replacement. See [RT-OBJ-conversation-history](#rt-obj-conversation-history).

> completed = bool(final_answer and str(final_answer).strip())
> --- `chapter1/context/agent.py`

> "task_success": None,
> --- `chapter1/context/agent.py`

Recovery is only partially wired. Tool implementations generally catch exceptions and return error objects; malformed JSON has a dedicated continuation route. However, `agent.py` imports `OpenAI` from `openai`, not the `openai` module name, while its outer exception handler names `openai.APITimeoutError`. On an exception inside the loop, resolving that handler can itself raise `NameError`, bypassing the intended error dictionaries. This is an inspected implementation defect, not an observed failing invocation. The ablation wrapper catches exceptions from a test; interactive mode has an outer catch; the single-task function shown has no equivalent wrapper. Therefore a reliable structured-error guarantee cannot be attributed to every entry path. SRC-1: `chapter1/context/agent.py`, `chapter1/context/main.py`.

> from openai import OpenAI
> --- `chapter1/context/agent.py`

> except (openai.APITimeoutError, requests.exceptions.Timeout) as exc:
> --- `chapter1/context/agent.py`

### Forcing case 1: the request, not the stored trajectory, defines visible context

The ablation driver creates a fresh agent for each case/mode and sequentially invokes the same loop. `NO_HISTORY` supplies only system messages and the latest user task, though local trajectory still accumulates. `NO_REASONING` removes `reasoning_content` from stored assistant messages; it does not turn off hidden provider reasoning. `NO_TOOL_CALLS` supplies no tools/tool choice in the request, but does not remove local executor methods or introduce an independent response-side prohibition. `NO_TOOL_RESULTS` still runs requested tools and stores real results locally, then replaces valid results delivered to the model with the configured marker or empty string. Its malformed-JSON branch delivers an error independently of that replacement. This is intentional experimental context restriction, not a security boundary. SRC-1: `chapter1/context/agent.py`, `chapter1/context/main.py`; [RT-RTE-context-ablation](#rt-rte-context-ablation).

Interactive mode is a material stateful alternate entry. It reuses the agent for ordinary tasks; `reset` clears history/trajectory, while provider or mode switches construct a new agent. The human decides those changes, not a model-selected dynamic extension. An operator's task confirmation on a sample is launch approval, not per-tool or per-content approval. SRC-1: `chapter1/context/main.py`.

The ablation comparison's correctness oracle is not a known reference answer: its result explicitly keeps `task_success` unknown. It calls a grounding assessor using quantities in actually sent observations. That call is not evidence of correct task completion, and the assessor implementation and retained campaign results were not inspected here. The driver returns case/mode summaries; no effect of context reduction is observed in this report. SRC-1: `chapter1/context/main.py`.

### Forcing case 2: a local syntax restriction is not a process sandbox

The calculator owner is `calc_sandbox.safe_eval`, and its enforcement point is recursive AST checking before compilation/evaluation. Its covered route rejects nonwhitelisted syntax. This is a local invariant of that code path, subject to Python AST/compiler semantics. It is not a resource-bound or whole-agent isolation guarantee. Allowed arithmetic, including powers, is not given a CPU/memory budget there. The adjacent `code_interpreter` executes supplied Python directly; local PDF access and remote HTTP access are also outside the AST check. The current grant set is the launcher's process/file/network authority, not merely the four advertised schemas. No deployed OS isolation envelope is evidenced for this context process. SRC-1: `chapter1/context/calc_sandbox.py`, `chapter1/context/agent.py`; [RT-RTE-calculation-path](#rt-rte-calculation-path), [RT-RTE-code-execution](#rt-rte-code-execution).

> _check(tree)
>     return eval(compile(tree, "<safe_calc>", "eval"), {"__builtins__": {}}, ALLOWED_NAMES)
> --- `chapter1/context/calc_sandbox.py`

> exec(code, safe_namespace)
> --- `chapter1/context/agent.py`

The source calls the code interpreter namespace restricted. Inspection supports reduced named builtins, not a safe general Python execution guarantee. There is no equivalent AST validator, subprocess resource budget or OS isolation in that method. Attribute access is not filtered. This counterpath is enough to reject extending the calculator guarantee to all model-directed execution, without running or claiming a particular escape exploit. The loop ceiling bounds model/tool rounds only when each blocking call returns; it does not interrupt a nonterminating host `exec`. SRC-1: `chapter1/context/agent.py`, `chapter1/context/calc_sandbox.py`.

### Forcing case 3: change admission ends at a candidate, not production activation

`chapter9/self-modifying-agent/demo.py` separately launches diagnosis, generation, sandbox validation and manifest output. It defaults to a deterministic patch and optionally requests an LLM-generated module. The campaign driver additionally generates and evaluates a deliberately over-broad rejected control, gives its failure history to the coding model, and compares deterministic and model-generated candidates. This is a bounded experiment with fixed retry-policy expectations, not an open-ended system rewriting itself. SRC-1: `chapter9/self-modifying-agent/demo.py`, `chapter9/self-modifying-agent/run_experiment_9_6.py`; [RT-RTE-policy-candidate](#rt-rte-policy-candidate).

Diagnosis groups supplied failure trajectories with repeated non-retryable calls; at least two cases in a tool/error-code cluster trigger a proposed change. Its explicit criticism identifies retry/circuit code rather than a prompt as the target. Deterministic generation replaces exact source regions; the coding model receives stable source, diagnosis, predicted effects and rejected history, with a request to preserve public interfaces and temporary-failure behavior. The host parses a JSON source proposal. No human approves each generated module in the inspected drivers. The human selects the launch, generator/provider/model and output destination. SRC-1: `chapter9/self-modifying-agent/evolution.py`, `chapter9/self-modifying-agent/llm_generator.py`, `chapter9/self-modifying-agent/run_experiment_9_6.py`.

> "The deterministic control policy ignores retryable=false and does not open the circuit "
>             "for permanent errors. The root cause belongs in retry/circuit-breaker code, not a prompt."
> --- `chapter9/self-modifying-agent/evolution.py`

Host validation checks source size, compilation and a coarse AST deny-list before Docker execution. Candidate evaluation uses a subprocess launched with no network, read-only filesystem, unprivileged user, dropped capabilities, CPU/memory/PID limits, bounded I/O and wall-clock timeout. Missing Docker, execution failures or malformed responses fail closed through `SandboxError` and false checks. The external contract is a correctly configured Docker daemon/kernel and trusted image. An operator can override the image; its actual contents and deployment are not verified here. The tag derived from Dockerfile/runner bytes is not proof of immutable image contents. SRC-1: `chapter9/self-modifying-agent/candidate_sandbox.py`, `chapter9/self-modifying-agent/evolution.py`; [RT-RTE-candidate-validation](#rt-rte-candidate-validation).

> "--network", "none",
>         "--ipc", "none",
>         "--read-only",
>         "--cap-drop", "ALL",
>         "--security-opt", "no-new-privileges:true",
>         "--user", "65534:65534",
> --- `chapter9/self-modifying-agent/candidate_sandbox.py`

The sandbox runner executes the candidate, calls its exported policy functions, and checks expected signatures and boolean outcomes. These expectations are software answer oracles, not model judgments. They cover supplied failure cases and a handful of temporary-timeout/circuit thresholds, not every future task. Candidate code executes in the same container process as the evaluator; container separation protects the host envelope but does not by itself establish an adversarially tamper-proof answer oracle. The AST prefilter is explicitly not the isolation boundary. This is a protocol with external dependencies, not a deployment guarantee. SRC-1: `chapter9/self-modifying-agent/sandbox_runner.py`, `chapter9/self-modifying-agent/evolution.py`.

> # fast prefilter; the container, not this deny-list, is the security boundary.
> --- `chapter9/self-modifying-agent/evolution.py`

The release function decides from `changed` and all supplied check values. The normal validation callers construct the check set; a direct caller of `release_manifest` can supply a different check dictionary. The campaign adds protected-source hash comparison, which the demo does not. Artifact writing is not gated: the demo and campaign retain rejected candidates too. The manifest's `release_to_canary` is an eligibility decision; its declared scope is shadow traffic with stable unchanged. No live canary traffic or production installation was traced. Rollback readiness tests stable behavior and records its hash; it is not an exercised rollback of a deployed successor. Thus the inspected flow establishes a candidate-admission plane, not exercised self-improvement of the operational agent. SRC-1: `chapter9/self-modifying-agent/evolution.py`, `chapter9/self-modifying-agent/demo.py`, `chapter9/self-modifying-agent/run_experiment_9_6.py`.

> accepted = candidate.get("changed", False) and bool(checks) and all(checks.values())
> --- `chapter9/self-modifying-agent/evolution.py`

> "scope": "shadow traffic only; stable remains unchanged",
> --- `chapter9/self-modifying-agent/evolution.py`

### Coverage of controls and remaining limits

| Load-bearing statement | Owner / enforcement | Strength and coverage | Alternate path / external contract | Implementation conclusion status | Operation conclusion status |
| --- | --- | --- | --- | --- | --- |
| Calculator syntax is checked before evaluation | `safe_eval` / `_check` | invariant on calculator expressions | Python semantics; code interpreter, PDF I/O and other suite projects not covered | wired | uninspected |
| Model rounds stop at a ceiling or terminal reply | `execute_task` / while guard and terminal branch | best effort for returning calls, not whole-process resource isolation | direct API uses same loop; host exec can block; provider/SDK timeout behavior external | wired | uninspected |
| Candidate evaluations request container isolation | `run_in_sandbox` / Docker command and limits | protocol for validation and metrics paths | Docker daemon/kernel/image trusted; operator image override; context interpreter not covered | wired | uninspected |
| Candidate decision requires all caller-supplied checks true | `release_manifest` / conjunction | invariant of decision expression, not universal release authorization | direct calls can supply arbitrary checks; artifact writes occur independently; production activation uninspected | wired | uninspected |

The inspected capability surface contains host file/HTTP access, host Python execution, separate Docker candidate execution, and provider requests. The current context-agent tool grant is a fixed dispatcher; the actual OS grants and provider entitlements depend on launch environment. Dynamic source generation appears in the candidate workflow but does not dynamically extend the context dispatcher. The suite's other shell, callback, worker, collaboration, training and instruction-loading routes remain uninspected; there is no basis for generalizing these guarantees to them. Memory maintenance and later disk read-back have initial witnesses in the boundary and are left for the memory member, not classified as absent here. SRC-1: `chapter1/context/agent.py`, `chapter9/self-modifying-agent/candidate_sandbox.py`, `chapter9/self-modifying-agent/llm_generator.py`; [boundary](boundary.md#boundary-and-evidence).

## Shared records

### Components

#### RT-CMP-context-model
Label: Context agent completion model

Source-native identity: `ContextAwareAgent.model` and its resolved OpenAI-compatible backend. Representational form: distributed-parametric model accessed through a natural-language/message and symbolic tool-call interface. Storage substrate: external provider or local provider runtime; weights and internal provider state are opaque. SRC-1: `chapter1/context/agent.py`, `agentbook/providers/resolution.py`, `chapter1/context/config.py`.

Parameters changing during operation: uninspected — no weight update is implemented in this caller, but provider internals are unavailable. Exact version pinned: no; a configured model name is not a weight/artifact pin. Mutable endpoint resolving to another model: afforded by caller overrides, provider switching and resolution fallback; provider-side alias changes remain uninspected. Primary-key resolution can use the direct backend; missing credentials can route through OpenRouter with model mapping. GPT-5 routing has its own branch, including the explicit OpenAI/Krill selection exception. Therefore requested provider identity is not sufficient to identify the answering model. Backend fields and per-turn snapshots expose the resolved name and URL, not immutable weights.

> if available_openrouter_key:
>         return build_openrouter_backend(resolved_model, available_openrouter_key, spec.name)
> --- `agentbook/providers/resolution.py`

#### RT-CMP-coding-model
Label: Retry-policy Coding Agent model

Source-native identity: `generate_with_openai`'s `selected_model`. Representational form: distributed-parametric model; its source proposal arrives as natural-language JSON content parsed into symbolic module text. Storage substrate: OpenRouter, Ark or OpenAI service. SRC-1: `chapter9/self-modifying-agent/llm_generator.py`.

Parameters changing during operation: uninspected — this function performs inference, not a weight update, and provider internals are outside evidence. Exact version pinned: no weight digest; model argument/default or environment supplies a service identifier. Mutable endpoint resolving to another model: afforded by model/provider configuration; service-side resolution is uninspected. A seed and temperature-zero request do not establish immutable parameters or deterministic outcomes. Receipt generation records requests, responses, elapsed time and exposed usage; no receipt was adopted as run evidence here.

### Operative objects

#### RT-OBJ-conversation-history
Label: ContextAwareAgent conversation history

Source-native identity: `conversation_history`. Representational form: mixed container; role and tool-call associations are symbolic, while system/user/assistant/tool-result content reaches the model through language interpretation. Storage substrate: in-process Python list. This record describes the container; the system instruction's authority is separately recorded below. SRC-1: `chapter1/context/agent.py`, `chapter1/context/main.py`.

The list starts with a shipped system prompt, accumulates tasks, assistant messages and tool replies, and is reused by the live agent. `reset` replaces it and trajectory state. Interactive mode retains it across tasks; mode/provider switching replaces the agent. JSON result persistence in single mode is not a reload path in the inspected driver. The `NO_HISTORY` selector can omit stored decisions and results from the next request, so stored presence does not imply delivery.

> windowed.append(messages[last_user_idx])
>         return windowed
> --- `chapter1/context/agent.py`

#### RT-OBJ-retry-policy
Label: Retry-policy source candidate and stable-source comparison

Source-native identity: the complete `retry_policy.py` module string read as `stable_source` and transformed into `candidate["source"]`. Representational form: symbolic Python policy consumed by the compiler and exported-function calls; comments/docstrings also explain intended policy to the coding model. Storage substrate: read-only stable source input, in-memory proposal, and written candidate files. SRC-1: `chapter9/self-modifying-agent/evolution.py`, `chapter9/self-modifying-agent/demo.py`, `chapter9/self-modifying-agent/sandbox_runner.py`.

The operative policy distinguishes retryable/permanent errors, attempt ceiling and circuit opening. Generation does not write the stable module; the demo saves candidate source and a release manifest. It is a bounded work product and evaluator input here, not established live production machinery. Diagnosis and rejected-history material are proposal inputs, not part of the executable policy module.

### Routes

#### RT-RTE-context-task
Label: Context task execution and caller return

Endpoints/progression: CLI or Python caller → `execute_task` → resolved completion model → local tool dispatcher → later completion → caller result, optionally serialized by single-task driver. Owner: local Python loop, with the model proposing calls and answer. Effects: append messages/trajectory; tools act with host grants; terminal output is text/result dictionary. Operating mode: open task request, including supplied samples. Proposer: model; decision/veto: dispatcher rejects unknown names, caller chooses mode and ceiling; no per-tool human approval in this path. Answer oracle: none in this loop; task correctness is not inferred from completion. SRC-1: `chapter1/context/agent.py`, `chapter1/context/main.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: answer/error dictionary with trajectory, iterations and resolved backend identity; `process` reduces this to a string, and single mode writes JSON.
- Later read-back: the same agent can send accumulated earlier-task messages in a later call; saved single-task JSON has no reload in the inspected driver.
- Delegated visibility: provider receives selected messages/tool schemas; tool methods receive parsed arguments; no separate delegated worker in this loop.
- Selection predicate: configured context mode selects request messages; model response selects tool name/arguments or terminal text; dispatch uses a fixed map.
- Invalidation or expiry: reset clears history/trajectory; interactive provider or mode replacement creates a fresh agent; iteration cap ends the current loop.
- Activation or effect: wired local dispatch and response delivery; actual model compliance, correctness and beneficial effects remain unobserved.
- Evidence limits: implementation only; provider service behavior and OS grants are external; undefined `openai` in exception matching limits structured recovery.

#### RT-RTE-context-ablation
Label: Case and context-mode ablation

Endpoints/progression: case/mode enumeration → fresh agent → task route → completion/grounding summary. Owner: `AblationTestSuite`; human selects cases/modes, software iterates them. Operating mode: bounded comparison, not successor selection. Answer oracle: no reference-answer rubric in the inspected suite; observation quantities feed a grounding assessor whose internals remain uninspected. No candidate product change is admitted by this comparison. SRC-1: `chapter1/context/main.py`, `chapter1/context/agent.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: flat case-by-mode result summaries, including errors caught by the wrapper.
- Later read-back: inapplicable — inspected test construction does not reuse one arm's result as another arm's agent history.
- Delegated visibility: the provider receives each arm's actual filtered request; local trajectory can retain information withheld from it.
- Selection predicate: caller case/mode selection and the mode-dependent message/tool/result transformations.
- Invalidation or expiry: fresh agent per arm; mode-specific omission lasts for that arm; results do not automatically alter shipped prompts.
- Activation or effect: tools can still execute in no-tool-results mode while their results are withheld; performance or answer differences were not observed here.
- Evidence limits: source wiring only; no inspected retained results or independent component intervention outcome; grounding implementation uninspected.

> agent = ContextAwareAgent(self.api_key, context_mode, provider=self.provider, model=self.model)
> --- `chapter1/context/main.py`

#### RT-RTE-calculation-path
Label: AST-checked calculator execution

Endpoints/progression: model tool arguments or direct method call → `calculate` → caret rewrite → `safe_eval` → recursive AST check → evaluation → tool result. Owner: local calculator code. Context/state/effects: expression and allowed-name table, numeric result or error object; no persistent policy update. SRC-1: `chapter1/context/agent.py`, `chapter1/context/calc_sandbox.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: expression, result and type, or an error object to the calling loop.
- Later read-back: tool result can be sent on later model turns or subsequent tasks of the same live agent, except where mode filtering withholds it.
- Delegated visibility: no worker; calculation runs in the host process and its serialized result may reach the provider.
- Selection predicate: dispatcher name `calculate`; AST nodes/calls must pass whitelist rules before evaluation.
- Invalidation or expiry: current expression/result remains only in live history/trajectory unless a driver writes a report; reset replaces live state.
- Activation or effect: symbolic expression execution is wired; rejection of prohibited AST forms precedes evaluation; actual invocations unobserved.
- Evidence limits: no CPU/memory isolation guarantee; separate `code_interpreter` and file/HTTP tools are outside this enforcement point.

#### RT-RTE-code-execution
Label: Host-process Python code interpreter

Endpoints/progression: model-selected `code_interpreter` or direct Python call → reduced namespace → host `exec` → captured stdout and selected variables → tool result. Owner: `ToolRegistry.code_interpreter`. Effects: supplied Python runs in the launching process, not the candidate Docker sandbox. SRC-1: `chapter1/context/agent.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: code, result/output/variables and success flag, or caught error dictionary.
- Later read-back: returned material can enter the same live agent's later requests through tool history unless withheld by context mode.
- Delegated visibility: no worker boundary; provider sees serialized results, not the entire Python namespace as executable state.
- Selection predicate: fixed dispatcher name; result extraction checks `result` and fallback variable names.
- Invalidation or expiry: local namespace per call; result retention follows history/reset; no execution timeout in this method.
- Activation or effect: wired arbitrary Python statements with reduced named builtins; no equivalent AST restriction or OS sandbox is established.
- Evidence limits: no execution or exploit attempted; reduced builtins do not warrant broad isolation or reliable resource bounds.

#### RT-RTE-policy-candidate
Label: Failure diagnosis and retry-policy candidate admission

Endpoints/progression: supplied trajectories + stable source → deterministic diagnosis → deterministic or model generation → validation → manifest decision and candidate files. Owner: demo/campaign host; model is proposal author only on the LLM branch. Operating modes: deterministic comparison, LLM demo, and bounded campaign with rejected control. Improvement trigger: repeated non-retryable failures across at least two matching cases. Proposed change: permanent-error retry/circuit handling while preserving temporary recovery and public API. Admission/rejection: host conjunction of candidate change and checks; no content-by-content human approval. A caller may veto by not running or by withholding later deployment; no live deployment is implemented in inspected paths. Rollback/recovery: stable left unchanged, hashes recorded, stable behavior checked; failed candidates retained as artifacts. Guidance: diagnosis/change contract, stable module and explicit coding request; candidate code, diff, predictions and manifest persist. SRC-1: `chapter9/self-modifying-agent/evolution.py`, `chapter9/self-modifying-agent/demo.py`, `chapter9/self-modifying-agent/llm_generator.py`, `chapter9/self-modifying-agent/run_experiment_9_6.py`.

Answer oracle: fixed signatures and boolean retry/circuit expectations in sandbox runner, including supplied failure records and temporary-timeout thresholds; model predictions are not the oracle. The rejected control is software-authored, not a naturally occurring failed predecessor. Its evaluation summary is delivered to one subsequent coding request.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: candidate package, check dictionary and release/rejection manifest; drivers write both accepted and rejected proposals.
- Later read-back: rejected-control failed checks/reason enter the same campaign's coding-model prompt; no installed successor reload was inspected.
- Delegated visibility: coding provider receives diagnosis, rejected history and stable source; sandbox receives proposed source and cases; host receives bounded JSON verdicts.
- Selection predicate: diagnosis cluster threshold, generator CLI choice and all supplied checks true for a changed candidate.
- Invalidation or expiry: exact-region deterministic patches fail if source no longer matches; hash metadata identifies candidate/stable; no automatic expiry of written artifacts.
- Activation or effect: candidate execution is wired inside evaluation; manifest eligibility does not establish canary traffic, production activation or changed future agent behavior.
- Evidence limits: no retained campaign run was inspected; metrics and admission labels do not independently establish benefit or exercised self-improvement; direct manifest callers can provide arbitrary check sets.

Theory account: the localized retry/circuit functions express a formal rule about when retries and circuit opening should occur. Diagnosis criticizes the existing rule's omission of permanent/retryability conditions, and deterministic generation changes those exact parts. Guidance applies an unchanged objective—one attempt for permanent failures without losing temporary recovery—rather than selecting solely by a free-form model score. Stable, candidate, criticism/diagnosis and rejected-check summary can be reconstructed from saved artifacts/prompt receipts; later live operation under a candidate is not traced.

Theory-builder conditions 1–4:
- Condition 1 conclusion status: wired

Complete policy source is an individually replaceable localized formal unit; diagnosis also states the challenged behavior.
- Condition 2 conclusion status: wired

Sandbox function calls consume the policy's content to determine retries/circuit expectations and verdicts; provider interpretation of explanatory comments is not established.
- Condition 3 conclusion status: wired

Deterministic diagnosis places blame on specific retry/circuit policy omissions and exact-region generation changes them. The rejected-control summary supplies a different criticism of disabling temporary retries; model compliance with that criticism is uninspected.
- Condition 4 conclusion status: afforded

Rejected history is carried into a subsequent model proposal request within one campaign; content-dependent revision by that model and a recurrent live successor loop are not established. Mere prompt delivery does not prove iteration through criticism.

Addressability: source functions, constants and exact patch regions are inspectable/revisable at the supplied retry-policy module boundary. Persistence: candidate files and manifest outlive one run; rejected history reaches a later request within the campaign, while cross-session use is uninspected. Learning: improved future capacity is uninspected; synthetic checks and an unexecuted comparison do not establish it. Reflection: wired diagnosis receives representations of retry failures and can generate a candidate for the represented policy; the return direction into live stable behavior is uninspected, so a complete reflective loop is not established. Reflective theory builder: method/validator revision against its own operation is uninspected; the proposed update is the retry policy, not the diagnostic or release method. Autonomous theory builder: host diagnosis, proposal generation and veto are computationally wired within this bounded experiment, but autonomous fulfillment of all four conditions is not established because condition 4's content-dependent iteration is uninspected.

Self-improvement assessment boundary: the launched retry-policy campaign and stable agent policy, over the campaign and any subsequent operational use; objective: fewer redundant permanent-error calls while preserving temporary-error recovery. Evidence feeds the proposed patch, but link 2 (installed change to operational organization), link 3 (live later authority path) and link 4 (subsequent operation causally depending on that change) are not established. Evaluation consumes candidate code; that is not production adoption. No exercised self-improvement or successful improvement is attributed. A candidate-generation/admission disposition is supported independently of learning, reflection and autonomy.

#### RT-RTE-candidate-validation
Label: Container candidate validation and metrics

Endpoints/progression: host source/cases → size and AST prefilter for validation → Docker subprocess → container candidate execution and expected-output checks → bounded JSON → host checks/metrics. Owner: host runner and container evaluator. Operating mode: bounded test evaluation. Answer oracle: source-defined signatures, failure-case behavior and temporary recovery/threshold outcomes. Proposer: generation route; decision/veto: host failures/checks and manifest caller; no model has direct release authority here. This evaluation route returns evidence for admission; it does not itself install changes. SRC-1: `chapter9/self-modifying-agent/candidate_sandbox.py`, `chapter9/self-modifying-agent/sandbox_runner.py`, `chapter9/self-modifying-agent/evolution.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: parsed check/metric dictionary or `SandboxError`; validation converts sandbox errors into false checks.
- Later read-back: check summaries can feed the policy-generation route's rejected-history prompt; otherwise no evaluator-state reload in this implementation.
- Delegated visibility: disposable container receives source, trajectories and optional stable source by stdin; host receives bounded stdout JSON and limited error detail.
- Selection predicate: validation action versus metrics action; validation checks source and runs fixed expected-behavior tests, metrics executes the same policy functions for aggregate measures.
- Invalidation or expiry: disposable named container; wall-clock timeout forces removal; source/request/output limits reject oversized data; externally overridden image contents remain a trust dependency.
- Activation or effect: candidate Python runs inside the requested Docker envelope, not host execution; model-generated source is evaluated but not installed.
- Evidence limits: deployment unobserved; Docker/kernel/image correctness required; candidate and evaluator share a process, so isolation from the host is distinct from verdict integrity against hostile code.

### Claims

#### RT-CLM-context-purpose
Label: Context ablation teaching purpose

Claimed operation: agent demonstrates context importance through ablation studies. This is attributed purpose, not measured causal evidence. SRC-1: `chapter1/context/agent.py`.

> Designed to demonstrate the importance of context through ablation studies.
> --- `chapter1/context/agent.py`

#### RT-CLM-canary-decision
Label: Retry-policy canary eligibility

Claimed operation: accepted candidate receives a canary eligibility decision with shadow-only scope and stable unchanged. The code establishes manifest construction; it does not show canary deployment. SRC-1: `chapter9/self-modifying-agent/evolution.py`; supported by [RT-RTE-policy-candidate](#rt-rte-policy-candidate).

> "decision": "release_to_canary" if accepted else "reject_candidate",
> --- `chapter9/self-modifying-agent/evolution.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-system-prompt
Label: Shipped context-agent system instruction

Consumer: completion model. Channel: initial system message in `conversation_history`, retained even by `NO_HISTORY`. Force: natural-language guidance requesting tool-based stepwise solving and a final-answer marker; semantic compliance is not an invariant. Horizon: turns/tasks while the live agent persists, re-created on reset. The terminal branch also accepts unmarked text, so this instruction's wording is not a parser gate. SRC-1: `chapter1/context/agent.py`; [RT-RTE-context-task](#rt-rte-context-task).

#### RT-BAP-candidate-policy
Label: Candidate policy authority inside evaluation

Consumer: container evaluator's calls to `should_retry` and `should_open_circuit`. Channel: compiled/exec-loaded candidate Python and exported functions. Force: symbolic executable behavior determines bounded test results. Horizon: one disposable evaluation, repeated by drivers for validation/metrics. Candidate authority in later stable operation is uninspected; writing it or marking it eligible does not extend this horizon. SRC-1: `chapter9/self-modifying-agent/sandbox_runner.py`, `chapter9/self-modifying-agent/evolution.py`; [RT-RTE-candidate-validation](#rt-rte-candidate-validation).

> exec(compile(source, "candidate/retry_policy.py", "exec"), namespace)
> --- `chapter9/self-modifying-agent/sandbox_runner.py`

## Annotations

none
