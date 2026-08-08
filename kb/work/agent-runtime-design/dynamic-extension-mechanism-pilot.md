# Dynamic-Extension Mechanism Pilot

## Purpose and comparison boundary

This pilot tests the agent-runtime review vocabulary against several dynamic-extension mechanisms. It is **not** a comparison of peer agent runtimes.

- RLM is a computational pattern. Concrete systems such as Fractal or llm-do can host an RLM-style loop.
- Dynamic workflows are a subsystem of the Claude Code runtime. A workflow script is a generated control program, not the enclosing runtime.
- Tendril's generated capabilities are a subsystem of the Tendril agent and desktop product.
- llm-do's unified callable namespace and `dynamic_agents` toolset are mechanisms inside the llm-do runtime.

Some source material uses *harness* for a generated workflow. This workshop keeps that source wording when describing the claim, but reserves **agent runtime** for the operational system that supplies execution, authority, lifecycle, client interaction, and recovery. A generated orchestrator can choose runtime policy without thereby becoming the runtime that enforces it.

The pilot asks two questions:

1. Which facts distinguish dynamic execution, durable extension, and runtime self-modification?
2. Which guarantees belong to the extension mechanism, and which come only from its enclosing runtime and client?

## Evidence basis

- **RLM:** [RLM has the model write ephemeral orchestrators over sub-agents](../../notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md), the [RLM–Tendril–llm-do persistence comparison](../../notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md), and the concrete [Fractal review](../../agentic-systems/fractal.md). These establish the pattern and one enclosing runtime; this pilot does not treat the pattern as a product.
- **Claude Code dynamic workflows:** the existing [subsystem analysis](../../agentic-systems/claude-code-dynamic-workflows.md), grounded in an [official documentation snapshot](../../sources/claude-code-dynamic-workflows-docs.md) captured 2026-06-03 and a first-hand tool contract observed 2026-06-12.
- **Tendril:** the existing [code-grounded Tendril review](../../agent-memory-systems/reviews/tendril.md), pinned to `e671a4143d28de68289efd81580002041bb4cb6a` and checked 2026-06-05.
- **llm-do:** first-hand reading on 2026-08-06 of the clean relevant scope in the sibling checkout at `d86c686813ec569f1d688ee6948919ff6d0022bb`. Inspected source included `DynamicAgentsToolset`, builtin registration, runtime registry and approval wiring, tests, the RLM example, and the proposed pure-dynamic-tools note. The wider checkout had unrelated local changes. No live model run or test was executed for this pilot.

Evidence status matters especially for llm-do: `dynamic_agents` is implemented and wired as a builtin; model-authored pure executable tools remain a design note, not a shipped mechanism.

## Mechanisms inside their enclosing systems

| Compared mechanism | Enclosing operational system | Mechanism's role | Responsibilities retained by the enclosing system |
|---|---|---|---|
| RLM-generated REPL program | An RLM implementation such as PredictRLM/Fractal or the llm-do RLM example | Model-authored task-local symbolic computation and recursive call orchestration | REPL construction, inference primitive, isolation, effect surface, run lifecycle, UI, and any persistence |
| Claude Code workflow script | Claude Code | Model-authored JavaScript control program over `agent()`, `pipeline`, `parallel`, and saved workflows | Script sandbox, subagent implementation, tool allowlist, permissions, journals, session resume, budgets, progress UI, and save/discovery path |
| Tendril generated capability | Tendril agent sidecar plus desktop host | Model-authored named TypeScript action registered for later execution | Bootstrap tool loop, workspace registry, Deno sandbox, filesystem/network envelope, desktop browser, and process lifecycle |
| llm-do unified callable | llm-do runtime plus project linker | Stable name and input boundary shared by `.agent` definitions and Python tools | Project discovery, registry, call scopes, model/tool dispatch, depth, approvals, events, and client surfaces |
| llm-do dynamic agent | llm-do `dynamic_agents` toolset inside the runtime | Model-authored `.agent` definition created and callable during the current runtime session | Tool and toolset registries, model selection, file placement, session registry, nested calls, approval wrapping, and UI callback |
| llm-do pure dynamic tool | Proposed llm-do subsystem | Proposed RestrictedPython control program with `call_agent` as its only effectful handle | Not implemented; no shipped lifecycle or guarantee should be attributed |

The enclosing-system column is load-bearing. RLM does not inherently have or lack user approval. A generated workflow does not itself own Claude Code's permission prompts. A Tendril capability does not choose its Deno flags. The mechanism supplies control logic or a new callable; the runtime supplies the authority and lifecycle semantics under which it acts.

