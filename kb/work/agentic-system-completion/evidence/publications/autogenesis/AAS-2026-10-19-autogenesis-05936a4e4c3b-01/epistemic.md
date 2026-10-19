---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Autogenesis epistemic routes: candidate generation, memory compaction, corpus reuse, evaluators and capability reliance."
run-id: AAS-2026-10-19-autogenesis-05936a4e4c3b-01
reviewed-boundary: "5b070d5cd497e951a188a01409138e8b530eaf4a"
---

# Autogenesis epistemic report

## Source-and-claim boundary

The question is how Autogenesis generates or acquires truth-apt content, checks it, grants reliance and lets it affect later behavior. The [boundary Source register](boundary.md#source-register) supplies SRC-1 and its frozen revision. This is a source-only assessment of the enclosing runtime, including its improvement plane, shipped drivers and clients. Excluded dependencies, gitlink internals and remote services remain excluded. No execution or comparison evidence was supplied; no target code was executed. Implementation supports capacities, not observed compliance, reliability or benefit.

The supplied runtime is provisional. Its main dispatch and admission account is retained, but direct inspection adds corpus operations, deterministic processors, benchmark scoring, version-scoped workflow evaluations and compaction. In particular, workflow evaluation has stronger provenance checks than generic model evaluation or smoke. This is an added material part, not a contradiction of the runtime's explicitly incomplete coverage. Public evolution and approval claims are in [RT-CLM-evolution-guidance](runtime.md#rt-clm-evolution-guidance). The memory evaluator's narrower quality claim is [EPI-CLM-memory-rubric](#epi-clm-memory-rubric).

| Entry point or operation | Source path in SRC-1 | Coverage and evidence basis |
|---|---|---|
| Console command / TUI / serve | `autogenesis/cli.py` | Direct read of TerminalClient dispatch; supplied [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task) covers Gateway task loop. Console command success means dispatch success, not answer truth. |
| Task model, child and direct driver | `autogenesis/agent/types.py`, `autogenesis/protocol/server.py`, `examples/run_general_agent.py` | Supplied [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task), [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation), [RT-RTE-direct-agent](runtime.md#rt-rte-direct-agent); not independently reread end to end. |
| Direct model chat / ProceduralAgent | `autogenesis/gateway/service.py`, `autogenesis/agent/types.py` | Supplied [RT-RTE-model-chat](runtime.md#rt-rte-model-chat); procedures cannot inherit a universal model-review gate. |
| Registered skill transformation | `autogenesis/skill/context.py` | Supplied [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery), including exact replacement expression; concrete deduction below. |
| Registration hooks, smoke, rollback, unload | `autogenesis/extension/server.py`, `autogenesis/tool/default/evolution.py`, `autogenesis/memory/context.py`, `autogenesis/hook/default/memory.py`, `autogenesis/agent/types.py` | Direct rejection-consumer and tool-operation reads; correction directly rechecks class-based memory registration and instance-guarded event/context consumers. Supplied [RT-RTE-extension-admission](runtime.md#rt-rte-extension-admission) and peer fragment [MEM-RTE-memory-admission](memory.md#mem-rte-memory-admission) preserve the missing-live-instance exception. Other registration hooks not each independently read. |
| Trace compaction and prompt read-back | `autogenesis/memory/default/tiered.py`, `autogenesis/hook/default/compact.py`, `autogenesis/memory/default/general_memory_system.py` | Direct reads of get, compaction, todos and JSON renderer; [EPI-RTE-history-compact](#epi-rte-history-compact), [EPI-RTE-summary-retain](#epi-rte-summary-retain). |
| Corpus ingest / retrieve | `autogenesis/knowledge/server.py`, `autogenesis/knowledge/default/rankers.py` | Direct complete reads; [EPI-RTE-corpus-ingest](#epi-rte-corpus-ingest), [EPI-RTE-corpus-retrieve](#epi-rte-corpus-retrieve). |
| Canvas / workflow processor and benchmark branches | `autogenesis/workflow/runtime.py`, `autogenesis/process/default/text.py`, `autogenesis/benchmark/server.py`, `autogenesis/benchmark/default/exact_match.py` | Direct dispatch and complete text-processor/exact-match reads; [EPI-RTE-json-parse](#epi-rte-json-parse), [EPI-RTE-exact-match](#epi-rte-exact-match); remaining graph traversal supplied by [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution). |
| Workflow evaluation recording / summary | `autogenesis/tool/default/evolution.py`, `autogenesis/workflow/context.py` | Direct operation and validation/summary reads; [EPI-RTE-workflow-evaluation](#epi-rte-workflow-evaluation). |
| Memory evaluator | `autogenesis/agent/evaluator/memory_evaluate_agent.py`, `autogenesis/prompt/default/memory_evaluate_agent.html`, `configs/agents/memory_evaluate_agent.py`, `autogenesis/memory/types.py` | Direct class, prompt, configuration and type reads; [EPI-RTE-memory-evaluate](#epi-rte-memory-evaluate). |
| Remaining evaluator classes, reviewer, benchmark domains, environments, data/plugin/web ingestion and domain skills | `autogenesis/agent/evaluator/`, `autogenesis/benchmark/default/`, `autogenesis/environment/`, `autogenesis/data/`, `autogenesis/plugins/`, `autogenesis/tool/default/` | Available but not fully inspected. Source-path discovery is not evaluator assessment. Prevents a system-complete negative about external checking, accepted knowledge or all acquisition transformations. |
| Other memory backends, provider internals and deployed model state | `autogenesis/memory/`, `autogenesis/model/` | Backend alternatives not exhaustively inspected; provider limits see [RT-CMP-model-manager](runtime.md#rt-cmp-model-manager). Prevents universal memory and parametric-learning verdicts. |

No supplied episode individuates a generated factual proposition and its premises. Thus non-entailment of a particular model output, its acceptance, and later activation are not determinable. Missing traces prevent an observed generation-to-acceptance-to-integration chain. Missing comparisons prevent causal attribution of improvement. Available but unread domain evaluators additionally prevent a complete negative about all system routes; they are not access gaps.

## Epistemic-object inventory

The content field names a candidate class, not an observed candidate. Identity/form/substrate and other owned fields are in the cited records.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-response](#epi-obj-response) | Task answers, evaluations or chat assertions; actual proposition not determinable | see record | SRC-1; see record | A task or method can also be non-truth-apt; no observed output |
| [EPI-OBJ-working-memory](#epi-obj-working-memory) | Execution-history claims in generated summaries | see record | SRC-1 `autogenesis/memory/default/tiered.py` | Summary fidelity not checked by consumer |
| [EPI-OBJ-corpus](#epi-obj-corpus) | Caller-supplied document assertions | see record | SRC-1 `autogenesis/knowledge/server.py` | Document authorship and warrant unknown |
| [EPI-OBJ-evaluation](#epi-obj-evaluation) | Prediction/reference equality and workflow success/quality claims | see record | SRC-1; see record | Distinct checks split by route; quality remains caller-supplied |
| [RT-OBJ-skill-content](runtime.md#rt-obj-skill-content) | Method assertions where truth-apt; otherwise policy | see record | SRC-1; see record | Returned instruction is not acceptance |
| [RT-OBJ-extension-manifest](runtime.md#rt-obj-extension-manifest) | Version/load identity, not a quality certificate | see record | SRC-1; see record | Active source may mix symbolic behavior and method assertions |
| [EPI-OBJ-checkpoint](#epi-obj-checkpoint) | Executable identity and completed-invocation state | see record | SRC-1; see record | Recovery evidence, not factual-output certification |

## Authority-route ledger

Each field owned by a canonical record says see. Architectural status and content relation are this overlay's assessments. All implemented rows are unobserved in operation.

Route ID: [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task)
Route function: content transformation
Architectural status: implemented

Object/candidate ID: [EPI-OBJ-response](#epi-obj-response).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: Task-answer assertions, when present.
Evaluator/condition and domain: Configured model under task and context; no general independent answer oracle.
Activation and timing: Each decision / explicit done or termination.
Possible or observed result: Answer, tool proposals, errors or incomplete response; possible, not observed.
Implemented force: Model output and dispatch; see record.
Epistemic authority and scope: Candidate only; neither fluency nor success licenses factual truth.
Operational authority: Proposes actions and completion; code may block dispatch.
Behavioral-authority path: See [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task).
Evidence source ID and local anchor: SRC-1; see [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task).
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: No concrete proposition/premise pair; could import, reshape, derive or conjecture. Requires output and inputs to distinguish.

Route ID: [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery)
Route function: content transformation
Architectural status: implemented

Object/candidate ID: [RT-OBJ-skill-content](runtime.md#rt-obj-skill-content).
Content/update relation: truth-apt transformation: non-ampliative reshaping.
Transition or check target: Registered instruction body and script paths.
Evaluator/condition and domain: Fixed string replacement; not an epistemic evaluator.
Activation and timing: On selected skill call.
Possible or observed result: Body with absolute script prefix and resource listings; possible, not observed.
Implemented force: Advisory method text.
Epistemic authority and scope: No new factual warrant from the replacement.
Operational authority: Calling model can follow returned method.
Behavioral-authority path: See [RT-BAP-method-instructions](runtime.md#rt-bap-method-instructions).
Evidence source ID and local anchor: SRC-1; see [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery).
Claim IDs or none: [RT-CLM-evolution-guidance](runtime.md#rt-clm-evolution-guidance).
Mismatch marker or none: none.
Gap/limit: For skill_dir=/opt/s, literal input `python scripts/check.py` becomes `python /opt/s/scripts/check.py`. This implementation-layer deduction uses the supplied exact replace expression, not target execution. Resource append is inventory, not truth-checking.

Route ID: [EPI-RTE-history-compact](#epi-rte-history-compact)
Route function: content transformation
Architectural status: implemented

Object/candidate ID: [EPI-OBJ-working-memory](#epi-obj-working-memory).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: Formatted execution records and previous summary.
Evaluator/condition and domain: LLM instructed to preserve exact values; no fidelity comparator.
Activation and timing: Overflow recent_max; compact chunk.
Possible or observed result: Summary text or no output; possible, not observed.
Implemented force: Advisory text once retained.
Epistemic authority and scope: Requested compression is not established semantic preservation.
Operational authority: Creates candidate replacement for prompt history.
Behavioral-authority path: See record.
Evidence source ID and local anchor: SRC-1; see [EPI-RTE-history-compact](#epi-rte-history-compact).
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: No actual source/summary pair. Non-ampliative reshaping, entailed derivation and added conjecture remain unresolved; loss of source warrant possible.

Route ID: [EPI-RTE-summary-retain](#epi-rte-summary-retain)
Route function: retention
Architectural status: implemented

Object/candidate ID: [EPI-OBJ-working-memory](#epi-obj-working-memory).
Content/update relation: no content change.
Transition or check target: Nonempty compact output versus empty output.
Evaluator/condition and domain: Code tests text presence, not factual adequacy.
Activation and timing: After compaction returns.
Possible or observed result: Append summary or restore chunk on empty return; possible, not observed.
Implemented force: Enforcing memory selection.
Epistemic authority and scope: Nonemptiness licenses storage, not acceptance for truth.
Operational authority: Drops compacted raw chunk, keeps bounded summaries and later selected tail.
Behavioral-authority path: See record.
Evidence source ID and local anchor: SRC-1; see [EPI-RTE-summary-retain](#epi-rte-summary-retain).
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Separate from lifecycle integration; no evidence-consuming epistemic acceptance decision in this consumer.

Route ID: [EPI-RTE-corpus-ingest](#epi-rte-corpus-ingest)
Route function: retention
Architectural status: implemented

Object/candidate ID: [EPI-OBJ-corpus](#epi-obj-corpus).
Content/update relation: truth-apt transformation: acquisition/import.
Transition or check target: Caller documents and valid named RAG backend.
Evaluator/condition and domain: Code normalization, backend/name and I/O checks.
Activation and timing: Explicit knowledge_ingest call.
Possible or observed result: Appended documents, manifest or failure; possible, not observed.
Implemented force: Enforcing corpus admission.
Epistemic authority and scope: Source warrant unknown; fields preserved but provenance not required.
Operational authority: Makes documents available for later retrieval.
Behavioral-authority path: See record.
Evidence source ID and local anchor: SRC-1; see [EPI-RTE-corpus-ingest](#epi-rte-corpus-ingest).
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Storage admission is not factual acceptance or post-acceptance integration.

Route ID: [EPI-RTE-corpus-retrieve](#epi-rte-corpus-retrieve)
Route function: operational admission/selection/consumption
Architectural status: implemented

Object/candidate ID: [EPI-OBJ-corpus](#epi-obj-corpus).
Content/update relation: no content change.
Transition or check target: Query/document lexical relevance.
Evaluator/condition and domain: BM25 or TF-IDF similarity; scores concern retrieval, not truth.
Activation and timing: Named base and nonempty query.
Possible or observed result: Top-k document records with score; possible, not observed.
Implemented force: Ranking.
Epistemic authority and scope: No endorsement from relevance; source warrant stays unknown.
Operational authority: Selects corpus material for downstream workflow use.
Behavioral-authority path: See record.
Evidence source ID and local anchor: SRC-1; see [EPI-RTE-corpus-retrieve](#epi-rte-corpus-retrieve).
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Metadata score is overwritten by retrieval score; document text is carried through. No checked downstream factual reliance observed.

Route ID: [EPI-RTE-json-parse](#epi-rte-json-parse)
Route function: content transformation
Architectural status: implemented

Object/candidate ID: [EPI-OBJ-response](#epi-obj-response).
Content/update relation: truth-apt transformation: non-ampliative reshaping.
Transition or check target: JSON encoding of caller assertions.
Evaluator/condition and domain: json.loads parser; syntax domain only.
Activation and timing: Explicit parse_json processor.
Possible or observed result: Parsed value and records or syntax failure; possible, not observed.
Implemented force: Enforcing syntax output.
Epistemic authority and scope: Preserves encoded assertion, not its world truth.
Operational authority: Provides structured fields to downstream graph.
Behavioral-authority path: See record.
Evidence source ID and local anchor: SRC-1; see [EPI-RTE-json-parse](#epi-rte-json-parse).
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Input `{"temperature":20}` yields value {temperature:20}, records containing that dictionary and count 1. Deduction from inspected implementation; unit, measurement and truth unvalidated.

Route ID: [EPI-RTE-exact-match](#epi-rte-exact-match)
Route function: check/evidence production
Architectural status: implemented

Object/candidate ID: [EPI-OBJ-evaluation](#epi-obj-evaluation).
Content/update relation: truth-apt transformation: entailed derivation.
Transition or check target: Supplied prediction/reference pairs, with task_id for batch manager.
Evaluator/condition and domain: Numeric difference below 1e-9 or exact stripped string equality.
Activation and timing: Benchmark step or manager batch evaluation.
Possible or observed result: Per-task score and average; possible, not observed.
Implemented force: Evidence output, not mandatory capability veto.
Epistemic authority and scope: Conditional equality to supplied reference in this comparison domain.
Operational authority: Workflow receives score/count; no automatic keep/rollback in this branch.
Behavioral-authority path: See record.
Evidence source ID and local anchor: SRC-1; see [EPI-RTE-exact-match](#epi-rte-exact-match).
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Reference correctness and process quality not established; workflow Response.success=True even when score=0.

Route ID: [EPI-RTE-workflow-evaluation](#epi-rte-workflow-evaluation)
Route function: disposition/acceptance
Architectural status: implemented

Object/candidate ID: [EPI-OBJ-evaluation](#epi-obj-evaluation).
Content/update relation: no content change.
Transition or check target: Version-scoped evaluation record for retained terminal workflow run, or static failure case.
Evaluator/condition and domain: Code matches run identity/hash/state/success; rejects duplicate run evidence.
Activation and timing: record_workflow_evaluation call before persistence.
Possible or observed result: Validated record or exception; possible, not observed.
Implemented force: Enforcing evidence admission.
Epistemic authority and scope: Accepts provenance/terminal-status consistency for evaluation ledger use, not task-domain quality.
Operational authority: Permits persistence and summary only after guards.
Behavioral-authority path: See record.
Evidence source ID and local anchor: SRC-1; see [EPI-RTE-workflow-evaluation](#epi-rte-workflow-evaluation).
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Quality_score is caller-supplied. Human authorship and domain oracle not established.

Route ID: [EPI-RTE-workflow-evaluation](#epi-rte-workflow-evaluation)
Route function: check/evidence production
Architectural status: implemented

Object/candidate ID: [EPI-OBJ-evaluation](#epi-obj-evaluation).
Content/update relation: truth-apt transformation: entailed derivation.
Transition or check target: Current-version recorded success rate, quality average and case count.
Evaluator/condition and domain: Code thresholds: >=3 distinct cases, >=0.8 success rate, >=0.7 average quality.
Activation and timing: evaluation_summary request following recording or independently.
Possible or observed result: Healthy boolean and aggregates; possible, not observed.
Implemented force: Advisory keep/optimize/rollback signal.
Epistemic authority and scope: Arithmetic over accepted record fields, not independent quality warrant.
Operational authority: Returns summary to tool caller; no automatic rollback in inspected consumer.
Behavioral-authority path: See record.
Evidence source ID and local anchor: SRC-1; see [EPI-RTE-workflow-evaluation](#epi-rte-workflow-evaluation).
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Repeated labels can affect case count; different cases are not controlled comparison or causal intervention.

Route ID: [EPI-RTE-memory-evaluate](#epi-rte-memory-evaluate)
Route function: check/evidence production
Architectural status: implemented

Object/candidate ID: [EPI-OBJ-response](#epi-obj-response).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: Memory implementation quality in five rubric dimensions.
Evaluator/condition and domain: Model-directed source/registry/probe assessment; rubric supplied as text.
Activation and timing: When evaluator agent is selected.
Possible or observed result: Scored report or partial/critical-failure report; possible, not observed.
Implemented force: Advisory response to caller.
Epistemic authority and scope: Report is candidate assessment, not independently validated judgment.
Operational authority: Caller may use report; no automatic admission veto in evaluator class.
Behavioral-authority path: See record.
Evidence source ID and local anchor: SRC-1; see [EPI-RTE-memory-evaluate](#epi-rte-memory-evaluate).
Claim IDs or none: [EPI-CLM-memory-rubric](#epi-clm-memory-rubric).
Mismatch marker or none: rubric/implementation mismatch.
Gap/limit: Prompt describes get_state and action API while inspected TieredMemory uses get/record. No observed evaluator output; fidelity and score validity unestablished.

Route ID: [RT-RTE-extension-admission](runtime.md#rt-rte-extension-admission)
Route function: check/evidence production
Architectural status: implemented

Object/candidate ID: [RT-OBJ-extension-manifest](runtime.md#rt-obj-extension-manifest).
Content/update relation: no content change.
Transition or check target: Generic general_agent response after new component live-load.
Evaluator/condition and domain: Smoke uses response.success and stopped_by_constraint, not changed-component correctness.
Activation and timing: Default post-load smoke unless disabled.
Possible or observed result: ReplayReport ok/failure; possible, not observed.
Implemented force: Result consumed by recovery; see next row.
Epistemic authority and scope: License only generic response completion under probe, not quality of changed artifact.
Operational authority: Supplies pass/fail to extension manager.
Behavioral-authority path: See [RT-RTE-extension-admission](runtime.md#rt-rte-extension-admission).
Evidence source ID and local anchor: SRC-1; see [RT-RTE-extension-admission](runtime.md#rt-rte-extension-admission).
Claim IDs or none: [RT-CLM-evolution-guidance](runtime.md#rt-clm-evolution-guidance).
Mismatch marker or none: quality/approval overreach.
Gap/limit: Not forced to invoke changed component or compare OK text; model alias/provider uninspected.

Route ID: [RT-RTE-extension-admission](runtime.md#rt-rte-extension-admission)
Route function: disposition/acceptance
Architectural status: implemented

Object/candidate ID: [RT-OBJ-extension-manifest](runtime.md#rt-obj-extension-manifest).
Content/update relation: no content change.
Transition or check target: Keep new registration versus revert/unload.
Evaluator/condition and domain: Extension manager consumes report.ok; software can veto after load.
Activation and timing: After smoke when enabled.
Possible or observed result: Keep; previous version restore; unload; recovery error; possible, not observed.
Implemented force: Enforcing registration disposition.
Epistemic authority and scope: Operational admission, not evidence-consuming acceptance of factual claims.
Operational authority: Changes future dispatch availability for supported live consumers; memory-class registration can retain configuration/source without a live instance. Cannot undo arbitrary external effects.
Behavioral-authority path: See [RT-BAP-capability-load](runtime.md#rt-bap-capability-load).
Evidence source ID and local anchor: SRC-1; see [RT-RTE-extension-admission](runtime.md#rt-rte-extension-admission).
Claim IDs or none: [RT-CLM-evolution-guidance](runtime.md#rt-clm-evolution-guidance).
Mismatch marker or none: no mandatory human veto.
Gap/limit: Explicit false and restore bypass smoke. Executed import precedes check. These countercases defeat a universal validated-before-live claim.

Route ID: [RT-RTE-extension-admission](runtime.md#rt-rte-extension-admission)
Route function: behavior/policy adaptation
Architectural status: implemented

Object/candidate ID: [RT-OBJ-extension-manifest](runtime.md#rt-obj-extension-manifest).
Content/update relation: non-truth-apt policy/content update: capability machinery or method replacement.
Transition or check target: Registered source/instructions and module-specific live-consumer availability.
Evaluator/condition and domain: Generator/software admission; evaluator-guided revision requested but not universally enforced.
Activation and timing: Successful finalization or explicit promotion/restore.
Possible or observed result: New future callable set/source for supported modules; memory-class branch can retain source/configuration with instance=None; possible, not observed.
Implemented force: Executable dispatch or model instruction supply for live consumers; memory-class admission alone supplies neither event retention nor context delivery.
Epistemic authority and scope: Operational authority does not certify an explanatory mechanism.
Operational authority: Future invocation can use active tools, agents, workflows or instructions. The memory-class branch requires an additional build or supplied-instance path before lifecycle hooks and prompt reads can use it.
Behavioral-authority path: See [RT-BAP-capability-load](runtime.md#rt-bap-capability-load).
Evidence source ID and local anchor: SRC-1; see [RT-RTE-extension-admission](runtime.md#rt-rte-extension-admission).
Claim IDs or none: [RT-CLM-evolution-guidance](runtime.md#rt-clm-evolution-guidance).
Mismatch marker or none: none.
Gap/limit: Generated source can include factual assertions, but route-level factual update is indeterminate without actual artifact; no later activation trace. [MEM-RTE-memory-admission](memory.md#mem-rte-memory-admission) identifies the memory-class exception: import/constructor effects and archive/manifest retention do not complete a path to later context delivery. Separate build and instance registration prevent a blanket inert-memory conclusion.

Route ID: [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution)
Route function: lineage/freshness/recovery
Architectural status: implemented

Object/candidate ID: [EPI-OBJ-checkpoint](#epi-obj-checkpoint).
Content/update relation: no content change.
Transition or check target: Runtime-major and workflow name/version compatibility; executable identity only when a prior nonempty program hash is present, not factual outputs.
Evaluator/condition and domain: Code rejects runtime-major/name/version mismatch and unequal nonempty program hashes. A missing/empty hash is stamped with the current definition's hash after legacy checks.
Activation and timing: Resume request.
Possible or observed result: Reject mismatch or reuse completed invocations as cached in either accepted branch; possible, not observed.
Implemented force: Enforcing resume admission with a supported hashless migration path.
Epistemic authority and scope: Nonempty matching hash supports executable-contract consistency; hashless migration supports only the legacy compatibility checks, not the original executable identity. Neither establishes replay safety or output truth.
Operational authority: Permits continuation/cache reuse after those checks, including hashless checkpoints whose original executable identity was not verified.
Behavioral-authority path: See [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution).
Evidence source ID and local anchor: SRC-1; see [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution).
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Not lifecycle integration of accepted knowledge; external effects and input freshness require separate evidence. Stamping a current hash does not retroactively verify the executable that produced cached completed work.

Route ID: [RT-RTE-model-chat](runtime.md#rt-rte-model-chat)
Route function: content transformation
Architectural status: implemented

Object/candidate ID: [EPI-OBJ-response](#epi-obj-response).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: Caller chat assertions and generated answer.
Evaluator/condition and domain: Selected remote model; no independent general oracle.
Activation and timing: Direct model.chat request.
Possible or observed result: Text/thinking/done/error events; possible, not observed.
Implemented force: Output delivery only.
Epistemic authority and scope: Candidate assertion when truth-apt.
Operational authority: Streams answer without agent review or done_tool gate.
Behavioral-authority path: See [RT-RTE-model-chat](runtime.md#rt-rte-model-chat).
Evidence source ID and local anchor: SRC-1; see [RT-RTE-model-chat](runtime.md#rt-rte-model-chat).
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Provider state is opaque; cannot equate this path with ordinary agent controls.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source / evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-evolution-guidance](runtime.md#rt-clm-evolution-guidance) | see record | SRC-1; see record; doctrine/design | see record | [RT-RTE-extension-admission](runtime.md#rt-rte-extension-admission), [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery) | None supplied | No interventions; generic smoke cannot identify component effect | Improvement-directed self-change capacity; evaluator and comparison steps requested | Prompt approval and playbook staging language conflict with implemented routes; skill type filter limits ordinary delivery |
| [EPI-CLM-memory-rubric](#epi-clm-memory-rubric) | see record | SRC-1; see record; doctrine/design | see record | [EPI-RTE-memory-evaluate](#epi-rte-memory-evaluate) | None supplied | No score validity or outcome comparison; rubric partly describes a different API | Model-driven assessment/report capacity, not a reliable truth or functionality oracle | No universal evaluator-approval transaction; invalid rubric assumptions can mis-score valid memory implementations |

## Bounded conclusion

Autogenesis supports candidate answer generation and imported-content reuse, but does not receive epistemic warrant from task completion flags. [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task) explicitly includes a MetaAgent no-progress countercase where done is true despite incompleteness. Direct chat has still fewer agent gates. Specific generated factual novelty, acceptance and integration are not determinable without a proposition-bearing artifact and its linked inputs/checks. This is not a system-wide absence verdict.

The strongest directly inspected narrow derivations are parser output, reference-equality scores and workflow-evaluation aggregates. [EPI-RTE-json-parse](#epi-rte-json-parse) and the skill replacement deduction establish syntax/format changes, not new world knowledge. [EPI-RTE-exact-match](#epi-rte-exact-match) establishes a comparison result conditional on caller references, not source truth, answer-producing mechanism or transfer. There are no warranted real-world premises supplied from which this report can infer a newly accepted domain proposition.

[EPI-RTE-corpus-ingest](#epi-rte-corpus-ingest) retains acquired documents without required provenance or truth approval; [EPI-RTE-corpus-retrieve](#epi-rte-corpus-retrieve) ranks them lexically and delivers selected records. Source warrant is unknown, not repaired by a high score. [EPI-RTE-history-compact](#epi-rte-history-compact) asks a model to summarize trace records; [EPI-RTE-summary-retain](#epi-rte-summary-retain) grants nonempty output prompt authority without checking semantic fidelity. Selected summaries can affect future model input; actual behavioral activation and benefit remain unobserved. Keeping memory is distinct from accepting and integrating knowledge.

[EPI-RTE-workflow-evaluation](#epi-rte-workflow-evaluation) is an important countercase to a blanket no-check account. It admits evaluation records only after version/run/hash/terminal-status checks, requires real runs for successes, and rejects duplicate run evidence. The acceptance criterion is evidence-record consistency; intended use is the current-version evaluation ledger and summary; scope excludes the substantive quality score's truth. Its enforcing channel controls ledger admission; the resulting healthy flag is advisory to the tool caller. No automatic policy selection or rollback consumer was found in this inspected operation. Acceptance of a record for bookkeeping is not acceptance of an ampliative claim for domain reliance.

Capability loading has a real future behavioral-authority path for supported live consumers such as tools, agents and workflows through active managers, schemas and executable invocation ([RT-BAP-capability-load](runtime.md#rt-bap-capability-load)). Memory-class extension registration is a material exception: it stores instance=None, so lifecycle event hooks and agent prompt reads skip it until a separate build or supplied-instance path provides a live instance ([MEM-RTE-memory-admission](memory.md#mem-rte-memory-admission)). Its source/configuration retention and import/constructor effects do not establish later context delivery or live session restoration. This exception does not erase the other capability paths or separate live-memory paths; later activation remains unobserved. Smoke rejection can revert/unload; it is post-load and optional, and its evaluator licenses generic response completion only. The prescribed scored reviews and with/baseline probes are not established as mandatory gates. Method text supplies advisory authority ([RT-BAP-method-instructions](runtime.md#rt-bap-method-instructions)); instruction delivery does not establish compliance. Neither retained capability artifacts nor a smoke pass warrants their explanations or transfer.

Workflow recovery likewise grants a bounded operational license, not universal executable-identity warrant. [EPI-OBJ-checkpoint](#epi-obj-checkpoint) and [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution) distinguish unequal nonempty-hash rejection from hashless migration: after runtime-major and workflow name/version checks, the latter stamps the current hash and can reuse completed work without verifying its original executable. Neither branch establishes output truth or external replay safety.

These paths support independent conclusions: trace-fed memory rewriting is wired; improvement-directed machinery change is wired; actual learning as improved future capacity is unestablished by supplied evidence; parametric adaptation remains opaque under [RT-CMP-model-manager](runtime.md#rt-cmp-model-manager). The runtime's separately bounded theory-builder conditions, reflection and self-improvement account remains in [RT-RTE-extension-admission](runtime.md#rt-rte-extension-admission). No supplied episode establishes content-directed criticism plus retained next-round influence, nor later behavior causally depending on an update. Missing those episodes does not erase localized method text or the implemented change capacity. There is no single system epistemic score or universal verdict here.

## Shared records

### Operative objects

#### EPI-OBJ-response
Label: Agent and chat response content

Source-native identity: Response.message, generated model messages and evaluator reports. Natural-language assertions and methods are held in in-process response objects and may be logged; symbolic success/data fields have different consumers. This object isolates semantic content, not the runtime route or provider component. Closest supplied records [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task) and [RT-RTE-model-chat](runtime.md#rt-rte-model-chat) cover its producing routes, not a canonical content object. No supplied object counterpart. SRC-1; minimum passages supplied by those route records. [RT-CMP-model-manager](runtime.md#rt-cmp-model-manager) owns remote model mutability/version limits; this report adds no training claim.

#### EPI-OBJ-working-memory
Label: Working memory summaries

Source-native identity: `_SessionState.working`, natural-language strings in a bounded in-process deque, serialized in JSON execution_history. Claimed role: compress execution history for later prompt input. Distinct from [RT-OBJ-skill-content](runtime.md#rt-obj-skill-content), which stores authored methodology, and [RT-OBJ-extension-manifest](runtime.md#rt-obj-extension-manifest), which selects active capability versions. No supplied memory-object record. SRC-1 `autogenesis/memory/default/tiered.py`, `autogenesis/memory/default/general_memory_system.py`.

> "working_memory": list(state.working),
> --- `autogenesis/memory/default/general_memory_system.py`

#### EPI-OBJ-corpus
Label: Knowledge corpus documents

Source-native identity: per-base `corpus.jsonl` records and `manifest.json` RAG type. Text fields carry natural-language content; metadata/base/type/score are symbolic fields. Disk JSONL is reloaded on each retrieval. Claimed role: named corpora for relevance retrieval. No supplied object counterpart; unlike [RT-OBJ-extension-manifest](runtime.md#rt-obj-extension-manifest), these are caller documents rather than executable registry metadata. SRC-1 `autogenesis/knowledge/server.py`.

> docs.append(json.loads(line))
> --- `autogenesis/knowledge/server.py`

#### EPI-OBJ-evaluation
Label: Benchmark and workflow evaluation records

Source-native identity: benchmark Task.score/Stats, workflow WorkflowEvaluation and summary dictionaries. Symbolic records/numbers reside in process; version-scoped workflow records persist under evaluations.json. Natural-language notes are caller assertions, not evaluated evidence. Claimed role: score predictions or summarize workflow evidence. These are distinct from the registration metadata [RT-OBJ-extension-manifest](runtime.md#rt-obj-extension-manifest); no supplied evaluation-object counterpart. Routes below split the different checks/consumers. SRC-1 `autogenesis/benchmark/default/exact_match.py`, `autogenesis/workflow/context.py`.

> task.score = score
> --- `autogenesis/benchmark/default/exact_match.py`

#### EPI-OBJ-checkpoint
Label: Workflow checkpoint

Source-native identity: persisted WorkflowRun checkpoint and completed invocation state, including workflow name/version and program_hash. Symbolic serialized execution state is reloaded by workflow resume. Claimed role: resume execution after runtime-major and workflow name/version checks, with executable-contract consistency checked only when the checkpoint has a nonempty prior program_hash. The hashless migration branch stamps the current hash and can cache completed invocations without verifying their original executable identity. Distinct from [RT-OBJ-extension-manifest](runtime.md#rt-obj-extension-manifest), which holds registered capability versions rather than per-run execution. No supplied object counterpart; [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution) supplies implementation evidence and minimum passage for program-hash rejection. SRC-1 `autogenesis/workflow/runtime.py`; correction directly rechecks resume guards, hash migration and completed-invocation caching. The supplied runtime additionally traces WorkflowRun's empty-hash default and Gateway/manager restore forwarding. No independently observed checkpoint was supplied.

### Routes

#### EPI-RTE-history-compact
Label: History compaction

Endpoints: recent-history overflow → TieredMemory._compact → compact hook → model → returned summary. Code owns overflow selection, model supplies summary. Input includes chunk lines and previous working summary. No supplied route counterpart: [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task) consumes memory but does not describe its producer. SRC-1 `autogenesis/memory/default/tiered.py`, `autogenesis/hook/default/compact.py`; implementation and summarization instructions as doctrine/design. Selected records are popped before model return. Working-context control removes old raw records, retains newer recent tail, and supplies summaries; raw reload from this path is not implemented by get. This is by-value replacement, not an agent frame or a dereferenceable pointer. Model fidelity is requested, not independently checked. This transformation is separate from disposition/retention below.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Hook output string or None to compactor.
- Later read-back: Summary can reach later get calls after the retention route.
- Delegated visibility: inapplicable — no child agent is created; summarizer gets formatted records and prior summary only.
- Selection predicate: Overflow over recent_max; oldest compact_chunk selected.
- Invalidation or expiry: Bounded working deque eventually drops oldest summaries; get selects working_fetch.
- Activation or effect: Creates a summary candidate; later model-context delivery is wired, behavioral change unobserved.
- Evidence limits: No observed summary/input pair or independent semantic check; model weight fixity/version limits see RT-CMP-model-manager.

> "Summarise the records above in 2-4 sentences. Focus on what agents ran, "
> "what tools/skills were called, key results, and any failures. Preserve exact "
> "values (file paths, numbers, errors). Do not repeat the existing summary."
> --- `autogenesis/hook/default/compact.py`

#### EPI-RTE-summary-retain
Label: Summary retention

Endpoints: compact output → nonempty test → working deque → JSON persistence and get → future prompt assembly. TieredMemory owns admission. Compared with [RT-RTE-gateway-task](runtime.md#rt-rte-gateway-task), this is the memory write/selection mechanism rather than task execution. No supplied route counterpart. SRC-1 `autogenesis/memory/default/tiered.py`, `autogenesis/memory/default/general_memory_system.py`. Trigger and proposal: summarizer return after overflow; code decides and can reject empty output; no per-summary human approval or answer oracle. Rejection restores the popped chunk when output is empty; successful replacement keeps text, not a checked source-to-claim mapping. Exceptions are logged, not an arbitrary-effect transaction. Guidance shaping the proposal is in the preceding route. This is retention before epistemic acceptance, not lifecycle integration.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Append summary, or restore chunk and stop on empty output.
- Later read-back: get injects last working_fetch summaries and selected recent records into next requesting agent context; persistence renderer includes summaries.
- Delegated visibility: inapplicable — same-session memory path, not child delegation.
- Selection predicate: Nonempty text; session_id and working_fetch determine later selection.
- Invalidation or expiry: Old summaries evicted by bounded deque; process-restart rehydration not established here.
- Activation or effect: Changes future prompt-visible history without a fidelity approval gate.
- Evidence limits: No observed later consumer behavior; a truth-acceptance criterion is not present in this inspected nonempty test.

> if text:
>     state.working.append(text)
> else:
>     async with state._lock:  # lossless: restore and stop
>         state.recent.extendleft(reversed(chunk))
>     break
> --- `autogenesis/memory/default/tiered.py`

> working = list(state.working)[-self.working_fetch:]
> --- `autogenesis/memory/default/tiered.py`

#### EPI-RTE-corpus-ingest
Label: Corpus ingestion

Endpoints: caller knowledge_ingest payload → document coercion/backend check → appended JSONL and RAG manifest. KnowledgeManager owns admission, caller proposes documents; no required human authorship/approval or truth oracle. Open pipeline input, not fixed evaluation curriculum. No supplied route counterpart; overlap with [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution) is the workflow caller only. SRC-1 `autogenesis/knowledge/server.py`. Admission requires base/backend and writable disk, not evidence for claims. Normalization retains dict fields, selecting text_field into text; caller strings become text records. Rejection covers missing base, unknown type and I/O error. Repeated writes append, not replace; no deletion/rollback operation is exposed by this manager's two-operation dispatch. No theory-revision inference from storage.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Counts/base/type envelope, not the full ingested content.
- Later read-back: Later knowledge_retrieve reloads corpus.jsonl.
- Delegated visibility: inapplicable — no agent fork; caller-supplied payload only.
- Selection predicate: Named base, available backend, coerceable documents.
- Invalidation or expiry: Append-only in inspected operation; no built-in deduplication/expiry.
- Activation or effect: Makes caller text persistently retrievable; does not enforce truth acceptance.
- Evidence limits: No actual corpus or provenance supplied; source warrant unknown; no automatic citation binding.

> for doc in docs:
>     handle.write(json.dumps(doc, ensure_ascii=False) + "\n")
> --- `autogenesis/knowledge/server.py`

#### EPI-RTE-corpus-retrieve
Label: Corpus retrieval

Endpoints: base/query → disk corpus → selected RagBackend.search → indexed documents with scores → workflow caller. KnowledgeManager and lexical ranker own selection. Distinct from [RT-RTE-skill-delivery](runtime.md#rt-rte-skill-delivery): document ranking, not named methodology retrieval. No supplied counterpart. SRC-1 `autogenesis/knowledge/server.py`, `autogenesis/knowledge/default/rankers.py`, `autogenesis/workflow/runtime.py`. Built-in BM25 lowercases/splits words; TF-IDF fits sparse vectors on corpus and uses cosine similarity. These are symbolic/statistical retrieval representations, not inspected learned provider weights. The operation evaluates relevance, not truth. Query may be model- or caller-authored; authorship unresolved. Source document fields are carried through, with score overwritten/added. No evaluator result accepts facts for a named task-domain use.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Top-k records with relevance score and query/base/type.
- Later read-back: Requested delivery of stored acquired material; corpus stays available for future queries.
- Delegated visibility: inapplicable — no separate child context.
- Selection predicate: Named base; nonempty query; persisted backend type; top_k bounded below by 1.
- Invalidation or expiry: Missing/empty corpus, unavailable ranker or search errors return failure; no endorsement invalidation.
- Activation or effect: Ranks and delivers documents to requesting workflow; downstream graph may consume selected fields.
- Evidence limits: No observed retrieval/answer or claim-specific provenance; downstream warrant remains unknown.

> results = [{**docs[index], "score": score} for index, score in hits if 0 <= index < len(docs)]
> --- `autogenesis/knowledge/server.py`

> ranked = sorted(enumerate(scores), key=lambda pair: pair[1], reverse=True)
> --- `autogenesis/knowledge/default/rankers.py`

#### EPI-RTE-json-parse
Label: JSON parsing

Endpoints: parse_json processor input → _as_text/strip → json.loads → canonical Response → workflow consumer. Processor code owns deterministic syntax conversion. No supplied counterpart; [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution) is a broader container route.
Part of: [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution)
SRC-1 `autogenesis/process/default/text.py`, `autogenesis/workflow/runtime.py`. The concrete ledger input is already a JSON string so _as_text returns it unchanged; parsed dictionary is wrapped as one record. This is implementation deduction, not an observed execution. Syntax failure can reject conversion but does not test an encoded factual proposition.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Parsed value, records/count or invalid-JSON error.
- Later read-back: inapplicable — pure processor does not retain changed state.
- Delegated visibility: inapplicable — deterministic local processor, no delegation.
- Selection predicate: Explicit parse_json target and input text.
- Invalidation or expiry: inapplicable — no retained state; invalid JSON fails current call.
- Activation or effect: Downstream graph gets structured values.
- Evidence limits: Only JSON encoding fidelity for this input; no units, measurements, source truth or general semantic validation.

> value = json.loads(raw)
> --- `autogenesis/process/default/text.py`

> records = value if isinstance(value, list) else [value] if isinstance(value, dict) else []
> --- `autogenesis/process/default/text.py`

#### EPI-RTE-exact-match
Label: Exact match evaluation

Endpoints: workflow BENCHMARK payload → batch manager Task construction → ExactMatchBenchmark.eval → average → Response score/count. Code owns evaluation. Caller supplies predictions and references; no built-in oracle provider verifies ground_truth. Operating mode: caller-defined bounded record batch. No supplied counterpart; a material benchmark part of the broader workflow route.
Part of: [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution)
SRC-1 `autogenesis/benchmark/default/exact_match.py`, `autogenesis/benchmark/server.py`, `autogenesis/workflow/runtime.py`. Prediction/reference are stripped strings; nonempty prediction first attempts numeric tolerance, otherwise string equality. No task_id in batch means zero; errors also contribute zero. The workflow returns success=True for the completed scoring call even if average is zero. No inspected code here keeps, revises or rolls back a capability from that score. This is evidence production, not acceptance.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Numeric average from manager, wrapped by workflow with count.
- Later read-back: inapplicable — scoring output is current invocation data; benchmark keeps in-process scored Tasks for stats but no later behavioral reader is established.
- Delegated visibility: inapplicable — batch coroutine scoring, no model child.
- Selection predicate: Explicit benchmark target and supplied results; nonempty task_id required by batch manager.
- Invalidation or expiry: initialize/reset clear in-process scored task list.
- Activation or effect: Produces evidence signal for downstream graph/caller, not mandatory dispatch veto.
- Evidence limits: Reference truth and dataset quality unknown; equality does not identify mechanism, causal benefit or replay safety.

> score = 1.0 if abs(float(pred) - float(gt)) < 1e-9 else 0.0
> --- `autogenesis/benchmark/default/exact_match.py`

> score = 1.0 if pred == gt else 0.0
> --- `autogenesis/benchmark/default/exact_match.py`

> avg_score = sum(scores) / len(scores) if scores else 0.0
> --- `autogenesis/benchmark/server.py`

#### EPI-RTE-workflow-evaluation
Label: Workflow evaluation admission and summary

Endpoints: evolution_tool record_workflow_evaluation → WorkflowContextManager.record_evaluation → persisted evaluations → evaluation_summary → caller. Code owns consistency veto, caller proposes success/quality/notes. Human authorship is not established by invoking this API. Operating mode: version-scoped workflow run/case tracking. No supplied counterpart; distinct from [RT-RTE-workflow-execution](runtime.md#rt-rte-workflow-execution), which executes/resumes rather than evaluates records. SRC-1 `autogenesis/tool/default/evolution.py`, `autogenesis/workflow/context.py`. Successful records require a real retained terminal run with matching name/version/program hash and success classification; metrics are derived from the run; duplicate run evidence rejected. Static failures instead require case_id. Accepted records persist; proposal guidance is caller-controlled. No automatic rollback is performed by this tool branch. Current-version summaries compute healthy against three thresholds. Ledger rows separate admission from evidence derivation; same implementation container, not interchangeable functions. No domain answer oracle verifies caller quality_score. This is record acceptance/integration into an operational ledger, not accepted ampliative knowledge.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Stored evaluation and summary; errors become tool failure.
- Later read-back: evaluations(name) filters to active version; summary aggregates retained matching records; _load_evaluations reloads file.
- Delegated visibility: inapplicable — no delegated context constructed.
- Selection predicate: Registered version; matching terminal run or named static failure; no duplicate run_id.
- Invalidation or expiry: Version filtering excludes older records from current summary; admission rejects mismatches rather than repairing them.
- Activation or effect: Enforces ledger admission; advisory healthy signal reaches tool caller.
- Evidence limits: Not a controlled comparison; success is workflow state, quality remains caller claim; no observed recorded run supplied.

> if evaluation.success != run.successful:
>     raise ValueError("Evaluation success must match the recorded Workflow run")
> --- `autogenesis/workflow/context.py`

> if evaluation.run_id and any(item.run_id == evaluation.run_id for item in existing):
>     raise ValueError("This Workflow run has already been evaluated")
> existing.append(evaluation)
> self._save_evaluations()
> --- `autogenesis/workflow/context.py`

> "healthy": len(distinct_cases) >= 3 and success_rate >= 0.8 and quality >= 0.7,
> --- `autogenesis/workflow/context.py`

#### EPI-RTE-memory-evaluate
Label: Memory evaluation report

Endpoints: selected MemoryEvaluateAgent → ordinary Agent loop under evaluation prompt → scored Response → caller. Model proposes judgments; ordinary code dispatches tools and returns report. No supplied evaluator-specific counterpart: [RT-RTE-child-delegation](runtime.md#rt-rte-child-delegation) describes optional orchestration, but this evaluator can also be invoked directly. SRC-1 `autogenesis/agent/evaluator/memory_evaluate_agent.py`, `autogenesis/prompt/default/memory_evaluate_agent.html`, `configs/agents/memory_evaluate_agent.py`. Config uses google/gemini-3.1-pro-preview, same endpoint/version limitations as [RT-CMP-model-manager](runtime.md#rt-cmp-model-manager). Domain is memory source/interface/code/actions/integration/functionality, not factual truth of retained memory. Prompt prescribes registry inspection, source reading and in-process probes, then report. Those steps are requested, not enforced as universal prerequisites by the class. No expected-answer oracle is supplied; model reports rubric judgments. Prompt's ENVIRONMENT decorator/get_state/action assumptions do not match the inspected MEMORY_SYSTEM-registered TieredMemory.get/record route. Thus even nominal interface scores need criterion repair before reliance. No target execution or report was supplied. The evaluator produces no registrable artifact and has no direct accept/rollback transaction; parent may choose to act on advice.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ordinary agent Response containing complete/partial report or failure.
- Later read-back: uninspected — configured memory may retain reports; this class does not establish report-specific later selection.
- Delegated visibility: When delegated, task and selected files/registry facts, not complete parent context; direct calls need no child.
- Selection predicate: Explicit evaluator selection and named target memory in task.
- Invalidation or expiry: inapplicable — no artifact admission or persistent evaluation ledger in evaluator class.
- Activation or effect: Advice reaches caller; no mandatory quality veto or source mutation by this class.
- Evidence limits: Tool availability/probe implementation not established from prompt text; actual report, rubric adherence and validity unobserved.

> return await super().__call__(task=task, files=files, ctx=ctx, **kwargs)
> --- `autogenesis/agent/evaluator/memory_evaluate_agent.py`

> - `@ENVIRONMENT.register_module(force=True)` decorator present.
> --- `autogenesis/prompt/default/memory_evaluate_agent.html`

> async def get(self, session_id: str, short_term_n: Optional[int] = None, **kwargs) -> Optional[str]:
> --- `autogenesis/memory/default/tiered.py`

### Claims

#### EPI-CLM-memory-rubric
Label: Memory evaluation quality claim

Claimed operation: evaluate existing memory over five dimensions, return scored report and optimization suggestions, without modifying memory. SRC-1 `autogenesis/prompt/default/memory_evaluate_agent.html`, `autogenesis/agent/evaluator/memory_evaluate_agent.py`; doctrine/design. Distinct from [RT-CLM-evolution-guidance](runtime.md#rt-clm-evolution-guidance), which prescribes the orchestration and admission method, not this evaluator's target/rubric. Implementation supports an ordinary model loop requesting that work, not validated score reliability. API mismatch and unverified probe availability limit the promised coverage.

> You are an expert memory evaluation agent. You receive an evaluation task, read the target memory's source file, run quality checks, and produce a complete evaluation report with per-dimension scores and concrete optimization suggestions.
> --- `autogenesis/prompt/default/memory_evaluate_agent.html`

### Behavioral-authority paths

none declared in this member
