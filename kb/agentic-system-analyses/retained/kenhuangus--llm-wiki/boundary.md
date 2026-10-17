---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "LLM Wiki's shipped knowledge-production, maintenance and consumption paths at Git revision d2bd485921f6c7b6071afbb389f44ab8e4e83c69."
run-id: AAS-2026-10-17-llm-wiki-507fade8a56e-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: d2bd485921f6c7b6071afbb389f44ab8e4e83c69
analysis-cutoff: "2026-10-17"
evidence-tier: code-grounded
source:
  identity: https://github.com/kenhuangus/llm-wiki
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-20-kenhuangus--llm-wiki/related-systems/kenhuangus--llm-wiki
  revision: d2bd485921f6c7b6071afbb389f44ab8e4e83c69
  sha256: null
---

# LLM Wiki boundary

## Boundary and evidence

LLM Wiki is in scope as a **memory/knowledge/context-engineering system**. Its intended use is to compile incoming research and security sources into a persistent Markdown wiki, maintain that wiki, and make retained material available to people and subsequent model calls. This is not merely the integration library: the repository ships monitors, batch and daemon drivers, a manual-drop watcher, maintenance and evaluation programs, a FastAPI service, and a React client. Those callers and consumers belong to the target (SRC-1: `README.md`, `tools/pipeline_all.py`, `tools/daemon.py`, `tools/unified_daemon.py`, `tools/watchdog_monitor.py`, `api_server.py`, `ui/src/App.jsx`).

The boundary is **whole-system** at commit `d2bd485921f6c7b6071afbb389f44ab8e4e83c69`, with applicability cutoff **2026-10-17**. The acquired checkout's HEAD matches that pin and its working tree was clean when inspected. Only the frozen repository supplies evidence. The overall tier is **code-grounded**: executable paths were traced across source acquisition, normalization, model extraction, persisted integration, maintenance, retrieval and later synthesis. A complete boundary does not mean every advertised feature works or that a successful autonomous run has been observed.

### Functional inclusions and entry-point trace

- **Admission and production:** `tools/ingest.py` accepts files or URLs; arXiv, CVE, GitHub, RSS and curated monitors produce incoming files. `tools/common.py` supplies shared deduplication state and configuration. `tools/pipeline_all.py` invokes monitors, discovers raw files, normalizes, extracts, integrates and rebuilds the catalog. The CVE monitor also has its own high-severity pipeline. `tools/watchdog_monitor.py` supplies another complete driver for manual drops (SRC-1: those paths).
- **Model-mediated retention:** `tools/normalize.py` writes content-derived Markdown paths; `tools/extract.py` reads normalized content, requests structured knowledge and persists a JSON sidecar; `tools/integrate.py` builds a wiki destination from caller-supplied category, subcategory and title. When that page already exists, the implementation reloads its body and supplies old and new claims to the model before rewriting the page. Extraction and integration prompts are shipped in `tools/prompts.py`, not inferred from the README (SRC-1: those paths).
- **Orchestration and maintenance:** `tools/daemon.py` polls monitors and processes a priority queue; its own main loop schedules lint and index work. `tools/unified_daemon.py` calls the source-processing methods and separately schedules optimization, research, retrospective validation and paper generation. These are distinct shipped paths, not interchangeable evidence for one another. Include the prompt optimizer, research agent, validator, lint and metrics collector, including their incomplete or placeholder branches; do not assume their names establish their advertised effects (SRC-1: `tools/daemon.py`, `tools/unified_daemon.py`, `tools/prompt_optimizer.py`, `tools/research_agent.py`, `tools/retrospective_validator.py`, `tools/lint.py`, `tools/metrics_collector.py`).
- **Consumption and feedback:** `tools/query.py` reloads wiki Markdown and ranks lowercased whitespace tokens with BM25. `api_server.py` calls that search function, reads and saves pages, accepts uploads, initiates ingestion, and exposes Git-backed history. `ui/src/App.jsx` calls those endpoints and is therefore included, not treated as an external application. `tools/newsletter_agent.py` reads recently modified wiki pages and persists synthesis back under the wiki; `tools/paper_agent.py` and `tools/paper_agent_long.py` consume retained wiki content to generate draft files under `papers/` (SRC-1: those paths).
- **Governance and evaluation:** include `AGENTS.md`, `research_agenda.md`, `tools/prompts.py`, the evaluation-set builder, manifest and fixtures, root test scripts and `tools/test_*.py`. Instructions express intended constraints; executable checks express what is checked. Neither establishes that every declared rule is enforced (SRC-1: those paths).

