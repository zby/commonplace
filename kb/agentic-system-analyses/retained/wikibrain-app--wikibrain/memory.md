---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "WikiBrain memory: PostgreSQL-backed source, wiki and rule pages, conversation reuse, derived navigation and bounded recovery."
run-id: AAS-2026-11-08-wikibrain-f815b0976cda-01
source-identity: https://github.com/wikibrain-app/wikibrain
reviewed-boundary: "32cc135877c8d7cd7be997ce57f25bb83128d891"
---

# WikiBrain memory report

## Boundary and evidence

This report covers the shipped knowledge loop, including import and scheduled Zotero admission, automatic compilation and lint, chat and answer filing, direct client/editor writes, template rule reuse, note history, archive/reset, and human-facing read surfaces. The functional boundary and source register are [boundary](boundary.md#source-register). All source findings below use SRC-1 at the registered commit. These are implementation and doctrine/design findings, not observed executions. The frozen checkout's HEAD was rechecked as `32cc135877c8d7cd7be997ce57f25bb83128d891`.

The runtime is provisional input, not an inspection ceiling. Direct reads covered `src/notes.ts`, `src/chat.ts`, `src/ingest.ts`, provider loops in `src/ai/providers.ts`, `src/mcp.ts`, `src/templates.ts`, `src/lint.ts`, `src/retention.ts`, `src/import-api.ts`, source rendering/saving in `src/import.ts`, sync in `src/zotero.ts`, `src/web-api.ts`, `src/assets.ts`, `src/shares.ts`, `src/export.ts`, `src/workspaces.ts`, relevant `src/api.ts` dispatch, `src/server.ts`, `package.json`, browser Workspace reload/edit/history operations and ChatPanel history/filing/discussion operations, and the general English schema instructions. Searches checked the registered tools, package dispatch and alternative REST operations. The package starts the server, not a separate memory-agent CLI; the import API explicitly accommodates external hooks/scripts, but their private trigger logic is not shipped in that API. [SRC-1: `package.json`, `src/server.ts`, `src/import-api.ts`, `src/mcp.ts`]

Remote provider state, external client context management and private hosted operations remain outside inspectable evidence. Conversion internals and renderer correctness were not exhaustively audited; source Markdown is converted capture, not necessarily an original byte-for-byte document. Scenario/translated template contents beyond the general English rules remain uninspected; their loader/update path is inspected. These limits prevent claims about capture fidelity, every template's guidance, multimodal interpretation and external-client compliance, not the local persistence/reload wiring.

| Entry point or operation | Directly inspected source (SRC-1) | Covering records / local limit |
|---|---|---|
| URL/text/upload/bibliography; external hook-compatible import | `src/import-api.ts`, `src/import.ts` saving/rendering | [MEM-RTE-source-admission](#mem-rte-source-admission), [MEM-OBJ-raw](#mem-obj-raw); extraction internals not fully inspected |
| Manual/hourly Zotero sync | `src/zotero.ts`, `src/server.ts`, `src/api.ts` | [MEM-RTE-source-admission](#mem-rte-source-admission); remote library contents unobserved |
| Automatic ingest and direct MCP/REST writes | `src/ingest.ts`, `src/mcp.ts`, `src/web-api.ts`, `src/notes.ts` | [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), [RT-RTE-client-tools](runtime.md#rt-rte-client-tools), [MEM-OBJ-wiki](#mem-obj-wiki) |
| Schema/rules reload and alternative schema admission | `src/notes.ts`, `src/ingest.ts`, `src/mcp.ts` | [RT-BAP-schema-instructions](runtime.md#rt-bap-schema-instructions), [RT-RTE-schema-spelling](runtime.md#rt-rte-schema-spelling), [MEM-OBJ-schema](#mem-obj-schema) |
| Search/list/path read, index-first guidance | `src/notes.ts`, `src/chat.ts`, general English rules | [MEM-RTE-note-retrieval](#mem-rte-note-retrieval), [MEM-OBJ-links-tags](#mem-obj-links-tags) |
| Structural checks, semantic repair/report | `src/lint.ts`, `src/ingest.ts` | [RT-RTE-lint-job](runtime.md#rt-rte-lint-job), [MEM-OBJ-wiki](#mem-obj-wiki); model fulfillment unobserved |
| Session history, answer filing, failed-turn fallback | `src/chat.ts`, `web/src/components/ChatPanel.tsx` | [RT-RTE-chat-session](runtime.md#rt-rte-chat-session), [MEM-OBJ-chat-sessions](#mem-obj-chat-sessions) |
| Discussion transcript supplied to compilation | `web/src/components/ChatPanel.tsx`, `src/ingest.ts` | [MEM-RTE-discussion-guidance](#mem-rte-discussion-guidance) |
| Template apply/merge/replace, custom schema snapshot/edit/apply/delete | `src/templates.ts`, `src/api.ts` | [RT-RTE-rule-update](runtime.md#rt-rte-rule-update), [MEM-OBJ-template-state](#mem-obj-template-state) |
| Working window, model alternatives, diagnostic checkpoints | `src/ai/providers.ts`, `src/ingest.ts`, `src/chat.ts` | [RT-CMP-provider-models](runtime.md#rt-cmp-provider-models), [RT-OBJ-ingest-jobs](runtime.md#rt-obj-ingest-jobs), annotations below; provider internals uninspected |
| Versions/rollback, archive/undo, soft delete, purge, reset | `src/notes.ts`, `src/retention.ts`, `src/web-api.ts`, `src/workspaces.ts`, `web/src/pages/Workspace.tsx` | [MEM-RTE-state-withdrawal](#mem-rte-state-withdrawal), [MEM-OBJ-note-versions](#mem-obj-note-versions); physical workspace deletion cascades not independently audited |
| Browser tree, author, properties, backlinks, graph | `src/web-api.ts`, `src/notes.ts`, `web/src/pages/Workspace.tsx` | [MEM-RTE-note-retrieval](#mem-rte-note-retrieval); frontend rendering internals not fully inspected |
| Attachment admission/read/delete; share/revoke and export | `src/assets.ts`, `src/shares.ts`, `src/export.ts`, bounded API/app dispatch searches | [MEM-OBJ-assets](#mem-obj-assets), [MEM-RTE-human-delivery](#mem-rte-human-delivery); no evidence binary assets enter built-in model inputs |

## Core ideas

1. The persistent unit is a workspace-bound Markdown page, not a vector or opaque memory payload. Raw source text, compiled wiki prose and rule prose share storage functions but have different update permissions and downstream authority. Navigation tables are derived symbolic state, not independent knowledge. See [MEM-OBJ-raw](#mem-obj-raw), [MEM-OBJ-wiki](#mem-obj-wiki), [MEM-OBJ-schema](#mem-obj-schema), [MEM-OBJ-links-tags](#mem-obj-links-tags).
2. Retrieval is requested tool delivery. Models are told to load rules and index, then choose queries and full-page reads. get_instructions does add a code-selected pending-source prelude, but this occurs inside a requested tool response, not an unsolicited push into an invocation. There is no global token-budget selector in the inspected local loops. See [MEM-RTE-note-retrieval](#mem-rte-note-retrieval) and [RT-BAP-schema-instructions](runtime.md#rt-bap-schema-instructions).
3. Conversation reuse has several distinct forms: saved user/assistant prose becomes next-turn history; an explicit filing action turns an answer into wiki content; a separate browser action submits a bounded discussion transcript as compilation guidance. These do not retain the full tool episode or certify its conclusions. See [MEM-OBJ-chat-sessions](#mem-obj-chat-sessions), [RT-RTE-chat-session](runtime.md#rt-rte-chat-session), [MEM-RTE-discussion-guidance](#mem-rte-discussion-guidance).
4. Maintenance changes durable content without a mandatory human acceptance of each generated page. Lint reports and log entries are requested records of reasons/actions, not enforced evidence packages or proven improvements. Snapshot recovery is per page and time-limited; hiding or archiving material is not deleting every route to its content. See [RT-RTE-lint-job](runtime.md#rt-rte-lint-job), [MEM-RTE-state-withdrawal](#mem-rte-state-withdrawal).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-raw
Label: raw source pages

Source-native identity: live `raw/` notes, including archived sources. Substrate: PostgreSQL `notes.content_md`; form: primarily natural-language source/body and bibliographic text, with symbolic frontmatter/path/version fields. Lineage: converted URL/upload/text or bibliographic entry, Zotero metadata/optional PDF text, or direct create_note content; raw is a logical layer, not proof of external or immutable-original provenance. Distinct from the runtime job row [RT-OBJ-ingest-jobs](runtime.md#rt-obj-ingest-jobs): this is content consumed by compilation, not diagnostic events.

Admission follows [MEM-RTE-source-admission](#mem-rte-source-admission) or [RT-RTE-client-tools](runtime.md#rt-rte-client-tools). updateNote rejects normalized raw paths. Individual delete rejects raw but archive changes path while retaining identity and content. Consumers: ingest/lint/chat can request full text; get_instructions/pending selectors use path/title/link metadata. Built-in reads label raw content untrusted; MCP reads do not add that label. Content influences model synthesis as source data, not an enforced instruction source. [SRC-1: `src/notes.ts`, `src/import.ts`, `src/zotero.ts`, `src/ingest.ts`, `src/mcp.ts`]

> if (layerOf(path) === 'raw') throw new NoteError('FORBIDDEN', { 'zh-TW': `raw/ 為唯讀來源層，不可更新：${path}`, en: `raw/ is the read-only source layer and cannot be updated: ${path}` });
> --- `src/notes.ts`

#### MEM-OBJ-wiki
Label: compiled wiki pages

Source-native identity: `wiki/` notes, including summaries, entity/concept pages, `wiki/index.md`, `wiki/log.md`, query pages and lint reports. Substrate: PostgreSQL Markdown; form: natural-language knowledge, catalog descriptions and reports, with symbolic paths/frontmatter and parsed links. Lineage: templates seed pages; automatic model compilation/chat/lint, human edits and external-client content can subsequently create or replace them. No closest supplied content-object counterpart; [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), [RT-RTE-chat-session](runtime.md#rt-rte-chat-session) and [RT-RTE-lint-job](runtime.md#rt-rte-lint-job) operate on this shared substrate.

Material consumption differs: summaries/concepts/queries supply knowledge to later requested reads; index is a model-interpreted catalog used for subsequent page selection; log/lint pages retain narrated history/diagnosis and can be read, but there is no compulsory later model read of those reasons. The index and append-only log discipline are guidance rather than field-level write enforcement. A full Markdown update can alter or omit earlier reasons; version snapshots retain previous text only within their retention limits. Source citations/conflict markers are requested, not validated truth or guaranteed lineage completeness. [SRC-1: `src/notes.ts`, `src/chat.ts`, `src/lint.ts`, `templates/general/en/schema/instructions.md`]

> 6. When a source contradicts an existing page, mark "⚠ conflict" on both and list both sides; never pick silently.
> --- `templates/general/en/schema/instructions.md`

> - **wiki/index.md** is the catalog: one line per page with a link and a one-line summary, grouped by category. Update it on every ingest; read it first when answering a question.
> --- `templates/general/en/schema/instructions.md`

#### MEM-OBJ-schema
Label: schema rule pages

Source-native identity: live `schema/` notes, natural-language compilation instructions encoded as Markdown, with symbolic path/version controls. Storage: PostgreSQL notes, not only shipped template files. Lineage: built-in/custom templates or authorized direct edits; the alternate automatic spelling path is supported by [RT-RTE-schema-spelling](runtime.md#rt-rte-schema-spelling). Distinct from [RT-BAP-schema-instructions](runtime.md#rt-bap-schema-instructions), which is the authority path consuming this object. Retained rules may contain rationale but no enforced schema requires it.

The actual consumer is the model receiving a requested get_instructions response, or an external client requesting it. This is behavioral guidance through interpretation, not a code-enforced invariant. Concatenation includes all live schema pages ordered by path, without a token budget or semantic ranking. Templates and edited rules persist across tasks until changed/deleted/reset. [SRC-1: `src/notes.ts`, `src/templates.ts`, `src/ingest.ts`, `src/mcp.ts`]

> // All schema/ pages concatenated in path order; effectively the knowledge base's CLAUDE.md.
> --- `src/notes.ts`

#### MEM-OBJ-links-tags
Label: derived links and tags

Source-native identity: `links`, `tags`, plus parsed note title and basename used for navigation. Storage: PostgreSQL rows; form: symbolic strings, IDs and relations consumed by SQL predicates. Lineage: writeDerived parses Markdown, resolves targets and replaces prior outgoing links/tags in the note transaction. It also repoints dangling links when a matching note becomes available. Distinct from [RT-OBJ-ingest-jobs](runtime.md#rt-obj-ingest-jobs), which stores tool events, and from the prose catalog [MEM-OBJ-wiki](#mem-obj-wiki).

Consumers include folder/tag search, backlinks, graph, property tables, pending-source computation and structural lint. A raw source ceases to be pending when a live wiki page links to its note ID, not when semantic compilation quality is verified. Link resolution prefers full path, extension/layer variants, basename, then title; lexical ambiguity can determine the selected target. Parsing strips code spans/fences and recognizes wiki links and pandoc citations. These are navigation/access metadata, not evidence that the referenced claim is true. [SRC-1: `src/notes.ts`, `src/lint.ts`]

> await c.query('DELETE FROM tags WHERE note_id = $1', [noteId]);
> --- `src/notes.ts`

> WHERE l.to_note_id = n.id AND f.deleted_at IS NULL AND f.path LIKE 'wiki/%')
> --- `src/notes.ts`

#### MEM-OBJ-note-versions
Label: note version snapshots

Source-native identity: `note_versions`, containing full prior/current title/content, version, author and timestamps. Substrate: PostgreSQL; form: natural-language snapshot content plus symbolic recovery/attribution fields. Lineage: each successful create/update writes a snapshot with links/tags in the same transaction. This is a distinct content checkpoint, not [RT-OBJ-ingest-jobs](runtime.md#rt-obj-ingest-jobs)' truncated operational log. The author string records actor kind/name; it is not semantic approval or original source authorship.

Consumers: REST/browser version list, historical view/diff and explicit rollback. Rollback feeds snapshot content to updateNote, so it is a new current version and rebuilds derived metadata; it does not rewind an entire job. A raw snapshot cannot be restored through updateNote because normalized raw updates are forbidden. Purge excludes current version and removes old non-current versions under plan-dependent windows (7 days free, 90 pro/active trial in the shipped implementation). [SRC-1: `src/notes.ts`, `src/retention.ts`, `src/web-api.ts`, `web/src/pages/Workspace.tsx`]

> return updateNote(ws, n.path, rows[0].content_md, ifVersion, actor);
> --- `src/notes.ts`

> AND v.version <> n.version
> --- `src/retention.ts`

#### MEM-OBJ-chat-sessions
Label: retained conversation messages

Source-native identity: `chat_sessions.messages`; PostgreSQL JSON containing natural-language user/assistant content and symbolic time/job/usage/tool-summary/filedTo fields. Distinct from the job log [RT-OBJ-ingest-jobs](runtime.md#rt-obj-ingest-jobs); it survives as conversation rather than full tool trace. Closest supplied route is [RT-RTE-chat-session](runtime.md#rt-rte-chat-session), not an existing object declaration.

Lineage: admitted user text, runner finalText or a fallback based on writtenPaths, and failure replies. Next-turn model history maps every saved message to role/content only, dropping old tool summaries, usage and execution bodies. The stored message tools list is a readable diagnostic summary derived from truncated job events, not the model's prior tool state. The browser reads fuller message metadata. Filing retains selected assistant text with question and query frontmatter as a new wiki page. Failed replies are stored assistant messages too; sendMessage's history map does not filter them. A deleted session loses this history route; filed notes remain separate. [SRC-1: `src/chat.ts`, `web/src/components/ChatPanel.tsx`]

> const history = session.messages.map(m => ({ role: m.role, content: m.content }));
> --- `src/chat.ts`

#### MEM-OBJ-template-state
Label: delivered rule comparison bases

Source-native identity: `template_applied` delivered hashes/content/version/language. Storage: PostgreSQL JSON/text fields; form: symbolic provenance/comparison metadata and natural-language delivered rule text. Consumer: pendingRuleUpdates uses delivered bases for deterministic future merge/admission. Closest supplied referent [RT-RTE-rule-update](runtime.md#rt-rte-rule-update) is the transformation route, not this store. Custom editable bundles have a different admission/read consumer and are separately declared in [MEM-OBJ-user-templates](#mem-obj-user-templates).

Built-in application records delivered schema bytes. pendingRuleUpdates compares recorded version/hash, current text and newly shipped text; safe conflict retention and overwrite behavior are in the runtime route. A base retained for comparison is not automatically an instruction until content is admitted into live schema. This comparison state is code-authored, not a human approval or quality judgment. [SRC-1: `src/templates.ts`]

> contents[path] = text;          // the base for a later three-way merge
> --- `src/templates.ts`

#### MEM-OBJ-user-templates
Label: editable custom template bundles

Source-native identity: `user_templates` file bundles, name/description, base ID and starter prompt. Storage: PostgreSQL JSON/text fields; form: symbolic file paths/IDs and natural-language rule/page/prompt content. Lineage: direct caller content, duplication of built-ins, or snapshot of live workspace rules. Distinct from [MEM-OBJ-template-state](#mem-obj-template-state)'s delivered comparison bases; closest supplied route [RT-RTE-rule-update](runtime.md#rt-rte-rule-update) already names custom apply but does not declare the bundle object.

Custom snapshot copies current live schema and index, but substitutes a fresh empty log header for historical log contents. API callers can subsequently edit/delete bundles independently of live notes. Custom apply adds absent paths and skips conflicts, returning its starter prompt; it is not an automatic workspace-wide replacement or an observed model invocation. The content gains model authority only if applied as live schema and retrieved, or if a caller subsequently uses the returned prompt. Direct caller identity does not establish human per-content control. No quality evaluator approves rules. [SRC-1: `src/templates.ts`, `src/api.ts`]

> const files = rows.map(r => ({ path: r.path, content: r.path === 'wiki/log.md' ? '# 紀錄（log）\n\n依時間順序、只追加不修改的紀錄。\n' : r.content_md }));
> --- `src/templates.ts`

#### MEM-OBJ-assets
Label: image attachment payloads

Source-native identity: assets with ID, filename, MIME, bytes and optional source URL. Substrate: PostgreSQL bytea for payload and columns for metadata. Form: encoded image bytes (SVG may include symbolic markup/text), not distributed model parameters; metadata is symbolic. They are not natural-language note bodies or a vector store. Lineage: upload or downloaded Markdown image; MIME sniffing, size checks and approximate SVG sanitization precede storage. Source URL is provenance metadata, not an authenticity proof. Distinct from supplied runtime objects; the note body holds links rather than image data.

Consumers: authenticated browser asset reads, shared-note embedded-image reads, and ZIP export. The built-in tools deliver Markdown link text and snippets, not these binary payloads; the inspected provider loops contain no asset/image fetch-to-message conversion. Thus local storage does not establish the comment's claim that the LLM can see images later. Remote client multimodal reads remain uninspected. Delete removes the asset, separately from page history. [SRC-1: `src/assets.ts`, `src/import-api.ts`, `src/shares.ts`, `src/export.ts`, `src/ai/providers.ts`, `src/mcp.ts`]

> Stored as Postgres bytea, isolated per workspace, referenced from notes as /api/assets/<id>; rewritten to raw/assets/<filename> on export. */
> --- `src/assets.ts`

### Routes

#### MEM-RTE-source-admission
Label: source capture admission

Endpoints/progression: session or write-scoped bearer import → text/URL/file/bibliography conversion → optional image localization → rendered source → capacity check/createNote → raw page; alternatively configured Zotero manual/hourly sync → metadata/optional PDF extraction → saveSource. Owners: caller supplies inputs/configuration, code chooses path and performs admission. No counterpart after comparison with [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job): that route begins with import-backed content but its central admission is a separate model compilation job, not this scheduled/manual capture mechanism. [SRC-1: `src/import-api.ts`, `src/import.ts`, `src/zotero.ts`, `src/server.ts`]

- Immediate return: created path/meta and an ingest prompt, or sync added/skipped/error lists; import does not itself run the compilation agent.
- Later read-back: raw pages reach pending lists and model-requested full reads; Zotero library version and stored keys influence later sync selection.
- Delegated visibility: inapplicable — conversion/sync is not a child-model invocation.
- Selection predicate: requested URL/text/file; bibliography skips existing citation_key; Zotero filters item types/children and skips already stored zotero_key, with a per-round item cap.
- Invalidation or expiry: raw update refusal preserves imported content; modified Zotero items are skipped rather than replacing prior raw; archive/reset semantics are separate.
- Activation or effect: admitted capture changes later available source text and pending state; fidelity and use in actual synthesis are unobserved.
- Evidence limits: converter internals not exhaustively inspected; no remote library, upload or successful sync trace supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission control: authorization, format/conversion, size/capacity and note path/create checks can reject; physical createNote is software I/O, not a human approval step. Manual source choice supplies content; scheduled Zotero admission does not wait for per-item human review. Original authors can be external, user, or mixed; the actor label alone does not settle authorship. No expected-answer oracle or quality-driven selection experiment. Recovery: per-item sync errors retained in result, repeat sync skips seen keys, truncated rounds retain old library version; no all-capture rollback. [SRC-1: `src/import-api.ts`, `src/zotero.ts`, `src/import.ts`]

> if (seen.has(it.key)) { result.skipped++; continue; } // v1: modified items are not overwritten (raw/ is read-only), just counted as skipped
> --- `src/zotero.ts`

#### MEM-RTE-note-retrieval
Label: requested workspace retrieval

Endpoints/progression: built-in model/MCP request or browser action → workspace-bound getInstructions/searchNotes/readNote/listFolder or web projections → selected text/metadata → model or human. Owners: model/client selects tool and inputs; SQL/code chooses matching content. This elaborates read operations within [RT-RTE-client-tools](runtime.md#rt-rte-client-tools) and [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), but is not a replacement for either's write/job referent. It spans several supplied routes rather than being part of exactly one. [SRC-1: `src/notes.ts`, `src/mcp.ts`, `src/ingest.ts`, `src/web-api.ts`, `web/src/pages/Workspace.tsx`]

- Immediate return: instructions text, bounded search snippets and versions, full Markdown path read, folder summaries, or browser tree/properties/backlinks/graph/version projections.
- Later read-back: current live pages accumulated through earlier work reach subsequent tool/model invocations; this is actual wired consumer delivery, not merely a hypothetical storage API.
- Delegated visibility: built-in model receives its requested result; external client's forwarding/delegation is uninspected.
- Selection predicate: exact normalized workspace/path for full reads; up to eight lexical terms ANDed across title/body, optional tag/folder, newest-first and caller limit for search; all live schema for instructions, plus non-archived pending raw by missing live wiki backlink.
- Invalidation or expiry: deleted notes omitted from ordinary queries; archive removes pending inclusion, not exact read/search access; successful updates change next read; no cache TTL on the inspected note read path.
- Activation or effect: material is delivered as model-visible text or human-readable projections; interpretation/compliance and better answers unobserved.
- Evidence limits: no retrieval trace or benchmark; lexical matching does not establish semantic recall; graph/link membership does not establish full-source reading or adequate compilation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Budget and direction: search snippets are 160-character slices around earliest matching body term, dropping frontmatter for snippet display although matching includes it. MCP permits 1–50 results/default 10; built-in executor caps at 50/default 10. read_note returns full content up to the 1 MB page storage bound. get_instructions returns all schema plus all selected pending titles/paths, without an aggregate token limit. The pending prelude is automatic selection inside a requested response; no inspected server push preloads it before a model decision. Catalog-first is a prompt policy, not compulsory retrieval. [SRC-1: `src/notes.ts`, `src/mcp.ts`, `src/ingest.ts`, `src/chat.ts`]

> return rows.map(r => ({ path: r.path, title: r.title, version: r.version, snippet: snippet(r.content_md, terms) }));
> --- `src/notes.ts`

> const list = pending.map(p => `- ${p.path}（${safeTitle(p.title)}）`).join('\n');
> --- `src/notes.ts`

#### MEM-RTE-discussion-guidance
Label: discussion transcript to compilation

Endpoints/progression: browser opens/displays saved session → identifies pending raw path in first user message or draft → user invokes ingest per discussion → filters failed messages and renders role/content transcript → last 12,000 characters passed through onIngestFromChat → compilation guidance → ingest user prompt → model writes ordinary wiki. Distinct from [RT-RTE-chat-session](runtime.md#rt-rte-chat-session)'s next-turn history and answer filing; its destination is the compilation task, not a query page. [SRC-1: `web/src/components/ChatPanel.tsx`, `web/src/pages/Workspace.tsx`, `src/ingest.ts`]

- Immediate return: browser initiates ingest for the discussed pending source; server returns compilation job.
- Later read-back: accumulated discussion text reaches a new compilation invocation; resulting wiki is later readable through [MEM-RTE-note-retrieval](#mem-rte-note-retrieval).
- Delegated visibility: compiler receives role-labeled prose as user-task guidance, not the chat tool trace, usage or binary attachments.
- Selection predicate: first-user/draft raw path must remain pending; transcript excludes failed messages, keeps role/content and its final 12,000 characters; server trims guidance to 12,000 characters.
- Invalidation or expiry: browser offer depends on current pending set; no subsequent expiry of admitted page text beyond normal note changes.
- Activation or effect: guidance is appended under a request to follow the discussion conclusions when compiling; actual influence on outputs unobserved.
- Evidence limits: no discussion transcript or compilation trace; slicing need not preserve a whole message or only conclusions.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: explicit user action selects the episode, but code does not independently adjudicate its claims or require a per-page human acceptance. Transcript is mixed user and model provenance, not purely agent-generated experience. The server can still veto writes through the standard executor. This is a trace-fed guidance delivery chain, not an automatic experience-to-policy update or evidence of improved capacity. Reasons can survive in the transcript tail if originally stated, but no reason-extraction or complete-rationale guarantee exists. No answer oracle; open compilation request. Recovery uses ordinary job and page mechanisms. Closest related supplied route [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job) already supports optional guidance; this record establishes its shipped trace producer and selector, not a duplicate generic ingest job.

> const transcript = (session?.messages ?? []).filter(m => !m.failed).map(m => `${m.role === 'user' ? 'User' : 'Assistant'}: ${m.content}`).join('\n\n');
> --- `web/src/components/ChatPanel.tsx`

> onIngestFromChat(discussed, transcript.slice(-12_000));
> --- `web/src/components/ChatPanel.tsx`

#### MEM-RTE-state-withdrawal
Label: withdrawal and page recovery

Endpoints/progression: authenticated browser/REST action → deleteNote/archiveNote/rollbackNote or workspace reset → changed SQL visibility/content; scheduled purge → expired non-current snapshots removed. Owners: user/caller chooses action/version, software applies rules; purge uses plan/time predicate. Distinct from [RT-RTE-client-tools](runtime.md#rt-rte-client-tools)'s six-tool interface: these maintenance operations are exposed through REST/browser, not all as MCP tools. [SRC-1: `src/notes.ts`, `src/retention.ts`, `src/workspaces.ts`, `src/web-api.ts`, `web/src/pages/Workspace.tsx`]

- Immediate return: success/updated path/new version or conflict/error; reset returns note/share counts; purge returns removed count.
- Later read-back: ordinary consumers omit soft-deleted notes; archive path still supports reads/search; rollback's copied content becomes current; session history survives workspace reset.
- Delegated visibility: inapplicable — deterministic state operations, not delegated models.
- Selection predicate: exact path/target version with optimistic current version for rollback; raw-only archive and non-raw individual delete; workspace reset marks all live notes deleted; purge compares non-current snapshot age against owner plan/trial.
- Invalidation or expiry: delete is logical hiding, create at same path revives with continued version numbering; reset also revokes shares; old snapshots expire independently; current snapshots excluded from purge.
- Activation or effect: next queries observe visibility/path/content changes; archive does not withdraw compiled wiki assertions or delete copies already in chat.
- Evidence limits: no executed restore/purge; no full graph-repair guarantee for archive; no physical erasure guarantee from soft delete/reset; physical workspace/account deletion behavior not audited end-to-end.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission and recovery: rollback is caller-selected historical content, not quality-scored candidate selection. Stale version and absent snapshot can veto it; normalized raw updates veto raw rollback. Browser saves permit human editing, retains a conflict draft, and offers current reload/re-edit rather than silently overwriting. Archive changes note path with same ID and versions; undo places it under raw/sources with collision suffix if needed, not necessarily its original nested path. Archive preserves stored links/IDs, without rewriting all textual target strings or derived wiki summaries. Reset bypasses individual raw-delete refusal by workspace-wide soft deletion. These countercases qualify the word immutable: raw content is protected against ordinary update/delete, not against every visibility/path operation. [SRC-1: `src/notes.ts`, `src/workspaces.ts`, `web/src/pages/Workspace.tsx`]

> let target = undo ? `raw/sources/${path.slice(ARCHIVE_PREFIX.length).split('/').pop()}` : ARCHIVE_PREFIX + path.slice('raw/'.length);
> --- `src/notes.ts`

> const notes = await pool.query(`UPDATE notes SET deleted_at = now() WHERE workspace_id = $1 AND deleted_at IS NULL`, [ws]);
> --- `src/workspaces.ts`

#### MEM-RTE-human-delivery
Label: published and exported content

Endpoints/progression: explicit share creation → retained token/note relation → later token request → current page and permitted embedded assets; alternatively authenticated ZIP export → live notes plus assets with rewritten paths. Consumer: human/browser or download recipient; ownership: caller chooses sharing/export, code selects retained material. Distinct from [RT-RTE-client-tools](runtime.md#rt-rte-client-tools)'s workspace-authorized tool interface; a share is a narrower public credential. [SRC-1: `src/shares.ts`, `src/export.ts`, `src/assets.ts`, `src/api.ts`, `src/app.ts`]

- Immediate return: share URL/token, revoked status or ZIP bytes.
- Later read-back: subsequent share request receives current note Markdown, not a frozen publication snapshot; exported files afford external reading with no inspected downstream consumer execution.
- Delegated visibility: inapplicable — human-facing delivery; no built-in model delegation.
- Selection predicate: live unrevoked token joins one live note; shared asset must be referenced by its content and belong to share workspace; ZIP selects all live workspace notes and all workspace assets.
- Invalidation or expiry: revoke or soft deletion blocks new shared reads; export copies already delivered are not retracted by later note deletion.
- Activation or effect: read-only delivery changes what recipients can read, not the workspace knowledge or rule text.
- Evidence limits: no observed recipient use; export is not a full database checkpoint of versions, conversations or jobs; no provider-image delivery follows from browser access.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Sharing is user/caller selection of material for exposure, not semantic approval of every claim. No proposed knowledge revision or answer oracle is involved. Browser and exported representations can expose text and attachment payloads separately from agent tool delivery. [SRC-1: `src/shares.ts`, `src/export.ts`]

> if (!s.content.includes(`/api/assets/${assetId}`)) return null; // only images the shared page actually embeds
> --- `src/shares.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-BAP-schema-instructions](runtime.md#rt-bap-schema-instructions)

Memory-specific lineage and delivery: [MEM-OBJ-schema](#mem-obj-schema) stores the active text; [MEM-OBJ-template-state](#mem-obj-template-state) is an upstream alternative/checkpoint, not automatically active instructions. Tool response includes every live schema page and a fresh pending prelude; titles flattened/truncated through safeTitle are display hints, not source bodies. The consumer receives trimmed rule bodies, but no removal of rules by relevance or token budget. Behavioral horizon crosses runs until current notes change. Forced preflight and compliance remain unestablished; direct reads agree with the supplied path. [SRC-1: `src/notes.ts`, `src/ingest.ts`, `src/mcp.ts`]

#### On [RT-RTE-rule-update](runtime.md#rt-rte-rule-update)

Memory-specific extension: delivered-base hashes and exact text support later three-way comparison; they are not outcome evidence. Retained conflicts preserve the old base/version, while written pages receive a new base. Custom schema snapshots are another retained form: copy live rule/index content, reset log history, then permit explicit bundle edits/application. Copying, merging and overwrite can curate instructions without any model-based learning or answer-quality gate. Human per-content control is explicit in a browser edit/choice, not established for every authorized API caller. See [MEM-OBJ-template-state](#mem-obj-template-state) and [MEM-OBJ-user-templates](#mem-obj-user-templates). [SRC-1: `src/templates.ts`, `src/api.ts`]

#### On [RT-RTE-chat-session](runtime.md#rt-rte-chat-session)

Memory-specific content boundary: next-turn history retains message prose, including failure replies, but omits prior tool evidence/usage. Filing copies the selected assistant answer with the preceding question and timestamp, without job logs or verification records. Model finalText passes to onDone without the 20,000-character job-result slice, so retained chat text and job result need not be identical checkpoints. [MEM-OBJ-chat-sessions](#mem-obj-chat-sessions) and [MEM-RTE-discussion-guidance](#mem-rte-discussion-guidance) distinguish these consumers. [SRC-1: `src/chat.ts`, `src/ingest.ts`]

> if (spec.onDone) await spec.onDone({ finalText: r.finalText, job: { ...job, tokens_in: r.tokens_in, tokens_out: r.tokens_out, steps: r.steps, cost_usd: estimateCost(r.tokens_in, r.tokens_out, price) } });
> --- `src/ingest.ts`

#### On [RT-OBJ-ingest-jobs](runtime.md#rt-obj-ingest-jobs)

Memory-specific trace chain: model/tool events → last-200-event persisted log, with individual result output limited to 400 characters → chat tool summaries and written-path fallback. Full tool results still reach subsequent model calls within the job. This diagnostic transformation changes the later readable trace and may shape fallback prose, but does not install a durable policy or automatically summarize the whole episode into instructions. The supplied runtime caveat about truncated error JSON remains consequential. Page snapshots and full saved chat reply are separate checkpoint alternatives, not replicas of this log. [SRC-1: `src/ai/providers.ts`, `src/ingest.ts`, `src/chat.ts`]

> results.push({ type: 'tool_result', tool_use_id: tu.id, content: out });
> --- `src/ai/providers.ts`

#### On [RT-CMP-provider-models](runtime.md#rt-cmp-provider-models)

Working-context controls: Anthropic and OpenAI-compatible loops initialize their own per-job message arrays, seeded only with supplied chat role/content history plus task/system/tools. Other sessions and ingest jobs are not implicitly loaded. They accumulate current tool results verbatim and do not trim/compact those arrays in the inspected loops. Next chat job reconstructs the selected session's prose only; old tool-call bodies remain out, with note-path reload available through read_note. This is code-level isolation between job contexts and projection between turns, not a model-selected subagent frame or summary compactor. Frame analogy: job-local tool state disappears at job end while final text/durable page effects escape; unlike a popped stack frame, all saved conversation prose can be copied into a later independent job and pages remain addressable through fresh tool requests. The tool-call cap does not bound input tokens; provider-side truncation/state is uninspected. [SRC-1: `src/ai/providers.ts`, `src/chat.ts`, `src/ingest.ts`]

> const messages: any[] = [{ role: 'system', content: o.system }, ...(o.history ?? []), { role: 'user', content: o.user }];
> --- `src/ai/providers.ts`

## Write side

Acquisition and authorship are separate from admission. [MEM-RTE-source-admission](#mem-rte-source-admission) records a human-selected URL/file/text path and a configured scheduled alternative that requires no per-item approval. Direct create tools can also initialize raw, wiki or rules; source-layer location is not an authorship guarantee. Compilation then uses model decisions to transform retained sources into wiki prose under natural-language schema guidance, with path/version/capacity vetoes but no semantic approval gate. [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), [RT-RTE-client-tools](runtime.md#rt-rte-client-tools) and [RT-RTE-schema-spelling](runtime.md#rt-rte-schema-spelling) preserve the different write authorities.

Successful writes atomically update the individual note, snapshot and derived links/tags. This supports later access and per-page rollback, not multi-page correctness or all-or-nothing compilation. The symbolic backlink predicate marks a source processed independently of whether a complete summary or all requested edits were produced. [MEM-OBJ-links-tags](#mem-obj-links-tags), [MEM-OBJ-note-versions](#mem-obj-note-versions).

Maintenance has multiple non-equivalent results. Structural lint computes graph/index/log checks; model lint is requested to diagnose contradictions/staleness and either repair or retain suggestions in report/log pages. Those derived pages are ordinary editable knowledge/report material, not a durable independent rejection gate. A bad tool call may fail without failing the whole job; partial page changes can survive. Safe template conflicts reject replacement at that page, whereas overwrite mode admits shipped text; neither mechanism evaluates truth or improved capacity. Answer filing is an explicit content selection by the browser user, while chat's direct create/update tools need no filing approval. [RT-RTE-lint-job](runtime.md#rt-rte-lint-job), [RT-RTE-rule-update](runtime.md#rt-rte-rule-update), [RT-RTE-chat-session](runtime.md#rt-rte-chat-session).

Trace-fed behavior must be kept precise. Session prose is automatically retained and reloaded as history; job events become diagnostic summaries/fallback, not a new policy; discussion-guided ingest is an explicit user-triggered mixed-provenance trace delivery; query filing copies an answer as knowledge. The general template requests log/reason/conflict retention, but later retrieval need not read those reasons, and content replacement can omit them. These chains establish persistent material affecting available future context, not demonstrated experience learning, reflection, reliable theory criticism or self-improvement. No supplied run closes an improvement/activation claim. [MEM-OBJ-chat-sessions](#mem-obj-chat-sessions), [MEM-RTE-discussion-guidance](#mem-rte-discussion-guidance), [MEM-OBJ-wiki](#mem-obj-wiki), annotation on [RT-OBJ-ingest-jobs](runtime.md#rt-obj-ingest-jobs).

Withdrawal is consumer-relative: source archive only excludes pending, individual soft delete excludes normal note reads, reset also revokes shares but leaves conversations, version purge reduces recoverability, and external exported copies cannot be retracted by a note change. Rejection and cleanup do not automatically remove derived claims from other pages or old conversational prose. [MEM-RTE-state-withdrawal](#mem-rte-state-withdrawal), [MEM-RTE-human-delivery](#mem-rte-human-delivery).

## Read-back

The built-in consumer is a later provider invocation supplied by the local tool loop, not an unspecified hypothetical API caller. A tool request returns selected retained text and the loop incorporates full output into the next message exchange. Later jobs retrieve fresh notes; later chat turns also reload prior prose. External MCP provides an afforded external-agent consumer interface with inspected server execution, but external planning/compliance remains outside the pin. Browser readers reload note/history projections and completed chats. [MEM-RTE-note-retrieval](#mem-rte-note-retrieval), [RT-RTE-client-tools](runtime.md#rt-rte-client-tools), [MEM-OBJ-chat-sessions](#mem-obj-chat-sessions).

Selection is lexical/path-based or prompt-guided, not semantic-vector search. Index-first guidance compensates for cross-language search misses without enforcing index use. The 160-character snippet and sanitized pending title are display summaries; neither is the original source nor an assurance the model read it. All-schema concatenation has behavioral authority only after a model calls for it and interprets it. An archive remains reachable by search/path; a file path in a tool result is not an in-window pointer the model can dereference without another request. [MEM-RTE-note-retrieval](#mem-rte-note-retrieval), [MEM-OBJ-links-tags](#mem-obj-links-tags), [RT-BAP-schema-instructions](runtime.md#rt-bap-schema-instructions).

Working-context control is narrow locally: per-job arrays isolate current-run tool episodes; next-turn projection deliberately omits old tool bodies; explicit tools reload external retained pages. No local summarizing compaction or separate-context delegated worker appears in the directly inspected provider loops. This is a bounded code finding, not a claim about all provider internals or MCP clients. The discussion transcript tail is a distinct browser budget control with a new compilation consumer. Anthropic's 8,192 output-token cap is not a total input/window budget; no aggregate schema/history token budget is supplied here. [RT-CMP-provider-models](runtime.md#rt-cmp-provider-models), [MEM-RTE-discussion-guidance](#mem-rte-discussion-guidance).

## Integration issues

- No supplied fact requires withdrawal. The runtime's core note, schema-spelling, per-page persistence, log-truncation and chat-history findings were checked against source and retained.
- Possible route overlap: [MEM-RTE-note-retrieval](#mem-rte-note-retrieval) decomposes reads spanning [RT-RTE-client-tools](runtime.md#rt-rte-client-tools), [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job) and [RT-RTE-chat-session](runtime.md#rt-rte-chat-session), not a new competing implementation. [MEM-RTE-discussion-guidance](#mem-rte-discussion-guidance) supplies a concrete trace producer for the optional guidance accepted by ingest; it is distinct from generic ingest dispatch. [MEM-RTE-source-admission](#mem-rte-source-admission) elaborates an upstream endpoint in the runtime ingest route with alternative scheduled/import admissions. Reconciliation should connect these rather than infer separate stores or unrelated pipelines.
- Rule-state containment: [MEM-OBJ-template-state](#mem-obj-template-state) and [MEM-OBJ-user-templates](#mem-obj-user-templates) are separate stores used upstream of [RT-RTE-rule-update](runtime.md#rt-rte-rule-update); delivered comparison bases are not live instructions. Custom snapshot resets historical log text. Treating all retained template text as active policy would overstate its authority. [SRC-1: `src/templates.ts`]
- Image claim qualification: the import comment says localization lets the LLM see images later, but the actual built-in consumer receives Markdown links only. [MEM-OBJ-assets](#mem-obj-assets) and [MEM-RTE-human-delivery](#mem-rte-human-delivery) retain the implemented browser/export path; external multimodal consumer behavior is unresolved, so no model image-read conclusion follows. [SRC-1: `src/import-api.ts`, `src/ai/providers.ts`, `src/assets.ts`]
- Withdrawal limits: [MEM-RTE-state-withdrawal](#mem-rte-state-withdrawal) distinguishes immutable content from mutable source location/visibility and retained chat copies. Archive target-text repair and physical workspace/account cascade coverage were not fully audited; neither complete lineage repair nor physical erasure is established. No conclusion about causal benefit, actual model rule-following, successful semantic criticism or later output quality is permitted without execution evidence.
- Alternative template-language/scenario guidance, remote capture accuracy, provider window behavior and external-client orchestration remain uninspected. Known later consumers are retained beside their actual part; these unknowns do not erase inspected note/history/template transformations.

## Limitations and checks

Source identity and checkout HEAD match the supplied boundary; method authority is the supplied job, member type, collection, worker rules and records contract, not another run or prior characterization. No target program, test, model or service was executed. Direct inspection challenged source labels: raw is not necessarily original bytes, pending is backlink absence rather than quality, a saved result is not complete tool history, human-owned schema is not universally enforced, asset localization does not wire binary model input, and cleanup does not withdraw every copy. Supported implementation does not establish activation or benefit.

Deterministic validation: the supplied commonplace-validate command with the artifact and role memory passed (exit 0): “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” This checks form and quotation occurrence, not claim support or workflow acceptance.
