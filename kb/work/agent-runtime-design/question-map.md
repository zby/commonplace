# Initial Question Map for Agent Runtime Design

This is a starting map, not a requirements verdict. It identifies the decisions a later synthesis must make and the evidence needed to make them. The central risks are conflating the runtime with its clients and treating every useful mechanism or control as universal. A candidate requirement belongs in the final set only when a concrete work story needs it, its absence produces a recognizable failure, and ownership across runtime, client, policy, and host application can be named.

## Desired outcome

An agent runtime makes a bounded model useful in an environment that has more state, duration, authority, and failure modes than one inference call can hold. A runtime client lets a person or application operate it: select and configure work, understand what is happening, grant or withhold authority, steer or interrupt execution, and recover or inspect results.

The comparison target is the runtime architecture together with its externalized control boundaries, not raw model quality or the polish of one user interface. The method must ask what the runtime owns, which state and commands it exposes, which guarantees cross process or context loss, and what it leaves to a client or host application.

The first substantive thesis is [Capabilities are the clean interface for user approval](./capabilities-are-the-clean-interface-for-user-approval.md). The runtime exposes an action alphabet and derives scoped capability requests from attempted effects. Policy resolves existing grants. A runtime client asks the user only about unresolved authority and carries the resulting grant or denial back into execution. Because that answer may arrive much later, meaningful approval also tests durable suspension and resumption.

## Work stories that expose different needs

| Work story | What makes it distinct | Candidate runtime requirements and client surfaces |
|---|---|---|
| Interactive tool task | Short-lived work with a human present and immediate feedback | Proposed effects, scoped approval choices, tool results, steering, stop and retry controls |
| Long-running task | The work exceeds one context window or one process lifetime | Progress projection, pending decisions, checkpoints, cancel/resume controls, bounded reconstruction evidence |
| Delegated review or research | Several bounded contexts produce artifacts for a parent | Worker tree, task and capability scopes, ownership, status/failure propagation, reconciliation controls |
| High-authority or untrusted task | Inputs may be adversarial and actions may affect valuable state | Isolation profile, unavailable capabilities, privilege boundaries, approval context, mutation audit |
| Embedded agent capability | An application owns branching, state projection, and re-entry | Event/command protocol, callbacks for unresolved decisions, composable policy and state projection |
| Model-authored symbolic decomposition | The model discovers that parts of the task need exact loops, joins, transforms, or recursive calls during execution | Capability-bounded guest code, run-local registration, recursive invocation, typed boundaries, suspension and resource limits |
| Durable service or control plane | Many runs, users, workers, or schedules share infrastructure | Run identity, principal identity, concurrent pending decisions, queues, cancellation, reconnect and audit |
| Runtime improvement loop | A builder proposes changes to prompts, tools, policies, or runtime machinery | Update boundary, evaluation evidence, versions, rollback, protected substrate, explicit admission decision |

No single system has to optimize every row. The eventual method needs to say which responsibilities are a common floor, which are conditional on a claimed use story, and which can be externalized without misrepresenting the system.

## A concrete demand already present in Commonplace

The [agent-memory review-writing skill](../../instructions/write-agent-memory-system-review/SKILL.md) is one worked runtime-demand case. Its code-grounded drafting workflow assumes that the parent can:

- discover whether a real sub-agent mechanism and an execution slot are available;
- launch one worker with fresh, task-local context rather than an inherited conversation;
- give the worker a narrow artifact boundary while the parent retains checkout, lifecycle, index, and QA ownership;
- receive explicit completion, validation, provenance, and trace-learning results;
- close or release the worker before starting a separate semantic-QA phase;
- stop or wait visibly when delegation is unavailable instead of silently replacing it with a nested command-line agent.

These expectations expose both runtime and client responsibilities. The runtime must implement fresh contexts, worker lifecycle, scoped actions, status, and safe cancellation. A client must show whether those capabilities exist, let the user authorize additional effects, and make timeout, cancellation, and partial completion visible. Does “fresh context” mean no inherited conversation, a clean filesystem view, or both? Is a worker's artifact boundary enforced or merely instructed? Can a worker bypass its granted authority through another execution channel?

