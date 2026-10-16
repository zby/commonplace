---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Claude Workstream Kit runtime baseline: installed instructions, state reload, model-mediated work, guarded rewrites and change admission."
run-id: AAS-2026-10-15-claude-workstream-kit-103204afa1ab-01
reviewed-boundary: "15705c38a4fffb206b868b3e6bc5ffb4fd8b9d64"
---

# Claude Workstream Kit runtime report

## Runtime account

### Boundary and claimed work

The kit coordinates repository work across Claude Code sessions; it does not run the model loop itself. Its executable parts install instructions, inject state summaries, measure records, rewrite selected text and check final-message references. Its natural-language parts ask a foreground model to inspect real artifacts, plan bounded work, delegate, verify, obtain user decisions and commit checkpoints. Native model turns, tool execution, subagent isolation, permission prompts, compaction and `/goal` evaluation belong to the external host. SRC-1, `.claude/settings.json`, `.claude/skills/workstream-work/SKILL.md`, `tests/va3-acceptance.sh`.

This account uses only SRC-1 at the boundary's frozen commit. Added inspection covers full work/create/capture/review/extract/close/status/upgrade/handoff skills, all three agent definitions, both hooks, settings and the three-session evaluator; selected installer, rewrite, shared-parser and telemetry ranges were inspected. Implementation and doctrine/design are distinguished below. Comments recounting live failures are reported operation, not this analysis's execution evidence. No target, acceptance test or provider was executed. Activation, successful installation, reliable task completion and benefit remain unobserved.

### Ordinary invocation end to end

