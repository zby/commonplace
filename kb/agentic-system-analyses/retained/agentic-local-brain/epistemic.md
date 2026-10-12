---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Agentic Local Brain epistemic routes: imported content, generated metadata and wiki text, structural checks, retrieval authority and bounded warrant."
run-id: AAS-2026-10-12-agentic-local-brain-f00cbd577178-01
reviewed-boundary: "41ea0cb104686eb0d39f32c94c2b84d37cdff0e7"
---

# Agentic Local Brain epistemic report

## Source-and-claim boundary

The question is how this knowledge application imports or generates truth-apt content, checks it, licenses reliance and supplies later consumers. Scope and exclusions are those of [boundary](boundary.md#boundary-and-evidence); evidence identity and layers are in its [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design only. The excluded desktop-agent host and development hooks do not become Local Brain evaluators or capabilities. No installation trace, user knowledge store, model output specimen or causal experiment was supplied. Consequently, factual quality, exercised acceptance, successful persistence/reuse and improvement remain unobserved.

The supplied runtime is provisional. Direct inspection adds structural filtering, deterministic summary extraction, numeric relation/topic criteria, recommendation adaptation, item withdrawal, a shipped duplicate-cleanup driver and the category recompilation criterion. Public claims are [RT-CLM-context-answer](runtime.md#rt-clm-context-answer), [EPI-CLM-wiki-synthesis](#epi-clm-wiki-synthesis) and [EPI-CLM-staleness-tracking](#epi-clm-staleness-tracking). The last has a specific implementation mismatch: changing source text without changing category document IDs need not trigger recompilation.

| Entry point or operation | SRC-1 source path | Coverage and records | Limit / conclusion prevented |
|---|---|---|---|
| Console and HTTP dispatch | `kb/cli.py`; `kb/web/app.py` | Direct dispatch search; supplied [RT-RTE-file-admission](runtime.md#rt-rte-file-admission), [RT-RTE-chat-query](runtime.md#rt-rte-chat-query), [RT-RTE-mining-run](runtime.md#rt-rte-mining-run) | Registered operations are not proof every collector or consumer was inspected. |
| File admission and host fallback | `kb/commands/collect.py`; `skills/localbrain-collect/SKILL.md` | Supplied [RT-RTE-file-admission](runtime.md#rt-rte-file-admission), [RT-RTE-host-fallback](runtime.md#rt-rte-host-fallback) | Individual webpage, email, bookmark and paper fetch/parser bodies remain unassessed; prevents source-complete fidelity/authenticity conclusions. |
| Extraction and cleanup | `kb/processors/tag_extractor.py`; `kb/processors/builtin_extractor.py`; `kb/processors/entity_extractor.py` | Direct bounded reads; [EPI-RTE-structural-checks](#epi-rte-structural-checks), [EPI-RTE-extractive-summary](#epi-rte-extractive-summary) | Provider output semantics and truth not demonstrated. |
| Legacy/enhanced RAG and ranking | `kb/query/retrieval_pipeline.py`; `kb/query/reranker.py`; `kb/query/rag.py` | Direct confidence/scoring reads plus supplied [RT-RTE-chat-query](runtime.md#rt-rte-chat-query), [RT-RTE-legacy-query](runtime.md#rt-rte-legacy-query), [EPI-RTE-confidence-metadata](#epi-rte-confidence-metadata) | Expansion/context/history details rely on runtime; no observed answer/citation quality. |
| Mining relations/topics | `kb/processors/doc_relation_builder.py`; `kb/processors/topic_clusterer.py` | Direct reads plus [RT-RTE-mining-run](runtime.md#rt-rte-mining-run); [EPI-RTE-numeric-selection](#epi-rte-numeric-selection) | External HDBSCAN internals uninspected; full clustering labels and embedding semantics are not truth tests. |
| Wiki synthesis, browsing and recompilation | `kb/processors/wiki_compiler.py`; `kb/web/routes/wiki.py` | Direct compile/parser/budget/staleness reads; supplied browsing in [RT-RTE-wiki-compile](runtime.md#rt-rte-wiki-compile); [EPI-RTE-category-recompilation](#epi-rte-category-recompilation) | Entity-card and subcategory generation details not independently fully traced; prevents complete semantic-generation enumeration. |
| Reading history and recommendations | `kb/web/routes/items.py`; `kb/web/routes/recommendations.py`; `kb/processors/recommendation.py` | Direct view/history-weighted selection reads; [EPI-RTE-history-recommendation](#epi-rte-history-recommendation) | Recommendation reason-generation details unassessed; no evidence that recommendations improve future action. |
| Editing, deleting and duplicate cleanup | `kb/web/routes/items.py`; `kb/storage/sqlite_storage.py`; `tests/cleanup_duplicate_webpages.py` | Direct deletion and cleanup reads; supplied [RT-RTE-item-update](runtime.md#rt-rte-item-update); [EPI-RTE-item-withdrawal](#epi-rte-item-withdrawal), [EPI-RTE-title-cleanup](#epi-rte-title-cleanup) | Other fixture-generation/processing/URL-cleanup drivers remain unassessed, not excluded; prevents a system-complete negative about evaluators or disposition. |
| Settings, replacement code, backup/restore | `kb/web/routes/settings.py`; `kb/self_update.py`; `kb/commands/backup.py` | Supplied [RT-RTE-settings-update](runtime.md#rt-rte-settings-update), [RT-RTE-product-update](runtime.md#rt-rte-product-update), [RT-RTE-backup-restore](runtime.md#rt-rte-backup-restore) | These admit configuration/code/archives, not source truth. Actual external successor bytes and restoration unobserved. |
| Graph/topics/export/tag/front-end and remaining tests | `kb/commands/`; `kb/web/static/`; `tests/` | Included but detailed epistemic consumers/evaluation suites uninspected | No universal absence of testing, criticism, acceptance or lifecycle integration is asserted. |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-collected-metadata](#epi-obj-collected-metadata) | Imported text and summaries can assert source-domain facts; tags are indexing policy unless interpreted as subject claims | see record | SRC-1 `kb/processors/tag_extractor.py` | Source warrant unknown; generated summaries not established faithful. |
| [EPI-OBJ-entity-relations](#epi-obj-entity-relations) | Entity descriptions and typed relations assert facts about named entities; mention links assert association to a document | see record | SRC-1 `kb/processors/entity_extractor.py` | Structural admissibility is separate from assertion truth. |
| [EPI-OBJ-wiki-article](#epi-obj-wiki-article) | Topic/entity articles can assert source-domain facts | see record | SRC-1 `kb/processors/wiki_compiler.py` | Actual proposition instances unavailable; cannot determine entailment or novelty. |
| [EPI-OBJ-chat-answer](#epi-obj-chat-answer) | Generated answer/history text can assert facts; container also holds separately assessed confidence | see record | SRC-1 `kb/query/retrieval_pipeline.py` | Container membership does not transfer answer-content authority to the score. |
| [EPI-OBJ-answer-confidence](#epi-obj-answer-confidence) | None: heuristic numeric score, not answer-content truth probability | see record | SRC-1 `kb/query/retrieval_pipeline.py` | Retrieval-only producer; advisory result/cache consumer, not saved answer text or a factual evaluator. |
| [RT-CMP-litellm-provider](runtime.md#rt-cmp-litellm-provider) | Provider weights: individuated truth-apt content not determinable from accessible calling code | see record | SRC-1 `kb/processors/tag_extractor.py`; `kb/query/retrieval_pipeline.py` | Opaque distributed-parametric state; generated response content is assessed separately above. |
| [RT-CMP-query-expander](runtime.md#rt-cmp-query-expander) | Rewrites/entities/intent are retrieval suggestions; any particular truth-apt assertion not determinable | see record | SRC-1 `kb/query/query_expander.py` | Query rewriting is not intrinsically knowledge production. |
| [RT-CMP-llm-reranker](runtime.md#rt-cmp-llm-reranker) | Relevance scores license ranking, not factual truth | see record | SRC-1 `kb/query/reranker.py` | Score-domain checks do not establish relevance calibration. |
| [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider) | Dense representations: truth-apt proposition not individuated | see record | SRC-1 `kb/processors/embedder.py` | Exact weights/version/provenance opaque; no training inferred from stored vectors. |
| [EPI-RTE-numeric-selection](#epi-rte-numeric-selection) | Stored numeric similarity and shared-entity counts support statements over represented vectors/mention rows; topical interpretation is additional | see record | SRC-1 `kb/processors/doc_relation_builder.py` | Numeric and semantic domains must remain separate. |
| [RT-OBJ-prompt-templates](runtime.md#rt-obj-prompt-templates), [RT-OBJ-config](runtime.md#rt-obj-config) | Task guidance and symbolic control policy, not an answer oracle | see records | SRC-1 `kb/query/prompt_templates.py`; `kb/config-template.yaml` | Natural-language requests do not enforce compliance. |
| [EPI-RTE-history-recommendation](#epi-rte-history-recommendation) | Reading-event IDs/times feed preference policy; no truth-apt new claim required for selection | see record | SRC-1 `kb/processors/recommendation.py` | Reading history is not outcome evidence of correctness. |

## Authority-route ledger

Rows distinguish checking, disposition and retention even where the same record contains their implementation. Fields owned by records are supplied by citation rather than copied. No row denotes observed execution.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-file-admission](runtime.md#rt-rte-file-admission) | content transformation | implemented | [EPI-OBJ-collected-metadata](#epi-obj-collected-metadata) | truth-apt transformation: acquisition/import | External text enters retained file | see route | see route | see route | see route | Source warrant unknown, not upgraded by admission | see route | see route | SRC-1 `kb/commands/collect.py` | none | none | Parser/fetch alternatives unassessed. |
| [RT-RTE-host-fallback](runtime.md#rt-rte-host-fallback) | content transformation | doctrine only | [EPI-OBJ-collected-metadata](#epi-obj-collected-metadata) | truth-apt transformation: acquisition/import | Host-obtained text enters file admission | see route | see route | see route | see route | Original webpage lineage/warrant unknown | see route | see route | SRC-1 `skills/localbrain-collect/SKILL.md` | none | none | Host compliance unobserved. |
| [RT-RTE-file-admission](runtime.md#rt-rte-file-admission) | content transformation | implemented | [EPI-OBJ-collected-metadata](#epi-obj-collected-metadata) | truth-apt transformation: indeterminate | Model summary generation | see route | see route | see route | see route | Candidate summary, not established faithful compression | see route | see route | SRC-1 `kb/processors/tag_extractor.py` | none | none | Output specimens and source comparison needed; generated tags can be non-truth-apt indexing policy. |
| [RT-RTE-mining-run](runtime.md#rt-rte-mining-run) | content transformation | implemented | [EPI-OBJ-entity-relations](#epi-obj-entity-relations) | truth-apt transformation: indeterminate | Entity/typed-relation generation | see route | see route | see route | see route | Candidate source-domain descriptions/relations only | see route | see route | SRC-1 `kb/processors/entity_extractor.py` | none | none | Structural endpoint checks do not establish entailment or non-entailment. |
| [RT-RTE-wiki-compile](runtime.md#rt-rte-wiki-compile) | content transformation | implemented | [EPI-OBJ-wiki-article](#epi-obj-wiki-article) | truth-apt transformation: indeterminate | Article synthesis | see route | see route | see route | see route | Candidate article, not established accepted ampliative claim | see route | see route | SRC-1 `kb/processors/wiki_compiler.py` | [EPI-CLM-wiki-synthesis](#epi-clm-wiki-synthesis) | none | Generated output and checked input interpretation needed; budget truncation degrades available evidence. |
| [RT-RTE-chat-query](runtime.md#rt-rte-chat-query), [RT-RTE-legacy-query](runtime.md#rt-rte-legacy-query) | content transformation | implemented | [EPI-OBJ-chat-answer](#epi-obj-chat-answer); legacy answer | truth-apt transformation: indeterminate | Answer generation from retrieved context | see routes | see routes | see routes | see routes | Candidate answer only | see routes | see routes | SRC-1 `kb/query/retrieval_pipeline.py`; `kb/query/rag.py` | [RT-CLM-context-answer](runtime.md#rt-clm-context-answer) | none | Enhanced history/cache and legacy fallback differ; neither proves semantic preservation or novelty. |
| [EPI-RTE-extractive-summary](#epi-rte-extractive-summary) | content transformation | implemented | [EPI-OBJ-collected-metadata](#epi-obj-collected-metadata) | truth-apt transformation: non-ampliative reshaping | Source-sentence selection | see record | see record | see record | see record | Warrant no stronger than selected source; omission can lose qualification | see record | see record | SRC-1 `kb/processors/builtin_extractor.py` | none | none | Concrete complete-sentence case established; truncation branches need separate semantic caution. |
| [EPI-RTE-structural-checks](#epi-rte-structural-checks) | check/evidence production | implemented | [EPI-OBJ-collected-metadata](#epi-obj-collected-metadata) | no content change | Tag type/length/count and summary length | see record: tag branch | see record | see record | see record | Metadata shape/size only | see record | see record: extraction caller | SRC-1 `kb/processors/tag_extractor.py` | none | none | No source-fidelity check established. |
| [EPI-RTE-structural-checks](#epi-rte-structural-checks) | disposition/acceptance | implemented | [EPI-OBJ-collected-metadata](#epi-obj-collected-metadata) | truth-apt transformation: indeterminate | Tags padded/truncated; long summary truncated | see record: tag branch | see record | see record | see record | Operational size/count admissibility only | see record | see record: extraction caller | SRC-1 `kb/processors/tag_extractor.py` | none | none | Tag policy update need not be truth-apt; truncating summary can lose necessary conditions. |
| [EPI-RTE-structural-checks](#epi-rte-structural-checks) | check/evidence production | implemented | [EPI-OBJ-entity-relations](#epi-obj-entity-relations) | no content change | Allowed entity/relation types and endpoint membership | see record: entity branch | see record | see record | see record | Vocabulary and referential license only | see record | see record: extraction/save caller | SRC-1 `kb/processors/entity_extractor.py` | none | none | False relation among allowed endpoints can pass. |
| [EPI-RTE-structural-checks](#epi-rte-structural-checks) | disposition/acceptance | implemented | [EPI-OBJ-entity-relations](#epi-obj-entity-relations) | truth-apt transformation: non-ampliative reshaping | Surviving entity/relation subset | see record: entity branch | see record | see record | see record | Structural admission, not source-domain acceptance | see record | see record: extraction/save caller | SRC-1 `kb/processors/entity_extractor.py` | none | none | Discarded candidates are not refuted. |
| [EPI-RTE-structural-checks](#epi-rte-structural-checks) | check/evidence production | implemented | [EPI-OBJ-wiki-article](#epi-obj-wiki-article) | no content change | JSON parseability | see record: wiki branch | see record | see record | see record | Parseability only | see record | see record: compiler | SRC-1 `kb/processors/wiki_compiler.py` | none | none | Parse failure does not veto text retention. |
| [EPI-RTE-structural-checks](#epi-rte-structural-checks) | disposition/acceptance | implemented | [EPI-OBJ-wiki-article](#epi-obj-wiki-article) | truth-apt transformation: indeterminate | Parsed data or raw-response-prefix fallback | see record: wiki branch | see record | see record | see record | Renderable candidate, not accepted claim | see record | see record: compiler | SRC-1 `kb/processors/wiki_compiler.py` | none | none | Prefix fallback can change meaning; no formal schema validator established. |
| [RT-RTE-file-admission](runtime.md#rt-rte-file-admission) | retention | implemented | [EPI-OBJ-collected-metadata](#epi-obj-collected-metadata) | no content change | File/frontmatter, metadata and search-index writes | see route | see route | see route | see route | Retained source/candidate available, not endorsed | see route | see route | SRC-1 `kb/commands/collect.py` | none | none | Indexing failure can coexist with collection success. |
| [RT-RTE-mining-run](runtime.md#rt-rte-mining-run) | retention | implemented | [EPI-OBJ-entity-relations](#epi-obj-entity-relations); numerical derived state | no content change | Derived SQLite tables | see route | see route | see route | see route | Graph associations available, not factual acceptance | see route | see route | SRC-1 `kb/processors/entity_extractor.py` | none | none | Stage failures and alternate drivers differ. |
| [RT-RTE-wiki-compile](runtime.md#rt-rte-wiki-compile) | retention | implemented | [EPI-OBJ-wiki-article](#epi-obj-wiki-article) | no content change | Article file and metadata writes | see route | see route | see route | see route | Durable candidate article available for browsing | see route | see route | SRC-1 `kb/processors/wiki_compiler.py` | [EPI-CLM-wiki-synthesis](#epi-clm-wiki-synthesis) | none | No factual acceptance or coordinated file/database transaction established. |
| [RT-RTE-chat-query](runtime.md#rt-rte-chat-query) | retention | implemented | [EPI-OBJ-chat-answer](#epi-obj-chat-answer) | no content change | Attempted session-turn writes and result cache | see route | see route | see route | see route | Prior answer available as context, not confirmed | see route | see route | SRC-1 `kb/query/retrieval_pipeline.py` | none | none | Cache hits/empty retrieval/save failure defeat universal turn retention. |
| [RT-RTE-chat-query](runtime.md#rt-rte-chat-query), [RT-RTE-legacy-query](runtime.md#rt-rte-legacy-query), [RT-CMP-llm-reranker](runtime.md#rt-cmp-llm-reranker) | operational admission/selection/consumption | implemented | Stored text, generated history, expansion/ranking proposals | no content change | Relevance and context inclusion, not assertion truth | see records | see routes | see routes | see records | Context inclusion and ranking only | see routes | see routes; prompt force in [RT-BAP-template-guidance](runtime.md#rt-bap-template-guidance) | SRC-1 `kb/query/retrieval_pipeline.py`; `kb/query/reranker.py` | [RT-CLM-context-answer](runtime.md#rt-clm-context-answer) | none | Returned source IDs can exceed model-delivered text; options omitted from cache key. |
| [EPI-RTE-confidence-metadata](#epi-rte-confidence-metadata) | check/evidence production | implemented | [EPI-OBJ-answer-confidence](#epi-obj-answer-confidence) | non-truth-apt policy/content update: heuristic confidence metadata | Retrieval scores, unique sources and stage labels | see record | see record | see record | see record | Arithmetic score-domain license, not answer-truth probability | see record | see record | SRC-1 `kb/query/retrieval_pipeline.py` | none | confidence label exceeds established calibration | Answer content is not an input to the formula. |
| [EPI-RTE-numeric-selection](#epi-rte-numeric-selection) | check/evidence production | implemented | Stored document vectors | truth-apt transformation: entailed derivation | Cosine similarity | see record: vector branch | see record | see record | see record | Derived numerical similarity over supplied vectors only | see record | see record: relation builder | SRC-1 `kb/processors/doc_relation_builder.py` | none | none | Does not establish semantic relation truth; zero-norm branch returns 0. |
| [EPI-RTE-numeric-selection](#epi-rte-numeric-selection) | check/evidence production | implemented | Entity mention rows | truth-apt transformation: entailed derivation | Shared-mention count | see record: SQL branch | see record | see record | see record | Count/association over stored rows only | see record | see record: relation builder | SRC-1 `kb/processors/doc_relation_builder.py` | none | none | Upstream extracted mentions remain candidates, not confirmed source facts. |
| [EPI-RTE-numeric-selection](#epi-rte-numeric-selection) | disposition/acceptance | implemented | Document relation candidates | no content change | Numeric threshold or shared-row criterion | see record | see record | see record | see record | Admission criterion for graph association, not factual acceptance | see record | see record | SRC-1 `kb/processors/doc_relation_builder.py` | none | none | No independent oracle validates embedding meaning. |
| [EPI-RTE-numeric-selection](#epi-rte-numeric-selection) | behavior/policy adaptation | implemented | Topic memberships/centroids | non-truth-apt policy/content update: nearest-cluster membership and running centroid | Nearest centroid threshold and document existence | see record | see record | see record | see record | Topic classification license only | see record | see record | SRC-1 `kb/processors/topic_clusterer.py` | none | none | Later classification sees changed centroid; improvement not established. |
| [EPI-RTE-history-recommendation](#epi-rte-history-recommendation) | behavior/policy adaptation | implemented | Reading history and document embeddings | non-truth-apt policy/content update: history-weighted recommendation selection | Current preference proxy | see record | see record | see record | see record | Recommendation rank, not knowledge warrant | see record | see record | SRC-1 `kb/processors/recommendation.py` | none | none | No explicit answer/outcome test; reason generation unassessed. |
| [EPI-RTE-item-withdrawal](#epi-rte-item-withdrawal) | disposition/acceptance | implemented | Stored item | no content change | Requested item ID | see record: HTTP branch | see record | see record | see record | Withdrawal from selected substrates, not refutation | see record | see record: HTTP storage path | SRC-1 `kb/web/routes/items.py` | none | none | File deletion optional; vector/file failures can be swallowed; cached/derived text withdrawal unestablished. |
| [EPI-RTE-title-cleanup](#epi-rte-title-cleanup) | disposition/acceptance | implemented | Equal-title webpage groups | no content change | Exact title equality within listed rows | see record | see record | see record | see record | Operational deduplication, not semantic equivalence | see record | see record: SQLite cleanup driver | SRC-1 `tests/cleanup_duplicate_webpages.py` | none | none | Keeps first row, deletes others without content comparison; limited listing and SQLite-only deletion. |
| [EPI-RTE-category-recompilation](#epi-rte-category-recompilation) | lineage/freshness/recovery | implemented | [EPI-OBJ-wiki-article](#epi-obj-wiki-article) | no content change | Category source-ID set change or force | see record | see record | see record | see record | Recompilation eligibility, not endorsement | see record | see record | SRC-1 `kb/processors/wiki_compiler.py` | [EPI-CLM-staleness-tracking](#epi-clm-staleness-tracking) | Same-ID text edits not detected by this predicate | No content hash/version comparison in inspected predicate. |
| [RT-RTE-item-update](runtime.md#rt-rte-item-update) | disposition/acceptance | implemented | Caller-provided title/summary/notes/tags | truth-apt transformation: acquisition/import | Existing ID and supplied fields | see route | see route | see route | see route | Caller assertions admitted; warrant unknown | see route | see route | SRC-1 `kb/web/routes/items.py` | none | none | Caller identity/human authorship and semantic endorsement unresolved. |
| [RT-RTE-settings-update](runtime.md#rt-rte-settings-update), [RT-RTE-product-update](runtime.md#rt-rte-product-update), [RT-RTE-backup-restore](runtime.md#rt-rte-backup-restore) | lineage/freshness/recovery | implemented | Configuration, installed code, archives | non-truth-apt policy/content update: configure, replace or restore machinery/state | Syntax/install/hash/backup availability checks | see routes | see routes | see routes | see routes; configuration path in [RT-BAP-config-selection](runtime.md#rt-bap-config-selection) | Integrity/availability checks do not validate retained assertions | see routes | see routes | SRC-1 `kb/web/routes/settings.py`; `kb/self_update.py`; `kb/commands/backup.py` | none | none | Hash bypass, cached constructors and manual restore placement limit force. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-context-answer](runtime.md#rt-clm-context-answer) | see record | SRC-1 `kb/query/prompt_templates.py`; doctrine/design | see record | [RT-RTE-chat-query](runtime.md#rt-rte-chat-query) | none supplied | No answer oracle, citation verification or controlled comparison established in this path | Requests contextual/cited answers and supplies selected content | Compliance, factual fidelity and benefit unknown; legacy/template/cache alternatives retain separate conditions. |
| [EPI-CLM-wiki-synthesis](#epi-clm-wiki-synthesis) | see record | SRC-1 `README.md`; doctrine/design | see record | [RT-RTE-wiki-compile](runtime.md#rt-rte-wiki-compile), [EPI-RTE-structural-checks](#epi-rte-structural-checks) | none supplied | Parsing and persisted source IDs do not validate statements or complete consumption | Implemented candidate synthesis and durable article browsing | Coherence, truth and faithful contradiction handling unobserved. |
| [EPI-CLM-staleness-tracking](#epi-clm-staleness-tracking) | see record | SRC-1 `README.md`; doctrine/design | see record | [EPI-RTE-category-recompilation](#epi-rte-category-recompilation) | none supplied | Same document-ID set can contain changed text | Source-set changes/force can select recompilation | Broader source-document-change detection not supported by the inspected criterion. |

## Bounded conclusion

Local Brain wires imported text, generated metadata, extracted entity relations, wiki articles and conversation turns into retention and later use. These functions are established separately from factual acceptance: see [RT-RTE-file-admission](runtime.md#rt-rte-file-admission), [RT-RTE-mining-run](runtime.md#rt-rte-mining-run), [RT-RTE-wiki-compile](runtime.md#rt-rte-wiki-compile) and [RT-RTE-chat-query](runtime.md#rt-rte-chat-query). Import preserves access to candidate source content, but no source-truth/authenticity warrant is established. Generated summaries, relations, articles and answers may preserve or change claims; accessible code without output specimens cannot decide their semantic relation. Ampliative conjecture is not inferred merely from model generation.

The deterministic summary case in [EPI-RTE-extractive-summary](#epi-rte-extractive-summary) establishes sentence selection and reordering, not independent confirmation. [EPI-RTE-numeric-selection](#epi-rte-numeric-selection) licenses computed similarity/count claims over vectors and mention rows, not conclusions about the source domain. Its premises are stored representations with unknown semantic warrant, so no warranted real-world derivation follows from numerical validity alone.

The structural criteria in [EPI-RTE-structural-checks](#epi-rte-structural-checks) enforce allowed types, relation endpoints, counts and parseability, and their results change which fields survive. They are real checks, not factual acceptance. The inspected wiki parser can substitute raw response text after parse failure. The confidence route [EPI-RTE-confidence-metadata](#epi-rte-confidence-metadata) produces the separate numeric part [EPI-OBJ-answer-confidence](#epi-obj-answer-confidence) without inspecting answer assertions. Its result/cache consumers receive advisory metadata; this does not license the paired answer's truth. Retrieval ranking permits or prevents content inclusion; prompt instructions are advisory to the answer model. Neither ranking nor continuation grants epistemic authority beyond those domains.

No evidence-consuming factual acceptance decision, with a criterion, intended use and source-domain scope, is established for the inspected generation/admission paths. Their source links and retention therefore do not establish post-acceptance lifecycle integration. This is not a system-complete absence: remote collectors, entity-card/subcategory details, remaining consumers and test/data drivers retain explicit inspection gaps. It is also not a requirement that an operational personal-KB application implement a universal truth oracle.

History-weighted recommendations and changing topic centroids directly adapt selection without requiring a truth-apt theory route ([EPI-RTE-history-recommendation](#epi-rte-history-recommendation), [EPI-RTE-numeric-selection](#epi-rte-numeric-selection)). This establishes behavioral capacity, not improved capacity or exercised self-improvement. Provider parameters are not changed by the inspected calling paths; exact versions are not pinned and endpoints may resolve to different weights, as separately recorded in the supplied runtime components. Local retention is not evidence of provider training.

Withdrawal is operational and substrate-specific, not criticism/refutation; duplicate cleanup uses title equality, not content equivalence ([EPI-RTE-title-cleanup](#epi-rte-title-cleanup), a part of [EPI-RTE-item-withdrawal](#epi-rte-item-withdrawal)). HTTP withdrawal attempts vector and optional file deletion; the cleanup driver only calls SQLite deletion. Neither effect boundary transfers to the other. Recompilation uses source-ID set changes or force, and can miss same-ID text edits ([EPI-RTE-category-recompilation](#epi-rte-category-recompilation)). No particular formulated theory, content-directed criticism or iterative theory revision is established from inaccessible model output. Those uncertainties do not establish absent theories, reflection, learning or autonomy. No run or causal evidence supports actual answer quality, reliable reuse, improved retrieval or self-improvement.

## Shared records

### Operative objects

#### EPI-OBJ-collected-metadata
Label: Collected text and extracted summary/tag parts

Part of: [RT-RTE-file-admission](runtime.md#rt-rte-file-admission)

This object is the material retained output of that route, not a duplicate of the route. Source-native identities: saved Markdown body, `summary` and `tags`. Natural-language body/summary and symbolically selected tags have different epistemic roles. Substrates: Markdown/frontmatter and SQLite knowledge/tag fields; chunks/vectors have their own runtime component account. Imported body warrant is unknown. Model summary truth-apt fidelity is indeterminate; built-in summary selection is separately assessed. Evidence: SRC-1 `kb/processors/tag_extractor.py`; file persistence and consumer passages in the parent record.

> tags = data.get("tags", [])
> summary = data.get("summary", "")
> --- `kb/processors/tag_extractor.py`

#### EPI-OBJ-entity-relations
Label: Entity descriptions and typed source-linked relations

Part of: [RT-RTE-mining-run](runtime.md#rt-rte-mining-run)

Material output part of mining, distinct from its orchestration. Source-native identities: `entities`, `entity_mentions`, `entity_relations`, `entity_relation_sources`. Descriptions/context are natural language; entity/type/endpoint/source identifiers are symbolic. SQLite is the substrate. The model proposes source-domain descriptions and relations; normalized names and source-document contexts retain lineage but do not validate facts. Evidence: SRC-1 `kb/processors/entity_extractor.py`; generated extraction and persistence passages below in the structural-check record.

> INSERT OR IGNORE INTO entity_relation_sources (relation_id, knowledge_id, context)
> --- `kb/processors/entity_extractor.py`

#### EPI-OBJ-wiki-article
Label: Rendered article text and source-document metadata

Part of: [RT-RTE-wiki-compile](runtime.md#rt-rte-wiki-compile)

Material output part of compilation, not a second compiler route. Source-native identity: rendered Markdown and `source_doc_ids`. Article text is natural language; source IDs, article ID and entity refs are symbolic. Substrates: Markdown file and SQLite wiki metadata. Truth-apt statements depend on unknown generated text. IDs derive from filtered documents, not from a statement-level evidence check; prompt truncation can omit content while retaining its document ID. Evidence: SRC-1 `kb/processors/wiki_compiler.py`; persistence/read-back passage in parent record.

> source_doc_ids = [doc.get("id") for doc in filtered_docs if doc.get("id")]
> --- `kb/processors/wiki_compiler.py`

> if current_tokens + doc_tokens > self.max_source_tokens:
>     break
> --- `kb/processors/wiki_compiler.py`

#### EPI-OBJ-chat-answer
Label: Answer text, saved turns and confidence metadata

Part of: [RT-RTE-chat-query](runtime.md#rt-rte-chat-query)

Material output part of enhanced chat. `answer` is natural language, saved in conversation SQLite where successful; `confidence` is symbolic numeric metadata returned in the result. They have separate consumers and checks. The source-domain truth of an actual answer is not determinable without content instances. The confidence formula consumes retrieval metadata, not answer claims. Evidence: SRC-1 `kb/query/retrieval_pipeline.py`; turn-retention passage and read-back in parent record.

> response = litellm.completion(**kwargs)
> answer = response.choices[0].message.content
> --- `kb/query/retrieval_pipeline.py`

#### EPI-OBJ-answer-confidence
Label: Retrieval-derived numeric confidence part

Part of: [EPI-OBJ-chat-answer](#epi-obj-chat-answer)

Source-native identity: `confidence` in the enhanced chat result. Representational form: symbolic floating-point metadata. Storage substrate: current result object and its process-local cache; not the natural-language answer/turn text. This is the material score part of the valid answer/result container, not a replacement for it or a duplicate of [EPI-RTE-confidence-metadata](#epi-rte-confidence-metadata), which owns production. Relative to [RT-RTE-chat-query](runtime.md#rt-rte-chat-query), it identifies one output part, not the orchestration. SRC-1 `kb/query/retrieval_pipeline.py` supplies implementation; the confidence route retains the formula and call passages.

Python produces the score from chunk scores, source count and stage labels after generation; no answer assertion is a formula input. Its check domain is bounded arithmetic, not factual fidelity or calibrated truth probability. Consumers are result construction, HTTP callers and later cache returns; channel is the numeric field, force advisory, horizon current result and cache lifetime. Successful turn storage/reuse of answer prose does not establish storage/reuse of this score as conversation text. No source-domain epistemic authority follows from sharing the container. User reliance, exercised cache reuse and calibration remain unobserved.

### Routes

#### EPI-RTE-structural-checks
Label: Candidate structural filtering and parse fallback

Distinct material cross-cutting check/disposition across [RT-RTE-file-admission](runtime.md#rt-rte-file-admission), [RT-RTE-mining-run](runtime.md#rt-rte-mining-run) and [RT-RTE-wiki-compile](runtime.md#rt-rte-wiki-compile), not a duplicate of their orchestration. SRC-1 `kb/processors/tag_extractor.py`, `kb/processors/entity_extractor.py`, `kb/processors/wiki_compiler.py` implement program evaluators before return/save. Check targets differ: tag strings/count/summary length; entity types and relation endpoints; wiki JSON parseability. Python filters, pads/truncates or substitutes fallback. The model proposes, software decides, caller may avoid the workflow or later edit; no per-result human veto, factual oracle or improvement curriculum is shown. This is operational format admission, not evidence-consuming source-domain acceptance. A false relation between allowed entity names is a countercase to treating endpoint checks as factual verification.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Cleaned metadata/entities/relations, failure/empty extraction, or fallback wiki structure.
- Later read-back: Admitted outputs can persist through the cited parent routes and reach retrieval, graph and wiki consumers.
- Delegated visibility: Model providers receive bounded source content before these local checks, not an independent verification request.
- Selection predicate: Allowed type vocabularies, normalized endpoint membership, nonempty/length/count criteria and parse branch.
- Invalidation or expiry: inapplicable — these checks dispose current responses; later revision/deletion follows separate routes.
- Activation or effect: Software controls surviving fields; factual compliance and later use unobserved.
- Evidence limits: No semantic comparator in the inspected methods; wiki parse failure can retain raw generated content rather than reject it. Other generation methods remain outside this bounded check account.

> if relation_type in self.RELATION_TYPES:
>     source_norm = self._normalize_name(str(r["source"]))
>     target_norm = self._normalize_name(str(r["target"]))
>     if source_norm in entity_names and target_norm in entity_names:
> --- `kb/processors/entity_extractor.py`

> if len(tags) < self.min_tags:
>     tags = self._pad_tags(tags, title)
> elif len(tags) > self.max_tags:
>     tags = tags[:self.max_tags]
> --- `kb/processors/tag_extractor.py`

> "title": "Untitled Article",
> "sections": [{"heading": "Content", "content": response_text[:2000]}],
> "entity_refs": [],
> "summary": "",
> --- `kb/processors/wiki_compiler.py`

#### EPI-RTE-extractive-summary
Label: Built-in sentence-selection summary

Part of: [RT-RTE-file-admission](runtime.md#rt-rte-file-admission)

This is a material deterministic transformation inside extraction, not the admission driver. `BuiltinExtractor.extract_summary` owns sentence splitting, filtering, position/title/length scoring, budget selection and original-order join. SRC-1 `kb/processors/builtin_extractor.py` supplies implementation. Concrete deduction: title `Rocks`, content `Rocks are solid. Water is liquid.`, budget 200. Both sentences exceed the ten-character minimum; both fit and neither reaches the 160-character early-stop threshold. Scores select both, original indices restore their order, and joining yields the original two statements. This is non-ampliative reshaping, not independent truth testing. If the best sentence exceeds the budget, a prefix may replace it; semantic preservation of that prefix is not established. Guidance is fixed scoring policy; no semantic approval or oracle; parent route supplies admission/recovery.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Selected/joined summary text, or a truncated prefix/title fallback.
- Later read-back: Summary can persist through the parent route and enter metadata, embedding and mining consumers.
- Delegated visibility: inapplicable — built-in extraction itself does not call a model.
- Selection predicate: Sentence eligibility, score order, character budget and original-order restoration.
- Invalidation or expiry: inapplicable — current-call transformation; stored summary changes via separate edits/re-extraction.
- Activation or effect: Summary text is computed by inspected rules; no target execution or downstream benefit observed.
- Evidence limits: The concrete complete-sentence case carries only source content; truncation and omission can remove necessary context.

> if current_length + len(sentence) + 1 <= max_length:
>     selected.append((idx, sentence))
>     current_length += len(sentence) + 1
> --- `kb/processors/builtin_extractor.py`

> selected.sort(key=lambda x: x[0])
> 
> return " ".join(s for _, s in selected).strip()
> --- `kb/processors/builtin_extractor.py`

#### EPI-RTE-confidence-metadata
Label: Retrieval-derived answer confidence metadata

Part of: [RT-RTE-chat-query](runtime.md#rt-rte-chat-query)

Material confidence-production part of chat, producing [EPI-OBJ-answer-confidence](#epi-obj-answer-confidence), not answer evaluation. Pipeline `_calculate_confidence` maps chunk scores, unique sources and stage labels to a bounded float. Owner/consumer: Python answer/result construction, then HTTP result consumer. Channel: numeric `confidence`; force: returned advisory metadata, not an answer rejection threshold; horizon: current result and any cached reuse. An arbitrary false answer with unchanged chunks/stages receives the same score as a true answer. Thus calibration as probability of answer truth is unestablished. SRC-1 `kb/query/retrieval_pipeline.py` is implementation evidence; parent record covers return, persistence and cache.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Float in [0,1], paired with generated answer; generation-error fallback returns 0.5.
- Later read-back: Cached result can return the same metadata later; score is not a retained corrective theory.
- Delegated visibility: inapplicable — confidence computation is local, not a provider judgment of answer correctness.
- Selection predicate: Top chunk scores, unique source count and fired-stage labels.
- Invalidation or expiry: Parent pipeline cache TTL/invalidation applies to cached results.
- Activation or effect: Value enters returned answer/result; no implemented score-based veto in the inspected answer branch.
- Evidence limits: Formula contains no answer text, source-claim comparison or known reference answer; user reliance and calibration unobserved.

> confidence = (
>     0.5 * avg_score +
>     0.3 * source_coverage +
>     0.2 * strategy_completeness
> )
> --- `kb/query/retrieval_pipeline.py`

> confidence = self._calculate_confidence(context.chunks, stages_fired)
> --- `kb/query/retrieval_pipeline.py`

#### EPI-RTE-numeric-selection
Label: Numeric relation admission and topic-centroid update

Part of: [RT-RTE-mining-run](runtime.md#rt-rte-mining-run)

Material algorithmic part of derived-state mining. SRC-1 `kb/processors/doc_relation_builder.py` computes cosine similarity over stored vectors and counts shared entity-mention rows, selects relations, and saves them to SQLite. SRC-1 `kb/processors/topic_clusterer.py` assigns a document to the nearest centroid above threshold after checking document existence, then updates membership and running-average centroid. These are separate target/domain/consumer paths, not factual evaluators of source assertions. Relation numeric results can reach graph/retrieval via the parent route; changed centroid reaches later classifier calls. Force is software-enforced threshold admission/update; horizon extends across later document classifications. Models produce embeddings upstream, application decides numeric admission, callers select mode/steps and can avoid/rebuild. No expected-answer oracle or objective-based improvement experiment is present. Full clustering uses HDBSCAN and resets derived tables, not semantic endorsement.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Similar-document/shared-entity tuples, saved relation counts or assigned cluster ID/None.
- Later read-back: SQLite relations support later graph consumers; topic memberships/centroids support later compilation and classification.
- Delegated visibility: Embedding services receive upstream title/summary text; numeric checks themselves are local.
- Selection predicate: Cosine threshold, shared-mention rows, nearest centroid and existing knowledge ID; full clustering excludes noise labels.
- Invalidation or expiry: Full relation rebuild clears relation rows; full topic clustering clears wiki metadata/categories/memberships/clusters before replacement. No general file deletion or coordinated rollback established.
- Activation or effect: Numeric decisions wire relation/membership writes and a changed centroid into subsequent selection capacity.
- Evidence limits: Semantic adequacy of embeddings/mentions and exercised benefit unobserved; HDBSCAN library internals not inspected. Derived numbers entail only represented-input facts, not warranted real-world relations.

> sim = _cosine_similarity(embedding, other_embedding)
> if sim >= self.similarity_threshold:
>     results.append((other_id, sim))
> --- `kb/processors/doc_relation_builder.py`

> HAVING shared_count >= 1
> ORDER BY shared_count DESC
> --- `kb/processors/doc_relation_builder.py`

> new_centroid = (
>     (best_centroid * best_doc_count + doc_vec) / (best_doc_count + 1)
> ).tolist()
> --- `kb/processors/topic_clusterer.py`

#### EPI-RTE-history-recommendation
Label: Reading-history-weighted recommendation selection

No same-route counterpart after comparison with [RT-RTE-chat-query](runtime.md#rt-rte-chat-query): that route records history/personalization but does not declare this recommendation endpoint or scoring route. `GET /recommendations` constructs `RecommendationEngine`, which reads recent history and embeddings, computes a time-decay weighted mean, ranks unread documents by cosine similarity plus topic bonus and returns titles/reasons/scores. Owners: endpoint and engine, not a model deciding subsequent tool calls. Evidence: SRC-1 `kb/web/routes/recommendations.py`, `kb/processors/recommendation.py`, `kb/web/routes/items.py`. A viewed item can create a history event; this trace later changes rank policy. It is a preference proxy, not truth-apt acceptance. Consumer: recommendation engine, then API caller; channel: history/embeddings to numeric rank and returned list; force: ranking, not enforced reading; horizon: later requests over persistent history. Caller chooses request/limit and can ignore recommendations. No correctness oracle or measured improvement objective; no product-machinery revision is claimed.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ranked document metadata/reasons/scores or fallback recommendations.
- Later read-back: Retained reading-history events enter later recommendation invocations.
- Delegated visibility: uninspected — reason-generation details not assessed; numeric profile/ranking path inspected locally.
- Selection predicate: Recent readable history, available embeddings, time decay, exclusion of recently read IDs, topic bonus and limit.
- Invalidation or expiry: Profile recomputed per call; time decay changes weights, not established deletion of history.
- Activation or effect: Recorded views can shape later ranking without a factual claim check; actual exercised recommendations/benefit unobserved.
- Evidence limits: Reason text generation and actual caller response unassessed; this does not establish better future action or exercised self-improvement.

> user_profile = weighted_sum / weight_total
> --- `kb/processors/recommendation.py`

> if doc_topic and doc_topic in doc_topics:
>     similarity += self.topic_bonus
> --- `kb/processors/recommendation.py`

> candidates.sort(key=lambda x: x[1], reverse=True)
> top_candidates = candidates[:limit]
> --- `kb/processors/recommendation.py`

#### EPI-RTE-item-withdrawal
Label: Item deletion and title-based duplicate cleanup

Distinct from supplied [RT-RTE-item-update](runtime.md#rt-rte-item-update): deletion/cleanup is not metadata editing. SRC-1 `kb/web/routes/items.py` deletes an exact requested item via SQLite, then best-effort vector/file deletion. SRC-1 `tests/cleanup_duplicate_webpages.py` is a shipped runnable maintenance driver, not excluded as a test: it lists up to 1000 webpage rows, groups by title, keeps first and deletes remaining through SQLite. This valid container retains both dispositions; the separately citable cleanup part is [EPI-RTE-title-cleanup](#epi-rte-title-cleanup). Its HTTP branch overlaps [MEM-RTE-item-withdrawal](memory.md#mem-rte-item-withdrawal), which isolates exact-ID HTTP withdrawal; that peer record does not contain the cleanup driver. These dispositions have separate predicates/consumers. HTTP caller proposes deletion, handler decides existence; duplicate script chooses by equal title without per-group approval. No factual comparator/oracle or refutation criterion; title equality does not establish identical content. Guidance is explicit deletion request or fixed deduplication rule. No coordinated rollback; backups are separate recovery.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: HTTP deletion message/error or script deletion counts/statistics.
- Later read-back: Later SQLite consumers see surviving rows; files, vectors, prior answers and wiki text need not be withdrawn together.
- Delegated visibility: inapplicable — local storage/file operations, not model delegation.
- Selection predicate: Existing item ID for HTTP; repeated exact title within listed webpage rows for cleanup.
- Invalidation or expiry: HTTP vector/file failures are swallowed; file deletion defaults false; inspected handler has no pipeline cache invalidation. Script calls SQLite deletion only.
- Activation or effect: SQLite removal is operative; broader store/claim withdrawal and successful cleanup unobserved.
- Evidence limits: Equal titles can contain different propositions; a success response does not prove all representations disappeared. Schema cascades beyond inspected deletion helper not fully assessed.

> if storage.delete_knowledge(item['id']):
>     deleted_count += 1
> --- `tests/cleanup_duplicate_webpages.py`

> if chunk_ids:
>     try:
>         chroma = get_chroma_storage()
>         chroma.delete(ids=chunk_ids)
>     except Exception as e:
>         # Log but don't fail - SQLite deletion was successful
>         pass
> --- `kb/web/routes/items.py`

#### EPI-RTE-title-cleanup
Label: Exact-title webpage duplicate cleanup

Part of: [EPI-RTE-item-withdrawal](#epi-rte-item-withdrawal)

Endpoints/progression: direct script invocation → `cleanup_duplicates` → SQLite webpage listing limited to 1000 rows → exact-title grouping → retain first listed row per group → delete remaining IDs through `SQLiteStorage.delete_knowledge` → counts and another limited listing. Owner: maintenance script under caller's OS principal. Context/state/effects: listed metadata, title groups and IDs; SQLite row deletion with linked chunks/tag associations and tag-count cleanup. SRC-1 `tests/cleanup_duplicate_webpages.py`, `kb/storage/sqlite_storage.py` supply implementation. Unlike [MEM-RTE-item-withdrawal](memory.md#mem-rte-item-withdrawal), this part neither invokes Chroma deletion nor optional file removal. It is a part of the supplied epistemic container, not a replacement for its HTTP branch or the memory HTTP record.

The caller triggers or withholds script execution; software proposes and decides which rows to delete from title equality and list order, with no per-group human approval. Human identity is unresolved. The target/domain is duplicate titles within the limited listing, not identical source content, truth or refutation. An equal title on different content is a countercase to semantic equivalence. Fixed script policy supplies guidance; no model or expected-answer oracle is involved. Operating mode is maintenance, not an improvement experiment. The deletion helper reports failure on exceptions; there is no coordinated rollback or backup adoption in this script. Surviving rows persist; independently retained files, vectors, wiki prose, history and caches are not demonstrated retracted.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Printed repeated-title groups, deletion count and limited remaining-row count, or no-duplicates message.
- Later read-back: Later SQLite queries see surviving knowledge rows and associated state; other substrates are not purged by this caller.
- Delegated visibility: inapplicable — the script calls local SQLite, not a model or delegated worker.
- Selection predicate: Exact title equality among at most 1000 webpage rows; keep first listed row, delete subsequent rows in each group.
- Invalidation or expiry: SQLite helper deletes linked chunks/tag associations and updates tag counts; script has no vector/file deletion or pipeline-cache invalidation.
- Activation or effect: Software-enforced SQLite disposition changes availability to later SQLite consumers; no factual acceptance or universal claim withdrawal follows.
- Evidence limits: Source-only trace; listing is bounded, content is not compared, and actual deletions, downstream retraction and successful recovery are unobserved.

Consumer: SQLite deletion helper and later SQLite readers. Channel: selected knowledge IDs into deletion. Force: enforcing row disposition, not advisory semantic criticism. Horizon: subsequent reads until separate recollection/restoration. This effect boundary is narrower than the HTTP branch's attempted vector/optional-file cleanup.

> items = storage.list_knowledge(content_type="webpage", limit=1000)
> --- `tests/cleanup_duplicate_webpages.py`

> title_groups = {}
> for item in items:
>     title = item['title']
>     if title not in title_groups:
>         title_groups[title] = []
>     title_groups[title].append(item)
> --- `tests/cleanup_duplicate_webpages.py`

> cursor.execute("DELETE FROM knowledge WHERE id = ?", (id,))
> --- `kb/storage/sqlite_storage.py:540-571`

The parent retains the exact deletion-call witness. The first-row branch in the inspected script supplies retention order; title grouping establishes only title equality.

#### EPI-RTE-category-recompilation
Label: Category document-set recompilation eligibility

Part of: [RT-RTE-wiki-compile](runtime.md#rt-rte-wiki-compile)

Material selection part of compilation. `_get_categories_needing_compilation` compares current and previously compiled document-ID sets, or returns all categories on force. `_is_stale` only tests whether an article row exists. Python owns eligibility before synthesis. Target: source membership/absence, not source-content truth or endorsement. Consumer: compiler selection; channel: eligible category list; force: software selection of compilation work; horizon: next maintenance invocation. SRC-1 `kb/processors/wiki_compiler.py` supplies implementation. Same IDs with changed source text falsify the stronger claim that this predicate detects arbitrary source-document changes. Caller may force recompile; no factual oracle or per-article approval; synthesis/write/recovery remain in the parent route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Categories selected for recompilation.
- Later read-back: Prior article `source_doc_ids` are loaded from SQLite on later compilation runs.
- Delegated visibility: inapplicable — this eligibility check is local; later synthesis sends selected source text through parent route.
- Selection predicate: Force, missing compiled IDs or unequal current/compiled ID sets.
- Invalidation or expiry: Same-ID source text changes do not alter this predicate; force bypasses it.
- Activation or effect: Changed ID sets can select new synthesis; factual correction and actual recompilation unobserved.
- Evidence limits: No source-text hash/version comparison in inspected eligibility methods; other source edits/writers not fully enumerated.

> elif current_doc_ids != compiled_doc_ids:
>     # Doc IDs have changed (new docs added or removed)
>     categories_needing_compilation.append(category)
> --- `kb/processors/wiki_compiler.py`

### Claims

#### EPI-CLM-wiki-synthesis
Label: Coherent wiki reference articles from collected documents

Distinct from [RT-CLM-context-answer](runtime.md#rt-clm-context-answer): this concerns durable wiki products, not RAG answers. Claimed operation: LLM synthesis of collected topic documents into coherent reference articles. SRC-1 `README.md` supplies doctrine/design; [RT-RTE-wiki-compile](runtime.md#rt-rte-wiki-compile) supplies implemented generation/persistence/browsing, not observed coherence or warranted factual synthesis.

> - **Topic Articles** — LLM synthesizes documents from topic clusters into coherent reference articles
> --- `README.md`

#### EPI-CLM-staleness-tracking
Label: Detect changed wiki source documents for recompilation

Distinct from [RT-CLM-context-answer](runtime.md#rt-clm-context-answer), with no same claim declared in supplied runtime. Claimed operation: source-document change detection and article flagging. SRC-1 `README.md` supplies doctrine/design. [EPI-RTE-category-recompilation](#epi-rte-category-recompilation) supports source-ID-set comparison, not general same-ID content-change detection; that mismatch limits claims of currentness, not article generation capacity.

> - **Staleness Tracking** — Automatically detects when source documents change and flags articles for recompilation
> --- `README.md`
