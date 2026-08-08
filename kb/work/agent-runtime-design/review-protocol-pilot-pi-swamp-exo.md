# Review-Protocol Pilot: Pi, Swamp, and Exo

## Purpose and evidence

This pilot applies the [provisional review protocol](./agent-runtime-review-protocol.md) to three unlike systems. It tests the comparison method; it does not replace or refresh the existing library reviews.

- **Pi:** first-hand source inspection of `badlogic/pi-mono` at `fc3554e16defffcf76553b1bd12f676adf26d0a4` (2026-08-06), recorded in the [Pi subprocess-subagent baseline](./pi-subprocess-subagents-expose-an-approval-routing-choice.md).
- **Swamp:** the existing [code-grounded Swamp analysis](../../agentic-systems/swamp.md), pinned to `cf38c4ec1068613bb7d3432eb74a1ad854156dd7` (2026-07-18). This pilot did not refresh its source checkout.
- **Exo:** the existing [code-grounded Exo analysis](../../agentic-systems/exo.md), pinned to `ef4cfe057af02955a73c85beb6ab79e253253114` (2026-07-29). This pilot did not refresh its source checkout.

The selection deliberately spans a small interactive coding runtime, a durable distributed automation control plane, and a reflective runtime whose agent generates durable changes to its own executor.

## Boundary summaries

### Pi

Pi's minimal `agent` package owns a model/tool loop, per-agent state, streaming events, cancellation, steering, and tool preflight. The `coding-agent` package adds sessions, tools, extensions, clients, and interactive or headless modes. Subagent orchestration is an example extension that launches more Pi processes; it is not a protected core primitive.

The claimed center is interactive and programmable coding-agent execution. The child-process example supports isolated model contexts and tool-name assignment, but not durable child sessions or child-to-parent approval routing.

### Swamp

Swamp places the open-ended coding agent outside its execution kernel. The agent interprets intent and authors typed models or declarative workflows. Swamp owns validation, deterministic DAG scheduling, policy checks, secret resolution, distributed dispatch, persisted execution state, reports, and audit.

Its center is repeatable operational automation rather than a general conversational agent loop. Remote workers are execution workers, not subagents with independent semantic judgment. Treating them as equivalent would erase the system's main boundary.

### Exo

Exo separates a protected Rust substrate from a rewritable TypeScript executor. The substrate owns identity, ordered events, artifacts, secrets, bindings, and sandbox lifecycle. The executor owns prompts, model calls, tool policy, memory, and context handling. The agent may rewrite the executor and install or remove capabilities through managed surfaces; the default policy withholds the substrate.

Its center is long-running reflective self-modification: the agent authors changes to its executor and tools, and accepted changes persist into later operation. The protected-versus-rewritable boundary matters more than conventional subagent orchestration, which the reviewed revision does not implement despite broader cloning language in overview documents.

## Cross-system runtime map

| Role | Pi | Swamp | Exo |
|---|---|---|---|
| Semantic judgment | Model calls inside each Pi agent | External coding agent at authoring time; optional AI-backed methods | Model calls in the rewritable executor |
| Protected execution owner | Agent loop and coding-agent session machinery | Workflow orchestrator, policy services, data and worker control plane | Rust harness and sandbox/event substrate |
| Client or control surface | TUI, CLI/JSON, SDK and extension UI | CLI/API/control protocol, workflow commands, reports | Adapter/client surfaces plus operator CLI and agent tools |
| Symbolic strategy | Host and extension code; ordinary model tool loop | Typed model methods, CEL, and declarative DAGs | Rewritable executor, prompts, tools, adapters, and source changes |
| Durable state | Sessions in the coding-agent; subagent example disables child sessions | Persisted workflow, approval, data, report, and audit state | Ordered event files, artifacts, update records, snapshots, git |
| Builder plane | Trusted extension and SDK code | Agent-authored definitions and extensions plus registry lifecycle | Agent edits executor and tools, rebuilds, restarts, and may roll back |

The map discriminates immediately. “Runtime” names a tool loop in Pi, a deterministic automation kernel in Swamp, and a protected reflective substrate plus mutable executor in Exo. A review type that assumes every runtime owns a conversational loop would misclassify Swamp. One that ignores the builder plane would miss Exo's defining architecture.

## Execution, context, and state

### Pi

