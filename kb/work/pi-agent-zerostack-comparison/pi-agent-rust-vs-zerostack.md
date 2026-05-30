---
description: "Code-grounded comparison of pi_agent_rust and zerostack as Rust coding-agent applications, focusing on agent loops, TUI design, tool safety, extensibility, performance, and workflow"
type: kb/types/note.md
traits: [has-comparison, has-implementation]
status: seedling
---

# The Rust ports of TypeScript Pi split between governed runtime and small TUI workbench

`pi_agent_rust` and `zerostack` are both Rust ports of Pi, the TypeScript coding agent, but they interpret that lineage differently. `pi_agent_rust` treats the port as a chance to make the agent runtime itself the product: provider adapters, an explicit evented loop, branchable sessions, extension hostcalls, policy gates, replay artifacts, evidence contracts, and TUI controls are all first-class surfaces. `zerostack` treats the port as a compact terminal workbench: a Rig-backed chat loop, direct file and shell tools, prompt modes, permission prompts, MCP tools, optional loop automation, and git worktree movement are exposed through a small TUI. The shared vocabulary is "Rust port of TypeScript Pi"; the architectural split is governable runtime versus minimal interactive coding appliance.

**Sources:** local checkouts `related-systems/pi_agent_rust` and `related-systems/zerostack`; both source trees were clean when inspected.

**Reviewed revisions:** `pi_agent_rust` `28b69b1f306d34cc0d15cb743c90e1c30c0da5e6`; `zerostack` `6800987104d5e15fce7d485c8bac5d32e4d39146`.

## TLDR

Both projects are Rust ports of the TypeScript Pi agent, so the interesting difference is not lineage; it is product theory. `pi_agent_rust` asks what a Rust port can become if the runtime is the product: explicit loop ownership, session trees, extension policy, replay, evidence gates, and operational governance. `zerostack` asks how small the port can stay while still feeling like a useful coding workbench: Rig owns the agent loop, the TUI owns the workflow, and prompt modes, permissions, MCP, loops, and worktrees cover the daily path.

The most important split is branch semantics. `pi_agent_rust` branches conversations with parent links, selected leaves, forks, and branch summaries that can re-enter context. `zerostack` branches workspaces with git worktrees and loop plans, which is practical for coding but does not create a first-class parent/child conversation boundary.

The safety split is also sharper than the READMEs suggest. `pi_agent_rust` has serious governance around extensions, trust, evidence, and hostcalls, but ordinary built-in bash is not the same kind of user-visible approval flow. `zerostack` has the clearer operator-facing permission story for day-to-day tools, even though its overall governance and replay layer is much thinner.

## Full Review

## System Profiles

`pi_agent_rust` is the larger, runtime-oriented Rust port of the TypeScript Pi agent. `src/main.rs` routes many subcommands through startup-fast paths before building the async runtime, while `src/cli.rs` exposes provider, model, session, RPC, ACP, extension, skill, prompt-template, theme, search, doctor, replay, validation, and migration surfaces. The core loop in `src/agent.rs` owns turn boundaries, streaming, tool execution, hook dispatch, auto-retry events, latency breakdowns, steering messages, cancellation, and tool-effect batching. The TUI in `src/interactive/view.rs`, `src/interactive/commands.rs`, `src/interactive/tree.rs`, and `src/interactive/tree_ui.rs` is one interface onto a broader runtime that also has extension policy, session storage, provider routing, and evidence-gate machinery.

`zerostack` is the smaller, workbench-oriented Rust port of the TypeScript Pi agent. `src/main.rs` assembles configuration, context files, sessions, permissions, MCP tools, and the selected provider, then runs either print mode, the optional headless loop, or the TUI. The agent loop is mostly delegated to Rig in `src/agent/runner.rs` and `src/agent/builder.rs`; zerostack maps Rig stream items into a small local `AgentEvent` enum in `src/event.rs`. The product surface is concentrated in `src/ui/mod.rs`, `src/ui/slash.rs`, `src/ui/renderer.rs`, `src/ui/status.rs`, prompt packs under `prompts/`, and direct tool implementations under `src/agent/tools/`.

