# Pi subagent extension architecture review

## Status and conclusion

Retained at the operator's request from a conversational review of the project
Pi extension. This is an architectural assessment and a set of simplification
candidates, not an adopted redesign or authorization to change the extension.
It does not change the rerun commission, active assignments or recovery holds.

The core is reasonable; the interface around it is broader than the Commonplace
workflow appears to need. It is a process launcher with a small in-memory job
manager, not a workflow engine. Much of its size comes from supporting several
invocation styles and elaborate terminal displays.

Keep fresh-process isolation and lifecycle management. Investigate reducing the
supported execution modes and unifying job ownership. Removing cancellation
machinery would save the wrong complexity.

The review inspected the three implementation files, agent definitions,
operating instructions and tests at repository HEAD
`f29b54862908d81721016a53ea13e4eec0fc77c1`. The extension files had no reported
working-tree changes. Other files, including the workshop README, had unrelated
working-tree changes; the review used their working-tree contents. No real
workers were launched and no implementation files were changed.

## What happens when it launches a worker

```text
Parent Pi session
  |
  +-- subagent tool
       +-- reads an agent definition
       +-- selects model, thinking level and tools
       +-- starts a fresh Pi process
       +-- collects its JSON messages
       +-- returns its answer and execution details
```

The worker is another invocation of Pi, approximately:

```text
pi --mode json -p --no-session
   --model <selected model>
   --thinking <selected effort>
   --tools read,bash,edit,write
   --append-system-prompt <temporary agent-definition file>
   "Task: <handoff>"
```

This provides a fresh conversation, not a sandbox:

- The parent's conversation is not copied.
- The child still loads applicable repository instructions and resources.
- It inherits the process environment, including `PATH`.
- It can access the filesystem with the parent's operating-system permissions.
- Its conversation is not saved as an independent Pi session.

The parent collects messages, tool results, errors and usage information from
the child's JSON output. The final answer goes back into the parent's tool
result; more extensive execution details are retained alongside it.

This lets a workflow commission an independent reviewer or author without
passing along the coordinator's accumulated interpretations.

## Workers and coordinators are configurations

There are two project agent definitions:

| Role | Selected tools | Purpose |
|---|---|---|
| `commonplace-worker` | `read`, `bash`, `edit`, `write` | Execute one assigned job |
| `commonplace-coordinator` | The above plus `subagent` | Run a workflow that commissions its own workers |

Both use the same launcher.

A coordinator must explicitly read `.pi/APPEND_SYSTEM.md`, load its workflow
skill and run the worker-launch diagnostic. These are instructions to the model,
not a state machine enforced by the extension.

The extension makes delegation possible. Workflow instructions decide whether
delegation is authorized and what counts as successful work. The extension does
not validate a publication, enforce an audit gate, decide recovery or check a
worker's permitted write scope.

## Why asynchronous jobs were added

The copied Pi example supported three styles:

| Style | Behavior |
|---|---|
| Single | Launch one worker and wait |
| Parallel | Launch a batch, with up to four running, and wait for the entire batch |
| Chain | Run workers sequentially, optionally inserting the previous answer into the next prompt |

The rerun workflow needs different behavior:

```text
Start four system analyses.
When any one finishes, start its audit immediately.
When that audit is resolved, put another system in that slot.
Do not wait for the other three systems.
```

A batch call cannot provide this behavior because it returns only after the
entire batch finishes. The asynchronous interface therefore adds:

- `start`: launch one child and immediately return an identifier, called a handle.
- `wait`: return the first completed job among selected handles.
- `status`: inspect jobs.
- `cancel`: request termination.
- `forget`: discard a finished job's retained result.

This serves a current requirement, not a speculative one. The registry
implementing it is 87 lines in `.pi/extensions/subagent/jobs.ts`.

Interrupting `wait` stops waiting but leaves the children running. Cancelling a
job is a separate, explicit operation. Completed results remain repeatable until
forgotten; callers must remove completed handles from their pending set.

## What lifecycle management protects against

Once workers can outlive a tool call, somebody must own them. The extension:

- Limits asynchronous execution to four active jobs per session.
- Retains at most 128 handles.
- Keeps a cancelling job active until its process closes.
- Cancels asynchronous jobs on orderly shutdown, reload or session replacement.
- Sends TERM first, then escalates to KILL after five seconds.
- On POSIX, gives root launches a process group so cancellation can target
  descendants that remain in that group.

This prevents the parent from treating a slot as free and launching replacement
work while the old worker is still writing.

It is not a durable background-job service:

- Handles disappear when the session is replaced or restarted.
- An abrupt parent crash is not covered by orderly cleanup.
- Detached descendants are not covered by the process-group guarantee.
- Windows cancellation targets the direct child.
- Workflow recovery still requires examining retained files and ownership.

Preserve these explicit limitations rather than building persistence and
recovery into the extension without a demonstrated need.

## Simplification candidates

### Two execution systems coexist

There is a synchronous execution path for single, parallel and chain calls, and
a separate asynchronous job registry. They share the child launcher, but not
ownership and capacity accounting:

- Parallel mode has its own four-worker limit.
- Asynchronous mode separately has its own four-job limit.
- Synchronous launches do not enter the asynchronous registry.

Consequently, four is not a global limit. Operating instructions must warn
against combining modes to evade workflow capacity.

Nested coordinators each have their own limits. Four system coordinators can
therefore launch additional internal workers, as the rerun workflow intends.

