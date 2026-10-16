---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Kompl memory: source-derived wiki, cross-session extraction indexes, bounded query context and alternate admission/withdrawal paths."
run-id: AAS-2026-10-14-kompl-9cffb1e5eb86-01
source-identity: "https://github.com/tuirk/Kompl"
reviewed-boundary: "17970c969b0c2576bf722840e0e2db3c6416a7aa"
---

# Kompl memory report

## Boundary and evidence

Kompl retains converted sources, extracted facts and indexes, draft prose, admitted wiki pages, schema instructions and conversation/activity records. Its memory scope includes the app-owned write/read loop, Python storage/vector/model operations, MCP delivery, CLI startup maintenance and archive restoration. External agents' context assembly and provider-internal state remain outside inspectable consumer wiring. The frozen source is SRC-1 in [boundary](boundary.md#source-register). All new source reads below concern implementation at that revision. No target execution was performed; delivery is wired, activation and benefit are unobserved.

Direct reads supplement, rather than replace, the supplied runtime. They include bounded sections of `app/src/lib/db.ts`, `app/src/app/api/compile/plan/route.ts`, `nlp-service/services/llm_client.py` and `scripts/migrate.py`, and complete reads of the small alternate endpoints/helpers identified below. The direct database trace contradicts the runtime's history-tail account and qualifies its chat-draft adoption account.

