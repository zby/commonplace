# Review Instruction: pi_agent_rust vs zerostack

## Goal

Produce a code-grounded comparative review of `pi_agent_rust` and `zerostack` as Rust coding-agent applications: full agentic software systems with terminal user interfaces.

The review should not summarize two READMEs side by side. It should identify the architectural choices each system makes about the agent loop, TUI interaction model, tool execution, permissions, provider integration, extensibility, performance, operational governance, packaging, and user workflow, then say what those choices imply for agentic software design.

The main comparison question:

> What does each project treat as the core product surface of a coding agent: a fast terminal app, a governed runtime, an extensible platform, a prompt/workflow launcher, a TUI-centered workbench, or some combination?

## Inputs

Use these local source directories:

- `source_dir_a`: `related-systems/pi_agent_rust`
- `source_dir_b`: `related-systems/zerostack`

At the time this instruction was written, the local revisions were:

- `pi_agent_rust`: `28b69b1f306d34cc0d15cb743c90e1c30c0da5e6`
- `zerostack`: `6800987104d5e15fce7d485c8bac5d32e4d39146`

Re-establish the revisions before writing the review. If either directory has moved, been refreshed, or has uncommitted local changes relevant to the review, report that in the source metadata.

## Establish Source State

Before reading mechanism files, run:

```bash
test -d related-systems/pi_agent_rust
test -d related-systems/zerostack
git -C related-systems/pi_agent_rust rev-parse HEAD
git -C related-systems/zerostack rev-parse HEAD
git -C related-systems/pi_agent_rust status --short
git -C related-systems/zerostack status --short
```

Do not fetch, pull, update dependencies, run installers, or mutate either repo. The review should inspect the checked-out source state.

## Review Discipline And Background

Use the existing code-grounded related-system review materials as style and evidence-discipline references. Their subject matter is narrower than this comparison, but their source-grounding habits are useful: ground claims in source code, distinguish implemented mechanisms from documented aspirations, classify behavior-shaping artifacts precisely when useful, and make borrowable ideas concrete.

Use these local conceptual lenses when they clarify the comparison:

- **Runtime decomposition:** separate scheduler, context engine, and execution substrate. A filesystem is not a scheduler; a tool runner is not a context engine; a TUI may expose or hide all three.
- **Loop ownership:** ask where the next-step policy lives: framework loop, LLM conversation, symbolic scheduler, stateful tool, extension runtime, loop command, worktree workflow, or swarm controller.
- **Scoping and branching:** sub-agents, session trees, and forks are mechanisms for fresh frames, capability-surface changes, and parent/child coordination, not just convenience UI.
- **Handoff artifacts:** distinguish raw transcript inheritance, prompt refinement, compressed return artifacts, branch summaries, replay traces, and generated evidence files.
- **Observability:** final task success is not enough; check whether the system exposes degraded execution, fallback paths, tool failures, retries, branch state, and provenance.

Use this vocabulary inline:

- **Retained artifact:** state that persists across time and can later be consumed by an agentic loop in a behavior-shaping way. The boundary is behavioral consequence, not storage label. A session file, prompt pack, extension registry, validator, route table, replay trace, worktree branch, or generated evidence artifact counts only when some later model, runtime, router, validator, retriever, reviewer, or learning loop can use it to change what happens.
- **Operative part:** the behavior-affecting content, structure, parameterization, or mechanism inside a retained artifact or consumption path. Classify the part that actually shapes behavior, not the whole stored object. For example, a prompt file may contain prose instruction plus symbolic section contracts; a session tree may contain raw transcript, branch metadata, and a selected handoff summary.
- **Behavioral authority:** how a retained artifact or operative part becomes behavior-shaping: who consumes it, through which channel, and with what force. Consumers can include models, runtimes, routers, validators, reviewers, maintainers, assemblers, or learning loops. Channels include prompt assembly, execution, configuration, validation, routing, ranking, review, and training. Force can be advice, instruction, enforcement, ranking influence, audit trigger, or learning input.

Keep these review-time questions:

