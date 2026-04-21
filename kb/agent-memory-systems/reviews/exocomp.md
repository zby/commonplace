---
description: Go coding-agent harness with role-scoped tools, sandboxed execution, and file-backed bug/changelog coordination; execution controls are real, but planning and sub-agent workflows are still stubbed
type: kb/agent-memory-systems/types/agent-memory-system-review.md
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-04-05"
---

# Exocomp

Exocomp is a Go CLI harness for local coding agents, built by Cookie Engineer around Ollama-style tool calling. The repo's center of gravity is a small execution substrate: role-typed agent prompts, per-role tool allowlists, sandboxed file/program access, and shared markdown files for bug and changelog state. The interesting part is that the coordination surface stays inspectable. The caution is that much of the README's fuller multi-agent workflow remains aspirational: the requirements tool is stubbed, the documented `NOTES.md` and `TODO.md` coordination layer does not match the code, and the hired-subagent boot path is not yet wired end to end.

**Repository:** https://github.com/cookiengineer/exocomp

## Core Ideas

**Role types are compiled as prompt-plus-capability bundles.** [`agents/Agent.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/agents/Agent.go) hardcodes each role's prompt, tool allowlist, program allowlist, and default temperature. That is stronger than prompt-only roleplay because the session only exposes tool schemas matching the role's allowlist through [`tools/EncodeSchema.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/tools/EncodeSchema.go). The repo is really making a capability-surface argument: "architect", "coder", "tester", and "manager" differ because different code paths are reachable, not just because different prose was injected.

**The tool loop and sandbox boundary are the most complete mechanisms in the repo.** [`ollama/Session.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/ollama/Session.go) and [`ollama/ReceiveChatResponse.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/ollama/ReceiveChatResponse.go) implement a real synchronous tool-calling loop: send chat request with schemas, execute returned tool calls, append `tool` messages, and recurse until the model returns plain text. [`tools/resolveSandboxPath.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/tools/resolveSandboxPath.go) and [`tools/sanitizeSandboxPath.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/tools/sanitizeSandboxPath.go) enforce sandbox confinement for file access and path-bearing program arguments. This is the clearest part of the repo where the implementation cleanly delivers the claimed property.

**Coordination state is file-backed and inspectable, but thinner than the README implies.** The actual shared-state mechanisms live in [`tools/Bugs.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/tools/Bugs.go), [`tools/readBugs.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/tools/readBugs.go), [`tools/writeBugs.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/tools/writeBugs.go), [`tools/Changelog.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/tools/Changelog.go), and their read/write helpers. Those tools operate on `BUGS.md` and `CHANGELOG.md`, not the README's `NOTES.md` and `TODO.md` claim. The requirement/specification path is even thinner: [`tools/Requirements.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/tools/Requirements.go) is a stub and [`tools/Requirements.json`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/tools/Requirements.json) is empty. Even the bug lifecycle is only partially wired, because `bugs.Add` persists to disk while `bugs.Fix` only mutates in-memory state and never calls `writeBugs`.

**The project lifecycle is doctrine, not runtime control.** [`agents/Agent.Manager.txt`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/agents/Agent.Manager.txt) defines planning, implementation, testing, deployment, and maintenance phases, but there is no state machine, no phase data structure, and no transition logic that enforces this sequence. [`TODO.md`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/TODO.md) explicitly lists a future planner agent and state machine, which confirms that the author also sees this as missing infrastructure rather than completed machinery.

**The advertised multi-agent topology currently outruns the implementation.** [`tools/Agents.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/tools/Agents.go) does spawn a new process for `agents.Hire`, but it passes split flags like `--name`, `--agent`, and `--prompt` while [`cmds/exocomp/main.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/cmds/exocomp/main.go) only parses `--flag=value` forms. The hired child is launched in `jsonl` mode, but that branch is still marked TODO in the same file. So the repo has a real sub-agent API surface and process isolation story, but not yet a working child-agent runtime path that matches the README's framing.

## Comparison with Our System

| Dimension | Exocomp | Commonplace |
|---|---|---|
| Primary goal | Execute local coding work through role-typed agents and tool calls | Build, curate, and validate a durable knowledge base for agents |
| Durable artifacts | `BUGS.md`, `CHANGELOG.md`, prompts, tool code, sandbox files | Notes, ADRs, instructions, indexes, workshop artifacts |
| Coordination model | Shared operational files plus process spawning | Shared repository artifacts plus routing, links, and review/validation workflows |
| Strongest enforcement | Sandbox path checks, executable allowlists, per-role tool exposure | Structural note types, deterministic validation, review bundles, explicit link semantics |
| Knowledge structure | Flat operational state with little retrieval or synthesis structure | Typed, linked, retrieval-oriented knowledge artifacts |
| Learning/promotion model | No real promotion loop yet; requirements/planner path is stubbed | Explicit workshop-to-library extraction, distillation, codification, and review |
| Maturity signal | Early experimental repo with one shallow test and multiple TODO surfaces | Production methodology repo with established validation and review paths |

Exocomp is strongest where commonplace is relatively thin: local execution controls around agent tool use. It gives the model a bounded sandbox, a concrete tool surface, and a small inspectable coordination substrate. Commonplace is stronger where Exocomp is thin: durable knowledge structure, quality gating, retrieval, and honest distinction between workshop artifacts and library artifacts.

