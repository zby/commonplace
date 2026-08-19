# Workshop: Agent Runtime Design

## Question

What must an agent runtime provide to turn bounded model calls into governable, long-lived work? Which state, effects, guarantees, and control operations belong to the runtime, and which must it expose to a CLI, TUI, API client, or host application?

## Why this workshop exists

The agent-memory work established a useful sequence: start from what future work needs, derive requirements and boundaries, and only then turn the stable comparison lens into a review type and writing workflow. Its durable results now include [Designing a Memory System for LLM-Based Agents](../../notes/designing-agent-memory-systems.md), the [agent-memory requirements](../../notes/agent-memory-requirements/README.md), the [agent-memory-system review type](../../agent-memory-systems/types/agent-memory-system-review.md), and the [review-writing skill](../../instructions/write-agent-memory-system-review/SKILL.md).

Agent-runtime coverage has reached the point where the same move is useful. [`kb/agentic-systems/`](../../agentic-systems/README.md) contains code-grounded analyses of execution loops, orchestration APIs, context assembly, sub-agent coordination, permission boundaries, durable state, recovery, and self-modification. Those analyses do not yet share a requirements-derived review contract. The collection contract already says that a mature methodology should follow the memory collection's path.

This workshop develops that methodology. It does not begin by standardizing the current reviews. First it must determine what work an agent runtime is responsible for, distinguish the runtime from its clients and surrounding application, and identify which differences support fair comparison across unlike systems.

## Working boundary

For this workshop, the **agent runtime** is the operational system that turns model judgments into situated work across time. Its starting decomposition is [scheduler, context engine, and execution substrate](../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md), but that is a hypothesis to test rather than a fixed definition. Runtime policy, durable run state, delegation, recovery, and event protocols may require sharper treatment.

A **runtime client or interface** lets a person or application operate that system. It can configure and start work, project runtime state, carry steering and authority decisions back into execution, and expose interruption or recovery controls. A TUI, CLI, API callback, organizational policy service, or headless runner can play this role. Runtime and client may share one process without becoming the same architectural responsibility.

User approval is the forcing case for the boundary. An effect may remain pending until policy or a person grants or denies authority. The first working thesis is that [capability requests and scoped grants are the clean interface for this decision](./capabilities-are-the-clean-interface-for-user-approval.md). The runtime derives and enforces the request; a client presents an unresolved decision and returns the answer.

Approval also exposes a deeper runtime requirement: the dependent effect must remain blocked while the operational system either retains a continuation or ends with typed pending work that can be re-entered later without replaying the effect. The recent [recursive-agent architecture ingest](../../sources/jdegoes-recursive-agent-architecture-2081854216264392934.ingest.md) makes the durable case explicit through pending work, effect guarantees, recovery, and capability-bounded enforcement.

Memory-system internals remain covered by [`kb/agent-memory-systems/`](../../agent-memory-systems/README.md); this workshop asks what runtime contract consumes memory and makes its consequential state or controls available. A builder or improvement plane that changes the runtime must also be distinguished from the runtime version currently executing work.

## Current working material

