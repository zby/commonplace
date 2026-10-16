---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "VLM-wiki's shipped personal knowledge workflow and supporting scripts at commit 503c43f98b5d1e21c74df384fdffd3e0652573b3."
run-id: AAS-2026-10-14-vlm-wiki-311faef777b4-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "503c43f98b5d1e21c74df384fdffd3e0652573b3"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/veniVeci/VLM-wiki
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/vlm-wiki-311faef777b4/related-systems/veniVeci--VLM-wiki
  revision: "503c43f98b5d1e21c74df384fdffd3e0652573b3"
  sha256: null
---

# VLM-wiki boundary

## Boundary and evidence

VLM-wiki is in scope as a **memory/knowledge/context-engineering system**: it ships instructions for model-assisted compilation of personal media into a persistent Markdown wiki, later question answering from that wiki, and scripts that import, analyse, maintain and deliver retained content. Its intended use is personal recollection, knowledge organization and reflection, not hosting a general-purpose agent runtime. This is a **whole-system** boundary over the repository's shipped workflow, instructions, scripts, configuration, templates and example state. It does not imply that the repository implements its own agent host or that every documented operation has an executable implementation. SRC-1: `README.md`, `AGENTS.md`, `scripts/qwen_vlm_analyzer.py`, `scripts/reflection_engine.py`.

The declared persistence and reuse contract is explicit:

> Build and maintain a personal full-modal knowledge base using VLMs (Vision Language Models) and LLMs. Manage multiple directories for different media types, compile them into unified wiki articles. The wiki compounds over time.
> --- `AGENTS.md`

> 1. Read `wiki/index.md` to locate relevant articles
> 2. Read those articles and synthesize an answer
> 3. Prefer wiki content over training knowledge
> 4. Cite sources with wiki-internal links: `[[Category/Article]]`
> --- `AGENTS.md`

### Functional scope and traced entry points

- **Model-assisted authoring and later query:** the English and Chinese agent instructions cover initialization, image/video/audio/text ingest, article format, related-page updates, pattern discovery, query and archive maintenance. The model-driven wiki-writing and query responsibilities are included as shipped instructions, not attributed to a Python agent loop. SRC-1: `AGENTS.md`, `AGENTS.zh.md`, `references/article-template.md`, `references/archive-template.md`.
- **Admission and media processing:** the importer loads configuration and a persisted manifest, copies local files into raw storage, records import state and reloads it on later invocations. The video extractor writes sampled frames; the metadata analyser persists an analysis JSON. The Qwen batch driver calls a model and writes per-image Markdown and a summary; the two single-image drivers also persist responses next to their input. These shipped callers are included, not treated as external applications. SRC-1: `scripts/import_data_sources.py`, `scripts/video_extractor.py`, `scripts/image_analyzer.py`, `scripts/qwen_vlm_analyzer.py`, `scripts/run_analysis_now.py`, `scripts/single_image_demo.py`.
- **Retained-content consumption and maintenance:** the reflection engine reads articles across seven wiki categories and diary Markdown, computes summaries and recommendations, then writes daily/weekly review Markdown, a runtime brief and log entries. Its inspected implementation is deterministic Python; its inclusion does not establish model-based reflection. SRC-1: `scripts/reflection_engine.py`.
- **Work-project production and delivery:** the work scanner reads configured external project files and Git metadata, writes project articles, replaces the index's Projects section, writes a review and runtime payload, and appends a log entry. The cycle driver invokes that producer and then the WeCom reader/sender unless push is skipped. Windows CMD/PowerShell wrappers launch the cycle and retain a local log. All those repository-owned paths are included. SRC-1: `scripts/work_project_reflection.py`, `scripts/run_work_reflection_cycle.py`, `scripts/run_work_reflection_task.cmd`, `scripts/run_work_reflection_task.ps1`, `scripts/wecom_push.py`.
- **Supporting state and repair:** base/local configuration merging, templates, current index/log/articles, example analyses, and the disclaimer-rewriting helper are included. Runtime output names referenced by code remain within the functional boundary even where their files are not tracked. SRC-1: `scripts/config_utils.py`, `.vlmwiki/config.json`, `.gitignore`, `scripts/update_vlm_docs.py`, `wiki/index.md`, `wiki/log.md`.

The scheduled cycle's shipped producer-to-consumer handoff is retained here to establish that neither side is excluded:

> run_step(["python", "scripts/work_project_reflection.py", "--timestamp", timestamp])
> if not args.skip_push:
>     run_step(["python", "scripts/wecom_push.py", f"wiki/reviews/{review_file}"])
> --- `scripts/run_work_reflection_cycle.py`

