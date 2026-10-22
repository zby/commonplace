---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Harness² workflow report tracing parallel task refinement through composition, output selection, rejection recovery and optional experience retention."
run-id: AAS-2026-10-22-harness2-d5a180ba559c-01
reviewed-boundary: "1cfe254e8d25b15f37048c3730134686abe60335"
---

# Harness² workflow report

## Workflow account

### Selected workflow and evidence boundary

This account selects one task in parallel (`agg`) mode, with k greater than one, inside the shipped domain sweep. It exposes both consequential model handoffs: proposal-to-composition and composition-to-output-selection. It also reaches the optional cross-task experience path. This is a representative implemented workflow, not a supplied successful run. Sequential mode is a different scheduling policy, not an additional step in this trace. The supplied [RT-RTE-task-recursion](runtime.md#rt-rte-task-recursion) covers both modes.

The evidence is SRC-1 at the boundary's frozen revision. Focused source inspection covers `harness2/core/recursion.py` (`_accept_tree`, `_run_stage`, `run_parallel`), `harness2/core/schedule.py` (`_run_one_mode`, `run_task`) and `harness2/core/selection.py` (`_fallback`, `_persist`, `run_selection`, `trivial_selection`). These provide implementation evidence; prompt requests in the runtime baseline remain doctrine/design, not demonstrated model compliance. No observed-run or causal-experiment evidence was supplied. The account therefore establishes wiring, not successful execution, reliable selection or improvement.

### 1. Task request becomes a bounded experiment

The operator supplies benchmark/substrate, task stream, modes and k through the CLI. The scheduler owns subsequent progression; it is not a conversation in which a foreground agent freely decides the next phase. Domains can run concurrently, while each domain's tasks proceed in stream order with per-mode libraries restricted to preceding tasks. The task's shared k base executions precede refinement. Executor identity is separate from the improver/selector channels. See [RT-RTE-task-recursion](runtime.md#rt-rte-task-recursion) and [RT-RTE-solver-execution](runtime.md#rt-rte-solver-execution); SRC-1: `harness2/core/schedule.py`, `harness2/cli/run_sweep.py`.

`run_task` validates the request before delegation: k must be positive, modes distinct and supported, and selection policy finals-only. If none of the base runs has `ok` set, code writes a `base-failed` summary and returns instead of asking a model to reconstruct missing evidence. Partial base survival is sufficient to continue; this is not a requirement that every base deliver a valid answer. SRC-1: `harness2/core/schedule.py`.

> if not any(b.ok for b in base):
>     res.status = "base-failed"
>     res.errors.append("no base rollout produced anything")
>     _write_summary(summary_path, res)
>     return res
> --- `harness2/core/schedule.py`

### 2. Independent proposals return edited trees

Parallel recursion constructs 2k stage specifications: one INV and one DOM proposal for each index. Each receives the same base execution evidence, base harness and available library, with a dimension-specific mission. Code waits for all proposal results before launching the corresponding solver executions. This is phase-level fan-out/fan-in, not agents exchanging messages directly. SRC-1: `harness2/core/recursion.py`; [RT-RTE-task-recursion](runtime.md#rt-rte-task-recursion).

The handoff is a fresh filesystem evidence context, not the predecessor model's private conversation. The external proposer edits `context/harness`; code harvests those files and extracts notes from the reply. Reply prose alone cannot install an edit. The supplied baseline establishes the temporary-session lifetime and its separate audit persistence. The accepted tree is materialized for a fresh solver execution through the benchmark adapter. Solver artifacts and rendered trajectories become evidence for the next phase; the solver's external tool loop is not fully established by this repository. See [RT-RTE-edit-admission](runtime.md#rt-rte-edit-admission), [RT-RTE-solver-execution](runtime.md#rt-rte-solver-execution) and [RT-BAP-harness-consumption](runtime.md#rt-bap-harness-consumption); SRC-1: `harness2/core/proposer.py`, `harness2/core/context.py`, `harness2/core/recursion.py`.

### 3. Composition consumes the pool, not just a winning proposal

After the proposal executions complete, code constructs a pool containing each proposal label, harness directory and associated rollout. It then launches k independent AGG sessions. Each receives the bases and original base harness again, plus that pool and proposal notes or errors. Thus composition is not simply a continuation of one proposal session, and no score-based first-round winner is required. The composer chooses what changes to make; code owns admission and execution. SRC-1: `harness2/core/recursion.py`; [RT-RTE-task-recursion](runtime.md#rt-rte-task-recursion).

> pool=pool_ev,
> decisions={stage.label: stage.notes or stage.error for stage in stages},
> --- `harness2/core/recursion.py`

Each composed stage is appended to the finals list and executed. The same admission mechanism applies as for proposals. The k bases, 2k proposal executions and k composition executions account for 4k rollouts; they do not count every model call, retry, selection or reflection. A final label denotes a workflow position, not evidence that the harness changed or improved. SRC-1: `harness2/core/recursion.py`; [RT-RTE-edit-admission](runtime.md#rt-rte-edit-admission).

### 4. Verification can reject structure, not establish superiority

Code checks harvested proposals for missing workspaces, empty trees, off-surface files, tree constraints, adapter constraints and grader markers. An invalid proposal gets rejection feedback and one further stage attempt. An evidence-build failure returns the fallback immediately; transport failure ends stage attempts after the proposer's transport-retry handling. Exhausted rejection inherits a copy of the fallback tree, with error and accounting, instead of stopping the whole task. In this parallel workflow the fallback is the base tree for both proposal and composition sessions. SRC-1: `harness2/core/recursion.py`; [RT-RTE-edit-admission](runtime.md#rt-rte-edit-admission).

The rejection handoff explicitly asks the proposer to repair files:

> f"\n\n# YOUR PREVIOUS ATTEMPT WAS REJECTED\n\n{err}\n\n"
> f"Fix it in `context/harness/` and reply again."
> --- `harness2/core/recursion.py`

This gate can veto invalid structure; it neither proves a semantically good harness nor compares output quality. A fallback stage can still be executed and become a final candidate. Separately, exceptions while running one mode are recorded on the task, and the scheduler writes partial summaries before deriving the merged status. Recovery ownership remains with code, not an autonomous supervisor model. SRC-1: `harness2/core/schedule.py`, `harness2/core/recursion.py`.

### 5. Selection makes a produced artifact the delivered result

The scheduler selects among exactly the k composed finals, not the bases or all intermediate outputs. Adapter rendering filters eligible outputs. At k greater than one, the selector receives task/source evidence and anonymous candidate artifacts, not the full improver conversations. It must name a recognized anonymous ID; code parses and checks that choice. No expected-answer oracle or per-output human veto is wired into this selection path. Separate judging is downstream, not the admission test for this choice. See [RT-RTE-output-selection](runtime.md#rt-rte-output-selection); SRC-1: `harness2/core/schedule.py`, `harness2/core/selection.py`, `harness2/core/judge.py`.

The rejection path matters: an invalid selector reply or proposer failure can choose the lexicographically first surviving final, set `fallback=True` and persist its identity, but does not set `ok=True`. The scheduler consequently records selection failure and does not run reflection/library admission. A chosen label is therefore weaker than successful delivery. An empty eligible pool returns failure without such a choice. At k=1 the alternate path bypasses the selector model and delivers the single eligible final; it is not comparative verification. These distinctions are captured in [RT-RTE-output-selection](runtime.md#rt-rte-output-selection); SRC-1: `harness2/core/selection.py`, `harness2/core/schedule.py`.

Operational delivery is an existing selected benchmark output associated with a successful selection record, not a newly authored answer by the selector. Persistence failure can turn an otherwise valid choice into failed selection. The task summary retains chosen run location, harness fingerprint, selection metadata and errors. The CLI later writes the sweep record; a separate judge command may score outputs. Neither successful selection nor a summary proves task correctness. SRC-1: `harness2/core/selection.py`, `harness2/core/schedule.py`; [RT-RTE-resume-reuse](runtime.md#rt-rte-resume-reuse).

### 6. Optional retention is another handoff, not automatic deployment

If a library exists and selection succeeds, the selector channel is invoked again for reflection on the local record. Code admits experience only when required fields are present and marker checks pass; the prompt permits abstention with `NO_ENTRY`. The adopted harness and experience can then enter the same-domain/mode library for later task improvers. The library is evidence supplied to those improvers, not an automatic replacement of every later solver harness. Later behavioral effect still requires a subsequent admitted tree and solver execution. See [RT-RTE-experience-admission](runtime.md#rt-rte-experience-admission) and [RT-BAP-harness-consumption](runtime.md#rt-bap-harness-consumption); SRC-1: `harness2/core/schedule.py`, `harness2/core/selection.py`, `harness2/core/library.py`.

This closes the implemented task-to-later-task handoff, but not an empirical improvement claim. The frozen source supplies no generated candidate, retained lesson or later execution establishing that a particular criticism was valid, used or beneficial. Resume can reuse successful summaries and reconstruct library state under integrity predicates; that is recovery wiring, not independent validation of the original choice. See [RT-RTE-resume-reuse](runtime.md#rt-rte-resume-reuse).

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

#### On [RT-RTE-task-recursion](runtime.md#rt-rte-task-recursion)

Workflow role: phase coordinator for the selected parallel task. The consequential barrier is completion of proposal stages and their rollouts before independent composers receive the whole proposal pool. Code, not a peer agent, owns fan-in and next-phase launch.

#### On [RT-RTE-edit-admission](runtime.md#rt-rte-edit-admission)

Workflow verification role: structural veto with repair feedback. Exhausted rejection preserves workflow continuity through inherited harness execution; it does not establish a newly authored refinement. In the selected parallel path, composition falls back to the original base rather than to a winning proposal.

#### On [RT-RTE-output-selection](runtime.md#rt-rte-output-selection)

Workflow delivery role: promote an eligible produced output into the selected run record. Distinguish a valid persisted selection from a fallback label on a failed selection. The latter does not authorize the subsequent reflection/retention handoff.