A maintainer installs the kit into a consumer repository ([RT-RTE-install-upgrade](#rt-rte-install-upgrade)). A user requests creation; the foreground model checks for duplication, interviews for purpose, type, deletion criteria and initial tasks, drafts the two state files, shows their wording, obtains approval, commits and stops. Starting work is a separate user decision ([RT-RTE-state-lifecycle](#rt-rte-state-lifecycle)). These are instructions, not a scripted transaction.

At the next host SessionStart, a registered shell command reads the pointer and derives roster, age, gate and drain signals ([RT-RTE-session-reload](#rt-rte-session-reload)). It prints ACTIVE.md, not the full active workstream. The work skill separately instructs the model to read the workstream, reconcile drift, verify the task's premises against the current artifacts and derive a goal. The user can arm that goal, work interactively, or refine it ([RT-RTE-work-goal](#rt-rte-work-goal)). Thus state injection, full-state reading and goal activation are separate operations.

For a bounded task, the foreground model owns scope, next-step selection and acceptance. It may obtain read-only scouting, send an explicit packet to a worker and pass that same specification to a fresh verifier. A worker has file and shell tools; the verifier's output returns to the foreground model, which must check it rather than treating it as authoritative ([RT-RTE-agent-packet](#rt-rte-agent-packet)). Work artifacts and evidence-bearing completion notes land in the consumer repository. At a user checkpoint the model is instructed to stop with evidence rather than mark its own approval. At session exit it captures unrecorded decisions, findings and synthesis, routes them, advances the pointer and commits state. The terminal product is committed work plus a resume target, a recorded blocker or a user gate; not necessarily a completed workstream.

Closure is a distinct terminal path: extract unresolved retained content to governed destinations, show per-criterion evidence, obtain closure approval, commit `status: done`, create an annotated tag, delete the directory, conditionally reset ACTIVE.md, and commit again. Publishing the tag has its own gate. A long-running workstream instead drains/rotates without closing. These lifecycle instructions are in [RT-RTE-state-lifecycle](#rt-rte-state-lifecycle); revision semantics belong to the memory analyst. Mechanical condensation has a separate executor and weaker, precisely bounded preservation checks ([RT-RTE-rewrite-state](#rt-rte-rewrite-state)).

### Forcing routes and guarantees

Three source-supported countercases prevent treating the instructions as universal enforcement:

1. **Unattended model driver.** The shipped evaluator calls `claude -p --dangerously-skip-permissions` and supplies approval in its prompt. Session B only stands in for a goal session; it does not arm the interactive native goal. This is a material model-calling route within the boundary, with a different grant configuration ([RT-RTE-acceptance-driver](#rt-rte-acceptance-driver)).
2. **Alternate writes.** Standard condensation uses a heading/checkbox fingerprint, but rotation intentionally removes completed structure and uses different checks. Manual shell/editor writes do not pass through either guard. The extract skill's general preservation sentence therefore is not an invariant across all shipped operations ([RT-CLM-rewrite-preservation](#rt-clm-rewrite-preservation)).
3. **Fail-open Stop guard.** A bare-reference final message can trigger one repair turn, but `stop_hook_active`, import errors, absent transcripts or parsing failure allow stop. Earlier messages and file edits are outside that check ([RT-RTE-stop-gloss](#rt-rte-stop-gloss)). It is not an authorization or task-completion guard.

The gate owner is the user; enforcement in the kit is a model-facing policy, with the external host supplying any actual tool permission controls. For read/edit/commit actions the work skill grants routine autonomy, while shared-visible actions and irreversible changes require a user stop unless standing authorization names the action. That statement covers skill-following work, not all Bash commands the host can execute. Agent tool lists are a capability surface, not an OS isolation envelope. No deployed consumer grant set, sandbox configuration, callback restriction or provider-native tool policy is supplied. The evaluator's bypass flag is inspectable, but its actual account-side permissions are not. SRC-1, `.claude/skills/workstream-work/SKILL.md`, `.claude/agents/worker.md`, `.claude/agents/scout.md`, `.claude/agents/verifier.md`, `tests/va3-acceptance.sh`.

The inspected materially alternate paths are foreground model tool use, delegated Bash/editing, manual direct script invocation, installer writes, hook callbacks, history/tag retrieval, cross-project filing, and the model-calling evaluator. The kit does not make its Python rewrite entry point the exclusive file-write interface. Provider internals, actual host control enforcement and live recovery from interrupted operations remain uninspected. No system-wide negative about other host capabilities follows.

### Context and observability

The model's working context is controlled by several different owners. SessionStart code selects a pointer plus summaries automatically; the foreground model requests the detailed files. Skills reserve within-session tracking for native Tasks/plan mode and cross-session tracking for the backlog. Subagent packets keep full delegated work outside the foreground context and return findings/evidence, resembling a temporary frame whose return escapes; the host, not kit code, implements isolation. The returned text is by value, not a dereferenceable shared context. Work/capture instructions checkpoint before clear/compact/exit, while SessionStart registration is intended to re-ground after compaction. The capture skill says `/clear` fires no hook, whereas the reload hook's comment lists clear among SessionStart events; actual event sequencing is an unresolved external-host contract, not an established kit guarantee. SRC-1, `.claude/rules/workstreams-rule.md`, `.claude/skills/workstream-capture/SKILL.md`, `.claude/hooks/session-start.sh`.

The status-line reader selects the newest project-matching temporary telemetry record, or prints nothing; capture reports its two numbers last and leaves clear/compact decisions to the user. This is a budgeting signal, not implemented kit-side truncation or automatic compaction. Status additionally selects every workstream, archive ledger, inbox and the project-declared context list, asking for raw record coverage, count rederivation and a scout citation check before producing chat only. Its read-only rule is a skill policy; scouts still have Bash, and the utility's read-only design does not constrain every possible model action. SRC-1, `.claude/scripts/status-line.sh`, `.claude/skills/workstream-status/SKILL.md`, `.claude/skills/workstream-capture/SKILL.md`.

## Shared records

### Components

#### RT-CMP-claude
Label: External Claude Code model calls

Identity: the foreground and delegated models invoked through Claude Code, including the evaluator's bare `claude -p` commands. Representational form: distributed-parametric for model internals; skills and packets are separate natural-language inputs. Storage substrate: external provider/host, inaccessible here. Operational parameter updates are uninspected; no training operation is established by these inspected routes. Exact model version is not pinned by the evaluator or agent definitions. A mutable host configuration may resolve the command/agent to another model; endpoint-resolution behavior is external and uninspected. The status line reads a model display name, not a parameter-version guarantee. SRC-1, `tests/va3-acceptance.sh`, `.claude/agents/worker.md`, `.claude/agents/scout.md`, `.claude/agents/verifier.md`, `.claude/scripts/status-line.sh`.

> tools: Read, Edit, Write, Grep, Glob, Bash
> --- `.claude/agents/worker.md`

### Operative objects

#### RT-OBJ-active
Label: ACTIVE.md resume pointer

Source-native identity: `.state/ACTIVE.md` in a consumer project. Storage substrate: local Markdown file, intended to be committed to Git. Its `workstream` and `task` fields are symbolic selectors; Now/Next/Blockers are natural-language instructions/context. These parts have different consumers: shell parsing locates the active file, while the model interprets the prose. It is not proof that a native goal is armed. SRC-1, `.claude/rules/workstreams-rule.md`, `.claude/hooks/session-start.sh`.

> It carries the SCOPE of any goal a session derived — the task or phase and the turn bound — and never whether one is armed or cleared: the file cannot know that, and a status it asserts is a claim the next session cannot verify.
> --- `.claude/rules/workstreams-rule.md`

#### RT-OBJ-workstream
Label: Workstream record

Source-native identity: `.state/workstreams/<type>/<name>/workstream.md`. Substrate: local Markdown and intended Git history/tag snapshots. Natural-language Purpose, task descriptions, Decisions, Learnings, Open Questions and criteria guide model judgment. Symbolic headings, IDs, checkboxes and dated markers support deterministic counters, references and rewriting. A marker establishes a parser match, not the truth of its claim. State shapes and operative parts are identified here; the memory analyst owns retention/revision findings. SRC-1, `.claude/rules/workstreams-rule.md`, `.claude/skills/workstream-review/SKILL.md`.

> A Learning's disposition is a fact about ANOTHER file: a missing marker is presumptive evidence of an unexecuted routing, a present marker is evidence of nothing, so verify every entry against the artifact it names, in both directions, and read the entries rather than counting them.
> --- `.claude/skills/workstream-review/SKILL.md`

### Routes

#### RT-RTE-session-reload
Label: SessionStart reload and signals

Endpoints/progression: host SessionStart → registered `sh` hook → ACTIVE.md, active file, full roster and inbox scans → stdout to host. Owner: hook code determines selection/counts; foreground model decides reconciliation. State effects: no workstream mutation in the inspected hook; optional Python measures add drain and gloss signals. No semantic oracle: age/count/marker predicates are signals, not decisions that the work is correct. SRC-1, `.claude/settings.json`, `.claude/hooks/session-start.sh`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ACTIVE.md text, active metadata, roster and conditionally emitted warnings, drain/gloss and inbox signals.
- Later read-back: each host event rereads current retained state; full workstream reading is separately requested by the work skill.
- Delegated visibility: uninspected — host propagation of hook output to delegated agents is not specified here.
- Selection predicate: existing state directory; workstream pointer for active detail, all matching workstream files for roster, markdown inbox files for pending count.
- Invalidation or expiry: recomputed per event; substantive age uses Git checkbox/Decision changes, with file-time fallback; inbox age uses mtime.
- Activation or effect: delivery wiring exists; reconciliation behavior by a model is unobserved.
- Evidence limits: host event semantics and actual context receipt are external; missing Python suppresses supplemental measures rather than proving quiet state.

> # ACTIVE.md: print whole file (kept short by convention).
> --- `.claude/hooks/session-start.sh`

#### RT-RTE-work-goal
Label: Work selection and native goal delivery

Owner/progression: user requests work → foreground model reads state and real artifacts, chooses critical-path scope and drafts an outcome condition → user chooses clipboard delivery, interactive work or refinement → host owns any armed goal evaluation. Model proposes/executes; user can veto scope and gates. Operating modes: open-ended project work bounded by task/phase, optional native goal, or interactive operation. Oracle: user criteria and task-specific test commands may supply expected outcomes; model judgment itself is not an oracle. Product changes are admitted by foreground task acceptance with evidence, plus user decisions for gates/shared-visible actions. Commit-sized changes and checkpointed blockers provide requested recovery; failing tests can yield a recorded blocked result, not forced completion. SRC-1, `.claude/skills/workstream-work/SKILL.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: resume announcement, outcome summary and user choice; eventually committed work, held gate or blocker report.
- Later read-back: updated backlog and ACTIVE.md guide a later work invocation; armed-goal state is not recoverable from them.
- Delegated visibility: explicit bounded packets supply selected task material, not presumed access to the entire foreground conversation.
- Selection predicate: verified current task premises, derivable critical path, either/or-completable scope and resumability/context budget.
- Invalidation or expiry: task/world mismatch triggers rederivation or review; native met goals clear and new goals replace old ones by the stated host contract.
- Activation or effect: instructions request model execution and stop behavior; no supplied run establishes compliance.
- Evidence limits: goal arming/evaluation and account permissions are external; clipboard delivery does not itself arm a goal.

> Do not set the goal yourself; `/goal` is the user's to issue.
> --- `.claude/skills/workstream-work/SKILL.md`

> Shared-visible or irreversible actions (pushing to shared remotes, opening PRs/issues, deleting non-session files, scope changes): STOP and surface, unless standing authorization names the specific action.
> --- `.claude/skills/workstream-work/SKILL.md`

#### RT-RTE-agent-packet
Label: Scout worker verifier packets

Endpoints: foreground orchestrator → selected host subagent → findings/work report → fresh verifier where required → foreground acceptance. Decision policy is natural-language packet/agent instructions; tool lists are symbolic host declarations. Worker mutates only the requested file scope by policy; it may retry an in-scope failed verification twice. Scout and verifier are instructed read-only, despite Bash availability. Foreground model retains scope, sequencing and admission; verifier proposes PASS/FAIL, not an independently enforced veto. Human decisions retain the work skill's gates. Operating mode is bounded task delegation, not autonomous open-ended worker design. Answer oracle is the packet's specification and verification command, whose coverage must itself be checked; no universal expected-answer provider is supplied. SRC-1, `.claude/agents/worker.md`, `.claude/agents/scout.md`, `.claude/agents/verifier.md`, `.claude/skills/workstream-work/SKILL.md`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: compact evidence-bearing worker/scout report or verifier verdict to orchestrator.
- Later read-back: accepted artifacts and completion notes may be committed and later read; subagent chat is not specified as the durable checkpoint.
- Delegated visibility: originating specification verbatim, objective, file scope, verification command and stop conditions; actual host context isolation is uninspected.
- Selection predicate: judgment-heavy reads to scout, mechanical bounded work to worker, fresh-context verification before acceptance/next packet.
- Invalidation or expiry: missing packet fields stop work; out-of-scope needs return to orchestrator; failed checks limit retries.
- Activation or effect: affords file/shell execution with requested constraints, not demonstrated isolation or reliable execution.
- Evidence limits: tool availability does not prove permission grant; no live delegation trace or OS sandbox is supplied.

> If the packet is missing any of those four, stop immediately and reply asking for the missing part — do not improvise scope.
> --- `.claude/agents/worker.md`

> Findings from sub-agents — and the LIMITATIONS a sub-agent states about them — are inputs to verify, not conclusions to repeat: an overstated limitation costs the same re-derivation as an understated one and draws less scrutiny, because it reads as honest hedging.
> --- `.claude/skills/workstream-work/SKILL.md`

#### RT-RTE-state-lifecycle
Label: Model-mediated state lifecycle and admission

Endpoints: creation interview → reviewed state; session work → capture/checkpoint; drift → review; accretion → extract; closure approval → Git tag/ledger and directory removal. The foreground model proposes and physically edits; the user approves creation wording, substantive restructuring and closure, but routine capture and mechanical repairs proceed without per-content approval. Cross-project handoff has destination/visibility confirmation and a separate publication decision; receiving triages to action, backlog or decline and deletes processed files after durable filing. These are distinct gate locations inside a model-interpreted protocol, not a universal software write filter. SRC-1, `.claude/skills/workstream-create/SKILL.md`, `.claude/skills/workstream-capture/SKILL.md`, `.claude/skills/workstream-review/SKILL.md`, `.claude/skills/workstream-extract/SKILL.md`, `.claude/skills/workstream-close/SKILL.md`, `.claude/skills/handoff/SKILL.md`.

Admission guidance asks for current artifact evidence, explicit rationale and routing to governed destinations; it persists in shipped skills and resulting state/artifacts. Operating modes are interactive lifecycle maintenance and bounded unattended evaluation when approval is supplied in advance. Oracles are local verifiable criteria, named files, commits and test results, not the disposition marker itself. A user can refuse substantive changes/closure; the model must stop on unsatisfied criteria. Recovery is intended through scoped commits, in-place supersession and pre-deletion tags, not a transactional controller. Paused/maintain workstreams can remain live indefinitely, with standing rechecks rather than forced closure.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: displayed creation draft, checkpoint report, restructure case, extraction account or closure evidence/summary.
- Later read-back: committed ACTIVE.md/workstream files, named permanent artifacts, receiving backlog and archive-tag snapshots reach later invocations.
- Delegated visibility: handoffs must include self-contained context because the receiver cannot see the sender's conversation/repository; extraction does not bypass handoff's gate.
- Selection predicate: explicit request or drift/drain/boundary signals; close checks whether criteria describe an actual exit rather than standing health.
- Invalidation or expiry: superseded decisions marked in place; processed inbox files deleted; closure removes workstream directory after tag; ACTIVE.md reset only if it points there.
- Activation or effect: requested durable instruction/knowledge/product changes; their later behavioral use is unobserved.
- Evidence limits: no execution demonstrates comprehensive capture, truthful dispositions, user-gate compliance or successful remote publication.

> Then the user approves or directs edits; iterate until approved.
> --- `.claude/skills/workstream-create/SKILL.md`

> Mechanical fixes (a rotted pointer, a stale status) proceed; substantive restructures are presented for approval with the drift evidence behind them.
> --- `.claude/skills/workstream-review/SKILL.md`

> When all criteria have evidence, ask the user to approve closure. Never self-certify.
> --- `.claude/skills/workstream-close/SKILL.md`

#### RT-RTE-rewrite-state
Label: Direct Python state rewrite

Endpoints: caller selects subcommand/options/file → deterministic parser/transformer → dry-run report or direct file replacement. Owner: code rejects structural mismatch; caller decides semantic applicability, shipped Decisions and retained phrases. Operating mode: bounded transformation, not model-based improvement search. Oracle: old/new structural predicates and explicit IDs/tags, not correctness of the retained prose. Trigger/proposal/admission: extract recommends condensation/rotation, caller requests it and `--write` authorizes physical I/O; a human per-content decision is not enforced by the CLI. Rollback depends on prior committed text/tag; the inspected write tail opens the file directly, not an atomic Git transaction. SRC-1, `.claude/scripts/workstream-rewrite.py`, `.claude/scripts/workstream_state.py`, `.claude/skills/workstream-extract/SKILL.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: proposed-change summary, per-entry report, refusal, NO CHANGE or WRITTEN.
- Later read-back: a written workstream replaces the input for later hook/model reads; historical text is reachable only if retained in Git/tag as instructed.
- Delegated visibility: inapplicable — this script invokes no subagent in the inspected dispatch and write paths.
- Selection predicate: records/decisions/learnings command rules, explicit Decision selections, or rotate's live-content selection and keep options.
- Invalidation or expiry: old live text overwritten only with --write; failed check refuses; rotation can explicitly allow stale numerical claims.
- Activation or effect: executable retained-text transformation; no evidence that transformed text was consumed or improved behavior.
- Evidence limits: structural checks cannot certify preserved meaning; manual editing bypasses them, and rotation uses a different predicate.

> if fingerprint(new_lines) != fingerprint(old_lines):
> --- `.claude/scripts/workstream-rewrite.py`

> # The fingerprint is not identical by design here (headings and done
> # boxes leave), so the shared tail is not used.
> --- `.claude/scripts/workstream-rewrite.py`

#### RT-RTE-install-upgrade
Label: Install or upgrade executable and instruction payload

Endpoints: maintainer-supplied checkout/target → installer preflight/classification → payload copy, settings merge, state seed, stamps → review/commit by caller. Symbolic shell/jq code controls copying; upgrade's preview/stash/review sequence is natural-language model guidance. Trigger is initial installation or a newer/different checkout. Proposed changes include skills, agents, hooks, scripts and host registrations: this is a capability/instruction admission path, not merely data import. Caller can reject preview or local-edit discard; code refuses classified local modifications only under its documented conditions. `--force` bypasses that refusal. Git copies of payload are another update path outside installer control. Recovery depends on target Git/stash; no rollback transaction is established by the inspected code. SRC-1, `install.sh`, `.claude/skills/workstream-upgrade/SKILL.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: preview/refusal/action-required messages or installed/upgraded summary and provenance stamps.
- Later read-back: host reads installed hooks/skills on later events/invocations; installer seeds only missing state files and stages untracked nonignored seeds.
- Delegated visibility: inapplicable — installer copies agent definitions but does not run subagents.
- Selection predicate: payload enumeration, explicit target, existing settings/state and local drift classification; source checkout may change before a later upgrade.
- Invalidation or expiry: installed payload is replaced by later install or repository updates; source/version stamps record provenance, not permanent pinning.
- Activation or effect: copies and registrations are wired; actual host loading and new behavior remain unobserved.
- Evidence limits: no deployed target inspected; jq absence can leave manual settings work; force and non-Git kit conditions weaken overwrite refusal.

Decision roles: caller chooses source/target/force; code classifies drift; upgrade guidance asks the user about ambiguous targets, local changes and unreleased builds. Operating mode: bounded deployment with dry-run, not automated proposal comparison. Oracle: file equality/history classification for drift, not a functional test of the installed behavior. Required external contracts are shell utilities, Git and jq for complete automated settings integration.

> if [ "$FORCE" -eq 0 ] && [ "$KIT_IS_GIT" -eq 1 ]; then
> --- `install.sh`

> Route them to the kit first, or re-run with --force to discard them.
> --- `install.sh`

The latter sentence appears inside an installer diagnostic string; it is quoted here as text only, not as executable syntax.

#### RT-RTE-stop-gloss
Label: Final-message gloss repair hook

Endpoints: host Stop JSON → transcript trailing assistant text → shared bare-ID detector → optional JSON block decision. Owner: deterministic Python hook; external host applies the response; foreground model repairs text. Strength: best effort, not invariant. Covered path: final assistant text with a usable transcript. Alternate paths: previous messages, file/commit contents, repeated Stop, missing/import-failed hook and malformed transcript are not equivalent enforced outputs. It does not decide user approval or stop-on-task-completion. SRC-1, `.claude/hooks/bare-id-guard.py`, `.claude/settings.json`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: no output on clean/fail-open paths; otherwise JSON block with IDs and repair request.
- Later read-back: inapplicable — the hook does not write a retained behavior-shaping result.
- Delegated visibility: uninspected — whether subagent Stop callbacks use this registration is a host matter.
- Selection predicate: final assistant text only, blanking fenced content and detecting bare references with the shared parser.
- Invalidation or expiry: stop_hook_active allows the next stop through; import/payload/transcript failures also pass.
- Activation or effect: one corrective request is wired; actual repair and host blocking are unobserved.
- Evidence limits: no universal reference correctness, task completion or permission guarantee follows from a gloss check.

> if payload.get('stop_hook_active'):
>         return 0
> --- `.claude/hooks/bare-id-guard.py`

#### RT-RTE-acceptance-driver
Label: Three-session model-calling evaluator

Endpoints: test maintainer → temporary Git project/install → sequential create/work/close `claude -p` sessions → shell assertions and retained session output. Owner: script supplies scenario/conditional approvals; models perform lifecycle work and delegate; assertions select PASS/FAIL/HELD. Operating mode: bounded fixture, not ordinary open project work. Answer oracle: greeting output, smoke-test exit, state patterns, evidence-note pattern, tag/status/ledger/deletion checks and clean-tree predicate. The prompt supplies a user-like approval contribution in advance; model judgment still checks closure evidence, while the driver checks the resulting artifacts. Tests admit no automatic product patch back to the kit: comments ask a maintainer to read captured findings before deleting fixtures. SRC-1, `tests/va3-acceptance.sh`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: test verdict, per-check lines, closing observations and fixture/log paths.
- Later read-back: maintainer can inspect saved output, fixture Git history and Learnings; incorporation into kit guidance requires a separate decision/change.
- Delegated visibility: Session B explicitly requires worker packets and verifier checks; the driver does not itself inspect their complete execution trace for correctness.
- Selection predicate: fixed greeting-script scenario; closure_held classifies directory still present with non-None ACTIVE Blockers as held.
- Invalidation or expiry: independent temporary paths per run; driver leaves fixture/logs for inspection rather than deleting them.
- Activation or effect: three direct host model calls and permission-bypass arguments are wired; no supplied invocation result establishes exercise.
- Evidence limits: Session B stands in for /goal, not native arming; HELD is not an archive success; scenario assertions are not a general safety/effectiveness oracle.

> this non-interactive session stands in for the /goal session, so proceed under that condition.
> --- `tests/va3-acceptance.sh`

The quoted phrase is part of Session B's long prompt string, not a separately implemented goal evaluator.

### Claims

#### RT-CLM-rewrite-preservation
Label: Rewrite preservation contract and rotation exception

Claimed operation: extract says all shipped rewrites refuse heading/checkbox changes. Source: SRC-1, `.claude/skills/workstream-extract/SKILL.md`.

> Every rewrite the kit ships dry-runs by default, refuses to write when a heading or a checkbox would change, and leaves the full text in git at the commit before;
> --- `.claude/skills/workstream-extract/SKILL.md`

Assessment: [RT-RTE-rewrite-state](#rt-rte-rewrite-state) narrows this to the standard finish path. Rotation deliberately removes completed structure and instead checks retained open/gate/standing structure, references and stale claims. The library fingerprint itself tracks heading multiset and checkbox state/ID sequence; it cannot prove preservation of task meaning or prose. The owner is rewrite code, enforcement is before its own writes, strength is invariant only for that checked relation on that path, not universal preservation. Prior Git retention additionally requires the caller's commit discipline. Direct model edits/CLI shell writes bypass it.

- implementation conclusion status: wired
- operation conclusion status: uninspected

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-guidance
Label: Installed skill guidance to foreground and delegates

Consumer: foreground Claude Code model and explicitly packeted subagents. Channel: installed rule/skill text and verbatim specification packets. Force: natural-language policy plus requested checks; host tool declarations supply a separate symbolic capability channel. Horizon: later skill invocations and sessions until files are updated. Installation or delivery is not observed compliance. SRC-1, `.claude/skills/workstream-work/SKILL.md`, `.claude/skills/workstream-upgrade/SKILL.md`, `.claude/agents/worker.md`.

> The session-start hook and the skills are read at the next session start and the next invocation, so a session that upgraded itself keeps running on the old text until then; say so.
> --- `.claude/skills/workstream-upgrade/SKILL.md`

#### RT-BAP-resume-state
Label: Retained state to later work selection

Consumer: hook parsers and foreground work model, with different effects. Channel: ACTIVE.md and workstream files delivered/retrieved on later invocation. Force: symbolic pointer/count selection in hook code, natural-language planning guidance in model context. Horizon: cross-session within the consumer project; cross-machine reach additionally requires Git publication. Altered state can change what is selected or proposed without changing model parameters. Actual activation remains unobserved. SRC-1, `.claude/hooks/session-start.sh`, `.claude/skills/workstream-work/SKILL.md`.

> Read `.state/ACTIVE.md` and the active `workstream.md` first, then announce "Resuming <name> at <task>".
> --- `.claude/skills/workstream-work/SKILL.md`

## Annotations

none
