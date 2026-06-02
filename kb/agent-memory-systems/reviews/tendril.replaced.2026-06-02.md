---
description: "Desktop Strands/Tauri agent sandbox that turns live task needs into workspace-local executable TypeScript capabilities"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-05-16"
---

# Tendril

Tendril is serverless-dna's desktop agent sandbox for the Agent Capability pattern: a Strands-powered sidecar, hosted by a Tauri app, that keeps the model's visible tool surface small while letting it create, register, and reuse executable capabilities in a user-selected workspace. The memory mechanism is not a transcript store. It is live codification: a task request and the agent's tool observations can become a persistent TypeScript file plus registry metadata that future sessions can list and execute.

**Repository:** https://github.com/serverless-dna/tendril

**Reviewed revision:** [e671a4143d28de68289efd81580002041bb4cb6a](https://github.com/serverless-dna/tendril/commit/e671a4143d28de68289efd81580002041bb4cb6a)

## Core Ideas

**The current implementation is a three-tool bootstrap loop.** The README and Agent Capability spec still discuss search/load terminology in places, but the source creates a Strands `Agent` with exactly `listCapabilities`, `registerCapability`, and `execute` tools. `listCapabilities` returns the full capability summary list; `registerCapability` writes metadata and source; `execute` accepts only a registered name and JSON-string args, then loads code internally. That means the live model never gets a broad static tool bag and cannot pass arbitrary code directly to execution through the tool schema. See [`agent.ts`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/agent.ts), [`tools.ts`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/tools.ts), and the spec's older/abstract language in [`docs/agent-capability-spec.md`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/docs/agent-capability-spec.md).

**The system prompt makes capability creation mandatory, not optional advice.** `TENDRIL_SYSTEM_PROMPT` tells the model that every action starts with `listCapabilities`; if no match exists, it must register a capability and then execute it. It also forbids answering from memory when a tool can get live data and routes workspace reads/writes through registered capabilities. This prompt is the main behavioral authority for the loop: it is a system-definition artifact consumed by the Strands agent as instruction. The same prompt is also written to `system-prompt.txt` for the settings UI, where it becomes a knowledge artifact for human inspection. See [`prompt.ts`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/prompt.ts).

**The durable capability substrate is plain workspace files.** `CapabilityRegistry` stores the active index at `{workspace}/tools/index.json` and implementation files at `{workspace}/tools/{name}.ts`. A capability definition contains a snake_case name, one-sentence capability text, trigger strings, suppression strings, `tool_path`, creation date, author, and version. The registry returns only the selection fields to the model, keeping metadata out of the prompt-time decision surface. Upserts replace by name and overwrite the `.ts` file; there is no archive, dependency graph, provenance field beyond `created_by`, or automatic retirement. See [`registry.ts`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/registry.ts), [`types.ts`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/types.ts), and [`registry.test.ts`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/tests/registry.test.ts).

**Execution is symbolic and sandboxed, but the sandbox is intentionally practical rather than proof-grade.** `executeDeno` prepends `args` and `__workspace`, writes a random temp TypeScript file, and runs `deno run` with read/write permissions scoped to the workspace, network either unrestricted or restricted to configured domains, `--no-prompt`, a timeout, cancellation support, and a 1 MB output cap. It does not allow shell access through Tendril's tool API, but generated Deno code remains powerful within the configured filesystem/network boundary. Empty `allowedDomains` means unrestricted network by design. See [`sandbox.ts`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/sandbox.ts), [`config.ts`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/config.ts), and [`sandbox.test.ts`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/tests/sandbox.test.ts).

**The Tauri shell is a protocol host and workspace guard.** The Rust backend spawns the Node SEA sidecar, resolves a bundled Deno path, injects provider API keys, sends ACP-style JSON-RPC over stdin, and routes sidecar stdout `session/update` notifications into Tauri events. It also records host/agent protocol messages into a debug stream and detects rapid sidecar crash loops. Workspace commands reject dangerous roots, create `tools/index.json`, validate file operations against the configured workspace, and expose file/capability browsing commands to the UI. See [`acp.rs`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src-tauri/src/acp.rs), [`events.rs`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src-tauri/src/events.rs), [`workspace.rs`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src-tauri/src/workspace.rs), [`files.rs`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src-tauri/src/files.rs), and [`capabilities.rs`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src-tauri/src/capabilities.rs).

**Live traces are rendered, not retained as memory.** The agent sidecar classifies Strands stream events into think, act, observe, and metadata phases, then emits ACP `session/update` messages for text chunks, tool calls, tool results, token usage, errors, and prompt completion. The React state stores those messages and tool traces in memory for the current app session, while the debug panel keeps a capped in-memory protocol log. Tendril's retained behavior-changing artifact is the registered capability, not the conversation transcript or protocol event stream. See [`index.ts`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/index.ts), [`stream.ts`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/transport/stream.ts), [`protocol.ts`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/transport/protocol.ts), [`AgentContext.tsx`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src/context/AgentContext.tsx), and [`ToolTrace.tsx`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src/components/ToolTrace.tsx).

**The UI treats capabilities as inspectable first-class artifacts.** The app has tabs for chat, capabilities, workspace, and settings. The capability browser reads `tools/index.json`, displays trigger/suppression metadata, and expands to show the TypeScript source loaded through a Tauri command. That makes the executable registry human-auditable even though there is no approval gate before promotion. See [`App.tsx`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src/App.tsx), [`CapabilityBrowser.tsx`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src/components/CapabilityBrowser.tsx), and [`useCapabilities.ts`](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src/hooks/useCapabilities.ts).

## Comparison with Our System

| Dimension | Tendril | Commonplace |
|---|---|---|
| Primary retained unit | Registered executable capability: metadata in `tools/index.json` plus `tools/{name}.ts` | Typed notes, instructions, reviews, indexes, scripts, and validation rules |
| Storage substrate | Local workspace filesystem plus app config under `~/.tendril/config.json` | Git repository as KB, methodology source, and shipped package |
| Representational form | Mixed: prose trigger/suppression metadata plus symbolic TypeScript code | Mostly prose and markdown structure, with symbolic validators/CLI commands |
| Behavioral authority | System-definition artifact when listed/executed by the agent; knowledge artifact when browsed by humans | Notes advise; instructions/skills guide; validators enforce |
| Activation | Always list full registry, model selects by reading summaries, execute by name | `rg`, indexes, descriptions, links, skills, and explicit procedures |
| Learning path | Online trace-to-tool codification during a live task | Mostly deliberate distillation into notes/instructions/scripts, with review and validation |
| Governance | Name validation, workspace scoping, Deno permissions, timeout/output caps, inspectable UI | Type contracts, review gates, status lifecycle, link semantics, validation |
| Lifecycle | Upsert or manual deletion/editing; no archive, tests, provenance chain, or retirement | Current/superseded/outdated states, generated indexes, review workflows |

Tendril is stronger than commonplace at immediate capability externalization. When the current task needs a tool, the agent can write one and use it in the same turn, and the next session inherits the result. That is a direct path from task pressure to executable system-definition artifact. Commonplace usually requires a separate curation act before a repeated procedure becomes a `commonplace-*` command or skill.

Commonplace is stronger on authority, lineage, and lifecycle. Tendril collapses "candidate", "approved", and "active" into one registration step. The model-written triggers and suppression rules guide later selection, but they are not evaluated against examples, linked to source traces, versioned beyond a reset `1.0.0`, or retired on failure. Commonplace is slower because it treats durable behavior-shaping artifacts as things that need typed contracts, review state, validation, and source alignment.

The deeper difference is oracle strength. Tendril has no external judge that a generated capability is generally correct; the live user task and Deno execution result are the only immediate feedback. That makes the loop useful for personal automation and exploration, but risky as a shared capability library. Its best fit is a local, inspectable, low-friction sandbox where the user can browse and edit generated tools.

**Read-back:** pull — agents deliberately list registered capability summaries and execute selected capabilities by name.

## Borrowable Ideas

**Name-gated execution after registration.** `execute` accepts a capability name, not code. A commonplace analogue would be stronger separation between "propose a script/check" and "run an approved named command." Ready to borrow as a safety pattern for any future generated-command workflow.

**Trigger and suppression metadata for executable artifacts.** Tendril requires each capability to say when it should and should not fire. Commonplace skills already use descriptions as activation hints; richer suppression fields would make activation boundaries more reviewable. Ready to borrow for skill authoring where false positives are costly.

**Capability browser beside chat.** The UI makes learned executable artifacts visible without requiring the user to inspect the filesystem manually. Commonplace could use the same idea for generated indexes, active skills, review warnings, and candidate promotions. Needs a UI surface first.

**Local workspace as a personal capability substrate.** Tendril keeps generated tools in the user's chosen workspace, not in a remote service. That fits commonplace's preference for inspectable files and git-friendly artifacts. Ready as a framing; actual borrowing should wait for a generated-capability use case.

**Immediate codification as a mode, not the default.** Tendril shows the high-agency end of the design space: build the tool now, then let inspection/governance catch up. Commonplace should not make that the general KB rule, but it is useful for workshop-layer experiments where fast executable prototypes are acceptable.

## Trace-derived learning placement

**Trace source.** Tendril's source signal is the live deployment interaction: user request text, the current capability summaries from `tools/index.json`, model judgment about trigger/suppression fit, generated TypeScript, JSON args, Deno stdout/stderr/errors, and workspace file state. The system does not mine stored transcripts, benchmark trajectories, or long-running event logs. Raw protocol/tool traces are in-memory UI/debug surfaces, not durable memory.

**Extraction.** Extraction is model-mediated direct codification. The system prompt instructs the model to list capabilities, decide whether one matches, and if not, write a capability definition plus TypeScript implementation. Failed executions can return errors through the observe phase; the prompt tells the model to fix and retry. There is no separate judge, recurrence detector, human approval queue, or offline consolidation step.

**Storage substrate.** The distilled retained state lives in the selected workspace's `tools/index.json` and `tools/{name}.ts`; app/provider settings live in `~/.tendril/config.json`; runtime protocol events live only in process/UI state except for debug visibility while the app runs. This split matters: live conversation/tool traces are evidence and interaction state, while registered files are the persistent memory substrate.

**Representational form.** A capability bundles prose and symbolic parts. The metadata fields (`capability`, `triggers`, `suppression`) are prose selection policy consumed by the model. The `.ts` file is symbolic executable code consumed by Deno through the `execute` tool. The operative behavior-changing part is mixed: prose governs activation, code governs action.

**Lineage.** Lineage is weak. A registered capability records `created`, `created_by`, and `version`, but not the originating prompt, tool result, error history, user approval, source URLs, tests, or previous versions. Upsert overwrites the active entry and source file. The generated capability is the canonical source, not a derived view that can be regenerated from an attached trace.

**Behavioral authority.** Registered capabilities are system-definition artifacts when the agent lists them, chooses one, and executes by name. The same metadata/source files are knowledge artifacts when a human views them in the capability browser or file explorer. Raw tool traces and ACP events are knowledge artifacts for observation/debugging only; they do not instruct future behavior unless distilled into a registered capability.

**Scope and timing.** Scope is per workspace and online during ordinary use. The system learns immediately from live task pressure, not from repeated benchmark trajectories. This places Tendril on the survey axis as trace-to-tool learning: weaker evidence than critic-gated trajectory systems such as Voyager, but a clearer desktop pattern for turning ad hoc work into persistent executable affordances.

On the [survey's axes](../trace-derived-learning-techniques-in-related-systems.md), Tendril strengthens the "readable artifact learning" and "executable code as promotion target" claims, but with a different trigger boundary: live task need, not successful rollout. It also sharpens the governance gap around executable trace-derived artifacts whose promotion oracle is "the model needed it now and the command ran."

## Curiosity Pass

**The docs still overstate or drift from the implementation.** The README says "searchCapabilities" in examples and shows a root `index.json` in one workspace sketch, while current code uses `listCapabilities` and `{workspace}/tools/index.json`. The project brief describes a Rust crate architecture that does not match the inspected TypeScript sidecar. The reliable evidence is the current source.

**The registry size limit is configuration, not enforcement.** `WorkspaceConfigSchema` has `registry.maxCapabilities`, but `CapabilityRegistry.register` does not check it. At tens of capabilities, listing everything is simple and transparent. At hundreds, token cost, selection accuracy, and duplicate tools become the scaling limit.

**"Every action starts with list" is prompt-enforced.** The runtime exposes tool descriptions and a system prompt that insist on the cycle, but it does not programmatically reject an `execute` call that skipped `listCapabilities`. The discipline depends on model compliance.

**Sandboxing is meaningful but not policy review.** Deno permission flags, name-gated execution, timeouts, and workspace validation reduce blast radius. They do not tell whether a generated tool is correct, non-duplicative, privacy-preserving, dependency-stable, or safe to keep.

**One browser command is less workspace-scoped than the others.** The file-browser commands validate paths against the configured workspace, and `read_capabilities` validates the passed registry root. `read_tool_source` validates the tool name but trusts the `workspace` argument supplied by the frontend before reading `tools/{name}.ts`. In the normal UI path that argument comes from app config, but the command itself is weaker than the surrounding workspace guard.

**The UI is governance-adjacent, not governance.** Human inspection is possible through the capability browser and file explorer, but there is no review state, diff workflow, test harness, approval bit, or quarantine path. The system makes artifacts visible; it does not make them accountable.

## What to Watch

- Whether Tendril adds a real search layer or keeps full-registry listing as the scaling bet.
- Whether capability registration gains provenance fields, source prompt links, test commands, approval state, or failure counters.
- Whether the Deno sandbox adds stricter default network policy instead of treating an empty allowlist as unrestricted access.
- Whether generated capabilities learn to call other capabilities, and whether the system then needs dependency tracking.
- Whether the capability browser becomes an edit/review workflow rather than a read-only inspection surface.
- Whether multi-provider support changes behavior enough that capability quality depends strongly on provider/model choice.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Tendril is the online live-request-to-executable-capability case, distinct from stored transcript mining or critic-gated trajectory learning
- [RLM, Tendril, and llm-do place symbolic work at different persistence points](../../notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md) - compares: Tendril externalizes symbolic work into persistent workspace tools rather than keeping it inside one reasoning call
- [Codification](../../notes/definitions/codification.md) - clarifies: Tendril's durable memory changes medium from prompt text to executable TypeScript
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) and [system-definition artifact](../../notes/definitions/system-definition-artifact.md) - vocabulary: the same capability file advises when browsed and instructs/enables action when selected by the agent
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - vocabulary: Tendril's authority path runs through system prompt, Strands tool schema, registry listing, and Deno execution
- [Storage substrate](../../notes/definitions/storage-substrate.md), [representational form](../../notes/definitions/representational-form.md), and [lineage](../../notes/definitions/lineage.md) - vocabulary: Tendril separates workspace files, mixed prose/code form, and weak derivation metadata
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - rationale: Tendril shows a readable symbolic artifact path with a very weak promotion oracle
- [Promote only when value exceeds cost](../../notes/agent-memory-requirements/promote-only-when-value-exceeds-cost.md) - contrasts: Tendril promotes immediately on task need rather than after evidence accumulation
