---
description: "EchoWiki review: Obsidian plugin and CLI that compile raw notes and voice transcripts into file-backed wiki pages via the Vercel AI SDK"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-07-06"
---

# EchoWiki

EchoWiki, from `mohammadmaso/echowiki`, is a local-first Obsidian plugin and optional Node CLI that compile files from `raw/` into a Markdown wiki under `wiki/`. At the reviewed commit it handles manual text notes and voice transcripts, generates summaries plus concept/entity pages, updates an index and log, and stores the result as ordinary Obsidian-readable files. The implementation uses the Vercel AI SDK and OpenAI-compatible LLM/STT endpoints; the older PRD and tech spec still describe a Mastra implementation, but the package dependencies and runtime client are Vercel AI SDK based ([README.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/README.md), [package.json](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/package.json), [src/llm/client.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/llm/client.ts), [.ai/02-TECH-SPEC.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/.ai/02-TECH-SPEC.md)).

**Repository:** https://github.com/mohammadmaso/echowiki

**Reviewed commit:** [11446997423e88177dba62d6a3d5c1e8b4886c62](https://github.com/mohammadmaso/echowiki/commit/11446997423e88177dba62d6a3d5c1e8b4886c62)

**Source directory:** `related-systems/mohammadmaso--echowiki`

**Last checked:** 2026-07-06

## Core Ideas

**The primary store is an Obsidian vault file tree.** EchoWiki creates `raw/` and `wiki/` folders, accepts `.md`, `.txt`, and `.markdown` raw files, records voice audio plus STT transcripts into `raw/`, and writes generated wiki files under `wiki/summaries/`, `wiki/concepts/`, `wiki/entities/`, `wiki/index.md`, and `wiki/log.md` ([README.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/README.md), [obsidian-plugin/src/main.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/main.ts), [obsidian-plugin/src/utils.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/utils.ts)). The plugin has no separate server process; it bundles the compiler into the Obsidian plugin build ([obsidian-plugin/esbuild.config.mjs](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/esbuild.config.mjs)).

**Compilation is a multi-step LLM rewrite loop.** `compileShortDoc` generates a summary, reads existing concept/entity briefs, asks the model for create/update/related plans, writes or rewrites concept and entity pages, cleans impossible wikilinks, backfills related-document links, updates `index.md`, and appends to `log.md` ([src/wiki/compiler.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/compiler.ts), [src/wiki/prompts.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/prompts.ts), [src/wiki/page-writer.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/page-writer.ts), [src/wiki/index-writer.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/index-writer.ts)).

**Context efficiency is brief-list progressive disclosure, not search.** The compiler sends all existing concept and entity one-line briefs into the planning prompt, then reads full existing pages only for model-selected update targets. It also sends a whitelist of existing wiki targets before later generation steps so the model cannot create arbitrary wikilinks ([src/wiki/briefs.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/briefs.ts), [src/wiki/compiler.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/compiler.ts), [src/wiki/wikilink.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/wikilink.ts)). There is no top-k retrieval, embedding index, vector store, or token budget; the brief catalog grows with the wiki and its quality is not measured in code.

**The wiki can carry its own compiler instructions.** `getAgentsMd` reads `wiki/AGENTS.md` at compile time and falls back to an embedded default schema, while `templates/wiki/AGENTS.md` presents the file as an editable runtime instruction manual ([src/wiki/schema.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/schema.ts), [templates/wiki/AGENTS.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/templates/wiki/AGENTS.md)). This gives the vault owner an adoption-friendly way to change compiler conventions without rebuilding the plugin.

**Trust machinery is mostly structural.** EchoWiki guards wiki-root path traversal in Node storage, strips wikilinks that do not target known pages, parses JSON-ish model outputs, and writes frontmatter itself rather than asking the model to emit YAML ([src/storage/node-storage.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/storage/node-storage.ts), [src/wiki/wikilink.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/wikilink.ts), [src/wiki/llm.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/llm.ts), [src/wiki/frontmatter.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/frontmatter.ts)). Semantic fidelity, duplicate avoidance, and conflict detection still rest on the model and user review. The docs say not to silently overwrite manually edited wiki pages, but current writers modify existing concept/entity files directly when the plan chooses update ([CLAUDE.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/CLAUDE.md), [src/wiki/page-writer.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/page-writer.ts), [obsidian-plugin/src/vault-storage.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/vault-storage.ts)).

## Artifact analysis

- **Storage substrate:** `files` `repo` - User memory persists as vault files under `raw/` and `wiki/`, plus Obsidian plugin data for settings and the pending queue. The shipped behavior layer is a git repository containing the compiler, plugin, prompts, templates, manifests, and release workflow ([obsidian-plugin/src/settings.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/settings.ts), [src/storage/types.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/storage/types.ts), [obsidian-plugin/manifest.json](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/manifest.json), [.github/workflows/release.yml](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/.github/workflows/release.yml)).
- **Representational form:** `prose` `symbolic` - Raw notes, transcripts, generated summaries, concept/entity pages, prompts, and `AGENTS.md` are prose; frontmatter, folder roles, slugs, wikilinks, model plans, pending-queue records, settings, indexes, and operation logs are symbolic. I found no retained vector index, graph database, embedding store, adapter, or model-weight artifact in the reviewed code.
- **Lineage:** `authored` `imported` `other-compiled` - Users author raw notes and can author `wiki/AGENTS.md`; dropped files are imported into the raw channel; voice transcripts are compiled from audio through STT; generated summaries, concept pages, entity pages, index entries, backlinks, and logs are compiled from raw content plus existing wiki state. I did not find durable artifacts derived from agent execution traces.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `enforcement` `learning` - Generated wiki pages advise future users and compiler runs as knowledge artifacts, and existing concept/entity briefs plus selected concept/entity page bodies give the compiled wiki learning authority over future wiki growth. `wiki/AGENTS.md`, templates, and prompts instruct the compilation agent; indexes, wikilinks, slugs, source lists, and brief catalogs route attention; config checks, JSON parsing, frontmatter writers, and connection tests validate shape and availability; approval mode, path guards, in-flight tracking, and ghost-link stripping enforce local operational boundaries ([obsidian-plugin/src/raw-watcher.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/raw-watcher.ts), [obsidian-plugin/src/approval-modal.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/approval-modal.ts), [obsidian-plugin/src/compiler-client.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/compiler-client.ts), [obsidian-plugin/src/stt-client.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/stt-client.ts)).

**Raw and generated wiki files.** The standing user-facing artifact is the generated wiki, not a retrieval database. Summary files carry `full_text: "sources/<doc>.md"` frontmatter, but I did not find compile-path code that writes a copy to `wiki/sources/`; the live source of truth is the raw file passed into the compiler unless the user preserves it separately ([src/wiki/page-writer.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/page-writer.ts), [src/wiki/compiler.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/compiler.ts), [obsidian-plugin/src/main.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/main.ts)).

**Compiler instructions and prompt code.** `wiki/AGENTS.md` is a prose system-definition artifact consumed at runtime, while `src/wiki/prompts.ts` and the compiler code are shipped system definitions. The effective schema is therefore split between editable vault instructions and packaged TypeScript constraints.

**Plugin state and gates.** The approval queue is retained plugin data, not wiki knowledge. It changes whether raw files become compiled memory, so it has enforcement authority over writes but no independent semantic authority over the generated pages.

**Promotion path.** EchoWiki promotes raw material into summaries, concept/entity pages, backlinks, and index/log entries. It does not currently promote repeated lessons into validators, rules, rankers, or stronger symbolic contracts; editing `wiki/AGENTS.md` is a manual instruction-promotion path.

## Comparison with Our System

EchoWiki and Commonplace share the file-backed premise: Markdown, frontmatter, links, indexes, and agent-readable instructions can be enough to make retained knowledge operational. EchoWiki's strongest adoption move is that this all lives inside a normal Obsidian vault, with voice capture, watch mode, and approval UI close to the user's capture flow.

The main divergence is evidence and authority. Commonplace treats collection contracts, type specs, validation, review gates, link vocabulary, and citation discipline as part of the retained system. EchoWiki treats the LLM compiler as the main organizer: it can rewrite concept/entity pages from new raw notes, but semantic correctness, source grounding, and duplicate control are not independently checked. Its generated wiki is useful as a personal knowledge surface, but it is weaker as a code-grounded methodology KB because generated claims do not carry source-span provenance or review status.

EchoWiki's context model is also narrower. Commonplace routes by curated indexes, tags, descriptions, type contracts, and explicit search. EchoWiki routes compilation through all existing concept/entity briefs and model-selected page rewrites. That is simple and local-first, but it will grow less predictable as the concept/entity catalog expands unless stronger selection, validation, or sharding appears.

### Borrowable Ideas

**Capture-first Obsidian plugin surface.** Needs a concrete Commonplace use case. EchoWiki makes ingestion ergonomic by putting voice, raw note copying, pending approval, and status feedback inside the editor where capture happens.

**Editable runtime schema file for the compiler.** Ready with guardrails. Commonplace already uses collection contracts and skills, but a vault-local compiler instruction file can be a useful override point when clearly lower authority than validated type specs.

**Brief-list planning before page rewrites.** Worth borrowing only for small stores. The "briefs first, full pages only for selected updates" pattern is cheap and inspectable, but Commonplace would need token caps and deterministic candidate selection before using it on large collections.

**Ghost-link stripping after generation.** Ready now. EchoWiki's post-generation cleanup of wikilinks against known targets is a practical, low-cost validation step for LLM-written Markdown.

**Do not borrow direct semantic overwrite as-is.** EchoWiki's model can rewrite existing concept/entity pages without a merge review or conflict marker. Commonplace should keep stronger review and provenance gates before generated synthesis changes durable methodology notes.

## Write side

**Write agency:** `manual` `automatic` - Humans create or drop raw notes, send active Obsidian notes to `raw/`, record voice notes, approve queued items, run the CLI, and can edit wiki files directly. Automatic paths watch raw-file create/modify events, transcribe audio to text, compile raw content through the LLM, write summaries, create or update concepts/entities, add backlinks, refresh `index.md`, append `log.md`, and store plugin settings/pending state ([obsidian-plugin/src/main.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/main.ts), [obsidian-plugin/src/raw-watcher.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/raw-watcher.ts), [src/cli/compile.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/cli/compile.ts)).

**Curation operations:** `evolve` - EchoWiki evolves existing concept and entity pages in place when the plan marks them for update, adding the new source and rewriting the page body. Its prompts ask the model to create concept pages and relationships from a new source plus existing brief context, but the implementation does not verify that a generated page asserts a genuinely new cross-source insight rather than summarizing or extending inputs, so I would not mark `synthesize` from code alone. Summary creation from a raw file is acquisition rather than curation, and index/log rewrites are access-structure upkeep rather than memory curation.

## Read-back

**Read-back:** `both` - Humans and future agents can pull the retained wiki by opening `wiki/index.md`, graph view, or individual Markdown files; the compiler also pushes retained concept/entity briefs and selected existing page bodies into later compilation prompts whenever a raw item is compiled.

**Read-back signal:** `coarse` `inferred / judgment` - The compiler sends the whole concept/entity brief catalog to the planning prompt as coarse recall. Full existing page bodies are read for update targets selected by the model's judgment from the new document summary and existing brief list, not by lexical search, embeddings, or a deterministic identifier router ([src/wiki/briefs.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/briefs.ts), [src/wiki/compiler.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/compiler.ts)).

**Faithfulness tested:** `no` - The repo has manual test checklists and connection-test helpers, but I did not find automated tests or ablations showing that pushed wiki context improves compilation quality or that generated concept/entity rewrites faithfully preserve prior meaning ([README.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/README.md), [package.json](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/package.json), [obsidian-plugin/src/settings-tab.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/settings-tab.ts)).

**Direction edge cases.** The editable `wiki/AGENTS.md` is loaded into the system message during compilation, but static compiler instructions alone are not memory read-back. The memory read-back is the existing wiki content being reintroduced into later compilation prompts.

**Selection, scope, and complexity.** Scope is vault-local. Selection is simple: all briefs, then model-selected full pages. Complexity is bounded by compact briefs early in growth, but there is no coded cap on the number of concept/entity briefs sent to the model and no deterministic ranking beyond the model plan.

**Authority at consumption.** For humans, wiki pages are advisory knowledge. For the compiler, `wiki/AGENTS.md` is instruction authority and existing concept/entity pages are behavior-shaping context for future rewrites. The generated knowledge does not hard-gate later user behavior.

**Other consumers.** Obsidian graph view, human readers, the plugin UI, the Node CLI, and future compiler invocations consume the same file tree. External LLM/STT services consume request payloads during compilation and transcription, but no service-side retained memory is part of the inspected implementation.

## Curiosity Pass

**The implemented product is less agent-framework-heavy than the planning docs.** The design docs repeatedly mention Mastra, but the shipped code is a direct Vercel AI SDK client plus hand-written orchestration functions.

**The source-preservation story is incomplete.** The directory layout and summary frontmatter refer to `wiki/sources/`, yet the current short-document compile path does not appear to write source copies there.

**The dead `tools.ts` surface looks like upstream parity residue.** It exposes wiki file, page, image, and exploration helpers, but I found no imports from the plugin, CLI, or compiler entrypoint. It should not be treated as deployed retrieval behavior at this commit ([src/wiki/tools.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/tools.ts)).

**The approval gate controls compilation, not knowledge quality.** Approval lets a user decide whether a raw item should enter the compiler, but once compilation starts the semantic merge is still model-mediated.

**Obsidian is doing the browsing work.** EchoWiki does not need a query engine for its MVP because it delegates navigation to `wiki/index.md`, wikilinks, files, and graph view.

## What to Watch

- Whether EchoWiki implements the promised `wiki/sources/` copy path. That would strengthen provenance and make generated summary `full_text` links resolvable.
- Whether concept/entity rewrites gain conflict detection, diffs, or a review gate before modifying manually edited pages. That determines whether direct LLM evolution can be trusted for durable notes.
- Whether brief-list planning receives token budgets, sharding, lexical filtering, or embedding retrieval as the wiki grows. That would change context-efficiency and read-back signal classification.
- Whether the planned lint/health reports under `wiki/reports/` become implemented validation artifacts. That would shift some authority from prompt discipline to symbolic checks.
- Whether Query/Chat or exploration exports move from stretch-goal/docs into code. That would add a separate read-back surface over the compiled wiki.

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: EchoWiki's raw files, generated pages, `AGENTS.md`, prompts, indexes, plugin state, and structural guards differ by substrate, form, lineage, and authority.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - classifies: stored wiki pages matter only when humans pull them or the compiler pushes briefs/pages into later prompts.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: generated summaries, concepts, entities, indexes, and logs mostly serve as evidence, reference, context, and advice.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: compiler prompts, `wiki/AGENTS.md`, plugin settings, path guards, and approval gates directly shape future behavior.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - grounds: EchoWiki manages context with brief catalogs and selected full-page reads rather than loading the whole wiki or maintaining a vector index.
