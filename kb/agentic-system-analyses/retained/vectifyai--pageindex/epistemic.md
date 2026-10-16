---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "PageIndex's document evidence, structural checks, summary admission and answer authority at the frozen revision."
run-id: AAS-2026-10-15-pageindex-50056ef72767-01
reviewed-boundary: af92d9658a6a9c0ae31171b43198db28951af2f4
---

# PageIndex epistemic report

## Source-and-claim boundary

The question is how PageIndex turns imported documents into retained navigation and later answers, and which checks license reliance on each product. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence). Evidence identities and layers: see the [Source register](boundary.md#source-register). All additional source reads below use SRC-1 at that same revision. No target execution, tests, live services, supplied execution traces or causal experiments establish operation or benefit.

The public warrant claims are [EPI-CLM-tree-retrieval](#epi-clm-tree-retrieval), [EPI-CLM-benchmark-results](#epi-clm-benchmark-results) and [EPI-CLM-cited-grounding](#epi-clm-cited-grounding); extraction's narrower model-free claim is [RT-CLM-layout-extraction](runtime.md#rt-clm-layout-extraction). These are heterogeneous claims, not a general claim that storing text certifies knowledge.

### Coverage

“Direct” denotes source inspected for this member; “supplied” denotes the runtime finding, not independent source inspection. Coverage is functional, not an exhaustive source audit.

| Entry point or operation | Source path in SRC-1 | Coverage and records, or limit |
|---|---|---|
| Local PDF submit and store admission | `pageindex/local_api.py`, `pageindex/local_store.py` | Direct extraction/check/save/getter branches and complete store; [RT-RTE-local-submit](runtime.md#rt-rte-local-submit), [EPI-RTE-document-withdrawal](#epi-rte-document-withdrawal). |
| Flash layout tree, fallback and bookmarks | `pageindex/flash/main.py`, `pageindex/flash/api.py`, `pageindex/flash/embedded_toc.py` | Direct main orchestration; supplied wrapper/refinement [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine). Embedded-TOC function inventory searched; deep bookmark reconciliation, heading and layout predicates remain uninspected here. Prevents an exhaustive judgment of structural fidelity or every heuristic evaluator. |
| Expansion proposal/check/cost admission and optimizer CLI | `pageindex/tree_optimize.py` | Direct model proposal, cache candidate construction, shared ownership filter, expansion selection, CLI dispatch/writer; supplied merge/formula/scheduler [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine), [RT-OBJ-cost-policy](runtime.md#rt-obj-cost-policy). New-issue reporting is not a write veto in the CLI. |
| Summary, retitling, fallback and description | `pageindex/utils.py` | Direct scheduler leaf/parent/finish, normalization and mapping; searched summary/description helpers; [EPI-OBJ-node-summary](#epi-obj-node-summary), [EPI-OBJ-doc-description](#epi-obj-doc-description). Description helper details remain supplied through [RT-RTE-local-submit](runtime.md#rt-rte-local-submit); no measured fidelity. |
| Classic TOC extraction, sanitization, verification, repair/fallback | `pageindex/page_index_classic.py` | Direct sanitizer, appearance evaluator, verification denominator and meta-processor disposition; supplied remaining generation/repair [RT-RTE-alternate-builders](runtime.md#rt-rte-alternate-builders). |
| Markdown heading/text construction and optional model passes | `pageindex/page_index_md.py`, `run_pageindex.py` | Direct heading extraction and node-text slicing, summary short-text branch and CLI routing/writing; supplied thinning/tree construction [RT-RTE-alternate-builders](runtime.md#rt-rte-alternate-builders). Uninspected thinning details prevent complete semantic-preservation judgment. |
| Local registered tools: browse/get metadata/structure/pages/remove | `pageindex/agent_tools.py` | Direct registered operation map, page delivery, remover and managed/citation prompts; supplied discovery/structure dispatch [RT-RTE-document-chat](runtime.md#rt-rte-document-chat). Local semantic ranking explicitly unavailable in searched source; model compares metadata instead. |
| SDK tree/page/structure helpers and citation utilities | `pageindex/client.py`, `pageindex/utils.py` | Direct getter dispatch, cloud-only block/image/retrieval gates, citation resolver and tree normalizer; [EPI-RTE-tree-normalization](#epi-rte-tree-normalization), [EPI-RTE-citation-resolution](#epi-rte-citation-resolution). |
| Chat, Chat Completions, Responses, Messages and streams | `pageindex/client.py`, `pageindex/local_chat.py`, `pageindex/chat_stream.py` | Supplied [RT-RTE-document-chat](runtime.md#rt-rte-document-chat), [RT-RTE-protocol-history](runtime.md#rt-rte-protocol-history). These are provisional implementation findings; not independently re-read end to end here. Prevents an independent whole-driver audit. |
| Cloud HTTP/MCP and exposed remote operations | `pageindex/cloud_api.py`, `pageindex/mcp_bridge.py`, `pageindex/client.py`, `pageindex/agent_tools.py` | Direct endpoint inventory and client getter/query gates; supplied [RT-RTE-cloud-tools](runtime.md#rt-rte-cloud-tools). Includes deprecated submit-query/get-retrieval, remote block/image reads, document/folder operations and managed chat. Server algorithms, current catalogs, OCR and acceptance policy unavailable; prevents characterizing remote warrant. Folder bookkeeping is not itself a truth check. |
| Adapter/hosted tool grants | `pageindex/integrations/openai_agents.py`, `pageindex/integrations/anthropic_sdk.py`, `pageindex/integrations/claude_agent_sdk.py` | Supplied [RT-RTE-framework-tools](runtime.md#rt-rte-framework-tools). No independent host-loop or dependency audit. |
| Six notebooks, including separate image answering | `cookbook/pageindex-vision-rag.ipynb`, `cookbook/` | Supplied boundary coverage and [RT-RTE-vision-notebook](runtime.md#rt-rte-vision-notebook). Embedded outputs not admitted as observed runs; other notebook paths remain supplied coverage only. |
| Benchmarks, tests and examples | `README.md`, `tests/`, `examples/`, `assets/` | Direct README claims; supplied boundary inventory. Test bodies/fixtures, example results and image pixels not independently assessed here. External runners/data unavailable. Prevents a measured QA verdict or inference that examples establish route execution. |

This assessment therefore does not assert a system-complete absence of evaluators, learning or acceptance. Provider parameters are separately scoped by [RT-CMP-index-model](runtime.md#rt-cmp-index-model), [RT-CMP-summary-model](runtime.md#rt-cmp-summary-model), [RT-CMP-chat-model](runtime.md#rt-cmp-chat-model) and [RT-CMP-vision-model](runtime.md#rt-cmp-vision-model): operation-time inference is wired, parameter updates are not wired in the inspected helpers, versions are not pinned, endpoints can resolve differently, and provider-internal learning remains uninspected.

## Epistemic-object inventory

Fields owned by a declaring record are supplied there, not redefined here. Content is truth-apt when it asserts document content, location or an answer; a routing instruction is not itself an answer claim.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-page-text](#epi-obj-page-text) | Imported statements on numbered pages | See record | SRC-1 `pageindex/local_api.py` | Extraction is not source endorsement or OCR. |
| [EPI-OBJ-tree-structure](#epi-obj-tree-structure) | Titles, hierarchy and page-location assertions | See record | SRC-1 `pageindex/tree_optimize.py` | Structural checks do not certify topic completeness. |
| [EPI-OBJ-node-summary](#epi-obj-node-summary) | Descriptions of section content; sometimes raw text | See record | SRC-1 `pageindex/utils.py` | Raw reuse and generated descriptions have different warrant. |
| [EPI-OBJ-doc-description](#epi-obj-doc-description) | One-sentence document characterization | See record | SRC-1 `pageindex/local_api.py` | Generation uses an already compressed tree. |
| [EPI-OBJ-answer-text](#epi-obj-answer-text) | Answer propositions over the user's question | See record | SRC-1 `pageindex/local_chat.py` | Exact propositions/entailment not determinable without responses. |
| [EPI-OBJ-citation-entries](#epi-obj-citation-entries) | Asserted document/page/block references | See record | SRC-1 `pageindex/client.py` | Resolving an identifier does not establish support for its attached claim. |
| [RT-OBJ-agent-instructions](runtime.md#rt-obj-agent-instructions) | None as answer content; behavior policy | See record | SRC-1 `pageindex/agent_tools.py` | Prompt delivery differs from compliance. |
| [RT-OBJ-cost-policy](runtime.md#rt-obj-cost-policy) | Formal search-cost account under its assumptions | See record | SRC-1 `pageindex/tree_optimize.py` | Not a measured answer-quality model. |

## Authority-route ledger

Ledger rows split functions even where the cited record is a valid container. All results are possible implementation results, not observed events. “See” delegates source-native mechanics to the cited record; the relation, license and mismatch columns are this member's assessment. No row treats retention as acceptance or lifecycle integration. For the inspected local paths, no evidence-consuming acceptance of an ampliative answer or summary against a named truth criterion was established; narrower structural admission is implemented.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-local-submit](runtime.md#rt-rte-local-submit) — import | content transformation | implemented | [EPI-OBJ-page-text](#epi-obj-page-text) | truth-apt transformation: acquisition/import | PDF → extracted page statements | Parser; extraction domain, not truth adjudication | See route | See route | Text becomes later evidence | Source warrant unknown; document association/page order retained, extraction fidelity unmeasured | Makes extracted content available for save | Store writer; parser output; permissive; retained-document horizon | SRC-1 `pageindex/local_api.py` | none | none | Graphical content may be missing; no external source validation. |
| [RT-RTE-local-submit](runtime.md#rt-rte-local-submit) — bounds | check/evidence production | implemented | [EPI-OBJ-tree-structure](#epi-obj-tree-structure) | no content change | Nonblank extraction, Flash result class, supplied span endpoints | Code; input readability/refusal policy and limited page bounds | Before save; see route | Exception or continuation | Enforcing | Only the tested predicates; not complete interval validity, hierarchy or factual truth | Failed checks block managed persistence | Submission driver; exception/control flow; enforcing; current submit | SRC-1 `pageindex/local_api.py` | none | narrow-check | Does not check all endpoint conditions; direct builders differ. |
| [RT-RTE-local-submit](runtime.md#rt-rte-local-submit) — admit | disposition/acceptance | implemented | [EPI-OBJ-tree-structure](#epi-obj-tree-structure) | no content change | Save eligibility after managed checks | Code decides, caller initiates; see route | Before store write | See route | Permissive | Structural operational admission only, not acceptance of all claims as true | Allows new document ID to enter local retrieval | Store caller; successful check return; permissive; later document use | SRC-1 `pageindex/local_api.py` | none | admission-not-warrant | No per-content human approval; no QA criterion. |
| [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine) — propose | content transformation | implemented | [EPI-OBJ-tree-structure](#epi-obj-tree-structure) | truth-apt transformation: indeterminate | Candidate subsection labels, locations and inferred grouping | Model proposes; cached headings alternate; see route | Full optimization above trigger | See route | Candidate only until later tests | Location/title hypotheses; printed titles may be copied, hierarchy entailment not established | Supplies candidates to filters | Optimizer; returned JSON/cache; advisory; candidate round | SRC-1 `pageindex/tree_optimize.py` | none | none | No concrete output to distinguish preservation from conjecture. |
| [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine) — model headings | check/evidence production | implemented | [EPI-OBJ-tree-structure](#epi-obj-tree-structure) | no content change | Model-proposed heading/page correspondence | Code in `propose_children`: nonempty title, integer/range, normalized substring, duplicate/own-title and page-order checks | Model branch before shared ownership filtering/scoring | Keep/drop model-proposed headings | Enforcing within model branch | Normalized text occurrence on the proposed page and tested range/order predicates only; not relevance, completeness or heading semantics | Only passing model proposals reach shared filters/scorer | Optimizer; model candidate list; enforcing; current expansion | SRC-1 `pageindex/tree_optimize.py` | none | branch-limited-check | Cache candidates bypass this evaluator; matching source text can still be an inappropriate semantic heading. |
| [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine) — cache candidates | operational admission/selection/consumption | implemented | [EPI-OBJ-tree-structure](#epi-obj-tree-structure) | no content change | Cached headings eligible for a node | `children_from_cache` selects node page span and configured kinds and excludes own normalized title | Cache branch before shared ownership filtering/scoring | Candidate heading/page list | Enforcing selection, not source-occurrence validation | Eligibility under supplied cache fields only; no independently established printed occurrence | Selected cached candidates reach shared filters/scorer without `propose_children` | Optimizer; cache-derived candidate list; permissive; current expansion | SRC-1 `pageindex/tree_optimize.py` | none | cache-occurrence-unknown | Cache provenance/prior validation uninspected; no observed unprinted candidate or acceptance. |
| [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine) — shared ownership | check/evidence production | implemented | [EPI-OBJ-tree-structure](#epi-obj-tree-structure) | no content change | Known/ancestor duplication and shared-page ownership of model or cache headings | `own_children` rejects represented headings and headings outside ownership boundaries when printed matches establish position | Both branches before scoring | Keep/drop candidate headings | Enforcing tested predicates | Bounded ownership/duplication license only; a missing printed match alone decides nothing | Surviving candidates from either branch reach common span assignment and scorer | Optimizer; filtered candidate lists; enforcing; current expansion | SRC-1 `pageindex/tree_optimize.py` | none | narrow-check | Does not grant universal printed-heading occurrence or semantic-fidelity assurance. |
| [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine) — cost | check/evidence production | implemented | [RT-OBJ-cost-policy](runtime.md#rt-obj-cost-policy) | truth-apt transformation: entailed derivation | Candidate costs and token-read estimates under fixed formulae | Deterministic arithmetic over tree ranges/token counts; see record | Each expansion candidate | See route | Supplies ranking and predicate | Numerical comparisons within encoded proxy assumptions only; source ranges not thereby true | Produces scores used by selector | Selector; computed scalars; ranking; current optimization | SRC-1 `pageindex/tree_optimize.py` | none | proxy-not-outcome | Warrant is implementation deduction, not observed retrieval latency or accuracy. |
| [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine) — attach | disposition/acceptance | implemented | [EPI-OBJ-tree-structure](#epi-obj-tree-structure) | no content change | Whether best decomposition replaces collapsed node | Code decides/vetoes against cost, gain-ratio and read-token predicates; see route | After filtering/scoring | Attach or remain collapsed | Enforcing | Acceptance for encoded navigation-cost objective and current tree, not answer truth or universal source occurrence; model/cache eligibility differs | Changes next tree traversal and summary inputs | Tree/scheduler; in-place children; enforcing; remaining indexing and later saved reads | SRC-1 `pageindex/tree_optimize.py` | none | proxy-not-outcome | CLI reports new validation issues but still writes; not a general validity veto. |
| [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine) — summaries | content transformation | implemented | [EPI-OBJ-node-summary](#epi-obj-node-summary) | truth-apt transformation: indeterminate | Leaf text or opening text plus child summaries → description/title | Model; parsing/nonempty/fallback logic, not semantic evaluator | Settled nodes, children before parent | See object | Retained routing content | Generated text is a candidate characterization; no established entailment or non-entailment | Feeds parent summary and later retrieval prompts | Scheduler/answering model; summary strings; advisory; parents and later sessions | SRC-1 `pageindex/utils.py` | none | generation-not-acceptance | Short leaves are separately warranted raw reuse; generated and fallback branches differ. |
| [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine) — raw reuse | content transformation | implemented | [EPI-OBJ-node-summary](#epi-obj-node-summary) | truth-apt transformation: non-ampliative reshaping | Short leaf text → summary field | Code below token threshold | Leaf summary branch | Stripped source text | Permissive | Inherits only extracted-text warrant | Allows model-free summary value | Parent summary/structure reader; text field; advisory; indexing/later reads | SRC-1 `pageindex/utils.py` | none | none | Does not certify original document statements. |
| [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine) — completion | check/evidence production | implemented | [EPI-OBJ-node-summary](#epi-obj-node-summary) | no content change | Settled-tree stability and whether requested model calls all failed | Scheduler code, runtime consistency and call-success domain | Finish; see route | Raise or return tree with summaries/fallbacks | Enforcing | Successful generation/stability only; not summary truth or coverage | Prevents returning globally failed/inconsistent summary run | Flash caller; exceptions/tree; enforcing; current indexing | SRC-1 `pageindex/utils.py` | none | completion-not-truth | Individual failed summaries can become fallback text. |
| [EPI-RTE-document-sanitization](#epi-rte-document-sanitization) | content transformation | implemented | [EPI-OBJ-page-text](#epi-obj-page-text) | truth-apt transformation: non-ampliative reshaping | Raw extracted evidence → redacted/framed model input | Regex substitution and delimiter escaping; see record | Classic prompt construction | Filtered document text | Alters model-visible evidence, not stored page truth | Warrant degraded for literal quotation/content involving matched phrases; no semantic safety guarantee | Removes selected strings from evidence shown to indexing/check models | Classic model; prompt text; enforcing substitution plus advisory framing; each call | SRC-1 `pageindex/page_index_classic.py` | none | redaction-not-truth | Phrase matching can remove legitimate document content. |
| [RT-RTE-alternate-builders](runtime.md#rt-rte-alternate-builders) — classic check | check/evidence production | implemented | [EPI-OBJ-tree-structure](#epi-obj-tree-structure) | no content change | Title appears or starts on proposed page | Model fuzzy judgment over sanitized page text; code aggregates nonexception results | After generated TOC/physical-index checks | Fraction and incorrect-entry list | Evidence to caller, not independent oracle | Bounded model assessment of location; no independent answer reference | Supplies repair/fallback decision | Meta-processor; fraction/list; ranking; current build | SRC-1 `pageindex/page_index_classic.py` | none | denominator-limit | Exceptions excluded; sanitized evidence differs from raw source. |
| [RT-RTE-alternate-builders](runtime.md#rt-rte-alternate-builders) — classic disposition | disposition/acceptance | implemented | [EPI-OBJ-tree-structure](#epi-obj-tree-structure) | no content change | TOC usable for builder continuation | Code thresholds plus model repair; see route | After check | Continue, bounded correction, fallback or fail | Enforcing | Operational TOC acceptance for building a navigation tree; not complete document truth | Returned repaired TOC may still contain errors | Builder; control flow/returned TOC; permissive; current and persisted product | SRC-1 `pageindex/page_index_classic.py` | none | repair-not-certification | Three correction attempts do not establish all entries correct. |
| [RT-RTE-alternate-builders](runtime.md#rt-rte-alternate-builders) — Markdown | content transformation | implemented | [EPI-OBJ-tree-structure](#epi-obj-tree-structure) | truth-apt transformation: non-ampliative reshaping | Recognized headings and their literal line segments | Regex/line slicing in inspected unthinned extraction branch | Markdown build before optional passes | Literal title/text nodes | Navigation input | Warrant limited to recognized syntax and copied text, not general Markdown semantics | Seeds hierarchy and optional summaries | Markdown builder; extracted nodes; permissive; generated file | SRC-1 `pageindex/page_index_md.py` | none | branch-limited | Optional model summaries indeterminate; thinning not independently assessed. |
| [RT-RTE-local-submit](runtime.md#rt-rte-local-submit) — description | content transformation | implemented | [EPI-OBJ-doc-description](#epi-obj-doc-description) | truth-apt transformation: indeterminate | Cleaned tree → one-sentence document description | Model; see route | Before metadata save | See object | Later selection cue | Candidate characterization, not accepted source proposition | Guides browse-time document choice | Answering model; metadata description; advisory; later invocations | SRC-1 `pageindex/local_api.py` | none | compression-lineage | No actual description to establish preservation or added claims. |
| [RT-RTE-local-submit](runtime.md#rt-rte-local-submit) — retain | retention | implemented | [EPI-OBJ-page-text](#epi-obj-page-text), [EPI-OBJ-tree-structure](#epi-obj-tree-structure), [EPI-OBJ-node-summary](#epi-obj-node-summary), [EPI-OBJ-doc-description](#epi-obj-doc-description) | no content change | Accepted-for-storage document product → disk | Store writer; see route | Successful submit | See route | Availability, not truth endorsement | Retains source associations and generated metadata; no new epistemic license | Makes pages/tree discoverable and reloadable | Local tools/getters; JSON files; permissive; until deletion | SRC-1 `pageindex/local_store.py` | none | retention-not-integration | No claim-level accepted ampliative product is established to undergo lifecycle integration. |
| [EPI-RTE-tree-normalization](#epi-rte-tree-normalization) | content transformation | implemented | [EPI-OBJ-tree-structure](#epi-obj-tree-structure), [EPI-OBJ-node-summary](#epi-obj-node-summary) | truth-apt transformation: non-ampliative reshaping | Wire aliases/range defaults → exposed tree | Deterministic assignment; see record | Getter return | See record | Changes exposed navigation | Copied descriptions keep prior warrant; default endpoints are compatibility conventions, not measurements | Exposes normalized values to readers | Getters/agents; returned JSON; permissive; current consumer | SRC-1 `pageindex/utils.py` | none | prefix-summary-loss | Both summary fields present: prefix overwrites summary. Earlier-server page endpoints are inferred, not checked. |
| [RT-RTE-document-chat](runtime.md#rt-rte-document-chat) — select/read | operational admission/selection/consumption | implemented | [EPI-OBJ-page-text](#epi-obj-page-text), [EPI-OBJ-tree-structure](#epi-obj-tree-structure) | no content change | Which documents/outline/pages reach answering context | Model semantic choices; local scope/budget code; see route | Tool calls within chat | See route | Scope enforcement plus advisory content | Imported evidence only; selection does not endorse truth | Allows selected evidence into next model call; budget can omit pages explicitly | Answering model; tool-result text; advisory, with enforcing scope; current chat | SRC-1 `pageindex/agent_tools.py` | [EPI-CLM-tree-retrieval](#epi-clm-tree-retrieval) | no-relevance-oracle | First valid page can exceed budget; direct SDK reads have different filtering. |
| [RT-RTE-document-chat](runtime.md#rt-rte-document-chat) — answer | content transformation | implemented | [EPI-OBJ-answer-text](#epi-obj-answer-text) | truth-apt transformation: indeterminate | Question/history/tool evidence → answer | Answer model, no demonstrated post-generation truth evaluator; see route | Final agent output | See route | Delivered answer | Candidate answer; source support and scope depend on actual output/evidence | Returns answer to caller without demonstrated semantic certification | Caller; answer text; advisory; current response, later history if supplied | SRC-1 `pageindex/local_chat.py` | [EPI-CLM-cited-grounding](#epi-clm-cited-grounding) | prompt-not-check | Neither entailed derivation nor ampliative conjecture can be established for unknown outputs. |
| [EPI-RTE-citation-resolution](#epi-rte-citation-resolution) | check/evidence production | implemented | [EPI-OBJ-citation-entries](#epi-obj-citation-entries) | no content change | Citation tags → document/block lookup results | Code name resolution and optional server block lookup; see record | Explicit caller helper invocation | See record | Reference resolution only | Can associate a citation with accessible material, not establish claim support | Produces display data; no answer rejection/rewrite-for-truth | Renderer/caller; citation dictionaries; advisory; displayed answer | SRC-1 `pageindex/client.py` | [EPI-CLM-tree-retrieval](#epi-clm-tree-retrieval), [EPI-CLM-cited-grounding](#epi-clm-cited-grounding) | resolution-not-support | Unknown names and some missing blocks survive; Markdown citation format is not parsed. |
| [EPI-RTE-document-withdrawal](#epi-rte-document-withdrawal) | lineage/freshness/recovery | implemented | [EPI-OBJ-page-text](#epi-obj-page-text), [EPI-OBJ-tree-structure](#epi-obj-tree-structure) | no content change | Document availability after deletion or manifest repair | Marker/cache/schema checks, not truth evaluator | Management call or listing | See record | Enforcing future local lookup availability | Withdrawal from retrieval, not retraction of a false proposition | Blocks later store reads; cannot erase evidence already in caller history | Store/getters; marker and files; enforcing; future lookups | SRC-1 `pageindex/local_store.py` | none | deletion-not-retraction | No semantic invalidation propagated into earlier answers/transcripts. |
| [RT-RTE-cloud-tools](runtime.md#rt-rte-cloud-tools) | operational admission/selection/consumption | implemented | [RT-OBJ-agent-instructions](runtime.md#rt-obj-agent-instructions), [EPI-OBJ-page-text](#epi-obj-page-text) | truth-apt transformation: acquisition/import | Remote guidance/content → local model or caller | Remote server supplies; local client constructs; see route | Cloud API/MCP path | See route | Remote instructions and tools admitted | Remote evidence warrant unknown; client wiring licenses no server-internal truth assessment | Changes available tools, instructions and evidence | Agent/caller; MCP/HTTP; permissive/advisory; per-call/session | SRC-1 `pageindex/agent_tools.py` | none | opaque-server | Remote acquisition/evaluation/acceptance not determinable from this artifact. |
| [RT-RTE-vision-notebook](runtime.md#rt-rte-vision-notebook) | operational admission/selection/consumption | implemented | [EPI-OBJ-tree-structure](#epi-obj-tree-structure), [EPI-OBJ-answer-text](#epi-obj-answer-text) | no content change | Model-selected nodes → page-image input selection | VLM relevance judgment; code maps ranges; see route | Before separate answer call | See route | Selection controls visible images | Selection is not checked relevance or answer warrant | Restricts evidence of independent answer frame | Answer VLM; selected images; permissive; second call | SRC-1 `cookbook/pageindex-vision-rag.ipynb` | [EPI-CLM-tree-retrieval](#epi-clm-tree-retrieval) | no-independent-oracle | Generated answer relation remains indeterminate; cloud-produced tree opaque. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-tree-retrieval](#epi-clm-tree-retrieval) | See record | SRC-1 `README.md`; doctrine/design | Tree navigation and explicit references requested | [RT-RTE-document-chat](runtime.md#rt-rte-document-chat), [RT-RTE-vision-notebook](runtime.md#rt-rte-vision-notebook), [EPI-RTE-citation-resolution](#epi-rte-citation-resolution) | None supplied | No independent relevance/answer intervention; tools allow page access rather than forcing all reasoning through hierarchy | Implemented evidence-navigation and reference-resolution affordances | Traceable identifiers do not certify explanation or entailment; small documents may bypass structure by design. |
| [EPI-CLM-benchmark-results](#epi-clm-benchmark-results) | See record | SRC-1 `README.md`; reported operation | Attributed numerical results and external runner links | [RT-RTE-document-chat](runtime.md#rt-rte-document-chat) is a plausible mechanism, not the frozen experiment | None admitted | Missing datasets, runner, answers and controlled comparisons prevent verification or component attribution | README reports results; architecture is compatible with selective reading | No transfer of headline accuracy to all local/cloud paths, models or documents. |
| [EPI-CLM-cited-grounding](#epi-clm-cited-grounding) | See record | SRC-1 `pageindex/agent_tools.py`; doctrine/design and prompt-delivery implementation | Explicit source-only and citation instructions | [RT-RTE-document-chat](runtime.md#rt-rte-document-chat), [RT-BAP-managed-guidance](runtime.md#rt-bap-managed-guidance), [EPI-RTE-citation-resolution](#epi-rte-citation-resolution) | None supplied | Prompt delivery is not compliance; resolver checks references, not support | Implemented request for grounded answers with optional page references | No implemented post-answer truth acceptance established in supplied driver account. |
| [RT-CLM-layout-extraction](runtime.md#rt-clm-layout-extraction) | See record | SRC-1 `pageindex/flash/api.py`; implementation/design | Extraction separated from optional model passes | [RT-RTE-local-submit](runtime.md#rt-rte-local-submit), [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine) | None supplied | Default full pipeline contains expansion/summaries; layout heuristics can err | Narrow LLM-free extraction claim supported, not a model-free indexing claim | Semantic fidelity unmeasured. |

## Bounded conclusion

PageIndex acquires document statements rather than establishing their external truth. In the local route, extraction preserves document/page association but leaves source warrant and extraction fidelity unknown; scanned or graphical content is not equivalent to the stored text ([EPI-OBJ-page-text](#epi-obj-page-text)). It retains page text separately from navigation and generated descriptions. Later retrieval gives a model selected evidence, not a certified proposition set ([RT-RTE-local-submit](runtime.md#rt-rte-local-submit), [RT-RTE-document-chat](runtime.md#rt-rte-document-chat)).

There are real evaluators with narrow domains. The model-proposal branch tests normalized printed-title occurrence, range, order and duplicates. Cache candidates instead enter through node-span/kind selection and own-title exclusion, without that occurrence veto. Both branches undergo shared known/ancestor and conditional shared-page ownership filtering, span assignment and cost selection; missing printed matches alone do not reject cached candidates. Thus attachment grants no universal source-occurrence license. Arithmetic derives proxy costs from encoded inputs. Cost-based acceptance grants a decomposition operational authority over subsequent indexing and later navigation, for the intended use of reducing encoded search/read cost, not verified answer error. Classic title/page verification consumes evidence through model judgments and changes repair/fallback/continuation, but its exception-excluding denominator and bounded repair prevent interpreting acceptance as universal correctness ([RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine), [RT-RTE-alternate-builders](runtime.md#rt-rte-alternate-builders)). These conclusions survive the strongest local counterexamples to a blanket “no checks” account.

Model-produced summaries, retitles, document descriptions and answers are truth-apt candidates. Their individual preservation, entailment or added conjecture is not determinable without actual input/output pairs. The short-leaf raw-text branch is a concrete non-ampliative counterexample to labeling all summaries novel model claims. Nonempty results, scheduler consistency, storage and answer return are not evidence-consuming semantic acceptance. No accepted ampliative claim followed by lifecycle integration is established in these inspected local paths; this is not an assertion about inaccessible Cloud server internals ([EPI-OBJ-node-summary](#epi-obj-node-summary), [EPI-OBJ-doc-description](#epi-obj-doc-description), [EPI-OBJ-answer-text](#epi-obj-answer-text)).

Content can change at the evidence-consumer boundary: tree normalization may prefer a prefix summary, and page delivery omits budget-exceeding later pages with explicit continuation guidance. Citation resolution links names/tags to material when available but does not reject unsupported propositions. Deletion withdraws future store availability, not already delivered answers. These mechanisms matter to lineage and reliance even though none is a truth oracle ([EPI-RTE-tree-normalization](#epi-rte-tree-normalization), [EPI-RTE-citation-resolution](#epi-rte-citation-resolution), [EPI-RTE-document-withdrawal](#epi-rte-document-withdrawal)).

Behavioral authority differs by consumer. Optimizer predicates enforce decisions; retained descriptions advise model selection; managed source-only instructions request behavior per invocation. Cloud tools/prompts can change the agent's available behavior without any locally established truth-apt acceptance route ([RT-BAP-cost-selection](runtime.md#rt-bap-cost-selection), [RT-BAP-managed-guidance](runtime.md#rt-bap-managed-guidance), [RT-RTE-cloud-tools](runtime.md#rt-rte-cloud-tools)). This is capability/guidance admission, not evidence of parametric learning. Improved future capacity, reflection, theory-directed revision, autonomy and self-improvement do not follow from retrieval or cost reduction. The separate bounded theory findings remain those of [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine); no additional positive or system-wide negative is inferred here. Missing run and experimental evidence prevents exercised-reliability and causal-benefit conclusions, including independent verification of [EPI-CLM-benchmark-results](#epi-clm-benchmark-results).

## Shared records

### Operative objects

#### EPI-OBJ-page-text
Label: Page text

Source-native identity: local `pages` entries with `page_index` and `markdown`. Natural-language extracted statements plus symbolic page keys, stored in `pages.json`. Produced by local PyPDF2 extraction and later read as document evidence. Distinct from the process [RT-RTE-local-submit](runtime.md#rt-rte-local-submit); no supplied operative-object counterpart. Source warrant unknown: source/page association persists, but no external truth check or measured extraction fidelity is established. SRC-1: `pageindex/local_api.py`.

> pages = [{"page_index": i + 1, "markdown": text}
>                  for i, text in enumerate(page_texts)]
> --- `pageindex/local_api.py`

> return [_scrub_surrogates(page.extract_text() or "")
>                     for page in reader.pages]
> --- `pageindex/local_api.py`

#### EPI-OBJ-tree-structure
Label: Tree structure

Source-native identity: `structure` nodes with titles, node IDs, page spans and children. Mixed natural-language heading strings and symbolic hierarchy/ranges; in-memory dictionaries and local `tree.json` or CLI JSON. Claims are about document organization and location. Distinct output object of [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine) and [RT-RTE-alternate-builders](runtime.md#rt-rte-alternate-builders), not those processes themselves; no supplied object counterpart. Generation/check/admission mechanics: see those routes. Printed-heading checking applies to model-proposed children, not all candidates. Cache candidates bypass `propose_children`; node-span/kind selection and own-title exclusion precede shared ownership/cost filtering. The shared ownership filter rejects represented headings and conditionally misplaced printed headings, but does not reject solely for missing printed matches. Neither branch certifies semantic fidelity, and cache admission additionally lacks an independent occurrence guarantee. SRC-1: `pageindex/tree_optimize.py`, `pageindex/page_index_md.py`.

> if normalize(title) not in normalize(pages[page - 1]):
>             continue                     # the heading must be printed on that page
> --- `pageindex/tree_optimize.py`

The cache counterpath and shared filter are directly inspected implementation evidence, consistent with [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine) and [MEM-OBJ-headings-cache](memory.md#mem-obj-headings-cache). This object remains the output tree, not a duplicate cache object. No execution shows an unprinted heading being supplied or attached.

> cached = own(children_from_cache(node, args.cache, args.kinds))
>         if cached:
>             candidates.append(("cache", cached))
> --- `pageindex/tree_optimize.py`

> if kinds and heading.get("kind") not in kinds:
>                 continue
>             if normalize(heading["title"]) == normalize(node["title"]):
>                 continue
> --- `pageindex/tree_optimize.py`

> printed = found(page, lambda line: key in normalize(line)) if key else []
>         if (is_node(page, child["title"])
>                 or page == start and top and printed and printed[-1] < top[0]
>                 or page == end and bottom and printed and printed[0] >= bottom[-1]):
>             continue
>         kept.append(child)
> --- `pageindex/tree_optimize.py`

A deterministic Markdown witness, deduced without execution: input `# A\nBody\n## B\nTail` produces heading metadata for A at line 1/level 1 and B at line 3/level 2; slicing yields `# A\nBody` and `## B\nTail`. This is copied content and syntax-based grouping, not new claims about the world. It applies before optional thinning/model passes. SRC-1: `pageindex/page_index_md.py`.

> header_pattern = r'^(#{1,6})\s+(.+)$'
> --- `pageindex/page_index_md.py`

> node['text'] = '\n'.join(markdown_lines[start_line:end_line]).strip()
> --- `pageindex/page_index_md.py`

#### EPI-OBJ-node-summary
Label: Node summary

Source-native identity: node `summary`, Markdown `prefix_summary`, and same-page fused-node retitle. Natural-language values in the tree, eventually in tree JSON for retained paths. Distinct produced material from [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine), which remains a valid container process, and [RT-RTE-alternate-builders](runtime.md#rt-rte-alternate-builders); no supplied object counterpart. Leaf summaries use selected text; parents receive opening text and child summaries. A generated characterization need not preserve all meaning, but no actual unsupported proposition is supplied to prove ampliation. Generated relation is indeterminate; raw short-text reuse is non-ampliative. Nonempty parsing and fallback are completion controls, not truth acceptance. SRC-1: `pageindex/utils.py`.

> if count_tokens(text, model=self._model) < self._small_node_tokens:
>             return text.strip()
> --- `pageindex/utils.py`

> [{'title': c.get('title', ''), 'summary': c.get('summary', '')} for c in children],
> --- `pageindex/utils.py`

> if retitle:
>             written = parse_title(reply)
>             if written:
>                 node['title'] = written
>         return parse_summary(reply)
> --- `pageindex/utils.py`

> if not node['summary']:
>             node['summary'] = fallback_summary(node, "" if children else self._leaf_text(node))
> --- `pageindex/utils.py`

> if (self._asked and not self._answered) or not _any_summary(self.structure):
> --- `pageindex/utils.py`

#### EPI-OBJ-doc-description
Label: Document description

Source-native identity: generated `description` stored in document metadata. Natural-language one-sentence characterization held in a Python string, `doc.json` and manifest metadata. It can influence later document choice without certifying source truth. Distinct from [EPI-OBJ-node-summary](#epi-obj-node-summary): whole-document discovery cue, different model input and consumer. Closest supplied record is producing route [RT-RTE-local-submit](runtime.md#rt-rte-local-submit), not a duplicate object. Flash passes a cleaned top-level tree to generation; no per-description semantic acceptance is established. SRC-1: `pageindex/local_api.py`; later interpretation is requested in `pageindex/agent_tools.py`.

> description = generate_doc_description(
>             create_clean_structure_for_description(structure, top_level_only=True),
>             model=self._summary_model,
>         )
> --- `pageindex/local_api.py`

> - After discovery: 1 match or 1 clearly best match → proceed to read and answer without asking. Multiple equally relevant → ask user to pick.
> --- `pageindex/agent_tools.py`

#### EPI-OBJ-answer-text
Label: Answer text

Source-native identity: own-model final answer, cloud answer or notebook VLM answer. Natural-language propositions in returned text/protocol envelopes; no automatic local durable answer store is established. Different producers and inputs remain those of [RT-RTE-document-chat](runtime.md#rt-rte-document-chat), [RT-RTE-cloud-tools](runtime.md#rt-rte-cloud-tools) and [RT-RTE-vision-notebook](runtime.md#rt-rte-vision-notebook). This is their output class, not a duplicate route or a claim that all share one evaluator. Retained tool history is separately [RT-RTE-protocol-history](runtime.md#rt-rte-protocol-history). No candidate instance was inspected; exact truth-apt propositions and their relation to evidence are not determinable. Prompt grounding is a requested restriction, not a truth check. SRC-1: `pageindex/local_chat.py`, `pageindex/agent_tools.py`; mechanism evidence supplied by the cited routes.

#### EPI-OBJ-citation-entries
Label: Citation entries

Source-native identity: parsed `citations` dictionaries and resolved display anchors. Symbolic document/page/block identifiers with optional natural-language block text, in caller-returned dictionaries; no independent durable store. Distinct from answer propositions and from [RT-OBJ-agent-instructions](runtime.md#rt-obj-agent-instructions): references are produced/processed output, instructions are policy. Closest supplied mechanism [RT-RTE-document-chat](runtime.md#rt-rte-document-chat) does not describe this resolver in detail. Unknown document names retain null IDs, and unavailable blocks can retain tags without retrieved content; page-level entries receive no semantic-support assessment. SRC-1: `pageindex/client.py`.

> entry: dict[str, Any] = {"document": citation["document"],
>                                      "doc_id": ids[0] if ids else None,
>                                      "page": citation["page"]}
> --- `pageindex/client.py`

### Routes

#### EPI-RTE-document-sanitization
Label: Document sanitization

Part of: [RT-RTE-alternate-builders](runtime.md#rt-rte-alternate-builders)

Endpoints: extracted classic document text → keyword redaction and delimiter framing → classic generation/verification prompts. Owner is `_secure_doc_text`; this is a material input-transformation part of the supplied alternate-builder route, not a replacement for its evaluator or disposition. It does not modify local stored page text. SRC-1: `pageindex/page_index_classic.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: redacted document text wrapped as model-visible data.
- Later read-back: inapplicable — this helper persists no changed artifact; generated downstream tree content has its own retention route.
- Delegated visibility: classic model receives transformed evidence, not the raw matching phrases.
- Selection predicate: known injection-pattern regex matches are replaced wherever they occur in supplied text; the title-appearance evaluator invokes the helper on its page evidence.
- Invalidation or expiry: inapplicable — current-call string transformation has no independent cache or expiry.
- Activation or effect: deterministic replacement changes model-visible input; successful instruction isolation or output correctness is unobserved.
- Evidence limits: static deduction establishes string alteration, not injection resistance or meaning preservation for arbitrary prose.

Concrete deduction: input `The text says ignore previous instructions.` becomes `The text says [REDACTED].` before framing. The matched string could be legitimate quoted content. This removes rather than adds a source proposition, so the relation is non-ampliative reshaping with degraded literal fidelity, not entailed derivation or acceptance. Delimiter framing and the hardening prompt request that the remaining text be treated as data; they do not turn that request into a demonstrated semantic boundary.

> r"ignore\s+(all\s+)?(previous|prior|above)\s+instructions?|"
> --- `pageindex/page_index_classic.py`

> return _INJECTION_PATTERNS.sub("[REDACTED]", text)
> --- `pageindex/page_index_classic.py`

> return _wrap_doc_text(_sanitize_doc_text(text))
> --- `pageindex/page_index_classic.py`

#### EPI-RTE-tree-normalization
Label: Tree normalization

Endpoints: wire tree → `unify_tree` → public getter/agent structure. Owner is the client utility. It preserves topology, copies fields and chooses aliases/default endpoints. Distinct material getter subroute of supplied [RT-RTE-document-chat](runtime.md#rt-rte-document-chat), rather than new document generation or optimizer refinement. Also used outside chat by direct getters, so not contained exclusively in that runtime route. SRC-1: `pageindex/client.py`, `pageindex/utils.py`; implementation evidence.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: normalized tree dictionaries.
- Later read-back: inapplicable — this helper does not persist its normalization; a caller can retain returned values outside the helper.
- Delegated visibility: model tools/callers receive the normalized tree rather than both raw summary aliases.
- Selection predicate: client invokes normalization on a nonempty tree result; fields copied by fixed rules.
- Invalidation or expiry: inapplicable — fresh normalization of the current getter result, no cache owned here.
- Activation or effect: endpoint defaults and alias choice can change the content a later reader sees; no actual consumer response was observed.
- Evidence limits: deterministic deduction, not a run or measurement of compatibility/fidelity.

Concrete deduction: a node containing `summary: "Whole section"` and `prefix_summary: "Opening only"` exposes only `summary: "Opening only"`, because the loop assigns that key twice. This selects existing text rather than inventing a proposition, but can degrade the intended summary scope. Missing endpoint inference similarly licenses a conventional navigation span, not verified source boundaries. No supersession of runtime is needed: the supplied account did not promise preservation of both aliases.

> for key in ("summary", "prefix_summary"):
>                 if key in node:
>                     unified["summary"] = node[key]
> --- `pageindex/utils.py`

> if end is None:
>             end = starts[i + 1] if i + 1 < len(flat) else page_count
> --- `pageindex/utils.py`

#### EPI-RTE-citation-resolution
Label: Citation resolution

Endpoints: answer text → tag parsing/name lookup/optional cloud block lookup → reference entries and optionally numbered display links. Owner is `PageIndexClient.get_citations` / `resolve_citations`. Distinct from [RT-RTE-document-chat](runtime.md#rt-rte-document-chat): explicit post-answer caller utility, not a required agent acceptance gate. Source is SRC-1: `pageindex/client.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: reference dictionaries or answer text with numbered links and reference data.
- Later read-back: inapplicable — helper writes no retained state; caller owns any storage/display.
- Delegated visibility: caller/renderer receives looked-up block material when available; this is not automatically re-fed to the answering model.
- Selection predicate: explicit caller invocation, recognized tag syntax, supplied document IDs or library enumeration; ambiguous names raise.
- Invalidation or expiry: uninspected — helper performs current lookups but no observed source/document change or later caller use was supplied.
- Activation or effect: lookup/display wiring is implemented; changed reader reliance is unobserved.
- Evidence limits: identifier association and formatting are not entailment checks; Markdown prose references are explicitly not parsed.

Target/domain: tag identity and accessible document/block association, not the proposition next to the tag. Evaluator: deterministic parser/name resolver plus remote block availability. Unknown names and selected missing-block errors leave entries; no correctness veto, answer revision, rollback or claim acceptance occurs here. Caller chooses to resolve; code handles lookup failure. This is a check/evidence-production route, not product admission. Its display reshaping changes notation without granting additional warrant.

> if entry["doc_id"]:
>                     try:
>                         entry.update(self.get_block(entry["doc_id"], block_id))
>                     except PageIndexAPIError as exc:
>                         # Local raises carry no status; 429/5xx propagate.
>                         if exc.status_code not in (None, 403, 404):
>                             raise
> --- `pageindex/client.py`

#### EPI-RTE-document-withdrawal
Label: Document withdrawal

Endpoints: SDK delete or registered remove operation → marker/file/cache removal → future lookup absence. Related maintenance: listing/get-metadata reconstruct or use schema-valid metadata caches. Owner: `DocStore`; tool wrapper resolves names and reports per-document outcomes. Distinct management/availability route, not duplicate of creation in [RT-RTE-local-submit](runtime.md#rt-rte-local-submit). Management tool exposure is accounted for by [RT-RTE-framework-tools](runtime.md#rt-rte-framework-tools). SRC-1: `pageindex/local_store.py`, `pageindex/agent_tools.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: store deletion boolean; SDK/tool response and per-name statuses.
- Later read-back: future store reads require the marker; cached metadata can reconstruct discovery only for directories whose marker exists.
- Delegated visibility: management caller receives statuses; already delivered evidence/history is not reached by this operation.
- Selection predicate: caller-selected ID or tool-resolved names; all supplied name elements checked before any deletion, at most ten names per tool call.
- Invalidation or expiry: marker removed first, directory removal attempted and manifest entry dropped; no time-based truth expiry or semantic claim invalidation.
- Activation or effect: future getter availability is changed by code; exercised deletion and downstream answer effects unobserved.
- Evidence limits: file cleanup is best effort and this is not semantic retraction of earlier answers or removal from external transcripts.

Caller or tool-using model initiates deletion; code can veto malformed inputs and resolve missing names. No additional per-document human approval occurs inside the remover. The trigger is an explicit management request, not a falsity judgment. No recovery/rollback restores removed content; re-submission is an external subsequent action. Cached metadata validity checks license use as metadata, not endorsement of the document's statements.

> if doc_dir is None or not (doc_dir / "doc.json").is_file():
>             return None
>         return _read_json(doc_dir / name)
> --- `pageindex/local_store.py`

> (doc_dir / "doc.json").unlink()
> --- `pageindex/local_store.py`

> if doc_dir.is_dir():
>             shutil.rmtree(doc_dir, ignore_errors=True)
> --- `pageindex/local_store.py`

### Claims

#### EPI-CLM-tree-retrieval
Label: Tree retrieval

Claimed operation/warrant: hierarchical indexing and LLM reasoning replace vector retrieval and provide traceable, explainable, context-aware retrieval. Source: SRC-1 `README.md`, doctrine/design. Closest supplied claim [RT-CLM-layout-extraction](runtime.md#rt-clm-layout-extraction) concerns model-free extraction, not retrieval quality or traceability; distinct identity. Route comparison must distinguish a mechanism and explicit references from warranted answer support.

> 1. **Index**: generate a **tree-structure index** for each document
> 2. **Retrieve**: agentically **search that tree** with LLM reasoning
> --- `README.md`

> <blockquote>PageIndex is a <b>vectorless</b>, <b>reasoning-based RAG</b> engine that <b>mirrors how humans read</b>, delivering <b>traceable</b>, <b>explainable</b>, and <b>context-aware</b> retrieval, with <b>no vector DBs</b> or <b>chunking</b>.</blockquote>
> --- `README.md`

#### EPI-CLM-benchmark-results
Label: Benchmark results

Claimed operation/warrant: local quickstart evaluation, comparative selective-read cost figures and FinanceBench accuracy. SRC-1 `README.md`, reported operation, not admitted observed-run/causal evidence. Different datasets/configurations remain distinct reported results; none is inferred from another. No supplied claim counterpart after comparison with [RT-CLM-layout-extraction](runtime.md#rt-clm-layout-extraction); that concerns architecture, not benchmark outcomes.

> [**PageIndex-OSS-Benchmark**](https://github.com/VectifyAI/PageIndex-OSS-Benchmark) measures exactly the setup in the quickstart above (`PageIndexClient()` in local mode, flash indexing, no OCR) on 62 lookup questions over 34 PDFs (1,945 pages) drawn from [MMLongBench-Doc-V2](https://github.com/VectifyAI/MMLongBench-Doc-V2). Every question's answer is a fact stated in running text, so a wrong answer is a **retrieval or reading failure**, not a reasoning one.
> --- `README.md`

> On documents where both routes return the same answer, native PDF input costs **2.1× more at 52 pages and 16.6× more at 420** (`gpt-5.6-sol`, prompt caching excluded) — and at 805 pages the document no longer fits in the context window at all.
> --- `README.md`

> PageIndex reached a state-of-the-art [**98.7% accuracy**](https://vectify.ai/blog/Mafin2.5) on [FinanceBench](https://arxiv.org/abs/2311.11944) (financial document QA benchmark), vastly outperforming vector-based RAG.
> --- `README.md`

#### EPI-CLM-cited-grounding
Label: Cited grounding

Claimed design contract: source-only answers stating only read evidence and supported citations. SRC-1 `pageindex/agent_tools.py`, doctrine/design embodied in delivered prompt text. This is a material part of the instruction object, not a new copy of [RT-OBJ-agent-instructions](runtime.md#rt-obj-agent-instructions); different record kind because this record identifies what the policy demands, not the stored policy itself. Distinct from extraction claim [RT-CLM-layout-extraction](runtime.md#rt-clm-layout-extraction).

> "markdown": """\
> GROUNDING
> - Answer only from the user's PageIndex documents. Call get_page_content() and state only what was actually read there.
> - Never fill a gap from general knowledge. When the documents do not answer the question, say so.
> --- `pageindex/agent_tools.py`

> - Cite only statements supported by tool outputs, as a bracketed reference: [{docName}, p. {pageNumber}] or [{docName}, p. {pageNumber}, block {blockId}]. Place immediately after the claim.
> --- `pageindex/agent_tools.py`
