---
description: "EchoWiki review: Obsidian plugin and CLI compile raw notes and voice transcripts into a local LLM-maintained wiki"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: outdated
tags: []
last-checked: "2026-07-06"
---

# EchoWiki

> Replaced 2026-07-06. See [echowiki](./echowiki.md) for the current review.

EchoWiki, from `mohammadmaso/echowiki`, is a local-first Obsidian plugin plus optional Node CLI that compiles Markdown/text notes and STT transcripts from `raw/` into an Obsidian-compatible `wiki/` of summaries, concepts, entities, an index, and a log. At the reviewed commit it is a wiki compiler and maintenance loop: it uses the Vercel AI SDK against OpenAI-compatible LLM endpoints, stores retained knowledge as local Markdown/frontmatter files, and does not implement a query/chat layer, vector index, graph database, or retained model artifact ([README.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/README.md), [manifest.json](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/manifest.json), [src/wiki/compiler.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/compiler.ts), [src/llm/client.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/llm/client.ts)).

**Repository:** https://github.com/mohammadmaso/echowiki

**Reviewed commit:** [11446997423e88177dba62d6a3d5c1e8b4886c62](https://github.com/mohammadmaso/echowiki/commit/11446997423e88177dba62d6a3d5c1e8b4886c62)

**Source directory:** `related-systems/mohammadmaso--echowiki`

**Last checked:** 2026-07-06

## Core Ideas

**`raw/` is the universal acquisition surface.** The README and plugin implementation converge on one intake folder: manual Markdown/text notes, copies of active Obsidian notes, and STT transcripts all become raw files before compilation. The Obsidian plugin creates `raw/` and `wiki/`, watches raw-file create/modify events when watch mode is on, debounces events for one second, and either queues the path for approval or compiles it immediately ([README.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/README.md), [obsidian-plugin/src/main.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/main.ts), [obsidian-plugin/src/raw-watcher.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/raw-watcher.ts), [obsidian-plugin/src/stt-client.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/stt-client.ts)).

**The compiler turns source notes into a standing wiki, not into a retrieval index.** `compileShortDoc` sends the full raw source to an LLM for a summary, asks for a concept/entity plan using existing concept and entity briefs, creates or rewrites selected concept/entity pages, rewrites the summary after valid link targets are known, updates `index.md`, and appends to `log.md` ([src/wiki/compiler.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/compiler.ts), [src/wiki/briefs.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/briefs.ts), [src/wiki/page-writer.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/page-writer.ts), [src/wiki/index-writer.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/index-writer.ts)). The future action it changes is later compilation and human/agent browsing of the wiki, not a runtime top-k memory retrieval call.

**`wiki/AGENTS.md` is an editable runtime instruction artifact.** The template says the file is the compiler agent's instruction manual, and `getAgentsMd` reads it from the wiki root on each compilation, falling back to a default schema prompt if the file is absent ([templates/wiki/AGENTS.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/templates/wiki/AGENTS.md), [src/wiki/schema.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/schema.ts)). That gives users a high-authority prose system-definition artifact inside the same local wiki that holds the generated knowledge artifacts.

**Context efficiency is staged but coarse.** EchoWiki does not search or rank stored wiki pages with BM25, embeddings, or a graph. It loads the complete raw source for the current document, loads all concept/entity one-line briefs for the planning call, and then loads full existing page bodies only for LLM-selected concept/entity updates. Complexity control comes from summaries/briefs, per-step prompts, a known-target wikilink whitelist, ghost-link stripping, and configured generation concurrency rather than from token budgets or learned retrieval ([src/wiki/compiler.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/compiler.ts), [src/wiki/briefs.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/briefs.ts), [src/wiki/wikilink.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/wikilink.ts), [src/config.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/config.ts)).

**Adoption affordances are Obsidian-native and provider-light.** The plugin runs in-process, targets Obsidian desktop and mobile, uses ordinary vault files, stores settings through Obsidian plugin data, and calls OpenAI-compatible LLM/STT endpoints configured by the user. The CLI path can compile a raw file against the same compiler API with a filesystem-backed storage adapter ([README.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/README.md), [obsidian-plugin/src/settings.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/settings.ts), [obsidian-plugin/src/settings-tab.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/settings-tab.ts), [src/cli/compile.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/cli/compile.ts), [src/storage/node-storage.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/storage/node-storage.ts)).

**Trust is mostly prompt- and structure-based.** The code manages frontmatter, strips invalid wikilinks, confines storage paths, and requires configured model credentials, but I did not find OKF schema validation, semantic citation checking, or a conflict detector for manual edits. A concrete code/docs gap: summaries receive `full_text: "sources/<doc>.md"` frontmatter and docs describe `wiki/sources/`, but the inspected compile path reads the raw file and does not copy it into `wiki/sources/` ([CLAUDE.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/CLAUDE.md), [templates/wiki/AGENTS.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/templates/wiki/AGENTS.md), [src/wiki/page-writer.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/page-writer.ts), [src/compiler-api.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/compiler-api.ts), [src/wiki/frontmatter.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/frontmatter.ts), [src/storage/node-storage.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/storage/node-storage.ts)).

## Artifact analysis

- **Storage substrate:** `files` - The central durable artifacts are local vault files: `raw/` source notes/transcripts and `wiki/` Markdown/frontmatter pages, plus Obsidian plugin data for settings and the pending queue. The inspected implementation does not persist a database, vector store, graph store, key-value service, or model weights ([README.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/README.md), [obsidian-plugin/src/vault-storage.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/vault-storage.ts), [src/storage/node-storage.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/storage/node-storage.ts)).
- **Representational form:** `prose` `symbolic` - Raw notes, summaries, concepts, entities, `AGENTS.md`, prompts, and index/log prose are read by humans and LLM calls; frontmatter, wikilinks, page slugs, source lists, settings, pending queue entries, CLI flags, JSON response contracts, and TypeScript code are symbolic. External models are called, but EchoWiki stores no embeddings, adapters, rankers, or model weights ([src/wiki/prompts.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/prompts.ts), [src/wiki/frontmatter.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/frontmatter.ts), [src/llm/client.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/llm/client.ts)).
- **Lineage:** `authored` `imported` - The source inputs and system definitions fall under the controlled lineage tokens: users author raw Markdown/text notes, settings, and optional `wiki/AGENTS.md`; package prompts, templates, and compiler code are authored system definitions; voice transcripts and copied notes are imported into `raw/`. The central generated wiki pages are LLM-derived views over those authored/imported source materials and prior wiki pages, not a separate controlled lineage token in this review vocabulary. I found no durable artifacts derived from agent session logs, tool traces, trajectories, or execution histories ([obsidian-plugin/src/main.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/main.ts), [obsidian-plugin/src/stt-client.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/stt-client.ts), [src/wiki/compiler.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/compiler.ts)).
- **Behavioral authority:** `knowledge` `instruction` `routing` `enforcement` `validation` `learning` - Generated wiki pages are knowledge artifacts for humans and later compiler calls; existing summaries, concept/entity briefs, and selected page bodies give the compiled wiki learning authority over future wiki growth. `wiki/AGENTS.md`, package prompts, and settings are system-definition artifacts with instruction authority; index entries, wikilinks, briefs, slugs, and valid-target whitelists route attention; the approval gate, raw-folder filter, in-flight set, and path confinement enforce operational boundaries; JSON parsing, entity-type filtering, frontmatter rewriting, API-key checks, and ghost-link stripping provide structural validation ([src/wiki/schema.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/schema.ts), [src/wiki/compiler.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/compiler.ts), [obsidian-plugin/src/main.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/main.ts), [src/wiki/wikilink.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/wikilink.ts)).

**Raw inputs and transcripts.** `raw/` files are imported or authored source material. They become behavior-shaping only when the compiler reads them as the current document; otherwise they are retained source artifacts, not the standing wiki memory.

**Compiled wiki pages.** `summaries/`, `concepts/`, `entities/`, `index.md`, and `log.md` are the durable knowledge surface. Summary pages point at `sources/<doc>.md` or `.json`, concept/entity pages carry `sources: ["summaries/<doc>.md"]`, and index/log pages route human and agent attention. Because the code does not appear to copy the raw source into `wiki/sources/`, the generated source pointer is weaker than the docs imply.

**Runtime compiler instructions.** `wiki/AGENTS.md` and the package prompts are prose system-definition artifacts. `AGENTS.md` is user-editable and loaded at compilation time; package prompts specify JSON contracts, concept/entity planning rules, update behavior, and the valid-wikilink whitelist.

**Brief lists and selected full-page reads.** Concept/entity brief lists are derived views computed from existing pages on each run. They are not stored as a separate index, but they are a key read-back surface: the compiler uses them to choose which existing memory to update, then reads full page bodies for selected updates.

**Plugin settings and queue state.** `rawFolder`, `wikiFolder`, watch mode, approval requirement, LLM/STT endpoints, language, and pending queue entries shape when the compiler runs and which folders are authoritative. These are operational system-definition artifacts rather than wiki knowledge.

**Promotion path.** EchoWiki's implemented path is raw note or transcript -> summary -> concept/entity update -> index/log routing. This can promote source material from a one-off note into a reusable concept/entity page, but it does not promote claims into validated gates, typed review states, external citations, embeddings, or learned model artifacts.

## Comparison with Our System

EchoWiki and Commonplace share a file-first assumption: local Markdown, wikilinks, and agent-readable instruction files are valuable because agents and humans can inspect and edit the same artifacts. EchoWiki is more adoption-oriented: an Obsidian user can record or drop notes into `raw/`, approve compilation, and browse the resulting graph without learning a KB type system.

The main divergence is authority. Commonplace treats collection contracts, type specs, validation, citations, review gates, and navigation indexes as the system. EchoWiki treats the LLM-generated wiki as a helpful compiled view and relies on prompts plus light structural cleanup for quality. That makes EchoWiki easier to use as a personal capture compiler, but weaker as an evidence-bearing agent memory system: source preservation is incomplete in the inspected code, OKF is not schema-validated, and manual-edit conflicts are a documented concern rather than an implemented guard.

EchoWiki's automatic update loop is still relevant to Commonplace because it shows a simple "raw intake -> approved compile -> standing wiki" workflow with editor-native UX. Commonplace already has stronger retained-artifact governance; EchoWiki is mainly useful as an acquisition and compilation pattern, not as a trust model.

### Borrowable Ideas

**A universal raw intake folder with an approval queue.** Ready for consuming projects, not necessarily Commonplace core. A workshop or ingestion layer could accept source notes, transcripts, or pasted material in one place and require approval before promotion.

**Runtime-editable compiler instructions.** Ready with constraints. Commonplace already has collection contracts; a per-workshop or per-import `AGENTS.md`-style instruction artifact could let operators tune temporary compilation behavior without changing framework code.

**Brief-first compilation context.** Ready now. EchoWiki's concept/entity brief lists are a cheap middle layer between loading nothing and loading every page body.

**Known-target wikilink whitelist and ghost-link stripping.** Ready now. Generated notes should be constrained to existing targets or planned targets, with invalid links downgraded to plain text before write.

**Editor-native watch and approval UX.** Needs a concrete consuming project. The Obsidian plugin shape is useful where the human already lives in an editor, but Commonplace's own library artifacts should remain validator-governed rather than silently rewritten by file-watch events.

**Do not borrow source/provenance weakness.** If Commonplace compiles raw material, the raw source snapshot or citation target must be retained before generated pages point to it.

## Write side

**Write agency:** `manual` `automatic` - Humans manually create/drop raw files, send active notes to `raw/`, record voice notes, approve or reject queued items, edit settings, invoke the CLI, and can edit wiki pages directly. EchoWiki automatically writes transcripts, queues pending paths, compiles raw files in watch mode or on command, writes summaries/concepts/entities, rewrites existing concept/entity pages, updates indexes/backlinks/source lists, and appends the operations log ([obsidian-plugin/src/main.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/main.ts), [obsidian-plugin/src/raw-watcher.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/obsidian-plugin/src/raw-watcher.ts), [src/wiki/compiler.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/compiler.ts), [src/wiki/page-writer.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/page-writer.ts), [src/wiki/index-writer.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/index-writer.ts)).

**Curation operations:** `evolve` - The automatic compiler modifies existing concept/entity pages in place when the LLM plan chooses an update, and it also evolves surrounding routing artifacts by adding source references, backlinks, index entries, and log entries. Summary generation and STT transcription are acquisition, not curation over already-stored memory. The prompts aim for cross-document concept synthesis, but I would not mark `synthesize` from the code alone: there is no implemented oracle or checker that distinguishes a genuinely new cross-source insight from a rewrite or expansion of source summaries.

## Read-back

**Read-back:** `both` - The compiled wiki can be pulled by humans or agents through Obsidian files, `index.md`, graph navigation, and ordinary file reads. It is also pushed into future compiler actions: each compilation loads `wiki/AGENTS.md`, all existing concept/entity briefs, and, after an LLM plan, selected full existing pages into subsequent LLM calls ([src/wiki/schema.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/schema.ts), [src/wiki/briefs.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/briefs.ts), [src/wiki/compiler.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/wiki/compiler.ts)).

**Read-back signal:** `coarse` `inferred / judgment` - `AGENTS.md` and all concept/entity briefs are coarse always-loaded memory for a compilation run. Full existing concept/entity pages are loaded only after the LLM judges, from the current summary and brief list, which pages should be updated. There is no lexical, embedding, or deterministic identifier-triggered retrieval layer over arbitrary wiki content.

**Faithfulness tested:** `no` - I found no tests, ablations, audits, or post-action checks showing that pushed briefs or selected pages improve later compiler behavior. The root `package.json` test script is a placeholder rather than an implemented test suite ([package.json](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/package.json)).

**Direction edge cases.** The Obsidian wiki is mostly pull for ordinary users: open `wiki/index.md`, follow links, or use graph view. For the compiler agent, however, stored memory is pushed by host code before each LLM call. User approval is a write-side gate; it does not itself decide what memory is read back.

**Selection, scope, and complexity.** EchoWiki has no top-k memory budget. The current raw document is loaded in full, brief lists can grow with every concept/entity page, and selected update pages are full-body reads. The known-target whitelist reduces link-space complexity, and brief-first planning reduces page-body volume, but actual context dilution is not measured in code.

**Authority at consumption.** `wiki/AGENTS.md` and package prompts are instructions to the compiler. Existing concept/entity pages are advisory knowledge when used as update context, but their content can still be rewritten into future pages, so bad memory can propagate. Index/log entries route attention but do not hard-gate behavior.

**Other consumers.** Obsidian users consume wiki pages, graph links, plugin notices, the status bar, approval modal, and settings UI. The compiler consumes raw files, `AGENTS.md`, briefs, selected existing pages, and settings. The CLI consumes filesystem files and environment-backed model configuration.

## Curiosity Pass

**EchoWiki is closer to a local knowledge compiler than to RAG.** It does not retrieve snippets to answer questions. It compiles raw material into a new standing wiki that may later guide users or future compilation.

**The source layer is weaker than the wiki shape suggests.** `sources/` is documented and summary frontmatter points at it, but the inspected short-document compile path does not write the raw source there. That matters because generated summaries and concepts otherwise outrun their retained evidence.

**The design docs lag the implementation stack.** `.ai/01-PRD.md` and `.ai/02-TECH-SPEC.md` still describe a Mastra implementation, while `CLAUDE.md`, the README, and code use the Vercel AI SDK directly ([.ai/01-PRD.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/.ai/01-PRD.md), [.ai/02-TECH-SPEC.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/.ai/02-TECH-SPEC.md), [CLAUDE.md](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/CLAUDE.md), [src/llm/client.ts](https://github.com/mohammadmaso/echowiki/blob/11446997423e88177dba62d6a3d5c1e8b4886c62/src/llm/client.ts)).

**Manual-edit safety is stated but not enforced.** The instructions say not to silently overwrite manually edited wiki pages, but `writeConcept`, `writeEntity`, and the Obsidian storage adapter rewrite existing files without a conflict marker, hash check, or review step.

**The strongest implemented guard is symbolic cleanup.** The known-target whitelist and ghost-link stripping are small but concrete: they prevent generated pages from accumulating dead wikilinks even when the LLM invents targets.

## What to Watch

- Whether EchoWiki starts copying raw sources into `wiki/sources/` and validating summary source pointers. That would materially improve provenance and reviewability.
- Whether OKF schema validation or a wiki lint report is implemented. That would move generated pages from prompt-shaped prose toward checked artifacts.
- Whether manual-edit conflict detection lands. That would make automatic `evolve` safer for human-maintained concept/entity pages.
- Whether query/chat, search, embeddings, or graph retrieval are added over `wiki/`. That would change read-back from compiler-pushed briefs plus human pull into an active retrieval layer.
- Whether concept/entity matching gains deterministic deduplication or invalidation. That would add curation operations beyond `evolve`.
- Whether future versions compile agent session logs or tool traces into wiki rules, concepts, or instructions. That would be the point where trace-derived learning applies.

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: EchoWiki splits source notes, generated wiki pages, runtime instructions, settings, and indexes across different artifact roles.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: stored wiki pages matter only when humans pull them or the compiler pushes briefs/pages into an LLM call.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: generated summaries, concepts, entities, index entries, and raw sources mostly serve as evidence, reference, context, or advice.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: `wiki/AGENTS.md`, prompts, settings, approval state, and storage constraints shape behavior with instruction, routing, enforcement, or validation authority.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - grounds: EchoWiki manages context with brief-first compilation and whitelisted links rather than retrieval budgets.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - explains: EchoWiki's read-back depends on visible symbols such as slugs, wikilinks, frontmatter descriptions, source lists, and raw paths.
