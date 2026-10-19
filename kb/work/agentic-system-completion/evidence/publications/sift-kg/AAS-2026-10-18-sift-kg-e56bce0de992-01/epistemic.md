---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "sift-kg epistemic routes: source attribution, structural checks, confidence policies and later reliance."
run-id: AAS-2026-10-18-sift-kg-e56bce0de992-01
reviewed-boundary: "d786991c024f5401f113fc0cb70aee96dd1bd3bf"
---

# sift-kg epistemic report

## Source-and-claim boundary

Question: what licenses reliance on document-derived graph assertions and generated prose, and which results actually change later use? Scope and external exclusions are those of [boundary](boundary.md#boundary-and-evidence); evidence identities are in its [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not an observed run or causal experiment. The runtime is a provisional route map, not an inspection limit.

The direct reads added here cover extraction prompt rules and parser/deduplication; graph support aggregation; postprocessing, review flagging and rejection removal; CLI search/export/view and init; public exports; and README approval/provenance claims. All are at the registered commit. Existing runtime records supply the other route evidence. No supersession is needed: the finer records below are material parts, not replacements of the valid runtime containers.

| Entry point or operation | Source path (SRC-1) | Coverage and records, or limit |
|---|---|---|
| CLI dispatch, module and public API | `src/sift_kg/cli.py`, `src/sift_kg/__init__.py`, `src/sift_kg/__main__.py`, `pyproject.toml` | Direct CLI decorator enumeration and public API read; module/console dispatch supplied by runtime. No model-registered tool loop is established; models return data to fixed stages. |
| extract, direct text/document APIs | `src/sift_kg/extract/extractor.py`, `src/sift_kg/extract/prompts.py` | Direct parser/prompt/dedupe reads; remaining orchestration supplied by [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction). |
| schema discovery | `src/sift_kg/domains/discovery.py` | Supplied [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery); quality unmeasured. |
| build, postprocess, flag | `src/sift_kg/graph/builder.py`, `src/sift_kg/graph/postprocessor.py`, `src/sift_kg/graph/knowledge_graph.py` | Direct material transformation/flag/support reads; load/save and pre-dedup supplied by [RT-RTE-graph-build](runtime.md#rt-rte-graph-build). |
| resolve, review, apply-merges | `src/sift_kg/resolve/resolver.py`, `src/sift_kg/resolve/reviewer.py`, `src/sift_kg/resolve/engine.py` | Supplied runtime records; direct rejection consumer read. |
| narrate and phrase repair | `src/sift_kg/narrate/generator.py` | Supplied [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation); no generated sentence/source comparison performed here. |
| search including descriptions | `src/sift_kg/cli.py` | Direct full search body; [EPI-OBJ-narrative-artifacts](#epi-obj-narrative-artifacts). |
| info, topology, query | `src/sift_kg/cli.py`, `src/sift_kg/graph/communities.py` | Supplied [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval). |
| export, view and library wrappers | `src/sift_kg/cli.py`, `src/sift_kg/pipeline.py` | Direct CLI wrappers; supplied library wrapper account. Wrappers load graph/descriptions without a new content approval. Serializer/filter/browser internals uninspected: prevents claims of complete lineage preservation or complete evaluator coverage there. |
| domains, init | `src/sift_kg/cli.py` | Dispatch scan; direct init body writes caller-controlled configuration, not corpus facts. Domain listing body uninspected; no knowledge-warrant conclusion assigned to it. |
| host skill, model components | `.agents/skills/sift-kg/SKILL.md`, `src/sift_kg/extract/llm_client.py`, `src/sift_kg/resolve/clustering.py` | Supplied runtime records; actual host uptake and provider internals outside available evidence. |
| ingestion/OCR, examples, tests, viewer internals | `src/sift_kg/ingest/reader.py`, `examples/`, `tests/`, `src/sift_kg/viewer/` | Not independently inspected here. Prevents end-to-end fidelity, benchmark accuracy and system-complete negative claims. Shipped artifacts without route-linked traces would not establish checking or acceptance anyway. |

Public warrant claims assessed below: persistent understanding and changed-document reuse from runtime, plus approval and provenance from this member. Missing provider state prevents assessment of internal model reasoning or training; absent execution evidence prevents activation and benefit findings; absent source/answer comparisons prevent factual accuracy and calibration findings. Uninspected relevant paths remain inspection limits, not evidenced absences.

## Epistemic-object inventory

Fields owned by a shared record are given by citation rather than copied. Schema symbolic rules and natural-language guidance remain separate consumption paths in the supplied container.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-domain-vocabulary](#epi-obj-domain-vocabulary) | see [EPI-OBJ-domain-vocabulary](#epi-obj-domain-vocabulary) | see [EPI-OBJ-domain-vocabulary](#epi-obj-domain-vocabulary) | see [EPI-OBJ-domain-vocabulary](#epi-obj-domain-vocabulary) | see [EPI-OBJ-domain-vocabulary](#epi-obj-domain-vocabulary) |
| [EPI-OBJ-domain-guidance](#epi-obj-domain-guidance) | see [EPI-OBJ-domain-guidance](#epi-obj-domain-guidance) | see [EPI-OBJ-domain-guidance](#epi-obj-domain-guidance) | see [EPI-OBJ-domain-guidance](#epi-obj-domain-guidance) | see [EPI-OBJ-domain-guidance](#epi-obj-domain-guidance) |
| [RT-OBJ-graph-data](runtime.md#rt-obj-graph-data) | see [RT-OBJ-graph-data](runtime.md#rt-obj-graph-data) | KnowledgeGraph retained stage boundary; see [RT-OBJ-graph-data](runtime.md#rt-obj-graph-data) | see [RT-OBJ-graph-data](runtime.md#rt-obj-graph-data) | see [RT-OBJ-graph-data](runtime.md#rt-obj-graph-data) |
| [RT-OBJ-review-files](runtime.md#rt-obj-review-files) | see [RT-OBJ-review-files](runtime.md#rt-obj-review-files) | Merge and relation decision files; see [RT-OBJ-review-files](runtime.md#rt-obj-review-files) | see [RT-OBJ-review-files](runtime.md#rt-obj-review-files) | see [RT-OBJ-review-files](runtime.md#rt-obj-review-files) |
| [EPI-OBJ-extraction-records](#epi-obj-extraction-records) | see [EPI-OBJ-extraction-records](#epi-obj-extraction-records) | see [EPI-OBJ-extraction-records](#epi-obj-extraction-records) | see [EPI-OBJ-extraction-records](#epi-obj-extraction-records) | see [EPI-OBJ-extraction-records](#epi-obj-extraction-records) |
| [EPI-OBJ-graph-assertions](#epi-obj-graph-assertions) | see [EPI-OBJ-graph-assertions](#epi-obj-graph-assertions) | see [EPI-OBJ-graph-assertions](#epi-obj-graph-assertions) | see [EPI-OBJ-graph-assertions](#epi-obj-graph-assertions) | see [EPI-OBJ-graph-assertions](#epi-obj-graph-assertions) |
| [EPI-OBJ-graph-support](#epi-obj-graph-support) | see [EPI-OBJ-graph-support](#epi-obj-graph-support) | see [EPI-OBJ-graph-support](#epi-obj-graph-support) | see [EPI-OBJ-graph-support](#epi-obj-graph-support) | see [EPI-OBJ-graph-support](#epi-obj-graph-support) |
| [EPI-OBJ-narrative-artifacts](#epi-obj-narrative-artifacts) | see [EPI-OBJ-narrative-artifacts](#epi-obj-narrative-artifacts) | see [EPI-OBJ-narrative-artifacts](#epi-obj-narrative-artifacts) | see [EPI-OBJ-narrative-artifacts](#epi-obj-narrative-artifacts) | see [EPI-OBJ-narrative-artifacts](#epi-obj-narrative-artifacts) |

## Authority-route ledger

Architectural statuses concern inspected implementation (directly or through supplied records), not operation. Each linked row isolates a function; repeated citations do not declare duplicate routes. An operational disposition is not automatically epistemic acceptance.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery) | content transformation | implemented | [RT-OBJ-domain-config](runtime.md#rt-obj-domain-config) | non-truth-apt policy/content update: extraction vocabulary and instructions | Corpus-specific schema | Model proposal; structural parsing/nonempty type check | see [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery) | see [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery) | see [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery) | Guidance fit is not corpus truth or completeness | Reusable guidance shapes prompts/build | see [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery) | see [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery) | none | none | see [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery); operation unobserved |
| [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery) | retention | implemented | [RT-OBJ-domain-config](runtime.md#rt-obj-domain-config) | no content change | Parsed schema to YAML | Code admission, not semantic acceptance | see [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery) | see [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery) | see [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery) | No additional warrant from persistence | Later schema reuse | see [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery) | see [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery) | none | none | see [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery); operation unobserved |
| [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | content transformation | implemented | [EPI-OBJ-extraction-records](#epi-obj-extraction-records) | truth-apt transformation: indeterminate | Chunk assertions to structured candidate assertions | Model interpreting text; requests explicit support | see [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | see [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | see [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | Source attribution retained as model text; source truth and semantic fidelity unknown | Candidates enter parser/cache | see [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | see [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | none | none | see [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction); operation unobserved |
| [EPI-RTE-extraction-check](#epi-rte-extraction-check) | check/evidence production | implemented | [EPI-OBJ-extraction-records](#epi-obj-extraction-records) | no content change | Returned field structure | Python/Pydantic structure and conversion only | see [EPI-RTE-extraction-check](#epi-rte-extraction-check) | see [EPI-RTE-extraction-check](#epi-rte-extraction-check) | see [EPI-RTE-extraction-check](#epi-rte-extraction-check) | Structural validity only, not quotation entailment | Malformed entries skipped; valid candidates continue | see [EPI-RTE-extraction-check](#epi-rte-extraction-check) | see [EPI-RTE-extraction-check](#epi-rte-extraction-check) | none | none | see [EPI-RTE-extraction-check](#epi-rte-extraction-check); operation unobserved |
| [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | retention | implemented | [EPI-OBJ-extraction-records](#epi-obj-extraction-records) | no content change | Parsed candidates to extraction cache | Code writer after deduplication | see [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | see [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | see [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | Retention precedes evidence-consuming acceptance | Build/narration/cache reuse | see [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | see [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | none | none | see [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction); operation unobserved |
| [EPI-RTE-support-aggregation](#epi-rte-support-aggregation) | content transformation | implemented | [EPI-OBJ-graph-support](#epi-obj-graph-support) | truth-apt transformation: entailed derivation | Numerical support statistics over admitted mentions | Fixed arithmetic/counts over supplied inputs | see [EPI-RTE-support-aggregation](#epi-rte-support-aggregation) | see [EPI-RTE-support-aggregation](#epi-rte-support-aggregation) | see [EPI-RTE-support-aggregation](#epi-rte-support-aggregation) | Arithmetic over mention list; not calibrated probability of world truth | Confidence participates in later review flagging | see [EPI-RTE-support-aggregation](#epi-rte-support-aggregation) | see [EPI-RTE-support-aggregation](#epi-rte-support-aggregation) | none | none | see [EPI-RTE-support-aggregation](#epi-rte-support-aggregation); operation unobserved |
| [EPI-RTE-graph-cleanup](#epi-rte-graph-cleanup) | content transformation | implemented | [EPI-OBJ-graph-assertions](#epi-obj-graph-assertions) | truth-apt transformation: indeterminate | Relation labels/endpoints and retained assertion set | Fixed vocabulary, topology and type rules | see [EPI-RTE-graph-cleanup](#epi-rte-graph-cleanup) | see [EPI-RTE-graph-cleanup](#epi-rte-graph-cleanup) | see [EPI-RTE-graph-cleanup](#epi-rte-graph-cleanup) | Known passive mappings can preserve meaning; generic rewrites need semantic assumptions | Changed and removed assertions reach saved graph | see [EPI-RTE-graph-cleanup](#epi-rte-graph-cleanup) | see [EPI-RTE-graph-cleanup](#epi-rte-graph-cleanup) | none | none | see [EPI-RTE-graph-cleanup](#epi-rte-graph-cleanup); operation unobserved |
| [RT-RTE-graph-build](runtime.md#rt-rte-graph-build) | retention | implemented | [RT-OBJ-graph-data](runtime.md#rt-obj-graph-data) | no content change | Built graph to disk | Code writer, not independent fact evaluator | see [RT-RTE-graph-build](runtime.md#rt-rte-graph-build) | see [RT-RTE-graph-build](runtime.md#rt-rte-graph-build) | see [RT-RTE-graph-build](runtime.md#rt-rte-graph-build) | Source fields do not certify source truth | Retrieval permitted before review | see [RT-RTE-graph-build](runtime.md#rt-rte-graph-build) | see [RT-RTE-graph-build](runtime.md#rt-rte-graph-build) | none | none | see [RT-RTE-graph-build](runtime.md#rt-rte-graph-build); operation unobserved |
| [EPI-RTE-relation-flagging](#epi-rte-relation-flagging) | check/evidence production | implemented | [EPI-OBJ-graph-support](#epi-obj-graph-support) | no content change | Confidence/type review policy | Threshold and review-required type membership | see [EPI-RTE-relation-flagging](#epi-rte-relation-flagging) | see [EPI-RTE-relation-flagging](#epi-rte-relation-flagging) | see [EPI-RTE-relation-flagging](#epi-rte-relation-flagging) | Flags policy exceptions, not falsehood | Review entries produced, not quarantine | see [EPI-RTE-relation-flagging](#epi-rte-relation-flagging) | see [EPI-RTE-relation-flagging](#epi-rte-relation-flagging) | none | none | see [EPI-RTE-relation-flagging](#epi-rte-relation-flagging); operation unobserved |
| [RT-RTE-entity-resolution](runtime.md#rt-rte-entity-resolution) | content transformation | implemented | [RT-OBJ-review-files](runtime.md#rt-obj-review-files) | truth-apt transformation: indeterminate | Identity and variant judgments | Model on selected attributes; deterministic same-name heuristic | see [RT-RTE-entity-resolution](runtime.md#rt-rte-entity-resolution) | see [RT-RTE-entity-resolution](runtime.md#rt-rte-entity-resolution) | see [RT-RTE-entity-resolution](runtime.md#rt-rte-entity-resolution) | Identity not entailed by name/selected attributes alone; individual judgments unobserved | Draft proposals only | see [RT-RTE-entity-resolution](runtime.md#rt-rte-entity-resolution) | see [RT-RTE-entity-resolution](runtime.md#rt-rte-entity-resolution) | none | none | see [RT-RTE-entity-resolution](runtime.md#rt-rte-entity-resolution); operation unobserved |
| [RT-RTE-review-decisions](runtime.md#rt-rte-review-decisions) | disposition/acceptance | implemented | [RT-OBJ-review-files](runtime.md#rt-obj-review-files) | no content change | Draft identity/relation proposals | Confidence policies or human keys; no reference oracle | see [RT-RTE-review-decisions](runtime.md#rt-rte-review-decisions) | see [RT-RTE-review-decisions](runtime.md#rt-rte-review-decisions) | see [RT-RTE-review-decisions](runtime.md#rt-rte-review-decisions) | Operational approval; human evidence-consuming criterion/use/scope not established | CONFIRMED permits merges; REJECTED permits deletion | see [RT-RTE-review-decisions](runtime.md#rt-rte-review-decisions) | see [RT-RTE-review-decisions](runtime.md#rt-rte-review-decisions) | [EPI-CLM-merge-approval](#epi-clm-merge-approval) | human-only reading contradicted | see [RT-RTE-review-decisions](runtime.md#rt-rte-review-decisions); operation unobserved |
| [RT-RTE-apply-decisions](runtime.md#rt-rte-apply-decisions) | operational admission/selection/consumption | implemented | [RT-OBJ-graph-data](runtime.md#rt-obj-graph-data) | truth-apt transformation: indeterminate | Confirmed identities and rejected relations | Status selection and node/key existence | see [RT-RTE-apply-decisions](runtime.md#rt-rte-apply-decisions) | see [RT-RTE-apply-decisions](runtime.md#rt-rte-apply-decisions) | see [RT-RTE-apply-decisions](runtime.md#rt-rte-apply-decisions) | No new truth license; executes prior decisions | Merge and deletion persist for later queries | see [RT-RTE-apply-decisions](runtime.md#rt-rte-apply-decisions) | see [RT-RTE-apply-decisions](runtime.md#rt-rte-apply-decisions) | none | none | see [RT-RTE-apply-decisions](runtime.md#rt-rte-apply-decisions); operation unobserved |
| [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) | content transformation | implemented | [EPI-OBJ-narrative-artifacts](#epi-obj-narrative-artifacts) | truth-apt transformation: indeterminate | Graph/excerpts to prose | Model generation and model phrase rewriting | see [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) | see [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) | see [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) | Requested factual preservation not established; no accepted ampliative claim shown | Prose/labels available without per-content approval | see [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) | see [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) | none | none | see [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation); operation unobserved |
| [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) | check/evidence production | implemented | [EPI-OBJ-narrative-artifacts](#epi-obj-narrative-artifacts) | no content change | Banned prose phrases, not facts | Regex detection over generated text | see [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) | see [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) | see [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) | Lexical match only; repair is a separate model transformation | Matches trigger rewrite, failure can retain original | see [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) | see [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) | none | none | see [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation); operation unobserved |
| [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) | retention | implemented | [EPI-OBJ-narrative-artifacts](#epi-obj-narrative-artifacts) | no content change | Generated prose/labels to files | Code assembly/writer | see [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) | see [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) | see [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) | No additional warrant from artifact availability | Descriptions and community labels reach later consumers | see [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) | see [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) | none | none | see [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation); operation unobserved |
| [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval) | operational admission/selection/consumption | implemented | [RT-OBJ-graph-data](runtime.md#rt-obj-graph-data) | truth-apt transformation: non-ampliative reshaping | Selected graph view for caller | Exact/name/alias, degree, BFS selection | see [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval) | see [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval) | see [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval) | Graph-local view, not independent answer verification | Delivers stdout to host; actual reliance unknown | see [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval) | see [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval) | [RT-CLM-second-brain](runtime.md#rt-clm-second-brain) | none | see [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval); operation unobserved |
| [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | lineage/freshness/recovery | implemented | [EPI-OBJ-extraction-records](#epi-obj-extraction-records) | no content change | Cache reuse | Configuration metadata predicate, not source hash | see [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | see [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | see [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | Freshness and endorsement not established by cache hit | Old candidates can be reused | see [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | see [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | [RT-CLM-incremental-extraction](runtime.md#rt-clm-incremental-extraction) | changed-document claim too broad | see [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction); operation unobserved |

No lifecycle-integration row is inferred from storage or graph linking. In the inspected routes the missing premise is an evidence-consuming acceptance decision with criterion, intended use and scope; a confirmed status alone does not supply it. This is a bounded finding, not a claim about all external human review. Imported document content is acquired, not produced knowledge. Semantic extraction, identity merging and narrative generation remain indeterminate transformations: the source establishes neither universal preservation nor a specific non-entailed output. Novelty or a generation prompt alone would not license an ampliative classification.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-second-brain](runtime.md#rt-clm-second-brain) | see [RT-CLM-second-brain](runtime.md#rt-clm-second-brain) | see [RT-CLM-second-brain](runtime.md#rt-clm-second-brain) | see [RT-CLM-second-brain](runtime.md#rt-clm-second-brain) | [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval) | none supplied | No comparison experiment; no causal attribution | Reload/select/deliver affordance | Delivery is not demonstrated grounding or better answers |
| [RT-CLM-incremental-extraction](runtime.md#rt-clm-incremental-extraction) | see [RT-CLM-incremental-extraction](runtime.md#rt-clm-incremental-extraction) | see [RT-CLM-incremental-extraction](runtime.md#rt-clm-incremental-extraction) | see [RT-CLM-incremental-extraction](runtime.md#rt-clm-incremental-extraction) | [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | none supplied | No comparison experiment; no causal attribution | Configuration-based reuse | Same-stem source edits can remain invisible |
| [EPI-CLM-merge-approval](#epi-clm-merge-approval) | see [EPI-CLM-merge-approval](#epi-clm-merge-approval) | see [EPI-CLM-merge-approval](#epi-clm-merge-approval) | see [EPI-CLM-merge-approval](#epi-clm-merge-approval) | [RT-RTE-review-decisions](runtime.md#rt-rte-review-decisions); [RT-RTE-graph-build](runtime.md#rt-rte-graph-build) | none supplied | No comparison experiment; no causal attribution | Status-gated apply, not human-only merging | Auto-approval and build pre-dedup are countercases |
| [EPI-CLM-source-provenance](#epi-clm-source-provenance) | see [EPI-CLM-source-provenance](#epi-clm-source-provenance) | see [EPI-CLM-source-provenance](#epi-clm-source-provenance) | see [EPI-CLM-source-provenance](#epi-clm-source-provenance) | [EPI-RTE-extraction-check](#epi-rte-extraction-check); [EPI-RTE-support-aggregation](#epi-rte-support-aggregation) | none supplied | No comparison experiment; no causal attribution | Document and model-supplied passage fields | Passage fidelity and universal lineage preservation unverified |

## Bounded conclusion

The implemented path acquires document text, constructs model-interpreted candidates and makes structurally parseable records operational before a factual acceptance decision is established. Extraction evidence fields preserve an attribution channel, not independently checked quotation fidelity or source warrant. Graph counts and confidence arithmetic derive statements about the admitted mention list; they do not establish the corresponding world propositions. See [EPI-RTE-extraction-check](#epi-rte-extraction-check), [EPI-RTE-support-aggregation](#epi-rte-support-aggregation) and [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction).

Cleanup has real deletion and rewriting force. Known passive-to-active maps can reshape a proposition without adding it; broad label normalization and schema-directed reversal do not independently warrant their semantic interpretation. Missing source evidence or unsupported schema assumptions cannot be repaired by graph consistency alone. Flagging is advisory until subsequent review/application. A confidence aggregate can change which relations are flagged even without new independent documents. See [EPI-RTE-graph-cleanup](#epi-rte-graph-cleanup) and [EPI-RTE-relation-flagging](#epi-rte-relation-flagging).

Review can supply a human disposition, but automatic thresholds and editable statuses also authorize action. The named implemented criteria are confidence thresholds, draft status and later node/key existence. Their intended operational scope is merge application or relation deletion. The consumer is the merge/rejection engine through YAML, enforcing changes in the next apply invocation and persisted graph. This is not an evidenced acceptance procedure for independently warranted factual claims. Rejected relations really can be removed; the opposite overstatement that all review is cosmetic would be false. Confirmed variant suggestions, however, are not inserted by that consumer. See [RT-RTE-review-decisions](runtime.md#rt-rte-review-decisions) and [RT-RTE-apply-decisions](runtime.md#rt-rte-apply-decisions).

Narrative generation and phrase correction retain prose without a factual oracle. Later search can explicitly return those descriptions; retrieval/export/view wrappers do not establish a new endorsement. Their authority is availability to readers and an advisory host instruction to rely on graph content, not demonstrated user or agent compliance. Retained discovered schemas directly shape later extraction/build behavior; this non-truth-apt policy update is independently supported even though its quality is unmeasured. See [EPI-OBJ-narrative-artifacts](#epi-obj-narrative-artifacts), [RT-BAP-host-skill](runtime.md#rt-bap-host-skill) and [RT-BAP-domain-guidance](runtime.md#rt-bap-domain-guidance).

The distributed-parametric components are separately bounded by [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client) and [RT-CMP-sentence-transformer](runtime.md#rt-cmp-sentence-transformer): inspected code does not train their parameters, exact external artifacts are not pinned, and provider internals remain uninspected. This does not rule out adaptation through retained schemas. No execution/contrast evidence establishes improved future capacity, exercised self-improvement or causal benefit; no route here establishes iterative criticism of an explanatory theory. These are independent limits, not a single system verdict. Accuracy, semantic preservation and evidence-consuming acceptance remain locally unestablished where specified, not globally disproved.

## Shared records

### Operative objects

#### EPI-OBJ-domain-vocabulary
Label: DomainConfig symbolic vocabulary
Part of: [RT-OBJ-domain-config](runtime.md#rt-obj-domain-config)

Source-native identity: entity/relation type names, endpoint-type lists, canonical_names, fallback_type, symmetric and review_required fields. Symbolic encoding consumed by fixed build/review rules; substrate is DomainConfig objects and bundled/custom/discovered YAML. Primarily policy rather than a claim that a particular corpus fact is true. Claimed role is vocabulary and selected structural constraints, not complete semantic validation. SRC-1, `src/sift_kg/domains/models.py`, `src/sift_kg/graph/builder.py`; supporting passage and conditional enforcement limits are in the supplied parent. Its distinct consumer path is [RT-BAP-domain-guidance](runtime.md#rt-bap-domain-guidance). Canonical enforcement requires a configured fallback; incompatible directions can remain unchanged.

#### EPI-OBJ-domain-guidance
Label: DomainConfig interpreted guidance
Part of: [RT-OBJ-domain-config](runtime.md#rt-obj-domain-config)

Source-native identity: descriptions, extraction hints and system context. Natural-language encoding consumed through model interpretation, on the same object/YAML substrate as the symbolic vocabulary. Instructions set extraction policy; descriptive statements may be truth-apt, but no particular discovered descriptive assertion is individuated by supplied execution evidence. Claimed role is corpus-specific extraction guidance. SRC-1, `src/sift_kg/extract/prompts.py`, `src/sift_kg/domains/discovery.py`; see the supplied parent and [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery) for passages, write/read-back route and admission. Prompt delivery is not a deterministic validator or evidence of model compliance. This part changes later model input without establishing improved schema quality.

#### EPI-OBJ-extraction-records
Label: DocumentExtraction candidates

No supplied object counterpart: distinct intermediate from [RT-OBJ-graph-data](runtime.md#rt-obj-graph-data), produced by [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction). Source-native identity: DocumentExtraction/ExtractionResult entities and relations. Symbolic field structure, type strings, confidence values and endpoints are consumed by code; natural-language names, attributes, contexts and evidence carry candidate propositions to models/humans. Substrate: process objects and per-document JSON. Claimed role is extraction from text, not certification. SRC-1, `src/sift_kg/extract/extractor.py`, `src/sift_kg/extract/prompts.py`. Source truth, translation fidelity, completeness and whether a returned quote occurs in its chunk are not established by the parser. Document summaries are transient model-generated context for later chunk calls; their wording/fidelity is unobserved, as traced by the supplied extraction route.

> - Extract only explicit information from the text
> --- `src/sift_kg/extract/prompts.py:112-115`

> - Do not infer relationships from co-occurrence alone
> --- `src/sift_kg/extract/prompts.py:120-123`

#### EPI-OBJ-graph-assertions
Label: Graph assertion payload
Part of: [RT-OBJ-graph-data](runtime.md#rt-obj-graph-data)

Source-native identity: nodes' names/attributes and edges' relation_type/source/target. Symbolic endpoints/types drive code; natural-language names and attributes require interpretation. Substrate: NetworkX graph and graph_data.json. Distinct from support metadata below: asserts identities, properties and relations, not merely how many extraction mentions exist. SRC-1, `src/sift_kg/graph/builder.py`, `src/sift_kg/graph/postprocessor.py`; supplied parent provides persistence evidence. Automatic build admission is not epistemic acceptance. Cleanup can alter which propositions remain and how readers interpret their direction/type.

#### EPI-OBJ-graph-support
Label: Relation support and evidence
Part of: [RT-OBJ-graph-data](runtime.md#rt-obj-graph-data)

Source-native identity: mentions, support_count, support_documents, support_doc_count, confidence, evidence and source_document edge fields. Symbolic counts/IDs/numbers feed review rules; natural-language evidence is delivered to human/model interpretation. Same graph/disk substrate as parent, different check target and authority. Candidate truth-apt content includes statements about extracted mention counts and source attribution, not a proven probability that the relation is true. SRC-1, `src/sift_kg/graph/knowledge_graph.py`, `src/sift_kg/graph/builder.py`. Mention repetition need not be independent evidence; counters and default confidence can grow within one document. See the aggregation route for a concrete deduction and passage.

#### EPI-OBJ-narrative-artifacts
Label: Narrative and descriptions

No supplied object counterpart after comparison with [RT-OBJ-graph-data](runtime.md#rt-obj-graph-data): separate narrative.md and entity_descriptions.json artifacts, produced by [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation). Natural-language prose may assert document-world claims, but no specific generated claim/entailment can be individuated from inspected execution evidence. JSON entity keys are symbolic selectors. Disk substrate; descriptions later reach search, export and viewer wrappers. Community labels additionally occupy the community sidecar described by the supplied narrative route. SRC-1, `src/sift_kg/cli.py`, `src/sift_kg/narrate/generator.py`. Search's --description branch exposes descriptions to a caller without a factual check; serializer/viewer internals remain uninspected. Claimed role is explanatory prose; source warrant after generation/repair is unknown.

> if description and node_id in descriptions:
>     entry["description"] = descriptions[node_id]
> --- `src/sift_kg/cli.py`

### Routes

#### EPI-RTE-extraction-check
Label: Extraction structural admission
Part of: [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction)

Code owns the step from model-returned JSON to typed entity/relation entries. Target/domain: field presence/defaults, numeric conversion and Pydantic structure, not the truth or textual entailment of assertions. Model proposes; code skips malformed entries; caller can later edit/remove/force outputs. No human or independent answer oracle participates. Open extraction, not a reference-scored experiment. Prompts request explicit relationships and evidence quotes, but parser copies evidence without source-substring comparison in the inspected function. The non-empty object is an operational candidate, not an accepted claim. Distinct check part of the supplied extraction container. SRC-1, `src/sift_kg/extract/extractor.py`.

- Immediate return: Typed entries or skipped malformed entries; handled call/parse failures return an empty chunk result.
- Later read-back: inapplicable — this check has no separate retained result; surrounding extraction persists candidates.
- Delegated visibility: inapplicable — checking is Python code over returned JSON.
- Selection predicate: Each returned entities/relations entry; malformed conversions are skipped.
- Invalidation or expiry: inapplicable — recomputed on each uncached chunk result.
- Activation or effect: Only structurally constructible entries reach the chunk result; no truth gate is added.
- Evidence limits: Pydantic admission and float conversion establish structure, not evidence authenticity.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> confidence=float(raw.get("confidence", 0.5)),
> evidence=raw.get("evidence", ""),
> --- `src/sift_kg/extract/extractor.py`

> except (ValueError, TypeError, KeyError) as e:
>     logger.debug(f"Skipping malformed relation: {e}")
> --- `src/sift_kg/extract/extractor.py`

#### EPI-RTE-support-aggregation
Label: Canonical relation support aggregation
Part of: [RT-RTE-graph-build](runtime.md#rt-rte-graph-build)

Code-owned add_relation folds same source/type/target mentions into a canonical edge, appending mention records, updating counts, keeping a unique document list and choosing the highest-confidence evidence for the top-level field. This is a distinct numerical/lineage part of build, not a replacement of the build route. Target/domain: statistics over supplied extraction mentions; default product-complement arithmetic is not empirically calibrated truth estimation. SRC-1, `src/sift_kg/graph/knowledge_graph.py`. Concrete implementation deduction, not execution: two admitted mentions of the same triple, each confidence 0.6 and both from document d, yield support_count 2, support_doc_count 1 and default confidence 1-(0.4*0.4)=0.84. At flag threshold 0.7 this clears the low-confidence predicate, although a review-required relation type still flags. There is no independence test in the append/aggregate path. User can select mean/max at the graph API, disable canonicalization or rebuild; these alternatives prevent a universal confidence-inflation claim. No reference-answer oracle or human admission is present in this aggregation.

- Immediate return: Boolean add result and mutated edge metadata.
- Later read-back: Saved edge support/confidence reaches later flagging, review and graph consumers through the build container.
- Delegated visibility: inapplicable — local arithmetic, not a delegated model judgment.
- Selection predicate: Canonicalization enabled, matching source/target/relation_type and existing endpoints.
- Invalidation or expiry: Recomputed from build inputs; mention records are not source-content freshness proofs.
- Activation or effect: Appended mentions raise support count; default confidence changes review eligibility; evidence/source_document top-level fields track a preferred mention.
- Evidence limits: The arithmetic is entailed by admitted numeric inputs; correctness, independence and calibration of those inputs remain unknown.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> mentions.append(mention)
> edge_data["mentions"] = mentions
> --- `src/sift_kg/graph/knowledge_graph.py`

> return 1.0 - prod(1.0 - c for c in confidences)
> --- `src/sift_kg/graph/knowledge_graph.py`

#### EPI-RTE-graph-cleanup
Label: Graph cleanup and schema rewriting
Part of: [RT-RTE-graph-build](runtime.md#rt-rte-graph-build)

Code owns deterministic graph mutation before save when postprocess is enabled. Fixed rules, not model/human evaluation, choose transformations: passive mappings/heuristic reversals, self-loop removal, LOCATED_IN transitive reduction, isolation pruning, vocabulary normalization and schema-directed flips. Targets/domains differ within these linked operations: label spelling, graph topology and configured endpoint types. None tests documentary truth. Concrete input deduction through inspected code: A TRAVELED_FROM B, with a nonempty domain vocabulary not containing TRAVELED_FROM, maps through _RELATION_SYNONYMS to A TRAVELED_TO B, with the endpoints unchanged by normalize_relation_types. The old and new directional meanings are not generally equivalent. Separately A ENABLED_BY B maps to B ENABLES A with copied evidence. These contrasting cases prevent classifying all cleanup as either faithful reshaping or novel knowledge production. Unfixable endpoint-type mismatches are kept as-is. Self-loop removal and isolation pruning can remove truthful assertions; their criterion is graph policy. LOCATED_IN A→C is removed when A→B→C exists; no new A→C edge is inferred. Caller can disable postprocess, change inputs/schema or rebuild; there is no inspected exact inverse log. No expected-answer oracle; fixed policy, no improvement experiment. SRC-1, `src/sift_kg/graph/postprocessor.py`, `src/sift_kg/graph/builder.py`.

- Immediate return: Mutated graph and transformation counters.
- Later read-back: Saved graph changes reach later query, resolution and narration through build.
- Delegated visibility: inapplicable — deterministic code owns the cleanup decisions.
- Selection predicate: postprocess and nonempty graph; individual mappings, topology predicates and configured types choose changes.
- Invalidation or expiry: Rebuild applies rules again; disabling postprocess bypasses them.
- Activation or effect: Changes/removes edges and prunes nodes before graph persistence; rules are enforcing, not warnings.
- Evidence limits: Known local rewrites can preserve meaning; generic schema fit and topology do not license source truth or universal equivalence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "TRAVELED_FROM": "TRAVELED_TO",
> --- `src/sift_kg/graph/postprocessor.py`

> mapped = _RELATION_SYNONYMS.get(rel_type)
> if not mapped and valid:
>     mapped = "ASSOCIATED_WITH"
> --- `src/sift_kg/graph/postprocessor.py`

> kg.graph.edges[source, target, key]["relation_type"] = mapped
> --- `src/sift_kg/graph/postprocessor.py`

> new_data = dict(data)
> new_data["relation_type"] = active
> kg.graph.add_edge(target, source, key=key, **new_data)
> --- `src/sift_kg/graph/postprocessor.py`

#### EPI-RTE-relation-flagging
Label: Relation review policy flags
Part of: [RT-RTE-graph-build](runtime.md#rt-rte-graph-build)

Code compares saved-graph relation confidence to threshold and checks configured review-required types, skipping MENTIONED_IN. Target/domain is review eligibility, not factual validity. Distinct check/evidence-production part of build. Code proposes review entries; later reviewer decides and can veto through status, then apply removes rejected edges. Flags do not themselves remove or quarantine an edge. SRC-1, `src/sift_kg/graph/builder.py`; save-before-flag sequencing is supplied by [RT-RTE-graph-build](runtime.md#rt-rte-graph-build). Default check threshold is 0.7 at function level; caller can change it. No answer oracle, open policy triage, no capacity-improvement experiment.

- Immediate return: Flagged dictionaries with evidence, source, confidence and reason.
- Later read-back: Caller-written relation_review.yaml feeds review and apply, as described by the build/review containers.
- Delegated visibility: inapplicable — this selector uses Python rules; humans see its output later.
- Selection predicate: Non-MENTIONED_IN relation with confidence below threshold or type in review_types.
- Invalidation or expiry: Recomputed on build; persisted flags are not graph-version-bound acceptance records.
- Activation or effect: Advisory selection into review; rejection acquires enforcing force only at apply.
- Evidence limits: An unflagged relation is not verified; aggregate confidence may count repeated mentions from one source.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if confidence < confidence_threshold:
>     reasons.append(f"Low confidence ({confidence:.2f} < {confidence_threshold})")
> if rel_type in review_types:
>     reasons.append(f"Type '{rel_type}' requires review")
> --- `src/sift_kg/graph/builder.py`

### Claims

#### EPI-CLM-merge-approval
Label: Nothing merges without approval

Claimed operation: human approval precedes merging. No supplied claim counterpart after comparison with [RT-CLM-second-brain](runtime.md#rt-clm-second-brain) and [RT-CLM-incremental-extraction](runtime.md#rt-clm-incremental-extraction). SRC-1, `README.md`, doctrine/design. The same README explicitly describes automatic build pre-dedup, so a charitable narrow reading concerns proposed resolution merges only. Even there [RT-RTE-review-decisions](runtime.md#rt-rte-review-decisions) auto-confirms eligible proposals; file status, not human identity, is checked by apply. Thus explicit per-item human verification is not an invariant. This does not deny that a user can choose manual YAML review or disable automatic approval.

> Nothing gets merged without your approval — the LLM proposes, you verify. Every extraction links back to the source document and passage.
> --- `README.md`

> Before entities become graph nodes, sift deterministically collapses names that are obviously the same. No LLM involved, no cost, no review needed:
> --- `README.md`

#### EPI-CLM-source-provenance
Label: Extraction links to source passage

Claimed operation: every extraction links to source document and passage. Distinct from the supplied agent-memory and cache claims; shares a README sentence with the approval claim but has a different target and route. SRC-1, `README.md`, doctrine/design; the verbatim passage is retained in [EPI-CLM-merge-approval](#epi-clm-merge-approval). Evidence/context fields and graph mention metadata implement attribution, not source-authenticated evidence or guaranteed exact quotations. [EPI-RTE-extraction-check](#epi-rte-extraction-check) accepts an absent evidence field as an empty string. [EPI-RTE-support-aggregation](#epi-rte-support-aggregation) retains mentions but selects a preferred top-level quotation. End-to-end preservation through export/browser paths is uninspected, preventing a universal lineage guarantee. Distinguish source document traceability from proof of the claimed relation.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; supplied route records and [RT-BAP-domain-guidance](runtime.md#rt-bap-domain-guidance), [RT-BAP-host-skill](runtime.md#rt-bap-host-skill) carry the relevant consumers and horizons.
