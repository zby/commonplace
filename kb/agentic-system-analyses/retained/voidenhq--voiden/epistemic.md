---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Voiden epistemic routes: request evidence, outcome classification, response retention and delegated tool verification."
run-id: AAS-2026-10-14-voiden-98188b4a2f55-01
reviewed-boundary: d7a0d05c40acb6cc483000643c700f17aecba0ef
---

# Voiden epistemic report

## Source-and-claim boundary

The question is what the agent-facing MCP subsystem can establish about requests and published tools, and how those results affect later use. Scope and exclusions are those of the [boundary](boundary.md#boundary-and-evidence); source identities and layers are in its [Source register](boundary.md#source-register). Every source finding below uses SRC-1 at the frozen revision. This is a subsystem assessment, not a whole-product or external-agent verdict.

Direct reads establish request outcome classification, result serialization, fixed tools, pipeline hooks, provider dispatch, CLI verification and publisher refresh. Supplied runtime records establish the surrounding registration, network, variable, plugin and durable-driver routes. All are implementation or doctrine/design evidence. There are no supplied observed runs or causal experiments. Missing external plugin implementations prevent judging verification predicates, expected answers, status persistence semantics and parameter binding. Missing remote endpoint evidence prevents verifying response propositions. Missing host/model evidence prevents establishing interpretation, obedience, criticism or accepted knowledge in the enclosing agent. Actual project artifacts and provenance are not supplied, so no candidate instance is claimed observed.

The consequential warrant claim found is [EPI-CLM-request-check](#epi-clm-request-check). The supplied [RT-CLM-version-gating](runtime.md#rt-clm-version-gating) is consequential to reproducibility; access and confinement claims concern operational limits rather than truth of response content.

| Entry point or operation | Source path, SRC-1 | Coverage and evidence basis | Limit / conclusion prevented |
| --- | --- | --- | --- |
| Bundled agent/run/stdio; desktop registration | `apps/electron/src/voiden-cli.ts`; `apps/electron/src/main/ipc/mcp.ts` | Supplied [RT-RTE-host-registration](runtime.md#rt-rte-host-registration), [RT-RTE-request-execution](runtime.md#rt-rte-request-execution), [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission) | Host operation and plugin bytes unavailable |
| Six fixed tools, discovery, environment choice | `packages/voiden-runner/src/mcpServing.ts` | Direct handlers; supplied [RT-OBJ-runtime-vars](runtime.md#rt-obj-runtime-vars), [RT-RTE-result-write](runtime.md#rt-rte-result-write) | Discovery is not factual verification; environment choice is policy/state |
| Builders, pre/post hooks, response callbacks | `packages/executors/src/orchestrator.ts`; `packages/executors/src/pipeline/executor.ts`; `packages/voiden-runner/src/runner.ts` | Direct pipeline and runner reads; [RT-CMP-request-orchestrator](runtime.md#rt-cmp-request-orchestrator), [EPI-RTE-outcome-classification](#epi-rte-outcome-classification) | Plugin checks opaque; a response callback exception is swallowed |
| Write-back and replacement | `packages/voiden-runner/src/resultBlock.ts` | Direct complete file; [EPI-RTE-response-serialization](#epi-rte-response-serialization), supplied [RT-RTE-result-write](runtime.md#rt-rte-result-write) | No authenticated binding to a preceding execution |
| Standalone tool list/verify/--write | `packages/voiden-runner/src/index.ts` | Direct command dispatch; [EPI-RTE-cli-verification](#epi-rte-cli-verification) | Runtime omitted this separate evaluator-output consumer, not a defect in its publishing route |
| Provider APIs and status/cache objects | `packages/voiden-runner/src/mcpToolCapability.ts` | Direct complete file; supplied [RT-OBJ-serve-decisions](runtime.md#rt-obj-serve-decisions), [RT-RTE-tool-publication](runtime.md#rt-rte-tool-publication) | Registered provider implementation unavailable; statuses are not proof |
| Publisher planning/check/refresh | `packages/voiden-mcp/src/lib.ts` | Direct refresh and exclusion helper; supplied [RT-RTE-tool-publication](runtime.md#rt-rte-tool-publication) | No independent inspected evaluator beyond delegated provider |
| Outgoing MCP, protocol execution | `packages/executors/src/mcp.ts`; `packages/executors/src/secureRequest.ts` | Supplied [RT-RTE-remote-mcp](runtime.md#rt-rte-remote-mcp) | Remote tool-level failure can coexist with RPC success |
| Variables and durable standalone run | `packages/voiden-runner/src/runner.ts`; `packages/voiden-runner/src/index.ts` | Direct capture consumer; supplied [RT-RTE-session-driver](runtime.md#rt-rte-session-driver) | No acceptance gate between response extraction and variable use |
| Plugin install/update and guides | `packages/voiden-runner/src/plugins/managementTools.ts`; `packages/executors/src/skillContent.ts`; `apps/electron/src/main/skillsComposer.ts` | Supplied plugin/guide records; direct standalone guide | Software admission is not performance comparison; guide obedience unobserved |

Uninspected protocol-specific implementations and excluded general desktop functions prevent a system-complete negative about evaluation. The selected core routes support bounded positive mechanisms without resolving those alternatives.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-run-result](#epi-obj-run-result) | Response payload propositions, if any; bounded claim about status-based outcome | see record | SRC-1, `packages/voiden-runner/src/runner.ts` | Payload content not supplied; truth-apt payload individuation not determinable |
| [RT-RTE-result-write](runtime.md#rt-rte-result-write) | Caller-proposed outcome record | see record | SRC-1, `packages/voiden-runner/src/resultBlock.ts` | Retained YAML has no execution authentication; synthetic timestamp is write time |
| [RT-OBJ-runtime-vars](runtime.md#rt-obj-runtime-vars) | Extracted response values may carry claims; identifiers/secrets are often not truth-apt | see record | SRC-1, `packages/voiden-runner/src/runner.ts` | Classification depends on uncaptured values and consumers |
| [RT-OBJ-serve-decisions](runtime.md#rt-obj-serve-decisions) | Passed/state claims concerning authored verification cases | see record | SRC-1, `packages/voiden-runner/src/mcpToolCapability.ts` | Provider criteria and actual records unavailable |
| [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance) | Procedural policy plus claims about checking requests | see record | SRC-1, `packages/executors/src/skillContent.ts` | Natural-language interpretation external |
| [RT-CMP-plugin-runner](runtime.md#rt-cmp-plugin-runner) | None established in executable module/version admission | see record | SRC-1, `packages/voiden-runner/src/plugins/loader.ts` | Callback contents opaque; availability is not warrant |

## Authority-route ledger

Route ID: [RT-RTE-request-execution](runtime.md#rt-rte-request-execution)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-run-result](#epi-obj-run-result).
Content/update relation: truth-apt transformation: acquisition/import — where a response contains propositions; source warrant unknown. Otherwise the payload is operational data.
Transition or check target: see route; external response to structured result.
Evaluator/condition and domain: no evaluator of payload truth established; protocol execution is the acquisition mechanism.
Activation and timing: see route.
Possible or observed result: see route; no observed instance.
Implemented force: delivery, not endorsement.
Epistemic authority and scope: endpoint-attributed data, not accepted truth.
Operational authority: external host may continue; plugin hooks may alter response/state.
Behavioral-authority path: host via MCP JSON, advisory, present invocation; variables via symbolic map, permissive, later calls.
Evidence source ID and local anchor: SRC-1, `packages/voiden-runner/src/runner.ts`; see route.
Claim IDs: [EPI-CLM-request-check](#epi-clm-request-check).
Mismatch marker: execution does not establish intended task correctness.
Gap/limit: plugin transformation semantics and endpoint truth unavailable.

Route ID: [EPI-RTE-outcome-classification](#epi-rte-outcome-classification)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-run-result](#epi-obj-run-result).
Content/update relation: truth-apt transformation: entailed derivation.
Transition or check target: bounded proposition that a PipelineResponse meets the success predicate.
Evaluator/condition and domain: see record; deterministic TypeScript over response error, protocol and status.
Activation and timing: see record.
Possible or observed result: see record; boolean success, no observed run.
Implemented force: outcome labeling only; consumption separate below.
Epistemic authority and scope: exact predicate result, conditional on supplied fields; not response truth or task fulfillment.
Operational authority: no independent action at this check.
Behavioral-authority path: see consumption row.
Evidence source ID and local anchor: SRC-1, `packages/voiden-runner/src/runner.ts`.
Claim IDs: [EPI-CLM-request-check](#epi-clm-request-check).
Mismatch marker: guide requests a stricter non-2xx/body check than the core predicate.
Gap/limit: fields may be plugin-mutated; source premises not independently warranted.

Route ID: [RT-RTE-request-execution](runtime.md#rt-rte-request-execution)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-run-result](#epi-obj-run-result).
Content/update relation: no content change.
Transition or check target: aggregate failure indication from section success fields.
Evaluator/condition and domain: fixed MCP handler tests whether any result explicitly has success false.
Activation and timing: after runVoidFile returns.
Possible or observed result: full result with optional isError; see route.
Implemented force: caller-visible error marking; no automatic repair or factual acceptance.
Epistemic authority and scope: same limited classifier license.
Operational authority: host can inspect/retry; failure marking does not block write_result or later calls.
Behavioral-authority path: external MCP caller, result/isError, advisory, this call.
Evidence source ID and local anchor: SRC-1, `packages/voiden-runner/src/mcpServing.ts`.
Claim IDs: [EPI-CLM-request-check](#epi-clm-request-check).
Mismatch marker: none.
Gap/limit: host action unobserved; per-section execution can continue after failure.

Route ID: [EPI-RTE-response-serialization](#epi-rte-response-serialization)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [RT-RTE-result-write](runtime.md#rt-rte-result-write).
Content/update relation: truth-apt transformation: non-ampliative reshaping — selected supplied fields serialized, string body truncated, write metadata added.
Transition or check target: caller result to fenced YAML response.
Evaluator/condition and domain: see record; no semantic evaluator.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: none independent of subsequent file write.
Epistemic authority and scope: no added warrant; completeness degraded on truncation and omitted fields, original provenance unknown.
Operational authority: prepares file content, not approval.
Behavioral-authority path: see retention row.
Evidence source ID and local anchor: SRC-1, `packages/voiden-runner/src/resultBlock.ts`.
Claim IDs: [EPI-CLM-request-check](#epi-clm-request-check).
Mismatch marker: recorded content need not be what actually happened.
Gap/limit: no execution-linked proof; reportEntries and protocol are not among serialized attributes.

Route ID: [RT-RTE-result-write](runtime.md#rt-rte-result-write)
Route function: retention
Architectural status: implemented
Object/candidate ID: see route.
Content/update relation: no content change — write of prepared block.
Transition or check target: matching UID and section placement, not factual acceptance.
Evaluator/condition and domain: see route.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: persistent replacement/insertion.
Epistemic authority and scope: none added by retention; missing UID rejects placement only.
Operational authority: later readers can use recorded response; no acceptance criterion for a knowledge claim.
Behavioral-authority path: filesystem readers, response YAML, advisory/reader-defined, until replacement or overwrite.
Evidence source ID and local anchor: SRC-1, `packages/voiden-runner/src/resultBlock.ts`.
Claim IDs: [EPI-CLM-request-check](#epi-clm-request-check).
Mismatch marker: no authenticated execution-to-record binding.
Gap/limit: rerunning reads the document but does not by itself prove a response proposition changed a later request. No lifecycle integration after evidence-consuming acceptance is established here.

Route ID: [RT-RTE-tool-publication](runtime.md#rt-rte-tool-publication)
Route function: check/evidence production
Architectural status: not determinable
Object/candidate ID: [RT-OBJ-serve-decisions](runtime.md#rt-obj-serve-decisions).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: authored tool contract/auth cases in provider-defined domain.
Evaluator/condition and domain: provider's validate/verify/plan implementation unavailable; dispatch implemented.
Activation and timing: see route.
Possible or observed result: see route; verified/unverified/failing protocol labels, not observed results.
Implemented force: delegation is wired; substantive check not inspected.
Epistemic authority and scope: license not determinable without case predicates, expected values and environment binding.
Operational authority: planning supplies decisions for later registration.
Behavioral-authority path: see next row.
Evidence source ID and local anchor: SRC-1, `packages/voiden-runner/src/mcpToolCapability.ts`.
Claim IDs: none.
Mismatch marker: no-provider validateTools accepts supplied tools, whereas verify/plan return empty lists.
Gap/limit: interfaces and status names do not establish checks or acceptance. No ampliative classification follows merely from unknown entailment.

Route ID: [RT-RTE-tool-publication](runtime.md#rt-rte-tool-publication)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-serve-decisions](runtime.md#rt-obj-serve-decisions).
Content/update relation: no content change.
Transition or check target: decisions passed to registration and later refreshed.
Evaluator/condition and domain: core timing/transport; provider registration policy opaque.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: core invokes provider registration; HTTP uses latest successful decisions; supervised stdio may restart.
Epistemic authority and scope: no extra warrant from availability or restart.
Operational authority: exposure/withdrawal through provider, not universal verified-only execution.
Behavioral-authority path: MCP clients, tool surface/descriptions, permissive/advisory, startup or successful refresh horizon.
Evidence source ID and local anchor: SRC-1, `packages/voiden-mcp/src/lib.ts`.
Claim IDs: none.
Mismatch marker: refresh failures log without clearing previous decisions; detection misses additions/deletions and description-only changes.
Gap/limit: unavailable provider controls actual registration; generic request and outgoing MCP routes bypass publication admission.

Route ID: [EPI-RTE-cli-verification](#epi-rte-cli-verification)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-serve-decisions](runtime.md#rt-obj-serve-decisions), provider status subset.
Content/update relation: no content change.
Transition or check target: computed status/issues to report and process exit.
Evaluator/condition and domain: see record; state failing or issues present determines failure exit.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: reporting and exit status; optional delegated status write is a separate retention function, not acceptance.
Epistemic authority and scope: delegated status only; no additional validation of expected answers.
Operational authority: human/CI can reject continuation on nonzero exit; no inspected CI consumer.
Behavioral-authority path: CLI operator/CI, stdout and exit code, advisory or externally enforcing, invocation.
Evidence source ID and local anchor: SRC-1, `packages/voiden-runner/src/index.ts`.
Claim IDs: none.
Mismatch marker: unverified alone does not fail; empty discovery exits success.
Gap/limit: persisted status semantics and downstream consumer unavailable.

Route ID: [EPI-RTE-cli-verification](#epi-rte-cli-verification)
Route function: retention
Architectural status: not determinable
Object/candidate ID: provider-produced ToolStatus; see [RT-OBJ-serve-decisions](runtime.md#rt-obj-serve-decisions).
Content/update relation: truth-apt transformation: indeterminate — state/note passed to an unavailable writer.
Transition or check target: computed state to tool-block status record, not acceptance of a new proposition.
Evaluator/condition and domain: CLI --write condition is inspected; substantive persistence delegated to provider.
Activation and timing: after verification, for each returned status when --write is set.
Possible or observed result: core attempts writes and logs exceptions; no observed persistence.
Implemented force: writer dispatch wired; material retention semantics not determinable.
Epistemic authority and scope: no added warrant from attempted persistence.
Operational authority: possible later status use is provider-defined, not established.
Behavioral-authority path: project-file readers, delegated status encoding, force/horizon uninspected.
Evidence source ID and local anchor: SRC-1, `packages/voiden-runner/src/index.ts`; see record.
Claim IDs: none.
Mismatch marker: write failures do not enter failure-exit calculation.
Gap/limit: no inspected later consumer or lifecycle integration; core wiring does not prove provider persistence.

Route ID: [RT-RTE-request-execution](runtime.md#rt-rte-request-execution), [RT-CLM-version-gating](runtime.md#rt-clm-version-gating)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: tagged block version metadata, not response truth.
Content/update relation: no content change.
Transition or check target: compatibility of declared plugin version with installed metadata.
Evaluator/condition and domain: see claim; classifier plus runner rejection, tagged blocks only.
Activation and timing: before section orchestration; see route.
Possible or observed result: rejection or continuation; no observed instance.
Implemented force: enforced for this runner check, not transitive plugin execution.
Epistemic authority and scope: metadata-level compatibility, not byte identity, source truth or outcome reproducibility.
Operational authority: permits or blocks section execution.
Behavioral-authority path: runVoidFile, exception/continuation, enforcing, present section.
Evidence source ID and local anchor: SRC-1, `packages/voiden-runner/src/runner.ts`; `packages/executors/src/blockVersioning.ts`; see claim.
Claim IDs: [RT-CLM-version-gating](runtime.md#rt-clm-version-gating).
Mismatch marker: compatible newer versions pass; untagged blocks bypass.
Gap/limit: accurate metadata and external plugin compatibility are required; no authenticity check.

Route ID: [RT-RTE-session-driver](runtime.md#rt-rte-session-driver)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: see [RT-OBJ-runtime-vars](runtime.md#rt-obj-runtime-vars).
Content/update relation: non-truth-apt policy/content update: execution bindings from selected request/response values, potentially carrying truth-apt content whose scope is uncaptured.
Transition or check target: extracted values become later substitution inputs, not accepted propositions.
Evaluator/condition and domain: capture expressions and session mode; see records.
Activation and timing: see records.
Possible or observed result: see records.
Implemented force: symbolic binding/substitution; durable standalone variant reloads values.
Epistemic authority and scope: no warrant upgrade or truth acceptance.
Operational authority: later requests can change without a separate factual check.
Behavioral-authority path: request executor/plugins, map and saved JSON, permissive, later sections/calls or standalone sessions.
Evidence source ID and local anchor: SRC-1, `packages/voiden-runner/src/runner.ts`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: exercised dependence and improved capacity unobserved.

Route ID: [RT-RTE-host-registration](runtime.md#rt-rte-host-registration), [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-run-result](#epi-obj-run-result).
Content/update relation: no content change.
Transition or check target: response body matches intended request purpose.
Evaluator/condition and domain: foreground human/model interpretation requested by installed guide; intended purpose project-dependent, no reference answer supplied.
Activation and timing: after run_request, before optional recording; see guidance.
Possible or observed result: inspect/fix/rerun or record requested, not observed.
Implemented force: advisory natural-language instruction.
Epistemic authority and scope: requested purpose-fit assessment, not implemented evidence-consuming acceptance.
Operational authority: host may revise or continue; fixed handlers do not enforce this order.
Behavioral-authority path: see guidance record.
Evidence source ID and local anchor: SRC-1, `packages/executors/src/skillContent.ts`.
Claim IDs: [EPI-CLM-request-check](#epi-clm-request-check).
Mismatch marker: policy exceeds enforcement at write_result.
Gap/limit: external host reasoning and compliance unavailable.

Plugin compatibility/admission and remote MCP remain separate operational checks: see [RT-CLM-version-gating](runtime.md#rt-clm-version-gating), [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission), [RT-RTE-remote-mcp](runtime.md#rt-rte-remote-mcp). Their evaluators concern compatibility, asset availability/loadability and RPC completion, respectively, not truth of acquired content. They license compatible execution/capability installation/remote continuation within their recorded domains; none supplies an answer oracle for the caller's task. Core responses and recovery cannot undo remote effects. These distinctions prevent importing publication verification into generic execution.

## System-claim versus route comparison

| Claim ID | Claimed operation/warrant | Source/anchor and layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support/design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-request-check](#epi-clm-request-check) | see record | SRC-1, `packages/executors/src/skillContent.ts`, doctrine/design | Execute, inspect, fix/rerun, optionally record | [RT-RTE-request-execution](runtime.md#rt-rte-request-execution), [EPI-RTE-outcome-classification](#epi-rte-outcome-classification), [RT-RTE-result-write](runtime.md#rt-rte-result-write) | none supplied | No host compliance, reference-answer or outcome experiment | Real execution mechanism plus bounded classifier and requested semantic review | Body correctness and record authenticity not enforced; 3xx passes core classifier but guide flags non-2xx |
| [RT-CLM-version-gating](runtime.md#rt-clm-version-gating) | see record | SRC-1, `packages/voiden-runner/src/runner.ts`, implementation comment versus implementation | see record | [RT-RTE-request-execution](runtime.md#rt-rte-request-execution) | none supplied | External bytes and metadata contract | Tagged-block compatibility predicate | Not exact version/byte replay; untagged blocks bypass |

## Bounded conclusion

Voiden's inspected core acquires network/tool output and derives bounded execution classifications. It does not warrant endpoint propositions from successful status codes. A concrete REST response with status 302 and no error yields success true; status 401 yields false. Those are entailed results of the inspected predicate, not warranted assertions that the requested business operation succeeded. Outgoing MCP separately distinguishes RPC completion from remote tool-level success.

Response retention is a caller-controlled ledger operation. Serialization loses completeness on long bodies and drops some fields, while assigning a fresh write timestamp and UID. Matching requestUid establishes placement, not historical provenance. The guidance asks for purpose-fit inspection and genuine results, but no core evidence-consuming acceptance decision against a named factual criterion is enforced before writing. Post-acceptance lifecycle integration is consequently not established by this route; persistence and operational use remain separate.

Published-tool verification is a meaningful but opaque alternative, not an evidenced absence of testing. Core dispatch, cached decision reuse, refresh and CLI status consumption are implemented; actual check predicates, oracles and acceptance scope belong to the unavailable provider. CLI failure status can inform CI; unverified status is not itself a failure. Refresh failure preserves the prior plan, and generic execution bypasses this publishing channel. Availability and verification labels alone therefore establish no system-wide warrant.

Captured variables can directly change later request execution, and plugin management changes available executable machinery. Neither route independently establishes learning, improved performance or exercised self-improvement. Installed prose can request external-agent inspection and revision; delivery alone establishes neither reflection nor theory-builder consumption, criticism or iteration. No inspected core route calls or updates distributed-parametric state; the external model host's internals remain outside scope. These independent limits do not erase the implemented acquisition, checking, retention and operational-consumption paths.

## Shared records

### Operative objects

#### EPI-OBJ-run-result
Label: RunResult

Part of: [RT-RTE-request-execution](runtime.md#rt-rte-request-execution)

This object is the result material produced by that route, hence a different-kind containment relation, not a duplicate route. Source-native symbolic fields plus payload text/JSON; substrate is process memory and MCP JSON delivery, optionally reshaped into document YAML through a separate supplied write route. Source: SRC-1, `packages/voiden-runner/src/runner.ts`. Status-derived claims have a concrete predicate; payload propositions depend on missing actual content. The object can include reportEntries that write-back does not serialize.

> if (response.metadata?.reportEntries) {
>     result.reportEntries = response.metadata.reportEntries
>   }
> --- `packages/voiden-runner/src/runner.ts`

### Routes

#### EPI-RTE-outcome-classification
Label: Outcome classification

Part of: [RT-RTE-request-execution](runtime.md#rt-rte-request-execution)

Material deterministic check/derivation part, distinct from network acquisition and its downstream consumer. Endpoints: PipelineResponse → toRunResult → RunResult.success. Owner is symbolic TypeScript; context is protocol/status/error supplied after hooks. It derives a predicate result, without evaluating body truth. For a concrete hypothetical input protocol rest, statusCode 302, error undefined, protocol membership is true, !error is true and 200 <= 302 < 400 is true, hence success true. Changing statusCode to 401 makes it false. This is deduction from implementation, not target execution. No reference answer or human veto is involved in this classifier; mode is open request execution, not an improvement experiment. SRC-1, `packages/voiden-runner/src/runner.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: RunResult with success and protocol/status/body/error fields.
- Later read-back: inapplicable — classifier itself does not retain state; optional caller write is separate.
- Delegated visibility: MCP caller receives fields; downstream capture code reads the result.
- Selection predicate: REST/HTTP/HTTPS membership, status range and absence of error.
- Invalidation or expiry: recomputed each execution; old retained results are not updated automatically.
- Activation or effect: boolean controls MCP failure marking; actual host response unobserved.
- Evidence limits: input fields not independently authenticated; no task/body oracle; non-HTTP rule uses positive status.

> const protocol = response.protocol ?? 'rest'
>   const isHttpLike = protocol === 'rest' || protocol === 'http' || protocol === 'https'
>   const statusCode = response.statusCode ?? 0
>   const success = !response.error && (
>     isHttpLike ? (statusCode >= 200 && statusCode < 400) : statusCode > 0
>   )
> --- `packages/voiden-runner/src/runner.ts`

#### EPI-RTE-response-serialization
Label: Response serialization

Part of: [RT-RTE-result-write](runtime.md#rt-rte-result-write)

Material reshaping part of supplied result admission, distinct from placement/write. Endpoints: caller RunResult → buildResponseBlockText → YAML fence. Owner is symbolic serializer; context includes caller fields and requestUid; new UID and capturedAt are write metadata. With a hypothetical string body of 20,001 characters, slice retains 20,000 and sets truncated true. A 20,000-character body remains unchanged. This deterministic deduction needs no target execution. Selected field copying and truncation do not add a novel endpoint claim; semantic completeness is degraded. Admission/authorship and rollback are those of the parent route; serializer offers neither separate human approval nor an answer oracle. SRC-1, `packages/voiden-runner/src/resultBlock.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: fenced response YAML text with supplied fields and write metadata.
- Later read-back: inapplicable — this part returns text; parent persists it.
- Delegated visibility: parent writes selected attributes; reportEntries and protocol are not copied.
- Selection predicate: optional attributes copied when their conditions hold; body truncates only for long strings.
- Invalidation or expiry: parent replacement/overwrite governs retained instance.
- Activation or effect: string passed into document replacement; no semantic check or acceptance.
- Evidence limits: caller provenance unknown; no source-visible factual validation; write timestamp is not execution time.

> const MAX_BODY_CHARS = 20_000
> --- `packages/voiden-runner/src/resultBlock.ts`

> if (typeof body === 'string' && body.length > MAX_BODY_CHARS) {
>     body = body.slice(0, MAX_BODY_CHARS)
>     truncated = true
>   }
> --- `packages/voiden-runner/src/resultBlock.ts`

> const attrs: Record<string, any> = {
>     uid: randomUUID(),
>     requestUid,
>     capturedAt: new Date().toISOString(),
>     success: result.success,
>   }
> --- `packages/voiden-runner/src/resultBlock.ts`

#### EPI-RTE-cli-verification
Label: CLI verification consumer

Distinct from [RT-RTE-tool-publication](runtime.md#rt-rte-tool-publication): standalone CLI command consumes the same provider APIs but does not publish tools or schedule refresh. No counterpart among supplied records for this operator/CI consumer. Endpoints: tool verify command → discover/validate/verify → output/optional status write → exit. Operator or CI supplies paths, cadence and environment; provider decides validity/status; code decides exit and invokes write when requested. External humans/CI may veto later deployment, but that consumer is not inspected. No core expected-answer oracle; provider internals opaque. Mode is one-shot verification; cadence is a filter, not time enforcement. --write admits provider-computed status into project files; errors are reported without transactional rollback. It is not historical truth acceptance and does not itself demonstrate improvement. SRC-1, `packages/voiden-runner/src/index.ts` and `packages/voiden-runner/src/mcpToolCapability.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: stdout statuses/issues, failure exit for failing state or validation issues; empty discovery succeeds.
- Later read-back: uninspected — optional provider status write is wired but persistence format and later consumer are unavailable.
- Delegated visibility: provider receives tool list/environment/cadence; operator/CI receives status output and exit code.
- Selection predicate: discovered tools under requested roots, provider validTools, optional cadence, and --write flag.
- Invalidation or expiry: command recomputes provider results; written status replacement/expiry delegated and uninspected.
- Activation or effect: process exit is implemented; CI gating, status persistence and later reuse unobserved.
- Evidence limits: missing plugin predicates/oracles; write failure logging does not enter anyFailing calculation; unverified alone passes exit rule.

> const { validTools, issues } = await validateTools(resolve(targets[0]), allTools)
>     const statuses = await verifyTools(validTools, { cadence: opts.cadence, env, activePlugins, projectRoot: resolve(targets[0]) })
> --- `packages/voiden-runner/src/index.ts`

> upsertToolStatus(status.tool.filePath, status.tool.toolBlockUid, { state: status.state, note: status.note })
> --- `packages/voiden-runner/src/index.ts`

> const anyFailing = statuses.some(s => s.state === 'failing') || issues.length > 0
> --- `packages/voiden-runner/src/index.ts`

> process.exit(anyFailing ? EXIT_RUN_FAILURE : EXIT_SUCCESS)
> --- `packages/voiden-runner/src/index.ts:1808-1820`

### Claims

#### EPI-CLM-request-check
Label: Execute and inspect requests

Distinct claim associated with [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance), not a duplicate of its behavioral-authority path. Installed guide claims request execution and structured inspection can check more than plausible syntax, asks a purpose-fit body check and genuine-result recording. SRC-1, `packages/executors/src/skillContent.ts`, doctrine/design. It is an interactive operator/host checking procedure, not a claim of autonomous general knowledge production. Enforcement and compliance do not follow from prose.

> A request block that merely looks well-formed can still be wrong (bad URL, wrong auth, malformed body). Don't stop at "this looks right" when you can check that it *is* right.
> --- `packages/executors/src/skillContent.ts`

> \`success: true\` — sanity-check the response \`body\` actually matches what the request was supposed to do.
> --- `packages/executors/src/skillContent.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
