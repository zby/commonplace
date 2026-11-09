---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Stigmergy epistemic routes: source fidelity, filing authority, identity evidence, answer verification and release evaluation."
run-id: AAS-2026-11-08-stigmergy-2de42cc04367-01
reviewed-boundary: "0ca8bb1963ad9cf43eaf2c18329998023a9caa4f"
---

# Stigmergy epistemic report

## Source-and-claim boundary

The question is how captures become relied-on wiki content and answers, what checks license that reliance, and what later consumers do with their results. The functional boundary, external exclusions and frozen source identity are those of [boundary](boundary.md#boundary-and-evidence); source evidence is SRC-1 in its [Source register](boundary.md#source-register). The checkout HEAD was checked against that pin. This report adds implementation and doctrine reads at the same revision. It neither executed Stigmergy nor called a provider.

The system's consequential claims are [RT-CLM-scoped-knowledge](runtime.md#rt-clm-scoped-knowledge), [EPI-CLM-verified-answer](#epi-clm-verified-answer), [EPI-CLM-self-healing](#epi-clm-self-healing), [EPI-CLM-quality-measures](#epi-clm-quality-measures) and [EPI-CLM-parity-release](#epi-clm-parity-release). These claims concern different targets; a citation verifier, graph linter and release comparison are not interchangeable evaluators.

### Coverage

“Direct” means source text inspected for this member; “supplied” means the handed runtime's records/account. Available but unread paths are not access gaps.

| Entry point or operation | SRC-1 path | Coverage and record |
|---|---|---|
| Installed CLI dispatch | `pyproject.toml` | Direct: index, server, bridge, librarian, boot, credential, Slack and admin entry points. Runtime responsibilities: see [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing), [RT-RTE-index-convergence](runtime.md#rt-rte-index-convergence), [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission). Boot/credential internals uninspected here: no global credential-isolation conclusion. |
| MCP tools and bridge | `src/stigmergy/server/mcp_server.py`; `src/stigmergy/bridge/server.py` | Direct server registration and bridge registration search: search, read, list, describe, ask, submit, submissions, delete. Raw retrieval is not answer verification. Supplied bridge acquisition: [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing). |
| Capture bytes, readable source, OCR | `src/stigmergy/capture/extraction.py`; `src/stigmergy/capture/vision.py`; `src/stigmergy/knowledge/writer.py` | Direct dispatch, UTF-8, extraction entry and OCR; [EPI-RTE-evidence-extraction](#epi-rte-evidence-extraction). PDF/Office/Slack parser bodies not fully inspected: semantic fidelity for those formats remains unassessed. Original byte admission supplied by [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing). |
| Filing and source/candidate guidance | `src/stigmergy/knowledge/writer.py`; `src/stigmergy/knowledge/librarian_skill.md` | Direct capture, plan application, preservation, contradiction, garden and deletion code; [EPI-RTE-filing-transform](#epi-rte-filing-transform), [EPI-RTE-filing-check](#epi-rte-filing-check), [EPI-RTE-filing-retention](#epi-rte-filing-retention), [EPI-RTE-contradiction-disposition](#epi-rte-contradiction-disposition). |
| Alias curation | `src/stigmergy/knowledge/aliases.py` | Direct complete file and writer call sites; [EPI-RTE-alias-judgment](#epi-rte-alias-judgment), [EPI-RTE-alias-admission](#epi-rte-alias-admission). A material part not separately individuated by runtime. |
| Entity maintenance | `src/stigmergy/knowledge/writer.py`; `src/stigmergy/entities/service.py` | Direct entity dispatch, merge, source-evidence grammar; [EPI-RTE-merge-check](#epi-rte-merge-check), [EPI-RTE-entity-merge](#epi-rte-entity-merge). Adds the explicit ENTITY operation to runtime's selected routes; no supplied record requires supersession. Rename/delete also visible in writer. |
| Lint and trusted authorship | `src/stigmergy/knowledge/lint.py`; `src/stigmergy/knowledge/trust.py` | Direct complete files; structural, ACL, source-reference and identity-string criteria, not source-truth or semantic-entailment oracles. Runtime publication consumers: [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing), [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission). Universal hook enforcement unestablished. |
| Garden, recompile, deletion, erasure, index | `src/stigmergy/knowledge/writer.py`; `src/stigmergy/librarian/worker.py` | Direct garden/deletion/reference-sweep and dispatcher; worker erasure dispatch search. Supplied recompile, erasure and index: [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission), [RT-RTE-index-convergence](runtime.md#rt-rte-index-convergence); [EPI-RTE-evidence-withdrawal](#epi-rte-evidence-withdrawal) narrows withdrawal to inspected sweep. Reset and full erasure internals uninspected: cannot establish complete removal from every copy. |
| Layer assignment and scoped readers, Slack/admin/web | `src/stigmergy/server/routing.py`; `src/stigmergy/server/service.py`; `src/stigmergy/slack/mention.py`; `src/stigmergy/admin/routes.py` | Supplied [RT-RTE-layer-routing](runtime.md#rt-rte-layer-routing), [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer), runtime account. Not independently re-audited end to end; no all-channel confidentiality conclusion. |
| Answer proposal, checks, correction, refusal | `src/stigmergy/answer/synthesize.py`; `src/stigmergy/answer/verify_answer.py`; `src/stigmergy/answer/numbers.py`; `src/stigmergy/answer/service.py` | Direct schemas, evidence ledger, instructions, complete verifier/numbers and AnswerBrain renderers, scoped raw-head fetch, service gate search; [EPI-RTE-answer-check](#epi-rte-answer-check), [EPI-RTE-answer-disposition](#epi-rte-answer-disposition); supplied budgets and recovery in [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer). |
| QA and other evaluations | `evals/run_qa.py`; `evals/README.md` | Direct runner construction, scorer, output/history and documentation; [EPI-RTE-qa-evaluation](#epi-rte-qa-evaluation). Retrieval/graph/alias/routing runners beyond documented contracts uninspected; no comprehensive evaluation-quality verdict. |
| Filing parity and release | `evals/filing/README.md`; `evals/filing/parity.py`; `scripts/deploy_staging.sh` | Direct gate orchestration, comparison/rejection branch and complete deploy script; [EPI-RTE-release-evaluation](#epi-rte-release-evaluation), [EPI-RTE-release-admission](#epi-rte-release-admission). Full replay/helper audit and external evidence bundle uninspected. Contributor/CI route supplied by [RT-RTE-product-admission](runtime.md#rt-rte-product-admission). |

No live tenant corpus or authenticated production trace was supplied. Thus source preservation and model compliance are implemented/requested properties, not observed factual fidelity. The actual content of provider processing is not determinable; model fixity limits are separately recorded in [RT-CMP-librarian-model](runtime.md#rt-cmp-librarian-model), [RT-CMP-ocr-model](runtime.md#rt-cmp-ocr-model), [RT-CMP-layer-model](runtime.md#rt-cmp-layer-model) and [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model). No parameter-training route is established by those clients. Uninspected included operations above preclude a system-complete negative about all possible evaluators or knowledge production.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-readable-source](#epi-obj-readable-source) | Source assertions and machine transcription | see record | SRC-1, `src/stigmergy/capture/extraction.py` | Byte identity is not factual truth; transcription fidelity unknown. |
| [RT-OBJ-filing-plan](runtime.md#rt-obj-filing-plan) | Proposed page propositions, relationships and conflicts | see record | SRC-1, `src/stigmergy/knowledge/librarian_skill.md` | Model request does not establish its compliance or entailment. |
| [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | Dated facts, states, concepts and project synthesis | see record | SRC-1, `src/stigmergy/knowledge/writer.py` | Local attribution can survive while a new statement remains unsupported. |
| [EPI-OBJ-contradictions](#epi-obj-contradictions) | Competing sourced claims and conflict explanation | see record | SRC-1, `src/stigmergy/knowledge/writer.py` | Recording a conflict is not adjudicating truth. |
| [EPI-OBJ-entity-aliases](#epi-obj-entity-aliases) | Variant names the same entity | see record | SRC-1, `src/stigmergy/knowledge/aliases.py` | Distinguish model probability from verified identity. |
| [EPI-OBJ-merge-evidence](#epi-obj-merge-evidence) | Selected names denote the same entity | see record | SRC-1, `src/stigmergy/entities/service.py` | Restricted assertion grammar; source itself can be false. |
| [RT-OBJ-synthesis-context](runtime.md#rt-obj-synthesis-context) | Retrieved source/wiki assertions; query/window bookkeeping is symbolic non-claim state | see record | SRC-1, `src/stigmergy/answer/synthesize.py` | Quote checks use freshly fetched scoped page heads plus recorded fragment numbers, not a snapshot of delivered tool text. |
| [EPI-OBJ-answer-output](#epi-obj-answer-output) | Answer propositions, citation quotations, confidence label; refusal flag is a disposition request | see record | SRC-1, `src/stigmergy/answer/synthesize.py` | “Verified” checks token/quote conditions, not all propositions. |
| [EPI-OBJ-qa-results](#epi-obj-qa-results) | Golden-case outcomes and aggregate scores | see record | SRC-1, `evals/run_qa.py` | Reporting is not runtime semantic acceptance. |
| [EPI-OBJ-parity-artifact](#epi-obj-parity-artifact) | Recorded filing outputs, provenance and comparative editorial judgments | see record | SRC-1, `evals/filing/parity.py` | No actual passing release packet inspected. |
| [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model) | Individual truth-apt propositions not determinable in dense state | see record | SRC-1, `src/stigmergy/index/backends/embedder.py` | Ranking authority does not certify content. |
| [RT-CMP-librarian-model](runtime.md#rt-cmp-librarian-model), [RT-CMP-ocr-model](runtime.md#rt-cmp-ocr-model), [RT-CMP-layer-model](runtime.md#rt-cmp-layer-model) | Individual propositions in remote weights not determinable | see records | SRC-1, `src/stigmergy/kernel/llm.py` | No access to internal representations, training history or immutable weight versions. |

## Authority-route ledger

Fields owned by supplied records say “see”; the additional distinctions here concern epistemic license. All new route declarations below have implementation status wired and operation status uninspected. “Result” therefore means possible code result, not an observed run.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-RTE-evidence-extraction](#epi-rte-evidence-extraction) | content transformation | implemented | [EPI-OBJ-readable-source](#epi-obj-readable-source) | truth-apt transformation: acquisition/import | Original bytes to readable source | Format dispatch; UTF-8 decode or parser/OCR | Capture filing | Readable text or extraction rejection | Source supplied to planner | Original-source warrant unknown; UTF-8 preserves supplied text, not its truth; OCR fidelity unverified | Allows readable evidence to enter filing | Writer → planner source input; permissive data supply; current/later filing | SRC-1, `src/stigmergy/capture/extraction.py` | none | none | Operation and benefit unobserved. |
| [EPI-RTE-filing-transform](#epi-rte-filing-transform) | content transformation | implemented | [RT-OBJ-filing-plan](runtime.md#rt-obj-filing-plan) | truth-apt transformation: indeterminate | Evidence/context to wiki proposal | Librarian model under skill; no semantic answer oracle | Before mutation | Proposed synthesis and relations | Advisory until writer gates | Requested source-backed reshaping; entailment versus conjecture cannot be classified without candidate/input pairs | Chooses proposed creates/updates/deletes and conflicts | Planner → writer via typed FilingPlan; advisory; this write | SRC-1, `src/stigmergy/knowledge/librarian_skill.md` | none | none | Operation and benefit unobserved. |
| [EPI-RTE-filing-check](#epi-rte-filing-check) | check/evidence production | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: entailed derivation | Page/graph contract and old cited-block preservation | Deterministic writer/lint; finite text/ACL/reference domain | Feeds filing correction/veto | Violation set, missing block or clean | Feeds correction/veto | Derives contract compliance from parsed files; not truth of sourced assertion or semantic support | Writer/linter → capture gate; enforcing; one filing operation | Writer/linter → capture/garden gate; enforcing; one operation | SRC-1, `src/stigmergy/knowledge/lint.py` | [EPI-CLM-self-healing](#epi-clm-self-healing) | none | Operation and benefit unobserved. |
| [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing) | disposition/acceptance | implemented | [RT-OBJ-filing-plan](runtime.md#rt-obj-filing-plan) | no content change | Whole or individual proposed mutation | see [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing) | see [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing) | see [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing) | see [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing) | Admission under structural criteria; not evidence-consuming semantic acceptance of every proposition | see [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing) | see [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing) | SRC-1, `src/stigmergy/knowledge/writer.py` | [RT-CLM-scoped-knowledge](runtime.md#rt-clm-scoped-knowledge) | none | Operation and benefit unobserved. |
| [EPI-RTE-filing-retention](#epi-rte-filing-retention) | retention | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Passed pages and immutable source to Git | Writer publication gate/lease, not independent factual evaluator | After gates; source-only fallback allowed | Committed pages/source; change record | Enforcing publication | Retains candidates and provenance; retention precedes any unestablished semantic acceptance | Makes content eligible for indexing and later context | Git/index → later filing/answer; permissive evidence supply; later requests | SRC-1, `src/stigmergy/knowledge/writer.py` | none | none | Operation and benefit unobserved. |
| [EPI-RTE-contradiction-disposition](#epi-rte-contradiction-disposition) | disposition/acceptance | implemented | [EPI-OBJ-contradictions](#epi-obj-contradictions) | no content change | Proposed conflict or named resolution | Model proposes; writer enforces evidence-path/ACL/target/update contracts; explicit master for resolution | Capture plan application | Persist conflict; retain existing conflict; remove named one only after accepted page update | Enforcing preservation/removal rule | License is recorded competing claims or authorized resolution, not independently settled truth | Blocks silent marker deletion and unrelated resolution | Writer → Markdown conflicts → later readers/planners; enforcing storage rule then advisory evidence; later captures/questions | SRC-1, `src/stigmergy/knowledge/writer.py` | none | none | Operation and benefit unobserved. |
| [EPI-RTE-alias-judgment](#epi-rte-alias-judgment) | check/evidence production | implemented | [EPI-OBJ-entity-aliases](#epi-obj-entity-aliases) | no content change | Variant names same entity rather than role/product/part | Typed decision model; page summary/type/aliases and link sentence | Capture/garden alias step within cap/window | Alias probability or failure | Advisory probability to threshold | Model judgment within supplied context; no reference answer in live path | Feeds accept/reject threshold | Classifier → alias recorder; advisory; current alias step | SRC-1, `src/stigmergy/knowledge/aliases.py` | none | none | Operation and benefit unobserved. |
| [EPI-RTE-alias-admission](#epi-rte-alias-admission) | disposition/acceptance | implemented | [EPI-OBJ-entity-aliases](#epi-obj-entity-aliases) | no content change | Candidate alias for later name resolution | Code accepts probability ≥0.75 after eligibility filters; no per-alias human approval | After judgment | Accepted/rejected/skipped candidate | Enforcing threshold; accepted names written | Operational acceptance for entity lookup, scope is eligible variant; truth reliability unmeasured | Updates entity name metadata or leaves it unchanged | Recorder → entity page aliases → later lookup; permissive resolution; subsequent indexed reads | SRC-1, `src/stigmergy/knowledge/aliases.py` | none | none | Operation and benefit unobserved. |
| [EPI-RTE-alias-admission](#epi-rte-alias-admission) | lifecycle integration | implemented | [EPI-OBJ-entity-aliases](#epi-obj-entity-aliases) | truth-apt transformation: indeterminate | Accepted name mapping to entity metadata | Threshold acceptance plus guarded writes; rollback writes on exception | After alias acceptance | New persisted name association | Enforcing metadata write; downstream ranking/resolution | Integrates accepted mapping for use; no independent identity proof | Changes which page can answer to a name | Entity page/index → readers and filing context; selection; later operations | SRC-1, `src/stigmergy/knowledge/aliases.py` | none | none | Operation and benefit unobserved. |
| [EPI-RTE-merge-check](#epi-rte-merge-check) | check/evidence production | implemented | [EPI-OBJ-merge-evidence](#epi-obj-merge-evidence) | truth-apt transformation: entailed derivation | Selected pages equated by quoted source assertion | Code checks source body occurrence and unambiguous restricted identity grammar; same type/ACL | Master-requested entity merge | Raise or pass | Enforcing precondition to merge | Derives syntactic source-backed equivalence under grammar, conditional on source truth and encoding; not independent world identity | Blocks absent/ambiguous assertion or incompatible pages | Entity service → merge executor; enforcing; current merge | SRC-1, `src/stigmergy/entities/service.py` | none | none | Operation and benefit unobserved. |
| [EPI-RTE-entity-merge](#epi-rte-entity-merge) | lifecycle integration | implemented | [EPI-OBJ-merge-evidence](#epi-obj-merge-evidence) | truth-apt transformation: non-ampliative reshaping | Accepted identity assertion to unified graph | Code after merge check; actor chooses first canonical page | After evidence validation | Concatenate prior bodies, union aliases/sources, rewrite links, remove duplicate pages | Enforcing graph mutation after writer gates | Operational identity acceptance for merging these pages; premises remain imported | Consolidates lookup and incoming links | Entity service → Git/index → later readers; enforcing consolidation then selection; later requests | SRC-1, `src/stigmergy/entities/service.py` | none | none | Operation and benefit unobserved. |
| [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer) | content transformation | implemented | [EPI-OBJ-answer-output](#epi-obj-answer-output) | truth-apt transformation: indeterminate | Gathered evidence to answer draft | see [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer) | see [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer) | see [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer) | see [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer) | Model requested to answer only from evidence; no established entailment of actual draft | see [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer) | see [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer) | SRC-1, `src/stigmergy/answer/synthesize.py` | [EPI-CLM-verified-answer](#epi-clm-verified-answer) | none | Operation and benefit unobserved. |
| [EPI-RTE-answer-check](#epi-rte-answer-check) | check/evidence production | implemented | [EPI-OBJ-answer-output](#epi-obj-answer-output) | truth-apt transformation: entailed derivation | Figures in recorded tool text; citation occurrence in refetched scoped heads and recorded fragment windows | Deterministic numbers/quote normalizers, page membership and problem counting | After draft and bounded retry/completion | verified / partial / failed plus problem lists | Consumed by strict gate | License: figures occur in recorded tool evidence; quotes occur in refetched scoped page content, not necessarily delivered tool text; neither entails answer support or source truth | Determines retry and ship rank | Verifier → AnswerService; enforcing via separate disposition; current answer | SRC-1, `src/stigmergy/answer/verify_answer.py` | [EPI-CLM-verified-answer](#epi-clm-verified-answer) | Broader reading of verified is unsupported | Operation and benefit unobserved. |
| [EPI-RTE-answer-disposition](#epi-rte-answer-disposition) | disposition/acceptance | implemented | [EPI-OBJ-answer-output](#epi-obj-answer-output) | no content change | Draft eligible to ship or be withheld | Service scans answer and quote figures; any missing figure or failed verdict suppresses; lone citation defect may ship partial | After verifier; completion requires verified | Answer/partial or server-composed refusal; retry only when suppression would occur | Enforcing output gate | Operational acceptance for returning this answer under occurrence criteria; not factual acceptance of every proposition | Replaces failed drafts with refusal; higher-ranked correction can win | AnswerService → MCP/Slack caller; enforcing dispatch then advisory answer; this question | SRC-1, `src/stigmergy/answer/service.py` | [EPI-CLM-verified-answer](#epi-clm-verified-answer) | Partial is intentionally shippable | Operation and benefit unobserved. |
| [RT-RTE-index-convergence](runtime.md#rt-rte-index-convergence) | operational admission/selection/consumption | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: non-ampliative reshaping | Committed corpus to searchable representations | see [RT-RTE-index-convergence](runtime.md#rt-rte-index-convergence) | see [RT-RTE-index-convergence](runtime.md#rt-rte-index-convergence) | see [RT-RTE-index-convergence](runtime.md#rt-rte-index-convergence) | see [RT-RTE-index-convergence](runtime.md#rt-rte-index-convergence) | Searchable presence/ranking is not endorsement; embeddings may change relevance, not establish truth | see [RT-RTE-index-convergence](runtime.md#rt-rte-index-convergence) | see [RT-RTE-index-convergence](runtime.md#rt-rte-index-convergence) | SRC-1, `src/stigmergy/index/build.py` | none | none | Operation and benefit unobserved. |
| [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission) | disposition/acceptance | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Garden repair / recompiled pages | see [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission) | see [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission) | see [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission) | see [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission) | Garden clean means no remaining defined violations; recompile is regeneration, not independent truth verification | see [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission) | see [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission) | SRC-1, `src/stigmergy/knowledge/writer.py` | [EPI-CLM-self-healing](#epi-clm-self-healing) | none | Operation and benefit unobserved. |
| [EPI-RTE-evidence-withdrawal](#epi-rte-evidence-withdrawal) | lineage/freshness/recovery | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: non-ampliative reshaping | Explicit deleted source/page to dependent references | Authorized writer deletion; deterministic scope/reference sweep and introduced-lint gate | On explicit delete/related sweep | Remove citing units/conflicts/source metadata; unlink dead links; delete empty pages | Enforcing managed corpus withdrawal | Removal follows evidence availability, not a verdict that a proposition is false | Prevents removed managed units reaching later reads after index convergence | Writer → Git → reader index; enforcing managed retention; subsequent requests | SRC-1, `src/stigmergy/knowledge/writer.py` | [RT-CLM-scoped-knowledge](runtime.md#rt-clm-scoped-knowledge) | Immutability is ordinary-path only | No global purge guarantee or automatic restoration established. |
| [EPI-RTE-qa-evaluation](#epi-rte-qa-evaluation) | check/evidence production | implemented | [EPI-OBJ-qa-results](#epi-obj-qa-results) | truth-apt transformation: entailed derivation | Answers to selected golden cases, not arbitrary factual answers | Golden expected text/numbers/pages, refusal kinds or enumeration sets; deterministic scorer | Optional QA runner; fixed corpus/scopes | Per-case pass and aggregate metrics/history | Reporting; return nonzero on incomplete run, not each quality miss | Defined metric on cases; disambiguation can pass misattributed prose; no broad factual correctness or mechanism attribution | Informs operator comparisons; this runner does not revise runtime automatically | Runner → report/history → operator; advisory; evaluation/release decisions | SRC-1, `evals/run_qa.py` | [EPI-CLM-quality-measures](#epi-clm-quality-measures) | none | Operation and benefit unobserved. |
| [EPI-RTE-release-evaluation](#epi-rte-release-evaluation) | check/evidence production | implemented | [EPI-OBJ-parity-artifact](#epi-obj-parity-artifact) | truth-apt transformation: entailed derivation | Candidate configuration and recorded filing outputs against production/fixtures | Parity orchestration, replay helpers and blind-review bundle; trusted operator supplies reviewer evidence | Explicit release evaluation | Pass/fail and reasons; candidate regressions must not exceed production | Feeds deploy gate | Evidence consistency and comparative quality for named cases/configurations; not reviewer authentication or universal fidelity | Allows or denies guarded deployment in next route | Parity validator → deploy script; enforcing criterion; candidate release | SRC-1, `evals/filing/parity.py` | [EPI-CLM-parity-release](#epi-clm-parity-release) | Selected implementation inspected, full helper audit not performed | No inspected terminal real release packet; no authenticated exercised comparison. |
| [EPI-RTE-release-admission](#epi-rte-release-admission) | disposition/acceptance | implemented | [EPI-OBJ-parity-artifact](#epi-obj-parity-artifact) | no content change | Candidate image eligible for staging deploy | Clean checkout plus passing parity exit; explicit STIGMERGY_PARITY_GATE=off bypass | Before fly deploy | Exit on failure or invoke deployment | Enforcing only through guarded entrypoint unless bypassed | Release acceptance for configured candidate/cases; does not certify every later capture | Blocks or permits replacement of deployed code/skill | Deploy script → Fly; permissive gate; future installed requests | SRC-1, `scripts/deploy_staging.sh` | [EPI-CLM-parity-release](#epi-clm-parity-release) | Operator bypass is explicit | Actual installation, use and benefit unobserved. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-scoped-knowledge](runtime.md#rt-clm-scoped-knowledge) | see record | SRC-1, `README.md`; doctrine/design | see record | [RT-RTE-layer-routing](runtime.md#rt-rte-layer-routing), [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer), [EPI-RTE-evidence-withdrawal](#epi-rte-evidence-withdrawal) | No inspected production trace | No independent isolation or benefit experiment | Code-mediated scope and ordinary-path source protection | Explicit deletion/erasure narrows immutable; external contracts still matter. |
| [EPI-CLM-verified-answer](#epi-clm-verified-answer) | see record | SRC-1, `README.md`; doctrine/design | see record | [EPI-RTE-answer-check](#epi-rte-answer-check), [EPI-RTE-answer-disposition](#epi-rte-answer-disposition) | No answer run supplied | Source-traced counterexamples below; occurrence checks establish neither proposition attribution nor prior tool delivery of each quote | Defined citation/figure gate with correction/refusal | Broad factual or delivered-evidence meanings of “verified answer” exceed check domain; partial answers intentionally ship. |
| [EPI-CLM-self-healing](#epi-clm-self-healing) | see record | SRC-1, `README.md`; doctrine/design | see record | [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission), [EPI-RTE-filing-check](#epi-rte-filing-check) | No repair trace | Lint cleanliness is not semantic accuracy or improved future capacity | Scheduled repair route can reject dirty output | Factual healing, reliable compliance and successful improvement not established. |
| [EPI-CLM-quality-measures](#epi-clm-quality-measures) | see record | SRC-1, `README.md`; reported operation | see record | [EPI-RTE-qa-evaluation](#epi-rte-qa-evaluation) | Attributed latest-run summary only; no replayed/authenticated trace used | Golden-case proxies, selected scopes and permissive scorer bound results; no component effect inferred | Metrics have inspectable finite-domain definitions | Groundedness 1.00 is not proof of semantic grounding of all future answers. |
| [EPI-CLM-parity-release](#epi-clm-parity-release) | see record | SRC-1, `evals/filing/README.md`; doctrine/design | see record | [EPI-RTE-release-evaluation](#epi-rte-release-evaluation), [EPI-RTE-release-admission](#epi-rte-release-admission) | No terminal evidence bundle inspected | Candidate-vs-production review is configuration-level; no independent component variation | Source supports a guarded release criterion with explicit bypass | No proof this revision passed it, no reviewer authenticity guarantee and no measured downstream benefit. |

## Bounded conclusion

**Content can acquire operational authority before semantic acceptance.** Captures import assertions of unknown source warrant. UTF-8 decoding preserves valid supplied text; OCR asks for faithful transcription and marks its provenance, but does not independently compare its reading with ground truth. Filing requests sourced factual synthesis and retains linked Markdown after structural checks. Those checks enforce page contracts, ACL flow, existing attribution and cited-text preservation; they do not determine whether each new sentence follows from its source. See [EPI-RTE-evidence-extraction](#epi-rte-evidence-extraction), [EPI-RTE-filing-transform](#epi-rte-filing-transform), [EPI-RTE-filing-check](#epi-rte-filing-check) and [EPI-RTE-filing-retention](#epi-rte-filing-retention). Uninspected concrete production input/output pairs leave reshaping, entailed derivation and ampliative conjecture unresolved for actual wiki sentences. No produced accepted ampliative claim is established merely by publication.

**There are content-specific checks beyond syntax.** The alias classifier judges the proposition that a variant denotes the same entity rather than its role/product/part. Software accepts its probability at 0.75 for later name lookup, then integrates the mapping into metadata; model probability is not a reference oracle. Explicit entity merge is a different route: a source assertion must occur and equate every selected page under a restricted grammar before code combines bodies, aliases and links. This is evidence-consuming acceptance for a bounded identity-maintenance use, conditional on imported source truth and the adequacy of the encoding. It is not a proof of world identity. See [EPI-RTE-alias-judgment](#epi-rte-alias-judgment), [EPI-RTE-alias-admission](#epi-rte-alias-admission), [EPI-RTE-merge-check](#epi-rte-merge-check) and [EPI-RTE-entity-merge](#epi-rte-entity-merge). This explicit merge check is a counterexample to an unqualified “only syntactic checks” verdict.

**Answer verification is narrower than semantic support.** For a concrete source-code deduction, suppose a surfaced page body is “Aurora remains a draft.”, a draft answer is “Aurora is signed.”, and its sole citation quotes “Aurora remains a draft.” from that same surfaced path. In `src/stigmergy/answer/verify_answer.py`, quote normalization leaves the quote as an occurring substring; there are no numerical tokens for `src/stigmergy/answer/numbers.py` to reject; citations are nonempty, so the problem count is zero and verdict is verified. The strict gate in `src/stigmergy/answer/service.py` then has neither figure problems nor a failed verdict to suppress. This hypothetical is traced through implementation, not an executed model example. It refutes semantic-entailment interpretation while preserving the scoped quote-occurrence guarantee. A separate implementation branch also refutes a stronger delivered-evidence interpretation: suppose list_pages returns an Aurora path, title and summary without the sentence “Aurora remains a draft.”, while that sentence occurs elsewhere in its scoped page head. Listing records the path as surfaced. A non-refused AnswerOutput can carry that sentence as its citation quote and a nonnumeric answer. `page_as_read` calls AnswerBrain.get_page, which refetches the scoped head through fetch_page_raw rather than checking a snapshot of the listing text. The quote therefore passes occurrence checking; no figures exist for the separate recorded-tool-evidence figure gate to veto, so it can ship verified. No actual model production of this draft is asserted. Fragment numbers constrain appended fragment text, but do not require prior delivery of the head. The normalization also deliberately drops short struck spans on the page side; its documented 200-character bound leaves longer retractions quotable. Single bare digits are skipped as list markers, and numerical pooling checks values across evidence rather than their attribution to an entity or period. See [EPI-RTE-answer-check](#epi-rte-answer-check) and [EPI-RTE-answer-disposition](#epi-rte-answer-disposition). A non-refusal with one citation-only problem may ship partial; budget-completion uses a stricter verified-only branch.

**Conflicts, withdrawal and maintenance change later reliance without globally proving truth.** On capture filing, the model is instructed to retain unresolved conflicting claims; that route's writer code preserves conflict records and permits only the named master-authorized resolution after an accepted page update. This is not an invariant of every maintenance transformation: garden's separate repair-body replacement is governed by preservation guidance and lint/projection/diff/ACL gates, not the capture-body preservation comparison; no actual garden loss is established. Source deletion instead removes dependent citing units and conflicts, rewrites dead links and deletes emptied pages. These are different reasons for changing the managed corpus. Garden repairs defined violations; recompile regenerates from sources. None is a blanket mechanism for validating every statement. See [EPI-RTE-contradiction-disposition](#epi-rte-contradiction-disposition), [EPI-RTE-evidence-withdrawal](#epi-rte-evidence-withdrawal) and [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission).

**Use and quality evaluation have distinct consumers.** Stored source/wiki text reaches later filing and answering through [RT-BAP-corpus-data](runtime.md#rt-bap-corpus-data), with scoped retrieval and asynchronous indexing rather than a new endorsement step. Raw search/read/list/describe bypass the answer verifier. The QA runner compares against golden expectations, reports/history-appends results, and does not automatically revise production. Its disambiguation scorer explicitly admits misattributed cited prose. Filing parity adds fixture/effective-output comparison and external blind editorial judgment, then a guarded deployment path can replace code and packaged skill; the operator can bypass that local gate. These release-evaluation routes make a system-wide “no semantic review anywhere” claim false, but establish no per-capture semantic review. See [EPI-RTE-qa-evaluation](#epi-rte-qa-evaluation), [EPI-RTE-release-evaluation](#epi-rte-release-evaluation) and [EPI-RTE-release-admission](#epi-rte-release-admission).

No inspected run establishes that retrieved material changed a real user's or agent's behavior, or that retained changes improved future capacity. That observation limit does not erase implemented retention, alias adaptation, corpus repair or release gates. The inspected maintenance loop changes the knowledge product, not its own Python/skill machinery; the separate contributor/release route can replace that machinery, but evidence-to-update determination and exercised downstream causal dependence are not supplied, so exercised self-improvement is unestablished on that route. Learning, reflection, autonomy and formulated-theory criticism are separate questions, not consequences of a clean corpus or a passing answer gate. The source-only scope supports no unified score or system-wide negative about opaque model processes.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-readable-source
Label: Readable extracted source

Readable capture assertions are natural-language text in ExtractionResult and rendered source Markdown in a layer's Git corpus, with original/readable references and extraction metadata. This differs from the transient proposal [RT-OBJ-filing-plan](runtime.md#rt-obj-filing-plan); its production is a part of [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing). Original bytes retained by capture storage and source immutability do not certify their assertions. SRC-1, `src/stigmergy/capture/extraction.py`, `src/stigmergy/knowledge/writer.py`.

> relative_source = source_path(envelope)
> source_text = render_source(envelope, extracted)
> physical_source = layers.physical_path(layer, relative_source)
> --- `src/stigmergy/knowledge/writer.py`

#### EPI-OBJ-wiki-pages
Label: Derived wiki pages

Natural-language page bodies with symbolic type/status/ACL/source metadata reside in Markdown/Git, later projected into the reader index. These are durable mutation results, not the transient [RT-OBJ-filing-plan](runtime.md#rt-obj-filing-plan) or per-question [RT-OBJ-synthesis-context](runtime.md#rt-obj-synthesis-context). Prose includes facts, states, explanations and links; page creation attaches the current source, while updates union source paths. SRC-1, `src/stigmergy/knowledge/writer.py`; later delivery see [RT-BAP-corpus-data](runtime.md#rt-bap-corpus-data).

> sources=tuple(dict.fromkeys((*page.sources, source))),
> --- `src/stigmergy/knowledge/writer.py`

#### EPI-OBJ-contradictions
Label: Persisted contradictions

Part of: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages)

Structured records combine natural-language competing claim text/explanation with symbolic IDs and source references, embedded in page Markdown. The retained object is distinct from the proposal in [RT-OBJ-filing-plan](runtime.md#rt-obj-filing-plan). It is governed by its own preservation and explicit resolution checks, not just ordinary page-body replacement. SRC-1, `src/stigmergy/knowledge/writer.py`.

> if any(candidate[item_id] != record for item_id, record in current.items() if item_id in candidate):
>     raise KnowledgeWriteError("existing contradiction claims cannot be rewritten in a page mutation")
> --- `src/stigmergy/knowledge/writer.py`

#### EPI-OBJ-entity-aliases
Label: Entity aliases

Part of: [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages)

Alias strings are symbolic metadata consumed by fixed name-resolution rules; the names denote an identity relation judged semantically by a classifier. The classifier receives natural-language sentence and page summary plus typed metadata. This persisted part differs from proposal metadata in [RT-OBJ-filing-plan](runtime.md#rt-obj-filing-plan); its live extra admission route is not separately declared in runtime. SRC-1, `src/stigmergy/knowledge/aliases.py`.

> file.write_text(render_like(page, updated=at, aliases=(*page.aliases, candidate.text)),
>                 encoding="utf-8")
> --- `src/stigmergy/knowledge/aliases.py`

#### EPI-OBJ-merge-evidence
Label: Entity merge evidence

EntityMergeEvidence is a typed request object containing source assertions and paths; the assertions are natural-language claims that selected entity names are equivalent. Its immediate substrate is the parsed queued entity request; accepted consolidation persists as entity-page Markdown and change reasons. It is a distinct supplied-request object, not model-produced [RT-OBJ-filing-plan](runtime.md#rt-obj-filing-plan). SRC-1, `src/stigmergy/entities/service.py`, `src/stigmergy/knowledge/writer.py`.

> if request.evidence is None:
>     raise GateRefused("merge evidence is missing")
> canonical = _merge_in_layer(worktree, request.entities, at=at, evidence=request.evidence)
> --- `src/stigmergy/knowledge/writer.py`

#### EPI-OBJ-answer-output
Label: AnswerOutput

AnswerOutput mixes natural-language answer Markdown and citation quote text with symbolic paths, confidence enum and refusal boolean in an in-process Pydantic object. Bounded quotes/citation count precede verification; shaped JSON is returned. It is the model's draft, distinct from the evidence/bookkeeping [RT-OBJ-synthesis-context](runtime.md#rt-obj-synthesis-context). SRC-1, `src/stigmergy/answer/synthesize.py`; output consumer see [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer).

> answer_markdown: str = Field("", description="the answer; concise; every figure from tool evidence")
> --- `src/stigmergy/answer/synthesize.py`

#### EPI-OBJ-qa-results
Label: QA golden results

Symbolic golden expectations, per-case booleans and aggregate metrics with natural-language misses/reasons live in runner dictionaries, optional JSON reports and history records. They assess answers; they are not retained answer context or a wiki knowledge update. Closest supplied route is [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer), whose output they evaluate; no supplied object counterpart after comparison. SRC-1, `evals/run_qa.py`.

> scored = _score(case, res)
> --- `evals/run_qa.py`

#### EPI-OBJ-parity-artifact
Label: Filing parity artifact

A release artifact and external content-addressed evidence bundle carry symbolic provenance, per-case/run results and natural-language effective page outputs/editorial judgments. They reside in operator JSON files read by the release validator, not the live wiki or provider parameters. They are evidence for [RT-RTE-product-admission](runtime.md#rt-rte-product-admission), not another declaration of that route or of QA results. A terminal actual packet was not supplied for inspection. SRC-1, `evals/filing/README.md`, `evals/filing/parity.py`.

> Keep the complete
> evidence bundle outside the candidate checkout; a self-reported verdict or mutable path is rejected.
> --- `evals/filing/README.md`

### Routes

#### EPI-RTE-evidence-extraction
Label: Readable evidence extraction

Part of: [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing)

Writer extract_capture dispatches by detected media and renders readable evidence. Parser code owns extraction bounds; OCR model proposes text under a faithful-transcription instruction. UTF-8 input b'Aurora remains a draft.' passes _text's size/UTF-8 checks and returns that exact string in ExtractionResult: a concrete implementation deduction, not target execution. Other format fidelity and actual OCR output are unresolved.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Readable text and extraction metadata, or exception.
- Later read-back: Rendered source is retained for later filing and reader retrieval; originals remain separately referenced.
- Delegated visibility: OCR receives image bytes and transcription prompt; filing receives readable text.
- Selection predicate: Media dispatch, supported format and resource/readable-size bounds.
- Invalidation or expiry: Extraction fails on invalid UTF-8/empty OCR/limits; durable source lifecycle is governed separately.
- Activation or effect: Can admit a machine reading to source/planner context; compliance with transcription instruction unobserved.
- Evidence limits: Full PDF/Office/Slack extraction bodies uninspected; byte identity is not world truth.

Evidence: SRC-1, `src/stigmergy/capture/extraction.py`, implementation.

> text = data.decode("utf-8")
> except UnicodeDecodeError as error:
>     raise ArtifactRejected("text artifact is not valid UTF-8") from error
> return ExtractionResult(text=text, media_type=media_type, extractor="utf8")
> --- `src/stigmergy/capture/extraction.py`

#### EPI-RTE-filing-transform
Label: Source to filing proposal

Part of: [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing)

The planner produces the proposal, not an accepted factual claim. Code supplies the skill as recorded by [RT-BAP-librarian-skill](runtime.md#rt-bap-librarian-skill). The instruction explicitly distinguishes unsupported results, document wording versus signed state, OCR errors, old/current states and unresolved conflict. This is semantic guidance rather than an independent evaluator. Owner, no human per-plan veto and bounded correction: see parent route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Typed FilingPlan proposal.
- Later read-back: Only admitted projected pages persist, via the separate retention route.
- Delegated visibility: Source plus bounded safe existing context; no hidden repository inference licensed.
- Selection predicate: Current source, visible candidate pages and source evidence.
- Invalidation or expiry: Draft can be replaced or rejected by contracts/lint.
- Activation or effect: Requests page synthesis and cross-page corrections; delivered instruction is not demonstrated compliance.
- Evidence limits: Without concrete source/plan pairs, reshaping, entailment and non-entailing conjecture remain unresolved.

Evidence: SRC-1, `src/stigmergy/knowledge/librarian_skill.md`, implementation and doctrine/design.

> Write facts plainly; the citation is the attribution. Name who claims it only for another
>   party's unverified result, and never upgrade that to proof.
> --- `src/stigmergy/knowledge/librarian_skill.md`

#### EPI-RTE-filing-check
Label: Candidate contract evaluation

Part of: [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing)

The writer and linter evaluate candidate files: page contracts, source existence/flow, name collisions, links, conflict references, H1/body/local-source editorial minima. Writer also requires ordered preservation of old source-backed block lines and existing local attributions. The result is a code-derived violation set or exception. This route is the filing invocation of those checks; garden reuses lint under [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission). Deterministic acceptance criteria are not a semantic reference-answer oracle. Code can veto or drive bounded replacement; human request initiation is not per-content approval.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Violation set, preservation failure or clean result.
- Later read-back: inapplicable — checks themselves are current-operation state; admitted pages persist separately.
- Delegated visibility: Fixed gate feedback can reach correction model; source/model text is not itself gate message authority.
- Selection predicate: Proposed files and previously cited text; only changed editorial paths receive editorial checks.
- Invalidation or expiry: Re-evaluated for corrected candidate; rejection discards/restores draft.
- Activation or effect: Feeds enforcing writer admission, independently of whether prose is actually entailed.
- Evidence limits: Source references establish provenance pointers, not correctness of a novel paragraph.

Evidence: SRC-1, `src/stigmergy/knowledge/writer.py`, implementation.

> lost = _lost_source_backed_lines(page.body, body)
> if lost:
>     raise ExistingSourceBlockNotPreserved(target_path, lost)
> --- `src/stigmergy/knowledge/writer.py`

#### EPI-RTE-filing-retention
Label: Admitted source and wiki retention

Part of: [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing)

After code admission, writer publishes source and projected pages to Git and records the change; invalid filing may retain only the source. Publication/recovery owner and lease limits are supplied by the parent. Retention is not lifecycle integration after a demonstrated semantic acceptance decision. Closest supplied object is [RT-OBJ-filing-plan](runtime.md#rt-obj-filing-plan); this route concerns persisted effects, not proposal generation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Commit/change/report; caller's early receipt is only queue admission.
- Later read-back: Retained source/wiki enters later indexed reads and subsequent planning context.
- Delegated visibility: Model sees source/context, not writer Git credentials through configured planner tools.
- Selection predicate: Diff/ACL/lease gates and source-only fallback.
- Invalidation or expiry: Ordinary source protection; explicit deletion/erasure remain alternate destructive paths.
- Activation or effect: Committed content becomes eligible for downstream use; actual reliance unobserved.
- Evidence limits: Semantic acceptance and index synchronization are not implied by landed.

Evidence: SRC-1, `src/stigmergy/knowledge/writer.py`, implementation.

> if plan_invalid:
>     # Gate messages are fixed sentences, never source or model text.
>     log.warning("filing plan rejected for %s: %s", envelope.capture_id, plan_rejection)
>     _restore_mutable(tree, snapshot)
>     reasons = {relative_source: "Archived immutable readable evidence"}
>     fallback = _introduced(check(tree), tolerated)
> --- `src/stigmergy/knowledge/writer.py`

#### EPI-RTE-contradiction-disposition
Label: Conflict preservation and resolution

Part of: [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing)

Model proposes conflicting claims; code checks source paths against supplied evidence, validates records and preserves existing conflict markers. Explicit resolution requires master authorization and exactly the capture-named conflict; removal requires an accepted update of every affected page. Proposal comes from model/source; code decides allowable mutation and can veto; caller names resolution target, not an automatic source-truth oracle. Intended use is managed conflict bookkeeping, not proof which side is true. Rejected changes remain uncommitted; prior persisted conflicts survive ordinary replacement.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Persisted conflict or target removal; invalid plan raises.
- Later read-back: Conflict Markdown and cited claims return in later visible page/context reads.
- Delegated visibility: Planner receives only safe context/source evidence; broader-page mutations may be dropped/refused.
- Selection predicate: Allowed source set, writable target and named resolution with updated pages.
- Invalidation or expiry: Cannot rewrite or silently omit old records; explicit authorized resolution or evidence deletion has separate rules.
- Activation or effect: Forces preservation or bounded named removal in managed corpus.
- Evidence limits: Whether visible claims really conflict or a resolution is factually justified remains model/source-dependent.

Evidence: SRC-1, `src/stigmergy/knowledge/writer.py`, implementation.

> if not expected or tuple(plan.resolved_contradictions) != (expected,):
>     raise KnowledgeWriteError("only the contradiction named by the capture can be resolved")
> --- `src/stigmergy/knowledge/writer.py`

#### EPI-RTE-alias-judgment
Label: Alias semantic classification

Distinct from layer routing [RT-RTE-layer-routing](runtime.md#rt-rte-layer-routing): this judges name equivalence, not audience. It is an extra semantic step in both [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing) and [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission), so not part of exactly one supplied route. Code extracts new wikilink labels, then typed-decision model judges alias versus description/role/part/product/different entity. No expected-answer oracle is used during live classification. The kernel typed-decision mechanism is shared; this distinct task's provider/weight provenance is not independently inspected beyond supplied model records.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Probability for alias or skipped/failure entry.
- Later read-back: inapplicable — probability is step state; accepted names persist by separate admission route.
- Delegated visibility: Entity title/type/summary/aliases, candidate and local sentence.
- Selection predicate: New eligible link variants not already named/ambiguous/shared; at most eight within ten-second window.
- Invalidation or expiry: Deadline/cap/decision failure skips a candidate; no independent truth correction established.
- Activation or effect: Probability is consumed by admission threshold; no actual decisions observed.
- Evidence limits: Configured judgment is semantic, not proof or calibrated error rate.

Evidence: SRC-1, `src/stigmergy/knowledge/aliases.py`, implementation.

> OPTIONS = {
>     ALIAS: ("The candidate is another name for this same entity: a spelling, an abbreviation, a short "
>             "form, a first name, a full name, or a former name."),
> --- `src/stigmergy/knowledge/aliases.py`

#### EPI-RTE-alias-admission
Label: Alias acceptance and integration

Paired with [EPI-RTE-alias-judgment](#epi-rte-alias-judgment), distinct from generic filing mutation admission because a separate probability threshold grants a name lookup consequence. Overlaps capture and garden parents cited there. No per-candidate human approval occurs in this code. Criterion: eligibility plus probability at least 0.75; intended use: entity-name resolution; scope: this entity and candidate variant. The accepted mapping is written to aliases; exceptions during writes restore prior text. Writer checks and publication still gate durability. This is operational acceptance/integration of an identity claim, not a license to infer independent source truth.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Accepted/rejected/skipped report and page edits.
- Later read-back: Updated aliases persist into later entity lookup after publication/indexing.
- Delegated visibility: inapplicable — recorder is code; model visibility is declared by judgment route.
- Selection predicate: Probability at least THRESHOLD after candidate filters.
- Invalidation or expiry: Write exception restores all changed alias pages; collision/lint check can undo or reject publication.
- Activation or effect: Adds accepted name mapping to retained metadata for later selection.
- Evidence limits: No actual threshold calibration or demonstrated downstream benefit inspected.

Evidence: SRC-1, `src/stigmergy/knowledge/aliases.py`, implementation.

> decision = "accepted" if probability >= THRESHOLD else "rejected"
> report.append({**entry, "decision": decision, "probability": round(probability, 4)})
> if decision == "accepted":
>     accepted.append(candidate)
> --- `src/stigmergy/knowledge/aliases.py`

#### EPI-RTE-merge-check
Label: Source-assertion merge check

No separately declared supplied route covers ENTITY dispatch's identity evidence check. Closest route [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission) discusses maintenance/deletion but not this source-assertion evaluator. Actor requests merge and supplies evidence; code can veto before consolidation. Check target: these existing same-type/same-ACL entities denote the same identity. Criterion: supplied assertion occurs in immutable source body and unambiguously binds every selected entity under recognized identity grammar. Intended use/scope: consolidation of these selected pages. No model or human semantic adjudication is invoked inside this evaluator. Source truth and grammar interpretation are premises, not independently established facts.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Pass by return or EntityOperationError.
- Later read-back: inapplicable — evaluator itself is current request; merged pages and change reason persist separately.
- Delegated visibility: inapplicable — deterministic local evaluator, no delegated model call.
- Selection predicate: Explicit merge request, valid immutable source and restricted identity assertion grammar.
- Invalidation or expiry: Any failed assertion aborts before consolidation.
- Activation or effect: Permits or blocks merge executor.
- Evidence limits: Occurrence and grammar exclude some ambiguity, not all false identity assertions; full API human-vs-agent caller origin unresolved.

Evidence: SRC-1, `src/stigmergy/entities/service.py`, implementation.

> if assertion not in readable:
>     raise EntityOperationError("merge assertion is not present in the cited source")
> if not _assertion_binds_pages(assertion, pages):
>     raise EntityOperationError("merge assertion does not unambiguously equate every selected entity")
> --- `src/stigmergy/entities/service.py`

#### EPI-RTE-entity-merge
Label: Evidence-backed entity consolidation

Distinct from supplied capture/garden routes: explicit ENTITY operation admitted by master authorization, evidence check, introduced-lint and diff/lease publication gates. Pairs with [EPI-RTE-merge-check](#epi-rte-merge-check); no supplied counterpart after comparison. Actor selects the first page as canonical; code concatenates the others under Formerly headings, unions aliases/sources, deletes duplicate files and rewrites links. Intended change is identity consolidation, not newly measured truth. Code can reject before publication; ephemeral worktree scopes failure, but automatic post-publication rollback is not established. Rename and entity-delete branches are also visible; they do not invoke this equivalence check.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Canonical path then writer commit/change/report.
- Later read-back: Unified entity bodies/aliases/links reach later indexed readers and filing.
- Delegated visibility: inapplicable — local deterministic mutation; no model request in merge_entities.
- Selection predicate: Distinct existing same-type/same-ACL pages plus passed evidence and master authorization.
- Invalidation or expiry: Rejected request leaves published base; admitted duplicate paths are removed.
- Activation or effect: Makes accepted identity assertion reorganize graph and later lookup.
- Evidence limits: Conditional on source assertions; no independent factual identity validation or benefit observation.

Evidence: SRC-1, `src/stigmergy/entities/service.py`, implementation.

> _verify_merge_evidence(source_roots or (root,), chosen, evidence)
> canonical = chosen[0]
> --- `src/stigmergy/entities/service.py`

#### EPI-RTE-answer-check
Label: Answer occurrence verification

Part of: [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer)

Distinct evaluator part of scoped answering, not a second declaration of the whole route. Code checks numeric token interpretations against recorded tool-result text. Citation checking separately requires surfaced path membership, then normalizes quotes against a newly fetched scoped page title/head plus fragments identified by recorded window numbers. `page_as_read` delegates to AnswerBrain.get_page, which calls fetch_page_raw again; the service sanitizes and excerpts the head to PAGE_EXCERPT (6000 characters). Search and listing can mark a path surfaced while returning only metadata, summaries or snippets. Therefore quote occurrence need not mean the quote appeared in a tool result delivered to the model, and the check is not bound to a snapshot of that earlier response. Empty citations on nonempty answers add a defect. Refusals are vacuously verified. Deterministic verdict is derived under this domain, not from an external answer oracle. _SPAN=200 bounds page-side strikethrough removal; numbers skip bare single digits and do not bind values to entity/period.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Verdict and unverified-figure/citation problem lists.
- Later read-back: inapplicable — fresh per-question context; audit counts are not reuse of answer knowledge.
- Delegated visibility: Correction receives gate feedback and prior history. Figure checks consume recorded tool text; citation checks consume refetched scoped page heads and fragment text selected by recorded window numbers after surfaced-path membership checks.
- Selection predicate: Every citation must name a current-question surfaced path; quotes match the refetched scoped head/title or recorded fragment windows. Recognized figures must occur in current-question recorded tool text.
- Invalidation or expiry: Corrected draft rechecked; context lifetime ends with question.
- Activation or effect: Result drives retry/ship rank through separate disposition.
- Evidence limits: A quote may match an undisplayed part of a refetched scoped head; occurrence does not prove prior delivery, snapshot identity or entailment of the surrounding answer. These are implementation deductions, not observed model behavior.

Evidence: SRC-1, `src/stigmergy/answer/verify_answer.py`, `src/stigmergy/answer/synthesize.py`, `src/stigmergy/answer/brain.py`, `src/stigmergy/server/service.py`, implementation.

> page_path, _number = fragments.parse_reference(path)
> page = self.service.fetch_page_raw(page_path)
> if page is None:
>     return None
> --- `src/stigmergy/answer/brain.py`

> "body": body[:PAGE_EXCERPT],
> "truncated": len(body) > PAGE_EXCERPT,
> --- `src/stigmergy/server/service.py`

> if ctx is not None:
>     ctx.note_page(page["path"])
> span = " to ".join(dict.fromkeys(day for day in (page["first_source"], page["last_source"])
> --- `src/stigmergy/answer/brain.py`

> problems = len(figures) + len(citation_problems)
> verdict = "verified" if problems == 0 else ("partial" if problems == 1 else "failed")
> --- `src/stigmergy/answer/verify_answer.py`

#### EPI-RTE-answer-disposition
Label: Strict answer output disposition

Part of: [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer)

Software consumes verifier findings and additionally scans all citation quote figures. Any missing figure or failed verdict suppresses draft; one citation-only problem can ship partial. Suppressible non-refusal drafts can receive bounded correction and only improved ship rank wins. Evidence-only completion requires no figure defects and verified verdict; otherwise refusal is composed from server-recorded facts, not model prose. No per-answer human approval. Intended use is returning this answer under occurrence criteria, not certifying its propositions true; no persistent wiki admission occurs.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Answer JSON or server-shaped refusal.
- Later read-back: inapplicable — answer is not persisted for later question context in inspected path.
- Delegated visibility: Primary/correction evidence tools and fixed evidence-only completion as supplied by parent.
- Selection predicate: Ship rank over strict figure/citation findings.
- Invalidation or expiry: Suppressed drafts withheld; failed retry keeps original disposition; question budgets terminate.
- Activation or effect: Enforces return/refusal; caller reliance remains unobserved.
- Evidence limits: A partial result and vacuous verified refusal must not be read as a fully checked factual answer.

Evidence: SRC-1, `src/stigmergy/answer/service.py`, implementation.

> # suppress on ANY untraced figure, or on a `failed` verdict (2+ problems); exactly one
> # citation-only problem ships, labeled `partial`
> if figs or v["verdict"] == "failed":
> --- `src/stigmergy/answer/service.py`

#### EPI-RTE-evidence-withdrawal
Label: Managed evidence reference sweep

Part of: [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission)

Material subpath of explicit destructive lifecycle admission. _delete checks explicit master authorization, removes requested paths in an ephemeral worktree, sweeps dependent references, rejects introduced lint violations and publishes under delete-specific diff rules. Code removes citing units/conflicts/source declarations, plain-texts dead links and recursively removes emptied pages. This changes which evidence can later be relied upon without deciding it was false. Corpus withdrawal is distinct from resolving a live conflict; no automatic post-publication factual restoration is shown.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Deletion commit/change/report or refusal.
- Later read-back: Later managed corpus/index reads no longer contain removed units after convergence.
- Delegated visibility: inapplicable — sweep is code, not a model request.
- Selection predicate: Requested physical paths and references resolvable in each affected layer/public scope.
- Invalidation or expiry: Deletion invalidates dependent units by source-path membership.
- Activation or effect: Enforces withdrawal from managed Markdown and eventual index.
- Evidence limits: Git history/external clones, object-store erasure and full workspace purge are not established by this narrower sweep.

Evidence: SRC-1, `src/stigmergy/knowledge/writer.py`, implementation.

> body = _remove_citing_units(body, dead_sources)
> sources = tuple(source for source in page.sources if source not in dead_sources)
> --- `src/stigmergy/knowledge/writer.py`

#### EPI-RTE-qa-evaluation
Label: Golden QA scoring

Distinct from live answer verification [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer): this optional runner asks through that service and scores against externally supplied golden cases/scopes. Golden corpus expectations are the reference oracle, not model self-judgment. Mode: bounded evaluation; no runtime improvement trigger. Scorer accepts refusal for refusal/refute/disambiguate as appropriate; ordinary cases require expected content and citation with nonfailed verdict; enumeration uses expected/forbidden sets. Reports/history inform operators, but this runner returns success on a complete run even if quality cases miss. No production knowledge or code admission is implemented here.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Case outcomes and aggregate report; complete/incomplete exit.
- Later read-back: Real complete-run metrics append to history for later comparison; fake runs do not.
- Delegated visibility: Answer model gets production-style scoped retrieval; scorer sees golden expectations and result.
- Selection predicate: Chosen golden file, identities, repeats, corpus/index and budget.
- Invalidation or expiry: Incomplete budget run cannot append as a complete real measurement.
- Activation or effect: Advisory measurement; not automatic update or per-answer acceptance.
- Evidence limits: Misattributed disambiguation prose can pass; golden expectations and underlying corpus truth are supplied premises, not independently authenticated.

Evidence: SRC-1, `evals/run_qa.py`, implementation.

> code cannot judge attribution prose, so a cited answer that
>                      misattributes also passes; the citation is the mitigation.
> --- `evals/run_qa.py`

#### EPI-RTE-release-evaluation
Label: Filing release evidence evaluation

Part of: [RT-RTE-product-admission](runtime.md#rt-rte-product-admission)

Specializes the supplied release/product route: parity evaluator checks artifact shape/provenance, replayed case outputs and blind review, then rejects candidate when material regressions exceed production. Targets are fixture-bounded filing outputs and candidate configuration. Reference evidence comprises fixture/case contracts and matched production outputs; an external independent reviewer judges factual support and reuse quality from anonymous complete payloads. Reviewer human/model identity and actual judgments are uninspected here. Mode: explicit repeated comparative release evaluation, not live capture acceptance. Trusted operator supplies bundle; code can veto inconsistent/failing evidence. Full helper correctness is not audited.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Pass/fail with failures; CLI returns nonzero for failing result.
- Later read-back: External bundle can be consumed again by deployment; does not enter tenant wiki.
- Delegated visibility: Documented reviewer receives fixture and anonymous effective outputs, not implementation identities.
- Selection predicate: Bound candidate/production/corpus/skill, required repeats and cases, blind comparison coverage.
- Invalidation or expiry: Missing/stale/failing evidence rejects release; no bypass within validator, distinct deploy bypass follows.
- Activation or effect: Feeds candidate deployment veto.
- Evidence limits: No terminal actual artifact inspected; content addressing does not authenticate an operator-controlled reviewer; configuration comparison does not isolate component effect.

Evidence: SRC-1, `evals/filing/parity.py`, implementation.

> elif len(stigmergy_regressions) > len(production_regressions):
>     _failure(failures, "review", "regression-beyond-production",
>              candidate=len(stigmergy_regressions), production=len(production_regressions))
> --- `evals/filing/parity.py`

#### EPI-RTE-release-admission
Label: Guarded staging deployment

Part of: [RT-RTE-product-admission](runtime.md#rt-rte-product-admission)

Specializes product delivery's concrete gate, not a second identity for the whole contributor protocol. Code requires clean exact checkout and passing parity CLI before fly deploy unless operator explicitly sets STIGMERGY_PARITY_GATE=off. Operator proposes candidate/bundle and can bypass local gate; code otherwise vetoes. Intended use is installing this configuration for future requests, scoped to release criteria rather than every future statement. Failure exits before deploy; installed rollback and actual downstream activation not established.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Deploy invocation or nonzero early exit.
- Later read-back: Installed code/packaged skill can govern later requests; actual deployment unobserved.
- Delegated visibility: External parity reviewer visibility is described in evaluation, not expanded by deployment.
- Selection predicate: Clean checkout plus artifact validator exit, unless explicit bypass.
- Invalidation or expiry: Gate failure aborts this script; operator-controlled direct deployment remains outside enforcement.
- Activation or effect: Permits replacing deployed behavior-determining machinery, conditional on external Fly operation.
- Evidence limits: Source wiring does not establish evidence-responsive update determination, installation or exercised improvement.

Evidence: SRC-1, `scripts/deploy_staging.sh`, implementation.

> if ! PYTHONDONTWRITEBYTECODE=1 "$PREFLIGHT_PY" "$HERE/evals/filing/parity.py" \
>     --artifact "$PARITY_ARTIFACT" --repo-root "$HERE"; then
>     echo "deploy: recorded parity gate rejected this candidate" >&2
>     exit 2
>   fi
> --- `scripts/deploy_staging.sh`

### Claims

#### EPI-CLM-verified-answer
Label: Cited verified answer

The public tool table calls ask a cited verified answer or honest refusal. Compared with [RT-CLM-scoped-knowledge](runtime.md#rt-clm-scoped-knowledge), this is a distinct warrant claim, not a visibility claim. SRC-1, `README.md`, doctrine/design.

> | `ask(question)` | a cited, verified answer — or an honest refusal |
> --- `README.md`

#### EPI-CLM-self-healing
Label: Self-healing corpus

The public feature table describes scheduled gardener repair through gates and no human to-do list. Distinct from [RT-CLM-scoped-knowledge](runtime.md#rt-clm-scoped-knowledge): this concerns maintenance autonomy/quality, not scoped reading. SRC-1, `README.md`, doctrine/design.

> | **Self-healing corpus** | A scheduled gardener repairs through the same gates. No human to-do list. |
> --- `README.md`

#### EPI-CLM-quality-measures
Label: Latest quality measures

The README reports latest retrieval Recall@5, honesty, groundedness and refutation all 1.00, with displayed bars. It is attributed reported operation, not this run's experiment. Distinct from general [RT-CLM-scoped-knowledge](runtime.md#rt-clm-scoped-knowledge) and from the narrower public wording [EPI-CLM-verified-answer](#epi-clm-verified-answer). SRC-1, `README.md`.

> | Answer groundedness | **1.00** | ≥ 0.84 |
> --- `README.md`

#### EPI-CLM-parity-release
Label: Filing parity release criterion

Release documentation claims real-model repeated filing comparison, replay and blind editorial review with a fail-closed criterion. This is distinct from tenant knowledge guarantees and is the source-native criterion within [RT-RTE-product-admission](runtime.md#rt-rte-product-admission), not a new declaration of that route. SRC-1, `evals/filing/README.md`, doctrine/design.

> Missing, stale, incomplete, or failing evidence rejects the release.
> --- `evals/filing/README.md`

> Content addressing proves which bytes
> were reviewed; it does not authenticate the reviewer against an operator who controls the release host.
> --- `evals/filing/README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; the route ledger records the paths and cites [RT-BAP-librarian-skill](runtime.md#rt-bap-librarian-skill) and [RT-BAP-corpus-data](runtime.md#rt-bap-corpus-data) where applicable.
