---
description: "Tolaria review: local-first markdown/git vault with typed lenses, saved views, managed agent guidance, AI context snapshots, CLI-agent launchers, and MCP tools"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-02"
---

# Tolaria

> Replaced 2026-06-05. See [Tolaria](./tolaria.md) for the current review.

Tolaria is RefactoringHQ's local-first desktop app for managing markdown knowledge bases as git-backed, agent-readable vaults. It is not a memory model or background learner. Its memory relevance comes from productizing the authoring, navigation, activation, and agent-access layers around ordinary files: vault markdown, type documents, saved views, root agent guidance, derived caches, UI context snapshots, git workflows, built-in CLI-agent launchers, and Tolaria MCP tools.

**Repository:** https://github.com/refactoringhq/tolaria

**Reviewed commit:** [6c979addb3dc9ab6e0ef265156e58e4b1026b1c5](https://github.com/refactoringhq/tolaria/commit/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5)

**Last checked:** 2026-06-02

## Core Ideas

**The vault filesystem is the authority boundary.** The architecture states that markdown files on disk are the source of truth and that cache and React state are reconstructible views; the Rust scanner implements this by recursively reading non-hidden vault files, parsing markdown into `VaultEntry` records, classifying editable non-markdown files, recovering pending rename transactions, and sorting entries by modified time ([docs/ARCHITECTURE.md](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/docs/ARCHITECTURE.md), [src-tauri/src/vault/mod.rs](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/src-tauri/src/vault/mod.rs)). Git is a vault capability rather than a hosted sync service: commit, Pulse/history, remotes, conflict checks, and auto-git operate through the user's local repository ([src-tauri/src/git/commit.rs](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/src-tauri/src/git/commit.rs), [src-tauri/src/git/pulse.rs](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/src-tauri/src/git/pulse.rs)).

**Types are navigational lenses, not validation schemas.** Tolaria resolves type from `type:` frontmatter, not folder placement, and type documents can carry icon, color, ordering, sidebar label, templates, sort, view, visibility, pinned/list properties, and defaults ([docs/ABSTRACTIONS.md](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/docs/ABSTRACTIONS.md), [src-tauri/src/vault/frontmatter.rs](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/src-tauri/src/vault/frontmatter.rs)). This gives agents useful conventions without requiring every note category to become a checked contract.

**Relationships are inferred from wikilink-bearing frontmatter.** The frontmatter parser ignores reserved fields, then treats any remaining field whose value contains `[[wikilinks]]` as a relationship. The markdown parser also records body wikilinks, and typed notes get a synthetic `Type` relationship so types become graph nodes ([src-tauri/src/vault/frontmatter.rs](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/src-tauri/src/vault/frontmatter.rs), [src-tauri/src/vault/mod.rs](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/src-tauri/src/vault/mod.rs)). The remembered connection is open-vocabulary and UI-legible; it changes what adjacent material can be surfaced, but it does not define the inference that a relationship authorizes.

**Saved views are persisted activation queries.** Tolaria stores saved views as YAML under `views/*.yml`, with name, icon, color, order, sort, display columns, and nested filter groups; Rust scans, saves, deletes, and evaluates those filters against `VaultEntry` metadata ([src-tauri/src/vault/views.rs](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/src-tauri/src/vault/views.rs)). A view is therefore a symbolic routing artifact over the vault: it decides what the user or agent sees first without changing the underlying notes.

**Managed agent guidance makes vault conventions loadable.** Tolaria can seed and restore root `AGENTS.md` plus `CLAUDE.md` and `GEMINI.md` shims; it classifies managed, missing, broken, and custom guidance before replacement ([src-tauri/src/vault/config_seed.rs](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/src-tauri/src/vault/config_seed.rs)). The managed `AGENTS.md` tells agents how to use H1 titles, `type:` frontmatter, wikilinks, saved views, attachments, underscored system fields, and bundled Tolaria docs. This is stronger than simply storing notes because it gives external agents an instruction artifact at the vault root.

**Context efficiency is UI-scoped, bounded, and progressively recoverable.** The AI context snapshot includes the active note, open tabs, current note list, note-list filter, vault type summary, and explicitly referenced notes, but it caps active note bodies at 24,000 characters, referenced notes at 12,000 characters, and note-list items at 100, inserting instructions to call `get_note` when context is truncated ([src/utils/ai-context.ts](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/src/utils/ai-context.ts), [src/components/useAiPanelContextSnapshot.ts](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/src/components/useAiPanelContextSnapshot.ts)). MCP search and note reads then provide progressive disclosure rather than loading the whole vault.

**The built-in agent launcher is an activation bridge, not a learner.** Tolaria can launch Claude Code, Codex, OpenCode, Pi, Gemini, and Kiro with vault path, active vault set, permission mode, system prompt, and Tolaria MCP config ([src-tauri/src/ai_agents.rs](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/src-tauri/src/ai_agents.rs), [src-tauri/src/codex_cli.rs](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/src-tauri/src/codex_cli.rs), [src-tauri/src/claude_invocation.rs](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/src-tauri/src/claude_invocation.rs)). The frontend builds a system prompt with vault scope, MCP tool instructions, bundled-doc guidance, and Safe/Power User policy, then appends the context snapshot to that prompt ([src/utils/ai-agent.ts](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/src/utils/ai-agent.ts), [src/lib/aiAgentConversation.ts](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/src/lib/aiAgentConversation.ts)).

**MCP is read/orientation plus UI action, not a write API.** The stdio MCP server exposes `search_notes`, `get_vault_context`, `list_vaults`, `get_note`, `open_note`, `highlight_editor`, and `refresh_vault`; its vault helpers search markdown, parse frontmatter, list recent notes, and include `AGENTS.md` instructions in vault context ([mcp-server/index.js](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/mcp-server/index.js), [mcp-server/vault.js](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/mcp-server/vault.js), [mcp-server/agent-instructions.js](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/mcp-server/agent-instructions.js)). UI actions travel through a local WebSocket bridge with loopback/origin checks ([mcp-server/ws-bridge.js](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/mcp-server/ws-bridge.js)).

## Artifact analysis

- **Storage substrate:** `repo` — User-owned vault files on disk, usually in a git repository
- **Representational form:** `prose` `symbolic` — Markdown prose plus symbolic YAML frontmatter, wikilinks, saved-view filters, JSON snapshots, tool schemas, config, git records, and app code
- **Lineage:** `authored` `imported` — Vault artifacts are authored by humans, agents, app save operations, Tolaria-managed templates, imports, migrations, and filesystem/git scans; caches and UI state are derived views
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `ranking` — Notes and git history advise as knowledge; root guidance and prompts instruct; permission/path boundaries enforce; views, links, filters, snapshots, and MCP tools route and order context

**Vault notes and assets.** Storage substrate: user-owned vault files on disk, usually in a git repository. Representational form: markdown prose with YAML frontmatter, wikilinks, editable text files, and binary assets. Lineage: authored by humans, agents, import flows, or app save operations; filesystem content is source-of-truth, while cache and UI state are derived. Behavioral authority: knowledge artifacts when read as evidence/context/reference; soft system-definition artifacts when a note is consumed as a procedure, template, or instruction by an agent or UI path.

**Type documents.** Storage substrate: markdown files, commonly `type/*.md` or root type notes depending on the vault. Representational form: mixed prose and symbolic frontmatter metadata. Lineage: authored or Tolaria-seeded, then parsed into `VaultEntry` metadata and UI configuration. Behavioral authority: system-definition artifacts for grouping, labeling, sorting, defaulting, templates, and display behavior; knowledge artifacts when read as category descriptions. Promotion path is weak: a type can become more behavior-shaping by adding metadata, but Tolaria does not promote it into a schema validator.

**Relationship fields and wikilinks.** Storage substrate: frontmatter values and markdown body text inside vault files. Representational form: symbolic link syntax embedded in prose or YAML. Lineage: authored/imported and parsed during vault scans; regenerated only by edit/rename/link-rewrite operations. Behavioral authority: knowledge artifacts as stated relations; navigation and activation artifacts when Tolaria groups outgoing, inverse, type, or backlink neighborhoods. The vocabulary remains open, so relationship meaning is advisory rather than enforced.

**Saved views.** Storage substrate: YAML files under `views/`. Representational form: symbolic filter trees, sort keys, display columns, and chrome metadata. Lineage: authored through UI or files, migrated from older view formats where applicable, and evaluated against current `VaultEntry` state. Behavioral authority: system-definition artifacts with routing and display authority because they select which notes appear in a view and in what order.

**Root agent guidance files.** Storage substrate: vault-root `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md`. Representational form: prose instructions plus markdown/frontmatter. Lineage: Tolaria-managed templates, repaired shims, or custom user edits; replacement policy depends on managed/custom/broken classification. Behavioral authority: system-definition artifacts when loaded by coding agents or returned in MCP vault context, because they instruct note creation, relationships, saved views, and what agents should avoid.

**Cache and React state.** Storage substrate: external app cache under `~/.laputa/cache/<vault-hash>.json`, localStorage/app settings, and in-memory `VaultEntry[]`. Representational form: symbolic JSON and TypeScript/Rust structs. Lineage: derived from filesystem scans, git HEAD, uncommitted changes, note opens, and watcher events; invalidated by reload, cache version, file identity, and git diffs. Behavioral authority: routing/display/performance authority inside Tolaria, but not canonical knowledge authority.

**AI context snapshots and prompt assembly.** Storage substrate: ephemeral frontend strings passed to model/API/CLI calls. Representational form: prose system prompt plus structured JSON snapshot. Lineage: assembled at send time from active UI state, active note content, visible/open notes, inline wikilink references, vault summaries, permission mode, and bundled-doc paths. Behavioral authority: system-definition artifact for the receiving agent turn; it instructs scope and injects selected context before the model acts.

**MCP server and bridge.** Storage substrate: bundled JavaScript files plus transient MCP config passed to launched agents or registered in external clients. Representational form: symbolic tool definitions, schemas, Node code, JSON/TOML configuration, and WebSocket messages. Lineage: authored application code, runtime vault-path environment, and active vault list. Behavioral authority: read/orientation tool authority for agents, plus UI-action authority for opening/highlighting/refreshing notes. It does not itself create durable note mutations.

**Git history and Pulse.** Storage substrate: the vault `.git` repository and git CLI outputs. Representational form: symbolic commits, refs, status lines, and change records. Lineage: generated from user/app/agent commits and remote operations. Behavioral authority: audit, rollback, sync, and activity context. It is not trace-derived learning because Tolaria does not mine commits or agent sessions into new durable rules, notes, validators, rankings, or policies at this commit.

## Comparison with Our System

| Dimension | Tolaria | Commonplace |
|---|---|---|
| Primary purpose | Desktop app for authoring, browsing, git-syncing, and agent-activating markdown vaults | Methodology KB framework with typed artifacts, validation, reviews, indexes, and operational conventions |
| Canonical substrate | User vault filesystem plus optional git history; cache and settings live outside the vault | Git-tracked `kb/` collections, source snapshots, generated indexes, type specs, review reports, and scripts |
| Type model | Flexible type documents as lenses and defaults | Type specs and collection contracts with stronger validation expectations |
| Activation | Saved views, neighborhoods, search, AI context snapshots, MCP tools, CLI-agent launchers | `rg`, descriptions, authored links, indexes, skills, validation, review bundles, and loaded instructions |
| Agent guidance | Managed root guidance plus shims and bundled Tolaria docs | Repository `AGENTS.md`, collection contracts, skills, instructions, and type specs |
| Trace-derived learning | No durable trace-to-artifact learning found | Treated as a separate methodology axis requiring lineage, authority, and promotion rules |

Tolaria is closest to Commonplace in its files-first instinct: retained artifacts remain inspectable, git history is available, and derived state is rebuildable. The difference is authority. Tolaria favors product ergonomics: lightweight type lenses, flexible relationships, UI filters, and context snapshots. Commonplace favors explicit contracts: collection routing, type specs, validation, semantic review, and curated cross-note connections.

The strongest Commonplace-relevant contribution is the activation layer around local files. Tolaria does not just say "agents can read markdown"; it gives them a managed `AGENTS.md`, a context snapshot from what the user is viewing, MCP read/orientation tools, and CLI launch settings that scope the agent to active vaults.

**Read-back:** `both` — Tolaria exposes pull paths through MCP search/read/context tools and ordinary file/git access, and it implements engineered push activation for built-in AI sessions by injecting a bounded UI-derived snapshot of retained vault notes before the receiving agent acts; bundled Tolaria docs and generic vault instructions are baseline context, not memory read-back

### Borrowable Ideas

**Managed guidance state should distinguish custom, broken, missing, and canonical files.** Ready for Commonplace init/repair workflows. Commonplace already depends on `AGENTS.md`; a repair command could classify whether local guidance is managed, custom, or stale before proposing changes.

**Context snapshots should carry UI/workshop provenance and truncation instructions.** Ready for review and workshop tools. A Commonplace review UI could pass the active artifact, visible related artifacts, selected references, and explicit truncation markers into an agent handoff instead of relying on the agent to infer what the operator was looking at.

**Saved views are a small symbolic activation layer.** Needs a concrete use case. Commonplace could support YAML-defined note sets for workshops, review queues, or reading paths, but they should be validated and classified as system-definition artifacts rather than ordinary notes.

**Neighborhood mode is useful even without a graph database.** Ready as a report command. Commonplace could generate local neighborhoods from outbound links, backlinks, shared tags, and index membership around one artifact, preserving file-first storage while improving activation.

**Permission modes should be tied to artifact authority.** Needs design work. Tolaria's Safe/Power User modes map to CLI flags and shell access; Commonplace sub-agent launchers could use analogous modes tied to writable collections, validation expectations, and whether generated artifacts may become instructions.

**Do not borrow flexible type lenses as a substitute for contracts.** Tolaria's type system is excellent for adoption and UI grouping, but Commonplace's methodology notes and instructions need stronger checkable obligations. Borrow lenses for browsing; keep schemas/contracts for behavior-shaping artifacts.

## Write-side placement

**Write agency:** `automatic` `manual` — the review describes system-driven generation, extraction, consolidation, or update of retained artifacts rather than only manual authoring.

**Curation operations:** `consolidate` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

## Read-back placement

**Direction.** Tolaria is both pull and push. Pull comes from MCP `search_notes`, `get_vault_context`, `list_vaults`, and `get_note`, plus normal file/git access. Push comes from the built-in AI panel and CLI-agent launch path: the user opens an AI session, and Tolaria injects active vault memory from the UI context before the receiving agent responds. The same prompt path also includes shipped Tolaria product docs and generic vault-use instructions, but those are baseline context surfaces rather than read-back.

**Read-back signal:** `identifier` `inferred / lexical` — pushed memory keys on active note path, open-tab paths, note-list type/filter state, and inline wikilink references; a visible note list narrowed by free-text UI query adds lexical inference.

**Faithfulness tested:** `no` — the review found structure, prompt, truncation, and launcher tests, but no ablation showing that injected UI context changes downstream behavior.

**Targeting and signal.** Targeting is `instance`: the pushed memory is selected for the current UI instance rather than always loaded. The primary signal is `identifier`, because the snapshot keys on active note path, open-tab paths, note-list type/filter state, and inline wikilink references already present in the user interface. If the visible note list was narrowed by a free-text UI query, that sub-path is `inferred / lexical`; the implemented push path itself does not use embedding retrieval or an LLM relevance judge. Precision/recall quality and context dilution are not verifiable from code, but the selection mechanism is implemented.

**Injection point.** The snapshot and agent system prompt are built before `sendAgentMessage()` streams the selected target, and the Rust launchers pass the resulting prompt/system prompt into the external CLI or model call. This can change the next action, not merely summarize it afterward ([src/lib/aiAgentConversation.ts](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/src/lib/aiAgentConversation.ts), [src/utils/streamAiAgent.ts](https://github.com/refactoringhq/tolaria/blob/6c979addb3dc9ab6e0ef265156e58e4b1026b1c5/src/utils/streamAiAgent.ts)).

**Selection, scope, and complexity.** Selection is bounded by `MAX_ACTIVE_NOTE_BODY_CHARS`, head/tail truncation, `MAX_REFERENCED_NOTE_BODY_CHARS`, `MAX_NOTE_LIST_ITEMS`, active vault paths, and explicit `vaultPath` disambiguation for MCP tools. Complexity remains moderate: the agent receives one structured JSON snapshot and can pull fuller notes through MCP when needed rather than receiving the whole vault.

**Authority at consumption.** The context snapshot is advisory but arrives through the system prompt path, so it has stronger practical authority than a note the agent may or may not search for. MCP outputs are advisory context. Permission-mode instructions and CLI sandbox flags have system-definition authority over allowed action channels, although final enforcement depends on the selected agent and platform.

**Faithfulness.** I found tests for snapshot structure, prompt formatting, references, truncation, and CLI argument construction, but not an ablation showing that injected UI context reliably improves or changes agent behavior. The `push-activation` tag rests on the implemented pre-action activation mechanism, not on measured downstream faithfulness.

**Other consumers.** Human users consume the same retained artifacts through Tolaria's sidebar, note list, editor, right panel, Pulse, search, and saved views. The same files can be knowledge artifacts for humans, system-definition artifacts for Tolaria, and instructions for agents depending on the consumption path.

## Curiosity Pass

**The product is more interesting as an activation surface than as storage.** Markdown-plus-git is familiar; the distinctive part is how Tolaria turns the user's current UI state into an agent prompt and pull-tool surface.

**MCP write authority is deliberately absent in the reviewed server.** The server can open, highlight, refresh, search, list, and read. Durable edits come from native app commands or the selected CLI agent's own file-edit tools, so MCP should not be described as the write substrate.

**Types as lenses are a strength and a ceiling.** They make a vault easy to start and easy for agents to browse, but the lack of required fields or validation means type membership alone cannot support high-trust agent behavior.

**Git activity is audit, not learning.** Pulse and commit history expose what changed, but no inspected code derives durable lessons, rules, saved views, guidance edits, or ranking weights from those changes.

**The active-vault boundary is clearer inside Tolaria than outside it.** Tauri command paths and MCP vault path checks are explicit. External agents in Power User modes still rely on the host agent's sandbox and Tolaria's prompt/config choices, so authority is shared rather than fully enforced by Tolaria.

## What to Watch

- Whether Tolaria adds MCP write tools; that would materially change the artifact-authority story from read/orientation to direct mutation.
- Whether type documents gain validation or required-field semantics; that would move them from lenses toward schemas and make them closer to Commonplace type specs.
- Whether AI chat/tool traces are ever distilled into durable notes, `AGENTS.md` guidance, type templates, saved views, rankings, or policies; that would change the `trace-derived` decision.
- Whether saved views gain provenance, review status, or generated-view lineage as they become more central to agent activation.
- Whether the Safe/Power User contract stays aligned across Claude Code, Codex, OpenCode, Pi, Gemini, Kiro, direct model targets, and external MCP clients.

Relevant Notes:

- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: ordinary vault notes, git history, Pulse entries, MCP-read note contents, and UI neighborhoods when consumed as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: type documents, saved views, root guidance files, prompt assembly, permission modes, MCP configs, and path-boundary code when they instruct, route, configure, or enforce behavior.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - sharpens: the same markdown or YAML surface has different force depending on whether a human reads it, Tolaria renders it, or an agent is instructed by it.
- [Storage substrate](../../notes/definitions/storage-substrate.md) - applies: Tolaria separates canonical vault files, external app settings, external cache, runtime React state, MCP subprocesses, and git history.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: Tolaria's memory effect comes from saved views, neighborhoods, context snapshots, and MCP tools, not from storing markdown alone.
