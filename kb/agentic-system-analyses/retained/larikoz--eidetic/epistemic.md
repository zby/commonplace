---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Eidetic epistemic routes: source-relative support, maintenance judgments, retention and later operational authority."
run-id: AAS-2026-10-14-eidetic-0e54f3c114b3-01
reviewed-boundary: "67506b62fdd0944c243537c3cb10938f7343b6b2"
---

# Eidetic epistemic report

## Source-and-claim boundary

The question is which Eidetic routes acquire or transform truth-apt content, what checks license reliance, and which later consumers receive the results. Scope and exclusions are as declared in [boundary](boundary.md#boundary-and-evidence); evidence identities are in its [Source register](boundary.md#source-register). All direct reads below are SRC-1 at the frozen commit. They establish implementation or doctrine/design, not observed execution. No target, tests or providers were run.

The public warrant claim assessed here is [EPI-CLM-truth-maintenance](#epi-clm-truth-maintenance). More narrowly, assembly visibility and base containment are [RT-CLM-feedback-visibility](runtime.md#rt-clm-feedback-visibility) and [RT-CLM-base-isolation](runtime.md#rt-clm-base-isolation). Neither is a claim of truth acceptance. The source's M3 anti-laundering claim is [EPI-CLM-support-gate](#epi-clm-support-gate).

### Coverage

“Supplied” means the runtime member, not an independently reread implementation. “Direct” denotes added source inspection, including checks for counterpaths. Available but uninspected routes remain limitations, not absences.

| Entry point or operation | Source path, SRC-1 | Coverage records / limitation |
| --- | --- | --- |
| SessionStart refresh and rules delivery | `install.sh`, `hooks/smart-memory-inject.sh`, `bin/assemble_context.py` | Supplied: [RT-RTE-context-injection](runtime.md#rt-rte-context-injection), [RT-BAP-memory-rules](runtime.md#rt-bap-memory-rules). Assembly internals not independently audited. |
| Stop extraction and compounding; direct personal/base writes | `hooks/session-signals.sh`, `bin/compound.py`, `bin/remember.py`, `bin/base.py` | Supplied: [RT-RTE-signal-compound](runtime.md#rt-rte-signal-compound), [RT-RTE-explicit-admission](runtime.md#rt-rte-explicit-admission). |
| MCP dispatch and base tool replacement | `mcp_server.py` | Direct: `handle_request`, personal HANDLERS and base replacement checked against [RT-RTE-memory-recall](runtime.md#rt-rte-memory-recall), [RT-RTE-explicit-admission](runtime.md#rt-rte-explicit-admission). Export adds [EPI-RTE-vault-generation](#epi-rte-vault-generation). Health/lint/serendipity internals not assessed; no system-complete negative about their advice. |
| Search ranking and confidence | `bin/search_impl.py`, `bin/confidence.py` | Direct ranking formula and full confidence fold; remaining retrieval implementation supplied by [RT-RTE-memory-recall](runtime.md#rt-rte-memory-recall). [EPI-RTE-confidence-ranking](#epi-rte-confidence-ranking). |
| Pending-ingest M1/M2 | `bin/m1_contradiction.py`, `bin/m2_synthesis.py`, `bin/index_impl.py` | Direct confirmer, disposition, synthesis construction, region commit and supersession checks; dispatcher supplied by [RT-RTE-semantic-maintenance](runtime.md#rt-rte-semantic-maintenance). [EPI-RTE-m2-reshaping](#epi-rte-m2-reshaping). Opposition lexicon and callback alternatives not exhaustively assessed. |
| M3 recall support, filing, affirmation | `bin/m3_autofile.py`, `bin/m3_judge.py`, `bin/lifecycle_signals.py` | Direct support scorer, judge registration/verdict, affirmation consumer/producer and Bash-event capture. [EPI-RTE-support-check](#epi-rte-support-check), [EPI-RTE-test-affirmation](#epi-rte-test-affirmation); driver/miner supplied by [RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing). |
| Acquisition/agent dark lane | `bin/m3_acquisition.py` | Direct quote/judge/outcome path: [EPI-RTE-acquisition-check](#epi-rte-acquisition-check). Child-transcript transport/cache implementation supplied only at runtime's stated scope. |
| Cleanup wrapper and CLI modes | `bin/cleanup.sh`, `bin/cleanup.py` | Direct wrapper search and candidate/archive/event-cleanup code: [EPI-RTE-cleanup-archive](#epi-rte-cleanup-archive). |
| Usage-based curation CLI | `bin/curate.py` | Direct candidate, status writer and main dispatch: [EPI-RTE-curate-archive](#epi-rte-curate-archive). Upstream telemetry computation not fully inspected. |
| Export polish and optional topic synthesis | `bin/export_vault.py`, `bin/export-vault.sh` | Direct generation and write seams; shell flags located by search. [EPI-RTE-vault-generation](#epi-rte-vault-generation). Discovery/gating, cluster generation and deterministic template conversion not exhaustively assessed. |
| Logical-index worker and source update | `bin/eidetic_engine_worker.py`, `bin/engine.py`, `bin/update.sh` | Supplied: [RT-RTE-engine-worker](runtime.md#rt-rte-engine-worker), [RT-RTE-product-update](runtime.md#rt-rte-product-update). |
| Recall evaluations | `bin/recall_smoke.py`, `bin/recall_lab.py`, `bin/canary.py` | Direct smoke decision function and main/exit consumer; [EPI-RTE-smoke-evaluation](#epi-rte-smoke-evaluation). Lab/canary functions located, not fully traced. No measured calibration, recall benefit or causal attribution. |
| Replay, dark reports, commissioning, drift/lint and resource tooling | `bin/m3_post_entailment_replay.py`, `bin/m3_legacy_replay.py`, `bin/m3_dark_report.py`, `bin/m3_commission.py`, `bin/drift_check.py`, `bin/lint_impl.py`, `bin/resource_budget.py` | Located/inventoried, not assessed in detail. Prevents exhaustive evaluator coverage and a system-wide absence claim about criticism, evaluation or policy adaptation. |

Missing deployment flags and host traces prevent activation/compliance findings. Missing corpus, actual proposed claims and provider outputs prevent deciding semantic preservation or non-entailment for individual generated candidates. Missing original evidence prevents validating imported source truth. Missing evaluator results and controlled interventions prevent performance, calibration, learning or component-effect claims. Opaque provider/model state is bounded as in [RT-CMP-session-extractor](runtime.md#rt-cmp-session-extractor), [RT-CMP-embed](runtime.md#rt-cmp-embed), [RT-CMP-rerank](runtime.md#rt-cmp-rerank), [RT-CMP-shimnachi-local](runtime.md#rt-cmp-shimnachi-local) and [RT-CMP-query-translation](runtime.md#rt-cmp-query-translation). No inference about training or immutable weights follows from named routes.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-signal-cards](#epi-obj-signal-cards) | Session decisions, project facts and failure descriptions; directives are not themselves truth claims | see record | SRC-1 `hooks/session-signals.sh` | No actual extraction supplied; directive and descriptive content can coexist. |
| [EPI-OBJ-recall-provenance](#epi-obj-recall-provenance) | Recalled answer propositions and cited card spans | see record | SRC-1 `bin/m3_autofile.py` | Sources constrain support, not original truth. |
| [EPI-OBJ-synthesis-region](#epi-obj-synthesis-region) | Bounded copied salient lines from related cards | see record | SRC-1 `bin/m2_synthesis.py` | Lossy line selection can omit conditions; callback output is opaque. |
| [EPI-OBJ-confidence-events](#epi-obj-confidence-events) | Symbolic assertions of verification, confirmation or contradiction; numerical fold is not proposition truth | see record | SRC-1 `bin/confidence.py` | Event type records a contract, not independently authenticated evidence. |
| [RT-OBJ-memory-context](runtime.md#rt-obj-memory-context) | Selected facts plus behavioral directives | see record | SRC-1 `bin/assemble_context.py` | Budgeted names/snippets are not complete claims. |
| [EPI-OBJ-vault-pages](#epi-obj-vault-pages) | Model-rewritten note bodies and generated topic articles | see record | SRC-1 `bin/export_vault.py` | Actual generated propositions not available. |

## Authority-route ledger

Fields owned by canonical records are referenced rather than copied. These are function-level overlays: repeated route citations distinguish checking, disposition and retention within the same implementation.

Route ID: [RT-RTE-signal-compound](runtime.md#rt-rte-signal-compound)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-signal-cards](#epi-obj-signal-cards).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: transcript descriptive content to proposed signals; directives are a separate non-truth-apt policy/content update.
Evaluator/condition and domain: model extraction request, then prefix/candidate rules; no factual answer oracle.
Activation and timing: see record.
Possible or observed result: see record; no observed output.
Implemented force: formatting/candidate rules enforce write eligibility, not fidelity.
Epistemic authority and scope: retained candidate; external transcript's warrant unknown after model extraction.
Operational authority: behavior permitted, blocked, or changed: proposed signal can become later context without evidence-consuming factual acceptance.
Behavioral-authority path: consumer, channel, force, horizon: later host/recall caller, cards via index and rules, advisory/directive, later sessions; see [RT-BAP-memory-rules](runtime.md#rt-bap-memory-rules).
Evidence source ID and local anchor: SRC-1 `hooks/session-signals.sh`; see route record.
Claim IDs or none: [EPI-CLM-truth-maintenance](#epi-clm-truth-maintenance).
Mismatch marker or none: storage is not truth acceptance.
Gap/limit: no individual transformation can be classified as non-ampliative or conjectural without content evidence.

Route ID: [RT-RTE-explicit-admission](runtime.md#rt-rte-explicit-admission)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-signal-cards](#epi-obj-signal-cards); caller-supplied base text is distinct imported content.
Content/update relation: truth-apt transformation: acquisition/import.
Transition or check target: caller text to durable card/base file; source warrant unknown.
Evaluator/condition and domain: nonempty/content/kind/path checks, not truth assessment; approval policy versus enforcement see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: enforcing local write selection.
Epistemic authority and scope: no new source warrant established.
Operational authority: behavior permitted, blocked, or changed: persisted content becomes eligible for personal injection or attached-base search.
Behavioral-authority path: consumer, channel, force, horizon: personal host rules or base MCP caller, text delivery, advisory/directive, later sessions.
Evidence source ID and local anchor: SRC-1 `bin/remember.py`, `bin/base.py`, `mcp_server.py`; see record.
Claim IDs or none: [RT-CLM-base-isolation](runtime.md#rt-clm-base-isolation).
Mismatch marker or none: isolation and explicit-user instructions are not content validation.
Gap/limit: caller approval and source authenticity unresolved.

Route ID: [EPI-RTE-support-check](#epi-rte-support-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-recall-provenance](#epi-obj-recall-provenance).
Content/update relation: no content change.
Transition or check target: material answer claims relative to supplied source spans, not facts relative to the world.
Evaluator/condition and domain: deterministic token overlap/vetoes, or registered model verdict with a default-on, configurable quote gate; see record. With EIDETIC_M3_JUDGE_REQUIRE_QUOTE set to 0, false or empty, a positive model verdict needs no matching quotation.
Activation and timing: see record.
Possible or observed result: support score/entailed/not_entailed/error; no observed result.
Implemented force: score feeds filing disposition.
Epistemic authority and scope: heuristic textual support; even valid entailment would only inherit source warrant.
Operational authority: behavior permitted, blocked, or changed: checker alone supplies a decision input, not a write.
Behavioral-authority path: consumer, channel, force, horizon: filing gate, support function result, permissive/enforcing at next gate, current candidate.
Evidence source ID and local anchor: SRC-1 `bin/m3_autofile.py`, `bin/m3_judge.py`.
Claim IDs or none: [EPI-CLM-support-gate](#epi-clm-support-gate).
Mismatch marker or none: overlap is not general entailment.
Gap/limit: unregistered and registered routes have different domains; a registered judge's later failure rejects rather than reverting to overlap.

Route ID: [RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-recall-provenance](#epi-obj-recall-provenance).
Content/update relation: no content change.
Transition or check target: eligibility to file a recall answer or hand it to M2.
Evaluator/condition and domain: nonempty sources and every material score strictly above floor before dedup routing; see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: enforcing source-relative support protocol for this route only.
Epistemic authority and scope: an evidence-consuming filing decision against a named support criterion, intended for recalled personal-memory content. This is not acceptance of an independently warranted ampliative claim.
Operational authority: behavior permitted, blocked, or changed: permits filing or M2 handoff, blocks unsupported candidates.
Behavioral-authority path: consumer, channel, force, horizon: writer/M2, result branch, enforcing, this candidate.
Evidence source ID and local anchor: SRC-1 `bin/m3_autofile.py`; see record.
Claim IDs or none: [EPI-CLM-support-gate](#epi-clm-support-gate).
Mismatch marker or none: separate direct-write routes bypass this protocol by design.
Gap/limit: provenance spans may themselves be wrong; outcome not observed.

Route ID: [RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-recall-provenance](#epi-obj-recall-provenance).
Content/update relation: truth-apt transformation: acquisition/import.
Transition or check target: supported recall answer plus source spans and scores to new personal page.
Evaluator/condition and domain: see record; initial confidence 0.40 is a mark, not a read exclusion threshold.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: durable write, enabling later indexing.
Epistemic authority and scope: preserves a local source-support trail; original source warrant remains unknown.
Operational authority: behavior permitted, blocked, or changed: new card becomes available for recall/injection.
Behavioral-authority path: consumer, channel, force, horizon: later memory readers, indexed card text, advisory/directive according to content, later sessions.
Evidence source ID and local anchor: SRC-1 `bin/m3_autofile.py`; see record.
Claim IDs or none: [EPI-CLM-support-gate](#epi-clm-support-gate).
Mismatch marker or none: filing does not mint verified_by_test or confirmed.
Gap/limit: acquisition here is of the caller answer; its earlier semantic generation is not established by the write.

Route ID: [EPI-RTE-acquisition-check](#epi-rte-acquisition-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: candidate claim and assistant quote described in record.
Content/update relation: no content change.
Transition or check target: claim support by a quote that occurs in the mined assistant turns.
Evaluator/condition and domain: normalized quote occurrence, durability rejection, then model verdict; see record.
Activation and timing: see record.
Possible or observed result: would_file/would_reject/transient outcomes, not actual card filing.
Implemented force: logs and seen-cache/retry input only.
Epistemic authority and scope: assistant utterance provenance plus judged support, not real-world verification.
Operational authority: behavior permitted, blocked, or changed: changes retry eligibility, not knowledge-card admission.
Behavioral-authority path: consumer, channel, force, horizon: driver/cache, outcome string, enforcing retry selection, later Stop invocations.
Evidence source ID and local anchor: SRC-1 `bin/m3_acquisition.py`.
Claim IDs or none: none.
Mismatch marker or none: would_file does not mean filed.
Gap/limit: no observed activation or downstream semantic use.

Route ID: [RT-RTE-semantic-maintenance](runtime.md#rt-rte-semantic-maintenance)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: retained card propositions; [EPI-OBJ-confidence-events](#epi-obj-confidence-events).
Content/update relation: no content change.
Transition or check target: M1 pair conflict; M2 relevance and temporal supersession, each in same-project selected pairs.
Evaluator/condition and domain: M1 deterministic opposition over shared frame with optional topic corroboration; M2 reranker relevance and version/year/plan-to-shipped heuristic. Callback alternatives possible.
Activation and timing: see record.
Possible or observed result: conflict/no conflict/uncertain; relevance score; supersession proposal. Direct source detail in [EPI-RTE-m2-reshaping](#epi-rte-m2-reshaping).
Implemented force: results feed separate event/edit branches.
Epistemic authority and scope: judgments about selected text pairs; no proof that one claim is factually correct.
Operational authority: behavior permitted, blocked, or changed: supplies eligibility and candidate loser/target, not itself a content write.
Behavioral-authority path: consumer, channel, force, horizon: maintenance disposition branches, verdicts/scores, permissive, current ingest.
Evidence source ID and local anchor: SRC-1 `bin/m1_contradiction.py`, `bin/m2_synthesis.py`.
Claim IDs or none: [EPI-CLM-truth-maintenance](#epi-clm-truth-maintenance).
Mismatch marker or none: no_contradiction can mean no detected opposition, not demonstrated compatibility.
Gap/limit: heuristic domain and configurable callbacks prevent a general semantic warrant.

Route ID: [RT-RTE-semantic-maintenance](runtime.md#rt-rte-semantic-maintenance)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-confidence-events](#epi-obj-confidence-events).
Content/update relation: non-truth-apt policy/content update: authority and ranking metadata changes.
Transition or check target: conflict demotion or supersession eligibility.
Evaluator/condition and domain: M1 loser authority/high-water mark, event and M1 switches; M2 autosupersede switch, strict relevance and dominating authority; see evidence in [EPI-RTE-m2-reshaping](#epi-rte-m2-reshaping).
Activation and timing: see record.
Possible or observed result: diagnostic/relation_claim/event; supersession suggestion or metadata plus terminal event.
Implemented force: gated event/metadata mutation; suggestions do not enforce retirement.
Epistemic authority and scope: operational preference constrained by declared authority, not a criterion deciding world truth.
Operational authority: behavior permitted, blocked, or changed: confidence/status ranking demotion, while underlying text can remain retrievable.
Behavioral-authority path: consumer, channel, force, horizon: index then search/context, Evidence/frontmatter to weights, ranking, later reads; [EPI-RTE-confidence-ranking](#epi-rte-confidence-ranking).
Evidence source ID and local anchor: SRC-1 `bin/m1_contradiction.py`, `bin/m2_synthesis.py`.
Claim IDs or none: [EPI-CLM-truth-maintenance](#epi-clm-truth-maintenance).
Mismatch marker or none: demotion or supersession is not factual rejection across all consumers.
Gap/limit: flags unknown; relation_claim can intentionally carry no ranking penalty.

Route ID: [EPI-RTE-m2-reshaping](#epi-rte-m2-reshaping)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-synthesis-region](#epi-obj-synthesis-region).
Content/update relation: truth-apt transformation: non-ampliative reshaping.
Transition or check target: default writer selects, cleans, deduplicates and sorts source one-liners into linked rows.
Evaluator/condition and domain: see record; source-relative gates do not evaluate a new explanatory theory.
Activation and timing: see record.
Possible or observed result: deterministic bounded consolidation body; optional callback is separately indeterminate.
Implemented force: managed-region write, plus at most one observed event per operation.
Epistemic authority and scope: source attribution, not newly established truth; first-line/truncation loss can degrade source scope.
Operational authority: behavior permitted, blocked, or changed: linked summary becomes indexed content.
Behavioral-authority path: consumer, channel, force, horizon: later search/context reader, managed region, advisory, later sessions.
Evidence source ID and local anchor: SRC-1 `bin/m2_synthesis.py`.
Claim IDs or none: none.
Mismatch marker or none: synthesis label does not establish ampliative production or lifecycle integration after factual acceptance.
Gap/limit: optional synth_body_fn requires output evidence to classify; no actual edit observed.

Route ID: [EPI-RTE-test-affirmation](#epi-rte-test-affirmation)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-confidence-events](#epi-obj-confidence-events).
Content/update relation: non-truth-apt policy/content update: confidence promotion event.
Transition or check target: filed page in same session/project as passing test-class command, not page-specific truth.
Evaluator/condition and domain: hook event classifier and project/session correlation; affirmation consumer also trusts typed user_affirmation; see record.
Activation and timing: see record.
Possible or observed result: verified_by_test or confirmed event, or guard rejection/no write.
Implemented force: gated Evidence append.
Epistemic authority and scope: test correlation is expressly a ranking signal; no claim-level test coverage or mechanism attribution.
Operational authority: behavior permitted, blocked, or changed: raises managed confidence when later folded.
Behavioral-authority path: consumer, channel, force, horizon: index fold then ranking consumers, event row, ranking, later reads; [EPI-RTE-confidence-ranking](#epi-rte-confidence-ranking).
Evidence source ID and local anchor: SRC-1 `bin/m3_autofile.py`, `bin/lifecycle_signals.py`.
Claim IDs or none: [EPI-CLM-support-gate](#epi-clm-support-gate).
Mismatch marker or none: verified_by_test label exceeds what project-level correlation can establish about an individual claim.
Gap/limit: event delivery authenticity is a host/producer contract; no test trace supplied.

Route ID: [EPI-RTE-confidence-ranking](#epi-rte-confidence-ranking)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-confidence-events](#epi-obj-confidence-events).
Content/update relation: no content change.
Transition or check target: ordered event records to numerical confidence and ranking weight.
Evaluator/condition and domain: pure arithmetic and authority-tier gate; not a truth evaluator.
Activation and timing: see record.
Possible or observed result: bounded confidence, relation_claim flags, weighted search score.
Implemented force: ranking when configured, not hard read exclusion.
Epistemic authority and scope: no calibrated truth probability established.
Operational authority: behavior permitted, blocked, or changed: relative prominence changes.
Behavioral-authority path: consumer, channel, force, horizon: search/context selector, indexed numbers, ranking, later queries/sessions.
Evidence source ID and local anchor: SRC-1 `bin/confidence.py`, `bin/search_impl.py`.
Claim IDs or none: [EPI-CLM-truth-maintenance](#epi-clm-truth-maintenance).
Mismatch marker or none: confidence mark is distinct from retrieval-confidence annotation and truth acceptance.
Gap/limit: actual flags and index contents unknown.

Route ID: [RT-RTE-memory-recall](runtime.md#rt-rte-memory-recall)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: retained card text and detail pointers; see record.
Content/update relation: truth-apt transformation: non-ampliative reshaping.
Transition or check target: query to ranked snippets and optional full detail.
Evaluator/condition and domain: relevance and corroboration heuristics; confidence annotation is not truth verification.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: ranking plus advisory weak-result policy.
Epistemic authority and scope: candidate relevance, with lifecycle warnings, not a new source endorsement.
Operational authority: behavior permitted, blocked, or changed: consuming agent can inspect/use or ignore; weak candidates remain accessible.
Behavioral-authority path: consumer, channel, force, horizon: caller model, skill/MCP result text, advisory, current task and later recalls.
Evidence source ID and local anchor: SRC-1 `bin/search_impl.py`, `skill/SKILL.md`; see record.
Claim IDs or none: [EPI-CLM-truth-maintenance](#epi-clm-truth-maintenance).
Mismatch marker or none: optional query translation has indeterminate semantic fidelity, not proven non-ampliative transformation.
Gap/limit: no retrieval outcome or compliance evidence.

Route ID: [RT-RTE-context-injection](runtime.md#rt-rte-context-injection)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-memory-context](runtime.md#rt-obj-memory-context).
Content/update relation: truth-apt transformation: non-ampliative reshaping.
Transition or check target: indexed retained text to budgeted rules/snippets/names.
Evaluator/condition and domain: assembly SQL/budget policy, not factual acceptance.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: local delivery artifact, natural-language instruction downstream.
Epistemic authority and scope: retained material selected for visibility, not validated anew.
Operational authority: behavior permitted, blocked, or changed: host may load feedback under ALWAYS APPLY.
Behavioral-authority path: consumer, channel, force, horizon: see [RT-BAP-memory-rules](runtime.md#rt-bap-memory-rules).
Evidence source ID and local anchor: SRC-1 `bin/assemble_context.py`; see record.
Claim IDs or none: [RT-CLM-feedback-visibility](runtime.md#rt-clm-feedback-visibility).
Mismatch marker or none: name-only visibility does not deliver every rule's semantics.
Gap/limit: failed refresh/assembly and host loading prevent unconditional delivery/compliance conclusions.

Route ID: [EPI-RTE-cleanup-archive](#epi-rte-cleanup-archive)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: retained nonprotected Markdown cards.
Content/update relation: no content change.
Transition or check target: storage-maintenance eligibility, not proposition falsity.
Evaluator/condition and domain: age/orphan/size score; see record.
Activation and timing: see record.
Possible or observed result: report or file relocation; separate age-based lifecycle-log deletion.
Implemented force: advisory report or enforcing filesystem move/delete.
Epistemic authority and scope: no factual withdrawal licensed.
Operational authority: behavior permitted, blocked, or changed: moves cards outside ordinary source locations; existing index requires refresh.
Behavioral-authority path: consumer, channel, force, horizon: filesystem/index collector, paths, enforcing availability after refresh, future reads.
Evidence source ID and local anchor: SRC-1 `bin/cleanup.py`.
Claim IDs or none: none.
Mismatch marker or none: archival differs from semantic rejection and immediate index removal.
Gap/limit: caller must reindex; no automatic rollback or actual archive observed.

Route ID: [EPI-RTE-curate-archive](#epi-rte-curate-archive)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: retained nonprotected cards and frontmatter status.
Content/update relation: non-truth-apt policy/content update: archived status.
Transition or check target: age_stale plus never-pulled maintenance candidates.
Evaluator/condition and domain: telemetry/drift selectors and explicit CLI switches; see record.
Activation and timing: see record.
Possible or observed result: advisory promotion/archive list or status write.
Implemented force: advisory by default; --apply --yes enforces status mutation.
Epistemic authority and scope: low-use/stale heuristic, not factual rejection.
Operational authority: behavior permitted, blocked, or changed: later ranking demotion while card remains searchable.
Behavioral-authority path: consumer, channel, force, horizon: index/search, frontmatter status, ranking, later queries.
Evidence source ID and local anchor: SRC-1 `bin/curate.py`, `bin/search_impl.py`.
Claim IDs or none: none.
Mismatch marker or none: archive here is metadata, not cleanup's move.
Gap/limit: usage upstream not fully assessed; no observed write.

Route ID: [EPI-RTE-vault-generation](#epi-rte-vault-generation)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-vault-pages](#epi-obj-vault-pages).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: exported note bodies to polished bodies; selected notes to topic article.
Evaluator/condition and domain: fact-preserving prompts plus subprocess success/output-length gates, not entailment checks.
Activation and timing: see record.
Possible or observed result: generated page bodies persisted to vault; none observed.
Implemented force: write eligibility and atomic file replacement; no semantic acceptance gate inspected at these seams.
Epistemic authority and scope: requested preservation, not established preservation or new warrant.
Operational authority: behavior permitted, blocked, or changed: human-readable rewritten/combined articles made available.
Behavioral-authority path: consumer, channel, force, horizon: vault reader, Markdown pages/MOC, advisory, subsequent browsing. No automatic return to authoritative personal store established here.
Evidence source ID and local anchor: SRC-1 `bin/export_vault.py`.
Claim IDs or none: none.
Mismatch marker or none: polished:true and source links do not prove factual fidelity.
Gap/limit: generation output/provider internals absent; cannot establish a particular novel proposition or ampliative acceptance.

Route ID: [EPI-RTE-smoke-evaluation](#epi-rte-smoke-evaluation)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: retrieval payloads compared with authored cases, not a knowledge-card object.
Content/update relation: no content change.
Transition or check target: expected retrieval item and confidence, or no confident negative result.
Evaluator/condition and domain: deterministic authored-substring and confidence comparisons; see record.
Activation and timing: manual evaluator invocation; positive code cases skip if code index is absent.
Possible or observed result: PASS/FAIL/SKIP and exit status, not supplied outcomes.
Implemented force: test process reporting/failure status, not runtime filing veto.
Epistemic authority and scope: passing a case licenses that case's retrieval predicate only.
Operational authority: behavior permitted, blocked, or changed: evaluator main increments failure count and exits nonzero; no inspected consumer changes stored claim authority.
Behavioral-authority path: consumer, channel, force, horizon: operator or calling process, stdout/exit status, advisory/process failure, evaluator invocation.
Evidence source ID and local anchor: SRC-1 `bin/recall_smoke.py`.
Claim IDs or none: none.
Mismatch marker or none: retrieval expectations do not test all returned propositions or explain task success.
Gap/limit: no actual result, wider harness consumer or causal comparison supplied.

The worker's hash/stamp checks and update ancestry check remain separate non-truth-apt identity/compatibility/admission routes: see [RT-RTE-engine-worker](runtime.md#rt-rte-engine-worker) and [RT-RTE-product-update](runtime.md#rt-rte-product-update). They preserve operational lineage but do not validate source propositions or demonstrate self-improvement. No lifecycle-integration row is established merely from retaining or linking content. The M3 decision licenses source-relative filing; the M2 links do not establish subsequent integration of a factually accepted new theory.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-truth-maintenance](#epi-clm-truth-maintenance) | see record | SRC-1 `README.md`, doctrine/design | see record | [RT-RTE-memory-recall](runtime.md#rt-rte-memory-recall), [RT-RTE-semantic-maintenance](runtime.md#rt-rte-semantic-maintenance), [EPI-RTE-confidence-ranking](#epi-rte-confidence-ranking) | Not supplied | Ranking and selected maintenance are implemented; no agent-quality comparison | Staleness/authority metadata can change prominence; gated semantic-pair heuristics exist | Does not establish knowing world truth, reliable silent-rename detection, or preventing poorer agent performance |
| [EPI-CLM-support-gate](#epi-clm-support-gate) | see record | SRC-1 `bin/m3_autofile.py`, doctrine/design and implementation | see record | [EPI-RTE-support-check](#epi-rte-support-check), [RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing), [EPI-RTE-test-affirmation](#epi-rte-test-affirmation) | Not supplied | No gate-quality or causal experiment; route-specific and configurable | Source-relative admission runs before duplicate routing; filing alone does not mint promotion | Default overlap is not general entailment; registered quote gating is default-on but configurable off; sources can be false; later test promotion is project correlation |
| [RT-CLM-feedback-visibility](runtime.md#rt-clm-feedback-visibility) | see record | SRC-1 `bin/assemble_context.py`, implementation | see record | [RT-RTE-context-injection](runtime.md#rt-rte-context-injection) | Not supplied | Visibility invariant within successful assembly only | see record | Name/cluster visibility is not complete semantic delivery or compliance |
| [RT-CLM-base-isolation](runtime.md#rt-clm-base-isolation) | see record | SRC-1 `bin/index_impl.py`, implementation | see record | [RT-RTE-explicit-admission](runtime.md#rt-rte-explicit-admission) | Not supplied | Scanner containment, not OS isolation or approval authentication | see record | No implication of content correctness |

## Bounded conclusion

Eidetic acquires caller text and model-extracted session candidates, retains them as cards, and delivers selected content through personal rules or requested recall. Source warrant is generally unknown; prefix validation, source metadata, freshness and relevance do not confer factual acceptance. Personal feedback can have strong natural-language behavioral force without a claim-level truth check. Delivery is wired; changed host behavior is unobserved. See [RT-RTE-signal-compound](runtime.md#rt-rte-signal-compound), [RT-RTE-explicit-admission](runtime.md#rt-rte-explicit-admission), [RT-BAP-memory-rules](runtime.md#rt-bap-memory-rules).

M3 has a real, route-local, evidence-consuming support disposition before filing or duplicate handoff. Its intended use is source-supported personal recall, its criterion is every material claim passing the configured support floor, and its immediate authority is permission to route/write. The default evaluator is lexical, not general entailment; registered model judgment adds a different support check, with a quote-origin constraint only when the default-on EIDETIC_M3_JUDGE_REQUIRE_QUOTE gate is enabled. The raw-verdict configuration accepts positive model judgment without requiring quote occurrence. Neither path establishes original source truth. No supplied candidate proves accepted ampliative production. The acquisition lane separately requires quote occurrence in assistant turns before judgment, regardless of the judge's quote-gate configuration, but logs would_file rather than admitting a card. See [EPI-RTE-support-check](#epi-rte-support-check), [RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing), [EPI-RTE-acquisition-check](#epi-rte-acquisition-check).

Default M2 synthesis demonstrably reshapes selected source lines rather than generating a new explanatory proposition. Its region edit adds at most a bounded observed event; optional synthesis callbacks remain semantically indeterminate. M1 conflict and M2 supersession can change reliance through diagnostics, events and ranking metadata. Their heuristic checks, authority protection and opt-in demotion are separate functions; no_contradiction is not an acceptance of compatibility. These linked, retained maintenance decisions support a route-level criticism/revision mechanism, not a complete demonstrated theory-builder cycle. See [EPI-RTE-m2-reshaping](#epi-rte-m2-reshaping), [RT-RTE-semantic-maintenance](runtime.md#rt-rte-semantic-maintenance).

Test affirmation is a consequential counterexample to equating verification labels with claim tests: a passing test-class event in the same session/project can raise confidence on a filed page without testing that page's proposition. Numerical confidence then influences ranking only when enabled. Neither event arithmetic nor retrieval confidence is an established truth probability. Cleanup and curation withdraw location or prominence by age/usage/size criteria, not semantic falsification. See [EPI-RTE-test-affirmation](#epi-rte-test-affirmation), [EPI-RTE-confidence-ranking](#epi-rte-confidence-ranking), [EPI-RTE-cleanup-archive](#epi-rte-cleanup-archive), [EPI-RTE-curate-archive](#epi-rte-curate-archive).

Export adds another generated-content route outside the supplied runtime's detail: fact-preserving prompts feed rewritten notes and optional topic articles, with process/length checks at the write seams rather than source-entailment acceptance. No individual output establishes non-entailment, so ampliative conjecture is not asserted. See [EPI-RTE-vault-generation](#epi-rte-vault-generation).

The smoke evaluator's named target is retrieval of authored expected substrings at minimum confidence, or absence of confident negative results. It licenses a bounded test decision, not correctness of every retrieved fact, agent task success, component causation or runtime admission. Its decision and exit-status consumer were inspected directly; see [EPI-RTE-smoke-evaluation](#epi-rte-smoke-evaluation). No results were supplied. Other evaluator and replay families remain explicitly unassessed. Parameter adaptation is not evidenced by these inspected call sites, while provider internals remain opaque. Trace-fed persistence, maintenance criticism, learning as improved capacity, reflection, autonomy and self-improvement are independent: the first two have implemented paths here, but the latter conclusions cannot be inferred from filing, event promotion, linking or product installation. No single system-wide epistemic verdict follows.

## Shared records

### Components

#### EPI-CMP-vault-models
Label: Vault polish and topic model routes

Source-native identities: POLISH_MODEL_SONNET, POLISH_MODEL_HAIKU, TOPIC_CLUSTER_MODEL and TOPIC_SYNTHESIS_MODEL in SRC-1 `bin/export_vault.py`. Distributed-parametric weights are outside the checkout; model request/response text is local natural language. Defaults include claude-sonnet-5-5, claude-haiku-4-5-20251001 and claude-opus-4-6. Parameters changing during operation: no training request in these adapters; provider internals uninspected. Exact version pinned: model labels, not immutable weights. Mutable endpoint can resolve another model: environment overrides and external claude-batch/provider routing permit uncertainty. Distinct from [RT-CMP-session-extractor](runtime.md#rt-cmp-session-extractor): different call sites, tasks and output consumers, not an assertion of different underlying weights.

> TOPIC_CLUSTER_MODEL = os.environ.get("EIDETIC_TOPIC_CLUSTER_MODEL", POLISH_MODEL_SONNET)
> TOPIC_SYNTHESIS_MODEL = os.environ.get("EIDETIC_TOPIC_SYNTHESIS_MODEL", "claude-opus-4-6")
> --- `bin/export_vault.py`

### Operative objects

#### EPI-OBJ-signal-cards
Label: Personal signal and promoted cards

Natural-language descriptions, rules and History/Update sections persisted as Markdown. Type/source/evidence metadata are symbolic selectors. Source-native identities are the durable cards written by [RT-RTE-signal-compound](runtime.md#rt-rte-signal-compound) and [RT-RTE-explicit-admission](runtime.md#rt-rte-explicit-admission); no supplied operative-object counterpart after comparison. Distinct from generated [RT-OBJ-memory-context](runtime.md#rt-obj-memory-context), which is a selected derivative, not the authoritative card. SRC-1 `bin/compound.py`, `bin/remember.py`; minimum write/protection evidence is in those runtime records. No supplied actual card proves a route operated.

#### EPI-OBJ-recall-provenance
Label: Recalled answer provenance

Source-native provenance object and generated Provenance block contain natural-language answer claims, source spans, query/session identifiers and symbolic per-claim scores. In-process object then Markdown block; source IDs/spans give local lineage, not original source truth. No supplied object counterpart after comparison; this is a material input/output part of [RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing), distinct from the general rules artifact. SRC-1 `bin/m3_autofile.py`.

> lines.append("Claim support (deterministic span-overlap):")
> --- `bin/m3_autofile.py`

#### EPI-OBJ-synthesis-region
Label: M2 managed synthesis region

Source-native synthesis_region_id and bounded region contain natural-language salient lines plus symbolic delimiters/wikilinks, stored within target Markdown. Region body changes have their own operation marker and event-repair path. No supplied operative-object counterpart after comparison; the containing implementation is [RT-RTE-semantic-maintenance](runtime.md#rt-rte-semantic-maintenance), not a separately declared source-card object. SRC-1 `bin/m2_synthesis.py`; evidence in [EPI-RTE-m2-reshaping](#epi-rte-m2-reshaping).

#### EPI-OBJ-confidence-events
Label: Evidence events and confidence fold

Source-native Evidence event rows persisted in cards, parsed/materialized by indexing; event_type, actor_tier, session identity and deltas have fixed symbolic consumers. Confidence is a scalar computed from chronological events, not a distributed-parametric model. Distinct from [RT-OBJ-memory-context](runtime.md#rt-obj-memory-context), which may contain content selected using these values; no supplied operative-object counterpart. SRC-1 `bin/confidence.py`; evidence in [EPI-RTE-confidence-ranking](#epi-rte-confidence-ranking) and [EPI-RTE-test-affirmation](#epi-rte-test-affirmation).

#### EPI-OBJ-vault-pages
Label: Polished and synthesized vault pages

Source-native exported notes and topics/*.md are natural-language Markdown on filesystem storage, with symbolic frontmatter and links. Distinct from [RT-OBJ-memory-context](runtime.md#rt-obj-memory-context): generated for vault readers, not the host rules loader. No supplied object counterpart. SRC-1 `bin/export_vault.py`; generation and persistence evidence in [EPI-RTE-vault-generation](#epi-rte-vault-generation).

### Routes

#### EPI-RTE-support-check
Label: M3 claim support scoring
Part of: [RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing)

This part isolates the evaluator from the parent's disposition and retention. SRC-1 `bin/m3_autofile.py` implements _overlap_support and active_support; `bin/m3_judge.py` implements registration, quote checks and binary score. Code owns scorer selection; optional model supplies a verdict. Human role is configuration, not per-candidate approval. Answer oracle: source spans are a reference corpus for support, not known-correct world answers. Operating mode: bounded recall-answer checking. A registered judge's subsequent route error maps to score zero; registration failure leaves deterministic overlap. The registered judge defaults to requiring both a positive model verdict and a matching quote. EIDETIC_M3_JUDGE_REQUIRE_QUOTE set to 0, false or empty disables that requirement: positive model judgment then suffices without quote occurrence. Local quote checks require a literal quotation within one span; external checks use normalized tokens against redacted spans. A quote occurring in source proves occurrence only, not that the quote entails the claim. The verdict docstring's unconditional quote-gate description is narrower than the executable raw-verdict path.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: overlap float or registered judge score 1.0/0.0.
- Later read-back: per-claim scores/source spans can be retained in a filed Provenance block and later read as card content.
- Delegated visibility: judge receives claim and spans; external route redacts both before judgment and any enabled quote gate.
- Selection predicate: material claims selected by filing gate; active registered scorer or default overlap. Registered score requires positive model judgment and, only when _REQUIRE_QUOTE is enabled (default), a passing quote gate.
- Invalidation or expiry: ephemeral score recomputed per call; retained scores have no truth-expiry check here.
- Activation or effect: score feeds parent rejection/routing; no observed judgment.
- Evidence limits: token overlap with negation/entity/curated-antonym vetoes is not general entailment; model accuracy and source truth unavailable.

> if not claim_salient.issubset(pool):   # a salient token in NO cited span ⇒ fail
>         return 0.0
> --- `bin/m3_autofile.py`

> covered = sum(1 for t in claim_tokens if t in span_set)
>         best = max(best, covered / len(claim_tokens))
>     return best
> --- `bin/m3_autofile.py`

> _REQUIRE_QUOTE = os.environ.get("EIDETIC_M3_JUDGE_REQUIRE_QUOTE", "1").strip() not in ("0", "false", "")
> --- `bin/m3_judge.py`

> filed = bool(ent) and (not _REQUIRE_QUOTE or _quote_gate(quote, spans))
> --- `bin/m3_judge.py`

> return 1.0 if verdict(claim, spans) == "entailed" else 0.0
> --- `bin/m3_judge.py`

> _log(f"DO_NOT_REGISTER SDK/route absent ({exc!r}) → M3 keeps deterministic overlap")
>         return False
> --- `bin/m3_judge.py`

#### EPI-RTE-acquisition-check
Label: M3 acquisition dark check
Part of: [RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing)

This is the parent's acquisition/agent candidate branch, not recall filing. SRC-1 `bin/m3_acquisition.py` checks candidate claim and transcript_quote against assistant turns, applies durability rejection, calls the judge, and appends a dark record. Program owns gates/logging; model judges quote support. Human contribution is activation configuration. No factual answer oracle. Mode: bounded transcript candidates. Rejection is nonmatching quote, safety rejection or not_entailed; route failures remain retryable. What persists is a diagnostic decision, not an admitted knowledge page. Acquisition's own quote_in_assistant_turns check remains required when the shared judge's quote gate is disabled; that configuration only removes the judge's additional quotation requirement.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: would_file, would_reject, judge_unavailable, error, or acknowledged-transport dark_append_failed.
- Later read-back: outcome feeds driver seen-cache/retry behavior; dark records retain claims/quotes/judgments for reports, not normal knowledge-card consumption.
- Delegated visibility: judge receives candidate claim and matching quote; acquisition reader rereads minable turns.
- Selection predicate: nonempty claim, quote present in assistant text, no durability rejection, then judge entailed.
- Invalidation or expiry: transient outcomes retry; definitive outcomes are cacheable; full cache module not directly inspected.
- Activation or effect: dark append and retry selection; no actual card admission in this branch.
- Evidence limits: transcript provenance establishes an assistant utterance, not its truth; child-lane transport and deployed activation unobserved.

> quote_ok = bool(claim) and quote_in_assistant_turns(quote, turns)
>     safety_reject = _miner.durability_reject_reason(cand)
> --- `bin/m3_acquisition.py`

> if would_file:
>         return "would_file"
>     if safety_reject or not quote_ok or judge == "not_entailed":
>         return "would_reject"
> --- `bin/m3_acquisition.py`

#### EPI-RTE-m2-reshaping
Label: M2 default consolidation and managed commit
Part of: [RT-RTE-semantic-maintenance](runtime.md#rt-rte-semantic-maintenance)

This part isolates body construction/commit from the parent's conflict, supersession and relevance evaluators. SRC-1 `bin/m2_synthesis.py`. Default _salient_claim skips Evidence and empty/noise lines, cleans the first usable line and caps it; _default_synthesis_body deduplicates slugs and sorts linked one-liner rows. Concrete deduction from inspected code: trigger text `# **Cache uses Redis.**`, slug `cache`, and no related rows yields salient `Cache uses Redis`; the generated body places `- [[cache]] — Cache uses Redis` after provenance and the consolidation heading. Formatting removal and row construction add no new substantive proposition in this case. This is implementation evidence, not target execution. A longer first line may lose scope when capped; reshaping is not a proof of fidelity.

Program proposes the default body, selects neighbors and decides writes. Callback synth_body_fn can replace generation; its semantic relation is indeterminate without output. Relevance and no-detected-conflict are admission criteria for a related-context edit, not factual acceptance. No answer oracle. Mode: event-triggered maintenance. Protected/uneditable cards, cross-project pairs, conflict/uncertainty, missing relevance and broken managed region can veto. Atomic locked replacement and retry/event repair protect consistency, not semantic rollback. Guidance is the fixed consolidation algorithm plus source cards; managed body and observed event persist.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: edit/skip/defer outcome with path, operation and region identity when applicable.
- Later read-back: region text and at most one observed event per edit enter subsequent indexing and recall/context selection.
- Delegated visibility: default construction sees trigger and relevance-passed related one-liners; callback receives the same seam's inputs.
- Selection predicate: parent activation, same project, editable target, no classified conflict/supersession, relevance above floor, valid region.
- Invalidation or expiry: region replacement rather than append growth; unchanged stable body skips edit or repairs missing event; broken region is not blindly overwritten.
- Activation or effect: bounded region write plus tier-1 observed event; no observed downstream behavior.
- Evidence limits: relevance is not factual support; deterministic source-line copying does not establish accepted ampliative production or successful learning.

> for s, salient in sorted(entries):  # deterministic slug order
>         lines.append(f"- [[{s}]] — {salient}" if salient else f"- [[{s}]]")
>     return "\n".join(lines)
> --- `bin/m2_synthesis.py`

> wrote = _EV.append_event(path, "observed", actor="agent-extracted",
>                                      note=note, _locked=True, _content=new_content)
> --- `bin/m2_synthesis.py`

Parent checks and disposition were independently inspected here. M1 uses selected lexical opposition, not arbitrary semantic conflict; absence of a detected reason returns no_contradiction. Authority can convert an otherwise demoting conflict to a non-ranking relation_claim diagnostic. M1 writes are separately opt-in. M2 temporal heuristics propose supersession; destructive mutation requires autosupersede, strict relevance and authority dominance. These counterpaths prevent reading detection as automatic semantic retirement.

> if not reason:
>         return "no_contradiction"
> --- `bin/m1_contradiction.py`

> if not m1_write_enabled():
>             outcomes.append({"loser": loser["path"], "winner": winner["slug"],
>                              "action": "diagnostic"})
>             continue
> --- `bin/m1_contradiction.py`

> if (m2_autosupersede_enabled() and same_project
>                     and r_sup is not None and r_sup >= M2_SUPERSEDE_MIN):
>                 act = _apply_supersession(index_db_path, T, P)
> --- `bin/m2_synthesis.py`

> if not _authority_dominates(trigger, target):
>         _oplog(index_db_path, OP_SUPERSESSION_SUGGESTION, target["slug"], trigger=trigger,
>                extra="reason=non-dominating-authority")
>         return "supersession_suggested"
> --- `bin/m2_synthesis.py`

#### EPI-RTE-test-affirmation
Label: Same-project test affirmation
Part of: [RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing)

This part isolates later promotion from initial support/file admission. SRC-1 `bin/lifecycle_signals.py` and `bin/m3_autofile.py`. PostToolUse Bash capture classifies a test command and emits test_pass. The producer matches session and nonempty project slug against M3 filed records, then calls affirm_filed_page with literal test_pass and target filed slug. The consumer trusts affirmation kind, checks target/idempotence, and appends the mapped event. User affirmation is another accepted typed kind; this inspection does not establish an automatic genuine-user-signal producer. No claim-specific expected answer or test-coverage oracle is supplied. Mode: session-correlated evidence promotion. Program selects/adopts; human can configure gates or supply a genuine affirmation but is not consulted for every correlated test promotion. No automatic semantic rollback; Evidence remains inspectable and later events can change its folded result.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: promoted event type, skip/rejection reason or producer results list.
- Later read-back: verified_by_test/confirmed event affects indexed confidence on subsequent fold, then optional ranking consumers.
- Delegated visibility: producer sees session/project metadata and filed paths, not claim-specific executed assertions; consumer trusts typed affirmation.
- Selection predicate: producer switch and M3 active; same session and nonempty matching project; target match and no duplicate event/session.
- Invalidation or expiry: repeated same event/session skipped; no expiry or proof-of-coverage check in this consumer.
- Activation or effect: append event; observed host test outcomes and later ranking changes absent.
- Evidence limits: capture assumes successful PostToolUse test delivery; project correlation cannot establish factual correctness of each filed claim.

> if command_class == "test":
>         _write_test_signal(memory_system, record)
> --- `bin/lifecycle_signals.py`

> slug = row.get("project_slug") or ""
>         if not slug or slug not in passing:           # cross-project / no-project ⇒ no match
>             continue
> --- `bin/m3_autofile.py`

> ok = _EV.append_event(filed_path, etype, session_id=sess,
>                           note=f"m3 affirmation {kind}")
> --- `bin/m3_autofile.py`

> "test_pass": "verified_by_test",
> --- `bin/m3_autofile.py`

#### EPI-RTE-confidence-ranking
Label: Confidence fold to ranking

Distinct from [RT-RTE-memory-recall](runtime.md#rt-rte-memory-recall) and [RT-RTE-context-injection](runtime.md#rt-rte-context-injection): shared upstream arithmetic/authority function spanning both consumers, not a replacement for either route. SRC-1 `bin/confidence.py`, `bin/search_impl.py`; context consumer wiring is supplied in runtime. Fold uses source cold starts, diminishing observed gain, event deltas and tier-3 high-water protection. It recomputes deltas rather than trusting stored edits. No human truth decision happens inside the algebra; events may originate from software/model judgments or user signals. No expected-answer oracle. Mode: deterministic event replay to selection metadata; not a candidate-generating theory route. Reindex is recovery/recomputation, not factual revalidation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: confidence plus flags; conf_weight returns scalar multiplier.
- Later read-back: index materializes confidence; later query/context consumers use configured weights.
- Delegated visibility: no model delegate in arithmetic; later consumers see selected content, not necessarily all event history.
- Selection predicate: managed/exempt type/source/kind; confidence ranking switch; event type and actor tier.
- Invalidation or expiry: each reindex recomputes from current events; decayed event has separate floor; no content truth expiry.
- Activation or effect: enabled multiplier enters ranking; low-confidence content is not universally inaccessible.
- Evidence limits: arithmetic has a named formal domain, but event authenticity, calibrated truth and improved decisions are not proven by it.

> "verified_by_test": {"tier": 2, "delta": +0.15},
> --- `bin/confidence.py`

> return CONF_FLOOR + (1.0 - CONF_FLOOR) * confidence
> --- `bin/confidence.py`

> compound = raw_rank * ev_w * src_w * fr_w * status_w * conf_w * max(0.1, match_quality)
> --- `bin/search_impl.py`

#### EPI-RTE-cleanup-archive
Label: Cleanup report or file archive

No supplied counterpart after comparison with [RT-RTE-semantic-maintenance](runtime.md#rt-rte-semantic-maintenance): this is age/size/link storage disposition, not pending-ingest semantic maintenance. SRC-1 `bin/cleanup.py`, entry wrapper `bin/cleanup.sh`. Code scores age over 90 days as two points (over 60 as one), orphan as one and under-100-byte size as one; score at least three becomes candidate. Feedback/user types are protected. Report is default; caller chooses --archive and count, after which code moves top candidates without per-card truth evaluation. Human versus agent caller identity is unknown. No answer oracle. Recovery is manual move/reindex; collision-safe archive names prevent overwrite. Separate --lifecycle-events deletes old JSONL by mtime, default 30 days, potentially reducing audit evidence but not rejecting a card proposition.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: printed ranked candidates or archive/deletion counts and failures.
- Later read-back: moved card locations alter future file collection after refresh; old index can still expose stale content until reindexed.
- Delegated visibility: inapplicable — filesystem maintenance has no model delegate.
- Selection predicate: nonprotected card, age/orphan/size score at least three; archive capped by caller count; log deletion uses retention age.
- Invalidation or expiry: archive relocation rather than card destruction; lifecycle-event deletion is irreversible without external backup.
- Activation or effect: report advisory; --archive moves files; --lifecycle-events removes selected metadata logs.
- Evidence limits: no semantic falsity or immediate index-consistent withdrawal established; no archive observed.

> if score >= 3:
>             candidates.append((score, name, path, reasons, age_days, size))
> --- `bin/cleanup.py`

> shutil.move(path, dest)
>             archived += 1
> --- `bin/cleanup.py`

> print(f"Run index.sh --full to update index")
> --- `bin/cleanup.py`

#### EPI-RTE-curate-archive
Label: Usage curation and status archive

No supplied counterpart after comparison with [RT-RTE-semantic-maintenance](runtime.md#rt-rte-semantic-maintenance); distinct also from cleanup relocation. SRC-1 `bin/curate.py`. Promote reports cards surfaced by sufficiently many distinct queries; it does not automatically change them to behavioral rules. Archive selects unresolved age_stale findings never pulled according to telemetry and excludes protected types. Code proposes; caller can veto by omitting --apply --yes, but flags do not prove a human decision. After both flags it writes status:archived atomically without moving the body. No answer oracle; use counts are not knowledge correctness. Guidance is drift/usage metadata; status persists. Reversal is setting current and reindexing.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: promotion/archive report or archived/already/skipped counts.
- Later read-back: reindex propagates status; search status weight downranks archived cards while keeping them accessible.
- Delegated visibility: inapplicable — no model delegate in this CLI.
- Selection predicate: age_stale, no recorded pull, nonprotected; --apply --yes for mutation.
- Invalidation or expiry: status can be manually restored; source body remains; derived state requires refresh.
- Activation or effect: report or status write, not immediate factual rejection or guaranteed removal from every context route.
- Evidence limits: upstream telemetry completeness not audited; user invocation is not claim-level approval evidence.

> if not args.yes:
>         print(f"DRY RUN — would set status:archived on {len(rows)} card(s); search keeps\n"
>               f"them, drift stops flagging. Re-run with --apply --yes to write.\n")
> --- `bin/curate.py`

> res = _set_status_archived(r["path"])
> --- `bin/curate.py`

#### EPI-RTE-vault-generation
Label: Vault polish and topic synthesis

Distinct extension of the export handler in `mcp_server.py`, not a duplicate of [RT-RTE-explicit-admission](runtime.md#rt-rte-explicit-admission): outputs are vault projection pages, not personal/base admission. SRC-1 `bin/export_vault.py`. _build_polish_prompt asks for unchanged facts; polish_note admits process success plus output over 50 characters, then apply_polished/write replace body. Topic synthesis reads up to 20 weighted note bodies, bounds text, asks for a coherent article with preserved facts, and accepts successful output over 100 characters before writing topics/*.md with member links. Neither inspected seam checks generated entailment or author approval. Code owns invocation, limits and write selection; [EPI-CMP-vault-models](#epi-cmp-vault-models) generates. No answer oracle. Mode: requested export; polish default on, topic synthesis explicit. CLI caller may disable either, but no per-claim veto. Failure skips/aborts generation; atomic replacement protects integrity, not semantic rollback. Generated articles and polished flag persist.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: rewritten body or None; topic/page metadata and export report after writes.
- Later read-back: subsequent vault browsing/exports can read generated pages; synthesized articles are linked from vault navigation. Automatic personal-store reintegration not established.
- Delegated visibility: polish sees one exported body; topic model sees bounded selected note texts; omitted notes/conditions are not available to that call.
- Selection predicate: requested export and available claude-batch; polish routing by structure/size; topic generation enabled and source contents present; subprocess success and minimum length.
- Invalidation or expiry: polish flag skips already-polished bodies; manifests/delta machinery influence rewrites, not source-warrant checks; complete invalidation semantics not assessed.
- Activation or effect: generated body/flag or topic page written; later reader use unobserved.
- Evidence limits: instruction to preserve facts is not evidence of compliance; no output proves entailment, ampliative novelty, acceptance or benefit.

> "Keep ALL facts exactly as written: numbers, names, paths, model IDs, error "
>     "codes, dates, links. Remove agent jargon like 'compound_weight', "
> --- `bin/export_vault.py`

> if len(out) <= 50:
>         return None
>     return out
> --- `bin/export_vault.py`

> if len(out) <= 100:
>         return None
>     return out
> --- `bin/export_vault.py`

> new_content = apply_polished(content, rewritten)
>                 tmp = note_path + ".tmp"
>                 with open(tmp, "w", encoding="utf-8") as f:
>                     f.write(new_content)
>                 os.replace(tmp, note_path)
> --- `bin/export_vault.py`

> with open(tmp, "w", encoding="utf-8") as f:
>             f.write(content)
>         os.replace(tmp, path)
> --- `bin/export_vault.py:956-959`

#### EPI-RTE-smoke-evaluation
Label: Recall smoke case evaluation

Distinct from [RT-RTE-memory-recall](runtime.md#rt-rte-memory-recall): this is an offline authored-case evaluator invoking search, not the runtime's relevance/confidence decision. SRC-1 `bin/recall_smoke.py`. A case supplies expect_any substrings and minimum confidence, or expect_no_confident. Code judges payload fields and result text; main prints PASS/FAIL, counts failures and returns status. Human/source authors supply expectations, not a per-run model oracle. Mode: fixed bounded test cases, optionally one selected case. No card admission, revision or rollback follows here; invalid/failed searches are test failures, and missing optional code index skips positive code cases. Guidance is the static authored case set. These tests do not independently vary a component or demonstrate recall calibration on arbitrary corpora.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: evaluate returns Boolean/detail; main emits PASS/FAIL/SKIP and process status.
- Later read-back: inapplicable — this inspected evaluator writes no revised knowledge artifact or retained policy consumed by a later invocation; redirected usage telemetry is not an accepted claim.
- Delegated visibility: search subprocess receives DB/query/case options; evaluator sees structured payload, not source truth or host task behavior.
- Selection predicate: authored cases or --case; positive code cases require code chunks; substring and minimum-confidence predicates or negative-result checks.
- Invalidation or expiry: inapplicable — no retained evaluator decision changes a later knowledge state in this inspected path.
- Activation or effect: failure count sets process exit status; no runtime memory admission gate.
- Evidence limits: implementation only, no observed test results; substring presence is a retrieval check, not comprehensive factual accuracy or causal benefit.

> if any(token in haystack for token in expected):
>             confidence = result.get("confidence", "low")
>             if confidence_at_least(confidence, min_confidence):
>                 return True, f"{result.get('path')} ({confidence})"
> --- `bin/recall_smoke.py`

> return 1 if failed else 0
> --- `bin/recall_smoke.py`

### Claims

#### EPI-CLM-truth-maintenance
Label: Detecting memories going bad

SRC-1 `README.md` describes stale-memory detection/downranking and drift plus truth maintenance. Distinct public warrant claim from the narrower assembly/base invariants [RT-CLM-feedback-visibility](runtime.md#rt-clm-feedback-visibility) and [RT-CLM-base-isolation](runtime.md#rt-clm-base-isolation). It also explicitly limits silent-rename detection and places full semantic maintenance on a roadmap; the claim is not fairly read as infallibility. Inspected maintenance code has gated M1/M2 paths beyond that prose's simple roadmap split. No README performance assertion is treated as observed evidence.

> **Long-term memory for AI coding agents — that knows when its memories go bad.**
> --- `README.md`

> Eidetic attacks it with **drift detection + truth maintenance**: dead wikilinks, age-stale cards, unconfirmed agent escalation, and declared contradictions / supersession (`contradicts:` / `supersedes:` frontmatter) all genuinely down-rank a card before it poisons the agent. The one case above that nothing declares — a *silent* rename with no broken link — still needs **semantic** contradiction detection, which is the [v6 roadmap](#roadmap); until then it's caught when the rule's wikilink dies, the card ages out, or a newer card declares `contradicts:` it.
> --- `README.md`

#### EPI-CLM-support-gate
Label: M3 anti-laundering support gate
Part of: [RT-RTE-m3-filing](runtime.md#rt-rte-m3-filing)

The source-native module docstring calls the support gate anti-laundering and distinguishes initial confidence from runtime read gating. This claim is a design assertion within the parent implementation route, not a second filing route. SRC-1 `bin/m3_autofile.py`. Its warranted scope is rejection before filing/M2 routing under enabled flags, not global factual guarantee.

> confidence (0.40 = confidence.COLD_AGENT_EXTRACTED). The gate is the
> anti-laundering mechanism; confidence is a trust MARK, not a runtime read gate —
> --- `bin/m3_autofile.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
