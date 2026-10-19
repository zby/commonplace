---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "AI-Context-OS memory: canonical Markdown levels, query-time selection, access feedback and separate operational stores in the public snapshot."
run-id: AAS-2026-10-18-ai-context-os-82777c0c3926-01
source-identity: "https://github.com/alexdcd/AI-Context-OS"
reviewed-boundary: "9ed263080cadf98702bebb42d5260b45bd526f6c"
---

# AI-Context-OS memory report

## Boundary and evidence

This report covers the memory loop of the public MEMM snapshot fixed by [boundary](boundary.md): canonical content, acquisition and admission, query delivery, generated discovery artifacts, access feedback, operational journals/tasks/logs, governance and restore. External model internals, external agents' instruction loading, private vault contents and the private continuation are outside inspectable evidence. The supplied [runtime](runtime.md) orders the investigation but is not an inspection limit. No target program, example, test or inference endpoint was executed. All source-dependent findings below use SRC-1 at the reviewed commit; source reads establish implementation or generated instruction policy, not observed use or benefit.

Direct inspection added or deepened: `src-tauri/src/core/index.rs`, `src-tauri/src/core/types.rs`, `src-tauri/src/core/frontmatter.rs`, `src-tauri/src/core/levels.rs`, `src-tauri/src/core/memory.rs`, `src-tauri/src/core/paths.rs`, `src-tauri/src/core/usage.rs`, `src-tauri/src/core/scoring.rs`, `src-tauri/src/core/engine.rs`, `src-tauri/src/core/router.rs`, `src-tauri/src/core/mcp.rs`, `src-tauri/src/core/watcher.rs`, `src-tauri/src/core/governance.rs`, `src-tauri/src/core/tasks.rs`, observability schema and optimizer bodies; registered command inventory and CLI dispatch; desktop memory/read/save/delete, scoring, daily, journal, governance, backup and observability commands; inbox capture/normalization, inference and application; onboarding control and serialization helpers; chat send, file-watcher hook, governance action handlers and journal/task caller locations. The inspected real-vault diagnostic is evaluator source, not a supplied result. Runtime supplies remaining details of raw-file guards, HTTP transport, provider payloads and connector handoff; those supplied findings are identified below rather than presented as new direct reads.