## Product And TUI Model

`pi_agent_rust`'s TUI is an operations console for a runtime. `src/interactive/commands.rs` supports login/logout, model switching, scoped models, settings, themes, session resume, export, copy, hotkeys, changelog, tree, fork, compaction, reload, template expansion, and sharing. `src/interactive/view.rs` renders a header with model, branch indicators, resource counts, thinking and bash badges, pending messages, session pickers, settings and theme pickers, branch selectors, markdown-rendered messages, and tool output summaries. The UI makes runtime state visible: model scope, branch position, resources, tools, extension overlays, and degraded route evidence are part of the working surface.

Zerostack's TUI is deliberately narrower. `src/ui/mod.rs` drives a crossterm event loop with scrollback, mouse selection and copy, reasoning visibility, interrupt behavior, permission prompts, auto-compaction, and loop continuation. `src/ui/slash.rs` exposes model switching, session list/load/delete, reasoning toggle, permission mode switching, MCP listing, todo-tool toggles, compression, loop start/stop, prompt selection, prompt regeneration, worktree creation, worktree merge/exit, undo, retry, clear, and help. `src/ui/status.rs` shows cwd, model, optional loop label, token usage, state, compaction count, prompt name, and non-standard permission mode. The UI makes the common coding workflow cheap, but it does not expose a separate runtime control plane.

The difference matters for what a user can reason about. In `pi_agent_rust`, the TUI is a view over retained runtime structure: session trees, provider route evidence, extension policy, resources, packages, and replay/gate artifacts. In zerostack, the TUI is the primary structure: prompt mode, current session, permission mode, loop state, and cwd/worktree are the behavior-shaping state the user mostly sees.

## Runtime Decomposition

`pi_agent_rust` separates scheduler, context engine, and execution substrate more explicitly. The scheduler is the application-owned loop in `src/agent.rs`: it constructs provider context, streams model events, detects tool calls, batches compatible tools by `ToolEffects`, applies extension hooks, queues steering messages, enforces iteration limits, and emits `TurnEnd` events with latency breakdowns. The context engine spans sessions, compaction, prompt templates, skills, resource loading, tree navigation, and context preview paths in `src/session.rs`, `src/compaction.rs`, `src/interactive/tree_ui.rs`, and `src/main.rs`. The execution substrate is a mix of built-in tools in `src/tools.rs`, provider adapters in `src/providers/`, extension hostcalls in `src/extensions.rs` and `src/extensions_js.rs`, and governance helpers such as `src/resource_governor.rs` and `src/validation_broker.rs`.

Zerostack collapses more boundaries into the workbench. Rig owns the multi-turn tool loop in `src/agent/runner.rs`; zerostack's scheduler-level code decides when to call Rig, when to start a loop iteration, when to compact, and how to respond to UI commands. The context engine is compact and file-oriented: `src/context/mod.rs` loads global and ancestor `AGENTS.md` / `CLAUDE.md`, `src/context/prompts.rs` loads prompt modes, and `src/session/mod.rs` supplies prior messages plus compaction summaries. The execution substrate is direct: file tools, bash, grep, find, list, MCP wrappers, and optional bubblewrap command wrapping in `src/sandbox.rs`.

Neither system is "just a CLI." `pi_agent_rust`'s CLI exposes a runtime with explicit control surfaces. Zerostack's CLI exposes a small agentic workbench whose scheduler is split between Rig, the TUI loop, and optional workflow commands.

## Sub-Agents And Session Trees

