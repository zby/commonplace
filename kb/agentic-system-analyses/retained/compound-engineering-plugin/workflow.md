---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Compound Engineering Plugin's autonomous LFG plan-to-PR workflow, including native worker handoffs, return rejection, review admission and CI-decided delivery."
run-id: AAS-2026-10-13-compound-engineering-plugin-6ac79f4e7555-01
reviewed-boundary: "50532b00de523980010d97fe950965b35382a3b7"
---

# Compound Engineering Plugin workflow report

## Workflow account

### Selected workflow and evidence boundary

This account selects an explicitly autonomous new code-change request through `lfg`, taking its plan route and native implementation engine. It is representative because the shipped caller connects planning, implementation, independent review, learning capture and shipping in one numbered procedure. It is not a workflow assembled from unrelated skills. The host foreground agent remains the coordinator; named skills and fresh implementation workers supply bounded results. Host model execution, permissions and scheduling remain outside the plugin, as described by [RT-RTE-host-loading](runtime.md#rt-rte-host-loading), [RT-RTE-native-work](runtime.md#rt-rte-native-work) and [RT-RTE-lfg-shipping](runtime.md#rt-rte-lfg-shipping).

All added inspection is SRC-1 at the boundary's frozen commit: `skills/lfg/SKILL.md`, `skills/lfg/references/intake.md`, `skills/lfg/references/plan-brief.md`, `skills/lfg/references/work-return.md`, `skills/lfg/references/review-followup.md`, `skills/lfg/references/shipping.md`, `skills/ce-work/references/return-to-caller.md`, `skills/ce-work/references/implementation-loop.md` and `skills/ce-work/references/execution-strategy.md`. These supply doctrine/design evidence for the prescribed workflow, not an observed execution. No target command, test, model or provider was run. Detailed planner, browser, reviewer, PR creator and babysitter internals were not independently audited here; the account establishes their caller-facing handoffs, not every child recovery branch.

### Request to implementation authority

1. **Choose a work source, not an arbitrary existing plan.** LFG classifies the request by intent. For the selected new-change route it invokes `ce-plan` with the feature request. When the conversation carries user decisions, it supplies a temporary brief: direction, decisions with user-directed/user-approved provenance, rejected alternatives and reasons, open areas and a conflict-reporting instruction. An agent recommendation is evidence, not a settled decision. A planning-stage routing carrier, when supplied, travels separately from product content. LFG never discovers a convenient plan by searching the plans directory (SRC-1, `skills/lfg/references/intake.md`, `skills/lfg/references/plan-brief.md`).

2. **Admit the plan by content and return status.** LFG inspects the path `ce-plan` reports writing this run. The artifact must contain implementation scope, direction and verification, with no launch-blocking question. A requirements-only artifact or old readiness label does not suffice. An explicit blocked planning result is terminal even if a readable plan exists. Only absence of both blocker and reported plan permits one second planning invocation, with the same arguments and unchanged brief. A ready plan already written by `ce-plan` in this session bypasses replanning; `ce-work` then checks its readiness and prerequisites (SRC-1, `skills/lfg/SKILL.md`, `skills/lfg/references/plan-brief.md`).

> An explicit `status: blocked` return is terminal even when `artifact_path` names a readable plan.
> --- `skills/lfg/references/plan-brief.md`

3. **Pass implementation, not shipping, to `ce-work`.** LFG invokes `ce-work mode:return-to-caller <plan-path>`. The implementation skill owns unit decomposition, engine selection, test-evidence strategy, local verification and canonical unit commits; LFG retains the final simplify/review/PR/CI tail. Return-to-caller ends the child, not the turn. Its actual continuation depends on host/model compliance, not an executable LFG state machine ([RT-RTE-native-work](runtime.md#rt-rte-native-work); SRC-1, `skills/ce-work/references/return-to-caller.md`).

### Worker handoff and canonical verification

For structured independent units, `ce-work` schedules a fresh-worker wave from committed prerequisites after inspecting declared files, shared contracts and hidden write surfaces. Dependent units stay serial; lack of a subagent mechanism means inline work. Harness-isolated workers receive the intended base SHA and must reject a mismatching HEAD before editing. Shared-workspace workers require exclusive write ownership and no index writes; this is an instruction-level ownership contract, not plugin-enforced filesystem confinement (SRC-1, `skills/ce-work/references/execution-strategy.md`; [RT-RTE-native-work](runtime.md#rt-rte-native-work)).

Each worker receives the plan path plus bounded excerpts: goal capsule, definition of done, unit goal/files/approach, relevant verification entries, referenced intent/decision IDs and applicable settled Product Contract decisions found through their governing requirement links. It also receives inherited scope, the rule against unrequested mechanisms, and the evidence-reporting obligation. It does not merely receive “read the whole plan.” Its fresh context excludes previous implementation-unit transcripts; it returns changed paths and per-unit verification evidence. The unit-bound handle is retired after integration. Host internals determining the actual model window remain uninspected (SRC-1, `skills/ce-work/references/execution-strategy.md`).

The evidence handoff matters because the diff cannot prove that a worker observed a failing test before implementation. The orchestrator must preserve that reported observation, not invent it from resulting tests. A worker's self-check is not canonical acceptance: the foreground orchestrator inspects the actual tree, detects scope or semantic collisions, runs authoritative verification and makes canonical commits in dependency order. A clean apply is not compatibility evidence. Unattributed changes may belong to the user and must be preserved for reconciliation (SRC-1, `skills/ce-work/references/execution-strategy.md`, `skills/ce-work/references/implementation-loop.md`).

> **Inspect the actual tree, not reported paths.** Determine what each worker really changed (`git status`/diff in its workspace or the shared dir). Reported paths are a hint; declared `Files:` are often incomplete, because workers create or modify files the plan didn't anticipate.
> --- `skills/ce-work/references/execution-strategy.md`

Within a unit, evidence strategy precedes behavior edits. Applicable strategies include an existing failing test, strengthened test, new failing test, characterization or a deliberate exception with replacement verification. Failed tests prevent commits. After two ineffective fixes to one check, the implementer must examine their common assumption rather than keep patching. An in-scope correction can proceed; authority gaps or an invalidated settled decision block. These are prescribed recovery decisions, not demonstrated defect-detection reliability (SRC-1, `skills/ce-work/references/implementation-loop.md`).

### Return acceptance and a supported rejection/recovery path

Before returning, `ce-work` reopens the plan and compares active units, verification contract and definition of done with the diff. It returns status, plan/source identity, changed files, attempted/completed units, verification results and evidence, settled-decision conflicts, requested/actual route and model, run/receipt/recovery information and `standalone_shipping_skipped: true`. Native execution permits null external-run fields but does not omit them. LFG checks that changes extend beyond the plan and that source identity matches the plan authority handed in (SRC-1, `skills/ce-work/references/return-to-caller.md`, `skills/lfg/references/work-return.md`).

The caller has a specific recovery exception to its complete-and-evidenced gate. If behavior changed but verification evidence is missing or too vague, LFG invokes `ce-work` once more for evidence reconciliation, preserving plan and engine carrier. An external return needs a safe run ID and resumes that exact run; a native return with null run ID repeats the original invocation through native idempotency. A non-native return without a safe ID remains blocked. The recovery is instructed to inspect already implemented work and complete evidence, not dispatch implementation again. A second incoherent return blocks simplify, review and shipping (SRC-1, `skills/lfg/references/work-return.md`).

> If the second return still lacks coherent verification evidence, stop as blocked and report the missing fields instead of continuing to simplify/review/ship.
> --- `skills/lfg/references/work-return.md`

An additional caller-level rejection qualifies the runtime's external fallback account. `ce-work` may fall back natively even for an unavailable `require` engine, as [RT-RTE-external-unit](runtime.md#rt-rte-external-unit) describes. LFG nevertheless blocks shipping if the completed return reports `require` and an actual route different from the requested route. `prefer` fallback can proceed after prominent disclosure, without a second implementation. Child completion and caller admission are therefore different decisions (SRC-1, `skills/lfg/references/work-return.md`).

### Review, residuals and learning before shipping

LFG next invokes branch-diff simplification, except for docs-only or roughly sub-ten-line changes. It supplies the plan as preservation context, including settled structure, rather than as the diff scope. Simplification leaves edits uncommitted so the subsequent `ce-code-review mode:agent plan:<path>` reviews the working tree as well. Review is deliberately report-only: the reviewer returns findings and an artifact, and LFG applies eligible changes. A failed review stops; a settled-conflict finding showing infeasibility, wrong-thing or destructiveness blocks, whereas preference conflicts become residuals (SRC-1, `skills/lfg/SKILL.md`, `skills/lfg/references/review-followup.md`).

The separate admission mechanism is [WF-RTE-review-admission](#wf-rte-review-admission). High confidence alone cannot authorize a contract, permission, security or product behavior change. The foreground agent checks still-current code evidence, applies mechanical eligible fixes, runs required targeted tests and commits review-driven files. Eligible fixes left uncommitted prevent advancement. With a remote, this stage can push before learning capture and final PR creation, so a later stop is not a promise to undo already pushed state (SRC-1, `skills/lfg/SKILL.md`, `skills/lfg/references/review-followup.md`).

Unapplied actionable findings, review-stamped settled conflicts and implementation's proceeded-and-flagged conflicts must become durable. With a remote, LFG composes an unapplied-findings PR-body section, including review run/artifact context, and passes it to shipping. These findings remain undecided, not accepted debt. Without a PR, tracker filing is attempted and failed/no-sink items are carried verbatim in the DONE report. Filing failure does not itself block DONE. Only reasoning absent from code, tests and plan whose loss plausibly causes recurrence or substantial rediscovery triggers `ce-compound mode:non-interactive`; `Documentation skipped` succeeds. Capture runs before the final shipping head, not after CI-decided, so the intended PR includes the learning ([RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission); SRC-1, `skills/lfg/references/review-followup.md`).

### Delivery and its limits

LFG invokes `ce-test-browser mode:pipeline` and then the shipping handoff. This read establishes the invocation, not browser availability, coverage or successful execution. With a remote, `ce-commit-push-pr mode:pipeline branding:on` receives plan provenance, flagged decisions and residual section. A project-defined handoff replaces the default when active project instructions name one; inability to run headlessly or to produce pushed work in an open PR blocks rather than falls back. An existing PR requires a description-update invocation so residual context is not silently lost. With no remote, LFG invokes neither shipping skill nor project process: it commits only run-owned files locally, leaves pre-existing dirt alone and skips push/PR/CI watching (SRC-1, `skills/lfg/SKILL.md`, `skills/lfg/references/shipping.md`).

For an open PR, `ce-babysit-pr mode:pipeline` owns the bounded CI/review-feedback loop. LFG consumes `{ status, fixes_applied, residuals }`; it does not substitute a momentary green CI poll. The caller contract describes convergent CI fixes through `ce-debug`, no weakened assertions, and a default three-fix-round budget. Stack shipping may already have handed off a bottom-PR watch; a merely started watch is insufficient, and LFG must wait for its result rather than launch a competing current-PR watch. These are caller-facing requirements; babysitter internals and actual external CI remain uninspected here (SRC-1, `skills/lfg/references/shipping.md`).

> If step 9 only confirmed babysit **started** (or no structured result is available), re-invoke `ce-babysit-pr mode:pipeline <bottom-pr-url> posture:<same>` and wait for its pipeline completion — never treat "started" as DONE.
> --- `skills/lfg/references/shipping.md`

Delivery normally means pushed changes, an open PR URL, CI-decided result and close-out before `<promise>DONE</promise>`, not merge. No-remote delivery is explicitly local-only. Needs-human residuals must be rendered completely under `## Needs your decision`; a non-empty set is a decision handoff, not successful completion, even if the procedural DONE marker is emitted. An uncarriable single-PR merge grant is disclosed rather than acted on; stack grants have their own carrier. These distinctions prevent treating the marker, worker exit, green check or PR existence as interchangeable acceptance signals (SRC-1, `skills/lfg/references/shipping.md`; [RT-RTE-lfg-shipping](runtime.md#rt-rte-lfg-shipping)).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-review-admission
Label: Review fix admission

Part of: [RT-RTE-lfg-shipping](runtime.md#rt-rte-lfg-shipping)

This is the caller's steps 4–6 review-result-to-edit/commit/residual subroute, not another declaration of the whole autonomous shipping pipeline. It also follows implementation acceptance in [RT-RTE-native-work](runtime.md#rt-rte-native-work), but is contained in the LFG caller rather than ce-work. SRC-1, `skills/lfg/references/review-followup.md`, `skills/lfg/SKILL.md`.

Endpoints and progression: simplified branch/working-tree diff plus plan → report-only `ce-code-review` → foreground LFG filtering → eligible edits, verification and commit → residual PR-description context or local tracker/report handoff. The reviewer proposes; LFG decides mechanical eligibility and applies; the user later judges residuals through the PR. Operating mode is autonomous open requested work, not an improvement experiment. Confidence and persona agreement are selection criteria, not an expected-answer oracle. Current code and targeted tests provide task-specific checks; their adequacy is not established by the caller policy. Guidance is the plan's settled decisions, reviewer evidence and the mechanical-only rule. Persisted output is product commits and durable unresolved findings, not a revised plugin method. Failed review or invalidated settled decisions can stop; no automatic rollback of every previously committed or pushed change is established. The stop preserves already-pushed state rather than authorizing its removal.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: accepted fixes with commit/test reporting and residual context, or a failed/blocked stage result.
- Later read-back: unapplied findings reach the human PR reviewer; local tracker/report records provide the no-PR alternative. Actual later consumption is unobserved.
- Delegated visibility: reviewer gets branch/working-tree scope and plan context; shipping receives the composed residual section and review run/artifact identity.
- Selection predicate: concrete suggested fix, confidence 100 or 75 with cross-persona agreement, mechanical change only, and evidence still matching current code.
- Invalidation or expiry: stale evidence invalidates edit eligibility; manual/advisory/design or behavior/authority-changing findings remain unapplied; infeasible settled-decision conflicts block the pipeline.
- Activation or effect: requests foreground edits, required targeted tests, review-file commits and durable residual recording; actual successful application is unobserved.
- Evidence limits: natural-language admission policy requires model compliance; review internals, live findings and actual tests/commits were not executed or observed.

> 3. **The fix is mechanical** — one coherent change; no change to a contract, permission, or security stance; no new public API shape; no behavior change that needs product sign-off.
> --- `skills/lfg/references/review-followup.md`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-native-work](runtime.md#rt-rte-native-work)

Workflow handoff: the native worker's returned red/characterization observations are necessary evidence inputs to the structured caller return; actual-tree inspection validates scope but cannot reconstruct their timing. Fresh-unit contexts release only reported evidence and change artifacts back to the orchestrator; authoritative verification and canonical commits stay foreground-owned. Same-plan evidence reconciliation is explicitly distinct from reimplementation. See the worker and return account above (SRC-1, `skills/ce-work/references/execution-strategy.md`, `skills/ce-work/references/return-to-caller.md`).

#### On [RT-RTE-lfg-shipping](runtime.md#rt-rte-lfg-shipping)

Workflow acceptance: `skills/lfg/references/work-return.md` adds a caller-level `require` route-mismatch veto even when ce-work completed natively. Its one evidence-reconciliation retry preserves source and route/run identity, and cannot license a second shipping run. `skills/lfg/references/shipping.md` separates CI-decided from merged, watch-started from watch-finished, local-only from failed shipping, and needs-human decision handoff from successful completion. Added inspected caller contracts are doctrine/design, not operational evidence (SRC-1 at these paths). Review admission is separately recorded as [WF-RTE-review-admission](#wf-rte-review-admission).
