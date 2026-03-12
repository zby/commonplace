---
description: MCP forces stateless tool operations through a persistent server process — most tools are pure functions that don't need session state, connections, or lifecycle management, but pay the complexity tax anyway
type: note
traits: []
areas: [kb-design]
status: seedling
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

This is the [files-not-database](./files-not-database.md) argument applied to the tool layer. A database earns its complexity when you need transactions, concurrent access, and indexes. Files earn their simplicity when you need read/write/version. Most MCP tools are file-shaped operations — stateless, independent, no shared state — forced through a database-shaped runtime.

The economic alternative: stateless tool invocation as the default, where the tool is a function call with no server process. State only where the tool genuinely requires it. This is what Claude Code's native tools already are — Read, Write, Grep, Bash are direct function calls with no intermediate server, no session, no lifecycle.

The pattern generalises: when an architecture bundles a simple common case with a complex rare case under a single abstraction, the common case pays complexity rent for capabilities it doesn't use. The economic solution is to separate them — stateless by default, stateful opt-in.

---

Relevant Notes:

- [files beat a database for agent-operated knowledge bases](./files-not-database.md) — same pattern at the storage layer: files are the stateless default, databases earn their complexity only for specific capabilities (temporal queries, graph analytics)
- [ephemeral computation prevents accumulation](./ephemeral-computation-prevents-accumulation.md) — stateless tool invocation is ephemeral by design; MCP's persistent server pushes toward accumulating state whether or not the tools need it
- [context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — unnecessary intermediate layers add latency and failure modes without improving the agent's context
- [indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — same principle: indirection through a server process costs overhead on every call, unlike code where indirection is nearly free

Topics:

- [kb-design](./kb-design.md)
