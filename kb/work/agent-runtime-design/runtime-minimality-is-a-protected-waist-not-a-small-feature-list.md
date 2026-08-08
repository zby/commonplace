# Runtime Minimality Is a Protected Waist, Not a Small Feature List

## Working thesis

An agent runtime should be minimal in the number of **semantic commitments it fixes**, not in the number of functions it implements. A runtime may need substantial machinery for suspension, isolation, identity, capability enforcement, and recovery. Those mechanisms still form a minimal core when every execution strategy above them can vary.

The boundary test is:

> A responsibility belongs in the protected runtime when an extension cannot implement it without gaining the ability to bypass it, corrupt shared execution state, or break guarantees across suspension and recovery. Everything else should remain replaceable strategy.

This gives the runtime a protected waist and an open execution plane. The protected waist enforces invariants. The execution plane lets human-written or model-written programs choose decompositions, perform symbolic work, and compose bounded inference calls dynamically.

The result is not a runtime that contains every useful feature. It is a runtime that can host features without silently turning each one into an ambient privilege or a new, incompatible control loop.

## Mechanism and policy must be separated inside the runtime decomposition

The existing decomposition into [scheduler, context engine, and execution substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md) is still useful, but each component contains both mechanism and policy.

| Component | Protected mechanism | Extensible policy |
|---|---|---|
| Scheduler | Run and call identity, ready/waiting/completed state, suspension, cancellation, fork/join mechanics, continuation recovery | Decomposition, topology, ordering, aggregation, retry strategy, stopping heuristics |
| Context engine | Bounded call envelope, provenance channels, scope boundaries, context-size enforcement | Retrieval, compaction, source selection, prompt construction, projection into child calls |
| Execution substrate | Capability enforcement, isolation ceiling, effect interception, durable state primitives, resource accounting | Tool implementations, data transforms, domain integrations, task-local programs |

This split changes what it means to say that the scheduler “owns decomposition.” The runtime owns the machinery that can execute and recover a decomposition. It should not need to own the decomposition policy. [Agent orchestration occupies a multi-dimensional design space](../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) already separates scheduler placement from the artifact that carries decomposition policy. A model-authored symbolic program can carry that policy while the runtime supplies the scheduling mechanism beneath it.

The same distinction applies elsewhere. The runtime must enforce a context boundary, but it need not choose one universal retrieval algorithm. It must intercept effects, but it need not ship every tool. It must recover a suspended call, but it need not decide that every failure deserves three retries.

## The runtime must be dynamically extensible by model-authored code

If the model is allowed to choose a decomposition, natural language is not always the right form for the chosen result. A decomposition may contain exact loops, filters, joins, counters, dependency edges, or validation steps. Forcing those parts back into conversation makes the model perform symbolic bookkeeping in bounded stochastic context.

[RLM has the model write ephemeral orchestrators](../../notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) shows the clean move: the model writes the scheduler rather than remaining the scheduler. [Claude Code dynamic workflows](../../agentic-systems/claude-code-dynamic-workflows.md) shows a shipped variant: the model writes an isolated JavaScript program that calls bounded agents, holds intermediate values outside the parent context, and can later be promoted as a reusable command. The recent [recursive-agent architecture ingest](../../sources/jdegoes-recursive-agent-architecture-2081854216264392934.ingest.md) generalizes the same shape into recursive code–inference execution.

For the general-purpose runtime we want, dynamic extension therefore means more than registering another prewritten tool. During a run, the model must be able to create a task-local symbolic program that can:

- perform ordinary deterministic computation over task data;
- define local functions and intermediate representations;
- invoke bounded model or agent calls with explicit context and capability surfaces;
- fan out, join, branch, loop, and aggregate;
- call already granted tools and execution services;
- suspend when an invoked effect needs approval or an external result;
- return a typed result or artifact to its caller.

The runtime supplies the execution semantics. The model supplies the program. This is the dynamic counterpart of [the practical scheduler is the host language](../../notes/the-practical-scheduler-is-the-host-language.md): ordinary code should carry `select` and live state when it can, while the runtime reifies the continuation when process lifetime, human approval, or distribution makes live call-stack state insufficient.

## Dynamic extension must not mean ambient mutation

Model-authored code should enter as a **guest program**, not as a patch to the protected runtime. The default lifetime should be the current run or task. The program receives explicit handles to the capabilities it may use. It cannot mint authority, replace enforcement, read runtime secrets, or install itself globally merely because it can execute code.

The runtime needs at least these boundaries around generated programs:

- **Explicit authority** — capabilities are passed into the program and may be attenuated for child calls. New authority requires a capability request.
- **Isolation** — guest code executes inside an environment ceiling that approval cannot expand.
- **Namespace scope** — generated functions and callables are local to the run unless separately admitted. They do not pollute a global registry by default.
- **Provenance** — the runtime records the source program, authoring call, model, input identity, version or content hash, and invoked effects.
- **Resource bounds** — time, memory, model calls, concurrency, money, output size, and recursion depth can be limited.
- **Typed boundaries** — calls and returns can be validated even when the program body remains dynamically generated.
- **Lifecycle** — cancellation, suspension, failure, cleanup, and resumption have defined semantics.

This is the same logic as capability-based approval. Generated code may choose *how* to use the authority it has, but it cannot decide whether it possesses that authority. The policy and enforcement path remain outside the generated program.

## Extension horizon and authorship should not be collapsed

“Extensible” hides several different authority, authorship, target, and persistence choices.