`pi_agent_rust` has an explicit conversation tree and fork model. `docs/tree.md` documents session entries with `id`, `parentId`, and a current leaf pointer. `src/session.rs` implements branch summaries, fork plans, navigation, branch creation, current-path entries, and sibling branches. `src/interactive/tree.rs` and `src/interactive/tree_ui.rs` expose `/tree` and `/fork`, including branch selectors, user-message targets, forked sessions, prefilled selected text, and optional branch summaries generated through compaction. The unit of branching is a session entry path, not a git branch. The operative part of the retained artifact is the parent-link graph plus the selected leaf and optional branch summary; its behavioral authority is prompt assembly and UI navigation.

`pi_agent_rust` also has swarm, replay, validation, and resource-governance artifacts in `src/swarm_activity_ledger.rs`, `src/swarm_flight_recorder.rs`, `src/swarm_progress_slo.rs`, `src/swarm_replay.rs`, `src/validation_broker.rs`, `docs/swarm-*.md`, and `docs/contracts/*.json`. These make multi-agent or long-running operational governance visible as CLI and evidence surfaces. In the inspected code, however, ordinary interactive chat remains a single application-owned agent loop. The swarm materials are best read as replay, ledger, SLO, validation, and operator-handoff machinery rather than as proof that the default TUI runs a live multi-agent controller.

Zerostack has no explicit conversation tree, forked-session abstraction, or sub-agent boundary in the inspected code. Sessions are linear JSON conversations in `src/session/mod.rs` and `src/session/storage.rs`; compaction creates summaries and removes earlier messages. Worktrees in `src/extras/git_worktree/mod.rs` and `/worktree`, `/wt-merge`, `/wt-exit` in `src/ui/slash.rs` create and move through git workspaces, but they are filesystem/git branches, not agent-child branches. The optional loop feature in `src/extras/loop/mod.rs` is a stateful prompt scheduler around `LOOP_PLAN.md`; it can continue iterations and save transcripts, but it does not create separate child agents with separate tool surfaces.

The practical consequence is not that zerostack is weaker in every workflow. Its simpler model gives users fewer state types to reconcile. The cost is that any fresh-frame delegation, branch comparison, or parent/child handoff must be approximated with prompts, sessions, worktrees, and filesystem state rather than represented as a first-class runtime structure.

## Comparison Matrix

| Axis | pi_agent_rust | zerostack |
| --- | --- | --- |
| Core product surface | Rust port of TypeScript Pi as governed terminal runtime and extensible platform with TUI, CLI, replay, validation, extension, and session-tree surfaces. | Rust port of TypeScript Pi as small TUI-centered coding workbench with direct tools, prompt modes, permissions, MCP, loop automation, and worktree helpers. |
| Loop ownership | Application-owned loop in `src/agent.rs`; `pi_agent_rust` controls turn events, tool batching, hook dispatch, retries, steering, latency, and cancellation. | Framework-owned Rig loop in `src/agent/runner.rs`; zerostack wraps streams, TUI state, sessions, permissions, and optional workflow loops. |
| TUI role | Runtime console with branch/tree controls, model/settings/theme selectors, resources, tool renderers, extension overlays, and route/state visibility. | Compact chat workbench with scrollback, selection/copy, status line, slash commands, permission prompts, loop status, prompts, MCP, and worktrees. |
| Branching | Session tree and `/fork` over conversation entries; branch summaries can cross the boundary back into context. | Linear sessions; git worktrees move filesystem branch state but not conversation parent/child state. |
| Tool execution | Built-in tool registry with declared `ToolEffects`, read/network parallelization, process/write serialization, output limits, cancellation, extension hooks, and latency samples. | Direct Rig tools for read/write/edit/bash/search/list; permission checker and optional bubblewrap apply mainly around bash and path operations. |
| Safety authority | Extension capability policy, persistent decisions, trust lifecycle, dangerous exec mediation, hostcall gating, kill-switch tests, and evidence contracts. Built-in bash execution is constrained more by process hygiene than by an ordinary command approval model. | User-facing permission modes, rule matching, external path checks, doom-loop detection, AllowOnce/AllowAlways prompts, session allowlist, and optional sandbox wrapping for bash. |
| Context | Skills, prompt templates, resource loading, sessions, compaction, branch summaries, context preview, provider options, and extension resources. | Global and ancestor `AGENTS.md` / `CLAUDE.md`, prompt modes, session history, compaction summaries, current cwd, MCP tools, and selected model. |
| Extension surface | JS/QuickJS and native descriptors, hostcalls, extension tools/providers/slash commands/events/UI/session access, policy profiles, package/index commands. | MCP tools, custom providers, prompt packs, config, and built-in tools; no general JS extension host in inspected code. |
| State and replay | JSONL/tree session store, segmented V2 store contracts, SQLite session index, branch summaries, replay previews, swarm ledgers, flight recorder, validation/evidence artifacts. | Pretty JSON sessions, compaction records, permission allowlists, prompt selections, `LOOP_PLAN.md`, per-iteration loop transcripts, git worktree state. |
| Performance posture | Startup fast paths, render cache, segmented session store, event/latency telemetry, large-session evidence artifacts, and release gates around claims. | Small dependency and code surface, current-thread runtime, release-size profile, simple renderer; README footprint claims are less supported by checked evidence. |
| Governance | Claim gating, schema contracts, release evidence tests, TUI E2E tests, trust-onboarding/kill-switch tests, provider gate artifacts. | Mostly direct code behavior and inline tests; no comparable release-gate/evidence-contract layer found in inspected source. |

