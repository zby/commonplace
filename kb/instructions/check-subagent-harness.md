---
description: "Use when checking another harness at two layers: orchestrating one Commonplace analysis, then maintaining the outer four-pipeline rerun workflow"
type: types/instruction.md
---

# Check a subagent harness

Determine whether the current harness can orchestrate one Commonplace analysis
and, separately, the outer rerun workflow, with exact launch recipes, tested
limits and explicit blockers for an operator's adoption decision.

## Consumption and scope

An operator gives this document to an agent running inside the harness being
assessed. It is a requirements checklist and bounded check procedure, not a
claim that any harness already meets the requirements. Use the actual loaded
tools and runtime settings, not a remembered product feature list. Report the
harness version, configuration and account restrictions that bound the result.

This instruction authorizes inspection and a report in the conversation. It does
not authorize production workers, workflow recovery, installation, configuration
changes or an adapter implementation. Live diagnostic launches require explicit
operator approval and must also satisfy the current harness's standing preflight.
If launch authority or tools are missing, return the inspection result; do not
acquire tools or launch an agent CLI through a shell as a substitute.

Assess exactly two layers. The operator may request either layer; if unspecified,
assess both by inspection. Basic worker support is part of layer 1, not a third
layer.

### Layer 1: orchestrate one analysis

An analysis runs as one `commonplace-analysis run` process in its prepared
isolated worktree. Code schedules the jobs and launches every analytical
worker itself, as a fresh headless session of the worker profile's harness
(`claude -p`, `codex exec` or `pi -p`); the agent commissioning the analysis
launches no workers. It confirms the target, prepares the worktree, starts the
run, waits for it to exit, and reports with `commonplace-analysis inspect`. It
does not select analytical jobs, judge outputs, invent retries or bypass stops.

The operational interface is the current analysis skill,
`kb/agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md`.
This check does not execute that workflow. A layer-1 assessment establishes
that an agent in this harness can run a shell command lasting hours in a
chosen working directory, wait for its exit and read its status and output;
the harness's own subagent tool is not involved. Whether a harness can serve
as the workers' headless harness is a separate question, answered by the
worker-profile probes, not by this check.

### Layer 2: orchestrate the outer rerun workflow

An outer orchestrator executes `kb/work/agentic-system-reruns/README.md`: maintain
four independent system pipelines, each with a fresh analysis coordinator
followed by a fresh independent auditor. After audit disposition or a recorded
hold, refill that slot without waiting for the other pipelines. The outer
orchestrator owns assignments, recovery decisions and serial integration.

Layer 2 needs layer 1 inside a delegated coordinator, establishing the full
outer orchestrator → analysis coordinator → `commonplace-analysis run` path. Four is the
outer pipeline count, not a global limit on all descendants. The inner round
boundary must not become a barrier between independent outer pipelines. Report
the two layers separately; layer 1 can pass while layer 2 is unsupported.

## Requirements

Map each requirement to an exact native operation or an already installed adapter.
Separate runtime-enforced properties from instructions the model must obey.

