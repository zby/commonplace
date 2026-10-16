---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "CORAL runtime baseline: coding-agent launch, asynchronous evaluation, feedback, steering and island migration at the frozen commit."
run-id: AAS-2026-10-15-coral-25e5fdab9dc4-01
reviewed-boundary: "0123dfb939b35228cf2c1fde224cd0561e727408"
---

# CORAL runtime report

## Runtime account

CORAL owns the outer experiment loop, not the inner model/tool loop. It takes a task configuration, code seed and packaged grader; provisions agent worktrees and shared-state access; launches external coding harnesses; evaluates submitted commits; and restarts agents with feedback. This is the source-native basis for its claim of autonomous organizations, not evidence of successful autonomous research ([RT-CLM-agent-organizations](#rt-clm-agent-organizations)). All findings below use SRC-1 at the boundary's frozen commit. Implementation is inspected source, prompts are doctrine/design, and actual operation, compliance and benefit remain unobserved. No target code, tests or examples were executed.

### Ordinary shipped invocation

A representative ordinary path is `coral start -c task.yaml` with the default Claude Code runtime. The operator supplies the objective and evaluation machinery. CLI configuration and overrides select the runtime, model, workspaces and session wrapper. Local execution enters the manager directly; tmux and Docker wrap a reissued command. `cmd_start` performs structural task validation before `AgentManager.start_all()`. This is not the baseline-grading loop of `coral validate`: structural validation checks configuration, grader entrypoint/direction and private-data placement. The separate validation runner grades the baseline. Sources: SRC-1, `coral/cli/start.py`, `coral/cli/validation.py`, `coral/task/validation.py`.

The manager creates the project, starts optional gateway and sandbox services, starts the grader daemon, seeds heartbeat configuration, optionally runs a research phase, then provisions each worktree and starts its harness. Agent identity is carried in `.coral_agent_id`, the `coral/<agent>` branch, role file and attempt metadata. The island breadcrumb and manager's live island map determine shared-state routing. Resolved assignment specs may select different runtimes/models per agent. Generated `CLAUDE.md` or `AGENTS.md`, runtime settings, role seeds and optional mounted files supply model-facing guidance. The model chooses the next implementation action; CORAL's code chooses launches, interrupts, feedback scheduling and migration. See [RT-RTE-agent-launch](#rt-rte-agent-launch), [RT-CMP-model-endpoints](#rt-cmp-model-endpoints) and [RT-BAP-generated-instructions](#rt-bap-generated-instructions).

A harness subprocess works inside its Git worktree and can invoke shell/tool operations. Worktree separation provides independent checked-out code, not an unconditional filesystem security boundary. Shared notes, skills, roles, attempts and logs are reachable through symlinks into public or island state. This is coordination through shared files and scored commits, not a central model choosing every colleague's task. The generated prompt asks agents to choose complementary roles and use specialist subagents. Those delegation instructions do not establish that any harness created a subagent or that its context isolation worked ([RT-RTE-specialist-delegation](#rt-rte-specialist-delegation)).

For evaluation, the agent calls `coral eval -m ...`. Submission stages and commits current code, checkpoints shared state, and writes an attempt with `status="pending"`. The daemon checks out that commit into a detached evaluation worktree, calls the configured packaged grader in its private Python environment, removes the checkout, and writes score/status/feedback. The normal caller waits for finalization; asynchronous submission returns a pending record instead. The terminal artifact of an iteration is a committed candidate plus finalized attempt, not automatic promotion of that candidate into a deployment. See [RT-RTE-eval-submission](#rt-rte-eval-submission), [RT-OBJ-attempt](#rt-obj-attempt) and [RT-RTE-grader-execution](#rt-rte-grader-execution).

The manager polls finalized attempts. It derives score history, checks stop conditions and heartbeat rules, then interrupts the committing agent and resumes its session with a score header and selected prompts. The changed source code remains the candidate product; knowledge/role/skill edits are separate agent-authored material, not a prerequisite checked by submission. Detailed retained-knowledge revision belongs to the memory report. See [RT-RTE-heartbeat-feedback](#rt-rte-heartbeat-feedback). A requested reflection or consolidation is not verified completion of that work.

### Selected forcing routes and guarantee coverage

Four forcing cases constrain the baseline:

1. **Uncontained alternate harness.** Codex launch bypasses its native approvals and sandbox on both fresh and resume paths. Claude instead uses `auto` without OS containment, but skips permission checks when a sandbox spec or isolated user is supplied. Claude's settings grant general Bash as well as scoped file tools. Neither file-tool settings nor generated prohibitions prove that arbitrary shell or provider-native tools cannot access host files. An optional outer process wrapper is the stronger control. See [RT-CLM-isolation-scope](#rt-clm-isolation-scope).
2. **Asynchronous/tune evaluation.** `wait=False` returns before a score exists. `tune=True` changes budget metadata; it does not universally choose a cheaper workload. Only a task grader that implements a tune distinction can provide that distinction. Manager plateau history excludes tune and grader-error budgets, but interval actions use counters computed separately. Thus “tune never triggers any heartbeat” is broader than the inspected monitor implementation supports. See [RT-RTE-eval-submission](#rt-rte-eval-submission) and [RT-RTE-heartbeat-feedback](#rt-rte-heartbeat-feedback).
3. **Durable resume, rewind and migration.** Resume may recover a harness session or start fresh with pointers to retained files. Steering can rewind descendant worktrees and archive discarded attempts. Migration preserves agent identity/session while changing its shared-state island and permission configuration; notes/skills stay on the source island. It is not simply a prompt announcing a move. See [RT-RTE-resume-steering](#rt-rte-resume-steering) and [RT-RTE-island-migration](#rt-rte-island-migration).
4. **Advertised Pi entry path.** The registry exposes Pi, but the inspected Pi `start` signature lacks the `sandbox` keyword unconditionally passed by the manager. This is a static interface defect even when sandboxing is disabled (`None` is still passed), not evidence of successful Pi launch or a silent fallback to unsandboxed operation. The default Claude and inspected Codex signatures accept it. See [RT-CLM-pi-launch](#rt-clm-pi-launch).

Load-bearing guarantees have different owners and enforcement points:

| Guarantee and owner | Enforcement, strength and covered paths | Alternate paths / external contract | Separate conclusions |
|---|---|---|---|
| Candidate snapshot stability; grader daemon | Detached worktree at attempt commit, removed in `finally`; **protocol** for daemon-mediated evaluation | Agent edits to its live worktree do not change that checkout. Mutable external data, installed grader code and services are not snapshotted by this mechanism. A dependency environment is not a security sandbox. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Evaluation timeout; subprocess grader | `subprocess.run(timeout=self.timeout)`; **protocol** for the grader worker, with zero configured as no limit | This bounds the waited worker, not a proved kill of every descendant process or remote service. Grader-specific subprocess and service management remains task-dependent. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Host/private-state protection; launch integration | Optional SRT settings/prefix or OS-user privilege separation; **deployment guarantee** only under a correctly enforcing external OS/runtime | Local no-isolation paths, custom adapters, direct shell/provider traffic and overridden sandbox settings prevent a universal claim. Docker adds read-only task mount and private volume. No deployed envelope was supplied. | implementation conclusion status: wired; operation conclusion status: uninspected |
| No human approval during work; adapter and prompt authors | Headless prompts, runtime flags and some tool denies; **policy** for requested behavior, with configured approval flags on inspected launches | External harness interpretation remains a dependency. Starting a run is not approval of every code or knowledge edit. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Score-driven continuation; manager | Finalized-attempt filtering, budget classification, stop conditions, heartbeat selection and interrupt/relaunch; **best effort** | Polling, process crashes, missing sessions and batched arrivals limit delivery. Source marks all scored-new files seen but reads one latest attempt for feedback; do not assume one interrupt per finalized file. | implementation conclusion status: wired; operation conclusion status: uninspected |

Evidence: SRC-1, `coral/grader/daemon.py`, `coral/grader/subprocess_grader.py`, `coral/agent/manager.py`, `coral/agent/runtime.py`, `coral/sandbox/srt.py`, `coral/cli/start.py`, and the route/claim passages below. These are source-level conclusions, not deployment certification.

### Runtime-client controls, recovery and admission

The operator can choose local/tmux/Docker sessions, models, assignments, research, runtime mounts, optional gateway/sandbox, turn cap and stop thresholds. Max-turn behavior belongs partly to adapters: Claude forwards a positive cap; the inspected Codex/Pi command construction does not establish equivalent cap enforcement. Manager restarts, session extraction and fresh-start fallback provide recovery, not guaranteed preservation of all model-visible context. Stall and burst-restart mechanisms exist in manager code; their source policies are not measured reliability. Grader timeout/crash classification returns terminal feedback with grader-error budget rather than a successful score. Stopping leaves code and attempt files for later inspection/resume (SRC-1, `coral/config.py`, `coral/agent/manager.py`, `coral/grader/daemon.py`).

Task authoring and dynamic runtime/grader/sandbox imports admit changes to production machinery through configuration and installed packages. Mounts can replace runtime guidance/settings. Heartbeat commands admit future prompt/cadence changes. These are distinct from candidate-code admission through `coral eval`; neither path proves promotion into an external product or weight training ([RT-RTE-machinery-admission](#rt-rte-machinery-admission)). Memory revisions are left to the memory analyst.

Gateway observability is optional. Adapter settings/environment redirect selected harness requests to LiteLLM; middleware identifies agents by keys, stamps metadata and logs traffic. Its sole-agent fallback can attribute an unmatched key with a warning. This is not complete provenance for every model call: traffic outside the configured base URL, custom extension calls and direct shell network traffic need not traverse it. The default sandbox network mode is open through a proxy, not a model-provider allowlist. The provider itself and its logs are not frozen execution evidence (SRC-1, `coral/gateway/middleware.py`, `coral/config.py`, `coral/sandbox/srt.py`).

Additional inspected coverage under SRC-1 extends the boundary's initial reads: runtime protocol/registry; Claude and Codex launch settings/commands; Pi signature/command; heartbeat selection; manager launch, interruption, resume, steering, feedback and migration application; migration planning; warm-start runner; grader loader/worker/daemon evaluation; SRT settings builder; task structural validation; plugin session hook and task-authoring skill; librarian prompt; and circle-packing verifier. All are implementation or doctrine/design, not observed runs. Other built-in adapters, frontend controls, all task graders, full maintenance-skill transformations, provider-native tool policies and host compaction remain uninspected in detail. They prevent completeness claims about adapter parity, context management, evaluation security and realized improvement, not the bounded route descriptions here.

## Shared records

### Components

#### RT-CMP-model-endpoints
Label: External coding-harness model endpoints

The inspected launch paths pass model strings to external harnesses: default configuration uses `sonnet`; registry defaults include `gpt-5.4` for Codex and `zai/glm-5.1` for Pi. The operative models are distributed-parametric components hosted behind external harness/provider interfaces, not weights stored in the CORAL repository. CORAL retains symbolic model identifiers in YAML/specs/argv and natural-language instructions in files. The provider's storage substrate and internals are uninspected.

Parameter changes during operation: uninspected — the inspected CORAL paths launch inference clients and do not expose provider training or model-update internals. Exact model version pinned: not established for the general route; aliases such as `sonnet` are not weight digests. Mutable endpoint can resolve to another model: yes as an integration possibility, because model/base URL and optional LiteLLM configuration are externally resolved/configurable. The shipped `litellm_config.yaml` names dated Claude models but neither pins provider weights nor forces every run to use that file. This conclusion does not deny adaptation through retained files.

Evidence: SRC-1, `coral/config.py`, `coral/agent/registry.py`, `coral/agent/builtin/claude_code.py`, `coral/agent/builtin/codex.py`, `litellm_config.yaml`.

> "claude_code": "sonnet",
> "codex": "gpt-5.4",
> --- `coral/agent/registry.py`

### Operative objects

#### RT-OBJ-attempt
Label: Attempt record

Source-native `Attempt` is a symbolic record serialized as JSON under shared-state `attempts/<commit_hash>.json`; free-text title/feedback are natural-language parts interpreted by agents. It associates candidate commit, agent, parent, timestamp, score/status, budget metadata and shared-state checkpoint lineage. Submission creates pending state; the daemon constructs finalized state while preserving submission identity. Later manager reads drive scheduling and feedback. It is not itself proof of test correctness or of a knowledge revision. Evidence: SRC-1, `coral/hooks/post_commit.py`, `coral/grader/daemon.py`, `coral/agent/manager.py`.

> # Write pending record. The grader daemon will observe this and fill in
> # score/status/feedback asynchronously.
> --- `coral/hooks/post_commit.py`

#### RT-OBJ-task-config
Label: Task configuration and runtime options

Source-native `CoralConfig` is symbolic YAML/dataclass state; task description and embedded prompt strings have natural-language consumption paths. Files and resolved in-memory assignment specs select grader imports, runtime/model, workspace setup, isolation, mounts, heartbeat and stopping policy. Configuration is supplied by a caller and saved for a run; author identity or human review cannot be inferred from its existence. Evidence: SRC-1, `coral/config.py`, `coral/cli/start.py`, `coral/agent/manager.py`.

> # Apply per-agent file mounts last so the user's files win over
> # CORAL's defaults (e.g. dropping a custom .claude/settings.json
> # next to CORAL's settings.local.json — Claude Code merges both).
> --- `coral/agent/manager.py`

### Routes

#### RT-RTE-agent-launch
Label: Ordinary agent launch and coding loop

Operator CLI → structural validator → manager → project/worktree → external harness → candidate edits. Manager owns provisioning and process launch; the external model/harness owns tool-turn decisions. State includes agent/island breadcrumbs, per-agent worktree, shared-state links, runtime settings, instruction file and logs. Instructions are natural language; launch configuration and process calls are symbolic. Executor is the harness subprocess under configured host privileges, not a CORAL model interpreter. Evidence: SRC-1, `coral/cli/start.py`, `coral/agent/manager.py`, `coral/workspace/worktree.py`, `coral/agent/builtin/claude_code.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `start_all` returns handles; CLI prints PIDs/paths and enters monitoring rather than returning a completed solution.
- Later read-back: launch/relaunch exposes existing role/shared files and may resume a harness session; retained-content selection and revisions are left to memory analysis.
- Delegated visibility: agents see their worktree and configured public/island links; effective visibility beyond that depends on isolation and harness tools.
- Selection predicate: resolved runtime/model assignment and live island identity select adapter and shared root; model selects subsequent edits.
- Invalidation or expiry: process exit/interrupt ends a launch; worktree readiness marker avoids repeated environment setup; instruction/settings generation repeats on relaunch.
- Activation or effect: code provisions files and launches a process; successful tool use and instruction compliance are unobserved.
- Evidence limits: dependencies, credentials, harness internals and actual launches were not exercised; Pi has the separate interface defect below.

Operating mode: open optimization within a task-defined metric, not unrestricted control of all CORAL machinery. Proposal/decision: model proposes candidate edits; CORAL commits only when eval is called. Human contribution: initial objective/configuration and optional later steering; no per-edit approval in this source path. Oracle: task grader, not the coding model's confidence. Product admission/rejection/rollback is described in [RT-RTE-eval-submission](#rt-rte-eval-submission) and [RT-RTE-resume-steering](#rt-rte-resume-steering).

> manager = AgentManager(config, verbose=verbose, config_dir=config_path.parent)
> handles = manager.start_all()
> --- `coral/cli/start.py`

#### RT-RTE-eval-submission
Label: Candidate commit and pending evaluation admission

Agent or caller → `submit_eval` → queue-cap check → Git commit → shared-state checkpoint → pending JSON → optional poll. The proposer chooses code and message; software admits the current working-tree changes to the attempt stream. A score does not gate creation of that commit. No mandatory human approval is implemented here. The checkpoint captures shared files; it does not verify that their claims are justified. Evidence: SRC-1, `coral/hooks/post_commit.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: final Attempt by default; pending Attempt with `wait=False`; timeout/error raises rather than providing a score.
- Later read-back: daemon consumes pending JSON; manager and agent later consume finalized attempt, feedback and checkpoint linkage.
- Delegated visibility: shared attempt state is available through the current island/public root; grading receives the committed code snapshot.
- Selection predicate: current code changes and discovered agent/island context; queue cap rejects excess pending submissions when enabled.
- Invalidation or expiry: pending becomes terminal after daemon grading; polling has a timeout; archived/discarded attempts can later leave active views through steering.
- Activation or effect: Git stages/commits the candidate and publishes pending evaluation state, not a production deployment.
- Evidence limits: queue count is a producer-side check, not proof against concurrent bypassing writers; source supports intended admission, not observed submissions.

Admission trigger: `coral eval`; proposed change: edited worktree. Rejection ability: missing config/breadcrumb, queue cap, no staged changes or Git errors can reject submission. The later grader can score failure without undoing the commit. Recovery: inspect/revert/checkout a prior candidate or use resume steering; waiting can be retried without implying regrading. Guidance: generated plan → edit → eval loop; rationale persists in message and candidate commit. Tune mode stamps `budget_class="tune"`; actual cheaper evaluation is grader-specific. There is no universal expected-answer oracle at submission. The operating mode is task optimization with optional tune experiments.

> # Git add + commit
> commit_hash = _git_add_and_commit(message, str(workdir_path))
> parent_hash = _get_parent_hash(commit_hash, str(workdir_path))
> --- `coral/hooks/post_commit.py`

> if not wait:
>     return attempt
> --- `coral/hooks/post_commit.py`

#### RT-RTE-grader-execution
Label: Isolated snapshot grading and finalized feedback

Pending attempt → daemon → detached Git checkout → configured `SubprocessGrader` worker → ScoreBundle → finalized Attempt. The task author supplies the grader and evaluation criterion; code dispatches it and compares scores using maximize/minimize direction. Worker imports a `TaskGrader` subclass in the private grader environment, passes codebase path/task/island metadata, and returns JSON. This is dependency isolation and snapshot selection, not proved hostile-code containment. Evidence: SRC-1, `coral/grader/daemon.py`, `coral/grader/loader.py`, `coral/grader/subprocess_grader.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: grader returns ScoreBundle or exception; daemon writes finalized score/status/feedback, including timeout/crashed classifications.
- Later read-back: manager polls finalized attempts; waiting agent sees final result and can read eval logs.
- Delegated visibility: worker receives candidate checkout path, task metadata and private-dir path; public score breakdowns depend on bundle visibility handling.
- Selection predicate: pending attempts at known commit hashes; grader entrypoint and direction are configured by task author.
- Invalidation or expiry: temporary checkout removed in `finally`; attempt/log artifacts remain; timeout is disabled when configured as zero.
- Activation or effect: worker executes task evaluation; daemon updates attempt and eval count; neither proves candidate correctness beyond the grader's actual tests.
- Evidence limits: external task resources and descendant cleanup are not established by a worker timeout; no grader run was supplied.

Answer oracle is task-dependent. In inspected circle packing, the supplied verifier checks shape, NaNs, negative radii, bounds and pairwise overlaps, recomputes the sum, and normalizes by `BENCHMARK = 2.635977`. That benchmark is a reference outcome, not an exact target answer the model must reproduce. It supports metric-directed comparison, not general solution correctness. The agent's returned sum is not blindly used as the score. Other graders, including LLM-judge patterns described by the plugin, are not equivalent oracles. Human author chooses criterion; software computes and records score/status; model uses feedback to choose the next candidate. Mode: bounded task evaluation, optionally tune-classified. Evidence: SRC-1, `examples/circle_packing/grader/src/circle_packing_grader/grader.py`.

> actual_sum = float(np.sum(radii))
> score = actual_sum / BENCHMARK if BENCHMARK > 0 else 0.0
> --- `examples/circle_packing/grader/src/circle_packing_grader/grader.py`

> timeout=self.timeout,
> --- `coral/grader/subprocess_grader.py`

#### RT-RTE-heartbeat-feedback
Label: Finalized score to resumed agent instructions

Manager polling → finalized attempt filtering → budget/history/stop checks → HeartbeatRunner → selected prompt text → interrupt and resume. Code decides interval/plateau triggers and stop conditions; the resumed model decides how to respond. User/caller can supply custom heartbeat text/cadence through CLI. Feedback contains selected score, short commit, title, budget marker and grader feedback, followed by action prompts. It is not the full experiment history. Evidence: SRC-1, `coral/agent/manager.py`, `coral/agent/heartbeat.py`, `coral/cli/heartbeat.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: manager replaces a live handle after interruption/relaunch; no proof of completed reflect/consolidate work is returned.
- Later read-back: finalized attempts are reread for scheduling; resumed harness may reload its saved session and shared artifacts.
- Delegated visibility: prompt goes to the committing live agent selected by manager, not automatically to every colleague; other agents can inspect shared outputs.
- Selection predicate: interval counts or plateau streak with epsilon, score direction and configured action scope; auto-stop can preempt heartbeat.
- Invalidation or expiry: pending attempts do not trigger; seen files leave the new-attempt set; changed heartbeat files affect later runner construction; missing session falls back to fresh start.
- Activation or effect: SIGINT and launch with combined prompt are wired; requested reflection/knowledge creation and resulting behavioral change remain unobserved.
- Evidence limits: source processes one latest attempt from a scored-new set after marking that set seen; no per-attempt delivery guarantee or demonstrated prompt compliance.

Admission: heartbeat `set` can change future guidance after value/scope checks; custom names require a prompt. Human or agent caller may propose it; software writes the config, not a human approval gate. Remove/reset afford recovery subject to protected-action rules. The active model may then propose knowledge/capability changes under those instructions; memory revisions are not judged here. Oracle: grader score for triggering, not an oracle for whether consolidation is true. Mode: cadence/plateau-triggered intervention within open task optimization.

> combined_prompt = "\n\n".join(prompts)
> names = ", ".join(action_names)
> --- `coral/agent/manager.py`

> if name not in DEFAULT_PROMPTS and not prompt:
> --- `coral/cli/heartbeat.py`

#### RT-RTE-resume-steering
Label: Session resume and candidate rewind

Operator resume or queued `ContinueFromAction` → ancestry matching → reset selected worktrees and archive discarded attempt segments → recover session or fresh prompt → relaunch. Manager chooses affected worktrees by ancestry, not by semantic relevance. User/caller selects target hash and optional instructions; queued actions may originate in the dashboard. This route changes active candidate code and future agent guidance, not necessarily all retained state. Evidence: SRC-1, `coral/agent/manager.py`, `coral/hub/steering.py`, `coral/cli/start.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: resumed agent handles and monitoring; an unmatched steering action does not reset an unrelated worktree.
- Later read-back: saved harness sessions or fallback prompts point to leaderboard, notes, skills and prior attempts; archived JSON/Git objects stay on disk.
- Delegated visibility: each resumed agent gets its steering/instruction prompt and configured island links.
- Selection predicate: worktree HEAD descends from requested hash; later matching action for an agent supplies its steering.
- Invalidation or expiry: discarded segments are archived from active leaderboard/status/log views; missing local session causes fresh start; matching queued actions are marked applied.
- Activation or effect: source resets worktree and changes launch prompt; no evidence that an old session correctly reconciles its narrative with rewound files.
- Evidence limits: this is not an atomic rollback of code, shared knowledge, external services and model context; no supplied resume trace.

Admission trigger: resume with hash or pending steering. Change: active code lineage and instructions. Rejection ability: non-descendant match skips an action; missing session rejects reuse, not the whole run. Recovery keeps discarded objects/JSON but requires a deliberate later selection; resetting candidate code alone does not establish restoration of the checkpointed knowledge state. Oracle: explicit target hash, not a computed correct answer. Human judgment selects a target when a human issues steering; generic queued caller identity does not establish human authorship. Mode: manual/caller-controlled intervention in the experiment loop.

> # Reset matched worktrees before any agent starts, archiving the
> # attempts on the discarded segments first (soft delete: the run has
> # explicitly rewound past them, so leaderboard/status/log must stop
> # showing them). The JSONs and git objects stay on disk.
> --- `coral/agent/manager.py`

#### RT-RTE-island-migration
Label: Score-directed agent relocation between islands

Configured cadence → migration planner → score/eligibility/destination selection → manager preflight → interrupt → move identity/attempt artifacts → repoint shared links and settings → relaunch. Planner is symbolic code using finalized real scored attempts, minimum evaluations, rank window, direction, cooldown and destination policy. Manager can defer paused candidates or drop stale ones and coordinate batches; a later resync can refresh sandbox state for bystanders. The migrant keeps code worktree and recovered session while switching shared-state neighborhood. Evidence: SRC-1, `coral/agent/migration.py`, `coral/agent/manager.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: planned candidates become relaunched agent handles; disabled/single-island/ineligible cycles yield no move.
- Later read-back: moved role, cadence, attempts and eval logs follow the agent; source-island notes/skills remain there; future reads resolve destination links.
- Delegated visibility: destination receives migrant identity and optional arrival note, not a bulk copy of source knowledge; the saved conversation may retain source information.
- Selection predicate: eligible real-score history, configured source ranking/destination weighting, cooldown and roster balance, followed by live manager checks.
- Invalidation or expiry: cooldown persists in migration state; stale candidates are filtered; paused batches may be deferred and retried.
- Activation or effect: moves files, repoints symlinks, refreshes settings/specs and restarts process; effective behavioral transfer and benefit remain unobserved.
- Evidence limits: logical island routing is not erasure of saved context or a proved security partition; external sandbox enforcement and transactional recovery across partial moves are not demonstrated.

Decision roles: configured policy/code proposes and selects migrations; manager preflight can veto/defer; no per-move human approval is on this path. Oracle: grader-derived rank signal, not expected correct agent placement. Mode: automatic score-directed coordination inside configured experiments. Admission changes organization: live agent neighborhood, settings and retained identity/cadence location. Guidance is a generated arrival prompt; recovery uses idempotent steps, deferred retry and future relaunch, not an evidenced all-or-nothing rollback.

> # (3) Move per-agent identity / cadence files src → dst.
> _move_agent_files(coral_dir, agent_id, src=src, dst=dst)
> --- `coral/agent/manager.py`

#### RT-RTE-machinery-admission
Label: Task, extension and runtime configuration admission

Caller/author → task YAML, packaged grader, installed custom classes or mounted runtime files → validators/import resolution → future launch/evaluation. Plugin session hook delivers task-authoring/running skill pointers; authoring skill prescribes seed/grader/config iteration and smoke test before scaling. This is natural-language workflow guidance, not a gate proving the author followed it. Runtime registry imports `module.path:ClassName` and checks a runtime protocol; grader worker imports a `TaskGrader` subclass. Custom sandbox providers are also configured entrypoints. These are executable extension surfaces with host authority, not safe plugin sandboxes. Evidence: SRC-1, `plugin/hooks/session-start.py`, `plugin/skills/creating-a-coral-task/SKILL.md`, `coral/agent/registry.py`, `coral/grader/subprocess_grader.py`, `coral/config.py`, `coral/agent/manager.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: configuration/validation diagnostics or imported adapter/worker result; plugin hook emits additionalContext without blocking the host session.
- Later read-back: saved configuration, installed code and mounted settings shape subsequent launches/evaluations; exact installed dependency/provider state is not frozen by this report.
- Delegated visibility: plugin-host model receives skill pointers; launched adapters receive resolved config, mounted files and privileges.
- Selection predicate: caller-selected entrypoint/runtime/options; structural/protocol/subclass checks determine acceptance, not semantic safety or superiority.
- Invalidation or expiry: changed configuration or files can replace future behavior; runtime classes are cached in registry; no universal hot-reload or rollback is established.
- Activation or effect: imports can execute installed code; mounts overwrite defaults; task authoring itself is requested agent behavior rather than observed construction.
- Evidence limits: author identity, dependency trust and per-content human review are unresolved; no target dependency installation or authoring loop was executed.

Admission trigger/change: task creation/edit, runtime entrypoint/config or mounted file selection. Software can reject malformed settings, unresolved classes and interface mismatches; initial human request is not approval of each generated grader or script. Rollback is configuration/package/file replacement; no uniform transactional mechanism is shown. Guidance: task-authoring skill calls for `coral validate` and a one-agent smoke test, hidden data outside surfaced grader source, and correctness before speed. Persistence: task artifacts and installed machinery, not model weight changes. Oracle: baseline grading can check runnable scoring; it cannot prove the chosen metric captures the user's objective. Mode: authoring/maintenance preceding or between optimization runs.

> module = importlib.import_module(mod_path)
> --- `coral/agent/registry.py`

> A CORAL task is **three things that must line up**. Scaffold them with `coral init`, then iterate `edit → coral validate` until the grader scores the seed.
> --- `plugin/skills/creating-a-coral-task/SKILL.md`

#### RT-RTE-specialist-delegation
Label: Prompt-directed specialist work and context separation

Foreground agent → host subagent mechanism using seeded specialist definition → summary and direct shared-file edits. Librarian definition grants Bash/Read/Write/Edit/Glob/Grep and names organization/skill-creator skills; it requests an end-to-end audit and concise summary. The foreground model chooses when to spawn; external harness decides actual subagent execution/context handling. CORAL supplies the files and instructions, not an inspected inner delegation runtime. Evidence: SRC-1, `coral/template/agents/librarian.md`, `coral/template/coral.md.template`, `coral/workspace/worktree.py`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: requested summary of moved/merged files, new skills and index changes; actual return transport is host-owned.
- Later read-back: delegated edits can enter shared notes/skills and later agent reads; their revision mechanics and correctness belong to memory analysis.
- Delegated visibility: seeded definition requests broad file/shell access; actual input context, inherited grants and isolation are uninspected host behavior.
- Selection predicate: foreground judgment when research or organization is needed; librarian asks to organize only when discovery is hard.
- Invalidation or expiry: inapplicable — no CORAL-controlled subagent-frame lifetime or compaction policy was found in these prompt and provisioning paths.
- Activation or effect: supplies delegation instructions and mutable output destinations; no inspected trace establishes spawn, context separation or compliance.
- Evidence limits: distinct subagent definition is not evidence of an isolated model invocation; no claim about host trimming, summaries or reload semantics beyond the requested summary.

Admission/decision roles: model chooses delegation and file changes; no mandatory human review of resulting scripts/skills is specified here. Librarian guidance preserves contradictions and archives originals; those instructions are not enforced semantic checks. Oracle: no independent expected answer for a correct reorganization. Mode: maintenance within task research. Working-context interpretation: if the host implements a separate frame, selected inputs enter and a summary escapes, while shared-file side effects also escape; this breaks a pure call-stack analogy. Whether the host really excludes the specialist's detailed turns from the parent window remains uninspected.

> When spawned, execute this process end-to-end and return a summary of what you changed.
> --- `coral/template/agents/librarian.md`

### Claims

#### RT-CLM-agent-organizations
Label: Autonomous experiment organizations claim

Source-native claimed operation is multi-agent experimentation, sharing and continuous solution improvement. This report establishes orchestration/evaluation/feedback wiring, not achieved quality, learning or causal benefit. It does not equate external candidate improvement with CORAL changing its own behavior-determining organization. Evidence: SRC-1, `README.md` and routes above.

> **CORAL** is infrastructure for **autonomous AI agent organizations** that run experiments, share knowledge, and continuously improve solutions. Give it a codebase and a grader, and CORAL handles the rest: isolated workspaces, safe evaluation, persistent shared state, and multi-agent collaboration. Natively integrated with Claude Code, OpenCode, Codex, Cursor Agent, and Kiro.
> --- `README.md`

#### RT-CLM-isolation-scope
Label: Isolation is conditional on path and deployment

The config documentation claims uniform process-tree sandboxing when enabled. Code supports an optional wrapper and settings, not universal deployed isolation. The current grant set depends on runtime options/mounts and generated settings; the capability surface includes shell, plugins, subprocesses and configured network access. The deployed envelope is unobserved. Evidence: SRC-1, `coral/config.py`, `coral/agent/runtime.py`, `coral/agent/builtin/codex.py`, `coral/agent/builtin/claude_code.py`, `coral/workspace/worktree.py`, `coral/sandbox/srt.py`, `coral/cli/start.py`.

> if sandbox is None or not sandbox.command_prefix:
>     return cmd
> return [*sandbox.command_prefix, *cmd]
> --- `coral/agent/runtime.py`

Codex bypasses native approval/sandbox on fresh and resumed commands. Claude's native denies cannot be generalized to shell descendants or arbitrary extensions; general Bash is allowed. SRT settings deny private reads/writes and specify additional read/write sets, then deep-merge caller overrides. Default open networking does not force provider calls through the gateway. Docker's task `:ro` mount is a different enforcement point; local advisory read-only grader guidance is not equivalent.

> 'approval_policy = "never"',
> 'sandbox_mode = "danger-full-access"',
> --- `coral/workspace/worktree.py`

> return _deep_merge(settings, cfg.extra_settings)
> --- `coral/sandbox/srt.py`

> # editable install from this same source, so writes here would perturb
> # grading; in the Docker session the target is a read-only (:ro) bind mount,
> # which makes it physically unwritable. On the host there is no isolation,
> # so read-only is best-effort (see the CORAL.md reminder). The symlink
> --- `coral/workspace/worktree.py`

Guarantee owner: outer launcher/provider/OS, not model compliance. Guarantee strength: deployment guarantee, conditional on actually applying the spec and an enforcing backend. Covered path: inspected Claude/Codex prefix launch and their descendants under the external sandbox contract. Alternatives: no spec, empty custom prefix, custom runtime code that ignores it, externally initiated processes and Pi's launch defect. Runtime protocol checking does not establish semantic containment. No deployment security or complete model-call mediation is inferred.

- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-CLM-pi-launch
Label: Pi manager launch interface mismatch

The claim of Pi being a selectable built-in must be qualified at this commit. Registry maps `pi` directly to `PiAgentRuntime`; `get_runtime` returns a direct instance. Manager always calls `runtime.start(..., sandbox=sandbox_spec)`. Pi's explicit signature ends at `run_as_user` and accepts no variadic keywords. Static Python call semantics therefore predict a keyword-argument TypeError on that manager path before the Pi subprocess starts. No runtime execution was performed. This does not refute the external Pi harness's capabilities or the ordinary Claude route. Evidence: SRC-1, `coral/agent/registry.py`, `coral/agent/manager.py`, `coral/agent/builtin/pi_agent.py`.

> "pi": PiAgentRuntime,
> --- `coral/agent/registry.py`

> gateway_api_key=gateway_api_key,
> run_as_user=run_as_user,
> sandbox=sandbox_spec,
> --- `coral/agent/manager.py`

> gateway_api_key: str | None = None,
> run_as_user: dict[str, Any] | None = None,
> ) -> AgentHandle:
>     """Start a Pi agent in the given worktree."""
> --- `coral/agent/builtin/pi_agent.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-generated-instructions
Label: Generated task instructions and injected heartbeat text

Consumer: external coding model/harness. Channel: generated runtime-native instruction file plus initial/resume command prompt. Force: natural-language behavioral guidance with configured harness-level grants; not a CORAL interpreter-enforced proof of compliance. Horizon: current task, resumed sessions and subsequent launches that regenerate/read the files. Task configuration and shared artifacts can shape the supplied text; model judgment mediates candidate actions. The immediate instructions prohibit direct Git and require evaluation/knowledge updates, but code does not make every statement an invariant. Evidence: SRC-1, `coral/agent/manager.py`, `coral/template/coral.md.template`, `coral/hub/prompts/consolidate.md`; routes [RT-RTE-agent-launch](#rt-rte-agent-launch) and [RT-RTE-heartbeat-feedback](#rt-rte-heartbeat-feedback).

> Your job is a loop: **plan → edit → eval → repeat**. Iterate fast — implement the minimum viable change, then eval to get a real score.
> --- `coral/template/coral.md.template`

> Pause your current work and synthesize the shared knowledge base. Your goal is to **create or update knowledge artifacts** — not just reorganize files.
> --- `coral/hub/prompts/consolidate.md`

## Annotations

none