## Core Differences

**`pi_agent_rust` treats runtime state as a product surface.** Sessions, branches, provider routes, tool effects, extension policies, package metadata, replay traces, and evidence files are retained artifacts that later UI, runtime, validators, or operators can consume. Zerostack treats most retained state as workbench continuity: session JSON, compaction summary, prompt mode, permission allowlist, loop plan, transcript, and cwd/worktree.

**`pi_agent_rust` owns the loop; zerostack wraps one.** `src/agent.rs` is the scheduler in `pi_agent_rust`. It emits structured `AgentEvent`s, batches tools by declared effects, records turn latency, and gives extension hooks a chance to block or modify tool calls. Zerostack delegates the multi-turn loop to Rig and translates stream items into `Token`, `Reasoning`, `ToolCall`, `ToolResult`, `Done`, and `Error` events in `src/event.rs`.

**`pi_agent_rust` branches conversations; zerostack branches workspaces.** `pi_agent_rust`'s `/tree` and `/fork` operate over the session graph and can return branch summaries to the agent context. Zerostack's `/worktree` changes the git workspace and rebuilds the agent with reloaded context; `/wt-merge` defers to an agent prompt for merge/push/delete work. That is useful workflow state, but the parent/child boundary is filesystem state plus a prompt, not a conversation-tree contract.

**`pi_agent_rust`'s safety model is strongest around extensions and governance; zerostack's is strongest around user-visible tool approval.** `pi_agent_rust` has extension capability profiles, persistent permission decisions, dangerous exec mediation, trust states, quarantine, alerts, and tests such as `tests/trust_onboarding_killswitch_sec52.rs`. Zerostack has simple, visible permission modes and prompts in `src/permission/checker.rs` and `src/ui/mod.rs`, plus optional bash sandboxing in `src/sandbox.rs`. For ordinary built-in bash, `pi_agent_rust` should not be credited with the same user-facing approval loop zerostack exposes.

**`pi_agent_rust` has more observability machinery; zerostack has less state to observe.** `pi_agent_rust`'s event stream, route evidence, validation broker, replay previews, extension alerts, TUI E2E artifacts, and release evidence tests make degraded execution inspectable. Zerostack surfaces denials, errors, status, loop activity, compaction counts, and reasoning visibility, but provider/tool internals mostly pass through Rig's abstractions and simple error lines.

## Common Ground

