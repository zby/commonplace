---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Cortex workflow account: MCP capture through staged processing, bounded rejection, explicit recovery and result delivery."
run-id: AAS-2026-10-17-cortex-3da14ce55a2b-01
reviewed-boundary: a51c2209eb6d26812c19c97aaade3cb64ccfc23c
---

# Cortex workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is one `cortex_capture` request with `run_pipeline=True`, from caller input through ingestion, normalization, linking, enrichment and reasoning to the returned capture result. This is a connected shipped call chain, not a reconstruction of an external agent's task. It was selected because it combines caller classification, optional model proposals, durable mutations, structural rejection and partial-failure handling in one request. Its existing referent is [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline); this member adds workflow annotations rather than redeclaring it. SRC-1, `src/cortex/transport/mcp/server.py`, `src/cortex/pipeline/orchestrator.py`.

The evidence is inspected implementation and shipped doctrine/design at the [boundary](boundary.md#boundary-and-evidence), not an observed execution. Additional workflow inspection covers the complete orchestrator, normalizer, linker, enricher, reasoner and LLM service, and bounded MCP capture, context/read, reprocessing and classification handlers. These files belong to SRC-1 at the frozen revision. No target code, provider call or test was executed. The account establishes control flow and its limits, not successful capture, recovery, model compliance or benefit. External host planning and the decision to use returned knowledge remain outside the workflow.

### Request and ownership

The MCP caller supplies title, body, type, project, tags and optional template, summary, entities and properties. The tool's instruction assigns classification to the external Claude caller; it does not launch that caller or ensure compliance. Entities/properties arrive as JSON strings. A JSON syntax error discards the affected field rather than rejecting the capture. A supplied summary sets confidence to 0.9, which is a convention rather than a tested correctness probability. SRC-1, `src/cortex/transport/mcp/server.py`; [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline).

The handler transfers these inputs to `pipeline.capture`, with `captured_by="mcp"`. The orchestrator, not a model planner, owns every subsequent stage transition. Optional model calls are returning computations through [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client), not internally delegated agents with independent tool loops. Calling the tool supplies no evidence of per-object human approval. Source tool descriptions are doctrine/design; the Python call chain is implementation evidence. SRC-1, `src/cortex/transport/mcp/server.py`, `src/cortex/pipeline/orchestrator.py`, `src/cortex/services/llm.py`.

### Consequential handoffs

| Handoff | Supplied context and decision owner | Durable effect and returned state |
|---|---|---|
| Handler → capture | Caller fields plus channel label; code applies a recognized template and merges properties, with template properties winning. | `Store.create` admits the object before intelligence processing. Capture obtains its ID and initializes an `ingested` result. |
| Capture → normalize | The retained object ID; normalizer reloads the SQLite row. A stored non-empty summary selects reuse, otherwise the LLM service receives title and at most 8000 body characters. | Code writes summary/confidence/stage, conditionally type and missing tags/project, and graph summary/string properties. Optional embedding generation uses title plus at most 2000 body characters. Normalizer returns classification metadata and entities, not the full body. |
| Normalize → link | Orchestrator passes the object ID and caller entities when supplied, otherwise normalized entities. Linker reloads the document and selects up to 30 recent objects excluding self; the model prompt lists at most 20 candidates' IDs, types and titles, plus the new title/type and at most 4000 body characters. | Entity resolution creates/reuses nodes and adds mentions. Structurally accepted model relationships become graph edges. Return includes resolved entities and relationships/counts. |
| Link → enrich | Orchestrator passes the ID; enricher reloads the current row and relationships. Fixed code chooses tier and computes connection/staleness measures. | Tier and stage writes are attempted; the result reports tier, connection count and staleness. It is not a semantic acceptance judgment. |
| Enrich → reason | Orchestrator calls the reasoner without the capture ID. Fixed shipped queries operate on the whole current graph. | Missing inferred triples are added until no additions occur or the default ten-iteration bound is reached. Result contains per-rule counts, total and iterations. |
| Pipeline → handler → caller | Orchestrator collects stage dictionaries and computes overall status. Handler returns the capture dictionary directly. | Caller receives ID, initial capture type, status and per-stage results; retained content/edges remain available independently of caller follow-up. |

Evidence for these implementation handoffs: SRC-1, `src/cortex/transport/mcp/server.py`, `src/cortex/pipeline/orchestrator.py`, `src/cortex/pipeline/normalize.py`, `src/cortex/pipeline/link.py`, `src/cortex/pipeline/enrich.py`, `src/cortex/pipeline/reason.py`, `src/cortex/services/llm.py`. Storage compensation and consistency limits are established by [RT-OBJ-store](runtime.md#rt-obj-store) and [RT-CLM-store-consistency](runtime.md#rt-clm-store-consistency). In particular, the capture result's top-level type is initialized before normalization and is not replaced by the pipeline result; a normalized stage type and the retained type need not match that initial field. SRC-1, `src/cortex/pipeline/orchestrator.py`, `src/cortex/pipeline/normalize.py`.

The code chooses entity handoff precedence explicitly:

> entities = pre_entities if pre_entities is not None else norm_result.get("entities", [])
> --- `src/cortex/pipeline/orchestrator.py`

Thus even an explicitly supplied empty entity list overrides extraction. The caller-supplied path and internally validated classifier path have different checks: the classifier filters entity types and generic stopwords, while linker entity resolution trims names and skips empty names. The tool boundary parses caller JSON but does not apply the classifier's entity filter. This is not a claim that malformed shapes always succeed; exceptions can instead produce failed stages after ingestion. SRC-1, `src/cortex/transport/mcp/server.py`, `src/cortex/services/llm.py`, `src/cortex/pipeline/link.py`.

### Verification and rejection

This is open knowledge admission, not a bounded experiment with an independent expected-answer oracle. The caller proposes raw knowledge and may propose classification; the internal model optionally proposes classification or relationships. Fixed software decides how to parse, normalize and persist them. No inspected stage checks their truth against an independent reference or waits for human acceptance. The normalizer can skip the model entirely when a summary exists, and ingestion-only capture bypasses every processing stage. [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline); SRC-1, `src/cortex/pipeline/orchestrator.py`, `src/cortex/pipeline/normalize.py`, `src/cortex/services/llm.py`.

A concrete rejection branch exists within relationship discovery. The LLM adapter requires a JSON list, required relationship keys and confidence above 0.5. LinkStage then rejects an unknown predicate, missing endpoint, self-link or endpoint absent from SQLite. Relationship-write exceptions are logged and the rejected relationship is omitted from the created list. The captured document and earlier entity mentions are not thereby rejected. SRC-1, `src/cortex/services/llm.py`, `src/cortex/pipeline/link.py`.

> if from_id == to_id:
>     continue
> --- `src/cortex/pipeline/link.py`

The candidate prompt requests links between the new and an existing object, but LinkStage's inspected acceptance checks do not require either endpoint to equal the new object's ID or belong to the prompt candidate list. Their enforced scope is existing nonidentical endpoints and an allowed predicate. This limits what model-output validation guarantees; it is not evidence that a model actually proposed an out-of-scope link. SRC-1, `src/cortex/services/llm.py`, `src/cortex/pipeline/link.py`.

Reasoning applies the unchanged formal rules in [RT-OBJ-inference-rules](runtime.md#rt-obj-inference-rules), with authority described by [RT-BAP-rule-execution](runtime.md#rt-bap-rule-execution). Derivation is not a further correctness review of the captured body or criticism/revision of the rule set. Its theory-builder and learning limits remain those of [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge).

### Failure ownership and explicit recovery

If normalization raises to the orchestrator, it records normalize as failed and still invokes linking with caller entities or an empty list. Enrichment and reasoning also run under separate handlers. Any stage result marked exactly `failed` makes the overall result `partial`. The already-ingested object is not rolled back. This is best-effort continuation owned by the orchestrator, conditional on stage calls returning or raising; it is not a guarantee through process failure or dependency hangs. [RT-CLM-stage-resilience](runtime.md#rt-clm-stage-resilience); SRC-1, `src/cortex/pipeline/orchestrator.py`.

Some failures do not reach that status test. Classification failure returns a title-based summary with confidence zero; normalization can return `normalized` while preserving the original retained type. Graph-update and embedding errors are logged locally. Enrichment can report `enriched` despite write errors. ReasonStage converts a failed rule query into zero inferred triples. Consequently `complete` means no collected stage status equals `failed`, not verified semantic completion, consistent storage or successful application of every rule. SRC-1, `src/cortex/services/llm.py`, `src/cortex/pipeline/normalize.py`, `src/cortex/pipeline/enrich.py`, `src/cortex/pipeline/reason.py`; [RT-CLM-stage-resilience](runtime.md#rt-clm-stage-resilience).

Recovery beyond continuation requires another caller action. `cortex_pipeline(id)` first checks object existence, then reruns the pipeline. It does not resume a recorded failed instruction or reconstruct the original entity argument. In particular, it supplies no `pre_entities`; normalization of an object with a stored summary returns an empty entity list. A non-empty fallback summary can also cause later normalization to skip fresh classification after a provider becomes available. Reprocessing therefore is not guaranteed to repeat the original model/extraction handoff. SRC-1, `src/cortex/transport/mcp/server.py`, `src/cortex/pipeline/normalize.py`, `src/cortex/services/llm.py`, `src/cortex/pipeline/orchestrator.py`.

> return pipeline.run_pipeline(obj_id)
> --- `src/cortex/transport/mcp/server.py`

The separate `cortex_classify` tool permits the caller to supply corrected classification and entities after inspecting an object. That is an explicit maintenance route, not an automatic response to a partial capture, and it does not provide universal temporal rollback. [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge); SRC-1, `src/cortex/transport/mcp/server.py`.

### Delivery boundary

For this workflow, delivery is the MCP handler's return of the retained ID and processing result. No later `context`, `read`, approval, external action or success feedback is required by the capture call chain. A caller that chooses those later tools starts a separate request. Context delivers selected summaries; read reloads a fuller document and records access. Those are wired reuse opportunities, not evidence that this capture was retrieved, injected into a model window or acted on successfully. [RT-RTE-retrieve-context](runtime.md#rt-rte-retrieve-context), [RT-BAP-knowledge-delivery](runtime.md#rt-bap-knowledge-delivery); SRC-1, `src/cortex/transport/mcp/server.py`.

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

#### On [RT-RTE-capture-pipeline](runtime.md#rt-rte-capture-pipeline)

Workflow role: representative request-to-result chain. All inter-stage scheduling belongs to fixed orchestration code. Optional internal model work returns proposals rather than independent worker trajectories. Entity arguments have caller-over-normalizer precedence; persisted IDs carry state between stages. Processing begins after admission and can produce partial results without undoing the admitted document.

Workflow acceptance boundary: relationship rejection can omit individual proposals without rejecting capture. Overall completion is a stage-status aggregation, not a semantic oracle. The capture result's initial type is not a fresh read of final normalized state.

Workflow delivery: returned ID and stage/result dictionary terminate this request. Later retrieval and host use are optional, separately initiated operations.

#### On [RT-RTE-maintain-knowledge](runtime.md#rt-rte-maintain-knowledge)

Workflow recovery role: caller-selected reprocessing and caller-supplied reclassification are alternatives after an incomplete or unsatisfactory capture. Reprocessing neither restores the initial entity argument nor forces a new classification when a stored summary exists. Successful recovery remains unobserved.