Pi's loop is explicit and small. It streams an assistant response, validates and preflights tool calls, executes them sequentially or in parallel, records results, and continues until no more calls or queued messages remain. Each `Agent` receives its own message and tool arrays. The subagent extension adds process-level context separation but starts children with `--no-session`, so that example treats child work as one headless invocation rather than durable delegated state.

Context assembly and compaction are replaceable coding-agent/session policies over the smaller core. This is evidence for a narrow waist, but the trusted extension environment remains broad.

### Swamp

Swamp replaces a conversational loop with a persistent state machine. Weighted DAG scheduling, dependencies, conditions, concurrency bounds, nested workflows, scheduled triggers, and approval gates advance without another model judgment. Context is typed operational state and CEL-resolved data rather than a prompt assembled for every transition.

The protocol therefore needs to ask what state reaches the next computation, not assume that every runtime has an LLM context engine. Swamp's answer is largely symbolic dataflow; the external coding agent has its own context boundary outside Swamp.

### Exo

Exo's protected substrate records ordered events and artifacts while the mutable executor decides prompt assembly and model/tool policy. The reviewed executor materializes the full conversation on each model round and has a round-trip bound but no implemented history window or compaction. Long-running state survives through events, artifacts, sandbox state, update records, and git rather than through a compact conversational state alone.

The protocol must therefore distinguish durable canonical state from the projection currently loaded into a model. Exo can preserve a failed attempt even when it rewinds the filesystem that attempt changed.

## Effects, grants, and isolation

### Pi

Pi can enforce a per-session allowlist over registered tool names, including dynamically registered tools. That is meaningful dispatch enforcement. It does not by itself constrain absolute filesystem paths, the effects reachable through Bash, inherited process environment, or the ambient authority of extension code. Capability surface, grant set, and isolation envelope are therefore visibly different.

### Swamp

Swamp has the clearest policy/control-plane separation of the three. Grant decisions match principals, actions, resources, and conditions. Remote method code receives capability-like proxy adapters while the orchestrator retains secrets, state, data, and audit. Worker isolation remains a deployment property: fleet placement or containerization establishes the outer envelope.

### Exo

Exo exposes broad sandboxed shell authority plus named host-control tools. Tool profiles select visible action sets, while `manage_tool` stages and validates durable capability installation. The docs explicitly treat loading a tool as a trust decision rather than a security boundary. The sandbox and withheld Rust substrate form the stronger envelope; the exact protected boundary is also configurable policy.

This comparison validates the three-layer authority record. A single “permissions” field would collapse Pi's tool dispatch, Swamp's principal/resource policy, and Exo's sandbox/profile/trusted-tool boundary.

## Approval and operator attention

Pi's core can await an asynchronous preflight hook before executing a tool. Its shipped subagent example does not route a child's unresolved request to the parent UI: children are headless and their stdin is ignored. The parent may confirm use of a project-local agent definition, which is a separate trust decision. The case exposes direct prompting, parent-brokered escalation, and preassigned headless authority as distinct possibilities.

Swamp models approval as a durable workflow gate. The run records a gate token and suspends until a human command or model method decides it, after which execution resumes. This is not a tool-call confirmation inside a child agent. It is an explicit state-machine step with runtime-owned provenance.

The existing Exo review does not establish a general live user-approval protocol for agent effects. It establishes profiles, named control tools, operator-only commands, sandbox policy, and trust decisions around installed code. The correct pilot value is therefore **not established**, not an inference that Exo has no approval or that every action is automatically allowed.

The lens discriminates, but it is conditional. Approval may be an inline effect decision, a durable workflow state, a preconfigured authority envelope, or outside the reviewed boundary. Reviews should describe routing and attention consequences rather than treating prompt count as a security score.

## Delegation, workers, and extension horizons

Pi's subagent example launches independent semantic workers. Agent Markdown supplies a prompt, model, and optional tool names; the extension owns parallelism, chaining, cancellation, and result aggregation. Authority insufficiency has no structured escalation protocol. Pi's ordinary extensions are deployment-lifetime trusted code, even though tools can be registered dynamically during a session. This is not capability-bounded model-authored guest execution.

Swamp dispatches deterministic method code to disposable remote workers. Workers receive extension bundles and capability proxies but do not own the repository, vault configuration, or orchestration state. Agent-authored definitions and workflows are durable symbolic artifacts admitted before repeated execution. This is not a subagent context tree and not run-local model-written orchestration.

