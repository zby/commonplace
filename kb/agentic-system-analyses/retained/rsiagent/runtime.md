---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "RSIAgent runtime baseline tracing benchmark entrypoints, model-authored execution, verification boundaries and learning admission."
run-id: AAS-2026-10-14-rsiagent-b11225763c0b-01
reviewed-boundary: "4d7ef43770dda341fccd9a5743db92407687c615"
---

# RSIAgent runtime report

## Runtime account

### Evidence and consequential work

RSIAgent ships an enclosing runtime for discovering how digital environments work, solving tasks through generated programs, checking candidate states, and carrying experience into later tasks through files. The retained mechanism is not weight training. The authors' claim is [RT-CLM-training-free](#rt-clm-training-free); implementation supports a completion-client architecture and an admission path for durable experience, not demonstrated improvement. All findings below use SRC-1 at the frozen revision. No execution traces, tests or experiments were run or supplied. Implementation conclusion statuses describe wiring, not successful activation or benefit.

Additional inspection beyond the boundary's initial coverage included the Actor turn protocol, context folding and resume controller in `core/loop.py`, role configuration, `core/checks.py`, legacy and full-Agent verification in `core/verifier.py`, namespace execution and Look routing in `core/verifier_runtime.py`, and selected recovery admission in `explore/phase1_boundary_recovery.py` and `explore/phase2_recovery.py`. These supply implementation evidence; prompts and role comments additionally supply doctrine/design. Recovery variant bodies not read remain uninspected, not absent.

### One ordinary invocation and its enclosing phases

A public OSWorld batch, for example the README's `python run_osworld.py --arm both --name osworld_run_01 --concurrency 1`, expands each task into a baseline subprocess and an RSI protocol's three phase subprocesses. The planner obtains a target query from a shipped query file or the public task instruction. It places the same task into Phase 2 development and Phase 3 task lists. Thus this public route is target-conditioned adaptation, not an independent held-out-task generalization test merely because the protocol field is named `held_out_tasks`. Execution verifies release preparation before launching jobs, uses separate cache paths, writes logs/status JSON, and stops a task's command sequence on a nonzero return (SRC-1, `README.md`, `run_osworld.py`).