## Authorship, persistence, activation, and target

Artifact persistence and behavioral persistence must be recorded separately. A file can remain on disk without being loaded by a later runtime. Conversely, a session journal can preserve an invocation without promoting its control strategy into a reusable artifact.

| Mechanism | Concrete generated unit | Authorship | Artifact lifetime | Activation lifetime | Change target |
|---|---|---|---|---|---|
| RLM program | REPL code and variables | Model, during the task | Normally discarded with the task | Current task | Current orchestration and task state |
| Claude Code workflow, unsaved | JavaScript workflow script | Model, for one requested task | Stored under session state | Resumable within the same session | Current workflow control policy |
| Claude Code workflow, saved | The same script saved as a named command | Model authors; user admits through save | Project or user scope across sessions | Discoverable as `/<name>` in later sessions | Claude Code's reusable command/workflow extension surface |
| Tendril capability | Registry entry plus TypeScript source | Model through `registerCapability` | Workspace files across sessions | Available to later turns through registry listing and named execution | Workspace capability surface |
| llm-do static callable | `.agent` or Python tool definition | Normally human or builder | Project files | Linked on configured later runs | Project callable namespace |
| llm-do dynamic agent | Generated `.agent` file plus in-memory `AgentSpec` | Model through `agent_create` | File remains in a configured directory or the default temporary directory | Automatically callable only in the current `Runtime` instance | Session dynamic-agent registry |

The llm-do dynamic-agent case exposes the key distinction. `agent_create` writes a file and stores the compiled `AgentSpec` in `Runtime.dynamic_agents`. The implemented linker does not automatically discover that generated file in a new runtime process. Re-activation requires a later human or host action to place or reference it as project configuration. The file may outlive the process, although the default temporary path supplies no durable-retention guarantee; automatic behavioral activation lasts only for the current `Runtime` instance, which may serve several top-level runs.

This produces four useful boundary cases:

- **Self-generated but not durable:** an ordinary RLM program.
- **Durable but not self-generated:** an ordinary hand-written llm-do agent or Python tool.
- **Self-generated and file-retained, but not automatically reactivated:** a current llm-do dynamic agent; cross-run artifact durability depends on its configured storage path.
- **Self-generated and durably operative:** a saved Claude Code workflow or Tendril capability, within the extension boundary each product recognizes.

The last class is eligible for durable self-extension. Whether it is **runtime self-modification** still depends on the declared system boundary and change target. Adding a callable to an extension surface is not the same intervention as rewriting protected scheduling, enforcement, or admission machinery.

## Admission is separate from generation

The systems place the admission decision differently:

- RLM admits generated code only into the current task's REPL. Discarding it avoids a cross-run trust decision.
- Claude Code asks before launching a generated workflow according to permission mode. Saving it as a reusable command is a separate explicit user action. The user admits a model-authored artifact but does not become its author.
- Tendril's model-facing `registerCapability` writes directly to the workspace registry. The inspected review found validation of names, schemas, paths, and sandbox execution, but no test or review gate establishing that the capability deserves durable reuse.
- llm-do's `agent_create` itself requires approval unless policy pre-approves it. Creation validates requested tool and toolset names against registries. Cross-run promotion remains manual and outside the current dynamic-agent activation path.

Generation, mechanical validity, admission, and demonstrated improvement are therefore four different claims. Automatic retention does not prove improvement. Human approval does not convert model-authored code into human-authored code. A persisted but undiscovered file does not establish operative retention.

## Authority and approval through the enclosing runtime

### RLM

The RLM pattern specifies a model-authored program and a recursive inference primitive. It does not determine an effect or approval model. A pure implementation may expose only computation and recursive calls. Fractal adds a Docker/SBX environment with direct workspace mounts and no network by default. The llm-do example supplies a restricted in-process REPL and recursive access to its registered `rlm` agent under llm-do's ordinary runtime policy. These are host choices, not RLM properties.

### Claude Code workflows

The workflow script cannot use filesystem, shell, or Node APIs directly. Effects occur through subagents. Claude Code separately asks whether to launch the generated workflow, then runs subagents in `acceptEdits` mode with the session tool allowlist. Shell, web, or MCP effects outside that allowlist can still prompt through the Claude Code client during the run. In headless modes, configured permission rules replace interactive confirmation.