| Operation / retained part | SRC-1 paths | Coverage and limit |
|---|---|---|
| Staging, conversion, acquisition and retry | `app/src/app/api/onboarding/stage/route.ts`, `app/src/app/api/onboarding/finalize/route.ts`, `app/src/app/api/compile/run/route.ts`, `n8n/workflows/session-compile.json` | Supplied [RT-RTE-session-compile](runtime.md#rt-rte-session-compile); raw storage directly read in [MEM-OBJ-raw](#mem-obj-raw). Conversion branches not exhaustively inspected; source fidelity not established. |
| Extraction, aliases, historical mentions and plan selection | `app/src/lib/db.ts`, `app/src/app/api/compile/plan/route.ts`, `app/src/app/api/compile/resolve/route.ts` | Direct DB/plan reads plus supplied [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft); [MEM-OBJ-extractions](#mem-obj-extractions), [MEM-OBJ-aliases](#mem-obj-aliases), [MEM-OBJ-mentions](#mem-obj-mentions). Resolver supplied, not independently audited. |
| Draft context and schema | `app/src/app/api/compile/draft/route.ts`, `nlp-service/services/llm_client.py` | Direct scoped search and prompt read; annotations on [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft), [RT-OBJ-schema](runtime.md#rt-obj-schema). Actual generated schema/prose unavailable. |
| Commit, approval, rejection and flush | `app/src/lib/approve-plan.ts`, `app/src/app/api/drafts/[plan_id]/reject/route.ts`, `app/src/lib/db.ts`, `app/instrumentation.ts` | Approval/rejection/DB directly read; driver/startup supplied through [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval); [MEM-OBJ-pages](#mem-obj-pages). No atomic filesystem/index guarantee. |
| Chat selection, answering, history and manual saving | `app/src/lib/retrieval.ts`, `app/src/app/api/chat/route.ts`, `app/src/app/api/chat/save-draft/route.ts`, `nlp-service/services/llm_client.py`, `app/src/lib/db.ts` | Direct reads; [MEM-RTE-history-read](#mem-rte-history-read), [MEM-RTE-manual-save](#mem-rte-manual-save), [MEM-CLM-chat-provenance](#mem-clm-chat-provenance). |
| Wiki/MCP and previous version access | `mcp-server/index.ts`, `app/src/app/api/wiki/[page_id]/data/route.ts`, `app/src/app/api/wiki/[page_id]/previous/route.ts` | Current delivery supplied [RT-RTE-mcp-read](runtime.md#rt-rte-mcp-read); previous endpoint directly read. Client's later behavior excluded. |
| Source deletion, archive/unarchive and recompile | `app/src/lib/source-delete.ts`, `app/src/lib/recompile.ts`, `app/src/app/api/sources/[source_id]/route.ts`, `app/src/app/api/sources/[source_id]/recompile/route.ts`, `app/src/lib/db.ts` | Deletion/redraft supplied [RT-RTE-source-maintenance](runtime.md#rt-rte-source-maintenance); archive/recompile/cleanup DB directly read; [MEM-RTE-withdrawal-cleanup](#mem-rte-withdrawal-cleanup). |
| Lint, saved links and startup backup | `app/src/app/api/wiki/lint-pass/route.ts`, `app/src/lib/saved-links.ts`, `cli/src/startup-tasks.ts`, `cli/src/index.ts` | Direct reads/search; [MEM-RTE-lint-retention](#mem-rte-lint-retention), [MEM-RTE-saved-links](#mem-rte-saved-links). Startup is an overdue check, not continuous scheduling. |
| Direct storage APIs and older model crossref | `nlp-service/routers/storage.py`, `nlp-service/routers/pipeline.py` | Storage directly read and pipeline dispatch searched; [MEM-RTE-storage-write](#mem-rte-storage-write). Older crossref is exposed, but its returned prose has no independently traced alternative persistence caller. |
| Vector upsert/search/restore/delete/backfill | `nlp-service/services/vector_store.py`, `nlp-service/routers/vectors.py`, `app/src/app/api/compile/backfill-vectors/route.ts` | Direct reads; [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages). App retry helper is supplied rather than independently audited. |
| Export/import and operator replacement | `app/src/app/api/export/route.ts`, `app/src/app/api/import/route.ts`, `AGENTS.md` | Supplied [RT-RTE-archive-import](runtime.md#rt-rte-archive-import); archive import can restore every listed memory family. Complete export implementation not independently read; backup completeness not established. |
| Evaluation and retained reports | `validation/2026-05-05-multi-provider-corpus/REPORT.md`, `validation/2026-05-22-deepseek-flash/REPORT.md`, `scripts/integration-test.sh` | Supplied boundary evidence only. Exact corpus unavailable; production memory update from evaluation results not traced. Prevents claiming evaluation-driven semantic improvement. |
| Settings, progress and provider state | `app/src/lib/db.ts`, `nlp-service/services/providers/gemini.py`, `nlp-service/services/providers/deepseek.py` | DB settings/control searches plus supplied provider/compile records. Settings influence later selection/admission; remote context/weights opaque. No inferred provider memory or training. |

## Core ideas

1. **Compile before querying.** Raw markdown is retained separately from model-derived wiki prose. Extractions and canonical mention indexes can affect future planning even before a page is admitted. Later drafting rereads prior prose and schema rather than inheriting a persistent model window. [MEM-OBJ-raw](#mem-obj-raw), [MEM-OBJ-extractions](#mem-obj-extractions), [MEM-OBJ-mentions](#mem-obj-mentions).
2. **Retention and consumer visibility differ.** SQLite outbox prose, gzip files, FTS and vectors are separate products. An existing file takes precedence over pending content in the app reader, while chat lacks pending-content fallback. Admission is not uniform read-back. [MEM-OBJ-pages](#mem-obj-pages), [MEM-OBJ-pages-fts](#mem-obj-pages-fts), [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages).
3. **Budgets select evidence, not just storage.** Draft prompts privilege schema/old prose/dossiers before trailing sources. Chat clips selected pages and limits history. The implemented history query actually selects earliest rows, not the claimed recent tail. [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft), [MEM-RTE-history-read](#mem-rte-history-read).
4. **Trace feedback is a proposal path with a broken ordinary adoption link.** Chat answers can become pending wiki drafts automatically or by explicit save. Their page IDs are stored as source IDs; ordinary approval attempts source-provenance insertion against a sources foreign key. Thus pending retention does not establish a working page-to-answer-to-page cycle for normal disjoint IDs. [MEM-RTE-manual-save](#mem-rte-manual-save), [MEM-CLM-chat-provenance](#mem-clm-chat-provenance).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-raw
Label: Raw source markdown

Converted input text is natural-language material in `/data/raw/<source_id>.md.gz`; source IDs, hashes, URLs and statuses in SQLite are symbolic access/lineage metadata, not the prose. Conversion means raw here is not necessarily verbatim original bytes. The app writes it on ingestion; later extraction, ordinary drafting, deletion redraft and source display reread it. Raw storage is distinct from the control plans in [RT-OBJ-page-plans](runtime.md#rt-obj-page-plans); its write/read chain is within [RT-RTE-session-compile](runtime.md#rt-rte-session-compile). SRC-1: `app/src/lib/db.ts`; supplied runtime source-consumer trace.

> const gzipped = zlib.gzipSync(Buffer.from(markdown, 'utf-8'));
> fs.writeFileSync(filePath, gzipped);
> --- `app/src/lib/db.ts`

The shipped comment calls raw sources immutable and says re-ingest uses another ID. This is a workflow convention, not a prohibition against direct volume/file API replacement. Input choice is caller-controlled; each conversion/extraction result is software-admitted, not individually approved.

#### MEM-OBJ-extractions
Label: Retained source extractions

SQLite `extractions` holds JSON NER, profile, keyphrases, TF-IDF and model output keyed by source ID. Claim text and explanations are natural language; named fields and identifiers have symbolic consumers. These are derived source knowledge, not agent action traces. Extraction writes replace a row; later planning/dossier construction rereads fields across sessions. Distinct from [RT-OBJ-page-plans](runtime.md#rt-obj-page-plans): it supplies evidence to planning rather than plan progression. SRC-1: `app/src/lib/db.ts`, `app/src/app/api/compile/draft/route.ts`; [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft).

> INSERT OR REPLACE INTO extractions
> --- `app/src/lib/db.ts`

> WHERE e.source_id IN (${placeholders})
> --- `app/src/lib/db.ts`

No independent truth check is established by JSON persistence. Dossiers privilege this derived text as factual reference at the drafting consumer; semantic trust is requested, not warranted by the index.

#### MEM-OBJ-aliases
Label: Retained canonical aliases

SQLite `aliases` maps alias strings to canonical names and optionally canonical page IDs. Its symbolic lookup consumers include later resolution, mention normalization and cross-reference/link work. Lineage mixes name-resolution results and deterministic page-ID backfill; a successful prose approval can pin an alias independently of its file flush. It is distinct from the schema instructions in [RT-OBJ-schema](runtime.md#rt-obj-schema), and belongs to the memory carried by [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft). SRC-1: `app/src/lib/db.ts`, `app/src/lib/approve-plan.ts`; runtime resolution account. Exact correctness of canonical identity remains unobserved.

> 'SELECT alias, canonical_name FROM aliases WHERE canonical_name IS NOT NULL'
> --- `app/src/lib/db.ts`

#### MEM-OBJ-mentions
Label: Historical entity and relationship mentions

SQLite `entity_mentions` and `relationship_mentions` are symbolic indexes derived from extractions plus canonicalization. Each source/name or source/pair/type row can survive session boundaries. Counts and retrieved historical source IDs govern promotion and dossier provenance, not evidence of independent corroboration or truth. Re-extraction deletes the prior source's mentions; source deletion has cascading foreign keys in the shipped migrations. Distinct from [RT-OBJ-page-plans](runtime.md#rt-obj-page-plans), these are upstream accumulators used by [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft). SRC-1: `app/src/lib/db.ts`, `scripts/migrate.py`, `app/src/app/api/compile/plan/route.ts`.

> SELECT COUNT(*) AS n FROM entity_mentions WHERE canonical_name = ?
> --- `app/src/lib/db.ts`

> DELETE FROM entity_mentions WHERE source_id = ?
> --- `app/src/lib/db.ts`

Archive status does not appear in this count predicate. Hiding all-archived pages from query indexes therefore does not establish removal of those sources from historical promotion evidence.

#### MEM-OBJ-pages
Label: Wiki prose and recovery versions

Natural-language markdown persists as current gzip page files, pending SQLite `pages.pending_content`, and timestamped previous files. Page metadata, hashes, provenance and previous-path pointers are symbolic; metadata summaries are lossy text displays, not full page payloads. Prose lineage includes original-source passthrough, model drafts, redrafts, imported content and deterministic saved-links generation. Consumers include wiki/MCP display, future draft calls and answer synthesis. Distinct from the draft/control referent [RT-OBJ-page-plans](runtime.md#rt-obj-page-plans): these are installed/readable products of [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval).

SRC-1: `app/src/lib/db.ts`, `app/src/lib/approve-plan.ts`, `app/src/app/api/wiki/[page_id]/previous/route.ts`; archive protocol and its failure window are supplied in the runtime account.

> if (fs.existsSync(filePath)) {
> --- `app/src/lib/db.ts:537-545`

> return page?.pending_content ?? null;
> --- `app/src/lib/db.ts`

An old existing file wins over new outbox prose. Previous-version access requires a page row, a validated archive path and an existing file; this is a recovery inspection route, not automatic rollback. Import or direct writes can bypass ordinary generation/admission. No retention expiry for old page archives was established in these paths.

#### MEM-OBJ-pages-fts
Label: Full-text page index

SQLite `pages_fts` stores title/body text as a derived symbolic search representation with fixed FTS ranking. Approval strips frontmatter before insertion; saved-links insertion indexes its generated markdown. The index can change before file delivery succeeds. Distinct from [MEM-OBJ-pages](#mem-obj-pages) and from [RT-OBJ-page-plans](runtime.md#rt-obj-page-plans): it is selection state, not admitted prose or a plan. SRC-1: `app/src/lib/approve-plan.ts`, `app/src/lib/saved-links.ts`, `app/src/lib/retrieval.ts`.

> db.prepare('INSERT INTO pages_fts (page_id, title, content) VALUES (?, ?, ?)').run(
> --- `app/src/lib/approve-plan.ts`

Later hybrid retrieval uses search results to choose files, not FTS body as final answer context. Deletion/archive cleanup can remove entries separately from file removal.

#### MEM-OBJ-wiki-pages
Label: Chroma wiki page vectors

Chroma collection `wiki_pages` under `/data/vectors` retains distributed-parametric dense embeddings, symbolic metadata/IDs and text document prefixes. Keep these parts distinct: dense vectors support cosine selection, metadata/document text supplies access/display/backup material, and answer delivery subsequently rereads gzip prose. Derived vectors are not changes to [RT-CMP-mini-lm](runtime.md#rt-cmp-mini-lm) weights. Normal lineage embeds the first 2000 characters of page content; archive restoration can insert supplied vectors without re-embedding, leaving their original model/content lineage unresolved. SRC-1: `nlp-service/services/vector_store.py`, `nlp-service/routers/vectors.py`.

> truncated = text[:_MAX_EMBED_CHARS]
> --- `nlp-service/services/vector_store.py`

> collection.upsert(ids=ids, embeddings=embeddings, documents=documents, metadatas=metadatas)
> --- `nlp-service/services/vector_store.py`

The fixed-name loader's version limits are in the supplied component. Upsert, restore and backfill are software-admitted service operations; no semantic approval is present in those inspected handlers. Backfill skips IDs already indexed, so it is not proof of refreshing stale vectors. This is distinct from [RT-RTE-archive-import](runtime.md#rt-rte-archive-import), which can restore the object, and contributes to [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback). Successful delete/retry remains unobserved.

#### MEM-OBJ-chat-messages
Label: Retained chat messages

SQLite `chat_messages` keeps caller questions and model/fixed answers as natural-language trace content, with symbolic role/session/model/citation/page-ID fields. Imported messages add archive-supplied lineage. Persistence is longer than the delivered window; message text, not stored citation metadata, enters subsequent synthesis history. Distinct from [RT-OBJ-page-plans](runtime.md#rt-obj-page-plans): answers can separately propose drafts but conversation rows remain raw interaction traces. SRC-1: `app/src/lib/db.ts`, `app/src/app/api/chat/route.ts`; [MEM-RTE-history-read](#mem-rte-history-read).

> INSERT INTO chat_messages (session_id, role, content, citations, pages_used, chat_model)
> --- `app/src/lib/db.ts`

#### MEM-OBJ-activity-log
Label: Retained maintenance and contradiction activity

SQLite `activity_log` stores symbolic event/session/step metadata plus natural-language reasons and JSON findings. Contradiction triage reasons become page-sidebar evidence; lint results become latest-result/operator diagnostics. These are retained observations/judgments, not automatically revised method instructions. Control-progress rows and settings are separate symbolic records used for retry and overdue checks. Closest supplied record is [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft), which mentions reasons but does not declare this store. SRC-1: `app/src/app/api/compile/plan/route.ts`, `app/src/lib/db.ts`, `app/src/app/api/wiki/lint-pass/route.ts`.

> AND json_extract(details, '$.page_id') = ?
> --- `app/src/lib/db.ts`

The later contradiction reader parses `details.source_id`, but the planner supplies source ID to the outer activity row rather than that details field; title/URL/reason remain readable. Thus readable judgment and complete structured lineage differ.

### Routes

#### MEM-RTE-history-read
Label: Chat history read-back

Part of: [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback)

This material selection subroute corrects the supplied history claim. The app inserts the current question, asks `getChatHistory(sessionId, 11)`, drops the last returned row, and passes only role/content to synthesis. The database returns earliest timestamp-ordered rows, not a recent tail. Beyond eleven messages, the current question need not be in those rows, so dropping the last returned row can discard an older message instead. The current question is separately supplied to synthesis. SRC-1: `app/src/lib/db.ts`, `app/src/app/api/chat/route.ts`, `nlp-service/services/llm_client.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Up to eleven stored rows to the app, then up to ten role/content entries to synthesis.
- Later read-back: Earlier persisted user/assistant text reaches later model calls; older nonselected rows remain stored.
- Delegated visibility: Text only, without historical citation/page-use metadata; Python additionally takes history[-10:].
- Selection predicate: Session equality, ascending timestamp, LIMIT 11, then slice(0, -1); no descending-tail query.
- Invalidation or expiry: Selection excludes later rows once the limit is reached; no deletion or summary replacement occurs here.
- Activation or effect: Prompt inclusion is wired; dependence or improved dialogue behavior unobserved.
- Evidence limits: No executed long conversation; static SQL and caller establish the selection mismatch, not measured harm.

> ORDER BY created_at ASC
> LIMIT ?
> --- `app/src/lib/db.ts:2193-2203`

> .slice(0, -1)
> --- `app/src/app/api/chat/route.ts`

This is trimming by selection, not compaction: no derived history summary is produced, and no pointer in the model window automatically reloads excluded messages. The history API also uses the same helper with limit 20, according to scoped source search in `app/src/app/api/chat/history/route.ts`.

#### MEM-RTE-manual-save
Label: Manual answer draft saving

An app caller supplies session, content and citations to `/api/chat/save-draft`; code creates query-generated markdown and inserts a pending plan. It is an additional admission-to-draft route, distinct from the automatic count trigger in [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback); both converge on [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval). SRC-1: `app/src/app/api/chat/save-draft/route.ts`, `app/src/lib/db.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: saved true after pending-plan insertion.
- Later read-back: Draft list/approval reads the retained prose; ordinary installed wiki read-back is constrained by [MEM-CLM-chat-provenance](#mem-clm-chat-provenance).
- Delegated visibility: No additional generation call; submitted answer text and citation links form the retained draft.
- Selection predicate: Nonempty session/content; no three-page requirement or source-of-content check in this handler.
- Invalidation or expiry: Pending approval can be rejected; page deletion prunes associated IDs or removes an empty chat draft.
- Activation or effect: Draft persistence wired; later adoption/behavior unobserved.
- Evidence limits: Submitted text need not match a persisted assistant message; caller-controlled citations do not authenticate support.

> session_id: `chat-manual-${session_id}`,
> --- `app/src/app/api/chat/save-draft/route.ts`

> pages_used: citations.map((c) => c.page_id),
> --- `app/src/app/api/chat/save-draft/route.ts`

Trigger and proposer: a caller-selected answer/content, with a shipped Save to wiki affordance. Admission: software accepts the draft; explicit approval/rejection is a separate decision. Caller identity does not establish human authorship/review; code, not a model, formats it. Mode: open content submission, no answer oracle. Recovery: rejection retains the row; successful installation uses the shared outbox route, not this save response. Citation links persist, not an independently retained reasoning justification.

#### MEM-RTE-lint-retention
Label: Lint findings retention

CLI startup checks a 36-hour overdue timestamp and calls the lint API; a manual API flag bypasses the lint-enabled guard. SQL detects structural candidates, while up to ten same-category summary pairs feed best-effort model contradiction scanning. Findings persist in activity and return to operator surfaces; no automatic challenged-page rewrite is present in this handler. Distinct from [RT-RTE-source-maintenance](runtime.md#rt-rte-source-maintenance), which changes prose. SRC-1: `cli/src/startup-tasks.ts`, `app/src/app/api/wiki/lint-pass/route.ts`, `app/src/lib/db.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Structured lint findings or skipped; latest timestamp and lint_complete activity written.
- Later read-back: Settings govern the next startup check; latest-result DB helper and operator diagnostics can reread saved findings.
- Delegated visibility: Contradiction model sees selected titles/summary pairs, not full pages or raw sources.
- Selection predicate: Structural SQL plus same-category pair query LIMIT 10; overdue/manual predicates initiate checks.
- Invalidation or expiry: A later lint records another result; the handler does not withdraw challenged content automatically.
- Activation or effect: Diagnostic persistence and saved-links regeneration are wired; semantic correction not observed.
- Evidence limits: Summary disagreement is not verified contradiction; best-effort provider failures can leave an empty contradiction result.

> logActivity('lint_complete', {
> --- `app/src/app/api/wiki/lint-pass/route.ts`

The software/model proposes diagnoses; callers can disable scheduled lint or request manual checking. No expected-answer oracle decides correctness. The open maintenance operation retains findings and timing, not a revised schema. No automatic findings-to-new-maintenance-guidance chain was established; raw diagnostic retention alone is not trace-fed behavioral improvement.

#### MEM-RTE-saved-links
Label: Saved-links trace projection

Failed/unresolved ingestion entries become a deterministic wiki overview at `saved-links`. Code parses optional metadata, trims descriptions to 160 characters and errors to friendly text or an 80-character fallback. It writes DB metadata/FTS/outbox, then attempts Python file flush. This is a trace-fed derived page, distinct from model drafts in [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft). SRC-1: `app/src/lib/saved-links.ts`, `app/src/lib/db.ts`, `app/src/app/api/wiki/lint-pass/route.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Regeneration promise; calling paths can fire-and-forget and flush failure is logged.
- Later read-back: Wiki/FTS selection can expose the saved-links page as unresolved-link knowledge; retained outbox supports startup flush retry.
- Delegated visibility: File service gets deterministic markdown, not original failed input payloads.
- Selection predicate: Current unresolved-links query, invoked after failure/deletion per helper contract and explicitly by lint.
- Invalidation or expiry: Successful ingest or dismissal removes entries from the projection; empty input yields a cleared-state page.
- Activation or effect: Error traces become a readable/retrievable page; later retry decisions or answer benefit unobserved.
- Evidence limits: Error descriptions and peek metadata are not successfully ingested source content; no additional semantic extraction occurs here.

> const links = getUnresolvedLinks();
> const markdown = buildMarkdown(links);
> --- `app/src/lib/saved-links.ts`

Admission is automatic code projection without draft approval. Failure/dismissal state proposes and selects what remains; code owns installation. Operators may dismiss links, but there is no per-generated-page human approval in the helper. No answer oracle or semantic improvement objective is present. Pending content is recovery state; replaced files can be archived by the ordinary writer.

#### MEM-RTE-withdrawal-cleanup
Label: Source and page withdrawal cleanup

Source PATCH changes active/archived status; consumers filtering all-archived source sets suppress those pages from default indexes. Deletion additionally prunes provenance/pending plans. The admin zombie cleanup selects pages lacking valid backing-source joins, deletes DB state and requests best-effort file/vector deletion. This is distinct from [RT-RTE-source-maintenance](runtime.md#rt-rte-source-maintenance)'s redraft branch; it records alternative withdrawal/cleanup entry points and their retained residue. SRC-1: `app/src/app/api/sources/[source_id]/route.ts`, `app/src/lib/db.ts`, `app/src/app/api/admin/cleanup/zombie-pages/route.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Status update, dry-run zombie list, or purge counts.
- Later read-back: Changed indexes/rows alter future default query selection; surviving pending drafts can still hold prose from deleted contributors.
- Delegated visibility: Vector service receives IDs; file cleanup removes matching page files without model interpretation.
- Selection predicate: All backing sources archived for suppression; no valid provenance/source join for zombies, saved-links exempt; source/page ID matching for pending cleanup.
- Invalidation or expiry: Source removal shrinks pending source_ids; empty lists delete plans. Page removal separately handles chat page-ID lists and pending updates targeting the page.
- Activation or effect: Symbolic pruning is wired; physical deletion best effort, semantic removal from surviving prose unestablished.
- Evidence limits: Archive suppresses default indexes, not proven direct-ID access prohibition; cleanup changes ID lists without rewriting surviving draft bodies.

> SET source_ids = (SELECT COALESCE(json_group_array(value), '[]')
> --- `app/src/lib/db.ts:2563-2589`

Initiating archive/delete/purge is caller-controlled; software chooses cascade effects, without per-effect approval. Open maintenance has no answer oracle. A surviving draft's guidance/prose remains unchanged after provenance pruning, so later approval can retain deleted-source semantics. Recompile/source-redraft and outbox recovery have the separate limits in the supplied maintenance route; these are not universal semantic rollback.

#### MEM-RTE-storage-write
Label: Direct storage replacement

Exposed Python `/storage/write-page` and `/storage/write-file` allow a service caller to replace page or data-volume text independently of app approval. Page writes preserve a previous version; generic file writes use direct text overwrite. Distinct from [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval): the endpoint is a storage capability, not another proven consumer loop. SRC-1: `nlp-service/routers/storage.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Current/previous page paths or generic written response; validation/I/O errors otherwise.
- Later read-back: Storage capability only for an unspecified direct caller; existing app schema/page consumers can read changed matching paths, but no independent direct-writer invocation is observed.
- Delegated visibility: Submitted markdown/content, page ID or contained /data path.
- Selection predicate: Caller path/ID, safe-path and request checks; not semantic selection.
- Invalidation or expiry: Generic write replaces contents without the page archive protocol; DB/FTS/vector reconciliation is not supplied by this generic write.
- Activation or effect: Filesystem replacement wired; admission into consistent app metadata or changed model behavior unobserved.
- Evidence limits: API exposure does not establish a deployed caller, human review or a service-internal knowledge consumer.

> with open(resolved, "w", encoding="utf-8") as f:
>     f.write(req.content)
> --- `nlp-service/routers/storage.py`

Caller proposes content; software validates location/shape and writes. There is no model decision, answer oracle or semantic veto in the inspected handler. Recovery differs by endpoint: archived prior page versus generic overwrite. Thus unknown direct-writer control does not erase known subsequent app reading, but prevents attributing all installed schema/page content to compile generation.

### Claims

#### MEM-CLM-chat-provenance
Label: Chat draft provenance blocks ordinary adoption

The source advertises chat compounding through pending drafts, but a nonempty ordinary pages-used list prevents shared approval when its page IDs are not also existing source IDs. `insertChatDraft` writes pages_used into `page_plans.source_ids`; `commitSinglePlan` interprets those strings as source IDs and inserts provenance. Shipped schema references `sources(source_id)` and the app enables foreign keys. The transaction catch returns commit_failed. This narrows, rather than denies, the feedback affordance in [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback) and [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval). SRC-1: `app/src/lib/db.ts`, `app/src/lib/approve-plan.ts`, `scripts/migrate.py`.

> .run(data.plan_id, data.session_id, data.title, JSON.stringify(data.pages_used ?? []), data.draft_content);
> --- `app/src/lib/db.ts`

> insertProvenance({ source_id: sid, page_id, content_hash: contentHash, contribution_type: contribType });
> --- `app/src/lib/approve-plan.ts`

> source_id TEXT NOT NULL REFERENCES sources(source_id),
> --- `scripts/migrate.py:45-52`

> _db.pragma('foreign_keys = ON');
> --- `app/src/lib/db.ts`

Countercases bound the finding: a manual save with empty citations has no IDs to insert, and imported or deliberately coincident source/page IDs can satisfy the foreign key. Such exceptions do not repair ordinary page-based provenance. No execution failure was observed; this is an implementation-level constraint, not a measured failure rate.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-page-plans](runtime.md#rt-obj-page-plans)

Its `draft_content` payload is natural-language derived memory stored in SQLite, separate from symbolic status/action/IDs. Later approval and layer-summary extraction reread that payload. Rejection changes status and retains prose for audit, not automatic corrective learning. Source deletion can prune symbolic lineage without changing prose. SRC-1: `app/src/app/api/drafts/[plan_id]/reject/route.ts`, `app/src/lib/db.ts`; supplied draft route.

> updatePlanStatus(plan_id, 'rejected');
> --- `app/src/app/api/drafts/[plan_id]/reject/route.ts`

#### On [RT-OBJ-schema](runtime.md#rt-obj-schema)

Storage is natural-language `/data/schema.md`, not database schema. Initial generated lineage is committed-page metadata; import/direct file replacement add alternative lineage. Normal bootstrap retains one document, and later drafting requests conventions without an enforcement proof. No actual schema sample or retained rationale instance is supplied; the requested rule content is inspectable in the runtime schema record, but criticism and rationale consumers are not established. SRC-1: `nlp-service/routers/storage.py`, `nlp-service/services/llm_client.py`; [RT-RTE-schema-bootstrap](runtime.md#rt-rte-schema-bootstrap).

#### On [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft)

Each page call isolates selected inputs in a new model request: return prose persists, not a continuing agent context. Raw text, existing page, schema and extracted dossiers remain externally reachable by explicit code reads. Earlier-layer summaries are lossy derivatives supplied to later invocations; original-source pages avoid the drafting model. Dossier caps do not necessarily remove the corresponding raw source documents: the call separately supplies sourceContents and the capped dossier. Source prefix truncation is therefore a different budget mechanism. SRC-1: `app/src/app/api/compile/draft/route.ts`, `nlp-service/services/llm_client.py`; scoped call-site inspection and supplied route passages.

The drafting consumer is told to prefer pre-extracted data, present contradictory source data alongside it, and retain existing page content on updates. This gives derived content requested epistemic priority, not a demonstrated trust guarantee.

> IMPORTANT: Prefer the pre-extracted data above for key facts, types,
> --- `nlp-service/services/llm_client.py`

The prompt orders schema and existing prose before raw documents; prefix truncation preferentially loses later sources while separately appended category guidance survives. This resembles an isolated call frame with selected inputs and a returned value, but external retained text must be copied into a later window; a source ID is not a live model-memory reference. No host compaction or provider-hidden checkpoint behavior was inspected.

#### On [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback)

Selection receives a lightweight title/summary index, not full wiki bodies. Small-index choice is model-mediated; large-index selection merges FTS/vector scores, source counts and recency. Popular-page fallback is not proof of topical relevance. File retrieval first clips to 8000 characters, then synthesis receives 2000-character top-five prefixes and 300-character lower-ranked prefixes, not actual extracted summaries. Python assembles history before pages and question, then prefix-truncates the entire user prompt. Very large retained history text can therefore evict page text or even the trailing question. SRC-1: `app/src/lib/retrieval.ts`, `app/src/app/api/chat/route.ts`, `nlp-service/services/llm_client.py`.

> f"{history_text}"
> f"Wiki pages:\n\n{pages_text}\n\n"
> f"---\n\n"
> f"Question: {question}"
> --- `nlp-service/services/llm_client.py`

The system prompt requests wiki-only answers. It does not establish reliable separation of untrusted source/page prose from instruction-like content or validate factual entailment of citations. The returned answer is natural-language trace content; automatic FAQ creation counts selected readable pages, not verified use. No improved future capacity follows from storing this result, and ordinary adoption has the provenance constraint above. History-tail claims are corrected by [MEM-RTE-history-read](#mem-rte-history-read).

#### On [RT-BAP-wiki-answering](runtime.md#rt-bap-wiki-answering)

Authority differs by consumer: answer models receive requested evidence in a clipped user prompt, external agents receive an explicitly requested tool result, and humans receive displayed page prose. Provider compliance and client prompt inclusion remain unobserved. Read-by-ID targeting is exact object lookup, whereas chat query selection uses question/index/ranking inputs. Tool result delivery is not unsolicited memory injection. SRC-1: `app/src/app/api/chat/route.ts`, `nlp-service/services/llm_client.py`; supplied MCP route.

## Write side

The ordinary acquisition/drafting/admission chain is [RT-RTE-session-compile](runtime.md#rt-rte-session-compile) → [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft) → [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval). Selecting an input or starting compile is not approving each generated page. Software retains raw conversion, extraction, aliases and mention evidence before prose admission. Models author derived prose; code writes files and status. Auto-approval and explicit pending approval differ; rejection retains the proposal rather than deriving another rule from rejection reasons. Caller identity leaves actual human review unresolved.

Alternate admission matters. Source deletion can install a model redraft without the compile approval gate or schema/old-page context; short-source deletion can preserve old prose plus a note. Import restores caller-supplied pages/settings/schema/vectors directly. Direct storage can replace files without app metadata reconciliation. Saved-links generation admits a deterministic error-trace projection without a model or draft gate. SRC-1 support is in [RT-RTE-source-maintenance](runtime.md#rt-rte-source-maintenance), [RT-RTE-archive-import](runtime.md#rt-rte-archive-import), [MEM-RTE-storage-write](#mem-rte-storage-write), [MEM-RTE-saved-links](#mem-rte-saved-links).

Trace-fed paths must not be conflated. Chat keeps raw questions/answers, creates derived FAQ/manual draft prose, and proposes it for later page consumption; ordinary adoption has a foreign-key constraint. Saved-links converts failed-ingest records and metadata into a later readable wiki page. Lint/triage retains judgments and reasons for operator/sidebar consumers, not an inspected automatic rule revision. Page compaction by source synthesis and layer summaries yields derived content for later calls, while chat history selection discards window entries without a new summary/checkpoint artifact. No alternative provider checkpoint form is inspectable; provider hidden state remains unknown, not absent.

Curation requests attribution, contradiction notes, coherent synthesis and conventions. Those prompts are not evidence that generated meaning changed correctly. Provenance links identify contributing material, not necessarily retained justification for every derived claim. Triage reasons have a later sidebar reader; query draft citation links persist but do not preserve provider reasoning. Generated schema rationale and its actual later reading remain uninspected. Source-dependent evidence: [MEM-OBJ-activity-log](#mem-obj-activity-log), schema annotation and supplied schema route.

## Read-back

- **Later compile:** source-ID lookup copies raw text and extraction data; historical mention counts/aliases select candidates; previous page prose and schema enter drafting. TF-IDF dossier caps, known-title cap and prompt prefix budget bound delivered evidence. Symbolic planning authority and requested prose-instruction authority differ. [MEM-OBJ-mentions](#mem-obj-mentions), plan/draft annotation.
- **Question answering:** question-driven index or hybrid selection → readable page files → clipped prose/history → synthesis. Retained FTS/vector candidates are selection aids, not full model evidence. Missing/unflushed files are skipped. Metadata bypass returns database facts without synthesis. [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback), [MEM-RTE-history-read](#mem-rte-history-read).
- **Human/external agent:** wiki/MCP explicit read/list/search returns current prose and provenance; previous endpoint returns a validated prior version. The external client owns when/what to read and its eventual authority. This is pull, not independently unsolicited delivery. [RT-RTE-mcp-read](runtime.md#rt-rte-mcp-read), [MEM-OBJ-pages](#mem-obj-pages).
- **Recovery/maintenance:** retained outbox, plan/progress states and last-run settings affect flush/retry/overdue operations. Contradiction reasons/lint results inform display. Old archives afford inspection, not automatic semantic reversion. [RT-CLM-durable-completion](runtime.md#rt-clm-durable-completion), [MEM-RTE-lint-retention](#mem-rte-lint-retention).

The automatic selector used for answering is nested inside a question request, not an unsolicited push. Automatic saved-links maintenance and startup lint are triggered by code/events, but later model consumption still requires a query or compile call. No deployed independent push of wiki content to an external agent was supplied.

## Integration issues

1. **History correction:** [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback) and its runtime prose claim ten prior/last messages. [MEM-RTE-history-read](#mem-rte-history-read) directly establishes earliest ascending rows and removal of the last selected row. Update all tail-based context conclusions; stored older/newer rows are not deleted.
2. **Adoption qualification:** [RT-RTE-chat-feedback](runtime.md#rt-rte-chat-feedback) and [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval) imply approval can close normal query feedback. [MEM-CLM-chat-provenance](#mem-clm-chat-provenance) establishes the ordinary nonempty page-ID foreign-key obstruction. Preserve the pending-draft affordance and empty/coincident-ID countercases; do not mark successful automatic compounding as wired end-to-end without this constraint.
3. **Additional admission path:** [MEM-RTE-manual-save](#mem-rte-manual-save) bypasses the three-retrieved-page trigger. It converges on the supplied approval route but has distinct submitted-content control and is not a duplicate of the automatic route.
4. **Reason/lineage discrepancy:** [MEM-OBJ-activity-log](#mem-obj-activity-log) retains triage reason/title/URL, but the contradiction helper reads source_id from JSON details whereas plan writes it on the outer activity row. This limits complete returned structured lineage; it does not erase readable reasons. SRC-1: `app/src/lib/db.ts`, `app/src/app/api/compile/plan/route.ts`.
5. **Withdrawal limits:** source archival default-query suppression does not prove removal from historical mention counts, direct-ID access, or surviving prose. Pending source-ID pruning does not rewrite draft bodies. [MEM-OBJ-mentions](#mem-obj-mentions), [MEM-RTE-withdrawal-cleanup](#mem-rte-withdrawal-cleanup), [RT-RTE-source-maintenance](runtime.md#rt-rte-source-maintenance).
6. **Opaque/imported lineage:** original generation model/content provenance of imported vectors, actual generated schema rationale and provider-hidden context are unresolved. [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages), [RT-OBJ-schema](runtime.md#rt-obj-schema). Prevents attributing all retained material to ordinary compile or claiming rationale-guided learning.
7. **Record identity:** history is explicitly a material part of the supplied chat route. New stores are distinct from supplied control plans/schema/components, as compared in their declarations. Manual save, lint, saved-links, cleanup and direct storage are additional entry points, not renamed supplied routes. No possible duplicate requiring supersession identified; component and schema identities were reused through annotations.

## Limitations and checks

HEAD was directly rechecked as `17970c969b0c2576bf722840e0e2db3c6416a7aa`; source identity and run identity match the supplied boundary/invocation. Only source text/search and Commonplace validation were used. No target tests/providers/services ran. One combined source search returned code 2 because `app/src/app/drafts` does not exist; its positive results were retained only as search evidence, not as a complete UI audit. Files intentionally read in bounded ranges are not claimed fully audited.

Inspected source supports wiring and the named countercases, not observed recovery, factual accuracy, exercised influence, semantic withdrawal or improved future capacity. Evaluators are covered through supplied boundary evidence only; unavailable exact corpus prevents replication. UI editing affordances, exhaustive ingestion converters, complete export assertions and historical result payloads were not independently inspected, preventing exhaustive claims about editing, source fidelity, backup coverage and evaluation outcomes. Shipped service replacement operations are covered as capabilities without fabricated external consumers. No negative claim about inaccessible provider memory is made.

Validation: deterministic validate-output check passed; this establishes structure, identity and quotation occurrence, not semantic acceptance or operation.
