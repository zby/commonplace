---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "OpenResearch runtime baseline: local chat admission, native harness execution, snapshot compute, run wake-ups and instruction/update admission."
run-id: AAS-2026-10-20-openresearch-62725ad1cd0a-01
reviewed-boundary: "2c45ff3183b494aac4001bd44eefbe57a3c249ae"
---

# OpenResearch runtime report

## Runtime account

OpenResearch encloses installed coding agents and compute controllers rather than implementing model inference. Its consequential work is an asynchronous research workspace: a user asks a project-scoped agent to inspect code, formulate experiments, execute them and explain results. The playbook requests this behavior; it does not prove scientific validity. The target's own contract explicitly separates execution and interpretation (SRC-1 `SYSTEM_PROMPT.md`):

> When asked to run and summarize an experiment, load `orx-compute` and
> `orx-results` before launching: execution and interpretation are separate skill
> areas. Use `orx-logs` when retrieving supporting output.
> --- `SYSTEM_PROMPT.md`

All findings below are implementation or doctrine/design evidence under SRC-1, not fresh target execution. No supplied trace or causal comparison was assessed. Activation, successful completion, agent compliance and benefit remain unobserved. Added inspection beyond the boundary's initial scope covers `src/compute.rs`, `src/local/localrun.rs`, `src/local/claude.rs`, `src/local/harness/codex.rs`, `src/local/user_skills.rs`, `src/updates.rs`, `src/commands/supervise.rs`, `agent-skills/orx-customize/SKILL.md`, and further ranges in `src/local/chat/mod.rs`, `src/commands/up.rs`, `src/local/experiments.rs`, `src/local/opencode.rs`, plus the UI shell API caller in `ui/src/api.ts`. These are same-revision sources, not new source identities.

### Ordinary shipped invocation

The desktop/dashboard host path reaches `orx up`. Startup binds localhost, opens the store, reconciles unfinished turns, reattaches supervisors for active experiment runs, constructs ChatHost, resumes persisted queues and starts run-wake and lease-reconciliation tasks (SRC-1 `src/commands/up.rs`). Harnesses start lazily. A UI/API user message carries session ID, text, attachments, annotations, settings and optional client-turn identity. ChatHost chooses start versus durable queue, then dispatches the session's selected harness. The turn, message, native-session and usage-execution IDs have different purposes; they are not interchangeable. [RT-RTE-chat-turn](#rt-rte-chat-turn) traces this path.