Candidate: one internal job-ownership mechanism, even if a blocking convenience
call remains. This would reduce duplicated lifecycle reasoning without requiring
every caller to manage handles.

### Chain mode looks like inherited generality

Chain mode substitutes `{previous}` with the preceding worker's answer. This is
convenient for generic delegation, but Commonplace's controlled workflows already
define explicit handoffs and evidence boundaries. Automatically forwarding
answers can be inappropriate for independent reviews.

The review found no Markdown consumer of chain syntax in its scoped search of
`.pi`, `kb/instructions` and `kb/agentic-system-analyses/instructions`. This does
not prove it is unused everywhere.

Candidate: remove chain mode if a full consumer check confirms it has no required
use.

### A substantial amount is presentation code

The implementation totals 1,390 TypeScript lines at the inspected revision:

| File | Lines | Responsibility |
|---|---:|---|
| `index.ts` | 1,146 | Launching, dispatch modes, output collection and rendering |
| `agents.ts` | 157 | Agent discovery and configuration |
| `jobs.ts` | 87 | Asynchronous job ownership |

Terminal rendering methods occupy approximately 317 lines, with additional
formatting helpers earlier in the file. They provide expanded and collapsed
views, tool-call previews, usage displays and separate single, parallel and
chain layouts. This makes the file look more like a large scheduler than it is.

Candidate: one compact result display, or at least move presentation out of the
execution file. Moving it improves comprehensibility; deleting unnecessary
display variants reduces maintenance.

### The generic agent interface creates extra rules

The launcher supports:

- User agents, project agents or both.
- Project-over-user name precedence.
- Agent-pinned models.
- Parent model inheritance.
- Call-wide overrides.
- Per-item overrides.
- Special thinking-level inheritance when a model is pinned.

Commonplace's two shipped agents do not pin models. Its operating contract
always selects project scope.

These features may serve a general-purpose extension, but the product decision
should be explicit: are we maintaining a reusable generic subagent extension,
or a small Commonplace workflow adapter? The current implementation serves both,
which increases its configuration and documentation burden.

## Architectural edges

### Agent discovery uses the parent's directory

Definitions are discovered through `discoverAgents(ctx.cwd, ...)`, while the
child can launch with a different `cwd`. A coordinator launched into another
worktree can therefore receive an agent definition from the parent worktree
while loading repository resources from the destination. This may be
intentional, but it should be an explicit contract.

### The output cap does not bound retained memory

Parallel and asynchronous summaries are truncated, but full child messages and
stderr remain retained. The 128-handle limit limits job count, not result size.
Nested coordinators can embed worker details in their own results.

### Malformed tool configuration can fall back to default selection

An empty or unrecognized tool-list value becomes `undefined`, causing the
launcher to omit `--tools`. The shipped definitions are valid. For a
workflow-specific adapter, rejecting malformed definitions would be easier to
reason about than silently falling back.

### The loaded runtime can lag behind the files

At review time, the reviewing session's exposed `subagent` schema supported
single, parallel and chain modes but had no `action` or `handles`. The on-disk
implementation had asynchronous operations. This was an observation about that
session, not a permanent runtime blocker.

Editing the extension does not update an already-loaded tool schema. Reload is
required before using the new interface, not during active work.

## Recommended direction

The job manager is not the overengineered part. The excess is mostly the generic
example's interface and presentation features, plus maintaining two execution
paths.

A smaller target architecture would be:

```text
Workflow instructions and Commonplace commands
  Own handoffs, evidence, audits, recovery and scheduling decisions
                         |
                         v
Pi extension
  One child launcher
  One session-local job owner
  Small start/wait/status/cancel/result interface
                         |
                         v
Fresh Pi processes
```

Review simplification in this order:

1. Confirm whether chain mode has any real consumer.
2. Decide whether generic user-agent discovery and configuration are required.
3. Unify process ownership across blocking and asynchronous calls.
4. Simplify terminal rendering.
5. Keep cancellation, fresh contexts and separation from workflow state.

These are proposals awaiting a separate implementation decision, not changes to
the current rerun procedure.

## Technical basis and verification

Repository evidence inspected:

- [Extension implementation](../../../.pi/extensions/subagent/index.ts):
  `runSingleAgent`, dispatch branches, session hooks and renderers.
- [Job registry](../../../.pi/extensions/subagent/jobs.ts): ownership, capacity,
  waiting, cancellation and shutdown.
- [Agent discovery](../../../.pi/extensions/subagent/agents.ts): lookup scope and
  configuration parsing.
- [Worker definition](../../../.pi/agents/commonplace-worker.md) and
  [coordinator definition](../../../.pi/agents/commonplace-coordinator.md).
- [Pi operating documentation](../../../.pi/README.md) and the
  [rerun commission](./README.md).
- [Asynchronous lifecycle tests](../../../.pi/extensions/subagent/tests/async.test.mjs)
  and [launch override tests](../../../.pi/extensions/subagent/tests/launch-overrides.test.mjs).

The review ran:

```bash
PI_PACKAGE_DIR=/home/zby/.pi/agent/install/releases/1.1.0/node_modules/@earendil-works/pi-coding-agent \
  node --test .pi/extensions/subagent/tests/*.test.mjs
```

Result: both test files passed, with 22 subtests plus their two parent tests
reported as 24 passing tests and zero failures. These tests check argument
construction and simulated lifecycle behavior. They do not establish
real-process cancellation, resource inheritance or end-to-end nested workflow
correctness.
