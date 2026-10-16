---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Synto epistemic routes: source-derived candidates, structural checks, publication authority and later answer consumption."
run-id: AAS-2026-10-15-synto-eabcdcce3da2-01
reviewed-boundary: "91ac6a3681df0552b6c9baef159439c7ebd780c9"
---

# Synto epistemic report

## Source-and-claim boundary

The question is how Synto turns source notes into claims available for later reliance, and what its checks license. Scope and exclusions are those of [the boundary](boundary.md#boundary-and-evidence); source identities and evidence layers are in its [Source register](boundary.md#source-register). Every source finding below uses SRC-1 at the frozen commit. Implementation and doctrine/design are distinguished; no target execution was performed and no observed-run or causal evidence was supplied.

Model weights, human judgment, actual host compliance and external source truth are outside the inspected implementation. Their absence prevents conclusions about factual accuracy, reviewer competence, downstream benefit or parameter learning. A source ID, content hash, confidence number or published status does not alone supply those facts. No supplied runtime finding needs supersession: the new records below separate material functions inside its valid route containers.

### Coverage

Direct reads supplement, rather than replace, the supplied runtime account. Available but uninspected operations are explicit below; this report makes no system-complete negative about all possible evaluation or knowledge production.

| Entry point or operation | Source path (SRC-1) | Inspection and record coverage or limit |
|---|---|---|
| run, ingest, compile, watch; legacy compile | `src/synto/cli.py`, `src/synto/pipeline/orchestrator.py`, `src/synto/pipeline/ingest.py`, `src/synto/pipeline/compile.py`, `src/synto/watcher.py` | Supplied [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run); direct CLI dispatch search, ingest filters/occurrences/relations, writer prompt and draft cleanup. Legacy compile dispatch identified but its planning implementation not inspected here; prevents exhaustive production-route classification. |
| Source add, extraction, segmentation | `src/synto/cli.py`, `src/synto/extractors/` | Supplied boundary import account; direct CLI dispatch search only. Extraction fidelity and exact import warrant remain unassessed. |
| Source-type prompting, parsing | `src/synto/pipeline/prompts/notes.md`, `src/synto/models.py`, `src/synto/structured_output.py` | Notes prompt and AnalysisResult/SingleArticle directly read; parser wiring supplied by runtime. Other six prompt wordings uninspected here, preventing universal prompt-policy claims. |
| approve, verify, reject, review, unblock | `src/synto/pipeline/compile.py`, `src/synto/pipeline/review.py`, `src/synto/cli.py` | Publication/verification/rejection directly read; interactive review dispatch searched; [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication). Human decision content not supplied. |
| query, save, synthesize | `src/synto/pipeline/query.py`, `src/synto/engines.py` | Core, saving and synthesis checks directly read; engine wiring supplied by [RT-RTE-query-answer](runtime.md#rt-rte-query-answer). |
| MCP answer and article primitives | `src/synto/serve.py` | Handler search; supplied [RT-RTE-mcp-answer](runtime.md#rt-rte-mcp-answer). Article visibility is operational disclosure authority, not epistemic endorsement. |
| MCP verbatim reads/search/passages/list | `src/synto/serve.py` | Direct read of registration, segment read, search and passage selection preamble; remainder supplied at container level only. Exact list/passages formatting not fully assessed; prevents complete delivery-fidelity verdict. |
| maintain, curation, alias operations, items, trace, find, doctor reconcile | `src/synto/pipeline/maintain.py`, `src/synto/pipeline/lint.py`, `src/synto/cli.py` | CLI dispatch searched; lint graph advisories directly read; merge/split supplied by [RT-RTE-concept-curation](runtime.md#rt-rte-concept-curation). Alias/keep/reconcile mutation bodies and item extraction remain uninspected here; prevents exhaustive semantic-curation and authority claims. |
| undo, clean | `src/synto/cli.py` | Direct complete command reads; recovery/withdrawal qualifications below. |
| eval, compare, smoke/CI | `src/synto/pipeline/eval.py`, `src/synto/compare/runner.py`, `scripts/`, `.github/` | Complete offline evaluator directly read; comparison supplied by [RT-RTE-compare-eval](runtime.md#rt-rte-compare-eval). Test/script definitions are not runs. |
| pack export, indexes and read-back | `src/synto/pack_export.py`, `src/synto/indexer.py`, `src/synto/readers.py` | Direct `generate_index` read distinguishes synthesis admission from ordinary Q&A persistence; supplied [RT-RTE-pack-export](runtime.md#rt-rte-pack-export), [RT-BAP-pack-guidance](runtime.md#rt-bap-pack-guidance) and boundary. Exported instructions request source verification; host adherence unobserved. |
| setup, config, init, migrate, vault, report, support | `src/synto/cli.py` | Dispatch searched. Configuration can change model/prompt/admission settings; model mutability supplied by runtime components. Setup/migration correctness not assessed; counters and support are not evidence of accepted factual content. |

Knowledge/warrant-facing claims are [EPI-CLM-wiki-synthesis](#epi-clm-wiki-synthesis), [EPI-CLM-quality-evaluation](#epi-clm-quality-evaluation) and [EPI-CLM-staged-review](#epi-clm-staged-review).

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-source-segment](#epi-obj-source-segment) | Imported source assertions | Original wording/evidence | See record | Truth of original source unknown; extraction lineage not fully inspected |
| [EPI-OBJ-analysis-result](#epi-obj-analysis-result) | Summaries, concept/source associations, source-quality assessment | Source analysis | See record | Model output semantic fidelity unobserved |
| [EPI-OBJ-relation](#epi-obj-relation) | Subject–predicate–object assertion and evidence string | Graph/routing relation | See record | Endpoint existence does not establish asserted relationship |
| [EPI-OBJ-single-article](#epi-obj-single-article) | Generated article assertions | Retained wiki knowledge | See record | No supplied article instance or reviewer evidence |
| [EPI-OBJ-confidence](#epi-obj-confidence) | None as a factual claim about article correctness; deterministic source-count/quality indicator | Admission and quality signal | See record | Not a calibrated probability of truth |
| [EPI-OBJ-query-answer](#epi-obj-query-answer) | Answer/synthesis assertions | Answer using wiki content | See record | Entailment, novelty and truth not determinable without actual candidate and inputs |
| [RT-CMP-fast](runtime.md#rt-cmp-fast), [RT-CMP-heavy](runtime.md#rt-cmp-heavy), [RT-CMP-embed](runtime.md#rt-cmp-embed) | Not determinable at individually localized claim level | Inference and optional vectors | See components | Provider-held distributed-parametric state; no inspected parameter update, immutable weights unpinned, mutable endpoints possible; internals uninspected |
| [RT-BAP-rejection-guidance](runtime.md#rt-bap-rejection-guidance) | Feedback may challenge claims; no feedback instance supplied | Revision guidance | See record | Cannot infer formulated theory criticism or successful revision from delivery |
| [RT-BAP-pack-guidance](runtime.md#rt-bap-pack-guidance) | Policy rather than new factual knowledge | Later-agent reading instructions | See record | Delivery/compliance host-dependent |

## Authority-route ledger

The architectural statuses below concern inspected wiring, not operation. Fields owned by declaring records are referenced rather than recopied. Content relations concern the named edge, not everything in its container. Separate rows keep checking, disposition and retention apart.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run) | content transformation | implemented | [EPI-OBJ-analysis-result](#epi-obj-analysis-result), [EPI-OBJ-single-article](#epi-obj-single-article) | truth-apt transformation: indeterminate | Source text → generated summaries/articles | Fast/heavy inference; schema parse, not truth oracle | Ingest/compile invocation | Candidate text and metadata | Generation and persistence | Candidate only; imported premises are not independently warranted | Makes content available for draft review | see [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run) | see [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run) | [EPI-CLM-wiki-synthesis](#epi-clm-wiki-synthesis) | none | Requested faithful extraction/synthesis; neither entailment nor non-entailment established for absent instances |
| [EPI-RTE-candidate-filter](#epi-rte-candidate-filter) | check/evidence production | implemented | [EPI-OBJ-analysis-result](#epi-obj-analysis-result), [EPI-OBJ-relation](#epi-obj-relation) | no content change | Candidate name support and relation endpoints | Code lexical/identity domain | Before canonical admission | Surviving concepts; resolvable endpoints | Enforcing local filter | Lexical occurrence/identity only | Blocks selected candidates, not every unsupported assertion | see [EPI-RTE-candidate-filter](#epi-rte-candidate-filter) | see [EPI-RTE-candidate-filter](#epi-rte-candidate-filter) | none | none | No observed run |
| [EPI-RTE-occurrence-lineage](#epi-rte-occurrence-lineage) | retention | implemented | [EPI-OBJ-source-segment](#epi-obj-source-segment), [EPI-OBJ-relation](#epi-obj-relation) | no content change | Chunk/segment association retained | Code canonical-name survival and chunk membership | After analysis normalization | Occurrence rows and relation evidence | Durable linkage | Chunk association, not exact supporting passage proof | Changes later passage retrieval/ranking and graph context | see [EPI-RTE-occurrence-lineage](#epi-rte-occurrence-lineage) | see [EPI-RTE-occurrence-lineage](#epi-rte-occurrence-lineage) | none | none | Concepts attributed to every segment in chunk; confidence 1.0 does not certify local assertion support |
| [EPI-RTE-confidence-score](#epi-rte-confidence-score) | check/evidence production | implemented | [EPI-OBJ-confidence](#epi-obj-confidence) | no content change | Source count and best quality | Code arithmetic over fast-model structural quality label | Before draft writing | 0–1 scalar | Threshold input | Only named proxy; not correctness calibration | Can hold drafts back when threshold enabled | see [EPI-RTE-confidence-score](#epi-rte-confidence-score) | see [EPI-RTE-confidence-score](#epi-rte-confidence-score) | [EPI-CLM-staged-review](#epi-clm-staged-review) | Proxy versus truth scope | No observed run |
| [EPI-RTE-markdown-repair](#epi-rte-markdown-repair) | content transformation | implemented | [EPI-OBJ-single-article](#epi-obj-single-article) | truth-apt transformation: non-ampliative reshaping | Link syntax in generated text | Code known-title rules | Before draft persistence | Unknown links become plain text | Enforcing formatting | No added warrant for underlying proposition | Removes navigation, retains unsupported prose | see [EPI-RTE-markdown-repair](#epi-rte-markdown-repair) | see [EPI-RTE-markdown-repair](#epi-rte-markdown-repair) | none | none | Classification scoped to link unwrapping; not universal semantic preservation of all cleanup |
| [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication) | disposition/acceptance | implemented | [EPI-OBJ-single-article](#epi-obj-single-article) | no content change | Draft → verified/published or rejected | Explicit human command or automatic threshold; code path/existence checks | After generation; verify optional | Status/write or deletion/feedback | Publication enforcing; feedback advisory | Recorded approval marker, but evidence-consuming factual acceptance not established | Published location admits later consumers; rejection removes draft | see [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication) | see [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication) | [EPI-CLM-staged-review](#epi-clm-staged-review) | Verification not required | No observed run |
| [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run) | retention | implemented | [EPI-OBJ-analysis-result](#epi-obj-analysis-result), [EPI-OBJ-single-article](#epi-obj-single-article) | no content change | Generated analysis/draft → disk/DB | Code after parse and preprocessing | During ingestion/compile | Persistent candidates | Storage | Retention is not acceptance | Later compilation/review/export can read candidates | see [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run) | see [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run) | none | none | No observed run |
| [RT-RTE-query-answer](runtime.md#rt-rte-query-answer) | operational admission/selection/consumption | implemented | [EPI-OBJ-single-article](#epi-obj-single-article), [EPI-OBJ-query-answer](#epi-obj-query-answer) | no content change | Retained pages → model input | Fast relevance selector, code caps/optional graph expansion | Per question | Page body slices in answer prompt | Ranking and context admission | Selected context, not truth endorsement | Conditions answer generation on delivered slice | see [RT-RTE-query-answer](runtime.md#rt-rte-query-answer) | see [RT-RTE-query-answer](runtime.md#rt-rte-query-answer) | [EPI-CLM-wiki-synthesis](#epi-clm-wiki-synthesis) | none | Selected names do not prove every body loaded |
| [RT-RTE-query-answer](runtime.md#rt-rte-query-answer) | content transformation | implemented | [EPI-OBJ-query-answer](#epi-obj-query-answer) | truth-apt transformation: indeterminate | Question plus selected pages → answer | Heavy model; structured parsing and sanitation | After selection | Answer text | Returned/advisory | Grounding request; no inspected entailment decision | Returns answer even if no matching page context | see [RT-RTE-query-answer](runtime.md#rt-rte-query-answer) | see [RT-RTE-query-answer](runtime.md#rt-rte-query-answer) | [EPI-CLM-wiki-synthesis](#epi-clm-wiki-synthesis) | none | No answer instance; cannot classify as entailed derivation or ampliative conjecture |
| [EPI-RTE-synthesis-guard](#epi-rte-synthesis-guard) | check/evidence production | implemented | [EPI-OBJ-query-answer](#epi-obj-query-answer) | no content change | Synthesis source chain, duplicate identity and overwrite safety | Code path/hash/equality domain | On synthesis save/update | Refusal, keep existing or eligible write | Enforcing safety checks | No factual-answer license | Blocks synthesis-of-synthesis and edited overwrite | see [EPI-RTE-synthesis-guard](#epi-rte-synthesis-guard) | see [EPI-RTE-synthesis-guard](#epi-rte-synthesis-guard) | none | none | Safety and lineage checks are counterexamples to no-check claims, not semantic validation |
| [EPI-RTE-answer-retention](#epi-rte-answer-retention) | retention | implemented | [EPI-OBJ-query-answer](#epi-obj-query-answer) | no content change | Answer → queries/synthesis files | Caller save flag; code save guards | After answer return | Published-tagged Q&A file or registered synthesis | Durable admission | No evidence-consuming factual acceptance established | Synthesis enters index selection; ordinary Q&A remains filesystem/export-accessible and resolvable if its title is supplied | see [EPI-RTE-answer-retention](#epi-rte-answer-retention) | see [EPI-RTE-answer-retention](#epi-rte-answer-retention) | [EPI-CLM-wiki-synthesis](#epi-clm-wiki-synthesis) | Bypasses draft publication | No observed run |
| [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication) | behavior/policy adaptation | implemented | [RT-BAP-rejection-guidance](runtime.md#rt-bap-rejection-guidance) | non-truth-apt policy/content update: rejection feedback supplied as revision guidance | Rejected draft → later writing prompt | Human feedback; code stores/delivers; rejection cap blocks | Later recompile | Feedback inclusion or blocked concept | Advisory model instruction plus enforcing cap | Correctness of criticism unestablished | Changes next writer input; unblock can restore eligibility | see [RT-BAP-rejection-guidance](runtime.md#rt-bap-rejection-guidance) | see [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication) | none | none | No observed successful correction, capacity improvement or own-method revision |
| [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | check/evidence production | implemented | [EPI-OBJ-single-article](#epi-obj-single-article) | no content change | Article existence, sources-list presence, links, INDEX schema | Deterministic structural evaluator | Explicit eval; comparison uses separate runs | Metric report | Advisory/reporting | Structural coverage only | Operator can inspect; no inspected automatic production adoption | see [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | see [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | [EPI-CLM-quality-evaluation](#epi-clm-quality-evaluation) | Citation support is metadata coverage | No observed run |
| [EPI-RTE-verbatim-source](#epi-rte-verbatim-source) | operational admission/selection/consumption | implemented | [EPI-OBJ-source-segment](#epi-obj-source-segment) | no content change | Stored source text → MCP response | ID lookup/license gate; optional character cap | Tool invocation | Body, hash, source identity, truncation marker | Enforcing disclosure gate | Attributed stored text, not truth of source | Permits external agent to inspect original assertions | see [EPI-RTE-verbatim-source](#epi-rte-verbatim-source) | see [EPI-RTE-verbatim-source](#epi-rte-verbatim-source) | none | none | Storage text lineage to original bytes not fully inspected |
| [RT-RTE-concept-curation](runtime.md#rt-rte-concept-curation) | content transformation | implemented | [EPI-OBJ-analysis-result](#epi-obj-analysis-result) | truth-apt transformation: indeterminate | Human-selected concept grouping → identities/source allocation | Human semantic decision, software preflight | Explicit merge/split | Changed routing and source assignments | Enforcing mutation | No semantic equivalence oracle established | Changes later compile/query context | see [RT-RTE-concept-curation](runtime.md#rt-rte-concept-curation) | see [RT-RTE-concept-curation](runtime.md#rt-rte-concept-curation) | none | none | No applied curation instance; alias/keep branches not fully inspected here |
| [RT-RTE-pack-export](runtime.md#rt-rte-pack-export) | operational admission/selection/consumption | implemented | [EPI-OBJ-single-article](#epi-obj-single-article), [EPI-OBJ-query-answer](#epi-obj-query-answer) | no content change | Retained files → distributed pack | Exporter selection/copy rules | Explicit export | Pack, including optional unpublished trees | Filesystem delivery and requested guidance | Portable content is not accepted factual content | Later host may read/index/summarize | see [RT-BAP-pack-guidance](runtime.md#rt-bap-pack-guidance) | see [RT-RTE-pack-export](runtime.md#rt-rte-pack-export) | none | none | Host compliance unobserved; no export-wide draft exclusion |
| [EPI-RTE-state-recovery](#epi-rte-state-recovery) | lineage/freshness/recovery | implemented | [EPI-OBJ-single-article](#epi-obj-single-article), [EPI-OBJ-analysis-result](#epi-obj-analysis-result) | no content change | Undo/clean retained state | Human invocation; code identity-op guard | Explicit recovery/destruction | File revert or state/wiki deletion with seed | Enforcing local operation | Withdrawal/rebuild, not factual correction | Changes available files; DB may diverge after revert | see [EPI-RTE-state-recovery](#epi-rte-state-recovery) | see [EPI-RTE-state-recovery](#epi-rte-state-recovery) | none | none | Not distributed revocation of prior packs or returned answers |

No lifecycle-integration row is asserted: publication, indexes and source links are operational organization, but evidence-consuming acceptance of a claim against a named factual criterion is not established for these inspected paths. This is a route-local limit, not a claim that a human cannot perform such review.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source and evidence layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support/design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-wiki-synthesis](#epi-clm-wiki-synthesis) | Synthesized, current wiki; query/synthesis using pages | See claim | Source prompts and answer grounding instructions | See [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run), [RT-RTE-query-answer](runtime.md#rt-rte-query-answer), [EPI-RTE-answer-retention](#epi-rte-answer-retention) | None supplied | No measured accuracy, novelty or benefit | Generated and retained wiki/answer candidates, bounded context reload | “Synthesis” does not establish produced accepted ampliative claims; freshness not endorsement |
| [EPI-CLM-quality-evaluation](#epi-clm-quality-evaluation) | Offline quality/citation support | See claim | Offline structural scope explicitly documented elsewhere in README | See [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | None supplied | No proposition-level citation support test | Structural indicators and reports | Citation label broader than actual nonempty-sources-list predicate if read semantically |
| [EPI-CLM-staged-review](#epi-clm-staged-review) | Confidence and draft → verified → published lifecycle | See claim | Optional explicit review step | See [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication), [EPI-RTE-confidence-score](#epi-rte-confidence-score) | None supplied | Human review quality unknown; automatic publishing available | Optional staging plus proxy threshold | Not mandatory sequential verification; score not truth probability |

## Bounded conclusion

Synto acquires externally authored notes and can deliver stored source paragraphs with identity, hash and optional truncation indication. Retained segments reach later MCP client invocations: this is read-back even though the read handler does not write knowledge. Delivery does not establish answer saving or downstream model use. This preserves access to attributed assertions, not their truth; original extraction fidelity remains unassessed. Chunk-to-segment attribution can overinclude passages: association is not exact sentence support. See [EPI-RTE-verbatim-source](#epi-rte-verbatim-source) and [EPI-RTE-occurrence-lineage](#epi-rte-occurrence-lineage).

The fast/heavy stages produce truth-apt candidate summaries, relationships, articles and answers. Their semantic relation is indeterminate without candidate/input instances. Faithful extraction is requested, but model novelty or entailed derivation is not established. Deterministic unwrapping of an unknown link preserves its displayed assertion while removing navigation; source-count scoring derives only an operational indicator. Neither licenses source truth or article correctness. See [EPI-RTE-markdown-repair](#epi-rte-markdown-repair), [EPI-RTE-confidence-score](#epi-rte-confidence-score) and [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run).

There are real implemented checks: schema parsing, lexical candidate filters, closed relation endpoints, synthesis-chain/duplicate/edit guards, lint and offline structural tests. Their domains are not factual acceptance. Publication, verified labels and automatic thresholds grant operational availability rather than demonstrated evidence-consuming acceptance. Retention and index refresh therefore do not establish lifecycle integration after epistemic acceptance. Saved synthesis bypasses the draft gate and enters later index selection (the generated catalogue includes at most 25 synthesis entries). Ordinary Q&A saving writes files but does not automatically enumerate them into that index. Both retained forms remain available through filesystem/export paths; the recursive title resolver can load an ordinary Q&A file if its title is supplied. These are distinct consumer routes, not an absolute absence of Q&A recall. Exported packs may also contain drafts and raw material. The contrary cases were checked before limiting the conclusion: human review is possible, safety checks are present, but neither makes factual checking universal. See [EPI-RTE-candidate-filter](#epi-rte-candidate-filter), [EPI-RTE-synthesis-guard](#epi-rte-synthesis-guard), [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation), [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication) and [RT-RTE-pack-export](runtime.md#rt-rte-pack-export).

Rejection can remove a draft, retain criticism and change later writer input; the cap can block compilation until unblocked. This is a durable behavioral-authority path independent of whether the feedback itself is truth-apt. Learning benefit, formulated content-directed theory criticism, autonomous theory building and exercised self-improvement do not follow from storage/delivery; no concrete criticism/revision episode or improvement comparison was supplied. Provider-held parameters remain separately opaque and unpinned as stated in the runtime components. See [RT-BAP-rejection-guidance](runtime.md#rt-bap-rejection-guidance) and [RT-CMP-heavy](runtime.md#rt-cmp-heavy).

Undo and clean change local availability but do not retract distributed packs, reverse all DB state or warrant corrected knowledge. Evaluation reports support operator inspection; no inspected automatic winner-installation consumer turns comparison scores into production policy. Actual accuracy, future capacity improvement and causal benefit remain unobserved, without negating the implemented candidate, check, retention and consumption routes. See [EPI-RTE-state-recovery](#epi-rte-state-recovery) and [RT-RTE-compare-eval](runtime.md#rt-rte-compare-eval).

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-source-segment
Label: Source segment

Imported natural-language paragraph held in SQLite source_segments, with symbolic segment/source IDs and content hash. It can contain truth-apt source assertions. Distinct from model components; a material input/read object along [RT-RTE-mcp-answer](runtime.md#rt-rte-mcp-answer) rather than a duplicate route. SRC-1, `src/synto/serve.py` (read_source_segment).

#### EPI-OBJ-analysis-result
Label: AnalysisResult

Natural-language summary and concept names plus symbolic quality/language fields; persisted analysis and source associations are in DB/generated source pages. [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run) consumes/produces this object; different record kind, not a duplicate. SRC-1, `src/synto/models.py` and `src/synto/pipeline/ingest.py`.

#### EPI-OBJ-relation
Label: Relation

Part of: [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run)

Subject/predicate/object labels and natural-language evidence with symbolic confidence/source segment binding, persisted in SQLite. Candidate assertions can affect graph-expanded querying. A material part of [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run) as a cross-kind output; not the inference component or full pipeline. SRC-1, `src/synto/pipeline/ingest.py` (_extract_and_persist_relations).

#### EPI-OBJ-single-article
Label: SingleArticle

Natural-language Markdown assertions, title and tags returned by heavy inference; draft/published Markdown and DB metadata retain the result. Object distinct from [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run) and [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication) route containers. SRC-1, `src/synto/models.py` and `src/synto/pipeline/compile.py`.

#### EPI-OBJ-confidence
Label: Confidence

Symbolic numeric indicator in draft frontmatter/DB. Source-count and best structural-quality calculation, not a calibrated correctness probability. Distinct scalar output of a part of [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run) and input to [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication). SRC-1, `src/synto/pipeline/compile.py` (_compute_confidence).

#### EPI-OBJ-query-answer
Label: QueryAnswer

Natural-language Markdown answer/title in current-call result; save paths retain Markdown and symbolic source lists/hashes. It is the output object, not a duplicate of [RT-RTE-query-answer](runtime.md#rt-rte-query-answer). SRC-1, `src/synto/pipeline/query.py` (_query_core, run_query, _save_synthesis_new).

Object evidence (implementation/schema; model instruction descriptions are doctrine/design):

> summary: str = Field(description="2-3 sentence summary in the note's language")
> --- `src/synto/models.py`

> description="Source quality: high=well-structured, medium=usable, low=noise"
> --- `src/synto/models.py`

> title: str
> content: str = Field(
>     description="Full markdown body with [[wikilinks]] inline (no frontmatter)"
> )
> --- `src/synto/models.py`

### Routes

#### EPI-RTE-candidate-filter
Label: Concept and relation filtering

Part of: [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run)

SRC-1, `src/synto/pipeline/ingest.py`: code checks model-proposed concept lexical support (low/medium sources, including validated aliases) and relation endpoint resolvability. Python decides/vetoes; high-quality sources are a counterexample to universal lexical filtering. No answer oracle. Open ingestion, not a controlled experiment. These are checks before durable admission, not evidence-consuming decisions about article truth.

- Immediate return: Filtered candidate list and eligible relation writes.
- Later read-back: Surviving names and relation rows affect later compilation/routing; rejected raw relations remain in relation_candidates.
- Delegated visibility: Models supply proposals; code sees source body/path, quality and known identities.
- Selection predicate: Non-noise names; low/medium lexical evidence or alias evidence; relation endpoints canonicalizable.
- Invalidation or expiry: Reingestion/identity changes may replace associations; no truth expiry established.
- Activation or effect: Blocks selected candidate admission by fixed predicates.
- Evidence limits: No observed candidate or semantic evaluation; relation predicate/evidence truth not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if result.quality in ("low", "medium") and not has_evidence:
> --- `src/synto/pipeline/ingest.py`

> if subject is None or object_ is None:
> --- `src/synto/pipeline/ingest.py`

> db.insert_relation_candidates(result.relations, seg_id)
> --- `src/synto/pipeline/ingest.py`

#### EPI-RTE-occurrence-lineage
Label: Chunk occurrence and relation retention

Part of: [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run)

SRC-1, `src/synto/pipeline/ingest.py`: normalized concepts are attributed to every segment in their analysis chunk, with occurrence confidence 1.0; relation evidence and segment identity are retained separately. Code owns writes after normalization/endpoint filtering; no per-row human approval or semantic oracle. This is retained provenance metadata, not lifecycle integration after factual acceptance. Its consumer overlaps [RT-RTE-mcp-answer](runtime.md#rt-rte-mcp-answer) and graph-expanded [RT-RTE-query-answer](runtime.md#rt-rte-query-answer) but its persistence is within the pipeline only.

- Immediate return: DB occurrence replacement and relation upserts.
- Later read-back: MCP concept passages and graph neighbors can reuse these bindings later.
- Delegated visibility: Chunk input segment IDs and returned concept names; relations carry model evidence strings.
- Selection predicate: Only names surviving canonical normalization; relations require known endpoints.
- Invalidation or expiry: Clears source occurrences before replacement; source/identity changes govern future associations.
- Activation or effect: Retains attribution that can rank/select later source passages and context.
- Evidence limits: Chunk association overincludes possible evidence; no supplied attribution correctness measurements.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> for sid in seg_ids:
>     seg_to_concepts.setdefault(sid, set()).update(canon_here)
> --- `src/synto/pipeline/ingest.py`

> db.upsert_concept_occurrences([occ(name=c, confidence=1.0) for c in sorted(concepts)], sid)
> --- `src/synto/pipeline/ingest.py`

#### EPI-RTE-confidence-score
Label: Source-count quality proxy

Part of: [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run)

SRC-1, `src/synto/pipeline/compile.py`: deterministic code computes min(1, 0.25 × resolved source count + best quality bonus). Quality means structural usability in AnalysisResult, not source truth. It evaluates a proxy for draft admission, not propositions. Example deduction from inspected code: four low-quality resolved sources give 1.0; three high-quality resolved sources also give 1.0. Those scores can satisfy an enabled threshold without checking any article sentence. This is arithmetic over metadata, not entailed derivation of article facts.

- Immediate return: Numeric scalar passed to draft writer.
- Later read-back: Retained confidence is read by review/publication thresholds and article consumers.
- Delegated visibility: Code sees source paths/DB quality, not claim-level supporting text in this function.
- Selection predicate: Best available quality, default low; count of resolved sources.
- Invalidation or expiry: Recompile recalculates; changing sources does not establish historical calibration.
- Activation or effect: Can enforce caller-selected minimum through publication branch; not a universal gate.
- Evidence limits: No calibration or factual-outcome comparison supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> _QUALITY_BONUS = {"high": 0.25, "medium": 0.1, "low": 0.0}
> --- `src/synto/pipeline/compile.py`

> best = _source_quality_summary(source_paths, db)
> return min(1.0, len(source_paths) * 0.25 + _QUALITY_BONUS.get(best, 0.0))
> --- `src/synto/pipeline/compile.py`

#### EPI-RTE-markdown-repair
Label: Unknown-link cleanup

Part of: [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run)

SRC-1, `src/synto/pipeline/compile.py`: _write_draft calls _strip_unknown_wikilinks before retention. Deterministic example: with known_titles=["Known"] and no stem map, input "A causes [[Missing]]." becomes "A causes Missing." The predicate keeps known/source links; otherwise display or target text is returned. This scoped non-ampliative reshaping removes a navigation assertion but neither tests nor retracts the causal assertion. The example is a code deduction, not target execution; other cleanup steps are not assumed globally semantics-preserving.

- Immediate return: Rewritten Markdown body.
- Later read-back: Draft/published text and later query/export receive the cleaned body.
- Delegated visibility: Code sees generated text, resolvable titles and source targets.
- Selection predicate: Unknown target outside source prefix and known names.
- Invalidation or expiry: Recomputed on draft writing; original model text not guaranteed separately retained.
- Activation or effect: Removes broken-link syntax while preserving ordinary display text.
- Evidence limits: No truth evaluator or observed generation; semantic safety of every cleanup helper unassessed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if target.lower().startswith("sources/") or target.lower() in known:
>     return match.group(0)
> return display or f"{target}{fragment}"
> --- `src/synto/pipeline/compile.py`

> body = _strip_unknown_wikilinks(body, (resolvable_titles or []) + source_targets, stem_to_title)
> --- `src/synto/pipeline/compile.py`

#### EPI-RTE-synthesis-guard
Label: Synthesis safety checks

Part of: [RT-RTE-query-answer](runtime.md#rt-rte-query-answer)

SRC-1, `src/synto/pipeline/query.py`: Python rejects synthesis sources that resolve to synthesis pages, recognizes duplicate normalized questions, and refuses in-place overwrite of hash-detected edits. The caller selects duplicate strategy; code can veto; humans can edit files but no factual reviewer is required. These checks target source-chain policy, identity and edit preservation, not answer truth. Keep-existing may return an old file before chain checks. Open question-saving mode; no reference-answer oracle.

- Immediate return: Save eligibility, existing-file return or exception.
- Later read-back: Source paths/hashes and saved answer are retained only through save route; existing file can remain.
- Delegated visibility: Code reads resolved source types, question hash and existing file/body hash.
- Selection predicate: Duplicate strategy, synthesis source exclusion, content hash conflict.
- Invalidation or expiry: New question/source resolution per call; manual edits block update rather than validate truth.
- Activation or effect: Can prevent write or keep existing; no factual authority is granted.
- Evidence limits: No executed save or recovery trace; hash consistency does not show grounding.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if any(_is_synthesis_source(config, db, path) for path in resolved_sources):
>     raise SynthesisChainError("Synthesis sources cannot include another synthesis page")
> --- `src/synto/pipeline/query.py`

> if existing.content_hash and existing.content_hash != _body_hash(existing_body):
> --- `src/synto/pipeline/query.py`

#### EPI-RTE-answer-retention
Label: Saved answer admission

Part of: [RT-RTE-query-answer](runtime.md#rt-rte-query-answer)

SRC-1, `src/synto/pipeline/query.py` and `src/synto/indexer.py`: caller flags admit model-written answer text through two distinct paths. Ordinary Q&A is written to `wiki/queries/` with published metadata but no article DB registration in `_save_query`; refreshing the index does not enumerate that tree. Synthesis is registered as an article with kind synthesis and enters the generated index, which shows up to 25 newest synthesis entries; it uses separate guards. Both forms are filesystem/export-accessible (see [RT-RTE-pack-export](runtime.md#rt-rte-pack-export)). `_find_page_unchecked` recursively scans wiki Markdown frontmatter titles, so an unindexed Q&A can still load if its title reaches the resolver. The registration/index distinction agrees with the supplied peer [MEM-OBJ-synthesis](memory.md#mem-obj-synthesis) and [MEM-OBJ-index](memory.md#mem-obj-index). Flags authorize automatic content admission, not per-content review; the generating model proposes, code writes, caller can decline saving. Recovery uses keep-existing/update/suffix strategies and edit guards rather than draft rejection. Prompt guidance requests answering from wiki text. No inspected evidence-consuming factual acceptance decision precedes saving.

- Immediate return: Path/resolution or save exception.
- Later read-back: Registered synthesis enters later index selection, subject to the 25-entry catalogue cap. Ordinary Q&A files are not automatically enumerated into that index; they remain filesystem/export-accessible and can be loaded by the recursive title resolver when a matching title is supplied. No actual later consumption was observed.
- Delegated visibility: Stored answer, selected page names, synthesis source hashes; selected names may exceed loaded bodies.
- Selection predicate: save/synthesize flags and synthesis guard outcomes.
- Invalidation or expiry: Question deduplication and source hashes track identity/freshness, not endorsement; no factual expiry.
- Activation or effect: Saves both forms without the draft publication gate; synthesis changes indexed answer context, while ordinary Q&A changes filesystem/export availability and remains title-resolvable without automatic index admission.
- Evidence limits: No saved answer instance; status published is operational metadata.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> status="published",
> kind="synthesis",
> question_hash=question_hash,
> --- `src/synto/pipeline/query.py`

> "Synthesis pages capture prior answers; consider them when relevant "
> "but never prefer them over a fresh concept page. "
> --- `src/synto/pipeline/query.py`

> "status": "published",
> }
> write_note(path, meta, answer)
> --- `src/synto/pipeline/query.py`

> write_note(path, meta, answer)
> append_log(config, f"query | {question[:60]}")
> generate_index(config, db)
> return path
> --- `src/synto/pipeline/query.py`

> visible_entries = synthesis_entries[:25]
> --- `src/synto/indexer.py`

> for md in config.wiki_dir.rglob("*.md"):
> --- `src/synto/pipeline/query.py`

#### EPI-RTE-offline-evaluation
Label: Offline structural checks

Part of: [RT-RTE-compare-eval](runtime.md#rt-rte-compare-eval)

SRC-1, `src/synto/pipeline/eval.py`: deterministic evaluator compares expected concept existence, nonempty sources metadata, INDEX schema and link resolution. Fixture author supplies expected concepts, not an answer oracle for truth; expected_contains is loaded but term_recall is skipped. Operating mode is offline structural evaluation; no production-policy successor selection is implemented here. A concrete deduction: any article with sources=["missing.md"] counts in citation coverage because only list type and length are checked; its body and the source contents are not compared. This does not establish actual corpus behavior.

- Immediate return: EvalResult and text/JSON metric report.
- Later read-back: Reports/comparison artifacts can be inspected later; no inspected automatic installation consumer.
- Delegated visibility: Reader supplies published article frontmatter/body and index; fixture supplies expected concepts.
- Selection predicate: All listed articles and fixture concepts; missing metrics skipped in aggregate.
- Invalidation or expiry: A later invocation recomputes; report itself confers no expiry or acceptance.
- Activation or effect: Reporting force; no universal publication veto or knowledge rewrite.
- Evidence limits: No observed scores, answer quality or causal component effect; live mode unimplemented.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> sources = article.frontmatter.get("sources", [])
> if isinstance(sources, list) and len(sources) > 0:
>     with_sources += 1
> --- `src/synto/pipeline/eval.py`

> term_recall = None
> --- `src/synto/pipeline/eval.py`

> "metrics_skipped": ["term_recall"],
> --- `src/synto/pipeline/eval.py`

#### EPI-RTE-verbatim-source
Label: Verbatim segment delivery

Part of: [RT-RTE-mcp-answer](runtime.md#rt-rte-mcp-answer)

SRC-1, `src/synto/serve.py`: a separate primitive in the MCP container looks up a source segment, checks license permission and returns stored text/identity/hash with truncation status. This is not the synthesized answer subroute. ID and policy checks decide disclosure; no evaluator decides original source truth. Source search ranks by BM25 and concept passages use retained occurrence bindings; ranking does not confer epistemic endorsement.

- Immediate return: Dictionary with body, source identity/hash and truncation flag, or tool error.
- Later read-back: Previously imported and persisted source segments reach later MCP client invocations as stored text, with optional truncation. This is a read-only memory read-back, not a Synto answer-saving write; downstream model use remains host-dependent and unobserved. See the earlier import object [MEM-OBJ-source-documents](memory.md#mem-obj-source-documents) and later delivery [MEM-RTE-source-passages](memory.md#mem-rte-source-passages).
- Delegated visibility: External caller receives stored paragraph, optionally clipped with ellipsis; models need not generate it.
- Selection predicate: Requested segment ID, existence and source license gate; search/passage alternatives select differently.
- Invalidation or expiry: Source/license policy changes govern availability; runtime notes process-cached legacy mode.
- Activation or effect: Permits or blocks source disclosure; gives a consumer attributed source text.
- Evidence limits: Extraction-to-original fidelity not fully inspected; no external reader compliance or truth evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> body: str = row["text"]
> truncated = False
> --- `src/synto/serve.py`

> body = body[:cap] + "…"
> truncated = True
> --- `src/synto/serve.py`

#### EPI-RTE-state-recovery
Label: Undo and clean state

Distinct identity: no supplied route isolates this operation; comparisons are stated below.

SRC-1, `src/synto/cli.py`: distinct recovery/destructive operations absent from the supplied route inventory, not duplicates of [RT-RTE-concept-curation](runtime.md#rt-rte-concept-curation). An operator requests Git revert or clean. Undo refuses identity-op batches unless forced because Git cannot reverse DB mutations; clean preserves an INDEX rebuild seed then removes DB/wiki while keeping raw notes. Human invocation/confirmation admits withdrawal; software guards known inconsistency. These are operational recovery paths, not truth-directed rejection or complete rollback.

- Immediate return: Reverted commit messages, refusal, or deleted-state report.
- Later read-back: Reverted files/remaining DB or rebuild seed affect future ingest/compile.
- Delegated visibility: Operator sees warnings and selected targets; no model judgment is involved.
- Selection predicate: Last N auto-commits; identity-op guard unless force; configured DB/wiki paths for clean.
- Invalidation or expiry: Changes local availability immediately; raw notes/rebuild seed persist.
- Activation or effect: Withdraws local generated material or reverts files; DB may remain divergent after undo.
- Evidence limits: No observed rollback; cannot revoke already exported packs or external answers.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if identity_commits and not force:
> --- `src/synto/cli.py`

> seed_path = generate_index_json(config, db)
> --- `src/synto/cli.py`

> targets = [
>     ("state DB", config.state_db_path),
>     ("wiki/", config.wiki_dir),
> ]
> --- `src/synto/cli.py`

### Claims

#### EPI-CLM-wiki-synthesis
Label: Synthesized current wiki

Distinct identity: no claims are declared in the supplied runtime. SRC-1, `README.md`, doctrine/design: the public rationale describes synthesis, cross-reference and currency; this is not observed knowledge quality. Compare [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run) and [RT-RTE-query-answer](runtime.md#rt-rte-query-answer).

> a personal knowledge base where the model doesn't just store what you tell it — it synthesizes, cross-references, and keeps everything current. You add raw material; it does the bookkeeping.
> --- `README.md`

#### EPI-CLM-quality-evaluation
Label: Offline quality evaluation

Distinct identity: no supplied claim counterpart. SRC-1, `README.md`, doctrine/design. Public “citation support” is bounded by the inspected metadata check, not source-entailment assessment. README also explicitly calls the mechanism offline structural evaluation, so the limited implementation is consistent with that narrower characterization. See [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation).

> **Quality evaluation.** `synto eval` scores your wiki offline: concept coverage, citation support, link resolution, `INDEX.json` validity. Run it before a pack export or in CI.
> --- `README.md`

> - `synto eval` — offline structural evaluation (coverage, citation support, link resolution)
> --- `README.md`

#### EPI-CLM-staged-review
Label: Confidence and staged lifecycle

Distinct identity: no supplied claim counterpart. SRC-1, `README.md`, doctrine/design. The three-state wording must not be read as enforced sequential verification; the same text allows an explicit staged step rather than requiring it. See [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication) and [EPI-RTE-confidence-score](#epi-rte-confidence-score).

> **Confidence scores.** Each compiled draft gets a confidence score (0–1). Approve selectively or set a threshold — drafts below it stay in `.drafts/` for manual review.
> --- `README.md`

> **Three-state lifecycle.** Drafts move through `draft` → `verified` → `published`.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; new route records state their distinct consumers, channels, forces and horizons. The supplied [RT-BAP-rejection-guidance](runtime.md#rt-bap-rejection-guidance) and [RT-BAP-pack-guidance](runtime.md#rt-bap-pack-guidance) remain canonical for those paths.