The baseline or final task process resets a DesktopEnv, optionally quarantines guest-visible evaluator files, wraps its VM transport, uploads any attached memory, and builds a filename/size inventory. It passes the task, inventory preamble and optional benchmark user-simulator callback to `run_with_resume`. Actor, Verifier and vision decisions use distinct contexts even when a configured model identity overlaps. The Actor receives a system method, task, observations and history; it returns text JSON, not provider-native tools. The parser and loop choose Program, Look, Ask or Done. Python/Bash Programs run through the VM; stdout/stderr and exit classification return on the next turn. Look either delivers pixels or a delegated vision report. Ask invokes the supplied simulator rather than establishing a human approval gate. Done proposes checks and initiates independent inspection in the baseline profile (SRC-1, `benchmarks/osworld/task.py`, `core/actor.py`, `core/loop.py`). See [RT-RTE-task-execution](#rt-rte-task-execution) and [RT-RTE-candidate-verification](#rt-rte-candidate-verification).

A local Verifier failure can return findings to the same Actor for revision. The current baseline enables a persistent full-Agent Verifier, allows UNVERIFIED evidence requests, and selects `rollback_mirror`; it does not enable Curriculum routing or candidate-blind orientation. Its watchdog ceilings are 500 iterations and ten hours, with one stalled-context resume and a configured cross-model escalation. Model changes get separate Verifier sessions. These are runtime-client controls, not proof that any particular run reached a ceiling or escalation (SRC-1, `config/osworld/baseline.yaml`, `core/loop.py`).

After the harness terminates, the task process saves transcript, candidate checkpoint and provider counts, then invokes the sealed official evaluator. Grading failure retains the completed VM and retries grading rather than rerunning stochastic Actor work; blocked verification preserves a recovery surface and withholds grading. Final output includes score, status, counters and artifact paths. Official grading is an external outcome measurement, not an answer oracle supplied to the Actor or learning loop on this inspected route (SRC-1, `benchmarks/osworld/task.py`).

For RSI, Phase 1 chooses practice projects, including parallel waves, and serializes branch learning into one bank. Phase 2 creates a fresh target environment, Actor and Verifier for each target cycle, learns from grounded outcomes, and asks persistent Curriculum for informative practice before fresh target attempts. Curriculum STALLED leads to a final target test, not inferred correctness. A PASS may itself be learned from and reviewed under the default `curriculum_review` stop policy. See [RT-RTE-curriculum-search](#rt-rte-curriculum-search) and [RT-RTE-learning-admission](#rt-rte-learning-admission). Phase 3 copies frozen memory and runs task consumers without curriculum or host writeback, checking host hashes and boundary records after each task (SRC-1, `core/self_evolving_loop.py`, `explore/phase1_wave.py`, `benchmarks/osworld/phase2.py`, `benchmarks/osworld/pipeline.py`).

ALE is a material second entry family, not an excluded host. `run_ale.py` dispatches preparation/planning/run/report operations. Its host provisions environments and launches a release-copy worker with public task inputs, transport and an allowlisted environment plus model credentials. The worker executes baseline/Phase 3 or learning phases; after a successful `safe_to_grade` result, the host collects output, stages references and calls the external evaluator. Learning phases instead require transition readiness and zero official evaluator calls. Failed guests are kept for diagnosis. This separation changes the effect and evidence boundaries: worker completion alone is not an official score (SRC-1, `run_ale.py`, `benchmarks/ale/host.py`, `benchmarks/ale/worker.py`).

### Context and identity control

The Actor's summary mode folds old user/assistant pairs when configured count or character thresholds are crossed. Code selects the oldest eligible pairs, preserving a configured verbatim tail; a model revises a bounded WORK LOG, with deterministic digest fallback on an empty response. Subsequent calls receive the task verbatim, summary and tail, not all original turns. History and saved artifacts remain separate from the rendered context; recovering omitted facts generally means re-probing the machine or reading files, not dereferencing an automatic transcript pointer. This supplies same-run read-back of a model-written summary. Full-history profiles (`history_keep_pairs: 0`, including inspected practice and Verifier roles) bypass this folding path (SRC-1, `core/loop.py`, `config/roles/actor.yaml`, `config/roles/verifier.yaml`).

> + instruction + "\n\nWORK LOG — your running summary of earlier "
> "turns (full details live in the machine; re-probe if you need "
> "specifics):\n" + summary}]
> + history[covered * 2:]) if summary else history
> --- `core/loop.py`

The assembly preserves a task/log envelope and an unfurled history tail; it does not establish summary fidelity. The summarization rule itself is model-mediated content selection, while thresholds, batch choice and tail retention are code rules.

Stalled Actor recovery discards its conversation but keeps the machine. A worklog or synthesized summary, optionally a strategy review, crosses into a fresh Actor context; escalation may switch both Actor and Verifier configuration. The caller's combined transcript is not the new Actor's complete live history. The frame analogy fits fresh role/project contexts: selected inputs enter, results/reports escape. It does not imply shared lexical memory or automatic reachability of omitted turns. Persistent Curriculum history, Verifier scratch and canonical memory are separate surviving state. Full-Agent Verifier transport recovery also checkpoints substantive actions and can remove recurrent actionless exchanges through semantic replay while preserving observations and image attachments (SRC-1, `core/loop.py`, `core/verifier.py`).

> discard the conversation, keep the machine, and start a fresh attempt on the
> remaining budget with a factual handoff.
> --- `core/loop.py`

### Guarantees, grants and forcing cases

Capability is broad generated Python/Bash, including subprocesses and whatever filesystem, application and network operations the selected environment grants. The current grant differs by role and mode. Ordinary Actor Programs use `vm.run_script`; the full Verifier substitutes a protected executor and role-specific Look fetcher. Curriculum runs on a fresh practice VM and its project root is captured. Prompt prohibitions on supplying solutions or grading are not a general-purpose process sandbox. No inspected live deployment establishes the actual host/guest isolation envelope (SRC-1, `core/loop.py`, `env/vm.py`, `core/verifier_runtime.py`, `explore/unified_evolution.py`, `explore/charter.py`).