The minimum implementation evidence for the classification is the explicit reuse of retained content in a later model call (SRC-1: `tools/integrate.py`):

> system_prompt = get_integration_prompt()
> input_text = f"Old Claims:\n{exist_body}\n\nNew Claims:\n{new_claims_body}"
> --- `tools/integrate.py`

The independent later-consumption path is also explicit (SRC-1: `tools/paper_agent.py`):

> # Step 2: Analyze wiki for insights
> print("\n🔍 Analyzing wiki for novel insights...")
> wiki_insights = self._analyze_wiki(topics)
> --- `tools/paper_agent.py`

Shipped governance requires preserving and distinguishing historical claims; this is doctrine, not proof of runtime compliance (SRC-1: `AGENTS.md`):

> - Retain historical claims by shifting them to a `## Historical Claims` section.
> - Add `[CONFLICT]` to the section and log it in `log.md` when two sources contradict directly.
> --- `AGENTS.md`

### Top-level coverage

Every tracked top-level file or directory is classified below. Grouped rows enumerate their members. All rows refer to SRC-1; paths in directory rows identify material responsibilities rather than merely naming a directory. “Included” fixes functional scope, not an assertion that every byte was read. Initial inspection used the tracked tree, scoped searches and selected file reads. Available material not yet read in detail is identified separately from unavailable evidence.

