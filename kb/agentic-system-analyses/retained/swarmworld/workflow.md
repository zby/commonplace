---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "SwarmWorld workflow: a headless model-agent research episode from configured invocation through planning, simulator rejection, outage recovery and recorded delivery."
run-id: AAS-2026-10-15-swarmworld-e39fbc17e3fb-01
reviewed-boundary: "6af7ae9fa36d98b07b0492cf139658e8af1f6eab"
---

# SwarmWorld workflow report

## Workflow account

The representative workflow is one headless CLI episode using an LLM policy. It is selected because the shipped `_simulate_episode` function connects model-agent planning, world effects, recovery and final output in one driver. This is an implemented workflow, not a reconstructed successful scientific discovery. A request supplies run configuration, policy, tick horizon and output path; the delivered product is an episode trace plus a printed metrics summary, not a model-authored answer accepted as scientifically true. The frozen source and external-data limits remain those of [the boundary](boundary.md#boundary-and-evidence).

Inspection here adds deeper implementation coverage of SRC-1, `src/biofoundry/cli.py` (episode orchestration and terminal summary), `src/biofoundry/policies/llm.py` (scheduled batch, context, admission and recovery), and `src/biofoundry/simulation.py` (action rejection, outcome feedback and replan triggers). All are at the reviewed commit. No target execution, provider response, episode artifact or passing replay was supplied or produced. The following account therefore establishes wiring, not observed coordination, reliable model compliance or research benefit.

### 1. The driver creates the job and owns its horizon

The CLI loads configuration and applies command-line overrides, then creates a simulation and policy inside `_simulate_episode`. It opens the recorder with configuration, engine revision and scenario metadata, writes an initial full snapshot/digest, and loops over the requested ticks. The driver—not an agent manager model—decides when planning and world stepping occur. This follows the ownership in [RT-RTE-model-planning](runtime.md#rt-rte-model-planning) and [RT-RTE-world-stepping](runtime.md#rt-rte-world-stepping). SRC-1, `src/biofoundry/cli.py`.

> ticks = args.ticks or config.simulation.max_ticks
> summary = asyncio.run(_simulate_episode(config, ticks, args.policy, args.output))
> print(json.dumps(summary, indent=2, sort_keys=True))
> --- `src/biofoundry/cli.py`

This request starts computation; it is not human approval of each plan, hypothesis or subsequent action. The finite horizon ends the episode independently of whether an agent believes its goal complete.

### 2. Scheduling hands local research work to agent-specific model calls

At a macroturn the policy takes scheduled agent IDs, limits that batch by remaining model-call budget, and concurrently invokes `_decide` for each selected ID. Each call receives a fresh system/user message pair: scenario or generic guidance, treatment action manual, semantic local observation, retrieved private-memory excerpts and the latest self-authored research state. Optional experience-attention trimming can omit retrieved records and observation details before delivery; it does not delete the underlying records. Agent IDs bind returned plans to queues and memories. See [RT-OBJ-action-queues](runtime.md#rt-obj-action-queues) and [RT-RTE-model-planning](runtime.md#rt-rte-model-planning). SRC-1, `src/biofoundry/policies/llm.py`.

This is fan-out by software scheduler, not a lead model delegating tasks to subordinate models and synthesizing their replies. The model calls propose each agent's research state and next action sequence. They do not receive another agent's hidden reasoning; shared-world observations and simulator-mediated communication are distinct from returning sub-agent answers. The scheduler waits for the batch, collects decisions by agent ID, and stores traces in sorted ID order, rather than treating completion order as execution priority.

### 3. Plan admission returns executable proposals, not verified science

Local JSON/schema admission and conversion precede private research-state writing and queue commitment. Retained evidence IDs are filtered to IDs resolvable in private memory, the public archive or program knowledge. That check establishes reference availability, not that cited evidence supports the hypothesis. Successful calls retain the research-state text; a later macroturn can receive it as prior state. The policy then replaces the agent's old queue with the newly admitted plan. See [RT-RTE-model-planning](runtime.md#rt-rte-model-planning). SRC-1, `src/biofoundry/policies/llm.py`.

> research_state["evidence_ids"] = sorted(retained_evidence)
> --- `src/biofoundry/policies/llm.py`

The proposing model chooses content; local code can reject its representation; no routine human approval or expected-answer oracle judges scientific merit. The action manual and empirical-grounding guidance shape the proposal, but schema success is neither a truth check nor evidence of useful theory revision. The separate theory-property limits in the runtime planning record apply here unchanged.

### 4. The driver hands one queued action per agent to the world

Only after planning commits does the driver consume the next actions, record that action mapping and call `simulation.step`. The simulator converts/admits actions, checks executable verbs and action-specific conditions, then advances artifacts/world dynamics. Repeated ticks consume the bounded queues until replaced or exhausted; an empty queue yields WAIT. This is a second decision boundary: schema-admitted proposals can still fail world admission. See [RT-RTE-world-stepping](runtime.md#rt-rte-world-stepping) and [RT-BAP-action-dispatch](runtime.md#rt-bap-action-dispatch). SRC-1, `src/biofoundry/cli.py`, `src/biofoundry/simulation.py`.

For simulator validation failures caught by the action dispatcher, it emits `action_rejected` with the agent, verb and reason. When collective-science action feedback is enabled, it also records an outcome. Successful configured experimental verbs can mark an agent for immediate replanning; rejection itself is not evidence of automatic model repair. A later scheduled model decision can choose a different plan from changed observations and retained outcomes. No source-supplied execution demonstrates that repair succeeding.

> except (RecipeValidationError, ProgramValidationError, RuntimeError, ValueError) as exc:
>     success = False
>     failure_reason = str(exc)[:240]
> --- `src/biofoundry/simulation.py`

> self._record_action_outcome(index, action, success, detail, events)
> --- `src/biofoundry/simulation.py`

This is per-action rejection and later feedback, not whole-tick rollback. The existing world-stepping record bounds previously performed sub-effects and the distinction between physical effects and claimed function.

### 5. Provider failure has a different recovery owner

An invalid output or provider exception yields a WAIT proposal and error trace. Without outage freezing, that failed decision can replace its old queue with WAIT. With freeze-on-provider-outage enabled, any transient provider failure in the scheduled batch—not just a total outage—causes restoration of scheduled agents' memory snapshots, preservation of old queues and a false commitment return. Even successful decisions in that batch are not committed. The CLI records the traces and an outage record, waits the configured retry interval and retries without advancing the world. SRC-1, `src/biofoundry/policies/llm.py`, `src/biofoundry/cli.py`; [RT-RTE-model-planning](runtime.md#rt-rte-model-planning).

> "world_advanced": False,
> --- `src/biofoundry/cli.py`

The policy owns batch restoration; the driver owns waiting and withholding world advancement. Provider availability remains external, so this path supplies no eventual-completion guarantee. Invalid output and terminal provider errors do not trigger this freeze. The convenience policy `actions()` route does not honor false in the same way; the no-advancement conclusion is specific to the inspected driver protocol, as the runtime record already establishes.

### 6. Delivery closes recording, then returns the summary

The driver records step events and periodic full snapshots. At the end of its tick loop it writes a final snapshot/digest before leaving the recorder context. It constructs a summary containing final positions, artifact and ecology metrics, event/action counts, model usage/errors, the digest and the absolute output path. Optional evaluator/checkpoint results and scenario analysis can augment the summary before return. The CLI prints that returned JSON. SRC-1, `src/biofoundry/cli.py`.

> digest = simulation.state_digest()
> recorder.write_snapshot(
>     simulation.snapshot(display_limit=None),
>     state_digest=digest,
> )
> --- `src/biofoundry/cli.py`

Delivery here means the shipped function reaches its normal return after recording and summary construction. It does not mean an evaluator certified a theory, that artifacts exceeded an improvement threshold, or that the trace replayed successfully. Optional assay results are report fields rather than a plan-admission or delivery-acceptance gate; see [RT-RTE-ecology-assay](runtime.md#rt-rte-ecology-assay). Replay is a separate verification consumer with compatible-state/digest rejection, not a mandatory stage of this episode; see [RT-RTE-recorded-replay](runtime.md#rt-rte-recorded-replay). The source supports this end-to-end orchestration, but without run evidence it cannot establish that a particular episode completed, recovered or produced useful scientific work.

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

#### On [RT-RTE-model-planning](runtime.md#rt-rte-model-planning)

Workflow role: the per-agent planning handoff inside a driver-owned episode. Batch return is not the terminal product: the driver must honor commitment before consuming queues. Models propose local research work; there is no model-manager answer-synthesis stage in the inspected driver. Outage recovery requires both policy restoration and driver retry, with no eventual provider-recovery guarantee.

#### On [RT-RTE-world-stepping](runtime.md#rt-rte-world-stepping)

Workflow role: effect admission after plan admission. Rejection feedback can inform later planning when enabled, but a completed tick does not certify an agent's scientific claims. Episode delivery depends on recorder closure and summary return, not on every supplied action succeeding.

#### On [RT-RTE-ecology-assay](runtime.md#rt-rte-ecology-assay)

Workflow role: optional checkpoint/final report production. The episode caller includes results in researcher-facing output rather than using them to approve the model's plan or requiring a scientific success threshold before normal return.