The following are source-level forcing cases, not executed attacks:

1. **Verifier noninterference is mode- and path-scoped.** The effect-isolated Program wrapper uses private PID/network/IPC/UTS/mount namespaces, read-only candidate mounts, writable scratch and a capability-dropped desktop identity. Its selected primitive fails closed on preflight failure. But the public OSWorld baseline selects rollback mirror, which instead permits live-state interaction within a QEMU transaction. External services remain outside rollback. A remote write therefore refutes a system-wide reading of “all effects are rolled back,” without refuting the narrower guest-state protocol (SRC-1, `core/verifier_runtime.py`, `env/qemu_rollback.py`, `config/osworld/baseline.yaml`).
2. **Program substitution is not every action.** Document rendering goes through the Verifier executor, but live-screen capture is a fixed trusted harness operation in the desktop namespace; direct image reads are trusted too. Legacy verifier probes and Actor Done checks call `vm.run_command` after textual validation, not the full-Agent executor. Their read-only intent has a different enforcement strength from mount isolation. A guarantee about isolated model Programs cannot be extended to these paths (SRC-1, `core/verifier_runtime.py`, `core/verifier.py`, `core/checks.py`).
3. **Frozen host memory does not mean immutable guest copies or reliable delivery.** Phase 3 omits writeback and checks the host bank. Actor code still receives a guest copy through upload. The standalone OSWorld task path logs a failed upload and continues memory-OFF, whereas Phase-2 attachment and ALE evaluation raise on failed upload. Consequently a planned memory condition alone does not prove delivered or used memory; the pipeline's final records and hashes cover a narrower admission protocol (SRC-1, `benchmarks/osworld/task.py`, `benchmarks/osworld/phase2.py`, `benchmarks/ale/worker.py`, `benchmarks/osworld/pipeline.py`).

| Guarantee | Owner and enforcement point | Strength and covered routes | External contract and conclusion limits |
| --- | --- | --- | --- |
| Full-Agent Program confinement | `AgenticVerifierExecutor`; preflight, namespace wrapper and privilege drop | protocol for effect-isolated Programs and routed document rendering, not Actor Programs, legacy probes or trusted screen capture | Requires guest Linux primitives, sudo/control transport and correct mounts. implementation conclusion status: wired; operation conclusion status: uninspected. |
| Mirror candidate restoration before scoring | Executor close and QEMU transaction rollback; failure raises infrastructure error | protocol for checkpoint-covered guest disk/RAM/process/GUI state, not remote services | Requires provider checkpoint support and successful restoration. implementation conclusion status: wired; operation conclusion status: uninspected. |
| No official evaluator feedback in learning | Phase state machine, task grading order and ALE host/worker handoff | protocol on inspected shipped routes; not a universal information-flow proof against arbitrary environment content | Requires external adapters to honor their supplied public/grader separation. implementation conclusion status: wired; operation conclusion status: uninspected. |
| Frozen evaluation bank | Pipeline tree hashes and no host writeback; ALE memory checks | protocol for host retained tree, not guest-copy immutability or model compliance | Requires correct filesystem/transport records. implementation conclusion status: wired; operation conclusion status: uninspected. |

> If the selected protection primitive is unavailable, execution fails closed as
> infrastructure. It never falls back to ordinary unprotected model execution.
> --- `core/verifier_runtime.py`

The isolation wrapper implements this intent with `unshare`, read-only mount checks and `setpriv`; this is inspected enforcement code, not only its docstring (SRC-1, `core/verifier_runtime.py`). The mirror's restoration implementation invokes QEMU and waits for transport recovery:

> self._hmp("loadvm " + self.tag)
> recovered, detail = self.vm.wait_for_controller(
>     timeout=180, probe_interval=2.0, stable_probes=2)
> --- `env/qemu_rollback.py`

> External
> services outside the QEMU guest are not covered by this transaction.
> --- `env/qemu_rollback.py`

