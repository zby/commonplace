---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Nemsy runtime baseline: local document ingestion, CLI and Web question answering, conversation saving and maintenance at the frozen revision."
run-id: AAS-2026-11-09-nemsy-2a6b7963bf65-01
reviewed-boundary: "2338bab0aab96a91efb90a80249f33510b630260"
---

# Nemsy runtime report

## Runtime account

Nemsy is a caller-directed knowledge assistant, not an inspected autonomous tool-execution loop. Python selects files and context, makes a model request and processes returned text. The model supplies summaries, answers, insights or maintenance suggestions; Python owns the next executable step and filesystem effects. This account uses SRC-1 implementation and shipped prompt/configuration intent only. No supplied execution trace or causal experiment establishes actual model compliance, cache benefit, successful deployment or knowledge improvement. Inspection covers the boundary's included Python implementation and the browser Chat caller, with additional focused tracing of configuration, smoke assertions and FileLibrary ingestion; these are all at the boundary revision, not new sources.

### Entry paths and ordinary work

`pyproject.toml` registers `nemsy`, `nemsy-smoke` and `nemsy-web`. The main Click group defaults to chat and also exposes ingest, query, lint, status, sources and web. Web startup hosts FastAPI and conditionally serves `frontend/dist`; `uvicorn nemsy.web:app` is another documented startup path. The optional Web dependencies and runtime-relative lookup of frontend/config files matter: a checkout includes them, but the wheel configuration names only `src/nemsy`. Source presence does not establish that an installed wheel supplies a functioning browser deployment (SRC-1: `pyproject.toml`, `src/nemsy/cli.py`, `src/nemsy/web.py`, `src/nemsy/config.py`).

