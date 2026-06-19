---
description: "VLM-wiki review: file-backed multimodal personal wiki scaffold with AGENTS instructions, raw media, VLM analysis scripts, and Obsidian Markdown read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-05"
---

# VLM-wiki

VLM-wiki, from `VeniVeci/VLM-wiki`, is a local-first personal knowledge-base scaffold inspired by Karpathy's LLM Wiki and extended toward images, video, audio, diary, and text. At the reviewed commit it is mostly an agent instruction file, directory contract, templates, checked-in demo wiki, and small media-analysis scripts: raw media and generated analysis stay in `raw/`, compiled knowledge pages stay in `wiki/`, and the agent is instructed to maintain Obsidian-readable Markdown rather than using a database or packaged memory service.

**Repository:** https://github.com/VeniVeci/VLM-wiki

**Reviewed commit:** [9813fb12de9b82c9279a47c537a8c94a68292de0](https://github.com/VeniVeci/VLM-wiki/commit/9813fb12de9b82c9279a47c537a8c94a68292de0)

**Last checked:** 2026-06-05

## Core Ideas

**The central memory substrate is a raw-to-wiki file hierarchy.** `AGENTS.md` defines `raw/` as immutable source material, `wiki/` as VLM/LLM-maintained compiled articles, `.vlmwiki/config.json` as model/storage configuration, and `wiki/index.md` plus `wiki/log.md` as navigation and operation history. The checked-in demo follows that shape with raw diary/media files, generated media-analysis Markdown, place pages, a moment page, an index, and a log ([AGENTS.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/AGENTS.md), [.vlmwiki/config.json](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/.vlmwiki/config.json), [wiki/index.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/wiki/index.md), [wiki/log.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/wiki/log.md)).

**The agent contract is broader than the implemented scripts.** `AGENTS.md` specifies initialization, image/video/audio/text ingest, wiki article format, query behavior, pattern discovery, archives, and logging. The Python code I found implements image metadata extraction, Qwen image analysis, single-image demos, simple video-frame extraction, and a disclaimer patcher for simulated VLM docs; it does not implement the full article integration, index maintenance, query answering, audio transcription, or pattern-discovery loop as a reusable runtime ([AGENTS.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/AGENTS.md), [scripts/image_analyzer.py](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/scripts/image_analyzer.py), [scripts/qwen_vlm_analyzer.py](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/scripts/qwen_vlm_analyzer.py), [scripts/video_extractor.py](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/scripts/video_extractor.py), [scripts/update_vlm_docs.py](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/scripts/update_vlm_docs.py)).

**VLM acquisition produces source-side descriptions, not a hidden memory index.** `qwen_vlm_analyzer.py` scans `raw/images/`, sends base64 image content to `qwen3.5-omni-flash`, writes one Markdown result per image plus `summary.json`, and leaves later wiki integration to the agent/user workflow. `video_extractor.py` samples evenly spaced frames from a video into `raw/videos/...`; the demo wiki then links those frames and the original video from a compiled moment page ([scripts/qwen_vlm_analyzer.py](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/scripts/qwen_vlm_analyzer.py), [scripts/video_extractor.py](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/scripts/video_extractor.py), [raw/analysis_results.json](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/raw/analysis_results.json), [wiki/moments/2023-05-青岛旅行.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/wiki/moments/2023-05-%E9%9D%92%E5%B2%9B%E6%97%85%E8%A1%8C.md)).

**Context efficiency is human/agent navigation over files, not algorithmic retrieval.** The read contract tells the agent to read `wiki/index.md`, open relevant articles, synthesize an answer, prefer wiki content over training knowledge, and cite with Obsidian links. That is efficient relative to replaying all raw media because the index and compiled articles are smaller pointers, but the inspected source has no token budget, ranking function, semantic search, progressive disclosure API, or automatic context packing beyond this index-first instruction ([AGENTS.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/AGENTS.md), [wiki/index.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/wiki/index.md)).

**Adoption comes from Obsidian-readable Markdown and simple templates.** The README emphasizes opening the folder directly in Obsidian, while the templates prescribe YAML frontmatter, raw-media references, related links, sources, metadata, and archive summaries. This keeps retained memory inspectable and editable, but also means quality, linking, and update discipline depend on the host agent following prose instructions ([README.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/README.md), [references/article-template.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/references/article-template.md), [references/raw-template.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/references/raw-template.md), [references/archive-template.md](https://github.com/VeniVeci/VLM-wiki/blob/9813fb12de9b82c9279a47c537a8c94a68292de0/references/archive-template.md)).

## Artifact analysis

- **Storage substrate:** `files` `repo` — The behavior-shaping state is a repository/file tree: `AGENTS.md`, `.vlmwiki/config.json`, `raw/` source media and generated analyses, `wiki/` Markdown articles, `wiki/index.md`, `wiki/log.md`, templates, and Python scripts. There is no inspected database, vector store, graph store, or service object.
- **Representational form:** `prose` `symbolic` — Wiki articles, analysis Markdown, diary notes, agent instructions, templates, and generated descriptions are prose; YAML frontmatter, JSON config/results, directory categories, Obsidian links, media paths, trigger keywords, and Python scripts are symbolic. The repository does not retain embeddings or model weights.
- **Lineage:** `authored` `imported` — The agent contract, templates, config, scripts, and demo wiki pages are authored. Raw media and diary material are imported personal source material, with VLM/image-analysis outputs and compiled pages derived from those sources. I do not classify it as `trace-extracted`: the inspected system derives memory from media/documents, not from agent session logs, tool traces, event streams, trajectories, or rollouts.
- **Behavioral authority:** `knowledge` `instruction` `routing` `learning` — Compiled wiki pages and raw analyses serve as knowledge artifacts for later answers; `AGENTS.md`, templates, config, and trigger keywords instruct and route the host agent's actions; VLM image analysis is an acquisition/learning step from imported media into retained prose. I did not find validation, enforcement, or ranking code beyond ordinary script errors and index/category conventions.

**Raw media and diary material.** Storage substrate: local files under `raw/images/`, `raw/videos/`, `raw/audio/`, `raw/text/`, and `raw/diary/`. Representational form: media bytes, diary prose, generated Markdown analyses, and JSON metadata. Lineage: imported source material plus derived media descriptions. Behavioral authority: evidence for compiled wiki pages and future answers, not direct instruction to the agent.

**Compiled wiki pages.** Storage substrate: Markdown files under `wiki/moments/`, `wiki/places/`, and the other category directories. Representational form: prose articles with symbolic frontmatter, media paths, tags, related links, and source links. Lineage: derived from raw media, diary notes, and generated descriptions, with the checked-in demo showing manual/agent-authored synthesis. Behavioral authority: knowledge context when the agent answers queries or the human browses in Obsidian.

**Index and log.** Storage substrate: `wiki/index.md` and `wiki/log.md`. Representational form: symbolic tables and append-only operation records wrapped in Markdown prose. Lineage: maintained by the agent/user workflow rather than by inspected update code. Behavioral authority: routing and audit context; the query instruction makes `wiki/index.md` the first read surface.

**Agent contract, templates, and config.** Storage substrate: `AGENTS.md`, `references/*.md`, and `.vlmwiki/config.json`. Representational form: prose instructions plus symbolic model/storage settings and article schemas. Lineage: authored system-definition artifacts. Behavioral authority: instruction and routing because they tell a host agent where to write, what to update, how to query, and which model settings to use.

**Media-analysis scripts.** Storage substrate: Python files in `scripts/`. Representational form: symbolic code plus embedded prose prompts. Lineage: authored acquisition utilities. Behavioral authority: learning/acquisition and weak validation through file existence/API-key checks; the scripts can create analysis files, extracted frames, and summaries, but they do not themselves maintain the compiled wiki or enforce article quality.

Promotion path: VLM-wiki has a clear conceptual promotion ladder from raw media/diary material to generated analysis to compiled article to index entry/archive. At this commit the ladder is mostly an instruction contract and demo artifact, not a fully codified pipeline with source-span preservation, deterministic index rebuilding, validation, or automatic stale-entry invalidation.

## Comparison with Our System

| Dimension | VLM-wiki | Commonplace |
|---|---|---|
| Primary purpose | Personal multimodal life wiki for Obsidian browsing and agent-assisted recall | Agent-operated methodology KB with typed reviews, notes, instructions, sources, and validation |
| Source layer | Raw media, diary/text files, generated VLM descriptions | Source snapshots, GitHub checkouts, captured documents, and cited evidence |
| Knowledge layer | Category Markdown pages and an index | Typed Markdown artifacts with collection contracts, schemas, links, generated indexes, and review gates |
| Write path | Prose agent instructions plus narrow acquisition scripts | Direct file edits governed by collection/type contracts, validators, indexes, semantic review, and git history |
| Read path | Agent reads `wiki/index.md`, opens pages, answers with Obsidian links | Agents search, follow indexes/links, load contracts/skills, and validate artifacts |

VLM-wiki and Commonplace share the file-first bet: durable memory should remain inspectable as Markdown, with generated or compiled views acting as navigational aids rather than replacing source material. VLM-wiki is lighter and more adoption-oriented: a user can open the folder in Obsidian and let an AI IDE follow `AGENTS.md`. Commonplace is heavier because its artifacts are meant to support repeatable agent work with explicit types, contracts, validation, source citations, and review state.

The main divergence is governance. VLM-wiki's README says the wiki "writes and maintains itself," but the inspected implementation relies on the host agent honoring instructions. Commonplace treats those same concerns as system-definition artifacts: collection contracts, schemas, validation commands, source citation rules, and generated indexes make the write/read behavior more auditable.

Another useful divergence is modality. Commonplace mostly ingests text/code/web sources; VLM-wiki foregrounds images and videos as first-class memory inputs. Its current acquisition scripts are simple, but the raw-media-to-compiled-note pattern is directly relevant to any future Commonplace source type that includes screenshots, diagrams, UI recordings, or multimodal evidence.

### Borrowable Ideas

**Make raw multimodal evidence a first-class source layer.** Needs a concrete use case first. Commonplace could add source conventions for screenshots or video frames when methodology claims depend on UI or visual evidence, but it would need citation, retention, and privacy rules before adoption.

**Keep compiled pages and raw analyses separate.** Ready now as a design rule. VLM-wiki's raw/generated/compiled split is a good low-friction analogue to Commonplace's sources versus notes: raw evidence can stay broad while compiled artifacts stay readable.

**Use Obsidian compatibility as an adoption constraint.** Ready where it does not weaken contracts. Standard Markdown, frontmatter, and wiki-style backlinks are useful because humans can browse and repair memory outside the agent loop.

**Borrow the index-first query instruction only with validation.** Ready as a weak pattern, not as an implementation. Commonplace already uses indexes, but VLM-wiki shows how easy it is for an index to become an unstated router; generated or curated indexes need freshness checks.

**Do not borrow uncodified self-maintenance claims.** Needs implementation before reuse. A prose instruction that an agent should discover patterns is useful as a prompt, but Commonplace should not treat it as a system mechanism until there is a concrete extraction, review, and invalidation path.

## Write side

**Write agency:** `manual` `automatic` — The main wiki write path is manual/agent-authored editing through `AGENTS.md` instructions and templates. Automatic writes are narrow script outputs: image metadata JSON, Qwen analysis Markdown, extracted video frames, and disclaimer edits to generated analysis files. The inspected code does not automatically integrate those outputs into wiki articles, refresh `wiki/index.md`, discover patterns, or maintain stale/contradictory entries.

**Curation operations:** `consolidate` — The conceptual workflow consolidates raw media, diary notes, generated analyses, and extracted frames into shorter compiled wiki pages such as the Qingdao trip moment. The implemented scripts mainly acquire or transform source-side analysis artifacts; I did not find automatic dedup, evolve, synthesize-across-stored-entries, invalidate, decay, or promote operations over existing wiki memory.

## Read-back

**Read-back:** `pull` — Retained memory reaches future action when a human or host agent deliberately reads `wiki/index.md`, opens relevant wiki articles, or browses the Obsidian vault. The inspected source does not push selected memory into an agent prompt on session start, hook events, or instance-triggered relevance matches.

The query instruction is explicit but pull-only: read the index, locate relevant articles, read them, synthesize an answer, prefer wiki content over training knowledge, and cite with Obsidian links. There is no deployed retrieval API, embedding index, always-loaded memory file, tool hook, or pre-invocation context assembler. If an AI IDE always loads `AGENTS.md`, that is baseline instruction loading, not memory read-back from the accumulated wiki.

Selection scope is page-level and symbol-driven by category, title, tags, related links, and index rows. This can be efficient for a small personal wiki because the agent need not inspect every raw image or video, but precision/recall and context dilution are not verified from code. Authority at consumption is advisory knowledge: wiki pages can guide an answer, but they do not enforce actions, route tools, or gate outputs.

## Curiosity Pass

**The strongest artifact is the instruction contract, not the code.** VLM-wiki is more like an AGENTS.md-operated vault template than an application. That is not a flaw for adoption, but it matters for review: many claimed behaviors are host-agent obligations.

**The multimodal promise currently stops at source description.** The Qwen script can create image-analysis Markdown, and the video script can create frames. Turning those into durable people/place/moment/pattern knowledge is demonstrated in files, not implemented as a reusable pipeline.

**The demo includes simulated or externally generated analysis.** `update_vlm_docs.py` adds disclaimers to simulated VLM analysis docs, while checked-in raw image/video analysis pages name a model and date. Per-entry provenance is therefore important if this pattern is used for trusted recall.

**The index is both useful and fragile.** It is the intended first read surface, but there is no deterministic rebuild or validation path in the inspected repository. A stale index would directly impair recall.

**Pattern discovery is underspecified.** `AGENTS.md` asks the agent to detect time, people, location, mood, and learning patterns, but the source does not define a recurrence threshold, evidence model, review state, or pattern invalidation policy.

## What to Watch

- Whether VLM-wiki adds a real integration command that turns raw analyses into wiki articles, updates `wiki/index.md`, appends `wiki/log.md`, and preserves source links; that would move the write path from prompt convention toward codified maintenance.
- Whether query support gains search, ranking, token budgets, or page-level retrieval modes; that would change read-back from manual/index pull toward a more engineered context surface.
- Whether pattern discovery gets an explicit evidence threshold and review workflow; without that, generated life-pattern pages should remain low-authority reflections.
- Whether multimodal outputs carry model, prompt, timestamp, raw media path, and confidence/provenance fields consistently; this determines whether VLM-derived claims can be audited.
- Whether audio transcription and video summarization become implemented rather than instructed behavior; that would broaden the acquisition surface beyond images and frame extraction.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: VLM-wiki stores a wiki, but the inspected system relies on explicit index/page reads rather than pushed memory.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: raw media, generated analyses, compiled articles, index/log files, templates, config, and scripts have different forms and authority.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: compiled wiki pages and raw analyses advise future answers as evidence/context.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: `AGENTS.md`, templates, config, trigger keywords, and scripts shape future agent behavior.
- [Frontloading spares execution context](../../../notes/frontloading-spares-execution-context.md) - relates: compiled wiki pages and indexes precompute smaller context from raw multimodal material.
- [Symbolic context engineering is bounded by symbol availability](../../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - explains: VLM-wiki's pull path depends on available symbols such as categories, titles, tags, links, and index rows.
