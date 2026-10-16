---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Beever Atlas: what extraction, cleanup, contradiction checks, wiki maintenance and QA license for later reliance."
run-id: AAS-2026-10-15-beever-atlas-10a3512c094c-01
reviewed-boundary: "7d791af27ef4aa19644cb385c7ca24619bc4f848"
---

# Beever Atlas epistemic report

## Source-and-claim boundary

The question is which routes turn conversation-derived candidates into material relied on by later wiki and QA consumers, and what the checks license. Scope and exclusions are those of [the boundary](boundary.md#boundary-and-evidence); evidence identities and layers are in its [Source register](boundary.md#source-register). SRC-1 is the sole source. All added code findings below are implementation evidence; prompt/doc assertions are doctrine/design. None is an observed run or causal experiment. No target code was executed.

Runtime is provisional. Direct source inspection found a consequential post-sync contradiction/supersession route beyond its account, a narration rewrite that can remove attribution, a structural-only implemented lint route despite LLM-coherence wording, and a no-op default entity LLM-fallback hook. These extend or qualify the account rather than replacing its valid pipeline container. They prevent describing Atlas merely as unchecked storage, but do not establish semantic truth or verified improvement.

| Entry point or operation | Source path (SRC-1) | Coverage and records, or limit |
|---|---|---|
| Backend launch, HTTP/bot/dashboard QA, push/sync | `src/beever_atlas/server/app.py`, `src/beever_atlas/api/ask.py`, `src/beever_atlas/api/sources.py` | Supplied runtime findings for ordinary invocation; direct app read for contradiction subscriber. See [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask), [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion). |
| Frozen CLI, MCP dispatch, catalog hooks | `src/beever_atlas/api/mcp_server/__main__.py`, `src/beever_atlas/api/mcp_server/__init__.py`, `pyproject.toml` | Direct reads/search: CLI constructs the same catalog without stores; build registers discovery, retrieval, graph, session, orchestration, resources and prompts, then audit/rate wrappers. Supplied [RT-RTE-mcp-ask](runtime.md#rt-rte-mcp-ask) covers alternate answer runner. Resource/prompt bodies and all graph tool internals remain uninspected here: no exhaustive claim about every exposed operation. |
| Extraction, callback admission, narration, entity dedup | `src/beever_atlas/agents/ingestion/pipeline.py`, `src/beever_atlas/agents/callbacks/quality_gates.py`, `src/beever_atlas/agents/ingestion/narration_filter.py`, `src/beever_atlas/services/entity_dedup.py`, `src/beever_atlas/agents/ingestion/cross_batch_validator.py` | Direct reads. See new extraction-part records below; persister and model constructors additionally supported by runtime. |
| Temporal contradiction and withdrawal | `src/beever_atlas/services/contradiction_detector.py`, `src/beever_atlas/agents/ingestion/contradiction_detector.py`, `src/beever_atlas/agents/prompts/contradiction_detector.py`, `src/beever_atlas/stores/weaviate_store.py`, `src/beever_atlas/services/consolidation.py` | Direct reads/search of selector, evaluator, disposition, state mutation, read filters and cluster-context consumer. See contradiction records. Full consolidation generation/enrichment not audited. |
| Fact-tool retrieval fallback | `src/beever_atlas/agents/tools/memory_tools.py`, `src/beever_atlas/stores/weaviate_store.py` | Direct reads of semantic/native-hybrid filters, BM25 return, and `search_channel_facts` through candidate formatting/MMR. BM25 fallback can return invalidated facts without an explicit superseded-content request; see [EPI-RTE-fact-supersession](#epi-rte-fact-supersession). |
| Incremental and full wiki generation | `src/beever_atlas/services/wiki_maintainer.py`, `src/beever_atlas/wiki/builder.py`, `src/beever_atlas/wiki/compiler.py` | Runtime covers incremental route; direct drift scheduling and selected compiler retry/cache-save branches. Full compiler module variants, folder planning and data gatherer not fully inspected; prevents universal synthesis/check claims. |
| Lint and drift | `src/beever_atlas/services/wiki_lint.py`, `src/beever_atlas/services/wiki_drift_comparator.py`, `src/beever_atlas/api/wiki.py`, `src/beever_atlas/api/mcp_server/_tools_retrieval.py` | Full service reads, direct HTTP handler read, MCP registration/consumer searches. See lint/drift records. |
| Curation, versioning, refresh | `src/beever_atlas/api/wiki.py` | Runtime curation findings plus direct searches of refresh/snapshot/version routes; complete deletion/restore behavior uninspected. No universal rollback or curation invariant over all writers. |
| Citation annotations | `src/beever_atlas/agents/tools/_citation_decorator.py` | Direct wrapper/annotation read; see citation route. Downstream citation finalization not fully inspected. |
| External capability/model changes | `src/beever_atlas/agents/mcp_registry.py`, `src/beever_atlas/api/assignments.py` | Supplied [RT-RTE-outbound-tools](runtime.md#rt-rte-outbound-tools), [RT-RTE-model-assignment](runtime.md#rt-rte-model-assignment); remote content/parameter internals opaque. |
| QA test and compiler benchmark | `scripts/qa_test_harness.py`, `scripts/wiki_bench.py`, `tests/integration/test_sim_memory_then_wiki.py` | Direct QA grade read and benchmark function searches; simulation only supplied boundary excerpt. No run results supplied. Test-wide correctness or causal effects not assessed. |
| Other import/batch/media, merge rejection administration, migrations, demo, web/bot, CI and maintenance scripts | `src/beever_atlas/services/file_importer.py`, `src/beever_atlas/services/batch_pipeline.py`, `src/beever_atlas/services/media_processor.py`, `scripts/`, `demo/`, `web/`, `bot/`, `.github/` | Included by boundary; not fully inspected in this job. Supplied consumer findings remain usable; these omissions prevent system-complete negative conclusions about truth checks, acceptance, or adaptation. |

Missing evidence is conclusion-specific: no deployment trace means no demonstrated activation or acceptance instance; no authenticated source corpus plus checked source-to-output trace means no established extraction fidelity; no actual provider identity/parameters means no weight-learning finding; no controlled outcome comparison means no attribution of answer consistency, hallucination reduction or latency benefit. These are unavailable observations, not source access gaps. Public knowledge/warrant claims are declared below; relevant supplied control/recovery claims remain in runtime.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-extracted-facts](#epi-obj-extracted-facts) | see [EPI-OBJ-extracted-facts](#epi-obj-extracted-facts) | see [EPI-OBJ-extracted-facts](#epi-obj-extracted-facts) | SRC-1: `src/beever_atlas/agents/callbacks/quality_gates.py` | see [EPI-OBJ-extracted-facts](#epi-obj-extracted-facts) |
| [EPI-OBJ-extracted-entities](#epi-obj-extracted-entities) | see [EPI-OBJ-extracted-entities](#epi-obj-extracted-entities) | see [EPI-OBJ-extracted-entities](#epi-obj-extracted-entities) | SRC-1: `src/beever_atlas/agents/ingestion/cross_batch_validator.py` | see [EPI-OBJ-extracted-entities](#epi-obj-extracted-entities) |
| [EPI-OBJ-wiki-content](#epi-obj-wiki-content) | see [EPI-OBJ-wiki-content](#epi-obj-wiki-content) | see [EPI-OBJ-wiki-content](#epi-obj-wiki-content) | SRC-1: `src/beever_atlas/wiki/builder.py` | see [EPI-OBJ-wiki-content](#epi-obj-wiki-content) |
| [EPI-OBJ-contradiction-report](#epi-obj-contradiction-report) | see [EPI-OBJ-contradiction-report](#epi-obj-contradiction-report) | see [EPI-OBJ-contradiction-report](#epi-obj-contradiction-report) | SRC-1: `src/beever_atlas/services/contradiction_detector.py` | see [EPI-OBJ-contradiction-report](#epi-obj-contradiction-report) |
| [EPI-OBJ-lint-report](#epi-obj-lint-report) | see [EPI-OBJ-lint-report](#epi-obj-lint-report) | see [EPI-OBJ-lint-report](#epi-obj-lint-report) | SRC-1: `src/beever_atlas/services/wiki_lint.py` | see [EPI-OBJ-lint-report](#epi-obj-lint-report) |

Additional operative parts:

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-qa-answer](#epi-obj-qa-answer) | see [EPI-OBJ-qa-answer](#epi-obj-qa-answer) | see [EPI-OBJ-qa-answer](#epi-obj-qa-answer) | SRC-1: `src/beever_atlas/api/ask.py` | see [EPI-OBJ-qa-answer](#epi-obj-qa-answer) |
| [EPI-OBJ-drift-report](#epi-obj-drift-report) | see [EPI-OBJ-drift-report](#epi-obj-drift-report) | see [EPI-OBJ-drift-report](#epi-obj-drift-report) | SRC-1: `src/beever_atlas/services/wiki_drift_comparator.py` | see [EPI-OBJ-drift-report](#epi-obj-drift-report) |

Provider parameter state is separately covered by [RT-CMP-fact-extractor](runtime.md#rt-cmp-fact-extractor), [RT-CMP-entity-extractor](runtime.md#rt-cmp-entity-extractor), [RT-CMP-wiki-maintainer](runtime.md#rt-cmp-wiki-maintainer), [RT-CMP-qa-agent](runtime.md#rt-cmp-qa-agent) and [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model). The additional contradiction model is declared below. Numerical vectors support similarity, not individuated warranted propositions about the team. Provider-internal truth-apt content and parameter updates are not determinable from this boundary.

## Authority-route ledger

Each `see` delegates the declaring record's fields; architectural status is this overlay's judgment. Functions are split even when their implementation shares a container. No observed candidate state is inferred from source alone.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-RTE-narration-rewrite](#epi-rte-narration-rewrite) | content transformation | implemented | see [EPI-RTE-narration-rewrite](#epi-rte-narration-rewrite) | see [EPI-RTE-narration-rewrite](#epi-rte-narration-rewrite) | see [EPI-RTE-narration-rewrite](#epi-rte-narration-rewrite) | see [EPI-RTE-narration-rewrite](#epi-rte-narration-rewrite) | see [EPI-RTE-narration-rewrite](#epi-rte-narration-rewrite) | see [EPI-RTE-narration-rewrite](#epi-rte-narration-rewrite) | see [EPI-RTE-narration-rewrite](#epi-rte-narration-rewrite) | see [EPI-RTE-narration-rewrite](#epi-rte-narration-rewrite) | see [EPI-RTE-narration-rewrite](#epi-rte-narration-rewrite) | see [EPI-RTE-narration-rewrite](#epi-rte-narration-rewrite) | SRC-1: `src/beever_atlas/agents/ingestion/narration_filter.py` | see [EPI-CLM-knowledge-quality](#epi-clm-knowledge-quality) | none | see [EPI-RTE-narration-rewrite](#epi-rte-narration-rewrite) |
| [EPI-RTE-quality-check](#epi-rte-quality-check) | check/evidence production | implemented | see [EPI-RTE-quality-check](#epi-rte-quality-check) | see [EPI-RTE-quality-check](#epi-rte-quality-check) | see [EPI-RTE-quality-check](#epi-rte-quality-check) | see [EPI-RTE-quality-check](#epi-rte-quality-check) | see [EPI-RTE-quality-check](#epi-rte-quality-check) | see [EPI-RTE-quality-check](#epi-rte-quality-check) | see [EPI-RTE-quality-check](#epi-rte-quality-check) | see [EPI-RTE-quality-check](#epi-rte-quality-check) | see [EPI-RTE-quality-check](#epi-rte-quality-check) | see [EPI-RTE-quality-check](#epi-rte-quality-check) | SRC-1: `src/beever_atlas/agents/callbacks/quality_gates.py` | see [EPI-CLM-knowledge-quality](#epi-clm-knowledge-quality) | none | see [EPI-RTE-quality-check](#epi-rte-quality-check) |
| [EPI-RTE-quality-admission](#epi-rte-quality-admission) | disposition/acceptance | implemented | see [EPI-RTE-quality-admission](#epi-rte-quality-admission) | see [EPI-RTE-quality-admission](#epi-rte-quality-admission) | see [EPI-RTE-quality-admission](#epi-rte-quality-admission) | see [EPI-RTE-quality-admission](#epi-rte-quality-admission) | see [EPI-RTE-quality-admission](#epi-rte-quality-admission) | see [EPI-RTE-quality-admission](#epi-rte-quality-admission) | see [EPI-RTE-quality-admission](#epi-rte-quality-admission) | see [EPI-RTE-quality-admission](#epi-rte-quality-admission) | see [EPI-RTE-quality-admission](#epi-rte-quality-admission) | see [EPI-RTE-quality-admission](#epi-rte-quality-admission) | SRC-1: `src/beever_atlas/agents/callbacks/quality_gates.py` | see [EPI-CLM-knowledge-quality](#epi-clm-knowledge-quality) | none | see [EPI-RTE-quality-admission](#epi-rte-quality-admission) |
| [EPI-RTE-entity-dedup](#epi-rte-entity-dedup) | content transformation | implemented | see [EPI-RTE-entity-dedup](#epi-rte-entity-dedup) | see [EPI-RTE-entity-dedup](#epi-rte-entity-dedup) | see [EPI-RTE-entity-dedup](#epi-rte-entity-dedup) | see [EPI-RTE-entity-dedup](#epi-rte-entity-dedup) | see [EPI-RTE-entity-dedup](#epi-rte-entity-dedup) | see [EPI-RTE-entity-dedup](#epi-rte-entity-dedup) | see [EPI-RTE-entity-dedup](#epi-rte-entity-dedup) | see [EPI-RTE-entity-dedup](#epi-rte-entity-dedup) | see [EPI-RTE-entity-dedup](#epi-rte-entity-dedup) | see [EPI-RTE-entity-dedup](#epi-rte-entity-dedup) | SRC-1: `src/beever_atlas/services/entity_dedup.py` | see [EPI-CLM-knowledge-quality](#epi-clm-knowledge-quality) | none | see [EPI-RTE-entity-dedup](#epi-rte-entity-dedup) |
| [EPI-RTE-contradiction-check](#epi-rte-contradiction-check) | check/evidence production | implemented | see [EPI-RTE-contradiction-check](#epi-rte-contradiction-check) | see [EPI-RTE-contradiction-check](#epi-rte-contradiction-check) | see [EPI-RTE-contradiction-check](#epi-rte-contradiction-check) | see [EPI-RTE-contradiction-check](#epi-rte-contradiction-check) | see [EPI-RTE-contradiction-check](#epi-rte-contradiction-check) | see [EPI-RTE-contradiction-check](#epi-rte-contradiction-check) | see [EPI-RTE-contradiction-check](#epi-rte-contradiction-check) | see [EPI-RTE-contradiction-check](#epi-rte-contradiction-check) | see [EPI-RTE-contradiction-check](#epi-rte-contradiction-check) | see [EPI-RTE-contradiction-check](#epi-rte-contradiction-check) | SRC-1: `src/beever_atlas/services/contradiction_detector.py` | see [EPI-CLM-knowledge-quality](#epi-clm-knowledge-quality) | none | see [EPI-RTE-contradiction-check](#epi-rte-contradiction-check) |
| [EPI-RTE-fact-supersession](#epi-rte-fact-supersession) | disposition/acceptance | implemented | see [EPI-RTE-fact-supersession](#epi-rte-fact-supersession) | see [EPI-RTE-fact-supersession](#epi-rte-fact-supersession) | see [EPI-RTE-fact-supersession](#epi-rte-fact-supersession) | see [EPI-RTE-fact-supersession](#epi-rte-fact-supersession) | see [EPI-RTE-fact-supersession](#epi-rte-fact-supersession) | see [EPI-RTE-fact-supersession](#epi-rte-fact-supersession) | see [EPI-RTE-fact-supersession](#epi-rte-fact-supersession) | see [EPI-RTE-fact-supersession](#epi-rte-fact-supersession) | see [EPI-RTE-fact-supersession](#epi-rte-fact-supersession) | see [EPI-RTE-fact-supersession](#epi-rte-fact-supersession) | SRC-1: `src/beever_atlas/services/contradiction_detector.py` | see [EPI-CLM-knowledge-quality](#epi-clm-knowledge-quality) | none | see [EPI-RTE-fact-supersession](#epi-rte-fact-supersession) |
| [EPI-RTE-wiki-lint](#epi-rte-wiki-lint) | check/evidence production | implemented | see [EPI-RTE-wiki-lint](#epi-rte-wiki-lint) | see [EPI-RTE-wiki-lint](#epi-rte-wiki-lint) | see [EPI-RTE-wiki-lint](#epi-rte-wiki-lint) | see [EPI-RTE-wiki-lint](#epi-rte-wiki-lint) | see [EPI-RTE-wiki-lint](#epi-rte-wiki-lint) | see [EPI-RTE-wiki-lint](#epi-rte-wiki-lint) | see [EPI-RTE-wiki-lint](#epi-rte-wiki-lint) | see [EPI-RTE-wiki-lint](#epi-rte-wiki-lint) | see [EPI-RTE-wiki-lint](#epi-rte-wiki-lint) | see [EPI-RTE-wiki-lint](#epi-rte-wiki-lint) | SRC-1: `src/beever_atlas/services/wiki_lint.py` | see [EPI-CLM-knowledge-quality](#epi-clm-knowledge-quality) | none | see [EPI-RTE-wiki-lint](#epi-rte-wiki-lint) |
| [EPI-RTE-drift-comparison](#epi-rte-drift-comparison) | check/evidence production | implemented | see [EPI-RTE-drift-comparison](#epi-rte-drift-comparison) | see [EPI-RTE-drift-comparison](#epi-rte-drift-comparison) | see [EPI-RTE-drift-comparison](#epi-rte-drift-comparison) | see [EPI-RTE-drift-comparison](#epi-rte-drift-comparison) | see [EPI-RTE-drift-comparison](#epi-rte-drift-comparison) | see [EPI-RTE-drift-comparison](#epi-rte-drift-comparison) | see [EPI-RTE-drift-comparison](#epi-rte-drift-comparison) | see [EPI-RTE-drift-comparison](#epi-rte-drift-comparison) | see [EPI-RTE-drift-comparison](#epi-rte-drift-comparison) | see [EPI-RTE-drift-comparison](#epi-rte-drift-comparison) | SRC-1: `src/beever_atlas/services/wiki_drift_comparator.py` | see [EPI-CLM-knowledge-quality](#epi-clm-knowledge-quality) | none | see [EPI-RTE-drift-comparison](#epi-rte-drift-comparison) |
| [EPI-RTE-citation-annotation](#epi-rte-citation-annotation) | lineage/freshness/recovery | implemented | see [EPI-RTE-citation-annotation](#epi-rte-citation-annotation) | see [EPI-RTE-citation-annotation](#epi-rte-citation-annotation) | see [EPI-RTE-citation-annotation](#epi-rte-citation-annotation) | see [EPI-RTE-citation-annotation](#epi-rte-citation-annotation) | see [EPI-RTE-citation-annotation](#epi-rte-citation-annotation) | see [EPI-RTE-citation-annotation](#epi-rte-citation-annotation) | see [EPI-RTE-citation-annotation](#epi-rte-citation-annotation) | see [EPI-RTE-citation-annotation](#epi-rte-citation-annotation) | see [EPI-RTE-citation-annotation](#epi-rte-citation-annotation) | see [EPI-RTE-citation-annotation](#epi-rte-citation-annotation) | SRC-1: `src/beever_atlas/agents/tools/_citation_decorator.py` | see [EPI-CLM-traceable-citations](#epi-clm-traceable-citations) | none | see [EPI-RTE-citation-annotation](#epi-rte-citation-annotation) |
| [EPI-RTE-compiler-retry](#epi-rte-compiler-retry) | check/evidence production | implemented | see [EPI-RTE-compiler-retry](#epi-rte-compiler-retry) | see [EPI-RTE-compiler-retry](#epi-rte-compiler-retry) | see [EPI-RTE-compiler-retry](#epi-rte-compiler-retry) | see [EPI-RTE-compiler-retry](#epi-rte-compiler-retry) | see [EPI-RTE-compiler-retry](#epi-rte-compiler-retry) | see [EPI-RTE-compiler-retry](#epi-rte-compiler-retry) | see [EPI-RTE-compiler-retry](#epi-rte-compiler-retry) | see [EPI-RTE-compiler-retry](#epi-rte-compiler-retry) | see [EPI-RTE-compiler-retry](#epi-rte-compiler-retry) | see [EPI-RTE-compiler-retry](#epi-rte-compiler-retry) | SRC-1: `src/beever_atlas/wiki/compiler.py` | see [EPI-CLM-knowledge-quality](#epi-clm-knowledge-quality) | none | see [EPI-RTE-compiler-retry](#epi-rte-compiler-retry) |
| [EPI-RTE-builder-retention](#epi-rte-builder-retention) | retention | implemented | see [EPI-RTE-builder-retention](#epi-rte-builder-retention) | see [EPI-RTE-builder-retention](#epi-rte-builder-retention) | see [EPI-RTE-builder-retention](#epi-rte-builder-retention) | see [EPI-RTE-builder-retention](#epi-rte-builder-retention) | see [EPI-RTE-builder-retention](#epi-rte-builder-retention) | see [EPI-RTE-builder-retention](#epi-rte-builder-retention) | see [EPI-RTE-builder-retention](#epi-rte-builder-retention) | see [EPI-RTE-builder-retention](#epi-rte-builder-retention) | see [EPI-RTE-builder-retention](#epi-rte-builder-retention) | see [EPI-RTE-builder-retention](#epi-rte-builder-retention) | SRC-1: `src/beever_atlas/wiki/builder.py` | see [EPI-CLM-knowledge-quality](#epi-clm-knowledge-quality) | none | see [EPI-RTE-builder-retention](#epi-rte-builder-retention) |
| [EPI-RTE-qa-grading](#epi-rte-qa-grading) | check/evidence production | implemented | see [EPI-RTE-qa-grading](#epi-rte-qa-grading) | see [EPI-RTE-qa-grading](#epi-rte-qa-grading) | see [EPI-RTE-qa-grading](#epi-rte-qa-grading) | see [EPI-RTE-qa-grading](#epi-rte-qa-grading) | see [EPI-RTE-qa-grading](#epi-rte-qa-grading) | see [EPI-RTE-qa-grading](#epi-rte-qa-grading) | see [EPI-RTE-qa-grading](#epi-rte-qa-grading) | see [EPI-RTE-qa-grading](#epi-rte-qa-grading) | see [EPI-RTE-qa-grading](#epi-rte-qa-grading) | see [EPI-RTE-qa-grading](#epi-rte-qa-grading) | SRC-1: `scripts/qa_test_harness.py` | none | none | see [EPI-RTE-qa-grading](#epi-rte-qa-grading) |
| [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | content transformation | implemented | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | SRC-1: `src/beever_atlas/agents/ingestion/pipeline.py` | none | none | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) |
| [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | retention | implemented | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) | SRC-1: `src/beever_atlas/agents/ingestion/persister.py` | see [RT-CLM-write-completion](runtime.md#rt-clm-write-completion) | none | see [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) |
| [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | content transformation | implemented | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | SRC-1: `src/beever_atlas/services/wiki_maintainer.py` | see [EPI-CLM-knowledge-quality](#epi-clm-knowledge-quality) | none | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) |
| [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | disposition/acceptance | implemented | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | SRC-1: `src/beever_atlas/services/wiki_maintainer.py` | none | none | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) |
| [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | retention | implemented | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) | SRC-1: `src/beever_atlas/services/wiki_maintainer.py` | none | none | see [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) |
| [RT-RTE-page-curation](runtime.md#rt-rte-page-curation) | operational admission/selection/consumption | implemented | see [RT-RTE-page-curation](runtime.md#rt-rte-page-curation) | see [RT-RTE-page-curation](runtime.md#rt-rte-page-curation) | see [RT-RTE-page-curation](runtime.md#rt-rte-page-curation) | see [RT-RTE-page-curation](runtime.md#rt-rte-page-curation) | see [RT-RTE-page-curation](runtime.md#rt-rte-page-curation) | see [RT-RTE-page-curation](runtime.md#rt-rte-page-curation) | see [RT-RTE-page-curation](runtime.md#rt-rte-page-curation) | see [RT-RTE-page-curation](runtime.md#rt-rte-page-curation) | see [RT-RTE-page-curation](runtime.md#rt-rte-page-curation) | see [RT-RTE-page-curation](runtime.md#rt-rte-page-curation) | SRC-1: `src/beever_atlas/api/wiki.py` | none | none | see [RT-RTE-page-curation](runtime.md#rt-rte-page-curation) |
| [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | operational admission/selection/consumption | implemented | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | SRC-1: `src/beever_atlas/api/ask.py` | see [RT-CLM-channel-isolation](runtime.md#rt-clm-channel-isolation) | none | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) |
| [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | content transformation | implemented | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) | SRC-1: `src/beever_atlas/agents/query/qa_agent.py` | see [EPI-CLM-knowledge-quality](#epi-clm-knowledge-quality) | none | see [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) |
| [RT-RTE-mcp-ask](runtime.md#rt-rte-mcp-ask) | content transformation | implemented | see [RT-RTE-mcp-ask](runtime.md#rt-rte-mcp-ask) | see [RT-RTE-mcp-ask](runtime.md#rt-rte-mcp-ask) | see [RT-RTE-mcp-ask](runtime.md#rt-rte-mcp-ask) | see [RT-RTE-mcp-ask](runtime.md#rt-rte-mcp-ask) | see [RT-RTE-mcp-ask](runtime.md#rt-rte-mcp-ask) | see [RT-RTE-mcp-ask](runtime.md#rt-rte-mcp-ask) | see [RT-RTE-mcp-ask](runtime.md#rt-rte-mcp-ask) | see [RT-RTE-mcp-ask](runtime.md#rt-rte-mcp-ask) | see [RT-RTE-mcp-ask](runtime.md#rt-rte-mcp-ask) | see [RT-RTE-mcp-ask](runtime.md#rt-rte-mcp-ask) | SRC-1: `src/beever_atlas/api/mcp_server/_ask_runner.py` | none | none | see [RT-RTE-mcp-ask](runtime.md#rt-rte-mcp-ask) |
| [RT-RTE-outbound-tools](runtime.md#rt-rte-outbound-tools) | operational admission/selection/consumption | implemented | see [RT-RTE-outbound-tools](runtime.md#rt-rte-outbound-tools) | see [RT-RTE-outbound-tools](runtime.md#rt-rte-outbound-tools) | see [RT-RTE-outbound-tools](runtime.md#rt-rte-outbound-tools) | see [RT-RTE-outbound-tools](runtime.md#rt-rte-outbound-tools) | see [RT-RTE-outbound-tools](runtime.md#rt-rte-outbound-tools) | see [RT-RTE-outbound-tools](runtime.md#rt-rte-outbound-tools) | see [RT-RTE-outbound-tools](runtime.md#rt-rte-outbound-tools) | see [RT-RTE-outbound-tools](runtime.md#rt-rte-outbound-tools) | see [RT-RTE-outbound-tools](runtime.md#rt-rte-outbound-tools) | see [RT-RTE-outbound-tools](runtime.md#rt-rte-outbound-tools) | SRC-1: `src/beever_atlas/agents/mcp_registry.py` | see [RT-CLM-untrusted-tools](runtime.md#rt-clm-untrusted-tools) | none | see [RT-RTE-outbound-tools](runtime.md#rt-rte-outbound-tools) |
| [RT-RTE-model-assignment](runtime.md#rt-rte-model-assignment) | behavior/policy adaptation | implemented | see [RT-RTE-model-assignment](runtime.md#rt-rte-model-assignment) | see [RT-RTE-model-assignment](runtime.md#rt-rte-model-assignment) | see [RT-RTE-model-assignment](runtime.md#rt-rte-model-assignment) | see [RT-RTE-model-assignment](runtime.md#rt-rte-model-assignment) | see [RT-RTE-model-assignment](runtime.md#rt-rte-model-assignment) | see [RT-RTE-model-assignment](runtime.md#rt-rte-model-assignment) | see [RT-RTE-model-assignment](runtime.md#rt-rte-model-assignment) | see [RT-RTE-model-assignment](runtime.md#rt-rte-model-assignment) | see [RT-RTE-model-assignment](runtime.md#rt-rte-model-assignment) | see [RT-RTE-model-assignment](runtime.md#rt-rte-model-assignment) | SRC-1: `src/beever_atlas/api/assignments.py` | none | none | see [RT-RTE-model-assignment](runtime.md#rt-rte-model-assignment) |

For the supplied containers, extraction/wiki/QA semantic change is **truth-apt transformation: indeterminate**: source instructions request extraction/distillation/grounding, but no checked input-output interpretation licenses a uniform preservation, entailment or non-entailment classification. Incoming platform/push content is **truth-apt transformation: acquisition/import** with source warrant unknown, not produced knowledge merely because Atlas stores it. Retention, curation eligibility, assignments and capability admission are **no content change** to team propositions, or **non-truth-apt policy/content update: tool/model/update eligibility** as appropriate. Their actual object, timing, force, consumer and recovery fields are owned by the cited records, not redefined by these classifications.

No separate lifecycle integration after evidence-consuming acceptance of an ampliative claim is established in these inspected routes. This is not a system-wide absence: alternative compiler, import, administrative and evaluation surfaces remain partially uninspected. The supersession route does implement withdrawal from selected consumers, and compiler checks do alter a next request; neither should be erased by that acceptance limit.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support and limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-knowledge-quality](#epi-clm-knowledge-quality) | see [EPI-CLM-knowledge-quality](#epi-clm-knowledge-quality) | SRC-1: `README.md`; doctrine/design | see [EPI-CLM-knowledge-quality](#epi-clm-knowledge-quality) | [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion), [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance), [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask), [EPI-RTE-quality-check](#epi-rte-quality-check), [EPI-RTE-narration-rewrite](#epi-rte-narration-rewrite), [EPI-RTE-fact-supersession](#epi-rte-fact-supersession) | none supplied | see [EPI-CLM-knowledge-quality](#epi-clm-knowledge-quality) | see [EPI-CLM-knowledge-quality](#epi-clm-knowledge-quality) | see [EPI-CLM-knowledge-quality](#epi-clm-knowledge-quality) |
| [EPI-CLM-traceable-citations](#epi-clm-traceable-citations) | see [EPI-CLM-traceable-citations](#epi-clm-traceable-citations) | SRC-1: `README.md`; doctrine/design | see [EPI-CLM-traceable-citations](#epi-clm-traceable-citations) | [EPI-RTE-citation-annotation](#epi-rte-citation-annotation), [RT-RTE-mcp-ask](runtime.md#rt-rte-mcp-ask) | none supplied | see [EPI-CLM-traceable-citations](#epi-clm-traceable-citations) | see [EPI-CLM-traceable-citations](#epi-clm-traceable-citations) | see [EPI-CLM-traceable-citations](#epi-clm-traceable-citations) |
| [EPI-CLM-lint-coherence](#epi-clm-lint-coherence) | see [EPI-CLM-lint-coherence](#epi-clm-lint-coherence) | SRC-1: `src/beever_atlas/api/wiki.py`; doctrine/design | see [EPI-CLM-lint-coherence](#epi-clm-lint-coherence) | [EPI-RTE-wiki-lint](#epi-rte-wiki-lint) | none supplied | see [EPI-CLM-lint-coherence](#epi-clm-lint-coherence) | see [EPI-CLM-lint-coherence](#epi-clm-lint-coherence) | see [EPI-CLM-lint-coherence](#epi-clm-lint-coherence) |

The public README also says QA retrieves wiki first; [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask) establishes a tool grant/model choice, not a mandatory first-stage enforcement. Scope/control and cross-store completion claims remain separately assessed in [RT-CLM-channel-isolation](runtime.md#rt-clm-channel-isolation), [RT-CLM-untrusted-tools](runtime.md#rt-clm-untrusted-tools) and [RT-CLM-write-completion](runtime.md#rt-clm-write-completion); none supplies factual warrant.

## Bounded conclusion

Atlas acquires conversation/source content, generates structured candidates and wiki/QA prose, and gives retained candidates operational authority in later retrieval and maintenance. Source warrant is unknown at import; signatures/ACLs authenticate admission scope, not message truth. Model scores and representation checks permit normal downstream processing without per-proposition human acceptance. See [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion), [EPI-RTE-quality-check](#epi-rte-quality-check), [EPI-RTE-quality-admission](#epi-rte-quality-admission).

Two content edges deserve independent caution. Narration rewriting can promote what someone said into an unqualified assertion; entity dedup can conflate identities by normalized labels or vector similarity. Neither semantic preservation nor source-backed entailment is established uniformly. These are implementation-supported risks, not observed incorrect outputs. See [EPI-RTE-narration-rewrite](#epi-rte-narration-rewrite), [EPI-RTE-entity-dedup](#epi-rte-entity-dedup).

Atlas does more than retain/retrieve: the implemented contradiction model produces a judgment that confidence thresholds turn into supersession or a warning flag. Semantic/native-hybrid reads with default `include_superseded=False` and consolidation context can withhold old content. Ordinary `search_channel_facts` can instead fall back to BM25 after embedding or hybrid-call exceptions; BM25 lacks the invalidation filter, and candidate formatting/MMR does not restore it. This fallback, as well as explicit superseded/ID reads, prevents complete withdrawal. This changes reliance under a heuristic criterion, not verified acceptance of the newer proposition. It operates after persistence, can miss candidates and can advance a watermark despite per-fact failures. See [EPI-RTE-contradiction-check](#epi-rte-contradiction-check), [EPI-RTE-fact-supersession](#epi-rte-fact-supersession).

Wiki maintenance can merge/save candidate prose under curation/parser constraints. Full compilation has output checks and corrective retry prompts, but inspected twice-failed branches can still deliver content; builder cache and identity-only incremental seeds differ. Retention and operational use must not be renamed acceptance or post-acceptance integration. No inspected route establishes warranted new team knowledge merely by fluent generation. See [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance), [RT-BAP-page-curation](runtime.md#rt-bap-page-curation), [EPI-RTE-compiler-retry](#epi-rte-compiler-retry), [EPI-RTE-builder-retention](#epi-rte-builder-retention).

Lint derives structural/freshness predicates; drift derives text-distance measurements against another generation; harness PASS derives authored test predicates. These derivations are licensed only within those computational domains and supplied inputs. None establishes source truth, general answer correctness, causal component benefit or transfer. Lint results are advisory, drift occurs after save, and test grades do not automatically reject production answers. See [EPI-RTE-wiki-lint](#epi-rte-wiki-lint), [EPI-RTE-drift-comparison](#epi-rte-drift-comparison), [EPI-RTE-qa-grading](#epi-rte-qa-grading).

Citations supply provenance aids, not a truth evaluator. HTTP and MCP answer routes and remote tools have different context/grant paths; selecting retrieved evidence does not establish compliant grounding or complete source lineage. See [EPI-RTE-citation-annotation](#epi-rte-citation-annotation), [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask), [RT-RTE-mcp-ask](runtime.md#rt-rte-mcp-ask), [RT-RTE-outbound-tools](runtime.md#rt-rte-outbound-tools).

Separate direct policy paths exist: persisted curation controls constrain incremental updates and assignment changes select model machinery. They are not model-weight learning or autonomous improvement. Automatic checks/retries and content-fed maintenance establish computational operations; improved future capacity, reflection on Atlas's own methods, retained content-directed method criticism, and exercised self-improvement are not established by those operations alone. No observed outcome or controlled intervention was supplied. These limits do not negate the implemented automatic updating or decision gates, and no system-wide negative follows from uninspected alternatives. See [RT-RTE-page-curation](runtime.md#rt-rte-page-curation), [RT-RTE-model-assignment](runtime.md#rt-rte-model-assignment), [EPI-RTE-compiler-retry](#epi-rte-compiler-retry).

## Shared records

### Components

#### EPI-CMP-contradiction-detector
Label: Contradiction detector model

Source-native identity: `contradiction_detector`, a distributed-parametric provider model. Parameter substrate is behind provider endpoint, not Atlas session state. Exact deployed weights/version are not pinned by this application revision. Explicit constructor override or mutable provider assignment can resolve another model. No parameter update is wired in this constructor/service; provider-internal updates are uninspected. Distinct from the supplied fact/entity/QA/maintainer model components: it compares retained fact candidates after persistence. SRC-1: `src/beever_atlas/agents/ingestion/contradiction_detector.py`.

> model=model or get_llm_provider().resolve_model("contradiction_detector"),
> --- `src/beever_atlas/agents/ingestion/contradiction_detector.py`

### Operative objects

#### EPI-OBJ-extracted-facts
Label: Extracted facts

Source-native identity: `extracted_facts` / `classified_facts`, and the resulting AtomicFact prose. Natural-language propositions in symbolic records, first ADK session memory then persisted fact-store records. Distinct material part from the generic working-state container; spans extraction state and durable output, so not wholly contained in that container. Compare [RT-OBJ-session-state](runtime.md#rt-obj-session-state) and [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion).

Content and role: Statements about team decisions, tools, people and work; actual fidelity is not established. Model scores are not independent observations. SRC-1: `src/beever_atlas/agents/callbacks/quality_gates.py`.

> # Bridge: also write as classified_facts so the embedder can read it
>     # without the classifier stage (which has been removed).
>     callback_context.state["classified_facts"] = callback_context.state["extracted_facts"]
> --- `src/beever_atlas/agents/callbacks/quality_gates.py`

#### EPI-OBJ-extracted-entities
Label: Extracted entities

Source-native identity: `extracted_entities` / `validated_entities` and relationships. Symbolic entity/edge records containing natural-language names and properties, in session dictionaries then graph store via the runtime persister. Distinct from [RT-OBJ-session-state](runtime.md#rt-obj-session-state) because this tracks the material content across validation and persistence, not the session substrate.

Content and role: Identity and relational claims; similarity/name equality need not establish real-world identity. SRC-1: `src/beever_atlas/agents/ingestion/cross_batch_validator.py`.

> state_delta={"validated_entities": result.model_dump()},
> --- `src/beever_atlas/agents/ingestion/cross_batch_validator.py`

#### EPI-OBJ-wiki-content
Label: Wiki content

Source-native identity: compiled page content and incremental page sections. Natural-language synthesis inside symbolic page/section records; Mongo-backed cache/page collections. No runtime object counterpart; [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance) is the update route, not this retained prose. Separate compiled cache and incremental seed representations must not be conflated.

Content and role: Candidate team knowledge; compiler cache contains rendered content while initial page-store seed omits sections. SRC-1: `src/beever_atlas/wiki/builder.py`.

> wiki_dict["pages"] = {p_id: p.model_dump(mode="json") for p_id, p in pages.items()}
> --- `src/beever_atlas/wiki/builder.py`

#### EPI-OBJ-contradiction-report
Label: Contradiction report

Source-native identity: `contradiction_report`. Symbolic list with natural-language reasons and numerical confidence, in ADK session state. No supplied object counterpart; distinct from fact/entity extractor outputs.

Content and role: Candidate incompatibility/supersession judgments, not independent adjudication of which proposition is true. SRC-1: `src/beever_atlas/services/contradiction_detector.py`.

> report = state.get("contradiction_report") or {}
> --- `src/beever_atlas/services/contradiction_detector.py`

#### EPI-OBJ-lint-report
Label: Lint report

Source-native identity: `LintReport` / `LintFinding`. Symbolic report with natural-language diagnostic messages, returned to API/MCP clients; no durable report storage established for lint. Distinct from retained wiki content and supplied runtime state.

Content and role: Structural/freshness/overlap predicates; no implemented LLM coherence verdict. SRC-1: `src/beever_atlas/services/wiki_lint.py`.

> findings.extend(find_duplicate_sections(pages))
> --- `src/beever_atlas/services/wiki_lint.py`

#### EPI-OBJ-qa-answer
Label: QA answer

Source-native identity: `accumulated_text` passed as `answer` to `_persist_qa_history`. Natural-language generated answer in process memory, delivered through SSE and persisted by the HTTP history route. Candidate assertions may concern channel knowledge, external context or a refusal. Distinct from extracted facts and wiki pages: this is query-conditioned prose; it spans working state and durable history rather than being wholly part of [RT-OBJ-session-state](runtime.md#rt-obj-session-state). Its generation, selection and read-back mechanisms are supplied by [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask); MCP has a separate session route in [RT-RTE-mcp-ask](runtime.md#rt-rte-mcp-ask). The history write is not acceptance of answer truth. SRC-1: `src/beever_atlas/api/ask.py`; implementation.

> await _persist_qa_history(
>                     question=question,
>                     answer=accumulated_text,
>                     citations=citations,
>                     channel_id=channel_id,
>                     user_id=user_id,
>                     session_id=session_id,
>                     use_v2_schema=use_v2_schema,
>                     thinking_text=accumulated_thinking,
>                     thinking_duration_ms=thinking_duration_ms,
>                     tool_calls=persisted_tool_calls,
>                     attachments=persisted_attachments,
>                 )
> --- `src/beever_atlas/api/ask.py:1398-1410`

#### EPI-OBJ-drift-report
Label: Drift report

Source-native identity: `DriftReport`. Symbolic metric fields and numerical edit-distance/statistical values describe the compared outputs; they are truth-apt over those input strings, not team facts. Stored in logs and best-effort MongoDB through `insert_wiki_drift_report`; transient return is available to caller. No supplied object counterpart: unlike wiki prose, this is evaluation evidence about generator output. Consumer scope and limitations are in [EPI-RTE-drift-comparison](#epi-rte-drift-comparison). Source snapshots, baseline truth and observed report instances remain unavailable. SRC-1: `src/beever_atlas/services/wiki_drift_comparator.py`; implementation.

> await mongo.insert_wiki_drift_report(report)
> --- `src/beever_atlas/services/wiki_drift_comparator.py`

### Routes

#### EPI-RTE-narration-rewrite
Label: Narration rewrite

Part of: [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion)

Part of the ingestion container, not a duplicate extraction model. Concrete implementation deduction without execution: `Alice mentioned that Redis is secure` matches the activity detector and author prefix; pattern2 captures `Redis is secure`; capitalisation leaves it unchanged; filter_fact replaces only memory_text and retains other fields. The input can be true while Redis is insecure (Alice may be wrong). For this concrete input, the output is an ampliative conjecture: its truth does not follow from the input. The general route remains indeterminate because extracted inputs may already encode direct claims. Thus this is not guaranteed non-ampliative reshaping: it removes the report qualifier without testing its embedded proposition. If the input fact instead already intended the embedded claim, preservation is possible; deciding that needs a source-to-extracted-claim trace. Remaining classifications are preservation or ampliative promotion, not established entailment. author_name retention preserves attribution metadata but does not restore the qualifier in the standalone assertion. No human per-fact approval or answer oracle; open ingestion follows shipped style rules. Exceptions retain original facts; no automatic semantic rollback.

Object/candidate: [EPI-OBJ-extracted-facts](#epi-obj-extracted-facts). Content/update relation: truth-apt transformation: indeterminate.

Transition or check target: Activity narration in memory_text. Evaluator/condition and domain: Regex detector and string slicing; English opener patterns, not a semantic evaluator. Activation and timing: After extraction/recovery, before quality threshold. Possible result: Residual text replaces narration, or importance becomes low, or original survives on failure. Implemented force: Enforcing text replacement/demotion in the callback. Epistemic authority and scope: No license from reported speech to the truth of the embedded proposition. Operational authority: Changed prose reaches classified_facts, embedding, persistence and later wiki/QA. Behavioral-authority path: Callback → classified_facts → fact consumers; enforcing stored wording, later-invocation horizon.

- Immediate return: Rewritten/demoted fact dictionaries.
- Later read-back: Retained output is consumed by later wiki/QA via the ingestion route; this function itself does not reload it.
- Delegated visibility: Downstream callback receives revised text and unchanged other fields.
- Selection predicate: Detected narration regex, then rewrite patterns; otherwise demote importance.
- Invalidation or expiry: Later writes can replace content; no text-rewrite undo here.
- Activation or effect: Changes output assertion or importance before admission; no observed downstream answer effect.
- Evidence limits: Deduction uses inspected implementation only; source truth and actual extractions unavailable.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1: `src/beever_atlas/agents/ingestion/narration_filter.py`; implementation.

> new_fact["memory_text"] = rewritten
> --- `src/beever_atlas/agents/ingestion/narration_filter.py`

> pattern2 = re.match(
>         r"^(?:noted|mentioned|stated|pointed\s+out|highlighted)\s+that\s+(.+)$",
>         author_stripped,
>         re.IGNORECASE,
>     )
>     if pattern2:
>         residual = pattern2.group(1).strip()
>         residual = _capitalise_first(residual)
>         return residual, True
> --- `src/beever_atlas/agents/ingestion/narration_filter.py`

#### EPI-RTE-quality-check
Label: Quality score check

Part of: [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion)

Fact model proposes its own content and quality; entity model supplies confidence. Code compares those values. Per-channel fact threshold can override global default; relationship threshold is global. No human per-content decision or external answer key. Recovery can salvage partial JSON and then apply the same gate, or set empty outputs on failure. The check and its disposition are separate material functions within the supplied extraction container.

Object/candidate: [EPI-OBJ-extracted-facts](#epi-obj-extracted-facts). Content/update relation: no content change.

Transition or check target: Model-emitted quality_score and relationship confidence against configured thresholds. Evaluator/condition and domain: Deterministic comparison of supplied numeric fields; no independent fact/source truth comparison. Activation and timing: After extraction or JSON salvage. Possible result: Predicate of threshold satisfaction. Implemented force: Operative input to the separately listed disposition. Epistemic authority and scope: Licenses only score ≥ configured threshold; score calibration unestablished. Operational authority: Selects predicate consumed by gate. Behavioral-authority path: Comparison → callback filter; enforcing eligibility in this batch.

- Immediate return: Threshold predicate within callback.
- Later read-back: inapplicable — predicate is current-batch computation, not retained memory.
- Delegated visibility: Filter receives score-bearing records, not independent evidence.
- Selection predicate: quality_score or confidence versus configured threshold.
- Invalidation or expiry: Recomputed each callback.
- Activation or effect: Controls gate eligibility; no semantic truth inference.
- Evidence limits: No calibration run or authenticated source comparison.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1: `src/beever_atlas/agents/callbacks/quality_gates.py`; implementation.

> filtered = [f for f in facts_dicts if f.get("quality_score", 0.0) >= threshold]
> --- `src/beever_atlas/agents/callbacks/quality_gates.py`

#### EPI-RTE-quality-admission
Label: Quality admission

Part of: [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion)

Part of the same ingestion container; distinct from checking numerical fields and from the preceding prose rewrite. Intended use is ingestion into stores; named criterion is configured model-score eligibility. It is not independent acceptance of an ampliative claim. The graph entity branch keeps global entities even without surviving relationships: no universal every-entity-has-supported-edge inference. Malformed/unrecoverable extraction can become empty; exceptions in narration filtering instead retain originals. Shipped prompts guide proposal, not a supplied answer oracle. No human-origin inference from initiating a sync.

Object/candidate: [EPI-OBJ-extracted-facts](#epi-obj-extracted-facts). Content/update relation: truth-apt transformation: non-ampliative reshaping.

Transition or check target: Candidate membership in downstream fact/entity outputs. Evaluator/condition and domain: Code applies threshold predicates; graph entities survive if global or referenced by surviving edges. Activation and timing: Immediately following quality comparison. Possible result: Dropped candidates or filtered state bridged to classified_facts. Implemented force: Enforcing omission from normal downstream state. Epistemic authority and scope: Operational eligibility only, not evidence-consuming acceptance of proposition truth. Operational authority: Admits surviving candidates to embedder/persister without per-fact human approval. Behavioral-authority path: Callback state → embedder/persister; enforcing batch gate, then retained outputs.

- Immediate return: Filtered extraction state.
- Later read-back: Output may persist and reach later wiki/QA; no separate read in callback.
- Delegated visibility: Only surviving state flows downstream on normal branch.
- Selection predicate: Threshold predicates, global scope or surviving relationship names.
- Invalidation or expiry: Subsequent processing replaces working state; dropped records not independently accepted.
- Activation or effect: Admits content operationally; no observed execution.
- Evidence limits: Persister fallback and alternate import/batch paths prevent universal gate claims.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1: `src/beever_atlas/agents/callbacks/quality_gates.py`; implementation.

> callback_context.state["extracted_entities"] = {
>         "entities": filtered_entities,
>         "relationships": filtered_rels,
>         "skip_reason": skip_reason,
>     }
> --- `src/beever_atlas/agents/callbacks/quality_gates.py`

#### EPI-RTE-entity-dedup
Label: Entity deduplication

Part of: [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion)

Part of ingestion, not a distinct LLM validator. Normalization maps `A-B` and `A B` to `a b`; such labels need not denote one entity. Merging may be lossless alias cleanup or an unwarranted identity conflation, so semantic relation is indeterminate. Primary name/type wins; aliases union, empty primary properties fill, and relationship source/target are rewritten. Registry absence or embedding failure degrades to exact-only; ambiguous hook is a stub even when fallback is enabled. No actual LLM judgment is supported by its fallback counter. Software decides; rejected cosine pairs can veto; exact-name collisions bypass that lookup. No oracle or per-merge human approval established. Rerun/reconfiguration is available, but no transactional undo demonstrated.

Object/candidate: [EPI-OBJ-extracted-entities](#epi-obj-extracted-entities). Content/update relation: truth-apt transformation: indeterminate.

Transition or check target: Entity identity and relationship endpoint substitution. Evaluator/condition and domain: Normalized names and name-vector cosine ≥0.92; 0.85–0.92 default hook returns false. Activation and timing: Parallel enrichment before persister. Possible result: Merged properties/aliases, renamed edge endpoints, merge records; ambiguous pairs retained separately. Implemented force: Enforcing output substitution, with registry rejected-pair veto on cosine tier. Epistemic authority and scope: Algorithmic equivalence only; no general real-world identity warrant. Operational authority: Canonicalized graph candidates can be persisted and used later. Behavioral-authority path: Validator → validated_entities → persister/graph consumers; enforcing names, persistent horizon.

- Immediate return: ValidationResult plus fallback count.
- Later read-back: Canonicalized persisted graph is available to later consumers; function itself only reads supplied prior entities and registry.
- Delegated visibility: Persister receives rewritten entities/edges and merges.
- Selection predicate: Exact normalized names/prior aliases, then cosine bands and rejected-pair registry.
- Invalidation or expiry: New batches/rejected-pair settings can alter future results; undo of old merges uninspected.
- Activation or effect: Substitutes graph identities; no observed correctness.
- Evidence limits: Embeddings do not prove coreference; default ambiguous hook supplies no model verdict.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1: `src/beever_atlas/services/entity_dedup.py`; implementation.

> new_rel.source = rename_map.get(rel.source, rel.source)
>         new_rel.target = rename_map.get(rel.target, rel.target)
> --- `src/beever_atlas/services/entity_dedup.py`

> The default implementation conservatively returns ``False`` (no
>     merge). Tests patch this symbol to simulate LLM-yes / LLM-no
>     decisions.
> --- `src/beever_atlas/services/entity_dedup.py`

#### EPI-RTE-contradiction-check
Label: Contradiction comparison

No supplied counterpart: this is a post-persistence evaluator, not the extraction validator. app.py subscribes a best-effort task to memory_settled. Watermark selection paginates new facts (ceiling 25k); candidate lookup actually uses only first entity tag, limit ten, excluding self and invalid_at facts. A topic-only fact can pass the outer tag guard yet find no candidates; the docstring about entity/topic overlap overstates implementation. Model receives formatted fact text/tags, not original messages or truth adjudication. Prompt requests direct contradictions, distinguishes additive updates and prioritizes newer statements. Whether a particular comparison is entailed analysis or an ampliative judgment needs inputs/output and checked interpretation. Exceptions return empty; absence of a finding is not corroboration. Bulk watermark can advance after swallowed per-fact failures. No human reviewer or expected-answer oracle; ongoing maintenance, not bounded experiment.

Object/candidate: [EPI-OBJ-contradiction-report](#epi-obj-contradiction-report). Content/update relation: truth-apt transformation: indeterminate.

Transition or check target: New fact versus selected live existing facts, for direct contradiction/temporal supersession. Evaluator/condition and domain: Provider model prompted to compare text, topics and entities; no independent source corroboration. Activation and timing: memory_settled subscriber, channel watermark window; also legacy per-batch branch found by source search. Possible result: At most one requested strongest contradiction with ID/confidence/reason, or empty report. Implemented force: Operative model result for threshold disposition. Epistemic authority and scope: Candidate incompatibility judgment only; cannot settle source truth or priority by recency alone. Operational authority: High/lower confidence consumed by lifecycle code. Behavioral-authority path: Model report → check_and_supersede; advisory judgment becomes enforcing via next route.

- Immediate return: Candidate contradiction dictionaries or empty list.
- Later read-back: inapplicable — transient report is not reloaded here; disposition persists lifecycle consequences.
- Delegated visibility: Model sees new/old texts and tags; disposition sees IDs/confidences/reasons.
- Selection predicate: Watermark for new facts; first entity tag for up to ten existing active candidates.
- Invalidation or expiry: Working report ends with call; watermark can suppress reconsideration on future events.
- Activation or effect: Judgment can reach supersession; no observed check instance.
- Evidence limits: Candidate restriction, fallbacks and swallowed errors prevent complete contradiction detection.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Identity comparison: no supplied route counterpart after comparison with the runtime containers; the distinct evaluator/writer/test boundary is stated above.

SRC-1: `src/beever_atlas/services/contradiction_detector.py`; implementation.

> contradictions = await detect_contradictions(new_fact, candidates[:10])
> --- `src/beever_atlas/services/contradiction_detector.py`

> _contradiction_worker.subscribe_memory_settled(_on_memory_settled_contradiction)
> --- `src/beever_atlas/server/app.py`

> filters=MemoryFilters(entity=new_fact.entity_tags[0]),
>                         limit=10,
> --- `src/beever_atlas/services/contradiction_detector.py`

> 1. Only flag DIRECT contradictions — not additive updates or loosely related facts.
> 2. Consider temporal context: a newer statement about the same subject likely supersedes the older one.
> --- `src/beever_atlas/agents/prompts/contradiction_detector.py`

#### EPI-RTE-fact-supersession
Label: Fact supersession

Distinct from check: code decides, model proposes conflict, no per-item human veto in this service. Named criterion is confidence threshold, intended use current team knowledge, scope selected candidate pairs. Existing fact gets invalid_at and superseded_by, new gets supersedes. Lower-band new fact only gets potential_contradiction. Consolidation _build_cluster_context filters superseded_by but keeps potential_contradiction. Semantic/native-hybrid search post-filters invalid_at when include_superseded=False; BM25 does not. Ordinary search_channel_facts enters BM25 on embedding or hybrid-call exceptions, then formats candidates and applies token-overlap MMR without checking invalid_at. Thus withdrawal is branch-specific: an invalidated fact can reach ordinary tool results without a deliberate superseded-content request. Explicit include_superseded and fetch_by_ids are additional counterexamples to total withdrawal. No checked source-to-truth acceptance or lifecycle integration following such acceptance is established. Two store updates are sequential, best-effort; partial errors and watermark advancement limit replay. No universal wiki invalidation/rollback inferred.

Object/candidate: [EPI-OBJ-extracted-facts](#epi-obj-extracted-facts). Content/update relation: no content change.

Transition or check target: Reliance on existing fact versus new fact. Evaluator/condition and domain: Code thresholds on model-reported confidence; new fact is preferred rather than independently verified. Activation and timing: After contradiction result; persisted lifecycle flags affect later reads. Possible result: High confidence invalidates old fact/links successor; lower confidence flags new fact; otherwise unchanged. Implemented force: Enforcing fact lifecycle mutation; flag alone is not rejection. Epistemic authority and scope: Records a conditional preference against a selected contradiction, not warranted acceptance of new truth. Operational authority: Old fact excluded by semantic/native-hybrid search with include_superseded=False and by consolidation context; ordinary fact-tool BM25 fallback can still deliver it, and potential contradictions remain. Behavioral-authority path: Threshold → Weaviate invalid_at/superseded_by → guarded semantic/native-hybrid readers and cluster context; enforcing eligibility on those branches until changed, not on the BM25 fallback.

- Immediate return: No semantic verdict return; durable flags/links and logs.
- Later read-back: Semantic/native-hybrid reads with include_superseded=False and consolidation context consume changed flags in later calls. search_channel_facts BM25 fallback does not filter invalid_at; formatting/MMR can pass invalidated content to the caller.
- Delegated visibility: Store receives fact IDs; later consumers receive selected surviving records, not the complete model rationale.
- Selection predicate: Confidence thresholds; selected existing ID from report.
- Invalidation or expiry: Persisted invalidation until another mutation; no automatic undo inspected.
- Activation or effect: Changes future content eligibility on guarded retrieval/consolidation branches; BM25 fallback can bypass withdrawal. No observed effect on answers or already-written wiki.
- Evidence limits: Not universal withdrawal: ordinary fact-tool BM25 fallback lacks the invalid_at filter, and include_superseded/fetch_by_ids remain explicit alternatives; failure recovery is best effort.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Identity comparison: no supplied route counterpart after comparison with the runtime containers; the distinct evaluator/writer/test boundary is stated above.

SRC-1: `src/beever_atlas/services/contradiction_detector.py`; implementation.

> if confidence >= settings.contradiction_confidence_threshold:
>                         await stores.weaviate.supersede_fact(
>                             old_fact_id=fact_id,
>                             new_fact_id=new_fact.id,
>                         )
> --- `src/beever_atlas/services/contradiction_detector.py`

> "invalid_at": now,
>                     "superseded_by": new_fact_id,
> --- `src/beever_atlas/stores/weaviate_store.py`

> active = [f for f in members if f.superseded_by is None]
> --- `src/beever_atlas/services/consolidation.py`

> # Post-filter superseded facts Python-side (avoids is_none nullstate
>                 # indexing requirement that Weaviate rejects when nullstate is not
>                 # indexed in the schema).
>                 if not include_superseded and fact.invalid_at is not None:
>                     continue
> --- `src/beever_atlas/stores/weaviate_store.py:901-905`

The ordinary fallback and its unfiltered store return are implementation evidence, not an observed return of an invalidated fact. SRC-1: `src/beever_atlas/agents/tools/memory_tools.py`, `src/beever_atlas/stores/weaviate_store.py`.

> facts = await store.bm25_search(
>                 query=query, channel_id=channel_id, tier="atomic", limit=fetch_limit
>             )
> --- `src/beever_atlas/agents/tools/memory_tools.py`

> result = collection.query.bm25(
>                 query=query,
>                 query_properties=self._BM25_QUERY_PROPERTIES,
>                 limit=limit,
>                 filters=combined,
>             )
>             return [self._obj_to_fact(obj) for obj in result.objects]
> --- `src/beever_atlas/stores/weaviate_store.py`

#### EPI-RTE-wiki-lint
Label: Wiki lint checks

No supplied route counterpart: RT-RTE-page-curation is mutation, not diagnosis. Direct HTTP handler passes llm_provider=None; no-provider coherence branch reports empty titled sections. Non-None provider branch also returns findings without a call. Thus LLM coherence exists as wording, not inspected evaluator. Example deduction: a page_id topic:abc with abc absent from live_cluster_ids produces an orphan finding. If live-cluster enumeration fails, handler leaves empty set; aggregator uses live_cluster_ids or set(), so all topic pages can appear orphaned despite the warning saying detection skips. This check is valid only relative to supplied set completeness. Duplicate signature uses first 50 sorted unique words longer than three chars, not semantic equality. No admission criterion, answer oracle or rollback: diagnosis returns evidence only.

Object/candidate: [EPI-OBJ-lint-report](#epi-obj-lint-report). Content/update relation: truth-apt transformation: entailed derivation.

Transition or check target: Page origin cluster membership, age, word-set signature equality, titled empty sections. Evaluator/condition and domain: Deterministic predicates over supplied pages/current cluster set/time; no implemented semantic LLM call. Activation and timing: Explicit HTTP/MCP lint request, not mandatory before serving pages. Possible result: Structured findings sorted by severity, returned to caller. Implemented force: Advisory; report does not rewrite, reject or block page use. Epistemic authority and scope: Predicate results within given snapshot, not factual correctness or semantic coherence. Operational authority: Human/model caller may decide maintenance; no automatic disposition in aggregator. Behavioral-authority path: API/MCP return → caller/UI; advisory this request, later caller action unresolved.

- Immediate return: LintReport returned, not a mutation verdict.
- Later read-back: inapplicable — no retained lint report/reload in inspected service.
- Delegated visibility: Caller gets findings/page counts; model coherence inspection is not implemented.
- Selection predicate: Explicit channel/language request; optional coherence fallback.
- Invalidation or expiry: Recomputed when requested; findings are time/snapshot-relative.
- Activation or effect: Advises maintenance without enforcing it.
- Evidence limits: Incomplete live-cluster set can produce spurious orphan findings; no semantic truth license.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Identity comparison: no supplied route counterpart after comparison with the runtime containers; the distinct evaluator/writer/test boundary is stated above.

SRC-1: `src/beever_atlas/services/wiki_lint.py`; implementation.

> findings.extend(find_orphans(pages, live_cluster_ids or set()))
> --- `src/beever_atlas/services/wiki_lint.py`

> llm_provider=None,  # Production wires LLMProvider here
> --- `src/beever_atlas/api/wiki.py`

> # Production LLM path is wired by the API handler — this function
>     # is kept pure-async so unit tests can stub the provider easily.
>     return findings
> --- `src/beever_atlas/services/wiki_lint.py`

#### EPI-RTE-drift-comparison
Label: Wiki drift comparison

No supplied counterpart: runtime maintenance describes production, not this comparison. Comparator is scheduled after saved_page and cannot veto that save. Regeneration is a comparison output, not an expected true answer. Operator soak thresholds are doctrine (median <0.15, p95 <0.30 over two weeks/three channels), not observed pass evidence. No randomized intervention or independently varied component is supplied. The actual incremental factory returns an already saved page; its timed factory is not the original update duration. No factual acceptance, rollback or automatic method revision is established by metric storage.

Object/candidate: [EPI-OBJ-wiki-content](#epi-obj-wiki-content) as target and [EPI-OBJ-drift-report](#epi-obj-drift-report) as produced evidence. Content/update relation: truth-apt transformation: entailed derivation.

Transition or check target: Incremental saved page versus regenerated output text and section identities. Evaluator/condition and domain: Levenshtein normalized by max string length; Jaccard section-ID sets; interpolated percentiles. Activation and timing: Flag-enabled/rate-selected post-save asynchronous comparison. Possible result: DriftReport metrics logged and best-effort persisted. Implemented force: Observational/advisory; no per-page content rejection from score. Epistemic authority and scope: Textual divergence from another generator, not truth, transfer or quality. Operational authority: Reports support admin/soak analysis, not an implemented automatic default flip here. Behavioral-authority path: Comparator → logs/Mongo/admin aggregation; advisory across soak window.

- Immediate return: DriftReport or None on error.
- Later read-back: Persisted report may be aggregated later; resulting policy changes uninspected.
- Delegated visibility: Logger/storage receive metrics; caller gets report; baseline builder output used locally.
- Selection predicate: wiki_drift_ab plus per-page scheduling/rate limit.
- Invalidation or expiry: Later comparisons replace evidence, not page content; no rollback of saved page.
- Activation or effect: Emits comparative evidence without blocking primary route.
- Evidence limits: No supplied soak results/causal design; comparator timing is factory timing.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Identity comparison: no supplied route counterpart after comparison with the runtime containers; the distinct evaluator/writer/test boundary is stated above.

SRC-1: `src/beever_atlas/services/wiki_drift_comparator.py`; implementation.

> raw = _levenshtein(a, b)
>     return raw / max(len(a), len(b))
> --- `src/beever_atlas/services/wiki_drift_comparator.py`

#### EPI-RTE-citation-annotation
Label: Citation annotation

Part of: [RT-RTE-dashboard-ask](runtime.md#rt-rte-dashboard-ask)

Part of HTTP QA container, distinct from its model generation and history retention. Wrapper skips list rows marked _empty, requires usable native identity and excerpt, and logs annotation failures. This is evidence transport, material because the public claim promises auditable citations. Linking an excerpt is not testing what an answer says about it. No per-claim human acceptance, truth oracle, rollback or downstream source-to-assertion check established by this wrapper. Full finalizer/registry resolvers remain outside direct inspection; runtime also distinguishes MCP parsed-text citations.

Object/candidate: [EPI-OBJ-extracted-facts](#epi-obj-extracted-facts). Content/update relation: no content change.

Transition or check target: Source identity/excerpt available on selected tool results. Evaluator/condition and domain: Wrapper derives native identity/excerpt, registers source, annotates source IDs; no assertion-entailment evaluator. Activation and timing: Only when a registry is bound; otherwise transparent return. Possible result: Tool dictionaries gain _cite/_src_id or remain unchanged. Implemented force: Permissive lineage supply to QA, not semantic verification. Epistemic authority and scope: Can identify retrieval provenance; cannot license every generated claim as supported. Operational authority: Model can emit references to registered retrieved content. Behavioral-authority path: Tool wrapper → model-visible dict → QA response; advisory provenance current invocation.

- Immediate return: Annotated tool result dictionaries.
- Later read-back: inapplicable — wrapper is current-turn registration; durable QA history is separate runtime route.
- Delegated visibility: Model receives selected excerpts with IDs and metadata, not independently verified source truth.
- Selection predicate: Bound registry, recognized dictionary/list shapes, nonempty native identity/excerpt.
- Invalidation or expiry: Registry binding horizon is current turn; no source endorsement TTL.
- Activation or effect: Enables referencing provenance; no demonstrated compliance or fidelity.
- Evidence limits: Finalizer semantics and every-source coverage uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1: `src/beever_atlas/agents/tools/_citation_decorator.py`; implementation.

> if source_id is not None:
>             item["_cite"] = f"[src:{source_id}]"
>             item["_src_id"] = source_id
> --- `src/beever_atlas/agents/tools/_citation_decorator.py`

#### EPI-RTE-compiler-retry
Label: Compiler output retry

No supplied counterpart: distinct full-generation evaluator beyond incremental maintenance. Target is page output against structural validators. Code decides retry; model proposes replacement; no human review. Shipped prompts plus failed-validation reason guide next attempt. The inspected branch returns content2 or content after twice-failed validation and can ship degenerate retry content. Other compiler branches and module-level validators are not exhaustively audited, so neither universal rejection nor universal absence of stronger checks follows. No expected-answer oracle. This is generation repair, not retained criticism of Atlas method theory.

Object/candidate: [EPI-OBJ-wiki-content](#epi-obj-wiki-content). Content/update relation: no content change.

Transition or check target: Generated page content format/substance heuristics in inspected delimited branch. Evaluator/condition and domain: Code checks short/safety output, degeneracy and optional validator; no source-truth oracle. Activation and timing: Within _call_llm retry loop, flags/mode dependent. Possible result: Validation reason appended to retry prompt; retry output may still fail. Implemented force: Operative retry request; not universal hard rejection. Epistemic authority and scope: Formatting/heuristic domain only. Operational authority: Triggers another generation call, not verified semantic correction. Behavioral-authority path: Validator result → retry prompt → compiler model; advisory model correction bounded retries.

- Immediate return: CompiledPageContent or another retry, in selected branches.
- Later read-back: inapplicable — retry judgment is within compilation; output retention is separate.
- Delegated visibility: Model receives diagnostic reason and prompt, not an independent checked reference.
- Selection predicate: Feature/mode flags, content presence, optional validator, remaining retry count.
- Invalidation or expiry: Current compilation; no retained critic report established.
- Activation or effect: Changes next model request, not guaranteed compliance.
- Evidence limits: Only selected compiler branches inspected; passing heuristic is not factual acceptance.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Identity comparison: no supplied route counterpart after comparison with the runtime containers; the distinct evaluator/writer/test boundary is stated above.

SRC-1: `src/beever_atlas/wiki/compiler.py`; implementation.

> prompt
>                             + f"\n\nNOTE: The previous attempt failed validation — {reason} Fix this on retry.",
> --- `src/beever_atlas/wiki/compiler.py`

> "WikiCompiler: validator_failed_twice event=deterministic_fallback page_kind=%s reason=%s",
>                             page_kind,
>                             reason2,
>                         )
>                         return CompiledPageContent(
>                             content=content2 or content, summary=summary2 or summary
>                         )
> --- `src/beever_atlas/wiki/compiler.py`

#### EPI-RTE-builder-retention
Label: Builder page retention

No supplied route counterpart: full builder writer is distinct from RT-RTE-wiki-maintenance. compile returns rendered domain pages; seeds use persistence-page schema. Seed intentionally omits sections/last_facts_seen, to be filled by maintainer. Therefore compiled prose cannot be assumed delivered unchanged to every incremental page reader. Shipped generation guidance and software assembly govern admission; no per-proposition human approval. Cache hash can skip recompile when inputs unchanged, not reaffirm truth. Snapshot/refresh API searches show recovery surfaces, not automatic semantic rollback. This route is retention before established epistemic acceptance, not lifecycle integration after it.

Object/candidate: [EPI-OBJ-wiki-content](#epi-obj-wiki-content). Content/update relation: no content change.

Transition or check target: Compiled pages into wiki cache and incremental page-store seeds. Evaluator/condition and domain: Code assembles WikiResponse and persists; seed failures logged per page. Activation and timing: After compile, no mandatory truth acceptance found in inspected save branch. Possible result: Rendered cache pages saved; incremental seeds contain identity/kind without sections. Implemented force: Enforcing persistence, not epistemic endorsement. Epistemic authority and scope: No additional warrant from save/is_stale=False. Operational authority: Enables later cache/UI reads and incremental first-sync eligibility. Behavioral-authority path: Builder → cache/page store → later readers/maintainer; permissive durable horizon.

- Immediate return: Wiki response/cache save and page seed attempts.
- Later read-back: Later cache/UI consumers can read rendered pages; maintainer reads identity-only seeds until first update.
- Delegated visibility: Cache gets rendered content; seed store gets identity/kind, not that prose.
- Selection predicate: Compiled page map and channel/language; build-input hash/force controls regeneration.
- Invalidation or expiry: Refresh/rebuild can replace cache; universal writer rollback not inspected.
- Activation or effect: Retains content and opens incremental update eligibility.
- Evidence limits: No observed build, correct output, or acceptance instance.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Identity comparison: no supplied route counterpart after comparison with the runtime containers; the distinct evaluator/writer/test boundary is stated above.

SRC-1: `src/beever_atlas/wiki/builder.py`; implementation.

> await self._cache.save_wiki(channel_id, wiki_dict, target_lang=target_lang)
> --- `src/beever_atlas/wiki/builder.py`

#### EPI-RTE-qa-grading
Label: QA harness grading

No supplied counterpart: RT QA routes are open questions; this is a bounded test mode with authored expected tools/kinds/minimum references and must-mention/not-mention strings as limited reference outcomes. Runtime model judgment is not the oracle here. Refusal-regex matches can satisfy canaries; citation floor permits expected-minus-one (except zero with positive floor); tools_ok/kinds_ok use any matching expected member, not full expected-set coverage. These counterexamples limit PASS. No per-fact acceptance or human authorship of each runtime answer; no automatic rollback/revision route in inspected grading. The benchmark script is separately available but not fully assessed: presence of a cassette benchmark is no observed real-service accuracy experiment.

Object/candidate: [EPI-OBJ-qa-answer](#epi-obj-qa-answer). Content/update relation: truth-apt transformation: entailed derivation.

Transition or check target: Test answer/tool/citation behavior against declared TestCase expectations. Evaluator/condition and domain: Deterministic grade dictionary with soft citation floor, substring canaries, kind/tool membership, follow-ups and length. Activation and timing: Explicit offline test battery against selected channel questions. Possible result: PASS iff all grade booleans; advisory warnings and summary artifacts. Implemented force: Diagnostic verdict only; no production answer gate or automatic source/policy update found here. Epistemic authority and scope: Only tested predicates, not general truth or answer support. Operational authority: Operator sees test summary; production mutation from verdict not established. Behavioral-authority path: Harness grade → printed/logged summary; advisory development horizon.

- Immediate return: Per-case grade/advisory/verdict and test result.
- Later read-back: uninspected — downstream use of persisted test summary is not traced.
- Delegated visibility: Test report includes answer, references, tool calls and predicates.
- Selection predicate: Authored TestCase expectations; selected channel and battery.
- Invalidation or expiry: New test runs can supersede reports, not production knowledge.
- Activation or effect: Creates diagnostic selection evidence; no automatic deployment admission established.
- Evidence limits: No supplied executed battery; PASS would not prove semantic correctness.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Identity comparison: no supplied route counterpart after comparison with the runtime containers; the distinct evaluator/writer/test boundary is stated above.

SRC-1: `scripts/qa_test_harness.py`; implementation.

> verdict = "PASS" if all(grade.values()) else "FAIL"
> --- `scripts/qa_test_harness.py`

### Claims

#### EPI-CLM-knowledge-quality
Label: Knowledge quality

Claimed operation: Better answers/fewer hallucinations from distilled knowledge. SRC-1: `README.md`; doctrine/design. Public comparative benefit claim, not a measured result. Source-native support is production/maintenance/QA plus operational quality thresholds, not a demonstrated increase in truth or reduction in hallucination. No observed or causal support supplied; no controlled treatment/comparison over source-grounded answers. Distinct from [RT-CLM-write-completion](runtime.md#rt-clm-write-completion) (persistence recovery), [RT-CLM-untrusted-tools](runtime.md#rt-clm-untrusted-tools) (capability restrictions) and [RT-CLM-channel-isolation](runtime.md#rt-clm-channel-isolation) (access policy).

> - **Better answers, fewer hallucinations** — retrieval operates on fact-dense prose with explicit entity relationships, not on fragmented turn-by-turn chat.
> --- `README.md`

#### EPI-CLM-traceable-citations
Label: Traceable citations

Claimed operation: Every wiki claim links back to source messages. SRC-1: `README.md`; doctrine/design. Public universal lineage claim. Citation annotation and generation instructions support an intended auditable path, not per-claim entailment or universal occurrence. Null/unbound registration, missing native identity/excerpt and partially inspected compiler/finalizer prevent proving every-claim coverage. No observed citation audit supplied. Distinct from runtime access/recovery claims.

> - **Traceable citations** — every wiki claim links back to the source messages that produced it, so answers are auditable all the way down to the original Slack/Discord/Teams thread.
> --- `README.md`

#### EPI-CLM-lint-coherence
Label: Lint coherence

Claimed operation: One bounded LLM coherence pass per page. SRC-1: `src/beever_atlas/api/wiki.py`; doctrine/design. Handler docstring doctrine conflicts with implementation: handler supplies None, fallback checks only empty sections, and even the non-None service branch makes no model call. No actual LLM-coherence evaluator is established at the inspected lint endpoint. Not a semantic truth check.

> Three deterministic checks (orphan / stale / duplicate-section)
>     + one bounded LLM coherence pass per page (max 1 call per page).
> --- `src/beever_atlas/api/wiki.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
