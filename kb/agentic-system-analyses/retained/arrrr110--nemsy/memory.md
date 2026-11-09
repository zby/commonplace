---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Nemsy memory: Markdown derivation and recency-window read-back, conversation saving, status metadata and browser consumption."
run-id: AAS-2026-11-09-nemsy-2a6b7963bf65-01
source-identity: https://github.com/arrrr110/nemsy
reviewed-boundary: "2338bab0aab96a91efb90a80249f33510b630260"
---

# Nemsy memory report

## Boundary and evidence

This member covers Nemsy's shipped document-to-Wiki and conversation-to-Wiki retention, query archives, Wiki selection, context lifetime, status/accounting records, maintenance advice, exposed storage helpers and browser reading. The frozen boundary and SRC-1 declaration are in [boundary](boundary.md#source-register). Evidence is implementation and task-prompt/configuration intent at commit 2338bab0aab96a91efb90a80249f33510b630260, not observed operation. No user Vault, service trace, provider cache state or evaluation result is supplied. Provider hidden state remains opaque; development-assistant rules and roadmap material retain the boundary's exclusions.

Direct reads covered `src/nemsy/agent.py`, `src/nemsy/vault.py`, `src/nemsy/config.py`, `src/nemsy/schema.py`, `config/settings.toml`, `config/_index.example.md`, `pyproject.toml`, `tests/test_smoke.py`, the operative endpoint range of `src/nemsy/web.py`, chat/save/context branches of `src/nemsy/cli.py`, message construction in `src/nemsy/llm.py`, `frontend/src/App.tsx`, `frontend/src/views/Chat.tsx`, the acquisition/preview/filter portion of `frontend/src/views/FileLibrary.tsx`, and `frontend/src/components/MessageContent.tsx`. Remaining dispatch, wrapper and deployment details use the supplied runtime account; they are not represented as fresh direct inspection.

