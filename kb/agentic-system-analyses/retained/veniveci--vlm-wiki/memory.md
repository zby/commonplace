---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "VLM-wiki memory: file-based media and wiki retention, manifest-controlled imports, deterministic review reuse and lossy delivery."
run-id: AAS-2026-10-14-vlm-wiki-311faef777b4-01
source-identity: https://github.com/veniVeci/VLM-wiki
reviewed-boundary: "503c43f98b5d1e21c74df384fdffd3e0652573b3"
---

# VLM-wiki memory report

## Boundary and evidence

The memory boundary includes the shipped importers, media preparations and model-response writers, personal and project wiki content, navigation, logs, reviews, runtime payloads, delivery and the two agent instruction files. SRC-1 is the repository and revision in [boundary](boundary.md#source-register). This report directly inspected the paths below at that revision; supplied runtime records supply the already-declared invocation identities. Source text establishes implementation or doctrine, not execution. Checked-in analyses and articles establish retained text and attributed operation, not authenticated model provenance or accuracy.

The enclosing host's instruction loader, context window, filesystem permissions and possible compaction are excluded dependencies. Provider parameters and endpoint behavior are opaque; their mutability limits remain in [RT-CMP-qwen](runtime.md#rt-cmp-qwen) and [RT-CMP-ide-model](runtime.md#rt-cmp-ide-model). Private external inputs, local overrides and ignored generated files are unavailable. No image/video pixels were audited. Those gaps prevent deployed-history, context-compliance, model-quality and benefit conclusions, not source-level tracing of the shipped readers.

| Entry point or operation | Directly inspected SRC-1 paths | Covering records and limits |
|---|---|---|
| Host compilation, related-page editing, pattern discovery and archive | `AGENTS.md`, `AGENTS.zh.md`, `references/article-template.md`, `references/archive-template.md`; sample `wiki/moments/2023-05-青岛旅行.md`, `wiki/places/五四广场.md` | [RT-RTE-agent-workflow](runtime.md#rt-rte-agent-workflow), [MEM-OBJ-wiki-articles](#mem-obj-wiki-articles). Instructions, not a repository-owned compiler; initial sample authorship unknown. |
| Host question answering and context selection | `AGENTS.md`, `AGENTS.zh.md`, `wiki/index.md` | [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), [MEM-OBJ-wiki-index](#mem-obj-wiki-index), [MEM-CLM-index-targets](#mem-clm-index-targets). Host execution and token budget uninspected. |
| Import CLI and exposed import functions | `scripts/import_data_sources.py`, `scripts/config_utils.py`, `.vlmwiki/config.json` | [RT-RTE-source-import](runtime.md#rt-rte-source-import), [MEM-OBJ-import-manifest](#mem-obj-import-manifest), [MEM-OBJ-raw-inputs](#mem-obj-raw-inputs). No private source folders or manifest supplied. |
| Qwen batch and both single-image entry points | `scripts/qwen_vlm_analyzer.py`, `scripts/run_analysis_now.py`, `scripts/single_image_demo.py` | [RT-RTE-image-analysis](runtime.md#rt-rte-image-analysis), [MEM-OBJ-analysis-reports](#mem-obj-analysis-reports). Later automatic report-to-wiki reader not established. |
| Frame extraction and metadata CLI/library operations | `scripts/video_extractor.py`, `scripts/image_analyzer.py` | [MEM-RTE-frame-extraction](#mem-rte-frame-extraction), [MEM-RTE-metadata-extraction](#mem-rte-metadata-extraction). Frame bytes not visually examined. |
| Historical review CLI and callable builder | `scripts/reflection_engine.py` | [RT-RTE-history-review](runtime.md#rt-rte-history-review), [MEM-OBJ-history-reviews](#mem-obj-history-reviews), [MEM-CLM-parser-projection](#mem-clm-parser-projection). Source reveals projection limits; no generated review supplied. |
| Work scanner, writer and cycle | `scripts/work_project_reflection.py`, `scripts/run_work_reflection_cycle.py` | [RT-RTE-work-cycle](runtime.md#rt-rte-work-cycle), [MEM-OBJ-project-pages](#mem-obj-project-pages), [MEM-OBJ-work-review](#mem-obj-work-review). External work tree unavailable. Windows-wrapper behavior is supplied runtime evidence, not a new direct read here. |
| Standalone push and cycle push | `scripts/wecom_push.py`, `README.md` lines 140 onward | [RT-RTE-work-cycle](runtime.md#rt-rte-work-cycle), [MEM-CLM-daily-delivery](#mem-clm-daily-delivery). Both HTTP modes inspected; recipient response outside boundary. |
| Runtime JSON and operational history | `scripts/reflection_engine.py`, `scripts/work_project_reflection.py`, `wiki/log.md`, `.gitignore`; manifest loader above | [MEM-OBJ-runtime-briefs](#mem-obj-runtime-briefs), [MEM-OBJ-wiki-log](#mem-obj-wiki-log). Brief readers not found in the inspected scripts; manifest has an actual reader. |
| Disclaimer repair, replacement and withdrawal limits | `scripts/update_vlm_docs.py`, all Python writers above, both agent instructions | [RT-CLM-raw-immutability](runtime.md#rt-clm-raw-immutability) and its annotation below. Repair targets `raw/vlm_analysis`, not every analysis file. No semantic withdrawal propagation established. |
| Reported media-analysis lineage | `raw/images/微信图片_20260503182120_190_41_analysis.md`, `raw/videos/2023-05-frames/frame_analysis.md` | [MEM-OBJ-analysis-reports](#mem-obj-analysis-reports). Other checked-in analyses/metadata and articles were enumerated, not reread; boundary supplies their inventory. No complete content audit claimed. |

A bounded search of `scripts/`, both AGENTS files, both READMEs and `references/` covered CLI guards, file readers/writers, manifest/brief names, deletion, hooks, evaluation and context/embedding terms. Together with direct Python reads, it exposed no additional registered-tool or hook dispatch to trace. This is a source inventory, not a negative claim about host extensions. Available uninspected supporting templates/guides and wrapper files are not access gaps; this report relies on the supplied runtime/boundary for their roles.

## Core ideas

1. **The wiki, not a vector store or conversation checkpoint, is the intended semantic memory.** The model is told to compile media into durable category articles, use the index to select them later, prefer their content over training knowledge, and archive a synthesis only on request. Their source links can preserve evidence pointers; the instructions do not require a criticism or confidence ledger. See [MEM-OBJ-wiki-articles](#mem-obj-wiki-articles) and the supplied [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query).
2. **Access metadata has a stronger implemented feedback loop than many semantic outputs.** The import manifest changes later admission by fixed fingerprint lookup. Analysis text and runtime briefs are persisted, but persistence does not establish a later consumer. See [MEM-OBJ-import-manifest](#mem-obj-import-manifest), [MEM-OBJ-analysis-reports](#mem-obj-analysis-reports) and [MEM-OBJ-runtime-briefs](#mem-obj-runtime-briefs).
3. **Deterministic reviews read retained material but do not learn their own rules.** Article/diary statistics and external work traces become recommendations under unchanged Python branches. Project pages can reach a subsequent historical review; review files themselves are outside its collector. The meaningful loop is retained evidence to a later report or human, not demonstrated improvement or recursive model reflection. See annotations on [RT-RTE-history-review](runtime.md#rt-rte-history-review) and [RT-RTE-work-cycle](runtime.md#rt-rte-work-cycle).
4. **Projection and navigation limit what survives to consumers.** Parsed article fields are not the full article, the index has targets without files, and outbound delivery is a truncated preview. The generic daily review's English preview heading is not recognized by the sender. See [MEM-CLM-parser-projection](#mem-clm-parser-projection), [MEM-CLM-index-targets](#mem-clm-index-targets) and [MEM-CLM-daily-delivery](#mem-clm-daily-delivery).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-raw-inputs
Label: Raw source media and text

Source-native identity: `raw/images/`, `raw/videos/`, `raw/audio/`, `raw/text/`, `raw/diary/`. Storage: local filesystem. Media files hold encoded perceptual inputs, not model weights or embeddings: codecs/bytes are symbolic encodings, while their depicted meaning requires model/human interpretation. Text and diary prose is natural language. These are separate consumption paths, not numerical learned state. Imported files are byte copies; the original external authors and per-file human admission decisions remain unknown. The importer admits copies automatically after configured source/fingerprint/bucket checks. A human starting import is not per-file approval. SRC-1: `scripts/import_data_sources.py`, `AGENTS.md`.

This object is distinct from the operations in [RT-RTE-source-import](runtime.md#rt-rte-source-import) and [RT-RTE-agent-workflow](runtime.md#rt-rte-agent-workflow): it is their retained input/output substrate. No supplied operative-object counterpart exists. Later readers are direct image drivers, frame/metadata tools, the documented host and, specifically for direct diary Markdown, the historical-review collector. Text imports under month directories have no corresponding implemented semantic compiler here; imported `.txt` diaries are not collected by the `.md` review glob. Media is delivered as an image to the provider, not promoted into an executable instruction. Human/host interpretation of text remains outside enforced trust isolation. Source immutability is the policy bounded by [RT-CLM-raw-immutability](runtime.md#rt-clm-raw-immutability).

> shutil.copy2(source_file, target_path)
> --- `scripts/import_data_sources.py`

> for path in sorted(diary_dir.glob("*.md")):
> --- `scripts/reflection_engine.py`

#### MEM-OBJ-import-manifest
Label: Import admission manifest

Source-native identity: `.vlmwiki/runtime/import_manifest.json`; symbolic JSON on disk. Lineage: code records source name/path, target path, bucket and import time keyed by a SHA-1 of resolved source path, byte size and integer mtime. This is access/admission metadata, not retained source meaning or a content digest. Physical write and admission are Python-controlled; initial absent state becomes an empty `files` mapping, and later invocation reloads it. The fingerprint, not the retained explanatory fields, governs skipping. No per-file reviewer, semantic oracle, automatic expiry or target-existence repair appears in this importer. A deleted target can still be skipped while its key remains; metadata-preserving source changes can also be skipped. SRC-1: `scripts/import_data_sources.py`.

Distinct from [RT-OBJ-config](runtime.md#rt-obj-config), which selects source policy, and from [RT-RTE-source-import](runtime.md#rt-rte-source-import), which operates on the manifest. It is not a duplicate declaration of that route. The runtime record supplies the fingerprint quote. Copying occurs before the eventual manifest save, so crash recovery can create unmatched copies rather than transactional rollback.

> if fingerprint in files_state:
>     skipped += 1
>     continue
> --- `scripts/import_data_sources.py`

#### MEM-OBJ-analysis-reports
Label: Natural-language media analysis reports

Source-native identity: batch `raw/qwen_vlm_results/vlm_result_*.md`, single-image `*_qwen_analysis.md`, checked-in `raw/images/*_analysis.md` and `raw/videos/2023-05-frames/frame_analysis.md`. Storage: Markdown files. Form: natural-language descriptions, mood and tags, with symbolic path/time wrappers. The first two forms are automatically admitted provider-response text, without response review, quality evaluation or factual veto. Same-name reruns replace them. Checked-in reports attribute a different model; their exact producing invocation and admission control are unknown. Do not backfill Qwen provenance from the shipped driver. SRC-1: `scripts/qwen_vlm_analyzer.py`, `scripts/run_analysis_now.py`, `scripts/single_image_demo.py`, `raw/images/微信图片_20260503182120_190_41_analysis.md`, `raw/videos/2023-05-frames/frame_analysis.md`.

Distinct retained outputs of [RT-RTE-image-analysis](runtime.md#rt-rte-image-analysis), not another route. No supplied object counterpart. They are derived semantic accounts, not raw visual evidence or internal model reasoning. The inspected drivers provide no later report-reader/compiler. Documented host compilation affords media-to-wiki work, but does not establish that this batch-output directory is consumed. The disclaimer helper has yet another target directory and patterns; it cannot be assumed to repair these reports. See the annotation on [RT-CLM-raw-immutability](runtime.md#rt-clm-raw-immutability).

> **分析模型**: 豆包多模态模型
> --- `raw/images/微信图片_20260503182120_190_41_analysis.md`

The source supports the attribution string, not its authenticity. Provider model identity/fixity remains [RT-CMP-qwen](runtime.md#rt-cmp-qwen).

#### MEM-OBJ-frame-images
Label: Extracted video frame files

Source-native identity: `raw/videos/2023-05-frames/frame_*.jpg` in the CLI example; callable extraction accepts another output directory. Storage: local JPEG files. Form: symbolic image encoding with perceptual meaning interpreted by later humans/models. Lineage: evenly indexed source-video frames, not a semantic summary or transcript. The code admits each successfully decoded frame and writes it without human per-frame review; existing matching filenames can be replaced, and old nonmatching frames are not pruned. Later PIL metadata inspection is wired in [MEM-RTE-metadata-extraction](#mem-rte-metadata-extraction); host semantic use is only documented. SRC-1: `scripts/video_extractor.py`, `scripts/image_analyzer.py`, `AGENTS.md`.

Compared with [RT-RTE-image-analysis](runtime.md#rt-rte-image-analysis), these are the supporting extractor's durable outputs, not provider-response text. No supplied object counterpart. The distinct producing route is [MEM-RTE-frame-extraction](#mem-rte-frame-extraction).

#### MEM-OBJ-analysis-results
Label: Media metadata and batch status

Source-native identities: `raw/analysis_results.json` and Qwen batch `summary.json`. Both are symbolic JSON on local disk, but their consumers and derivations differ. The first records PIL dimensions/format/mode/size, paths and errors, with a hardcoded timestamp; it is derived physical metadata, not visual understanding. The second records image/output paths and success/error status; success means driver completion, not semantic validity. Both are admitted by code, overwritten on rerun, and have no later reader established in the inspected scripts. They therefore establish retention capability, not an additional read-back route. SRC-1: `scripts/image_analyzer.py`, `scripts/qwen_vlm_analyzer.py`.

No supplied object counterpart: [RT-RTE-image-analysis](runtime.md#rt-rte-image-analysis) mentions these outputs but denotes the operation. These two metadata parts are kept distinct here from the natural-language payload in [MEM-OBJ-analysis-reports](#mem-obj-analysis-reports). Neither is opaque model state.

> "timestamp": "2026-05-03",
> --- `scripts/image_analyzer.py`

#### MEM-OBJ-wiki-articles
Label: Personal category articles and archives

Source-native identity: Markdown in `wiki/moments/`, `wiki/people/`, `wiki/places/`, `wiki/concepts/`, `wiki/patterns/`, `wiki/archives/`. Storage: local files. Article body, captions and summaries are natural-language knowledge. Path/link/date/type/tag units are symbolic metadata when used by the Python parser; the host also interprets the same text semantically. Templates retain media pointers, related articles and sources, while the archive template additionally retains context and reflections. These are evidence pointers and authored conclusions, not guaranteed preserved derivation, criticism or complete transcript. SRC-1: `AGENTS.md`, `AGENTS.zh.md`, `references/article-template.md`, `references/archive-template.md`, `wiki/moments/2023-05-青岛旅行.md`.

No supplied object counterpart; these are the knowledge products/read inputs of [RT-RTE-agent-workflow](runtime.md#rt-rte-agent-workflow) and [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query). The requested writer/curator is the host model, with file I/O by its tools. User initiation and an archive request specify the task, not per-claim human admission. Historical checked-in authorship/control remains unknown. Later consumers: host query as preferred evidence, Python historical review as parsed fields, and humans via Markdown editors. The query convention grants epistemic preference, not executable policy authority or correctness. Archives remain eligible for Python collection; a transient answer does not become retained memory until separately saved.

> ## Sources
> 
> {{sources_raw_links}}
> --- `references/article-template.md`

> ## Context
> 
> {{context_and_background}}
> --- `references/archive-template.md`

#### MEM-OBJ-project-pages
Label: Generated project articles

Source-native identity: `wiki/projects/<slug>.md`. Storage: local Markdown, ignored by Git. Natural-language descriptions/previews and symbolic dates/links/paths are distinct operative parts. Python derives summaries from recent file counts/extensions/filenames and Git metadata, and copies short text previews. It admits pages directly, with no model and no per-page human review. Same-slug writes replace complete files, including any manual additions; projects absent from a later scan are not deleted. SRC-1: `scripts/work_project_reflection.py`, `.gitignore`.

Distinct from the personal host-authored articles above and the operation [RT-RTE-work-cycle](runtime.md#rt-rte-work-cycle); no supplied object counterpart. These are derived external activity records, not the system's own execution-learning rules. Their later consumers are the wired historical-review collector and intended index-led host queries. The former takes parsed fields rather than file previews/body; the latter may read the full page. Source paths and Git clues preserve some lineage, but generated interpretations such as fixed topical claims are not evidence-validated. The writer does not read the previous page before replacing it.

> path = PROJECTS_DIR / f"{slug}.md"
> --- `scripts/work_project_reflection.py`

#### MEM-OBJ-wiki-index
Label: Global article index

Source-native identity: `wiki/index.md`; local Markdown table with category headings, links and natural-language summaries. It is human/model navigation, not an enforced relational index. Host authoring is instructed to update it, while the work producer deterministically replaces only the Projects section. Initialization and historical per-row admission are unknown. The host is told to select relevant articles from it; Python historical review instead enumerates directories directly. SRC-1: `AGENTS.md`, `wiki/index.md`, `scripts/work_project_reflection.py`, `scripts/reflection_engine.py`.

Distinct selector input of [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query), with no supplied object counterpart. The index's summaries are not a complete compressed replacement for article bodies; the query asks for a second read. It can become stale or point to absent pages; see [MEM-CLM-index-targets](#mem-clm-index-targets). Work-index replacement neither withdraws old project files from the review collector nor proves index-to-file consistency.

#### MEM-OBJ-wiki-log
Label: Operation log and local task logs

Source-native identity: `wiki/log.md`, plus the Windows wrapper's local execution log described by [RT-RTE-work-cycle](runtime.md#rt-rte-work-cycle). Storage: text files. Form: natural-language event descriptions with symbolic dates and links. Wiki history is intended append-only; Python append functions physically reread and replace the file. They record generated paths and scan/review events, not complete source snapshots, model reasoning or user-outcome feedback. Existing entries report operation without authenticating execution. SRC-1: `wiki/log.md`, `scripts/reflection_engine.py`, `scripts/work_project_reflection.py`.

No supplied object counterpart. Neither the wiki log nor wrapper log is a read-back input to the inspected semantic generators. No trace-to-policy transformation follows from their existence. The manifest differs: its retained operational metadata actually changes later importer decisions. Runtime supplies wrapper behavior; that local log was not directly inspected here.

#### MEM-OBJ-history-reviews
Label: Daily and weekly review Markdown

Source-native identity: `wiki/reviews/YYYY-MM-DD-daily.md` and `wiki/reviews/YYYY-MM-DD-weekly.md`; local Markdown, ignored by Git. Natural-language snapshots, fixed interpretations and up to four recommendations are rendered with symbolic frontmatter and a short delivery preview. Lineage: parsed category articles plus direct diary Markdown, not prior reviews or model conversational traces. Python automatically authors and admits them under unchanged rules; same-date reruns replace files. No per-recommendation review, expected-answer oracle or retained user-outcome check appears. SRC-1: `scripts/reflection_engine.py`, `.gitignore`.

Distinct outputs of [RT-RTE-history-review](runtime.md#rt-rte-history-review), not a duplicate route; no supplied object counterpart. Consumers: humans and the documented standalone sender in `README.md`. The engine excludes `reviews` from its article collection and does not update the index with these files. A later model-query route to them is therefore not established merely by placing them under `wiki/`. The sender's actual projection differs from the embedded preview; see [MEM-CLM-daily-delivery](#mem-clm-daily-delivery). Reviews retain counts, snippets and recommendations, not complete original evidence or reasons for each inference.

#### MEM-OBJ-work-review
Label: Work review and outbound preview

Source-native identity: configured `wiki/reviews/work-project-review.md` by default. Storage: local Markdown. Form: natural-language activity interpretations and next steps, symbolic frontmatter, and a dedicated Chinese-heading message preview. Lineage: external files/Git selection in the current scan. Python authors and admits it directly; fixed-name reruns replace it. It is distinct from historical reviews because the producer, input selection, replacement horizon and shipped push wiring differ. It is the retained output read by the sender within [RT-RTE-work-cycle](runtime.md#rt-rte-work-cycle); no supplied object counterpart. SRC-1: `scripts/work_project_reflection.py`, `scripts/run_work_reflection_cycle.py`, `scripts/wecom_push.py`.

The sender reloads the file, takes at most twenty nonempty preview lines, then each HTTP mode takes at most 4,000 characters. WeCom recipients receive that selected text, not full project pages, raw files, Git history or the JSON payload. This is an automatic push after explicit cycle invocation; recurrence still depends on an external scheduler. Its authority is human-facing recommendation, not a later model instruction or software update. No delivered/acted-on outcome is observed.

#### MEM-OBJ-runtime-briefs
Label: Latest historical and work briefs

Source-native identities: `.vlmwiki/runtime/latest_brief.json` and `.vlmwiki/runtime/latest_work_brief.json`. Storage: local ignored JSON files. Their structure is symbolic; insights/recommendations and file previews are natural-language payloads. The historical brief retains date, generated time, insights and recommendations. The work brief additionally retains a review path and up to eight activity records, each with file previews. Both are code-admitted derived state, replaced on generation. SRC-1: `scripts/reflection_engine.py`, `scripts/work_project_reflection.py`, `.gitignore`.

Distinct from [RT-OBJ-config](runtime.md#rt-obj-config) and from the two producing runtime routes; no supplied object counterpart. Their names do not establish a model context checkpoint or retrieval service. Direct reads and the bounded name search found writers, not a later brief consumer, in the shipped scripts. Retention is implemented; cross-invocation behavioral authority through these payloads remains unestablished. The disk review, not this JSON, is passed to WeCom. Initial private instances and their actual revision history are unavailable; known later overwrite behavior is still inspectable.

### Routes

#### MEM-RTE-frame-extraction
Label: Video frame extraction

User/caller supplies video, output directory and count; the CLI supplies fixed example paths and the default five frames. OpenCV decodes evenly spaced indices and Python writes successful frames to disk. Code selects and admits each frame, with no semantic oracle, scene-change evaluator or per-frame approval. Fixed arithmetic is the guidance; failure to open returns `None`, decode failures are skipped, and manual cleanup/rerun is recovery. This is a distinct preparation operation discussed but not separately declared in [RT-RTE-image-analysis](runtime.md#rt-rte-image-analysis). SRC-1: `scripts/video_extractor.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Metadata dictionary with video path, frame count, FPS, duration and extracted paths; JPEG files and console output.
- Later read-back: The separate metadata executable reads the example frame directory; the host's video-ingest instructions request later visual interpretation.
- Delegated visibility: inapplicable — local decoder and filesystem writes, not delegated model work.
- Selection predicate: Evenly spaced indices across total frames, retaining only successfully decoded frames; caller controls count.
- Invalidation or expiry: Matching filenames can be replaced; no stale-frame cleanup or semantic invalidation in this script.
- Activation or effect: Source wires durable frame production and a later metadata-reader path; successful execution and semantic use are unobserved.
- Evidence limits: No pixel audit or execution; no transcription or scene-change selection is implemented by this extractor.

> frame_indices = [int(i * (total_frames - 1) / (num_frames - 1)) for i in range(num_frames)]
> --- `scripts/video_extractor.py`

#### MEM-RTE-metadata-extraction
Label: Image metadata extraction

CLI scans immediate raw images and, if present, the fixed example frame directory. PIL extracts dimensions/format/mode and Python obtains file size; errors become metadata entries. Code admits and writes the resulting JSON without a content reviewer or expected-answer oracle. This is a separate producer from the model route [RT-RTE-image-analysis](runtime.md#rt-rte-image-analysis); its output is [MEM-OBJ-analysis-results](#mem-obj-analysis-results). Fixed file rules guide an open folder scan; errors are retained rather than semantically rejected, and rerun/manual repair is recovery. SRC-1: `scripts/image_analyzer.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Functions return metadata dictionaries/lists; CLI writes `raw/analysis_results.json` and prints details.
- Later read-back: Reads previously retained images/frames; later use of its generated JSON is uninspected — no reader is shown in the inspected script set.
- Delegated visibility: inapplicable — local PIL/file inspection, not model delegation.
- Selection predicate: Immediate-directory files with supported image suffixes; optional fixed frame directory, not recursive month-folder selection.
- Invalidation or expiry: Same JSON replaced on rerun; no per-record invalidation or pruning beyond rebuilding the selected result list.
- Activation or effect: Metadata-dependent durable output is wired, not observed semantic understanding or decision improvement.
- Evidence limits: Physical properties are not captions, EXIF interpretation, factual evaluation or a report-to-wiki compiler.

> "size": (width, height),
> "format": format,
> "mode": mode,
> "filesize": image_path.stat().st_size
> --- `scripts/image_analyzer.py`

### Claims

#### MEM-CLM-parser-projection
Label: Historical review consumes a lossy projection

The review parser does not behave as a full YAML reader. Its generic colon branch runs before the media-continuation branch, so `src:` and `caption:` become top-level values and clear `current_key`; subsequent media list items need not remain in `media`. The example multi-image moment article therefore cannot be assumed to contribute its full media list/count. Its month-only `date: 2023-05` also fails the `%Y-%m-%d` parser used for latest-record selection. These are source-level consequences, not observed output measurements. SRC-1: `scripts/reflection_engine.py`, `wiki/moments/2023-05-青岛旅行.md`.

This qualifies the generic simple-parser account in [RT-RTE-history-review](runtime.md#rt-rte-history-review); it is a distinct claim, not another review route. Article body is stored in `ArticleRecord` but not semantically summarized by the output builder. The builder uses counts, tags, related links, latest title/summary and exact repeated diary lines. It does not consume the article's explanations or validate their truth. The hardcoded travel-related link and fixed travel bias interpretation likewise need not derive from the selected corpus.

> if ":" in stripped and not stripped.startswith("- "):
>     key, value = stripped.split(":", 1)
> --- `scripts/reflection_engine.py`

> if value:
>     data[key] = value
>     current_key = None
> --- `scripts/reflection_engine.py`

> return datetime.strptime(value, "%Y-%m-%d").date()
> --- `scripts/reflection_engine.py`

> date: 2023-05
> --- `wiki/moments/2023-05-青岛旅行.md`

#### MEM-CLM-index-targets
Label: Index navigation does not guarantee target retention

The index lists `[[Places/青岛]]`, `[[Places/海水浴场]]`, `[[Places/琴屿路]]` and `[[Places/信号山]]`, but the frozen tracked `wiki/places/` contains only three different pages: 五四广场, 小青岛 and 海博馆. The boundary inventory plus the directly checked tracked tree establishes missing retained targets at this commit, not deletion history. SRC-1: `wiki/index.md`. This limits the index-first retrieval affordance in [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query); it is not evidence that all host queries fail.

The project writer additionally names files using `slugify(activity.name)` but constructs index links from the original `activity.name`. For names changed by slugification, link-to-file agreement is not ensured. This is a source-level conditional mismatch, not an observed configured project name. SRC-1: `scripts/work_project_reflection.py`. Distinct from the operation [RT-RTE-work-cycle](runtime.md#rt-rte-work-cycle), with no supplied claim counterpart.

> | [[Places/青岛]] | 海滨城市, 山东, 旅行目的地 | 山东省的海滨城市，以美丽的海景闻名 | 2026-05-03 |
> --- `wiki/index.md`

> slug = slugify(activity.name)
> path = PROJECTS_DIR / f"{slug}.md"
> --- `scripts/work_project_reflection.py`

> f"| [[Projects/{activity.name}]] | active | {summary} | {activity.last_activity.date().isoformat()} |"
> --- `scripts/work_project_reflection.py`

#### MEM-CLM-daily-delivery
Label: Standalone daily-review delivery omits its intended preview

`README.md` explicitly affords sending the daily file with the same sender used by the work cycle. The daily/weekly renderer emits `## Delivery Preview`, whereas the sender recognizes only `## 企业微信消息预览`. Thus the historical file takes the first-twenty-nonempty-lines fallback, starting with frontmatter, rather than selecting its embedded recommendation preview. Both HTTP modes then truncate to 4,000 characters. This bounds what the documented external recipient receives; it is not evidence of a failed service call. SRC-1: `README.md`, `scripts/reflection_engine.py`, `scripts/wecom_push.py`.

The work-cycle selection quote is already retained by [RT-RTE-work-cycle](runtime.md#rt-rte-work-cycle); this claim covers the additional historical-review input, not a duplicate of that route. The full on-disk historical review still retains recommendations, and manual file access is unaffected.

> python scripts/wecom_push.py wiki/reviews/2026-06-30-daily.md
> --- `README.md`

> "## Delivery Preview",
> --- `scripts/reflection_engine.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-source-import](runtime.md#rt-rte-source-import)

Retained control is [MEM-OBJ-import-manifest](#mem-obj-import-manifest), separate from copied [MEM-OBJ-raw-inputs](#mem-obj-raw-inputs). Later import automatically loads the manifest and tests membership on each current candidate's metadata fingerprint. No model interprets it; symbolic membership has executable admission authority across invocations. Human source configuration is distinct from code admission of individual files. A target deletion does not remove its manifest key. Config disablement prevents future scanning, not withdrawal of already copied content. SRC-1: `scripts/import_data_sources.py`; supplied route carries copy/fingerprint quotations.

#### On [RT-RTE-agent-workflow](runtime.md#rt-rte-agent-workflow)

Natural-language semantic curation is requested: extracting people/places/activities, updating related categories and patterns, and saving a requested synthesis with index/log updates. The retained products are [MEM-OBJ-wiki-articles](#mem-obj-wiki-articles), [MEM-OBJ-wiki-index](#mem-obj-wiki-index) and [MEM-OBJ-wiki-log](#mem-obj-wiki-log). These operations can reshape authored meaning, unlike byte-copy import. They have no repository-owned per-content approval gate or implemented source-quality evaluation. Initial example authorship is unknown; known future requested model authorship does not settle it. SRC-1: `AGENTS.md`, `AGENTS.zh.md`, `references/article-template.md`, `references/archive-template.md`.

The raw-to-derived-to-consumer chain is media/text to compiled article/archive to later query. Templates preserve source links and optional context/reflections, not necessarily the model's reasons. The later query requests articles, not a separate reasoning log. Automatic pattern detection is a requested behavior, not an implemented trace-fed parameter or instruction update. Source content is read as evidence under a convention; neither escaping untrusted content nor host enforcement is specified by these files.

#### On [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query)

Read-back is a user-question pull: host/model reads index, selects relevant articles, then reads them and answers with internal links. Selector inputs are question and index summaries; selected content is article text. Delivery is host file/tool reading into model context. No top-k, token budget, ranking algorithm or automatic push to the model is implemented here. Retained article preference is requested epistemic authority, contingent on host loading/compliance. The full article remains on disk after the session; query persistence requires the separate archive request. SRC-1: `AGENTS.md`, `AGENTS.zh.md`; the supplied route retains the query passage. [MEM-CLM-index-targets](#mem-clm-index-targets) bounds navigation completeness.

Working-context control here is selective external-file loading, not conversation compaction. The initial index is a small navigation surface, not a guaranteed budgeted summary. No task-frame isolation, eviction policy, preserved verbatim tail, checkpoint alternative or removed-content reload mechanism is specified by these instructions; host internals remain uninspected rather than absent. Reading a link requires another actual file read; a pointer is not resident article content.

#### On [RT-RTE-image-analysis](runtime.md#rt-rte-image-analysis)

Each model request has one base64 image plus fixed text, with no wiki, prior image analyses or accumulated conversation supplied by the driver. The per-image context does not carry prior responses forward. It resembles isolated requests only in that selected input is sent and response text escapes; it is not host subagent delegation or a popped conversation frame. Durable [MEM-OBJ-analysis-reports](#mem-obj-analysis-reports) and batch metadata are written without semantic approval; actual provider context management is opaque. Source model/fixity fields remain with [RT-CMP-qwen](runtime.md#rt-cmp-qwen). SRC-1: `scripts/qwen_vlm_analyzer.py`, `scripts/run_analysis_now.py`, `scripts/single_image_demo.py`; supplied route retains request/output evidence.

The immediate return is provider text, distinct from proof of later reuse. Batch output filenames differ from checked-in analysis names, and the sample attributes 豆包 rather than Qwen. Neither sample presence nor provider-request code supplies the missing authentic lineage or later report-to-wiki consumer. Batch directory selection also excludes importer month subdirectories, as the supplied runtime already notes.

#### On [RT-RTE-history-review](runtime.md#rt-rte-history-review)

Retained read-back inputs are direct Markdown files across seven category directories, including archives/projects, plus direct `raw/diary/*.md`. Selection is exhaustive within those globs, not relevance-targeted or daily/weekly date-window retrieval. Both labels operate over the same corpus; dates affect latest-record/recommendation branches. The body and parsed fields exist in memory, but the output uses metadata counters/latest summary and exact diary-line repetition, not semantic reasoning over every body. [MEM-CLM-parser-projection](#mem-clm-parser-projection) limits even that projection. SRC-1: `scripts/reflection_engine.py`.

> for subdir in ("moments", "people", "places", "projects", "concepts", "patterns", "archives"):
> --- `scripts/reflection_engine.py`

> return recommendations[:4]
> --- `scripts/reflection_engine.py`

Trace-fed transformation is retained article/diary history to fixed-rule [MEM-OBJ-history-reviews](#mem-obj-history-reviews) and [MEM-OBJ-runtime-briefs](#mem-obj-runtime-briefs). Diary origin is external personal text; wiki origin is mixed/partly unknown, and generated project pages add external work traces. Code writes guidance for a human, not an updated executable rule or model weight. A later standalone sender is documented, but review-to-next-engine-input recursion is not wired by the category enumeration. The briefs lack an established reader. Output recommendations may explain their branch informally, but no input/outcome criticism record or subsequent rule adaptation is retained here. No capacity improvement follows merely from the name reflection.

#### On [RT-RTE-work-cycle](runtime.md#rt-rte-work-cycle)

The durable handoff is [MEM-OBJ-work-review](#mem-obj-work-review) to the separately invoked sender, selected by file path. The automatic selector then strips blank/fence lines, selects the Chinese preview when present, limits twenty lines, and the HTTP constructor caps 4,000 characters. Recipients receive a human-facing digest; no model consumes this push. The default activity selection budgets are twelve projects/eight files per project; previews are first two nonempty text lines capped at 180 characters, with Git history up to three commits. These are deterministic reporting budgets, not a model context window. SRC-1: `.vlmwiki/config.json`, `scripts/work_project_reflection.py`, `scripts/wecom_push.py`; supplied route carries sender and sequence passages.

[MEM-OBJ-project-pages](#mem-obj-project-pages) are eligible for a subsequent historical-review invocation whether or not still in the updated index. File previews and Git lines retained in the page are not subsequently consumed by that engine's summary builder. The latest work JSON retains up to eight activity records, but there is no established JSON reader. A rerun scans external current files rather than adapting to its own review/log or previous recommendations. Edits to generated pages can be overwritten on rerun. Index replacement does not delete stale project pages; failure after index/page writes does not roll them back. SRC-1: `scripts/work_project_reflection.py`, `scripts/reflection_engine.py`.

#### On [RT-CLM-raw-immutability](runtime.md#rt-clm-raw-immutability)

The disclaimer maintenance operation targets only `raw/vlm_analysis/image_*.md` and `video_frame_*.md`. It reads and prefixes a simulation warning when the marker is absent, then performs two textual replacements. Python admits that fixed rewrite automatically; a caller choosing to run it is not a per-file factual adjudicator. No answer oracle or rollback is supplied. Its semantic effect is source-trust qualification, not a demonstrated global cleanup of Qwen results, checked-in image reports, frame analysis or wiki derivatives. A later reader of a rewritten document can encounter the warning, but no automatic propagation into already compiled articles or retraction of dependent claims is shown. SRC-1: `scripts/update_vlm_docs.py`.

> vlm_dir = Path(__file__).parent / "../raw/vlm_analysis"
> --- `scripts/update_vlm_docs.py`

> patterns = ["image_*.md", "video_frame_*.md"]
> --- `scripts/update_vlm_docs.py`

> **注意**: 此文档内容是为了演示目的而创建的模拟分析，不是真实调用 qwen3.5-omni-flash 模型的结果。
> --- `scripts/update_vlm_docs.py`

## Write side

Admission has several owners, not one wiki-wide curator. Import configuration determines eligible sources, and Python admits unseen metadata fingerprints into copies plus a manifest. It does not judge source meaning. The image models author descriptions; Python admits their returned text. Host-mediated compilation instead delegates semantic selection and related-page edits to an external model under conventions. Historical example initialization remains unknown for both prose and index rows. The two review engines author/admit their own rule-generated recommendations; a human can change configuration or later edit files, but source text does not establish human approval of each generated claim. SRC-1: `scripts/import_data_sources.py`, `scripts/qwen_vlm_analyzer.py`, `AGENTS.md`, `scripts/reflection_engine.py`, `scripts/work_project_reflection.py`; corresponding records and annotations above retain the evidence.

Rejection is local: disabled sources, duplicate keys or unmapped buckets prevent import; API errors create batch failure entries; feature disablement prevents the history-review CLI; notification settings gate transmission, not local retention or truth. Exposed builders/functions are not all subject to their CLI's confirmation/feature checks. A callable image analyzer has no batch confirmation; `build_reviews` does not itself load the feature gate. No expected-answer evaluation is provided by these admission mechanisms. Runtime already distinguishes CLI initiation from per-response approval. SRC-1: `scripts/import_data_sources.py`, `scripts/qwen_vlm_analyzer.py`, `scripts/reflection_engine.py`, `scripts/wecom_push.py`.

Maintenance is mostly replacement, not accumulated criticism: same-name analyses, generated project pages, configured work review and latest briefs are overwritten; dated reviews are replaced for that date; log entries are retained by read-and-rewrite append. The known disclaimer rewrite changes the trust label of selected raw-derived reports. There is no established dependency-aware withdrawal route from that edit, source deletion or index replacement to all derived wiki/review claims. The manifest can retain a skip decision after deletion of its copy; stale project files can survive losing their index row. These are limits of the inspected writers/readers, not claims about every manual host operation. SRC-1: `scripts/update_vlm_docs.py`, `scripts/import_data_sources.py`, `scripts/work_project_reflection.py`, `scripts/reflection_engine.py`.

Raw-to-derived paths remain separate: video to selected JPEGs to physical metadata; image to provider prose/status; external project traces to pages/review/brief; article/diary history to historical review/brief; and instructed media-to-wiki compilation. Only traced later consumers support read-back. None of the generated JSON payloads is a demonstrated conversation checkpoint, and no alternative opaque checkpoint format was encountered in the inspected scripts. Static prompts/configuration shape proposals but are not themselves experience-derived memory. Model parameter updates remain provider-internal and uninspected. No trace-to-rule, trace-to-weight or review-driven self-revision follows from these transformations.

## Read-back

- **Question-driven semantic pull:** a host reads index then relevant retained articles; natural-language preference and citation instructions govern the answer. Selection budget and compliance are unknown. See the query annotation and [MEM-CLM-index-targets](#mem-clm-index-targets).
- **Importer pull on a later invocation:** current file candidates are filtered against a retained manifest; fixed symbolic membership changes admission. It reads metadata, not the semantic content of earlier copies. See [MEM-OBJ-import-manifest](#mem-obj-import-manifest).
- **Historical report generation:** a new CLI/builder invocation rereads category files/diaries and automatically chooses statistical branches; it emits a review for a human rather than supplying unsolicited context to a model. It does not read prior reviews/logs/briefs. See the history annotation and [MEM-CLM-parser-projection](#mem-clm-parser-projection).
- **Work-cycle push:** the cycle produces a retained file, starts the sender with its path, and code selects/truncates the preview for a configured WeCom recipient. It is producer-initiated delivery after invocation, not query-driven retrieval. Standalone sender use can read a file from an earlier invocation. External scheduling and recipient action remain unobserved. See the work annotation and [MEM-CLM-daily-delivery](#mem-clm-daily-delivery).
- **Preparation reuse:** metadata extraction rereads retained frame JPEGs; this is a shipped file-to-file pipeline, not model retrieval. See [MEM-RTE-frame-extraction](#mem-rte-frame-extraction) and [MEM-RTE-metadata-extraction](#mem-rte-metadata-extraction).
- **Storage without established consumer:** raw analysis prose, batch/physical metadata JSON, runtime briefs and logs have writers, but their mere presence supplies no new semantic reuse or feedback route. A human can browse Markdown, as `README.md` documents, without establishing deployed use or automatic activation.

## Integration issues

1. **Projection qualification, not route replacement:** [MEM-CLM-parser-projection](#mem-clm-parser-projection) narrows the simple-parser/count account of [RT-RTE-history-review](runtime.md#rt-rte-history-review). Media continuations, month-only dates and unused bodies prevent treating its report as a faithful full-corpus synthesis. Evidence and consequences are retained in the claim; runtime's generic route identity remains valid.
2. **Additional documented sender input:** [MEM-CLM-daily-delivery](#mem-clm-daily-delivery) adds the README's daily-review invocation to the work-route sender account. English preview selection is not wired, so reconciliation must not equate all outbound delivery with the producer's intended preview. The daily output's consumer is afforded by documentation; no deployed delivery is established.
3. **Navigation consistency:** [MEM-CLM-index-targets](#mem-clm-index-targets) qualifies [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) and [RT-RTE-work-cycle](runtime.md#rt-rte-work-cycle). Existing missing page targets and conditional slug/link mismatches prevent claiming complete index discoverability. The direct history collector can still read surviving stale pages independently.
4. **Unknown initialization and report lineage:** [MEM-OBJ-analysis-reports](#mem-obj-analysis-reports), [MEM-OBJ-wiki-articles](#mem-obj-wiki-articles) and [MEM-OBJ-wiki-index](#mem-obj-wiki-index) retain unknown original admission/authoring. Checked-in attribution differs from shipped Qwen calls; do not assign its outputs authenticated Qwen provenance. Missing actual host/provider traces prevents settling that history.
5. **No established reader for latest briefs:** [MEM-OBJ-runtime-briefs](#mem-obj-runtime-briefs) remains storage capability rather than model read-back. The manifest's executable reuse and the disk-review-to-sender route must not be generalized to all runtime JSON.
6. **Limited trust repair:** the annotation on [RT-CLM-raw-immutability](runtime.md#rt-clm-raw-immutability) scopes disclaimer replacement to its actual patterns/directory; whether private matching files existed and whether anyone consumed the warning are unknown. It does not establish global rejection or withdrawal of derived claims.

No new declaration is a possible duplicate of a supplied referent after comparison. The new operative objects are retained inputs/products of supplied operations, not replacements for those route identities; the two new preparation routes were only supporting prose in runtime. Claims refine distinct consequences. These comparisons and the supplied closest records are stated beside the declarations. No peer epistemic/workflow fragments were supplied, so possible cross-specialist duplicates remain for reconciliation rather than inferred here.

## Limitations and checks

The analysis is source-only. No target code, tests, model requests or external services were executed. Supplied runtime and boundary evidence was read in full; this report rechecked source HEAD as `503c43f98b5d1e21c74df384fdffd3e0652573b3`, enumerated the tracked tree and checked the source checkout's clean status. Direct source inspection and bounded searching added no source identity or evidence tier. It established implemented paths and documented affordances, not activation, accurate personal memory, real scheduler recurrence, successful delivery or improved future capacity.

Host context isolation/compaction, provider parameter lineage, ignored runtime/generated files, private override values and external source trees remain uninspected or unavailable as specified above. Source-linked reasons in templates are affordances, not proof of retained rationale for every derived claim. Media pixels and unselected sample texts were not audited; article/report truth remains outside this report's conclusions.

Deterministic validation: the supplied `commonplace-run validate-output` command passed with “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” This is a deterministic content-check result, not evidence of semantic correctness, operation or acceptance.