An ordinary document-to-answer sequence follows [RT-RTE-document-ingest](#rt-rte-document-ingest), then [RT-RTE-wiki-answer](#rt-rte-wiki-answer). A human selects a local text document. CLI code resolves the path, collects eligible files, reads UTF-8 text and determines status from stripped-content hashes. For a pending document it reads ancestor `_index.md` guidance, loads the Wiki index plus up to ten recently modified other pages (fifty with `--wide`), and calls the configured model. Source title, source body, directory guidance and current Wiki text enter one user prompt; fixed task instructions and the schema enter the system argument. The API receives the local document and selected Wiki text, so the filesystem boundary is not a confidentiality boundary against the configured service. Code streams text or awaits one full response, logs token usage, extracts SUMMARY/QUESTIONS, writes the summary page, appends an index entry, logs the operation and records the source hash. A later query loads up to thirty recent other pages plus index and asks for a Wiki-grounded answer. There is no question-dependent page selector in `_load_wiki_context`; relevance selection within the supplied text is requested of the model (SRC-1: `src/nemsy/cli.py`, `src/nemsy/agent.py`, `src/nemsy/vault.py`, `src/nemsy/llm.py`).

The default chat path holds an in-process history and a Wiki snapshot loaded once at session start. Each ordinary turn sends the snapshot, instructions, history and current input; response text returns to the console and enters history. Inline commands run code-selected operations rather than model-selected tools. Ingesting or saving during that chat does not refresh its Wiki snapshot. Positive `max_turns` discards the oldest history messages after a completed turn; the shipped value is zero, meaning no such trimming. There is no summary substitute in this trimming branch. New retained pages can reappear through a fresh context load, not through a pointer in the discarded history. Web chat instead reloads Wiki context on each request and accepts caller-supplied history. Browser Wiki mode sends no history, although mode switching does not erase the displayed message array; switching back to Chat can include earlier Wiki-mode messages. These distinctions are detailed in [RT-RTE-conversation-chat](#rt-rte-conversation-chat) (SRC-1: `src/nemsy/cli.py`, `src/nemsy/web.py`, `frontend/src/views/Chat.tsx`, `config/settings.toml`).

### Guarantees and forcing cases

**Knowledge grounding is a prompt policy, not an output invariant.** The instruction owner is Nemsy's task prompt; the enforcement point is provider/model interpretation. The required external contract is that the service follows the system instruction despite user and Wiki content. Both ordinary query and chat routes request grounding, but no inspected answer validator rejects extra-Wiki claims. Web prompts additionally request confident first-person expression. Covered paths are agent query/chat and Web's independently constructed query/chat prompts; the low-level wrapper accepts arbitrary system text. Guarantee strength: policy. Implementation conclusion status: wired. Operation conclusion status: uninspected. See [RT-BAP-wiki-context](#rt-bap-wiki-context) and [RT-CLM-wiki-grounding](#rt-clm-wiki-grounding).

Four forcing cases delimit stronger interpretations:

1. **Deep reasoning is reachable but not type-correct through its CLI consumer.** `query --reason` calls `llm.reason`, which returns `(text, TokenUsage)`. `_run_query` stores that tuple as `response`, prints it, tests membership in it rather than in the answer string, and with `--archive` forwards the tuple to an archive helper that calls `.replace`. Thus the ordinary archive path cannot be generalized to reasoning queries: source wiring predicts a type error on reasoning-plus-archive, not a tested failure. The option and wrapper signatures establish caller reachability; provider success is still required to reach the faulty consumer (SRC-1: `src/nemsy/cli.py`, `src/nemsy/llm.py`, `src/nemsy/agent.py`; [RT-RTE-reasoning-query](#rt-rte-reasoning-query)).
2. **CLI ingestion controls do not govern HTTP ingestion.** CLI collection and status filtering skip unchanged sources unless forced. HTTP accepts `force` but never reads it, and for a direct file uses `[path]` without `collect_files`. It calls ingest regardless of prior hash. Separately, `collect_files`' own direct-file early return applies suffix filtering but not the directory blacklist or `_index.md` exclusion used by its directory loop. CLI supports explicit file paths, and HTTP's request schema is a free string, so these alternate branches are reachable, not merely speculative types. A directory exclusion is not a universal non-ingestion guarantee. Owner/enforcement: collector and CLI driver; strength: protocol scoped to those branches. Implementation conclusion status: wired. Operation conclusion status: uninspected (SRC-1: `src/nemsy/vault.py`, `src/nemsy/cli.py`, `src/nemsy/web.py`; [RT-RTE-document-ingest](#rt-rte-document-ingest)).
3. **Dry-run and success labels have narrower meanings than durable success.** Empty sources are recorded before CLI's dry-run return. `_run_ingest_single` returns True after awaiting ingest without testing its optional page result; ingest records a nonempty source even if SUMMARY parsing returned None. Therefore dry-run prevents model processing of pending files but not every state write, and a CLI success count or HTTP `ingested` count does not certify a usable page. This is a source counterexample to treating those labels as validation. [RT-RTE-document-ingest](#rt-rte-document-ingest) owns the evidence.
4. **Archive controls differ across entry paths.** Agent query only saves with explicit archive; the model's `ARCHIVABLE: true` alone cannot write. CLI chat requests confirmation on that marker and `/save` explicitly starts model rewriting. Browser archive is available for completed assistant messages independently of the marker and calls `/api/save`. HTTP QueryRequest admits `archive`, but `api_query` never consumes it and never archives. Client `archive: true` therefore does not establish retention on that route (SRC-1: `src/nemsy/agent.py`, `src/nemsy/cli.py`, `src/nemsy/web.py`, `frontend/src/views/Chat.tsx`; [RT-RTE-answer-archive](#rt-rte-answer-archive), [RT-RTE-insight-save](#rt-rte-insight-save)).

### Effects, grants and recovery

The model-call capability actually wired in `llm.py` is text generation, with an optional thinking request, not an SDK tool dispatcher. The calls pass model, system, messages and generation settings, not tools; returned non-text blocks are omitted by `_extract_text`. Comments about protocol support for Tool Calls are not a current tool grant. File reads/writes, logging and deletion are host Python capabilities. No model-produced arbitrary shell command or model-selected delegation is executed by the inspected calls. This bounded observation does not describe provider internals or every dependency capability (SRC-1: `src/nemsy/llm.py`, `src/nemsy/agent.py`, `src/nemsy/vault.py`).

The deployed isolation envelope is not supplied. Web startup binds `0.0.0.0`; CORS permits a particular development origin but is not an authentication check. Inspected endpoint definitions have no caller authentication dependency. `api_file`'s claimed Vault check uses lexical `relative_to` without canonical resolution. A caller-supplied absolute path containing parent segments can be lexically below the Vault while filesystem lookup leaves it; symlink containment is also not established. Existence/read permissions and actual deployment constrain any access. HTTP ingest has no analogous Vault containment check, though ancestor-guidance lookup can itself fail for outside-root paths when forming relative labels. These are static control limitations, not observed exploitation. A resolved, authenticated sandbox cannot be inferred (SRC-1: `src/nemsy/web.py`, `src/nemsy/vault.py`).

> p.relative_to(vault)
> --- `src/nemsy/web.py`

> uvicorn.run("nemsy.web:app", host="0.0.0.0", port=port, reload=False)
> --- `src/nemsy/web.py`

The separate deletion helper rejects unless its caller supplies `confirmed=True`; its contract trusts the caller to have obtained confirmation. This is not evidence that every content replacement is approved: ordinary ingest, save and archive write same-named dated files without per-content review. Writes, index appends and JSON logs are separate filesystem operations, without a transaction or rollback in those inspected functions. Failures can leave partial state; retry/force can regenerate or overwrite, not restore a previous page. Batch CLI and HTTP processing are sequential within a request; cross-request coordination and crash recovery are not implemented in the inspected write sequences. Token logs and Wiki operation logs expose accounting and intent, not semantic validation; stream completion is needed before final usage and subsequent processing. Browser abort ends its fetch stream and UI streaming state, not a source-established transactional cancellation protocol (SRC-1: `src/nemsy/vault.py`, `src/nemsy/agent.py`, `src/nemsy/cli.py`, `src/nemsy/web.py`, `frontend/src/views/Chat.tsx`).

> if not confirmed:
>     raise RuntimeError("删除操作必须先通过 click.confirm() 获得用户确认，再传入 confirmed=True")
> path.unlink()
> --- `src/nemsy/vault.py`

Knowledge changes are admitted by the caller starting ingest/archive/save, followed by code accepting model text, not a separate semantic approval gate. Lint returns suggestions without applying them. Model and filesystem settings are operator configuration loaded at import, not model-admitted production changes. Web settings POST is a placeholder reporting success, not configuration mutation. No route inspected here uses lint feedback or smoke-test scores to select and install new product code, prompts or model weights. This is a bounded account of these mechanisms, not a repository-wide assertion that external development cannot change Nemsy (SRC-1: `src/nemsy/config.py`, `src/nemsy/web.py`, `src/nemsy/agent.py`, `tests/test_smoke.py`).

> # TODO: Phase 3 实现 — 解析并写回 toml + .env，然后热重载 settings 单例
> return {"ok": True, "message": "配置保存功能待 Phase 3 实现"}
> --- `src/nemsy/web.py`

## Shared records

### Components

#### RT-CMP-deepseek
Label: Configured DeepSeek generation service

SRC-1: `config/settings.toml`, `src/nemsy/config.py`, `src/nemsy/llm.py`. This distributed-parametric component is accessed remotely through an Anthropic-compatible client; weights and provider storage are opaque. Default aliases are `deepseek-v4-flash` and `deepseek-v4-pro`, with configurable endpoint and model names. Exact weights/version are not pinned. A mutable endpoint or alias can resolve to a different model; the repository cannot establish endpoint fixity. Inspected runtime requests do not update parameters; whether provider-side parameters or hidden state change remains uninspected. Retained Wiki changes are separate from parameter mutation. Invocation parameters include output-token limit and temperature; reasoning asks for thinking with budget 4096 and temperature 1.0. The wrapper strips thinking blocks from the returned text, not from provider processing. Implementation conclusion status: wired. Operation conclusion status: uninspected.

> default_model = "deepseek-v4-flash"
> reasoning_model = "deepseek-v4-pro"
> --- `config/settings.toml`

> thinking={"type": "enabled", "budget_tokens": 4096},  # type: ignore[arg-type]
> --- `src/nemsy/llm.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-document-ingest
Label: Local document ingestion and page admission

SRC-1: `src/nemsy/cli.py`, `src/nemsy/agent.py`, `src/nemsy/vault.py`, `src/nemsy/web.py`. CLI/API caller chooses source; Python chooses pending inputs and serial progression, the model proposes page content, and the parser admits it without semantic veto. Directory guidance and shipped schema constrain the requested text. Open user-selected ingestion is the operating mode; no expected-answer oracle is used. The human approves the operation, not the particular generated summary. Code can reject missing SUMMARY; it does not check that returned content is truthful or schema-conforming before writing. Browser FileLibrary confirmation is another operation-level approval (SRC-1: `frontend/src/views/FileLibrary.tsx`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Agent returns a relative page path or None; CLI prints progress/content; HTTP returns a results array and count.
- Later read-back: Generated source Markdown and appended index can enter later Wiki context loads; source hash log controls later CLI pending selection.
- Delegated visibility: Source text, ancestor guidance and selected Wiki text reach the remote generation service; no separate worker is launched.
- Selection predicate: CLI chooses new/changed nonempty eligible files or forced unchanged files; Web bypasses hash status filtering and its direct-file branch bypasses collection; context uses recency/count, not query relevance.
- Invalidation or expiry: Content hash changes or force permit CLI re-ingestion; dated title collisions overwrite pages; no automatic expiry or rollback of earlier page text.
- Activation or effect: Parser writes model Markdown and questions, appends index and logs; later delivery is wired, changed answer behavior unobserved.
- Evidence limits: No supplied ingest run; successful count can coexist with None page result. Hash records do not prove page existence or semantic quality.

Admission trigger is a caller ingest request; proposed knowledge is SUMMARY plus optional QUESTIONS. Parser rejection returns None on a missing delimiter, but ingest still logs and records the source. Recovery is another request/force or manual file repair, not automatic rollback. Guidance says to summarize, relate existing pages and flag contradictions; code implements a new summary page and index append rather than a general model-directed edit plan for all related pages.

> summary_match = re.search(r"---SUMMARY---\n(.*?)(?=---QUESTIONS---|$)", response, re.DOTALL)
> --- `src/nemsy/agent.py`

> wiki_page = _parse_and_write_ingest(full_response, source_title, out_console=_con)
> append_log("ingest", source_title)
>
> # 写入 ingest_log（含 hash、wiki_page）
> if source_path is not None:
>     record_ingest(source_path, source_content, ingest_mode="full", wiki_page=wiki_page)
> --- `src/nemsy/agent.py`

> elif status == "done" and not force:
>     skipped.append(f)
> --- `src/nemsy/cli.py`

> if path.is_file():
>     return [path] if path.suffix in ext_set else []
> --- `src/nemsy/vault.py`

> files = collect_files(path, recursive=req.recursive) if path.is_dir() else [path]
> --- `src/nemsy/web.py`

> _record(f, content)
> --- `src/nemsy/cli.py`

> await agent_ingest(
>     content,
>     source_title,
>     source_path=path,
>     index_context=index_context,
>     wide=wide,
>     stream=stream,
>     out_console=_con,
> )
> return True
> --- `src/nemsy/cli.py`

#### RT-RTE-wiki-answer
Label: Wiki question answering

SRC-1: `src/nemsy/agent.py`, `src/nemsy/web.py`, `src/nemsy/llm.py`. CLI ordinary query calls agent.query; Web constructs its own system prompt and streams directly. Python controls context and call completion; the model chooses answer wording and citations. The mode is open user questions without an answer oracle. Natural-language Wiki content is supplied as text, while symbolic recency/count rules select its subset. See [RT-BAP-wiki-context](#rt-bap-wiki-context).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Answer string for agent query; text chunks and final usage SSE for Web.
- Later read-back: Only when explicitly archived through the agent path; Web QueryRequest.archive is unused. See [RT-RTE-answer-archive](#rt-rte-answer-archive).
- Delegated visibility: Provider sees selected Wiki contents and question; no isolated sub-agent context exists.
- Selection predicate: Caller-supplied context if non-None in agent.query, otherwise index plus thirty recent other Markdown pages; Web always loads its own context.
- Invalidation or expiry: Fresh noncached requests reload current files; caller-supplied context has no freshness check.
- Activation or effect: Model is asked to answer exclusively from Wiki and cite pages; answer grounding and correct citations are unobserved.
- Evidence limits: No inspected run demonstrates successful grounding. This is recency-window provision, not implemented semantic retrieval over every page.

> ctx = wiki_context if wiki_context is not None else _load_wiki_context()
> --- `src/nemsy/agent.py`

> other_files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
>
> for f in other_files[:max_files]:
> --- `src/nemsy/agent.py`

#### RT-RTE-conversation-chat
Label: CLI and browser conversation progression

SRC-1: `src/nemsy/cli.py`, `src/nemsy/agent.py`, `src/nemsy/web.py`, `frontend/src/views/Chat.tsx`, `config/settings.toml`. The human supplies each message, code builds the next model invocation and appends the result. CLI slash commands are foreground-driver dispatch. Browser state supplies Web history; backend ChatRequest uses a list of dictionaries and build_messages forwards each role/content rather than imposing an application-level role allowlist. Provider acceptance of unusual roles remains external. Mode: open conversation; no reference-answer oracle.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: CLI prints reply; browser appends SSE chunks and marks completion, error or stopped state.
- Later read-back: Completed chat messages return in subsequent history; retained Wiki insights require explicit save. Conversation history is current-run state, not by itself a cross-session store.
- Delegated visibility: Provider receives history and Wiki snapshot; browser Wiki queries omit history, not the visible messages themselves.
- Selection predicate: CLI loads twenty recent pages once at session start; Web loads twenty on each chat request. Browser sends nonstreaming nonempty previous messages.
- Invalidation or expiry: Positive CLI max_turns keeps only the last configured turn pairs; default zero leaves history untrimmed. No summary or reload of discarded turns is wired in this branch; Wiki snapshot remains unchanged until a fresh load/session.
- Activation or effect: Text replies become later conversational context; causal behavioral effects of a particular history item are unobserved.
- Evidence limits: No run trace or effective provider-cache measurement. Stable prefix construction is not a provider cache-hit guarantee; actual context-window overflow handling is external/uninspected.

> _session_wiki_context = _load_wiki_context(max_files=20)
> --- `src/nemsy/cli.py`

> if max_turns > 0 and len(history) > max_turns * 2:
>     history = history[-(max_turns * 2):]
> --- `src/nemsy/cli.py`

> const body = mode === 'wiki'
>   ? JSON.stringify({ question: text })
>   : JSON.stringify({ message: text, history })
> --- `frontend/src/views/Chat.tsx`

#### RT-RTE-reasoning-query
Label: CLI reasoning query variant

SRC-1: `src/nemsy/cli.py`, `src/nemsy/llm.py`, `src/nemsy/agent.py`. Human `--reason` chooses this alternate route. Python builds the same query instructions and calls the reasoning model in [RT-CMP-deepseek](#rt-cmp-deepseek); no autonomous task routing or answer oracle. The distinct tuple consumer prevents assuming ordinary-route return and admission semantics.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Wrapper returns text and usage tuple; CLI prints the tuple and optionally returns it despite a string-oriented annotation.
- Later read-back: Intended archive is wired to a tuple-incompatible helper; successful page persistence is not established and source predicts failure on `.replace` after a successful provider response.
- Delegated visibility: Provider sees question and selected Wiki, and may generate hidden thinking; wrapper returns only text blocks plus usage.
- Selection predicate: Explicit CLI query --reason; uses supplied context or the normal thirty-page loader.
- Invalidation or expiry: inapplicable — no distinct durable reasoning result is established by this consumer.
- Activation or effect: Request enables thinking; printed tuple and possible archive error are source-predicted, not observed.
- Evidence limits: Provider internals and an actual execution of this mismatch are uninspected.

> response = await llm_module.reason(system, messages)
> console.print(response)
> if archive:
>     _archive_query_result(question, response)
> --- `src/nemsy/cli.py`

> return text, usage
> --- `src/nemsy/llm.py:208-219`

#### RT-RTE-answer-archive
Label: Explicit query answer archive

SRC-1: `src/nemsy/agent.py`, `src/nemsy/web.py`, `src/nemsy/cli.py`. Caller `archive=True` decides admission of an ordinary agent query answer; model ARCHIVABLE is only advisory. Code constructs query metadata, strips the marker, writes a dated queries page and updates index. There is no expected-answer oracle or independent semantic veto. Mode is an open question with optional retention, not candidate comparison.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Query still returns answer; CLI reports saved filename.
- Later read-back: Query Markdown/index becomes eligible for later Wiki context loads.
- Delegated visibility: No extra model invocation for ordinary archive; the preceding query service already saw its inputs.
- Selection predicate: Explicit agent/CLI archive flag, not the model marker. Web query accepts but does not consume archive; reasoning variant has the separate consumer defect.
- Invalidation or expiry: Same sanitized question-prefix/date path can overwrite; no version rollback or expiry in helper.
- Activation or effect: Writes generated answer without further content review; later influence is possible through Wiki read-back, not observed.
- Evidence limits: Save action establishes neither novel synthesis nor correctness; HTTP query parity is not supported.

Admission trigger is the explicit flag; the proposed change is the already returned answer. The caller can omit the flag, but cannot review the particular answer before this flagged call writes it. Recovery is manual edit/removal or regeneration. Persisted material is answer text and fixed metadata, not a tested theory revision.

> if archive:
>     _archive_query_result(question, full_response)
>     archived = True
> --- `src/nemsy/agent.py`

> content = f"# {question}\n\n{answer.replace('ARCHIVABLE: true', '').strip()}"
> --- `src/nemsy/agent.py`

#### RT-RTE-insight-save
Label: Conversation-to-insight admission

SRC-1: `src/nemsy/agent.py`, `src/nemsy/cli.py`, `src/nemsy/web.py`, `frontend/src/views/Chat.tsx`. CLI `/save`, accepted CLI marker prompt, or browser archive click supplies conversation history to a separate model call. Browser includes preceding messages through the selected answer, not just its visible answer text. Human selects the operation/history boundary; model proposes the rewritten page and title; code writes without review. Mode is open conversation-derived synthesis, no reference-answer oracle.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Agent returns relative insight path or None for empty history; HTTP returns wiki_page; UI treats an OK response as archived without inspecting wiki_page.
- Later read-back: Insight Markdown and index are eligible for later Wiki loaders, but the current CLI session's cached Wiki is not refreshed.
- Delegated visibility: Save service receives formatted conversation and optional topic; it does not receive a newly loaded Wiki despite instructions requesting associated Wiki knowledge.
- Selection predicate: Caller chooses history/topic; empty history is rejected. Browser presents save independently of ARCHIVABLE.
- Invalidation or expiry: Sanitized generated-title/date collisions overwrite; no automatic expiry, prior version capture or rollback.
- Activation or effect: New natural-language insight page written and index/log appended; later behavior change unobserved.
- Evidence limits: Transformation is requested, not demonstrated faithful synthesis. Neither operation approval nor filename derivation verifies its propositions.

The proposal guidance requests core insights, conclusions, background/derivation and associated knowledge in a schema-shaped page. Parser removes an enclosing code fence and extracts a title; it does not validate truth or require the model to preserve the conversation. Retained content can guide later answers, but persistence alone does not demonstrate learning or self-improvement. Recovery requires another save or manual file repair.

> user_prompt = f"请整理以下对话中的洞见：\n\n{history_text}{topic_hint}"
> --- `src/nemsy/agent.py`

> file_path.write_text(content, encoding="utf-8")
>
> _update_index(raw_title, filename, f"对话洞见：{raw_title[:30]}")
> --- `src/nemsy/agent.py`

#### RT-RTE-wiki-lint
Label: Model-based Wiki health suggestions

SRC-1: `src/nemsy/agent.py`, `src/nemsy/web.py`. Human CLI or HTTP request triggers index plus fifty recent-page loading, then one model call requesting contradictions, outdated views, orphans, missing concepts, missing links and further sources. Python returns a report; the model diagnoses and proposes, but neither route applies the proposed page changes. There is no deterministic graph-wide orphan check or answer oracle in this path. Mode is open maintenance advice.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Report string/console stream for agent; SSE report and usage for HTTP.
- Later read-back: inapplicable — these functions do not retain the report as a knowledge update; ordinary logs are not applied suggestions.
- Delegated visibility: Provider receives selected Wiki text, not an independently isolated maintenance worker or complete guaranteed corpus.
- Selection predicate: Caller request, count-bounded recency loader.
- Invalidation or expiry: inapplicable — no admitted lint-result object or automatic revision lifecycle here.
- Activation or effect: Diagnostic text returned, CLI operation log and token log written; correction of Wiki content remains outside this route.
- Evidence limits: Unobserved suggestions and their benefit; windowed input limits claims of comprehensive health checking.

The model can recommend, while the user can ignore or act separately. No software admission gate installs those suggestions, and no rollback is needed for unperformed page edits.

> 1. 页面间的逻辑矛盾
> 2. 被新资料推翻的过时观点
> 3. 没有入站链接的孤立页面（orphan）
> --- `src/nemsy/agent.py`

> append_log("lint", "Wiki 健康检查", detail="自动健检完成")
> return full_response
> --- `src/nemsy/agent.py`

### Claims

#### RT-CLM-wiki-grounding
Label: Wiki-only answers and citation policy

SRC-1: `src/nemsy/agent.py`, `src/nemsy/web.py`. Query and chat instructions prohibit filling Wiki gaps with training knowledge, and request linked citations. This is a claimed behavioral constraint, implemented as model instructions with no inspected semantic response gate. The Web wording also requests confident first-person presentation, so style is not evidence of warrant. Guarantee strength: policy; implementation conclusion status: wired; operation conclusion status: uninspected. The constraint's authority path is [RT-BAP-wiki-context](#rt-bap-wiki-context).

> - 回答必须以 Wiki 内容为唯一依据，不得引入 Wiki 中没有的信息
> - 如果 Wiki 中找不到相关内容，直接回答「Wiki 中暂无此内容」，不要推测或补全
> - 禁止用训练知识填补 Wiki 的空白，避免用户误以为是已归档知识
> --- `src/nemsy/agent.py`

> - 用词自信、简洁，避免"可能"、"似乎"等不必要的不确定性修饰——除非确实存在争议
> --- `src/nemsy/web.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-wiki-context
Label: Wiki and task instructions reaching generation

SRC-1: `src/nemsy/agent.py`, `src/nemsy/llm.py`, `src/nemsy/web.py`. Consumer: configured generation model. Channel: Wiki text is placed in query/ingest/lint user prompts and chat system prefix; task/schema instructions occupy the system argument. Force: natural-language guidance, not deterministic enforcement. Horizon: each supplied request, with a session-long Wiki snapshot for CLI chat and fresh loads for Web chat. Retained pages from ingest/archive/save can enter this path in later invocations through recency selection. Symbolic Python selects and concatenates; the model interprets page contents and instruction text. Wiki prose appearing in a system prefix does not acquire a code-enforced distinction between trustworthy facts and embedded instructions. Delivery is wired; compliance, resistance to conflicting content and activation of any particular retained claim are unobserved. See [RT-RTE-wiki-answer](#rt-rte-wiki-answer) and [RT-RTE-conversation-chat](#rt-rte-conversation-chat).

> system_prompt = (
>     f"当前 Wiki 摘要：\n{wiki_context}\n\n"
>     + chat_system.format(wiki_path=settings.vault.wiki_path)
> )
> --- `src/nemsy/agent.py`

> messages.append({"role": msg["role"], "content": msg["content"]})
> --- `src/nemsy/llm.py`

## Annotations

none
