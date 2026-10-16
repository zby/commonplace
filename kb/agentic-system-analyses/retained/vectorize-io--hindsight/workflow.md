---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Hindsight workflow account: HTTP reflection from scoped retrieval through model completion, document rejection, recovery and response delivery."
run-id: AAS-2026-10-14-hindsight-34c2ca821edf-01
reviewed-boundary: "610c135b6f2d0d8b972da94146ae635943f36271"
---

# Hindsight workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is an HTTP reflection request that gathers bank-scoped evidence and delivers an answer. It was selected because it contains an implemented multi-step model/tool loop, explicit completion checks and a bounded rejection-and-retry path. It is Hindsight's inner answer workflow, not the external agent's complete task. The requesting principal's human or software identity is unresolved. The service owns progression and tool execution; the configured model proposes queries and completion. There is no established per-answer human approval or expected-answer oracle ([RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request)).

The baseline supplies request admission, retrieval dispatch and terminal synthesis. Added inspection covers `done` processing, document-shape rejection, length rewriting and HTTP delivery/error mapping. These are implementation passages in SRC-1 at the frozen commit: `hindsight-api-slim/hindsight_api/engine/reflect/agent.py`, `hindsight-api-slim/hindsight_api/engine/reflect/structured_doc.py` and `hindsight-api-slim/hindsight_api/api/http.py`. Their comments supply design rationale, not independently checked incident histories. No target execution, supplied trace or causal experiment establishes successful operation. The partial-loop boundary remains unchanged ([boundary](boundary.md#boundary-and-evidence)).

### Request to evidence

1. **Caller to service.** The caller supplies bank ID, query, retrieval budget and exposed filtering/output controls to the HTTP reflect endpoint. The handler delegates cancellable work to the memory engine. Authentication and an optional operation validator can reject the request. Authentication strength depends on configured tenancy and trusted-context conventions, not merely the presence of an authentication call ([RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request), [RT-CLM-tenant-check](runtime.md#rt-clm-tenant-check)).
2. **Engine to reflection loop.** The engine supplies resolved bank configuration, bank identity, directives and callbacks bound to the request's bank and selection controls. The model receives assembled messages and tool descriptions. It does not gain arbitrary database authority from a tool name. Code chooses the initial forced retrieval sequence; the model supplies query content and subsequent discretionary calls ([RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request)).
3. **Model proposals to real retrieval.** The loop checks enabled tool names and dispatches recognized proposals to scoped callbacks. Returned evidence enters current-request messages and history for later model calls. This is orchestration of model calls and retrieval executors, not delegation to independent agents authorized to execute arbitrary host tasks. For the Claude Code provider alternative, SDK MCP handlers collect proposals; Hindsight still performs the actual retrieval ([RT-RTE-provider-round](runtime.md#rt-rte-provider-round)).

### Evidence to accepted completion

4. **Completion proposal and evidence gate.** A proposed `done` call before the terminal iteration is sent back for more retrieval when no memory, mental-model or observation IDs have been gathered. Code checks evidence presence; it does not establish whether the evidence supports the answer. The baseline's forced retrieval policy and its terminal-synthesis exception prevent interpreting this as a universal grounding invariant ([RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request), [RT-RTE-context-synthesis](runtime.md#rt-rte-context-synthesis)).
5. **Document-shape gate where applicable.** When `done` carries a document object, code validates and renders its sections rather than treating arbitrary object representations as markdown. It normalizes certain unambiguous variations, including a single section without a wrapper. Type-invalid sections or blocks produce field-specific errors. The loop returns the rejected call and error to the same model conversation, requesting a corrected `done`. This is structural checking, not a semantic fact-check or criticism of a formulated explanation ([WF-CLM-completion-checks](#wf-clm-completion-checks)).
6. **Final content transformation.** A usable answer passes through optional length rewriting. A separate model call sees the answer and target budget and is asked to preserve key facts and structure while dropping lower-priority detail. Document-mode rewrites receive their own structural checks. On repeated structural failure the original full document survives, even if over budget. Afterwards unseen IDs are removed from answer text and declared supporting IDs are filtered against retrieved sets. Optional response-schema extraction operates on this resulting answer. Consequently the delivered text need not be the original `done` text, and retained supporting IDs establish retrieval membership rather than factual warrant or causal reliance ([WF-CLM-completion-checks](#wf-clm-completion-checks)).

### Recovery and delivery

Recovery is owned by orchestration code, with correction content supplied by the model. In the ordinary loop, document rejection increments a bounded counter, appends diagnostic feedback and continues; exhaustion or the terminal iteration raises the error. A completion with no usable answer fails rather than becoming a successful placeholder. Length-rewrite rejection has a different recovery rule: retry the rewrite, then preserve the pre-rewrite answer. These are distinct acceptance policies. Shape validity is enforced by code at these gates; semantic preservation and adherence to a requested length remain model-dependent ([WF-CLM-completion-checks](#wf-clm-completion-checks)).

Budget exhaustion can instead stop retrieval and invoke final synthesis, including evidence partitioning and parallel compression when needed. Compression calls return generated claim sections to reduction, not necessarily every original evidence byte. Compacted tool messages do not erase the separate current-request history reachable by synthesis. This fallback is a working-context mechanism; it does not establish durable memory or lossless semantic preservation ([RT-RTE-context-synthesis](runtime.md#rt-rte-context-synthesis)).

Delivery means the engine result reaches an HTTP response containing text, usage, optional supporting material/traces and structured-output result or error. It does not mean the client accepted the answer, an external host acted on it, or Hindsight automatically retained the answer. HTTP maps no-answer and tool-calling failures to server failures; retrieval failure can receive a store-unavailable response, and timeout receives 504. The caller must own any subsequent request retry; this account establishes no retry-until-success contract ([RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request), [WF-CLM-completion-checks](#wf-clm-completion-checks)).

The selected workflow therefore establishes implemented delegation, structural verification, local recovery and transport delivery. It does not establish answer correctness, model compliance with directives, client uptake, improved future action or reliable deployed completion. Full recall ranking, alternative integrations, consolidation admission and host task execution are not conclusions of this trace.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

#### WF-CLM-completion-checks
Label: Reflection completion checks

Claimed operation: reflection's completion processing checks document shape, can request correction, transforms accepted content for visible-length and ID handling, and returns a result or failure through HTTP. This record adds a workflow-specific finding about verification and recovery, not a second declaration of the request or synthesis route. Its closest supplied records are [RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request) and [RT-RTE-context-synthesis](runtime.md#rt-rte-context-synthesis); those describe route identity and budget fallback, whereas this claim establishes the inspected completion gates and their different rejection outcomes.

- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, implementation: `hindsight-api-slim/hindsight_api/engine/reflect/agent.py`, `hindsight-api-slim/hindsight_api/engine/reflect/structured_doc.py`, `hindsight-api-slim/hindsight_api/api/http.py`. Structural checks do not provide an answer oracle, establish successful correction or guarantee semantic preservation.

Document parsing validates block types and raises rather than coercing object content:

> for j, raw_block in enumerate(raw_blocks):
>     if not isinstance(raw_block, str):
>         errors.append(
>             f"sections[{i}].blocks[{j}]: expected a markdown string, got {type(raw_block).__name__} "
>             f"({raw_block!r:.80}) — write the markdown itself, not an object wrapping it"
>         )
> validated.append(raw_section)
> if errors:
>     raise DocumentSectionsInvalidError(errors)
> --- `hindsight-api-slim/hindsight_api/engine/reflect/structured_doc.py`

Ordinary completion rejection ends in failure when retries or iterations are exhausted; otherwise errors re-enter the model conversation:

> if document_rejections > _MAX_DOCUMENT_REJECTIONS or iteration >= max_iterations - 1:
>     raise
> messages.extend(_document_rejection_messages(done_call, exc))
> continue
> --- `hindsight-api-slim/hindsight_api/engine/reflect/agent.py`

The corrective handoff explicitly requests the same content with shape repairs:

> "Your document did not match the required shape, so it was discarded. "
> "Call done() again with the same content, fixing: " + "; ".join(exc.errors)
> --- `hindsight-api-slim/hindsight_api/engine/reflect/agent.py`

Length rewriting instead preserves the original document after repeated rejection:

> if rejections > _MAX_DOCUMENT_REJECTIONS:
>     # ``applied`` records that a call was made and billed; the
>     # content is the input unchanged.
>     return _rewrite(answer, document)
> --- `hindsight-api-slim/hindsight_api/engine/reflect/agent.py`

The rewrite's instruction requests preservation; it does not verify it:

> "Shorten the user's document so it fits within the requested token budget. "
> "Preserve the key facts and the document's structure; drop lower-priority detail. "
> --- `hindsight-api-slim/hindsight_api/engine/reflect/agent.py`

Final processing removes unseen IDs and filters supporting identifiers against retrieved sets:

> answer = presenter.drop_unseen_ids(answer)
> if document is not None:
>     document = _map_document_text(document, presenter.drop_unseen_ids)
>
> # Validate IDs (only include IDs that were actually retrieved)
> used_memory_ids = [mid for mid in (args.get("memory_ids") or []) if mid in available_memory_ids]
> used_mental_model_ids = [mid for mid in (args.get("mental_model_ids") or []) if mid in available_mental_model_ids]
> used_observation_ids = [oid for oid in (args.get("observation_ids") or []) if oid in available_observation_ids]
> --- `hindsight-api-slim/hindsight_api/engine/reflect/agent.py`

HTTP delivery includes postprocessed text and may report structured-output extraction failure separately:

> return ReflectResponse(
>     text=core_result.text,
>     based_on=based_on_result,
>     structured_output=core_result.structured_output,
>     structured_output_error=core_result.structured_output_error,
>     usage=core_result.usage,
>     trace=trace_result,
> )
> --- `hindsight-api-slim/hindsight_api/api/http.py`

The no-answer path is a failure, not delivered answer content:

> logger.warning("Reflect produced no answer in bank %s: %s", bank_id, e)
> raise HTTPException(status_code=500, detail=str(e))
> --- `hindsight-api-slim/hindsight_api/api/http.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-reflect-request](runtime.md#rt-rte-reflect-request)

Workflow verification: transport admission and enabled-tool dispatch are code-owned gates. Evidence presence before ordinary completion is not evidential sufficiency. Document-mode completion adds structural rejection and model correction; a delivered result has passed intervening transformations rather than necessarily preserving the raw proposal. Workflow recovery and delivery details are established in [WF-CLM-completion-checks](#wf-clm-completion-checks). No per-answer human judgment or correctness oracle is established.

#### On [RT-RTE-context-synthesis](runtime.md#rt-rte-context-synthesis)

Workflow role: this is the branch that ends retrieval under iteration/context pressure, not an approval of every nominal retrieval step. The terminal answer still undergoes final output processing. A length budget is a requested target rather than a strict transport acceptance limit, since document rewrite failure can preserve an over-budget original ([WF-CLM-completion-checks](#wf-clm-completion-checks)).
