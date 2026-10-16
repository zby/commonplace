---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Fractal workflow account: caller-coordinated security audit, explicit session resumption and delegated repair at the frozen revision."
run-id: AAS-2026-10-14-fractal-ee03010af4c2-01
reviewed-boundary: "6a226e7d539e229b5c7cc9ffa3b05ab1c8f00385"
---

# Fractal workflow report

## Workflow account

The selected workflow is the shipped headless recipe: audit `auth.py`, capture the session ID, then ask the resumed session to fix the worst issue. It is representative because it demonstrates Fractal's coding delegation and a consequential cross-process handoff without inventing an internal worker graph. The caller sequences two turns; Fractal persists and reloads context; PredictRLM owns each delegated model/code computation. This is a source-supported calling procedure and inspected implementation, not an observed audit or successful repair (SRC-1, `.agents/skills/fractal/RECIPES.md`, `src/fractal/cli.py`, `src/fractal/runtime.py`, `src/fractal/agent/service.py`). The composite procedure is [WF-RTE-audit-repair](#wf-rte-audit-repair); each turn uses [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn).

**1. Request and delegation.** The caller supplies an audit request and workspace. The first process resolves provider/model configuration and creates a fresh session when no resume ID is supplied. It prints the session ID to stderr before submission. Runtime submission records and saves a pending user turn before calling the agent. The handoff to PredictRLM supplies mutable workspace objects, the request and detailed session history as inputs, plus root project guidance and the rendered session summary in the signature. Model adapters, skills, interpreter and iteration budget are configured by Fractal. Fractal awaits one computation; subordinate scheduling is inside the excluded dependency, not a Fractal-owned coordinator established by this source (SRC-1, `src/fractal/cli.py`, `src/fractal/runtime.py`, `src/fractal/agent/service.py`; [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn), [RT-OBJ-edit-workspace](runtime.md#rt-obj-edit-workspace)).

The audit wording is not a filesystem read-only gate. The adapter creates DIRECT workspaces. The recipe itself warns that prompts can imply edits and recommends an explicit no-modification request for pure questions. Consequently the first turn is not established as an enforced analysis-only phase, and neither turn waits for per-file approval (SRC-1, `.agents/skills/fractal/RECIPES.md`, `src/fractal/agent/service.py`; [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn)).

**2. Audit return and cross-process handoff.** A normal adapter return is checked for the expected response/list types, then recorded as a terminal turn and printed. These checks do not verify the alleged security issue or the actual filesystem diff ([RT-CLM-result-contract](runtime.md#rt-clm-result-contract)). The caller extracts the session ID from the first process's stderr and starts a second process with the same workspace and `--resume`. The recipe has no branch checking the audit exit code before issuing the repair request. Capturing an ID therefore does not prove a successful audit: the ID is printed before model work. A failed or budget-limited first turn can still supply a session for the second request (SRC-1, `.agents/skills/fractal/RECIPES.md`, `src/fractal/cli.py`, `src/fractal/runtime.py`).

**3. Resume and repair selection.** Runtime resumption checks for an existing session file and loads it. The next submit supplies the rendered structured summary and bounded detailed history, rather than copying only the audit response into a new prompt. The summary is always-visible signature text; exact details are reachable through the history input from Python. Detailed history is capped at 20 turns; this does not bound the summary to 20 turns. The fresh predictor receives the new request to fix the worst issue. That wording delegates issue ranking and repair to the computation; the recipe does not specify a severity rubric, reference answer or independent security reviewer (SRC-1, `src/fractal/runtime.py`, `src/fractal/session.py`, `src/fractal/agent/signature.py`; [RT-OBJ-session-state](runtime.md#rt-obj-session-state), [RT-OBJ-edit-workspace](runtime.md#rt-obj-edit-workspace)).

The recipe's claim that sessions live under the workspace's `.fractal/sessions/` directory is stale. The supplied boundary and runtime establish workspace-keyed global persistence. The workflow depends on the CLI resume interface and persisted session, not on that recipe path ([RT-OBJ-session-state](runtime.md#rt-obj-session-state); SRC-1, `.agents/skills/fractal/RECIPES.md`, `src/fractal/session.py`).

**4. Verification and delivery.** The shipped signature asks the delegated coding agent to inspect before modifying, preserve unrelated content and verify important edits. This is model-interpreted guidance, not an executable acceptance test. The adapter checks output structure; runtime distinguishes a recognized budget fallback from ordinary return; CLI emits text or JSON and an exit status. Thus delivery means the recorded response and reported changed-file list reach the caller, with edits already effected in the mutable workspace. It does not mean a staged patch was independently tested and accepted. Normal status `succeeded` does not certify repair correctness ([RT-CLM-result-contract](runtime.md#rt-clm-result-contract), [RT-RTE-budget-exhaustion](runtime.md#rt-rte-budget-exhaustion); SRC-1, `src/fractal/agent/signature.py`, `src/fractal/cli.py`, `src/fractal/runtime.py`).

The calling recipes separately recommend a clean Git tree and an independent post-run diff. That can reveal filesystem changes independently of model prose, but the source does not wire it into the audit/repair sequence or make it a correctness oracle. A caller must arrange any tests, security review or final acceptance beyond the returned envelope (SRC-1, `.agents/skills/fractal/RECIPES.md`).

**5. Failure and recovery.** For exceptions inside the guarded agent call, runtime persists a failed turn with available trace/error information and re-raises; the headless driver reports failure and exits 1, then attempts runtime cleanup. Budget exhaustion instead preserves the fallback response, records `max_iterations` and exits 2. The caller decides whether to inspect, retry or resume. Neither branch restores already modified workspace files. Failures before the guarded agent call, including pending-save failures, do not have the same terminal-turn recovery guarantee ([RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn), [RT-RTE-budget-exhaustion](runtime.md#rt-rte-budget-exhaustion); SRC-1, `src/fractal/runtime.py`, `src/fractal/cli.py`). Headless KeyboardInterrupt reporting must not be conflated with the predicate-recognized interactive persistence branch described by [RT-RTE-interactive-interrupt](runtime.md#rt-rte-interactive-interrupt).

Resumption itself can reject a nonexistent session. Existing but unreadable or invalid session content may be ignored with a warning and replaced by a fresh in-memory session under the requested ID. Consequently existence and ID continuity alone do not guarantee preserved audit context; this is a loader recovery path, not observed data loss (SRC-1, `src/fractal/runtime.py`, `src/fractal/session.py`; passages in [WF-RTE-audit-repair](#wf-rte-audit-repair)).

Added inspection under SRC-1 covered the complete caller recipe, headless driver admission/return/cleanup, runtime resume and submit, session load/save/history supply, the signature body, and agent workspace/predictor construction. These are implementation and doctrine/design evidence at the frozen commit. No command, target test, provider or example was executed. Actual issue discovery, verification, dependency recursion, sandbox enforcement and successful recovery remain unobserved; no end-to-end reliability or benefit is established.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-audit-repair
Label: Caller-coordinated audit and repair

Distinct identity: this is the shipped cross-process procedure joining an audit turn to a repair turn by explicit session-ID capture and resumption. It spans two invocations of [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn) and consumption of [RT-OBJ-session-state](runtime.md#rt-obj-session-state), rather than declaring another identity for either single-turn submission or the checkpoint container.

Endpoints and progression: caller → audit CLI process → PredictRLM → saved audit result → caller extracts ID → resumed repair CLI process → PredictRLM → saved repair result and terminal output. The caller owns sequencing and continuation; Fractal owns checkpoint loading/saving and output classification; the dependency owns issue selection and execution inside each computation. Context crosses the process boundary through session state and the same mutable workspace. Evidence: SRC-1, `.agents/skills/fractal/RECIPES.md`, `src/fractal/cli.py`, `src/fractal/runtime.py`, `src/fractal/session.py`, `src/fractal/agent/service.py`, `src/fractal/agent/signature.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: each process prints a response or failure report and an exit status; the repair may leave direct filesystem edits plus a reported changed-file list.
- Later read-back: the resumed repair turn receives audit-derived summary/history from saved session state; future explicit resume can consume the repair outcome. Workspace edits remain available to later work.
- Delegated visibility: each computation receives workspace objects, current request and detailed history; summary and root instructions enter signature text. Exact dependency-internal context transformation is uninspected.
- Selection predicate: the caller uses the same workspace and captured session ID with --resume, then asks to fix the worst issue; runtime checks file existence and the loader validates saved content. Issue ranking inside the computation is uninspected.
- Invalidation or expiry: detailed history is capped at 20 turns; malformed/unsupported saved content can be ignored with warnings; missing session files reject runtime resume. No automatic workspace rollback occurs on failed or budget-limited turns.
- Activation or effect: the source wires reloaded context into the repair call and grants mutable workspaces. Actual repair decisions depending on that context and successful edits are unobserved.
- Evidence limits: the recipe establishes intended sequencing, not its execution; it lacks an audit-exit-code gate. External dependency implementation and an actual user workspace are not evidence in this run.

Admission account: the caller proposes both tasks and the workspace grant. The delegated computation chooses the issue and effects repairs under focused-edit guidance. Fractal can reject structurally invalid returned output, not veto individual edits before they occur. The caller can choose not to launch repair or can inspect the result afterwards; generic caller identity does not establish a human approver. No expected-answer oracle or independent result gate is supplied. Operating mode is an open coding request, not a bounded candidate-comparison experiment. Failure/budget outcome persistence enables manual continuation but is not rollback. The checkpoint and direct workspace changes persist; no trained-parameter update is established.

> fractal -p "Audit auth.py for security issues" --workspace "$ws" 2>err1.log
> sid=$(grep -m1 '^fractal: session ' err1.log | awk '{print $3}')
> fractal -p "Now fix the worst issue you found" --resume "$sid" --workspace "$ws"
> --- `.agents/skills/fractal/RECIPES.md`

> Keep changes focused on the current user request. Inspect files before modifying
> them, preserve unrelated content, and verify important edits. Return only a
> concise user-facing response and a list of changed file paths, relative to the
> primary workspace when possible.
> --- `src/fractal/agent/signature.py`

> To verify edits independently of the model's prose, run in a clean git tree and
> diff afterwards (`git -C "$ws" diff` / `git status --porcelain`).
> --- `.agents/skills/fractal/RECIPES.md`

> if not session_path(self.workspace_path, session_id).exists():
>     raise FileNotFoundError(f"No Fractal session found for id {session_id!r}.")
> self.session = FractalSession.load(self.workspace_path, session_id=session_id)
> --- `src/fractal/runtime.py`

> f"Ignoring unreadable Fractal session at {path}: {exc}. "
> f"{backup_note}",
> RuntimeWarning,
> stacklevel=2,
> )
> return cls(session_id=session_id)
> --- `src/fractal/session.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn)

Workflow role: invoked once for audit and again for repair in [WF-RTE-audit-repair](#wf-rte-audit-repair). The session ID is exposed before execution, so it is a continuation handle, not an audit acceptance certificate. The caller recipe does not check the first turn's exit code before the second request. Post-run independent diff inspection is advised elsewhere in the recipe, not enforced in this sequence (SRC-1, `src/fractal/cli.py`, `.agents/skills/fractal/RECIPES.md`).

#### On [RT-CLM-result-contract](runtime.md#rt-clm-result-contract)

Workflow verification role: this check is a structural adapter boundary after direct execution. It cannot certify the security finding or repair, and is not an edit-commit gate. The signature separately requests important-edit verification; that request does not establish compliance (SRC-1, `src/fractal/agent/signature.py`, `src/fractal/agent/service.py`).