This one workflow should not define the general model. It is evidence that delegation quality is more than the ability to start another model call: context isolation, authority, lifecycle, and result semantics are part of the capability.

## Initial pressure map

The existing theory suggests three runtime components—scheduler, context engine, and execution substrate. Runtime clients project selected state from those components and return user or application decisions. A builder plane may change the runtime and must be analysed separately from the version currently executing work.

| Pressure area | Runtime responsibility | Required client or API exposure | Failure at the boundary |
|---|---|---|---|
| Progress and control flow | State transitions, termination, retry, branching, deadlines | Show current state and expose valid steer, stop, retry, or resume operations | User acts on stale or fictional progress; non-termination cannot be interrupted |
| Context assembly | Loaded sources, scope, compaction, instruction precedence | Show consequential context state or provenance where intervention depends on it | User cannot explain or correct missing, stale, or conflicting context |
| Tools and effects | Capability surface, concrete requests, results, errors, timeouts | Present effects and scopes; carry grants/denials; distinguish denial from tool failure | Equivalent authority bypasses approval through another tool; false success hides failure |
| Durable run state | Run identity, checkpoints, suspension, cancellation, idempotency, and resume semantics | Preserve or recover the controls and pending decisions the runtime actually supports | Client reconnect loses pending work; “resume” may replay unsafe effects |
| Delegation and coordination | Worker tree, scopes, ownership, dependencies, guarantees | Show principals and attenuation; expose status, escalation, cancellation, and reconciliation | Ambient authority leaks to children; failures or conflicting outputs become invisible |
| Authority and isolation | Grant set, environment ceiling, privilege quarantine, secrets boundary | Distinguish what may be approved from what isolation makes impossible | Approval is presented as security; user grants authority to the wrong principal or scope |
| Observation and diagnosis | Events, traces, structured errors, causal drill-down | Project enough evidence for monitoring, approval, debugging, and audit | Final success conceals broken infrastructure or unintended paths |
| Evaluation and evolution | Outcome evidence, candidate attribution, versions, rollback | Present the basis and consequence of admitting a change | User approves a retained change without evidence that it helps |
| Integration and economics | Provider/environment assumptions, latency, tokens, money, parallelism | Expose consequential cost and compatibility choices at decision time | User cannot distinguish a blocked capability from an unavailable one or bound a costly grant |

The map is deliberately phrased as pressures and failures. Later work must decide whether each pressure produces a general requirement, a conditional requirement, or merely a comparison axis.

## Tests for a candidate requirement

For every proposed requirement, ask:

1. **Work story:** Which concrete work becomes impossible, unsafe, or misleading without it?
2. **Observable failure:** What evidence would show that the responsibility is not being met?
3. **Owner:** Which part is runtime mechanism, client surface, policy decision, tool declaration, host integration, or human judgment?
4. **Guarantee:** Is this a hard invariant, a best-effort policy, or only an available API?
5. **Wiring:** Does the shipped system use the capability, or merely make it possible for an integrator to use?
6. **Boundary:** Does the property survive process loss, context reset, delegation, and alternative execution channels?
7. **Cost:** What context, latency, compute, operator attention, or implementation complexity buys the guarantee?
8. **Evidence:** Can the claim be established from code and tests, or does it require a live behavioral probe?

These tests should stop the eventual review type from becoming a feature checklist. A field earns a place when it changes how a system should be trusted, used, compared, or improved.

## Open design questions

### Purpose and boundary

- What minimum event-and-command protocol makes a runtime governable by clients rather than merely launchable?
- Which runtime state must be projected for approval, steering, interruption, and recovery to be meaningful?
- Where does the runtime end when a host application supplies scheduling, state, policy, or recovery?
- Which memory controls belong in a runtime review: read-back visibility, context injection, deletion/retirement controls, or only the runtime-facing memory contract?

### Decomposition

