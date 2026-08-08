# Provisional Agent-Runtime Requirements Map

## Status

This is a workshop synthesis derived from the [Pi–Swamp–Exo runtime pilot](./review-protocol-pilot-pi-swamp-exo.md), the [dynamic-extension mechanism pilot](./dynamic-extension-mechanism-pilot.md), the [Fractal–llm-do code-grounded runtime pilot](./fractal-llm-do-code-grounded-runtime-pilot.md), the [PydanticAI–DSPy boundary pilot](./pydantic-ai-dspy-code-grounded-boundary-pilot.md), and the [initial question map](./question-map.md). It is not yet a library requirements inventory, review type, or implementation plan.

The map separates four things that are easy to conflate:

1. **Mandatory review records** — questions every review should answer. These are requirements of the review method, not features every runtime must implement.
2. **Candidate common floor** — semantic contracts that appear necessary for governable execution across the work stories examined so far.
3. **Conditional requirements** — machinery required only when a runtime claims a work story that needs it.
4. **Externalizable responsibilities** — work another layer may own if the runtime boundary preserves the required semantics.

The classifications are provisional. A later review can downgrade a common-floor candidate, split a requirement, or show that a responsibility can be externalized more cleanly than this map currently assumes.

## Derivation method

The map follows [scenario decomposition drives architecture](../../notes/scenario-decomposition-drives-architecture.md): start from complete work stories, identify the state and control needed at each step, and derive requirements from recurring steps and recognizable failures.

The work-story keys are:

| Key | Work story |
|---|---|
| W1 | Interactive tool use with a person present |
| W2 | Embedded or headless agent execution |
| W3 | Long-running, reconnectable, or resumable work |
| W4 | Delegated semantic work or distributed deterministic execution |
| W5 | High-authority work or work over untrusted inputs |
| W6 | Model-authored run-local symbolic execution |
| W7 | Durable generated capabilities or workflows |
| W8 | Runtime improvement or self-modification |
| W9 | Multi-user, multi-tenant, scheduled, or fleet operation |

No runtime must optimize every story. The review should first establish which stories the system claims.

## Classification and guarantee vocabulary

| Classification | Meaning |
|---|---|
| Candidate common floor | Appears necessary for an operational system to claim governable agent execution; may be supplied through a host boundary rather than one internal component |
| Conditional | Required only when a claimed work story activates the failure it prevents |
| Externalizable | Another named layer may own the responsibility if an explicit boundary contract preserves the claimed guarantee |
| Comparison axis | Useful for describing systems but not yet shown to be an implementation requirement |

Guarantee strength should also be explicit:

| Strength | Meaning |
|---|---|
| Invariant | Relevant execution paths cannot bypass the property inside the declared boundary |
| Protocol | Participants exchange defined identities, states, commands, and outcomes |
| Policy | A replaceable decision rule chooses among behavior allowed by the mechanism |
| Best effort | The system attempts the property without promising it under every failure |
| Deployment guarantee | The property depends on the actual process, sandbox, storage, identity, or fleet environment |

“Externalizable” never means “absent but excused.” It means a stated scenario and guarantee are preserved by a named owner and boundary contract.

A returning model computation or host-language module is not automatically an operational runtime. The common floor applies when a selected surface claims to turn model judgments into situated execution. A nested mechanism can still be tested against the requirements it activates, but missing lifecycle, client, durability, or authority machinery must not be scored as a runtime gap unless the mechanism or its enclosing product claims that work.

## Mandatory review records

These records belong in every completed review even when the corresponding implementation feature does not apply.

| Record | What the review must establish |
|---|---|
| RR1 Evidence basis | Revision or version, inspected source, scenarios or tests run, missing evidence, and whether each load-bearing claim is wired, merely available, documented, or not established |
| RR2 Target and enclosing system | Which operational surface inside the repository is being reviewed; whether it is a runtime, client, host, returning computation, pattern, workflow, generated program, tool, or subsystem; nested mechanisms must name their enclosing operational system |
| RR3 Claimed work | Which work stories the system claims and which it explicitly leaves outside its boundary |
| RR4 Responsibility map | Model, runtime, client, host, memory, policy, deployment, and builder ownership; shared processes do not erase distinct responsibilities |
| RR5 End-to-end scenario and outcome | Principal, input, state path, context/action surface, effect path, events and controls, terminal result, and what persists or is lost |
| RR6 Guarantee strength | Whether a property is an invariant, protocol, policy, best effort, deployment guarantee, or carries no claimed guarantee; RR1 separately records whether its implementation is wired, a hook, documented, or unknown |
| RR7 Authority record | For effectful systems: capability surface, grant set, and isolation envelope; for returning computations or effect-free operational surfaces: why effects are empty or owned by the host |
| RR8 Externalization and unknowns | What another layer owns, the contract at that boundary, unsupported implications, and concrete changes that would alter the assessment |

