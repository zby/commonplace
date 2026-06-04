---
description: "VLM-wiki review: multimodal personal wiki with raw media, VLM analysis notes, Markdown articles, Obsidian browsing, and pull-only index/article read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-03"
---

# VLM-wiki

VLM-wiki, from `VeniVeci/VLM-wiki`, is a small file-first personal knowledge-base scaffold inspired by Karpathy's LLM Wiki idea. At the reviewed commit it is not a packaged memory server, RAG service, or autonomous agent runtime. It is a repository layout, agent instruction file, templates, sample raw media, sample compiled wiki pages, and a few Python scripts for extracting video frames, recording image metadata, and calling a Qwen-compatible VLM for image captions.

**Repository:** https://github.com/VeniVeci/VLM-wiki

**Reviewed commit:** [9813fb12de9b82c9279a47c537a8c94a68292de0](https://github.com/VeniVeci/VLM-wiki/commit/9813fb12de9b82c9279a47c537a8c94a68292de0)

**Last checked:** 2026-06-03

## Core Ideas

**Raw media and compiled wiki pages are deliberately separated.** The README and `AGENTS.md` define a three-layer project: immutable-ish `raw/` source material, maintained `wiki/` articles, and `.vlmwiki/config.json` model/storage settings ([README.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/README.md), [AGENTS.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/AGENTS.md), [.vlmwiki/config.json](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/.vlmwiki/config.json)). That gives the system a clear lineage story: raw files remain inspectable evidence, while Markdown wiki articles are derived, organized views.

**The distinctive twist is multimodal intake, not retrieval infrastructure.** The repo adds image/video/audio directories and VLM-oriented instructions to the LLM Wiki shape. The implemented media code is modest: `video_extractor.py` samples five evenly spaced frames with OpenCV, `image_analyzer.py` records basic PIL metadata into `raw/analysis_results.json`, and `qwen_vlm_analyzer.py` can submit images to `qwen3.5-omni-flash` and save Markdown analysis files ([scripts/video_extractor.py](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/scripts/video_extractor.py), [scripts/image_analyzer.py](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/scripts/image_analyzer.py), [scripts/qwen_vlm_analyzer.py](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/scripts/qwen_vlm_analyzer.py)).

**The agent contract carries more architecture than the code.** `AGENTS.md` tells an assistant to ingest images, videos, audio, and diary/text; update `wiki/moments/`, `wiki/people/`, `wiki/places/`, `wiki/projects/`, `wiki/concepts/`, `wiki/patterns/`, and `wiki/archives/`; update `wiki/index.md`; and append to `wiki/log.md` ([AGENTS.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/AGENTS.md)). There is no implemented CLI that performs the full cascade, so the review treats this as a host-agent instruction surface rather than a verified autonomous workflow.

**Context efficiency is index-first and human-readable, but weakly enforced.** Query instructions say to read `wiki/index.md`, locate relevant articles, then synthesize an answer from those articles ([AGENTS.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/AGENTS.md), [wiki/index.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/wiki/index.md)). Volume is bounded by starting from the index and opening selected Markdown pages rather than loading all media. Complexity is still largely up to the acting assistant: there is no search ranking, token budget, freshness filter, or schema validator beyond the article template.

**The sample wiki demonstrates a raw-to-article distillation path.** The Qingdao travel article links diary text, images, extracted video frames, image analysis, and a video file into a single `moment` article with frontmatter, media references, related links, sources, and metadata ([wiki/moments/2023-05-青岛旅行.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/wiki/moments/2023-05-%E9%9D%92%E5%B2%9B%E6%97%85%E8%A1%8C.md), [raw/analysis_results.json](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/raw/analysis_results.json), [raw/videos/2023-05-frames/frame_analysis.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/raw/videos/2023-05-frames/frame_analysis.md)). This is the strongest implemented memory mechanism: authored and generated source material is consolidated into navigable Markdown.

**Adoption affordance is high because the output is just an Obsidian vault.** The README explicitly frames the wiki as Markdown browsable in Obsidian, and the templates use ordinary YAML frontmatter, relative raw-file links, and Obsidian `[[links]]` ([README.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/README.md), [references/article-template.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/references/article-template.md), [references/raw-template.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/references/raw-template.md)). The cost is governance: article shape is conventional, not enforced.

## Artifact analysis

- **Storage substrate:** `files` — The central retained state is the project filesystem: `raw/` media and diary/text files, `wiki/` Markdown articles/index/log, `references/` templates, `.vlmwiki/config.json`, and local script outputs.
- **Representational form:** `prose` `symbolic` — prose Markdown/articles/logs/instructions/analysis outputs and symbolic JSON/config/frontmatter/links/templates/scripts participate in the memory path; raw media remains file evidence rather than a controlled representational-form token.
- **Lineage:** `authored` `imported` — raw files are authored, imported, or captured by the user, while analysis notes, compiled wiki articles, index/log entries, templates, config, scripts, and instructions are authored or derived from imported raw material.
- **Behavioral authority:** `knowledge` `instruction` `routing` — raw material, analysis outputs, and compiled articles serve as knowledge/context; `AGENTS.md`, templates, config, and scripts instruct the host agent; `wiki/index.md` routes lookup toward selected articles.

**Raw material files.** Storage substrate: files under `raw/images/`, `raw/videos/`, `raw/audio/`, `raw/text/`, and `raw/diary/` ([README.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/README.md), [AGENTS.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/AGENTS.md), [raw/diary/2023-05-06.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/raw/diary/2023-05-06.md)). Representational form: mixed binary media and prose text. Lineage: authored, imported, or captured by the user; `AGENTS.md` says raw files are immutable and wiki pages should cite them. Behavioral authority: knowledge artifacts as source evidence for later article writing and question answering.

**VLM and media analysis outputs.** Storage substrate: Markdown and JSON files such as `raw/images/*_analysis.md`, `raw/videos/2023-05-frames/frame_analysis.md`, `raw/analysis_results.json`, and possible `raw/qwen_vlm_results/*` outputs from the Qwen script ([raw/images/微信图片_20260503182120_190_41_analysis.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/raw/images/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20260503182120_190_41_analysis.md), [scripts/qwen_vlm_analyzer.py](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/scripts/qwen_vlm_analyzer.py), [scripts/image_analyzer.py](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/scripts/image_analyzer.py)). Representational form: prose captions/analyses plus symbolic metadata. Lineage: derived from raw media by a human/model/script pipeline; the repo contains some analysis files, but only part of their generation is implemented and repeatable in the scripts. Behavioral authority: knowledge artifacts and intermediate evidence for compiled wiki pages; they do not directly instruct an agent except when loaded during a task.

**Compiled wiki articles.** Storage substrate: Markdown files under `wiki/moments/`, `wiki/people/`, `wiki/places/`, `wiki/projects/`, `wiki/concepts/`, `wiki/patterns/`, and `wiki/archives/`. Representational form: prose Markdown with YAML frontmatter, raw media references, tags, summaries, source links, and Obsidian links. Lineage: LLM/VLM-maintained according to `AGENTS.md`, with the sample Qingdao article derived from diary, images, video frames, and analysis outputs ([AGENTS.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/AGENTS.md), [wiki/moments/2023-05-青岛旅行.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/wiki/moments/2023-05-%E9%9D%92%E5%B2%9B%E6%97%85%E8%A1%8C.md)). Behavioral authority: knowledge artifacts when queried; weak system-definition artifacts only when a host agent treats a wiki article as instruction or pattern guidance.

**`wiki/index.md` and `wiki/log.md`.** Storage substrate: Markdown files in `wiki/`. Representational form: symbolic tables and append-only log prose. Lineage: maintained by the acting agent or human as articles are created/updated. Behavioral authority: routing and audit artifacts; the index decides what article a future agent is likely to open first, while the log preserves operation history ([wiki/index.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/wiki/index.md), [wiki/log.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/wiki/log.md)).

**`AGENTS.md`.** Storage substrate: repository Markdown instruction file. Representational form: prose procedure with command triggers, article schema, query policy, and logging conventions. Lineage: authored system-definition artifact shipped with the repo. Behavioral authority: host-agent instruction if the assistant environment loads it; it tells the agent how to ingest, update, query, and archive memory ([AGENTS.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/AGENTS.md)).

**Configuration and scripts.** Storage substrate: `.vlmwiki/config.json` plus Python scripts under `scripts/`. Representational form: symbolic JSON and Python code. Lineage: authored package scaffolding, with user-editable model/provider/storage settings. Behavioral authority: system-definition artifacts for model choice, raw/wiki base paths, supported formats, feature flags, frame extraction, image metadata extraction, and Qwen VLM calls ([.vlmwiki/config.json](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/.vlmwiki/config.json), [scripts/requirements.txt](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/scripts/requirements.txt)).

**Templates.** Storage substrate: Markdown templates under `references/`. Representational form: symbolic/prose skeletons. Lineage: authored scaffolds copied or followed when creating raw records, articles, archives, and indexes. Behavioral authority: weak system-definition convention: they shape article structure but are not validated or enforced ([references/article-template.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/references/article-template.md), [references/index-template.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/references/index-template.md)).

There is a promotion path from raw media and diaries to analysis notes to compiled wiki articles to index entries, but no implemented promotion from candidate insight to validated rule or enforced gate. Pattern pages are a stated destination; the inspected repo does not implement a detector or validator for them.

## Comparison with Our System

| Dimension | VLM-wiki | Commonplace |
|---|---|---|
| Primary purpose | Personal multimodal life wiki from photos, videos, audio, diary, and text | Git-native methodology KB for agents and maintainers |
| Main substrate | Project files: raw media, Markdown wiki, templates, config, scripts | Typed Markdown collections, sources, instructions, ADRs, indexes, validation, and review reports |
| Memory making | Host agent plus small scripts distill media/text into category articles | Deliberate source capture, note writing, type contracts, validation, semantic review, and promotion |
| Retrieval/read-back | Read index, then selected wiki articles | `rg`, generated indexes, authored links, collection contracts, skills, review reports |
| Governance | Templates, AGENTS instructions, operation log, raw/source links | Schemas, collection contracts, deterministic validation, semantic gates, git diffs, archive workflow |
| Multimodal handling | Native raw media folders and VLM-oriented analysis notes | Mostly textual artifacts and source snapshots; media is incidental rather than first-class |

VLM-wiki is closest to Commonplace in its insistence that durable memory remain visible as files. It is also a useful reminder that a KB can preserve rich non-text evidence while compiling human/agent-readable Markdown views. The separation between `raw/` and `wiki/` is especially compatible with Commonplace's source/synthesis split.

The main divergence is authority discipline. In VLM-wiki, `AGENTS.md` tells an assistant to create and update articles, but the repo does not provide type validation, schema enforcement, review states, stale-source detection, or generated indexes beyond the manually maintained Markdown table. That is fine for a personal life wiki demo; it is too weak for Commonplace's methodology claims, where a derived note needs reviewable lineage and explicit authority.

The other divergence is context strategy. VLM-wiki relies on a global index and category folders. Commonplace has a deeper navigation stack: collection contracts, type specs, generated indexes, curated indexes, links, reports, validation, and command workflows. VLM-wiki's simplicity is appealing, but it leaves relevance and context budgeting mostly in the acting agent's judgment.

**Read-back:** `pull` — Retained memory reaches the agent when the agent or user asks a query and the agent follows `AGENTS.md` by reading `wiki/index.md` and selected articles; the repo does not implement automatic memory push, pre-action hooks, semantic retrieval, or a selection budget.

### Borrowable Ideas

**Treat raw multimodal evidence as a first-class source layer.** A Commonplace analogue would keep source media under `kb/sources/` or a dedicated source subtree, then derive textual notes with explicit citations and review status. Ready as a convention if a real media-heavy KB appears.

**Keep raw-to-compiled lineage visible in the article body.** VLM-wiki's sample moment article ends with source links to diary, photos, video, frames, and analysis JSON. Commonplace already does this for textual sources; the borrow is to preserve that discipline for media-derived notes. Ready now.

**Use a simple operation log for personal KB changes.** `wiki/log.md` is weaker than git plus review reports, but it is more legible to a non-technical user. Commonplace could expose a generated human-facing activity log without replacing git history. Needs a consumption use case.

**Do not borrow unenforced pattern discovery.** The README advertises habit, mood, place, and relationship patterns, but the inspected code does not implement those detectors. Commonplace should keep pattern claims as candidate notes until grounded by code, evidence, or review.

**Separate adoption templates from governance.** VLM-wiki's templates are good onboarding surfaces. Commonplace should preserve the distinction between scaffolded shape and validated artifact quality.

## Write-side placement

**Write agency:** `manual` `automatic` — humans and host agents maintain raw/wiki/index/log files under `AGENTS.md`, while the media scripts can write frame, metadata, and VLM analysis outputs from retained raw media.

**Curation operations:** `consolidate` — the implemented scripts and sample workflow derive smaller analysis/wiki views from raw media and diary material, but the review does not find an enforced detector, validator, or automatic promotion path.

## Curiosity Pass

**The repository is partly a demo vault, not only a tool.** It contains sample Qingdao travel media, generated wiki pages, analysis outputs, and logs. That makes the memory model concrete, but also means some behavior is demonstrated by checked-in state rather than implemented as reusable commands.

**The VLM story is narrower in code than in prose.** The README and `AGENTS.md` describe image, video, audio, text, pattern discovery, and query workflows. The implemented scripts cover video frame extraction, image metadata extraction, and Qwen image analysis; audio transcription, full wiki update cascades, and pattern discovery are instruction-level behavior rather than verified code.

**Some analysis artifacts are not reproducibly generated by the visible scripts.** The checked-in image analysis files cite a Doubao multimodal model, while the reusable VLM script calls Qwen through an OpenAI-compatible DashScope endpoint. That is not necessarily wrong, but it weakens the repo as a reproducible pipeline.

**The index is both navigation and authority.** Since query instructions start with `wiki/index.md`, missing or stale rows can hide memory from the agent even when the underlying article exists. The repo has no validator to compare the index against the filesystem.

**The raw layer creates a privacy/governance problem earlier than text-only KBs.** Photos, videos, audio, people, places, and mood patterns are sensitive; the repo treats them as local files and gives no access-control or redaction mechanism beyond ordinary filesystem control.

## What to Watch

- Whether VLM-wiki adds an actual ingest CLI that updates raw analysis files, wiki articles, index rows, and log entries together. That would move the project from instruction scaffold to implemented memory workflow.
- Whether pattern discovery gains code, tests, or evaluation examples. That would change the review from media distillation to behavior-shaping life-pattern learning.
- Whether audio transcription and video captioning become implemented rather than described. That would test whether the "full-modal" claim is more than directory structure.
- Whether the index becomes generated or validated from article frontmatter. That would make read-back less dependent on manual consistency.
- Whether article frontmatter gets a schema or review state. That would move VLM-wiki closer to governed KB operation rather than Obsidian-style note convention.

## Bottom Line

VLM-wiki is a clear file-first multimodal personal wiki scaffold. Its useful design contribution is not a novel retrieval engine; it is the raw-to-compiled split for media-heavy memory, with Obsidian-readable Markdown as the human/agent interface. For Commonplace, it is most valuable as a reminder that non-text evidence needs preserved source lineage and compiled textual views, while its instruction-only automation and weak governance are not enough for high-authority knowledge artifacts.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: VLM-wiki stores multimodal memory in files, but activation depends on explicit index/article lookup.
- [Preserve evidence without loading history](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) - aligns: raw media and diary files remain available while compiled wiki pages carry the smaller working view.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - grounds: VLM-wiki separates raw files, VLM analysis notes, compiled articles, indexes/logs, instructions, config, scripts, and templates by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw media, analysis notes, and wiki articles mainly advise later work as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: `AGENTS.md`, `.vlmwiki/config.json`, templates, and scripts define behavior for the host agent and analysis workflow.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: the index-first query path is the repo's main context-routing strategy.
