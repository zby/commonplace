---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "EQUIPA runtime baseline: task execution, provider alternatives, gated product admission and prompt/configuration change paths."
run-id: AAS-2026-10-15-equipa-32016e8dd9ae-01
reviewed-boundary: fa8f41a6948584ee53e804edbb08b7449d05cd14
---

# EQUIPA runtime report

## Runtime account

### Evidence and claimed work

EQUIPA surrounds model-driven software work with task scheduling, developer/tester iteration, security review, merge admission and recorded outcomes. This is an enclosing runtime, not the inference engine itself. The frozen boundary is [boundary.md](boundary.md). All new inspection below is implementation evidence from SRC-1 at its registered revision. No target code, tests, model calls or deployment probes were executed. Wiring is distinguishable from activation, reliability and benefit throughout.

Added detailed coverage comprises `equipa/cli.py` task dispatch, `equipa/dispatch.py` task worktrees and merge gate, `equipa/loops.py` cycle control, `equipa/agent_runner.py` CLI construction/provider dispatch/spawn, `equipa/isolation.py` refusal, launch and export-import functions, `equipa/security_gate.py` provenance definitions, `equipa/security.py` integrity checking, `ollama_agent.py` tool handlers and loop, `equipa/manager.py` planner/evaluator and rounds, `equipa/mcp_server.py` dispatch handler, `equipa/rlm_decompose.py` threshold and session loop, `equipa/hooks/__init__.py` async events and external hooks, `equipa/role_resolver.py` role construction/resolution, `equipa/prompts.py` assembly and GEPA selection, `forgesmith.py` patch/config admission and full pipeline, `forgesmith_gepa.py` validation/storage/selection/rollback, and `scripts/autoresearch_loop.py` mutation/deployment/selection. This expands inspection within SRC-1, not its evidence identity.

### Ordinary invocation and ownership

