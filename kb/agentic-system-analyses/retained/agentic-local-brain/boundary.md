---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Agentic Local Brain's shipped knowledge collection, mining, wiki and retrieval application at commit 41ea0cb104686eb0d39f32c94c2b84d37cdff0e7."
run-id: AAS-2026-10-12-agentic-local-brain-f00cbd577178-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "41ea0cb104686eb0d39f32c94c2b84d37cdff0e7"
analysis-cutoff: "2026-10-12"
evidence-tier: code-grounded
source:
  identity: https://github.com/agent-creativity/agentic-local-brain
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/agentic-local-brain-f00cbd577178/related-systems/agent-creativity--agentic-local-brain
  revision: 41ea0cb104686eb0d39f32c94c2b84d37cdff0e7
  sha256: null
---

# Agentic Local Brain boundary

## Boundary and evidence

This run analyses the shipped personal knowledge application, including the
agent-facing collection instructions, rather than only its Python collector
API. Its intended use is to retain material from files, webpages, papers,
emails, bookmarks and notes, derive searchable and synthesized state, and
later retrieve or browse that state. This purpose is declared in SRC-1
`README.md` and implemented through the entry points and consumers below.

The target is a **memory/knowledge/context-engineering system**. It is in
scope because its own code calls models to transform collected content and
to answer questions using retained content. It is not classified as the
enclosing desktop-agent runtime: the collection skill supplies instructions
for that host, while the application also has its own model-dependent paths
(SRC-1 `skills/localbrain-collect/SKILL.md`, `kb/processors/wiki_compiler.py`,
`kb/query/rag.py`).

> response = litellm.completion(**kwargs)
> answer = response.choices[0].message.content
> return answer
> --- `kb/query/rag.py`

The boundary kind is **whole-system** for this knowledge application. It
includes the material shipped paths that admit, persist, derive, maintain
and consume knowledge, not just a cloned repository or a library interface.
The repository's development-agent scaffolding is a separate engineering
workflow, not the application's user knowledge store. Its exclusion is
explicit in the coverage table; it does not exclude the collection skill,
RAG prompts, mining drivers or wiki maintenance paths.

### Entry points and state loop

- **Admission and persistence:** `pyproject.toml` registers both `localbrain`
  and `kb` to `kb.cli:cli`; `kb/cli.py` registers collection, search, mining,
  wiki, graph, topics, management and backup commands. The collection driver
  calls collectors, reads their saved material, applies extraction, writes
  metadata and tags to SQLite, and calls the chunk/embedding indexing helper.
  The base collector writes Markdown with YAML frontmatter. Chunk text and
  embeddings go to Chroma, while chunk records also go to SQLite. These
  shipped drivers belong to the target, not to an excluded caller (SRC-1
  `pyproject.toml`, `kb/cli.py`, `kb/commands/collect.py`,
  `kb/collectors/base.py`, `kb/commands/utils.py`,
  `kb/storage/chroma_storage.py`, `kb/storage/sqlite_storage.py`).
- **Derivation and maintenance:** the CLI mining driver reads existing
  knowledge records and document files, then invokes entity extraction,
  document embeddings, relations, topics and wiki compilation. The web
  mining route invokes a separate batch runner with progress and history
  state. Both are included; their behavior must not be assumed identical.
  The per-document background worker's implementation is also included,
  without claiming from its presence that every admission path invokes it
  (SRC-1 `kb/commands/mine.py`, `kb/web/routes/mining.py`,
  `kb/processors/mining_runner.py`, `kb/processors/mining_worker.py`).
- **Durable synthesis and later browsing:** the wiki compiler calls its
  provider, renders Markdown, writes articles, and saves article metadata
  including source document IDs to SQLite. The shipped wiki route later
  reloads article metadata and reads the Markdown file, enriching the result
  with source documents and entities. Wiki CLI compilation and viewing also
  belong to the target (SRC-1 `kb/processors/wiki_compiler.py`,
  `kb/web/routes/wiki.py`, `kb/commands/wiki.py`).
- **Retrieval and conversational reuse:** the CLI's RAG command calls
  `RAGQuery.query`; the web chat route calls `RetrievalPipeline.run` through
  application-owned dependency construction. The latter loads conversation
  history, runs retrieval/context stages, and stores user and assistant
  turns. Its conversation manager persists those turns to a separate SQLite
  database. Reading-history recording and recommendation consumers are also
  included (SRC-1 `kb/commands/search.py`, `kb/query/rag.py`,
  `kb/web/routes/search.py`, `kb/web/dependencies.py`,
  `kb/query/retrieval_pipeline.py`, `kb/query/conversation.py`,
  `kb/query/reading_history.py`, `kb/processors/recommendation.py`).