| Entry point or operation | Source paths (SRC-1) | Coverage and limit |
|---|---|---|
| CLI ingest, inline ingest, HTTP ingest | `src/nemsy/agent.py`, `src/nemsy/vault.py`, `src/nemsy/cli.py`, `src/nemsy/web.py` | Direct parser/storage/HTTP reads plus supplied [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest); [MEM-OBJ-source-page](#mem-obj-source-page), [MEM-OBJ-ingest-log](#mem-obj-ingest-log). |
| Ancestor guidance | `src/nemsy/vault.py`, `config/_index.example.md` | Direct reads; [MEM-OBJ-index-guidance](#mem-obj-index-guidance). Actual user guidance and initial author identity unavailable. |
| Query, optional answer archive, reasoning alternative | `src/nemsy/agent.py`, `src/nemsy/web.py`, `src/nemsy/cli.py` | Direct ordinary archive/HTTP reads; supplied reasoning defect [RT-RTE-reasoning-query](runtime.md#rt-rte-reasoning-query); [MEM-OBJ-query-page](#mem-obj-query-page). |
| Chat history and Wiki snapshot; mode switching | `src/nemsy/cli.py`, `src/nemsy/web.py`, `frontend/src/views/Chat.tsx`, `frontend/src/App.tsx` | Direct context/trimming/browser reads; annotation on [RT-RTE-conversation-chat](runtime.md#rt-rte-conversation-chat). |
| Save insight, CLI confirmation, browser archive | `src/nemsy/agent.py`, `src/nemsy/cli.py`, `frontend/src/views/Chat.tsx` | Direct reads; [MEM-OBJ-insight-page](#mem-obj-insight-page), [RT-RTE-insight-save](runtime.md#rt-rte-insight-save). |
| Recency loader and index append | `src/nemsy/agent.py`, `src/nemsy/vault.py` | Direct reads; [MEM-OBJ-wiki-index](#mem-obj-wiki-index), annotation on [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer). |
| File library, citation resolve and file preview | `src/nemsy/web.py`, `frontend/src/views/FileLibrary.tsx`, `frontend/src/views/Chat.tsx`, `frontend/src/components/MessageContent.tsx` | Direct reads; [MEM-RTE-browser-read](#mem-rte-browser-read). Human-directed file reading differs from model-context selection. |
| Lint, smoke evaluation, cleanup | `src/nemsy/agent.py`, `src/nemsy/web.py`, `tests/test_smoke.py`, `src/nemsy/vault.py` | Direct reads; [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint), [MEM-OBJ-operation-log](#mem-obj-operation-log). No evaluated repair is installed by these paths. |
| Status and accounting | `src/nemsy/vault.py`, `src/nemsy/web.py`, `src/nemsy/cli.py` | Direct store/HTTP-source reads, supplied CLI/status wiring; [MEM-OBJ-token-log](#mem-obj-token-log), [MEM-OBJ-ingest-log](#mem-obj-ingest-log). |
| Exposed read/search/write/append/delete helpers | `src/nemsy/vault.py` | Direct reads; storage capabilities, not unspecified external-consumer routes. [MEM-CLM-storage-lifecycle](#mem-clm-storage-lifecycle). |
| Configured history/cache directories, hooks/tools | `src/nemsy/config.py`, `pyproject.toml`, `src/nemsy/llm.py` | Direct directory/reference search plus runtime wrapper inspection; [MEM-ABS-history-store](#mem-abs-history-store). No separate plugin or model-tool retention path established. |
| Opaque remote generation state | `src/nemsy/llm.py`, `config/settings.toml` | Supplied [RT-CMP-deepseek](runtime.md#rt-cmp-deepseek); provider state, exact weights and cache effectiveness uninspected. Prevents claims of comprehensive memory or fixed provider internals. |

## Core ideas

Nemsy's durable behavioral material is readable Markdown, not a learned vector store. Source summaries, archived answers and rewritten conversations share the same later Wiki loader despite different origins and checks. The loader privileges index text and recent modification times, not question-specific retrieval. Page labels, tags and source metadata do not establish epistemic trust or determine model admission. See [MEM-OBJ-source-page](#mem-obj-source-page), [MEM-OBJ-query-page](#mem-obj-query-page), [MEM-OBJ-insight-page](#mem-obj-insight-page), and [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context).

The source hash ledger is a second kind of memory: it changes whether CLI work is attempted, without contributing knowledge to the answer model. Accounting logs have still different consumers. Keeping these apart matters because a recorded ingestion can suppress retries even when no page was generated, while an index entry can survive page deletion. See [MEM-OBJ-ingest-log](#mem-obj-ingest-log) and [MEM-CLM-storage-lifecycle](#mem-clm-storage-lifecycle).

Saving conversation is an explicit trace-fed transformation, not automatic history compaction. The caller chooses when and which history to supply; software admits the model's rewritten page without reviewing its propositions. Later requests can consume that derived page, but persistence and delivery do not demonstrate improved capacity or reliable source fidelity. See [RT-RTE-insight-save](runtime.md#rt-rte-insight-save) and its annotation below.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-source-page
Label: Source summary page

SRC-1: `src/nemsy/agent.py`, `src/nemsy/schema.py`. Distinct output object of [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest); no supplied object counterpart. Stored as UTF-8 Markdown in Wiki `sources/<sanitized-title>-<date>.md`. Natural-language summary, relationships and questions reach later generation as uninterpreted file text; frontmatter has symbolic display/type uses in the browser, but is not a truth gate or model-context selector. The original document remains separate: ingest reads rather than rewrites it. The derived page comes from source text, ancestor guidance and selected existing Wiki text, so it is not necessarily a pure extract of one external document.

The parser requires SUMMARY, unwraps an outer code fence, removes an embedded questions heading and appends separately parsed QUESTIONS. Missing SUMMARY returns None; present SUMMARY is accepted without schema or truth validation. The source-path provenance field is requested in schema text, not independently filled by this parser. Original reasoning and verbatim evidence need not survive this transformation; later consumers receive the resulting page, not the original prompt or full response. Filename collisions overwrite rather than create versions. Implementation conclusion status: wired; operation conclusion status: uninspected.

> summary_content = summary_match.group(1).strip()
> --- `src/nemsy/agent.py`

> summary_content = summary_content + "\n\n---\n\n## 待探索问题\n\n" + questions_text
> --- `src/nemsy/agent.py`

#### MEM-OBJ-query-page
Label: Archived query page

SRC-1: `src/nemsy/agent.py`, `src/nemsy/schema.py`. Distinct output of [RT-RTE-answer-archive](runtime.md#rt-rte-answer-archive), not another declaration of that route. Filesystem Markdown in `queries/` contains question heading, answer minus ARCHIVABLE marker, and code-made type/title/date/tags metadata. Natural-language synthesis has mixed lineage through selected pages and model generation; metadata is symbolic for browser display. Ordinary archive makes no second synthesis call or per-answer truth check. Later Wiki loading treats this output like other recent pages, allowing generated answers to become input to future answers. It retains only reasoning actually present in answer text, not provider hidden thinking or the original selection window. The supplied reasoning tuple mismatch and unused HTTP archive flag limit reachable successful archives. Implementation conclusion status: wired; operation conclusion status: uninspected.

> metadata = make_query_metadata(title=question, date=str(date.today()))
> write_wiki_note(filename, content, metadata=metadata)
> --- `src/nemsy/agent.py`

#### MEM-OBJ-insight-page
Label: Rewritten conversation insight

SRC-1: `src/nemsy/agent.py`, `frontend/src/views/Chat.tsx`. Distinct output of [RT-RTE-insight-save](runtime.md#rt-rte-insight-save). UTF-8 Markdown in `insights/` contains model-authored natural-language conclusions and any background/derivation it follows instructions to retain; frontmatter title also supplies the sanitized filename. The raw input mixes user and assistant messages, potentially including earlier Wiki-derived answers. Browser save includes history through the selected answer. An optional topic focuses rewriting. No newly loaded Wiki enters the save call even though associated-knowledge links are requested.

The model receives a fresh, separately constructed messages list containing formatted history, not the live chat request frame; only the rewritten page returns to retention. The source conversation is not durably checkpointed by this function. This is a trace-fed write of behavior-shaping text, with later knowledge authority through Wiki context, not parameter learning. Retained rationale is requested but not guaranteed or separately validated; if present it reaches later consumers only with the page selected. No supplied object counterpart; implementation conclusion status: wired; operation conclusion status: uninspected.

> ## 背景与推导
>
> <这些洞见是如何在对话中形成的，简要说明>
> --- `src/nemsy/agent.py`

> system, messages = llm.build_messages(
>     _SAVE_SYSTEM.format(wiki_path=settings.vault.wiki_path), [], user_prompt
> )
> --- `src/nemsy/agent.py`

#### MEM-OBJ-wiki-index
Label: Wiki index

SRC-1: `src/nemsy/agent.py`, `src/nemsy/vault.py`. Separate Markdown file `index.md`, automatically initialized when absent and appended after ingest/archive/save. No supplied object counterpart; used by the supplied answer/ingest/lint/chat routes. The model receives its natural-language summary lines and wikilinks as text. Links function as human/browser navigation tokens; the model loader does not follow each link to fetch all its destinations. Thus always including index does not imply including every indexed page. Titles and summary lines derive from source title, question or generated insight title, not a separate curator's judgment.

Initialization uses metadata; later additions append a dated entry, without deduplication or replacing an obsolete entry. Index is prioritized outside the recent-page count and read in full, so count limiting alone does not bound total input size. Implementation conclusion status: wired; operation conclusion status: uninspected.

> entry = f"- [[{stem}]] — {summary_line} （{date.today()}）\n"
> --- `src/nemsy/agent.py`

> context_parts.append(f"=== {settings.vault.wiki_index_file} ===\n{index_path.read_text(encoding='utf-8')}")
> --- `src/nemsy/agent.py`

#### MEM-OBJ-index-guidance
Label: Ancestor directory guidance

SRC-1: `src/nemsy/vault.py`, `config/_index.example.md`, `src/nemsy/agent.py`. Filesystem `_index.md` prose supplies domain, collection intent, tags and viewpoint preferences to ingest's user prompt. Static template is shipped instruction, not accumulated memory; actual local guidance may be authored/edited outside the inspected application. Its initial authorship and per-content human control remain unresolved. Runtime code selects extant nonempty ancestor files, farthest first, stopping at raw root when reached or filesystem root otherwise. The guidance is not a generated source page in ordinary directory collection, though direct-file exceptions in [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest) prevent a universal exclusion claim.

This object is distinct from index.md and all supplied records. Natural-language authority acts at the ingest model, not by code-enforced tag validation. Its source markers retain local directory lineage in the prompt; guidance is not automatically copied verbatim into the resulting summary. Implementation conclusion status: wired; operation conclusion status: uninspected.

> found.append(f"<!-- 目录语境：{rel_label} -->\n{text}")
> --- `src/nemsy/vault.py`

#### MEM-OBJ-ingest-log
Label: Ingest status ledger

SRC-1: `src/nemsy/vault.py`, `src/nemsy/cli.py`, `src/nemsy/web.py`. Distinct retained control object used by [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest). JSON file adjacent to configured history directory, ordinarily `.nemsy/ingest_log.json`; symbolic version-2 dictionary keyed by resolved source path. Stores stripped-content hash, previous hash, byte size, status, mode, timestamps and associated page path. It is access/progression metadata, not retained document meaning. Code authors/adopts records after attempted ingestion or empty-source handling; there is no per-record human approval.

CLI get_file_status compares current stripped hash against the ledger, not page existence or generation quality. Web sources display instead compares source mtime against last ingestion time, with zero-byte empty detection. FileLibrary filters visible actions by this display status and locally marks HTTP success done without checking page content. A ledger fallback to empty v2 on missing/invalid/old-format data can make material appear new; it is not a recovery of prior page versions. Returned page None preserves any existing wiki_page pointer. Implementation conclusion status: wired; operation conclusion status: uninspected.

> "prev_hash": existing.get("hash"),  # 记录上一次的 hash
> --- `src/nemsy/vault.py`

> "wiki_page": wiki_page or existing.get("wiki_page"),
> --- `src/nemsy/vault.py`

> if record.get("hash") == current_hash:
>     return "done"
> --- `src/nemsy/vault.py`

#### MEM-OBJ-token-log
Label: Token accounting ledger

SRC-1: `src/nemsy/vault.py`, `src/nemsy/agent.py`, `src/nemsy/web.py`. Distinct symbolic JSON list at `.nemsy/token_log.json` beside configured history directory. Code appends timestamp, command, model and usage counts from completed model calls. It does not retain the prompt, answer, criticism or expected outcome. summarize_token_log aggregates by command/model for status consumers; supplied runtime describes CLI and HTTP status wiring. No inspected generator uses these aggregates to select knowledge, revise prompts or admit improvements. This object differs from both ingest-control and natural-language Wiki memory. Implementation conclusion status: wired; operation conclusion status: uninspected.

> records.append(entry)
> log_path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
> --- `src/nemsy/vault.py`

#### MEM-OBJ-operation-log
Label: Wiki operation log

SRC-1: `src/nemsy/vault.py`, `src/nemsy/agent.py`. `log.md` contains appended timestamp/operation/title/detail entries. Symbolic operation labels and readable prose describe actions, not full interaction traces or verified semantic changes. Code admits entries without human review. The normal model-context loader excludes this filename, whereas recursive browser Wiki listing can expose it. Lint's completion log survives, but its diagnostic report is returned rather than installed or saved here. No supplied object counterpart; related supplied route is [RT-RTE-wiki-lint](runtime.md#rt-rte-wiki-lint). Implementation conclusion status: wired; operation conclusion status: uninspected.

> _skip = {settings.vault.wiki_index_file, settings.vault.wiki_log_file}
> --- `src/nemsy/agent.py`

### Routes

#### MEM-RTE-browser-read
Label: Browser file and citation reading

SRC-1: `src/nemsy/web.py`, `frontend/src/views/FileLibrary.tsx`, `frontend/src/views/Chat.tsx`, `frontend/src/components/MessageContent.tsx`. No supplied route counterpart after comparison with [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer) and [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context): this route ends at a human-facing read, not a generation-model invocation. FileLibrary mounts, fetches source/Wiki metadata, filters names locally and requests a chosen file; browser code renders the returned content. Chat citation buttons resolve model-emitted page tokens to a file stem and open the file API in another tab, which returns JSON content rather than a generation prompt. Owner: browser interaction and endpoint code.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Wiki/source listings, raw UTF-8 file content or 404/403; file-library preview renders content and chat reference opens a file response.
- Later read-back: Retained Wiki pages or source documents reach a later browser reading on explicit selection; no automatic forwarding of the read file into a chat call.
- Delegated visibility: Human-facing browser receives content; no model or worker call is made by these read endpoints.
- Selection predicate: FileLibrary title/path substring filters and explicit absolute path; citation resolve matches case-insensitive stem after stripping .md and returns the first matching listed note. No token/page count budget for the selected file.
- Invalidation or expiry: A new file request reads current disk content; already displayed content has no automatic freshness or retraction protocol in the inspected branch.
- Activation or effect: Makes file content and citation destinations inspectable; correctness of the citation's substantive support and human reliance remain unobserved.
- Evidence limits: Endpoint returns content under a lexical Vault check, not proven canonical containment; duplicate stems and invented model citations need not resolve uniquely or correctly. Displaying a source does not establish warrant for an answer.

> if note.stem.lower() == target:
>     return {"title": title, "abs_path": str(note), "rel_path": str(note.relative_to(wiki_path))}
> --- `src/nemsy/web.py`

> .then((d) => { setPreviewContent(d.content); setPreviewLoading(false) })
> --- `frontend/src/views/FileLibrary.tsx`

### Claims

#### MEM-CLM-storage-lifecycle
Label: Storage mutation is not a synchronized knowledge lifecycle

SRC-1: `src/nemsy/vault.py`, `src/nemsy/agent.py`, `tests/test_smoke.py`. Related supplied [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest) and [RT-RTE-insight-save](runtime.md#rt-rte-insight-save) describe writes; this claim distinguishes storage capability from withdrawal propagation. write_wiki_note, append_wiki_note, read_note and search_notes expose library operations, but a hypothetical external caller establishes no additional deployed read-back/admission route. Search is escaped case-insensitive text matching over collected source files, not the query model's Wiki selector. delete_wiki_note requires caller-supplied confirmed=True and unlinks the file; no call site was found in searched `src/` and `frontend/src/`. Its caller's identity and actual confirmation remain external to this helper. It does not repair the index, ingest ledger or already supplied context. Same-path writes are replacement without version capture. Guarantee strength: no claimed guarantee; implementation conclusion status: afforded; operation conclusion status: uninspected.

Deleting a page can remove it from fresh loaders, but cannot withdraw bytes from an existing CLI snapshot or prior generated derivatives. Re-ingest may append a new index entry while overwriting a same-day file or leaving a differently dated older page. Tests explicitly leave generated Wiki content for manual cleanup; they are definitions, not successful cleanup or retention-quality evidence.

> path.unlink()
> return True
> --- `src/nemsy/vault.py`

> 测试会调用真实 LLM API，测试完成后生成的 Wiki 内容需手动清理。
> --- `tests/test_smoke.py`

### Evidenced absences

#### MEM-ABS-history-store
Label: No implemented history/cache checkpoint in inspected product paths

SRC-1: `src/nemsy/config.py`, `src/nemsy/cli.py`, `src/nemsy/vault.py`, `frontend/src/views/Chat.tsx`, `frontend/src/App.tsx`. Conclusion status: absent. At the frozen revision, bounded `rg` search of `src/` and `frontend/src/` for history_dir, summary_cache_dir, localStorage and sessionStorage found directory configuration/creation and sibling ledger-path construction, not history serialization or summary-cache read-back. Direct CLI/chat reads show in-memory history; direct browser state initializes messages empty and App conditionally mounts Chat. This supports absence of a shipped cross-session history/summary checkpoint in those paths, not absence of all memory: explicit insight saving is a counterexample to that stronger statement. No hidden provider-state conclusion follows.

> self.memory_history_dir.mkdir(parents=True, exist_ok=True)
> self.memory_summary_cache_dir.mkdir(parents=True, exist_ok=True)
> --- `src/nemsy/config.py`

> const [messages, setMessages] = useState<Message[]>([])
> --- `frontend/src/views/Chat.tsx`

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer)

SRC-1: `src/nemsy/agent.py`. Request direction is caller question → code-selected Wiki window → model, not a question-indexed search API. The automatic selector operates on all recursive Markdown paths, excludes index/log names from the recent-page set, sorts by mtime and takes up to thirty other files. Index is included separately in full. No per-file clipping or input-token budget is applied here. Natural-language page content reaches the user prompt; text frontmatter/tags are not parsed for model retrieval. Recency/count limits can omit the relevant page, while an old page's index mention survives without its body. There is no model-accessible follow-link tool wired by this route. Fresh load or explicitly supplied context determines freshness; supplied context can preserve an older selection.

> content = f.read_text(encoding="utf-8")
> context_parts.append(f"=== {rel} ===\n{content}")
> --- `src/nemsy/agent.py`

#### On [RT-RTE-conversation-chat](runtime.md#rt-rte-conversation-chat)

SRC-1: `src/nemsy/cli.py`, `src/nemsy/web.py`, `frontend/src/views/Chat.tsx`, `frontend/src/App.tsx`, `config/settings.toml`. Wiki context is a plain string snapshot, not a reference back to live pages: CLI selects twenty other pages at session start, Web at each request. Positive CLI max_turns removes oldest message pairs only after a turn (and after the optional save prompt); default zero leaves them all. What survives is the verbatim tail, not a summary/pointer to evicted turns. Discarded history cannot be reconstructed by the configured history directory. A separately saved insight can later re-enter via Wiki selection; it does not restore the raw chat.

Browser filters streaming/empty messages for chat input, omits all history in Wiki mode, but keeps the visible array across mode switches. Stopped partial or error-appended text can become eligible once marked nonstreaming. Leaving Chat for a different App view unmounts its local state; unlike a mode switch this can lose unsaved conversation. No isolated agent delegation or frame-return memory is established here. In the frame analogy, Wiki-mode calls keep conversation outside that invocation, while the array remains available for later Chat calls; CLI trimming instead destroys old local values without a reload pointer.

> const history = messages
>   .filter((m) => !m.streaming && m.content)
>   .map((m) => ({ role: m.role, content: m.content }))
> --- `frontend/src/views/Chat.tsx`

> {view === 'chat'     && <Chat />}
> --- `frontend/src/App.tsx`

#### On [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)

SRC-1: `src/nemsy/agent.py`, `src/nemsy/vault.py`. Admission remains software/model controlled after caller operation approval. The directory guidance's human-authorship template is not evidence of actual human authorship of local guidance or source text. The raw source is presented with ten other Wiki pages, or fifty with wide, plus index, without an input-token limit. Parsed source summary/questions are the retained result; the original full response is not a raw-trace store. Existing-page relationship instructions do not implement edits to each related page. Ledger writes can outlive failed page parsing; there is no stored criticism causing automatic correction/rejection of the retained propositions.

> wiki_context = _load_wiki_context(max_files=50 if wide else 10)
> --- `src/nemsy/agent.py`

#### On [RT-RTE-insight-save](runtime.md#rt-rte-insight-save)

SRC-1: `src/nemsy/agent.py`, `frontend/src/views/Chat.tsx`. This is the explicit trace → derived insight → later Wiki-model chain. Human CLI/browser selection starts it, but does not approve the particular rewritten text; HTTP can supply arbitrary nonempty history without proving a human selected it. Code/model supply content admission and title extraction. It is not automatic trace accumulation or enforced history compaction: history is neither replaced with the new page nor durably copied. Background and derivation are requested; later answers can receive them if retained and selected, not through a dedicated rationale consumer. No improvement or faithful retention experiment is supplied.

> const historyForSave = [
>   ...messages
>     .slice(0, msgIndex)
>     .filter((m) => !m.streaming && m.content)
>     .map((m) => ({ role: m.role, content: m.content })),
>   { role: 'assistant' as const, content: msg.content },
> ]
> --- `frontend/src/views/Chat.tsx`

#### On [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context)

SRC-1: `src/nemsy/agent.py`, `src/nemsy/web.py`. Retained page authority is natural-language influence over later generation within each invocation; preservation on disk can span sessions but selection gates actual delivery. User sources, generated summaries, generated answers and conversation insights are not assigned separate trust checks by the loader. Page prose can appear in the chat system prefix; code does not distinguish embedded page instructions from reliable knowledge. No semantic output validator establishes obedience. The producer's model-generated title/type/source labels do not independently authenticate claims. Symbolic ledger hashes instead have deterministic skip authority at the CLI driver, not truth authority at the answer consumer.

## Write side

Acquisition is caller-directed local-file reading or supplied chat history. Initial source/guidance provenance is unresolved, but subsequent transformations are inspectable. For ingest, the model proposes source Markdown, Python admits a SUMMARY-delimited result, normalizes questions/fences and writes page/index/log/ledger separately. For answer archive, the explicit flag admits the answer with fixed metadata, regardless of ARCHIVABLE. For save, a caller-selected history is rewritten in a separate model call, then written without per-content review. See [MEM-OBJ-source-page](#mem-obj-source-page), [MEM-OBJ-query-page](#mem-obj-query-page), [MEM-OBJ-insight-page](#mem-obj-insight-page) and their supplied routes.

These admissions are not equivalent to human editing/approval: a person may supply or edit files in the surrounding filesystem, but the shipped browser preview is read-only and the inspected generation writers do not wait for the new page's text to be approved. Generic HTTP request identity leaves human participation unresolved. Rejection is syntactic (missing SUMMARY or empty save history), not an evaluated semantic veto. Source counters/hashes can still signal completion without a usable page; HTTP force/archive fields do not enforce CLI parity. The supplied runtime's forcing cases remain consequential, not corrected away by the memory account.

Maintenance includes overwriting/regenerating pages, appending index/log entries, and model lint advice. Lint sends index plus fifty other recent pages and returns suggestions without installing them. Smoke definitions inspect basic metadata/body/answer/archive existence, not a production admission gate or successful measured improvement. Deletion is only a confirmation-argument storage helper in the inspected call graph; no synchronized withdrawal, derivative invalidation or transaction restores prior content. [MEM-CLM-storage-lifecycle](#mem-clm-storage-lifecycle) and [MEM-OBJ-ingest-log](#mem-obj-ingest-log) delimit recovery.

## Read-back

Model read-back is request-triggered code selection followed by prompt delivery, not unsolicited background memory injection. Budgets are page counts plus an unbounded index, not input tokens: ingest ten/fifty, ordinary query thirty, chat twenty, lint fifty. A user query does not change the page selector. The model can interpret the delivered window but cannot fetch a missing page through an inspected registered tool. Different configured output-token limits do not impose a local input-selection budget. Actual provider overflow/truncation/cache behavior remains uninspected. See the answer/chat/ingest annotations and [RT-CMP-deepseek](runtime.md#rt-cmp-deepseek).

Human read-back is separate: [MEM-RTE-browser-read](#mem-rte-browser-read) retrieves a chosen retained file with no recency restriction or automatic subsequent model forwarding. Status read-back is also separate: source metadata informs displayed new/changed/done badges, CLI hashes determine pending ingestion and token aggregates inform accounting. None of these metadata read paths is evidence of trace-derived knowledge revision. The configured history/cache names do not establish another checkpoint form; [MEM-ABS-history-store](#mem-abs-history-store) retains the bounded search and counterexample of explicit insight saving.

## Integration issues

- No correction to supplied runtime facts is proposed. The storage/page declarations have no supplied object counterparts; their generating routes are cited rather than redeclared. [MEM-RTE-browser-read](#mem-rte-browser-read) adds the human consumer omitted from the model-answer route, not a duplicate of it.
- [MEM-OBJ-ingest-log](#mem-obj-ingest-log) adds an important distinction: HTTP source display uses mtime while CLI pending selection uses stripped-content hashes. A displayed done badge or successful HTTP response is not evidence of a semantically valid page; this reinforces rather than replaces [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest).
- [MEM-CLM-storage-lifecycle](#mem-clm-storage-lifecycle) overlaps runtime's generic effects/recovery discussion, but is a claim about separate helper capability and incomplete withdrawal propagation, not an alias of a supplied route. Reconciliation should preserve the distinction between API capability and a wired consumer.
- Local source/guidance authorship, actual retained reasoning quality, provider hidden state/cache behavior and activation of particular retained claims remain unresolved for the evidence limits stated above. No unavailable operational fact is silently inferred from file labels. These prevent empirical fidelity, learning, deployment-cache or improvement conclusions, not the implemented read-back account.

## Limitations and checks

The source HEAD was rechecked as 2338bab0aab96a91efb90a80249f33510b630260 and short status was empty. Identity matches the supplied boundary/run; no source was added. The assigned job, member/boundary/runtime types, collection, worker rules and full records contract were read before source analysis. Only the authorized candidate output and optional empty answers are written; no target execution, test, service call or dependency installation was performed.

Counterexamples considered include direct-file ingestion bypassing directory exclusions, source-ledger completion without a summary page, Web fields not enforcing CLI archive/force behavior, browser mode changes preserving visible messages, and index inclusion without target-body inclusion. These prevent stronger claims about universal filtering, retention success, context isolation and complete retrieval. The report establishes wiring/capability and requested model behavior, not observed operation, activation, causal benefit or comprehensive provider memory. Deterministic validation: passed using the assigned commonplace-validate command; quotation occurrence and structural conformance do not establish semantic correctness or workflow acceptance.
