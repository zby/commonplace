---
description: "LLM Wiki fork with local-first wiki compilation, autonomous source monitors, metrics-backed research tasks, retrospective validation, and synthesis"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-02"
---

# LLM Wiki (kenhuangus)

> Replaced 2026-06-04. See [LLM Wiki (kenhuangus)](./kenhuangus--llm-wiki.md) for the current review.

Ken Huang's LLM Wiki is a local-first knowledge compilation system for agentic AI, AI security, LLM, physical AI, and secure-coding research. It starts as a markdown/Obsidian wiki pipeline that ingests sources, normalizes them, extracts entities and claims with a local LLM, integrates claims into cross-linked wiki pages, and queries the result with BM25. The newer Phase 3 code adds an autonomous daemon, metrics database, prompt-optimization loop, proactive research agent, retrospective validator, newsletter synthesis, and research-paper agent.

**Repository:** https://github.com/kenhuangus/llm-wiki

**Reviewed commit:** [d2bd485921f6c7b6071afbb389f44ab8e4e83c69](https://github.com/kenhuangus/llm-wiki/commit/d2bd485921f6c7b6071afbb389f44ab8e4e83c69)

**Last checked:** 2026-06-02

## Core Ideas

**The base memory substrate is a file-backed wiki.** The README defines a pipeline from source ingestion through normalization, LLM extraction, LLM-assisted integration, linting, indexing, and query ([README.md](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/README.md)). `AGENTS.md` gives the agent a behavioral schema for page templates, update rules, cross-linking, source attribution, confidence scoring, source trust tiers, model routing, human escalation, and logging ([AGENTS.md](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/AGENTS.md)). The canonical retained knowledge is ordinary markdown plus YAML frontmatter under `wiki/`, with `raw/` and generated JSON used as upstream evidence and extraction state.

**The ingestion pipeline compiles source documents into claims.** `tools/ingest.py`, `tools/normalize.py`, `tools/extract.py`, and `tools/integrate.py` implement the staged path described by the README. The integration step creates or updates pages under `wiki/<category>/<subcategory>/`, increments source count, asks the local model to merge old and new claims, marks conflicts when the model emits `STATUS: CONFLICT`, and writes the resulting frontmatter/body pair back to markdown ([tools/integrate.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/integrate.py)). This is source-derived knowledge synthesis, not trace learning by itself.

**Query is BM25 pull over markdown pages.** `tools/query.py` recursively reads `wiki/**/*.md`, excludes `index.md` and `log.md`, tokenizes by lowercase whitespace, scores with `rank_bm25`, and prints the top five non-zero matches ([tools/query.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/query.py)). There is no agent hook that injects selected pages into another agent's prompt. Context efficiency is therefore simple and bounded at the search output layer: top-five result paths and scores are exposed, while any subsequent page loading is a caller decision.

**The daemon makes the wiki autonomous, but not agent-context-push driven.** `tools/daemon.py` polls arXiv, CVE, GitHub, and RSS monitors, queues new sources with CVSS-sensitive priority, processes up to ten queued items per cycle, periodically runs lint and index rebuilds, and writes a `CRITICAL_ALERT.md` for high-severity CVEs ([tools/daemon.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/daemon.py)). `tools/unified_daemon.py` schedules source processing continuously, prompt optimization every four hours, research hypotheses every six hours, retrospective validation every seven days, and paper generation every fourteen days ([tools/unified_daemon.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/unified_daemon.py)). These loops push work into the wiki pipeline, not memories into an agent context.

**Phase 3 adds trace-sensitive maintenance surfaces.** `tools/metrics_collector.py` creates SQLite tables for extraction metrics, integration outcomes, prompt experiments, research hypotheses, and daily summaries ([tools/metrics_collector.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/metrics_collector.py)). `tools/prompt_optimizer.py` reads recent extraction failures, generates a prompt-improvement hypothesis, asks an LLM to draft an improved prompt, evaluates on a fixed test set, and logs the experiment to the database and `wiki/experiments.md`; however, its commit path explicitly says the full implementation would modify `prompts.py`, and the reviewed code mostly stages the file without writing the generated prompt into it ([tools/prompt_optimizer.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/prompt_optimizer.py)). The qualifying trace-derived path is therefore narrower than a true prompt ratchet.

**Research and synthesis agents consume the wiki as working memory.** `tools/research_agent.py` scans the wiki for coverage gaps, low-confidence pages, synthesis opportunities, and outdated pages, then logs hypotheses to the metrics database and `wiki/experiments.md` ([tools/research_agent.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/research_agent.py)). `tools/retrospective_validator.py` scans recently updated pages, detects existing conflict tags, changes page status/confidence, and emits `wiki/validation_report.md` ([tools/retrospective_validator.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/retrospective_validator.py)). `tools/newsletter_agent.py`, `tools/paper_agent.py`, and `tools/paper_agent_long.py` synthesize recent pages and broader wiki content into newsletters and long-form papers ([tools/newsletter_agent.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/newsletter_agent.py), [tools/paper_agent.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/paper_agent.py), [tools/paper_agent_long.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/paper_agent_long.py)).

## Artifact analysis

- **Storage substrate:** `files` — Filesystem directories under `raw/auto_ingest/`, `raw/normalized/`, and related source queues
- **Representational form:** `prose` `symbolic` — Prose markdown and reports plus symbolic frontmatter, JSON sidecars, links, Python prompt/config constants, and SQLite tables
- **Lineage:** `authored` `imported` `trace-extracted` — Authored agent policy/prompts and daemon code, imported source documents and monitor inputs, and trace-extracted metrics/reports from extraction, integration, validation, and page-state events
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Wiki pages and reports provide knowledge; `AGENTS.md`, prompts, daemon schedules, validators, BM25 scores, metrics rows, and prompt experiments instruct, route, validate, rank, and feed learning loops

**Raw sources and normalized markdown.** Storage substrate: filesystem directories under `raw/auto_ingest/`, `raw/normalized/`, and related source queues. Representational form: prose markdown with frontmatter and source metadata. Lineage: imported from monitors, manual files, arXiv, CVE/NVD, GitHub, RSS, or curated feeds; normalized files are derived from raw sources and should be regenerated when source parsing or domain routing changes. Behavioral authority: knowledge artifacts. They provide evidence and context for extraction, integration, validation, and later human/agent review.

**Extracted JSON and integrated wiki pages.** Storage substrate: JSON sidecars beside normalized sources and markdown files under `wiki/`. Representational form: mixed symbolic/prose: JSON entities/claims/relationships, YAML frontmatter, Obsidian links, and markdown claim bodies. Lineage: extracted by local/cloud LLM calls configured in `tools/common.py`, then merged by `tools/integrate.py`; invalidated by source changes, prompt changes, model changes, or merge-policy changes. Behavioral authority: wiki pages are knowledge artifacts when queried or synthesized, but their frontmatter status/confidence and conflict markers also have light routing/evaluation force for validators and research agents.

**Agent behavioral schema and prompts.** Storage substrate: repository files such as `AGENTS.md`, `tools/prompts.py`, `.env.example`, phase docs, and daemon schedules. Representational form: prose rules plus symbolic Python constants/config. Lineage: authored project policy and later prompt-optimizer candidates. Behavioral authority: system-definition artifacts. `AGENTS.md` instructs compatible coding agents; prompt functions shape extraction/integration behavior; daemon intervals and monitor configuration route work.

**SQLite metrics and state databases.** Storage substrate: `metrics.db` and `state.db` in the repository root, created by `MetricsCollector` and `common.get_state_db()`. Representational form: symbolic relational tables and time-series rows. Lineage: generated from extraction outcomes, integration outcomes, prompt experiments, research hypotheses, daily summaries, and monitor deduplication events. Behavioral authority: evaluation, routing, and learning input. These tables decide prompt-optimization baselines, hypothesis numbering, ingestion deduplication, and some scheduling decisions, but the prompt optimizer does not yet persist generated prompt text as the active prompt artifact.

**Experiments, validation, newsletters, and paper outputs.** Storage substrate: markdown files such as `wiki/experiments.md`, `wiki/validation_report.md`, `wiki/synthesis/newsletters/*.md`, and `papers/*.md`. Representational form: prose reports with frontmatter in synthesized outputs. Lineage: generated from operational traces, recent wiki modifications, validation scans, wiki pages, and LLM synthesis calls. Behavioral authority: mostly knowledge artifacts for human/agent review; validation updates become system-definition-adjacent when they mutate page `status` or `confidence`.

The main promotion path is source evidence -> extracted claims -> integrated wiki pages -> indexes/query results -> synthesis/report artifacts. A second Phase 3 path is operational/evaluation trace -> metrics row or recent-page scan -> research/validation decision -> experiment log, page status/confidence change, or research/paper task. The repository has weaker promotion governance than Commonplace: many promotions are LLM-judged, and prompt improvement code is partly scaffolded around git actions rather than a fully reviewable migration protocol.

## Comparison with Our System

| Dimension | LLM Wiki (kenhuangus) | Commonplace |
|---|---|---|
| Primary aim | Local autonomous research wiki for AI/security knowledge | Methodology KB for agent-operated knowledge systems |
| Storage substrate | Raw files, markdown wiki, JSON sidecars, SQLite DBs, generated papers/reports | Typed markdown collections, reports, indexes, scripts, git history |
| Runtime surface | Python CLIs, monitors, daemons, local/cloud LLM calls, Obsidian vault | Skills, `AGENTS.md`, `commonplace-*` commands, validators, review gates |
| Context activation | BM25 query and explicit file/page consumption | Agent pull through indexes/search plus instruction and validation surfaces |
| Trace learning | Metrics-backed experiments, research hypotheses, validation reports, and page status/confidence changes | Review runs, gate reports, validation outputs, explicit artifact lifecycle |
| Governance | Frontmatter, confidence/status, lint, logs, metrics, critical alerts | Collection contracts, type specs, schemas, semantic review, generated indexes |

LLM Wiki and Commonplace share a file-first premise: durable knowledge should be inspectable, linkable, and reviewable rather than buried in chat history. Ken Huang's fork is more autonomous and application-specific. It has monitors, a queue, local/cloud model routing, a self-optimization loop, proactive research tasks, retrospective validation, newsletter generation, and paper generation. Commonplace is more explicit about artifact typing, collection register, link semantics, validation contracts, and review lifecycle.

The strongest divergence is governance of learned behavior. LLM Wiki lets operational traces affect confidence scores, statuses, hypotheses, reports, and prompt-experiment logs, but much of that is mediated by an LLM and logged after the fact. Commonplace would want source-retained review artifacts, stronger invalidation, and an explicit promotion boundary before a prompt experiment or validation adjustment becomes authoritative.

**Read-back:** `pull` — For agents over BM25/index/wiki files; daemon queues and scheduled jobs push work through the pipeline, but the source does not implement engineered relevance-gated memory/context push into a receiving agent or model context

The context-efficiency story is mixed. Query is deliberately small because it returns top-five BM25 matches, and source monitors process bounded batches. Research and paper agents, however, gather wiki pages by filesystem scans and truncate snippets ad hoc, so complexity is controlled by simple caps rather than a typed context budget or provenance-aware selector.

### Borrowable Ideas

**Metrics tables as first-class learning traces.** Ready in narrowed form. Commonplace already has review runs and reports; adding structured metrics rows for validation failures, gate decisions, and repair outcomes could make improvement loops easier to audit without relying on prose logs alone.

**Autonomous maintenance with explicit schedules.** Needs a concrete operational use case. The unified daemon's schedule is a useful shape for background maintenance, but Commonplace should keep the authority of background tasks low until their outputs pass review gates.

**Prompt experiments with keep/revert decisions.** Borrow the ratchet pattern, not the current implementation. A Commonplace version would write a proposed prompt artifact, evaluate it on fixed scenarios, record gate outputs, and promote only through an explicit review path.

**Retrospective validation reports.** Ready as a concept. Commonplace could periodically inspect recently touched notes for contradictions, confidence changes, and stale sources, then write reviewable reports rather than mutating high-authority artifacts directly.

**Newsletter and paper synthesis as generated views.** Useful for outward-facing summaries, but they should stay derived knowledge artifacts. Commonplace should not let generated synthesis outrank the typed notes and source snapshots it summarizes.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
**Trace source:** `session-logs` `event-streams` — Operation logs, extraction/integration metrics, monitor deduplication events, wiki page-state changes, validation scans, and generated experiment/hypothesis records
**Learning scope:** `per-project` `cross-task` — The loops operate within one wiki repository while aggregating failures, page states, validation results, and research gaps across many wiki tasks
**Learning timing:** `online` `staged` — The daemon runs as live maintenance over the repository, while prompt optimization, research, validation, and paper generation are scheduled cycles
**Distilled form:** `prose` `symbolic` — Trace loops produce prose experiment logs, validation reports, hypotheses, newsletters, and papers plus symbolic metrics rows, page status/confidence fields, and prompt candidates

LLM Wiki (kenhuangus) qualifies for `trace-derived`, but narrowly. The ordinary source ingestion path is external-source-derived, not trace-derived, and the prompt optimizer is not yet a true prompt-writing ratchet. The qualifying mechanisms are evaluation/operation traces stored in metrics tables, research hypotheses derived from wiki state, and retrospective validation that mutates durable page `status` and `confidence` fields from recent-page/update traces.

**Trace source.** The raw signals include extraction failures and successes, integration outcomes, JSON validity, confidence and conflict metrics, monitor ingestion IDs, wiki page modification times, low-confidence pages, stale pages, existing `[CONFLICT]` markers, and generated experiment/hypothesis decisions. These traces are stored in SQLite tables, `wiki/log.md`, `wiki/experiments.md`, and generated validation reports.

**Extraction.** The extraction oracle varies by loop. Prompt optimization uses `MetricsCollector.get_recent_failures()`, baseline metrics, an LLM-generated hypothesis, test-set evaluation, and threshold rules in `make_decision()`, but does not write the generated prompt into the active prompt file at this commit. The research agent uses filesystem and frontmatter heuristics to identify coverage gaps, low confidence, synthesis opportunities, and outdated pages. The validator uses modification time, frontmatter, body sections, conflict tags, and source-count/confidence heuristics. These are practical but shallow judges; they do not prove semantic correctness.

**Scope and timing.** The trace loops are project-local and scheduled: prompt optimization every four hours, research every six hours, validation weekly, and paper generation biweekly in the unified daemon. They are online maintenance loops over one wiki repository, not cross-project model learning.

**Survey placement.** This system strengthens the survey's distinction between logs as evidence and traces as learning input. It does not merely write operation logs; it uses failure tables and page-state traces to choose prompt experiments, research tasks, validation adjustments, and generated reports. It also shows the risk of weak promotion boundaries: validation changes and research-task logs can become behavior-shaping without the kind of typed review gate Commonplace would require, while prompt experiments remain mostly logged candidates until the prompt file is actually changed.

## Curiosity Pass

The README frames the system as a stateful knowledge compilation engine, and the code does implement a real filesystem/SQLite pipeline. The surprising part is how quickly it broadens from wiki maintenance into autonomous research management, prompt optimization, validation, newsletter writing, and paper drafting.

The prompt optimizer is conceptually important but not fully closed-loop in the code reviewed. `apply_hypothesis()` produces a new prompt string, while `commit_prompt_change()` mostly stages and commits `tools/prompts.py`; the implementation comments acknowledge that a fuller version would actually modify `prompts.py`.

The daemon's integration step currently routes extracted JSON into a default `concepts/agentic-ai/test-integration` target. That makes the autonomous loop less semantically precise than the architecture docs imply.

The system has multiple confidence mechanisms, but they are not equivalent. Source trust tiers in `AGENTS.md`, extraction confidence in claims, page confidence in frontmatter, metrics baselines, and validation confidence adjustments all share the same word while serving different authorities.

The project has more generated/planning/status docs than most reviewed systems. Those documents are useful for intent and deployment posture, but the review relies on implementation files for mechanism claims.

## What to Watch

- Whether prompt optimization begins writing explicit prompt versions and diffs instead of logging an unmaterialized candidate string; that would make the trace-derived learning loop reviewable.
- Whether daemon integration stops using the fixed `concepts/agentic-ai/test-integration` target and routes by extracted source metadata; that decides whether autonomous ingestion can maintain a real wiki without human cleanup.
- Whether retrospective validation gains source-level contradiction checks rather than detecting pre-existing `[CONFLICT]` markers and simple confidence heuristics.
- Whether metrics rows become linked from generated reports and wiki page frontmatter, giving humans a navigable lineage from a page status/confidence change back to the operational trace that caused it.
- Whether BM25 query results are wrapped in an agent-facing context assembly layer. That would reopen the `push-activation` decision if the layer injects selected memories before actions.

## Bottom Line

LLM Wiki (kenhuangus) is a local-first autonomous wiki system with a narrow but real trace-derived maintenance layer. Its most useful contribution for Commonplace is not the wiki pipeline alone, but the combination of structured metrics, scheduled maintenance loops, retrospective validation, and generated synthesis artifacts. Its main weakness is authority control: operational traces can influence page status, confidence, research direction, and prompt-experiment logs without a strong typed promotion gate.

Relevant Notes:

- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw sources, extracted claims, wiki pages, newsletters, validation reports, and generated papers when consumed as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: `AGENTS.md`, prompt definitions, daemon schedules, monitor configuration, and validation/update code when they instruct, route, evaluate, or mutate behavior.
- [Lineage](../../notes/definitions/lineage.md) - applies: source-derived wiki pages and trace-derived metrics/reports need different invalidation and promotion paths.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - frames: the difference between advisory wiki content, evaluation traces, and prompt/daemon artifacts with system-definition force.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - clarifies: BM25 search and wiki storage do not by themselves create an engineered memory push path.