- **Operator and agent surfaces:** FastAPI registers the application's
  routes and serves its shipped frontend and documentation. The frontend
  calls item, graph, topic, mining, chat, conversation, wiki and backup
  endpoints. The collection skill routes user intent to the CLI and gives
  fallback instructions when direct webpage collection fails. These are
  included as executable callers or declared instructions, respectively
  (SRC-1 `kb/web/app.py`, `kb/web/static/index.html`,
  `skills/localbrain-collect/SKILL.md`,
  `kb/web/static/docs/skills/localbrain-collect/SKILL.md`,
  `kb/web/static/docs/skills/knowledge-collect-localbrain/SKILL.md`).
- **Retention operations:** item edits/deletion, tag management, export,
  backups/restoration, scheduler startup/shutdown, configuration and
  installation/update paths remain in scope. Initial tracing includes item
  updates and the scheduler's dispatch to the backup driver, which walks
  retained files into an archive (SRC-1 `kb/web/routes/items.py`,
  `kb/cli.py`, `kb/scheduler/backup_scheduler.py`,
  `kb/commands/backup.py`, `kb/web/app.py`).

Minimum implementation passages supporting the retained-state boundary:

> file_path = target_dir / filename
> file_path.write_text(full_content, encoding="utf-8")
> --- `kb/collectors/base.py`

> file_path.parent.mkdir(parents=True, exist_ok=True)
> file_path.write_text(markdown, encoding="utf-8")
> --- `kb/processors/wiki_compiler.py:567-568`

> conversation_history = self.conversation_manager.format_history_for_prompt(
>     effective_session_id, max_turns=max_history_turns
> )
> --- `kb/query/retrieval_pipeline.py`

The agent-facing fallback crosses into the excluded host's capabilities;
those capabilities are not attributed to Local Brain:

> **Use the agent's own browser/fetch capabilities first**: If the agent has access to a browser tool or fetch tool (e.g., `mcp_fetch_fetch`, `agent-browser`, or similar), use it to retrieve the page content directly.
> --- `skills/localbrain-collect/SKILL.md`

### Top-level tracked coverage

All rows refer to SRC-1 at the reviewed commit. Included means part of the
functional/evidence boundary, not a claim that every line has already been
inspected. Initial inspection consists of the repository tree, bounded
source reads and source searches used to trace the loop above. The table
separates deliberate exclusions from included material still needing detailed
inspection. No material knowledge-application path was inaccessible.

