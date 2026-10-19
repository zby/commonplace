---
description: "Use when checking whether a harness can run one Commonplace analysis: a session that runs the analysis skill, and the headless worker launches that commonplace-analysis run performs"
type: types/instruction.md
---

# Check a subagent harness

Determine whether a harness can run one Commonplace analysis, with exact
launch recipes, tested limits and explicit blockers for an operator's adoption
decision.

## Consumption and scope

An operator gives this document to an agent running inside the harness being
assessed. It is a requirements checklist and bounded check procedure, not a
claim that any harness already meets the requirements. Use the actual loaded
tools and runtime settings, not a remembered product feature list. Report the
harness version, configuration and account restrictions that bound the result.

This instruction authorizes inspection and a report in the conversation. It does
not authorize production workers, workflow recovery, installation, configuration
changes or an adapter implementation. Live diagnostic launches require explicit
operator approval. If launch authority or tools are missing, return the
inspection result; do not acquire tools as a substitute.

### What is assessed

An analysis runs as one `commonplace-analysis run` process in its prepared
isolated worktree
([ADR 118](../reference/adr/118-analyses-run-as-a-workflow-over-headless-harnesses.md)).
The check covers two parts of that path:

- **The operator's session.** A harness session runs the analysis skill,
  `kb/agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md`:
  it runs `prepare`, starts `run`, waits for it to exit, reads `inspect`, and
  runs `integrate` after operator authorization. It launches no workers. It
  does not select jobs, judge outputs, invent retries or bypass stops.
- **The worker launches.** The workflow process launches each role's worker
  as a fresh headless session of the worker profile's harness (`claude -p`,
  `codex exec` or `pi -p`), in the prepared worktree, with a timeout. Code
  composes each prompt and checks each result.

The harness under assessment may serve as either part or both. Report each
part separately; the operator's session can pass while the harness's headless
mode is unsupported as a worker profile.

## Requirements

Map each requirement to an exact native operation, command-line flag or
already installed adapter. Separate runtime-enforced properties from
instructions the model must obey.

| ID | Applies to | Required behavior and evidence |
|---|---|---|
| B1 | Worker launch | Start a genuinely fresh conversation without parent turns, summaries, prior answers or automatic answer forwarding. Shared repository rules are allowed and must be identified. A request to “ignore history” is not isolation. |
| B2 | Worker launch | Deliver the exact prompt the workflow composed, including its absolute instruction and input paths. The worker can read the complete files and recover truncated reads. |
| B3 | Worker launch | Deliver applicable standing instructions and job contracts with known authority. Identify what the headless mode loads automatically in the worktree (project instructions, skills, settings, extensions), what the worker must read explicitly, and what is absent. |
| B4 | Worker launch | Provide the job's needed file and command tools. Select the requested model and reasoning effort through supported flags. Report the model the harness itself records for the launch, separately from the requested one; never infer execution identity from a role name or successful reply. Unknown required settings block model-specific work. |
| B5 | Both | Execute in the prepared worktree with its code, command environment and resources. A worker must not silently use the origin checkout's definitions or the shared editable installation. Identify cwd, executable resolution and configuration origins. |
| B6 | Worker launch | Return an individually attributable result or failure: exit status, final answer, stderr and a session identifier that locates the harness's own record. Surface truncation and a usage-limit failure distinctly. A process exiting normally does not mean its job succeeded. |
| B7 | Worker launch | Stop writing when the workflow's timeout or interruption ends the launch. Explain how termination reaches descendants and what remains uncertain after a crash. |
| B8 | Both | Preserve the commissioned write scope and evidence boundary. State whether these are instructions or sandbox enforcement. Fresh conversation isolation is not filesystem isolation; shared filesystem access must not be described as a sandbox. |
| A1 | Operator's session | Run `commonplace-analysis run` in the prepared worktree as one shell command lasting hours, without the harness ending it, and read its exit status and output when it ends. State the harness's command timeout and how a command outlives a tool call (a background process whose exit is awaited, a terminal the operator keeps open). |
| A2 | Both | Let the workers run unattended: the operator's harness must not prompt for, throttle or kill the child processes, and the worker harness's headless mode must not wait for an approval nobody answers. Resolve trust and permissions for the prepared worktree before the run, without disabling trust globally or treating the analysed source repository as trusted agent configuration. |

