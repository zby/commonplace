---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "LLM Wiki epistemic routes: candidate extraction, unchecked wiki admission, metadata reinforcement and synthesis verification at the frozen revision."
run-id: AAS-2026-10-17-llm-wiki-507fade8a56e-01
reviewed-boundary: d2bd485921f6c7b6071afbb389f44ab8e4e83c69
---

# LLM Wiki epistemic report

## Source-and-claim boundary

The question is which routes turn incoming research/security material into content licensed for later reliance, and what actually checks that license. Scope and exclusions are those of [the boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are in its [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not observed execution or causal experiments. The runtime is a provisional baseline, not an inspection limit.

The principal distinction is between **admitting a file** and **accepting its claims against evidence for an intended use**. The former is implemented in several paths. The latter is requested in prompts and governance, but is not established by parsing, nonempty completions, source counts or verification labels. This is a route-specific finding, not a judgment that the imported material is false.

Consequential claims inspected here are [EPI-CLM-knowledge-compilation](#epi-clm-knowledge-compilation), [EPI-CLM-source-integrity](#epi-clm-source-integrity), [EPI-CLM-retrospective-validation](#epi-clm-retrospective-validation), and [RT-CLM-prompt-ratchet](runtime.md#rt-clm-prompt-ratchet). The newsletter adds a machine-written verification assertion in [EPI-RTE-newsletter-admission](#epi-rte-newsletter-admission).

| Entry point or operation | SRC-1 source paths | Coverage and records | Limit / conclusion prevented |
|---|---|---|---|
| File/URL ingestion, feed acquisition and normalization | `tools/ingest.py`, `tools/arxiv_monitor.py`, `tools/cve_monitor.py`, `tools/github_monitor.py`, `tools/rss_monitor.py`, `tools/curated_monitor.py`, `tools/common.py`, `tools/normalize.py` | Supplied [RT-RTE-batch-ingestion](runtime.md#rt-rte-batch-ingestion), [RT-RTE-scheduled-drivers](runtime.md#rt-rte-scheduled-drivers); direct normalization and relevance/hash/frontmatter reads | Feed truth, complete provenance and PDF extraction fidelity not independently established |
| CLI extraction, integration and prompt accessors | `tools/extract.py`, `tools/integrate.py`, `tools/prompts.py` | Direct complete executable reads; [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission), [EPI-RTE-claim-projection](#epi-rte-claim-projection) | No model outputs or source-grounded adjudications supplied |
| Batch, manual watcher, immediate CVE, daemon and unified scheduling | `tools/pipeline_all.py`, `tools/watchdog_monitor.py`, `tools/cve_monitor.py`, `tools/daemon.py`, `tools/unified_daemon.py`, `tools/run_all_monitors.py` | Supplied runtime account plus direct function/entry-point and validation-call searches; [RT-RTE-scheduled-drivers](runtime.md#rt-rte-scheduled-drivers) | Driver wiring does not show successful execution; different drivers do not inherit each other's checks |
| Lightweight/deep lint and retrospective CLI | `tools/lint.py`, `tools/retrospective_validator.py` | Direct full reads; [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance), [EPI-RTE-reinforcement-selection](#epi-rte-reinforcement-selection), [EPI-RTE-confidence-update](#epi-rte-confidence-update) | Semantic evaluator accuracy and human review uptake unobserved; helper `check_contradiction` is callable but not called by weekly validation |
| Optimizer, fixture builder and metrics | `tools/prompt_optimizer.py`, `tools/create_eval_set.py`, `tools/metrics_collector.py`, `eval_set_index.json`, `eval_set/` | Direct builder and proposal/evaluation/decision reads; supplied [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization), [RT-OBJ-metrics](runtime.md#rt-obj-metrics) | No independent expected-answer oracle or installed candidate treatment; fixtures are not certified ground truth |
| Research execution branches | `tools/research_agent.py` | Direct execution/validation/synthesis reads plus supplied [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance) | Task labels and generated queries/outlines do not establish completed searches or evidence acceptance |
| Search, catalog, article edit/read, upload, backlinks and history; browser calls | `tools/query.py`, `tools/index.py`, `api_server.py`, `ui/src/App.jsx` | Direct query/index and API read/save/backlink reads; API route search and supplied [RT-RTE-api-mutation](runtime.md#rt-rte-api-mutation), [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption) | Git history is not automatic rollback; ranking is not warrant; rendering/build internals not assessed |
| Newsletter synthesis and verification assignment | `tools/newsletter_agent.py` | Direct full read; [EPI-RTE-newsletter-context](#epi-rte-newsletter-context), [EPI-RTE-newsletter-admission](#epi-rte-newsletter-admission) | Assigned verification has no evidence-consuming check at this write site |
| Ordinary/long paper generation and critique | `tools/paper_agent.py`, `tools/paper_agent_long.py` | Direct ordinary analysis/draft/critique/finalization reads; supplied long-form override in [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption) | No measured novelty, valid experimental results or validated transfer; long form skips critiques |
| Provider call and model state | `tools/common.py` | Supplied [RT-RTE-model-call](runtime.md#rt-rte-model-call), [RT-CMP-main-model](runtime.md#rt-cmp-main-model), [RT-CMP-openrouter-model](runtime.md#rt-cmp-openrouter-model) | Weights, provider state, response grounding and training remain inaccessible |
| Test/configuration/host diagnostic entry points | `test_api.py`, `test_e2e.py`, `test_ingest.py`, `test_llm.py`, `test_phase2.py`, `test_user_workflow.py`, `tools/test_daemon.py`, `tools/test_optimizer.py`, `tools/test_research_agent.py`, `tools/check_model_config.py`, `check_rss_state.py`, `clear_rss_state.py`, `configure_lms_max_context.sh`, `tasks/` | Boundary coverage plus direct scoped evaluator/verification searches in Python tools/root tests | Not executed; no benchmark result or host deployment guarantee; detailed diagnostic branches unassessed |
| Governance and public specification | `README.md`, `AGENTS.md`, `llm-wiki.md`, `research_agenda.md` | Direct README introduction, AGENTS complete, specification trust section; supplied agenda account | Remaining status/design narratives and individual retained page assertions not audited; no system-complete negative across every claim in the repository |

The dispatch search enumerated Python top-level functions/classes, `__main__` guards and FastAPI decorators across `tools/*.py` and `api_server.py`. A second search across those tools, API and root tests covered validation, acceptance/rejection, withdrawal/retraction, rollback, verification, reinforcement, contradiction helpers, registration, hooks and tool calls. The inspected paths expose CLI functions, HTTP handlers and code-scheduled calls, not a model-native registered-tool loop. This is a bounded search account, not an absence claim about excluded plugin/host behavior. The callable contradiction helper is a counterexample to saying no model contradiction operation exists; the weekly caller does not use it (SRC-1: `tools/retrospective_validator.py`). Deep lint is another real counterexample to a blanket claim of no semantic checking.

Missing evidence is localized: source/provider truth prevents certifying imported premises; linked extraction/merge traces prevent classifying actual generated propositions or checking preservation; adjudicated evidence decisions prevent claiming produced accepted new knowledge; deployment traces prevent claiming the routes operated; independent interventions prevent attributing quality gains. Tracked wiki artifacts alone do not identify their producing/checking route. No needed supersession of the supplied runtime was found: its broad containers remain valid; this report adds material parts, including the newsletter's verification assignment and omission of conflict status from its model context.

## Epistemic-object inventory

Fields owned by records are cited rather than redefined here. All source anchors below are SRC-1 at the frozen revision.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-source-text](#epi-obj-source-text) | see record | Normalized input | SRC-1 `tools/normalize.py` | Source warrant unknown, PDF fidelity untested |
| [EPI-OBJ-extracted-claims](#epi-obj-extracted-claims) | see record | Extraction candidate | SRC-1 `tools/extract.py`, `tools/prompts.py` | JSON parsing does not adjudicate claim truth |
| [EPI-OBJ-evidence-fields](#epi-obj-evidence-fields) | see record | Requested evidence/relationships | SRC-1 `tools/prompts.py`, `tools/integrate.py` | Not delivered by the integration projection |
| [EPI-OBJ-wiki-body](#epi-obj-wiki-body) | see record | Retained claims and synthesis | SRC-1 `tools/integrate.py`, `tools/newsletter_agent.py` | Import, merge, synthesis and direct-edit lineage differ |
| [EPI-OBJ-wiki-metadata](#epi-obj-wiki-metadata) | see record | Reliance labels and selectors | SRC-1 `tools/integrate.py`, `tools/retrospective_validator.py`, `tools/newsletter_agent.py` | Claimed confidence/verification not calibrated warrant |
| [RT-OBJ-prompts](runtime.md#rt-obj-prompts) | see record | Instructions and registry | SRC-1 `tools/prompts.py` | Guidance and symbolic selection are separate parts; no truth oracle |
| [RT-OBJ-metrics](runtime.md#rt-obj-metrics) | see record | Evaluation aggregates | SRC-1 `tools/metrics_collector.py`, `tools/prompt_optimizer.py` | Self-confidence/process validity, not adjudicated accuracy |
| [EPI-OBJ-eval-set](#epi-obj-eval-set) | see record | Fixed test input | SRC-1 `tools/create_eval_set.py` | No independently labelled answers in the inspected builder |
| [RT-CMP-main-model](runtime.md#rt-cmp-main-model), [RT-CMP-openrouter-model](runtime.md#rt-cmp-openrouter-model) | not determinable for internal state | Inference | SRC-1 `tools/common.py` | Unpinned provider-resolved distributed-parametric state; no accessible content-level acceptance account |

Catalogs, alerts, research-task notes and paper drafts are covered by their route records below rather than treated as another uniform knowledge store. Paper assertions remain candidate text; queries/outlines can be non-truth-apt instructions as well as carry claims. Their exact generated content is not determinable without outputs.

## Authority-route ledger

All architectural statuses concern the route, not observed operation. Every result here is possible under inspected code; none is claimed observed. Repeated route IDs denote distinct consequential functions within a supplied container. The source record owns generic runtime details (`see`); this ledger supplies the epistemic distinctions. “No license” means the check described does not establish factual warrant, not that no true claim could pass it.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-batch-ingestion](runtime.md#rt-rte-batch-ingestion) | content transformation | implemented | [EPI-OBJ-source-text](#epi-obj-source-text) | truth-apt transformation: acquisition/import | External source to normalized input | File/feed admission, not source-truth judgment | see route | Imported text | File creation | Source warrant unknown | Eligible for extraction | Extractor; file body; permissive; later stage | SRC-1 `tools/normalize.py` | [EPI-CLM-knowledge-compilation](#epi-clm-knowledge-compilation) | none | PDF and monitor transformations may lose context |
| [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission) | content transformation | implemented | [EPI-OBJ-extracted-claims](#epi-obj-extracted-claims) | truth-apt transformation: indeterminate | Source body to proposed claims | Model instructed to cite evidence and assess confidence | see route | Candidate JSON text | Advisory model generation | No checked preservation/entailment established | Supplies parser input | Parser; completion string; permissive if parse succeeds; current stage | SRC-1 `tools/extract.py`, `tools/prompts.py` | [EPI-CLM-knowledge-compilation](#epi-clm-knowledge-compilation) | unknown semantic relation | Reshaping, derivation and conjecture cannot be separated without content evidence |
| [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission) | check/evidence production | implemented | [EPI-OBJ-extracted-claims](#epi-obj-extracted-claims) | no content change | Completion syntax as JSON | Python `json.loads`; JSON domain only | Before sidecar assignment/write | Parse success or exception | Enforcing syntax gate | Parseability only; no schema or factual license | Failed parse exits; parsed values proceed to later field operations | Extractor; parse result; enforcing; current invocation | SRC-1 `tools/extract.py` | [EPI-CLM-source-integrity](#epi-clm-source-integrity) | syntax is not evidence validation | Parseable non-object values can still fail later |
| [EPI-RTE-claim-projection](#epi-rte-claim-projection) | content transformation | implemented | [EPI-OBJ-extracted-claims](#epi-obj-extracted-claims), [EPI-OBJ-evidence-fields](#epi-obj-evidence-fields) | truth-apt transformation: non-ampliative reshaping | Sidecar to new-claim Markdown | see record | see record | see record | Fixed projection | Claim text retained, evidence lineage degraded at this edge | Reduced claims become direct-write or merge input | Integrator/model; claim body; informational/permissive; current and future pages | SRC-1 `tools/integrate.py` | [EPI-CLM-source-integrity](#epi-clm-source-integrity) | evidence omitted | Sidecar remains independently available; omission is not source deletion |
| [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission) | content transformation | implemented | [EPI-OBJ-wiki-body](#epi-obj-wiki-body) | truth-apt transformation: indeterminate | Old body plus projected new claims to merged body | Model; merge/history/conflict instruction | Existing destination only | Nonempty merge, conflict marker or empty fallback | Guidance; replacement text supplied | No checked semantics; confidence averaging only requested | Supplies write candidate | Writer; completion body; permissive; destination overwrite | SRC-1 `tools/integrate.py`, `tools/prompts.py` | [EPI-CLM-knowledge-compilation](#epi-clm-knowledge-compilation), [EPI-CLM-source-integrity](#epi-clm-source-integrity) | preservation unenforced | Empty fallback appends, rather than rejecting |
| [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission) | disposition/acceptance | implemented | [EPI-OBJ-wiki-body](#epi-obj-wiki-body) | no content change | New or merged body admitted to wiki | Existence/nonempty-result rules; marker sets conflict status | see route | Write selected even with conflict | Enforcing software admission, not evidence acceptance | No acceptance criterion naming evidence, use and scope | Permits automatic overwrite | Writer; branch/string result; enforcing; current write | SRC-1 `tools/integrate.py` | [EPI-CLM-source-integrity](#epi-clm-source-integrity) | admission differs from acceptance | Human escalation does not veto this write |
| [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission) | retention | implemented | [EPI-OBJ-wiki-body](#epi-obj-wiki-body), [EPI-OBJ-wiki-metadata](#epi-obj-wiki-metadata) | no content change | Selected text to persisted page | see route | see route | Page retained | Durable overwrite | Retention does not add warrant | Future merges/search/synthesis can use it | see [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context) | SRC-1 `tools/integrate.py` | [EPI-CLM-knowledge-compilation](#epi-clm-knowledge-compilation) | none | Not lifecycle integration after evidenced acceptance |
| [RT-RTE-api-mutation](runtime.md#rt-rte-api-mutation) | disposition/acceptance | implemented | [EPI-OBJ-wiki-body](#epi-obj-wiki-body) | truth-apt transformation: indeterminate | Caller text replaces article | Path/I/O only; caller controls content | see route | Direct save | Software admission; human browser authorship possible | No source-truth check | Bypasses extraction/merge | API writer then readers; HTTP/file; permissive; subsequent invocations | SRC-1 `api_server.py` | [EPI-CLM-source-integrity](#epi-clm-source-integrity) | alternate path | Caller text could preserve or revise claims; no output supplied |
| [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance) | check/evidence production | implemented | [EPI-OBJ-wiki-body](#epi-obj-wiki-body) | truth-apt transformation: indeterminate | Direct factual contradiction among page prefixes | Model sees first 600 body characters with basename identities | `lint.py --deep`, at least two included pages | JSON contradiction descriptions or parse failure | Produces advisory semantic judgments | Limited to supplied excerpts; neither fact truth nor complete-page consistency certified | Feeds filename-mapped tagging | Lint tagging; parsed list; permissive; current maintenance run | SRC-1 `tools/lint.py` | [EPI-CLM-source-integrity](#epi-clm-source-integrity) | partial semantic check exists | Basename collisions and truncation limit target resolution/coverage |
| [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance) | disposition/acceptance | implemented | [EPI-OBJ-wiki-metadata](#epi-obj-wiki-metadata) | non-truth-apt policy/content update: conflict annotation | Lint result to status/note | JSON list, filename membership; skip already-conflict page | After deep-lint response | Conflict note/status written | Enforcing tagging; advisory review request | Model diagnosis retained, not independently accepted truth | Adds review visibility; does not block query/synthesis | Writer/catalog; file status/note; advisory to human; later reads | SRC-1 `tools/lint.py`, `tools/index.py`, `tools/query.py` | [EPI-CLM-source-integrity](#epi-clm-source-integrity) | no withdrawal gate | No automatic prior-page restoration |
| [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance) | check/evidence production | implemented | [EPI-OBJ-wiki-metadata](#epi-obj-wiki-metadata) | no content change | Metadata presence, high-unverified confidence, existing conflict marker | Fixed rules; metadata/string domain | Lightweight lint / weekly validation | Warnings, existing-conflict counts | Console/report advisory; conflict status update | Validates representation predicates only | Exposes issues, not factual rejection | Human/report reader; console/report/status; advisory; maintenance horizon | SRC-1 `tools/lint.py`, `tools/retrospective_validator.py` | [EPI-CLM-retrospective-validation](#epi-clm-retrospective-validation) | no new-source comparison in weekly path | Lightweight broken-link counter stays zero; not evidence links were checked |
| [EPI-RTE-reinforcement-selection](#epi-rte-reinforcement-selection) | check/evidence production | implemented | [EPI-OBJ-wiki-metadata](#epi-obj-wiki-metadata) | no content change | Page deemed reinforced | see record | see record | see record | Threshold classification | Source-count/confidence predicate only; no independence or truth license | Permits confidence-update branch | see record | SRC-1 `tools/retrospective_validator.py` | [EPI-CLM-retrospective-validation](#epi-clm-retrospective-validation) | corroboration not established | Integration increments counts per call, not distinct evidence |
| [EPI-RTE-confidence-update](#epi-rte-confidence-update) | behavior/policy adaptation | implemented | [EPI-OBJ-wiki-metadata](#epi-obj-wiki-metadata) | non-truth-apt policy/content update: confidence label increment | Reinforced page to stronger reliance label | see record | see record | see record | Enforcing file update | No new evidential license | Changes downstream confidence-driven selection and displayed aggregates | see record | SRC-1 `tools/retrospective_validator.py` | [EPI-CLM-retrospective-validation](#epi-clm-retrospective-validation) | confidence without new corroboration | Operational effect capacity, not observed behavioral activation |
| [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization) | check/evidence production | implemented | [RT-OBJ-metrics](runtime.md#rt-obj-metrics), [EPI-OBJ-eval-set](#epi-obj-eval-set) | no content change | Existing extractor on first ten available fixtures | Process/JSON success, returned confidence; conflict rate fixed zero | see route | Aggregate metrics | Supplies thresholds | Process validity and self-report only | Drives keep/reject label | Optimizer; numeric deltas; enforcing decision; cycle | SRC-1 `tools/prompt_optimizer.py` | [RT-CLM-prompt-ratchet](runtime.md#rt-clm-prompt-ratchet) | candidate installation missing | Not independent correctness or a controlled candidate contrast |
| [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization) | disposition/acceptance | implemented | [RT-OBJ-prompts](runtime.md#rt-obj-prompts) | non-truth-apt policy/content update: keep/reject experiment bookkeeping | Metric deltas to decision/reset | see route | see route | Keep label or Git reset | Code decision and Git effects | No warrant for proposed prompt effectiveness | Logging/baseline/reset; not candidate activation | see route | SRC-1 `tools/prompt_optimizer.py` | [RT-CLM-prompt-ratchet](runtime.md#rt-clm-prompt-ratchet) | keep is not installation | Mixed reset not a content rollback |
| [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance) | other — describe | implemented | [EPI-OBJ-wiki-metadata](#epi-obj-wiki-metadata) | non-truth-apt policy/content update: research task selection and result labels | Coverage/confidence/age to tasks | Code thresholds; model query/outline requests | see route | Query, task identified or outline; SUCCESS possible | Task scheduling/logging | No completed corroboration established by labels | Logs tasks, not accepted claims | Research logger; result dictionary; advisory; later metrics/notes | SRC-1 `tools/research_agent.py` | [EPI-CLM-retrospective-validation](#epi-clm-retrospective-validation) | none | Claim-bearing generated outlines remain semantically indeterminate |
| [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption) | operational admission/selection/consumption | implemented | [EPI-OBJ-wiki-body](#epi-obj-wiki-body) | no content change | Wiki to query/article/paper context | BM25/top five; explicit path; topic matching/truncation | see route | Ranked paths, article or excerpts | Ranking/delivery | Relevance score does not license truth | Conflict/unverified content can be delivered | API/human/model; responses/user message; ranking/informational; request/later calls | SRC-1 `tools/query.py`, `api_server.py`, `tools/paper_agent.py` | [EPI-CLM-knowledge-compilation](#epi-clm-knowledge-compilation) | semantic-ranking wording exceeds token matching | No fact-based consumer exclusion |
| [EPI-RTE-newsletter-context](#epi-rte-newsletter-context) | content transformation | implemented | [EPI-OBJ-wiki-body](#epi-obj-wiki-body), [EPI-OBJ-wiki-metadata](#epi-obj-wiki-metadata) | truth-apt transformation: non-ampliative reshaping | Recent pages to newsletter context | see record | see record | Snippets and confidence without status | Fixed selection/projection | Warrant degraded by omitted conflict state/context | Supplies synthesis model | see record | SRC-1 `tools/newsletter_agent.py` | [EPI-CLM-source-integrity](#epi-clm-source-integrity) | status collected but dropped | Full files remain available outside model context |
| [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption) | content transformation | implemented | [EPI-OBJ-wiki-body](#epi-obj-wiki-body) | truth-apt transformation: indeterminate | Wiki insights/snippets to synthesis/draft | Model instructions including novelty/strategic interpretation | see route | Generated newsletter/paper candidates | Generation, not acceptance | Neither entailment nor non-entailment shown for actual outputs | Candidate reaches length gate or draft finalizer | see route | SRC-1 `tools/newsletter_agent.py`, `tools/paper_agent.py` | [EPI-CLM-knowledge-compilation](#epi-clm-knowledge-compilation) | requested novelty not demonstrated conjecture | External-source helper supplies placeholder; no measured experiment |
| [EPI-RTE-newsletter-admission](#epi-rte-newsletter-admission) | disposition/acceptance | implemented | [EPI-OBJ-wiki-body](#epi-obj-wiki-body), [EPI-OBJ-wiki-metadata](#epi-obj-wiki-metadata) | non-truth-apt policy/content update: verification and confidence assignment | Generated body to verified newsletter | see record | see record | Saved with confidence 0.95, verified true | Length admission and durable labels | Verification assertion without evidence acceptance | Enters catalog, search and future synthesis scans | see record | SRC-1 `tools/newsletter_agent.py` | [EPI-CLM-source-integrity](#epi-clm-source-integrity) | verified label exceeds check | Count includes all recent paths, not independently corroborating sources |
| [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption) | check/evidence production | implemented | [EPI-OBJ-wiki-body](#epi-obj-wiki-body) | truth-apt transformation: indeterminate | Ordinary paper draft prefix | Model reviewer asked novelty/rigor/clarity/completeness/impact | Two critique/improve rounds; long form skips | Review and improved draft requested; parser can keep whole result | Model proposal; no independent acceptance veto | Critique request only; no empirical novelty/rigor license | Improved text goes onward and is saved as draft | Drafting model/finalizer; selected completion; informational/permissive; current generation | SRC-1 `tools/paper_agent.py` | none | review is not validated research | Review need not persist to next round; missing content-directed criticism evidence |

No post-acceptance lifecycle-integration route is established by these writes. That statement is restricted to the admissions above: ordinary retention/linking/indexing is implemented, but an evidence-consuming acceptance decision antecedent to it has not been established. Human/coding-agent review remains doctrine or external behavior under [RT-BAP-agent-doctrine](runtime.md#rt-bap-agent-doctrine), not a hidden Python gate.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-knowledge-compilation](#epi-clm-knowledge-compilation) | see record | SRC-1 `README.md`; doctrine/design | Extraction/merge instructions | [RT-RTE-batch-ingestion](runtime.md#rt-rte-batch-ingestion), [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission), [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption) | None supplied | No independent variation or benefit measurement | Persistent compilation and reuse are wired; generation is candidate production | Compounding value and semantic correctness not established; BM25 is token-based ranking |
| [EPI-CLM-source-integrity](#epi-clm-source-integrity) | see record | SRC-1 `AGENTS.md`, `llm-wiki.md`, `tools/prompts.py`; doctrine/design | Attribution/history/trust/human escalation rules | [EPI-RTE-claim-projection](#epi-rte-claim-projection), [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission), [RT-RTE-api-mutation](runtime.md#rt-rte-api-mutation), [EPI-RTE-newsletter-context](#epi-rte-newsletter-context), [EPI-RTE-newsletter-admission](#epi-rte-newsletter-admission) | None supplied | No source-independence or full-history check | Citations/markers and review notifications have routes; not invariant safeguards | Evidence field omitted at merge; direct edit bypass; newsletter verified without cross-validation |
| [EPI-CLM-retrospective-validation](#epi-clm-retrospective-validation) | see record | SRC-1 `tools/retrospective_validator.py`; doctrine/design and implementation contrast | Docstring promises new-evidence validation | [EPI-RTE-reinforcement-selection](#epi-rte-reinforcement-selection), [EPI-RTE-confidence-update](#epi-rte-confidence-update), [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance) | None supplied | Metadata repetition is not independent corroboration | Existing conflict detection, threshold reinforcement and confidence writes are implemented | Weekly validation does not invoke new-source contradiction helper; research validation only identifies task |
| [RT-CLM-prompt-ratchet](runtime.md#rt-clm-prompt-ratchet) | see record | SRC-1 `tools/prompt_optimizer.py`; doctrine/design | Metric thresholds and proposal prompt | [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization) | None supplied | Proposed text not installed; conflict metric constant; no candidate contrast | Working proposal/evaluation/bookkeeping machinery | Keep/revert labels do not establish installed improvement or safe rollback |

## Bounded conclusion

**Acquisition and retention:** source text, extracted candidates and wiki content have implemented persistence/reuse paths, with source warrant unknown at acquisition. Deterministic claim projection preserves the supplied claim text but removes the evidence field from the integration input. Later merge semantics are indeterminate, not automatically entailed and not automatically novel. See [EPI-RTE-claim-projection](#epi-rte-claim-projection) and [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission).

**Checks and authority:** JSON parsing can enforce syntax; lint can warn about representation predicates, and deep lint can request semantic contradiction judgments over limited excerpts. Those are real but different checks. Parsed/nonempty/long-enough outputs gain operational authority to be saved and reused, without establishing evidence-consuming acceptance for factual reliance. Conflict tags cause advisory review visibility, not a general block on search or synthesis. The newsletter is a particularly consequential counterpath: it drops status from its model context and assigns verified true/confidence 0.95 after a length gate. See [EPI-RTE-newsletter-context](#epi-rte-newsletter-context), [EPI-RTE-newsletter-admission](#epi-rte-newsletter-admission), and [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance).

**Deterministic reinforcement:** repeated integration of the same input can raise `source_count`; the weekly validator then uses that count and existing confidence to strengthen confidence without reading additional source evidence. This supports a metadata-feedback mechanism, not corroborated knowledge growth or observed degradation. See [EPI-RTE-reinforcement-selection](#epi-rte-reinforcement-selection) and [EPI-RTE-confidence-update](#epi-rte-confidence-update).

**Derivation, conjecture and acceptance:** no inspected route establishes a produced accepted ampliative claim. Actual model output contents are unavailable, so the extraction/merge/synthesis edges remain indeterminate among reshaping, derivation and conjecture. No checked derivation from independently warranted scientific/security premises is established here. The implemented arithmetic predicates and confidence increments support only their narrow metadata-domain deductions. Draft critique requests and publication-ready wording do not certify novelty, experiments or explanatory transfer. Subsequent indexing is retention/organization before established acceptance, not evidence of post-acceptance lifecycle integration.

**Independent properties:** automated schedules and software admission exist; they do not establish reliable autonomy in opaque reasoning. Metrics represent aspects of extraction and affect later proposal selection, but the optimizer lacks the proposal-installation link, so its own candidate-change path does not establish exercised self-improvement. Its localized method text and consumption are separately supported; content-directed criticism and criticism-fed iteration remain unestablished, as detailed in [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization). Paper critique has a request for criticism and two-round revision wiring, but no supplied output establishing a challenged claim, blame placement and carried criticism; that does not justify a theory-builder finding. Retained wiki context and confidence updates can affect later operations independently of the broken prompt installer. No improved future capacity or causal benefit is demonstrated for either. External model parameters, exact versions and provider-side learning remain uninspected under [RT-CMP-main-model](runtime.md#rt-cmp-main-model) and [RT-CMP-openrouter-model](runtime.md#rt-cmp-openrouter-model). These conclusions remain separate; they imply no single epistemic score or system-wide verdict.

## Shared records

### Operative objects

#### EPI-OBJ-source-text
Label: Normalized source text

Source-native identity: body of `raw/normalized/<domain>/<hash>.md`; natural-language content stored in filesystem Markdown. Producer is normalization of downloaded/copied text or PDF text; consumers are extraction and fixture builder. Imported propositions can be truth-apt over their source's stated domain; no truth adjudication occurs in normalization. Distinct from [RT-OBJ-prompts](runtime.md#rt-obj-prompts), which supplies instructions rather than input documents; this input crosses [RT-RTE-batch-ingestion](runtime.md#rt-rte-batch-ingestion), not a separate invocation mechanism. SRC-1: `tools/normalize.py`.

> normalized_content = serialize_frontmatter(metadata, content)
> --- `tools/normalize.py`

#### EPI-OBJ-extracted-claims
Label: Extracted claim text

Source-native identity: `claims[*].text` in extraction JSON, with model-assigned confidence. Natural-language propositions plus associated numerical labels, stored as a filesystem JSON sidecar. Producer is an external completion; consumers are integration and optimizer analysis. A proposition's scope depends on its actual text, unavailable as a traced run here. This is a material output object of [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission), not the prompt referent [RT-OBJ-prompts](runtime.md#rt-obj-prompts). SRC-1: `tools/extract.py`, `tools/prompts.py`.

> "claims": [{"text": str, "confidence": float, "evidence": str}],
> --- `tools/prompts.py:8-16`

> output_path = filepath + ".json"
> --- `tools/extract.py`

#### EPI-OBJ-evidence-fields
Label: Extraction evidence fields

Source-native identity: `claims[*].evidence`, `entities`, `relationships` in the requested JSON. Natural-language evidence/labels with symbolic JSON field structure, persisted if returned in the sidecar. Unlike [EPI-OBJ-extracted-claims](#epi-obj-extracted-claims), these fields do not reach the merge request through the inspected integrator. They are a distinct material object in [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission), not another extraction mechanism. Presence in every returned object is not schema-enforced. SRC-1: `tools/prompts.py`, `tools/extract.py`, `tools/integrate.py`.

> - Cite specific sentences as evidence for each claim
> --- `tools/prompts.py:18-25`

The projection passage in [EPI-RTE-claim-projection](#epi-rte-claim-projection) supports the consumer omission.

#### EPI-OBJ-wiki-body
Label: Wiki page body

Source-native identity: body of wiki Markdown pages, including synthesis/newsletters. Natural-language claims, historical/conflict notes and links stored in filesystem files. Producers differ: initial claim projection, merge completion, API caller, lint annotation, newsletter completion. Consumers include later integration, query/API delivery, paper/newsletter models. Unlike [RT-OBJ-prompts](runtime.md#rt-obj-prompts), this is retained subject matter, not shipped instructions; closest supplied route is [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption), whose reuse passage supplies evidence. SRC-1: `tools/integrate.py`, `api_server.py`, `tools/newsletter_agent.py`. [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context) owns the broad text-to-model path.

#### EPI-OBJ-wiki-metadata
Label: Wiki frontmatter fields

Source-native identity: `source_count`, `confidence`, `verified`, `status` and other page frontmatter. Symbolic values under fixed parser/threshold rules, persisted in Markdown YAML; displayed to humans/models as well. Producers are integrator defaults/count increments, retrospective updates, lint, API caller and newsletter constants. Consumers are catalog aggregation, research task selection, validator reinforcement and newsletter context. Verification/confidence can be interpreted as truth-apt assertions about support, but their implemented force is metadata selection/display, not a proof of factual truth. Distinct from [RT-OBJ-metrics](runtime.md#rt-obj-metrics), which is SQLite/log evaluation state. Closest route containers are [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission) and [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance); this object spans both, not a part of exactly one. SRC-1: `tools/integrate.py`, `tools/retrospective_validator.py`, `tools/newsletter_agent.py`, `tools/index.py`.

> 'source_count': 1,
> 'confidence': 0.8,
> 'verified': False,
> --- `tools/integrate.py`

#### EPI-OBJ-eval-set
Label: Fixed evaluation sources

Source-native identity: `eval_set/` Markdown and `eval_set_index.json`. Natural-language input bodies with symbolic file/domain manifest, stored in filesystem. Builder copies normalized files, balances domains by traversal order and fills from largest domain; optimizer uses first ten manifest items. This differs from [RT-OBJ-metrics](runtime.md#rt-obj-metrics), which stores evaluation outputs, and from [RT-OBJ-prompts](runtime.md#rt-obj-prompts), the method being nominally optimized. It belongs to the evaluation context of [RT-RTE-prompt-optimization](runtime.md#rt-rte-prompt-optimization). SRC-1: `tools/create_eval_set.py`, `tools/prompt_optimizer.py`. No independently adjudicated expected answers are established by copying inputs.

> shutil.copy2(file_info['path'], dest_path)
> --- `tools/create_eval_set.py`

### Routes

#### EPI-RTE-claim-projection
Label: Claim body projection
Part of: [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission)

Endpoints: parsed sidecar → `new_claims_body` → initial page or merge input. Owner is `integrate_knowledge`; fixed Python formatting consumes claim text/confidence/source_id but not evidence/entities/relationships. It is the deterministic material part of the supplied admission container, not a duplicate complete route. SRC-1: `tools/integrate.py`.

- Immediate return: Constructed Markdown body within integration; no separate external return.
- Later read-back: Written text is reloaded by subsequent merges/search/synthesis; omitted sidecar fields have no automatic delivery there.
- Delegated visibility: Merge model sees the projected claim body, not the full JSON.
- Selection predicate: Every element of `data.get('claims', [])`; direct keys text/confidence, optional source_id.
- Invalidation or expiry: Reconstructed per integration; old destination overwritten by containing route.
- Activation or effect: Projection wired; semantics beyond exact text formatting not adjudicated.
- Evidence limits: Deduction from implementation, not an executed example; arbitrary field contents may contain delimiters/instructions.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> new_claims_body = "## Claims\n"
> for claim in data.get('claims', []):
>     new_claims_body += f"- {claim['text']} (Confidence: {claim['confidence']}, Source: [[{data.get('source_id')}]])\n"
> --- `tools/integrate.py`

Concrete symbolic trace: with `source_id = s`, one claim `text = X is Y`, `confidence = 0.7`, `evidence = Sentence E`, the constructed body is `## Claims\n- X is Y (Confidence: 0.7, Source: [[s]])\n`. `Sentence E` is not interpolated. This is non-ampliative formatting of the claim, with degraded evidence delivery, not a novel proposition or a check that X is Y. No target execution was needed.

#### EPI-RTE-reinforcement-selection
Label: Reinforced page selection
Part of: [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance)

Endpoints: recently updated page metadata → reinforced list/eligible confidence branch. Owner is `find_reinforced_claims`; target is the page's recorded count/confidence, not independently verified source agreement. Code decides, no per-page human veto or answer oracle. Mode is open scheduled/CLI maintenance, not a controlled corroboration experiment. SRC-1: `tools/retrospective_validator.py`.

- Immediate return: List of title/confidence/source_count dictionaries; invokes update branch for eligible pages below cap.
- Later read-back: inapplicable — list is current-run state; durable effects belong to the linked update part.
- Delegated visibility: No source text or model request in this selector; code receives metadata snapshots.
- Selection predicate: `source_count >= 3` and `confidence >= 0.75`; confidence below 0.9 additionally enables increment.
- Invalidation or expiry: Inputs refreshed from mtime-selected files on a later validation invocation; no distinct-source test.
- Activation or effect: Predicate controls update invocation, not acceptance of factual truth.
- Evidence limits: Counts can reflect repeated integrations; no observed invocation or independent evidence comparison.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if page['source_count'] >= 3 and page['confidence'] >= 0.75:
> --- `tools/retrospective_validator.py`

> metadata['source_count'] = exist_meta.get('source_count', 0) + 1
> --- `tools/integrate.py`

Concrete countercase: integrate the same well-formed claim JSON three times at the same destination, with merge calls returning empty strings. First write sets count 1/confidence 0.8; later calls increment count to 2 then 3, preserve append-fallback content and reset confidence to 0.8. The validator predicate can now succeed without a second independent source. This is a code-path deduction, not observed operation; no conclusion about actual deployment counts follows.

#### EPI-RTE-confidence-update
Label: Reinforcement confidence update
Part of: [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance)

Endpoints: selected page metadata → increment → rewritten frontmatter → later catalog/research/validation consumers. Code owns admission: selected confidence below 0.9 increases by 0.05 capped at 0.9. The intended reinforcement guidance is the selector's interpretation of count/confidence; no new-source evidence or expected-answer oracle is consumed. Proposed change is a reliance label; software decides, exceptions can prevent write, no built-in content rollback or human veto. Metadata and log persist. Mode is open maintenance; trigger is weekly/CLI validation. This part owns the write, separately from the predicate in [EPI-RTE-reinforcement-selection](#epi-rte-reinforcement-selection). SRC-1: `tools/retrospective_validator.py`, `tools/index.py`; downstream research selectors are also described by [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance).

- Immediate return: Frontmatter update, log entry and adjustment count.
- Later read-back: Later scans reload confidence; catalog averages and research low-confidence selection can depend on it.
- Delegated visibility: File readers receive new confidence with unchanged body; no source text is consulted by this update.
- Selection predicate: Linked reinforcement predicate plus confidence below 0.9.
- Invalidation or expiry: Future integrations can reset confidence; later validators can increment again if still selected; no evidence-expiry check.
- Activation or effect: Durable metadata mutation wired; changed downstream behavior not observed.
- Evidence limits: Numerical increase establishes neither better calibration nor increased factual support.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> new_confidence = min(0.9, page['confidence'] + 0.05)
> self.update_page_confidence(page['path'], new_confidence)
> --- `tools/retrospective_validator.py`

> meta['confidence'] = new_confidence
> --- `tools/retrospective_validator.py`

For the predicate countercase's 0.8 input, the expression yields 0.85, modulo ordinary floating-point representation. It changes a support label, not the underlying claim or its evidence.

#### EPI-RTE-newsletter-context
Label: Newsletter context projection
Part of: [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption)

Endpoints: recent wiki files → category entries → first five entries per bucket → model context. Owner is newsletter code. Targets include current, unverified or conflict pages because recentness selection does not inspect status. `status` is collected in entries but omitted from formatting; confidence remains. This distinct part qualifies the broad supplied synthesis container without superseding it. SRC-1: `tools/newsletter_agent.py`.

- Immediate return: Concatenated section-context string for the current completion request.
- Later read-back: inapplicable — this string is current-run context; newsletter retention belongs to the linked admission part.
- Delegated visibility: Model receives titles, paths, confidence and 400-character body prefixes, at most five per bucket, but no status field.
- Selection predicate: Mtime within lookback; omit index/log; bucket by domain/path; traversal order within bucket.
- Invalidation or expiry: Context rebuilt per call; full files remain available on filesystem outside model input.
- Activation or effect: Projection wired; no guarantee snippets contain conflict notes or preserve all qualifications.
- Evidence limits: Code deduction supports lost status channel; no observed false synthesis is asserted.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> 'status': meta.get('status', 'current'),
> 'snippet': body.strip()[:400],
> --- `tools/newsletter_agent.py`

> for e in entries[:max_items]:
>     lines.append(f"TITLE: {e['title']}\nPATH: {e['path']}\nCONFIDENCE: {e['confidence']}\nSNIPPET: {e['snippet']}\n")
> --- `tools/newsletter_agent.py`

#### EPI-RTE-newsletter-admission
Label: Newsletter verification assignment
Part of: [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption)

Endpoints: completion body → length decision → fixed frontmatter → saved wiki newsletter → catalog/search/future scans. Code owns admission; model proposes body under an instruction not to invent information. The proposed product is synthesized prose; software rejects absent/short response, otherwise assigns confidence 0.95, verified true and current status. No source-evidence comparison, human veto or independent answer oracle at that decision. Trigger is CLI generation with recent input pages; mode is open synthesis. Guidance persists as source prompt; body/labels persist as dated Markdown. Re-run may overwrite same-date file; errors are not automatic rollback. This material part is not another complete synthesis route. SRC-1: `tools/newsletter_agent.py`, `tools/query.py`, `tools/index.py`.

- Immediate return: Saved newsletter, console/log output and attempted catalog rebuild.
- Later read-back: Query/index include newsletter; future recent-page synthesis and topic-matched paper selection can include it.
- Delegated visibility: Readers receive generated prose with unconditional support labels; raw source evidence is not inspected by the length gate.
- Selection predicate: Nonempty body with length at least 200 characters; recent_paths nonempty before generation.
- Invalidation or expiry: Same-date path can be overwritten; no verification expiry or independent retraction mechanism here.
- Activation or effect: Durable verified/confidence assignment and read eligibility wired; factual grounding and changed behavior unobserved.
- Evidence limits: Label is not an evidence-consuming acceptance decision; source_count counts paths, not independent corroboration.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not newsletter_body or len(newsletter_body) < 200:
> --- `tools/newsletter_agent.py`

> f"source_count: {len(recent_paths)}\n"
> f"confidence: 0.95\n"
> f"verified: true\n"
> --- `tools/newsletter_agent.py`

> "Do not invent information not present in the context."
> --- `tools/newsletter_agent.py`

The last passage is a source-supported counterweight: factual restraint is requested. It does not turn the length predicate into verification.

### Claims

#### EPI-CLM-knowledge-compilation
Label: Stateful knowledge compilation

Claimed operation: sources become a persistent cross-linked, compounding wiki with BM25 semantic ranking. SRC-1 `README.md`, doctrine/design. No counterpart among supplied claims after comparison: [RT-CLM-prompt-ratchet](runtime.md#rt-clm-prompt-ratchet) concerns prompt improvement, not source-to-wiki compilation. Relevant supplied routes are [RT-RTE-batch-ingestion](runtime.md#rt-rte-batch-ingestion) and [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption).

> The result is a knowledge base that **compounds over time** — every new source enriches the existing structure rather than existing in isolation.
> --- `README.md`

> 5. **Queryable** — the wiki is searched with BM25 semantic ranking
> --- `README.md`

#### EPI-CLM-source-integrity
Label: Attribution and trust constraints

Claimed operation: claim attribution/confidence follows source tiers; conflicts preserve history and trigger human escalation; specification requires source tier and verification state per claim and independent corroboration before CVE verification. SRC-1 `AGENTS.md`, `llm-wiki.md`, `tools/prompts.py`, doctrine/design. Distinct from [RT-CLM-prompt-ratchet](runtime.md#rt-clm-prompt-ratchet); closest supplied evidence is [RT-BAP-agent-doctrine](runtime.md#rt-bap-agent-doctrine), a delivery/authority path rather than this claim.

> - Each extracted claim must include a citation inline, linking back to `/raw/normalized/<domain>/<filename>.md`.
> - Confidence must be rated based on source tiers in Section 7.
> --- `AGENTS.md`

> - When conflicts arise with a CVSS >= 7.0 or if explicitly flagged by a direct contradiction on a high-confidence topic, pause and raise to the human user by updating the file status to `conflict` and bringing it to the user's attention appropriately.
> --- `AGENTS.md`

> \- Claims are cross-validated across a minimum of two independent sources before `verified: true`
> --- `llm-wiki.md`

Scope caution: the specification's minimum-two-sources rule explicitly concerns CVE entries, not every newsletter. Newsletter verification nevertheless lacks any evidence check of its own; that finding does not require extending the CVE rule to all products.

#### EPI-CLM-retrospective-validation
Label: Old claims against new evidence

Claimed operation: retrospective validation checks old claims against new sources, detects contradictions and adjusts confidence. SRC-1 `tools/retrospective_validator.py`, doctrine/design. Distinct from the supplied prompt-ratchet claim; [RT-RTE-research-maintenance](runtime.md#rt-rte-research-maintenance) supplies the relevant broad implementation container rather than a duplicate claim.

> Retrospective validator that checks old claims against new sources.
> Detects contradictions and adjusts confidence scores.
> --- `tools/retrospective_validator.py`

> # Check for contradictions (simplified - would need actual new sources)
> # For now, just check if page has [CONFLICT] tags
> --- `tools/retrospective_validator.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
