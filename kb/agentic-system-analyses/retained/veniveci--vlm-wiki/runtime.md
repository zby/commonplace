---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "VLM-wiki runtime baseline: host-mediated compilation and query, direct image calls, deterministic reviews, import and delivery."
run-id: AAS-2026-10-14-vlm-wiki-311faef777b4-01
reviewed-boundary: "503c43f98b5d1e21c74df384fdffd3e0652573b3"
---

# VLM-wiki runtime report

## Runtime account

VLM-wiki combines model-facing procedures with standalone Python producers and consumers. It does not make every claimed workflow a repository-owned model loop. The ordinary authoring invocation begins when a person adds media and asks an enclosing AI host to analyse it. The host supplies model execution and file tools; the shipped instructions ask that model to extract information, write category articles and maintain related state. Later questions are supposed to read the index and selected articles before answering. This is an instruction-level path, not evidence that any particular host follows it. See [RT-RTE-agent-workflow](#rt-rte-agent-workflow) and [RT-RTE-wiki-query](#rt-rte-wiki-query). SRC-1: `AGENTS.md`, `README.md`.

The implemented image route is narrower: a direct OpenAI-compatible request sends one image and a fixed Chinese analysis prompt to a named Qwen endpoint, receives text, and persists it. It does not itself compile wiki articles. These drivers bypass the advertised general model configuration and host fallback; their distinct endpoint and key behavior matter to any account of privacy, permission or model selection. See [RT-RTE-image-analysis](#rt-rte-image-analysis) and [RT-CMP-qwen](#rt-cmp-qwen). SRC-1: `scripts/qwen_vlm_analyzer.py`, `scripts/run_analysis_now.py`, `scripts/single_image_demo.py`.

An ordinary executable work-review invocation runs the cycle driver from Python or the Windows wrapper. Code loads base/local configuration, chooses one timestamp, launches the work scanner, then optionally launches delivery. The scanner reads configured external project files and Git metadata, selects recent activity, directly writes project pages, replaces the index Projects section, writes a review/runtime JSON and appends a log entry. Delivery rereads the review from disk, selects its message preview or first twenty nonempty lines, then sends at most 4,000 characters. The producer and consumer are shipped paths inside the boundary; the work tree, Python installation and WeCom service are dependencies. See [RT-RTE-work-cycle](#rt-rte-work-cycle). SRC-1: `scripts/run_work_reflection_cycle.py`, `scripts/work_project_reflection.py`, `scripts/wecom_push.py`.

The separate daily/weekly engine is deterministic too. Its recommendations are code branches over article counts, dates, tags and diary lines. Both review types use the collected corpus; their names do not establish different temporal windows or a model's reflection. See [RT-RTE-history-review](#rt-rte-history-review). Import is another independent invocation, not an automatic compiler trigger: it copies source files and writes a manifest for subsequent deduplication. See [RT-RTE-source-import](#rt-rte-source-import). SRC-1: `scripts/reflection_engine.py`, `scripts/import_data_sources.py`.

### Control boundaries and forcing cases

Four source-level cases challenge broad readings of the claimed workflow:

1. **Raw immutability is a policy, not a sandbox invariant.** Its owner is the host/user following the agent convention. Its enforcement point is instruction interpretation. The importer avoids existing destination names, but image drivers open derived raw reports for replacement; the disclaimer helper explicitly rewrites raw analysis Markdown. These do not prove original media bytes are modified, but disprove treating the whole raw tree as enforced read-only. See [RT-CLM-raw-immutability](#rt-clm-raw-immutability).
2. **Import deduplication has a narrower identity than content identity.** Its owner and enforcement point are importer fingerprint lookup. Path, size and integer modification time determine the key; changed bytes with unchanged metadata can be skipped, and copies at different paths can be imported again. The manifest is saved after all source operations; an interruption can leave copied files without persisted deduplication state. See [RT-RTE-source-import](#rt-rte-source-import).
3. **A successful producer does not imply delivery, and a failed producer can leave partial durable changes.** The cycle checks subprocess return codes and stops on nonzero, but producer writes precede later review rendering and push. In the empty-activity branch, only one recommendation is produced while rendering indexes recommendations 1 and 2: this can fail after the index update. Standalone producer, standalone sender and `--skip-push` are material alternate paths. Windows logging does not itself verify Python's exit status before recording “cycle finished.” See [RT-RTE-work-cycle](#rt-rte-work-cycle).
4. **Import storage and image selection need not meet.** Import groups images in month subdirectories, whereas the Qwen batch executable globs only the direct `raw/images` directory. Video extraction samples evenly spaced indices rather than implementing the documented scene-change/transcription pipeline. These are separate shipped tools, not a demonstrated end-to-end automatic media compiler. See [RT-RTE-image-analysis](#rt-rte-image-analysis) and [RT-RTE-source-import](#rt-rte-source-import). SRC-1: `scripts/video_extractor.py`.

The capability surface includes host-mediated file work, Python filesystem writes, provider requests, Git subprocess reads, fixed Windows shell date/time commands and outbound WeCom HTTP. These capabilities do not establish the current deployed grant set. Base configuration disables imports and WeCom; ignored local overrides can replace it. Model analysis drivers have their own API-key gates. No supplied host tool policy, operating-system isolation or deployed credentials establish a sandbox or approval envelope. Batch confirmation and workflow initiation are not per-content approvals. The image request contains no tool definitions; provider-native tool use or host callback policy is not inferable from this request. SRC-1: `.vlmwiki/config.json`, `scripts/config_utils.py`, `scripts/qwen_vlm_analyzer.py`, `scripts/wecom_push.py`.

Working context is shaped by the documented index-first selection and by the per-image request constructor. Each explicit model request contains the image and fixed prompt, without an application conversation history. This is not an implemented subagent delegation/compaction mechanism. Project file previews and top-N limits constrain deterministic reports, not a model context in the inspected work scanner. Host-side context trimming, tool authorization, scheduling, dynamic extensions and model fallback remain external and uninspected. SRC-1: `AGENTS.md`, `scripts/qwen_vlm_analyzer.py`, `scripts/work_project_reflection.py`.

This report adds implementation inspection of the cited paths at SRC-1's registered commit; it adds no source or evidence layer. No target code, services or examples were executed. The boundary's tracked analyses and log are reported operation, not supplied provider traces or experiments. Activation, correctness and benefit remain unobserved. Memory revision inventories belong to the memory member.

## Shared records

### Components

#### RT-CMP-qwen
Label: Qwen image inference endpoint

Source-native identity: `qwen3.5-omni-flash` in the three image-call scripts. Representational form: distributed-parametric model behind a remote API; storage substrate: provider-managed parameters, not supplied weights. Parameters changing during operation: uninspected; the client contains no weight-update operation. Exact model version pinned: no immutable version/digest is specified. Mutable endpoint resolution: the alias and configurable batch-function base URL do not rule out another model version; provider resolution is uninspected. The ordinary batch executable uses the mainland endpoint, the immediate-run driver the international endpoint, and the demo the mainland endpoint. SRC-1: `scripts/qwen_vlm_analyzer.py`, `scripts/run_analysis_now.py`, `scripts/single_image_demo.py`.

> model="qwen3.5-omni-flash",
> --- `scripts/qwen_vlm_analyzer.py`

> base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
> --- `scripts/run_analysis_now.py`

#### RT-CMP-ide-model
Label: Host-selected VLM and LLM

Source-native identity: configured VLM/LLM or current AI IDE built-in model. Representational form: distributed-parametric; storage substrate: external host/provider weights, inaccessible here. Parameter mutation during operation: uninspected. Exact version pinned: no; base configuration names `gpt-4o`, not an immutable model artifact. Endpoint resolution and actual choice: uninspected host behavior; the fallback is declared intent, not implemented here. SRC-1: `AGENTS.md`, `.vlmwiki/config.json`.

> **Model Note**: If multi-modal models are not configured in `.vlmwiki/config.json`, the agent will automatically use the built-in models from the current AI IDE (e.g., Trae IDE's MiniMax-M2).
> --- `AGENTS.md`

### Operative objects

#### RT-OBJ-config
Label: Base and local configuration

Source-native identity: `.vlmwiki/config.json` and optional `.vlmwiki/config.local.json`; symbolic JSON on the local filesystem, consumed by fixed Python configuration lookups. Recursive object merge preserves unspecified base keys and replaces other values. It controls importer sources, work selection, review enablement and delivery, not the hardcoded direct image request's model. Private local override contents are unavailable; default imports and delivery are disabled. SRC-1: `scripts/config_utils.py`, `.vlmwiki/config.json`.

> if LOCAL_CONFIG_PATH.exists():
>     local = json.loads(LOCAL_CONFIG_PATH.read_text(encoding="utf-8"))
>     return deep_merge(base, local)
> --- `scripts/config_utils.py`

### Routes

#### RT-RTE-agent-workflow
Label: Host-mediated media compilation and archive

Trigger/principal: user media request or archive request to the enclosing AI host. Endpoints: raw media/user request to wiki articles, related updates, index and log. Host model owns next-step selection under natural-language `AGENTS.md` guidance; host tools own physical I/O. Inputs include media, metadata and relevant existing content; no repository-owned scheduler, planner or permission checker is established by this instruction. Context acquisition, tool grants and recovery depend on that host. The model proposes and admits article content under the shipped conventions; no distinct per-content human approval or answer oracle is specified. Operating mode: open user requests, not a bounded experiment. Triggering a run is not approval of each resulting claim. Rejection/veto: user/host can intervene, but no shipped content gate is established. Rollback: uninspected host/manual capability; the procedure supplies no transactional undo. Archive requests retain a synthesis and add index/log entries. No claim of theory-building or improved capacity follows from this writing procedure. SRC-1: `AGENTS.md`, `AGENTS.zh.md`, `README.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Intended host response plus written knowledge artifacts; exact host return protocol is uninspected.
- Later read-back: Intended article/index reuse by the separate wiki query route.
- Delegated visibility: uninspected — no host delegation/context contract is supplied.
- Selection predicate: Model interprets media type, identified people/places, moment significance and user archive request.
- Invalidation or expiry: Related pages are to be updated; no fixed expiry or automatic invalidation rule is specified.
- Activation or effect: Requested persistent article creation and related updates; compliant execution is not observed.
- Evidence limits: Doctrine/design, not a shipped Python compiler or inspectable host trace.

> 5. **Update wiki**:
>    - Add to `wiki/moments/` if it's a life moment
>    - Add to relevant `wiki/people/` if people are identified
>    - Add to relevant `wiki/places/` if location identified
>    - Update `wiki/patterns/` if new pattern discovered
> --- `AGENTS.md`

#### RT-RTE-wiki-query
Label: Index-led later question answering

Endpoints: user question to host model answer, via retained index and articles. Next-step owner and selector: host model interpreting the question and index. Natural-language instructions prescribe preferential use of wiki content and internal-link citations; they are policy, not enforced retrieval or answer correctness. Model/tool execution and context limits belong to the host. Terminal output is an answer, not an automatic archive; the archive branch requires a user request. SRC-1: `AGENTS.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Synthesized answer with wiki-internal links, as requested by instructions.
- Later read-back: This invocation reads articles retained by earlier authoring; answer persistence requires the separate archive request.
- Delegated visibility: uninspected — host tool and delegation behavior is outside supplied evidence.
- Selection predicate: Read index, identify relevant articles, then read those articles.
- Invalidation or expiry: No query cache or expiry mechanism is specified in the inspected procedure.
- Activation or effect: Instructions request wiki preference over training knowledge; actual answer dependence is unobserved.
- Evidence limits: No retrieval trace, answer oracle, relevance evaluation or compliance result is supplied.

> 1. Read `wiki/index.md` to locate relevant articles
> 2. Read those articles and synthesize an answer
> 3. Prefer wiki content over training knowledge
> 4. Cite sources with wiki-internal links: `[[Category/Article]]`
> --- `AGENTS.md`

#### RT-RTE-source-import
Label: Local source import and manifest reload

Endpoints: enabled configured local sources to raw copies and persisted import manifest. Principal: CLI user; owner/executor: deterministic Python. Config selects sources, recursion, destination paths and format buckets. Explicit source-type mapping chooses a bucket before extension fallback; it is not semantic media validation. Decision/admission: code accepts unseen fingerprints and a mapped destination, without per-file human review or an answer oracle. Mode: open local folder import; `--dry-run` suppresses copying/manifest persistence but still creates destination directories. Guidance is symbolic configuration and filename/date rules; copied bytes plus manifest entries persist. Rejection is enabled-source, fingerprint and bucket filtering; user can disable a source or choose dry-run. Recovery is rerun/manual cleanup, not transaction rollback. Copying precedes manifest persistence; concurrent runs have no shown coordination lock. SRC-1: `scripts/import_data_sources.py`, `scripts/config_utils.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Printed counts and up to five target paths per source.
- Later read-back: Manifest reload skips known fingerprints on subsequent imports; downstream media compilation is separate.
- Delegated visibility: inapplicable — synchronous local code, not delegated model work.
- Selection predicate: Enabled/named source, recursive enumeration, unseen path-size-integer-mtime fingerprint, destination bucket.
- Invalidation or expiry: Metadata/path changes produce a new key; no manifest expiry is implemented in this file.
- Activation or effect: Copy and manifest writes are implemented; no supplied run demonstrates them.
- Evidence limits: Deduplication is not content hashing; private configured sources and manifest are unavailable.

> payload = f"{path.resolve()}|{stat.st_size}|{int(stat.st_mtime)}"
> return hashlib.sha1(payload.encode("utf-8")).hexdigest()
> --- `scripts/import_data_sources.py`

> if not dry_run:
>     shutil.copy2(source_file, target_path)
>     files_state[fingerprint] = {
> --- `scripts/import_data_sources.py`

#### RT-RTE-image-analysis
Label: Direct image request and report persistence

Endpoints: local image bytes to provider response to Markdown report/summary. Principal: script caller; batch CLI asks for key if missing and then `y` confirmation. Callable function has no confirmation. Demo asks for a key; immediate-run script requires the environment key. Owner of semantic description: [RT-CMP-qwen](#rt-cmp-qwen); Python owns request construction and unreviewed persistence. Context is one base64 image plus the fixed Chinese request for scene, objects, detailed description, mood and tags; no tools or conversational history are supplied. Mode: open image description. Model proposes response content and code admits it directly; no per-response human gate, expected-answer oracle or quality test. Batch exceptions record per-image failure and continue; single-image scripts return `None` for missing files and otherwise do not wrap the request in that batch recovery. Existing named reports can be overwritten; no version rollback is supplied. SRC-1: `scripts/qwen_vlm_analyzer.py`, `scripts/run_analysis_now.py`, `scripts/single_image_demo.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Model text from the function; persisted report and batch summary/status or single-image console output.
- Later read-back: uninspected — these drivers do not implement a later report reader or wiki compiler.
- Delegated visibility: Remote provider receives image bytes and text, not the wiki or full raw tree.
- Selection predicate: Batch globs supported extensions only in its immediate image directory; single-image executables use a hardcoded default path.
- Invalidation or expiry: Rerun replaces same-named reports/summary; no semantic invalidation or expiry gate.
- Activation or effect: Direct network call and text persistence wired; factual accuracy and later influence unobserved.
- Evidence limits: Endpoint/model alias is not an immutable version; SDK/provider behavior and invocation success are unobserved.

> return completion.choices[0].message.content
> --- `scripts/qwen_vlm_analyzer.py`

> output_file = output_dir / f"vlm_result_{image_path.stem}.md"
> with open(output_file, "w", encoding="utf-8") as f:
> --- `scripts/qwen_vlm_analyzer.py`

Supporting media tools do not fill the semantic compiler gap. `scripts/image_analyzer.py` uses PIL for dimensions, format, mode and size and writes `raw/analysis_results.json`. `scripts/video_extractor.py` writes uniformly indexed JPEG frames; neither is a model description/transcription route. Their symbolic arithmetic and file writes are implementation evidence, not observed media understanding. SRC-1: `scripts/image_analyzer.py`, `scripts/video_extractor.py`.

> frame_indices = [int(i * (total_frames - 1) / (num_frames - 1)) for i in range(num_frames)]
> --- `scripts/video_extractor.py`

#### RT-RTE-history-review
Label: Deterministic historical review generation

Endpoints: seven category directories plus diary Markdown to two dated review files, latest brief and log. Principal: CLI caller supplying/defaulting review date; owner: Python rules. Configuration can disable the engine. A simple parser reads frontmatter/body; counts, dates, repeated diary lines and fixed branches determine output. Both daily and weekly outputs use the same collected records rather than date-window filtering. Code proposes and admits generated content with no human review gate or answer oracle. Mode: ordinary corpus summarization/recommendation, not a comparison experiment. Guidance persists in Python; output persists as Markdown/JSON. Rejection is feature disablement/date validation, not recommendation-quality rejection. Rerun overwrites named reviews and brief; log append is implemented by read/replace. Partial writes have no shown transaction or rollback. SRC-1: `scripts/reflection_engine.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Printed generated review paths; daily/weekly Markdown, JSON brief and log entry.
- Later read-back: Reads articles/diaries retained by prior invocations; the engine's collector excludes reviews, so this does not itself establish recursive review consumption.
- Delegated visibility: inapplicable — no model or worker delegation in this implementation.
- Selection predicate: Direct `.md` files in seven category directories and raw diary directory; date parsing and counts shape recommendation branches.
- Invalidation or expiry: Same-date reviews/latest brief are replaced; no pruning or recommendation validation is implemented here.
- Activation or effect: Source wires retained-content-dependent output; no observed delivery, user action or benefit.
- Evidence limits: The name reflection does not establish model reflection, theory criticism or improved future capacity.

> records = collect_articles()
> diaries = collect_diaries()
> summary = summarize_articles(records)
> --- `scripts/reflection_engine.py`

> for review_type, period_name in (("daily", "最近一次历史"), ("weekly", "最近一段历史")):
> --- `scripts/reflection_engine.py`

#### RT-RTE-work-cycle
Label: Project scan, durable review and optional delivery

Endpoints: configured external project tree/Git metadata to project pages/index/review/runtime payload/log, then WeCom. Principal: CLI user or externally scheduled Windows task. Next-step owner: cycle subprocess sequence; scanner/delivery are standalone alternate entry points. Symbolic code selects files since configured date excluding named directories, takes newest file previews (first two nonempty lines, at most 180 characters), limits projects, and renders fixed interpretations/recommendations. Git runs use fixed argument arrays and return empty output on nonzero. No model receives the scan. Configuration comes from [RT-OBJ-config](#rt-obj-config). SRC-1: `scripts/work_project_reflection.py`, `scripts/run_work_reflection_cycle.py`.

Decision/admission: Python proposes and writes pages/reviews without per-content approval or answer oracle. Mode: repeated activity scanning, not an experiment or candidate contest. Guidance is config and fixed Python statements; project articles, index, review and runtime JSON persist. User can change config, skip push or run producer/sender separately. Sender gates outbound operation on enabled settings and required credentials, not semantic correctness. It sends a selected preview rather than full project evidence. HTTP timeouts and provider error-code checks bound delivery attempts; no retry queue, acknowledgement persistence or state rollback is implemented in these files. The producer has already changed disk when delivery fails. SRC-1: `scripts/work_project_reflection.py`, `scripts/wecom_push.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Generated paths, subprocess status and sender success/error; durable local changes can precede failure.
- Later read-back: Sender rereads produced review from disk. Project pages are eligible for later history-review reads and intended host queries; runtime JSON has no shown reader in these paths.
- Delegated visibility: Child processes run in project root; sender receives a review path. WeCom receives only selected/truncated Markdown and configured recipient information.
- Selection predicate: Recent eligible files, configured top-N limits; sender chooses Chinese preview section or first twenty cleaned lines, then at most 4,000 characters.
- Invalidation or expiry: Named project/review/runtime files and Projects index section are replaced; log grows; stale project-file removal is not part of this writer.
- Activation or effect: Source wires disk update and optional external send, not deployed recurrence or successful delivery.
- Evidence limits: External project tree, local configuration, scheduler registration, credentials and server behavior are unavailable; wrapper logs alone would not prove successful subprocess execution.

> completed = subprocess.run(command, cwd=str(PROJECT_ROOT), check=False)
> if completed.returncode != 0:
>     raise SystemExit(completed.returncode)
> --- `scripts/run_work_reflection_cycle.py`

> if not args.skip_push:
>     run_step(["python", "scripts/wecom_push.py", f"wiki/reviews/{review_file}"])
> --- `scripts/run_work_reflection_cycle.py`

> if "## 企业微信消息预览" in cleaned:
>     start = cleaned.index("## 企业微信消息预览") + 1
>     preview = cleaned[start:]
> else:
>     preview = cleaned[:20]
> return "\n".join(preview[:20])
> --- `scripts/wecom_push.py`

> "msgtype": "markdown",
> "markdown": {"content": content[:4000]},
> }
> return request_json(webhook_url, payload)
> --- `scripts/wecom_push.py`

The empty-result case challenges all-or-nothing completion: `build_focus_summary` returns one recommendation, while rendering dereferences three. Index replacement occurs before render/write. This source-level failure possibility is not an observed failure. SRC-1: `scripts/work_project_reflection.py`.

> ["先检查 `work_reflection.source_root` 是否正确。"],
> --- `scripts/work_project_reflection.py`

> "2. " + recommendations[1],
> "3. " + recommendations[2],
> --- `scripts/work_project_reflection.py`

The CMD wrapper invokes PowerShell with execution-policy bypass; PowerShell logs native output, then writes a finished line without explicitly checking `$LASTEXITCODE`. It supplies a task entry point, not task registration or an enforced recurrence interval. SRC-1: `scripts/run_work_reflection_task.cmd`, `scripts/run_work_reflection_task.ps1`.

> python scripts\run_work_reflection_cycle.py 2>&1 | Out-File -FilePath $logFile -Append -Encoding utf8
> "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] cycle finished" | Out-File -FilePath $logFile -Append -Encoding utf8
> --- `scripts/run_work_reflection_task.ps1`

### Claims

#### RT-CLM-raw-immutability
Label: Raw immutability convention

Claimed operation: raw material remains unchanged. Owner: interpreting host/user. Enforcement point: model-facing convention, not filesystem permissions. Guarantee strength: policy. Covered path: intended host compilation. Alternate paths: importer adds collision-avoiding copies; image reports/frame outputs are written under raw; the disclaimer helper replaces matching raw analysis Markdown. Required external contract: host and user respect the distinction between source media and generated analyses and do not mutate source bytes. SRC-1: `AGENTS.md`, `scripts/import_data_sources.py`, `scripts/qwen_vlm_analyzer.py`, `scripts/video_extractor.py`, `scripts/update_vlm_docs.py`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected

> - Raw files are immutable (never modify)
> --- `AGENTS.md`

> doc_file.write_text(new_content, encoding="utf-8")
> --- `scripts/update_vlm_docs.py`

The helper is a separate maintenance admission mechanism: user launches fixed code; it prefixes a simulation disclaimer and performs two textual replacements on matched reports that lack the marker. No model or human content decision occurs per file, no quality oracle is supplied, and no rollback is provided. Its existence bounds raw-tree read-only claims without proving alteration of original media. SRC-1: `scripts/update_vlm_docs.py`.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-agent-instructions
Label: Agent instruction interpretation

Consumer: external AI host/model. Channel: loaded `AGENTS.md` or Chinese equivalent as natural-language instructions. Force: requested task/selection/writing policy, contingent on host loading and compliance, not executable enforcement. Horizon: current authoring/query session and later sessions that reload the file. The article/query procedures in [RT-RTE-agent-workflow](#rt-rte-agent-workflow) and [RT-RTE-wiki-query](#rt-rte-wiki-query) carry this authority. SRC-1: `AGENTS.md`, `AGENTS.zh.md`.

> The wiki writes and maintains itself with VLM/LLM; the human reads and reflects.
> --- `AGENTS.md`

#### RT-BAP-config-consumption
Label: Runtime configuration control

Consumer: importer, reflection engine, work scanner/cycle and sender. Channel: loaded/merged JSON to fixed Python lookups. Force: executable selection, enablement, paths and delivery parameters; not model instructions. Horizon: each later invocation that reloads config. The merged configuration can change capabilities exercised by these scripts without changing product code. It does not select the hardcoded Qwen request model. See [RT-OBJ-config](#rt-obj-config). SRC-1: `scripts/config_utils.py`, `scripts/import_data_sources.py`, `scripts/reflection_engine.py`, `scripts/work_project_reflection.py`, `scripts/wecom_push.py`.

> if not settings["enabled"]:
>     raise SystemExit("WeCom delivery is disabled in .vlmwiki/config.json")
> --- `scripts/wecom_push.py`

## Annotations

none