| ID | Applies to | Required behavior and evidence |
|---|---|---|
| B1 | Layer 1, inherited by layer 2 | Launch a genuinely fresh conversation without parent turns, summaries, prior answers or automatic answer forwarding. Shared repository rules are allowed and must be identified. A request to “ignore history” is not isolation. |
| B2 | Both layers | Deliver the exact task handoff, including an absolute invocation-file path when supplied. The child can read the complete file and recover truncated reads. Do not replace a supplied handoff with the parent's interpretation. |
| B3 | Both layers | Deliver applicable standing instructions and job contracts with known authority. Identify what is automatically loaded, explicitly read, or absent; do not assume inheritance across harnesses. |
| B4 | Both layers | Provide the job's needed file and command tools. Select or verify the requested model and reasoning effort through supported overrides or binding inheritance. Report requested and runtime-exposed identity separately; never infer execution identity from a role name or successful reply. Unknown required settings block model-specific work. |
| B5 | Both layers | Execute in the commissioned directory with the intended code, command environment and resources. A worker in another worktree must not silently use the origin's definitions or shared editable installation. Identify cwd, executable resolution and definition/configuration origins. |
| B6 | Both layers | Return an individually attributable result or failure. Preserve the task/attempt mapping, tool-call/result pairing, command exit status, stderr and relevant output. Surface truncation and how complete evidence can be obtained. A child process exiting normally does not mean its workflow succeeded. |
| B7 | Both layers | Know when a worker can no longer write before replacing it or reassigning its output. Explain cancellation, termination acknowledgement, session shutdown and interruption behavior. Expose uncertainty after crashes rather than treating an empty registry as proof of termination. |
| B8 | Both layers | Preserve the commissioned write scope and evidence boundary. State whether these are instructions or sandbox enforcement. Fresh conversation isolation is not filesystem isolation; shared filesystem access must not be described as a sandbox. |
| A1 | Layer 1 | Run `commonplace-analysis run` in the prepared worktree as one shell command lasting hours, without the harness ending it, and read its exit status and output when it ends. State the harness's command timeout and how a command outlives a tool call (a background process whose exit is awaited, a terminal the operator keeps open). |
| A2 | Layer 1 | Let the run's workers, which are fresh headless sessions of the worker profile's harness started by code, run unattended: the harness running this agent must not prompt for, throttle or kill the child processes. Capacity for the workers is the worker harness's, checked by the worker-profile probes, not this agent's subagent pool. |
| R1 | Layer 2 | Launch four independent coordinators without awaiting all their completions in the launch call. Return control to the orchestrator while unfinished jobs continue. Handles, callbacks or another supported completion interface may satisfy this. |
| R2 | Layer 2 | Receive one terminal result and launch its successor while other jobs remain live. Demonstrate first-completion handling and refill; progress messages from a wait-for-all call are insufficient. |
| R3 | Layer 2 | Distinguish active, terminating and terminal jobs; retain results until recorded or explicitly consumed. State repeated-read, cancellation, failed-start and capacity behavior. The orchestrator can retain a durable job-to-assignment mapping outside ephemeral handles. |
| R4 | Layer 2 | Demonstrate the outer orchestrator → analysis coordinator → `commonplace-analysis run` path with the required isolation, tools and model/effort at each boundary. The run's own workers are processes of the worker harness, outside the subagent pool. Show the resource policy and bounded observed capacity. |
| R5 | Layer 2 | Resolve trust and approval for the commissioned destinations before unattended dispatch. Support either bounded preapproval or an explicit operator interaction plan. Do not disable trust globally or treat external source repositories as trusted agent configuration. |

The workflow owns scheduling, audit disposition, acceptance, integration and
recovery. The harness only supplies execution and lifecycle operations. Neither
a transport success nor a worker's self-reported completion substitutes for the
workflow's validation and publication checks.

These are behavioral requirements, not demands for Pi's implementation. Separate
OS processes, a tool named `subagent`, `fork_turns`, `action`, `handles`, agent
Markdown files, persistent sessions and a particular renderer are not required.
Automatic retry, resuming the same worker, unlimited depth and crash-surviving
handles are also not prerequisites. Describe their presence or absence only
where it changes execution or recovery. Do not retry failed probes automatically.

## Inspection first

1. Identify the loaded harness and delegation tool schema. Read relevant local
   runtime documentation if available. Distinguish an installed implementation
   from operations exposed to this session; an unavailable operation is not usable
   merely because code or documentation names it.
2. Map the requirements to actual arguments and result fields. For every gap,
   identify whether it is a missing capability, missing permission, unsupported
   model, configuration problem, or untested behavior. Preserve exact errors.
3. Identify which properties require live evidence. If probes are not authorized,
   stop with a provisional report and the smallest proposed probe budget. Do not
   claim a complete layer pass from inspection alone.

## Bounded live probes

Before probing, obtain approval for the selected layers, model/effort settings,
maximum launches, maximum simultaneous children, deadline and any scratch root.
Use disposable fixtures, never live run state. Count diagnostic and nested
launches in the budget. If timing, capacity or tool restrictions prevent a probe,
report it as untested or blocked rather than improvising a different experiment.

The parent owns scheduling and cleanup. Each child packet must specify its probe
purpose, allowed inputs, unique output or response token, read/write scope, tool
use, deadline and no-further-delegation rule. Only the nested probe coordinator
may launch its explicitly commissioned child. Do not give probe children the
whole parent conversation. No source downloads or substantive analyses belong
in these probes. Return visible runtime facts, not hidden reasoning or secrets.

### Layer 1 probes: worker isolation and round handling

