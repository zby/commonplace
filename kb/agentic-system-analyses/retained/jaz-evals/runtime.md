---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "jaz-evals runtime baseline: configured evaluation, agent adapters, improvement admission and control limits at the frozen parent revision."
run-id: AAS-2026-10-15-jaz-evals-17ab95f93794-01
reviewed-boundary: "2ffe7b5e6792a76fccb26f9ce188c88fb95ffa72"
---

# jaz-evals runtime report

## Runtime account

### What the package executes

jaz-evals is an evaluation workflow around external agent runtimes, not the implementation of JAZ. Its consequential work is to select an environment/method pair, let a model-driven method act on benchmark state, grade completed work, preserve attempt evidence, and aggregate results. Some methods also change guidance supplied to later solver sessions. The frozen parent code exposes those seams; it does not expose the complete benchmark, provider or agent-runtime implementation. No target code was executed for this report. Implementation wiring below is not evidence of activation, historical performance or improvement (SRC-1, `pyproject.toml`, `src/jaz_evals/eval_harness.py`; [boundary](boundary.md#boundary-and-evidence)).

The ordinary shipped entry is `jaz-evals <config>`. The CLI loads YAML, creates a timestamped run identity, calls `run_evaluation`, prints score/cost and returns failure when an attempt has an error. Configuration has a validated envelope but method/environment-specific mappings are interpreted by their constructors. Relative prompt paths resolve against the configuration's directory. These are operator-selected experiments, not open-ended problem discovery (SRC-1, `src/jaz_evals/cli.py`, `src/jaz_evals/config.py`). See [RT-RTE-evaluation-attempt](#rt-rte-evaluation-attempt).

For a concrete ordinary path, `configs/appworld_jaz.yaml` selects the AppWorld task queue, seed 42, the TTSI prompt, a dated nano solver and a different dated root model. `run_attempt` creates an isolation identity and artifact directory, builds both adapters, sets up the environment, and gives the harness an `AgentEnv`, not the grader. `JazHarness` scopes shared tools across the invocation tree and supplies queue tools to the root invocation only. The root model owns task sequencing, delegation and proposed prompt/tool edits. It invokes the external JAZ runtime, which owns the next model/code step. The environment owns task opening, submission, grading and queue advancement. These ownership boundaries differ from a per-task driver, where Python owns sequencing (SRC-1, `configs/appworld_jaz.yaml`, `src/jaz_evals/eval_harness.py`, `src/jaz_evals/harnesses/jaz_harness.py`, `src/jaz_evals/envs/appworld.py`; [RT-RTE-jaz-queue](#rt-rte-jaz-queue), [RT-RTE-fresh-session](#rt-rte-fresh-session)).

In AppWorld, `get_next_task` opens a fresh external world and returns supervisor identity plus task text. `apis` dispatches host calls through the current world's namespace and `world.execute`; it is not merely a provider-native tool schema. The root's `complete_task(answer)` submits, evaluates, streams the result, closes the world and advances. Its returned dict includes assertion results and may include expected versus actual values; task IDs and indices stay in the retained row but are removed from the agent's copy. The top-level grade scores completed successes against the entire selected queue. The returned Python value from the root agent is not itself the evaluation's score. Terminal outputs are `RunReport`, attempt `results.json`, optional `analysis.json`, traces, and run-level aggregates (SRC-1, `src/jaz_evals/envs/appworld.py`, `src/jaz_evals/eval_harness.py`).

The comparable StuLife path has a different feedback contract: `complete_task` stores correctness, score and reason in its internal/streamed record but returns only queue progress and next-step text. Its tool-use guard rejects unacted action tasks in agent-driven mode; driver mode instead records zero so a dead solver cannot stall the queue. Thus the same adapter label does not imply the same answer oracle. ACE's feedback renderer cannot restore fields the environment omitted (SRC-1, `src/jaz_evals/envs/stulife.py`, `src/jaz_evals/harnesses/ace.py`; [RT-RTE-ace-adaptation](#rt-rte-ace-adaptation)).

### Material alternate routes and forcing cases

The report inspected four forcing cases rather than treating the default JAZ path as universal:

1. **Direct model calls outside agent hooks.** ACE invokes the same public LLM backend directly for reflector, curator and optional merge calls. Session `BudgetPool` hooks neither meter nor cap these calls; a separate ledger adds them to reported usage. This falsifies an evaluation-wide interpretation of the configured session cost budget (SRC-1, `src/jaz_evals/harnesses/ace.py`; [RT-RTE-ace-adaptation](#rt-rte-ace-adaptation)).
2. **Host object access versus the agent sandbox.** AppWorld's API tree hides ordinary internals and blocks submission on the agent-facing tree, but explicit dunder traversal and runtime sandbox behavior remain external responsibilities. `AgentEnv` is weaker than its docstring suggests: it stores `_env` as an ordinary attribute and only defines `__getattr__`, so a holder can read that existing attribute without triggering its missing-name guard. Shipped model bindings use extracted tools rather than the whole view. The private submitting tree deliberately bypasses the agent-facing submission and budget-reserve checks. These are scoped adapter controls, not proof of a hostile-code security boundary (SRC-1, `src/jaz_evals/env.py`, `src/jaz_evals/envs/appworld.py`; [RT-CLM-tool-boundary](#rt-clm-tool-boundary)).
3. **Remote execution after a client timeout.** Letta's server may still perform tool calls after the client abandons a response. The adapter settles server step records and serializes environment calls under a lock; that lock prevents simultaneous entry, not an atomic whole delivery transaction. The shared-tools bridge binds an unauthenticated host port. A per-attempt container name does not authenticate callers or isolate the host-side benchmark from reachable clients (SRC-1, `src/jaz_evals/harnesses/letta_harness.py`; [RT-RTE-letta-bridge](#rt-rte-letta-bridge)).
4. **Delegation and bypass of the central runner.** smolagents gives child agents bounded return rejection while the root remains unbounded; its context cue requests handoff rather than enforcing it. Separately, the official-AppWorld shell script launches the external native agent without `run_evaluation`. Neither path inherits JAZ's exact hook/return/provenance guarantees (SRC-1, `src/jaz_evals/harnesses/smolagents_harness.py`, `scripts/run_appworld_official_react.sh`; [RT-RTE-smolagents-chain](#rt-rte-smolagents-chain), [RT-RTE-official-baseline](#rt-rte-official-baseline)).

Direct provider-native tools, arbitrary shell access inside excluded runtimes, their extension loading and durable/resume semantics are not established by the inspected adapters. There is no universal permission/approval layer inferred from the presence of a tool wrapper. Capability surfaces include configured JAZ hooks/REPL components, callable host tools, Letta's generated remote tools and optional base tools, and smolagents' local executor plus managed children. Current grants depend on the selected configuration and environment; `appworld_jaz.yaml` restricts imports and disables raises and timeout pragmas, but those are requests to the external JAZ implementation, not a verified deployment envelope (SRC-1, `configs/appworld_jaz.yaml`, `src/jaz_evals/harnesses/jaz_harness.py`, `src/jaz_evals/harnesses/letta_harness.py`, `src/jaz_evals/harnesses/smolagents_harness.py`).

### Guarantees and their actual owners

| Guarantee | Owner and enforcement | Strength and coverage | Alternate path / external contract | Conclusion statuses |
| --- | --- | --- | --- | --- |
| A named central run cannot silently reuse its directory | `run_evaluation`, atomic `mkdir(exist_ok=False)` | invariant for that entry path | Direct `run_attempt` does not claim the directory or write run provenance; official driver has its own names | implementation: wired; operation: uninspected |
| Harness errors retain partial scores | `run_attempt` catches setup/run failures, closes harness, calls grade | protocol, conditional on construction/cleanup/grading completing | KeyboardInterrupt propagates; construction, close, grade and hard process failure can prevent a record | implementation: wired; operation: uninspected |
| Normal JAZ return is rejected when Env reports incomplete | harness installs `ValidateReturn` over `env.is_complete()` | protocol for selected root/tree return channel; effective on StuLife's override | AppWorld inherits the base `True` result, so its queue is not protected by this guard; limits/errors also end runs; external JAZ must dispatch hooks | implementation: wired; operation: uninspected |
| Driver-owned tools do not propagate to ordinary solver children | `AgentEnv` partition plus adapter-specific binding | protocol, not hostile-code isolation | AppWorld marks all queue tools root-only; StuLife varies by delivery/per-task mode; opaque executor introspection is not covered | implementation: wired; operation: uninspected |
| Attempt identities scope state | fresh random `Isolation.key`; consumers derive names/cache keys | best effort at adapter seams | No OS/process separation between central thread workers; weights may be shared; Letta bridge remains reachable | implementation: wired; operation: uninspected |

Evidence and minimum passages for these conclusions are retained in [RT-RTE-evaluation-attempt](#rt-rte-evaluation-attempt), [RT-RTE-jaz-queue](#rt-rte-jaz-queue), [RT-CLM-tool-boundary](#rt-clm-tool-boundary) and [RT-RTE-letta-bridge](#rt-rte-letta-bridge). In particular, source comments report concurrency failures and historical guard behavior, but this evidence set has no observed run confirming those reports. AppWorld's environment declaration forces sequential attempts because of dependency-global state; other environments can use thread workers. Sequential selection is a recovery recommendation in the source, not an experimentally confirmed repair here (SRC-1, `src/jaz_evals/eval_harness.py`, `src/jaz_evals/cli.py`).

### Change admission and context control

There are two distinct improvement planes. The JAZ TTSI prompt asks the root model to inspect solver histories, propose general prompt/helper changes, test on later batches and discard ineffective changes. The shipped adapter affords passing those changes through invocation inputs; it does not independently approve each edit or verify the prompt's experimental discipline. ACE implements a code-owned adaptation cycle: task completion feeds diagnostics, models propose additions, parsers admit structurally acceptable operations, optional dedup revises redundancy, and the next task receives the resulting playbook. No per-content human veto is wired in either inspected loop. Starting an evaluation or choosing a seed is not per-update approval. Neither route establishes successful learning or exercised self-improvement without runs (SRC-1, `prompts/ttsi/jaz.md`, `src/jaz_evals/harnesses/jaz_harness.py`, `src/jaz_evals/harnesses/ace.py`, `src/jaz_evals/harnesses/ace_playbook.py`).

Context isolation is also method-specific. Per-task JAZ discards the session frame and recreates hooks; only its answer crosses back to the driver, while external benchmark state may persist according to the environment. ACE recreates the solver session but explicitly supplies changed playbook text. Its diagnostics keep the first 400,000 trajectory characters and drop the tail, with shorter task excerpts for reflector and curator. smolagents appends a threshold-triggered handoff cue to observations; it does not forcibly evict or compact the current history. The optional CodeAct hook removes history/string *bindings* and their naming guidance while preserving textual task inputs in messages. Letta compaction/search behavior is chiefly in excluded dependencies, even though this adapter records diagnostics and prices compaction and embedding spend. A stack-frame analogy fits fresh solver sessions and return values; it breaks where ambient tools access a live shared world and changed text is supplied by value to later sessions (SRC-1, `src/jaz_evals/harnesses/jaz_per_task.py`, `src/jaz_evals/harnesses/ace.py`, `src/jaz_evals/harnesses/smolagents_harness.py`, `src/jaz_evals/hooks.py`, `src/jaz_evals/harnesses/letta_harness.py`).

Code-level capability changes instead require modifying imported adapters/registered classes or configured runtime components. The registry rejects conflicting names and unsafe name shapes; the JAZ hook builder resolves exported local hooks before external `jaz.hooks`. These are configuration/import admission seams, not evidence of an agent installing product patches. The official script writes external Jsonnet configurations as launch preparation. No live product-code self-modification is established (SRC-1, `src/jaz_evals/registry.py`, `src/jaz_evals/harnesses/jaz_harness.py`, `scripts/run_appworld_official_react.sh`).

### Added source coverage and limits

All additional inspection uses SRC-1 at the frozen parent commit and supplies implementation or doctrine/design evidence, never an observed-run layer. Beyond the boundary's initial reads, this report inspected CLI/configuration and registry logic; central attempt/concurrency handling; `isolation.py`; `env.py` tool partition, wrappers and `AgentEnv`; JAZ invocation/hook/component construction and return guard; per-task session lifecycle; ACE prompts, adaptation, truncation, feedback and accounting; playbook format/sections; encoder construction in `ace_dedup.py`; Letta bridge, registration and run/settlement loop; smolagents return guards, context callback and chain/run construction; CodeAct callback implementation; AppWorld API proxy and queue/grading; StuLife completion and tool-scope branches; and the full official-baseline shell driver. Relevant anchors are the full paths in the records below. Remaining uninspected helper branches, container patches, analysis/plot/release implementations and excluded dependencies prevent an exhaustive control audit or historical result reconstruction. Readable but uninspected material is not an evidenced absence.

## Shared records

### Components

#### RT-CMP-lite-llm
Label: JAZ LiteLLM model backend

Source-native identity: `jaz.llm.LiteLLM`, constructed by `build_config_override` and independently by ACE's reflector factory. Representational form: distributed-parametric remote models; local Python clients/configuration are symbolic adapters, not the model weights. Storage substrate: provider-hosted parameters, unavailable here. No parameter-update operation is wired in these inspected callers. Exact version: the selected AppWorld JAZ arm names dated solver/root model IDs, but the general adapter accepts arbitrary model strings and ACE has a separate reflector selector. Mutable endpoint resolution: provider-side replacement behind any identifier remains uninspected; dated names are not inspectable weight digests. SRC-1, `configs/appworld_jaz.yaml`, `src/jaz_evals/harnesses/jaz_harness.py`, `src/jaz_evals/harnesses/ace.py`.

> response = client.complete_with_retry(
>     self._reflector_model, [{"role": "user", "content": prompt}], **kwargs
> )
> --- `src/jaz_evals/harnesses/ace.py`

#### RT-CMP-lite-llm-model
Label: smolagents LiteLLMModel

Source-native identity: `smolagents.LiteLLMModel`, wrapped per agent by `_MeteredModel` but backed by one constructed model object. Representational form: distributed-parametric provider model; symbolic metering wrapper. Storage substrate: remote parameters and local accounting state. Parameter changes during operation: none implemented by the inspected adapter. Exact model pin: caller-supplied `model_id`, not enforced as a dated snapshot by construction. Mutable endpoint resolution: possible through supplied aliases; provider internals and weight identity uninspected. The smolagents package itself is pinned to 1.26.0, which does not pin model weights (SRC-1, `src/jaz_evals/harnesses/smolagents_harness.py`, `pyproject.toml`).

> model = smolagents.LiteLLMModel(**model_cfg)
> --- `src/jaz_evals/harnesses/smolagents_harness.py`

#### RT-CMP-letta-model
Label: Letta agent model

Source-native identity: `model=self.model` in Letta agent creation, with OpenAI provider settings. Representational form: distributed-parametric remote model. Storage substrate: provider-hosted parameters, with agent state in the external server. Parameter changes during operation: no training path in the inspected client adapter. Exact version: configuration supplies a model identifier, not a verified weight revision. Mutable endpoint resolution: unresolved for the selected provider endpoint; the adapter cannot establish immutability. Compaction and embedding model identities may differ from the agent model and are priced from instrumentation; their operational selection and weights remain external. SRC-1, `src/jaz_evals/harnesses/letta_harness.py`.

> model=self.model,
> agent_type=self.agent_type,
> tool_ids=tool_ids,
> --- `src/jaz_evals/harnesses/letta_harness.py`

#### RT-CMP-sentence-transformer
Label: ACE SentenceTransformer encoder

Source-native identity: `SentenceTransformer`, default model name `all-mpnet-base-v2`. Representational form: distributed-parametric encoder and dense output vectors. Storage substrate: locally loaded CPU weights, cached by model-name key in process memory. Parameters change during operation: no update path in the inspected dedup constructor; it calls `encode`. Exact version: model name only, no revision supplied to construction. Mutable endpoint resolution: a later cold load can resolve the model name differently; cached instance reuse does not pin future downloads. SRC-1, `src/jaz_evals/harnesses/ace_dedup.py`.

> encoder = _ENCODERS[embedding_model] = SentenceTransformer(embedding_model, device="cpu")
> --- `src/jaz_evals/harnesses/ace_dedup.py`

### Operative objects

#### RT-OBJ-agent-env
Label: AgentEnv tool view

Source-native identity: `AgentEnv`, created around each attempt's `Env`. Representational form: symbolic Python object, tool-name snapshot and callable bindings; its instruction strings are separately interpreted natural-language content. Storage substrate: in-process references/closures. The public interface exposes instructions and selected tools while grading remains on the underlying environment. However, `_env` is a real readable attribute: `__getattr__` guards missing names, not existing private attributes. This prevents interpreting the view as enforcing grader secrecy for arbitrary holders. Shipped harnesses extract tool bindings instead of handing this whole object to the model. Root/shared partitioning is adapter-mediated; introspection security is not supplied by the view (SRC-1, `src/jaz_evals/env.py`, `src/jaz_evals/eval_harness.py`).

> This is a guard against reaching into internals by ordinary attribute access -- which is how it
> would happen in practice -- not a security boundary.
> --- `src/jaz_evals/env.py`

### Routes

#### RT-RTE-evaluation-attempt
Label: Central evaluation attempt

Endpoints/progression: operator CLI → YAML/config → registered environment and harness → setup → agent run → grade/analysis → attempt and aggregate files. Owner: CLI and central Python runner; model owns steps only inside the harness. Identities: run ID, ordered attempt index and fresh random isolation key. State/effects: benchmark mutations plus filesystem artifacts. Config and prompt selection are caller contributions, not model-selected experiment scope (SRC-1, `src/jaz_evals/cli.py`, `src/jaz_evals/config.py`, `src/jaz_evals/eval_harness.py`, `src/jaz_evals/isolation.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: AttemptRecord list to CLI; RunReport from the method is paired with an environment Grade.
- Later read-back: retained result/analysis/trace files can feed shipped analysis and log-viewer entry points; the central loop itself does not reload a previous attempt's context.
- Delegated visibility: harness gets AgentEnv; grader retains the underlying Env. Attempts can run in threads, not separate processes.
- Selection predicate: configuration names choose registered classes; attempt count and worker bound choose scheduling; environment concurrency declaration can force sequential execution.
- Invalidation or expiry: fresh isolation key per attempt; duplicate central run directory rejected; process death can leave partial files without aggregate.
- Activation or effect: implementation calls setup/run/grade and writes records; actual completion or artifact production is unobserved.
- Evidence limits: construction and cleanup/grade failures can escape; interrupts propagate. External dependency and provider behavior is unavailable.

Guarantee owner: central runner. Enforcement point: directory claim and nested try/finally. Guarantee strength: protocol for failure recording, invariant for exclusive directory creation; not a guarantee that every failure leaves results. Required external contract: cleanup and grading must return, and the process must survive. No decision about content revision is made here; grading oracle is environment-specific.

> directory.mkdir(parents=True, exist_ok=False)
> --- `src/jaz_evals/eval_harness.py`

> report = harness.run_task(AgentEnv(env))
> --- `src/jaz_evals/eval_harness.py`

> grade = env.grade()
> analysis = _write_analysis(env, artifacts)
> --- `src/jaz_evals/eval_harness.py`

#### RT-RTE-jaz-queue
Label: JAZ whole-queue and TTSI delegation

Endpoints/progression: configured instructions/guidance/tools → root `jaz.invoke` → model-directed code/delegation → host benchmark tools → completion feedback → later task/batch. Owner: root model for queue policy and change proposals; external JAZ for execution/hook dispatch; Env for task state and grading. Configuration can supply tree-wide settings/hooks and root-only overrides/hooks. AppWorld's selected arm uses a strong root and nano delegates with recursion, iteration and session-budget hooks (SRC-1, `src/jaz_evals/harnesses/jaz_harness.py`, `configs/appworld_jaz.yaml`, `prompts/ttsi/jaz.md`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: delegated values go to the root; top-level completion becomes a usage/status RunReport rather than a scored answer.
- Later read-back: TTSI guidance requests revised prompt/helper objects be supplied to subsequent solver invocations across tasks in the attempt; actual authored revisions and reuse are unobserved.
- Delegated visibility: shared tools propagate by `jaz.scope`; root tools and root guidance/overrides are local unless the configured guidance scope is tree. Single-task instructions require explicit root forwarding.
- Selection predicate: root model chooses next batch, delegates and changes; root/tree settings select return-guard reach.
- Invalidation or expiry: prompt asks removal of ineffective tools/changes; external invoke lifetimes bound session frames. No independent edit rollback gate is implemented by the adapter.
- Activation or effect: calls into the JAZ runtime are wired; compliance with batch optimization and causal effects of changed guidance are unobserved.
- Evidence limits: external runtime dispatch/isolation is not inspected. Prompt mandates are policy, not enforced admission criteria.

Guarantee owner: harness installs external ValidateReturn. Enforcement point: return validator reads `env.is_complete()`, root by default or tree-wide when configured. Guarantee strength: protocol, not correctness invariant. Covered path: normal guarded returns when the environment reports incomplete. Crucial forcing case: the base Env returns True and AppWorldEnv does not override it; therefore this guard does not stop early return from the selected AppWorld queue. StuLifeEnv explicitly overrides it. This finding follows inspection/search of `is_complete` in SRC-1, `src/jaz_evals/env.py`, `src/jaz_evals/envs/appworld.py` and `src/jaz_evals/envs/stulife.py` at the frozen revision. Alternate paths: limits/exceptions terminate anyway; bounded delegates may return before the entire queue ends. Required external contract: JAZ applies scoped/local hooks as requested.

> # that overrides it today, so it is the only env the guard bites.
> return True
> --- `src/jaz_evals/env.py`

Admission: trigger is completed solver batches; proposed changes are prompt text and helper tools. Root model proposes, diagnoses, decides and can discard; no human per-edit approval or software success test is wired. Operating mode: finite benchmark curriculum. Answer oracle: AppWorld completion reports can expose assertion outcomes/expected values; this does not generalize to StuLife. Recovery requested by guidance includes defensive exception handling, smaller edits and discarding unsuccessful changes. What persists by intention is changed solver guidance/helpers and histories in the root's ongoing attempt, not model weight updates.

Theory account: guidance asks general diagnoses, minimal changes and tests against subsequent tasks. It can support localized natural-language workflow accounts, but no authored candidate is supplied here. theory-builder conditions 1–4: condition 1 conclusion status: afforded (root can formulate whole prompt units); condition 2 conclusion status: uninspected (delivery does not prove semantic dependence); condition 3 conclusion status: claimed (prompt explicitly asks hypotheses, targeted criticism and rejection); condition 4 conclusion status: afforded (later batches can receive revisions). Addressability: whole prompts and callable helpers are individually editable; actual assumptions and criticisms are not observed. Persistence: requested across tasks of one run; cross-run persistence unestablished. learning: uninspected — no future-capacity or attribution evidence. Reflection: afforded self-representation through solver histories and editable guidance, but both causal directions are not observed. Reflective theory builder: uninspected. Autonomous theory builder: uninspected as a full property; proposal/evaluation roles are assigned to computation, but conditions are not established. Self-improvement: dispositional improvement-directed self-change is afforded within the root-plus-solvers boundary, with task success as the independent objective; no exercised claim because evidence shaping a particular update, live installation and later causal dependence are unobserved.

> jaz.invoke(*self._root_overrides(), *self._build_root_hooks(), *root_guard, **inputs)
> --- `src/jaz_evals/harnesses/jaz_harness.py`

> return ValidateReturn(lambda ret: _reject_early_return(env, ret), max_failures=None)
> --- `src/jaz_evals/harnesses/jaz_harness.py`

> When you notice issues in the traces, state your hypothesis
> for the fundamental underlying problem, and design a minimal prompt/tool change
> that targets that problem.
> --- `prompts/ttsi/jaz.md`

#### RT-RTE-fresh-session
Label: JAZ per-task driver

Endpoints/progression: Python queue loop fetches task → fresh invoke with fresh hooks → answer or exception → complete task → next session. Owner: driver, not a meta-model. It supplies single-task instructions and shared tools; queue tools are withheld according to Env partitioning. Mutable world state remains environment-owned (SRC-1, `src/jaz_evals/harnesses/jaz_per_task.py`, `src/jaz_evals/envs/stulife.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: session answer to driver, submitted only when the completion signature accepts an answer.
- Later read-back: no driver-accumulated solver guidance is reloaded in this method; environment-retained state is separate from fresh invocation history.
- Delegated visibility: session sees shared tools, not driver-only queue tools; per-task hooks cover the session subtree.
- Selection predicate: Python `while env.tasks_remaining()` and ordered fetch; each session solves the supplied task.
- Invalidation or expiry: fresh hooks/session context per task; exceptions produce per-task traceback and the driver still completes that task.
- Activation or effect: driver invokes and submits; actual model actions remain unobserved.
- Evidence limits: withholding relies on Env's correct root-only declaration; hook construction failure and queue failure differ from absorbed session failure.

Guarantee owner: per-task adapter. Enforcement point: hook construction and session exception boundary. Guarantee strength: protocol for continuing after ordinary session exceptions, not all BaseExceptions or queue failures. No improvement admission mechanism is implemented by this loop.

> answer = jaz.invoke(**self._inputs(env, task))
> --- `src/jaz_evals/harnesses/jaz_per_task.py`

#### RT-RTE-ace-adaptation
Label: ACE task-to-playbook adaptation

Endpoints/progression: current playbook → fresh solver → complete task → trajectory/report → reflector → curator → JSON validation/additions → optional embedding/merge dedup → playbook snapshot → next solver. Owner: Python driver controls ordering and freeze threshold; models diagnose/propose; software admits structurally valid additions. It uses [RT-CMP-lite-llm](#rt-cmp-lite-llm) and optional [RT-CMP-sentence-transformer](#rt-cmp-sentence-transformer). SRC-1, `src/jaz_evals/harnesses/ace.py`, `src/jaz_evals/harnesses/ace_playbook.py`, `src/jaz_evals/harnesses/ace_dedup.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: updated playbook/next ID to queue loop; session answers and failures are graded before adaptation.
- Later read-back: count-stripped changed playbook is rendered into each subsequent solver prompt and later adaptation prompts; per-task and final snapshots are written.
- Delegated visibility: solvers get shared tools; reflector gets task prefix, head-truncated trajectory, feedback and interface/instruction excerpt; curator gets a shorter task prefix, reflection, trajectory and playbook.
- Selection predicate: adapt while freeze_after is unset or task index is below it; optional dedup selects similarity groups using encoder vectors/threshold, not a task-success oracle.
- Invalidation or expiry: invalid curator JSON/operations retain the prior playbook; adaptation exception retains last good state and records failure; configured freeze stops later changes.
- Activation or effect: accepted text reaches later model input by construction; semantic adoption or improved task solving is not observed.
- Evidence limits: no independent quality gate on the added advice; truncated trajectories can omit later events. Session BudgetPool excludes direct adaptation calls, although total usage includes their ledger.

Admission trigger: each completed task while adaptation is enabled. Proposed change: ADD advice bullets and optional merge replacement. Computational contributions: reflector diagnosis, curator proposal, parser validation, software application and optional model merge. Human contribution: initial configuration/seed selection; no per-bullet approval or veto. Rejection ability: structural parse/validation failures and operational exceptions; no demonstrated semantic rejection of bad advice. Recovery: retain previous playbook on those failures, log error and continue. Guidance: explicit reflector root-cause instructions and curator request for missing generalizable advice; persisted output is playbook content, while raw calls are retained separately. Operating mode: bounded task curriculum with optional frozen phase.

Answer oracle: `_feedback` uses only the returned completion mapping, omitting success after rendering it in prose, and dropping next_step/tasks_remaining/api_executions. AppWorld supplies pass/fail details; StuLife's completion supplies no correctness fields, so the result can be `(no evaluation feedback available)`. The reflector's reference-code slot is explicitly not applicable; model judgment is not an oracle.

Theory account: sections can hold strategies, workflow rules, mistakes and corrections. The prompts request diagnosis of errors and new advice; structural admission alone does not establish formulated content-directed criticism. theory-builder conditions 1–4: condition 1 conclusion status: afforded (whole advice bullets); condition 2 conclusion status: uninspected (solver dependence on advice unobserved); condition 3 conclusion status: claimed (root-cause/strategy criticism requested, no generated case supplied); condition 4 conclusion status: wired (admitted results reach the next adaptation/solver round). Addressability: bullet IDs and fixed sections expose local advice units; finer assumption structure depends on generated content. Persistence: wired across tasks within the run, plus optional seed-file loading on another run. learning: uninspected — changed context and persistence alone do not demonstrate improved future capacity. Reflection: diagnostic representation of the method's own solver trajectories and guidance-mediated later action is afforded; actual content fidelity and behavioral causation are unobserved. Reflective theory builder: uninspected. Autonomous theory builder: uninspected as a full property, despite computational proposal/admission roles. Self-improvement: dispositional trace-responsive change to later solver guidance is wired within the ACE workflow boundary; exercised attribution is prevented by missing particular update and subsequent dependence evidence, especially causal link 4. Success is separately unestablished.

> playbook, next_id = apply_add_operations(playbook, operations, next_id)
> if deduplicate is not None:
>     playbook = deduplicate(playbook, index)
> return playbook, next_id
> --- `src/jaz_evals/harnesses/ace.py`

> prompt = _render(_SUBAGENT_PROMPT, instructions=instructions, playbook=strip_counts(playbook))
> --- `src/jaz_evals/harnesses/ace.py`

> return "\n".join(lines) if lines else "(no evaluation feedback available)"
> --- `src/jaz_evals/harnesses/ace.py`

> # "Outside any agent loop" is also the budget caveat, and it is a big one: this is a direct
> # backend call, so it passes through no hook dispatcher and `BudgetPool` -- which books cost
> # off `LLMQueryExit` inside an invoke -- neither counts nor caps it.
> --- `src/jaz_evals/harnesses/ace.py`

#### RT-RTE-letta-bridge
Label: Letta remote-agent loop and host tool bridge

Endpoints/progression: adapter → per-attempt server container/client → registered generated tool source → unauthenticated host HTTP bridge → shared Env tool → result/error → remote agent. Driver sends kickoff/continue or delivered task messages, settles server step usage and tests completion/cost/round limits. Owner: external agent owns steps; Python driver owns messages, registration and lifecycle; Env owns benchmark order. SRC-1, `src/jaz_evals/harnesses/letta_harness.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: bridge returns JSON result or 422 error; method returns status and usage after settlement/diagnostic drain.
- Later read-back: remote agent memory blocks/history and optional base tools can carry context within the attempt; full persistence/compaction/search semantics remain uninspected external behavior. Host writes messages/rounds/usage logs for inspection.
- Delegated visibility: only shared tools are served/registered; driver-owned delivery callable stays in-process. Generated source serializes arguments and JSON response, so Python object identity is not preserved across this channel.
- Selection predicate: configured delivery tool must match the environment's declared tool; otherwise kickoff/continue messages; stop on complete, maximum rounds, priced settled agent cost or persistent no-step client failure.
- Invalidation or expiry: container teardown destroys ephemeral server DB after diagnostics drain; a timeout need not stop server work; lock serializes host/driver environment calls.
- Activation or effect: host bridge dispatch is wired and can mutate benchmark state; actual remote calls and memory activation are unobserved.
- Evidence limits: default bridge binds 0.0.0.0 without authentication; lock does not make delivery atomic. The loop's cost check prices settled agent steps, whereas final accounting separately adds compaction and embedding spend.

Guarantee owner: adapter for locking/withholding, Env for legal task order. Enforcement points: bridge tool dictionary, shared lock and delivery-name checks. Guarantee strength: protocol, not a deployment guarantee. Required external contract: reachable bridge/network must be trusted or isolated; server steps and patches must provide expected records. Agent tool registration failure can degrade to a subset; zero registered tools aborts. Approval: no per-tool-call human gate is wired. Models choose tool calls within the remote agent's external policy; include_base_tools is enabled for letta_v1_agent, so the bridge dictionary is not the entire remote capability surface.

> bridge = LettaToolServer(env.shared_tool_bindings(), known_tool_names=env.tool_bindings())
> --- `src/jaz_evals/harnesses/letta_harness.py`

> self._server = _ToolHTTPServer((self._host, 0), _ToolHandler)
> --- `src/jaz_evals/harnesses/letta_harness.py`

> host: str = "0.0.0.0",
> --- `src/jaz_evals/harnesses/letta_harness.py`

#### RT-RTE-smolagents-chain
Label: smolagents managed-agent continuation chain

Endpoints/progression: adapter builds eager depth-bounded CodeAgent chain → manager run → local code/tool calls or managed child → answer/error back to parent → terminal state/usage. Owner: model chooses steps and handoff; code selects chain topology, metering and callbacks. All levels share benchmark tool objects and accounting state, but have separate agent contexts. SRC-1, `src/jaz_evals/harnesses/smolagents_harness.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: child results return through managed-agent tool calls; root terminal result state determines completed versus step-budget status.
- Later read-back: handoff guidance can request history copied into the child's task; exact selected retained content and its use remain model/runtime-dependent, not enforced by the callback.
- Delegated visibility: each chain level receives tools and a child except at maximum depth; domain guidance initially reaches root task text only. Authorized imports and execution timeout are configured on each executor.
- Selection predicate: model chooses delegation; callback appends a cue when reported input tokens meet warning fraction and a child exists.
- Invalidation or expiry: manager starts with reset=True; child-context reset semantics are supplied by external smolagents. Return-rejection counters reset when the observed steps-list object changes.
- Activation or effect: context warning is appended to observations, not a forced handoff or trim; return checks and shared metering are wired.
- Evidence limits: dependency code is unavailable; no observed handoff/compliance. Root return guard cannot enforce correctness and child guard deliberately relents after its configured rejection budget.

Guarantee owner: harness installs checks per agent and a metered model per depth. Enforcement points: final_answer_checks, callback, metered backend. Guarantee strength: protocol. Normal root returns are checked against Env completion; child returns can be allowed while incomplete, restoring parent control. Cost/step stops and agent-authored BaseExceptions still end the run and are recorded. External contract: CodeAgent invokes configured checks/callbacks and routes model calls through the wrapper. No independent human approval or improvement admission occurs on this route. Environment completion can be achieved by low-quality submissions; it is not an answer oracle.

> if max_rejections is not None and rejections >= max_rejections:
>     # Bound reached: let this agent return so its parent regains control.
>     return True
> --- `src/jaz_evals/harnesses/smolagents_harness.py`

> memory_step.observations = f"{existing}\n\n{warning}" if existing else warning
> --- `src/jaz_evals/harnesses/smolagents_harness.py`

#### RT-RTE-codeact-filter
Label: Optional CodeAct input/history-binding filter

Endpoints/progression: invoke enter/send captures string names → first LLM-query hook rewrites naming/history sections → iteration-zero REPL hook drops bindings. Owner: deterministic local hook, activated only when configured. Form: symbolic message/variable transformations; natural-language task/instruction bodies are not thereby removed. SRC-1, `src/jaz_evals/hooks.py`, `src/jaz_evals/harnesses/jaz_harness.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: hook effects replace persistent messages and remove variables; next external model/REPL step consumes resulting context.
- Later read-back: inapplicable — this filter does not write a retained result for later reload; it changes current-invoke visibility.
- Delegated visibility: maps are keyed by invoke_id so nested invocations have independent edit state when the hook propagates.
- Selection predicate: string-valued input/scope names, expected prompt markers, first query and iteration zero.
- Invalidation or expiry: state removed on invoke exit; prompt-shape mismatch aborts rather than silently changing the measured method.
- Activation or effect: suppresses direct history/input-variable access and corresponding naming guidance; does not prove absence of history in ordinary messages or model reasoning.
- Evidence limits: external JAZ must implement DropMessages/AddMessages/DropVariables effects; no actual prompt diff or execution supplied.

> effects: list[Any] = [DropVariables({_REPL_HISTORY_NAME})]
> --- `src/jaz_evals/hooks.py`

#### RT-RTE-official-baseline
Label: Official AppWorld baseline shell driver

Endpoints/progression: operator parameters/environment → generated per-repetition Jsonnet → separate external appworld subprocesses → logs/output trees → wait and printed integrity diagnostics. Owner: shell script for launch and external AppWorld for agent/grader execution. Unique experiment names separate per-task database state and cache keys. The script deliberately bypasses the central runner. SRC-1, `scripts/run_appworld_official_react.sh`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: process exit status reflects failed waits; printed costs/error and credit-hit summaries supplement status.
- Later read-back: external skip_if_finished is requested in generated configuration; actual marker/resume semantics are uninspected. Logs are read for diagnostics by the script.
- Delegated visibility: subprocess receives exported environment, root and generated configuration; .env, when present, overrides previously exported settings.
- Selection predicate: requested repetition count/dataset, checkout/root overrides and available CLI; one process per repetition and sequential tasks within each.
- Invalidation or expiry: timestamp/repetition naming avoids database collisions; generated config controls cost/step limits and skip behavior in the excluded runner.
- Activation or effect: script writes configurations and launches native runs; printed zero-spend/rate-limit diagnostics do not themselves set failure.
- Evidence limits: native agent, fork patches, grader and task data are unavailable; a successful wait does not establish a valid evaluation.

Admission: software writes launch configuration from operator-selected parameters; no agent-selected product update. Model/provider, budget and prompt choices govern a bounded benchmark experiment. Answer oracle: delegated to external AppWorld evaluation. Recovery/rejection: invalid roots/keys/counts fail fast; subprocess failure sets fail, but diagnostic outage hits require operator judgment. No claim of compatibility with central-run provenance/guard coverage.

> ( cd "$APPWORLD" && "$APPWORLD_BIN" run "$EXP" --root "$APPWORLD_DATA_ROOT" --num-processes 1 --with-evaluation ) \
>     > "${LOGS}/rep${rep}.log" 2>&1 &
> --- `scripts/run_appworld_official_react.sh`

### Claims

#### RT-CLM-tool-boundary
Label: Tool wrappers are not a security boundary

Claimed operation: AgentEnv's docstring claims ordinary-access restriction, but its `_env` attribute is directly readable: construction sets it and no `__getattribute__` blocks it. The missing-attribute dispatcher is not a complete access check. Shipped adapters bind extracted tools, which limits the practical exposure; the report does not assert an exercised exploit. AppWorld's separate agent-facing tree blocks supervisor submission, validates path/argument identifiers and refuses callable-bearing results, while the private submitting tree serves the queue. Owner/enforcement: AgentEnv's missing-name dispatcher and `_APITree.__call__`; strength: protocol only for their covered paths. Runtime sandbox/provider/OS security remains external. Covered alternatives include whole-AgentEnv access and bare tool bindings, proxy path construction and host-call results; explicit dunder traversal is intentionally delegated to the sandbox. Implementation conclusion status: wired. Operation conclusion status: uninspected. This claim is not absence of all exploit paths. SRC-1, `src/jaz_evals/env.py`, `src/jaz_evals/envs/appworld.py`; see [RT-OBJ-agent-env](#rt-obj-agent-env).

> object.__setattr__(self, "_env", env)
> --- `src/jaz_evals/env.py`

> if segments == _SUBMIT_SEGMENTS:
>     raise RuntimeError(_SUBMIT_BLOCKED)
> --- `src/jaz_evals/envs/appworld.py`

> if _hands_back_a_callable(result):
>     raise RuntimeError(_CALLABLE_RESULT)
> --- `src/jaz_evals/envs/appworld.py`

#### RT-CLM-ttsi-experiment
Label: TTSI asks for evidence-responsive prompt and tool optimization

Claimed operation: solve tasks through single-call delegates, diagnose histories, optimize general prompt/tools and validate changes in later batches. The prompt gives a method and a veto instruction, not enforcement of fair experiments or benefit. Claim conclusion status: claimed. Operation conclusion status: uninspected. SRC-1, `prompts/ttsi/jaz.md`; admission and independent properties are assessed in [RT-RTE-jaz-queue](#rt-rte-jaz-queue).

> Discard the change if it did not help.
> --- `prompts/ttsi/jaz.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-domain-guidance
Label: Configured domain guidance to agent decisions

Consumer: JAZ root model, smolagents root model or Letta agent. Channel: domain prompt selected by configuration, supplied as JAZ guidance input/scope, appended to smolagents root task, or merged with Letta system text. Force: natural-language model instruction, not a parser-enforced experimental protocol. Horizon: selected invocation/attempt; further delegation depends on scope or explicit forwarding. Updating a prompt file is distinct from its later consumption. SRC-1, `src/jaz_evals/config.py`, `src/jaz_evals/harnesses/jaz_harness.py`, `src/jaz_evals/harnesses/smolagents_harness.py`, `src/jaz_evals/harnesses/letta_harness.py`.

> if self.guidance_scope == "tree" and guidance is not None:
>     scoped["guidance"] = guidance
> --- `src/jaz_evals/harnesses/jaz_harness.py`

#### RT-BAP-playbook-guidance
Label: Admitted ACE advice to subsequent solver decisions

Consumer: later fresh solver sessions and subsequent adaptation models. Channel: rendered count-stripped playbook in prompt text, after structural admission/optional dedup. Force: natural-language advice interpreted by models; admission validation determines admissible operation syntax, not truth. Horizon: remaining tasks in the attempt and optional later seed loading. Delivery is wired in [RT-RTE-ace-adaptation](#rt-rte-ace-adaptation); semantic dependence is unobserved. SRC-1, `src/jaz_evals/harnesses/ace.py`, `src/jaz_evals/harnesses/ace_playbook.py`.

> - The playbook you created will be used to help solve similar tasks.
> --- `src/jaz_evals/harnesses/ace.py`

## Annotations

none