| Top-level tracked path | Classification and material paths | Role and initial inspection; limit or prevented conclusion |
|---|---|---|
| `.claude/` | Excluded: `settings.json`, `hooks/session-start.py`, `hooks/inject-subagent-context.py`, `hooks/inject-workflow-state.py`, Trellis agents, commands, skills and references | Development-agent context injection and coding workflow. Settings and hook references inspected to establish this distinction. Exclusion prevents conclusions about the development team's agent coordination or engineering-memory effectiveness. |
| `.env.example` | Included: configuration declaration | Provider/environment setup; listed, not yet inspected in detail. No conclusion about secret handling from this initial inventory. |
| `.gitignore` | Excluded: repository hygiene | Tracked-file inventory establishes presence; no application entry point. Exclusion prevents assessing repository ignore policy, not the knowledge loop. |
| `.trellis/` | Excluded: `workflow.md`, `scripts/task.py`, `scripts/get_context.py`, `scripts/add_session.py`, `scripts/common/`, `spec/`, `tasks/`, `workspace/`, configuration and template metadata | Development specs, tasks and developer journals, distinct from user knowledge. Workflow and hook references inspected. Exclusion prevents assessing Trellis's cross-session development memory or task lifecycle. |
| `AGENTS.md` | Included as design context only | Coding-agent project description and application module map inspected; engineering instructions are not the application's knowledge-admission policy. No claim of enforcement by the external coding host. |
| `CHANGELOG.md` | Included as reported version history | Listed; detailed release assertions not yet inspected or accepted as behavior. No runtime conclusion from version history alone. |
| `CLAUDE.md` | Included as design context only | Same project and module-map content inspected; coding context, not evidence that a desktop agent obeys the collection skill. |
| `README.md` | Included: installation, collection, extraction, mining, RAG, wiki, backup and architecture declarations | Read for intended use, surfaces and dependencies. Documentation promises are not substituted for implementation or run results. |
| `README.zh-CN.md` | Included: alternate-language documentation | Listed, not yet inspected in detail. No independent evidence layer or translation-equivalence claim. |
| `VERSION` | Included: build version input | Consumption identified in `pyproject.toml`; content not yet inspected. Revision, not version label, is the evidence pin. |
| `docs/` | Included: design, architecture, features, guides, development/test reports, releases, troubleshooting, plans/specs, blog/meta and assets | Tree inventoried; root README supplies the initial architecture/design account. Individual documents and image contents not yet inspected. Reports may later support attributed reported operation, not observed execution without inspectable artifacts. |
| `examples/` | Included: `usage_file_collector.py`, `usage_webpage_collector.py`, `usage_bookmark_collector.py` | Shipped programmatic admission callers, not external applications. Imports/call sites searched and webpage example read; remaining details not yet inspected. Examples have not been executed. |
| `kb/` | Included: `cli.py`; `commands/collect.py`, `search.py`, `mine.py`, `wiki.py`, `manage.py`, `backup.py`, `utils.py`, graph/topics/init/doctor/update/uninstall commands | Application-owned admission, persistence, consumption and operator drivers. Registration and core collection/search/mining/wiki/backup paths inspected; remaining command details are included for later tracing. |
| `kb/` continued | Included: `collectors/`; `processors/` extraction, chunking, embedding, entity/relation/topic mining, wiki prompts/compilation, recommendations and built-in fallback | Base file write, indexing helper, batch and per-document mining implementations, wiki generation/persistence and recommendation interface inspected or searched. Other collector/provider algorithms and wiki staleness details remain to be inspected; no reliability or synchronization guarantee is established here. |
| `kb/` continued | Included: `storage/sqlite_storage.py`, `storage/chroma_storage.py`; `query/` keyword/semantic/RAG, retrieval pipeline, context builder, query expander, reranker, prompts, conversations, reading history, graph/topic queries and models | SQLite schemas and storage APIs searched; Chroma persistence, RAG model call, enhanced retrieval/history persistence and prompt manager inspected. Lower-level query/enrichment algorithms remain included but not yet fully inspected. |
| `kb/` continued | Included: `web/app.py`, `web/dependencies.py`, all `web/routes/`, `web/static/index.html`, settings JS/templates, backup page, static docs/skills and frontend libraries | Shipped HTTP and browser callers. App registration, dependency construction, chat, wiki reads, item edits, mining dispatch and frontend endpoint calls inspected/search-traced. Remaining route bodies, static docs and vendored frontend-library internals are not yet inspected; no frontend correctness/security claim. |
| `kb/` continued | Included: `config.py`, `config-template.yaml`, package/version/update modules, `scheduler/backup_scheduler.py` | Configuration, lifecycle and retained-state operations. Scheduler startup/shutdown and backup dispatch inspected; remaining configuration/update/restore details await inspection. No end-to-end restore or upgrade success claim. |
| `localbrain.spec` | Included: binary packaging entry and data/import declarations | Searched for `kb/cli.py` and bundled assets. Actual binary contents and installed behavior unavailable in this source-only run. |
| `pyproject.toml` | Included: console entry points, dependencies, package data and test configuration | Read completely. Supports declared distribution/entry points, not proof of a successful installation. |
| `requirements.txt` | Included: dependency declaration | Listed, not yet reconciled with project metadata. Dependency implementations are external to this frozen repository. |
| `scripts/` | Included: Python/binary installers and build/release scripts; documentation organization helper as engineering support only | Build/release and installer references searched to trace the CLI artifact and update metadata. Other platform variants and helper bodies not yet inspected. Remote release bytes and deployed skills are not frozen by these scripts. |
| `skills/` | Included: `localbrain-collect/SKILL.md`, `package.json` | Collection intent routing, extraction defaults, host-assisted fallback and command references inspected/search-traced. Package metadata not yet inspected. Instructions support declared agent workflow, not observed host compliance. |
| `tests/` | Included: collector/storage/chunking/embedding/mining/graph/topics/recommendation/retrieval/cache/CLI/web/config/update/install tests; `test_data/` and generation/cleanup/processing drivers | Tree inventoried and mining/retrieval/model-service test definitions searched. Retrieval fixture and mocked answer test read. Data-generation and cleanup callers remain included, not excluded merely because they sit under tests. They and other test bodies await detailed inspection. No test was run and no pass-rate, retrieval-quality or causal-effect claim follows. |

### Frozen evidence and limits

