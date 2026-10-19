---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Siftly epistemic routes: imported bookmarks, generated annotations, validation, reliance and withdrawal at the frozen revision."
run-id: AAS-2026-10-18-siftly-b81c94cf0f77-01
reviewed-boundary: b25daa45b858f4be096b5c368671c34db4407d8e
---

# Siftly epistemic report

## Source-and-claim boundary

The question is how Siftly's bookmark collection acquires truth-apt content, generates annotations, checks candidates and licenses later reliance. Scope, exclusions and source identity are see [boundary](boundary.md#boundary-and-evidence); evidence layers are see its [Source register](boundary.md#source-register). All source-dependent findings below use SRC-1, implementation unless explicitly marked doctrine/design. No target execution was performed or supplied.

The material distinction is between admitting usable metadata and accepting its truth. Siftly's structural checks can reject malformed or out-of-domain output. They do not independently check whether a depicted person, transcribed sentence, topic assignment or relevance explanation is correct. Imported statements remain acquired source content, not propositions established by Siftly. Source attribution is retained through bookmark identities/raw JSON, but source warrant is unknown; recording a tweet does not verify what it says. See [RT-RTE-import-content](runtime.md#rt-rte-import-content).

Consequential claims are [RT-CLM-bookmark-work](runtime.md#rt-clm-bookmark-work), [RT-CLM-category-policy](runtime.md#rt-clm-category-policy) and [EPI-CLM-tags-reliability](#epi-clm-tags-reliability). The last two explicitly license reliance on earlier AI output. The search/retrieval architecture can be assessed without asserting that these reliability claims are true.

| Entry point or operation | Source path | Coverage and records | Basis or remaining limit |
|---|---|---|---|
| File import and browser pipeline trigger | `app/api/import/route.ts`, `app/import/page.tsx` | [RT-RTE-import-content](runtime.md#rt-rte-import-content) | Supplied runtime; endpoint persistence is distinct from browser-triggered processing. |
| Bookmarklet, Twitter, live/sync, OAuth ingestion | `app/api/import/bookmarklet/route.ts`, `app/api/import/twitter/route.ts`, `lib/x-sync.ts`, `app/api/import/x-oauth/fetch/route.ts` | [RT-RTE-import-content](runtime.md#rt-rte-import-content) | Supplied runtime/boundary; OAuth normalization not independently inspected here. This prevents a system-complete assertion about import fidelity. |
| Main pipeline, force, stop, write and read-back | `app/api/categorize/route.ts`, `lib/categorizer.ts` | [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize), [EPI-RTE-semantic-tags](#epi-rte-semantic-tags) | Direct reads of parser/writer, prompts, pipeline enrichment and endpoint selector; supplied runtime for stop branches. |
| Raw JSON entity backfill | `lib/rawjson-extractor.ts` | [EPI-RTE-entity-extraction](#epi-rte-entity-extraction) | Direct read of extraction/backfill; tool-domain lookup internals not independently assessed. |
| Vision and independent image endpoint | `lib/vision-analyzer.ts`, `app/api/analyze/images/route.ts` | [EPI-RTE-image-analysis](#epi-rte-image-analysis) | Direct read of analysis, cache, failure disposition and independent endpoint; helper batch scheduling partly supplied by runtime. |
| Image-context reduction | `lib/image-context.ts` | [EPI-RTE-image-context](#epi-rte-image-context) | Complete direct read; concrete deduction below. |
| Category generation, creation, manual replacement and deletion | `lib/category-suggester.ts`, `app/api/categories/suggest/route.ts`, `app/api/bookmarks/[id]/categories/route.ts`, `app/api/categories/[slug]/route.ts` | [RT-RTE-category-admission](runtime.md#rt-rte-category-admission), [EPI-RTE-content-withdrawal](#epi-rte-content-withdrawal) | Supplied runtime for suggestion/manual admission; direct read of deletion. |
| Direct caller-authored categories and empty-store default seeding | `app/api/categories/route.ts` | [EPI-OBJ-category-description](#epi-obj-category-description) | Direct read confirms additional writer and GET seeding. Not fully assessed as a separate authority route; category-admission inventory remains partial. No inference that custom descriptions must originate in model suggestions or that only pipeline start seeds defaults. |
| AI search and FTS | `app/api/search/ai/route.ts`, `lib/fts.ts` | [RT-RTE-search-content](runtime.md#rt-rte-search-content), [EPI-CLM-tags-reliability](#epi-clm-tags-reliability) | Direct read of reranking prompt/parser/hydration/cache write and complete FTS; supplied runtime for candidate selectors. |
| CLI dispatch, show and non-model search; exports | `cli/siftly.ts`, `lib/obsidian-exporter.ts` | [RT-RTE-cli-export](runtime.md#rt-rte-cli-export) | Direct CLI dispatch inspection confirms only search/list/show/categories/stats. Supplied runtime for command bodies; direct reads of emitted-field builders in `lib/exporter.ts` and `lib/obsidian-exporter.ts` establish omission of imageTags, not full export fidelity. |
| Browse, graph, count and clearing operations | `app/api/bookmarks/route.ts`, `app/api/mindmap/route.ts`, `app/api/stats/route.ts` | [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark), [EPI-RTE-content-withdrawal](#epi-rte-content-withdrawal) | Direct browse/clear read; graph/count roles supplied by boundary, not full direct inspection. No graph-wide semantic guarantee follows. |
| Provider/CLI settings and dispatch | `lib/ai-client.ts`, `lib/claude-cli.ts`, `lib/codex-cli.ts`, `app/api/settings/route.ts` | [RT-RTE-model-dispatch](runtime.md#rt-rte-model-dispatch), [RT-RTE-settings-change](runtime.md#rt-rte-settings-change) | Supplied runtime; no Siftly registered-tool loop identified there. External executables' tools/hooks remain outside frozen source. |
| Media, preview, auth and setup | `app/api/media/route.ts`, `app/api/link-preview/route.ts`, `middleware.ts`, `start.sh` | See [boundary](boundary.md#boundary-and-evidence) and [RT-RTE-model-dispatch](runtime.md#rt-rte-model-dispatch) | Transport/admission support retained in scope; no independent claim of an epistemic evaluator for these operations. |

Missing provider responses prevent classifying actual generated edges as faithful transcription, entailed description or novel non-entailed assertion. Missing image ground truth, human judgments and retrieval benchmarks prevent assessing transcription/entity/category/relevance accuracy. Missing execution traces prevent concluding that a route operated, influenced a model, or benefited an agent. Missing provider internals prevent assessing weight updates or internal model criticism. Available operations not directly inspected here are identified above; the report makes no system-complete negative about every possible evaluator or ontology transformation.

## Epistemic-object inventory

Objects split where form, producer or reliance differs. Container identity is see [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark); its parts below do not supersede it.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark) | See record; imported text can assert external facts | See record | SRC-1, `prisma/schema.prisma` | Collection-level container; acquired source assertions are not verified facts. |
| [EPI-OBJ-entities](#epi-obj-entities) | See record | See record | SRC-1, `lib/rawjson-extractor.ts` | Extracted fields and heuristic labels have different warrant. |
| [EPI-OBJ-image-tags](#epi-obj-image-tags) | See record | See record | SRC-1, `lib/vision-analyzer.ts` | No inspected response or ground truth; `{}` is a control marker, not an image proposition. |
| [EPI-OBJ-semantic-tags](#epi-obj-semantic-tags) | See record | See record | SRC-1, `lib/vision-analyzer.ts` | Search terms may be non-propositional; sentiment/person/company associations can be true or false over a bookmark. |
| [EPI-OBJ-bookmark-category](#epi-obj-bookmark-category) | See record | See record | SRC-1, `lib/categorizer.ts` | Topic membership is assessable relative to category meaning; confidence is not calibrated probability. |
| [EPI-OBJ-category-description](#epi-obj-category-description) | See record | See record | SRC-1, `lib/categorizer.ts` | Category guidance is principally policy, not an explanation validated against evidence. |
| [EPI-OBJ-search-matches](#epi-obj-search-matches) | See record | See record | SRC-1, `app/api/search/ai/route.ts` | Relevance reasons may assert bookmark facts; ranking preference alone is not a factual proposition. |

## Authority-route ledger

Ledger fields owned by a shared record use `see`. Each compact row separates a consequential function even when one source routine implements several. Architectural status concerns source wiring, not observed activation. No ledger row claims observed operation.

Route ID: [RT-RTE-import-content](runtime.md#rt-rte-import-content)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark)
Content/update relation: truth-apt transformation: acquisition/import; source warrant unknown.
Transition or check target: See route.
Evaluator/condition and domain: See route; parsing/duplicate checks license shape and identity handling, not truth of tweet statements.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Attribution to imported source only; no fact endorsement established.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `app/api/import/route.ts`; see route.
Claim IDs or none: [RT-CLM-bookmark-work](runtime.md#rt-clm-bookmark-work)
Mismatch marker or none: none
Gap/limit: Import normalization is not a truth check; operation unobserved.

Route ID: [RT-RTE-import-content](runtime.md#rt-rte-import-content)
Route function: retention
Architectural status: implemented
Object/candidate ID: [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark)
Content/update relation: no content change
Transition or check target: See route's write/read-back fields.
Evaluator/condition and domain: See route; storage admission only.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Retention does not add source warrant.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `app/api/import/route.ts`; see route.
Claim IDs or none: [RT-CLM-bookmark-work](runtime.md#rt-clm-bookmark-work)
Mismatch marker or none: none
Gap/limit: No evidence-consuming factual acceptance decision identified in this route.

Route ID: [EPI-RTE-entity-extraction](#epi-rte-entity-extraction)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-entities](#epi-obj-entities)
Content/update relation: truth-apt transformation: non-ampliative reshaping for copied/lowercased fields; truth-apt transformation: entailed derivation only for code-defined structural predicates such as hasMedia, conditional on correctly encoded input. Tool-name semantic inference remains indeterminate without assessment of lookup conventions.
Transition or check target: See route.
Evaluator/condition and domain: See route; deterministic extraction is not independent evidence of external reality.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Preserves selected source values, not their truth; structural results licensed only in the JSON/code domain.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `lib/rawjson-extractor.ts`; see route.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Default original/false values also arise from missing or invalid input; they do not warrant claims about an actual tweet.

Route ID: [EPI-RTE-image-analysis](#epi-rte-image-analysis)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-image-tags](#epi-obj-image-tags)
Content/update relation: truth-apt transformation: indeterminate; requested OCR may reshape text, descriptions may be entailed by image evidence, and inferred mood/person/template tags may be ampliative. Actual response and image interpretation are needed to classify an edge.
Transition or check target: See route.
Evaluator/condition and domain: See route; model proposes annotation, not an independent factual evaluator.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Candidate image assertions only, with video assertions scoped to thumbnail rather than whole video.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `lib/vision-analyzer.ts`; see route.
Claim IDs or none: [RT-CLM-bookmark-work](runtime.md#rt-clm-bookmark-work)
Mismatch marker or none: none
Gap/limit: CLI receives a URL, not the SDK image bytes; actual image access is not established.

Route ID: [EPI-RTE-image-analysis](#epi-rte-image-analysis)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-image-tags](#epi-obj-image-tags)
Content/update relation: no content change
Transition or check target: See route's parseability target.
Evaluator/condition and domain: See route; JSON parser licenses syntax only, not OCR accuracy or object identity.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Parseable JSON only; no independent license for its assertions.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `lib/vision-analyzer.ts`; see route.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Object field schema and semantic correctness are not established by JSON.parse.

Route ID: [EPI-RTE-image-analysis](#epi-rte-image-analysis)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-image-tags](#epi-obj-image-tags)
Content/update relation: no content change
Transition or check target: See route's success/failure/cache disposition.
Evaluator/condition and domain: See route; automatic software admission, not evidence-consuming factual acceptance.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: No added factual warrant; cached result inherits unknown original warrant.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `lib/vision-analyzer.ts`; see route.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: A failure marker suppresses ordinary retry and can be copied; this is operational attempted-state, not accepted knowledge.

Route ID: [EPI-RTE-image-analysis](#epi-rte-image-analysis)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-image-tags](#epi-obj-image-tags)
Content/update relation: no content change
Transition or check target: See route's MediaItem write.
Evaluator/condition and domain: See route.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Candidate retention, not lifecycle integration after factual acceptance.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `lib/vision-analyzer.ts`; see route.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: No model-version or correctness-based invalidation established here.

Route ID: [EPI-RTE-image-context](#epi-rte-image-context)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-image-tags](#epi-obj-image-tags)
Content/update relation: truth-apt transformation: non-ampliative reshaping in the traced well-formed input domain.
Transition or check target: See route.
Evaluator/condition and domain: See route; deterministic selection/truncation, not evaluation of truth.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: No added warrant; omissions narrow information available to subsequent judgments.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `lib/image-context.ts`; see route.
Claim IDs or none: [RT-CLM-category-policy](runtime.md#rt-clm-category-policy)
Mismatch marker or none: none
Gap/limit: Formatting does not preserve every original field or full OCR text.

Route ID: [EPI-RTE-semantic-tags](#epi-rte-semantic-tags)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-semantic-tags](#epi-obj-semantic-tags)
Content/update relation: truth-apt transformation: indeterminate for factual associations; remaining alternatives are reshaping, entailed extraction and ampliative inference. Pure search keywords can instead be non-truth-apt content. Responses and their input evidence are needed to decide.
Transition or check target: See route.
Evaluator/condition and domain: See route; model generation.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Candidate associations, not warranted facts about people, companies or sentiment.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route and [RT-BAP-enrichment-search](runtime.md#rt-bap-enrichment-search).
Evidence source ID and local anchor: SRC-1, `lib/vision-analyzer.ts`; see route.
Claim IDs or none: [EPI-CLM-tags-reliability](#epi-clm-tags-reliability)
Mismatch marker or none: Claimed reliability exceeds demonstrated evidence.
Gap/limit: Prior image annotations enter generation without independent corroboration.

Route ID: [EPI-RTE-semantic-tags](#epi-rte-semantic-tags)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-semantic-tags](#epi-obj-semantic-tags)
Content/update relation: no content change
Transition or check target: See route's shape normalization.
Evaluator/condition and domain: See route; checks array/field form, not semantic accuracy or calibrated sentiment.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Normalized strings and nonempty tags only.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `lib/vision-analyzer.ts`; see route.
Claim IDs or none: [EPI-CLM-tags-reliability](#epi-clm-tags-reliability)
Mismatch marker or none: Shape checks do not establish high reliability.
Gap/limit: Requested tag counts, sentiment vocabulary and entity grounding are not independently enforced in the inspected parser.

Route ID: [EPI-RTE-semantic-tags](#epi-rte-semantic-tags)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-semantic-tags](#epi-obj-semantic-tags)
Content/update relation: no content change
Transition or check target: See route's caller result selection/write condition.
Evaluator/condition and domain: See route; code admits first returned nonempty result in ordinary per-bookmark pipeline. This is a narrower identity check than the separate bulk helper's resultMap lookup.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Computational admission for search use, not criterion-based acceptance of truth.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `app/api/categorize/route.ts`; see route.
Claim IDs or none: [EPI-CLM-tags-reliability](#epi-clm-tags-reliability)
Mismatch marker or none: none
Gap/limit: Parser's nonempty returned ID does not prove correspondence to the requested bookmark in this caller.

Route ID: [EPI-RTE-semantic-tags](#epi-rte-semantic-tags)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-semantic-tags](#epi-obj-semantic-tags)
Content/update relation: no content change
Transition or check target: See route's SQLite write.
Evaluator/condition and domain: See route.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Retained candidate metadata, not lifecycle integration after factual acceptance.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route and [RT-BAP-enrichment-search](runtime.md#rt-bap-enrichment-search).
Evidence source ID and local anchor: SRC-1, `app/api/categorize/route.ts`; see route.
Claim IDs or none: [EPI-CLM-tags-reliability](#epi-clm-tags-reliability)
Mismatch marker or none: none
Gap/limit: Existing tags can outlive the model or category configuration that generated them.

Route ID: [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-bookmark-category](#epi-obj-bookmark-category)
Content/update relation: truth-apt transformation: indeterminate; category membership is model judgment under descriptions, not a proven entailment. Actual assignments could be entailed or ampliative relative to the full input.
Transition or check target: See route.
Evaluator/condition and domain: See route; category model with supplied guidance, no answer oracle.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Candidate category membership only.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See [RT-BAP-category-guidance](runtime.md#rt-bap-category-guidance) and [RT-BAP-enrichment-search](runtime.md#rt-bap-enrichment-search).
Evidence source ID and local anchor: SRC-1, `lib/categorizer.ts`; see route.
Claim IDs or none: [RT-CLM-category-policy](runtime.md#rt-clm-category-policy)
Mismatch marker or none: Reliance on earlier metadata is requested, not validated.
Gap/limit: Heavy trust can propagate upstream annotation errors; no observed error rate or propagation supplied.

Route ID: [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-bookmark-category](#epi-obj-bookmark-category)
Content/update relation: no content change
Transition or check target: See route's slug/confidence/ID checks.
Evaluator/condition and domain: See route; executable check against registered categories and existing bookmark IDs.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Domain membership and confidence range, not topical correctness or probability calibration.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `lib/categorizer.ts`; see route.
Claim IDs or none: [RT-CLM-bookmark-work](runtime.md#rt-clm-bookmark-work)
Mismatch marker or none: Requested 1–3 count and current-batch identity are not enforced.
Gap/limit: An existing but out-of-batch tweet ID can reach writer lookup; source-reachable countercase, not an observed model response.

Route ID: [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-bookmark-category](#epi-obj-bookmark-category)
Content/update relation: no content change
Transition or check target: See route's nonempty assignment and database lookup gates.
Evaluator/condition and domain: See route; automatic writer admission, not factual acceptance.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Usable category link, no independent warrant for its meaning.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `lib/categorizer.ts`; see route.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: No assignments means no category write; an attempted pipeline item is not necessarily enriched.

Route ID: [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-bookmark-category](#epi-obj-bookmark-category)
Content/update relation: no content change
Transition or check target: See route's transactional upsert/enrichedAt write.
Evaluator/condition and domain: See route.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Persistent assignment, not lifecycle integration of an accepted factual claim.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route and [RT-BAP-enrichment-search](runtime.md#rt-bap-enrichment-search).
Evidence source ID and local anchor: SRC-1, `lib/categorizer.ts`; see route.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Upsert does not delete prior assignments omitted by a later model response.

Route ID: [RT-RTE-category-admission](runtime.md#rt-rte-category-admission)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-category-description](#epi-obj-category-description)
Content/update relation: non-truth-apt policy/content update: model proposes category vocabulary and guidance. Any descriptive claims about sample clustering remain unvalidated candidates.
Transition or check target: See route.
Evaluator/condition and domain: See route; sample-driven model proposal.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Organizational proposal, not evidence of a true explanatory theory of the collection.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See [RT-BAP-category-guidance](runtime.md#rt-bap-category-guidance).
Evidence source ID and local anchor: SRC-1, `lib/category-suggester.ts`; see route.
Claim IDs or none: [RT-CLM-bookmark-work](runtime.md#rt-clm-bookmark-work)
Mismatch marker or none: none
Gap/limit: Sample representativeness and category utility unobserved.

Route ID: [RT-RTE-category-admission](runtime.md#rt-rte-category-admission)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-category-description](#epi-obj-category-description)
Content/update relation: no content change
Transition or check target: See route's slug/name/length/example checks.
Evaluator/condition and domain: See route; programmatic validity/identity checks only.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Structurally admissible category, not validated topic coverage.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `lib/category-suggester.ts`; see route.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Model confidence and sample matches do not supply an expected-answer oracle.

Route ID: [RT-RTE-category-admission](runtime.md#rt-rte-category-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-category-description](#epi-obj-category-description), [EPI-OBJ-bookmark-category](#epi-obj-bookmark-category)
Content/update relation: non-truth-apt policy/content update: category vocabulary admission; no added warrant for category memberships.
Transition or check target: See route, with suggestion creation and manual membership replacement as separate mechanisms there.
Evaluator/condition and domain: See route; UI offers human veto, API caller selection does not prove human review. Manual confidence 1.0 denotes assigned value, not epistemic certainty.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Caller-authorized organization, not named evidence-consuming factual acceptance.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See [RT-BAP-category-guidance](runtime.md#rt-bap-category-guidance).
Evidence source ID and local anchor: SRC-1, `app/api/categories/suggest/route.ts`, `app/api/bookmarks/[id]/categories/route.ts`; see route.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Organization may change without any assessment of improved search outcomes.

Route ID: [RT-RTE-category-admission](runtime.md#rt-rte-category-admission)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-category-description](#epi-obj-category-description), [EPI-OBJ-bookmark-category](#epi-obj-bookmark-category)
Content/update relation: no content change
Transition or check target: See route's persisted descriptions and manual memberships.
Evaluator/condition and domain: See route.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Retains organization, not integration after acceptance of a truth claim.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See [RT-BAP-category-guidance](runtime.md#rt-bap-category-guidance).
Evidence source ID and local anchor: SRC-1, `lib/category-suggester.ts`; see route.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Default reseeding and category deletion bound persistence; no version history established.

Route ID: [RT-RTE-search-content](runtime.md#rt-rte-search-content)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark)
Content/update relation: truth-apt transformation: non-ampliative reshaping for indexing and candidate context construction.
Transition or check target: See route's keyword/category/recent selectors and prompt construction.
Evaluator/condition and domain: See route; selection rules, not a truth evaluator.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Retrieval eligibility does not endorse content.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See [RT-BAP-enrichment-search](runtime.md#rt-bap-enrichment-search).
Evidence source ID and local anchor: SRC-1, `lib/fts.ts`, `app/api/search/ai/route.ts`; see route.
Claim IDs or none: [EPI-CLM-tags-reliability](#epi-clm-tags-reliability)
Mismatch marker or none: none
Gap/limit: Candidate omissions and truncation bound what reranking can assess; stale nonempty indexes need not trigger fallback.

Route ID: [RT-RTE-search-content](runtime.md#rt-rte-search-content)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-search-matches](#epi-obj-search-matches)
Content/update relation: truth-apt transformation: indeterminate for factual reasons/explanations; ranking itself is a non-truth-apt preference update. Actual output is needed to distinguish reshaping, entailed description or ampliative assertion.
Transition or check target: See route; target is candidate relevance to current query, not truth of the tweet or its underlying explanation.
Evaluator/condition and domain: See route; model relevance judgment over bounded candidate context, no reference-answer oracle.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Proposed relevance, with reasons remaining candidate assertions.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `app/api/search/ai/route.ts`; see route.
Claim IDs or none: [EPI-CLM-tags-reliability](#epi-clm-tags-reliability)
Mismatch marker or none: No independent corroboration of highly reliable tags.
Gap/limit: Relevance success would not establish truth of imported or generated content.

Route ID: [RT-RTE-search-content](runtime.md#rt-rte-search-content)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-search-matches](#epi-obj-search-matches)
Content/update relation: no content change
Transition or check target: See route's hydration and sort.
Evaluator/condition and domain: See route; candidate-ID map restricts returned objects, but does not check relevance reasons or enforce all prompt constraints.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Candidate identity established at hydration, not correctness of score/reason or factual acceptance.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `app/api/search/ai/route.ts`; see route.
Claim IDs or none: none
Mismatch marker or none: Minimum score, result count and uniqueness are instructions rather than enforced invariants.
Gap/limit: Duplicate candidate matches can survive even though matchMap exists.

Route ID: [RT-RTE-search-content](runtime.md#rt-rte-search-content)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-search-matches](#epi-obj-search-matches)
Content/update relation: no content change
Transition or check target: See route's result cache.
Evaluator/condition and domain: See route; TTL, not endorsement or evidence freshness.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Reuses earlier candidate response without adding warrant.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `app/api/search/ai/route.ts`; see route.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Cache key lacks collection/model revision; withdrawal need not remove a cached response immediately.

Route ID: [RT-RTE-cli-export](runtime.md#rt-rte-cli-export)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark)
Content/update relation: truth-apt transformation: non-ampliative reshaping for JSON/Markdown delivery, within inspected/supplied formatting scope.
Transition or check target: See route.
Evaluator/condition and domain: See route; caller filters and formatting code, not truth evaluation.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Exposes retained content with unknown source/generated warrant, not a guarantee to downstream agents.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `cli/siftly.ts`, `lib/obsidian-exporter.ts`; see route.
Claim IDs or none: [RT-CLM-bookmark-work](runtime.md#rt-clm-bookmark-work)
Mismatch marker or none: none
Gap/limit: Export retention has skip/overwrite semantics, not automatic synchronization or retraction in an external vault.

Route ID: [EPI-RTE-content-withdrawal](#epi-rte-content-withdrawal)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark)
Content/update relation: no content change
Transition or check target: See route's clear/category-delete operations.
Evaluator/condition and domain: See route; caller-directed deletion, not evidence-based refutation.
Activation and timing: See route.
Possible or observed result: See route.
Implemented force: See route.
Epistemic authority and scope: Removes selected operative records without establishing their falsity.
Operational authority: behavior permitted, blocked, or changed: See route.
Behavioral-authority path: consumer, channel, force, horizon: See route.
Evidence source ID and local anchor: SRC-1, `app/api/bookmarks/route.ts`, `app/api/categories/[slug]/route.ts`; see route.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: No full withdrawal guarantee for prior caches, exports or in-flight work.

Route ID: [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize), [RT-RTE-search-content](runtime.md#rt-rte-search-content)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark)
Content/update relation: no content change
Transition or check target: See routes' force, failure-marker, stop, FTS and TTL fields.
Evaluator/condition and domain: See routes; procedural state predicates, not accuracy evaluations.
Activation and timing: See routes.
Possible or observed result: See routes.
Implemented force: See routes.
Epistemic authority and scope: No renewed endorsement follows from retry, enrichedAt or a rebuilt index.
Operational authority: behavior permitted, blocked, or changed: See routes.
Behavioral-authority path: consumer, channel, force, horizon: See routes.
Evidence source ID and local anchor: SRC-1, `app/api/categorize/route.ts`, `lib/fts.ts`, `app/api/search/ai/route.ts`; see routes.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Force resets only failure/empty markers; cooperative stop can leave writes and skip FTS rebuild. These are not transactional rollback or universal recomputation.

Route ID: [RT-RTE-settings-change](runtime.md#rt-rte-settings-change), [RT-RTE-model-dispatch](runtime.md#rt-rte-model-dispatch)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: See routes' Setting values and model components.
Content/update relation: non-truth-apt policy/content update: caller changes provider/model configuration.
Transition or check target: See routes.
Evaluator/condition and domain: See routes; identifier allowlists and availability, not evidence of improvement.
Activation and timing: See routes.
Possible or observed result: See routes.
Implemented force: See routes.
Epistemic authority and scope: No warrant transferred from configuration choice to generated assertions.
Operational authority: behavior permitted, blocked, or changed: See routes.
Behavioral-authority path: consumer, channel, force, horizon: See routes.
Evidence source ID and local anchor: SRC-1, `app/api/settings/route.ts`, `lib/ai-client.ts`; see routes.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: External CLI resolution can differ from selected SDK model; no parametric update or evaluation-responsive improvement established.

No lifecycle-integration row is asserted: in these inspected annotation, category and search routes, retention and operational use occur without an evidenced prior factual acceptance decision. This is a route-local limit, not an inference that every truth-apt edge lacks warrant or that an operational bookmark organizer has failed its purpose.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-bookmark-work](runtime.md#rt-clm-bookmark-work) | See record | SRC-1, `package.json`; doctrine/design | See record | [RT-RTE-import-content](runtime.md#rt-rte-import-content), [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize), [RT-RTE-search-content](runtime.md#rt-rte-search-content), [RT-RTE-cli-export](runtime.md#rt-rte-cli-export) | None supplied | No accuracy or benefit comparison | Bookmark acquisition, annotation and consumption capacity is wired. | Product usefulness and factual reliability unobserved, not disproved. |
| [RT-CLM-category-policy](runtime.md#rt-clm-category-policy) | See record | SRC-1, `lib/categorizer.ts`; doctrine/design | See record | [EPI-RTE-semantic-tags](#epi-rte-semantic-tags), [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize) | None supplied | No independent quality check of precomputed tags; syntactic admission only | A later model is instructed to rely heavily on generated metadata. | Neither compliance nor justified heavy trust established. |
| [EPI-CLM-tags-reliability](#epi-clm-tags-reliability) | See record | SRC-1, `app/api/search/ai/route.ts`; doctrine/design | See record | [EPI-RTE-semantic-tags](#epi-rte-semantic-tags), [RT-RTE-search-content](runtime.md#rt-rte-search-content) | None supplied | No ground truth or causal experiment; model scores are not a benchmark | Reliability is asserted inside a consequential search prompt; metadata delivery is wired. | “Highly reliable” is not established by parseability, persistence, confidence or relevance generation. |

## Bounded conclusion

**Acquisition and reshaping are established capacities.** Imported bookmarks retain source identity/raw content without verifying source assertions. Entity-field normalization, index building, image-context selection and JSON/Markdown output reshape selected content. The deterministic deductions in [EPI-RTE-entity-extraction](#epi-rte-entity-extraction) and [EPI-RTE-image-context](#epi-rte-image-context) establish only code-domain consequences, conditional on input encoding; they do not warrant external facts. Their information losses matter because later models receive the selected representation, not necessarily the whole source.

**Generation and checking have different licenses.** Vision, semantic enrichment, categorization and search can produce truth-apt descriptions or associations, but actual semantic edges remain indeterminate without outputs and their input evidence. JSON parsing, slug filtering, confidence clamping, existing-ID lookup and candidate hydration are implemented checks in their narrow structural domains. They authorize storage/use at those boundaries, not factual acceptance. Search relevance judgments concern a query/candidate relation; even correct relevance would not verify a tweet's claims. See [EPI-RTE-image-analysis](#epi-rte-image-analysis), [EPI-RTE-semantic-tags](#epi-rte-semantic-tags), [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize) and [RT-RTE-search-content](runtime.md#rt-rte-search-content).

**Retained metadata has consequential force before factual acceptance.** Stored image/semantic tags enter future prompts and keyword eligibility; category assignments affect grouping and retrieval; descriptions guide later assignments. Fixed selectors enforce eligibility while natural-language guidance depends on model interpretation. Human selection is afforded for category suggestions and manual edits, but HTTP admission alone does not establish human review or an evidence-consuming truth criterion. The intended use is collection organization/search, not a universal truth oracle. See [RT-BAP-enrichment-search](runtime.md#rt-bap-enrichment-search), [RT-BAP-category-guidance](runtime.md#rt-bap-category-guidance) and [RT-RTE-category-admission](runtime.md#rt-rte-category-admission).

**Recovery and withdrawal are partial, not epistemic revision.** Failure markers can block retries; force selectively clears them. Null semanticTags allows the enrichment stage to run only after endpoint selection: successful categorization can set enrichedAt despite enrichment failure, excluding the row from later ordinary enrichedAt=null selection. Explicit IDs or force can reselect it; the separate bulk helper's semanticTags=null selector does not establish ordinary endpoint retry. See [EPI-RTE-semantic-tags](#epi-rte-semantic-tags). Category upserts do not retract omitted assignments. Manual replacement and deletion provide real countercases to an assertion that assignments are immutable. Clear/category-delete operations remove live DB content, but short-lived result caches, prior exports and in-flight calls limit immediate withdrawal. None records a criticism showing a proposition false. See [EPI-RTE-content-withdrawal](#epi-rte-content-withdrawal), [RT-RTE-category-admission](runtime.md#rt-rte-category-admission) and [RT-RTE-search-content](runtime.md#rt-rte-search-content).

**Parameter and improvement conclusions remain separate.** Provider components are see [RT-CMP-anthropic](runtime.md#rt-cmp-anthropic), [RT-CMP-openai](runtime.md#rt-cmp-openai) and [RT-CMP-minimax](runtime.md#rt-cmp-minimax): exact weights are not pinned, endpoints can resolve differently, and internal mutation is uninspected. Retained guidance can change future application behavior without a weight change. That path does not by itself establish improved capacity, reflection, autonomous theory criticism or self-improvement; no causal improvement evidence was supplied. Category descriptions are individually accessible guidance, not demonstrated content-directed criticism of theories. The route-local lack of factual acceptance does not negate supported acquisition, checking or operational adaptation capacities, nor imply a single system-wide epistemic status.

## Shared records

### Operative objects

#### EPI-OBJ-entities
Label: ExtractedEntities
Part of: [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark)

The Bookmark.entities JSON string in SQLite contains symbolic arrays/labels consumed by fixed selectors and natural-language tokens interpreted by models. Hashtags, URLs and mentions are selected from raw JSON; tools come from URL matching; tweetType/hasMedia/mediaTypes are structural classifications. This part differs from imported text and generated image descriptions in producer and warrant. SRC-1, `lib/rawjson-extractor.ts`; evidence passage is in [EPI-RTE-entity-extraction](#epi-rte-entity-extraction).

#### EPI-OBJ-image-tags
Label: MediaItem.imageTags
Part of: [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark)

SQLite string containing model JSON with natural-language OCR, scenes, people, objects, moods and tags. These associate propositions with an image; JSON syntax is symbolic packaging, not semantic validation. `_type` denotes video-thumbnail scope; `{}` can instead be a non-truth-apt attempted/failure marker. Distinct from entities by media/model provenance and retry consumer. SRC-1, `lib/vision-analyzer.ts`; passages in [EPI-RTE-image-analysis](#epi-rte-image-analysis).

#### EPI-OBJ-semantic-tags
Label: semanticTags and enrichmentMeta
Part of: [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark)

Two SQLite JSON strings written together: semanticTags holds search terms; enrichmentMeta holds sentiment/people/companies. Terms may be indexing choices rather than propositions. Associating a named person/company or sentiment with a bookmark is truth-apt over that content, though sentiment also depends on interpretation. Natural-language values are consumed through model interpretation and keyword selectors. Empty-array markers have separate skip semantics. Distinct from imageTags by producer inputs and consumer fields. SRC-1, `lib/vision-analyzer.ts`, `app/api/categorize/route.ts`; passages in [EPI-RTE-semantic-tags](#epi-rte-semantic-tags).

#### EPI-OBJ-bookmark-category
Label: BookmarkCategory
Part of: [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark)

SQLite relational link with symbolic bookmark/category IDs and numeric confidence; category meaning is natural-language guidance. Topic-fit claims are relative to that meaning. Confidence is model-generated/clamped or manually set, not measured calibration. Different from Category.description because membership selectors and replacement/upsert policies consume this part. SRC-1, `lib/categorizer.ts`; closest supplied record is [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize), which supplies parser/writer evidence. Manual contrast is see [RT-RTE-category-admission](runtime.md#rt-rte-category-admission).

#### EPI-OBJ-category-description
Label: Category.description
Part of: [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark)

SQLite natural-language category guidance; symbolic slug determines output admissibility. Shipped defaults, admitted suggestions and directly caller-authored descriptions have different origins but share the later categorization prompt consumer. The admission-route inventory here is partial: `app/api/categories/route.ts` also persists caller descriptions with isAiGenerated=false, and its GET seeds defaults when the category store is empty. This is not evidence of human approval or topic quality. SRC-1, `app/api/categories/route.ts`:

> description: description?.trim() ?? null,
>         isAiGenerated: false,
> --- `app/api/categories/route.ts`

 These are organizational instructions, not necessarily truth-apt explanations. Distinct from membership links by content and downstream channel. SRC-1, `lib/categorizer.ts`; see [RT-BAP-category-guidance](runtime.md#rt-bap-category-guidance) for load-bearing prompt construction and [RT-RTE-category-admission](runtime.md#rt-rte-category-admission) for admission.

#### EPI-OBJ-search-matches
Label: matches and explanation

Model-returned JSON in current request memory and short-lived module cache: symbolic IDs/scores plus natural-language reasons/explanation. Relevance assessments can include factual claims about candidate content. Unlike [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark), this is a transient query-specific result rather than persisted collection state; no supplied object counterpart after comparison. Closest supplied route is [RT-RTE-search-content](runtime.md#rt-rte-search-content). SRC-1, `app/api/search/ai/route.ts`:

> const response = { bookmarks: results, explanation: aiResponse.explanation }
>   setCache(cacheKey, response)
>   return NextResponse.json(response)
> --- `app/api/search/ai/route.ts`

### Routes

#### EPI-RTE-entity-extraction
Label: Raw JSON entity extraction
Part of: [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize)

Material subroute separated from the pipeline because deterministic extraction has a different warrant from model generation. Pipeline backfill selects Bookmark.entities=null, reads rawJson, applies extractEntities and writes JSON into Bookmark.entities. Software owns progression; abort checks are cooperative. No human per-record veto or expected-answer oracle. Operating mode is ordinary backfill, not an experiment. Missing/invalid JSON yields defaults rather than a source-truth rejection. Fields copied from JSON are acquired assertions; type/media predicates are consequences of code conditions, not independently verified tweet properties. URL tool lookup's semantic fidelity is unassessed.

- Immediate return: Count of updated bookmarks with optional progress callbacks.
- Later read-back: entities feeds categorization, semantic enrichment, FTS/search and CLI detail on later invocations.
- Delegated visibility: Selected hashtags/tools/mentions enter bounded model prompts, not all rawJson.
- Selection predicate: entities=null; chunks of 100; source extraction tries root and legacy paths.
- Invalidation or expiry: No version-based expiry in inspected backfill; non-null values no longer selected there.
- Activation or effect: Code writes fields consumed later; actual influence unobserved.
- Evidence limits: Input encoding fidelity, tool-label correctness and deployed values unobserved; invalid input can resemble a genuinely empty original tweet.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `lib/rawjson-extractor.ts`:

> const hashtags = (hashtagObjs as Record<string, unknown>[])
>     .map((h) => String(h.tag ?? h.text ?? '').toLowerCase())
>     .filter(Boolean)
> --- `lib/rawjson-extractor.ts`

> const hasMedia = (mediaArr as []).length > 0
> --- `lib/rawjson-extractor.ts`

> data: { entities: JSON.stringify(entities) },
> --- `lib/rawjson-extractor.ts`

Implementation deduction, not execution: for raw input `{"entities":{"hashtags":[{"tag":"AI"}],"media":[{"type":"photo"}]}}`, root-path lookup yields hashtags `["ai"]`, hasMedia=true and mediaTypes `["photo"]`. This follows only within the inspected JSON/code domain. It does not establish that an image exists remotely or that the post is about AI. No quote or input artifact is claimed as observed operation.

#### EPI-RTE-image-analysis
Label: Vision annotation and disposition
Part of: [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize)

This is the pipeline's image-analysis part, also reached independently from `app/api/analyze/images/route.ts`. Model proposes annotations; software fetches image bytes for SDK or sends URL text to an external CLI, extracts an object-shaped substring and checks parseability. The check target is JSON syntax, not correspondence to the image. analyzeItem first checks another row with the same URL and non-null imageTags; cached text can bypass generation and new validation. Video uses thumbnailUrl when present and injects a thumbnail marker into newly generated JSON. Successful text or `{}` is persisted. Starting analysis is not human approval; code can reject invalid/missing output, retry designated errors or mark attempted failure. No answer oracle; ordinary annotation mode. Force cleanup and downstream selectors are see [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize).

- Immediate return: analyzeItem returns 1 after copied/generated tags or 0 after failure marker; independent image endpoint returns analyzed/remaining counts.
- Later read-back: imageTags reaches enrichment, categorization, FTS/AI search, CLI show and later URL cache lookup. Export builders omit the imageTags payload; influence via exported semantic tags or category assignments is a separate upstream chain, not direct payload delivery (SRC-1, `lib/exporter.ts`, `lib/obsidian-exporter.ts`).
- Delegated visibility: SDK receives fetched base64 image and analysis prompt; CLI receives sanitized URL text plus prompt. Downstream prompts receive selected image fields.
- Selection predicate: Pipeline untagged media; independent endpoint photo/gif with imageTags=null; URL cache first selects a different row with same URL and non-null imageTags.
- Invalidation or expiry: `{}` prevents ordinary null-only retries; force clears these markers, but successful annotations have no assessed TTL/version invalidation.
- Activation or effect: Annotation/failure writes and later selectors are wired; correctness and behavioral influence unobserved.
- Evidence limits: Cached marker inherits unknown provenance; CLI image access opaque; JSON syntax establishes neither schema nor truth; counter increments do not certify useful analysis.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `lib/vision-analyzer.ts`:

> JSON.parse(jsonMatch[0]) // throws if invalid
>     return jsonMatch[0]
> --- `lib/vision-analyzer.ts`

> where: { url: imageUrl, imageTags: { not: null }, id: { not: excludeId } },
> --- `lib/vision-analyzer.ts`

> if (cached) {
>     await prisma.mediaItem.update({ where: { id: item.id }, data: { imageTags: cached } })
>     return 1
>   }
> --- `lib/vision-analyzer.ts`

> await prisma.mediaItem.update({ where: { id: item.id }, data: { imageTags: '{}' } })
>   return 0
> --- `lib/vision-analyzer.ts`

The independent endpoint is a countercase to treating categorization as the only writer:

> const analyzed = await analyzeBatch(untagged, client)
> --- `app/api/analyze/images/route.ts`

#### EPI-RTE-image-context
Label: Compact image context
Part of: [RT-RTE-model-dispatch](runtime.md#rt-rte-model-dispatch)

A distinct pre-dispatch transformation, not another model executor. buildImageContext parses imageTags and selects style/scene/action, bounded OCR, first tags and meme template; on parse failure it returns a 300-character raw slice. Category and enrichment prompt builders consume the string. This transformation supplies working context but does not check annotation accuracy. Code owns selection. No human admission, expected answer or improvement loop applies; ordinary prompt preparation.

- Immediate return: Compact string or empty string for missing input.
- Later read-back: inapplicable — this helper does not persist its output; callers independently read retained imageTags for later invocations.
- Delegated visibility: Selected fields enter categorization/enrichment prompts; people/objects/mood are not emitted as named fields by this helper.
- Selection predicate: Truthy named scalar fields, array OCR and tags; first 15 tags and first 200 joined OCR characters.
- Invalidation or expiry: inapplicable — recomputed current-call value, no helper cache.
- Activation or effect: Fixed omissions and truncation determine delivered context; effect on model judgment unobserved.
- Evidence limits: Parse fallback is raw truncation; no semantic preservation guarantee for arbitrary malformed types or truncation across a sentence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `lib/image-context.ts`:

> if (parsed.style) parts.push(`Style: ${parsed.style}`)
> --- `lib/image-context.ts`

> if (Array.isArray(parsed.tags) && (parsed.tags as unknown[]).length)
>       parts.push(`Visual tags: ${(parsed.tags as string[]).slice(0, 15).join(', ')}`)
> --- `lib/image-context.ts`

> return parts.join(' | ')
> --- `lib/image-context.ts`

Concrete implementation deduction: `{"style":"chart","tags":["bitcoin"],"people":["Ada"]}` becomes `Style: chart | Visual tags: bitcoin`; the people field is omitted. This is field selection/reformatting, not a new inference that the chart concerns bitcoin, nor acceptance that Ada appears. No execution was needed to derive this fixed transformation from the inspected branches. Callers may retain original imageTags even though this particular context drops the field.

#### EPI-RTE-semantic-tags
Label: Semantic metadata generation and admission
Part of: [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize)

Separate material part because generated semantic metadata has its own parser, writer and later consumers. The model receives bounded bookmark text, image context and selected entities. parseResponse extracts a JSON array, coerces IDs/fields to strings and drops empty IDs; it does not validate semantic associations. In the ordinary per-bookmark pipeline, code selects results[0] and writes its tags/meta to the current bookmark if tags are nonempty. It does not compare returned ID to bm.id at that point. The bulk helper instead constructs a resultMap keyed by ID and selects the matching current bookmark. This countercase limits the identity weakness to the actual caller rather than asserting it for every helper. Software admits results; no per-result human approval or expected-answer oracle. Open annotation mode. Trivial short text without image tags gets `[]`; failed ordinary enrichment otherwise leaves tags unset. Null tags preserve stage eligibility, not endpoint reselection: the endpoint first selects enrichedAt=null unless explicit IDs or force override it. The bookmark is still queued for categorization after enrichment failure; category admission can independently set enrichedAt. A later ordinary invocation then skips that row despite null semanticTags. Explicit-ID or force selection can recover the missing enrichment; force also clears empty markers, not all successful output. The separate bulk helper selects semanticTags=null independently of enrichedAt, so its retry behavior does not establish retry through the shipped endpoint.

- Immediate return: EnrichmentResult array or empty array/error handled by caller; pipeline progress counts attempts/effects, not truth.
- Later read-back: Stored semanticTags/enrichmentMeta feed category prompts, search eligibility/reranking and CLI detail; prior tags can shape category suggestions via sampled metadata.
- Delegated visibility: Text sliced to 500 characters, compact image context, bounded hashtags/mentions and tools; models do not receive the entire imported record.
- Selection predicate: Endpoint first selects explicit bookmarkIds, else all rows for force, else enrichedAt=null. Only within that selected set does the enrichment stage test missing semanticTags and triviality. The separate bulk helper selects semanticTags=null with cursor pagination, without an enrichedAt gate. Parser accepts nonempty returned IDs and arrays coerced to strings; ordinary writer requires first result's nonempty tags.
- Invalidation or expiry: No correctness/version TTL identified. Null semanticTags permits another stage attempt only if the endpoint reselects the row: ordinary reselection requires enrichedAt=null, while successful categorization can set enrichedAt even after enrichment failed. Explicit IDs or force bypass that reselection gate; empty-array markers require force clearing in the pipeline. The bulk helper's null-tag selector is a distinct retry path, not a guarantee of endpoint recovery.
- Activation or effect: Durable metadata write and downstream prompt/index wiring; compliance, accuracy and benefit unobserved.
- Evidence limits: Model sentiment/people/company associations unverified; no actual response demonstrates non-entailment or faithfulness; caller ID policies differ.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `lib/vision-analyzer.ts`:

> - people: named people mentioned or shown (max 5, empty array if none)
> - companies: company/product/tool names explicitly referenced (max 8, empty array if none)
> --- `lib/vision-analyzer.ts`

> sentiment: String(item.sentiment ?? 'neutral'),
> --- `lib/vision-analyzer.ts`

SRC-1, `app/api/categorize/route.ts`:

> const result = results[0]
>                   if (result?.tags.length) {
>                     await prisma.bookmark.update({
>                       where: { id: bm.id },
> --- `app/api/categorize/route.ts`

The endpoint's outer selection precedes the missing-tag stage gate (SRC-1):

> const unprocessed = await prisma.bookmark.findMany({
>               where: { enrichedAt: null },
> --- `app/api/categorize/route.ts`

Enrichment failure does not prevent subsequent queue admission:

> // Queue for categorization
>             catPending.push(bm.id)
> --- `app/api/categorize/route.ts`

The category writer updates the selection timestamp without testing semanticTags:

> prisma.bookmark.updateMany({
>       where: { id: { in: bookmarkIdsToUpdate } },
>       data: { enrichedAt: now },
> --- `lib/categorizer.ts`

The contrasting bulk helper uses a different outer selector (SRC-1):

> const rows = await prisma.bookmark.findMany({
>       where: {
>         semanticTags: null,
>         ...(cursor ? { id: { gt: cursor } } : {}),
> --- `lib/vision-analyzer.ts`

Its returned-ID lookup also differs:

> const resultMap = new Map(results.map((r) => [r.id, r]))
>
>       for (const b of batch) {
>         const result = resultMap.get(b.id)
> --- `lib/vision-analyzer.ts`

#### EPI-RTE-content-withdrawal
Label: Collection clearing and category deletion

Distinct from [RT-RTE-category-admission](runtime.md#rt-rte-category-admission), which describes creation/manual assignment, and [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize), which upserts rather than retracts omitted assignments. HTTP caller requests deletion; code owns transaction/category lookup. Clear deletes all BookmarkCategory, MediaItem, Bookmark and Category rows transactionally. Category DELETE checks slug existence then deletes the category; schema cascade removes its membership links. No content critic or truth oracle judges the removed content. Mode is caller-directed maintenance, not an evaluation. No rollback history implemented in these handlers; reimport/recreation is a separate path. The clear handler does not cancel a running pipeline, rebuild FTS, clear search result caches or delete exported notes. Search cache can return a previously hydrated response until TTL; fresh DB reads cannot find deleted rows. Deleting defaults can be temporary because pipeline seeding recreates them. These limits prevent claiming immediate universal withdrawal.

- Immediate return: success or error for clearing; category deleted/slug/name, 404 or error for category deletion.
- Later read-back: Later uncached database reads reflect removal; prior result cache and external exports can retain old content.
- Delegated visibility: HTTP caller receives acknowledgment; deletion supplies no new model prompt directly.
- Selection predicate: All collection/category rows for clear; existing Category.slug for single category deletion.
- Invalidation or expiry: Database deletion persists unless reimport/reseed/recreation; independent five-minute search-result TTL remains.
- Activation or effect: Database deletion and downstream read exclusion wired; no observed withdrawal run.
- Evidence limits: No target execution, remote-vault deletion or in-flight concurrency guarantee; no evidence-consuming acceptance/rejection of proposition truth.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `app/api/bookmarks/route.ts`:

> await prisma.$transaction([
>       prisma.bookmarkCategory.deleteMany({}),
>       prisma.mediaItem.deleteMany({}),
>       prisma.bookmark.deleteMany({}),
>       prisma.category.deleteMany({}),
>     ])
> --- `app/api/bookmarks/route.ts`

SRC-1, `app/api/categories/[slug]/route.ts`:

> await prisma.category.delete({
>       where: { slug },
>     })
> --- `app/api/categories/[slug]/route.ts`

Cache and export persistence countercases are see [RT-RTE-search-content](runtime.md#rt-rte-search-content) and [RT-RTE-cli-export](runtime.md#rt-rte-cli-export); default reseeding is see [RT-RTE-category-admission](runtime.md#rt-rte-category-admission). These supplied records bound consequential consumers rather than treating database deletion as complete withdrawal.

### Claims

#### EPI-CLM-tags-reliability
Label: Search prompt tag reliability

SRC-1, `app/api/search/ai/route.ts`, doctrine/design: the search prompt describes precomputed AI tags as highly reliable and instructs the reranking model to check them. This is a distinct downstream warrant claim from [RT-CLM-category-policy](runtime.md#rt-clm-category-policy), which asks the categorization model to trust aiTags heavily. The shared origin of tags does not make these different consumer instructions one referent. Search prompt delivery is implemented; reliability is not established by the generation/parsing route or supplied run evidence.

> 2. Check ALL fields — the ai_tags field contains pre-computed semantic context and is highly reliable
> --- `app/api/search/ai/route.ts`
