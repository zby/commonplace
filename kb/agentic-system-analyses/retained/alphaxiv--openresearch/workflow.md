---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "OpenResearch workflow account: a local snapshot experiment from project request through asynchronous execution, evidence inspection, repair and chat delivery."
run-id: AAS-2026-10-20-openresearch-62725ad1cd0a-01
reviewed-boundary: "2c45ff3183b494aac4001bd44eefbe57a3c249ae"
---

# OpenResearch workflow report

## Workflow account

The representative workflow is a project-scoped request to run and summarize an experiment using the configured local backend. It was selected because the shipped playbook explicitly routes that request through compute and results skills, and the supplied runtime traces local execution end to end. It connects actual shipped responsibilities rather than joining unrelated capabilities: user message, native agent, committed experiment branch, detached compute, completion signal, log inspection and cited chat response. The request and local configuration are scenario conditions, not an observed user session. All findings use SRC-1 at the frozen revision; implementation and doctrine/design evidence do not establish successful execution or scientific benefit.

### Request, preparation and delegation

The UI/API submits a session-scoped user message. ChatHost owns start/queue admission and dispatch to the selected installed harness; the native model owns subsequent tool/text decisions. For the sampled Claude path, a private worktree, project-state playbook, skill folders and native resume or bounded transcript recovery prepare the context. These are the handoff described by [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn) and [RT-OBJ-playbook](runtime.md#rt-obj-playbook). A private worktree separates ordinary edits, not OS capabilities. Permission review can interpose code and human decisions on supported native requests, but its coverage depends on the harness, as bounded by [RT-RTE-permission-review](runtime.md#rt-rte-permission-review).

The playbook directs the agent to load compute and results instructions before launching. The experiment-tree skill supplies the planning protocol: inspect baseline code and run command; make hypothesis-relevant child branches; implement and commit changes; print effective configuration, final metrics and a compact summary. These are requested model behaviors, not an enforced experiment planner (SRC-1 `SYSTEM_PROMPT.md`, `agent-skills/orx-experiment-tree/SKILL.md`).

> Before launching, ensure the committed code
>    prints its effective configuration, final metrics, and a compact summary to
>    stdout. Long runs should also print periodic searchable metrics.
> --- `agent-skills/orx-experiment-tree/SKILL.md`

The agent hands `orx exp run` an experiment identity and applicable backend settings. The code resolves the branch tip and inherited command, stages an immutable source archive and reserves a run. A default in-flight guard can reject another run on the node unless explicitly forced. The local controller receives selected committed files, command and environment, extracts a run directory and starts detached execution and supervision. This delegation is to a process/controller, not a separate reasoning agent. [RT-RTE-experiment-run](runtime.md#rt-rte-experiment-run) and [RT-OBJ-source-snapshot](runtime.md#rt-obj-source-snapshot) provide the implementation evidence and bound the snapshot guarantee: uncommitted edits are excluded, but ambient data, dependencies and services are not all frozen. Code owns launch admission and run-state maintenance; it does not approve the scientific hypothesis.

### Asynchronous return and verification

Submission returns a run identity rather than a measured answer. The agent may block with wait or explicitly register wake and end its turn; the compute skill says to choose one, not both. In a multi-run round, wait is only a completion signal: the instructed foreground agent rereads all run states to catch completions that happened while it was analyzing another result. This is a model-operated reconciliation loop, not proof that a scheduler interprets every completion (SRC-1 `agent-skills/orx-compute/SKILL.md`, `agent-skills/orx-experiment-tree/SKILL.md`).

> A wait is a sleep-until-change signal, not the source of truth. After every
>   return, read `orx runs <projectId>` and reconcile all newly terminal runs.
> --- `agent-skills/orx-compute/SKILL.md`

For the wake alternative, the host claims an idle session and sends status-only hidden text after prior opt-in. It does not automatically deliver a final metric or full log. [RT-RTE-run-wakeup](runtime.md#rt-rte-run-wakeup) bounds persistence, claim release, monitoring alerts and delivery. Thus the next native invocation must still retrieve evidence; a completion message is not a verification verdict.

The actual evidence handoff is selective. [WF-RTE-log-retrieval](#wf-rte-log-retrieval) establishes that `orx logs` supplies a local file path, byte size and short tail, not the entire output. The native agent is instructed to search/read the file and then apply [WF-RTE-result-handoff](#wf-rte-result-handoff). Verification asks whether the log identifies the variant/configuration, contains final metrics and summary, preserves the trajectory where needed, and actually supports the citation. Process success cannot accept a measured claim. The evidence gate here is natural-language guidance to the model, not a symbolic validator that blocks unsupported final responses.

### Failure, recovery and delivery

Two failure layers have different owners. At the execution layer, software can reject a conflicting launch; cancellation and detached supervision handle run lifecycle, and startup can reattach supervision independently of chat. These are wired paths in [RT-RTE-experiment-run](runtime.md#rt-rte-experiment-run), not proof of flawless recovery or exactly-once external effects. At the interpretation layer, a model is told not to treat missing evidence, timeout or unintended failure as a scientific result. The results handoff owns that instruction, not the run-status field.

For repair, the experiment-tree skill distinguishes an unanswered provisional node from an answered frozen node. It tells the agent to repair/relaunch the former in place, but branch a child after a genuine answer, even a disappointing result. An OOM can itself answer a memory hypothesis; the rule depends on the question, not merely the exit status. Two consecutive unanswered runs require asking the user, as does the same failure on a second node. This cap is an instructed escalation policy, not an inspected counter-based launch veto (SRC-1 `agent-skills/orx-experiment-tree/SKILL.md`).

> **Repair cap:** two runs in a row that answer nothing on one node, then ask the
> user. Different errors still count; a bare relaunch or a flavor/backend switch
> is a repair.
> --- `agent-skills/orx-experiment-tree/SKILL.md`

A successful handoff, as specified rather than observed, is a short explanation of what changed, what ran and what the evidence shows, with limitations and raw run/file references. Results guidance permits a concise text-only result; graphics are optional and may not invent data. A turn that ran or changed experiments should close with a per-node summary. In a continuing research round the model may repair, refill, promote or stop; those choices remain model judgments under the task and skills, not a scientific answer oracle or automatic ranking function. The delivered response travels through the persisted native-turn/UI path in [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn). Persisted assistant output establishes transport wiring, not that its measurements are valid, the user accepted it, or the research objective was met.

Added SRC-1 coverage beyond the supplied baseline: complete reads of `agent-skills/orx-compute/SKILL.md`, `agent-skills/orx-compute/references/local.md`, `agent-skills/orx-experiment-tree/SKILL.md`, `agent-skills/orx-logs/SKILL.md` and `src/commands/logs.rs`, plus rereads of `SYSTEM_PROMPT.md` and `agent-skills/orx-results/SKILL.md`. The Rust file supplies implementation evidence; the skills and prompt supply doctrine/design. No target code, tests, examples or services were executed. This account does not establish backend parity, native sub-agent context isolation, compliance with repair caps, or exercised research quality.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-log-retrieval
Label: Persisted log retrieval

Part of: [RT-RTE-experiment-run](runtime.md#rt-rte-experiment-run)

This is the concrete log-consumption subroute of the supplied run route, not a second declaration of submission or supervision. Endpoints: run identity → `resolve_run` → persisted local log → compact stdout summary → model file search/read. Rust owns identity resolution, file opening and bounded preview; the foreground agent chooses subsequent evidence reads. SRC-1 `src/commands/logs.rs` supplies implementation evidence; `agent-skills/orx-logs/SKILL.md` supplies the requested continuation.

> const PREVIEW_CHARS: usize = 500;
> --- `src/commands/logs.rs`

> "Use targeted search on this path (for example `rg PATTERN` or an editor) to inspect portions of the log. This preview is not proof of absence."
> --- `src/commands/logs.rs`

> Truncated output is not evidence of absence. Search or read the reported file until
> the relevant portion has been found.
> --- `agent-skills/orx-logs/SKILL.md`

- Immediate return: file path, exact byte length and last approximately 500 characters; a missing file prints that no log is captured yet and returns successfully, without synthesizing a result.
- Later read-back: the persisted run output can be searched/read by later agent invocations through the printed path; actual file consumption is not observed.
- Delegated visibility: the calling native agent initially receives only compact stdout; the full log remains outside its context until file tools retrieve selected portions.
- Selection predicate: caller supplies run ID; code resolves it and computes its log path; byte-suffix and character-tail rules select preview, then the agent selects further ranges.
- Invalidation or expiry: uninspected — this read command does not establish log-retention duration or deletion policy; metadata-captured length bounds this preview read and truncation can cause an error.
- Activation or effect: wired delivery of a pointer and bounded evidence preview; the instruction requests targeted rereading rather than flooding the context with the entire log.
- Evidence limits: source only; preview inclusion does not prove sufficient evidence, model rereading or correct interpretation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### WF-RTE-result-handoff
Label: Measured result handoff

Endpoints and progression: retrieved run evidence → native agent's requested evidence check and interpretation → cited chat summary, with optional next experiment. Owner: foreground model under user task and shipped instructions. This is distinct from [RT-RTE-experiment-run](runtime.md#rt-rte-experiment-run), which launches and maintains execution, and [RT-RTE-run-wakeup](runtime.md#rt-rte-run-wakeup), which supplies a status stimulus. Neither supplied route declares the content-level reporting protocol. SRC-1 `agent-skills/orx-results/SKILL.md`, `SYSTEM_PROMPT.md` and `agent-skills/orx-experiment-tree/SKILL.md` supply doctrine/design, not an observed verification pass.

> Never infer a result from run status or memory. Before accepting or reporting a
> run-derived claim, confirm that:
>
> - the log identifies the variant and effective configuration;
> - the final metric and compact summary are present;
> - the relevant trajectory is recoverable for a long run; and
> - the cited file lines actually contain the supporting output.
> --- `agent-skills/orx-results/SKILL.md`

> Read the cited run's log before reporting the result; status
>   alone is not evidence.
> --- `SYSTEM_PROMPT.md`

> Briefly explain what changed, what ran, and what the evidence shows.
> --- `agent-skills/orx-results/SKILL.md`

- Immediate return: requested short measured-result explanation and limitations, with run/file evidence references; no separate software acceptance result is established.
- Later read-back: chat persistence and native resume can make the summary available later through the supplied chat route; actual subsequent reliance is unobserved.
- Delegated visibility: foreground model receives selected log portions through tools, rather than an automatically complete experiment dossier; user receives its selected explanation and references.
- Selection predicate: results skill applies before measured-result reporting or evidence-based next-experiment recommendation; the model chooses relevant measurements and presentation.
- Invalidation or expiry: inapplicable — no automatic expiry or retraction protocol is specified by these reporting instructions; unsupported output is to be withheld rather than inferred from status.
- Activation or effect: instructions request evidence-conditioned reporting and repair/refill/promote/stop decisions; compliant behavior and changed subsequent experiments remain unobserved.
- Evidence limits: a requested semantic check, not a wired correctness gate; no inspectable response or user acceptance is supplied.
- instruction conclusion status: claimed
- operation conclusion status: uninspected

Admission and comparison: the foreground model proposes an interpretation and next action, and is instructed to reject unsupported measured claims. A user supplies the goal and can be asked to resolve uncertainty or repeated failures; no mandatory per-result human approval is specified in these passages. There is no expected-answer oracle supplied by this reporting protocol: logs are measured evidence, not a predesignated correct interpretation. Operating mode is an open project request, with optional rounds of hypotheses rather than a scored curriculum. Guidance shapes proposals through fixed run contracts, frozen answered nodes and evidence inspection. A provisional failure may trigger repair on the same node; an answered node should retain its measured source and spawn a child for changes. Persistence is chat output and experiment/run state, not an established revision of the runtime's own methods. No automatic rollback of an already reported unsupported conclusion is established by these instructions.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn)

Workflow role: carries the initial problem and final assistant response. A started/queued turn and a persisted final message are transport milestones, not acceptance of scientific content. Worktree separation and native transcript recovery must not be confused with an independently verified reasoning handoff.
