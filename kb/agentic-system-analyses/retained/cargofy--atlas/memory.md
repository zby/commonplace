---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "ATLAS memory: shared Markdown enrichment and read-back, operational records, extraction metadata, progress checkpoints and browser conversation replay."
run-id: AAS-2026-10-12-atlas-b28ea1ea613f-01
source-identity: "https://github.com/cargofy/ATLAS"
reviewed-boundary: "65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988"
---

# ATLAS memory report

## Boundary and evidence

The subject is ATLAS's shipped retention-to-consumption loop at SRC-1, commit `65b91b4fd5d703e8a82ad8fa2a9b8d2f38754988`. This member includes operational records, Markdown knowledge, extraction logs, acquisition/enrichment checkpoints, browser history, model-context selection, direct editing and withdrawal. Configuration and module state are included where they govern those mechanisms. External MCP hosts' memory and provider-internal state are not attributed to ATLAS. No deployed KB, provider response, test result or execution trace was supplied. Consequently source establishes wiring, not exercised recall or improved answers.

Direct reads added or rechecked `src/ai/knowledge-engine.js`, `src/ai/extract.js`, `src/ai/extract-pipeline.js`, `src/ai/chat.js`, `src/modules/file-watch/index.js`, `src/modules/knowledge-enricher/index.js`, the Drive processing range of `src/modules/google-drive/index.js`, `src/module-loader.js`, database/state/query/pruning/KB ranges of `src/atlas.js`, KB/enrichment/pruning handlers of `src/ui-server.js`, `src/ui/pages/chat.js`, `src/ui/pages/knowledge.js` and selected mock-test ranges of `src/__tests__/knowledge-engine.test.js`. These supply implementation and test-design evidence under SRC-1. The CLI, non-AI connector, model-provider, configuration-reload and MCP accounts below additionally rely on the supplied runtime records; their quotations are not claimed as fresh direct reads here.

