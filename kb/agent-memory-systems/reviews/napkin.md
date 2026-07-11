---
description: "Napkin review: local Markdown/Obsidian vault CLI and SDK with progressive overview, BM25 search, read, templates, and file writes"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
---

# napkin

napkin, by Michaelliv, is a TypeScript CLI and SDK for operating a local Markdown/Obsidian-compatible vault as agent memory. At the reviewed commit it implements vault initialization, templates, overview generation, BM25-style search through MiniSearch, file CRUD, daily notes, tags, properties, tasks, links, bases, canvases, bookmarks, and structured JSON/quiet output. The durable memory is ordinary local files; the agent-facing design is progressive disclosure rather than automatic conversation memory.

**Repository:** https://github.com/Michaelliv/napkin

**Reviewed commit:** [ffd2b04c628e0ccf946002909dbe36a5c751a473](https://github.com/Michaelliv/napkin/commit/ffd2b04c628e0ccf946002909dbe36a5c751a473)

**Last checked:** 2026-06-04

## Core Ideas

**The vault is the memory substrate.** Napkin stores user and agent memory as normal files under the project or vault root, with `.napkin/config.json` for configuration and `.obsidian/` files generated for Obsidian compatibility. The SDK's constructor calls `findVault`, which either discovers a `.napkin` directory or creates a bare vault with `.napkin/`, `.obsidian/`, and `NAPKIN.md` in the starting directory ([src/sdk.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/sdk.ts), [src/utils/vault.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/utils/vault.ts), [src/utils/config.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/utils/config.ts)).

**Progressive disclosure is implemented as a tool sequence.** The README advertises four levels: `NAPKIN.md`, `napkin overview`, `napkin search`, and `napkin read`. In code, `overview` reads `NAPKIN.md` when present and returns a folder map; `search` returns ranked files and snippets; `read` returns full file content. The CLI human output also prints workflow hints that nudge an agent from overview to search to read ([README.md](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/README.md), [src/core/overview.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/core/overview.ts), [src/commands/overview.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/commands/overview.ts), [src/commands/search.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/commands/search.ts), [src/commands/crud.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/commands/crud.ts)).

**Context efficiency is lexical and staged, not vector or graph based.** `overview` groups Markdown files by folder, extracts tags and TF-IDF keywords from filenames, frontmatter, headings, and body text, and skips internal folders. `search` builds or loads a MiniSearch index over Markdown filenames and content, boosts basenames, allows fuzzy/prefix matching, adds backlink and recency boosts, and returns match-line snippets with configurable context. Search cache state is a derived JSON artifact under `.napkin/search-cache.json`; content is re-read for snippets so the cache does not store full note bodies ([src/core/overview.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/core/overview.ts), [src/core/search.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/core/search.ts), [src/utils/search-cache.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/utils/search-cache.ts), [docs/overview-keyword-extraction.md](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/docs/overview-keyword-extraction.md)).

**The write surface is local file editing through typed commands.** Napkin can create, read, append, prepend, move, rename, delete-to-trash, update frontmatter properties, manage daily notes, toggle tasks, create bases and canvases, and scaffold template directories. These operations mutate the vault directly; there is no background daemon, remote memory service, LLM summarizer, automatic contradiction handling, or entry-level review state in the core package ([src/core/crud.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/core/crud.ts), [src/core/daily.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/core/daily.ts), [src/core/properties.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/core/properties.ts), [src/core/tasks.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/core/tasks.ts), [src/core/init.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/core/init.ts)).

**Adoption affordances are strong because the system stays boring.** The package exposes a CLI and a data-returning SDK, avoids `console.log` and `process.exit` in core modules, supports `--json` and `-q`, and uses Obsidian-compatible Markdown, wikilinks, frontmatter, Bases YAML, JSON Canvas, bookmarks, and templates. That makes the memory inspectable and scriptable, but leaves semantic quality to the operator or host agent ([README.md](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/README.md), [src/sdk.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/sdk.ts), [src/core/core.test.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/core/core.test.ts), [src/utils/bases.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/utils/bases.ts), [src/core/canvas.ts](https://github.com/Michaelliv/napkin/blob/ffd2b04c628e0ccf946002909dbe36a5c751a473/src/core/canvas.ts)).

## Artifact analysis

- **Storage substrate:** `files` `in-memory` — The central retained state is local Markdown and Obsidian-compatible files plus `.napkin/config.json`, `.obsidian/` settings, templates, bases, canvases, bookmarks, and `.napkin/search-cache.json`; Bases queries construct an in-memory SQLite database from vault files at query time rather than persisting a database.
- **Representational form:** `prose` `symbolic` — Markdown note bodies and `NAPKIN.md` are prose; frontmatter, wikilinks, tags, task checkboxes, config JSON, search-cache JSON, Base YAML, Canvas JSON, templates, CLI options, and SDK return types are symbolic. The inspected code does not implement embeddings, model weights, or another parametric retained form.
- **Lineage:** `authored` `imported` — Normal vault content is authored by humans or agents through file editing and CLI/SDK write calls; templates and scaffolds are authored package artifacts; benchmark scripts can import external conversation datasets into temporary Markdown notes, but core Napkin does not derive durable memory from live agent traces.
- **Behavioral authority:** `knowledge` `routing` `ranking` `validation` — Notes, daily entries, tags, links, tasks, and properties serve as knowledge artifacts for agents and humans; folder/template/config structure routes where content goes and how overviews are built; MiniSearch, backlinks, recency, TF-IDF keywords, and optional Base queries rank and select recall surfaces; file resolution, ambiguity errors, malformed-frontmatter warnings, and config parsing provide structural validation.

**Vault content.** Storage substrate: Markdown files under the vault root, excluding `.napkin/`, `.obsidian/`, `.git/`, `.trash/`, `.nanny/`, and `node_modules`. Representational form: prose notes with symbolic frontmatter, tags, links, tasks, headings, and filenames. Lineage: authored or imported by the user, agent, script, or benchmark harness. Behavioral authority: knowledge and advice when read by an agent; stronger instruction only when a host agent chooses to treat a note such as `NAPKIN.md` as context instructions.

**Overview artifacts.** Storage substrate: computed command output, not a durable index file. Representational form: symbolic folder records plus prose-ish keyword strings and optional `NAPKIN.md` context. Lineage: derived from current vault file contents, frontmatter, headings, tags, and paths on each overview call. Behavioral authority: routing and knowledge; it orients the agent toward folders and candidate search terms.

**Search index and snippets.** Storage substrate: `.napkin/search-cache.json` plus live file reads. Representational form: symbolic serialized MiniSearch index, document metadata, backlink counts, and snippet line records. Lineage: derived from Markdown paths and mtimes; the fingerprint invalidates the cache when files are added, removed, or modified. Behavioral authority: ranking and routing for pull retrieval.

**Config, templates, and Obsidian sync.** Storage substrate: `.napkin/config.json`, generated `.obsidian/*.json`, package template definitions, and scaffolded template files. Representational form: symbolic JSON/TypeScript plus prose template content. Lineage: authored package defaults or user-edited config. Behavioral authority: routing and validation, because they set overview depth, keyword count, search limit, snippet lines, daily note paths, template folders, graph renderer, and Obsidian integration defaults.

**Bases and graph-like surfaces.** Storage substrate: `.base` YAML and Markdown/wiki-link files; the SQLite database for Base queries is in-memory. Representational form: symbolic YAML, formula/filter expressions, SQL translation, tags, links, backlinks, and embeds. Lineage: authored Base files and derived query views over current vault files. Behavioral authority: ranking, routing, and knowledge for human/agent inspection, not autonomous memory activation.

Promotion path: Napkin can move from bare prose notes to more structured Markdown through frontmatter, tags, links, tasks, properties, Bases, canvases, and templates. It can also build derived overview/search surfaces from those files. It does not promote memories into semantic validators, enforced gates, learned rules, or automatic trace-derived skills.

## Comparison with Our System

| Dimension | napkin | Commonplace |
|---|---|---|
| Primary purpose | Local-first Markdown/Obsidian vault operations for agents and humans | Typed methodology KB for agent-operated knowledge-base design |
| Main artifact | Free-form Markdown vault plus Obsidian-compatible metadata | Typed Markdown artifacts governed by collection/type contracts |
| Write path | CLI/SDK file operations and template scaffolds | Agent/human edits, skills, validation, semantic review, indexes |
| Read path | Pull sequence: overview, search, read, links, bases | Pull through `rg`, indexes, links, skills, and curated navigation |
| Governance | Filesystem errors, config defaults, ambiguity checks, tests, simple frontmatter warnings | Type validation, link checks, collection contracts, review gates, source citations |

Napkin and Commonplace share the bet that local files are a good memory substrate for agents: they are inspectable, versionable, editable, and easy to operate without a hosted service. Napkin optimizes for a broad personal/project vault with Obsidian compatibility and simple CLI affordances. Commonplace optimizes for artifact types, source-grounded claims, validation, and review status.

The main divergence is authority. Napkin provides useful memory access tools but leaves the meaning of each note mostly unconstrained. Commonplace spends more machinery on what kind of artifact a file is, how it should be written, what links mean, and which checks must pass before it should guide future agents.

Napkin is also deliberately pull-oriented in the inspected package. A host such as Pi could inject overview context or distill conversations, and the docs reference that ecosystem, but the Napkin repo itself implements the local store and retrieval/write surface rather than an always-on read-back loop.

### Borrowable Ideas

**Default search snippets to match-only lines.** Ready now for agent-facing tools. Napkin's `snippetLines: 0` default is a good reminder that agents often need dense evidence lines before they need surrounding prose.

**Hide relevance scores unless debugging.** Ready as a UI principle. Napkin still ranks by score but hides the number unless `--score` is passed, reducing the chance that an agent treats a numeric rank as stronger evidence than the snippet.

**Make every tool output teach the next move.** Ready for CLIs. The overview/search hints are lightweight progressive disclosure for workflow, not only content. Commonplace command output could use this where users or agents regularly stall after an index-like result.

**Keep the SDK side effect discipline.** Ready now. Napkin's split between core data-returning functions and CLI output wrappers is a useful shape for Commonplace commands that should be callable by agents without scraping terminal prose.

**Do not borrow weak semantic governance.** Napkin's freedom is an adoption strength, but Commonplace should not relax typed frontmatter, link contracts, validation, and review gates for library artifacts.

## Write side

**Write agency:** `manual` — Napkin changes the store when a user, agent, script, or host explicitly calls create, append, prepend, move, rename, delete, property, task, daily, template, base, canvas, bookmark, init, or config operations. The inspected core package does not implement automatic curation over already-stored memories.

## Read-back

**Read-back:** `pull` — Core Napkin memory re-enters an agent's context when the agent or host explicitly calls `overview`, `search`, `read`, link, outline, Base, or related commands. The inspected package does not itself push retained vault memory into every model invocation.

`NAPKIN.md` is a boundary case. Docs describe it as Level 0 pinned context, and `overview` includes it when the command is called, but the CLI/SDK does not automatically inject it into an agent session. The benchmark docs and README reference external Pi integration for context injection and automatic distillation; those extension implementations are not present in this repository, so they do not change the Napkin-core read-back verdict.

Selection and scope are explicit and staged. `overview` gives a folder-level map with tags and TF-IDF keywords; `search` performs lexical/fuzzy/prefix retrieval over Markdown filenames and content, boosted by backlinks and recency; `read` opens a full resolved file. Complexity control comes from overview depth, keyword count, search limit, snippet context, folder path filtering, and the agent's choice to stop before full-file reads. Effective recall quality is supported by benchmarks but remains runtime behavior, not a guaranteed property of the code.

At consumption, retrieved notes are advisory knowledge unless the host agent or user gives them stronger authority. Napkin does not distinguish "instruction" notes from ordinary notes in a typed way, and it does not test whether an agent faithfully follows a retrieved note after it appears in context.

## Curiosity Pass

**The strongest memory idea is progressive disclosure, not automatic memory.** Napkin makes a local vault more usable for agents by shaping how they inspect it. It does not try to infer what should be remembered from every conversation in the core package.

**Search is intentionally lexical.** The README says "No embeddings, no graphs, no summaries," and the code matches that for core retrieval. Backlinks and recency are rank features over files, not a separate graph memory or vector store.

**The docs contain future or adjacent mechanisms.** `docs/distill.md` describes a Pi extension that watches conversations and writes structured notes, and `docs/agent-memory-progressive-disclosure.md` mentions `napkin distill`; neither is implemented as a Napkin CLI command in the inspected source tree.

**Bare vault auto-creation is convenient but surprising.** `findVault` creates `.napkin/`, `.obsidian/`, and `NAPKIN.md` if no vault is found. That helps SDK calls "always work," but a host integrating Napkin should be explicit about paths to avoid accidental memory stores.

**The search cache is a useful derived artifact with limited authority.** It improves access speed and rank computation, but the source of truth remains Markdown files and mtimes. That keeps invalidation simple and avoids a hidden stale content store.

## What to Watch

- Whether the Pi `napkin-context` and `distill` extensions move into this repository or become part of the reviewed package; that would likely change trace-derived status and may change read-back from pull to push or both.
- Whether a real `napkin distill` command is implemented; that would add automatic or agent-triggered consolidation and could create trace-derived or imported derived artifacts.
- Whether access-pattern tracking or promotion of frequently read facts is added; that would introduce automatic `promote` or `decay` operations not present now.
- Whether search grows an embedding or hosted vector backend; that would add a parametric retained form and change the inspection/debugging story.
- Whether Napkin adds typed note classes, status fields, or validation gates; that would move it closer to Commonplace's stronger artifact authority.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Napkin stores a vault, but core read-back is explicit tool use.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: notes, config, templates, search cache, Base queries, and overview output have different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: vault notes and retrieved snippets mostly serve as evidence, reference, context, or advice.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - contrasts: Napkin config, templates, and CLI behavior shape access, but vault content is not automatically enforced as a system definition.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - relates: Napkin relies on filenames, folders, tags, links, headings, mtimes, and lexical terms as available retrieval symbols.
