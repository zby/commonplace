---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "sqlite-graph-memory workflow: host-requested MCP recall through child retrieval, delivery checks and bounded error return."
run-id: AAS-2026-11-08-sqlite-graph-memory-ca3785ec5c2e-01
reviewed-boundary: f05db2778159d50a0ad8a35be4f2be3a6aea94b1
---

# sqlite-graph-memory workflow report

## Workflow account

### Selection and limits

The representative workflow is an agent's associative `memory_recall` request, traced from the MCP request through retrieval to a returned context bundle. It is selected because it is the shipped agent-facing interface, and its process boundary exposes both successful delivery and rejection paths. This is a multi-step tool workflow inside an external agent's work, not a shipped multi-agent plan-to-answer workflow. The package does not supply the enclosing agent's request selection, reasoning, final-answer verification or delivery to a human. Consequently, the trace ends at the MCP tool result, not at a completed user task ([RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall), [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery)).

Evidence is static implementation and integration doctrine from SRC-1 at the [boundary](boundary.md). No target, example or test was run. Inspection for this member covered `src/sqlite_graph_memory/mcp_server.py`, the `main` orchestration in `src/sqlite_graph_memory/brain_ask.py`, and `examples/README.md`. These are same-pin implementation and doctrine coverage, not new sources or observed operation. The integration guide describes cross-encoder reranking as part of associative mode; executable orchestration instead loads it only when enabled. The workflow below follows implementation, consistent with [RT-CMP-rerank-model](runtime.md#rt-cmp-rerank-model).

### Request and consequential handoffs

1. **Prepare retained inputs.** The integration guide asks the operator to install an embedding extra, index a Markdown directory and configure the MCP server with index and database paths. This supplies the retained corpus and runtime environment; it is not per-query human approval. Index admission and its nontransactional refresh limits are already established in [RT-RTE-index-admission](runtime.md#rt-rte-index-admission). A recall request does not itself rebuild the index (SRC-1, `examples/README.md`, `src/sqlite_graph_memory/brain_ask.py`).

2. **Host to server.** The external host submits `tools/call`, naming `memory_recall` and supplying query and optional mode. `handle_request` rejects a falsey query and otherwise calls `run_recall`. The advertised schema specifies a string query, but the handler's truthiness check is not full type validation. The server owns progression after this handoff; it does not delegate a goal to another reasoning agent. Unknown recall modes fall back to associative mode rather than being rejected (SRC-1, `src/sqlite_graph_memory/mcp_server.py`; [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall)).

3. **Server to child.** Associative mode becomes `--graph --ask` plus the query in a Python subprocess argument list. The server creates a unique temporary answer file, overrides `BRAIN_ANSWER_OUT`, adds the package source directory to `PYTHONPATH`, and inherits the remaining environment and working directory. The child therefore receives the query and configured filesystem/model access, not the enclosing conversation or a delegated agent instruction. The parent captures stdout/stderr and waits with a bounded timeout. This isolates a failing computation, not its OS permissions or a separate model reasoning context ([RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall), [RT-CLM-scoped-return](runtime.md#rt-clm-scoped-return); SRC-1, `src/sqlite_graph_memory/mcp_server.py`).

4. **Child selection and formatting.** The child checks that a query and embedding index exist, reloads the index, loads the encoder and computes query similarities. Code deduplicates candidates by note path, expands indexed outgoing-link neighbors, applies the entity-shaped-query exception, then orders candidates. For an entity-shaped graph query, selected additions are restricted to supersession targets; this is not a temporal-truth check. Dense ordering is the default; inherited settings can enable reranking or PageRank. These branches and their differing A/B composition are established by [RT-RTE-recall-options](runtime.md#rt-rte-recall-options). The `--ask` branch delivers only the first eight ranked snippets with title, date and score headers. It neither generates an answer nor tests statements against a reference answer. Truncation and selection control which retained material reaches the host; they do not summarize or evict the host's previous turns (SRC-1, `src/sqlite_graph_memory/brain_ask.py`).

5. **Child to server to host.** The child writes the formatted text to the scoped file. The parent first requires exit code zero, then reads and strips that file. A nonempty file becomes success text; the handler wraps it as MCP textual content with `isError: false`. Finally, the stdio loop serializes the response and flushes stdout. This is the package's delivery point. Agent adoption, citation fidelity and a later final answer remain outside the inspected consumer boundary ([RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery); SRC-1, `src/sqlite_graph_memory/mcp_server.py`, `src/sqlite_graph_memory/brain_ask.py`).

### What verification rejects, and who recovers

The server's checks verify process/output availability, not answer quality. A nonzero child exit returns stderr, or stdout when stderr is empty, as error content. A timeout returns an error naming its duration. A file-read failure returns an error; an empty file returns an explicit no-match error rather than promoting startup output to success. The temporary file is removed in `finally`, with deletion failures ignored. There is no retry in `run_recall`; once it returns an error, the host/operator must decide whether to fix configuration, rebuild inputs or issue another request. The server remains able to process subsequent requests after these handled errors, but malformed nested request shapes are not covered by this local recovery envelope (SRC-1, `src/sqlite_graph_memory/mcp_server.py`; [RT-CLM-scoped-return](runtime.md#rt-clm-scoped-return)).

The timeout setting itself has a rejection path before child execution:

> return "Recall configuration error: BRAIN_RECALL_TIMEOUT must be an integer from 1 to 600 seconds.", True
> --- `src/sqlite_graph_memory/mcp_server.py`

The successful file check is weaker than a semantic or even a match-count acceptance gate. In particular, the child creates query/scope header text before iterating over hits:

> if ask:
>     lines.append('=== CONTEXT BUNDLE (paste to your agent) ===\n')
>     for i, sc in reranked[:8]:
> --- `src/sqlite_graph_memory/brain_ask.py`

Thus an empty ranked list can still produce a nonempty formatted file and pass the parent's file-content check. The parent's empty-file error must not be interpreted as a complete detector of zero retrieved notes. No claim about the frequency of that condition follows from static inspection (SRC-1, `src/sqlite_graph_memory/brain_ask.py`, `src/sqlite_graph_memory/mcp_server.py`).

Local graph/PPR fallback is a different recovery mechanism: it preserves a prior candidate/order route rather than restarting the request. It does not cover missing indices or failed model loading ([RT-RTE-recall-options](runtime.md#rt-rte-recall-options)). The Stop-hook ledger and benchmark answer/abstention logic are separate shipped routes, not later stages of this recall workflow. Joining them would invent a capture-to-reflection-to-verified-answer loop that this trace does not establish ([RT-RTE-turnstate-capture](runtime.md#rt-rte-turnstate-capture), [RT-RTE-evaluation-paths](runtime.md#rt-rte-evaluation-paths)).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall)

Workflow role: the selected request-to-tool-result chain. Delegation is to a retrieval process, not an autonomous subagent. Host-to-server input contains query/mode; server-to-child input adds flags and inherited deployment state; child-to-parent success supplies a scoped text file. The host retains ownership of the enclosing task and decides whether to use the returned context. Delivery is serialized MCP output, not a verified user-facing answer.

#### On [RT-CLM-scoped-return](runtime.md#rt-clm-scoped-return)

Workflow acceptance boundary: child success plus nonempty scoped text establishes availability of the designated output, not relevant hits or correct claims. A header-only bundle can satisfy that check. Handled failure returns control to the host without an internal retry; file cleanup concludes the call. Timeout configuration rejection occurs before the child starts. These are process-level rejection/recovery steps, not a content critic or an answer oracle.
