---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "cass_memory_system epistemic routes: historical evidence heuristics, model judgment, retained guidance and feedback-driven authority at the frozen revision"
run-id: AAS-2026-10-13-cass-memory-system-30c18219cf68-01
reviewed-boundary: "8aca3bbb6732321dca041b32c155617784687897"
---

# cass_memory_system epistemic report

## Source-and-claim boundary

This report asks what licenses reliance on CM's session-derived rules, how checks change their admission or later use, and whether claimed validation and learning exceed the inspected routes. Scope and external exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identity and layers are see [Source register](boundary.md#source-register). All added inspection uses SRC-1 at the frozen commit. Source implementation and target-authored doctrine are available; no execution, populated deployment corpus, provider internals or causal experiment is supplied. Accordingly no row reports observed operation.

Truth-apt parts include session assertions, diary descriptions, rule-support judgments and any conditional effectiveness claim expressed or implied by a rule. A bare imperative can instead be policy, and a corpus of actual generated rules was not supplied. Individual rule truth-aptness is therefore not determinable from the instruction schema alone. Scoring and regex policy remain assessable without treating every imperative as a proposition.

Claims under assessment are [EPI-CLM-scientific-validation](#epi-clm-scientific-validation), [EPI-CLM-pattern-learning](#epi-clm-pattern-learning), [RT-CLM-automatic-learning](runtime.md#rt-clm-automatic-learning) and [RT-CLM-rule-criticism](runtime.md#rt-clm-rule-criticism). Missing transcript-to-candidate-to-verdict traces prevent establishing faithful extraction or accepted candidate instances. Missing later agent traces prevent behavioral activation; missing controlled outcomes prevent useful learning and component attribution. External cass and originating-agent evidence would be needed to establish historical completeness and source truth. Provider response/version evidence would be needed for generation quality and immutable model identity.

### Coverage

Direct reads below are bounded selected ranges, not complete file audits. Supplied runtime findings are explicitly distinguished. The CLI registration search covered SRC-1 `src/cm.ts`; runtime supplied the HTTP tools and hook dispatch account. Available but uninspected operations preclude a system-complete negative about knowledge production or acceptance.

| Entry point or operation | Source path | Coverage and records; limit |
|---|---|---|
| context, similar, project export; HTTP context/search/resources | SRC-1 `src/commands/context.ts`, `src/commands/serve.ts`, `src/commands/project.ts` | Supplied [RT-RTE-context-read](runtime.md#rt-rte-context-read), [RT-RTE-http-tools](runtime.md#rt-rte-http-tools). Similar and full resource/export transforms not independently read; semantic completeness beyond supplied projection remains unassessed. |
| reflect; HTTP memory_reflect; session-end hook | SRC-1 `src/orchestrator.ts`, `src/llm.ts`, `src/validate.ts`, `src/curate.ts`, `src/commands/hook.ts` | Direct prompt, validation, refinement handoff, replacement/merge/inversion/maturity reads; correction also traces valid-delta collection through curation/save, new-add source-session/reason retention and later reflection/context consumers; supplied [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update). Added checks and dispositions are [EPI-RTE-evidence-check](#epi-rte-evidence-check), [EPI-RTE-validation-disposition](#epi-rte-validation-disposition). |
| diary / fast extraction | SRC-1 `src/diary.ts`, `src/llm.ts` | Direct outcome inference and fast diary assembly; [EPI-RTE-diary-inference](#epi-rte-diary-inference). Model prompt directly read; schema and retention supplied by runtime. Exact model-output preservation not established. |
| onboard; playbook add / batch; starters / quickstart | SRC-1 `src/commands/onboard.ts`, `src/commands/playbook.ts`, `src/rule-validation.ts`, `src/starters.ts` | Supplied [RT-RTE-onboard-add](runtime.md#rt-rte-onboard-add); direct quality heuristics. Starter expansion and full batch implementation not independently inspected; cannot extend reflection's evidence gate to these admissions. |
| playbook import/export/conflicts | SRC-1 `src/commands/playbook.ts`, `src/curate.ts` | Direct schema/defaults, replacement, similarity/feedback merge and warning-after-import reads; [EPI-RTE-playbook-import](#epi-rte-playbook-import). Export evidence supplied only; heuristic conflict parser read, not proof of logical incompatibility. |
| validate | SRC-1 `src/commands/validate.ts` | Direct whole command; [EPI-RTE-standalone-validate](#epi-rte-standalone-validate). Printed verdict has no inspected automatic persistence consumer. |
| mark; HTTP feedback | SRC-1 `src/commands/mark.ts`, `src/scoring.ts` | Supplied [RT-RTE-feedback-update](runtime.md#rt-rte-feedback-update); direct decay, weighting and maturity reads. Caller truthfulness and human versus computational authorship unresolved. |
| outcome/outcome-apply and reflection auto-grading | SRC-1 `src/outcome.ts` | Direct score and apply functions/context-log enrichment; [EPI-RTE-outcome-feedback](#epi-rte-outcome-feedback). Full transcript classifier and orchestrator auto-grading trigger not independently read; do not infer the source of an actual outcome. |
| forget, undo, remove, scrub | SRC-1 `src/commands/forget.ts`, `src/commands/undo.ts`, `src/commands/playbook.ts` | Direct forget inversion, undo helper and scrub save/deprecate branch; [EPI-RTE-reliance-maintenance](#epi-rte-reliance-maintenance). Remove located by search, not full confirmation-policy inspection. Scrub helper internals uninspected: prevents certifying complete lineage removal or recomputation fidelity. |
| trauma add/heal/remove/import and guard | SRC-1 `src/commands/trauma.ts`, `src/trauma_guard_script.ts` | Direct add/heal; guard supplied by [RT-RTE-trauma-guard](runtime.md#rt-rte-trauma-guard). Remove/import full admission uninspected; syntax checks cannot certify a safety policy. |
| retrieval benchmark and learning-loop tests | SRC-1 `test/context-retrieval-benchmark.test.ts`, `test/learning-loop.e2e.test.ts` | Direct benchmark comparator/evaluator/assertions; [EPI-RTE-retrieval-benchmark](#epi-rte-retrieval-benchmark). Learning-loop stubs supplied by runtime, not executed. |
| init, privacy, serve authentication, locks/config, delivery | SRC-1 `src/cm.ts`, `src/commands/serve.ts`, `src/playbook.ts` | Dispatch search and supplied runtime controls. Plumbing material only insofar as it affects admission, lineage or visibility; no deployed permission or multi-file transaction claim. |
| audit, why, stale, doctor; other tests and shipped helper branches | SRC-1 `src/cm.ts`, `src/commands/audit.ts`, `test/` | Registered operations located, deeper implementation uninspected. May expose or assess provenance/health; prevents exhaustive evaluator and withdrawal coverage. |

## Epistemic-object inventory

Fields owned by cited records are see those records; this inventory adds only the candidate-content assessment and limits.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-session-diary](#epi-obj-session-diary) | Descriptions of accomplishments, decisions, outcomes and lessons | Extracted session insight | SRC-1 `src/diary.ts`, `src/llm.ts` | Sanitized import has unknown source warrant; regex/model interpretation is not authenticated observation. |
| [RT-OBJ-playbook-bullet](runtime.md#rt-obj-playbook-bullet) | Conditional guidance may imply an effectiveness claim; bare imperative may be policy | Retained reusable guidance | SRC-1 `src/llm.ts` | Actual semantic instances not supplied; truth-aptness and preservation of particular rules not determinable. |
| [RT-OBJ-reflector-prompt](runtime.md#rt-obj-reflector-prompt) | Method instructions, not themselves evidence that a rule works | Candidate extraction and criticism request | SRC-1 `src/llm.ts` | Static method; requesting reusable content establishes no successful generalization. |
| [EPI-OBJ-validation-result](#epi-obj-validation-result) | Support/contradiction verdict, confidence and evidence labels | Admission evidence and gate output | SRC-1 `src/validate.ts` | Numeric confidence is assigned or model-generated, not calibrated probability. |
| [RT-CMP-generation-model](runtime.md#rt-cmp-generation-model) | Opaque distributed-parametric state; no individuated proposition established | Generates diary, deltas and judgments | SRC-1 `src/llm.ts` | Version, provider changes and internal warrant uninspected; no CM weight-training route established. |
| [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model) | Dense similarity representation, not a truth verdict | Ranking/dedup aid | SRC-1 `src/semantic.ts` | Version and representation fidelity unresolved; similarity does not certify equivalence. |
| [EPI-OBJ-outcome-feedback](#epi-obj-outcome-feedback) | Asserted task outcome and inferred rule usefulness/harm | Changes score and maturity | SRC-1 `src/outcome.ts`, `src/scoring.ts` | Shown/cited rules and success do not establish causal contribution. |
| [RT-RTE-trauma-guard](runtime.md#rt-rte-trauma-guard) | Regex restriction is policy; explanation can assert historical danger | Persistent safety-state consumer | SRC-1 `src/commands/trauma.ts` | Explanation and regex validity are separate; no evaluator establishes that matching commands are harmful. |

## Authority-route ledger

Each compact entry below is a consequential function, not a restatement of its declaring record. Shared fields owned by records say see. All implemented entries remain operationally unobserved.

Route ID: [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [EPI-OBJ-session-diary](#epi-obj-session-diary) and [RT-OBJ-playbook-bullet](runtime.md#rt-obj-playbook-bullet).
Content/update relation: truth-apt transformation: indeterminate. Importing the transcript acquires assertions with unknown warrant; model diary/delta generation may reshape, derive or conjecture. No response/premise pair establishes semantic preservation or non-entailment. Reusable wording requested by a prompt does not settle that classification.
Transition or check target: transcript/diary/history to candidate guidance.
Evaluator/condition and domain: schema and prompt requirements constrain output shape, not source truth; see the runtime route for driver conditions.
Activation and timing: reflection after explicit/discovered session, before admission.
Possible or observed result: possible structured diary and deltas; no observed instance.
Implemented force: candidate generation only, subject to later code admission.
Epistemic authority and scope: none from fluency or schema alone.
Operational authority: candidate reaches validator/curator, not an enclosing agent action directly.
Behavioral-authority path: see [RT-BAP-rule-guidance](runtime.md#rt-bap-rule-guidance); new candidate first enters CM's update consumer.
Evidence source ID and local anchor: SRC-1 `src/llm.ts`; see runtime route for supplied passages.
Claim IDs: [RT-CLM-rule-criticism](runtime.md#rt-clm-rule-criticism).
Mismatch marker: no trace of content-directed criticism or reliable generalization.
Gap/limit: neither model opacity nor absence of traces proves no conjecture occurs.

Route ID: [EPI-RTE-diary-inference](#epi-rte-diary-inference)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [EPI-OBJ-session-diary](#epi-obj-session-diary).
Content/update relation: truth-apt transformation: ampliative conjecture for inferred session success. A no-indicator input does not entail task success; code nevertheless assigns it. This does not classify copied metadata or every diary field.
Transition or check target: session text to status.
Evaluator/condition and domain: fixed regex classifier, domain of text markers rather than verified task completion.
Activation and timing: fast diary assembly before save.
Possible or observed result: success, failure or mixed; concrete deduction in shared record.
Implemented force: labels persisted diary; not a truth check.
Epistemic authority and scope: classification under code's lexical convention only, not actual success.
Operational authority: status available to later diary readers; influence of this specific fast diary on grading uninspected.
Behavioral-authority path: stored JSON to subsequent CM readers, advisory/evaluation input, later invocations.
Evidence source ID and local anchor: SRC-1 `src/diary.ts`.
Claim IDs: none.
Mismatch marker: default success exceeds the evidence conveyed by no-indicator text.
Gap/limit: no actual execution or outcome trace supplied.

Route ID: [EPI-RTE-evidence-check](#epi-rte-evidence-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-OBJ-validation-result](#epi-obj-validation-result).
Content/update relation: no content change.
Transition or check target: proposed add rule's support in historical snippets.
Evaluator/condition and domain: distinct-session success/failure regex counts; optional model support/contradiction judgment. Domain is retrieved text and its interpreted applicability, not a controlled test of rule effectiveness.
Activation and timing: enabled add validation, content at least 15 characters; selected gate branches skip model judgment.
Possible or observed result: gate counts/draft/active suggestion; optional ACCEPT, REJECT, REFINE or ACCEPT_WITH_CAUTION judgment.
Implemented force: results supplied to separate disposition; standalone printing differs.
Epistemic authority and scope: lexical count is warranted as an algorithmic property of returned snippets, not an outcome oracle; model verdict is an evidence-consuming but fallible assessment.
Operational authority: see separate disposition below.
Behavioral-authority path: validator result to orchestrator, admission signal, current update.
Evidence source ID and local anchor: SRC-1 `src/validate.ts`, `src/llm.ts`.
Claim IDs: [EPI-CLM-scientific-validation](#epi-clm-scientific-validation).
Mismatch marker: search relevance plus success language does not establish the rule was followed or caused success.
Gap/limit: external corpus completeness, truth, actual judgments and calibration uninspected.

Route ID: [EPI-RTE-validation-disposition](#epi-rte-validation-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see [EPI-OBJ-validation-result](#epi-obj-validation-result).
Content/update relation: no content change in valid/invalid decision; refinement handoff is a distinct, semantically indeterminate text change.
Transition or check target: candidate eligibility for curation as reusable guidance.
Evaluator/condition and domain: see shared record's bypasses, count thresholds and normalized model verdicts.
Activation and timing: after check, before fresh locked curation.
Possible or observed result: reject, allow without corroboration, allow from counts, or allow from model judgment; valid refined adds can receive suggested text.
Implemented force: orchestrator filters invalid deltas; no per-rule human veto in this route.
Epistemic authority and scope: branches that consume evidence instantiate acceptance against historical-support criteria for playbook use. Disabled/short/non-add/no-success branches instantiate operational admission or candidate retention, not evidence-backed acceptance. Count/model criteria do not license unconditional rule truth or transfer.
Operational authority: valid changes reach curation; valid does not guarantee save.
Behavioral-authority path: boolean/refined text to orchestrator then curator, permissive current update; saved rules subsequently advisory.
Evidence source ID and local anchor: SRC-1 `src/validate.ts`, `src/orchestrator.ts`.
Claim IDs: [EPI-CLM-scientific-validation](#epi-clm-scientific-validation).
Mismatch marker: universal pre-admission validation claim is contradicted by implemented bypasses.
Gap/limit: evidence-backed architecture is not observed acceptance of an ampliative claim; refinements are not separately rechecked in inspected handoff.

Route ID: [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update)
Route function: retention
Architectural status: implemented
Object/candidate ID: see [RT-OBJ-playbook-bullet](runtime.md#rt-obj-playbook-bullet).
Content/update relation: no content change for save itself.
Transition or check target: curated delta to durable playbook.
Evaluator/condition and domain: see runtime record for locks, reload, duplicate checks and processed marking.
Activation and timing: after validated-delta collection and curation; acceptance not universal prerequisite.
Possible or observed result: persisted rule/feedback changes and later read-back.
Implemented force: file writes; not one cross-file transaction.
Epistemic authority and scope: retention does not add warrant.
Operational authority: subsequent context/reflection can consume saved content.
Behavioral-authority path: see [RT-BAP-rule-guidance](runtime.md#rt-bap-rule-guidance).
Evidence source ID and local anchor: SRC-1 `src/orchestrator.ts`; see runtime record.
Claim IDs: [RT-CLM-automatic-learning](runtime.md#rt-clm-automatic-learning).
Mismatch marker: retention and restartability do not prove learning benefit.
Gap/limit: no observed saved-to-used trace.

Route ID: [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update)
Route function: lifecycle integration
Architectural status: implemented
Object/candidate ID: see [RT-OBJ-playbook-bullet](runtime.md#rt-obj-playbook-bullet).
Content/update relation: no content change for linking source-session lineage and proposal reasoning or subsequent use; any substituted refinement remains a separately qualified semantically indeterminate change.
Transition or check target: evidence-accepted addition surviving curation to lineage-linked retained guidance and later model-visible use.
Evaluator/condition and domain: see [EPI-RTE-validation-disposition](#epi-rte-validation-disposition) for conditional historical-support acceptance. The downstream driver collects valid deltas, curates and saves them; the new-add branch retains source-session lineage and optional proposal reasoning. Curation can still skip an accepted addition. The same downstream machinery also admits unchecked candidates, which do not thereby acquire lifecycle-integration status.
Activation and timing: after evidence-consuming acceptance and surviving curation; later reflection/context requests reload saved content. No candidate instance was observed traversing this conditional route.
Possible or observed result: accepted original content can be linked to its originating session and organized for later guidance; no observed accepted ampliative instance established. A model refinement is not independently rechecked, so original-candidate acceptance does not establish refined-text warrant.
Implemented force: curation adds lineage/reasoning, persistence saves the organized rule, and later consumers receive its text; not an additional truth check or universal acceptance guarantee.
Epistemic authority and scope: conditional integration after historical-support acceptance is wired, within that criterion's intended playbook use and scope. Linking originating-session provenance is not retention of the full validator evidence dossier or verification of source truth.
Operational authority: saved guidance enters subsequent CM reflection and offered agent context; consumer dependence and benefit remain unobserved.
Behavioral-authority path: see [RT-BAP-rule-guidance](runtime.md#rt-bap-rule-guidance), advisory prompt/context channel across subsequent invocations.
Evidence source ID and local anchor: SRC-1 `src/orchestrator.ts`, `src/curate.ts`, `src/playbook.ts`, `src/reflect.ts`, `src/commands/context.ts`; load-bearing passages in [EPI-RTE-validation-disposition](#epi-rte-validation-disposition).
Claim IDs: none.
Mismatch marker: shared downstream collection does not confer evidence-backed acceptance on unchecked candidates, nor refined-text warrant from original-candidate acceptance.
Gap/limit: missing candidate/verdict/save/read-back traces prevent observed accepted-instance attribution, not assessment of the implemented conditional architecture; complete evidence-dossier and provenance-consumer use remain unestablished.

Route ID: [EPI-RTE-curator-inversion](#epi-rte-curator-inversion)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [RT-OBJ-playbook-bullet](runtime.md#rt-obj-playbook-bullet).
Content/update relation: non-truth-apt policy/content update: deterministic positive-directive to avoidance-directive conversion. If interpreted as claiming that avoidance is generally beneficial, that extra claim is ampliative, not entailed by harmful marks.
Transition or check target: eligible harmful positive rule to new active anti-pattern.
Evaluator/condition and domain: decayed harmful threshold and dominance; no semantic safety evaluator.
Activation and timing: curator postprocessing before automatic deprecation; pinned/negative/anti-pattern cases differ.
Possible or observed result: new warning, original deprecated; concrete deduction in shared record.
Implemented force: automatic durable-state proposal/applied mutation, not just an explanatory report.
Epistemic authority and scope: reliable text rewrite under code convention; neither causal diagnosis nor transfer of a lesson established.
Operational authority: changes what later rule-guidance channel offers.
Behavioral-authority path: see [RT-BAP-rule-guidance](runtime.md#rt-bap-rule-guidance), across sessions after persistence.
Evidence source ID and local anchor: SRC-1 `src/curate.ts`.
Claim IDs: [EPI-CLM-pattern-learning](#epi-clm-pattern-learning).
Mismatch marker: executable conversion is less specific than the documented expiry-validation example.
Gap/limit: no observed harm attribution, safety benefit or independent acceptance of new avoidance rule.

Route ID: [EPI-RTE-playbook-import](#epi-rte-playbook-import)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see [RT-OBJ-playbook-bullet](runtime.md#rt-obj-playbook-bullet).
Content/update relation: truth-apt transformation: acquisition/import, source warrant unknown. Imported instruction policies also enter; similarity-based feedback transfer does not preserve warrant by proof.
Transition or check target: imported bullet schema and duplicate/replacement identity, not historical truth.
Evaluator/condition and domain: schema parse, ID/hash/Jaccard/directive predicates; caller --replace controls collision replacement.
Activation and timing: import under lock; contradiction report generated before save but not used as veto.
Possible or observed result: add/replace/skip/merge tracks and return conflicts.
Implemented force: writes admitted data; printed warning is advisory.
Epistemic authority and scope: structural validity and approximate duplication only; no historical-support acceptance decision.
Operational authority: imported scores/state can change later selection.
Behavioral-authority path: YAML and merged feedback to future scorer/context, ranking and advice, cross-session.
Evidence source ID and local anchor: SRC-1 `src/commands/playbook.ts`, `src/curate.ts`.
Claim IDs: [EPI-CLM-scientific-validation](#epi-clm-scientific-validation).
Mismatch marker: imported and replace branches qualify universal validation claims.
Gap/limit: producer truthfulness and semantic equivalence unknown.

Route ID: [RT-RTE-onboard-add](runtime.md#rt-rte-onboard-add)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see [RT-OBJ-playbook-bullet](runtime.md#rt-obj-playbook-bullet).
Content/update relation: truth-apt transformation: acquisition/import with unknown external caller warrant; imperative policy admitted too.
Transition or check target: caller-supplied content; optional quality/category/similarity checks.
Evaluator/condition and domain: see runtime record. Direct quality reads show word-count, context-marker and vague-word heuristics, not truth tests.
Activation and timing: requested add/batch; --check and --strict conditional.
Possible or observed result: add, warn or veto under strict checking.
Implemented force: persists accepted input; strict optional veto is not historical validation.
Epistemic authority and scope: structural/editorial quality only; external extraction epistemics uninspected.
Operational authority: later guidance available without reflection gate.
Behavioral-authority path: see [RT-BAP-rule-guidance](runtime.md#rt-bap-rule-guidance).
Evidence source ID and local anchor: SRC-1 `src/commands/playbook.ts`, `src/rule-validation.ts`.
Claim IDs: [EPI-CLM-scientific-validation](#epi-clm-scientific-validation).
Mismatch marker: starting onboarding is not per-rule evidence-backed approval.
Gap/limit: caller human/computational identity unresolved.

Route ID: [EPI-RTE-standalone-validate](#epi-rte-standalone-validate)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-OBJ-validation-result](#epi-obj-validation-result).
Content/update relation: no content change; suggested refinement is returned rather than automatically installed.
Transition or check target: proposed text's support in retrieved history.
Evaluator/condition and domain: same count gate then optional model; no-history returns caution. With noisy history but zero successes, unlike reflection it can call the model.
Activation and timing: explicit validate request.
Possible or observed result: printed verdict/confidence/refinement/evidence.
Implemented force: advisory output; no persistence call in command.
Epistemic authority and scope: bounded heuristic/model support assessment, no automatic authority grant to retained state.
Operational authority: external caller may act on output; no inspected consumer does so automatically.
Behavioral-authority path: CLI result to caller, advisory current request.
Evidence source ID and local anchor: SRC-1 `src/commands/validate.ts`.
Claim IDs: [EPI-CLM-scientific-validation](#epi-clm-scientific-validation).
Mismatch marker: printed ACCEPT is not playbook admission.
Gap/limit: model and caller operations unobserved.

Route ID: [EPI-RTE-outcome-feedback](#epi-rte-outcome-feedback)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: see [EPI-OBJ-outcome-feedback](#epi-obj-outcome-feedback).
Content/update relation: non-truth-apt policy/content update: scores/maturity from outcome labels; claimed per-rule helpfulness is an inference with unestablished causal warrant.
Transition or check target: outcome signal to rule feedback/reliance.
Evaluator/condition and domain: deterministic score/harm-margin/blast-radius rules, then maturity; evaluates supplied signals, not rule-caused results.
Activation and timing: outcome feedback application; context enrichment can backfill displayed IDs.
Possible or observed result: helpful/harmful event or abstention, missing-ID report, changed maturity.
Implemented force: persistent counters/events and ranking/state changes.
Epistemic authority and scope: bounded signal interpretation; neither citation nor delivery certifies component effect.
Operational authority: later selection can strengthen, weaken or exclude guidance.
Behavioral-authority path: events → scorer/context, ranking, future requests; rule wording itself unchanged here.
Evidence source ID and local anchor: SRC-1 `src/outcome.ts`, `src/scoring.ts`.
Claim IDs: [RT-CLM-automatic-learning](runtime.md#rt-clm-automatic-learning).
Mismatch marker: shown rules can receive shared task-level credit without demonstrated use.
Gap/limit: safety guards mitigate broad harm attribution but do not identify causal helpfulness.

Route ID: [RT-RTE-feedback-update](runtime.md#rt-rte-feedback-update)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: see [RT-OBJ-playbook-bullet](runtime.md#rt-obj-playbook-bullet).
Content/update relation: non-truth-apt policy/content update: caller judgments change reliance metadata.
Transition or check target: exact ID helpful/harmful event, then maturity.
Evaluator/condition and domain: caller judgment plus deterministic decay/maturity; see runtime record.
Activation and timing: explicit mark or HTTP feedback.
Possible or observed result: saved label, changed effective score/maturity and possible retirement.
Implemented force: software policy, with pinned rules exempt from automatic maturity demotion in inspected scoring.
Epistemic authority and scope: label assertion not verified outcome; proven means threshold-defined maturity, not proof.
Operational authority: future relevance ranking incorporates bounded feedback influence; deprecated guidance loses active selection eligibility.
Behavioral-authority path: feedback store → scorer → context; ranking/advisory future requests.
Evidence source ID and local anchor: SRC-1 `src/scoring.ts`; see runtime record for direct event write.
Claim IDs: [EPI-CLM-pattern-learning](#epi-clm-pattern-learning).
Mismatch marker: numerical confidence/decay is not epistemic endorsement or calibrated accuracy.
Gap/limit: no observed content-directed criticism from a bare label.

Route ID: [EPI-RTE-reliance-maintenance](#epi-rte-reliance-maintenance)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: see [RT-OBJ-playbook-bullet](runtime.md#rt-obj-playbook-bullet).
Content/update relation: no content change for feedback removal, deprecation or reactivation; optional forget inversion separately creates policy text.
Transition or check target: selected rule or feedback provenance to changed reliance.
Evaluator/condition and domain: caller-selected reason/ID/session predicate; code existence and state checks, not renewed empirical testing.
Activation and timing: explicit maintenance; dry-run scrub does not save.
Possible or observed result: blocked log/deprecation, optional avoidance rule, last-event removal, restored active state; scrub can save cleaned metadata and deprecate unpinned orphans.
Implemented force: durable metadata/policy changes after save; backups in scrub, not universal semantic rollback.
Epistemic authority and scope: withdrawal/restoration is operational reliance management; restoration itself supplies no new warrant.
Operational authority: future active-state filtering and scoring reflect changed metadata.
Behavioral-authority path: YAML/status to context/scorer, selection and advice, subsequent sessions.
Evidence source ID and local anchor: SRC-1 `src/commands/forget.ts`, `src/commands/undo.ts`, `src/commands/playbook.ts`.
Claim IDs: none.
Mismatch marker: undo does not retrospectively authenticate the original claim.
Gap/limit: scrub helper, full remove/undo dispatch and effect completeness uninspected.

Route ID: [RT-RTE-context-read](runtime.md#rt-rte-context-read)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: see [RT-OBJ-playbook-bullet](runtime.md#rt-obj-playbook-bullet).
Content/update relation: truth-apt transformation: non-ampliative reshaping for selected rule projection/ranking; separately imported history has unknown source warrant. The projection retains content but omits provenance arrays and feedback events.
Transition or check target: active applicable rules to task briefing, not truth assessment.
Evaluator/condition and domain: see runtime selector; lexical/optional semantic relevance and bounded feedback ranking.
Activation and timing: caller request, current playbook reload.
Possible or observed result: guidance, warnings and snippets, not full evidential dossier.
Implemented force: ranking/delivery; no obligation that caller follows guidance.
Epistemic authority and scope: selection does not accept a claim or preserve its complete warrant context.
Operational authority: code controls offered material, not enclosing task execution.
Behavioral-authority path: see [RT-BAP-rule-guidance](runtime.md#rt-bap-rule-guidance).
Evidence source ID and local anchor: SRC-1 `src/commands/context.ts`; see runtime record.
Claim IDs: none.
Mismatch marker: offered guidance is not demonstrated behavioral dependence.
Gap/limit: correctness, applicability and consumer interpretation remain unobserved.

Route ID: [RT-RTE-trauma-guard](runtime.md#rt-rte-trauma-guard)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: retained active regex policy; see runtime record.
Content/update relation: no content change.
Transition or check target: Bash command/staged text matching active restrictions.
Evaluator/condition and domain: fixed matcher, bounded tool/input and fail-open behavior; not a semantic danger judge.
Activation and timing: installed host/Git callback; heal changes future active-entry loading.
Possible or observed result: allow/deny JSON or failed commit.
Implemented force: conditional enforcement signal; host must honor it.
Epistemic authority and scope: regex match establishes pattern membership, not actual dangerousness or safety outside coverage.
Operational authority: can block matched host actions without a further epistemic check.
Behavioral-authority path: see [RT-BAP-guard-denial](runtime.md#rt-bap-guard-denial).
Evidence source ID and local anchor: SRC-1 `src/commands/trauma.ts`, `src/trauma_guard_script.ts`.
Claim IDs: none.
Mismatch marker: valid regex and a historical explanation are not accepted safety knowledge.
Gap/limit: manual add checks JavaScript regex syntax; downstream Python interpretation and installed-host outcomes remain independently unestablished here.

Route ID: [EPI-RTE-retrieval-benchmark](#epi-rte-retrieval-benchmark)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: ranker performance on authored labelled queries, not rule truth.
Content/update relation: no content change.
Transition or check target: current versus reconstructed incumbent keyword ranker.
Evaluator/condition and domain: expected rule IDs, recall@3, reciprocal rank, generic-rule displacement; test assertions.
Activation and timing: test execution, not production requests; none run here.
Possible or observed result: metrics and pass/fail, not observed result.
Implemented force: test failure when assertions violated; no inspected live rule withdrawal or admission consumer.
Epistemic authority and scope: if executed, bounded fixture ranking comparison; no claim correctness, downstream task benefit or model component effect.
Operational authority: development check, not production acceptance.
Behavioral-authority path: assertions to test runner, evaluation failure, test invocation only.
Evidence source ID and local anchor: SRC-1 `test/context-retrieval-benchmark.test.ts`.
Claim IDs: none.
Mismatch marker: source assertions are not observed benchmark success.
Gap/limit: authorship/representativeness and compound ranker contrast limit external validity and fine-grained attribution.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Source/anchor and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support/design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-scientific-validation](#epi-clm-scientific-validation) | Validation before every new rule joins; candidates without historical evidence | SRC-1 `README.md`, doctrine/design | Prompt asks scientific support/contradiction analysis | [EPI-RTE-evidence-check](#epi-rte-evidence-check), [EPI-RTE-validation-disposition](#epi-rte-validation-disposition), [EPI-RTE-playbook-import](#epi-rte-playbook-import), [RT-RTE-onboard-add](runtime.md#rt-rte-onboard-add) | None supplied | Text counts and model judgments, no controlled rule-effect test | Conditional evidence-consuming admission exists, alongside unchecked admissions | Universal wording unsupported; draft suggestion not a universal evidence-backed endorsement |
| [EPI-CLM-pattern-learning](#epi-clm-pattern-learning) | Harmful rules become warnings; confidence decays and maturity rewards helpful guidance | SRC-1 `README.md`, doctrine/design | Explicit decay/inversion/maturity description | [EPI-RTE-curator-inversion](#epi-rte-curator-inversion), [RT-RTE-feedback-update](runtime.md#rt-rte-feedback-update) | None supplied | Harm labels and deterministic policy do not identify why a rule failed | Persistent feedback-driven policy adaptation and warning conversion wired | Specific expiry-qualified example is not the generic code rewrite; usefulness and transfer unknown |
| [RT-CLM-automatic-learning](runtime.md#rt-clm-automatic-learning) | End work; learning automatic | See declaring record, doctrine/design | See record | [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update), [EPI-RTE-outcome-feedback](#epi-rte-outcome-feedback) | None supplied | Hook/model/admission conditions; no counterfactual task evidence | Conditional automated state-update and later read-back mechanism | Neither session completion nor persistence establishes improved future capacity |
| [RT-CLM-rule-criticism](runtime.md#rt-clm-rule-criticism) | Identify rule-caused harm and replace/deprecate by ID | See declaring record, doctrine/design | Rule-specific prompt request | [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update) | None supplied | Model judgment and score changes are not a criticism trace | Addressable rule update/withdrawal and criticism request wired | Content dependence, claim/result/blame and iterative criticism not established |

## Bounded conclusion

CM acquires historical assertions through external cass and caller input with unknown source warrant. It retains diary descriptions, rules and reliance metadata, and reloads selected guidance for later agents and for its own reflector. Projection preserves selected rule text while excluding much evidential metadata; retrieval is a relevance decision, not endorsement. These conclusions have implementation support through [RT-RTE-context-read](runtime.md#rt-rte-context-read) and [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update), not observed compliance.

Historical-support evaluation is genuinely consequential in some branches: count/model results can veto or allow a proposed add for playbook use. Its criterion is retrieved textual support, its intended use reusable guidance, and its scope the checked add branch. Other branches explicitly allow unchecked or uncorroborated candidates, manual/imported instructions and replacements. Evidence-consuming acceptance is therefore a supported conditional architecture, not a universal rule property. Conditional lifecycle integration is also implemented: an evidence-accepted addition that survives curation can retain originating-session lineage and proposal reasoning, be saved, and enter later reflection/context use. This downstream wiring is separate from observed operation. No supplied candidate trace establishes an observed accepted ampliative claim followed by evidence-linked lifecycle integration. Unchecked branches remain candidate retention, and substitution of a model refinement lacks an independent recheck; acceptance of the original candidate does not establish the refinement's warrant ([EPI-RTE-evidence-check](#epi-rte-evidence-check), [EPI-RTE-validation-disposition](#epi-rte-validation-disposition)). No new domain proposition is shown derived from independently warranted premises; deterministic marker/count/score computations establish only facts about their encoded inputs and conventions.

Two concrete implementation deductions identify generation beyond extraction without model execution. Fast diary status defaults to success even when text contains no success/error indicator. Curator inversion rewrites harmful positive policy into avoidance text without explaining a condition under which avoidance is effective. The former is an ampliative outcome conjecture; the latter is a policy change, with any broader effectiveness interpretation unsupported by entailment ([EPI-RTE-diary-inference](#epi-rte-diary-inference), [EPI-RTE-curator-inversion](#epi-rte-curator-inversion)). Model-generated content remains semantically indeterminate without input/output evidence, rather than being classified as conjecture merely because entailment is unknown.

Reliance can change without rule text changing: feedback/outcome labels, decay, maturity, import-track merging, withdrawal, scrub and undo affect later ranking and active eligibility. These are operative policy/recovery paths, not proof that a rule is true. Outcome attribution expressly distinguishes displayed rules and deliberate citations, limits broad harmful grading, and can abstain; these safeguards do not demonstrate rule-caused success. The standing adaptation/read-back architecture coexists with unestablished improved capacity, exercised self-improvement and causal benefit ([EPI-RTE-outcome-feedback](#epi-rte-outcome-feedback), [EPI-RTE-reliance-maintenance](#epi-rte-reliance-maintenance)).

Rules can exert advisory force across sessions; trauma patterns can exert conditional host-enforcing force. The latter's check licenses regex membership only. Neither channel establishes actual host behavior or safety. Distributed-parametric generation and embedding components have separately recorded version/endpoint uncertainty and no inspected CM parameter-update path; that does not negate learning through retained symbolic or linguistic state (see [RT-CMP-generation-model](runtime.md#rt-cmp-generation-model), [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model)).

Whole-rule addressability is afforded, criticism is requested, and revisions can persist. Actual content-dependent decisions and criticism-driven iteration remain uninspected, independently of retention and adaptation. Reflection's representation/update loop does not establish reflective method revision or autonomous theory building; see the independent theory findings in [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update). Benchmark source supplies a bounded evaluator design, not observed benefit. Named uninspected operations in coverage preclude a system-complete negative or a single epistemic verdict.

## Shared records

### Operative objects

#### EPI-OBJ-session-diary
Label: Session diary assertions

Source-native identity: `DiaryEntry` status/accomplishments/decisions/challenges/keyLearnings. Representational form: natural-language session descriptions plus symbolic status consumed by fixed code. Storage substrate: diary JSON. Different checks apply to the status classifier and model-derived text; the routes separate them. No counterpart object is declared in supplied runtime; diaries are inputs within [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update), not identical to its playbook output. Evidence: SRC-1 `src/diary.ts`, `src/llm.ts`, implementation and doctrine/design.

> const outcome = inferOutcome(sanitizedContent);
> --- `src/diary.ts`

> keyLearnings: summary ? [summary] : [],
> --- `src/diary.ts`

> If the session lacks information for a field, provide an empty array.
> --- `src/llm.ts`

#### EPI-OBJ-validation-result
Label: Validation verdict and evidence labels

Source-native identity: `EvidenceGateResult`, `ValidationResult`, validator verdict/confidence/supportingEvidence/contradictingEvidence. Representational form: symbolic counts/booleans/verdicts for fixed consumers and linguistic reason/refinement for model/caller interpretation. Storage substrate: current-run objects and decision-log entries; durable completeness of the validator dossier is not established. No supplied counterpart object; it is check output inside [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update), not the rule itself. Evidence: SRC-1 `src/validate.ts`, implementation.

> confidence: 1.0,
> reason: gate.reason,
> evidence: [],
> approved: true,
> supportingEvidence: [],
> contradictingEvidence: [],
> --- `src/validate.ts`

#### EPI-OBJ-outcome-feedback
Label: Outcome attribution signals

Source-native identity: `OutcomeRecord`, `rulesUsed`, `autoGraded` and generated `FeedbackEvent`. Representational form: symbolic outcome/ID/score records consumed by fixed policy, with natural-language context. Storage substrate: outcome/context logs and playbook event arrays. Distinct from [RT-RTE-feedback-update](runtime.md#rt-rte-feedback-update): this object supplies inferred batch feedback rather than an explicit caller mark for one ID. Evidence: SRC-1 `src/outcome.ts`, implementation.

> return { ...outcome, rulesUsed: match.ruleIds, autoGraded: true };
> --- `src/outcome.ts`

### Routes

#### EPI-RTE-diary-inference
Label: Fast diary outcome inference
Part of: [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update)

The record isolates a content-producing step of the supplied container; the standalone diary entry point also exposes it. Endpoints: sanitized session text → marker classifier → saved diary status. Owner: deterministic diary code; no human approval or expected-outcome oracle. Trigger: fast diary generation. Proposed assertion is success/failure/mixed; code decides it. Context is session text and fixed regexes; status persists. A later correction requires regeneration or maintenance, not an inspected objective-outcome rollback.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: diary object after save.
- Later read-back: diary JSON can be loaded by subsequent diary/reflection operations; exact deployed reader activation uninspected.
- Delegated visibility: status and condensed insights, not all original session content.
- Selection predicate: success/error regex matches; neither match defaults to success.
- Invalidation or expiry: uninspected — automatic invalidation of erroneous inferred status not inspected.
- Activation or effect: persisted outcome representation; no observed downstream dependence.
- Evidence limits: text indicators do not verify task completion.

Concrete source deduction, not execution: `inferOutcome("Planning deployment")` matches neither regex family and returns `success`; the input entails no completed deployment. The output is thus an unsupported outcome conjecture, not mere extraction. Evidence: SRC-1 `src/diary.ts`, implementation.

> if (hasErrors && hasSuccess) return "mixed";
> if (hasErrors) return "failure";
> if (hasSuccess) return "success";
>
> return "success"; // Default to success if no clear indicators
> --- `src/diary.ts`

#### EPI-RTE-evidence-check
Label: Historical support check
Part of: [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update)

Endpoints: add content → keyword search → unique session marker counts → optional model verdict. Owner: validation program and configured model. This isolates checking from disposition. Criterion requested of the model is historical support/contradiction, applicability and scope; there is no supplied expected correct rule or external outcome oracle. Model/provider identity limits are see [RT-CMP-generation-model](runtime.md#rt-cmp-generation-model). Computational assessment is open-session maintenance, not an intervention experiment.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: gate and optional result/decision-log data.
- Later read-back: inapplicable — check output itself has no established complete persisted dossier/read-back in inspected handoff; resulting rule retention is a separate function.
- Delegated visibility: model sees proposed text and formatted selected snippets, session paths and relevance, not the exhaustive corpus.
- Selection predicate: add, validation enabled, content at least 15 characters; gate queries up to 20 hits with lookback, optional model query up to 10.
- Invalidation or expiry: future checks can query changed history; no automatic truth withdrawal inferred.
- Activation or effect: evidence output supplied to separate valid/invalid disposition.
- Evidence limits: regex success is not proof of applying the proposed rule; snippets can support, contradict or omit actual outcomes.

A counterexample to strong corroboration is visible in the implementation: five distinct returned source paths whose snippets say `success` satisfy auto-accept even if none says the proposed rule was followed. Counts are about lexical signals, not a checked causal relation. Evidence: SRC-1 `src/validate.ts`, implementation; SRC-1 `src/llm.ts`, doctrine/design.

> if (matchesPatterns(snippet, SUCCESS_PATTERNS)) successSessions.add(sessionPath);
> if (matchesPatterns(snippet, FAILURE_PATTERNS)) failureSessions.add(sessionPath);
> --- `src/validate.ts`

> if (successCount >= 5 && failureCount === 0) {
> --- `src/validate.ts`

> Analyze whether the evidence supports, contradicts, or is neutral toward the proposed rule.
> --- `src/llm.ts`

#### EPI-RTE-validation-disposition
Label: Reflection candidate disposition
Part of: [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update)

Endpoints: gate/model/bypass result → valid flag → orchestrator filtered/refined deltas → curator. Owner: code; model proposes verdict/refinement, operator configures gates but does not approve each candidate. Triggers/proposal guidance are see container and [RT-OBJ-reflector-prompt](runtime.md#rt-obj-reflector-prompt). Code can veto strong-failure or rejecting model results; configuration disables checks. No external answer oracle. Recovery is retry/file-level persistence and later maintenance, not proof-preserving rollback.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: valid/invalid and optional gate/model result.
- Later read-back: allowed deltas can persist and enter later context/reflector; exact evidence dossier retention unestablished.
- Delegated visibility: orchestrator receives validation result; later context sees compact rule text/metadata rather than full check rationale.
- Selection predicate: non-add, disabled and short inputs pass; strong failure rejects; strong success passes; draft/no-success passes; remaining model ACCEPT/caution/refinement pass, rejection fails.
- Invalidation or expiry: later feedback, replacement and deprecation can alter reliance; no independent revalidation of suggested refinement is in inspected handoff.
- Activation or effect: invalid deltas excluded; valid refined add text substituted before curation.
- Evidence limits: valid is admission permission; unchecked paths are not evidence-backed acceptance, and remaining curation can still skip.

Evidence: SRC-1 `src/validate.ts`, `src/orchestrator.ts`, implementation. This qualifies, rather than supersedes, the valid container account in the runtime.

> if (gate.suggestedState === "draft" && gate.successCount === 0) {
> --- `src/validate.ts`

> if (validation.valid) {
> // Apply LLM refinement if suggested
> if (validation.result?.refinedRule && delta.type === "add") {
> delta.bullet.content = validation.result.refinedRule;
> }
> validatedDeltas.push(delta);
> }
> --- `src/orchestrator.ts`

The conditional downstream integration path is implemented, not merely possible because of missing run evidence. Valid deltas enter `allDeltas`; curation's surviving new-add branch passes `delta.sourceSession` into `addBullet` and retains optional proposal reasoning. The helper stores the session link. Curated playbooks are saved and later reloaded for reflection/context. These steps also serve unchecked admissions; only evidence-accepted branches qualify as post-acceptance integration. The refinement qualification above still applies. Evidence: SRC-1 `src/orchestrator.ts`, `src/curate.ts`, `src/playbook.ts`, `src/reflect.ts`, `src/commands/context.ts`, implementation. No observed instance, complete validator dossier or actual dependence on provenance is established.

> if (validatedDeltas.length > 0) {
> allDeltas.push(...validatedDeltas);
> }
> --- `src/orchestrator.ts`

> delta.sourceSession,
> config.scoring.decayHalfLifeDays,
> );
>
> if (typeof delta.reason === "string" && delta.reason.trim()) {
> newBullet.reasoning = delta.reason.trim();
> }
> --- `src/curate.ts`

> sourceSessions: [sourceSession],
> --- `src/playbook.ts`

> await savePlaybook(repoResult.playbook, repoPath, { updateLastReflection: true });
> --- `src/orchestrator.ts`

> const existingBullets = formatBulletsForPrompt(playbook.bullets);
> --- `src/reflect.ts`

> const sources = await loadMergedPlaybookWithSources(
> config,
> effectiveWorkspace ? { cwd: effectiveWorkspace } : {},
> );
> const playbook = sources.playbook;
> --- `src/commands/context.ts:629-633`

#### EPI-RTE-curator-inversion
Label: Curator anti-pattern conversion
Part of: [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update)

Endpoints: harmful feedback on rule → decayed threshold → new avoidance rule and original deprecation. Owner: curator code. Distinct material transformation within runtime's curation step, not another complete reflection route. Software proposes and decides wording; pinned or already negative/anti-pattern rules are excluded or treated differently. No human approval or answer oracle. Operating mode: maintenance, triggered by accumulated harmful dominance; original feedback is evidence for a policy decision, not a checked mechanism. Proposed warning persists after playbook save; later maintenance can withdraw it.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: mutated playbook and inversion report.
- Later read-back: saved anti-pattern content can enter future context and reflection prompts.
- Delegated visibility: future consumer sees warning text; copied provenance does not explain causal mechanism.
- Selection predicate: eligible unpinned positive rule, decayed harmful at configurable prune threshold (fallback 3 with epsilon), greater than twice decayed helpful.
- Invalidation or expiry: original deprecated; later feedback/deprecation/maintenance governs new warning.
- Activation or effect: new active candidate anti-pattern added and original withdrawn in curator state; persistence supplied by container.
- Evidence limits: harm counts and textual inversion do not establish that the converse policy works.

Concrete source deduction: eligible `Use cache` with harmfulCount 3 becomes `AVOID: cache. Marked harmful 3 times`. This is a policy rewrite, not the README's condition-aware warning synthesis. No target execution is needed for this deduction. Evidence: SRC-1 `src/curate.ts`, implementation.

> const reason = `Marked harmful ${bullet.harmfulCount} times`;
> const cleaned = bullet.content
> .replace(/^(always |prefer |use |try |consider |ensure )/i, "")
> .trim();
> const invertedContent = `AVOID: ${cleaned}. ${reason}`;
> --- `src/curate.ts`

> if (bullet.deprecated || bullet.pinned || bullet.kind === "anti_pattern") continue;
> --- `src/curate.ts`

#### EPI-RTE-playbook-import
Label: Playbook import admission

No exact supplied counterpart: overlaps [RT-RTE-onboard-add](runtime.md#rt-rte-onboard-add)'s manual admissions but admits full retained bullets, imported feedback and replacement state, not caller rule text only. Endpoints: file → defaults/schema → ID/hash/similarity decision → merged/replaced playbook → save. Owner: code; caller supplies file and replace flag. Structural schema can veto; contradiction warning does not veto. Guidance: portable retained-state import, not reflector prompt. No historical answer oracle; open import mode. File-level locking/save, not automatic semantic recovery.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: added/merged/updated/skipped counts and conflicts.
- Later read-back: imported rules/feedback/state consumed by later scoring, context and reflection.
- Delegated visibility: caller sees warnings; later context receives compact rules rather than authenticated imported provenance.
- Selection predicate: schema-valid bullets; ID match plus replace, content hash or threshold overlap with directive-disagreement protection.
- Invalidation or expiry: normal later maturity/maintenance; imported replace can overwrite prior state.
- Activation or effect: persisted merged state; conflicts reported without automatic rejection.
- Evidence limits: schema validity and near-duplicate matching do not establish source truth or identity of warrant.

Evidence: SRC-1 `src/commands/playbook.ts`, implementation. Conflict parser itself is a heuristic: SRC-1 `src/curate.ts` checks shared topic and polarity/exception markers, not a general logic prover.

> const validated = PlaybookBulletSchema.parse(bullet);
> importedBullets.push(validated);
> --- `src/commands/playbook.ts`

> if (flags.replace) {
> const idx = existingPlaybook.bullets.indexOf(sameId);
> existingPlaybook.bullets[idx] = bullet;
> updated++;
> --- `src/commands/playbook.ts`

#### EPI-RTE-standalone-validate
Label: Standalone validation report

Distinct from [RT-RTE-reflection-update](runtime.md#rt-rte-reflection-update): explicit CLI check ends at output, not curation/save. Endpoints: proposed text → evidenceCountGate/optional model → printed result. Owner: code/model; caller supplies candidate and can ignore output. No expected-answer oracle. Open requests; admission into durable knowledge is inapplicable here. REFINE becomes caution, no-history becomes caution; unlike reflection, nonempty/no-success history can reach model judgment. Recovery: caller can rerun, no rollback needed because no mutation inspected.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON/text verdict, confidence, possible refinement and snippets.
- Later read-back: inapplicable — inspected command does not persist result or playbook update.
- Delegated visibility: caller receives result; model sees bounded snippets and proposed text.
- Selection predicate: nonempty proposal; count gate determines reject/accept/no-history caution versus model call.
- Invalidation or expiry: inapplicable — returned assessment has no stored authority interval.
- Activation or effect: advisory print only; no automatic installed-state consumer inspected.
- Evidence limits: source result formatting is not observed judgment or caller reliance.

Evidence: SRC-1 `src/commands/validate.ts`, implementation.

> verdict: "ACCEPT_WITH_CAUTION",
> confidence: 0.6,
> reason: gate.reason,
> evidence: [],
> };
> return printResult(output, options, { command, startedAtMs });
> --- `src/commands/validate.ts`

#### EPI-RTE-outcome-feedback
Label: Outcome-derived rule feedback

Distinct from [RT-RTE-feedback-update](runtime.md#rt-rte-feedback-update): task-level outcome inference updates several attributed rules rather than one explicit helpful/harmful request. Endpoints: outcome and optional context log → signal score → target IDs → events/count/maturity → save. Owner: code; caller or automatic classifier supplies outcome signals, not a verified expected answer. Open feedback maintenance. Proposed update is reliance metadata; harm/abstention policy can veto events. Recovery uses idempotent-event check and later maintenance; no semantic truth rollback.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: applied count and missing IDs.
- Later read-back: persisted feedback reaches later scorer/context and maturity decisions.
- Delegated visibility: events/context summarize signal reasons; do not reproduce causal evidence per rule.
- Selection predicate: rulesUsed or same-session latest context-log IDs; non-null score; known target ID; duplicate-event suppression.
- Invalidation or expiry: feedback decays; subsequent events/state maintenance change reliance.
- Activation or effect: persistent count/maturity changes; actual future agent response unobserved.
- Evidence limits: abstention/broad-harm guards bound attribution policy, not empirical attribution accuracy.

Evidence: SRC-1 `src/outcome.ts`, `src/scoring.ts`, implementation.

> const scored = scoreImplicitFeedback(enriched);
> if (!scored) continue;
>
> for (const ruleId of enriched.rulesUsed) {
> --- `src/outcome.ts`

> bullet.maturity = calculateMaturityState(bullet, config);
> --- `src/outcome.ts`

> // Pinned bullets should not be auto-deprecated or demoted by feedback
> if (bullet.pinned) return bullet.maturity;
> --- `src/scoring.ts`

#### EPI-RTE-reliance-maintenance
Label: Explicit reliance maintenance

No exact supplied counterpart: maintenance can undo the event in [RT-RTE-feedback-update](runtime.md#rt-rte-feedback-update), withdraw its target, or scrub provenance. Endpoints: caller ID/reason/session filter → code state/event edits → save → later active selection. Owner: caller chooses operation, code applies; generic caller identity does not establish human approval. No answer oracle. Open maintenance triggers; proposed changes are withdrawal/restore/lineage correction and optional avoidance content. ID/state checks can fail; scrub has dry-run and backup, but full semantic rollback is not established. Admitting a restored rule requires no newly supplied historical test in inspected helper.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: maintenance report or error; scrub includes change/backup report.
- Later read-back: changed state/counts/provenance in playbook affect later retrieval and reflection.
- Delegated visibility: caller sees operation report; later consumer receives changed active guidance.
- Selection predicate: explicit ID or session predicate; scrub orphan deprecation conditional and pinned-exempt.
- Invalidation or expiry: deprecation persists until explicit undo/other edit; removed events no longer supply that score input.
- Activation or effect: writes withdrawal or restoration metadata; forget can add a new avoidance rule.
- Evidence limits: complete scrub helper/removal dispatch not inspected; no renewed warrant follows from restoration.

Evidence: SRC-1 `src/commands/forget.ts`, `src/commands/undo.ts`, `src/commands/playbook.ts`, implementation.

> deprecateBullet(playbook, bulletId, flags.reason!, antiPatternId);
> --- `src/commands/forget.ts`

> bullet.feedbackEvents = events.slice(0, -1);
> --- `src/commands/undo.ts`

> bullet.state = "active";
> // Restore to candidate if it was deprecated, otherwise keep current
> if (bullet.maturity === "deprecated") {
> bullet.maturity = "candidate";
> }
> --- `src/commands/undo.ts`

> if (flags.deprecateOrphans) {
> --- `src/commands/playbook.ts`

#### EPI-RTE-retrieval-benchmark
Label: Labelled retrieval comparator

No supplied route counterpart; this evaluates [RT-RTE-context-read](runtime.md#rt-rte-context-read) rather than returning production context. Endpoints: authored queries/expected IDs → reconstructed incumbent/current keyword ranker → metrics/assertions. Owner: test code; authors choose oracle IDs and dataset. Bounded test mode, not ongoing autonomous experimentation. Proposed comparison evaluates ranking change, with assertions able to fail but no inspected deployment/rollback consumer. Generation, semantic backend and downstream agents are not independently varied.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: printed metrics and assertion pass/fail on execution.
- Later read-back: inapplicable — no changed retained rule or live policy consumed later by this test.
- Delegated visibility: test runner sees metrics/failures; production agents receive none from this route.
- Selection predicate: fixed QUERIES/fixture bullets, K=3, keyword functions and authored expected IDs.
- Invalidation or expiry: inapplicable — source test result does not persist an accepted rule.
- Activation or effect: development assertion failure only; no test was run here.
- Evidence limits: whole ranker contrast, authored fixture and no execution prevent actual improvement or component-causal claims.

Evidence: SRC-1 `test/context-retrieval-benchmark.test.ts`, implementation/evaluator design, not observed run.

> const ids = rank(bullets, extractKeywords(query)).map((b) => b.id);
> const pos = ids.indexOf(expected);
> if (pos >= 0 && pos < k) hits++;
> if (pos >= 0) reciprocal += 1 / (pos + 1);
> --- `test/context-retrieval-benchmark.test.ts`

> expect(current.recallAtK).toBeGreaterThanOrEqual(incumbent.recallAtK);
> expect(current.mrr).toBeGreaterThanOrEqual(incumbent.mrr);
> --- `test/context-retrieval-benchmark.test.ts`

### Claims

#### EPI-CLM-scientific-validation
Label: Pre-admission scientific validation claim

No counterpart claim in supplied runtime: runtime gives bypass witnesses but not this public universal claim. Claimed operation: all new rules validated against history before joining, uncorroborated rules candidate until proven. Evidence: SRC-1 `README.md`, doctrine/design. The qualifying routes distinguish support judgments from proof and candidates from evidence-backed acceptance.

> New rules aren't blindly accepted. Before a rule joins your playbook, it's validated against your cass history:
> --- `README.md`

> Rules without historical evidence are flagged as candidates until proven.
> --- `README.md`

#### EPI-CLM-pattern-learning
Label: Confidence and anti-pattern learning claim

Distinct from [RT-CLM-automatic-learning](runtime.md#rt-clm-automatic-learning): this specifies decay, maturity and harmful-rule conversion rather than automatic session-end initiation. Claimed operation: harmful rules automatically become warnings; feedback/decay tracks confidence and maturity. Evidence: SRC-1 `README.md`, doctrine/design. Implemented rewrite/score machinery supports policy adaptation, not calibrated truth probability or demonstrated warning effectiveness.

> When a rule is marked harmful multiple times, it's automatically inverted into an anti-pattern that warns future agents away from the same mistake.
> --- `README.md`

> - **Maturity progression**: `candidate` → `established` → `proven`
> --- `README.md`