- Does scheduler/context-engine/execution-substrate remain sufficient once policy, durable suspension, event protocols, and clients are made explicit?
- Which scheduler mechanisms must be protected while decomposition policy remains replaceable or model-authored?
- Is runtime policy part of the runtime or a boundary object configured through a client and enforced by the runtime?
- Should the runtime, builder plane, and improvement loop be reviewed separately even when one product ships all three?
- Which state belongs to the scheduler, which to tools, and which to the host application?

### Dynamic extension

- What symbolic execution surface lets the model express exact parts of a decomposition without becoming trapped in a fixed orchestration DSL?
- Which runtime primitives must be compositionally complete for a model-authored guest program?
- How are generated programs scoped, identified, versioned, observed, cancelled, and resumed?
- Can generated code define new run-local callables without mutating a global registry?
- How are capabilities attenuated across calls made by generated code, and how does that code request additional authority?
- Where is the boundary between run-local self-generated execution, externally authored durable extension, durable self-generated capability promotion, and durable self-generated modification of the protected runtime?
- Which declared system boundary makes a generated durable capability part of the runtime's own behavior-determining organization rather than an external work product?
- Which invariants cannot themselves be extension points because an extension could then bypass or redefine them?

### Reliability and recovery

- What does completion mean: model stop, loop termination, committed effects, or a verified task outcome?
- Which retry and resume semantics are safe when tools have external side effects?
- How should cancellation propagate through queued work, sub-agents, tool calls, and external services?
- When should failure remain visible even if the model found a workaround?

### Context and delegation

- What isolation guarantees distinguish a sub-agent from another call in the same conversation?
- Which coordination guarantees are needed for shared artifacts, competing proposals, dependent steps, and final synthesis?
- When a sub-agent lacks authority, does it prompt the user directly, route a request through its parent, suspend, fail closed, or return a structured escalation result?
- How should task-local instructions interact with runtime-discovered skills, policies, and automatic discovery?
- What evidence shows that compaction or context projection preserved the state needed for the next action?

### Authority and human control

- What capability request fields are necessary for an informed user decision: principal, effect, target, arguments, limits, provenance, and proposed lifetime?
- Which grants may be inherited by children, which must be attenuated, and which may never cross a delegation boundary?
- Which principals may interrupt the user for approval, and how does the runtime bound or aggregate approval requests from concurrent children?
- Can the absence of child-to-user approval be a deliberate attention policy rather than a missing mechanism, and which work stories does each interpretation support?
- How do one-call, task, session, and persistent grants remain inspectable and revocable?
- Is per-tool permission scope enough, or do untrusted-reader roles require privilege quarantine across all channels?
- How are identity and authority preserved across delegation and service boundaries?
- What information and timing make a human approval meaningful rather than ceremonial?
- Which protected substrate must remain outside a self-modifying runtime's update boundary?

### Observation, evaluation, and improvement

- What is the minimum event and state model needed to reconstruct why a run behaved as it did?
- Which claims are code-groundable, and which require behavioral or fault-injection probes?
- How should reviews distinguish crash recovery, task correctness, behavioral faithfulness, and operational health?
- Can the same review contract cover ordinary and reflective runtimes without flattening the builder plane into runtime features?

### Adoption and cost

- Which model, provider, operating-system, shell, sandbox, and tool-protocol assumptions are architectural?
- When does a framework-owned loop simplify the common case, and when does it block state projection, branching, or re-entry?
- How should token use, latency, parallelism, cache reuse, and operator attention enter the comparison without displacing correctness and control?
- What remains usable if the specialized runtime or service disappears?

## Evidence already available

The current corpus is useful because it is heterogeneous rather than standardized:

- [Claude Code dynamic workflows](../../agentic-systems/reviews/claude-code-dynamic-workflows.md) exposes model-authored orchestration over bounded sub-agents and makes the withheld runtime state visible by contrast.
- [Fractal](../../agentic-systems/reviews/fractal.md) separates workspace turns, sandbox mounting, delegation, and session continuity.
- [Swamp](../../agentic-systems/reviews/swamp.md) emphasizes a typed operational model, declarative workflows, distributed execution, policy gates, and audit.
- [Agno AgentOS](../../agentic-systems/reviews/agno-agentos.md) separates agent/team loops, workflow control flow, a service control plane, recovery, and builder authority.
- [Exo](../../agentic-systems/reviews/exo.md) separates a protected substrate from a rewritable executor and exposes the boundary of self-modification.
- [Autogenesis](../../agentic-systems/reviews/autogenesis.md) contrasts versioned mutation and rollback with weaker evidence that a change deserved commitment.

The theory base supplies candidate explanations rather than a ready schema:

- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) gives the binding resource pressure.
- [LLM frameworks should keep the tool loop optional](../../notes/llm-frameworks-should-keep-the-tool-loop-optional.md) exposes the host-ownership boundary.
- [Agent orchestration occupies a multi-dimensional design space](../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) identifies independent orchestration choices.
- [Agent orchestration needs coordination guarantees](../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) asks what prevents composed-agent failure modes.
- [Runtime structure determines governance control surfaces](../../notes/runtime-structure-determines-governance-control-surfaces.md) connects architecture to intervention and audit.
- [Diagnostic richness constrains outer-loop learning quality](../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) separates outcome selection from evidence for the next improvement.
- [Scenario decomposition drives architecture](../../notes/scenario-decomposition-drives-architecture.md) supplies the requirement-derivation method used here.

The source base also contains a direct forcing case for runtime durability:

- [Your Old Agent Architecture Is Dead… Meet Its Replacement](../../sources/jdegoes-recursive-agent-architecture-2081854216264392934.ingest.md) argues that reviewed plans and human approvals require durable suspension, exactly-once effects, recovery, and capability-bounded enforcement from the runtime.

The second working thesis combines the existing symbolic-execution cases:

- [Runtime minimality is a protected waist, not a small feature list](./runtime-minimality-is-a-protected-waist-not-a-small-feature-list.md) separates invariant-owning runtime mechanisms from model-authored decomposition policy and distinguishes run-local guest programs from durable promotion.

## Next analytical decision

The first [review-protocol pilot](./review-protocol-pilot-pi-swamp-exo.md) established the fixed boundary-and-evidence spine. The [dynamic-extension mechanism pilot](./dynamic-extension-mechanism-pilot.md) separated authorship, artifact persistence, activation, change target, admission, and authority without treating features as peer runtimes. The [provisional requirements map](./agent-runtime-requirements-map.md) keeps “always ask in a review” separate from “every runtime must implement.”

The [Fractal–llm-do code-grounded runtime pilot](./fractal-llm-do-code-grounded-runtime-pilot.md) tests those conclusions against two runtime-facing systems with different externalized boundaries. It shows why source inspection must be primary: Fractal's effect hooks observe rather than authorize, and llm-do's approval wrapper governs toolsets but not every exposed execution path. It also separates awaited local approval from global runtime blocking and separates conversational history, runtime-instance state, durable continuation, retained bytes, and later activation.

The [PydanticAI–DSPy code-grounded boundary pilot](./pydantic-ai-dspy-code-grounded-boundary-pilot.md) completes the embedded-library and lower-bound tests. It shows that PydanticAI owns an inner agent graph while a host may own durable waiting and the sequence of runs. It also shows that DSPy core is a returning computation library, not a deficient runtime, even though `ReAct` is a nested agentic mechanism. Approval therefore needs correlated pending-decision resolution that preserves the blocked dependency; inline waiting and terminal deferral plus later re-entry are both valid shapes. Target classification must precede runtime assessment.

The [provisional review protocol](./agent-runtime-review-protocol.md#code-grounded-review-procedure) now states a compact source-inspection procedure. The next decision is whether another reviewer can reproduce its target classification, boundary, and guarantee judgments without inheriting the pilot conclusions. The hardest remaining forcing cases are durable approval across process loss, concurrent child escalation, a composite whose effects are only partly knowable up front, durable generated-artifact activation, and an untrusted-reader role that must never receive a high-authority capability.