Unobserved forcing paths include concrete guest escape attempts, remote effect recovery, external evaluator internals and the unread recovery variants. Provider-native tools are not an equivalent execution bypass in the inspected client: unsolicited native calls are logged, not executed. Plain-text JSON remains actionable even when native tool use is disabled. Extension/plugin inventory is not claimed; the actual broad capability path here is generated code and host callbacks (SRC-1, `llm/client.py`, `core/actor.py`).

## Shared records

### Components

#### RT-CMP-actor
Label: Actor model role

Source-native Actor seat; distributed-parametric provider model behind a natural-language method and text-JSON protocol. Parameters live outside the repository at the provider; host stores model slugs/config and conversation artifacts. The inspected role uses `z-ai/glm-5.3`, with baseline stalled recovery able to switch to `moonshotai/kimi-k3`. These are endpoint names, not immutable weight hashes. No inspected request updates weights; fixed parameters are author doctrine, while provider internals remain uninspected. Mutable endpoints/provider routing may resolve to another backend/version. SRC-1: `config/roles/actor.yaml`, `config/osworld/baseline.yaml`, `core/loop.py`, `llm/client.py`.

> model: z-ai/glm-5.3
> --- `config/roles/actor.yaml`

#### RT-CMP-verifier
Label: Verifier model role

Source-native Verifier seat; distributed-parametric remote completion model with separate conversation and scratch, configured as `moonshotai/kimi-k3` in the inspected full-Agent profile. Weights are provider-side, not stored or revised by this runtime's inspected calls. The exact weight version is not pinned; a mutable endpoint or configured escalation can change the effective model. Provider internals are uninspected. SRC-1: `config/roles/verifier.yaml`, `core/verifier.py`, `llm/client.py`.

> model: moonshotai/kimi-k3
> --- `config/roles/verifier.yaml`

#### RT-CMP-curriculum
Label: Curriculum model role

Source-native Curriculum seat; distributed-parametric remote model, with distinct persistent history and host/guest notes rather than a shared Verifier context. `moonshotai/kimi-k3` is a configured slug, not a weight pin. The inspected runtime changes prompts/notes, not provider parameters; mutable endpoint resolution and provider internal state are uninspected. SRC-1: `config/roles/curriculum.yaml`, `explore/unified_evolution.py`, `llm/client.py`.

> model: moonshotai/kimi-k3
> --- `config/roles/curriculum.yaml`

#### RT-CMP-vision-model
Label: Delegated vision model

Source-native `vision_model`; distributed-parametric provider component used when the primary Actor receives text rather than image pixels. The inspected Actor profile names `moonshotai/kimi-k3`; Verifier's empty `vision_model` selects native image consumption instead. Storage is remote provider weights plus local delivered-image/report history. No inspected weight-update operation; exact version is not pinned, mutable routing may change backend and provider internals remain uninspected. SRC-1: `config/roles/actor.yaml`, `config/roles/verifier.yaml`, `core/loop.py`, `llm/client.py`.

> vision_model: moonshotai/kimi-k3
> --- `config/roles/actor.yaml`

### Operative objects

#### RT-OBJ-loop-result
Label: LoopResult and task artifacts

Symbolic statuses, counters and routing fields live in Python state and serialized result/checkpoint JSON; natural-language reports and transcripts live alongside them on the host filesystem. This record concerns the control-result interface, not canonical memory content. Phase-2 mapping requires both transport route and report, rather than equating any end-of-loop status with correctness. SRC-1: `core/loop.py`, `benchmarks/osworld/phase2.py`, `benchmarks/osworld/task.py`.

> if result.status == "done" and route == "HANDOFF" and report.strip():
>     return TargetVerification(TargetVerdict.PASS, report)
> --- `benchmarks/osworld/phase2.py`

### Routes

#### RT-RTE-task-execution
Label: Model-authored task execution