| Entry point or operation | Source paths in SRC-1 | Coverage and limits |
|---|---|---|
| CLI seed; REST/non-AI imports; incremental connectors | `bin/atlas.js`, `src/connector-runner.js`, `src/atlas.js` | Supplied [RT-RTE-record-import](runtime.md#rt-rte-record-import); direct storage reads in [MEM-OBJ-record-payloads](#mem-obj-record-payloads) and [MEM-OBJ-progress-state](#mem-obj-progress-state). Source deletion propagation is not established. |
| AI upload and directory connector | `src/ui-server.js`, `src/ai/extract.js`, `src/ai/extract-pipeline.js`, `src/connector-runner.js` | [RT-RTE-file-extraction](runtime.md#rt-rte-file-extraction), [MEM-OBJ-extract-log](#mem-obj-extract-log); direct transformation reads. Connector path lacks the immediate enrichment engine supplied by upload/modules, per runtime. |
| File-watch and Drive acquisition | `src/modules/file-watch/index.js`, `src/modules/google-drive/index.js` | Direct checkpoint and pipeline-call reads; [MEM-OBJ-progress-state](#mem-obj-progress-state). Live transport/credentials and historical documents unavailable. |
| Immediate entity-to-KB and raw-text-to-KB enrichment | `src/ai/knowledge-engine.js`, `src/ui-server.js` | Direct reads; annotations on [RT-RTE-knowledge-enrichment](runtime.md#rt-rte-knowledge-enrichment) and [RT-OBJ-knowledge](runtime.md#rt-obj-knowledge). Original input, model reasoning and initial KB provenance not retained by a separate ledger here. |
| Scheduled metadata-to-KB enrichment | `src/modules/knowledge-enricher/index.js` | Direct read; [RT-RTE-extraction-summary](runtime.md#rt-rte-extraction-summary), [MEM-OBJ-extract-log](#mem-obj-extract-log). Counts are not document facts. |
| Chat list/read/save and later history | `src/ai/chat.js`, `src/ui/pages/chat.js` | Direct tool definitions, executor and consumer reads; [RT-RTE-chat-tools](runtime.md#rt-rte-chat-tools), [MEM-OBJ-messages](#mem-obj-messages), [MEM-RTE-conversation-replay](#mem-rte-conversation-replay). No explicit history/content truncation budget in these consumers. |
| Human KB tree/read/save/delete/folder creation | `src/ui/pages/knowledge.js`, `src/ui-server.js`, `src/atlas.js` | Direct reads; [RT-RTE-knowledge-edit](runtime.md#rt-rte-knowledge-edit). Folder creation changes discovery layout, not knowledge content by itself. Generic API callers need not be human. |
| MCP/REST record read-back | `src/index.js`, `src/ui-server.js`, `src/atlas.js` | Registered-tool search plus supplied [RT-RTE-mcp-query](runtime.md#rt-rte-mcp-query); direct query/getRecords reads. Registered MCP callbacks here do not expose the chat knowledge read/save tools. External host continuation excluded. |
| Record pruning and knowledge withdrawal | `src/atlas.js`, `src/ui-server.js` | Direct reads; [MEM-RTE-record-pruning](#mem-rte-record-pruning), [RT-RTE-knowledge-edit](runtime.md#rt-rte-knowledge-edit). No linked withdrawal of derived Markdown. |
| Config/module initialization, timers and state | `src/module-loader.js`, `src/ui-server.js`, `src/ai/model-registry.js` | Direct loader reads and supplied [RT-RTE-module-lifecycle](runtime.md#rt-rte-module-lifecycle), [RT-RTE-config-reload](runtime.md#rt-rte-config-reload). External plugin code unavailable; provider-private persistence opaque. |
| Evaluators | `src/__tests__/knowledge-engine.test.js`, `src/__tests__/models.test.js`, `src/validate-models.js` | Direct selected knowledge tests and supplied boundary evaluation inventory. Mock assertions establish evaluation design, not an operational evaluator gating KB admission or observed quality. |

The source register is in `boundary.md`. The checkout HEAD matched the pin and Git status was clean at inspection. All material knowledge-writing routes identified by runtime were checked against the actual store, rather than treating the additive engine policy as a store invariant.

## Core ideas

1. **One Markdown store has several admission authorities.** The enrichment model proposes updates that software applies automatically. A chat model can replace files with a tool call. A browser user can explicitly save or delete a file; the same API admits generic callers. These do not share a semantic approval gate. [RT-OBJ-knowledge](runtime.md#rt-obj-knowledge), [RT-RTE-knowledge-enrichment](runtime.md#rt-rte-knowledge-enrichment), [RT-RTE-knowledge-edit](runtime.md#rt-rte-knowledge-edit), [RT-CLM-additive-knowledge](runtime.md#rt-clm-additive-knowledge).
2. **Read-back differs by consumer.** Enrichment software automatically selects positively scoring full files for a provider prompt. Chat automatically receives filenames but requests actual content by path. A knowledge editor explicitly opens a file. Database queries select symbolic rows. Selection and delivery are wired; none establishes that a later model follows the delivered content. See the annotations and [MEM-OBJ-record-payloads](#mem-obj-record-payloads).
3. **Operational traces govern replay and can also become text knowledge.** Hash/error/count logs suppress repeat extraction; module checkpoints select future work; the scheduled enricher turns only log metadata into potential Markdown changes. That latter trace-fed update can reach later chat/engine invocations, but is not learning demonstrated by improved capacity. [MEM-OBJ-extract-log](#mem-obj-extract-log), [MEM-OBJ-progress-state](#mem-obj-progress-state), [RT-RTE-extraction-summary](runtime.md#rt-rte-extraction-summary).
4. **A contradiction is retained prose, not executable deprecation.** It keeps the two attributed values and a verification request, without marking the original assertion ineligible at retrieval. Reasons requested in update JSON are not automatically written into the file. [MEM-OBJ-contradiction-block](#mem-obj-contradiction-block).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-record-payloads
Label: Operational record payloads

Part of: [RT-OBJ-atlas-db](runtime.md#rt-obj-atlas-db)

Source-native identity: the `data` JSON payloads and query/index columns in operational tables, distinct from extraction logs and progress rows. Representational form: symbolic IDs, fields and relations consumed by SQL/JavaScript; embedded free text can later be interpreted by models/humans. Substrate: Atlas database, SQLite file or memory on shipped entry points. Lineage: seed/import/mapping and model-extracted document entities, followed by ID upserts. Initial deployment content and source truth are unavailable. Evidence: SRC-1, `src/atlas.js`, `src/ai/extract.js`, `src/ai/extract-pipeline.js`; admission distinctions and physical producer paths are supplied by [RT-RTE-record-import](runtime.md#rt-rte-record-import) and [RT-RTE-file-extraction](runtime.md#rt-rte-file-extraction).

> ON CONFLICT(id) DO UPDATE SET data = excluded.data
> --- `src/atlas.js`

This generic upsert replaces the payload rather than retaining an earlier revision. Type-specific upserts likewise replace data, as the runtime account describes. Database consumers include MCP/REST callers and chat tools. `getRecords` selects an enabled model, equality filters via `json_extract` and default limit 50. `query` scores token-substring matches in at most 500 rows each of shipments/carriers/lanes and returns default top ten; its broad natural-language label is not semantic retrieval over every table (SRC-1, `src/atlas.js`; [RT-RTE-mcp-query](runtime.md#rt-rte-mcp-query)). These records are data evidence at the model consumer, not privileged instructions. Provider-visible query results are separate from original document text and may lack extraction lineage. Pruning changes future record results without retracting Markdown derived from them; [MEM-RTE-record-pruning](#mem-rte-record-pruning).

#### MEM-OBJ-extract-log
Label: AI extraction log

Part of: [RT-OBJ-atlas-db](runtime.md#rt-obj-atlas-db)

Source-native identity: `ai_extract_log` rows keyed by `file_hash`. Form: symbolic SHA-256, filename, entity/record counts, token usage, error and processed timestamp. Substrate: SQLite on shipped entry points. Lineage: pipeline processing outcomes, including errors, not the raw document, model completion or extracted-record bodies. These are access/progress metadata rather than a semantic fact store. Evidence: SRC-1, `src/ai/extract-pipeline.js`, `src/atlas.js`, `src/modules/knowledge-enricher/index.js`; closest supplied route is [RT-RTE-file-extraction](runtime.md#rt-rte-file-extraction).

> INSERT INTO ai_extract_log (file_hash, filename, entity_count, record_count, input_tokens, output_tokens, last_error, processed_at)
> --- `src/ai/extract-pipeline.js`

Later consumers differ. Pipeline checks any existing hash, including a failed extraction, unless force is passed. Stats aggregate metadata for display. Scheduled enrichment selects rows with `last_error IS NULL` and a timestamp after its cursor, then renders just filename/counts/time into text. [RT-RTE-extraction-summary](runtime.md#rt-rte-extraction-summary) retains that exact transformation passage. The provider cannot recover particular document facts from counts. Software authors/adopts the log automatically; there is no content approval. Reprocessing a hash replaces its log fields/timestamp; this is not an append-only raw event history. A record count can exceed successfully retained entities because optional callback absence or silent upsert return still increments it (SRC-1, `src/ai/extract-pipeline.js`; [RT-OBJ-atlas-db](runtime.md#rt-obj-atlas-db)). No benefit is established by this trace retention.

#### MEM-OBJ-progress-state
Label: Connector and module progress state

Part of: [RT-OBJ-atlas-db](runtime.md#rt-obj-atlas-db)

Source-native identity: `connector_state`, including module-prefixed keys written through ModuleContext. Form: symbolic timestamps and JSON/string markers controlling fixed predicates. Substrate: same database as records. Lineage: connector outcomes and module runs; initial checkpoints may be absent, after which code derives new markers. No human per-marker approval is wired. Evidence: SRC-1, `src/atlas.js`, `src/module-loader.js`, `src/modules/file-watch/index.js`, `src/modules/google-drive/index.js`, `src/modules/knowledge-enricher/index.js`; supplied containers/routes [RT-RTE-module-lifecycle](runtime.md#rt-rte-module-lifecycle) and [RT-RTE-record-import](runtime.md#rt-rte-record-import).

> const stateKey = `module:${moduleId}`;
> --- `src/module-loader.js`

> const row = atlas.getConnectorState(`${stateKey}:${key}`);
> --- `src/module-loader.js`

Material parts have different selectors and failure semantics:

- File-watch's `hash:<hash>` JSON records filename/time/count after `result.ok`; it can mark a pipeline duplicate as processed and optionally archive the physical source. The next scan skips a present marker. This is not curated logistics knowledge.
- Drive's `file:<id>` stores modifiedTime/time/count/filename after success or pipeline dedup. The next sync skips matching modifiedTime. The downloaded temporary file is removed after the pipeline returns; retained marker/display fields do not constitute the document payload.
- Knowledge-enricher's `last_processed_at` selects strictly newer successful-log timestamps, oldest first with default batch size five. Returned `ok:false` enrichment still advances the cursor; thrown entries do not themselves advance it, although a later entry can move the overall cursor past them. Equal-timestamp entries outside a limited batch can be skipped permanently.
- Connector `last_synced_at` can supply the next REST since parameter. Runtime traces advancement after final failure as well as success; a cursor is not evidence of complete source synchronization.

The actual next acquisition/selection software gives these retained values behavioral authority. Loader state has no TTL in the inspected accessor. Disabling a module stops future scheduling, not retained data or past effects. These are recovery/selection adaptation paths; improved acquisition capacity is not established. Source premises and counterexamples are also in [RT-RTE-extraction-summary](runtime.md#rt-rte-extraction-summary) and [RT-RTE-record-import](runtime.md#rt-rte-record-import).

#### MEM-OBJ-contradiction-block
Label: Knowledge contradiction block

Part of: [RT-OBJ-knowledge](runtime.md#rt-obj-knowledge)

Source-native identity: Markdown block produced by `_applyMarkContradiction`. Form: natural-language conflict text, with current/new values, source/date and request for verification. Substrate: the same filesystem file as the original assertion. Lineage: model-proposed contradiction object plus supplied or model-overridden source. This part differs from ordinary appended facts by its explicit unresolved-conflict display; it is not a second store or a replacement candidate for the knowledge container. Evidence: SRC-1, `src/ai/knowledge-engine.js`; originating route [RT-RTE-knowledge-enrichment](runtime.md#rt-rte-knowledge-enrichment).

> const block = `\n\n> **Суперечність** (джерело: ${src}, ${date}):\n> Поточне значення: ${contradiction.current_value}\n> Нове значення: ${contradiction.new_value}\n> Потребує перевірки.\n`;
> --- `src/ai/knowledge-engine.js`

The code requires truthy current/new values, inserts after the named header or at file end, and leaves existing text intact. Full-file retrieval can deliver this warning to the next enrichment model, chat model or human editor. Its force there is interpretive evidence/warning, not a deterministic exclusion of either value. No special contradiction-status predicate operates in the inspected retrieval methods. Source attribution is text, not verified provenance. The requested JSON `reason` and analysis are returned in update results but are not independently serialized into this block; a model may include explanation inside content elsewhere, which is an unobserved alternative, not a universal absence of rationale.

A read exception returns silently, after which `applyUpdates` still reports applied true:

> return; // Can't mark contradiction in non-existent file
> --- `src/ai/knowledge-engine.js`

The mock test explicitly expects this no-op to be reported applied. Thus applied-count displays cannot certify durable conflict retention (SRC-1, `src/__tests__/knowledge-engine.test.js`). The operation is model admission followed by mechanical insertion, not human resolution or demonstrated criticism improving later behavior.

#### MEM-OBJ-messages
Label: Browser chat messages

Source-native identity: the chat page's ES-module `messages` array, not the request-local provider tool blocks. Form: user/assistant natural-language text, plus symbolic tool-call/usage display metadata. Substrate: browser process memory. Lineage: user input, returned model reply or rendered request/connection error; initial empty state is source-defined. Closest supplied record [RT-RTE-chat-tools](runtime.md#rt-rte-chat-tools) describes its route; [RT-OBJ-atlas-db](runtime.md#rt-obj-atlas-db) and [RT-OBJ-knowledge](runtime.md#rt-obj-knowledge) are distinct stores, not counterparts. Evidence: SRC-1, `src/ui/pages/chat.js`.

> // --- state (persists across navigation — ES module singleton) ---
> const messages = [];
> --- `src/ui/pages/chat.js`

Assistant entries retain tool logs for display, with preview truncated to 500 characters, but later API messages include only role/content. The display summary is not evidence that full prior tool payloads reach a later model. Text and even displayed errors can be replayed; no summary/compaction is introduced here. Browser reload/cross-device persistence is not established by the inspected array. This memory's automatic admission of returned replies differs from explicit user knowledge-file saving. Its later consumption is [MEM-RTE-conversation-replay](#mem-rte-conversation-replay).

### Routes

#### MEM-RTE-conversation-replay
Label: Browser conversation replay

Part of: [RT-RTE-chat-tools](runtime.md#rt-rte-chat-tools)

This is the later-request history subroute of the supplied internal chat loop, not a duplicate of its tool executor. Trigger: another user send in the same page-module lifetime. Owner/selector: browser code retains messages and filters/maps them; user supplies the next prompt and model choice; provider interprets replayed text. Progression: prior reply/error → messages array → role/content projection → POST /api/chat → handleChat/provider. Mode: open conversation, no answer oracle. Admission of assistant content is automatic after a response; the user does not separately approve each retained reply. Recovery is another send; module reload can reset the state but does not undo saved KB files. Guidance for generation is the static chat system prompt in [RT-BAP-chat-guidance](runtime.md#rt-bap-chat-guidance), not a learned policy.

- Immediate return: the endpoint's new reply/log/usage or error, then browser renders and appends text.
- Later read-back: accumulated user/assistant text enters a subsequent handleChat invocation.
- Delegated visibility: configured chat provider sees submitted history, but prior tool logs are omitted from this projection.
- Selection predicate: user/assistant role filter, projecting role and content without a targeted relevance selector or explicit length budget.
- Invalidation or expiry: page-module lifetime; no durable reload store in the inspected page; current-run tool blocks expire with the request.
- Activation or effect: replay is wired to model context; whether earlier text changes subsequent decisions is unobserved.
- Evidence limits: browser/runtime/provider execution unavailable; semantic reliability and cross-session persistence not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `src/ui/pages/chat.js`, `src/ai/chat.js`:

> const apiMsgs = messages
>       .filter(m => m.role === 'user' || m.role === 'assistant')
>       .map(m => ({ role: m.role, content: m.content }));
> --- `src/ui/pages/chat.js`

#### MEM-RTE-record-pruning
Label: Operational record pruning

Closest supplied record [RT-RTE-record-import](runtime.md#rt-rte-record-import) mentions expiry, but this route is the independently callable cleanup operation, not import admission. Trigger: POST /api/admin/prune or an API caller invoking `pruneOldRecords`. Owner: caller/config supplies retention_days; fixed JavaScript/SQL decides age/status and executes deletes. Context: current time, retention_days default 90, shipment status/synced_at and rate valid_to. Proposed change: removal of old closed shipments, their events/documents and expired rates. Admission: software predicates, not semantic model judgment or per-row human approval. A browser/API request can initiate it but caller identity is unresolved. Mode: administrative cleanup, no answer oracle. Recovery/rollback: catch and log errors; no prior-version store or cross-statement transaction in the inspected method. Retained guidance is configuration, not a generated improvement instruction.

- Immediate return: deleted counts; method may return partial counts after caught failure; HTTP handler wraps response as ok true.
- Later read-back: later data queries see remaining rows; Markdown knowledge, extract logs and checkpoint rows are not deleted by these statements.
- Delegated visibility: later MCP/REST/chat data consumers receive the changed data view; pruning itself calls no model.
- Selection predicate: delivered/cancelled shipments with synced_at older than cutoff, related events/documents by shipment ID, rates with non-null valid_to older than cutoff.
- Invalidation or expiry: physical row deletion; source-derived KB text is independently replaceable/deletable, not automatically retracted here.
- Activation or effect: source wires deletion and changed subsequent query eligibility; deployed invocation unobserved.
- Evidence limits: no execution, transaction success or historical content supplied; stale knowledge after deletion is possible, not observed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Evidence: SRC-1, `src/atlas.js`, `src/ui-server.js`:

> const evDel = this.db.prepare(`DELETE FROM tracking_events WHERE shipment_id IN (${placeholders})`).run(...oldIds);
> const docDel = this.db.prepare(`DELETE FROM documents WHERE shipment_id IN (${placeholders})`).run(...oldIds);
> const shpDel = this.db.prepare(`DELETE FROM shipments WHERE id IN (${placeholders})`).run(...oldIds);
> --- `src/atlas.js`

The source comment claims automatic startup pruning. The completed search for `pruneOldRecords` throughout `src/` and `bin/` identified only the REST call besides the method. Startup activation is not inferred from the comment.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-knowledge](runtime.md#rt-obj-knowledge)

Lineage and curation: files can originate from human/direct API content, model chat findings, model transformation of extracted entities or raw text, and scheduled transformation of extraction metadata. Existing deployment-file origins are unknown; that does not obscure subsequent source-wired transformations. Source trust is no stronger than the supplied/model source text: engine uses `update.source ?? source`, while direct writers need not attribute at all. Storage is the filesystem; natural-language Markdown is interpreted by models/humans, with paths as symbolic addresses. Engine actions add source/date text; they do not attach a verified record/document lineage key. Evidence: SRC-1, `src/ai/knowledge-engine.js`, `src/atlas.js`; overwriting passage in [RT-CLM-additive-knowledge](runtime.md#rt-clm-additive-knowledge).

Admission varies independently of physical I/O: enrichment applies model proposals; chat admits model tool saves; browser save/delete is an explicit human content decision; generic API caller authorship remains unresolved. The editor's explicit adoption passage is:

> await api.post('/api/kb/file', { path: currentFile, content: cachedContent });
> --- `src/ui/pages/knowledge.js`

Later consumers are enrichment prompts, requested chat file reads and human file views. A whole-file read delivers original assertions together with conflict blocks/attribution; no deterministic trust precedence or expiry is added at this boundary. Deletion removes the file from future index/read operations, not from already delivered model messages or replayed assistant text. No rollback is wired in the store methods. Actual revisions/content quality and reasons embedded by a model are unavailable.

#### On [RT-RTE-knowledge-enrichment](runtime.md#rt-rte-knowledge-enrichment)

Read-back selection is automatic within an explicitly started enrichment route, not an independently unsolicited chat push. Inputs: the first mapped entity topic; up to twenty keywords from short string identifier/name/code/location fields in the first twenty records per group; or capitalized phrases/codes extracted from raw text. Selection scans the Markdown index, reads every readable candidate for keyword matching, scores topic-path match three and each content keyword one, then sorts positive matches. This is lexical full-file selection, not embeddings or section retrieval. Default five files/30000 characters is not a hard budget: first oversized file is admitted and a later oversized file ends selection rather than allowing smaller lower-ranked files. Only selected contents enter the provider prompt. Evidence: SRC-1, `src/ai/knowledge-engine.js`:

> if (totalChars + item.content.length > maxChars && result.length > 0) break;
> --- `src/ai/knowledge-engine.js`

Extraction-derived new information serializes only the first ten records per entity group, whereas selector keywords may consider twenty. Database failures do not remove those in-memory entities from the enrichment input. Thus KB may be derived from extracted records not durably admitted to the DB. This is curation of new source material, not necessarily trace learning from agent outcomes. Reasons/analysis remain immediate result fields unless independently put in content. Subsequent provider retries for malformed JSON see prior response plus format hint, not original newInfo/KB context. The write gate validates only action/path envelope, known dispatch and action-specific errors; add-only/deduplication/same-language/source-truth remain model guidance, not semantic admission checks. Supplied [RT-CLM-additive-knowledge](runtime.md#rt-clm-additive-knowledge) retains the counterexample.

The `append_section` action searches a header and inserts before the next same/higher-level header or at file end; a failed read creates a new file with section/content. `create_file` can overwrite. `mark_contradiction` retains a warning part, [MEM-OBJ-contradiction-block](#mem-obj-contradiction-block). No content-level human approver separates provider output from filesystem write. Retained material has interpretive authority at future models, not guaranteed answer control or improved capacity.

#### On [RT-RTE-chat-tools](runtime.md#rt-rte-chat-tools)

The automatic context selector supplies current counts and every Markdown path in the system prompt, with no explicit index budget. Content delivery requires model-selected `read_knowledge` with a literal path; `list_knowledge` requests a folder tree, not relevance scoring. Full read output is serialized as provider-specific tool-result messages. Current-run results are not a server-retained episode record; the browser replay projects them out, while a model-requested save can separately retain derived prose. Evidence: SRC-1, `src/ai/chat.js`, `src/ui/pages/chat.js`; executor passages in the supplied record.

> const resultStr = JSON.stringify(result, null, 2);
> toolCallLog.push({ name: tc.name, args: tc.input, result: resultStr });
> toolResults.push({ type: 'tool_result', tool_use_id: tc.id, content: resultStr });
> --- `src/ai/chat.js`

Five tool-enabled iterations limits rounds, not number of files, bytes, tool effects or retained-message length. No compaction/summary is implemented in this consumer. Provider-internal context management remains opaque. Save content is model-authored and mechanically adopted, not human approved, and replaces full files independently of engine rules. The delivered file is knowledge/evidence interpreted by the provider; an instruction inside it is not promoted by a dedicated trusted-source parser. Whether such text controls behavior is unobserved.

#### On [RT-RTE-extraction-summary](runtime.md#rt-rte-extraction-summary)

Trace-fed chain: pipeline outcome → [MEM-OBJ-extract-log](#mem-obj-extract-log) → oldest eligible log rows → metadata string/topic heuristic → selected KB plus metadata to provider → automatic file updates → later engine/chat file consumers. Original trace origin is file-extraction processing metadata, not task success/failure of the chat agent and not original logistics entities. The engine might produce no update or produce substantive prose; actual model outputs are unavailable. The chain is wired but neither accurate fact reconstruction nor improved future capacity follows. The retained cursor is a separate selection artifact, [MEM-OBJ-progress-state](#mem-obj-progress-state), not the derived semantic result. Evidence: SRC-1, `src/modules/knowledge-enricher/index.js`, `src/ai/knowledge-engine.js`; the supplied record retains the exact metadata string.

## Write side

Acquisition admits source records through two major gates: minimum-field software validation after mapping for non-AI imports, or model extraction followed by those checks. User upload initiates the workflow; it does not approve each fact. Unknown types/invalid rows are skipped, with console errors, not retained rejected candidates for later model criticism. Database payloads replace matching IDs; extracted text/model reasoning are not a durable event archive in this pipeline. Text input is limited to the first 40000 characters by default (SRC-1, `src/ai/extract.js`; [RT-RTE-file-extraction](runtime.md#rt-rte-file-extraction)).

Knowledge maintenance then has alternative inputs: bounded extraction entities; caller-supplied raw text; or extraction-log metadata. They are not interchangeable. Proposed actions are automatically admitted after mechanical checks; per-update failure does not revert earlier changes. Analysis/reason returned to the initiating caller is distinct from lasting content/attribution/conflict text. Existing files provide model comparison context, but no supplied outcome establishes reliably deduplicated, truthful or explanatory updates. See the enrichment annotations and [MEM-OBJ-contradiction-block](#mem-obj-contradiction-block).

Progress markers and failure logs can suppress later retry rather than improve recovery: any logged hash dedups, module markers add their own filters, and the scheduled cursor can advance past a returned failure. File-watch optional archive retains the source physically elsewhere; Drive temporary-download deletion does not retract DB or KB outputs. Native module/config admission is separate from data curation and remains bounded by the supplied [RT-RTE-module-lifecycle](runtime.md#rt-rte-module-lifecycle) and [RT-RTE-config-reload](runtime.md#rt-rte-config-reload). External plugin behavior and provider-private persistence cannot be enumerated from these sources.

Human editor save/delete admits human content decisions in the browser route; generic REST and chat saves are alternative non-human-approval paths. KB deletion removes future discovery; replacing a file can remove earlier knowledge and warnings. Record cleanup is separate and does not cascade into derived Markdown, logs, checkpoints or browser replies. The rejection/withdrawal paths therefore do not define a coherent source-to-all-derivatives retraction protocol (SRC-1, `src/atlas.js`, `src/ui-server.js`, `src/ui/pages/knowledge.js`; [MEM-RTE-record-pruning](#mem-rte-record-pruning)).

Mock tests check selection, action insertion, unknown-action errors, partial batches and conflict no-op behavior. They use in-memory Atlas and fake completions. They neither run a deployed quality evaluator nor gate live engine adoption. For example:

> async complete(system, user) {
>       calls.push({ system, user });
>       return { text: responseText, usage: { input_tokens: 10, output_tokens: 5 } };
>     },
> --- `src/__tests__/knowledge-engine.test.js`

No target tests were run. The shipped model-validator designs mentioned in boundary cannot be promoted into semantic evaluation of retained KB content.

## Read-back

- **Enrichment:** an incoming text/extraction invocation triggers a software selector; selected whole files are pushed into its provider request. Budget and keyword losses are recorded in the annotation. A later update consumer receives current files, including earlier additions and warnings; semantic reliance remains unobserved.
- **Chat:** every invocation receives filenames automatically; full knowledge is delivered only on model file requests. Data queries return filtered symbolic payloads. These mechanisms have different selectors and limits and must not be collapsed into one retrieval quality claim. [RT-RTE-chat-tools](runtime.md#rt-rte-chat-tools), [MEM-OBJ-record-payloads](#mem-obj-record-payloads).
- **Editor:** human path selection loads full content through GET, then explicit save/delete can adopt replacement/withdrawal. This is a shipped later consumer, not hypothetical library read-back (SRC-1, `src/ui/pages/knowledge.js`, `src/ui-server.js`; [RT-RTE-knowledge-edit](runtime.md#rt-rte-knowledge-edit)).
- **Conversation:** replayed reply text is retained across later requests within browser-module lifetime; prior tool evidence is not replayed. [MEM-RTE-conversation-replay](#mem-rte-conversation-replay).
- **Acquisition/maintenance:** hashes, modifiedTime and cursors are read by fixed selectors on subsequent runs. This is behavioral authority through symbolic progress data, not a model prompt. [MEM-OBJ-progress-state](#mem-obj-progress-state).
- **External MCP clients:** requested operational rows return to a documented external agent role, but its further memory/action loop is excluded. No query-produced retained adaptation is wired in the callbacks accounted by [RT-RTE-mcp-query](runtime.md#rt-rte-mcp-query).

The inspected code has no alternate conversation-summary checkpoint in these chat paths. The schema-description cache is static source-derived setup, not experience read-back (SRC-1, `src/ai/extract.js`). Provider caching, truncation and latent reasoning remain uninspected, so this source cannot exclude opaque provider-side alternatives.

## Integration issues

1. **Applied does not imply written.** [MEM-OBJ-contradiction-block](#mem-obj-contradiction-block) qualifies [RT-RTE-knowledge-enrichment](runtime.md#rt-rte-knowledge-enrichment) and [RT-RTE-extraction-summary](runtime.md#rt-rte-extraction-summary): missing/unreadable conflict targets return silently yet appear applied. Preserve the distinction between returned result flags, durable artifacts and actual consumer delivery. Evidence: SRC-1, `src/ai/knowledge-engine.js`, `src/__tests__/knowledge-engine.test.js`.
2. **Database lineage is not the engine input boundary.** Enrichment reads the extraction result even when callbacks fail or silently do nothing, and includes only ten records/group. [MEM-OBJ-record-payloads](#mem-obj-record-payloads), [RT-RTE-file-extraction](runtime.md#rt-rte-file-extraction) and [RT-RTE-knowledge-enrichment](runtime.md#rt-rte-knowledge-enrichment) must not imply that KB facts are all successfully persisted DB rows. Evidence: SRC-1, `src/ai/extract-pipeline.js`, `src/ai/knowledge-engine.js`.
3. **Startup pruning is a source-comment claim, not established caller wiring.** [MEM-RTE-record-pruning](#mem-rte-record-pruning) separates the known admin caller from automatic startup. This qualifies any reading of the source's retention comment, not a correction to runtime's explicit route record. A complete bounded caller search is recorded below.
4. **No duplicate declarations proposed.** The three DB parts and contradiction part explicitly retain their containers. [MEM-OBJ-messages](#mem-obj-messages) is a browser store distinct from supplied DB/KB objects. The replay subroute is part of the supplied chat route; pruning is an independent cleanup route mentioned, but not declared, by runtime. Annotations enrich existing referents rather than create parallel records.
5. **Unresolved included parts and consequences:** operational KB initialization/history and actual model outputs are unavailable; no judgment of content truth, retained explanation quality or exercised reliance is possible. Provider-internal retention/compaction and precise model version are opaque; [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client) bounds model mutability rather than proving absence of external updates. External plugins may retain additional state; their unavailable implementations prevent universal storage or withdrawal claims. Config reload can leave old module registry references, per [RT-RTE-config-reload](runtime.md#rt-rte-config-reload), so universal immediate model-routing propagation is not established. These are limits, not hidden absent mechanisms.

## Limitations and checks

Evidence is implementation and doctrine/design only; no observed activation or benefit. Searches were bounded to frozen SRC-1 paths, not prior analyses. The complete source pin was rechecked against HEAD and a clean status. Method identity is the supplied memory type, job instruction, worker rules and shared record contract; no other worker was launched and no source was executed or modified.

Caller check: `rg -n 'pruneOldRecords' src bin` at the frozen checkout distinguishes the known REST caller from the method/comment. Conversation alternatives check: `rg -n 'compact|embedding|vector|localStorage|sessionStorage' src` found the schema-prompt comment, not an implemented browser durable store or chat compactor; direct chat/page reads establish the local limitation, not a whole-system provider absence. Registered tools and source write/read/delete operations were searched in `src/index.js`, `src/ui-server.js`, `src/atlas.js` and the shipped drivers. A broad name search alone is not relied upon as exhaustive proof of absent memory.

Validation: completed with the invocation's deterministic validate-output command; its passing result establishes form and quote occurrence, not semantic acceptance or successful target operation.
