---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "ATLAS runtime baseline: shipped chat, extraction, enrichment, MCP and administrative paths at the frozen repository revision."
run-id: AAS-2026-10-12-atlas-b28ea1ea613f-01
reviewed-boundary: "65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988"
---

# ATLAS runtime report

## Runtime account

### Evidence and claimed work

ATLAS ships two different agent-facing paths. MCP returns indexed logistics data to an external agent; the web server also runs its own model-directed chat and knowledge-maintenance loops. The data-layer claim of no decisions or external communication is not a whole-system guarantee: extraction and enrichment call providers, and chat can write knowledge. See [RT-CLM-data-layer](#rt-clm-data-layer), [RT-RTE-chat-tools](#rt-rte-chat-tools) and [RT-RTE-knowledge-enrichment](#rt-rte-knowledge-enrichment).

This account uses implementation and doctrine/design in SRC-1, at the boundary's frozen commit. No supplied run, test result or intervention establishes activation, reliability, accuracy, performance or benefit. Added inspection beyond the initial boundary tracing includes complete `src/connector-runner.js`, `src/module-loader.js`, `src/ai/extract.js`, `src/ai/chat.js`, `src/ai/llm-client.js`, `src/ai/model-registry.js`, `src/modules/file-watch/index.js`, `src/modules/knowledge-enricher/index.js`, `src/ui/pages/chat.js` and `bin/atlas.js`; the KB storage, model admission, query and pruning ranges of `src/atlas.js`; HTTP authentication, chat/import/KB/config/module handlers and listen path in `src/ui-server.js`; and Google Drive processing/state ranges in `src/modules/google-drive/index.js`. These are implementation evidence, not observed operation. `package.json`, `Dockerfile` and `docker-compose.yml` establish shipped launch/deployment configuration, not successful builds or deployments. Other available source remains unaudited rather than inaccessible.

`package.json` launches `src/index.js` for stdio MCP and `src/ui-server.js` for the combined UI/REST/SSE service. `atlas start` imports the latter. Both instantiate Atlas, load configuration, initialize SQLite and start ConnectorRunner. Only the combined server creates the chat ModelRegistry and ModuleLoader at bootstrap. Its `initDb` call does not choose the separately available PostgreSQL initialization API. SQLite may be configured to a file or fall back to `:memory:`; Markdown lives at the package-relative `knowledge/` directory, independently of the SQLite path (SRC-1, `package.json`, `bin/atlas.js`, `src/index.js`, `src/ui-server.js`, `src/atlas.js`). The persistence horizon therefore depends on actual storage/mount configuration, not merely on running a server.

### Ordinary invocation: browser chat with retained knowledge

A user sends a question in the shipped chat page. The browser owns a module-singleton `messages` array, preserving text during navigation, and posts user/assistant text plus its selected model ID to `/api/chat`. It does not resend the prior tool-result blocks, though it displays their logs. The server checks that messages is a nonempty array and calls `handleChat`. It does not derive a per-user grant set from this request. The client-selected model ID takes precedence over role routing; otherwise chat/default resolution supplies the LlmClient. Model choice and external endpoint mutability are recorded in [RT-CMP-llm-client](#rt-cmp-llm-client).

The server creates a fresh system prompt from current record counts and the full sorted Markdown path index, not the contents of all files. The model chooses whether to request a data query, knowledge read, knowledge write or text answer. A fixed JavaScript switch owns dispatch and rejects unknown tool names. Each requested tool executes with the shared Atlas instance. Individual executor exceptions become JSON error results fed back to the model. Claude and OpenAI-compatible branches encode tool requests/results differently but invoke the same executor and therefore have the same local effect boundary. At most five tool-enabled model rounds run; a sixth, tool-free call requests final text if that budget is exhausted. There is no independent check that the final answer follows the prompt's truthfulness rule. A single round may contain several calls, so five rounds is not five effects.

The terminal API result contains reply text, a tool-call log and accumulated reported token usage. A model failure outside executeTool, including OpenAI argument JSON parsing, reaches the endpoint's error response. A prior successful write is not undone. Durable knowledge written by `save_knowledge` is discoverable on a subsequent invocation through the index and requested reads. Browser conversation text itself has only the inspected page-module lifetime; reload persistence is not established here. See [RT-RTE-chat-tools](#rt-rte-chat-tools) and [RT-BAP-chat-guidance](#rt-bap-chat-guidance) (SRC-1, `src/ui/pages/chat.js`, `src/ui-server.js`, `src/ai/chat.js`, `src/ai/llm-client.js`, `src/atlas.js`).

### State-producing and change-admission paths

AI file import has a distinct loop: HTTP multipart upload → temporary file → SHA-256 deduplication → document text extraction → schema-informed model completion → JSON parsing → minimum-field filtering → database upserts → extraction-log metadata → optional knowledge enrichment. This is [RT-RTE-file-extraction](#rt-rte-file-extraction). The synchronous upsert executor is the ConnectorRunner/Atlas code, not the model provider. Enrichment then selects retained files, asks a model for update actions, filters a minimal envelope and applies actions sequentially through Atlas. There is no separate content approver between a valid model proposal and its filesystem effect; [RT-RTE-knowledge-enrichment](#rt-rte-knowledge-enrichment) separates proposal judgment from mechanical admission.

Material acquisition alternatives share only parts of this loop. File-watch and Google Drive pass a KnowledgeEngine to the pipeline. The `ai_extract` ConnectorRunner path does not. File-watch keeps hash markers and can archive files; Drive uses file ID/modified-time state plus pipeline content hashes. The separately scheduled knowledge-enricher does not reconstruct extracted facts from database rows: it sends extraction filename, group/record counts and timestamp. Its route must not be treated as equivalent to enrichment from extracted entities; see [RT-RTE-extraction-summary](#rt-rte-extraction-summary). Non-AI connectors and CLI seeding parse/map records and use minimum-field validation without a model; these are [RT-RTE-record-import](#rt-rte-record-import). Connector retries and durable checkpoints are recovery machinery, not proof of complete synchronization (SRC-1, `src/connector-runner.js`, `src/modules/file-watch/index.js`, `src/modules/google-drive/index.js`, `src/modules/knowledge-enricher/index.js`, `bin/atlas.js`).

Direct KB editing and model-issued `save_knowledge` can replace whole files without the knowledge engine's additive policy. Configuration POST writes YAML and rebuilds the server's ModelRegistry and connector list. Admin reload also reinitializes extension tables. Neither path updates the already constructed ModuleLoader registry/context in the inspected code. Installed module admission is stronger than a tool-schema extension: loader imports and initializes discovered JavaScript even before the enabled test, supplying the Atlas object, registry and durable module state. Capability-changing code has ordinary process privileges; stop/disable is not rollback. See [RT-RTE-knowledge-edit](#rt-rte-knowledge-edit), [RT-RTE-config-reload](#rt-rte-config-reload) and [RT-RTE-module-lifecycle](#rt-rte-module-lifecycle) (SRC-1, `src/ui-server.js`, `src/module-loader.js`, `src/atlas.js`).

### Forcing cases and enforcement scope

Four source-supported cases bound the consequential guarantees:

1. **An existing KB path receives `create_file`.** The engine's prompt forbids overwriting, but the action writes directly with no existence veto. Chat saves and REST edits also overwrite. Owner: KnowledgeEngine prompt author and Atlas executor. Enforcement point: model instruction, not file-existence admission. Guarantee strength: policy. Implementation conclusion status: wired. Operation conclusion status: uninspected. A conforming model is the required external contract for the engine's additive intent; even that contract does not cover direct writers. [RT-CLM-additive-knowledge](#rt-clm-additive-knowledge) retains the counterexample.
2. **A caller bypasses MCP and posts to REST chat/config/KB.** `checkAuth` is invoked only at the two SSE transport endpoints, without a required permission argument. Configured read tokens therefore do not create a scoped internal-chat grant set. Owner/enforcement: combined-server request branches and startup token array. Guarantee strength: protocol for token checks on MCP; no claimed guarantee for REST authorization. Implementation conclusion status: wired for MCP token checks. Operation conclusion status: uninspected. The external host/network must separately restrict REST access if required. No deployed proxy/firewall is supplied. [RT-ABS-rest-auth](#rt-abs-rest-auth) and [RT-RTE-mcp-query](#rt-rte-mcp-query) bound this finding.
3. **An unchanged file failed earlier.** Pipeline dedup tests existence of a hash in `ai_extract_log`, not whether its last_error is null. A failed extraction log can therefore make an unchanged file return skipped on a later attempt. `force` bypasses the check where exposed by the directory connector, but the inspected web upload does not pass force. Per-record upsert failures also do not turn the pipeline's terminal `ok` false. Owner: processFile. Enforcement point: hash query and exception handlers. Guarantee strength: best effort for processing/recovery, not transactional completion. Implementation conclusion status: wired. Operation conclusion status: uninspected. [RT-RTE-file-extraction](#rt-rte-file-extraction).
4. **A discovered module is disabled or an alternate file writer is used.** Import and initialize occur before the enabled test; native plugin code is not contained by the chat switch. Atlas's KB check is lexical `startsWith(KB_ROOT)`, not a separator-aware/realpath isolation boundary: sibling-prefix paths and filesystem symlink resolution are not excluded by that predicate alone. Owner: ModuleLoader and Atlas. Enforcement point: manifest checks and lexical path check. Guarantee strength: best effort for the path guard, no claimed guarantee for plugin sandboxing. Implementation conclusion status: wired. Operation conclusion status: uninspected. Required external contract: trusted installed code and controlled filesystem layout/OS permissions. Actual layout and installed external modules are unavailable. [RT-RTE-module-lifecycle](#rt-rte-module-lifecycle) and [RT-OBJ-knowledge](#rt-obj-knowledge).

The capability surface includes database queries/upserts, Markdown writes/deletes, provider HTTP calls, acquisition fetches, configuration changes and arbitrary installed module code. The internal chat's current source-defined grant is the fixed tool list including KB save, not arbitrary shell execution. The external MCP tool surface is read-oriented, but its hosting process starts state-producing connectors. The deployed isolation envelope is unobserved. Docker specifies a non-root user and persistent mounts, yet uses a writable app/KB and publishes port 3000; Compose mounts config read-only, which may cause runtime config writes to fail. The boundary also reports absent tracked `knowledge/` input requested by Docker COPY, preventing a proven build claim. Source-level restrictions must not be promoted into end-to-end deployment guarantees (SRC-1, `src/ai/chat.js`, `src/index.js`, `src/ui-server.js`, `src/module-loader.js`, `Dockerfile`, `docker-compose.yml`).

No supplied execution establishes which forcing case occurs in practice. Provider-native tool adapters were inspected for both supported branches; their requests expose ATLAS function schemas and return normalized calls to local dispatch. Provider internals, external MCP host callbacks/workers, installed plugins and deployment network controls remain uninspected. Manual module sync and scheduled timers reach the same run method; the loader has no mutual-exclusion test in those inspected paths, so serialized completion is not guaranteed. This is a bounded source trace, not an exhaustive security audit.

## Shared records

### Components

#### RT-CMP-llm-client
Label: LlmClient model services

Source-native identity: LlmClient instances selected by ModelRegistry for chat, extraction and knowledge. The registry is symbolic in-process Maps/configuration; the model computation is distributed-parametric numerical state hosted by external providers. The repository stores provider/model identifiers and credentials/configuration, not model weights (SRC-1, `src/ai/llm-client.js`, `src/ai/model-registry.js`).

For the **chat role**, parameters are not changed by inspected ATLAS calls; exact served model revision is not pinned by this source; a caller-selected model or mutable OpenAI-compatible endpoint can resolve to different parameters. For the **extract role**, parameters are not changed by its complete calls; a configured model string is not an immutable served-revision pin; mutable endpoint/provider resolution remains possible. For the **knowledge role**, the same non-training complete interface applies; exact weights are unpinned and endpoint mutability remains possible. Roles may resolve to the same client. ATLAS exposes no parameter update in these inspected clients; provider-side training, caching or revisions remain inaccessible rather than established absent.

> this.model = config.model ?? (this.provider === 'claude' ? 'claude-sonnet-4-20250514' : 'gpt-4o');
> --- `src/ai/llm-client.js`

> const opts = { apiKey: this.apiKey };
> if (this.baseUrl) opts.baseURL = this.baseUrl;
> --- `src/ai/llm-client.js`

The constructor's dated Claude default and OpenAI alias are source-native defaults, not evidence of the deployed selections. SDKs are lazy imported. Configuration reload can replace the registry used by web chat and new endpoint-created engines; preexisting module contexts retain their original registry reference.

### Operative objects

#### RT-OBJ-knowledge
Label: Atlas knowledge files

Identity: Markdown files beneath package-relative KB_ROOT, indexed and accessed by Atlas. Form: natural-language Markdown for model/human interpretation; file paths are symbolic selection keys. Substrate: host filesystem, potentially mounted across container lifetimes. Actual content and mount state are unavailable. The runtime identifies the shared effect boundary; memory transformations and revision semantics remain the memory analyst's responsibility (SRC-1, `src/atlas.js`, `docker-compose.yml`).

> const KB_ROOT = join(__dirname, '..', 'knowledge');
> --- `src/atlas.js`

> const resolved = resolve(KB_ROOT, cleaned);
> if (!resolved.startsWith(KB_ROOT)) throw new Error('Path traversal not allowed');
> --- `src/atlas.js`

> const abs = this._resolveKbPath(p);
> mkdirSync(dirname(abs), { recursive: true });
> writeFileSync(abs, content, 'utf8');
> return { path: p, ok: true };
> --- `src/atlas.js`

The path guard covers calls through these methods, not plugin code performing independent I/O. It compares lexical prefixes and does not inspect real filesystem targets. File writes replace content; no version store or rollback is wired in these methods. Separate JSON/filesystem effects can succeed partially.

#### RT-OBJ-atlas-db
Label: Atlas database and progress state

Identity: Atlas.db operational records, connector_state and ai_extract_log. Form: symbolic table fields and JSON record payloads consumed by fixed SQL/JavaScript rules; free-text values remain text data. Substrate on both inspected entry points: better-sqlite3, configured file or :memory:, WAL. The async PostgreSQL method exists but is not called by those entry points (SRC-1, `src/atlas.js`, `src/index.js`, `src/ui-server.js`).

> const path = dbPath ?? this.config?.storage?.path ?? ":memory:";
> this.db = new Database(path);
> this.db.pragma("journal_mode = WAL");
> --- `src/atlas.js`

Progress state stores connector cursors, module hash/file markers and scheduled-enrichment timestamps. Extraction metadata stores counts/errors/usage, not a record-level provenance join. Counts returned by a producer are not proof of durable admission: generic upsert can return silently for a disabled model, while the pipeline increments totalRecords whenever the callback does not throw.

> if (!this._enabledModels.has(resolved)) return;
> if (!record.id) return;
> --- `src/atlas.js`

### Routes

#### RT-RTE-chat-tools
Label: Internal chat tool loop

Endpoints/progression: browser messages → POST /api/chat → handleChat → role/explicit model → model-selected calls → executeTool → Atlas → provider continuation → reply/log/usage. Owner: user supplies the request/history/model preference; model chooses tools and answer; JavaScript decides whether a tool name dispatches. Context: current counts, KB filenames, guidelines, submitted history and current-run tool results. Symbolic tool schemas/dispatch frame natural-language/model judgment. No answer oracle is supplied; data-tool results are evidence, not an expected-answer reference. Mode: open user questions. Knowledge-save trigger/proposal: model's tool call; admission: direct write; veto: unknown names or executor error, not human per-content approval. Recovery: tool errors returned to model, final tool-free call after budget; no write rollback (SRC-1, `src/ai/chat.js`, `src/ui/pages/chat.js`, `src/ui-server.js`).

- Immediate return: reply text, tool-call log and usage, or endpoint error.
- Later read-back: saved Markdown can be indexed/read by later chats or engines; browser sends accumulated user/assistant text on subsequent requests but omits prior tool-result blocks.
- Delegated visibility: configured provider receives prompt/history and returned tool contents; all tools use the shared Atlas, without a per-user scope in handleChat.
- Selection predicate: explicit registry model ID or role fallback; model requests tool name/arguments; KB filenames are supplied before requested file-content reads.
- Invalidation or expiry: tool-loop context ends with request; browser module state lasts across navigation; saved files persist until replaced/deleted; no KB TTL in this loop.
- Activation or effect: wired local tool dispatch can query or save knowledge; model compliance and effects on later answers are unobserved.
- Evidence limits: source only; no trace authenticates actual tool use, answer correctness or future benefit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> case 'save_knowledge':
>   return atlas.writeKnowledgeFile(args.path, args.content);
> --- `src/ai/chat.js`

> // If we exhausted iterations, do one final call without tools
> const finalRes = await llm.chatWithTools(llmMessages, [], systemPrompt);
> --- `src/ai/chat.js`

#### RT-RTE-file-extraction
Label: AI file extraction and admission

Endpoints: upload/file acquisition → processFile → parser → extract → upsert callback → logExtraction → optional KnowledgeEngine. Owner: caller chooses file/force/callback; extractor model proposes record groups; software canonicalizes types and applies validateMapped; executor writes records. Prompt guidance comes from model registry/schema descriptions and normalization/ID rules; only accepted record data, extraction metadata and optional knowledge outputs persist, not the completion reasoning. Mode: open documents, not a bounded experiment. No answer oracle. Human upload starts the workflow, not per-record approval. Veto: configuration, parse failure, unknown type, minimum-field checks, DB error; no semantic accuracy approval. Recovery: one model retry for parsing; per-record failures logged and continued; no cross-record/KB transaction or rollback (SRC-1, `src/ai/extract.js`, `src/ai/extract-pipeline.js`, `src/mapper.js`, `src/connector-runner.js`, `src/ui-server.js`).

- Immediate return: processing status, filename/hash, group and record counts, usage and optional knowledgeUpdates; dedup can return skipped.
- Later read-back: database records reach query tools; extraction-log hash controls later processing; knowledge files reach later engines/chats when enrichment is passed.
- Delegated visibility: provider receives filename and first 40000 characters of extracted text by default, plus schema prompt; optional knowledge provider receives summaries and selected KB text.
- Selection predicate: whole-file content hash skips any existing log unless force; extraction resolves recognized entity type and accepts records passing validateMapped; enrichment summaries include only first ten records per group.
- Invalidation or expiry: changed content changes hash; force bypasses dedup; record upsert replaces ID-matched data; admin retention can remove operational records; KB invalidation is separate.
- Activation or effect: database callback and optional knowledge application are wired; successful record-count reporting does not certify each write or subsequent use.
- Evidence limits: optional parsers/providers/actual files unobserved; first-text truncation can omit document facts; per-record errors and silent generic upsert returns weaken completion claims.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const existing = atlas.db.prepare('SELECT file_hash FROM ai_extract_log WHERE file_hash = ?').get(hash);
> --- `src/ai/extract-pipeline.js`

> const { valid, errors } = validateMapped(resolvedType, record);
> if (valid) {
>   validRecords.push(record);
> --- `src/ai/extract.js`

The validator is not full JSON Schema validation:

> if (!record.id) errors.push('Missing required field: id');
> if (entity === 'shipments' && !record.status) errors.push('Missing field: status');
> if (entity === 'carriers' && !record.name) errors.push('Missing field: name');
> --- `src/mapper.js`

It additionally tests rate origin/destination presence. Schema-valid enums, truth and extraction completeness are not established by those checks. Equivalent non-AI imports share these minimum checks; direct native plugins/API methods are not forced through extract's gate.

#### RT-RTE-knowledge-enrichment
Label: Knowledge engine model admission

Endpoints: enrichFromExtraction/enrichFromText → relevant-file selection → complete → parse/minimal envelope → applyUpdates → Atlas writes. Owner: caller supplies source/date/topic/input; model proposes action/path/content; software admits known actions and minimally structured envelopes. Human contribution is input initiation when manually called, not approval of returned updates. Mode: open incoming information. No answer oracle; existing files provide comparison context rather than a verified expected outcome. Guidance requests add-only/source-attributed/same-language updates and contradiction flags. Proposed output persists as Markdown plus attribution; analysis/reason values are returned but no independent durable decision ledger is wired here. Rejection: unconfigured model, JSON failure after retry, missing action/path, unknown action or write exception. Recovery: per-update results; no batch rollback (SRC-1, `src/ai/knowledge-engine.js`).

- Immediate return: ok/error, analysis, per-update applied/error status and usage; ok can coexist with failed individual updates.
- Later read-back: applied files are eligible for subsequent relevant-file selection and chat reads through the shared Atlas store.
- Delegated visibility: provider receives selected full files and new information; retry after malformed output receives prior model response plus format hint, not the original userPrompt.
- Selection predicate: topic substring in path scores three; keyword substring in contents scores one each; positive-score files sorted descending; default five files/30000 characters, but first oversized file can exceed the character budget.
- Invalidation or expiry: no TTL; append/mark modifies selected file; create_file writes whole content even if path already exists; other writers can replace/delete files.
- Activation or effect: source wires automatic application of proposals; no supplied evidence that contradiction flags alter later decisions or that model semantic rules are followed.
- Evidence limits: opaque provider reasoning; selected context may omit relevant files; extraction input summaries are bounded; no observed knowledge quality or benefit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const validUpdates = updates.filter(u => u && typeof u === 'object' && u.action && u.path);
> --- `src/ai/knowledge-engine.js`

> case 'create_file':
>   this._applyCreateFile(update, source, date);
>   results.push({ ...update, applied: true });
>   break;
> --- `src/ai/knowledge-engine.js`

These are executable admission mechanics, not a theory-builder classification. The prompt requests comparison and flags conflicts; whether a model formulates or criticizes explanations is not exposed. Detailed retained-knowledge revision findings belong to the memory and epistemic members.

#### RT-RTE-extraction-summary
Label: Scheduled extraction metadata enrichment

Endpoints: enabled module start/timer/manual sync → query ai_extract_log → buildSummaryForEntry → enrichFromText → persist cursor. Owner: ModuleLoader schedules; module chooses pending entries and filename topic; KnowledgeEngine/provider performs the admission in [RT-RTE-knowledge-enrichment](#rt-rte-knowledge-enrichment). Mode: ongoing incoming metadata, no answer oracle or per-entry human approval. Trigger is a new successful extraction-log timestamp; proposed change is a model-generated KB update based on metadata, not the document facts. Software/model decide; failed enrichment can still advance the latest timestamp, preventing automatic replay. No rollback of successful updates (SRC-1, `src/modules/knowledge-enricher/index.js`).

- Immediate return: enriched count or skip/error; logs report applied-update count.
- Later read-back: persisted last_processed_at selects subsequent entries; generated KB files reach later engines/chats.
- Delegated visibility: provider receives extraction filename/counts/timestamp plus selected retained files, not associated extracted record bodies from this driver.
- Selection predicate: processed_at greater than cursor, last_error IS NULL, oldest first, configurable max_files_per_run default five; filename heuristics supply topic.
- Invalidation or expiry: cursor advances after a returned enrichment failure as well as success; same-timestamp entries outside a limited batch can be excluded by the strict greater-than predicate.
- Activation or effect: wired metadata-to-KB proposal/application path; original extraction fact reconstruction is not wired in buildSummaryForEntry.
- Evidence limits: no run traces; metadata may support only that an extraction occurred, not substantive logistics assertions.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> function buildSummaryForEntry(entry) {
>   return `Extracted file: ${entry.filename}\nEntity groups: ${entry.entity_count}\nTotal records: ${entry.record_count}\nProcessed at: ${entry.processed_at}`;
> }
> --- `src/modules/knowledge-enricher/index.js`

#### RT-RTE-record-import
Label: Connector and seed record admission

Endpoints: configured REST/filesystem connector or CLI seed → parse/envelope normalization → optional mapping/composite expansion → validateMapped → type-specific/generic upsert → state/count. Owner: caller/configuration supplies source/mappings; fixed software decides minimum validity; no model or answer oracle. Mode: ongoing synchronization or explicit seed load. Human control supplies configuration/data and can disable connector, but fetched row content receives software admission. Recovery: REST timeout, bounded exponential retry on thrown connector errors; per-file/per-row catches continue; terminal connector state records current time even after final failure. This cursor is not proof of a complete successful source read (SRC-1, `src/connector-runner.js`, `bin/atlas.js`, `src/atlas.js`).

- Immediate return: seed count/logs, internal synchronized count and connector status/error state.
- Later read-back: retained records reach MCP/chat/REST queries; last_synced_at can become a subsequent REST since_param.
- Delegated visibility: REST source receives configured credentials and optional since cursor; imported rows are local unless later exposed to queries/models.
- Selection predicate: enabled connectors, configured entity/mapping/formats; seed entity from filename; minimum validation before dispatch.
- Invalidation or expiry: repeated ID upserts replace payload; configured/admin pruning removes old closed shipments and related rows plus expired rates; source deletions are not propagated by these upsert loops.
- Activation or effect: wired database admission and incremental fetch cursor; full dataset equivalence and successful durable count are unobserved.
- Evidence limits: live service completeness/parser correctness unobserved; row-level catches can coexist with a successful connector terminal status.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const { valid, errors } = validateMapped(entity, record);
> if (!valid) {
>   console.error(`[ATLAS] Connector "${connector.id}" skip: ${errors.join(', ')}`);
>   continue;
> }
> this._upsert(entity, record);
> synced++;
> --- `src/connector-runner.js`

#### RT-RTE-mcp-query
Label: External MCP read service

Endpoints: external host → stdio transport or HTTP SSE session/message → registered schema/callback → Atlas query → JSON text content/error. Owner: external host decides request/next action; ATLAS owns fixed data query. No ATLAS model decision in this route. Stdio exposes generic discovery/record tools in addition to domain tools; the inspected HTTP server exposes a smaller domain-oriented set. The `query` implementation is token substring matching over up to 500 rows per shipments/carriers/lanes table, not model inference or a search across every enabled model (SRC-1, `src/index.js`, `src/ui-server.js`, `src/atlas.js`).

- Immediate return: serialized data/context or error to calling MCP host.
- Later read-back: query consumes operational data changed by imports; no query-produced retained adaptation in these callbacks.
- Delegated visibility: external host receives requested results; its later worker/action use is outside this boundary.
- Selection predicate: schema arguments and domain SQL; generic get_records targets enabled models on stdio; query scores token substring matches and truncates top results.
- Invalidation or expiry: session removed on SSE close; data changes by upsert/prune; no client-result cache validity protocol established here.
- Activation or effect: fixed returning query path wired; no evidence of downstream host behavior or answer accuracy.
- Evidence limits: MCP SDK and host internals not inspected; HTTP deployment/network isolation unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const tokens = question.toLowerCase().split(/\s+/).filter(t => t.length > 2);
> --- `src/atlas.js`

> const auth = checkAuth(req);
> if (!auth.ok) {
>   res.writeHead(401, { "Content-Type": "application/json" });
>   res.end(JSON.stringify({ error: "Unauthorized", reason: auth.reason }));
>   return;
> }
> --- `src/ui-server.js:231-236`

This passage is the GET transport check; POST /mcp/message repeats it. RequiredPermission is not passed. Possession of a configured token controls transport access; sessionId lookup does not bind the stored transport to the token identity. Stdio relies on host launch/access control, not this HTTP token check. The process starts connectors, so read-only tool callbacks do not imply a read-only process.

#### RT-RTE-knowledge-edit
Label: Direct knowledge file editing

Endpoints: browser editor or direct REST caller → /api/kb/file → Atlas write/delete; chat save reaches the same write method under [RT-RTE-chat-tools](#rt-rte-chat-tools). Owner: editor user supplies complete content/path and presses save/delete; server implements I/O without an enrichment review. Direct API caller identity need not be human. Mode: open edits; no oracle. Guidance is the editor UI/Markdown formatting, not the engine's add-only rules. Proposal/admission: supplied full file content admitted after JSON/path presence and filesystem checks. Veto/recovery: caller can cancel before sending; malformed request/write failure rejected; replacement/deletion has no stored prior-version rollback (SRC-1, `src/ui/pages/knowledge.js`, `src/ui-server.js`, `src/atlas.js`).

- Immediate return: path/ok or HTTP error; browser can reload the file/tree.
- Later read-back: replacement content is eligible for engine selection and chat reads across later requests.
- Delegated visibility: API reads expose file content; subsequent model routes can deliver it to the configured provider.
- Selection predicate: caller chooses path; POST appends .md if absent; tree enumerates Markdown files.
- Invalidation or expiry: full replacement or DELETE; no version/TTL mechanism in inspected handlers.
- Activation or effect: write/delete wired independently of model guidance or source-attribution checks.
- Evidence limits: actual editors/caller identities and content unavailable; browser confirmation is not API authorization.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const { path: p, content } = JSON.parse(body);
> if (!p) return json({ error: 'path is required' }, 400);
> json(atlas.writeKnowledgeFile(p, content ?? ''));
> --- `src/ui-server.js`

#### RT-RTE-config-reload
Label: Configuration and model routing replacement

Endpoints: POST /api/config, POST /api/setup/save or admin reload → Atlas configuration → new ModelRegistry/connector list; admin reload reinitializes extension models. Setup save serializes submitted JSON as YAML and performs the same registry/connector replacement; its separate test-ai endpoint makes a caller-configured completion with a requested literal answer, but does not gate config admission on a successful test. Owner: caller proposes YAML or reload; software accepts a non-null parsed object for config POST. Human authorship is possible but caller identity is unresolved; no oracle, bounded experiment or result-based improvement selection. Changes admit provider/model/endpoint, source/mapping and enabled-model settings. POST writes config before later reload steps; a subsequent error need not undo the file. Constructor-held ModuleLoader context and startup configuredTokens are not rebuilt by these handlers. Recovery: caller must restore/repost prior config; no automatic rollback (SRC-1, `src/ui-server.js`, `src/atlas.js`, `src/ai/model-registry.js`).

- Immediate return: save/reload status with timestamps or error; admin response reports connector/model counts.
- Later read-back: config persists to config.yml; future process startup consumes it; current chat uses replaced registry while existing modules may use older references.
- Delegated visibility: changed provider settings control later model destinations; GET /api/config returns raw YAML and parsed configuration without the MCP token gate.
- Selection predicate: caller YAML, non-null object parse check, role IDs referencing registered clients, default fallback.
- Invalidation or expiry: subsequent POST/reload/startup; running connector timers restarted, not previously completed effects undone.
- Activation or effect: live chat model routing and connector-list replacement wired; universal live configuration propagation is not established.
- Evidence limits: no deployed config/secrets or write-success trace; read-only Compose config mount can reject file writes.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> atlas.loadConfig(configPath);
> modelRegistry = ModelRegistry.fromConfig(atlas.config?.ai);
> runner.stop();
> runner.connectors = (atlas.config?.connectors ?? []).filter(c => c.enabled !== false);
> runner.start();
> --- `src/ui-server.js:652-656`

#### RT-RTE-module-lifecycle
Label: Installed module admission and execution

Endpoints: server bootstrap → discover built-in/external manifest directories → import index.js → initialize full context → optional start → timer/manual run; REST enable/disable persists a flag and starts/stops an existing instance. Owner: filesystem installer proposes code/manifest, loader validates manifest presence/required values, administrator/caller configures start, native module code decides run effects. No answer oracle or per-effect human approval. Operating mode: extension installation plus scheduled/open sync. Guidance: manifest/config/runtime context; persists code/config and module state, not a verified capability improvement. Admission rejects missing manifest keys/index or import/init exceptions, not unsafe semantics. Rollback: stop clears timer and calls optional stop; does not unload code, revert I/O or undo import/initialize (SRC-1, `src/module-loader.js`, `src/ui-server.js`).

- Immediate return: module status/error and optional run result; bootstrap logs discoveries.
- Later read-back: module state is stored in connector_state via module-prefixed keys; built-in hash/cursor/file state affects subsequent runs; installed code/config loaded on future startup.
- Delegated visibility: initialize receives Atlas, module config, registry, logger and durable state access; external implementations are unavailable.
- Selection predicate: valid manifest/index discovered in src/modules and package-root modules directory; import/initialize precede enabled predicate; timers require a positive configured/default interval.
- Invalidation or expiry: disable/stop cancels scheduled timer; state has no loader TTL; imported code remains in process; timer/manual invocations have no inspected mutual-exclusion guard.
- Activation or effect: wired native-code execution and full-context grant; neither disabled flag nor manifest validation is a sandbox.
- Evidence limits: installed external modules, actual process privileges and live overlap unobserved; no successful plugin or isolation demonstration.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const mod = await import(indexPath);
> const instance = mod.default ?? mod;
> --- `src/module-loader.js`

> const ctx = this._buildContext(id, modConfig);
> if (typeof instance.initialize === 'function') {
>   await instance.initialize(ctx);
> }
>
> // Start if enabled
> if (modConfig.enabled !== false && modConfig.enabled !== undefined) {
>   await this.startModule(id);
> }
> --- `src/module-loader.js`

### Claims

#### RT-CLM-data-layer
Label: Data layer only scope claim

Claimed operation: Atlas core's comment describes a data layer without actions, decisions or external communication. Form: natural-language source doctrine, stored in source, not an executable prohibition (SRC-1, `src/atlas.js`).

> * Universal logistics MCP server — data layer only.
> * No actions, no decisions, no external communication.
> --- `src/atlas.js`

The narrower returning MCP callbacks fit a read-oriented role. The complete shipped system includes provider-mediated extraction, model-selected KB writes and native modules, so the comment cannot establish a whole-system absence of decisions/effects/communication. The distinction is warranted by [RT-RTE-chat-tools](#rt-rte-chat-tools), [RT-RTE-file-extraction](#rt-rte-file-extraction) and [RT-RTE-module-lifecycle](#rt-rte-module-lifecycle).

#### RT-CLM-additive-knowledge
Label: Knowledge engine add-only policy

Claimed operation: existing knowledge is never overwritten, only augmented or flagged. Form: natural-language prompt policy interpreted by provider; source comment also attributes this intent. Scope: KnowledgeEngine, not all writers (SRC-1, `src/ai/knowledge-engine.js`).

> 1. NEVER delete or overwrite existing information — only ADD or MARK contradictions.
> --- `src/ai/knowledge-engine.js`

Counterexample at executable admission:

> _applyCreateFile(update, source, date) {
>   const { path: relPath, content } = update;
>   const src = update.source ?? source;
>   const attribution = `\n\n> Джерело: ${src} (${date})\n`;
>   this.atlas.writeKnowledgeFile(relPath, content + attribution);
> }
> --- `src/ai/knowledge-engine.js`

No existence check intervenes here. Atlas replaces content, while chat/API use that writer directly. The guarantee is policy, not invariant; model cooperation is necessary but coverage is narrower than the store's mutation surface. Source-attribution text is appended by engine actions, but its provenance/truth is not independently checked and direct saves need not include it.

### Evidenced absences

#### RT-ABS-rest-auth
Label: REST route authorization gate absent

- implementation conclusion status: absent

Bounded search at SRC-1 revision 65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988: `rg -n 'checkAuth' src/ui-server.js` locates the definition and exactly two calls, in GET /mcp and POST /mcp/message. Inspected request dispatch, REST chat/import/KB/config/admin/module handlers and server tail contain no common authentication middleware or branch-local gate for these REST routes. The quoted direct write in [RT-RTE-knowledge-edit](#rt-rte-knowledge-edit) and token checks in [RT-RTE-mcp-query](#rt-rte-mcp-query) retain the contrasting execution passages. This establishes absent **server-side REST use of the shipped token gate**, not absent external network authentication or absence of every possible deployment restriction. Deployment safety and actual anonymous use remain unobserved.

### Behavioral-authority paths

#### RT-BAP-chat-guidance
Label: Chat prompt and knowledge delivery authority

Consumer: role-selected chat model. Channel: system prompt with counts/KB paths/guidelines and tool-result messages containing requested KB content. Force: model-interpreted natural-language guidance/evidence, not a deterministic factuality invariant; symbolic dispatch gives returned tool calls concrete query/write authority. Horizon: current request/rounds; saved files and repeated browser text can reach later requests (SRC-1, `src/ai/chat.js`, `src/ui/pages/chat.js`).

> - Call tools to get real data before answering. Do not guess or fabricate data.
> - If no results are found, say so clearly.
> --- `src/ai/chat.js`

Requested truthfulness is not validated against an answer oracle. File delivery is wired; compliance, activation and benefit are unobserved. The path does not grant shell commands or plugin installation to the chat model.

#### RT-BAP-native-module
Label: Native module process authority

Consumer: installed module JavaScript. Channel: native import/initialize and ModuleContext containing Atlas, registry and config. Force: executable process code, rather than advisory model text. Horizon: import-time effects, loaded process lifetime and durable state/files across later runs. Effects can bypass chat dispatch and KB method checks using ordinary JavaScript/Node APIs; actual installed external code and OS grants remain unavailable (SRC-1, `src/module-loader.js`).

> return {
>   atlas,
>   config: moduleConfig ?? {},
>   registry: this.registry,
> --- `src/module-loader.js`

The loader supplies capabilities before optional start. Manifest validity and enabled state therefore do not establish isolation. See [RT-RTE-module-lifecycle](#rt-rte-module-lifecycle) for admission and recovery limits.

## Annotations

none