For the inspected Claude route, each turn ensures a private Git worktree, renders current project state into the shared playbook, and refreshes bundled and uploaded native skill folders. A resident Claude child receives stream-JSON input, native permission/model/effort flags, an appended system-prompt file, and a native store directory. Native context is resumed when available; a missing native session can instead receive a bounded textual ORX transcript snapshot. The host normalizes emitted events into persisted wire parts for the UI. Model decisions remain natural-language/parametric decisions inside the native harness; ORX admission and supervision are symbolic Rust/SQL rules. [RT-CMP-claude-model](#rt-cmp-claude-model) bounds model mutability, and [RT-OBJ-playbook](#rt-obj-playbook) identifies the delivered instruction object.

The foreground agent can create an experiment branch and then call `orx exp run`. Experiment creation forks its parent tip or project baseline, inherits a run command and writes a SQLite experiment row (SRC-1 `src/local/experiments.rs`). This admits an external research work product, not automatically a change to ORX itself. The agent/user proposes code; Git commits determine the source subsequently selected for execution. There is no scientific answer oracle in the inspected launch path: code validates configuration and backend readiness, not whether a hypothesis is true. [RT-RTE-experiment-run](#rt-rte-experiment-run) traces local execution, cancellation, status/log return and the optional later wake-up [RT-RTE-run-wakeup](#rt-rte-run-wakeup).

### Forcing cases and guarantee coverage

Three selected forcing comparisons prevent treating the normal path as a universal security or correctness contract:

1. **Same permission label, different enforcement.** Claude plan-mode bridge requests apply a read/deny/review policy. Codex plan mode explicitly uses workspace-write and on-request, relying on a native planning prompt rather than a read-only sandbox. This is a reachable configured alternative, not a hypothetical bypass. [RT-RTE-permission-review](#rt-rte-permission-review) records both.
2. **A separate human shell path.** The shipped shell endpoint checks host stopping/moving state, session idleness and session checkout, then runs Bash without consulting the session model permission mode. `ui/src/api.ts` supplies the `/shell` caller. This disproves a system-wide inference that Plan means no workspace mutation, but does not demonstrate that a model can invoke the human endpoint through a native tool. [RT-RTE-user-shell](#rt-rte-user-shell) bounds that distinction.
3. **Compute launch without a live dashboard.** `LocalExperimentPlane::launch` either forwards to trusted `orx up` or dispatches a local backend directly. The local backend still calls `compute::submit`; therefore snapshot selection and run reservation are not merely UI behaviors. `--force` deliberately relaxes the existing-in-flight check, not the source snapshot. Arbitrary native shell commands and the human shell endpoint do not pass through that compute contract. [RT-RTE-experiment-run](#rt-rte-experiment-run) records the guard and escape scope.

Capability surface, current grant and isolation must remain separate. The native agent can have shell/file/network tools; a session's selected permission mode determines what ORX asks the native runtime to allow; deployment still relies on the OS user account, external harness implementation and backend isolation. A private Git worktree prevents ordinary checkout interference; it is not an OS capability sandbox. The inspected local compute controller receives configured environment and shell PATH and runs the user's command in an extracted snapshot, not an isolated provider container (SRC-1 `src/local/localrun.rs`). No blanket tenant-isolation or provider-internal permission guarantee follows.

Load-bearing controls have these bounded strengths:

| Control | Owner and enforcement point | Strength and coverage | External contract and limits | Separate statuses |
|---|---|---|---|---|
| Claude bridge request validity | ChatHost `request_permission` checks per-child token and busy turn, revalidating after review-lock acquisition | protocol; covers requests delivered to this bridge, not arbitrary shell/native operations | Claude must route relevant requests to the bridge and honor replies | implementation conclusion status: wired; operation conclusion status: uninspected |
| Plan write restriction | Claude plan auto-policy denies named editing tools; Codex policy mapping differs | policy; not a system-wide invariant | native hooks, tool classification and native sandbox behavior remain dependencies; unknown tools go to review rather than a universal deny | implementation conclusion status: wired; operation conclusion status: uninspected |
| Recorded source execution | `SourceSnapshot::create`, content-addressed archive and local snapshot script | protocol; inspected local `exp run` and standalone dispatch; other backend adapters only mapped here | Git archive, filesystem and shell must behave as requested; ambient dependencies are not frozen | implementation conclusion status: wired; operation conclusion status: uninspected |
| One in-flight run by default | per-experiment file lock and reservation transaction | policy; only when `force` is false in `compute::submit` | local locking and SQLite; not arbitrary scripts | implementation conclusion status: wired; operation conclusion status: uninspected |

Backend parity beyond the local controller, remote host authentication, provider-native tools, ACP peers, full sub-agent lifecycle and updater platform installers remain uninspected here. Claude event handling exposes native sub-agent events, but this report does not establish a universal child permission envelope or complete context-isolation contract. These limits do not imply absent behavior. Reusable instruction admission and release machinery changes are independently recorded in [RT-RTE-skill-upload](#rt-rte-skill-upload) and [RT-RTE-release-update](#rt-rte-release-update); neither is evidence of autonomous self-improvement.

## Shared records

### Components

#### RT-CMP-claude-model
Label: Claude-selected model

Source-native identity: Claude Code's selected `model` in SpawnConfig, passed as a `--model` option when supplied. Representational form: distributed-parametric inference behind the external Claude executable/service; parameter storage is provider/native-runtime owned, not this checkout. SRC-1 `src/local/claude.rs` and `src/local/harness/claude.rs` establish invocation, not provider internals.

> if let Some(model) = &spec.config.model {
>         cmd.args(["--model", model]);
>     }
> --- `src/local/claude.rs`

Parameters changing during operation: uninspected at the external provider; the inspected ORX path sends no weight-training update. Exact version pinned: no immutable weight revision is enforced by this invocation; an optional model string or native default is used. Mutable endpoint resolving to another model: possible under the external model/default contract, not controlled here. Per-session native state and textual instructions can change behavior without changing these parameters.

#### RT-CMP-codex-model
Label: Codex-selected model

Source-native identity: the Codex session model/provider selected through the native adapter. Representational form: distributed-parametric; storage substrate and inference implementation are external. SRC-1 `src/local/harness/codex.rs` supplies the adapter and provider-sensitive policy path.

> first_party_provider && first_party_url
> --- `src/local/harness/codex.rs`

This predicate governs availability of automatic approval review, not scientific answer checking. Parameters changing during operation: provider internals uninspected; inspected policy code does not update weights. Exact version pinned: no weight-level pin established. Mutable endpoint: provider configuration and native defaults can resolve differently; this report does not authenticate the served model or automatic-review model. The separate hidden review component's exact version and parameter behavior are opaque.

### Operative objects

#### RT-OBJ-playbook
Label: Session playbook

Source-native identity: playbook produced by `ensure_playbook` from `SYSTEM_PROMPT.md`, project facts/state and skill names. Representational form: natural-language instructions plus embedded symbolic identifiers, stored as a worktree file; the native model interprets the instructions. SRC-1 `src/local/opencode.rs` and `SYSTEM_PROMPT.md`.

> let project_state = ProjectState::load(&project.id)?;
>     std::fs::write(&playbook, playbook_md(project, &project_state))
> --- `src/local/opencode.rs`

It requests tool selection, evidence citation and environment practice. Refreshing the file every turn does not prove the resident model rereads it every turn; Claude rereads its appended file on respawn (SRC-1 `src/local/harness/claude.rs`). It is not an enforcement engine or an observed research theory revision.

#### RT-OBJ-source-snapshot
Label: SourceSnapshot

Source-native identity: `SourceSnapshot` with revision, digest, size, path and optional Ray package. Representational form: symbolic archive/container metadata and committed program files; filesystem content-addressed tar/zip caches and run descriptors record its substrate. The files may contain natural-language instructions, but this record concerns source selection for execution. SRC-1 `src/compute.rs`.

> let revision = crate::local::git::local_head_sha(repo, &experiment.branch_name)?;
> --- `src/compute.rs`

> let path = dir.join(format!("{digest}.tar"));
> --- `src/compute.rs`

The branch tip is mutable before submission; the recorded revision/archive binds this run's code. This does not pin data, secrets, dependencies or remote services used by that code.

### Routes

#### RT-RTE-chat-turn
Label: User message to native turn

Endpoints and progression: UI/API user request → ChatHost `send_message` → `SendTurnRequest` with QueueIfBusy → harness dispatch → wire parts and persisted turn result. The user supplies the problem and session; code owns admission/serialization, and the native model owns next tool/text decisions. Settings and selected model/permission travel in TurnCtx. Native resume state and the ORX transcript have separate stores. SRC-1 `src/local/chat/mod.rs`, `src/local/harness/claude.rs`, `src/local/claude.rs`.

> admission: TurnAdmission::QueueIfBusy,
> --- `src/local/chat/mod.rs`

> Some(harness) => harness.run_turn(&mut ctx).await,
> --- `src/local/chat/mod.rs`

- Immediate return: started/queued/existing turn identity; asynchronous parts subsequently reach the UI.
- Later read-back: native resume can reuse prior context; when native state is missing, Claude can prepend a flattened ORX transcript snapshot bounded to 32 KiB by the harness recovery helper.
- Delegated visibility: native harness receives prepared text, attachments and playbook in its session worktree; event handling normalizes native output. Full native child-context rules remain external.
- Selection predicate: session harness/model/settings choose adapter and context; native-session existence chooses resume versus recovery text.
- Invalidation or expiry: config change, crash or interrupt can require child respawn; stale held prompts are resolved. Host startup reconciles unfinished turns and queues.
- Activation or effect: wired path can produce file/tool effects through the native runtime and terminal assistant/error parts; compliance and successful effects unobserved.
- Evidence limits: source implementation only; no observed invocation or backend parity result.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Recovery is not transparent identity with the missing native context. The snapshot flattens text, tool labels/status and prompt state, preferentially retaining newest entries; it does not restore all original tool bodies. ORX's 30-minute no-event watchdog and bounded retry scheduling are recovery policies, not proof against hangs or duplicated external effects (SRC-1 `src/local/harness/mod.rs`). Claude authentication recovery retries only its checked rejected/no-activity case (`src/local/harness/claude.rs`).

#### RT-RTE-permission-review
Label: Native tool permission review

Endpoints: native tool request → bridge token/policy checks → automatic allow/deny or held user card → native reply. ChatHost owns bridge validity and review serialization; human answers gray-area requests. Claude and Codex do not share identical enforcement. SRC-1 `src/local/chat/mod.rs`, `src/local/claude.rs`, `src/local/harness/codex.rs`.

> _ => return Err(anyhow!("unknown or stale gate token")),
> --- `src/local/chat/mod.rs`

> PermissionMode::Plan => ("workspace-write", "on-request", "user"),
> --- `src/local/harness/codex.rs`

- Immediate return: bridge allow/deny or pending review; native request remains held while the user decides.
- Later read-back: inapplicable — this is permission delivery, not a retained-knowledge write; prompt resolution persists for UI/recovery.
- Delegated visibility: bridge receives tool name and JSON input, not every operation available to the native process.
- Selection predicate: Claude Manual/Accept edits/Plan use the bridge when configured; Auto/Bypass do not require that bridge. Plan auto-policy allows recognized read-only Bash and web reads, denies named editing tools, reviews other requests.
- Invalidation or expiry: child token change, ended turn, timeout and pending-guard cleanup invalidate held decisions; queued reviews revalidate token and busy state.
- Activation or effect: native runtime is asked to honor the decision; bypass can return updated input directly when not in Plan and not an exit-plan/question request.
- Evidence limits: no native-runtime execution verified; a missing bridge configuration is logged, not proof of all-tool coverage.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: native model proposes an action, code can deny/review it and the user can veto reviewed actions. This is open-request operation with no expected-answer oracle. Guarantee strength: protocol for authenticated bridge requests, policy for plan restrictions; required external contract is native enforcement. The separate human shell route is outside this guarantee. Codex's provider-supported automatic reviewer delegates judgment to another opaque model; it does not establish equivalent human oversight or correctness.

#### RT-RTE-user-shell
Label: Operator shell command

SRC-1 `ui/src/api.ts`, `src/commands/up.rs`, `src/local/chat/mod.rs`: a shipped API caller posts a command to the session shell endpoint. The endpoint checks stopping/moving, nonempty input, idleness and session/project existence, resolves the checkout, then invokes Bash. It does not read Plan/permission mode on this path.

> let mut spawn = tokio::process::Command::new(crate::local::bash::program());
> --- `src/local/chat/mod.rs`

- Immediate return: user-role tool message with command, cwd, exit/signal/timeout metadata and capped stdout/stderr.
- Later read-back: persisted shell result joins the session transcript; later native consumption depends on subsequent context preparation.
- Delegated visibility: inapplicable — command executes directly through the host shell, not a delegated model decision.
- Selection predicate: caller supplies command; host supplies the resolved session checkout and environment.
- Invalidation or expiry: shell timeout kills its process group; output drain is bounded even if background children retain pipes.
- Activation or effect: OS-user Bash effects, potentially outside the checkout; cwd is not a sandbox.
- Evidence limits: source wiring establishes reachability from a shipped caller, not model exploitation, authenticated deployment security or successful command execution.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The caller is the proposing/deciding principal; this route contains no per-command native permission review or answer oracle. Ordinary shell mutations are admitted through caller authority, not a scientific revision gate. It can change project files but does not itself commit them into the compute snapshot.

#### RT-RTE-experiment-run
Label: Snapshot experiment submission

SRC-1 `src/commands/exp.rs`, `src/plane/local_plane.rs`, `src/compute.rs`, `src/local/localrun.rs`, `src/commands/supervise.rs`: experiment-ID launch resolves backend defaults, validates flags, optionally forwards through trusted up, preflights the backend, stages source and reserves a starting run. The local controller extracts that archive into a run directory, executes the inherited run command and spawns detached supervision. Code owns scheduling/state; the user/agent supplies experiment content and run command.

> if !force {
>         if let Some(run) = store
>             .list_runs_by_experiment(&pending.experiment_id)?
>             .into_iter()
>             .find(|run| !crate::local::is_terminal(&run.status))
> --- `src/compute.rs`

> commit_sha: Some(source.revision),
> --- `src/local/localrun.rs`

- Immediate return: run ID and backend handle/directory after submission; completion is asynchronous.
- Later read-back: run row, source revision/descriptor and supervisor log are available through status/runs/logs commands and UI; optional wake-up initiates a later agent turn.
- Delegated visibility: local run receives archive-selected code, run command and configured environment; other compute providers receive backend-specific submissions whose detailed parity is uninspected here.
- Selection predicate: experiment branch tip supplies source; experiment command overrides project default; explicit/persisted backend defaults choose executor. Without trusted up the standalone dispatch still reaches the local compute submission path.
- Invalidation or expiry: new submissions select new revisions; existing archives remain run-specific. Cancellation sets intent and supervisor attempts backend cancellation; startup can reattach supervision.
- Activation or effect: wired local shell execution, polling, terminal status and log mirroring; these are not measured-result validation.
- Evidence limits: only local controller traced end to end; no run performed and no conclusion about remote reliability or full dependency reproducibility.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: user/agent proposes branch/code/command; Git commits supply executable code; software validates flags/readiness and can reject a concurrent in-flight run unless explicitly forced. File locking plus transactional reservation handles that check. Source archive execution is a protocol, not an OS isolation guarantee. A backend handle is recorded before final run persistence; local submission cancels the launched job if handle recording fails. Supervisor recovers independent of a chat process, mirrors logs, applies run state and handles cancel requests. Missing scientific outcomes are not manufactured from process success. Operating mode is an open research request with externally chosen experiments, not a built-in scored curriculum. No scientific answer oracle or automatic successor experiment selection is established by this route. Rollback is cancellation/new branch/revision rather than automatic reversion of research conclusions. This admits changed research code, not a demonstrated change to ORX's own organization.

#### RT-RTE-run-wakeup
Label: Run completion to hidden turn

SRC-1 `src/commands/exp.rs`, `src/local/chat/mod.rs`: an agent explicitly registers its launching chat for the latest experiment run. The host watcher prunes subscriptions, selects earliest ready wake-up per session, claims an idle turn and durable delivery token, formats status-only text and sends a hidden message. Code, not a new user message, triggers the resumed model.

> match chat
>             .send_hidden_message(&wakeup.chat_session_id, text, guard)
>             .await
> --- `src/local/chat/mod.rs`

- Immediate return: registration reports scheduled/already pending/already delivered; no synchronous experiment result.
- Later read-back: pending subscription and recorded run status cause a later agent invocation; delivered state is recorded only for a started hidden turn.
- Delegated visibility: hidden turn gets run ID/status and instructions to inspect runs/logs, not full measured results automatically.
- Selection predicate: explicit session/run subscription, ready pending state and idle claim; cancelled runs do not produce the completion text, lost outcomes receive an uncertainty warning.
- Invalidation or expiry: pruning, claim release on failure/non-start, delivered marking and session deletion/expiry govern pending work.
- Activation or effect: wired unsolicited resumption after prior opt-in; subsequent log inspection/behavior is unobserved.
- Evidence limits: no delivery trace; claim/delivery mechanics do not establish exactly-once external tool effects or interpretation correctness.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The message is a scheduling stimulus, not an answer oracle. Monitoring failures have a separate alert path that leaves terminal wake-ups pending. This prevents treating inability to monitor as scientific failure or success.

#### RT-RTE-skill-upload
Label: Reusable instruction admission

SRC-1 `agent-skills/orx-customize/SKILL.md`, `src/local/user_skills.rs`, `src/local/opencode.rs`: a caller uploads UTF-8 SKILL.md or a supported archive; code parses frontmatter, validates names/paths/budgets and writes a reusable folder. The native session copy is refreshed through `ensure_playbook` on subsequent turns.

> // A re-upload fully replaces the prior version — no stale sibling files.
> --- `src/local/user_skills.rs`

- Immediate return: saved skill identity/replacement result; source content is retained in the active data directory.
- Later read-back: content-aware copying updates managed native skill folders for later turns across projects; discovered native skills remain native rather than explicit uploads.
- Delegated visibility: native harness sees files in its skills directory; model loading and compliance are external behaviors.
- Selection predicate: upload name identifies replacement; an existing project-owned skill of the same name wins over an unmanaged session overwrite.
- Invalidation or expiry: changed source replaces managed copies, removed/inapplicable sources are pruned; supporting-file content comparison detects changes, not just timestamps.
- Activation or effect: wired instruction distribution; running resident harness need not immediately reload content.
- Evidence limits: no observed upload or subsequent behavioral change; file-format validation is not epistemic review.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger/proposal: user asks to save reusable guidance; agent can prepare files and invoke the CLI. Human request is not per-content approval: the write path performs software validation, not a required human acceptance of every instruction. Guidance requests reusable skills/templates and says same-name replacement is complete. Rejection is structural (format/name/path/budget), not a quality oracle. Recovery requires replacing/re-uploading content; the inspected delete-then-write implementation does not establish automatic rollback on partial failure. This is a capability/instruction admission path, not established trace-fed learning or self-improvement. Theory properties are not assigned merely because a skill can contain prose.

#### RT-RTE-release-update
Label: Release machinery update

SRC-1 `src/updates.rs`, `src/commands/up.rs`: a user apply request or periodic update pass can start the separate updater. Code checks opt-out, installation-channel eligibility, cached newer semantic version and attempt schedule; release maintainers provide candidate binaries. The host can later drain and restart into replaced code.

> if outdated && attempt_due(cache.as_ref()) {
>         spawn_background_update();
>     }
> --- `src/updates.rs`

- Immediate return: user apply waits for updater success/failure subject to timeout; timeout can leave the updater running.
- Later read-back: update cache/status and executable-on-disk checks drive later restart decisions.
- Delegated visibility: separate updater receives installation/release context; no model-based proposal generation shown here.
- Selection predicate: version/channel/opt-out/attempt rules select availability; auto restart additionally checks changed executable/deferred update and host idleness.
- Invalidation or expiry: cached availability and attempts are refreshed; busy host defers restart and reopens admission if restart cannot commit.
- Activation or effect: standing path can replace production machinery and restart the host; no installed update observed.
- Evidence limits: platform-specific installer/swap and release authenticity controls not traced; updater success status does not establish new-version quality.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission is maintainer release plus channel/software policy, optionally initiated by a human; automatic mode is not per-release human approval. Explicit opt-outs reject update activity, and eligibility prevents treating every installation as self-managed. `begin_restart` commits only after request/data-move/remote-session/chat-idleness checks. This is a protocol for continuity, not a deployment guarantee. Rollback of installed platform binaries remains uninspected. There is no research answer oracle, trace-responsive revision of ORX by its own model, or observed self-improvement in this inspected route.

### Claims

#### RT-CLM-research-assistance
Label: Project research assistance

Claimed operation: the shared prompt assigns ideation, literature review, hypothesis formulation, execution and artifacts to the project agent. Source: SRC-1 `SYSTEM_PROMPT.md`, doctrine/design.

> You are an OpenResearch agent helping the user across the research process,
> including ideation, literature review, hypothesis formulation, experiment
> execution, and artifact generation.
> --- `SYSTEM_PROMPT.md`

The adapters/compute wiring support a capacity to request these activities, not an effectiveness conclusion, autonomous completion of every research phase, or valid theories produced.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-playbook-injection
Label: Playbook instruction authority

Consumer: Claude Code's model session. Channel: `--append-system-prompt-file` at child spawn. Force: natural-language guidance interpreted by the native runtime/model, not a symbolic file-access guard. Horizon: resident session until respawn, then a refreshed playbook can enter. SRC-1 `src/local/claude.rs`, `src/local/harness/claude.rs`, linked object [RT-OBJ-playbook](#rt-obj-playbook).

> .arg("--append-system-prompt-file")
>     .arg(&spec.playbook)
> --- `src/local/claude.rs`

Delivery is wired; activation and downstream quality unobserved. Uploaded skills have a separate file distribution channel, not automatically the same system-prompt force.

## Annotations

none
