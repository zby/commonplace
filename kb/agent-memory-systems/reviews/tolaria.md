---
description: "Tolaria review: files-first Markdown vault desktop app with Git, type conventions, MCP tools, and active-note AI context push"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-05"
---

# Tolaria

Tolaria, from RefactoringHQ, is a local-first Tauri/React desktop app for managing Markdown knowledge-base vaults. At the reviewed commit it treats vault files and Git history as the durable user-owned substrate, derives cache and UI state from those files, exposes read-oriented MCP tools for external agents, and can spawn local CLI agents with active-vault context and scoped permission modes.

**Repository:** https://github.com/refactoringhq/tolaria

**Reviewed commit:** [82b2ff2ac455334a255c7c2a2a1d2173083c6d59](https://github.com/refactoringhq/tolaria/commit/82b2ff2ac455334a255c7c2a2a1d2173083c6d59)

**Last checked:** 2026-06-05

## Core Ideas

**The vault is the memory, and the app is a derived view over it.** Tolaria's architecture states that Markdown files with YAML frontmatter are the single source of truth, while cache and React state are reconstructible from the filesystem ([docs/ARCHITECTURE.md](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/docs/ARCHITECTURE.md)). The Rust command layer writes note content and frontmatter back to disk through validated vault boundaries, so retained knowledge remains ordinary files rather than an app-owned database ([src-tauri/src/commands/vault/file_cmds.rs](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src-tauri/src/commands/vault/file_cmds.rs), [src-tauri/src/commands/vault/frontmatter_cmds.rs](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src-tauri/src/commands/vault/frontmatter_cmds.rs)).

**Types and relationships are conventions, not hard schemas.** Standard frontmatter keys such as `type`, `status`, dates, and relationship fields drive sidebar grouping, chips, backlinks, neighborhoods, saved views, and agent legibility, but the README says types are "lenses, not schemas" and the abstractions doc describes relationship fields as dynamically detected wikilink-bearing properties ([README.md](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/README.md), [docs/ABSTRACTIONS.md](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/docs/ABSTRACTIONS.md)).

**Context efficiency is mostly UI selection, lexical search, cache, and truncation.** The vault scanner maintains an external `~/.laputa/cache/<hash>.json` keyed by Git commit and uncommitted changes, while search walks Markdown files and ranks title/content substring matches ([src-tauri/src/vault/cache.rs](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src-tauri/src/vault/cache.rs), [src-tauri/src/search.rs](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src-tauri/src/search.rs)). For AI calls, the context snapshot includes the active note, open tabs, visible note-list items, vault type summary, and explicitly referenced notes, with head/tail truncation and instructions to call `get_note` before content-sensitive work on truncated bodies ([src/utils/ai-context.ts](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src/utils/ai-context.ts)).

**The AI surface is local-agent orchestration plus vault tools, not a learned memory model.** App-managed Claude, Codex, OpenCode, Pi, Gemini, and Kiro sessions are spawned as local CLI subprocesses with safe/power-user permission modes and transient Tolaria MCP configuration ([docs/ARCHITECTURE.md](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/docs/ARCHITECTURE.md), [src-tauri/src/ai_agents.rs](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src-tauri/src/ai_agents.rs), [src-tauri/src/codex_cli.rs](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src-tauri/src/codex_cli.rs)). The MCP server exposes search, vault context, note reading, UI open/highlight, and refresh operations; the current stdio tool list is read/UI oriented rather than a durable autonomous writeback service ([mcp-server/index.js](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/mcp-server/index.js), [mcp-server/vault.js](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/mcp-server/vault.js)).

**Adoption affordance is unusually strong for agent memory.** Notes are plain Markdown, vaults can be Git repositories, Tolaria can register its MCP server with several external clients, and root `AGENTS.md` instructions are discovered and included in vault context ([README.md](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/README.md), [mcp-server/agent-instructions.js](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/mcp-server/agent-instructions.js), [src-tauri/src/mcp.rs](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src-tauri/src/mcp.rs)).

## Artifact analysis

- **Storage substrate:** `files` `repo` `service-object` — The main retained memory is Markdown and frontmatter on disk, usually inside a Git-backed vault; Git state supplies history, changes, sync, and AutoGit surfaces; app-local settings, localStorage, AI workspace session state, MCP child processes, and cache files are installation-level service objects around the vault rather than the canonical knowledge store ([docs/ARCHITECTURE.md](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/docs/ARCHITECTURE.md), [src-tauri/src/settings.rs](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src-tauri/src/settings.rs), [src/lib/aiWorkspaceSessionStore.ts](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src/lib/aiWorkspaceSessionStore.ts)).
- **Representational form:** `prose` `symbolic` — Note bodies, AGENTS guidance, bundled docs, prompts, transcripts, and generated agent replies are prose; YAML frontmatter, type documents, wikilinks, views, cache entries, settings, MCP schemas, CLI permission modes, Git status, and search result records are symbolic. I did not find retained embeddings, vector indexes, model weights, or adapters in this revision.
- **Lineage:** `authored` `imported` — Users and agents author vault notes, type documents, views, guidance files, and chat prompts; Tolaria imports or derives app state from existing vault files, Git status, configured workspaces, selected UI context, and local agent streams. It records AI workspace messages, but I did not find qualifying code that distills session/tool traces into durable rules, lessons, validators, or learned retrieval state.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` — Vault notes and search results serve as knowledge/context; AGENTS files, bundled docs, system prompts, permission prompts, and generated MCP configs instruct agents; types, relationships, workspace aliases, MCP config, CLI adapters, and views route work; vault-boundary checks, cache fingerprints, path validation, permission modes, tests, and Git conflict/status checks validate operations; note-list sorting, search scoring, recent-note ordering, sidebar type order, and Git Pulse ranking influence what gets inspected first.

**Vault notes and type documents.** Markdown files with frontmatter are the core behavior-shaping artifacts. They are readable by humans and external agents, editable outside Tolaria, and consumed through UI panels, search, MCP tools, and active-note context snapshots ([docs/ABSTRACTIONS.md](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/docs/ABSTRACTIONS.md), [mcp-server/vault.js](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/mcp-server/vault.js)).

**Derived cache and search structures.** The cache accelerates startup and incremental scans with Git-aware update paths, but it is disposable and regenerated from the vault. Keyword search is an access layer over Markdown, not an independent semantic memory ([src-tauri/src/vault/cache.rs](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src-tauri/src/vault/cache.rs), [src-tauri/src/search.rs](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src-tauri/src/search.rs)).

**AI prompts, MCP schemas, and permission modes.** Tolaria's agent behavior is shaped by authored prompts that describe vault conventions, docs lookup, safe/power-user scope, MCP tool use, and UI-open expectations. These are system-definition artifacts with instruction and routing authority, but they do not replace the vault as the knowledge source ([src/utils/ai-agent.ts](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src/utils/ai-agent.ts), [mcp-server/index.js](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/mcp-server/index.js)).

**AI workspace sessions.** Conversation messages are persisted in cross-window localStorage plus native settings/session storage for continuity and replay within the workspace, but their authority is conversational context. I did not find a promotion path that turns successful agent behavior into reviewed vault procedures or enforcement rules without an explicit user/agent file edit ([src/lib/aiWorkspaceSessionStore.ts](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src/lib/aiWorkspaceSessionStore.ts), [src/components/aiWorkspaceConversations.ts](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src/components/aiWorkspaceConversations.ts)).

**Promotion path.** Tolaria's implemented promotion path is manual or agent-mediated: a found note, active context, transcript, or search result becomes durable memory only when a human or CLI agent writes a Markdown note/frontmatter update and, optionally, commits it. The system supplies affordances and guardrails rather than automatic semantic promotion.

## Comparison with Our System

Tolaria and Commonplace share the repo-first intuition: retained knowledge should be inspectable text with Git history, not a private service object. Tolaria is a desktop operating surface for arbitrary Markdown vaults; Commonplace is a governed methodology KB with explicit type contracts, validation, review bundles, and curated collection rules. Tolaria makes adoption easier for non-framework vaults because it gives users an editor, search, Git UI, agent panel, MCP setup, and mounted workspace graph. Commonplace gives stronger semantic authority because artifacts are typed, routed through collection contracts, validated, and reviewed.

The biggest divergence is enforcement. Tolaria intentionally treats types as lenses and conventions; Commonplace treats type specs and collection contracts as operational constraints. That makes Tolaria more forgiving and portable, but weaker when an agent needs to know whether a note satisfies a formal review contract or whether a link/tag/status carries assigned consequences.

The read-back model is also different. Commonplace generally relies on explicit agent navigation through `rg`, indexes, skills, and links. Tolaria pushes the current UI context into the agent prompt and provides MCP pull tools for deeper lookup. That is a practical human-in-the-loop context-engineering pattern: the user selects the working locus, and the app turns that selection into a bounded prompt packet.

### Borrowable Ideas

**Active-artifact context snapshots.** Commonplace could borrow Tolaria's active-note snapshot pattern for Roughdraft or review workflows: push the currently reviewed artifact, nearby navigation state, and truncation metadata into an agent prompt, then require explicit full-file reads for sensitive edits. Ready when there is a stable UI or session surface that knows the active artifact.

**Vault-neutral MCP registration.** Tolaria's durable external MCP entry resolves active workspaces at tool-call time instead of baking one vault path into every client config. Commonplace could use this for multi-KB workspaces if it grows a desktop or daemon surface; it needs a concrete host first.

**Conventions as onboarding before contracts.** Tolaria's types-as-lenses model is useful for early, user-authored vaults before a collection contract exists. Commonplace could keep this as a seedling mode, but not as the authority model for mature framework artifacts.

**Disposable cache discipline.** Tolaria's external cache is explicitly reconstructible from filesystem and Git state. Commonplace already has generated indexes; the borrowable rule is to keep every acceleration artifact either reproducible or clearly lower-authority than source notes.

**Do not borrow weak schema authority for reviewed notes.** Tolaria's permissiveness is a feature for personal vaults, but Commonplace's review files need schema and section enforcement. For Commonplace, type lenses should not replace validation.

## Write side

**Write agency:** `manual` `automatic` — Users and app-managed agents manually create, edit, move, delete, link, archive, and commit Markdown files through the UI, file tools, or Git. Automatic writes include autosave, title/frontmatter synchronization, vault cache refresh, AI workspace transcript/session persistence, MCP bridge/config setup on explicit user request, vault guidance restoration, file-operation-triggered reloads, and AutoGit checkpoint/commit workflows ([src-tauri/src/commands/vault/file_cmds.rs](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src-tauri/src/commands/vault/file_cmds.rs), [src-tauri/src/vault/cache.rs](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src-tauri/src/vault/cache.rs), [src/lib/aiWorkspaceSessionStore.ts](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src/lib/aiWorkspaceSessionStore.ts), [src-tauri/src/mcp.rs](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src-tauri/src/mcp.rs)).

**Curation operations:** `none` — The inspected automatic writes are persistence, cache/index upkeep, UI refresh, title synchronization, config registration, transcript storage, and Git checkpointing. I did not find implemented automatic consolidation, deduplication, in-place semantic evolution, synthesis, invalidation history, decay, or salience promotion over existing vault memories under the review vocabulary.

Tolaria does store and replay AI workspace conversation state, and it detects agent file writes so the vault view can refresh ([src/lib/aiAgentFileOperations.ts](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src/lib/aiAgentFileOperations.ts)). That is useful operational state, but it is not trace-learning in the current review sense: I did not find a code path that mines session logs or tool traces into durable lessons, rules, playbooks, validators, rankers, or model updates. Accordingly this review omits the `trace-learning` tag.

## Read-back

**Read-back:** `both` — Tolaria supports pull through UI search, note opening, Git/history views, MCP `search_notes`, `get_vault_context`, `list_vaults`, and `get_note`; it also pushes retained vault memory into app-managed AI calls by embedding the active note, referenced notes, open tabs, note-list slice, and vault summary in the context snapshot before the agent acts ([src/utils/ai-context.ts](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src/utils/ai-context.ts), [src/hooks/useCliAiAgent.ts](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src/hooks/useCliAiAgent.ts), [mcp-server/index.js](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/mcp-server/index.js)).

**Read-back signal:** `identifier` — Push read-back is keyed by explicit UI and prompt identifiers: active note path, open-tab entries, wikilink-style references, visible note-list selection/filter state, and mounted vault roots. Tolaria does not use embeddings or an LLM relevance judge to decide which vault memories to push in the inspected path.

**Faithfulness tested:** `no` — I found tests for context construction, agent streaming, MCP tools, and file-operation refresh, but not an ablation or post-action audit that verifies pushed active-note context changes downstream agent behavior correctly.

The injection point is pre-invocation. `buildContextSnapshot` creates a JSON packet and preamble before `stream_ai_agent` invokes the selected CLI agent; large note bodies are head/tail compacted and the prompt tells the agent to call `get_note` for full content before sensitive edits or summaries ([src/utils/ai-context.ts](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src/utils/ai-context.ts), [src/utils/streamAiAgent.ts](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/src/utils/streamAiAgent.ts)). Selection is bounded by the active UI state, explicit references, `MAX_NOTE_LIST_ITEMS`, and body character caps rather than semantic retrieval budgets.

The authority of pushed memory is advisory context plus instructions. The active note body and related metadata advise the agent; the system prompt carries stronger instruction about vault scope, AGENTS/docs lookup, MCP use, wikilink syntax, and permission mode. External MCP stdio clients remain pull-oriented unless their host independently chooses to call tools and inject the results.

Other consumers include the human user, the React note list/editor/sidebar, external MCP clients, local CLI agents, Git workflows, and Tolaria's own cache/search/watch/reload machinery.

## Curiosity Pass

**The current MCP implementation is more conservative than the architecture table suggests.** The architecture document lists create/edit/delete/link tools, but the inspected stdio server advertises search/context/list/get/open/highlight/refresh only. Actual vault mutation for agents is routed through the selected CLI agent's file/edit/shell permissions, not through a broad MCP write API ([docs/ARCHITECTURE.md](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/docs/ARCHITECTURE.md), [mcp-server/index.js](https://github.com/refactoringhq/tolaria/blob/82b2ff2ac455334a255c7c2a2a1d2173083c6d59/mcp-server/index.js)).

**Tolaria's most interesting memory feature is the UI-mediated push, not retrieval sophistication.** Search is lexical and the cache is mechanical. The distinctive context-engineering move is using the user's active note/workspace selection as a low-cost relevance signal for the next agent call.

**Conversation persistence is not yet learning.** The AI workspace can retain transcripts and titles, but those records do not automatically become vault notes, procedures, link structures, or enforcement rules. Successful agent behavior still has to be written into the vault deliberately.

**Files-first does not mean schema-free in practice.** Tolaria avoids hard validation, yet its UI and prompts create strong soft conventions around `type`, status, wikilinks, AGENTS guidance, Type documents, saved views, and workspace aliases. That is enough for navigation, but not enough for Commonplace-style review authority.

## What to Watch

- Whether Tolaria adds a semantic/vector retrieval layer; that would change read-back signal from identifier/lexical toward inferred embedding or judgment.
- Whether the MCP server grows first-class write/edit tools again; that would move more authority from CLI-agent file permissions into Tolaria's own tool surface.
- Whether AI workspace transcripts gain an accepted-lessons or procedure-promotion workflow; that would make trace-learning relevant.
- Whether Type documents acquire validation rules or required fields; that would shift types from lenses toward enforceable collection contracts.
- Whether AutoGit becomes a review/checkpoint policy with gates rather than a commit convenience; that would strengthen Git history as a governance artifact.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Tolaria's vault memory can be pulled by tools, while active-note snapshots are pushed into app-managed agent calls.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Tolaria separates canonical Markdown files from derived caches, prompts, settings, and service processes.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: Tolaria routes bounded vault context into agents through UI selection, MCP tools, and truncation rules.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: Tolaria prompts, MCP schemas, permission modes, cache rules, and path validators constrain later behavior.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: vault notes, search results, transcripts, and context snapshots advise human and agent action without becoming hard gates.