These records should become candidates for the eventual review type or writing skill. They must not be turned into runtime feature checkboxes.

## Candidate common floor

The common floor is phrased as semantic contracts rather than a required internal decomposition. It applies to a selected operational surface that claims governable agent execution, including a runtime-plus-host composition. Scheduler, context engine, and execution substrate remain useful translation lenses, not mandatory classes or services.

| ID | Candidate requirement | Trigger and recognizable failure | Default owner and strength | Evidence test |
|---|---|---|---|---|
| CF1 | **Addressable execution and explicit outcomes** | Any claimed operational work story W1–W9. Without a named invocation or run, clients cannot correlate events or tell whether work is live, completed, failed, denied, cancelled, or interrupted. | Runtime or lifecycle-owning host; protocol | Trace a request from start through intermediate work to every supported terminal state. Confirm identifiers and outcome meanings cross the client boundary. |
| CF2 | **Bounded semantic-call projection** | Every bounded model judgment. Without an explicit projection, the next call receives stale, unbounded, or unexplained state, and recovery cannot say what must be reconstructed. | Runtime, context service, or host; protocol plus enforced limits where claimed | Inspect the actual instructions, state, tools, provenance, and limits supplied to a call. Cross a context or process boundary and establish what is retained, recomputed, or lost. |
| CF3 | **Mediated action/result boundary** | Any consequential action the declared operational surface claims to govern. Without mediation, an alternate tool, shell, extension, or child path bypasses identity, policy, events, or error semantics. | Runtime invocation path; invariant for the declared governed surface | Enumerate ordinary, generated, delegated, extension, and broad-shell routes. Cause equivalent effects through each and identify the common enforcement/result point or the explicitly external route. |
| CF4 | **Control and observation boundary fitted to the claimed client** | W1 or W2, and every longer story. Without it, a person or host cannot start/configure work, observe a truthful outcome, or invoke the controls the runtime claims. | Runtime defines commands/events; client or host presents and calls them; protocol | Exercise the shipped CLI, TUI, API, callback, or embedding path. Correlate status, result, stop, cancel, steer, or retry commands with the addressed work. |
| CF5 | **Claimed guarantees cover every exposed execution path** | Any claimed runtime property. Without this rule, authority, cancellation, context, accounting, or another guarantee holds on the main path while an alternate exposed path bypasses it. | Runtime and host boundary; invariant for each claimed property | Enumerate the execution paths the runtime exposes. Compare equivalent calls across them and verify the claimed property remains true, or record the deliberate scope limit. |

CF3 does not require every runtime to implement human approval. A returning computation may externalize all situated effects to its host rather than satisfy CF3 vacuously; an agentic module such as DSPy `ReAct` activates CF3 only for the tool path it owns. CF4 does not require a graphical interface: an embedding API may be the claimed client boundary. CF5 is vacuous for a runtime that exposes only one path; it does not require composition. The common claim is that the semantics needed by the declared work and client are explicit and testable.

## Conditional requirement: iterative and recursive execution

| ID | Candidate requirement | Trigger and recognizable failure | Owner and strength | Evidence test |
|---|---|---|---|---|
| IT1 | **Enforceable termination and resource policy** | Any iterative, recursive, concurrent, or costly execution. Without a stop, cancellation, depth, time, cost, or other bound, non-termination and runaway resource use are indistinguishable from useful progress. | Runtime or host; policy backed by enforceable limits | Force a loop, recursion, long tool call, concurrency saturation, or exhausted budget. Confirm which limit stops it, what outcome is reported, and which cleanup or partial results remain. |

## Conditional requirements: authority and approval

These requirements activate when an effect may be denied or require authority not already granted.

