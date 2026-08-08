# PydanticAI and DSPy: Code-Grounded Runtime-Boundary Pilot

## Purpose and evidence basis

This pilot tests the lower boundary of the provisional review method. It is not a ranking of two peer runtimes. PydanticAI is an embedded agent-runtime library that owns an inner model/tool loop while leaving the outer application lifecycle to its caller. DSPy is primarily a host-language programming library; its `ReAct` module contains an agentic loop, but the package does not thereby become the enclosing operational runtime.

**PydanticAI evidence basis:** `pydantic/pydantic-ai` at commit [`4be0d648c1a5ddbc127a4ba2407f9af7587812fe`](https://github.com/pydantic/pydantic-ai/tree/4be0d648c1a5ddbc127a4ba2407f9af7587812fe), captured 2026-08-07. Inspection covered `Agent` and `AgentRun`, graph and tool execution, deferred tools, approval-required toolsets, UI adapters, durable-execution integrations, and the Temporal human-in-the-loop test. A focused test invocation did not start because the local Snap environment lacked a required `snap-confine` capability, so the assessment uses source and checked-in tests rather than a new behavioral result.

**DSPy evidence basis:** `stanfordnlp/dspy` at commit [`b967c3e9ef9987cfe763f62b4d76930fd9073e32`](https://github.com/stanfordnlp/dspy/tree/b967c3e9ef9987cfe763f62b4d76930fd9073e32), captured 2026-08-07. Inspection covered `Module`, `Predict`, `LM`, `ReAct`, `Tool`, settings, callbacks, parallel execution, and program serialization. No model calls or repository tests were run. The pilot therefore establishes code paths and ownership boundaries, not provider behavior or deployment isolation.

## The two targets sit on different sides of the runtime boundary

| Role | PydanticAI | DSPy |
|---|---|---|
| Bounded model call | Provider-backed `Model` invoked inside the agent graph | `LM` called through an adapter by `Predict` |
| Runtime-owned control | `AgentRun` executes a per-invocation graph from prompt through model requests, tool calls, and `End` | No package-wide operational lifecycle; a host-authored `Module.forward` is an ordinary Python call |
| Agentic mechanism | The ordinary `Agent` path | Optional modules such as `ReAct` implement a bounded local model/tool loop |
| Client | Caller coroutine or API; optional UI adapters project events and deferred requests | The calling Python program |
| Host-owned work | Outer lifecycle, persistence, deployment, authorization, isolation, and composition among agents | Entry, composition, effects, policy, persistence, client, isolation, and lifecycle |
| Durable owner | Optional Temporal, DBOS, or Prefect integration plus its external engine and host workflow | None for run state; module/program serialization persists artifacts rather than executions |

The distinction is not about code size. PydanticAI creates an addressable execution object with legal graph transitions and terminal results. DSPy's basic contract is callable composition. A repository can also straddle the boundary: DSPy core remains a programming library while `ReAct` is a runtime-like mechanism whose guarantees stop at that module's call.

## PydanticAI owns the inner run, not the outer service

`Agent.iter()` constructs an internal graph for one invocation, and `AgentRun` exposes its nodes, history, result, events, cancellation, and manual advancement. A host can inspect, mutate, or skip the next node before calling `next()`. Completion is explicit: the result becomes available after the graph reaches `End` ([`run.py`](https://github.com/pydantic/pydantic-ai/blob/4be0d648c1a5ddbc127a4ba2407f9af7587812fe/pydantic_ai_slim/pydantic_ai/run.py#L30-L38), [`run.py`](https://github.com/pydantic/pydantic-ai/blob/4be0d648c1a5ddbc127a4ba2407f9af7587812fe/pydantic_ai_slim/pydantic_ai/run.py#L394-L470)).

The caller supplies the prompt, prior messages, dependencies, models, toolsets, capabilities, usage limits, and optional identifiers for each run. The library assembles them into the graph state and tool manager. It does not own the service process, user identity, storage, or the policy that decides which caller may ask for which effect. This is deliberate embedding, not an incomplete implementation of a universal client.

The manual graph interface also prevents a simple “library owns the loop” versus “host owns the loop” dichotomy. PydanticAI owns the transition semantics of its inner graph, but the host may drive that graph and always owns the sequence of invocations around it. A review should identify both horizons.

## Approval can end one run and re-enter through another

PydanticAI's approval path starts on the declared Agent tool surface. A tool may always require approval, or may raise `ApprovalRequired` after inspecting validated arguments and run context. The approval-required toolset refuses to call its wrapped tool until `ctx.tool_call_approved` is true ([`approval_required.py`](https://github.com/pydantic/pydantic-ai/blob/4be0d648c1a5ddbc127a4ba2407f9af7587812fe/pydantic_ai_slim/pydantic_ai/toolsets/approval_required.py#L15-L31)). The tool executor catches the exception and collects the call as unapproved rather than executing it ([`_tool_execution.py`](https://github.com/pydantic/pydantic-ai/blob/4be0d648c1a5ddbc127a4ba2407f9af7587812fe/pydantic_ai_slim/pydantic_ai/_tool_execution.py#L689-L725)).

The resulting `DeferredToolRequests` contains validated tool calls with unique tool-call identifiers. There are then two resolution modes:

1. An inline handler returns `DeferredToolResults`. The executor validates and feeds those results back through the ordinary tool pipeline, and the same run continues.
2. Unresolved requests become the run's terminal output. The caller later starts a new run with the prior message history and `DeferredToolResults`. The new run has a fresh `run_id`; `conversation_id` correlates the related runs ([`deferred-tools.md`](https://github.com/pydantic/pydantic-ai/blob/4be0d648c1a5ddbc127a4ba2407f9af7587812fe/docs/deferred-tools.md#L14-L21), [`_tool_execution.py`](https://github.com/pydantic/pydantic-ai/blob/4be0d648c1a5ddbc127a4ba2407f9af7587812fe/pydantic_ai_slim/pydantic_ai/_tool_execution.py#L917-L1003)).

The second mode is not a suspended coroutine or a paused process. The dependent effect is blocked because the first run ends without executing it. Waiting and later re-entry are asynchronous at the application level. This is the important correction to the workshop's earlier synchronous-approval intuition: the dependency is synchronous, but the enclosing operational system need not stay blocked or alive.

The request is structured and correlated, but it is not yet the workshop's full capability-grant record. It carries a tool name, validated arguments, call identifier, and optional metadata; it does not establish a universal principal, effect class, target scope, lifetime, or limit. PydanticAI also warns that approval submitted with client-controlled history is sign-off against model action, not authorization against an untrusted client. Endpoint authentication and authorization inside the consequential tool remain necessary ([`deferred-tools.md`](https://github.com/pydantic/pydantic-ai/blob/4be0d648c1a5ddbc127a4ba2407f9af7587812fe/docs/deferred-tools.md#L91-L106)).

This source also exposes a vocabulary collision. PydanticAI calls composable cross-cutting run behaviors **capabilities**. The workshop uses **capability** in the authority sense: an unforgeable or policy-recognized right to perform a scoped effect. A review must establish the semantics of the source term rather than inferring authority from its name.

## Durable waiting is supplied by a workflow host

PydanticAI's core protocol provides typed deferred requests and results that a compatible host can serialize and use for re-entry; serializability still depends on their contents and the host's serializer. The library does not itself persist the pending decision. The optional durable integrations route model and tool operations through an external workflow engine, but the application must still define the outer human-in-the-loop workflow.

The checked-in Temporal test demonstrates the division. Consumer workflow code retains message history, pending requests, and results; marks itself `waiting_for_results`; waits on a Temporal condition; and accepts results through a workflow signal before calling the agent again ([`test_temporal.py`](https://github.com/pydantic/pydantic-ai/blob/4be0d648c1a5ddbc127a4ba2407f9af7587812fe/tests/test_temporal.py#L3408-L3480)). The test is evidence that the core deferral protocol composes with durable waiting. It is not evidence that every PydanticAI agent has durable approvals, duplicate-decision handling, or in-flight effect reconciliation.

This is a legitimate externalization because the boundary is concrete: PydanticAI supplies typed pending work, tool-call correlation, history, and re-entry; the durable host supplies storage, client reconnection, wait state, and signals. A review still has to inspect the host implementation before attributing AP5 or DR1–DR3 to a deployed system.

## DSPy core is host-language computation

A DSPy `Module` is a composable program whose author implements `forward`. Calling the module directly invokes that Python method; asynchronous calling invokes `aforward`. Usage tracking and callbacks wrap the call, but there is no runtime-owned run object or legal lifecycle beyond ordinary call and exception semantics ([`module.py`](https://github.com/stanfordnlp/dspy/blob/b967c3e9ef9987cfe763f62b4d76930fd9073e32/dspy/primitives/module.py#L40-L129)).

`Predict` gives a model call a typed semantic projection. It selects an explicit or configured `LM`, formats signature inputs through an adapter, and returns a `Prediction` ([`predict.py`](https://github.com/stanfordnlp/dspy/blob/b967c3e9ef9987cfe763f62b4d76930fd9073e32/dspy/predict/predict.py#L141-L165), [`predict.py`](https://github.com/stanfordnlp/dspy/blob/b967c3e9ef9987cfe763f62b4d76930fd9073e32/dspy/predict/predict.py#L250-L275)). The host can put arbitrary computation and effects before, after, or inside that call. Those actions do not “bypass the DSPy runtime,” because the core package does not claim to govern the host program in the first place.

Module state or a complete program can be saved and loaded. JSON state preserves parameters; whole-program and pickle forms may execute arbitrary code and therefore require a trusted-source decision ([`base_module.py`](https://github.com/stanfordnlp/dspy/blob/b967c3e9ef9987cfe763f62b4d76930fd9073e32/dspy/primitives/base_module.py#L156-L178), [`base_module.py`](https://github.com/stanfordnlp/dspy/blob/b967c3e9ef9987cfe763f62b4d76930fd9073e32/dspy/primitives/base_module.py#L254-L277)). This is program-artifact persistence, not durable run state, approval recovery, or runtime self-modification.

## DSPy `ReAct` is an agentic module with direct host-callable effects

`ReAct` is the narrower surface on which runtime questions become meaningful. It asks a `Predict` module to select a tool, invokes the corresponding host callable, appends the result or formatted exception to a trajectory, and repeats up to `max_iters` before extracting a final prediction ([`react.py`](https://github.com/stanfordnlp/dspy/blob/b967c3e9ef9987cfe763f62b4d76930fd9073e32/dspy/predict/react.py#L16-L88), [`react.py`](https://github.com/stanfordnlp/dspy/blob/b967c3e9ef9987cfe763f62b4d76930fd9073e32/dspy/predict/react.py#L95-L149)).

The `Tool` wrapper validates JSON-schema-shaped arguments and then directly calls or awaits the supplied function ([`tool.py`](https://github.com/stanfordnlp/dspy/blob/b967c3e9ef9987cfe763f62b4d76930fd9073e32/dspy/adapters/types/tool.py#L120-L147), [`tool.py`](https://github.com/stanfordnlp/dspy/blob/b967c3e9ef9987cfe763f62b4d76930fd9073e32/dspy/adapters/types/tool.py#L177-L200)). Callbacks observe starts, results, and errors, but they are not an enforcement boundary. If a `ReAct` tool deletes a file, DSPy validates its arguments and calls it; an approval or isolation layer must wrap the callable or constrain the process. If an ordinary `Module.forward` performs the same effect directly, even `ReAct`'s tool observation is outside the path.

This is not a defect relative to DSPy's host-language programming contract. It does mean that a product embedding `ReAct` cannot infer effect mediation, approval, isolation, run durability, or a user control plane from DSPy alone.

## Requirements test

| Candidate | PydanticAI embedded Agent path | DSPy core and `ReAct` | Pilot finding |
|---|---|---|---|
| CF1 addressable execution and explicit outcomes | Strong for one `AgentRun`, including run and conversation identifiers, graph end, events, result, and cancellation | Core exposes call/result/exception rather than runtime identity; `ReAct` adds a bounded trajectory but no operational run lifecycle | Keep CF1 for systems that claim operational execution. Do not impose it on a returning computation merely because it calls a model. |
| CF2 bounded semantic-call projection | Explicit per run, although caller-owned history and deployment limits remain external | Strong at `Predict` signature/adapter boundary; host program composition remains ordinary Python | Keep CF2 at every bounded model call, while naming whether the runtime or host constructs it. |
| CF3 mediated action/result boundary | Strong for declared Agent function-tool paths, including deferred execution; host Python, direct model APIs, and some provider paths remain separate boundaries | `ReAct` owns a model-to-tool-to-observation path but directly executes host callables; ordinary `Module.forward` effects are fully host-owned | CF3 applies only to actions the reviewed operational surface claims to govern. It is externalized, not vacuously satisfied, when arbitrary host code owns effects. |
| CF4 client-fitted control and observation | Embedding API is the primary client boundary; optional UI adapters add interactive projections | Ordinary function API; no claimed runtime client | Keep CF4, but accept a host API as the client boundary and do not require a shipped TUI. |
| CF5 guarantees cover every exposed path | Essential: Agent, direct model APIs, manual graph control, UI adapters, and durable variants have different guarantees | Essential as an attribution rule: `ReAct` guarantees do not extend to arbitrary host modules | Keep CF5. It prevents both library-wide overclaiming and treating a nested module as the entire runtime. |
| IT1 termination and resources | Conditional; limits, retries, tool configuration, and cancellation exist, while whole-host resources remain external | `ReAct` has `max_iters`; ordinary `Module` computation is host-bounded | Keep conditional on iterative, recursive, concurrent, or costly execution. |

PydanticAI activates AP1 and AP3 on its deferred-tool path, but only partially meets the workshop's stronger forms. AP1 has a structured, correlated tool request without a complete scoped authority record. AP3 blocks the dependent effect and supports either inline resolution or terminal deferral plus correlated re-entry. It does not promise that a live continuation remains suspended. AP5 and DR1–DR3 require a durability-owning host; the Temporal test is an example composition, not a base-library guarantee.

DSPy core does not activate the approval requirements. A host that supplies consequential `ReAct` tools activates authority questions at that product's enclosing boundary. `ReAct` itself supplies neither approval nor authorization, but the review should report that fact as an externalization or a gap according to the enclosing product's claims, not score DSPy as a failed durable agent service.

Neither target establishes subagent principals, authority attenuation, durable generated extensions, a builder admission loop, or runtime self-modification. DSPy optimizers and saved programs belong to a host-invoked builder/artifact plane unless a larger system wires generation, admission, later discovery, and activation.

## Method conclusions

1. **The review target is an operational surface, not a repository.** A repository may expose returning model computations, nested agent loops, optional clients, and durable integrations with different owners. The review must name which one it evaluates.
2. **Boundary classification can be a substantive result.** DSPy core should not receive a completed agent-runtime review that presents missing durability, approvals, or client controls as deficiencies. It can receive a mechanism analysis, or be reviewed as one component of a product that owns those responsibilities.
3. **Embedded ownership can be nested.** PydanticAI owns the inner graph and its tool semantics; its host owns the outer sequence of runs, persistence, user relationship, and deployment. “Who owns the loop?” needs a horizon.
4. **Approval blocks an effect dependency, not necessarily an execution process.** Inline awaiting and terminal deferral with later re-entry are two valid shapes. Durability is a separate property of the waiting owner.
5. **Approval is not authorization.** A human sign-off record may protect against unintended model action while remaining forgeable by an untrusted client or too weakly scoped to authorize the effect.
6. **Externalization needs a protocol, not a callback-shaped hole.** PydanticAI's typed request/result/history re-entry is enough to compose with a durable host. The host must still be inspected for persistent identity, duplicate decisions, client recovery, and effect reconciliation.
7. **Source vocabulary does not establish semantics.** PydanticAI “capabilities” are composable behavior hooks; workshop capability grants concern authority. A code-grounded review must inspect construction and enforcement.

## Protocol and map revisions earned by the pilot

- Add an early target-classification step. When a package does not own an operational lifecycle, review its nested mechanism or enclosing host without manufacturing a deficient-runtime comparison.
- Record both inner-run and outer-application ownership for embedded libraries.
- Broaden AP3 from live suspension to correlated pending-decision resolution. The invariant is that the dependent effect does not execute without a resolution; the implementation may await inside one run or end with typed pending work and start another.
- Record approval/sign-off separately from authorization and environmental confinement.
- Treat package-specific uses of `capability` as untrusted vocabulary until the code shows authority semantics.
- Attribute optional durable integrations only to the wired runtime-plus-host path. An example or adapter proves composability, not a deployment guarantee.

## Next code-grounded tests

1. Trace an approval request across client and process loss, including cancellation, timeout, duplicate response, and a crash near effect commitment.
2. Trace concurrent children with insufficient authority to test parent routing, unrelated progress, and bounded operator attention.
3. Trace a generated composite whose effects become known only during execution.
4. Trace a generated artifact through restart, admission, discovery, activation, rollback, and retirement.
5. Test an untrusted-reader role that must not receive or indirectly reach a high-authority capability.
6. Give the compact protocol to an independent reviewer and test whether target classification, ownership, and guarantee judgments reproduce.