| Top-level tracked entries | Classification and role | Initial inspection and limits |
|---|---|---|
| `tools/` | Included: `common.py`; `ingest.py`, `normalize.py`, `extract.py`, `integrate.py`; `arxiv_monitor.py`, `cve_monitor.py`, `github_monitor.py`, `rss_monitor.py`, `curated_monitor.py`, `run_all_monitors.py`; `pipeline_all.py`, `watchdog_monitor.py`, `daemon.py`, `unified_daemon.py`; `prompts.py`, `prompt_optimizer.py`, `research_agent.py`, `retrospective_validator.py`, `metrics_collector.py`; `lint.py`, `index.py`, `query.py`; `newsletter_agent.py`, `paper_agent.py`, `paper_agent_long.py`; `create_eval_set.py`, `check_model_config.py`, `test_daemon.py`, `test_optimizer.py`, `test_research_agent.py`. | Main production, scheduling, persistence, retrieval and maintenance paths read; additional monitor, research and evaluator entry points searched. Paper generation and long-form override inspected at their wiki-read and orchestration paths. Remaining detailed prompts and diagnostic branches remain available, not access gaps. `tools/__pycache__/common.cpython-313.pyc` is excluded as a generated cache; no bytecode/source-equivalence claim. |
| `api_server.py` | Included: service entry point, ingestion driver, article read/write, search, uploads, backlinks and Git history. | Full source read; included as a shipped state producer and consumer. No live-server behavior established. |
| `ui/` | Included: `src/main.jsx`, `src/App.jsx`, API-facing read/search/edit/upload/history flows; `package.json`, Vite configuration and HTML entry point. | API calls and component dispatch inspected in `src/App.jsx`; remaining rendering/build details available but not exhaustively inspected. CSS, images, public icons and dependency lock data are excluded from behavioral analysis; no visual fidelity or dependency-security conclusion. |
| `tasks/` | Included: `schedule_monitors.ps1`, `start_watchdog.ps1`, host scheduling and watcher launch. | Searched task registrations and launch commands. Windows Task Scheduler execution and installation success not observed. |
| `raw/` | Included: `auto_ingest/{arxiv,cve,github,manual}/`, `normalized/{agentic-ai,ai-security}/`, and shipped extraction sidecars as retained input artifacts. | Tracked inventory and `raw/normalized/agentic-ai/8218a40c.md` inspected alongside producer/consumer code. Remaining documents are available, not individually verified; their scientific/security claims are not analysis evidence merely because they were ingested. |
| `wiki/` | Included: `concepts/`, `entities/`, `security/`, `synthesis/`, `index.md`, `log.md`, `experiments.md`, `validation_report.md`. Persisted knowledge, derived catalogs and operation records; `synthesis/curated-sources.md` also supplies future monitor topics. | Tree inventoried; curated-source table and `entities/models/gpt-5-eval.md` read; maintenance and consumer code traced. Other page bodies and logs not yet audited in detail. These tracked files do not by themselves establish trustworthy operation or claim accuracy. |
| `eval_set/`, `eval_set_index.json` | Included: optimizer's retained evaluation inputs, sidecars and file manifest. | Builder and optimizer loading/evaluation code read; inventory and manifest header sampled. No benchmark execution or independent ground-truth judgment. |
| `AGENTS.md`, `research_agenda.md` | Included: behavioral doctrine, source attribution, trust and confidence conventions, research priorities, experiment constraints and human escalation. | Both read completely as target-authored contracts, not instructions binding this analysis. |
| `README.md`, `llm-wiki.md` | Included: public operating description and product/design specification. | README read completely; specification inventoried but not yet read in detail. Implementation trace, not an uninspected design passage, grounds the boundary. |
| `.env.example`, `.gitignore` | Included: configuration surface and retention/exclusion policy. | Sections and relevant state/configuration references searched; runtime defaults read in `tools/common.py`. Actual operator secrets/configuration and ignored databases are not supplied by the tracked source. |
| `.obsidian/` | Included: `app.json`, `community-plugins.json`, `core-plugins-workspace.json` as vault integration configuration. Excluded: bundled `plugins/dataview/{main.js,manifest.json,styles.css}` implementation. | Configuration files read. Obsidian and plugin execution are outside the analyzed wiki-processing implementation; exclusion prevents claims about dashboard behavior, plugin internals or automatic Git commits actually occurring. |
| `.vscode/` | Excluded: `settings.json`, editor-local setup rather than knowledge-loop logic. | Inventory/configuration search only; no editor integration behavior conclusion. |
| `test_api.py`, `test_e2e.py`, `test_ingest.py`, `test_llm.py`, `test_phase2.py`, `test_user_workflow.py` | Included: shipped test and diagnostic entry points covering model/API access, ingestion, persisted artifacts and user-facing consumption. | Scoped searches of test functions, requests, subprocess calls and assertions; end-to-end pipeline calls identified. Not executed; test presence is not a passing result. |
| `check_rss_state.py`, `clear_rss_state.py`, `configure_lms_max_context.sh` | Included: retained-state inspection/reset helpers and model-server configuration helper. | Entry-point/state references and shell configuration flow searched. No state reset or model-server command executed. |
| `temp_source.txt` | Included as a tracked input/test artifact, not an executable entry point. | Inventory only; contents not yet inspected. No inference about its claims or provenance. |
| `AUTONOMOUS_LOOP_DIAGRAM.md`, `DAEMON_COMPARISON.md`, `SYSTEM_ARCHITECTURE.md`, `PHASE3_AUTONOMOUS_RESEARCH_PLAN.md`, `PHASE3_EXECUTIVE_SUMMARY.md`, `README_PHASE3.md` | Included as target-authored architecture and planned operation. | Heading-scanned, not yet read in detail; no implementation or observed-operation conclusion taken from these descriptions. |
| `DEPLOYMENT_CHECKLIST.md`, `LMS_CLI_CONFIGURATION.md`, `MODEL_CONTEXT_ANALYSIS.md`, `PAPER_AGENT_GUIDE.md`, `QUICK_START.md`, `README_CONFIGURATION.md` | Included as target-authored deployment, configuration and generation instructions. | Heading-scanned; detailed operating recipes remain available. No installed-environment compatibility conclusion. |
| `FINAL_SUMMARY.md`, `GITIGNORE_UPDATE_SUMMARY.md`, `IMPLEMENTATION_COMPLETE.md`, `IMPLEMENTATION_STATUS.md`, `LOCAL_CHANGES_SUMMARY.md`, `NEURIPS_PAPER_SUMMARY.md`, `PAPER_AGENT_SUMMARY.md`, `PHASE2_TESTING_REPORT.md`, `PHASE3_FINAL_SUMMARY.md`, `PHASE3_PROGRESS.md`, `PUSH_COMPLETE.md`, `SECURITY_UPDATE_COMPLETE.md`, `VIEW_HISTORY_IMPLEMENTATION.md`, `WIKI_UI_STATUS.md` | Included as target-authored status, testing and implementation narratives, not independent evaluations. | Heading-scanned only. Detailed claims are not yet inspected and support no success, performance, novelty or deployment conclusion here. |