The implementation also explicitly reloads retained wiki and diary content before generating reviews:

> records = collect_articles()
> diaries = collect_diaries()
> summary = summarize_articles(records)
> --- `scripts/reflection_engine.py`

### Top-level tracked coverage

Every top-level tracked entry at the frozen commit is classified below. Included means part of the analysis boundary, not proof of successful execution. All listed text was inspected; media bytes were enumerated but deliberately not visually audited. No material shipped executable or instruction path remains uninspected.

| Top-level entry | Treatment and inspected material paths | Role and limits |
|---|---|---|
| `.gitignore` | Included; inspected `.gitignore` (SRC-1). | Retention boundary for private local configuration, runtime state and generated project/review pages. Ignored files are not supplied evidence. |
| `.vlmwiki/` | Included; inspected `.vlmwiki/config.json` (SRC-1), and its loader `scripts/config_utils.py`. | Shipped model/storage/import/work-scan/delivery settings. Local override and runtime artifacts are referenced but unavailable; no deployed configuration or execution outcome is inferred. |
| `AGENTS.md` | Included; inspected `AGENTS.md` (SRC-1). | English model-facing authoring, maintenance and query contract; doctrine rather than evidence of host compliance. |
| `AGENTS.zh.md` | Included; inspected `AGENTS.zh.md` (SRC-1). | Chinese model-facing contract, including ingestion, retrieval and archive operations. |
| `CONTRIBUTING.md` | Included; inspected `CONTRIBUTING.md` (SRC-1). | Contributor setup and testing guidance. Its local-run example does not supply test results. |
| `LICENSE` | Included; inspected `LICENSE` (SRC-1). | MIT distribution terms, not operational evidence. |
| `README.md` | Included; inspected `README.md` (SRC-1). | English intended use, manual triggers, import, reflection and delivery entry points. Feature claims require implementation-level checking. |
| `README_zh.md` | Included; inspected `README_zh.md` (SRC-1). | Chinese workflow and import/WeCom/work-reflection instructions. |
| `raw/` | Included as example input and retained analysis state; inspected `raw/analysis_results.json`, all six `raw/images/*_analysis.md` files and `raw/videos/2023-05-frames/frame_analysis.md` (SRC-1). Enumerated image/video files and empty audio/diary/text placeholders. | Source media and attributed analysis examples. Pixel/video-content auditing is deliberately excluded; this prevents judging caption accuracy or reconstructing model execution from matching media. No raw-state producer or consumer is excluded. |
| `references/` | Included; inspected `references/raw-template.md`, `references/article-template.md`, `references/archive-template.md`, `references/index-template.md`, `references/import-guide.zh.md` (SRC-1). | Input/article/archive/index contracts and admission guide. Templates do not establish automatic enforcement. |
| `scripts/` | Included; inspected all tracked scripts: `scripts/config_utils.py`, `scripts/import_data_sources.py`, `scripts/video_extractor.py`, `scripts/image_analyzer.py`, `scripts/qwen_vlm_analyzer.py`, `scripts/run_analysis_now.py`, `scripts/single_image_demo.py`, `scripts/reflection_engine.py`, `scripts/work_project_reflection.py`, `scripts/run_work_reflection_cycle.py`, `scripts/run_work_reflection_task.cmd`, `scripts/run_work_reflection_task.ps1`, `scripts/wecom_push.py`, `scripts/update_vlm_docs.py`; also `scripts/.env.example`, `scripts/requirements.txt`, `scripts/requirements-qwen.md` (SRC-1). | Complete shipped code/driver/helper surface, model prompts, dependencies and usage guidance. Tree inspection and bounded searches for test/eval/benchmark/audit found no dedicated evaluator or automated test suite; `CONTRIBUTING.md` instead points to a single-image live analysis command. No execution or evaluation is claimed. |
| `wiki/` | Included; inspected `wiki/index.md`, `wiki/log.md`, both `wiki/moments/` articles and all three `wiki/places/` articles; enumerated category placeholders in archives, concepts, patterns, people and projects (SRC-1). | Retained knowledge, navigation and reported maintenance history. The log is attributed reported operation, not an independently inspectable model-call trace. Generated reviews/projects are covered through their producer and consumer code, not assumed present. |

### Dependencies, exclusions and evidence limits

The enclosing AI IDE/agent host, its tools and its model-selection behavior are external dependencies. The instructions say that an unconfigured model falls back to the current IDE's built-in model; the repository does not supply that IDE's implementation. Excluding host internals prevents conclusions about actual instruction loading, tool authority, model fallback, autonomous scheduling or host-enforced source immutability. The shipped instructions themselves remain included. SRC-1: `AGENTS.md`, `AGENTS.zh.md`.

