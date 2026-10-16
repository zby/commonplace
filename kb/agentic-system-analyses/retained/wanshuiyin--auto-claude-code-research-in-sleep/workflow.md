---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Auto-claude-code-research-in-sleep workflow: research direction to experimental results, bounded review and narrative delivery, including sanity failure and resume paths."
run-id: AAS-2026-10-15-auto-claude-code-research-in-sleep-a8abf5f80cbb-01
reviewed-boundary: 26b95cfa0d8747078e9e43b42e20952709e561b8
---

# Auto-claude-code-research-in-sleep workflow report

## Workflow account

### Selection and evidence

The representative workflow is `/research-pipeline`: a research direction becomes a selected idea, experiment implementation and results, iterative review, then a narrative handoff. It is selected because the shipped parent explicitly connects these stages through named artifacts, checkpoints and completion rules, rather than merely listing compatible skills. The default endpoint is a research report, not a submitted paper. The container route is [RT-RTE-research-pipeline](runtime.md#rt-rte-research-pipeline).

This is a source-grounded protocol account, not an execution trace. SRC-1 remains the sole source at the frozen revision in [boundary](boundary.md). This member inspected all of `skills/research-pipeline/SKILL.md` and `skills/experiment-bridge/SKILL.md`, and the initialization/backend-selection, assessment/memory/stop-gate, human-checkpoint, fix, result-waiting, documentation and termination passages of `skills/auto-review-loop/SKILL.md`. These passages supply doctrine/design. Executable helper behavior below relies on the supplied runtime records; no target commands, experiments or providers were run. Idea-generation internals, queue execution, native evidence validation, claim conversion and paper audits are not independently inspected here. Consequently their successful operation and semantic quality are not established.

### Request and first handoff

The foreground host agent interprets the user's direction and flags. A project-root `RESEARCH_BRIEF.md`, when present, supplies detailed context. The parent invokes `/idea-discovery` with the arguments and resolved `AUTO_PROCEED`; it expects ranked ideas in `idea-stage/IDEA_REPORT.md` and the downstream experiment plan in `refine-logs/EXPERIMENT_PLAN.md`. The parent describes the child as literature → idea creation → novelty check → research review, but that description does not independently establish those internal checks (SRC-1, `skills/research-pipeline/SKILL.md`).

Selection authority is conditional. With default `AUTO_PROCEED=true`, the host announces its selected idea and continues in the same turn; this is not human approval. With `false`, the human can approve, alter the constraints, reject all ideas and request another discovery pass, or stop with the idea report saved. The next expensive stage therefore has an optional, not universal, human veto. The checkpoint rule is explicit:

> Once a turn ends, silence cannot resume the pipeline. The user can still
> interrupt a non-blocking run at any time.
> --- `skills/research-pipeline/SKILL.md`

### Plan to executed-result handoff

The parent delegates the selected title and code-review/base-repository/compact settings to `/experiment-bridge`, then waits for its handoff summary. The bridge reads the plan, tracker and proposal; extracts ordered milestones, metrics, success criteria and compute budget; and writes or extends experiment scripts. If no expected inputs exist it asks what to implement. It also requests creation of a missing research contract from the selected idea and plan claims, providing a claims source for downstream consumers (SRC-1, `skills/experiment-bridge/SKILL.md`).

The optional code reviewer receives pasted plan sections, method description and implementation, not automatically the foreground context. Its task includes checking loss/data/metrics, seeds and use of dataset ground truth. This particular prompt is an executor-selected representation of artifacts; it does not establish the stronger unfiltered-input ideal of [RT-CLM-review-independence](runtime.md#rt-clm-review-independence). No CRITICAL issues allows progress; CRITICAL issues request fixes and resubmission with a two-round limit. The passage does not specify a distinct disposition for a still-critical second review. Furthermore code review can be disabled or silently skipped when Codex MCP is unavailable. It is therefore not an invariant admission gate for experiment effects (SRC-1, `skills/experiment-bridge/SKILL.md`; runtime's container record supplies the skip quotation).

Sanity executes the smallest experiment before the full suite. The foreground agent checks error-free execution, saved metrics, GPU memory and output format. Failure enters [WF-RTE-sanity-recovery](#wf-rte-sanity-recovery), not immediate full deployment. This detailed child contract specifies two patches plus two clean reimplementations, unlike the parent's three-attempt summary; the trace uses the child's operative procedure, as does the runtime baseline (SRC-1, `skills/experiment-bridge/SKILL.md`, `skills/research-pipeline/SKILL.md`).

After sanity, the child selects deployment per milestone. The explicit routing predicate sends at least ten jobs or teacher/student dependencies to `/experiment-queue`, otherwise `/run-experiment`; thus six to nine independent jobs fall into the latter despite the overview's small/large examples. Queue retry and persistence are advertised, not independently verified here. The agent monitors, parses JSON/CSV/logs, updates the tracker and checks plan criteria; W&B training checks are conditional. Positive main results request ablation planning; absent planner or nonpositive results skip that extension. Results and tracker paths plus completion counts form the return to the parent. This is artifact-level coordination under host interpretation, not proof that the host actually waits for truthful completion (SRC-1, `skills/experiment-bridge/SKILL.md`).

### Review, rejection and revision

The parent next invokes `/auto-review-loop` with the direction, selected idea and reviewer difficulty. The reviewer judges the product; the executor implements changes; [RT-RTE-review-transition](runtime.md#rt-rte-review-transition) computes stop/continue/escalate/unavailable from supplied fields. The ordinary Codex transport is [RT-RTE-codex-call](runtime.md#rt-rte-codex-call), but this is not the only backend. The child initializes an unspecified backend to `auto`, attempts a native marker/challenge, and selects native Copilot on binding or Codex on the specified unbound outcome. Explicit reviewer selection bypasses activation. Native evidence-helper internals remain uninspected, so this member does not generalize the Codex path to every fresh invocation (SRC-1, `skills/auto-review-loop/SKILL.md`).

The reviewer returns score, verdict and ranked fixes. The executor must preserve its full raw response and append reviewer memory before stop evaluation. Only the gate's `stop` authorizes positive termination; score alone does not. Compatibility Copilot positives require a finalizer, while native Copilot and default Codex have different evidence/identity conditions, retained in the runtime record rather than flattened into a universal independence guarantee. Unresolved or unexecutable gating terminates as unavailable:

> A `review_unavailable` decision is terminal.
> --- `skills/auto-review-loop/SKILL.md`

On a continuing round the foreground agent modifies code/analysis, deploys requested experiments, waits for results and documents actions and outcomes. Expensive or unavailable-data fixes may be deferred and flagged, so continuation does not mean all criticisms were resolved. Optional human checkpoints allow changing/skipping fixes or stopping; default operation has no such per-round approval. The protocol requires implementation before re-review:

> Implement fixes BEFORE re-reviewing (don't just promise to fix)
> --- `skills/auto-review-loop/SKILL.md`

The bound is four rounds. Exhaustion without positive assessment produces remaining blockers, effort estimates and manual-continuation/pivot advice, not a successful review. A `completed` review-state label therefore denotes loop termination, not necessarily positive acceptance. These are instructions, not observed compliance (SRC-1, `skills/auto-review-loop/SKILL.md`, `skills/research-pipeline/SKILL.md`).

### Recovery and delivery

Two recovery scopes coexist. The pipeline records stage completion separately from acceptance and asks resume to re-audit done-but-unaccepted work; the helper's actual metadata checks and alternative advancement paths are bounded by [RT-RTE-phase-resume](runtime.md#rt-rte-phase-resume). Separately the review child reloads recent in-progress round state, review history and pending experiments. Its within-24-hour rule, saved next backend and thread/evidence/profile determine round continuation; stale in-progress state restarts. Neither mechanism proves that retained artifacts are correct or that a crash/resume has succeeded (SRC-1, `skills/research-pipeline/SKILL.md`, `skills/auto-review-loop/SKILL.md`).

Normal delivery is `NARRATIVE_REPORT.md` plus the pipeline report, assembled from idea, implementation, results and review history, with claim evidence, figures needed and remaining limitations. The narrative is also a future writing input. Review termination optionally calls `/result-to-claim`; absent skill skips it, while a returned `REVIEW_UNAVAILABLE` verdict must remain unchanged and claims must be labelled unadjudicated. Thus a downstream file name alone is not validation. These delivery and non-success distinctions are detailed in the annotations below (SRC-1, `skills/research-pipeline/SKILL.md`, `skills/auto-review-loop/SKILL.md`).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-sanity-recovery
Label: Bounded sanity failure recovery

Part of: [RT-RTE-research-pipeline](runtime.md#rt-rte-research-pipeline)

This material subroute has its own retry budget and deletion boundary inside the supplied pipeline container; it does not replace that route. Endpoints/progression: failed sanity output → error inspection/classification → patch and rerun → optional rescue → clean reimplementation → successful sanity or failure report. Owner: foreground executor; optional `/codex:rescue` offers another diagnosis, not unilateral acceptance. Context is the plan/research contract, failing generated scripts and primary error logs. Effects include modifying attempt code and rerunning experiments through host tools.

- Immediate return: passing sanity permits full deployment; exhausted or identically failing clean rebuilds return attempted fixes and logs with a failure report.
- Later read-back: uninspected — logs must be reported and plan/data/results preserved, but this passage does not specify a later invocation selecting the recovery history.
- Delegated visibility: rescue independently reads code and error logs when the plugin is available; exact transport context is uninspected here.
- Selection predicate: same-failure patch exhaustion triggers clean rebuild; budget exhaustion or two identically failing rebuilds stops. An unavailable rescue leaves foreground diagnosis in control.
- Invalidation or expiry: another failed sanity result rejects that attempt; no time-based expiry is specified for the retry evidence.
- Activation or effect: requests bounded code changes and experimental reruns; no successful repair or deployment observed.
- Evidence limits: doctrine/design in SRC-1, `skills/experiment-bridge/SKILL.md`; remote executor, rescue implementation and actual runs uninspected.
- design conclusion status: claimed
- operation conclusion status: uninspected

Admission/recovery: the executor proposes patches from error classes such as OOM, missing imports/paths and divergence, guided by the experiment plan and contract. It judges the rerun against sanity expectations; these are task checks, not a universal expected research answer. Human assistance is requested after repeated identical rebuild failure suggests a plan/environment problem. Recovery permits replacing only generated attempt scaffolding, not a repository-wide rollback. The plan, tracker, user source, data and results persist. This is bounded product repair, not established improvement of ARIS's own organization.

> Delete ONLY the
>   attempt's own code/scaffolding (scripts this phase generated); the plan,
>   `EXPERIMENT_TRACKER.md`, user-authored project source, collected data, and results
>   are never deletable
> --- `skills/experiment-bridge/SKILL.md`

The stop-budget passage is already retained under the parent runtime route; no duplicate evidence declaration is needed.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-research-pipeline](runtime.md#rt-rte-research-pipeline)

Workflow delivery distinction: Stage 4 synthesizes the research record, but synthesis is not a fresh adjudication of each claim. Exhausted review must report unresolved issues instead of forcing forward. With default `AUTO_WRITE=false`, paper-writing is marked skipped after summary acceptance, allowing resume to report COMPLETE without a paper. With `AUTO_WRITE=true` and missing venue/manual figures under nonblocking operation, writing is deferred and left pending; clean return is not full phase completion. Optional HTML failure is expressly nonblocking even though the summary-acceptance table mentions rendering. No inference of render success follows from summary delivery (SRC-1, `skills/research-pipeline/SKILL.md`).

> the HTML view is a convenience artifact, not a pipeline prerequisite.
> --- `skills/research-pipeline/SKILL.md`

Optional writing receives the narrative path, explicit venue and resolved auto-proceed setting; a successful child return is expected to supply PDF, source and improvement logs. Actual writing/audit execution and submission to a venue are not established. The representative trace ends at default narrative/report delivery, with paper production retained only as a conditional continuation (SRC-1, `skills/research-pipeline/SKILL.md`).

#### On [RT-RTE-review-transition](runtime.md#rt-rte-review-transition)

Workflow sequencing: raw response preservation and reviewer-memory append precede gating, so the terminal review is not supposed to disappear from later history. Continuing rounds document actions/results and persist the next backend, separately from the current round's snapshotted backend. This prevents an escalation request from being documented as if the finalizer had already performed the current review. These are host-followed instructions, not additional enforcement by the stateless helper (SRC-1, `skills/auto-review-loop/SKILL.md`).

Termination can return an unresolved product. The child writes a final method description for later illustration and may invoke result-to-claim, but explicitly prohibits upgrading unavailable claim adjudication:

> If it ran but its output starts with `verdict: REVIEW_UNAVAILABLE`, keep that file AS-IS (do not overwrite or paraphrase it) and record in `AUTO_REVIEW.md` that claims are UNADJUDICATED — downstream paper stages must not treat them as validated.
> --- `skills/auto-review-loop/SKILL.md`

#### On [RT-RTE-phase-resume](runtime.md#rt-rte-phase-resume)

Workflow recovery boundary: stage-level resume chooses the next unfinished acceptance obligation, whereas the review child's own recent-state recovery chooses the next round and reviewer continuation. Both require the foreground host to consume their outputs; neither resumes remote GPU work by itself. The pipeline permits warning and continuing when the phase helper is unresolved, so durable stage recovery is not guaranteed for every invocation (SRC-1, `skills/research-pipeline/SKILL.md`, `skills/auto-review-loop/SKILL.md`).
