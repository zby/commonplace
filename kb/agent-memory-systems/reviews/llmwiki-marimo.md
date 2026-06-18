---
description: "llmwiki-marimo review: local Marimo LLM Wiki with generated Markdown pages, SQLite FTS/citation graph, pull chat tools, and repairable wiki memory"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-18"
---

# llmwiki-marimo

llmwiki-marimo, by Clod, is a local-first LLM Wiki implemented as Marimo notebook apps over a framework-agnostic Python core. At the reviewed commit it ingests PDF/DOCX sources, extracts chunks and concepts, writes human-readable Markdown wiki pages, indexes both sources and wiki pages in SQLite FTS5, records citation/link edges, exposes a PydanticAI chat agent that reads wiki pages before raw chunks, lets the human save cited chat answers back into the wiki, and provides lint/repair, eval-packet, trace-report, deletion, and local git snapshot paths.

**Repository:** https://github.com/Clod/llmwiki-marimo

**Reviewed commit:** [0dc8e731df6a4bbb03926b17a891d03736f1267a](https://github.com/Clod/llmwiki-marimo/commit/0dc8e731df6a4bbb03926b17a891d03736f1267a)

**Last checked:** 2026-06-18

## Core Ideas

**The durable memory is a generated encyclopedia, not the raw retrieval cache.** The README's workspace layout has `sources/` for uploaded documents, `wiki/` for generated `index.md`, `overview.md`, `log.md`, `summaries/`, and `concepts/`, plus `.llmwiki/index.db` for the local index. The programmer manual names the same split as filing cabinet versus encyclopedia: SQLite is the search/cache layer, while Markdown is the human-readable wiki the user reads and later chat cites ([README.md](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/README.md), [docs/programmer_manual.md](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/docs/programmer_manual.md), [docs/sqlite_data_dictionary.md](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/docs/sqlite_data_dictionary.md)).

**Ingestion compiles source documents into pages and graph edges.** `ingest_file()` validates a source, extracts page text, chunks it, writes source rows/pages/chunks into SQLite, asks an LLM for structured concepts, creates or updates concept pages, creates a source summary, rewrites the overview, appends the log, updates `index.md`, records references, and optionally commits the wiki folder to the workspace's own git repo ([base/domain/ingestion/pipeline.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/ingestion/pipeline.py), [base/domain/ingestion/wiki_generator.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/ingestion/wiki_generator.py), [base/domain/tools/references.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/tools/references.py)).

**Context efficiency is wiki-first pull retrieval.** The default chat prompt requires retrieval before factual answers and routes the agent through `read_wiki_page("wiki/index.md")`, wiki FTS, and then raw-source chunk search as fallback. The agent factory registers exactly those read tools and no write tool; tests guard that contract ([base/domain/chat/config.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/chat/config.py), [base/domain/chat/agent.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/chat/agent.py), [base/domain/chat/wiki_tools.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/chat/wiki_tools.py), [tests/unit/test_wiki_tools.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/tests/unit/test_wiki_tools.py)).

**Citations are a first-class interface contract, but mostly prompt/parser enforced.** `read_wiki_page()` prefixes returned pages with `[wiki page: <path>]`, search results include wiki paths or source filenames/pages, `document_references` parses footnotes, Sources bullets, and internal Markdown links into `cites` and `links_to` edges, and the chat prompt requires every factual claim to cite retrieved evidence. This is stronger than opaque RAG snippets, but the code does not prove model faithfulness beyond tests for prompt content and tool output shape ([base/domain/chat/wiki_tools.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/chat/wiki_tools.py), [base/domain/chat/tools.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/chat/tools.py), [base/domain/tools/references.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/tools/references.py), [tests/unit/test_wiki_tools.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/tests/unit/test_wiki_tools.py)).

**Human save is the chat-to-memory boundary.** The chat agent can propose a page, but `read_app.py` exposes the actual "Save last response to wiki" form and calls `save_to_wiki()`. That function runs a structuring/merge LLM pass, writes or updates a concept/summary page, rebuilds references, updates `index.md`, and runs scoped lint/repair. The agent itself is deliberately read-only ([marimo/read_app.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/marimo/read_app.py), [base/domain/chat/wiki_tools.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/chat/wiki_tools.py), [tests/unit/test_wiki_tools.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/tests/unit/test_wiki_tools.py)).

**Maintenance is executable, not just advisory.** Lint checks orphans, staleness, missing cross-references, missing concepts, contradictions, data gaps, and filled gaps; repair can delete orphan concept pages, regenerate stale summaries, add cross-links, create missing concepts, flag contradictions, add data-gap notes, and replace filled-gap markers. Source deletion also deletes one-to-one summary pages and marks citing multi-source pages stale ([base/domain/lint/checks.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/lint/checks.py), [base/domain/repair/actions.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/repair/actions.py), [base/domain/repair/runner.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/repair/runner.py), [base/domain/tools/deletion.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/tools/deletion.py)).

## Artifact analysis

- **Storage substrate:** `files` `repo` `sqlite` `graph` — The standing memory spans workspace files (`sources/`, `wiki/`, `wiki_config.toml`), an optional local git repo for the wiki workspace, and `.llmwiki/index.db` with documents, pages, chunks, FTS5, and `document_references` citation/link edges. The graph is represented as SQLite edge rows rather than a separate graph database.
- **Representational form:** `prose` `symbolic` — Markdown source summaries, concept pages, overview, log, prompts, and trace reports are prose; the SQLite schema, FTS rows, citation edges, frontmatter, source hashes, statuses, lint issues, repair actions, config, git operations, tests, and Marimo app code are symbolic. There is no retained vector store or model-weight adaptation at the reviewed commit.
- **Lineage:** `authored` `imported` — Source documents are imported, generated summary/concept/overview pages are LLM-derived from those sources, chat-saved pages are human-approved from a chat answer, and prompts/code/tests/config are authored. Opt-in traces are diagnostic records of runs, but I did not find durable wiki artifacts learned from agent traces, tool trajectories, or session logs.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` — Wiki pages and raw source rows are knowledge artifacts; system prompts and `wiki_config.toml` instruct agent behavior; the path guard, file-type checks, DB constraints, delete/stale behavior, and read-only tool registration enforce boundaries; `index.md`, FTS scopes, page paths, citation edges, and wiki picker state route activity; lint, repair, tests, eval readers, and source freshness checks validate; FTS5 rank orders retrieval candidates.

**Markdown wiki pages.** The central behavior-shaping memory is the generated Markdown under `wiki/`: source-specific summaries, cross-source concepts, overview, log, and index. These pages are the readable encyclopedia the human and chat agent consume, while `create_page()` keeps disk, SQLite document rows, and FTS chunks synchronized ([base/domain/tools/wiki_fs.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/tools/wiki_fs.py)).

**SQLite index and citation graph.** The DB stores both source and wiki documents, raw document pages, chunks, FTS5 virtual search rows, and `document_references` edges for `cites` and `links_to`. The schema comments and data dictionary explicitly call this derived state: useful and queryable, but not a byte-identical rebuild of the wiki without re-running extraction and generation ([database/sqlite_schema.sql](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/database/sqlite_schema.sql), [docs/sqlite_data_dictionary.md](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/docs/sqlite_data_dictionary.md)).

**Agent prompts and config.** `_DEFAULT_SYSTEM_PROMPT` and per-wiki `wiki_config.toml` are system-definition artifacts. They bind the chat agent to corpus-only answering, retrieval before factual claims, wiki-before-source routing, mandatory citations, and user-mediated saving; `create_agent()` registers the read tools that make those instructions actionable ([base/domain/chat/config.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/chat/config.py), [base/domain/chat/agent.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/chat/agent.py), [wiki_config.example.toml](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/wiki_config.example.toml)).

**Lint, repair, deletion, and git snapshots.** Maintenance artifacts have stronger authority than advisory prose when invoked. Repair mutates stored pages and references; deletion cascades source removal and stale marking; git snapshots version only the wiki and `.gitignore`, not raw sources or `.llmwiki/` ([base/domain/repair/runner.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/repair/runner.py), [base/domain/tools/deletion.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/tools/deletion.py), [base/domain/tools/git_ops.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/tools/git_ops.py)).

**Trace artifacts.** When `WIKI_TRACE=1`, ingestion emits `.llmwiki/traces/<run_id>/trace.jsonl` plus content-addressed sidecars for prompts, responses, extracted text, chunks, and generated Markdown. These are observability and debugging artifacts, not replay cassettes or a learning substrate: the code records calls and artifacts, and the trace-report app renders them, but no durable wiki memory is derived from traces ([base/domain/ingestion/trace.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/ingestion/trace.py), [marimo/trace_report_app.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/marimo/trace_report_app.py), [tests/unit/test_trace.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/tests/unit/test_trace.py)).

Promotion path: source PDFs/DOCXs become extracted pages and chunks, then generated summary/concept Markdown, then index entries, reference edges, FTS rows, overview/log updates, and optional local git commits. Chat answers can become wiki pages only after a human presses the save form. The system does not promote memory into executable tools, hard runtime gates for downstream agents, model weights, or vector indexes.

## Comparison with Our System

| Dimension | llmwiki-marimo | Commonplace |
|---|---|---|
| Primary purpose | Personal local LLM Wiki for source documents, reading, chat, and maintenance | Agent-operated methodology KB for Commonplace itself and consuming projects |
| Main artifact | Generated Markdown encyclopedia backed by SQLite index/citation graph | Typed Markdown notes, reviews, instructions, sources, ADRs, indexes, and validators |
| Write path | Source ingest, generated pages, human save form, lint/repair, source deletion, git snapshot | Human/agent authored artifacts, skills, validation, semantic review, curated navigation |
| Read path | PydanticAI tool calls over index page, wiki FTS, read page, raw-source FTS fallback | Agent search, authored links, indexes, type contracts, skills, and review workflows |
| Governance | Prompt contracts, path guard, DB constraints, tests, lint/repair, eval packets, git history | Collection/type contracts, validators, source snapshots, review gates, indexes, and skills |

llmwiki-marimo is close to Commonplace on the local-first and inspectable-artifact axis: both treat Markdown as the readable memory surface and use deterministic tooling around it. The major architectural difference is that llmwiki-marimo has a product app and chat loop: Marimo gives a human reading surface, and PydanticAI gives an embedded agent that can pull memory during a conversation. Commonplace's current read-back is more distributed across agent instructions, search, indexes, and review commands.

The second difference is representational discipline. Commonplace puts type specs and collection contracts in front of authoring; llmwiki-marimo relies more on generation prompts, page conventions, FTS rows, and repair routines. That makes llmwiki-marimo easier to use as a personal document wiki, but weaker as a long-lived methodology corpus where artifact kind and linking semantics must be reviewable before runtime.

The third difference is maintenance posture. Commonplace tends to surface review and validation findings for agents/humans to resolve under explicit contracts. llmwiki-marimo is more willing to apply automatic page mutations: delete orphan pages, add cross-links, regenerate stale summaries, create missing concepts, flag contradictions, and mark pages stale after source deletion.

### Borrowable Ideas

**Embed a wiki-first chat reader over a local KB.** Needs a concrete Commonplace use case. A bounded chat surface that reads curated indexes and notes before raw sources could make ad hoc KB interrogation easier, but it should preserve Commonplace's stronger type and citation contracts.

**Use page-path citation anchors in read tools.** Ready now. `read_wiki_page()` prefixes returned content with the exact wiki path, giving the model a nearby citation token. Commonplace read helpers could use the same pattern when serving notes to agents.

**Keep human approval on chat-to-library writes.** Ready as a design constraint. llmwiki-marimo's read-only chat agent plus explicit save form is a useful boundary for any Commonplace conversational assistant: draft from retrieved evidence, then require a separate write action.

**Pair lint findings with targeted repair actions.** Needs careful policy. Commonplace already has validation and review gates; borrowing targeted repair for safe mechanical changes would help, but content-changing repairs should stay explicit because Commonplace's artifacts often carry system-definition authority.

**Make optional trace reports inspectable without treating them as learning.** Ready for debugging workflows. llmwiki-marimo's trace sidecars and join map are useful observability, while the absence of trace-derived memory avoids silently upgrading diagnostics into authority.

## Write side

**Write agency:** `manual` `automatic` — Humans add source files, choose saves from chat, can edit generated Markdown, run apps, and manage git remotes; the system automatically imports/extracts/chunks sources, generates and updates wiki pages, rewrites overview/log/index files, syncs DB chunks and references, records traces when enabled, runs lint/repair when invoked, deletes or stales dependent pages on source deletion, and optionally creates local git commits.

**Curation operations:** `evolve` `synthesize` `invalidate` — Automatic maintenance can modify existing memory by merging new concept insights, adding cross-references, appending contradiction/data-gap markers, replacing filled-gap markers, regenerating stale summaries, and syncing references. It synthesizes a narrative `overview.md` across the current overview, new summary, and concept list during ingest. It invalidates or demotes stored memory by marking citing pages stale when a source is deleted and by deleting one-to-one derived summaries that no longer have a source. I did not find automatic deduplication, recurrence promotion, age/capacity decay, or trace-derived learning.

## Read-back

**Read-back:** `pull` — Retained wiki memory reaches the PydanticAI agent when the agent deliberately calls its read/search tools during a chat turn; baseline prompts are installed instructions, and Marimo page browsing is a human read surface, not automatic memory push into the agent.

The implemented retrieval cascade is `read_wiki_page("wiki/index.md")`, `search_wiki_fts`, likely `read_wiki_page` calls for pages found there, and `search_source_chunks` as fallback. Wiki and source search both use SQLite FTS5 over `document_chunks`; there is no vector retrieval, reranker, MCP server, token-budgeted prompt compiler, or automatic pre-invocation context injection at the reviewed commit ([base/domain/chat/config.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/chat/config.py), [base/domain/tools/search.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/tools/search.py), [base/domain/chat/tools.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/chat/tools.py)).

Selection is bounded by tool calls and `limit` parameters, not by a global context budget. The design controls complexity by asking the agent to read the index and curated pages first and raw chunks only when the wiki is insufficient. Effective faithfulness remains prompt-and-test based: tests assert the grounding and citation mandate exists, but the system does not run a behavioral ablation proving that retrieved memory changed the answer.

Other consumers matter. The same retained memory is also read directly by the human in the Marimo read app, by lint/repair routines, by eval-packet builders, by trace reports, by git history, and by source deletion logic.

## Curiosity Pass

**The DB is both derived and not trivially rebuildable.** Documentation calls SQLite derived state, but also notes that rebuilding is not a passive reindex: it re-invokes extraction/generation and can overwrite Markdown or lose DB-only fields. That is a sharper caveat than the README's "delete `.llmwiki/` anytime" framing suggests ([README.md](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/README.md), [docs/sqlite_data_dictionary.md](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/docs/sqlite_data_dictionary.md)).

**The graph exists, but graph retrieval does not.** `document_references` records citation and link edges, powers orphan/stale/cross-reference checks, and can provide backlinks/forward refs. The chat agent does not yet use graph traversal as a retrieval strategy; it uses index/page reads and FTS.

**Trace capture is intentionally not memory learning.** The trace system records enough to inspect LLM/data flow and join events to DB rows, but the module comments explicitly reject record/replay and the pipeline never distills traces into future instructions or pages. This avoids the common ambiguity where observability logs are mistaken for retained learning.

**Repair has real authority despite being user-invoked.** The runner is not just a report generator: it deletes pages, rewrites summaries, creates pages, and appends markers. From a memory-system perspective, "manual command invocation" still exposes automatic curation once the command runs.

**Security is concentrated around the LLM-callable reader.** `read_wiki_page()` resolves paths and rejects escapes outside `wiki/`, with tests for parent traversal and deep traversal. I did not audit every non-agent file operation for equivalent path confinement, but the highest-risk LLM-callable path is explicitly guarded ([base/domain/chat/wiki_tools.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/base/domain/chat/wiki_tools.py), [tests/unit/test_wiki_tools.py](https://github.com/Clod/llmwiki-marimo/blob/0dc8e731df6a4bbb03926b17a891d03736f1267a/tests/unit/test_wiki_tools.py)).

## What to Watch

- Whether graph traversal becomes part of the chat agent's retrieval path. That would change the context-efficiency story from index/FTS pull to graph-assisted pull.
- Whether a passive "reindex from existing wiki files" path appears. That would make SQLite more safely derived and reduce rebuild risk for manually edited pages.
- Whether lint/repair gains an explicit review queue before destructive/content-changing repairs. That would make automatic curation safer for higher-authority wiki pages.
- Whether eval packets become enforced gates for model or prompt changes. That would upgrade eval artifacts from reporting to enforcement.
- Whether an MCP or CLI retrieval surface is added for external agents. That would broaden read-back beyond the embedded PydanticAI/Marimo app.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - classifies: llmwiki-marimo stores durable wiki memory, but the chat agent activates it by pull tool calls.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: the system separates Markdown knowledge, SQLite indexes, citation edges, prompts, repair actions, traces, and git snapshots by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: generated pages, source rows, raw chunks, trace reports, and eval packets serve as evidence/reference unless a tool consumes them with stronger force.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: prompts, path guards, lint/repair routines, DB constraints, source deletion rules, and tests carry instruction, enforcement, routing, validation, or ranking force.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - relates: retrieval works best when page paths, source names, concept titles, index entries, citations, and lexical query terms are available as symbols.
