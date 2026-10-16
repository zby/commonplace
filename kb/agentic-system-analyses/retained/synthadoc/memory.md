---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Synthadoc memory: compiled wiki content, route-specific admission, trace ingestion, session truncation, audit-derived state and alternate consumers."
run-id: AAS-2026-10-15-synthadoc-a3cae9152fff-01
source-identity: https://github.com/axoviq-ai/synthadoc
reviewed-boundary: b80d9388a3013e8051baf2854c7250942c46e91a
---

# Synthadoc memory report

## Boundary and evidence

Synthadoc retains editable knowledge in Markdown, reloads it for question answering and maintenance, and exposes alternative delivery through context packs, direct reads, cross-wiki retrieval and exports. This account uses SRC-1 at the commit fixed by [boundary](boundary.md). Its whole-system boundary includes the server, CLI, MCP, shipped clients and exported-bundle consumer. External coding-agent context, provider-side state, actual deployed files and model compliance remain outside inspectable operation. No target program, test, example or provider was executed.

Direct source reads extend the initial boundary inventory. The supplied runtime is evidence of prior inspection, not proof of completeness. The table distinguishes direct inspection from supplied findings. Every source path below belongs to SRC-1 and supplies implementation evidence unless marked doctrine. Uninspected material remains included; uncertainty is not an access gap.