- [Question map](./question-map.md) — initial scenarios, pressure areas, comparison tests, and open questions.
- [Capabilities are the clean interface for user approval](./capabilities-are-the-clean-interface-for-user-approval.md) — first working thesis: capability requests, policy, scoped grants, correlated pending-decision resolution, and the bidirectional runtime-client protocol.
- [Runtime minimality is a protected waist, not a small feature list](./runtime-minimality-is-a-protected-waist-not-a-small-feature-list.md) — second working thesis: protect cross-cutting invariants while letting the model author run-local symbolic control programs, and reserve runtime self-modification for durable self-generated changes to the runtime's own organization.
- [Pi subprocess subagents expose an approval-routing choice](./pi-subprocess-subagents-expose-an-approval-routing-choice.md) — pinned baseline evidence: Pi assigns child tool allowlists but does not route child effect approvals to the parent UI, exposing operator attention and escalation as comparison questions rather than settled requirements.
- [Provisional agent-runtime review protocol](./agent-runtime-review-protocol.md) — code-grounded source-inspection procedure and fixed evidence-and-boundary spine, with conditional lenses for execution, authority, approval, delegation, dynamic extension, recovery, and control.
- [Review-protocol pilot: Pi, Swamp, and Exo](./review-protocol-pilot-pi-swamp-exo.md) — first test across a small coding runtime, a durable distributed automation plane, and a reflective self-modifying system.
- [Dynamic-extension mechanism pilot](./dynamic-extension-mechanism-pilot.md) — compares RLM programs, Claude Code's workflow subsystem, Tendril capabilities, and llm-do callables without treating those mechanisms as peer runtimes; separates artifact persistence from later activation.
- [Provisional agent-runtime requirements map](./agent-runtime-requirements-map.md) — derives mandatory review records, a candidate common floor, conditional requirement bundles, and externalization contracts from the first two pilots.
- [Code-grounded runtime pilot: Fractal and llm-do](./fractal-llm-do-code-grounded-runtime-pilot.md) — traces two runtime-facing systems with explicit externalized boundaries, tests the common-floor and approval requirements, and separates conversational continuity, process-local state, durable continuation, and later extension activation.
- [Code-grounded boundary pilot: PydanticAI and DSPy](./pydantic-ai-dspy-code-grounded-boundary-pilot.md) — tests an embedded inner runtime and a host-language computation library, broadens approval to terminal deferral and re-entry, and establishes target classification as a substantive review result.
- [Agentic systems collection](../../agentic-systems/README.md) — current heterogeneous evidence base.
- [Agent runtime decomposition](../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) — starting component model, not a fixed conclusion.
- [Bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) — starting account of symbolic scheduling around semantic calls.
- [Agent orchestration occupies a multi-dimensional design space](../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — warning against ranking runtimes on one ladder.
- [Runtime structure determines governance control surfaces](../../notes/runtime-structure-determines-governance-control-surfaces.md) — starting account of how architecture constrains intervention and audit.
- [Your Old Agent Architecture Is Dead… Meet Its Replacement](../../sources/jdegoes-recursive-agent-architecture-2081854216264392934.ingest.md) — argument that approval and irreversible work require durable suspension and effect guarantees from the execution substrate.

## Possible graduated artifacts

The analysis may earn some or all of these artifacts:

- a synthesis note explaining the agent-runtime boundary and the requirements that follow;
- a small requirements inventory, split only where individual requirements are useful on their own;
- a code-grounded `agent-runtime-review` type for `kb/agentic-systems/`;
- a local skill for writing or updating agent-runtime reviews;
- a comparison matrix or survey if repeated controlled fields prove useful.

These are possible outputs, not a required package. In particular, the workshop should not create a review schema until the fields discriminate real systems and change an architectural judgment.

## Working conventions

- Derive requirements from concrete work stories and observable failures, not feature catalogues.
- Keep unconditional requirements separate from scenario-dependent capabilities.
- Record separately what the runtime implements, what a client exposes, what policy decides, and what remains with the user or host application.
- Separate protected runtime mechanisms from extensible execution policies. Record authorship, persistence, and change target independently: generated ephemeral code, externally authored durable extensions, durable generated capabilities, and runtime self-modification are different cases.
- Make commit-pinned code inspection the primary evidence for runtime ownership, wiring, alternate paths, and enforcement claims. Use focused tests or first-hand operation for deployment behavior that static inspection cannot establish. Documentation-only and closed-source evidence may generate questions or support a mechanism analysis, but does not by itself validate the code-grounded review contract.
- Keep memory-system internals out of scope while recording the runtime-side memory contract.
- Treat current review headings as evidence about useful questions, not as a schema to preserve.
- Use **harness** only when preserving a source's own terminology; use **agent runtime** for the architectural object studied here.

## What closes the workshop

The workshop closes when it has:

1. a requirements map grounded in several materially different work stories and their failure modes;
2. a clear boundary among model, runtime, runtime client or interface, host application, memory subsystem, and builder or improvement plane;
3. a comparison lens tested against heterogeneous systems in the current collection, including at least one interactive runtime, one durable or distributed runtime, and one self-modifying or builder-oriented system;
4. an explicit account of which requirements are general, conditional, or externalized;
5. durable conclusions promoted to the appropriate library collections.

If those conclusions support a stable review type and writing skill, promote them too. If they do not, record why a shared methodology would erase important differences. Then remove this workshop and its entry from the active-workshop index.
