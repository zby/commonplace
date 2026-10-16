---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Synto memory mechanisms: source-derived wiki text, identity constraints, restart checkpoints, response reuse and later vault/pack consumers."
run-id: AAS-2026-10-15-synto-eabcdcce3da2-01
source-identity: https://github.com/kytmanov/synto
reviewed-boundary: "91ac6a3681df0552b6c9baef159439c7ebd780c9"
---

# Synto memory report

## Boundary and evidence

The memory boundary includes the shipped import, ingestion, compilation, review, identity curation, cleanup, query saving, indexing, MCP, export and evaluation paths. Synto retains source-derived knowledge and routing constraints in Markdown, JSON and SQLite. It also retains intermediate analysis for restart and model responses for reuse. These are different mechanisms, not one undifferentiated memory store.

The frozen source is SRC-1 at `91ac6a3681df0552b6c9baef159439c7ebd780c9`; its identity and source register are in [boundary](boundary.md#source-register). HEAD and clean status were rechecked. All new findings below are implementation or doctrine/design findings. No target, test, example, model or service was executed. There is no supplied observed-run evidence.

The coverage table distinguishes direct source inspection in this job from supplied runtime findings. Every source path below is under SRC-1. Provider-held weights and any injected RAG store remain opaque; an exposed write does not establish a deployed retrieval route. External editors and agent hosts are excluded, while the instructions and handlers Synto supplies to them are included. These exclusions prevent conclusions about actual edits, instruction loading and task benefit, not about the shipped interfaces.

| Entry point or operation | Source path and inspection basis | Coverage and limit |
|---|---|---|
| `add`, direct raw notes, browser/watch ingress | `src/synto/cli.py`, `src/synto/pipeline/ingest.py`; direct reads of import and ingest; watcher supplied | [MEM-OBJ-source-documents](#mem-obj-source-documents), [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run). Import dispatch inspected; PDF extractor internals not independently audited here, so exact extraction fidelity is not assessed. |
| Fast analysis, candidate normalization, named-reference items, summaries | `src/synto/pipeline/ingest.py`; direct reads | [MEM-OBJ-raw-notes](#mem-obj-raw-notes), [MEM-OBJ-source-summaries](#mem-obj-source-summaries), [MEM-OBJ-concept-entities](#mem-obj-concept-entities). Item extraction helpers not read in full; their detailed admission semantics remain uninspected. |
| Source-type instructions and concept-writing instructions | `src/synto/pipeline/prompts/notes.md`, `paper.md`, `api_docs.md`, `corp_docs.md`, `sql.md`, `textbook.md`, `web_article.md` in that directory; `src/synto/pipeline/compile.py`; direct reads | All seven prompt bodies inspected. They request source-faithful extraction with type-specific emphasis; wording is not evidence of compliance. Compiler guidance and rejection reuse annotated below. |
| Chunk restart and single-call alternative | `src/synto/pipeline/ingest.py`; direct reads | [MEM-OBJ-ingest-chunks](#mem-obj-ingest-chunks), [MEM-RTE-checkpoint-resume](#mem-rte-checkpoint-resume). Both segment-aligned units and fixed-size note chunks covered. |
| Optional chunk/embed write | `src/synto/pipeline/ingest.py`; direct read; [RT-CMP-embed](runtime.md#rt-cmp-embed) | [MEM-OBJ-rag-embeddings](#mem-obj-rag-embeddings). Injected store persistence and consumers unresolved; no claim of ordinary vector retrieval. |
| Concept compile and CLI `--legacy` plan/write alternative | `src/synto/pipeline/compile.py`; direct scoped reads plus supplied runtime | [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run) annotation. Legacy planning uses first 500 characters of source bodies, not stored analysis summaries. Shared source gathering and draft writing remain distinct from admission. |
| Approve, verify, reject, review | `src/synto/pipeline/compile.py`, `src/synto/state.py`, `src/synto/cli.py`; direct rejection/state reads plus supplied publication findings | [MEM-OBJ-rejections](#mem-obj-rejections), [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication) annotation. Human review and automatic publication are alternatives. |
| Rename/merge/split/unmerge and alias add/remove/move/keep | `src/synto/cli.py`, `src/synto/state.py`, `src/synto/pipeline/maintain.py`; dispatch search, alias-state reads, supplied curation findings | [MEM-OBJ-concept-entities](#mem-obj-concept-entities), [RT-RTE-concept-curation](runtime.md#rt-rte-concept-curation) annotation. Not every inverse implementation inspected; universal rollback is not claimed. |
| Lint/fix/stubs and retired-file relocation | `src/synto/pipeline/maintain.py`, `src/synto/cli.py`; scoped search and supplied runtime | [RT-RTE-concept-curation](runtime.md#rt-rte-concept-curation), [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run). Detailed lint predicates uninspected here; structural maintenance is not treated as a factual oracle. |
| `clean`, `undo`, cache clearing, metrics clearing | `src/synto/cli.py`, `src/synto/cache.py`, `src/synto/metrics.py`; direct reads/search | [MEM-RTE-identity-rebuild](#mem-rte-identity-rebuild), [MEM-RTE-response-reuse](#mem-rte-response-reuse), [MEM-OBJ-metric-events](#mem-obj-metric-events). Files, DB and distributed packs have different withdrawal horizons. |
| Markdown index, JSON rebuild seed, pack metadata | `src/synto/indexer.py`, `src/synto/pack_export.py`; direct reads | [MEM-OBJ-index](#mem-obj-index); [RT-RTE-pack-export](runtime.md#rt-rte-pack-export) annotation. Markdown routing index is not the JSON seed. |
| Question routing, graph expansion, answer save/synthesis | `src/synto/pipeline/query.py`; direct reads | [RT-RTE-query-answer](runtime.md#rt-rte-query-answer) annotation, [MEM-OBJ-synthesis](#mem-obj-synthesis), [MEM-RTE-synthesis-save](#mem-rte-synthesis-save). Ordinary saved Q&A has no established automatic selector-index admission. |
| MCP article, source, lineage and answer tools | `src/synto/serve.py`, `src/synto/readers.py`; direct reads of handlers/readers plus supplied answer findings | [MEM-RTE-source-passages](#mem-rte-source-passages); [RT-RTE-mcp-answer](runtime.md#rt-rte-mcp-answer) annotation. Article visibility and verbatim-source licenses are separate policies. |
| Relation extraction, candidates, evidence and optional graph read | `src/synto/pipeline/ingest.py`, `src/synto/pipeline/query.py`, `src/synto/state.py`, `src/synto/pack_export.py`; direct ingestion/query reads and scoped searches | [MEM-OBJ-relations](#mem-obj-relations). Relation upsert aggregation details not fully audited; no exact evidence-retraction guarantee. |
| Metrics/report, doctor backlog and compare/eval reports | `src/synto/metrics.py`, `src/synto/cli.py`; direct reads; `src/synto/pipeline/eval.py`, `src/synto/compare/runner.py` supplied | [MEM-OBJ-metric-events](#mem-obj-metric-events), [RT-RTE-compare-eval](runtime.md#rt-rte-compare-eval). Reports reach operators, not an established automatic production-update consumer. |
| Response-cache clients | `src/synto/cache.py`, `src/synto/openai_compat_client.py`; direct reads; `src/synto/ollama_client.py`, `src/synto/anthropic_compat_client.py` scoped wiring searches | [MEM-OBJ-llm-cache](#mem-obj-llm-cache), [MEM-RTE-response-reuse](#mem-rte-response-reuse). Exact OpenAI-compatible key behavior established; other adapters' full parameter equivalence not assessed. |

## Core ideas

1. **Knowledge production and admission are separate.** Fast analysis produces summaries and relationships; heavy compilation produces drafts. Source summaries are written directly as published pages. Saved synthesis is another direct knowledge-admission route. Thus the draft-review gate does not cover all knowledge a later model can receive. See [MEM-OBJ-source-summaries](#mem-obj-source-summaries), [MEM-RTE-synthesis-save](#mem-rte-synthesis-save) and [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication).
2. **Identity state is executable routing memory.** Human-blessed aliases and denials have symbolic consequences at subsequent normalization, unlike the prose article's model-interpreted informational authority. The JSON seed preserves selected identity decisions across DB rebuilding. See [MEM-OBJ-concept-entities](#mem-obj-concept-entities), [MEM-RTE-identity-rebuild](#mem-rte-identity-rebuild).
3. **Restart memory and inference reuse are not reasoning summaries.** Chunk checkpoints store typed analysis results; response cache entries store returned strings. Neither establishes host conversation compaction or retained private reasoning. Their later consumers are merger/parser code before downstream writing, not necessarily another model reading the same strings as instructions. See [MEM-RTE-checkpoint-resume](#mem-rte-checkpoint-resume), [MEM-RTE-response-reuse](#mem-rte-response-reuse).
4. **Context is reconstructed and budgeted at each call.** Source preparation strips media/OCR material in memory, concept hints are capped, compilation shares a source budget, and queries select a few page slices. The source remains reloadable, but pointers in the model window do not automatically reload it. These are separate call frames returning structured values, not an implemented general sub-agent stack or conversational compactor. See annotations on [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run) and [RT-RTE-query-answer](runtime.md#rt-rte-query-answer).
5. **Provenance labels do not establish epistemic warrant.** Concept occurrence confidence can be a fixed value assigned by code, article confidence is a source-count/quality heuristic, and relation evidence is a model-returned field. A later consumer may receive useful lineage without receiving a verified reason that the generated claim is true. See [MEM-OBJ-relations](#mem-obj-relations) and the compiler annotation.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-source-documents
Label: Source documents and segments

These are acquisition objects, distinct from the derived outputs of [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run), whose ordinary account begins with raw Markdown. Original bytes are copied to `.synto/sources/<source_id>/original<ext>`. SQLite `source_documents` holds identity, hash, origin URI and policy metadata; source segments hold extracted text with ordinal/identity metadata. Original PDF bytes are opaque binary here, while extracted text is natural-language content; IDs, hashes, offsets and license fields are symbolic access/lineage data. PDF extraction is called by `add`; non-PDF input is assembled into raw Markdown without establishing equivalent paragraph-segment indexing. Later ingestion and verbatim-source tools consume different parts (SRC-1, `src/synto/cli.py`, `src/synto/pipeline/ingest.py`, `src/synto/serve.py`).

The human selects an import file and can force replacement; software copies/extracts/persists it without per-segment human approval. Import failure cleans newly created import data and files. Reimport is not demonstrated to retract all previously generated articles or distributed packs.

> The original is copied to
> .synto/sources/<source_id>/ and recorded in the state database.  For PDF
> files, segments are extracted immediately.
> --- `src/synto/cli.py`

#### MEM-OBJ-raw-notes
Label: Raw notes and analysis metadata
Part of: [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run)

This object is the input/analysis-state part of that route, not a duplicate route. `raw/` Markdown contains source text, possibly manually supplied or assembled from imported segments. Natural-language prose is consumed by models; source-type/frontmatter fields are symbolic dispatch inputs. SQLite `raw_notes` retains summary, quality, language, body hash, prompt version and status. The summary is model-derived natural language; status/hash fields have deterministic skip/retry effects. Physical storage in one DB does not give every field the same authority. Later compilers consume source text and source metadata, ingestion consumes prior concept hints, and indexing exposes derived material (SRC-1, `src/synto/pipeline/ingest.py`).

> # Update state DB (raw files stay immutable — metadata lives in state.db only)
> --- `src/synto/pipeline/ingest.py`

That comment describes ingestion's handling of existing raw files, not an invariant against import replacement, external editing or cleanup. Starting ingestion authorizes automatic analysis and candidate filtering, not human approval of each generated summary or concept.

#### MEM-OBJ-source-summaries
Label: Source summary pages
Part of: [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run)

`wiki/sources/<sanitized title>.md` is generated from the analysis summary, canonical concept links and source/bibliographic metadata, without another model call. The natural-language summary is derived knowledge, not raw source text or a transcript. Its YAML status/path/quality fields and link targets provide symbolic metadata; bibliographic display is not independent verification. It is written directly with published status, outside draft approval, and is later listed by the Markdown index, loadable by query and copied by export. Re-ingestion can rewrite the title-derived path; this path scheme is not a content-addressed version history. No per-summary manual-edit gate appears in this writer (SRC-1, `src/synto/pipeline/ingest.py`; compare [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication)).

> Generate wiki/sources/{Title}.md from AnalysisResult. No extra LLM call.
> --- `src/synto/pipeline/ingest.py`

#### MEM-OBJ-concept-entities
Label: Concept entities, labels and denials

Unlike the mutation route [RT-RTE-concept-curation](runtime.md#rt-rte-concept-curation), this record identifies its retained symbolic objects: SQLite concept entities, preferred labels, aliases with provenance, source links, occurrences, identity log and alias-denial rows. Labels are readable text, but normalization treats their keys and provenance by fixed rules; they are not prose instructions. Ingestion automatically proposes and filters concepts/weak aliases; explicit human commands can bless or deny aliases and change identities. Curation provenance is distinct from model authorship and from software executing the writes. Starting `run` does not human-approve each identity assignment (SRC-1, `src/synto/pipeline/ingest.py`, `src/synto/state.py`, `src/synto/cli.py`).

Denied aliases constrain subsequent admission. Re-adding clears a denial. Blessed aliases pre-fold extracted candidates; weak aliases do not get that same pre-fold authority. The JSON seed retains selected IDs, source allocations, identity log, blessed aliases and denials for rebuild. It is not a complete copy of all SQLite behavior state. Later ingestion normalization, query alias expansion, readers and export use these retained identities.

> Detach ALIAS from concept_name and record a denial so re-ingest can't reattach it.
> --- `src/synto/state.py`

> # Only BLESSED aliases pre-fold a candidate to its canonical here; a weak (LLM-guessed) alias
> # surface re-extracted as a concept must reach _normalize_concepts and mint (order-independent).
> --- `src/synto/pipeline/ingest.py`

#### MEM-OBJ-relations
Label: Relations, evidence and candidates
Part of: [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run)

This is the optional graph-producing part, not the overall pipeline route. It separates SQLite accepted relations/edges, their evidence strings and all raw model-returned relation candidates. Predicate/endpoints/confidence are symbolic graph data; evidence strings are natural-language payloads. Raw candidates include rows not admitted as edges because endpoints cannot resolve. Neither their retention nor a field named evidence verifies a quote or a relation. Optional extraction runs a fast-model pass over packed source units; a tracked unit's evidence pointer uses its first segment, not every paragraph. Plain notes receive note/chunk pseudo-identifiers (SRC-1, `src/synto/pipeline/ingest.py`).

Concept occurrences are a different association: chunk-extracted concepts are linked to every segment in the unit with code-assigned confidence 1.0. This supports retrieval of candidate passages, not a demonstrated paragraph-level entailment score. Re-ingestion replaces source occurrence rows and clears source relation artifacts before extraction. Accepted graph neighbors can affect later query expansion; graph export delivers edges to external consumers. Raw candidates are an audit surface, not established query context (SRC-1, `src/synto/pipeline/ingest.py`, `src/synto/pipeline/query.py`, `src/synto/pack_export.py`).

> # there is no ordering side-effect. Candidates with an unresolvable endpoint are NOT
> # upserted; relation_candidates keeps every raw LLM row as the hallucination audit
> # trail. A qualified homonym like "Mercury (planet)" still won't match a bare
> --- `src/synto/pipeline/ingest.py`

> db.upsert_concept_occurrences([occ(name=c, confidence=1.0) for c in sorted(concepts)], sid)
> --- `src/synto/pipeline/ingest.py`

#### MEM-OBJ-ingest-chunks
Label: Ingest chunk checkpoints
Part of: [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run)

SQLite `ingest_chunks` retains per-unit serialized `AnalysisResult` JSON, keyed by source path, checkpoint hash, chunk index/count/size and schema. This is inspectable structured output with natural-language summaries and symbolic fields, not opaque model hidden state or an agent-session transcript. Lineage starts in note text or imported segments; interrupted analysis outputs can survive to a later invocation. [MEM-RTE-checkpoint-resume](#mem-rte-checkpoint-resume) supplies the consumer and invalidation mechanism (SRC-1, `src/synto/pipeline/ingest.py`, `src/synto/state.py`).

#### MEM-OBJ-llm-cache
Label: LLM response cache

SQLite `llm_cache` retains response strings plus model/key/timestamps/hit counts. Responses may encode structured results; timestamps and counts are access metadata, not the remembered answer content. This object is distinct from the model endpoints [RT-CMP-fast](runtime.md#rt-cmp-fast) and [RT-CMP-heavy](runtime.md#rt-cmp-heavy): it does not change their weights. It spans several runtime routes rather than being part of exactly one. The key is an exact SHA256 over namespace, model name and sorted-message JSON, despite the state module's historical label “semantic cache.” No semantic similarity lookup occurs in this class. The OpenAI-compatible caller looks up and stores returned content, not provider reasoning state (SRC-1, `src/synto/cache.py`, `src/synto/openai_compat_client.py`).

> data = namespace + "\x00" + model + json.dumps(messages, sort_keys=True)
> return hashlib.sha256(data.encode()).hexdigest()
> --- `src/synto/cache.py`

#### MEM-OBJ-rejections
Label: Rejection feedback and rejected bodies
Part of: [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication)

SQLite rejection records retain feedback, rejected body and time keyed by concept name; blocked-concept state gives separate symbolic scheduling authority. The human-supplied reason and body are natural-language content. A nonempty feedback string is required to add the record: rejecting without feedback still deletes a draft and resets its source compilation state but does not necessarily preserve the rejected body here. The compiler loads the latest three records but injects feedback strings only, deduplicated, not the rejected-body text. Human review can inspect rejected bodies via rejection diffs. Thus reasons are retained and later delivered, but the writer does not receive the entire criticism episode or any guaranteed causal diagnosis (SRC-1, `src/synto/pipeline/compile.py`, `src/synto/state.py`, `src/synto/cli.py`; [RT-BAP-rejection-guidance](runtime.md#rt-bap-rejection-guidance)).

> if feedback:
>     db.add_rejection(title, feedback, body=draft_body)
> --- `src/synto/pipeline/compile.py`

#### MEM-OBJ-index
Label: Routing index and identity seed

This record spans the knowledge-production and export routes rather than duplicating either [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run) or [RT-RTE-pack-export](runtime.md#rt-rte-pack-export). `wiki/index.md` is a generated catalogue of concepts, source summaries and up to 25 newest synthesis entries. Although its links have symbolic resolution, the query selector reads this catalogue as natural-language model input. It includes filesystem fallbacks for source pages and wiki-root pages absent from the DB. Admission to this selector is therefore not solely a published DB row check (SRC-1, `src/synto/indexer.py`, `src/synto/pipeline/query.py`).

`.synto/INDEX.json` is a separate symbolic seed/index: IDs, identity log, blessed aliases, denials and source-concept allocation support rebuilding. Its article entries use `summary: None` and `confidence: "high"` literals; those values are not an assessment of article truth. Exported `index/INDEX.json` is another generated representation: it uses reader references, including their first-paragraph summary. Do not transfer the seed's literal values to the pack, or confuse either with the Markdown selector input (SRC-1, `src/synto/indexer.py`, `src/synto/readers.py`, `src/synto/pack_export.py`).

> visible_entries = synthesis_entries[:25]
> --- `src/synto/indexer.py`

> "identity_log": db.list_identity_log(),
> "entity_aliases": db.list_blessed_aliases(),
> "alias_denials": db.list_alias_denials(),
> --- `src/synto/indexer.py`

#### MEM-OBJ-synthesis
Label: Saved synthesis and ordinary Q&A
Part of: [RT-RTE-query-answer](runtime.md#rt-rte-query-answer)

The retained answer part comprises two distinct admissions. `wiki/queries/` stores ordinary generated Q&A as Markdown with question-derived title and selected-page metadata, without a synthesis article DB row in `_save_query`. `wiki/synthesis/` stores model-derived natural-language answers with question hash, body hash, source-page paths and source-body hashes in files and DB. These symbolic fields manage identity/overwrite/provenance; they do not verify answers. Source-page names are the selector's output and can exceed successfully loaded bodies. Neither object is a verbatim source nor a record of the model's private reasoning. Export copies both trees; synthesis enters the Markdown index and later query context, while `_save_query` refreshing the index does not itself add Q&A entries to that index (SRC-1, `src/synto/pipeline/query.py`, `src/synto/indexer.py`, `src/synto/pack_export.py`).

#### MEM-OBJ-rag-embeddings
Label: Optional RAG embeddings
Part of: [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run)

When an API caller supplies `rag`, ingestion chunks preprocessed body text, invokes [RT-CMP-embed](runtime.md#rt-cmp-embed), then passes chunks, dense numerical embeddings and source/type metadata to `rag.add_document`. Dense vectors are distributed numerical representations; their source text and IDs remain separate parts. Exact vector provenance depends on the configured endpoint; stored substrate, admission policy, replacement semantics, initialization and later retrieval consumer of the injected object are uninspected. This establishes a write capability, not an ordinary deployed memory route or a known vector read-back budget. It does not replace known Markdown/SQLite transformations with a system-wide unknown (SRC-1, `src/synto/pipeline/ingest.py`).

> rag.add_document(
>     doc_id=rel_path,
>     chunks=chunks,
>     embeddings=embeddings,
>     metadata={"source": rel_path, "type": "raw"},
> )
> --- `src/synto/pipeline/ingest.py`

#### MEM-OBJ-metric-events
Label: Metric events, audit and reports

This spans [RT-RTE-mcp-answer](runtime.md#rt-rte-mcp-answer) and [RT-RTE-compare-eval](runtime.md#rt-rte-compare-eval), not a duplicate of either. SQLite metric events/rollups retain symbolic call outcomes, counts, timing and optional detailed metadata. MCP auditing can retain hashed or detailed argument/label data. These are activity traces, not automatically distilled instructions. `doctor --backlog` reads audit rows to display zero-result demand, weak single-source queries and tool mix. A human can use those diagnostics, but no inspected consumer automatically turns that backlog into knowledge edits (SRC-1, `src/synto/metrics.py`, `src/synto/serve.py`, `src/synto/cli.py`).

Metrics retention removes detailed events after a configured horizon and rollups after four times that horizon; size-cap maintenance trims event rows. Explicit report clearing is a separate operator command. Compare artifacts are separately retained report files, and deletion of temporary contestant vaults does not imply deleting the reports. Their later reader is an examining operator, not an established automatic model-selection installer (SRC-1, `src/synto/metrics.py`, `src/synto/cli.py`; supplied [RT-RTE-compare-eval](runtime.md#rt-rte-compare-eval)).

> Informational only — never affects exit status. Reads existing audit rows
> in `metric_events`; degrades gracefully when audit_detailed is off (labels
> show as <hash:8>).
> --- `src/synto/cli.py`

### Routes

#### MEM-RTE-checkpoint-resume
Label: Checkpoint reuse across ingestion attempts
Part of: [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run)

Python selects retained per-chunk analysis after an ingest trigger, validates JSON, reconstructs the result slots, analyzes missing chunks, merges all results and removes the matching checkpoints after merge. It is automatic recovery admission, not human approval of each recovered field. There is no expected-answer oracle; mode is interrupted-work resumption. Force purges checkpoints; corrupt entries are reanalyzed. Short notes take a direct, non-checkpointed call alternative. Source-backed inputs instead use segment-aligned units (SRC-1, `src/synto/pipeline/ingest.py`, `src/synto/state.py`).

- Immediate return: Merged AnalysisResult to ingestion.
- Later read-back: Persisted result JSON from an interrupted prior attempt feeds merger code, then current DB/summary/concept outputs and later compilation.
- Delegated visibility: Missing units go to fast-model analysis; resumed units' validated results go to the merger and attribution mapping rather than being resent as full source context.
- Selection predicate: Source path, checkpoint hash, chunk count/size and schema; hash includes content, prompt policy/type fingerprint, fast model/connection and concept contexts.
- Invalidation or expiry: Force purges; changed hash purges stale versions; corrupt JSON is ignored; matching checkpoints are deleted after successful merge. No time expiry established.
- Activation or effect: Valid cached results bypass those unit calls and contribute directly to derived output; content quality and successful operation remain unobserved.
- Evidence limits: Source wiring only; no crash/restart trace. Chunk boundaries and configuration remain preconditions of reuse.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> results = [result for result in chunk_results if result is not None]
> merged = _merge_chunk_results(results)
> db.delete_ingest_chunks(rel_path, checkpoint_hash, len(chunks), chunk_size)
> return merged
> --- `src/synto/pipeline/ingest.py`

#### MEM-RTE-response-reuse
Label: Response lookup before inference

This is a shared client-layer route beneath the supplied model-call routes, with no single supplied parent. Clients propose no semantic revision here: code stores successful returned response text and later exact-key lookups can return it before provider invocation. Software admits the cache write without per-response human review or a factual oracle. OpenAI-compatible requests use model/messages/namespace for lookup; generation options such as temperature and output cap are not in that key. Thus a changed request option does not necessarily cause fresh inference on this adapter (SRC-1, `src/synto/cache.py`, `src/synto/openai_compat_client.py`; nearest supplied [RT-RTE-query-answer](runtime.md#rt-rte-query-answer)).

- Immediate return: Cached content string or cache miss followed by inference.
- Later read-back: Subsequent calls can reuse a prior response across invocations while the DB entry remains; structured callers then parse that string as the response.
- Delegated visibility: Reuse returns stored output to calling code, not full prior input/output history to a fresh model invocation.
- Selection predicate: Exact digest of namespace, model string and sorted-message JSON; not embedding similarity or topical relevance.
- Invalidation or expiry: Explicit `maintain --clear-cache`, optionally older than N days; replacement by same key. No automatic maximum age in `get`.
- Activation or effect: A hit bypasses inference; this establishes deterministic control flow, not demonstrated improved answer quality or speed.
- Evidence limits: No observed hits. Mutable model aliases and omitted generation options limit equivalence with a new provider call; other adapters were only searched for wiring.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if cached is not None:
>     self._last_stats = {"latency_ms": 0, "cache_hit": True}
>     return cached
> --- `src/synto/openai_compat_client.py`

#### MEM-RTE-identity-rebuild
Label: Clean and rebuild retained identities

This crosses cleanup and ingestion and is not identical to the live identity-mutation route [RT-RTE-concept-curation](runtime.md#rt-rte-concept-curation). The operator selects `clean` and confirms or uses `--yes`; code snapshots selected read-only DB content to JSON before deleting the DB and wiki, preserves raw notes, and recreates empty directories. A later ingest restores seed identities where appropriate. The seed's preexisting provenance supplies guidance; current code, not a human per restored row, admits reconstruction. It is recovery, not an experiment with an answer oracle (SRC-1, `src/synto/cli.py`, `src/synto/indexer.py`, `src/synto/pipeline/ingest.py`).

- Immediate return: Cleaned vault with raw notes and preserved rebuild seed; later ingest restores selected identities and regenerates derived content.
- Later read-back: JSON IDs, identity log, denials and blessed aliases reach restore code, then later normalization and routing.
- Delegated visibility: Restore code receives serialized identity state; fast analysis receives resulting canonical-name/alias hints, not every historical identity operation.
- Selection predicate: Seed entries from source_concepts and articles; restore respects existing DB entities; denial restoration precedes blessed-alias restoration.
- Invalidation or expiry: Missing/invalid JSON is skipped; absent seed allows reminting by label. Clean is destructive for other DB/wiki content, not complete rollback.
- Activation or effect: Selected past identity decisions can constrain new ingestion after reconstruction; rebuild fidelity beyond the serialized fields is not established.
- Evidence limits: No observed clean/rebuild. Rejections, cache, metric histories and arbitrary prior article prose are not established as restored by this seed path.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # Denials MUST restore before blessed aliases: a blessed alias that was later denied
> # (`concept alias remove` on a rename/merge-blessed surface) must stay gone after
> # rebuild, and restore_blessed_aliases would otherwise resurrect it.
> --- `src/synto/pipeline/ingest.py`

#### MEM-RTE-synthesis-save
Label: Admit an answer as synthesis
Part of: [RT-RTE-query-answer](runtime.md#rt-rte-query-answer)

The human's save/synthesize flag enables automatic admission of a newly generated answer, not per-content approval. The heavy model authors prose; code determines duplicate handling, source eligibility, path allocation and manual-edit protection. The default keeps an existing question match; alternative strategies update in place or allocate a suffixed file. There is no factual-answer oracle. This is an open question followed by optional retention, not an autonomous evaluation experiment (SRC-1, `src/synto/pipeline/query.py`).

- Immediate return: QuerySaveResult or explicit save error, alongside the answer route's result.
- Later read-back: Published synthesis is included in later index generation and can be selected by a subsequent fast routing call and delivered to a heavy answer call.
- Delegated visibility: Later models receive the saved prose slice as wiki content; paths/hashes record source lineage but do not recreate the original context or private reasoning.
- Selection predicate: Normalized question hash for duplicates; resolved source paths exclude synthesis sources; in-place updates check stored body hash against current file.
- Invalidation or expiry: Keep/update/suffix policy; edited or unparseable existing content can block overwrite. Source hashes are retained but this path establishes no automatic validity expiry when a source changes.
- Activation or effect: File and DB admission refresh the index; actual future selection, compliance with grounding and answer benefit remain unobserved.
- Evidence limits: Selected-page lineage can overstate loaded evidence; refusing direct synthesis chaining does not prove absence of all indirect derivative reuse.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if any(_is_synthesis_source(config, db, path) for path in resolved_sources):
>     raise SynthesisChainError("Synthesis sources cannot include another synthesis page")
> --- `src/synto/pipeline/query.py`

#### MEM-RTE-source-passages
Label: Request verbatim source passages
Part of: [RT-RTE-mcp-answer](runtime.md#rt-rte-mcp-answer)

This is the primitive source-read part of the supplied MCP container, whose description explicitly includes primitive handlers; it does not synthesize an answer. An external client requests source text by literal phrase search, concept/ID lookup or sequential segment enumeration. Python performs selection, license gating and truncation; the requesting host chooses subsequent use. Read admission is policy enforcement, not content authoring (SRC-1, `src/synto/serve.py`).

- Immediate return: Segment metadata, snippets or bodies with IDs, source paths and truncation/policy counts.
- Later read-back: Raw retained segments and derived concept-to-segment associations reach later client requests; no Synto answer-saving mutation is requested by these handlers.
- Delegated visibility: External client gets the selected passages; FTS search returns snippets and IDs, and an explicit follow-up fetch returns full or capped bodies.
- Selection predicate: Literal-phrase FTS/BM25, concept-to-segment association ordered by confidence/reading order, exact segment ID, or source ID plus offset; license gate is distinct from article visibility.
- Invalidation or expiry: Reimport/reingest can change underlying segments/associations; source-access mode has process-lifetime legacy caching as supplied by runtime. No passage-specific time expiry established.
- Activation or effect: Tool payload delivery is wired; downstream agent interpretation, prompt inclusion and benefit are host-dependent and unobserved.
- Evidence limits: FTS depends on SQLite capability. Concept passage associations are chunk-derived; confidence does not establish paragraph entailment. A direct segment fetch is addressing, not evidence of content-relevance selection.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Budgets: FTS returns at most 50 results; concept passages at most 20, with default 8,000 and maximum 16,000 characters per passage; sequential metadata pages cap at 500. Direct segment fetch defaults to an unbounded body, with an optional cap no larger than 16,000 (SRC-1, `src/synto/serve.py`).

> Returns snippets only; fetch the full body with
> `read_source_segment`. limit is capped at 50.
> --- `src/synto/serve.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run)

The retained draft/article payload is natural-language Markdown on disk; metadata, source references, status, hashes and compile-run IDs have symbolic consumers in SQLite/YAML. Fast-model source-type prompts request accurate extraction, including paper claims/limitations, SQL object definitions versus references, corporate policy/ownership and web claims/evidence. That guidance does not establish adherence or source trustworthiness (SRC-1, `src/synto/pipeline/prompts/paper.md`, `src/synto/pipeline/prompts/sql.md`, `src/synto/pipeline/prompts/corp_docs.md`, `src/synto/pipeline/prompts/web_article.md`).

Context control starts before analysis: OCR/image noise and opaque media references are removed in memory, leaving raw material on disk. Existing concept hints favor body/title matches and cap at 30; writer link hints cap at 50 titles. Source gathering reads retained raw bodies, strips image text/placeholders, shares a budget so long sources do not starve short ones, then truncates. Its parameter name `max_chars` is misleading: sharing uses `max_chars * 4`, and caller supplies `heavy_ctx // 2`. This is an approximate context allocation, not a proof of token fit. Overflow recovery reduces source/existing-text budgets; only the resulting slices reach the writer (SRC-1, `src/synto/pipeline/ingest.py`, `src/synto/pipeline/compile.py`).

> limit = max_chars * 4  # same chars-per-token estimate as _truncate_to_budget
> --- `src/synto/pipeline/compile.py`

Compiled confidence is a software heuristic, not model certainty or verification:

> return min(1.0, len(source_paths) * 0.25 + _QUALITY_BONUS.get(best, 0.0))
> --- `src/synto/pipeline/compile.py`

The alternative `compile_notes` library/CLI legacy route constructs a fast planning prompt from 500-character source-body prefixes, then heavy writing uses gathered bodies. It does not merely consume the persisted summary column despite its “from source summaries” docstring. Contexts are separate inference calls, returning structured plans or articles; no general conversation transcript crosses them (SRC-1, `src/synto/pipeline/compile.py`).

> short = body[:500].replace("\n", " ")
> summaries.append(f"- {p.name}: {short}")
> --- `src/synto/pipeline/compile.py`

#### On [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication)

The generated body is model-authored; the human can inspect/edit/verify/approve/reject it, while automatic approval uses code predicates instead. Neither the status label nor verification metadata makes published prose factual. Later query receives body text, whereas readers can also inspect status/confidence/provenance. Rejection retains reasons and body only when feedback is nonempty. Writer delivery is restricted to the three recent feedback strings, not the stored rejected bodies. Rejection caps have software scheduling authority even when a model ignores the feedback (SRC-1, `src/synto/pipeline/compile.py`, `src/synto/state.py`; retained passage in [RT-BAP-rejection-guidance](runtime.md#rt-bap-rejection-guidance)).

#### On [RT-BAP-rejection-guidance](runtime.md#rt-bap-rejection-guidance)

Trace origin is human feedback on a generated draft, not a model's automatically extracted lesson from a full task transcript. Persistence is cross-compilation/session in SQLite. At the update consumer, feedback has requested revision authority; the resulting article later has informational authority at an answering model. This raw-feedback → prompt → revised-artifact → later-answer path is wired, but no improved future capacity is demonstrated. Feedback may state reasons; the system does not ensure it states a challenged theory, test result and blame placement (SRC-1, `src/synto/pipeline/compile.py`, `src/synto/state.py`).

#### On [RT-RTE-query-answer](runtime.md#rt-rte-query-answer)

Read-back is request-led: a current question triggers the fast model to choose retained page titles from `wiki/index.md`. Alias-based query expansion adds at most ten routing matches; optional graph expansion adds at most two confidence-filtered neighbors. Code then resolves/filters/loads up to the configured page cap plus extras, delivering at most 8,000 body characters per page to the heavy model. Its known-title linking list caps at 80. Source remains on disk after each call; a page ID in the window is not an automatically dereferenced memory handle (SRC-1, `src/synto/pipeline/query.py`).

The selector request explicitly distinguishes prior synthesized answers from fresh concept knowledge:

> "Synthesis pages capture prior answers; consider them when relevant "
> "but never prefer them over a fresh concept page. "
> --- `src/synto/pipeline/query.py`

The heavy consumer receives selected body slices plus the original question, not the full index, complete source collection or selector's private reasoning. Informational grounding is requested, not machine-checked entailment. Ordinary Q&A saves are exported and manually readable but do not obtain synthesis's explicit index admission merely by calling `generate_index` (SRC-1, `src/synto/pipeline/query.py`, `src/synto/indexer.py`).

#### On [RT-RTE-mcp-answer](runtime.md#rt-rte-mcp-answer)

Article primitives use `VaultReader`: list/search consumes first-paragraph summaries and aliases; read/get_concept returns published article body/frontmatter, with visibility checks. Its article record catalogue is cached per reader instance while bodies are read from disk; this is not an automatic live catalogue refresh guarantee. `trace_lineage` returns frontmatter lineage, not an independent recomputation of evidential support. Verbatim-source primitives have their own raw-text route and license controls. Answering's source-summary exception remains as supplied by runtime and prevents generalizing article visibility to all delivered memory (SRC-1, `src/synto/readers.py`, `src/synto/serve.py`; [MEM-RTE-source-passages](#mem-rte-source-passages)).

> summary=_extract_first_paragraph(body),
> --- `src/synto/readers.py:648-735`

#### On [RT-RTE-concept-curation](runtime.md#rt-rte-concept-curation)

Identity operations change symbolic associations and can rewrite natural-language link syntax, retire content or create disambiguation stubs. These are distinct curation effects, not proof of improved article meaning. Explicit alias denial is retained negative admission guidance; adding/moving aliases and rebuild persistence give that guidance future effect. Retirement to `.synto/retired/` keeps old bodies outside ordinary drafts, avoiding indiscriminate reapproval. Source comments describe legacy retired-draft relocation for the same reason (SRC-1, `src/synto/state.py`, `src/synto/pipeline/maintain.py`).

Unmerge is bounded recovery, not restoration of all history:

> Name-keyed behavioral ledgers (rejections, blocked_concepts, stubs) are NOT restored.
> --- `src/synto/pipeline/maintain.py`

`undo` can revert files without reverting `state.db`; it normally refuses batches with identity operations unless forced. Therefore Git history, DB identity state, retired bodies and exported packs have different recovery boundaries (SRC-1, `src/synto/cli.py`).

#### On [RT-RTE-pack-export](runtime.md#rt-rte-pack-export)

Export creates a portable snapshot of concept prose plus source summaries, raw notes, drafts, saved Q&A, synthesis, resources, metadata and routing instructions. Markdown is copied/relinked; JSON graph/identity/routes have symbolic consumer roles; generated prose instructions have model-interpreted behavioral authority. PackReader's indexed article reading is narrower than the full set of files an agent can directly open. Raw/draft copying has no per-content review or MCP-visibility predicate in export. Re-export resets managed content directories and refreshes instruction blocks; previously distributed copies have no established automatic withdrawal (SRC-1, `src/synto/pack_export.py`, `src/synto/readers.py`; supplied quote in [RT-RTE-pack-export](runtime.md#rt-rte-pack-export)).

#### On [RT-BAP-pack-guidance](runtime.md#rt-bap-pack-guidance)

Pack guidance is derived from retained vault state and a static rendering template, then stored in generated AGENTS.md/CLAUDE.md blocks. Its title/summary catalogue can shape later routing across sessions; human text outside generated blocks is preserved. It requests starting from JSON summaries, opening articles for detail and returning to raw sources for exact quotations. The external host must load and interpret it: persistence and delivery afford a later route but do not demonstrate instruction compliance (SRC-1, `src/synto/pack_export.py`; supplied passages in [boundary](boundary.md#boundary-and-evidence) and [RT-BAP-pack-guidance](runtime.md#rt-bap-pack-guidance)).

#### On [RT-RTE-compare-eval](runtime.md#rt-rte-compare-eval)

Report/snapshot persistence serves later operator inspection. Structural evaluation and contestant query outputs are neither automatic production-memory edits nor demonstrated training updates. These artifacts are different from raw source summaries, semantic knowledge edits and rejection guidance. Without supplied executions, report generation and comparison benefit remain unobserved; the existing record supplies the inspected evaluation boundary and quoted live-mode limitation (SRC-1, `src/synto/pipeline/eval.py`, `src/synto/compare/runner.py`).

## Write side

Acquisition starts with human-selected files or externally authored raw notes. `add` archives original bytes and creates canonical raw text; ingestion then automatically produces typed analysis, concept/source relationships, summaries and optional relations. Software filters candidate counts using model quality, normalizes against retained identities, and may preserve raw rejected relation candidates separately from admitted edges. Model authorship, deterministic physical I/O and human admission are not interchangeable. Import permission is not endorsement of each extracted claim ([MEM-OBJ-source-documents](#mem-obj-source-documents), [MEM-OBJ-raw-notes](#mem-obj-raw-notes), [MEM-OBJ-relations](#mem-obj-relations)).

Article writing proposes derived prose under shipped guidance, vault conventions, source budgets, existing article text and rejection feedback. Ordinary compilation respects certain edit/pending-draft guards; explicit force and malformed-content fallbacks qualify preservation. Publication offers human or numeric automatic admission. Summaries and synthesis bypass that gate, while identity operations require explicit semantic arguments. Rejection can retain a human reason, block repeated attempts and influence later writing. It is a durable feedback path, not evidence that model reasoning or knowledge quality improved ([RT-RTE-pipeline-run](runtime.md#rt-rte-pipeline-run), [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication), [MEM-OBJ-rejections](#mem-obj-rejections), [MEM-RTE-synthesis-save](#mem-rte-synthesis-save)).

Checkpointing and caching are automatic trace-fed writes with narrow purposes: prior model results reach resumed derivation or later calling code. They retain results, not a guaranteed account of why the result is correct. Rejection is different: a reason string can persist and reach a writer, but only the human supplied reason is retained as guidance. Metrics/audit traces reach reports; their storage alone does not establish automatic lesson formation. The known raw-to-derived-to-consumer chains coexist with the injected RAG store's unresolved consumer ([MEM-RTE-checkpoint-resume](#mem-rte-checkpoint-resume), [MEM-RTE-response-reuse](#mem-rte-response-reuse), [RT-BAP-rejection-guidance](runtime.md#rt-bap-rejection-guidance), [MEM-OBJ-metric-events](#mem-obj-metric-events), [MEM-OBJ-rag-embeddings](#mem-obj-rag-embeddings)).

Maintenance changes links, identities, files or admission state; it does not automatically validate article truth. Withdrawal has several horizons: rejection deletes a draft, curation retires an article, denial prevents an alias's readmission, clean deletes DB/wiki while preserving an identity seed, and cache/metrics clearing remove different retained artifacts. None of these establishes universal retraction from exported snapshots or past answers. Git undo is expressly not DB rollback ([RT-RTE-concept-curation](runtime.md#rt-rte-concept-curation), [MEM-RTE-identity-rebuild](#mem-rte-identity-rebuild), [RT-RTE-pack-export](runtime.md#rt-rte-pack-export)).

## Read-back

There are three distinct consumer patterns. A question requests model-selected page context; a primitive tool requests exact or lexical/concept-selected retained material; an exported agent can follow supplied guidance on disk. Request-driven automatic page loading is not independent unsolicited memory supply. No inspected route establishes an always-on host memory injector. Static shipped prompts shape current invocations but are not themselves material learned through use. Generated pack guidance, by contrast, can contain a retained vault-derived catalogue ([RT-RTE-query-answer](runtime.md#rt-rte-query-answer), [MEM-RTE-source-passages](#mem-rte-source-passages), [RT-BAP-pack-guidance](runtime.md#rt-bap-pack-guidance)).

Content and access metadata have different authority. Article bodies and summaries provide model-interpreted information. Rejection prose requests revision. Alias denials, status/hash guards, path containment, page caps and license policy cause deterministic inclusion/exclusion. Returning a source path or displaying lineage is not equivalent to opening the source; returning a selected title is not proof its body reached the model. The optional vector write has no established later consumer, so it stays a storage capability rather than being upgraded to a retrieval route ([MEM-OBJ-rag-embeddings](#mem-obj-rag-embeddings)).

## Integration issues

- **Qualified supplied fact — ordinary Q&A versus synthesis indexing.** [RT-RTE-query-answer](runtime.md#rt-rte-query-answer) says saves retain answer files and refreshed indexes. That is true as I/O but must not imply all saved Q&A is selectable by the standard index. `_save_query` writes `wiki/queries/` without an article row; `generate_index` explicitly enumerates concepts, source pages and synthesis, not that Q&A tree. Export still copies Q&A. [MEM-OBJ-synthesis](#mem-obj-synthesis) and [MEM-OBJ-index](#mem-obj-index) keep the consumer difference (SRC-1, `src/synto/pipeline/query.py`, `src/synto/indexer.py`, `src/synto/pack_export.py`).
- **Qualified supplied fact — rejection retention.** [RT-RTE-draft-publication](runtime.md#rt-rte-draft-publication) retains the right overall feedback route; the precise guard is nonempty feedback. Empty-feedback rejection can delete without retaining a rejection body/record. [MEM-OBJ-rejections](#mem-obj-rejections) supplies that limit (SRC-1, `src/synto/pipeline/compile.py`).
- **Possible identity overlap resolved as parts.** No replacement duplicate is intended. The new pipeline objects and checkpoint route are material parts of the existing pipeline; rejection content is part of draft admission; synthesis retention is part of query; source primitives are part of the supplied MCP container. Cross-route cache, index, identity and metric objects are distinct retained artifacts, not duplicate route declarations. The source-passages containment relies on the supplied MCP record explicitly covering primitive handlers as well as answering; reconciliation should not erase that distinction.
- **Optional RAG consumer unresolved.** [MEM-OBJ-rag-embeddings](#mem-obj-rag-embeddings) establishes injected write arguments but not persistence, initialization, retrieval selection or later consumers. [RT-CMP-embed](runtime.md#rt-cmp-embed) is consistent with that limit. Prevented conclusion: ordinary Synto operation uses durable vector recall (SRC-1, `src/synto/pipeline/ingest.py`).
- **Fine-grained extraction/curation limits.** PDF extractor internals, item helper admission, relation aggregation/retraction and every maintenance inverse were not fully inspected in this job. Known dispatch, persistence and later-consumer paths remain covered; exact extraction fidelity, universal relation retraction and full-state rollback remain unestablished. Relevant objects are [MEM-OBJ-source-documents](#mem-obj-source-documents), [MEM-OBJ-relations](#mem-obj-relations), [MEM-OBJ-concept-entities](#mem-obj-concept-entities) (SRC-1, `src/synto/cli.py`, `src/synto/pipeline/ingest.py`, `src/synto/state.py`, `src/synto/pipeline/maintain.py`).
- **Deployment and provenance unresolved.** No user vault or trace establishes actual activation, manually curated seed provenance, provider versions, agent compliance or benefit. The report records the shipped admission mechanisms without inventing the initial authorship of external material. These limits affect every route's operation status independently of its implementation status.

## Limitations and checks

The source identity, full revision and clean checkout were rechecked without executing Synto. Required method inputs were read completely, including the bounded runtime and record-contract reads. New source reads stayed within SRC-1 and read-only scope. Available-but-uninspected detail is named locally rather than treated as an access gap or absence. Countercases checked included direct summary publication versus review, ordinary Q&A versus synthesis, raw candidate retention versus admitted edges, empty-feedback rejection, legacy compilation, forced import/compilation, cache-option mismatch, and file-only undo versus DB recovery.

This is source-grounded wiring and doctrine analysis, not demonstrated operation or causal benefit. Deterministic `validate-output` validation passed. The first check identified two comment quotations with omitted comment markers; rereading and restoring the exact source text repaired their attribution without narrowing either finding. A pass establishes form and quotation occurrence, not analytical correctness or acceptance.
