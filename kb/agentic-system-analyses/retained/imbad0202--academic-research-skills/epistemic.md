---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Epistemic routes of academic-research-skills: research synthesis, citation and claim checks, screening admission and revocable reliance."
run-id: AAS-2026-10-17-academic-research-skills-6fe859d62c16-01
reviewed-boundary: "060cb3cbffc2ca1bdfb8f7c6d2ffa4883cf09b1a"
---

# academic-research-skills epistemic report

## Source-and-claim boundary

The question is how ARS moves from literature and user materials to substantive claims, checks them, and permits downstream reliance. The functional boundary and external exclusions are see [boundary](boundary.md#boundary-and-evidence); source identity and layers are see its [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not an observed run or causal experiment. Host model behavior, provider weights, actual human reading, external source truth, authentic data and performed experiments are not established by package code. No target code or tests were executed.

The runtime is a provisional container account, not evidence that its role instructions operated. Additional direct inspection separates citation existence, claim support, read declarations and screening disposition. These checks have different domains and cannot certify each other. Public claims assessed are [EPI-CLM-integrity-boundary](#epi-clm-integrity-boundary), [EPI-CLM-synthesis-understanding](#epi-clm-synthesis-understanding) and [EPI-CLM-review-calibration](#epi-clm-review-calibration), plus [RT-CLM-complete-pipeline](runtime.md#rt-clm-complete-pipeline) and [RT-CLM-pi-scope](runtime.md#rt-clm-pi-scope).

Coverage is deliberately bounded. Direct means this member read the source; supplied means it relies on the cited runtime record and its evidence passages. A path appearing only in a search is not an inspected implementation.

| Entry point or operation | SRC-1 source path | Coverage and records, or conclusion prevented |
|---|---|---|
| Pi discovery and command dispatch | `package.json`, `pi/wrapper.js`, `commands/ars-full.md` | Manifest directly read; adapter/dispatch supplied: [RT-RTE-command-dispatch](runtime.md#rt-rte-command-dispatch). Four manifest skills do not exclude separately shipped screening. |
| Claude tool hook | `hooks/hooks.json`, `hooks/run_guard.sh`, `scripts/ars_write_scope_guard.py` | Manifest directly read; launcher/core supplied: [RT-RTE-tool-scope](runtime.md#rt-rte-tool-scope). Write/Edit/MultiEdit/Bash matcher is not universal mediation. |
| Research source grading and synthesis | `deep-research/agents/source_verification_agent.md`, `deep-research/agents/synthesis_agent.md`, `deep-research/SKILL.md` | Direct bounded role reads and skill searches: [EPI-RTE-source-grading](#epi-rte-source-grading), [EPI-RTE-synthesis-content](#epi-rte-synthesis-content). No source-backed instance of a new scientific finding established. |
| Folder/corpus intake and literature consumption | `scripts/adapters/folder_scan.py`, `sr-screener/scripts/build_outputs.py`, `academic-paper/agents/literature_strategist_agent.md` | Supplied boundary and [RT-RTE-screening-fanout](runtime.md#rt-rte-screening-fanout); adapter details and every import format not audited. Source warrant of a particular imported item remains unknown. |
| Citation API and standalone verifier | `scripts/verification_gate/__init__.py`, `scripts/citation_verification_summary.py`, `scripts/verify_passport.py` | API/reducer directly read completely; CLI supplied: [EPI-RTE-citation-lookup](#epi-rte-citation-lookup), [RT-RTE-final-output](runtime.md#rt-rte-final-output). Resolver matching internals not independently audited. |
| Claim audit API, disposition and formatter | `scripts/claim_audit_pipeline.py`, `scripts/claim_audit_finalizer.py`, `academic-paper/agents/formatter_agent.md`, `academic-pipeline/agents/pipeline_orchestrator_agent.md` | Direct API signature/judge wrapper, finalizer classifier/reduction reads; formatter/orchestrator targeted searches plus supplied final-output route. [EPI-RTE-claim-judgment](#epi-rte-claim-judgment), [EPI-RTE-audit-disposition](#epi-rte-audit-disposition). Retrieval-driver truth and all sampling/cleanup paths not audited. |
| Read declaration and withdrawal commands | `commands/ars-mark-read.md`, `commands/ars-unmark-read.md`, `scripts/human_read_attestation_resolver.py` | Command searches and direct resolution core: [EPI-RTE-read-withdrawal](#epi-rte-read-withdrawal). Writer internals and identity authentication not audited. |
| Screening merger and pilot | `sr-screener/scripts/merge_decisions.py`, `sr-screener/scripts/build_workflow.py` | Direct merge, QC, pilot-comparison and pilot-gate cores: [EPI-RTE-screening-merge](#epi-rte-screening-merge), [EPI-RTE-pilot-comparison](#epi-rte-pilot-comparison). Builder/template dispatch supplied: [RT-RTE-screening-fanout](runtime.md#rt-rte-screening-fanout). Full-text merge branch not audited. |
| Revision, re-review, integrity and final packaging | `academic-pipeline/agents/pipeline_orchestrator_agent.md`, `academic-paper/agents/formatter_agent.md` | Supplied [RT-RTE-revision-review](runtime.md#rt-rte-revision-review), [RT-RTE-final-output](runtime.md#rt-rte-final-output). Detailed integrity agent, patch engine, re-review checker and package verifier not audited; prevents complete semantic/safety judgment. |
| Retention and resumed consumption | `scripts/run_ledger.py`, `academic-pipeline/agents/state_tracker_agent.md`, `academic-pipeline/references/passport_as_reset_boundary.md` | Supplied [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery). No independent memory-member findings supplied. Hash/receipt checks do not endorse scientific claims. |
| Optional cross-model checks | `shared/cross_model_verification.md`, `scripts/cross_model_codex_transport.py` | Supplied [RT-RTE-cross-verification](runtime.md#rt-rte-cross-verification); full generic-consumer retention not inspected. |
| Evaluation/change admission | `scripts/run_evals.py`, `scripts/check_ranking_lift.py` | Supplied [RT-RTE-evaluation-admission](runtime.md#rt-rte-evaluation-admission). No new audit of gold validity or shipped recorded results. |
| Other material operations | `deep-research/agents/meta_analysis_agent.md`, `academic-pipeline/agents/integrity_verification_agent.md`, `scripts/claim_standing_discovery.py`, `scripts/temporal_integrity_audit.py`, `scripts/verify_submission_package.py` | Available but uninspected here. Meta-analysis derivations, experiment alignment, later claim-standing changes, temporal/retraction coverage and package acceptance remain unassessed; no system-complete negative follows. Optional monitoring, calibration, observer and maintenance branches likewise not fully traced. |

Missing end-to-end traces prevent conclusions about actual acceptance, production lineage, compliance, empirical accuracy or benefit. Missing warranted input instances and semantic comparisons prevent attribution of a specific entailed discovery or accepted ampliative claim. Uninspected operations above prevent a universal claim that ARS only reformats or never produces knowledge. No supplied fact needs supersession: the new records split material parts of valid runtime containers rather than contradicting them.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-synthesis-report](#epi-obj-synthesis-report) | Cross-source findings, explanatory reconciliation and gap claims | see record | see record | No generated instance or source-to-claim comparison |
| [EPI-OBJ-citation-summary](#epi-obj-citation-summary) | Index lookup outcomes; anchor-kind presence | see record | see record | Does not assert claim faithfulness |
| [EPI-OBJ-claim-audit](#epi-obj-claim-audit) | Support/ambiguity/violation judgments and rationales | see record | see record | Caller-supplied retrieval and model judgment |
| [EPI-OBJ-screening-decisions](#epi-obj-screening-decisions) | Protocol-relative eligibility decisions, reasons and pilot agreement | see record | see record | Not a source-truth or full-text acquisition certificate |
| [EPI-OBJ-read-ledger](#epi-obj-read-ledger) | User declaration of reading coverage, not demonstrated reading | see record | see record | Declaration authenticity and actual comprehension unestablished |
| [RT-OBJ-ref-markers](runtime.md#rt-obj-ref-markers) | Some status fields report evidence state; delimiters alone assert none | see record | see record | Marker presence alone grants no warrant |
| [RT-OBJ-run-ledger](runtime.md#rt-obj-run-ledger) | Recorded decisions, counters and artifact bindings | see record | see record | Integrity of chain is not truth of words |
| [RT-OBJ-pipeline-skill](runtime.md#rt-obj-pipeline-skill) | Mainly policy; includes procedural/design claims | see record | see record | Static guidance, not accepted task findings |
| [RT-CMP-session-model](runtime.md#rt-cmp-session-model), [RT-CMP-cross-model](runtime.md#rt-cmp-cross-model) | Not determinable at parameter level | see records | see records | Distributed-parametric state is external; no individuated proposition or weight-update trace |

## Authority-route ledger

Each row is a separate consequential function. A repeated route citation denotes a valid container with multiple functions, not a merger of checking and disposition. Fields owned by declaring records are left as `see`; the architectural status is this overlay's assessment. No row has observed operation evidence.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-source-grading](#epi-rte-source-grading) | check/evidence production | doctrine only | [EPI-OBJ-synthesis-report](#epi-obj-synthesis-report) | no content change | External findings and source quality | Model; hierarchy and cross-source checking | Phase 2 | Grades and per-claim verdicts | Protocol | Fallible source/claim assessment, not independent raw-data verification | Supplies evidence weights to synthesis | Synthesis model; verification report; advisory/evidential; Phase 3 | see [EPI-RTE-source-grading](#epi-rte-source-grading) | [EPI-CLM-integrity-boundary](#epi-clm-integrity-boundary) | none | No observed operation |
| [EPI-RTE-synthesis-content](#epi-rte-synthesis-content) | content transformation | doctrine only | [EPI-OBJ-synthesis-report](#epi-obj-synthesis-report) | truth-apt transformation: indeterminate | Findings to integrated claims | Model; thematic and interpretive synthesis | Phase 3 | New-understanding candidate report | Protocol | No checked entailment or accepted novel claim established | Feeds report compilation | Compiler/scholar; synthesis report; advisory; later drafting | see [EPI-RTE-synthesis-content](#epi-rte-synthesis-content) | [EPI-CLM-synthesis-understanding](#epi-clm-synthesis-understanding) | generation is not acceptance | Imported summaries, reshaping, derivation and conjecture remain distinguishable only with actual inputs/outputs |
| [EPI-RTE-citation-lookup](#epi-rte-citation-lookup) | check/evidence production | implemented | [EPI-OBJ-citation-summary](#epi-obj-citation-summary) | truth-apt transformation: entailed derivation | Resolver outcomes to three-class lookup label | Fixed reducer over matched/unmatched/skipped/unreachable and query kind | verify_citation/verify_passport call | true, false, unresolvable plus anchor flag | Deterministic summary; invalid slug raises | Classification follows supplied outcomes; source existence remains index-dependent | Provides current finalizer evidence, not a gate by itself | Finalizer; summary JSON; evidential; current/reused verification | see [EPI-RTE-citation-lookup](#epi-rte-citation-lookup) | [EPI-CLM-integrity-boundary](#epi-clm-integrity-boundary) | lookup is not faithfulness | Resolver internals and external evidence truth not independently established |
| [EPI-RTE-claim-judgment](#epi-rte-claim-judgment) | check/evidence production | implemented | [EPI-OBJ-claim-audit](#epi-obj-claim-audit) | truth-apt transformation: indeterminate | Cited claim versus retrieved passage; constraints versus sentences | Injected judge; caller retrieval; schema/path validation | Opt-in workflow audit or direct API | Judgments or tagged failure | Checks shape, not semantic truth | A local support assessment; no empirical authenticity license | Produces aggregates for separate disposition | Finalizer; aggregate dictionaries; evidential; audit pass | see [EPI-RTE-claim-judgment](#epi-rte-claim-judgment) | [EPI-CLM-integrity-boundary](#epi-clm-integrity-boundary) | implemented judge request is not reliable judging | Production retrieval driver is not established by the API; corpus argument is reserved |
| [EPI-RTE-audit-disposition](#epi-rte-audit-disposition) | disposition/acceptance | implemented | [EPI-OBJ-claim-audit](#epi-obj-claim-audit) | no content change | Judgment/severity to refusal recommendation | Fixed matrix; schema-valid input assumed | After audit, before formatting | gate_refuse, annotations and reasons | Deterministic result; final refusal is model protocol | Operational admission only; passing is not acceptance of all claims | Unsupported/constraint failures block prescribed formatting; ambiguity/paywall/tool failure can continue | Formatter; tokens/aggregate; enforcing instruction conditional on compliance; current output | see [EPI-RTE-audit-disposition](#epi-rte-audit-disposition) | [EPI-CLM-integrity-boundary](#epi-clm-integrity-boundary) | advisory continuation is not warrant | No observed operation |
| [EPI-RTE-read-withdrawal](#epi-rte-read-withdrawal) | disposition/acceptance | implemented | [EPI-OBJ-read-ledger](#epi-obj-read-ledger) | no content change | Latest declaration and anchor coverage | Fixed event-order/scope resolver, not a reading examiner | Every finalizer pass | covered/partial/unknown/rescinded/invalid | Deterministic eligibility; model rerenders markers | Declared coverage only; no claim verification | Withdrawn eligibility prevents ok promotion; does not clear unsupported claims | Finalizer then formatter; transient state/markers; permissive or refusing policy; current and next pass | see [EPI-RTE-read-withdrawal](#epi-rte-read-withdrawal) | [EPI-CLM-integrity-boundary](#epi-clm-integrity-boundary) | read attestation is not epistemic acceptance | No observed operation |
| [EPI-RTE-screening-merge](#epi-rte-screening-merge) | disposition/acceptance | implemented | [EPI-OBJ-screening-decisions](#epi-obj-screening-decisions) | no content change | Review decisions to operational eligibility | Fixed merge/QC policy; human override wins | After A/B/ADJ/QC results | Final, pending, QC promotion/flag | Enforcing within merger output | Protocol-relative selection, not universal truth | Selects records for reporting/export; missing decisions remain pending | Reporter/corpus producer; decisions.json; selection; screening revision | see [EPI-RTE-screening-merge](#epi-rte-screening-merge) | [RT-CLM-complete-pipeline](runtime.md#rt-clm-complete-pipeline) | screening admission is not manuscript inclusion | No observed operation |
| [EPI-RTE-pilot-comparison](#epi-rte-pilot-comparison) | check/evidence production | implemented | [EPI-OBJ-screening-decisions](#epi-obj-screening-decisions) | truth-apt transformation: entailed derivation | AI advance labels versus human pilot labels | Fixed count/ratio comparison; team labels are local reference | Merge with pilot labels | Missed advances, agreement, sensitivity or null | Evidence producer; separate builder gate consumes | Agreement only on compared pilot and label definition | Provides gate input and amendment advice | Builder/user; pilot_check.json; evidential; same hashed context | see [EPI-RTE-pilot-comparison](#epi-rte-pilot-comparison) | [RT-CLM-complete-pipeline](runtime.md#rt-clm-complete-pipeline) | pilot recall is not dataset truth | No observed operation |
| [RT-RTE-screening-fanout](runtime.md#rt-rte-screening-fanout) | operational admission/selection/consumption | implemented | [EPI-OBJ-screening-decisions](#epi-obj-screening-decisions) | no content change | Full-run pilot admission | Builder gate over current comparison/context or override | Before generated out-of-pilot work | Block, admitted run, or recorded override | Enforcing builder path; bypassable manual alternatives | No broader license than current pilot | Withholds full-run generation unless passing or reason supplied | Builder; pilot JSON/hash checks; enforcing; generation | see [RT-RTE-screening-fanout](runtime.md#rt-rte-screening-fanout) | [RT-CLM-complete-pipeline](runtime.md#rt-clm-complete-pipeline) | none | No observed operation |
| [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery) | retention | implemented | [RT-OBJ-run-ledger](runtime.md#rt-obj-run-ledger) | no content change | Receipt/decision storage | Locked chain/file validation | Helper append | Persisted ledger or refusal | Enforcing helper append; reset remains protocol | Recorded provenance only | Preserves state consumed by later resume | Tracker; YAML/report; recovery selection; later invocation | see [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery) | [RT-CLM-complete-pipeline](runtime.md#rt-clm-complete-pipeline) | hash integrity is not truth | No observed operation |
| [RT-RTE-final-output](runtime.md#rt-rte-final-output) | operational admission/selection/consumption | doctrine only | [RT-OBJ-ref-markers](runtime.md#rt-obj-ref-markers) | no content change | Markers/policies to conversion permission | Model formatter under terminal rules | Stage 5 after fresh evaluation | Refusal, repair, conversion | Instruction; direct shell conversions not universally covered | No scientific-truth guarantee | Permits or blocks final deliverables | Formatter; working markers; enforcing instruction; one finalization | see [RT-RTE-final-output](runtime.md#rt-rte-final-output) | [EPI-CLM-integrity-boundary](#epi-clm-integrity-boundary) | none | No observed operation |
| [RT-RTE-final-output](runtime.md#rt-rte-final-output) | content transformation | doctrine only | [RT-OBJ-ref-markers](runtime.md#rt-obj-ref-markers) | truth-apt transformation: non-ampliative reshaping | Working manuscript to clean converted artifact | Formatter strips provenance only after gates | Final conversion | Clean artifact, provenance retained elsewhere | Instruction | No new warrant; clean output omits visible lineage | Submission output lacks internal markers | External reader; clean file; presentation; delivered artifact | see [RT-RTE-final-output](runtime.md#rt-rte-final-output) | [EPI-CLM-integrity-boundary](#epi-clm-integrity-boundary) | clean does not mean verified | No observed operation |
| [RT-RTE-revision-review](runtime.md#rt-rte-revision-review) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-synthesis-report](#epi-obj-synthesis-report) | no content change | Authorized manuscript patch and re-review decision | Author scope, model review, prescribed checker | Revision/re-review | Accept/Minor/Major, deferral or abort | Protocol; internals uninspected | Bounded editorial decision, not known-answer oracle | Determines next revision or final integrity | Orchestrator; patch/evidence/decision; selection; revision round | see [RT-RTE-revision-review](runtime.md#rt-rte-revision-review) | [EPI-CLM-review-calibration](#epi-clm-review-calibration) | none | No observed operation |
| [RT-RTE-cross-verification](runtime.md#rt-rte-cross-verification) | check/evidence production | implemented | [EPI-OBJ-claim-audit](#epi-obj-claim-audit) | truth-apt transformation: indeterminate | Bounded second-model verification request | Provider judgment plus local receipt/event checks | Opt-in with consent | Grounded-shaped receipt, disagreement, unavailable | Local shape rejection; downstream judgment policy | Not an oracle or proof of independence | Supplies primary workflow with secondary evidence | Primary model/user; receipt; advisory; checkpoint | see [RT-RTE-cross-verification](runtime.md#rt-rte-cross-verification) | [EPI-CLM-integrity-boundary](#epi-clm-integrity-boundary) | none | No observed operation |
| [RT-RTE-evaluation-admission](runtime.md#rt-rte-evaluation-admission) | operational admission/selection/consumption | implemented | [RT-OBJ-pipeline-skill](runtime.md#rt-obj-pipeline-skill) | no content change | Proposed package change versus baseline metrics | Numeric comparison and PR acknowledgement | Maintainer evaluation | Blocked or admitted comparison result | Checker result; universal CI forcing unestablished | Selected synthetic gold metrics only | Can condition change admission; no automatic deployment | Maintainer/CI; report; permissive/blocking policy; proposed change | see [RT-RTE-evaluation-admission](runtime.md#rt-rte-evaluation-admission) | [RT-CLM-complete-pipeline](runtime.md#rt-clm-complete-pipeline) | no causal component or self-improvement conclusion | No observed operation |

Lifecycle integration is not established by the inspected routes. Retaining a report, exporting eligibility, accepting a patch, or permitting a formatted artifact does not by itself show an evidence-consuming acceptance of a substantive claim followed by its integration. This is a bounded evidence limit, not an absence claim about all ARS branches.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-synthesis-understanding](#epi-clm-synthesis-understanding) | see record | see record | Cross-source interpretation, weighting and contradiction procedures | No deterministic implementation of substantive synthesis inspected; [EPI-RTE-synthesis-content](#epi-rte-synthesis-content) is doctrine only | None established | No input/output witness or controlled test | A specified candidate-generation method, not established new knowledge | Scholar confirmation explicitly pending; novelty and entailment unresolved |
| [EPI-CLM-integrity-boundary](#epi-clm-integrity-boundary) | see record | see record | Explicit separation of reported consistency from empirical authenticity | [EPI-RTE-citation-lookup](#epi-rte-citation-lookup), [EPI-RTE-claim-judgment](#epi-rte-claim-judgment), [EPI-RTE-audit-disposition](#epi-rte-audit-disposition), [EPI-RTE-read-withdrawal](#epi-rte-read-withdrawal) | None established | No ARS effectiveness experiment; models/resolvers can err; optional/sampled checks | Selected checks and operational gates are present, with narrow licenses | No warrant for performed procedures or reproduction; some claimed checks unassessed |
| [EPI-CLM-review-calibration](#epi-clm-review-calibration) | see record | see record | Source explicitly calls current live reviews NOT_CALIBRATED | [RT-RTE-revision-review](runtime.md#rt-rte-revision-review) is prescribed orchestration; calibration internals uninspected | None established | No validity/reliability comparison assessed | Model editorial feedback is not a calibrated scientific oracle | Does not warrant interpreting Accept as true research |
| [RT-CLM-complete-pipeline](runtime.md#rt-clm-complete-pipeline) | see record | see record | Stage protocol and checkpoints | [RT-RTE-command-dispatch](runtime.md#rt-rte-command-dispatch), [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery), [EPI-RTE-screening-merge](#epi-rte-screening-merge) | None established | Stage coverage does not establish quality or gate compliance | Shipped workflow guidance with selected executable helpers | Not a runtime-wide theorem of mandatory checks |
| [RT-CLM-pi-scope](runtime.md#rt-clm-pi-scope) | see record | see record | Explicit prompt-level limit | [RT-RTE-tool-scope](runtime.md#rt-rte-tool-scope), [RT-RTE-command-dispatch](runtime.md#rt-rte-command-dispatch) | None established | No deployed host trace | Hook controls cannot be attributed to Pi wrapper | Independent host protections remain outside boundary |

## Bounded conclusion

ARS specifies substantive research work, not merely retrieval or formatting. Its synthesis role requests integrated findings and new interpretive constructs; without a source-to-output witness, their relation remains indeterminate. The source gives positive reasons not to collapse all synthesis into summary, but no basis for calling every candidate an ampliative discovery or an accepted claim. Source grading and contradiction assessment are evidence-consuming model procedures in doctrine, not observed checks or infallible inference.

Citation verification has an inspectable symbolic domain: given resolver outcomes, a matched result wins; absent matches, an ID-keyed miss yields false; title-only misses, outages and manual exemptions can yield unresolvable. This is derivation of a classification from inputs, not derivation of scientific truth from warranted premises. The source warrant of imported literature remains unknown for actual unseen items. Index matches and anchor-kind presence do not entail source support, data authenticity or reproducibility. The claim-audit API supplies a different path: injected retrieval and judge callbacks produce support/constraint judgments, and a separate deterministic matrix supplies refusal annotations. Its corpus parameter does not implement retrieval. Optional activation, caller context, sampling, outages and advisory cases limit the license.

Operational authority is concrete but heterogeneous. The screening merger chooses eligible records under fixed policy, preserves pending work and gives human overrides priority; the pilot compares automatic labels with review-team labels and feeds a hash-bound builder gate that admits explicit overrides. Eligibility is not manuscript inclusion or scientific acceptance. Read declarations can be rescinded; the current resolver can withdraw coverage eligibility, and the prescribed finalizer can demote a formerly ok marker. Neither reading nor declaring reading clears source-support failures. Final-output gates and marker stripping are model instructions, not an unavoidable conversion monitor. Passing and cleaning an artifact therefore do not establish accepted knowledge.

The package retains provenance, decisions and output artifacts for later consumers, including resumed stages. No inspected evidence establishes lifecycle integration after a recorded acceptance of a new scientific claim. Review, revision and numeric change-admission mechanisms are independently bounded by their criteria; manuscript revision does not alone change ARS's own behavior-determining organization. No single epistemic score follows. Learning, reflection, autonomy and self-improvement are not inferred from retained artifacts, multiple agents or review loops. Screening criteria's separately qualified theory-builder account is see [RT-RTE-screening-fanout](runtime.md#rt-rte-screening-fanout); no stronger inference is added. Provider-owned distributed-parametric changes and exact weight fixity remain uninspected, as recorded separately in [RT-CMP-session-model](runtime.md#rt-cmp-session-model) and [RT-CMP-cross-model](runtime.md#rt-cmp-cross-model).

## Shared records

### Operative objects

#### EPI-OBJ-synthesis-report
Label: Synthesis Report

Natural-language integrated findings, contradiction resolutions and gap claims; a literature matrix and pair inventory add symbolic fields. The intended substrate is Phase 3 report files/context, not model weights. SRC-1, `deep-research/agents/synthesis_agent.md`. No supplied object counterpart after comparison: [RT-OBJ-pipeline-skill](runtime.md#rt-obj-pipeline-skill) is static instruction, not the deliverable. No generated report instance is established.

> Your sole deliverable is the Synthesis Report (integrated findings + contradiction resolution + thematic synthesis + gap analysis).
> --- `deep-research/agents/synthesis_agent.md`

#### EPI-OBJ-citation-summary
Label: Citation verification summary

Symbolic dictionary/list returned by verification APIs, with citation/ref identifiers, lookup class, anchor flag, timestamp and resolver outcomes; optional cache metadata. Persistence into passport is a caller responsibility. SRC-1, `scripts/verification_gate/__init__.py`. Distinct from [RT-OBJ-ref-markers](runtime.md#rt-obj-ref-markers), which live in prose; no counterpart among supplied declarations.

> "lookup_verified": reduce_lookup_verified(resolver_outcomes),
> "anchor_present": _anchor_present(anchor),
> --- `scripts/verification_gate/__init__.py`

#### EPI-OBJ-claim-audit
Label: Claim audit results

Symbolic passport aggregate rows containing natural-language rationales; dictionaries are returned by the API, with downstream passport/file retention handled by the orchestrator. The content concerns source support and constraints. SRC-1, `scripts/claim_audit_pipeline.py`, `scripts/claim_audit_finalizer.py`. No supplied object counterpart after comparison: [RT-OBJ-ref-markers](runtime.md#rt-obj-ref-markers) is the downstream display/gate carrier, not these judgments.

> The classify_* functions
> project each passport aggregate row to `{annotation, tier, gate_refuse}`;
> --- `scripts/claim_audit_finalizer.py`

#### EPI-OBJ-screening-decisions
Label: Screening decisions

Symbolic JSON labels, ordered exclusion codes, provenance and fixed merge fields, with natural-language reasons. Stored in `decisions.json`; pilot comparison is stored separately in `pilot_check.json`. SRC-1, `sr-screener/scripts/merge_decisions.py`. No supplied object counterpart; these are task decisions, not [RT-OBJ-run-ledger](runtime.md#rt-obj-run-ledger) receipts. The distinct producer/consumer path is within the supplied screening route.

> srlib.save_json(os.path.join(work, "decisions.json"), final)
> --- `sr-screener/scripts/merge_decisions.py`

#### EPI-OBJ-read-ledger
Label: User-attested read ledger

Symbolic timestamped declarations keyed by citation key with scope/locators and optional rescission. Local ledger loading feeds a transient resolver dictionary. Human declarations describe claimed reading; code evaluates coverage rules, not whether the reader read or understood. SRC-1, `commands/ars-mark-read.md`, `commands/ars-unmark-read.md`, `scripts/human_read_attestation_resolver.py`. Distinct from [RT-OBJ-run-ledger](runtime.md#rt-obj-run-ledger), whose role is workflow receipt/decision recovery.

> "latest matching event rescinds the attestation",
> --- `scripts/human_read_attestation_resolver.py`

### Routes

#### EPI-RTE-source-grading
Label: Source verification grading

Part of: [RT-RTE-pipeline-stages](runtime.md#rt-rte-pipeline-stages)

Phase 2 bibliography/source material → model verifier → graded sources and per-claim judgments → synthesis. Owner: source-verification role under research orchestration. Target/domain: source quality and factual claims in supplied literature. SRC-1, `deep-research/agents/source_verification_agent.md`. This is a distinct check inside the stage container, not a second declaration of the entire pipeline. The role proposes verdicts, reader/human retains interpretive authority; no known-answer oracle is established. The hierarchy is evaluation guidance, not a demonstrated theory-revision route.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Evidence grades, flags and verification report
- Later read-back: uninspected — later persistence/reload of an actual verification report is not supplied
- Delegated visibility: Bibliography and permitted phase context; no actual host isolation trace
- Selection predicate: Sources entering Phase 2 investigation
- Invalidation or expiry: Unverified claims are flagged; source findings can be reassessed
- Activation or effect: Requested report changes synthesis evidence weighting; actual compliance unobserved
- Evidence limits: Doctrine/design; source truth and model cross-reference reliability not established

> Cross-reference claims against 2+ independent sources
> --- `deep-research/agents/source_verification_agent.md`

#### EPI-RTE-synthesis-content
Label: Synthesis content generation

Part of: [RT-RTE-pipeline-stages](runtime.md#rt-rte-pipeline-stages)

Verified/graded source reports and question/method context → model synthesis → Synthesis Report → report compiler/scholar. SRC-1, `deep-research/agents/synthesis_agent.md`. This material transformation is part of the pipeline container. The model proposes interpretations; scholar confirms pair resolutions. No answer oracle is specified. Content/update relation remains indeterminate: doctrine requests thematic organization and new constructs, but neither semantic preservation, entailment nor non-entailment of a concrete output is established. Theory-related interpretations are task outputs, not an observed theory-building iteration. Localized synthesis methods exist; actual consumption, content-directed criticism and retained iteration of a scientific theory are unestablished here, independently of the screening-criteria account in runtime.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Candidate synthesis narrative, matrix, gaps and pair inventory
- Later read-back: uninspected — report retention is prescribed, but no later invocation with a retained instance is evidenced
- Delegated visibility: Phase 1–3 context; pair evidence pointers are limited to corpus context
- Selection predicate: Selected thematic/candidate paper pairs, not exhaustive contradiction enumeration
- Invalidation or expiry: Scholar may dispute a resolution; pending confirmation is not self-promoted
- Activation or effect: Report is intended to shape drafting; no observed activation
- Evidence limits: Doctrine/design; no warranted premise set, checked inference or actual accepted novel claim

> You always emit `pending` on emission; `confirmed` / `disputed` are scholar-set after the scholar reviews the pair. Never self-assign `confirmed` or `disputed`.
> --- `deep-research/agents/synthesis_agent.md`

#### EPI-RTE-citation-lookup
Label: Citation lookup reduction

Part of: [RT-RTE-final-output](runtime.md#rt-rte-final-output)

Corpus entry plus caller-supplied prose slug/anchor → resolver outcomes → reducer → summary → current finalizer. Owner: verification API/helper code; external indexes own their records. SRC-1, `scripts/verification_gate/__init__.py`, `scripts/citation_verification_summary.py`. A check part, not the formatter's disposition. Fixed code decides output labels; caller supplies clients and source join. No truth oracle beyond those fallible inputs. Manual origin skips all resolvers. Anchor presence checks kind membership, not value fidelity or source support.

Concrete implementation deduction, not execution: provide a non-empty ref slug and `obtained_via: manual`. All four outcomes are skipped. The reducer's applicable list is empty, neither match nor ID-miss branch fires, and output is `unresolvable`. A page-kind anchor makes `anchor_present` true even though this path did not query a source. Separately, one matched outcome wins even alongside an ID-keyed miss; all title-only misses produce unresolvable, not false. These countercases rule out treating either summary field as proof of claim support. The relation is entailed derivation within the classification domain only; truth of external resolver premises is not supplied.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Three-class label, anchor flag and detailed outcomes; invalid slug raises ValueError
- Later read-back: Cached resolver outcomes can reach later checks; cache age is advisory and opt-in stale revalidation recomputes; actual reuse unobserved
- Delegated visibility: Caller joins corpus citation key to writer-prose ref slug and parsed anchor
- Selection predicate: Each corpus entry; manual exemption; arXiv resolver requires ID
- Invalidation or expiry: Recomputation depends on caller inputs and cache policy; missing join refuses
- Activation or effect: Summary supplies evidence to policy; it neither accepts a claim nor converts output
- Evidence limits: Implementation only; injected clients, cache and external metadata may be fallible

> if any(o.get("status") == STATUS_MATCHED for o in applicable):
>     return "true"
> --- `scripts/citation_verification_summary.py`

#### EPI-RTE-claim-judgment
Label: Claim audit judgment

Part of: [RT-RTE-final-output](runtime.md#rt-rte-final-output)

Caller-selected citations/manifests/sentences → injected retrieval and judge → validated audit aggregates. Owner: API plus caller-owned retrieval/judge. SRC-1, `scripts/claim_audit_pipeline.py`. The material check is separate from disposition below. Target: source support for a cited assertion, or compliance with active negative constraints; not authentic experiments or reproduction. The judge proposes support judgments, fixed code validates allowed shapes/constraint identifiers, downstream policy decides continuation; human can repair claims. No known-answer oracle. No direct semantic guarantee follows from callback shape validation. A critical counterexample to assuming a full retrieval implementation is the reserved corpus parameter: the API explicitly leaves retrieval in `retrieve_fn`. Two uncited streams also differ; passing only detector positives can miss uncited constraint violations.

The API names model/prompt identity for cache scope; unknown model identity is run-bound. This labels caller state, not an immutable weight digest. Exact external model mutability remains see the runtime components.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Audit result/violation/drift/failure/sampling aggregates
- Later read-back: Optional cached verdicts can reach later API invocations; unknown judge identity prevents cross-run reuse by run-bound cache key
- Delegated visibility: Caller controls citations, retrieved passages, manifests and full versus filtered uncited sentences
- Selection predicate: Workflow opt-in audit or direct API; caller config bounds sampling
- Invalidation or expiry: Changed evidence/model/prompt/config affects reuse; schema-invalid judgments become failure paths
- Activation or effect: Implemented call and validation create decision candidates for separate finalizer; actual judging unobserved
- Evidence limits: Implementation of callback mediation, not validated claim accuracy or production retrieval driver

> # Intentional no-op: `corpus` is reserved for the production retrieval-driver
> # wiring (spec §4 step 2). Mark as read so static analysers (ruff ARG002,
> # mypy strict unused-arg) do not flag the forward-compat parameter.
> _ = corpus
> --- `scripts/claim_audit_pipeline.py`

#### EPI-RTE-audit-disposition
Label: Claim audit disposition

Part of: [RT-RTE-final-output](runtime.md#rt-rte-final-output)

Audit aggregates → fixed classification and reduction → annotations/gate_refuse → formatter instruction. Owner: finalizer code for result, model formatter for honoring it. SRC-1, `scripts/claim_audit_finalizer.py`, `academic-paper/agents/formatter_agent.md`. Software decides operational refusal classification, not whether source evidence is true. Unsupported source-level judgments and constraint violations refuse; ambiguity, paywall and tool-failure paths can pass with advisories. Human repairs prose/source/constraint scope under workflow rules; merely marking read cannot erase a structural verdict. No known-answer oracle is added by mapping a model judgment.

Concrete input deduction: `judgment=UNSUPPORTED`, `defect_stage=synthesis_overclaim` returns `[HIGH-WARN-CLAIM-NOT-SUPPORTED]`, high_warn, gate_refuse true. `apply_finalizer` adds the annotation/reason and returns overall gate_refuse true. The formatter refusal list names that token and offers rewrite, replace citation or drop claim, not read acknowledgment. Conversely AMBIGUOUS returns low_warn and gate_refuse false. This is deterministic disposition of supplied judgments, not an independent second check. It does no file I/O, so actual artifact refusal remains a separate host/model obligation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Annotations, gate_refuse Boolean and refusal reasons
- Later read-back: uninspected — API does no I/O; later retention and re-consumption are caller-managed
- Delegated visibility: All explicitly passed aggregate rows; omitted aggregates produce no annotations
- Selection predicate: Classify each supplied row, reduce any refusal reason
- Invalidation or expiry: Out-of-contract judgments can raise; repaired evidence/prose requires a new pass
- Activation or effect: Locally computes refusal recommendation; prescribed formatter blocks current conversion
- Evidence limits: No global conversion interposition, no inference that a non-refusal is acceptance

> if result["gate_refuse"]:
>     gate_refuse_reasons.append(result["annotation"])
> --- `scripts/claim_audit_finalizer.py`

#### EPI-RTE-read-withdrawal
Label: Read declaration withdrawal

Part of: [RT-RTE-final-output](runtime.md#rt-rte-final-output)

Current read ledger plus citation/anchor → strict resolver → transient covered/partial/unknown/rescinded/invalid state → prescribed finalizer marker → formatter. Owner: resolver for state, user for declaration, finalizer for marker use. SRC-1, `scripts/human_read_attestation_resolver.py`, `commands/ars-mark-read.md`, `commands/ars-unmark-read.md`, `academic-pipeline/agents/pipeline_orchestrator_agent.md`. No supplied route separately declared this part. This is operational attestation eligibility, not evidence-consuming acceptance of a source claim. User proposes/withdraws declared coverage; fixed code can reject invalid or insufficient scope. No reading-performance oracle or authenticated user identity is established by this inspection.

The latest matching event wins, with explicit rescind precedence on ties. A latest rescind returns rescinded. Full-text declaration can cover a resolved anchor; abstract-only/toc-only cannot. The finalizer is instructed to recompute every pass, so changed declarations or anchors can demote prior ok markers. Writer internals are uninspected; the implementation conclusion covers resolution, not a guarantee that the command wrote the intended event.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Transient closed state and ok eligibility; no persisted audit receipt
- Later read-back: Retained ledger entries are read on each later finalizer pass; current resolution must not be replayed as an audit receipt
- Delegated visibility: Resolver receives exact citation key/anchor and current ledger; not the manuscript truth or reading behavior
- Selection predicate: Latest matching validated timestamped event; scope/locator coverage
- Invalidation or expiry: Rescission, anchor changes, invalid ledger or inadequate scope remove eligibility
- Activation or effect: Resolution can change marker authority on prescribed next pass; no observed demotion
- Evidence limits: Reading is declared, not independently measured; semantic claim checks remain separate

> if event_kind == "rescind":
>     return _result(
>         citation_key,
>         "rescinded",
>         "latest matching event rescinds the attestation",
>         marked_at=marked_at,
>     )
> --- `scripts/human_read_attestation_resolver.py`

#### EPI-RTE-screening-merge
Label: Screening decision merge

Part of: [RT-RTE-screening-fanout](runtime.md#rt-rte-screening-fanout)

Scoped A/B/ADJ/QC returns and overrides → merger → final decisions/pending lists → screening reports/corpus export. Owner: merger for fixed combination, models for candidate judgments, human override for priority. SRC-1, `sr-screener/scripts/merge_decisions.py`. Distinct material disposition within fan-out container. Target/domain: protocol-relative advance/exclude decisions, not full study validity. Fixed rules validate batch membership/decision shape, combine agreeing reviewers, use adjudication or liberal advance, and keep incomplete work pending. QC can advance a joint exclusion or flag it; it never changes human overrides. No known-answer oracle in this merge; pilot comparison is separate. Overrides and pre-QC/pre-override values preserve revision lineage. Exported corpus does not force manuscript inclusion, as the runtime's next-consumer evidence shows.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: decisions.json, pending/adjudication work and agreement/QC state
- Later read-back: Serialized decisions support later reporting and resumed work; full loader/revision invalidation was not independently audited
- Delegated visibility: Only allowed IDs and valid result labels survive into per-record decisions
- Selection predicate: A/B agreement, ADJ, liberal conflict policy, QC policy or human override
- Invalidation or expiry: Invalid/wrong-batch returns dropped; new overrides/QC can change operational outcome
- Activation or effect: Determines reporter-visible final eligibility and pending work
- Evidence limits: Direct title/abstract merge core only; no measured recall or full-text branch audit

> # QC rechecks: an exclusion the senior reviewer would advance is advanced (policy "advance") or flagged.
> # Human overrides are never changed by QC.
> --- `sr-screener/scripts/merge_decisions.py`

#### EPI-RTE-pilot-comparison
Label: Human-labelled pilot comparison

Part of: [RT-RTE-screening-fanout](runtime.md#rt-rte-screening-fanout)

Automatic pilot decisions and independent review-team label file → comparison → pilot_check.json → builder admission. Owner: comparison code for metrics, team for reference labels, builder for full-run admission. SRC-1, `sr-screener/scripts/merge_decisions.py`, `sr-screener/scripts/build_workflow.py`. Check is distinct from disposition by the builder and merger. Expected-answer reference is include/unclear versus exclude from team labels on the pilot, not general scientific truth. Human overrides are removed from the AI comparison where recorded, avoiding circular credit. Software computes missed advances and agreement; user can amend protocol/re-pilot or provide an override reason. It checks reason presence, not sincerity or competence. Guidance to amend after missed advances is a task-criteria adaptation opportunity, not demonstrated future learning; separate theory properties remain as qualified in runtime.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Pilot counts, missed advances, sensitivity or null, hashes and incomplete comparisons
- Later read-back: pilot_check.json is read before later full-run generation with current context and label-file hash
- Delegated visibility: Only labelled pilot IDs with automatic AI decisions enter comparison; missing AI decisions listed
- Selection predicate: Explicit --pilot-labels; builder checks nonempty comparison, missed advances and freshness
- Invalidation or expiry: Changed labels/context or missing decisions invalidates admission; override reason permits exceptional generation
- Activation or effect: Evidence influences builder admission and advises criterion amendment; neither adaptation nor benefit observed
- Evidence limits: Local oracle and current pilot only; not a causal recall estimate for unseen records

> "sensitivity": round(both / human_adv, 3) if human_adv else None,
> "missed_advances": missed, "extra_advances": extra, "agreement": srlib.agreement(rows)}
> --- `sr-screener/scripts/merge_decisions.py`

### Claims

#### EPI-CLM-integrity-boundary
Label: Integrity and verification boundary

SRC-1, `README.md` declares checks of manuscript/reported process and explicitly excludes empirical authenticity and reproduction. Doctrine/design, not measured ARS effectiveness. Distinct from [RT-CLM-complete-pipeline](runtime.md#rt-clm-complete-pipeline): this is the epistemic license of checks, not stage coverage.

> ARS does **not** establish that procedures were actually performed, raw data are authentic, or results reproduce; a consistently reported fabrication can pass these checks.
> --- `README.md`

#### EPI-CLM-synthesis-understanding
Label: Synthesis creates new understanding

SRC-1, `deep-research/agents/synthesis_agent.md` specifies a substantive synthesis role rather than sequential summary. Doctrine/design only. Distinct from [RT-CLM-complete-pipeline](runtime.md#rt-clm-complete-pipeline): the claim concerns the intellectual operation inside Phase 3. Its own pending-scholar and recall limits qualify interpretation.

> Synthesis means creating NEW understanding by connecting ideas across sources. It is NOT sequential summarization.
> --- `deep-research/agents/synthesis_agent.md`

> Generate new interpretive constructs
> --- `deep-research/agents/synthesis_agent.md`

#### EPI-CLM-review-calibration
Label: Live reviews not calibrated

SRC-1, `README.md` limits the reviewer product's calibration status. Doctrine/design, not a measurement reproduced here. No supplied claim counterpart after comparison: [RT-RTE-revision-review](runtime.md#rt-rte-revision-review) describes workflow authority and does not attest calibration.

> Current live reviews remain `NOT_CALIBRATED`; full calibration produces a bounded candidate profile, while live-profile application is not yet wired.
> --- `README.md`
