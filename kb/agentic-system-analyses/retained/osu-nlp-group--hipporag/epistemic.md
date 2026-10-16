---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "HippoRAG epistemic routes: passage acquisition, model extraction, structural admission, relevance selection and answer evaluation."
run-id: AAS-2026-10-16-hipporag-2b37edfc7ade-01
reviewed-boundary: d5c8329422e0a0b834a15874545cb6a74b4f9b26
---

# HippoRAG epistemic report

## Source-and-claim boundary

The question is which content HippoRAG acquires or produces, what checks license reliance on it, and which later consumers give those results force. Scope, external dependencies and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identities and layers are see [Source register](boundary.md#source-register). All source anchors below refer to SRC-1 at the frozen revision. Direct reads supply implementation or doctrine/design evidence, never observed operation. No target execution, supplied run trace or causal comparison establishes realized accuracy or benefit.

The material routes assessed are passage import, NER/relation generation, parsing and structural disposition, normalization, persistence and reuse, provenance/compatibility checks, deletion, fact relevance filtering, graph/dense selection, QA, IRCoT, benchmark evaluation and host-guided checking. Storage and transport enter this account only where they preserve lineage or carry these results to consumers. Model weights and external services are excluded internals; their actual judgments, weight identity and any internal learning are not determinable. Available but uninspected alternatives below preclude a system-complete negative about semantic checks or knowledge production.

| Entry point or operation | Source path (SRC-1) | Coverage and prevented conclusion |
| --- | --- | --- |
| CLI experiment and method selection | `main.py` | Direct complete read; see [EPI-RTE-metric-evaluation](#epi-rte-metric-evaluation), [RT-RTE-standard-rag](runtime.md#rt-rte-standard-rag). Gold labels are post-generation references. |
| MCP executable, transports, tools, resource and lifecycle hooks | `pyproject.toml`; `src/hipporag/mcp_server.py` | Direct script registration, helpers, tool registration and CLI reads; service queue/cleanup supplied by [RT-RTE-mcp-tools](runtime.md#rt-rte-mcp-tools). All five tools and config resource accounted for; no separate evaluator dispatched by these wrappers. |
| Plugin launcher and host instructions | `plugins/hipporag/.claude-plugin/plugin.json`; `plugins/hipporag/skills/hipporag-memory/SKILL.md` | Direct complete reads; see [EPI-RTE-host-check](#epi-rte-host-check), [EPI-CLM-call-guidance](#epi-clm-call-guidance). No host adherence evidence. Folder preparation skill supplied via [RT-BAP-plugin-skills](runtime.md#rt-bap-plugin-skills), not directly reread. |
| Index, delete, source contribution withdrawal | `src/hipporag/HippoRAG.py` | Direct index/delete/helper reads; see [RT-RTE-index-state](runtime.md#rt-rte-index-state), [EPI-RTE-text-normalization](#epi-rte-text-normalization). |
| Extraction and triple cleanup | `src/hipporag/information_extraction/openie_openai.py`; `src/hipporag/utils/llm_utils.py`; `src/hipporag/utils/misc_utils.py` | Direct online extractor, triple validator and normalization/reformat helpers; see [EPI-RTE-openie-generation](#epi-rte-openie-generation), [EPI-RTE-triple-check](#epi-rte-triple-check), [EPI-RTE-triple-admission](#epi-rte-triple-admission). |
| Normal retrieve, fact filter, PPR, direct QA and evaluated QA | `src/hipporag/HippoRAG.py`; `src/hipporag/rerank.py` | Direct retrieve/build-result, rerank/PPR, QA and rag_qa dispatch reads; see [EPI-RTE-fact-check](#epi-rte-fact-check), [EPI-RTE-fact-selection](#epi-rte-fact-selection), [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer). Seed-weight internals supplied by runtime, not independently audited here. |
| IRCoT | `src/hipporag/HippoRAG.py`; `src/hipporag/utils/qa_utils.py` | Direct retrieve_ircot/answer_with_ircot; prompt helper supplied by [RT-RTE-ircot-retrieval](runtime.md#rt-rte-ircot-retrieval). |
| QA, extraction and filter guidance | `src/hipporag/prompts/templates/rag_qa_musique.py`; `src/hipporag/prompts/templates/triple_extraction.py`; `src/hipporag/prompts/filter_default_prompt.py` | Direct reads; static guidance, not a record of runtime criticism or optimization. Other dataset templates and configured DSPy JSON uninspected here; no universal prompt-content conclusion. |
| Metrics and answer normalization | `src/hipporag/evaluation/qa_eval.py`; `src/hipporag/evaluation/retrieval_eval.py`; `src/hipporag/utils/eval_utils.py` | Direct complete reads; see [EPI-RTE-metric-evaluation](#epi-rte-metric-evaluation). |
| Compatibility, reload, response caches | `src/hipporag/utils/state_utils.py`; `src/hipporag/embedding_store.py`; `src/hipporag/llm/openai_gpt.py`; `tests/integration/_shared.py` | Supplied [RT-CLM-state-compatibility](runtime.md#rt-clm-state-compatibility), [RT-RTE-index-state](runtime.md#rt-rte-index-state), [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer); not independently reread. No crash/replay experiment. |
| Offline extraction, StandardRAG and direct DPR | `src/hipporag/information_extraction/openie_vllm_offline.py`; `src/hipporag/information_extraction/openie_transformers_offline.py`; `src/hipporag/StandardRAG.py`; `src/hipporag/HippoRAG.py` | Supplied [RT-RTE-offline-extraction](runtime.md#rt-rte-offline-extraction), [RT-RTE-standard-rag](runtime.md#rt-rte-standard-rag), [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer). These alternatives refute universal online fail-fast or graph-filter claims. |
| Other adapters, remote stores, examples, bulk fixtures/datasets, tests | `src/hipporag/llm/`; `src/hipporag/embedding_model/`; `src/hipporag/vector_store/`; `examples/`; `outputs/`; `reproduce/`; `tests/` | Available but not independently inspected here, except named supplied runtime scopes. No complete enumeration of injected/backend behavior, fixture provenance, reference quality or provider semantics. |

Consequential design claims are see [EPI-CLM-memory-connections](#epi-clm-memory-connections), [EPI-CLM-grounded-answer](#epi-clm-grounded-answer), [EPI-CLM-call-guidance](#epi-clm-call-guidance) and [RT-CLM-state-compatibility](runtime.md#rt-clm-state-compatibility). None is treated as empirical validation.

## Epistemic-object inventory

The inventory separates content from selectors and compatibility metadata. A vector or graph score does not independently state the truth of the associated passage or triple.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-passages](#epi-obj-passages) | see record | see record | SRC-1: `src/hipporag/HippoRAG.py` | see record |
| [EPI-OBJ-openie-triples](#epi-obj-openie-triples) | see record | see record | SRC-1: `src/hipporag/information_extraction/openie_openai.py` | see record |
| [EPI-OBJ-normalized-facts](#epi-obj-normalized-facts) | see record | see record | SRC-1: `src/hipporag/utils/misc_utils.py` | see record |
| [EPI-OBJ-answer-thoughts](#epi-obj-answer-thoughts) | see record | see record | SRC-1: `src/hipporag/HippoRAG.py` | see record |
| [RT-OBJ-index-manifest](runtime.md#rt-obj-index-manifest) | Compatibility assertions, not passage truth; see record | see record | SRC-1: `src/hipporag/utils/state_utils.py` | see record |
| [RT-CMP-extraction-llm](runtime.md#rt-cmp-extraction-llm), [RT-CMP-qa-llm](runtime.md#rt-cmp-qa-llm), [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model), [RT-CMP-vllm-offline](runtime.md#rt-cmp-vllm-offline), [RT-CMP-transformers-offline](runtime.md#rt-cmp-transformers-offline) | Not determinable as individuated propositions in weights; see records | see records | SRC-1: `src/hipporag/HippoRAG.py` | see records; no inference from opaque weights to absent learning |

## Authority-route ledger

Each compact entry separates its function and transformation assessment from the declaring record's fields. Fields marked “see” are owned by that record; the ledger assigns architectural status. All implementation statuses concern wiring, not exercised behavior.

Route ID: [RT-RTE-index-state](runtime.md#rt-rte-index-state)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-passages](#epi-obj-passages).
Content/update relation: truth-apt transformation: acquisition/import; source warrant unknown, not certified by admission.
Transition or check target: caller document to retained passage; remaining route fields, evidence and claim scope: see record. Claimed warrant comparison: [EPI-CLM-memory-connections](#epi-clm-memory-connections). Gap: imported content is not produced knowledge.

Route ID: [EPI-RTE-openie-generation](#epi-rte-openie-generation)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-openie-triples](#epi-obj-openie-triples).
Content/update relation: truth-apt transformation: indeterminate; requested extraction may preserve or derive source relations, or add unsupported propositions. No paired runtime input/output establishes entailment or non-entailment.
Other ledger fields: see record. Claim: [EPI-CLM-memory-connections](#epi-clm-memory-connections). Mismatch: generation is not acceptance.

Route ID: [EPI-RTE-triple-check](#epi-rte-triple-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-openie-triples](#epi-obj-openie-triples).
Content/update relation: no content change (the assessment of structural validity); cleanup consequences are the linked disposition below.
Other ledger fields: see record. Claim IDs: none. Gap: syntactic checks do not check asserted relations against passages.

Route ID: [EPI-RTE-triple-admission](#epi-rte-triple-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-openie-triples](#epi-obj-openie-triples).
Content/update relation: truth-apt transformation: non-ampliative reshaping (structural filtering and exact deduplication).
Other ledger fields: see record. Claim IDs: none. Mismatch: software admission for indexing, not epistemic acceptance of source truth.

Route ID: [EPI-RTE-text-normalization](#epi-rte-text-normalization)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-normalized-facts](#epi-obj-normalized-facts).
Content/update relation: truth-apt transformation: indeterminate; case/punctuation loss can collapse distinct referents. It is not established as universally meaning-preserving reshaping or a checked entailed derivation.
Other ledger fields: see record. Claim: [EPI-CLM-memory-connections](#epi-clm-memory-connections). Gap: original passages remain available, limiting but not eliminating the effect on selection.

Route ID: [RT-RTE-index-state](runtime.md#rt-rte-index-state)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-passages](#epi-obj-passages), [EPI-OBJ-openie-triples](#epi-obj-openie-triples), [EPI-OBJ-normalized-facts](#epi-obj-normalized-facts).
Content/update relation: no content change (saving and reopening already-admitted material).
Other ledger fields: see record. Claim: [EPI-CLM-memory-connections](#epi-clm-memory-connections). Mismatch: retention and graph connection occur without a recorded evidence-consuming semantic acceptance decision; they are not lifecycle integration after acceptance.

Route ID: [RT-CLM-state-compatibility](runtime.md#rt-clm-state-compatibility), [RT-RTE-index-state](runtime.md#rt-rte-index-state)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [RT-OBJ-index-manifest](runtime.md#rt-obj-index-manifest).
Content/update relation: no content change (identity/provenance checks and retrieval invalidation).
Other ledger fields: see records. Claim: [RT-CLM-state-compatibility](runtime.md#rt-clm-state-compatibility). Gap: checked configuration equality is not immutable weight identity, semantic truth or a transaction.

Route ID: [RT-RTE-index-state](runtime.md#rt-rte-index-state)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-passages](#epi-obj-passages), [EPI-OBJ-normalized-facts](#epi-obj-normalized-facts).
Content/update relation: truth-apt transformation: non-ampliative reshaping (withdraw selected sources and unreferenced derivatives).
Other ledger fields: see record; direct deletion evidence also in [EPI-OBJ-normalized-facts](#epi-obj-normalized-facts). Claim IDs: none. Gap: caller-directed withdrawal, not a falsity judgment; shared assertions can survive another source's deletion.

Route ID: [EPI-RTE-fact-check](#epi-rte-fact-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-normalized-facts](#epi-obj-normalized-facts).
Content/update relation: no content change (query-relevance judgment).
Other ledger fields: see record. Claim: [EPI-CLM-call-guidance](#epi-clm-call-guidance). Gap: model judgment is not a reference-answer oracle or truth test.

Route ID: [EPI-RTE-fact-selection](#epi-rte-fact-selection)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-normalized-facts](#epi-obj-normalized-facts).
Content/update relation: truth-apt transformation: non-ampliative reshaping (select candidate tuples; returned tuples come from candidates).
Other ledger fields: see record. Claim: [EPI-CLM-call-guidance](#epi-clm-call-guidance). Mismatch: approximate remapping with cutoff zero enforces candidate membership, not faithful model selection or relevant truth.

Route ID: [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer), [RT-RTE-standard-rag](runtime.md#rt-rte-standard-rag)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-passages](#epi-obj-passages).
Content/update relation: truth-apt transformation: non-ampliative reshaping (rank and deliver original passage texts).
Other ledger fields: see records. Claims: [EPI-CLM-memory-connections](#epi-clm-memory-connections), [EPI-CLM-grounded-answer](#epi-clm-grounded-answer). Gap: ranking force affects model context, not epistemic endorsement. Filter bypass/DPR and caller-supplied solutions bound the ordinary graph route.

Route ID: [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-answer-thoughts](#epi-obj-answer-thoughts).
Content/update relation: truth-apt transformation: indeterminate; evidence does not decide whether actual answers restate, entail from, or go beyond selected premises.
Other ledger fields: see record; parsing evidence in [EPI-OBJ-answer-thoughts](#epi-obj-answer-thoughts). Claim: [EPI-CLM-grounded-answer](#epi-clm-grounded-answer). Gap: no semantic correctness gate precedes answer return in inspected QA.

Route ID: [RT-RTE-ircot-retrieval](runtime.md#rt-rte-ircot-retrieval)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-answer-thoughts](#epi-obj-answer-thoughts).
Content/update relation: no content change (consume generated thought as query or termination signal); thought production itself remains indeterminate as above.
Other ledger fields: see record. Claim IDs: none. Gap: literal answer marker and step limit terminate search, not verify an answer. Thought-directed continuation can change selection without accepting a claim.

Route ID: [EPI-RTE-metric-evaluation](#epi-rte-metric-evaluation)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-answer-thoughts](#epi-obj-answer-thoughts), [EPI-OBJ-passages](#epi-obj-passages).
Content/update relation: no content change (compute comparison scores).
Other ledger fields: see record. Claim: [EPI-CLM-grounded-answer](#epi-clm-grounded-answer). Gap: comparison is relative to supplied references and normalization; no threshold consuming scores as knowledge acceptance or automatic method revision in inspected driver.

Route ID: [EPI-RTE-host-check](#epi-rte-host-check)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-answer-thoughts](#epi-obj-answer-thoughts).
Content/update relation: no content change (requested comparison to returned passages).
Other ledger fields: see record. Claim: [EPI-CLM-grounded-answer](#epi-clm-grounded-answer). Gap: host performance, disposition and adherence not supplied; skill instruction does not establish an enforcing server gate.

No semantic acceptance or subsequent lifecycle integration route was found in the directly inspected online index, filter, QA, benchmark driver and MCP wrappers. That is a bounded finding, not a system-complete absence: arbitrary injections, other adapters and external host behavior are not resolved by those reads. Offline staging and parsing differences are see [RT-RTE-offline-extraction](runtime.md#rt-rte-offline-extraction); response reuse is see [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer). Neither supplies semantic acceptance evidence.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-memory-connections](#epi-clm-memory-connections) | see record | SRC-1: `README.md`; doctrine/design | see record | [RT-RTE-index-state](runtime.md#rt-rte-index-state), [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer), [EPI-RTE-openie-generation](#epi-rte-openie-generation), [EPI-RTE-text-normalization](#epi-rte-text-normalization) | None supplied | No experiment; graph structure is not a truth certificate | Retains documents and model-derived links that can influence retrieval | Reliable recognition, biological analogy and retrieval benefit unestablished |
| [EPI-CLM-grounded-answer](#epi-clm-grounded-answer) | see record | SRC-1: `src/hipporag/mcp_server.py`; doctrine/design | see record | [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer), [EPI-RTE-metric-evaluation](#epi-rte-metric-evaluation), [EPI-RTE-host-check](#epi-rte-host-check) | None supplied | References are answer-form comparisons; host check only guidance | Passages reach QA and are returned to permit inspection | Grounding means conditioned generation here, not demonstrated factual support |
| [EPI-CLM-call-guidance](#epi-clm-call-guidance) | see record | SRC-1: `plugins/hipporag/skills/hipporag-memory/SKILL.md`; doctrine/design | see record | [EPI-RTE-openie-generation](#epi-rte-openie-generation), [EPI-RTE-fact-check](#epi-rte-fact-check), [RT-RTE-mcp-tools](runtime.md#rt-rte-mcp-tools) | None supplied | No measured costs; cache hits and bypasses alter counts | Default retrieval includes generative fact filtering; online extraction has two stages | Universal no-call/one-call guidance contradicted by wired paths |
| [RT-CLM-state-compatibility](runtime.md#rt-clm-state-compatibility) | see record | SRC-1: `src/hipporag/utils/state_utils.py`; implementation | see record | [RT-RTE-index-state](runtime.md#rt-rte-index-state) | see record | see record | Compatibility over checked identities, not semantic endorsement | Provider drift, partial writes and manually altered state remain limits |

## Bounded conclusion

HippoRAG acquires caller passages and retains them together with model-extracted structures. Source warrant is unknown, not strengthened by a content hash, graph membership or persistence. Its symbolic checks license parseability, arity, deduplication and recorded identity compatibility for indexing and reuse. They do not license the truth of the source or extracted relations. The original passage route remains distinct from potentially lossy normalized graph facts: see [EPI-OBJ-passages](#epi-obj-passages), [EPI-RTE-triple-admission](#epi-rte-triple-admission), [EPI-RTE-text-normalization](#epi-rte-text-normalization) and [RT-CLM-state-compatibility](runtime.md#rt-clm-state-compatibility).

Fact filtering evaluates query relevance, then selection grants ranking force through graph seeds or dense fallback. Only selected passage text reaches QA; the ordinary graph is not itself an answer oracle. Answers and IRCoT thoughts are candidates whose semantic transformation class is indeterminate without paired outputs and warranted premises. No produced accepted ampliative claim is established, but this does not assert that no model ever conjectures or derives anything. See [EPI-RTE-fact-check](#epi-rte-fact-check), [EPI-RTE-fact-selection](#epi-rte-fact-selection), [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer), [RT-RTE-ircot-retrieval](runtime.md#rt-rte-ircot-retrieval).

For benchmark answers, the implemented criteria are normalized alias exact match and token F1; passage retrieval uses exact-text reference recall. Their intended use is reporting benchmark agreement, not content admission. Their consumers log and return scores. No inspected threshold accepts claims for later reliance or connects such acceptance to retained knowledge. Host instructions ask for answer checking, but neither a completed judgment nor its consequence is evidenced. Retention and caller-directed deletion operate independently of semantic acceptance: see [EPI-RTE-metric-evaluation](#epi-rte-metric-evaluation), [EPI-RTE-host-check](#epi-rte-host-check), [RT-RTE-index-state](runtime.md#rt-rte-index-state).

Direct behavioral effects do not require truth acceptance: empty fact output forces dense fallback, generated thoughts select further retrieval, and a marker stops IRCoT. These are per-call policy effects, not evidenced retained method improvement. No observed benefit, causal component effect, improved future capacity, reflective criticism loop or self-improvement follows from the supplied implementation evidence. These are independent limits, not one system-wide score. Distributed-parametric fixity and provenance limits remain see the component records in the inventory; inaccessible internals establish neither the presence nor the absence of learning.

## Shared records

### Operative objects

#### EPI-OBJ-passages
Label: Passage contents

Part of: [RT-RTE-index-state](runtime.md#rt-rte-index-state)

Source-native identity: `chunk_texts` and chunk-store row `content`. This is a material content part of the parent's indexing route, not another name for the route. Natural-language passages persist in the configured chunk embedding store alongside numerical vectors and separate symbolic metadata; the text, vectors and metadata have different consumption paths. Passages can state truths over their source's domain, but arbitrary input may also contain instructions or nonassertive text. Caller provenance is not independent source verification. The graph selector eventually returns original stored text, not normalized triple text. Closest supplied result container is [RT-OBJ-query-solution](runtime.md#rt-obj-query-solution), which is per-call delivery rather than the retained passage corpus. SRC-1 implementation: `src/hipporag/HippoRAG.py`.

> chunk_texts = [chunk.content for chunk in processed_chunks]
> --- `src/hipporag/HippoRAG.py`

> docs = [self.chunk_embedding_store.get_row(key)["content"] for key in passage_keys]
> --- `src/hipporag/HippoRAG.py`

#### EPI-OBJ-openie-triples
Label: OpenIE relation triples

Part of: [RT-RTE-index-state](runtime.md#rt-rte-index-state)

Source-native identity: `extracted_triples` in saved OpenIE rows and `TripleRawOutput.triples`. Natural-language subject/predicate/object strings assert relations, while list structure and keys are symbolic parser inputs. Retained substrate is OpenIE state; process results also carry response/error metadata. Named entities are the preceding model-generated lexical candidates, not independent relation evidence. Their consumer is triple extraction; triples feed normalization and graph construction. This content part differs from [EPI-OBJ-normalized-facts](#epi-obj-normalized-facts), which has undergone punctuation/case conversion. SRC-1 implementation: `src/hipporag/information_extraction/openie_openai.py`; retention context see parent.

> extracted_triples = _extract_triples_from_response(real_response)
> triplets = filter_invalid_triples(triples=extracted_triples)
> --- `src/hipporag/information_extraction/openie_openai.py`

#### EPI-OBJ-normalized-facts
Label: Normalized facts

Part of: [RT-RTE-index-state](runtime.md#rt-rte-index-state)

Source-native identity: `chunk_triples`, `facts`, `fact_embedding_store`. Natural-language normalized relation strings are encoded into distributed numerical embeddings; symbolic tuples, hashes and graph edges direct indexing/ranking. Substrates are fact/entity stores, saved graph, OpenIE source rows and process reverse mappings. Graph edges are retrieval links with source counts or synonym scores, not independently warranted relation assertions. Deletion removes source contributions and drops unreferenced facts/entities; shared material survives. This content part is not the full parent route. SRC-1 implementation: `src/hipporag/HippoRAG.py`, `src/hipporag/utils/misc_utils.py`.

> self.fact_embedding_store.insert_strings([str(fact) for fact in facts])
> --- `src/hipporag/HippoRAG.py`

> if remove_sources_from_mapping(self.proc_triples_to_docs, str(processed_triple), chunk_ids_to_delete):
>     unreferenced_processed_triples.append(processed_triple)
> --- `src/hipporag/HippoRAG.py`

#### EPI-OBJ-answer-thoughts
Label: Answer and thought contents

Part of: [RT-OBJ-query-solution](runtime.md#rt-obj-query-solution)

Source-native identity: `answer` and `thoughts` content fields. Natural-language candidate conclusions differ from symbolic scores and metadata in the parent container. Substrate: process values and return payloads; no durable answer-as-document admission in these methods, though model response caching is a separate supplied route. Answers may assert propositions about the question domain; thoughts may assert intermediate propositions or serve as search queries. Runtime model behavior remains unobserved. A delimiter parser does not verify grounding; its fallback can return the whole response. SRC-1 implementation: `src/hipporag/HippoRAG.py`.

> pred_ans = response_content.split('Answer:')[1].strip()
> --- `src/hipporag/HippoRAG.py`

> pred_ans = response_content
> --- `src/hipporag/HippoRAG.py:1172-1172`

### Routes

#### EPI-RTE-openie-generation
Label: OpenIE candidate generation

Part of: [RT-RTE-index-state](runtime.md#rt-rte-index-state)

Caller/code supplies passage; extraction model proposes named entities then relations; code owns progression. Endpoint is passage → NER → triple prompt with passage and entities → candidate relation lists. Online calls are separate; static guidance asks for RDF triples and pronoun resolution. No reference-answer oracle or human per-relation judgment is present in this implementation. Trigger is missing extraction state or authorized regeneration, in both open ingestion and benchmark use. Guidance persists as shipped templates; generated structures persist via parent route, not as revised methods. Exact generation quality and weights are not determined. SRC-1 implementation: `src/hipporag/information_extraction/openie_openai.py`; doctrine/design: `src/hipporag/prompts/templates/triple_extraction.py`.

- Immediate return: NER/triple output dictionaries and metadata, or online batch error.
- Later read-back: generated OpenIE rows are saved and reopened by parent indexing/retrieval routes.
- Delegated visibility: each passage reaches NER; passage and named entity list reach triple model.
- Selection predicate: missing chunk keys select generation; model proposes contents.
- Invalidation or expiry: parent force/provenance policy governs regeneration; not a truth-based expiry.
- Activation or effect: candidate structures are wired into downstream stores/graph, not evidence of compliance or benefit.
- Evidence limits: no paired execution output, entailment test or independent semantic evaluator; offline differences see [RT-RTE-offline-extraction](runtime.md#rt-rte-offline-extraction).
- implementation conclusion status: wired
- operation conclusion status: uninspected

> re_futures = {
>     executor.submit(self.triple_extraction, ner_result.chunk_id,
>                     chunk_passages[ner_result.chunk_id],
>                     ner_result.unique_entities): ner_result.chunk_id
>     for ner_result in ner_results_list
> }
> --- `src/hipporag/information_extraction/openie_openai.py`

Prompt authority and minimum instruction passage are see [RT-BAP-extraction-prompt](runtime.md#rt-bap-extraction-prompt).

#### EPI-RTE-triple-check
Label: Triple structural checking

Part of: [RT-RTE-index-state](runtime.md#rt-rte-index-state)

Target/domain: online extraction's JSON list field and triple length/duplicate identity, not asserted relation truth. Model proposes; deterministic JSON/parser and `filter_invalid_triples` evaluate; software can veto malformed output. Human input is caller-supplied content, not evidenced per-item approval. Checks run immediately after generation. Result licenses structural processing only; it does not license factual reliance. SRC-1 implementation: `src/hipporag/information_extraction/openie_openai.py`, `src/hipporag/utils/llm_utils.py`.

- Immediate return: parsed list and structural-validity outcomes consumed by linked admission.
- Later read-back: inapplicable — this check itself retains no decision record for later semantic reliance.
- Delegated visibility: inapplicable — parser and validator are deterministic local code.
- Selection predicate: JSON named field must be a list; retained items must have three elements and unique string tuples.
- Invalidation or expiry: inapplicable — per-result check, not a standing endorsement.
- Activation or effect: outcomes are wired to rejection, string conversion and duplicate removal in [EPI-RTE-triple-admission](#epi-rte-triple-admission).
- Evidence limits: syntactic domain only; no source entailment comparison or expected-answer oracle.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if not isinstance(value, list):
>     raise ValueError(f"OpenIE response field {field_name!r} must be a list.")
> return value
> --- `src/hipporag/information_extraction/openie_openai.py`

> if len(triple) != 3: continue  # Skip triples that do not have exactly 3 elements
> --- `src/hipporag/utils/llm_utils.py`

#### EPI-RTE-triple-admission
Label: Triple structural disposition

Part of: [RT-RTE-index-state](runtime.md#rt-rte-index-state)

Endpoint: structural results → cleaned list or error metadata → online batch continuation or exception. Code decides; the caller can retry or rebuild but does not approve each relation. The criterion is parsability/shape/error-free completion for indexing, not evidence-consuming semantic acceptance. Rejection occurs before downstream derivation but after parent passage writes; it is not atomic rollback. Open and benchmark ingestion share this admission mechanism. Guidance is static extraction instruction; admitted triple lists persist via OpenIE/derived stores. SRC-1 implementation: `src/hipporag/utils/llm_utils.py`, `src/hipporag/information_extraction/openie_openai.py`; parent provides recovery limits.

- Immediate return: unique string triples, or raised online batch failure.
- Later read-back: surviving lists feed retained OpenIE and later graph reconstruction.
- Delegated visibility: inapplicable — this disposition is code, not another model judgment.
- Selection predicate: valid shape and tuple uniqueness; any online stage error metadata vetoes its batch.
- Invalidation or expiry: explicit re-extraction/rebuild or deletion, not criticism-triggered correction.
- Activation or effect: cleaned triples are eligible for persistent indexing without a truth verdict; failure blocks later batch progression.
- Evidence limits: offline parse failures do not uniformly share online fail-fast behavior; successful structure permits false triples too.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> valid_triple = [str(item) for item in triple]
> if tuple(valid_triple) not in unique_triples:
>     unique_triples.add(tuple(valid_triple))
>     valid_triples.append(valid_triple)
> --- `src/hipporag/utils/llm_utils.py`

Online error veto passage is see [RT-RTE-index-state](runtime.md#rt-rte-index-state). A concrete implementation deduction: input `[["A","is","B"],["A","is","B"],["A","B"]]` leaves one three-string triple. This establishes shape/deduplication, not whether A is B. No target execution was needed.

#### EPI-RTE-text-normalization
Label: Fact text normalization

Part of: [RT-RTE-index-state](runtime.md#rt-rte-index-state)

Endpoint: parsed triple strings → casefold/punctuation/whitespace normalization → deduplicated fact tuples → entity/fact stores and graph construction. Code owns transformation, with no semantic evaluator or oracle. Operational authority is persistent searchable identity: collapsed labels can share fact/entity identity and influence later selection. Source warrant through this edge is not established as preserved. No per-normalization human approval or rejection is wired. Recovery is parent deletion/rebuild, not automatic semantic disambiguation. SRC-1 implementation: `src/hipporag/utils/misc_utils.py`, `src/hipporag/HippoRAG.py`.

- Immediate return: normalized strings and unique tuples.
- Later read-back: normalized fact/entity strings and graph nodes reach future retrieval/filter calls.
- Delegated visibility: embedding model later receives normalized strings; normalization itself is local code.
- Selection predicate: every admitted triple is normalized, then tuples deduplicated by equality.
- Invalidation or expiry: parent source deletion or rebuild governs retained derivatives.
- Activation or effect: labels are wired to fact/entity identity and retrieval context; actual answer effect unobserved.
- Evidence limits: deterministic collision witness establishes possible referent loss, not an observed false answer or prevalence estimate.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> normalized = ''.join(character if character.isalnum() or character.isspace() else ' ' for character in text.casefold())
> return ' '.join(normalized.split())
> --- `src/hipporag/utils/misc_utils.py`

> chunk_triples = [[text_processing(t) for t in triple_results_dict[chunk_id].triples] for chunk_id in chunk_ids]
> --- `src/hipporag/HippoRAG.py`

Concrete implementation deduction: `["C++","differs from","C#"]` becomes `["c","differs from","c"]`. Casefold yields `c++`/`c#`; punctuation becomes spaces; split/join yields `c` for both. The original distinction is not recoverable from normalized labels alone. Original passage text still reaches QA through [EPI-OBJ-passages](#epi-obj-passages), a counterexample to any claim that all source distinctions are destroyed system-wide. This is an implementation-layer trace, not execution evidence.

#### EPI-RTE-fact-check
Label: Query relevance judgment

Part of: [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer)

Target/domain: relevance of the supplied top embedding-ranked fact candidates to this query, including requested multi-hop utility. `DSPyFilter` extraction model proposes which candidates matter, using question, candidates, system instructions and static demonstrations. No gold references enter this call. Prompt requests at most four relevant facts and no new facts; that is guidance, not evidence that actual outputs comply. Result has ranking use only, no corpus endorsement. SRC-1 implementation: `src/hipporag/rerank.py`; doctrine/design: `src/hipporag/prompts/filter_default_prompt.py`.

- Immediate return: model response parsed into proposed fact lists, or empty on parsing/inference failure.
- Later read-back: inapplicable — the judgment is current-query state; any adapter response cache is a distinct parent-supplied reuse path.
- Delegated visibility: model sees question and candidate fact strings, not full source passages or gold answers.
- Selection predicate: top `linking_top_k` fact similarities determine input; model judges relevance.
- Invalidation or expiry: per-query invocation; bypass when no candidates or nonpositive linking budget.
- Activation or effect: proposed lists feed deterministic selection and can alter graph seed ranking.
- Evidence limits: no independent relevance or factuality evaluator; actual judgment and benefit unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> response = self.llm_infer_fn(
>     messages=messages,
>     **self.default_gen_kwargs
> )
> --- `src/hipporag/rerank.py`

> self.llm_infer_fn = hipporag.extraction_llm.infer
> --- `src/hipporag/rerank.py`

#### EPI-RTE-fact-selection
Label: Filter result selection

Part of: [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer)

Endpoint: parsed model fact proposals → nearest candidate-string remapping → candidate indices/tuples → graph branch or dense fallback. Code decides and can discard on exception; no human veto or answer oracle. Candidate membership is enforced by returning indexed input tuples, but nearest matching has cutoff zero and does not establish exact model intent. Consumer: graph entity seeding through tuple/index channels, ranking force for the current retrieval, then passage delivery to QA/host. No epistemic authority beyond candidate membership and current-query operational use. SRC-1 implementation: `src/hipporag/rerank.py`, `src/hipporag/HippoRAG.py`.

- Immediate return: selected candidate indices/tuples and confidence metadata set to None, or empty selection.
- Later read-back: inapplicable — selection does not update retained facts or establish future endorsement.
- Delegated visibility: inapplicable — local remapping and branching consume the model result.
- Selection predicate: nearest string at cutoff zero, candidate index lookup, length prefix; empty selection chooses dense retrieval.
- Invalidation or expiry: selection lasts for current retrieval only.
- Activation or effect: selected facts seed graph ranking; empty/error selection permits dense fallback, not rejection of the question.
- Evidence limits: syntactic membership does not license relevance, source truth or accurate interpretation of model intent.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> sorted_candidate_indices = [candidate_indices[i] for i in result_indices]
> sorted_candidate_items = [candidate_items[i] for i in result_indices]
> return sorted_candidate_indices[:len_after_rerank], sorted_candidate_items[:len_after_rerank], {'confidence': None}
> --- `src/hipporag/rerank.py`

Nearest-match and fallback passages are see [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer). A one-item candidate list will map any parsed generated fact to that candidate, provided matching completes. Thus novel generated wording need not be faithfully rejected, even though returned facts remain drawn from candidates.

#### EPI-RTE-metric-evaluation
Label: Benchmark reference evaluation

Endpoint: caller gold documents/answer aliases and selected passages/answers → deterministic metrics → log/return values. Distinct from the broader [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer): this route spans normal QA, DPR/StandardRAG and IRCoT evaluation rather than one retrieval branch. The driver supplies references from dataset fields; reference quality is uninspected. Targets/domains: exact document-string coverage at k; normalized answer equality against aliases; normalized token overlap against aliases. Defaults take maximum alias score then mean over examples. Code computes, caller consumes; no model answer oracle or human adjudication is present. No metric threshold vetoes generated output, admits a claim or updates the pipeline in inspected `main.py`/HippoRAG evaluation. Operating mode is optional benchmark reporting, not the open MCP request. SRC-1 implementation: `main.py`, `src/hipporag/HippoRAG.py`, `src/hipporag/evaluation/qa_eval.py`, `src/hipporag/evaluation/retrieval_eval.py`, `src/hipporag/utils/eval_utils.py`.

- Immediate return: aggregate/per-example scores from evaluators; library returns aggregates and attaches gold labels to solutions in evaluated QA.
- Later read-back: inapplicable — inspected driver logs/returns results without a retained score-consuming revision route.
- Delegated visibility: inapplicable — metrics are local code; inference already occurred without gold references in its QA prompt.
- Selection predicate: references supplied by caller enable evaluation; maximum alias agreement is default aggregation.
- Invalidation or expiry: inapplicable — scores describe this result/reference comparison, not a standing content license.
- Activation or effect: advisory reporting through logger/return channel at call horizon; no enforcing acceptance force.
- Evidence limits: normalized agreement does not establish source truth, reasoning mechanism, replay safety, transfer or component effect; no experiment supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> em_scores = [1.0 if normalize_answer(gold) == normalize_answer(predicted) else 0.0 for gold in gold_list]
> aggregated_em = aggregation_fn(em_scores) if em_scores else 0.0
> --- `src/hipporag/evaluation/qa_eval.py`

> common = Counter(predicted_tokens) & Counter(gold_tokens)
> num_same = sum(common.values())
> --- `src/hipporag/evaluation/qa_eval.py`

> relevant_retrieved = set(top_k_docs) & set(example_gold_docs)
> --- `src/hipporag/evaluation/retrieval_eval.py`

> return white_space_fix(remove_articles(remove_punc(lower(answer))))
> --- `src/hipporag/utils/eval_utils.py`

> logger.info(f"Evaluation results for QA: {overall_qa_results}")
> --- `src/hipporag/HippoRAG.py:956-956`

A deterministic contrast bounds exact-match license: gold `C++` and prediction `C#` both normalize to `c`, so this evaluator returns normalized agreement even for distinct programming-language names. This is an implementation deduction, not a claim that a supplied benchmark contains that case. Conversely, genuine aliases absent from references may score poorly. Reference agreement is useful within its declared comparison domain, not a universal factuality test.

#### EPI-RTE-host-check
Label: Host answer checking

Part of: [RT-BAP-plugin-skills](runtime.md#rt-bap-plugin-skills)

This is a material checking subpath of the parent's host-interpreted policy, not the MCP server route. Target/domain: the server answer's support by returned passages. Evaluator: enclosing agent instructed to compare; criterion is described only as checking against passages. Trigger: explicit request for HippoRAG's own answer. Skill proposes; host decides adherence and any disposition. No observed check, pass/fail result, enforced rejection or retained correction is supplied. Consumer is host answering behavior through natural-language guidance, advisory at request horizon. Source passage checks would still not independently authenticate original source truth. SRC-1 doctrine/design: `plugins/hipporag/skills/hipporag-memory/SKILL.md`; implementation contrast: `src/hipporag/mcp_server.py` returns answer/passages directly.

- Immediate return: uninspected — host execution and judgment are outside supplied evidence.
- Later read-back: uninspected — no retained host check result or later consumer supplied.
- Delegated visibility: guidance asks host to use answer and returned passages, not inaccessible full graph state.
- Selection predicate: explicit user request for server-side QA according to the skill.
- Invalidation or expiry: uninspected — host rejection/correction policy beyond this instruction is unspecified.
- Activation or effect: instruction can shape host checking; actual check and changed reliance unobserved.
- Evidence limits: doctrine only; no server-side semantic validation follows from the skill.
- guidance conclusion status: claimed
- operation conclusion status: uninspected

> - **`rag_qa`**: only when the user explicitly wants HippoRAG's own answer, for example when comparing against the paper's QA pipeline. It costs an extra server-side LLM call, and you still need to check its answer against the returned passages.
> --- `plugins/hipporag/skills/hipporag-memory/SKILL.md`

### Claims

#### EPI-CLM-memory-connections
Label: Memory connection recognition

Claimed operation: memory for LLMs recognizes and uses connections in new knowledge. SRC-1 doctrine/design: `README.md`. Closest supplied [RT-RTE-index-state](runtime.md#rt-rte-index-state) describes its implementation, not this public claim; no counterpart claim declared there. Retained graph and fact selection support an operational reading of connections, not established semantic warrant or measured improvement.

> HippoRAG 2 is a memory framework for LLMs that recognizes and uses connections in new knowledge, mirroring a key function of human long-term memory.
> --- `README.md`

#### EPI-CLM-grounded-answer
Label: Passage grounded answer

Claimed operation: MCP QA answers grounded in retrieved passages. SRC-1 doctrine/design in executable tool docstring: `src/hipporag/mcp_server.py`. This is distinct from compatibility [RT-CLM-state-compatibility](runtime.md#rt-clm-state-compatibility). Closest runtime mechanism is [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer), not a separate semantic guarantee. Implementation supplies selected passages and returns them alongside an answer; no proof of entailment or correctness is implemented by that wrapper.

> """Answer a question with the server-side LLM, grounded in passages retrieved by HippoRAG."""
> --- `src/hipporag/mcp_server.py`

#### EPI-CLM-call-guidance
Label: Retrieval extraction call guidance

Claimed operation: retrieval makes no LLM call; each new passage costs one extraction call. SRC-1 doctrine/design: `plugins/hipporag/skills/hipporag-memory/SKILL.md`. Closest supplied [RT-BAP-plugin-skills](runtime.md#rt-bap-plugin-skills) already flags the mismatch; this record individuates the consequential cost/route claim, not another host authority path. Normal model-backed filtering and two-stage online extraction contradict universal call-count readings. Cache hits, empty facts and DPR bypasses prevent replacing the guidance with a single universal observed cost figure.

> - **`retrieve`**: the default for answering questions. It returns ranked passages with `source_id` and metadata and makes no LLM call. Read the passages, answer in your own words, and cite `source_id`s. Use `top_k` 5–10 for most questions and up to ~20 for broad or multi-hop ones.
> --- `plugins/hipporag/skills/hipporag-memory/SKILL.md`

> - Every **new** passage costs one LLM extraction call on the user's API key. Passages already in the index are skipped. Before indexing more than ~50 passages, tell the user roughly how many there are and get confirmation.
> --- `plugins/hipporag/skills/hipporag-memory/SKILL.md`
