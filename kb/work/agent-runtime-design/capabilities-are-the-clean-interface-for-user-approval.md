# Capabilities Are the Clean Interface for User Approval

## Working thesis

User approval is a decision about **authority to cause an effect**, not a property of a tool. A tool call is only the occasion on which the question becomes concrete. The clean interface is therefore:

1. a tool or runtime describes the effect a call requires as a scoped capability request;
2. runtime policy compares that request with the authority already granted to this run;
3. a runtime client asks the user only when policy cannot resolve the request;
4. the runtime enforces the resulting grant or denial at the effect boundary.

This separates the agent runtime from its clients. The runtime executes calls, owns run state, and mediates effects. A runtime client starts, observes, steers, interrupts, or authorizes the runtime on behalf of a person or application. “Interface” here means an interaction protocol, not only a graphical surface. A TUI prompt, a CLI `--approve-all` flag, a policy file selected by the user, and an API callback can all be client surfaces.

Approval is the forcing case that prevents a runtime client from being a passive renderer. The runtime can emit ordinary events in one direction, but approval requires a return channel: the dependent effect remains unexecuted, the client presents a pending decision, and the user's answer resumes or reconstructs the dependent work. A runtime may await the answer inside one live invocation, or end that invocation with typed pending work and accept the answer in a correlated later invocation. The wait may outlive the client or agent process. Approval is therefore both part of the runtime-client control protocol and, where long-lived work is claimed, a test of durable pending-work re-entry.

## Two capability sets

The word “capability” is used too loosely unless two sets are separated. Some libraries also use it for composable hooks or behavior wrappers; that source label does not imply authority unless construction and enforcement establish grant semantics.

The **capability surface** is the action alphabet exposed to an agent call. It is part of the minimal technical agent convention: prompt, capability surface, and stop condition. Giving one child `{search, summarize}` and another `{read_file, patch_file, run_test}` constructs different agents because the calls can attempt different actions. [Subtasks that need different tools force loop exposure](../../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent.md) for exactly this reason.

The **grant set** is the subset of effects this principal may execute under the current policy and environment. A tool can remain visible while a particular call requires approval; alternatively, a headless runner can hide capabilities it knows it will deny so the model does not waste calls on impossible actions. Exposure and authorization are related but not identical.

The distinction gives a precise approval flow:

```text
agent sees capability surface
           |
           v
agent proposes a tool call
           |
           v
runtime derives a scoped capability request
           |
           v
policy: existing grant?  deny rule?  unresolved?
           |                 |             |
         execute           reject          v
                                       client asks user
                                             |
                                   grant / deny / narrow
                                             |
                                             v
                                      runtime enforces
```

The client does not need to understand every tool implementation. It needs a stable description of the requested effect, enough context for a human decision, and a control channel that returns the decision. The runtime does not need to render a prompt. It needs to derive requests faithfully, resolve policy, keep or emit the blocked dependency with enough state for its claimed re-entry horizon, and enforce the result.

## A capability request and a grant

A bare label such as `fs.write` is useful for grouping, but insufficient for a real decision. A request needs at least:

- **principal** — the run, agent, worker, or delegation path asking;
- **effect class** — for example `fs.write`, `fs.delete`, `net.egress`, `proc.exec`, `secret.read`, or `agent.spawn`;
- **target scope** — the path, host, command class, secret name, agent type, or other affected resource;
- **operation details** — the concrete arguments or a safe summary of them;
- **limits** — count, bytes, money, time, concurrency, or another bounded quantity where relevant;
- **provenance** — which tool and call produced the request, and what task it serves.

A grant adds:

- **decision source** — configured policy, live user decision, or inherited/derived grant;
- **lifetime** — one call, one task, one session, one project, or persistent until revoked;
- **constraints** — a narrowed scope or budget;
- **identity** — enough stable state to audit, revoke, and avoid applying a stale decision to a different request.

This turns the familiar `yes / no / always` prompt into a small policy editor:

- **yes** — grant this request once;
- **no** — deny this request once, possibly with guidance the agent can use;
- **always** — grant a stated capability and scope for a stated lifetime;
- **narrow** — permit a smaller path, host, command, amount, or duration than requested;
- **deny by rule** — prevent repeated prompts for a capability the user will not grant.

The user should not have to read raw identifiers to make the decision. `fs.write` is useful to policy code; the client should say what will change, where, which agent requested it, and how long the proposed grant lasts.

## Why capabilities are cleaner than tool approvals

### Tool identity is the wrong stable unit

Different tools can cause the same effect. A patch tool, file-write tool, shell command, and generated script may all write the workspace. Attaching independent approval rules to each lets equivalent authority travel through whichever tool has the weakest policy.

The reverse also occurs: one tool can cause different effects. A shell tool can inspect local state, overwrite files, start processes, reach the network, or combine all four. Treating “shell” as one approval unit is either too permissive or constantly noisy. A runtime may inspect a concrete command to derive a narrower request, but if it cannot establish the effect reliably it must request the broad capability.

Capabilities let implementation change without changing the user's authority policy. Replacing one filesystem tool with another should not require reconstructing every approval decision.

### Description and decision have different owners

The component closest to the effect knows what the operation can do. The runtime knows the environment, current principal, existing grants, isolation envelope, and user-selected policy. The client knows how to present an unresolved choice and collect an answer.

Combining these roles inside every tool creates inconsistent precedence: a tool decides it needs approval, a global mode says approve, an agent override says deny, and a wrapper tries to reconcile them. Capability requests make tools report facts and leave one policy engine to decide.

### Interactive and headless execution become policy variants

An interactive client resolves `prompt` through the user. A headless runner supplies a complete policy before execution: allow, deny, or constrain each relevant capability. Both use the same runtime request and enforcement path. Headless execution is not “approval turned off”; it is approval decisions supplied without a live human round trip.

### Scoped grants reduce prompt fatigue without hiding authority

Repeated per-call prompts train users to approve reflexively. A capability grant can express the intended trust directly: allow writes under this worktree for this task, allow network access only to this host, or allow at most three workers. The rule is inspectable and revocable. A client can show the current grant set instead of making the user remember what “always” meant several prompts ago.

## The capability possibility space

Capabilities do not merely replace boolean prompts. They expose a design space for runtime authorization:

| Axis | Possibilities | Consequence |
|---|---|---|
| Request time | Declared before run, derived per call, composite preflight, escalation during execution | Determines whether the user approves a plan, individual effects, or both |
| Decision | Allow, prompt, deny, narrow | Avoids treating “not preapproved” and “forbidden” as the same state |
| Granularity | Tool, effect class, resource scope, concrete instance | Trades policy reuse against decision precision |
| Lifetime | Call, task, session, project, persistent | Determines prompt rate and stale-authority risk |
| Principal | Run, agent, role, delegation path, human identity | Determines who actually receives the authority |
| Delegation | No inheritance, attenuated subset, explicit propagation, shared budget | Controls whether a child silently expands the parent's authority |
| Environment | Host, workspace sandbox, container, remote executor | Sets the maximum effect a grant can authorize |
| Revocation | Not supported, future-only, cancellation plus future denial | Determines whether the user can withdraw authority from live work |
| Interaction | Live prompt, policy profile, API callback, organizational policy | Lets one runtime serve TUI, CLI, automation, and service clients |

This matrix is a better starting point for runtime comparison than a list of permission modes. A mode such as `accept edits` or `full access` is one packaged point in the matrix. The comparison should unpack what it grants, to whom, over which scope, for how long, and through which environment boundary.

## Approval turns UI into run control

Once work can remain pending for approval, the runtime-client protocol needs more than event rendering:

- stable request ids so a response cannot authorize the wrong call;
- pending-request state that survives UI redraws and, where claimed, reconnects;
- cancellation and timeout semantics;
- idempotent responses so retries do not execute an effect twice;
- concurrency rules for several pending requests;
- invalidation when the call, arguments, principal, or grant context changes;
- safe summaries and redaction for arguments shown to the user;
- a record of the decision and its lifetime;
- a denial result the agent can interpret without pretending the tool failed accidentally.

