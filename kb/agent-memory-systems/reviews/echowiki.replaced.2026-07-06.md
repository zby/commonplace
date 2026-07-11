---
description: "EchoWiki review: Obsidian plugin and CLI that compile raw notes and voice transcripts into an interlinked local wiki"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
last-checked: "2026-07-06"
---

# EchoWiki

> Replaced 2026-07-06. See [echowiki](./echowiki.md) for the current review.

EchoWiki, by mohammadmaso, is a TypeScript Obsidian plugin and CLI for compiling local `raw/` notes and voice transcripts into an Obsidian-compatible `wiki/` with summaries, concept pages, entity pages, an index, and an operations log. At the reviewed commit it is a local-first wiki compiler built around the Vercel AI SDK and OpenAI-compatible STT/LLM endpoints, not a retrieval/chat layer over the compiled wiki ([README.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/README.md), [CLAUDE.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/CLAUDE.md), [package.json](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/package.json), [src/wiki/compiler.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/compiler.ts)).

**Repository:** https://github.com/mohammadmaso/echowiki

**Reviewed commit:** [11446997423e88177dba62d6a3d5c1e8b4886c62](https://github.com/mohammadmaso/echowiki/commit/11446997423e88177dba62d6a3d5c1e8b4886c62)

**Last checked:** 2026-07-06

## Core Ideas

**The retained memory is an Obsidian wiki compiled from a single raw inbox.** The product docs and README define `raw/` as the universal ingestion point for manual notes and voice transcripts, and `wiki/` as the durable output tree: `summaries/`, `concepts/`, `entities/`, `index.md`, `log.md`, plus scaffolded `sources/` and `reports/` folders ([README.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/README.md), [.ai/01-PRD.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/.ai/01-PRD.md), [obsidian-plugin/src/main.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/main.ts), [templates/wiki/AGENTS.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/templates/wiki/AGENTS.md)). The plugin stores API keys and the pending queue in Obsidian plugin data, but the knowledge substrate is plain Markdown in the vault.

**The compiler turns each raw document into a summary, then mutates concept and entity pages.** `compileShortDoc` builds a system prompt from `wiki/AGENTS.md` or a default schema, asks the model for a summary, asks for a concept/entity plan from existing page briefs, creates or updates planned pages, strips ghost wikilinks, rewrites the summary against the known target whitelist, backlinks pages, updates `index.md`, and appends `log.md` ([src/wiki/compiler.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/compiler.ts), [src/wiki/prompts.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/prompts.ts), [src/wiki/page-writer.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/page-writer.ts), [src/wiki/index-writer.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/index-writer.ts)). That is stronger than "save a note": later compilation runs are expected to rewrite existing concept/entity pages in light of new source material.

**Context efficiency is coarse progressive disclosure, not retrieval ranking.** The compiler does not embed, search, or rank arbitrary wiki pages. It reads compact briefs from every existing concept/entity page, passes those brief lists into the planning prompt, then whitelists known wikilink targets before generating pages ([src/wiki/briefs.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/briefs.ts), [src/wiki/wikilink.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/wikilink.ts), [src/wiki/prompts.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/prompts.ts)). This bounds prompt complexity by summary/brief/index surfaces, but it is still all-briefs recall for concepts/entities rather than top-k retrieval.

**Obsidian is the primary integration surface.** The plugin registers commands for voice recording, sending the active note to `raw/`, compiling the active raw file, and reviewing pending compilations; a ribbon mic icon opens voice capture; settings configure folders, approval, watch mode, language, and provider credentials ([obsidian-plugin/src/main.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/main.ts), [obsidian-plugin/src/settings-tab.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/settings-tab.ts), [obsidian-plugin/manifest.json](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/manifest.json)). The root CLI exposes `npm run compile -- <raw-file> [--kb-dir <vault-root>]` for headless compilation ([src/cli/compile.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/cli/compile.ts)).

**Some design docs are stale relative to the code.** The `.ai/` PRD and tech spec still describe a Mastra implementation and leave the task checklist unchecked, while `CLAUDE.md`, README, manifests, and implementation use the Vercel AI SDK and an in-process Obsidian plugin bundle ([.ai/02-TECH-SPEC.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/.ai/02-TECH-SPEC.md), [.ai/03-TASKS.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/.ai/03-TASKS.md), [CLAUDE.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/CLAUDE.md), [src/llm/client.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/llm/client.ts), [obsidian-plugin/esbuild.config.mjs](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/esbuild.config.mjs)). The review therefore treats `.ai/` as intent/background, not as proof of implemented behavior.

## Artifact analysis

- **Storage substrate:** `files` — The central retained artifacts are vault files: `raw/` inputs, `wiki/AGENTS.md`, generated Markdown under `wiki/summaries/`, `wiki/concepts/`, and `wiki/entities/`, plus `wiki/index.md` and `wiki/log.md`. Obsidian plugin settings and the pending queue are stored through plugin data; there is no inspected persistent database, vector store, graph store, or model-artifact store ([obsidian-plugin/src/main.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/main.ts), [obsidian-plugin/src/settings.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/settings.ts), [src/storage/node-storage.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/storage/node-storage.ts), [obsidian-plugin/src/vault-storage.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/vault-storage.ts)).
- **Representational form:** `prose` `symbolic` — Summary, concept, entity, schema, and log pages are prose Markdown; YAML frontmatter, `sources` lists, entity types, wikilinks, known-target whitelists, settings, manifests, path guards, index entries, and pending queue records are symbolic. The code calls external LLM/STT services but does not retain embeddings, weights, adapters, or another parametric artifact ([src/wiki/frontmatter.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/frontmatter.ts), [src/wiki/wikilink.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/wikilink.ts), [src/llm/client.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/llm/client.ts), [obsidian-plugin/src/stt-client.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/stt-client.ts)).
- **Lineage:** `authored` `imported` — `wiki/AGENTS.md`, templates, settings, prompts, and source raw notes are authored by maintainers, users, or agents; generated summaries/concepts/entities/index/log are imported/derived views over raw notes and existing wiki pages. Voice transcripts become imported text once STT writes them into `raw/`. I did not find a durable learning path from agent session logs, tool traces, trajectories, or interaction histories into new behavior-shaping artifacts, so this review omits the `trace-derived` tag ([obsidian-plugin/src/voice-modal.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/voice-modal.ts), [obsidian-plugin/src/main.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/main.ts), [src/wiki/compiler.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/compiler.ts)).
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `learning` — Generated wiki pages and index entries serve as knowledge artifacts for humans, Obsidian, and future compiler runs; `wiki/AGENTS.md` and the prompt templates instruct the compiler; folder settings, page types, known-target whitelists, slugs, and index sections route writes and links; frontmatter construction, path containment checks, API-key/model checks, approval queueing, and ghost-link stripping provide structural validation; existing concept/entity briefs guide future compilation, so the compiled wiki has learning authority over later wiki growth ([src/wiki/schema.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/schema.ts), [src/wiki/prompts.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/prompts.ts), [src/wiki/briefs.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/briefs.ts), [src/storage/node-storage.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/storage/node-storage.ts), [obsidian-plugin/src/main.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/main.ts)).

**Raw inputs and voice transcripts.** Storage substrate: files under `raw/`. Representational form: prose Markdown/text, with optional audio files saved beside transcripts by the plugin. Lineage: authored notes or STT-imported speech. Behavioral authority: acquisition source material; raw files do not directly instruct the compiler until a manual command or watcher/approval path selects them for compilation.

**Generated wiki pages.** Storage substrate: Markdown under `wiki/summaries/`, `wiki/concepts/`, and `wiki/entities/`. Representational form: prose bodies plus symbolic frontmatter, `sources`, `doc_type`, `type`, descriptions, and wikilinks. Lineage: imported/derived from raw inputs and existing wiki briefs. Behavioral authority: knowledge for Obsidian/human browsing and learning input for future compiler runs.

**Schema, prompts, and known targets.** Storage substrate: `wiki/AGENTS.md` or the default schema string, plus package prompt templates. Representational form: prose instructions with symbolic placeholders and whitelisted targets. Lineage: authored configuration/package content. Behavioral authority: instruction, routing, and validation, because these artifacts define page shape, entity vocabulary, link permissions, and rewrite behavior.

**Index, log, approval queue, and settings.** Storage substrate: `wiki/index.md`, `wiki/log.md`, Obsidian plugin data, and plugin settings. Representational form: symbolic-plus-prose catalogue/log records and JSON-like settings. Lineage: generated from compilation events and user settings. Behavioral authority: routing and audit for humans and agents; approval has real workflow authority because raw files can be held before compilation.

**Governance gap.** The docs say manually edited wiki pages should not be silently overwritten, but `writeConcept`, `writeEntity`, `updateIndex`, and the Obsidian storage adapter modify existing files directly when the compiler chooses an update. I did not find conflict detection, manual-edit provenance, schema validation against OKF, or semantic faithfulness tests in the inspected code ([CLAUDE.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/CLAUDE.md), [templates/wiki/AGENTS.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/templates/wiki/AGENTS.md), [src/wiki/page-writer.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/page-writer.ts), [src/wiki/index-writer.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/index-writer.ts), [obsidian-plugin/src/vault-storage.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/vault-storage.ts)).

Promotion path: EchoWiki promotes raw prose into summary pages, then into concept/entity pages, backlinks, index entries, and future compilation context. It does not promote entries into hard validators, enforced gates beyond approval/path checks, embeddings, rankers, or reusable skills.

## Comparison with Our System

| Dimension | EchoWiki | Commonplace |
|---|---|---|
| Primary purpose | Compile raw personal notes and voice transcripts into an Obsidian wiki | Maintain a typed methodology KB for agent-operated knowledge-base design |
| Main artifact | Generated wiki page with frontmatter and wikilinks | Typed Markdown artifact governed by collection/type contracts |
| Write path | Obsidian commands, raw watcher, approval modal, CLI, LLM compiler | Agent/human edits, skills, validation, semantic review, indexes |
| Read path | Obsidian browsing plus compiler injection of existing concept/entity briefs | `rg`, indexes, links, collection contracts, skills, review reports |
| Governance | Approval queue, path guards, frontmatter/link cleanup, connection checks | Type validation, collection contracts, link checks, source citations, review gates |

EchoWiki and Commonplace share the file-first bet: durable memory is inspectable Markdown with symbolic metadata and links, not an opaque hosted memory service. EchoWiki is more product-facing: it makes voice capture, raw inbox handling, Obsidian commands, mobile-compatible plugin packaging, and provider settings part of the main surface.

The main divergence is artifact authority. EchoWiki's wiki pages are generated, mutable summaries and synthesis pages. Commonplace's library artifacts are typed claims, instructions, reviews, or references with explicit collection contracts and validation. EchoWiki asks the compiler prompt to respect wiki conventions; Commonplace makes more of the convention machine-checkable and reviewable.

EchoWiki's most interesting design pressure for Commonplace is not Obsidian itself. It is the update loop where existing concept/entity briefs are used as a compact memory of the current wiki while the compiler decides how a new source should modify the store. That is close to a lightweight, file-backed "semantic merge" path, but EchoWiki currently relies on the model and simple slug/frontmatter rules rather than conflict-aware governance.

### Borrowable Ideas

**Raw inbox plus approval queue.** Ready for consuming-project KBs. Commonplace itself should keep deliberate edits for library artifacts, but projects with high-volume notes could benefit from a `raw/` staging area and an explicit approve-to-promote workflow.

**Use editable runtime instructions for a compiler.** Ready with guardrails. EchoWiki's `wiki/AGENTS.md` lets users change compilation conventions without redeploying code; Commonplace can use the same idea for project-local import pipelines, while keeping type specs authoritative for durable library artifacts.

**Known-target whitelisting before wikilink generation.** Ready now. EchoWiki's whitelist and ghost-link stripping are a practical way to keep generated links from inventing pages.

**Compact brief lists as a cheap compilation memory.** Useful but needs scale tests. Reading every concept/entity description is simpler and more inspectable than embeddings; Commonplace could use that pattern for small workspaces before adding heavier retrieval.

**Do not borrow prompt-only overwrite governance.** EchoWiki's documented conflict rule is not enforced by the inspected writer. Commonplace should keep deterministic validation, diff review, and explicit ownership boundaries for generated updates.

## Write side

**Write agency:** `manual` `automatic` — Users manually record voice, send the active note to `raw/`, compile an active raw file, approve queued items, or run the CLI; automatic paths include watch-mode detection of created/modified raw files, STT transcript creation after recording, compilation after approval or when approval is disabled, generated page writes, index/log updates, backlink insertion, frontmatter construction, and ghost-link cleanup ([obsidian-plugin/src/main.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/main.ts), [obsidian-plugin/src/raw-watcher.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/raw-watcher.ts), [obsidian-plugin/src/approval-modal.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/approval-modal.ts), [src/wiki/compiler.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/compiler.ts)).

**Curation operations:** `evolve` — EchoWiki automatically rewrites existing concept/entity pages when the model's plan marks them for update, and it can add related-summary backlinks to existing pages. Creating a summary or first concept/entity page from a raw input is acquisition, not curation. Index rebuilds, log appends, and whitelisted-link cleanup are access/governance upkeep, not consolidation, deduplication, decay, invalidation, or promotion over stored memories.

The system can generate synthesis-like concept prose, but I would not classify this as implemented `synthesize` in the review vocabulary. The code has no separate operation that reasons across multiple already-stored entries to create a new durable claim beyond the ordinary LLM page-generation/update path, and the quality of any cross-document insight is not verified from code.

## Read-back

**Read-back:** `both` — Humans and agents can pull the generated wiki through Obsidian, `wiki/index.md`, page links, and the filesystem; the compiler also pushes retained wiki memory into future compilation prompts by reading `wiki/AGENTS.md` and all existing concept/entity briefs whenever it compiles a new raw document ([src/wiki/schema.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/schema.ts), [src/wiki/briefs.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/briefs.ts), [src/wiki/compiler.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/compiler.ts), [README.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/README.md)).

**Read-back signal:** `coarse` — The automatic push path is coarse: compile runs include the editable schema/instructions and a global list of current concept/entity briefs. Page-specific updates are then selected by the model's plan and slug checks; there is no identifier-triggered hook, lexical search, embedding retrieval, or LLM relevance judge over arbitrary wiki pages before every user action.

**Faithfulness tested:** `no` — The repository has connection-test helpers and a manual test checklist, but the root `test` script exits with "Error: no test specified," and I did not find an ablation or audit showing that pushed briefs or generated pages reliably improve later compilation decisions ([package.json](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/package.json), [obsidian-plugin/src/settings-tab.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/settings-tab.ts), [README.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/README.md)).

**Direction edge cases.** `wiki/AGENTS.md` is partly configuration, partly retained instruction memory. I count its compile-time inclusion as push for the compiler loop because the file is read from the user's wiki at runtime and can change future compilation behavior. Static README/docs do not count as memory read-back.

**Selection, scope, and complexity.** The push scope is per vault and compile-time. EchoWiki reads descriptions/previews from all concept/entity pages, not full bodies, then reads the full body only for pages selected for update. This makes context smaller than loading the whole wiki, but complexity grows with concept/entity count and there is no retrieval budget beyond "briefs only" plus generation concurrency.

**Authority at consumption.** Generated pages are advisory knowledge when browsed in Obsidian. In the compiler loop, existing briefs and `wiki/AGENTS.md` have stronger authority: they steer the model's plan and page generation. Effective authority is not measured; the code can place the context, but cannot prove the model obeys it.

**Other consumers.** Humans consume the wiki through Obsidian graph view, links, pages, status notices, approval modal, and settings UI. The CLI and compiler consume the same file store through `WikiStorage`, which keeps the plugin and headless paths aligned.

## Curiosity Pass

**EchoWiki is a compiler, not a memory search engine.** Its retrieval story is "read the index/wiki in Obsidian" and "compiler reads briefs," not query/chat over the wiki. The `.ai/` docs explicitly put query/chat and skill-factory features out of MVP scope.

**The strongest design is the shared text/voice ingestion funnel.** Once voice becomes a transcript under `raw/`, the compiler treats it like any other note. That keeps modality-specific code out of the memory compiler.

**The docs overstate OKF enforcement.** README and planning docs claim OKF frontmatter, and the code does write YAML-like fields, but I did not find an OKF schema validator or report generator.

**The `sources/` story is incomplete in code.** Summary frontmatter points `full_text` to `sources/{docName}.md`, and the plugin creates a `sources/` folder, but the inspected compile path reads raw content from `raw/` and writes generated pages; I did not find a write of the source copy under `wiki/sources/`.

**The tool helpers look ahead of the integrated product.** `src/wiki/tools.ts` has constrained helpers for reading/writing wiki, output, and exploration files, including long-document JSON page reads, but I did not find imports wiring those helpers into the compiler or Obsidian plugin.

## What to Watch

- Whether conflict detection for manually edited concept/entity pages is implemented. That would decide whether EchoWiki can safely evolve an authored wiki or only a generated one.
- Whether `wiki/sources/` becomes an actual retained source mirror. That would improve provenance and make summary `full_text` links truthful.
- Whether query/chat or explorations become integrated commands rather than schema placeholders. That would change read-back from compile-time brief push plus human pull to an agent-facing retrieval layer.
- Whether OKF validation, lint reports, or automated tests are added. That would move governance from prompt/schema intent into enforceable checks.
- Whether concept/entity selection changes from all-briefs prompting to lexical or embedding retrieval. That would change context-efficiency and read-back signal classification.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: EchoWiki stores a wiki, but only compile-time briefs and explicit browsing activate it.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: raw inputs, generated pages, prompts, settings, index/log, and approval state differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: generated summaries, concept pages, entity pages, and indexes mostly serve as evidence, reference, context, and advice.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: `wiki/AGENTS.md`, prompt templates, settings, path guards, and approval rules shape future compiler behavior.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - grounds: EchoWiki manages compiler context with briefs and whitelisted targets rather than full-wiki loading or vector retrieval.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - explains: EchoWiki's recall depends on available slugs, frontmatter descriptions, wikilinks, and directory conventions.
