---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "LLM-WIKI-MCP memory: Markdown knowledge, sidecar retrieval, lossy conversation retention and separate recursive-context consumers."
run-id: AAS-2026-10-15-llm-wiki-mcp-5dff0dd0576a-01
source-identity: https://github.com/Electro-resonance/LLM-WIKI-MCP
reviewed-boundary: "25efb7631082fa3732723fee08e24d39b43311fa"
---

# LLM-WIKI-MCP memory report

## Boundary and evidence

This report covers retained knowledge, derived access structures, conversation memory, configuration and maintenance within the whole-system [boundary](boundary.md#boundary-and-evidence). SRC-1 is the frozen repository at 25efb7631082fa3732723fee08e24d39b43311fa. HEAD was rechecked against that identity. Direct inspection below adds implementation evidence, not execution evidence. No target code, tests, examples or providers were executed.

The provisional runtime correctly separates release agentic/plain ask from store ask. Memory tracing must additionally separate live ask turns, their compressed archive, recursive-context tools, CLI session recovery and transcript/decision admission. Retaining something does not mean the final agentic prompt reads it. Source anchors below are commit-relative SRC-1 paths; supplied records provide passages for runtime findings not reread here.

| Entry point or operation | Source path and inspection basis | Coverage or limit |
| --- | --- | --- |
| Final agentic prompt and recorder | `src/llm_wiki_mcp/context_api.py`, direct: final context builder, read executor, ask tail | [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask), [RT-OBJ-context-pack](runtime.md#rt-obj-context-pack), annotations below; alternate history channel can include stored prompts |
| Plain and store ask; retrieval/context APIs | `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/server.py`, supplied runtime; final search override directly read | [RT-RTE-plain-ask](runtime.md#rt-rte-plain-ask), [RT-RTE-store-ask](runtime.md#rt-rte-store-ask), [MEM-OBJ-pages-fts](#mem-obj-pages-fts); no transferred agentic-history guarantee |
| History append/load/compress; explicit record/compress tools | `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/server.py`, direct | [MEM-OBJ-ask-history](#mem-obj-ask-history), [MEM-OBJ-ask-history-compressed](#mem-obj-ask-history-compressed), [MEM-RTE-history-compaction](#mem-rte-history-compaction) |
| Recursive preview/context and history-status/self-access | Same two source files, direct helpers/registered wrappers; `src/llm_wiki_mcp/cli.py`, scoped dispatch search | [MEM-RTE-recursive-context](#mem-rte-recursive-context); helper/handler wiring is not evidence of an external host's use |
| CLI visible-turn guard, session merge, command history | `src/llm_wiki_mcp/cli.py`, direct guard/merge; dispatch and readline searches | [MEM-RTE-cli-history](#mem-rte-cli-history); command history is distinct from answers |
| Page create/update/seed/index; file ingestion and provenance | `src/llm_wiki_mcp/server.py`, direct; `src/llm_wiki_mcp/context_api.py`, direct provenance, wrapper and final ingest | [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write), [MEM-OBJ-wiki](#mem-obj-wiki), [MEM-OBJ-provenance](#mem-obj-provenance) |
| Sidecar iteration, combined text, current note search and following-page windows | `src/llm_wiki_mcp/context_api.py`, direct | [MEM-OBJ-notes](#mem-obj-notes), knowledge-write annotation; window-helper internals not fully audited, so exact page-marker parsing correctness remains uninspected |
| Transcript import and decision log | `src/llm_wiki_mcp/server.py`, direct methods and registry search | [MEM-RTE-transcript-decision](#mem-rte-transcript-decision); separate controls and retained parts described |
| Rename/delete and tombstones | `src/llm_wiki_mcp/server.py`, direct | [MEM-RTE-page-withdrawal](#mem-rte-page-withdrawal); no whole-vault erasure claim |
| Lint/repair; runtime config; documentation consolidation | `src/llm_wiki_mcp/server.py`, `src/llm_wiki_mcp/context_api.py`, supplied runtime | [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write), [RT-RTE-runtime-config](runtime.md#rt-rte-runtime-config), [RT-RTE-docs-consolidate](runtime.md#rt-rte-docs-consolidate); complete maintenance correctness not audited |
| TOC and schema guidance | `src/llm_wiki_mcp/server.py`, direct `toc`/`schema_doc` bodies in this correction | Generated navigation page and separate editable/default vault schema; full schema caller/model read-back uninspected, preventing exhaustive instruction-surface comparison |
| Metrics, usage/self-access, runtime journal | `src/llm_wiki_mcp/context_api.py`, direct producer, sanitizer, metrics append/load/summary and usage/self-access; `src/llm_wiki_mcp/server.py`, registered diagnostic wrappers; `src/llm_wiki_mcp/cli.py`, diagnostic displays | [MEM-OBJ-runtime-traces](#mem-obj-runtime-traces); final ask journal production not established by old superseded bodies |
| MCP transport and mutation availability | `src/llm_wiki_mcp/server.py`, supplied dispatch record plus direct memory wrapper inspection | [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch); deployed grants and downstream host context are external |
| Regression evaluators and demonstration caller | `tests/`, `examples/demo_commands.sh`, supplied boundary inventory | Tests are not run results. Full evaluator-body inspection is not claimed; observed memory benefit and complete regression coverage are prevented |
| Model weights/provider state | External endpoint, supplied runtime | [RT-CMP-ollama-model](runtime.md#rt-cmp-ollama-model); opaque provider memory, training lineage and behavior remain uninspected |

Populated deployment pages, runtime config, paired traces and external host state are not supplied. Static shipped prompts and developer/maintenance instructions are guidance, not accumulated memory; their effective use by later contributors is unobserved. Generated documentation is covered by the supplied consolidation route, not silently treated as model learning.

## Core ideas

1. **Markdown is the retained content; SQLite and caches select access.** Pages can originate in arbitrary caller text, extraction, seeds, transcript clipping or decision entries. Their labels and source fields provide lineage, not truth certification. Sidecars are automatically admitted templates and affect retrieval before any human promotion of suggested links.
2. **There are two different historical reductions.** Live JSONL preserves a question, prompt and answer. Compaction drops older exact prompts/metadata into a lossy Markdown archive; the final agentic pack normally selects recent live turns, whereas the registered recursive-context tool can return the archive. Archive storage is not automatic archive delivery to the final ask model.
3. **Context budgeting is path-specific and not a single history cap.** The recent-history Markdown gets a budget, but separate `wiki_ask_history` tool evidence can serialize full live records, including stored prompts, into the source-evidence section. Whole-pack trimming still applies. Thus 900 characters per historical answer is not a bound on all historical material reaching the first prompt.
4. **Trace retention can influence later work without establishing improvement.** A prior question can deterministically alter follow-up query resolution, and prior answers can enter later prompts. Compaction is string reduction, not model critique or learned weights. No observed capacity gain is established.

These mechanisms are recorded below and in annotations on the supplied routes. SRC-1: `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/server.py`, `src/llm_wiki_mcp/cli.py`.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-wiki
Label: Wiki pages

Source-native identity: vault `wiki/*.md`, with optional frontmatter and wiki links. The substrate is local UTF-8 files; prose is natural-language knowledge for people/models, while frontmatter, titles and link syntax also have symbolic consumers in indexing/navigation. Lineage includes caller bodies, automatic seed pages, extracted source wrappers, clipped transcripts, decision entries and structural repair text. Initial corpus authorship/trust is unresolved without a deployment corpus. A generic API caller need not be human. Closest supplied record is [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write), a producer route rather than this retained object; no supplied object counterpart.

Later consumers include direct page readers, FTS indexing, note generation, page/note search, retrieval packs and model prompts. Storage does not itself give pages instruction-level permission; actual generation authority is interpreted evidence under shipped answer guidance. Raw source copies under `raw/` are a separate ingest artifact, not the normal retrieval body. Caller `copy_raw` and directory ingestion can preserve those bytes, but later re-extraction from the raw copy is not established here. SRC-1: `src/llm_wiki_mcp/server.py`, `src/llm_wiki_mcp/context_api.py`.

> body = f'# {page_title}\n\nSource file: `{src.name}`\n\n## Extracted Content\n\n{text.strip()}\n'
> created = self.create_page(page_title, body, tags=['source','ingested'], source=str(src), overwrite=True)
> --- `src/llm_wiki_mcp/server.py`

#### MEM-OBJ-pages-fts
Label: Page index and search caches

Source-native identity: `pages` metadata and `pages_fts` text tables in the store SQLite database, plus process-local `search_cache`/`context_cache`. These are symbolic access structures and copied text, not vector embeddings or model parameters. They derive from current Markdown at indexing time; `pages` holds path/hash/time/counts while FTS holds title/body. Final contextual search uses cached query/vault/limit keys, FTS candidates and bounded fallback scanning; store retrieval then rereads page bodies. Metadata is not an independent semantic memory.

Closest supplied record [RT-RTE-store-ask](runtime.md#rt-rte-store-ask) owns the reader route, not this substrate. No supplied object counterpart. Reindex deletes and rebuilds tables; process cache freshness remains separately bounded by TTL rather than proven immediate invalidation across every write. The supplied runtime gives the route and limits. SRC-1: `src/llm_wiki_mcp/server.py`, `src/llm_wiki_mcp/context_api.py`.

> con.execute('DELETE FROM pages')
> con.execute('DELETE FROM pages_fts')
> con.commit()
> --- `src/llm_wiki_mcp/server.py`

#### MEM-OBJ-notes
Label: AI sidecar notes

Source-native identity: vault `notes/<page filename>.md`. Local natural-language Markdown includes a templated working summary, extracted terms, scored link suggestions and suggested actions. Symbolic ranking code consumes its terms/text; people/models consume its prose. It is derived from page text plus old note text and other page/title matches. The implementation uses term counting and templates, not an inference request, despite the AI-maintained label. Reruns overwrite the note and can recycle old-note vocabulary. No supplied object counterpart; [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write) describes its producer route.

Search joins page and note into its scoring blob, adds a note-match bonus and may return the note's centred snippet instead of the canonical source's snippet. `release_combined_page_text` supplies another explicit reader. Full page expansion itself reads the source page, not this combined text. Human/agent link promotion is described in the note, not enforced as a gate before note text affects search. SRC-1: `src/llm_wiki_mcp/context_api.py`.

> terms = release_extract_terms(page_text + "\n" + old_note, 25)
> links = release_find_candidate_links(vault_path, title, max_links)
> --- `src/llm_wiki_mcp/context_api.py`

> excerpt_source = note if note and any(t in note.lower() for t in terms) else source
> win = release_centered_match_excerpt(excerpt_source, matched or terms, context_chars=context_chars)
> --- `src/llm_wiki_mcp/context_api.py`

#### MEM-OBJ-ask-history
Label: Exact ask history

Source-native identity: configured JSONL file, default `ask_history.jsonl`. Symbolic rows carry natural-language question, prompt and answer plus sources, metadata, token estimates and timestamp. The source list can be tool names, not passage citations; final agentic recording supplies trace tool names. This is retained interaction material, not an audited record of every actual provider prompt: second-pass answers can coexist with the first stored prompt, as [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask) establishes. Direct record tools also admit caller-supplied histories, so CLI provenance is not guaranteed by display labels.

Closest supplied records are agentic/plain ask producer routes and [RT-OBJ-context-pack](runtime.md#rt-obj-context-pack), a current invocation object rather than this persistent log. No duplicate object is intended. Live rows feed recent-history rendering, explicit history tools, deterministic intent resolution and CLI history. At the code intent consumer, prior-question content can change the resolved query; at the model consumer, selected text is follow-up guidance rather than verified truth. SRC-1: `src/llm_wiki_mcp/context_api.py`.

> q=row.get("question") or row.get("prompt") or row.get("user")
> a=row.get("answer") or row.get("response")
> if q: hist.append({"question":q,"answer":a})
> --- `src/llm_wiki_mcp/context_api.py`

> return {"intent":"contextual_followup","original_question":original,"resolved_question":f"Interpret as a follow-up to previous topic. Previous question: {last_q}. Current follow-up: {q}","context_hint":"Short follow-up expanded using ask history."}
> --- `src/llm_wiki_mcp/context_api.py`

#### MEM-OBJ-ask-history-compressed
Label: Compressed ask history

Source-native identity: configured Markdown file, default `ask_history_compressed.md`. Local natural-language derived memory contains older question headings, whitespace-collapsed answer prefixes up to 1000 characters and at most ten source entries per older turn, appended to existing archive text. It does not retain those turns' exact prompts, metadata or full rationale independently of answer prefixes. Source entries can be tool labels. No supplied counterpart after comparison with [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask); this is the distinct older-memory object, not the current pack.

The recursive-context helper reads it; the final pack's recent-history reader does not. Its consumer and content-loss rules belong to [MEM-RTE-history-compaction](#mem-rte-history-compaction) and [MEM-RTE-recursive-context](#mem-rte-recursive-context). Archive text is not globally capped by the live-history threshold. SRC-1: `src/llm_wiki_mcp/context_api.py`.

> existing = release_read_compressed_history(vault_path)
> summary_parts = []
> if existing:
>     summary_parts.append(existing.strip())
> --- `src/llm_wiki_mcp/context_api.py`

#### MEM-OBJ-provenance
Label: Ingest provenance

Source-native identity: `llm_wiki_provenance.sqlite`, with directories, source_files and file_versions. Symbolic rows retain paths, hashes, size, datestamps, page mapping, ingest counts and version events. They are access/update metadata, not old source payloads; a version row cannot by itself restore prior content. Initial source authorship remains outside these fields. Closest supplied referent [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write) is the admission route; no supplied object counterpart.

The next ingest plan consumes datestamp/hash equality to skip or update, with a separate PDF-placeholder refresh case. This metadata has executable selection authority at the planner, not truth authority at the answer model. Record ingestion follows page write; failure can leave a page without corresponding successful provenance/index updates. SRC-1: `src/llm_wiki_mcp/context_api.py`.

> if int(row["mtime_ns"])==rec["mtime_ns"] and row["current_sha256"]==rec["sha256"]:
>     return {"action":"skip","reason":"same datestamp and hash","record":rec,"source_file_id":row["id"],"wiki_title":row["wiki_title"]}
> --- `src/llm_wiki_mcp/context_api.py`

#### MEM-OBJ-runtime-traces
Label: Metrics and runtime journal

Source-native identities: `ask_metrics.jsonl` and `runtime_journal.jsonl`, separate local symbolic row streams. Metrics derive prompt/answer estimates and elapsed time, retaining question, source labels and metadata. For final agentic ask, that metadata includes the complete sanitized `llm` dictionary: a successful adapter result contains `answer` and raw provider output, and second-pass results can be nested within it. Thus metrics can independently preserve provider answer bodies, not only estimates. Deterministic/basic or failed responses need not contain such bodies; the retained provider answer is not necessarily the final normalized/fallback answer. Journal records caller-supplied command/query/tools/success/latency/token fields. Neither label authenticates a successful execution. The recorder for metrics is called by final ask; journal write helpers and registered tools exist, but old overwritten ask bodies do not prove current automatic journal recording.

Metrics append is separate from live-history admission and compression: `history_enabled: false` makes the history append return None but does not suppress the subsequent metrics write if control reaches it. Live-history compaction rewrites history files, not `ask_metrics.jsonl`. Metrics are therefore a separate answer-retention surface, not governed by the live-history threshold. This does not guarantee successful metrics persistence after a recorder exception, or reconstruct the exact answer-producing prompt.

Consumers are `release_load_metrics` (last requested number of JSONL lines, default 100) and `release_metrics_summary` (aggregate fields plus the last ten complete loaded rows). Usage snapshots embed this summary; self-access snapshots embed usage and its metrics. Registered MCP `wiki_llm_metrics`, `wiki_usage_snapshot` and `wiki_self_access_snapshot` return these structures to the calling host. This exposes retained answer metadata to an explicit diagnostic consumer without establishing downstream model delivery. CLI `/tokens` instead prints aggregates and the last five questions/speeds, not complete metadata; `/self-stats` and `/self-usage` print selected counts/usage fields. Journal readers are separate. These supply operational reports; a source-supported automatic quality-driven policy update from their scores is not established by the inspected helpers. Closest supplied records [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask) and [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch) concern producer/access routes; no supplied object counterpart. Command history `.llm_wiki_history` is another raw trace, consumed by readline navigation rather than model answer history. SRC-1: `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/cli.py`, `src/llm_wiki_mcp/server.py`.

> hist = release_record_ask_turn(vault_path, question, prompt, answer, sources or [], metadata or {})
> met = release_record_llm_metrics(vault_path, question, prompt, answer, elapsed_seconds, sources or [], metadata or {})
> return {"history": hist, "metrics": met}
> --- `src/llm_wiki_mcp/context_api.py`

> {"agentic": True, "protocol_mode": protocol_mode, "ollama": release_sanitize_public_obj(llm), "context_pack": {k: v for k, v in context_pack.items() if k != "prompt"}},
> --- `src/llm_wiki_mcp/context_api.py`

> return {"ok": True, "answer": answer, "elapsed_seconds": elapsed, "raw": obj, "model": model, "host": host}
> --- `src/llm_wiki_mcp/context_api.py`

> "metadata": metadata or {},
> }
> path = release_metrics_path(vault_path)
> path.parent.mkdir(parents=True, exist_ok=True)
> with path.open("a", encoding="utf-8") as f:
>     f.write(_release_json.dumps(rec, ensure_ascii=False) + "\n")
> --- `src/llm_wiki_mcp/context_api.py`

> "recent": rows[-10:],
> --- `src/llm_wiki_mcp/context_api.py`

> return release_metrics_summary(arguments.get("vault_path") or arguments.get("vault") or "wiki_vault", int(arguments.get("limit",100)))
> --- `src/llm_wiki_mcp/server.py`

The summary's complete-row return is a diagnostic read-back path. It is not an automatic answer-history reload path: the final context pack's recognized tool-evidence list does not include these diagnostic tool names. The supplied [RT-OBJ-context-pack](runtime.md#rt-obj-context-pack) gives that whitelist. SRC-1: `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/server.py`, `src/llm_wiki_mcp/cli.py`.

### Routes

#### MEM-RTE-history-compaction
Label: History compaction

This is a distinct maintenance subroute of answer persistence, not a replacement for the supplied ask route.
Part of: [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask)

Trigger/owner: recording invokes code's compression check; explicit compress, CLI history-status and self-access can also invoke it. Config enables compression and supplies a threshold. Code loads at most 500 live rows, totals question/prompt/answer estimates, and if over budget writes the older-turn reduction before rewriting live JSONL with the configured recent tail. Software decides content removal; the caller can disable compression but need not approve each summary. Generic caller identity is unresolved. No answer oracle or semantic rejection occurs; this is open operational maintenance, not an improvement experiment. History recovery is retained recent rows plus archive, not full prompt restoration; independently retained metrics can preserve provider answer copies but are not reloaded by this compactor or the normal history readers; no multi-file atomic commit or automatic backup is shown.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Compression flag, prior estimated total, archive path and retained/compacted counts, or disabled/under-budget reason.
- Later read-back: Live recent rows enter later asks; older reductions enter the separate recursive-context reader, not automatically the final pack's recent-history section.
- Delegated visibility: Explicit tool caller receives compression metadata, not a launched agent context.
- Selection predicate: Over-budget check over at most 500 rows; keep_recent_turns selects the exact tail, older rows contribute truncated answers and source labels.
- Invalidation or expiry: Exact older rows are overwritten out of live JSONL; accumulated archive remains until separately replaced. This is not a strict bound on total archive size or even retained-tail size.
- Activation or effect: Code changes future reader inputs; deployed model dependence or improved capacity is unobserved.
- Evidence limits: Loading only the last 500 before rewriting can discard earlier unselected rows without adding them to this archive update. No deployment values or crash behavior are supplied.

SRC-1: `src/llm_wiki_mcp/context_api.py`. It is a trace-fed automatic reduction whose durable result can shape later context; it is not merely raw logging, nor evidence of improved competence. Reasons survive only when included in retained answer prefixes; no criticism/rationale extraction is implemented in this reducer.

> a = " ".join(str(row.get("answer", "")).split())[:1000]
> src = row.get("sources") or []
> summary_parts.append(f"## Turn: {q[:120]}")
> --- `src/llm_wiki_mcp/context_api.py`

> with live.open("w", encoding="utf-8") as f:
>     for row in recent:
>         f.write(_release_json.dumps(row, ensure_ascii=False) + "\n")
> --- `src/llm_wiki_mcp/context_api.py`

#### MEM-RTE-recursive-context
Label: Recursive memory context

Distinct alternate reader compared with [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask): explicit Python/MCP `wiki_recursive_context` calls `release_recursive_context_with_memory`. Code combines the compressed archive, reduced recent rows, caller base context and current question when recursive config permits. This returns context; it does not itself send a provider request. The external MCP consumer role is afforded, but downstream host delivery to a model is uninspected. The older preview helper is a different construction: it reduces live rows and does not read the compressed archive.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Context text, recursive flag, estimated tokens and archive-presence metadata.
- Later read-back: Archive and recent retained answers become returned context on a later explicit request; host/model use after that return is uninspected.
- Delegated visibility: MCP caller receives text; no internal sub-agent or isolated execution frame is created.
- Selection predicate: Recursive setting gates archive/recent insertion; recent count comes from keep_recent_turns, reduction uses max_history_tokens, archive is included whole.
- Invalidation or expiry: Context rebuilt from current files; archive persists separately; no final whole-context cap in this helper.
- Activation or effect: Local string composition is wired; behavioral influence on an external model is afforded, not observed.
- Evidence limits: A storage reader and registered tool do not establish automatic use by the final agentic synthesis path. Provider capacity and host selection remain external.

SRC-1: `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/server.py`.

> if ask.get("recursive_enabled", True):
>     if compressed:
>         parts.append("# Compressed Long-Term Ask Memory\n\n" + compressed)
>     if recent:
>         parts.append("# Recent Ask Memory\n\n" + recent)
> --- `src/llm_wiki_mcp/context_api.py`

> return {"ok": True, **release_recursive_context_with_memory(
>     vault,
>     arguments.get("question", ""),
>     arguments.get("base_context", "")
> )}
> --- `src/llm_wiki_mcp/server.py`

#### MEM-RTE-cli-history
Label: CLI visible history

Distinct shipped caller-level retention/recovery layer compared with [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask). After a nonempty visible answer, `_record_visible_cli_ask_turn` builds a record, checks signatures against twelve recent disk rows, attempts recorder/metrics if not already present, and keeps a session copy. Software controls admission, with no per-answer review; history_enabled still governs underlying disk append. Failures are swallowed for continued UI use. CLI `/history` merges disk and session rows and displays the latest ten. This is not the final pack's source of session history.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: No result value; helper updates session list and may append persistent history/metrics.
- Later read-back: Session copies feed later `/history` displays in the same shell; successful file rows feed normal history readers across invocations.
- Delegated visibility: User sees merged question/answer display; no model delivery of session-only fallback is established.
- Selection predicate: Nonempty question/answer; signature deduplication; recent twelve file records and twenty session records checked, merged display limited to ten.
- Invalidation or expiry: Session list is process-local; disk compaction can remove exact rows; session-only records disappear on process exit.
- Activation or effect: Gives the history UI a recovery source after persistence failures; successful answer generation is not established by this helper.
- Evidence limits: No observed write failure/recovery. UI continuity does not prove durable memory or future model access. Generic API callers lack this CLI layer.

SRC-1: `src/llm_wiki_mcp/cli.py`. Open requests trigger this retention; no correctness oracle or candidate selection. Closest supplied ask route does not own this post-return CLI guard, so no duplicate route is intended.

> if not any(_visible_turn_signature(row) == sig for row in session_turns[-20:]):
>     session_turns.append(record)
> --- `src/llm_wiki_mcp/cli.py`

#### MEM-RTE-transcript-decision
Label: Transcript and decision admission

Part of: [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write)

Two exposed store/MCP admissions with different transformations: caller transcript becomes stripped nonblank line bullets clipped to 280 characters, overwriting the named page; caller decision/rationale/links become a SQLite decisions row plus appended Decision Log page entry. Human versus computational authorship is unresolved. Caller chooses content and can decline invocation, but code performs admission without separate review. These are open requests with no expected-answer oracle. Transcript clipping is deterministic reduction, not model synthesis. Decision rationale remains in the readable page and SQLite row; normal retrieval can read the page, while a dedicated later SQL decision-reader route is not established here. Failure between SQL commit and page update can leave only the SQL entry.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Transcript page creation metadata or decision ID/title/decision/links.
- Later read-back: Indexed transcript and Decision Log pages enter ordinary retrieval; the SQL record alone does not establish another later consumer.
- Delegated visibility: MCP caller receives metadata; providers see only subsequently selected page passages.
- Selection predicate: Caller-selected transcript/title or decision/rationale/links; code clips each transcript line and always appends decision text.
- Invalidation or expiry: Transcript reimport overwrites its page; normal page edits/delete can change both readable artifacts; no automatic prior-version restoration is shown.
- Activation or effect: Creates derived conversation knowledge or retained decision reasons available to future answers; improved answers are unobserved.
- Evidence limits: speaker_prefixes is accepted but unused in the inspected transcript body. Neither a summary label nor a rationale field establishes valid criticism or a theory-building loop.

SRC-1: `src/llm_wiki_mcp/server.py`. The parent route covers generic page admission; this part adds the material specialized transformations and SQL/readable split.

> if len(ln) > 280:
>     ln = ln[:277] + '...'
> bullets.append(f'- {ln}')
> --- `src/llm_wiki_mcp/server.py`

> self.update_page('Decision Log', entry, mode='append')
> return {'id': rowid, 'title': title, 'decision': decision, 'links': links}
> --- `src/llm_wiki_mcp/server.py`

#### MEM-RTE-page-withdrawal
Label: Page rename and withdrawal

Part of: [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write)

Caller-triggered store/MCP rename/delete changes active page availability. Code rejects missing source or occupied rename destination. Rename writes the new file, removes old file and optionally rewrites recognized wiki-link forms before reindex. Delete optionally copies a tombstone under vault `deleted/`, removes the page and reindexes. The caller controls the operation/tombstone option; no semantic approval or oracle is inserted. The shipped rule is structural file/link maintenance, not criticism of page truth. Tombstones preserve bytes but no automatic restore invocation is established by these methods.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Renamed titles/changed pages or deletion flag and predelete inbound links.
- Later read-back: Rebuilt index and live page scans reflect active files; deleted tombstones are outside normal wiki scans. Old answer history can still contain previously selected text.
- Delegated visibility: MCP caller receives result; no downstream host erasure contract is supplied.
- Selection predicate: Exact sanitized title and caller update_links/tombstone flags, not content evaluation.
- Invalidation or expiry: Removes or moves active Markdown and rebuilds index; methods do not remove matching sidecars, ingest provenance or history, and do not explicitly clear search caches.
- Activation or effect: Changes future live reads; cached selections, retained prompts and external copies prevent a whole-system forgetting guarantee.
- Evidence limits: No observed delete or concurrency/crash test. Orphan sidecars are not independently enumerated by page-driven note search, but a recreated same-name page can encounter an old note.

SRC-1: `src/llm_wiki_mcp/server.py`, `src/llm_wiki_mcp/context_api.py`. This explicit withdrawal part is not a replacement for the parent admission route.

> if tombstone:
>     shutil.copyfile(path, deleted_dir/f'{title}.{int(time.time())}.md')
> path.unlink(); self.reindex()
> --- `src/llm_wiki_mcp/server.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-context-pack](runtime.md#rt-obj-context-pack)

The prompt's recent-history section is derived from live JSONL question/answer text, not the archive and not past prompts verbatim. However, the separate recognized tool-evidence branch can also serialize `wiki_ask_history` results. The final executor returns sanitized full live rows, and the pack takes up to 6000 serialized characters of that result. Stored prompt fields can therefore enter this second channel; the recent-history budget is not a universal history-exposure budget. This qualifies the supplied object's wording about selected recent turns. SRC-1: `src/llm_wiki_mcp/context_api.py`.

> elif tool in {"wiki_capabilities", "wiki_tool_catalog", "wiki_command_tool_map", "wiki_ask_history"}:
>     # Keep runtime/tool evidence, but compact it.
>     source_sections.append(f"## Tool Evidence: {tool}\n\n```json\n" + _release_json.dumps(result, indent=2, ensure_ascii=False)[:6000] + "\n```")
> --- `src/llm_wiki_mcp/context_api.py`

#### On [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask)

Read-back includes code-mediated intent as well as model-visible text. `release_resolve_intent` reads recent questions and uses the last question to expand short follow-ups; that is symbolic selection acting on natural-language content before retrieval. The final model pack also includes recent-history Markdown and possibly full-row tool evidence, subject to source and whole-pack truncation. History framing says follow-up context, not immutable truth. Actual model compliance is unobserved. SRC-1: `src/llm_wiki_mcp/context_api.py`; [MEM-OBJ-ask-history](#mem-obj-ask-history).

> lines = ["# Recent Ask/Reply History", "", "These are recent local CLI ask turns. Use them for follow-up context, not as immutable truth.", ""]
> --- `src/llm_wiki_mcp/context_api.py`

#### On [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write)

Distinct admission mechanisms remain distinct. Direct bodies are caller-selected and existing files need overwrite permission. Provenance ingestion automatically decides new/changed/skip from paths/hashes/datestamps; apply authorizes a batch, not individual content truth. Page write precedes provenance recording, and the final ingest reindexes only after processed writes. Unchanged provenance can skip a source even when a separately deleted generated page is missing, except for the separately coded PDF refresh check. Notes are software-generated from page plus old-note terms and are immediately available to search; candidate-link promotion is a later editorial choice, not the note-write gate. Lint repair admission and before/after structural reports are as supplied, not a semantic quality oracle. SRC-1: `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/server.py`.

> wiki_path.write_text(content, encoding="utf-8")
> release_record_ingest_result(vault_path, p, wiki_title=title, wiki_path=str(wiki_path), action="updated_or_new")
> --- `src/llm_wiki_mcp/context_api.py`

#### On [RT-RTE-runtime-config](runtime.md#rt-rte-runtime-config)

The retained JSON is symbolic control state consumed by code: disabling history append does not erase existing history or inherently disable recent-history reads. The compressor is called after the append attempt even when history_enabled makes append return None. Thus retention admission and read-back are separate controls; an existing archive/live file can still be processed. SRC-1: `src/llm_wiki_mcp/context_api.py`.

> path = release_append_history(vault_path, record)
> release_compress_history_if_needed(vault_path)
> return {"history_file": path, "record": record}
> --- `src/llm_wiki_mcp/context_api.py`

## Write side

**Acquisition and authoring.** Pages admit caller text and extracted local files. The direct store ingestion can copy raw originals and overwrite generated pages; the provenance path records a source wrapper and hash metadata. Neither is an inference-backed synthesis or per-content human approval. Seeds initialize empty knowledge structure but do not establish a populated deployment corpus. The specialized transcript and decision producers retain clipped conversation text and supplied reasons respectively. See [MEM-OBJ-wiki](#mem-obj-wiki), [MEM-OBJ-provenance](#mem-obj-provenance), [MEM-RTE-transcript-decision](#mem-rte-transcript-decision) and the knowledge-write annotation.

**Transformation and maintenance.** Sidecar generation counts terms and scores links, then overwrites a template. Its readable summary is derived, but its mechanism does not warrant the AI label as a model-authoring claim. Indexing transforms page content into searchable tables and caches, with separate freshness limits. Structural repair can alter links, index navigation, short pages and missing-page stubs when enabled; structural before/after checks do not evaluate factual warrant. Documentation consolidation is separately governed by [RT-RTE-docs-consolidate](runtime.md#rt-rte-docs-consolidate), with generated Markdown and optional archive moves, not automatic executable deployment.

**Trace-fed retention.** The final agentic/unified plain recorder automatically retains question, first prompt, final answer and metadata; CLI's guard adds a session fallback. The source field is often a tool list. A failed or deterministic answer can be retained without correctness review. Compression transforms prior interaction traces into persistent natural-language answer prefixes, preserving source labels but losing full prompts and possibly reasons. The later recursive reader is concrete local wiring; model use beyond that tool return is not. This supports a trace-fed memory transformation, not a demonstrated increase in future capacity. Metrics independently retain sanitized provider answer/raw-response metadata when supplied by agentic generation, even if history append is disabled; live-history compaction does not remove these copies. Metrics/journal retention alone supplies no demonstrated learned policy. See [MEM-RTE-history-compaction](#mem-rte-history-compaction), [MEM-RTE-cli-history](#mem-rte-cli-history) and [MEM-OBJ-runtime-traces](#mem-obj-runtime-traces).

**Rejection, replacement and withdrawal.** Existing-title checks, unsupported update modes, dry-run/apply controls and ingest errors are structural admission controls. They do not reject false content. Caller edits/reingest overwrite pages; note reruns overwrite sidecars; delete/rename rebuild the index but do not retract historical prompts, provenance or external copies. Tombstones and archive files are preservation mechanisms, not general rollback. Live-history rewrite is destructive for removed exact history records, but does not erase independent provider-answer copies in metrics metadata. Those diagnostic copies do not guarantee exact prompt/turn reconstruction. No all-artifact transaction is established. See [MEM-RTE-page-withdrawal](#mem-rte-page-withdrawal) and [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write).

## Read-back

**Requested retrieval.** Store APIs and MCP expose pages, snippets, articles, context, history and recursive-context construction. Search input is the question/query, not merely a stored identifier. Page/note search ranks lexical matches with title/note/repetition bonuses; following-page search rereads full Markdown before creating a matched-window excerpt, avoiding the ordinary prefix-read cap. This alternative is wired as an exposed search capability, not guaranteed delivery through the final pack, whose evidence whitelist omits that tool name. Explicit title reads are address lookup rather than relevance selection. SRC-1: `src/llm_wiki_mcp/context_api.py`; [MEM-OBJ-notes](#mem-obj-notes), [RT-RTE-store-ask](runtime.md#rt-rte-store-ask).

**Automatic supply inside an ask.** Code selects live recent turns at each pack build, caps answer display text, trims history, allocates source text and trims the entire prompt. System/self-context precedes question and retrieved evidence, so tail loss preferentially removes evidence. A separate full-row history evidence channel can include prompt text; it competes for source/whole-pack space rather than only history_budget_tokens. Prior-question intent expansion can change retrieval even before model delivery. This is automatic inclusion triggered by a requested ask, not an independently scheduled unsolicited notification. See the context-pack/ask annotations and [RT-CLM-context-budget](runtime.md#rt-clm-context-budget).

**Diagnostic read-back.** [MEM-OBJ-runtime-traces](#mem-obj-runtime-traces) traces recent complete metrics rows through summary, usage and self-access APIs/MCP returns. Their metadata can include provider answers independently of live-history retention. CLI diagnostics display selected numeric/question fields instead. Diagnostic return to a host is not automatic insertion into the final model pack; downstream host interpretation and delivery remain uninspected. SRC-1: `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/server.py`, `src/llm_wiki_mcp/cli.py`.

**Working-context control.** There is no internal sub-agent frame in these inspected routes: code constructs prompts by value. Prefix truncation removes source tails; search windows bring on-disk passages back on demand; archive reduction retains a lossy older-history form reachable through a different tool. External files are not model-followable pointers automatically dereferenced in a window. Plain ask, store ask and second-pass synthesis have separate context selection/budget rules; first-pass debug does not prove what the eventual answer-producing request contained. [RT-RTE-plain-ask](runtime.md#rt-rte-plain-ask), [RT-RTE-store-ask](runtime.md#rt-rte-store-ask), [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask).

**Authority at the consumer.** Config and provenance influence executable code selection. Pages, sidecars and history influence model/human interpretation through evidence and instruction framing, not executable permissions. Prior-question resolution has a narrower code-level consequence. The archive's exposed consumer returns context to a host; actual host/model consumption remains uninspected. Recorded reasons in Decision Log can be retrieved as knowledge but are not shown to govern an automatic critic/revision loop. The supplied [RT-BAP-answer-guidance](runtime.md#rt-bap-answer-guidance) and [RT-BAP-config-control](runtime.md#rt-bap-config-control) remain the closest authority records; no duplicate paths are declared.

## Integration issues

1. **Qualification to supplied context-pack finding.** [RT-OBJ-context-pack](runtime.md#rt-obj-context-pack) says it contains selected recent question/answers rather than past prompts verbatim. That is true of recent-history Markdown, not necessarily the entire pack: `wiki_ask_history` full-row results can enter serialized tool evidence. The annotation supplies the exact branch. Consequence: do not classify history as only reduced answers or history_budget_tokens as a universal history exposure cap.
2. **Compaction is not automatic archive consumption by final ask.** [MEM-RTE-history-compaction](#mem-rte-history-compaction) and [MEM-RTE-recursive-context](#mem-rte-recursive-context) add concrete archive persistence/reader detail to [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask). The final ask's recent reader reads live rows; the explicit recursive tool can return archive text. No observed host/model use of that return is supplied.
3. **Additional operative parts, not competing route identities.** [MEM-RTE-transcript-decision](#mem-rte-transcript-decision) and [MEM-RTE-page-withdrawal](#mem-rte-page-withdrawal) are declared parts of the supplied knowledge-write route; [MEM-RTE-history-compaction](#mem-rte-history-compaction) is a maintenance part of the ask route with additional triggers. [MEM-RTE-cli-history](#mem-rte-cli-history) is a separate shipped caller layer. The new objects are retained substrates/contents, unlike the supplied current context pack. No exact duplicate record is identified.
4. **Unknown deployed corpus, caller identity and downstream use.** These prevent conclusions about human approval, source reliability, actual prompt activation and benefit across [MEM-OBJ-wiki](#mem-obj-wiki), [MEM-OBJ-ask-history](#mem-obj-ask-history) and [MEM-RTE-recursive-context](#mem-rte-recursive-context). Provider weights remain opaque under [RT-CMP-ollama-model](runtime.md#rt-cmp-ollama-model).
5. **Withdrawal/freshness and reconstruction limits.** [MEM-RTE-page-withdrawal](#mem-rte-page-withdrawal), [MEM-OBJ-pages-fts](#mem-obj-pages-fts) and [MEM-OBJ-provenance](#mem-obj-provenance) show why active-page removal is not whole-vault forgetting or automatic source restoration. Full writer/cache/concurrency audit remains uninspected; no universal immediate freshness claim is warranted.
6. **Diagnostic retention correction.** [MEM-OBJ-runtime-traces](#mem-obj-runtime-traces) corrects this report's previous exclusion of full answer bodies: sanitized provider answer/raw-response metadata can persist independently of live-history admission/compaction and return in recent diagnostic rows. It does not establish automatic model delivery or exact prompt reconstruction. The record also separates actual final metrics recording from journal helper capability. Old definitions and command-map labels cannot prove current final automatic journal writes or score-driven learning. No correction to the supplied runtime's positive metrics finding is needed.

7. **Navigation/guidance inventory limit.** SRC-1 `src/llm_wiki_mcp/server.py` also supplies `toc` (generated Table of Contents wiki page) and `schema_doc` (separate vault `schema.md`, caller replacement or default initialization, returned to its caller). This correction round directly read those bodies, but did not trace all dispatch/read-back consumers of schema guidance. The wiki object is not an exhaustive inventory of editable instructions; complete instruction-surface and maintenance-route comparisons remain prevented. No automatic final-model schema delivery is established.

> schema_path=self.cfg.vault/'schema.md'
> if update and body is not None:
>     schema_path.write_text(body.strip()+'\n', encoding='utf-8')
> --- `src/llm_wiki_mcp/server.py`

## Limitations and checks

Source identity was rechecked with Git HEAD at the boundary revision. Analysis used only the supplied invocation/contracts, supplied boundary/runtime and registered frozen SRC-1 source; no other run or prior review was consulted. Repeated-definition risks were handled by inspecting final exported context/ask/search/ingest bodies and distinguishing explicit older helpers still called by wrappers. The method is source tracing, not execution, a correctness audit or an experiment.

Available but incompletely inspected evaluator bodies, page-marker window internals, startup-command execution, every malformed configuration edge and cross-writer cache/crash behavior prevent exhaustive correctness claims. Startup settings are covered as retained configuration, not asserted to execute automatically. Provider training/state and external host authorization/context remain outside the frozen implementation. Exact history fidelity is already limited by second-pass prompt mismatch, sanitizer/display reduction, full-row secondary exposure and destructive compaction. These limits do not erase the positive implemented memory paths.

Validation: the required invocation-specific `commonplace-run validate-output` check passed; it checks form and quotation occurrence, not analytical correctness, observed activation, causal benefit or coordinator acceptance.
