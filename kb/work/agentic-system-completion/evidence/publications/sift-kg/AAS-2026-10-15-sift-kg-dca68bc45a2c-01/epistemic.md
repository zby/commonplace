---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "sift-kg epistemic routes: document fidelity, graph mutation, review authority and later agent reliance."
run-id: AAS-2026-10-15-sift-kg-dca68bc45a2c-01
reviewed-boundary: d786991c024f5401f113fc0cb70aee96dd1bd3bf
---

# sift-kg epistemic report

## Source-and-claim boundary

Question: what licenses reliance on sift-kg's extracted relations, normalized graph and derived prose, and which results actually change later use? Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence); evidence identities: see its [Source register](boundary.md#source-register). The external host's answers, provider internals, hosted Civic Table verification and dependency internals are excluded, not presumed to supply checks inside sift-kg.

This is implementation and doctrine/design analysis of SRC-1, not target execution. Runtime supplies the broad traces below; direct additional reads check extraction admission, graph cleanup, style rewriting and omitted CLI operations. No execution trace, authenticated reviewer record, gold corpus or intervention/comparison is supplied. These respectively prevent observed-route attribution, demonstrated human acceptance, extraction/identity accuracy estimates and causal benefit claims. Example artifacts are not linked production/check/acceptance traces. Model transformations without paired inputs/results remain semantically indeterminate, rather than automatically classified as conjecture. Imported document assertions have unknown source warrant: documentary origin is not established truth.

