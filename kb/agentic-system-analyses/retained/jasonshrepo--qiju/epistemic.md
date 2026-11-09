---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Qiju epistemic routes: session-record admission, privileged historical reliance, action rollup and retrospective recommendations."
run-id: AAS-2026-11-08-qiju-1a12c31c13d1-01
reviewed-boundary: a5ea9db29262ce7ec514cdc1dc5c5d017a6a3f89
---

# Qiju epistemic report

## Source-and-claim boundary

The question is what licenses reliance on Qiju's session history and on recommendations drawn from it. The scope and exclusions are those of [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are in its [Source register](boundary.md#source-register). All source anchors below resolve to SRC-1 at the frozen revision. This is source inspection, not target execution.

Qiju includes the shipped host instructions, not just JSON storage. External host cognition, provider weights, file-tool permission enforcement and actual host discovery remain outside inspection. No session store, execution trace, accepted review report or experiment was supplied. Those gaps prevent conclusions about factual record accuracy, exercised acceptance, actual instruction compliance, learning benefit or causal self-improvement. They do not prevent assessing executable admission and selection. The distributed-parametric dependency remains as in [RT-CMP-host-model](runtime.md#rt-cmp-host-model); no weight-update inference follows.

The consequential claims are [EPI-CLM-verified-history](#epi-clm-verified-history), [EPI-CLM-review-improvement](#epi-clm-review-improvement), and [RT-CLM-lossless-records](runtime.md#rt-clm-lossless-records). The first is stronger than retrievability: installed guidance asks the host to privilege history as verified. The log prompt's artifact anchors and decision-status discipline are a relevant countercase to a claim of wholly unconstrained generation; they are not an implemented factual check.

| Entry point or operation | SRC-1 source path | Coverage and record |
| --- | --- | --- |
| CLI dispatch; log and temp-entry | `src/qiju/cli.py`, `src/qiju/capture.py`, `src/qiju/schema.py` | Direct reads of parser/dispatch, capture and full schema; [RT-RTE-record-capture](runtime.md#rt-rte-record-capture), [EPI-RTE-shape-check](#epi-rte-shape-check), [EPI-RTE-shape-admission](#epi-rte-shape-admission). Staging guards supplied through runtime. |
| Search/show; actions, summaries and field projections | `src/qiju/search.py`, `src/qiju/cli.py` | Direct full search and renderer reads; [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval), [EPI-RTE-action-rollup](#epi-rte-action-rollup). Tier merge supplied through runtime, not independently re-audited. |
| Log/search/review host operations | `src/qiju/init_cmd.py` | Direct complete instruction bodies; [RT-OBJ-qiju-skills](runtime.md#rt-obj-qiju-skills), [RT-RTE-skill-review](runtime.md#rt-rte-skill-review), [RT-BAP-host-guidance](runtime.md#rt-bap-host-guidance). No registered host execution tools or hooks in inspected CLI parser; external host operations are instructions, not Qiju orchestration. |
| Init/update installation | `src/qiju/init_cmd.py`, `src/qiju/update_cmd.py` | Supplied [RT-RTE-skill-install](runtime.md#rt-rte-skill-install); direct prompt reads. Package replacement is not a review-result consumer. |
| Maintain, archive checks, staging cleanup | `src/qiju/maintain.py`, `src/qiju/archive.py`, `src/qiju/staging.py` | Supplied [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance), [RT-RTE-record-capture](runtime.md#rt-rte-record-capture); row/ID and deletion guards have operational force but no factual license. |
| Redact | `src/qiju/retro_redact.py`, `src/qiju/redact.py` | Supplied [RT-RTE-privacy-repair](runtime.md#rt-rte-privacy-repair); direct CLI gate read. Exact replacement, not factual correction. |
| Migrate: normalization, retag and legacy import | `src/qiju/migrate.py`, `src/qiju/cli.py` | Supplied [RT-RTE-store-migration](runtime.md#rt-rte-store-migration); direct rebrand helpers and CLI mode selection. Concrete semantic countercase below. Other helper internals remain supplied findings, not direct independent audit. |
| Uninstall; purge-data | `src/qiju/cli.py`, `src/qiju/cleanup.py` | Direct purge/confirmation reads plus supplied [RT-CLM-lossless-records](runtime.md#rt-clm-lossless-records); [EPI-RTE-store-withdrawal](#epi-rte-store-withdrawal). Default integration removal differs from data withdrawal. |
| Projects | `src/qiju/cli.py` | Direct dispatch: lists storage project names; no factual evaluator or content-revision role. |
| Public/design warrant | `README.md`, `docs/architecture.md` | Direct English claims and full architecture; [EPI-CLM-verified-history](#epi-clm-verified-history), [EPI-CLM-review-improvement](#epi-clm-review-improvement), [RT-CLM-lossless-records](runtime.md#rt-clm-lossless-records). |
| Other included documentation | `README.zh.md`, `docs/overview.md`, `docs/overview.zh.md`, `docs/cli-reference.md`, `docs/redaction-and-privacy.md` | Not independently read for complete claim enumeration; runtime supplies some privacy findings. Prevents a complete multilingual public-claim inventory, not the scoped route findings. |
| External host and actual retained instances | `docs/host-integration.md` | Boundary/runtime findings only; no supplied operational evidence. Prevents attributing host compliance or outcome success. |

No system-complete negative about every possible warrant claim is asserted. The inspected dispatch surface and supplied runtime cover the material shipped CLI operations; private host reasoning is not an additional inspected evaluator.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-body-md](#epi-obj-body-md) | Claims about actions, decisions, reasons, rejected alternatives and artifact lineage | see record | SRC-1 `src/qiju/init_cmd.py` | No actual authored instance; source warrant of model-composed claims unknown. Artifact pointers are not inspected evidence at admission. |
| [EPI-OBJ-next-steps](#epi-obj-next-steps) | Imperatives themselves are policy, not truth-apt; classifying them as agreed and still open implies historical/current-state claims | see record | SRC-1 `src/qiju/search.py` | Rollup does not resolve completion, rejection or later supersession. |
| [EPI-OBJ-record-metadata](#epi-obj-record-metadata) | Timestamp, project, model/source/agent labels; title may assert history | see record | SRC-1 `src/qiju/capture.py`, `src/qiju/schema.py` | Parseability and caller labels do not authenticate historical origin. |
| [RT-OBJ-qiju-skills](runtime.md#rt-obj-qiju-skills) | Mixed operating policy and the assertion that records are verified | see record | SRC-1 `src/qiju/init_cmd.py` | Installed bytes versus actual host loading/compliance separated. |
| [RT-RTE-skill-review](runtime.md#rt-rte-skill-review) | Potential diagnoses and lessons about what caused mistakes; proposed imperative wording is policy | see record | SRC-1 `src/qiju/init_cmd.py` | Route citation stands for requested outputs, not an observed candidate artifact. No actual review content individuated. |
| [RT-CMP-host-model](runtime.md#rt-cmp-host-model) | Not determinable inside opaque parameters | see record | SRC-1 `docs/host-integration.md` | Provider state and model changes uninspected. |

## Authority-route ledger

The compact records below are an overlay. Fields owned by shared records say “see”; a repeated record citation can cover distinct functions without redeclaring its referent. “Doctrine only” describes requested host conduct, even where installation of that request is implemented.

Route ID: [RT-RTE-record-capture](runtime.md#rt-rte-record-capture)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-body-md](#epi-obj-body-md), [EPI-OBJ-next-steps](#epi-obj-next-steps).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: session context to narrative/decision history.
Evaluator/condition and domain: see [RT-RTE-record-capture](runtime.md#rt-rte-record-capture); no observed content with which to distinguish faithful import/reshaping from inference or conjecture.
Activation and timing; possible or observed result: see [RT-RTE-record-capture](runtime.md#rt-rte-record-capture).
Implemented force; epistemic authority and scope: request for anchored, status-preserving composition, not evidence-consuming factual acceptance.
Operational authority; behavioral-authority path: see [RT-BAP-host-guidance](runtime.md#rt-bap-host-guidance).
Evidence source ID and local anchor: SRC-1 `src/qiju/init_cmd.py`; see [RT-RTE-record-capture](runtime.md#rt-rte-record-capture).
Claim IDs: [EPI-CLM-verified-history](#epi-clm-verified-history).
Mismatch marker: verified-before-factual-check.
Gap/limit: no produced proposition or checked premise chain supplied; non-entailment is not established merely by model authorship.

Route ID: [EPI-RTE-shape-check](#epi-rte-shape-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-record-metadata](#epi-obj-record-metadata), [EPI-OBJ-body-md](#epi-obj-body-md).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force: see [EPI-RTE-shape-check](#epi-rte-shape-check).
Epistemic authority and scope: syntactic validity only, not historical truth.
Operational authority; behavioral-authority path: check result feeds [EPI-RTE-shape-admission](#epi-rte-shape-admission) synchronously, enforcing.
Evidence source ID and local anchor: SRC-1 `src/qiju/schema.py`.
Claim IDs: [EPI-CLM-verified-history](#epi-clm-verified-history).
Mismatch marker: schema-valid is not fact-verified.
Gap/limit: direct input can satisfy all checks with arbitrary unsupported narrative.

Route ID: [EPI-RTE-shape-admission](#epi-rte-shape-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-body-md](#epi-obj-body-md), [EPI-OBJ-record-metadata](#epi-obj-record-metadata).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; operational authority; behavioral-authority path: see [EPI-RTE-shape-admission](#epi-rte-shape-admission).
Epistemic authority and scope: operational admission to storage, not factual acceptance against evidence for later historical use.
Evidence source ID and local anchor: SRC-1 `src/qiju/capture.py`.
Claim IDs: [EPI-CLM-verified-history](#epi-clm-verified-history).
Mismatch marker: admission does not warrant source-of-truth status.
Gap/limit: successful return may name an already stored ID, not establish equality with newly submitted payload.

Route ID: [RT-RTE-record-capture](runtime.md#rt-rte-record-capture)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-body-md](#epi-obj-body-md), [EPI-OBJ-next-steps](#epi-obj-next-steps), [EPI-OBJ-record-metadata](#epi-obj-record-metadata).
Content/update relation: truth-apt transformation: acquisition/import.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; operational authority; behavioral-authority path: see [RT-RTE-record-capture](runtime.md#rt-rte-record-capture).
Epistemic authority and scope: source warrant unknown; redaction and timestamp coercion can alter what is retained. Storage grants availability, not endorsement.
Evidence source ID and local anchor: SRC-1 `src/qiju/capture.py`; see [RT-RTE-record-capture](runtime.md#rt-rte-record-capture).
Claim IDs: [RT-CLM-lossless-records](runtime.md#rt-clm-lossless-records), [EPI-CLM-verified-history](#epi-clm-verified-history).
Mismatch marker: persistence is not acceptance.
Gap/limit: retained generated content is acquired by CLI; it is not thereby an accepted ampliative product.

Route ID: [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-body-md](#epi-obj-body-md), [EPI-OBJ-next-steps](#epi-obj-next-steps), [EPI-OBJ-record-metadata](#epi-obj-record-metadata).
Content/update relation: truth-apt transformation: non-ampliative reshaping.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; operational authority; behavioral-authority path: see [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval).
Epistemic authority and scope: matching supplied predicates/exact ID, not relevance or truth. Host's privileged reliance is separately requested by [RT-BAP-host-guidance](runtime.md#rt-bap-host-guidance).
Evidence source ID and local anchor: SRC-1 `src/qiju/search.py`, `src/qiju/cli.py`.
Claim IDs: [EPI-CLM-verified-history](#epi-clm-verified-history).
Mismatch marker: delivery is not verification.
Gap/limit: projected/limited outputs can omit relevant body/status; hydrating an ID preserves retrieved text, not source warrant.

Route ID: [EPI-RTE-action-rollup](#epi-rte-action-rollup)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-next-steps](#epi-obj-next-steps).
Content/update relation: non-truth-apt policy/content update: trim, deduplicate and render retained task strings as unchecked action items.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; operational authority; behavioral-authority path: see [EPI-RTE-action-rollup](#epi-rte-action-rollup).
Epistemic authority and scope: supports membership in selected records' next_steps, not the proposition “still open now.”
Evidence source ID and local anchor: SRC-1 `src/qiju/search.py`, `src/qiju/cli.py`.
Claim IDs: [EPI-CLM-verified-history](#epi-clm-verified-history).
Mismatch marker: open-status inference exceeds string deduplication.
Gap/limit: later body text reporting completion does not suppress an older next_steps item.

Route ID: [RT-RTE-skill-review](runtime.md#rt-rte-skill-review)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: see [RT-RTE-skill-review](runtime.md#rt-rte-skill-review).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; operational authority; behavioral-authority path: see [RT-RTE-skill-review](runtime.md#rt-rte-skill-review).
Epistemic authority and scope: Requested record-based diagnosis with recurrence, impact and alternative-cause cautions; no measured correctness criterion or external answer oracle.
Evidence source ID and local anchor: SRC-1 `src/qiju/init_cmd.py`; see [RT-RTE-skill-review](runtime.md#rt-rte-skill-review).
Claim IDs: [EPI-CLM-review-improvement](#epi-clm-review-improvement).
Mismatch marker: requested review is not demonstrated improvement.
Gap/limit: no actual review, accepted diagnosis, applied guidance or later dependent behavior supplied.

Route ID: [RT-RTE-skill-review](runtime.md#rt-rte-skill-review)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: see [RT-RTE-skill-review](runtime.md#rt-rte-skill-review).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; operational authority; behavioral-authority path: see [RT-RTE-skill-review](runtime.md#rt-rte-skill-review).
Epistemic authority and scope: Actual diagnoses might import/reshape history or conjecture causes; no candidate content supplied establishes entailment or non-entailment. Proposed imperative guidance is a separate non-truth-apt policy update.
Evidence source ID and local anchor: SRC-1 `src/qiju/init_cmd.py`; see [RT-RTE-skill-review](runtime.md#rt-rte-skill-review).
Claim IDs: [EPI-CLM-review-improvement](#epi-clm-review-improvement).
Mismatch marker: requested review is not demonstrated improvement.
Gap/limit: no actual review, accepted diagnosis, applied guidance or later dependent behavior supplied.

Route ID: [RT-RTE-skill-review](runtime.md#rt-rte-skill-review)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: see [RT-RTE-skill-review](runtime.md#rt-rte-skill-review).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; operational authority; behavioral-authority path: see [RT-RTE-skill-review](runtime.md#rt-rte-skill-review).
Epistemic authority and scope: User authorization is requested for applying targeted edits; it is not an evidence-consuming acceptance decision establishing the truth of a diagnosis.
Evidence source ID and local anchor: SRC-1 `src/qiju/init_cmd.py`; see [RT-RTE-skill-review](runtime.md#rt-rte-skill-review).
Claim IDs: [EPI-CLM-review-improvement](#epi-clm-review-improvement).
Mismatch marker: requested review is not demonstrated improvement.
Gap/limit: no actual review, accepted diagnosis, applied guidance or later dependent behavior supplied.

Route ID: [RT-RTE-privacy-repair](runtime.md#rt-rte-privacy-repair)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: retained record fields; see [RT-RTE-privacy-repair](runtime.md#rt-rte-privacy-repair).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; operational authority; behavioral-authority path: see [RT-RTE-privacy-repair](runtime.md#rt-rte-privacy-repair).
Epistemic authority and scope: caller-chosen literal removal, not correction against facts; semantic preservation depends on actual replaced strings.
Evidence source ID and local anchor: SRC-1 `src/qiju/retro_redact.py`; see [RT-RTE-privacy-repair](runtime.md#rt-rte-privacy-repair).
Claim IDs: [RT-CLM-lossless-records](runtime.md#rt-clm-lossless-records).
Mismatch marker: none.
Gap/limit: source-derived factual claims may lose evidence-bearing detail; variants and external copies are not universally withdrawn.

Route ID: [RT-RTE-store-migration](runtime.md#rt-rte-store-migration)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: imported/retagged records; see [RT-RTE-store-migration](runtime.md#rt-rte-store-migration).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; operational authority; behavioral-authority path: see [RT-RTE-store-migration](runtime.md#rt-rte-store-migration).
Epistemic authority and scope: no source-truth license from renaming; imported warrant unknown and content fidelity can degrade. Identity preflight differs from factual review.
Evidence source ID and local anchor: SRC-1 `src/qiju/migrate.py`.
Claim IDs: [RT-CLM-lossless-records](runtime.md#rt-clm-lossless-records).
Mismatch marker: global rebranding is not guaranteed semantic preservation.
Gap/limit: concrete implementation deduction: body_md “We migrated from Kedu to Qiju.” becomes “We migrated from Qiju to Qiju.” _rebrand_value visits every string and _rebrand_text substitutes Kedu. The historical distinction is erased; no execution is claimed. Quote retained below.

Route ID: [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: archived record batch; see [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; operational authority; behavioral-authority path: see [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance).
Epistemic authority and scope: Parquet row-count/ID-set agreement licenses archive replacement in that structural domain, not field equality or narrative truth.
Evidence source ID and local anchor: SRC-1 `src/qiju/archive.py`; see [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance).
Claim IDs: [RT-CLM-lossless-records](runtime.md#rt-clm-lossless-records).
Mismatch marker: structural roundtrip check has narrower scope than full losslessness.
Gap/limit: no executed failure recovery or content-equivalence experiment supplied.

Route ID: [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance)
Route function: retention
Architectural status: implemented
Object/candidate ID: record tiers/staging; see [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance).
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; operational authority; behavioral-authority path: see [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance).
Epistemic authority and scope: age/size placement, not acceptance, freshness of claims or rejection of false history.
Evidence source ID and local anchor: SRC-1 `src/qiju/maintain.py`; see [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance).
Claim IDs: [RT-CLM-lossless-records](runtime.md#rt-clm-lossless-records).
Mismatch marker: none.
Gap/limit: temporal eligibility does not judge whether later behavior should rely on the record.

Route ID: [RT-RTE-skill-install](runtime.md#rt-rte-skill-install)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-qiju-skills](runtime.md#rt-obj-qiju-skills).
Content/update relation: non-truth-apt policy/content update: replace installed skills with package bodies.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; operational authority; behavioral-authority path: see [RT-RTE-skill-install](runtime.md#rt-rte-skill-install), [RT-BAP-host-guidance](runtime.md#rt-bap-host-guidance).
Epistemic authority and scope: package selection and byte equality, not evidence-based validation of proposed lessons.
Evidence source ID and local anchor: SRC-1 `src/qiju/init_cmd.py`, `src/qiju/update_cmd.py`; see [RT-RTE-skill-install](runtime.md#rt-rte-skill-install).
Claim IDs: [EPI-CLM-review-improvement](#epi-clm-review-improvement).
Mismatch marker: direct update is not a retrospective-result admission gate.
Gap/limit: installation is implemented; later host dependence and benefit unobserved.

Route ID: [EPI-RTE-store-withdrawal](#epi-rte-store-withdrawal)
Route function: retention
Architectural status: implemented
Object/candidate ID: durable long/archive records.
Content/update relation: no content change.
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; operational authority; behavioral-authority path: see [EPI-RTE-store-withdrawal](#epi-rte-store-withdrawal).
Epistemic authority and scope: administrative withdrawal of availability, not retraction of particular false claims.
Evidence source ID and local anchor: SRC-1 `src/qiju/cleanup.py`, `src/qiju/cli.py`.
Claim IDs: [RT-CLM-lossless-records](runtime.md#rt-clm-lossless-records).
Mismatch marker: deletion is narrower than all historical copies.
Gap/limit: project short records and external host context can still contain content.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-verified-history](#epi-clm-verified-history) | see record | SRC-1 `src/qiju/init_cmd.py`, `README.md`; doctrine/design | Anchors, explicit statuses, authoritative metadata only; artifacts outrank paraphrases | [RT-RTE-record-capture](runtime.md#rt-rte-record-capture), [EPI-RTE-shape-check](#epi-rte-shape-check), [EPI-RTE-shape-admission](#epi-rte-shape-admission), [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval), [EPI-RTE-action-rollup](#epi-rte-action-rollup) | None supplied | No factual oracle or comparison; schema cannot check whether a decision occurred | Retrieved records are accessible history claims with unknown source warrant | “Verified” and source-of-truth priority exceed implemented check domain; “verifiable” can mean pointer-enabled checking, not completed verification |
| [EPI-CLM-review-improvement](#epi-clm-review-improvement) | see record | SRC-1 `README.md`, `src/qiju/init_cmd.py`; doctrine/design | Pattern/evidence-first retrospective and optional targeted edits | [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval), [RT-RTE-skill-install](runtime.md#rt-rte-skill-install); review procedure [RT-RTE-skill-review](runtime.md#rt-rte-skill-review) is requested | None supplied | No interventions, control group or applied-change trace; method text is not an evaluator execution | An improvement-proposal procedure is supplied | Correct causal diagnoses, successful updates and repeated use unestablished |
| [RT-CLM-lossless-records](runtime.md#rt-clm-lossless-records) | see record | SRC-1 `docs/architecture.md`; doctrine/design | Explicitly limits losslessness to captured intentional records | [RT-RTE-record-capture](runtime.md#rt-rte-record-capture), [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance), [RT-RTE-privacy-repair](runtime.md#rt-rte-privacy-repair), [RT-RTE-store-migration](runtime.md#rt-rte-store-migration), [EPI-RTE-store-withdrawal](#epi-rte-store-withdrawal) | None supplied | No durability/fault experiment; archive check only counts/IDs | Persistence/retrieval architecture, not universal byte or semantic preservation | Normalization, redaction, collisions, migration and explicit purge qualify the scope |

## Bounded conclusion

Qiju acquires caller/host-authored claims, retains normalized/redacted versions and selects them for later host use ([RT-RTE-record-capture](runtime.md#rt-rte-record-capture), [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval)). No inspected content admission consumes artifact evidence to decide historical truth. The schema target is shape and metadata validity; its enforcing result permits persistence, not epistemic acceptance ([EPI-RTE-shape-check](#epi-rte-shape-check), [EPI-RTE-shape-admission](#epi-rte-shape-admission)). The priority rule asks a later host to treat these records as verified through a natural-language instruction channel ([RT-BAP-host-guidance](runtime.md#rt-bap-host-guidance)); that is a reliance policy, not an additional evaluator.

The source-native log procedure limits unsupported record composition by requesting artifact anchors, agreement boundaries, rejected/undecided statuses and authoritative metadata. It also makes code/project files authoritative for artifact content. This narrows the trust claim but does not close the missing factual-check edge. Actual source warrant remains unknown. Timestamp coercion can replace malformed origin metadata with capture time ([EPI-OBJ-record-metadata](#epi-obj-record-metadata)); literal scrub and legacy rebranding can remove or change evidence-bearing meaning ([RT-RTE-privacy-repair](runtime.md#rt-rte-privacy-repair), [RT-RTE-store-migration](runtime.md#rt-rte-store-migration)). Retention and retrieval do not repair that lineage.

Action rendering produces policy from stored next-step strings. It does not infer current task completion from later records. A record with an old “Fix login” next step and a later body saying it was completed can still yield an unchecked “Fix login” action ([EPI-RTE-action-rollup](#epi-rte-action-rollup)). That implementation deduction is not a target run or a claim that all stores contain stale tasks.

No specific entailed new historical proposition is established from warranted premises, and no specific produced ampliative claim is available to assess. This is indeterminate content classification, not evidence that the host cannot conjecture. There is no established acceptance-then-lifecycle-integration event in the supplied evidence: storage precedes factual acceptance, and review recommendations lack actual accepted instances. The requested review does inspect evidence and alternative causes in doctrine; its outputs and application are not observed ([RT-RTE-skill-review](runtime.md#rt-rte-skill-review)).

Direct package refresh changes instruction bytes without a truth-apt route ([RT-RTE-skill-install](runtime.md#rt-rte-skill-install)). Optional review application could change behavioral guidance, but installation does not prove activation. Learning, reflection, theory-builder iteration, autonomy and self-improvement remain separately bounded by the supplied findings in [RT-RTE-skill-review](runtime.md#rt-rte-skill-review); none follows merely from retention or the review label. No causal benefit, reliable recall or exercised self-improvement is established. These route-specific limits do not negate the implemented persistence, selection, structural checks or withdrawal pathways.

## Shared records

### Operative objects

#### EPI-OBJ-body-md
Label: body_md

Identity: record body_md process narrative, including decision status, reasons and artifact anchors. Representational form: natural-language history interpreted by host; embedded paths/IDs are symbolic retrieval references only where a tool consumes them. Storage substrate: JSON strings in staging and short/long JSONL, then archive storage as supplied in [RT-RTE-record-capture](runtime.md#rt-rte-record-capture), [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance). Distinct identity: the retained narrative is not [RT-OBJ-qiju-skills](runtime.md#rt-obj-qiju-skills); [RT-RTE-record-capture](runtime.md#rt-rte-record-capture) is its producer/admitter route, not a supplied object counterpart. No counterpart object after comparison with supplied runtime.

SRC-1 `src/qiju/init_cmd.py` supplies requested content, not an actual generated record.

> - **Decision process** — what was decided, what was rejected, what is still undecided,
>        each with its explicit status.
> --- `src/qiju/init_cmd.py`

> Code and project documents are the single
>      source of truth — never restate content that lives in a file; anchor it instead.
> --- `src/qiju/init_cmd.py`

#### EPI-OBJ-next-steps
Label: next_steps

Identity: the record's string list of remaining items; consumed as instructions/tasks or as evidence of prior agreement. Representational form: natural-language imperatives with symbolic list structure. Storage substrate: fields of the same records as [EPI-OBJ-body-md](#epi-obj-body-md). Distinct identity: different field and action renderer from body_md; no supplied operative-object counterpart. Closest supplied route [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval). The log instruction preserves status in prose but schema does not validate agreement or completion.

> Record what we have done and
> what we agreed to do next. Do not record your own suggestions as plans or next steps.
> --- `src/qiju/init_cmd.py`

> Preserve rejected and undecided items with their status — record them only as
> rejected/undecided, never as action items, and never silently drop them.
> --- `src/qiju/init_cmd.py`

#### EPI-OBJ-record-metadata
Label: Record metadata

Identity: id, ts, project, agent, source, optional model/model_effort, title, tags/search_terms and redaction metadata used to identify/filter records. Representational form: symbolic field structure and predicates; title/tags also carry natural-language content. Storage substrate: record JSONL/Parquet, supplied [RT-RTE-record-capture](runtime.md#rt-rte-record-capture), [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval). Distinct identity: not the host's distributed parameters or installed skills; these fields are a material part of captured records, with no supplied object counterpart.

SRC-1 `src/qiju/capture.py` overwrites project/source and repairs invalid/missing timestamps. Consequently a returned timestamp need not evidence the date of the narrated event.

> if util.try_parse_iso(entry.get("ts")) is None:
>         entry["ts"] = util.utcish_now_iso()
> --- `src/qiju/capture.py`

### Routes

#### EPI-RTE-shape-check
Label: Schema shape check
Part of: [RT-RTE-record-capture](runtime.md#rt-rte-record-capture)

Endpoints/progression: prepared/redacted dictionary → schema.validate → returned dictionary or ValidationError. Owner: deterministic Python schema code. Context/state/action effects: checks required keys, types, list element classes, parseable timestamp, version/source and nonempty identity fields; no session or artifact evidence is an input. Distinct part: check only, not the capture route's disposition or persistence.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: input dictionary on success, exception on invalid shape.
- Later read-back: inapplicable — this check does not persist material; downstream capture does.
- Delegated visibility: inapplicable — no worker is invoked.
- Selection predicate: capture calls validate on prepared data and again after assigning ID.
- Invalidation or expiry: inapplicable — result applies to that dictionary at the synchronous check.
- Activation or effect: exception interrupts ordinary capture; success feeds admission.
- Evidence limits: inspected check domain is shape, not historical accuracy or semantic agreement.

SRC-1 `src/qiju/schema.py`, implementation:

> missing = [field for field in REQUIRED_FIELDS if field not in entry]
> --- `src/qiju/schema.py`

> if not isinstance(entry[name], spec.expected):
>             errors.append(f"{name} must be {spec.expected.__name__}")
> --- `src/qiju/schema.py`

> if errors:
>         raise ValidationError("; ".join(errors))
>
>     return entry
> --- `src/qiju/schema.py`

#### EPI-RTE-shape-admission
Label: Capture admission gate
Part of: [RT-RTE-record-capture](runtime.md#rt-rte-record-capture)

Endpoints/progression: shape-check success → ID-location branches → missing tier appends or existing archived-ID return. Owner: capture.log_entry code; proposer is external host/caller. Distinct part: operational disposition based on validation and identity, not [EPI-RTE-shape-check](#epi-rte-shape-check)'s evaluator. SRC-1 `src/qiju/capture.py`; shared load-bearing passages are retained in [RT-RTE-record-capture](runtime.md#rt-rte-record-capture).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: record ID after storage branch, or exception/failure.
- Later read-back: admitted records reach search/show; existing-ID skips can retain the older payload rather than the proposal.
- Delegated visibility: inapplicable — synchronous local code.
- Selection predicate: project/root rules, schema success, generated versus explicit ID and existing locations.
- Invalidation or expiry: inapplicable — no epistemic acceptance state to expire; maintenance/repair independently affect records.
- Activation or effect: permits physical retention without a factual review decision.
- Evidence limits: wired admission does not establish a particular successful capture or truthful narrative.

Admission fields: caller/host proposes; code can veto schema/project errors. Human trigger does not approve each sentence. Operating mode is open record capture, no answer oracle. Guidance and rollback/retry limits: see [RT-RTE-record-capture](runtime.md#rt-rte-record-capture). Proposed change is a normalized/redacted record retained on success, not a checked truth claim.

> entry["id"] = entry_id
>         schema.validate(entry)
>         locations = id_locations(qiju_paths, entry_id)
> --- `src/qiju/capture.py`

#### EPI-RTE-action-rollup
Label: Actions rollup
Part of: [RT-RTE-record-retrieval](runtime.md#rt-rte-record-retrieval)

Endpoints/progression: selected entries → rollup_next_steps → cli actions renderer → host/user unchecked checklist. Owner: deterministic search/CLI code. Distinct part: field-specific policy delivery, rather than general retrieval; target is string-list membership and duplicate keys, not current task truth. SRC-1 `src/qiju/search.py`, `src/qiju/cli.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: unchecked task text with source date/title.
- Later read-back: inapplicable — renderer writes no retained material; consumes previously retained next_steps.
- Delegated visibility: inapplicable — no child context.
- Selection predicate: search-selected records; nonempty stripped steps deduplicated by collapsed-whitespace casefold key, first occurrence wins.
- Invalidation or expiry: no completion/rejection lookup; only query omission or changed stored next_steps removes an item.
- Activation or effect: delivers an action checklist; task execution by a host is unobserved.
- Evidence limits: “open” is a requested interpretation, not a tested state predicate.

Concrete deterministic deduction, not execution: entry A has next_steps ["Fix login"]; newer entry B has next_steps [] and body_md "Fix login completed." Given both selected, the loop never reads B's body, so A contributes "Fix login". The renderer prints it unchecked. Even equal text with varied whitespace is merely deduplicated, not checked for completion.

> key = " ".join(text.split()).casefold()
>             if key in seen:
>                 continue
>             seen.add(key)
>             rolled.append((text, entry))
> --- `src/qiju/search.py`

> print(f'- [ ] {_cell(text)}  (from: {date} "{title}")')
> --- `src/qiju/cli.py`

#### EPI-RTE-store-withdrawal
Label: Durable store purge

Endpoints/progression: uninstall --purge-data → CLI confirmation unless --yes → cleanup.purge_data → remove home long/archive directories. Owner: caller chooses; CLI checks confirmation; helper deletes. Distinct identity: [RT-CLM-lossless-records](runtime.md#rt-clm-lossless-records) describes this mechanism but is a claim, not a route. [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance) moves/ages records; this route withdraws entire durable stores. No duplicate supplied route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: removed/skipped paths or CLI abort/failure.
- Later read-back: search/show cannot read deleted durable paths; surviving project short copies may still supply records.
- Delegated visibility: inapplicable — no delegation.
- Selection predicate: explicit purge mode; home long/archive directories that exist.
- Invalidation or expiry: irreversible deletion in this code; no automatic restoration.
- Activation or effect: removes availability, without judging the truth of individual claims.
- Evidence limits: no executed purge; not universal withdrawal from staging/backups/project short/external host state.

Admission/disposition: human or automated caller can invoke and pass --yes; confirmation is CLI policy and absent from direct helper calls. No factual evaluator or answer oracle. Mode: administrative withdrawal, not improvement-directed selection. No rollback specified; dry-run reports without deleting.

SRC-1 `src/qiju/cleanup.py`, implementation:

> for name in ("long", "archive"):
>         path = home / name
>         if path.exists() and path.is_dir():
>             if not dry_run:
>                 shutil.rmtree(path)
> --- `src/qiju/cleanup.py`

### Claims

#### EPI-CLM-verified-history
Label: Verified source-of-truth history

Claimed operation: records are verified session handoffs, privileged over platform memories for historical progress/decisions/next steps. SRC-1 `src/qiju/init_cmd.py`, doctrine/design; load-bearing exact priority passage is in [RT-BAP-host-guidance](runtime.md#rt-bap-host-guidance). Distinct identity: this is the warrant claim carried by that behavioral path, not a second declaration of the path or [RT-CLM-lossless-records](runtime.md#rt-clm-lossless-records)'s persistence claim.
Claim conclusion status: claimed

The narrower public phrasing says verifiable, which can mean possible to check through anchors rather than already checked:

> Local-first, structured session records that let Claude Code, Codex, Kiro,
>   Cursor, and future agents continue from verifiable development history.
> --- `README.md`

#### EPI-CLM-review-improvement
Label: Review produces improvements

Claimed operation: recent records turn into concrete improvements for future development. SRC-1 `README.md`, doctrine/design. Distinct identity: [RT-RTE-skill-review](runtime.md#rt-rte-skill-review) is the requested mechanism, not this public outcome claim.
Claim conclusion status: claimed

> **Finds the gold** — `/qiju-review` turns last week's records into concrete
>   improvements for the next round of development.
> --- `README.md`

The procedure's actual safeguards oppose a reading of unrestricted lesson generation, but remain requests:

> Do not invent missing record details. Mark gaps as "unknown from records."
> --- `src/qiju/init_cmd.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

### Supporting transformation evidence

SRC-1 `src/qiju/migrate.py`, implementation. These passages support the ledger's semantic counterexample, not a claim that this input was observed:

> return value.replace("KEDU", "QIJU").replace("Kedu", "Qiju").replace("kedu", "qiju")
> --- `src/qiju/migrate.py`

> if isinstance(value, str):
>         return _rebrand_text(value)
> --- `src/qiju/migrate.py`
