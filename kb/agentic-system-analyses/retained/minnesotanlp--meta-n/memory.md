---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Meta-n memory: evaluated traces and retained injection chains, selective Ω context, resume and per-task compaction."
run-id: AAS-2026-10-14-meta-n-18c23b6f8bb4-01
source-identity: "https://github.com/MinnesotaNLP/Meta-n"
reviewed-boundary: b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8
---

# Meta-n memory report

## Boundary and evidence

Meta-n retains evaluated task source and outcomes, then derives preprocessing, helpers and rationale for subsequent candidate chains. This account includes archive selection, prompt views, disk continuation, frozen winner reuse, local conversation compaction, external trace/log retention and post-run readers. Static prompts and task inputs shape these operations but are not themselves experience read-back. Provider parameters remain opaque external state, as described by [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client) and [RT-CMP-external-backend](runtime.md#rt-cmp-external-backend); this report does not infer weight updates from retained source.

All new evidence is direct implementation reading within SRC-1 at the frozen commit. Supplied runtime findings are identified separately below. HEAD was rechecked against the boundary and `git status --short` returned no tracked changes. No target execution, tests, model calls or benchmarks were performed. No execution evidence establishes compaction fidelity, actual helper adoption or improved future performance.

| Entry point or operation | Source path and inspection basis | Records or local limit |
|---|---|---|
| CLI admission, resume and seed import | Direct: `meta_n/main.py` seed loader, configuration and archive-required guard; supplied runtime CLI construction | [MEM-RTE-seed-import](#mem-rte-seed-import), [MEM-RTE-archive-resume](#mem-rte-archive-resume). Bare `--tasks` additionally requires `--use-archive`. |
| Candidate write, checkpoint and reconstruction | Direct: `meta_n/core/run_persistence.py` resume/checkpoint/candidate writer; `meta_n/core/archive.py` reconstruction and index updates; `meta_n/utils/atomic_io.py` | [MEM-OBJ-trace](#mem-obj-trace), [MEM-OBJ-checkpoint](#mem-obj-checkpoint), [MEM-RTE-archive-resume](#mem-rte-archive-resume) |
| Parent traces, inspiration, old-chain selection | Direct: `meta_n/core/omega.py` generation, formatting and structured summaries; `meta_n/utils/context_manager.py`; archive inspiration selector | [MEM-RTE-omega-context](#mem-rte-omega-context). Model-visible views are not complete archive contents. |
| Derived injection generation and repair admission | Direct Ω generation; supplied runtime gate, helper filtering, within-layer and downstream repair | [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission), [RT-RTE-within-refine](runtime.md#rt-rte-within-refine), [RT-RTE-downstream-repair](runtime.md#rt-rte-downstream-repair); annotations below |
| Native/agentic/external preprocessing and helper consumption | Direct object schema and merge code in `meta_n/core/meta_layer.py`; supplied runtime consumer wiring and external mapper | [MEM-OBJ-python-library](#mem-obj-python-library), [MEM-OBJ-bash-library](#mem-obj-bash-library), [RT-BAP-executable-injection](runtime.md#rt-bap-executable-injection). Host effects are not universally sandboxed. |
| Frozen maps, inherited traces and test read-back | Supplied frozen assembly; direct test-evaluation branches in `meta_n/core/evolutionary_orchestrator.py` | [RT-RTE-frozen-routing](runtime.md#rt-rte-frozen-routing), [MEM-RTE-test-readback](#mem-rte-test-readback) |
| Per-task context isolation and summary replacement | Direct: `meta_n/core/agentic_solver.py` budget gates and summary replacement; supplied loop frame/return account | [MEM-RTE-context-compaction](#mem-rte-context-compaction), [MEM-OBJ-prior-summary](#mem-obj-prior-summary) |
| External log copy, scratch teardown, telemetry | Direct finalization/copy-call seam in `meta_n/core/external_agents/solver.py`; supplied backend lifecycle | [RT-RTE-external-spine](runtime.md#rt-rte-external-spine). Copy implementation and every backend transcript format not inspected; prevents a guarantee of complete/reloadable conversation retention. |
| Post-run summary/code/trace consumers | Direct: `meta_n/analysis/best_of_k.py` loader and `meta_n/analysis/emergent_roles.py` injection loader. Scoped searches: `metrics.py`, `depth_attribution.py`, `injection_telemetry.py`, `telemetry.py` under `meta_n/analysis/` | [MEM-RTE-postrun-analysis](#mem-rte-postrun-analysis). Remaining analysis transformations not audited; no guarantee that all metrics preserve provenance. |
| Backend conversation caches, data/evaluator caches and cost ledgers | Supplied model/budget boundaries; scoped core and analysis searches, not full adapter/cache audit | SDK compaction/persistence and adapter cache invalidation uninspected. Prevents attributing their internal memory policies or exact resumed cost enforcement to this account. |
| Registered tools, hooks and service APIs | Supplied CLI/package and backend tool wiring; direct CLI guard; library operations traced above | Native memory routes use Python calls, not a retrieved-note tool. Backend tool grants are in [RT-RTE-external-spine](runtime.md#rt-rte-external-spine). No exhaustive hook/service absence is asserted. |

## Core ideas

1. **Retained outcomes change later proposals, not model parameters.** Archive traces supply Ω with execution source, failures and evaluator feedback. Its output becomes persistent source and rationale; candidate admission and reconstruction make that organization available for later trials. [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission) establishes the improvement-directed write capacity, not demonstrated learning.
2. **The improvement model sees less than the solver uses.** Sampling, truncated output displays and old-layer eviction change the Ω view. Those operations do not remove earlier source from a candidate's executable chain. Cross-candidate inspiration has its own selector and narrower display. [MEM-RTE-omega-context](#mem-rte-omega-context) distinguishes those consumer views.
3. **Archive authority is split.** Whole-candidate mean determines archive best, while per-task best uses success/score ranking, optional floors and adoption bars. A barred trace remains in candidate history and can coexist with a high candidate mean. There is no single universal “approved memory” bit (SRC-1, `meta_n/core/archive.py`; [MEM-OBJ-trace](#mem-obj-trace)).
4. **Resumption restores executable interventions but not all original reasoning context.** Injection JSON carries rationale and full helper/preprocessing source. Raw Ω prompt/response sidecars exist for inspection but ordinary archive reconstruction does not load them. Compacted per-task conversation is a separate invocation-local memory, not a checkpointed agent continuation ([MEM-RTE-archive-resume](#mem-rte-archive-resume), [MEM-RTE-context-compaction](#mem-rte-context-compaction)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-trace
Label: Evaluated task trace

Source-native identity: `Trace` within `Candidate.traces`. Storage substrate: mutable Pydantic objects, `archive/<candidate>/traces/<task>.json`, plus `.py`/`.sh` source copies. Representational form: symbolic script and numeric outcome/access instrumentation, with natural-language reasoning, stdout/stderr, error and evaluator displays. Raw task execution results and stamped summaries are not identical to an unabridged model/tool transcript. Lineage: native execution, agentic best attempt or external scorer/telemetry produces a trace; consolidation can inherit it without fresh solving. Consumers: Ω interprets selected display text; archive code ranks numeric outcomes; test evaluators execute stored source. The script can have executable authority; prose delivery alone establishes no model compliance. Distinct from [RT-OBJ-task-solution-map](runtime.md#rt-obj-task-solution-map): that map is assembled from trace scripts and lacks their complete outcome record. Closest route is [RT-RTE-native-solve](runtime.md#rt-rte-native-solve), not an object counterpart (SRC-1, `meta_n/core/meta_layer.py`, `meta_n/core/run_persistence.py`, `meta_n/core/archive.py`).

> with open(traces_dir / f"{trace.task_id}.json", "w") as f:
>     json.dump(trace.model_dump(), f, indent=2)
> --- `meta_n/core/run_persistence.py`

> if cur_key is None or (bool(trace.success), trace.score) > cur_key:
>     self._best_per_task[trace.task_id] = (
>         trace.score,
>         candidate.candidate_id,
>         trace,
>     )
> --- `meta_n/core/archive.py`

Bars alter index promotion, not history retention. Helper instrumentation distinguishes `None` (unmeasurable) from an empty measured call list; neither source availability nor a positive score proves executed helper use. Source and finalization details are in SRC-1, `meta_n/core/meta_layer.py` and [RT-RTE-helper-verification](runtime.md#rt-rte-helper-verification).

#### MEM-OBJ-python-library
Label: Python helper library part

Part of: [RT-OBJ-code-library](runtime.md#rt-obj-code-library)

Source-native identity: `InjectedCode.code_library`. Symbolic Python name/source mapping; storage in live injection objects, injection JSON and helper sidecars, with native prepend or external staged files as consumer copies. Lineage: parsed Ω output, imported seed or repaired injection. Same-name later entries override earlier ones. Optional value verification can filter these helpers and stamp `sandbox_verified_names` when `passed` and `ran_in_sandbox` are both true. This retained metadata is not independently proven helper execution or value verification: the sandbox bit is derived from returned status, and the predicate trusts the last stdout JSON object without first rejecting a nonzero process return code. Any passing value assessment is conditional on trustworthy runner measurements and the evaluator contract. Stub-kept helpers and restored dependencies do not acquire that stamp merely by being retained. Native executors consume source when invoked; the model receives descriptions as guidance. Foster-adoption and deployment fallback are separate authority channels. This part is distinct from bash because the Python value gate and dependency closure do not cover bash (SRC-1, `meta_n/core/meta_layer.py`; [RT-RTE-helper-verification](runtime.md#rt-rte-helper-verification)).

> merged_py.update(ic.code_library)
> merged_bash.update(ic.code_library_bash)
> --- `meta_n/core/meta_layer.py`

The retained stamp feeds override-aware non-adoption bars at the per-task-best consumer, not an authenticated proof channel. Same-name unverified overrides clear prior stamped status in the live merged view; persistence/reconstruction preserves metadata without renewing its warrant (SRC-1, `meta_n/core/verified_code.py`, `meta_n/core/evolutionary_orchestrator.py`; [RT-RTE-helper-verification](runtime.md#rt-rte-helper-verification)).

> ran_in_sandbox = result.get("status") != "exec_error"
> passed = bool(self.success_predicate(result))
> --- `meta_n/core/verified_code.py`

> if res.passed:
>     kept[name] = source
>     if res.ran_in_sandbox:
>         sandbox_verified.add(name)
> --- `meta_n/core/evolutionary_orchestrator.py`

No exploit or helper invocation was observed. The checked result channel bounds provenance; it does not erase the implemented filtering, retained stamp or downstream ranking effect.

#### MEM-OBJ-bash-library
Label: Bash helper library part

Part of: [RT-OBJ-code-library](runtime.md#rt-obj-code-library)

Source-native identity: `InjectedCode.code_library_bash`. Symbolic bash mapping; storage in injection JSON, `.sh` sidecars and native/external staging. Lineage: Ω parsing or repair, then same-name merge. Later consumers are bash execution/tool calls and model-interpreted helper descriptions. Bash does not acquire the Python held-out verification status merely by sharing this container. No deployed invocation or benefit is observed (SRC-1, `meta_n/core/meta_layer.py`, `meta_n/core/run_persistence.py`; [RT-RTE-helper-verification](runtime.md#rt-rte-helper-verification), [RT-BAP-executable-injection](runtime.md#rt-bap-executable-injection)).

> with open(cand_dir / f"solver_lib_bash_{name}_d{i+2}.sh", "w") as f:
>     f.write(src)
> --- `meta_n/core/run_persistence.py`

#### MEM-OBJ-checkpoint
Label: Search continuation checkpoint

Source-native identity: `checkpoint.json`. Symbolic JSON control/access metadata on disk: iteration, patience, previous best/oracle, histories, RNG, usage, optional base floors/config snapshot and admission bars. It is not a transcript or a replacement for injection files. Lineage: software snapshots live search state. Later consumer: resume restores control and reconstructs selection from separate candidate directories. Authority is deterministic scheduling/recovery state. Starting/resuming is an operator decision; field contents are software-authored. Distinct from retained rationale and maps in [RT-OBJ-rationale](runtime.md#rt-obj-rationale) and [RT-OBJ-task-solution-map](runtime.md#rt-obj-task-solution-map); closest supplied continuation account is [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission), not a checkpoint object (SRC-1, `meta_n/core/run_persistence.py`).

> atomic_json_dump(out_dir / "checkpoint.json", checkpoint)
> --- `meta_n/core/run_persistence.py`

Candidate-level co-located bars supplement checkpoint bars, so stale checkpoint metadata need not resurrect a barred best. This is an explicit recovery rule, not proof of a complete atomic run transaction (SRC-1, `meta_n/core/archive.py`).

#### MEM-OBJ-prior-summary
Label: Compacted prior-work summary

Source-native identity: the user message headed `Prior work summary` produced by `_summarize_context`. Natural-language derived memory stored in the current task's message list. Lineage: removed messages, including an earlier summary on repeated compaction, are rendered with role labels into a separate model call. Later foreground turns receive the returned summary instead of those bodies. Its authority is model interpretation, not a forced preservation of facts or rules. Distinct from [RT-OBJ-rationale](runtime.md#rt-obj-rationale): this compresses a solving conversation, not an injection proposal's reasons. It is local to [RT-RTE-agentic-loop](runtime.md#rt-rte-agentic-loop), with no inspected disk reload of the summary (SRC-1, `meta_n/core/agentic_solver.py`).

> to_summarize = messages[1:-keep_n]
> conversation_text = "\n\n".join(
>     f"[{m['role']}]\n{m['content']}" for m in to_summarize
> )
> --- `meta_n/core/agentic_solver.py`

### Routes

#### MEM-RTE-omega-context
Label: Selected archive context for Ω

Part of: [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission)

This route is the read/selection portion of the supplied generation route, not another declaration of candidate admission. Trigger: generation or repair asks Ω to process retained traces and chain. `ContextManager` and Ω formatters decide the view; archive code separately supplies inspiration. Neither selector requires per-content human approval. Task evaluator outcomes are reference signals, not an independent summary truth oracle. Operating mode: bounded improvement experiment (SRC-1, `meta_n/utils/context_manager.py`, `meta_n/core/omega.py`, `meta_n/core/archive.py`).

- Immediate return: formatted Ω request and, after a provider call, parsed injection/token count.
- Later read-back: retained parent traces, prior injections/rationale and selected other-candidate scripts reach the next Ω invocation.
- Delegated visibility: default sample targets at most 20 traces with 75% failure slots; default eviction removes successes first. Ω raw displays strip library prefixes, keep stdout head/tail (200/300 chars), stderr/eval-feedback tails (800 each), script and error summary. Depth at least 3 with previous scores normally gets category/failure/delta summaries and up to three representative traces; discover mode forces raw presentation. Context-stack rendering includes preprocessing, Python/bash source and rationale, not raw Ω sidecars or frozen maps.
- Selection predicate: trace success flag, seeded randomness, estimated trace budget; old-layer eviction for context-stack budget; focus-task pin and failure/regression/success representative selection. Inspiration selects other candidates' indexed best scripts for task score gaps, sorts gaps, caps at five; its display omits execution feedback.
- Invalidation or expiry: omitted bodies remain in the archive/live chain; eviction expires visibility for this request only. The newest injection is kept even if oversized. No automatic obsolete-source deletion follows.
- Activation or effect: a one-user-message Ω request is wired; its parsed proposal can affect later admitted chains. Actual dependence on a particular excerpt is unobserved.
- Evidence limits: chars/4 estimates and allocated section budgets do not bound the complete request including inspiration, metadata and other sections; text interpretation and faithfulness unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> sampled = self.context_manager.sample_traces(traces)
> truncated_stack = self.context_manager.truncate_context_stack(context_stack)
> --- `meta_n/core/omega.py`

> def traces_budget(self) -> int:
>     return int(self.available_tokens * self.traces_ratio)
> --- `meta_n/utils/context_manager.py`

Default available budget is 100,000 minus 2,000 overhead, allocated 65% to traces and 35% to the stack. Optional symmetric sampling backfills failure slots and preserves the ratio during budget eviction. This is code-selected requested delivery, not an unsolicited memory suggestion service. A full-trace helper-usage scan is scoped to visible stack names before appending its guidance (SRC-1, `meta_n/core/omega.py`).

> if code.rationale:
>     part += f"Rationale: {code.rationale}\n"
> --- `meta_n/core/omega.py`

This retained reason has an actual subsequent reader. Category and delta sections are computed representations of selected traces, not evidence that the model formulated content-directed criticism.

#### MEM-RTE-archive-resume
Label: Durable archive reconstruction

Distinct from the trial/generation progression of [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission): this route consumes persisted files to rebuild selection and execution state. Owner: `RunPersistence`, `Archive` and orchestrator resume control. Operator requests continuation; software admits files using parsing/integrity checks, without renewed human approval of injection content. Operating mode: search recovery; no new value oracle on loaded source (SRC-1, `meta_n/core/run_persistence.py`, `meta_n/core/archive.py`).

- Immediate return: checkpoint mapping plus rebuilt archive, or `None` and fresh archive on failure/empty reconstruction.
- Later read-back: restored traces, full injection source/rationale, stamped verified-name metadata and repaired-event JSON feed resumed selection, Ω and reconstructed solves. Loading the stamp does not authenticate helper execution or renew value verification; its warrant remains conditional on trustworthy original runner measurements.
- Delegated visibility: reconstruction reads summaries, trace JSON, depth-indexed injection JSON and repair JSON. It does not read raw prompt/response `.txt` sidecars; those fields restore empty. Foreground models receive only their route-specific rendered views.
- Selection predicate: candidate directories with readable summaries; replay sorted by iteration/name; depth-minus-one injection count integrity; corrupt candidate skipped, corrupt diagnostic repair sidecar skipped separately. Bars union checkpoint and candidate summary copies; child counts recompute from loaded parent edges.
- Invalidation or expiry: missing/inconsistent files can exclude a candidate; invalid/empty checkpoint falls back to fresh. Current configuration wins after drift warning, so this is not exact replay. Existing disk history is not thereby withdrawn.
- Activation or effect: rebuilt indexes and RNG/control state govern resumed work, with executable chains available to later consumers.
- Evidence limits: candidate writes are multi-file non-atomic; checkpoint/index replacement is atomic via a temporary file, with directory fsync best effort. Source/code has no renewed freshness or security proof merely by being loaded.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if len(injected_codes) != expected_ics:
> --- `meta_n/core/archive.py`

> ck_bar = (barred_from_best or {}).get(candidate.candidate_id)
> disk_bar = summary.get("barred_from_best_task_ids")
> merged = set(ck_bar or []) | set(disk_bar or [])
> archive.add(candidate, bar_from_best=merged or None)
> --- `meta_n/core/archive.py`

The partial-chain countercheck rules out the stronger claim that every saved summary is reusable. It does not establish complete trace-file consistency or a transaction across candidate files. Admission guidance is schema/integrity and previously recorded policy state, not a new human review; recovery can retain earlier valid candidates while excluding corrupt ones.

#### MEM-RTE-context-compaction
Label: Per-task summary replacement

Part of: [RT-RTE-agentic-loop](runtime.md#rt-rte-agentic-loop)

Software controls when to compact; a separate model call authors the replacement under `SUMMARIZE_PROMPT`. No per-summary human approval or independent factual oracle is wired. This is a bounded solving episode, not a permanent memory store. Proposed change: replace aged-out conversation with interpreted prose; rollback on a raised summary-call exception leaves the original messages assigned. Returned summary fidelity is not independently checked (SRC-1, `meta_n/core/agentic_solver.py`).

- Immediate return: compressed messages and summary-call token usage; fewer than six messages return unchanged.
- Later read-back: subsequent task turns receive the derived summary, including recursively summarized prior work on repeated triggers.
- Delegated visibility: summary call sees the removed middle rendered with role labels; foreground retains first message, summary and last four messages. Other tasks' ongoing conversations remain outside this frame; returned best trace and accounting escape to candidate search.
- Selection predicate: chars/4 estimate above 85% of context budget triggers compaction; above 95% stops before the call. Code selects middle messages, not semantic importance. Summary request uses temperature 0.3 and max_tokens 2000, subject to client retry behavior.
- Invalidation or expiry: successful replacement removes old bodies from model-visible messages; no pointer-based reload route is wired in this loop. Frame ends on return; saved trace is not a full reloadable conversation.
- Activation or effect: later model requests use the replacement messages; reasoning preservation and behavioral influence of any particular sentence remain unobserved.
- Evidence limits: no sampled summary or execution trace; heuristic budget is not a provider-token invariant. A returned summary is not a verified retention of executable details or reasons.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The implementation passage for the first-message/summary/tail return is supplied by [RT-RTE-agentic-loop](runtime.md#rt-rte-agentic-loop). The selection mechanics are directly inspected:

> first = messages[0]
> keep_n = min(4, len(messages) - 2)
> keep = messages[-keep_n:]
> --- `meta_n/core/agentic_solver.py`

The frame analogy describes isolation and selective return, not references into a persistent heap: the later model gets values, not dereferenceable handles for evicted messages. Compaction is a trace-fed derived-memory write within one task; candidate code generation is a separate trace-fed write across trials.

#### MEM-RTE-seed-import
Label: Operator-selected helper initialization

Distinct from Ω generation in [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission): this alternative admission originates in a selected JSON file, not current experiment traces. The CLI operator selects the path; authorship and upstream trace provenance of its contents are unresolved. Software checks dictionary/string shape and static code validation before configuration passes the mapping to the seeded candidate. No independent performance oracle at load time. Operating mode: experiment initialization, with later seed evaluation and consumers supplied by [RT-RTE-native-solve](runtime.md#rt-rte-native-solve) (SRC-1, `meta_n/main.py`).

- Immediate return: validated helper mapping, `None` without a path, or `ValueError` on invalid contents.
- Later read-back: seeded helper source enters an evaluated chain, persistence and subsequent chain/Ω consumers; this route itself does not establish that the file was experience-derived.
- Delegated visibility: loader sees the entire JSON mapping; native consumers receive staged source/descriptions, Ω sees its selected context view.
- Selection predicate: explicit seed path, string name/source entries and `validate_code` success.
- Invalidation or expiry: invalid import is rejected before staging; later name overrides change merged live source, not old stored candidates. No source freshness policy is established.
- Activation or effect: seed source is wired into chain initialization rather than a new model proposal; actual adoption is unobserved.
- Evidence limits: operator supplying a path is not evidence of human authorship or review of each function; AST acceptance is not safety/value proof.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> ok, msg = validate_code(source)
> if not ok:
>     raise ValueError(
>         f"--seed-code-library {path}: helper '{name}' failed safety "
>         f"validation: {msg}"
>     )
> seeded[name] = source
> --- `meta_n/main.py`

Guidance and admission are static loader rules plus operator selection; prior experimentation, reasons and approval history are not required by this file contract. Rejection raises at load time; fallback to a previously admitted chain is an operator/search choice, not an automatic undo of execution.

#### MEM-RTE-test-readback
Label: Retained source test evaluation

Distinct terminal read-back from [RT-RTE-frozen-routing](runtime.md#rt-rte-frozen-routing): these consumers evaluate stored source or re-solve using a reconstructed best chain on adapter test tasks. Software selects; operators enable evaluation, not per-script approval. Oracle: adapter `evaluate_test`; operating mode: held-out evaluation, not fresh injection generation. It need not traverse the original proposal gate (SRC-1, `meta_n/core/evolutionary_orchestrator.py`).

- Immediate return: per-task test-score mapping, empty mapping if unsupported, with caught errors reported as zero.
- Later read-back: per-task-best stored scripts go to oracle test evaluation; single-best-chain test evaluation either reuses that chain's stored traces or calls its reconstructed solver for adapter-provided test tasks.
- Delegated visibility: evaluator gets script/task; only the re-solve branch exposes current test task and chain context to a solver model.
- Selection predicate: executor adapter exposes `evaluate_test`; oracle index selects each task; chain selects archive best; presence of `get_test_task` chooses re-solving.
- Invalidation or expiry: missing traces skip tasks; changed inputs/environment can invalidate earlier scores. Held-out failure does not automatically remove archived source in these functions.
- Activation or effect: stored source is handed to adapter evaluation, or solver is called again; fresh test results are not inferred from recorded development scores.
- Evidence limits: adapter correctness, held-out independence and actual execution/results unobserved; frozen task-ID shortcuts can affect a reconstructed native solver.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> eval_result = await adapter.evaluate_test(task, trace.script)
> --- `meta_n/core/evolutionary_orchestrator.py:3824-3876`

> if needs_re_solve:
>     test_task = adapter.get_test_task(task)
>     script, _, _ = await solver.solve(test_task)
>     eval_result = await adapter.evaluate_test(test_task, script)
> --- `meta_n/core/evolutionary_orchestrator.py`

#### MEM-RTE-postrun-analysis
Label: Durable diagnostic readers

No supplied record counterpart: these post-run consumers are not later solver invocations. The inspected best-of-k reader consumes scores/usage/status; emergent-role loading consumes injection source from legacy depth layout or best archived chain. Software selects records under caller-supplied experiment paths. Operating mode: post-hoc analysis, not agent adoption. Remaining analysis consumers are inventoried but not fully audited (SRC-1, `meta_n/analysis/best_of_k.py`, `meta_n/analysis/emergent_roles.py`).

- Immediate return: structured run metrics or loaded injection objects for further analysis.
- Later read-back: retained summaries and injection JSON reach later analysis invocations; this does not establish feedback into search or a model's operating instructions.
- Delegated visibility: best-of-k sees finite summary metrics, per-task scores and call counts. Emergent-role loader augments legacy JSON with response text but does not augment archived JSON with `omega_response_d*.txt` sidecars.
- Selection predicate: supplied run/experiment directory; unique summary discovery for best-of-k; legacy contiguous depths first for role analysis, else best-chain ID from lineage then summary.
- Invalidation or expiry: unavailable/ambiguous summary can raise; missing code paths can yield empty load. No inspected withdrawal of source from the active archive by these readers.
- Activation or effect: source data becomes diagnostic output, not a new admitted intervention on the inspected loader path.
- Evidence limits: downstream model/rule analyses and all metric algorithms not fully inspected; their accuracy and actual execution unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> d = json.loads(_summary_path(run_dir).read_text())
> --- `meta_n/analysis/best_of_k.py`

> cand_dir = self.experiment_dir / "archive" / best_id
> return _load_contiguous_injected_codes(
>     lambda d: cand_dir / f"injected_code_d{d}.json"
> )
> --- `meta_n/analysis/emergent_roles.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-pre-process](runtime.md#rt-obj-pre-process)

Lineage: Ω parses source; native/agentic/external shared preprocessing derives a task-local string. Source is durably retained in injection JSON and `.py` sidecar, whereas the emitted context is recomputed for current tasks. Consumers differ: host Python executes the symbolic rule; the solver/SDK interprets emitted prose. Reasons can survive separately as rationale, but no requirement establishes explanation of every rule. Existing host-limit and copy-fallback passages in [RT-CLM-host-boundary](runtime.md#rt-clm-host-boundary) bound its authority; source emission is not a trusted retrieval corpus (SRC-1, `meta_n/core/meta_layer.py`, `meta_n/core/run_persistence.py`).

#### On [RT-OBJ-rationale](runtime.md#rt-obj-rationale)

Storage/read-back: ordinary injection JSON retains rationale even though raw Ω messages are excluded; archive reconstruction restores the field. `_format_context_stack` includes it in subsequent Ω requests when that layer survives budget selection. Rationale is retained natural-language reasoning about proposed changes, not a proof or executable gate; no direct native solver rationale channel is established by this formatter. Direct quote and consumer details are in [MEM-RTE-omega-context](#mem-rte-omega-context) (SRC-1, `meta_n/core/omega.py`, `meta_n/core/archive.py`).

#### On [RT-OBJ-task-solution-map](runtime.md#rt-obj-task-solution-map)

Storage/lineage: normal injection JSON serializes the map alongside source/rationale; reconstruction loads it. The map derives from indexed retained winners, not an Ω-authored general strategy. Native task-ID matching grants executable dispatch authority and bypasses model reasoning; external mapper parity is not established. Ω context-stack rendering does not include the map, even though persisted injection objects can contain it. Admission bars/floors affect the index supplying winners, not every archived trace ([MEM-OBJ-trace](#mem-obj-trace); SRC-1, `meta_n/core/run_persistence.py`, `meta_n/core/archive.py`, `meta_n/core/omega.py`; [RT-RTE-frozen-routing](runtime.md#rt-rte-frozen-routing)).

#### On [RT-RTE-within-refine](runtime.md#rt-rte-within-refine)

Write/curation horizon: gate-failure traces enter a model-authored repaired injection under the fixed repair directive; passing repaired chain and repair-event metadata persist. Candidate writer saves event JSON and paired raw-text sidecars; reconstruction loads event JSON but not raw text. Rejected original remains outside this archive branch. A durable event classifies the attempt, not a later solver instruction; altered source/rationale have the later chain/Ω consumers. Admission and theory limits remain those supplied by the route (SRC-1, `meta_n/core/run_persistence.py`, `meta_n/core/archive.py`).

#### On [RT-RTE-downstream-repair](runtime.md#rt-rte-downstream-repair)

Trace-fed write: lower-chain source plus full-chain failures and higher-layer feedback produce a replacement injection in a new candidate, leaving old candidate history intact. Ω's downstream formatter renders above-layer source/rationale and explicitly warns that failure traces are contaminated by those layers. This provides reasons/context to the proposal consumer, not independent attribution. Nonempty evaluated variants can persist even when classified non-improving; retained event acceptance is not a universal archive veto (SRC-1, `meta_n/core/omega.py`; supplied route passage).

#### On [RT-RTE-external-spine](runtime.md#rt-rte-external-spine)

Storage distinction: evaluated `Trace` is readable task source/result material used by archive consumers; telemetry rows supply run/accounting/access metadata; copied `agent_logs` and transcript pointers are not interchangeable with that trace. The inspected caller invokes best-effort log copying before finishing its telemetry row and releasing the lease. A backend without logs can retain null pointers. No later SDK-conversation reload is established. Backend transcript encoding/content completeness and copy internals remain uninspected, preventing a claim that complete raw conversations survive teardown (SRC-1, `meta_n/core/external_agents/solver.py`).

> self._dereap_logs(rec, lease)
> --- `meta_n/core/external_agents/solver.py:533-554`

## Write side

The ordinary automatic experience-to-intervention chain is **evaluated traces → selected/formatted Ω request → model-written preprocessing/helpers/rationale → software admission/evaluation → archive/persistence → subsequent Ω and solver consumers**. The supplied [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission) and helper/repair records give rejection ability and proposal guidance; [MEM-RTE-omega-context](#mem-rte-omega-context) gives what actually reaches the proposal model. Software physical writes do not imply human curation. Starting a run or choosing a prompt configuration is not per-injection approval.

The checkpoint and candidate directory are complementary forms, not alternative complete copies. The first keeps control/RNG/admission metadata; the second keeps behavior-shaping source and traces. Corrupt candidate exclusion and empty-checkpoint fallback are recovery, not content-directed criticism. Same-name overrides remove previous helper authority from a new merged view while old candidates remain available. Optional helper filtering and non-adoption bars likewise have narrower rejection scope than “delete bad experience” ([MEM-RTE-archive-resume](#mem-rte-archive-resume), [MEM-OBJ-python-library](#mem-obj-python-library), [MEM-OBJ-trace](#mem-obj-trace)).

There are two additional acquisition/curation routes. Operator-selected seed JSON imports helper content of unresolved authorship/provenance, followed by static admission and seed evaluation. Compaction transforms within-task model/action/observation messages into prose for the next invocation, with no persistence requirement beyond the current task. Neither should be collapsed into storing raw logs ([MEM-RTE-seed-import](#mem-rte-seed-import), [MEM-RTE-context-compaction](#mem-rte-context-compaction)).

Consolidation inherits non-focus traces; merge assembly derives task-ID/source routing from winners without new Ω generation or evaluation. Persisting that result does not convert its recorded score into a fresh observed result. Test reads can execute it or existing source again; they are downstream consumers, not universal re-admission ([RT-RTE-frozen-routing](runtime.md#rt-rte-frozen-routing), [MEM-RTE-test-readback](#mem-rte-test-readback)). No source-grounded claim of obsolete-content expiry, human review of every stored item or reversal of executed filesystem/network effects follows from these mechanisms.

## Read-back

- **Proposal consumer:** Ω requests retained experience; automatic selectors supply sampled failures/successes, summaries, prior source/rationale and scored inspiration. Archive task/score targeting, random sampling and section budgets are distinct operations. Delivery is rendered text in a model call; guidance authority does not prove reliable interpretation ([MEM-RTE-omega-context](#mem-rte-omega-context)).
- **Task consumer:** native chains execute preprocessing and stage merged source; agentic and external routes reuse those interventions via their respective context/staging channels. Full live source can exceed Ω's selected view. Static prompts are not retained experience ([RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance), [RT-BAP-executable-injection](runtime.md#rt-bap-executable-injection)).
- **Continuation consumer:** resume parses persisted candidates/checkpoint state before resumed selection and solving. Diagnostic raw Ω sidecars remain outside that ordinary reload ([MEM-RTE-archive-resume](#mem-rte-archive-resume)).
- **Within-task consumer:** later agentic turns receive first message, derived summary and verbatim tail; eviction leaves no dereferenceable pointer to removed conversation in that context ([MEM-RTE-context-compaction](#mem-rte-context-compaction)).
- **Evaluation/analysis consumers:** stored winners and reconstructed best chains feed test evaluation; retained scores/code feed post-run readers. These are actual shipped consumers, not hypothetical callers inferred from storage APIs ([MEM-RTE-test-readback](#mem-rte-test-readback), [MEM-RTE-postrun-analysis](#mem-rte-postrun-analysis)).

## Integration issues

1. **CLI qualification:** the supplied ordinary CLI account uses `meta-n --tasks <json>` as representative, but the frozen guard rejects invocation without archive mode. Bare custom-task use needs `--use-archive` or an enabling configuration. This affects reachability of [RT-RTE-native-solve](runtime.md#rt-rte-native-solve), not its execution mechanism (SRC-1, `meta_n/main.py`).

   > "[red]Error: --use-archive is required (the linear orchestrator has "
   > "been retired). The bundled benchmark config enables it by default; "
   > --- `meta_n/main.py`

2. **Persistence qualification, not a transaction claim:** [MEM-RTE-archive-resume](#mem-rte-archive-resume) adds atomic checkpoint/index replacement and partial injection-count rejection. The supplied account's non-atomic multi-file limit remains valid; blanket “ordinary writes” should not conceal the single-file protection (SRC-1, `meta_n/utils/atomic_io.py`, `meta_n/core/archive.py`; [RT-RTE-chain-admission](runtime.md#rt-rte-chain-admission)).
3. **Diagnostic availability differs from consumption:** the candidate writer saves raw Ω sidecars, but ordinary archive rebuilding does not restore them. The emergent-role archive loader also does not augment injection JSON with those response sidecars; its comment claims none exist, contradicted by the writer. Do not infer complete rationale/request exposure from file retention. Rationale field itself is loaded and has an Ω reader ([MEM-RTE-postrun-analysis](#mem-rte-postrun-analysis), [MEM-RTE-archive-resume](#mem-rte-archive-resume), [RT-OBJ-rationale](runtime.md#rt-obj-rationale); SRC-1, `meta_n/core/run_persistence.py`, `meta_n/analysis/emergent_roles.py`).
4. **Contained records, not duplicates:** Python/bash objects are declared parts of the supplied library container; selected Ω context and compaction are route parts. They preserve the container referents and add materially different checks/consumers. Resume, seed import, test and diagnostic routes have distinct endpoints; trace/checkpoint/summary objects have no supplied object counterpart. No possible duplicate remains after these comparisons.
5. **Unresolved included surfaces:** SDK/provider conversation management, exact copied transcript content, all adapter/evaluator-cache invalidation and remaining diagnostic metric transformations were not inspected in depth. These limits prevent complete external conversation retention/reload, exact cache freshness and complete metric-provenance conclusions; they do not suppress known trace-to-code and trace-to-summary paths. A diagnostic pointer is not evidence of readable or complete payload ([RT-RTE-external-spine](runtime.md#rt-rte-external-spine), [MEM-RTE-postrun-analysis](#mem-rte-postrun-analysis)).

6. **Verification provenance correction:** [MEM-OBJ-python-library](#mem-obj-python-library) now distinguishes retained pass/status-derived stamping from independently proven helper execution or value verification. Its downstream non-adoption authority and reconstructed metadata retain the same trust limit. The supplied current [RT-RTE-helper-verification](runtime.md#rt-rte-helper-verification) already carries this qualification; the older fragment in the refusal does not supersede that current input. Stub/dependency distinctions, storage and reconstruction remain supported (SRC-1, `meta_n/core/verified_code.py`, `meta_n/core/evolutionary_orchestrator.py`).

## Limitations and checks

The source identity and frozen HEAD match the supplied boundary. Direct source excerpts and cited runtime records supply implementation/design evidence only. Negative conclusions are bounded to inspected consumers: lack of raw-text reload in the named archive/analysis loader is not a system-wide absence of inspection tools. Included but shallowly inspected caches, backend logs and diagnostic algorithms remain explicit coverage limits. No complete execution campaign, actual summary, or intervention/comparison was supplied; improvement, causal benefit, faithful criticism and exercised model reliance remain unestablished independently of the wired memory routes.

Validation: the invocation-specific `commonplace-run validate-output` check passed: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” This establishes the checks the command performed, not semantic acceptance or measured benefit.