Exo's distinctive extension path satisfies the authorship and durability conditions of runtime self-modification: changes are generated by the agent and accepted changes remain operative after rebuild and restart. They also target the executor and its capability machinery rather than an external work product. The agent can edit the executor, install managed tools, modify adapters, rebuild, restart, and retain or roll back the result. Staging, schema checks, exact source pins, atomic replacement, build, and tests constrain admission, while usefulness and behavioral-regression oracles remain weak. Cloning or subagent lineage is not implemented at the reviewed revision.

The four extension horizons are useful, but the pilot adds an important distinction: **agent-authored declarative automation** is neither merely a run-local guest program nor necessarily runtime self-modification. Reviews must record authorship, operative lifetime, and change target. Generated but ephemeral RLM-style code is dynamic execution. Durable but externally authored runtime code is an extension. Only durable self-generated change to the bounded runtime's own organization qualifies as runtime self-modification.

## Reliability, recovery, and observation

Pi provides event streaming, abort signals, tool completion, session persistence in the coding-agent layer, and process cancellation in the subagent example. The example does not preserve a child continuation across process loss or approval because child sessions are disabled and no nested approval channel exists.

Swamp persists workflow transitions, outputs, approval state, cancellation, remote data operations, reports, and audit records. Its runtime boundary is built for reconnect and repeated operation. Correctness of the coding agent's original semantic interpretation remains outside those deterministic guarantees.

Exo records each attempt in an append-oriented event substrate, separates update requests from guardian-driven restart, retains failed update records, and can rewind sandbox state without erasing the history of what failed. Its strongest recovery property is reflective: the next version can inspect the failed attempt. Its acceptance oracle does not yet establish that a mechanically valid rewrite improves agent judgment.

The protocol must keep operational recovery separate from task correctness and behavioral improvement. All three systems can expose a successful terminal state while supporting very different claims about what that success means.

## Pilot findings about the protocol

The pilot supports these parts of the protocol:

1. **Boundary mapping must be mandatory.** It prevents a general tool loop, a workflow control plane, and a reflective substrate from being treated as three sizes of the same product.
2. **Claimed work must select the depth of review.** Durable gates matter centrally to Swamp; child approval routing matters to Pi; protected mutation and oracle reach matter to Exo.
3. **A fixed spine with flexible sections is preferable to uniform headings.** The stable information recurs, but the explanatory structure differs.
4. **Capability surface, grant set, and isolation envelope must remain separate.** Each system places real control at a different layer.
5. **Implemented wiring must be separated from available hooks and documented claims.** Pi's example extension, Swamp's external coding agent, and Exo's unimplemented cloning claim make this distinction load-bearing.
6. **Externalized is not the same as missing.** Swamp intentionally leaves semantic interpretation to a coding agent; Pi extensions intentionally own some orchestration; Exo intentionally leaves judgment-quality evaluation incomplete while protecting recovery mechanics.
7. **Approval needs an operator-attention dimension.** The relevant question is not only whether execution can block, but which principals can interrupt the user and how unresolved child authority is surfaced.
8. **Completion requires a local definition.** Model stop, workflow completion, committed effects, successful restart, and verified improvement are different outcomes.

The pilot also exposes cautions:

- The scheduler/context-engine/execution-substrate decomposition is useful for Pi and Exo but needs translation for a symbolic workflow engine such as Swamp. “Context engine” may mean typed state projection rather than prompt assembly.
- A delegation section must distinguish semantic subagents, deterministic workers, and cloned successor systems.
- Dynamic extension needs authorship, lifetime, and change-target fields in addition to language and API shape.
- Approval and durable suspension should remain conditional requirements until more work stories are tested.
- The protocol remains too broad to turn every lens into a required section or controlled frontmatter field.

## Follow-up test

The [dynamic-extension mechanism pilot](./dynamic-extension-mechanism-pilot.md) follows this pilot by stressing online model-authored symbolic execution. It first corrects the comparison boundary: RLM programs, Claude Code workflows, Tendril capabilities, and llm-do callables are mechanisms within operational systems, not peer runtimes. The pilot tests guest-language restrictions, capability construction, run-state journaling, model-authored control flow, and promotion into durable reusable behavior.

The [provisional requirements map](./agent-runtime-requirements-map.md) now derives candidate requirements from both pilots. Only after those requirements are tested against further enclosing runtimes should the workshop decide which findings belong in a completed-review type contract and which belong only in the writing skill's investigation procedure.