| ID | Candidate requirement | Trigger and recognizable failure | Owner and strength | Evidence test |
|---|---|---|---|---|
| AP1 | **Structured capability request and scoped grant** | Any claimed work story with unresolved authority. A tool-name prompt cannot distinguish principal, effect, target, limits, or lifetime, and equivalent effects gain inconsistent treatment. | Effect adapter describes the request; runtime or policy resolves and enforces it; protocol plus authorization invariant | Cause the same effect through different tools. Verify a request identifies principal, effect, target/scope, provenance, limits, and proposed lifetime, and that the resulting grant is enforced at execution. |
| AP2 | **Separately represented creation, invocation, and nested-effect authority** | W6 or W7. Approval to create a generated callable accidentally becomes permission to invoke it later or perform every effect it can reach. | Runtime policy and client/headless resolver; policy with distinct enforcement boundaries | Represent and test creation, later invocation, and an effect inside the extension independently. If policy deliberately bundles them, verify the bundled grant states its combined scope and lifetime explicitly. |
| AP3 | **Correlated pending-decision resolution with explicit scope** | Any unresolved request. The answer reaches the wrong call, the dependent effect executes prematurely, the waiting or termination scope is implicit, or denial appears as accidental tool failure. | Runtime scheduler or lifecycle-owning host plus client protocol; protocol and stated liveness guarantee | Leave an effect pending; approve, deny, cancel, and time out the request. Verify the effect does not execute before resolution and each result is structured. Establish whether one live continuation waits or the invocation ends with typed pending work and a later invocation re-enters it; record run/conversation identities, retained state, and whether unrelated work continues, serializes, or is intentionally blocked. Test concurrent progress only when claimed. |
| AP4 | **Approval routing and bounded operator attention** | W4 or W9 with concurrent principals. Children prompt the user directly without policy, requests become unmanageable, or authority insufficiency is hidden. | Runtime supplies principal/correlation data; policy and client choose routing, aggregation, or fail-closed behavior; policy | Launch several children with insufficient authority. Inspect direct, parent-brokered, aggregated, or denied routing and measure which principals can interrupt the user. |
| AP5 | **Durable pending-decision recovery** | W3 or W9 when a decision may outlive a client or process. The request disappears, is answered twice, or resumes changed arguments or grants. | Durability-owning runtime or host plus client/policy protocol; recovery invariant | Stop at a pending decision, disconnect or kill the owner, resume, and verify stable request identity, invalidation rules, duplicate responses, and documented effect semantics. |

Capability requests are the workshop's strongest current approval interface. The exact component that constructs the request remains open: a tool adapter, effect interceptor, host policy service, or runtime may do it. The current requirement candidate is one correlated authority object and one enforcement path, not one prescribed class layout. A source's use of `capability` for composable behavior does not establish authority semantics, and human sign-off does not replace client authentication or effect-local authorization.

## Conditional requirements: durability and recovery

| ID | Candidate requirement | Trigger and recognizable failure | Owner and strength | Evidence test |
|---|---|---|---|---|
| DR1 | **Durable run state and re-entry** | W3 or W9, and W7 only when invocation of the durable extension itself claims resumable operation. Process loss erases progress, pending work, or the legal next transitions. | Runtime or orchestration host backed by storage; recovery invariant | Crash between meaningful transitions, restart, and verify identity, state version, pending work, valid commands, and terminal result. |
| DR2 | **In-flight effect reconciliation** | Retry or resume around consequential effects. An effect is silently repeated, skipped, or reported complete without evidence. | Runtime/tool protocol and effect adapter; invariant appropriate to the effect | Crash before and after effect commitment. Verify idempotency keys, at-most-once behavior, exactly-once where genuinely supported, or an explicit reconciliation path. |
| DR3 | **Reconnectable control and audit** | W3 or W9. A new client sees fictional state or cannot recover controls and decisions owned by the run. | Runtime/host event and state protocol; protocol plus delivery semantics | Disconnect a client, allow work to advance, reconnect, and compare reconstructed state, missing-event semantics, pending decisions, and available controls. |

Exactly-once execution is one possible guarantee, not a universal requirement. The requirement is to define and uphold effect semantics strong enough for the claimed recovery story.

## Conditional requirements: delegation and distribution

