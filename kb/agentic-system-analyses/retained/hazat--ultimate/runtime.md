---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Ultimate runtime baseline: browser admission, durable coding conversations, delegation, extension loading and change admission at the frozen commit."
run-id: AAS-2026-11-01-ultimate-f5179584de71-01
reviewed-boundary: "e2b9fa61962f6aecd394dea1c670688fac3ec432"
---

# Ultimate runtime report

## Runtime account

Ultimate is a project-specialized coding application whose server encloses an externally implemented Pi Durable harness. The application owns browser admission, project configuration, extension discovery, storage ownership and process replacement. The model chooses work steps through natural-language instructions and structured tool calls; Pi Durable schedules the conversation and task machinery. This is not evidence that the external scheduler's durability contract is correct. All findings below use SRC-1 at the revision in [the boundary](boundary.md). Source inspection establishes implementation wiring and declared policy, not exercised operation or benefit. No supplied execution trace or causal experiment was available; the target and its tests were not executed.

### Ordinary invocation and state ownership

The installed driver forks `server/main.ts`; direct development startup can enter that server without the supervisor. `prepareHarness` creates a ModelRuntime, Pi settings, registry and per-cwd NodeExecutionEnv. Extensions load before the harness serves requests. Storage opens under a project-home ownership lock, against the active chapter's SQLite database. Interrupted reset markers block opening; chapter-switch completion precedes storage use. The root is created/configured, then the harness resumes. `serve` runs extension open callbacks, creates the API and resumes scheduling. SRC-1: `bin/ultimate.ts`, `server/main.ts`, `server/harness.ts`.

