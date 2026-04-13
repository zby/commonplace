---
description: "Executable local-first LLM Wiki pipeline with Python ingestion, LLM extraction/merge, BM25 search, monitors, UI, and a partial prompt-optimization loop"
type: agent-memory-system-review
traits: [has-comparison, has-implementation]
tags: [related-systems]
status: current
last-checked: "2026-04-13"
---

# kenhuangus/llm-wiki

Ken Huang's LLM Wiki is a local-first, agent-maintained knowledge compilation system for agentic AI, AI security, LLM, robotics, and secure-coding research. Unlike the promptware-oriented [nvk/llm-wiki](./llm-wiki.md) review, this repository is an executable Python and React implementation: source monitors fetch papers/advisories/feed items, pipeline scripts normalize and extract claims through an LLM, integration scripts merge claims into an Obsidian-compatible markdown wiki, BM25 query searches the generated wiki, and a FastAPI/React UI provides search, article editing, logs, backlinks, and git history. The most interesting design point is not the retrieval layer, which is intentionally simple, but the shift from stateless RAG to a compounding markdown graph with operation logs and conflict/frontmatter governance.

**Repository:** https://github.com/kenhuangus/llm-wiki

**Reviewed commit:** https://github.com/kenhuangus/llm-wiki/commit/d2bd485921f6c7b6071afbb389f44ab8e4e83c69

## Core Ideas

**The implemented center is a source-to-wiki pipeline.** The README describes `source -> ingest -> normalize -> extract (LLM) -> integrate (LLM merge) -> wiki`, and the repo backs that with separate scripts for each stage: `tools/ingest.py` copies or downloads sources into `raw/auto_ingest`, `tools/normalize.py` converts text or PDFs into frontmatter-wrapped normalized markdown, `tools/extract.py` calls the active extraction prompt and expects JSON entities/claims/relationships, and `tools/integrate.py` writes or merges those claims into `wiki/{category}/{subcategory}/{slug}.md` with confidence/status frontmatter ([README.md](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/README.md), [tools/ingest.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/ingest.py), [tools/normalize.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/normalize.py), [tools/extract.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/extract.py), [tools/integrate.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/integrate.py)).

**Markdown is the primary knowledge substrate; SQLite is operational state.** Durable knowledge lives in `wiki/` as Obsidian-style markdown with frontmatter, wikilinks, generated index entries, and an append-only `wiki/log.md`. The code uses SQLite only for monitor deduplication (`state.db`) and quality/experiment metrics (`metrics.db`), not as the primary memory store ([tools/common.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/common.py), [tools/metrics_collector.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/metrics_collector.py), [wiki/index.md](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/wiki/index.md)).

**Retrieval is plain BM25 over the compiled wiki.** `tools/query.py` recursively loads `wiki/**/*.md`, excludes `index.md` and `log.md`, tokenizes by lowercased whitespace splitting, runs `rank_bm25.BM25Okapi`, and returns the top five nonzero matches. There is no embedding store, reranker, query planner, or cached index here. The "semantic ranking" language in the docs is therefore best read as "BM25 over synthesized pages," not semantic retrieval in the vector sense ([tools/query.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/query.py)).

**Continuous ingestion is real, but the autonomous integration path is rough.** The repo includes source-specific monitors for arXiv, CVE/NVD, GitHub, RSS, and curated sources, plus `WikiDaemon` and `UnifiedDaemon` orchestrators. The monitors do useful deterministic work: SQLite deduplication, keyword filters, citation filters, PDF extraction for arXiv, full-body scraping for short RSS summaries, and priority handling for CVEs. The daemon loop then normalizes, extracts, integrates, lints, and indexes queued files. But the daemon integration path still calls `integrate.py` with a hard-coded `concepts agentic-ai test-integration` target, so the fully autonomous path is less mature than the manual CLI pipeline ([tools/arxiv_monitor.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/arxiv_monitor.py), [tools/rss_monitor.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/rss_monitor.py), [tools/github_monitor.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/github_monitor.py), [tools/curated_monitor.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/curated_monitor.py), [tools/daemon.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/daemon.py), [tools/unified_daemon.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/unified_daemon.py)).