| Entry point / operation | Source paths in SRC-1 | Coverage and limit |
|---|---|---|
| Scan, parse, reload | `src-tauri/src/core/index.rs`, `src-tauri/src/core/frontmatter.rs`, `src-tauri/src/core/paths.rs`, `src-tauri/src/core/types.rs` | [MEM-OBJ-memory-meta](#mem-obj-memory-meta); root inbox and managed operational subdirectories are skipped; folder contract violations warn. Parser defaults are less strict than the generated writing contract. |
| Structured and raw edits; rename/move/duplicate | `src-tauri/src/commands/memory.rs`, `src-tauri/src/commands/filesystem.rs`, `src-tauri/src/core/mcp.rs` | Direct read/save/delete inspected; alternate rename/move/duplicate signatures inventoried, full mutation behavior not re-audited. Supplied [RT-RTE-workspace-write](runtime.md#rt-rte-workspace-write) covers the main guards; no universal confinement or protection claim follows. |
| Context query, simulation, chat fallback | `src-tauri/src/core/engine.rs`, `src-tauri/src/commands/scoring.rs`, `src/components/chat/ChatPanel.tsx`, `src-tauri/src/commands/inbox.rs` | [RT-RTE-context-query](runtime.md#rt-rte-context-query), [RT-RTE-desktop-chat](runtime.md#rt-rte-desktop-chat), annotations below; simulation returns scored metadata, not the assembled bodies. |
| MCP tools, HTTP/stdio drivers | `src-tauri/src/core/mcp.rs`, `src-tauri/src/lib.rs`, `src-tauri/src/cli.rs` | Four registered tool bodies checked: context, save, skill, session log. Supplied runtime covers HTTP and embedded stdio startup. [MEM-RTE-access-feedback](#mem-rte-access-feedback), [MEM-OBJ-session-log](#mem-obj-session-log). |
| Static routes, CLI search/score/show/regenerate, connector | `src-tauri/src/core/router.rs`, `src-tauri/src/cli.rs`, `src/views/ConnectorsView.tsx` | Direct CLI/router reads and supplied [RT-RTE-adapter-handoff](runtime.md#rt-rte-adapter-handoff); no deployed external reader demonstrated. |
| Text/link/file acquisition and normalization | `src-tauri/src/commands/inbox.rs` | [MEM-RTE-inbox-capture](#mem-rte-inbox-capture); nontext attachment bytes retained separately from display text. Normalization does not establish extraction. |
| Inference, promote, source routing, reject/discard | `src-tauri/src/commands/inbox.rs` | [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal), annotation; proposal reasons persist outside canonical bodies. No observed review process. |
| Access trace → later ranking | `src-tauri/src/core/usage.rs`, `src-tauri/src/core/scoring.rs`, `src-tauri/src/core/mcp.rs`, `src-tauri/src/commands/memory.rs` | [MEM-RTE-access-feedback](#mem-rte-access-feedback); availability feedback, not answer-success feedback. |
| Journal, typed bullets, extracted tasks, metadata propagation | `src-tauri/src/commands/journal.rs`, `src-tauri/src/core/tasks.rs`, `src/views/JournalView.tsx`, `src/views/TaskView.tsx` | [MEM-RTE-journal-derive](#mem-rte-journal-derive); distinct durable stores and automatic canonical metadata writes. |
| Daily/session/proposal operational read-back | `src-tauri/src/commands/daily.rs`, `src-tauri/src/commands/inbox.rs`, `src-tauri/src/core/mcp.rs` | [MEM-OBJ-daily-log](#mem-obj-daily-log), [MEM-OBJ-session-log](#mem-obj-session-log); session log writer is not the daily-log consolidation input. No shipped session-log consumer established by the inspected search. |
| Governance, withdrawal, scratch expiry | `src-tauri/src/core/governance.rs`, `src-tauri/src/commands/governance.rs`, `src/views/GovernanceView.tsx`, `src-tauri/src/commands/memory.rs` | [MEM-RTE-governance-actions](#mem-rte-governance-actions); “archive” invokes deletion. Scratch cleanup uses indexed IDs although scratch is skipped by scanning. |
| Observability, health, optimization | `src-tauri/src/core/observability.rs`, `src-tauri/src/core/optimizer.rs`, `src-tauri/src/commands/observability.rs` | [MEM-OBJ-observability-db](#mem-obj-observability-db), [RT-RTE-optimization-status](runtime.md#rt-rte-optimization-status); health implementation itself not deeply inspected, so no score-validity or automatic revision conclusion. |
| Initialization and workspace selection | `src-tauri/src/commands/onboarding.rs`, `src-tauri/src/cli.rs`, `src-tauri/src/lib.rs`, `src-tauri/src/commands/config.rs` | [MEM-RTE-onboarding-write](#mem-rte-onboarding-write); supplied boundary covers config synchronization and vault switching. Full template text and vault-management implementation not audited; no conclusion about safe template overwrite or cross-vault isolation. |
| Backup/restore | `src-tauri/src/commands/backup.rs` | [MEM-RTE-backup-restore](#mem-rte-backup-restore); overlays files, not transactional checkpoint replacement. |
| Evaluation | `src-tauri/src/core/engine.rs`, `src-tauri/src/core/scoring.rs`, `src-tauri/tests/diagnose_vault_query.rs`, `sim_test.js` | Inline selector/assembly/scoring tests and real-vault diagnostic inspected as source; boundary supplies graph-layout scope of JS test. No observed relevance benchmark, answer oracle or evaluation-driven rewrite demonstrated. |

Available but less-inspected branches above are limits, not inaccessible sources or evidenced absences. Provider weights and private evidence are genuinely unavailable within this boundary; [RT-CMP-inference-provider](runtime.md#rt-cmp-inference-provider) retains their independent version/mutability limits. None of the Markdown, index or usage stores is a model-weight update.

## Core ideas

1. **Levels are retained authoring surfaces, not automatic chat compaction.** L0 lives in frontmatter, L1 and L2 in body sections. Code splits/selects existing strings; the name “summary” does not show that a model derived one from a transcript. Inbox proposals can derive these strings, while direct writes can supply them verbatim. Their distinct delivery paths are [MEM-OBJ-l0](#mem-obj-l0), [MEM-OBJ-l1](#mem-obj-l1) and [MEM-OBJ-l2](#mem-obj-l2).
2. **Retrieval is a request-driven, code-selected package, with materially different displays.** Query terms, lexical/BM25 scores, graph proximity, access recency/frequency, importance and skill dependencies select bodies. MCP adds rule summaries and unloaded references; chat omits that prelude/list; skill loading bypasses the allocator; CLI score is a different simulation. Delivery is advisory to a model, not proof of obedience. See the annotations on [RT-RTE-context-query](runtime.md#rt-rte-context-query), [RT-RTE-skill-load](runtime.md#rt-rte-skill-load) and [RT-BAP-workspace-instructions](runtime.md#rt-bap-workspace-instructions).
3. **Usage is a small closed feedback path even without semantic rewriting.** Selected MCP loads and desktop reads increment durable access state; later scans overlay it and scoring uses it. The originating evidence is a read/serve event, not a judged success. This can shape future availability without establishing improved capacity: [MEM-RTE-access-feedback](#mem-rte-access-feedback).
4. **“Governed,” “normalized,” “archive,” and “applied” do not identify one common control.** Root inbox exclusion is an indexing rule; proposal application is caller-directed; direct canonical writes bypass proposal review; normalization can only relabel; governance archive deletes; optimization apply only sets a suggestion status. Journal save independently mutates canonical tags. The mechanisms and their admission controls must remain separate: [MEM-RTE-inbox-capture](#mem-rte-inbox-capture), [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal), [MEM-RTE-journal-derive](#mem-rte-journal-derive), [MEM-RTE-governance-actions](#mem-rte-governance-actions), [RT-RTE-optimization-status](runtime.md#rt-rte-optimization-status).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-l0
Label: Memory L0 summary

Part of: [RT-OBJ-memory](runtime.md#rt-obj-memory)

Natural-language one-line description stored as the YAML `l0` string in the canonical Markdown file. It can originate in caller input, onboarding templates/profile fields, an inbox preview or a generated proposal; arbitrary existing-file origin remains unresolved. Code also tokenizes it for lexical scoring. It is not a raw trace or access counter. It reaches static routers/catalogs, MCP rule summaries and unloaded references, chat headings, and connector exports; each display is a projection, not the full canonical document. Authority is human/model interpretation in those channels, plus deterministic lexical-scoring influence. Editing L0 can change discovery and selection without changing L1/L2. SRC-1: `src-tauri/src/core/types.rs`, `src-tauri/src/core/router.rs`, `src-tauri/src/core/engine.rs`, `src-tauri/src/core/scoring.rs`; supplied connector evidence in [RT-RTE-adapter-handoff](runtime.md#rt-rte-adapter-handoff).

> out.push_str(&format!("- [{}] {} — `{}`\n", rule.id, rule.l0, rule.path));
> --- `src-tauri/src/core/router.rs`

#### MEM-OBJ-l1
Label: Memory L1 body

Part of: [RT-OBJ-memory](runtime.md#rt-obj-memory)

Natural-language body substring persisted in the canonical file. A query can load it alone or with L2; skill dependencies receive L1 without their L2. No-marker bodies become L1. Caller/model interpretation supplies its behavioral force; the parser does not certify concision, truth or provenance. Lineage may be authored, copied or proposal-derived, not necessarily automatic summarization. Source read and token estimates are reconstructed on query. SRC-1: `src-tauri/src/core/levels.rs`, `src-tauri/src/core/memory.rs`, `src-tauri/src/core/engine.rs`, `src-tauri/src/core/mcp.rs`.

> (None, None) => {
>     // No markers — treat everything as L1
>     (body.trim().to_string(), String::new())
> }
> --- `src-tauri/src/core/levels.rs`

#### MEM-OBJ-l2
Label: Memory L2 detail

Part of: [RT-OBJ-memory](runtime.md#rt-obj-memory)

Natural-language detail substring persisted after the L2 marker. Query delivery of L2 also includes L1, subject to allocator thresholds and an at-most-three L2 count. Direct skill load includes the skill's L2, but not dependency L2; CLI show prints both. Separate consumer selection makes this a material part, not another whole-memory identity. Source-routed L2 can append original URL/import path; opaque attachments do not thereby become its extracted contents. Initial user-vault authorship is unresolved. SRC-1: `src-tauri/src/core/levels.rs`, `src-tauri/src/core/engine.rs`, `src-tauri/src/core/mcp.rs`, `src-tauri/src/cli.rs`, `src-tauri/src/commands/inbox.rs`.

> LoadLevel::L2 => {
>     format!("{}\n\n{}", mem.l1_content, mem.l2_content)
> }
> --- `src-tauri/src/core/engine.rs`

#### MEM-OBJ-memory-meta
Label: Memory control metadata

Part of: [RT-OBJ-memory](runtime.md#rt-obj-memory)

Symbolic YAML fields in the same file: ID, ontology, importance, confidence, tags, links, dates/version, dependencies, status and protection; the natural-language L0 is separately assessed above. Folder category and system role are derived in RAM from path/folder contract, not serialized canonical fields. Access fields are overlaid from a separate store. Metadata directly controls indexing, score terms, graph links, dependency selection and some mutation guards. It does not make the contained prose trusted. In the inspected score expression, confidence and processed status are not admission thresholds. Unknown ontology/status variants can still load; unknown ontology round-tripping loses its original spelling. `id` is required by the deserializer, but `type` defaults: valid parse is weaker than the generated authoring requirements. SRC-1: `src-tauri/src/core/types.rs`, `src-tauri/src/core/index.rs`, `src-tauri/src/core/paths.rs`, `src-tauri/src/core/scoring.rs`.

> pub id: String,
> #[serde(rename = "type", default = "default_ontology")]
> pub ontology: MemoryOntology,
> --- `src-tauri/src/core/types.rs`

> #[serde(default, skip_serializing, skip_deserializing)]
> pub folder_category: Option<String>,
> #[serde(default, skip_serializing, skip_deserializing)]
> pub system_role: Option<SystemRole>,
> --- `src-tauri/src/core/types.rs`

#### MEM-OBJ-memory-usage
Label: Memory usage store

Distinct from the canonical container [RT-OBJ-memory](runtime.md#rt-obj-memory) and transient [RT-OBJ-context-result](runtime.md#rt-obj-context-result): `.cache/memory-usage.json` stores a symbolic ID-keyed map of last-access timestamps and saturating counts. It is derived access metadata, not retained document prose or a reasoning transcript. Subsequent scans apply it to metadata; absent/corrupt store content defaults to an empty map, with fallback access time from modified and count zero. No per-event reasons/outcomes survive in this aggregate. Consumers are ranking and decay/maintenance calculations that use the overlaid metadata. SRC-1: `src-tauri/src/core/usage.rs`, `src-tauri/src/core/paths.rs`, `src-tauri/src/core/index.rs`, `src-tauri/src/core/scoring.rs`.

> pub fn usage_json(&self) -> PathBuf {
>     self.root.join(".cache/memory-usage.json")
> }
> --- `src-tauri/src/core/paths.rs`

#### MEM-OBJ-inbox-item
Label: Inbox item and manifest

Distinct precursor to [RT-OBJ-ingest-proposal](runtime.md#rt-obj-ingest-proposal) and canonical [RT-OBJ-memory](runtime.md#rt-obj-memory). Inbox Markdown sidecars retain title, summary and L1/L2 text with symbolic source URL, hashes, attachment descriptors, timestamps and workflow states; `.ai/ingest/manifest.json` is derived acquisition inventory. The source may be caller text, fetched link preview plus notes, imported text, or only a description of an opaque file. Hash/URL duplicate checks and inference consume item fields; the canonical query scanner excludes root inbox. Its preview is not evidence of complete source extraction. SRC-1: `src-tauri/src/commands/inbox.rs`, `src-tauri/src/core/index.rs`, `src-tauri/src/core/paths.rs`.

> let needs_extraction = !is_text_like(&source);
> let l1 = if text_preview.trim().is_empty() {
>     format!("Imported file: {}", original_name)
> } else {
>     preview_text(&text_preview)
> };
> --- `src-tauri/src/commands/inbox.rs`

#### MEM-OBJ-inbox-attachment
Label: Imported attachment bytes

Distinct from [MEM-OBJ-inbox-item](#mem-obj-inbox-item) and [RT-OBJ-ingest-proposal](runtime.md#rt-obj-ingest-proposal). Files are copied into `inbox/_attachments`; descriptors retain path, original name, MIME, byte size and hash. Representation is source-format-dependent and opaque here, not uniformly natural-language memory. Text-like imports decode bytes into sidecar text; nontext imports can retain empty L2 and extraction flags. Proposal inference receives textual item fields and flags, not these attachment bytes; route-to-sources copies existing attachments alongside the source memory. No binary-extraction consumer is established by normalization. SRC-1: `src-tauri/src/commands/inbox.rs`.

> let text_preview = if is_text_like(&source) {
>     String::from_utf8_lossy(&bytes).to_string()
> } else {
>     String::new()
> };
> --- `src-tauri/src/commands/inbox.rs`

#### MEM-OBJ-router-manifest
Label: Generated discovery artifacts

Distinct derived projections of [RT-OBJ-memory](runtime.md#rt-obj-memory), produced on [RT-RTE-adapter-handoff](runtime.md#rt-rte-adapter-handoff). The manifest is a transient structured value; persistent outputs include `.ai/index.yaml`, `.ai/catalog.md`, `claude.md`, `.cursorrules` and `.windsurfrules`. Symbolic paths/IDs/metadata and natural-language L0/rules are not canonical L1/L2 copies. Catalog/index preserve `derived_from` pointers; they do not incorporate proposal rationale. Hosts are afforded discovery and direct-file reading under written rules, not forced compliance. Rebuild replaces these projections; already copied or model-loaded text is not revoked. SRC-1: `src-tauri/src/core/router.rs`, `src-tauri/src/cli.rs`; generated-policy excerpts also in [RT-BAP-workspace-instructions](runtime.md#rt-bap-workspace-instructions).

> out.push_str("5. If you need richer metadata (links, provenance, dependencies), open `.ai/catalog.md` or `.ai/index.yaml`.\n");
> --- `src-tauri/src/core/router.rs`

#### MEM-OBJ-journal-page
Label: Daily journal page

No counterpart in supplied runtime objects. Natural-language dated Markdown under `.ai/journal`, parsed into display blocks for a human journal reader; task markers and typed hashtags also have symbolic consumers. Save rewrites a page; derived task files and appended daily events are distinct results, not a compacted replacement of the page. A source date links tasks/events back to the page. This subtree is excluded from canonical retrieval by scanner policy. SRC-1: `src-tauri/src/core/paths.rs`, `src-tauri/src/commands/journal.rs`, `src/views/JournalView.tsx`.

> let result = journal::save_journal_page(&root, &date, &content)?;
> --- `src-tauri/src/commands/journal.rs`

#### MEM-OBJ-task-item
Label: Task item

No counterpart in supplied runtime objects. Files under `.ai/tasks` retain natural-language title/notes and symbolic state, priority, source date/file, timestamps, tags and due date. They may originate in direct task commands or journal checkbox extraction. Later `list_tasks` reparses files, filters and sorts for the task view and journal duplicate checking; task state is a work-management control, not an instruction automatically delivered by the context engine. Files are independently editable/deletable, and this directory is excluded from canonical scans. SRC-1: `src-tauri/src/core/tasks.rs`, `src-tauri/src/commands/tasks.rs`, `src/views/TaskView.tsx`, `src-tauri/src/commands/journal.rs`, `src-tauri/src/core/paths.rs`.

> let file_path = tasks_dir.join(format!("{}.md", &task.id));
> let content = serialize_task(task);
> --- `src-tauri/src/core/tasks.rs`

#### MEM-OBJ-daily-log
Label: Daily operational log

No counterpart in supplied runtime objects. `.ai/journal/daily-log.jsonl` retains event records: symbolic timestamp/type/tags/source and natural-language summary. Inputs include explicit append commands, journal typed-bullet extraction and inbox-operation events. This is retained raw/normalized operational evidence, not canonical synthesized knowledge. Consumers include date-filtered daily reads, recent operational context and consolidation suggestions. Saving the same journal content can append its typed bullets again; the inspected loop has no deduplication of daily events. SRC-1: `src-tauri/src/commands/daily.rs`, `src-tauri/src/commands/journal.rs`, `src-tauri/src/commands/inbox.rs`, `src-tauri/src/commands/governance.rs`.

> let entries: Vec<DailyEntry> = read_jsonl(&paths.daily_log())?;
> Ok(suggest_consolidation(&entries))
> --- `src-tauri/src/commands/governance.rs`

#### MEM-OBJ-session-log
Label: MCP session event log

No counterpart in supplied runtime objects. MCP `log_session` appends caller-authored natural-language summaries with symbolic event type, tags, source and generated timestamp to `.ai/journal/sessions/YYYY-MM-DD.jsonl`. This is not a raw automatically recorded model/tool transcript and not the daily-log file consumed by consolidation. The tool description's “daily JSONL log” does not establish integration with daily entries. Searching `sessions_dir` and session/log readers in `src-tauri/src` established the writer/path helper but no later session-log reader; later consumer and behavioral force remain unestablished, not presumed from storage. SRC-1: `src-tauri/src/core/mcp.rs`, `src-tauri/src/core/paths.rs`, `src-tauri/src/commands/governance.rs`.

> let log_path = crate::core::paths::SystemPaths::new(&root)
>     .sessions_dir()
>     .join(format!("{}.jsonl", today));
> --- `src-tauri/src/core/mcp.rs`

#### MEM-OBJ-observability-db
Label: Observability database

Distinct from [MEM-OBJ-memory-usage](#mem-obj-memory-usage), though both derive from serving events. SQLite `.cache/observability.db` retains request/query/budget/session/source/task classifications, served/not-loaded memory IDs, score/level/token accounting, health history and optimization suggestions. Structured numerical/symbolic traces are not provider outcome judgments or full served bodies; `memory_title` is a stored natural-language L0 display string. Derived suggestion descriptions/evidence coexist with traces in separate tables. Consumers are observability queries/UI, health and optimization detectors; context ranking directly reads usage JSON instead, not this SQL request history in the inspected engine. No memory-quality learning benefit follows from a health score. SRC-1: `src-tauri/src/core/observability.rs`, `src-tauri/src/core/mcp.rs`, `src-tauri/src/core/optimizer.rs`, `src-tauri/src/commands/observability.rs`, `src-tauri/src/core/engine.rs`.

> let db_path = cache_dir.join("observability.db");
> let conn = Connection::open(&db_path)
>     .map_err(|e| format!("Failed to open observability DB: {}", e))?;
> --- `src-tauri/src/core/observability.rs`

### Routes

#### MEM-RTE-access-feedback
Label: Access feedback into retrieval

Distinct continuation of [RT-RTE-context-query](runtime.md#rt-rte-context-query), [RT-RTE-skill-load](runtime.md#rt-rte-skill-load) and desktop get-memory; it spans their trace writes and later scans rather than duplicating one request. Producers are MCP selected body loads, skill plus required-dependency reads, and desktop `get_memory`. Code automatically admits timestamp/count updates without per-event human approval; callers initiate the reads, not necessarily approve every derived update. Optional skill dependencies are displayed but omitted from the recorded ID list. Shared engine/build/simulation do not themselves call the access writer. Original trace is serving/reading retained content, not task success, and no answer oracle is used. SRC-1: `src-tauri/src/core/mcp.rs`, `src-tauri/src/commands/memory.rs`, `src-tauri/src/core/usage.rs`, `src-tauri/src/core/index.rs`, `src-tauri/src/core/scoring.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: original context/skill/body plus attempted durable update to [MEM-OBJ-memory-usage](#mem-obj-memory-usage); MCP ignores accounting errors, desktop get-memory propagates a record-access error.
- Later read-back: subsequent scan loads usage JSON, overlays metadata and supplies recency/access-frequency score terms; governance also uses the access metadata for decay candidates.
- Delegated visibility: MCP callers receive assembled prose, not the usage map; the selector consumes the derived counters at later invocations.
- Selection predicate: served loaded IDs or exact desktop read ID, with skill required IDs only; new ranking depends on query and the entire current corpus maximum access count.
- Invalidation or expiry: counts saturate, timestamps replace; missing/corrupt usage falls back; no semantic invalidation or outcome-based rollback is shown in the writer. Changes to an ID's content do not inherently change its usage key.
- Activation or effect: a durable trace-derived ranking input is wired; changed rankings, model reliance and improved capacity remain unobserved.
- Evidence limits: request popularity can influence later selection without any warrant of truth, usefulness or success; canonical text is not rewritten by this path.

> entry.last_access = timestamp;
> entry.access_count = entry.access_count.saturating_add(1);
> --- `src-tauri/src/core/usage.rs`

> let recency = recency_score(&memory.meta.last_access, now);
> let importance = memory.meta.importance;
> let access_frequency =
>     access_frequency_score(memory.meta.access_count, max_access_count(all_memories));
> --- `src-tauri/src/core/scoring.rs`

#### MEM-RTE-inbox-capture
Label: Inbox capture and normalization

Distinct upstream production route for [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal), not its apply decision. Explicit commands admit text, validated HTTP link capture or selected files into [MEM-OBJ-inbox-item](#mem-obj-inbox-item) and [MEM-OBJ-inbox-attachment](#mem-obj-inbox-attachment). Caller supplies selection/content, software fetches/copies and derives previews, hash, state and manifest; caller human-versus-agent identity is not enforced by the API. No second content-approval gate or expected-answer oracle intervenes. Editing item text replaces retained content; normalization changes state and fills an empty preview, not a binary extraction step. SRC-1: `src-tauri/src/commands/inbox.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: new/edited/normalized item(s), manifest refresh and inbox events; associated daily events for capture.
- Later read-back: item loading feeds duplicate checks, heuristic/provider proposals and operational APIs; root inbox remains outside canonical context until a separate canonical write.
- Delegated visibility: inference receives textual item fields/schema, not attachment bytes or assembled vault context; caller receives item/proposal representations.
- Selection predicate: explicit text/URL/file paths or item IDs; text-like classification chooses decoding versus opaque attachment retention; hash/URL matches guide later duplicate proposals.
- Invalidation or expiry: edit recomputes item summary/hash; retained attachments and prior proposals are separate artifacts. The inspected normalization bodies do not clear extraction flags or produce extracted binary text; rollback is not automatic.
- Activation or effect: acquisition and representation changes are wired; extraction quality, successful fetch and later model use are unobserved.
- Evidence limits: fetched preview plus notes is not the original website; attachment presence is not readable-content admission; normalization is not canonical promotion or demonstrated curation quality.

> pub fn normalize_inbox_item(
>     id: String,
>     app: AppHandle,
>     state: State<AppState>,
> ) -> Result<InboxItem, String> {
>     let root = state.get_root();
>     let mut item = load_inbox_items(&root)?
>         .into_iter()
>         .find(|item| item.id == id)
>         .ok_or_else(|| format!("Inbox item not found: {}", id))?;
>     item.status = InboxItemStatus::Normalized;
>     item.capture_state = "normalized".to_string();
>     item.modified = Utc::now();
> --- `src-tauri/src/commands/inbox.rs`

#### MEM-RTE-journal-derive
Label: Journal-derived operational and metadata writes

No supplied route describes this mechanism; it adds an automatic canonical-write path beyond [RT-RTE-workspace-write](runtime.md#rt-rte-workspace-write) and [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal). Caller invokes journal save with dated text; code writes [MEM-OBJ-journal-page](#mem-obj-journal-page), extracts typed events into [MEM-OBJ-daily-log](#mem-obj-daily-log), creates [MEM-OBJ-task-item](#mem-obj-task-item) for unchecked boxes lacking an exact-title task, and propagates the journal date tag to matching canonical memories. A generic save action is not human approval of each selected memory mutation. Regex/matching code proposes and admits the derivatives without a model call or answer oracle. SRC-1: `src-tauri/src/commands/journal.rs`, `src-tauri/src/core/tasks.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: saved page path; derived log/task/tag writes are attempted, with several errors ignored.
- Later read-back: journal/task views reload their files; daily events feed consolidation; canonical date tags enter later scans and tag scoring, with modified timestamp updated on the memory write.
- Delegated visibility: human views see pages/tasks/events; selector sees canonical metadata, not the journal as a query candidate. No sub-agent transcript or compacted conversation crosses a frame boundary.
- Selection predicate: typed bullet regex; unchecked-box regex and exact-title task deduplication; other hashtags match memory ID/L0 substrings or existing tags, then add the date if absent.
- Invalidation or expiry: page save replaces page text, but appended events and created tasks are not retracted when source lines disappear. Date-tag additions are durable; explicit later edits/deletes can change them. No journal-save rollback links these stores.
- Activation or effect: operational derivatives and ranking-relevant metadata writes are wired, not observed relevance improvement.
- Evidence limits: canonical tag propagation calls low-level write_memory without checking protected status or reusing the structured-save unlock guard; not evidence of arbitrary protected-body editing, but a counterexample to a universal no-mutation guarantee.

> mem.meta.tags.push(date_tag);
> mem.meta.modified = now;
> let _ = memory::write_memory(std::path::Path::new(file_path), &mem);
> --- `src-tauri/src/commands/journal.rs`

#### MEM-RTE-governance-actions
Label: Governance suggestions and withdrawal

Distinct from [RT-RTE-optimization-status](runtime.md#rt-rte-optimization-status): governance endpoints compute conflicts, archival candidates, daily-entry consolidation suggestions and scratch TTL candidates; the shipped governance view provides confirmed delete and importance-boost actions. Code selects candidates; human confirmation in these UI handlers is the admission/veto for their chosen action, while callable backend APIs need not establish a human review. Heuristics guide selection, not a model or expected-answer oracle. Archive actions do not preserve an archive copy in the inspected handler. SRC-1: `src-tauri/src/core/governance.rs`, `src-tauri/src/commands/governance.rs`, `src/views/GovernanceView.tsx`, `src-tauri/src/commands/memory.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: transient candidate/suggestion lists; confirmed archive invokes deleteMemory; boost reads the body and saves importance plus 0.2 capped at 1.0.
- Later read-back: successful deletes remove files from later scans and regenerated discovery artifacts; boosts persist metadata used by scoring. Daily consolidation suggestions are displayed, not themselves promoted canonical memories by this endpoint.
- Delegated visibility: governance UI/human receives IDs/descriptions/candidates; later model consumers receive whatever survives query selection, not a retained governance rationale.
- Selection predicate: related-memory keyword pairs for conflicts; access/decay thresholds; daily decision/idea groups of at least three; scratch file modification age. These are proxies, not adjudicated contradictions or quality scores.
- Invalidation or expiry: recomputation refreshes candidates; deletion removes the file, subject to protection; recovery needs another edit or backup, not an automatic archive rollback. Delivered/copied context is unaffected.
- Activation or effect: wired candidate computation and UI mutation calls; successful cleanup, consolidation benefit and later model dependence are unobserved.
- Evidence limits: scratch candidates come from an excluded subtree, but clear-all converts filenames to IDs and calls indexed deleteMemory, catches failures and clears its local list. A scratch file's successful removal is not established by that UI state; same-ID collisions need care.

> for (const m of decayCandidates) {
>   try { await deleteMemory(m.id); } catch { /* skip */ }
> }
> --- `src/views/GovernanceView.tsx`

> let _ = app.emit("file-deleted", &path);
> crate::commands::router::regenerate_router_internal(&app, &state)?;
> --- `src-tauri/src/commands/memory.rs`

#### MEM-RTE-onboarding-write
Label: Onboarding memory admission

Distinct initializer preceding [RT-RTE-workspace-write](runtime.md#rt-rte-workspace-write). Caller supplies profile fields, root, template and tools. Software writes a profile memory and selected developer/creator/entrepreneur templates, then regenerates discovery and synchronizes workspace runtime. Selecting a template admits coded text without per-file approval; profile fields have caller provenance, template words maintainer provenance. No model comparison, quality oracle or outcome-triggered successor selection appears in the inspected control/helpers. Full template content was not audited. SRC-1: `src-tauri/src/commands/onboarding.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Boolean success/error after workspace/profile/template/router operations and vault registration.
- Later read-back: profile and template memories outside excluded folders become scan candidates; rules/skills gain their path/contract roles and generated discovery exposure.
- Delegated visibility: later host/query readers receive selected generated texts, not a model-generated account of the onboarding process.
- Selection predicate: requested template and profile fields; use_existing_root suppresses starter folder creation, not the later profile/template calls in the inspected control.
- Invalidation or expiry: helper writes replace target paths; regeneration derives adapters anew; no atomic rollback or preserved previous profile checkpoint is established.
- Activation or effect: deterministic content initialization is wired; later compliance and benefit unobserved.
- Evidence limits: ownership/control of pre-existing imported vault content remains unresolved; these known subsequent/initial transformations do not establish its provenance or safe overwrite handling for every template.

> // Step 4: Generate perfil-profesional.md
> create_profile_memory(&root, &profile)?;
> --- `src-tauri/src/commands/onboarding.rs`

#### MEM-RTE-backup-restore
Label: Workspace backup and overlay restore

No supplied route covers this alternate admission/recovery path. Explicit backup walks the workspace into a ZIP; explicit restore selects a ZIP and writes enclosed paths into the active root. Caller chooses the artifact; software admits bytes after ZIP/path handling, without per-memory parse, protection, proposal review or content validation in the inspected body. This differs from [RT-RTE-workspace-write](runtime.md#rt-rte-workspace-write). Stored representation is a compressed filesystem snapshot with format-dependent contents, not a semantic summary. SRC-1: `src-tauri/src/commands/backup.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ZIP destination or restore Boolean/error; file writes may already have occurred before a later error.
- Later read-back: future scans consume restored parseable canonical files; restored operational files are available to their own readers. The restore command itself does not refresh the memory index or regenerate routers.
- Delegated visibility: caller sees outcome, later views/selectors see restored state; backups are not automatically supplied to model inference.
- Selection predicate: recursively visited workspace files for backup; entries with enclosed_name accepted for restore into root. This is path-oriented admission, not relevance/meaning selection.
- Invalidation or expiry: overwrite overlays matching paths but does not delete unrelated newer files; thus it is not exact rollback. No transaction or automatic restore-on-error is shown.
- Activation or effect: durable state replacement capability wired; successful consistent recovery and later behavioral effects unobserved.
- Evidence limits: SQLite/WAL snapshot consistency, permissions and symlink isolation were not audited; ZIP creation alone is not proof of a coherent running-database checkpoint.

> let mut outfile = fs::File::create(&entry_path)
>     .map_err(|e| format!("Failed to create file: {}", e))?;
> --- `src-tauri/src/commands/backup.rs`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-ingest-proposal](runtime.md#rt-obj-ingest-proposal)

Memory lineage and reasons: inferred proposals persist item/path, provider kind/preset, origin, rationale and candidate levels. Applied canonical memories retain `derived_from: item.id`, confidence and selected text/tags, but their builders do not copy the proposal rationale or provider fields. Source routing additionally appends original URL/import path and copies attachments; protected source status is a later API edit policy, not external-source verification. Proposal readers and recent operational context can expose reasons; canonical query assembly does not reload proposal rationale from those item links. Thus reasons remain reconstructible by explicit operational inspection, not automatically co-delivered with the promoted knowledge. SRC-1: `src-tauri/src/commands/inbox.rs`.

> rationale: parsed.rationale,
> --- `src-tauri/src/commands/inbox.rs`

#### On [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal)

Read-back/persistence detail: application and rejection update proposal JSON and inbox state, retaining the original item and reason-bearing proposal as separate artifacts. `get_recent_operational_context` selects the latest 20 daily entries, up to 10 pending proposals and up to 10 Applied proposals; “recently_promoted” is selected by Applied state, not by a check that the action actually promoted a memory. This establishes an operational API consumer, not a wired provider-context channel or observed review UI. Rejected proposals stay loadable in the full proposal list but fall outside these two selected subsets. Raw item → heuristic/inferred proposal → selected canonical text → later query is wired only for the write-producing actions; discard/update_memory/needs_review do not complete that canonical-content chain. SRC-1: `src-tauri/src/commands/inbox.rs`; action excerpt in the supplied record supports its narrower semantics.

> let recently_promoted = proposals
>     .iter()
>     .filter(|proposal| proposal.state == ProposalState::Applied)
>     .take(10)
>     .cloned()
>     .collect::<Vec<_>>();
> --- `src-tauri/src/commands/inbox.rs`

#### On [RT-RTE-context-query](runtime.md#rt-rte-context-query)

Memory selection and working context: this is requested external-content read-back, not an independent unsolicited push. Rust receives query/budget/config, rescans canonical files and selects levels; code chooses content, not the runtime model. Symbolic score calculation combines tag/L0 overlap and ontology heuristics, BM25 over existing bodies, recency, importance, access frequency and graph proximity. “Semantic” names a free-tier lexical/ontology approximation here, not evidence of dense embeddings or model judgment. Existing access metadata can affect later selection through [MEM-RTE-access-feedback](#mem-rte-access-feedback). SRC-1: `src-tauri/src/core/engine.rs`, `src-tauri/src/core/scoring.rs`.

> 0.40 * tag_score + 0.35 * l0_score + 0.25 * ontology_bonus
> --- `src-tauri/src/core/scoring.rs`

Budget/display limits: estimates are ceil(words × 1.3), not tokenizer counts. Greedy allocation may keep L1 while withholding L2; ordinary L0-only allocations appear in MCP unloaded references, not loaded bodies. Required dependencies only relax the L1 score test; they do not reserve budget. A force-marked item that fits only L0 is neither pushed to loaded nor to the ordinary L0 unloaded branch, although it can remain in scored results. “Force” is therefore weaker than guaranteed delivery. Budget-exhausted items are absent from scored results but appear as unloaded references in MCP. The prelude/unloaded output, headers and conversation history prevent a whole-window guarantee. SRC-1: `src-tauri/src/core/levels.rs`, `src-tauri/src/core/engine.rs`.

> if level == LoadLevel::L0 && !is_force_loaded {
> --- `src-tauri/src/core/engine.rs`

#### On [RT-OBJ-context-result](runtime.md#rt-obj-context-result)

The result holds references by ID alongside selected text by value in RAM, not durable pointer-based model memory. MCP assembly displays loaded content plus unloaded L0 list and rules; chat displays selected content with L0 headings but no unloaded list/rules prelude; simulation exposes scored metadata only. A cached/copied package is not automatically invalidated when the canonical file changes. The selector can omit content without removing already remembered information from a provider or prior answer. SRC-1: `src-tauri/src/core/engine.rs`, `src-tauri/src/commands/scoring.rs`.

#### On [RT-RTE-skill-load](runtime.md#rt-rte-skill-load)

Memory consumers receive full requested skill text and immediate dependency L1 text. This is caller-ID-directed retrieval, not automatic task matching; trigger words in generated discovery are host-interpreted. No recursive dependency closure or token budget is present in the inspected tool. Required dependencies and the skill contribute access records, optional dependencies do not. Body delivery can guide an external agent but the tool does not execute or validate that agent's task. SRC-1: `src-tauri/src/core/mcp.rs`; the supplied record retains the supporting required-loop passage.

#### On [RT-RTE-desktop-chat](runtime.md#rt-rte-desktop-chat)

Working-context scope: frontend turns are component `useState` data, accumulated and forwarded; the inspected send path has no compaction checkpoint, summary replacement, per-task worker frame or history-trimming selector. Query-selected vault context is rebuilt on each send, and context opt-out clears the dedicated channel rather than filtering old history. This is external-content load control, not evidence of durable cross-session conversation memory. Provider-side caching, hidden compaction and weight behavior remain uninspected. No alternative transcript checkpoint form is established in the inspected frontend/backend route. SRC-1: `src/components/chat/ChatPanel.tsx`; provider pass-through evidence is supplied in the runtime record.

> const [turns, setTurns] = useState<ChatTurn[]>([]);
> --- `src/components/chat/ChatPanel.tsx`

The classical frame analogy is limited: the caller does not push an isolated sub-agent frame and pop it, and delivered Markdown is a copy in a model input, not a dereferenceable live file reference. IDs/file paths can support a future explicit read, not automatic model-window liveness management. This follows from the textual assembly and direct send operations, not an audit of an external host's compactor. SRC-1: `src-tauri/src/core/engine.rs`, `src/components/chat/ChatPanel.tsx`.

#### On [RT-RTE-workspace-write](runtime.md#rt-rte-workspace-write)

Memory admission and withdrawal have additional alternate paths, not a replacement of this route's identity. [MEM-RTE-journal-derive](#mem-rte-journal-derive) writes tags through the low-level serializer without protected checks; [MEM-RTE-backup-restore](#mem-rte-backup-restore) overlays files outside structured mutation guards; [MEM-RTE-onboarding-write](#mem-rte-onboarding-write) admits template/profile text. Direct save increments metadata version and modified time; these are revision labels, not preserved historical bodies. Delete removes the file and regenerates discovery; it does not retract already delivered text. SRC-1: `src-tauri/src/commands/journal.rs`, `src-tauri/src/commands/backup.rs`, `src-tauri/src/commands/onboarding.rs`, `src-tauri/src/commands/memory.rs`.

#### On [RT-RTE-adapter-handoff](runtime.md#rt-rte-adapter-handoff)

Generated discovery is persisted after canonical edits/regeneration; watcher-driven refresh is another admission-to-discovery bridge. The Rust watcher ignores `.cache` and generated artifacts, emits Markdown/YAML/JSONL change events and skips recent local writes. The frontend responds to external path events by regenerating and reloading views/graph. It does not push a replacement context string into an already executing agent. Connector scratch output is a distinct L0 summary export, not a serialized full ContextResult; a later external reader remains afforded, not observed. SRC-1: `src-tauri/src/core/watcher.rs`, `src/hooks/useFileWatcher.ts`; connector passage supplied by this runtime record.

#### On [RT-RTE-optimization-status](runtime.md#rt-rte-optimization-status)

Trace lineage: SQL serving/not-loaded records and current canonical size/metadata feed seven detector families: compress L1, archive unused, promote importance, downgrade L2, remove decayed, merge candidates and nudge threshold. Stored suggestions carry textual reasons/evidence and estimated savings. This is raw trace → derived maintenance advice → maintenance caller, not raw trace → automatically rewritten canonical summary → model. Reanalysis clears pending suggestions; apply/dismiss update status only. Reasons are available through suggestion readers, but no inspected selector consumes “applied” as a changed retrieval policy. SRC-1: `src-tauri/src/core/optimizer.rs`, `src-tauri/src/commands/observability.rs`.

> // Store all suggestions in DB
> for opt in &suggestions {
>     let _ = db.insert_optimization(opt);
> }
> --- `src-tauri/src/core/optimizer.rs`

#### On [RT-BAP-workspace-instructions](runtime.md#rt-bap-workspace-instructions)

Authority is channel-specific: rule L0 summaries and writing/reading instructions are natural language delivered to an MCP/adapter reader. Full rule bodies may independently qualify for scored retrieval, but are not guaranteed by the prelude. Chat omits the prelude. Ontology and path roles are code-selection metadata, not assurance that a `source` is verified, a `synthesis` is warranted or a `skill` executed. Provenance pointers remain discovery metadata unless the consumer explicitly follows them. SRC-1: `src-tauri/src/core/router.rs`, `src-tauri/src/core/engine.rs`, `src-tauri/src/core/types.rs`.

## Write side

The principal write/admission mechanisms are deliberately separated:

| Mechanism | Authorship and physical transformation | Admission control and later reach |
|---|---|---|
| Desktop structured save / MCP save / raw edits | Caller supplies content; Rust serializes/writes; external editors can also change files. | Command invocation plus path-specific validation/guards, not necessarily human approval. MCP canonical-folder override and desktop canonical creation bypass proposal review. Subsequent scans/adapters expose accepted content: [RT-RTE-workspace-write](runtime.md#rt-rte-workspace-write). |
| Indexing existing files | Parser derives metadata/levels and scan applies access overlay. No known author for arbitrary vault files. | Root inbox and selected system subtrees excluded; required-field defaults and warnings are weaker than the generated author contract. [MEM-OBJ-memory-meta](#mem-obj-memory-meta). |
| Inbox acquisition / normalization | Caller text/files/URL, code preview/hash/copy/state change. Binary bytes may remain opaque. | Caller-selected inputs admitted to staging; normalization is not promotion or extraction. [MEM-RTE-inbox-capture](#mem-rte-inbox-capture). |
| Proposal production / application | Heuristics or configured model propose; JSON persists content/reasons/provenance. | Caller apply/reject dispatch is separate from proposer confidence. Apply lacks a Pending-state requirement in supplied runtime inspection; canonical builders omit proposal reasons. [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal). |
| Onboarding | Caller profile plus maintainer-authored template text serialized by code. | Template selection admits generated files without per-file review; initial external-vault provenance remains unknown. [MEM-RTE-onboarding-write](#mem-rte-onboarding-write). |
| Access feedback | Read/serve trace becomes count/time JSON, canonical prose unchanged. | Automatic code admission; later ranking consumes the aggregate. [MEM-RTE-access-feedback](#mem-rte-access-feedback). |
| Journal/daily/task | Caller page or direct commands; code derives events/tasks/date tags. | Save initiates automatic derivatives, including canonical tag writes without the structured protected guard. Task/daily direct commands admit caller values. [MEM-RTE-journal-derive](#mem-rte-journal-derive). |
| Discovery regeneration | Current scan metadata → router/catalog/index/adapter renderers. | Software admits generated projections on explicit calls or watcher refresh, without per-line review; external host loading remains its own decision. [MEM-OBJ-router-manifest](#mem-obj-router-manifest). |
| Governance / optimization | Heuristic diagnosis and advice; UI delete/boost versus database status changes. | Confirmed governance actions can change retained files; optimization apply does not implement its suggested edit. [MEM-RTE-governance-actions](#mem-rte-governance-actions), [RT-RTE-optimization-status](runtime.md#rt-rte-optimization-status). |
| Restore | ZIP bytes overwrite matching paths. | Caller artifact selection and enclosed-path handling, not semantic/protected-memory approval; overlay is not exact rollback. [MEM-RTE-backup-restore](#mem-rte-backup-restore). |

Rejection and withdrawal are different. A rejected proposal and discarded inbox item remain operational records outside canonical retrieval; a successful canonical delete removes future scan input and regenerates derived discovery. Neither action revokes a model's already delivered copy. A failed router refresh can leave canonical and discovery states temporarily divergent. Repeated journal saves can leave events/tasks/date tags after source text changes. These are separate invalidation domains, not one transactional memory revision system. See [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal), [RT-RTE-workspace-write](runtime.md#rt-rte-workspace-write), [MEM-RTE-journal-derive](#mem-rte-journal-derive) and [MEM-RTE-backup-restore](#mem-rte-backup-restore).

No inspected raw-chat-to-compacted-checkpoint-to-next-inference chain was established. The supported trace-fed paths instead retain access aggregates, operational derivatives and maintenance advice. Proposal-derived knowledge retains an item pointer while its rationale persists separately; later ordinary retrieval does not reconstruct the reason. Static template text and ordinary growing turn history are not counted as experience-derived read-back merely because they appear in a prompt. [MEM-RTE-access-feedback](#mem-rte-access-feedback), [MEM-RTE-journal-derive](#mem-rte-journal-derive), [RT-RTE-optimization-status](runtime.md#rt-rte-optimization-status), [RT-RTE-desktop-chat](runtime.md#rt-rte-desktop-chat).

## Read-back

- **Canonical query route:** requester supplies task/query and budget; code selects retained levels using current file contents and metadata, returns a transient package. MCP receives prelude, selected bodies and unloaded summaries; chat receives selected bodies/headings; simulation receives scored metadata only. No automatic unsolicited push to an external agent is established. [RT-RTE-context-query](runtime.md#rt-rte-context-query), [RT-OBJ-context-result](runtime.md#rt-obj-context-result).
- **Explicit body route:** MCP exact skill ID selects skill and immediate dependencies without budget allocation; desktop get-memory and CLI show provide direct reads. Desktop reads additionally change future access metadata, while CLI show does not call that writer. ID lookup is explicit addressing, not evidence of semantic targeting. [RT-RTE-skill-load](runtime.md#rt-rte-skill-load), [MEM-RTE-access-feedback](#mem-rte-access-feedback); SRC-1: `src-tauri/src/cli.rs`, `src-tauri/src/commands/memory.rs`.
- **Discovery/handoff route:** canonical metadata → regenerated adapters/catalog/index → documented external-host reader role → possible direct canonical-file read. The role is afforded by shipped instructions, not observed host wiring. Connector copies or persists an L0 export, not allocated full content; its later reader remains unspecified. [RT-RTE-adapter-handoff](runtime.md#rt-rte-adapter-handoff), [MEM-OBJ-router-manifest](#mem-obj-router-manifest).
- **Operational read-back:** journal date selects a page; task filters select sorted task files; daily API filters retained events by date; recent operational context selects daily/proposal subsets; governance reads daily events for suggestions. These wired API/UI consumers do not make operational subdirectories canonical retrieval candidates. MCP session logs have a writer but no established later consumer in the inspected search. [MEM-OBJ-journal-page](#mem-obj-journal-page), [MEM-OBJ-task-item](#mem-obj-task-item), [MEM-OBJ-daily-log](#mem-obj-daily-log), [MEM-OBJ-session-log](#mem-obj-session-log), [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal).
- **Trace read-back:** durable access map → scan metadata → code ranking/decay; SQLite traces → optimization descriptions/maintenance views, with no canonical rewrite by apply. These have different consumers and authority. [MEM-RTE-access-feedback](#mem-rte-access-feedback), [MEM-OBJ-observability-db](#mem-obj-observability-db), [RT-RTE-optimization-status](runtime.md#rt-rte-optimization-status).

Source trust remains local policy and provenance, not an established truth filter. Parseable content outside excluded paths can enter ranking without a human approval event, confidence cutoff or source verification in the inspected selector. A source-routed memory's `protected: true` inhibits certain later edits; it does not make its text reliable. Natural-language material remains advisory at the provider/host consumer; fixed metadata rules control selection and local mutation only. [MEM-OBJ-memory-meta](#mem-obj-memory-meta), [RT-BAP-context-provider](runtime.md#rt-bap-context-provider), [RT-BAP-workspace-instructions](runtime.md#rt-bap-workspace-instructions).

## Integration issues

1. **Additional protected-mutation exception:** [MEM-RTE-journal-derive](#mem-rte-journal-derive) shows canonical date-tag writes without the structured-save protection check. This supplements rather than contradicts the runtime's API-scoped guard finding in [RT-RTE-workspace-write](runtime.md#rt-rte-workspace-write), but blocks strengthening it to universal protected-file immutability. Restore and onboarding are further alternate admission surfaces. Evidence: SRC-1 `src-tauri/src/commands/journal.rs`, `src-tauri/src/commands/backup.rs`, `src-tauri/src/commands/onboarding.rs`.
2. **Generated contract versus parser:** the boundary quotes the scan comment about a type field and describes canonical YAML; the actual `MemoryMeta` deserializer defaults missing type. Unknown types/statuses can load. Do not treat the generated required fields or the scan comment as a strict parser-enforced admission contract. [MEM-OBJ-memory-meta](#mem-obj-memory-meta) owns this detail; [RT-OBJ-memory](runtime.md#rt-obj-memory) remains a valid container. Evidence: SRC-1 `src-tauri/src/core/types.rs`, `src-tauri/src/core/index.rs`.
3. **Force-load and simulation edge:** [RT-RTE-context-query](runtime.md#rt-rte-context-query) correctly says dependencies lack budget reservation. Added inspection shows a forced L0-only item can be in scored output while omitted from both loaded/unloaded package branches, and budget-exhausted items are not in scored output. Reconciliation should not infer a complete body-delivery list from simulation or guarantee mandatory dependency delivery. Evidence: SRC-1 `src-tauri/src/core/engine.rs`; annotation above.
4. **Operational integrations are incomplete, not absent stores:** [MEM-OBJ-session-log](#mem-obj-session-log) is separate from [MEM-OBJ-daily-log](#mem-obj-daily-log). No session-to-consolidation reader was established by the inspected `src-tauri/src` search. [RT-RTE-ingest-proposal](runtime.md#rt-rte-ingest-proposal) has a callable recent-context reader but no established provider-context/UI wiring here. These limits prevent claiming a unified episodic memory pipeline; they do not erase those retained artifacts or APIs.
5. **Cleanup labels overstate effects:** [MEM-RTE-governance-actions](#mem-rte-governance-actions) distinguishes destructive archive from preserved history, and scratch UI state from successful file removal. [RT-RTE-optimization-status](runtime.md#rt-rte-optimization-status) remains status-only. A coordinator must not merge these into autonomous consolidation/compression. Evidence: SRC-1 `src/views/GovernanceView.tsx`, `src-tauri/src/commands/memory.rs`, `src-tauri/src/commands/observability.rs`.
6. **Part/identity inventory:** L0, L1, L2 and control metadata are declared material parts of [RT-OBJ-memory](runtime.md#rt-obj-memory), not candidate replacements. [MEM-OBJ-router-manifest](#mem-obj-router-manifest) is the retained projection produced by [RT-RTE-adapter-handoff](runtime.md#rt-rte-adapter-handoff); [MEM-OBJ-observability-db](#mem-obj-observability-db) supplies the traces/suggestions used by [RT-RTE-optimization-status](runtime.md#rt-rte-optimization-status). [MEM-RTE-access-feedback](#mem-rte-access-feedback) spans trace writes and later ranking across several runtime routes. These are distinct parts/continuations; no same-referent duplicate of a supplied declaration is intended. Remaining new operational objects/routes have no counterpart among supplied runtime declarations.
7. **Unresolved included branches:** full rename/move/duplicate behavior, complete starter-template bodies, health-score implementation, vault-management isolation and restore/database consistency remain less inspected. Their identities and available paths are retained in the coverage table. No empirical quality, isolation guarantee, complete mutation audit or exact recovery guarantee follows. Unknown pre-existing vault provenance and opaque provider behavior are separately retained in [MEM-RTE-onboarding-write](#mem-rte-onboarding-write) and [RT-CMP-inference-provider](runtime.md#rt-cmp-inference-provider).

## Limitations and checks

Source HEAD was rechecked as `9ed263080cadf98702bebb42d5260b45bd526f6c`, with no source status changes reported. Source identity, public-snapshot boundary, supplied run ID and reviewed-boundary are preserved. The worker read the supplied member types, collection contract, job instruction, worker rules and complete records contract. No source IDs were added, no private/upstream revision evidence was substituted and no other analysis was consulted.

Negative/uncertain statements are scoped to inspected routes; uninspected provider internals and external host policy are not target absences. There is no supplied execution or causal experiment, so activation, correct model use, improved future capacity, consistent restore and autonomous maintenance remain unobserved. The diagnostic test prints selected context and debug information but does not establish an answer-quality oracle; inline tests are inspectable intended checks, not results from this run. SRC-1: `src-tauri/tests/diagnose_vault_query.rs`, `src-tauri/src/core/engine.rs`, `src-tauri/src/core/scoring.rs`.

Deterministic validation: the invocation-specific `commonplace-run validate-output` completed successfully and reported: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” This establishes the performed content check, not semantic acceptance, complete invocation-residue verification or demonstrated system benefit.
