---
description: MCP forces stateless tool operations through a persistent server process — most tools are pure functions that don't need session state, connections, or lifecycle management, but pay the complexity tax anyway
type: kb/types/note.md
traits: []
tags: []
---

# MCP bundles stateless tools with a stateful runtime

The Model Context Protocol packages two things together: a protocol for tool discovery and invocation, and a server runtime that maintains persistent state (connections, sessions, process lifecycle). Most tool operations are pure functions — take input, return output, done. But MCP forces them through a stateful server, so every tool pays the complexity cost of state management whether it needs state or not.

## The state tax

A stateful intermediate layer imposes costs that stateless operations don't require:

- **Lifecycle management** — the server process must start, stay alive, handle crashes, and clean up. A stateless function call has no lifecycle.
- **Test isolation** — writing well-isolated tests for stateful servers is hard. State leaks between tests, setup/teardown is complex, and you're testing the server machinery alongside the tool logic. Stateless functions are trivially testable.
- **Connection management** — maintaining client-server connections adds failure modes (timeouts, reconnection, serialization) to what could be a direct function call.
- **Concurrency** — shared state requires synchronization. Stateless tools are embarrassingly parallel.

The difficulty of writing isolated tests is a signal that the architecture is mixing concerns — the test wants to exercise the tool logic, but the stateful runtime forces it to also manage server state.

## Most tools don't need state

The typical MCP tool surface — read a file, search for content, run a command, fetch a URL — is stateless. The tool takes arguments, does work, returns a result. No session context needed between calls.

State genuinely earns its keep in some cases. The strongest is **authorisation** — holding OAuth tokens, managing refresh flows, authenticating with external services on behalf of a user. This is inherently stateful and hard to do per-call. Connection pooling for database-backed tools, caches, and streaming results are other legitimate cases. But many tools don't need any of these — and they still pay the server cost.

## The economic argument

The useful storage analogy is narrower. [Schema timing and database authority are separate commitments](./files-defer-centralized-schema-commitment-until-invariants-stabilize.md), and [choosing files or a database requires a concrete workload comparison](./many-to-many-edge-state-is-where-files-yield-to-a-database.md). At the tool layer, the corresponding question is whether a call needs persistent runtime capabilities. Most operations described above are independent calls, so the comparison is direct invocation versus server-mediated invocation, with stateful infrastructure justified by requirements the tool actually uses.

The economic alternative: stateless tool invocation as the default, where the tool is a function call with no server process. State only where the tool genuinely requires it. This is what Claude Code's native tools already are — Read, Write, Grep, Bash are direct function calls with no intermediate server, no session, no lifecycle.

The pattern generalises: when an architecture bundles a simple common case with a complex rare case under a single abstraction, the common case pays complexity rent for capabilities it doesn't use. The economic solution is to separate them — stateless by default, stateful opt-in.

---

Relevant Notes:

- [canonical files may defer a shared schema while database authority remains a separate commitment](./files-defer-centralized-schema-commitment-until-invariants-stabilize.md) — grounds: separates schema timing from database authority; this note imports only the requirement-driven comparison for tool-runtime state
- [ephemeral computation prevents accumulation](./ephemeral-computation-prevents-accumulation.md) — stateless tool invocation is ephemeral by design; MCP's persistent server pushes toward accumulating state whether or not the tools need it
- [context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — unnecessary intermediate layers add latency and failure modes without improving the agent's context
