---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Pond workflow account: recovering a prior decision through Pi search, transcript follow-up and caller-owned answering."
run-id: AAS-2026-10-14-pond-7a589a889ca1-01
reviewed-boundary: "0c440e130faf44052d0d896a585e572090079f1f"
---

# Pond workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is a host agent answering a user's question about a prior decision: search archived conversations, read the relevant session's latest turns, expand a message when necessary, then answer in the host. This is selected because Pond ships connected tool instructions and executable handoffs for those steps, rather than merely independent retrieval capabilities. It is the requested recall route already declared as [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall), not a new workflow executor. Pond delegates no reasoning worker in this path. The host model chooses subsequent calls and the answer; Pond executes archive operations.

The [boundary](boundary.md) fixes SRC-1 and the reviewed revision. This account adds implementation inspection of Pi argument conversion, response handling and MCP error relay, plus Rust session lookup, pagination rejection and MCP transcript delivery; it also reads the complete bundled skill as doctrine/design. Anchors: SRC-1, `packages/pi-pond/src/tools.ts`, `packages/pi-pond/src/mcp.ts`, `packages/pond/src/handlers.rs`, `packages/pond/src/transport.rs`, `packages/pond/SKILL.md`. Correction inspection also covers the search projection in SRC-1, `packages/pond/src/sessions.rs`, and SQL's column/body recovery hint in SRC-1, `packages/pond/src/sql.rs`, as implementation evidence. No program or test was executed and no host trace was supplied. These are wired tool steps and requested model behavior, not evidence of a completed answer or successful recovery. This is a selective requested-tool account, not an exhaustive inventory of interactive recall delivery channels; Pi's human-selected editor-reference insertion is not traced here.

### Request, search and follow-up

1. **Request and next-step owner.** A user asks what was decided earlier. Pi's registered prompt guidelines request a search on references to past work; the host model supplies distinctive query words and any project/session/date filters. These static guidelines are [RT-OBJ-prompt-guidelines](runtime.md#rt-obj-prompt-guidelines), delivered through [RT-BAP-recall-guidance](runtime.md#rt-bap-recall-guidance). Their load does not enforce invocation. The archive must already contain captured sessions; [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) supplies that prerequisite, not a mandatory capture step on every recall request. SRC-1, `packages/pi-pond/src/tools.ts`, `packages/pond/SKILL.md`.
2. **Computational handoff.** Pi trims the query, refuses an empty value, clamps the search limit, and forwards recognized filters over MCP. The server parses mode and ordering, executes the retrieval handler, and renders successful hits as a transcript. Its tool description tells the caller to pass a hit's session ID to a session read or message ID to a message read. Each call is a separately chosen operation; Pond does not automatically chain search into a read. The runtime record supplies the retrieval-arm and embedding limits. SRC-1, `packages/pi-pond/src/tools.ts`, `packages/pond/src/transport.rs`; [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall).
3. **Interpretation and latest-state check.** The host selects a hit and requests `pond_get_session` with `from="end"` for a latest-decision question. This is an instructed check against early conclusions being superseded, not an executable verdict on which historical claim is true. Session reads default to a bounded page, not an unrestricted whole transcript. A message ID can resolve to its parent session and anchor the page. Before/after IDs support further paging. The model must decide whether another page is needed. SRC-1, `packages/pond/SKILL.md`, `packages/pond/src/handlers.rs`, `packages/pond/src/transport.rs`.
4. **Evidence expansion.** A session transcript includes user/assistant text and compact tool/file references; full tool bodies remain behind `pond_get_message`. That follow-up supplies the selected message's parts and a requested neighbor window. Archived child sessions can be exposed as IDs in the first session page's footer and opened separately. This is historical navigation, not spawning live sub-agents; footer lookup is best effort, so missing footer content is not proof that no children exist. SRC-1, `packages/pond/src/transport.rs`; [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall).
5. **Return and delivery.** Pi converts successful MCP text into the host's tool result and clips oversized text at a UTF-8 boundary with an explicit narrowing hint. Archive IDs remain available for additional requests; the returned text is copied into context rather than a live archive reference. Delivery by Pond means the requested transcript/error reached this return surface. A final answer is delivered by the enclosing host, whose actual answer, interpretation and completeness check are unobserved. There is no task-answer oracle or Pond-owned answer acceptance gate. SRC-1, `packages/pi-pond/src/tools.ts`, `packages/pi-pond/src/mcp.ts`; [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall).

The shipped latest-state rule states the intended epistemic check:

> - Long sessions supersede their own early conclusions. For "what did we
>   decide / latest state", read the end (`pond_get_session(id, from="end")`)
>   or `pond_search` with `sort_by=recency` - relevance rank favors the early,
>   confident, possibly overturned phrasing.
> --- `packages/pond/SKILL.md`

This rule guides interpretation; it does not establish that every late statement is correct or that a model obeyed the instruction.

### Rejection, recovery and verification limits

**Disabled semantic search.** A requested vector search can be refused by the server when embeddings are disabled. The MCP branch deliberately returns that refusal as a tool error so the caller can retry with full-text search without treating the event as a broken RPC connection. Pi's MCP client maps `isError` to an error result, and the tool relay returns its text to the host. The next-step owner is the caller; no automatic query repair or retry occurs in this inspected branch. SRC-1, `packages/pond/src/transport.rs`, `packages/pi-pond/src/mcp.ts`, `packages/pi-pond/src/tools.ts`; [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall).

