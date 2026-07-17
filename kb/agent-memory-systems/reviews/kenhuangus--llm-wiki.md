---
description: "LLM Wiki review: local-first Obsidian/wiki compiler with source monitors, LLM extraction and integration, BM25 search, autonomous maintenance loops, and weak trace-learning prompt-optimization scaffolding"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-06-04"
---

# LLM Wiki (kenhuangus)

LLM Wiki, from `kenhuangus/llm-wiki`, is a local-first knowledge compiler for AI/security material. At the reviewed commit it stores raw and normalized sources, generated wiki pages, operation logs, state databases, metrics databases, experiment logs, newsletters, and generated papers; it fetches arXiv, CVE, GitHub, RSS, and curated sources; uses an LLM to extract JSON claims and merge them into Markdown pages; exposes BM25 search and a FastAPI/React wiki UI; and includes an autonomous daemon layer for processing, validation, prompt-optimization experiments, research hypotheses, and paper generation.

**Repository:** https://github.com/kenhuangus/llm-wiki

**Reviewed commit:** [d2bd485921f6c7b6071afbb389f44ab8e4e83c69](https://github.com/kenhuangus/llm-wiki/commit/d2bd485921f6c7b6071afbb389f44ab8e4e83c69)

**Last checked:** 2026-06-04

## Core Ideas

**The main memory is a compiled Markdown wiki, not query-time RAG over raw documents.** The README describes a source -> ingest -> normalize -> extract -> integrate -> wiki pipeline, with raw sources under `raw/auto_ingest`, normalized Markdown under `raw/normalized`, and durable pages under `wiki/` ([README.md](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/README.md)). The code implements the same shape: `ingest.py` copies or downloads source files, `normalize.py` writes frontmatter-wrapped normalized Markdown, `extract.py` calls the configured chat model and writes JSON, and `integrate.py` creates or merges a wiki page with frontmatter, claims, confidence, source count, and conflict status ([tools/ingest.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/ingest.py), [tools/normalize.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/normalize.py), [tools/extract.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/extract.py), [tools/integrate.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/integrate.py)).

**AGENTS.md is a human-authored behavioral schema for wiki-writing agents.** It defines page templates, update rules, Obsidian links, source attribution, confidence scoring, trust tiers, model routing, escalation triggers, prohibited actions, and logging requirements ([AGENTS.md](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/AGENTS.md)). This is a system-definition artifact parallel to Commonplace collection contracts, but it is prose policy rather than a validated type surface.

**Automation is broad, but the compiler core is simple.** Monitors poll arXiv, NVD/CVE, GitHub releases/advisories/Dependabot, and RSS feeds; they deduplicate with `state.db`, write Markdown source snapshots, and sometimes trigger immediate processing or critical alerts ([tools/arxiv_monitor.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/arxiv_monitor.py), [tools/cve_monitor.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/cve_monitor.py), [tools/github_monitor.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/github_monitor.py), [tools/rss_monitor.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/rss_monitor.py)). The integration path itself is one target page at a time: merge old page body plus new claim bullets through an LLM prompt, set `status: conflict` when the LLM emits `STATUS: CONFLICT`, then write the page.

**Search is lexical BM25 over wiki pages.** `query.py` loads Markdown pages, lowercases and whitespace-tokenizes page content, ranks with `rank_bm25`, and returns top nonzero results; the FastAPI `/api/search` endpoint wraps those results with snippets for the React UI ([tools/query.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/query.py), [api_server.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/api_server.py), [ui/src/App.jsx](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/ui/src/App.jsx)). Despite README language calling this "semantic ranking", the inspected implementation is lexical BM25, not embedding retrieval.

**The autonomous layer adds scheduling, metrics, and synthesis surfaces.** `WikiDaemon` polls monitors, queues sources by priority, runs normalization/extraction/integration, lint, and index rebuilds; `UnifiedDaemon` adds prompt optimization every four hours, research hypothesis generation every six hours, retrospective validation every seven days, and paper generation every fourteen days ([tools/daemon.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/daemon.py), [tools/unified_daemon.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/unified_daemon.py)). Metrics and hypotheses persist in SQLite tables, while experiment and newsletter outputs are Markdown files ([tools/metrics_collector.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/metrics_collector.py), [tools/research_agent.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/research_agent.py), [tools/newsletter_agent.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/newsletter_agent.py), [tools/paper_agent.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/paper_agent.py)).

**Some documented autonomy is ahead of the code.** The architecture docs describe a prompt-ratchet loop that modifies `prompts.py`, commits improvements, and resets failed attempts ([AUTONOMOUS_LOOP_DIAGRAM.md](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/AUTONOMOUS_LOOP_DIAGRAM.md)). The implementation generates `new_prompt`, but `commit_prompt_change()` explicitly says the full implementation would modify `prompts.py` and currently only runs `git add` and `git commit` against the existing file; `git_revert()` uses `git reset HEAD~1` rather than a safe revert commit ([tools/prompt_optimizer.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/prompt_optimizer.py)). So the trace-learning prompt path is scaffolded and logged, but the code does not actually persist the generated prompt text.

## Artifact analysis

- **Storage substrate:** `repo` `files` `sqlite` — The wiki, raw sources, normalized sources, generated papers, newsletters, AGENTS policy, prompts, logs, UI, and code are repository files; `state.db` deduplicates ingested IDs, `metrics.db` stores extraction/integration/experiment/hypothesis/daily-summary state, and the API exposes git history for wiki files ([tools/common.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/common.py), [tools/metrics_collector.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/metrics_collector.py), [api_server.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/api_server.py)).
- **Representational form:** `prose` `symbolic` — Wiki pages, raw/normalized source Markdown, prompts, AGENTS policy, newsletters, papers, logs, and conflict notes are prose; frontmatter, JSON extraction outputs, SQLite schemas, monitor state, priority constants, prompt registries, route schemas, git commit hashes, status fields, and command schedules are symbolic. The repo uses LLMs and BM25 ranking, but I did not find a retained embedding or model-weight store in this checkout.
- **Lineage:** `authored` `imported` `trace-extracted` — AGENTS policy, prompts, code, research agenda, UI, and docs are authored; arXiv, CVE, GitHub, RSS, uploaded files, and curated source captures are imported; operation logs, extraction/integration metrics, prompt experiments, research hypotheses, validation reports, newsletters, and generated papers are derived from pipeline events, wiki state, and prior generated artifacts.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Wiki pages and sources serve as knowledge; AGENTS.md, prompts, and research agenda instruct; CVSS priorities, critical alerts, conflict status, prohibited actions, lint rules, and daemon schedules enforce or constrain work; domains, categories, source types, state DB keys, queue priorities, and API paths route; lint, retrospective validation, test scripts, and confidence propagation validate; BM25 ranks search; metrics and optimizer/research-agent loops implement learning-like feedback.

**Wiki pages.** Pages are Markdown files under `wiki/` with YAML frontmatter containing `id`, `title`, `domain`, `source_count`, `confidence`, `verified`, `last_updated`, and `status`; `index.py` rebuilds a global catalog and pending-review list from those fields ([README.md](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/README.md), [tools/index.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/index.py)). They are knowledge artifacts for readers and later LLM synthesis, while their frontmatter controls search, validation, UI stats, and maintenance.

**Source and extraction artifacts.** Raw source Markdown is imported evidence; normalized Markdown adds frontmatter and hashes; extracted JSON contains entities, claims, relationships, source IDs, confidence, and evidence fields generated by the LLM extraction prompt ([tools/normalize.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/normalize.py), [tools/extract.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/extract.py), [tools/prompts.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/prompts.py)). The extraction JSON is an intermediate symbolic/prose derivative, not the final read surface.

**State and metrics databases.** `state.db` prevents repeated ingestion of the same source IDs across monitor runs; `metrics.db` tracks extraction quality, integration conflicts, prompt experiments, research hypotheses, and daily summaries ([tools/common.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/common.py), [tools/metrics_collector.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/metrics_collector.py)). These are not user-facing knowledge pages, but they route and score future maintenance loops.

**System-definition files.** `AGENTS.md` defines agent rules; `tools/prompts.py` defines extraction and integration prompts plus the active prompt registry; `.env.example` and common configuration define LLM endpoints, source limits, monitored repos, and feed filters ([AGENTS.md](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/AGENTS.md), [tools/prompts.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/prompts.py), [.env.example](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/.env.example)). These carry instruction and routing authority, but the repo does not validate them against a schema.

**Synthesis outputs.** Newsletter and paper agents read recent or topic-matched wiki pages, ask an LLM to synthesize a report or paper, and save Markdown outputs with frontmatter ([tools/newsletter_agent.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/newsletter_agent.py), [tools/paper_agent.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/paper_agent.py)). This is an automatic promotion from compiled wiki memory into a higher-level prose artifact, but source-span provenance is coarse.

Promotion path: imported source -> raw file -> normalized Markdown -> LLM extraction JSON -> wiki page merge -> index/search/API read surface. Additional paths promote wiki updates into newsletters and papers, and operation traces into prompt/research experiments. The strongest implemented promotion path is source-to-wiki; the prompt-ratchet promotion path is not complete because generated prompt text is not actually written to `prompts.py`.

## Comparison with Our System

LLM Wiki and Commonplace both use Markdown files, git, frontmatter, indexes, and agent-readable rules to make knowledge durable. LLM Wiki is more autonomous on acquisition: monitors fetch external feeds, process them on a schedule, and can produce newsletters or papers without a manual note-writing step. Commonplace is stronger on artifact contracts: collection-local type specs, deterministic validation, review gates, and explicit linking rules make the authority of each retained artifact clearer.

The main tradeoff is compilation authority. LLM Wiki trusts an LLM extraction and merge prompt to turn new source material directly into current wiki pages, with conflict status as the main guardrail. Commonplace keeps generated source snapshots, reviews, notes, and instructions more separated, so a source-derived candidate can remain lower authority until it is reviewed and validated.

Read-back differs too. LLM Wiki has ordinary pull search and UI reads, but its synthesis agents also push selected wiki content into LLM calls for newsletters, papers, lint, and analysis. Commonplace usually requires an agent to choose and cite the context it loaded, which is slower but easier to audit.

### Borrowable Ideas

**Monitor deduplication as a small SQLite sidecar.** Ready when Commonplace has recurring web/source monitors. A tiny `ingested_ids` table is enough to keep polling state out of the durable library while preserving repeat-run behavior.

**Generated newsletters as workshop summaries.** Ready with constraints. Commonplace could synthesize recent source/review changes into workshop reports, but they should remain summaries or review candidates rather than library notes.

**Priority queues for source triage.** Ready for security-like domains. LLM Wiki's CVSS priority and critical-alert path is a concrete example of source metadata driving processing urgency.

**Do not borrow direct source-to-current-page authority.** LLM Wiki's merge path writes straight into durable pages. Commonplace should keep imported-source extraction, candidate drafts, and reviewed library artifacts distinct.

**Prompt-ratchet scaffolding needs a safer implementation first.** The idea of evaluating prompt changes on a fixed set is useful, but the inspected implementation does not persist generated prompt changes and uses `git reset HEAD~1` for reversion. Commonplace would need patch-level diffs, validation, and revert commits before adopting it.

## Write side

**Write agency:** `manual` `automatic` — Humans and agents can edit wiki Markdown through Obsidian, the React editor, direct files, uploads, and CLI commands; automatic paths fetch sources, normalize files, extract JSON, merge wiki pages, rebuild indexes, run lint, mark conflicts, update confidence, record metrics, generate hypotheses, write experiment logs, create newsletters and papers, and schedule these operations through daemons.

**Curation operations:** `evolve` `synthesize` `invalidate` `promote` — Integration evolves existing wiki pages by merging new claims and incrementing source counts; newsletter and paper agents synthesize new higher-level Markdown artifacts from existing wiki pages; lint and retrospective validation mark pages as `conflict` and write validation reports; source count/confidence reinforcement, CVSS priority handling, and critical-alert paths promote salience without necessarily changing page prose.

### Trace-learning

**Trace source:** `event-streams` `tool-traces` — The qualifying trace-learning path is operational rather than conversational: extraction successes/failures, integration outcomes, prompt experiments, research hypotheses, daemon processing counts, log entries, and git/history events are retained as metrics rows, experiment logs, and operation logs.

**Learning scope:** `per-project` — The retained traces and generated experiments apply to this local wiki/repo, not a cross-install model or shared service.

**Learning timing:** `online` `staged` — Metrics are recorded as pipeline tools run; prompt optimization, research hypotheses, validation, and paper generation run on daemon schedules.

**Distilled form:** `prose` `symbolic` — Distilled outputs include experiment Markdown, research hypothesis entries, generated newsletters/papers, validation reports, and SQLite rows summarizing extraction/integration quality.

**Extraction.** `PromptOptimizer` reads recent extraction failures from `metrics.db`, chooses an improvement hypothesis, asks the LLM to modify a prompt, evaluates on the fixed eval set, records the decision in SQLite and `wiki/experiments.md`, and optionally commits or resets git state ([tools/prompt_optimizer.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/prompt_optimizer.py), [tools/metrics_collector.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/metrics_collector.py)). The important caveat is that the generated prompt is not actually written into `prompts.py`, so the intended trace-to-prompt loop is incomplete at this commit.

**Scope and timing.** The trace-learning loop is best understood as scaffolded meta-learning. The system does retain traces and can derive experiment records from them; it does not yet prove durable behavioral improvement because the generated prompt edit is not applied to the prompt registry.

**Survey fit.** LLM Wiki weakly fits the trace-to-system-definition family: operational traces are meant to drive prompt changes, but the current code mostly produces audit and experiment artifacts. Its stronger implemented learning path is imported-source distillation into wiki pages, which is not trace-learning under the agent-trace definition.

## Read-back

**Read-back:** `both` — Search, article reads, backlinks, git history, and CLI `query.py` are pull surfaces; synthesis, deep lint, newsletter, paper, and some analysis agents push selected retained wiki content into LLM calls without the model issuing a retrieval action.

**Read-back signal:** `coarse` `inferred / lexical` — Deep lint and newsletter generation use broad or recency-bounded page sets; paper and research analysis use substring/topic matching over wiki content, while ordinary query/search uses lexical BM25 only after a user or caller asks.

**Faithfulness tested:** `no` — The repo includes smoke and phase tests for pipeline pieces, state files, indexes, pages, and API availability, but I did not find an ablation or audit showing that retrieved or pushed wiki context changed LLM answers, papers, newsletters, or agent decisions faithfully ([test_e2e.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/test_e2e.py), [test_phase2.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/test_phase2.py)).

**Direction edge cases.** The React UI and FastAPI search are pull: a human or API caller requests a query, page, backlinks, logs, or history ([api_server.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/api_server.py), [ui/src/App.jsx](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/ui/src/App.jsx)). The paper and newsletter agents are push to the synthesis LLM because their host code scans files and inserts selected snippets into prompts before the model call ([tools/paper_agent.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/paper_agent.py), [tools/newsletter_agent.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/newsletter_agent.py)).

**Selection, scope, and complexity.** BM25 pull search ranks all wiki pages and returns the top five nonzero matches. Newsletter push uses modification time and domain/path bucketing, then includes at most five snippets per bucket. Paper-agent push scans for topic strings in page content and includes up to five pages with up to 2,000 characters each for analysis. Deep lint can send 600-character summaries of every wiki page to the LLM. These policies are code-grounded; precision, recall, and context dilution are not verified.

**Authority at consumption.** Search results and article reads are advisory knowledge. Lint, validation, prompt optimization, and daemon schedules have stronger operational authority because their outputs can mark conflicts, change confidence, generate experiments, or trigger further writes. Generated newsletters and papers are prose outputs with high apparent confidence metadata, but their source grounding is coarse.

**Other consumers.** Humans consume the Obsidian vault, React UI, API, logs, index, newsletters, papers, and git history. Daemons, monitors, validators, search endpoints, paper/newsletter agents, prompt optimizer, and research agent consume the same wiki and state artifacts operationally.

## Curiosity Pass

**The repo is two systems layered together.** The source-to-wiki compiler is relatively small and readable; the autonomous research/paper-generation layer is much larger and more aspirational.

**The strongest memory mechanism is not vector retrieval.** The durable advantage comes from compiling sources into pages, frontmatter, status fields, indexes, logs, and reports. BM25 search is useful, but not the architectural center.

**The prompt optimizer is the most interesting and least complete loop.** It has metrics, hypotheses, evaluation, and logging, but not the crucial write of the generated prompt into the active prompt artifact.

**Git history is exposed but not fully governed.** The API can read file history and old file contents through `git log` and `git show`, but automatic writes are ordinary file writes, and prompt optimization uses reset-style rollback.

**Research papers are memory consumers and memory products.** Paper generation reads compiled wiki pages and emits new Markdown papers. That can be valuable as synthesis, but without stronger provenance it can also launder low-confidence wiki claims into polished prose.

## What to Watch

- Whether `PromptOptimizer.commit_prompt_change()` starts writing patchable prompt changes to `tools/prompts.py`; that would turn the current trace-extracted scaffold into a real behavior-changing loop.
- Whether generated newsletters and papers get source-span provenance back to exact wiki pages and source IDs rather than page snippets and broad frontmatter.
- Whether conflict handling grows beyond `[CONFLICT]` tags and status fields into explicit contradiction records with source lineage and resolution decisions.
- Whether BM25 search is replaced or supplemented by an inspectable hybrid retrieval layer; that would change read-back signal and ranking behavior.
- Whether daemon and API writes move from direct file mutation to transactional or reviewable commits; current automation can mutate durable knowledge without a Commonplace-style gate.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: LLM Wiki stores a large compiled wiki, but only search, synthesis, lint, newsletter, and paper paths actually read it back into action.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: LLM Wiki has wiki pages, raw sources, prompts, databases, logs, generated papers, and indexes with different substrates, forms, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: source snapshots, wiki pages, newsletters, search results, and generated papers mostly serve as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: AGENTS.md, prompts, daemon schedules, schemas, status fields, validation logic, queue priorities, and API routes shape future behavior.
- [Use trace extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) - qualifies narrowly: metrics and operation traces feed the prompt/research experiment loops, though prompt edits are not yet persisted.
- [Trace-learning techniques in related systems](../trace-learning-techniques-in-related-systems.md) - places: LLM Wiki is a weak trace-learning case and a stronger imported-source distillation system.