Both systems are Rust ports of the TypeScript Pi coding agent, and that shared lineage explains their common terminal-agent vocabulary: streaming provider calls, session continuity, file and shell tools, prompt/context loading, model/provider selection, compaction, reasoning visibility, and visible tool calls. Both treat `AGENTS.md` / `CLAUDE.md`-style project instructions as behavior-shaping context. Both can operate in print/headless modes as well as interactive TUI modes. Both use retained artifacts to influence later behavior, but they differ sharply in how formal those artifacts are.

## Agentic Architecture Analysis

`pi_agent_rust`'s agent loop is architecturally explicit. `src/provider.rs` defines the provider contract around messages, tools, stream options, and models; `src/providers/mod.rs` selects concrete providers and reports route errors; `src/model_selector.rs` and `src/model_routing.rs` add model search and advisory route evidence. `src/agent.rs` then becomes the scheduler that interprets streamed content and tool calls. Tool execution is not just a callback: `src/tools.rs` declares `ToolEffects`, and `src/agent.rs` plans effect batches so read/network work can run concurrently while writes/processes/barriers serialize.

Zerostack's architecture is smaller because it buys the framework-owned loop. `src/agent/builder.rs` constructs a Rig agent with the system prompt, current prompt mode, context files, tools, MCP tools, and model options. `src/agent/runner.rs` converts session history and compaction summaries into Rig messages and then streams a multi-turn chat. The scheduler that remains in zerostack is product-level: when to compact, whether to continue a loop iteration, how to render events, when to ask permission, and how to rebuild the agent after model, prompt, or cwd changes.

`pi_agent_rust`'s context engine is correspondingly broader. Session history is tree-shaped in `src/session.rs`; compaction in `src/compaction.rs` can summarize discarded content and insert summaries during context construction; prompt templates and resources can be reloaded or expanded; branch summaries can be created when navigating. These are not merely storage choices. The operative parts are selected message paths, summary text, template expansion, resource inclusion, and branch metadata, and their behavioral authority is prompt assembly or runtime routing.

Zerostack's context engine is intentionally easy to inspect. `src/context/mod.rs` loads global and ancestor instruction files, while `src/context/prompts.rs` overlays built-in, global, and local prompt modes. `src/session/mod.rs` stores messages, token estimates, compactions, model/provider, working directory, and permission allowlist. A compaction summary becomes a system-level history prefix in `src/agent/runner.rs`, while prompt mode content is injected when building the agent. That simplicity is operationally attractive, but it makes context scoping mostly conventional rather than structural.

The extension surfaces reveal the clearest product split. In `pi_agent_rust`, `docs/extension-architecture.md` describes QuickJS and native descriptor modes, and the implementation in `src/extensions.rs`, `src/extensions_js.rs`, `src/extension_tools.rs`, `src/extension_events.rs`, and `src/extension_dispatcher.rs` gives extensions hostcalls, tools, events, UI interactions, providers, session access, logging, and policy mediation. Zerostack's integration model is narrower and more standard: MCP clients and tool wrappers in `src/extras/mcp/`, custom provider definitions in `src/provider.rs`, prompt packs, and config.

## State, Trace, And Replay

`pi_agent_rust` has several retained artifact families with different authority. Session files and the V2 session store in `src/session.rs` and `src/session_store_v2.rs` preserve conversation state, branch structure, hash chains, manifests, checkpoints, offset indexes, and migration events. The SQLite session index in `src/session_index.rs` makes session listing and search efficient. Branch summaries affect future context; raw session history supports resume and navigation; V2 manifests and contracts support integrity and migration verification.

`pi_agent_rust`'s replay and evidence layer has audit and release authority rather than ordinary prompt authority. `docs/schema/session_store_v2_contract.json`, `tests/session_store_v2_contract.rs`, `docs/contracts/*.json`, `docs/evidence/*.json`, `docs/provider-*-report.json`, and `tests/release_evidence_gate.rs` encode schemas, gates, and evidence expectations. `docs/swarm-replay-operator-workflow.md`, `src/swarm_replay.rs`, and `docs/schema/swarm_replay_preview.json` point to replayable operational traces. These artifacts should be read as validators, audit triggers, and operator inputs unless a specific runtime path consumes them during chat.

