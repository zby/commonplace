---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Zikkaron epistemic routes: memory admission, heuristic conjectures, reliance changes, freshness checks and benchmark judgments."
run-id: AAS-2026-10-15-zikkaron-0102ec63c6e5-01
reviewed-boundary: dda34a5d903d04ecb5517af214d437873c833302
---

# Zikkaron epistemic report

## Source-and-claim boundary

This report asks which retained or delivered propositions Zikkaron checks and licenses for later reliance, rather than equating persistence with accepted knowledge. Scope, exclusions and source identity are see [boundary](boundary.md#boundary-and-evidence); evidence identities are see [Source register](boundary.md#source-register). All new source reads use SRC-1 at the frozen commit, with implementation evidence except explicitly labelled claims. Nothing was executed. There is no supplied observed-run or causal-experiment evidence.

The ordinary host-authored memory, seed and replay routes acquire content; its external warrant is unknown. Directly inspected counterpaths include semantic promotion that actually vetoes inconsistent clusters, recall that rewrites future memories from queries, and inferred reranking passages that add unsupported preferences. These prevent both a blanket “no checks” conclusion and a blanket “validated memory” conclusion. The runtime is a baseline, not the inspection boundary.

| Entry point or operation | Source path under SRC-1 | Coverage and record | Unassessed part / conclusion prevented |
|---|---|---|---|
| CLI dispatch: service, drain, restore, capture, context, stats, seed | `zikkaron/__main__.py` | Direct dispatch read; supplied [RT-RTE-replay-context](runtime.md#rt-rte-replay-context), [RT-RTE-seed-admission](runtime.md#rt-rte-seed-admission), [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation) | Stats formatting is not a truth-acceptance gate. |
| MCP remember, recall, project context, anchor, checkpoint, restore; HTTP compact/capture | `zikkaron/server.py`, `zikkaron/restoration.py` | Supplied [RT-RTE-remember-recall](runtime.md#rt-rte-remember-recall), [RT-RTE-context-selection](runtime.md#rt-rte-context-selection), [RT-RTE-replay-context](runtime.md#rt-rte-replay-context); direct recall/curation reads, [EPI-RTE-recall-rewrite](#epi-rte-recall-rewrite) | Full CRDT conflict resolution and sensory-buffer lineage uninspected; no universal provenance guarantee. |
| MCP forget, validate_memory, rate_memory | `zikkaron/server.py`, `zikkaron/storage.py`, `zikkaron/staleness.py`, `zikkaron/thermodynamics.py` | Direct reads; [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal), [EPI-RTE-file-validation](#epi-rte-file-validation), [EPI-RTE-feedback-update](#epi-rte-feedback-update) | Whole derived-state withdrawal is not established. |
| Background/forced consolidation and sleep | `zikkaron/consolidation.py`, `zikkaron/curation.py`, `zikkaron/cls_store.py`, `zikkaron/sleep_compute.py`, `zikkaron/compression.py` | Direct selected producers/checks/consumers; [EPI-RTE-cls-consistency](#epi-rte-cls-consistency), [EPI-RTE-cls-promotion](#epi-rte-cls-promotion), [EPI-RTE-synthetic-facts](#epi-rte-synthetic-facts), [EPI-RTE-memory-compression](#epi-rte-memory-compression) | Astrocyte-domain transformations, full fractal clustering and sleep cluster summaries remain unassessed; prevents system-complete negative about acceptance or semantic preservation. |
| Insertion-time enrichment and profile extraction; callable belief derivation | `zikkaron/storage.py`, `zikkaron/enrichment.py`, `zikkaron/profiles.py` | Direct wiring and producer reads; [EPI-RTE-index-enrichment](#epi-rte-index-enrichment), [EPI-RTE-profile-beliefs](#epi-rte-profile-beliefs) | External ConceptNet responses and model outputs absent; no judgment of actual generated propositions. |
| Service reranking, implied passages, NLI, adversarial confidence | `zikkaron/retrieval.py` | Direct reads; [EPI-RTE-inferred-ranking](#epi-rte-inferred-ranking), supplied [RT-RTE-context-selection](runtime.md#rt-rte-context-selection) | All retrieval signals not independently verified; relevance scores do not establish truth. |
| Prompt/session hooks and installed integration | `zikkaron/hooks/prompt-recall.py`, `zikkaron/hooks/session-start-context.py`, `zikkaron/server.py` | Supplied [RT-RTE-hook-context](runtime.md#rt-rte-hook-context), [RT-RTE-install-integration](runtime.md#rt-rte-install-integration); direct prompt stale-filter search | Host execution/injection/compliance unobserved. |
| MCP hierarchical recall/drill-down/navigation and hot/stale/process/stat resources | `zikkaron/server.py`, `zikkaron/retrieval.py` | Direct registration/wrapper reads; supplied [RT-RTE-context-selection](runtime.md#rt-rte-context-selection), [RT-CMP-cognitive-map](runtime.md#rt-cmp-cognitive-map) | Full hierarchy internals unassessed; wrappers alone establish delivery, not validation. |
| MCP create_trigger, remember-trigger extraction and checking | `zikkaron/prospective.py`, `zikkaron/server.py` | Direct reads; [EPI-RTE-trigger-delivery](#epi-rte-trigger-delivery) | Full matching grammar unassessed; no truth license from firing. |
| MCP project story, narrative resource; sleep narrative production | `zikkaron/narrative.py`, `zikkaron/sleep_compute.py`, `zikkaron/server.py` | Direct selected reads; [EPI-RTE-narrative-production](#epi-rte-narrative-production) | Detailed extraction fidelity unassessed. |
| MCP coverage/gaps and causal-chain; maintenance graph discovery | `zikkaron/metacognition.py`, `zikkaron/causal_discovery.py`, `zikkaron/knowledge_graph.py`, `zikkaron/consolidation.py` | Direct selected reads; [EPI-RTE-coverage-advice](#epi-rte-coverage-advice), [EPI-RTE-causal-outputs](#epi-rte-causal-outputs) | PC event encoding, independence tests and orientation not fully inspected; prevents mathematical-correctness and causal-identification conclusions. |
| Rule admission, query and application | `zikkaron/server.py`, `zikkaron/rules_engine.py` | Supplied [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) | Fixed retrieval policy is not a truth oracle or universal access barrier. |
| Benchmark ingestion, retrieval, generation, F1 and LLM judgment | `benchmarks/run_locomo_jscore.py`, `benchmarks/run_longmemeval.py`, `benchmarks/run_locomo_ablation.py`, `benchmarks/run_benchmark_gpu.py`, `benchmarks/test_e_locomo.py`, `benchmarks/od_diagnostic.py` | Supplied [RT-RTE-evaluation-mode](runtime.md#rt-rte-evaluation-mode); direct LoCoMo judge/result reads, [EPI-RTE-answer-judgment](#epi-rte-answer-judgment) | Dataset/results/provider responses absent; non-LoCoMo evaluator details supplied rather than independently rechecked. No reproduced scores or component attribution. |

Knowledge/warrant claims: see [RT-CLM-write-gate](runtime.md#rt-clm-write-gate), [RT-CLM-context-replay](runtime.md#rt-clm-context-replay), [EPI-CLM-derived-facts](#epi-clm-derived-facts), [EPI-CLM-cls-consistency](#epi-clm-cls-consistency), [EPI-CLM-benchmark-benefit](#epi-clm-benchmark-benefit). The latency claim [RT-CLM-hook-budget](runtime.md#rt-clm-hook-budget) does not warrant content and is not independently reassessed here.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-RTE-remember-recall](runtime.md#rt-rte-remember-recall) | Caller statements about tasks/projects | see record | SRC-1, `zikkaron/server.py` | Authorship and external truth warrant unknown; natural-language SQLite content is interpreted by host. |
| [RT-RTE-seed-admission](runtime.md#rt-rte-seed-admission) | Project scan summaries | see record | SRC-1, `zikkaron/seed.py` | External source files absent; templates are not per-claim validation. |
| [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation) | Tool counts and truncated summaries | see record | SRC-1, `zikkaron/consolidation.py` | Counts can describe recorded calls, not prove tool outcomes. |
| [EPI-RTE-synthetic-facts](#epi-rte-synthetic-facts) | Modified-together assertions and dream relation suggestions | see record | SRC-1, `zikkaron/curation.py`, `zikkaron/sleep_compute.py` | Separate producers and conditions, shared ordinary memory consumer; no observed instances. |
| [EPI-RTE-cls-promotion](#epi-rte-cls-promotion) | Recurring-pattern schema | see record | SRC-1, `zikkaron/cls_store.py` | Word abstraction can change or destroy propositions. |
| [EPI-RTE-recall-rewrite](#epi-rte-recall-rewrite) | Existing text plus current query, or new query-as-memory | see record | SRC-1, `zikkaron/reconsolidation.py` | A question may be non-truth-apt; assertions in queries remain unverified. |
| [EPI-RTE-profile-beliefs](#epi-rte-profile-beliefs) | Profile attributes and derived preferences/traits | see record | SRC-1, `zikkaron/profiles.py` | SQLite symbolic fields contain natural-language values; evidence IDs do not prove entailment. |
| [EPI-RTE-index-enrichment](#epi-rte-index-enrichment) | Concepts, generated inferences; synthetic queries may be non-truth-apt | see record | SRC-1, `zikkaron/enrichment.py` | Generated content unavailable; form and truth-aptness vary by output. |
| [EPI-RTE-inferred-ranking](#epi-rte-inferred-ranking) | Transient inferred preferences/traits | see record | SRC-1, `zikkaron/retrieval.py` | Used as ranker input, not necessarily delivered verbatim. |
| [EPI-RTE-causal-outputs](#epi-rte-causal-outputs) | Directed entity relations claiming causes/effects | see record | SRC-1, `zikkaron/causal_discovery.py`, `zikkaron/knowledge_graph.py` | Fixed symbolic consumers; causal truth unestablished. |
| [EPI-RTE-coverage-advice](#epi-rte-coverage-advice) | Claims about available coverage plus advice | see record | SRC-1, `zikkaron/metacognition.py` | Numerical coverage and confidence are proxies, not checked adequacy for every task. |
| [EPI-RTE-narrative-production](#epi-rte-narrative-production) | Recorded counts, decisions, events and focus areas | see record | SRC-1, `zikkaron/narrative.py` | Extracted labels and truncations need not preserve qualification. |
| [EPI-RTE-file-validation](#epi-rte-file-validation) | File-change status, not memory truth | see record | SRC-1, `zikkaron/staleness.py` | Missing file reference can return valid. |
| [EPI-RTE-feedback-update](#epi-rte-feedback-update) | None in numerical confidence/stability update | see record | SRC-1, `zikkaron/thermodynamics.py` | Usefulness differs from factual accuracy. |
| [RT-OBJ-memory-rules](runtime.md#rt-obj-memory-rules), [EPI-RTE-trigger-delivery](#epi-rte-trigger-delivery) | Policy/conditions need not be truth-apt; reminder text can contain assertions | see records | SRC-1, `zikkaron/rules_engine.py`, `zikkaron/prospective.py` | Symbolic parsing/matching licenses selection, not truth. |
| [RT-OBJ-zikkaron-section](runtime.md#rt-obj-zikkaron-section), [RT-OBJ-hooks-config](runtime.md#rt-obj-hooks-config) | Primarily behavioral policy and executable configuration | see records | SRC-1, `zikkaron/server.py` | Installed policy is not use-derived accepted knowledge. |
| [RT-RTE-replay-context](runtime.md#rt-rte-replay-context) | Caller checkpoint/protected assertions | see record | SRC-1, `zikkaron/restoration.py` | Protection is operational preference, not corroboration. |
| [EPI-RTE-answer-judgment](#epi-rte-answer-judgment) | Generated answers and correctness labels | see record | SRC-1, `benchmarks/run_locomo_jscore.py` | Dataset gold supplies reference; provider response and actual correctness unknown. |
| [RT-CMP-embedding-engine](runtime.md#rt-cmp-embedding-engine), [RT-CMP-nli-model](runtime.md#rt-cmp-nli-model), [RT-CMP-comet-inferencer](runtime.md#rt-cmp-comet-inferencer) | Distributed-parametric internal content not individually identifiable | see records | SRC-1, `zikkaron/embeddings.py`, `zikkaron/retrieval.py`, `zikkaron/enrichment.py` | Truth-apt propositions in weights: not determinable from accessible artifacts. |

Other numerical operative parts remain separate: see [RT-CMP-gte-reranker](runtime.md#rt-cmp-gte-reranker), [RT-CMP-flashrank-ranker](runtime.md#rt-cmp-flashrank-ranker), [RT-CMP-cross-encoder](runtime.md#rt-cmp-cross-encoder), [RT-CMP-doc2-query](runtime.md#rt-cmp-doc2-query), [RT-CMP-hopfield-memory](runtime.md#rt-cmp-hopfield-memory), [RT-CMP-hdc-encoder](runtime.md#rt-cmp-hdc-encoder), [RT-CMP-cognitive-map](runtime.md#rt-cmp-cognitive-map), [RT-CMP-evaluation-models](runtime.md#rt-cmp-evaluation-models). Fixity, mutation and endpoint resolution are see each component record. Dense learned weights, rebuilt pattern matrices and use-updated transition state are not interchangeable evidence of learning or truth.

## Authority-route ledger

Every row is an architectural finding, not an observed event. Detailed endpoint, control and read-back fields are see the cited declaring record. Repeated records below split functions rather than duplicate identities.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-curation-merge](#epi-rte-curation-merge) | content transformation | implemented | [EPI-RTE-curation-merge](#epi-rte-curation-merge) | truth-apt transformation: non-ampliative reshaping | Caller and existing text | Cosine threshold plus token Jaccard >0.5; similarity/dedup domain | remember after gate | Concatenated text and tags | Overwrite existing row | Preserves both input texts, not their external warrant | Changes future selected memory | Retriever; SQLite text; advisory to host; later calls | SRC-1, `zikkaron/curation.py` | none | none | Operation unobserved |
| [EPI-RTE-contradiction-scan](#epi-rte-contradiction-scan) | check/evidence production | implemented | [EPI-RTE-contradiction-scan](#epi-rte-contradiction-scan) | no content change | Potential lexical conflict | Similarity plus negation/action-set comparison | Callable helper; no ordinary production caller found | Conflict list/reason | Internal confidence consumer follows | Lexical heuristic only | Identifies rows for confidence change | Helper; returned/branch-local result; advisory to caller; this invocation | SRC-1, `zikkaron/curation.py` | none | Not semantic truth evaluation | No observed invocation |
| [EPI-RTE-contradiction-scan](#epi-rte-contradiction-scan) | disposition/acceptance | implemented | [EPI-RTE-contradiction-scan](#epi-rte-contradiction-scan) | non-truth-apt policy/content update: lower confidence | Old flagged row | Negation/action divergence branch | Immediately after flag | Confidence minus 0.2 or 0.1, floor 0.1 | SQL mutation | Changed reliance proxy, not truth rejection | Alters later weighting/pruning eligibility | Metadata consumers; SQLite confidence; ranking/selection; later calls | SRC-1, `zikkaron/curation.py` | none | No resolution of which statement is true | Production caller unestablished |
| [EPI-RTE-cls-consistency](#epi-rte-cls-consistency) | check/evidence production | implemented | [EPI-RTE-cls-promotion](#epi-rte-cls-promotion) | no content change | Cluster member consistency | Negation-presence pair mismatch; lexical domain | Before schema generation | consistent boolean and conflict strings | Result consumed by promotion | Only equal negation-presence established; not semantic consistency | Can prevent schema promotion | CLS; returned dict; enforcing; this cycle | SRC-1, `zikkaron/cls_store.py` | [EPI-CLM-cls-consistency](#epi-clm-cls-consistency) | Lexical check weaker than semantic claim | Operation unobserved |
| [EPI-RTE-cls-promotion](#epi-rte-cls-promotion) | disposition/acceptance | implemented | [EPI-RTE-cls-promotion](#epi-rte-cls-promotion) | no content change | Cluster eligibility for semantic memory | Consistency boolean, schema nonempty, semantic similarity duplicate check | After pattern selection | Skip or insert schema | Enforcing operational admission | No established truth acceptance criterion for intended downstream use | Vetoes inconsistent or duplicate patterns | CLS insertion; code branch; enforcing; cycle | SRC-1, `zikkaron/cls_store.py` | [EPI-CLM-cls-consistency](#epi-clm-cls-consistency) | none | Operation unobserved |
| [EPI-RTE-cls-promotion](#epi-rte-cls-promotion) | content transformation | implemented | [EPI-RTE-cls-promotion](#epi-rte-cls-promotion) | truth-apt transformation: indeterminate | Selected episodic text to schema | Common-word threshold, stop-word removal; no semantic checker | Admitted clusters | Recurring-pattern text | Candidate generation | Semantic preservation/entailment not established | New text available to ordinary selection | Retriever; semantic row; advisory; later calls | SRC-1, `zikkaron/cls_store.py` | none | none | Need concrete cluster and proposition interpretation to classify each output |
| [EPI-RTE-cls-promotion](#epi-rte-cls-promotion) | retention | implemented | [EPI-RTE-cls-promotion](#epi-rte-cls-promotion) | no content change | Schema and derived_from links | Direct insertion and linking | Same cycle | Semantic memory plus retained episodes | Durable storage | Lineage exists without epistemic acceptance | Later dual-store recall may select schema | DualStoreCLS/retriever; rows/links; selection; later queries | SRC-1, `zikkaron/cls_store.py` | none | none | Operation unobserved |
| [EPI-RTE-synthetic-facts](#epi-rte-synthetic-facts) | content transformation | implemented | [EPI-RTE-synthetic-facts](#epi-rte-synthetic-facts) | truth-apt transformation: ampliative conjecture | Weighted co-occurrence to modified-together assertion | Weight >=10 and no exact duplicate | Memify cycle | Synthetic derived-fact text | Direct durable admission | Co-occurrence/heat weights do not entail modification frequency | Creates normal retrievable memory | Retriever; ordinary memory row; advisory; future calls | SRC-1, `zikkaron/curation.py` | [EPI-CLM-derived-facts](#epi-clm-derived-facts) | Proxy is promoted into stronger assertion | Operation unobserved |
| [EPI-RTE-synthetic-facts](#epi-rte-synthetic-facts) | content transformation | implemented | [EPI-RTE-synthetic-facts](#epi-rte-synthetic-facts) | truth-apt transformation: indeterminate | Random unconnected pair to dream relation | Embedding similarity >0.7 | Sleep dream replay | May-relate text plus graph link | Direct durable admission | Association candidate only; “may relate” has underspecified domain | Adds ordinary text and weak graph edge | Retriever/graph traversal; rows; selection/advisory; future calls | SRC-1, `zikkaron/sleep_compute.py` | none | none | Exact truth conditions of relation suggestion not specified |
| [EPI-RTE-inferred-ranking](#epi-rte-inferred-ranking) | content transformation | implemented | [EPI-RTE-inferred-ranking](#epi-rte-inferred-ranking) | truth-apt transformation: ampliative conjecture | Mention to preference assertion | Keyword rules, including camping; ignores negation | Open-domain FlashRank branch | Inferred passages | Rank input only | Counterexample demonstrates non-entailment | May improve maximum rank score of source memory | FlashRank; transient passage; ranking; current recall | SRC-1, `zikkaron/retrieval.py` | none | Inferred proposition stronger than source | Operation unobserved |
| [EPI-RTE-inferred-ranking](#epi-rte-inferred-ranking) | check/evidence production | implemented | [EPI-RTE-inferred-ranking](#epi-rte-inferred-ranking) | no content change | Query-memory relevance / textual entailment proxy | Cross-encoders and NLI truncated premise/hypothesis | Configured model-dependent reranking | Rank scores | Blended ordering, not factual veto | NLI score is not checked proof or source truth | Selects memory delivery; uncertainty flag does not itself abstain | Retriever; numerical scores; ranking; current call | SRC-1, `zikkaron/retrieval.py` | none | none | Model/class mapping and calibration unverified; dependency may fail |
| [EPI-RTE-file-validation](#epi-rte-file-validation) | check/evidence production | implemented | [EPI-RTE-file-validation](#epi-rte-file-validation) | no content change | Referenced file equality to saved hash | Hash comparison or missing-reference success | validate_memory or file watcher | valid/invalid status | Status return and mismatch branch | At most file freshness; no-reference valid is not truth validation | Supplies mismatch for metadata consumer | Caller/staleness logic; return/comparison; advisory/branching; current call | SRC-1, `zikkaron/staleness.py`, `zikkaron/server.py` | none | is_valid exceeds check domain if read as factual validity | Operation unobserved |
| [EPI-RTE-file-validation](#epi-rte-file-validation) | disposition/acceptance | implemented | [EPI-RTE-file-validation](#epi-rte-file-validation) | non-truth-apt policy/content update: stale flag and lower heat | File-mismatch-associated memories | Mismatch branch, plus watcher parent-directory selection | After file comparison | Stale flag and halved heat | Persisted metadata mutation | Withdraws freshness reliance, not a factual verdict | Can lower future selection and exclude in prompt hook | Prompt hook/retriever; metadata; filtering/ranking; future calls | SRC-1, `zikkaron/staleness.py`, `zikkaron/hooks/prompt-recall.py` | none | Not all read paths exclude stale rows | Operation unobserved |
| [EPI-RTE-feedback-update](#epi-rte-feedback-update) | behavior/policy adaptation | implemented | [EPI-RTE-feedback-update](#epi-rte-feedback-update) | non-truth-apt policy/content update: confidence and stability | Memory usefulness history | Caller boolean; useful_count/access_count after >3 accesses | rate_memory | Numerical confidence/stability | Persisted ranking/rewrite controls | Usefulness is not independent factual corroboration | Changes priority and susceptibility to future rewrite | Server sort/context packer/reconsolidation; DB scalars; ranking/selection; later calls | SRC-1, `zikkaron/thermodynamics.py`, `zikkaron/server.py`, `zikkaron/reconsolidation.py` | none | none | Operation unobserved |
| [EPI-RTE-recall-rewrite](#epi-rte-recall-rewrite) | disposition/acceptance | implemented | [EPI-RTE-recall-rewrite](#epi-rte-recall-rewrite) | no content change | Mismatch between query and retrieved memory | Embedding/directory/time/tag distance, stability/plasticity thresholds; protected veto | After current recall scoring | none/update/archive | Code decides rewrite; no fact acceptance | Thresholds license state change only | Rewrites future state or creates query memory | Reconsolidation; branch; enforcing; future calls | SRC-1, `zikkaron/server.py`, `zikkaron/reconsolidation.py` | none | none | Operation unobserved |
| [EPI-RTE-recall-rewrite](#epi-rte-recall-rewrite) | content transformation | implemented | [EPI-RTE-recall-rewrite](#epi-rte-recall-rewrite) | truth-apt transformation: indeterminate | Old memory and current query | Append with update delimiter; truncate old text if long; archive branch inserts query | After selection | Query-augmented/new text | Durable mutation | Imported assertion warrant unknown; question need not be truth-apt | Later retrieval can expose query-derived text | Retriever; mutated/new row; advisory; future calls | SRC-1, `zikkaron/reconsolidation.py` | none | none | Depends on query content; archive branch does not delete original |
| [EPI-RTE-index-enrichment](#epi-rte-index-enrichment) | check/evidence production | implemented | [EPI-RTE-index-enrichment](#epi-rte-index-enrichment) | no content change | Candidate enrichment terms | FPA cosine similarity to original embedding | Enabled expander output, before assembly | Kept/rejected similarity result | Threshold comparison | Association threshold only | Supplies subset for assembly | Enrichment pipeline; kept list; enforcing subset; this insertion | SRC-1, `zikkaron/enrichment.py` | none | Does not validate claims | Missing embedding can bypass FPA |
| [EPI-RTE-index-enrichment](#epi-rte-index-enrichment) | disposition/acceptance | implemented | [EPI-RTE-index-enrichment](#epi-rte-index-enrichment) | no content change | Supplement retention eligibility | Enabled branches and FPA-kept terms; logic bypasses FPA | Before enriched-content assembly | Omitted or appended terms | Code admission | No evidence-consuming factual acceptance established | Selects supplements retained/encoded | Enrichment/storage; list assembly; enforcing; insertion | SRC-1, `zikkaron/enrichment.py`, `zikkaron/storage.py` | none | Logic structural label not semantic verification | Generated outputs absent |
| [EPI-RTE-index-enrichment](#epi-rte-index-enrichment) | content transformation | implemented | [EPI-RTE-index-enrichment](#epi-rte-index-enrichment) | truth-apt transformation: indeterminate | Content to index supplements | ConceptNet/COMET/Doc2Query/logic with optional similarity filtering | Caller supplies settings/embeddings | Enriched fields and dense encoding | Index/ranking influence | Association and model generation are not checked entailment; imported warrant unknown | Can alter later vector selection | Embedding/index consumers; enriched fields/vectors; ranking; future calls | SRC-1, `zikkaron/enrichment.py`, `zikkaron/storage.py` | none | none | Generated outputs absent; different supplement types remain distinct |
| [EPI-RTE-profile-beliefs](#epi-rte-profile-beliefs) | content transformation | implemented | [EPI-RTE-profile-beliefs](#epi-rte-profile-beliefs) | truth-apt transformation: ampliative conjecture | Activity mentions to enjoys assertions | Substring categories and first name; fixed confidence 0.6 | Callable belief derivation | Belief row with evidence IDs | Direct persistence when called | Activity mention does not entail liking | Stored belief can enter recall after reranking | Retriever FTS belief search; row; ranking/advisory; future calls | SRC-1, `zikkaron/profiles.py`, `zikkaron/retrieval.py` | none | none | Production caller not found in scoped search; not evidence that this producer runs in ordinary insertion |
| [EPI-RTE-causal-outputs](#epi-rte-causal-outputs) | content transformation | implemented | [EPI-RTE-causal-outputs](#epi-rte-causal-outputs) | truth-apt transformation: ampliative conjecture | Co-occurrence plus order to caused_by relation | Threshold and temporal-order heuristic | Consolidation graph maintenance | Causal-labelled graph edge | Persisted graph organization | Temporal association does not entail causation | Changes graph available for traversal | Graph consumers; relation row; selection; later calls | SRC-1, `zikkaron/knowledge_graph.py` | none | none | Temporal helper and full downstream graph usage not independently verified |
| [EPI-RTE-causal-outputs](#epi-rte-causal-outputs) | check/evidence production | implemented | [EPI-RTE-causal-outputs](#epi-rte-causal-outputs) | truth-apt transformation: indeterminate | Event data to PC directed edges | PC procedure after minimum 5 variables/10 windows | Periodic discovery | DAG metadata and persisted directed edges | MCP causal-chain answers | Conditional statistical output only; causal assumptions unvalidated | Provides causes/effects to caller | get_causal_chain; DB edge query; advisory; later requests | SRC-1, `zikkaron/causal_discovery.py`, `zikkaron/server.py` | none | none | CI implementation/encoding/orientation partly uninspected; no causal experiment |
| [EPI-RTE-coverage-advice](#epi-rte-coverage-advice) | check/evidence production | implemented | [EPI-RTE-coverage-advice](#epi-rte-coverage-advice) | no content change | Stored-topic coverage and gaps | Density/entity/recency/confidence blend; thresholds 0.7/0.4 | Explicit coverage/gap request | sufficient/partial/insufficient advice | Advisory result | Description of proxy coverage, not verified answer adequacy | Asks caller to proceed or investigate; no enforcing gate | Host; MCP result; advisory; current task | SRC-1, `zikkaron/metacognition.py`, `zikkaron/server.py` | none | none | Operation unobserved |
| [EPI-RTE-memory-compression](#epi-rte-memory-compression) | content transformation | implemented | [EPI-RTE-memory-compression](#epi-rte-memory-compression) | truth-apt transformation: indeterminate | Memory text to gist/tag | Sentence scores, first/last selection, code preservation, tag truncation | Maintenance compression | Archived original and replacement content | Future ordinary reads receive compressed text | Omitted qualifications can change meaning; no fidelity evaluator found in read methods | Changes text available to retrieval | Retriever; replacement row; advisory; future calls | SRC-1, `zikkaron/compression.py` | none | none | Need specific input and clause dependencies for semantic classification |
| [EPI-RTE-narrative-production](#epi-rte-narrative-production) | content transformation | implemented | [EPI-RTE-narrative-production](#epi-rte-narrative-production) | truth-apt transformation: indeterminate | Project memory window to narrative | Counts plus truncated extracted decisions/events/entities/hot topics | Sleep auto_narrate | Persisted summary | Story tool/resource delivery | Recorded-count premise bounded to DB, interpretation of decisions/focus unchecked | Later story text supplies selected history | Host; narrative tool/resource; advisory; later calls | SRC-1, `zikkaron/narrative.py`, `zikkaron/sleep_compute.py` | none | none | Operation unobserved |
| [EPI-RTE-trigger-delivery](#epi-rte-trigger-delivery) | operational admission/selection/consumption | implemented | [EPI-RTE-trigger-delivery](#epi-rte-trigger-delivery) | non-truth-apt policy/content update: reminders and matching conditions | Reminder type and matching context | Type enumeration; fixed matcher and firing-count deactivation | remember and explicit create_trigger | Persisted reminder and triggered output | Context-conditioned delivery | No factual license from trigger match | May surface previously retained reminder | Host; remember response; advisory; triggering call | SRC-1, `zikkaron/prospective.py`, `zikkaron/server.py` | none | none | Detailed match grammar not fully assessed |
| [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal) | lineage/freshness/recovery | implemented | [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal) | no content change | Memory and named dependents | Caller ID; direct SQL deletion | forget or pruning | Memory/archive/transition/vector deletion | Enforcing store removal | Withdrawal of source row, not retraction of every derived proposition | Stops future ordinary lookup of deleted row | Store readers; SQL deletion; enforcing; subsequent calls | SRC-1, `zikkaron/storage.py`, `zikkaron/server.py` | none | none | Profile/belief evidence IDs are not traversed by inspected delete_memory |
| [EPI-RTE-answer-judgment](#epi-rte-answer-judgment) | check/evidence production | implemented | [EPI-RTE-answer-judgment](#epi-rte-answer-judgment) | no content change | Generated answer versus dataset gold | F1 lexical comparison; LLM judge accepts essential meaning and partial answers | After generation in benchmark | F1 and CORRECT/WRONG or judge error | Appends sample; aggregates and optional JSON persistence | Dataset-relative answer evaluation only | Changes reported scores, not production memory acceptance | Benchmark report; sample/aggregate; measurement; evaluation run | SRC-1, `benchmarks/run_locomo_jscore.py` | [EPI-CLM-benchmark-benefit](#epi-clm-benchmark-benefit) | none | No observed result or independently frozen oracle; judge errors counted false |
| [RT-RTE-remember-recall](runtime.md#rt-rte-remember-recall) | operational admission/selection/consumption | implemented | [RT-RTE-remember-recall](runtime.md#rt-rte-remember-recall) | truth-apt transformation: acquisition/import | Caller content | Predictive novelty policy and bypasses; curator/direct insert | Explicit remember | Reject or persist | Early veto and insertion | Imported source warrant unknown; novelty is not truth | Controls which caller text persists | Retriever/host; DB and MCP; selection/advisory; later calls | SRC-1, `zikkaron/server.py`, `zikkaron/predictive_coding.py` | [RT-CLM-write-gate](runtime.md#rt-clm-write-gate) | Gate is not storage-wide | Operation unobserved |
| [RT-RTE-rule-admission](runtime.md#rt-rte-rule-admission) | operational admission/selection/consumption | implemented | [RT-OBJ-memory-rules](runtime.md#rt-obj-memory-rules) | non-truth-apt policy/content update: retrieval rules | Symbolic policy | Parser/type validation then scoped rules application | Rule addition and later service recall | Error or filter/boost/penalty | Enforcing on covered retrieval path | Grammar validity only | Filters/reranks service results, not hooks/replay | RulesEngine; SQLite rules; enforcing/ranking; until changed | SRC-1, `zikkaron/rules_engine.py`, `zikkaron/retrieval.py` | none | none | See supplied route for bypass boundaries |

Retention is not lifecycle integration after acceptance. The CLS links constitute implemented organization, but no truth acceptance of the abstracted proposition has been established; the retention row deliberately does not call it lifecycle integration. No system-complete absence follows because the named unassessed transformations remain in scope.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-write-gate](runtime.md#rt-clm-write-gate) | see record | SRC-1, `zikkaron/predictive_coding.py`; doctrine/design | see record | [RT-RTE-remember-recall](runtime.md#rt-rte-remember-recall), [RT-RTE-seed-admission](runtime.md#rt-rte-seed-admission) | None supplied | None supplied | Gate selects novelty on explicit path | Novelty neither truth nor invariant across writers. |
| [RT-CLM-context-replay](runtime.md#rt-clm-context-replay) | see record | SRC-1, `zikkaron/restoration.py`; doctrine/design | see record | [RT-RTE-replay-context](runtime.md#rt-rte-replay-context), [RT-RTE-hook-context](runtime.md#rt-rte-hook-context) | None supplied | None supplied | Selected retained context can be reconstructed | Preferential bounded selection, not full conversation or factual validation. |
| [EPI-CLM-derived-facts](#epi-clm-derived-facts) | see record | SRC-1, `zikkaron/curation.py`; doctrine/design | see record | [EPI-RTE-synthetic-facts](#epi-rte-synthetic-facts) | None supplied | Heat can boost weights without modifications; no controlled outcome comparison | Automatic conjecture production and retained-state adaptation | “Derived-fact” is stronger than demonstrated warrant; improved capacity unestablished. |
| [EPI-CLM-cls-consistency](#epi-clm-cls-consistency) | see record | SRC-1, `zikkaron/cls_store.py`; doctrine/design | see record | [EPI-RTE-cls-consistency](#epi-rte-cls-consistency), [EPI-RTE-cls-promotion](#epi-rte-cls-promotion) | None supplied | No semantic-consistency validation | Real lexical veto before promotion | Equal negation flags do not imply consistent propositions. |
| [EPI-CLM-benchmark-benefit](#epi-clm-benchmark-benefit) | see record | SRC-1, `README.md`; reported operation | see record | [RT-RTE-evaluation-mode](runtime.md#rt-rte-evaluation-mode), [EPI-RTE-answer-judgment](#epi-rte-answer-judgment) | No inspectable results supplied | Different reader models explicitly confound QA comparison; no independent component intervention supplied | Shipped evaluator and attributed reported scores | Neither reproduced benefit nor specific causal contribution established. |

## Bounded conclusion

Zikkaron implements durable acquisition, selection and reshaping of caller text, trace summaries, project scans and checkpoints. Those routes grant operational availability, not automatic epistemic authority: see [RT-RTE-remember-recall](runtime.md#rt-rte-remember-recall), [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation), [RT-RTE-seed-admission](runtime.md#rt-rte-seed-admission), [RT-RTE-replay-context](runtime.md#rt-rte-replay-context). Acquired warrant is unknown, and transformations can degrade qualifications. Host delivery is advisory; rule filters enforce only their covered selection path, see [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery), [RT-BAP-retrieval-rules](runtime.md#rt-bap-retrieval-rules).

The inspected semantic-promotion check is consequential: a negation mismatch blocks promotion. Its criterion is lexical consistency of a cluster, intended use is admission of a generated semantic memory, and its scope is that cluster/cycle. It does not verify the schema's proposition against the world. Retaining a schema and connecting derived_from edges are therefore not evidence of accepted ampliative knowledge, see [EPI-RTE-cls-consistency](#epi-rte-cls-consistency), [EPI-RTE-cls-promotion](#epi-rte-cls-promotion). A separate contradiction detector can lower confidence, but production invocation was not found in the recorded search; its existence cannot be attributed to every remember call, see [EPI-RTE-contradiction-scan](#epi-rte-contradiction-scan).

The source produces conjectures, not merely storage artifacts: modification-frequency claims, mention-to-preference beliefs, transient inferred preferences, dream suggestions and causal-labelled graph structures. The concrete inferred-ranking counterexample establishes non-entailment on that route. Other model outputs and word abstractions remain locally indeterminate rather than automatically classified as conjecture or derivation. No inspected route demonstrates a new accepted ampliative proposition supported by an evidence-consuming decision with criterion, use and scope; the unassessed domain/sleep/graph internals prevent a system-complete negative. See [EPI-RTE-synthetic-facts](#epi-rte-synthetic-facts), [EPI-RTE-profile-beliefs](#epi-rte-profile-beliefs), [EPI-RTE-inferred-ranking](#epi-rte-inferred-ranking), [EPI-RTE-causal-outputs](#epi-rte-causal-outputs), [EPI-RTE-index-enrichment](#epi-rte-index-enrichment).

File validation supports a narrower check—reference equality/freshness—not truth. Usefulness feedback adapts numerical authority; recall can also rewrite retained text from a query before any later truth check. “Archive” preserves an archive and creates a new memory but does not remove the original in the inspected branch. Forget removes named rows without traversing profile/belief evidence references. These are independent authority and withdrawal limits, see [EPI-RTE-file-validation](#epi-rte-file-validation), [EPI-RTE-feedback-update](#epi-rte-feedback-update), [EPI-RTE-recall-rewrite](#epi-rte-recall-rewrite), [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal).

The benchmark has a genuine reference outcome: dataset gold supplied to F1 and the judge, not merely an unconstrained model opinion. Its operative consumer is the measurement/reporting path. That check licenses dataset-relative scores under a generous rubric, not general memory truth or an automatic deployed update. No observed result or causal comparison was supplied. Improved future capacity, exercised self-improvement, reliable reflection and theory-building iteration are separate unestablished properties, not consequences of the name memify. For memify, the boundary is the memory engine across consolidation cycles and later retrieval; the independent proposed objective is useful future retrieval. State updates and later consumers are wired, but objective-bearing outcome evidence selecting these updates and subsequent operation depending on them are not established, so the four-link exercised self-improvement attribution is not closed. See [EPI-CLM-derived-facts](#epi-clm-derived-facts), [EPI-RTE-feedback-update](#epi-rte-feedback-update), [EPI-RTE-answer-judgment](#epi-rte-answer-judgment).

## Shared records

### Routes

#### EPI-RTE-curation-merge
Label: Curation merge

Part of: [RT-RTE-remember-recall](runtime.md#rt-rte-remember-recall)

SRC-1, `zikkaron/curation.py`, `zikkaron/server.py`. The curator is the ingestion subroute of the supplied remember container. Caller proposes content; code chooses merge/link/create. Merge concatenates text, unions tags and re-embeds; neither human veto nor expected-answer oracle is wired. Operating mode is open requests. Gate rejection precedes this part. No whole-update rollback is shown.

The separately assessed contradiction helper is see [EPI-RTE-contradiction-scan](#epi-rte-contradiction-scan); it is not an automatic step established in this merge route.

- Immediate return: Action/memory ID dictionary.
- Later read-back: Merged text reaches ordinary recall.
- Delegated visibility: Host receives memory result, not a new delegated agent context.
- Selection predicate: Similarity and Jaccard overlap.
- Invalidation or expiry: Ordinary forgetting, curation or decay; no transaction-wide rollback evidenced.
- Activation or effect: Persisted merge mutation wired.
- Evidence limits: No runs or semantic equivalence check supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> merged_content = existing["content"] + "\n" + new_content
> --- `zikkaron/curation.py`

#### EPI-RTE-contradiction-scan
Label: Callable contradiction scan

SRC-1, `zikkaron/curation.py`. Distinct from the ingestion route [RT-RTE-remember-recall](runtime.md#rt-rte-remember-recall) and its merge part [EPI-RTE-curation-merge](#epi-rte-curation-merge): this is a separately callable check with its own confidence-mutation consumer. Search for `detect_contradictions(` across SRC-1 `zikkaron/` found the definition and test use, not a production caller. Similar memories (>=0.7) are checked for unequal negation presence or divergent action-token sets. Program returns possible conflicts and immediately lowers old confidence by 0.2 or 0.1. It does not decide which proposition is true. For “Alice uses Python” and “Alice uses Java”, identical action sets and no negation produce no flag if the pair is selected; their intended scopes could nevertheless conflict. Conversely unrelated negation can flag a pair. This is a predicate deduction, not execution. Caller supplies candidate and embedding; code decides flags/mutations without human veto or expected-answer oracle. Mode is callable open input. Recovery is later metadata change/deletion, not a demonstrated rollback.

- Immediate return: Possible-conflict dictionaries with old memory content and reason.
- Later read-back: Mutated confidence is available to later ranking, pruning and coverage consumers if the helper is invoked.
- Delegated visibility: Caller receives conflict list; no independent critic agent.
- Selection predicate: Similarity >=0.7, negation-presence difference or action-set divergence.
- Invalidation or expiry: Later confidence updates/deletion can change effect; no automatic reversal shown.
- Activation or effect: Callable evaluator and internal confidence mutation implemented; ordinary remember invocation not established.
- Evidence limits: No run; absence of a production caller in this scoped search does not prove no external caller.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

> if new_has_negation != old_has_negation:
>     contradictions.append({
>         "memory_id": mem_id,
>         "content": old_content,
>         "similarity": sim,
>         "reason": "negation_mismatch",
>     })
> --- `zikkaron/curation.py`

> old_confidence = mem.get("confidence", 1.0)
> self._storage._conn.execute(
>     "UPDATE memories SET confidence = ? WHERE id = ?",
>     (max(old_confidence - 0.2, 0.1), mem_id),
> )
> --- `zikkaron/curation.py`

#### EPI-RTE-cls-consistency
Label: CLS cluster consistency check

Part of: [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation)

SRC-1, `zikkaron/cls_store.py`. Distinct check stage inside the runtime maintenance container; it precedes, and is not the same referent as, semantic promotion. Program evaluates each cluster pair for unequal negation presence; returns consistent only when no such pair is found. The promotion consumer skips inconsistent clusters. No human review or answer oracle. A cluster containing “Alice uses Python” and “Alice uses Java” passes this lexical check regardless of whether their project/version scopes actually conflict. Conversely unrelated negated and positive statements can fail. The counterexamples are static deductions about the inspected predicate, not executed tests.

- Immediate return: Consistency boolean and conflict strings.
- Later read-back: inapplicable — checker returns a current-cycle result; subsequent promotion owns persistence.
- Delegated visibility: Promotion code receives result; no delegated model.
- Selection predicate: Negation-presence inequality in any pair.
- Invalidation or expiry: inapplicable — result recomputed for each cluster.
- Activation or effect: Veto wired through continue in promotion.
- Evidence limits: Checks lexical polarity, not contradiction logic or source truth.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if has_neg_a != has_neg_b:
>     contradictions.append(
> --- `zikkaron/cls_store.py`

#### EPI-RTE-cls-promotion
Label: CLS semantic promotion

Part of: [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation)

SRC-1, `zikkaron/cls_store.py`, `zikkaron/consolidation.py`. A material maintenance part distinct from its lexical checker. Idle/forced cycles call CLS. Cluster selection proposes episodes; code can veto inconsistency, empty schema and similar existing semantic memory. It admits a generated schema, sets semantic type, links source episodes and retains them. Guidance is common-word thresholds, stop-word deletion and at most 15 phrase words; no answer oracle or per-schema human approval. This licenses operational admission, not epistemic acceptance. No rollback is shown for partial insertion/linking.

- Immediate return: Pattern/promotion/skipped counters.
- Later read-back: Semantic rows can enter dual-store query; derived_from links retain episode association.
- Delegated visibility: Retriever receives stored schema; host receives selected output.
- Selection predicate: Recurring pattern, lexical consistency, nonempty abstraction and duplicate threshold.
- Invalidation or expiry: Ordinary deletion/maintenance; original episodes are not deleted by promotion.
- Activation or effect: Schema insertion and linking wired.
- Evidence limits: No actual cluster/output; removing negation as a stop word prevents a blanket semantic-preservation claim.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> consistency = self.check_consistency(cluster_mems)
> if not consistency["consistent"]:
>     stats["skipped_inconsistent"] += 1
>     continue
> --- `zikkaron/cls_store.py`

#### EPI-RTE-synthetic-facts
Label: Memify facts and dream suggestions

Part of: [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation)

SRC-1, `zikkaron/curation.py`, `zikkaron/sleep_compute.py`, `zikkaron/consolidation.py`. Distinct production part within maintenance, split by producer in the ledger. Memify proposes a modified-together assertion for co_occurrence weight >=10, exact-deduplicates, embeds and inserts it with derived/auto-generated tags. Earlier reweight can add 0.5 for hot endpoints and weight >=5, so crossing the threshold need not mean ten observed modifications. Co-occurrence does not entail modification frequency. Dream replay proposes “may relate” text for randomly selected unconnected memories with similarity >0.7 and adds a weak edge. Both directly admit candidates under fixed heuristics, without human review, answer oracle or evidence-consuming truth decision. Open idle/forced maintenance, not a controlled improvement curriculum. Later pruning removes cold/low-confidence unused memories; it is not falsification of their propositions. No whole-cycle rollback shown.

- Immediate return: Derived/insight counters.
- Later read-back: Ordinary memory retrieval and graph selection can use inserted candidates.
- Delegated visibility: Selected text later reaches host; no autonomous critic or delegated agent.
- Selection predicate: Memify weight/duplicate checks; dream random pair/connectivity/similarity checks.
- Invalidation or expiry: Forget, decay and ordinary pruning; no semantic retraction protocol evidenced here.
- Activation or effect: Automatic durable conjecture production wired.
- Evidence limits: No observed candidate, acceptance or capacity gain; dream truth conditions underspecified.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> derived_content = f"{src_name} and {tgt_name} are frequently modified together"
> --- `zikkaron/curation.py`

> if avg_heat > 0.7 and weight >= 5.0:
>     # Both entities are hot AND relationship is established -> boost
>     new_weight = weight + 0.5
> --- `zikkaron/curation.py`

> content = f"Dream connection: {summary_a} may relate to {summary_b}"
> --- `zikkaron/sleep_compute.py`

#### EPI-RTE-inferred-ranking
Label: Inferred passages and ranking checks

Part of: [RT-RTE-context-selection](runtime.md#rt-rte-context-selection)

SRC-1, `zikkaron/retrieval.py`. A material part of service context selection. Deterministic trace: input “Alice dislikes camping.” matches the capitalized-subject expression, contains camping, and yields “Alice enjoys outdoor activities, nature, camping, hiking, and national parks.” No negation/preference check intervenes. Disliking camping does not entail enjoying it; this establishes ampliative conjecture rather than merely unproven entailment. In open-domain FlashRank mode, inferred text is scored as an extra passage and maximum passage score is mapped to the original memory. The conjecture changes ranking, not necessarily returned content.

NLI is a separate check: target is whether the first 512 memory characters support a question-to-statement hypothesis, domain is model-predicted textual entailment. Code assumes probability index 2, then blends with cross-encoder scores. It neither proves the premise true nor records a truth-acceptance decision. Adversarial checking computes abstain, but the inspected recall consumer only copies confidence and logs uncertainty; it does not branch on abstain. Numerical evidence therefore licenses ranking/advice, not enforced abstention.

- Immediate return: Scored selected memories; inferred text is internal ranker supply.
- Later read-back: inapplicable — this subroute does not persist inferred passages; outer recall separately changes access/rewrite state.
- Delegated visibility: Ranker sees extra inferred passage; host sees original selected memory after remaining packing.
- Selection predicate: Open-domain branch, configured models; maximum variant score, NLI blend and later selection.
- Invalidation or expiry: inapplicable — passage/score state is current-call only.
- Activation or effect: Rank-score effect wired; activation or benefit unobserved.
- Evidence limits: Model calibration, class mapping and external artifacts unverified; deterministic deduction uses implementation only.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if any(word in lower for word in ("camping", "campfire", "meteor shower", "hiking", "forest", "mountains")):
>     _add(f"{subject} enjoys outdoor activities, nature, camping, hiking, and national parks")
> --- `zikkaron/retrieval.py`

> hypothesis = _question_to_statement(query)
> pairs = [(m["content"][:512], hypothesis) for m in memories]
> scores = self._nli_model.predict(pairs)  # Shape: (n, 3) for [contradiction, neutral, entailment]
> --- `zikkaron/retrieval.py`

> if self._settings.ADVERSARIAL_DETECTION_ENABLED and result_memories:
>     adv_info = self._detect_adversarial(result_memories)
>     for mem in result_memories:
>         mem["_retrieval_confidence"] = adv_info["confidence"]
>     if adv_info["is_uncertain"]:
>         logger.debug(
>             "Low retrieval confidence (%.3f), score_gap=%.3f",
>             adv_info["confidence"], adv_info["score_gap"]
>         )
> --- `zikkaron/retrieval.py`

#### EPI-RTE-file-validation
Label: File freshness validation

SRC-1, `zikkaron/server.py`, `zikkaron/staleness.py`, `zikkaron/hooks/prompt-recall.py`. No supplied counterpart covers this exposed operation's evaluator domain. validate_memory calls the detector when initialized; its target is saved file-hash equality. Missing memory fails, missing hash or unresolved reference succeeds, changed hash lowers heat and flags stale. MCP fallback has different path resolution: it hashes directory_context and similarly treats missing saved hash as valid. The file watcher can flag all parent-directory memories as well as matching hashes. The prompt hook filters stale rows. This is operative freshness metadata, not acceptance of the natural-language memory. Success does not authenticate authorship or source correctness.

- Immediate return: MCP memory_id/is_valid/reason dictionary.
- Later read-back: Heat and stale flags affect future consumers; prompt FTS/vector SQL require is_stale=0.
- Delegated visibility: Caller sees status; later host receives filtered context.
- Selection predicate: Current/saved hash comparison; missing-reference exceptions above.
- Invalidation or expiry: No automatic truth certification or all-path retraction; successful unchanged check does not itself clear all stale state in read method.
- Activation or effect: Mismatch metadata mutation and prompt exclusion wired.
- Evidence limits: Only selected consumers verified; direct directory context does not filter by stale flag in inspected storage query.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not file_hash:
>     return {"valid": True, "reason": "no file reference"}
> --- `zikkaron/staleness.py`

> if current_hash != file_hash:
>     new_heat = memory["heat"] / 2.0
>     self._storage.update_memory_heat(memory_id, new_heat)
>     self._storage.update_memory_staleness(memory_id, True)
>     return {"valid": False, "reason": "file changed"}
> --- `zikkaron/staleness.py`

#### EPI-RTE-feedback-update
Label: Usefulness confidence and stability update

SRC-1, `zikkaron/server.py`, `zikkaron/thermodynamics.py`, `zikkaron/reconsolidation.py`, `zikkaron/metacognition.py`. Distinct exposed rate_memory operation, not a duplicate of supplied generic context selection. Caller proposes was_useful; human versus automated authorship unresolved. Code accepts it without independent truth review, records counts and updates stability. After more than three accesses confidence becomes useful_count/access_count. It is consumed by server heat*confidence sorting and metacognitive chunk scoring; stability changes rewrite thresholds. No expected answer oracle, experiment, per-rating veto or rollback. Mode is open feedback; guidance is fixed count/stability formula. A useful false claim and a useless true claim are possible, so this is not truth calibration.

- Immediate return: Rated status, counters, confidence and stability.
- Later read-back: Persisted scalars affect later ranking, coverage advice and reconsolidation susceptibility.
- Delegated visibility: Caller receives rating result; no delegated judging context.
- Selection predicate: Existing memory and supplied boolean; count threshold for confidence.
- Invalidation or expiry: Later feedback/forget modifies or removes state; no rating reversal protocol shown.
- Activation or effect: Durable behavior-determining metadata update wired.
- Evidence limits: No observed helpfulness, accuracy or capacity comparison; callers not authenticated as evaluators in wrapper.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if access_count > 3:
>     confidence = useful_count / access_count
> else:
>     confidence = mem.get("confidence", 1.0)
> --- `zikkaron/thermodynamics.py`

#### EPI-RTE-recall-rewrite
Label: Query-driven reconsolidation

Part of: [RT-RTE-context-selection](runtime.md#rt-rte-context-selection)

SRC-1, `zikkaron/server.py`, `zikkaron/reconsolidation.py`. Part of the supplied service context-selection loop, after current scoring. Server calls reconsolidate(memory ID, query, empty directory). Program computes weighted embedding/directory/time/tag mismatch, changes plasticity, then vetoes rewriting for protected memories or low mismatch. Moderate mismatch appends current query, truncating old text when necessary; high mismatch archives old content and inserts current query with old tags. Contrary to an extinction/replacement reading, the inspected archive branch does not delete or disable the original. The current response remains the already-selected dictionaries; future reads see changed DB state. No fact oracle or per-change human veto; guidance is fixed thresholds plus use-derived stability. Archive is recovery material, not evidence an automatic rollback is invoked.

- Immediate return: Internal action/mismatch/new-content dictionary, ignored by recall wrapper.
- Later read-back: Mutated or new memories are available on later calls; current scored return is not rebuilt.
- Delegated visibility: Host current return and future DB contents differ; no delegated agent.
- Selection predicate: Protected flag, mismatch, stability and plasticity thresholds.
- Invalidation or expiry: Later edits/forget; archive retention depends on original deletion and storage lifecycle.
- Activation or effect: Durable query-fed update wired, semantic benefit unobserved.
- Evidence limits: Queries can be non-truth-apt or false; directory argument is empty, not authenticated project identity.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> _reconsolidation.reconsolidate(m["id"], query, "")
> --- `zikkaron/server.py`

#### EPI-RTE-index-enrichment
Label: Index-time enrichment

SRC-1, `zikkaron/storage.py`, `zikkaron/enrichment.py`. Distinct caller-conditioned insertion subroute spanning the supplied remember/seed/evaluation containers; not part of exactly one supplied route. Requires settings, embedding engine, embedding and minimum length; normal direct insert callers need not supply these. Separate parts are ConceptNet acquired concepts (external warrant unknown), COMET generated inference, Doc2Query questions (not necessarily truth-apt), and fixed logic expansion fragments. Optional FPA uses similarity, not proposition validation. Code directly persists supplements/model-name metadata and updates the memory embedding column using enriched text; then the inspected end of insertion inserts the original local embedding variable into the vector table. Therefore changed ranking from that particular enriched vector is consumer-dependent, not universally guaranteed. No per-supplement human approval, expected-answer oracle or whole-insert rollback. Guidance is enabled expanders/filter thresholds, not outcome criticism.

- Immediate return: Outer storage returns memory ID.
- Later read-back: Enrichment columns persist; numerical consumers may see updated DB embedding, but initial vector insert uses original variable.
- Delegated visibility: Host normally sees original content, not proof of supplements; models receive source text.
- Selection predicate: Flags, minimum length, model availability and similarity filtering.
- Invalidation or expiry: Caller updates/deletion; exact provider content not frozen.
- Activation or effect: Persistence/encoding wiring inspected; actual expansion and consumer-specific use unobserved.
- Evidence limits: Cannot individuate model-produced propositions without outputs; syntax/association terms do not imply sound logical inference.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if enrichment_data.get("enriched_content") and embeddings_engine is not None:
>     new_embedding = embeddings_engine.encode_document_enriched(
>         memory["content"], enrichment_data["enriched_content"]
>     )
> --- `zikkaron/storage.py`

> similarity = float(np.dot(original_vec, text_vec))
> if similarity >= threshold:
>     kept.append(text)
> --- `zikkaron/enrichment.py`

#### EPI-RTE-profile-beliefs
Label: Profile extraction and callable beliefs

SRC-1, `zikkaron/profiles.py`, `zikkaron/storage.py`, `zikkaron/retrieval.py`. A mixed production/consumption chain not wholly contained in one supplied route. Settings-enabled insertion calls ProfileExtractor and persists attributes/evidence IDs. BeliefDeriver separately maps activity substrings to enjoys assertions and fixed 0.6 confidence; trait/preference patterns and multi-profile summaries have their own fixed confidences/evidence references. A mention such as “Alice dislikes camping” is insufficient warrant for enjoys-outdoor-category. Search for derive_from_memory/derive_from_profiles across `zikkaron/` found definitions and tests, not a production invocation; ordinary insertion therefore does not establish belief generation. Existing belief rows are nevertheless consumed by FTS and merged after cross-encoder reranking. Software proposes/admit values; no human approval or gold oracle. Current source specifies no evidence-consuming truth acceptance or production rollback.

- Immediate return: Profile extraction side effect / callable belief insertion; outer insert returns memory ID.
- Later read-back: Profile and belief FTS rows become synthetic recall results with confidence-based scores.
- Delegated visibility: Host can receive structured-value summaries; no delegated critic.
- Selection predicate: Extraction patterns/category substring match; retrieval FTS/confidence.
- Invalidation or expiry: Update/delete methods and ordinary store lifetime; inspected memory deletion does not traverse evidence IDs.
- Activation or effect: Profile insertion and belief consumer wired; production belief producer invocation unestablished.
- Evidence limits: Model-free extraction still requires semantic interpretation; source IDs are lineage, not confirmation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> belief_content = f"enjoys {label} (evidence: {', '.join(activities)})"
> --- `zikkaron/profiles.py`

#### EPI-RTE-causal-outputs
Label: Causal-labelled graph outputs

Part of: [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation)

SRC-1, `zikkaron/knowledge_graph.py`, `zikkaron/causal_discovery.py`, `zikkaron/consolidation.py`, `zikkaron/server.py`. A maintenance subroute with separately exposed read consumer. Temporal heuristic assigns caused_by to sufficiently weighted co-occurrences ordered by a helper; association plus temporal ordering does not entail causation. PC discovery is separate: after >=5 variables and >=10 windows it calls pc_algorithm and persists directed edges for resolvable entities; periodic consolidation invokes it after an event counter reaches 50. The MCP causal-chain wrapper returns the PC engine's graph answer, not necessarily heuristic graph edges. These consumers are kept separate. Program proposes and admits graph updates without human review, expected-answer oracle or verified causal intervention. Full CI/orientation implementation and assumptions remain unassessed; the claim is not that PC cannot identify causes under suitable assumptions. No update-wide rollback or old-edge withdrawal policy established.

- Immediate return: Counters/DAG metadata or causes/effects dictionary.
- Later read-back: Directed edges persisted for later causal-chain requests; heuristic relations remain graph state.
- Delegated visibility: Host receives graph answer; no autonomous causal experiment.
- Selection predicate: Heuristic co-occurrence/order; PC minimum data and resulting edges.
- Invalidation or expiry: Deletion/supersession of old causal edges not traced; no current-completeness guarantee.
- Activation or effect: Discovery/storage/query wiring present; no observed or causal validation.
- Evidence limits: PC algorithm internals and observational assumptions not fully inspected; cannot certify encoding or identify true causal edges.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> dag = self.pc_algorithm(data, variable_names)
> 
> # Store directed edges in causal_dag_edges table
> --- `zikkaron/causal_discovery.py`

#### EPI-RTE-coverage-advice
Label: Metacognitive coverage advice

SRC-1, `zikkaron/metacognition.py`, `zikkaron/server.py`. New exposed operation omitted from the supplied principal routes. The check target is available topic coverage, not whether a specific answer is true. Code blends density, entity coverage, recency and mean confidence; >=0.7 yields sufficient/advice to proceed, >=0.4 partial, otherwise insufficient. Gap detection emits descriptions and suggested investigations. MCP returns the advice; no inspected wrapper enforces investigation or prevents answering. It is evidence about local proxies, not a measured guarantee of adequate knowledge. Current-run check, no proposal admission/rollback and no expected-answer oracle.

- Immediate return: Coverage/confidence/suggestion/gaps or gap list.
- Later read-back: inapplicable — advisory result is not persisted by these wrappers.
- Delegated visibility: Host receives advice; no delegated inspection task automatically launched.
- Selection predicate: Query/directory, retrieval proxies and thresholds.
- Invalidation or expiry: inapplicable — each request recomputes current advice.
- Activation or effect: Advice delivery wired; changed host behavior unobserved.
- Evidence limits: Density/recency and usefulness-derived confidence do not prove factual completeness.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if overall >= 0.7:
>     suggestion = "sufficient"
>     detail = "Proceed with confidence — strong knowledge coverage."
> --- `zikkaron/metacognition.py`

#### EPI-RTE-memory-compression
Label: Gist and tag compression

Part of: [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation)

SRC-1, `zikkaron/compression.py`, `zikkaron/consolidation.py`. Maintenance part, not a new acceptance route. Code chooses compression by schedule, archives original, selects high-score sentences with first/last and code blocks, replaces content/embedding, then optionally generates a shortened tag representation. No human approval, truth oracle or semantic equivalence checker is shown in read extraction/update methods. This is extraction/reshaping in form, but proposition preservation is indeterminate without clause-level interpretation of actual input: omitted conditions can change truth. Source archive/original_content affords reconstruction; neither proves automatic retrieval uses the original. Admission is automatic according to schedule and compression level; no cycle-wide rollback.

- Immediate return: Gist/tag string and cycle counters.
- Later read-back: Ordinary consumers receive replacement text; archive/original_content are separate recovery material.
- Delegated visibility: Host later sees selected compressed memory, not necessarily original.
- Selection predicate: Schedule/level plus sentence scores and length target.
- Invalidation or expiry: Further compression and deletion; delete_memory also removes associated archives.
- Activation or effect: Content/embedding replacement wired.
- Evidence limits: Full compression schedule/decompression consumers unassessed; no lossless guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # Archive original content
> self._storage.insert_archive({
>     "original_memory_id": memory_id,
>     "content": original_content,
>     "embedding": memory.get("embedding"),
>     "archive_reason": "compression",
> })
> --- `zikkaron/compression.py`

#### EPI-RTE-narrative-production
Label: Narrative production and story read

Part of: [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation)

SRC-1, `zikkaron/narrative.py`, `zikkaron/sleep_compute.py`, `zikkaron/server.py`. Distinct sleep-produced state and story/resource consumers, compared with the runtime maintenance container. Sleep invokes auto_narrate; active directories without recent narrative get memory-window counts and bounded extracted decisions/events/entities/focus text. Code directly inserts narrative entries, and story retrieval concatenates summaries chronologically. No human approval, expected answer oracle or truth acceptance; guidance is fixed extraction/time-window policy. A count is entailed only about recorded DB entries selected by this window, not actual work or successful outcomes. Detailed extracted propositions remain indeterminate. Recovery is later stored entries/operator action; no automatic revision loop shown.

- Immediate return: Inserted entry/counters or story string.
- Later read-back: Narrative entries persist and reach get_project_story and narrative resource.
- Delegated visibility: Host receives concatenated summaries rather than all source rows.
- Selection predicate: Directory, created-at window, active heat and narrative interval; limited lists.
- Invalidation or expiry: New time windows/entry selection; withdrawal propagation unassessed.
- Activation or effect: Sleep production and later read wired.
- Evidence limits: No actual narrative; extraction fidelity and completeness not verified.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> entry_id = self._storage.insert_narrative_entry(entry)
> entry["id"] = entry_id
> return entry
> --- `zikkaron/narrative.py`

> stats["narrative"] = self._narrative.auto_narrate()
> --- `zikkaron/sleep_compute.py`

#### EPI-RTE-trigger-delivery
Label: Prospective reminder delivery

SRC-1, `zikkaron/prospective.py`, `zikkaron/server.py`. Part of remember includes automatic future-phrase extraction and checking of prior reminders; explicit create_trigger is an additional producer. This spans more than one supplied referent. Program validates trigger type, directly persists reminder/condition/directory, matches context, increments counts and deactivates after count limit. Caller or regex proposes text; code admits it without per-content human approval. No gold oracle or fact check. Triggering is operational matching, not claim confirmation. Guidance is fixed phrase/type/match policy; no automatic rollback beyond deactivation is shown.

- Immediate return: Created reminder ID or triggered reminder material in remember flow.
- Later read-back: Persisted reminders can match later remember contexts.
- Delegated visibility: Host receives triggered reminder through response, not a separately tasked agent.
- Selection predicate: Valid type; context match; firing count.
- Invalidation or expiry: Count-based deactivation; detailed matching grammar unassessed.
- Activation or effect: Persistence and later condition-driven selection wired.
- Evidence limits: Reminder can contain claims or instructions; no factual license follows.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> _prospective.auto_create_from_content(content, context)
> --- `zikkaron/server.py`

> if triggered_memories:
>     memory["triggered_prospective_memories"] = [
>         {"id": pm["id"], "content": pm["content"]}
>         for pm in triggered_memories
>     ]
> --- `zikkaron/server.py`

#### EPI-RTE-memory-withdrawal
Label: Memory deletion and dependent-state limits

SRC-1, `zikkaron/server.py`, `zikkaron/storage.py`. Exposed forget is distinct from runtime's remember/recall container; memify pruning is an alternate caller of the same deletion primitive. Caller proposes ID; code checks existence and deletes. delete_memory explicitly removes archives, transitions and vector rows before the memory; it does not traverse profile/belief evidence_memory_ids. Thus retaining derived evidence IDs does not establish dependency retraction. No expected-answer oracle or human per-content veto; deliberate caller deletion is not a recorded factual rejection. Guidance is caller ID or pruning thresholds. No automatic undo; archive deletion can remove recovery material.

- Immediate return: Deleted/not_found status.
- Later read-back: Deleted memory no longer reaches ordinary lookup; independent profile/belief rows can remain queryable.
- Delegated visibility: Host receives status; later consumers see surviving state.
- Selection predicate: ID existence or caller pruning predicate.
- Invalidation or expiry: Deletion is terminal absent external copy; no automatic rollback.
- Activation or effect: Scoped removal wired, not universal epistemic withdrawal.
- Evidence limits: No concurrent-failure test or complete dependency cleanup audit; no whole-system retraction guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> self._conn.execute("DELETE FROM memories WHERE id = ?", (memory_id,))
> self._conn.commit()
> --- `zikkaron/storage.py`

#### EPI-RTE-answer-judgment
Label: Benchmark answer judgment

Part of: [RT-RTE-evaluation-mode](runtime.md#rt-rte-evaluation-mode)

SRC-1, `benchmarks/run_locomo_jscore.py`. Check part of supplied evaluation container; generation, judging and deployed memory changes are not conflated. Operator supplies data/configuration and model/provider. Gold answer is an explicit expected-answer oracle for F1 and judge, withheld from generation in supplied runtime trace. Judge compares generated answer with gold under a generous essential-meaning/partial-answer rubric. F1 is lexical similarity under category handling, not independent truth proof. Driver maps CORRECT to true, exceptions to false, appends samples, aggregates and optionally saves JSON. Result consumer is measurement/reporting, not production-memory or model-weight admission. This is bounded benchmark mode; retries/fallbacks are not rollback of a product update. Provider fixity/caching limits are see [RT-CMP-evaluation-models](runtime.md#rt-cmp-evaluation-models).

- Immediate return: F1, correctness boolean and reasoning in samples and aggregate report.
- Later read-back: Optional output file can be read by operator; no automatic production-policy read-back established.
- Delegated visibility: Generation sees question/selected context; judge sees question/gold/generated answer.
- Selection predicate: Question subset/category, f1-only flag, selected generation/judge configuration.
- Invalidation or expiry: Operator controls result lifetime; evaluator failures become false scores.
- Activation or effect: Scoring/reporting wired, observed scores absent.
- Evidence limits: No dataset/results/provider traces; answer scores do not identify mechanism effects or transfer.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> j_correct = judgment["label"].upper() == "CORRECT"
> j_reasoning = judgment.get("reasoning", "")
> --- `benchmarks/run_locomo_jscore.py`

### Claims

#### EPI-CLM-derived-facts
Label: Memify derived facts and self-improvement

SRC-1, `zikkaron/curation.py`; doctrine/design. Distinct claim from [RT-CLM-write-gate](runtime.md#rt-clm-write-gate): automatic synthetic fact production and improvement during maintenance, not explicit ingestion novelty. Its implemented route is [EPI-RTE-synthetic-facts](#epi-rte-synthetic-facts). The source calls the cycle self-improvement; this does not establish an improvement objective measured against outcomes or exercised improvement. The transformation is stronger than its weighted co-occurrence premise.

> """Generate synthetic derived-fact memories for high-weight entity pairs."""
> --- `zikkaron/curation.py`

> """Run the full memify self-improvement cycle.
> --- `zikkaron/curation.py`

#### EPI-CLM-cls-consistency
Label: CLS consistency verification

SRC-1, `zikkaron/cls_store.py`; doctrine/design. No supplied claim counterpart after comparison with [RT-CLM-write-gate](runtime.md#rt-clm-write-gate); this targets semantic-promotion consistency rather than novelty. The lexical implementation in [EPI-RTE-cls-consistency](#epi-rte-cls-consistency) does not establish the unqualified semantic claim.

> """Verify cluster members don't contradict each other.
> --- `zikkaron/cls_store.py`

#### EPI-CLM-benchmark-benefit
Label: Reported benchmark and knowledge-update benefit

SRC-1, `README.md`; reported operation and doctrine/design. No supplied claim counterpart: [RT-RTE-evaluation-mode](runtime.md#rt-rte-evaluation-mode) is the executable evaluation container, not this public outcome claim. README reports LoCoMo Recall@10 86.8%, BEAM overall 0.404 and attributes update/contradiction abilities to thermodynamics/reconsolidation/metadata. It explicitly discloses different readers, preventing attribution of the entire QA contrast to retrieval. No output artifacts or causal intervention were supplied. [EPI-RTE-answer-judgment](#epi-rte-answer-judgment) supports a measurement procedure, not these reported numbers.

> One important caveat: the BEAM paper's baselines use GPT-4.1-nano as the reader model. We use Claude Opus 4.6, which is substantially more capable. The instruction-following result (0.750 with a retrieval MRR of just 0.086) demonstrates that reader quality contributes to QA scores independently of retrieval quality. Our retrieval metrics (MRR 0.422, Recall@10 0.353) are model-independent and directly comparable to the paper's baselines.
> --- `README.md`

### Behavioral-authority paths

none declared in this member; delivery and rule authority are see [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery), [RT-BAP-retrieval-rules](runtime.md#rt-bap-retrieval-rules). Route declarations above identify distinct scalar-update and measurement consumers without redefining those paths.
