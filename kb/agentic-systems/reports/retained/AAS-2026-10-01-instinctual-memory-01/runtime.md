---
type: agentic-systems/types/agentic-system-runtime-report.md
description: "Runtime baseline of instinctual-memory's mem CLI and service paths at the pinned repository commit"
run-id: AAS-2026-10-01-instinctual-memory-01
reviewed-boundary: "6acb13dc35765bf5ccfc87e445dd09c480f1c28a"
---

# instinctual-memory runtime report

## Runtime account

The shipped `mem` program is a local CLI and service for a Git-first memory store. `src/main.rs` parses CLI arguments, resolves the store, dispatches the command, prints errors to stderr, and exits nonzero on failure. No scheduler or autonomous agent loop is implemented inside this repository; an enclosing host or operator invokes the CLI or service. The boundary excludes host scheduling and prompt assembly, so this analysis cannot establish that returned memory enters an agent's context or changes its decisions.

> if let Err(err) = cli.resolve_store().and_then(|()| run(&cli)) {
> --- `src/main.rs:18-18` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

An ordinary local search begins when a caller invokes the `search` command. The parsed CLI command dispatches to the search handler, which queries retained facts and journal events and may rerank results using configured JEV or a local model. The CLI returns formatted hits to its caller. The source establishes implementation paths, not actual invocation, selection quality, or downstream activation. `src/cli.rs` and `src/ops.rs` are the principal implementation anchors for this route.

The materially distinct service route starts with an external MCP client sending line-delimited JSON-RPC over stdio. The service parses each line, answers initialize/list/call requests, dispatches tool calls into `ops::execute`, then serializes the payload as text for the client. Available tools include search, status, read, history, task-list reads and updates, and validated remember/correct/forget changes. The MCP transport is an adapter over the same operations; it does not establish how a host presents or uses the response.

> "tools/call" => Some(result(id, call_tool(root, scope_id, session_id, &params))),
> --- `src/mcp.rs:62-62` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

Other material paths include direct CLI ingestion/consolidation/change/erase operations, hooks and writeback, and MCP-backed task and memory mutations. The HTTP service is an alternate transport. These paths can alter durable state and have distinct adapters and callers; the selected source set includes `src/cli.rs`, `src/ops.rs`, `src/mcp.rs`, and `src/hook.rs`. This member has not established a single enforcement point covering all callers, nor a deployed isolation envelope, approval policy, or host permission grant set. Such controls depend on the caller and deployment. No execution traces are supplied, so actual operation, recovery behavior in deployment, delegated visibility, activation, and benefit remain unobserved.

The repository wires model-backed extraction and optional reranking into selected memory operations. Provider calls and model internals are outside this source boundary, and this runtime account does not infer their behavior or claim a pinned deployed model. Memory-specific retained state and its admission/revision semantics are for the memory analyst to characterize.

## Shared records

### Components

none declared in this member. Model-backed extraction and reranking are present in the implementation, but this runtime member does not declare their exact deployed model identities or versions; provider and deployment configuration are not execution evidence.

### Operative objects

#### OBJ-1 — mem CLI and service
- Source-native identity: the `mem` executable/library and its CLI, MCP, HTTP, and hook entry paths.
- Representational form: executable program and request/response protocols.
- Storage substrate: local configured memory root; durable substrates are assessed by the memory analyst.
- Evidence: `src/main.rs`, `src/cli.rs`, `src/mcp.rs`, `src/ops.rs`, `src/hook.rs` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`.

### Routes

#### RTE-1 — Local CLI operation
- Endpoints: operator or host process → `mem` CLI → command handler and operations → local store → CLI output.
- Progression/owner: external caller selects and invokes the command; the executable parses, resolves the store, dispatches, and returns or reports an error. There is no internal scheduler.
- Context/state/action effects: command arguments and resolved root determine operation; search/read return memory, while ingestion, consolidation, change, erase, and related commands can mutate local state.
- Immediate return: command-specific output or error; exact presentation depends on the command.
- Later read-back: applicable to writes that persist in the store; exact persistence and selectors are memory-analyst scope. No execution evidence establishes a subsequent read.
- Delegated visibility: uninspected; depends on the invoking host and filesystem permissions.
- Selection predicate: command-specific arguments and operation logic; search/reranking details belong to the memory analyst.
- Invalidation/expiry: command-specific; uninspected here.
- Activation/effect: returned data is available to the caller, but downstream use is unobserved.
- Evidence limits: implementation only; no supplied traces or deployment configuration.
- Diagnosis/candidate/admission: inapplicable to ordinary invocation; explicit state-changing commands have separate admission mechanics to be analyzed on their routes.

#### RTE-2 — MCP stdio operation
- Endpoints: MCP client → line-delimited JSON-RPC server → `call_tool` → `ops::execute` → configured local store → JSON-RPC response.
- Progression/owner: external client chooses tool and arguments; the server validates known tool names, executes the operation and returns payload text with error/conflict/not-found indicators.
- Context/state/action effects: request arguments and server-provided root, scope, and session IDs are passed to operations; mutation tools can change task or memory state.
- Immediate return: JSON response containing tool payload and status.
- Later read-back: applicable for persistent mutations; exact semantics are memory-analyst scope.
- Delegated visibility: uninspected; host/client policy and deployment determine which agent can call tools.
- Selection predicate: caller-supplied tool name and arguments, then operation-specific logic.
- Invalidation/expiry: tool-specific; not established by transport code.
- Activation/effect: response delivery is wired; agent uptake and behavior change are unobserved.
- Evidence limits: `src/mcp.rs` shows the adapter and routing, not actual host registration, caller grants, or execution.
- Admission: explicit memory change requests have validation and publication behavior implemented in operations; detailed admission account belongs to the memory analyst.

#### RTE-3 — Hook and writeback integration
- Endpoints: external host lifecycle/integration invocation → hook or writeback handler → local memory operations/files → host-visible result or file changes.
- Progression/owner: external host controls invocation; repository code handles configured integration behavior.
- Context/state/action effects: event/input data can be ingested or memory written back; scope depends on integration arguments and configuration.
- Immediate return: hook/writeback-specific output; deployment evidence absent.
- Later read-back: applicable when the operation stores material; details belong to memory analysis.
- Delegated visibility: host-dependent and unobserved.
- Selection predicate: event, options, and configured project/store.
- Invalidation/expiry: uninspected at this runtime level.
- Activation/effect: integration output is wired; downstream host behavior is unobserved.
- Evidence limits: implementation anchors `src/hook.rs` and `src/cli.rs`; no host traces or installed configuration supplied.
- Admission: inapplicable to the hook invocation itself; any durable content changes are analyzed by the memory analyst.

### Claims

none declared in this member.

### Evidenced absences

none declared in this member. The boundary's lack of execution traces is an evidence limitation, not evidence that operation or activation is absent.

### Behavioral-authority paths

none declared in this member. Host and operator authority over invocation and tool exposure are outside the selected implementation evidence.

## Annotations

none