- Launch one harmless child that returns a unique supplied token and explicitly
  exposed model, effort and depth settings, using `unknown` for unstated values.
  It must not inspect unrelated files, sessions, credentials or process environments.
- Check exact handoff-file delivery with an approved scratch fixture. Have the
  child report its cwd, the designated command executable and which supplied
  instruction files it received. A child claim alone is not proof of the
  runtime's instruction priority or actual model; retain runtime evidence too.
- For context exclusion, inspect the launch configuration or available child
  input trace. A synthetic parent-only marker can detect leakage, but failure
  to repeat the marker is not proof of isolation. Do not use real private data.
- Run an approved harmless long shell command in the prepared worktree (for
  example a script that sleeps past the harness's usual tool timeout and then
  writes a file) the way the analysis run would be started, and show the
  command's exit status and output were read after it ended. Do not invoke
  the production workflow for this probe.

### Layer 2 probes: nested coordination, rolling completion and refill

First launch a fresh coordinator whose only job is to launch one harmless
worker with its exact supplied packet and return the paired result. Report
observed depth and capacity, not a guessed ceiling. A direct worker probe from
the outer session does not establish this nested path.

Use a bounded fixture that lets the parent distinguish a short job from jobs
still alive. Prefer a supported hold/release mechanism with a deadline; short
bounded waits are acceptable when event evidence establishes overlap. Do not
leave indefinite sleep loops or unattended workers.

1. Start four independently identified jobs. Record each launch result and
   identity before awaiting completion.
2. Let one complete while at least one other remains demonstrably active. Read
   its terminal result without cancelling or waiting for the remaining jobs.
3. Start a fresh successor in the released slot. Show from ordered events that
   it started before a remaining original job terminated. Use a separate fresh
   successor as the analogue of an auditor; do not reuse the completed worker.
4. Finish or terminate all fixture jobs and confirm their terminal states.

This proves outer scheduling only. The nested path and layer-1 requirements
still need evidence inside delegated coordinators; R4 also needs capacity
evidence with descendants under outer load. Propose a separately budgeted
combined probe if the limits cannot otherwise be established. Do not report
four leaf workers as proof of four nested system pipelines.

### Failure and lifecycle

Within the approved budget, test a harmless failing command or invalid job
request and show how it reaches the parent without becoming a successful
workflow result. Check whether interrupting a wait also terminates workers;
report the actual semantics rather than requiring one universal behavior.

Test cancellation and termination acknowledgement with disposable work only.
A shutdown/reload probe requires a disposable parent session, explicit approval
and an external observer or retained evidence; never reload the active production
coordinator to test cleanup. Document descendant and platform limits. If a child
may still write after a crash, report that uncertainty and the required ownership
reconciliation before replacement. Do not kill processes owned by other sessions.

## Report and decision

Return the report in the conversation unless the operator supplied an authorized
report path. Keep exact evidence locators rather than dumping unrelated traces.
Use this shape:

```text
Harness/version/platform:
Loaded delegation surface and adapter/version:
Parent model/effort; requested and observed child model/effort:
Layer(s) assessed: one-analysis orchestration / outer rerun orchestration
Authorized probe budget; actual launches, peak concurrency, elapsed time/cost:

ID | verdict | operation/arguments | evidence locator | limit or repair
B1 | ...
...
R5 | ...

Layer 1 verdict: one-analysis orchestration
Layer 2 verdict: outer rerun orchestration (including delegated layer 1)
Exact launch, individual wait, cancellation and result-retrieval recipes:
Trust and worktree configuration required:
Instructions that must be carried in child packets:
Interruption/shutdown behavior; handles/results retained or lost:
Remaining live probe jobs and ownership, or confirmed none:
Blockers, untested properties and smallest next action:
```

Use verdicts `demonstrated`, `documented-only`, `unsupported`, `blocked` or
`untested`. A layer is ready only when its applicable requirements have adequate
runtime/configuration evidence and its critical live probes succeed. List any
remaining limits beside the verdict. A positive result applies only to the tested
configuration and does not authorize a production workflow, relax isolation or
release an existing run hold.

If a required capability is absent, return the exact blocker and the affected
layers. Adapter design or a weaker workflow needs a separate operator decision;
do not quietly substitute serial execution, full-history forks or shell-launched
agent processes for the commissioned behavior.
