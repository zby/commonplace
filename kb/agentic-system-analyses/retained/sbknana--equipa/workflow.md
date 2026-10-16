---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "EQUIPA workflow: one Git task through developer/tester iteration, security review, merge admission and recorded delivery."
run-id: AAS-2026-10-15-equipa-32016e8dd9ae-01
reviewed-boundary: fa8f41a6948584ee53e804edbb08b7449d05cd14
---

# EQUIPA workflow report

## Workflow account

### Selected path and evidence

The representative workflow is `python -m equipa --task <id> --dev-test --yes` for a Git project. It is selected because the shipped CLI connects a concrete operator request to developer/tester iteration and then to a separate product-admission decision. It exposes both retry and rejection without joining unrelated capabilities. The account follows the existing [RT-RTE-dev-test](runtime.md#rt-rte-dev-test) and [RT-RTE-gated-merge](runtime.md#rt-rte-gated-merge), rather than declaring another identity for their composition.

All evidence is SRC-1 implementation at the revision in [boundary.md](boundary.md). Additional detailed inspection covered task-mode helpers in `equipa/cli.py`, cycle handoffs and tester-failure handling in `equipa/loops.py`, and `review_task_branch` and `run_task_in_isolation` in `equipa/dispatch.py`. No target program, test, model call or example was executed. This is an implemented workflow, not an observed completed task; project/database state and actual enabled settings are unavailable.

### Request becomes an execution frame

The CLI resolves the task, project directory and project context. Dry-run stops before dispatch; otherwise the operator confirms unless `--yes` supplies launch authorization. This is not human approval of subsequent code or review findings. For the selected Git path, `_run_task_isolated` passes a callback into `run_task_in_isolation`; the callback invokes `_run_dev_test_mode` in the assigned worktree with the task branch identity. SRC-1, `equipa/cli.py`.

> if args.dev_test:
>     return await _run_dev_test_mode(
>         task, worktree_dir, project_context, args, task_branch=task_branch,
>     )
> --- `equipa/cli.py`

Dispatch pins the default branch, refuses an already-tripped guard or unusable worktree, and creates `forge-task-<id>`. It supplies the callback with the task worktree's project subdirectory, not the stable project checkout as the agent's working directory. Branch identity and guard checks remain the orchestrator's responsibility after the callback returns. A worktree separates product candidates; it is not itself OS confinement. The conditional separate-user launcher and its host contracts are assessed in [RT-RTE-isolated-agent](runtime.md#rt-rte-isolated-agent), not assumed enabled here. SRC-1, `equipa/dispatch.py`.

### Developer to tester to another developer

The Python loop owns phase transitions and budgets. Each developer invocation gets assembled role/task/project instructions and selected extra context. Before dispatch, code reads inter-agent messages for the task role and marks them read. It constructs extra context from compaction history under the configured policy; plugin `pre_cycle` returns can add text. The model owns tool/action choice inside that invocation, not whether a tester or merge gate runs next. See [RT-RTE-dev-test](runtime.md#rt-rte-dev-test) for the baseline prompt and termination evidence. SRC-1, `equipa/loops.py`.

The tester is a separate invocation with its own role prompt, task/project context and a captured Git diff against the prior cycle's HEAD. It sees product state and selected change context, not the developer's entire conversation. The prior-cycle SHA advances after a continuing cycle, so later tester prompts need not repeat all earlier diffs. The task worktree remains the shared product substrate. SRC-1, `equipa/loops.py`.

> tester_extra_context = await _capture_git_diff_context(
>     project_dir, cycle, output, base_ref=prev_cycle_sha,
> )
> --- `equipa/loops.py`

Tester output is compacted into history and parsed from `result_text`. The code then routes the parsed outcome; it does not accept the tester's subprocess success flag as sufficient product acceptance. A reported pass faces count/skip consistency checks described in [RT-RTE-dev-test](runtime.md#rt-rte-dev-test). Project tests could provide executable expectations, but their actual execution, validity and coverage are not supplied evidence. Model judgment is not an independent answer oracle.

For the inspected failure path, the tester's parsed failures become a task/role-addressed message. The payload includes counts and at most five failure details; a separate failure context enters compaction history. The loop continues, and the next developer phase reads messages again. Thus a failed test can shape another proposal without transporting the entire tester frame. History inclusion remains conditional on the context policy; the message channel is separately explicit. SRC-1, `equipa/loops.py`.

> post_agent_message(task_id, cycle, "tester", task_role,
>                    "test_failures", msg_content)
> --- `equipa/loops.py`

> failure_context = build_test_failure_context(test_results, cycle)
> compaction_history.append(failure_context)
> return "continue_loop", None, None
> --- `equipa/loops.py`

Recovery ownership is bounded. Code schedules another developer cycle; the developer must propose a repair. Cost/progress/turn limits and cycle exhaustion can terminate rather than repair the task. Sustained tester overload returns an overload outcome instead of accepting untested work. Optional CLI autoresearch retries surround the cycle loop and can reset a failed attempt using captured reflections; they are feature-dependent, not an unconditional guarantee of eventual completion. SRC-1, `equipa/loops.py`, `equipa/cli.py`; [RT-RTE-dev-test](runtime.md#rt-rte-dev-test).

### Candidate acceptance is not delivery

The cycle loop's `tests_passed` or `no_tests` result is only merge eligibility. The latter is an explicit route without established passing tests; the runtime also documents audit and no-change shortcuts. The selected ordinary code-change path therefore cannot support a universal claim that every delivered task passed an independent test suite. SRC-1, `equipa/loops.py`, `equipa/dispatch.py`; [RT-RTE-dev-test](runtime.md#rt-rte-dev-test).

After execution, dispatch checks that the worktree still uses the assigned branch and verifies the default-branch guard. A clean unchanged branch can be a no-op. An unchanged branch with uncommitted work instead yields merge failure, preserving that work rather than treating it as delivered. Changed merge-eligible work proceeds to security review, unless the review policy is disabled or the diff is doc-only. SRC-1, `equipa/dispatch.py`.

The reviewer runs against task state, while its artifact is persisted/read at the stable project directory. Submodule-pointer changes are explicitly added to the task description supplied for review. The reviewer proposes findings; software decides whether those findings and the run provenance admit a merge. A crash, run failure or sustained overload blocks this path. CRITICAL/HIGH counts block; missing-artifact blocking depends on policy. No per-finding human approval is shown. SRC-1, `equipa/dispatch.py`; [RT-RTE-gated-merge](runtime.md#rt-rte-gated-merge).

> failure = reviewer_run_failure(task_id)
> if failure is not None:
> --- `equipa/dispatch.py`

> if review_crashed:
>     log(
>         f"[Task #{task_id}] SECURITY GATE: blocking merge — security "
>         f"review crashed; branch {branch} left unmerged for operator "
>         f"review.",
>         output,
>     )
>     return "security_review_blocked", True
> --- `equipa/dispatch.py`

This is a rejection boundary, not an automatic reviewer-to-developer repair cycle. The inspected wrapper leaves rejected candidate branches for operator resolution. `_gated_merge_task` then applies the separate actual-diff, provenance, pinned-commit and guard protocol documented in [RT-RTE-gated-merge](runtime.md#rt-rte-gated-merge). A reviewer verdict does not independently prove security; a valid review artifact alone does not establish that its candidate was merged.

### Delivery and retained failure

For a changed Git product, delivery means admission onto the default branch, followed by merge-reconciled status and telemetry. `run_task_in_isolation` returns an `IsolatedTaskRun` containing the reconciled outcome, original agent outcome, result, cycles, optional merged SHA and reason. The CLI records the reconciled outcome, not simply the inner tester verdict. SRC-1, `equipa/dispatch.py`, `equipa/cli.py`.

> await _record_task_telemetry(
>     task, isolated.result, isolated.outcome, isolated.cycles, args,
>     merged_sha=isolated.merged_sha,
> )
> --- `equipa/cli.py`

Clean no-op work is a distinct terminal case with no new merge. Failed/unmerged candidates retain their branch; cleanup can stash uncommitted work. A retained failed branch refuses redispatch until the operator resolves it. A tripped guard keeps candidate state and obstructs subsequent merges. This preserves evidence/work but does not implement autonomous resolution of every rejection. SRC-1, `equipa/dispatch.py`; [RT-OBJ-task-branch](runtime.md#rt-obj-task-branch).

The source establishes connected delegation, bounded corrective feedback and separate product admission. It does not establish a successful run, guaranteed test completeness, deployed containment or eventual delivery. Non-Git tasks, goal planning and prompt-improvement pipelines are separate paths; this trace does not generalize its branch-level delivery criterion to their other effects.

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

#### On [RT-RTE-dev-test](runtime.md#rt-rte-dev-test)

Workflow role: the task callback delegates bounded implementation and checking, not final landing authority. Corrective handoff: a parsed tester failure posts a role-addressed message and appends failure context, then a later developer invocation may act on it. The frame boundary passes selected task/product/diff/summary material rather than a complete shared conversation. Retry is a protocol, not evidence of a repaired product.

#### On [RT-RTE-gated-merge](runtime.md#rt-rte-gated-merge)

Workflow role: independent admission after cycle-level acceptance. Rejection recovery belongs to the operator for retained branches, rather than a demonstrated automatic security-fix loop. Completion handoff: the wrapper returns merge-reconciled outcome/SHA to CLI telemetry. No-op is terminal without a new commit; changed work must reach the default branch before being represented as delivered.
