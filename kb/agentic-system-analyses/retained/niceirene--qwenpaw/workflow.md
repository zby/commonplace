---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "QwenPaw workflow: foreground forked project work from parent request through child handoff, Git finalization and returned branch."
run-id: AAS-2026-10-15-qwenpaw-e41495d47fc0-01
reviewed-boundary: "16b2e712d198166c9359e77055b13bf2668bf5ae"
---

# QwenPaw workflow report

## Workflow account

### Selected workflow and evidence boundary

This account selects foreground `spawn_subagent(fork=True)` project work. It joins a source-supported request, separate worker session, project worktree, finalization check and parent-facing result. It is more informative about coordination than an ordinary single reply because child completion and project integration are separate milestones. The outer native invocation is [RT-RTE-native-turn](runtime.md#rt-rte-native-turn); the delegated route is [RT-RTE-fork-worker](runtime.md#rt-rte-fork-worker). This report adds inspection of the fork endpoint, response collector and finalizer, rather than treating the runtime baseline's references to success or merge readiness as content verification.

All findings concern SRC-1 at the revision in [the boundary](boundary.md). Newly inspected implementation is `src/qwenpaw/app/routers/fork.py`, `src/qwenpaw/agents/tools/agent_management.py` (request assembly, fork dispatch, collection and formatting), and selected protocol, commit and finalization functions in `src/qwenpaw/agents/fork_project.py`. No target code or tests were executed. No observed run was supplied. The workflow is wired; successful work, model compliance and delivered product quality remain unobserved.

### Request, delegation and worker inputs

The native parent receives a user request through the ordinary route. Its model can propose delegated work with a task string and optional tool/skill restrictions. The fork dispatcher takes current agent, parent session, user and channel identities into a localhost fork API call. The endpoint reads the parent's **saved session file**, writes that state to a new `sub-` session, and optionally creates a Git worktree and branch. Missing/unreadable session files yield empty state. Thus a fork does not establish a copy of the parent's latest in-memory deliberation. The state reader and fork endpoint provide this distinction (SRC-1, `src/qwenpaw/app/routers/fork.py`).

> state = _read_session_state(parent_file)
> --- `src/qwenpaw/app/routers/fork.py`

> if not session_file.exists():
>     return {}
> --- `src/qwenpaw/app/routers/fork.py`

The dispatcher registers a created worktree for scoped tracking; registration failure aborts dispatch. It supplies the worker session ID, user/channel identities and a user-message task. Request context supplies the worktree directory through both fork and ACP metadata, branch and scope identifiers, optional allowed tools and skills, and an optional configured subagent model override. The target agent identity remains the current agent; the session and project location change. The ordinary builder's filtering and session restoration are established in [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) and [RT-OBJ-session-state](runtime.md#rt-obj-session-state).

Worktree tasks receive an injected commit protocol. This is instruction to the worker, not proof that the worker followed it. Code finalization provides a separate fallback for dirty changes. The protocol explicitly allows task-specified absolute output paths outside the worktree, so directory rebinding is not a general confinement guarantee (SRC-1, `src/qwenpaw/agents/fork_project.py`).

> Uncommitted worktree changes cannot be merged into the main branch.
> If the task asks you to write under an absolute path outside this
> worktree (e.g. a workflow results dir), use that absolute path as given.
> --- `src/qwenpaw/agents/fork_project.py`

The parent tool delegates through `/console/chat` with the target agent header. QwenPaw owns request assembly, session routing and collection; the child's model/runtime owns its internal action sequence. The parent does not receive the entire evolving child window. It gets formatted final collected text with a session marker and, conditionally, a branch marker. Context isolation therefore resembles a separate call frame only loosely: it inherits saved context and can leave durable project effects, rather than discarding everything except a pure return value (SRC-1, `src/qwenpaw/agents/tools/agent_management.py`; [RT-RTE-fork-worker](runtime.md#rt-rte-fork-worker)).

### Verification is administrative, not a product oracle

The foreground collector retains the last parsed non-usage SSE payload. The spawn path tests whether `response_data` is truthy before finalization. Neither check establishes a correct answer, completed requested edits or passing tests. In particular, the nearby comment about a successful worker response is stronger than the executable predicate. This limits the baseline's success terminology to received payload plus finalization, not independently verified task success (SRC-1, `src/qwenpaw/agents/tools/agent_management.py`).

> if parsed and parsed.get("type") != "turn_usage":
>     response_data = parsed
> --- `src/qwenpaw/agents/tools/agent_management.py:300-326`

> finalize_ok = False
> if worktree_path and response_data:
> --- `src/qwenpaw/agents/tools/agent_management.py`

The narrower finalization mechanism is [WF-RTE-fork-finalization](#wf-rte-fork-finalization). It checks registry/scope ownership, coordinates concurrent finalizers and stages/commits dirty files. It does not compare the work to an expected answer. A clean worktree can return success without a new commit. Accordingly the result can become administratively finalized even when this invocation produced no changes. Human content review is not established by these checks; the parent model is also not an answer oracle.

### Rejection, recovery and delivery

Fork API failure returns a tool error. A failed worktree registration aborts the spawn. No collected response marks a worktree fork failed and returns a no-response message. With a response but failed finalization, the parent receives text plus `FORK_FINALIZE_FAILED` and guidance to rerun before merging. Exceptions in finalization mark failure and re-raise. These mechanisms preserve failure information; they do not establish automatic repair of the child's task (SRC-1, `src/qwenpaw/agents/tools/agent_management.py`, `src/qwenpaw/agents/fork_project.py`).

For foreground work, successful finalization adds `FORK_BRANCH` and leaves the worktree in place for subsequent merge. The tool result is delivered to the parent agent, not yet integrated into the parent's project and not necessarily delivered as a final answer to the original user. The parent's later native reply travels through [RT-RTE-native-turn](runtime.md#rt-rte-native-turn). No inspected step requires a human to approve the content before this return. Actual merge execution, merge-conflict recovery and enforcement at every merge path were not traced; this account cannot claim that advertising a branch proves integration or a universal merge gate.

The background alternative must not inherit the foreground marker interpretation. Its submission path adds `FORK_BRANCH` immediately and separately binds a task/watchdog for later finalization. A branch marker alone is therefore not a system-wide certificate of completion. This is a path-specific qualification of [RT-RTE-fork-worker](runtime.md#rt-rte-fork-worker), supported by SRC-1, `src/qwenpaw/agents/tools/agent_management.py`.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-fork-finalization
Label: Fork worktree finalization

Part of: [RT-RTE-fork-worker](runtime.md#rt-rte-fork-worker)

This is the administrative finalization subroute, not a second identity for the entire worker dispatch. Endpoints: worktree path, branch and expected scope → per-branch finalization lock → registry transition/recovery → dirty-worktree commit → persisted finalized head or failed state. Owner: QwenPaw fork-project code. Effects: Git index/commit changes and registry status/head updates; no automatic parent-project merge. SRC-1, `src/qwenpaw/agents/fork_project.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Boolean finalization result; exceptions are marked failed and re-raised by the wrapper.
- Later read-back: registry status and recorded head are read by subsequent finalization calls; retained Git commits/worktree remain available for later integration.
- Delegated visibility: foreground dispatcher maps the Boolean to a branch-ready or failure marker for the parent; the worker's entire context is not returned.
- Selection predicate: foreground worktree plus truthy collected response; finalizer additionally requires valid path/branch and acceptable registry/scope state.
- Invalidation or expiry: unknown/inactive or mismatched-scope rows cannot be newly finalized; later scope changes constrain stale callers. Full retention and cleanup policy uninspected.
- Activation or effect: code can commit dirty changes and record finalized status; successful execution and product correctness unobserved.
- Evidence limits: selected finalization and commit functions inspected, not all recovery helper internals or merge callers; no runtime evidence or quality evaluator supplied.

Trigger/proposal: worker project changes and a received response initiate foreground finalization. Code decides administrative acceptance; human review/veto is not part of this inspected subroute. Operating mode: open delegated work, not a bounded experiment. Answer oracle: none. Guidance: injected worker commit protocol; code also stages/commits if the worker leaves changes dirty. Persistence: Git commits, retained worktree and registry metadata. Rejection: invalid/inactive scope, lock/path failures or unsuccessful Git operations can prevent finalization. Recovery: repeat finalization can reuse an already finalized result; the wrapper marks unsuccessful attempts failed. No rollback of arbitrary worker side effects is established.

Guarantee owner: fork-project finalizer. Enforcement point: per-branch lock, registry transition and scope checks. Guarantee strength: protocol. Covered path: calls through the inspected finalization functions; direct Git operations and later merge execution are not constrained by this finding. Required external contract: Git/filesystem/OS locking behavior. No successful operation was observed.

> if action == "done":
>     return True
> if action == "skip":
> --- `src/qwenpaw/agents/fork_project.py`

> if not status:
>     return True
> --- `src/qwenpaw/agents/fork_project.py:1063-1113`

> ["git", "add", "-A"],
> --- `src/qwenpaw/agents/fork_project.py`

> ["git", "commit", "-m", message],
> --- `src/qwenpaw/agents/fork_project.py`

> reason="finalize_fork_worktree failed",
> --- `src/qwenpaw/agents/fork_project.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-fork-worker](runtime.md#rt-rte-fork-worker)

Workflow verification boundary: foreground response presence is a truthiness check on the last non-usage SSE payload, not task-success validation. Administrative finalization is separately recorded in [WF-RTE-fork-finalization](#wf-rte-fork-finalization). Foreground branch advertising follows finalization; background submission advertises a branch before later finalization. Delivery to the parent, branch finalization, integration and delivery to the original user are distinct milestones. The workflow account gives the supporting inspection and quotations without treating this annotation as a redefinition of the delegated route.
