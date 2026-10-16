---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Hyperagents workflow: one paper-review code-editing generation, staged verification, failure handling and delivery into the next lineage."
run-id: AAS-2026-10-14-hyperagents-dd9d501b160c-01
reviewed-boundary: "59a68f672dfb92c74aeb7e61535d776fb36e172d"
---

# Hyperagents workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a normal paper-review generation with the initial editor, agent optimization, staged evaluation and host parent selection enabled. It connects an operator's generation request to edited code, benchmark predictions, recorded scores and a possible next-generation lineage. It was selected because the shipped driver, editor, task caller and report implement this chain together; it is not an assembly of unrelated capabilities. This is an implementation trace, not a successful run. The frozen source has no observed-run layer, so neither actual archive inspection by the model nor successful recovery, deployment or improvement is established ([boundary](boundary.md); SRC-1, `generate_loop.py`, `meta_agent.py`, `domains/harness.py`, `domains/report.py`).

The canonical referents already exist in [RT-RTE-generation-cycle](runtime.md#rt-rte-generation-cycle), [RT-RTE-editor-admission](runtime.md#rt-rte-editor-admission), [RT-RTE-task-evaluation](runtime.md#rt-rte-task-evaluation) and [RT-RTE-parent-selection](runtime.md#rt-rte-parent-selection). This member adds workflow findings as annotations rather than redeclaring them. Inspection for this account covered `generate_loop.py`'s generation, evaluation/copy and outer completion blocks; `meta_agent.py`; `run_meta_agent.py`; the loading, worker and persistence blocks of `domains/harness.py`; the normalization/scoring block of `domains/report.py`; `domains/paper_review/utils.py`; and `task_agent.py`. All are implementation evidence under SRC-1 at the unchanged pin; no additional source or target execution was introduced.

### Request and first delegation: host to inherited editor

The operator chooses the domain, generation budget and modes. The host schedules generations, identifies a parent, prepares the root and reconstructs that parent's executable lineage. Bootstrap depends on previously prepared initial evaluations; resume reads saved archive/root state. These responsibilities belong to the shipped host, not to an autonomous model scheduler ([RT-RTE-generation-cycle](runtime.md#rt-rte-generation-cycle); SRC-1, `generate_loop.py`, `utils/gl_utils.py`).

For the selected ordinary route, `generate` creates the generation output directory and metadata, starts a container, applies the parent's ordered patch list and copies past generation outputs into `/tmp/`. The normal copy helper removes the current generation, validation/test-named artifacts, repository copies and bytecode. The copied material is therefore a filtered filesystem view, not the complete evaluation archive. The prune command results are not individually checked in the inspected loop, so the intended exclusion is not a verified execution outcome. The editor's repository is writable; containerization does not make the change process a transaction or establish security containment (SRC-1, `generate_loop.py`; [RT-RTE-editor-admission](runtime.md#rt-rte-editor-admission)).

The host launches `run_meta_agent.py` with repository path, evaluation-folder path, base commit, chat-log path, diff-output directory and remaining iterations. The initial `MetaAgent.forward` accepts the evaluation path and remaining budget but does not put either into its instruction. Its prompt asks only to modify the repository, and its model history starts empty. Past results and generated README guidance are available for tool-mediated discovery, not proven model inputs or actual reasons for the changes (SRC-1, `generate_loop.py`, `run_meta_agent.py`, `meta_agent.py`; [RT-OBJ-readme](runtime.md#rt-obj-readme)).

The model proposes edits through the textual tool loop. Python owns call parsing, dispatch and the call bound; the model chooses calls and content. Bash and file-edit tools execute within the process-visible environment. No separate reviewer agent or per-change human approval occurs in this route. The history returned by the helper is not a verification certificate: the initial meta-agent itself has no explicit return value, and the runner delivers the edited filesystem as a saved diff ([RT-RTE-model-tools](runtime.md#rt-rte-model-tools), [RT-RTE-editor-admission](runtime.md#rt-rte-editor-admission); SRC-1, `meta_agent.py`, `run_meta_agent.py`).

### Editor return and second delegation: host to task workers

After the editor returns, the runner attempts to reset `domains/` and saves `model_patch.diff` relative to the reconstructed base. The host copies editor artifacts out, requires a nonempty diff for ordinary evaluation, and runs import checks. These are eligibility checks for attempting evaluation, not checks that the proposed code is correct, improves the parent, or preserves all evaluator dependencies. The domain reset happens after editing, and dependencies outside that directory remain mutable ([RT-OBJ-model-patch](runtime.md#rt-obj-model-patch), [RT-RTE-editor-admission](runtime.md#rt-rte-editor-admission); SRC-1, `run_meta_agent.py`, `generate_loop.py`).

The host next launches `domains.harness` against the edited `task_agent.py`, passing domain, subset, sample count, worker count and output/run identifiers. It launches `domains.report` after the harness and copies predictions, task logs and reports to the generation directory. These subprocesses are bounded by the host's timeout commands; those controls do not apply universally to direct runner or harness invocations ([RT-RTE-task-evaluation](runtime.md#rt-rte-task-evaluation); SRC-1, `generate_loop.py`).

The harness loads the edited `TaskAgent` class and submits dataset rows to worker futures. Each row receives a fresh task-agent instance and row-specific chat-log path. For paper review, the formatter supplies `domain` and `paper_text`, excluding the `outcome` label. The shipped initial task agent starts with an empty model history, asks for a JSON `response`, and returns prediction plus history. Its helper has no initial tool grant; edited code may change that behavior. The worker returns only the prediction to the harness, while logs escape separately to disk (SRC-1, `domains/harness.py`, `domains/paper_review/utils.py`, `task_agent.py`; [RT-RTE-task-evaluation](runtime.md#rt-rte-task-evaluation)).

### Verification, rejection and recovery

The answer oracle is the dataset's outcome label, not the editor's assessment. The report strips and lowercases prediction/label strings, compares them and derives accuracy. This establishes a scoring rule, not correctness of the reference labels or robustness against arbitrary generated Python. The staged gate permits fuller evaluation when every selected domain score is present and positive; with one paper-review domain, this is a positive-score gate, not improvement over the parent. An operator can skip staged evaluation (SRC-1, `domains/report.py`, `domains/paper_review/utils.py`, `generate_loop.py`; [RT-RTE-task-evaluation](runtime.md#rt-rte-task-evaluation)).

Full evaluation reuses the same split output locations. The harness reloads existing non-NA predictions and skips those rows, so the staged-to-full handoff extends saved predictions rather than necessarily rerunning the entire subset. Periodic checkpoints and final CSV writes preserve completed answers; an exception from `future.result()` prevents the normal final save, so the most recent uncheckpointed results are not guaranteed retained. This is row-level reuse, not a demonstrated recovery episode (SRC-1, `generate_loop.py`, `domains/harness.py`).

The rejection path is explicit. An empty diff suppresses ordinary task evaluation. A nonpositive or missing staged score suppresses fuller evaluation without necessarily setting `run_eval` false. An exception caught by `generate` sets `run_eval` false. The host then attempts root reset, untracked-file cleanup and container cleanup before saving metadata. Because the cleanup calls themselves can fail, this is best-effort restoration, not unconditional continuation after every failure ([RT-RTE-editor-admission](runtime.md#rt-rte-editor-admission); SRC-1, `generate_loop.py`).

> except Exception as e:
>     safe_log(f"Error in generate: {e}")
>     metadata["run_eval"] = False
> --- `generate_loop.py`

When generation processing returns normally to the outer loop, the host appends its ID even if it failed eligibility. A failed parent editor causes the parent's `valid_parent` flag to be cleared. The host selector can exclude ordinary ineligible nodes, but its starting-node exception and first-node fallback prevent a universal successful-evaluation prerequisite. Also, the `meta_patch_files is not None` branch in eligibility admits more than successful score loading; the runtime identifies the CLI's empty-list default. Archive append, candidate eligibility and score-based successor choice are distinct decisions ([RT-OBJ-metadata](runtime.md#rt-obj-metadata), [RT-RTE-parent-selection](runtime.md#rt-rte-parent-selection); SRC-1, `generate_loop.py`, `utils/gl_utils.py`).

### Delivery and next-round authority

The delivered generation product is the persisted diff, editor log, available task predictions/reports and control metadata, with its ID added to the archive. It is not a deployed winning agent. After plotting, the host selects a next parent; the next generation can replay that parent's saved patch list into executable code. Thus delivery has two different recipients: retained artifacts for inspection and an executable lineage for later task/editor invocation. Filesystem delivery of past scores does not establish that a later model reads or responds to them ([RT-BAP-code-replay](runtime.md#rt-bap-code-replay), [RT-RTE-parent-selection](runtime.md#rt-rte-parent-selection); SRC-1, `generate_loop.py`, `utils/gl_utils.py`).

> archive = update_and_save_archive(output_dir, archive, new_node=current_genid)
> --- `generate_loop.py`

After the scheduled loop, `generate_loop` returns the output directory. This defines completion of the shipped driver path, not proof that every generation succeeded. Plotting and selection lie outside `generate`'s local exception handler; the inspected local recovery mechanism therefore does not promise whole-run recovery from their failures. Optional inherited selection/ensemble execution is an alternate workflow covered by [RT-RTE-optional-consumers](runtime.md#rt-rte-optional-consumers), not a necessary stage in this selected ordinary workflow (SRC-1, `generate_loop.py`).

> # Return output dir
> return output_dir
> --- `generate_loop.py`

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

#### On [RT-RTE-generation-cycle](runtime.md#rt-rte-generation-cycle)

Workflow selection: ordinary paper-review generation with host selection and staged evaluation. Delivery is archive/artifact retention followed by a possible next-parent replay; terminal delivery is an output-directory path. Local generation failure handling does not enclose later plotting and parent selection. These distinctions bound what “through to delivery” establishes (SRC-1, `generate_loop.py`).

#### On [RT-RTE-editor-admission](runtime.md#rt-rte-editor-admission)

Handoff distinction: the runner supplies evaluation-path and remaining-budget arguments, but the initial editor prompt does not use them. Nonempty diff/import checks admit an attempt at task evaluation, not a correct or improved agent. A caught generation exception disables evaluation; attempted cleanup precedes metadata save, so cleanup failure can prevent normal handoff to archive append (SRC-1, `generate_loop.py`, `meta_agent.py`, `run_meta_agent.py`).

#### On [RT-RTE-task-evaluation](runtime.md#rt-rte-task-evaluation)

Staged-to-full handoff: repeated split output locations and existing-prediction skipping extend the saved prediction table. Row futures return predictions to the harness; task histories are separately logged rather than returned into the caller's model context. Checkpoint writes preserve partial progress, but future exceptions can bypass the final CSV write. Oracle and admission remain separate: normalized label accuracy gates fuller evaluation only for present positive staged scores, with an explicit skip mode (SRC-1, `generate_loop.py`, `domains/harness.py`, `domains/report.py`, `domains/paper_review/utils.py`).

#### On [RT-RTE-parent-selection](runtime.md#rt-rte-parent-selection)

Recovery owner: the host invalidates a failed editor parent and chooses another candidate through its selection policy, subject to starting-node exceptions and fallback. This is implemented lineage redirection, not an observed retry that produced a successful result. Neither selecting a successor nor archiving the failed child certifies improvement (SRC-1, `generate_loop.py`, `utils/gl_utils.py`).