This is parent-runtime mediation: the generated script composes calls, while the enclosing runtime owns both the subagent capability surface and the user channel. The inspected evidence establishes same-session journaling and resume, but does not establish that an unresolved permission request itself survives loss of the session or client.

### Tendril capabilities

Tendril's generated TypeScript executes under runtime-supplied Deno flags: workspace read/write, configured network scope, `--no-prompt`, timeout, and output limit. Registration places the capability directly in a human-browsable workspace registry. The existing review did not establish a capability-request/grant protocol or a per-execution user approval path. The correct value is `not established`, not an inference that the capability owns approval.

### llm-do dynamic agents

`agent_create` can request existing tool and toolset names but cannot invent a registry capability. The creation call itself goes through `DynamicAgentsToolset.needs_approval`. `agent_call` can be pre-approved or prompted according to run and per-agent configuration. Once called, the generated agent's tools are materialized and wrapped through the same approval callback used for static agents.

This is a useful separation of three decisions:

1. admit a generated agent definition into the session;
2. authorize invocation of that agent;
3. authorize consequential effects attempted inside the child call.

The current callback may be awaited, so the dependent tool call blocks causally while the runtime and TUI can remain asynchronous. The state is in-process. The inspected implementation does not journal the suspended continuation or preserve a pending approval across process loss. Headless `prompt` denies when no callback can ask a user. This supports interactive nested approval, not durable approval suspension.

## What the pilot changes in the review method

### A mechanism comparison is not a runtime review

A runtime review should have one operational system as its target. It may analyze a subsystem in depth, but must attribute each guarantee to the layer that implements and wires it. A cross-cutting workshop pilot may compare mechanisms across systems, provided every row names the enclosing runtime and does not turn the mechanism's API into a system boundary.

### Dynamic extension needs an activation path

The protocol's authorship, persistence, and target fields remain useful but incomplete. Reviews also need:

- generated artifact identity;
- admission decision and decision maker;
- storage lifetime;
- activation or discovery path on later runs;
- authority available at creation, invocation, and nested effects;
- rollback and retirement path.

Without activation, persistence is archival rather than operative. Without an enclosing-system record, approval and recovery properties are easily attributed to the wrong layer.

### Approval belongs at several boundaries

“Does generated code require approval?” conflates at least three questions:

- Must the generated artifact be admitted?
- Must a principal be authorized to invoke it?
- What happens when its execution requests an effect outside its grant set?

The answers can differ. llm-do exposes all three positions. Claude Code separates workflow launch from mid-run subagent effects. RLM intentionally leaves every position to its host. Tendril currently emphasizes sandbox configuration and durable registration rather than a live approval protocol.

### Self-modification is an end-to-end path

For this workshop, runtime self-modification requires:

1. an in-boundary process generates the concrete change;
2. an admission path makes it part of the bounded runtime's own behavior-determining organization;
3. later operation discovers and exercises it beyond the generating run.

Persistence of source bytes establishes storage, not operative admission. It contributes to the second step, while the third requires a wired discovery and activation path. This is why the current llm-do dynamic-agent path is not yet durably operative even though it writes `.agent` files.

## Candidate conditional requirements

This pilot does not settle a universal runtime contract. It supports conditional requirements for runtimes that claim dynamic extension.

**For run-local generated execution:**

- define the generated unit, namespace, principal, lifetime, result contract, and resource bounds;
- construct an explicit capability surface and prevent the guest program from minting authority;
- route nested calls through the runtime's normal identity, policy, event, cancellation, and error paths;
- retain enough source and provenance to explain the run.

**For durable generated extension:**

- distinguish artifact storage from later discovery and activation;
- define admission, version, compatibility, rollback, retirement, and conflict semantics;
- retain authorship and evidence provenance across promotion;
- state whether a generated extension changes a project capability surface, runtime policy, or protected runtime machinery.

**When unresolved authority can arise:**

- distinguish approval of creation, invocation, and nested effects;
- identify which principal requests authority and which client or policy resolver answers;
- suspend only dependent work and define denial, cancellation, and retry semantics;
- add durable suspension only when the claimed work requires approvals to survive client or process loss.

These are candidate requirements tied to claimed work stories. The next synthesis must still classify them as general, conditional, or safely externalized.

## Next step

The [provisional requirements map](./agent-runtime-requirements-map.md) now combines this pilot with the earlier Pi–Swamp–Exo pilot. Its next test is to review Claude Code and Fractal as enclosing runtimes rather than treating their generated programs as peer runtimes.
