---
description: "Executable LLM Wiki review: source monitors, local LLM extraction, markdown wiki storage, BM25 search, linting, UI/API, metrics, and incomplete prompt optimization"
type: ../types/agent-memory-system-review.md
tags: [related-systems]
status: current
last-checked: "2026-05-16"
---

# LLM Wiki (kenhuangus)

LLM Wiki is Ken Huang's executable local-first knowledge pipeline for turning monitored sources into a persistent markdown wiki. It is not the same design as the promptware-only LLM Wiki protocol reviewed elsewhere: this repo ships Python monitors, ingestion, normalization, LLM extraction, LLM-assisted integration, BM25 query, linting, daemon orchestration, metrics tables, a FastAPI service, and a React UI around a checked-in `wiki/` tree.

**Repository:** https://github.com/kenhuangus/llm-wiki

**Reviewed commit:** [d2bd485921f6c7b6071afbb389f44ab8e4e83c69](https://github.com/kenhuangus/llm-wiki/commit/d2bd485921f6c7b6071afbb389f44ab8e4e83c69)

## Core Ideas

**The primary substrate is a markdown wiki with separate source layers.** The README frames the pipeline as `source -> ingest -> normalize -> extract -> integrate -> wiki`, with raw sources under `raw/auto_ingest/`, normalized markdown under `raw/normalized/`, and canonical pages under `wiki/` ([README.md](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/README.md)). The code follows that split: `ingest.py` copies or downloads sources into `raw/auto_ingest/{source_type}/`, `normalize.py` writes frontmatter-bearing normalized markdown keyed by an eight-character content hash, and `integrate.py` writes merged pages into `wiki/{category}/{subcategory}/` ([tools/ingest.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/ingest.py), [tools/normalize.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/normalize.py), [tools/integrate.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/integrate.py)). Raw and normalized files are knowledge artifacts when used as evidence; integrated wiki pages are the retained knowledge artifacts future search, UI, and agents consume.

**LLM extraction is JSON-first, but the contract is prompt-defined rather than type-defined.** `extract.py` reads a normalized markdown file, calls `get_extraction_prompt()`, sends the body to the configured local or fallback model, strips optional code fences, parses JSON, adds `source_id`, and writes `{normalized_path}.json` ([tools/extract.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/extract.py)). The operative representational form is mixed: prose sources, symbolic frontmatter, JSON entities/claims/relationships, and prompt text in `tools/prompts.py` ([tools/prompts.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/prompts.py)). The prompt registry is a system-definition artifact because it configures what the extractor and integrator are allowed to produce.

**Integration merges claims into ordinary wiki pages.** `integrate.py` converts extracted claims into a `## Claims` section, preserves source IDs as Obsidian links, and either creates a new page or asks the model to merge old and new claims. If the model returns `STATUS: CONFLICT`, the page frontmatter becomes `status: conflict` ([tools/integrate.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/integrate.py)). This gives integration prompt text system-definition authority: it is not just documentation, it decides whether new claims reinforce, conflict, or move to historical sections.

**Monitors are source collectors, not memory learners.** arXiv, RSS, GitHub, and CVE monitors fetch new external items, deduplicate with SQLite state, and write source files into `raw/auto_ingest/` ([tools/arxiv_monitor.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/arxiv_monitor.py), [tools/rss_monitor.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/rss_monitor.py), [tools/github_monitor.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/github_monitor.py), [tools/cve_monitor.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/cve_monitor.py)). CVE ingestion can immediately trigger normalize, extract, integrate, and index for high-severity CVEs, and CVSS >= 9 writes `CRITICAL_ALERT.md`; that is a priority/escalation policy over external source data, not trace-derived learning from the system's own action outcomes.

**Search is disposable BM25 over the wiki, not a canonical vector store.** `query.py` scans all markdown files under `wiki/`, excludes `index.md` and `log.md`, tokenizes by lowercase whitespace, builds an in-memory `BM25Okapi` index, and returns the top scored files ([tools/query.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/query.py)). The ranking index is runtime state, not a retained artifact. The durable substrate remains markdown pages plus git history.

**Governance exists as agent rules, lint, index, logs, and UI affordances.** `AGENTS.md` defines page templates, source attribution, confidence scoring, source tiers, model routing, human escalation, prohibited actions, and logging requirements ([AGENTS.md](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/AGENTS.md)). `lint.py` checks required frontmatter, warns on high unverified confidence, and optionally asks an LLM to detect contradictions and mark pages as conflicts ([tools/lint.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/lint.py)). `index.py` rebuilds `wiki/index.md` with coverage summaries and pending review pages ([tools/index.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/index.py)). These files are system-definition artifacts because they instruct, validate, escalate, and route future behavior.

**The UI/API makes the wiki an editable local service.** `api_server.py` exposes search, ingest, article read/write, upload, backlinks, logs, git history, and stats endpoints over FastAPI ([api_server.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/api_server.py)). The React UI uses those endpoints for search, article browsing, edit/save, history, upload, backlinks, logs, and status panels ([ui/src/App.jsx](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/ui/src/App.jsx)). This is more product-shaped than a pure folder of notes, but the API can also overwrite article files directly, so UI edits have weaker validation authority than the pipeline path.

**Prompt optimization is present but not yet a real ratchet.** `PromptOptimizer` loads an eval set, asks the LLM for an improved prompt, evaluates extraction on sample files, records metrics, and logs experiments ([tools/prompt_optimizer.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/prompt_optimizer.py), [tools/metrics_collector.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/metrics_collector.py)). At this commit, however, `commit_prompt_change()` only stages `tools/prompts.py`; it does not write the generated prompt into that file before committing, and rollback uses `git reset HEAD~1`. The checked-in `wiki/experiments.md` shows reverted experiments and malformed research-hypothesis output, which is useful audit evidence but not a durable learned prompt update ([wiki/experiments.md](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/wiki/experiments.md)).

## Comparison with Our System

| Dimension | LLM Wiki (kenhuangus) | Commonplace |
|---|---|---|
| Primary substrate | Markdown `wiki/` plus `raw/`, SQLite state, metrics DB, logs, git history, FastAPI/UI | Typed markdown under `kb/`, generated indexes, review reports, validation outputs, git |
| Source model | External feeds and manual files become raw and normalized source artifacts | Source snapshots, notes, references, instructions, reviews, and workshop artifacts |
| Extraction model | LLM prompt extracts entities, claims, relationships JSON | Mostly human/agent-authored notes governed by collection/type contracts |
| Retrieval | In-memory BM25 over wiki markdown plus UI search | `rg`, descriptions, curated/generated indexes, authored links, skills |
| Governance | AGENTS rules, frontmatter lint, LLM contradiction lint, operation log, conflict status, critical alerts | Type specs, collection conventions, deterministic validation, semantic review gates, link vocabulary |
| Runtime | Python scripts, daemon, FastAPI, React UI, local/cloud LLM calls | Local CLI commands and agent skills around a repo-native KB |
| Learning loop | Metrics and prompt-optimizer scaffolding, but no proven prompt mutation at this commit | Review, validation, manual revision, and promotion from work artifacts to library artifacts |

The strongest alignment is the "knowledge compilation" posture. Both systems prefer durable readable files over answering from transient retrieval alone. LLM Wiki pushes more work into an executable ingestion pipeline: sources arrive from monitors, get normalized, extracted, integrated, searched, linted, and rendered. Commonplace pushes more work into artifact contracts and review discipline: the system cares less about continuous source harvesting and more about what kind of retained artifact is allowed to shape agent behavior.

The main divergence is authority precision. In LLM Wiki, many behavior-shaping rules live in general-purpose prompt text and scripts: extraction schema, integration semantics, source tiers, conflict policy, lint checks, daemon schedules, and API write permissions. Commonplace tries to make those distinctions explicit in collection docs, type specs, schemas, validation, link labels, and review procedures. LLM Wiki is more executable but less explicit about when a wiki page is merely evidence versus when a prompt, lint rule, daemon schedule, or API endpoint has instruction, validation, routing, or enforcement force.

LLM Wiki is also much more source-ingestion oriented. Its durable artifacts are mostly derived from outside publications, releases, advisories, and feeds. That makes it closer to an automated local research desk than to an agent memory system that learns from its own task traces. The metrics and prompt optimizer point toward self-improvement, but the inspected implementation has not crossed the boundary into reliable outcome-to-behavior learning.

## Borrowable Ideas

**Keep raw, normalized, extracted, and integrated layers separate.** Ready to borrow for high-volume source ingestion. Commonplace already snapshots sources, but LLM Wiki's explicit raw/normalized/JSON/wiki split is a useful staging pattern when sources arrive continuously and need replayable processing.

**Use cheap BM25 as the first executable search layer.** Ready as a pragmatic option. LLM Wiki gets useful query behavior without committing to a vector store, and the index can be rebuilt from files on demand. A commonplace analogue could sit below authored links and curated indexes as a disposable search accelerator.

**Treat an operation log as part of governance.** Ready to borrow in limited form. `wiki/log.md` gives a chronological record of ingest, normalize, extract, integrate, lint, index, monitor, and experiment events. Commonplace has git and review outputs, but a compact append-only activity log could help agents understand recent automated maintenance.

**Escalate high-risk domains at ingestion time.** Ready as a pattern, not as CVE-specific code. LLM Wiki routes high-severity CVEs into immediate processing and writes critical alerts. Commonplace could use the same shape for high-risk note classes: the source monitor marks priority, and the workflow routes it to review before ordinary publication.

**Do not borrow direct UI writes without validation.** The UI's article save endpoint writes markdown immediately. That is ergonomic, but for commonplace it would need validation and review hooks before it could safely modify library artifacts.

**Do not count prompt-optimization scaffolding as learned memory until it mutates a real behavior surface.** The prompt optimizer has the right evaluation-loop outline, but at this commit the generated prompt does not become the active prompt. The borrowable lesson is the acceptance criterion: a learning loop only matters when an evaluated outcome changes a durable system-definition artifact.

## Curiosity Pass

**The checked-in wiki is itself evidence of the pipeline's strengths and weaknesses.** Pages under `wiki/concepts/`, `wiki/entities/`, and `wiki/security/` show the intended derived-artifact surface, while `wiki/log.md` shows real monitor, normalize, extraction, conflict, and rate-limit events ([wiki/log.md](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/wiki/log.md)). Some generated claims look brittle or future-dated, which reinforces that the system needs its lint and human-review surfaces.

**The daemon and API disagree on integration discipline.** `WikiDaemon` processes sources through normalize, extract, integrate, lint, and index paths, but the API can save arbitrary article content directly to `wiki/` ([tools/daemon.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/tools/daemon.py), [api_server.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/api_server.py)). That is a governance split: one write path is pipeline-mediated, the other is editor-mediated.

**The extraction schema is intentionally small.** Entities, claims, and relationships are enough to seed a wiki, but not enough to preserve detailed lineage, contradiction provenance, source trust, supersession policy, or block-level review state. Those details are partly in frontmatter, prompts, logs, and AGENTS rules rather than in a stable artifact schema.

**Git history is exposed as a product feature.** The API can return file history and a file's content at a commit using `git log` and `git show` ([api_server.py](https://github.com/kenhuangus/llm-wiki/blob/d2bd485921f6c7b6071afbb389f44ab8e4e83c69/api_server.py)). That makes version history a user-facing knowledge surface, not just a developer fallback.

**Trace-derived status is not supported at this commit.** The repo stores operation logs, metrics, experiments, and git history, but the inspected code does not show a real loop from agent/session/tool traces or outcome trajectories into a durable behavior-changing artifact. External source ingestion, source deduplication, and prompt-optimizer scaffolding are not enough.

## What to Watch

- Whether `PromptOptimizer` starts writing generated prompt candidates into `tools/prompts.py`, switching active prompt versions, and preserving commit-level lineage for kept improvements.
- Whether metrics collection becomes integrated into ordinary extraction and integration paths beyond daemon-mediated processing.
- Whether raw/normalized JSON/page lineage becomes explicit enough to audit which source sentence produced which wiki claim.
- Whether API article writes gain validation, lint, review, or conflict checks before saving.
- Whether BM25 remains enough as the wiki grows, or whether retrieval adds stable indexes, embeddings, or source-aware ranking.
- Whether source monitors add stronger freshness, redaction, and trust controls for feeds that can be noisy or adversarial.

---

Relevant Notes:

- [Files not database](../../notes/files-not-database.md) - exemplifies: LLM Wiki keeps the canonical readable surface in markdown while using SQLite and runtime indexes around it
- [Designing agent memory systems](../../notes/designing-agent-memory-systems.md) - compares-with: LLM Wiki improves future answers by changing the retained wiki and prompt/lint surfaces, not by storing memory as an opaque service object
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - defined-in: raw, normalized, extracted, and integrated wiki artifacts mostly act as evidence, context, and reference
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - defined-in: AGENTS rules, prompts, lint checks, daemon schedules, API write paths, and escalation policies configure or validate behavior
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - contrasts: this repo has source ingestion and incomplete optimizer scaffolding, but not a qualifying trace-to-artifact learning loop at the reviewed commit
- [LLM Wiki](./llm-wiki.md) - compares-with: the same name covers a promptware protocol in one review and an executable Python/React pipeline here