| ID | Candidate requirement | Trigger and recognizable failure | Owner and strength | Evidence test |
|---|---|---|---|---|
| DG1 | **Child identity with explicit context and authority projection** | W4. A child inherits ambient parent context or power, or reviewers cannot attribute its effects and results. | Runtime/orchestrator and policy; protocol plus an invariant against ambient or silent privilege escalation | Spawn a child and inspect its instructions, state, action surface, grants, environment, budget, and parent relation. Attempt an undeclared effect. |
| DG2 | **Join, cancellation, failure, and ownership semantics** | W4. Parents lose failures, cancellation leaks, outputs conflict, or completion has no reconciliation rule. | Runtime/orchestrator; protocol | Run successful, failed, timed-out, and cancelled children over shared and separate artifacts. Verify propagation, join behavior, cleanup, ownership, and result aggregation. |
| DG3 | **Structured authority escalation** | W4 with attenuated children. A child silently bypasses its scope, fails opaquely, or independently overloads the user. | Runtime and policy/client routing; protocol and policy | Give a child insufficient authority and verify a structured denial or parent-correlated escalation preserves child identity, requested scope, and continuation. |
| DS1 | **Distributed ownership and retry protocol** | W4 or W9 with remote workers. Duplicate workers, lost leases, split-brain state, or retry ambiguity corrupt results. | Distributed scheduler, queue, and worker host; deployment and protocol guarantee | Fault-inject worker loss, duplicate delivery, delayed result, cancellation, and reconnect. Inspect leases, deduplication, backpressure, and authoritative state. |

Semantic subagents, deterministic workers, and cloned successors satisfy different versions of these requirements. A subprocess alone is not evidence of delegation semantics.

## Conditional requirements: generated execution and durable extension

| ID | Candidate requirement | Trigger and recognizable failure | Owner and strength | Evidence test |
|---|---|---|---|---|
| EX1 | **Capability-bounded guest execution plane** | W6. Model-authored code reaches private runtime state or ambient host authority instead of composing public primitives. | Runtime execution substrate and host isolation; containment invariant | Generate a program that computes, branches, joins, invokes bounded calls, requests effects, and attempts private/ambient access. Verify only explicit handles work. |
| EX2 | **Run-local namespace and lifecycle by default** | W6. Temporary functions silently become global behavior or leak into unrelated runs. | Runtime registry/lifecycle; scope invariant | Create a generated callable, cancel or finish its run, then start another run and verify it is absent unless an explicit promotion occurred. |
| EX3 | **Common invocation semantics for generated composition** | W6. Nested generated calls bypass identity, authority, events, cancellation, error, or accounting paths. | Runtime scheduler and execution substrate; invariant | Compare static and generated callers invoking the same agent or tool. Verify the same policy, event, cancellation, and result contracts. |
| EX4 | **Generated-source provenance and resource accounting** | W6 or W7. Operators cannot identify what ran, who generated it, or why recursive work exceeded time, cost, or depth. | Runtime state/accounting; protocol and enforceable limits | Retain source/hash, authoring call, model/input identity, invoked effects, and limits. Exceed each supported budget and inspect the recorded result. |
| EX5 | **Durable extension admission, discovery, and lifecycle** | W7. Bytes remain on disk without later activation, or unreviewed/incompatible code enters a durable namespace with no rollback or retirement. | Registry and builder/deployment plane; protocol plus admission/activation invariants | Exercise generate → validate/review → admit → restart → discover/load → invoke → roll back/retire. Preserve authorship and version provenance. |

Dynamic execution requires model authorship but not durable storage. Durable self-extension requires a model-authored artifact to become operative in later runs. Artifact retention without later discovery and activation is archival storage, not durable extension.

## Conditional requirements: isolation, memory, and multi-principal operation

