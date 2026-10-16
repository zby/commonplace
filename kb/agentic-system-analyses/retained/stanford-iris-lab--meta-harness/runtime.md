---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Meta-Harness runtime baseline: reference harness search, task execution and the experimental Harbor evaluation loop."
run-id: AAS-2026-10-14-meta-harness-5e480e270fee-01
reviewed-boundary: "8123ccabe2b19fa1123090b2e5f1bacc20963ce8"
---

# Meta-Harness runtime report

## Runtime account

Meta-Harness searches executable harnesses rather than updating model weights. The operator starts a bounded search; a coding model proposes source files; software evaluates them and retains scores for another proposal. The shipped classification and terminal drivers implement that pattern differently. The experimental pilot adds an explicit evaluation tool around a child Harbor controller. These are separate entry paths, not one universal runtime. All findings below use SRC-1 at the frozen revision in [boundary](boundary.md). They describe inspected implementation and shipped instructions, not observed successful execution or measured benefit.

### Ordinary invocation: classification search

The root quick start invokes `meta_harness.py --iterations 1` from the classification directory. The driver reads configuration, sets a run-specific log directory, optionally benchmarks baselines, and starts a fresh Claude Code proposer subprocess per iteration. Its prompt points to summary, frontier, reports and pending-evaluation paths; its wrapper appends the shipped skill to the system prompt. Claude chooses filesystem reads, prototypes and edits, then writes candidate identities and hypotheses to `pending_eval.json`. The driver, not Claude, owns the next benchmark step. It removes an old pending file before proposing and skips iterations when proposal execution fails or no candidate imports successfully. See [RT-RTE-classification-search](#rt-rte-classification-search). SRC-1, `README.md`, `reference_examples/text_classification/meta_harness.py`, `reference_examples/text_classification/claude_wrapper.py`.

The benchmark constructs isolated inner-loop processes over dataset/model/candidate/seed combinations. A candidate class receives an LLM callable. The inner loop trains in the configured offline mode (online is also shipped), saves candidate state, evaluates validation predictions against dataset targets and writes results. `evaluate_memory` runs predictions concurrently on the same instance and does not call `learn_from_batch`; that is not enforcement of candidate immutability. A candidate can mutate inside `predict`. Results produce a validation frontier and evolution summary containing hypotheses and outcomes. The next proposer is instructed to read these artifacts, including training traces, and to write missing post-evaluation reports. Memory-internal revision rules are left to the memory analysis. SRC-1, `reference_examples/text_classification/config.yaml`, `reference_examples/text_classification/benchmark.py`, `reference_examples/text_classification/inner_loop.py`, `reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md`.

Final testing is an explicit separate driver mode: choose baselines and validation winners, write a finalization marker, load saved training memory, evaluate test splits and mark complete only after required results exist. This is operational sequencing, not a secrecy boundary. See [RT-RTE-classification-finalize](#rt-rte-classification-finalize).

### Material alternatives and forcing cases

1. **Import versus isolation.** Both reference drivers execute candidate Python during validation; the terminal driver additionally requires a Terminus2 subclass and normally a smoke trial, but smoke can be skipped. The pilot instead AST-checks source before staging it for child Harbor import. Thus neither a universal import-free controller nor a universal sandbox guarantee follows. Child Python runs in the Harbor orchestration path; a subprocess is not itself a security boundary. See [RT-RTE-terminal-search](#rt-rte-terminal-search) and [RT-RTE-pilot-search](#rt-rte-pilot-search).
2. **Natural-language restrictions versus actual grants.** Classification says not to delegate, while the proposer grant includes `Agent`. Terminal instructions explicitly request analysis and implementation subagents. Both grants include Bash, Edit and Write. The wrapper disables ambient skill/MCP discovery and passes an explicit tool set, but also requests `--dangerously-skip-permissions`. No per-candidate human approval gate is wired in these drivers. The restrictions on modifying evaluation machinery and avoiding benchmark-specific hints are model-facing policy, not filesystem access enforcement. See [RT-BAP-proposer-instructions](#rt-bap-proposer-instructions).
3. **Direct provider and tool paths.** Terminal candidates may override any method and make raw API calls. The baseline already calls LiteLLM directly rather than Harbor Chat for inference. Its image reader is another model-call path. Neither the classification LLM wrapper's cache/truncation nor proposer tool restrictions cover these paths. See [RT-RTE-kira-execution](#rt-rte-kira-execution).
4. **Budgeted evaluation versus shell and direct controller paths.** The pilot's outer `_evaluate` decrements its private state after a controller result and rejects calls at zero; its shell tool is a separate route to the outer container. The controller CLI can also be invoked independently and does not implement that budget. Source filtering catches literal forbidden strings plus a minimal AST interface, not equivalent obfuscated behavior. The final verifier checks report arithmetic and maximum accepted reward, not source provenance or final candidate equivalence. See [RT-RTE-pilot-search](#rt-rte-pilot-search).

These cases were inspected as source, not executed adversarially. The deployed host filesystem, actual credentials, Claude Code implementation, Harbor imports and remote environments remain external contracts. They prevent a claim of verified deployed isolation. Capability is broad Python/shell/model access; the current reference proposer grant is the explicit tool list; the deployed isolation envelope is unobserved. SRC-1, `reference_examples/text_classification/claude_wrapper.py`, `reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md`, `experimental/harbor_meta_harness/controller.py`.

### Controls, guarantees and working context

| Load-bearing property | Owner, enforcement and strength | Coverage and counterpath | Required external contract and status |
|---|---|---|---|
| Completed classification run refuses further evolution | Driver checks `finalized.json` before evolution; protocol | That driver/run name only; direct benchmark/inner-loop calls, source edits and other run names are not covered. An `in_progress` marker does not trigger the completed-run guard. | Writable marker and result files must remain trustworthy. Implementation conclusion status: wired. Operation conclusion status: uninspected. |
| Candidate compatibility | Reference import check; terminal subclass check; pilot AST interface; protocol | Admission to the selected evaluation path only. Successful import or inheritance does not establish safety or useful predictions. Pilot does not type-check inherited runtime semantics. | Python and Harbor must load/run compatible candidates. Implementation conclusion status: wired. Operation conclusion status: uninspected. |
| Pilot evaluation-tool budget | Outer agent's immutable `EvaluationState`, zero check and decrement; invariant over normally completed `_evaluate` calls with a nonnegative configured budget | Only this agent's evaluation tool, not standalone controller invocation or all compute/spend. Exceptions before `record` can leave a call uncharged. | Valid suite budget and functioning controller/result transfer. Implementation conclusion status: wired. Operation conclusion status: uninspected. |
| General-purpose candidates and no benchmark references | Proposer instructions; policy; pilot adds a literal-string rejection protocol | Instruction compliance unobserved; AST/string filter covers source spelling, not all actions Python can perform. | Model compliance and external isolation cannot be inferred. Implementation conclusion status: wired. Operation conclusion status: uninspected. |

Sources: SRC-1, `reference_examples/text_classification/meta_harness.py`, `reference_examples/terminal_bench_2/meta_harness.py`, `experimental/harbor_meta_harness/agents/meta_harness.py`, `experimental/harbor_meta_harness/controller.py`.

Working-context control is route-specific. Each reference proposal starts a new Claude process, with selected paths rather than all prior transcript content pushed into the new context. The terminal skill requests two separate subagent contexts with summary/hypothesis and implementation-status returns; their actual context isolation is Claude Code's external responsibility. Classification instead asks for one main context despite granting Agent. This resembles selected-input frames whose returned text escapes, but files edited by a child remain shared effects, not frame-local values. Neither path provides a repository-enforced prohibition on alternate reads. SRC-1, `reference_examples/text_classification/claude_wrapper.py`, `reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md`, `reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md`.

At task inference, classification's LLM callable removes the middle of prompts exceeding 224,000 characters and preserves head and tail plus a marker; this is a character heuristic, not a strict token bound. Removed content has no reload mechanism in that wrapper. Pilot tools return only stdout/stderr tails (12,000 characters each for the outer agent), while maintaining accumulated messages until termination. KIRA exposes proactive summarization and overflow recovery; the exact inherited summarizer's selection and retention are uninspected external behavior. Its fallback supplies the original instruction plus the last 1,000 screen characters. See [RT-RTE-kira-execution](#rt-rte-kira-execution). SRC-1, `reference_examples/text_classification/llm.py`, `experimental/harbor_meta_harness/agents/meta_harness.py`, `experimental/harbor_meta_harness/agents/terminal_harness.py`.

> prompt = prompt[:half] + "\n\n... [TRUNCATED] ...\n\n" + prompt[-half:]
> --- `reference_examples/text_classification/llm.py`

Additional inspected coverage beyond the boundary's initial trace includes provider cache-key construction and prompt truncation, terminal subclass validation and native-call recovery, pilot terminal scaffold and complete outer verifier, and onboarding. These supply implementation or doctrine/design evidence only. Supporting tests and downloaded collection payloads were not executed; provider internals, actual search traces, full inherited Harbor summarization and causal comparisons remain unobserved or outside the frozen source. This limits reliability, activation and performance conclusions without negating wired routes.

## Shared records

### Components

#### RT-CMP-claude-proposer
Label: Claude Code proposer model

Distributed-parametric model accessed through the external `claude` executable; weights reside in an external service, not repository files. Both drivers request `model="opus"` with `effort="max"`. No parameter-update operation is wired here; exact weights/version are not pinned, and the alias can resolve to another model. Claude Code's internal model routing and compaction are uninspected. SRC-1, `reference_examples/text_classification/meta_harness.py`, `reference_examples/terminal_bench_2/meta_harness.py`, `reference_examples/text_classification/claude_wrapper.py`.

> model="opus",
> allowed_tools=PROPOSER_ALLOWED_TOOLS,
> --- `reference_examples/text_classification/meta_harness.py`

#### RT-CMP-classification-llm
Label: Classification LLM

Distributed-parametric solver behind LiteLLM and optionally an OpenAI-compatible endpoint. Configuration names `openrouter/openai/gpt-oss-120b`; runtime accepts configured models and API base. Parameters are not changed by inspected wrapper operations. A model string is not a weight digest; exact version is unpinned and a mutable endpoint can serve another model. Model outputs can be cached as symbolic keyed files, distinct from weights; cache keys include normalized model, API base, system prompt, prompt and kwargs, not backend weight identity. SRC-1, `reference_examples/text_classification/config.yaml`, `reference_examples/text_classification/llm.py`.

> response = litellm_completion(model=model, messages=messages, **call_kwargs)
> --- `reference_examples/text_classification/llm.py`

#### RT-CMP-kira-llm
Label: KIRA task model

Distributed-parametric external solver accessed through LiteLLM, including a separate image-call path. Default adapter model is `anthropic/claude-opus-4-6`, overridable by `HARBOR_MODEL`; the agent uses its configured model name. No parameter updates are wired. Exact weights are not pinned, and provider/endpoint resolution may change. The ordinary and image paths bypass any guarantee located only in Harbor Chat inference. SRC-1, `reference_examples/terminal_bench_2/scripts/run_eval.sh`, `reference_examples/terminal_bench_2/agents/baseline_kira.py`.

> This bypasses harbor's Chat class to get access to tool_calls.
> --- `reference_examples/terminal_bench_2/agents/baseline_kira.py`

#### RT-CMP-pilot-outer
Label: Pilot outer model

Distributed-parametric service called with `self.model_name`, provided by Harbor configuration. Weights are external; no parameter changes are implemented in this outer loop. Exact model version is unpinned and the configured service may resolve differently. This model chooses edits and evaluation calls, not task-level reward computation. SRC-1, `experimental/harbor_meta_harness/agents/meta_harness.py`.

> model=self.model_name,
> messages=messages,
> tools=tools,
> tool_choice="auto",
> temperature=0,
> --- `experimental/harbor_meta_harness/agents/meta_harness.py`

#### RT-CMP-pilot-child
Label: Pilot child model

Distributed-parametric task solver external to the controller. The suite's `child_model` is passed to Harbor; the loader default is `openai/gpt-5.4-nano`. No parameter modification is wired in the controller or shipped terminal scaffold. Exact weight identity is not pinned; endpoint resolution may change. Generated Python can introduce other model calls, so this component covers the configured child path, not every possible candidate. SRC-1, `experimental/harbor_meta_harness/controller.py`, `experimental/harbor_meta_harness/agents/terminal_harness.py`.

> child_model=raw.get("child_model", "openai/gpt-5.4-nano"),
> --- `experimental/harbor_meta_harness/controller.py`

### Operative objects

#### RT-OBJ-pending-eval
Label: Pending evaluation manifests

The two reference experiments each use a run-local `pending_eval.json`: symbolic JSON read by their driver, containing candidate identifiers and model-authored natural-language hypotheses. Identity is the manifest handoff, not the candidate implementation or later score store. Both drivers delete the old manifest before proposing and parse the replacement. Classification imports named agent files; terminal normalizes the class portion of an import path to `AgentHarness`. SRC-1, `reference_examples/text_classification/meta_harness.py`, `reference_examples/terminal_bench_2/meta_harness.py`.

> candidates = json.loads(PENDING_EVAL.read_text()).get("candidates", [])
> --- `reference_examples/text_classification/meta_harness.py`

### Routes

#### RT-RTE-classification-search
Label: Classification candidate search and admission

Operator invocation → baseline evaluation → Claude proposal → manifest → import check → benchmark child processes → validation frontier/summary → next proposal. Owner alternates between deterministic Python driver and model-based coding session. Candidate Python is symbolic executable content on disk; hypotheses, reports and proposer skill are natural-language guidance. The proposal can change retrieval, prompts, learning strategy and memory structure. The driver admits importable candidates without a human content decision or a score-improvement threshold; score comparison selects frontier entries, not permission to run code. The operator can stop the loop and controls starting configuration. SRC-1, `reference_examples/text_classification/meta_harness.py`, `reference_examples/text_classification/benchmark.py`, `reference_examples/text_classification/inner_loop.py`.

- Immediate return: Benchmark scores and log paths to the driver; iteration status to the operator. Proposer terminal text is not the candidate list authority; the JSON manifest is.
- Later read-back: Next model session is instructed to read evolution summary, frontier, recent training traces and prior code; read completion and model reliance are unobserved.
- Delegated visibility: Skill requests all work in the main session; Agent is nevertheless in the granted tool set. Actual child visibility is host-dependent.
- Selection predicate: Import success admits evaluation; validation accuracy and context-size Pareto computation determine frontier, with per-dataset best entries also retained. Training uses configured offline/online mode; default configuration is offline with one epoch.
- Invalidation or expiry: Pending manifest is deleted each iteration; run-specific log directories separate histories. Usable existing result files are skipped by benchmark scheduling rather than automatically invalidated by source hash.
- Activation or effect: Imported candidate code determines the instantiated MemorySystem and can alter subsequent model inputs and learning calls; exercised behavior and benefit are unobserved.
- Evidence limits: No actual proposal, trace, correctness measurement or compliance with three-candidate/prototyping requirements was supplied. Python import checking is code execution, not isolation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Answer oracle: dataset targets passed to the dataset evaluator, not the proposer model's judgment. Mode: bounded experiment over configured datasets, seeds and iterations. Improvement trigger: each iteration's instruction to propose mechanisms using past scores/traces. Software may reject failed imports or benchmark failures; human review of each candidate is not required. Recovery skips failed proposals/invalid sets, resumes numbering from summary, and reuses usable results. Candidate copies and histories afford manual rollback; no automatic transactional restoration of arbitrary filesystem edits is shown. SRC-1, `reference_examples/text_classification/meta_harness.py`, `reference_examples/text_classification/benchmark.py`, `reference_examples/text_classification/inner_loop.py`.

> if result.returncode == 0 and "OK" in result.stdout:
> --- `reference_examples/text_classification/meta_harness.py`

> Formulate 3 hypotheses — each must be falsifiable and target a different mechanism.
> --- `reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md`

Theory account: the skill supplies mechanism-first guidance, asks falsifiable hypotheses, prototyping, self-critique and reports explaining regressions. It requests criticism and revision, but source code does not establish that a model actually formulates blame or changes reliance. Hypotheses, candidate programs, summaries and requested reports persist across rounds of one run; later proposer is their intended reader. Addressability is file/method-level for executable rules and field-level for hypotheses; no complete theory rationale is guaranteed. Theory-builder conditions 1–4: condition 1 conclusion status: afforded (whole executable mechanisms and hypothesis fields can state theories); condition 2 conclusion status: wired (executed candidate rules govern predictions); condition 3 conclusion status: claimed (content-directed criticism requested, no supplied instance); condition 4 conclusion status: claimed (reports/history are requested inputs to another round, not demonstrated criticism-mediated iteration). Learning: uninspected improvement, no measured future-capacity gain. Reflection: architectural feedback represents candidate identity/hypothesis/outcome and delivers that representation to another proposer; actual two-way reliance is unobserved. Reflective and autonomous theory-builder operation is not established by model availability. Self-improvement is only a dispositional pathway at the enclosing builder-plus-task-harness boundary over search rounds, with validation performance as independent objective: evidence is supplied to proposals, code can become later solver organization, and imports can give it behavioral force; actual evidence-responsive determination and subsequent exercised dependence (links 1 and 4) are not observed. No successful self-improvement is claimed.

#### RT-RTE-classification-finalize
Label: Classification finalization and direct evaluation

Operator `--test` → select baseline/frontier systems → marker → benchmark test jobs loading saved memory → results/completion marker. Driver owns selection and completion; benchmark owns scheduling; inner loop owns load and prediction. Direct `benchmark.py` and `inner_loop.py` invocations are alternate entry paths without the outer completion guard. SRC-1, `reference_examples/text_classification/meta_harness.py`, `reference_examples/text_classification/benchmark.py`, `reference_examples/text_classification/inner_loop.py`.

- Immediate return: Test metrics and either complete finalization or explicit failure/missing-result report.
- Later read-back: Saved training memory is loaded for test prediction; completed test results are reused on subsequent result display. No outer proposer invocation is made by finalization.
- Delegated visibility: Child receives memory path, dataset/model/seed configuration and requested test output path; test secrecy from a shell-capable proposer is not enforced.
- Selection predicate: Baselines, aggregate validation Pareto entries and per-dataset validation winners; dataset evaluator compares predictions to targets.
- Invalidation or expiry: `complete` marker blocks ordinary evolution for that run name; `in_progress` allows incomplete finalization recovery. Existing usable test files can be skipped; no code-digest invalidation is shown.
- Activation or effect: `set_state` supplies retained training state before task predictions; candidate may consume it according to its implementation.
- Evidence limits: Operational separation does not prove no test access, no contamination or a frozen candidate byte identity. No test run was observed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Mode is one final test pass, with retries after failures. Proposal is inapplicable here: selected code already exists. Software vetoes final completion when jobs fail or required result groups are missing; the operator starts/restarts finalization. Oracle remains target-backed dataset evaluation. SRC-1, `reference_examples/text_classification/meta_harness.py`, `reference_examples/text_classification/benchmark.py`.

> if state.get("status") == "complete":
> --- `reference_examples/text_classification/meta_harness.py`

> state = Path(args.load_memory).read_text()
> memory.set_state(state)
> --- `reference_examples/text_classification/inner_loop.py`

#### RT-RTE-terminal-search
Label: Terminal candidate search and admission

Operator → Claude session → manifest import path → subclass validation → optional one-task smoke trial → Harbor full-dataset trials → pass rates/metrics → frontier and summary → next proposal. The skill requests one analysis subagent returning state/hypothesis, followed by one implementation subagent returning file and import status. Driver executes candidates; task-level Harbor verifiers provide outcomes. Candidate class is normalized to `AgentHarness`, but arbitrary Python methods and raw API calls are an intentional search surface. SRC-1, `reference_examples/terminal_bench_2/meta_harness.py`, `reference_examples/terminal_bench_2/scripts/run_eval.sh`, `reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md`.

- Immediate return: Import/smoke result, per-task pass rates, aggregate score and runtime/cost summaries to driver and operator.
- Later read-back: Frontier, evolution summary, candidate code and successful/failed trajectories are instructed inputs to the next proposer/analysis child.
- Delegated visibility: Analysis receives state/trajectory/code paths; implementation receives the selected change and working directory. Files are shared; actual host context filtering is uninspected.
- Selection predicate: Import of exact class and Terminus2 inheritance; smoke normally requires no errors but can be skipped. Frontier replaces entries on better per-task or average pass rate. Optional final pass reevaluates the overall winner for five trials on the same full dataset.
- Invalidation or expiry: Fresh pending manifest each iteration; smoke job can be removed before rerun. Existing histories/results can support resume; no universal code-hash invalidation is established.
- Activation or effect: New Python/prompt files are loaded by Harbor; candidate can alter tools, observation transformation, model invocation or command execution.
- Evidence limits: No exercised delegation or candidate improvement observed. Final full-dataset pass is not an untouched holdout. Remote execution and verifier correctness depend on external Harbor/services.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger and mode: bounded iterations and repeated task trials. Model proposes and implements; driver rejects invalid subclasses and, unless bypassed, failed smoke trials. Human sets model, iterations/concurrency and can interrupt, but no content-by-content approval is wired. Answer oracle is Harbor verifier reward, not model critique. Recovery records failed benchmarks as zero results, continues iterations and retains earlier frontier winners; candidate files are not automatically rolled back. Guidance requests one mechanism per candidate, no task-specific hints, no edits to existing agents/driver/wrapper, and trajectory-led hypotheses. These are policies rather than filesystem vetoes. SRC-1, `reference_examples/terminal_bench_2/meta_harness.py`, `reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md`.

> if args.skip_smoke:
> --- `reference_examples/terminal_bench_2/meta_harness.py`

> The search space is arbitrary Python code.
> --- `reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md`

Theory account: hypotheses describe expected mechanism effects, and source/prompt code embodies revisable task policies. Candidate files, hypotheses, results and trajectories persist across rounds. Theory-builder conditions 1–4: condition 1 conclusion status: afforded (localized rule/hypothesis content); condition 2 conclusion status: wired (candidate rules execute); condition 3 conclusion status: claimed (failure-mode analysis requested, no inspectable criticism instance); condition 4 conclusion status: claimed (later rounds requested to use history, no demonstrated retention of criticism's result). Addressability is individual Python methods, prompt files and hypothesis fields. Learning: improved future capacity is uninspected. Reflection: candidate/trajectory/score representation is available for changes to that same task machinery, but actual representation-mediated changes are unobserved. Reflective/autonomous theory-builder operation is not established. Self-improvement is dispositional at the enclosing search-plus-solver boundary, over rounds and toward pass rate: candidate admission and execution are wired, while observed evidence-responsive determination and subsequent causal dependence are missing. At the narrower standalone proposer boundary the task harness is its output, not necessarily its own organization.

#### RT-RTE-kira-execution
Label: KIRA task execution and recovery

Harbor instruction/environment → inherited Terminus2 setup → KIRA episode loop → native LiteLLM tool call → parsed shell/image/completion actions → environment effects and next prompt. The model decides actions; KIRA parses and executes, with inherited terminal-session machinery. Shell commands modify task-container files; image handling makes an additional model call. Task completion requires the baseline's confirmation exchange; grading is external Harbor responsibility. SRC-1, `reference_examples/terminal_bench_2/agents/baseline_kira.py`, `reference_examples/terminal_bench_2/prompt-templates/terminus-kira.txt`.

- Immediate return: Commands/tool feedback, terminal observations and image-reading response to the episode loop; eventual task termination to Harbor.
- Later read-back: Summarization/handoff prompts can carry transformed current task history into a later inference. Cross-task learned memory is not established by the inspected baseline.
- Delegated visibility: Native model request contains copied chat messages plus new prompt; image calls receive a constructed multimodal request. Inherited summarization references can be recorded as subagent trajectory references; actual inherited child context is uninspected.
- Selection predicate: Model tool choice parsed by KIRA; context overflow when summarization enabled or proactive inherited check triggers handoff. Finite episode loop and session liveness bound progression.
- Invalidation or expiry: Overflow unwinds messages to free tokens and requests summary; if that fails, fallback keeps original instruction plus last 1,000 screen characters. Exact inherited preferential eviction/retention is outside inspected code.
- Activation or effect: Parsed commands execute in tmux-backed task environment; summarized context is supplied to subsequent model calls. No measured fidelity or benefit established.
- Evidence limits: Inherited Harbor internals, provider-native enforcement and actual deployed isolation are uninspected. Candidate overrides need not preserve these controls.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Recovery includes context-window exception conversion, summarization retry and output-length handling. Command execution adds completion markers, polls for them, then removes marker-containing output lines before applying the inherited output limiter (requested limit 30,000 bytes). The image call uses a separate request containing the image-reading instruction and base64 image, not the whole chat history; the analysis text returns to the task loop. This is a selected-input frame with an escaping textual result, not an independent persistent task memory. Baseline controls cover this implementation, not arbitrary subclass replacements. Ordinary message accumulation and placeholder tool acknowledgements are not proof that every real tool outcome reaches the next model verbatim. SRC-1, `reference_examples/terminal_bench_2/agents/baseline_kira.py`.

> self._unwind_messages_to_free_tokens(chat, target_free_tokens=4000)
> --- `reference_examples/terminal_bench_2/agents/baseline_kira.py`

> f"{original_instruction}\n\nCurrent state: {limited_screen}"
> --- `reference_examples/terminal_bench_2/agents/baseline_kira.py`

#### RT-RTE-pilot-search
Label: Pilot edit evaluate and score loop

Harbor starts outer `AgentHarness` with instruction/environment/model. A system prompt asks it to improve `/app/harness.py`; the model selects shell edits or `evaluate_harness`. Evaluation downloads source to host logs, invokes controller in a subprocess, validates literal forbidden references and AST interface, stages a temporary `candidate.py`, then starts child Harbor jobs sequentially for suite tasks. Controller reads verifier rewards and aggregates by suite policy. Outer state records the result and returns score/task summaries plus remaining budget to the model. On no tool calls or turn exhaustion it uploads evaluation history; the task verifier awards the maximum accepted historical reward if report arithmetic is valid. SRC-1, `experimental/harbor_meta_harness/agents/meta_harness.py`, `experimental/harbor_meta_harness/controller.py`, `experimental/harbor_meta_harness/tasks/select-harness/tests/test_outputs.py`.

- Immediate return: Shell exit/output tails or evaluation reward/task summaries to outer model, then history artifact and verifier scalar to enclosing Harbor task.
- Later read-back: Evaluation outcomes are added to messages for later proposals within this run. Child jobs receive staged source, not the outer model's whole conversation.
- Delegated visibility: Controller receives downloaded source and selected suite; children receive candidate module, child-model config and task environment. Task verifiers remain a separate scoring path, not an admitted candidate input by design.
- Selection predicate: Outer model chooses edits/evaluation times. Controller admits source with required class/base/async run and no forbidden literals; it scores every suite task. Final verifier chooses maximum accepted historical reward, not reward of final `/app/harness.py`.
- Invalidation or expiry: Evaluation state resets per outer run; normal completed calls consume budget. Temporary candidate directory is deleted after evaluation. Host source snapshots and inner-job results persist in logs. Turn bound is `max(24, eval_budget * 3)`.
- Activation or effect: Child Harbor imports candidate and may execute its arbitrary Python; the outer model receives evaluation feedback for another edit. Activation and improvement were not observed.
- Evidence limits: String/AST admission is not a semantic safety proof. Budget does not cover direct controller invocations, arbitrary shell compute or exceptions before recording. Verifier arithmetic is not cryptographic provenance or final-artifact revalidation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Mode is bounded suite experimentation; trigger is model-selected evaluation after code edits. Model supplies changes, software admits/rejects source and computes scores, human supplies initial task/suite/budget but is not asked to approve each change. Answer oracle is child task verifier reward. Syntax/forbidden/interface errors reject without score; missing/malformed child results, nonzero child exit and timeout yield zero reward. Outer evaluator nonzero exit is recorded as rejection, while general tool exceptions return errors without guaranteed budget decrement. There is no automatic restore-best step: historical best reward and final code are distinct outputs. SRC-1, `experimental/harbor_meta_harness/controller.py`, `experimental/harbor_meta_harness/agents/meta_harness.py`, `experimental/harbor_meta_harness/tasks/select-harness/tests/test_outputs.py`.

> if item.lower() in lowered:
>     return f"forbidden benchmark reference: {item}"
> --- `experimental/harbor_meta_harness/controller.py`

> next_state = state.record(result)
> --- `experimental/harbor_meta_harness/agents/meta_harness.py`

> reward = max(rewards, default=0.0) if valid else 0.0
> --- `experimental/harbor_meta_harness/tasks/select-harness/tests/test_outputs.py`

Guidance persists initially as source/system prompt: improve the general harness, use scarce evaluations and avoid benchmark references. Candidate programs and snapshots persist, but no separate criticism field is enforced. Theory-builder conditions 1–4: condition 1 conclusion status: afforded (whole program rules are replaceable); condition 2 conclusion status: wired (child executes admitted rules); condition 3 conclusion status: uninspected (no content-directed criticism evidence supplied); condition 4 conclusion status: uninspected (scores recur, but criticism-mediated iteration not established). Addressability is source-file/class/method-level; persistence is one outer run plus logs, with no wired automatic next-run reuse established. Learning and beneficial self-change are unobserved. Reflection has a wired representation loop from harness snapshot to evaluation feedback to outer editing opportunity, not observed model reliance. Autonomous/reflective theory-builder operation is not established. At enclosing outer-plus-child boundary this is dispositional improvement-directed self-change toward suite reward; exercised causal links 1 and 4 remain unestablished. No successful self-improvement claim follows from the reported maximum.

#### RT-RTE-domain-onboarding
Label: Domain specification handoff

Operator asks a coding assistant to adapt Meta-Harness → repository onboarding text guides questions and interface inspection → `domain_spec.md` → stop pending separate implementation request. This is shipped natural-language procedure, not an executable adaptation driver. Human supplies consequential choices; assistant proposes defaults and records unknowns. SRC-1, `README.md`, `ONBOARDING.md`.

- Immediate return: A domain specification with task, mutable boundary, evaluation, baseline, budget, evidence and smallest acceptance check.
- Later read-back: Another implementation agent is the intended reader of the specification; actual later loading is unobserved.
- Delegated visibility: Handoff should be understandable without original conversation. It includes decisions/defaults/unknowns, not a required full conversation transcript.
- Selection predicate: Fit requires repeated tasks, consistent success evaluation and a plausible benefit from harness changes with fixed base model. User decisions govern scope; assistant resolves or marks unknowns.
- Invalidation or expiry: Existing domain specification must be read before edit and unrelated content preserved; no automatic version/revocation mechanism is specified.
- Activation or effect: Provides a plan capable of shaping a later implementation; explicitly withholds authority to implement or evaluate during onboarding.
- Evidence limits: Instructions establish requested behavior only. No completed handoff, downstream execution or compliance supplied.
- doctrine conclusion status: claimed
- operation conclusion status: uninspected

Admission: operator conversation is the decision channel, not automatic code acceptance. Proposed defaults are not confirmed decisions; a proposed budget grants no spend. Recovery is a partial spec with explicit unknowns when consequential answers are unavailable. This route does not revise executable machinery itself. Oracle is inapplicable — onboarding elicits task success criteria rather than scoring candidate answers. Mode is an open adaptation request ending in a bounded plan. SRC-1, `ONBOARDING.md`.

> Do not implement the system or run evaluations during onboarding.
> --- `ONBOARDING.md`

### Claims

#### RT-CLM-fixed-model
Label: Fixed-model harness search

Declared operation is executable search around a fixed base model. The inspected routes implement code/prompt/state changes, not weight training. This supports an architectural search claim, not fixed exact endpoint identity, exercised gains or paper-result reproduction. See model mutability in the component records and admission in the search routes. SRC-1, `README.md`, `ONBOARDING.md`.

> Meta-Harness searches over executable code around a fixed base model.
> --- `ONBOARDING.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-proposer-instructions
Label: Proposer skill instruction channel

Consumer: Claude Code proposer and, for terminal, its requested analysis/implementation children. Channel: wrapper loads canonical skill file text, prepends `Follow these skill instructions:` and appends it as system prompt. Force: natural-language policy interpreted by the model; tool availability is a separate CLI configuration. Horizon: current proposer session, with candidate code/reports capable of reaching later rounds. Classification forbids delegation in text despite Agent grant; terminal deliberately requests two child roles. Neither compliance nor isolation follows from injection. SRC-1, `reference_examples/text_classification/claude_wrapper.py`, `reference_examples/text_classification/meta_harness.py`, `reference_examples/text_classification/.claude/skills/meta-harness/SKILL.md`, `reference_examples/terminal_bench_2/.claude/skills/meta-harness-terminal-bench-2/SKILL.md`.

> prefix = f"Follow these skill instructions:\n\n{skill_text}\n\n"
> --- `reference_examples/text_classification/claude_wrapper.py`

> "--dangerously-skip-permissions",
> --- `reference_examples/text_classification/claude_wrapper.py`

#### RT-BAP-candidate-execution
Label: Admitted candidate code authority

Consumer: classification inner-loop loader, terminal Harbor import path, or pilot child Harbor. Channel: imported Python module/class and optional prompt-template reads. Force: executable rules can change solver prompts, tool schemas, observation processing and environment actions subject to host privileges; not just advisory prose. Horizon: one evaluation and later evaluations that reuse that candidate. Admission is heterogeneous: reference import checks can execute code before trial, pilot stages source without importing in controller but child Harbor does import it. Selection of a frontier is not required before the candidate first gains execution authority. SRC-1, `reference_examples/text_classification/inner_loop.py`, `reference_examples/terminal_bench_2/meta_harness.py`, `experimental/harbor_meta_harness/controller.py`.

> module = importlib.import_module(module_name)
> --- `reference_examples/terminal_bench_2/meta_harness.py`

> (candidate_dir / "candidate.py").write_text(source)
> --- `experimental/harbor_meta_harness/controller.py`

## Annotations

none
