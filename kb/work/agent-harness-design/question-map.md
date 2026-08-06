# Initial Question Map for Agent Harness Design

This is a starting map, not a requirements verdict. It identifies the decisions a later synthesis must make and the evidence needed to make them. The central risk is treating every useful harness feature as universal. A capability belongs in the final requirements only when a concrete work story needs it, its absence produces a recognizable failure, and its owner can be named.

## Desired outcome

A harness should make a bounded model useful in an environment that has more state, duration, authority, and failure modes than one inference call can hold. That sentence is intentionally broad. The workshop still needs to decide what “make useful” means across settings and which guarantees must come from the harness rather than from the host application, tools, model, or operator.

The comparison target is therefore not raw model quality. It is the difference the surrounding system makes: what work becomes possible, what failures become containable or visible, and what costs or constraints the harness introduces.

## Work stories that expose different needs

| Work story | What makes it distinct | Candidate harness responsibilities |
|---|---|---|
| Interactive tool task | Short-lived work with a human present and immediate feedback | Tool dispatch, result projection, stop conditions, permission prompts, concise context maintenance |
| Long-running task | The work exceeds one context window or one process lifetime | Explicit progress state, checkpoints, resume, retry policy, cancellation, bounded reconstruction |
| Delegated review or research | Several bounded contexts produce artifacts for a parent | Task-local context, worker authority, ownership of outputs, status and failure propagation, result reconciliation |
| High-authority or untrusted task | Inputs may be adversarial and actions may affect valuable state | Privilege separation, sandbox boundaries, approvals, secret isolation, auditable mutations |
| Embedded agent capability | An application owns branching, state projection, and re-entry | Optional rather than framework-owned loops, composable call APIs, host-visible state and errors |
| Durable service or control plane | Many runs, users, workers, or schedules share infrastructure | Persistent run identity, concurrency control, authorization, queues, backpressure, operational observation |
| Harness improvement loop | A builder proposes changes to prompts, tools, policies, or the harness itself | Addressable change surfaces, evaluation, versioning, rollback, protected substrate, provenance |

No single system has to optimize every row. The eventual method needs to say which responsibilities are a common floor, which are conditional on a claimed use story, and which can be externalized without misrepresenting the system.

## A concrete demand already present in Commonplace

The [agent-memory review-writing skill](../../instructions/write-agent-memory-system-review/SKILL.md) is one worked harness-demand case. Its code-grounded drafting workflow assumes that the parent can:

- discover whether a real sub-agent mechanism and an execution slot are available;
- launch one worker with fresh, task-local context rather than an inherited conversation;
- give the worker a narrow artifact boundary while the parent retains checkout, lifecycle, index, and QA ownership;
- receive explicit completion, validation, provenance, and trace-learning results;
- close or release the worker before starting a separate semantic-QA phase;
- stop or wait visibly when delegation is unavailable instead of silently replacing it with a nested command-line agent.

These expectations expose real harness questions. Does “fresh context” mean no inherited conversation, a clean filesystem view, or both? Is a worker's artifact boundary enforced or merely instructed? What status can the parent observe? How are cancellation, timeout, and partial writes represented? Can a harness prevent a worker from bypassing its authority through another execution channel?

This one workflow should not define the general model. It is evidence that delegation quality is more than the ability to start another model call: context isolation, authority, lifecycle, and result semantics are part of the capability.

## Initial pressure map

The existing theory suggests three functional components—scheduler, context engine, and execution substrate. Real systems also expose human/control surfaces and sometimes a builder plane. The workshop must determine whether those are components, cross-cutting concerns, or adjacent systems.

| Pressure area | What must be made explicit | Failure when it stays implicit |
|---|---|---|
| Progress and control flow | State transitions, next-step selection, termination, retry, branching, deadlines | Repeated actions, lost progress, prompt-only bookkeeping, non-termination |
| Context assembly | Routing, loading, scoping, compaction, instruction precedence, provenance | Context dilution, stale or missing constraints, cross-task contamination |
| Tools and effects | Capability discovery, argument/result contracts, errors, timeouts, side-effect boundaries | Silent workaround, malformed calls, duplicate effects, false success |
| Durable run state | Run identity, checkpoints, resume semantics, cancellation, external-effect reconciliation | “Resume” that replays unsafe work, orphaned runs, process loss erasing control state |
| Delegation and coordination | Worker context, ownership, dependencies, communication, reconciliation, guarantees | Duplicated work, inconsistent artifacts, contamination, liability diffusion |
| Authority and isolation | Principal identity, permission scope, privilege quarantine, approvals, secrets, sandbox escape paths | Confused deputy behavior, prompt injection reaching high-authority tools, unaudited mutation |
| Human control | Intervention points, explanations, approval semantics, cancellation, escalation | Nominal human oversight that arrives too late or lacks enough state to decide |
| Observation and diagnosis | Events, traces, structured errors, state inspection, causal drill-down | Final success hiding broken infrastructure; scores showing what won but not why |
| Evaluation and evolution | Outcome oracles, regression checks, candidate attribution, versioning, rollback, protected boundaries | Reliable retention of changes that were never shown to help; self-modification outside the oracle's domain |
| Integration and economics | Host-owned versus framework-owned loop, model/provider portability, environment assumptions, latency and token costs | Lock-in, duplicated state machines, instructions that cannot execute in the deployed channel |

The map is deliberately phrased as pressures and failures. Later work must decide whether each pressure produces a general requirement, a conditional requirement, or merely a comparison axis.