External model-provider operation, exported source folders, the user's configured work-project tree, Windows scheduler registration/state, Markdown editors and WeCom servers are not frozen by this repository. This prevents conclusions about model quality, real personal-data coverage, installed recurrence, delivery success and user outcomes. The repository-owned model request construction, scanner, wrappers and delivery adapter remain included and inspectable. SRC-1: `scripts/qwen_vlm_analyzer.py`, `scripts/import_data_sources.py`, `scripts/work_project_reflection.py`, `scripts/run_work_reflection_task.ps1`, `scripts/wecom_push.py`, `README.md`.

Private local configuration, ignored runtime manifests/briefs/logs and generated review/project pages are unavailable in the frozen tracked evidence. This prevents reconstruction of an actual deployed cycle or longitudinal reuse history, but not source-level tracing of their writers and readers. These are unavailable evidence, distinct from deliberately uninspected image/video contents. SRC-1: `.gitignore`, `scripts/config_utils.py`, `scripts/import_data_sources.py`, `scripts/reflection_engine.py`, `scripts/work_project_reflection.py`.

The frozen evidence is SRC-1 at **503c43f98b5d1e21c74df384fdffd3e0652573b3**, verified against the supplied checkout HEAD. The applicability cutoff is **2026-10-14**; it is a run cutoff, not an assertion that the source was current on that date. The overall tier is **code-grounded** because shipped implementations and their callers were inspected. Instruction-only features remain doctrine/design, and checked-in analyses/logs remain attributed reported operation. No target code, tests, examples, model calls or service requests were executed. No observed-run or causal-experiment evidence is established by this boundary.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/veniVeci/VLM-wiki` | 503c43f98b5d1e21c74df384fdffd3e0652573b3 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/vlm-wiki-311faef777b4/related-systems/veniVeci--VLM-wiki`. Implementation: every tracked Python/CMD/PowerShell file under `scripts/`, including model prompts, admission, persistence, reload, work-cycle callers and delivery. Doctrine/design: both READMEs, both AGENTS files, all reference templates/guides, base configuration, requirements/setup guidance, contribution guide, ignore policy and license. Reported operation: all tracked wiki articles/index/log, raw metadata JSON, six image-analysis Markdown files and frame-analysis Markdown. Full tracked tree enumerated; image/video bytes not visually inspected. | Implementation: [model analysis](https://github.com/veniVeci/VLM-wiki/blob/503c43f98b5d1e21c74df384fdffd3e0652573b3/scripts/qwen_vlm_analyzer.py), [importer](https://github.com/veniVeci/VLM-wiki/blob/503c43f98b5d1e21c74df384fdffd3e0652573b3/scripts/import_data_sources.py), [retained-content consumer](https://github.com/veniVeci/VLM-wiki/blob/503c43f98b5d1e21c74df384fdffd3e0652573b3/scripts/reflection_engine.py), [work producer](https://github.com/veniVeci/VLM-wiki/blob/503c43f98b5d1e21c74df384fdffd3e0652573b3/scripts/work_project_reflection.py), [cycle](https://github.com/veniVeci/VLM-wiki/blob/503c43f98b5d1e21c74df384fdffd3e0652573b3/scripts/run_work_reflection_cycle.py), [delivery](https://github.com/veniVeci/VLM-wiki/blob/503c43f98b5d1e21c74df384fdffd3e0652573b3/scripts/wecom_push.py). Doctrine/design: [agent contract](https://github.com/veniVeci/VLM-wiki/blob/503c43f98b5d1e21c74df384fdffd3e0652573b3/AGENTS.md), [configuration](https://github.com/veniVeci/VLM-wiki/blob/503c43f98b5d1e21c74df384fdffd3e0652573b3/.vlmwiki/config.json). Reported operation: [wiki log](https://github.com/veniVeci/VLM-wiki/blob/503c43f98b5d1e21c74df384fdffd3e0652573b3/wiki/log.md), [metadata artifact](https://github.com/veniVeci/VLM-wiki/blob/503c43f98b5d1e21c74df384fdffd3e0652573b3/raw/analysis_results.json). | Implementation lacks supplied execution evidence; host/provider/WeCom internals and private external input folders are outside this frozen source. Ignored local configuration and runtime/generated outputs are unavailable. Doctrine does not establish execution; checked-in reports do not establish model-call provenance, quality or causal benefit. Deliberate media-content exclusion prevents accuracy auditing, not functional loop coverage. |
