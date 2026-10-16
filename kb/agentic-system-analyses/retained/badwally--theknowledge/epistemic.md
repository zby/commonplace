---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "TheKnowledge epistemic routes: source acquisition, citation checks, model synthesis, evaluators and reversible reliance at the frozen Git revision."
run-id: AAS-2026-10-14-theknowledge-319a64927ee3-01
reviewed-boundary: aca6e29e69c6a72b697b8178841d03e6296ee3fc
---

# TheKnowledge epistemic report

## Source-and-claim boundary

Question: which shipped routes acquire or produce truth-apt content, check it, grant reliance, retain it and affect later behavior? Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identities are see [Source register](boundary.md#source-register). All additional reads below are SRC-1 implementation or attributed doctrine/design at the frozen revision, not new sources. No target code, tests, examples or providers were executed. No observed-run or causal evidence is supplied.

Assessed families: source/editorial admission; model page and answer production; citation-shaped validation; retained context selection; golden evaluation; candidate policy calibration; contradiction detection/precedence/withdrawal; bibliographic retraction warnings; reversible graph-based cleanup; caller-corrected editorial guidance. Runtime is provisional: direct inspection found additional evaluator, scan and recovery routes. No supplied record needs renaming or supersession; its valid container remains. The deposit identity-copy path was also read directly in SRC-1 `src/gateway/ops/deposit.py` to test whether source_type was authenticated before conflict precedence. New parts state containment. New mechanisms without a supplied counterpart state their distinction.

Missing run evidence prevents conclusions about exercised acceptance, model compliance, retrieval quality, successful recovery, learning or causal improvement. Provider internals prevent reconstructing NotebookLM synthesis grounding, exact parameter state and any provider-side adaptation. Individual retained domain claims were not assessed: their presence cannot identify which production/check route actually operated. Uninspected included operations below prevent a system-complete negative about truth checking or knowledge production; they are available evidence, not access gaps.

Public warrant claims: [EPI-CLM-retrieval-grounding](epistemic.md#epi-clm-retrieval-grounding), [EPI-CLM-answer-grounding](epistemic.md#epi-clm-answer-grounding), [EPI-CLM-citation-provenance](epistemic.md#epi-clm-citation-provenance). Gateway-write doctrine is see [RT-CLM-gateway-only](runtime.md#rt-clm-gateway-only).

| Entry point / operation | Source path | Coverage and records | Remaining boundary |
|---|---|---|---|
| CLI dispatch; full/read MCP; browser operations | SRC-1 `src/gateway/cli.py`, `src/gateway/mcp_server.py`, `src/gateway/web/routes/ops.py` | Direct dispatch searches; supplied runtime account | Every handler was not read in full; no complete enforcement verdict |
| Ingest/filter/plan/apply/finalize/deposit worker | SRC-1 `src/gateway/ops/ingest.py`, `src/gateway/ops/apply_plan.py`, `src/gateway/ops/finalize.py`, `src/gateway/ops/committer.py` | Supplied [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship), [RT-RTE-draft-finalization](runtime.md#rt-rte-draft-finalization), [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit); direct citation checker and dedup/gate branches | Acquisition converters individually unassessed; source warrant after extraction unknown |
| Retrieve/answer; FTS ranking | SRC-1 `src/gateway/ops/answer.py`, `src/gateway/search_index.py`, `src/gateway/ops/retrieve.py` | Direct answer/ranking reads; supplied [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer) | Dense/multidomain assembly evidence supplied by runtime; no answer-quality run |
| Research/query/NotebookLM | SRC-1 `src/gateway/research/orchestrator.py`, `src/gateway/ops/query.py` | Supplied [RT-RTE-research-query](runtime.md#rt-rte-research-query) | Remote indexed corpus and inference opaque; adapters individually unassessed |
| Policy bootstrap/edit/finetune/skill-emit | SRC-1 `src/gateway/ops/bootstrap_domain.py`, `src/gateway/ops/policy_edit.py`, `src/gateway/ops/finetune.py`, `src/gateway/ops/skill_emit.py` | Supplied runtime routes; direct calibration/policy/filter prompt reads | Candidate improvement/promotion unobserved; generated guidance is not checked truth |
| evaluate; eval-retrieval; calibration readiness/correction | SRC-1 `src/gateway/evaluate/runner.py`, `src/gateway/evaluate/judge.py`, `src/gateway/evaluate/wiki_context.py`, `src/gateway/evaluate/retrieval_eval.py`, `src/gateway/ops/calibration.py`, `src/gateway/ops/filter_calibrator.py`, `src/gateway/ops/filter_correct.py` | Direct reads; [EPI-RTE-wiki-evaluation](epistemic.md#epi-rte-wiki-evaluation), [EPI-RTE-retrieval-measure](epistemic.md#epi-rte-retrieval-measure), [EPI-RTE-filter-calibration](epistemic.md#epi-rte-filter-calibration), [EPI-RTE-filter-correction](epistemic.md#epi-rte-filter-correction) | Embedding bakeoff and merge-map evaluator implementation not independently traced; policy gate coverage is supplied runtime |
| lint/sweep/drift/structured resolution/revert | SRC-1 `src/gateway/lint/contradictions.py`, `src/gateway/ops/contradiction_sweeper.py`, `src/gateway/ops/contradiction_drift.py`, `src/gateway/ops/contradiction.py`, `src/gateway/commit_gate.py` | Direct reads; [EPI-RTE-contradiction-scan](epistemic.md#epi-rte-contradiction-scan), [EPI-RTE-conflict-selection](epistemic.md#epi-rte-conflict-selection), [EPI-RTE-conflict-materialization](epistemic.md#epi-rte-conflict-materialization), [EPI-RTE-resolution-revert](epistemic.md#epi-rte-resolution-revert) | Automatic reopen detectors and all lint checks unassessed; no complete conflict coverage |
| pubmed-retractions; retracted-citations | SRC-1 `src/gateway/pollers/pubmed_retractions.py`, `src/gateway/lint/retracted_citations.py` | Direct reads; [EPI-RTE-retraction-monitor](epistemic.md#epi-rte-retraction-monitor), [EPI-RTE-retraction-warning](epistemic.md#epi-rte-retraction-warning) | arXiv revisions/link-rot and cascade helper not fully inspected; full withdrawal coverage unknown |
| remediate/restore-depath/reverse-merge | SRC-1 `src/gateway/ops/remediate.py`, `src/gateway/ops/reverse_merge.py`, `src/gateway/commit_gate.py` | Direct selectors/public restoration/apply branches; [EPI-RTE-orphan-selection](epistemic.md#epi-rte-orphan-selection), [EPI-RTE-depath-recovery](epistemic.md#epi-rte-depath-recovery) | reverse_merge_plan helper, overlap and crash behavior not fully assessed |
| cite-add/edit-section/editorial review | SRC-1 `src/gateway/ops/cite_add.py`, `src/gateway/ops/edit_section.py`, `.claude/skills/wiki-editorial-review/SKILL.md` | Direct bounded repair/read-only-review paths; [EPI-RTE-citation-check](epistemic.md#epi-rte-citation-check) distinguishes citation appearance from support | Underlying cite/cite-suggest/capture, concept-add and other direct authoring helpers not fully traced; no universal semantic admission claim |
| Hooks/scheduler/watcher/foreground skills | SRC-1 `.claude/settings.json`, `.claude/hooks/precompact-snapshot.sh`, `.claude/hooks/session-start-reanchor.sh`, `src/gateway/scheduler.py`, `src/gateway/watcher.py` | Supplied [RT-RTE-session-reanchor](runtime.md#rt-rte-session-reanchor) and boundary; editorial skill directly read | Host delivery/compliance unobserved; shell schedules are not a truth gate |
| Other maintenance, agents, migrations, raw/wiki payload | SRC-1 `src/gateway/ops/`, `src/gateway/agents/`, `migrations/`, `wiki/`, `raw/` | Operation inventory only for demand-cluster, discovery/promotion, daily digest/review, orphan discharge, reingest, backfills and publishing | Included but unassessed; prevents exhaustive positive/negative about all content or policy updates |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-source-text](epistemic.md#epi-obj-source-text) | Imported source assertions, bibliographic status | see record | SRC-1 `src/gateway/filter/semantic.py` | Extraction fidelity and original source warrant unknown |
| [EPI-OBJ-page-text](epistemic.md#epi-obj-page-text) | Wiki facts/syntheses/answers/conflict annotations | see record | SRC-1 `src/gateway/ops/answer.py` | Delivered/generated prose not necessarily entailed or accepted |
| [RT-OBJ-plan](runtime.md#rt-obj-plan) | Markdown candidate inside symbolic update envelope | see record | SRC-1 `src/gateway/plan.py` | Parser and file checks do not certify every assertion |
| [RT-OBJ-intent](runtime.md#rt-obj-intent) | Caller prose or reversal/policy payload inside queued control state | see record | SRC-1 `src/gateway/intent_queue.py` | Receipt is not canonical admission or truth acceptance |
| [EPI-OBJ-eval-results](epistemic.md#epi-obj-eval-results): EvalRunSummary | Wiki/reference-fit judgment and reasoning | see record | SRC-1 `src/gateway/evaluate/runner.py` | Model score is advisory, retained in YAML/trend CSV |
| [EPI-OBJ-eval-results](epistemic.md#epi-obj-eval-results): EvalReport | First expected-slug rank and aggregate hit fraction | see record | SRC-1 `src/gateway/evaluate/retrieval_eval.py` | Reference relevance, not source truth; policy gate consumes metric |
| [EPI-OBJ-eval-results](epistemic.md#epi-obj-eval-results): CalibrationMetrics | Candidate binary-label agreement | see record | SRC-1 `src/gateway/ops/calibration.py` | Optional candidate annotation; no promotion threshold here |
| [EPI-OBJ-eval-results](epistemic.md#epi-obj-eval-results): LintFinding | Candidate conflict/retraction exposure | see record | SRC-1 `src/gateway/lint/contradictions.py` | Advisory findings; scan can persist as draft or snapshot |
| [EPI-OBJ-eval-results](epistemic.md#epi-obj-eval-results): resolution act | Rule-selected winner/loser and recorded rationale | see record | SRC-1 `src/gateway/ops/contradiction.py` | Symbolic precedence feeds annotation/reversal; not a truth verdict |
| [EPI-OBJ-policy-text](epistemic.md#epi-obj-policy-text): editorial criteria | Relevance prescriptions; descriptions may be truth-apt | see record | SRC-1 `src/gateway/filter/policy.py` | Live/candidate YAML have different installation paths |
| [EPI-OBJ-policy-text](epistemic.md#epi-obj-policy-text): corrected examples | Binary editorial labels and rationale | see record | SRC-1 `src/gateway/ops/filter_correct.py` | Prompt selection mediates future influence; caller identity unresolved |
| [EPI-OBJ-policy-text](epistemic.md#epi-obj-policy-text): domain skill | Host instructions plus selected wiki titles | see record | SRC-1 `src/gateway/ops/skill_emit.py` | Persisted text is interpretive; discovery/compliance unobserved |
| [EPI-OBJ-policy-text](epistemic.md#epi-obj-policy-text): session snapshot | Requested assertions about working tree, decisions and next step | see record | SRC-1 `.claude/hooks/session-start-reanchor.sh` | Snapshot generation/checking is requested, not evidenced completion |
| [RT-CMP-qwen3-embedding](runtime.md#rt-cmp-qwen3-embedding) | not determinable as individuated propositions; numerical retrieval state | see record | SRC-1 `src/gateway/retrieval_encoder.py` | Exact weights/provenance unknown; no truth oracle inferred |
| [RT-CMP-claude-haiku](runtime.md#rt-cmp-claude-haiku), [RT-CMP-claude-opus](runtime.md#rt-cmp-claude-opus), [RT-CMP-claude-sonnet](runtime.md#rt-cmp-claude-sonnet), [RT-CMP-notebooklm](runtime.md#rt-cmp-notebooklm) | Provider-parametric truth-apt content not determinable from accessible state | see records | SRC-1 `src/gateway/llm/config.py` | Inference outputs are accessible candidates; hidden parameter contents/updates are not |

## Authority-route ledger

This is an epistemic overlay, not a second declaration of generic route fields. `see` points to the owning record. All implemented rows have source-only support; activation and observed results remain unobserved. Linked rows separate checking, disposition, retention and consumption. Non-ampliative reshaping is not inferred for opaque model synthesis or citation deletion.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship) | content transformation | implemented | [EPI-OBJ-source-text](epistemic.md#epi-obj-source-text) | truth-apt transformation: acquisition/import | External source into retained raw text | Converter and source validators; see record | see [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship) | Canonical source and optional source page | Admission protocol | Source warrant unknown; hash equality licenses body identity, not truth | Persist input for later authorship | Plan/retrieval consumers; filesystem text; permissive; later calls | SRC-1 `src/gateway/ops/ingest.py` | none | none | Converter fidelity/source truth unassessed. |
| [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship) | check/evidence production | implemented | [EPI-OBJ-source-text](epistemic.md#epi-obj-source-text) | no content change | Domain relevance/quality fit | Model scores capped source against policy/examples; code parses bounded numeric score | see [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship) | Score/rationale | Advisory score to threshold consumer | Editorial-fit judgment only | Provide source admission input | Ingest code; FilterResult; permissive threshold input; current ingest | SRC-1 `src/gateway/filter/semantic.py` | none | none | Not a source-factuality check; force-include bypasses scoring. |
| [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship) | disposition/acceptance | implemented | [EPI-OBJ-source-text](epistemic.md#epi-obj-source-text) | no content change | Wiki-source inclusion | Code policy thresholds or caller force; see record | see [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship) | Include/review/reject/skip/error | Enforcing source-page gate; raw retention separate | Operational editorial admission, not accepted source claims | Admit source page independently of raw and generated-page admission | Ingest code; filter result/override; enforcing; current write | SRC-1 `src/gateway/ops/ingest.py` | none | none | No execution supplied. |
| [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship) | content transformation | implemented | [RT-OBJ-plan](runtime.md#rt-obj-plan) | truth-apt transformation: indeterminate | Model full-page updates | Source/existing-page prompt plus error-fed repair; see record | see [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship) | Plan candidate | Proposal only before validation | Cannot distinguish faithful reshaping, derivation and conjecture without actual propositions/input comparison | Submit generated changes to validation | apply_plan; parsed Plan; permissive candidate; current call | SRC-1 `src/gateway/plan.py` | none | none | Prompt requests synthesis; novelty/non-entailment and accepted ampliation not evidenced. |
| [EPI-RTE-citation-check](epistemic.md#epi-rte-citation-check) | check/evidence production | implemented | [EPI-OBJ-page-text](epistemic.md#epi-obj-page-text) | no content change | Claim-shaped sentences citation presence | Deterministic heuristic, not source evidence judge | see [EPI-RTE-citation-check](epistemic.md#epi-rte-citation-check) | Errors/warnings | Strict-veto input; draft advisory | Citation-shaped coverage only | Permit/reject depending on strict/draft consumer | apply_plan/finalize; ValidationResult; enforcing/advisory; current admission | SRC-1 `src/gateway/validator.py` | [EPI-CLM-citation-provenance](epistemic.md#epi-clm-citation-provenance) | citation tokens != semantic warrant | No execution supplied. |
| [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship) | disposition/acceptance | implemented | [RT-OBJ-plan](runtime.md#rt-obj-plan) | no content change | Schema/citation-preservation/update guards | Code validation then write/rollback; see record | see [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship) | Write or rejection/warning | Enforcing file-admission protocol | Structural acceptance for canonical file use, not truth acceptance | Allow later wiki reuse including drafts | Filesystem/retrieval; accepted write; permissive; subsequent calls | SRC-1 `src/gateway/ops/apply_plan.py` | none | none | No execution supplied. |
| [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship) | retention | implemented | [EPI-OBJ-page-text](epistemic.md#epi-obj-page-text) | no content change | Validated/draft content persistence | Filesystem write; see record | see [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship) | Retained pages/backlinks/contradiction log | Durable-by-protocol ledger use | Retention/integration bookkeeping is not evidence-consuming claim acceptance | Later page retrieval and authorship permitted | Models/humans; retained markdown; interpretive/permissive; across calls | SRC-1 `src/gateway/ops/apply_plan.py` | none | none | No lifecycle-integration finding follows without demonstrated claim acceptance; exception rollback is best effort. |
| [RT-RTE-draft-finalization](runtime.md#rt-rte-draft-finalization) | disposition/acceptance | implemented | [EPI-OBJ-page-text](epistemic.md#epi-obj-page-text) | no content change | Strict page validation / draft metadata | Code full validator; see record | see [RT-RTE-draft-finalization](runtime.md#rt-rte-draft-finalization) | Nondraft or failure/escalation; abandon deletes | Enforcing status transition | Nondraft means stricter syntax, not source entailment | Removes draft metadata; draft reading already possible | Retrieval/maintenance; retained status; permissive; later calls | SRC-1 `src/gateway/ops/finalize.py` | none | none | No execution supplied. |
| [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit) | operational admission/selection/consumption | implemented | [RT-OBJ-intent](runtime.md#rt-obj-intent) | truth-apt transformation: indeterminate | Caller prose; alias-based entity identity/dedup and Git state | Deterministic same-kind normalized-name criterion; see record | see [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit) | Merge/link/distinct; commit/reject/quarantine | Enforcing queue/Git admission | Co-reference is a policy assumption; names/geometry do not warrant every merged fact | Write/union retained text without apply_plan citation checks | Commit worker/gate; rendered writes; enforcing; current drain and later retrieval | SRC-1 `src/gateway/dedup.py` | [RT-CLM-gateway-only](runtime.md#rt-clm-gateway-only) | none | Verbatim deposit is import; union with inferred co-reference makes whole semantic relation indeterminate. |
| [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer) | operational admission/selection/consumption | implemented | [EPI-OBJ-page-text](epistemic.md#epi-obj-page-text) | truth-apt transformation: indeterminate | Retained sections into model context | Rank/quota/budget code; see record | see [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer) | Ranked/truncated marked blocks | Ranking/permissive delivery | No new truth warrant; source attribution can be lost on truncation | Supply selected wiki prose including drafts to answer generation | Answer model; context blocks; interpretive; current question | SRC-1 `src/gateway/ops/retrieve.py` | [EPI-CLM-retrieval-grounding](epistemic.md#epi-clm-retrieval-grounding) | strict bounded/citation-preserved wording exceeds exceptions | Untruncated selection is non-ampliative reshaping; truncated prose can lose qualifiers/citations, so semantic preservation of the whole assembled result is indeterminate. |
| [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer) | content transformation | implemented | [EPI-OBJ-page-text](epistemic.md#epi-obj-page-text) | truth-apt transformation: indeterminate | Question-conditioned answer prose | Sonnet/API model prompt; see record | see [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer) | Generated answer candidate | Prompt-requested context reliance | No output comparison proves entailment or non-entailment | Return candidate to cleanup; optional draft filing | Cleanup/caller; answer string; advisory/permissive; current call | SRC-1 `src/gateway/ops/answer.py` | [EPI-CLM-answer-grounding](epistemic.md#epi-clm-answer-grounding) | none | External parametric inference is not a checked derivation. |
| [EPI-RTE-answer-cleanup](epistemic.md#epi-rte-answer-cleanup) | content transformation | implemented | [EPI-OBJ-page-text](epistemic.md#epi-obj-page-text) | truth-apt transformation: indeterminate | Answer citation membership | Regex against retrieved-ID set | see [EPI-RTE-answer-cleanup](epistemic.md#epi-rte-answer-cleanup) | Unknown IDs removed, prose survives | Enforcing token deletion only | Membership in supplied block, not semantic support | Return cleaned answer, optionally retain draft | Caller/later wiki readers; surviving prose; interpretive/permissive; current and future calls | SRC-1 `src/gateway/ops/answer.py` | [EPI-CLM-answer-grounding](epistemic.md#epi-clm-answer-grounding) | ungrounded citation != unsupported fact | No execution supplied. |
| [RT-RTE-research-query](runtime.md#rt-rte-research-query) | content transformation | implemented | [EPI-OBJ-page-text](epistemic.md#epi-obj-page-text) | truth-apt transformation: acquisition/import | NotebookLM synthesis and source-map rendering | Opaque provider and local citation remapping/application; see record | see [RT-RTE-research-query](runtime.md#rt-rte-research-query) | Cited/draft wiki synthesis | Remote proposal plus local structural admission | Acquired provider prose; semantic entailment and source-map completeness unknown | Retain for later retrieval even if promotion warns | Wiki readers/answer model; synthesis files; interpretive/permissive; future calls | SRC-1 `src/gateway/ops/query.py` | none | none | Provider facts imported, not automatically locally produced knowledge; exact remote corpus opaque. |
| [EPI-RTE-wiki-evaluation](epistemic.md#epi-rte-wiki-evaluation) | check/evidence production | implemented | [EPI-OBJ-eval-results](epistemic.md#epi-obj-eval-results) | no content change | Selected domain wiki against golden facts/citations | Sonnet judge + output parser | see [EPI-RTE-wiki-evaluation](epistemic.md#epi-rte-wiki-evaluation) | Per-question and aggregate score | Advisory report, no page gate here | Reference-fit judgment within supplied context only | Record report; no automatic page revision in runner | Operator; YAML/CSV/returned score; advisory; run/history | SRC-1 `src/gateway/evaluate/runner.py` | none | none | Golden validity, omitted source evidence and model score arithmetic unknown. |
| [EPI-RTE-retrieval-measure](epistemic.md#epi-rte-retrieval-measure) | check/evidence production | implemented | [EPI-OBJ-eval-results](epistemic.md#epi-obj-eval-results) | no content change | First expected slug rank | Deterministic curated-slug comparison | see [EPI-RTE-retrieval-measure](epistemic.md#epi-rte-retrieval-measure) | Hit fraction/MRR | Advisory standalone; floor input in policy-edit | Retrieval of at least one expected slug, not correct answer | Gate may block policy-edit | Policy gate/operator; EvalReport; advisory/enforcing input; current proposal | SRC-1 `src/gateway/evaluate/retrieval_eval.py` | none | none | No execution supplied. |
| [RT-RTE-policy-edit](runtime.md#rt-rte-policy-edit) | disposition/acceptance | implemented | [EPI-OBJ-policy-text](epistemic.md#epi-obj-policy-text) | non-truth-apt policy/content update: proposed policy replacement | Policy write and tested dedup/retrieval domains | Principal and evaluator gates; see record | see [RT-RTE-policy-edit](runtime.md#rt-rte-policy-edit) | Commit/dead-letter; explicit dev missing-golden skips | Enforcing route-local change control | Tested retrieval floor and proposed dedup golden fit only | Admit full policy despite broader untested fields | Policy-dependent consumers; YAML; enforcing guidance when consumed; later calls | SRC-1 `src/gateway/commit_gate.py` | none | none | No universal policy admission: bootstrap/force bypasses these gates. |
| [EPI-RTE-filter-calibration](epistemic.md#epi-rte-filter-calibration) | check/evidence production | implemented | [EPI-OBJ-policy-text](epistemic.md#epi-obj-policy-text) | no content change | Candidate binary editorial criteria fit | Model classifier + code against calibration labels | see [EPI-RTE-filter-calibration](epistemic.md#epi-rte-filter-calibration) | Precision/recall/F1/accuracy or None | Advisory candidate metrics | Agreement on capped examples, not generalization/source truth | Retain metric beside candidate, no promotion gate here | Reviewer; candidate YAML/result; advisory; later review | SRC-1 `src/gateway/ops/calibration.py` | none | none | No execution supplied. |
| [RT-RTE-policy-distillation](runtime.md#rt-rte-policy-distillation) | behavior/policy adaptation | implemented | [EPI-OBJ-policy-text](epistemic.md#epi-obj-policy-text) | non-truth-apt policy/content update: editorial/host guidance | Criteria/skill generation | see [RT-RTE-policy-distillation](runtime.md#rt-rte-policy-distillation) | see [RT-RTE-policy-distillation](runtime.md#rt-rte-policy-distillation) | Retained criterion candidate and optional metrics | Advisory candidate only | No epistemic acceptance inferred from guidance production | Stops before live policy replacement | Reviewer; candidate YAML; advisory; later review | SRC-1 `src/gateway/ops/finetune.py` | none | none | Conditions/learning/reflection/autonomy are see runtime record, independently unresolved where recorded. |
| [RT-RTE-policy-bootstrap](runtime.md#rt-rte-policy-bootstrap) | behavior/policy adaptation | implemented | [EPI-OBJ-policy-text](epistemic.md#epi-obj-policy-text) | non-truth-apt policy/content update: editorial/host guidance | Criteria/skill generation | see [RT-RTE-policy-bootstrap](runtime.md#rt-rte-policy-bootstrap) | see [RT-RTE-policy-bootstrap](runtime.md#rt-rte-policy-bootstrap) | Schema-valid live policy, or draft/error | Enforcing live write; criteria interpretive at filter | Schema validity, not criterion truth or quality | Govern future domain filter scoring | Filter model; loaded policy YAML; interpretive; future source requests | SRC-1 `src/gateway/ops/bootstrap_domain.py` | none | none | Conditions/learning/reflection/autonomy are see runtime record, independently unresolved where recorded. |
| [RT-RTE-skill-emission](runtime.md#rt-rte-skill-emission) | behavior/policy adaptation | implemented | [EPI-OBJ-policy-text](epistemic.md#epi-obj-policy-text) | non-truth-apt policy/content update: editorial/host guidance | Criteria/skill generation | see [RT-RTE-skill-emission](runtime.md#rt-rte-skill-emission) | see [RT-RTE-skill-emission](runtime.md#rt-rte-skill-emission) | Retained domain SKILL.md | Interpretive host guidance if loaded | Deterministic re-render of selected guidance, not new warrant | Supply domain criteria and selected titles to later host sessions | Foreground agent; generated skill; interpretive; sessions until regeneration | SRC-1 `src/gateway/ops/skill_emit.py` | none | none | Conditions/learning/reflection/autonomy are see runtime record, independently unresolved where recorded. |
| [EPI-RTE-filter-correction](epistemic.md#epi-rte-filter-correction) | behavior/policy adaptation | implemented | [EPI-OBJ-policy-text](epistemic.md#epi-obj-policy-text) | non-truth-apt policy/content update: retained corrected label and rationale | Past editorial decision | Caller proposal, code diff check | see [EPI-RTE-filter-correction](epistemic.md#epi-rte-filter-correction) | Pinned example and raw correction | Interpretive guidance through future example selection | Editorial label, not truth acceptance | Can alter future model scoring prompts | Filter model; selected example/rationale; interpretive; future requests | SRC-1 `src/gateway/ops/filter_correct.py` | none | none | No execution supplied. |
| [EPI-RTE-contradiction-scan](epistemic.md#epi-rte-contradiction-scan) | check/evidence production | implemented | [EPI-OBJ-page-text](epistemic.md#epi-obj-page-text) | no content change | Direct contradiction between extracted sentences | Model pair/rationale proposal; code index checks | see [EPI-RTE-contradiction-scan](epistemic.md#epi-rte-contradiction-scan) | Potential contradictions; empty/failure results | Advisory diagnostic | Candidate inconsistency judgment, not winner truth | Lint review; no mandatory factual repair | Operator/sweeper; findings; advisory; current scan | SRC-1 `src/gateway/lint/contradictions.py` | none | none | No execution supplied. |
| [EPI-RTE-contradiction-scan](epistemic.md#epi-rte-contradiction-scan) | retention | implemented | [EPI-OBJ-eval-results](epistemic.md#epi-obj-eval-results) | no content change | Scan output as draft/snapshot | Weekly/daily code drivers | see [EPI-RTE-contradiction-scan](epistemic.md#epi-rte-contradiction-scan) | Draft synthesis and daily diff retained | Direct write and advisory retained diagnosis | Disappeared keys only; resolved label does not license factual resolution | Draft can reach ordinary retrieval; snapshot informs later diff | Wiki readers/operator; markdown/JSON; interpretive/advisory; later calls/days | SRC-1 `src/gateway/ops/contradiction_sweeper.py` | none | none | Same-week skip, batch scope and parse-to-empty can obscure unresolved conflicts. |
| [EPI-RTE-conflict-selection](epistemic.md#epi-rte-conflict-selection) | disposition/acceptance | implemented | [EPI-OBJ-page-text](epistemic.md#epi-obj-page-text) | no content change | Unequal extracted claim objects | Code source-type trust then string comparison | see [EPI-RTE-conflict-selection](epistemic.md#epi-rte-conflict-selection) | Winner/loser labels and act | Enforcing precedence input | Policy preference only; no evidence-consuming factual acceptance | Permit contested-edge construction while retaining both claims | Gate materializer; act dict; permissive; current deposit | SRC-1 `src/gateway/ops/contradiction.py` | none | old/new comparison is not actual recency; caller-derived new source_type | No execution supplied. |
| [EPI-RTE-conflict-materialization](epistemic.md#epi-rte-conflict-materialization) | retention | implemented | [EPI-OBJ-page-text](epistemic.md#epi-obj-page-text) | truth-apt transformation: indeterminate | Disputes annotation and loser claim | Deterministic selected-loser render | see [EPI-RTE-conflict-materialization](epistemic.md#epi-rte-conflict-materialization) | Retained Contested section | Interpretive annotation in canonical prose | Operational dispute claim; factual conflict/winner not independently checked | Later context contains both claims and dispute annotation | Retrieval/answer; markdown; interpretive; subsequent calls | SRC-1 `src/gateway/commit_gate.py` | none | claim-specific loser down-weight not established | No execution supplied. |
| [EPI-RTE-resolution-revert](epistemic.md#epi-rte-resolution-revert) | lineage/freshness/recovery | implemented | [EPI-OBJ-page-text](epistemic.md#epi-obj-page-text) | truth-apt transformation: indeterminate | Recorded conflict annotation withdrawal | Caller act request; code source-token scan and section strip | see [EPI-RTE-resolution-revert](epistemic.md#epi-rte-resolution-revert) | Committed removal/reverted act or dead-letter | Enforcing annotation deletion | Withdrawal of annotation, not truth of either claim | Later readers no longer receive stripped section | Retrieval/operator; modified markdown/act status; permissive; later calls | SRC-1 `src/gateway/commit_gate.py` | none | none | First matching page and whole sections are coarser than one act. |
| [EPI-RTE-retraction-monitor](epistemic.md#epi-rte-retraction-monitor) | content transformation | implemented | [EPI-OBJ-source-text](epistemic.md#epi-obj-source-text) | truth-apt transformation: acquisition/import | Bibliographic retraction status | External NCBI XML + broad substring checker | see [EPI-RTE-retraction-monitor](epistemic.md#epi-rte-retraction-monitor) | Raw retracted flag/cursor | Enforcing metadata write; warning input | Acquired bibliographic signal; source warrant may be degraded, no claim-by-claim invalidation | Permit lint warning without deleting raw claims | Lint; raw YAML flag; advisory downstream; future checks | SRC-1 `src/gateway/pollers/pubmed_retractions.py` | none | none | Parse-false and broad notice matching bound interpretation. |
| [EPI-RTE-retraction-warning](epistemic.md#epi-rte-retraction-warning) | check/evidence production | implemented | [EPI-OBJ-page-text](epistemic.md#epi-obj-page-text) | no content change | Direct/transitive cited retracted dependencies | Code link/graph check | see [EPI-RTE-retraction-warning](epistemic.md#epi-rte-retraction-warning) | ERROR/WARNING review findings | Advisory, not retrieval exclusion | Dependency exposure only; no claim truth verdict | Request review/replacement; retained prose remains usable | Operator; lint result/report; advisory; later maintenance | SRC-1 `src/gateway/lint/retracted_citations.py` | none | none | No execution supplied. |
| [EPI-RTE-orphan-selection](epistemic.md#epi-rte-orphan-selection) | operational admission/selection/consumption | implemented | [EPI-OBJ-page-text](epistemic.md#epi-obj-page-text) | no content change | Orphan de-path eligibility | Code index/provenance reachability | see [EPI-RTE-orphan-selection](epistemic.md#epi-rte-orphan-selection) | Queued delete candidate or dry-run list | Permissive intent production | Graph-based disposal, not falsehood rejection | Authorize delayed deletion for selected paths | Worker/gate; typed intent; permissive; later drain | SRC-1 `src/gateway/ops/remediate.py` | none | none | Selection-time safety does not ensure unchanged apply-time graph. |
| [EPI-RTE-depath-recovery](epistemic.md#epi-rte-depath-recovery) | lineage/freshness/recovery | implemented | [EPI-OBJ-page-text](epistemic.md#epi-obj-page-text) | no content change | Delete/restoration of recorded text | Code captures content then deletes; public restore reloads provenance | see [EPI-RTE-depath-recovery](epistemic.md#epi-rte-depath-recovery) | Removed/recreated file or dead-letter | Enforcing filesystem mutation | Recorded lineage only; restoration does not restore warrant | Remove/reintroduce page to future retrieval | Wiki retrieval; canonical file/provenance; permissive; later calls | SRC-1 `src/gateway/commit_gate.py` | none | none | No execution supplied. |
| [RT-RTE-session-reanchor](runtime.md#rt-rte-session-reanchor) | other — describe | doctrine only | [EPI-OBJ-policy-text](epistemic.md#epi-obj-policy-text) | truth-apt transformation: indeterminate | Requested development snapshot/check against tree | Host/agent natural-language instructions; see record | see [RT-RTE-session-reanchor](runtime.md#rt-rte-session-reanchor) | Requested snapshot/reread/verification | Advisory/interpretive host instructions | No observed acceptance of snapshot facts | Agent asked to verify before plan/write and escalate mismatch | Foreground agent; hook stdout/file; interpretive; compaction/later session | SRC-1 `.claude/hooks/session-start-reanchor.sh` | none | none | Actual compression, retained content and compliance opaque; no automatic script-level truth validation. |

Concrete implementation deductions (no target execution):

- Given valid ID `a`, answer input `The treatment cures every disease. [[sources/a]] [[sources/b]]` becomes `The treatment cures every disease. [[sources/a]]`: cleanup deletes only the unmatched `b` link. It does not challenge the universal claim. Evidence is see [EPI-RTE-answer-cleanup](epistemic.md#epi-rte-answer-cleanup). Thus link-set enforcement cannot establish factual grounding.
- In same-line text `This treatment always works for everyone. [[sources/a]]`, the claim heuristic sees at least five words, terminal period and any source token on the line. It marks cited irrespective of what source `a` says. Conversely code-fenced/bold-header/exempt text can escape claim detection. SRC-1 `src/gateway/citations.py`; see [EPI-RTE-citation-check](epistemic.md#epi-rte-citation-check). This is a concrete citation-presence check, not source evidence consumption.
- For equal source-type trust in gate conflict selection, `committed_at="old"` is greater lexicographically than `"new"`, so the existing side wins. This contradicts a literal latest-commit interpretation. See [EPI-RTE-conflict-selection](epistemic.md#epi-rte-conflict-selection). No claim truth follows whichever side wins.
- Same-kind names `ACME, Inc.` and `acme inc` normalize to the same string and trigger merge if selected as candidates; same spelling with different entity_kind never merges. SRC-1 `src/gateway/dedup.py`. This checks an encoded identity convention, not real-world co-reference or proposition support.

## System-claim versus route comparison

| Claim ID | Claimed operation/warrant | Source and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support/design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-retrieval-grounding](epistemic.md#epi-clm-retrieval-grounding) | see record | SRC-1 `README.md`; doctrine/design | Context grounding and preserved citations | [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer) | none supplied | No retrieval/answer experiment; budget/truncation exceptions | Ranked delivery with controls | Not a strict bounded/provenance-complete invariant |
| [EPI-CLM-answer-grounding](epistemic.md#epi-clm-answer-grounding) | see record | SRC-1 `README.md`; doctrine/design | Context-only answer with ungrounded IDs stripped | [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer), [EPI-RTE-answer-cleanup](epistemic.md#epi-rte-answer-cleanup) | none supplied | Prompt compliance not guaranteed; membership check leaves prose | Only retrieved-ID membership enforced | Semantic grounding remains unestablished |
| [EPI-CLM-citation-provenance](epistemic.md#epi-clm-citation-provenance) | see record | SRC-1 `WIKI.md`; doctrine/design | NLM citation tokens said to prove corpus provenance | [EPI-RTE-citation-check](epistemic.md#epi-rte-citation-check), [RT-RTE-research-query](runtime.md#rt-rte-research-query) | none supplied | Opaque token existence not locally checked; corpus-source mapping incomplete cases | Syntactic grounding token accepted | A token plus notebook ID does not prove actual provenance |
| [RT-CLM-gateway-only](runtime.md#rt-clm-gateway-only) | see record | SRC-1 `CLAUDE.md`; doctrine/design | Foreground gateway discipline | [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship), [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit) | none supplied | No host filesystem isolation; gateway paths have distinct validators | Instruction and route-local checks | Gateway use does not imply one universal factual/citation admission gate |

## Bounded conclusion

**Imported and retained content can influence later answers before any demonstrated factual acceptance.** See [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship), [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer), [RT-RTE-research-query](runtime.md#rt-rte-research-query). Raw assertions, model-generated pages, caller deposits and drafts are different admission paths. Source identity/hash and citation shape retain some lineage, but original source warrant is unknown, and truncation/opaque provider tokens can weaken attribution. Query imports provider-produced prose; local model authorship and answering are candidate production. No inspected actual proposition/input pair establishes checked entailed derivation or demonstrable non-entailment of an accepted ampliative claim. Local model transformation remains indeterminate, not automatically conjecture because a model generated text; provider synthesis is acquired with unknown source warrant.

**Implemented evaluators have distinct licenses and consumers.** Citation checking and finalization enforce structural file criteria, not factual entailment; answer cleanup enforces retrieved-ID membership only. Wiki-state evaluation judges selected context against declared golden facts/citations and retains scores without a page gate in its runner. Retrieval measurement checks first expected slug rank and can feed an enforcing policy-edit floor. Calibration compares candidate classifier labels to retained reference labels, but stops at candidate metrics. See [EPI-RTE-citation-check](epistemic.md#epi-rte-citation-check), [EPI-RTE-answer-cleanup](epistemic.md#epi-rte-answer-cleanup), [EPI-RTE-wiki-evaluation](epistemic.md#epi-rte-wiki-evaluation), [EPI-RTE-retrieval-measure](epistemic.md#epi-rte-retrieval-measure), [EPI-RTE-filter-calibration](epistemic.md#epi-rte-filter-calibration). None of these criteria licenses claims beyond its checked target, reference validity, context and intended use. There is no observed evidence-consuming acceptance decision here naming a generated factual claim, criterion and intended epistemic use; this is an assessed-route limit, not a whole-system absence.

**Conflict and withdrawal routes change operational reliance without determining factual truth.** See [EPI-RTE-contradiction-scan](epistemic.md#epi-rte-contradiction-scan), [EPI-RTE-conflict-selection](epistemic.md#epi-rte-conflict-selection), [EPI-RTE-conflict-materialization](epistemic.md#epi-rte-conflict-materialization), [EPI-RTE-resolution-revert](epistemic.md#epi-rte-resolution-revert), [EPI-RTE-retraction-monitor](epistemic.md#epi-rte-retraction-monitor), [EPI-RTE-retraction-warning](epistemic.md#epi-rte-retraction-warning), [EPI-RTE-orphan-selection](epistemic.md#epi-rte-orphan-selection), [EPI-RTE-depath-recovery](epistemic.md#epi-rte-depath-recovery). Model contradiction warnings are candidates; weekly driver can write them directly as drafts. Trust/recency policy labels a preferred claim while keeping both; the inspected equal-trust gate does not implement actual recency. A disputes annotation reaches later readers interpretively, not as a line-level ranking/exclusion rule. Public reversals and graph cleanup remove/restore content or annotations, not warrant. Bibliographic retraction flags produce direct/transitive review warnings; they do not automatically repair claims or ban retrieval in the inspected paths. Existing structured-page resolve writes a status/note, not a verified factual adjudication. These counterexamples prevent both a universal acceptance claim and a universal no-withdrawal claim.

**Behavior-shaping guidance is separate from knowledge warrant and from demonstrated improvement.** See [EPI-RTE-filter-correction](epistemic.md#epi-rte-filter-correction), [RT-RTE-policy-distillation](runtime.md#rt-rte-policy-distillation), [RT-RTE-policy-bootstrap](runtime.md#rt-rte-policy-bootstrap), [RT-RTE-policy-edit](runtime.md#rt-rte-policy-edit), [RT-RTE-skill-emission](runtime.md#rt-rte-skill-emission), [RT-RTE-session-reanchor](runtime.md#rt-rte-session-reanchor). Corrected examples can enter future filter prompts; candidate distillation is not live installation; bootstrap can install schema-valid policy directly; policy-edit gates only selected test domains; host skill/snapshot delivery depends on host activation/compliance. Criteria and rationale are inspectable natural-language guidance in symbolic files; inaccessible model weights remain independently unresolved. Inspected inference does not update parameters, but exact provider weights, endpoint changes and internal learning cannot be assessed. Learning, reflection, theory-builder conditions, autonomy and self-improvement are not inferred from retention or generation; retain the separate runtime findings on those policy routes. No new causal benefit is established by this source-only inspection.

Included but unassessed operations in the coverage table leave broader knowledge-production and lifecycle-integration conclusions open. Ordinary backlinks, retained contradiction acts and corpus maps are bookkeeping/use before demonstrated epistemic acceptance, not evidence that accepted new theory was integrated. The report therefore has no single system-wide epistemic verdict.

## Shared records

### Operative objects

#### EPI-OBJ-source-text
Label: Imported source text and metadata

Source-native identity: canonical raw markdown body and mutable bibliographic/frontmatter metadata. Body assertions are natural-language content; source IDs/hash/retraction flags are symbolic inputs to fixed consumers. Substrate: raw/<type>/<id>.md filesystem files and current filter/model prompt strings. Separate from [RT-OBJ-plan](runtime.md#rt-obj-plan) and [RT-OBJ-intent](runtime.md#rt-obj-intent): those are operation envelopes, not retained acquired input. SRC-1 `src/gateway/filter/semantic.py`, `src/gateway/pollers/pubmed_retractions.py`.

> return f"### Frontmatter\n\n```yaml\n{front_yaml}\n```\n\n### Body (truncated)\n\n{body_head}"
> --- `src/gateway/filter/semantic.py`

#### EPI-OBJ-page-text
Label: Wiki and answer assertion text

Source-native identity: natural-language markdown bodies and generated answer text, with symbolic citation tokens interpreted by link/check code. Substrate: canonical wiki files, current AnswerResult and retrieved context strings. Distinct from [RT-OBJ-plan](runtime.md#rt-obj-plan) (candidate update envelope) and [RT-OBJ-intent](runtime.md#rt-obj-intent) (durable queue envelope); this is retained/delivered knowledge content across those mechanisms. It is not a part of exactly one envelope, since direct edits, scans, query and deposits also write it. SRC-1 `src/gateway/ops/answer.py`, `src/gateway/ops/contradiction_sweeper.py`.

>     return AnswerResult(
>         answer=cleaned, sections=sections, source_ids=cited,
>         stripped=stripped, usage=usage,
>     )
> --- `src/gateway/ops/answer.py`

#### EPI-OBJ-eval-results
Label: Evaluator and conflict result records

Source-native identity: EvalResult/EvalRunSummary, EvalReport, CalibrationMetrics, LintFinding and conflict act outputs. Symbolic scores/IDs/status feed fixed program consumers; natural-language reasoning/claims require interpretation. Substrate: current Python values, evaluation YAML/trend CSV, lint JSON/markdown and resolution JSONL. No supplied operative-object counterpart after comparing [RT-OBJ-plan](runtime.md#rt-obj-plan) and [RT-OBJ-intent](runtime.md#rt-obj-intent): these are measurements/diagnoses, not write requests. Material routes below separate their consumers rather than treating all scores as one oracle. SRC-1 `src/gateway/evaluate/runner.py`, `src/gateway/ops/contradiction.py`.

>         "winner": {"source": winner.get("source"), "claim": winner.get("claim"),
>                    "trust": _side_trust(winner)},
>         "loser": {"source": loser.get("source"), "claim": loser.get("claim"),
>                   "trust": _side_trust(loser)},
> --- `src/gateway/ops/contradiction.py`

#### EPI-OBJ-policy-text
Label: Editorial and host guidance text

Source-native identity: inclusion_criteria/exclusion_criteria, example rationale/corrected labels and emitted host/snapshot guidance. Natural-language guidance has interpretive force; symbolic domain/version/threshold fields and labels select/rule program behavior. Substrate: policy/example YAML, generated SKILL.md and requested session-state document. Compared with [RT-RTE-policy-distillation](runtime.md#rt-rte-policy-distillation), [RT-RTE-policy-bootstrap](runtime.md#rt-rte-policy-bootstrap), [RT-RTE-skill-emission](runtime.md#rt-rte-skill-emission), [RT-RTE-session-reanchor](runtime.md#rt-rte-session-reanchor): those are distinct producers/consumers, not the guidance object. Exact generated contents and snapshot existence/use unobserved. SRC-1 `src/gateway/filter/policy.py`.

>         inclusion_criteria=list(data.get("inclusion_criteria", []) or []),
>         exclusion_criteria=list(data.get("exclusion_criteria", []) or []),
> --- `src/gateway/filter/policy.py`

### Routes

#### EPI-RTE-citation-check
Label: Citation-shaped claim checking

Part of: [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship)

This is a material subfunction, not a replacement of its supplied route container.

Plan validators call validate_citation_grounding; code classifies claim-shaped sentences and checks citation presence. Code decides errors/warnings; no human or truth oracle supplies the verdict. Normal strict and draft modes differ. Guidance is the citation heuristic and structural/aggregate exemptions, not source-body entailment. An error can veto strict page admission; draft mode changes it to warning. SRC-1 `src/gateway/validator.py`; implementation layer.

- Immediate return: ValidationResult errors or warnings.
- Later read-back: inapplicable — this check itself retains nothing; its downstream page admission belongs to the containing route.
- Delegated visibility: inapplicable — deterministic checker, not a delegated model.
- Selection predicate: Schema citation_grounded flag and uncited_claims over page body/frontmatter.
- Invalidation or expiry: Recomputed per validation; no semantic endorsement persists.
- Activation or effect: Strict errors can block the containing apply path; draft warnings cannot.
- Evidence limits: SRC-1 `src/gateway/citations.py`: line-level citation membership, sentence length/punctuation and exemptions leave unsupported prose possible. Finalization invokes this check strictly; deposit renderer is a separate path.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>         if draft:
>             result.warnings.append(ve)
>         else:
>             result.errors.append(ve)
> --- `src/gateway/validator.py:587-590`

#### EPI-RTE-answer-cleanup
Label: Unknown citation stripping

Part of: [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer)

This is a material subfunction, not a replacement of its supplied route container.

After model generation, code extracts source IDs from the delivered retrieval block and deletes links to IDs outside that set. Model proposes prose; code decides token deletion without judging facts. Open answering mode has no expected answer oracle. Caller optionally files the surviving answer through draft application; no per-claim approval or rejection is wired in cleanup. SRC-1 `src/gateway/ops/answer.py`; implementation layer.

- Immediate return: Cleaned answer and stripped-ID list.
- Later read-back: Optional draft answer can reach later retrieval, through the containing route.
- Delegated visibility: Answer model sees selected blocks, question and prompt-only source constraint; cleanup sees strings.
- Selection predicate: Regex source IDs in retrieval block, not a claim/source support comparison.
- Invalidation or expiry: Each answer recomputes valid IDs; no continued check of surviving claims.
- Activation or effect: Deletes unknown citation tokens; leaves their prose intact; result returned and optionally filed.
- Evidence limits: No factual acceptance or semantic preservation follows from deleting an attribution. Source-supported counterexample: a valid ID can be attached to an unsupported claim.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>         if sid in valid:
>             return m.group(0)
>         stripped.append(sid)
>         return ""
> --- `src/gateway/ops/answer.py`

#### EPI-RTE-wiki-evaluation
Label: Golden wiki-state judgment

Compared with [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship), [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit) and [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer): no supplied record declares this specific mechanism; related generation/write containers are not the same referent.

CLI/MCP evaluate dispatches runner → wiki_context loader → Sonnet Judge → parsed EvalResults → run YAML/trend CSV/summary. Model judges the selected wiki against caller-maintained golden must_cite/must_assert/must_not_assert and rubric weights; code parses and aggregates. This is bounded reference evaluation, not generation of a new answer. No page-revision or page-admission consumer is implemented in the inspected runner. Oracle correctness and golden provenance are uninspected. SRC-1 `src/gateway/evaluate/runner.py`; implementation layer.

- Immediate return: EvalRunSummary with mean and per-question results.
- Later read-back: Run YAML and trend CSV retain scores for later operator inspection; automatic revision from these files is not established.
- Delegated visibility: Judge sees all selected synthesis bodies, first 20 concept lines, first 15 entity lines, and only synthesis-enumerated raw bodies up to 30,000 chars; longer bodies omitted.
- Selection predicate: Domain goldens, optional limit, domain-tagged pages and synthesizes source IDs.
- Invalidation or expiry: Each run reassembles context; malformed JSON can rescue a numerical score via regex.
- Activation or effect: Records and returns an assessment, not a mandatory acceptance gate for wiki prose.
- Evidence limits: SRC-1 `src/gateway/evaluate/judge.py`, `src/gateway/evaluate/wiki_context.py`: score is trusted from model output, not independently recomputed; no observed evaluation or causal outcome supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>     write_run(summary)
>     append_to_trend(summary)
>     return summary
> --- `src/gateway/evaluate/runner.py`

#### EPI-RTE-retrieval-measure
Label: Golden retrieval measurement

Compared with [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship), [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit) and [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer): no supplied record declares this specific mechanism; related generation/write containers are not the same referent.

CLI eval-retrieval selects FTS authority ranking or grep baseline; evaluator compares first expected slug rank and calculates hit-at-k/MRR. Curated expected slugs are the reference outcomes. Code owns measurement; standalone CLI is advisory, while policy-edit consumes the same FTS metric as a blocking floor. Distinct identity from policy-edit: this is its measurement dependency, not policy replacement. It does not measure the full hybrid section assembly or answer truth. SRC-1 `src/gateway/evaluate/retrieval_eval.py`; implementation layer.

- Immediate return: EvalReport and formatted misses/metrics.
- Later read-back: inapplicable — standalone evaluator retains no report itself; policy-edit can retain the gate result through its containing write/provenance path.
- Delegated visibility: inapplicable — deterministic reference comparison.
- Selection predicate: Golden query/domain and expected slug set, ranked top k.
- Invalidation or expiry: Recomputed from current index; expected labels are not source-truth checks.
- Activation or effect: Standalone report advises; policy-edit gate can reject under its floor.
- Evidence limits: SRC-1 `src/gateway/commit_gate.py`: policy-edit tests current FTS recall, not every effect of the proposed policy. A hit means at least one expected slug was found, not all expected pages.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>         for i, slug in enumerate(ranked, start=1):
>             if slug in g.expect:
>                 best = i
>                 break
> --- `src/gateway/evaluate/retrieval_eval.py`

#### EPI-RTE-filter-calibration
Label: Candidate criterion calibration

Part of: [RT-RTE-policy-distillation](runtime.md#rt-rte-policy-distillation)

This is a material subfunction, not a replacement of its supplied route container.

Distillation optionally invokes score_calibration with proposed inclusion/exclusion criteria. A model classifies a source excerpt; code compares include/exclude against saved calibration labels and computes precision/recall/F1. Candidate metrics are retained with candidate YAML, not used here to install a live policy. Human review/promotion remains declared; readiness routine only recommends distillation. This is bounded label comparison; label accuracy and independence from training examples are not established. SRC-1 `src/gateway/ops/calibration.py`; implementation layer.

- Immediate return: CalibrationMetrics or None for absent/empty set.
- Later read-back: Candidate policy versions retain optional metrics for review; future live deployment unobserved.
- Delegated visibility: Classifier receives proposed criteria and first 1,500 characters of raw file text, including frontmatter when present; missing source becomes source_id text.
- Selection predicate: Calibration entries by domain; include substring decides predicted label.
- Invalidation or expiry: Explicit label addition is idempotent by source ID; metrics recomputed.
- Activation or effect: Annotates a retained candidate; no measured-quality threshold promotes it.
- Evidence limits: SRC-1 `src/gateway/ops/filter_calibrator.py` recommends a command once a domain crosses count threshold; it does not run distillation. This resolves runtime’s locally uninspected calibration implementation, without establishing results.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>         raw = client.call(prompt).strip().lower()
>         predicted = "include" if "include" in raw else "exclude"
> --- `src/gateway/ops/calibration.py`

#### EPI-RTE-contradiction-scan
Label: Candidate contradiction scan

Compared with [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship), [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit) and [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer): no supplied record declares this specific mechanism; related generation/write containers are not the same referent.

Lint/weekly sweep/drift invoke a shared model check: extract claim-shaped sentences by domain, truncate to 280 chars, partition into batches of 80, request at most 12 directly conflicting pairs, parse/check pair indices. Model proposes contradiction and rationale; code removes invalid/duplicate pairs. No external evidence oracle adjudicates which claim is true. Weekly sweep writes a draft synthesis directly; drift stores snapshots and labels disappeared pair keys resolved. Separate from queued deposit conflict selection and from explicit structured-page resolution. SRC-1 `src/gateway/lint/contradictions.py`; implementation layer.

- Immediate return: Warnings/pair candidates; failed calls become warnings; malformed JSON can become empty pairs.
- Later read-back: Weekly draft synthesis reaches later wiki retrieval; drift JSON reaches next comparison and optional weekly digest.
- Delegated visibility: Model receives capped sentence text with page names, not complete source evidence.
- Selection predicate: At least four claims per domain, selected page types, contiguous batches; cross-batch contradictions not compared.
- Invalidation or expiry: Existing domain/week page skips regeneration; daily snapshot replaces same-date output.
- Activation or effect: Reports possible conflicts; weekly driver directly retains them for review without apply_plan; drift does not itself resolve page claims.
- Evidence limits: SRC-1 `src/gateway/ops/contradiction_sweeper.py`, `src/gateway/ops/contradiction_drift.py`: disappeared detector output is not evidence of successful factual repair; no human acceptance trace supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>         "Task: identify pairs of claims that ASSERT CONTRADICTORY FACTS within this",
>         "      domain. A pair must directly conflict on a specific empirical or",
>         "      definitional point — not differ in scope, framing, or context.",
> --- `src/gateway/lint/contradictions.py`

#### EPI-RTE-conflict-selection
Label: Deposit conflict precedence

Part of: [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit)

This is a material subfunction, not a replacement of its supplied route container.

CommitGate extracts first new and existing prefix-matching claim objects for claim_subject; unequal objects invoke auto_resolve. Code proposes the pair and selects winner by source-type trust then lexicographic committed_at. No truth oracle or source evidence assessment decides the conflict. New-side source_type is read from caller-supplied intent.identity; existing side is read/inferred from source page. The rule does not directly consume self-reported numeric trust, but this is weaker than authenticating source category. Normal asynchronous deposit mode needs no per-content human approval. SRC-1 `src/gateway/ops/contradiction.py`; implementation layer.

- Immediate return: Winner/loser resolution act; appended JSONL act.
- Later read-back: Recorded act reaches reversal producer and materialization; both claims remain page content.
- Delegated visibility: inapplicable — deterministic rule; no model evaluator.
- Selection predicate: Entity/concept identity with claim_subject, one write, existing page, prefix extraction and object inequality.
- Invalidation or expiry: Explicit queued reversion can mark act reverted; it is not a new truth check.
- Activation or effect: Labels preference and permits contested-edge materialization; does not delete losing claims.
- Evidence limits: SRC-1 `src/gateway/commit_gate.py`: sends committed_at values old and new, so equal-trust comparison favors old ("old" > "new"), contrary to actual-recency wording. Truth of either claim remains undetermined.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>         ca = str(side_a.get("committed_at", ""))
>         cb = str(side_b.get("committed_at", ""))
>         winner, loser = (side_a, side_b) if ca > cb else (side_b, side_a)
> --- `src/gateway/ops/contradiction.py`

#### EPI-RTE-conflict-materialization
Label: Contested edge materialization

Part of: [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit)

This is a material subfunction, not a replacement of its supplied route container.

Gate consumes the selected loser and appends a Contested section with a disputes link and loser claim, then commits through normal write machinery. Code admits and retains this annotation; both claims remain available. This is operational annotation, not evidence-consuming acceptance of the winner. Numeric trust affects page ranking through source_type/filter_score, but ordinary authored entity/concept pages default neutral; inspected index does not read the resolution act to separately demote the losing line. SRC-1 `src/gateway/commit_gate.py`; implementation layer.

- Immediate return: Rewritten AuthoredIntent enters commit path.
- Later read-back: Contested prose/citation retained in page; act retained separately; later retrieval may supply either claim.
- Delegated visibility: inapplicable — deterministic rendering; future answer model interprets page text.
- Selection predicate: Conflict act loser fields; normal gate commit success required.
- Invalidation or expiry: Queued reversion removes Contested sections and marks act reverted after success.
- Activation or effect: Changes later model-visible context through an interpretive disputes annotation, not a line-level enforcing truth gate.
- Evidence limits: SRC-1 `src/gateway/search_index.py`: source-type page trust is a ranking tiebreaker, never eligibility exclusion. Gate’s losing-claim down-weight wording is not established as claim-specific ranking.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>         loser_src = str((act.get("loser") or {}).get("source") or "")
>         loser_claim = str((act.get("loser") or {}).get("claim") or "")
> --- `src/gateway/commit_gate.py`

#### EPI-RTE-resolution-revert
Label: Conflict annotation withdrawal

Compared with [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship), [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit) and [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer): no supplied record declares this specific mechanism; related generation/write containers are not the same referent.

CLI/MCP revert-resolution queues an act reversal; gate reloads act, scans sorted wiki pages for the first Contested section containing the loser-source disputes token, strips Contested sections, commits and marks act reverted. Caller requests withdrawal; code can veto unknown act/missing matching page. No fact oracle validates the reversal. Matching is by source token, not exact act/page lineage, so several acts citing the same source can be ambiguous. Separate from structured contradiction resolve, which merely writes status/note and can set contested on source pages. SRC-1 `src/gateway/commit_gate.py`; implementation layer.

- Immediate return: Queued receipt, then commit result or dead-letter.
- Later read-back: Edited page and reverted-act status survive; both original claims remain.
- Delegated visibility: inapplicable — code scans retained pages and acts.
- Selection predicate: Named act and first sorted matching loser-source token/Contested page.
- Invalidation or expiry: Successful commit marks act reverted; section stripping can remove several Contested sections.
- Activation or effect: Withdraws annotation from later context; it does not establish the opposing claim.
- Evidence limits: SRC-1 `src/gateway/ops/contradiction.py`: explicit status resolution neither chooses a factual winner nor rewrites their supporting prose. Other automatic reopen detectors were inventoried, not fully traced.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>         result = self._commit_reversal_writes(
>             intent_id, {target_rel: new_content}, [], basis,
>             summary=f"reverted contradiction act {act_id}",
>         )
>         if result.success:
>             contradictions_log.mark_act_reverted(act_id, intent_id)
> --- `src/gateway/commit_gate.py`

#### EPI-RTE-retraction-monitor
Label: PubMed status acquisition

Compared with [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship), [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit) and [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer): no supplied record declares this specific mechanism; related generation/write containers are not the same referent.

Registered pubmed-retractions poller fetches NCBI XML for retained PubMed sources, checks PublicationType/CommentsCorrections substring retraction, and stamps raw frontmatter while preserving body. Program decides a status annotation; external registry supplies evidence, not a direct truth verdict on every source claim. Open maintenance mode uses a 30-day cursor rule and leaves no reset path when later response is non-retracted. Parse failure returns false, not an explicit unknown result. SRC-1 `src/gateway/pollers/pubmed_retractions.py`; implementation layer.

- Immediate return: Counts/errors and retained retracted metadata.
- Later read-back: Raw metadata reaches retracted-citations lint; source bodies stay retained.
- Delegated visibility: inapplicable — deterministic XML checker.
- Selection predicate: PubMed ID, cursor age, broad case-insensitive retraction substrings.
- Invalidation or expiry: No automatic clearing of a retracted flag; cursor controls rechecks.
- Activation or effect: Updates a bibliographic warning input; does not remove source or revoke all downstream claims.
- Evidence limits: XML containing Retraction of Publication also satisfies substring match; detector is broader than checking only retracted-original status. Provider evidence authenticity and individual claims remain outside the check.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>             if retracted and not front.get("retracted"):
>                 front["retracted"] = True
>                 front["retracted_at"] = _now_iso()
>                 new_text = fm.serialize(front, body)
>                 write_atomic(src, new_text)
> --- `src/gateway/pollers/pubmed_retractions.py`

#### EPI-RTE-retraction-warning
Label: Retraction dependency warning

Compared with [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship), [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit) and [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer): no supplied record declares this specific mechanism; related generation/write containers are not the same referent.

Lint collects flagged raw PubMed/arXiv IDs, scans wiki links for direct cites and invokes cascade_detail for transitive synthesizes dependents. Code returns ERROR direct findings and WARNING transitive findings asking review. No automatic claim replacement, deletion or retrieval exclusion follows in this lint function. Human/operator chooses repair; no mandatory acceptance criterion is recorded here. SRC-1 `src/gateway/lint/retracted_citations.py`; implementation layer.

- Immediate return: LintFinding list with source and depth.
- Later read-back: Lint report/operator context can retain findings; inspected function only returns them.
- Delegated visibility: inapplicable — deterministic link/dependency warning.
- Selection predicate: Raw retracted flags, direct source links and transitive dependency helper.
- Invalidation or expiry: Recomputed; flag and linked prose can remain after warnings.
- Activation or effect: Advises review without withdrawing retained prose from answer context.
- Evidence limits: Transitive graph helper implementation was not fully inspected; complete dependency coverage is not claimed. Source-local search of `src/gateway/ops/retrieve.py` and `src/gateway/search_index.py` for retracted/superseded/contested/trust/resolution/disputes found no retracted eligibility test; this is not a negative about every downstream consumer.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>                     message=(
>                         f"page cites retracted source `{source_id}` — "
>                         "review the claim(s) this source supports and remove "
>                         "or replace the citation (QUAL-7)"
>                     ),
> --- `src/gateway/lint/retracted_citations.py`

#### EPI-RTE-orphan-selection
Label: Corpus de-path candidate selection

Compared with [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship), [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit) and [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer): no supplied record declares this specific mechanism; related generation/write containers are not the same referent.

CLI/MCP remediate enumerates wiki pages, skips moc/artifact and any indexed inbound count or recursively referenced provenance decision-basis path, and enqueues a typed depath intent otherwise (dry-run only returns candidates). Program chooses cleanup candidates; no semantic truth evaluator or answer oracle participates. Separate from deposit and authored-page admission: this consumer uses graph reachability, not evidence for claims. Selection occurs before later queue draining. SRC-1 `src/gateway/ops/remediate.py`; implementation layer.

- Immediate return: Candidate paths and skipped reachable paths; live mode queues intents.
- Later read-back: Queue intents reach commit-worker; retained provenance protects pages during later scans.
- Delegated visibility: inapplicable — deterministic graph/index selectors.
- Selection predicate: Zero inbound and not provenance-referenced; exempt page types.
- Invalidation or expiry: Content-addressed enqueue; next scan recomputes eligibility; gate does not recheck reachability in inspected depath helper.
- Activation or effect: Grants delayed removal authority to selected intents, not epistemic rejection.
- Evidence limits: Concurrent new references after selection are not protected by an apply-time eligibility recheck in the inspected helper; no concurrency execution supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>         if counts.get(rel, 0) > 0:
>             # Has inbound links — safe, skip.
>             continue
>         # Zero inbound links. Check provenance reachability.
>         if rel in prov_reachable:
>             skipped_reachable.append(rel)
>             continue
> --- `src/gateway/ops/remediate.py`

#### EPI-RTE-depath-recovery
Label: De-path and recorded restoration

Compared with [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship), [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit) and [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer): no supplied record declares this specific mechanism; related generation/write containers are not the same referent.

Worker/gate depath captures page text, then calls reversal commit machinery to delete; restore-depath producer retrieves latest recorded content from provenance and queues recreation. Missing target/content vetoes. Caller requests recovery; deterministic program applies it, without evaluating source truth. This record is the paired deletion/restoration mechanism, not orphan selection. Reverse-merge is a different exposed reversal: it strips recorded contributed aliases/sections/exact claim lines from the canonical and deletes the tombstone; its plan helper was not fully inspected. SRC-1 `src/gateway/commit_gate.py`; implementation layer.

- Immediate return: Queued receipt then commit/dead-letter result.
- Later read-back: Provenance carries deleted content; restore producer reloads it; recreated page can reenter retrieval.
- Delegated visibility: inapplicable — deterministic persistence/recovery.
- Selection predicate: Typed depath/restore payload with target; restore content supplied from recorded provenance by public producer.
- Invalidation or expiry: Deletion removes canonical file; later restore recreates previous text, not a newly checked proposition.
- Activation or effect: Changes retrievability and retained lineage; not acceptance or factual rehabilitation.
- Evidence limits: SRC-1 `src/gateway/ops/reverse_merge.py`: public restoration is provenance-fed. Low-level typed payload handling does not independently authenticate restored truth. Full reverse-merge lineage/overlap safety remains unassessed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>         return self._commit_reversal_writes(
>             intent_id, {}, [target_rel], basis,
>             summary=f"de-pathed {target_rel}",
>         )
> --- `src/gateway/commit_gate.py`

#### EPI-RTE-filter-correction
Label: Caller label correction

Compared with [RT-RTE-ingest-authorship](runtime.md#rt-rte-ingest-authorship), [RT-RTE-deposit-commit](runtime.md#rt-rte-deposit-commit) and [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer): no supplied record declares this specific mechanism; related generation/write containers are not the same referent.

CLI/MCP/browser filter-correct takes include/exclude and rationale; validates mutable raw-frontmatter diff, stamps user_correction and pins a user-correction example. Caller proposes the label; code vetoes malformed input, unknown source/domain and diff failure. A user-correction name does not authenticate a human caller. Next filter prompt can use selected corrected examples; this is direct editorial decision adaptation, not source-claim acceptance. SRC-1 `src/gateway/ops/filter_correct.py`; implementation layer.

- Immediate return: Corrected result and pinned example.
- Later read-back: Raw correction block/example bank survive and can enter later filter prompts.
- Delegated visibility: Later filter model receives selected examples/rationales, not necessarily this example on every call.
- Selection predicate: Known raw source/domain; explicit binary decision; example selection remains separate.
- Invalidation or expiry: Repeated correction overwrites correction block; raw body unchanged.
- Activation or effect: Changes future editorial guidance through natural-language rationale and binary label; no improved capacity shown.
- Evidence limits: SRC-1 `src/gateway/filter/semantic.py`: model consumes policy plus examples, not a certified truth oracle; correction need not immediately create/delete the existing wiki source page.
- implementation conclusion status: wired
- operation conclusion status: uninspected

>         new_filter["user_correction"] = correction_block
>         front["filter"] = new_filter
> --- `src/gateway/ops/filter_correct.py`

Additional implementation passages for the linked records:

>     ident = dict(identity)
>     ident.setdefault("page_type", payload["page_type"])
>     iid = compute_intent_id(payload, ident, semantics="deposit")
> --- `src/gateway/ops/deposit.py`

>             "committed_at": "old",
> --- `src/gateway/commit_gate.py`

>             "committed_at": "new",
> --- `src/gateway/commit_gate.py`

>             "source_type": str(ident_d.get("source_type", "")),
> --- `src/gateway/commit_gate.py`

>             has_citation = (
>                 bool(_CITATION_LINE_RE.search(raw_line))
>                 or bool(_NLM_CITATION_LINE_RE.search(raw_line))
>                 or _line_cites_via_footnote(raw_line, footnote_map)
>             )
> --- `src/gateway/citations.py`

>     if src_type:
>         trust_val = _trust.server_trust_tier(src_type, filter_score)
>     else:
>         trust_val = _trust.NEUTRAL_TRUST
> --- `src/gateway/search_index.py`

>     key += _W_TRUST * (h.trust - 0.5)
>     return key
> --- `src/gateway/search_index.py`

>     page = _build_page(domain, week, all_findings)
>     out_path.parent.mkdir(parents=True, exist_ok=True)
>     with file_lock(_LOCK_NAME):
>         write_atomic(out_path, page)
> --- `src/gateway/ops/contradiction_sweeper.py`

>     new = [x for x in current if _finding_key(x) not in prev_keys]
>     resolved = [x for x in previous if _finding_key(x) not in curr_keys]
>     return new, resolved
> --- `src/gateway/ops/contradiction_drift.py`

>                     if len(body) <= max_body_chars:
>                         bodies[sid] = body
> --- `src/gateway/evaluate/wiki_context.py`

>         # RULE 2 (authority): same-kind + alias/canonical exact-or-normalized match → merge.
>         if id_names & cand_names:
>             return Verdict("merge", c.slug, "alias-canonical-exact-match", basis)
> --- `src/gateway/dedup.py`

>     # Skip any prose preamble before the first `{`. Sonnet sometimes emits
>     # "Here is the evaluation:\n\n{...}" despite the strict-output instruction.
> --- `src/gateway/evaluate/judge.py`

>             if predicted == "include":
>                 fp += 1
>             else:
>                 fn += 1
> --- `src/gateway/ops/calibration.py`

### Claims

#### EPI-CLM-retrieval-grounding
Label: Bounded cited retrieval promise

Claimed operation: ranked bounded context with preserved citations grounds later answering. SRC-1 `README.md`; doctrine/design. Distinct from [RT-CLM-gateway-only](runtime.md#rt-clm-gateway-only): this claim concerns read delivery, not write discipline.

> 3. `wiki retrieve "<question>" [--domain X]` — the default grounding call: a ranked, bounded context block of the most relevant sections, citations preserved. Prefer over reading `index.md` or grepping.
> --- `README.md`

#### EPI-CLM-answer-grounding
Label: Grounded local synthesis promise

Claimed operation: answer performs grounded synthesis and strips ungrounded citations. SRC-1 `README.md`; doctrine/design. Distinct from [RT-CLM-gateway-only](runtime.md#rt-clm-gateway-only) and [EPI-CLM-retrieval-grounding](epistemic.md#epi-clm-retrieval-grounding): this concerns newly returned answer prose after model inference.

> | `wiki answer "<question>" [--domain X] [--file]` | Retrieve + one grounded Claude call; cites only retrieved sources (ungrounded citations stripped). NotebookLM-independent. `--file` drafts a synthesis page |
> --- `README.md`

#### EPI-CLM-citation-provenance
Label: Opaque corpus-token provenance claim

Claimed operation: NLM corpus tokens count as valid grounding and prove provenance to the page’s corpus, despite no local UUID existence verification. SRC-1 `WIKI.md`; doctrine/design. Distinct from [RT-CLM-gateway-only](runtime.md#rt-clm-gateway-only) and [EPI-CLM-answer-grounding](epistemic.md#epi-clm-answer-grounding): this claims token/corpus provenance rather than local answer ID membership.

> **NotebookLM-internal corpus citations: `[[nlm:<uuid>]]`.** NLM-authored synthesis pages (those carrying `nlm_notebook_id:` in frontmatter) frequently cite the corpus via chunk-level UUIDs that NotebookLM emits inline (e.g., `[[nlm:a17f0b4f-ba96-46b0-b4e1-6be759219e89]]`). These are accepted as valid grounding by the validator alongside `[[sources/<id>]]` — the citation maps into the page's NLM corpus, not a wiki source page. The validator does not verify UUID existence (that would require live NLM API access; out of scope for the in-page validator). Treat NLM citations as opaque grounding tokens — they prove provenance to the corpus listed in `nlm_notebook_id`, but do not by themselves create wiki backlinks.
> --- `WIKI.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; route-specific consumer/channel/force/horizon assessments are in the ledger, and supplied prompt/host paths remain see [RT-BAP-authorship-prompt](runtime.md#rt-bap-authorship-prompt), [RT-BAP-domain-skill](runtime.md#rt-bap-domain-skill), [RT-BAP-session-state](runtime.md#rt-bap-session-state).
