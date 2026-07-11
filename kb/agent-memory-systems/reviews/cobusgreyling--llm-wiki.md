---
description: "LLM Wiki review: file-backed agent-maintained markdown wiki with scaffolded instructions, BM25/qmd search, linting, and pull-only read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-07-06"
---

# LLM Wiki (cobusgreyling)

LLM Wiki, from Cobus Greyling's `cobusgreyling/llm-wiki` repository, is a Python toolkit and project scaffold for Karpathy-style LLM-maintained markdown wikis. It ships `wiki` CLI commands, an MCP server, templates, examples, and agent instructions that make a host coding agent maintain `raw/` source files, `wiki/` pages, links, index, synthesis, contradictions, and log as an inspectable file-backed knowledge base.

**Repository:** https://github.com/cobusgreyling/llm-wiki

**Reviewed commit:** [a424e6875aa2d5736d9c0d03d7c28bdbe32892a5](https://github.com/cobusgreyling/llm-wiki/commit/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5)

**Last checked:** 2026-07-06

## Core Ideas

**The retained memory is a markdown wiki, not a hidden database.** A scaffolded project separates immutable `raw/` sources from LLM-maintained `wiki/` pages: `index.md`, `log.md`, `synthesis.md`, `contradictions.md`, and typed-ish subdirectories for entities, concepts, sources, and answers ([README.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/README.md), [docs/ARCHITECTURE.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/docs/ARCHITECTURE.md), [src/llm_wiki/scaffold/](https://github.com/cobusgreyling/llm-wiki/tree/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/scaffold)). The package can initialize that tree and optionally initialize git, but the durable knowledge remains ordinary files ([src/llm_wiki/bootstrap.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/bootstrap.py)).

**The semantic ingest loop is delegated to the host agent.** The README says the agent reads a source, extracts key information, and integrates it into the persistent wiki. The implementation boundary is narrower: `wiki ingest-status` only compares files in `raw/` with `wiki/sources/` pages through `raw_file` frontmatter, while `AGENTS.md` tells the host agent how to create source pages, update entities/concepts, revise synthesis, flag contradictions, update the index, and append to the log ([README.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/README.md), [AGENTS.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/AGENTS.md), [src/llm_wiki/ingest.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/ingest.py), [src/llm_wiki/cli.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/cli.py)). The system therefore supplies a maintainer protocol and tooling, not a deterministic semantic ingestion engine.

**Context efficiency is index-first pull plus section-level expansion.** Query instructions tell the agent to read `wiki/index.md`, search with `wiki search`, expand relevant pages, and use `wiki expand <page> --section` to load one heading block at a time ([AGENTS.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/AGENTS.md), [src/llm_wiki/expand.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/expand.py)). Built-in BM25 scores markdown pages with title and heading boosts; optional qmd delegates to an external hybrid search collection while keeping wiki pages as the source of truth ([src/llm_wiki/search.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/search.py), [README.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/README.md)). It controls volume by choosing pages/sections; it does not bound semantic complexity beyond that selection.

**Validation is structural and graph-oriented.** `wiki lint` checks required files, frontmatter shape, source/raw coverage, wikilink resolution, markdown links, ambiguous slugs, orphans, index gaps, repeated backticked terms, and contradiction/staleness hints ([src/llm_wiki/lint.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/lint.py), [docs/LINT.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/docs/LINT.md)). That gives the agent a repair surface, but the code does not validate whether an entity page faithfully summarizes a raw source or whether synthesis claims have source-spans.

**Adoption is deliberately native to common agent and note-taking surfaces.** `wiki init` packages `AGENTS.md`, `CLAUDE.md`, MCP configs for Cursor/Claude/Windsurf/OpenCode-style clients, templates, and Obsidian-friendly wikilinks; the MCP server exposes search, expand, lint, list, stats, ingest status, logs, backlinks, graph, and page creation as JSON tools ([src/llm_wiki/bootstrap.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/bootstrap.py), [src/llm_wiki/mcp_server.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/mcp_server.py), [docs/MCP.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/docs/MCP.md), [docs/OBSIDIAN.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/docs/OBSIDIAN.md)). The trust affordance is inspectability: users can browse files, run lint, view links, and use git if initialized.

## Artifact analysis

- **Storage substrate:** `files` — The standing memory store is a project directory of markdown files, templates, raw source files, and optional git history; the Python package reads and writes files rather than maintaining a database.
- **Representational form:** `prose` `symbolic` — Wiki pages, source summaries, synthesis, answers, logs, and instructions are prose; YAML frontmatter, wikilinks, directory placement, CLI/MCP schemas, lint categories, and BM25 scoring code are symbolic. Optional qmd integration can query an external embedding/hybrid retrieval collection, but the reviewed repository does not own that parametric state.
- **Lineage:** `authored` `imported` `other-compiled` `trace-extracted` — Raw files are imported unchanged by the human; wiki pages, templates, AGENTS instructions, and examples are authored; source summaries, synthesis, index entries, contradictions, answers, backlinks, graph exports, lint reports, and search indexes are compiled from retained raw/wiki material; `wiki/log.md` entries are trace-extracted operation evidence because the shipped protocol records ingest/query/lint actions there. The log does not make the system trace-derived learning, because no code path mines those traces into lessons, rules, skills, rankings, or other learned behavior-shaping artifacts.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` — The authority families split between knowledge artifacts and system-definition artifacts: wiki pages advise agents and humans as knowledge artifacts, while `AGENTS.md`, `CLAUDE.md`, templates, path conventions, lint checks, and search/ranking code shape behavior through instruction, routing, validation, and ranking.

**Wiki pages and raw sources.** The central retained artifacts are source summaries, entity pages, concept pages, synthesis, answers, contradictions, index, and log. Source pages carry `raw_file` frontmatter, and examples show source summaries linking outward to concepts/entities and back to the raw file ([examples/demo/wiki/sources/karpathy-llm-wiki-gist.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/examples/demo/wiki/sources/karpathy-llm-wiki-gist.md), [examples/demo/wiki/synthesis.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/examples/demo/wiki/synthesis.md), [examples/demo/wiki/index.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/examples/demo/wiki/index.md)). Their authority is knowledge context: useful if read, not self-enforcing.

**Agent instructions and templates.** `AGENTS.md` is a system-definition artifact: it defines the schema, page types, ingest/query/lint procedures, naming, frontmatter, cross-reference rules, and human/agent division of labor. Templates under `src/llm_wiki/scaffold/templates/` give new pages structured symbolic/prose slots, while `wiki new` only instantiates those templates and reminds the caller to update the index and links ([AGENTS.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/AGENTS.md), [src/llm_wiki/scaffold/templates/](https://github.com/cobusgreyling/llm-wiki/tree/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/scaffold/templates), [src/llm_wiki/new_page.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/new_page.py)). Effective compliance depends on the host agent reading and following the prose.

**Search, expand, links, graph, and MCP tools.** BM25 search builds a corpus over `wiki/*.md`, boosts headings, returns snippets, and can delegate to qmd; expand resolves a page and optionally returns a single heading block with outbound links; link helpers resolve Obsidian wikilinks, backlinks, and graph exports; MCP wraps the same functions as JSON tools ([src/llm_wiki/search.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/search.py), [src/llm_wiki/expand.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/expand.py), [src/llm_wiki/links.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/links.py), [src/llm_wiki/mcp_server.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/mcp_server.py)). These are routing and ranking artifacts: they decide what is cheap to discover, not what is true.

**Lint and status reports.** `wiki lint`, `wiki ingest-status`, `wiki stats`, `wiki log`, and `wiki watch` expose health and maintenance state. They validate and report structural properties, raw/source coverage, and recent operation history, but they do not perform semantic repair or distill operation traces into new memory themselves ([AGENTS.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/AGENTS.md), [src/llm_wiki/lint.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/lint.py), [src/llm_wiki/ingest.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/ingest.py), [src/llm_wiki/stats.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/stats.py), [src/llm_wiki/watch.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/watch.py)).

**Promotion path.** The intended path is raw source -> source page -> entity/concept updates -> synthesis/contradictions/index -> optional answer pages. That promotion exists as an agent procedure and example corpus, not as deterministic package code. The strongest implemented promotion is structural: qmd or BM25 makes existing wiki pages more discoverable, and lint turns missing/broken structure into actionable repair signals.

## Comparison with Our System

| Dimension | LLM Wiki | Commonplace |
|---|---|---|
| Primary purpose | Scaffold a general personal/team markdown wiki that a host LLM maintains | Maintain a typed methodology KB and framework for agent-operated KBs |
| Canonical substrate | Plain files under `raw/`, `wiki/`, and templates, with optional git | Git-tracked markdown collections, type specs, validators, sources, reviews, and instructions |
| System-definition surface | Single `AGENTS.md`, scaffold templates, CLI/MCP tool schemas, lint rules | Collection contracts, type specs, skills, validators, review gates, commands, and generated indexes |
| Write path | Host agent follows prose ingest/query/lint instructions; toolkit scaffolds and checks | Agents write typed artifacts under collection contracts, with deterministic validation and review workflows |
| Read-back | Pull through index, lexical/qmd search, expand, list, backlinks, graph, and Obsidian | Mostly pull through `rg`, indexes, links, skills, snapshots, validation output, and explicit review runs |
| Governance | Lint, init-check, source/raw coverage, git if initialized | Stronger schema/type validation, link checks, semantic review, source snapshots, and workflow-specific gates |

The closest alignment is file-first agent knowledge: both systems keep behavior-shaping knowledge in ordinary markdown that agents can read, edit, validate, and version. LLM Wiki is the lighter pattern: one scaffolded `AGENTS.md` tells a general host agent how to maintain a wiki, while Commonplace breaks authority into collection contracts, type specs, commands, skills, validators, and reviews.

The main tradeoff is adoption friction versus methodological precision. LLM Wiki is easy to start and explain: drop files into `raw/`, let an agent maintain `wiki/`, browse in Obsidian, and use CLI/MCP tools for search and lint. Commonplace has heavier vocabulary and more operational ceremony, but the added type and review surface makes it harder for an agent to silently turn raw material into ungrounded permanent claims.

### Borrowable Ideas

**Packaged agent configs as part of project initialization.** LLM Wiki's scaffold creates MCP configs and agent-facing instructions in the same operation as the wiki tree. Commonplace already has initialization machinery, but keeping connector setup and first-run instructions as visible scaffold artifacts is ready now.

**Section-level expansion as a default read primitive.** `wiki expand --section` gives agents a cheap way to load one heading block plus outbound links. Commonplace can make the same read shape more prominent for large notes and reviews; ready now.

**Raw/source coverage as an operator-facing status command.** `wiki ingest-status` is intentionally simple: raw file, source page, status. Commonplace has richer source machinery, but a small status view for "what raw material still lacks an analyzed artifact" would be useful when source capture grows; ready for a concrete workflow.

**Do not borrow semantic ingest without stronger provenance.** The claim that a source update touches many linked pages is useful, but Commonplace should not make that a default automatic path without source spans, review state, and validation hooks. Needs a concrete use case and quality gates.

**Obsidian as a first-class human read path.** LLM Wiki treats Obsidian graph browsing as part of the UX rather than an afterthought. Commonplace can borrow the emphasis where humans need to inspect graph shape, but should keep agent-facing navigation optimized for bounded context rather than visual browsing.

## Write side

**Write agency:** `manual` `automatic` — Humans curate `raw/` and can edit the wiki directly; host agents author and edit `wiki/` pages by following `AGENTS.md`; users can also invoke deterministic scaffold/page-creation helpers. The package does not implement an autonomous Python semantic compiler, so the semantically important automatic path is instruction-mediated host-agent work rather than package-owned extraction code.

**Curation operations:** `evolve` `synthesize` `invalidate` — The instructed ingest path updates existing entity/concept/source/index/log pages in light of new sources, revises `synthesis.md`, files useful answers, and records contradictions. These operations are behavior-shaping parts of the shipped agent protocol, but their semantic quality is not verified by the Python implementation.

The instructed ingest procedure asks the host agent to create source pages, update entity/concept pages, revise synthesis, flag contradictions, update the index, and append to the log. Those are real behavior-shaping instructions, but the inspected Python code does not deterministically perform consolidation, contradiction invalidation, or synthesis over existing wiki memory. Effective write quality is therefore not verified from code.

## Read-back

**Read-back:** `pull` — Retained wiki memory reaches future work when a human or agent deliberately reads `wiki/index.md`, runs `wiki search`, calls MCP tools, expands a page/section, lists pages, follows backlinks, exports the graph, or browses in Obsidian. I found no code path that automatically pushes accumulated wiki content into an agent prompt based on the current task.

Static `AGENTS.md` loading is not memory read-back: it is shipped baseline instruction, not retained knowledge accumulated from use. The query procedure instructs an agent to perform a pull sequence - index first, search, expand, synthesize - and the MCP server makes that sequence easier, but the receiving agent still has to call the tools or read the files ([AGENTS.md](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/AGENTS.md), [src/llm_wiki/mcp_server.py](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/mcp_server.py)).

The read path is context-efficient at the page/section level, not at the claim level. BM25/qmd can rank candidate pages, and `expand --section` avoids loading a whole long page, but there is no tested faithfulness mechanism showing that retrieved memory changed a later answer or action.

## Curiosity Pass

**The README's "compiled once" claim depends on the host agent.** The package does not itself compile raw sources into the wiki; it provides instructions, examples, and tools for an agent to do so. That is a valid agent-operated design, but it should be evaluated as instruction-mediated maintenance rather than deterministic ingestion.

**The schema is mostly prose plus conventions.** Frontmatter types, directory names, and wikilinks are machine-checkable only in limited ways. That keeps the system flexible and easy to start, but many quality claims - accurate extraction, complete updates, contradiction handling, source faithfulness - remain dependent on agent judgment.

**The operation log is evidence, not learned memory.** `wiki/log.md` records ingest/query/lint events and can be listed, but the inspected code does not mine it into new rules, summaries, skills, or retrieval weights. It is an operation trace surface without trace-derived learning.

**qmd is an optional access layer, not the core architecture.** The README presents qmd as a scale path when BM25 misses paraphrase. The implemented qmd backend delegates search to an external CLI and collection; the wiki files still remain authoritative.

**The system is strongest as an adoption bridge.** It turns the Karpathy pattern into something installable, inspectable, and agent-addressable. It is weaker as a provenance-governed knowledge system unless the operator adds source-review discipline on top.

## What to Watch

- Whether semantic ingest becomes an implemented command or packaged agent loop; that would change the write-side classification from manual authoring toward automatic curation and require curation-operation tokens.
- Whether source pages gain per-claim provenance spans or source-section links; without them, compiled wiki claims remain harder to audit than the raw files they summarize.
- Whether qmd indexing becomes initialized, refreshed, and invalidated by `llm-wiki` itself; that would make parametric retrieval an active retained artifact rather than an optional external access layer.
- Whether MCP evolves from pull tools into task-triggered context injection; that would change read-back from pull-only toward push or both.
- Whether lint expands from structural health into semantic checks, such as source coverage by claim, contradiction verification, or synthesis freshness; that would move more governance from instruction to validation/enforcement.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: LLM Wiki stores and retrieves wiki memory, but the reviewed implementation remains pull-only.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: raw files, wiki pages, AGENTS instructions, lint rules, search scores, and MCP tools carry different forms and authorities.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - grounds: LLM Wiki's index/search/section-expand path is mainly a context-efficiency design.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: wiki pages, source summaries, synthesis, answers, and operation logs mostly advise rather than enforce.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: `AGENTS.md`, templates, lint rules, and MCP/CLI command schemas shape future agent behavior.