- What is the main product theory: minimal fast CLI, integrated terminal IDE, extensible runtime, safety-governed tool runner, or automated coding workflow?
- How do scheduler, context engine, and execution substrate appear in each codebase, and which boundaries are explicit versus collapsed?
- How is the agent loop structured: prompt assembly, provider streaming, tool-call dispatch, event handling, cancellation, retries, and turn boundaries?
- Where does orchestration live: inside the chat/tool loop, in symbolic code, in a stateful tool/runtime, in a prompt mode, in extension machinery, or in a separate loop/workflow feature?
- Does the system support sub-agents, agent forks, session trees, branchable conversations, work delegation, swarm/multi-agent orchestration, or similar structures? If so, what is the unit of branching, how is parent/child state represented, and how does the TUI expose it?
- What crosses execution boundaries: raw conversation, refined prompt, structured result, compressed episode, replay trace, branch summary, or filesystem/worktree state?
- How does the TUI shape work: input model, message rendering, markdown/code display, status surfaces, slash commands, selection/copy, scrolling, progress, model/tool visibility, and error display?
- What state is retained across turns or sessions, and what authority does it have: resume convenience, UI continuity, workflow plan, policy, audit evidence, replay input, or future behavior instruction?
- How are tool calls governed: permission modes, command mediation, sandboxing, external path policy, dangerous command detection, resource limits, and operator prompts?
- How does each system make failure visible: denied tools, blocked commands, retries, fallback paths, degraded guarantees, stalled loops, branch conflicts, provider failures, or extension failures?
- How do provider/model abstractions affect user workflow and implementation complexity?
- What extension surfaces exist: MCP, JS/WASM extensions, prompt packs, SDKs, slash commands, hooks, config files, or custom tools?
- How does each project handle performance as product experience: startup time, memory footprint, streaming latency, large-session behavior, and TUI responsiveness?
- What operational guarantees are actually enforced by code, tests, contracts, release gates, or evidence artifacts?
- Which ideas are worth borrowing for future agentic CLIs, TUIs, or commonplace workflows?

Reference loading:

The conceptual material above is the frontloaded brief. Do not read every reference in full before source inspection.

Use these broad indexes as navigation before or during source inspection:

- `kb/notes/context-engineering-index.md`, for routing, loading, scoping, scheduling, and maintenance questions under bounded context
- `kb/notes/computational-model-index.md`, for the select/call model, scoping, sub-agent isolation, session-history tradeoffs, and orchestration dimensions
- `kb/notes/tool-loop-index.md`, for loop ownership, sub-agent forcing cases, and hidden-scheduler tradeoffs
- `kb/notes/observability-index.md`, for runtime visibility and degraded-execution signals

Read these targeted notes early only if their topic is central to the emerging comparison:

- `kb/notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md`, when mapping runtime components
- `kb/notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md`, when comparing scheduler placement, persistence horizon, coordination form, coordination guarantees, or boundary-return artifacts
- `kb/notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md`, when comparing conversation, prompt refinement, forking, or sub-agent handoff
- `kb/notes/session-history-should-not-be-the-default-next-context.md`, when comparing session resume, transcript inheritance, compaction, or trace loading
- `kb/notes/llm-context-is-composed-without-scoping.md`, when comparing sub-agent isolation, branch contamination, or context hygiene
- `kb/notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent.md`, when comparing delegated work or changing tool surfaces
- `kb/notes/stateful-tools-recover-control-by-becoming-hidden-schedulers.md`, when a tool, extension, loop command, or runtime appears to own scheduling
- `kb/notes/apparent-success-is-an-unreliable-health-signal-in-framework-owned.md`, when comparing failure visibility, fallback paths, or degraded-execution reporting

Style and vocabulary references:

- `kb/agent-memory-systems/types/agent-memory-system-review.md`, for evidence discipline and precise artifact analysis
- `kb/agent-memory-systems/reviews/pi-self-learning.md`, for Pi ecosystem context and trace/extension comparison if useful
- 1-2 recent reviews in `kb/agent-memory-systems/reviews/`, to match local source-grounding style

For style references, skim enough to match the source-grounded review style. Full reads are only needed when the final review makes a load-bearing claim that depends on details not included in the frontloaded brief.