Zerostack's retained artifacts are more directly user-workflow shaped. `src/session/storage.rs` writes pretty JSON sessions under the data directory. `src/session/mod.rs` records messages, compactions, token/cost estimates, current provider/model, working directory, and a permission allowlist. `src/extras/loop/mod.rs` uses `LOOP_PLAN.md` and previous summaries/validation output to build the next loop prompt; `src/extras/loop/transcript.rs` saves per-iteration JSON transcripts. Git worktrees retain filesystem branch state and are later consumed by git and by the rebuilt agent context.

The important distinction is stored trace versus next context. `pi_agent_rust` stores enough structure to choose a leaf, fork from a user message, and optionally summarize a branch before returning to the model. Zerostack stores linear history and compaction summaries; `src/agent/runner.rs` decides what portion re-enters the next Rig call. A zerostack loop transcript supports debugging and audit, but the next iteration is shaped primarily by `LoopState::build_prompt`, `LOOP_PLAN.md`, prior summary, and validation output, not by replaying the transcript.

## Observability And Degraded Execution

`pi_agent_rust` exposes many degraded-execution signals. `src/agent.rs` emits start/end events, tool events, error events, turn latency breakdowns, tool iteration cap handoff text, and auto-retry events in print mode. `src/model_routing.rs` can report recommended, degraded, temporarily avoided, stale, or missing route evidence. Extension policy explanations in `src/extensions.rs` describe effective allow/deny state, dangerous capability status, and trust decisions. Tests such as `tests/e2e_tui.rs`, `tests/release_evidence_gate.rs`, and `tests/trust_onboarding_killswitch_sec52.rs` show that some UI, evidence, and security claims are exercised beyond README text.

Zerostack surfaces failures where the user needs immediate control: permission denials, permission prompts, external path checks, doom-loop asks, provider/tool errors, sandbox command failures, session load/delete ambiguity, loop status, and visible `error:` lines. `src/ui/mod.rs` also lets the user interrupt, toggle reasoning, inspect tool call/result lines, and see status. The weaker observability point is that Rig owns much of the multi-turn loop, and the UI mostly sees the mapped stream events. Ctrl+C drops the running receiver path in the TUI, but the inspected code did not show a rich cancellation/provenance model comparable to `pi_agent_rust`'s evented runtime.

There are also safety-edge differences worth preserving. Zerostack's validation command in headless loop mode is run as `sh -c` from `src/main.rs`; it is a workflow validation step rather than a normal permission-mediated tool call. `pi_agent_rust`'s built-in bash tool has process-group cleanup, timeout, output truncation, and artifact spill behavior in `src/tools.rs`, but ordinary built-in bash is not the same as zerostack's interactive permission prompt model. In both cases, the real guarantee is narrower than a simple "safe shell" label would imply.

## Borrowable Ideas

`pi_agent_rust`'s session tree is immediately borrowable for agentic CLIs that need real branch hygiene. A branch should be a retained artifact with parent links, selected leaf, branch summaries, and clear prompt authority, not merely a named transcript file.

Zerostack's permission UI is borrowable because it is comprehensible. Standard/restrictive/accept/yolo modes, external path checks, AllowOnce/AllowAlways, and session allowlists are easy for an operator to predict. A larger runtime can keep `pi_agent_rust`-style policy diagnostics while still adopting zerostack's direct approval ergonomics for ordinary tools.

`pi_agent_rust`'s tool-effect batching is a useful middle ground between fully serial and blindly parallel tool execution. Declared read/write/network/process/barrier effects give the scheduler enough structure to parallelize low-risk calls without pretending every tool is independent.

