---
description: "LLM Wiki review: Python toolkit and agent protocol for file-backed Markdown wikis with BM25/qmd search, MCP tools, linting, and Obsidian-oriented workflow"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: outdated
last-checked: "2026-07-06"
tags: []
---

# LLM Wiki (cobusgreyling)

> Replaced 2026-07-06. See [cobusgreyling--llm-wiki](./cobusgreyling--llm-wiki.md) for the current review.

LLM Wiki, from `cobusgreyling/llm-wiki`, is a Python package plus template repository for creating local Markdown wikis maintained by host agents. At the reviewed commit it ships a `wiki` CLI, optional MCP server, scaffolded `AGENTS.md` instructions, page templates, example wikis, BM25 search with optional qmd delegation, lint checks, graph/backlink utilities, raw-source coverage reporting, and Obsidian-oriented docs. The core memory store is not a database: it is a project folder with `raw/`, `wiki/`, `templates/`, and agent instructions.

**Repository:** https://github.com/cobusgreyling/llm-wiki

**Reviewed commit:** [a424e6875aa2d5736d9c0d03d7c28bdbe32892a5](https://github.com/cobusgreyling/llm-wiki/commit/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5)

**Status:** outdated

**Last checked:** 2026-07-06

## Core Ideas

**The package scaffolds a wiki, but the agent protocol maintains the knowledge.** `wiki init` copies a bundled scaffold into a new project and can initialize git; the scaffold includes `AGENTS.md`, `CLAUDE.md`, required wiki files, raw/templates folders, and page templates ([README.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/README.md), [bootstrap.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/bootstrap.py), [scaffold](https://github.com/cobusgreyling/llm-wiki/tree/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/scaffold)). The actual semantic ingest loop is a host-agent procedure: read raw sources, create source pages, update entity/concept pages, revise `synthesis.md`, flag contradictions, update `index.md`, and append to `log.md` ([AGENTS.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/AGENTS.md)).

**The retained memory is an Obsidian-compatible file graph.** Wiki projects keep immutable source material in `raw/`, maintained Markdown pages in `wiki/`, frontmatter and Obsidian wikilinks for structure, `wiki/index.md` as the catalog, `wiki/log.md` as the operation timeline, and `wiki/contradictions.md` as the conflict ledger ([AGENTS.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/AGENTS.md), [docs/ARCHITECTURE.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/docs/ARCHITECTURE.md), [examples/demo](https://github.com/cobusgreyling/llm-wiki/tree/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/examples/demo)).

**Context efficiency is index/search/section-first progressive disclosure.** The query procedure tells the agent to read `wiki/index.md`, search with `wiki search` or MCP `wiki_search`, then read selected pages and sections with `wiki expand <page> --section ...` ([AGENTS.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/AGENTS.md)). The implemented BM25 backend tokenizes Markdown, boosts title and heading terms, ranks pages, and returns snippets; `expand.py` can return one heading block plus outbound links, which is the main token-saving mechanism ([search.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/search.py), [expand.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/expand.py)). Optional qmd search delegates to an external collection; the wiki pages remain source of truth ([search.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/search.py)).

**Governance is structural, not semantic.** `wiki lint` checks required files, broken and ambiguous wikilinks, Markdown links, frontmatter, source-page raw references, raw/source coverage, orphan pages, index gaps, contradiction hints, and repeated code-styled terms that may deserve pages ([lint.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/lint.py), [docs/LINT.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/docs/LINT.md)). It can fail the CLI on errors or warnings, but it does not verify that an agent's source summary, synthesis, or contradiction judgment is faithful.

**The adoption surface is agent-native.** The same operations are exposed as CLI commands and MCP tools: search, expand, lint, list, stats, ingest status, recent log, backlinks, graph, and new-page scaffolding ([cli.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/cli.py), [mcp_server.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/mcp_server.py), [docs/MCP.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/docs/MCP.md)). Obsidian is a first-class human read surface, with Dataview snippets and graph-view guidance for browsing and checking orphans ([docs/OBSIDIAN.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/docs/OBSIDIAN.md)).

## Artifact analysis

- **Storage substrate:** `files` `repo` — User memory persists as Markdown files and frontmatter in `raw/`, `wiki/`, `templates/`, logs, indexes, and examples; the toolkit and scaffold are a git/Python package, and `wiki init --git` can make each wiki a git repo ([bootstrap.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/bootstrap.py), [README.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/README.md)).
- **Representational form:** `prose` `symbolic` — Source summaries, entity/concept pages, answers, synthesis, contradiction notes, AGENTS instructions, docs, and logs are prose; YAML frontmatter, page types, file paths, wikilinks, raw-file mappings, CLI/MCP arguments, lint categories, graph JSON, and search scores are symbolic. I did not find a retained vector store, graph database, or model-weight artifact in this repo; qmd is an optional external backend ([search.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/search.py), [docs/MCP.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/docs/MCP.md)).
- **Lineage:** `authored` `imported` — The toolkit, scaffold, templates, AGENTS policy, and maintained wiki pages are authored by humans or agents; raw files are imported by the human, then source pages and higher-level pages are derived from those imported sources by the agent protocol. The code does not show durable extraction from session transcripts, tool traces, or event streams.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `enforcement` `ranking` — Wiki pages advise later answers as knowledge; `AGENTS.md` and docs instruct the host agent; page types, folders, index rows, wikilinks, raw-file frontmatter, root detection, and MCP tool names route work; lint and init-check validate structure; lint exit codes can enforce CI/agent gates; BM25/qmd search ranks candidate pages ([AGENTS.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/AGENTS.md), [paths.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/paths.py), [lint.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/lint.py), [search.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/search.py)).

**Wiki pages and raw sources.** `raw/` files are supposed to stay read-only; `wiki/sources/` pages summarize one raw document and carry `raw_file`; entity, concept, answer, synthesis, and contradiction pages form the maintained knowledge graph ([AGENTS.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/AGENTS.md), [source template](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/scaffold/templates/source.md), [examples/demo/wiki](https://github.com/cobusgreyling/llm-wiki/tree/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/examples/demo/wiki)).

**Access structures.** `wiki/index.md` is an authored catalog rather than a generated index in the code; backlinks and graph exports are computed by scanning wikilinks, while BM25 scores are computed at read time over Markdown pages ([links.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/links.py), [search.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/search.py)).

**Validation and visibility surfaces.** Lint reports, stats, ingest-status rows, recent log entries, backlinks, and graph JSON are derived views over the file tree. They do not become stronger knowledge claims, but they route repair work and help agents or humans decide what to inspect next ([ingest.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/ingest.py), [stats.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/stats.py), [mcp_server.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/mcp_server.py)).

Promotion path: source material moves from human-curated `raw/` files into source pages and then into entity/concept/synthesis/answer pages through a host agent following `AGENTS.md`. Structural promotion is supported by templates, page types, lint, and search; semantic promotion is not independently checked by the package.

## Comparison with Our System

LLM Wiki and Commonplace share the premise that agent-usable memory can live in ordinary Markdown files, frontmatter, git, links, and local validation tools. Both make agent instructions part of the system surface, keep source material separate from synthesized knowledge, and treat navigation/indexing as a context-efficiency mechanism rather than an afterthought.

The main difference is where authority lands. Commonplace puts more of the durable behavior into collection contracts, type specs, validation, review gates, and controlled comparison vocabularies. LLM Wiki puts more responsibility on the active host agent: `AGENTS.md` tells the agent how to ingest, update, synthesize, flag contradictions, and answer, while the Python package mostly scaffolds, searches, exposes tools, and validates structure. That makes LLM Wiki easier to adopt as a personal Obsidian/agent workflow, but weaker as a governed methodology corpus.

The read path is also narrower. LLM Wiki gives useful pull tools and MCP wrappers, but it does not implement a push engine that automatically injects relevant retained memory into arbitrary future actions. Commonplace's skills and routing conventions are heavier, but they make "why this context was loaded" more inspectable.

### Borrowable Ideas

**Section-level expand as a default agent tool.** Ready now. Commonplace has many long Markdown artifacts; an explicit "expand this page section plus outbound links" command would reduce token load without changing storage.

**Lint categories as repair routing.** Ready now. LLM Wiki's issue categories are concrete enough for an agent to run targeted fix loops, especially for broken links, missing source refs, index gaps, and orphans.

**MCP parity for common read operations.** Useful when Commonplace is operated outside Codex/Claude skill contexts. Search, expand, backlinks, graph, stats, and validation are stable tool surfaces.

**Do not borrow unreviewed semantic ingest authority.** LLM Wiki intentionally lets the agent rewrite the wiki during ingest. Commonplace should keep source ingestion, candidate drafting, review, and durable library promotion separated unless a collection explicitly accepts lower assurance.

**Obsidian-first adoption affordances.** Worth borrowing for reader installs. Dataview snippets, graph-view guidance, and a scaffolded vault make the file-backed model legible to humans without adding a service.

## Write side

**Write agency:** `manual` `automatic` — `manual` covers human source curation, direct wiki edits, questions, and approval of emphasis; `automatic` covers both deterministic package writes such as wiki/new-page scaffolding and the host agent's instruction-driven execution of the `AGENTS.md` ingest/update protocol. The semantically important path is therefore agent-mediated automatic work, not autonomous Python source-processing code.

**Curation operations:** `evolve` `synthesize` `invalidate` — The agent protocol evolves existing entity/concept/source/index/log pages when a new source arrives, revises `synthesis.md` when the overall picture changes, files valuable answers, and records contradictions when new data conflicts with existing claims ([AGENTS.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/AGENTS.md)). Creating a first source/entity/concept page from raw material is acquisition, and deterministic blank-page creation is scaffolding; neither is counted here as a curation operation over already-stored memory. These operations are prompt/procedure-mediated; the inspected Python package detects pending raw files and scaffolds pages, but does not itself extract claims from raw files or merge semantic updates into existing pages ([ingest.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/ingest.py), [new_page.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/new_page.py)).

## Read-back

**Read-back:** `pull` — Retained wiki memory reaches the agent when the agent or user invokes search, expand, list, backlinks, graph, ingest-status, log, or lint tools, or when the host agent follows `AGENTS.md` and deliberately reads index/search results before answering. I did not find an implemented hook, scheduler, or relevance engine that pushes wiki memory into the agent context without such a lookup; static `AGENTS.md` instructions are baseline system definition, not read-back of accumulated memory.

Read-back is still optimized for bounded context. BM25 returns ranked snippets; qmd can be used for external hybrid retrieval; `expand` can load a single section and report outbound links; `list`, backlinks, graph, stats, and ingest status provide smaller inspection surfaces than reading the whole wiki ([search.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/search.py), [expand.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/expand.py), [links.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/links.py), [mcp_server.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/mcp_server.py)). The repo tests search ranking, section extraction, MCP wrappers, ingest coverage, lint, graph/backlink resolution, and path traversal rejection, but not whether retrieved wiki context changes an agent's answer faithfully ([tests](https://github.com/cobusgreyling/llm-wiki/tree/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/tests)).

## Curiosity Pass

**The strongest implementation is the tooling around the wiki, not the wiki compiler.** The README frames LLM Wiki as "knowledge compiled once and kept current," but the inspected package does not implement an autonomous compiler from raw sources into concepts. It gives the agent a schema, tools, and examples for doing that work.

**`wiki/index.md` is more authoritative than generated.** Agents are told to update it during ingest and read it first during queries, while lint only detects index gaps. That makes index quality central and also agent-dependent.

**qmd changes retrieval but not retention.** Optional qmd can add hybrid/vector-like read behavior, but it is an external search layer over wiki pages. The reviewed repo does not own qmd's embeddings or make them part of the wiki's durable artifact model.

**The security boundary is modest but explicit.** Page resolution rejects path traversal and MCP tools return structured error payloads for invalid inputs; that matters because these tools are meant to be called by agents ([links.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/links.py), [test_links_security.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/tests/test_links_security.py), [test_mcp.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/tests/test_mcp.py)).

**No trace-derived placement.** The repo has logs and answer filing, but I did not find durable lesson extraction from session logs, tool traces, or event streams. Query answers become knowledge artifacts when filed; they are not a trace-learning loop.

## What to Watch

- Whether ingest moves from an `AGENTS.md` procedure into package code that extracts claims, updates pages, and records source-span provenance; that would materially change write-side authority.
- Whether `wiki lint` gains semantic checks for source-summary faithfulness, contradiction resolution, or synthesis provenance instead of only structural/file-graph health.
- Whether qmd integration becomes managed state in the toolkit rather than a user-configured external collection; that would add a retained parametric search artifact.
- Whether the MCP server grows push-oriented hooks or subscriptions that inject relevant pages on task start or file changes; that would change the read-back verdict.
- Whether `wiki/index.md` becomes generated or partially generated from frontmatter and links; that would reduce dependence on agent-maintained navigation.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: LLM Wiki stores a file-backed wiki, but accumulated memory is activated only through search, expand, explicit page reads, or agent query procedure.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: raw files, wiki pages, AGENTS instructions, lint reports, indexes, and MCP/CLI tools differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw sources, source summaries, entity/concept pages, answers, synthesis, and contradiction notes mostly advise later work.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: AGENTS.md, page templates, lint rules, CLI/MCP schemas, and path/page-type conventions directly shape future agent behavior.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - explains: LLM Wiki's routing works best when file names, page types, wikilinks, headings, and frontmatter already expose useful symbols.
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) - relates: source-to-wiki compilation and section expansion shift repeated synthesis and navigation work out of the live answer context.
