---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "LLM Wiki memory: generated pages, lexical indexes, retained diagnostics, vocabulary controls and bounded conversation read-back."
run-id: AAS-2026-10-18-llmwiki-marimo-58054ccd9ae7-01
source-identity: https://github.com/Clod/llmwiki-marimo
reviewed-boundary: "0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7"
---

# llmwiki-marimo memory report

## Boundary and evidence

The subject is the whole-system knowledge loop frozen in SRC-1 at `0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7`, not only its chat retrieval agent. Included memory comprises source files and extracted text, generated and edited wiki pages, search/reference state, datasets, configuration and generated aliases, stored verification, caller-held conversation history, traces and recovery artifacts. Static shipped prompts are context controls, not accumulated memory. Provider-internal state and weights remain outside inspection; the generation and verifier integrations are described by [RT-CMP-openai-model](runtime.md#rt-cmp-openai-model) and [RT-CMP-local-nli-verifier](runtime.md#rt-cmp-local-nli-verifier). No provider persistence, parameter update or deployment-wide retention is inferred.

The supplied runtime is a provisional implementation account. Direct source reads below extend it, especially around withdrawal, diagnostic retention, selection budgets and alternative recovery. Evidence is implementation except where a source comment or template states intent. No application, tests, examples or models were executed. HEAD was rechecked against the frozen revision. No source access gap occurred; available but uninspected algorithms are named as limits rather than absences.

| Entry point / operation | SRC-1 paths and evidence coverage | Records / remaining limit |
|---|---|---|
| Upload, scan and regeneration | Direct reads of source extraction/chunk writes, page/alias admission and scan dataset-alias pass in `base/domain/ingestion/pipeline.py`; supplied service/caller tracing | [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest), [MEM-OBJ-source-text](#mem-obj-source-text), [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages); extractor internals and every regeneration edge not audited |
| Conversation draft/save, marimo last-answer save, convenience save | Direct `base/domain/chat/wiki_tools.py` drafting/write bodies; supplied `web/routes/chat.py`, marimo callers and chat service findings | [RT-RTE-chat-save](runtime.md#rt-rte-chat-save); caller-dependent review, not one admission policy |
| Pre-retrieval and open-page/collection alternatives | Direct `base/domain/chat/preretrieval.py` formatting, selectors, dataset injection and answer-dispatch bodies | [RT-RTE-preretrieval-chat](runtime.md#rt-rte-preretrieval-chat); default counts known, no audited global token cap |
| Agent reads/search and raw-source fallback | Direct `base/domain/chat/wiki_tools.py`, `base/domain/chat/tools.py`, `base/domain/tools/search.py`; supplied registration | [RT-RTE-strict-chat](runtime.md#rt-rte-strict-chat), [RT-RTE-streaming-chat](runtime.md#rt-rte-streaming-chat), [MEM-OBJ-document-chunks](#mem-obj-document-chunks) |
| Conversation filtering, trimming and condensation | Direct `base/domain/chat/history.py`, `base/services/chat.py` history conversion; supplied condenser and web/marimo ownership | Runtime chat route annotations below; cross-session persistence of UI conversations not established |
| Dataset query and finance overlay | Direct `base/domain/datasets/source.py`, dataset injection; supplied manifest-controlled tool composition | [RT-RTE-configure-grants](runtime.md#rt-rte-configure-grants), [MEM-OBJ-datasets](#mem-obj-datasets); complete finance formulas/parser semantics uninspected |
| Vocabulary and settings | Direct `base/domain/chat/config.py`, `base/domain/ingestion/alias_generation.py` and scan caller; supplied vocabulary/settings service findings | [MEM-OBJ-aliases-generated](#mem-obj-aliases-generated), configure-grants annotation; refresh parity across callers remains unresolved |
| Manual edit, page deletion, stale-page cleanup | Direct `base/services/wiki.py` save/delete bodies; bounded service searches; supplied repair dispatch | [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance); not every repair action audited |
| Source withdrawal | Direct complete `base/domain/tools/deletion.py`, retrieval SQL in `base/domain/tools/search.py` | [MEM-RTE-source-withdrawal](#mem-rte-source-withdrawal); stale is not a retrieval exclusion |
| Verification and reading-screen diagnostics | Direct `base/services/verification.py`, `base/domain/verify/store.py`, selected `base/domain/verify/page.py`; supplied verifier integration | [MEM-RTE-page-verification](#mem-rte-page-verification), [MEM-OBJ-page-verifications](#mem-obj-page-verifications); full context resolution and candidate ranking not audited |
| Lint annotations and gap replacement | Direct contradiction/data-gap/gap-filled bodies in `base/domain/repair/actions.py`; supplied runner/advisory checks | Maintenance annotation; model lint diagnosis reliability unestablished |
| History restore/reindex | Direct service interfaces, reindex contract and snapshot-versus-reindex dispatch in `base/domain/rollback/revert.py`; supplied restore progression | [MEM-OBJ-index-snapshots](#mem-obj-index-snapshots); crash consistency and every recovery failure uninspected |
| Evaluation, trace capture and inspection | Supplied direct-agent evaluator; direct `base/domain/tracing.py` payload writer and `scripts/render_trace.py` reader | [RT-RTE-model-evaluation](runtime.md#rt-rte-model-evaluation), [MEM-OBJ-spans](#mem-obj-spans); evaluator-to-policy feedback not established |

All new objects below name retained parts used by several supplied routes, rather than re-declaring those routes. The supplied runtime declares no operative objects. The two new routes isolate distinct maintenance subroutes with different effects and consumers.

## Core ideas

1. **The durable knowledge product is editable Markdown, not model weights.** Ingestion interprets source text, merges it into existing concepts and writes summaries. Chat can also become a page through a separate save action. Later ingestion consumes existing pages as input; later QA consumes selected page text. Neither path preserves inaccessible model reasoning. Source links and page prose can survive, but a request to preserve all old content is not an enforced semantic invariant ([RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest), [RT-RTE-chat-save](runtime.md#rt-rte-chat-save)).
2. **Read-back has several selectors, not a single search policy.** Code-selected chat uses roster/blacklist predicates, wiki chunks, open-page content, whole collection pages and dataset injection. Agentic chat lets the model choose registered reads/searches. These channels deliver different parts and different budgets. Calling content “curated” selects a branch; it does not prove verification or entailment ([RT-RTE-preretrieval-chat](runtime.md#rt-rte-preretrieval-chat), its annotation below).
3. **Access metadata and diagnostic state have different authority from prose.** Aliases affect which questions count as covered; page verification probabilities affect a reading-screen classification. They are not equivalent to facts in page prose, nor do they uniformly veto retention. Withdrawal removes raw-source access but can leave derived prose searchable ([MEM-OBJ-aliases-generated](#mem-obj-aliases-generated), [MEM-RTE-page-verification](#mem-rte-page-verification), [MEM-RTE-source-withdrawal](#mem-rte-source-withdrawal)).
4. **Conversation context is reduced, not transparently paged.** Refused exchanges disappear from model history; advisory tables become placeholders; only a short tail remains. A condenser can derive a standalone question from that tail, not recover arbitrarily old turns. Full UI text, the reduced model view and an explicitly saved page are separate artifacts ([RT-RTE-preretrieval-chat](runtime.md#rt-rte-preretrieval-chat), history annotations).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-source-text
Label: Sources and extracted source text

Source-native identity: workspace `sources/` files, extraction cache, source-kind `documents`, `document_pages` and source `document_chunks` in `.llmwiki/index.db`. Original files may be binary containers; extracted text is natural language with symbolic page/offset/parser metadata. Extraction and chunking do not make it model-derived synthesis. Ingestion commits text and chunks before knowledge generation, leaving a separately queryable evidential substrate. Initial document authorship/trust is external input, not guaranteed by the system. SRC-1, `base/domain/ingestion/pipeline.py`, `database/sqlite_schema.sql`.

> # Source doc now committed — subsequent tools can open their own connections.
> --- `base/domain/ingestion/pipeline.py`

This object spans ingestion, raw-source retrieval, verification and deletion; it is not identical to [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest). Read-back consumers include raw-source search and later page verification; original files also support re-extraction. Failed source rows are excluded by inspected search predicates. Raw sources do not gain instruction-level authority merely by being indexed. Withdrawal and recovery differ from generated page withdrawal ([MEM-RTE-source-withdrawal](#mem-rte-source-withdrawal)).

#### MEM-OBJ-wiki-pages
Label: Wiki Markdown pages

Source-native identity: `wiki/concepts/*.md`, `wiki/summaries/*.md` and collection `wiki/overview.md`, `wiki/index.md`, `wiki/log.md`. Natural-language bodies coexist with symbolic frontmatter, link syntax and maintenance markers on the filesystem. Summaries/concepts derive from source extraction, previous pages, or explicitly saved chat; manual edits can replace bodies. Overview is model-updated from previous overview, new summary and concept names; index entries are software-maintained pointers/short descriptions. Log/history are not automatically all injected into QA. SRC-1, `base/domain/ingestion/pipeline.py`, `base/domain/chat/wiki_tools.py`, `base/services/wiki.py`, `base/domain/chat/preretrieval.py`.

> existing = read_page(db_path, workspace, dir_path, slug)
> structured = structure_chat_content(
>         title, category, content, existing, client, model, language=language
>     )
> --- `base/domain/chat/wiki_tools.py`

Existing prose is update input and later answer evidence, not executable policy. Read-page tools deliver full Markdown, while pre-retrieval strips frontmatter from ordinary chunks and collection pages, retaining a raw-only fallback for chunks consisting solely of frontmatter. Thus source attribution metadata is not uniformly delivered across modes. Collection pages bypass FTS via direct disk reads. This object spans [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest), [RT-RTE-chat-save](runtime.md#rt-rte-chat-save) and maintenance/chat routes; no supplied object counterpart exists. Reasons survive only if written into prose or explicit warning details; no saved hidden reasoning is established.

#### MEM-OBJ-document-chunks
Label: Search chunks and reference metadata

Source-native identity: SQLite `document_chunks`, `chunks_fts`, `document_references` and document metadata. Chunk bodies encode natural-language source/page content; stemmed FTS terms, IDs, ranks, paths, references, versions and stale flags are symbolic access/control metadata. They are not embeddings or numerical learned memories. SRC-1, `database/sqlite_schema.sql`, `base/domain/ingestion/pipeline.py`, `base/domain/tools/search.py`, `base/domain/tools/reindex.py`.

> "WHERE chunks_fts MATCH ? AND d.status != 'failed'"
> --- `base/domain/tools/search.py`

Search adds scope predicates and orders by FTS rank with a result limit. The query returns content plus path/page/breadcrumb attribution; formatting downstream may truncate it. A stale flag is not in this exclusion predicate. Reference edges also drive source-dependent cleanup and verification scope; they are not identical to the prose they index. Files can rebuild much of this state, but not all metadata. The reindex contract explicitly names losses:

> Not recoverable from the
> files: `version`, `document_number` and the creation dates (reset), and
> `stale_since`.
> --- `base/domain/tools/reindex.py`

This store overlaps the effects of ingestion, chat-save and maintenance routes, with no supplied object counterpart. An SQL capability alone would not establish read-back; the shipped tools and pre-retrieval caller establish it here.

#### MEM-OBJ-datasets
Label: LocalMarkdownSource datasets

Source-native identity: `datasets/<categoria>.md`, parsed by `LocalMarkdownSource`. Files contain symbolic schema/frontmatter and structured rows, including values, dimensions, dates and source fields; free-text labels/prose remain interpreted text. Numeric row values are localized data, not distributed-parametric weights. Parser output lives transiently in Python; there is no dataset SQLite cache in this implementation. External authoring/replacement provenance remains unresolved. SRC-1, `base/domain/datasets/source.py`, `base/domain/chat/preretrieval.py`.

> rows = self._rows_for_file(path)
> if clave is not None:
>     rows = [r for r in rows if r.clave == clave]
> --- `base/domain/datasets/source.py`

Queries reparse latest files; category, key, metric and dimensions filter rows. Path resolution confines model-supplied category paths. Dataset presence alone is insufficient: at least one valid dataset activates the capability. Shipped pre-retrieval can append named-key rows to curated context, or only available key names when a category but no key is named. Tools/finance overlays are alternative consumers under [RT-RTE-configure-grants](runtime.md#rt-rte-configure-grants). Valid syntax and manifest checks are not data freshness guarantees. This is a retained operand of several routes, not a second declaration of tool activation.

#### MEM-OBJ-aliases-generated
Label: Generated aliases and configuration controls

Source-native identity: `.llmwiki/aliases.generated.toml`, `.llmwiki/dataset_aliases.fingerprint`, and relevant `wiki_config.toml` sections. Alias mappings, fingerprint, blacklist, false-synonym lists, thresholds and enable flags are symbolic controls; an optional configured system prompt is a separate natural-language part consumed as instructions. Files persist across calls; agents may cache their loaded interpretation. SRC-1, `base/domain/ingestion/alias_generation.py`, `base/domain/chat/config.py`; supplied settings/cache findings in [RT-RTE-configure-grants](runtime.md#rt-rte-configure-grants).

> data_aliases = merge_aliases(read_generated_aliases(wiki_path), data_aliases, false_synonyms)
> --- `base/domain/chat/config.py`

Concept extraction proposes aliases; software merges/revalidates accumulated mappings against coverage and owner rejections before writing. Scan has an alternative dataset-vocabulary proposal pass, gated by fingerprint or explicit force. It replaces dataset entries while preserving concept entries, rejects invented canonical terms and collisions, and writes the fingerprint. No-candidate scans return before this pass. Reasons for each accepted synonym are not stored in the inspected mapping; rejection controls can nevertheless suppress future regeneration. These controls shape later scope predicates rather than simply supplying answer prose. No supplied operative-object counterpart; their write and consumer paths cross ingestion and configure-grants.

#### MEM-OBJ-page-verifications
Label: Stored page verification

Source-native identity: SQLite `page_verifications` and `verification_sentences`, read as `StoredVerification`/`StoredSentence`. Mixed operative parts: sentence and excerpt prose; symbolic document IDs, offsets, body/source hashes, model/verifier names and timestamps; localized numerical probabilities. These probabilities are output scores, not model parameters. The stored best excerpt is whitespace-normalized and capped at 300 characters; it is not the complete comparison payload. SRC-1, `base/domain/verify/store.py`.

> def supported(self, threshold: float) -> bool:
>     return self.probability >= threshold
> --- `base/domain/verify/store.py`

No fixed supported verdict is persisted per sentence: later threshold changes reclassify scores. Body/source-hash checks distinguish valid/outdated results; ordinary page writes delete stale verification. Reading-screen consumers receive classified sentences and source/excerpt summaries, not classifier reasoning. This part has no supplied object counterpart and differs from [RT-CMP-local-nli-verifier](runtime.md#rt-cmp-local-nli-verifier), the model producing the scores. Its actual retention/consumer chain is [MEM-RTE-page-verification](#mem-rte-page-verification).

#### MEM-OBJ-spans
Label: Trace spans and optional payloads

Source-native identity: `.llmwiki/traces/spans.jsonl` and content-addressed files under `.llmwiki/traces/payloads/`. JSON span attributes are symbolic metadata; optional prompt, extraction, chunk and Markdown payloads contain underlying text/structured data. A collected path is a display summary holding references, not the full payload. SRC-1, `base/domain/tracing.py`, `scripts/render_trace.py`.

> if workspace is not None and channel in _channels():
>     payload_dir = workspace / ".llmwiki" / "traces" / "payloads"
> --- `base/domain/tracing.py`

Trace enablement, recording and channel selection govern persistence; heavy content is not guaranteed by a span's existence. The renderer loads JSON lines and optionally reads referenced payloads for operator inspection. These raw records can explain a route without constituting automatically derived future policy. Supplied evaluation findings establish no automatic trace-to-training update; bounded searches of tracing, chat services and renderer do not establish a production model consumer for these files. This is distinct from [RT-RTE-model-evaluation](runtime.md#rt-rte-model-evaluation) and the turn-local `ChatResult` summaries.

#### MEM-OBJ-index-snapshots
Label: Wiki history and index snapshots

Source-native identity: workspace Git page/config history and commit-associated SQLite snapshots. Git retains text versions and symbolic commit/file identities; snapshots retain the mixed database parts above. These are recovery inputs, not automatically selected chat context. SRC-1, `base/services/wiki.py`, `base/domain/rollback/revert.py`; supplied history behavior in [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance).

> if snapshots.is_usable(workspace, target_sha):
>     return "snapshot", f"the snapshot of {short} is available"
> --- `base/domain/rollback/revert.py`

When snapshot recovery is unavailable, preflight may choose reindex if extractor prerequisites exist; otherwise it refuses. Snapshot and reindex are not equivalent retained results: reindex reconstructs file-derived lookup state but loses metadata described in [MEM-OBJ-document-chunks](#mem-obj-document-chunks). A requested restore makes a new forward commit; later retrieval consumes the restored live state, not a historical pointer in the model window. History availability and snapshot retention depend on configuration/prerequisites. This object is a recovery input within supplied maintenance, not its duplicate route.

### Routes

#### MEM-RTE-source-withdrawal
Label: Source withdrawal with retained synthesis

Part of: [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance)

This isolates the source-deletion subroute within the broader maintenance route: user/service request with document ID → software classifies dependents before cascade → deletes one-to-one summaries → marks other citing pages stale → deletes source index row → optionally unlinks original file → history commit. Software, not a human reviewing each affected claim, determines retained/deleted dependents. SRC-1, `base/domain/tools/deletion.py`, `base/services/ingest.py`, `base/domain/tools/search.py`.

- Immediate return: `SourceDeletion` describes deleted summaries, newly stale citing pages, physical-file removal and success/failure.
- Later read-back: Surviving concepts still enter page/search reads; stale listing and maintenance can select them for review, regeneration or explicit deletion. Raw-source rows/chunks are removed through cascade.
- Delegated visibility: inapplicable — this deletion algorithm makes no model call; later retrieval separately supplies retained prose.
- Selection predicate: Source ID must exist and have source kind; `source_document_id` selects one-to-one derivatives, citation edges select other dependents, and `also_delete_file` controls physical deletion.
- Invalidation or expiry: Summaries and source index disappear; surviving concepts gain `stale_since`. Explicit stale-page deletion or later rewrite can supersede them. Keeping the original file permits later re-ingestion.
- Activation or effect: Software withdraws raw access but does not retract every proposition derived from the source. Search excludes failed rows, not stale pages, so retained synthesis remains eligible.
- Evidence limits: No execution or atomicity proof; stale does not identify precisely which sentences depend on the removed source. Derived prose accuracy after withdrawal is unestablished.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> stale_ids = citing_ids - delete_ids
> --- `base/domain/tools/deletion.py`

Admission is an open maintenance request. The caller can withhold it or choose file retention; the implementation rejects missing/non-source IDs and reports errors. There is no reference-answer oracle or semantic adjudication. History offers conditional recovery under the parent route, not a guarantee that all deletion effects are one transaction. The retained stale flag preserves a reason to revisit the page, but does not prevent its answer use.

#### MEM-RTE-page-verification
Label: Page verification retention and later display

Part of: [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance)

Explicit verification or post-ingest follow-up → page/source-context resolution → verifier comparison → SQLite result replacement → later reading-screen service. The service owns progression; the configured verifier produces scores. This subroute adds a diagnostic object without rewriting page prose. SRC-1, `base/services/verification.py`, `base/domain/verify/page.py`, `base/domain/verify/store.py`.

- Immediate return: `PageOutcome` with report and timing, or no-source outcome; multi-page service reports progress and continues after individual failures.
- Later read-back: `page_verification` loads current state and stored results, using the current configured threshold for reading-screen classification. Page/source hashes identify outdated results.
- Delegated visibility: Verifier receives body sentences and selected source passages, with generated boilerplate handling and candidate count; retained output is probabilities, offsets, source and abbreviated best excerpts, not opaque verifier internals.
- Selection predicate: Requested page IDs, all pages with context, or ingest-written pages; page must have disk file and index row. Resolved context, configured candidate count and threshold govern scoring/classification.
- Invalidation or expiry: A page without context deletes its stored verification; repeated verification replaces it. Hash mismatch marks it outdated; integrated page writes delete it. A new threshold reuses existing probabilities.
- Activation or effect: Later readers can see diagnostics; this route neither deletes unsupported sentences nor gates page admission or universally filters chat retrieval.
- Evidence limits: Full context resolution/candidate-ranking implementation not audited here; no model calibration, executed display or corrective benefit established. No evidence this stored report becomes ordinary chat prompt content.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> store.save_verification(conn, row["id"], report, body_hash=store.text_hash(body),
>                         source_hashes=context.source_hashes,
>                         model=getattr(verifier, "model_name", ""))
> --- `base/domain/verify/page.py`

Admission is software replacement of a diagnostic after an operator job or automatic follow-up, not approval of each sentence. Missing files/index rows reject the operation; no-context pages store nothing. Source passages serve as comparison evidence, not an independent expected-answer oracle. The route retains evidence summaries sufficient for a limited later explanation, but no claim of iterative theory revision follows from classification alone. Recovery of diagnostics differs between database snapshots and file-only reindex.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)

Storage/lineage: [MEM-OBJ-source-text](#mem-obj-source-text) is source-derived extraction; [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages) contains model-derived synthesis and deterministic summary assembly. The source is committed before page generation. Concept bodies are overwritten under software admission; operator file/job selection is not per-page approval. Existing content and the preservation template are update guidance, not an enforced lossless merge. Alias proposal/validation is another retained transformation, separate from prose and secondary on failure. SRC-1, `base/domain/ingestion/pipeline.py`, `base/domain/ingestion/alias_generation.py`; the parent record supplies the preservation and parse-fallback passages.

Read-back horizons extend across later source ingestions and QA sessions. Existing concepts go into another generation request; generated indexes/chunks select later answer context. This establishes wired reuse, not semantic activation or improved future capacity. Retained source associations support provenance; inaccessible generation reasoning is not reconstructed merely from them.

#### On [RT-RTE-chat-save](runtime.md#rt-rte-chat-save)

This is the inspected conversation-trace-to-durable-page chain: answered exchanges or the last answer → model structure/merge with existing same-slug page → optional web editing → page write, references/index, repairs → later chat retrieval or further merging. The origin is mixed user/model conversation, not independently verified source material. Files are marked with `sources=["chat"]`; that marker is provenance, not a correctness certificate. SRC-1, `base/domain/chat/wiki_tools.py`.

> overwrite=True, sources=["chat"],
> --- `base/domain/chat/wiki_tools.py`

Normal web review gives direct human content control; marimo/convenience saving admits the generated structure in software after initiation. Authoring, approval and physical file I/O must not be collapsed into “human-written memory.” The resulting prose can shape later answers by interpretation, but no automatic preservation of the full raw conversation, discarded refusals or model reasoning is shown. The runtime record supplies the bypass/review evidence.

#### On [RT-RTE-preretrieval-chat](runtime.md#rt-rte-preretrieval-chat)

Request direction is user-initiated QA; a deterministic selector supplies retained evidence to the answer invocation. Selector inputs include original/accepted rewritten question, blacklist, category/key vocabulary, concept names, aliases, open-page ID and collection intent. It defaults to six wiki chunks, or four raw chunks when no wiki hits; open-page content is prepended and duplicate labels removed. Collection overview/index are whole body reads. These are count budgets, not a global token budget. SRC-1, `base/domain/chat/preretrieval.py`.

> db_path: str, query: str, *, limit: int = 6, language: str | None = None
> --- `base/domain/chat/preretrieval.py`

The pre-retrieval formatter injects chunk content without the tools' 400-character preview truncation. Frontmatter is removed except raw-only chunks, and labels identify pages. Dataset augmentation on the curated branch selects named-key rows or only category key names; it is not a generic dump of every dataset. Open-page and collection routes can deliver retained content without an FTS match. “Curado” changes branch treatment, not epistemic warrant; the runtime record supplies evidence for branch-specific checks.

Working context: refusal filtering precedes table compaction and a default six-message tail. Reduced assistant prose/placeholder is fed to later model invocations while full caller answers can remain in UI memory. Condensation is an isolated rewrite invocation: selected history/question enter, only an accepted rewritten question crosses back into retrieval. It is not durable conversation summarization or an addressable pointer to evicted text. Older removed turns have no automatic reload in this inspected service. Tables may be recomputed by tools from current data, which is not recovery of historical values. SRC-1, `base/domain/chat/history.py`, `base/services/chat.py`, `base/domain/chat/preretrieval.py`.

> for message in trim_history(strip_refused_exchanges(list(messages))):
> --- `base/services/chat.py`

#### On [RT-RTE-strict-chat](runtime.md#rt-rte-strict-chat)

The model requests read-back through registered tools. A path chooses a full page, including frontmatter and inline citation header, confined to the wiki tree. Search queries choose wiki/raw scopes with rank ordering and default ten results; if the all-word search misses, any-word widening can supply partial hits. Tools format only the first 400 characters per result, with source/page/breadcrumb labels. A page read is therefore materially different from a search preview. SRC-1, `base/domain/chat/wiki_tools.py`, `base/domain/chat/tools.py`, `base/domain/tools/search.py`.

> snippet = r["content"][:400].strip()
> --- `base/domain/chat/wiki_tools.py`

The caller's conversation history is text-only conversion of user/assistant messages, not a persisted tool-message replay. Retrieved content is evidence interpreted by the model; the presence-of-substantive-tool-result check is not validation of that content. Same refusal/table/tail reduction applies as in the pre-retrieval annotation. Strict output can later be saved by the separate admission route.

#### On [RT-RTE-streaming-chat](runtime.md#rt-rte-streaming-chat)

Read-back uses the same agent tools and reduced prior history as strict mode, but immediate text display is not held for grounding substitution. Retained caller answers can enter subsequent reduced history or explicit saving despite that weaker output boundary. No stored verification flag is an inspected selector here. SRC-1, `base/services/chat.py`; the parent record supplies the minimum mode-difference passage. Full UI persistence beyond caller lifetime remains unestablished.

#### On [RT-RTE-configure-grants](runtime.md#rt-rte-configure-grants)

The retained parts have distinct consumers. Blacklists/aliases alter symbolic coverage decisions; configured prompt text instructs generation; threshold values classify stored scores; parsed dataset values supply tools/current context; finance attributes control tool construction. SRC-1, `base/domain/chat/config.py`, `base/domain/datasets/source.py`, `base/domain/verify/store.py`, and supplied manifest findings.

Generated aliases are admitted through software validation, with hand-written overrides winning and false-synonym deletion filters at read and write. The alternative dataset pass runs in scan after candidate iteration, but an empty candidate list returns first. Consequently “every dataset change immediately regenerates aliases” would be too strong. SRC-1, `base/domain/ingestion/pipeline.py`, `base/domain/ingestion/alias_generation.py`.

> if not candidates:
>     return []
> --- `base/domain/ingestion/pipeline.py`

The factory's cached config/grants and parse-on-query dataset values have different refresh horizons. The supplied web reset findings do not establish all callers refresh agents immediately after generation or external file replacement. Unknown initial dataset authorship does not obscure the known later alias-generation and row-selection mechanisms.

#### On [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance)

Manual save preserves frontmatter, replaces the body and rebuilds references/index/history; expected-version conflict prevention is conditional. Source deletion and stored verification have distinct retained-result chains in this member's two route records. Page deletion removes live file/index access; source deletion deliberately preserves multi-source concepts, so withdrawal is not one universal semantic retraction operation. SRC-1, `base/services/wiki.py`, `base/domain/tools/deletion.py`.

Contradiction repair writes an idempotent warning containing issue description and an invitation to review. Data-gap repair writes a marked TODO/suggestion; gap-filled repair replaces that block with a related-page link, preferring concepts over summaries. These transformations preserve some explicit criticism or missing-data reason in readable page content; later page reads or retrieval of its indexed chunk can deliver it, without a guarantee the model follows it. Unsupported-sentence checks are advisory under the supplied dispatch record, not automatic sentence deletion. SRC-1, `base/domain/repair/actions.py`.

> f"> Review both pages and resolve the conflicting claims."
> --- `base/domain/repair/actions.py`

Reindexing is not re-ingestion: it reconstructs search state without another generation call or Markdown rewrite. Snapshot restoration can preserve database state unavailable from files; file-based reconstruction loses stale/version metadata. Thus the schema's warning that re-running ingestion is nondeterministic must not be generalized to all index recovery. SRC-1, `base/services/wiki.py`, `base/domain/tools/reindex.py`, `base/domain/rollback/revert.py`.

#### On [RT-RTE-model-evaluation](runtime.md#rt-rte-model-evaluation)

Its immediate grades/verdict do not establish a durable policy update or production read-back consumer. The inspected trace writer and renderer retain/inspect raw execution evidence, but no inspected chain turns evaluator results into learned weights or automatic page admission rules. This is a bounded integration limit, not evidence that all evaluation artifacts are absent. SRC-1, `scripts/eval_chat_model.py` via supplied record; direct `base/domain/tracing.py`, `scripts/render_trace.py`.

## Write side

Source acquisition is operator-directed, but extracted text, generated synthesis and references are admitted by software. The source and generated layers must stay separate: a source can be ready before generation completes; malformed extraction can still produce a summary through the supplied fallback. Existing-page preservation is requested, not checked proposition by proposition ([RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)).

Chat saving is a qualifying trace-fed transformation, not merely a raw log: selected conversation becomes a structured page that later retrieval can consume. The UI-specific human review and software-only convenience paths have different admission controls. No automatic save after every answer is established. The page may retain argument prose if present, but the raw exchange and hidden reasoning are not guaranteed to survive structuring ([RT-RTE-chat-save](runtime.md#rt-rte-chat-save), its annotation).

Configuration editing, model-proposed aliases and dataset replacement are separate write surfaces. User settings can directly replace controls; alias validators enforce collisions/rejections; external dataset content has unresolved initial authorship. The scan's dataset-alias pass is a known subsequent transformation even though dataset initialization is unknown ([MEM-OBJ-aliases-generated](#mem-obj-aliases-generated)).

Maintenance can rewrite pages, append criticism, replace a gap warning, delete content or restore earlier state. Verification instead stores diagnostic scores/summaries; it does not rewrite the diagnosed page. Source withdrawal removes some dependents and marks others stale. Neither optional verification nor stale marking constitutes universal admission rejection ([MEM-RTE-page-verification](#mem-rte-page-verification), [MEM-RTE-source-withdrawal](#mem-rte-source-withdrawal)).

Trace spans and optional content-addressed payloads retain raw evidence for inspection, not an established automatic update rule. Conversation history reduction produces a later-invocation view but no inspected durable summary checkpoint; the condenser returns a rewritten query, not a replacement conversation archive. Database snapshots and file-based reconstruction are recovery alternatives, not equivalent semantic memory checkpoints ([MEM-OBJ-spans](#mem-obj-spans), [MEM-OBJ-index-snapshots](#mem-obj-index-snapshots)).

## Read-back

The operative chains are deliberately different:

- **Further ingestion:** slug-selected existing concept body enters a concept-update model call. It carries previous conclusions as generation input, without enforced losslessness.
- **Code-selected QA:** question/roster/open-page/collection selectors deliver page bodies/chunks, optionally dataset rows or key names, through a user-context template. Selection is automatic inside a requested turn, not an unsolicited background push to a future agent.
- **Agentic QA:** the answer model chooses registered page/search/data requests; formatted tool returns enter its loop. Full page reads, search previews and raw-source fragments differ in delivered parts and authority.
- **Subsequent conversation turns:** filtered, compacted tail text becomes PydanticAI messages. This resembles value-copying a short working frame; an omitted-turn placeholder does not act as a dereferenceable heap pointer. Dataset tools can fetch current numbers again, not resurrect omitted conversation text.
- **Reading/maintenance:** stored probabilities and hashes become current-threshold diagnostics; warning prose and stale flags guide human or maintenance operations. They do not uniformly gate QA.
- **Recovery:** operator-selected revision plus usable snapshot/reindex prerequisites restore live files/index. Later chat reads the resulting state rather than directly reading historical snapshots.
- **Trace inspection:** renderer loads stored spans and optionally payloads for operators. This is an inspection consumer, not established training or answer-policy feedback.

These chains are supported by the records/annotations above. They establish wired delivery and transformations only. No observed run demonstrates that selected text was used correctly or that later capacity improved.

## Integration issues

- **Refine withdrawal, not a correction of the supplied broad maintenance record.** [MEM-RTE-source-withdrawal](#mem-rte-source-withdrawal) is a part of [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance). SRC-1, `base/domain/tools/deletion.py`, `base/domain/tools/search.py`: stale concepts remain searchable. Reconciliation must not translate source deletion into full retraction of synthesized knowledge.
- **Separate verification model, retained report and page content.** [MEM-RTE-page-verification](#mem-rte-page-verification) and [MEM-OBJ-page-verifications](#mem-obj-page-verifications) extend maintenance; they do not duplicate [RT-CMP-local-nli-verifier](runtime.md#rt-cmp-local-nli-verifier). Full context-resolution/candidate-ranking inspection remains incomplete, preventing claims of complete source coverage. Stored diagnostics are not established ordinary chat context or a universal veto.
- **Alias refresh has a trigger limit.** The configure-grants annotation and [MEM-OBJ-aliases-generated](#mem-obj-aliases-generated) preserve the scan alternative and early no-candidate return. Cache refresh after generated-alias changes and marimo parity remain uninspected; immediate activation across all interfaces is not established. SRC-1, `base/domain/ingestion/pipeline.py`, `base/domain/chat/config.py`; [RT-RTE-configure-grants](runtime.md#rt-rte-configure-grants).
- **Recoverability is partial.** [MEM-OBJ-index-snapshots](#mem-obj-index-snapshots) and [MEM-OBJ-document-chunks](#mem-obj-document-chunks) qualify the broad maintenance account: reindex and snapshot have different metadata fidelity. SRC-1, `base/domain/tools/reindex.py`, `base/domain/rollback/revert.py`. No current runtime fact is contradicted; a blanket lossless-rebuild inference would be wrong.
- **Conversation and trace persistence are not interchangeable.** Full caller-held UI history, model-visible reduced history, optional trace payloads and a saved page are different parts. Cross-session UI persistence and an automatic evaluator/trace-to-production update remain unestablished; see chat annotations and [MEM-OBJ-spans](#mem-obj-spans). SRC-1, `base/services/chat.py`, `base/domain/tracing.py`, `scripts/render_trace.py`.
- **Coverage limits remain local.** Full extractor/parser/finance internals, every lint/repair path and every restoration failure were not audited. Supplied runtime evidence supports the named routes; direct reads refine selected memory mechanisms, not complete algorithm coverage. No new declaration is a possible duplicate of a supplied referent: runtime has no operative-object declarations and the two routes explicitly declare containment. No supplied factual correction is asserted.

## Limitations and checks

Implementation and source-native comments are the evidence layers; no execution trace or causal experiment was supplied or generated. Source trust, generated factual fidelity, verifier calibration, prompt-injection compliance, cross-process consistency and actual memory benefit remain unestablished. Roster inclusion, citation, delivery, diagnostic scores and retained warnings must not be substituted for those conclusions.

The frozen source HEAD was checked against `0df06b0499a6242a4a5edfb1495e1d55a3e3c8b7`; all direct source reads/searches were within the registered checkout. The supplied job, member types, worker rules, collection and records contract were read; no authoring skill or prior analysis was used. Deterministic validation is recorded after running the invocation's validator; its scope is structure, identity and quotation occurrence, not analytical acceptance.

Validation: passed with the supplied `commonplace-run validate-output` command.