Zerostack's prompt modes and `LOOP_PLAN.md` loop show how far a simple stateful scheduler can go before sub-agents are necessary. For commonplace workflows, this suggests a lightweight pattern: retain a plan file and validation output as explicit operative parts before promoting to a more complex multi-agent workflow.

`pi_agent_rust`'s evidence-gate habit is borrowable for claims that otherwise become README drift. Release-facing claims about performance, provider support, extension safety, or replay should have schema-backed artifacts and tests like `tests/release_evidence_gate.rs`, not just prose.

Zerostack's worktree commands are a good terminal workflow affordance, but they should be treated as workspace branching rather than agent branching. A future system could combine zerostack's git ergonomics with `pi_agent_rust`'s conversation fork summaries so code branch and context branch stay aligned.

## Curiosity Pass

- `pi_agent_rust`'s swarm and evidence surfaces sound like a live multi-agent operating system, but the inspected ordinary chat path is still a single explicit loop. The powerful part that is clearly implemented is governance: ledgers, replay previews, SLO/evidence artifacts, validation, and operator-facing gates.
- Zerostack's loop sounds like autonomous coding, but its simpler mechanism is a prompt scheduler around `LOOP_PLAN.md`, previous summary, optional validation output, and repeated Rig calls. That may be enough for many tasks and is easier to reason about than hidden sub-agent trees.
- README performance claims for zerostack are plausible given the small codebase and release profile, but the inspected source did not contain evidence gates comparable to `pi_agent_rust`'s `docs/evidence/*.json` and release tests.
- `pi_agent_rust`'s extension runtime is broad enough that its policy model matters as much as its tool model. Future review should check which hostcall paths are hot in normal user workflows rather than assuming every documented hostcall is commonly exercised.
- A future zerostack conversation-tree or explicit child-agent feature would change the comparison substantially. A future `pi_agent_rust` workflow that wires swarm controllers into ordinary TUI work would likewise move `pi_agent_rust` from governed runtime toward live orchestration platform.

## What to Watch

- Whether `pi_agent_rust` converts its swarm, validation, and replay artifacts into ordinary interactive scheduling paths, or keeps them as governance and operator surfaces.
- Whether `pi_agent_rust` adds a user-facing ordinary-tool approval model comparable to zerostack's permission prompts.
- Whether zerostack keeps Rig loop ownership as the project grows, or pulls turn scheduling, cancellation, retries, and tool batching into application code.
- Whether zerostack's worktree workflow grows an explicit context-branch contract so git branch state and conversation state can be reconciled.
- Whether either project makes compaction summaries inspectable and editable enough that users can control what authority summaries have in future turns.
- Whether performance claims remain source-evidenced as both projects accumulate provider, TUI, extension, and workflow features.

---

Relevant Notes:

- [Agent runtimes decompose into scheduler context engine and execution substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md) grounds the scheduler/context/execution split used above.
- [Agent orchestration occupies a multi-dimensional design space](../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) explains why `pi_agent_rust`'s tree, replay, and governance surfaces should not be collapsed into a single "more agentic" ladder.
- [Conversation vs prompt refinement in agent-to-agent coordination](../../notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) clarifies the difference between `pi_agent_rust` branch summaries, zerostack prompt loops, and raw transcript inheritance.
- [Session history should not be the default next context](../../notes/session-history-should-not-be-the-default-next-context.md) frames the distinction between stored traces and what gets loaded into the next model call.
- [LLM context is composed without scoping](../../notes/llm-context-is-composed-without-scoping.md) explains why first-class branches or child-agent frames matter when context contamination becomes a design problem.
- [Stateful tools recover control by becoming hidden schedulers](../../notes/stateful-tools-recover-control-by-becoming-hidden-schedulers.md) helps interpret zerostack's loop feature as scheduler relocation rather than true sub-agent delegation.
- [Apparent success is an unreliable health signal in framework-owned tool loops](../../notes/apparent-success-is-an-unreliable-health-signal-in-framework-owned.md) motivates the emphasis on observability, replay, and degraded-execution signals.
