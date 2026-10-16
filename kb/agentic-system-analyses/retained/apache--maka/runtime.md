---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Apache Maka runtime baseline: Host-admitted model/tool turns, boundary controls, delegated and durable work, and plugin capability admission at the frozen commit."
run-id: AAS-2026-10-15-maka-4a8b73e41579-01
reviewed-boundary: "1751c399239b0f6b717e98e2a5e2b875c3dd11ce"
---

# Apache Maka runtime report

## Runtime account

### Evidence and claimed work

The [boundary](boundary.md) fixes the whole-system scope and SRC-1. This account adds implementation inspection of the CLI send/resume path, Host backend selection and composition, main tool settlement, Code Mode nesting, filesystem and Bash boundaries, child creation, Graph supervisor admission, scheduled firing, recovery, plugin installation/composition and plugin model/executor seams. All source anchors below refer to SRC-1 at the frozen revision. These are source findings, not supplied execution traces. No target code, tests, models or experiments were run. Activation, recovery success, isolation in deployment, task success and benefit remain unobserved.

Maka claims task completion at measured cost and an event-ledger-centered runtime; [RT-CLM-task-runtime](#rt-clm-task-runtime) retains the claim. This report establishes executable paths, not the README's comparative benchmark claim. The boundary identifies Desktop, TUI, CLI, ACP, bots and Eval as shipped clients. The end-to-end path inspected here is noninteractive CLI; client-specific native IPC, bot authentication, peer transport and Eval verifier correctness are not established by that path.

### Ordinary invocation: CLI request to a terminal answer

A user supplies text, a workspace and a model target. The CLI connects to the Host, checks readiness, and creates a Host-backed session driver. It attaches to a session, waits for optional MCP readiness, calls `preparePrompt`, requires a Run identity, and observes the resulting Turn. Session, Turn and Run are separate identities, not interchangeable request labels. Resume queries the Host for a resume plan; stop targets the active Turn and optionally its Graph. These implementation findings are SRC-1, `packages/cli/src/runtime-host-run-command.ts`, particularly the send/resume path retained in [RT-RTE-cli-turn](#rt-rte-cli-turn).

The Host's backend registry supplies `ai-sdk` and `plugin-executor` preparations. For ordinary `ai-sdk` work it resolves the connection, credentials, model, proxy transport and current runtime-policy snapshot, then constructs a prompt/tool composer. This is not a fixed bundled model: [RT-CMP-ai-model](#rt-cmp-ai-model) describes the numerical component and version limits. The composer combines personalization, skill advertisements, workspace instructions, memory projection and optional plan/side-conversation material. Base prompts are cached per Session/Turn; scoped plugin contributions can be sampled at logical step boundaries. Bound tool lists and profiles constrain the composed surface. SRC-1, `packages/runtime-host/src/server/execution-composition.ts`, `packages/runtime-host/src/server/execution-model-composition.ts`, and `packages/runtime-host/src/server/interactive-run-composer.ts` provide the implementation evidence.

The model owns the proposed next text/tool action under natural-language instructions; code owns dispatch, context projection, tool availability and termination. The model's output is not itself execution authority. The turn loop resolves returned calls against the active tool map, sends unavailable calls through an invalid-tool fallback, settles a batch, waits for durable consumption and builds the continuation from durable events rather than raw returned objects. Limits, abort, permission handoff, yielding, terminal provider errors or a tool-free completion can end progression. Retries are bounded at a provider-step seam; an aborted stream is not silently treated as success. SRC-1, `packages/runtime/src/ai-sdk-turn.ts`; [RT-RTE-tool-settlement](#rt-rte-tool-settlement).

The executor is the selected tool implementation, filesystem worker, shell process or client/provider adapter. Its effects can leave the conversation and mutate files or external systems. Runtime events and AgentRun state are the durable execution authority; the CLI is an observer, not the sole retained transcript. Context projection can remove large tool bodies or replace history with a checkpoint before the next provider request; [RT-RTE-context-projection](#rt-rte-context-projection) distinguishes this from plain accumulation. Terminal output is a classified Turn outcome and model answer/events, not an independent proof that the requested task was accomplished. SRC-1, `packages/runtime/src/ai-sdk-turn.ts`, `packages/runtime-host/src/server/execution-model-composition.ts`, and `packages/cli/src/runtime-host-run-command.ts`.

### Load-bearing controls and forcing cases

Four forcing families test the tempting but overbroad claim that all effects have one uniform sandbox/approval boundary.

1. **Nested tools and client callbacks.** Code Mode nested calls re-enter `ToolRuntime.settleToolCall`, whereas client-capability calls require a preparation seam and a live boundary/mode check. In the actual guard, `ask` can reach preparation without an already-Bypass boundary; therefore the diagnostic phrase “require Bypass” alone is not a complete description. The remote/client preparation and execution contract remains necessary. [RT-RTE-tool-settlement](#rt-rte-tool-settlement).
2. **External executors and direct plugin model calls.** A plugin executor is an alternate backend, not another main-loop tool. It delegates text, cwd and optional instructions/configuration to a binding and converts returned events; it explicitly does not expose Maka sandbox-boundary requests. A plugin LLM adapter can also supply generation without entering the main model/tool loop. These defeat a universal claim about local tool-ledger or sandbox coverage. [RT-RTE-executor-plugin](#rt-rte-executor-plugin).
3. **Delegation and Graph control.** Child sessions have separate contexts, durable spawn identities and catalog-bound tools; executor-backed children instead have an empty local tool list. Graph supervisor wakes are separately admitted with Graph/wake/attempt identities and required durability. This is not just one foreground transcript with a different prompt. [RT-RTE-child-graph](#rt-rte-child-graph).
4. **Scheduled and recovered work.** A stored task can trigger an AgentRun without a new foreground user message; the scheduler binds execution identities, checks its connection entity and rechecks before root admission. Recovery validates admitted input and ledger identity rather than merely replaying whatever a UI last displayed. [RT-RTE-durable-wake](#rt-rte-durable-wake).

| Guarantee and owner | Enforcement and strength | Covered paths and counterpath | Required external contract | Conclusions |
|---|---|---|---|---|
| Durable continuation before further local tool effects; main turn loop/ToolRuntime | Durable current-run read before settlement; durable attempt preparation before implementation invocation. **protocol** | Main AI-SDK returned tools and Code Mode nested settlement; not arbitrary plugin implementation I/O or external-executor internals | Stores must enforce append/read/attempt semantics and report failures honestly | implementation conclusion status: wired; operation conclusion status: uninspected |
| Managed file/command containment; filesystem executor and Bash tool | Managed filesystem refuses a missing worker; inspected Bash branch refuses missing required command sandbox. **invariant** for those fail-closed branches, not a deployment guarantee | Built-in filesystem and inspected executor Bash path; Bypass deliberately uses host scope; external workspace and client tools have different effect envelopes | Worker, sandbox manager, OS and injected executor must enforce the passed profile | implementation conclusion status: wired; operation conclusion status: uninspected |
| Boundary expansion is explicit; ToolRuntime and Host interaction authority | Normalize expansion, require nonempty justification, prohibit concurrent negotiation, durable settlement; denial closes further negotiation/finalizes turn. **protocol** | Maka boundary-request surface and plugin approval service forwarding; external plugin executor explicitly excludes that surface | Correct Host interaction ownership, user/client response and storage settlement | implementation conclusion status: wired; operation conclusion status: uninspected |
| Composed tool ceiling; interactive composer | Bound lists suppress dynamic additions and deferred groups; runtime policy can remove subagent tools. **invariant** within composition | Child/local bound tool surfaces, not host-process plugin code or provider internals | Tools must honor their execution contracts; model prompt obedience is not required to reject an unavailable tool | implementation conclusion status: wired; operation conclusion status: uninspected |
| Durable desired plugin authority precedes convergence; Host plugin platform | Store replace precedes runtime recovery; unknown commit fences mutation. **protocol** | Inspected composition apply/install; a successful receipt need not mean every entry activated | Package loader, store and plugin lifecycle must obey commit/disposal contracts | implementation conclusion status: wired; operation conclusion status: uninspected |

The witnesses for these controls are in the linked route records. Capability surface, current grants and deployed isolation are different: tool catalogs say what can be offered; live session boundary and permission reads say what this dispatch can request; the OS/worker/client/external executor determines where effects really run. No deployed grant snapshot or OS trace was supplied. In particular, code passing an `ExecutionBoundary` to `tool.impl` is not by itself universal enforcement of that boundary.

### Change admission and remaining coverage

Maka admits capability and prompt-surface changes through package installation and desired composition edits, not only through source releases. [RT-RTE-plugin-admission](#rt-rte-plugin-admission) records proposal, rejection and recovery roles. Workspace files can also be changed through authorized tools, and subsequent prompt composition reads workspace instructions; these two implemented capabilities must not be mistaken for a dedicated, evaluated self-revision loop. The inspected code does not establish an exercised self-improvement claim. Memory extraction, local-memory editing, recall/import and assistant-maintained knowledge are retained-state mechanisms reserved for the memory analyst; their composer/backend entry points are visible here but their admission semantics are not inferred.

Remaining included but uninspected mechanisms are material limits, not exclusions or absences: assistant heartbeat/Matters/index maintenance, detailed goal/daily-review execution, Graph scheduling and manual update policies beyond supervisor admission, MCP server internals and full MCP adaptation, managed shell-run/PTY internals beyond the inspected Bash branch, computer-use/native client implementations, ACP executor protocol internals, platform-specific native workers, package-loader trust verification, and release/build acceptance. They prevent a universal security, recovery, capability-enumeration or change-admission conclusion. No provider training, provider-native tool execution or remote worker internals were available as frozen implementation. The four forcing families establish architectural differences, not an exhaustive audit of every adapter.

## Shared records

### Components

#### RT-CMP-ai-model
Label: Configured AI model

The component is the `getAIModel` result selected from the Host's resolved connection/model. Its representational form is distributed-parametric; weights are held by a provider/local serving endpoint, not by the inspected Host composition. SRC-1, `packages/runtime-host/src/server/execution-model-composition.ts`, constructs the model factory, the history-summary model and provider options from the same target. Provider-internal substrate and embedding/training provenance are uninspected.

> const contextWindow = resolveSelectedModelContextWindow(target.connection, target.model);
> --- `packages/runtime-host/src/server/execution-model-composition.ts`

Parameter changes during operation: uninspected at the serving implementation; this composition performs inference and contains no weight-update mechanism in the inspected construction path. Exact weight version pinned: not established by a configured model string. Mutable endpoint resolving to another model: possible under an external endpoint/alias contract; Maka's connection/model identity does not certify a weight digest. The same limits apply to the summary model constructed here. Plugin adapters and external executors can select additional opaque models; their actual numerical components are uninspected, not assumed identical to this component. Implementation conclusion status: wired. Operation conclusion status: uninspected.

### Operative objects

#### RT-OBJ-run-composition
Label: RunComposition baseline

Source-native `RunComposition` is symbolic metadata: composer identity/revision, source revisions, prompt/tool/provider hashes, tool names and context window. It is recorded through the Host's AgentRun-facing callback, separate from dynamic request epochs. It records what was composed, not whether a model followed its content. The storage handoff is inspected; physical on-disk layout is not established here. SRC-1, `packages/runtime-host/src/server/execution-model-composition.ts`.

> // RunComposition remains the immutable C0 baseline. Dynamic Tool changes
> // belong exclusively to RequestComposition epochs, so never re-sample them
> // while committing the baseline immediately before provider dispatch.
> --- `packages/runtime-host/src/server/execution-model-composition.ts`

This object supplies execution lineage, not a formulated theory or a learned parameter update. Its consumer is later request/run inspection and authority plumbing; the conditional commit callback preserves the distinction between an available recording seam and a proven deployed artifact.

### Routes

#### RT-RTE-cli-turn
Label: Host-backed CLI Turn

Endpoints are user text → CLI connection/session driver → Host Turn → event observation. The user proposes the task; CLI code selects the configured target and readiness gate; Host owns execution. The operating mode is open task requests, with optional bounded `maxSteps` and Graph orchestration, not a curriculum. No answer oracle is used by this CLI route. SRC-1, `packages/cli/src/runtime-host-run-command.ts`.

> if (!turn.runId) throw new Error('Runtime Host did not return a Run identity');
> --- `packages/cli/src/runtime-host-run-command.ts:325-350`

- Immediate return: An async event stream classified against the admitted Session/Turn/Run; terminal answer and outcome are delivered to the CLI.
- Later read-back: Resume queries a Host plan and resumes the latest eligible Turn; durable context projection is separate from the CLI's current observer state.
- Delegated visibility: Graph mode can observe graph completion; child contents are not implicitly copied by this CLI send method.
- Selection predicate: Attached session and explicit target/model, readiness, optional resume plan and step limit.
- Invalidation or expiry: Stop/cancel targets the active Turn and optionally Graph; closing the context cancels observation waiters.
- Activation or effect: Host-backed execution is wired; successful task completion is not observed.
- Evidence limits: The inspected client is CLI, not proof of equivalent desktop/bot/ACP presentation or authorization.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-tool-settlement
Label: Main and nested tool settlement

Endpoints are provider-returned call → active-tool lookup → ToolRuntime guards/attempt → tool implementation → durable result → next provider step. Host/runtime code decides eligibility; the model proposes name/arguments. Context includes immutable dispatch identities, current boundary/mode, cwd, abort signal, output/progress callbacks and limited child/interaction capabilities. Tool arguments/results are symbolic structures with natural-language payloads; arbitrary executable tool code is not a policy language enforced by that structure. SRC-1, `packages/runtime/src/ai-sdk-turn.ts` and `packages/runtime/src/tool-runtime.ts`.

> throw new Error('durable current-run reader is required for tool continuation');
> --- `packages/runtime/src/ai-sdk-turn.ts:2183-2183`

> const invokeTool = () =>
>   preparedExecution
>     ? preparedExecution.execute(toolContext)
>     : tool.impl(structuredClone(executionArgs) as never, toolContext);
> --- `packages/runtime/src/tool-runtime.ts`

The Code Mode callback uses the same settlement boundary, with nested call and parent-operation identities:

> origin: 'code_mode',
> parentToolCallId: context.toolCallId,
> --- `packages/runtime/src/ai-sdk-turn.ts`

Deferred tools are callable only after a step-start availability snapshot admits them. Repeated identical failures can be blocked; this is a recovery heuristic, not proof of eventual progress. Provider-executed calls are explicitly rejected in the inspected main loop, so that rejection cannot be generalized to all provider/adapter paths. Client capabilities have a distinct preparation gate:

> : clientCapabilityBoundary.kind !== 'bypass' && clientCapabilityPermissionMode !== 'ask'
>   ? CLIENT_CAPABILITY_BOUNDARY_MESSAGE
> --- `packages/runtime/src/tool-runtime.ts`

For built-ins, SRC-1, `packages/runtime/src/filesystem-executor.ts` separates managed worker, host-local Bypass, external workspace and embedding default. The managed missing-worker branch throws rather than silently choosing host execution:

> 'Managed filesystem execution is unavailable because the sandboxed worker cannot be enforced.',
> --- `packages/runtime/src/filesystem-executor.ts`

SRC-1, `packages/runtime/src/builtin-tools.ts` checks the analogous missing required command sandbox before its executor Bash invocation. Boundary-request negotiation in `packages/runtime/src/tool-runtime.ts` normalizes proposed expansion and requires justification. Computation proposes the expansion; the external interaction responder can deny; Host storage settles it. `packages/runtime/src/plugin-approval-service.ts` forwards plugin requests to that same callback. A denial triggers finalization, not an automatic broader retry. This is capability-grant admission, not proof of human approval for every file/tool operation. The CLI surface inspected above only exposes denial response. Other approval UI ownership remains uninspected.

- Immediate return: Settled result/error and event facts; nested Code Mode receives bounded settlement results.
- Later read-back: Subsequent provider requests reconstruct authoritative current-run events; retained history/context replacements are handled by the projection route.
- Delegated visibility: Tool context exposes explicit child spawn/list/output capabilities; Code Mode sees only its snapshot of active nestable tools.
- Selection predicate: Active name map, schema validation, deferred-step activation, repeat-failure gate, subagent capacity and applicable live execution-boundary checks.
- Invalidation or expiry: Abort, yield, tool unavailability, boundary denial/finalization and per-cell limits can stop further work; a grant is read from live authority rather than inferred from discovery.
- Activation or effect: Tool implementation can mutate the host, sandbox, injected workspace or client environment; these are distinct envelopes. No effect trace was supplied.
- Evidence limits: Passing context to arbitrary plugin code does not enforce all of its I/O. OS containment and client preparation are external contracts; main-loop provider-executed rejection is not a system-wide provider guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-executor-plugin
Label: Plugin executor and LLM alternatives

The Host registry selects a binding by stored executor ID and constructs `PluginExecutorBackend`; this is distinct from AI-SDK tool settlement. SRC-1, `packages/runtime-host/src/server/execution-composition.ts` and `packages/runtime/src/plugin-executor-backend.ts`. Its owner is the plugin binding for execution, and Maka for conversion/acknowledgement. Inputs include text, cwd, conversation/session identity, Turn/Run, optional model/configuration/instructions and attachments. The operating mode is delegated open work; no reference-answer oracle is established.

> throw new Error('Plugin executor does not expose Maka sandbox-boundary requests');
> --- `packages/runtime/src/plugin-executor-backend.ts`

The backend acknowledges only after its terminal event is accepted; a failed acknowledgement can call abandonment. That is an uncertainty protocol, not a claim that an external side effect was rolled back. The separate plugin LLM service requires an invocation, combines cancellation, selects a visible supporting adapter by priority if a model is requested, otherwise invokes the Host model runtime. SRC-1, `packages/runtime/src/plugin-llm-service.ts`:

> if (adapter) return adapter.generate(effectiveInput, invocation);
> return this.runtimeBinding.get().generate(effectiveInput, invocation);
> --- `packages/runtime/src/plugin-llm-service.ts`

The Host default model binding is visible in `packages/runtime-host/src/server/execution-composition.ts`; a custom adapter's telemetry, model fixity and effect restrictions are not inherited merely from the default.

- Immediate return: Executor events and terminal result converted to Maka's event stream; direct LLM calls return text/model ID/optional finish reason to the plugin.
- Later read-back: Executor conversation key is the Session ID; actual external retained context/checkpoints are binding-owned and uninspected. Maka acknowledgement/abandonment preserves uncertainty at the adapter boundary.
- Delegated visibility: Binding receives only explicitly passed input; invocation-scoped LLM adapters are selected through visible plugin scope.
- Selection predicate: Stored executor ID/binding for the backend; adapter support and priority or Host fallback for LLM generation.
- Invalidation or expiry: Dispose/stop aborts active executions and waits for settlement; binding retirement/invalidation is wired in Host composition, while remote cancellation effectiveness remains unknown.
- Activation or effect: Calls can reach external model/executor machinery outside ToolRuntime; no execution evidence establishes actual effects or model compliance.
- Evidence limits: External ACP/Codex/executor internals, provider-native tools and adapter parameter state remain uninspected; local sandbox and durable-tool-attempt guarantees cannot be projected through these seams.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-child-graph
Label: Child contexts and Graph wakes

The foreground model proposes child work through catalog tools; SessionManager verifies an active parent Run and reads the parent's boundary/policy before creating a durable child. Agent definitions determine profile, prompt and tools; worktree profiles provision a separate workspace. Executor-backed children use the executor path instead of local tools. SRC-1, `packages/runtime/src/session-manager.ts`, `packages/runtime-host/src/server/child-agent-composition.ts` and `packages/runtime/src/subagent-tools.ts`.

> const resolvedToolNames = executorId
>   ? []
>   : await this.resolveChildToolNames(parentSessionId, parentHeader, definition);
> --- `packages/runtime/src/session-manager.ts`

Child context is deliberately not a cloned parent transcript or implicit memory projection. SRC-1, `packages/runtime-host/src/server/interactive-run-composer.ts`:

> 'The child does not implicitly inherit local Memory or personalization context; required background must be included explicitly in the task.',
> --- `packages/runtime-host/src/server/interactive-run-composer.ts`

Children preserve parentRun/parentTurn/tool-call lineage, request fingerprints and initial child Turn/Run IDs. A post-creation check closes the cancelled-parent race. Output is explicitly readable, including bounded final committed model text; worktree patch publication is a separate path located but not fully traced. Separate child contexts keep intermediate work out of the caller window; only selected output crosses back. This resembles an isolated work frame, but the child session is durable and independently addressable, so it is not a disposable stack frame.

Graph supervisor work has a separate gate and origin contract. SRC-1, `packages/runtime-host/src/server/agent-graph-execution-coordinator.ts`:

> kind: 'agent_graph_supervisor_wake',
> graphId: origin.graphId,
> wakeId: origin.wakeId,
> attemptId: origin.attemptId,
> --- `packages/runtime-host/src/server/agent-graph-execution-coordinator.ts`

The coordinator checks currency before admission and again through an admission callback; conflicts wait for idle, and runtime sends require durability. Open delegated tasks and asynchronous Graph supervision are separate modes. Code can reject stale/cancelled parent or wake identities. Neither model child output nor Graph result status establishes an answer oracle; no reference-answer comparison is established here.

- Immediate return: Child readiness/output handles and eventual child result; Graph coordinator returns a classified terminal supervisor outcome.
- Later read-back: Durable child metadata/spawn identity supports later child-output reads; complete Graph history reuse policies remain uninspected.
- Delegated visibility: Explicit task/definition/workspace/tool ceiling; child memory and personalization are not implicitly inherited. Parent can explicitly list/read children.
- Selection predicate: Catalog profile and available tools/executor, active parent Run, boundary/policy and Graph current-wake checks.
- Invalidation or expiry: Parent cancellation checks, abort, stale wake rejection and Graph/root stop; child durable records can remain inspectable after rejection.
- Activation or effect: Separate model context and possibly worktree/external executor can perform delegated effects; no supplied trace establishes task decomposition success.
- Evidence limits: Manual Graph edit/scheduling policy, swarm coordination details, external child executor internals and patch admission remain uninspected; inheritance prose alone does not prove all constraints.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-durable-wake
Label: Scheduled admission and recovery

A persisted scheduled fire, not a new foreground human input, triggers either notification, session resume or new AgentRun work. The coordinator owns fire identity and admission; it validates a bound connection entity, selected model and stored execution template. SRC-1, `packages/runtime-host/src/server/scheduled-task-coordinator.ts`:

> if (!authorizeConnectionModel(resolved.connection, execution.model)) {
>   throw new Error('ScheduledTask model is no longer enabled');
> }
> --- `packages/runtime-host/src/server/scheduled-task-coordinator.ts`

The scheduler rechecks connection immediately before root admission, binds Session/Turn/Run/user-message IDs to the fire, and supplies task intent body as content. This is recurring/stored-request execution, not evidence of an autonomous improvement curriculum. No answer oracle is used in the inspected firing branch. Task authoring/update authority and human content approval are uninspected; starting a scheduled workflow does not establish approval of all later generated content.

Recovery is a second admission consumer, not blind transcript replay. SRC-1, `packages/runtime-host/src/server/hosted-execution-recovery.ts`, checks duplicated user-message identities, execution-specific queue/message contracts, logical handoff membership and scheduled authority before deciding replay versus recovery closure:

> 'ScheduledTask recovery admission has no canonical authority validator',
> --- `packages/runtime-host/src/server/hosted-execution-recovery.ts`

- Immediate return: A fire settlement saying notified/started/failed, not necessarily completed task success; recovery produces replay/closure plans.
- Later read-back: Stored fire execution identities and root admissions are consumed on later recovery; stored task intent supplies a later invocation.
- Delegated visibility: New runs receive explicit stored task body and execution template; notification effects can reach local or configured messaging channels.
- Selection predicate: Claimed scheduled fire, effect kind, resumable session or authorized bound connection/model; recovery checks admission/message identity and execution contract.
- Invalidation or expiry: Disabled/changed connection or unauthorized model rejects work; stale/inconsistent durable evidence can stop recovery. Task editing/expiry policies are not traced here.
- Activation or effect: Notification or Host root admission is wired; actual delivery, replay and crash recovery success are unobserved.
- Evidence limits: Fire admission is not final agent success; assistant proactive maintenance and the complete scheduler/calendar semantics are uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### RT-RTE-context-projection
Label: Effective history and compaction

Endpoints are durable runtime history → projection transitions/checkpoint validation → provider-visible messages. Runtime code chooses oversized tool-result archive candidates and validates raw/effective source coverage; a summary model proposes compressed content or an OpenAI Codex-native compactor supplies provider state, with text-summary fallback. This model is [RT-CMP-ai-model](#rt-cmp-ai-model). SRC-1, `packages/runtime/src/ai-sdk-compaction.ts` and `packages/runtime-host/src/server/execution-model-composition.ts`.

> // Writes (including a rival winner or an uncertain commit) cannot tell
> // us what the model sees. Read once after the batch and use this same
> // snapshot for checkpoint validation, replay, and diagnostics.
> --- `packages/runtime/src/ai-sdk-compaction.ts`

Pruning is over effective history, not the original body size after an earlier replacement. The checkpoint pins effective-source coverage; later transitions can invalidate it even when raw ledger identity still matches. Standalone compaction first prunes and then summarizes effective coverage; persistence failure returns `write_failed`. This separates the full ledger from what reaches the next invocation. Model summarization is natural-language interpretation; coverage digests and replay policy are symbolic controls, not semantic correctness checks.

- Immediate return: Effective event projection and budget diagnostics, or compacted/unchanged/failed outcome with checkpoint.
- Later read-back: Later sends load checkpoints and model-projection transitions; model/connection compatibility and effective-coverage checks determine reuse.
- Delegated visibility: Summary provider receives the covered effective events and prior checkpoint as applicable, not an assumption of every original tool body.
- Selection predicate: Configured context-budget/prune policy, candidate size rules, checkpoint identity/coverage and model compatibility; standalone and mid-turn machinery are distinct entry points.
- Invalidation or expiry: Effective-history change, source-prefix mismatch or incompatible model can reject reuse; missing prerequisites return unchanged and write failure prevents reporting successful compaction.
- Activation or effect: Projection can replace tool bodies and folded history before a later model request; behavioral compliance or improved performance is not observed.
- Evidence limits: Archive retrieval tool behavior, exact tail policy for every mid-turn/overflow route and provider-native opaque state contents are not fully inspected. No semantic preservation oracle is established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

This is working-context control rather than merely logging: code removes large tool bodies preferentially and can fold old history, leaving projections/checkpoints and a durable ledger. It is also retained context when a later invocation receives the summary. Detailed memory revisions and read-back inventory belong to the memory analyst. No human approves each summary in the inspected compaction function; code admits a planner result after structural/coverage checks. Error recovery can reconstruct from durable events, but that is not a guarantee of lossless model understanding.

#### RT-RTE-plugin-admission
Label: Plugin package and composition admission

The Host platform accepts a source package path or composition operations. Software prepares/loads a package, derives desired authority, commits the authority/package and adopts runtime contributions. For composition apply it normalizes operations, derives a strict projection, stores the next authority and only then converges live entries. Source-native package/composition data are symbolic artifacts stored under the Host control-directory platform services; contributed implementation is executable code and contributed prompt text has a separate model-interpreted path. SRC-1, `packages/runtime-host/src/server/plugin-platform.ts`, `packages/runtime/src/plugin-composition-loader.ts` and `packages/runtime-host/src/server/execution-composition.ts`.

> await this.#store.replace(next);
> this.#authority = next;
> this.#desired = projection.desired;
> this.#structuralDependencies = projection.structuralDependencies;
> --- `packages/runtime-host/src/server/plugin-platform.ts`

Trigger/proposal: a caller supplies a package or operations, not a model automatically rewriting itself in the inspected code. Decider/veto: platform normalization, generation checks, package validation, strict projection and persistence can reject; a caller can request disabling/removing entries. Human versus computational authorship/control at the outer operation caller remains uninspected. Guidance shaping the proposal is not established; manifest/composition constraints shape acceptance. Persisted authority and installed package layers, not a historical criticism narrative, survive.

Recovery is phase-sensitive: before authority commit installation attempts rollback; after authority commit it records convergence failures and may return complete/pending receipts. Unknown commit outcomes fence the platform. Therefore receipt completion is not proof that all plugin capabilities are live. The composition loader separately restores previous package registration on reload failure. These are operational consistency mechanisms, not task-quality evaluation or a reference-answer oracle. Operating mode is administrative capability/configuration mutation; no improvement trigger or evaluated successor search is established.

- Immediate return: Mutation receipt and extension ID for installation, with convergence failures separately available.
- Later read-back: Desired authority/package layers feed runtime recovery and later composition; prompt/tool contributions are sampled through the composer.
- Delegated visibility: Contributions are scoped through the plugin platform; bound child/local tool ceilings suppress unlisted dynamic tool additions.
- Selection predicate: Caller-supplied package/operations, schema/package/generation validation, desired-projection derivation and visible contribution scope.
- Invalidation or expiry: Disable/remove/uninstall and reload; precommit rollback, postcommit convergence/recovery and unknown-outcome fencing have different semantics.
- Activation or effect: Can change tools, prompt contributions, executors and service adapters without rebuilding the foreground agent; actual successful adoption remains unobserved.
- Evidence limits: Outer mutation authorization, package trust checks, dependency closure and arbitrary plugin process isolation are not established. No source-native theory revision or exercised self-improvement is inferred from installability.
- implementation conclusion status: wired
- operation conclusion status: uninspected

### Claims

#### RT-CLM-task-runtime
Label: Task completion and event authority claim

SRC-1, `README.md`, states the product purpose:

> An agent harness exists to finish tasks. We hold it to one measure: how many it completes and at what cost. We publish every run: same model, same official verifier, full per-task record.
> --- `README.md`

It also claims:

> **The log is the runtime.** Every model message, tool call, permission decision and termination is an append-only RuntimeEvent. The UI, the next prompt and crash recovery are projections of that log, never the only copy. Old tool output can leave the next prompt without leaving the log.
> --- `README.md`

Claim conclusion status: claimed

The inspected main-loop continuation, compaction and recovery routes support particular implemented parts of this contract. They do not establish universal event completeness for custom/external executors, successful task execution, measured cost correctness or benchmark superiority. No benchmark experiment was assessed in this runtime member.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-composed-prompt
Label: Composed prompt authority

Consumer: selected foreground or child model. Channel: composer system-prompt text assembled from shipped guidance, selected skills, workspace instructions, policy personalization and eligible memory; plugin prompt contributions can be added at logical steps. Force: natural-language guidance requiring model interpretation, not an OS capability grant. Horizon: base composition per Session/Turn, with later turns rereading relevant sources and plugins potentially resampled per step. SRC-1, `packages/runtime-host/src/server/interactive-run-composer.ts` and `packages/runtime-host/src/server/execution-model-composition.ts`.

> const workspaceInstructions = promptState.policy.workspaceInstructions.enabled
>   ? await buildWorkspaceInstructionsPromptFragment(context.cwd)
>   : undefined;
> --- `packages/runtime-host/src/server/interactive-run-composer.ts`

Delivery is wired; compliance, content-derived changed behavior and benefit are unobserved. Child prompt construction is distinct from main-session assembly. Detailed authority of retained memory parts is not declared here.

#### RT-BAP-tool-boundary
Label: Execution-boundary authority

Consumer: built-in filesystem/Bash executors and applicable client preparation callbacks. Channel: live symbolic `ExecutionBoundary` and permission-mode reads carried in tool context, plus validated boundary-request settlement. Force: dispatch rejection, worker/backend selection or sandbox invocation where the consumer enforces it; not a universal restriction on arbitrary plugin code. Horizon: current dispatch and persisted session grant until changed. SRC-1, `packages/runtime/src/tool-runtime.ts`, `packages/runtime/src/filesystem-executor.ts`, `packages/runtime/src/builtin-tools.ts` and `packages/runtime-host/src/server/execution-model-composition.ts`.

> readPermissionMode: async () =>
>   (await input.context.store.readHeader(input.context.sessionId)).permissionMode,
> --- `packages/runtime-host/src/server/execution-model-composition.ts`

The exact current deployed grant is unobserved. Bypass, managed and external workspace paths differ; requesting expansion does not itself grant it. This path supplies executable authority, whereas [RT-BAP-composed-prompt](#rt-bap-composed-prompt) supplies interpreted guidance.

## Annotations

none
