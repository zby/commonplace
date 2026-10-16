---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "SoL-Pi epistemic routes: exact evidence selection, operational admission and the limits of evidence-preservation claims."
run-id: AAS-2026-10-14-sol-pi-42f04fbbc6bb-01
reviewed-boundary: "41fa7e0e230bedc5e639aed2e7b9cc5698726db1"
---

# SoL-Pi epistemic report

## Source-and-claim boundary

This report asks what SoL-Pi's evidence-preserving and efficiency mechanisms license the next agent invocation to believe or do. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identities and layers are see [Source register](boundary.md#source-register). The extension and both shipped examples are included. Pi's internal summarizer, foreground model internals, renderers, test frameworks and external research process are not implementations inspected here. No target execution, provider call or test was performed or supplied. Thus source supports architecture, not exercised checking, successful repair, measured savings or causal benefit.

The consequential preservation claims are [EPI-CLM-preserve-evidence](#epi-clm-preserve-evidence) and [EPI-CLM-lossless-reducer](#epi-clm-lossless-reducer). The narrower fusion claim is see [RT-CLM-fusion-roundtrip](runtime.md#rt-clm-fusion-roundtrip). There is no need to interpret this operational extension as promising general scientific knowledge production. The truth-apt objects it transports still require assessment because selected evidence reaches task decisions.

Coverage distinguishes direct reads in this job from supplied findings. All source paths below are SRC-1 at the reviewed commit. Source inspection beyond the boundary's initial list adds reducer validation internals, exact observation projection, transcript clipping/rendering and Visual crop/cache internals. The public registration search covered `registerTool`, `pi.on(` and `registerCommand` under the core extensions and Visual source; CLI operations were accounted for against the supplied launcher account. No additional core command dispatcher was found in that search. This is material-route coverage, not an exhaustive correctness audit.

| Entry point or operation | Source path | Coverage and records / limit |
|---|---|---|
| Configured package loading, direct feature registration | `src/sol-pi/index.ts` | Direct read; [RT-RTE-config-admission](runtime.md#rt-rte-config-admission). File trust is not a universal guard on direct callers. |
| Replaced edit/write, optional command | `src/sol-pi/extensions/action-fusion/index.ts` | Supplied implementation account; [RT-RTE-action-fusion](runtime.md#rt-rte-action-fusion). Command results can be evidence, but arbitrary command semantics are not established. |
| Tool-result reducer: selection, check, fallback and replacement | `src/sol-pi/extensions/evidence-preserving-reducer/index.ts`; `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts`; `src/sol-pi/extensions/evidence-preserving-reducer/config.ts` | Direct reads; [RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt), [EPI-OBJ-validated-receipt](#epi-obj-validated-receipt), [EPI-OBJ-receipt-labels](#epi-obj-receipt-labels). Provider and full-output extraction details also supplied by runtime. |
| Context projection and obs_recall | `src/sol-pi/extensions/observation-pack/index.ts`; `src/sol-pi/extensions/observation-pack/observation.ts` | Registration searched, helper directly read, hook account supplied; [RT-RTE-observation-replay](runtime.md#rt-rte-observation-replay), [EPI-OBJ-observation-text](#epi-obj-observation-text). |
| update_plan; context/provider/input/turn-end/settlement/tree/compact/shutdown hooks | `src/sol-pi/extensions/online-context-compact/extension.ts`; `src/sol-pi/extensions/online-context-compact/tools.ts` | Hook surface searched; supplied [RT-RTE-online-compaction](runtime.md#rt-rte-online-compaction) and [RT-OBJ-online-state](runtime.md#rt-obj-online-state). Native summary semantics not inspected; no fidelity conclusion. |
| Skill launch, detached wait/status/result and host notification | `examples/sol-pi-skill/bin/sol-pi-run` | Supplied [RT-RTE-skill-handoff](runtime.md#rt-rte-skill-handoff). Exit/stop status and final-text extraction are not task acceptance. |
| Host transcript export and trim | `examples/sol-pi-skill/bin/sol-pi-context` | Direct complete read; [EPI-OBJ-exported-context](#epi-obj-exported-context). Host summaries are imported, not newly verified. |
| Visual policy and magnify | `examples/solpi-visual/src/scene/index.ts`; `examples/solpi-visual/src/scene/magnify.py` | Wrapper surface searched, wrapper account supplied, Python helper directly read; [RT-RTE-visual-inspection](runtime.md#rt-rte-visual-inspection), [EPI-OBJ-crop-artifact](#epi-obj-crop-artifact). |
| Evaluator suites and external outcome claims | `tests/pi-package-integration.test.ts`; `README.md` | Test design supplied through boundary; no observed test pass. README preservation claims directly read. Full suite assertions not independently inspected here, preventing a suite-complete evaluation claim. External trajectories and interventions absent from supplied evidence, preventing causal savings or reconstruction-quality conclusions. |

## Epistemic-object inventory

Fields owned by supplied records are see those records; the following identifies operative content distinctions rather than redeclaring their containers.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-observation-text](#epi-obj-observation-text) | Imported tool assertions and quoted file contents, when present | Exact replay/recall | SRC-1, `src/sol-pi/extensions/observation-pack/observation.ts` | Arbitrary text can be non-assertoric; payload truth is not checked by hashing. |
| [EPI-OBJ-validated-receipt](#epi-obj-validated-receipt) | Selected log quotations and source/status metadata | Checked evidence receipt | SRC-1, `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts` | Quote membership and host error flag, not complete diagnosis. |
| [EPI-OBJ-receipt-labels](#epi-obj-receipt-labels) | Kind assignments and uncertainty judgment | Guide the main agent's reading | SRC-1, `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts` | Kind enum and boolean type checked; semantic appropriateness is not. |
| [RT-OBJ-online-state](runtime.md#rt-obj-online-state) | See record; progress assertions alongside symbolic status/statistics | Plan boundary nomination | SRC-1, `src/sol-pi/extensions/online-context-compact/plan.ts` | No task-outcome oracle; successful plan-tool execution is not successful task work. |
| [RT-CMP-frontier-model](runtime.md#rt-cmp-frontier-model) | Not determinable for opaque parameters; external summary may contain task assertions | Foreground judgment/native summary | SRC-1, `src/sol-pi/extensions/online-context-compact/extension.ts` | No fixed weights or inspected summarizer. No separate candidate instance supplied. |
| [RT-CMP-reducer-model](runtime.md#rt-cmp-reducer-model) | Not determinable for opaque parameters; output parts above are inspectable | Evidence selection | SRC-1, `src/sol-pi/extensions/evidence-preserving-reducer/provider.ts` | See record for parameter-change, version and endpoint uncertainty; no training or execution established. |
| [EPI-OBJ-exported-context](#epi-obj-exported-context) | Imported host conversation and summaries | Reference for delegated work | SRC-1, `examples/sol-pi-skill/bin/sol-pi-context` | Lossy, may lose error provenance in Codex outputs; warns to reread files. |
| [RT-RTE-skill-handoff](runtime.md#rt-rte-skill-handoff) | See record for final assistant text and process summary | Parent handback | SRC-1, `examples/sol-pi-skill/bin/sol-pi-run` | Container cited for its output; no semantic verification of final answer. |
| [EPI-OBJ-crop-artifact](#epi-obj-crop-artifact) | Source-derived pixels and coordinate/hash metadata; pixels are inspection evidence rather than a diagnosis | Local visual inspection | SRC-1, `examples/solpi-visual/src/scene/magnify.py` | Interpolation does not reveal hidden geometry. Static receipt flags are not a visual evaluator. |
| [RT-BAP-visual-policy](runtime.md#rt-bap-visual-policy) | See record; workflow directions rather than accepted task claims | Editing/inspection guidance | SRC-1, `examples/solpi-visual/src/scene/policies.ts` | Advisory channel; no outcome-responsive revision shown. |

## Authority-route ledger

Each cited route retains its source-native identity. Linked rows split consequential functions of the same container, not new competing declarations. Where a supplied route owns timing, selection, invalidation or readback details, `see` delegates those fields to it. All statuses below describe inspected or supplied implementation, not observed activation.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-action-fusion](runtime.md#rt-rte-action-fusion) | check/evidence production | implemented | See route for command result | truth-apt transformation: acquisition/import | File state/command behavior in chosen environment | Caller-chosen command and host exit metadata; see route | See route | Text/error returned after mutation | Executes command, not semantic acceptance | Acquires command reports with source warrant unknown; test-specific license not determined | Removes intervening model decision; no rollback on failure | Foreground model, tool result, advisory evidence; shell effects immediate | SRC-1, `src/sol-pi/extensions/action-fusion/then-run.ts` | [RT-CLM-fusion-roundtrip](runtime.md#rt-clm-fusion-roundtrip) | none | A test command can disconfirm a product claim; wrapper alone cannot establish coverage or correctness. |
| [RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt) | content transformation | implemented | [EPI-OBJ-validated-receipt](#epi-obj-validated-receipt) | truth-apt transformation: non-ampliative reshaping | Select quotations from imported log | Model selection; byte/string membership checked later | See route | Smaller candidate receipt | Candidate generation only | Source wording preserved for selected quotes; omissions degrade completeness | Candidate may replace full delivered log after checks | Reducer to admission function, JSON, no force before checks; one result | SRC-1, `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts` | [EPI-CLM-lossless-reducer](#epi-clm-lossless-reducer) | selective-not-lossless | Underlying log assertions remain unverified. |
| [RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt) | content transformation | implemented | [EPI-OBJ-receipt-labels](#epi-obj-receipt-labels) | truth-apt transformation: indeterminate | Kind/uncertainty assignments | Model asked for causal-looking failure signals; semantic judgment uninspected | See route | Labels and boolean | Delivered with admitted quotes | Does not license causal explanation or complete failure accounting | Can steer foreground attention | Foreground model, receipt labels, advisory, following task turns | SRC-1, `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts` | [EPI-CLM-lossless-reducer](#epi-clm-lossless-reducer) | unchecked-semantics | Cannot establish entailment or non-entailment for an absent concrete model output. |
| [RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt) | check/evidence production | implemented | [EPI-OBJ-validated-receipt](#epi-obj-validated-receipt) | no content change | Schema/hash/host status, quote membership, failure-label presence | Deterministic validator over selected body and isError; see route | Before replacement | ok or reason | Check result consumed by replacement branch | Narrow license: selected strings occur and status matches host flag | Invalid candidate cannot reach normal replacement | Admission code, checked return value, enforcing, one tool result | SRC-1, `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts` | [EPI-CLM-preserve-evidence](#epi-clm-preserve-evidence) | none | Matching source hash field is not independent proof that the source is true. |
| [RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt) | disposition/acceptance | implemented | [EPI-OBJ-validated-receipt](#epi-obj-validated-receipt) | no content change | Fitness as smaller evidence projection, not task diagnosis | Software requires successful provider, validator and byte reduction; no per-receipt human veto | See route | Replacement or original | Enforces operational admission | Acceptance criterion is local evidence transport for foreground inspection of this log | Replaces tool body/fused suffix, preserves isError; fallback on ordinary failed checks | Foreground context, tool-result content, enforcing substitution then advisory use, later turns | SRC-1, `src/sol-pi/extensions/evidence-preserving-reducer/index.ts` | [EPI-CLM-preserve-evidence](#epi-clm-preserve-evidence) | narrower-than-task-acceptance | Not acceptance of an ampliative diagnosis; archive errors outside provider catch remain a limit. |
| [RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt) | retention | implemented | [EPI-OBJ-validated-receipt](#epi-obj-validated-receipt) | no content change | Raw log archive and decision journal | Archive integrity and normal write success; see route | Raw archive before provider, journal during decisions | Raw artifact plus pointer/receipt | Retains evidence for optional reread | Preserves selected raw body's lineage, not independent warrant | Explicit shell reads can recover omitted context | Foreground agent via source_artifact, requested readback, advisory, file lifetime | SRC-1, `src/sol-pi/extensions/evidence-preserving-reducer/index.ts` | [EPI-CLM-preserve-evidence](#epi-clm-preserve-evidence) | none | Retention precedes acceptance. It is not lifecycle integration of accepted knowledge. |
| [RT-RTE-observation-replay](runtime.md#rt-rte-observation-replay) | operational admission/selection/consumption | implemented | [EPI-OBJ-observation-text](#epi-obj-observation-text) | truth-apt transformation: non-ampliative reshaping | Which existing text reaches provider invocation | Success/pure-text/size checks and replay counts; see route | See route | Full text, placeholder or requested recall page | Enforced projection; recall is model-selected | Exact stored text available; excerpts do not certify relevance or sufficiency | Omits repeated middle text, allows id/offset reload | Foreground model, context placeholder and obs_recall, enforcing delivery selection/advisory content, future invocations while files/id survive | SRC-1, `src/sol-pi/extensions/observation-pack/observation.ts` | [EPI-CLM-preserve-evidence](#epi-clm-preserve-evidence) | none | Error/image/receipt bypass prevents an all-results packing claim. No automatic reread guarantees omitted evidence is used. |
| [RT-RTE-online-compaction](runtime.md#rt-rte-online-compaction) | check/evidence production | implemented | [RT-OBJ-online-state](runtime.md#rt-obj-online-state) | no content change | Plan transition and estimated compaction economics/window pressure | Deterministic shape/transition/economic checks, not task verification; see route | Successful update_plan boundary then turn end | Candidate selected or skipped | Check feeds compact request | Licenses policy choice under estimates, not completed-task truth | Can abort and compact; native/manual compaction is an alternate path | OCC code, plan/status/usage, enforcing selection, current compaction horizon | SRC-1, `src/sol-pi/extensions/online-context-compact/extension.ts` | none | completion-not-verification | No measured future savings or actual completion established. |
| [RT-RTE-online-compaction](runtime.md#rt-rte-online-compaction) | content transformation | implemented | [RT-CMP-frontier-model](runtime.md#rt-cmp-frontier-model) | truth-apt transformation: indeterminate | Replace accumulated history with native summary/recent tail | Host summarizer; preservation request only; see route | See route | Native compact callback, refusal or error | Requests host transformation; known settlement routes resume | Semantic preservation unestablished: could be reshaping or introduce unsupported claims | Later invocation consumes replacement; generic reminder triggers turn | Pi/foreground model, native context plus hidden continuation, enforcing continuation with advisory summary, later turns | SRC-1, `src/sol-pi/extensions/online-context-compact/extension.ts` | [EPI-CLM-preserve-evidence](#epi-clm-preserve-evidence) | opaque-summary | No independent summary acceptance evaluator inspected; no invented lifecycle integration. |
| [RT-RTE-skill-handoff](runtime.md#rt-rte-skill-handoff) | content transformation | implemented | [EPI-OBJ-exported-context](#epi-obj-exported-context) | truth-apt transformation: acquisition/import | Import host transcript through clipping/filtering | Deterministic exporter and source-host labels | Before delegated invocation; see route | Selected text, summaries and trimmed tool results | Supplies delegate context | Source warrant unknown; context/provenance degraded by omissions | Separate agent acts on limited imported context and shares workspace | Delegated foreground, prompt prefix, advisory reference, task invocation | SRC-1, `examples/sol-pi-skill/bin/sol-pi-context` | none | lossy-handoff | No truth check; Codex tool outputs receive false error flag in export. |
| [RT-RTE-skill-handoff](runtime.md#rt-rte-skill-handoff) | operational admission/selection/consumption | implemented | See route for final text/result | no content change | Subprocess end and parent result delivery | Process/stop status and last assistant text, not task oracle; see route | See route | done/error/timeout and final text | Delivers result, does not enforce patch review | No acceptance of task correctness from done | Parent can continue/check changes; mutations survive failure | Parent agent, host reminder/CLI return, advisory, subsequent parent actions | SRC-1, `examples/sol-pi-skill/bin/sol-pi-run` | none | process-not-product | Host delivery unobserved; final assistant assertions are not verified conclusions. |
| [RT-RTE-visual-inspection](runtime.md#rt-rte-visual-inspection) | content transformation | implemented | [EPI-OBJ-crop-artifact](#epi-obj-crop-artifact) | truth-apt transformation: non-ampliative reshaping | Existing image region and independent reference region | Bounds, file/size/mode checks; conventional interpolation, not visual grading | Model-selected magnify; see route | PNG crops, hashes and receipt or error | Supplies actual image bytes to model | Source-derived visible pixels, not hidden geometry, correctness or causal diagnosis | Enables targeted inspection; scene edits remain separate tools | Foreground model, image/text result, advisory evidence; artifact survives for later reads | SRC-1, `examples/solpi-visual/src/scene/magnify.py` | none | none | Static evaluation_unchanged is not measured external evaluation; reference crop not a software answer oracle. |
| [RT-BAP-visual-policy](runtime.md#rt-bap-visual-policy) | behavior/policy adaptation | implemented | See record for static policy | non-truth-apt policy/content update: append inspection/editing guidance | Model workflow | Prompt interpretation, not code-enforced locality | See record | Appended system policy | Advisory | No new task claim accepted | Requests local edits/crop inspection/foreground waiting | See record | SRC-1, `examples/solpi-visual/src/scene/policies.ts` | none | static-not-learned | Delivery is wired; compliance and evidence-responsive policy revision unobserved. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-preserve-evidence](#epi-clm-preserve-evidence) | See claim | SRC-1, `README.md`; doctrine/design | See claim | [RT-RTE-observation-replay](runtime.md#rt-rte-observation-replay), [RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt), [RT-RTE-online-compaction](runtime.md#rt-rte-online-compaction) | None supplied | No independent intervention; external native compaction and provider behavior remain limits | Exact local archives and ordinary fallback paths are implemented | Availability is conditional on archive lifetime and id/path; preservation of everything needed or actual use is not established. |
| [EPI-CLM-lossless-reducer](#epi-clm-lossless-reducer) | See claim | SRC-1, `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts`; doctrine/design prompt | See claim | [RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt) | None supplied | No semantic-completeness experiment | Lossless selected quotations, not lossless delivered log | Labels and omissions are not semantically checked. |
| [RT-CLM-fusion-roundtrip](runtime.md#rt-clm-fusion-roundtrip) | See claim | SRC-1, `src/sol-pi/extensions/action-fusion/index.ts`; doctrine/design | See claim | [RT-RTE-action-fusion](runtime.md#rt-rte-action-fusion) | None supplied | No measured latency, cost or repair comparison | Implemented direct sequencing for then_run | Not verification equivalence across all arbitrary commands or calls. |

## Bounded conclusion

**SoL-Pi admits evidence projections and execution/compaction choices, not independently warranted task diagnoses.** The reducer has a real evidence-consuming acceptance decision, but its criterion and intended use are narrow: a smaller representation of a selected diagnostic body for the foreground agent, with schema, hash, status and quote-membership constraints. The acceptance branch controls replacement; the foreground model receives retained quotes, labels and archive pointer, not the omitted log automatically. That operational acceptance is not acceptance of a novel causal explanation or a verified pass/fail answer ([RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt), [EPI-OBJ-receipt-labels](#epi-obj-receipt-labels)).

A source-supported counterexample defeats the broader reading. For a failing body containing two different failures, a receipt with one matching quote labelled failure can pass the validator even if the other failure is absent from the receipt; the index also requires net size reduction. This is a deduction from inspected validator/consumer code, not an executed test. Even the kind assignment is not checked against what its quote means. The raw archive preserves a route to omitted context, but availability does not establish later consumption or semantic completeness ([EPI-OBJ-validated-receipt](#epi-obj-validated-receipt)).

ObservationPack preserves raw selected tool text and identity, then supplies only deterministic excerpts until the model requests recall. Hashes license identity, not source truth. An explicit deterministic text witness is `clip('ABCDEFGHIJKL', 6)`: strip leaves twelve characters, head is four, tail is two, so the result is `ABCD`, newline, `[... 6 characters omitted ...]`, newline, `KL`. Render subsequently labels tool output as result/error and may discard older blocks. This is non-ampliative textual omission, not evidence-consuming acceptance. The Codex adapter sets output error flags to false, so the exported result label does not preserve original failure status. Imported transcript warrant is therefore unknown and some provenance is degraded ([EPI-OBJ-exported-context](#epi-obj-exported-context), [EPI-OBJ-observation-text](#epi-obj-observation-text)).

Plan statuses and command exit results have different licenses. A status transition nominates an economic/window-policy decision; it does not verify completed work. A command can supply disconfirming evidence in its own domain, but neither fusion nor a successful process status defines a universal task oracle. Compaction delegates semantic reshaping to an uninspected host summarizer and resumes later behavior without a separate fidelity evaluator in this boundary. Skill's handback similarly reports last assistant text/process state, not accepted task correctness. No supplied artifact establishes an accepted ampliative claim or its lifecycle integration through these routes ([RT-RTE-online-compaction](runtime.md#rt-rte-online-compaction), [RT-RTE-action-fusion](runtime.md#rt-rte-action-fusion), [RT-RTE-skill-handoff](runtime.md#rt-rte-skill-handoff)).

Visual crops preserve a bounded pixel/coordinate lineage through deterministic image processing. They do not determine scene correctness; the consumer is the foreground model. Static visual policy and compaction economic state can shape behavior without producing accepted truth-apt claims. Neither establishes a content-directed criticism/revision loop over the shipped policies. Reducer and foreground parameters remain externally opaque and not revision-pinned; those independent uncertainties do not negate the inspected symbolic checks. No single learning, reflection, autonomy, self-improvement or theory-building verdict follows from the transport and policy routes ([EPI-OBJ-crop-artifact](#epi-obj-crop-artifact), [RT-BAP-visual-policy](runtime.md#rt-bap-visual-policy), [RT-CMP-reducer-model](runtime.md#rt-cmp-reducer-model), [RT-CMP-frontier-model](runtime.md#rt-cmp-frontier-model)).

## Shared records

### Operative objects

#### EPI-OBJ-observation-text
Label: Observation text and projection

Part of: [RT-RTE-observation-replay](runtime.md#rt-rte-observation-replay)

The object is a material payload part of that supplied route, not a duplicate route. Source-native `Observation.text`, filePath and placeholder: natural-language tool text with symbolic id/hash/size/offset metadata; UTF-8 local files and transient projected messages. The helper joins multiple text blocks with newline, archives the resulting string, and selects complete head/tail lines. It preserves that assembled payload, not original block boundaries or the truth of its assertions. SRC-1, implementation, `src/sol-pi/extensions/observation-pack/observation.ts`.

> return (message.content as TextContent[]).map((block) => block.text).join("\n");
> --- `src/sol-pi/extensions/observation-pack/observation.ts`

> if (hash(existingContent) !== observation.contentHash) {
> --- `src/sol-pi/extensions/observation-pack/observation.ts`

> `[middle omitted; last complete lines, up to ${tailBudget} bytes]`,
> --- `src/sol-pi/extensions/observation-pack/observation.ts`

#### EPI-OBJ-validated-receipt
Label: Validated receipt quotations and metadata

Part of: [RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt)

A material object part, not another declaration of the supplied admission route. Source-native `ValidatedReceipt.evidence` quotes and receiptText source/status metadata: natural-language quotations nested in symbolic JSON/text fields; provider output and returned tool message, with raw body in the local archive. Labels/uncertainty have a distinct check domain and are split below. SRC-1, implementation, `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts` and `src/sol-pi/extensions/evidence-preserving-reducer/index.ts`.

> !body.includes(quote)
> --- `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts`

> isError &&
> FAILURE_SIGNAL.test(body) &&
> !evidence.some((item) => item.kind === "fatal" || item.kind === "failure")
> --- `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts`

> if (receiptBytes >= archive.bytes) {
> --- `src/sol-pi/extensions/evidence-preserving-reducer/index.ts`

> content: reducible.projectReceipt(receipt),
> isError: event.isError,
> --- `src/sol-pi/extensions/evidence-preserving-reducer/index.ts`

These checks support membership/status/size acceptance for the stated projection use. The validator's loop tests each submitted item, not every failure in the body. In the same code, `expectedStatus` follows isError, so success means agreement with the host flag, not verified task correctness. Exact quotation does not independently validate the log's propositions.

#### EPI-OBJ-receipt-labels
Label: Receipt kind and uncertainty judgments

Part of: [RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt)

Distinct material output fields from the quotations above. Source-native `EvidenceKind` and `ValidatedReceipt.uncertain`: symbolic enums/boolean in JSON and rendered text, interpreted as natural-language evidence categories by the foreground agent. Storage is provider response/receipt. The label's membership in an allowed enum is checked, but correspondence between its meaning and quote content is not. The model proposes, software admits shape, and no per-content human semantic veto is implemented. Exact claim relation is indeterminate without a concrete candidate output. SRC-1, implementation and prompt doctrine, `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts`.

> typeof parsed.uncertain !== "boolean" ||
> --- `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts`

> !allowedKinds.has(kind as EvidenceKind) ||
> --- `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts`

> "Set uncertain=true when the log is ambiguous or lacks a clear failure signal.",
> --- `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts`

#### EPI-OBJ-exported-context
Label: Exported host transcript

Part of: [RT-RTE-skill-handoff](runtime.md#rt-rte-skill-handoff)

Material input object of the supplied handoff, distinct from its process/result machinery. Source-native rendered transcript prefix: natural-language messages and summaries plus symbolic tool-call/result labels, on disk/stdout and then in the delegated prompt. Direct inspection covers both host adapters, clipping, current-handoff removal and recent-block selection. No supplied counterpart object declaration exists. SRC-1, implementation, `examples/sol-pi-skill/bin/sol-pi-context`.

> head = limit * 2 // 3
> tail = limit - head
> return f'{text[:head]}\n[... {len(text) - limit} characters omitted ...]\n{text[-tail:]}'
> --- `examples/sol-pi-skill/bin/sol-pi-context`

> events.append(('tool_result', clip(out or '', tool_chars), False))
> --- `examples/sol-pi-skill/bin/sol-pi-context`

> if total + len(block) > max_chars and kept:
>     break
> --- `examples/sol-pi-skill/bin/sol-pi-context`

The last clause preserves at least one most-recent block even when it exceeds the budget. Transcript selection and format changes cannot establish source truth. The false error flag in the Codex adapter warrants the local provenance qualification; it does not say all host errors are concealed in their textual bodies.

#### EPI-OBJ-crop-artifact
Label: Magnify crop and receipt

Part of: [RT-RTE-visual-inspection](runtime.md#rt-rte-visual-inspection)

Material object part of the supplied tool route, not a duplicate implementation route. Source-native `crop`, `reference_crop`, `RECEIPT.json`: pixel raster evidence plus symbolic source hashes, bbox, interpolation and coordinate mapping; PNG/JSON under content-addressed output root, returned as image/text blocks by the supplied wrapper account. This adds direct helper inspection where runtime left it uninspected, without contradicting its bounded wrapper findings. SRC-1, implementation, `examples/solpi-visual/src/scene/magnify.py`.

> crop=im.crop(bbox)
> if crop.size!=(ow,oh):crop=crop.resize((ow,oh),resample=getattr(Image.Resampling,method.upper()))
> --- `examples/solpi-visual/src/scene/magnify.py`

> if (target/'RECEIPT.json').read_bytes()!=encoded or any(digest((target/(k+'.png')).read_bytes())!=v[1]['output_sha256'] for k,v in assets.items()):raise ValueError('Existing artifact differs; refusing overwrite')
> --- `examples/solpi-visual/src/scene/magnify.py`

The helper reads bytes, applies EXIF orientation, bounds checks, crops and conventionally resamples. It recomputes identity from current inputs/tool and checks existing receipt/output hashes before reuse. Source equality is sampled again for receipt metadata; not a durable lock. This supports provenance/reuse guards, not an independent check of scene match or hidden geometry. No semantic evaluator is invented for this intentionally operational image tool.

### Claims

#### EPI-CLM-preserve-evidence
Label: Preserve evidence while reducing work

Distinct from [RT-CLM-fusion-roundtrip](runtime.md#rt-clm-fusion-roundtrip): this is the README's consequential preservation promise across mechanisms, not only sequencing. SRC-1, doctrine/design, `README.md`.

> - **Preserve evidence.** Original observations remain available locally, and reducer failures leave the original result unchanged.
> --- `README.md`

The archive and ordinary provider/validation fallback implementations support a scoped reading. They do not establish indefinite availability, automatic reread, native-summary fidelity or semantic adequacy of the selected evidence. See supplied runtime limits for archive errors outside the provider catch and no-session cleanup policy.

#### EPI-CLM-lossless-reducer
Label: Lossless output reducer

Distinct narrower prompt claim with no supplied claim counterpart; overlaps [EPI-CLM-preserve-evidence](#epi-clm-preserve-evidence) in intended preservation, not identity. SRC-1, doctrine/design in executable prompt construction, `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts`.

> "You are a lossless test/build output reducer.",
> --- `src/sol-pi/extensions/evidence-preserving-reducer/receipt.ts`

Selected quotes are literal, but the delivered receipt omits text. Lossless semantic coverage is not enforced by membership, allowed categories or at-least-one-failure evidence. The archive route preserves access to the selected source body separately from what reaches the foreground model.
