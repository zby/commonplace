---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "RSIAgent workflow tracing OSWorld target-conditioned learning, curriculum practice, fresh target retry and frozen evaluation delivery."
run-id: AAS-2026-10-14-rsiagent-b11225763c0b-01
reviewed-boundary: "4d7ef43770dda341fccd9a5743db92407687c615"
---

# RSIAgent workflow report

## Workflow account

### Selection and evidence

The selected workflow is the shipped OSWorld RSI path: a precommitted development task and an existing Phase-1 memory bank enter Phase 2; target work, verification and practice produce a frozen bank; Phase 3 consumes that bank and returns scored task records. It was selected because it connects role delegation to a concrete delivery gate, rather than merely listing the three model roles. The public batch route can put the same task in both phases, so the field name `held_out_tasks` does not by itself establish held-out generalization; see [RT-RTE-task-execution](runtime.md#rt-rte-task-execution) and the runtime account (SRC-1, `run_osworld.py`). This account does not generalize OSWorld phase admission details to ALE.

Evidence is implementation and, where identified, shipped guidance at SRC-1's frozen revision. Added inspection covered `core/self_evolving_loop.py`'s target lifecycle, `benchmarks/osworld/phase2.py`'s execution/verification/learning/evolution hooks and final result writer, `explore/unified_evolution.py`'s Curriculum publication and practice-return loop, and `benchmarks/osworld/pipeline.py`'s Phase-2 and Phase-3 admission and aggregation. These reads extend the boundary's initial scope within the same registered source. No target execution, tests, run artifacts or causal experiment were supplied or performed. A source-supported workflow exists; successful execution, verdict quality and improved capability remain unobserved.

### 1. The host supplies a task, bank and role configuration

The pipeline requires transition-ready Phase 1 and a nonempty precommitted development-task list. It launches the Phase-2 subprocess with task ID, seed, initial-memory path, stop policy, target/practice/Curriculum/memory configurations and benchmark profile. Tasks run serially through this pipeline, with each accepted output bank becoming the next task's input. These are code-owned scheduling and lineage decisions, not model decisions or per-content human approvals (SRC-1, `benchmarks/osworld/pipeline.py`; [WF-RTE-phase-transition](#wf-rte-phase-transition)).

Each target cycle creates a fresh environment, Verifier and Actor. Optional pre-Actor Verifier orientation is configuration-dependent, not a mandatory stage of every invocation. The target adapter installs the current bank, requires a successful guest upload, and supplies the Actor a complete filename/size inventory; the Actor selects which files to inspect. Task instructions, environment observations and subsequent generated-program results provide its working context. The distinct Verifier context is not the Actor's transcript (SRC-1, `core/self_evolving_loop.py`, `benchmarks/osworld/phase2.py`; [RT-RTE-task-execution](runtime.md#rt-rte-task-execution), [RT-RTE-candidate-verification](runtime.md#rt-rte-candidate-verification)).

### 2. Actor work returns a candidate, not correctness

The target adapter calls `run_with_resume` with the task, VM, memory preamble, role configuration and persistent Verifier-session registry. Generated Programs affect the VM; observations return to the Actor. Local repair and stalled-context recovery belong to the inner task runtime. The outer workflow does not equate Actor Done with a passed target. It inspects the inner result's status, committed Verifier route and nonempty report. `done` plus HANDOFF becomes PASS; `evolve` plus EVOLVE becomes FAIL; other endings become UNVERIFIED (SRC-1, `benchmarks/osworld/phase2.py`; [RT-OBJ-loop-result](runtime.md#rt-obj-loop-result)).

The full-Agent Verifier's inspection and effect boundaries are those in [RT-RTE-candidate-verification](runtime.md#rt-rte-candidate-verification), not an unrestricted promise of noninterference. In particular, rollback-mirror protection does not restore remote-service effects. The Verifier judges the task against machine evidence; the official evaluator is not its supplied expected-answer oracle. Symbolic verdict routing gives the judgment control authority without establishing that the judgment is true (SRC-1, `core/loop.py`, `env/qemu_rollback.py`; [RT-BAP-verdict-routing](runtime.md#rt-bap-verdict-routing)).

### 3. Grounded outcomes feed the same Actor, then Curriculum

A grounded FAIL always triggers learning; this OSWorld adapter also enables learning after PASS. Before learning, the adapter checks target direction, bank identity, grounded verdict and active Actor history. It restores the canonical bank to the guest and passes that active context, final Verifier report and outcome into promotion. Distillation, whole-corpus reconciliation, diagnosis, audit and installation are the existing mechanism in [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission). The Actor proposes retained lessons; the host may reject boundary-invalid content. Neither Curriculum nor Verifier certifies the memory's meaning (SRC-1, `benchmarks/osworld/phase2.py`, `explore/target_learning.py`, `explore/charter.py`).

After FAIL, the outer loop releases the failed target environment and delegates to persistent Curriculum with target direction, verdict, full report, same-Actor diagnosis and current memory. The adapter boots a separate practice environment and passes the role configurations and existing Curriculum session to `evolve_until_ready`. Curriculum proposes a project, not a replacement verdict or memory approval. Its durable publication must contain a project body naming the project root and a captured, replayable fixture tree before practice can start (SRC-1, `core/self_evolving_loop.py`, `benchmarks/osworld/phase2.py`, `explore/unified_evolution.py`; [RT-RTE-curriculum-search](runtime.md#rt-rte-curriculum-search)).

A malformed project or missing/empty/non-replayable fixture tree causes a continuation back to Curriculum, rather than launching an underspecified practice attempt. The selected implementation explicitly supplies this corrective instruction:

> f"{PROJECT_ROOT} was absent, empty, or not replayable")
> --- `explore/unified_evolution.py`

Once accepted, the project text, captured fixtures and current bank enter the practice attempt. Its Actor history, terminal outcome and Verifier report then enter learning promotion. Project outcome JSON and a latest-outcome text retain the request, handoff, verdict report, diagnosis and before/after bank manifests. Project summaries and latest outcome feed the next Curriculum round; private Curriculum reasoning is not automatically shared with the project Actor. These are bounded experimentation and report-return mechanisms, not evidence that the model actually designed an informative experiment (SRC-1, `explore/unified_evolution.py`; [RT-RTE-curriculum-search](runtime.md#rt-rte-curriculum-search)).

### 4. Readiness, stall and failure have different successors

READY returns the updated bank to the target state machine, which starts a fresh target environment and role contexts. STALLED also leads to a fresh target attempt, but marks that attempt as final. The source distinguishes a search stopping judgment from correctness:

> Curriculum ``STALLED`` is a semantic stop condition, not target correctness.
> The latest memory therefore receives one final fresh target test and that live
> state is returned for sealed measurement regardless of its local verdict.
> --- `core/self_evolving_loop.py`

The generic function transfers a live terminal environment to its caller; the OSWorld Phase-2 caller freezes memory and writes a result, then releases that environment without official grading. Measurement happens in the later Phase-3 task process. Thus the generic docstring does not imply that this adapter grades the Phase-2 VM (SRC-1, `benchmarks/osworld/phase2.py`, `benchmarks/osworld/pipeline.py`).

Under `curriculum_review`, PASS is learned from and can still prompt practice. A zero-project Curriculum return preserves the passed target as terminal; practice after PASS requires a fresh target test. Under `verifier_pass`, PASS learning is followed directly by termination. On the final post-STALLED attempt, another grounded FAIL can still be learned from, but does not start another Curriculum cycle (SRC-1, `core/self_evolving_loop.py`, `benchmarks/osworld/phase2.py`; [RT-RTE-curriculum-search](runtime.md#rt-rte-curriculum-search)).

UNVERIFIED is neither correctness nor a trigger for grounded learning. The outer loop terminates with `target_harness_unverified`; the OSWorld writer returns exit code 2, and the pipeline's terminal validator refuses that status. Infrastructure hook failures raise rather than becoming FAIL or STALLED; the outer finally block releases untransferred environments. The practice adapter likewise refuses nonsemantic `infra` or `quarantined` returns. These paths stop delivery instead of manufacturing a target judgment (SRC-1, `core/self_evolving_loop.py`, `benchmarks/osworld/phase2.py`, `benchmarks/osworld/pipeline.py`). Operator-initiated recovery is a separate checked lineage path, not an automatic semantic retry of every failure; its inspected scope and uninspected variants remain those of [RT-RTE-lineage-recovery](runtime.md#rt-rte-lineage-recovery).

### 5. Delivery is a checked phase artifact, not necessarily target success

Phase 2 writes terminal status, local verdict, cycle/project counts, initial/final bank hashes, final bank path and evaluator-boundary records. The pipeline validates both new and cached task results. A final post-STALLED FAIL can be transition-ready; an unverified ending cannot. It then freezes the resulting bank and writes the phase result. Phase 3 copies that bank, checks its hash, launches task consumers with curriculum and writeback disabled, and aggregates task score/status records only after its boundary checks pass (SRC-1, `benchmarks/osworld/phase2.py`, `benchmarks/osworld/pipeline.py`; [WF-RTE-phase-transition](#wf-rte-phase-transition)).

The task subprocess's post-harness sealed grading and grading-only recovery remain the mechanism in [RT-RTE-task-execution](runtime.md#rt-rte-task-execution). The delivered pipeline product is `phase3/result.json`, including frozen-bank identity, study design, task records, evaluator accounting and mean score. This is evidence of an implemented completion criterion, not an inspected delivered run. Host hashes protect the retained bank, not the mutability of a guest copy or semantic uptake by the Actor. The standalone task's memory-upload fallback also prevents inferring delivered memory solely from the intended evaluation condition (SRC-1, `benchmarks/osworld/pipeline.py`, `benchmarks/osworld/task.py`; runtime account).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-phase-transition
Label: OSWorld phase transition and delivery

This is the pipeline's host-side admission and aggregation route, distinct from model task execution in [RT-RTE-task-execution](runtime.md#rt-rte-task-execution), model curriculum selection in [RT-RTE-curriculum-search](runtime.md#rt-rte-curriculum-search), and lesson admission in [RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission). It spans their outputs rather than being a material part of exactly one supplied record. Endpoints are transition-ready Phase-1 output → serial Phase-2 task results and banks → frozen Phase-2 bank → Phase-3 task subprocess results → aggregate result. Python pipeline code decides readiness and can veto the next phase; the operator launches/configures the study, not each memory assertion. Models propose task work and lessons through the cited routes, not this gate. State is symbolic JSON status/verdict fields, manifests and hashes on the host filesystem; executable admission rules compare them and launch subprocesses. SRC-1, `benchmarks/osworld/pipeline.py`, `benchmarks/osworld/phase2.py`, implementation evidence.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Accepted phase payload and `result.json`, or ProtocolError/subprocess failure; Phase-3 aggregate includes score/status and source-result paths for each task.
- Later read-back: Accepted per-task banks become later Phase-2 inputs; the frozen bank becomes the Phase-3 attachment; existing result files are reloaded and checked before reuse.
- Delegated visibility: Phase-2 subprocess receives task/configuration/bank paths; Phase-3 task subprocess receives task, seed, locked configuration and frozen-bank path, not Curriculum's private conversation.
- Selection predicate: Precommitted task lists and configured stop policy; terminal status plus grounded verdict, zero evaluator-feedback records, input/output bank hashes, then Phase-3 bank and feedback-boundary checks.
- Invalidation or expiry: Policy mismatch, unready status, invalid verdict, lineage/hash drift or boundary-record mismatch refuses progression; conflicting existing frozen output is rejected rather than silently overwritten.
- Activation or effect: Admitted files supply later task invocations and aggregate records; actual model reliance, score quality and improvement are unobserved.
- Evidence limits: Host record/hash checks are not semantic certification, guest-copy immutability or an independent audit of external evaluator implementation; no execution evidence supplied.

Operating mode is protocol-driven development followed by frozen evaluation. Official scores are aggregate outputs after task handoff, not an expected-answer oracle in the Phase-2 admission decision. A local FAIL after Curriculum stall is accepted as a completed development boundary, not promoted to PASS. The exact stop-policy gate is:

> if status not in allowed or verdict not in {"PASS", "FAIL"}:
>     raise ProtocolError(
>         f"Phase-2 target {task} is not transition-ready: {status!r}, {verdict!r}")
> --- `benchmarks/osworld/pipeline.py`

Proposed state entering this gate is the phase worker's result and retained bank. Admission can veto transport/lineage/protocol inconsistencies, but not a false lesson that passes those checks. Recovery is checked reuse or a separately admitted lineage, not semantic undo; this gate does not reverse effects already made by task Programs. The phase freeze preserves accepted learned content for later consumption while ending further host learning on the evaluation path:

> if after["tree_sha256"] != frozen_record["tree_sha256"]:
>     raise ProtocolError("Phase-3 evaluation mutated frozen host memory")
> --- `benchmarks/osworld/pipeline.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-curriculum-search](runtime.md#rt-rte-curriculum-search)

Workflow-specific ordering: target FAIL is learned from before the failed environment is released and practice begins. Curriculum's STALLED returns control for a final fresh target test; it cannot substitute for the Verifier's verdict. PASS review retains the passed environment while Curriculum decides, permits zero-project completion, and requires fresh target work after any practice. Project-publication rejection continues the Curriculum turn; infrastructure/quarantine returns do not enter the target loop as semantic readiness. These handoffs were inspected in SRC-1, `core/self_evolving_loop.py`, `benchmarks/osworld/phase2.py`, `explore/unified_evolution.py`; the account above retains the workflow-specific passages. Existing theory/learning assessments remain bounded to wiring and guidance, not observed criticism or benefit.

#### On [RT-OBJ-loop-result](runtime.md#rt-obj-loop-result)

Workflow-specific delivery distinction: the adapter maps inner route/report to the local target verdict; the outer lifecycle adds its own termination reason. The pipeline subsequently checks the combination of termination and verdict. Thus a terminal object can mean successful protocol completion with a final local FAIL, while UNVERIFIED cannot advance the phase. SRC-1, `benchmarks/osworld/phase2.py`, `benchmarks/osworld/pipeline.py`; see [WF-RTE-phase-transition](#wf-rte-phase-transition).
