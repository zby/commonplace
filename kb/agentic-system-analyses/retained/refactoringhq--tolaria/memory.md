---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Tolaria memory: Markdown retention, transcript replay, bounded note context and MCP read-back, with partial maintenance coverage."
run-id: AAS-2026-10-14-tolaria-42ddaf2ee8cd-01
source-identity: https://github.com/refactoringhq/tolaria
reviewed-boundary: "48f2a70844c1e8005a7aa5f1499c66f7678360de"
---

# Tolaria memory report

## Boundary and evidence

Tolaria retains editable Markdown knowledge and application conversation transcripts. This account includes note writes and reads, guidance refresh, reference hydration, working-context filtering, and native withdrawal. It inherits the complete-artifact, partial-loop boundary in [boundary](boundary.md#boundary-and-evidence). External agents' own sessions, compaction, models and extension internals are excluded; their internal learning or memory cannot be attributed to Tolaria. User vaults and live remote starter content are not captured. No execution evidence was supplied.

All new inspection is SRC-1 implementation or shipped doctrine/design at the frozen commit. HEAD was rechecked against the full pin. Runtime findings below are supplied findings, not independent execution observations.

| Entry point or operation | Source paths and inspection | Covering records or unresolved limit |
|---|---|---|
| Workspace send and trimmed history | Direct: `src/lib/aiAgentConversation.ts`, `src/utils/ai-chat.ts`; supplied dispatch: `src/lib/aiAgentSession.ts` | [RT-RTE-workspace-send](runtime.md#rt-rte-workspace-send), memory annotation below; no application-generated history summary |
| Native and cross-window transcript save/load/reset/clone | Direct: `src-tauri/src/settings.rs`, `src/lib/aiWorkspaceSessionStore.ts`, `src/lib/crossWindowPersistedStore.ts` | [MEM-OBJ-workspace-sessions](#mem-obj-workspace-sessions), [MEM-RTE-transcript-replay](#mem-rte-transcript-replay); no crash-durability guarantee |
| Explicit note references and active-note context | Direct: `src/utils/ai-reference-content.ts`, `src/utils/ai-context.ts`, `src/components/useAiPanelContextSnapshot.ts` | [MEM-RTE-reference-context](#mem-rte-reference-context); active snapshot builder inspected, complete panel-to-dispatch wiring not retraced |
| MCP get/search/context/list and alternative guidance delivery | Direct: `mcp-server/tool-service.js`, `mcp-server/vault.js`, `mcp-server/agent-instructions.js`; tool map confirmed by search in `mcp-server/index.js` | [MEM-RTE-mcp-read](#mem-rte-mcp-read); external caller choices and live bridge delivery unknown |
| MCP create/update/append; direct-provider create | MCP service and filesystem functions directly read; provider path supplied | [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write), [RT-RTE-provider-create](runtime.md#rt-rte-provider-create); independent admission mechanisms |
| Managed AGENTS synchronization and compatibility configuration | Template directly read in `src-tauri/src/vault/getting_started.rs`; supplied refresh and Pi configuration findings | [RT-RTE-guidance-sync](runtime.md#rt-rte-guidance-sync), [RT-RTE-pi-extension](runtime.md#rt-rte-pi-extension); complete migration lifecycle not inspected |
| Native note save/delete/batch delete | Direct commands in `src-tauri/src/commands/vault/file_cmds.rs`, deletion in `src-tauri/src/vault/trash.rs` | [MEM-RTE-note-withdrawal](#mem-rte-note-withdrawal); editor confirmation and cache reconciliation uninspected |
| Desktop vault index, watcher/cache, Git and type/view consumers | Included, not traced end to end | Initialization, invalidation and symbolic metadata authority remain unresolved; no cross-client consistency claim |
| Web/server/collaboration and remote persistence | Included; source paths discovered in `apps/server/src/routes.ts`, `apps/server/src/collab/flush.ts`, `apps/server/src/collab/snapshots.ts` but not read | Admission, collaborative checkpoint forms and later consumers unresolved; desktop findings do not describe these paths |
| Evaluators, hooks and maintenance | Supplied test inventory; template maintenance instructions directly read; all hooks/evaluators not audited | No semantic-quality gate, trace-derived curation or absence of such mechanisms established system-wide; tests not executed |

## Core ideas

The retained knowledge is readable and replaceable, not an opaque vector store in the inspected routes. Search selects substring matches; orientation selects recent files; explicit references select named notes. These are different selectors, not evidence of semantic retrieval ([MEM-RTE-mcp-read](#mem-rte-mcp-read), [MEM-RTE-reference-context](#mem-rte-reference-context)).

Conversation retention and model-visible history differ. The store can retain references, reasoning and tool actions, but later history conversion supplies only user text and assistant response. It then drops an old prefix using an approximate character budget. This is raw-turn replay with selective omission, not a trace-to-summary learning mechanism ([MEM-OBJ-workspace-sessions](#mem-obj-workspace-sessions), [RT-RTE-workspace-send](runtime.md#rt-rte-workspace-send)).

Root guidance can be both mutable vault content and a later instruction source. Template refresh and content edits are separate admissions. A request to obey guidance is not proof that the external runtime obeys it ([RT-RTE-guidance-sync](runtime.md#rt-rte-guidance-sync), [MEM-BAP-retained-context](#mem-bap-retained-context)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-workspace-sessions
Label: AI workspace sessions

Source-native identity: session-keyed `SessionMap`, serialized as `ai-workspace-sessions.json` and cached under `tolaria:ai-workspace-sessions:v1`. Storage substrate: app configuration filesystem, localStorage and frontend memory. This is distinct from [RT-OBJ-stream-request](runtime.md#rt-obj-stream-request): it is retained input to later request construction, not an individual dispatch request. Its lineage is foreground prompts, streamed responses, reasoning/action events and application status updates, including cloned prefixes. Native initialization returns an empty object for a missing file or a parsed nonobject; parse/read errors propagate to a frontend catch that returns an empty map.

Operative parts differ: natural-language user/response/reasoning/reference content; symbolic status, IDs, streaming flags and action/access metadata. Event objects are normalized app traces, not necessarily verbatim external logs. The displayed assistant response is not equivalent to any opaque external agent checkpoint. Models remain the supplied [RT-CMP-cli-model](runtime.md#rt-cmp-cli-model) and [RT-CMP-api-model](runtime.md#rt-cmp-api-model), whose parameters/version resolution are external.

Later frontend consumers normalize status and streaming flags; request construction omits local markers, reasoning, actions and stored reference bodies. Thus retained reasons are present only when the original content includes them; neither a separate rationale derivation nor later replay of the reasoning field is established. Evidence: SRC-1, `src/lib/aiWorkspaceSessionStore.ts`, `src/lib/aiAgentConversation.ts`, `src-tauri/src/settings.rs`, `src/lib/crossWindowPersistedStore.ts`.

> let json = serde_json::to_string_pretty(&sessions)
>         .map_err(|e| format!("Failed to serialize AI workspace sessions: {}", e))?;
>     fs::write(path, json).map_err(|e| format!("Failed to write AI workspace sessions: {}", e))
> --- `src-tauri/src/settings.rs`

> const history: ChatMessage[] = [{ role: 'user', content: message.userMessage, id: message.id ?? '' }]
>     if (message.response) {
>       history.push({ role: 'assistant', content: message.response, id: `${message.id}-resp` })
>     }
> --- `src/lib/aiAgentConversation.ts`

#### MEM-OBJ-vault-notes
Label: Vault Markdown notes

Source-native identity: Markdown files read by `getNote` and changed by create/update/append/native file operations. Storage substrate: vault filesystem. Natural-language body and title are interpreted by readers/models; parsed frontmatter and paths are symbolic access/metadata fields. Complete frontend type/view semantics are uninspected rather than inferred from frontmatter presence. Lineage can be human, external agent, provider tool output, imported or seeded material; the inspected storage functions do not authenticate provenance or certify truth. Raw event traces and derived notes can both be written as Markdown; the format alone does not distinguish them.

Distinct from [RT-OBJ-agent-prompt](runtime.md#rt-obj-agent-prompt): retained vault files, not the assembled shipped prompt. This object is the shared result/retained input of [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write) and [RT-RTE-provider-create](runtime.md#rt-rte-provider-create), not a duplicate route. Root AGENTS is an instruction-bearing instance with special refresh/read consumers; it is not merely equivalent to ordinary note evidence. Evidence: SRC-1, `mcp-server/vault.js`, `mcp-server/agent-instructions.js`, `src-tauri/src/vault/getting_started.rs`.

> frontmatter: parsed.data,
>     content: parsed.content.trim(),
> --- `mcp-server/vault.js`

### Routes

#### MEM-RTE-transcript-replay
Label: Transcript storage and replay

Part of: [RT-RTE-workspace-send](runtime.md#rt-rte-workspace-send)

A route part of the supplied invocation, not a replacement for it: message/status mutation → cross-window publish → debounced native serialization → subsequent load → later history builder. Code admits updates and validates only container shape/status at load; user send initiates content, model supplies response, and no per-transcript review precedes storage. Reset and prefix clone are code-exposed content replacement operations, not quality evaluation. Open conversation mode, no answer oracle or improvement objective. Physical write failures are hidden from chat; native replacement has no inspected fsync/atomic-swap branch. Evidence: SRC-1, `src/lib/aiWorkspaceSessionStore.ts`, `src/lib/crossWindowPersistedStore.ts`, `src-tauri/src/settings.rs`, `src/lib/aiAgentConversation.ts`.

- Immediate return: published UI state; asynchronous native save is not awaited by message mutation.
- Later read-back: loaded session messages supply a later send's user/assistant history through the supplied trimming route.
- Delegated visibility: only completed nonmarker user/response strings enter app history; reasoning/actions/reference bodies do not.
- Selection predicate: session ID selects stored messages; native startup load is ignored if local storeVersion changed meanwhile; nonempty native map replaces current snapshot, empty native map can schedule current cache for saving.
- Invalidation or expiry: reset replaces one session with empty state; clone keeps a prefix with nonstreaming flags; load normalizes running state; no automatic expiry inspected.
- Activation or effect: persistence and later request reconstruction are wired; behavioral reliance and durable restart success unobserved.
- Evidence limits: concurrent window conflict resolution and shutdown completion unestablished; native storage uses whole-file write.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (storeVersion !== loadVersion) return
> --- `src/lib/aiWorkspaceSessionStore.ts`

> if (Object.keys(nativeSessions).length === 0) {
>     const currentSessions = sessionStore.getSnapshot()
>     if (Object.keys(currentSessions).length > 0) scheduleNativeSessionsWrite(currentSessions)
>     return
>   }
> --- `src/lib/aiWorkspaceSessionStore.ts`

#### MEM-RTE-reference-context
Label: Explicit reference context

Part of: [RT-RTE-workspace-send](runtime.md#rt-rte-workspace-send)

Current explicit references → hydration if no content supplied → frontmatter-stripped body → code-owned head/tail omission → formatted prompt → selected CLI or provider. This is a distinct selection part of dispatch. It reads retained notes, but its compact output is current-request context, not a separately persisted summary. A supplied content field bypasses disk hydration. Selection is user-driven reference choice with deterministic delivery, not independent unsolicited retrieval. Evidence: SRC-1, `src/utils/ai-reference-content.ts`, `src/utils/ai-context.ts`, `src/lib/aiAgentConversation.ts`; send hydration is also identified by source search in `src/lib/aiAgentSession.ts`.

- Immediate return: prompt text plus JSON-shaped reference metadata/body snapshots.
- Later read-back: named retained files can enter later invocations; old reference objects remain stored but are not automatically rehydrated or embedded by history conversion.
- Delegated visibility: body text and path/title/type, not complete original frontmatter; missing bodies produce get_note instructions.
- Selection predicate: current references; existing content wins, otherwise get_note_content attempts disk read; failure preserves a reference without content.
- Invalidation or expiry: next prompt uses its own references; no stored summary or automatic cache invalidation in this helper.
- Activation or effect: body delivery is wired; following the instruction to reload omitted text is not established, especially for direct providers lacking a read tool.
- Evidence limits: no combined prompt token bound or deployed reference accuracy established; hydrated disk content and editor snapshot content can differ.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (reference.content !== undefined) return reference
> --- `src/utils/ai-reference-content.ts`

> const MAX_REFERENCED_NOTE_BODY_CHARS = 12_000
> const REFERENCED_NOTE_BODY_HEAD_CHARS = 8_000
> const REFERENCED_NOTE_BODY_TAIL_CHARS = 2_000
> --- `src/utils/ai-context.ts`

#### MEM-RTE-mcp-read
Label: MCP retained content reads

Registered read/search/context handlers → active-vault service → filesystem selection/parsing → tool result to MCP caller. This is the read side, distinct from [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write). Caller chooses tools and arguments; code selects roots/results. An app-managed Codex caller is supplied by [RT-RTE-workspace-send](runtime.md#rt-rte-workspace-send); independent MCP clients are afforded consumers whose deployed identities remain unknown. Evidence: SRC-1, `mcp-server/index.js`, `mcp-server/tool-service.js`, `mcp-server/vault.js`, `mcp-server/agent-instructions.js`.

- Immediate return: get-note parsed frontmatter, trimmed body and mtime; search path/title/snippet; context types/count/folders/recent-note metadata/config and root agent instructions; list-vaults supplies guidance presence/path, not its body.
- Later read-back: subsequent tool calls consume current files created or changed by earlier work; not merely a hypothetical storage API.
- Delegated visibility: exact requested note body after parse/trim; search snippets are partial; orientation returns metadata and selected guidance rather than every note body.
- Selection predicate: explicit path/root for get-note with ambiguity rejection; case-insensitive title/content substring for search, default limit 10, scan order and earlier active roots can fill the global cap; context sorts by mtime and selects 20 recent notes, all roots unless one requested.
- Invalidation or expiry: filesystem rereads observe current content; no retained retrieval snapshot or expiry in inspected functions; deleted files cease to be readable at their path.
- Activation or effect: tool map/service and filesystem reads are wired; caller reliance and model compliance unobserved.
- Evidence limits: no semantic ranking, trust verification or global byte/token budget established by these selectors; scan exclusions/error handling prevent assuming every possible vault file is represented.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const q = query.toLowerCase()
> --- `mcp-server/vault.js`

> notesWithMtime.sort((a, b) => b.mtime - a.mtime)
>   const recentNotes = await Promise.all(
>     notesWithMtime.slice(0, 20).map(hydrateContextNoteTitle),
>   )
> --- `mcp-server/vault.js`

> agentInstructions: await readAgentInstructions(vaultPath),
> --- `mcp-server/agent-instructions.js`

#### MEM-RTE-note-withdrawal
Label: Native note withdrawal

Native delete command → path validation → permanent filesystem removal → returned deleted path; batch operation returns successes and logs skips. This is distinct from MCP replacement in [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write), not another implementation of that tool. Caller proposes target; native code rejects nonexistent/nonfile paths for single delete and performs physical removal. Human per-content control is unresolved because full caller confirmation was not inspected. Open maintenance operation, no answer oracle; no semantic rejection or recovery/rollback branch inspected. Evidence: SRC-1, `src-tauri/src/commands/vault/file_cmds.rs`, `src-tauri/src/vault/trash.rs`.

- Immediate return: deleted path or error; batch success list can coexist with failures.
- Later read-back: future filesystem/MCP reads cannot retrieve the removed file through its former path; already copied transcript/reference content is not revoked by this function.
- Delegated visibility: deletion results reach native command caller; model invocation from deletion itself is inapplicable — no model call in this path.
- Selection predicate: caller-supplied path(s), validated as existing before native deletion.
- Invalidation or expiry: permanent file removal; watcher/index/link reconciliation uninspected.
- Activation or effect: remove_file is wired; actual deletion and downstream refresh not observed.
- Evidence limits: no inspected caller admission, complete cache cleanup or undo mechanism; generic library availability does not establish model-driven withdrawal.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> fs::remove_file(file).map_err(|e| format!("Failed to delete {}: {}", path, e))?;
> --- `src-tauri/src/vault/trash.rs`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-retained-context
Label: Retained context interpretation

Consumer: later selected CLI agent/provider via replay/reference text, or MCP client/model via tools. Channel: natural-language retained body/history/guidance embedded in a prompt or returned as tool content. Force: interpretation as conversational evidence or behavioral guidance, not semantic validation or OS enforcement. Horizon: later sends/tool calls, potentially across application sessions. Distinct from [RT-BAP-prompt-policy](runtime.md#rt-bap-prompt-policy), which concerns the assembled prompt's policy: this path concerns mutable retained inputs. It overlaps policy delivery when AGENTS is returned, but not static assembly identity. Files may carry arbitrary user/import/model content; inspected readers do not authenticate epistemic provenance. Evidence: SRC-1, `src/lib/aiAgentConversation.ts`, `src/utils/ai-context.ts`, `mcp-server/agent-instructions.js`, `src-tauri/src/vault/getting_started.rs`; passages above establish delivery, not compliance.

## Annotations

#### On [RT-RTE-workspace-send](runtime.md#rt-rte-workspace-send)

Working-context control is deterministic suffix eviction, not compaction. At every send, code filters streaming/local-marker material and retains newest fitting user/assistant strings, stopping at the first nonfitting message. Approximate history budget is 100,000 tokens at ceil(chars/4), excluding latest prompt, system text and reference snapshots. Omitted older turns remain in the store, but this builder establishes no automatic reimport route. Stored action/reasoning fields are not included even when recent. The window is supplied by value; IDs outside it are not automatically dereferenced pointers. External CLI context isolation/compaction remains uninspected. Evidence: SRC-1, `src/utils/ai-chat.ts`, `src/lib/aiAgentConversation.ts`; supplied trimming passages support this finding.

#### On [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write)

Retained result is vault Markdown consumed by [MEM-RTE-mcp-read](#mem-rte-mcp-read). Replacement uses optional mtime conflict checking and temporary-file rename; append extends content without that conflict check. Content authorship and physical I/O are distinct: caller/model supplies text, code admits active-root paths, and physical storage does not evaluate claim quality. Temporary cleanup removes failed replacement staging, not previous knowledge from all copied contexts. Evidence: SRC-1, `mcp-server/vault.js`, `mcp-server/tool-service.js`; supplied replacement passages and direct reads establish the scope.

#### On [RT-RTE-guidance-sync](runtime.md#rt-rte-guidance-sync)

The shipped template is natural-language conventions with examples and explicit reasons for some rules (for example H1 drives display/link/search titles). It persists at root, while actual later obedience is unknown. MCP context explicitly returns root AGENTS content and can also return legacy `config/agents.md`; refresh is therefore not the only guidance-consumption path. The template asks agents to change AGENTS only on user request and avoid silently overwriting custom guidance; these are instructions, not the enforcement predicate. Evidence: SRC-1, `src-tauri/src/vault/getting_started.rs`, `mcp-server/agent-instructions.js`, `mcp-server/vault.js`.

> - Update `AGENTS.md` only when the user asks for vault-level guidance changes.
> --- `src-tauri/src/vault/getting_started.rs`

## Write side

The inspected write mechanisms have separate admissions. MCP active-root/path checks permit caller-proposed Markdown; provider create admits returned supported calls and exclusive file creation without per-content confirmation; managed guidance synchronization admits code-selected replacements under a custom-content preservation predicate. Native save accepts replacement text after writable-path validation, but full editor human-control wiring remains uninspected. Native delete removes files, without retracting already copied context. See [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write), [RT-RTE-provider-create](runtime.md#rt-rte-provider-create), [RT-RTE-guidance-sync](runtime.md#rt-rte-guidance-sync), [MEM-RTE-note-withdrawal](#mem-rte-note-withdrawal); SRC-1, `src-tauri/src/commands/vault/file_cmds.rs`.

Trace acquisition retains message/event fields. Normalization changes recovery flags, not the semantic content of lessons. Later user/assistant replay can influence work, but the inspected raw-to-selected-text chain does not produce a durable distilled summary or validated lesson. Note append can record experience, yet no automatic trace-to-note derivation is established by append capability alone. External CLI checkpoints, collaborative snapshots and other maintenance transformations remain unresolved. Neither retention nor editability demonstrates improved future capacity.

## Read-back

Conversation read-back is automatic after a user starts another send; code chooses a verbatim suffix. Explicit note references are requested selection followed by automatic hydration/omission. MCP selection is caller-requested: get-note targets a path, search targets substring matches, context targets recent metadata and instruction files. The context response's recency sorting is not an unsolicited model push. Current selection does not depend on successful past outcomes or epistemic quality in these inspected paths ([MEM-RTE-transcript-replay](#mem-rte-transcript-replay), [MEM-RTE-reference-context](#mem-rte-reference-context), [MEM-RTE-mcp-read](#mem-rte-mcp-read)).

The active-note builder supplies a second working-context control: over 24,000 body characters it retains a 16,000-character head and 4,000-character tail with an omission instruction; reference bodies over 12,000 retain 8,000 plus 2,000. Note lists cap at 100; other open tabs contribute metadata. This is mechanical omission, not model summarization. Source remains disk/editor text, while the snapshot is a value copy. get_note is a requested reload affordance for omitted text, not proof of reload; a direct-model create-only tool branch cannot execute that read instruction through its advertised tool. Full active-panel wiring remains a stated coverage limit (SRC-1, `src/utils/ai-context.ts`, `src/components/useAiPanelContextSnapshot.ts`; [RT-RTE-provider-create](runtime.md#rt-rte-provider-create)).

## Integration issues

- Storage gap narrowed, not contradicted: [RT-RTE-workspace-send](runtime.md#rt-rte-workspace-send) marked native storage uninspected. [MEM-OBJ-workspace-sessions](#mem-obj-workspace-sessions) and [MEM-RTE-transcript-replay](#mem-rte-transcript-replay) now establish object-shaped JSON save/load and best-effort cache/native synchronization. This supports implemented retention, not crash durability or observed restoration.
- Additional context control: [MEM-RTE-reference-context](#mem-rte-reference-context) and the active-note builder add head/tail omission beyond the supplied history trim. Do not classify all context limitation as old-turn trimming or infer a combined request bound. Editor-vs-disk freshness and complete active-panel dispatch wiring remain unresolved.
- Guidance alternative: [RT-RTE-guidance-sync](runtime.md#rt-rte-guidance-sync) persists AGENTS; [MEM-RTE-mcp-read](#mem-rte-mcp-read) can return it and legacy config guidance directly. Content divergence between these files and precedence at external consumers remain uninspected.
- Containment is explicit for transcript replay and explicit references under [RT-RTE-workspace-send](runtime.md#rt-rte-workspace-send). No new record is intended as a duplicate of a supplied record. [MEM-BAP-retained-context](#mem-bap-retained-context) overlaps the delivery channel of [RT-BAP-prompt-policy](runtime.md#rt-bap-prompt-policy) but has mutable retained inputs as its distinct referent.
- Partial loop remains material: collaborative checkpoints, remote writes, editor approval, watcher/cache/Git reconciliation, type/view symbolic consumers, all hooks and semantic evaluators have not been traced. Their missing admission/lineage/consumer facts prevent a whole-system memory ontology or absence claim. Known Markdown/transcript mechanisms must not erase these unresolved alternatives.
- Rejection and withdrawal are local: mtime refusal and temp-file cleanup in [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write) do not retract copied content; [MEM-RTE-note-withdrawal](#mem-rte-note-withdrawal) removes files but does not establish index or transcript revocation. Complete cleanup/recovery remains unresolved.

## Limitations and checks

Only pinned source text was inspected. No target execution, tests, services, dependencies or model calls were run. Positive wiring is not observed activation or benefit. Countercases checked include prefilled references bypassing hydration, missing bodies, raw history omitting stored reasons, writable direct-provider calls despite chat-only documentation, guidance read through MCP rather than prompt-only file access, and permanent native deletion despite the module name `trash`.

Source HEAD equals the supplied reviewed commit. Required invocation, type and record inputs were fully read; supplied identity fields are unchanged. Deterministic validate-output check passed; this establishes structural and quotation checks, not semantic acceptance.