### External dependencies and evidence limits

The system depends on Python packages, a writable filesystem, SQLite and Git, plus the FastAPI/Uvicorn and React/Vite stacks for its browser interface. Source admission depends on remote arXiv, NVD, GitHub, RSS/article services, optional Semantic Scholar access and DuckDuckGo search. These remote systems' implementations and current responses are excluded; the boundary can establish request/processing logic but not feed availability, freshness, completeness or upstream correctness (SRC-1: `README.md`, `tools/common.py`, `tools/arxiv_monitor.py`, `tools/cve_monitor.py`, `tools/github_monitor.py`, `tools/rss_monitor.py`, `tools/curated_monitor.py`, `api_server.py`, `ui/src/App.jsx`).

Model inference is an external service boundary. The implementation supplies a primary configured chat-completions endpoint and an OpenRouter fallback; model weights, provider internals and live responses are excluded. This prevents conclusions about answer quality, grounding, latency, model compliance and fully local operation. Obsidian, Windows scheduling and operator/coding-agent decisions are external execution environments; their configuration and shipped instructions are included, but their responsibilities are not attributed to the Python code (SRC-1: `tools/common.py`, `AGENTS.md`, `tasks/schedule_monitors.ps1`, `.obsidian/community-plugins.json`).

No target program, example or test was executed. No independently inspectable run trace or causal experiment was supplied or established during this boundary job. Runtime `state.db`, `metrics.db`, local `.env`, generated `papers/` outputs and live services are not part of the tracked frozen evidence set. Their absence prevents reconstruction of an operator's actual queue/deduplication history, measured optimization outcomes, effective deployment settings or paper-generation success. Available target-authored reports and tracked wiki logs are not access gaps; if later used, their claims require attributed, bounded treatment rather than promotion to independently observed operation (SRC-1: `.gitignore`, `tools/common.py`, `tools/metrics_collector.py`, `tools/paper_agent.py`).

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/kenhuangus/llm-wiki` | d2bd485921f6c7b6071afbb389f44ab8e4e83c69 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-20-kenhuangus--llm-wiki/related-systems/kenhuangus--llm-wiki`. Implementation: tracked tree; production stages, prompts, batch/daemon/watcher drivers, API, React API consumers, lint/index/query, optimizer, validator, research execution branches, metrics schema, wiki-consuming paper/newsletter generation and evaluator creation/loading; scoped monitor, task and test searches. Doctrine/design: full `README.md`, `AGENTS.md`, `research_agenda.md`, vault JSON configuration; headings of other root documentation. Retained input/wiki/manifest samples as named in the coverage table. | Implementation: [integration](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/integrate.py), [unified driver](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/unified_daemon.py), [API](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/api_server.py), [paper consumer](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/paper_agent.py). Doctrine/design: [agent contract](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/AGENTS.md), [research agenda](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/research_agenda.md). | No checkout access gap encountered. Uninspected available details are marked in the coverage table. External inference/feed/host execution, operator-local configuration/state and generated outputs are outside this frozen evidence set; no deployment-success, accuracy, sustained self-improvement or causal-effect conclusion. No observed-run or causal-experiment layer established. |
