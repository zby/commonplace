---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Continuity memory: versioned facts, narrative replacement, passive and requested retrieval, vault indexes and incomplete organization sync."
run-id: AAS-2026-10-14-continuity-3e490e1d39f0-01
source-identity: https://github.com/uziiuzair/continuity
reviewed-boundary: "4ca8f6b4108aa4494e3861ed33c8019dbd662c67"
---

# Continuity memory report

## Boundary and evidence

This report covers retained conversation, personal instructions, the shared memory database, narrative synthesis, vault context, organization knowledge, plugin results and developer memory-bank instructions within the [boundary](boundary.md). SRC-1 is the repository at the frontmatter revision. Evidence is implementation and shipped doctrine, not an observed run. The checkout HEAD was rechecked and its tracked working tree was clean. No target program, test, provider or service was executed.

Direct inspection concentrated on admission, transformations and actual consumers. Supplied runtime records are provisional evidence for the foreground loop, research and plugin forwarding. No new source identity is introduced. External vault content, provider weights, installed clients, deployment state and the excluded historical Threads database remain outside the evidence. Available but uninspected bodies are identified below; they are not access gaps or absences.

| Entry point / operation | SRC-1 paths and inspection basis | Coverage / limit and prevented conclusion |
|---|---|---|
| Desktop remember, recall, forget, project retrieval | Direct: `lib/ai/memory-tools.ts`, `lib/db/memories.ts`, `lib/db/memory-db.ts` | [MEM-RTE-desktop-retention](#mem-rte-desktop-retention), [MEM-RTE-passive-context](#mem-rte-passive-context). Memory content, metadata and history separated below. |
| MCP dispatch and six registered modules | Direct: `server/index.ts`, `server/tools/memory-tools.ts`, `server/tools/project-tools.ts`, `server/tools/search-tools.ts`, `server/tools/relationship-tools.ts`, `server/tools/lifecycle-tools.ts`, `server/tools/narrative-tools.ts`; direct CRUD/search/narrative/learning implementation | [MEM-RTE-mcp-memory](#mem-rte-mcp-memory). Relationship/project callback dispatch read; underlying project/link CRUD bodies not fully inspected, preventing a complete relational-integrity audit. |
| Packaged CLI | Direct: `server/bin/cli.mjs`; bounded registration searches in `server/dist/server.mjs` | CLI imports committed bundle; expected memory/narrative/learning/history names occur there. Full bundle equivalence is uninspected, preventing installed-build parity claims. |
| Narrative maintenance, launch/manual/post-chat hooks | Direct: `lib/ai/narrative-synthesis.ts`, `providers/memories-provider.tsx`; supplied [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission), bounded chat-source reads/searches | [MEM-RTE-narrative-synthesis](#mem-rte-narrative-synthesis). Conversation scheduling is not automatic extraction of learnings. |
| Passive personal context | Direct prompt construction in `providers/chat-provider.tsx`, save/load handler in `components/settings/panels/GeneralPanel.tsx` | [MEM-RTE-profile-context](#mem-rte-profile-context); user settings are distinct from memories with source labels. |
| Saved conversation and isolated research | Direct `lib/db/messages.ts`, bounded chat history construction; supplied [RT-RTE-desktop-chat](runtime.md#rt-rte-desktop-chat), [RT-RTE-deep-research](runtime.md#rt-rte-deep-research) | [MEM-OBJ-messages](#mem-obj-messages) and annotations. No host compaction, provider-internal state or effectiveness conclusion. |
| Vault scan, file read/write, index maintenance | Direct `lib/vault/memory.ts`, bounded `lib/ai/obsidian-tools.ts`; caller search in `components/settings/panels/VaultPanel.tsx` | [MEM-RTE-vault-context](#mem-rte-vault-context). Scanner/file-operation bodies not audited; path containment and external file correctness remain unresolved. |
| Organization push/pull/search and sync | Direct `plugins/continuity-org-memory-sync/src/sync-engine.ts`, bounded `src/index.ts`, `org-server/src/routes/memories-push.ts`, `org-server/src/routes/memories-pull.ts`; supplied SDK/host routing findings | [MEM-OBJ-org-memories](#mem-obj-org-memories), [MEM-CLM-sync-withdrawal](#mem-clm-sync-withdrawal), annotation on [RT-RTE-org-ingestion](runtime.md#rt-rte-org-ingestion). Search implementation, auth and event bridge not fully audited; prevents joined-loop and completeness guarantees. |
| Threads scoring, drafts, review, rejection and budgets | Supplied [RT-RTE-threads-engagement](runtime.md#rt-rte-threads-engagement); bounded direct persistence searches in `plugins/continuity-threads-engagement/src/db.ts` | [MEM-OBJ-threads-results](#mem-obj-threads-results), annotation. No claim that rejection trains or revises future drafting. |
| Plugin session prompts/tools | Supplied [RT-OBJ-plugin-session](runtime.md#rt-obj-plugin-session), [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission); direct `plugin-host/src/handlers/events.ts` | Session registrations are not durable memory or established desktop prompt delivery. |
| Journal, journal links, canvas/database and briefing | Bounded direct searches in `lib/db/journal.ts`, `lib/db/journal-links.ts`, `lib/db/briefing.ts`, `lib/db/threads.ts`; bounded `providers/journal-provider.tsx`; direct `lib/services/briefing-service.ts`; supplied desktop/research persistence findings | [MEM-OBJ-workspace-state](#mem-obj-workspace-state). Human/UI consumers supported; complete canvas reload/tool schema and journal auto-link caller chains uninspected, preventing full model-context or trace-learning classification. |
| Developer-agent memory bank | Direct complete `CLAUDE.md`; supplied boundary coverage of `claude_docs/` | [MEM-RTE-developer-memory](#mem-rte-developer-memory). Documented external-agent procedure only; full historical doc bodies and actual updates uninspected. |
| Remote model state | Supplied [RT-CMP-ai-client](runtime.md#rt-cmp-ai-client), [RT-CMP-ai-evaluator](runtime.md#rt-cmp-ai-evaluator) | Parameters and provider state inaccessible; no inference of weight learning or fixity. |

## Core ideas

Continuity has two differently maintained personal-memory layers. Keyed memories retain individual text plus structured scope/type/source/version metadata. Narrative synthesis replaces a briefing and structured sections using active memories, caller-recorded observations and its previous narrative. A saved narrative version number is not a retained history of narrative texts. These are separate from raw message history. SRC-1, `lib/db/memories.ts`, `lib/ai/narrative-synthesis.ts`, `server/db/narratives.ts`; [MEM-OBJ-memories](#mem-obj-memories), [MEM-OBJ-narratives](#mem-obj-narratives).

Read-back combines code-driven passive supply with model-requested retrieval. Passive selection is recent-first across scopes, then type grouping under a character budget; it is not relevance ranking against the current query or active project. The global narrative is separately injected without that memory budget. Requested recall can recover memories excluded by passive selection, but keyed desktop recall is narrower than search/list. SRC-1, `lib/ai/memory-tools.ts`, `providers/chat-provider.tsx`; [MEM-RTE-passive-context](#mem-rte-passive-context), [MEM-RTE-desktop-retention](#mem-rte-desktop-retention).

Trust labels have uneven enforcement and visibility. Synthesis is instructed to treat source `user` as ground truth; MCP callers can supply that label themselves. Desktop writes do not set source, so new rows use schema default `ai`, including vault index writes. Passive formatting omits source attribution altogether. Source labels are metadata, not authenticated authorship or calibrated truth. SRC-1, `server/tools/memory-tools.ts`, `lib/db/memory-db.ts`, `lib/db/memories.ts`, `lib/ai/narrative-synthesis.ts`; [MEM-CLM-source-trust](#mem-clm-source-trust).

Archiving a fact stops active fact selection but does not retract already derived narrative content or remote copies. The supplied runtime correctly qualifies organization pull routing and plugin prompt delivery. The sync source adds a distinct withdrawal failure: deletion events are serialized as ordinary content without tombstones. SRC-1, `lib/db/memories.ts`, `lib/ai/narrative-synthesis.ts`, `plugins/continuity-org-memory-sync/src/sync-engine.ts`; [MEM-CLM-sync-withdrawal](#mem-clm-sync-withdrawal).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-memories
Label: memories content

Natural-language `memories.content` is stored in local SQLite memory.db with a descriptive key. Producers include desktop model tools, external MCP callers and the vault-index builder. Human-authored, model-inferred and program-derived content can share this table; the source field alone cannot establish actual lineage. Later consumers include passive system-prompt formatting, requested recall/MCP reads, narrative synthesis and the memory UI. At model consumers text supplies knowledge/context through interpretation, not executable policy. This is retained material, not the saved raw conversation. SRC-1, `lib/db/memories.ts`, `lib/ai/memory-tools.ts`, `lib/vault/memory.ts`, `server/db/memories.ts`. No supplied object counterpart; it is the retained input/output of [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission), not that route itself.

> `SELECT * FROM memories
>      WHERE archived_at IS NULL
>      ORDER BY updated_at DESC`
> --- `lib/db/memories.ts`

#### MEM-OBJ-memory-metadata
Label: memories access and provenance metadata

Symbolic SQLite fields carry IDs, keys, type, scope, project ID, tags, JSON metadata, source, timestamps, archive state and version. SQL/code consumes archive/scope/recency/type; models/humans interpret displayed type/tags. Arbitrary metadata payload semantics are opaque until a caller interprets them. These fields are distinct from [MEM-OBJ-memories](#mem-obj-memories): metadata can control selection without supplying the remembered assertion. Schema source values are restricted to user/ai/system, default ai. SRC-1, `lib/db/memory-db.ts`, `lib/ai/memory-tools.ts`, `server/db/search.ts`. No counterpart in the supplied runtime objects.

> source TEXT NOT NULL DEFAULT 'ai'
>         CHECK (source IN ('user', 'ai', 'system')),
> --- `lib/db/memory-db.ts`

#### MEM-OBJ-memory-versions
Label: memory_versions revision content and attribution

SQLite rows retain natural-language memory content and optional change reason, with symbolic memory ID/version/changed_by/time. These are historical snapshots, not full conversation traces or a complete revision diff of all metadata. Desktop updates insert the prior content/version before replacement; server updates record the new version/content. MCP history and the UI are actual requested readers; passive injection and synthesis read current memories, not historical reasons. No automatic restoration follows from history availability. SRC-1, `lib/db/memories.ts`, `server/db/memories.ts`, `server/tools/lifecycle-tools.ts`, `providers/memories-provider.tsx`. Distinct retained consequence of [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission).

> [generateId(), existing.id, existing.content, existing.version, "continuity-app", now]
> --- `lib/db/memories.ts`

#### MEM-OBJ-memory-links
Label: projects and memory_links access structure

SQLite `projects` stores symbolic IDs/path/archive/timestamps and human/model-interpreted name/description. `memory_links` stores symbolic endpoints and relation enums. MCP project creation/link calls admit these structures; project/list/get and relationship/history UI calls later read them. Relation labels such as contradicts/supersedes do not themselves revise or suppress content: passive/synthesis queries do not consult links. Underlying relation mutation/integrity implementation is not fully inspected. SRC-1, `lib/db/memory-db.ts`, `server/tools/project-tools.ts`, `server/tools/relationship-tools.ts`, `providers/memories-provider.tsx`, `lib/ai/narrative-synthesis.ts`. No supplied counterpart; not a symbolic truth adjudicator.

> relationship_type TEXT NOT NULL DEFAULT 'related'
>         CHECK (relationship_type IN ('related', 'depends_on', 'contradicts', 'supersedes', 'implements')),
> --- `lib/db/memory-db.ts`

#### MEM-OBJ-learnings
Label: learnings observations and absorption state

Caller-supplied natural-language `observation` and signal label/confidence/source IDs reside in SQLite `learnings`. These are proposed interpretations of conversations, not raw messages. The MCP `learning_record` entry accepts optional thread/message references without proving that extraction occurred or that those references ground the observation. The synthesis consumer receives observation/signal/confidence, not message text or source IDs; the MCP listing is another reader. Absorption is symbolic scheduling metadata and does not physically remove the observation. SRC-1, `server/tools/narrative-tools.ts`, `server/db/learnings.ts`, `lib/ai/narrative-synthesis.ts`. No supplied object counterpart; one input part of [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission).

> const learningLines = learnings.map((l) =>
>     `- [${l.signal_type}] ${l.observation} (confidence: ${l.confidence})`
>   );
> --- `lib/ai/narrative-synthesis.ts`

#### MEM-OBJ-narratives
Label: narratives briefing and structured sections

Natural-language briefing and insight strings are embedded in a symbolic JSON sections container, stored alongside version/confidence/scope/snapshot/time in SQLite memory.db. Synthesis derives them from facts, unabsorbed observations and prior content; MCP narrative_save is an alternative caller-authored admission path, not necessarily model synthesis. Later desktop chat receives briefing content and displayed confidence/version/date, not full structured sections. Next synthesis receives prior content and existing sections.learnings; other section fields are not separately replayed. UI/MCP readers can see richer stored material. Confidence is self/caller-report, not evaluation. Both app and server update an existing row in place. SRC-1, `lib/ai/narrative-synthesis.ts`, `providers/chat-provider.tsx`, `server/db/narratives.ts`, `server/tools/narrative-tools.ts`. No supplied object counterpart; retained product of [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission).

> `UPDATE narratives
>        SET content = $1, sections = $2, version = $3, confidence = $4,
>            last_synthesized_at = $5, memory_snapshot_hash = $6, updated_at = $7
>        WHERE id = $8`
> --- `lib/ai/narrative-synthesis.ts`

#### MEM-OBJ-messages
Label: messages retained conversation

App SQLite messages retain natural-language role/content plus symbolic thread ID/time and JSON display metadata. This is a raw conversation record, not full model/tool protocol or a derived memory. Later thread loading reconstructs UI messages; subsequent sends map those to role/content only. Research completion additionally saves a derived summary under the same storage surface. The role/content projection and its limits are supported by [RT-RTE-desktop-chat](runtime.md#rt-rte-desktop-chat) and [RT-RTE-deep-research](runtime.md#rt-rte-deep-research); no supplied retained object counterpart. SRC-1, `lib/db/messages.ts`, `providers/chat-provider.tsx`.

> ...messages.map((m) => ({
>             role: m.role,
>             content: m.content,
>           }))
> --- `providers/chat-provider.tsx`

#### MEM-OBJ-vault-index
Label: obsidian_vault_index derived display

A material content specialization of [MEM-OBJ-memories](#mem-obj-memories), this natural-language index is stored under obsidian_vault_index/global in memory.db. Code derives it from scan metadata/excerpts: at most 15 top-level folders, 30 scored files, first excerpt line cut to 60 characters. It is not a full vault snapshot or embedding index. Scoring uses frontmatter, shallow depth, name substrings and size; despite a comment mentioning recent content, the inspected scoring body has no timestamp score. The text is consumed by dedicated vault prompt injection as well as eligible general memory/synthesis selection. Incremental writes replace any line containing the file path or append a new path/time line; this can discard previously displayed metadata/excerpt. SRC-1, `lib/vault/memory.ts`, `lib/ai/obsidian-tools.ts`. Distinct specialization; no supplied object counterpart.

> scored.sort((a, b) => b.score - a.score);
>   return scored.slice(0, MAX_KEY_FILES).map((s) => s.file);
> --- `lib/vault/memory.ts`

#### MEM-OBJ-org-memories
Label: organization memories and sync queue

Organization SQLite stores natural-language key/content with symbolic type/scope/tags/version/timestamps. Server identity is key+scope, unlike desktop's project-aware identity. Sync serialization omits project_id, source, arbitrary metadata, links, history, narratives, learnings and archive state. Its pending push array and lastSyncAt cursor are volatile process state, not durable recovery memory. Pull returns at most 1000 rows in received_at order but omits received_at from the returned columns. These are distinct from local memories and from the [RT-RTE-org-ingestion](runtime.md#rt-rte-org-ingestion) route; integration defects prevent equating the stores. SRC-1, `org-server/src/routes/memories-push.ts`, `org-server/src/routes/memories-pull.ts`, `plugins/continuity-org-memory-sync/src/sync-engine.ts`.

> const SELECT_COLUMNS =
>   "id, key, content, type, scope, tags, version, created_at, updated_at";
> --- `org-server/src/routes/memories-pull.ts`

#### MEM-OBJ-threads-results
Label: Threads posts, drafts, engagements and search log

Plugin-local SQLite threads-engagement.db stores fetched post text, model relevance reason/score, generated or edited draft text and publication result/error records. Text is natural-language material; IDs/status/selection/version/time/counts are symbolic state. The review UI and approval endpoint consume drafts; scheduled scans consume retained post identity for deduplication and search logs for rolling budget. Regeneration deletes old drafts, selection changes is_selected, and rejection/skipping records status. A rejection record is workflow state, not by itself a training signal or changed model guidance. SRC-1, `plugins/continuity-threads-engagement/src/db.ts`; model/consumer passages supplied by [RT-RTE-threads-engagement](runtime.md#rt-rte-threads-engagement). No supplied object counterpart; source data contents excluded by boundary.

#### MEM-OBJ-workspace-state
Label: journal, canvas, database and briefing retained work

App SQLite stores editor blocks/JSON values with natural-language contents and symbolic IDs/date/type/sort/link/work-state fields. Journal editing is a human authoring surface: the provider debounces and saves supplied blocks, then reloads entries by selected date. Journal clearing nulls content rather than restoring old versions; link deletion is physical SQL deletion. Canvas/database work can be model-authored via desktop tools; research completion can append a derived report. The briefing service is a deterministic projection over three active threads and task/date state for a human, not model-generated memory. These distinct operative parts share app storage, not one admission policy. SRC-1, `providers/journal-provider.tsx`, `lib/db/journal.ts`, `lib/db/journal-links.ts`, `lib/services/briefing-service.ts`, `lib/db/briefing.ts`; supplied [RT-RTE-desktop-chat](runtime.md#rt-rte-desktop-chat), [RT-RTE-deep-research](runtime.md#rt-rte-deep-research). No supplied object counterpart. Canvas reload/context selection and auto-link end-to-end details remain uninspected; no claim that all these records enter personal synthesis.

> const [rightNow, thisWeek, threadCount, taskCount] = await Promise.all([
>     getActiveThreadsForBriefing(3),
>     getTasksByDay(),
>     getThreadCount(),
>     getPendingTaskCount(),
>   ]);
> --- `lib/services/briefing-service.ts`

### Routes

#### MEM-RTE-desktop-retention
Label: Desktop memory mutation and requested recall
Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

This specializes the container's desktop tool path, including its memory read executors. Foreground model proposes remember/forget; tool code checks arguments and Tauri availability, writes SQLite and returns text to the foreground loop. Remember normalizes key and writes global/null-project content; no per-item confirmation or truth oracle. Forget guidance asks explicit user request or obsolete content, but executor only checks key/existence. In open conversation the model chooses content, software admits it and humans can request later correction/forget; exceptions report errors, not transactional restoration. Revisions preserve content snapshots, with desktop/MCP differences in [MEM-OBJ-memory-versions](#mem-obj-memory-versions). SRC-1, `lib/ai/memory-tools.ts`, `lib/db/memories.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: success/error or formatted remembered/archived/recall text as tool result.
- Later read-back: subsequent sends can receive active facts by passive supply; later tool calls request key/search/list or project-specific content.
- Delegated visibility: remember receives proposed key/value/type/tags; recall delivers formatted fact text, optional type/tags/version; project_get truncates each content to 200 characters.
- Selection predicate: key lookup selects global/null-project active record; search LIKE matches key/content across scopes; no-key list reads all active scopes; get_project selects project ID.
- Invalidation or expiry: forget sets archived_at; later active reads omit it. Desktop re-remember uses active-only lookup, unlike server revival, so duplicate-key behavior for null project IDs is not a cross-entry invariant.
- Activation or effect: persistence changes later available facts; behavioral use of returned facts unobserved.
- Evidence limits: source wiring only; no semantic admission gate, live concurrency test or complete rollback guarantee.

> await setMemory(normalizedKey, args.value.trim(), "global", memoryType, args.tags);
> --- `lib/ai/memory-tools.ts`

#### MEM-RTE-passive-context
Label: Passive memories selection and system delivery
Part of: [RT-RTE-desktop-chat](runtime.md#rt-rte-desktop-chat)

Code runs getMemoryContext during each prompt rebuild. Active rows sorted updated_at descending across all scopes are sliced to 50, then grouped in preference/decision/context/constraint/pattern order. A nominal 4000-character counter cuts delivery early; headers, separators and overflow notice mean it is not an exact hard cap on final string length. A long earlier entry can prevent later entries from being considered. The query is not targeted by current topic or active project. Source/tags/project identity are not displayed in this passive view. SRC-1, `lib/ai/memory-tools.ts`, `lib/db/memories.ts`, `providers/chat-provider.tsx`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: memory context string or null to prompt builder, not a requested recall result.
- Later read-back: selected retained content reaches each later send's system message.
- Delegated visibility: foreground provider receives selected key/content/version strings and instructions to use them silently.
- Selection predicate: code-driven recent-first top 50, then type priority and character counter; no query relevance score.
- Invalidation or expiry: rebuilt every send; archived rows excluded; load failure silently omits this layer.
- Activation or effect: implemented system delivery gives natural-language context/instruction authority; model compliance and personalization benefit unobserved.
- Evidence limits: no run; this layer's budget does not limit narrative, profile, vault or history size.

> const MAX_MEMORIES_IN_PROMPT = 50;
> const MAX_PROMPT_CHARS = 4000;
> --- `lib/ai/memory-tools.ts`

> const limited = memories.slice(0, MAX_MEMORIES_IN_PROMPT);
> --- `lib/ai/memory-tools.ts`

#### MEM-RTE-mcp-memory
Label: MCP caller admission and requested memory retrieval

Distinct external stdio entry mechanism within the scope of [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission), overlapping that route's MCP admission but extending across project/link/history and requested read services. This is not a duplicate desktop path. CLI imports server/dist/server.mjs; source entry initializes schema and registers all six modules. Callers propose content and metadata, Zod/SQL admit it, and generic caller identity leaves human control unresolved. No answer oracle or human approval gate is provided. Open caller operations include memory CRUD/bulk import, project creation, linking, narrative_save and learning_record. Bulk memory import uses a transaction; ordinary multi-statement mutations and narrative/learning updates are separate. Server writeMemory finds archived rows and clears archival on update; memory_update accepts optional change_reason. Errors return MCP isError text. SRC-1, `server/bin/cli.mjs`, `server/index.ts`, `server/tools/memory-tools.ts`, `server/tools/narrative-tools.ts`, `server/db/memories.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: structured records encoded as text JSON, formatted summaries, acknowledgments or errors to external caller.
- Later read-back: registered memory_read/search, project/list/get, links_get, version_history, narrative_read/list and learning_list consume retained records on request; desktop can later read the shared memory store.
- Delegated visibility: MCP consumers get requested richer record data; narrative_list gives only scope/version/confidence/time summary, learning_list gives observation/signal/confidence/absorption display, not complete lineage IDs.
- Selection predicate: explicit IDs or key/scope/project; search uses LIKE over key/content/tags, optional filters and recent-first default limit 20; learning_list defaults to 50 for global scope.
- Invalidation or expiry: archive suppresses active memory reads/search; server upsert can revive archived records; history remains request-readable by memory ID.
- Activation or effect: registered operations persist/return knowledge and access structures; external caller's eventual model use is afforded, not an inspected deployed route.
- Evidence limits: bundle equivalence and external-client behavior uninspected; read API wiring does not establish behavioral use, semantic validity or automatic synthesis after learning_record.

> const sql = `SELECT * FROM memories WHERE ${conditions.join(" AND ")} ORDER BY updated_at DESC LIMIT ?`;
> --- `server/db/search.ts`

#### MEM-RTE-narrative-synthesis
Label: Scheduled or manual narrative replacement and later delivery
Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Code or human workflow initiation triggers a tool-free call through [RT-CMP-ai-client](runtime.md#rt-cmp-ai-client). Software decides whether inputs changed and automatically admits model output; a manual Synthesize action is not content approval. Proposal guidance asks evolving understanding, preservation of existing learnings and both sides of contradictions with adjusted confidence. No answer oracle validates those judgments. Parse failure admits the first 2000 raw-response characters with empty sections/default confidence, then can still mark input learnings absorbed. JSON parse success is not structural/semantic validation. Existing narrative is updated in place; individual absorption writes occur after narrative persistence, with no encompassing transaction shown. SRC-1, `lib/ai/narrative-synthesis.ts`, `providers/memories-provider.tsx`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: boolean success/no-change or exception handled by scheduler/UI; saved narrative replaces current row.
- Later read-back: next synthesis reads prior briefing and sections.learnings; later desktop sends load the global briefing with confidence/version/date, and UI/MCP consumers can read stored sections.
- Delegated visibility: synthesis receives all active memories across scopes, matching-scope unabsorbed observations, previous briefing and learning strings; not raw saved chat or observation source messages. Foreground receives narrative.content only with display metadata.
- Selection predicate: launch/post-chat checks require active memories; no narrative, stale plus any global learnings, or at least five global learnings trigger synthesis, with five-minute attempt debounce; snapshot hash can then skip unchanged input. Manual synthesis bypasses those scheduling conditions.
- Invalidation or expiry: input fact archival changes the next snapshot but does not directly erase prior narrative text; absorbed signals leave the pending set, not the database. Narrative replacement increments version without retained narrative history in these inspected functions.
- Activation or effect: derived briefing has a wired cross-send system-message path; retention and delivery are established, changed behavior or improved capacity unobserved.
- Evidence limits: generic observations can have unknown original provenance; automatic scheduling alone does not establish extraction from conversations; source labels and model confidence are not truth/benefit evidence.

> // Trigger if: stale + has data, OR 5+ unabsorbed learnings
>     if ((isStale && hasLearnings) || (learningCount[0]?.count ?? 0) >= 5 || narratives.length === 0) {
>       return await synthesizeNarrative("global");
>     }
> --- `lib/ai/narrative-synthesis.ts`

> // If parsing fails, create a minimal narrative from the raw response
>     result = {
>       content: response.content.slice(0, 2000),
> --- `lib/ai/narrative-synthesis.ts`

#### MEM-RTE-vault-context
Label: Vault scan index, requested files and index updates

Distinct acquisition/read route from personal-memory admission, with index writes overlapping [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) and model delivery overlapping [RT-RTE-desktop-chat](runtime.md#rt-rte-desktop-chat). User connect/rescan starts scan-to-index generation; code selects and formats file metadata/excerpts, then setMemory persists it. A model write_to_obsidian proposes file content; execution checks nonempty path/content and performs file write/rescan/index update. Prompt asks user approval but inspected executor has no separate approval token/check. Humans can edit external files or rescan, while semantic correctness has no answer oracle. SRC-1, `lib/vault/memory.ts`, `lib/ai/obsidian-tools.ts`, `components/settings/panels/VaultPanel.tsx`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: scan completion/settings result, read file content, write acknowledgment or errors.
- Later read-back: connected-vault prompt includes stored index on later sends; model can request files by path, search or folder listing for additional content.
- Delegated visibility: passive index exposes selected paths/metadata/excerpt fragments; read file returns first 10000 characters; model-written file can be reread later. Actual external file bodies are not frozen evidence.
- Selection predicate: connect/rescan code chooses scored top 30 files and 15 folders; model chooses requested path/search; dedicated vault prompt reads full stored index without the general-memory character counter.
- Invalidation or expiry: rescan overwrites index; successful file writes attempt incremental path-line replacement/append; index update errors are noncritical. No archive or disconnect cleanup of the stored index is established by this inspection.
- Activation or effect: derived index can affect future file discovery/context through natural-language system delivery; provider behavior and correct file routing unobserved.
- Evidence limits: scanner/file-operation internals and disconnect handler not fully inspected; approval guidance is not enforcement; stale metadata and external trust remain bounded uncertainties.

> const MAX_CONTENT = 10000;
>   const truncated = content.length > MAX_CONTENT;
> --- `lib/ai/obsidian-tools.ts`

> parts.push(`\n## Current Vault Index\n\n${vaultMemory}`);
> --- `lib/ai/obsidian-tools.ts`

#### MEM-RTE-profile-context
Label: Human profile editing and later system context
Part of: [RT-RTE-desktop-chat](runtime.md#rt-rte-desktop-chat)

Human authors nickname/occupation/about/customInstructions in General settings and explicitly saves; app code trims and persists settings. This is per-content human selection, unlike manual initiation of synthesis. Software supplies settings on later sends; model interprets them. No semantic oracle or model curation appears in these handlers. Human can replace/empty saved values; write failures show error status, with no all-fields transaction/rollback established. Settings text is natural language in app SQLite, symbolic keys select fields. SRC-1, `components/settings/panels/GeneralPanel.tsx`, `providers/chat-provider.tsx`, `lib/db/settings.ts`. Distinct write surface within the supplied system-guidance path [RT-BAP-system-guidance](runtime.md#rt-bap-system-guidance), not a second declaration of that authority path.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: settings save success/error feedback.
- Later read-back: buildSystemPrompt fetches the four stored fields for each send and inserts profile/custom instructions in the system message.
- Delegated visibility: foreground model receives nonempty profile strings/custom instruction body; settings load errors omit this content.
- Selection predicate: exact setting keys and nonempty values, not topic-based search or ranking.
- Invalidation or expiry: user replacement/empty save affects later prompt rebuild; no explicit context-size cap in inspected builder.
- Activation or effect: direct human-selected natural-language instruction authority across conversations; compliance remains unobserved.
- Evidence limits: no deployed setting/UI run; this is not authenticated source=user memory metadata or provider-weight change.

> setSetting(SETTING_KEYS.customInstructions, customInstructions.trim()),
> --- `components/settings/panels/GeneralPanel.tsx`

#### MEM-RTE-developer-memory
Label: Developer memory bank update and requested reload

Distinct documented development-agent procedure, not part of the desktop runtime route. CLAUDE.md instructs an external coding agent to read ACTIVE_CONTEXT and CLAUDE.md each conversation, request specialized context as needed, and update ACTIVE_CONTEXT each task plus PROGRESS for significant work. Natural-language Markdown lives in Git files; source authorship includes developer/agent contributions but historical provenance and actual execution are not established here. The agent proposes/writes summaries and decisions under maintenance guidance; content approval/veto and concrete execution are unresolved. No answer oracle validates remembered context. SRC-1, `CLAUDE.md`; full context-file bodies uninspected. No supplied counterpart after comparing desktop, research and plugin routes.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: inapplicable — the document defines procedure, not an executable return contract.
- Later read-back: instructed external agent reads current state at the next conversation and specialized files on demand.
- Delegated visibility: instructed agent receives Markdown development context; host loading and compliance are outside inspected implementation.
- Selection predicate: fixed startup pair plus topic-to-file instructions; no context budget stated in the inspected instructions.
- Invalidation or expiry: task-end edits replace current-state prose and add progress history; actual revisions and review controls uninspected.
- Activation or effect: requested behavioral guidance across development sessions, not established in-app execution or observed improvement.
- Evidence limits: shipped doctrine only; no execution trace or audited doc derivation; starting each task does not establish per-content human approval.

> ### END EVERY TASK BY UPDATING:
> **Required**: `@claude_docs/ACTIVE_CONTEXT.md`
> - Move completed work to "Recently Completed"
> - Update "Recent Changes" with files modified
> - Update "Next Steps"
> - Change timestamp and session focus
> --- `CLAUDE.md`

### Claims

#### MEM-CLM-source-trust
Label: Source label trust exceeds verified provenance

Synthesis guidance declares user-set memories ground truth and ai memories hypotheses. MCP source enum is caller-set, desktop setMemory does not persist explicit source, and schema defaults ai. Passive injection omits source labels. Thus source labels can shape synthesis proposals without authenticated provenance; source=user is not proof of human approval or truth. A previously user-labelled row can retain that label through a desktop content update because the UPDATE does not change source. SRC-1, `lib/ai/narrative-synthesis.ts`, `server/tools/memory-tools.ts`, `lib/db/memories.ts`, `lib/db/memory-db.ts`. No supplied claim counterpart; specializes the trust issue left open by [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission).

> - User-set memories (source: "user") are ground truth — state them directly
> - AI-inferred memories (source: "ai") are hypotheses — frame appropriately
> --- `lib/ai/narrative-synthesis.ts`

> source: MemorySourceEnum.optional().describe("Who wrote this: 'user' (explicit preference), 'ai' (inferred), 'system' (automated)"),
> --- `server/tools/memory-tools.ts`

#### MEM-CLM-sync-withdrawal
Label: Sync deletion lacks retained withdrawal state

The sync listener receives created/updated/deleted names but handleLocalChange ignores action and constructs the same ordinary memory payload without archived_at/tombstone. Server push upserts content; pull returns content rows without archive state. Hence these inspected handlers do not carry local withdrawal to the server or later pull readers. This is a distinct claim from the database-target defect in [RT-RTE-org-ingestion](runtime.md#rt-rte-org-ingestion), not a duplicate. It does not claim observed resurrection or prove delivery of deletion events. SRC-1, `plugins/continuity-org-memory-sync/src/sync-engine.ts`, `org-server/src/routes/memories-push.ts`, `org-server/src/routes/memories-pull.ts`.

> private async handleLocalChange(
>     _action: string,
>     data: Record<string, unknown>
>   ): Promise<void> {
> --- `plugins/continuity-org-memory-sync/src/sync-engine.ts`

### Evidenced absences

#### MEM-ABS-learning-extractor
Label: Inspected desktop lacks learning observation writer

- implementation conclusion status: absent

Bounded search at SRC-1 revision over `lib/`, `providers/`, `components/memories/`, `server/tools/` and `server/db/` for learning_record, recordLearning and INSERT INTO learnings found the MCP callback and server storage implementation, but no desktop observation writer. Direct memory tool dispatch includes remember/recall/forget/list_projects/get_project only; synthesis consumes observations and marks them absorbed. This supports absence of a desktop extractor in the inspected source paths, not absence of externally recorded signals or every possible installed plugin writer. SRC-1, `lib/ai/memory-tools.ts`, `server/tools/narrative-tools.ts`, `server/db/learnings.ts`, `lib/ai/narrative-synthesis.ts`. No supplied absence counterpart. It prevents interpreting post-chat synthesis scheduling as automatic chat-to-learning extraction, while preserving the known later transformation.

> export const MEMORY_TOOL_NAMES = MEMORY_TOOLS.map((t) => t.name);
> --- `lib/ai/memory-tools.ts`

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-BAP-system-guidance](runtime.md#rt-bap-system-guidance)

Memory-specific authority is at the foreground model interpreting the rebuilt system message, not at storage. Human-selected custom instructions, model/caller-written facts and synthesized briefing are distinct lineages. Passive memories receive neither source nor project label; narrative supplies content and displayed self-reported confidence, not its structured reasons. Horizon is later sends across threads for global context. Actual activation is unobserved. SRC-1, `providers/chat-provider.tsx`, `lib/ai/memory-tools.ts`, `lib/ai/narrative-synthesis.ts`; supporting passages in [MEM-RTE-passive-context](#mem-rte-passive-context), [MEM-RTE-profile-context](#mem-rte-profile-context), [MEM-OBJ-narratives](#mem-obj-narratives).

#### On [RT-OBJ-current-messages](runtime.md#rt-obj-current-messages)

Working context is volatile role/content/tool-call state; later retained history is a projection of saved messages, not this whole array. Source construction maps history to role/content, and no explicit history trim appears in that inspected builder. This limits reconstruction and budget guarantees without asserting absent provider-side compaction. SRC-1, `providers/chat-provider.tsx`, `lib/db/messages.ts`; [MEM-OBJ-messages](#mem-obj-messages).

#### On [RT-RTE-deep-research](runtime.md#rt-rte-deep-research)

The supplied record establishes selected/truncated inputs into fresh analyst/reviewer/synthesis contexts, with canvas report and saved summary escaping through completion callbacks. These derived results can persist in app work/history; the full isolated reasoning contexts are not replayed. This resembles per-task stack frames with only selected values crossing back, but summaries/reports are copied content, not dereferenceable live context references. Raw source, abbreviated findings and final prose must not be treated as equivalent. SRC-1, `lib/ai/research-engine.ts`, `providers/chat-provider.tsx`; the supplied route provides the minimum analyst-message passage and source limits. No demonstrated feedback from report quality into a retained research-method revision follows.

#### On [RT-RTE-org-ingestion](runtime.md#rt-rte-org-ingestion)

Local queue and cursor are volatile; organization SQLite content is durable. Returned org fields omit source/project/history/narrative and archival metadata. Server timestamp guard is not present in local pull SQL. Server pull caps 1000 received_at-ordered rows, while syncCycle advances lastSyncAt to the local clock after pull catches failures; no returned server cursor/pagination continuation appears in the inspected pair. These details further prevent a complete convergence claim beyond the supplied default-app-database defect. SRC-1, `plugins/continuity-org-memory-sync/src/sync-engine.ts`, `org-server/src/routes/memories-pull.ts`, `org-server/src/routes/memories-push.ts`; [MEM-OBJ-org-memories](#mem-obj-org-memories), [MEM-CLM-sync-withdrawal](#mem-clm-sync-withdrawal).

The org search callback can format retained key/type/content for a requesting caller with default five results. Host registration does not establish that the desktop discovers the tool or injected prompt; the supplied [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission) remains the delivery limit. SRC-1, `plugins/continuity-org-memory-sync/src/index.ts`.

#### On [RT-RTE-threads-engagement](runtime.md#rt-rte-threads-engagement)

Stored model relevance reasons are derived interpretations, drafts are proposed public content, and engagement/error records are outcome traces. Later review reads them; deduplication and search budget consume symbolic identities/counts. Draft editing/selection is a material human-afforded curation surface, while the approval endpoint does not authenticate human agency. Rejected/skipped statuses persist but no rejection-to-future-persona/model update is established by the supplied route or bounded DB search. SRC-1, `plugins/continuity-threads-engagement/src/db.ts`, `plugins/continuity-threads-engagement/src/ui-server.ts`; [MEM-OBJ-threads-results](#mem-obj-threads-results). No observed quality evaluation or capacity gain is claimed.

#### On [RT-OBJ-plugin-session](runtime.md#rt-obj-plugin-session)

Natural-language injected prompt bodies sit in symbolic volatile session maps; they are not a persistent cross-session memory store. Frontend manager arrays and host registrations have distinct consumer wiring, so org-sync prompt registration cannot serve as evidence of later desktop delivery. The supplied object and [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission) establish that limit and carry its source passages. SRC-1, `plugin-host/src/server.ts`, `lib/plugins/manager.ts`.

## Write side

Admission mechanisms must be kept separate. Desktop tool content is model-selected and code-admitted; MCP content is caller-selected and schema/SQL-admitted; profile settings and journal blocks are human-edited; vault index generation is automatic after a user-selected scan; narrative replacement is model-authored and automatically saved. Threads scores select drafts automatically while later endpoints edit/select/publish. Org admission checks schema/auth/timestamps rather than truth. Each known later transformation remains established even where initial content provenance is unknown. See [MEM-RTE-desktop-retention](#mem-rte-desktop-retention), [MEM-RTE-mcp-memory](#mem-rte-mcp-memory), [MEM-RTE-profile-context](#mem-rte-profile-context), [MEM-RTE-vault-context](#mem-rte-vault-context), [MEM-RTE-narrative-synthesis](#mem-rte-narrative-synthesis), [MEM-OBJ-workspace-state](#mem-obj-workspace-state), and annotated runtime plugin routes.

The qualifying derived-observation chain is caller-recorded conversation interpretation → learnings row → automatic narrative synthesis → retained narrative briefing → later system message. The raw conversation-to-observation extraction is not wired in the inspected desktop source; optional source IDs do not close it. Synthesis explicitly requests contradiction preservation, not deletion of rejected beliefs, and no semantic checker confirms preservation. Parsed or fallback output is persisted and observations can be marked absorbed regardless of content quality. Reasons are optional in memory history and some narrative insight source/confidence fields; the foreground does not receive those structured sections or history reasons. SRC-1, `server/tools/narrative-tools.ts`, `lib/ai/narrative-synthesis.ts`, `providers/chat-provider.tsx`; [MEM-OBJ-learnings](#mem-obj-learnings), [MEM-ABS-learning-extractor](#mem-abs-learning-extractor).

> - Preserve ALL existing learnings from the previous narrative
> - Add new learnings from the unabsorbed signals
> - If a new learning contradicts an old one, keep both but adjust confidence
> --- `lib/ai/narrative-synthesis.ts`

Maintenance is not universal erasure. Memory archival excludes current fact rows; version history remains. Server upsert can revive an archived record. Narrative persistence is in-place replacement without a corresponding saved prior narrative in the inspected functions. Archived facts can remain paraphrased in previous narrative content, and automatic checks require appropriate learning/data conditions; merely changing a memory after a narrative exists need not schedule an effective replacement. Org serialization cannot transmit a withdrawal marker. Journal clearing and draft regeneration use other mechanisms, not the memory archive policy. SRC-1, `lib/db/memories.ts`, `server/db/memories.ts`, `lib/ai/narrative-synthesis.ts`, `lib/db/journal.ts`, `plugins/continuity-threads-engagement/src/db.ts`; [MEM-CLM-sync-withdrawal](#mem-clm-sync-withdrawal).

## Read-back

Passive fact supply is an automatic push into each foreground system prompt; the selector receives stored recency/type/archive state, not a query. Narrative supply independently selects global/current content. Profile supply uses exact saved keys. Dedicated vault supply can bypass general-memory truncation and duplicate the same index if selected there too. All are model-interpreted text, not guarantees of truthful or private behavior. Requested recall/search/project tools can bring excluded stored content into a later model call through tool-result messages. SRC-1, `lib/ai/memory-tools.ts`, `providers/chat-provider.tsx`, `lib/ai/obsidian-tools.ts`; [MEM-RTE-passive-context](#mem-rte-passive-context), [MEM-RTE-desktop-retention](#mem-rte-desktop-retention), [MEM-RTE-vault-context](#mem-rte-vault-context).

External MCP readers are real registered delivery endpoints, but their external consumer's eventual use is not inspected. Stored narrative sections, memory history and relationships have API/UI read paths, not an automatic full replay into the foreground prompt. Search is SQL substring matching, not semantic retrieval established by the inspected code. Org search provides a requested callback but frontend discovery remains unresolved. Thread reload restores saved role/content, not complete tool protocol; research uses isolated contexts with derived report/summary escape, and no explicit history trimming was found in the inspected construction. SRC-1, `server/tools/`, `server/db/search.ts`, `providers/memories-provider.tsx`, `providers/chat-provider.tsx`; [MEM-RTE-mcp-memory](#mem-rte-mcp-memory), [MEM-OBJ-messages](#mem-obj-messages), research annotation.

Human read-back includes memory browsing/history/link inspection, journal date selection, briefing projections and Threads review. These qualify as later consumers of retained material without proving agent activation or trace-fed capacity improvement. External developer-agent context loading is documented rather than wired by this desktop runtime. SRC-1, `providers/memories-provider.tsx`, `providers/journal-provider.tsx`, `lib/services/briefing-service.ts`, `CLAUDE.md`; [MEM-OBJ-workspace-state](#mem-obj-workspace-state), [MEM-RTE-developer-memory](#mem-rte-developer-memory).

## Integration issues

1. Clarification rather than contradiction of [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission): post-chat synthesis checks are not observation extraction. Only MCP observation admission was located in the bounded writer search. This prevents an automatic raw-chat learning claim while retaining observation-to-narrative transformation. SRC-1, `server/tools/narrative-tools.ts`, `lib/ai/narrative-synthesis.ts`; [MEM-ABS-learning-extractor](#mem-abs-learning-extractor).
2. No replacement duplicates declared: desktop retention and synthesis are parts of the runtime memory container; passive/profile routes are parts of desktop chat. The broader MCP route overlaps runtime admission but includes distinct read/project/link/history operations; it should remain distinguished or be reconciled without equating it to desktop write admission. Objects are retained parts absent from supplied object declarations. See all Part of fields and [MEM-RTE-mcp-memory](#mem-rte-mcp-memory).
3. Runtime's supplied organization routing and plugin-discovery limits stand. Additional defects are withdrawal serialization, missing server cursor continuation, and action-independent payloads. Their consequence is no complete joined/convergent memory loop, even before deployed-operation questions. Event subscription names were found, but a bounded search in lib/providers/server/plugin-host source found no ordinary memory-write emission under those event names; generic bridging is not fully audited, so event delivery remains unresolved rather than a system-wide absence. SRC-1, `plugin-host/src/handlers/events.ts`, `plugins/continuity-org-memory-sync/src/sync-engine.ts`; [MEM-OBJ-org-memories](#mem-obj-org-memories), [MEM-CLM-sync-withdrawal](#mem-clm-sync-withdrawal), org annotation.
4. Source label trust and narrative confidence cannot establish provenance or correctness. The foreground omits source and structured narrative reasons; synthesis treats caller-set user labels specially. SRC-1, `lib/ai/memory-tools.ts`, `lib/ai/narrative-synthesis.ts`, `server/tools/memory-tools.ts`; [MEM-CLM-source-trust](#mem-clm-source-trust). Reconciliation must not upgrade this into authenticated human approval.
5. Narrative version is not rollback history, and forget does not retract prior derived briefing. The runtime container's version/archive statement is correct for facts but should not imply universal reversibility. SRC-1, `lib/db/memories.ts`, `server/db/narratives.ts`, `lib/ai/narrative-synthesis.ts`; [MEM-OBJ-memory-versions](#mem-obj-memory-versions), [MEM-OBJ-narratives](#mem-obj-narratives).
6. Unresolved included parts remain local: complete bundle parity, project/link CRUD integrity, scanner/file containment, vault disconnect cleanup, canvas read-back/context details, journal auto-link caller chain, organization search/auth/event integration, developer doc derivation and provider-internal state. Coverage rows identify evidence and conclusions prevented; these are not claims that those mechanisms are absent. Relevant records are [MEM-OBJ-memory-links](#mem-obj-memory-links), [MEM-RTE-vault-context](#mem-rte-vault-context), [MEM-OBJ-workspace-state](#mem-obj-workspace-state), [MEM-RTE-developer-memory](#mem-rte-developer-memory), and the supplied model components.

## Limitations and checks

Source revision and clean tracked checkout were rechecked before source inspection. Supplied invocation, member types, collection/worker rules and full record contract were read, recovering bounded continuations. No other run, retained analysis or prior characterization was read. Source additions remain within SRC-1; missing execution evidence prevents observed activation, benefit, calibrated confidence, live sync success and causal learning claims. These limits do not erase inspected persistence, transformations or delivery capacities. No formulated-theory or self-improvement attribution is made from labels such as narrative, mental model or learning alone.

Deterministic validation: passed the invocation-specific validate-output command: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” This form check does not establish source support or analytical acceptance.