The workflow owns scheduling, acceptance, publication and recovery. The
harness supplies execution only. Neither a transport success nor a worker's
self-reported completion substitutes for the workflow's checks.

These are behavioral requirements, not demands for one harness's
implementation. Persistent sessions, automatic retry and resuming the same
worker are not prerequisites. Describe their presence or absence only where it
changes execution or recovery. Do not retry failed probes automatically.

## Inspection first

1. Identify the loaded harness and its headless mode's documented flags. Read
   relevant local runtime documentation if available. Distinguish an installed
   implementation from operations exposed to this session.
2. Map the requirements to actual arguments and result fields. For every gap,
   identify whether it is a missing capability, missing permission, unsupported
   model, configuration problem, or untested behavior. Preserve exact errors.
3. Identify which properties require live evidence. If probes are not authorized,
   stop with a provisional report and the smallest proposed probe budget. Do not
   claim a pass from inspection alone.

## Bounded live probes

Before probing, obtain approval for the model/effort settings, maximum
launches, deadline and any scratch root. Use disposable fixtures, never live
run state. If timing or tool restrictions prevent a probe, report it as
untested or blocked rather than improvising a different experiment.

Each probe prompt must specify its purpose, allowed inputs, unique response
token, read/write scope, tool use and a no-delegation rule. No source downloads
or substantive analyses belong in these probes. Return visible runtime facts,
not hidden reasoning or secrets.

- Launch one harmless headless worker in a prepared worktree that returns a
  unique supplied token and its exposed model, effort and cwd, using `unknown`
  for unstated values. It must not inspect unrelated files, sessions,
  credentials or process environments. Compare the reported model with the
  one the harness recorded.
- Check exact prompt-file delivery with an approved scratch fixture. Have the
  worker report the designated command executable and which instruction files
  it received. A worker's claim alone is not proof of instruction priority or
  actual model; retain runtime evidence too.
- For context exclusion, inspect the launch command and the harness's session
  record. A synthetic parent-only marker can detect leakage, but failure to
  repeat the marker is not proof of isolation. Do not use real private data.
- Test a harmless failing job and a launch that exceeds a short timeout, and
  show how each reaches the caller without becoming a successful result.
- In the operator's session, run an approved harmless long shell command in
  the prepared worktree (for example a script that sleeps past the harness's
  usual tool timeout and then writes a file) the way the analysis run would be
  started, and show the command's exit status and output were read after it
  ended. Do not invoke the production workflow for this probe.

Do not kill processes owned by other sessions.

## Report and decision

Return the report in the conversation unless the operator supplied an authorized
report path. Keep exact evidence locators rather than dumping unrelated traces.
Use this shape:

```text
Harness/version/platform:
Headless mode and flags assessed:
Requested and recorded worker model/effort:
Authorized probe budget; actual launches, elapsed time/cost:

ID | verdict | operation/arguments | evidence locator | limit or repair
B1 | ...
...
A2 | ...

Operator's session verdict:
Worker launch verdict (as a worker profile):
Exact launch command and profile entry:
Trust, permission and worktree configuration required:
Interruption and timeout behavior:
Remaining live probe processes and ownership, or confirmed none:
Blockers, untested properties and smallest next action:
```

Use verdicts `demonstrated`, `documented-only`, `unsupported`, `blocked` or
`untested`. A part is ready only when its applicable requirements have adequate
runtime or configuration evidence and its live probes succeed. List any
remaining limits beside the verdict. A positive result applies only to the
tested configuration and does not authorize a production run or relax
isolation.

If a required capability is absent, return the exact blocker and the affected
part. An adapter or a weaker workflow needs a separate operator decision; do
not quietly substitute full-history sessions or interactive approval for the
commissioned behavior.
