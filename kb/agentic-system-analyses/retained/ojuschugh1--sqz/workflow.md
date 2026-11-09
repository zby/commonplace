---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "sqz workflow report tracing upstream MCP tool execution, compressed delivery and explicit recovery through the stdio proxy."
run-id: AAS-2026-11-09-sqz-154fb86209ba-01
reviewed-boundary: "495c078d8f4c94d060ecfbb4d919286670b87898"
---

# sqz workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is an external coding agent's MCP tool request through `sqz-mcp proxy`, followed by compressed result delivery and, when requested, local recovery. This is selected because it connects shipped invocation, tool discovery, upstream work, admission checks, retained content and a recovery consumer in one implementation. It is not a sqz-owned autonomous agent workflow. The external host/model decides the task, tool arguments, whether to request more documentation or expansion, and whether the answer is sufficient. sqz owns subprocess mediation and representation changes, not the final task answer ([RT-RTE-mcp-proxy](runtime.md#rt-rte-mcp-proxy), [RT-BAP-host-guidance](runtime.md#rt-bap-host-guidance)).

The account establishes a wired protocol, not a successful execution. SRC-1 implementation inspection here covers `sqz-mcp/src/proxy.rs` through proxy shutdown and `sqz_engine/src/engine.rs` at `compress_tool_result`; HEAD matched the frozen commit. These are additional detailed inspections within the registered source, not new sources. No target, tests, examples or providers were executed. There is no supplied observed run establishing that a model requested recovery, received the intended complete task evidence, or delivered a correct final answer. Other runtime routes remain distinct; browser proposals and HTTP history transforms are not steps in this workflow.

### 1. Start the mediator and establish the tool contract

The caller supplies an upstream command and proxy flags. `run_proxy` constructs a native engine, spawns that command with piped stdin/stdout and inherited stderr, and runs client-to-upstream and upstream-to-client relay loops. An empty command or spawn failure returns an error; the code does not choose a replacement server. This delegates tool execution to an OS subprocess, not to a fresh model context or a sandbox. Upstream effects retain the process's available authority (SRC-1, `sqz-mcp/src/proxy.rs`; [RT-RTE-mcp-proxy](runtime.md#rt-rte-mcp-proxy)).

Initialization appends protocol guidance to the upstream instructions. Tool listing can shorten descriptions while leaving schemas intact. With lazy tools enabled, descriptions that actually become shorter are stored by name in process memory and can be requested through `sqz_tool_help`. The initial context therefore contains abbreviated documentation plus a reload route, rather than an isolated worker's return value. Full documentation crosses back only on an explicit help call. That route returns the stored string, not regenerated documentation. Missing storage produces an error explaining that the description may never have been shortened, the name may be unknown, or tool listing may not yet have occurred (SRC-1, `sqz-mcp/src/proxy.rs`).

> if brief.len() < desc.len() && !name.is_empty() {
>                         self.tool_docs.insert(name, desc.to_string());
>                         tool["description"] = serde_json::Value::String(brief);
>                     }
> --- `sqz-mcp/src/proxy.rs`