**Governance is split between agent rules, frontmatter, lint, and LLM prompts.** `AGENTS.md` defines invariants: raw sources are immutable, conflicting claims must not be deleted, Tier 3 sources must not be promoted to verified, every claim needs attribution, and every write should be logged. The extraction and integration prompts encode confidence rubrics, conflict handling, source citations, and "Historical Claims" behavior. `tools/lint.py` checks required frontmatter fields and can run an LLM deep-lint that tags pages with `[CONFLICT]` and `status: conflict` ([AGENTS.md](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/AGENTS.md), [tools/prompts.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/prompts.py), [tools/lint.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/lint.py)).

**The UI turns the wiki into a local Wikipedia-like surface.** `api_server.py` exposes search, ingest, article listing, article read/write, upload, logs, backlinks, git history, and stats endpoints, while `ui/src/App.jsx` renders a Wikipedia-style React app over those endpoints. This gives the markdown wiki a human browsing/editing surface, not just an agent CLI. It also creates a governance bypass: `/api/article/{path}` writes markdown directly and does not log the edit through `write_log`, while `/api/stats` reports a hard-coded average confidence of `0.92` ([api_server.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/api_server.py), [ui/src/App.jsx](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/ui/src/App.jsx), [ui/package.json](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/ui/package.json)).

## Comparison with Our System

| Dimension | kenhuangus/llm-wiki | Commonplace |
|---|---|---|
| Primary substrate | Markdown wiki under `wiki/`, with `raw/` staging and generated index | Typed repo KB under `kb/notes/`, `kb/reference/`, `kb/instructions/`, and workshop areas |
| Intake model | Continuous source monitors plus manual ingest pipeline | Explicit source snapshots, ingest reports, and review workflows |
| Knowledge transformation | LLM extraction to JSON, then LLM merge into wiki pages | Human/agent-authored notes with type-specific writing rules and semantic QA |
| Retrieval | BM25 scan over compiled wiki pages | `rg`, frontmatter descriptions, curated indexes, semantic links, and note types |
| Governance | AGENTS rules, frontmatter confidence/status, LLM prompts, lint scripts | Deterministic validation, semantic review bundles, type contracts, and stronger link/status conventions |
| Operational DB | SQLite for dedupe and metrics only | Mostly file-native; review system has generated metadata but KB content remains files |
| Interface | CLI scripts + FastAPI + React UI | CLI commands + skills/instructions; no dedicated wiki UI |
| Automation stance | Pushes toward daemon-driven ingestion, research, validation, prompt optimization, and paper generation | Pushes toward explicit workflows and review gates before promotion |

The closest shared bet is that a compiled markdown corpus can become the primary reasoning surface. LLM Wiki is more automation-heavy: it wants feeds, monitors, LLM extraction, merge prompts, and a daemon to keep the wiki moving. Commonplace is more type-and-review-heavy: it wants narrower artifacts, explicit note roles, stronger link semantics, and validation before accumulating claims. LLM Wiki therefore sits closer to an operational ingestion lab; commonplace sits closer to a curated methodology library with workshop workflows around it.

The UI/API layer is the biggest difference. Commonplace has good agent-facing instructions and scripts but no equivalent local reading/editing surface. LLM Wiki has a concrete browser interface, article history views, and upload/search flows. The tradeoff is that direct UI writes can bypass the same logging/governance path the agent rules require.

## Borrowable Ideas

**Small operational SQLite beside a file-first KB.** The state database for monitor deduplication is a narrow, useful exception to pure files. It does not move knowledge into a database; it just prevents repeated ingestion work. Ready to borrow if commonplace grows high-volume source polling.

**Generated coverage dashboard from wiki frontmatter.** `tools/index.py` turns page metadata into domain counts, average confidence, and pending-review lists. Commonplace's indexes are stronger semantically, but the simple "coverage and pending review" slice is useful for collection-level maintenance. Ready to borrow as an index adjunct, not a replacement for curated orientation.

**Local UI for browsing and editing KB artifacts.** The FastAPI/React surface is an existence proof that a markdown KB can have a lightweight Wikipedia-like editor without abandoning files. Worth borrowing only after deciding which writes must be gated or logged, because the current implementation shows exactly how a UI can bypass governance.

**Source-monitor prefilters.** The arXiv and RSS monitors combine dedupe, keyword filters, optional citation filters, PDF extraction, and full-article scraping in small scripts. Useful for source discovery workshops; not ready for core library ingestion without stronger classification and review.

**Negative experiment logging.** `wiki/experiments.md` records failed prompt-optimization runs and weird generated queries, which is more valuable than a clean success-only story. Commonplace review bundles already preserve findings, but experiment logs for failed automation attempts would be useful when we start evaluating outer loops ([wiki/experiments.md](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/wiki/experiments.md)).