Principal: operator-started benchmark task; endpoints: task driver → Actor completion → parsed action → VM or callback → observation → Actor/Verifier → result and sealed grading. Code owns parsing and scheduling; the Actor owns program and next-action content. Natural-language instructions and memory are model-interpreted; action JSON and configuration are symbolic. Current state includes VM artifacts, task-local history, summaries and counters. Executor grants are those of the VM except when a restricted role supplies overrides. SRC-1: `run_osworld.py`, `benchmarks/osworld/task.py`, `core/actor.py`, `core/loop.py`, `env/vm.py`, `benchmarks/ale/worker.py`, `benchmarks/ale/host.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Program trace, image or delegated vision text, Ask callback response, or terminal LoopResult/history; official grade arrives only after harness termination.
- Later read-back: Summary-mode WORK LOG and resume handoff reach later calls; optional bank inventory and Actor-selected files come from earlier admitted learning.
- Delegated visibility: Vision receives selected image/question; independent Verifier has its own context rather than Actor history; Ask reaches a supplied simulator callback.
- Selection predicate: Parsed action type and configuration choose executor; Actor chooses code, image path, question and memory reads; code chooses folding batches and resume eligibility.
- Invalidation or expiry: Fresh task/role frames isolate conversations; folding replaces old visible turns with summary and tail; stalled resume drops the old Actor window while retaining machine and handoff.
- Activation or effect: Programs can change guest state; code wires later observations and summaries into calls. Actual influence of delivered memory and task success remain unobserved.
- Evidence limits: Implementation only; VM/package/provider availability and sandbox effectiveness were not exercised.

> execute_program = program_executor or vm.run_script
> trace = execute_program(
>     turn.lang, turn.code, timeout=cfg.script_timeout)
> --- `core/loop.py`

#### RT-RTE-candidate-verification
Label: Candidate inspection and verdict routing

Endpoints: Actor Done/check results or forced inspection → independent Verifier → PASS/FAIL/UNVERIFIED or routed equivalent → Actor repair, evolution or handoff. Verifier proposes and decides local correctness; code can reject malformed or stale/insufficient transport and refuse to infer correctness from infrastructure absence. The ordinary baseline routes failure back to the Actor; optional callbacks admit Curriculum routing without giving Curriculum the local verdict. There is no per-candidate human approval in these inspected functions. Operating mode is task-directed inspection; expected truth comes from task requirements and machine evidence, not a supplied gold answer. External official evaluator is excluded from the live decision channel. SRC-1: `core/loop.py`, `core/verifier.py`, `core/verifier_runtime.py`, `core/checks.py`, `config/osworld/baseline.yaml`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Verdict and report/findings; failures bounce evidence to the Actor or route control outward; infrastructure/no-progress can block completion.
- Later read-back: Persistent Verifier conversation and, when enabled, private scratch are reused for later candidate inspections; current-candidate evidence is separately required.
- Delegated visibility: Task and candidate evidence reach a distinct Verifier; configured private Actor paths are masked/quarantined, while optional reproducible Actor evidence leads can be supplied.
- Selection predicate: `agentic_verifier_config` selects full-Agent versus legacy probe inspector; execution-mode configuration selects effect isolation or rollback mirror.
- Invalidation or expiry: Per-inspection evidence freshness differs from persistent conversation; model/config identity changes select a separate session; executor closure restores mirror state and closes private resources.
- Activation or effect: Committed verdict changes routing; inspection programs run in the chosen boundary. No observed verdict quality or rollback success is established.
- Evidence limits: Isolation applies at the Program/render executor, not every trusted host operation; legacy and Done probes use textual screening plus ordinary VM command execution.

> if getattr(cfg, "agentic_verifier_config", ""):
>     return False
> --- `core/loop.py`

This guard is inside `uv_accept_ok`: the full-Agent arm cannot turn repeated could-not-confirm results into acceptance through that legacy escape. Other historical acceptance policies remain available when that arm is not selected.

> Direct image reads and live-screen capture are trusted harness operations.
> --- `core/verifier_runtime.py`

> out = vm.run_command(c.probe, timeout=timeout) or ""
> passed = bool(re.search(r"\bPASS\b", out)) and not re.search(r"\bFAIL\b", out)
> --- `core/checks.py`

#### RT-RTE-curriculum-search
Label: Outcome-driven curriculum and target retry

Endpoints: grounded target outcome and same-Actor diagnosis → persistent Curriculum → PROJECT/practice Actor/Verifier loop → updated bank and outcomes → Curriculum → fresh target retry or stop. The outer Python state machine owns lifecycle validity; Curriculum owns project choice and readiness/stall judgment; Verifier owns correctness. The mode is bounded environment experimentation with model-chosen projects, not a gold-answer oracle. Project fixtures/reference inputs may be authored by Curriculum but are not an independently validated oracle. Human launch/configuration supplies scope and stop policy, not per-project semantic approval. SRC-1: `core/self_evolving_loop.py`, `benchmarks/osworld/phase2.py`, `explore/unified_evolution.py`, `explore/charter.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: EvolutionResult READY_FOR_RETRY or STALLED with memory, project count and reason; terminal target loop transfers the live environment and result to its caller.
- Later read-back: Curriculum retains its conversation, private notes, project summaries, complete latest verdict and Actor diagnosis across rounds; practice learning reaches later Actor invocations through the bank.
- Delegated visibility: Fresh project Actor/Verifier contexts do not receive Curriculum private reasoning; project handoff and captured fixture tree cross the boundary. Curriculum can receive canonical memory read-only or an empty ablation attachment.
- Selection predicate: FAIL triggers learning and practice; PASS behavior follows learn/review policy; Curriculum selects projects and semantic stop, while malformed handoffs or missing replayable fixtures prompt continuation.
- Invalidation or expiry: Fresh null-task VM separates practice from discarded target state; target retry creates fresh role frames; STALLED forces one final target test rather than declaring success.
- Activation or effect: Accepted handoff launches practice or returns target control; stored hypotheses are delivered into later Curriculum prompts. Whether they changed actual decisions is unobserved.
- Evidence limits: Prompt instructions establish requested experimental reasoning, not completed content-directed criticism or improved capability.