The sole frozen evidence source is SRC-1, canonical repository
`https://github.com/agent-creativity/agentic-local-brain` at full commit
`41ea0cb104686eb0d39f32c94c2b84d37cdff0e7`. The acquired checkout's HEAD was
checked against this pin. The absolute checkout path is only an access root.
The applicability cutoff is **2026-10-12**; later commits, moving hosted
installation/skill URLs and deployed releases are not evidence for this run.
There is no separate capture, execution trace or experimental result.

The overall evidence tier is **code-grounded**, with doctrine/design from
shipped documentation and instruction text. Tests are inspectable test
implementations, not supplied observed runs. Initial test inspection includes
mocked model responses (SRC-1 `tests/test_retrieval_pipeline.py`), so it cannot
establish actual model quality or deployment success.

External dependencies include the desktop/CLI agent host and its browser or
fetch tools; network content providers; model and embedding services accessed
through LiteLLM/OpenAI/DashScope interfaces; and third-party storage, web,
parsing and scheduling libraries. Optional backup services and the release
server are also external. Their declarations and repository-side adapters
remain included (SRC-1 `pyproject.toml`, `README.md`,
`skills/localbrain-collect/SKILL.md`, `kb/query/rag.py`,
`kb/commands/backup.py`, `scripts/python_installer/install.sh`). Their
implementations, service state, credentials, downloaded artifacts and host
sessions were not acquired. This prevents conclusions about provider
availability, host enforcement, restricted-site fetch success, deployed skill
identity, installed cross-platform behavior and actual cloud backup success.

User knowledge stores, runtime logs and conversation databases from a real
installation were not supplied. This prevents conclusions about observed
retention durability, successful reconstruction after restart, knowledge or
answer quality, latency, and causal improvements. It does not prevent tracing
the shipped read/write paths. No target code, tests, examples, model calls or
services were executed.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/agent-creativity/agentic-local-brain` | 41ea0cb104686eb0d39f32c94c2b84d37cdff0e7 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/agentic-local-brain-f00cbd577178/related-systems/agent-creativity--agentic-local-brain`. Implementation: tracked tree and packaging entry points; bounded reads/searches of CLI admission/indexing, collector file persistence, SQLite schema, Chroma persistence, RAG and enhanced retrieval, conversation storage, application wiring, chat/wiki/item/mining routes, browser endpoint callers, CLI/batch/per-document mining, wiki compilation, recommendation interface, scheduler/backup, build/install references, examples and selected test fixtures. Doctrine/design: full root README, project context files, collection skill intent/fallback/extraction rules and command references, prompt templates; Trellis workflow/settings/hooks inspected only to establish the deliberate development-workflow exclusion. Detailed coverage and uninspected material are listed above. | Implementation: [console entry points](https://github.com/agent-creativity/agentic-local-brain/blob/41ea0cb104686eb0d39f32c94c2b84d37cdff0e7/pyproject.toml), [collection driver](https://github.com/agent-creativity/agentic-local-brain/blob/41ea0cb104686eb0d39f32c94c2b84d37cdff0e7/kb/commands/collect.py), [enhanced retrieval](https://github.com/agent-creativity/agentic-local-brain/blob/41ea0cb104686eb0d39f32c94c2b84d37cdff0e7/kb/query/retrieval_pipeline.py), [wiki compiler](https://github.com/agent-creativity/agentic-local-brain/blob/41ea0cb104686eb0d39f32c94c2b84d37cdff0e7/kb/processors/wiki_compiler.py), [wiki consumer](https://github.com/agent-creativity/agentic-local-brain/blob/41ea0cb104686eb0d39f32c94c2b84d37cdff0e7/kb/web/routes/wiki.py). Doctrine/design: [README](https://github.com/agent-creativity/agentic-local-brain/blob/41ea0cb104686eb0d39f32c94c2b84d37cdff0e7/README.md), [collection instructions](https://github.com/agent-creativity/agentic-local-brain/blob/41ea0cb104686eb0d39f32c94c2b84d37cdff0e7/skills/localbrain-collect/SKILL.md), [RAG prompt templates](https://github.com/agent-creativity/agentic-local-brain/blob/41ea0cb104686eb0d39f32c94c2b84d37cdff0e7/kb/query/prompt_templates.py). | No access gap in the frozen application's material paths. No observed-run or causal-experiment evidence supplied; prevents empirical quality, durability and performance conclusions. External host/provider/library implementations, live content, installed releases and user stores are outside the acquired source; prevents attributing their guarantees or observed behavior to this target. Engineering scaffolding deliberately excluded; prevents conclusions about the Trellis development workflow. |
