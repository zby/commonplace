---
description: "LLM-WIKI-MCP review: local Markdown wiki with SQLite FTS, MCP/CLI retrieval, Ollama ask, provenance ingest, sidecar notes, and ask-history memory"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-18"
---

# LLM-WIKI-MCP

LLM-WIKI-MCP, from `Electro-resonance/LLM-WIKI-MCP`, is a local-first Python package for turning source folders into a Markdown wiki under `wiki_vault/`, indexing it with SQLite FTS, and exposing search, context packing, Ollama-backed ask, maintenance, and MCP tools. At the reviewed commit, the implemented system is a CLI plus in-process Python API plus stdio MCP server; the durable knowledge is mostly vault files, while SQLite, caches, context packs, and graph/export views are rebuildable access structures.

**Repository:** https://github.com/Electro-resonance/LLM-WIKI-MCP

**Reviewed commit:** [25efb7631082fa3732723fee08e24d39b43311fa](https://github.com/Electro-resonance/LLM-WIKI-MCP/commit/25efb7631082fa3732723fee08e24d39b43311fa)

**Last checked:** 2026-06-18

## Core Ideas

**Markdown is the source of truth, SQLite is the rebuildable access layer.** The docs describe the main flow as local source files -> Markdown wiki pages -> SQLite search index -> retrieved context -> local Ollama answer, and the code makes `wiki_vault/wiki/` the page store while `index.sqlite3` holds the `pages` table and `pages_fts` virtual table ([docs/01_OVERVIEW_AND_ARCHITECTURE.md](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/docs/01_OVERVIEW_AND_ARCHITECTURE.md), [src/llm_wiki_mcp/server.py](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/src/llm_wiki_mcp/server.py)). `reindex()` deletes and rebuilds the index from Markdown pages, so the database is not the canonical memory.

**Ingest is provenance-aware acquisition, not semantic distillation.** The release ingest path scans supported Markdown/text/RTF/PDF/DOCX files, skips the active `wiki_vault/`, records mtime/SHA provenance, writes generated `Source - ...` wiki pages, and reindexes after processing ([src/llm_wiki_mcp/context_api.py](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/src/llm_wiki_mcp/context_api.py), [tests/provenance_ingest_search_test.py](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/tests/provenance_ingest_search_test.py), [tests/reindex_docx_vault_skip_test.py](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/tests/reindex_docx_vault_skip_test.py)). The generated page includes extracted text and source file metadata; it does not try to infer stable concepts or claims from the source.

**Context efficiency is handled by search, budgets, and debug visibility.** The basic retrieval path uses SQLite FTS with prefix and singular/plural expansion, then falls back to deterministic token/title scoring; higher-level ask paths apply `context_budget_tokens`, `history_budget_tokens`, per-source budgets, `max_sources`, and `/debug-context` so a user can inspect the assembled prompt before calling Ollama ([src/llm_wiki_mcp/server.py](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/src/llm_wiki_mcp/server.py), [src/llm_wiki_mcp/context_api.py](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/src/llm_wiki_mcp/context_api.py), [tests/context_budget_debug_test.py](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/tests/context_budget_debug_test.py)). Long-book search windows and centered snippets are explicitly implemented to avoid handing the model only the beginning of a large page.

**There are three consumption surfaces over the same vault.** `llm-wiki` exposes human-facing shell commands, `LLMWikiContextEngine` exposes in-process retrieval/context methods, and `llm-wiki-mcp` exposes MCP tools for clients that want structured search, read, ask, lint, graph, config, and history operations ([README.md](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/README.md), [CLI_TOOLS_LIST.md](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/CLI_TOOLS_LIST.md), [MCP_FUNCTIONS_LIST.md](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/MCP_FUNCTIONS_LIST.md), [src/llm_wiki_mcp/context_api.py](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/src/llm_wiki_mcp/context_api.py), [src/llm_wiki_mcp/server.py](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/src/llm_wiki_mcp/server.py)).

**Ask history is a real trace-derived memory loop, but not autonomous rule learning.** Completed ask turns record question, full prompt/context, answer, source/tool names, token estimates, metrics, and sometimes runtime events in local vault files; future ask prompts include recent/compressed history when relevant ([docs/04_AGENTIC_ASK_AND_MEMORY.md](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/docs/04_AGENTIC_ASK_AND_MEMORY.md), [src/llm_wiki_mcp/context_api.py](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/src/llm_wiki_mcp/context_api.py), [tests/ask_history_context_test.py](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/tests/ask_history_context_test.py)). The loop preserves and compresses interaction traces; it does not promote repeated lessons into enforced instructions or validators.

**Maintenance is mostly structural and local.** Lint checks broken links, orphan pages, and short pages; repair can rewrite resolved links, link orphans from the index, scaffold short pages, create missing stubs when requested, and reindex after applied changes ([src/llm_wiki_mcp/server.py](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/src/llm_wiki_mcp/server.py)). AI sidecar notes add generated summaries, extracted terms, and candidate links beside canonical pages, but the notes themselves are explicitly not the canonical source document ([src/llm_wiki_mcp/context_api.py](https://github.com/Electro-resonance/LLM-WIKI-MCP/blob/25efb7631082fa3732723fee08e24d39b43311fa/src/llm_wiki_mcp/context_api.py)).

## Artifact analysis

- **Storage substrate:** `files` `sqlite` `repo` - Durable user/project memory lives in vault files: `wiki/*.md`, `raw/`, `notes/*.md`, `ask_history.jsonl`, `ask_history_compressed.md`, `ask_metrics.jsonl`, runtime journal/config files, and exports. SQLite stores the rebuildable FTS/index tables, while the repository stores the authored package, docs, tests, CLI/MCP tool definitions, and sample config.
- **Representational form:** `prose` `symbolic` - Wiki pages, source captures, sidecar notes, compressed history, prompts, and docs are prose; frontmatter, JSON/JSONL records, config keys, SQLite rows/FTS terms, tool schemas, scores, graph edges, provenance hashes, and lint actions are symbolic. I found no retained embeddings, adapters, or model weights.
- **Lineage:** `authored` `imported` `trace-extracted` - The package code, docs, seed pages, schemas, tool catalogues, and user-created wiki notes are authored; source documents are imported into generated wiki pages; ask history, tool traces, runtime journal events, metrics, and compressed ask memory are extracted from interaction traces.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` `enforcement` - Wiki pages, raw imports, sidecar notes, exports, and ask history provide knowledge/context; the agent system prompt and command/tool docs instruct behavior; tool planners, config, source titles, links, and page handles route retrieval; lint, health, dry-run write, provenance checks, and doc reconciliation validate; FTS/fallback scores, candidate links, and planner heuristics rank; ask-history recording/compression and sidecar notes learn from use; overwrite checks, tombstone deletion, dry-run defaults, and active-vault ingest exclusion enforce operational boundaries.

**Wiki pages and source pages.** `WikiStore.create_page()`, `update_page()`, `ingest_file()`, and `release_markdown_to_wiki_page()` write Markdown files that are both human-readable memory and machine-readable retrieval units. Source pages keep extracted content plus file/source metadata, so their default authority is evidence/reference rather than instruction.

**SQLite index and caches.** `pages`, `pages_fts`, and the small TTL caches serve retrieval speed and scoring. They shape read-back strongly, but because they are rebuilt from Markdown and query parameters, they are access structures rather than the retained source of truth.

**MCP/CLI/Python tool definitions.** The tool catalogues, command tables, function wrappers, and `LLMWikiContextEngine` methods are system-definition artifacts. They decide which operations are read-only, which mutate the vault, how context is budgeted, and which evidence is available to a host agent.

**Ask-history and metrics files.** `ask_history.jsonl`, `ask_history_compressed.md`, `ask_metrics.jsonl`, and runtime journal records are trace-derived memory. They are consumed by self-access, recursive-context, history, and agentic-ask paths, but their compression is a deterministic summary/truncation pass rather than a semantic promotion into durable rules.

**AI sidecar notes.** `release_build_page_note()` creates `notes/*.md` with a working summary, key terms, candidate links, and suggested next actions. These notes are derived views over existing pages and old notes; they improve search and review affordances while preserving the canonical page as the maintained source.

**Promotion path.** The strongest implemented path is source file -> generated wiki page -> SQLite/notes/search surfaces -> ask context -> recorded ask history -> compressed ask memory. There is also a possible page -> sidecar note -> candidate link -> manual promotion path, but I did not find an implemented gate that automatically promotes a sidecar suggestion into a canonical wiki link or higher-authority rule.

## Comparison with Our System

LLM-WIKI-MCP and Commonplace share a file-first stance: Markdown remains inspectable, and generated indexes or derived views are not the authoritative artifact. The main difference is scope and authority. Commonplace uses collection contracts, type specs, deterministic validation, review gates, and curated indexes to make a repository into an agent-operated knowledge base. LLM-WIKI-MCP is a more general local memory tool: it ingests user documents, indexes them, retrieves bounded context, asks a local model, and records runtime history.

LLM-WIKI-MCP's ask pipeline is more integrated than Commonplace's ordinary pull workflow. A user can ask a natural-language question and the system will plan read-only tools, search sidecar-enhanced pages, expand matching pages, include recent ask history, build a token-budgeted prompt, call Ollama, and record the result. Commonplace usually keeps those steps as visible agent operations over the KB, which is less seamless but easier to audit.

The tradeoff is semantic governance. LLM-WIKI-MCP has useful structural guards and tests around search, ingest, context budgets, and history, but its generated pages and sidecar notes do not carry Commonplace-like type contracts, link semantics, or review status. It is good at making a local pile of documents usable quickly; it is weaker at saying when a retained claim is ready to steer future work.

### Borrowable Ideas

**Debuggable prompt pack.** Ready now. Commonplace review and retrieval commands could expose a `/debug-context`-style artifact that shows exactly which notes, history, and budget settings are about to enter a model call.

**Ask-history as explicit local runtime memory.** Needs a concrete use case. Commonplace could keep a local, ignored runtime history for operator continuity, but should separate it from durable library artifacts and add retention/redaction rules before broad use.

**Sidecar notes as non-canonical retrieval aids.** Ready with constraints. A `notes/`-like sidecar layer could hold generated keywords, candidate links, and summaries without mutating canonical artifacts, provided validation prevents sidecar claims from masquerading as reviewed knowledge.

**Active-vault ingest exclusion.** Ready now. The guard that prevents `/ingest .` from recursively absorbing the generated vault is a small but important safety pattern for any self-hosted KB importer.

**Local Ollama answer fallback.** Useful but not central. Commonplace could borrow the "answer from gathered evidence even when synthesis fails" UX for reports, while keeping evidence and final answer distinct.

## Write side

**Write agency:** `manual` `automatic` - Humans and host agents create, update, rename, delete, configure, ingest, repair, and edit wiki pages through CLI/MCP/API calls; automatic paths create seed pages, import source documents, update generated source pages from changed files, rebuild indexes, write sidecar notes, record ask turns/metrics/runtime events, compress over-budget ask history, scaffold repairs when `apply` is requested, and export derived context files.

**Curation operations:** `consolidate` `evolve` - History compression condenses older exact ask turns into a Markdown rolling memory, sidecar note iteration summarizes existing pages and candidate links, and repair can evolve existing pages by fixing links, adding orphan links to the index, or adding retrieval scaffolds. Source ingest is acquisition, and SQLite reindex/export generation is access-structure upkeep, so neither counts as curation over already-stored memory.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` - The implemented trace inputs are ask prompt/response records, selected tools/sources, token estimates, LLM metrics, and runtime execution events stored in local vault files.

**Learning scope:** `per-project` `cross-task` - Memory is scoped to a vault, usually a local project wiki, and then reused across later questions and tasks in that vault.

**Learning timing:** `online` `staged` - Ask turns and metrics are recorded immediately after the ask path runs; compression and recursive-context assembly happen as a staged maintenance/read step when history exceeds budget or future prompts are built.

**Distilled form:** `prose` `symbolic` - Exact JSONL turns and metrics are symbolic/prose records; compressed ask memory, recent-history markdown, and agentic prompt packs are prose plus symbolic source/tool metadata.

**Extraction.** The extraction oracle is mostly the runtime path itself: the user question, built prompt, final answer, tools called, sources, and token estimates are saved without an external judge. Compression summarizes older rows by question, answer preview, and sources. That makes the loop useful for continuity and self-inspection, but weak for truth maintenance: the system remembers what happened, not whether the answer was correct.

**Scope and timing.** Recent/compressed history is read into later ask prompts through `release_recent_history_markdown()`, `release_recursive_context_with_memory()`, and the final `release_agentic_ask()` path. The system also records runtime events and metrics for self-access, but those are diagnostics rather than learned behavioral rules.

**Survey placement.** LLM-WIKI-MCP belongs in the trace-to-local-memory family: runtime interaction traces become durable local prose/symbolic artifacts and later prompt context. It strengthens the survey claim that trace-derived learning often starts as retained transcripts and summaries before it becomes enforceable policy; this implementation stops at continuity memory and diagnostics rather than promotion into stronger system-definition artifacts.

## Read-back

**Read-back:** `both` - Wiki memory can be pulled explicitly through search, read, retrieve, context, MCP, Python API, and export calls; it is also pushed into the final ask model call when `/ask` or `release_ask()` automatically searches, reads pages, includes recent history, and builds the prompt for Ollama.

**Read-back signal:** `coarse` `inferred / lexical` - Recent ask history and operational self-context are coarse prompt additions in the ask path; page selection is inferred primarily from lexical search, title/term matching, sidecar-note search, and rule-based planner heuristics.

**Faithfulness tested:** `no` - The tests check that search finds expected pages, context budgets include matching sources, and ask history is recorded and available, but I did not find a with/without memory ablation or post-answer audit proving that injected memory changed model behavior faithfully.

**Direction edge cases.** Static CLI/MCP docs and the agent system prompt are shipped baseline instructions, not accumulated memory read-back. Ask history and wiki pages do count: they are retained local artifacts created or changed during use and can be included in future ask prompts. MCP clients that call `wiki_search` or `wiki_read_page` are using pull; the bundled ask workflow turns the same mechanisms into push for the Ollama answer model.

**Selection, scope, and complexity.** Basic search uses FTS/fallback scoring over Markdown pages and returns snippets. The later agentic path can search with sidecar notes, choose a focus page, expand multiple pages, include recent history, and trim the final prompt to configured budgets. This controls volume reasonably, but the selected material can still be complex: full imported pages, sidecar notes, tool outputs, runtime capabilities, and history may all share the prompt.

**Authority at consumption.** Retrieved wiki pages and sidecar notes are advisory context. The agent system prompt instructs the answer model to prefer evidence, cite page/tool names, and avoid mutation during ask. Lint/repair outputs can guide maintenance, but they do not hard-gate the answer path.

**Other consumers.** Humans use the CLI shell, generated Markdown vault, Mermaid graphs, `llms.txt` exports, history commands, and config/status reports. MCP clients and Python applications consume the same vault through structured tools and `LLMWikiContextEngine`.

## Curiosity Pass

**The release file has an accretive shape.** `context_api.py` contains repeated definitions with later overrides; the final behavior is discoverable, but a reviewer has to read the tail of the file to know which helper is live. That is a maintenance risk for an agent-facing API.

**The strongest memory loop is conversation continuity, not wiki learning.** The trace-derived path stores and compresses ask turns, while source ingest mostly copies/extracts document content into pages. Durable semantic learning still depends on human or agent edits to the wiki.

**Sidecar notes are a good authority compromise.** They let the system add generated retrieval help without silently editing canonical pages. The cost is that search can start privileging generated terms whose quality is not independently reviewed.

**The MCP surface is broad enough to blur read/write safety.** The catalogue labels safety groups, and the recommended usage pattern says prefer read-only inspection, but the same server exposes create/update/rename/delete/repair/config tools. Host clients need their own permission discipline.

**Local-first privacy is only as strong as retention policy.** The code redacts local paths from public-facing answers and keeps history local, but ask prompts and answers can be stored exactly. That is useful memory and also sensitive runtime data.

## What to Watch

- Whether `context_api.py` is consolidated so final overrides, planner behavior, and trace-memory paths become easier for agents to audit.
- Whether sidecar notes gain an explicit accept/promote workflow with provenance back to the canonical page before candidate links or summaries affect durable wiki structure.
- Whether source ingest gains quote/span provenance rather than just file-level source metadata; that would make generated source pages easier to verify.
- Whether ask-history compression remains deterministic truncation or gains a reviewed summary/judgment step; this decides whether the trace loop becomes real learning or stays continuity memory.
- Whether host MCP clients enforce read/write permission boundaries around the broad tool surface, especially delete, repair apply, config, and ingest tools.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: LLM-WIKI-MCP stores wiki pages and ask history, but they affect future action only when pulled by tools or pushed into the ask prompt.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: wiki pages, SQLite indexes, sidecar notes, tool definitions, and ask-history files differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: imported source pages, wiki pages, sidecar notes, exports, and history mostly serve as evidence/reference/context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: CLI/MCP tool definitions, agent prompts, config, lint/repair rules, and provenance guards shape later behavior.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - explains: LLM-WIKI-MCP's targeted retrieval depends on page titles, terms, source names, links, and tool-selected focus pages being available as symbols.
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: LLM-WIKI-MCP derives local continuity memory and diagnostics from ask/session traces, but does not promote those traces into enforced rules.
