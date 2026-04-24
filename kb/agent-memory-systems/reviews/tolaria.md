---
description: "Mac desktop markdown-vault app with git-backed local files, type documents, neighborhood browsing, CLI-agent panel, and lightweight MCP tools for agent vault access"
type: ../types/agent-memory-system-review.md
traits: [has-comparison, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-04-24"
---

# Tolaria

Tolaria is a Mac desktop app from RefactoringHQ for operating markdown knowledge bases as local, git-backed vaults. At the reviewed commit, it is not primarily an autonomous memory learner: it is a filesystem-first knowledge workspace with conventions, typed note surfaces, git workflows, a local AI-agent panel, and MCP tools that let Claude Code, Codex, Cursor, or another local assistant read and navigate the same vault. The strongest relevance to commonplace is its productized answer to the "human note substrate plus agent access" problem: keep the user's markdown files authoritative, make convention-heavy metadata legible in the UI, and give agents a thin, explicit tool surface rather than a separate memory database.

**Repository:** https://github.com/refactoringhq/tolaria

**Reviewed commit:** https://github.com/refactoringhq/tolaria/commit/ba5c16501619c40c6c09545a1ea5bbe508a94602

## Core Ideas

**Filesystem and git are the memory substrate.** The README's principles are implemented in the Rust backend: `scan_vault` walks the active vault, ignores hidden directories, parses markdown and editable non-markdown files into `VaultEntry` records, and treats the cache and React state as rebuildable projections over disk ([README.md](https://github.com/refactoringhq/tolaria/blob/ba5c16501619c40c6c09545a1ea5bbe508a94602/README.md), [docs/ARCHITECTURE.md](https://github.com/refactoringhq/tolaria/blob/ba5c16501619c40c6c09545a1ea5bbe508a94602/docs/ARCHITECTURE.md), [src-tauri/src/vault/mod.rs](https://github.com/refactoringhq/tolaria/blob/ba5c16501619c40c6c09545a1ea5bbe508a94602/src-tauri/src/vault/mod.rs)). Git is first-class operational state: commits, pull/push, remote connection, conflicts, and Pulse activity are shell-outs to the user's system `git`, not a hosted sync layer ([src-tauri/src/git/commit.rs](https://github.com/refactoringhq/tolaria/blob/ba5c16501619c40c6c09545a1ea5bbe508a94602/src-tauri/src/git/commit.rs), [docs/ARCHITECTURE.md](https://github.com/refactoringhq/tolaria/blob/ba5c16501619c40c6c09545a1ea5bbe508a94602/docs/ARCHITECTURE.md)). This is a real files-first implementation, not a virtual filesystem over service storage.

**Types are lenses rather than validators.** `type:` frontmatter drives sidebar grouping, chips, instances, and the implicit Type relationship, while type documents carry UI metadata such as icon, color, sort, view, visibility, and templates ([docs/ABSTRACTIONS.md](https://github.com/refactoringhq/tolaria/blob/ba5c16501619c40c6c09545a1ea5bbe508a94602/docs/ABSTRACTIONS.md), [src-tauri/src/vault/mod.rs](https://github.com/refactoringhq/tolaria/blob/ba5c16501619c40c6c09545a1ea5bbe508a94602/src-tauri/src/vault/mod.rs)). The README is explicit that Tolaria types are navigation aids, not enforced schemas. That makes them cheaper for casual personal use but much weaker than commonplace types as authoring contracts: a Project type changes the UI path and grouping, not the permitted or required document structure.

**Relationship fields are dynamic wikilink properties.** Tolaria recognizes any frontmatter key whose value contains `[[wikilinks]]` as a relationship, with common conventions like `belongs_to`, `related_to`, and `has` but no fixed relation vocabulary ([docs/ARCHITECTURE.md](https://github.com/refactoringhq/tolaria/blob/ba5c16501619c40c6c09545a1ea5bbe508a94602/docs/ARCHITECTURE.md), [docs/ABSTRACTIONS.md](https://github.com/refactoringhq/tolaria/blob/ba5c16501619c40c6c09545a1ea5bbe508a94602/docs/ABSTRACTIONS.md)). The UI turns these relationships into Neighborhood mode: outgoing groups, inverse groups, backlinks, and duplicate-preserving grouped browsing. This is an important middle ground between Obsidian-style untyped links and commonplace's stricter link labels: relationship labels are user-extensible and UI-visible, but their semantics are not governed by collection-local contracts.

**The cache is a disposable derived index with concurrency discipline.** `scan_vault_cached` stores `VaultEntry[]` outside the vault in `~/.laputa/cache/<hash>.json`, keys it by vault path, cache version, and git HEAD, and uses `git status` / `git diff old..new --name-only` to reparse only changed files ([src-tauri/src/vault/cache.rs](https://github.com/refactoringhq/tolaria/blob/ba5c16501619c40c6c09545a1ea5bbe508a94602/src-tauri/src/vault/cache.rs)). The write path uses a lock file, temp file, fsync, rename, and fingerprint check so competing windows do not stampede the cache. This is one of the repo's cleanest engineering choices: it gets database-like startup performance without moving authority out of the files.

**Agent integration is a thin panel plus local tools, not a separate memory service.** The AI panel builds a JSON context snapshot from the active note, open tabs, visible note list, vault types, and explicit chat wikilink references ([src/utils/ai-context.ts](https://github.com/refactoringhq/tolaria/blob/ba5c16501619c40c6c09545a1ea5bbe508a94602/src/utils/ai-context.ts)). The Rust layer can spawn Claude Code or Codex CLI, passes Tolaria's MCP server to Codex via transient config, and streams normalized text/thinking/tool events back into the UI ([src-tauri/src/ai_agents.rs](https://github.com/refactoringhq/tolaria/blob/ba5c16501619c40c6c09545a1ea5bbe508a94602/src-tauri/src/ai_agents.rs)). The MCP stdio server exposes search, vault context, note read, UI open/highlight, and refresh operations; the WebSocket bridge exposes similar read/search/context/UI actions on localhost with origin checks ([mcp-server/index.js](https://github.com/refactoringhq/tolaria/blob/ba5c16501619c40c6c09545a1ea5bbe508a94602/mcp-server/index.js), [mcp-server/ws-bridge.js](https://github.com/refactoringhq/tolaria/blob/ba5c16501619c40c6c09545a1ea5bbe508a94602/mcp-server/ws-bridge.js), [src-tauri/src/mcp.rs](https://github.com/refactoringhq/tolaria/blob/ba5c16501619c40c6c09545a1ea5bbe508a94602/src-tauri/src/mcp.rs)). Despite the architecture doc's larger "14 tools" table, the checked-in stdio tool list is currently six tools, and create/edit/delete/link are mostly left to the agent's normal filesystem abilities.

**Vault-level AGENTS.md is treated as managed guidance.** Tolaria seeds or restores an `AGENTS.md` note that explains vault conventions to agents: H1 title discipline, `type:` frontmatter, relationships, wikilinks, YAML saved views, and what not to touch ([src-tauri/src/vault/getting_started.rs](https://github.com/refactoringhq/tolaria/blob/ba5c16501619c40c6c09545a1ea5bbe508a94602/src-tauri/src/vault/getting_started.rs), [src-tauri/src/vault/config_seed.rs](https://github.com/refactoringhq/tolaria/blob/ba5c16501619c40c6c09545a1ea5bbe508a94602/src-tauri/src/vault/config_seed.rs)). This is more than documentation: the app classifies managed, missing, broken, and custom guidance files and avoids overwriting custom guidance. The agent contract is therefore part of the vault, not only part of app docs.

**Saved views are query files, not hidden app state.** Tolaria stores saved filters in `views/*.yml`, parses nested `all`/`any` filter trees, and evaluates them against built-in fields, custom frontmatter, body content, favorite state, and dates ([src-tauri/src/vault/views.rs](https://github.com/refactoringhq/tolaria/blob/ba5c16501619c40c6c09545a1ea5bbe508a94602/src-tauri/src/vault/views.rs)). This extends the files-first stance from notes into UI navigation: a view is a portable artifact an agent can edit.

## Comparison with Our System

| Dimension | Tolaria | Commonplace |
|---|---|---|
| Primary substrate | User-owned markdown vault plus git | Repo-owned markdown KB plus git |
| System shape | Desktop app with Rust scanner/cache, React editor, AI panel, MCP server | Methodology repo with CLI validators, indexes, skills, and review workflow |
| Type model | Frontmatter `type:` as UI lens and grouping key | Path-valued type specs as structural authoring contracts |
| Link model | Wikilinks plus dynamic frontmatter relationship fields | Markdown links with collection-authorized labels and context phrases |
| Retrieval | Keyword scan/search, note list filters, Neighborhood mode, MCP `search_notes` | `rg`, generated indexes, typed links, descriptions, connect/review workflows |
| Agent contract | Seeded `AGENTS.md`, active-note context snapshot, MCP read/search/UI tools | `AGENTS.md`, collection conventions, skills, validators, review system |
| Learning loop | Human/agent edits files; no automatic trace-to-memory extraction | Human/agent distillation into notes, ADRs, reviews, and instructions |
| Governance | Filesystem boundary checks, managed guidance detection, cache rebuild invariants | Structural validation, semantic review, type conventions, link contracts |

The strongest alignment is substrate discipline. Tolaria and commonplace both treat plain files as the source of truth and use derived state only for speed or UX. Tolaria is more productized around a human operator: BlockNote editing, note windows, Pulse view, git sync UI, conflict banners, onboarding, and local AI-agent chat. Commonplace is stronger as a methodology engine: types have verifiable shapes, link labels have reader-need semantics, reviews are governed by type-specific instructions, and validation operates on the knowledge artifact rather than only on app state.

The deepest divergence is the meaning of "type." Tolaria's type is an entity category: Person, Project, Quarter, Topic. It helps users and agents route, but it intentionally does not enforce required fields or sections. Commonplace's type is closer to a callable interface: an `agent-memory-system-review` must have known sections, freshness metadata, and repo-grounded citations. Tolaria's choice is right for a broad personal vault because schemas would punish capture. It is too weak for a methodology KB where type assignment must constrain authoring and review.

Tolaria is also narrower than several reviewed "memory systems." It does not run background reflection over chat transcripts, maintain vector memories, deduplicate facts, or promote traces into learned rules. The local AI panel is an activation surface over the vault, not a learning loop. That makes Tolaria closer to Napkin, Hyalo, engraph, and GBrain's vault-facing side than to ClawVault, Hindsight, OpenViking, or ExpeL.

The useful contrast with commonplace is UI ownership. Commonplace assumes the agent operates directly in the repo with shell tools and small CLIs. Tolaria assumes a human wants a desktop cockpit while agents operate as local assistants through the same files. That makes Tolaria a strong reference for the parts of commonplace we have mostly left implicit: file-backed views, agent-visible guidance restoration, and ergonomic navigation around a flat vault.

## Borrowable Ideas

**Treat derived indexes as disposable but engineer their write path seriously.** Commonplace already has generated indexes, but Tolaria's cache has better concurrency hygiene: versioning, git-head checks, changed-file reparsing, stale-entry pruning, lock file, temp write, fsync, rename, and fingerprint guard. A future commonplace operational cache should copy this posture. *Ready to borrow when we add a cache; not needed for current static indexes.*

**Make agent guidance a managed vault artifact with custom-preservation states.** Tolaria's `AGENTS.md` classification is a concrete pattern: managed/missing/broken/custom plus a restore path that does not overwrite custom guidance. Commonplace currently treats `AGENTS.md` as repo guidance, but installed consuming KBs could benefit from the same restoration policy. *Ready to borrow for `commonplace-init` and skill installation.*

**Represent saved views as editable YAML files.** Tolaria's `views/*.yml` files are readable by the app and by agents. Commonplace indexes are mostly generated navigation artifacts; we do not have first-class "saved queries" or "review work queues" as files. A YAML view format could make recurring review targets and note subsets inspectable without embedding them in scripts. *Needs a use case first; the review system already has selectors, but their user-facing representation is thinner.*

**Neighborhood mode as grouped local navigation.** Tolaria's duplicate-preserving grouped view around one entity is more ergonomic than a raw backlink list. For commonplace, a `commonplace-neighborhood <note>` command could group outgoing typed links, backlinks, same-tag notes, same-type siblings, and review warnings. *Ready as a CLI/report idea; not a core storage change.*

**Context snapshot as a UI-to-agent boundary.** The AI panel's structured JSON snapshot is modest but useful: active note, frontmatter, body, open tabs, note list, filter, vault type list, explicit references. Commonplace agents reconstruct this context ad hoc from files and tool output. A typed "current work context" artifact for workshops could reduce prompt clutter and make handoffs clearer. *Needs a workshop-layer use case first.*

**Crash-safe note rename transactions.** Tolaria stages content, writes a manifest, moves the old note to backup, persists the new file with no-clobber semantics, and recovers incomplete transactions on scan ([src-tauri/src/vault/rename_transaction.rs](https://github.com/refactoringhq/tolaria/blob/ba5c16501619c40c6c09545a1ea5bbe508a94602/src-tauri/src/vault/rename_transaction.rs)). Commonplace already routes renames through `commonplace-relocate-note`; if that grows more automated, this transaction pattern is worth copying. *Ready to borrow for safer relocate internals.*

## Curiosity Pass

**The docs still overstate the MCP write surface.** `docs/ARCHITECTURE.md` lists tools such as `create_note`, `append_to_note`, `edit_note_frontmatter`, `delete_note`, `link_notes`, and `list_notes`. The actual `mcp-server/index.js` exports six stdio tools: search, vault context, get note, open note, highlight, refresh. `ws-bridge.js` exposes read/search/context plus UI actions, but not create/edit/delete/link. The implementation comment says write operations are handled by the agent's native bash/write/edit tools. That is a reasonable design, but the docs blur whether Tolaria is a vault-editing MCP server or a vault-orientation server.

**The app is files-first, but the in-app agent path still centralizes context construction.** A normal external agent can `rg` and edit the vault. The AI panel instead receives a fixed context snapshot and a Tolaria MCP config. That is useful for UX, but it reintroduces a product-defined retrieval boundary: what the panel includes, omits, or truncates matters. The current snapshot is simple enough to inspect, which is good; it is not yet a full context-engineering layer.

**Types as lenses are a deliberate refusal of schemas.** Tolaria says types are not schemas, and the code follows through. This makes the system approachable for personal knowledge, but it means the type system cannot carry quality obligations. If a vault wants "Project" to require sponsor, goal, status, and next action, that is guidance in `AGENTS.md` or custom convention, not validation. The upside is low-friction capture; the downside is that agents cannot trust type names as strongly as they can in commonplace.

**Relationship semantics are UI-legible but not argument-legible.** Dynamic wikilink properties make the graph easy to extend. A user can create `depends_on`, `sponsors`, or `blocked_by` without code changes. But because relation labels are not tied to reader needs or collection contracts, an agent can know that two notes are connected without knowing what inference the connection authorizes. This is enough for navigation and Neighborhood browsing, weaker for methodological argument.

**There is no trace-derived learning mechanism.** Tolaria can host OpenClaw/assistant memories as markdown files, and its AI panel can spawn agents that modify a vault. But the checked-in code does not automatically mine agent transcripts, tool traces, chat history, or git events into durable learned artifacts. AutoGit checkpoints and Pulse preserve activity; they do not distill it. Tolaria should therefore stay out of the trace-derived learning bucket unless a future release adds session-to-note extraction, reflection, or rule promotion.

## What to Watch

- Whether the MCP server grows the write tools described in the architecture doc, or the docs narrow to the actual orientation-only tool surface.
- Whether Tolaria adds validation for type documents or keeps the "types as lenses" doctrine intact.
- Whether the AI panel starts persisting conversations, summarizing sessions, or promoting agent actions into notes; that would change its trace-derived learning placement.
- Whether saved views become a general query/work-queue substrate that agents can rely on, rather than mostly UI filters.
- Whether the `AGENTS.md` restoration flow becomes configurable per vault or per type, which would make Tolaria a stronger reference for packaged agent instructions.
- Whether search stays keyword-only or adds derived indexes; the current files-first stance is clean, but 10,000+ note vaults will keep pressuring retrieval.

---

Relevant Notes:

- [files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) — exemplifies: Tolaria is a genuine product implementation of files plus git as the authoritative knowledge substrate
- [types give agents structural hints before opening documents](../../notes/types-give-agents-structural-hints-before-opening-documents.md) — contrasts: Tolaria types route and group notes, while commonplace types also constrain valid operations and structure
- [document types should be verifiable](../../notes/document-types-should-be-verifiable.md) — contrasts: Tolaria explicitly rejects schema enforcement, making its types useful lenses but weak quality contracts
- [agents navigate by deciding what to read next](../../notes/agents-navigate-by-deciding-what-to-read-next.md) — extends: Neighborhood mode and note-list context are UI-level supports for the agent's read/skip decision
- [pointer design tradeoffs in progressive disclosure](../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) — exemplifies: type chips, snippets, relationship groups, and context snapshots are Tolaria's pointer layer
- [agent memory is a crosscutting concern, not a separable niche](../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — exemplifies: Tolaria solves storage and activation surfaces but leaves learning to human/agent editing
- [a functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — foreshadows: Tolaria's AI panel context snapshot and git Pulse are workshop-adjacent state, but not yet a promotion system
- [Napkin](./napkin.md) — sibling: both adapt markdown vaults for agent use; Napkin emphasizes agent-shaped retrieval, Tolaria emphasizes desktop UX plus local CLI-agent integration
- [Hyalo](./hyalo.md) — sibling: both are local-first markdown-vault tools with derived indexes and Claude bootstrap paths; Hyalo is CLI-first, Tolaria is desktop-app-first
- [engraph](./engraph.md) — sibling: both expose a human note substrate to agents; engraph adds SQLite hybrid indexing and section-level writes, while Tolaria stays closer to filesystem scans and UI navigation
- [GBrain](./gbrain.md) — contrast: both use markdown plus agent guidance, but GBrain routes integrations and trace ingestion into compiled domain pages; Tolaria provides the vault cockpit without a comparable ingestion/dream loop
