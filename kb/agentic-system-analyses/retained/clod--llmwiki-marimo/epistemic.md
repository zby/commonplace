---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Epistemic routes of llmwiki-marimo: document compilation, mode-specific grounding, verification, repair and conditional financial derivation."
run-id: AAS-2026-10-18-llmwiki-marimo-58054ccd9ae7-01
reviewed-boundary: "0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7"
---

# llmwiki-marimo epistemic report

## Source-and-claim boundary

The question is how imported documents and datasets become retained claims and later answers, which checks license reliance, and which results actually change admission or use. Scope and external exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identity is see its [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not an observed workload or causal comparison. No target code, tests, model or example was executed for this report.

The route boundary includes generation, save admission, retrieval/grounding, verification, maintenance, structured-data admission and arithmetic, and developer evaluation. Generation and NLI parameters are separately described in [RT-CMP-openai-model](runtime.md#rt-cmp-openai-model) and [RT-CMP-local-nli-verifier](runtime.md#rt-cmp-local-nli-verifier). Their inaccessible weights and provider internals prevent claims about latent derivations, calibration, training or hidden state. No supplied provenance trace connects example pages to a particular generation/check/acceptance route. A retained example establishes availability, not an exercised warrant chain. No execution or controlled comparison establishes improved answers, factual accuracy, repair success or component benefit.

The following coverage distinguishes direct additional source inspection from the supplied runtime account. All direct reads are SRC-1 at the frozen commit. An available but uninspected relevant operation prevents a system-complete negative about acceptance, knowledge production or adaptation.

| Entry point or operation | Source path | Coverage and records / limit |
|---|---|---|
| Web/marimo launch, chat dispatch, standard tools and extension grants | `quickstart.py`, `web/routes/chat.py`, `marimo/read_app.py`, `marimo/read_app_tabs.py`, `base/domain/chat/agent.py` | Supplied [RT-RTE-configure-grants](runtime.md#rt-rte-configure-grants), [RT-CLM-readonly-chat](runtime.md#rt-clm-readonly-chat); direct web verification consumer and installer evaluator consumer reads. No independently inspected dependency dispatch or arbitrary caller extra tools. |
| Upload/scan/batch, extraction, concept merge, summary/overview | `base/services/ingest.py`, `base/domain/ingestion/pipeline.py`, `base/domain/ingestion/wiki_generator.py`, `prompts/extract_system.en.md` | Supplied [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest); direct generator summary/concept/chat structuring and outer-fence stripping, extraction instructions. Source extraction and overview internals rely on runtime; translation equivalence unassessed. |
| Strict, pre-retrieval and streaming answers; refused-history removal | `base/services/chat.py`, `base/domain/chat/guardrail.py`, `base/domain/chat/preretrieval.py`, `base/domain/chat/history.py` | Supplied [RT-RTE-strict-chat](runtime.md#rt-rte-strict-chat), [RT-RTE-preretrieval-chat](runtime.md#rt-rte-preretrieval-chat), [RT-RTE-streaming-chat](runtime.md#rt-rte-streaming-chat); direct guardrail and pre-retrieval post-check reads. History compaction relies on runtime. |
| Citation/table post-processing | `base/domain/chat/postprocess.py` | Direct full file; [EPI-RTE-answer-format](#epi-rte-answer-format). |
| Web draft/verify/save, marimo last-answer save, convenience save | `web/routes/chat.py`, `base/services/chat.py`, `base/domain/chat/wiki_tools.py` | Supplied [RT-RTE-chat-save](runtime.md#rt-rte-chat-save); direct draft-generation helper and answer verification consumer. Review opportunity is not universal acceptance. |
| Page/answer verification, persisted scores, freshness, warning consumers | `base/domain/verify/core.py`, `base/domain/verify/page.py`, `base/domain/verify/store.py`, `base/domain/verify/checkable.py`, `base/domain/verify/nli.py`, `base/domain/lint/checks.py`, `web/routes/chat.py` | Direct reads; [EPI-RTE-verify-check](#epi-rte-verify-check), [EPI-RTE-verify-store](#epi-rte-verify-store), [EPI-RTE-verify-use](#epi-rte-verify-use). Passage splitting/preselection helpers not fully audited: prevents exhaustive claims about encoding fidelity. |
| Lint dispatch, contradiction/data-gap checks and warning/TODO/filled-gap repairs | `base/domain/lint/runner.py`, `base/domain/lint/checks.py`, `base/domain/repair/runner.py`, `base/domain/repair/actions.py` | Direct selected checks/actions plus full dispatch; [EPI-RTE-contradiction-check](#epi-rte-contradiction-check), [EPI-RTE-contradiction-note](#epi-rte-contradiction-note), [EPI-RTE-gap-check](#epi-rte-gap-check), [EPI-RTE-gap-note](#epi-rte-gap-note). Other check/action bodies remain supplied-runtime coverage, not an exhaustive semantic audit. |
| Stale repair/delete, source deletion, manual edit/delete, reindex, forward restore | `base/services/ingest.py`, `base/services/wiki.py`, `base/domain/tools/wiki_fs.py`, `base/domain/rollback/revert.py` | Supplied [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance); additional service searches show source removal marks citing pages stale rather than retracting every claim. Domain deletion internals not independently read; prevents complete withdrawal guarantees. |
| Settings/vocabulary, generated aliases and conditional tool installation | `base/services/settings.py`, `base/services/vocabulary.py`, `base/domain/ingestion/wiki_generator.py`, `base/domain/finance_argentina/agent_tool.py` | Supplied [RT-RTE-configure-grants](runtime.md#rt-rte-configure-grants); collision/type/scope admission is not validation of synonym truth. No autonomous plugin installation established. |
| Dataset lookup, financial validation/eligibility/ranking/projection | `base/domain/datasets/source.py`, `base/domain/datasets/parser.py`, `base/domain/finance_argentina/validator.py`, `base/domain/finance_argentina/advisory.py`, `base/domain/finance_argentina/formulae.py` | Direct source, validator, formulae and advisory selection/calculation bodies; parser entry points searched, not audited. [EPI-RTE-finance-check](#epi-rte-finance-check), [EPI-RTE-finance-select](#epi-rte-finance-select), [EPI-RTE-finance-derive](#epi-rte-finance-derive). No value-source authentication or freshness accuracy conclusion. |
| Model smoke check and installer continuation | `scripts/eval_chat_model.py`, `quickstart.py` | Supplied [RT-RTE-model-evaluation](runtime.md#rt-rte-model-evaluation); direct installer body. Failure warns but does not block launch/install. |
| Eval packet and golden freeze CLI dispatch | `scripts/build_eval_packet.py`, `scripts/build_golden_corpus.py`, `base/domain/eval/` | Direct probe-generation and freeze/dispatch bodies; [EPI-RTE-eval-packet](#epi-rte-eval-packet), [EPI-RTE-corpus-freeze](#epi-rte-corpus-freeze). Rubric/reader/packet internals uninspected: no completeness or judge calibration claim. |
| Verification CLI/battery, finance UAT, regression and other tests | `scripts/verify_pages.py`, `scripts/verify_battery.py`, `scripts/uat_finanzas.py`, `tests/` | Script dispatch/verification-call search; supplied runtime's structural regression coverage. Battery aggregate implementation and UAT/test assertions not fully inspected or run; prevents comprehensive evaluator inventory, reported scores, and system-complete absence of further checks. |

Consequential claims are [EPI-CLM-wiki-compilation](#epi-clm-wiki-compilation), [EPI-CLM-grounding-mandate](#epi-clm-grounding-mandate), [EPI-CLM-wiki-maintenance](#epi-clm-wiki-maintenance), [EPI-CLM-finance-advisory](#epi-clm-finance-advisory), and [RT-CLM-readonly-chat](runtime.md#rt-clm-readonly-chat). These are source-native claims, not adopted guarantees.

## Epistemic-object inventory

Object properties are see the declaring records. The inventory separates parts by their evaluators and consequential consumers, not by a universal claim format.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-source-text](#epi-obj-source-text) | Document assertions | Imported evidence | see record | Original truth and extraction fidelity not established |
| [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | Summary/concept/overview and saved-chat assertions | Reusable curated knowledge | see record | Model semantic preservation unknown; code metadata is not a warrant |
| [EPI-OBJ-chat-answer](#epi-obj-chat-answer) | Turn's claims and comparisons | Grounded response or refusal | see record | Model output meaning relative to premises unobserved |
| [EPI-OBJ-verification-report](#epi-obj-verification-report) | Estimated sentence support; hashes are symbolic state | Diagnostic evidence | see record | Relative support is not source truth or semantic proof |
| [EPI-OBJ-lint-issues](#epi-obj-lint-issues) | Possible conflict/undercoverage; repair directives | Maintenance candidates | see record | Limited inputs; warning retention is not adjudication |
| [EPI-OBJ-dataset-rows](#epi-obj-dataset-rows) | Values, dates, attributed origins; symbolic eligibility attributes | Current structured evidence | see record | External source warrant unknown; replace-latest is not real-time verification |
| [EPI-OBJ-advisory-result](#epi-obj-advisory-result) | Conditional gains/ranks and non-estimable classifications | Computed advice | see record | Arithmetic/model-domain license only |
| [RT-CMP-openai-model](runtime.md#rt-cmp-openai-model) | Internal truth-apt units not determinable | Generation/condensation | see record | Opaque parametric state, not an inspectable proposition store |
| [RT-CMP-local-nli-verifier](runtime.md#rt-cmp-local-nli-verifier) | Internal truth-apt units not determinable | Pairwise evaluator | see record | Weight provenance/calibration not supplied |
| [RT-RTE-configure-grants](runtime.md#rt-rte-configure-grants) | Aliases may assert identity; blacklist/settings also encode policy, not necessarily truth | Scope/capability controls | see record | Retained policy affects later calls without thereby producing knowledge |

## Authority-route ledger

Architectural status below is the overlay's assessment. Other route fields and load-bearing passages are see the linked records. No observed-run state is inferred from implemented status. Each repeated route citation denotes a different function, not a second identity. No inspected passage establishes an evidence-consuming acceptance decision for the truth of all generated prose. Thus retention and operational admission are not labelled lifecycle integration after acceptance.

Route ID: [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: EPI-OBJ-source-text / EPI-OBJ-wiki-pages (see inventory).
Content/update relation: truth-apt transformation: acquisition/import.
Transition or check target: Document text into indexed source evidence.
Evaluator/condition and domain: Extractors and pipeline eligibility; file/format/hash domain.
Activation and timing: On upload/scan; before page generation; operation unobserved.
Possible or observed result: Extracted source rows or failure (possible, not an observed event).
Implemented force: Code-enforcing format eligibility.
Epistemic authority and scope: Imported assertions with source warrant unknown.
Operational authority: Source becomes available to generation/retrieval.
Behavioral-authority path: Pipeline, extracted text/SQLite, permissive, subsequent generation/queries.
Evidence source ID and local anchor: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest).
Claim IDs or none: [EPI-CLM-wiki-compilation](#epi-clm-wiki-compilation).
Mismatch marker or none: none.
Gap/limit: No source-truth check; extractor accuracy unobserved.

Route ID: [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: EPI-OBJ-wiki-pages (see inventory).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: Extraction/concept merge/overview candidates.
Evaluator/condition and domain: Generation model guided by localized templates; semantic fidelity unchecked.
Activation and timing: After source extraction and when same-slug page exists; operation unobserved.
Possible or observed result: Proposed summaries, insights, merged pages (possible, not an observed event).
Implemented force: Prompt advisory; code accepts returned prose.
Epistemic authority and scope: Candidate assertions only; may reshape, derive or introduce claims.
Operational authority: Candidate pages proceed to writes.
Behavioral-authority path: Pipeline, model response, permissive, page-write horizon.
Evidence source ID and local anchor: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest).
Claim IDs or none: [EPI-CLM-wiki-compilation](#epi-clm-wiki-compilation).
Mismatch marker or none: none.
Gap/limit: No input/output trace distinguishes non-ampliative reshaping, entailment and conjecture.

Route ID: [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages).
Content/update relation: no content change.
Transition or check target: Generated page candidate admission to pipeline writes.
Evaluator/condition and domain: Code handles representation/errors and progression, not proposition truth. JSON parse failure can still yield raw summary fallback.
Activation and timing: After model response, before create_page/summary write; operation unobserved.
Possible or observed result: Proposed prose admitted or failure/compensation; no observed ingest supplied.
Implemented force: Software-controlled operational admission without per-generated-page approval.
Epistemic authority and scope: No named truth acceptance criterion or independent answer oracle in this branch.
Operational authority: Allows candidate prose into page-writing path; operator can withhold entire job, not approve each candidate here.
Behavioral-authority path: Parser/pipeline to wiki writer, extraction object/Markdown, permissive, current ingest and downstream retained use.
Evidence source ID and local anchor: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest).
Claim IDs or none: [EPI-CLM-wiki-compilation](#epi-clm-wiki-compilation).
Mismatch marker or none: representation fallback is not truth acceptance.
Gap/limit: Model instruction to preserve content is not an enforced semantic comparison.

Route ID: [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Route function: retention
Architectural status: implemented
Object/candidate ID: EPI-OBJ-wiki-pages (see inventory).
Content/update relation: no content change.
Transition or check target: Generated page retention.
Evaluator/condition and domain: Pipeline write/exception conditions, not a factual acceptance criterion.
Activation and timing: During ingest; operation unobserved.
Possible or observed result: Pages/index/references; compensating recovery on caught failure (possible, not an observed event).
Implemented force: Enforcing writes; best-effort recovery.
Epistemic authority and scope: No additional truth license from persistence.
Operational authority: Later merges and retrieval can consume unapproved generated prose.
Behavioral-authority path: Wiki files/index, generation/retrieval consumers, permissive, later invocations.
Evidence source ID and local anchor: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest).
Claim IDs or none: [EPI-CLM-wiki-compilation](#epi-clm-wiki-compilation).
Mismatch marker or none: none.
Gap/limit: Retention is not post-acceptance lifecycle integration.

Route ID: [RT-RTE-strict-chat](runtime.md#rt-rte-strict-chat)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: EPI-OBJ-chat-answer (see inventory).
Content/update relation: no content change.
Transition or check target: Existence of substantive tool return, not answer entailment.
Evaluator/condition and domain: Deterministic has_grounding over ToolReturnPart nonempty text excluding sentinels.
Activation and timing: After buffered run; all_messages supplied; operation unobserved.
Possible or observed result: Boolean grounding proxy (possible, not an observed event).
Implemented force: Internal predicate.
Epistemic authority and scope: At most retrieved material exists under the predicate.
Operational authority: Feeds output gate.
Behavioral-authority path: Service, Boolean, enforcing via next disposition, current return.
Evidence source ID and local anchor: see [RT-RTE-strict-chat](runtime.md#rt-rte-strict-chat).
Claim IDs or none: [EPI-CLM-grounding-mandate](#epi-clm-grounding-mandate).
Mismatch marker or none: proxy not entailment.
Gap/limit: Prior-history semantics and negative-marker false negatives qualify scope.

Route ID: [RT-RTE-strict-chat](runtime.md#rt-rte-strict-chat)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: EPI-OBJ-chat-answer (see inventory).
Content/update relation: no content change.
Transition or check target: Return output versus substitute refusal.
Evaluator/condition and domain: Service uses grounding Boolean; criterion is tool-result presence.
Activation and timing: Before strict return; operation unobserved.
Possible or observed result: Answer retained or refusal substituted (possible, not an observed event).
Implemented force: Enforcing return substitution.
Epistemic authority and scope: Operational admission only, not acceptance of answer truth.
Operational authority: Allows answer through or blocks it.
Behavioral-authority path: Caller/display/history, final answer channel, enforcing, this turn and later saved/history uses.
Evidence source ID and local anchor: see [RT-RTE-strict-chat](runtime.md#rt-rte-strict-chat).
Claim IDs or none: [EPI-CLM-grounding-mandate](#epi-clm-grounding-mandate).
Mismatch marker or none: mode-scoped guarantee.
Gap/limit: A retrieved but ignored result passes; streaming omits check.

Route ID: [RT-RTE-preretrieval-chat](runtime.md#rt-rte-preretrieval-chat)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: EPI-OBJ-source-text / EPI-OBJ-wiki-pages / EPI-OBJ-dataset-rows (see inventory).
Content/update relation: no content change.
Transition or check target: Question scope and context selection.
Evaluator/condition and domain: Code roster/blacklist/open-page/collection/data predicates; optional model rewrite rechecked.
Activation and timing: Before answer generation; operation unobserved.
Possible or observed result: Refuse or inject curated/raw/data context or use data tools (possible, not an observed event).
Implemented force: Enforcing branch selection; prompt interpretation advisory.
Epistemic authority and scope: Licensed context delivery, not proposition endorsement.
Operational authority: May prevent generation or change its evidence/context.
Behavioral-authority path: Orchestrator to answer model, template/tool grants, permissive/enforcing, turn.
Evidence source ID and local anchor: see [RT-RTE-preretrieval-chat](runtime.md#rt-rte-preretrieval-chat).
Claim IDs or none: [EPI-CLM-grounding-mandate](#epi-clm-grounding-mandate).
Mismatch marker or none: branch-specific coverage.
Gap/limit: Existing page/collection/data alternatives defeat an FTS-only account.

Route ID: [RT-RTE-preretrieval-chat](runtime.md#rt-rte-preretrieval-chat)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: EPI-OBJ-chat-answer (see inventory).
Content/update relation: no content change.
Transition or check target: Raw-source lexical overlap and context-free tool grounding.
Evaluator/condition and domain: Coverage threshold for raw tier; tool predicate only when no injected context.
Activation and timing: After answer; curated tier lacks equivalent lexical check; operation unobserved.
Possible or observed result: Refusal or answer plus warning/attribution (possible, not an observed event).
Implemented force: Enforcing substitution at selected branches.
Epistemic authority and scope: Lexical similarity or lookup presence, not semantic entailment.
Operational authority: Return blocked on failed predicate; otherwise displayed.
Behavioral-authority path: Service to UI/history, answer/refusal, enforcing, turn and caller-retained uses.
Evidence source ID and local anchor: see [RT-RTE-preretrieval-chat](runtime.md#rt-rte-preretrieval-chat).
Claim IDs or none: [EPI-CLM-grounding-mandate](#epi-clm-grounding-mandate).
Mismatch marker or none: proxy not entailment.
Gap/limit: Raw and curated delivery are not a uniform semantic verifier.

Route ID: [RT-RTE-streaming-chat](runtime.md#rt-rte-streaming-chat)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: EPI-OBJ-chat-answer (see inventory).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: Generated answer emission.
Evaluator/condition and domain: Model generation, code event dispatch; no strict post-check.
Activation and timing: Text emitted during agent loop; operation unobserved.
Possible or observed result: Immediate chunks and final answer (possible, not an observed event).
Implemented force: Immediate display.
Epistemic authority and scope: No check-derived truth license.
Operational authority: User sees output before any later voluntary inspection.
Behavioral-authority path: Streaming caller, SSE/text chunks, permissive, immediate display/history.
Evidence source ID and local anchor: see [RT-RTE-streaming-chat](runtime.md#rt-rte-streaming-chat).
Claim IDs or none: [EPI-CLM-grounding-mandate](#epi-clm-grounding-mandate).
Mismatch marker or none: explicit unchecked alternative.
Gap/limit: Unverified mode is documented, not a demonstrated factual failure.

Route ID: [RT-RTE-chat-save](runtime.md#rt-rte-chat-save)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-chat-answer](#epi-obj-chat-answer), [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: Conversation/last answer and existing page to proposed structured Markdown.
Evaluator/condition and domain: Structuring model under localized concept instructions; no independent semantic-preservation check.
Activation and timing: Web draft request or marimo/convenience save; operation unobserved.
Possible or observed result: Structured/merged draft; no observed draft supplied.
Implemented force: Prompt-guided proposal, not factual acceptance.
Epistemic authority and scope: Candidate page assertions; semantic preservation/entailment unestablished.
Operational authority: Web displays editable draft; marimo/convenience route proceeds directly to write.
Behavioral-authority path: Draft model to web reviewer or write helper, Markdown, advisory proposal versus permissive software input, draft/save horizon.
Evidence source ID and local anchor: see [RT-RTE-chat-save](runtime.md#rt-rte-chat-save), SRC-1, `base/domain/ingestion/wiki_generator.py`.
Claim IDs or none: [RT-CLM-readonly-chat](runtime.md#rt-clm-readonly-chat).
Mismatch marker or none: review is caller protocol.
Gap/limit: No trace classifies a particular restructuring as reshaping, entailment or conjecture.

Route ID: [RT-RTE-chat-save](runtime.md#rt-rte-chat-save)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages).
Content/update relation: no content change.
Transition or check target: Submitted web Markdown's operational admission to write.
Evaluator/condition and domain: User can edit/cancel normal draft dialog; endpoint requires nonempty input/free lock, not verification or draft-provenance token.
Activation and timing: Explicit web save request, after normal review opportunity but not necessarily a prior draft; operation unobserved.
Possible or observed result: Save accepted or input/busy rejection; no observed request supplied.
Implemented force: Enforcing request predicates; human review is protocol.
Epistemic authority and scope: No recorded evidence-consuming truth criterion/intended use/scope; not epistemic acceptance.
Operational authority: Permits write of submitted Markdown; optional draft verification does not veto.
Behavioral-authority path: Web user/endpoint to service, submitted Markdown, permissive on request predicates, current save and later page reuse.
Evidence source ID and local anchor: see [RT-RTE-chat-save](runtime.md#rt-rte-chat-save).
Claim IDs or none: [RT-CLM-readonly-chat](runtime.md#rt-clm-readonly-chat).
Mismatch marker or none: review not enforced by endpoint.
Gap/limit: User initiation is not evidence of assessment of every proposition.

Route ID: [RT-RTE-chat-save](runtime.md#rt-rte-chat-save)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages).
Content/update relation: no content change.
Transition or check target: Model-structured last answer/conversation admission on marimo/convenience service paths.
Evaluator/condition and domain: User initiates save; software drafts then writes without intermediate review or semantic approval criterion.
Activation and timing: Marimo last-response save or save_conversation service call; operation unobserved.
Possible or observed result: Page write or surfaced/logged failure; no observed save supplied.
Implemented force: Permissive software admission; no per-draft human veto interval.
Epistemic authority and scope: Retainable candidate, not accepted true claim.
Operational authority: Lets returned model prose proceed to write and model-capable repair where client supplied.
Behavioral-authority path: Structuring model to save helper, generated Markdown, permissive, current save and future retrieval.
Evidence source ID and local anchor: see [RT-RTE-chat-save](runtime.md#rt-rte-chat-save).
Claim IDs or none: [RT-CLM-readonly-chat](runtime.md#rt-clm-readonly-chat).
Mismatch marker or none: no second review.
Gap/limit: Human direction and automatic content admission coexist.

Route ID: [RT-RTE-chat-save](runtime.md#rt-rte-chat-save)
Route function: retention
Architectural status: implemented
Object/candidate ID: EPI-OBJ-wiki-pages (see inventory).
Content/update relation: no content change.
Transition or check target: Admitted Markdown to retained page/index/references.
Evaluator/condition and domain: Write helper persists already admitted content; repair errors may not abort primary save.
Activation and timing: After caller-specific admission; operation unobserved.
Possible or observed result: Written/merged page and repairs (possible, not an observed event).
Implemented force: Software admission plus caller-dependent human protocol.
Epistemic authority and scope: No recorded named truth criterion, intended use and evidence-consuming decision.
Operational authority: Saved content enters retrieval and later same-slug generation.
Behavioral-authority path: Wiki service, Markdown/index, permissive, later turns/ingests.
Evidence source ID and local anchor: see [RT-RTE-chat-save](runtime.md#rt-rte-chat-save).
Claim IDs or none: [RT-CLM-readonly-chat](runtime.md#rt-clm-readonly-chat).
Mismatch marker or none: review is caller protocol.
Gap/limit: Draft restructuring may change assertions; voluntary initiation is not per-claim acceptance.

Route ID: [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: EPI-OBJ-wiki-pages (see inventory).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: Edit, regenerate, stale marking/deletion, repair and restore.
Evaluator/condition and domain: Issue dispatch, optional model, human job/version/revision choice.
Activation and timing: Maintenance or post-ingest; operation unobserved.
Possible or observed result: New/replaced/deleted/restored pages or warnings (possible, not an observed event).
Implemented force: Code mutations; some advisory results skipped.
Epistemic authority and scope: Lineage/recovery predicates do not warrant restored or regenerated truth.
Operational authority: Controls what later readers/agents can retrieve.
Behavioral-authority path: Services to files/index/history, enforcing or advisory by action, later invocations.
Evidence source ID and local anchor: see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance).
Claim IDs or none: [EPI-CLM-wiki-maintenance](#epi-clm-wiki-maintenance).
Mismatch marker or none: none.
Gap/limit: Combined container; distinct criticism/warning functions expanded below, other algorithms not exhaustively audited.

Route ID: [EPI-RTE-answer-format](#epi-rte-answer-format)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: EPI-OBJ-chat-answer / EPI-OBJ-advisory-result (see inventory).
Content/update relation: truth-apt transformation: non-ampliative reshaping.
Transition or check target: Append existing advisory table and attribution.
Evaluator/condition and domain: Deterministic tool-name/content/marker tests; rendering domain.
Activation and timing: After buffered gate/pre-retrieval, not streaming; operation unobserved.
Possible or observed result: Unchanged answer or appended table/source labels (possible, not an observed event).
Implemented force: Enforcing append conditional on string tests.
Epistemic authority and scope: Attribution to retrieved artifact, no verification of each claim.
Operational authority: Changes displayed answer and subsequent saved/history text.
Behavioral-authority path: Postprocessor to caller, Markdown, enforcing append, this return/later caller reuse.
Evidence source ID and local anchor: see [EPI-RTE-answer-format](#epi-rte-answer-format).
Claim IDs or none: [EPI-CLM-grounding-mandate](#epi-clm-grounding-mandate).
Mismatch marker or none: attribution is not support.
Gap/limit: Marker can suppress table copy even if model table is wrong.

Route ID: [EPI-RTE-verify-check](#epi-rte-verify-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: EPI-OBJ-chat-answer / EPI-OBJ-wiki-pages / EPI-OBJ-verification-report (see inventory).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: Checkable sentence support relative to selected passages.
Evaluator/condition and domain: NLI inference; maximum pair score threshold after lexical/FTS selection; bounded text-pair domain.
Activation and timing: Optional answer/draft/page verification, after candidate exists; operation unobserved.
Possible or observed result: Estimated support report or no checked sentences (possible, not an observed event).
Implemented force: Diagnostic evidence; no text mutation.
Epistemic authority and scope: Classifier-relative source support, not truth, proof or calibrated probability guarantee.
Operational authority: Makes diagnostic available to separate storage/display consumers.
Behavioral-authority path: Verifier core, report object, advisory until consumer, current verification.
Evidence source ID and local anchor: see [EPI-RTE-verify-check](#epi-rte-verify-check).
Claim IDs or none: [EPI-CLM-wiki-maintenance](#epi-clm-wiki-maintenance).
Mismatch marker or none: none.
Gap/limit: Questions, fragments, generated content, citation lines skipped; no context yields no page report.

Route ID: [EPI-RTE-verify-store](#epi-rte-verify-store)
Route function: retention
Architectural status: implemented
Object/candidate ID: EPI-OBJ-verification-report (see inventory).
Content/update relation: no content change.
Transition or check target: Last page report, body/source hashes and evidence excerpts.
Evaluator/condition and domain: Database replacement transaction for page report.
Activation and timing: After page verification, not ordinary answer annotation; operation unobserved.
Possible or observed result: Stored probabilities/hashes/model metadata, or deletion on empty context (possible, not an observed event).
Implemented force: Enforcing report retention only.
Epistemic authority and scope: No new support from storing a score.
Operational authority: Later reading/lint may reclassify at current threshold.
Behavioral-authority path: SQLite verification tables to UI/lint, advisory evidence, until replaced/invalidated.
Evidence source ID and local anchor: see [EPI-RTE-verify-store](#epi-rte-verify-store).
Claim IDs or none: [EPI-CLM-wiki-maintenance](#epi-clm-wiki-maintenance).
Mismatch marker or none: none.
Gap/limit: Retention is not claim acceptance or lifecycle integration.

Route ID: [EPI-RTE-verify-use](#epi-rte-verify-use)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: EPI-OBJ-verification-report (see inventory).
Content/update relation: no content change.
Transition or check target: Diagnostic freshness and unsupported classification.
Evaluator/condition and domain: Hash equality for page/context; current threshold for scores; web rendering for answer report.
Activation and timing: Page read/lint or optional answer verification after original answer display; operation unobserved.
Possible or observed result: Outdated/unverified/unsupported labels and highlights (possible, not an observed event).
Implemented force: Advisory; repair dispatcher skips unsupported/unverified findings.
Epistemic authority and scope: Freshness is license to reuse diagnostic, not endorse underlying assertions.
Operational authority: Warns user; no universal block, deletion or rewrite.
Behavioral-authority path: Web/lint human reader, HTML/report issues, advisory, reading/maintenance horizon.
Evidence source ID and local anchor: see [EPI-RTE-verify-use](#epi-rte-verify-use).
Claim IDs or none: [EPI-CLM-wiki-maintenance](#epi-clm-wiki-maintenance).
Mismatch marker or none: none.
Gap/limit: Changed threshold changes labels without new inference; valid hashes do not imply true sources.

Route ID: [EPI-RTE-contradiction-check](#epi-rte-contradiction-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: EPI-OBJ-lint-issues (see inventory).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: Possible conflict between pages sharing cited source.
Evaluator/condition and domain: LLM compares first 2000 characters per page; prefix parser emits issue.
Activation and timing: Full lint with client, once per selected pair; operation unobserved.
Possible or observed result: Possible contradiction finding or no issue (possible, not an observed event).
Implemented force: Diagnostic issue only.
Epistemic authority and scope: Possible conflict, no adjudication of which assertion is false.
Operational authority: Feeds repair dispatcher/human review.
Behavioral-authority path: Lint to repair/human, LintIssue, advisory before note consumer, maintenance run.
Evidence source ID and local anchor: see [EPI-RTE-contradiction-check](#epi-rte-contradiction-check).
Claim IDs or none: [EPI-CLM-wiki-maintenance](#epi-clm-wiki-maintenance).
Mismatch marker or none: none.
Gap/limit: Shared-source pairing/truncation can miss conflicts; absence of prefix is not consistency proof.

Route ID: [EPI-RTE-contradiction-note](#epi-rte-contradiction-note)
Route function: retention
Architectural status: implemented
Object/candidate ID: EPI-OBJ-lint-issues / EPI-OBJ-wiki-pages (see inventory).
Content/update relation: no content change.
Transition or check target: Persist diagnostic warning rather than resolve conflict.
Evaluator/condition and domain: Handler checks page existence and duplicate marker.
Activation and timing: Repair of contradiction issue; operation unobserved.
Possible or observed result: Warning appended to page A, reference graph updated (possible, not an observed event).
Implemented force: Enforcing note write, advisory note meaning.
Epistemic authority and scope: Retains possible-conflict attribution only.
Operational authority: Future readers/retrieval may encounter warning; disputed prose remains.
Behavioral-authority path: Page body/index to humans/agents, natural-language warning, advisory, later reads.
Evidence source ID and local anchor: see [EPI-RTE-contradiction-note](#epi-rte-contradiction-note).
Claim IDs or none: [EPI-CLM-wiki-maintenance](#epi-clm-wiki-maintenance).
Mismatch marker or none: warning not adjudication.
Gap/limit: No demonstrated changed reliance or next criticism round.

Route ID: [EPI-RTE-gap-check](#epi-rte-gap-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: EPI-OBJ-lint-issues (see inventory).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: Missing/underdeveloped topic relative to concept-title list.
Evaluator/condition and domain: LLM suggestions parsed as GAP lines, FTS picks host.
Activation and timing: Client-enabled lint with nonempty concepts; operation unobserved.
Possible or observed result: Gap candidate associated with host page (possible, not an observed event).
Implemented force: Diagnostic.
Epistemic authority and scope: Topic-undercoverage hypothesis, not missing-fact truth.
Operational authority: Feeds note handler and human acquisition decisions.
Behavioral-authority path: Lint to repair/human, issue object, advisory, maintenance.
Evidence source ID and local anchor: see [EPI-RTE-gap-check](#epi-rte-gap-check).
Claim IDs or none: [EPI-CLM-wiki-maintenance](#epi-clm-wiki-maintenance).
Mismatch marker or none: none.
Gap/limit: Title-only scan cannot certify corpus completeness.

Route ID: [EPI-RTE-gap-note](#epi-rte-gap-note)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: EPI-OBJ-lint-issues / EPI-OBJ-wiki-pages (see inventory).
Content/update relation: no content change.
Transition or check target: TODO retention/removal and replacement by related-page link.
Evaluator/condition and domain: Source FTS hit suppresses new note; marker checks; filled-gap source hit then non-host wiki hit.
Activation and timing: Gap repair or later filled-gap maintenance; operation unobserved.
Possible or observed result: TODO appended, skipped, or replaced by link (possible, not an observed event).
Implemented force: Enforcing marker edits; advisory topic note.
Epistemic authority and scope: Lexical source/page availability, not accepted topic coverage.
Operational authority: Changes future page context without accepting a missing claim.
Behavioral-authority path: Repair to page/index, TODO/link, advisory text and enforcing mutation, later reads.
Evidence source ID and local anchor: see [EPI-RTE-gap-note](#epi-rte-gap-note).
Claim IDs or none: [EPI-CLM-wiki-maintenance](#epi-clm-wiki-maintenance).
Mismatch marker or none: lexical coverage not semantic acceptance.
Gap/limit: Code can remove reminder based on hits without checking that new page resolves it.

Route ID: [EPI-RTE-finance-check](#epi-rte-finance-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: EPI-OBJ-dataset-rows (see inventory).
Content/update relation: no content change.
Transition or check target: Category metrics and required attributes.
Evaluator/condition and domain: Manifest metric presence and attribute type predicates; structured Markdown only.
Activation and timing: At capability construction and advisory call; operation unobserved.
Possible or observed result: Passing/failing categories with reasons (possible, not an observed event).
Implemented force: Validation evidence for selector.
Epistemic authority and scope: Structural suitability for formula domain only.
Operational authority: Feeds tool/category admission.
Behavioral-authority path: Validator to composition/advisory, ValidationReport, enforcing via selector, construction/call.
Evidence source ID and local anchor: see [EPI-RTE-finance-check](#epi-rte-finance-check).
Claim IDs or none: [EPI-CLM-finance-advisory](#epi-clm-finance-advisory).
Mismatch marker or none: none.
Gap/limit: Does not authenticate value, source, quote date or economic assumptions.

Route ID: [EPI-RTE-finance-select](#epi-rte-finance-select)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: EPI-OBJ-dataset-rows (see inventory).
Content/update relation: no content change.
Transition or check target: Passing category and eligible instrument.
Evaluator/condition and domain: Code requires passing category, same currency, minimum amount and available term; branches on method.
Activation and timing: Before projection; tool installation requires some category passing; operation unobserved.
Possible or observed result: Excluded reasons, eligible deterministic inputs, or non-estimable variable list (possible, not an observed event).
Implemented force: Enforcing category/eligibility exclusion.
Epistemic authority and scope: Operational arithmetic admission, not acceptance of source truth.
Operational authority: Blocks ineligible/malformed categories and non-deterministic gain computation.
Behavioral-authority path: Composition/advisory to tools/output, symbolic predicates, enforcing, agent lifetime/call.
Evidence source ID and local anchor: see [EPI-RTE-finance-select](#epi-rte-finance-select).
Claim IDs or none: [EPI-CLM-finance-advisory](#epi-clm-finance-advisory).
Mismatch marker or none: none.
Gap/limit: Model may still describe tool output inaccurately; code gate does not verify generated prose.

Route ID: [EPI-RTE-finance-derive](#epi-rte-finance-derive)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: EPI-OBJ-advisory-result (see inventory).
Content/update relation: truth-apt transformation: entailed derivation.
Transition or check target: Conditional gain and ranking from selected dataset rate and attributes.
Evaluator/condition and domain: Pure TEA/gain formulas; months times 30, 365-day year, constant-rate model.
Activation and timing: After validation/eligibility; operation unobserved.
Possible or observed result: Computed gains sorted descending; variable options separate (possible, not an observed event).
Implemented force: Deterministic computation/ranking.
Epistemic authority and scope: Conditional arithmetic consequence only; premises independently unwarranted.
Operational authority: Computed result can reach model answer and appended table.
Behavioral-authority path: Advisory tool/postprocessor, Markdown with sources/dates, ranking plus enforcing table copy condition, turn.
Evidence source ID and local anchor: see [EPI-RTE-finance-derive](#epi-rte-finance-derive).
Claim IDs or none: [EPI-CLM-finance-advisory](#epi-clm-finance-advisory).
Mismatch marker or none: conditional model not forecast.
Gap/limit: No warranted actual-return prediction or transfer beyond stated assumptions.

Route ID: [RT-RTE-model-evaluation](runtime.md#rt-rte-model-evaluation)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: EPI-OBJ-chat-answer (see inventory).
Content/update relation: no content change.
Transition or check target: Fixed fairy-tale refusal/citation/tool-use suitability.
Evaluator/condition and domain: Script graders and expected answer properties; not production service.
Activation and timing: Operator/installer run, no trace supplied; operation unobserved.
Possible or observed result: Printed verdict/exit status (possible, not an observed event).
Implemented force: Advisory for installer; not launch veto.
Epistemic authority and scope: Proxy suitability for fixed probes, not general correctness.
Operational authority: Installer continues even on failure; human can choose model.
Behavioral-authority path: Installer/operator, exit/text warning, advisory, installation decision.
Evidence source ID and local anchor: see [RT-RTE-model-evaluation](runtime.md#rt-rte-model-evaluation).
Claim IDs or none: [EPI-CLM-grounding-mandate](#epi-clm-grounding-mandate).
Mismatch marker or none: no enforced model admission.
Gap/limit: Model calls bypass production guardrails; script is not training.

Route ID: [EPI-RTE-eval-packet](#epi-rte-eval-packet)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: EPI-OBJ-chat-answer / EPI-OBJ-wiki-pages (see inventory).
Content/update relation: no content change.
Transition or check target: Chat grounding and ingestion faithfulness evaluation material.
Evaluator/condition and domain: Fixed direct-agent probes/citation heuristics and source/generated pairing; external human-mediated judge intended.
Activation and timing: Explicit script call; optional fresh ingest; operation unobserved.
Possible or observed result: Markdown packet with candidate answers/evidence, not returned judge decision (possible, not an observed event).
Implemented force: Advisory packet.
Epistemic authority and scope: Inspectable evaluation inputs only; judge validity/results unobserved.
Operational authority: Human may submit packet to chosen judge and act later.
Behavioral-authority path: Script to operator/external judge, packet, advisory, evaluation session.
Evidence source ID and local anchor: see [EPI-RTE-eval-packet](#epi-rte-eval-packet).
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: No automatic returned verdict consumer or production-policy adaptation established.

Route ID: [EPI-RTE-corpus-freeze](#epi-rte-corpus-freeze)
Route function: retention
Architectural status: implemented
Object/candidate ID: EPI-OBJ-wiki-pages (see inventory).
Content/update relation: no content change.
Transition or check target: Golden source/wiki/database fixture snapshot.
Evaluator/condition and domain: Human inspection is declared protocol; freeze code only checks staging database exists.
Activation and timing: Explicit freeze CLI command; operation unobserved.
Possible or observed result: Fixture files replaced, SQLite dump written (possible, not an observed event).
Implemented force: Enforcing copy, human-review protocol not machine-enforced.
Epistemic authority and scope: Snapshot lineage, not factual certification.
Operational authority: Later regression/evaluation can consume frozen baseline.
Behavioral-authority path: Freeze script to tests/evaluator, fixture files, reference authority by caller convention, later development runs.
Evidence source ID and local anchor: see [EPI-RTE-corpus-freeze](#epi-rte-corpus-freeze).
Claim IDs or none: none.
Mismatch marker or none: freeze not checked acceptance.
Gap/limit: No recorded human decision or particular fixture provenance supplied.

Route ID: [RT-RTE-configure-grants](runtime.md#rt-rte-configure-grants)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: EPI-OBJ-wiki-pages / EPI-OBJ-dataset-rows (see inventory).
Content/update relation: non-truth-apt policy/content update: scope, alias and capability control.
Transition or check target: Future retrieval/admission policy and granted tools.
Evaluator/condition and domain: Human settings/vocabulary edits; model alias proposals plus code collision checks; manifest-based grants.
Activation and timing: Configuration update and later agent construction/reset; operation unobserved.
Possible or observed result: Changed scope/grants or rejected edit (possible, not an observed event).
Implemented force: Code predicates enforcing; prompts advisory.
Epistemic authority and scope: No new proposition truth license from configuration admission.
Operational authority: May change reachable evidence/tool use on later requests.
Behavioral-authority path: Config/dataset files to orchestrator/agent, symbolic predicates/prompt addenda, enforcing/advisory, later constructions.
Evidence source ID and local anchor: see [RT-RTE-configure-grants](runtime.md#rt-rte-configure-grants).
Claim IDs or none: none.
Mismatch marker or none: none.
Gap/limit: Alias identity truth and improved capacity not demonstrated; existing cached agents may persist.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-wiki-compilation](#epi-clm-wiki-compilation) | see record | see record | Extraction/merge prompts request compilation; not factual acceptance | [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest), [RT-RTE-preretrieval-chat](runtime.md#rt-rte-preretrieval-chat) | None supplied | No controlled test of compounding quality; existing prose reused without guarantee of preservation | Generated prose is retained, indexed and reusable; source warrant through generation unknown | Compilation as persistence/reuse supported; accepted new knowledge or improved capacity not established |
| [EPI-CLM-grounding-mandate](#epi-clm-grounding-mandate) | see record | see record | Prompt demands every fact traceable; README names modes and source notes admit proxy limit | [RT-RTE-strict-chat](runtime.md#rt-rte-strict-chat), [RT-RTE-preretrieval-chat](runtime.md#rt-rte-preretrieval-chat), [RT-RTE-streaming-chat](runtime.md#rt-rte-streaming-chat), [EPI-RTE-answer-format](#epi-rte-answer-format), [EPI-RTE-verify-check](#epi-rte-verify-check) | None supplied | Tool presence, lexical overlap and string citation tests do not entail semantic support | Enforced refusal predicates exist in buffered branches; optional semantic classifier is diagnostic | Every-fact grounding remains requested, not guaranteed; unchecked mode is an explicit alternative, not concealed failure |
| [EPI-CLM-wiki-maintenance](#epi-clm-wiki-maintenance) | see record | see record | README explicitly limits unsupported/unverified repairs to reporting | [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance), [EPI-RTE-contradiction-check](#epi-rte-contradiction-check), [EPI-RTE-contradiction-note](#epi-rte-contradiction-note), [EPI-RTE-gap-check](#epi-rte-gap-check), [EPI-RTE-gap-note](#epi-rte-gap-note), [EPI-RTE-verify-use](#epi-rte-verify-use) | None supplied | No repair outcome, recurrence or improvement comparison | Diagnostics, selected automatic mutations and warning persistence are implemented | Does not establish autonomous factual adjudication; some criticism can persist without resolving disputed claims |
| [EPI-CLM-finance-advisory](#epi-clm-finance-advisory) | see record | see record | Constant-rate assumption and non-deterministic exclusion declared in formula/advisory code | [EPI-RTE-finance-check](#epi-rte-finance-check), [EPI-RTE-finance-select](#epi-rte-finance-select), [EPI-RTE-finance-derive](#epi-rte-finance-derive), [EPI-RTE-answer-format](#epi-rte-answer-format) | None supplied | No future-return outcome or financial-data validation experiment | Deterministic conditional computation/ranking over selected rows, not model arithmetic | Source authenticity/recency, semantic encoding and actual return are separate unknowns |
| [RT-CLM-readonly-chat](runtime.md#rt-clm-readonly-chat) | see record | see record | Standard tool grants plus explicit save action | [RT-RTE-configure-grants](runtime.md#rt-rte-configure-grants), [RT-RTE-chat-save](runtime.md#rt-rte-chat-save) | None supplied | No causal evidence; generic extra_tools can expand factory | Standard chat lacks write tool; save is separate | Web review protocol is not every caller's enforced per-claim acceptance. README expressly describes web UI, so marimo difference is a scope limit, not a contradiction of that UI description |

## Bounded conclusion

**Acquisition and reuse.** [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest) acquires source text, generates pages and retains them for later merges and retrieval. [RT-RTE-chat-save](runtime.md#rt-rte-chat-save) retains chat-derived prose through caller-dependent admission. Source identity and citation connections can survive, but neither a citation graph nor a merge request certifies source truth or semantic preservation. The model-mediated edges remain indeterminate among reshaping, entailment and conjecture without content-level input/output evidence. They cannot be called produced accepted ampliative knowledge merely because pages exist.

**Checks and permission.** [RT-RTE-strict-chat](runtime.md#rt-rte-strict-chat) gates operational return on a substantive tool-result proxy. [RT-RTE-preretrieval-chat](runtime.md#rt-rte-preretrieval-chat) adds code-controlled context/scope and branch-specific lexical checks; [RT-RTE-streaming-chat](runtime.md#rt-rte-streaming-chat) emits without those final checks. The license is retrieval/coverage under those predicates, not answer entailment. [EPI-RTE-answer-format](#epi-rte-answer-format) can force existing table/attribution text into an answer; it does not establish each claim's support. These are materially different force paths, not a single oracle.

**Verification and criticism.** [EPI-RTE-verify-check](#epi-rte-verify-check) estimates support of selected checkable sentences relative to selected/truncated passages. [EPI-RTE-verify-store](#epi-rte-verify-store) retains page diagnostics; [EPI-RTE-verify-use](#epi-rte-verify-use) consumes hashes/current thresholds to warn or highlight. No page rewrite, answer withdrawal or universal save/retrieval veto follows from an unsupported label in these inspected consumers. [EPI-RTE-contradiction-note](#epi-rte-contradiction-note) preserves possible conflict rather than deciding which proposition to reject. [EPI-RTE-gap-note](#epi-rte-gap-note) can replace a reminder with a related link using lexical availability. These are maintenance effects before any demonstrated evidence-consuming acceptance, not lifecycle integration after it.

**Derivation.** [EPI-RTE-finance-derive](#epi-rte-finance-derive) derives conditional projections and ranks from formula inputs; [EPI-RTE-finance-check](#epi-rte-finance-check) and [EPI-RTE-finance-select](#epi-rte-finance-select) enforce structural and eligibility prerequisites. No independently warranted source premises are supplied: the warranted conclusion is the implementation's arithmetic consequence under its encoding and constant-rate assumption, not future profit. The ranking can shape advice, and a postprocessor can append the table, without warranting surrounding generated prose.

**Acceptance, iteration and limits.** In inspected ingestion and save admissions, nonempty/format/job predicates and optional human review do not amount to a recorded evidence-consuming decision against a named truth criterion, intended use and scope. Diagnosis and retained warning material can support criticism infrastructure; no supplied record establishes localized formulated theory content, content-dependent consumption, blame-assigned criticism with revision/reliance change, and iterative reuse as one completed theory-builder chain. Model opacity establishes neither hidden presence nor absence of those properties. [RT-RTE-configure-grants](runtime.md#rt-rte-configure-grants) changes future scope and capability policy directly; this capacity is independent of accepted truth-apt production. Retained pages/settings can affect later operations with fixed generation weights. Learning as improved future capacity, reflection's two causal directions, autonomy across every internal role, and exercised self-improvement each require their own evidence; none follows simply from compilation, diagnostics or user-started auto-repair. No system-complete negative follows either: the named uninspected evaluator/maintenance internals remain coverage limits. No observed-run or causal evidence demonstrates improvement or activation benefit for these paths.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-source-text
Label: Extracted document text

Source-native identity: `document_pages`, source `documents` and indexed chunks. Natural-language assertions on source files/SQLite; IDs and page metadata are symbolic lineage, not independent warrant. Producer is extraction; consumers are model ingestion, raw retrieval and page verification. Distinct object in the supplied [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest) route, which declares no object counterpart. Evidence: SRC-1, `base/domain/verify/page.py` and supplied ingest record. Text accuracy against the original file is uninspected.

> "SELECT content FROM document_pages WHERE document_id = ? ORDER BY page", (doc_id,),
> --- `base/domain/verify/page.py`

#### EPI-OBJ-wiki-pages
Label: Retained wiki prose

Source-native identity: summary/concept/overview Markdown and saved chat pages, natural-language bodies on filesystem with SQLite content/chunks/references. Symbolic slugs/frontmatter select consumers but do not turn prose into fixed-rule truth. The distinct checks/consumers of diagnostic notes, generated answer prose and data are split below. No object counterpart was declared in runtime; overlap is the state carried by [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest), [RT-RTE-chat-save](runtime.md#rt-rte-chat-save) and [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance), whose passages supply write/read-back evidence. Existing bodies are input to later concept/chat merges. Source warrant after generation is unknown, not preserved merely by source metadata. SRC-1, `base/domain/ingestion/wiki_generator.py`:

> _, existing_body = split_frontmatter(existing_content)
>         user_msg = load_prompt("concept_update_template", language).format(
>             name=concept.name,
>             filename=filename,
>             insight=concept.insight,
>             existing=existing_body,
>         )
> --- `base/domain/ingestion/wiki_generator.py`

#### EPI-OBJ-chat-answer
Label: Chat response text

Source-native identity: `ChatResult.answer`, model output or substituted refusal; natural-language Markdown in application-held turn history, optionally promoted to wiki via save. The code-appended advisory table is a separate calculated object below. No runtime object counterpart; see [RT-RTE-preretrieval-chat](runtime.md#rt-rte-preretrieval-chat), [RT-RTE-strict-chat](runtime.md#rt-rte-strict-chat), [RT-RTE-streaming-chat](runtime.md#rt-rte-streaming-chat) for underlying evidence and distinct consumers. SRC-1, `base/services/chat.py`. Current-turn claim meaning and provenance cannot be reconstructed from an implementation alone.

#### EPI-OBJ-verification-report
Label: VerificationReport and stored verification

Source-native identity: sentence text/offsets, best passage/source, numerical support scores, model identity, body and source hashes in `VerificationReport`, `page_verifications` and `verification_sentences`. Sentence/excerpt meaning is natural-language; offsets, hashes, thresholds and comparison are symbolic; numerical scores are classifier outputs, not a second trainable component. SQLite persists page results; answer/draft reports can be transient UI inputs. Distinct diagnostic object, not the generated content or [RT-CMP-local-nli-verifier](runtime.md#rt-cmp-local-nli-verifier) that scores it. No supplied object counterpart. Evidence: SRC-1, `base/domain/verify/core.py`, `base/domain/verify/store.py`.

> supported=score >= threshold, probability=score,
>             page=passage.page if passage else None,
>             passage=passage.text if passage else None,
> --- `base/domain/verify/core.py`

#### EPI-OBJ-lint-issues
Label: LintIssue diagnostics and retained notes

Source-native identity: `LintIssue` fields with natural-language conflict/gap descriptions and symbolic check/page/topic keys, transient `LintReport` then selected warning/TODO text on wiki pages. Descriptions are candidate diagnoses; check keys dispatch repair. Distinct from content being criticized and from numerical verification reports. No object counterpart after comparison with [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance). Evidence: SRC-1, `base/domain/lint/checks.py`, `base/domain/repair/actions.py`.

> description=(
>                     f"Possible contradiction with '{pair['path_b']}': {detail}"
>                 ),
> --- `base/domain/lint/checks.py`

#### EPI-OBJ-dataset-rows
Label: DatasetRow and category attributes

Source-native identity: normalized `DatasetRow` values/metric/key/dimensions/date/source and category frontmatter attributes from `datasets/<categoria>.md`. Symbolic records encode truth-apt measurements/attributions and calculation policies; files are reparsed on each query, not a trained vector store. Human/workspace file changes provide inputs; query tools, validator and arithmetic consume them. Distinct data object underlying the supplied [RT-RTE-configure-grants](runtime.md#rt-rte-configure-grants), with no object counterpart. Evidence: SRC-1, `base/domain/datasets/source.py`. Parser validation and external provenance are not interchangeable.

> rows = self._rows_for_file(path)
>         if clave is not None:
>             rows = [r for r in rows if r.clave == clave]
> --- `base/domain/datasets/source.py`

#### EPI-OBJ-advisory-result
Label: AdvisoryResult

Source-native identity: `AdvisoryResult`/`RankedOption` values and rendered Markdown. Symbolic gains/rank/date/source fields in current-call memory, interpreted by the model/human as conditional financial assertions; Markdown output may later enter chat history/wiki. This is derived output, not imported `DatasetRow` or arbitrary model prose. No counterpart in supplied runtime; it expands finance processing mentioned in [RT-RTE-configure-grants](runtime.md#rt-rte-configure-grants). Evidence: SRC-1, `base/domain/finance_argentina/advisory.py`.

> gain = projected_gain(amount, rate_tea, horizon_days)
>     return RankedOption(
>         categoria=categoria,
>         clave=row.clave,
>         term_label=term_label,
>         tea=rate_tea,
>         gain=gain,
>         as_of=row.as_of.isoformat(),
>         fuente=row.fuente,
>     )
> --- `base/domain/finance_argentina/advisory.py`

### Routes

#### EPI-RTE-answer-format
Label: Deterministic answer formatting

Distinct identity: no counterpart after comparison with the supplied runtime records; this route adds a separately scoped operation.

Endpoints/progression and owner: tool-message log and answer → pure postprocessors → returned Markdown. Code owns append decisions; runtime strict/pre-retrieval routes are consumers, not duplicate identities. Evidence: SRC-1, `base/domain/chat/postprocess.py` (implementation).

- Immediate return: Answer unchanged or table/attribution appended
- Later read-back: Caller-held text may later enter history/save; no direct durable write here
- Delegated visibility: inapplicable — no model is called by these pure functions
- Selection predicate: Last substantive advisory return and absence of table marker; deliberate page/data sources for citations
- Invalidation or expiry: Recomputed per return; no persistent formatting state
- Activation or effect: Conditionally alters returned text; no exercised compliance established
- Evidence limits: String tests do not validate model table or claim-source correspondence
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete deduction, not target execution: with answer `A`, a last substantive advisory return `T`, and no table marker in `A`, `answer_with_table` returns `A` plus two newlines plus `T`. If `A` merely contains the literal marker `| opción`, the function returns `A` even when its table values differ from `T`. Thus a copying guarantee is conditional on a marker test, not semantic equality. Similarly `enforce_grounding` returns any output when one substantive tool return exists; the inspected implementation does not compare answer text to the result. This countercase qualifies, rather than denies, the implemented output gate. SRC-1, `base/domain/chat/guardrail.py`. The source-native claim is read with its acknowledged limitation.

> if _ADVISORY_TABLE_MARKER in answer:
>         return answer  # model already pasted a table — no duplicate
>     return f"{answer.rstrip()}\n\n{table}"
> --- `base/domain/chat/postprocess.py`

#### EPI-RTE-verify-check
Label: Sentence support computation

Distinct identity: no counterpart after comparison with the supplied runtime records; this route adds a separately scoped operation.

Endpoints/progression and owner: answer/page body and resolved context → sentence filtering/passage selection → verifier pairs → maximum-score report. Code selects pairs and threshold; supplied verifier judges pair entailment. Evidence: SRC-1, `base/domain/verify/core.py` (implementation).

- Immediate return: VerificationReport; page path may instead report no context
- Later read-back: inapplicable — computation alone retains nothing; page storage is separate
- Delegated visibility: NLI receives selected passage/sentence text, not entire source/workspace
- Selection predicate: Checkability filter; lexical top six by default, or caller-selected FTS candidates; split passage maximum
- Invalidation or expiry: Recompute on explicit verification; report validity handled separately
- Activation or effect: Produces per-sentence support estimates, not candidate mutation
- Evidence limits: No calibration/run evidence; omitted sentences and truncated premises limit checked domain
- implementation conclusion status: wired
- operation conclusion status: uninspected

Proposer: answer/page generation or editor; evaluator: classifier plus selection/threshold code; caller can withhold verification. Open diagnostic request, not candidate tournament. Sources are premises, not independent reference answers. No rollback needed because this function does not change content. Distinct from the verifier component and from the web/runtime routes that invoke and consume the result. Related [RT-CMP-local-nli-verifier](runtime.md#rt-cmp-local-nli-verifier). SRC-1, `base/domain/verify/checkable.py`, `base/domain/verify/nli.py`: generated blocks, questions, citations and short fragments are excluded; tokenizer truncates premise only. Changing source truth without changing the text will not be detected.

> scores = verifier.entailment(pairs) if pairs else []
>     if len(scores) != len(pairs):
>         raise ValueError(f"the verifier returned {len(scores)} scores for {len(pairs)} pairs")
> --- `base/domain/verify/core.py`

#### EPI-RTE-verify-store
Label: Page verification retention

Distinct identity: no counterpart after comparison with the supplied runtime records; this route adds a separately scoped operation.

Endpoints/progression and owner: page verification → save_verification → SQLite last-report rows. Page verifier resolves context and code owns report replacement. Evidence: SRC-1, `base/domain/verify/page.py` (implementation).

- Immediate return: PageOutcome/report or no-context outcome
- Later read-back: Reading screen/lint consumes stored scores and hashes at later invocation
- Delegated visibility: inapplicable — database writes delegate no semantic evaluation
- Selection predicate: Page exists/indexed; nonempty context; replace previous report for same document
- Invalidation or expiry: Body/source changes make report outdated; new report replaces; empty context deletes
- Activation or effect: Stores diagnostics and bounded excerpts, not edited page prose
- Evidence limits: Storage transaction does not certify source truth or report calibration
- implementation conclusion status: wired
- operation conclusion status: uninspected

Distinct diagnostic persistence absent from the runtime route inventory. SRC-1, `base/domain/verify/store.py`: one report per page, maximum 300-character normalized excerpt; raw probabilities persist so current threshold can reclassify without inference. This retention must not be merged with lifecycle integration of accepted claims.

> if context.empty:
>             store.delete_verification(conn, row["id"])
>             conn.commit()
>             return PageOutcome(relative_path, context.kind, None)
> --- `base/domain/verify/page.py`

#### EPI-RTE-verify-use
Label: Verification diagnostic consumption

Distinct identity: no counterpart after comparison with the supplied runtime records; this route adds a separately scoped operation.

Endpoints/progression and owner: report/hash state → web highlights or lint issue → human; repair dispatcher skips diagnostic-only checks. Code owns freshness/classification/rendering; humans may edit separately. Evidence: SRC-1, `base/domain/lint/checks.py` (implementation).

- Immediate return: Answer highlighting/summary or unverified/unsupported page issues
- Later read-back: Stored page report can be reused at later page/lint calls; answer display itself changes no wiki
- Delegated visibility: Human sees marked sentences; no rewrite model receives a forced correction
- Selection predicate: Hash match and current threshold for page labels; user-enabled answer verification
- Invalidation or expiry: Hash mismatch invalidates diagnostic; threshold changes classification without recomputation
- Activation or effect: Advisory visibility, no universal save/retrieval blocking or claim deletion
- Evidence limits: No human response, changed reliance or successful correction observed
- implementation conclusion status: wired
- operation conclusion status: uninspected

Diagnosis mode is open inspection. Code marks/proposes an issue; user may ignore it; no truth oracle adjudicates source reliability. Compared with [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance), this spans page diagnostics and separate chat rendering rather than being a part of exactly one runtime container. SRC-1, `web/routes/chat.py`: full answer is appended to history and displayed before optional report highlighting; verification exceptions leave original answer. SRC-1, `base/domain/verify/store.py`: body/source hash equality yields `VALID`, not semantic endorsement.

> if state is not State.VALID:
>             continue
>         weak = stored.unsupported(threshold)
> --- `base/domain/lint/checks.py`

> # `unsupported_sentences` and `unverified_pages` are report only: nothing deletes
> # or rewrites a sentence of a page, and verifying a page is an action of its own.
> --- `base/domain/repair/runner.py`

#### EPI-RTE-contradiction-check
Label: Related-page contradiction check

Part of: [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance)

Endpoints/progression and owner: shared-source page pairs → truncated prompt → LLM text → parsed issue. Model proposes conflict; code selects pairs/parses prefix. Evidence: SRC-1, `base/domain/lint/checks.py` (implementation).

- Immediate return: Possible-contradiction LintIssue list
- Later read-back: inapplicable — immediate issue list is not durable until separate note action
- Delegated visibility: First 2000 characters of each selected page
- Selection predicate: Pairs share a cites edge; client supplied; result starts CONTRADICTION
- Invalidation or expiry: New sweep can produce different diagnoses; no consistency certificate
- Activation or effect: Feeds warning repair and human report
- Evidence limits: No checked conflict outcome, source adjudication or run evidence
- implementation conclusion status: wired
- operation conclusion status: uninspected

Computation performs candidate criticism in a user-started/full-lint mode, but model judgment alone is not an answer oracle. User can withhold full lint; code accepts prefix, not a proof. Inputs truncated before judgment can omit scope conditions that reconcile apparent disagreement.

> content_a=(pair["content_a"] or "")[:2000],
>             path_b=pair["path_b"],
>             content_b=(pair["content_b"] or "")[:2000],
> --- `base/domain/lint/checks.py`

#### EPI-RTE-contradiction-note
Label: Contradiction warning retention

Part of: [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance)

Endpoints/progression and owner: contradiction issue → append warning to page A → rebuild references. Deterministic handler writes diagnostic, not conflict resolution. Evidence: SRC-1, `base/domain/repair/actions.py` (implementation).

- Immediate return: RepairResult flagged/skipped/failed
- Later read-back: Warning becomes page text available to future human/retrieval/model consumption
- Delegated visibility: inapplicable — this handler does not call a model
- Selection predicate: Existing page and absent per-pair marker
- Invalidation or expiry: Marker suppresses duplicate; later editing/restoration can remove note
- Activation or effect: Persists possible-conflict description; original challenged claims remain
- Evidence limits: Delivery of note does not establish changed reliance
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission follows selected issue, page existence and marker. Code proposes/decides note text using issue description; human can withhold repair or later edit/restore, but does not approve each note. No reference-answer oracle or automatic choice of true page. The retained criticism is distinct from acceptance or theory revision.

> f"> ⚠️ **Possible contradiction** with [{b_path}]({rel}): {detail}\n"
>         f"> Review both pages and resolve the conflicting claims."
> --- `base/domain/repair/actions.py`

#### EPI-RTE-gap-check
Label: Title-list gap diagnosis

Part of: [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance)

Endpoints/progression and owner: concept titles → model suggestions → GAP parser → FTS-selected host. Model proposes missing topic; code decides parsable/hosted issue. Evidence: SRC-1, `base/domain/lint/checks.py` (implementation).

- Immediate return: Data-gap issues or empty list
- Later read-back: inapplicable — no durable write in check
- Delegated visibility: Concept titles/paths, not full source corpus
- Selection predicate: Client and nonempty concept list; GAP line with topic and host FTS hit
- Invalidation or expiry: Recomputed on sweep; no stable guarantee of completeness
- Activation or effect: May cause note repair or human source acquisition
- Evidence limits: No verified missing fact or corpus-completeness measure
- implementation conclusion status: wired
- operation conclusion status: uninspected

Open maintenance request, not curriculum. Human may withhold job; model has no independent answer key. Its suggestion can exceed content entailed by a title list, but no observed output is supplied to classify a particular proposition as ampliative.

> messages=[{"role": "user", "content": load_prompt("lint_gap_template", language).format(concept_list=concept_list)}],
> --- `base/domain/lint/checks.py`

#### EPI-RTE-gap-note
Label: Gap reminder lifecycle

Part of: [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance)

Endpoints/progression and owner: gap/filled-gap issues → marker/source checks → append TODO or replace with page link. Code chooses mutation; model-supplied suggestion remains advisory. Evidence: SRC-1, `base/domain/repair/actions.py` (implementation).

- Immediate return: RepairResult for note insertion/skipping or gap-resolved link
- Later read-back: TODO/link stored on page for future reads; later sweep consumes marker
- Delegated visibility: inapplicable — no new model call in these handlers
- Selection predicate: Missing source FTS hit permits note; filled-gap needs source hit then a non-host wiki hit, concepts preferred
- Invalidation or expiry: Marker idempotency; link replacement removes gap block
- Activation or effect: Changes retained reminder based on lexical availability
- Evidence limits: Topic-match hit does not prove new source resolves old gap
- implementation conclusion status: wired
- operation conclusion status: uninspected

The earlier model suggests; handler decides under lexical predicates; user may withhold maintenance and edit/restore later. No per-note human truth approval. This joins warning retention and recovery of that warning because its operative object is the reminder, not an accepted proposition. The filled-gap check is SRC-1, `base/domain/lint/checks.py`; the replacement action preserves other body text.

> if query and search_chunks(db_path, query, limit=1, scope="sources"):
>         return RepairResult(
>             check="data_gap", page=issue.page,
>             action="skipped", success=True,
>             message=f"topic '{slug}' already covered by a source",
>         )
> --- `base/domain/repair/actions.py`

#### EPI-RTE-finance-check
Label: Finance structural validation

Distinct identity: validation is reused both within [RT-RTE-configure-grants](runtime.md#rt-rte-configure-grants) construction and during advisory calls; this shared operation is not wholly contained in one supplied route.

Endpoints/progression and owner: requirements manifest and DatasetSource → required metric/attribute checks → ValidationReport. Code owns Boolean category results/reasons; no model judgment. Evidence: SRC-1, `base/domain/finance_argentina/validator.py` (implementation).

- Immediate return: Passing/failing category list
- Later read-back: inapplicable — validation report is per-call state, not retained candidate history
- Delegated visibility: inapplicable — validator does not call a model
- Selection predicate: Required metric presence and required well-typed attributes in structured files
- Invalidation or expiry: Recomputed as files/config change; no stable value snapshot promised
- Activation or effect: Produces evidence for tool/category exclusion
- Evidence limits: Checks presence/types, not authenticity/recency/financial truth
- implementation conclusion status: wired
- operation conclusion status: uninspected

This shared finance-validation operation is called both by the supplied composition route and advisory execution. Human/file authors supply candidate rows/attributes, manifest is the criterion; code decides validity and downstream consumer may exclude. No independent answer oracle. File replacement or configuration/history restore is external recovery, not a validator rollback.

> reasons.extend(_check_dataset(categoria, spec.metricas, dataset_source))
>         reasons.extend(_check_attributes(categoria, spec.attributes, dataset_source))
>
>         ok = not reasons
> --- `base/domain/finance_argentina/validator.py`

#### EPI-RTE-finance-select
Label: Finance category and instrument admission

Distinct identity: no counterpart after comparison with the supplied runtime records; this route adds a separately scoped operation.

Endpoints/progression and owner: validation report and user amount/horizon/currency → category/eligibility/method dispatch → estimable or variable options. Code decides arithmetic eligibility; not model installation choice. Evidence: SRC-1, `base/domain/finance_argentina/advisory.py` (implementation).

- Immediate return: Eligible inputs, exclusions and separate variable options
- Later read-back: inapplicable — no persistent row/history modification
- Delegated visibility: Later tool-rendered result goes to answer agent, not private validator state
- Selection predicate: Passing category; currency/minimum/term checks; no deterministic gain for no_deterministico
- Invalidation or expiry: Each advisory call revalidates; rows are current files
- Activation or effect: Blocks unsuitable inputs and non-deterministic estimates
- Evidence limits: No factual acceptance of measurements or investment-outcome validation
- implementation conclusion status: wired
- operation conclusion status: uninspected

Distinct operational selector overlaps [RT-RTE-configure-grants](runtime.md#rt-rte-configure-grants) at tool construction and production chat consumption at invocation, rather than being wholly contained in one supplied route. User requests advice and can reject use; manifest/attributes guide computational admission. It may be disabled at construction if no category passes. No reference-answer oracle, candidate tournament or automatic model-policy training.

> for categoria in validation.passing:
>         attrs = _read_attrs(dataset_source, categoria)
>         if not _is_eligible(attrs, amount, horizon_days, moneda):
>             continue
> --- `base/domain/finance_argentina/advisory.py`

#### EPI-RTE-finance-derive
Label: Conditional financial projection

Distinct identity: no counterpart after comparison with the supplied runtime records; this route adds a separately scoped operation.

Endpoints/progression and owner: selected rate rows/attributes → TEA → projected_gain → gain sort/rendered advisory. Pure Python owns arithmetic/ranking; model owns only surrounding explanation. Evidence: SRC-1, `base/domain/finance_argentina/formulae.py` (implementation).

- Immediate return: Ranked deterministic options with source/date; variable options separate
- Later read-back: Caller can retain rendered result in chat and explicitly save; no training write
- Delegated visibility: Tool output conveys numbers/assumptions to model/human
- Selection predicate: Selected metric/rate/term and calculation method from previous selector
- Invalidation or expiry: Recomputed from latest file contents and request
- Activation or effect: Produces conditional gains and rank; table copy consumer may force display
- Evidence limits: No actual-return or accurate-source premise established
- implementation conclusion status: wired
- operation conclusion status: uninspected

No counterpart in runtime after comparison with the finance grant container and chat consumers: this operation is numerical inference, not grant admission. Concrete static deduction: `projected_gain(100, 0, 365)` evaluates to `100 * ((1 + 0) ** (365 / 365) - 1)`, hence zero under ordinary finite arithmetic. This follows from the inspected formula, not an executed target run. General projections follow the declared constant-rate model; source truth, encoding of a quoted rate and future stationarity are additional premises. SRC-1, `base/domain/finance_argentina/advisory.py`: horizon is round(months times 30), gains sort descending, no model arithmetic. Code can reject unknown/non-deterministic methods through ValueError; tool/display downstream still matters.

> return principal * ((1 + tea_value) ** (horizon_days / _DAYS_PER_YEAR) - 1)
> --- `base/domain/finance_argentina/formulae.py`

> ranked.sort(key=lambda opt: opt.gain, reverse=True)
> --- `base/domain/finance_argentina/advisory.py`

#### EPI-RTE-eval-packet
Label: Human-mediated evaluation packet

Distinct identity: no counterpart after comparison with the supplied runtime records; this route adds a separately scoped operation.

Endpoints/progression and owner: CLI fixed probes/direct agent and optional fresh ingest → candidate/evidence bundle → operator-selected judge. Script captures outputs/proxy checks; human mediates external judging. Evidence: SRC-1, `scripts/build_eval_packet.py` (implementation).

- Immediate return: Markdown evaluation packet, not machine-consumed final truth verdict
- Later read-back: uninspected — no retained judge result to later production-policy update inspected
- Delegated visibility: Candidate answers and resolved cited evidence intended for separately chosen judge
- Selection predicate: Fixed probes/intent; CLI can omit chat/ingestion or select wiki
- Invalidation or expiry: New packet generation can supersede evidence; no output-quality expiry checked
- Activation or effect: Provides inspection material; no observed evaluation or automatic correction
- Evidence limits: Reader/rubric internals and external judge behavior uninspected
- implementation conclusion status: wired
- operation conclusion status: uninspected

Distinct from [RT-RTE-model-evaluation](runtime.md#rt-rte-model-evaluation): this prepares ingestion and chat evidence for a human-mediated external grader, rather than only computing suitability exit status. Bounded evaluation mode, not open production. Script author provides expected probe intents; direct agent proposes answers; proxy graders check citation/leak shape. No enforced production admission, automatic successor selection or reference truth oracle follows. Packet collection is not causal isolation merely because source comments say isolates: no executed intervention/control is supplied.

> answer = agent.run_sync(question, deps=db_path).output
> --- `scripts/build_eval_packet.py`

#### EPI-RTE-corpus-freeze
Label: Golden fixture freezing

Distinct identity: no counterpart after comparison with the supplied runtime records; this route adds a separately scoped operation.

Endpoints/progression and owner: explicit build/verify/freeze CLI → copy staging sources/wiki/database and dump → golden fixture. Operator chooses freeze; code executes snapshot and replacement. Evidence: SRC-1, `scripts/build_golden_corpus.py` (implementation).

- Immediate return: Copied files/database plus human-auditable dump
- Later read-back: Regression tests/eval script later consume frozen fixture as reference
- Delegated visibility: Human can inspect staging pages and dump; no model called by freeze
- Selection predicate: Only database existence checked by freeze; earlier report/human review not enforced
- Invalidation or expiry: Existing golden directory is replaced; repository history external to freeze can recover previous fixture
- Activation or effect: Installs baseline for later tests, not evidence-consuming factual approval
- Evidence limits: No supplied human decision or provenance/run record establishes acceptance
- implementation conclusion status: wired
- operation conclusion status: uninspected

Distinct from production [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest) and model suitability evaluation: this changes developer reference data. Human review is a source-native protocol; software freeze does not require verify success or signed review. Operator can withhold/change snapshot. Tests use structural invariants of frozen state, which cannot establish all generated prose true. No curriculum or automatic training update is established.

> if _GOLDEN.exists():
>         shutil.rmtree(_GOLDEN)
>     _GOLDEN.mkdir(parents=True)
>
>     shutil.copytree(_STAGING / "sources", _GOLDEN / "sources")
>     shutil.copytree(_STAGING / "wiki", _GOLDEN / "wiki")
> --- `scripts/build_golden_corpus.py`

### Claims

#### EPI-CLM-wiki-compilation
Label: Compile knowledge once

Claimed operation: retained concept knowledge avoids rebuilding from raw chunks for each query. SRC-1, `README.md` (doctrine/design). Distinct from runtime's read-only claim: this concerns retained knowledge/reuse. Implemented retention/retrieval supports reuse, not independently accepted novel truths or demonstrated compounding quality.

> LLM Wiki **compiles knowledge once and keeps it current**. Each ingested source
> --- `README.md`

#### EPI-CLM-grounding-mandate
Label: Traceable every-fact grounding

Claimed operation: every factual answer comes from retrieved wiki/source content and carries citation; deterministic post-check prevents background-only answering. SRC-1, `prompts/system_prompt.en.md`, `README.md` (doctrine/design). Distinct from [RT-CLM-readonly-chat](runtime.md#rt-clm-readonly-chat), which concerns write grants. Counterevidence was sought in guardrail, pre-retrieval and streaming: the source itself documents the proxy limitation and unchecked mode. Thus stronger entailment is requested, not proved. Prompt wording is not an implementation guarantee.

> You are a personal knowledge-base assistant. You answer **only** from the user's own wiki and source documents — never from your own background knowledge. The entire point of this wiki is traceability: every fact you state must come from a retrieved page and carry a citation, so the user can verify it.
> --- `prompts/system_prompt.en.md`

> - Known limitation: this catches answers with NO grounding evidence (the common,
>   egregious leak). It does not catch an answer that ignored a result it did
>   retrieve; that needs answer-vs-source verification (future work).
> --- `base/domain/chat/guardrail.py`

#### EPI-CLM-wiki-maintenance
Label: Self-maintaining wiki

Claimed operation: diagnostic lint checks and automatic safe repairs, explicitly not automatic rewriting of unsupported sentences or unverified pages. SRC-1, `README.md` (doctrine/design). No matching runtime claim; related [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) implements its container. Read with named diagnostics/repair consumers, not as a claim that every conflict is adjudicated.

> - **Self-maintaining wiki** — twelve lint checks (contradictions, stale pages, orphans, missing concepts, missing cross-refs, data gaps, filled gaps, vocabulary drift, thin pages, sources that produced no page, sentences with no support in the sources, pages with no valid verification) with auto-repair of the safe ones. The last two are report only: they list the unsupported sentences of a verified page and the pages that need verification, and nothing rewrites the text.
> --- `README.md`

#### EPI-CLM-finance-advisory
Label: Deterministic grounded advisory

Claimed operation: pure-Python gain math/eligibility ranks cited alternatives and refuses non-deterministic estimates. SRC-1, `README.md` (doctrine/design). No runtime claim counterpart; related [RT-RTE-configure-grants](runtime.md#rt-rte-configure-grants) only describes grant activation. The inspected implementation supports conditional arithmetic, not future-rate constancy or externally verified measurements.

> - **Deterministic, grounded advisory** — the example `finance_argentina` overlay computes "what would I earn" over those datasets in pure Python (effective-rate math, eligibility), lists every option ranked and cited, and refuses to estimate the non-deterministic (equities, inflation, FX) rather than fabricating a number.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; route-specific consumers, channels, force and horizons are in the ledger. Shared chat prompt/configuration delivery is see [RT-BAP-chat-instructions](runtime.md#rt-bap-chat-instructions).