**Do not borrow the prompt optimizer yet.** It is conceptually interesting: generate a prompt-change hypothesis from recent extraction failures, evaluate on a fixed set, keep only improvements. But the current implementation generates a new prompt string without writing it into `tools/prompts.py`, then tries to commit and evaluate anyway. The pattern needs a tighter oracle and actual artifact mutation before adoption ([tools/prompt_optimizer.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/prompt_optimizer.py)).

## Curiosity Pass

**The repo is more concrete than a PRD, but some docs outrun the code.** The architecture docs frame a complete autonomous research system with paper generation, validation, prompt optimization, and multi-source monitoring. The code contains those components, but several surfaces are still thin: daemon integration uses a hard-coded target page, prompt optimization does not apply the generated prompt, and API stats include a hard-coded average confidence. This is not just "unfinished"; it marks the difference between having module names for autonomy and having a closed-loop system.

**"Semantic BM25" is a useful artifact-level distinction but a retrieval overclaim.** Searching synthesized wiki pages is meaningfully different from searching raw snippets, because the pages are already LLM-compiled. But `query.py` itself is basic BM25 over lowercased whitespace tokens. The semantic work happens upstream in extraction/integration, not in the query engine.

**The confidence model mostly lives in prompts and metadata.** Confidence scores are generated by model prompts, checked by lint heuristics, and aggregated in the generated index. There is no independent calibration oracle. This is still useful as a triage surface, but the number is not yet strong evidence unless source tier, corroboration, and contradiction checks become more deterministic.

**The system almost qualifies as trace-derived learning, then misses on promotion.** The prompt optimizer consumes run metrics, extraction failures, and an evaluation set; that is close to an operational trace-to-prompt loop. But because the generated prompt is not actually written into the active prompt registry before commit/evaluation, the current repo does not implement a durable trace-derived learning mechanism. It should not be listed in the trace-derived survey until the mutation and evaluation loop is real.

**The UI is both the most borrowable and the riskiest layer.** Browser access makes the wiki feel real to a human operator, and git history views are a good match for markdown knowledge. But direct saves without operation-log writes or validation can undercut the same invariants the agent schema insists on. The lesson for commonplace is that UI writes need the same contract as agent writes, not a side door.

## What to Watch

- Whether the prompt optimizer starts editing and evaluating actual prompt artifacts rather than logging proposed strings.
- Whether daemon integration replaces the hard-coded `test-integration` target with title/domain routing derived from extracted metadata.
- Whether UI writes gain validation, operation logging, and maybe git staging/commit hooks.
- Whether `query.py` stays a scan-time BM25 helper or grows a cached index, snippets, reranking, or source-aware result explanations.
- Whether a Python dependency manifest appears; at this commit the README lists manual `pip install` dependencies, while only the React UI has `package.json`.
- Whether the project keeps its markdown wiki as the source of truth, or lets metrics/state/API layers drift into parallel truth surfaces.

---

Relevant Notes:

- [Files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) - aligns: LLM Wiki keeps durable knowledge in markdown while using SQLite only for dedupe and metrics
- [Agents navigate by deciding what to read next](../../notes/agents-navigate-by-deciding-what-to-read-next.md) - extends: the generated index and BM25 search are navigation aids over the compiled wiki
- [Stale indexes are worse than no indexes](../../notes/stale-indexes-are-worse-than-no-indexes.md) - warns: LLM Wiki's generated catalog is useful only if daemon/UI writes keep it fresh
- [Quality signals for KB evaluation](../../notes/quality-signals-for-kb-evaluation.md) - relates: confidence, conflict status, and experiment logs are quality signals, but not yet independent oracles
- [Evaluation automation is phase-gated by comprehension](../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) - warns: the prompt optimizer needs a real artifact mutation path and trustworthy eval signal before it can be treated as a learning loop
- [LLM Wiki](./llm-wiki.md) - contrasts: same repository name, but the `nvk` version packages a prompt/protocol system while `kenhuangus` ships an executable ingestion/wiki/UI stack
- [Atomic](./atomic.md) - compares: both compile sources into wiki artifacts, but Atomic's database-backed atom/wiki model differs from LLM Wiki's markdown-first pipeline
- [Siftly](./siftly.md) - compares: both emphasize staged ingestion and deterministic progress markers, but Siftly's SQLite pipeline is stronger on resumability