## Source Reading Plan

### Shared first pass

For both repositories, read:

- `README.md`
- `Cargo.toml`
- CLI entry points and argument definitions
- TUI state, rendering, input, slash-command, and status modules
- sub-agent, branch, fork, tree, swarm, scheduler, replay, and work-delegation modules
- session storage and compaction code
- provider/model routing code
- tool execution and permission code
- prompt/context-loading code
- loop/workflow orchestration code
- extension, MCP, hook, or plugin surfaces
- packaging/install/release metadata
- tests or evidence artifacts that claim behavioral guarantees

Treat README performance or safety claims as hypotheses until source files, tests, contracts, or evidence artifacts support them.

### pi_agent_rust focus files

Start with:

- `src/main.rs`
- `src/cli.rs`
- `src/agent.rs`
- `src/app.rs`
- `src/interactive.rs`
- `src/interactive/agent.rs`
- `src/interactive/commands.rs`
- `src/interactive/conversation.rs`
- `src/interactive/state.rs`
- `src/interactive/tool_render.rs`
- `src/interactive/tree.rs`
- `src/interactive/tree_ui.rs`
- `src/interactive/view.rs`
- `src/agent_cx.rs`
- `src/scheduler.rs`
- `src/tui.rs`
- `src/theme.rs`
- `src/session.rs`
- `src/session_store_v2.rs`
- `src/session_sqlite.rs`
- `src/session_index.rs`
- `src/compaction.rs`
- `src/compaction_worker.rs`
- `src/tools.rs`
- `src/permissions.rs`
- `src/model_selector.rs`
- `src/model_routing.rs`
- `src/provider.rs`
- `src/providers/*.rs`
- `src/extensions.rs`
- `src/extensions_js.rs`
- `src/extension_dispatcher.rs`
- `src/extension_events.rs`
- `src/extension_tools.rs`
- `src/extension_validation.rs`
- `src/extension_replay.rs`
- `src/resource_governor.rs`
- `src/validation_broker.rs`
- `src/semantic_workspace_graph.rs`
- `src/swarm_activity_ledger.rs`
- `src/swarm_flight_recorder.rs`
- `src/swarm_progress_slo.rs`
- `src/swarm_replay.rs`
- `docs/context-intelligence.md`
- `docs/extension-architecture.md`
- `docs/extension-runtime-threat-model.md`
- relevant `docs/contracts/*.json` and `docs/evidence/*.json`

Read selectively from tests where the code claims enforcement, replay, conformance, security, TUI behavior, provider behavior, or evidence gates. This repo has enough docs and generated-looking artifacts that the review must separate implemented mechanisms from aspirational planning.

### zerostack focus files

Start with:

- `src/main.rs`
- `src/cli.rs`
- `src/agent/builder.rs`
- `src/agent/runner.rs`
- `src/agent/prompt.rs`
- `src/context/mod.rs`
- `src/context/prompts.rs`
- `src/session/mod.rs`
- `src/session/storage.rs`
- `src/provider.rs`
- `src/ui/events.rs`
- `src/ui/input.rs`
- `src/ui/markdown.rs`
- `src/ui/mod.rs`
- `src/ui/renderer.rs`
- `src/ui/slash.rs`
- `src/ui/status.rs`
- `src/ui/terminal.rs`
- `src/permission/checker.rs`
- `src/permission/pattern.rs`
- `src/sandbox.rs`
- `src/agent/tools/*.rs`
- `src/extras/loop/mod.rs`
- `src/extras/loop/plan.rs`
- `src/extras/loop/transcript.rs`
- `src/extras/git_worktree/mod.rs`
- `src/extras/mcp/*.rs`
- `prompts/*.md`

Read selectively for where prompts, `AGENTS.md` / `CLAUDE.md`, sessions, loop plans, tool approvals, sandboxing, MCP, TUI events, slash commands, and worktree operations become product-defining. Check explicitly whether zerostack has any conversation branching, sub-agent, worktree-as-agent-branch, or delegated-work abstraction; if absent, treat the absence as a design choice only after source inspection. This repo is intentionally small; the review should not mistake small surface area for missing architecture without checking the code.