| ID | Candidate requirement | Trigger and recognizable failure | Owner and strength | Evidence test |
|---|---|---|---|---|
| SE1 | **Isolation ceiling and secret quarantine** | W5 or executable W6. Tool grants are presented as confinement while paths, network, environment, extensions, or broad shell retain greater power. | Sandbox/container/identity deployment; runtime must expose and not overstate the envelope; deployment guarantee | Attempt filesystem, network, process, environment, and secret access through every channel, including children and extensions. |
| MC1 | **Runtime-facing memory and context contract** | Any claimed memory integration. Stored material enters calls without clear snapshot, provenance, precedence, limits, or invalidation semantics. | Memory subsystem or host supplies material; runtime/context boundary consumes it; protocol | Change or invalidate retained state and observe exactly which version reaches the next call, how it is scoped, and how conflicts are resolved. |
| MP1 | **Principal, tenancy, and audit identity** | W9 or shared high-authority work. Effects, grants, state, and decisions cannot be attributed to the correct user, agent, tenant, or service. | Runtime plus identity/policy services; protocol and authorization invariant | Cross tenant/user/agent boundaries, inspect propagated identity and audit records, and attempt confused-deputy access. |
| MP2 | **Concurrent pending-work policy** | W9. Queues, approvals, or budgets from one run starve or interfere with others, and no owner can apply backpressure. | Runtime/control plane; policy with enforceable accounting | Saturate concurrency, pending decisions, and budget. Verify fair or documented scheduling, cancellation, quotas, and isolation between principals. |

The memory subsystem's internal retrieval and maintenance design remains outside this workshop. MC1 concerns only the contract by which retained material becomes runtime state or model context.

## Conditional requirements: builder plane and self-modification

| ID | Candidate requirement | Trigger and recognizable failure | Owner and strength | Evidence test |
|---|---|---|---|---|
| BI1 | **Versioned candidate attribution and admission evidence** | W8. A change is retained without knowing its author, target, evidence, evaluator, or admitted version. | Builder/improvement plane; protocol and policy | Generate several candidates, evaluate them, admit one, and reconstruct why that exact version became operative. |
| BI2 | **Protected update boundary and recoverable installation** | W8. An update rewrites the machinery meant to enforce admission/recovery, or a failed build destroys the last working version and diagnostic trace. | Protected runtime/guardian and deployment plane; invariant | Attempt to cross the protected boundary; interrupt build/restart; verify atomic installation, last-known-good recovery, rollback, and retained failure evidence. |
| BI3 | **Outcome-appropriate improvement oracle** | A system claims self-improvement rather than mere self-change. Mechanical validity is mistaken for evidence that later judgment or task performance improved. | Builder/evaluation plane; best effort or stronger only within oracle domain | Compare the admitted version against the declared objective with held-out or causal evidence. Distinguish build success, task success, and behavioral improvement. |

For this workshop, **runtime self-modification** is an end-to-end W8 pathway: an in-boundary process generates the concrete change; admission makes it part of the runtime's own [behavior-determining organization](../../notes/definitions/behavior-determining-organization.md); and later operation discovers and exercises it beyond the generating run. A saved workflow or capability may be durable self-extension without changing protected runtime machinery. Human admission does not erase model authorship, and automatic admission does not establish improvement.

## Externalization matrix

| Responsibility | May be owned by | Minimum boundary contract | Insufficient evidence |
|---|---|---|---|
| Lifecycle and scheduling | Host application or workflow engine | Work and transition identity, legal commands, terminal/cancel/error semantics, and correlation | Opaque launch callback |
| Effect execution | Tool adapter, host action service, or domain integration | Action and principal identity, correlation, result/error/commit semantics, enforcement point, and effect scope | Bare host callback or tool name |
| Approval and policy | Client, parent, or policy service | Principal/action/target/scope request, decision identity, grant or denial, lifetime, and timeout; either inline waiting or typed pending output plus correlated re-entry; audit and authorization semantics | UI prompt with no run or effect linkage, or client-submitted sign-off treated as authorization |
| Durability and recovery | Store or orchestration host | Versioned checkpoint, resume input, pending-decision retention where claimed, and in-flight effect reconciliation | Logs or transcript alone |
| Context and memory | Host or memory service | Selected snapshot, provenance, precedence, scope, limits, and reconstruction/invalidation contract | Unspecified chat history |
| Isolation and secrets | Sandbox, container, operating system, or identity provider | Environment ceiling, credential/path/network boundary, enforcement point, and propagation to children | Tool-name allowlist |
| Delegation and worker placement | Process manager, fleet, or host | Child identity, context/authority projection, result/join/cancel/error protocol | Subprocess spawn alone |
| Extensions and self-change | Registry, build system, or deployment plane | Artifact identity/authorship, admission, discovery/activation, versions, rollback/retirement, and protected-boundary rule | Persisted source file |
| Observation and audit | Telemetry or event host | Correlated identifiers, delivery/loss semantics, state/result references, retention, and access boundary | Final text or report alone |

