---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Dense-Mem workflow account: the shipped Python Remember, replay, recall and trace sequence and its bounded assessment rejection path."
run-id: AAS-2026-10-15-dense-mem-1a314bed9a5c-01
reviewed-boundary: bd736450454e237f1ab6d138f4ae9755916d73f6
---

# Dense-Mem workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is the shipped Python Remember example: submit evidence and a relationship proposal, repeat the submission, check replay equality, request recall, trace each relationship split returned by Remember, and return the original result. It is selected because a single source function explicitly joins these steps. It is not a workflow invented by combining independent service capabilities. [WF-CLM-client-delivery](#wf-clm-client-delivery) establishes the caller sequence and delivery boundary.

The [boundary](boundary.md#boundary-and-evidence) fixes SRC-1 at the reviewed commit. This account uses implementation, not an observed successful run. Additional source inspection covers the complete `packages/python/examples/remember.py`, the constructor and operation lifecycle in `packages/python/src/densemem/client.py`, and the validation/repair loop in `internal/remember/service/submission_assessment_session.go`. These files belong to SRC-1. The runtime's supplied records provide the service-side baseline; no target, test, example or provider was executed.

### Request and consequential handoffs

1. **Caller supplies the task.** The example constructs one evidence item about PostgreSQL and one proposed relationship with `evidence_indices: [0]`, plus an externally supplied operation key. Endpoint and bearer token come from environment variables. This is an ordinary open submission, not a benchmark with a reference answer. The script's author supplied the sample content; actual operator identity and human approval of any deployed submission are not established (SRC-1, `packages/python/examples/remember.py`; [WF-CLM-client-delivery](#wf-clm-client-delivery)).
2. **Client hands a bounded request to the service.** Each SDK operation deep-copies its request, obtains a credential, opens the HTTP/MCP session, initializes it and calls the named tool. The client owns request transport and error translation, not semantic judgment. Server authentication, team binding, argument validation and service dispatch then lead into [RT-RTE-remember-intake](runtime.md#rt-rte-remember-intake). The SDK's per-call session is not an enclosing agent conversation or a model sub-agent (SRC-1, `packages/python/src/densemem/client.py`).
3. **Service delegates interpretation, not control of progression.** The processor selects replay versus new work, prepares evidence and server-selected candidates, and asks the assessor for semantic proposals. Embedding requests receive planned search texts. The assessor does not receive arbitrary host context or unrestricted database access. Code owns validation, repair, embedding planning and commit progression; the remote model does not delegate onward to arbitrary tools. [RT-RTE-remember-intake](runtime.md#rt-rte-remember-intake) and [RT-OBJ-assessment-session](runtime.md#rt-obj-assessment-session) supply these handoff boundaries and their evidence.
4. **Software can reject the proposal.** The service validates the response and any additional response validator before accepting it for subsequent processing. Invalid output receives bounded correction, not automatic admission. Exhaustion returns a malformed-response error; provider or refresh errors also stop this loop. The workflow-specific rejection details are annotated below. Even valid output remains subject to the database fences in [RT-CLM-commit-fences](runtime.md#rt-clm-commit-fences). These are protocol and admission checks, not an independent factual oracle. There is no required per-proposal human acceptance in this route.
5. **Repository hands back a durable outcome.** The direct Remember route commits accepted evidence, semantic and search state under transaction fences, then projects a terminal result. The assessor's response is an intermediate product, not delivery. Repository rejection can prevent an accepted write after provider work. The SDK accepts a structured non-error result; failure results become exceptions. Source wiring alone does not establish deployed transaction success, response receipt or semantic truth ([RT-RTE-remember-intake](runtime.md#rt-rte-remember-intake); [WF-CLM-client-delivery](#wf-clm-client-delivery)).
6. **Caller challenges replay, then consumes retained state.** The example repeats the identical request and asserts equality. Completed or non-retryable terminal attempts replay; changed content under the same key conflicts; retryable failures can be retried by a later eligible call. These are service-owned recovery decisions, not SDK retries ([RT-RTE-remember-intake](runtime.md#rt-rte-remember-intake)). The equality assertion compares responses, not an independently known correct interpretation. If Remember raises or equality fails, the script does not proceed to recall and trace (SRC-1, `packages/python/examples/remember.py`).
7. **Caller requests recall and trace before returning.** Recall receives a fixed query and limit. The service returns selected evidence, relationships, discovery and possible degradation, not an enclosing answer ([RT-RTE-recall-context](runtime.md#rt-rte-recall-context)). The example discards the recall response. Its subsequent trace identifiers come from the original Remember relationship splits, not recall results; thus it must not be described as validating every recalled discovery. Trace responses are also discarded. Once those awaited calls finish, the function returns the original Remember result and the executable prints its processing state (SRC-1, `packages/python/examples/remember.py`; [WF-CLM-client-delivery](#wf-clm-client-delivery)).

### Failure, recovery and delivery limits

The checked rejection path is invalid semantic assessment. The service, not a supervisory agent or human reviewer, supplies validation errors for another bounded attempt. Exhaustion is terminal for this assessment invocation, not an instruction to keep trying until success. Durable attempt/retry handling belongs to the processor; valid response admission and replay do not establish exactly-once provider execution. The runtime distinguishes optional outer locking from accepted-write fences ([RT-RTE-remember-intake](runtime.md#rt-rte-remember-intake); [RT-CLM-commit-fences](runtime.md#rt-clm-commit-fences)).

At the caller boundary, failed structured results raise typed exceptions; cancellation can leave receipt unknown. The example contains neither exception recovery nor automatic retry after SDK failure. A caller wishing to recover must make another call under the service's idempotency contract; an exception alone cannot establish that nothing committed. Recall or trace failure can also stop this example after Remember has already returned. No workflow-wide rollback appears in this inspected script. This is a bounded source finding, not a claim that Dense-Mem lacks lifecycle or administrative correction elsewhere (SRC-1, `packages/python/src/densemem/client.py`, `packages/python/examples/remember.py`).

Delivery has two distinct boundaries: Remember's structured terminal return to the SDK, and completion of the example's later replay/recall/trace sequence. Neither establishes that a host used the returned context in an answer. The example performs no semantic assessment of trace output. Recall's instruction to verify discovery is advisory at the host boundary, not a mechanically enforced downstream answer gate ([RT-BAP-discovery-guidance](runtime.md#rt-bap-discovery-guidance)). Observed reliability, host compliance and answer benefit remain unestablished.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

#### WF-CLM-client-delivery
Label: Python example sequence and delivery boundary

Claimed operation: the shipped example awaits Remember, explicit replay, recall and tracing of the original result's splits, then returns that original result. The SDK requires structured content and raises on MCP error or failed processing state. This caller-level sequencing and delivery claim is distinct from the server route [RT-RTE-remember-intake](runtime.md#rt-rte-remember-intake) and retrieval route [RT-RTE-recall-context](runtime.md#rt-rte-recall-context): it spans their consumer and adds ordering, ignored returns and caller failure behavior, rather than declaring either route again. No supplied record identifies this complete caller contract. Source: SRC-1, `packages/python/examples/remember.py`, `packages/python/src/densemem/client.py`; implementation evidence only.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> result = await client.remember(request)
> replay = await client.remember(request)
> assert replay == result
> await client.recall_memory({"query": "Dense-Mem durable memory PostgreSQL", "limit": 5})
> for proposal in result["relationship_results"]:
>     for split in proposal["splits"]:
>         await client.trace_memory({"relationship_id": split["relationship_id"]})
> return result
> --- `packages/python/examples/remember.py`

> if not isinstance(result, dict):
>     raise DenseMemProtocolError(
>         "Dense-Mem did not return structured content"
>     )
> if response.isError or result.get("processing_state") == "failed":
> --- `packages/python/src/densemem/client.py`

> except asyncio.CancelledError:
>     raise DenseMemCancelledError(
>         "Dense-Mem operation cancelled; receipt is unknown"
>     ) from None
> --- `packages/python/src/densemem/client.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-remember-intake](runtime.md#rt-rte-remember-intake)

Workflow verification and recovery: within `completeRememberSessionTurnsWithValidator`, provider-supplied validation errors are considered first, then response preparation and the additional validator when earlier checks pass. Success returns only when no validation errors remain. On an invalid turn, the service records validation history, checks the total-turn bound, refreshes the request and calls Repair with the next request plus validation errors. Refresh/provider failures propagate rather than being converted into acceptance. This is a bounded software-controlled correction handoff, not proof of correct model reasoning or semantic truth (SRC-1, `internal/remember/service/submission_assessment_session.go`).

> if len(validationErrors) == 0 {
>     response.ProviderTurns = totalTurns
>     return response, request, nil
> }
> --- `internal/remember/service/submission_assessment_session.go`

> Message:                 "semantic assessor response remained invalid after bounded correction",
> FailureClass:            "malformed_exhausted",
> --- `internal/remember/service/submission_assessment_session.go`

> turn, err = s.provider.Repair(ctx, session, assessor.SemanticAssessmentRepairRequest{
>     Request: nextRequest, ValidationErrors: validationErrors,
> })
> --- `internal/remember/service/submission_assessment_session.go`

The caller's replay equality assertion is a separate check after service return. It does not replace admission validation, assess recalled evidence or resolve unknown receipt after cancellation. No SDK failure recovery is implemented by the inspected example; service-level replay remains available to a subsequent caller invocation ([WF-CLM-client-delivery](#wf-clm-client-delivery)).
