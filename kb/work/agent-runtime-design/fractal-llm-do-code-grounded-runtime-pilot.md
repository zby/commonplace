# Code-Grounded Runtime Pilot: Fractal and llm-do

## Purpose and evidence basis

This pilot tests the [provisional review protocol](./agent-runtime-review-protocol.md) and [requirements map](./agent-runtime-requirements-map.md) against two operational runtime products rather than isolated feature mechanisms. It traces their source-visible runtime and client paths and records load-bearing responsibilities externalized to dependencies. Fractal's PredictRLM and SBX implementations were not inspected, so the pilot does not claim code-grounding for behavior inside those dependencies.

- **Fractal:** first-hand source inspection of `Trampoline-AI/fractal` at commit [5954a07d](https://github.com/Trampoline-AI/fractal/commit/5954a07d464feeaf6c311a9fa5ca2e54200a6794), covering the CLI/TUI, runtime, session store, agent adapter, event hooks, documentation, and focused tests. No tests or live model calls were run because the checkout lacks the `predict-rlm` dependency.
- **llm-do:** first-hand source inspection of `zby/llm-do` at commit [d86c6868](https://github.com/zby/llm-do/commit/d86c686813ec569f1d688ee6948919ff6d0022bb), covering the runtime and call scopes, project linker, CLI/TUI, approval wrappers, built-in toolsets, dynamic agents, documentation, and focused tests. No live model calls were run. A local focused-test attempt could not import `pydantic_ai`, so no test result is claimed.

This is a methodology pilot, not a replacement for the existing [Fractal system analysis](../../agentic-systems/fractal.md). Its evidence is stronger than the earlier mechanism comparison because both targets have commit-pinned source and their own runtime and client paths can be inspected. Dependency-owned behavior remains `not established` unless the inspected runtime enforces or tests the boundary itself.

## Architectural characterization

Fractal is a local coding runtime around PredictRLM and an SBX interpreter. It owns the interactive and headless clients, workspace/session identity, turn persistence, context assembly, status translation, and event projection. PredictRLM owns the model-authored Python loop and recursive model calls; SBX owns the default execution environment. Fractal therefore makes an RLM operational without implementing the whole RLM or isolation substrate itself.

llm-do is a process-local Python orchestration runtime over PydanticAI. A project manifest links declarative agents and trusted Python into one registry and selects either an agent or Python function as the entry. The runtime owns nested call scopes, registry-backed tool and agent dispatch, depth limits, usage and message collection, event callbacks, and approval wrapping for toolsets. Its clients provide interactive or headless operation. Dynamic agents are one runtime toolset, not the runtime itself.

The systems place their main control boundary differently. Fractal owns session and client continuity around a dependency-owned generated-program executor. llm-do owns a common nested-agent dispatcher and call-scoped toolset wrapper while deliberately letting trusted host Python own arbitrary orchestration.

## Runtime map

| Role | Fractal | llm-do |
|---|---|---|
| Semantic judgment | PredictRLM's primary and recursive model calls | PydanticAI agents selected from the linked registry |
| Runtime-owned mechanism | Session/turn lifecycle, context projection, status handling, event forwarding | Runtime registries, call frames, nested dispatch, depth limit, toolset approval wrapping, events and usage |
| Client | Interactive TUI and headless CLI share `FractalRuntime.submit()` | TUI and headless CLI share `Runtime.run_entry()` through UI adapters |
| Host or dependency | PredictRLM, supplied interpreter, SBX/Docker, mounted host workspace | Project linker, manifest-listed trusted Python, PydanticAI, tool implementations, deployment environment |
| Retained state | Workspace-keyed JSON sessions outside the workspace; summary plus recent detailed history | Process-local runtime state; TUI can pass top-level message history into the next turn |
| Dynamic/builder path | PredictRLM generates run-local Python; Fractal retains bounded recent traces but exposes no promotion path | Model creates declarative `.agent` files and registers them in the current runtime; no later automatic discovery |

This map prevents two boundary errors. Fractal's sandbox and recursive program semantics cannot be inferred from its session wrapper alone. llm-do's generated-agent tool cannot stand in for trusted entry Python, direct tools, built-in provider tools, or the whole client/runtime path.

## Forcing traces

### Fractal: effectful coding turn

The client creates or resumes a `FractalRuntime`, then `submit()` writes a pending user turn before calling the agent. The agent constructs a PredictRLM signature from workspace instructions, the user message, an always-visible rendered summary, and recent exact history. It mounts the workspace and any included directories at their host paths and invokes one `PredictRLM.acall()` ([runtime.py](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/src/fractal/runtime.py), [agent/service.py](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/src/fractal/agent/service.py), [agent/signature.py](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/src/fractal/agent/signature.py)).

The generated Python is taught to use filesystem and subprocess APIs. When PredictRLM's runtime-hook interface is available, Fractal requests hooks over selected file and subprocess calls. File-read and command events become session-history facts; hook-derived modified paths do not become the persisted `changed_files`, and the retained PredictRLM trace is a separate dependency result. The hooks do not return an authority decision and no Fractal branch denies or suspends the effect. They mediate observation, not authorization ([agent/skills.py](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/src/fractal/agent/skills.py), [events.py](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/src/fractal/events.py)). The effective ceiling is therefore supplied by SBX and the mount configuration. Source inspection of Fractal establishes the direct mutable mounts, but not SBX's network, secret, or process guarantees.

On completion, Fractal records `succeeded`, `failed`, `max_iterations`, or `interrupted`, the response, hook-derived session-history facts, a dependency-provided trace, and the model-returned `changed_files`. The changed-file list is not reconciled against the observed file events or filesystem state. The runtime can truthfully report its own turn outcome while its account of committed workspace effects remains model-reported.

### Fractal: interruption and later resume

Ctrl-C in the TUI marks the active turn as interrupted and cancels its task. `submit()` persists `interrupted` and any available trace before re-raising. A later turn can continue if the dependency leaves the interpreter usable. That recovery relies on a PredictRLM contract rather than a Fractal continuation protocol.

Explicit `resume(session_id)` reloads prior JSON state and makes it context for a new turn ([session.py](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/src/fractal/session.py)). It does not re-enter an in-flight transition. Pending tool calls, effect commitment, legal next commands, and approval decisions are not durable state. The word *resume* therefore means conversational continuation, not workflow continuation.

### llm-do: nested agent and approval

`Runtime.run_entry()` creates a depth-zero call context and invokes the selected entry. `CallContext.call_agent()` checks the maximum depth, creates a child frame with fresh messages and the selected toolsets, then awaits the child agent ([runtime.py](https://github.com/zby/llm-do/blob/d86c686813ec569f1d688ee6948919ff6d0022bb/llm_do/runtime/runtime.py), [context.py](https://github.com/zby/llm-do/blob/d86c686813ec569f1d688ee6948919ff6d0022bb/llm_do/runtime/context.py), [call.py](https://github.com/zby/llm-do/blob/d86c686813ec569f1d688ee6948919ff6d0022bb/llm_do/runtime/call.py)). The child receives a new conversational state but shares process-local registries, approval policy, usage, and event sinks.

Each agent call wraps its declared toolsets with the same approval callback. In TUI prompt mode, that callback emits a request and awaits a decision queue. The dependent coroutine stops at the tool call; the event loop and UI remain able to process the answer ([approval.py](https://github.com/zby/llm-do/blob/d86c686813ec569f1d688ee6948919ff6d0022bb/llm_do/runtime/approval.py), [ui/runner.py](https://github.com/zby/llm-do/blob/d86c686813ec569f1d688ee6948919ff6d0022bb/llm_do/ui/runner.py)). Headless execution cannot prompt and must select an approve-all or reject-all policy.

The runtime does not persist the request, continuation, or session approval cache. A process loss erases them. It also does not attach a runtime-owned run/call identifier or parent chain to the approval request; the TUI labels requests with the entry name. The implementation therefore proves awaited local suspension, not durable or parent-correlated approval.

The approval path is not universal. Agent toolsets are wrapped, while direct `AgentSpec.tools`, server-side built-in tools, and trusted Python entry code follow other paths ([agent_runner.py](https://github.com/zby/llm-do/blob/d86c686813ec569f1d688ee6948919ff6d0022bb/llm_do/runtime/agent_runner.py), [project/entry_resolver.py](https://github.com/zby/llm-do/blob/d86c686813ec569f1d688ee6948919ff6d0022bb/llm_do/project/entry_resolver.py)). This is compatible with a deliberately trusted host boundary. It is not compatible with an unqualified claim that the runtime intercepts every effect an LLM can cause.

### llm-do: dynamic agent creation and restart

The `dynamic_agents` toolset separates three policy points. Its own policy marks `agent_create` approval-required unless the enclosing toolset configuration has already pre-approved or blocked it. Creation writes a declarative `.agent` file, reparses it, resolves requested tools and toolsets only from the host registry, and registers the resulting `AgentSpec` in `Runtime.dynamic_agents`. `agent_call` has an independent configurable approval policy, pre-approved by default, and dispatches through the ordinary `call_agent()` path. Any toolset used by the child is then independently approval-wrapped ([dynamic_agents.py](https://github.com/zby/llm-do/blob/d86c686813ec569f1d688ee6948919ff6d0022bb/llm_do/toolsets/dynamic_agents.py)). Creation, invocation, and nested effect authority are therefore distinct in the shipped implementation even when policy pre-approves a point.

The file may survive the process, but operative registration does not. A new `Runtime` starts with an empty dynamic-agent map, and normal project linking discovers manifest-listed files rather than the generated directory. There is no generate → admit → restart → discover → activate lifecycle. This is model-authored artifact retention with runtime-local activation, not durable operative extension or runtime self-modification.

## Requirements test

| Candidate | Fractal | llm-do | Pilot finding |
|---|---|---|---|
| CF1 addressable execution and explicit outcomes | Strong for session and turn identity with explicit terminal statuses; a cancelled task outside the UI path can leave `pending` | Partial: agent name and depth label events, but there is no invocation/run identifier or durable terminal-state protocol | Keep CF1. The pilot shows why agent name, conversational session, invocation identity, and terminal outcome must not be conflated. |
| CF2 bounded semantic-call projection | Partial: inputs are explicit and detailed history is capped, but the rendered cumulative summary has no established size bound | Partial: instructions, tools, child frames, and message history are explicit, but no source-established size, provenance, or reconstruction bound | Keep CF2, but reviews should distinguish explicit projection from an enforced bound. |
| CF3 mediated action/result boundary | Partial/externalized: hooks observe selected effects; SBX owns the ceiling; changed files are model-reported | Gap for a universal governed surface: toolsets use the approval wrapper, while direct tools, built-ins, and trusted entry Python do not | Keep CF3. Mediation must name its declared surface and alternative paths; it need not mean human approval. |
| CF4 client-fitted control and observation | Implemented for local TUI/headless turns, interruption, and conversational resume | Implemented for process-local TUI/headless runs and interactive approval; no reconnect or resume claim | Keep CF4. Required commands and durability depend on the claimed client story. |
| CF5 guarantees cover every exposed path | Partial: shipped clients converge on `submit()`, but interpreter injection changes the deployment envelope | Gap for universal approval claims; valid if the guarantee is explicitly narrowed to approval-aware toolsets | Keep CF5 as an assessment rule. It forces a review to state the scope of a guarantee rather than treating an alternate path as a feature omission. |

The conditional requirements remain conditional. Fractal does not implement an unresolved-authority path, so AP1–AP5 do not apply to its current claimed interaction model; its lack of approval becomes consequential only for work that requires runtime-mediated authority decisions. llm-do's shipped TUI in `prompt` mode activates AP1–AP3. It partly meets them, but its request is tool-shaped rather than a full principal/effect/scope capability request. Raw `Runtime` instances default to `approve_all`, and AP4 remains conditional and untested because the trace did not establish concurrent multi-principal routing. There is no durable AP5 path. Neither system claims durable runs, so DR1–DR3 should be recorded as outside the work story rather than scored as universal defects.

Delegation also needs scoped wording. Fractal passes a recursive sub-model to PredictRLM but does not implement child identity, authority projection, joins, or escalation in its own source. llm-do implements fresh child messages, selected agent surfaces, a depth ceiling, and ordinary awaited result/error propagation. It does not implement durable child identity, independent lifecycle, parent-correlated escalation, cancellation reconciliation, or a distributed worker protocol.

## What the code-grounded focus changes

The pilot supports making code-grounded inspection the primary basis for this review methodology.

1. **The operational boundary becomes visible.** Source imports and constructors show that Fractal owns sessions while PredictRLM and SBX own generated execution and containment. Documentation alone makes that division easier to blur.
2. **Alternative execution paths become visible.** llm-do's toolset wrapper, direct tools, provider built-ins, and trusted Python entries have different governance semantics. A feature description of “approvals” would hide the scope.
3. **Persistence can be traced through activation.** Both systems retain something across time, but Fractal reloads conversational state and llm-do writes an agent file without rediscovering it. Neither fact establishes durable workflow continuation or durable operative extension.
4. **An awaited decision can be described without declaring the whole runtime synchronous.** llm-do suspends the dependent tool-call coroutine while the UI continues. Durability, unrelated progress, and restart recovery are separate properties.
5. **Claims can stop at the actual enforcement boundary.** Fractal's hook visibility is not policy enforcement; direct workspace mounts are not an admitted change set; llm-do registry resolution constrains declarative dynamic agents but does not sandbox trusted Python.

Code-grounded does not mean source-only. Live probes remain necessary for deployment properties such as sandbox escape resistance, event loss, interrupt cleanup, and concurrent approval behavior. The methodological rule should be: use pinned code to establish ownership, wiring, alternate paths, and claimed invariants; use focused tests or operation to challenge properties that static inspection cannot establish. Documentation-only and closed-source evidence may still generate questions or describe a mechanism, but should not by itself validate the code-grounded review contract.

## Protocol and map revisions earned by the pilot

- Keep RR1–RR8 and the fixed evidence/boundary spine. Both reviews needed every record even though their discriminating sections differed.
- Require load-bearing runtime claims to identify the exact enforced surface. “Tool calls require approval” is underspecified when only one tool representation is wrapped.
- Record continuity objects separately: conversational history, top-level-run state, runtime-instance state, process-external artifacts, durable run continuation, and later extension activation.
- In AP3, treat local awaited suspension, unrelated concurrency, and durable continuation as separate facts. Blocking the dependent effect is necessary; blocking the entire process is not.
- In DG1, distinguish a fresh model context from a distinct durable principal. llm-do has the former without a durable child identity protocol.
- In EX2, distinguish call-local, top-level-run-local, runtime-instance-local, and process-external artifact lifetime. “Session-local” is too ambiguous for the observed dynamic-agent registry.
- Preserve CF3 and CF5, but make their declared-surface qualification prominent. A runtime may deliberately trust its host entry path; the review must not silently extend a tool-plane guarantee to it.

## Subsequent code-grounded tests

The [PydanticAI–DSPy boundary pilot](./pydantic-ai-dspy-code-grounded-boundary-pilot.md) completed the first two tests identified here. It showed that an embedded library may own an inner run while externalizing the outer lifecycle, and that the lower-bound “pure runtime” candidate was more accurately classified as a returning computation library. CF3 is not vacuously satisfied there; situated effects belong to the host unless a nested agentic mechanism claims them.

The remaining tests are:

1. Trace an open-source runtime with a durable pending approval across client and process loss. Force approval, denial, timeout, cancellation, duplicate response, and a crash near effect commitment.
2. Trace concurrent children requesting authority to test principal identity, parent routing, unrelated progress, and bounded operator attention.
3. Trace a generated artifact through restart, discovery, admission, activation, rollback, and retirement. Retained bytes alone should continue to fail EX5.

The next methodology step is not to add more headings. It is to turn these code traces into a compact review-writing procedure, then test whether independent reviewers can reproduce the same boundary and guarantee judgments.