Externalized is not missing when the named layer actually supplies the contract. It is missing when the review can find only an assumption, an example integration, or a callback whose semantics are unspecified.

## What this map does not require

The evidence so far does not support universal requirements for:

- one scheduler/context-engine/execution-substrate implementation shape;
- a TUI, CLI, service, or any other particular client;
- subagents, distributed workers, durable execution, or self-modification;
- human approval for every effect;
- a live coroutine or process for every unresolved approval;
- prompt count as a security or governance score;
- exactly-once execution where idempotency or reconciliation is the honest guarantee;
- a runtime-owned sandbox when deployment supplies the real isolation ceiling;
- automatic promotion of generated artifacts;
- verified improvement merely because a rewrite builds, tests, or restarts;
- uniform review headings for every lens.

It also does not rank minimal and feature-rich runtimes on one scale. A smaller system can satisfy its claimed stories with fewer mechanisms. A larger system earns its machinery only through the guarantees and work it supports.

## Pilot traceability

| Pilot observation | Requirements or records it supports |
|---|---|
| Pi child processes receive tool names but no child-to-parent approval protocol; Bash and extension authority remain broader than the name list | RR7, CF3, CF5, AP4, DG1, DG3, SE1 |
| Swamp externalizes semantic interpretation while owning typed state, deterministic scheduling, durable gates, policy, workers, and audit | RR2–RR6, CF1–CF4, AP5, DR1–DR3, DS1 |
| Exo separates a protected substrate from an agent-rewritable executor and preserves failed updates without proving behavioral improvement | CF5, EX5, BI1–BI3 |
| RLM-generated programs are model-authored but ephemeral | EX1–EX4; negative boundary case for EX5 |
| Claude Code workflows are a subsystem whose runtime owns permissions, journals, budgets, UI, and promotion | RR2, AP1–AP3, EX1–EX5 |
| Tendril retains generated capabilities with a sandbox but weak admission and retirement evidence | EX5, SE1, BI1; negative evidence for treating retention as verified improvement |
| llm-do separates dynamic-agent creation, invocation, and child effects; generated files may outlive a process while automatic activation remains limited to the current `Runtime` instance | AP2–AP3, EX2–EX5; demonstrates storage versus activation |
| Fractal owns durable conversational turns while PredictRLM and SBX own generated execution and containment; available effect hooks observe but do not authorize | RR2–RR8, CF1–CF5, IT1, DR1, EX1–EX4, SE1; distinguishes conversational resume from continuation recovery |
| llm-do's TUI prompt path awaits toolset approvals while its event loop remains live, but direct tools, built-ins, and trusted Python entries follow other paths | CF3–CF5, AP1–AP3, DG1; negative boundaries for AP5 and DG2–DG3, while AP4 remains untested |
| llm-do retains generated `.agent` bytes while activation lasts only in the current runtime instance | EX2–EX5; requires precise call, run, runtime-instance, process, artifact, and activation lifetimes |
| PydanticAI owns an inner agent graph while its caller owns the outer sequence of runs; deferred approval can terminate one run and re-enter through another | RR2–RR8, CF1–CF5, AP1, AP3; protocol boundary for AP5 and DR1–DR3 |
| DSPy core is a returning host-language computation library, while `ReAct` is a nested tool loop whose direct callable effects remain host-governed | RR2–RR8, CF2–CF5, IT1; boundary case against manufacturing runtime gaps |

## Open tests before promotion

The map should not graduate yet. It needs at least these tests:

1. Trace an open-source approval path that survives client and process loss, including cancellation, duplicate response, and an effect committed near the failure boundary.
2. Trace concurrent children with unresolved authority to test principal identity, parent routing, unrelated progress, and bounded operator attention.
3. Trace a generated composite whose effects cannot all be known before execution.
4. Trace a generated artifact through restart, admission, discovery, activation, rollback, and retirement.
5. Test an untrusted-reader role that must never receive or indirectly reach a high-authority capability.
6. Ask which requirement fields change an architectural judgment often enough to deserve controlled review fields rather than prose.
7. Give a compact code-grounded procedure to an independent reviewer and test whether target classification, responsibility boundaries, and guarantee judgments reproduce.

Only after these tests should stable requirements be promoted into individual library notes. The eventual review type should retain compact, always-useful records. The writing skill should own scenario selection, source inspection, forcing tests, conditional lenses, semantic QA, and validation.