This explains why user approval complicates otherwise simple runtime clients. A one-way event stream is enough to watch a run. Approval makes the user a participant in the scheduler or outer lifecycle: a later transition depends on an external authority decision. A serious runtime or host must decide whether pending approvals are ephemeral client state, a live continuation, or typed durable work; what survives disconnect or process loss; and how re-entry avoids repeating the guarded effect.

The [recursive-agent architecture ingest](../../sources/jdegoes-recursive-agent-architecture-2081854216264392934.ingest.md) makes this structural demand explicit: a plan awaiting human approval may need to remain pending for hours or days without consuming resources or losing its place. Once the eventual answer releases an irreversible effect, durable deferral, idempotency or exactly-once semantics, and recovery are part of the authorization design rather than optional distributed-systems polish. The article argues for a particular durable execution substrate and should not be treated as empirical proof that every runtime needs its full machinery, but its approval case is a useful requirements test. The [PydanticAI boundary pilot](./pydantic-ai-dspy-code-grounded-boundary-pilot.md) demonstrates another valid shape: one agent run ends with typed pending requests and a later run re-enters through correlated history and results.

## Delegation requires attenuation, not ambient inheritance

Approval becomes harder under sub-agents because “the user approved the parent” is ambiguous. It might mean the parent may delegate judgment; it does not automatically mean every child may exercise every effect the parent could request.

The clean default is attenuation:

- a child receives an explicit subset of the parent's capability surface;
- grants are scoped to a principal or delegation path rather than placed in one ambient session bag;
- a child that needs more authority produces a new request attributable to that child and its parent task;
- composite work can receive an approved capability budget, but exceeding it requires another decision.

This is also where primitive and aggregate authority diverge. A loop that permits one file edit may permit a thousand edits when compiled into unattended coordination. [Compiling coordination preserves primitive authority but expands aggregate authority](../../notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md), so useful grants sometimes need volume, cost, or duration bounds in addition to effect scope.

Untrusted-content roles need a stronger boundary. If a worker reads attacker-controlled input, per-call approval does not establish whether that input manipulated its judgment. [Privilege quarantine](../../notes/orchestration-needs-privilege-quarantine-not-permission-scope.md) removes high-authority capabilities from that role entirely and gives a separate actor only vetted structured output. Capability policy expresses that split cleanly, but a live prompt cannot replace it.

## Approval is not the security boundary

The clean capability model should not be mistaken for object-capability security. String labels such as `fs.write` are descriptions unless they are backed by unforgeable references and complete enforcement. A buggy or malicious tool can under-declare its effects. An LLM can be manipulated into requesting a dangerous but apparently legitimate operation. A user can approve without understanding the consequences.

The execution environment therefore sets an outer authority ceiling. A container without network access cannot gain network access because a UI says yes. A read-only mount cannot become writable through an approval grant. Secrets absent from the executor cannot be exposed by a mislabeled tool. Approval chooses within the envelope; isolation creates the envelope.

For the descriptive capability layer to remain trustworthy:

- every effectful path must pass through an enforcement point;
- tools must not be able to bypass the runtime through another execution channel;
- capability declarations need tests against actual effects;
- broad or opaque tools must declare broad authority;
- denial and scope checks must happen at execution time, not only when tools are advertised;
- privilege quarantine must remain available where provenance-sensitive judgment defeats argument-level checks.

Capabilities are the cleanest solution to user approval because they expose authority explicitly. They are not a substitute for sandboxing, least privilege, or evaluation of whether the requested action is wise.

## What belongs to the runtime and what belongs to its clients

The split suggested by this model is:

