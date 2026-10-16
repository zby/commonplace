---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "SkillLift workflow account: one WildClaw task portfolio from caller settings through model proposals, benchmark selection, recovery and frozen-result delivery."
run-id: AAS-2026-10-14-skilllift-0f350bf64418-01
reviewed-boundary: "599358b4d4c4a27c0e004df8228ab93026600653"
---

# SkillLift workflow report

## Workflow account

### Selection and evidence limits

The representative workflow is the shipped **WildClaw single-task portfolio improvement path**. It connects a caller request to model-generated edits, verifier-only refinement, benchmark-backed successor selection, receipt calibration and durable output. It was selected because these steps share one coordinator and store; this is not a workflow assembled from independent capabilities. The separate category and tau2 drivers are not stages of this workflow. See [RT-RTE-task-evolution](runtime.md#rt-rte-task-evolution) and the [boundary](boundary.md#boundary-and-evidence).

All source evidence is SRC-1 at the frozen revision. This member directly inspects `skilllift_eval/runners/skilllift_wildclaw.py` (runner construction and result emission), `skilllift/skilllift/coordinator/task.py` (entry, preparation, logical-cell recovery and finalization), `skilllift/skilllift/coordinator/modes.py` (round sequencing, handoffs, refinement and calibration), and `skilllift/skilllift/adapters/wildclawbench.py` (evaluation, recovery and result admission). These are implementation evidence; direct inspection deepens the runtime baseline's coverage rather than adding a source. No target execution occurred. Unavailable benchmark submodules, graders and host internals prevent verification of actual task execution, skill compliance and reward correctness. Code-supported delivery below means artifact production and return, not observed successful operation.

### Request, initialization and delegation

1. **Caller to runner.** The CLI dispatch described by [RT-RTE-task-evolution](runtime.md#rt-rte-task-evolution) reaches `SkillLiftWildClawRunner.run`. Caller settings supply the task filter, endpoint, run root, configuration fingerprints and algorithm parameters. The runner resolves the task and constructs the adapter, store and model roles. Its settings factory transfers benchmark controls and identity fields to each trial. The ordinary construction uses rubricator/planner, bounded-edit generator and verifier clients; constructor-injected roles are alternatives, not separate autonomous workers. The runner calls `evolve(task_id)` synchronously. SRC-1: `skilllift_eval/runners/skilllift_wildclaw.py`; [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client).

2. **Coordinator to adapter/store.** The coordinator requests the public task, seed portfolio and reward policy, checks task identity, fingerprints its configuration and reconstructs any accepted parent. An anchor evaluation establishes the initial reward unless state already supplies it. An invalid anchor freezes the current parent and returns an indeterminate result. A terminal seed with no accepted changes freezes and returns without final trials. These are early deliveries, not successful adaptation. SRC-1: `skilllift/skilllift/coordinator/task.py`; [RT-RTE-task-evolution](runtime.md#rt-rte-task-evolution).

3. **Coordinator to planner/editor.** For a nonterminal evolving task, the coordinator loads or generates the receipt and scores the pre-round champion. A new plan receives the public task, current parent, previous plan, scalar history, direction history and prohibited novelty keys. Champion verifier feedback is supplied when the planner interface accepts it. Directions are bounded by the candidate limit. Each draft request gives the editor one direction and parent; the returned diff passes the portfolio patch gate before it becomes a valid branch. Persisted candidates can instead be replayed, with direction equality checked. SRC-1: `skilllift/skilllift/coordinator/modes.py`, `skilllift/skilllift/coordinator/task.py`. The patch gate and bounded editor's selected-file context are established in [RT-RTE-task-evolution](runtime.md#rt-rte-task-evolution) and [RT-RTE-branch-refinement](runtime.md#rt-rte-branch-refinement).

These model handoffs carry explicit inputs, not a shared benchmark-agent conversation. The planner proposes directions; the editor proposes patches; code owns scheduling and rejection. Caller configuration is not per-candidate human approval. The benchmark agent receives the materialized skill portfolio through a downstream loading channel, not necessarily the optimizer's plan, feedback or history; [RT-BAP-skill-delivery](runtime.md#rt-bap-skill-delivery) bounds that authority claim.

### Refinement, verification and successor decision

4. **Mode A: branch-local refinement.** Each valid branch is scored against the receipt. Below the configured verifier threshold and within the iteration budget, the coordinator supplies branch-local criterion hits through a refined direction to the editor. It applies the returned patch against the current branch and rescores. A patch failure, missing score or score decline ends refinement while retaining the previous branch; a nondecreasing score admits the refined tree. There are no benchmark calls inside this method. A higher verifier score is local rubric judgment, not a demonstrated task improvement. SRC-1: `skilllift/skilllift/coordinator/modes.py`; [RT-RTE-branch-refinement](runtime.md#rt-rte-branch-refinement), [RT-CLM-mode-a](runtime.md#rt-clm-mode-a).

5. **Coordinator to benchmark adapter.** Only branches with a portfolio enter candidate evaluation. The adapter receives task identity, candidate root/hash and trial identity. Although the coordinator can dispatch candidate evaluations through concurrency, the WildClaw adapter locks around its runner call. Returned records must identify the task and portfolio, report a successful result, match configuration fields, point to artifacts inside the trial root and carry a matching loader-manifest hash. The adapter then extracts a numeric benchmark reward and writes a trial marker. These checks authenticate artifact association under the receipt-producer contract; they do not prove grader correctness or actual model-visible compliance. SRC-1: `skilllift/skilllift/adapters/wildclawbench.py`; [RT-RTE-cell-recovery](runtime.md#rt-rte-cell-recovery).

6. **Successor selection.** Invalid evaluations are excluded. The selector considers competitive candidates and verifier scores; promotion requires either improved benchmark reward or equal reward with a strictly higher available verifier score than the champion. Otherwise the parent remains and the no-improvement count increases. Acceptance records the candidate's round and ID, not a new human approval. The benchmark reward is the reference outcome; the verifier is a secondary selector, not the answer oracle. SRC-1: `skilllift/skilllift/coordinator/modes.py`; [RT-RTE-task-evolution](runtime.md#rt-rte-task-evolution).

7. **Mode B: revise scoring guidance, not the selected winner.** After the successor decision, the coordinator compares the *pre-round* champion and valid evaluated candidates under existing benchmark rewards. It rescores their content, computes tie-aware alignment and criterion contrast, and can ask the rubricator to revise the receipt. Fewer than two usable portfolios or common scores prevents calibration. The best tested alignment is retained; receipt revision failure preserves the best seen receipt. This changes later verifier input, not the round's already-decided successor. Receipt validation, revision guidance and independently qualified theory properties belong to [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision). SRC-1: `skilllift/skilllift/coordinator/modes.py`.

### Rejection, recovery and delivery

An invalid initial patch is recorded with its failure kind and produces no portfolio; it cannot enter benchmark evaluation. A rejected refinement leaves the last admissible branch. A candidate with valid but insufficient reward remains in history without replacing the parent. After the round, rejected or unevaluated branches contribute prohibited novelty keys. All-invalid candidates, terminal accepted reward, two no-improvement rounds or the round budget can stop evolution. Context preflight can also stop before planning or during calibration. These are different failure/stop mechanisms, not one universal rollback guarantee. SRC-1: `skilllift/skilllift/coordinator/task.py`, `skilllift/skilllift/coordinator/modes.py`; the acceptance and refinement passages in [RT-RTE-task-evolution](runtime.md#rt-rte-task-evolution) and [RT-RTE-branch-refinement](runtime.md#rt-rte-branch-refinement) support their gates.

At the evaluation boundary, the coordinator owns recovery: it first reloads a matching logical-cell result, then asks the adapter to recover started physical attempts, then creates new attempts if needed. Valid rewards close the logical cell. Infrastructure failures trip a consecutive-failure fuse without permanently closing it; attempt markers remain. This does not guarantee exactly-once remote effects or automatic reconsideration of every stopped workflow. Task status and persisted candidate records still govern which cells a later `evolve` invocation reaches. SRC-1: `skilllift/skilllift/coordinator/task.py`; [RT-RTE-cell-recovery](runtime.md#rt-rte-cell-recovery).

Recovery also has a concrete content-identity limit: accepted Mode A refinements retain the original candidate record, while parent reconstruction reapplies that record's original patch. When an actually changed refined tree is accepted, replay need not reproduce the evaluated tree. [RT-CLM-refinement-replay](runtime.md#rt-clm-refinement-replay) retains the relevant source passages. This is an implementation risk, not an observed failure; it prevents claiming resume-stable delivery of every refined successor.

Ordinary completion freezes the parent and submits exactly two final logical trials. Only valid final rewards contribute to the reported maximum; no valid final reward yields null. This score is a reporting rule, not a guarantee that the chosen portfolio generalizes or beats the anchor. SRC-1: `skilllift/skilllift/coordinator/task.py`.

> final_score = max(final_rewards) if final_rewards else None
> --- `skilllift/skilllift/coordinator/task.py`

The result is delivered when the coordinator returns the frozen-portfolio result and the runner writes its summary and committed task records, then returns its result object. Early anchor exits still produce runner summaries but omit the ordinary final-trial stage. The downstream instruction channel remains a separate, unobserved activation question. SRC-1: `skilllift_eval/runners/skilllift_wildclaw.py`; [RT-BAP-skill-delivery](runtime.md#rt-bap-skill-delivery).

> summary = _cell_summary(settings, result, records, task_path)
> _write_json(settings.run_root / "cell_summary.json", summary)
> _write_json(settings.run_root / "task_run_records.json", [record.to_dict() for record in records])
> return SkillLiftWildClawRunResult(records, summary, resume)
> --- `skilllift_eval/runners/skilllift_wildclaw.py`

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

#### On [RT-RTE-task-evolution](runtime.md#rt-rte-task-evolution)

Workflow selection: the WildClaw task path is representative because the shipped runner joins proposal, verification, benchmark comparison, receipt calibration and final artifact emission under one coordinator. The category and domain routes are separate alternatives, not hidden steps in this trace.

Handoff responsibility: the runner supplies task/configuration and clients; the coordinator retains next-step ownership; models return directions, edits and judgments; the adapter returns admitted benchmark evaluations. Model roles are explicit requests rather than independently scheduling agents. Final delivery includes runner-written summary/records after the coordinator returns; early anchor exits bypass ordinary final trials.

#### On [RT-RTE-branch-refinement](runtime.md#rt-rte-branch-refinement)

Workflow rollback boundary: refinement rejection retains the current branch, while initial-patch rejection leaves no evaluable portfolio. Nondecreasing verifier score admits a refinement locally, but benchmark acceptance happens later. Recovery cannot be characterized as a universally faithful rollback/replay protocol given the separately retained refinement-record mismatch.

#### On [RT-RTE-receipt-revision](runtime.md#rt-rte-receipt-revision)

Workflow ordering: calibration follows successor selection and receives the pre-round champion plus evaluated candidates. Its retained result guides subsequent scoring; it does not reselect the current winner. Insufficient calibration evidence or failed revision can preserve an existing receipt without invalidating a benchmark-admitted successor.

#### On [RT-RTE-cell-recovery](runtime.md#rt-rte-cell-recovery)

Workflow recovery scope: coordinator recovery operates on a logical evaluation reached by control flow; adapter recovery authenticates associated artifacts before supplying reward. A retryable cell is not a guarantee that a completed or stopped task automatically reopens earlier candidate decisions. Physical calls may repeat while logical results are reused.