## Comparison Axes

Use these axes as the reading inventory. Do not mechanically produce an 18-row checklist if the evidence clusters more cleanly. For the published comparison matrix, merge adjacent axes and foreground the dimensions where the two systems actually differ.

1. **Product thesis:** what kind of agentic product each project is trying to be: minimal CLI, TUI workbench, extension host, governed runtime, automation harness, or compatibility port.
2. **Runtime decomposition:** how scheduler, context engine, and execution substrate are separated, collapsed, or hidden behind TUI/tool abstractions.
3. **Agent loop architecture:** turn construction, streaming, tool-call handling, cancellation, retries, event bus, background work, and concurrency model.
4. **Scheduler placement and loop ownership:** whether orchestration lives in application code, framework-owned loop, LLM conversation, stateful tool, extension runtime, prompt mode, or workflow command.
5. **Sub-agent and branching model:** sub-agents, session trees, conversation forks, branch selection, task delegation, swarm/multi-agent concepts, worktree-backed branches, and how parent/child context and outputs are represented.
6. **TUI interaction model:** layout, message rendering, input handling, markdown/code display, scrollback, selection/copy, status bars, progress indicators, reasoning visibility, command palette/slash commands, tree/branch navigation, and recoverability after errors.
7. **Workflow orchestration:** one-shot mode, resume, headless loops, planning files, worktree movement, delegated work, multi-agent/swarm concepts, and how the user controls long-running work.
8. **Tool authority and safety:** permission modes, command mediation, sandboxing, external path policy, resource governance, extension hostcalls, policy enforcement, and auditability.
9. **Context and prompt assembly:** project instruction files, prompt packs, selected modes, compaction summaries, prior turns, branch/sub-agent context, models, tool results, and how these are made visible or controllable.
10. **Boundary-return artifacts:** raw transcripts, refined prompts, summaries, branch outputs, loop plans, replay traces, evidence files, structured tool results, and what later stages consume.
11. **Retained state and session lifecycle:** session files, SQLite/indexes, sidecar logs, tree nodes, branch metadata, loop transcripts, prompt selections, plans, ledgers, evidence artifacts, extension registries, and what role each plays.
12. **Extension and integration surface:** built-in tools, MCP, JS/WASM extension runtime, prompt packs, provider abstraction, SDKs, hooks, config files, and plugin affordances.
13. **Provider and model abstraction:** supported providers, model selection, auth handling, streaming protocol handling, provider-specific affordances, and failure modes.
14. **Observability and degraded execution:** how the TUI/runtime exposes tool failures, fallback paths, retries, blocked actions, provider errors, branch state, provenance, and weaker-than-intended execution guarantees.
15. **Performance as UX:** startup latency, memory footprint, binary size, streaming smoothness, large-session resume, TUI responsiveness, branch/tree navigation responsiveness, and how claims are evidenced.
16. **Validation and governance:** tests, conformance matrices, contracts, evidence gates, release gates, manual review paths, and whether they are actually wired into execution.
17. **Adoption and operations:** install path, config burden, cross-platform assumptions, dependency footprint, inspectable files, terminal/git workflow fit, troubleshooting, and upgrade story.
18. **Borrowability:** concrete ideas worth borrowing for agentic CLIs, TUIs, extensions, safety systems, or commonplace workflows, and whether they need current use cases or should remain watch-list items.

## Required Review Shape

Write the review as a comparative analysis, not as two independent system reviews pasted together.

Use this structure unless the evidence strongly argues for another one:

```markdown
---
description: "Code-grounded comparison of pi_agent_rust and zerostack as Rust coding-agent applications, focusing on agent loops, TUI design, tool safety, extensibility, performance, and workflow"
type: kb/types/note.md
traits: [has-comparison, has-implementation]
tags: []
---

# {Claim-shaped title}

{Opening paragraph stating the core finding.}

**Sources:** {repo identities}

**Reviewed revisions:** {two SHAs}

## System Profiles

{One short paragraph per system. State what it is, what it is optimizing for, and what source files support that read.}

## Product And TUI Model

{Explain the product shape and terminal interaction model of each system. Cover layout, input, rendering, status/progress surfaces, commands, visibility into reasoning/tools, branch/tree navigation, and what the TUI makes easy or hard.}

## Runtime Decomposition

{Map each system into scheduler, context engine, and execution substrate. State which boundaries are explicit in code, which are hidden inside tools/extensions/workflow commands, and which are mostly product or TUI conventions.}

## Sub-Agents And Session Trees

{Compare sub-agent, branch, fork, tree, worktree, loop, and swarm mechanisms. State whether each system has an explicit conversation tree or delegated-agent model, how parent/child state is stored, how outputs rejoin the main workflow, and how much of the model is visible in the TUI. If one system lacks the mechanism, explain the practical consequence rather than treating absence as automatically bad.}

## Comparison Matrix

{A compact matrix across the most salient axes above. Keep cells concrete, not generic. Merge axes when that makes the comparison clearer.}

## Core Differences

{3-6 mechanisms or design choices where the projects really diverge. Use bolded lead phrases.}

## Common Ground

{Where both systems converge despite different scope: Rust CLI, session continuity, provider abstraction, permission surfaces, prompt/context files, etc.}

## Agentic Architecture Analysis

{Analyze the agent loop, sub-agent/session-tree model, TUI event model, tool execution path, provider integration, permission/sandbox layer, workflow orchestration, extension surface, and retained state. Use retained-artifact categories where they clarify behavior.}

## State, Trace, And Replay

{Describe sessions, transcripts, ledgers, evidence files, replay mechanisms, loop plans, branch summaries, and compaction outputs. Distinguish stored traces from what gets loaded into the next context. State whether these support resume/debugging, UI continuity, auditability, branching, validation, or future behavior.}

## Observability And Degraded Execution

{Explain how each system surfaces or hides failure and recovery paths: denied tools, blocked commands, retries, provider failures, extension failures, sandbox failures, fallback behavior, stalled loops, branch conflicts, and evidence/provenance gaps. Do not infer runtime health from final task success alone.}

## Borrowable Ideas

{For each idea, say what it would look like in an agentic CLI/TUI or in commonplace, and whether it is ready now or needs a use case first.}

## Curiosity Pass

- {What sounds powerful but may only be presentation or generated planning residue?}
- {What is the simpler mechanism that would achieve most of the effect?}
- {What would change the review if future commits implement it?}

## What to Watch

- {Future changes in either project that would affect agentic software, TUI design, safety, extensibility, or workflow conclusions.}

---

Relevant Notes:

- {Links into existing KB notes, references, or related-system coverage that actually help the reader.}
```

If a required-looking section has little source evidence, keep it brief and say that the mechanism is absent or not visible in the inspected code. Do not pad weak sections to satisfy the template.

## Evidence Discipline

Use source-relative file citations in prose, for example `src/ui/renderer.rs`, `src/interactive/view.rs`, or `docs/evidence/swarm-replay-closeout-gate.json`. Do not create Markdown links into `related-systems/...`; durable KB notes should remain readable without local checkout paths.

When a claim comes from docs rather than executable code, mark it as documented rather than implemented. When code and docs disagree, prefer the code and mention the disagreement if it matters.

Do not run full test suites unless explicitly asked. Selectively reading tests and evidence files is enough for this comparison instruction.

## Final Revision Pass

After drafting the review, read it once more before stopping. Revise for flow, logic, cohesion, and readability:

- Make the opening claim match what the body actually proves.
- Remove checklist residue, duplicated points, and sections that only repeat the matrix.
- Tighten transitions so product/TUI observations connect to architecture and borrowable ideas.
- Check that each comparison is grounded in source evidence rather than README phrasing.
- Keep absent mechanisms concise: say what is absent or not visible, then move on.

## Output Location

Draft the comparative review in the workshop first:

- `kb/work/pi-agent-zerostack-comparison/pi-agent-rust-vs-zerostack.md`

If the draft becomes durable enough to promote, decide the target collection after the review. It may belong in a future broader related-systems area for agentic software and TUI design.