The expansion tool is advertised unless caching is disabled; help is advertised in lazy mode. Dispatch nevertheless recognizes both local tool names independently of advertisement. Guidance requests that the external agent interpret references and ask for missing information; supplying it does not prove compliance ([RT-RTE-mcp-proxy](runtime.md#rt-rte-mcp-proxy), [RT-BAP-host-guidance](runtime.md#rt-bap-host-guidance)).

### 2. Hand off the tool request and associate its response

The client sends JSON-RPC tool name, arguments and request ID. Ordinary calls are forwarded rather than reconstructed with a new prompt. The proxy records the expected response kind and tool name under the serialized ID. This bookkeeping lets an upstream reply select the appropriate rewrite branch. It is coordination state for current requests, not retained experience or model planning. Notifications, unparseable lines and replies without a matching pending ID pass through without this transformation (SRC-1, `sqz-mcp/src/proxy.rs`).

> self.pending.insert(Self::id_key(&id), kind);
> --- `sqz-mcp/src/proxy.rs`

The upstream server performs the requested tool work. sqz does not verify the upstream answer against the user's task. A top-level JSON-RPC error bypasses rewriting. A tool result marked `isError` is not compressed, and non-text content items are left alone. Thus failure information can return to the host without a compression attempt, but deciding whether to retry or change the task belongs to the caller (SRC-1, `sqz-mcp/src/proxy.rs`; [RT-RTE-mcp-proxy](runtime.md#rt-rte-mcp-proxy)).

### 3. Admit or reject a representation change

For each eligible text item, `compress_tool_result` makes a code-controlled decision: reject small inputs, reject Safe-routed content, choose cached or uncached compression, then require sufficient estimated savings after reference/hint overhead. With caching enabled and the risk guard permitting storage, the cache can return fresh text, a reference or a delta. A fresh compressed body gains an explicit expansion hint. Persistence can precede the final savings test, so declining to replace the response does not itself prove that no cache write happened (SRC-1, `sqz_engine/src/engine.rs`; [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery)).

> let use_cache = use_cache && !self.never_store(text);
> --- `sqz_engine/src/engine.rs`

> if tokens_original.saturating_sub(tokens_compressed) < TOOL_RESULT_MIN_SAVING {
>             return None;
>         }
> --- `sqz_engine/src/engine.rs`

A `None` outcome keeps that item's original text. A selected candidate replaces only the text field. Native engine verification and its safer recompression policy apply where the underlying engine is invoked; cache hits are not newly verified against the user's intended answer. Neither the savings predicate nor preservation checks constitute an expected-answer oracle. They admit a representation, not a successful task result. The code is the proposer and admission decision-maker; there is no per-candidate human approval in this path ([RT-RTE-engine-compress](runtime.md#rt-rte-engine-compress), [RT-RTE-mcp-proxy](runtime.md#rt-rte-mcp-proxy)).

### 4. Deliver the response, or fail open during rewriting

The proxy serializes the rewritten JSON-RPC response and writes it to client stdout with a flush. This is the sqz delivery boundary: bytes emitted to the host, not proof of ingestion into a model window or completion of the user's task. Multiple content items can retain their order while eligible text items change independently (SRC-1, `sqz-mcp/src/proxy.rs`).

A caught panic in response rewriting clears engine poison and returns the original upstream line, discarding the partially rewritten JSON value. This is a failure-open delivery policy, not rollback of every cache/statistics side effect that may already have occurred. Serialization also has an original-line fallback. On stream/write failure, the relay can break; there is no task-level retry or durable delivery acknowledgment in the inspected relay loops. On client EOF the process allows a grace interval, then kills/waits for the upstream child. This is process cleanup, not recovery of unfinished user work (SRC-1, `sqz-mcp/src/proxy.rs`).

> if rewritten.is_err() {
>             self.engine.clear_poison();
>             return line.to_string();
>         }
> --- `sqz-mcp/src/proxy.rs`

### 5. Recover retained material when the caller needs it

A later `sqz_expand` request carries a ref token or prefix. The proxy answers locally and does not delegate the request to upstream. Cache lookup may return retained original bytes or a compressed-only legacy result. The proxy converts original bytes with UTF-8 replacement before returning text. This is therefore not an unconditional arbitrary-byte transport guarantee, even when the store retains original bytes. A missing entry produces `isError: true`; an expansion error likewise returns an error result. There is no automatic re-execution of the upstream tool to replace missing content (SRC-1, `sqz-mcp/src/proxy.rs`; [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery)).

> sqz_engine::ExpandResult::Original { bytes, .. } => {
>                         String::from_utf8_lossy(&bytes).into_owned()
>                     }
> --- `sqz-mcp/src/proxy.rs`

> "content": [{ "type": "text", "text": format!("no cached content found for prefix '{prefix}'") }],
>                 "isError": true
> --- `sqz-mcp/src/proxy.rs`

A panic while answering a local help/expand call becomes JSON-RPC internal error `-32603` after poison clearing. The host still owns the next decision: correct the request, reread upstream material, or stop. Expansion restores content, not earlier model reasoning or tool effects. Meaningful references also depend on the external consumer and surviving cache; timestamp-based freshness is not proof that the host still holds the earlier body ([RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery)).

The workflow can thus deliver compressed text and later supply retained evidence without owning final verification or task completion. The inspected checks support bounded recovery and best-effort representation selection, not demonstrated end-to-end model reliability or token-saving benefit.

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

#### On [RT-RTE-mcp-proxy](runtime.md#rt-rte-mcp-proxy)

Workflow role: mediates one external agent's request through upstream execution and response delivery. The caller supplies task/tool arguments; request IDs coordinate the return. Tool-list rewriting changes discoverable documentation, not upstream tool semantics. Response admission is code-controlled, with original-line recovery on caught rewrite panic. Delivery means stdout write/flush to the host, not final answer acceptance. Local help and expansion are explicit caller-selected continuation steps, not autonomous agent delegation.

#### On [RT-RTE-engine-compress](runtime.md#rt-rte-engine-compress)

Workflow verification scope: underlying engine candidates can receive preservation checks and safer recompression. The enclosing proxy's size/risk/savings gates can instead decline replacement. Neither layer verifies that the upstream tool fulfilled the user's objective; no expected task answer is supplied.

#### On [RT-RTE-cache-recovery](runtime.md#rt-rte-cache-recovery)

Workflow recovery ownership: sqz resolves retained content; the host/model must notice the need and issue the request. Proxy recovery delivers decoded text or a compressed-only result and reports lookup failure instead of automatically rerunning upstream. Returning that result does not establish model use, successful reconstruction or correction of a prior decision.