Admission: Curriculum proposes a natural-language project and fixtures. Code rejects malformed publication/non-replayable fixtures; Verifier may reject its resulting candidate. Curriculum is instructed not to solve or grade. Terminal project publication persists; rollback/recovery uses saved lineage and fresh environments, not automatic semantic undo of a bad hypothesis.

> Maintain and revise hypotheses about the Actor Agent's actual bottleneck. Treat
> each project as an experiment: its purpose is to improve capability or reduce
> important uncertainty.
> --- `explore/charter.py`

Theory account: shipped guidance asks Curriculum to use outcomes to revise bottleneck hypotheses, keeping private notes and outcomes for future search rather than passing its private rationale to the solver. **theory-builder conditions 1–4:** condition 1 conclusion status: afforded — notes can carry whole formulated hypotheses, but no generated hypothesis artifact is supplied; condition 2 conclusion status: claimed — the prompt directs hypothesis-dependent project choice, without observed semantic dependence; condition 3 conclusion status: claimed — contradiction is to change theory, but no supplied criticism places blame and changes reliance; condition 4 conclusion status: wired — notes/outcomes are supplied to repeated turns, without proof that a criticism result shaped one. Addressability: free-form notes permit whole-text inspection/replacement, not guaranteed claim-level structure. Persistence: rounds of one search in host artifacts and session history. Learning: improved future capacity and attribution unestablished. Reflection: the requested bottleneck account concerns Actor operation and is fed by its outcomes, with a wired return path through project selection; actual representation-mediated effects unobserved. Reflective theory builder: unestablished; the selected method text is not shown criticized/revised against its own operation. Autonomous theory builder: roles are computationally assigned, but actual satisfaction of all four internal operations is unobserved; this is not a demonstrated autonomous builder.

#### RT-RTE-learning-admission
Label: Same-Actor learning and bank publication