> // The `mode=vector` refusal is the caller's to fix in-turn (retry
> // with fts), so it rides back as a tool error, not a JSON-RPC
> // one: a JSON-RPC error makes plugin hosts tear down and respawn
> // the pond child on every call.
> --- `packages/pond/src/transport.rs`

The branch establishes deliberate error classification, not observed host retry or the SDK's behavior on every other error.

**Invalid follow-up.** The session handler refuses simultaneous forward/backward anchors and names the fix. A stale anchor returns a validation error requesting an ID from a prior page. A requested ID that matches neither session nor message returns not-found. These reject malformed navigation, not inaccurate conclusions. Caller correction is afforded by diagnostic text, but actual repair is unobserved. SRC-1, `packages/pond/src/handlers.rs`.

> "after_message_id and before_message_id are mutually exclusive",
> --- `packages/pond/src/handlers.rs`

**Weak evidence.** The bundled skill warns that search omits tool output, but its prescribed `contains_tokens(search_text, '...')` SQL predicate still checks the restricted conversational projection, not tool bodies. [MEM-OBJ-search-text](memory.md#mem-obj-search-text) and [EPI-RTE-search-projection](epistemic.md#epi-rte-search-projection) establish that distinction; correction inspection of SRC-1, `packages/pond/src/sessions.rs`, confirms it. Thus this specific instruction cannot recover evidence omitted because it was tool output. Its occurrence is doctrine, not support for its sufficiency. The broader SQL capability in [RT-RTE-corpus-sql](runtime.md#rt-rte-corpus-sql) does permit inspection of tool bodies through `parts.variant_data`; the skill separately directs callers to read the schema and identifies the tool-result `result` field. Such a body-targeted query is a caller-chosen conditional alternate, not an automatic recovery or compulsory step for every prior-decision question. The expected reference is historical corpus content, not an externally supplied correct answer. Neither the restricted predicate nor successful body-targeted SQL certifies archive completeness or historical truth. SRC-1, `packages/pond/SKILL.md`, `packages/pond/src/sql.rs`.

> - Search covers only user/assistant conversational text - tool output is
>   excluded by design. A weak search result is NOT proof of absence: verify
>   exact strings with `pond_sql` `contains_tokens(search_text, '...')` before
>   concluding something never happened.
> --- `packages/pond/SKILL.md`

The separate body-query guidance identifies the relevant retained part:

> - Tool bodies in SQL: tool_call is `{call_id, name, params}` (a Bash command
>   is `json_extract(variant_data, '$.params.command')`); tool_result is
>   `{call_id, name, is_failure, result}`.
> --- `packages/pond/SKILL.md`

The implementation's SQL recovery hint explicitly locates those bodies:

> parts(session_id, message_id, id, ordinal, type, provenance, tool_name, \
>              call_id, is_failure, variant_data, options). Part bodies live in \
>              parts.variant_data (JSONB) and nest by part type: tool_call is {call_id, \
>              name, params} - a Bash command is json_extract(variant_data, \
>              '$.params.command') - tool_result is {call_id, name, is_failure, result}, \
> --- `packages/pond/src/sql.rs`

This workflow reads retained evidence; it does not admit a revised instruction or write a verified final answer back into Pond. Any later archival capture of the host's answer follows the separate capture route. No successful downstream task outcome, learning benefit or model compliance is established by these shipped instructions and handlers.

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

#### On [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall)

Workflow role: the representative prior-decision workflow uses search → caller-selected latest-session page → optional paging/message expansion → host answer. The caller owns each consequential next step. Request arguments and returned IDs supply the handoffs, not a Pond-authored task plan. Acceptance of tool requests is deterministic argument/protocol/navigation checking; acceptance of evidence and delivery of the answer remain host responsibilities. The selected failure path is disabled-vector refusal followed by caller-owned full-text retry. Ordinary success responses are byte-bounded by the Pi projection. These workflow-specific findings are implementation wiring plus requested model conduct; successful invocation, recovery and answering remain unobserved.

#### On [RT-RTE-corpus-sql](runtime.md#rt-rte-corpus-sql)

Workflow role: conditional broader evidence inspection when conversational search is insufficient. SQL can reach tool bodies in `parts.variant_data`, but the skill's particular `contains_tokens(search_text, '...')` predicate cannot check them: it targets the same restricted projection described by [MEM-OBJ-search-text](memory.md#mem-obj-search-text) and [EPI-RTE-search-projection](epistemic.md#epi-rte-search-projection). Recovery of omitted tool evidence therefore requires a body-targeted query or the message expansion already traced, not that predicate alone. The bundled skill asks the caller to read the SQL schema resource first and avoid guessed columns/JSON paths, and separately documents tool-body fields. The host proposes the query and interprets the results; deterministic SQL admission can veto it. These are supported capabilities and requested caller conduct, not observed recovery. This does not add a task-answer oracle or certify that the retained corpus covers every past event. SRC-1, `packages/pond/SKILL.md`, `packages/pond/src/sql.rs`, `packages/pond/src/sessions.rs`.
