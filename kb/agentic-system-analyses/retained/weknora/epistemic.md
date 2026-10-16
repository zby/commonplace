---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "WeKnora epistemic routes: source acquisition, generated answers and wiki content, memory reliance, checks and bounded evaluation."
run-id: AAS-2026-10-15-weknora-7adf8a01c381-01
reviewed-boundary: "234aa948db29c10f5ed4b7939285c7b3711c5d4c"
---

# WeKnora epistemic report

## Source-and-claim boundary

Question: what truth-apt content can WeKnora acquire or generate, what checks affect reliance, and what later consumers receive the results? Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identity is see [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not observed operation or causal experiments. External model weights, provider internals and deployed storage/isolation are outside the inspected implementation. No target execution occurred.

The report directly inspected the additional source passages listed below, at the frozen pin. Supplied runtime routes remain provisional but provide the ordinary turn, RAG, context, document and installer witnesses. Available but uninspected alternatives remain included responsibilities, not access gaps. Coverage therefore supports independent positive findings and bounded limitations, not a system-complete negative about checking or knowledge production.

| Entry point or operation | SRC-1 source path | Coverage and records; conclusion prevented |
|---|---|---|
| Agent/RAG answers, source enablement, context and tools | `internal/application/service/session_agent_qa.go`, `internal/application/service/session_knowledge_qa.go`, `internal/application/service/knowledge_process.go`, `internal/agent/engine.go` | Supplied runtime findings: [RT-RTE-agent-turn](runtime.md#rt-rte-agent-turn), [RT-RTE-rag-answer](runtime.md#rt-rte-rag-answer), [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission), [RT-RTE-context-rewrite](runtime.md#rt-rte-context-rewrite). Exact answer content and model compliance unobserved. |
| CLI dispatch | `cli/cmd/root.go` | Direct read of command registrations: search, document/chunk CRUD, chat, model, MCP and skills surfaces corroborate multiple operations, not one agent-only entry. Individual command bodies and generic API passthrough uninspected; prevents exhaustive client-side semantic/admission account. |
| Registered built-ins | `internal/application/service/agent_service.go` | Direct read of register switch: search/read/list, graph, conversation/memory, SQL/data analysis, web, wiki read/issues/write/replace/rename/delete. Memory and wiki routes below add omitted maintenance checks. SQL/data-analysis derivation, web acquisition, graph claims and issue resolution bodies uninspected; prevents conclusions about every evaluator or derivation domain. |
| Model/tool controls and installer | `internal/agent/tools/registry.go`, `internal/agent/tools/mcp_tool.go`, `internal/application/service/tenant_skill_install.go` | Supplied [RT-RTE-mcp-call](runtime.md#rt-rte-mcp-call), [RT-RTE-sandbox-execution](runtime.md#rt-rte-sandbox-execution), [RT-RTE-skill-install](runtime.md#rt-rte-skill-install). Schema, approval and dependency checks have different targets from truth checking. |
| Background memory extraction/write/review | `internal/application/service/memory/extract.go`, `internal/application/service/memory/service.go`, `internal/router/routes_memory.go` | Direct reads; [EPI-RTE-memory-extraction](#epi-rte-memory-extraction), [EPI-RTE-memory-write](#epi-rte-memory-write), [EPI-RTE-memory-review](#epi-rte-memory-review). Topics/consolidation/vector internals not fully read; prevents complete memory adaptation and lineage account. |
| Memory later consumption | `internal/application/service/memory/service.go`, `internal/application/service/memory/search.go` | Direct reads; [EPI-RTE-memory-recall](#epi-rte-memory-recall); supplied caller injection in [boundary](boundary.md#boundary-and-evidence). Ranker internals and all stale-cache failure cases uninspected. |
| Wiki generation and withdrawal | `internal/application/service/wiki_ingest_batch.go`, `internal/application/service/wiki_ingest.go`, `internal/application/service/wiki_page.go` | Direct bounded reads; [EPI-RTE-wiki-rewrite](#epi-rte-wiki-rewrite), [EPI-RTE-wiki-guard](#epi-rte-wiki-guard). Map extraction/deduplication, all generation continuation and draft publication branches not fully read; prevents complete generated-content admission account. |
| Wiki lint and cleanup | `internal/application/service/wiki_lint.go`, `internal/application/service/wiki_ingest.go` | Direct reads; [EPI-RTE-wiki-maintenance](#epi-rte-wiki-maintenance). Link resolution helper and issue-tool internals uninspected; prevents semantic equivalence and complete criticism-loop claims. |
| Dataset metric hook and consumer | `internal/application/service/metric_hook.go`, `internal/application/service/metric/precision.go`, `internal/application/service/metric/bleu.go`, `internal/application/service/evaluation.go` | Direct reads; [EPI-RTE-dataset-metrics](#epi-rte-dataset-metrics). BLEU tokenization/helpers and other metric formulas not fully read; no measured quality or causal comparison. |
| Other state-producing surfaces | `docreader/main.py`, `internal/application/service/knowledge_create.go`, `internal/application/service/knowledgebase_search.go` | Boundary survey/runtime coverage only for parser, URL/manual/FAQ ingestion, connectors, OCR/VLM, graph and alternate indexes. End-to-end semantic fidelity and exact evaluator coverage remain unassessed. |

Knowledge/warrant claims: [RT-CLM-evidence-verification](runtime.md#rt-clm-evidence-verification), [EPI-CLM-cited-answers](#epi-clm-cited-answers), [EPI-CLM-automatic-wiki](#epi-clm-automatic-wiki), [EPI-CLM-end-evaluation](#epi-clm-end-evaluation). No inferred stronger promise of infallibility is assessed.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source/local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt) | Verification policy, not itself evidence of verified answers | see record | see record | Instructions do not establish obedience. |
| [RT-OBJ-agent-config](runtime.md#rt-obj-agent-config) | None for grants/limits; configuration is operational policy | see record | see record | Permission is not endorsement. |
| [EPI-OBJ-knowledge-chunks](#epi-obj-knowledge-chunks) | Imported source assertions over their document scope | see record | see record | Parser fidelity and source truth unestablished. |
| [EPI-OBJ-chat-response](#epi-obj-chat-response) | Candidate answer assertions or none, depending on response | see record | see record | Actual propositions and factual entailment not determinable without output instances. |
| [EPI-OBJ-context-checkpoint](#epi-obj-context-checkpoint) | Summarized earlier conversation claims | see record | see record | Compression can omit evidence; retained summary is not accepted truth. |
| [EPI-OBJ-memory-item](#epi-obj-memory-item) | User/project facts, preferences and tasks; inferred user claims | see record | see record | Truth apt only over named user/environment/time; source pointers and status do not prove truth. |
| [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | Document synopses, entity/concept assertions and source relationships | see record | see record | Summary refs and chunk refs differ; proposition-level support unproved. |
| [EPI-OBJ-metric-result](#epi-obj-metric-result) | Measurements about supplied evaluation pairs, not general truth of answers | see record | see record | Matching can omit unmatched retrieval results; see metric route. |

Answers, imported chunks and summaries are separately inventoried here as outputs of the supplied runtime routes, not as duplicate route declarations. Their exact propositions are not determinable without an instance. Model components remain separately typed in [RT-CMP-chat-model](runtime.md#rt-cmp-chat-model), [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model), [RT-CMP-rerank-model](runtime.md#rt-cmp-rerank-model) and [RT-CMP-vlm-model](runtime.md#rt-cmp-vlm-model): weights and exact parameter identities are not inspected. Dense vectors and ranking scores are not equated with localized factual claims.

## Authority-route ledger

Every row is an architectural assessment, not a claim of activation. Separate rows distinguish checking, disposition and retention even when one record covers their common implementation. Owned route details say see rather than being duplicated.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission) | content transformation | implemented | [EPI-OBJ-knowledge-chunks](#epi-obj-knowledge-chunks) | truth-apt transformation: acquisition/import | external source → indexed content | Parser/index pipeline; semantic fidelity uninspected | see [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission) | stored/indexed/enabled | see [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission) | Source warrant unknown; source storage does not check its truth | Eligible evidence for retrieval | Retrieval services; indexes; permissive; later queries | see [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission) | none | none | Operation unobserved; see record. |
| [RT-RTE-rag-answer](runtime.md#rt-rte-rag-answer) | content transformation | implemented | [EPI-OBJ-chat-response](#epi-obj-chat-response) | truth-apt transformation: indeterminate | retrieved evidence → answer | Configured chat model; no reference oracle in ordinary QA | see [RT-RTE-rag-answer](runtime.md#rt-rte-rag-answer) | answer/fallback/error | see [RT-RTE-rag-answer](runtime.md#rt-rte-rag-answer) | Candidate answer only; entailment and source truth not established | Answer delivered/stored | User and later QA context; answer/history; advisory; current/later turns | see [RT-RTE-rag-answer](runtime.md#rt-rte-rag-answer) | [EPI-CLM-cited-answers](#epi-clm-cited-answers) | none | Operation unobserved; see record. |
| [RT-RTE-agent-turn](runtime.md#rt-rte-agent-turn) | content transformation | implemented | [EPI-OBJ-chat-response](#epi-obj-chat-response); tool proposals are a distinct non-truth-apt action channel | truth-apt transformation: indeterminate | open task/context → model content | Configured model; code validates calls, not all factual claims | see [RT-RTE-agent-turn](runtime.md#rt-rte-agent-turn) | answer, partial content or error | see [RT-RTE-agent-turn](runtime.md#rt-rte-agent-turn) | Candidate assertions, not an inspected evidence-consuming acceptance decision | Can propose executable actions under distinct eligibility checks | Tools/user/history; calls and text; conditional executable/advisory; turn and later history | see [RT-RTE-agent-turn](runtime.md#rt-rte-agent-turn) | [RT-CLM-evidence-verification](runtime.md#rt-clm-evidence-verification) | none | Operation unobserved; see record. |
| [RT-RTE-context-rewrite](runtime.md#rt-rte-context-rewrite) | content transformation | implemented | [EPI-OBJ-context-checkpoint](#epi-obj-context-checkpoint); transient tool previews | truth-apt transformation: indeterminate | older context → compressed context | Summary model and code budget rules; token size not semantic equivalence | see [RT-RTE-context-rewrite](runtime.md#rt-rte-context-rewrite) | summary/raw fallback/preview | see [RT-RTE-context-rewrite](runtime.md#rt-rte-context-rewrite) | Semantic warrant unresolved; truncation can degrade evidence visibility | Replacement admitted into later model inputs | Foreground model; summary/checkpoint; advisory; later invocations | see [RT-RTE-context-rewrite](runtime.md#rt-rte-context-rewrite) | none | none | Operation unobserved; see record. |
| [RT-RTE-context-rewrite](runtime.md#rt-rte-context-rewrite) | retention | implemented | [EPI-OBJ-context-checkpoint](#epi-obj-context-checkpoint) | no content change | summary → saved checkpoint | Code eligibility, not factual acceptance | see [RT-RTE-context-rewrite](runtime.md#rt-rte-context-rewrite) | checkpoint persisted | see [RT-RTE-context-rewrite](runtime.md#rt-rte-context-rewrite) | Retention is not acceptance | Later history can start from checkpoint | History loader/model; repository/context; permissive/advisory; later turns | see [RT-RTE-context-rewrite](runtime.md#rt-rte-context-rewrite) | none | none | Operation unobserved; see record. |
| [RT-RTE-mcp-call](runtime.md#rt-rte-mcp-call) | disposition/acceptance | implemented | tool call arguments | non-truth-apt policy/content update: execution permission | proposed call → permitted/refused | Policy/schema and conditional user approval; effect authorization | see [RT-RTE-mcp-call](runtime.md#rt-rte-mcp-call) | execute/refuse/suspend | see [RT-RTE-mcp-call](runtime.md#rt-rte-mcp-call) | No truth license for returned content | Permits or blocks selected external call | Registry/MCP; policy/approval; enforcing when active; selected call | see [RT-RTE-mcp-call](runtime.md#rt-rte-mcp-call) | none | none | Operation unobserved; see record. |
| [RT-RTE-skill-install](runtime.md#rt-rte-skill-install) | check/evidence production | implemented | skill capability prerequisites | no content change | bundle/install candidate | Tree/script/declared command checks; dependency availability domain | see [RT-RTE-skill-install](runtime.md#rt-rte-skill-install) | verification findings | see [RT-RTE-skill-install](runtime.md#rt-rte-skill-install) | Bounded prerequisite evidence, not all functional promises | Findings can trigger repair or gate rejection | Installer service; verifier result; enforcing; installation rounds | see [RT-RTE-skill-install](runtime.md#rt-rte-skill-install) | none | none | Operation unobserved; see record. |
| [RT-RTE-skill-install](runtime.md#rt-rte-skill-install) | disposition/acceptance | implemented | snapshot candidate | non-truth-apt policy/content update: capability admission | verified install → image pointer | Verifier outcome plus lock/ownership checks | see [RT-RTE-skill-install](runtime.md#rt-rte-skill-install) | ready/image switch or failure | see [RT-RTE-skill-install](runtime.md#rt-rte-skill-install) | Acceptance for setup use under inspected prerequisite criteria only | New capability environment admitted | Workspace resolver; snapshot pointer; executable/permissive; later sessions | see [RT-RTE-skill-install](runtime.md#rt-rte-skill-install) | none | none | Operation unobserved; see record. |
| [EPI-RTE-memory-extraction](#epi-rte-memory-extraction) | content transformation | implemented | [EPI-OBJ-memory-item](#epi-obj-memory-item) | truth-apt transformation: indeterminate | transcript/existing notes → decisions | Extraction model; JSON/truncation code checks output usability | see [EPI-RTE-memory-extraction](#epi-rte-memory-extraction) | add/update/delete/none proposals | see [EPI-RTE-memory-extraction](#epi-rte-memory-extraction) | Repeating a statement acquires its claim; exact semantic preservation unproved | Proposes changes but does not itself confirm inferred claims | Write consumer; JSON decisions; advisory; background extraction | see [EPI-RTE-memory-extraction](#epi-rte-memory-extraction) | none | none | Prompt example explicitly licenses a non-entailed guess from event questions to organising events; that candidate class is ampliative conjecture. Particular actual outputs unobserved. |
| [EPI-RTE-memory-write](#epi-rte-memory-write) | check/evidence production | implemented | [EPI-OBJ-memory-item](#epi-obj-memory-item) | no content change | proposed memory write | Sanitization, credential policy, tombstones and conflicts; storage-policy domain | see [EPI-RTE-memory-write](#epi-rte-memory-write) | eligible/redacted/skipped/error | see [EPI-RTE-memory-write](#epi-rte-memory-write) | No test of source truth or of inferred flag correctness | Determines eligible writes | Memory service; validation results; enforcing; this write | see [EPI-RTE-memory-write](#epi-rte-memory-write) | none | none | Operation unobserved; see record. |
| [EPI-RTE-memory-write](#epi-rte-memory-write) | disposition/acceptance | implemented | [EPI-OBJ-memory-item](#epi-obj-memory-item) | non-truth-apt policy/content update: memory status | candidate → active/pending | Code uses Inferred and Origin supplied by producer | see [EPI-RTE-memory-write](#epi-rte-memory-write) | active or pending | see [EPI-RTE-memory-write](#epi-rte-memory-write) | Active licenses operational recall, not evidence-certified truth | Unflagged extraction can take effect without human confirmation | Repository/recall; status; permissive; later turns | see [EPI-RTE-memory-write](#epi-rte-memory-write) | none | none | Operation unobserved; see record. |
| [EPI-RTE-memory-write](#epi-rte-memory-write) | retention | implemented | [EPI-OBJ-memory-item](#epi-obj-memory-item) | no content change | eligible candidate → stored row | Code/repository write; capacity and embeddings best effort | see [EPI-RTE-memory-write](#epi-rte-memory-write) | saved/replaced/archived | see [EPI-RTE-memory-write](#epi-rte-memory-write) | Source pointers retained; warranted premises not independently checked | Retains claims for later selection | Recall/search; memory row; permissive; cross-session | see [EPI-RTE-memory-write](#epi-rte-memory-write) | none | none | Operation unobserved; see record. |
| [EPI-RTE-memory-review](#epi-rte-memory-review) | disposition/acceptance | implemented | [EPI-OBJ-memory-item](#epi-obj-memory-item) | non-truth-apt policy/content update: confirmation or withdrawal | pending claim → confirmed or rejected | API caller decision; service confirms or deletes | see [EPI-RTE-memory-review](#epi-rte-memory-review) | active or deleted/tombstoned | see [EPI-RTE-memory-review](#epi-rte-memory-review) | Human/caller endorsement possible; evidence consumed and named truth criterion not recorded | Confirmation permits recall; rejection blocks ordinary read and re-derivation when tombstone exists | Recall/write; status/tombstone; enforcing eligibility; later turns | see [EPI-RTE-memory-review](#epi-rte-memory-review) | none | none | Generic principal is not evidence of human review. Tombstone failure is logged but deletion continues; absolute non-recurrence is not warranted. |
| [EPI-RTE-memory-recall](#epi-rte-memory-recall) | operational admission/selection/consumption | implemented | [EPI-OBJ-memory-item](#epi-obj-memory-item) | no content change | active memories → selected prompt/tool result | Code active queries and lexical/semantic ranking; relevance domain | see [EPI-RTE-memory-recall](#epi-rte-memory-recall) | selected memories | see [EPI-RTE-memory-recall](#epi-rte-memory-recall) | Recall does not add truth warrant | Supplies model context; touch records use rather than truth | Foreground model; prompt/search result; advisory; subsequent model calls | see [EPI-RTE-memory-recall](#epi-rte-memory-recall) | none | none | Subject block cache fallback exists; no complete failure-path withdrawal guarantee established. |
| [EPI-RTE-wiki-rewrite](#epi-rte-wiki-rewrite) | content transformation | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | truth-apt transformation: indeterminate | existing page + sources/additions/retractions → revised page | Chat model guided by chunks, summaries and deleted/remaining sources | see [EPI-RTE-wiki-rewrite](#epi-rte-wiki-rewrite) | new body or generation failure | see [EPI-RTE-wiki-rewrite](#epi-rte-wiki-rewrite) | Source references aid inspection; generated body may be paraphrase, derivation or conjecture | Proposes page content including removal of deleted-source contributions | Wiki write service; generated body; advisory until write; batch/later reads | see [EPI-RTE-wiki-rewrite](#epi-rte-wiki-rewrite) | [EPI-CLM-automatic-wiki](#epi-clm-automatic-wiki) | none | Operation unobserved; see record. |
| [EPI-RTE-wiki-guard](#epi-rte-wiki-guard) | check/evidence production | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | no content change | stored/proposed table row identities | Deterministic identity-loss check; table preservation domain | see [EPI-RTE-wiki-guard](#epi-rte-wiki-guard) | loss ratio/refusal | see [EPI-RTE-wiki-guard](#epi-rte-wiki-guard) | Checks bounded loss, not cell truth, full evidence preservation or source encoding | Produces enforcing write condition | UpdatePage; loss result; enforcing with exemptions; this rewrite | see [EPI-RTE-wiki-guard](#epi-rte-wiki-guard) | none | none | Operation unobserved; see record. |
| [EPI-RTE-wiki-guard](#epi-rte-wiki-guard) | disposition/acceptance | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | non-truth-apt policy/content update: page write admission | candidate → saved or deferred | Code source-specific tolerance; intentional shrink exceptions | see [EPI-RTE-wiki-guard](#epi-rte-wiki-guard) | write or old page retained/deferred | see [EPI-RTE-wiki-guard](#epi-rte-wiki-guard) | No factual acceptance decision for all page propositions | Blocks offending rewrite; ingest retains contributing documents for retry | Ingest/agent writer; explicit error; enforcing; this write/next batch | see [EPI-RTE-wiki-guard](#epi-rte-wiki-guard) | none | none | Operation unobserved; see record. |
| [EPI-RTE-wiki-rewrite](#epi-rte-wiki-rewrite) | retention | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | no content change | generated page → persisted content and refs | Wiki service CreatePage/UpdatePage | see [EPI-RTE-wiki-rewrite](#epi-rte-wiki-rewrite) | page/ref update | see [EPI-RTE-wiki-rewrite](#epi-rte-wiki-rewrite) | Retained candidate with lineage, not necessarily accepted knowledge | Available to wiki read/search tools | Wiki clients/model; stored pages; advisory; later requests | see [EPI-RTE-wiki-rewrite](#epi-rte-wiki-rewrite) | none | none | Operation unobserved; see record. |
| [EPI-RTE-wiki-maintenance](#epi-rte-wiki-maintenance) | check/evidence production | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | no content change | wiki link/source availability and short content | RunLint live-slug/source probes and content-size rules; structural domain | see [EPI-RTE-wiki-maintenance](#epi-rte-wiki-maintenance) | lint issues | see [EPI-RTE-wiki-maintenance](#epi-rte-wiki-maintenance) | Existence/freshness evidence only; not endorsement | Selected results feed AutoFix | AutoFix/operator; lint report; advisory/conditional enforcing; maintenance invocation | see [EPI-RTE-wiki-maintenance](#epi-rte-wiki-maintenance) | none | none | Operation unobserved; see record. |
| [EPI-RTE-wiki-maintenance](#epi-rte-wiki-maintenance) | content transformation | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) content | truth-apt transformation: non-ampliative reshaping | exact broken-link markup → plain target text | AutoFix literal replacement; text/markup domain | see [EPI-RTE-wiki-maintenance](#epi-rte-wiki-maintenance) | plain text persisted | see [EPI-RTE-wiki-maintenance](#epi-rte-wiki-maintenance) | Preserves the demonstrated label text while withdrawing a navigable reference; not source endorsement | Changes displayed link availability | Wiki readers/model; stored content; advisory; later requests | see [EPI-RTE-wiki-maintenance](#epi-rte-wiki-maintenance) | none | none | Exact [[target]] replacement only; display-text variants remain unmatched in this branch. Semantic equivalence for fuzzy remapping remains unassessed. |
| [EPI-RTE-wiki-maintenance](#epi-rte-wiki-maintenance) | lineage/freshness/recovery | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) SourceRefs | non-truth-apt policy/content update: source-reference withdrawal | stale source reference on multi-source page | AutoFix lookup and remaining-source count; existence domain | see [EPI-RTE-wiki-maintenance](#epi-rte-wiki-maintenance) | metadata removed, prose not rewritten by this branch | see [EPI-RTE-wiki-maintenance](#epi-rte-wiki-maintenance) | Removes lineage to unavailable source; does not refute or re-ground the retained prose | Changes source drill-down without necessarily changing factual content | Wiki clients/model; stored refs; enforcing lineage selection; later requests | see [EPI-RTE-wiki-maintenance](#epi-rte-wiki-maintenance) | none | none | Separate model retract route attempts content withdrawal; source lookup failures can be classified as stale. |
| [EPI-RTE-wiki-maintenance](#epi-rte-wiki-maintenance) | disposition/acceptance | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) status/existence | non-truth-apt policy/content update: page withdrawal | short non-index page or stale sole-source page | AutoFix size and source-count rules; availability domain | see [EPI-RTE-wiki-maintenance](#epi-rte-wiki-maintenance) | archived or deleted | see [EPI-RTE-wiki-maintenance](#epi-rte-wiki-maintenance) | Withholds page availability, not a truth judgment | Removes page from normal availability according to service status/deletion semantics | Wiki services/readers; repository status/deletion; enforcing; later requests | see [EPI-RTE-wiki-maintenance](#epi-rte-wiki-maintenance) | none | none | Every downstream backend's status filtering and recovery semantics remain uninspected. |
| [EPI-RTE-dataset-metrics](#epi-rte-dataset-metrics) | check/evidence production | implemented | [EPI-OBJ-metric-result](#epi-obj-metric-result) | truth-apt transformation: entailed derivation | supplied QA pairs, mapped result IDs and generated text | HookMetric plus deterministic calculators; dataset/reference-relative domain | see [EPI-RTE-dataset-metrics](#epi-rte-dataset-metrics) | metric vector | see [EPI-RTE-dataset-metrics](#epi-rte-dataset-metrics) | Scores follow encoded inputs, not warranted source truth; denominator limited by mapping | Exposed result for caller comparison, no automatic successor admission | Evaluation caller; in-process task metric; advisory; task lifetime | see [EPI-RTE-dataset-metrics](#epi-rte-dataset-metrics) | [EPI-CLM-end-evaluation](#epi-clm-end-evaluation) | none | Unmatched chunks disappear from mapped IDs. Source fidelity, full metric formulas and observed measurements remain unestablished. |

No lifecycle-integration row is inferred from mere retention or operational consumption. The inspected content-write paths do not record an evidence-consuming acceptance decision naming a truth criterion, intended use and scope; this is a bounded finding about these paths, not a system-wide absence. Setup image admission has a distinct operational acceptance criterion. Wiki issue tools and other evaluators remain uninspected as recorded above.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-evidence-verification](runtime.md#rt-clm-evidence-verification) | see record | see record | Prompt asks source verification | [RT-RTE-agent-turn](runtime.md#rt-rte-agent-turn), [RT-RTE-mcp-call](runtime.md#rt-rte-mcp-call) | None registered | None; schema/approval do not check exact quotation truth | Verification is requested; source-reading tools are afforded | Actual verification and entailment unobserved; not an executable universal guarantee |
| [EPI-CLM-cited-answers](#epi-clm-cited-answers) | see record | see record | Source-cited QA intent | [RT-RTE-rag-answer](runtime.md#rt-rte-rag-answer) | None registered | None; ordinary QA has no reference oracle | Retrieval and answer supply wired | Whether every displayed citation supports its associated proposition remains unknown |
| [EPI-CLM-automatic-wiki](#epi-clm-automatic-wiki) | see record | see record | Generated/editable/wiki rollback intent | [EPI-RTE-wiki-rewrite](#epi-rte-wiki-rewrite), [EPI-RTE-wiki-guard](#epi-rte-wiki-guard), [EPI-RTE-wiki-maintenance](#epi-rte-wiki-maintenance) | None registered | None; rollback restores content fields, not historical provenance/placement; maintenance can bypass visible version bump | Model-assisted pages, source bookkeeping, bounded write veto and revision revert implemented | Literal “every change” is broader than inspected revert coverage; structural checks do not certify factual claims |
| [EPI-CLM-end-evaluation](#epi-clm-end-evaluation) | see record | see record | Recall/BLEU/ROUGE evaluation intent | [RT-RTE-dataset-evaluation](runtime.md#rt-rte-dataset-evaluation), [EPI-RTE-dataset-metrics](#epi-rte-dataset-metrics) | None registered | None; no intervention/component comparison; fixed evaluation RAG differs from open agent | Reference-relative metrics wired and exposed | Content mapping can hide unmatched retrievals; lexical similarity is not answer truth or mechanism validation |

## Bounded conclusion

WeKnora acquires documents and uses indexed content as model evidence; indexing/enablement is availability rather than truth acceptance ([RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission)). Source warrant and parsing fidelity remain unknown. RAG and ReAct produce candidate answers, but no actual answer instance here supports an entailment or non-entailment judgment. Model summaries and wiki rewrites likewise remain semantically indeterminate. Fluency and citations alone license no additional truth claim.

Memory is a materially different reliance route. The extraction prompt permits inferences and explicitly illustrates an ampliative user guess. The model-supplied inferred flag can hold that candidate pending; non-inferred extracted content can become active automatically. Confirmation/rejection changes recall eligibility and rejection can persist a tombstone. This defeats a blanket claim that all memory writes take effect silently, but it does not establish evidence-certified acceptance: the service records the caller action, not the evidence or truth criterion. Active memories are selected into later prompt/tool results ([EPI-RTE-memory-extraction](#epi-rte-memory-extraction), [EPI-RTE-memory-write](#epi-rte-memory-write), [EPI-RTE-memory-review](#epi-rte-memory-review), [EPI-RTE-memory-recall](#epi-rte-memory-recall)). Capacity, conflict, credential and forgotten-content checks constrain retention independently of truth. Flag fidelity, failed tombstones and cached-block fallback bound withdrawal guarantees.

Wiki generation and retraction receive source chunks, summaries, existing content and deleted/remaining source information. References provide navigable lineage but not an independent proposition-level oracle. Table identity preservation can veto a machine rewrite, while deliberate retract, user and revert operations have exceptions. Lint availability/size checks can drive text cleanup, metadata withdrawal, archival or deletion. Those are consequential maintenance checks, not factual acceptance. A multi-source stale-ref AutoFix may leave prose unchanged, unlike the separate model-directed retract route. Revert restores selected revision content while retaining current provenance and placement ([EPI-RTE-wiki-rewrite](#epi-rte-wiki-rewrite), [EPI-RTE-wiki-guard](#epi-rte-wiki-guard), [EPI-RTE-wiki-maintenance](#epi-rte-wiki-maintenance)). No evidence-consuming lifecycle integration is inferred merely from these edits.

The dataset evaluator derives numbers from encoded inputs and reference answers. Its operative target is retrieval IDs and lexical response similarity over supplied pairs, not general correctness, source truth or producing mechanism. The content-to-passage map drops unmatched retrieved chunks before precision computation, so an all-relevant mapped subset need not mean all actual returned chunks were relevant. Metrics reach the result caller; no automatic accepted successor is established in this path ([EPI-RTE-dataset-metrics](#epi-rte-dataset-metrics)).

Execution authority has separate scopes. MCP approvals authorize effects, and skill verification gates a durable environment under dependency/tree/script criteria. Neither certifies every generated claim. Skill image admission can change later capabilities; exercised self-improvement and successful learning require later-operation and improvement evidence not supplied here ([RT-RTE-skill-install](runtime.md#rt-rte-skill-install), [RT-BAP-skill-image](runtime.md#rt-bap-skill-image)). Trace-fed memory can alter later model input without proving improved capacity. Theory formulation, content-directed criticism, reflection and autonomy are not inferred from persistence, repair or ranking; issue-tool and other uninspected branches prevent complete negatives. Model weight mutability/version/endpoint limits remain component-local in the runtime records. All implemented routes remain operationally unobserved, and no causal benefit comparison is registered.

## Shared records

### Operative objects

#### EPI-OBJ-knowledge-chunks
Label: Indexed document chunks

Source-native identity: document text chunks produced through parsing/indexing. Form: natural-language source content, with symbolic knowledge identifiers and enablement controlling retrieval; numerical vectors are separate retrieval representations. Substrate: source storage and chunk/index repositories. No supplied operative-object counterpart: [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission) declares the producer/admission route, not this content object. SRC-1, `internal/application/service/knowledge_process.go`; minimum enablement passage and read-back witness are see that supplied record. Additional direct witness: `internal/application/service/wiki_ingest.go` reconstructContent filters text chunks and merges them; `internal/application/service/wiki_ingest_batch.go` resolves cited chunk content for the wiki editor. Chunk content is acquired source material; fidelity and source warrant remain unresolved.

#### EPI-OBJ-chat-response
Label: ChatResponse candidate content

Source-native identity: types.ChatResponse.Content produced by configured chat inference. Form: natural-language answer or other model content; protocol FinishReason is a separate symbolic usability input. Substrate: transient Go response, with answers subsequently stored in conversation history by application callers. No supplied object counterpart: [RT-RTE-rag-answer](runtime.md#rt-rte-rag-answer) and [RT-RTE-agent-turn](runtime.md#rt-rte-agent-turn) own distinct production/consumption routes, not a shared output object declaration. SRC-1, `internal/application/service/metric_hook.go`, reads chatResponse.Content for generation metrics; `internal/application/service/memory/extract.go` reads Content and FinishReason for extraction usability. Supplied runtime records establish ordinary answer output and persistence. Exact actual truth-apt claims cannot be individuated from implementation alone.

> generatedTexts = h.qaPairMetricList[index].chatResponse.Content
> --- `internal/application/service/metric_hook.go`

#### EPI-OBJ-context-checkpoint
Label: Context summary checkpoint

Source-native identity: eligible compaction summary checkpoint replacing covered conversation context. Form: natural-language summary with symbolic checkpoint coverage/read-back selection. Substrate: message repository through caller-installed checkpoint sink. No supplied object counterpart: [RT-RTE-context-rewrite](runtime.md#rt-rte-context-rewrite) owns transformation, persistence and later read-back, not this output-object declaration. SRC-1, `internal/application/service/session_agent_qa.go`, `internal/agent/compaction/compactor.go`; minimum checkpoint-sink quotation and summary-selection findings are see the supplied route. Eligibility to persist and budget reduction do not test semantic preservation. Raw fallback and transient previews are alternate current-context representations, not evidence of a correct accepted summary.

#### EPI-OBJ-memory-item
Label: MemoryItem claim and status

Source-native identity: types.MemoryItem, including natural-language Content and Topic and separately symbolic Origin, Status, source IDs and expiry. Substrate: memory repository rows; dense embeddings are separate selection material. Distinct from the supplied runtime's prompt/config objects: a durable per-subject claim source, later selected into [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt), not the prompt container itself. SRC-1, `internal/application/service/memory/service.go`, `internal/application/service/memory/extract.go`. Model extraction proposes Content and Inferred; write stores status and source IDs. Source linkage is lineage, not a verified entailment.

> Status:          statusForWrite(item),
> SourceSessionID: item.SourceSessionID,
> SourceMessageID: item.SourceMessageID,
> --- `internal/application/service/memory/service.go`

#### EPI-OBJ-wiki-page
Label: WikiPage content and provenance

Source-native identity: types.WikiPage natural-language Title/Content/Summary; symbolic SourceRefs, ChunkRefs, status, links and version have distinct fixed consumers. Substrate: wiki service repository, with revision snapshots. No supplied object counterpart: the closest [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission) concerns indexed document state, not generated wiki pages. SRC-1, `internal/application/service/wiki_ingest_batch.go`, `internal/application/service/wiki_page.go`. Summary pages have document-level refs but clear chunk refs; entity/concept addition rounds merge chunk refs. Neither establishes that every proposition follows from those refs.

> page.ChunkRefs = types.StringArray{}
> changed = true
> --- `internal/application/service/wiki_ingest_batch.go:2027-2033`

#### EPI-OBJ-metric-result
Label: MetricResult evaluation vector

Source-native identity: types.MetricResult retrieval/generation metrics. Form: symbolic numeric measurements interpreted through fixed calculator rules, not distributed model weights. Substrate: MetricList and evaluation task's in-process storage. No supplied object counterpart; produced inside [RT-RTE-dataset-evaluation](runtime.md#rt-rte-dataset-evaluation). SRC-1, `internal/application/service/metric_hook.go`, `internal/application/service/evaluation.go`.

> params.Metric = metricHook.MetricResult()
> params.Task.Finished = finished
> --- `internal/application/service/evaluation.go`

### Routes

#### EPI-RTE-memory-extraction
Label: Background memory extraction

Distinct from foreground [RT-RTE-agent-turn](runtime.md#rt-rte-agent-turn): asynchronous maintenance with a separate model request, JSON decisions and write consumer; no supplied route counterpart. Owner: memory Service. Progression: selected transcript plus existing/forgotten/topic context → chat model → truncation/JSON handling → applyDecisions.

SRC-1 implementation, `internal/application/service/memory/extract.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Parsed decisions or extraction error.
- Later read-back: Decision content can enter memory through [EPI-RTE-memory-write](#epi-rte-memory-write); temporary model context itself is not retained.
- Delegated visibility: Model gets segment, existing notes, forgotten notes/topics and workspace extraction instructions; foreground does not receive this whole temporary frame.
- Selection predicate: Configured extraction model; isTruncated retries once; malformed output rejected.
- Invalidation or expiry: Error prevents usable extraction result; per-item invalid target/action can be skipped. Full scheduling/watermark recovery not inspected.
- Activation or effect: Implemented proposal of memory addition, replacement, supersession; no observed output.
- Evidence limits: Semantic equivalence and correct source indexing not guaranteed by valid JSON; model processing opaque.

Open transcript distillation, not an experiment. Model proposes and can mark Inferred; code rejects unusable output, without an expected-answer oracle. Guidance names durable user notes, prohibits credentials and requests source-line IDs. The prompt example gives explicit non-entailment evidence: asking about ceremonies/venues does not entail organising events. For that candidate class the relation is ampliative conjecture; unobserved actual decisions remain indeterminate. Temporary summarizer-like work frame returns decisions by value; stored notes are later selected separately, not live references to the discarded frame.

> - Set "inferred" to true when you are deducing something about the user rather
>   than repeating what they said — for example concluding from questions about
>   award ceremonies and venue clearing that they organise events. Such entries
>   are shown to the user for confirmation instead of taking effect silently, so
>   a reasonable guess is welcome; a confident assertion is not.
> --- `internal/application/service/memory/extract.go`

#### EPI-RTE-memory-write
Label: Memory write admission

No supplied route counterpart; follows [EPI-RTE-memory-extraction](#epi-rte-memory-extraction) and also handles explicit/manual inputs. Owner: memory Service. Progression: content/policy checks → conflict/duplicate selection → SaveItem → capacity/block/embedding updates.

SRC-1 implementation, `internal/application/service/memory/service.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Stored/unchanged item, rejected sensitive/forgotten/conflicting candidate, or error.
- Later read-back: Repository rows and rendered block can reach [EPI-RTE-memory-recall](#epi-rte-memory-recall).
- Delegated visibility: Embedding subsystem receives stored claim; foreground later sees selected rendered text, not write checks.
- Selection predicate: Nonempty content; redaction and tombstone rules; inferred non-explicit/non-manual claims pending, other claims active.
- Invalidation or expiry: Save replaces target where selected; capacity can archive; expiry stored. Exact repository transaction semantics uninspected.
- Activation or effect: Active/pending retention and block rebuild wired; best-effort embedding does not gate save.
- Evidence limits: Model flag can misclassify an inference; policy checks do not evaluate truth.

Trigger: explicit/manual input or extracted decision. Input supplier proposes; code decides status and can reject; not per-content human approval on extraction. No expected-answer oracle. Admission criteria are policy/usability, intended use later recall over the user subject. Pending claims are retained but withheld from active-query consumers until confirmation. Checks do not prove source truth. Failed extraction writes can skip selected policy errors and preserve other decisions.

> func statusForWrite(item types.MemoryItem) string {
> 	if item.Inferred && item.Origin != types.MemoryOriginExplicit && item.Origin != types.MemoryOriginManual {
> 		return types.MemoryStatusPending
> 	}
> 	return types.MemoryStatusActive
> }
> --- `internal/application/service/memory/service.go`

> if forgotten {
> 	logger.Infof(ctx, "memory: skipped a statement the user previously deleted")
> 	return nil, ErrPreviouslyForgotten
> }
> --- `internal/application/service/memory/service.go`

#### EPI-RTE-memory-review
Label: Memory confirmation and rejection

Distinct subsequent caller decision, not extraction or [RT-RTE-mcp-call](runtime.md#rt-rte-mcp-call) effect approval. Owner: memory Service behind POST confirm/reject endpoints in SRC-1, `internal/router/routes_memory.go`. Progression: scoped lookup → confirm pending/rebuild or DeleteItem/tombstone → later recall/write eligibility.

SRC-1 implementation, `internal/application/service/memory/service.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Confirmed item or deletion/error.
- Later read-back: Confirmation activates stored claim; rejection removes row and records forgotten fingerprint/source for future write checks.
- Delegated visibility: inapplicable — no model is called for confirmation/rejection; later recall is separate.
- Selection predicate: Resolved caller scope and existing item; confirmation calls repository ConfirmPendingItem.
- Invalidation or expiry: Delete adds tombstone before removal; tombstone failure logs warning but deletion proceeds.
- Activation or effect: Status change/removal shapes later eligibility, not observed human deliberation or changed answer.
- Evidence limits: Principal may be software; service does not retain evidence consumed or named truth criterion. Repository pending-state preconditions not fully inspected.

Caller chooses confirm/reject, code performs it. Open memory-manager use, no expected-answer oracle. Rejection has operative force, but deletion with failed tombstone prevents an absolute no-reappearance guarantee. Human endorsement is possible, not established by endpoint invocation.

> if err := s.repo.ConfirmPendingItem(ctx, scope, id); err != nil {
> 	return nil, err
> }
> --- `internal/application/service/memory/service.go`

> if err := s.repo.AddTombstone(
> 	ctx, scope, existing.Topic, types.MemoryFingerprint(existing.Content), existing.SourceMessageID,
> ); err != nil {
> 	logger.Warnf(ctx, "memory: record tombstone failed: %v", err)
> }
> --- `internal/application/service/memory/service.go`

#### EPI-RTE-memory-recall
Label: Memory prompt and search consumption

Distinct stored-claim selection route supplying [RT-RTE-agent-turn](runtime.md#rt-rte-agent-turn) and [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt). Owner: memory Service. Progression: enabled scope → active resident/situational queries → rank/budget/render → prompt or search result → foreground model; supplied boundary establishes caller SetMemoryPrompt.

SRC-1 implementation, `internal/application/service/memory/service.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Recall.Prompt/Items; SearchMemory result in SRC-1, `internal/application/service/memory/search.go`.
- Later read-back: Later invocations select retained active notes; touchAsync changes usage metadata.
- Delegated visibility: Foreground receives rendered selected notes, not complete memory repository, tombstones or pending list.
- Selection predicate: Resident interests query-selected; active fact/task candidates and lexical/semantic selection with item/rune budgets.
- Invalidation or expiry: Superseded/archived items excluded from inspected active queries; block cache fallback exists on empty rendering. Full failure-path cache invalidation uninspected.
- Activation or effect: Delivered memory has advisory prompt/tool-result force; actual obedience/benefit unobserved.
- Evidence limits: Ranking checks relevance not truth; vector internals and every expiry/cache branch uninspected.

Open queries with no reference answer. Code chooses delivery; model may request SearchMemory. Normal active selection withholds pending claims; cache fallback bounds any universal withdrawal claim. Usage updates establish access bookkeeping, not an evaluation reward for correct beliefs.

> situational, err := s.repo.ListActiveByKinds(recallCtx, scope,
> 	[]string{types.MemoryKindFact, types.MemoryKindTask}, lexicalPoolSize(cfg))
> --- `internal/application/service/memory/service.go`

> prompt := types.WrapMemoryForPrompt(block, types.RenderMemoryRecall(matched))
> --- `internal/application/service/memory/service.go`

#### EPI-RTE-wiki-rewrite
Label: Wiki page generation and retraction

Distinct from [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission) indexed-document enablement and [RT-RTE-agent-turn](runtime.md#rt-rte-agent-turn) foreground loop. Owner: wikiIngestService/wiki page service. Progression: additions/retracts plus existing page → cited chunks/summary and source bookkeeping → template model call → decode/body split → guarded CreatePage/UpdatePage.

SRC-1 implementation, `internal/application/service/wiki_ingest_batch.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Updated page/change flags, deferred write or generation failure.
- Later read-back: Generated body and document/chunk refs persist; registered wiki read/search tools consume pages later (SRC-1, `internal/application/service/agent_service.go`).
- Delegated visibility: Editor gets existing page, source contexts, new/deleted/remaining source content and available link handles; summary context is not equivalent to every raw source passage.
- Selection predicate: Entity/concept additions or retract/retractStale; summary branch stores document synopsis separately.
- Invalidation or expiry: Retraction removes deleted-source refs and requests content removal; generation errors can leave current content. Guard can defer.
- Activation or effect: Body/ref changes are implemented, not observed correct source-preserving synthesis.
- Evidence limits: Actual generated propositions unobserved; partial source context and merged refs cannot prove each sentence grounded.

Worker/model proposes change; code can reject generation or guarded write. Guidance: WikiPageModifyUserPrompt, workspace ContentInstructions scoped to wiki_content and source blocks. No expected page/answer oracle. Open source-driven maintenance. Retention comes after structural admission, not epistemic acceptance. Intentional retractions pass WithWikiShrinkAllowed. Recovery/retry budget details beyond deferred result remain supplied/uninspected.

> updatedContent, err = s.generateWithTemplate(ctx, chatModel, agent.WikiPageModifyUserPrompt, map[string]string{
> 	"HasAdditions":            hasAdditionsStr,
> 	"HasRetractions":          hasRetractionsStr,
> --- `internal/application/service/wiki_ingest_batch.go`

> page.SourceRefs = newRefs
> --- `internal/application/service/wiki_ingest_batch.go`

> page.ChunkRefs = mergeChunkRefs(page.ChunkRefs, additions)
> --- `internal/application/service/wiki_ingest_batch.go`

#### EPI-RTE-wiki-guard
Label: Wiki rewrite preservation gate

Distinct check/disposition at page write, compared with [RT-RTE-skill-install](runtime.md#rt-rte-skill-install): both can veto changes but this checks stored table row identity loss, not dependency availability. Owner: wikiPageService.UpdatePage → explicit error consumed by ingest and agent writer.

SRC-1 implementation, `internal/application/service/wiki_page.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Write refusal with ErrWikiWriteDroppedTableRows, or normal update.
- Later read-back: Refusal preserves prior body; ingest deferred result retains documents for later batch. Revisions support later content revert.
- Delegated visibility: Caller/model can receive refused-write explanation; no separate truth evaluator is invoked.
- Selection predicate: Machine edit source without deliberate shrink flag; missing identities and source-specific loss tolerance.
- Invalidation or expiry: User/revert/intentional-shrink exemptions; identity preservation does not constrain all cell changes.
- Activation or effect: Gate blocks a bounded set of rewrites and permits others; operation unobserved.
- Evidence limits: Internal row identity helper/tolerance values not fully inspected; no guarantee of full table semantics.

Worker/agent supplies candidate, code can veto. Existing content is the preservation reference, not an independently warranted answer oracle. Ingest classifyWikiPageWrite consumes the sentinel as deferred, not successful version change. Revert restores Title/Content/Summary/PageType/Status/Aliases, retaining current placement/provenance. This is bounded recovery, not every-change rollback.

> source := types.WikiEditSourceFromContext(ctx)
> if source != types.WikiEditSourceUser && source != types.WikiEditSourceRevert &&
> 	!types.WikiShrinkAllowedFromContext(ctx) {
> --- `internal/application/service/wiki_page.go`

> return nil, fmt.Errorf(
> 	"%w: slug %s lost %d of %d table row identities (e.g. %s); the stored page is unchanged",
> 	ErrWikiWriteDroppedTableRows, page.Slug, len(missing), storedIdentities, examples)
> --- `internal/application/service/wiki_page.go`

> if errors.Is(updateErr, ErrWikiWriteDroppedTableRows) {
> 	return true, nil
> }
> --- `internal/application/service/wiki_ingest_batch.go`

> target.Content = rev.Content
> --- `internal/application/service/wiki_page.go`

#### EPI-RTE-wiki-maintenance
Label: Wiki structural lint and cleanup

No supplied counterpart; separate structural maintenance alongside [EPI-RTE-wiki-rewrite](#epi-rte-wiki-rewrite). Owner: WikiLintService. Progression: live-slug/source/content probes → issues → AutoFix → page edits/archive/delete → RebuildLinks.

SRC-1 implementation, `internal/application/service/wiki_lint.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Lint report or fix count/error.
- Later read-back: Persistent fixes shape wiki later availability and references; no retained acceptance rationale for factual claims established.
- Delegated visibility: Operator gets report; AutoFix program consumes fixable issue type and target.
- Selection predicate: Broken-link, short-content and stale-source conditions; not every lint issue is automatically fixable.
- Invalidation or expiry: Stale source can delete sole-source page or remove metadata when other sources remain; short pages archived except index.
- Activation or effect: Code-generated structural results have direct maintenance consumers; factual evaluation not implied.
- Evidence limits: Lint “health” is structural; source lookup errors can classify refs stale; partial stale-ref cleanup need not remove unsupported prose.

Caller triggers maintenance; code proposes/decides fixable updates and may skip failed pages. No reference factual answer. Concrete implementation deduction without target execution: with TargetSlug ghost and Content "See [[ghost]].", ReplaceAll produces "See ghost." and UpdateAutoLinkedContent persists on success. With "See [[ghost|label]].", that exact replacement leaves text unchanged, though a successful write can increment fixed. Separate stripDeadWikiLinks branch in SRC-1, `internal/application/service/wiki_ingest.go`, handles display labels and fuzzy resolution, whose helper equivalence is uninspected. Cleanup preserves prose in the exact plain-text branch, but withdrawing stale references changes lineage. RebuildLinks follows positive fix count; no universal semantic repair follows.

> target := issue.TargetSlug
> page.Content = strings.ReplaceAll(page.Content, "[["+target+"]]", target)
> if err := s.wikiService.UpdateAutoLinkedContent(ctx, page); err == nil {
> 	fixed++
> }
> --- `internal/application/service/wiki_lint.go`

> if len(remaining) == 0 {
> 	if err := s.wikiService.DeletePage(ctx, kbID, page.Slug); err == nil {
> 		fixed++
> 	}
> } else if len(remaining) != len(page.SourceRefs) {
> 	page.SourceRefs = remaining
> --- `internal/application/service/wiki_lint.go`

#### EPI-RTE-dataset-metrics
Label: Dataset reference metric calculation

Material metric-computation part of supplied evaluation route, not a duplicate of its whole request/KB/pipeline lifecycle. Owner: HookMetric/MetricList; progression: QA pair + selected retrieved content + response → passage-ID mapping → calculators → task Metric result.

SRC-1 implementation, `internal/application/service/metric_hook.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Per-pair scores and mean metric vector.
- Later read-back: In-process result lookup described in parent route; durable cross-restart retention unestablished.
- Delegated visibility: Calculators receive mapped IDs, reference IDs, generated text and reference answer; no new judging model call here.
- Selection predicate: Prefer rerank result when nonempty, otherwise search; skip empty chunks/passages; first substring containment match maps PID and duplicate IDs collapse.
- Invalidation or expiry: uninspected — parent in-process task lifetime/cleanup not fully traced; immutable references do not establish their truth.
- Activation or effect: Computed numbers exposed through evaluation.go task update; no automatic successor admission in inspected consumer.
- Evidence limits: Unmatched result disappears before metric denominator. Remaining calculator formulas/reference fidelity uninspected; no runs or causal experiments.

Part of: [RT-RTE-dataset-evaluation](runtime.md#rt-rte-dataset-evaluation)

Dataset provider supplies oracle QA pairs/PIDs/answer; code selects and computes, caller interprets. Bounded dataset mode. Precision domain is mapped PIDs, not all original retrievals. Implementation deduction: given one exact relevant chunk plus one unrelated unmatched chunk, mapping retains only the relevant PID; PrecisionMetric divides one hit by one mapped ID, yielding 1, not precision over both returned chunks. This follows inspected mapping and denominator, not an executed test. BLEU compares normalized text n-grams; semantic truth is beyond its licensed domain. No evidence-consuming acceptance/automatic optimization trigger in exposed task-metric consumer.

> if strings.Contains(passage, r.Content) || strings.Contains(r.Content, passage) {
> 	pid := qaPair.PIDs[i]
> --- `internal/application/service/metric_hook.go`

> totalPrecision += float64(hits) / float64(len(ids))
> --- `internal/application/service/metric/precision.go`

> candidate := splitIntoWords(splitSentences(metricInput.GeneratedTexts))
> references := []Sentence{splitIntoWords(splitSentences(metricInput.GeneratedGT))}
> --- `internal/application/service/metric/bleu.go`

> params.Metric = metricResult
> params.Task.Finished = finished
> --- `internal/application/service/evaluation.go`

### Claims

#### EPI-CLM-cited-answers
Label: Source-cited quick QA

Claimed operation: README claims quick QA answers from knowledge base with cited sources. Distinct from [RT-CLM-evidence-verification](runtime.md#rt-clm-evidence-verification) exact-evidence instruction; this is a public answer-consumption claim. SRC-1 doctrine/design, `README.md`. Conclusion status: claimed.

> **Two ways to ask.** Quick Q&A answers from the knowledge base with RAG and cites the sources it used. In smart reasoning the agent plans multi-step work, searching, reading documents and calling tools and skills, and shows each step in the conversation. [Docs →](https://weknora.weixin.qq.com/docs/03-features/18-chat-experience)
> --- `README.md`

#### EPI-CLM-automatic-wiki
Label: Automatic wiki and rollback

Claimed operation: README claims source-cited generated pages, editable with every change reversible. No supplied claim counterpart; distinct from foreground exact-evidence policy. SRC-1 doctrine/design, `README.md`. Conclusion status: claimed.

> **Documents organized into a browsable wiki.** With Wiki enabled, WeKnora extracts people, products and concepts from knowledge-base documents into pages with source citations, organized by directory. The knowledge graph shows how pages relate; pages can be edited directly and every change can be rolled back. [Docs →](https://weknora.weixin.qq.com/docs/03-features/14-wiki)
> --- `README.md`

#### EPI-CLM-end-evaluation
Label: End-to-end retrieval evaluation

Claimed operation: README claims end-to-end evaluation with recall and BLEU/ROUGE. No supplied claim counterpart; [RT-RTE-dataset-evaluation](runtime.md#rt-rte-dataset-evaluation) is implementation, not the public claim. SRC-1 doctrine/design, `README.md`. Conclusion status: claimed.

> | [Retrieval](https://weknora.weixin.qq.com/docs/03-features/05-retrieval-engines) | Keyword + vector hybrid search, rerank, parent-child chunking and GraphRAG ([Neo4j](https://weknora.weixin.qq.com/docs/03-features/09-knowledge-graph)); end-to-end evaluation with recall and BLEU / ROUGE |
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; route records name their consumers/channels/force/horizons and the supplied runtime owns [RT-BAP-prompt-instructions](runtime.md#rt-bap-prompt-instructions) and [RT-BAP-skill-image](runtime.md#rt-bap-skill-image).