The deeper contrast is that Exocomp is mostly an **execution substrate** with a thin coordination layer, while commonplace is mostly a **knowledge substrate** with thinner execution controls. They overlap on the inspectable-files bet, but they cash it out at different layers.

## Borrowable Ideas

**Compile role-specific capability surfaces into code.** Exocomp's best architectural instinct is that role separation should change the reachable tool surface, not just the prompt text. If commonplace ever grows multiple agent roles with distinct responsibilities, hardcoded capability bundles are ready to borrow as a design principle.

**Keep early coordination state in ordinary files before building services.** `BUGS.md` and `CHANGELOG.md` are crude, but the underlying instinct is right: make the shared state readable, diffable, and manually repairable first. This is borrowable for workshop-scale multi-agent experiments, but only with a concrete coordination use case and stronger update guarantees.

**Pair shell access with both sandbox confinement and executable allowlists.** The combination of path sanitization and per-role `Programs` allowlists is a solid execution-substrate pattern. This is ready to borrow now anywhere we expose shell-like power to an agent.

## Curiosity Pass

**Role bundles genuinely constrain capability, but not nearly as much as the role names suggest.** The property claimed is separation of concerns. Mechanistically, the repo does achieve real tool-level separation through [`agents/Agent.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/agents/Agent.go) and [`ollama/Session.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/ollama/Session.go). But it does not transform high-level role promises into lower-level file or behavior constraints. The tester is told not to edit non-test code, yet [`tools/Files.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/tools/Files.go) has no path policy that would stop it. So the mechanism constrains *which verbs exist*, not *which artifact classes each role may mutate*.

**The tool loop is real, but the customization story is thinner than the CLI suggests.** The property claimed is a configurable agent runtime. The tool-calling cycle itself is real. But [`cmds/exocomp/main.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/cmds/exocomp/main.go) parses model and temperature flags into config, while [`agents/NewAgent`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/agents/Agent.go) still hardcodes per-role model names and temperatures. The simpler description is not "configurable local agent runtime" but "hardcoded role presets with a configurable backend URL and sandbox."

**The markdown coordination layer mostly relocates state into readable files rather than creating strong coordination guarantees.** The benefit is inspectability, and that benefit is genuine. But the simpler alternative is exactly what the repo is doing: read a shared file, mutate local memory, and write it back. There is no locking, no append-only event log, no merge strategy, and no atomic claim protocol. The `bugs.Fix` persistence hole in [`tools/Bugs.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/tools/Bugs.go) is especially revealing: the idea is stronger than the implementation, and there is almost no test coverage to catch that gap.

**The phased lifecycle cannot produce what its prompt claims without more substrate.** The property claimed is structured multi-phase project delivery. But with [`tools/Requirements.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/tools/Requirements.go) stubbed and the planner state machine missing from [`TODO.md`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/TODO.md), the manager prompt in [`agents/Agent.Manager.txt`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/agents/Agent.Manager.txt) is mainly doctrine. Even if the model followed it perfectly, there is no durable representation of project phase or confirmed requirements beyond whatever the model happens to remember in-context.

**The "multi-agent" claim currently means process spawning more than functioning worker collaboration.** The property claimed is autonomous delegation. The repo does spawn separate OS processes, so the isolation part is real. But because [`tools/Agents.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/tools/Agents.go) and [`cmds/exocomp/main.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/cmds/exocomp/main.go) do not agree on flag format, and because `jsonl` mode is not implemented, the child-workflow path currently tops out below the README promise. The simplest alternative would be sequential role invocations in one process; Exocomp has not yet clearly surpassed that baseline.

## What to Watch

- Whether the hired-agent path becomes genuinely functional: `agents.Hire`, child flag parsing, and `jsonl` mode all need to line up before the multi-agent story is more than a shell.
- Whether the requirements/planner path lands, because that is the missing bridge between "role prompts" and an actual phased workflow.
- Whether the file-backed coordination layer gains stronger guarantees such as persistence correctness, append-safe updates, or typed event records.
- Whether the test surface grows beyond [`tools/Programs_test.go`](https://github.com/cookiengineer/exocomp/blob/6e2f8954788e125e349b4636a32fb30ad42e474d/tools/Programs_test.go); right now the repo has almost no verification around its coordination mechanisms.

---

Relevant Notes:

- [Tracecraft](./tracecraft.md) — contrasts: both systems keep coordination state in inspectable file-like artifacts, but Tracecraft makes the primitives explicit while Exocomp relies on ad hoc shared-file mutation
- [LACP](./lacp.md) — contrasts: both are local agent execution stacks, but LACP has much richer governance and session-level control while Exocomp is intentionally thinner
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../notes/agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md) — exemplifies: Exocomp has coordination channels (`BUGS.md`, `CHANGELOG.md`, process spawning) with weak guarantees around consistency and completion
- [Agent runtimes decompose into scheduler, context engine, and execution substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) — grounds: Exocomp is a clear execution-substrate-heavy system with a comparatively thin context and scheduler layer
- [Inspectable artifact, not supervision, defeats the blackbox problem](../../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — foundation: Exocomp's best design choice is keeping the coordination surface in ordinary readable files even when the higher-level workflow is incomplete
