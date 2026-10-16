---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Exo workflow account tracing a Harbor trial from job admission through attached-container execution and trajectory delivery."
run-id: AAS-2026-10-15-exo-f0905e2cf44b-01
reviewed-boundary: "423d7d0f4394a1ddc9955d13c73c9f8a9c4d4e7e"
---

# Exo workflow report

## Workflow account

### Selection and evidence boundary

The selected workflow is one Harbor evaluation trial using the default Exo harness: prepare a shared agent, create a trial conversation, attach Harbor's task container, delegate the instruction to Exo, and export the conversation as a trajectory. This shipped caller makes request ownership, execution ownership and delivery separate and inspectable. It is representative of Exo's evaluation integration, not a claim that every interactive or hosted invocation uses this sequence. The workflow is established as wiring, not as a successful trial. See [WF-RTE-harbor-trial](#wf-rte-harbor-trial).

All evidence is static implementation from SRC-1 at the reviewed commit. Added inspection covers `eval/harbor/src/exo_harbor/plugin.py`, `eval/harbor/src/exo_harbor/agent.py`, `eval/harbor/src/exo_harbor/exo.py`, `eval/harbor/src/exo_harbor/conventions.py` and `eval/harbor/src/exo_harbor/trajectory.py`. No target or evaluator was executed. Harbor's external lifecycle, grading internals and model-provider behavior are not established by this inspection.

### 1. Admit the job and bind shared state

The session plugin accepts Docker jobs with exactly one configured agent. For the default `exo` harness it rejects concurrent trials unless the concurrency is one. This is a configuration gate intended to avoid shared-agent races, not evidence that sequential trials produce learning. The plugin constructs an `ExoClient` from the supplied binary, state root, repository root and model options, then ensures the `harbor-eval` agent exists. An existing agent is reused without reapplying the requested model; creation supplies the model, Docker provider and, for this default harness, `exo/harness.ts` with tool creation enabled. SRC-1: `eval/harbor/src/exo_harbor/plugin.py`, `eval/harbor/src/exo_harbor/exo.py`, `eval/harbor/src/exo_harbor/conventions.py`.

> if job.config.n_concurrent_trials != 1 and harness == EXO_HARNESS:
> --- `eval/harbor/src/exo_harbor/plugin.py`

The plugin leaves run state in place at job end. The retained shared agent and per-trial conversation are different scopes; a fresh conversation does not establish a fresh agent or fresh source tree. The workflow does not demonstrate any actual cross-trial behavioral change. SRC-1: `eval/harbor/src/exo_harbor/plugin.py`, `eval/harbor/src/exo_harbor/exo.py`.

### 2. Delegate task effects into the borrowed container

Harbor supplies the environment and context identity. `ExoAgent.setup` resolves a running Docker container by the normalized Compose project and `main` service labels. Zero matches reject setup; multiple matches reject rather than guess. It ensures a conversation named `trial-<context_id>`, then calls `exo sandbox attach` with that container's external ID. The wrapper requires a sandbox ID in the command's output before setup succeeds. Harbor owns the container; Exo borrows it for the conversation's turns. These checks establish target selection and setup prerequisites, not task correctness or container isolation. SRC-1: `eval/harbor/src/exo_harbor/agent.py`, `eval/harbor/src/exo_harbor/exo.py`.

> if len(ids) > 1:
>     raise RuntimeError(
>         f"{len(ids)} running {MAIN_SERVICE} containers for Compose project "
>         f"{project!r}; refusing to guess"
>     )
> --- `eval/harbor/src/exo_harbor/agent.py`

### 3. Hand the instruction to the agent loop

`run` requires successful setup and passes the instruction, conversation slug and optional timeout to the client. The client launches `exo --root <state-root> --harness exo thread send harbor-eval <conversation> <instruction>` in the repository directory, with `EXO_ROOT` and an `EXO_PROFILE` default of `practical`. The caller supplies the task, not a plan or expected answer. SRC-1: `eval/harbor/src/exo_harbor/agent.py`, `eval/harbor/src/exo_harbor/exo.py`.

Exo's downstream admission and executor responsibilities are supplied by [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn); the default Exo profile's model/tool progression is [RT-RTE-responses-loop](runtime.md#rt-rte-responses-loop), not Basic's recovery algorithm. The model chooses actions from the profile's tools, while software dispatches and applies path-specific authorization. The runtime records messages and tool activity for later consumption. The integration does not itself delegate to a planner/reviewer pair or independently check the model's answer. Nor does the wrapper's process timeout establish cancellation of every descendant or external effect; its inspected enforcement is killing and waiting for the CLI subprocess. See the workflow annotations below.

### 4. Preserve an inspectable result, including on failure

Successful `send` returns printed messages, but `ExoAgent.run` discards that return value. Its durable handoff to Harbor is conversation metadata plus an attempted `trajectory.json` export. A `finally` block runs that export after normal return, a command error or timeout. The client kills and waits for the subprocess on timeout/cancellation and re-raises. The driver does not retry the task; `SUPPORTS_RESUME` is false. Export failure is logged and suppressed, so it cannot substitute for successful task execution or guarantee a trajectory file. SRC-1: `eval/harbor/src/exo_harbor/agent.py`, `eval/harbor/src/exo_harbor/exo.py`.

> except (asyncio.TimeoutError, asyncio.CancelledError):
>     # Kill rather than terminate: the turn holds a sandbox and we want
>     # the process gone before the caller moves on.
>     process.kill()
>     await process.wait()
>     raise
> --- `eval/harbor/src/exo_harbor/exo.py`

The export requests up to 10,000 events of three types and validates the returned JSON. It does not follow the returned cursor. It reconstructs a user instruction step, assistant steps, tool requests and matched observations; unmatched tool results are skipped. Runtime tool results contribute their value if available, otherwise their preview. Thus the delivered trajectory is a projection, not necessarily the complete journal, full tool output or proof of successful completion. See [WF-OBJ-trajectory](#wf-obj-trajectory). SRC-1: `eval/harbor/src/exo_harbor/trajectory.py`.

Delivery has two bounded meanings here: the CLI completed a task attempt, and the exporter successfully replaced the destination file. Neither is a correctness acceptance decision. Harbor's actual grading, any reference outcome and subsequent use of the trajectory are external and uninspected; no benchmark success or measured benefit is inferred.

## Shared records

### Components

none declared in this member

### Operative objects

#### WF-OBJ-trajectory
Label: Harbor trajectory

Source-native identity: the per-trial `trajectory.json` ATIF artifact emitted by `export_trial_trajectory`. Representational form: symbolic JSON identities, tool arguments, observation flags and metrics, with natural-language instruction, assistant text, reasoning text and observation content. Storage substrate: Harbor trial logs directory; written through a temporary sibling and replacement. SRC-1: `eval/harbor/src/exo_harbor/trajectory.py`, `eval/harbor/src/exo_harbor/agent.py`.

Compared with [RT-OBJ-turn-work](runtime.md#rt-obj-turn-work), this is an output projection of recorded events, not the queued execution envelope. It is also distinct from [RT-OBJ-guardian-update](runtime.md#rt-obj-guardian-update): it describes a trial, not host deployment status. No counterpart is declared in the supplied runtime member.

The exporter fetches a single page, rejects an empty event list, validates supported event shapes, joins calls/results by tool-call ID and synthesizes usage totals from supplied usage fields. It records model identity from usage where present and the configured model in trajectory metadata; these are not verification of actual provider resolution. The cursor is modeled but not consumed. Runtime result previews may already be truncated; native-agent results have their own text extraction. No full-output or complete-history guarantee follows. SRC-1: `eval/harbor/src/exo_harbor/trajectory.py`.

> temporary = destination.with_suffix(destination.suffix + ".tmp")
> temporary.write_text(json.dumps(trajectory.to_json_dict(), indent=2) + "\n")
> temporary.replace(destination)
> --- `eval/harbor/src/exo_harbor/trajectory.py`

### Routes

#### WF-RTE-harbor-trial
Label: Harbor trial orchestration

Endpoints: Harbor job/trial instruction and environment → Exo CLI/conversation and attached sandbox → Harbor metadata and trajectory artifact. Owners: session plugin admits job configuration; per-trial driver sets up the container binding and sends the task; Exo owns model/tool progression; exporter constructs the inspection artifact. SRC-1: `eval/harbor/src/exo_harbor/plugin.py`, `eval/harbor/src/exo_harbor/agent.py`, `eval/harbor/src/exo_harbor/exo.py`, `eval/harbor/src/exo_harbor/trajectory.py`.

Distinct identity: this orchestration spans client setup, one invocation and export. Its downstream execution overlaps [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn) and [RT-RTE-responses-loop](runtime.md#rt-rte-responses-loop), but neither record includes the plugin's job rejection, borrowed-container selection or Harbor artifact delivery. It is not contained in exactly one supplied route.

- Immediate return: normal `run` returns no answer value; the client internally returns printed text. Errors/timeouts propagate, while trajectory-export errors are logged and suppressed.
- Later read-back: the shared saved agent survives trials and job end; named trial conversations can be reused if already present. Later CLI calls read recorded conversation events to export the trajectory. Later Harbor artifact consumption is uninspected.
- Delegated visibility: Exo receives the task instruction, selected agent/conversation, root/profile configuration and attached sandbox binding. The exporter receives only the requested event page; Harbor metadata receives the conversation slug.
- Selection predicate: job harness and model options, fixed agent slug, context-derived trial slug, Docker Compose labels, and exporter event-type filter with a 10,000-event limit.
- Invalidation or expiry: per-trial driver is not resumable; Harbor owns container cleanup. Job-end code preserves Exo state. Successful export replaces the destination file; no automatic state reset or trajectory pagination is implemented in these paths.
- Activation or effect: the requested turn can act through Exo's selected harness in the attached container and other granted tool surfaces; exporter writes a projected artifact. Actual task effects and later behavioral dependence are unobserved.
- Evidence limits: static wiring only; no trace establishes completed execution, complete export, useful answer or successful grading. Killing the wrapper process is not proof of rollback of prior effects.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission and verification: caller configuration proposes the job and task. Plugin code can reject non-Docker, multi-agent or concurrent default-Exo jobs; container selection and attach-output parsing can reject setup; CLI exit status and event/schema validation check transport and representation. These are software checks, not per-answer human review. Human authorship of instructions is uninspected. Operating mode is a configured evaluation task sequence, not an inspected candidate-comparison or improvement curriculum. No expected-answer oracle is supplied to the driver in these files; external grading remains uninspected. The workflow retains agent state and event-derived artifacts, but neither retention nor sequential execution establishes improvement. Failure recovery here is bounded salvage through attempted export, not task retry, semantic repair or rollback. SRC-1: `eval/harbor/src/exo_harbor/plugin.py`, `eval/harbor/src/exo_harbor/agent.py`, `eval/harbor/src/exo_harbor/exo.py`, `eval/harbor/src/exo_harbor/trajectory.py`.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn)

Workflow role: downstream admission/execution boundary after the Harbor client sends its instruction. The caller's timeout is a separate client-side boundary, not evidence of runtime rollback. The selected default Exo harness must not inherit Basic-only safe-resumption conclusions from this record. Delivery to Harbor additionally requires the driver's metadata/export path; a runtime completion marker alone is not an exported trial artifact.

#### On [RT-RTE-responses-loop](runtime.md#rt-rte-responses-loop)

Workflow role: the selected Exo profile owns model/tool continuation after the trial handoff. Tool outputs can inform subsequent model choices, but the surrounding trial driver supplies no independent answer-review stage. The exported trajectory observes a projection of resulting events, not the complete context that each model invocation received. Source wiring does not establish compliance, correctness or successful task delivery.