| Entry point or operation | SRC-1 source path | Coverage and basis |
|---|---|---|
| `sift`, module invocation, library pipeline | `pyproject.toml`, `src/sift_kg/__main__.py`, `src/sift_kg/pipeline.py` | Supplied runtime account; stage ownership, not a conversational agent loop. |
| extract; reader/OCR; discovery | `src/sift_kg/extract/extractor.py`, `src/sift_kg/extract/models.py`, `src/sift_kg/extract/prompts.py`, `src/sift_kg/ingest/reader.py`, `src/sift_kg/domains/discovery.py` | Direct extraction/model reads and prompt search supplement [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction), [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery). OCR internals remain opaque. |
| build, cleanup, flags, save | `src/sift_kg/cli.py`, `src/sift_kg/graph/builder.py`, `src/sift_kg/graph/postprocessor.py` | Direct build and entire postprocessor reads supplement [RT-RTE-graph-build](runtime.md#rt-rte-graph-build). |
| resolve, review, apply-merges | `src/sift_kg/resolve/resolver.py`, `src/sift_kg/resolve/reviewer.py`, `src/sift_kg/resolve/engine.py` | Supplied [RT-RTE-entity-resolution](runtime.md#rt-rte-entity-resolution), [RT-RTE-review-application](runtime.md#rt-rte-review-application); human and automatic channels retained separately. |
| narrate; communities-only; style rewrite | `src/sift_kg/narrate/generator.py`, `src/sift_kg/narrate/prompts.py` | Direct rewrite bodies and prompt search supplement [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation). |
| query, search, topology | `src/sift_kg/cli.py`, `src/sift_kg/graph/communities.py` | Supplied [RT-RTE-graph-retrieval](runtime.md#rt-rte-graph-retrieval); selection, not verification. |
| view, export | `src/sift_kg/visualize.py`, `src/sift_kg/export.py` | Supplied [RT-RTE-view-export](runtime.md#rt-rte-view-export); delivered views omit provenance structure. Browser execution unobserved. |
| init, info, domains | `src/sift_kg/cli.py` | Direct init/info bodies and complete CLI command-registration search. Init writes caller-selected configuration, not factual approval. Info computes counts/status summaries and file-existence indicators, not semantic success. Domains enumeration body not inspected: domain listing fidelity is unassessed; no system-complete negative is inferred. |
| host-agent knowledge-island reasoning | `.agents/skills/sift-kg/SKILL.md` | Direct opening/reasoning instructions; [RT-BAP-agent-skill](runtime.md#rt-bap-agent-skill). Hypothesis generation belongs to the excluded host, not an implemented sift-kg inference executor. |
| hooks/tools and quality evaluations | `src/`, `.agents/`, `pyproject.toml`, `tests/`, `.github/` | Supplied [RT-ABS-tool-execution](runtime.md#rt-abs-tool-execution) and boundary test/CI inventory. No supplied passing run or factual benchmark; test bodies beyond supplied coverage unassessed. |

Consequential claims: [RT-CLM-merge-approval](runtime.md#rt-clm-merge-approval), [EPI-CLM-graph-grounding](#epi-clm-graph-grounding), [EPI-CLM-explicit-extraction](#epi-clm-explicit-extraction). The README also documents threshold automation; its approval language is not its only design statement.

## Epistemic-object inventory

Fields owned by linked records: see those records. IDs identify parts, not warranted knowledge.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-document-text](#epi-obj-document-text) | Document assertions | Input evidence | SRC-1 `src/sift_kg/extract/extractor.py` | Source truth and OCR fidelity unknown. |
| [EPI-OBJ-document-summary](#epi-obj-document-summary) | Participants, roles, subject | Shared chunk context | SRC-1 `src/sift_kg/extract/extractor.py` | First chunk only; no semantic check. |
| [EPI-OBJ-domain-config](#epi-obj-domain-config) | Category descriptions; constraints chiefly policy | Reusable schema guidance | SRC-1 `src/sift_kg/domains/discovery.py` | Schema adequacy not established by parse success. |
| [EPI-OBJ-extracted-content](#epi-obj-extracted-content) | Names, attributes, relation propositions, purported quotes | Document-derived facts | SRC-1 `src/sift_kg/extract/models.py` | Quotes/confidence are model output, not independent warrant. |
| [EPI-OBJ-graph-data](#epi-obj-graph-data) | Transformed entity/relation assertions | Retained structured understanding | SRC-1 `src/sift_kg/graph/builder.py` | Not identical to extraction; pending flags do not block publication. |
| [EPI-OBJ-review-state](#epi-obj-review-state) | Sameness hypotheses, reasons; status as control | Merge/removal decisions | SRC-1 `src/sift_kg/resolve/models.py` | Manual evidence use possible; threshold confirmation also possible. |
| [EPI-OBJ-derived-prose](#epi-obj-derived-prose) | Descriptions, narrative, thematic labels | Reader-facing synthesis | SRC-1 `src/sift_kg/narrate/generator.py` | Style checks do not establish factual preservation. |
| [EPI-OBJ-structural-results](#epi-obj-structural-results) | Reachability, counts, membership relative to loaded graph | Navigation and ranking | SRC-1 `src/sift_kg/cli.py` | Graph-relative structural facts do not prove real-world absence/connections. |

Opaque numerical parts remain separate: see [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client), [RT-CMP-sem-hash](runtime.md#rt-cmp-sem-hash), [RT-CMP-sentence-transformer](runtime.md#rt-cmp-sentence-transformer), [RT-CMP-ocr-backends](runtime.md#rt-cmp-ocr-backends). Parameter updates are not requested by inspected adapters; exact versions and endpoint fixity remain unestablished. This says nothing about hidden provider training or improved capacity through retained symbolic state.

## Authority-route ledger

All rows concern architecture, not observed activation. Repeated container citations refer to distinct local functions, not duplicate declarations. Generic fields owned by those records: see linked records. No recorded semantic acceptance is inferred from retention or operational use.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | content transformation | implemented | [EPI-OBJ-document-text](#epi-obj-document-text) | truth-apt transformation: acquisition/import | Documents to text | Reader/OCR adapter; supported file domain | Caller extract request | Text and chunks | Input supply | Source warrant unknown; not authenticated | Permit chunk processing | Extraction; text; permissive; current run | SRC-1 `src/sift_kg/extract/extractor.py` | none | none | OCR fidelity external/unobserved. |
| [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | content transformation | implemented | [EPI-OBJ-document-summary](#epi-obj-document-summary) | truth-apt transformation: indeterminate | First chunk to summary | Completion model; first-chunk participant/role/subject context | Before chunk extraction | Candidate document summary | Candidate generation | None beyond selected source context; intended compression may or may not preserve meaning | Supplies shared context to later chunk prompts | Extraction model; natural-language summary; advisory; current document calls | SRC-1 `src/sift_kg/extract/extractor.py` | none | none | Need paired input/result and semantic comparison to decide reshaping, entailment or conjecture. |
| [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | content transformation | implemented | [EPI-OBJ-extracted-content](#epi-obj-extracted-content) | truth-apt transformation: indeterminate | Chunk and generated summary to assertions | Completion model; selected document/domain context | During chunk extraction | Candidate entities/relations/evidence | Candidate generation | None beyond supplied source context; intended extraction may or may not preserve meaning | Supplies typed admission | Parser; JSON response; permissive; current call then files | SRC-1 `src/sift_kg/extract/extractor.py` | [EPI-CLM-explicit-extraction](#epi-clm-explicit-extraction) | none | Need paired inputs/results and semantic comparison to decide reshaping, entailment or conjecture. |
| [EPI-RTE-extraction-shape](#epi-rte-extraction-shape) | check/evidence production | implemented | [EPI-OBJ-extracted-content](#epi-obj-extracted-content) | no content change | Returned fields and confidence range | Pydantic and float conversion; data-shape domain | After JSON model response | Constructible item or caught malformed item | Computational check | Shape/range only; no source truth, quote identity or entailment license | Provides pass/fail to collection loop | Extraction loop; exception/typed object; enforcing; current item | SRC-1 `src/sift_kg/extract/models.py` | [EPI-CLM-explicit-extraction](#epi-clm-explicit-extraction) | none | A false but well-typed claim can pass. |
| [EPI-RTE-extraction-shape](#epi-rte-extraction-shape) | disposition/acceptance | implemented | [EPI-OBJ-extracted-content](#epi-obj-extracted-content) | no content change | Item admission | Python append/skip; no mandatory human | Immediately after construction | Valid items accumulated, malformed items skipped | Enforcing admission | Not evidence-consuming factual acceptance | Allows persisted candidates; failure can yield empty chunk | Aggregator; typed list; enforcing; document output | SRC-1 `src/sift_kg/extract/extractor.py` | none | none | No supplied run trace. |
| [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction) | retention | implemented | [EPI-OBJ-extracted-content](#epi-obj-extracted-content) | no content change | Extraction JSON persistence | Document owner writes accepted shape | After aggregation | Candidate file/cache | Retention | Not lifecycle integration after epistemic acceptance | Allows build/narration/reuse | Later stages; JSON; permissive; later invocations | SRC-1 `src/sift_kg/extract/extractor.py` | none | none | Configuration-only stale check does not ensure source freshness; see runtime. |
| [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery) | content transformation | implemented | [EPI-OBJ-domain-config](#epi-obj-domain-config) | non-truth-apt policy/content update: corpus-specific schema guidance | Samples to extraction policy | Model proposal; typed/nonempty configuration checks | Missing/forced domain discovery | Reusable YAML or fallback | Automatic policy admission | No proof that categories exhaust or correctly describe corpus | Changes prompts/build constraints | Extraction/build; domain config; advisory text and enforcing rules; future invocations | SRC-1 `src/sift_kg/domains/discovery.py` | none | none | Any factual description within guidance remains semantically unverified; see runtime theory account. |
| [RT-RTE-graph-build](runtime.md#rt-rte-graph-build) | content transformation | implemented | [EPI-OBJ-graph-data](#epi-obj-graph-data) | truth-apt transformation: indeterminate | Names/types/edges to graph | Code, SemHash, domain constraints; graph construction domain | Build, before save | Collapsed identities, changed types/directions, removed edges | Automatic mutation | Structural normalization, not proof of entity identity or original evidence support | Changes all graph consumers | Graph save; NetworkX/JSON; enforcing; until rebuild/surgery | SRC-1 `src/sift_kg/graph/builder.py` | none | Do not classify entire build as harmless reshaping. | Some edits are reshaping, some lose assertions, some depend on unverified equivalences. |
| [EPI-RTE-relation-normalization](#epi-rte-relation-normalization) | content transformation | implemented | [EPI-OBJ-graph-data](#epi-obj-graph-data) | truth-apt transformation: ampliative conjecture | TRAVELED_FROM edge with undefined type to TRAVELED_TO | Static synonym table and valid-type membership | Postprocess enabled; source type not valid | Destination assertion replacing origin assertion | Automatic replacement | No source-entailment license for this mapping | Publishes rewritten relation | Build and later query/export; relation_type field; enforcing; saved graph lifetime | SRC-1 `src/sift_kg/graph/postprocessor.py` | [EPI-CLM-explicit-extraction](#epi-clm-explicit-extraction) | Origin/destination semantics not preserved. | Implementation deduction, not observed bad extraction; scope is named mapping only. |
| [RT-RTE-graph-build](runtime.md#rt-rte-graph-build) | check/evidence production | implemented | [EPI-OBJ-graph-data](#epi-obj-graph-data) | no content change | Low confidence or configured review-required type | Threshold/type predicate; confidence metadata, not documents | After graph save | Review reason and YAML entry | Advisory flag | Check licenses only threshold/type finding | Schedules possible later review; does not quarantine | Reviewer; relation_review.yaml; advisory; later review call | SRC-1 `src/sift_kg/graph/builder.py` | none | none | Invalid direction type combinations can also be counted but kept. |
| [RT-RTE-graph-build](runtime.md#rt-rte-graph-build) | retention | implemented | [EPI-OBJ-graph-data](#epi-obj-graph-data) | no content change | Graph and communities | Build owner saves before flags | Build completion | Reloadable graph | Retention | Not demonstrated post-acceptance integration | Enables immediate retrieval including flagged claims | Query/narrate/export; saved files; permissive; later calls | SRC-1 `src/sift_kg/cli.py` | none | none | No supplied run trace. |
| [RT-RTE-entity-resolution](runtime.md#rt-rte-entity-resolution) | content transformation | implemented | [EPI-OBJ-review-state](#epi-obj-review-state) | truth-apt transformation: indeterminate | Entity identities to sameness/variant proposals | Model with selected fields; code normalized-name comparison | Resolve request | DRAFT proposals/reasons/confidence | Proposal only | Confidence not a calibrated identity warrant | Queues review, not surgery | Reviewer; YAML; advisory; later call | SRC-1 `src/sift_kg/resolve/resolver.py` | none | none | Identity equivalence may be compression or conjecture; limited payload cannot establish either for all proposals. |
| [RT-RTE-review-application](runtime.md#rt-rte-review-application) | check/evidence production | implemented | [EPI-OBJ-review-state](#epi-obj-review-state) | no content change | Merge minimum member confidence or relation confidence | Numeric threshold code; confidence domain only | Review invocation before interactive remainder | High/low threshold comparison | Result for automatic status setting | Numerical comparison only, not identity/factual validity | Supplies automated status decision | Review status writer; comparison result; permissive; current review | SRC-1 `src/sift_kg/resolve/reviewer.py` | [RT-CLM-merge-approval](runtime.md#rt-clm-merge-approval) | none | No independent oracle; code-generated confidence can also qualify. |
| [RT-RTE-review-application](runtime.md#rt-rte-review-application) | check/evidence production | implemented | [EPI-OBJ-review-state](#epi-obj-review-state) | no content change | Remaining candidate shown with reason/confidence or evidence | Interactive human; identity/relation validity judgment with unspecified criterion | Review invocation after automatic thresholds | Approve/reject/skip/quit | User-supplied result for status setting | Possible evidence-consuming judgment; actual evidence use, criterion and intended scope unobserved | Supplies manual status decision | Review status writer; terminal input; permissive; current review | SRC-1 `src/sift_kg/resolve/reviewer.py` | [RT-CLM-merge-approval](runtime.md#rt-clm-merge-approval) | none | Human review possible, not universally required; no supplied reviewer trace. |
| [RT-RTE-review-application](runtime.md#rt-rte-review-application) | disposition/acceptance | implemented | [EPI-OBJ-review-state](#epi-obj-review-state) | no content change | DRAFT to automatic CONFIRMED/REJECTED | Threshold code | Before interactive review and separate apply | Automated status persisted | Enforcing status admission | Operational disposition, not factual acceptance | Permits surgery/removal on later call | Apply engine; YAML statuses; permissive; until changed/applied | SRC-1 `src/sift_kg/resolve/models.py` | [RT-CLM-merge-approval](runtime.md#rt-clm-merge-approval) | Universal human approval contradicted by automation. | No supplied run trace. |
| [RT-RTE-review-application](runtime.md#rt-rte-review-application) | disposition/acceptance | implemented | [EPI-OBJ-review-state](#epi-obj-review-state) | no content change | DRAFT to manual status or direct YAML replacement | Human reviewer or unspecified file writer | Interactive review/file edit before separate apply | Chosen status persisted | Enforcing status admission | Human acceptance may occur; status alone records no evidence-consuming criterion/use/scope | Permits or withholds surgery/removal | Apply engine; terminal-to-YAML or direct YAML; permissive; until changed/applied | SRC-1 `src/sift_kg/resolve/models.py` | [RT-CLM-merge-approval](runtime.md#rt-clm-merge-approval) | none | Manual file authority is not authenticated; exact approver/evidence use unobserved. |
| [RT-RTE-review-application](runtime.md#rt-rte-review-application) | operational admission/selection/consumption | implemented | [EPI-OBJ-graph-data](#epi-obj-graph-data) | truth-apt transformation: indeterminate | Confirmed valid entity merges | Confirmed-status filter and node existence; not semantic re-evaluation | Separate apply request | Identity collapse, attribute/source aggregation, edge rewrites and self-loop dropping | Enforcing mutation | No additional source warrant; equivalence not rechecked against documents | Changes subsequent graph answers; old prose may remain | Query/narrate/view; saved graph; enforcing; until rebuild | SRC-1 `src/sift_kg/resolve/engine.py` | none | none | Rebuild does not preserve surgery automatically; no graph-revision binding. |
| [RT-RTE-review-application](runtime.md#rt-rte-review-application) | operational admission/selection/consumption | implemented | [EPI-OBJ-graph-data](#epi-obj-graph-data) | truth-apt transformation: non-ampliative reshaping | Rejected relation triples | REJECTED status and matching edge; not semantic re-evaluation | Separate apply request | Matching graph edges removed in both directions | Enforcing withdrawal | Withdraws operational use; neither proves falsity nor changes source truth | Removes graph assertions from later graph reads; no confirmed-variant insertion | Query/narrate/view; saved graph; enforcing; until rebuild | SRC-1 `src/sift_kg/resolve/engine.py` | none | none | Withdrawal not propagated to existing prose or exports; reverse removal may affect a separate assertion. |
| [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) | content transformation | implemented | [EPI-OBJ-derived-prose](#epi-obj-derived-prose) | truth-apt transformation: indeterminate | Graph/context to narrative/descriptions/labels | Completion model; bounded selected graph context | Narration request | Prose and labels | Automatic candidate output | Prompted factual restraint, not checked preservation | Makes prose available for search/view | Sidecar consumers; strings/files; permissive; later invocations | SRC-1 `src/sift_kg/narrate/generator.py` | none | none | Need paired graph/source/output checks; fluency alone does not establish conjecture or warranted derivation. |
| [EPI-RTE-style-rewrite](#epi-rte-style-rewrite) | check/evidence production | implemented | [EPI-OBJ-derived-prose](#epi-obj-derived-prose) | no content change | Banned phrase occurrences | Regex; linguistic-pattern domain | Before rewrite | Matches or no matches | Rewrite selection | Presence of matched style pattern only | Selects one rewrite pass | Rewrite caller; match list; enforcing selection; current generation | SRC-1 `src/sift_kg/narrate/generator.py` | none | none | Not a factual evaluator. |
| [EPI-RTE-style-rewrite](#epi-rte-style-rewrite) | content transformation | implemented | [EPI-OBJ-derived-prose](#epi-obj-derived-prose) | truth-apt transformation: indeterminate | Flagged text to replacement text | Model instructed not to change facts | One pass after matches | Rewritten prose or original on RuntimeError | Automatic replacement | No semantic equivalence check | Replacement can be saved/consumed | Narrator/sidecar reader; returned string; permissive; output lifetime | SRC-1 `src/sift_kg/narrate/generator.py` | none | none | Facts-preserving intent does not settle transformation class. |
| [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation) | retention | implemented | [EPI-OBJ-derived-prose](#epi-obj-derived-prose) | no content change | Prose/labels to files | Narration owner | After generation | Narrative and optional sidecars | Retention | No evidence-consuming factual acceptance required | Later search/view/topology may use derived content | Readers; sidecar files; permissive; across invocations | SRC-1 `src/sift_kg/narrate/generator.py` | none | none | Skipped generation need not delete stale sidecars. |
| [RT-RTE-graph-retrieval](runtime.md#rt-rte-graph-retrieval) | operational admission/selection/consumption | implemented | [EPI-OBJ-graph-data](#epi-obj-graph-data) | truth-apt transformation: non-ampliative reshaping | Saved graph to selected neighborhood | Exact/substring/type matching, degree rank, BFS | Caller query/search | Selected records/evidence; other matches | Ranking and delivery | Graph-relative representation only; rank is not truth | Chooses delivered candidate and context | Host; JSON/text; ranking then advisory; current request | SRC-1 `src/sift_kg/cli.py` | [EPI-CLM-graph-grounding](#epi-clm-graph-grounding) | none | Pending flags do not filter results; full raw sources/mentions not delivered. |
| [RT-RTE-graph-retrieval](runtime.md#rt-rte-graph-retrieval) | content transformation | implemented | [EPI-OBJ-structural-results](#epi-obj-structural-results) | truth-apt transformation: entailed derivation | Counts/reachability/membership of loaded graph | Fixed graph algorithms over stored state | Info/topology/query request | Graph-relative structural propositions | Computational derivation | Only relative to loaded graph and chosen representation; not real-world completeness | Ranks bridges/matches and guides navigation | Host; computed JSON; ranking/advisory; request/session | SRC-1 `src/sift_kg/cli.py` | none | none | Graph premises are not warranted real-world facts; dependency execution unobserved. |
| [RT-RTE-view-export](runtime.md#rt-rte-view-export) | operational admission/selection/consumption | implemented | [EPI-OBJ-graph-data](#epi-obj-graph-data) | truth-apt transformation: non-ampliative reshaping | Saved graph to reader/export | Format/filter rules; some exports strip provenance | Caller view/export | Reader-facing graph subset/attributes | Delivery | No new factual warrant; lineage detail may be degraded | Enables browser/downstream reliance | External readers; HTML/export; advisory; artifact lifetime | SRC-1 `src/sift_kg/export.py` | none | none | No observed reader behavior. |

No lifecycle-integration row is asserted: retention, proposed semantic identities and graph connections are implemented, but a preceding evidence-consuming acceptance decision with criterion, intended use and scope is not established by those facts. This is a limit on that classification within the inspected production/review/consumer routes, not a prohibition on a careful human accepting content.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-merge-approval](runtime.md#rt-clm-merge-approval) | see record | SRC-1 `README.md`; doctrine/design | Human review and YAML editing exist; README also explicitly documents defaults | [RT-RTE-graph-build](runtime.md#rt-rte-graph-build), [RT-RTE-review-application](runtime.md#rt-rte-review-application) | None supplied | No intervention; threshold confidence not factual validation | Confirmed-status gate for surgery, not universal human approval; source fields afford traceability | Pre-dedup and auto-confirmation defeat literal universal approval; quotes unchecked. |
| [EPI-CLM-explicit-extraction](#epi-clm-explicit-extraction) | see record | SRC-1 `src/sift_kg/extract/prompts.py`; doctrine/design | Explicit-only/source-quote instructions | [EPI-RTE-extraction-shape](#epi-rte-extraction-shape), [EPI-RTE-relation-normalization](#epi-rte-relation-normalization) | None supplied | No accuracy experiment | Implemented policy request, shape gate and automatic postprocessing | No source-entailment gate; normalization can introduce an unsupported destination proposition. |
| [EPI-CLM-graph-grounding](#epi-clm-graph-grounding) | see record | SRC-1 `.agents/skills/sift-kg/SKILL.md`; doctrine/design | Graph-first response policy and topology/query instructions | [RT-RTE-graph-retrieval](runtime.md#rt-rte-graph-retrieval), [RT-BAP-agent-skill](runtime.md#rt-bap-agent-skill) | None supplied | External host compliance and answer benefit not measured | Persistent lookup interface and advisory host protocol | Graph-derived answer is not necessarily source-true; disconnected graph components need not be disconnected in the world. |

## Bounded conclusion

sift-kg acquires document content with unknown source warrant, produces model-interpreted candidates, and retains both structured assertions and derived prose. The extraction gate checks data shape/ranges, not proposition truth or quotation identity. Model summaries, identity proposals and prose are semantically indeterminate without paired evidence; they are not automatically licensed as entailed extraction or accepted ampliative knowledge. See [EPI-RTE-extraction-shape](#epi-rte-extraction-shape), [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction), [RT-RTE-entity-resolution](runtime.md#rt-rte-entity-resolution), [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation).

Build is consequential, not mere formatting: automatic name collapse, domain typing, edge removal/direction changes and normalization change what later callers receive. The specific origin-to-destination mapping is demonstrably non-entailed by a concrete source-level case; it is not an observed incident. Review flags are produced after graph publication. Rejected-edge application withdraws graph content but does not establish withdrawal from preexisting prose, communities or already exported views. See [EPI-RTE-relation-normalization](#epi-rte-relation-normalization), [RT-RTE-graph-build](runtime.md#rt-rte-graph-build), [RT-RTE-review-application](runtime.md#rt-rte-review-application).

The material operational criteria are shape success for extraction, type/normalization rules for build, confidence/type flags for review, confidence thresholds or human choice for statuses, confirmed status plus node existence for surgery, and regex occurrence for rewriting. Their intended operational uses and scopes are in the ledger. None should be promoted to a system-wide truth oracle. Human evidence-consuming acceptance is possible but not established as a required or observed event. Retention, schema reuse and operational integration before such acceptance remain separately supported functions, not lifecycle integration as defined here.

Structural outputs derive facts about the saved graph; their license stops there. Retrieval, visualization and exports select/reshape that representation and can omit lineage detail. Host instructions grant it advisory answer-shaping authority, while sift-kg itself neither schedules sessions nor verifies final host answers. These paths do not demonstrate improved capacity, exercised reflection, self-improvement or all theory-builder conditions. Schema-directed behavior change is supported independently of those properties; see [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery). Distributed-parametric internals remain bounded as stated in the component records. No observed activation, extraction reliability, causal benefit or unqualified epistemic verdict follows.

## Shared records

### Operative objects

#### EPI-OBJ-document-text
Label: Document text

Part of: [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction)

This object is the material state part of the parent route, not a second route. Source-native identity, form and substrate: Reader-returned string and chunks, natural-language assertions in transient Python strings; upstream file is external input. Evidence: SRC-1 `src/sift_kg/extract/extractor.py`; the parent supplies the broad production/read-back account and passages where available. No supplied object counterpart: runtime declares no operative objects.

#### EPI-OBJ-document-summary
Label: Document context summary

Part of: [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction)

This object is the material state part of the parent route, not a second route. Source-native identity, form and substrate: Generated 2–3 sentence natural-language summary in transient Python string, delivered to subsequent chunk calls; no independent retained summary file established. Evidence: SRC-1 `src/sift_kg/extract/extractor.py`; the parent supplies the broad production/read-back account and passages where available. No supplied object counterpart: runtime declares no operative objects.

#### EPI-OBJ-domain-config
Label: DomainConfig guidance

Part of: [RT-RTE-schema-discovery](runtime.md#rt-rte-schema-discovery)

This object is the material state part of the parent route, not a second route. Source-native identity, form and substrate: Symbolic type names/source-target constraints and natural-language descriptions in Python configuration and reusable discovered_domain.yaml. Parts have different consumers: code interprets constraints, models interpret descriptions. Evidence: SRC-1 `src/sift_kg/domains/discovery.py`; the parent supplies the broad production/read-back account and passages where available. No supplied object counterpart: runtime declares no operative objects.

#### EPI-OBJ-extracted-content
Label: DocumentExtraction content

Part of: [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction)

This object is the material state part of the parent route, not a second route. Source-native identity, form and substrate: Natural-language names, assertions, contexts and evidence inside symbolic Pydantic records and per-document JSON; confidence is numerical metadata with fixed range checks, not distributed-parametric state. Evidence: SRC-1 `src/sift_kg/extract/models.py`; the parent supplies the broad production/read-back account and passages where available. No supplied object counterpart: runtime declares no operative objects.

#### EPI-OBJ-graph-data
Label: KnowledgeGraph content

Part of: [RT-RTE-graph-build](runtime.md#rt-rte-graph-build)

This object is the material state part of the parent route, not a second route. Source-native identity, form and substrate: NetworkX MultiDiGraph saved as graph_data.json; symbolic nodes/edges route selection while natural-language names/evidence receive human/model interpretation. Evidence: SRC-1 `src/sift_kg/graph/builder.py`; the parent supplies the broad production/read-back account and passages where available. No supplied object counterpart: runtime declares no operative objects.

#### EPI-OBJ-review-state
Label: Merge and relation review state

Part of: [RT-RTE-review-application](runtime.md#rt-rte-review-application)

This object is the material state part of the parent route, not a second route. Source-native identity, form and substrate: Natural-language identity reasons/evidence plus symbolic DRAFT/CONFIRMED/REJECTED controls in Python/YAML; status governs mutation, reason does not itself enforce correctness. Evidence: SRC-1 `src/sift_kg/resolve/models.py`; the parent supplies the broad production/read-back account and passages where available. No supplied object counterpart: runtime declares no operative objects.

#### EPI-OBJ-derived-prose
Label: Narrative and descriptive sidecars

Part of: [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation)

This object is the material state part of the parent route, not a second route. Source-native identity, form and substrate: Natural-language narrative Markdown, descriptions and community labels in saved sidecars; interpreted by readers/host, labels also attached to structural outputs. Evidence: SRC-1 `src/sift_kg/narrate/generator.py`; the parent supplies the broad production/read-back account and passages where available. No supplied object counterpart: runtime declares no operative objects.

#### EPI-OBJ-structural-results
Label: Graph-relative retrieval results

Part of: [RT-RTE-graph-retrieval](runtime.md#rt-rte-graph-retrieval)

This object is the material state part of the parent route, not a second route. Source-native identity, form and substrate: Symbolic computed counts, ranks, adjacency and membership with natural-language display labels, delivered as JSON/text; transient result, underlying graph/communities retained. Evidence: SRC-1 `src/sift_kg/cli.py`; the parent supplies the broad production/read-back account and passages where available. No supplied object counterpart: runtime declares no operative objects.

Load-bearing extraction object definitions (SRC-1 implementation):

> confidence: float = Field(default=0.5, ge=0.0, le=1.0)
> context: str = ""  # Quote from source text
> --- `src/sift_kg/extract/models.py`

> confidence: float = Field(default=0.5, ge=0.0, le=1.0)
> evidence: str = ""  # Quote from source text
> --- `src/sift_kg/extract/models.py`

Summary content and delivery (SRC-1 implementation):

> "Summarize this document excerpt in 2-3 sentences. "
> "Focus on: what type of document this is, who the key participants are, "
> --- `src/sift_kg/extract/extractor.py`

### Routes

#### EPI-RTE-extraction-shape
Label: Extraction item shape check and admission

Part of: [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction)

Distinct material part: JSON response item construction and skip/append, not the parent document-processing route. SRC-1 implementation: `src/sift_kg/extract/extractor.py`, `src/sift_kg/extract/models.py`. Model proposes; Pydantic/float conversion decide computational constructibility; loop admits or skips. There is no human veto call here, expected-answer oracle or bounded experiment. Trigger is a returned chunk response; unchanged extraction prompt guides content, typed assertions persist; retries/force and file editing are recovery, not authenticated rollback. A false relation with valid strings and confidence 0.9 satisfies these model fields: the check domain is shape, not document entailment.

- Immediate return: Shape-valid ExtractedEntity/ExtractedRelation items in ExtractionResult, or skipped malformed items.
- Later read-back: Accepted-shape records enter DocumentExtraction JSON and later build/narration/cache consumers.
- Delegated visibility: Provider already saw chunk and guidance; this check makes no further external call.
- Selection predicate: Entities/relations arrays returned by acall_json; fields constructed with defaults and confidence conversion.
- Invalidation or expiry: Parent force/config-staleness path or input-file edits; no item truth expiry.
- Activation or effect: append admits constructed items; caught item errors skip them.
- Evidence limits: Inspected source only; no document comparison or calibrated confidence established by these checks.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> except (ValueError, TypeError, KeyError) as e:
>     logger.debug(f"Skipping malformed relation: {e}")
> --- `src/sift_kg/extract/extractor.py`

#### EPI-RTE-relation-normalization
Label: Undefined relation normalization

Part of: [RT-RTE-graph-build](runtime.md#rt-rte-graph-build)

Distinct material part: normalize_relation_types, not the entire build. SRC-1 implementation: `src/sift_kg/graph/postprocessor.py`, `src/sift_kg/graph/builder.py`. A static table proposes mapping, Python decides without human approval, no expected-answer oracle or outcome comparison. Trigger is enabled postprocessing plus domain types; a valid input type bypasses mapping. Unknown types otherwise use synonyms or ASSOCIATED_WITH fallback. Recovery is dry-run for direct callers, disabled postprocessing/rebuild or external backup; the saved graph retains the new relation label and existing evidence, not a checked interpretation proof.

Concrete source-level deduction, not execution: let the graph contain Alice TRAVELED_FROM Paris, and let domain_types contain TRAVELED_TO but not TRAVELED_FROM. Membership does not bypass this edge. The table chooses TRAVELED_TO; assignment changes relation_type with the same endpoints. The result asserts Alice traveled to Paris. A trip originating in Paris and ending in Rome satisfies the input but not the output, proving non-entailment under the ordinary relation meanings. This particular deterministic rule thus introduces an ampliative conjecture; the rest of normalization is not assigned that classification wholesale. The retained evidence field is not rechecked against the new predicate. Explicit passive-pair inversion can preserve meaning, a counterexample to calling every graph rewrite conjecture; heuristic inversion and schema-direction fixing still require an interpretation check for source-level warrant.

- Immediate return: Normalization counts/mappings and in-place graph edit unless dry_run.
- Later read-back: Saved graph is consumed by retrieval, resolve, narrate, view and export.
- Delegated visibility: No provider call in this function; later readers receive the changed predicate.
- Selection predicate: Nonempty nonmetadata relation type not already in a nonempty valid set; known synonym or fallback.
- Invalidation or expiry: Explicit rebuild/repair; no attached semantic expiry or per-edge undo.
- Activation or effect: relation_type assignment changes future graph assertions automatically.
- Evidence limits: Deduction establishes conditional implementation behavior, not occurrence in supplied corpus or error frequency; interpretation assumes ordinary origin/destination meanings.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "TRAVELED_FROM": "TRAVELED_TO",
> --- `src/sift_kg/graph/postprocessor.py`

> if valid and rel_type in valid:
>     continue
> --- `src/sift_kg/graph/postprocessor.py`

> if not dry_run:
>     kg.graph.edges[source, target, key]["relation_type"] = mapped
> --- `src/sift_kg/graph/postprocessor.py`

Counterexample to treating cleanup as rejection enforcement:

> stats["relations_invalid"] += 1
> --- `src/sift_kg/graph/postprocessor.py`

> f"entity types outside schema constraints (kept as-is)"
> --- `src/sift_kg/graph/postprocessor.py`

#### EPI-RTE-style-rewrite
Label: Banned phrase detection and rewrite

Part of: [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation)

Distinct material part: _find_banned_phrases, _rewrite_banned_phrases and async description rewriting. SRC-1 implementation: `src/sift_kg/narrate/generator.py`. Code selects a style defect, model proposes replacement, code accepts returned string; caller can edit files but no human/content oracle is required. Domain is regex phrase occurrence, not factual entailment. This is open text rewriting under static guidance, not a measured improvement experiment or revision of explanatory theory. Rejection/recovery is original-text fallback on RuntimeError; there is no subsequent equivalence comparison or mandatory repeated style check in these bodies.

- Immediate return: Match strings, then original or replacement prose.
- Later read-back: Resulting prose enters parent's saved narrative/description outputs for readers/search/view.
- Delegated visibility: Flagged full prose and forbidden-phrase list reach completion provider.
- Selection predicate: At least one banned regex match; descriptions without matches retain original text.
- Invalidation or expiry: New narration or external editing; no factual freshness check.
- Activation or effect: Matches select rewriting; returned strings replace originals in generator flow.
- Evidence limits: Source-only; prompt prohibition on factual changes is not a semantic invariant or observed preservation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> for pattern in _BANNED_PATTERNS:
>     for m in pattern.finditer(text):
>         matches.append(m.group(0))
> --- `src/sift_kg/narrate/generator.py`

> return {eid: fixed.get(eid, desc) for eid, desc in descriptions.items()}
> --- `src/sift_kg/narrate/generator.py`

Parent retains exact rewrite instruction passage; see [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation).

### Claims

#### EPI-CLM-explicit-extraction
Label: Explicit source-supported extraction policy

SRC-1 doctrine/design, `src/sift_kg/extract/prompts.py`. This claim is the model extraction policy, distinct from the approval/source-linkage statement [RT-CLM-merge-approval](runtime.md#rt-clm-merge-approval). Literal instruction is not a measured compliance result; subsequent graph normalization has independent semantic risks.

> - Only extract relationships that are explicitly stated in the text and match a defined relation type
> - Do not infer relationships from co-occurrence alone
> --- `src/sift_kg/extract/prompts.py`

#### EPI-CLM-graph-grounding
Label: Persistent graph grounds host responses

SRC-1 doctrine/design, `.agents/skills/sift-kg/SKILL.md`. This warrant claim is distinct from merge approval and from the directive's behavioral-authority path [RT-BAP-agent-skill](runtime.md#rt-bap-agent-skill). The latter establishes a host protocol, not that its responses are source-true.

> **Treat the graph as your persistent understanding of the user's world.** When the user asks about their projects, domain, or knowledge — check the graph first. It grounds your responses in real entities and relationships instead of guessing. You don't need to query it for every interaction, but for anything related to the user's work or knowledge, the graph should inform your answer.
> --- `.agents/skills/sift-kg/SKILL.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; paths are specified in ledger and supplied runtime records.
