---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "MGI-Mind workflow: the shipped OpenAI Agents remember-then-question example, its response handoff and failure boundary."
run-id: AAS-2026-11-08-mgi-mind-e0f02081480f-01
reviewed-boundary: a8defc36f7d0bcd5108714763a12625a0eda0868
---

# MGI-Mind workflow report

## Workflow account

The representative workflow is the shipped OpenAI Agents example: ask an assistant to remember a production database address, then ask its port. It was selected because one driver explicitly connects requests, memory tools and final answer delivery, rather than requiring a hypothetical composition of unrelated APIs. This is implementation evidence, not a successful run. MGI-Mind owns memory effects; the external SDK and model own tool selection, assistant continuation and answer generation ([RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory)). SRC-1, `docs/integrations/openai_agents.py`.

> if __name__ == "__main__":
>     print(
>         Runner.run_sync(
>             agent, "Remember that our prod database is Postgres 16 on db-prod:5432."
>         ).final_output
>     )
>     print(Runner.run_sync(agent, "What port is the prod database on?").final_output)
> --- `docs/integrations/openai_agents.py`

**Request and delegation.** The driver creates one agent with natural-language instructions to remember durable facts and recall before dependent answers. It registers only `recall(query)` and `remember(fact)`, backed by `Memory(library="agent")`. The user supplies the database statement; the host model chooses whether and how to turn it into a tool argument. This delegates storage/search operations, not a separate reasoning task to a child agent. The instruction is advisory rather than a forced write/read sequence ([RT-CLM-recall-habit](runtime.md#rt-clm-recall-habit), [RT-BAP-host-recall](runtime.md#rt-bap-host-recall)). The two Runner calls supply only their respective request strings in this driver; actual SDK context construction is outside the inspected implementation. No driver-level transfer of the first run's conversation to the second is shown. SRC-1, `docs/integrations/openai_agents.py`.

**Write handoff and checks.** If the model calls `remember`, the wrapper passes its string to `Memory.add`; the client posts content and the configured library to `/memory/add`. The server's ordinary add branch reaches storage, which checks library registration and secrets, chunks and embeds the content, then writes Qdrant points. These checks may reject a write but do not verify that the production database statement is true. Direct add does not inherit ingest's relevance/novelty quarantine gate. There is no per-fact human approval in this example; the user provides the initial request, the model proposes the tool content and server code decides physical admission ([RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory), [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)). The returned confirmation is not a read-after-write test or proof of future retrieval.

**Recall and consumer-visible material.** The second request asks for a port, but the host must elect to call `recall`. That wrapper invokes `mem.search(query, tier=2)`, not the client's unified recall method. Query/library selection, hybrid retrieval, optional reranking, result limit and tier-2 display truncation determine what crosses back. Thus the assistant does not receive the entire stored database, all source text or all silos ([RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory)). The response-delivery subroute further strips search hits to content with optional author labels; structured identifiers and scores are not present in the wrapper's returned string ([WF-RTE-response-delivery](#wf-rte-response-delivery)). This makes the exact downstream handoff narrower than the raw JSON response.

**Verification, failure and recovery.** Transport/authentication/response checks can reject the memory operation; they are not an answer oracle. The failure path in [WF-RTE-response-delivery](#wf-rte-response-delivery) raises client errors rather than silently converting them into usable memory. The wrappers and driver contain no local retry, fallback answer, restart or repair handler. Whether the SDK exposes a tool exception to the model, retries it or terminates a run is uninspected host behavior. Configuration repair or service startup belongs to the operator, as suggested by the client's error text; it is not an implemented autonomous recovery loop. Storage checks and retrieval failure behavior are bounded by the supplied runtime record. A successful response with no hits can produce an empty string, not evidence that the original claim was false.

**Delivery and its limits.** Delivery in the driver means printing each returned `final_output`. The second print follows completion of the first Runner call; this sequencing does not prove that the first call stored anything or that the second recalled it. There is no driver assertion that the answer is `5432`, no comparison with the initial statement, and no product-acceptance gate after generation. The initial statement supplies a potentially checkable answer, but the driver does not use it as an oracle. Tool-result supply is wired; use of that material, answer correctness and benefit are unobserved ([RT-BAP-host-recall](runtime.md#rt-bap-host-recall)).

All findings use SRC-1 at the frozen boundary. Added implementation inspection covers the complete `docs/integrations/openai_agents.py` driver and the synchronous transport, response parsing/rendering and add/search bodies in `clients/python/mgimind/_client.py`. These paths are already within the registered source; no new source or execution evidence is introduced. Server internals rely on the supplied runtime records. No target execution was performed. The account establishes a source-supported conditional workflow, not reliable operation across the external SDK, configured service and model.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-response-delivery
Label: Client response delivery

Part of: [RT-RTE-assistant-memory](runtime.md#rt-rte-assistant-memory)

This is the response-processing part of the supplied assistant-memory route, not an alternative memory service or duplicate end-to-end route. Endpoints are the synchronous HTTP response, `MemoryResult`, the wrapper's string tool result and the driver's printed host answer. Python client code owns validation/rendering; the external Runner owns model continuation. The input JSON is symbolic response state. Rendered content is natural-language context for the model; Python does not enforce its semantic use. SRC-1, `clients/python/mgimind/_client.py`, `docs/integrations/openai_agents.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `_parse` returns a `MemoryResult` on an accepted envelope; `str` returns its text, which the wrapper delivers as the tool return. The driver prints Runner's final output, not the raw search response.
- Later read-back: inapplicable — response rendering does not persist or reload material; durable memory writes and subsequent search belong to the parent route.
- Delegated visibility: The model-facing string contains rendered hit content and optional author, omitting the hit's identifier, score and other structured metadata. No isolated child-agent context is created here.
- Selection predicate: Authentication errors are rejected first; JSON must parse and `ok` must be truthy. A `results` response is rendered as search hits; this is the relevant search branch for the selected workflow.
- Invalidation or expiry: inapplicable — transient response text has no independent expiry or replacement mechanism in this client path; host context retention is external.
- Activation or effect: Successful parsing supplies text to the calling wrapper; actual model reliance and printed answer correctness remain unobserved. HTTP transport exceptions become `MgiMindError`; response errors raise rather than returning hit text.
- Evidence limits: Source-only wiring. The wrappers contain no recovery handler; SDK exception handling and successful subsequent continuation are uninspected. Envelope checks verify neither stored truth nor generated answers.

> except httpx.HTTPError as e:
>             raise _unreachable(self.url, e) from e
>         return _parse(resp)
> --- `clients/python/mgimind/_client.py:301-303`

> if resp.status_code in (401, 403):
>         raise MgiMindError(
>             f"{resp.status_code} auth failed: set MGIMIND_TOKEN to the server's "
>             "bearer token (printed when you run `mgimind serve-http`)."
>         )
> --- `clients/python/mgimind/_client.py`

> if not data.get("ok"):
>         # {"ok": false, "error": "..."} (with a 4xx/5xx status).
>         raise MgiMindError(str(data.get("error", "unknown server error")))
> --- `clients/python/mgimind/_client.py`

> for h in hits:
>         who = f" ({h['author']})" if h.get("author") else ""
>         lines.append(f"- {h.get('content', '')}{who}")
>     return "\n".join(lines)
> --- `clients/python/mgimind/_client.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

none