| Extension horizon | Typical author | Lifetime | Admission rule |
|---|---|---|---|
| Call-local computation | Model or host | One bounded call or guest-program step | Execute inside the current capability envelope |
| Run-local control program | Model or host | One task or run | Register in a run-local namespace; journal if needed for recovery |
| Durable project capability | Model, builder, or human | Cross-session | Test, review, version, and explicitly admit; support rollback and retirement |
| Runtime or policy extension | Runtime maintainer, builder, or model | Deployment lifetime | Trusted installation outside ordinary run authority |

The first two are dynamic execution. The third is deploy-time learning or capability promotion. The fourth changes the protected substrate itself. A system may support all four, but it should never let a run-local program cross into the later horizons implicitly.

The horizon table alone does not identify self-modification. A human-written plugin can be durable without being self-generated. An RLM program can be self-generated without surviving the run. For this workshop, runtime self-modification needs both properties: a process inside the declared system boundary generates the concrete change, and the accepted change remains operative for later runs or sessions. It must also target the runtime's own [behavior-determining organization](../../notes/definitions/behavior-determining-organization.md) rather than merely produce an external work product.

| Case | Self-generated | Durable beyond generating run | Target | Classification |
|---|---|---|---|---|
| RLM task program | Yes | No | Current task's orchestration | Dynamic execution, not self-modification |
| Ordinary hand-written llm-do agent or tool | No | Yes | Durable callable namespace | Runtime extension, not self-modification |
| Tendril generated capability | Yes | Yes | Workspace capability surface | Durable self-extension; whether it is runtime self-modification depends on the declared system boundary |
| Exo agent rewrite of its executor | Yes | Yes | Runtime executor and capability machinery | Runtime self-modification |

Generation and admission remain separate. A user may review or approve a model-generated change without becoming its author, while a runtime may automatically install a generated artifact without showing that the change deserved retention. **Self-modifying** describes the origin, persistence, and target of the change; it does not imply autonomous admission, improvement, or adequate verification.

[RLM, Tendril, and llm-do place symbolic work at different persistence boundaries](../../notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md) already shows why these horizons matter. Ephemeral orchestration avoids maintenance and admission costs. Durable generated capabilities accumulate value but introduce provenance, testing, permission, dependency, and retirement obligations.

## Approval clarifies the asynchronous execution model

A generated program may invoke a capability that needs user authority. The runtime should defer the effect and every continuation that depends on its result. It may keep a live continuation, or end the current invocation with typed pending work and re-enter it through a later correlated invocation. It should not require unrelated branches, other runs, the UI, or the runtime process to remain blocked.

This requires the protected scheduler or lifecycle boundary to retain or externalize:

- the identity and arguments of the pending invocation;
- the principal and capability scope being requested;
- the continuation that consumes the result, or enough state and history to reconstruct its legal re-entry;
- the current guest-program version and relevant state;
- cancellation, timeout, invalidation, and duplicate-response rules.

On approval, the runtime resumes the invocation or starts a correlated successor under the granted scope and returns its real result. On denial, it returns a structured denial result and lets the symbolic program or model choose another path. The causal dependency is synchronous; the runtime operation is asynchronous and may be durable.

This is why deferral and continuation semantics belong below extensions. A model-written program cannot reliably preserve or reconstruct its own continuation across process loss unless the runtime supplies a resumable execution model or compiles the continuation into protected external state.

## A small waist is an interface, not a tiny implementation

It is too early to freeze an exact API, but the waist must make a small set of operations composable:

- invoke bounded inference with an explicit input, context projection, capability surface, and stop condition;
- invoke a symbolic capability through the same identity, policy, event, and result path;
- create or execute a run-local symbolic program;
- spawn, join, suspend, resume, and cancel addressable work;
- read and write explicit run state or artifacts through scoped capabilities;
- observe structured events and failures.

These may collapse into fewer primitives. For example, agents, tools, and generated programs may share one typed invocation protocol. The important requirement is semantic closure: model-authored code should be able to compose the public primitives into new decompositions without reaching into private runtime internals.

Minimality is then judged by questions such as:

- Does the core fix a decomposition strategy that could have been an extension?
- Can generated code bypass an invariant because enforcement lives in a wrapper rather than the common invocation path?
- Does adding a new capability require changing the scheduler?
- Can a run-local extension be promoted without changing its calling convention?
- Can the runtime suspend any composed invocation, or only built-in tool calls?
- Which pieces remain trustworthy when every task-level strategy is model-authored?

## Candidate requirement

The current candidate is:

> A general-purpose agent runtime must provide a capability-bounded symbolic execution plane in which the model can author task-local control programs over bounded inference and tool calls, while the runtime retains authority, identity, suspension, recovery, resource, and observability invariants beneath those programs.

This is stronger than saying the runtime supports plugins. It requires online authorship, run-local scope, recursive composition, and one enforcement path across prewritten and generated execution.

## Questions to test next

- Must guest programs use a restricted language, or can capability isolation make ordinary Python, JavaScript, or another host language acceptable?
- What minimum operations let generated code express decomposition without exposing runtime internals?
- Which guest-program state must be journaled to support approval, process loss, and distributed execution?
- Can the same invocation protocol cover a tool, agent, generated function, and durable workflow without erasing their different lifecycle semantics?
- What should execute before a batch of capability requests is resolved: independent pre-approved calls, nothing from that model turn, or a policy-selected subset?
- What evidence is sufficient to promote a run-local program into a durable project capability?
- Which context-selection policies may generated code replace, and which provenance or scope rules must remain protected?
- How can a runtime expose rich extension points without making every extension part of the trusted computing base?
