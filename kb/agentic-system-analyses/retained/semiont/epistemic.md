---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Semiont's source attribution, model criticism, candidate ranking and operational admission, distinguished from factual acceptance."
run-id: AAS-2026-10-15-semiont-d516c7013d8f-01
reviewed-boundary: a920067ac4ea63a57b1855b7d263485fbd22bab4
---

# Semiont epistemic report

## Source-and-claim boundary

The question is how Semiont's retained sources and model outputs acquire authority, and what its checks actually license. Scope and external exclusions are those of the [boundary](boundary.md#boundary-and-evidence); evidence identities and layers are in its [Source register](boundary.md#source-register). This remains a complete artifact, partial loop analysis. All new inspection below is SRC-1 implementation or explicitly identified doctrine/design at the frozen commit. No operation or benefit was observed, and no target code or tests were executed.

The relevant public warrant claim is [EPI-CLM-trusted-knowledge](#epi-clm-trusted-knowledge). More specific claims concern [RT-CLM-source-grounding](runtime.md#rt-clm-source-grounding) and [EPI-CLM-assessment-concerns](#epi-clm-assessment-concerns). A source link, model assessment, successful compilation, and permission to write have different targets and different licenses. They must not be combined into one truth verdict.

| Entry point or operation | Source path | Coverage and records, or limit |
|---|---|---|
| MCP registration and dispatch | `packages/mcp-server/src/server.ts`, `packages/mcp-server/src/handlers.ts` | Direct reads: eleven call branches; registered resources and prompts return empty lists. Browse/match/gather feed callers; mark/bind/direct yield/delegated yield can change retained content. Compared with [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation), [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission), [RT-RTE-mark-detection](runtime.md#rt-rte-mark-detection). |
| CLI dispatch and assessment entry | `apps/launcher/main.go`, `apps/launcher/internal/verbs/mark.go` | Direct bounded reads: main dispatch includes mark, yield, gather, bind, match and import/export; mark constructs typed motivation-specific jobs including assessing. [EPI-RTE-assessment-proposal](#epi-rte-assessment-proposal). Full import/export, other verbs and startup behavior remain uninspected; no all-entry-point negative follows. |
| Authentication, job routing, upload | `apps/gateway/src/routes/bus.rs`, `apps/dispatcher/handlers/src/admission.rs`, `apps/archivist/src/surface.rs` | Supplied runtime findings, not independent rereads: [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission), [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation). They supply provenance/protocol gates, not a factual oracle. |
| Citation commit attribution and refusal | `packages/sdk-python/src/semiont/claims.py`, `apps/dispatcher/handlers/src/handlers.rs`, `apps/archivist/src/commands.rs`, `apps/archivist/src/bus.rs` | Correction-round direct bounded reads trace original-resource assignment, new-resource commit refusal before recording, bus failure reply and SDK propagation; [EPI-RTE-citation-retention](#epi-rte-citation-retention). |
| Generated-document transformation and citations | `apps/worker/src/semiont_worker/processors.py`, `apps/worker/src/semiont_worker/generation/citations.py`, `apps/worker/src/semiont_worker/held_job.py`, `apps/worker/src/semiont_worker/generation/claim_search.py` | Direct reads of citation implementation and generation/upload/citation sections: [EPI-RTE-citation-processing](#epi-rte-citation-processing), [EPI-RTE-citation-retention](#epi-rte-citation-retention). |
| Annotation evaluation and anchoring | `apps/worker/src/semiont_worker/detection/parsers.py`, `apps/worker/src/semiont_worker/detection/anchor_audit.py`, `apps/worker/src/semiont_worker/detection/prompts.py` | Direct reads of parser/audit and assessment prompt ranges: [EPI-RTE-span-check](#epi-rte-span-check), [EPI-RTE-assessment-proposal](#epi-rte-assessment-proposal). Other motivations and reconciliation algorithm internals are not exhaustively inspected. |
| Annotation gather and PDF repair | `apps/librarian/src/semiont_librarian/annotation_gather.py`, `apps/worker/src/semiont_worker/generation/typst.py` | Supplied [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather), [RT-RTE-pdf-repair](runtime.md#rt-rte-pdf-repair); processors and generation prompt selection independently read. |
| Resource gather and annotation summary | `apps/librarian/src/semiont_librarian/resource_gather.py`, `apps/librarian/src/semiont_librarian/summary.py` | Direct reads: [EPI-RTE-summary-generation](#epi-rte-summary-generation). Resource checksum/settle handling is freshness, not endorsement. |
| Reference search and scoring | `apps/librarian/src/semiont_librarian/reference_search.py`, `apps/librarian/src/semiont_librarian/score.py` | Direct reads: [EPI-RTE-reference-search](#epi-rte-reference-search). Model reply parser and all UI selection policies remain uninspected. |
| Withdrawal and projection consequences | `apps/archivist/src/commands.rs`, `apps/weaver/src/semiont_weaver/fold.py`, `apps/smelter/src/semiont_smelter/smelter.py` | Direct bounded reads: [EPI-RTE-knowledge-withdrawal](#epi-rte-knowledge-withdrawal). Complete event/view folding, reconciliation and recursive invalidation are not assessed. |
| Shipped assessment/aggregate instructions | `docs/builder/skills/semiont-assess/SKILL.md`, `docs/builder/skills/semiont-aggregate/SKILL.md` | Assessment skill read directly; aggregate title/procedure/consumer guidance inspected by scoped search. [EPI-CLM-assessment-concerns](#epi-clm-assessment-concerns). External skill execution and aggregate synthesis correctness remain unknown. |
| Evaluation infrastructure | `tests/conformance/librarian/README.md` | Direct full documentation read; [EPI-CLM-conformance-scope](#epi-clm-conformance-scope). Assertions/harness and results uninspected; no passing-suite or factual-quality inference. |
| Other hooks, clients and maintenance | `apps/browser`, `apps/desktop`, `apps/launcher`, `apps/smelter`, `apps/weaver` | MCP registration and CLI dispatch checked, but no complete repository-wide hook/extension audit. Browser/desktop review and host extensions, full launcher import, OCR extraction, provider alternatives and full projection repair remain uninspected. These prevent a system-complete negative about evaluation, approval or knowledge production. |

No external corpus, deployed human decisions, model responses, acceptance records or causal comparisons were supplied. Missing responses prevent classifying actual generated propositions by entailment; missing run records prevent establishing acceptance or activation in operation. Available uninspected implementation is not an access failure. Remote weights, provider changes and exact model versions remain bounded as in [RT-CMP-worker-inference](runtime.md#rt-cmp-worker-inference), [RT-CMP-gatherer](runtime.md#rt-cmp-gatherer), and [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider).

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-job-params](runtime.md#rt-obj-job-params) | Supplied source/context statements can be truth-apt; task instructions and routing fields need not be | see record | see record | Client-supplied context is not certified current or true by admission. |
| [EPI-OBJ-generated-document](#epi-obj-generated-document) | Propositions in model-written document; specific instances not determinable without outputs | see record | see record | No semantic preservation, entailment or non-entailment established for an actual response. |
| [EPI-OBJ-assessment-text](#epi-obj-assessment-text) | Claims about a source passage's validity, assumptions or implications; concern instructions also allow normative judgments | see record | see record | Anchoring a target does not establish truth of the assessment. |
| [EPI-OBJ-gathered-prose](#epi-obj-gathered-prose) | Summaries and relationship sentences about retained content, plus suggested referent names | see record | see record | Generation is requested, not proven faithful compression; proposals may be non-propositional. |
| [EPI-OBJ-reference-score](#epi-obj-reference-score) | Numerical heuristic/rank has no independent truth value; accompanying candidate descriptions and reasons can state facts about retrieval inputs | see record | see record | A high score does not assert calibrated probability of correct identity or source truth. |

Resource bytes and annotation spans are retained operands, not evidence that every resource expresses a theory. Their generic admission/read-back is supplied by [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission) and [RT-RTE-mark-detection](runtime.md#rt-rte-mark-detection); this inventory splits material generated parts rather than duplicating a memory-store inventory.

## Authority-route ledger

Each compact row below is a consequential function. Fields owned by shared records are referenced rather than copied. All architectural statuses concern inspected wiring, not observed operation.

Route ID: [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-job-params](runtime.md#rt-obj-job-params)
Content/update relation: truth-apt transformation: acquisition/import; source warrant unknown. Selected retained passages enter a new request context, without an acceptance decision.
Transition or check target: see route.
Evaluator/condition and domain: see route.
Activation and timing: see route.
Possible or observed result: see route; implementation only.
Implemented force: see route.
Epistemic authority and scope: source attribution permits tracing selected content, not treating it as true.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: see [RT-BAP-generation-prompt](runtime.md#rt-bap-generation-prompt).
Evidence source ID and local anchor: see route.
Claim IDs: [EPI-CLM-trusted-knowledge](#epi-clm-trusted-knowledge).
Mismatch marker: warrant unknown.
Gap/limit: no supplied source-verification or deployment evidence.

Route ID: [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-generated-document](#epi-obj-generated-document)
Content/update relation: truth-apt transformation: indeterminate. Inputs are transformed into model prose; without a response, neither faithful reshaping nor entailment nor non-entailment is established. Novelty instructions alone would not establish an ampliative proposition.
Transition or check target: see route.
Evaluator/condition and domain: see route.
Activation and timing: see route.
Possible or observed result: see route; no observed candidate.
Implemented force: see route.
Epistemic authority and scope: candidate generation, not factual acceptance.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: see [RT-BAP-generation-prompt](runtime.md#rt-bap-generation-prompt).
Evidence source ID and local anchor: see route.
Claim IDs: [RT-CLM-source-grounding](runtime.md#rt-clm-source-grounding).
Mismatch marker: source-grounding instruction is not a guarantee.
Gap/limit: no evidence-consuming decision naming a factual criterion, intended use and scope is established by this generation path.

Route ID: [EPI-RTE-citation-processing](#epi-rte-citation-processing)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-generated-document](#epi-obj-generated-document)
Content/update relation: truth-apt transformation: non-ampliative reshaping. Token removal changes presentation and retains the asserted sentence, including where attribution is refused.
Transition or check target: see route's transformation case.
Evaluator/condition and domain: see route.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: see route.
Epistemic authority and scope: no added truth warrant.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: see route.
Evidence source ID and local anchor: see route.
Claim IDs: [RT-CLM-source-grounding](runtime.md#rt-clm-source-grounding).
Mismatch marker: invalid source tokens do not veto their associated propositions.
Gap/limit: sentence boundaries are syntactic heuristics, not semantic claim individuation.

Route ID: [EPI-RTE-citation-processing](#epi-rte-citation-processing)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-generated-document](#epi-obj-generated-document)
Content/update relation: no content change.
Transition or check target: see route's ID/preceding-span check.
Evaluator/condition and domain: see route.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: see route's check result; disposition is separated below.
Epistemic authority and scope: allowed-ID membership and a preceding syntactic span only; neither source entailment nor full prompt visibility.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: see route.
Evidence source ID and local anchor: see route.
Claim IDs: [RT-CLM-source-grounding](runtime.md#rt-clm-source-grounding).
Mismatch marker: full-context allowlist is broader than clipped prompt passages.
Gap/limit: independent annotation-ID and resource-ID membership does not check that their pair denotes the actual source relationship.

Route ID: [EPI-RTE-citation-processing](#epi-rte-citation-processing)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-generated-document](#epi-obj-generated-document)
Content/update relation: no content change.
Transition or check target: see route's citation admission decision.
Evaluator/condition and domain: see route.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: see route.
Epistemic authority and scope: structural eligibility to create citation metadata, not acceptance of the cited proposition for a knowledge use.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: see route.
Evidence source ID and local anchor: see route.
Claim IDs: [RT-CLM-source-grounding](runtime.md#rt-clm-source-grounding).
Mismatch marker: none beyond the preceding check limits.
Gap/limit: warning/drop acts on metadata, not resource retention.

Route ID: [EPI-RTE-citation-retention](#epi-rte-citation-retention)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-generated-document](#epi-obj-generated-document)
Content/update relation: no content change.
Transition or check target: see route.
Evaluator/condition and domain: see route.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: see route.
Epistemic authority and scope: no durable generated-citation authority from this caller; constructed links are not admitted, and no lifecycle integration after factual acceptance is established.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: see route.
Evidence source ID and local anchor: see route.
Claim IDs: [RT-CLM-source-grounding](runtime.md#rt-clm-source-grounding).
Mismatch marker: nonempty generated-citation batches are refused for missing job assignment on the new resource; resource upload and source linkage are separate effects.
Gap/limit: architectural status describes implemented construction and commit/refusal branches, not successful retention. An empty batch is skipped and can permit completion without citations.

Route ID: [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-generated-document](#epi-obj-generated-document), or imported caller bytes.
Content/update relation: truth-apt transformation: acquisition/import for external caller content, with source warrant unknown; no additional content change for the already-generated document.
Transition or check target: see route.
Evaluator/condition and domain: see route.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: see route.
Epistemic authority and scope: provenance/format acceptance licenses recording, not factual reliance. Imported content is acquired, not newly produced knowledge.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: see route.
Evidence source ID and local anchor: see route.
Claim IDs: [EPI-CLM-trusted-knowledge](#epi-clm-trusted-knowledge).
Mismatch marker: direct upload bypasses generation and citation processing.
Gap/limit: generic principal does not identify human versus software authorship or per-item approval.

Route ID: [RT-RTE-pdf-repair](runtime.md#rt-rte-pdf-repair)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-generated-document](#epi-obj-generated-document)
Content/update relation: no content change in compiler judgment.
Transition or check target: Typst source compilability in the configured compiler environment; see route.
Evaluator/condition and domain: see route.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: compiler diagnostic consumed by the separate disposition/repair function below.
Epistemic authority and scope: compilation/rendering success only, not factual correctness, faithful rendering of every claim, safety or transfer.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: see route.
Evidence source ID and local anchor: see route.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: no compiler execution supplied.

Route ID: [RT-RTE-pdf-repair](runtime.md#rt-rte-pdf-repair)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-generated-document](#epi-obj-generated-document)
Content/update relation: no content change in selection; replacement source generation remains semantically indeterminate.
Transition or check target: see route.
Evaluator/condition and domain: see route.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: see route.
Epistemic authority and scope: accepts artifact for PDF upload after compilation and budget checks, not a truth-apt ampliative claim against evidence.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: see route.
Evidence source ID and local anchor: see route.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: bounded repair is feedback on a work product, not proof of generalized learning or a revised system method.

Route ID: [EPI-RTE-assessment-proposal](#epi-rte-assessment-proposal)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-assessment-text](#epi-obj-assessment-text)
Content/update relation: truth-apt transformation: indeterminate for generated assessment assertions; non-truth-apt policy/content update: concern or recommendation where no truth-apt proposition is individuated.
Transition or check target: see route.
Evaluator/condition and domain: see route.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: see route; critical prose is advisory, not automatic source rejection.
Epistemic authority and scope: candidate content-directed criticism; no independent verification of the criticism or required changed reliance.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: see route.
Evidence source ID and local anchor: see route.
Claim IDs: [EPI-CLM-assessment-concerns](#epi-clm-assessment-concerns).
Mismatch marker: none; bounded evaluation is a real distinct capability.
Gap/limit: no observed assessment instance or revision loop.

Route ID: [EPI-RTE-span-check](#epi-rte-span-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-assessment-text](#epi-obj-assessment-text)
Content/update relation: no content change in the check.
Transition or check target: see route.
Evaluator/condition and domain: see route.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: see route; disposition separated below.
Epistemic authority and scope: evidence of recoverable source span, with ambiguity/degradation warnings, not truth of the accompanying judgment.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: see route.
Evidence source ID and local anchor: see route.
Claim IDs: [EPI-CLM-assessment-concerns](#epi-clm-assessment-concerns).
Mismatch marker: none.
Gap/limit: reconciliation implementation itself not inspected; no exact-location guarantee for fuzzy/first-of-many results.

Route ID: [EPI-RTE-span-check](#epi-rte-span-check)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-assessment-text](#epi-obj-assessment-text)
Content/update relation: no content change to the assessment body; source span may be reconciled to source wording.
Transition or check target: see route.
Evaluator/condition and domain: see route.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: see route.
Epistemic authority and scope: eligibility for annotation construction/commit; not acceptance of the assessment as fact.
Operational authority: behavior permitted, blocked, or changed: see route and [RT-RTE-mark-detection](runtime.md#rt-rte-mark-detection).
Behavioral-authority path: see route.
Evidence source ID and local anchor: see route.
Claim IDs: [EPI-CLM-assessment-concerns](#epi-clm-assessment-concerns).
Mismatch marker: none.
Gap/limit: warnings for doubtful anchors do not veto commit.

Route ID: [EPI-RTE-summary-generation](#epi-rte-summary-generation)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-gathered-prose](#epi-obj-gathered-prose)
Content/update relation: truth-apt transformation: indeterminate. Requested summarization does not establish semantic preservation; requested referent suggestions may not be truth-apt.
Transition or check target: see route.
Evaluator/condition and domain: see route.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: see route.
Epistemic authority and scope: generated contextual candidates without a fidelity or factual-acceptance gate in the inspected functions.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: see route.
Evidence source ID and local anchor: see route.
Claim IDs: [EPI-CLM-trusted-knowledge](#epi-clm-trusted-knowledge).
Mismatch marker: source identifiers accompany prose but do not verify it.
Gap/limit: no actual response available for semantic classification.

Route ID: [EPI-RTE-reference-search](#epi-rte-reference-search)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-reference-score](#epi-obj-reference-score)
Content/update relation: non-truth-apt policy/content update: heuristic ranking of possible referents; descriptions are non-ampliatively reshaped from retrieved descriptors.
Transition or check target: see route.
Evaluator/condition and domain: see route.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: see route.
Epistemic authority and scope: rank for candidate inspection, not correct-reference acceptance or endorsement of resource claims.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: see route.
Evidence source ID and local anchor: see route.
Claim IDs: [EPI-CLM-trusted-knowledge](#epi-clm-trusted-knowledge).
Mismatch marker: none.
Gap/limit: separate bind action records a choice; no supplied evidence that ranking causes that choice or that a chosen referent is correct.

Route ID: [EPI-RTE-knowledge-withdrawal](#epi-rte-knowledge-withdrawal)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-assessment-text](#epi-obj-assessment-text), [EPI-OBJ-generated-document](#epi-obj-generated-document), or other retained annotations/resources.
Content/update relation: non-truth-apt policy/content update: remove, archive, restore or edit availability/metadata; supplied body edits may independently change truth-apt content with unknown warrant.
Transition or check target: see route.
Evaluator/condition and domain: see route.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: see route.
Epistemic authority and scope: caller-requested withdrawal is an operative change to availability, not a recorded evidence-based retraction verdict.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: see route.
Evidence source ID and local anchor: see route.
Claim IDs: [EPI-CLM-trusted-knowledge](#epi-clm-trusted-knowledge).
Mismatch marker: none.
Gap/limit: no recursive retraction of already-generated descendants established by the inspected handlers/folds.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-trusted-knowledge](#epi-clm-trusted-knowledge) | see record | see record | see record | [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission), [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather), [EPI-RTE-citation-retention](#epi-rte-citation-retention), [EPI-RTE-knowledge-withdrawal](#epi-rte-knowledge-withdrawal) | none supplied | No causal comparison; corpus and provider quality excluded | Resource admission, source binding/linking, editing and retrieval are implemented; generated-citation retention from this caller is blocked | “Trusted” and “accurate” are aims, not demonstrated truth guarantees or measured accuracy. |
| [RT-CLM-source-grounding](runtime.md#rt-clm-source-grounding) | see record | see record | see record | [EPI-RTE-citation-processing](#epi-rte-citation-processing), [EPI-RTE-citation-retention](#epi-rte-citation-retention), [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation) | none supplied | No semantic/factual oracle or comparison | Conditional grounding instruction, structural citation processing and attempted commit; not durable generated citations | Nonempty batches are refused before recording because their target resource lacks the original job assignment. Empty batches skip commit and can complete. IDs may be allowed without their text surviving clipping; dropped tokens leave claims; ordinary MCP route omits cite. |
| [EPI-CLM-assessment-concerns](#epi-clm-assessment-concerns) | see record | see record | see record | [EPI-RTE-assessment-proposal](#epi-rte-assessment-proposal), [EPI-RTE-span-check](#epi-rte-span-check), [RT-RTE-mark-detection](runtime.md#rt-rte-mark-detection) | none supplied | Model quality unmeasured; no source-revision effect observed | Model judgments and manual concerns can be retained and later consumed | Neither an assessing motivation nor a source anchor establishes valid criticism, acceptance or correction of source claims. |
| [EPI-CLM-conformance-scope](#epi-clm-conformance-scope) | see record | see record | see record | No product authority route asserted by this documentation claim | none supplied | Scripted model/embedding stand-ins constrain what even a successful run could establish | Declared protocol evaluation design, not factual-knowledge evaluation | Assertions and runs uninspected; no passing result inferred. |

## Bounded conclusion

**Resource provenance and operational admission are implemented; generated-citation retention from this caller is blocked, and factual acceptance is not established for the assessed generated-content paths.** [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission) permits external imports and generated artifacts under identity, format and attribution rules. It licenses persistence and later retrieval, not the truth of uploaded propositions. Source warrant is unknown at import. [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather) and [EPI-RTE-summary-generation](#epi-rte-summary-generation) assemble and generate context; subsequent prompt selection can omit gathered material. Neither summaries nor generated documents can be classified as entailed derivations or actual ampliative conjectures without their propositions and inputs. No warranted-premise derivation is established merely by a source ID.

**Checks have real but narrow force.** [EPI-RTE-citation-processing](#epi-rte-citation-processing) can refuse a citation without refusing the associated sentence. [EPI-RTE-citation-retention](#epi-rte-citation-retention) constructs links after artifact upload but its nonempty batch is refused before recording: the held job is assigned on the original resource, while citation commit checks the new resource's log. SDK refusal propagation prevents completion and enters Worker failure handling without withdrawing the artifact or any successful source linkage. Empty batches, including when PDF anchoring drops every citation, skip commit and can permit completion without citations. [EPI-RTE-span-check](#epi-rte-span-check) can prevent an unanchorable annotation from being built, but fuzzy/ambiguous matches are warnings rather than vetoes. [RT-RTE-pdf-repair](runtime.md#rt-rte-pdf-repair) supplies an enforcing compiler result for PDF construction, with a bounded repair horizon; compilation is not source entailment or source truth. These narrow acceptance criteria do not constitute an evidence-consuming decision accepting an ampliative claim for a named factual use. Retention and linking therefore remain distinct from lifecycle integration after such acceptance.

**Model criticism and ranking are separate capabilities, not absent evaluation.** [EPI-RTE-assessment-proposal](#epi-rte-assessment-proposal) requests criticism of source passages and can retain it without per-item human approval. Its later authority is advisory prose, including when an assessment in focus reaches generation. [EPI-RTE-reference-search](#epi-rte-reference-search) uses program and optional model scores to rank possible referents, not to prove them correct. [EPI-RTE-knowledge-withdrawal](#epi-rte-knowledge-withdrawal) implements caller-controlled removal/archive/body changes and projection consequences; this is a counterexample to an assertion that reliance can never change. It is not evidence of automatically propagated truth retraction or revision of all prior products.

**No single system-wide epistemic verdict follows.** The conformance documentation concerns protocol behavior with scripted inference, not model accuracy. The assessed routes wire knowledge retention, model-based criticism, local repair and future context supply; exercised improvement remains unobserved. No response instance establishes a formulated explanatory theory undergoing blame-directed criticism and retained iterative revision. That limit does not negate the implemented assessment capability. Reflection, autonomous theory building and learning are not inferred from it. Compiler feedback changes the current work product; no generalized policy update is established. A claim of exercised self-improvement would additionally require evidence that an objective-responsive update enters the system's organization and causally affects subsequent operation, which is not supplied here. Uninspected Browser/desktop, import, hooks, maintenance and provider alternatives prevent extending these route-local findings to every shipped path.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-generated-document
Label: GeneratedDocument content

Source-native identity: `GeneratedDocument.content` and the artifact text derived from it. Natural-language propositions in Markdown/plain text; PDF generation mixes natural-language assertions with symbolic Typst source. Substrate: current-job Python string, then artifact bytes admitted as a resource. Closest supplied record is [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation), a producing route rather than this output object; no supplied object counterpart. No actual document instance supplied. SRC-1, `apps/worker/src/semiont_worker/generation/resource_generation.py`, `apps/worker/src/semiont_worker/processors.py`.

> class GeneratedDocument:
>     """What a model wrote."""
>
>     content: str
> --- `apps/worker/src/semiont_worker/generation/resource_generation.py`

#### EPI-OBJ-assessment-text
Label: AssessmentMatch assessment

Source-native identity: `AssessmentMatch.assessment`, copied into an assessing TextualBody. Natural-language judgment distinct from the symbolic target span and source ID; substrate is current-job match state and then annotation records. Closest supplied [RT-RTE-mark-detection](runtime.md#rt-rte-mark-detection) is the production/commit route, not an object counterpart. SRC-1, `apps/worker/src/semiont_worker/detection/parsers.py`, `apps/worker/src/semiont_worker/processors.py`.

> class AssessmentMatch(TextSpan):
>     """A passage of the text, and the model's judgement of it, as written."""
>
>     assessment: str
> --- `apps/worker/src/semiont_worker/detection/parsers.py`

#### EPI-OBJ-gathered-prose
Label: Gathered summary prose

Source-native identity: natural-language `summary` and suggested-reference fields produced for resource gather and annotation summary; relationship prose belongs to the adjacent supplied [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather). Substrate: request-local response fields, optionally copied by clients into job context; no durable summary store in these functions. Distinct from [RT-OBJ-job-params](runtime.md#rt-obj-job-params): that is a later queue input, not this producer's response. SRC-1, `apps/librarian/src/semiont_librarian/resource_gather.py`, `apps/librarian/src/semiont_librarian/summary.py`.

> summary = await ask(inference, asking)
> --- `apps/librarian/src/semiont_librarian/summary.py`

#### EPI-OBJ-reference-score
Label: Score points and reason

Source-native identity: `Score.points`, `Score.reason`, then `ScoredResource.score`/`matchReason`. Symbolic numeric heuristic consumed by sorting; natural-language explanation consumed by people/models. Substrate: request-local Python records and serialized response, not trained parameters. No supplied object counterpart; adjacent [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather) assembles context rather than these candidate scores. SRC-1, `apps/librarian/src/semiont_librarian/score.py`, `apps/librarian/src/semiont_librarian/reference_search.py`.

> return Score(points=rounded(score.points + model_score * 25), reason=reason)
> --- `apps/librarian/src/semiont_librarian/score.py`

### Routes

#### EPI-RTE-citation-processing
Label: Citation token processing
Part of: [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation)

Endpoints/progression: generated string → `resolve_citation_tokens` → clean text and candidate citation spans → artifact builder. Worker symbolic code owns progression. This part separates three functions in the ledger: token transformation, ID/span checking, and citation disposition. SRC-1 implementation, `apps/worker/src/semiont_worker/generation/citations.py`, `apps/worker/src/semiont_worker/processors.py`, `apps/worker/src/semiont_worker/generation/resource_generation.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `ResolvedCitations(content, citations)` to processor.
- Later read-back: inapplicable — processing itself is current-job state; artifact/link retention is the separate citation-retention route.
- Delegated visibility: artifact builder receives cleaned text and admitted citation metadata; warnings go to logging, not a required model revision.
- Selection predicate: only active when cite produces a non-null citable set; syntactically recognized tokens are removed, resource/annotation IDs parsed and checked against independent sets, then preceding sentence span located.
- Invalidation or expiry: current output replaces the local generated string; no source claim withdrawal or expiry is applied.
- Activation or effect: code uses clean text for stored/compiled output and resolved spans for citation annotation construction. No operation observed.
- Evidence limits: structural membership only; no comparison of proposition content with source content, pair relationship or the final model-visible prompt.

The model proposes tokens; code decides eligibility and vetoes citation metadata, not the sentence. Operating mode is open-request generation, not an accuracy experiment; no expected-answer oracle. Guidance requests source-ID citations under cite; cleaned document content can persist through upload, while eligible citation metadata proceeds to the separate commit attempt, whose nonempty batch is refused. The allowlist includes every semantic match in the supplied context; prompt code sorts and keeps three, clipping each to 240 code points. Graph resource nodes also enter the allowlist without a check that their asserted evidence text appeared in the final prompt. This bounds the runtime shorthand “what the context showed”; it does not supersede the valid generation container record.

Concrete source deduction, not execution: take `content = "The moon is cheese. [[ghost]]"` and empty citable sets. The regex recognizes the token; `rstrip(" \t")` leaves `The moon is cheese.`. Whether `ghost` fails parsing or just membership, that branch continues without a citation. Final content is the false proposition unchanged and the citation list is empty. Thus an invalid source token is not a factual veto. No test fixture or target run was created.

> clean += content[last : token.start()].rstrip(" \t")
>         last = token.end()
> --- `apps/worker/src/semiont_worker/generation/citations.py`

> if resource_id is None or resource_id not in citable.resource_ids:
>             LOG.warning("Citation token references an id absent from the provided context — dropped", extra={"resourceId": cited})
>             continue
> --- `apps/worker/src/semiont_worker/generation/citations.py`

> if context.semantic_context is not None:
>         for match in context.semantic_context.similar:
>             resource_ids.add(match.resource_id)
>             if match.annotation_id is not None:
>                 annotation_ids.add(match.annotation_id)
> --- `apps/worker/src/semiont_worker/generation/citations.py`

Prompt selection contrast is also supported by the retained sorting passage in [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation).

#### EPI-RTE-citation-retention
Label: Citation annotation retention
Part of: [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation)

Endpoints/progression: uploaded artifact/resource ID and resolved citations → `_citations` → `job.commit` attempt on generated resource → SDK attaches original job ID → Archivist `requester_of` checks the target resource's log → missing-assignment refusal before any annotation recording. Dispatcher assigned this job on the original focus resource, not the newly minted resource. Worker owns construction; Archivist owns refusal; the SDK rethrows the non-timeout refusal and Worker enters failure handling rather than completion. Source inputs and effect order differ from pre-upload token processing. SRC-1 implementation, `apps/worker/src/semiont_worker/held_job.py`, `apps/worker/src/semiont_worker/generation/claim_search.py`, `packages/sdk-python/src/semiont/claims.py`, `apps/dispatcher/handlers/src/handlers.rs`, `apps/archivist/src/commands.rs`, `apps/archivist/src/bus.rs`. The supplied [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation) independently retains this same parent-chain mismatch.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `_citations` returns constructed link annotations; a nonempty batch receives a commit refusal, not acknowledgement. An empty batch returns without sending a commit and can permit parent completion.
- Later read-back: no generated-citation annotations from this nonempty batch reach later browse/graph/gather because admission refuses before recording. Uploaded resource and successful source linkage have separate read-back paths.
- Delegated visibility: proposed link body carries cited resource ID; the token's annotation ID is not included in the `citing` body constructor. Refusal propagates to Worker failure handling, not to an automatic citation repair loop.
- Selection predicate: non-PDF offsets use cleaned artifact text; PDF citations require re-readable generated PDF text and a found span. Missing text drops all citations; missing claim drops that citation. Any remaining nonempty batch faces the target-log assignment check.
- Invalidation or expiry: dropping or refusing links does not withdraw the already-uploaded resource or successful source linkage; later source changes are not checked here.
- Activation or effect: construction and attempted commit are wired, but durable generated-citation admission is blocked by the assignment mismatch. Refusal prevents the subsequent completion call and triggers attempted failure reporting; no operation observed.
- Evidence limits: wired describes these construction/refusal branches, not successful retention. No alternative assignment transfer or successful citation-commit path is established in this inspected chain. First matching PDF text span can be an imperfect identity for repeated prose; no semantic acceptance or recursive invalidation proof.

Trigger is completion of artifact upload. Software constructs candidate links under source-ID and anchor rules; Archivist can veto their admission and does so for this caller's nonempty batch. A caller requested generation but supplies no per-link approval here. No semantic answer oracle. This is open-request attempted operational linking, not lifecycle integration after factual acceptance. Refusal is not a distributed rollback of resource creation; see [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission). Consumer/channel/force/horizon: Archivist consumes SDK `mark:commit` provenance with enforcing refusal before recording; the SDK consumes the failure reply and raises; Worker failure handling attempts to settle the current job. There is no later generated-citation provenance channel from this batch. Upload attribution checks the assignment on `generatedFrom.resourceId`, so successful upload does not satisfy the distinct citation-target check. Existing source binding/linking remains supported. The generic commit mechanism can record properly assigned source-resource annotations; that countercase does not rescue this new-resource batch.

> resource_id: job.params.resource_id.clone(),
>             holder,
>             requester: job.metadata.user_id.clone(),
> --- `apps/dispatcher/handlers/src/handlers.rs`

> await self._answered(MARK_COMMIT, MarkCommitCommand(resource_id=resource_id, annotations=list(annotations), job_id=self.job_id))
> --- `packages/sdk-python/src/semiont/claims.py`

> Some(job_id) => requester_of(archivist, resource_id, job_id, user)?,
> --- `apps/archivist/src/commands.rs`

> "refused: cites job {job_id}, but this resource's log holds no assignment for it"
> --- `apps/archivist/src/commands.rs`

> if not annotations:
>             # A batch of no annotations is no commit: there is nothing to establish.
>             return
> --- `packages/sdk-python/src/semiont/claims.py`

> if unanswered.code != "bus.timeout":
>                 raise
> --- `packages/sdk-python/src/semiont/claims.py`

> Err(refusal) => Reply {
>             channel: operation.failure,
>             payload: refused(refusal),
>         },
> --- `apps/archivist/src/bus.rs`

> except Exception as failure:
>                 await _fail(job, failure, reports, stood)
> --- `apps/worker/src/semiont_worker/held_job.py`

> def citing(cited: ResourceId) -> SpecificResource:
>         return SpecificResource(type="SpecificResource", source=cited, purpose="linking")
> --- `apps/worker/src/semiont_worker/held_job.py`

> await job.commit(new_resource_id, await _citations(job, client, made, new_resource_id, generator, reports))
> --- `apps/worker/src/semiont_worker/held_job.py`

> if found is None:
>             LOG.warning(
>                 "PDF citation dropped \N{EM DASH} claim not found in the rendered text",
> --- `apps/worker/src/semiont_worker/held_job.py`

#### EPI-RTE-assessment-proposal
Label: Assessment proposal
Part of: [RT-RTE-mark-detection](runtime.md#rt-rte-mark-detection)

Endpoints/progression: assessing job/source text and instructions → assessment prompt/model response → parsed assessment matches → annotation construction and chunk callback. Worker code selects processor; model evaluates passage validity/strength/implications. This is the assessing part, not every mark motivation. SRC-1, `apps/worker/src/semiont_worker/detection/prompts.py`, `apps/worker/src/semiont_worker/detection/parsers.py`, `apps/worker/src/semiont_worker/processors.py`; CLI entry in `apps/launcher/internal/verbs/mark.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: candidate assessments and anchored matches for annotation construction; parent returns counts/decline or failure.
- Later read-back: assessing bodies are committed by parent mark route and can reach later browse/gather/generation. Generation explicitly reads the first textual body for an annotation in focus.
- Delegated visibility: model sees selected source piece and job guidance; consumers receive assessment prose and source target, not an authenticated chain of the model's reasoning.
- Selection predicate: motivation assessing; instructions, tone, density and language shape model requests; structurally invalid/blank proposals are excluded and anchoring is separately assessed.
- Invalidation or expiry: chunk commits can survive job cancellation/failure; callers can later edit/delete annotations through a separate route.
- Activation or effect: processor constructs assessing bodies, commits through the parent callback, and future prompt assembly can include them. No observed changed reliance.
- Evidence limits: generated criticism may state truth-apt claims or recommendations; no response instance, independent source check or mandated source revision is supplied.

The model proposes judgments; code admits anchored text; callers can cancel later work or edit/delete retained concerns. No independent expected-answer oracle. Open-request mode, not a controlled curriculum. Starting a job is not per-item human approval. Guidance asks for criticism and exact quotations, and assessment prose persists, not a revised theory by default. The resulting source assessment is advisory: later generation's natural-language prompt can consume it for one invocation; persistence can extend availability across requests. The input text is not automatically rejected merely because an assessment criticizes it. This is a positive evaluation route, with unresolved validity and consequence rather than an absence of evaluation.

> - "assessment": your analytical assessment (1-3 sentences, evaluate validity/strength/implications)
> --- `apps/worker/src/semiont_worker/detection/prompts.py`

> lambda found, assessment: AssessmentMatch(
>             start=found.start, end=found.end, exact=found.exact, prefix=found.prefix, suffix=found.suffix, assessment=assessment
>         ),
> --- `apps/worker/src/semiont_worker/detection/parsers.py`

> first = annotation.body[0] if isinstance(annotation.body, list) else annotation.body
>         if isinstance(first, TextualBody) and first.value:
>             label = "Comment" if annotation.motivation == "commenting" else "Assessment"
>             parts.append(f"- {label}: {first.value}")
> --- `apps/worker/src/semiont_worker/generation/resource_generation.py`

#### EPI-RTE-span-check
Label: Detection span check
Part of: [RT-RTE-mark-detection](runtime.md#rt-rte-mark-detection)

Endpoints/progression: parsed proposals and full source text → `reconcile` → found/not-found → anchored match or omission → annotation builder/commit callback. Owner is symbolic parser code; audit logging classifies doubtful anchors. Ledger separates check from disposition. SRC-1, `apps/worker/src/semiont_worker/detection/parsers.py`, `apps/worker/src/semiont_worker/detection/anchor_audit.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: found matches and dropped count.
- Later read-back: inapplicable — this check stores no independent evidence artifact; retained annotations/read-back belong to the parent mark route.
- Delegated visibility: source span uses reconciled source wording; assessment/comment body is passed along as written. Logging exposes degraded anchor method.
- Selection predicate: valid proposal → reconcile against source → absent span omitted; found span accepted, including first-of-many/fuzzy-match with warning.
- Invalidation or expiry: current batch only; no later revalidation of source edits in this function.
- Activation or effect: not-found prevents annotation construction for that proposal; found match reaches builder. Warning does not block.
- Evidence limits: source text is an anchoring reference outcome, not an oracle for body truth; reconciliation internals and exact deployed extraction fidelity uninspected.

Model proposes quote and assessment; code decides whether the quote can be placed. This is automatic operational acceptance for annotation construction, not epistemic acceptance of the judgment. No per-proposal human veto is required here. Parent route controls cancellation/recovery and retains guidance/body effects. An anchor target is checked against supplied text in the current request; no claim of source truth or unique intended occurrence follows from finding words.

> found = reconcile(text, quoted)
>         if found is None:
>             LOG.warning("Proposal dropped — text not found in source", extra={**of, "text": quoted.exact})
>             continue
>         note_anchor(label, quoted.exact, found.anchor_method)
>         matches.append(match(found, said))
> --- `apps/worker/src/semiont_worker/detection/parsers.py`

> _DOUBTFUL: Final[frozenset[AnchorMethod]] = frozenset({"first-of-many", "fuzzy-match"})
> --- `apps/worker/src/semiont_worker/detection/anchor_audit.py`

> if method in _DOUBTFUL:
>         LOG.warning("Annotation anchored via degraded method", extra={"label": label, "text": exact, "anchorMethod": method})
> --- `apps/worker/src/semiont_worker/detection/anchor_audit.py`

#### EPI-RTE-summary-generation
Label: Resource and annotation summaries

Distinct identity: [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather) covers assembly around an annotation, including linked-resource summary/relationship calls. This record covers the other shipped resource-gather summary/suggestion path and dedicated annotation-summary operation. They share the configured gatherer, but different request endpoints and response consumers; neither is exactly a part of that supplied route. SRC-1, `apps/librarian/src/semiont_librarian/resource_gather.py`, `apps/librarian/src/semiont_librarian/summary.py`.

Endpoints/progression: resource gather reads main text and optionally asks model for summary plus suggestions; dedicated summary resolves annotation/source window and asks model, returning contextual summary. Librarian code owns read/model/return progression. Natural-language model output is embedded in symbolic response envelopes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: resource GatheredContext with optional summary/suggestions, or ContextualSummaryResponse with source/annotation context.
- Later read-back: inapplicable — these functions persist no revised summary; a caller may copy returned resource context into a later generation job, whose prompt reads its summary/suggestions.
- Delegated visibility: resource model gets main text/name/types; annotation-summary model gets selected text with bounded before/after and types. Client receives resulting prose and relevant source fields.
- Selection predicate: resource include-summary and readable main text; annotation existence, matching target source and readable/placeable text for dedicated summary.
- Invalidation or expiry: response snapshot only. Resource summary/suggestion exception removes both fields and degrades response; dedicated summary model failure raises instead.
- Activation or effect: output fields are returned; resource-focused generation has explicit summary/suggested-reference prompt consumers. Actual reliance unobserved.
- Evidence limits: no semantic fidelity test or truth acceptance decision in inspected functions; separate failures have different continuation force.

No independent oracle or candidate contest; provider generates prose in open-request mode. Code can refuse missing source/annotation, but that validates prerequisites, not generated content. Source IDs preserve a route back to the input, not source truth. Force is advisory through prose, with code enforcing which fields reach the next caller. Horizon is current response, extended only when client stores/submits it. Summary guidance itself is static, and no inferred method update follows.

> summary = await ask(inference, resource_summary_prompt(name=main.name, content=main_text, entity_types=types))
>             suggesting = reference_suggestions_prompt(title=main.name, entity_type=types[0] if types else None)
>             suggestions = read_suggestions(await ask_for_elements(inference, suggesting, SUGGESTION_ELEMENT))
> --- `apps/librarian/src/semiont_librarian/resource_gather.py`

> summary, suggestions = None, None
> --- `apps/librarian/src/semiont_librarian/resource_gather.py`

> if focus.summary:
>         parts.append(f"- Summary: {focus.summary}")
>     if focus.suggested_references:
>         parts.append(f"- Suggested references: {', '.join(focus.suggested_references)}")
> --- `apps/worker/src/semiont_worker/generation/resource_generation.py`

#### EPI-RTE-reference-search
Label: Reference candidate scoring

Distinct identity: unlike [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather), this route consumes gathered context to rank possible binding targets. It is not that route's generic semantic-passage retrieval. SRC-1, `apps/librarian/src/semiont_librarian/reference_search.py`, `apps/librarian/src/semiont_librarian/score.py`.

Endpoints/progression: match-search context → name/type/neighborhood/vector candidates → structural score → optional model score for highest twenty → rerank/limit → client. Librarian symbolic code owns progression; model adds a bounded heuristic contribution. Score target is candidate relevance as possible referent under supplied context, not truth of all candidate claims.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: scored resources and match reasons, highest first and limited by request.
- Later read-back: inapplicable — score route persists no binding; a separate caller action can bind a chosen target. No retained learning from earlier scores in this function.
- Delegated visibility: model receives candidate descriptors plus selected context; client receives ordered descriptors/scores/reasons. No automatic bind in search.
- Selection predicate: own resource excluded; name/type/neighborhood/vector candidates merged; top twenty offered for optional model scoring, followed by rerank and limit.
- Invalidation or expiry: request snapshot; model/vector failure can fall back to structural scoring, except collection-absent error is raised. No enduring probability estimate or expiry policy.
- Activation or effect: scores change response ordering. Candidate binding and correctness are not established by delivery.
- Evidence limits: model-score reply parser uninspected; no calibration, expected referent labels or observed selection/benefit supplied.

Program terms include name similarity, entity-type overlap/rarity, connections, recency, vector similarity and multiple retrieval sources. A model score adds up to its contribution under the parser contract, not a truth verdict. No independent answer oracle. Open-request search; caller decides any later bind, whose MCP handler simply submits the chosen target. Consumer/channel/force/horizon: sorting code consumes numeric fields with ranking force for this answer; people/models receive reasons as advisory prose; a later bind can persist a caller's chosen relationship but that is not licensed by this search alone.

> scored.sort(key=lambda each: each[1].points, reverse=True)
>     if scored and request.use_semantic_scoring is not False:
>         shown = [resource for resource, _ in scored[:MOST_SHOWN]]
> --- `apps/librarian/src/semiont_librarian/reference_search.py`

> ordered = sorted(scored, key=lambda each: each[1].points, reverse=True)
> --- `apps/librarian/src/semiont_librarian/reference_search.py`

> if candidate.date_created:
>         points += _recency(candidate.date_created, moment)
> --- `apps/librarian/src/semiont_librarian/score.py`

#### EPI-RTE-knowledge-withdrawal
Label: Knowledge withdrawal and editing

Distinct identity: [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission) creates resources; [RT-RTE-mark-detection](runtime.md#rt-rte-mark-detection) creates detected annotations. Neither covers these removal/archive/body-update commands and their derived-read effects. SRC-1, `apps/archivist/src/commands.rs`, `apps/weaver/src/semiont_weaver/fold.py`, `apps/smelter/src/semiont_smelter/smelter.py`.

Endpoints/progression: caller mark-delete/archive/unarchive/update-body or bind-update-body → Archivist event → graph/vector event consumers. Archivist owns command execution; Weaver/Smelter own their projection effects. Context is specified resource/annotation identity and command payload, not model judgment. The record remains event-based; this does not erase historical events.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: command acknowledgement after event append; archive may remove file first unless keep-file, and unarchive can refuse missing file.
- Later read-back: Weaver deletes removed annotation, updates body, or changes archive flag; Smelter deletes removed-annotation vectors and resource/annotation vectors on archive, restores by reindexing on unarchive, and restamps on body change. Later graph/vector reads can therefore differ.
- Delegated visibility: consumers receive event type and target identity/operations; no evidence-based reason for withdrawal is required by these handlers.
- Selection predicate: explicit caller target/operation; projection match branches choose effect by event type.
- Invalidation or expiry: active graph/index availability changes; archive is reversible where content exists; delete/body edits are not shown to recursively revise descendant generated content.
- Activation or effect: event append and projection mutations are wired. Failure/lag can delay derived effects; actual operation and full repair behavior uninspected.
- Evidence limits: no complete access-control or consistency audit, no observed withdrawal, and no global assertion that all consumers suppress archived content.

Caller proposes/decides the change; code executes or refuses prerequisites. Caller human versus software authorship is unresolved. No expected-answer oracle or mandated factual criterion; open requests. What persists is an event and changed active state, not necessarily the reason for a retraction. Consumer/channel/force/horizon: projection handlers consume event types with enforcing deletion/update force for future graph/vector retrieval; prior by-value contexts and stored descendants are not automatically rewritten by the inspected branches. Thus an implemented withdrawal path exists, without establishing epistemic retraction propagation.

> archivist.append(event(MarkRemoved::NAME, Some(resource_id), user, payload))?;
> --- `apps/archivist/src/commands.rs`

> case "mark:removed":
>             await graph.delete_annotation(MARK_REMOVED.event(event).annotation_id)
>         case "mark:body-updated":
>             await _update_body(graph, event)
> --- `apps/weaver/src/semiont_weaver/fold.py`

> await self._index.delete_annotation_vectors_for_resource(resource)
> --- `apps/smelter/src/semiont_smelter/smelter.py`

### Claims

#### EPI-CLM-trusted-knowledge
Label: Trusted source-grounded knowledge

Claimed operation: shared source-grounded knowledge construction/governance for accurate applications. SRC-1 doctrine/design, `README.md`. No supplied claim counterpart after comparison with narrower [RT-CLM-source-grounding](runtime.md#rt-clm-source-grounding), which concerns conditional generation instructions rather than the platform's public purpose.

> **Semiont is an open, source-grounded semantic knowledge platform for building and maintaining trusted AI knowledge bases and context layers. It gives humans and AI agents a shared workspace and architecture to annotate, connect, enrich, and govern domain knowledge for accurate applications, agents, and workflows.**
> --- `README.md`

#### EPI-CLM-assessment-concerns
Label: Assessment concerns

Claimed operation: assessment annotations evaluate passages and can feed aggregates. SRC-1 doctrine/design, `docs/builder/skills/semiont-assess/SKILL.md`. No supplied claim counterpart; closest [RT-RTE-mark-detection](runtime.md#rt-rte-mark-detection) is the encompassing implementation route, not this specific concern/reuse claim.

> An assessment evaluates a passage: a risk, a danger, an inaccuracy, a logical gap, a questionable assumption, or anything that deserves scrutiny.
> --- `docs/builder/skills/semiont-assess/SKILL.md`

> **Assessments feed aggregates.** To roll every flagged risk in a matter into one checklist or report, assess first and then run [`semiont-aggregate`](../semiont-aggregate/SKILL.md).
> --- `docs/builder/skills/semiont-assess/SKILL.md`

#### EPI-CLM-conformance-scope
Label: Librarian protocol conformance

Claimed operation: black-box protocol testing using scripted inference and embedding stand-ins. SRC-1 doctrine/design, `tests/conformance/librarian/README.md`. No supplied claim counterpart; boundary cites this design but declares no corresponding CLM record. Not an accuracy or observed-operation claim.

> A black-box suite for the Librarian: the process a librarian image runs. It
> starts the Librarian from a command and meets it only where the rest of
> Semiont does: on the bus, at its providers, and at its health port. It checks
> what the Librarian does against
> [docs/protocol/LIBRARIAN.md](../../../docs/protocol/LIBRARIAN.md).
> --- `tests/conformance/librarian/README.md`

> **A model is asked nothing a case did not script.** A generation no case
> scripted fails the case, whatever it was about, and so does a request a
> stand-in does not serve.
> --- `tests/conformance/librarian/README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