| Runtime | Runtime client or interface |
|---|---|
| Define or register the capability vocabulary | Render capability requests in task language |
| Derive a request from a concrete call | Show principal, target, effect, scope, and lifetime |
| Maintain principals, grants, limits, and policy state | Let the user allow, deny, narrow, remember, revoke, or cancel |
| Suspend and resume execution safely | Maintain interaction with pending decisions |
| Enforce grants at every effect boundary | Expose current policy and grant state |
| Emit events and structured denial results | Present progress, consequences, and audit history |
| Enforce isolation ceilings | Avoid presenting an impossible grant as effective |

The exact process boundary can vary. An embedded runtime may accept a callback supplied by application code; a local CLI may place runtime and client in one process; a remote service may separate them by a bidirectional protocol. The conceptual split still helps because the two sides have different contracts and failure modes.

## What the `llm-do` case contributes

The local `llm-do` design work independently reached the important pieces:

- approvals catch mistakes and provide visibility; isolation handles active attacks;
- tools should declare capabilities while runtime policy decides;
- scoped preapproval is a rule over operation and target, not a remembered tool name;
- a decoupled UI needs a return channel and pending-request identity;
- headless and interactive modes are different policy resolutions over one execution path.

Its current implementation also shows why the abstraction is not free. Filesystem and shell toolsets report capability sets, but approval still runs mainly through tool-local `needs_approval()` methods, per-tool configuration, runtime overrides, and wrapper layers. The target vocabulary exists beside the older decision machinery rather than replacing it. That is a useful warning for Commonplace: adding capability labels does not create the separation. The labels must become the authoritative input to one policy and enforcement path.

This workshop should borrow the decomposition, not the exact taxonomy. `fs.write` and `proc.exec` are plausible early values; a comparison methodology must first discover which distinctions recur across real runtimes and change user decisions.

## Limits of the thesis

Capabilities organize user authority. They do not explain the whole runtime.

A runtime still needs scheduling, context assembly, effect execution, durable state, delegation, recovery, and observation. Its clients still need progress and error presentation, task and conversation controls, context and provenance views, cancellation, output handling, and perhaps run comparison or replay. These properties cannot be reduced to grants: compaction faithfulness, retry correctness, recovery semantics, or evaluation quality are not capabilities a user approves.

The narrower claim is strong enough:

> Capability requests and scoped grants are the clean interface for every point where an agent runtime needs user authority to proceed.

That claim can organize the approval part of the workshop without forcing the entire runtime or its interfaces into one capability taxonomy.

## Open questions

- What is the smallest effect taxonomy that remains stable across tools and runtimes?
- Should tools declare effects, should the runtime infer them from arguments, or must both agree?
- Which reads deserve approval because their real effect is privacy exposure or secret access?
- Can dynamic or composite tools preflight their whole capability budget, or must they escalate incrementally?
- How should a grant name a delegation path when workers are created dynamically?
- What revocation semantics are possible once a side effect or long-running process has begun?
- When does changing the grant set require a fresh context because the old context still contains removed affordances?
- Which grants may persist across sessions, and what evidence makes their continued scope trustworthy?
- How should remote and multi-user runtime clients authenticate the human principal returning a decision?
- What behavioral probes can verify that a runtime's declared capability request matches the effect it actually performs?

## Local source basis

This analysis was prompted by first-hand reading of the sibling `llm-do` checkout, especially:

- `kb/notes/approvals-index.md`
- `kb/notes/approvals-guard-against-llm-mistakes-not-active-attacks.md`
- `kb/notes/capability-based-approvals.md`
- `kb/notes/preapproved-capability-scopes.md`
- `kb/notes/ui-event-stream-blocking-approvals.md`
- `kb/notes/execution-modes-user-stories.md`
- `kb/notes/adr/005-runner-harness-vs-clai.md`
- `kb/notes/adr/006-runtime-core-vs-simpler-runtime.md`
- `docs/architecture.md`, `docs/ui.md`, and the current approval, filesystem, shell, and UI implementation

The `llm-do` working tree was read in place and was not modified. The claims above are Commonplace's working synthesis, not an assertion that every `llm-do` proposal is implemented.