Endpoints: terminal PASS/FAIL and Actor history → distillation → whole-corpus reconciliation → diagnosis → pull/audit → journal/install → later inventory/file consumer. The same Actor proposes memory content and judges readiness; host code checks transport and target-boundary constraints, not semantic correctness of every lesson. Verifier judges the project, not memory. Curriculum receives a separate diagnosis and cannot approve the bank. No per-content human approval is wired in this inspected path. Operating mode is outcome-triggered experience retention, including failed attempts; answer oracle is inapplicable — the Verifier report is evidence/judgment, not a supplied expected memory answer. SRC-1: `explore/target_learning.py`, `explore/phase1_wave.py`, `explore/commit.py`, `explore/practice_loop.py`, `explore/charter.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Accepted tree, diagnosis and updated Actor history; boundary mismatch raises instead of silently installing a partial accepted subset.
- Later read-back: Canonical host bank is uploaded for later practice/target/frozen evaluation; complete inventory is supplied and Actor chooses reads. Diagnosis separately reaches Curriculum.
- Delegated visibility: Same Actor retains trajectory and final Verifier report; later fresh Actors receive selected retained content, not that whole trajectory. Neither Verifier nor Curriculum grades the memory.
- Selection predicate: Grounded terminal outcome triggers learning according to phase policy; Actor may add/revise/delete/reorganize or leave unchanged; host corpus audit gates publication.
- Invalidation or expiry: Reconciliation requests qualification/removal of stale or unsupported claims; complete-tree replacement can delete files; journal and before/after trees preserve recovery evidence. Parallel branches commit serially against the current bank.
- Activation or effect: Host installs durable files and later routes deliver them; semantic uptake and resulting improvement remain unobserved.
- Evidence limits: Admission is not factual certification. Target-overlap shingle rejection and safe paths constrain leakage/transport, not explanatory truth or effective learning.

Guidance requests future-useful lessons while distinguishing verification from causal explanation. Reconciliation explicitly treats the first update as a draft. Host rejection is possible when audit changes the candidate; installation stages/fsyncs a complete tree, renames the previous tree to backup, and restores it on a failed replacement. This is same-filesystem rename recovery, not a demonstrated crash-proof, always-visible directory swap. Phase-1 branch commits push the current canonical bank before resuming that branch's Actor, preventing a simple stale-tree merge from being the intended mechanism (SRC-1, `explore/phase1_wave.py`, `explore/practice_loop.py`).

> if accepted_memory != candidate_memory:
>     raise PracticeBoundaryError("terminal memory failed the target boundary")
> --- `explore/target_learning.py`

> Neither the Verifier Agent nor Curriculum Agent grades
> the memory.
> --- `explore/charter.py`

Theory account: the instructions request examination of conflicting assertions, stale assumptions and unsupported causal explanations, followed by qualification/revision/removal. They leave content and schema to the Actor. **theory-builder conditions 1–4:** condition 1 conclusion status: afforded — memory may contain whole explicit procedures/explanations, but no learned instance is supplied; condition 2 conclusion status: claimed — instructions ask later Actors to use relevant memory, without evidence of content-dependent decisions; condition 3 conclusion status: claimed — content-directed reconciliation is requested, not observed; condition 4 conclusion status: wired — admitted output reaches later learning/consumption, without a supplied iterative criticism artifact. Addressability: files are inspectable/revisable; finer claim segmentation is not enforced. Persistence: host bank across problems/sessions until replacement, with evaluation freeze. Learning: improved capacity is unestablished independently of durable trace-fed update. Reflection: Actor decisions/actions/outcomes are available for self-description and can inform later behavior through the bank, but both causal directions are not observed. Reflective theory builder: method self-revision is not established. Autonomous theory builder: software/model roles perform the requested pipeline without per-content human approval, but this alone does not establish all theory operations.

Self-improvement assessment: boundary is the shipped agent-plus-bank across exploration and subsequent task operation; objective is improved task capability, specifiable independently of any particular memory edit. Links 1–3 have a wired pathway: experience/report inputs to proposal, installation into the system's bank, and later Actor delivery. No supplied execution establishes actual evidence-responsive determination, semantic uptake or link 4, later behavior causally depending on the change. This supports a dispositional improvement-directed self-change mechanism, not exercised or successful self-improvement.

#### RT-RTE-lineage-recovery
Label: Admission of stopped learning lineages

Endpoints: operator-supplied resume boundary/plan plus archived artifacts → admission checks → restored histories/bank/budgets → resumed Curriculum/practice/target lifecycle. Software decides admissibility; human/operator initiation does not replace role evidence with a new semantic verdict. This is a recovery mode, not an answer oracle or permission to reinterpret infrastructure failure as correctness. SRC-1: `explore/phase1_boundary_recovery.py`, `explore/phase2_recovery.py`, `explore/unified_evolution.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Admitted recovery object or infrastructure refusal; continuation reuses the saved semantic boundary rather than inventing a stop decision.
- Later read-back: Archived Curriculum history, notes, complete outcomes and canonical bank reenter later role calls; budgets and manifests constrain restoration.
- Delegated visibility: Restored role-specific material crosses back to its corresponding role; host prose is not accepted as substitute role evidence in the inspected Phase-2 admission.
- Selection predicate: Phase-1 checks infrastructure stop, nonquarantine, completed wave ledger, unchanged protocol/bank and absence of later phases; Phase-2 checks plan hashes, configuration, completed transactions and nonterminal lineage.
- Invalidation or expiry: Changed artifacts/configuration, partial or rejected lineage, or already-completed boundaries refuse admission. Variant recovery kinds dispatch to separate modules.
- Activation or effect: Admitted state supplies subsequent runtime invocation inputs; no actual restored run is evidenced.
- Evidence limits: Only selected admission branches were read; verified-memory filesystem, post-target boot, ready-target replacement and unverified-practice variant bodies remain uninspected.