The shipped browser SDK posts text, optional images and busy-mode to the selected conversation. The API admits the HTTP caller, checks input shapes, expands an explicit skill command, and submits a Pi input. It returns a submission ID rather than pretending the answer is synchronous. A conversation ID identifies model context; task/call IDs identify work and replay receipts; model provider/ID identify the inference endpoint, not immutable weights. A user-input event is committed after the input, so a crash between commits can lose the event without losing the admitted input. Subsequent generation, tools and final answers belong to the durable conversation; browser event subscriptions and history requests expose activity and persisted entries. See [RT-RTE-browser-input](#rt-rte-browser-input).

The model's request context combines conversation state, instructions, extension sections, selected tool declarations and supplied input. The host executes granted coding tools through NodeExecutionEnv; read/write/edit and shell commands affect the machine, not just a conversation document. The prompt asks the agent to investigate, implement, verify and report. It distinguishes exploratory questions, which should await approval, from direct tasks and scheduled work, which supply permission to proceed. That is interpreted policy, not a universal per-effect approval gate. SRC-1: `extensions/prompt/server.ts`, `extensions/coding-tools/server.ts`, `server/harness.ts`; [RT-BAP-prompt-guidance](#rt-bap-prompt-guidance).

New work can instead start as a lineage branch. Root memory, when present, replaces the root tally with a brief at a reset entry; a fork of another branch keeps its context. Ordinary tools are restored explicitly rather than inheriting a source conversation's restricted tool selection. Branches are ownerless conversations with a first-input delivery task; summaries and landings feed the tree's tally. This path must not be conflated with bounded subagent creation. SRC-1: `extensions/lineage/server.ts`; [RT-RTE-lineage-branch](#rt-rte-lineage-branch).

### Alternate loops and working-context boundaries

Named subagents have their own durable conversations. A normal start supplies a self-contained task without parent history; `fork:true` inherits history before the calling assistant entry. Foreground calls wait interruptibly; background work returns an ID and reports later. Definition tools must be a subset of the parent's active tools on this start path. Definitions without explicit `subagent` permission lose the subagent tool and extension. Parent stop does not by itself imply child stop: the start path creates a background anchor owner and the tool contract asks callers to stop children explicitly. A worktree separates Git work but does not provide a filesystem sandbox. See [RT-RTE-subagent-start](#rt-rte-subagent-start).

Automations supply another principal: saved schedule/event/condition/script triggers, rather than a current browser input. A fired prompt creates a child under a durable run task. Named profiles exclude automation and subagent tools; an unnamed run copies the root and excludes automation only. Therefore the named-profile exclusion is not a system-wide prohibition on delegation from automation runs. Isolation settings are not applied by this scheduler call. It waits for the input's result, extracts text from the answer and records completion/failure. Rate limiting pauses excessive fires and overlapping runs can be skipped. See [RT-RTE-automation-run](#rt-rte-automation-run).

Codemode executes model-authored JavaScript in QuickJS/WASM, with no ordinary host I/O except injected functions. It derives nested tool declarations from the current agent's tools, validates arguments and calls their executors directly. **Nested tool hooks do not run.** Thus a guarantee implemented only in a tool hook cannot automatically cover codemode; checks inside the actual executor still can. Nested results stay outside model context unless emitted, so this path also filters what the foreground model receives. Timeout, VM memory limits and output selection limit the computation, not the effects of injected host tools. A yielded subagent wait aborts the VM and discards pending store changes, but prior host effects may have happened. See [RT-RTE-codemode-tools](#rt-rte-codemode-tools).

Not every inference is the foreground agent loop. Conversation summaries call `models.streamSimple` directly, with a saved response receipt reused before another request. Sketch uses its own bounded `completeSimple` loop and small read/render tool set, validating the render specification and allowing one invalid-spec repair. These paths are not generic permission-controlled foreground tool rounds. Claude Code also wraps the provider transport and environment lookup separately; failure to resolve extra environment falls back to original options rather than refusing the call. Exact remote model internals and CLI-native behavior are not captured here. See [RT-RTE-auxiliary-model](#rt-rte-auxiliary-model), [RT-CMP-provider-models](#rt-cmp-provider-models).

Working-context control is not limited to delegation. Compaction policy reserves answer space and a recent verbatim tail, with model-specific overrides. The source instructs that older turns become a summary while full history stays searchable; actual external compactor selection behavior is not independently inspected. A side chat forks settled history, then stops and either discards or injects a model-generated summary of only its later entries. Known persistent effects disable discard; this is bookkeeping of named effects, not isolation. Summary failure reopens the side copy for retry. These mechanisms resemble separate frames with selected returns, but durable conversations and host effects survive the apparent frame exit. See [RT-RTE-context-return](#rt-rte-context-return). Detailed memory writing, recall, distillation and dream-seed transformations are left to the memory member rather than redescribed as runtime guarantees.

### Load-bearing controls and forcing cases

Four forcing cases informed the account: ordinary HTTP input versus internal submissions; named subagent start versus ownerless lineage branch and unnamed automation; direct tools versus codemode nested execution; checked landings/supervised swap versus direct shell changes and live extension reload. Each defeats an overbroad reading of a local control. They establish reachable shipped alternatives, not experimental exploits.

1. **HTTP admission.** Owner: server; enforcement: `admit` at the API handler and server request integration. Strength: protocol. Non-proxied loopback host/origin can pass without remote identity verification; other origins require matching registered access rules and a verifier returning a login. This covers browser/API entry, not internal task submissions or host code. External contract: loopback binding and trusted proxy/header/identity behavior. Implementation conclusion status: wired. Operation conclusion status: uninspected. SRC-1: `server/request-security.ts`, `server/api.ts`, `server/main.ts`.
2. **Grant filtering, not confinement.** Owner: subagent start/configuration; enforcement: definition subset check and `definitionAgent` tool/extension filtering. Strength: protocol on that route. Alternate branches reset tool selection; unnamed automation uses different exclusions; codemode has injected host APIs; shell and trusted extensions can perform effects outside abstract tool labels. No deployed OS sandbox is established by constructing NodeExecutionEnv with cwd, and worktree instructions cannot prove path confinement. Exact live grants depend on discovered configuration, enabled extensions and credentials, none supplied as production state. Implementation conclusion status: wired. Operation conclusion status: uninspected. SRC-1: `extensions/subagents/server.ts`, `lib/agents.ts`, `extensions/lineage/server.ts`, `extensions/automations/scheduler.ts`, `extensions/codemode/server.ts`.
3. **Checked integration.** Owner: workspace lander; enforcement: configured commands, durable check receipts, unchanged integrated commit/worktree checks, serialized fast-forward. Strength: protocol; a check passing on its one retry is allowed and marked flaky. Empty/default command configuration does not prove semantic correctness. External contract: Git and check commands behave as assumed; verification commands encode the desired outcome. This covers submissions through the lander, not direct shell edits/commits or all possible pushes. Implementation conclusion status: wired. Operation conclusion status: uninspected. See [RT-RTE-change-admission](#rt-rte-change-admission).
4. **Runtime replacement and extension admission differ.** Supervisor type checking gates its swap path; old storage releases before the new process activates, with reacquisition attempted on failure. Live extension loading instead evaluates module code through Vite, validates extension registration shape and installs it in the registry; retaining the previous facet after a caught loading failure does not undo arbitrary module-initialization effects. Project trust gates discovery, not each later content revision. Type checks establish neither runtime correctness nor security. Direct development startup is not that supervised swap. Implementation conclusion status: wired. Operation conclusion status: uninspected. See [RT-RTE-change-admission](#rt-rte-change-admission), [RT-BAP-extension-code](#rt-bap-extension-code).

A further local safeguard checks `remember`'s caller in the executor against the standing Ultimate conversation. This is stronger than hiding a deferred tool: the source explicitly anticipates discovery from a branch. It can survive direct/nested calls to that executor, but cannot establish that trusted host code or shell has no other way to alter storage. SRC-1: `extensions/lineage/server.ts`.

> // Deferred only hides it: a branch can still find it with tool_search, so the caller is checked here.
> --- `extensions/lineage/server.ts`

Durable state is also not exactly-once external effects. Call receipts and task checkpoints reduce duplicate admissions; the prompt expressly warns that an interrupted tool may or may not have completed. MCP deliberately reconnects after broken transport without resending the failed call. The tool-argument guard routes both `streamSimple` and `completeSimple` through the whitespace detector, but other methods bind directly to the underlying runtime, so it is not proof that every possible provider stream is guarded. SRC-1: `server/tool-arguments.ts`, `extensions/mcp/server.ts`, `extensions/prompt/server.ts`.

> // The target's own completeSimple calls its streamSimple on itself, past this proxy: route it through ours.
> --- `server/tool-arguments.ts`

### Additional inspected coverage and remaining uncertainty

Beyond the boundary's initial inspection, this member inspected SRC-1 implementation in `server/tool-arguments.ts`, `server/request-security.ts`, `server/project-setup.ts`, `server/discovery.ts`, extension installation/invocation slices of `server/extensions.ts`, agent filtering in `lib/agents.ts`, subagent start/child creation, automation scheduler, coding tools, codemode nested dispatch, lineage fork/reset, workspace check/fast-forward, side-chat termination, summary helper, sketch loop, MCP dispatch, Claude Code registration and dream preparation/switch slices. It also inspected the browser submit/history SDK, API input validation, server activation and supervisor swap. Prompt content is doctrine/design even when supplied by executable section builders. These are added paths under SRC-1, not new sources.

Provider-native tooling, full external harness scheduling/compaction/storage semantics, live remote/cloud execution, installed user extensions and credentials remain unobserved or outside the captured dependency implementations. Shipped browser/cloud/automation adapters enlarge the capability surface, but this account does not certify their live service behavior. No throughput, token-saving, reliable completion, faithful summarization or improvement result follows from these source paths.

## Shared records

### Components

#### RT-CMP-provider-models
Label: Provider models

Source-native identities are ModelRuntime model references (`provider`, `modelId`), default families and definition pins. Distributed-parametric inference occurs at external providers/Claude Code; weights and provider storage are not in SRC-1. Local symbolic configuration is not the weights. SRC-1: `server/harness.ts`, `lib/agents.ts`, `extensions/claude-code/server.ts`, `extensions/conversations/summary.ts`, `extensions/sketch/server.ts`.

Parameters changing during operation: uninspected — the inspected application invokes inference and contains no inspected weight-update path; provider internals are not captured. Exact model version pinned: not established by provider/ID strings; family/default selection and runtime discovery are mutable. Mutable endpoint resolving to another model: possible through provider catalogs, configuration, previews and login-dependent selection; remote alias semantics are uninspected. `defaultModel` prefers configured logged-in choices, then a configured reference even when login is lost, before using the first available model only if nothing is configured. A branch has its own fallback logic. Fixed weights, even if established externally, would not exclude retained-text adaptation.

> const ref = previewModel() ?? overrideModel ?? pin ?? parent.model
> --- `lib/agents.ts`

### Operative objects

#### RT-OBJ-agent-doc
Label: AgentDoc and conversation state

AgentDoc is symbolic configuration consumed by fixed harness rules: model reference, tools/extensions, cwd and thinking level. Conversation entries carry symbolic kinds/ownership and natural-language model messages; these parts are consumed differently. The application opens an active-chapter SQLite store and uses transactional documents, entries and tasks through Pi Durable. Exact upstream storage internals remain outside the frozen repository. SRC-1: `server/harness.ts`, `extensions/subagents/children.ts`, `extensions/lineage/server.ts`.

> storage = await openNodeSqliteStorage(chapter.database)
> --- `server/harness.ts`

#### RT-OBJ-agent-instructions
Label: Agent instructions

Natural-language agent bodies and prompt sections shape model interpretation; symbolic frontmatter selects tools, models and other definition options. File-backed definitions, overlays and skills are discovered from built-in/user/trusted-project roots; selected instruction text enters conversation agent configuration. Changed instruction files can be reapplied and named in a build/input note. This is a capability/instruction update route, not evidence of model obedience or successful improvement. SRC-1: `lib/agents.ts`, `extensions/prompt/server.ts`, `server/skills.ts`.

> instructions: definition?.instructions ?? parent.instructions ?? null,
> --- `lib/agents.ts`

### Routes

#### RT-RTE-browser-input
Label: Browser input to durable conversation

The user/browser SDK posts to the selected conversation's submit endpoint. Server admission and shape validation precede skill expansion and `conversation.submit`; Pi owns subsequent generation scheduling, while the model chooses answers/tool calls. Node tools perform host effects; event/history endpoints return ongoing and stored results. The browser input event is a separate later transaction. SRC-1: `web/src/sdk/api.ts`, `server/api.ts`, `server/main.ts`, `server/harness.ts`.

- Immediate return: HTTP 202 and submissionId, not the model answer.
- Later read-back: persisted conversation entries through history; resumed harness state after reopening storage.
- Delegated visibility: subagents do not automatically receive all input; their selected task/fork path governs visibility.
- Selection predicate: SDK selects shown/requested conversation; API requires valid conversation and text or images, with supported busy modes.
- Invalidation or expiry: input rejection precedes admission; abort stops own non-background tasks while queued follow-ups are preserved by the API's explicit stop loop.
- Activation or effect: input is admitted to the conversation; inference and host tool effects are wired, actual behavioral response unobserved.
- Evidence limits: external harness execution and actual browser/provider runs not supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const submission = await conversation.submit(
>                 { type: 'input', content, whenBusy: data.whenBusy },
>                 context,
>               )
> --- `server/api.ts`

#### RT-RTE-lineage-branch
Label: Lineage branch creation

A caller requests a prompt/from/optional entry. Lineage validates the fork point, computes root/tally or memory brief, forks ownerlessly, sets project cwd and model policy, restores ordinary tools and optionally creates a workspace. A reset makes the memory brief the new model-context start without deleting the stored tally. The first prompt is delivered by a durable task. SRC-1: `extensions/lineage/server.ts`.

- Immediate return: branch conversation ID after commit and scheduler resume.
- Later read-back: branch conversation, tally/abstract breadcrumbs and brief-based context; detailed memory transformation belongs to the memory analysis.
- Delegated visibility: fork history when branching a branch; memory brief replaces root tally when available, not all root history.
- Selection predicate: supplied source/entry must exist; root-with-memory branch selects the brief path.
- Invalidation or expiry: reset changes visible context start, not stored history; further expiry uninspected.
- Activation or effect: new runnable work context with ordinary tools, independent of the source's restricted tool list.
- Evidence limits: model use of the brief and correctness of resulting work unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> // A branch gets ordinary tools whatever its source ran with.
>   const agent = await tx.doc(AgentDoc, fork.id)
>   delete agent.tools
>   delete agent.modelTools
> --- `extensions/lineage/server.ts`

#### RT-RTE-subagent-start
Label: Named subagent start and return

Foreground model proposes a named agent and task; tool code discovers an eligible definition, rejects unknown names/non-subset explicit tools, creates a background anchor task and child, configures instructions/grants/model, and submits via a reporter. Optional fork uses history before this call; optional worktree supplies branch instructions. Definition policy and code, not a per-child human approval, decide this path. Open task mode; no expected-answer oracle is established. SRC-1: `extensions/subagents/server.ts`, `extensions/subagents/children.ts`, `lib/agents.ts`.

- Immediate return: foreground answer/wait or background child ID; steering can yield a wait while work continues.
- Later read-back: durable child conversation and reported answer receipts.
- Delegated visibility: self-contained task by default; explicit fork inherits parent history before the call, not a fresh isolated history.
- Selection predicate: discovered definition permits subagent use; explicit definition tools must be a subset of active parent tools.
- Invalidation or expiry: stop/discard are explicit actions; parent stopping is not a child-stop guarantee; worktree discard keeps its branch per tool contract.
- Activation or effect: child model can run granted tools and produce host effects; worktree policy is not OS confinement.
- Evidence limits: external scheduling details, live grants and completion quality unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (definition?.tools?.some((name) => !parent.tools.some((tool) => tool.name === name)))
>               throw new Error('Definition tools must be a subset of parent tools')
> --- `extensions/subagents/server.ts`

#### RT-RTE-automation-run
Label: Automation prompt runs

Saved automation triggers create durable RunTask work; scheduler owns progression, selected profile/root supplies agent state, and child inference decides work steps. Code excludes tools differently for named and unnamed profiles, submits an idempotently keyed input and records extracted answer text. These are open operational requests, not a benchmark curriculum; no answer oracle is established. SRC-1: `extensions/automations/server.ts`, `extensions/automations/scheduler.ts`.

- Immediate return: fire/task bookkeeping; prompt run completion is recorded later.
- Later read-back: automation runs ledger and child conversation; saved prompt/configuration can affect later fires.
- Delegated visibility: child receives saved automation prompt plus optional fired text, not the foreground user's whole conversation by default.
- Selection predicate: enabled trigger and prompt; overlap scans prevent another simultaneous run and six recent fires cause pause/escalation.
- Invalidation or expiry: pause/delete/abort controls; scheduling data and durable checkpoints control recovery.
- Activation or effect: unattended model invocation with configured/root grants; no inference that scripts or prompt runs are safe merely because scheduled.
- Evidence limits: trigger reliability and real recurring operation unobserved; script-supervisor repair internals not assessed here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> excludeTools: a.agent ? ['automation', 'subagent'] : ['automation'],
>               excludeExtensions: ['automations'],
> --- `extensions/automations/scheduler.ts`

#### RT-RTE-codemode-tools
Label: Codemode nested host calls

The foreground agent supplies JavaScript; QuickJS executes it with injected tool/global functions. Code derives tools from agent.tools, prepares and validates arguments, then invokes the actual executor with a nested API/call ID and abort signal. Tool hooks are not replayed around that nested dispatch. Host effects are outside the VM's memory/store transaction. SRC-1: `extensions/codemode/server.ts`.

- Immediate return: script-selected text/JSON and call diagnostics rather than every nested tool result.
- Later read-back: conversation store JSON on successful completion; pending store writes discarded on yield; host-side durable effects can persist separately.
- Delegated visibility: subagent arguments select their context; nested results remain VM-local unless emitted/returned.
- Selection predicate: current agent tools supply declarations, plus injected host globals; argument schemas validate nested tool calls.
- Invalidation or expiry: timeout/abort closes VM; yielded waits terminate remaining script, not prior effects or running children.
- Activation or effect: nested executors perform real effects without nested hooks; this qualifies hook-only guarantees.
- Evidence limits: QuickJS internals are external; no deployed sandbox-escape or confinement test supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const result: StructuredResult = await resolved.execute(
>               validated,
>               nested,
>               withAbortSignal(signal, context),
>             )
> --- `extensions/codemode/server.ts`

#### RT-RTE-auxiliary-model
Label: Direct summary and sketch inference

Summary helpers and sketch call models outside foreground generation. Summary receipt code reuses a prior response before requesting another. Sketch owns a bounded message/tool loop with render-spec validation and one invalid-spec retry. Its data-present branch offers render only; data-absent branch offers a small project-reading surface. Model proposes a spec, software validates it; schema validity is not an answer oracle for factual correctness. SRC-1: `extensions/conversations/summary.ts`, `extensions/sketch/server.ts`.

- Immediate return: summary response receipt or validated sketch spec/read/steps; unavailable model and failed rendering throw.
- Later read-back: callers can persist summary receipts; sketch step memoization is wired by the tool caller; exact later memory uses belong to specialist accounts.
- Delegated visibility: selected summary input or sketch request/data only, not implicit full parent conversation.
- Selection predicate: configured summary/sketch model and caller-selected source; presence of run.data controls the sketch read-tool branch.
- Invalidation or expiry: receipt reuse prevents another call for saved response; invalid render allows one repair, then fails.
- Activation or effect: generated text/spec reaches its caller; accurate summaries and correct visualizations are unobserved.
- Evidence limits: no model traces supplied; providers are external; this is an implemented auxiliary loop, not evidence every direct call uses foreground hooks.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (receipt.response) return receipt.response
> --- `extensions/conversations/summary.ts`

> const tools = run.data === undefined ? [render, ...reads] : [render]
> --- `extensions/sketch/server.ts`

#### RT-RTE-context-return
Label: Compaction and side-chat return

Pi settings/model overrides control compaction thresholds; actual compaction algorithm is external. Side-chat termination stops its conversation, scans only later entries for injection, asks a summary model, and admits the summary as a user-role write in the main conversation. User-only end actions choose injection/discard; known effects veto discard. Summary stop reason/nonempty text are software admission checks, not truth or completeness oracles. SRC-1: `server/harness.ts`, `extensions/prompt/server.ts`, `extensions/side-chat/server.ts`.

- Immediate return: compaction scheduling or side-chat end-task completion; summary errors can reopen the side chat for retry.
- Later read-back: compacted summary replaces older model-visible context; injected side-chat summary enters later main context; original history stays stored.
- Delegated visibility: side chat has its forked context; summary scan excludes inherited history and pi.system entries.
- Selection predicate: token policies for compaction; user-selected injected mode for side-chat summary, versus discarded mode with no injected summary.
- Invalidation or expiry: compaction removes older turns from the active window, not storage; ending side chat concludes it, but does not roll back host effects.
- Activation or effect: new summary supplied to the next consumer; compliance and preserved meaning unobserved.
- Evidence limits: upstream compaction selection and live summaries not available; named-effect tracking is not a complete side-effect sandbox.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (mode === 'discarded' && side.effects)
>       throw new Error(`Side chat #${id} has effects; inject its summary instead`)
> --- `extensions/side-chat/server.ts`

#### RT-RTE-change-admission
Label: Product and runtime change admission

Agents/humans can propose code, instructions, extensions or configuration. The workspace lander merges/integrates, executes configured check groups with one retry per failed check, rejects twice-failed checks or changed checkout, then serializes a fast-forward. Configured checks are computational reference outcomes (process success), supplied by project settings; they are not an independently correct specification. Model-authored changes can also use ordinary shell/file tools outside this path. Live extension discovery loads enabled source and validates shape; its contents are not individually approved by the project trust choice. Supervised core replacement instead runs tsc before preparing/activating a replacement and releasing old storage. These are distinct admissions, not one system-wide gate. SRC-1: `extensions/workspaces/lander.ts`, `server/extensions.ts`, `server/discovery.ts`, `server/project-setup.ts`, `bin/ultimate.ts`.

- Immediate return: landing result/failure, extension registry update/error, or swap acknowledgement/result depending on entry path.
- Later read-back: landed Git commits, loaded extension code, changed definitions/instructions and persisted project settings; subsequent operations may consume them.
- Delegated visibility: workers submit workspaces; integration uses candidate merged revision; later conversations receive changed code capabilities/instructions rather than all worker history.
- Selection predicate: lander configured checks plus commit/clean-state guards; trusted/enabled discovery winners for extension load; successful tsc/prepare/ack/release/start sequence for supervised swap.
- Invalidation or expiry: lander failures leave work to repair/resubmit; swap failure kills replacement and attempts old-owner reacquisition; caught facet failure keeps previous registration where available, not a rollback of arbitrary module effects.
- Activation or effect: Git target moves, registry installs executable capability, or new core activates; these provide later behavioral-authority paths without proving improvement.
- Evidence limits: no successful runs supplied; direct shell changes bypass the named admission paths, and external runtime semantics remain contractual.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Trigger/proposal/admission: open coding tasks, explicit reload/restart or workspace submission initiate change. Guidance comes from selected agent instructions and project check settings. Computation runs checks/admission; humans can edit settings/source, withhold a requested go under prompt policy, or decline proposals, but these paths do not require per-content human approval. Rejection exists locally as described above; semantic rejection of valid-but-wrong code is not established. Recovery preserves Git history/check receipts or attempts prior process ownership, not universal effect rollback. Changed code, config and text persist by their substrates. No formulated-theory criticism, learned capacity or exercised self-improvement is inferred from admission alone.

> if (failed !== -1)
>                 return await fail(
>                   `check failed twice: ${commands[failed]}`,
> --- `extensions/workspaces/lander.ts`

> await checkTypes()
>     next = boot(previousBuild)
>     await prepare(next)
> --- `bin/ultimate.ts`

### Claims

#### RT-CLM-coding-work
Label: Project-specialized coding work

The prompt claims an agent that builds, verifies and reports under user steering, and asks it to specialize itself through tools, panels, agents and skills. This is shipped doctrine/design, not observed successful work. SRC-1: `extensions/prompt/server.ts`; implementation routes above establish means, not reliable fulfillment.

> You are Ultimate, a coding agent running in a web UI on the user's machine. The person in this conversation steers; you build, verify, and report.
> --- `extensions/prompt/server.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-prompt-guidance
Label: Instructions to model decisions

Consumer: foreground/child model. Channel: configured definition instructions and generated prompt sections. Force: natural-language policy interpreted during inference, unlike software tool-selection rules. Horizon: selected invocation and later invocations while configuration/text remains selected. Instructions are reapplied through discovery/configuration and changes can be announced in input notes. Actual compliance and benefit remain unobserved. SRC-1: `lib/agents.ts`, `extensions/prompt/server.ts`; [RT-OBJ-agent-instructions](#rt-obj-agent-instructions).

> Instructions changed: ${changes.instructions.join(', ')}. Your system prompt now carries the new text; drop habits from the old one.
> --- `extensions/prompt/server.ts`

#### RT-BAP-extension-code
Label: Loaded extension authority

Consumer: Vite/Node module loader and harness registry. Channel: enabled discovered server facet loaded into the host process and installed as executable tools/hooks/sections/tasks. Force: symbolic/executable host behavior, not model interpretation; extensions also have direct host services. Horizon: current installed facet until replacement/unload/process close, with durable state and external effects potentially surviving. Project discovery requires trust; user/builtin layers do not use that project gate. Shape validation happens after module evaluation and is not hostile-code isolation. SRC-1: `server/extensions.ts`, `server/discovery.ts`, `server/project-setup.ts`.

> const module = await vite.ssrLoadModule(join(target, 'server.ts'))
> --- `server/extensions.ts`

> host.registry.install(trace.tools(extension))
> --- `server/extensions.ts`

Dream is an additional user-facing admission surface: it prepares next-chapter metadata, then exposes user-only start/asleep/switch actions. Fall-asleep requires preparation, idle checks, seed building and backup before journaled restart; prepare itself delivers a card directing the user to act. This is evidence of a bounded human-controlled chapter transition, not proof that every model-proposed code change receives human approval. Exact seed contents and memory revisions belong to specialist analysis. SRC-1: `extensions/dream/server.ts`.

> export const userActions = ['start', 'asleep', 'switch']
> --- `extensions/dream/server.ts`

> if (userActions.get(name)?.includes(action))
>         throw new Error(`${name}/${action} is a user-only action`)
> --- `server/extensions.ts`

The user-only rejection is enforced in agent-facing host.invoke, not an OS security boundary against arbitrary trusted Node modules or shell. MCP expands capability through configured stdio/HTTP services and the generic mcp executor; actual grants and remote effects depend on server configuration. Its error branch reconnects a broken connection but intentionally does not resend uncertain effects. SRC-1: `extensions/mcp/server.ts`.

## Annotations

none