A representative shipped invocation is `python -m equipa --task <id> --dev-test --yes`. The boundary establishes package/root entry points. In `equipa/cli.py`, task mode resolves task, project directory and project context, honors dry-run, and asks confirmation unless `--yes`. That confirmation authorizes starting work; it is not approval of every proposed edit. For a Git project, the CLI supplies an execution callback to `run_task_in_isolation`. Dispatch pins the default branch, creates `forge-task-<id>` under `.forge-worktrees`, refuses stale or unusable worktrees, and executes in the corresponding project subdirectory. Task ID, project ID, role, cycle, task branch and run result are separate identities. The Python orchestrator owns the next phase; the inner agent owns tool choice within a phase. See [RT-RTE-dev-test](#rt-rte-dev-test) and [RT-RTE-gated-merge](#rt-rte-gated-merge).

The dev/test loop performs dependency/build preparation, restores optional session context and checkpoints, resets database task status to `in_progress`, and resolves role-specific model/turn budgets. Each cycle reads agent messages, constructs a developer prompt, fires lifecycle hooks and dispatches a fresh inner agent. The prompt combines common rules, role body and standing orders with task/project context, selected lessons/episodes, budget and extra context. The developer's filesystem/Git changes cross into the tester's invocation through the task worktree and a per-cycle diff, not through a shared full conversation. The tester receives its own role prompt and returns text which is parsed into outcomes. Failure information and summaries can enter another developer invocation. SRC-1, `equipa/loops.py`, `equipa/prompts.py`.

The runtime ends on pass/no-tests, blocked/failure, budget or progress limits, overload, timeout, or cycle exhaustion. It can continue timed-out/max-turn developer work with recovery context and can retry analysis paralysis with stronger action instructions. Those are instructions and code thresholds, not demonstrated repairs. A successful cycle result is only a candidate for product admission. Security review and the merge gate still intervene in Git dispatch. The final CLI path records merge-reconciled task status and telemetry; failed branches are preserved, and uncommitted work can be stashed during cleanup. SRC-1, `equipa/cli.py`, `equipa/dispatch.py`, `equipa/loops.py`.

### Material alternatives and forcing cases

The following source cases challenge broad guarantees rather than merely add features:

1. **Pass is not equivalent to independently tested correctness.** The pass branch rejects absent skip counts, zero tests, inconsistent counts and framework skip contradictions, but `no_tests` remains merge eligible. Audit/report tasks can return `tests_passed` without invoking the tester when a markdown deliverable exists and the relevant diff is empty. Developer “no changes needed” can bypass testing; dispatch separately checks for contradicting branch changes. Thus neither a task status nor a model verdict is a general correctness oracle. SRC-1, `equipa/loops.py`, `equipa/dispatch.py`; [RT-RTE-dev-test](#rt-rte-dev-test).
2. **Review policy has deliberate alternate paths.** `_gated_merge_task` recomputes the actual diff and can exempt doc-only work. Global operator policy can disable security review or relax missing-artifact blocking. Non-Git work has no branch/merge protection. A guarantee about protected code merges cannot be widened to all filesystem effects or all tasks. SRC-1, `equipa/dispatch.py`, `equipa/cli.py`; [RT-RTE-gated-merge](#rt-rte-gated-merge).
3. **Ollama is not the Claude sandbox.** Its tools execute in the orchestrator process/user, so isolation-enabled operation refuses this route at both dispatch and direct loop entry. When allowed, role filtering changes advertised tools, but dispatch looks up returned tool names in the full handler table. Read-only advertisement alone therefore is not a handler-level authorization check. Shell safety is prefix/substring filtering plus `shell=True`, not filesystem confinement. This is a source-level scope finding, not an executed exploit. SRC-1, `ollama_agent.py`, `equipa/agent_runner.py`; [RT-RTE-ollama-tools](#rt-rte-ollama-tools).
4. **Direct calls and callbacks are distinct enforcement surfaces.** Goal planner/evaluator call `run_agent` directly with read-only CLI restrictions rather than `dispatch_agent`. RLM calls Claude directly and is refused when isolation is enabled. External lifecycle hooks run shell subprocesses and return results to callers; a `blocked` result is not automatically a veto when a caller ignores it. The dev/test `pre_agent_start` calls inspected here ignore those return values. These cases preclude treating one dispatcher guard as a universal system guarantee. SRC-1, `equipa/manager.py`, `equipa/rlm_decompose.py`, `equipa/hooks/__init__.py`, `equipa/loops.py`.

Other shipped front doors reuse or surround this work. The MCP dispatch handler authenticates and checks rate/cost and role/model/turn constraints before spawning a detached CLI with `--yes`; its immediate response is a PID, not a completed task. Goals run planner → isolated task execution → evaluator rounds. The boundary also identifies automatic project dispatch, parallel goals/tasks, initiative waves and arena callers. Their shared gate is supported by the supplied boundary and inspected task helper, but their complete scheduling internals were not independently audited here. See [RT-RTE-goal-rounds](#rt-rte-goal-rounds). Interactive `.claude/skills/` procedures and memory maintenance remain included; the boundary's session-end evidence establishes a separate instruction-driven write surface, not an invocation of this dev/test gate.

### Controls, context and isolation envelope

The capability surface includes Claude's tools and configured MCP servers, file/shell tools in Ollama, project role additions, Python callbacks, external hook commands and improvement programs. Current grants depend on live configuration, credentials, filesystem permissions, model service and installed integrations, none supplied. The deployed isolation envelope cannot be inferred from an example config or a launch function. Model components and their version uncertainty are recorded in [RT-CMP-claude](#rt-cmp-claude) and [RT-CMP-ollama](#rt-cmp-ollama).

For Claude, the command includes a max-turn budget, no CLI session persistence, appended prompt file, selected model and `bypassPermissions`. Ordinary interactive permission prompting is therefore not the task's per-tool admission mechanism. EQUIPA separately isolates settings/MCP discovery, scrubs subprocess environments, checks project/MCP paths and, on Linux, refuses if orchestrator process protection fails. Spawn-level argument normalization also covers direct `run_agent` callers. A feature-gated PreToolUse Bash hook adds a pre-execution check; installation failures can skip it. A reactive stream check is not equivalent to preventing a tool effect. SRC-1, `equipa/agent_runner.py`.

The isolated execution path is [RT-RTE-isolated-agent](#rt-rte-isolated-agent). With agent isolation enabled, `_spawn_agent_process` delegates to the isolated launcher and turns setup failure into refusal rather than falling back. The inspected launch uses a systemd scope, resource properties, `sudo -n -u` to a separate agent user and a launcher handoff. Export import verifies a bundle, ancestry and links before compare-and-swap task-branch update. This is stronger than using a Git worktree alone, which shares repository state and is not an OS sandbox. External contracts include Linux/systemd/sudo configuration, separate-user permissions, cgroup functionality, networking/firewall enforcement, and Claude's handling of supplied CLI controls. The launch comments explicitly say an unprivileged user manager may not enforce `IPAddressDeny`; launcher checks and host firewall setup matter. No deployed success of these contracts was observed. SRC-1, `equipa/isolation.py`, `equipa/agent_runner.py`.

Context is deliberately selective. Separate developer/tester and planner/evaluator calls keep their full conversations apart; worktree state, diff, summaries, messages and parsed results cross frames. `_build_dev_extra_context` preserves paralysis warnings, conditionally consolidates regular history to a word cap and prepends messages. Without `anti_compaction_state`, regular history is omitted there. Session/checkpoint paths can supply later invocations, despite `--no-session-persistence` at the Claude layer. RLM retains repository text outside the outer prompt and replaces successive outer-call context with the original decomposition prompt plus the latest REPL results; earlier output remains in its aggregate return and sandbox state, not necessarily the next prompt. File/tool truncation in Ollama keeps only prefixes of oversized results. These are code-controlled context boundaries, not evidence that all important facts survive. Memory selection/revision details belong to the memory member. SRC-1, `equipa/loops.py`, `equipa/rlm_decompose.py`, `ollama_agent.py`.

### Admission and improvement plane

Product changes flow through [RT-RTE-gated-merge](#rt-rte-gated-merge). New prompt/configuration behavior can instead enter through [RT-RTE-forgesmith-changes](#rt-rte-forgesmith-changes), [RT-RTE-gepa-prompts](#rt-rte-gepa-prompts), [RT-RTE-autoresearch-prompts](#rt-rte-autoresearch-prompts) and [RT-RTE-role-extension](#rt-rte-role-extension). Their controls are not interchangeable: ForgeSmith's prompt-patch manual default does not govern the separate autoresearch script. Hook registration/configuration adds executable production behavior through [RT-RTE-lifecycle-hooks](#rt-rte-lifecycle-hooks).

The full ForgeSmith pipeline collects/analyzes runs, evaluates earlier changes, extracts lessons, invokes SIMBA, scores runs/evolves rubric weights, verifies findings, applies changes and optionally invokes OPRO/GEPA and LITM. Importantly, it returns immediately when `findings` is empty, before those later phases. Their existence is not evidence they run nightly or on every invocation. Detailed SIMBA lesson admission, episode value updates, LITM transformations and optimizer internals are not established by this runtime pass; they remain included, available source for the memory/epistemic analysts. Training export/import utilities, deployment/sync scripts, complete sweep/arena measurement semantics and all plugin bodies were not deeply inspected. This prevents a complete assurance claim about every improvement or production-machinery change, but does not erase the concrete admitted prompt/configuration paths below. No weight-update claim or successful self-improvement is inferred from script names. SRC-1, `forgesmith.py`; boundary coverage for remaining shipped paths.

## Shared records

### Components

#### RT-CMP-claude
Label: Claude model service

Source-native identity: Claude selected through CLI `--model`, including role-resolved models and direct optimizer calls. Representational form: distributed-parametric inference behind a text/tool interface. Storage substrate: external service/provider-managed weights; not the prompt files or SQLite database. SRC-1, `equipa/agent_runner.py`, `equipa/manager.py`, `equipa/rlm_decompose.py`, `scripts/autoresearch_loop.py`.

Parameters changing during operation: uninspected — these callers perform inference, while provider weight maintenance is outside the boundary. Exact model version pinned: not established; `model` is a configurable selector and the autoresearch mutator explicitly uses `opus`. Mutable endpoint resolving to another model: possible through configuration/provider alias resolution; exact service behavior is uninspected. No inspected invocation establishes online weight training.

> "--model", model,
> "--max-turns", str(max_turns),
> "--no-session-persistence",
> --- `equipa/agent_runner.py`

#### RT-CMP-ollama
Label: Ollama model endpoint

Source-native identity: role-configured Ollama model and base URL, with environment/default fallback at direct loop entry. Representational form: distributed-parametric model inference; JSON messages/tools are its symbolic transport. Storage substrate: Ollama-managed model files/service, outside the source evidence. Parameters changing during operation: uninspected; the loop only sends chat calls. Exact version pinned: not established by a configurable model string. Mutable endpoint resolving to another model: allowed by model/base-URL/environment configuration; actual endpoint contents are unavailable. SRC-1, `ollama_agent.py`, `equipa/agent_runner.py`.

> base_url = base_url or os.environ.get("OLLAMA_BASE_URL", DEFAULT_BASE_URL)
> model = model or os.environ.get("OLLAMA_MODEL", DEFAULT_MODEL)
> --- `ollama_agent.py`

### Operative objects

#### RT-OBJ-role-prompts
Label: Role prompt bodies

Identity: shared `prompts/<role>.md`, common prompt, standing orders and selected GEPA role variants; project overlays are separately admitted role additions. Representational form: natural-language instructions, with symbolic placeholders/frontmatter interpreted by assembly code. Storage substrate: Markdown files; GEPA change/version metadata in SQLite. The consumer supplies assembled text to an inference invocation; instruction delivery is not reliable compliance. SRC-1, `equipa/prompts.py`, `forgesmith_gepa.py`, `equipa/role_resolver.py`.

> static_prefix = common_text + "\n\n---\n\n" + role_text + standing_orders
> --- `equipa/prompts.py:508-508`

#### RT-OBJ-task-branch
Label: Task branch and worktree

Identity: `forge-task-<id>` and task worktree, plus pinned reviewed/merge commit identities. Representational form: symbolic Git references, commit graph and filesystem state; source files may themselves contain text instructions or code. Storage substrate: project filesystem and Git object/ref store. This object is the product candidate, not a model conversation. Failed/unmerged work survives on retained branches or stashes; merge success can delete the temporary branch/worktree. SRC-1, `equipa/dispatch.py`, `equipa/isolation.py`.

> task_branch = f"forge-task-{task_id}"
> --- `equipa/dispatch.py:4672-4926`

### Routes

#### RT-RTE-dev-test
Label: Developer tester iteration

Endpoints/progression: task/project context → developer call → tester call → parsed decision → retry or returned outcome. Python loop owns phase transitions, models propose code and tester judgments. Inputs include common/role rules, task text, selected retained context, prior failures and per-cycle Git diff; effects include file/commit writes, database status/messages and recovery material. The CLI or scheduling caller owns final telemetry and product admission. SRC-1, `equipa/loops.py`, `equipa/prompts.py`, `equipa/cli.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: last result dictionary, completed cycle count and outcome reason.
- Later read-back: checkpoints and optional session state can enter later task invocations; summaries/failure context can enter subsequent cycle calls. Memory admission details are not assessed here.
- Delegated visibility: separate developer/tester prompts; tester sees task context and cycle diff, developer can receive tester messages/summaries, not the tester's entire private frame.
- Selection predicate: selected dev-test mode or a manager task; bounded cycle count, progress, cost and parsed outcome govern continuation.
- Invalidation or expiry: clear checkpoints on accepted outcomes; cycle budget/termination ends the loop; context consolidation can omit regular history.
- Activation or effect: code routes parsed outcomes and issues tool-capable calls; actual tool execution, instruction compliance and quality are unobserved.
- Evidence limits: no execution trace; framework output scans and model summaries are not independent verification of arbitrary project correctness.

Operating mode: open task execution with bounded retries, not a fixed expected-answer curriculum. Proposer: developer model. Tester model proposes acceptance/failure; code can veto inconsistent pass counts and overload, terminate on budgets or admit `no_tests`. Human contributes task and initial confirmation/configuration, not necessarily per-edit review. Answer oracle: project tests can supply executable expected outcomes if actually run; their correctness and actual coverage are external and unobserved. Model judgment itself is not an oracle.

> if tests_run == 0:
>     return _route_inconclusive("pass_with_zero_tests")
> --- `equipa/loops.py`

> elif outcome in MERGE_ELIGIBLE_OUTCOMES and nothing_to_merge:
> --- `equipa/dispatch.py`

The latter branch qualifies any claim that every accepted task requires a new merge. A separate audit-task branch also synthesizes `tests_passed` from a markdown deliverable. Failure descriptions guide another attempt; executable changes persist through the product gate, while recovery context can persist through checkpoints/sessions. These mechanisms establish a retry protocol, not successful learning.

#### RT-RTE-gated-merge
Label: Gated task merge

Endpoints/progression: completed task branch → optional reviewer → diff-derived GateDecision → pinned-commit merge → guard verification → reconciled status. Owner: dispatch code and DefaultBranchGuard. Reviewer proposes severity findings; code decides merge eligibility, provenance and repository integrity; operator policy can opt out of review requirements. Proposed change: task product commits. Guidance: assigned task, developer/tester instructions and reviewer prompt. Persistence: landed Git commit and task/telemetry status, or preserved unmerged branch. SRC-1, `equipa/dispatch.py`, `equipa/security_gate.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: merged/blocked/skipped/noop/merge_failed and guard outcome with reason/SHA.
- Later read-back: future tasks consume the resulting project checkout; task status/merge SHA remains available to scheduling and reporting.
- Delegated visibility: reviewer gets a separate review invocation; gate consumes its artifact and in-process run record, not developer self-approval alone.
- Selection predicate: only `tests_passed` or `no_tests` reaches ordinary merge consideration; actual file diff and global security policy determine artifact requirement.
- Invalidation or expiry: a moved branch relative to reviewed SHA, failed provenance, repository hazards or tripped default-branch guard block admission; unmerged branches remain for operator resolution.
- Activation or effect: admitted commit updates default branch through the merge helper; no executed merge is supplied.
- Evidence limits: source proves checks and opt-outs, not absence of vulnerabilities, deployment isolation, or correctness of every generated conflict resolution.

Guarantee owner: `_gated_merge_task` plus defensive merge recheck and guard. Enforcement point: before merge and after expected default-tip movement. Guarantee strength: protocol. Covered paths: inspected Git task wrapper and supplied boundary's shared parallel/goal dispatch. Alternates: doc-only exemption, no-op, explicit security-review disable/missing-artifact policy, non-Git direct filesystem work, independent script/hook effects and external manual Git operations. Required external contract: trustworthy orchestrator/configuration and Git/OS semantics; reviewer model may still miss findings. Implementation conclusion status and operation conclusion status are those above. This is not a guarantee that agents cannot attempt to move refs: the guard detects/refuses subsequent admission, while separate OS isolation determines access prevention.

> if outcome not in ("tests_passed", "no_tests"):
> --- `equipa/dispatch.py`

> # A reviewed (code) diff merges exactly the commit the reviewer read.
> review_record = get_reviewer_run(task_id)
> --- `equipa/dispatch.py`

> if decision.blocks_merge:
> --- `equipa/dispatch.py`

Recovery: shutdown is deferred during merge; failures keep candidate work, and a tripped guard halts later merges. Generated-file conflict handling can produce a resolution commit checked by the guard, so “landed SHA always equals reviewed SHA” would be too strong. Operating mode: open product admission. Answer oracle: none universal; artifact severity/provenance and Git state are admission inputs, not expected correct source code.

#### RT-RTE-ollama-tools
Label: Ollama tool loop

Endpoints: assembled system prompt → Ollama chat → returned tool calls → local handlers → appended tool results, until no calls/error/turn cap. Owner: Python loop; model selects next tools. Executor: orchestrator-user Python/file/subprocess operations, not isolated Claude launcher. SRC-1, `ollama_agent.py`, `equipa/agent_runner.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: joined assistant text and success/errors/turns/duration; success uses presence of `RESULT:` and ending below the cap.
- Later read-back: filesystem changes are visible to later calls/tasks; this loop itself keeps messages in local memory, not a durable conversation store.
- Delegated visibility: service receives system prompt and accumulated message/tool history; tool output is truncated at configured limits.
- Selection predicate: provider override/config chooses Ollama; role changes advertised read/write schemas; isolation-enabled direct and dispatcher paths refuse it.
- Invalidation or expiry: loop ends on no tool calls, API error or turn cap; local history is discarded on return.
- Activation or effect: returned tool name dispatches through the global handler map; file and shell effects are afforded, not observed.
- Evidence limits: safe-path checks cover file helpers, not arbitrary shell commands; read-only role advertisement is not checked again against handler membership.

> handler = TOOL_HANDLERS.get(tool_name)
> if handler:
> --- `ollama_agent.py`

> command, shell=True, capture_output=True, text=True,
> timeout=120, cwd=str(Path(project_dir).resolve()),
> --- `ollama_agent.py`

Guarantee strength: best effort for the read-only shell classifier, not a sandbox invariant. Policy owner: role/tool lists and string filters. Enforcement: advertised tools, prefix checks for the ordinary Bash handler and blocked substrings. Alternate handler `bash_write` deliberately bypasses the read-only prefix check; returned names are not constrained to the advertised subset. Isolation refusal is a separate protocol and depends on active configuration. Product writes on this route have no per-tool human approval; later Git merge admission, when used by its caller, does not undo prior shell effects.

#### RT-RTE-isolated-agent
Label: Isolated Claude execution

Endpoints: CLI command/prompt/MCP inputs → isolated launcher handoff → separate-user scope and clone → exported Git bundle → checked task-worktree import. Owner: shared agent spawn and isolation modules; the launcher/host supplies the execution envelope. The model selects actions inside the inner CLI, while host code decides whether the envelope can be established and whether exported work can be imported. SRC-1, `equipa/agent_runner.py`, `equipa/isolation.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: subprocess and containment handle, followed by agent result; setup errors become dispatch refusal rather than unisolated fallback.
- Later read-back: imported task-branch/file state reaches later tester/reviewer/task invocations and eventual product admission; this is not automatic retention of the full model conversation.
- Delegated visibility: handoff supplies selected prompt/configuration and project snapshot; export/import brings checked product state back, not unrestricted access to orchestrator state.
- Selection predicate: active `agent_isolation` policy, including required-host marker and fail-closed configuration handling.
- Invalidation or expiry: agent scope/session termination ends the execution frame; export import refuses unsafe links, wrong export shape or non-descendant branch tips and compare-and-swap mismatch.
- Activation or effect: separate-user launch and candidate import are implemented; deployed isolation enforcement and actual import are unobserved.
- Evidence limits: host users, sudoers, filesystem permissions, cgroups and network policy are external setup contracts; source checks are not proof of their deployed state.

Guarantee owner: `_spawn_agent_process` and isolation launch/import code. Enforcement point: launch setup/refusal and export import, distinct from later security review/merge. Guarantee strength: protocol. Covered paths: normal Claude spawn, including direct `run_agent` users of that spawn. Alternate paths: in-process Ollama and direct RLM/optimizer calls use refusal checks rather than this launcher; arbitrary lifecycle callbacks are not shown to enter this envelope. Required external contract: functioning configured Linux/systemd/sudo/cgroups, restricted agent user and actual network denial; resource/firewall requests alone are not deployment guarantees. The implementation and operation conclusion-status fields above apply to this guarantee.

> except isolation.AgentIsolationError as exc:
>     raise AgentDispatchRefused(f"agent isolation: {exc}") from exc
> --- `equipa/agent_runner.py`

Product admission at import is software-controlled. The agent proposes exported commits/state, code can reject them, and the eventual merge has a separate reviewer/gate. Recovery does not silently downgrade isolation; unresolved imports/launch failures require another valid dispatch or operator repair. Operating mode: isolated execution for open tasks. Answer oracle: inapplicable — import integrity/ancestry checks do not supply an expected correct product. Guidance shaping the proposal remains the ordinary task/role instructions; the persisted result is candidate Git/file state.

#### RT-RTE-goal-rounds
Label: Goal planner evaluator rounds

Endpoints: operator goal → planner proposal → orchestrator-created tasks → dev/test and gated Git dispatch → evaluator → complete/blocked/another round. Owner: manager code. Planner and evaluator use direct `run_agent` calls with read-only restrictions; shared spawn guards still apply, but `dispatch_agent` provider/integrity behavior is not thereby universal. SRC-1, `equipa/manager.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: goal outcome, rounds, completed/blocked task lists and cost/duration aggregates.
- Later read-back: database-created tasks and landed product changes survive for later rounds and invocations.
- Delegated visibility: each planning/evaluation call receives constructed goal/project/task summaries; task agents have their own contexts.
- Selection predicate: goal mode, maximum rounds/cost, planner task availability, evaluator parsed status and guard state.
- Invalidation or expiry: overload/failure, branch-integrity refusal, blocked evaluation or round cap stop progress; already-done tasks can be skipped.
- Activation or effect: validated task proposals become database tasks; evaluators can propose follow-ups; execution uses the product admission route.
- Evidence limits: goal completion remains a model assessment; no supplied expected-answer oracle or observed successful goal.

Proposer: planner/evaluator model. Decider/veto: orchestrator task validation/caps and default-branch guard; evaluator supplies completion judgment. Human: supplies goal/config, not necessarily each new task. Operating mode: open goal decomposition, not a fixed curriculum. Answer oracle: none established beyond task-level project checks. Admission recovery: rejected claims execute no tasks; worktree/guard refusal stops the goal for operator attention.

> result = await run_agent(restrict_to_read_only_tools(cmd))
> --- `equipa/manager.py:354-423`

#### RT-RTE-rlm-review
Label: RLM review decomposition

Endpoints: large review prompt/repository map → outer Claude code blocks → validated Python REPL → focused subqueries → final aggregate. Owner: session loop and REPL; model chooses decomposition/code. Eligibility: flagged code-reviewer/integration-tester with estimated context above 100,000 tokens. Source files live in sandbox state rather than all entering the outer prompt. SRC-1, `equipa/rlm_decompose.py`, `equipa/agent_runner.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: aggregated outputs, error list, subquery count and repository-file count.
- Later read-back: inapplicable — inspected session state is current-call state, with no durable write-back in the session loop.
- Delegated visibility: focused subqueries receive selected input; outer successor calls receive decomposition prompt plus latest REPL block outputs, not full previous outer turns.
- Selection predicate: feature, eligible role and size threshold; direct model calls refuse when agent isolation is enabled.
- Invalidation or expiry: bounded outer turns/subqueries/timeouts, validation violations and errors limit work; sandbox expires with session.
- Activation or effect: model-generated code executes after AST checks in the REPL and can issue model subqueries; this is not an OS security proof.
- Evidence limits: no execution or completeness evidence; `files_examined` is set from repository-map length, not proof every file influenced the review.

> conversation = (
>     f"{decompose_prompt}\n\n"
>     f"## Previous REPL Results (turn {turn + 1})\n\n"
>     f"{block_output}\n\n"
> --- `equipa/rlm_decompose.py`

The deciding code replaces the outer-call frame, while the REPL keeps the repository accessible. This resembles isolated frames returning selected values, not shared full attention over the repository. Review diagnosis remains model judgment without a reference-answer oracle. Operating mode is an open review request bounded by decomposition limits; no retained capability change is admitted by this loop itself.

#### RT-RTE-forgesmith-changes
Label: ForgeSmith configuration and patches

Endpoints: collected run patterns → findings/rationale → apply_changes → config write or appended prompt tuning section → next configuration/prompt consumer. Owner: ForgeSmith code. Config path rejects prohibited writes and consults impact analysis; patch path additionally checks protected files, production-path markers and default manual gate. SRC-1, `forgesmith.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: applied/proposed change descriptor, or no applied change for refusal/manual-review/high-risk rejection.
- Later read-back: dispatch configuration and role prompt files feed later execution; change records/backups support evaluation and rollback.
- Delegated visibility: agents later receive modified role text or configured limits, not necessarily stored change rationale.
- Selection predicate: pattern findings, dry-run/auto mode, change type, protection/refusal rules, risk assessment and patch auto_apply configuration.
- Invalidation or expiry: duplicate patches skipped; protected/high-risk/manual-gated proposals not installed; backups and rollback machinery retain recovery options.
- Activation or effect: config writes and prompt appends are implemented; actual later behavior depending on them is unobserved.
- Evidence limits: impact-analysis internals and complete previous-change evaluation/rollback bodies were not deeply inspected; risk labels are not independent safety evidence.

Proposer: pattern analyzers, with OPRO separately supplying model proposals in the full pipeline. Decider/veto: software admission checks and configured manual gate; operator can change policy or manually review a recorded proposal. Starting auto mode is not per-content approval. Guidance: failure-pattern rationale and append-only tuning policy; what persists is changed config/prompt plus change metadata. Operating mode: trace-driven maintenance on open work. Answer oracle: no universal expected-answer oracle; measured outcomes/rubric scores are proxies whose validity is not established here. This route does not inherit the product security-review gate.

> if not patch_cfg.get("auto_apply", False):
>     log(f"  [MANUAL-GATE] Prompt patch for {role} recorded for manual "
>         f"review (auto_apply disabled)")
> --- `forgesmith.py`

> config[key] = new_val
> --- `forgesmith.py`

Prompt patching can regenerate the integrity manifest. Thus the manifest checks authorized bytes against current metadata, not the merit of the change or an immutable ban on evolution.

#### RT-RTE-gepa-prompts
Label: GEPA versioned prompt admission

Endpoints: optimizer candidate → validation → versioned prompt/SQLite change record → runtime A/B selector → optional baseline fallback/revert. Owner: GEPA maintenance and prompt assembly. SRC-1, `forgesmith_gepa.py`, `equipa/prompts.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: candidate acceptance/rejection and storage/version descriptor; runtime selector returns selected path/version label.
- Later read-back: prompts builds base-role input from the selected version when `gepa_ab_testing` is enabled; change/run records supply subsequent rollback selection.
- Delegated visibility: agent receives selected role body; recorded version metadata is used by host telemetry, not a guarantee the agent knows the experiment assignment.
- Selection predicate: enabled optimizer pipeline, candidate guards, allowed role for storage, active version/file existence, rollback statistics and randomized A/B split.
- Invalidation or expiry: size/protected-section/RESULT-format checks can reject candidates; worse observed success-rate statistics can select baseline and mark evolution reverted; version file is retained.
- Activation or effect: conditional delivery of evolved text is wired; changed behavior and benefit are not observed.
- Evidence limits: optimizer training/validation internals and numerical-model dependencies not deeply inspected here; A/B code alone is not an experimental result.

Proposer: optimizer model/program. Decider: validation code, then selector/statistical rollback; no per-candidate human approval is shown in inspected storage/selection functions. Guidance: existing role prompt plus preserved structure/protected sections. Persisted object: versioned natural-language prompt, metadata, backups and outcome statistics. Operating mode: candidate optimization and randomized runtime comparison. Answer oracle: success labels in agent_runs drive rollback; this is not a reference correct prompt. Recovery marks database evolution reverted without deleting file.

> if _should_rollback(role, current_version):
>     log(f"Evolved prompt v{current_version} for {role} performing worse — "
>         f"using baseline")
>     return baseline_path, "baseline"
> --- `forgesmith_gepa.py`

> role_text = parse_frontmatter(selected_path.read_text(encoding="utf-8"))[1]
> --- `equipa/prompts.py`

#### RT-RTE-autoresearch-prompts
Label: Autoresearch prompt mutation

Endpoints: recent metrics/failure text/current role prompt → Claude rewrite → minimal output check → direct deployment → benchmark tasks → keep/revert. Owner: separate optimization script, not ForgeSmith patch admission. SRC-1, `scripts/autoresearch_loop.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: round/final console metrics; mutated prompt remains installed when kept.
- Later read-back: next mutation rereads the role file and metrics; subsequent task dispatch is intended to consume the deployed prompt.
- Delegated visibility: mutator receives metrics, failures and entire current prompt; benchmark agents receive deployed role prompt through their ordinary loader.
- Selection predicate: role/target/max rounds, below-target metrics, nonempty mutation of at least 200 characters, and post-dispatch success percentages.
- Invalidation or expiry: failed mutation skips round; failed dispatch, zero passes or regression under script policy can restore most recent backup.
- Activation or effect: local write and optional SCP deployment are wired; successful remote installation/dispatch and later behavior are unobserved.
- Evidence limits: remote host state, manifest compatibility and test-template validity unavailable; no realized quality or causal gain follows from printed percentages.

Human supplies role/objective/launch. Model proposes full rewritten prompt; code approves before testing based on length and then retains/reverts by benchmark outcomes. No ForgeSmith high-risk/manual/protected-section gate appears in the inspected loop. Mutation guidance requests one concise targeted change selected from failure patterns; it even instructs stronger action on no-change outcomes. What persists is the rewritten prompt and backups; remote SCP return handling does not prove delivery. The direct mutator refuses when local agent isolation is on; remote configuration cannot be inferred from the local flag. Operating mode: bounded rotating test-task curriculum using recent metrics plus benchmark tasks. Answer oracle: task success outcomes, not a supplied reference prompt or independently validated correct implementation.

> if not new_prompt or len(new_prompt) < 200:
>     print(f"  Mutation failed (empty or too short). Skipping round.")
>     continue
> --- `scripts/autoresearch_loop.py`

> # 5. Deploy
> deploy_prompt(role, new_prompt)
> --- `scripts/autoresearch_loop.py`

This is an implemented improvement-directed self-change pathway over role prompts, with objective success percentage specified independently of a particular rewrite. Evidence-responsive determination, own-organization write and a later prompt-consumption channel are wired. Subsequent behavior causally depending on a changed prompt is unobserved, so exercised self-improvement and improved capacity are not established. The same distinction applies to GEPA and ForgeSmith. No claim about a formulated theory builder is made: the exposed route establishes mutation/selection, not content-directed criticism and attribution of blame for a challenged theory.

#### RT-RTE-role-extension
Label: Project role extension

Endpoints: trusted project role Markdown → role resolution/frontmatter processing → assembled model instructions and capped runtime settings. Owner: role resolver and prompt builder. New names may add roles; base roles remain shared rather than overridden by project files. SRC-1, `equipa/role_resolver.py`, `equipa/prompts.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: RoleConfig or unknown-role failure.
- Later read-back: fresh role resolution can load retained overlay content on subsequent dispatches; stable-root/pinned-source policy keeps active task-worktree edits out of the current trusted source.
- Delegated visibility: role body joins common rules and standing orders; project-supplied skills paths are discarded.
- Selection predicate: requested role name, available base/overlay file and trusted project source; overlay turns/effort/exemption are capped by operator configuration.
- Invalidation or expiry: resolution rereads rather than sharing mutable per-project role state; new trusted revision/pin can change future content; unknown role fails.
- Activation or effect: instruction and permitted setting changes are delivered, not demonstrated capability improvement.
- Evidence limits: authorship and human approval of trusted project commits are unresolved; resolver code does not establish a human authored every overlay.

Admission: whoever can supply the trusted project role source proposes content; software enforces source/name/settings rules. Human contribution depends on project change governance, not established by caller identity. Rejection: reserved/base-role rules and settings caps; rollback: restore prior trusted role source/pin, with operational procedure uninspected. Operating mode: extension loading for open tasks. Answer oracle: inapplicable — no expected-answer evaluation in this loader. The added role is an instruction/configuration extension, not a new model weight set.

> if skills:
>     logger.warning("role overlay %s: 'skills' is not honoured for "
>                    "project roles; ignored", role)
> skills = []
> --- `equipa/role_resolver.py`

#### RT-RTE-lifecycle-hooks
Label: Lifecycle callback execution

Endpoints: registered Python callback or configured external command → lifecycle event → callback result/exit status → consuming loop. Owner: hook registry/dispatcher and event caller. This is production-machinery extensibility, not a model-only tool path. SRC-1, `equipa/hooks/__init__.py`, `equipa/loops.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: list of callback values, exit-code mappings or blocked mappings; callback exceptions are logged and represented as None.
- Later read-back: configured commands/registered callbacks can affect later events; registry lifetime is process-local, configuration files may persist. Durable content written by arbitrary commands is uninspected.
- Delegated visibility: callbacks receive event kwargs; external hooks get constructed environment and project cwd, not automatically the full agent conversation.
- Selection predicate: matching registered event/config entries; pre_cycle return dictionaries with extra_context are appended to developer context.
- Invalidation or expiry: unregister/clear/config reload or process end changes registrations; timeout kills external command process in inspected async helper.
- Activation or effect: Python callback or shell execution plus optional prompt-text injection; actual deployed registrations and effects unobserved.
- Evidence limits: no global sandbox or veto is established for arbitrary callbacks/commands; built-in plugin consumers and descendant cleanup were not comprehensively audited.

Admission: code registration or config file supplies executable behavior; config loader checks event/list/command shape, not command safety or per-content human approval. Proposer identity and filesystem governance remain deployment-dependent. Veto: `block_on_fail` creates a result, but authority depends on caller consumption; inspected dev/test pre-agent events ignore the results. Recovery: remove callback/config or terminate process; transactional rollback of hook side effects is not shown. Operating mode: event extensions on open workflows. Answer oracle: none supplied; exit status is not a correctness reference.

> proc = await asyncio.create_subprocess_shell(
>     command,
>     cwd=project_dir,
>     env=env,
> --- `equipa/hooks/__init__.py`

### Claims

#### RT-CLM-skill-integrity
Label: Skill integrity dispatch guard

Claimed operation: dispatch refuses skill-integrity failure. Source: SRC-1, `equipa/agent_runner.py`, `equipa/security.py`. Implementation iterates files listed by the manifest and compares hashes; missing/corrupt/empty manifest fails. The check does not prove complete enumeration of all future prompt material and is not a universal prerequisite of direct manager/RLM calls. Regenerating the manifest admits intentional changed bytes. Guarantee owner: dispatch and manifest verifier; enforcement: dispatch_agent entry; guarantee strength: protocol. Required contract: trusted manifest/file governance. Implementation conclusion status: wired. Operation conclusion status: uninspected.

> if not verify_skill_integrity():
> --- `equipa/agent_runner.py`

> for rel_path, expected_hash in expected_files.items():
> --- `equipa/security.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-role-instructions
Label: Role instruction authority

Consumer: Claude or Ollama inference invocation. Channel: assembled common/role/standing-order text plus dynamic suffix. Force: model-interpreted instruction, not enforced application logic; provider receives it, compliance is not established. Horizon: current invocation; retained role changes can reach later tasks/sessions through [RT-RTE-forgesmith-changes](#rt-rte-forgesmith-changes), [RT-RTE-gepa-prompts](#rt-rte-gepa-prompts), [RT-RTE-autoresearch-prompts](#rt-rte-autoresearch-prompts) and [RT-RTE-role-extension](#rt-rte-role-extension). Object: [RT-OBJ-role-prompts](#rt-obj-role-prompts). SRC-1, `equipa/prompts.py`, `equipa/agent_runner.py`.

> "--append-system-prompt-file", prompt_file.name,
> --- `equipa/agent_runner.py`

#### RT-BAP-merge-policy
Label: Merge decision authority

Consumer: dispatch merge helper. Channel: symbolic GateDecision, reviewer record, actual diff, pinned commits and guard outcomes. Force: executable branching can block the product merge, unlike an advisory prompt. Horizon: task merge and subsequent merges sharing a tripped guard. Actual deployment activation is unobserved. See [RT-RTE-gated-merge](#rt-rte-gated-merge). SRC-1, `equipa/dispatch.py`.

> return finish("blocked", f"security gate: {decision.reason}")
> --- `equipa/dispatch.py`

## Annotations

none