| Entry point or operation | Source paths and inspection basis | Records, limits and conclusion prevented |
|---|---|---|
| CLI/HTTP/MCP ingest, force, staging, child sources | Direct: `synthadoc/agents/ingest_agent.py`; supplied dispatch: `synthadoc/cli/ingest.py`, `synthadoc/integration/http_server.py` | [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission), [MEM-OBJ-page-content](#mem-obj-page-content), [MEM-OBJ-source-sidecars](#mem-obj-source-sidecars). Detailed behavior of every extraction skill remains uninspected; extracted text need not be verbatim source. |
| Trace-file admission | Direct: `synthadoc/skills/session/scripts/main.py` | [MEM-RTE-session-ingest](#mem-rte-session-ingest). Filtered imported transcripts, not automatic learning from every local interaction. |
| Persist/reload page body and metadata | Direct: `synthadoc/storage/wiki.py` | [MEM-OBJ-page-content](#mem-obj-page-content), [MEM-OBJ-page-metadata](#mem-obj-page-metadata). Store I/O itself is not a later-consumer route. |
| Query, search, vectors, context pack, direct MCP read | Direct: `synthadoc/storage/search.py`, `synthadoc/agents/context_agent.py`; supplied query/MCP constructors and body handling: `synthadoc/agents/query_agent.py`, `synthadoc/core/orchestrator.py`, `synthadoc/integration/mcp_server.py` | [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [RT-RTE-context-export](runtime.md#rt-rte-context-export), [MEM-OBJ-search-vectors](#mem-obj-search-vectors). External MCP host consumption is afforded, not observed. |
| Session history, summarization, cached answers | Direct: `synthadoc/integration/http_server.py`, `synthadoc/storage/log.py`, `synthadoc/agents/summarize_agent.py`, `synthadoc/core/cache.py` | [MEM-RTE-session-context](#mem-rte-session-context), [MEM-OBJ-response-cache](#mem-obj-response-cache). Summary creation does not establish summary delivery. |
| Cross-wiki retrieval and synthesis | Direct: `synthadoc/agents/cross_wiki_query_agent.py`, `/retrieve` and cross-wiki handlers in `synthadoc/integration/http_server.py` | [MEM-RTE-cross-wiki](#mem-rte-cross-wiki). Peer contents, registry initialization and all peer-cache invalidation paths are not audited. |
| Lint, model repair, direct write, lifecycle, candidate discard | Supplied: `synthadoc/agents/lint_agent.py`, `synthadoc/integration/mcp_server.py`, candidate handlers; direct lifecycle contracts: `synthadoc/storage/wiki.py` | [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair), [RT-RTE-client-write](runtime.md#rt-rte-client-write), [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission). No universal approval or state gate. Complete adversarial gate internals remain uninspected. |
| Content-health fix, dismissal and rollback | Direct: `synthadoc/agents/workflows/tools/content_health_tools.py`; supplied gate/loop | [MEM-RTE-health-history](#mem-rte-health-history), [RT-RTE-workflow-loop](runtime.md#rt-rte-workflow-loop). Other workflow-specific retention/recovery branches are not exhaustively audited. |
| Faithfulness evaluation and retained verdicts | Direct: `synthadoc/agents/citation_faithfulness_agent.py`, `synthadoc/agents/faithfulness_cache.py`, `synthadoc/core/orchestrator.py`, cache GET handler | [MEM-RTE-faithfulness-audit](#mem-rte-faithfulness-audit). Verdict display and re-audit selection are supported; automatic factual repair from these verdicts is not established. |
| Sensitive-data withdrawal | Direct: `synthadoc/core/retract.py`, `synthadoc/cli/retract.py`, background/post-ingest handlers | [MEM-RTE-sensitive-mask](#mem-rte-sensitive-mask). Page masking is not erasure from old snapshots, sidecars, exports or caches. |
| Scaffold, purpose, instructions, index, routing, overview | Direct: `synthadoc/agents/scaffold_agent.py`, `synthadoc/core/orchestrator.py`, `synthadoc/cli/_init.py`, overview producer in ingest; supplied streaming routing consumer | [MEM-RTE-scaffold-guidance](#mem-rte-scaffold-guidance), [MEM-OBJ-overview](#mem-obj-overview). External instruction loading and overview-to-model delivery are not established. Templates/demos supply possible initial content, not observed initialization. |
| Export and shipped OKF consumer | Direct bundle selection/context in `tests/integration/okf_consumer_agent.py`; supplied export filters/rendering: `synthadoc/core/export.py` | [RT-RTE-context-export](runtime.md#rt-rte-context-export). No universal interoperability or source-fidelity result follows from the demo. |
| Backup and restore | Direct: `synthadoc/core/backup_engine.py` | [MEM-RTE-backup-restore](#mem-rte-backup-restore). Caller admission and complete live-server coherence after restore remain uninspected. |
| Scheduled operations, hooks and provider-native tools | Supplied: `synthadoc/core/scheduler.py`, `synthadoc/core/hooks.py`, `synthadoc/providers/coding_tool.py`, `synthadoc/agents/skill_agent.py` | [RT-RTE-scheduled-operation](runtime.md#rt-rte-scheduled-operation), [RT-RTE-extension-loading](runtime.md#rt-rte-extension-loading), [RT-RTE-provider-delegation](runtime.md#rt-rte-provider-delegation). Hook-written state and opaque host checkpoints have unresolved contents/consumers. |
| Client reload and evaluators | Supplied boundary inventory: `web-ui/src/api.ts`, `obsidian-plugin/src/api.ts`, `docs/example/aquaflow/evaluation/scripts/eval_queries.py`; direct source searches of `obsidian-plugin/src/main.ts` | Session and verdict display affordances; no inspected feedback-to-method update from benchmark scores. Full client/evaluation behavior remains uninspected, preventing an exhaustive feedback-loop claim. |

## Core ideas

1. **The wiki is derived knowledge, not a replay log.** Ingest interprets clipped source and selected old pages, then changes the library through action dispatch. Retained provenance identifies source files, hashes and ingestion times; it is not the model's complete reasoning. Imported session traces can take the same path, but exclude tool results and thinking blocks. See [MEM-OBJ-page-content](#mem-obj-page-content) and [MEM-RTE-session-ingest](#mem-rte-session-ingest).
2. **Eligibility is consumer-specific.** Ordinary search admits active/stale; cross-wiki `/retrieve` further requires active; default OKF export includes active/contradicted; direct reads use explicit slugs. Neither staging nor lifecycle provides one universal knowledge-admission gate. The forcing counterexamples in [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-client-write](runtime.md#rt-rte-client-write) and [RT-RTE-context-export](runtime.md#rt-rte-context-export) defeat that stronger claim.
3. **Persistence, selection and authority are separate.** Body text shapes model interpretation when explicitly retrieved; lifecycle and routing data change software selection. Vector blobs rerank rather than encode authoritative page facts. A cached answer can bypass synthesis altogether. See [MEM-OBJ-search-vectors](#mem-obj-search-vectors), [MEM-OBJ-response-cache](#mem-obj-response-cache) and [MEM-BAP-retained-content](#mem-bap-retained-content).
4. **Not every derived artifact closes a memory loop.** Session summaries are persisted, but the inspected local streaming handler supplies only the recent raw tail. Faithfulness verdicts retain reasons and control stale-only re-audit selection, but no inspected query consumer uses those reasons. A summary label, audit label or successful storage operation is insufficient evidence of later model consumption. See [MEM-RTE-session-context](#mem-rte-session-context) and [MEM-RTE-faithfulness-audit](#mem-rte-faithfulness-audit).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-page-content
Label: WikiPage content

Natural-language knowledge, source-derived quotations and Markdown links reside in `wiki/<slug>.md`; `WikiStorage` serializes the body and reparses it on read. This is a distinct retained product of [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), not another declaration of that route. No supplied object record has this identity. Content may be model-written, caller-edited, imported or restored; physical I/O does not determine authorship. Query synthesis, maintenance models, context packs, direct readers and export are different consumers. The readable page is not an opaque checkpoint. Reasons may occur in its prose, but storage does not require a derivation rationale (SRC-1, `synthadoc/storage/wiki.py`, `synthadoc/agents/ingest_agent.py`; downstream routes cited above).

> body = parts[2].lstrip("\n")
> --- `synthadoc/storage/wiki.py`

#### MEM-OBJ-page-metadata
Label: WikiPage frontmatter

YAML frontmatter on the same file is a separate operative part: symbolic lifecycle/status, timestamps, aliases, categories, source pointers/hashes/sizes and fix/snapshot identifiers have fixed parser consumers. Tags/titles also feed tokenization. Contradiction notes, unresolved notes and dismissal reasons are natural-language subfields consumed through interpretation or display, not factual truth flags. `SourceRef.truncated` reports ingest clipping; file/hash/size/ingested provide lineage and deduplication inputs, not proof that all source assertions survive compilation. No supplied object counterpart; the closest route is [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). Storage is inspectable Markdown/YAML, not a weight update (SRC-1, `synthadoc/storage/wiki.py`, `synthadoc/storage/search.py`).

> file: str
> hash: str
> size: int
> ingested: str
> --- `synthadoc/storage/wiki.py`

Lifecycle validation is explicitly narrower than all writes:

> # Lint and ingest write status via write_page() directly and bypass this check.
> --- `synthadoc/storage/wiki.py`

#### MEM-OBJ-source-sidecars
Label: Extracted source sidecars

`.synthadoc/extracted/<name>.txt` and PDF pagemaps retain extraction output before ingest sanitization and clipping. Text is readable natural language; pagemaps and citation line locators are symbolic access metadata. A skill may already have transformed the source, so these are not necessarily raw originals. Source Viewer is the documented consumer in code comments; citation faithfulness additionally resolves sidecars. Raw originals remain separate local files or remote sources; their availability and immutability are not guaranteed by a source pointer. No supplied object counterpart; closest production route is [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) (SRC-1, `synthadoc/agents/ingest_agent.py`, `synthadoc/agents/citation_faithfulness_agent.py`, `synthadoc/core/backup_engine.py`).

> (extracted_dir / f"{name}.txt").write_text(text, encoding="utf-8", newline="\n")
> --- `synthadoc/agents/ingest_agent.py`

#### MEM-OBJ-search-vectors
Label: VectorStore embeddings

Dense distributed numerical page representations reside as float32 blobs in SQLite, separately from readable page text and in-process BM25 token lists. `embed_page` derives each from at most 512 characters of supplied text. The configured embedding model is already [RT-CMP-text-embedding](runtime.md#rt-cmp-text-embedding); this record is its derived data, not the model or its weights. Query embeddings compare against stored page vectors only for BM25 candidates. Substrate persistence and changed embeddings establish neither model training nor fact preservation. Initial population and refresh completeness after every alternate edit are unresolved (SRC-1, `synthadoc/storage/search.py`).

> embedding = await loop.run_in_executor(None, self._embed_text, text)
> await self._vector_store.upsert(slug, embedding)
> --- `synthadoc/storage/search.py`

#### MEM-OBJ-response-cache
Label: CacheManager retained responses

SQLite `response_cache` contains JSON analysis/decision results and citation annotation strings; `query_cache` contains JSON answer/citation/gap results. Symbolic keys and fields control lookup/dispatch; natural-language cached sections and answers retain model text. These are derived computational products, distinct from original source, conversational logs and vector representations. Closest supplied routes are [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query); neither declares the stored object. Ingest decision cache omits candidate bodies from its key. Query keys normalize question and include epoch/model but not session/history. Cache hits substitute previous decisions or deliver previous answers without a new semantic judgment. Explicit clearing and query cleanup exist; lookup itself has no age test (SRC-1, `synthadoc/core/cache.py`, `synthadoc/agents/ingest_agent.py`, `synthadoc/integration/http_server.py`).

> normalized = " ".join(question.lower().split())
> payload = f"{normalized}|{epoch}|{model}"
> --- `synthadoc/core/cache.py`

> SELECT result_json FROM query_cache WHERE cache_key=?
> --- `synthadoc/core/cache.py`

#### MEM-OBJ-chat-messages
Label: AuditDB chat messages and summary

SQLite chat messages preserve user/assistant text, roles, citations and gap suggestions under session IDs. Natural-language turns are raw interaction records relative to summarization; role/order/session/citation fields are symbolic access metadata. `history_summary` is a separate natural-language model-derived value with `summary_turn_count` metadata. Both remain readable, unlike an opaque provider checkpoint. The recent raw tail has a synthesis consumer; a summary-to-synthesis path is not established by the inspected handler. No supplied object counterpart; closest route [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query). See [MEM-RTE-session-context](#mem-rte-session-context) for the distinction between durable retention and model visibility (SRC-1, `synthadoc/storage/log.py`, `synthadoc/integration/http_server.py`).

> "UPDATE chat_sessions SET history_summary=?, summary_turn_count=? WHERE session_id=?",
> (summary, covered_turns, session_id),
> --- `synthadoc/storage/log.py`

#### MEM-OBJ-lifecycle-history
Label: AuditDB lifecycle snapshots and fix records

SQLite lifecycle events retain state transitions, reason, trigger, timestamp and optional body-only `content_snapshot`. The snapshot is natural-language page content; IDs, state transitions and timestamps are symbolic recovery metadata. `WikiPage.content_health_fix_record` points to a pre-fix snapshot and records issue types/time; dismissal can add a reason without changing the body. This is distinct from [MEM-OBJ-page-content](#mem-obj-page-content) and from [RT-RTE-workflow-loop](runtime.md#rt-rte-workflow-loop). Snapshot access alone is storage capability; [MEM-RTE-health-history](#mem-rte-health-history) supplies an actual recovery consumer. A stable snapshot ID is preferable to a moving index, but the implementation falls back to an index if ID resolution fails. Full page frontmatter restoration is not implied (SRC-1, `synthadoc/storage/log.py`, `synthadoc/agents/workflows/tools/content_health_tools.py`).

> restored_content = snapshot["content_snapshot"]
> page.content = restored_content
> page.content_health_fix_record = None
> --- `synthadoc/agents/workflows/tools/content_health_tools.py`

#### MEM-OBJ-faithfulness-cache
Label: Citation faithfulness cache

`.synthadoc/faithfulness-cache.json` stores per-slug citation marker, model verdict, short reason, check time and page key. Reasons are natural language; verdict/key/time fields drive fixed display and staleness rules. This is derived evaluation material, not corrected page content or an expected-answer oracle. No supplied object counterpart; [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair) mentions the responsibility but is not this audit object. Its consumer paths are declared in [MEM-RTE-faithfulness-audit](#mem-rte-faithfulness-audit) (SRC-1, `synthadoc/agents/faithfulness_cache.py`).

> "citation_marker": r.citation_marker,
> "verdict": r.verdict,
> "reason": r.reason,
> --- `synthadoc/agents/faithfulness_cache.py`

#### MEM-OBJ-overview
Label: Generated wiki overview

`wiki/overview.md` is natural-language model output generated from the ten most recently modified non-system pages, each represented by the first 200 characters of its raw file. It is not a full-corpus or source-faithfulness summary: raw prefixes can include frontmatter. It is automatically written with active/high labels, not validated by those labels. Production is directly wired; a later model consumer of this overview is unestablished in the inspected paths. No supplied object counterpart; closest producer [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). Ordinary search excludes system pages, so overview existence cannot establish implicit injection into ordinary synthesis (SRC-1, `synthadoc/agents/ingest_agent.py`, `synthadoc/storage/wiki.py`, `synthadoc/storage/search.py`).

> page_ctx = [f"- {p.stem}: {p.read_text(encoding='utf-8')[:200].replace(chr(10), ' ')}"
>                 for p in pages]
> --- `synthadoc/agents/ingest_agent.py`

### Routes

#### MEM-RTE-session-ingest
Label: Imported session transcript compilation
Part of: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

This specializes source ingest for JSONL session files. Caller supplies a file; SessionSkill code detects a format, selects substantial user/assistant text and renders chunks; ingest then interprets and admits derived pages through its usual policy. Claude sidechains and non-user/assistant records are discarded; tool_use, tool_result, thinking and image blocks are excluded. Minimum word counts are 20 for assistant and 3 for other retained turns; chunks have at most 30 turns but are joined into one extraction result, not independently guaranteed model windows. Original provenance mixes human and model utterances, not verified environment outcomes. Format names do not authenticate trace origin (SRC-1, `synthadoc/skills/session/scripts/main.py`).

Admission follows the parent route: code/model decide create/update/flag/skip; caller starts ingest but per-result human editing/approval is unresolved. Staging/discard and force alternatives remain applicable. No expected-answer oracle or bounded improvement experiment is used; fixed ingest guidance shapes open compilation. Recovery uses parent history/re-ingest, not a transcript-specific rollback. This is a trace-fed knowledge write that can shape future answers, not demonstrated improvement or method revision.

- Immediate return: ExtractedContent with filtered text, format, turn count and suggested slug; parent ingest later returns changed pages/jobs.
- Later read-back: derived admitted pages can enter later eligible queries; original JSONL is a separate source, not automatically replayed into query.
- Delegated visibility: ingest receives rendered retained text and metadata, then sanitizer/clipping and snippets constrain its calls.
- Selection predicate: supplied JSONL, detected format, role/block/sidechain filters, minimum words, then parent ingest/search/staging rules.
- Invalidation or expiry: re-ingest/force/cache controls and later page edits; no automatic synchronization to subsequent transcript changes is established.
- Activation or effect: extraction and page-admission path are wired; future interpretation can use retained page content, but actual behavioral dependence is unobserved.
- Evidence limits: excluded tools/thinking mean a page is not a full execution trace; neither accurate experience extraction nor increased capacity is observed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> _SKIP_BLOCK_TYPES = frozenset(("tool_use", "tool_result", "thinking", "image"))
> --- `synthadoc/skills/session/scripts/main.py`

#### MEM-RTE-session-context
Label: Session tail selection and overflow summary

On local `/query/stream`, server code reloads stored messages, keeps the latest configured number of pairs, and may ask SummarizeAgent to summarize older turns. Code automatically admits a nonempty summary to the session row; the caller supplies session identity, not per-summary approval. The prompt requests 2–3 sentences preserving facts, names, decisions and unresolved questions. There is no answer oracle, semantic check or user veto in this branch. A subsequent overflow regenerates from old raw messages rather than incrementally reading a prior summary as content. No deletion of raw messages occurs in this compression branch (SRC-1, `synthadoc/integration/http_server.py`, `synthadoc/agents/summarize_agent.py`, `synthadoc/storage/log.py`).

Critically, `_history` remains the raw recent tail. The stored summary and covered-count are read to decide whether another summary is due and whether to display a notice. They are not appended to `_history` before `orch.query_stream`. Thus the trace-to-summary write is wired, but summary-to-answer memory is not established. The actual later model-visible trace path is raw-tail reload followed by QueryAgent character trimming. Cache hits may bypass that model call altogether ([MEM-OBJ-response-cache](#mem-obj-response-cache)). This extends, rather than duplicates, [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) with HTTP/session retention and selection before its endpoint.

- Immediate return: selected history to orchestrator; optional summary notice; answer/SSE; stored summary and new chat messages.
- Later read-back: subsequent session queries reload raw messages; prior summary/count are read by overflow control, not shown as synthesis content in this handler.
- Delegated visibility: summary model gets role/text rendering of overflow messages, not citation/gap columns; answer model gets recent history subject to further character trimming, not the summary here.
- Selection predicate: explicit session ID, positive conversation_history_turns, recent turns*2 messages, and increased overflow count for summarization.
- Invalidation or expiry: later overflow replaces summary; failure leaves existing state; raw-history trimming affects windows rather than deleting durable messages.
- Activation or effect: code persists derived summary and passes recent raw history; actual answer dependence on history is unobserved.
- Evidence limits: summary storage and notice do not demonstrate successful long-conversation recall; session deletion and every nonstreaming/client path are not exhaustively inspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> _history = _all_messages[-(turns * 2):]
> --- `synthadoc/integration/http_server.py`

> await _audit.update_summary(session_id, _new_summary, _overflow_turns)
> --- `synthadoc/integration/http_server.py`

#### MEM-RTE-cross-wiki
Label: Cross-wiki retained-page retrieval

HTTP cross-wiki driver supplies registry and question to CrossWikiQueryAgent. Code tries retained `CROSS_WIKI_ROUTING.md` keyword rules, otherwise asks a model to pick wikis from registry purpose summaries; fallback can use all, and own wiki is included. Concurrent `/retrieve` calls return retained active page bodies (at most 8000 characters each, top_k clamped to 1–20). Hybrid retrieval uses question or supplied subquestions. Coordinator merges scores and builds up to 80000 characters, potentially truncating the final page; history is trimmed to 4000 characters. A new model call receives this context and purpose summaries (SRC-1, `synthadoc/agents/cross_wiki_query_agent.py`, `synthadoc/integration/http_server.py`).

This is a distinct multi-store request/selection/delivery chain, not the local route [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) or export route [RT-RTE-context-export](runtime.md#rt-rte-context-export). Source trust remains page-content interpretation: the synthesis prompt requests page-only answers, but compliance and cross-peer authenticity are not established. Registry author and initialization authority are unresolved; subsequent runtime model routing is known. No knowledge write, per-content approval or answer oracle is supplied by this retrieval operation. Server retains session answers and can cache results; the cross-wiki cache key uses peer epochs/model/question, while a hit can occur even with prior history.

- Immediate return: synthesized QueryResult or SSE, offline/skip metadata, or cached answer.
- Later read-back: retrieves pages retained by earlier wiki operations and may append answer/history for subsequent session calls.
- Delegated visibility: each peer receives question/subquestions/top_k, not entire coordinator history; synthesis receives merged budgeted pages, scopes and trimmed history.
- Selection predicate: routing rules or model-selected registered wiki names, own-wiki inclusion, per-peer retrieval and active check, merged score order and character cap.
- Invalidation or expiry: fresh calls reread peers unless cached; peer epoch coverage, registry freshness and synchronization with all writers remain unresolved.
- Activation or effect: page text is delivered to completion or cached result delivered to client; semantic reliance is unobserved.
- Evidence limits: rankings from different peer corpora are merged without evidence of calibration; offline peers and truncation prevent complete-corpus answers.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if page and page.status == LifecycleState.ACTIVE:
> --- `synthadoc/integration/http_server.py`

> selected.append(self._own_wiki_name)
> --- `synthadoc/agents/cross_wiki_query_agent.py`

#### MEM-RTE-health-history
Label: Content-health fix history and rollback
Part of: [RT-RTE-workflow-loop](runtime.md#rt-rte-workflow-loop)

The guarded content-health tool reads current page content, snapshots it before replacing the body, records snapshot ID and issues_fixed in frontmatter, rescans, writes and bumps epoch. The model proposes edits; the workflow wrapper supplies the applicable per-call client gate described in the parent. A separate dismissal tool clears issue metadata and retains a reason without body changes or snapshot; its prompt asks for prior notification, which alone is not approval enforcement. Later list-fixes/rollback tools reload retained fix metadata. Rollback resolves stored ID to its current index, falls back to the recorded index, reads the snapshot, restores body, clears fix record and rescans. No expected factual answer is supplied: structural scan results are checks, not an oracle (SRC-1, `synthadoc/agents/workflows/tools/content_health_tools.py`).

This writes trace-derived recovery/control material and revised product text. The retained issues/reasons are not a learned general repair rule. Rollback demonstrates an implemented consumer rather than merely a snapshot API. Full historical metadata restoration, concurrency safety and recovery of each other workflow remain unestablished.

- Immediate return: status, snapshot identity, remaining issue count/fix record; rollback returns restored snapshot index.
- Later read-back: list/rollback reload fix records and snapshot content; normal queries can read the revised or restored page once eligible.
- Delegated visibility: model tools receive explicit slugs/content/issue lists; snapshot body is delivered through restoration to page storage, not automatically added to every model window.
- Selection predicate: explicit slug; guarded discovery/read requirements in the parent; stored snapshot ID/index for recovery; deterministic rescan of changed/restored body.
- Invalidation or expiry: later fix can replace the current fix record; rollback clears it; missing snapshot returns error and index fallback can be ambiguous.
- Activation or effect: approved fix and rollback branches write persistent content and bump epoch; structural rescanning is implemented, factual improvement is unobserved.
- Evidence limits: issue labels and client acceptance are not factual validation; dismissal changes future issue surfacing without necessarily repairing body content.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> await ctx.audit_db.snapshot_if_changed(
>         slug, page.content, triggered_by="content-health-fix", reason="content-health-fix"
>     )
> --- `synthadoc/agents/workflows/tools/content_health_tools.py`

#### MEM-RTE-faithfulness-audit
Label: Citation audit retention and re-audit selection

Caller enqueues audit; orchestrator chooses explicit slug, active corpus or stale-only subset. Citation extraction pairs claim text with available sidecar source lines. The adversarial-role provider judges citation support; code normalizes verdicts and records short reasons, including skipped/error outcomes. No independent expected-answer oracle is supplied: source excerpts are comparison material and the model is the judge. This is open corpus evaluation, not a demonstrated causal experiment. Software admits verdicts without individual human approval; caller can decline to run or request re-audit, not veto each stored result in this branch (SRC-1, `synthadoc/agents/citation_faithfulness_agent.py`, `synthadoc/core/orchestrator.py`, `synthadoc/agents/faithfulness_cache.py`).

The retained JSON is later read by cache GET for display and stale-only selection. Page key uses latest source ingestion timestamp, not a body hash; an edit preserving those timestamps need not invalidate a verdict. Empty-result entries for checked pages prevent repeated stale classification. This is a concrete trace/evaluation-to-control write affecting later auditing, not evidence of automatic knowledge correction. The route was only mentioned, not declared, in [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair); it is a distinct evaluation path.

- Immediate return: job ID, progress and counts; cache GET exposes verdict/reason/time and stale slugs.
- Later read-back: stale-only audit uses retained keys to choose work; GET exposes retained reasons to a reviewing client. Query synthesis use of those reasons is not established.
- Delegated visibility: judge receives extracted claims and selected source lines; retained reason is truncated to 150 characters, not full judgment reasoning.
- Selection predicate: requested scope, active status for broad/stale scans, citation markers/sidecar availability, timestamp-derived page key.
- Invalidation or expiry: changed max source-ingested timestamp or missing entry yields stale; body-only edits can leave matching keys; re-audit replaces entries.
- Activation or effect: writes verdict cache and changes subsequent stale-only workload; model factual correction and improved answers are unobserved.
- Evidence limits: unavailable source lines and parse/provider errors produce skipped results; cache display is not truth certification or universal correction admission.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> reason = str(entry.get("reason", ""))[:150]
> --- `synthadoc/agents/citation_faithfulness_agent.py`

> if entry is None or entry.get("page_key") != key:
>             stale.append(slug)
> --- `synthadoc/agents/faithfulness_cache.py`

#### MEM-RTE-sensitive-mask
Label: Sensitive-data masking and scan history

CLI scan is dry-run by default; --apply requests writes and normally asks confirmation, while --yes skips it. Server post-ingest and periodic scans instead admit regex substitutions automatically when enabled. Code chooses matches from built-in/configured patterns and replaces matched spans with redaction text. This is software curation, not model criticism or a factual oracle. Configuration author controls custom patterns; who installed them is unresolved. Post-ingest uses successful job result slugs; periodic scanning uses modification time and last scan-cycle timestamp, waiting while the queue has pending jobs. Scan metadata retains slug/count/types, not sensitive values (SRC-1, `synthadoc/core/retract.py`, `synthadoc/cli/retract.py`, `synthadoc/integration/http_server.py`).

The retained result is masked Markdown plus audit scan metadata. Later direct reads/retrieval can reload the masked page. In the inspected server masking bodies, direct file writes are not accompanied by search invalidation or epoch bump, so existing corpus/answer caches need not reflect masking immediately. Raw sources, sidecars, prior snapshots and exports are not erased by these page-scanning branches. This is distinct from the unresolved mention of retraction in [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair), not a duplicate repair route. Recovery is not a redaction-specific reversible transaction; other retained copies can still exist.

- Immediate return: CLI match table/counts or background audit events/cycle record and logs.
- Later read-back: page consumers reload changed files; subsequent incremental scan uses retained cycle timestamp, not old sensitive contents.
- Delegated visibility: scanner sees full page file including frontmatter; audit retains only match metadata; later consumers receive masked body when actually reloaded.
- Selection predicate: explicit slug/all files/changed-only in CLI, touched created+updated slugs after completed ingest, or mtime newer than last periodic cycle; enabled flag and patterns govern masking.
- Invalidation or expiry: future scans and edits can change results; no coordinated erasure or cache invalidation is shown in the inspected automatic masking functions.
- Activation or effect: file substitution and audit writes are wired; reduced disclosure across all delivery paths is not established.
- Evidence limits: regex misses/false positives, candidate location, earlier sidecars, history, exports and stale caches prevent a comprehensive withdrawal guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> page_path.write_text(masked, encoding="utf-8")
> pages_with_matches += 1
> --- `synthadoc/integration/http_server.py:794-795`

#### MEM-RTE-scaffold-guidance
Label: Scaffold and retained selection guidance

Queued scaffold uses requested domain and existing content-page slugs, asks a model for categories/purpose/guidelines, validates structure with retries, then writes index, purpose and agent instruction files. Existing marked user zones in index/purpose are preserved; regenerated content replaces scaffold zones. Existing ROUTING.md is rebuilt from index and categories are stamped onto linked pages. The package's static instruction template surrounds generated domain guidance. Ingest later reads purpose as scope; streaming query uses routing; external agent instruction consumption is an affordance contingent on host loading (SRC-1, `synthadoc/agents/scaffold_agent.py`, `synthadoc/core/orchestrator.py`, `synthadoc/cli/_init.py`, `synthadoc/agents/ingest_agent.py`; supplied [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query)).

No supplied scaffold route counterpart; this crosses purpose/instructions/index/routing objects, rather than duplicating [RT-OBJ-workflow-guidance](runtime.md#rt-obj-workflow-guidance), which is fixed package workflow text. Caller selects the operation/domain; model proposes semantic guidance; code validates/adopts. Starting scaffold is not per-generated-text approval. Validation is structural, not an expected-answer oracle. The queued path inspected has no separate per-content veto; marked user zones preserve some prior author control. Partial writes/retry do not imply multi-file rollback. This is retained task guidance generated from domain/slugs, not demonstrated reflective revision of Synthadoc's own methods.

- Immediate return: scaffold job result, categories_updated and routing_regenerated, or failure/retry.
- Later read-back: purpose conditions later ingest decisions; index-derived routing scopes later streaming retrieval; host may load retained instruction files in later sessions.
- Delegated visibility: generator gets requested domain and protected slugs, not necessarily full page bodies or prior operational outcomes; external instruction host delivery is unobserved.
- Selection predicate: existing non-system slugs and requested domain; marker-based merge decides preserved versus replaced text; routing regeneration requires an existing routing file.
- Invalidation or expiry: subsequent scaffold/manual changes can revise guidance; ingest decision prompt hash includes purpose; complete cache coherence after every scaffold write remains uninspected.
- Activation or effect: file writes and subsequent purpose/routing readers are wired; external host obedience and beneficial category organization remain unobserved.
- Evidence limits: exact initial human/model provenance of a deployed purpose/routing file is unresolved; known subsequent transformations do not depend on resolving it.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> final_purpose = preserve_user_zone(existing_purpose, result.purpose_md)
> purpose_path.write_text(final_purpose, encoding="utf-8", newline="\n")
> --- `synthadoc/core/orchestrator.py`

#### MEM-RTE-backup-restore
Label: Retained backup creation and restoration

Backup engine packages wiki Markdown, root Markdown/text, hooks, config, audit DB and extracted sidecars, optionally source files, exports and response cache. SQLite uses online backup to include committed WAL contents. Archive contains mixed readable text, symbolic configuration/manifests and opaque database bytes; a manifest/checksum is access/integrity metadata, not a summary of factual meaning. Extraction restores bytes within a destination wiki root. Caller supplies archive/target; byte selection/adoption is software, not model judgment. CLI confirmation policy was not inspected; engine API does not establish human review or a deployed later use by itself (SRC-1, `synthadoc/core/backup_engine.py`). No supplied route counterpart; this is not the rendered export route [RT-RTE-context-export](runtime.md#rt-rte-context-export).

- Immediate return: archive path/manifest or extracted wiki-root path.
- Later read-back: restoration makes retained files available to ordinary store/config readers; actual reload of a restored installation is unobserved. Engine functions alone establish recovery capability, not an exercised consumer deployment.
- Delegated visibility: archive includes selected raw files/DB snapshots; manifest does not expose all their contents to an agent automatically.
- Selection predicate: path/extension enumeration and include_sources/include_exports/include_cache; restore uses archive members and skips escaping paths.
- Invalidation or expiry: later archives are separate snapshots; live writes do not refresh old archives; subsequent restore can reintroduce old content.
- Activation or effect: archive creation and file restoration are implemented; restored content entering later behavior requires a subsequent consumer invocation.
- Evidence limits: no all-file transaction or complete state clone is established. Inspected enumeration does not include embeddings.db or faithfulness-cache.json, so those derived stores are not guaranteed preserved by this backup.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

> for name in ("config.toml", "audit.db"):
> --- `synthadoc/core/backup_engine.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-retained-content
Label: Retained knowledge and access controls reach consumers

Consumer: query/maintenance model, retrieval software, or requesting external host. Channel: reloaded body excerpts to synthesis/tool results; parsed metadata/routing to selectors; cached answer to HTTP output. Force: natural-language interpretation for bodies/reasons/purpose, symbolic selection/dispatch for lifecycle/routing/cache keys. Horizon: later calls and sessions while retained files/DB rows remain. A cached decision can select an action through Python without re-evaluating changed candidate bodies; a cached answer bypasses the model. This differs from [RT-BAP-source-decision](runtime.md#rt-bap-source-decision), which covers original-source compilation, and [RT-BAP-workflow-guidance](runtime.md#rt-bap-workflow-guidance), which covers static method text. Authority is the actual consumer's rule or model interpretation, not proof of truth or beneficial dependence (SRC-1, `synthadoc/storage/search.py`, `synthadoc/core/cache.py`, `synthadoc/integration/http_server.py`, `synthadoc/agents/context_agent.py`; [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query)). Supporting passages reside in [MEM-OBJ-response-cache](#mem-obj-response-cache), [MEM-RTE-cross-wiki](#mem-rte-cross-wiki) and the supplied query route.

## Annotations

#### On [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

Retention separates original source, extracted sidecar, cached analysis/decision, derived body and provenance. Sidecar precedes sanitizer/clipping; analysis entities/tags are not the full source. Source/force request is caller agency; compilation/action admission is model/software agency, except a later candidate review path. Cached decisions can shape later writes without rerunning proposal generation. These facts concern the memory chain, not a new route identity (SRC-1, `synthadoc/agents/ingest_agent.py`; [MEM-OBJ-source-sidecars](#mem-obj-source-sidecars), [MEM-OBJ-response-cache](#mem-obj-response-cache)).

#### On [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query)

Delivery is request-driven, with internal model/code selection rather than independent unsolicited memory push. Active/stale body text survives only if ranked and budgeted; trimmed old turns remain in DB rather than being summarized into this query input. Cached answer delivery is another consumer with greater direct output authority than advisory context. History and page excerpts are by-value strings: explicit search/read can reload omitted files; a slug in a window is not automatically dereferenced. Search corpus is process-cached and invalidation is explicit (SRC-1, `synthadoc/storage/search.py`, `synthadoc/integration/http_server.py`; [MEM-RTE-session-context](#mem-rte-session-context)).

#### On [RT-RTE-context-export](runtime.md#rt-rte-context-export)

Context packs retain no newly authored general memory in the inspected run: they return ranked first-120-word excerpts with slug/confidence/tags and omitted-page metadata, applying an approximate token estimate. They are requested retrieval, not independent push. A caller can read omitted pages explicitly. Export persists a separate readable snapshot. The shipped OKF consumer selects sorted files with type metadata and optional type filter, prepends description where present, and stops before a page would overflow its 760000-character default cap; it does not choose facts based on the question before loading. Thus bundle selection differs materially from wiki retrieval, and source lineage is whatever survives export, not the full audit DB (SRC-1, `synthadoc/agents/context_agent.py`, `tests/integration/okf_consumer_agent.py`).

> if total_chars + len(section) > max_chars:
> --- `tests/integration/okf_consumer_agent.py`

#### On [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission)

Candidate Markdown is retained proposed knowledge outside ordinary live-page lookup. Caller promotion/discard supplies admission/rejection but not authenticated human review. Promotion preserves the page's stored lifecycle state: filesystem admission is not query eligibility. Discard withdraws the candidate, not prior live pages, cached derivatives or external exports. These memory limits use the supplied handler passages; no stronger deletion or rollback claim follows (SRC-1, `synthadoc/integration/http_server.py`).

#### On [RT-RTE-lint-repair](runtime.md#rt-rte-lint-repair)

Contradiction/unresolved notes are retained interpreted reasons; the supplied resolution branch can clear them and replace body text. The current content snapshot is recovery/history material, not necessarily pre-write lineage or complete source evidence. A model's acceptance can admit active content without human review. Future search can therefore consume model-reconciled knowledge, but the declared reason for reconciliation need not accompany selected body text. This does not establish reliable contradiction elimination (SRC-1, `synthadoc/agents/lint_agent.py`; supplied minimum passage).

#### On [RT-RTE-client-write](runtime.md#rt-rte-client-write)

The external client supplies content; caller identity leaves human authorship/approval unresolved. Existing active state can survive a semantic rewrite; clearing contradiction note changes future diagnostic evidence. Snapshot retention is separate from content validity and cannot show who reviewed the edit. The later consumer chain is explicit read or eligible retrieval of replaced body, not automatic delivery to every external host (SRC-1, `synthadoc/integration/mcp_server.py`; supplied write passage).

#### On [RT-RTE-workflow-loop](runtime.md#rt-rte-workflow-loop)

Loop message accumulation alone is current-run context, not cross-invocation memory. Concrete durable outcomes are changed pages, fix records, snapshots and jobs. Content-health pre-fix retention plus explicit rollback provides a recovery chain, whereas ordinary accumulated tool results do not by themselves become reusable method guidance. No host-side compaction inference is made for coding-agent delegation (SRC-1, `synthadoc/agents/workflows/tools/content_health_tools.py`; [MEM-RTE-health-history](#mem-rte-health-history), [RT-RTE-provider-delegation](runtime.md#rt-rte-provider-delegation)).

## Write side

Acquisition and curation are not one trust boundary. Extraction can transform raw files before ingest; sidecars persist its output. Regex sanitization and character clipping then constrain model input. Analysis, snippet selection and action decision transform source into derived pages; citation annotation and merges further transform it. Provenance survives as source references rather than a complete reasoning transcript. Imported sessions supply a concrete trace-origin alternative, but their tool/thinking exclusions prevent equating the compiled page with verified operational evidence ([MEM-RTE-session-ingest](#mem-rte-session-ingest); SRC-1, `synthadoc/agents/ingest_agent.py`).

Admission varies by route. Caller source choice is not per-generated-text approval. Default/force live writes, staged candidate movement, automatic lint resolution, direct MCP replacement, guarded interactive edits and marker-preserving scaffold regeneration have different owners and veto points. Model skip, dedup, candidate discard, declined confirmation, unresolved lint response, structural-validation failure and missing recovery snapshots are different rejection/failure outcomes, not one correctness filter. The page-state machine itself explicitly excludes automatic lint/ingest writes from its validation contract ([MEM-OBJ-page-metadata](#mem-obj-page-metadata); supplied runtime routes).

Automatic trace-fed writes have different retained effects. Session overflow produces a stored summary whose semantic read-back is not established; imported JSONL can produce knowledge consumed later; content-health writes fix/recovery metadata; faithfulness results alter later re-audit selection; scan-cycle timestamps alter later scan selection. Raw event logs alone are not learned policy. No observed benefit or revised general method follows from these writes. Reasons survive selectively: faithfulness short reason, contradiction/unresolved notes and dismissal reasons; summary prompt asks to preserve decisions but not their full justification. Neither ordinary query nor context-pack excerpts guarantee delivery of those reasons ([MEM-RTE-session-context](#mem-rte-session-context), [MEM-RTE-faithfulness-audit](#mem-rte-faithfulness-audit), [MEM-RTE-health-history](#mem-rte-health-history)).

Withdrawal is similarly scoped. Candidate discard removes a proposed file; lifecycle changes alter some selectors; page masking edits matched text; rollback reintroduces prior bodies; restore can reintroduce entire retained files. None proves erasure from every derived or exported copy. Masking code in particular warrants a cache-coherence question rather than a system-wide non-disclosure claim ([MEM-RTE-sensitive-mask](#mem-rte-sensitive-mask), [MEM-RTE-backup-restore](#mem-rte-backup-restore)).

## Read-back

Local query, context packs, direct MCP/page reads, cross-wiki retrieval, exported-bundle answering, maintenance history and cached response reuse are distinct later-consumer chains. Local BM25/optional vector rerank selects by question-derived terms; routing can restrict candidates; the synthesis budget can remove or truncate retrieved pages. ContextAgent selects first-120-word excerpts and skips over-budget entries. Cross-wiki retrieval additionally drops non-active pages, merges peers and imposes a separate character cap. OKF consumption selects by type/file order and whole-page fit rather than live relevance search. This rejects a single active-only or whole-source model-input account ([RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [RT-RTE-context-export](runtime.md#rt-rte-context-export), [MEM-RTE-cross-wiki](#mem-rte-cross-wiki); SRC-1 paths in those records).

Working-context control is primarily code-owned isolation and selection: analysis/decision/synthesis calls receive selected strings and return structured/text results, without inheriting all previous calls. This resembles per-task frames only at the input/return boundary. There is no model-window pointer dereference or reference-counted liveness: omitted raw files remain reachable only through explicit I/O. Recent session tail selection removes older turns from input without removing DB messages. The separate summary model writes a compressed artifact but, in the inspected handler, that artifact does not replace the removed turns in synthesis. Workflow accumulation has budgets but no demonstrated repository-managed compaction; external coding-agent summaries/checkpoints remain opaque ([MEM-RTE-session-context](#mem-rte-session-context), [RT-RTE-workflow-loop](runtime.md#rt-rte-workflow-loop), [RT-RTE-provider-delegation](runtime.md#rt-rte-provider-delegation)).

Background masking, overview generation and scheduled operations are automatic producers/maintenance triggers, not evidence of independent memory push into a foreground model. Requested query/context/export tools remain request-driven even when their internal selector is automatic. An exposed storage API does not establish an unspecified later consumer: overview generation and backup restoration are explicitly bounded at that distinction. Faithfulness keys and scan timestamps do have identified later software selectors, but semantic judgment reasons are not thereby model instructions ([MEM-OBJ-overview](#mem-obj-overview), [MEM-RTE-backup-restore](#mem-rte-backup-restore), [MEM-RTE-faithfulness-audit](#mem-rte-faithfulness-audit)).

## Integration issues

- **No supported contradiction of a supplied runtime fact.** Runtime explicitly leaves sessions, faithfulness and sensitive retraction incomplete. This report extends those paths rather than correcting an established contrary claim. Summary storage must not be reconciled into a claim of summary-fed answers: only recent raw history is passed in the inspected local handler ([MEM-RTE-session-context](#mem-rte-session-context); SRC-1, `synthadoc/integration/http_server.py`).
- **Containment, not duplicate routes:** [MEM-RTE-session-ingest](#mem-rte-session-ingest) specializes [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); [MEM-RTE-health-history](#mem-rte-health-history) specializes [RT-RTE-workflow-loop](runtime.md#rt-rte-workflow-loop). All other new objects/routes state their distinct identities beside the closest supplied records. No candidate duplicate requiring supersession was found. [MEM-BAP-retained-content](#mem-bap-retained-content) concerns later consumption, not original source ingestion or static workflow guidance.
- **Summary integration remains limited:** repository search for `get_summary`, `history_summary` and `summary_turn_count` found declarations/migrations in `synthadoc/storage/log.py` and local overflow handling in `synthadoc/integration/http_server.py`. Those reads use summary/count for control; no summary-to-synthesis content delivery was found there. This is a bounded implementation finding, not a claim about external host compaction ([MEM-OBJ-chat-messages](#mem-obj-chat-messages)).
- **Masking coherence is unresolved:** the inspected automatic masking functions write files/audit events without epoch bump or corpus invalidation. Cached responses, prior snapshots, sidecars and exports can therefore defeat a stronger withdrawal claim. Complete interleaving with every independent writer/cache is uninspected; integration must not upgrade file masking to global erasure ([MEM-RTE-sensitive-mask](#mem-rte-sensitive-mask), [MEM-OBJ-response-cache](#mem-obj-response-cache); SRC-1, `synthadoc/integration/http_server.py`).
- **Body-only edits can leave evaluation freshness metadata unchanged:** faithfulness uses max source-ingested timestamp rather than content hash; direct edits need not change that key. Retained verdict reasons support display/re-audit history, not guaranteed current factual assessment ([MEM-RTE-faithfulness-audit](#mem-rte-faithfulness-audit), [RT-RTE-client-write](runtime.md#rt-rte-client-write); SRC-1, `synthadoc/agents/faithfulness_cache.py`).
- **Alternative stores remain named uncertainties:** exact initialization authority for deployed purpose/routing/registry, all embedding refresh paths, hook-produced state, coding-agent native checkpoints, every extraction skill's lineage and every workflow's recovery are unresolved. These prevent exhaustive provenance, coherence, compaction or approval claims, without negating inspected subsequent transformations. See coverage table, [MEM-OBJ-search-vectors](#mem-obj-search-vectors), [MEM-RTE-scaffold-guidance](#mem-rte-scaffold-guidance), [RT-RTE-extension-loading](runtime.md#rt-rte-extension-loading) and [RT-RTE-provider-delegation](runtime.md#rt-rte-provider-delegation).
- **Backup/export snapshots are not the live store:** inspected backup enumeration does not preserve every derived store; exports do not auto-refresh. Restore/rollback may revive content already withdrawn elsewhere. No deployed restoration or cross-system interoperability benefit was observed ([MEM-RTE-backup-restore](#mem-rte-backup-restore), [RT-RTE-context-export](runtime.md#rt-rte-context-export); SRC-1, `synthadoc/core/backup_engine.py`).

## Limitations and checks

The source HEAD was rechecked as b80d9388a3013e8051baf2854c7250942c46e91a with clean short status before analysis. The supplied method/type/collection/records inputs were read completely, recovering the runtime terminal range. Source searches and reads are implementation evidence only; comments and generated guidance supply intent where explicitly identified. No new source identity, target execution, live deployment, measured outcome or causal comparison was introduced.

There is no identified repository access gap. Available but uninspected paths are named in coverage and integration issues. In particular, no complete audit of all client behavior, evaluation feedback, workflow subclasses, model-provider state or cache invalidation is claimed. Presence and delivery do not establish actual reliance, source fidelity, correct reconciliation, beneficial learning or self-improvement. The standalone consumer's broad interoperability assertion is treated as a design claim; inspected selection code establishes one consumer implementation only.

Deterministic validation: completed successfully with the invocation's validate-output command. This checks form, identity and quotation occurrence, not semantic support, operation or acceptance.
