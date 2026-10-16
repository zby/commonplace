---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "DocMason epistemic routes: provenance, heuristic grounding, publication admission and interaction-derived reliance."
run-id: AAS-2026-10-13-docmason-deba9ae199d5-01
reviewed-boundary: f3970939593194a158ab7ea1d49995f06cbccc86
---

# DocMason epistemic report

## Source-and-claim boundary

The question is what licenses reliance on DocMason's acquired documents, generated semantics and answers, and which results change subsequent operation. Scope and exclusions are those of [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are in its [Source register](boundary.md#source-register). All additional source reads below are SRC-1 at the frozen commit. They establish implementation or doctrine/design, not execution. No target program was executed.

The supplied runtime is a provisional baseline, not an exhaustive epistemic audit. Direct inspection confirms its CLI split and adds the grounding classifier, knowledge-contract checks, overlay coverage, pending-interaction projection, memory ranking and orphan cleanup. These additions do not supersede its valid container records. Public warrant claims are [EPI-CLM-source-trust](#epi-clm-source-trust) and the narrower [RT-CLM-commit-gate](runtime.md#rt-clm-commit-gate).

| Entry point or operation | Source path, SRC-1 | Coverage and conclusion limit |
|---|---|---|
| Public CLI; hidden `_ask`, `_hook` | `src/docmason/cli.py` | Direct dispatch read; supplied [RT-RTE-canonical-ask](runtime.md#rt-rte-canonical-ask), [RT-RTE-host-hooks](runtime.md#rt-rte-host-hooks). No new public inference command found in this dispatch. |
| sync; validate-kb; publish | `src/docmason/knowledge.py` | Direct semantic-output and citation-check reads: [EPI-RTE-conservative-output](#epi-rte-conservative-output), [EPI-RTE-knowledge-check](#epi-rte-knowledge-check); supplied [RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish) for full admission/publication flow. Parser implementations and binary sample fidelity unassessed; prevents extraction-complete verdict. |
| retrieve; trace | `src/docmason/retrieval.py` | Direct classifier, trace consumer and memory-selector reads: [EPI-RTE-trace-check](#epi-rte-trace-check), [EPI-RTE-memory-selection](#epi-rte-memory-selection); reader/index scope otherwise supplied [RT-RTE-evidence-tools](runtime.md#rt-rte-evidence-tools). All ranking and graph branches not audited. |
| finalize; rejection/repair | `src/docmason/admissibility.py` | Direct state/scope rejection read plus supplied [RT-CLM-commit-gate](runtime.md#rt-clm-commit-gate). Exact-answer/version and external-manifest checks supplied, not independently re-audited here. |
| Semantic authoring and multimodal refresh | `skills/canonical/knowledge-construction/SKILL.md`; `skills/canonical/grounded-answer/SKILL.md`; `src/docmason/semantic_overlays.py`; `src/docmason/hybrid.py` | Direct contract, writer, validator and freshness/coverage reads; [EPI-RTE-overlay-coverage](#epi-rte-overlay-coverage), supplied [RT-RTE-hybrid-refresh](runtime.md#rt-rte-hybrid-refresh). Host visual interpretation and semantic criticism unobserved. |
| Native/canonical interaction capture, pending overlay, promotion, maintenance | `src/docmason/interaction.py` | Direct overlay, promoted reload, post-publish marking and orphan cleanup: [EPI-RTE-pending-overlay](#epi-rte-pending-overlay), [EPI-RTE-orphan-cleanup](#epi-rte-orphan-cleanup). Native reconciliation and semantic-kind inference not exhaustively inspected; complete correction/supersession semantics not established. |
| workflow operator evaluation | `src/docmason/evaluation.py`; `src/docmason/operator_eval.py` | Direct rubric aggregation and result persistence; supplied [RT-RTE-operator-eval](runtime.md#rt-rte-operator-eval) for candidate admission and baseline freezing. No supplied trials, baseline or experiment. |
| Adapter sync, updater, optional hooks | `src/docmason/commands.py`; `src/docmason/update_core.py`; `src/docmason/hooks.py` | Supplied [RT-RTE-adapter-sync](runtime.md#rt-rte-adapter-sync), [RT-RTE-core-update](runtime.md#rt-rte-core-update), [RT-RTE-host-hooks](runtime.md#rt-rte-host-hooks). Direct dispatch confirms exposure, not each implementation independently. These affect behavioral contracts, not factual acceptance. |
| prepare, doctor, status, setup/sample drivers | `src/docmason/cli.py`; `scripts/use-sample-corpus.py` | Dispatch directly read; driver scope supplied by boundary. Setup internals unassessed. No epistemic warrant inferred from readiness or materialization. |
| Projection workers, detailed artifacts/parsers and tests | `src/docmason/projections.py`; `src/docmason/_projection_worker.py`; `src/docmason/artifacts.py`; `tests/` | Relevant available material not fully inspected. Prevents a system-complete negative about derivation, criticism or semantic checking and any exhaustive source-preservation conclusion. |

No private corpus, generated KB, actual host answer/overlay lineage, evaluation artifacts or execution trace was supplied. This prevents claims that the reconstructed routes produced, accepted or improved any observed answer. Excluded host/provider internals prevent assessment of latent reasoning, model parameter updates, isolation and reliable rule adherence. The external distributed-parametric component's fixity and version limits are owned by [RT-CMP-host-agent](runtime.md#rt-cmp-host-agent). No system-wide absence of learning, reflection, autonomy or theory construction follows from these gaps.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-knowledge](#epi-obj-knowledge) | Source summaries, key points, claims, uncertainty and evidence references | see record | SRC-1, `src/docmason/knowledge.py` | Source statements are acquired; generated statement relations differ by branch. |
| [EPI-OBJ-semantic-overlay](#epi-obj-semantic-overlay) | Cross-region labels, annotations and relations; explicit uncertainty | see record | SRC-1, `src/docmason/semantic_overlays.py` | Authoring guidance is not observed semantic fidelity. |
| [EPI-OBJ-answer](#epi-obj-answer) | Host-authored answer propositions; refusals/composition may instead be non-truth-apt | see record | SRC-1, `skills/canonical/grounded-answer/SKILL.md` | No supplied instance permits claim-by-claim entailment assessment. |
| [EPI-OBJ-interaction-entry](#epi-obj-interaction-entry) | User/assistant interaction statements; intent and preferences may be policy rather than propositions | see record | SRC-1, `src/docmason/interaction.py` | Conversation lineage does not establish factual correctness. |
| [RT-OBJ-canonical-turn](runtime.md#rt-obj-canonical-turn) | None as business content; symbolic ownership, support and gate state | see record | SRC-1, `src/docmason/host_integration.py` | Controls legal closure, not sentence truth. |
| [RT-OBJ-publish-pointer](runtime.md#rt-obj-publish-pointer) | None as corpus content; symbolic current selection | see record | SRC-1, `src/docmason/versioning.py` | Current status is not endorsement. |

Evaluation expectations, scores and regression cases belong to [RT-RTE-operator-eval](runtime.md#rt-rte-operator-eval); they are reference and judgment artifacts for a bounded replay domain, not an independent corpus-wide truth oracle. Natural-language contracts reach the host through [RT-BAP-canonical-skills](runtime.md#rt-bap-canonical-skills).

## Authority-route ledger

Route ID: [RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-knowledge](#epi-obj-knowledge)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: private source material to staged evidence; source warrant unknown, with references and warnings retained.
Evaluator/condition and domain: see route for physical build; third-party parser truth/fidelity not assessed.
Activation and timing: see route.
Possible or observed result: see route; implementation only.
Implemented force: staged content becomes eligible for subsequent checking, not yet current-reader content.
Epistemic authority and scope: evidence of what extraction preserved, not endorsement of the source's assertions.
Operational authority: staged evidence can seed conservative semantics and bounded host authoring.
Behavioral-authority path: build/authoring consumers, file manifests and assets, permissive, build/follow-up horizon.
Evidence source ID and local anchor: SRC-1, `src/docmason/knowledge.py`.
Claim IDs: [EPI-CLM-source-trust](#epi-clm-source-trust).
Mismatch marker: provenance does not warrant source truth.
Gap/limit: source-format extraction fidelity and real corpus operation unobserved.

Route ID: [EPI-RTE-conservative-output](#epi-rte-conservative-output)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-knowledge](#epi-obj-knowledge)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: the generic branch's proposition about text included in staged evidence; not the truth of that text.
Evaluator/condition and domain: fixed template over actual snippet input; domain is staged representation only.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: writes a candidate knowledge object.
Epistemic authority and scope: checked code deduction supports the inclusion proposition, conditional on accurate snippet collection; underlying business claims remain imported.
Operational authority: candidate can proceed through contract validation and publication.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `src/docmason/knowledge.py`.
Claim IDs: [EPI-CLM-source-trust](#epi-clm-source-trust).
Mismatch marker: deterministic synthesis is not new warranted business knowledge.
Gap/limit: classification applies only to the concrete generic template traced below; other format/overlay-dependent branches require separate semantic assessment.

Route ID: [RT-RTE-hybrid-refresh](runtime.md#rt-rte-hybrid-refresh)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-semantic-overlay](#epi-obj-semantic-overlay); [EPI-OBJ-knowledge](#epi-obj-knowledge)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: host interpretation of structured/rendered evidence into semantic statements.
Evaluator/condition and domain: host reasoning guided to inspect real evidence and state uncertainty; authoring machinery is external.
Activation and timing: see route.
Possible or observed result: requested additive enrichment, capability blocker or uncertainty; no supplied generated instance.
Implemented force: authoring guidance; downstream file admission is implemented separately.
Epistemic authority and scope: instructions request warranted source-level semantics but establish neither entailment nor accepted ampliative production.
Operational authority: see route for bounded work and settlement.
Behavioral-authority path: see [RT-BAP-canonical-skills](runtime.md#rt-bap-canonical-skills).
Evidence source ID and local anchor: SRC-1, `skills/canonical/knowledge-construction/SKILL.md`.
Claim IDs: [EPI-CLM-source-trust](#epi-clm-source-trust).
Mismatch marker: author's evidence-binding metadata is not independent comprehension verification.
Gap/limit: actual claims/premises needed to distinguish reshaping, entailment and non-entailed conjecture. This status is for requested semantic production, not the implemented work-packet container.

Route ID: [EPI-RTE-knowledge-check](#epi-rte-knowledge-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-knowledge](#epi-obj-knowledge); [EPI-OBJ-semantic-overlay](#epi-obj-semantic-overlay)
Content/update relation: no content change
Transition or check target: staged artifact identity, schema, references, nonempty support and available assets.
Evaluator/condition and domain: see record; deterministic contract validation, not semantic entailment.
Activation and timing: see record.
Possible or observed result: errors/warnings and derived reader state; see record.
Implemented force: validation output feeds publish selection.
Epistemic authority and scope: citation resolvability, not whether cited text proves a proposition.
Operational authority: validation can block normal sync publication.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `src/docmason/knowledge.py`.
Claim IDs: [EPI-CLM-source-trust](#epi-clm-source-trust).
Mismatch marker: strict contract admission is narrower than factual correctness.
Gap/limit: no validated corpus instance or independent semantic acceptance demonstrated.

Route ID: [RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-knowledge](#epi-obj-knowledge)
Content/update relation: no content change
Transition or check target: eligibility of validated staging for normal publication.
Evaluator/condition and domain: see route; valid or warnings status consumed by sync.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: normal publication permitted/blocked; helper and arbitrary file writes have narrower guarantees.
Epistemic authority and scope: operational acceptance for reader publication under artifact contracts, not evidence-consuming acceptance of an ampliative claim's truth.
Operational authority: switches later readers' current KB.
Behavioral-authority path: see route and [RT-OBJ-publish-pointer](runtime.md#rt-obj-publish-pointer).
Evidence source ID and local anchor: SRC-1, `src/docmason/knowledge.py`.
Claim IDs: [EPI-CLM-source-trust](#epi-clm-source-trust).
Mismatch marker: publication is not semantic endorsement.
Gap/limit: integration after truth-apt acceptance is not established by this switch.

Route ID: [RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-knowledge](#epi-obj-knowledge); [EPI-OBJ-interaction-entry](#epi-obj-interaction-entry)
Content/update relation: no content change
Transition or check target: staged/published artifacts retained and interaction entries marked promoted.
Evaluator/condition and domain: see route; post-publication manifest membership drives marking.
Activation and timing: see route.
Possible or observed result: current artifacts and promoted status; old physical roots may be pruned.
Implemented force: later reload availability.
Epistemic authority and scope: retention of evidence/candidates, not truth acceptance.
Operational authority: later retrieve/trace can consume current records and promoted contexts.
Behavioral-authority path: see [RT-RTE-evidence-tools](runtime.md#rt-rte-evidence-tools).
Evidence source ID and local anchor: SRC-1, `src/docmason/interaction.py`.
Claim IDs: none.
Mismatch marker: promoted is a storage lifecycle state.
Gap/limit: no observed later behavioral effect.

Route ID: [EPI-RTE-overlay-coverage](#epi-rte-overlay-coverage)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-semantic-overlay](#epi-obj-semantic-overlay)
Content/update relation: no content change
Transition or check target: overlay fingerprint match and covered/blocked slots relative to deterministic substrate.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: stale overlays receive no coverage credit in work-packet evaluation.
Epistemic authority and scope: current binding and coverage bookkeeping only.
Operational authority: remaining slots can request renewed bounded follow-up.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `src/docmason/hybrid.py`.
Claim IDs: none.
Mismatch marker: fresh is not true; covered is not verified interpretation.
Gap/limit: all retrieval-time overlay invalidation paths not audited.

Route ID: [EPI-RTE-pending-overlay](#epi-rte-pending-overlay)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-interaction-entry](#epi-obj-interaction-entry)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: stored interaction text projected as retrieval/trace units and provenance with a lower-trust source family.
Evaluator/condition and domain: see record; pending-state selection, not truth check.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: pending material is available before published promotion.
Epistemic authority and scope: interaction evidence retains a distinguishable origin; source warrant remains unknown.
Operational authority: conditional reader merge permits use; admission/ranking differs by question domain.
Behavioral-authority path: see [EPI-RTE-memory-selection](#epi-rte-memory-selection).
Evidence source ID and local anchor: SRC-1, `src/docmason/interaction.py`.
Claim IDs: none.
Mismatch marker: automatically generated supported relation status is not semantic acceptance.
Gap/limit: relation-type inference and complete correction disposition unassessed.

Route ID: [EPI-RTE-memory-selection](#epi-rte-memory-selection)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-interaction-entry](#epi-obj-interaction-entry)
Content/update relation: no content change
Transition or check target: participation and score adjustment for pending/promoted interaction records.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: excludes some interaction records and ranks others.
Epistemic authority and scope: relevance/usage policy, not validation of remembered assertions.
Operational authority: affects what later retrieval can deliver to the host.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `src/docmason/retrieval.py`.
Claim IDs: none.
Mismatch marker: remembered preference/correction may affect ranking without warranting a factual conclusion.
Gap/limit: actual host compliance and improved future capacity not observed.

Route ID: [EPI-RTE-trace-check](#epi-rte-trace-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-answer](#epi-obj-answer)
Content/update relation: no content change
Transition or check target: answer segments' lexical support, admitted evidence, source scope and render need.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: diagnostic trace feeds host repair and canonical admission.
Epistemic authority and scope: bounded support heuristic and provenance, not entailment or truth proof.
Operational authority: contributes to block/repair and limits allowed grounded labels.
Behavioral-authority path: see record and [RT-CLM-commit-gate](runtime.md#rt-clm-commit-gate).
Evidence source ID and local anchor: SRC-1, `src/docmason/retrieval.py`.
Claim IDs: [EPI-CLM-source-trust](#epi-clm-source-trust).
Mismatch marker: lexical coverage can survive a proposition-changing negation.
Gap/limit: final support contract has other checks; the concrete countercase below targets this classifier, not universal full-gate bypass.

Route ID: [RT-RTE-canonical-ask](runtime.md#rt-rte-canonical-ask)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-answer](#epi-obj-answer); [RT-OBJ-canonical-turn](runtime.md#rt-obj-canonical-turn)
Content/update relation: no content change
Transition or check target: exact governed answer eligibility for commit under declared support basis.
Evaluator/condition and domain: see [RT-CLM-commit-gate](runtime.md#rt-clm-commit-gate); local/external/mixed/model-knowledge/boundary paths differ.
Activation and timing: see route.
Possible or observed result: see route; admit, repair, block or governed boundary.
Implemented force: invoked canonical commit enforcing; whole host route protocol only.
Epistemic authority and scope: admissibility of declared support and scope, not an independent proposition-level acceptance criterion.
Operational authority: commits permitted answers and provides terminal reply permission; out-of-band host replies remain external.
Behavioral-authority path: see route.
Evidence source ID and local anchor: SRC-1, `src/docmason/admissibility.py`.
Claim IDs: [RT-CLM-commit-gate](runtime.md#rt-clm-commit-gate).
Mismatch marker: canonical legality and epistemic truth differ.
Gap/limit: model-knowledge and external manifests are legitimate counterexamples to all-answers-must-be-KB-grounded.

Route ID: [EPI-RTE-orphan-cleanup](#epi-rte-orphan-cleanup)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-interaction-entry](#epi-obj-interaction-entry)
Content/update relation: no content change
Transition or check target: promoted-memory directory lineage to extant interaction entries.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: removes orphan directory and manifest entry.
Epistemic authority and scope: withdrawal from this storage surface for missing lineage, not falsity-based retraction.
Operational authority: removed directory unavailable to subsequent promoted-context reload.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1, `src/docmason/interaction.py`.
Claim IDs: none.
Mismatch marker: survival of one interaction entry suffices to keep a grouped memory.
Gap/limit: not proof of full invalidation of already delivered context or every stale subclaim.

Route ID: [RT-RTE-operator-eval](runtime.md#rt-rte-operator-eval)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see route for replay cases/results and reference facts.
Content/update relation: no content change
Transition or check target: supplied case outcomes against deterministic expectations and supplied rubric judgments.
Evaluator/condition and domain: see route; external score aggregation is not a live model oracle.
Activation and timing: see route.
Possible or observed result: run outcomes, scorecard and baseline comparison; no supplied executed run.
Implemented force: evaluator output changes reported run status and supplies review material, not automatic production-code replacement.
Epistemic authority and scope: bounded agreement with authored expectations/rubric; answer overrides narrow generation conclusions.
Operational authority: informs explicit review, regression promotion and baseline freeze.
Behavioral-authority path: operator and subsequent evaluator, persisted run/cases/baselines, advisory then explicit admission, later evaluation horizon.
Evidence source ID and local anchor: SRC-1, `src/docmason/evaluation.py`.
Claim IDs: none.
Mismatch marker: a score is not causal evidence of process, transfer or component improvement.
Gap/limit: no treatment/comparison evidence; source references for evaluator mutation are owned by the supplied route.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-source-trust](#epi-clm-source-trust) | Strict traceability and preventing hallucinated cross-source facts | SRC-1, `README.md`, doctrine/design | Prescribed evidence inspection, uncertainty and qualification | [EPI-RTE-knowledge-check](#epi-rte-knowledge-check), [EPI-RTE-trace-check](#epi-rte-trace-check), [RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish), [RT-RTE-canonical-ask](runtime.md#rt-rte-canonical-ask) | None supplied | No causal experiment; resolvable provenance and lexical overlap do not establish entailment | File/source identity and invoked protocol checks are implemented; trustworthy semantic synthesis remains host-dependent | Factual-prevention claim exceeds checks inspected; classifier countercase below |
| [RT-CLM-commit-gate](runtime.md#rt-clm-commit-gate) | Only legal canonical closure permits ordinary final reply | see record | see record | [RT-RTE-canonical-ask](runtime.md#rt-rte-canonical-ask); [EPI-RTE-trace-check](#epi-rte-trace-check) supplies part of its input | see record | see record | Canonical admissibility has code force; host reply discipline is protocol | Not universal mediation or correctness; diverse support bases remain legal |

## Bounded conclusion

DocMason acquires source content, preserves identifiable evidence surfaces and publishes them after deterministic contract checks. Source lineage is supported; source truth and complete extraction warrant remain unknown. Publication, promotion and retrieval availability grant operational reliance, not evidence-consuming acceptance of novel claims. The generic conservative template derives a bounded statement about staged text; it does not derive the underlying business fact. Other semantic and answer transformations remain indeterminate without actual premise/output pairs.

The trace route supplies lexical-support, source-scope and render diagnostics. Its result matters: canonical admission checks inconsistent grounded labels and missing scoped support, and authored workflows prescribe one rewrite/retrace or qualification/abstention. These consumers give the diagnostics real force, but do not enlarge their epistemic domain into entailment checking. The model-authored semantic route requests evidence-grounded interpretation and explicit uncertainty; no supplied instance establishes conjecture, semantic test, acceptance or lifecycle integration after truth acceptance. This is not a negative about uninspected model processing.

Interaction statements can reach later readers through pending overlays before promotion and through published memory after promotion. Lower-trust provenance and domain/rank rules prevent equating this route with first-class external factual verification. Orphan cleanup withdraws memory for missing lineage, while overlay fingerprint/slot checks withdraw coverage credit after substrate change. Neither is content-directed falsity criticism. Already delivered host context is not shown to be retracted. Preferences and intent can also shape selection as non-truth-apt policy inputs; their operational effect needs no theory claim.

Replay evaluation retains outcomes, rubric aggregations, cases and baselines for future comparisons. It offers an improvement-directed evaluation surface, but no supplied runs establish benefit, component causality or exercised self-improvement. Explicit core replacement and adapter projection can change later instructions/code under the supplied runtime's controls; they do not show evidence-responsive autonomous self-revision. Reflection, learning, autonomy and theory-builder conditions remain independently unestablished here rather than receiving a bundled negative. Relevant uninspected paths prevent an exhaustive system-wide absence claim.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-knowledge
Label: knowledge.json source semantics

Part of: [RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish)

This object is the material content output inside the supplied route, not a duplicate route or publication pointer. Natural-language bilingual summaries, key points, claims, confidence and gaps are interpreted by the host; symbolic source/unit/artifact IDs and fingerprints are consumed by Python. Storage is staged/published source directories on the local filesystem. SRC-1, `src/docmason/knowledge.py`.

>         "key_points": key_points,
>         "entities": entities,
>         "claims": claims,
>         "known_gaps": known_gaps,
>         "ambiguities": ambiguities,
> --- `src/docmason/knowledge.py`

#### EPI-OBJ-semantic-overlay
Label: semantic_overlay sidecar

Part of: [RT-RTE-hybrid-refresh](runtime.md#rt-rte-hybrid-refresh)

A material file output of refresh, not the complete packet/settlement route. Natural-language semantic labels, annotations, relations and uncertainty have a model interpretation path; symbolic IDs, origin, fingerprints and slot names have fixed validator consumers. Stored under a source's `semantic_overlay` directory. SRC-1, `src/docmason/semantic_overlays.py`.

>     overlay_path = overlay_dir / f"{unit_id}.json"
> --- `src/docmason/semantic_overlays.py`

>         "semantic_labels": payload.get("semantic_labels", []),
>         "artifact_annotations": payload.get("artifact_annotations", []),
>         "cross_region_relations": payload.get("cross_region_relations", []),
>         "uncertainty_notes": payload.get("uncertainty_notes", []),
> --- `src/docmason/semantic_overlays.py`

#### EPI-OBJ-answer
Label: Canonical answer text

Distinct from [RT-OBJ-canonical-turn](runtime.md#rt-obj-canonical-turn): the answer Markdown is a separate natural-language artifact linked by the control binding's `answer_file_path`, not content contained in that symbolic record. The wrapper resolves the stored path and writes host-supplied text to the separate file. This linkage governs answer ownership and exact-file tracing without making the answer propositions part of the control record. The answer is persisted under runtime answers and consumed by the user/host and by symbolic trace segmentation. No supplied answer instance. SRC-1, `src/docmason/host_integration.py`, implementation; `skills/canonical/grounded-answer/SKILL.md`, doctrine/design.

>         canonical_answer_path = _resolved_answer_path(
>             paths, _nonempty_string(turn.get("answer_file_path"))
>         )
>         if canonical_answer_path is None:
>             raise ValueError("missing-canonical-answer-path")
>         _write_exact_answer_text(canonical_answer_path, exact_answer_text)
> --- `src/docmason/host_integration.py`

> 7. Draft the canonical answer file under `runtime/answers/` when conversation context exists.
> --- `skills/canonical/grounded-answer/SKILL.md`

#### EPI-OBJ-interaction-entry
Label: Interaction entry and projected turn-text

Distinct from [RT-OBJ-canonical-turn](runtime.md#rt-obj-canonical-turn): this is conversation-derived evidence made available for memory/retrieval, not the turn's closure control binding. Natural-language interaction text and symbolic trust/memory/usage metadata persist in runtime entries and projected overlay/KB artifacts. Actual generation/claim lineage is not supplied. SRC-1, `src/docmason/interaction.py`.

>         "source_family": "interaction-pending",
>         "trust_tier": "interaction",
>         "pending_promotion": True,
>         "unit_id": "turn-text",
> --- `src/docmason/interaction.py`

### Routes

#### EPI-RTE-conservative-output
Label: Conservative staged semantics

Part of: [RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish)

This is its deterministic content-production part, separate from checking/publication. Python reads staged manifests and selected unit/artifact/overlay snippets and writes knowledge/summary files. Normal sync selects pending semantic work; host enrichment is an alternate producer, not attributed to this function. Software proposes these outputs; normal validation/publication may reject. User initiation is not per-claim approval. Open corpus maintenance; no business-answer oracle. Recovery is ordinary restaging/rebuild, not proved semantic rollback. What persists is candidate semantics under guidance to preserve evidence and explicit gaps. SRC-1, `src/docmason/knowledge.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Minimal publishable knowledge/summary output and function result.
- Later read-back: Published semantics can reach later retrieval and host interpretation through normal sync publication.
- Delegated visibility: inapplicable — this deterministic function performs no model delegation; host authoring belongs to refresh.
- Selection predicate: Staged manifests and selected snippets; the concrete deduction concerns the generic document branch without richer overlay/artifact snippets.
- Invalidation or expiry: Source fingerprints bind output; restaging/semantic refresh can replace it; all cache branches unassessed.
- Activation or effect: Writes candidate semantics; later content effect requires publication and reader consumption, not observed here.
- Evidence limits: Code establishes construction, not real-corpus correctness or beneficial use.

Concrete code deduction, without execution: assume the generic branch receives title `Plan`, an English source, one unit snippet with excerpt `Revenue rose`, and no overlay/artifact snippet. `snippet_seed` becomes `snippets`; `topic_summary` becomes `Revenue rose`; the stored summary is `This source covers: Revenue rose`; `evidence_claim` becomes `The staged evidence for `Plan` explicitly includes: Revenue rose` (the title carries backticks in the actual string). This latter proposition is entailed by the stipulated staged input. It does not license `Revenue rose` as a true statement about the world. The excerpt copies in key points are non-ampliative reshaping. Richer snippets, truncation and source-language labeling require separate scope qualifications.

>         topic_summary = (
>             "; ".join(snippet["excerpt"] for snippet in snippet_seed[:2])
>             if snippet_seed
> --- `src/docmason/knowledge.py`

>         summary_en = f"This source covers: {topic_summary}"
> --- `src/docmason/knowledge.py`

>         evidence_claim = (
>             f"The staged evidence for `{title}` explicitly includes: "
>             f"{snippet_seed[0]['excerpt']}"
> --- `src/docmason/knowledge.py`

#### EPI-RTE-knowledge-check
Label: Staged knowledge contract validation

Part of: [RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish)

Distinct checking part, not the driver's publication decision. Python inspects source identity/fingerprint, required fields, placeholders, real citation IDs/nonempty support, related sources and asset presence. Semantic-overlay validation checks kinds, ID membership, required fields and slot declarations. Host/code proposes content; these checks can veto normal publication via validation errors. Maintenance mode; the oracle is the declared artifact contract, not an expected business answer. Recovery follows corrected artifacts and rerun; nothing here establishes semantic truth rollback. SRC-1, `src/docmason/knowledge.py`, `src/docmason/semantic_overlays.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Source errors/warnings feeding validation report and reader/index construction.
- Later read-back: Validation-derived indexes are consumed by later readers after publication; no truth acceptance is inferred from their persistence.
- Delegated visibility: inapplicable — deterministic validator receives files, not delegated reasoning windows.
- Selection predicate: Selected staging/current target and its source/interaction artifacts.
- Invalidation or expiry: Revalidation against changed artifacts can replace findings; old delivered evidence is not revoked by this check alone.
- Activation or effect: Normal sync consumes report status to permit/block publication; see supplied publication route.
- Evidence limits: Only bounded validator passages inspected; nonempty citation support need not entail the cited claim.

>             if knowledge.get("source_fingerprint") != source_manifest.get("source_fingerprint"):
>                 source_errors.append(
>                     "knowledge.json source_fingerprint does not match source_manifest.json"
>                 )
> --- `src/docmason/knowledge.py`

>                 if not sanitize_text(citation.get("support")):
>                     source_errors.append("Each citation must include a non-empty support field")
> --- `src/docmason/knowledge.py`

>     if unit_id not in unit_ids:
>         errors.append(f"semantic overlay references unknown unit_id `{unit_id}`")
> --- `src/docmason/semantic_overlays.py`

#### EPI-RTE-overlay-coverage
Label: Overlay freshness and slot coverage

Part of: [RT-RTE-hybrid-refresh](runtime.md#rt-rte-hybrid-refresh)

Python compares overlay source/unit fingerprints against the substrate, derives covered/blocked/remaining slots and returns coverage state to source hybrid-packet construction. Host-authored metadata supplies claimed coverage; code rejects stale coverage credit. Maintenance/ask repair; oracle is equality/slot coverage, not source truth. Recovery is candidate-prepared follow-up, with uncertainty notes retained for fresh blocked work. SRC-1, `src/docmason/hybrid.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Freshness and slot lists, coverage_status and blocked reasons.
- Later read-back: Later packet builds reevaluate persisted overlay files against then-current fingerprints.
- Delegated visibility: Bounded hybrid packets expose remaining work; actual host receipt and interpretation unobserved.
- Selection predicate: Candidate required slots and supplied overlay payload, source and unit fingerprints.
- Invalidation or expiry: Fingerprint mismatch empties coverage/blocked credit and restores required slots.
- Activation or effect: Coverage result feeds packet candidate state and follow-up need; source wiring, not exercised repair.
- Evidence limits: Matching hashes establish lineage binding, not correct visual interpretation; global retrieval suppression unassessed.

>         payload.get("source_fingerprint") == source_fingerprint
>         and payload.get("unit_evidence_fingerprint") == unit_evidence_fingerprint
> --- `src/docmason/hybrid.py`

>     if not fresh:
>         coverage_status = "candidate-prepared"
>         blocked_reasons = []
>         covered_slots = []
>         blocked_slots = []
>         remaining_slots = required_slots
> --- `src/docmason/hybrid.py`

#### EPI-RTE-pending-overlay
Label: Pending interaction evidence projection

Distinct from [RT-RTE-evidence-tools](runtime.md#rt-rte-evidence-tools): this writes the evidence surface that the reader may merge. It overlaps the interaction marking edge of [RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish), but exists before publication, so is not wholly part of either route. Python selects pending entries, projects text/attachments, writes records/provenance/graph/queue files under an interaction-overlay lease. No factual evaluator intervenes in these inspected projection steps. SRC-1, `src/docmason/interaction.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Rebuilt overlay files and summary of pending evidence.
- Later read-back: Subsequent readers can load these runtime overlay artifacts under the supplied reader's merge predicate; publication marking rebuilds overlay without promoted entries.
- Delegated visibility: Selected overlay evidence can be delivered to the host through retrieve/trace; no isolation guarantee.
- Selection predicate: pending_interaction_entries; text/attachment fields and related_source_ids become projected evidence.
- Invalidation or expiry: Overlay is rebuilt from current pending entries; promotion removes pending status, not factual uncertainty.
- Activation or effect: Creates conditional evidence availability before publication; actual host reliance unobserved.
- Evidence limits: Projection preserves origin labels but gives no new truth warrant; capture and inference internals incompletely inspected.

For a concrete projection, an entry with searchable_text `The deadline is Friday` supplies exactly that string as the `turn-text` unit text/searchable_text. This is non-ampliative reshaping into an interaction-labeled record, not verification of the deadline. The automatically assigned relation status below is bookkeeping from entry associations, not evidence-consuming semantic acceptance.

>         "text": entry.get("searchable_text", ""),
> --- `src/docmason/interaction.py`

>                     "relation_type": relation_type,
>                     "strength": "medium",
>                     "status": "supported",
>                     "citation_unit_ids": ["turn-text"],
> --- `src/docmason/interaction.py`

>         write_json(paths.interaction_overlay_source_records_path, {"records": source_records})
>         write_json(paths.interaction_overlay_unit_records_path, {"records": unit_records})
> --- `src/docmason/interaction.py`

#### EPI-RTE-memory-selection
Label: Interaction memory participation and rank

Part of: [RT-RTE-evidence-tools](runtime.md#rt-rte-evidence-tools)

This is the reader's interaction-specific selection part, not a duplicate reader or memory write. Python receives source-family, usage policy, memory kind/rank prior, memory-profile mode and lexical scores. It can exclude or adjust participation. Code decides under fixed thresholds; generic caller identity supplies no per-content human approval. Open retrieval domain; no expected-answer oracle. Source content stays unchanged. SRC-1, `src/docmason/retrieval.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Boolean participation plus numerical ranking adjustment.
- Later read-back: Later retrieval can apply the same rules to retained pending/promoted evidence with a new question/profile.
- Delegated visibility: Only participating/ranked material can reach the reader output; downstream host use remains external.
- Selection predicate: External-factual excludes interaction families; workspace-corpus minimal mode excludes them; other modes use lexical thresholds, relevant kinds and rank prior.
- Invalidation or expiry: Question/profile changes can change participation without deleting the stored entry.
- Activation or effect: Selector changes evidence inclusion/rank, not the truth of remembered assertions; no observed answer influence.
- Evidence limits: Ranking and usage policy are not hard semantic guarantees across all reader/trace paths.

>     if question_domain == "external-factual":
>         return False, 0.0
>     if question_domain == "workspace-corpus" and mode == "minimal":
>         return False, 0.0
> --- `src/docmason/retrieval.py`

>     bonus = MEMORY_RANK_PRIOR_BONUS.get(retrieval_rank_prior, 0.0)
>     if mode == "strong":
>         bonus += 0.4
>         if relevant_kinds and memory_kind in relevant_kinds:
>             bonus += 0.6
> --- `src/docmason/retrieval.py`

#### EPI-RTE-trace-check
Label: Answer-segment grounding heuristic

Part of: [RT-RTE-evidence-tools](runtime.md#rt-rte-evidence-tools)

Python segments the answer, evaluates retrieved/admitted supports and produces segment diagnostics and aggregate answer state. This is the check part, separate from commit disposition. Target is answer-to-evidence support in the retrieved domain, not world truth. Evaluator uses score/lexical/unit thresholds, significant vocabulary coverage, source scope and render-needs. Host proposes the answer; trace can downgrade support and commit checks can reject inconsistent declarations. Open questions; no independent expected answer. Authored workflow asks qualification/abstention on contradiction and permits bounded rewrite/retrace. Persisted trace is evidence about this heuristic, not a semantic proof. SRC-1, `src/docmason/retrieval.py`, `src/docmason/admissibility.py`, `skills/canonical/grounded-answer/SKILL.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Segment grounding_status, coverage ratios/reasons, scope/render diagnostics and support IDs.
- Later read-back: Persisted traces can be selected by canonical closure or later session tracing under the supplied reader route.
- Delegated visibility: Compact diagnostics/support IDs are delivered; full nested payloads are prescribed file-first; actual host inspection unobserved.
- Selection predicate: Exact answer segments, admitted supports and selected source scope; support-set aggregation only upgrades unresolved to partial.
- Invalidation or expiry: Exact answer/version binding matters at commit; stale scope/support can block or require fresh trace; host context is not erased.
- Activation or effect: Canonical gate checks trace-state/scope mismatch; authored repair/qualification consumes diagnostics; host action unobserved.
- Evidence limits: Classifier measures vocabulary/support affinity, not entailment, negation consistency or causal truth.

Concrete countercase to a truth-oracle reading: take segment `Revenue rose in 2025`, matching terms `{revenue, rose, 2025}`, total score 6 and lexical sum 3. Significant terms are the three matched words (`in` is removed), coverage is 1, so the top-result classifier returns grounded. Change the segment to `Revenue never rose in 2025`, leaving the support/result unchanged. `never` is not a grounding stopword; coverage becomes 3/4, exactly the 0.75 threshold, so this conflicting proposition also receives grounded from that classifier. The threshold's license is lexical support only. No claim is made that these artificial result values arise in a supplied actual run or pass every other canonical support check.

>     covered_terms = significant_terms & matched_terms
>     return len(covered_terms) / len(significant_terms)
> --- `src/docmason/retrieval.py:3756-3767`

>     if total >= 6.0 and (lexical >= 3.0 or matched_units > 0) and coverage >= 0.75:
>         return "grounded"
> --- `src/docmason/retrieval.py`

>         grounding_status = groundedness_from_support_set(
>             admitted_results[:top],
>             segment_text=segment,
>             top_result_status=top_result_grounding_status,
>         )
> --- `src/docmason/retrieval.py`

>         issues.append(
>             "Top-level answer_state is grounded even though the canonical trace still "
>             "contains unresolved segments."
>         )
> --- `src/docmason/admissibility.py`

> - If the evidence is contradictory, ambiguous, or insufficient, qualify the answer or abstain.
> --- `skills/canonical/grounded-answer/SKILL.md`

#### EPI-RTE-orphan-cleanup
Label: Orphan promoted-memory removal

Distinct from the promotion edge of [RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish): maintenance removes directories for missing lineage rather than admitting a publication. Python checks promoted memory manifests against entry-file existence, deletes orphan directories and writes a kept-memory manifest. Proposer/decision/veto is deterministic maintenance; no human factual review or expected business-answer oracle. Recovery by rebuilding valid retained inputs is possible in the broader build surface, but deleted orphan content restoration is not established here. SRC-1, `src/docmason/interaction.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Removed IDs/count, target and refreshed interaction manifest.
- Later read-back: Subsequent promoted-context reload enumerates directories; deleted directories are not available there.
- Delegated visibility: inapplicable — filesystem maintenance performs no delegated model reasoning.
- Selection predicate: Promoted directories for selected target with no referenced interaction entry file still existing.
- Invalidation or expiry: Missing all origin entries withdraws directory; at least one surviving entry preserves it.
- Activation or effect: Deletes storage and reduces later loader availability; not semantic retraction or erasure of prior host context.
- Evidence limits: No live cleanup supplied; incomplete group origins can remain while one entry survives.

>         if not any(
>             _interaction_entry_path(paths, interaction_id).exists()
>             for interaction_id in interaction_ids
>         ):
>             import shutil
>
>             shutil.rmtree(memory_dir)
> --- `src/docmason/interaction.py`

>     for memory_dir in iter_promoted_interaction_dirs(paths, target=target):
> --- `src/docmason/interaction.py`

### Claims

#### EPI-CLM-source-trust
Label: Strict traceability and source-trust claims

No counterpart after comparison with [RT-CLM-commit-gate](runtime.md#rt-clm-commit-gate): that supplied claim governs canonical legality, while this README claim promises traceability and prevention of hallucinated cross-source facts. SRC-1, `README.md`, doctrine/design. The inspected mechanisms support lineage and scoped protocol controls, not the stronger universal factual claim.

> **DocMason** is built on a different thesis: **answers must be strictly traceable.**
> --- `README.md`

> * **Strict Source Identity.** DocMason enforces strict document boundaries. It prevents agents from hallucinating cross-source facts that only vaguely fit together.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

Additional load-bearing evaluator evidence for [RT-RTE-operator-eval](runtime.md#rt-rte-operator-eval), SRC-1, `src/docmason/evaluation.py`, implementation: rubric trials are supplied, dimension medians are aggregated, outcomes and baselines are persisted. Score disagreement recommends review rather than authenticating a factual mechanism. The closest supplied route owns this referent; no duplicate is declared.

>         dimension_scores[dimension] = int(statistics.median(values))
> --- `src/docmason/evaluation.py`

>     review_recommended = any(spread > 1 for spread in dimension_spread.values())
> --- `src/docmason/evaluation.py`

>         deterministic_passed = all(check["passed"] for check in checks)
> --- `src/docmason/evaluation.py`

>     write_json(run_json_path, run_payload)
>     scorecard_path.write_text(_render_scorecard_markdown(run_payload), encoding="utf-8")
> --- `src/docmason/evaluation.py`
