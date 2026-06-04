---
description: "Funes review: Git/Markdown Librarian protocol for raw-source preservation, compiled wiki memory, generated outputs, and pull-only agent read-back"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-03"
---

# Funes

Funes, from Bethany Hunt's `ulyssestenn/funes` repository, is a template and operating protocol for LLM-managed Markdown knowledge libraries. At the reviewed commit it is not a packaged CLI, MCP server, RAG service, or database-backed memory system. It is a Git repository scaffold plus `AGENTS.md` instructions that tell a host coding agent to act as a Librarian: preserve raw sources, compile them into a linked wiki, answer questions from that wiki, generate reusable outputs, and periodically audit the library.

**Repository:** https://github.com/ulyssestenn/funes

**Reviewed commit:** [872d82f65119306739a6c7a761df5add0736d0df](https://github.com/ulyssestenn/funes/commit/872d82f65119306739a6c7a761df5add0736d0df)

**Last checked:** 2026-06-03

## Core Ideas

**The implementation unit is a protocolized repository, not application code.** The checkout contains Markdown instructions, a starter library scaffold, and a license, with no package manifest or runtime source modules. The top-level `AGENTS.md` tells agents that the repository hosts one or more LLM-managed knowledge bases and that each library has its own `AGENTS.md`, while `protocol.md` is the shared operating manual ([AGENTS.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/AGENTS.md), [protocol.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/protocol.md)). The system's behavioral force therefore comes from host-agent instruction loading and file conventions, not from code that enforces the workflow.

**Funes separates raw preservation from compiled memory.** The README and protocol define a raw -> wiki -> outputs flow: raw files are saved under `raw/`, compiled into source summaries, concept articles, and topic maps under `wiki/`, and then used to answer questions or produce reports under `outputs/` ([README.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/README.md), [protocol.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/protocol.md)). This is its main memory design: keep evidence immutable, then maintain an abstraction layer above it.

**The wiki has a fixed three-tier shape.** `wiki/sources/` holds one summary note per raw source, `wiki/concepts/` holds atomic articles, and `wiki/topics/` holds maps across related concepts. The protocol requires bidirectional relative Markdown links among source notes, concepts, related concepts, and topic maps, with a maintained `wiki/INDEX.md` as master navigation ([protocol.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/protocol.md), [starter-library/wiki/INDEX.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/starter-library/wiki/INDEX.md), [starter-library/wiki/concepts/README.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/starter-library/wiki/concepts/README.md)).

**Context efficiency is structural and manual.** Funes does not implement vector retrieval, top-k search, token budgets, embeddings, or automatic context selection. Its context-efficiency story is the maintained hierarchy: search or scan `wiki/INDEX.md`, then read source notes, concept articles, topic maps, and raw records only as needed. That bounds volume by navigational discipline rather than by an algorithm, and it bounds complexity by splitting source evidence, atomic concepts, maps, and outputs into separate files.

**The Librarian is expected to own maintenance.** The protocol tells the agent to update indexes, mark raw sources compiled, add changelog entries, audit broken links, duplicate concepts, stale indexes, contradictions, gaps, and new-article candidates, and write dated health reports under `meta/health/` ([protocol.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/protocol.md), [starter-library/meta/CHANGELOG.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/starter-library/meta/CHANGELOG.md), [starter-library/meta/health/README.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/starter-library/meta/health/README.md)). This is governance by instruction and convention, not deterministic validation.

**The adoption surface is deliberately plain.** A user can copy or rename `starter-library/`, edit its scope line, and point Claude Code, Codex, or another file-editing agent at the repository. `library.md` supplies the recipe for creating more top-level libraries, each sharing the same protocol ([README.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/README.md), [library.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/library.md), [starter-library/AGENTS.md](https://github.com/ulyssestenn/funes/blob/872d82f65119306739a6c7a761df5add0736d0df/starter-library/AGENTS.md)). The tradeoff is low setup cost at the price of relying on the acting agent's instruction following.

## Artifact analysis

- **Storage substrate:** `repo` - The central retained state is plain Markdown and raw files inside a Git repository: top-level protocol files plus per-library `raw/`, `wiki/`, `outputs/`, and `meta/` folders.
- **Representational form:** `prose` `symbolic` - Funes combines prose instructions, Markdown articles, YAML-like frontmatter templates, relative links, source registries, indexes, and changelog/health-report conventions.
- **Lineage:** `authored` `imported` - Protocol files and compiled wiki articles are authored by the framework or Librarian, while raw sources are imported or captured from user-supplied material.
- **Behavioral authority:** `knowledge` `instruction` `routing` - Raw sources, source notes, concepts, topics, and outputs advise future work, while `AGENTS.md`, protocol files, scaffolds, indexes, and topic maps instruct or route the Librarian.

**Top-level Librarian protocol files.** Storage substrate: repository files `AGENTS.md`, `protocol.md`, and `library.md`. Representational form: prose instructions plus symbolic folder maps and templates. Lineage: authored framework guidance in the Funes template. Behavioral authority: system-definition artifacts for any host agent that reads `AGENTS.md`; they instruct the Librarian role, routing, workflow, naming, linking, and maintenance behavior.

**Raw source layer.** Storage substrate: per-library `raw/`, `raw/assets/`, and `raw/INDEX.md`. Representational form: mixed raw documents, pasted text, images/assets, and a symbolic Markdown registry table. Lineage: imported or captured from user-supplied sources; the protocol marks raw content as the immutable record and says not to edit it after ingestion. Behavioral authority: knowledge artifacts as preserved evidence; they should ground compiled notes and cited answers, but they are not themselves future instructions.

**Compiled wiki articles.** Storage substrate: per-library `wiki/sources/`, `wiki/concepts/`, `wiki/topics/`, and `wiki/INDEX.md`. Representational form: prose Markdown with frontmatter, relative links, backlinks, tags, and index sections. Lineage: LLM-derived from raw sources during compile, then incrementally updated by the Librarian. Behavioral authority: knowledge artifacts when read as evidence or context for Q&A; weak system-definition authority when concept/topic organization routes future search and determines which abstractions are salient.

**Generated outputs.** Storage substrate: per-library `outputs/` Markdown files. Representational form: prose reports, analyses, comparisons, routines, answers, or reading plans. Lineage: generated from the compiled wiki in response to user questions; durable findings are supposed to be filed back into the wiki. Behavioral authority: mostly knowledge artifacts for humans and future agents until promoted into wiki articles; promotion is manual/instructional, not enforced by code.

**Indexes, changelog, and health reports.** Storage substrate: `raw/INDEX.md`, `wiki/INDEX.md`, `meta/CHANGELOG.md`, and dated files under `meta/health/`. Representational form: symbolic/prose Markdown lists, tables, and audit reports. Lineage: maintained by the Librarian after ingest, compile, Q&A, and health-check work. Behavioral authority: routing, audit, and governance artifacts. They can direct future work and expose defects, but there is no validator in this repository that enforces their correctness.

**Starter-library scaffold.** Storage substrate: `starter-library/` directories and seed README/INDEX files. Representational form: symbolic directory structure plus prose setup instructions. Lineage: authored template copied or renamed for a concrete domain. Behavioral authority: initial system-definition artifact for new libraries; after adoption, the copied files become that library's local operating surface.

**Promotion path.** Funes promotes imported raw sources into source notes, source notes into atomic concept articles and topic maps, wiki material into outputs, and durable output findings back into the wiki. The authority jump is from preserved evidence to maintained knowledge artifacts, with some routing authority in indexes and topic maps. It does not promote notes into executable validators, schemas, or enforced gates.

## Comparison with Our System

| Dimension | Funes | Commonplace |
|---|---|---|
| Primary purpose | User-facing LLM-maintained research libraries | Agent-operated methodology KB and framework |
| Main substrate | Git repository with raw/wiki/output/meta Markdown folders | Git-tracked typed Markdown collections, sources, reviews, indexes, reports, and Python commands |
| Agent contract | `AGENTS.md` plus shared Librarian Protocol | `AGENTS.md`, collection contracts, type specs, skills, validators, and review workflows |
| Context strategy | Manual hierarchy: index -> source/concept/topic -> raw/output | Search, generated indexes, links, type specs, collection routing, validation/review reports |
| Governance | Changelog, health reports, backlink/index discipline by instruction | Deterministic validation, schemas, review gates, archive/replacement lifecycle, generated indexes |
| Learning loop | Raw source distillation into wiki articles and outputs | Source-grounded writing, workshop/library promotion, validation, semantic review, and indexed navigation |

Funes is close to Commonplace's file-first worldview. Both systems treat Markdown in Git as a durable substrate, rely on agents that can read and edit files, and make indexes/links part of the memory architecture. Funes is simpler and more directly usable for a non-technical library: copy the scaffold, drop sources into `raw/`, and ask a Librarian to compile and answer.

The main divergence is authority. Commonplace encodes much of its method in type specs, schemas, Python commands, generated indexes, and review gates. Funes encodes the method almost entirely as prose instructions to a host agent. That keeps the project portable but makes correctness depend on agent discipline: stale indexes, duplicate concepts, link rot, and missed source provenance are issues the protocol asks the Librarian to catch, not things the repository can currently detect.

Funes also makes a sharper raw/compiled split than many note systems. Commonplace has `kb/sources/` and source-grounded reviews, but Funes' library template foregrounds the immutable raw layer as the first-class user workflow. That is useful product framing for source-heavy personal or research KBs.

**Read-back:** `pull` - Retained memory reaches the acting agent when the Librarian deliberately searches or reads the wiki in response to Q&A or output work; this checkout has no hook, runtime, retriever, or host integration that pushes instance-selected retained memory into context before action.

### Borrowable Ideas

**Make raw preservation a default scaffold, not an expert convention.** Commonplace already preserves source snapshots, but Funes makes `raw/` the obvious first stop for users. A consuming-project template could borrow that visible raw -> compiled flow. Ready for project templates, not a core methodology change.

**Treat outputs as candidates for library filing.** Funes keeps generated reports in `outputs/` but instructs the Librarian to file durable findings back into the wiki. Commonplace's workshop layer is similar; the borrowable piece is the user-facing language that separates reusable findings from one-off answers. Ready now for workshop guidance.

**Use health reports as an explicit operating surface.** Commonplace has validation and semantic review, but Funes' `meta/health/` folder is a simple place for human-visible maintenance reports. A Commonplace analogue could make periodic KB health checks easier to browse. Needs a concrete reporting workflow to avoid duplicating existing review artifacts.

**Keep the library creation path small.** `library.md` asks only for scope, link style, and tooling before scaffolding. Commonplace init flows should preserve that bias: ask only the choices that change the structure. Ready for CLI/template UX review.

**Do not borrow prose-only governance where stronger gates are available.** Funes' method is a good low-friction template, but Commonplace should keep validation, type specs, and review gates for artifacts with durable methodological authority.

## Curiosity Pass

**The README says "self-maintenance built in," but implementation means instructions and folders.** The repository ships a protocol for changelogs and health reports, not code that audits links or detects contradictions. That is a valid template choice, but the phrase can sound more automated than the checkout supports.

**The system is closer to a KB operating system prompt than a memory library.** Its central artifact is the Librarian role and directory contract. The host agent supplies parsing, search, summarization, linking, and judgment.

**Funes is trace-adjacent but not trace-derived under this review's taxonomy.** It can ingest transcripts as raw sources, and it records a changelog of Librarian actions, but I did not find a mechanism that mines agent-session traces into durable behavior-shaping rules or learned state. It distills supplied source material into a wiki.

**The raw/compiled split is stronger than the validation story.** Preserving evidence gives readers a way to audit compiled notes, but there is no citation checker, backlink checker, duplicate detector, or frontmatter validator in the repo. The health-check workflow is the place where those tools could later attach.

**The example library is external.** The reviewed checkout includes an empty starter library and points to `funes-example-ai` for richer output examples. This review treats only the inspected repository as implemented behavior.

## What to Watch

- Whether Funes adds actual scripts or commands for health checks, backlink repair, source registry updates, or citation verification. That would move governance from prose instruction toward symbolic enforcement.
- Whether a richer example library or generated library state is vendored into the main repo. That would let future reviews assess how the protocol holds up on non-empty memory.
- Whether host integrations appear for Claude Code, Codex, or other agents. A real integration could change read-back from pull-only protocol discipline to coarse or instance-targeted memory push.
- Whether source notes or concept articles gain required citation fields beyond relative links. That would strengthen provenance and make compiled abstraction safer to reuse.
- Whether outputs get explicit promotion metadata, such as "filed back," "discarded," or "pending review." That would make the output -> wiki loop auditable rather than conversational.

## Bottom Line

Funes is a useful file-first Librarian protocol for turning raw sources into a maintained Markdown wiki. Its strongest design move is not retrieval technology; it is the operational split between immutable raw evidence, compiled concepts/topics, generated outputs, and health maintenance. For Commonplace, Funes is most borrowable as a simple adoption scaffold and as product language for raw-to-library workflows. Its weak point is that nearly all governance remains instructed rather than enforced.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Funes stores and organizes memory, but read-back depends on the Librarian choosing to search/read the wiki.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Funes separates raw evidence, compiled wiki notes, outputs, indexes, changelogs, and health reports by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw sources, source notes, concepts, topics, and outputs mostly serve as evidence, reference, and context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: `AGENTS.md`, `protocol.md`, library scaffolds, indexes, and health-check conventions instruct or route future agent behavior.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: Funes' hierarchy is a manual context-loading design for agents working under bounded context.
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - compares: Funes' `outputs/` folder functions as a candidate-work area whose durable findings should be filed back into the wiki.