Admission mechanism: proposed change is resumption from saved state, not acceptance of a new lesson by operator assertion. Checks can veto; Phase-1 uncommitted work is archived and not promoted. Persistence is saved role history and memory lineage; recovery does not establish semantic rollback of externally effected actions.

> _require(before == memory, "memory includes a partial/uncommitted project")
> --- `explore/phase1_boundary_recovery.py`

> for path, expected in plan['input_sha256'].items():
>     require(sha(path) == expected, 'an archived input changed: ' + path)
> --- `explore/phase2_recovery.py`

### Claims

#### RT-CLM-training-free
Label: Training-free recursive self-improvement claim

The authors claim recursive self-improvement with fixed parameters, broad exploration, targeted practice and frozen test-time reuse. SRC-1, `README.md` supplies doctrine/design, not an observed intervention establishing the contribution of memory or criticism. The independent assessment is the wired pathway and missing causal exercise described in [RT-RTE-learning-admission](#rt-rte-learning-admission).

> Model parameters stay fixed
> throughout exploration and downstream task execution.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-actor-method
Label: Actor method and retrieved knowledge

Consumer: Actor model at subsequent calls. Channel: shipped system method, opening memory inventory, then Actor-chosen file contents returned as ordinary observations. Force: natural-language guidance interpreted by the model, not a mandatory symbolic memory-rule interpreter; Python/Bash action content subsequently receives machine effects through [RT-RTE-task-execution](#rt-rte-task-execution). Horizon: system method per attempt; retained bank across tasks, with frozen evaluation copies. SRC-1: `core/actor.py`, `core/loop.py`, `benchmarks/osworld/task.py`, `explore/charter.py`.

> You own the content, representation, retrieval
> strategy, scope, and stopping decision;
> --- `explore/charter.py`

This describes instructed authority at the update consumer, not guaranteed downstream compliance or a confirmed learned improvement. At the downstream consumer the bank is explicitly fallible guidance:

> They may be wrong, outdated, or inapplicable to this task: treat them as hints
> and verify against the live environment.
> --- `explore/charter.py`

#### RT-BAP-verdict-routing
Label: Verdict-to-control authority

Consumer: Python loop and phase lifecycle. Channel: parsed committed Verifier report plus symbolic status/route. Force: conditional branch admitting repair, practice, handoff or infrastructure stop; content of reports also guides model decisions through interpretation. Horizon: current candidate and persistent role's subsequent inspections, then stored outcome inputs to learning. SRC-1: `core/loop.py`, `core/verifier.py`, `benchmarks/osworld/phase2.py`, `core/self_evolving_loop.py`; see [RT-RTE-candidate-verification](#rt-rte-candidate-verification). A symbolic verdict gate provides control authority without certifying the Verifier's semantic correctness.

## Annotations

none