## Tests for a candidate requirement

For every proposed requirement, ask:

1. **Work story:** Which concrete work becomes impossible, unsafe, or misleading without it?
2. **Observable failure:** What evidence would show that the responsibility is not being met?
3. **Owner:** Is the mechanism owned by the harness, host application, tool, memory subsystem, model, or human operator?
4. **Guarantee:** Is this a hard invariant, a best-effort policy, or only an available API?
5. **Wiring:** Does the shipped system use the capability, or merely make it possible for an integrator to use?
6. **Boundary:** Does the property survive process loss, context reset, delegation, and alternative execution channels?
7. **Cost:** What context, latency, compute, operator attention, or implementation complexity buys the guarantee?
8. **Evidence:** Can the claim be established from code and tests, or does it require a live behavioral probe?

These tests should stop the eventual review type from becoming a feature checklist. A field earns a place when it changes how a system should be trusted, used, compared, or improved.

## Open design questions

### Purpose and boundary

- Is the common floor simply “model call plus tools and a stop condition,” or must a harness own state projection and recovery too?
- Where does a framework end and a harness begin when the host application owns the loop?
- Is a user interface part of the harness when it carries approval, intervention, and explanation semantics?
- Which memory responsibilities belong in the harness review: store internals, read-back wiring, context injection, or only the interface contract?

### Decomposition

- Does scheduler/context-engine/execution-substrate remain sufficient when authorization, multi-user control, and durable services enter scope?
- Is the control plane a fourth component, or a set of cross-cutting governance surfaces over the three components?
- Should the runtime, builder plane, and improvement loop be reviewed separately even when one product ships all three?
- Which state belongs to the scheduler, which to tools, and which to the host application?

### Reliability and recovery

- What does completion mean: model stop, loop termination, committed effects, or a verified task outcome?
- Which retry and resume semantics are safe when tools have external side effects?
- How should cancellation propagate through queued work, sub-agents, tool calls, and external services?
- When should failure remain visible even if the model found a workaround?

### Context and delegation

- What isolation guarantees distinguish a sub-agent from another call in the same conversation?
- Which coordination guarantees are needed for shared artifacts, competing proposals, dependent steps, and final synthesis?
- How should task-local instructions interact with harness-wide skills, policies, and automatic discovery?
- What evidence shows that compaction or context projection preserved the state needed for the next action?

### Authority and human control

- Is per-tool permission scope enough, or do untrusted-reader roles require privilege quarantine across all channels?
- How are identity and authority preserved across delegation and service boundaries?
- What information and timing make a human approval meaningful rather than ceremonial?
- Which protected substrate must remain outside a self-modifying harness's update boundary?

### Observation, evaluation, and improvement

- What is the minimum event and state model needed to reconstruct why a run behaved as it did?
- Which claims are code-groundable, and which require behavioral or fault-injection probes?
- How should reviews distinguish crash recovery, task correctness, behavioral faithfulness, and operational health?
- Can the same review contract cover ordinary runtimes and reflective harnesses without flattening the builder plane into runtime features?

### Adoption and cost

- Which model, provider, operating-system, shell, sandbox, and tool-protocol assumptions are architectural?
- When does a framework-owned loop simplify the common case, and when does it block state projection, branching, or re-entry?
- How should token use, latency, parallelism, cache reuse, and operator attention enter the comparison without displacing correctness and control?
- What remains usable if the specialized harness or service disappears?

## Evidence already available

The current corpus is useful because it is heterogeneous rather than standardized:

- [Claude Code dynamic workflows](../../agentic-systems/claude-code-dynamic-workflows.md) exposes model-authored orchestration over bounded sub-agents and makes the withheld runtime state visible by contrast.
- [Fractal](../../agentic-systems/fractal.md) separates workspace turns, sandbox mounting, delegation, and session continuity.
- [Swamp](../../agentic-systems/swamp.md) emphasizes a typed operational model, declarative workflows, distributed execution, policy gates, and audit.
- [Agno AgentOS](../../agentic-systems/agno-agentos.md) separates agent/team loops, workflow control flow, a service control plane, recovery, and builder authority.
- [Exo](../../agentic-systems/exo.md) separates a protected substrate from a rewritable executor and exposes the boundary of self-modification.
- [Autogenesis](../../agentic-systems/autogenesis.md) contrasts versioned mutation and rollback with weaker evidence that a change deserved commitment.

The theory base supplies candidate explanations rather than a ready schema:

- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) gives the binding resource pressure.
- [LLM frameworks should keep the tool loop optional](../../notes/llm-frameworks-should-keep-the-tool-loop-optional.md) exposes the host-ownership boundary.
- [Agent orchestration occupies a multi-dimensional design space](../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) identifies independent orchestration choices.
- [Agent orchestration needs coordination guarantees](../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) asks what prevents composed-agent failure modes.
- [Runtime structure determines governance control surfaces](../../notes/runtime-structure-determines-governance-control-surfaces.md) connects architecture to intervention and audit.
- [Diagnostic richness constrains outer-loop learning quality](../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) separates outcome selection from evidence for the next improvement.
- [Scenario decomposition drives architecture](../../notes/scenario-decomposition-drives-architecture.md) supplies the requirement-derivation method used here.

## Next analytical decision

The next session should choose whichever unresolved distinction most changes the map, then test it against several unlike systems. Good candidates include the common-floor boundary, control plane versus cross-cutting governance, or runtime versus builder-plane separation. The evidence should determine the first path; this workshop does not prescribe an order.
