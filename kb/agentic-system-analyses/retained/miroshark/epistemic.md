---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "MiroShark epistemic routes: graph assertions, heuristic belief adaptation, report evidence and outcome-to-trading authority."
run-id: AAS-2026-10-15-miroshark-b3df0e053a29-01
reviewed-boundary: e95d3d8c2a2206b8b6695648e8504cf23436d3de
---

# MiroShark epistemic report

## Source-and-claim boundary

The question is how document/model/simulation content becomes relied-on graph material, agent context, reports and publicly labeled results. Scope, exclusions and frozen evidence identity: see the [boundary](boundary.md#boundary-and-evidence) and its [Source register](boundary.md#source-register), SRC-1. This is a source-grounded, not executed, account. No supplied trace, factual corpus, actual provider response, deployed database or causal comparison establishes operation, factual accuracy, calibration or benefit. External dependency/model internals remain uninspected. Models can supply truth-apt assertions; their inaccessible processing is not evidence of either acceptance or its absence.

The whole-system boundary remains unchanged. Coverage below distinguishes this member's direct source inspection from supplied runtime findings. Unassessed included paths prevent a system-complete negative about checking, acceptance, knowledge production or adaptation. Every direct source reference below is SRC-1 at the reviewed commit. Source-native warrant claims: see the claim records in block 4; graph-memory claim identity remains the runtime's.

| Entry point / operation | Source path (SRC-1) | Coverage and records / limit |
|---|---|---|
| Launcher, HTTP application and model/tool action loop | `miroshark`, `backend/app/__init__.py`, `backend/scripts/run_parallel_simulation.py` | Supplied runtime findings: [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds), [RT-RTE-interview-manual](runtime.md#rt-rte-interview-manual), [RT-RTE-agent-mcp](runtime.md#rt-rte-agent-mcp), [RT-RTE-director-context](runtime.md#rt-rte-director-context). Driver/hooks not independently exhaustively read here; no universal action-check verdict. |
| Installed CLI dispatch | `backend/pyproject.toml`, `backend/cli.py` | Direct script registration/parser/helper call-site inspection: ask, list, status, wait, stop, frame, publish, report, cost, trending, health. Ask is a material upstream operation absent from runtime's route inventory; see [EPI-RTE-ask-briefing](#epi-rte-ask-briefing). Status/cost/health are not truth-warrant evaluators of simulation claims. Trending dispatch is inspected; feed fetch/extraction and URL-import semantics remain unassessed, preventing an acquisition-complete account. |
| Graph ingestion, resolution, withdrawal and retrieval | `backend/app/storage/ner_extractor.py`, `backend/app/storage/neo4j_storage.py`, `backend/app/storage/entity_resolver.py`, `backend/app/storage/contradiction_detector.py`, `backend/app/storage/search_service.py` | Direct bounded function reads; see graph route records. Detailed resolver model-response parser, all Cypher paths and source extraction before add_text are unassessed; no exhaustive identity/fidelity guarantee. |
| Profile/config preparation | `backend/app/services/wonderwall_profile_generator.py`, `backend/app/services/web_enrichment.py` | Supplied [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population); direct enrichment research-body read and generator call-site search, [EPI-RTE-web-research](#epi-rte-web-research). Demographic sampling, remote data and complete config/ontology generation unassessed; demographic fidelity and source-complete grounding not established. |
| Round history and belief adaptation | `backend/scripts/round_memory.py`, `backend/scripts/belief_integration.py`, `backend/wonderwall/social_agent/belief_state.py` | Direct compaction, update, serialization/injection and trajectory-merge reads; [EPI-RTE-round-compaction](#epi-rte-round-compaction), [EPI-RTE-belief-revision](#epi-rte-belief-revision). RoundAnalyzer located by search but full perception construction unassessed; conclusions concern supplied-input update rules, not complete agent exposure. Single-platform equivalence unestablished. |
| Simulation activity graph update | `backend/app/services/graph_memory_updater.py` | Direct batch tagging/write read; [EPI-RTE-graph-retention](#epi-rte-graph-retention). Updater activation remains conditional; no completeness observation. |
| stdio registered tools and communities | `backend/mcp_server.py`, `backend/app/storage/community_builder.py` | Direct complete dispatch read plus bounded build/summary/delete/write reads; [RT-RTE-storage-mcp](runtime.md#rt-rte-storage-mcp), [EPI-RTE-community-generation](#epi-rte-community-generation). All eight dispatched operations accounted for: graph listing/search, cluster browse/search/detail, report listing/sections/trace. No separate truth evaluator appears in these branches. Clustering implementation is not fully assessed. |
| Reports, tool catalogue, cleanup and deletion | `backend/app/services/report_agent.py`, `backend/app/api/report.py`, `backend/app/storage/neo4j_storage.py` | Supplied [RT-RTE-report-sections](runtime.md#rt-rte-report-sections); direct catalogue/dispatch searches, completion/trace initialization/cleanup/delete reads and contradiction-scan body; [EPI-RTE-contradiction-flags](#epi-rte-contradiction-flags), [EPI-RTE-report-cleanup](#epi-rte-report-cleanup). Synthesis/chat/equilibrium implementations, graph-tool output transformations and full trace persistence unassessed; prevents report-complete negative or all-store retraction claim. |
| Quality, binary resolution, public outcome annotation | `backend/app/api/simulation.py`, `backend/app/services/gallery_filters.py`, `backend/app/services/feed.py` | Direct API evaluator/admission bodies and gallery filter; feed category call sites searched. See three evaluator/admission records. These omitted runtime operations defeat any reading that the system has no post-run evaluation. |
| Machine-readable trading derivatives | `backend/app/services/signal_service.py`, `backend/app/services/polymarket_service.py`, `backend/app/api/simulation.py` | Direct algorithm bodies and HTTP call/readiness/cache branches; [EPI-RTE-signal-derivation](#epi-rte-signal-derivation). Embed-summary producer and all alternate share surfaces not fully traced; arithmetic witness is conditional on supplied summary, not authenticated event probability. Signed results, publication, archive/export and notifications remain unassessed beyond identified call sites, preventing a complete downstream reliance/retraction account. |
| Tests and CI | `.github/workflows/tests.yml`, `backend/tests/test_smoke_camel_agent.py` | Search of workflow commands and smoke assertions only, in addition to supplied boundary. Source specifies compatibility/unit checks, not observed successful execution or predictive validity. No benchmark corpus/results supplied. |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-report-section](#epi-obj-report-section) | Narrative descriptions, explanations and implications about a simulation and its possible real-world relevance. | see [EPI-OBJ-report-section](#epi-obj-report-section) | SRC-1, `backend/app/services/report_agent.py` | Provider outputs absent; faithful synthesis versus additional conjecture cannot be classified. |
| [EPI-OBJ-interview-response](#epi-obj-interview-response) | Answers attributed to simulated agents; any world assertions or self-reports have participant/scenario scope, not automatic real-person testimony. | see [EPI-OBJ-interview-response](#epi-obj-interview-response) | SRC-1, `backend/wonderwall/social_agent/agent.py` | No actual question/response or restoration trace supplied; truth-apt instances not determinable. |
| [EPI-OBJ-tool-result](#epi-obj-tool-result) | Not determinable without actual tools/results: results may contain assertions, effect acknowledgments or errors. | see [EPI-OBJ-tool-result](#epi-obj-tool-result) | SRC-1, `backend/scripts/mcp_agent_bridge.py` | Remote source warrant and result semantics uninspected. |
| [EPI-OBJ-director-event](#epi-obj-director-event) | Caller-supplied event assumptions can contain truth-apt assertions, but are consumed as a scenario intervention rather than established world facts. | see [EPI-OBJ-director-event](#epi-obj-director-event) | SRC-1, `backend/scripts/director_events.py` | Actual event contents and compliance unobserved. |
| [EPI-OBJ-seed-document](#epi-obj-seed-document) | Question-conditioned assertions about named actors and events; truth-apt in the stated scenario/world scope. | see [EPI-OBJ-seed-document](#epi-obj-seed-document) | SRC-1, `backend/app/api/simulation.py` | No captured briefing or factual reference. |
| [EPI-OBJ-graph-relations](#epi-obj-graph-relations) | Assertions connecting named entities, attributed to an input episode. | see [EPI-OBJ-graph-relations](#epi-obj-graph-relations) | SRC-1, `backend/app/storage/neo4j_storage.py` | Input truth and extraction fidelity are separate unknowns. |
| [EPI-OBJ-entity-summaries](#epi-obj-entity-summaries) | Descriptions and identity claims about graph entities. | see [EPI-OBJ-entity-summaries](#epi-obj-entity-summaries) | SRC-1, `backend/app/storage/neo4j_storage.py` | Merged identity can combine descriptions from different inputs. |
| [EPI-OBJ-research-context](#epi-obj-research-context) | Entity biography/background assertions supplied to persona generation. | see [EPI-OBJ-research-context](#epi-obj-research-context) | SRC-1, `backend/app/services/web_enrichment.py` | Search snippets, model prior knowledge and actual outputs uncaptured. |
| [EPI-OBJ-round-record](#epi-obj-round-record) | Claims about simulated actions and dynamics, not real-world events. | see [EPI-OBJ-round-record](#epi-obj-round-record) | SRC-1, `backend/scripts/round_memory.py` | Model summarization fidelity unobserved; fallback counts have a narrower domain. |
| [EPI-OBJ-belief-state](#epi-obj-belief-state) | A simulated attitude/control state; a topic position is not itself a proposition with an independently specified truth condition. | see [EPI-OBJ-belief-state](#epi-obj-belief-state) | SRC-1, `backend/wonderwall/social_agent/belief_state.py` | Real belief, calibrated confidence and truth of positions not established. |
| [EPI-OBJ-community-summary](#epi-obj-community-summary) | Claims about what selected graph entities have in common. | see [EPI-OBJ-community-summary](#epi-obj-community-summary) | SRC-1, `backend/app/storage/community_builder.py` | Prompt samples at most 15 members with 100-character descriptions. |
| [EPI-OBJ-quality](#epi-obj-quality) | Participation, stance diversity, convergence and platform-interaction statistics over recorded simulation data. | see [EPI-OBJ-quality](#epi-obj-quality) | SRC-1, `backend/app/api/simulation.py` | Health is a rule-defined label, not predictive accuracy. |
| [EPI-OBJ-resolution](#epi-obj-resolution) | Whether selected final market consensus agrees with a supplied YES/NO outcome. | see [EPI-OBJ-resolution](#epi-obj-resolution) | SRC-1, `backend/app/api/simulation.py` | Outcome provenance and event/market alignment are caller obligations. |
| [EPI-OBJ-outcome](#epi-obj-outcome) | An administrator asserts a public run was correct, incorrect or partial. | see [EPI-OBJ-outcome](#epi-obj-outcome) | SRC-1, `backend/app/api/simulation.py` | URL is optional and is not fetched by admission. |
| [EPI-OBJ-signal](#epi-obj-signal) | Numerical restatements of simulated stance fractions; stronger event-probability interpretation needs additional warrant. | see [EPI-OBJ-signal](#epi-obj-signal) | SRC-1, `backend/app/services/signal_service.py` | Probability calibration and actual bot consumption unobserved. |
| [RT-OBJ-agent-profiles](runtime.md#rt-obj-agent-profiles) | Persona assertions can be true/false as biography, but simulated persona assumptions are not established population facts. | see [RT-OBJ-agent-profiles](runtime.md#rt-obj-agent-profiles) | see [RT-OBJ-agent-profiles](runtime.md#rt-obj-agent-profiles) | No demographic or behavioral validation observed. |
| [RT-OBJ-simulation-config](runtime.md#rt-obj-simulation-config) | None for platform/time/ID control fields; scenario probabilities and generated rationale need separate assessment. | see [RT-OBJ-simulation-config](runtime.md#rt-obj-simulation-config) | see [RT-OBJ-simulation-config](runtime.md#rt-obj-simulation-config) | Full generated rationale/market-origin semantics unassessed. |

Distributed-parametric substrates are not interchangeable with these retained objects: see [RT-CMP-model-clients](runtime.md#rt-cmp-model-clients), [RT-CMP-embedding-service](runtime.md#rt-cmp-embedding-service), [RT-CMP-reranker-service](runtime.md#rt-cmp-reranker-service), [RT-CMP-twhin-bert](runtime.md#rt-cmp-twhin-bert) and [RT-CMP-paraphrase-minilm](runtime.md#rt-cmp-paraphrase-minilm). Their component-specific fixity/version limits remain those records' fields. No accessible source or supplied execution establishes provider-side parameter learning. Belief updates and summary memory remain independent of that limit.

## Authority-route ledger

All listed routes have architectural status `implemented`: inspected source supports the path, not successful operation. Repeated rows distinguish functions of one implementation; a checking row never supplies disposition by implication. Fields owned by declaring records say `see`. No row claims lifecycle integration of accepted ampliative knowledge merely from storage or use.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-RTE-ask-briefing](#epi-rte-ask-briefing) | content transformation | implemented | [EPI-OBJ-seed-document](#epi-obj-seed-document) | truth-apt transformation: indeterminate | Question → purported actor/event briefing | Smart-model interpretation, open scenario | see [EPI-RTE-ask-briefing](#epi-rte-ask-briefing) | Candidate briefing | Permissive schema admission | Unknown source warrant; acquisition from model priors vs newly conjectured assertions cannot be distinguished from prompts alone. | Eligible seed for graph workflow | Graph client → briefing text → advisory/permissive → later setup | see [EPI-RTE-ask-briefing](#epi-rte-ask-briefing) | none | none | Need output and provenance to distinguish imported prior content, faithful reshaping and non-entailed additions. |
| [EPI-RTE-web-research](#epi-rte-web-research) | content transformation | implemented | [EPI-OBJ-research-context](#epi-obj-research-context) | truth-apt transformation: indeterminate | Entity context → synthesized biography | Model with optional snippets | see [EPI-RTE-web-research](#epi-rte-web-research) | Research prose or empty | Permissive length gate | Snippet acquisition is external import with unknown warrant; synthesis fidelity unknown. | Available persona context | Profile generator → research section → advisory → profile generation | see [EPI-RTE-web-research](#epi-rte-web-research) | [EPI-CLM-grounded-personas](#epi-clm-grounded-personas) | none | Need retrieved sources and generated text; no claim all enrichment is fabricated or all grounded. |
| [EPI-RTE-graph-extraction](#epi-rte-graph-extraction) | content transformation | implemented | [EPI-OBJ-graph-relations](#epi-obj-graph-relations) | truth-apt transformation: indeterminate | Input text → relation assertions/descriptions | NER model conditioned on ontology | see [EPI-RTE-graph-extraction](#epi-rte-graph-extraction) | Extraction candidates | Candidate generation | Intended source extraction; semantic preservation/entailment not established. | Candidates reach cleaner | Cleaner → parsed JSON → permissive → current ingestion | see [EPI-RTE-graph-extraction](#epi-rte-graph-extraction) | [EPI-CLM-epistemic-kinds](#epi-clm-epistemic-kinds) | none | Could import/reshape or add unsupported content; output-to-source comparison needed. |
| [EPI-RTE-graph-extraction](#epi-rte-graph-extraction) | check/evidence production | implemented | [EPI-OBJ-graph-relations](#epi-obj-graph-relations) | no content change | Extraction structure, names, endpoint shape | Deterministic lexical/structural rules | see [EPI-RTE-graph-extraction](#epi-rte-graph-extraction) | Cleaned/rejected items | Enforcing structure | Licenses only conformity to inspected syntactic/name rules, not source truth. | Filters candidates; missing endpoints can be added | Storage writer → cleaned dictionaries → enforcing → current ingestion | see [EPI-RTE-graph-extraction](#epi-rte-graph-extraction) | none | none | Witness: entity AI is rejected (length <=2); a valid relation source AI with other endpoint Acme can recreate AI as Entity. This is code deduction, not execution. |
| [EPI-RTE-entity-resolution](#epi-rte-entity-resolution) | check/evidence production | implemented | [EPI-OBJ-entity-summaries](#epi-obj-entity-summaries) | no content change | Candidate identities within graph | Fuzzy/vector similarity; optional same-entity model judgment | see [EPI-RTE-entity-resolution](#epi-rte-entity-resolution) | Scores and canonical match proposal | Ranking/advisory | Fallible identity evidence within bounded candidate corpus. | Offers canonical identity | Resolution selector → scores/verdict → ranking → batch | see [EPI-RTE-entity-resolution](#epi-rte-entity-resolution) | none | none | Similarity does not prove identity; missing or ambiguous candidates can remain separate. |
| [EPI-RTE-entity-resolution](#epi-rte-entity-resolution) | disposition/acceptance | implemented | [EPI-OBJ-entity-summaries](#epi-obj-entity-summaries) | no content change | Canonical identity chosen for MERGE | >=0.95 auto-match; >=0.70 optional model match | see [EPI-RTE-entity-resolution](#epi-rte-entity-resolution) | Recorded canonical-name map | Enforcing matching decision | Acceptance criterion is identity-selection policy for deduplication, not relation truth. | Changes canonical endpoints and attributes | add_text → resolution map → enforcing → persistent merged graph | see [EPI-RTE-entity-resolution](#epi-rte-entity-resolution) | none | none | No independently verified identity or demonstrated undo. |
| [EPI-RTE-graph-retention](#epi-rte-graph-retention) | retention | implemented | [EPI-OBJ-graph-relations](#epi-obj-graph-relations) | truth-apt transformation: acquisition/import | Caller text/extraction → episode and graph | Storage/schema rules; kind supplied by caller | see [EPI-RTE-graph-retention](#epi-rte-graph-retention) | Retained candidate relations | Permissive persistence | Lineage metadata retained; external source warrant unknown, extraction/merge can degrade it. | Makes candidates available for later search/setup | Graph consumers → persisted edges/descriptions → advisory → subsequent requests | see [EPI-RTE-graph-retention](#epi-rte-graph-retention) | [RT-CLM-graph-memory](runtime.md#rt-clm-graph-memory); [EPI-CLM-epistemic-kinds](#epi-clm-epistemic-kinds) | none | fact is not an evidence-consuming truth acceptance. Simulation kind assigned per batch, not proposition. |
| [EPI-RTE-edge-adjudication](#epi-rte-edge-adjudication) | check/evidence production | implemented | [EPI-OBJ-graph-relations](#epi-obj-graph-relations) | no content change | Old/new same-endpoint fact compatibility | LLM OLD/NEW test; assumes newer supersedes older | see [EPI-RTE-edge-adjudication](#epi-rte-edge-adjudication) | Contradicts/not_contradicts | Advisory to withdrawal code | Defeasible textual incompatibility judgment, not new-fact verification. | Produces old-edge withdrawal list | add_text → UUID verdict list → advisory → ingestion | see [EPI-RTE-edge-adjudication](#epi-rte-edge-adjudication) | none | none | Failure defaults to no withdrawal; kind/source and original evidence not part of adjudication. |
| [EPI-RTE-edge-invalidation](#epi-rte-edge-invalidation) | disposition/acceptance | implemented | [EPI-OBJ-graph-relations](#epi-obj-graph-relations) | no content change | Old-edge current reliance | UUID selection from verdict/caller | see [EPI-RTE-edge-invalidation](#epi-rte-edge-invalidation) | Invalidated timestamps | Enforcing current-edge filter | Withdraws current-edge status only; no positive new-fact acceptance. | Suppresses old edge in default edge search | SearchService → invalid_at → enforcing → later current-edge queries | see [EPI-RTE-edge-invalidation](#epi-rte-edge-invalidation) | [EPI-CLM-epistemic-kinds](#epi-clm-epistemic-kinds) | none | Historical queries can recover; existing reports/communities/node descriptions not thereby retracted. |
| [EPI-RTE-graph-ranking](#epi-rte-graph-ranking) | operational admission/selection/consumption | implemented | [EPI-OBJ-graph-relations](#epi-obj-graph-relations) | no content change | Graph results relevant to query/time/kind | Hybrid scores, optional reranker, filters | see [EPI-RTE-graph-ranking](#epi-rte-graph-ranking) | Limited hits | Ranking | Relevance/currentness/category, not endorsement. | Supplies selected facts to generators/report/MCP | Generation or external client → retrieved JSON/text → advisory/ranking → invocation | see [EPI-RTE-graph-ranking](#epi-rte-graph-ranking) | [EPI-CLM-epistemic-kinds](#epi-clm-epistemic-kinds) | none | Node direct-hit paths ignore temporal/kind filters; no universal clean-current view. |
| [EPI-RTE-round-compaction](#epi-rte-round-compaction) | content transformation | implemented | [EPI-OBJ-round-record](#epi-obj-round-record) | truth-apt transformation: indeterminate | Action descriptions → salience summary | Historian model; deterministic fallback counts | see [EPI-RTE-round-compaction](#epi-rte-round-compaction) | Summary or counts | Permissive summary admission | Model summary may reshape or infer; fidelity unknown. Fallback counts are narrow derivations over filtered records. | Replaces old model-visible detail | RoundMemory → later context → advisory → subsequent rounds | see [EPI-RTE-round-compaction](#epi-rte-round-compaction) | none | none | No summary-to-record verification. Count fallback is not evidence all events were retained. |
| [EPI-RTE-round-compaction](#epi-rte-round-compaction) | retention | implemented | [EPI-OBJ-round-record](#epi-obj-round-record) | no content change | Summary available after compactor returns | Code retains stripped result | see [EPI-RTE-round-compaction](#epi-rte-round-compaction) | Compacted/ancient memory | Permissive | Retention before epistemic acceptance. | Old summary reaches next model invocation | SocialAgent → system context → advisory → rounds while retained | see [EPI-RTE-round-compaction](#epi-rte-round-compaction) | none | none | Replacement is not lifecycle integration of an accepted claim. |
| [EPI-RTE-belief-revision](#epi-rte-belief-revision) | behavior/policy adaptation | implemented | [EPI-OBJ-belief-state](#epi-obj-belief-state) | non-truth-apt policy/content update: simulated stance/trust | Post/engagement signals → attitudes/confidence | Substring sentiment, topic overlap, trust/novelty/like weights | see [EPI-RTE-belief-revision](#epi-rte-belief-revision) | Scalar changes and prompt labels | Enforcing scalar update; advisory model use | No factual accuracy license; confidence tracks rule-defined social reinforcement. | Changes future context/saved state | Agent model → belief system text → advisory → later rounds/resume | see [EPI-RTE-belief-revision](#epi-rte-belief-revision) | none | none | Counterexample: “I disagree about AI” counts agree and disagree, yielding 0.0, not opposition; topic AI matches. Social adaptation exists independently of truth testing. |
| [EPI-RTE-community-generation](#epi-rte-community-generation) | content transformation | implemented | [EPI-OBJ-community-summary](#epi-obj-community-summary) | truth-apt transformation: indeterminate | Graph groups → descriptive labels | Clustering plus model summary of sampled descriptions | see [EPI-RTE-community-generation](#epi-rte-community-generation) | Labels/fallbacks | Permissive | Membership grouping follows graph algorithm; descriptive entailment unresolved. | Changes browsing/retrieval framing | Community reader → titles/summaries → advisory → future requests | see [EPI-RTE-community-generation](#epi-rte-community-generation) | none | none | Label synthesis is not automatically non-ampliative or accepted ampliative knowledge. |
| [EPI-RTE-community-generation](#epi-rte-community-generation) | retention | implemented | [EPI-OBJ-community-summary](#epi-obj-community-summary) | no content change | Labels/members replace previous communities | Size/count gates and write code | see [EPI-RTE-community-generation](#epi-rte-community-generation) | New community store | Enforcing replacement | Retention and organization without separate acceptance. | MCP/report can consume new labels | Browse/search → stored community text → advisory → until rebuild | see [EPI-RTE-community-generation](#epi-rte-community-generation) | none | none | Deletion/write not one transaction; too-small early return does not clear old communities. |
| [EPI-RTE-contradiction-flags](#epi-rte-contradiction-flags) | check/evidence production | implemented | [EPI-OBJ-graph-relations](#epi-obj-graph-relations) | no content change | Directed pairs with opposite lexical sentiment | Substring positive/negative counts | see [EPI-RTE-contradiction-flags](#epi-rte-contradiction-flags) | opposing_sentiments list | Advisory | Potential conflict hint, not logical refutation or fact verification. | Report may reconsider narrative | ReportAgent tool observation → natural language/JSON → advisory → section | see [EPI-RTE-contradiction-flags](#epi-rte-contradiction-flags) | none | none | No current-edge filter; no withdrawal consumer. “support X” and “oppose X” can flag but may concern different times/aspects. |
| [EPI-RTE-quality-diagnostics](#epi-rte-quality-diagnostics) | check/evidence production | implemented | [EPI-OBJ-quality](#epi-obj-quality) | truth-apt transformation: entailed derivation | Recorded participation/diversity/interaction | Deterministic metrics/badge criteria | see [EPI-RTE-quality-diagnostics](#epi-rte-quality-diagnostics) | Metrics and health | Advisory | Arithmetic and rule-defined activity health, conditional on input records, not forecast validity. | Suggests configurations; supplies quality class | API/gallery/signal → metrics/badge → advisory/filter/risk labeling → future requests | see [EPI-RTE-quality-diagnostics](#epi-rte-quality-diagnostics) | none | none | No external target outcome, causal contrast or autonomous application of suggestions. |
| [EPI-RTE-quality-diagnostics](#epi-rte-quality-diagnostics) | retention | implemented | [EPI-OBJ-quality](#epi-obj-quality) | no content change | Diagnostics cache | File exists → return cached | see [EPI-RTE-quality-diagnostics](#epi-rte-quality-diagnostics) | quality.json | Permissive cache reuse | Stored appraisal, not renewed endorsement or freshness. | May reuse mid-run/stale badge | Gallery/signal → cached health → ranking/filter/advisory → until file replaced | see [EPI-RTE-quality-diagnostics](#epi-rte-quality-diagnostics) | none | none | No cache invalidation criterion in inspected handler. |
| [EPI-RTE-prediction-resolution](#epi-rte-prediction-resolution) | check/evidence production | implemented | [EPI-OBJ-resolution](#epi-obj-resolution) | truth-apt transformation: entailed derivation | Selected market consensus vs supplied binary outcome | Code comparison; admin supplies reference | see [EPI-RTE-prediction-resolution](#epi-rte-prediction-resolution) | 1/0, split 0.5, or null | Advisory | Agreement with caller reference for one selected market; reference correctness unverified. | Records a bounded post-hoc score | Summary/share consumers → score → advisory → later reads | see [EPI-RTE-prediction-resolution](#epi-rte-prediction-resolution) | none | none | Not a causal experiment; no process/explanation/transfer license; no supplied resolutions. |
| [EPI-RTE-prediction-resolution](#epi-rte-prediction-resolution) | retention | implemented | [EPI-OBJ-resolution](#epi-obj-resolution) | no content change | Post-hoc score and reference | Valid authenticated POST | see [EPI-RTE-prediction-resolution](#epi-rte-prediction-resolution) | resolution.json | Permissive overwrite | Attributed reference retained; not independent validation. | Available for public summary/display | Summary/reporting surfaces → resolution file → advisory → until overwrite | see [EPI-RTE-prediction-resolution](#epi-rte-prediction-resolution) | none | none | Caller can change outcome; no evidence-consuming simulator update traced. |
| [EPI-RTE-outcome-annotation](#epi-rte-outcome-annotation) | disposition/acceptance | implemented | [EPI-OBJ-outcome](#epi-obj-outcome) | truth-apt transformation: acquisition/import | Caller correctness appraisal for public run | Admin token, enum, URL shape/length; no URL-content test | see [EPI-RTE-outcome-annotation](#epi-rte-outcome-annotation) | Admitted correct/incorrect/partial label | Permissive content admission | Acquired attributed appraisal; source warrant unknown. Not independent acceptance against event evidence. | Eligible for verified-only inclusion | Gallery filter → label presence → enforcing inclusion → public reads | see [EPI-RTE-outcome-annotation](#epi-rte-outcome-annotation) | [EPI-CLM-verified-outcomes](#epi-clm-verified-outcomes) | none | URL optional; user/human evidence review unobserved. |
| [EPI-RTE-outcome-annotation](#epi-rte-outcome-annotation) | retention | implemented | [EPI-OBJ-outcome](#epi-obj-outcome) | no content change | Admitted annotation | Save/load code | see [EPI-RTE-outcome-annotation](#epi-rte-outcome-annotation) | outcome.json | Permissive persistence | Retention does not add warrant. | Public consumers can filter/display annotation | Gallery/feed → recorded label → enforcing filter/advisory display → until overwrite | see [EPI-RTE-outcome-annotation](#epi-rte-outcome-annotation) | [EPI-CLM-verified-outcomes](#epi-clm-verified-outcomes) | none | No cross-export withdrawal cascade established. |
| [EPI-RTE-signal-derivation](#epi-rte-signal-derivation) | content transformation | implemented | [EPI-OBJ-signal](#epi-obj-signal) | truth-apt transformation: entailed derivation | Final stance fractions/health → signal/probability numbers | Deterministic plurality, rescaling, complement and label mapping | see [EPI-RTE-signal-derivation](#epi-rte-signal-derivation) | Direction/confidence/risk/YES-NO fields | Deterministic output | Derivation valid for adapter definitions only; real-event probability interpretation unwarranted without calibration. | Exposes automation-ready values | HTTP consumer → JSON → advisory machine-readable primitive → response/cache | see [EPI-RTE-signal-derivation](#epi-rte-signal-derivation) | [EPI-CLM-trading-probability](#epi-clm-trading-probability) | none | Concrete witness below is implementation deduction; embed-summary producer not fully verified. |
| [EPI-RTE-signal-derivation](#epi-rte-signal-derivation) | operational admission/selection/consumption | implemented | [EPI-OBJ-signal](#epi-obj-signal) | no content change | Public/readiness gate for derivatives | Public-summary loader; final belief fields; completed additionally for Polymarket | see [EPI-RTE-signal-derivation](#epi-rte-signal-derivation) | JSON or 404/error | Enforcing readiness, advisory downstream | Readiness is not factual acceptance. | Allows consumption by external automation; actual trading unobserved | External caller → signal.json/polymarket.json → advisory → 300-second cache | see [EPI-RTE-signal-derivation](#epi-rte-signal-derivation) | [EPI-CLM-trading-probability](#epi-clm-trading-probability) | none | Generic signal can be mid-run; no configured external bot captured. |
| [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population) | operational admission/selection/consumption | implemented | [RT-OBJ-agent-profiles](runtime.md#rt-obj-agent-profiles) | no content change | Generated population/config into run | see [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population) | see [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population) | Saved profiles/config or failed preparation | Permissive automatic admission | Operational persona assumptions, not validated population biography. | Enables model-driven simulation | Drivers → files/system personas → permissive/advisory → run | see [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population) | [EPI-CLM-grounded-personas](#epi-clm-grounded-personas) | none | Operation unobserved. |
| [RT-RTE-report-sections](runtime.md#rt-rte-report-sections) | content transformation | implemented | [EPI-OBJ-report-section](#epi-obj-report-section) | truth-apt transformation: indeterminate | Tool observations/outline → narrative assertions | Model interpretation of section-local evidence | see [RT-RTE-report-sections](runtime.md#rt-rte-report-sections) | Narrative candidate section | Permissive generation | Potential evidence-conditioned synthesis; entailment and non-entailment cannot be established without actual inputs/output. | Makes narrative available for completion gate | Report completion → model text → advisory/permissive → section | see [RT-RTE-report-sections](runtime.md#rt-rte-report-sections) | none | none | Fluency/tool use do not establish novel accepted knowledge or causal explanation. |
| [RT-RTE-interview-manual](runtime.md#rt-rte-interview-manual) | content transformation | implemented | [EPI-OBJ-interview-response](#epi-obj-interview-response) | truth-apt transformation: indeterminate | Agent persona/context/question → answer | Direct model response, not the action-tool loop | see [RT-RTE-interview-manual](runtime.md#rt-rte-interview-manual) | Participant answer or error | Permissive model output | Simulated-agent statement; world truth and fidelity to retained experience unestablished. | Returns/records answer for caller and possible conversation memory | Interviewer → response text → advisory → interview/later records | see [RT-RTE-interview-manual](runtime.md#rt-rte-interview-manual) | none | none | Could report context faithfully or add claims; no actual content to classify further. |
| [RT-RTE-report-sections](runtime.md#rt-rte-report-sections) | disposition/acceptance | implemented | [EPI-OBJ-report-section](#epi-obj-report-section) | no content change | Section text accepted for report use | Normal two-call criterion; bounded/forced-finish alternate | see [RT-RTE-report-sections](runtime.md#rt-rte-report-sections) | Final content/error placeholder | Enforcing normal count only; permissive force-finish | Sufficient tool count is not evidence-consuming factual acceptance. | Allows section completion and later report retention | ReportManager/readers → Markdown → advisory → saved report | see [RT-RTE-report-sections](runtime.md#rt-rte-report-sections) | none | none | Supplied route establishes bypass. Interpretations/causal stories are candidates, not accepted ampliative findings. |
| [EPI-RTE-report-cleanup](#epi-rte-report-cleanup) | content transformation | implemented | [EPI-OBJ-report-section](#epi-obj-report-section) | truth-apt transformation: non-ampliative reshaping | Markdown headings → presentation | Regex/title cleanup | see [EPI-RTE-report-cleanup](#epi-rte-report-cleanup) | Cleaned text | Enforcing formatting | No new warrant; deterministic presentation reshaping. | Alters report appearance | Report files/readers → Markdown → advisory → report lifetime | see [EPI-RTE-report-cleanup](#epi-rte-report-cleanup) | none | none | Witness: title Findings and input “# Findings\n\nRevenue rose.” yields “Revenue rose.” No truth check. |
| [EPI-RTE-report-cleanup](#epi-rte-report-cleanup) | lineage/freshness/recovery | implemented | [EPI-OBJ-report-section](#epi-obj-report-section) | no content change | Saved report availability | Explicit delete_report path | see [EPI-RTE-report-cleanup](#epi-rte-report-cleanup) | Folder/files removed | Enforcing local removal | Availability withdrawal, not evidence-based refutation. | Prevents manager reload of removed files | ReportManager → filesystem → enforcing → after deletion | see [EPI-RTE-report-cleanup](#epi-rte-report-cleanup) | none | none | Neo4j traces, exports and already delivered copies not shown deleted. |
| [RT-RTE-agent-mcp](runtime.md#rt-rte-agent-mcp) | operational admission/selection/consumption | implemented | [EPI-OBJ-tool-result](#epi-obj-tool-result) | no content change | External tool result enters later agent context | see [RT-RTE-agent-mcp](runtime.md#rt-rte-agent-mcp) | see [RT-RTE-agent-mcp](runtime.md#rt-rte-agent-mcp) | RPC result/error pending for next activation | Capability enforcement; advisory result | Successful RPC is not truth verification; external result warrant unknown. | May affect later action or remote side effects | Agent invocation → injected tool results → advisory → next activation | see [RT-RTE-agent-mcp](runtime.md#rt-rte-agent-mcp) | none | none | Deployed registry/remote tool semantics absent; cannot individuate truth-apt content. |
| [RT-RTE-director-context](runtime.md#rt-rte-director-context) | behavior/policy adaptation | implemented | [EPI-OBJ-director-event](#epi-obj-director-event) | non-truth-apt policy/content update: caller scenario intervention | New event assumption → requested reaction | see [RT-RTE-director-context](runtime.md#rt-rte-director-context) | see [RT-RTE-director-context](runtime.md#rt-rte-director-context) | Admitted event system text | Permissive/advisory | Fictional scenario authority, not empirical truth. | Requests changed posting/trading | Active agents → system-message event → advisory → until replacement | see [RT-RTE-director-context](runtime.md#rt-rte-director-context) | none | none | Truth-apt assertions may occur in events; no instance supplied, compliance unobserved. |

Concrete arithmetic witness (implementation deduction, not execution): for a completed summary with final percentages bullish=80, neutral=10, bearish=10 and health Excellent, signal selection picks Bullish; confidence is `(80 - 100/3)/(100 - 100/3)*100 = 70.0`, risk is low-risk. The Polymarket adapter returns yes_probability=0.8, no_probability=0.2 and confidence_tier=confident. These are consequences of the inspected rules, not evidence of an 80% real-event chance or measured low financial risk. See [EPI-RTE-signal-derivation](#epi-rte-signal-derivation). The truth-apt derivation domain is the adapter-defined numerical fields; the stronger probabilistic meaning remains unsupported.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-graph-memory](runtime.md#rt-clm-graph-memory) | see [RT-CLM-graph-memory](runtime.md#rt-clm-graph-memory) | see [RT-CLM-graph-memory](runtime.md#rt-clm-graph-memory) | see record | [EPI-RTE-graph-retention](#epi-rte-graph-retention), [EPI-RTE-graph-ranking](#epi-rte-graph-ranking) | None supplied | No completeness/benefit comparison | Optional activity-to-graph path is implemented; retention/retrieval are not proof of verified knowledge. | Activation and fidelity unobserved. |
| [EPI-CLM-grounded-personas](#epi-clm-grounded-personas) | see record | see record | see record | [EPI-RTE-web-research](#epi-rte-web-research), [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population) | None supplied | No demographic/reference test | Context-conditioned persona production and optional search synthesis are supported. | “Grounded” does not establish validated biography/population behavior; fallback need not browse. |
| [EPI-CLM-epistemic-kinds](#epi-clm-epistemic-kinds) | see record | see record | see record | [EPI-RTE-graph-retention](#epi-rte-graph-retention), [EPI-RTE-edge-adjudication](#epi-rte-edge-adjudication), [EPI-RTE-edge-invalidation](#epi-rte-edge-invalidation), [EPI-RTE-graph-ranking](#epi-rte-graph-ranking) | None supplied | Metadata filter, not truth assay | Requested belief edges can be category-filtered and invalidated edges omitted. | Default fact is not verified ground truth; batch kind is not per-proposition judgment; direct node hits bypass these filters. |
| [EPI-CLM-reasoning-traces](#epi-clm-reasoning-traces) | see record | see record | see record | [RT-RTE-report-sections](runtime.md#rt-rte-report-sections), [RT-RTE-storage-mcp](runtime.md#rt-rte-storage-mcp) | None supplied | No trace completeness or causal explanation test | Optional recorder/query wiring supports inspectable report steps. | “Every report” overstates flag-/failure-dependent recording; generated thought text is not causal access to private model reasoning. |
| [EPI-CLM-verified-outcomes](#epi-clm-verified-outcomes) | see record | see record | see record | [EPI-RTE-outcome-annotation](#epi-rte-outcome-annotation), [EPI-RTE-prediction-resolution](#epi-rte-prediction-resolution) | None supplied | References supplied by caller; no independent event verification | Admin annotation and binary agreement scoring exist. | Verified-only means valid annotation present, not independently substantiated forecast accuracy. |
| [EPI-CLM-trading-probability](#epi-clm-trading-probability) | see record | see record | see record | [EPI-RTE-signal-derivation](#epi-rte-signal-derivation), [EPI-RTE-quality-diagnostics](#epi-rte-quality-diagnostics) | None supplied | Arithmetic witness only; no calibration or trading comparison | Machine-readable stance/confidence/risk derivatives exist. | Event-probability and financial-risk meanings exceed the inspected evidence. |
| [EPI-CLM-scenario-caveat](#epi-clm-scenario-caveat) | see record | see record | see record | [RT-RTE-report-sections](runtime.md#rt-rte-report-sections) | None supplied | Prompt caveat is not output compliance | Declared report purpose is plausible dynamics under assumptions, not calibrated forecasting. | This limits the intended scope; it does not validate stronger trading/verified labels elsewhere. |

## Bounded conclusion

MiroShark has several independent authority paths, not one oracle or single epistemic status.

- **Acquisition and retained candidates:** document text, model-generated briefings, enrichment and simulated activity can feed graph assertions and personas. Episode/source metadata preserves some lineage. Original source warrant is unknown; model extraction, merge and summary fidelity are unestablished. `fact` is a category default, not a truth acceptance decision. See [EPI-RTE-ask-briefing](#epi-rte-ask-briefing), [EPI-RTE-web-research](#epi-rte-web-research), [EPI-RTE-graph-extraction](#epi-rte-graph-extraction) and [EPI-RTE-graph-retention](#epi-rte-graph-retention).
- **Checks with real but bounded force:** canonical-match thresholds/model decisions control deduplication for graph use; old/new incompatibility verdicts can withdraw old edges from current edge search. These decisions license identity selection and current-view exclusion, not truth of new relations. Query ranking licenses relevance only. Historical results, direct node descriptions, communities and already saved reports do not share a universal withdrawal horizon. See [EPI-RTE-entity-resolution](#epi-rte-entity-resolution), [EPI-RTE-edge-adjudication](#epi-rte-edge-adjudication), [EPI-RTE-edge-invalidation](#epi-rte-edge-invalidation) and [EPI-RTE-graph-ranking](#epi-rte-graph-ranking).
- **Reshaping and conjecture:** deterministic formatting is non-ampliative; adapter arithmetic is derivation under its explicit definitions and conditional inputs. Model-generated briefings, biographies, summaries, persona detail and narrative interpretations remain semantically indeterminate without actual input/output evidence: possible import, reshaping, entailed detail or non-entailed additions cannot be resolved from a prompt label. The report loop can request evidence and admit text, but tool-count/forced completion does not record evidence-consuming acceptance against a truth criterion. Retention and organization therefore do not establish lifecycle integration of accepted ampliative claims in these assessed paths. This is not a system-complete absence claim. See [EPI-RTE-report-cleanup](#epi-rte-report-cleanup), [EPI-RTE-round-compaction](#epi-rte-round-compaction), [EPI-RTE-community-generation](#epi-rte-community-generation), [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population) and [RT-RTE-report-sections](runtime.md#rt-rte-report-sections).
- **Direct adaptation:** belief/trust/confidence updates are wired from social signals into retained scalar state and later system messages. Their force is deterministic at the scalar update and model-interpreted at action selection. This is a genuine behavior-shaping route independent of truth-apt criticism, parameter training or demonstrated improvement; neither delivery nor persistence establishes activation/benefit. Topic stances are not sufficiently individuated propositions for a truth test. See [EPI-RTE-belief-revision](#epi-rte-belief-revision) and [RT-BAP-agent-context](runtime.md#rt-bap-agent-context).
- **Post-run appraisal and downstream reliance:** activity/diversity criteria produce health suggestions/badges; binary resolution compares a selected price to an administrator-supplied outcome; public outcome labels can admit a run into verified-only filtering without consuming URL evidence. Their criteria and intended scopes differ. Trading surfaces deterministically turn aggregate state into probability/risk-shaped values, whose numerical derivation does not license calibrated event probabilities or measured financial risk. API/filter force is implemented; actual public reliance, trading effects, outcome correctness, reference-event alignment and causal validity remain unobserved. See [EPI-RTE-quality-diagnostics](#epi-rte-quality-diagnostics), [EPI-RTE-prediction-resolution](#epi-rte-prediction-resolution), [EPI-RTE-outcome-annotation](#epi-rte-outcome-annotation) and [EPI-RTE-signal-derivation](#epi-rte-signal-derivation).

No conclusion here bundles learning, reflection, autonomy, self-improvement or theory building. Heuristic adaptation and retained context are independently supported architectural facts; improved capacity, exercised self-improvement and content-directed theory criticism are not established by those facts. Unassessed report/equilibrium/auxiliary and external-provider paths retain their local limits rather than being treated as absent mechanisms.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-report-section
Label: Report section assertions

Part of: [RT-RTE-report-sections](runtime.md#rt-rte-report-sections)

Identity/content: Narrative descriptions, explanations and implications about a simulation and its possible real-world relevance. Representational form and substrate: Natural-language section responses and saved Markdown, separate from symbolic tool-count control fields. SRC-1, `backend/app/services/report_agent.py` (implementation). Material output part of [RT-RTE-report-sections](runtime.md#rt-rte-report-sections); a route is the container, while this object is its produced text. Limit: Provider outputs absent; faithful synthesis versus additional conjecture cannot be classified. Source mechanics and load-bearing passages are in the route records below or the cited supplied container; those records do not change this object identity.

#### EPI-OBJ-interview-response
Label: Interview responses

Part of: [RT-RTE-interview-manual](runtime.md#rt-rte-interview-manual)

Identity/content: Answers attributed to simulated agents; any world assertions or self-reports have participant/scenario scope, not automatic real-person testimony. Representational form and substrate: Natural-language model responses recorded through platform interview channels. SRC-1, `backend/wonderwall/social_agent/agent.py` (implementation). Material output part of [RT-RTE-interview-manual](runtime.md#rt-rte-interview-manual); distinct from its direct-action effects. Limit: No actual question/response or restoration trace supplied; truth-apt instances not determinable. Source mechanics and load-bearing passages are in the route records below or the cited supplied container; those records do not change this object identity.

#### EPI-OBJ-tool-result
Label: External tool results

Part of: [RT-RTE-agent-mcp](runtime.md#rt-rte-agent-mcp)

Identity/content: Not determinable without actual tools/results: results may contain assertions, effect acknowledgments or errors. Representational form and substrate: Structured RPC objects and text injected into later model context. SRC-1, `backend/scripts/mcp_agent_bridge.py` (implementation). Material result part of [RT-RTE-agent-mcp](runtime.md#rt-rte-agent-mcp); not the registry or executable capability. Limit: Remote source warrant and result semantics uninspected. Source mechanics and load-bearing passages are in the route records below or the cited supplied container; those records do not change this object identity.

#### EPI-OBJ-director-event
Label: Director scenario text

Part of: [RT-RTE-director-context](runtime.md#rt-rte-director-context)

Identity/content: Caller-supplied event assumptions can contain truth-apt assertions, but are consumed as a scenario intervention rather than established world facts. Representational form and substrate: Natural-language event text in files and active-agent system messages. SRC-1, `backend/scripts/director_events.py` (implementation). Material text part of [RT-RTE-director-context](runtime.md#rt-rte-director-context); distinct from control count/length predicates. Limit: Actual event contents and compliance unobserved. Source mechanics and load-bearing passages are in the route records below or the cited supplied container; those records do not change this object identity.

#### EPI-OBJ-seed-document
Label: Seed briefing

Identity/content: Question-conditioned assertions about named actors and events; truth-apt in the stated scenario/world scope. Representational form and substrate: Natural-language Markdown and actor strings in returned JSON and process-local ask cache. SRC-1, `backend/app/api/simulation.py` (implementation). Distinct upstream input from the persona/configuration outputs of [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population). No supplied object counterpart. Limit: No captured briefing or factual reference. Source mechanics and load-bearing passages are in the route records below or the cited supplied container; those records do not change this object identity.

#### EPI-OBJ-graph-relations
Label: Extracted relation facts

Identity/content: Assertions connecting named entities, attributed to an input episode. Representational form and substrate: Natural-language fact text plus symbolic endpoints, kind, source and temporal properties on Neo4j RELATION edges. SRC-1, `backend/app/storage/neo4j_storage.py` (implementation). Upstream graph content, distinct from [RT-OBJ-agent-profiles](runtime.md#rt-obj-agent-profiles) and [RT-OBJ-simulation-config](runtime.md#rt-obj-simulation-config). Limit: Input truth and extraction fidelity are separate unknowns. Source mechanics and load-bearing passages are in the route records below or the cited supplied container; those records do not change this object identity.

#### EPI-OBJ-entity-summaries
Label: Entity descriptions

Identity/content: Descriptions and identity claims about graph entities. Representational form and substrate: Natural-language summaries/attributes plus symbolic canonical identity on Neo4j Entity nodes. SRC-1, `backend/app/storage/neo4j_storage.py` (implementation). Distinct from relation assertions and from downstream [RT-OBJ-agent-profiles](runtime.md#rt-obj-agent-profiles). Limit: Merged identity can combine descriptions from different inputs. Source mechanics and load-bearing passages are in the route records below or the cited supplied container; those records do not change this object identity.

#### EPI-OBJ-research-context
Label: Research enrichment

Identity/content: Entity biography/background assertions supplied to persona generation. Representational form and substrate: Natural-language synthesized research, process-local cache and persona-generation context. SRC-1, `backend/app/services/web_enrichment.py` (implementation). Upstream material for [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population), not its persona output; no supplied object counterpart. Limit: Search snippets, model prior knowledge and actual outputs uncaptured. Source mechanics and load-bearing passages are in the route records below or the cited supplied container; those records do not change this object identity.

#### EPI-OBJ-round-record
Label: Round summaries

Identity/content: Claims about simulated actions and dynamics, not real-world events. Representational form and substrate: Natural-language compacted_summary and ancient summary in RoundMemory objects; raw records remain a separate substrate. SRC-1, `backend/scripts/round_memory.py` (implementation). Material context part of the loop described by [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds); no supplied object declaration identifies it. Limit: Model summarization fidelity unobserved; fallback counts have a narrower domain. Source mechanics and load-bearing passages are in the route records below or the cited supplied container; those records do not change this object identity.

#### EPI-OBJ-belief-state
Label: Belief and trust state

Identity/content: A simulated attitude/control state; a topic position is not itself a proposition with an independently specified truth condition. Representational form and substrate: Symbolic topic-to-number dictionaries and thresholds, JSON snapshots, and natural-language prompt labels consumed by models. SRC-1, `backend/wonderwall/social_agent/belief_state.py` (implementation). Distinct operative state within [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds), not the control fields of [RT-OBJ-simulation-config](runtime.md#rt-obj-simulation-config). Limit: Real belief, calibrated confidence and truth of positions not established. Source mechanics and load-bearing passages are in the route records below or the cited supplied container; those records do not change this object identity.

#### EPI-OBJ-community-summary
Label: Community descriptions

Identity/content: Claims about what selected graph entities have in common. Representational form and substrate: Natural-language titles/summaries, dense summary embeddings and symbolic memberships on Neo4j Community nodes. SRC-1, `backend/app/storage/community_builder.py` (implementation). Construction output consumed by [RT-RTE-storage-mcp](runtime.md#rt-rte-storage-mcp); no supplied object counterpart. Limit: Prompt samples at most 15 members with 100-character descriptions. Source mechanics and load-bearing passages are in the route records below or the cited supplied container; those records do not change this object identity.

#### EPI-OBJ-quality
Label: Quality diagnostics

Identity/content: Participation, stance diversity, convergence and platform-interaction statistics over recorded simulation data. Representational form and substrate: Symbolic metrics and badge plus natural-language suggestions in quality.json and API JSON. SRC-1, `backend/app/api/simulation.py` (implementation). Distinct evaluator output not declared in the supplied runtime; closest loop [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds). Limit: Health is a rule-defined label, not predictive accuracy. Source mechanics and load-bearing passages are in the route records below or the cited supplied container; those records do not change this object identity.

#### EPI-OBJ-resolution
Label: Binary resolution

Identity/content: Whether selected final market consensus agrees with a supplied YES/NO outcome. Representational form and substrate: Symbolic consensus, score and caller outcome plus notes in resolution.json. SRC-1, `backend/app/api/simulation.py` (implementation). Distinct post-run evaluation output; no supplied counterpart after comparison with [RT-RTE-report-sections](runtime.md#rt-rte-report-sections). Limit: Outcome provenance and event/market alignment are caller obligations. Source mechanics and load-bearing passages are in the route records below or the cited supplied container; those records do not change this object identity.

#### EPI-OBJ-outcome
Label: Outcome annotation

Identity/content: An administrator asserts a public run was correct, incorrect or partial. Representational form and substrate: Symbolic label plus URL, summary and timestamp in outcome.json. SRC-1, `backend/app/api/simulation.py` (implementation). Distinct from binary resolution and report generation in [RT-RTE-report-sections](runtime.md#rt-rte-report-sections). Limit: URL is optional and is not fetched by admission. Source mechanics and load-bearing passages are in the route records below or the cited supplied container; those records do not change this object identity.

#### EPI-OBJ-signal
Label: Trading-signal payloads

Identity/content: Numerical restatements of simulated stance fractions; stronger event-probability interpretation needs additional warrant. Representational form and substrate: Symbolic direction, confidence, risk and probabilities in HTTP JSON; not model weights. SRC-1, `backend/app/services/signal_service.py` (implementation). Downstream derivative of belief/quality state, not [RT-OBJ-simulation-config](runtime.md#rt-obj-simulation-config) or its generation route. Limit: Probability calibration and actual bot consumption unobserved. Source mechanics and load-bearing passages are in the route records below or the cited supplied container; those records do not change this object identity.

### Routes

#### EPI-RTE-ask-briefing
Label: Question to seed briefing

No counterpart after comparison with [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population): this is its optional upstream seed producer, not preparation itself.

Caller question → smart-model JSON → _ask_clean_result → cache/API result. API code owns admission; the model proposes. In this open-request mode, shape/length and allowed-platform checks can reject an output; there is no reference-answer oracle or factual check in this handler. Starting the request is not per-assertion human approval. no_cache can request regeneration; it is not semantic rollback. Evidence layer: implementation, SRC-1, `backend/app/api/simulation.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Cleaned briefing/model/cache flag, or rate/shape/provider error.
- Later read-back: Cache serves repeated questions; API contract offers the briefing to the graph-ontology workflow, rather than automatically ingesting it.
- Delegated visibility: Question, date context and fixed prompt go to the model; source documents do not accompany this call.
- Selection predicate: Question length 8–400; requirement at least 40 characters and document at least 400.
- Invalidation or expiry: 32-entry process-local cache; no_cache bypasses read.
- Activation or effect: Admitted generated briefing can become graph input through the client workflow; no execution supplied.
- Evidence limits: Named real entities requested by prompt are not verified by the cleaner.

> if len(req) < 40 or len(doc) < 400:
>     return None
> --- `backend/app/api/simulation.py`

#### EPI-RTE-web-research
Label: Entity research enrichment

Part of: [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population)

Upstream content-producing part of [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population); not a replacement for its output admission.

Entity and scenario → optional live search snippets → LLM synthesis → research-context text. WebEnricher owns assembly; the model supplies prose. Search results select a grounded prompt, otherwise a configured model is asked without snippets. Nonempty responses of at least 30 characters are admitted for persona context. No independent factual oracle is checked; failure returns empty context. This is enrichment for an open scenario, not evaluation against expected biographies. Evidence layer: implementation, SRC-1, `backend/app/services/web_enrichment.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Formatted research section or empty string.
- Later read-back: In-process cache and persona context feed subsequent profile generation; see [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population).
- Delegated visibility: Scenario copy is capped; existing context is truncated to 500 characters; snippets are supplied only when search returns them.
- Selection predicate: Public-figure/thin-context enrichment policy; actual search results unknown.
- Invalidation or expiry: Cached research reused for the same entity; no factual expiry or claim-level correction shown here.
- Activation or effect: Context is available to persona generation, not enforced as truth.
- Evidence limits: Provider browsing, snippets and biographies uncaptured; source warrant unknown after synthesis.

> if not response or len(response.strip()) < 30:
>     return ""
> --- `backend/app/services/web_enrichment.py`

#### EPI-RTE-graph-extraction
Label: NER extraction and cleaning

Distinct upstream transform from [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population); supplied report does not declare graph extraction as its own route.

Input text/ontology → low-temperature model JSON → _validate_and_clean → entity/relation dictionaries. NERExtractor owns retries and deterministic cleaning. The model proposes content; code rejects malformed/fragments, duplicate names, self-relations and some ontology-type endpoints, but keeps unknown types and can create missing endpoint entities. This is ingestion, with no source-truth oracle. Failure yields empty lists; re-ingestion is possible, not an atomic semantic rollback. Evidence layer: implementation, SRC-1, `backend/app/storage/ner_extractor.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Cleaned extraction or empty lists after retries.
- Later read-back: add_text retains returned descriptions/facts and uses them in graph search/setup.
- Delegated visibility: Model sees text plus ontology; cleaner sees its parsed output, not a separate evidence corpus.
- Selection predicate: Nonblank input; structural/name tests; relation endpoints may be synthesized from relation fields.
- Invalidation or expiry: New extraction on each call; downstream graph entries have separate invalidation.
- Activation or effect: Changes which claims and identities can enter graph writes.
- Evidence limits: Intended extraction does not prove semantic preservation or correct hallucination rejection.

> "fact": fact or f"{source} {rtype} {target}",
> --- `backend/app/storage/ner_extractor.py`

#### EPI-RTE-entity-resolution
Label: Canonical entity matching

No supplied counterpart; this is upstream identity admission, unlike persona admission in [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population).

Extracted entity/embedding → fuzzy/vector candidate scores → optional LLM same-entity verdict → canonical name map. EntityResolver proposes matches computationally and admits high scores (0.95) automatically; scores from 0.70 can go to the configured model. No per-match human veto or external identity oracle is required. Empty map/failure preserves independent creation. Intended use is deduplication within this graph, not validating relation truth. Name-map decisions drive MERGE in add_text; no split/undo is established here. Evidence layer: implementation, SRC-1, `backend/app/storage/entity_resolver.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Entity-index to canonical-name map.
- Later read-back: add_text consumes it immediately; resulting merged identity is later graph state.
- Delegated visibility: At most three candidates per entity; name corpus bounded to 2000; optional model receives candidate descriptions.
- Selection predicate: Enabled flag, nonempty corpus and thresholds; LLM flag further gates ambiguous cases.
- Invalidation or expiry: Map is per batch; merged nodes persist until separate mutation/deletion.
- Activation or effect: Canonical identity selection changes relation endpoints and merged attributes.
- Evidence limits: Similarity and model judgment are fallible identity evidence; not demonstrated identity accuracy.

> if top["score"] >= self.AUTO_MERGE_THRESHOLD:
>     resolutions[idx] = top["name_lower"]
> --- `backend/app/storage/entity_resolver.py`

#### EPI-RTE-graph-retention
Label: Graph episode and relation writes

Distinct graph retention mechanism upstream of [RT-RTE-prepare-population](runtime.md#rt-rte-prepare-population) and used by optional graph-memory design [RT-CLM-graph-memory](runtime.md#rt-clm-graph-memory).

Text → Episode + Entity MERGE + relation CREATE. Neo4jStorage owns writes and consumes extraction/resolution/adjudication. kind is caller metadata (default fact), checked only against three allowed values; it is not a source-truth decision. Attributes and embeddings can update on match while a nonempty old summary is kept. Optional activity updater sends simulated prose as belief for entirely expressive batches and observation otherwise, with source_type agent. Metadata admission is computational; callers may initiate ingestion but do not approve each extracted proposition. Writes and invalidations occur in separate operations; retry is not a proven atomic/replay-safe transaction. Evidence layer: implementation, SRC-1, `backend/app/storage/neo4j_storage.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Episode UUID after writes.
- Later read-back: Graph consumers search facts, entity descriptions and temporal metadata; preparation and MCP/report tools can read retained state.
- Delegated visibility: Episode stores text; edges store episode_ids, source_type/source_id, kind and timestamps. Activity source IDs identify platform/round or mixed batch, not a per-claim external citation.
- Selection predicate: Valid kind; extracted endpoints found in UUID map.
- Invalidation or expiry: Edges start invalid_at null; withdrawal is separate; graph deletion is a separate destructive operation.
- Activation or effect: Persists unverified candidates for later retrieval; default fact grants a category, not demonstrated truth.
- Evidence limits: Original-document truth unknown; episode linkage preserves lineage but extraction/merge can degrade fidelity.

> kind: str = "fact",
> source_type: str = "document",
> --- `backend/app/storage/neo4j_storage.py`

#### EPI-RTE-edge-adjudication
Label: Old/new fact adjudication

No supplied counterpart after comparison with [RT-RTE-storage-mcp](runtime.md#rt-rte-storage-mcp): producer-side adjudication, not read dispatch.

New relation batch → existing uninvalidated same-endpoint edges → LLM pair verdict → UUID list. ContradictionDetector owns candidate selection; model judges whether a NEW fact supersedes OLD. This is a compatibility/later-update test on texts, not independent verification of the new assertion. It examines at most five existing edges per pair and 30 pairs per call. Exact fact replay is skipped. Model/lookup failure defaults to no withdrawal. No human veto or external truth oracle is required; mode is ingestion-time maintenance. Evidence layer: implementation, SRC-1, `backend/app/storage/contradiction_detector.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Old-edge UUIDs selected for invalidation.
- Later read-back: add_text immediately consumes verdicts; invalidation changes later retrieval.
- Delegated visibility: Model sees OLD/NEW strings, with quotes normalized, not original episodes or evidence of chronological order.
- Selection predicate: Feature enabled, same endpoint pair, different fact strings, bounded batch.
- Invalidation or expiry: Verdict transient; graph withdrawal persists.
- Activation or effect: May withdraw an older candidate from current search.
- Evidence limits: The prompt assumes the new assertion is later; detector does not compare evidence quality, source_type or kind.

> Be conservative. Only mark as "contradicts" when you're confident the new
> fact makes the old one false.
> --- `backend/app/storage/contradiction_detector.py`

#### EPI-RTE-edge-invalidation
Label: Withdrawal from current graph view

Producer-side disposition distinct from read adapter [RT-RTE-storage-mcp](runtime.md#rt-rte-storage-mcp).

Adjudicated edge UUID → invalidate_edge → timestamp properties → current/historical search filters. Storage owns the disposition. Caller can invoke this operation; ingestion automatically invokes it on verdict UUIDs. It sets invalid_at and expired_at but does not delete old text or approve the new fact. Re-ingestion errors are caught around contradiction processing; this is not an atomic replacement. No inspected automatic semantic reinstatement route is claimed. Evidence layer: implementation, SRC-1, `backend/app/storage/neo4j_storage.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Boolean updated flag.
- Later read-back: Current edge search excludes withdrawn edges; historical/include-invalidated requests can recover them.
- Delegated visibility: Consumer receives surviving ranked edges, or historical edges if explicitly requested.
- Selection predicate: UUID matches a RELATION with invalid_at null.
- Invalidation or expiry: Timestamped withdrawal persists; historical data remains.
- Activation or effect: Enforcing current-edge exclusion, not universal removal from all descriptions, communities or reports.
- Evidence limits: Direct node search and existing derived summaries have different invalidation paths.

> WHERE r.invalid_at IS NULL
> SET r.invalid_at = $ts, r.expired_at = $ts
> --- `backend/app/storage/neo4j_storage.py`

#### EPI-RTE-graph-ranking
Label: Graph search selection

Internal selection part of [RT-RTE-storage-mcp](runtime.md#rt-rte-storage-mcp), also used by graph-consuming generation; not a second MCP entry point.

Query → embedding/keyword/optional traversal candidate pools → score fusion → optional reranking → limited results. SearchService owns ranking; configured encoders/cross-encoder supply similarity scores. This evaluates query relevance within the candidate pool, not factual accuracy. Edge selection applies temporal/kind filters; direct node vector/BM25 hits do not. Caller selects scope/options, code/model ranking selects candidates; there is no answer oracle or per-hit approval. Failed reranking falls back to fused ranking. Evidence layer: implementation, SRC-1, `backend/app/storage/search_service.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ranked selected dictionaries.
- Later read-back: Retained graph is reread on requests; external client caching is uninspected.
- Delegated visibility: Result limit and candidate pools omit other facts; consumers do not automatically receive all supporting episodes.
- Selection predicate: Query, scope, temporal/kind flags, strategy flags and score/reranker order.
- Invalidation or expiry: Transient rankings; changing graph/models/flags can change future hits.
- Activation or effect: Advisory/ranking authority for persona/report/MCP evidence consumption.
- Evidence limits: Relevance scores do not establish source truth; node filtering is not equivalent to edge filtering.

> Node vector / BM25 hits ignore those filters since
> entities themselves aren't tagged with kind.
> --- `backend/app/storage/search_service.py`

#### EPI-RTE-round-compaction
Label: Round-history compaction

Part of: [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds)

Material compaction part of [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds).

Old round action text → background LLM summary or deterministic count fallback → compacted/ancient context → later agents. RoundMemory owns timing and replacement. A model proposes prose; code immediately retains stripped output without comparison against raw action text. Failures fall back to counts; older summaries can be merged again and individual records removed. This is context management, not evidence-consuming acceptance of claims. Raw databases/logs are separate evidence, not automatically followed references. Evidence layer: implementation, SRC-1, `backend/scripts/round_memory.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Scheduled compaction; later summary field or fallback.
- Later read-back: build_context supplies compacted history and recent detail in later invocations.
- Delegated visibility: Two-to-three sentence instruction focuses on salient dynamics; older batching further compresses.
- Selection predicate: Round N-2 if available and uncompacted; ancient batching when history is long.
- Invalidation or expiry: Summary replaces model-visible detail; ancient batches replace individual memory records.
- Activation or effect: Potentially behavior-shaping context via [RT-BAP-agent-context](runtime.md#rt-bap-agent-context); actual compliance unknown.
- Evidence limits: Semantic preservation unobserved; fallback counts describe retained non-skipped actions, not every event.

> summary = self.llm.chat(messages=messages, temperature=0.3)
> rec.compacted_summary = summary.strip()
> --- `backend/scripts/round_memory.py`

#### EPI-RTE-belief-revision
Label: Heuristic belief adaptation

Part of: [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds)

Material update part of [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds), distinct from its scheduling function.

Seen-post text/trust/likes/novelty → keyword stance and topic matching → position/confidence update → prompt labels. BeliefState owns deterministic rules, BeliefTracker supplies post-round inputs and injects text. The code changes stance directly; it neither formulates a truth test nor rejects a proposition for falsity. Engagement can raise confidence on every topic. An open simulation supplies actions, not an external reference answer; no per-update human approval. Tracker saves state/trajectory and reloads matching agents on resume. This is trace-fed policy/context adaptation, not model-weight training or demonstrated learning benefit. Evidence layer: implementation, SRC-1, `backend/wonderwall/social_agent/belief_state.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Position deltas and changed confidence/trust.
- Later read-back: Tracker serializes belief_states_<platform>.json and trajectories, restores state, and injects new labels into active-agent system messages.
- Delegated visibility: Selected analyzed actions/posts and scalar feedback, not a complete proof or truth criterion.
- Selection predicate: Topic overlap, sentiment substrings, exposure novelty, author trust and engagement.
- Invalidation or expiry: Clamping bounds; subsequent updates replace scalars; saved state can resume.
- Activation or effect: Model-interpreted stance/trust instructions can shape later posting/trading.
- Evidence limits: Inputs analyzed by RoundAnalyzer were not exhaustively audited; heuristic attitude changes do not validate argument content.

> boost = min(0.15, (likes_received - dislikes_received) * 0.03)
> self.confidence[topic] = min(1.0, current_conf + boost)
> --- `backend/wonderwall/social_agent/belief_state.py`

#### EPI-RTE-community-generation
Label: Community grouping and labels

Part of: [RT-RTE-storage-mcp](runtime.md#rt-rte-storage-mcp)

Material construction part of [RT-RTE-storage-mcp](runtime.md#rt-rte-storage-mcp), whose record explicitly leaves deeper semantics uninspected.

Valid-edge graph → clustering and size cap → sampled entity descriptions → LLM title/summary or fallback → replacement Community nodes. CommunityBuilder owns grouping and write admission; a model supplies labels. Size filtering is not a semantic check. Summaries use at most 15 member descriptions truncated to 100 characters, not all relation evidence. No independent acceptance gate or answer oracle verifies a label. Missing communities can trigger this automatically through MCP browsing. Deletion and writes use separate sessions despite the comment claiming one transaction; failure after deletion can leave old communities lost. Evidence layer: implementation, SRC-1, `backend/app/storage/community_builder.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Cluster/count statistics or failure.
- Later read-back: Stored summaries/members are browsed or searched by MCP/report consumers.
- Delegated visibility: Sampled metadata to the summarizer; clients get limited summaries/detail.
- Selection predicate: Minimum cluster size, maximum count and graph grouping.
- Invalidation or expiry: Full rebuild deletes existing Community nodes; small-graph early return can leave earlier communities untouched.
- Activation or effect: Changes navigation and model-visible framing, not proven accepted knowledge integration.
- Evidence limits: Cluster quality, label accuracy, freshness and atomic replacement unobserved.

> self._delete_existing(graph_id)
> self._write(graph_id, kept, labels, embeddings)
> --- `backend/app/storage/community_builder.py`

#### EPI-RTE-contradiction-flags
Label: Report contradiction hints

Part of: [RT-RTE-report-sections](runtime.md#rt-rte-report-sections)

Evidence tool part of [RT-RTE-report-sections](runtime.md#rt-rte-report-sections), distinct from composition and from edge-adjudication.

Entity pairs with at least two directed relation facts → substring sentiment counts → opposing_sentiments flags → report tool observation. Neo4jStorage owns this deterministic scan, distinct from ingestion-time LLM contradiction adjudication. It reads edges without a current-validity filter. The evaluator target is opposing lexical signals, not logical inconsistency in context. ReportAgent can consume these flags through detect_contradictions; no automatic withdrawal follows this scan. Evidence layer: implementation, SRC-1, `backend/app/storage/neo4j_storage.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: List of flagged pairs and their facts.
- Later read-back: A later report invocation can request flags from retained edges; flags themselves are not persisted by this method.
- Delegated visibility: Bounded top pairs, fact strings and sentiment labels.
- Selection predicate: Multiple edges, positive and negative classified facts in same directed pair.
- Invalidation or expiry: Transient result; no mutation or withdrawal.
- Activation or effect: Advisory report evidence only.
- Evidence limits: Negation, aspect and timing are not logically modeled by substring counts.

> if has_positive and has_negative:
>     contradictions.append({
> --- `backend/app/storage/neo4j_storage.py`

#### EPI-RTE-quality-diagnostics
Label: Quality metrics and badge

New evaluator omitted from supplied runtime; distinct from [RT-RTE-report-sections](runtime.md#rt-rte-report-sections) and the simulation loop.

Action logs/trajectory → participation, entropy, convergence, cross-platform ratios → rule badge/suggestions → quality.json/API. API code owns evaluation and immediate caching. Excellent requires participation >=0.8, entropy >=0.5 if present, convergence >=4 if present, and cross-platform rate >=0.2. Low follows low participation or entropy. These criteria define simulation activity/diversity, not agreement with real outcomes. No human adjudication or expected-answer oracle. Suggestions advise future configurations; this handler does not automatically apply them. Evidence layer: implementation, SRC-1, `backend/app/api/simulation.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Diagnostics, cached result, or insufficient-data result.
- Later read-back: quality.json is reused without recomputing when present; gallery filters and signal risk mapping consume health.
- Delegated visibility: Only recorded actions and trajectory statistics, not external population evidence.
- Selection predicate: Simulation directory and any actions or trajectory; missing denominators have fallbacks.
- Invalidation or expiry: Cache-first file path; no freshness/semantic invalidation in this handler.
- Activation or effect: Advisory badge/suggestions and enforcing gallery filter selection; risk label in derived signals.
- Evidence limits: A completed run is not required by the inspected GET; stale/mid-run diagnostics are possible.

> if os.path.exists(quality_path):
>     with open(quality_path, 'r', encoding='utf-8') as f:
>         return jsonify({"success": True, "data": json.load(f)})
> --- `backend/app/api/simulation.py`

#### EPI-RTE-prediction-resolution
Label: Binary outcome scoring

New post-run evaluator, not an oracle in [RT-RTE-synchronized-rounds](runtime.md#rt-rte-synchronized-rounds) or [RT-RTE-report-sections](runtime.md#rt-rte-report-sections).

Admin-supplied YES/NO → latest price_history market (or reserve fallback only if that table is absent) → consensus comparison → resolution.json. Endpoint owns scoring; caller supplies the reference outcome. Score is 1/0 for agreement/disagreement, 0.5 when within 0.05 of 0.5, null without usable data. Invalid outcomes or unknown simulation are rejected; no independent oracle acquisition verifies the outcome/event mapping. New submission overwrites the file. This is post-hoc open-run evaluation, not a controlled causal experiment. Evidence layer: implementation, SRC-1, `backend/app/api/simulation.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Resolution object or validation/error response.
- Later read-back: Saved resolution is available to summaries and share-card/transcript consumers.
- Delegated visibility: Scorer sees one selected market price plus caller outcome, not all markets or source evidence.
- Selection predicate: Admin authentication, YES/NO and existing simulation; no completion check in this handler.
- Invalidation or expiry: New POST overwrites resolution.json; no semantic audit history established.
- Activation or effect: Records agreement with supplied outcome; display/reporting authority, not automatic simulator revision.
- Evidence limits: Outcome success does not identify mechanism, calibration, component effect or safe transfer.

> predicted_consensus = "YES"
> accuracy_score = 1.0 if actual_outcome == "YES" else 0.0
> --- `backend/app/api/simulation.py`

#### EPI-RTE-outcome-annotation
Label: Public outcome annotation

No supplied counterpart; independent of binary prediction-resolution and report composition [RT-RTE-report-sections](runtime.md#rt-rte-report-sections).

Authenticated admin label/optional URL/summary → validation → outcome.json → gallery/feed annotation. Caller proposes and judges correctness; code checks authentication, public simulation, allowed labels, URL shape and length. Authenticated identity does not establish human authorship or evidence review. URL content is not fetched by this admission handler; no independent reference oracle is consumed. Result may be replaced with another POST. It is an attributed appraisal, not an implemented independent verification procedure. Evidence layer: implementation, SRC-1, `backend/app/api/simulation.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Saved annotation or validation/authentication error.
- Later read-back: GET reloads outcome.json; public summary includes it; gallery verified/outcome filters and feed categories consume the label.
- Delegated visibility: Optional URL/short summary only; the system does not require a cited event record.
- Selection predicate: Public simulation; correct/incorrect/partial label; http(s) URL if supplied; length bounds.
- Invalidation or expiry: File overwritten by a later valid submission; no withdrawal cascade into already copied exports shown.
- Activation or effect: Permits inclusion in verified-only gallery and claimed outcome filtering.
- Evidence limits: A verified label establishes annotation presence, not verified forecasting validity.

> record = {
>     "simulation_id": simulation_id,
>     "label": label,
>     "outcome_url": outcome_url,
> --- `backend/app/api/simulation.py`

#### EPI-RTE-signal-derivation
Label: Stance fractions to trading surfaces

New downstream consumption path, not the mutable model clients [RT-CMP-model-clients](runtime.md#rt-cmp-model-clients) or configuration in [RT-OBJ-simulation-config](runtime.md#rt-obj-simulation-config).

Embed-summary final stance percentages/quality → deterministic leader/confidence/risk → signal JSON; Polymarket adapter maps direction to YES/NO fractions and title. Code owns transformation and readiness; no model, human veto or outcome oracle is used. Public-summary loader gates access; Polymarket additionally requires completed status, generic signal does not. Missing/bad input yields None/404. No calibration check connects stance fractions to real-event probability. External automation is a declared consumer, not an observed trade. Evidence layer: implementation, SRC-1, `backend/app/services/signal_service.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Derived payload or None translated to 404.
- Later read-back: Later HTTP requests recompute from retained summary; responses cache for 300 seconds.
- Delegated visibility: Consumers get aggregate stance percentages and labels, not individual arguments or full simulation evidence.
- Selection predicate: Valid numeric final belief fields; completed status additionally for Polymarket adapter.
- Invalidation or expiry: Request-generated timestamps/cache; future summaries can change signal.
- Activation or effect: Machine-readable advisory trading primitive; completed/public gates enforce readiness, not truth.
- Evidence limits: Actual bots, effects and financial risk/calibration are outside observed evidence.

> leader_key = _pick_leader(bullish, neutral, bearish)
> --- `backend/app/services/signal_service.py`

#### EPI-RTE-report-cleanup
Label: Section formatting and report removal

Part of: [RT-RTE-report-sections](runtime.md#rt-rte-report-sections)

Formatting/removal parts adjacent to [RT-RTE-report-sections](runtime.md#rt-rte-report-sections), not a duplicate composition loop.

Section Markdown → heading cleanup → saved report; explicit deletion → remove report folder/files. ReportManager owns transformations and removal. Cleanup removes duplicated initial titles and converts headings to bold; it does not check statement truth or evidence sufficiency. API delete invokes filesystem removal, not epistemic retraction. This does not establish deletion of the separately stored Neo4j reasoning graph or already exported copies. Evidence layer: implementation, SRC-1, `backend/app/services/report_agent.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Cleaned section text or deletion boolean.
- Later read-back: Saved report files are reloaded by report consumers; deleted files stop being available through that manager.
- Delegated visibility: Cleanup sees section text/title, not evidence or claims.
- Selection predicate: Heading pattern/title equality; explicit report-ID deletion.
- Invalidation or expiry: Folder deletion is destructive; no semantic rollback or all-store retraction shown.
- Activation or effect: Changes presentation/availability, not claim warrant.
- Evidence limits: Only materially relevant as a counterexample to treating cleanup/deletion as evaluation/rejection.

> cleaned_lines.append(f"**{title_text}**")
> --- `backend/app/services/report_agent.py`

Additional load-bearing implementation passages, all SRC-1:

Graph retention and lineage:

> episode_ids: [r.episode_id],
> created_at: $now,
> valid_at: $valid_at,
> invalid_at: null,
> expired_at: null,
> kind: $kind,
> source_type: $source_type,
> source_id: $source_id
> --- `backend/app/storage/neo4j_storage.py`

Activity-category assignment is batch-level; CREATE_COMMENT is expressive in implementation despite the shorter docstring list:

> expressive_actions = {"CREATE_POST", "QUOTE_POST", "CREATE_COMMENT"}
> edge_kind = (
>     "belief"
>     if all(a.action_type in expressive_actions for a in activities)
>     else "observation"
> )
> --- `backend/app/services/graph_memory_updater.py`

Old-edge checking does not compare kind/source or the new assertion's evidence:

> verdicts = self._llm_adjudicate(pairs)
> to_invalidate = [
>     existing["uuid"]
>     for (_, existing), verdict in zip(pairs, verdicts)
>     if verdict == "contradicts"
> ]
> --- `backend/app/storage/contradiction_detector.py`

Direct model-visible belief supply and persistence:

> if combined.strip():
>     inject_belief_context(agent, combined)
> --- `backend/scripts/belief_integration.py`

> self.save_belief_states()
> --- `backend/scripts/belief_integration.py`

Substring stance evaluation explains the concrete negation/substring witness in the ledger:

> pos_count = sum(1 for w in positive_signals if w in content_lower)
> neg_count = sum(1 for w in negative_signals if w in content_lower)
>
> total = pos_count + neg_count
> if total > 0:
>     return (pos_count - neg_count) / total
> --- `backend/wonderwall/social_agent/belief_state.py`

Gallery inclusion consumes annotation presence rather than URL evidence:

> if verified_only and _outcome_label(card) is None:
>     continue
> --- `backend/app/services/gallery_filters.py`

Quality-to-risk mapping is not a financial-risk measurement:

> _RISK_TIER_BY_HEALTH: dict[str, _RiskTier] = {
>     "excellent": "low-risk",
>     "good": "medium-risk",
>     "fair": "high-risk",
>     "poor": "high-risk",
> }
> --- `backend/app/services/signal_service.py`

> distance = max(0.0, leading_pct - _EVEN_SPLIT_PCT)
> confidence = distance / _CONFIDENCE_DENOMINATOR * 100.0
> --- `backend/app/services/signal_service.py`

> if direction == "Bullish":
>     raw = bullish_pct / 100.0
> elif direction == "Bearish":
>     raw = 1.0 - bearish_pct / 100.0
> else:
>     raw = 0.5
> --- `backend/app/services/polymarket_service.py`

> if not isinstance(status, str) or status.lower() != "completed":
>     return None
> --- `backend/app/services/polymarket_service.py`

> "confidence_tier": _confidence_tier(signal["confidence_pct"]),
> --- `backend/app/services/polymarket_service.py`

> if confidence_pct >= 75.0:
>     return "high-conviction"
> if confidence_pct >= 50.0:
>     return "confident"
> --- `backend/app/services/polymarket_service.py`

Report deletion removes its filesystem directory, not all derivative evidence:

> if os.path.exists(folder_path) and os.path.isdir(folder_path):
>     shutil.rmtree(folder_path)
> --- `backend/app/services/report_agent.py`

### Claims

#### EPI-CLM-grounded-personas
Label: Grounded agents

Public description claims grounded agents; architecture describes real-world enrichment with web-search models. SRC-1, `.github/README.md` and `docs/ARCHITECTURE.md` (doctrine/design). Distinct from the graph-memory claim [RT-CLM-graph-memory](runtime.md#rt-clm-graph-memory): this concerns persona grounding, not retained activity.

> When generating personas for public figures (politicians, CEOs, founders) or when graph context is thin (<150 chars), the system makes an LLM research call to enrich the profile with real-world data. Set `WEB_SEARCH_MODEL=perplexity/sonar-pro` in `.env` for grounded web search via OpenRouter.
> --- `docs/ARCHITECTURE.md`

#### EPI-CLM-epistemic-kinds
Label: Beliefs versus ground truth

Architecture calls belief-kind filtering separation from ground-truth facts. SRC-1, `docs/ARCHITECTURE.md` (doctrine/design). No supplied counterpart: [RT-CLM-graph-memory](runtime.md#rt-clm-graph-memory) concerns retention, not truth warrant of categories.

> - Epistemic filtering (`kinds=["belief"]` returns only agent opinions, not ground-truth facts)
> --- `docs/ARCHITECTURE.md`

#### EPI-CLM-reasoning-traces
Label: Every-report reasoning retention

Architecture claims every report persists a traversable ReACT trace. SRC-1, `docs/ARCHITECTURE.md` (doctrine/design). This is distinct from report-loop identity [RT-RTE-report-sections](runtime.md#rt-rte-report-sections); it is the stronger scope claim about persistence.

> Every report generation persists a full ReACT trace as a traversable subgraph:
> --- `docs/ARCHITECTURE.md`

Implementation counterexample (SRC-1, `backend/app/services/report_agent.py`): recording initialization is feature-/storage-dependent and failure-tolerant, so universal retention is not established.

> if Config.REASONING_TRACE_ENABLED:
>     try:
>         storage = getattr(self.graph_tools, "storage", None)
>         if storage and hasattr(storage, "create_reasoning_recorder"):
> --- `backend/app/services/report_agent.py`

#### EPI-CLM-verified-outcomes
Label: Verified-prediction annotation

Endpoint describes an open-ended verified-prediction annotation layer and public filtering. SRC-1, `backend/app/api/simulation.py` (doctrine/design). No supplied claim counterpart after comparison with [RT-CLM-graph-memory](runtime.md#rt-clm-graph-memory); this is public post-run appraisal, not graph memory.

> A lightweight successor to ``/resolve``: that one writes a binary
> YES/NO Polymarket-aligned resolution, this one accepts an open-ended
> "did this run predict a real event?" annotation. The two are
> complementary — a simulation can have both — and outcome.json is the
> record the public gallery and ``/verified`` filter read from.
> --- `backend/app/api/simulation.py`

#### EPI-CLM-trading-probability
Label: Trading probability and risk meaning

Signal and Polymarket adapter designs describe directly consumable trading values and interpret YES as proposition truth. SRC-1, `backend/app/services/signal_service.py`, `backend/app/services/polymarket_service.py` (doctrine/design). No supplied claim counterpart; generated probability/risk semantics are distinct from model configuration [RT-CMP-model-clients](runtime.md#rt-cmp-model-clients).

> pipeline can consume directly — ``direction`` + ``confidence_pct`` +
> ``risk_tier`` + the three component percentages.
> --- `backend/app/services/signal_service.py`

> * **Direction-aware YES probability.** Polymarket's YES side
>   represents *"the proposition is true"*. We mirror that semantically:
> --- `backend/app/services/polymarket_service.py`

#### EPI-CLM-scenario-caveat
Label: Plausible dynamics not forecasts

Report guidance explicitly restricts intended warrant to plausible dynamics under assumptions. SRC-1, `backend/app/services/report_agent.py` (doctrine/design). This qualifies report purpose without replacing the distinct downstream trading claim or [RT-CLM-graph-memory](runtime.md#rt-clm-graph-memory).

> This simulation is powered by LLM-driven agents whose behavior reflects the language model's understanding of human personas, NOT empirically calibrated behavioral models. The value is in revealing plausible dynamics, pressure points, and non-obvious interactions — not in forecasting specific outcomes. Treat findings as "under these assumptions, this is what could happen" rather than "this is what will happen."
> --- `backend/app/services/report_agent.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; route-specific consumers, channels, forces and horizons are in the ledger and route declarations. The supplied [RT-BAP-agent-context](runtime.md#rt-bap-agent-context) remains the context-to-action path, not an observed compliance result.
