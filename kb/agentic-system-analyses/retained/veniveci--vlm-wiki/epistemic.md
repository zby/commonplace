---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "VLM-wiki epistemic routes: image candidates, corpus measurements, scripted interpretations, reliance and provenance relabeling."
run-id: AAS-2026-10-14-vlm-wiki-311faef777b4-01
reviewed-boundary: "503c43f98b5d1e21c74df384fdffd3e0652573b3"
---

# VLM-wiki epistemic report

## Source-and-claim boundary

The question is which shipped routes produce or acquire truth-apt content, what checks license reliance, and which later consumers receive it. Scope and exclusions are those of the [boundary](boundary.md#boundary-and-evidence); evidence identities remain in its [Source register](boundary.md#source-register). This member adds direct source inspection under SRC-1, not another source or evidence layer. Executable deductions below are implementation evidence, not target executions.

The material families are host compilation/query/archive, direct image descriptions, metadata measurement, deterministic history/work reviews, delivery selection and provenance relabeling. Import and video sampling are covered as lineage/input-selection operations, not semantic validators. Configuration gates and subprocess/HTTP success checks govern operation, not truth. No observed-run or causal-experiment source is supplied. Media pixels were not audited; provider weights, host internals, deployed inputs/configuration and ignored outputs remain unavailable as specified in the boundary. These gaps respectively prevent caption-accuracy judgments, internal model-process assessments, host-compliance conclusions and reconstruction of an actual review/delivery cycle. Checked-in reports establish candidate availability, not their production or acceptance history.

| Entry point or operation | Source path (SRC-1) | Coverage and reading basis |
|---|---|---|
| Host ingest, query, patterns, archive | `AGENTS.md`, `AGENTS.zh.md` | Direct English contract and Chinese query/pattern/archive reads; see [RT-RTE-agent-workflow](runtime.md#rt-rte-agent-workflow), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query). Host execution excluded, preventing compliance claims. |
| Image batch | `scripts/qwen_vlm_analyzer.py` | Direct request and batch persistence read; see [RT-RTE-image-analysis](runtime.md#rt-rte-image-analysis). |
| Single-image entry points | `scripts/run_analysis_now.py`, `scripts/single_image_demo.py` | Supplied runtime findings, not independently reread; see [RT-RTE-image-analysis](runtime.md#rt-rte-image-analysis). No independent complete-negative claim about their internal branches. |
| Metadata measurement | `scripts/image_analyzer.py` | Direct complete read; see [EPI-RTE-image-metadata](#epi-rte-image-metadata). |
| History review CLI | `scripts/reflection_engine.py` | Direct complete read, including parser, rules, renderer and dispatch; see [EPI-RTE-history-statistics](#epi-rte-history-statistics), [EPI-RTE-history-interpretation](#epi-rte-history-interpretation). |
| Work scanner/producer | `scripts/work_project_reflection.py` | Direct preview, scan, description, focus-summary, renderer and main reads; supplied runtime covers remaining writer/index/payload details; see [EPI-RTE-work-interpretation](#epi-rte-work-interpretation), [RT-RTE-work-cycle](runtime.md#rt-rte-work-cycle). |
| Cycle, scheduler wrappers, WeCom | `scripts/run_work_reflection_cycle.py`, `scripts/run_work_reflection_task.cmd`, `scripts/run_work_reflection_task.ps1`, `scripts/wecom_push.py` | Direct sender selection/settings/dispatch read; cycle/wrapper and HTTP details supplied by [RT-RTE-work-cycle](runtime.md#rt-rte-work-cycle). No independent complete audit of wrapper behavior. |
| Disclaimer helper | `scripts/update_vlm_docs.py` | Direct complete read including dispatch; see [EPI-RTE-disclaimer-rewrite](#epi-rte-disclaimer-rewrite). |
| Import, config, frame sampling | `scripts/import_data_sources.py`, `scripts/config_utils.py`, `scripts/video_extractor.py` | Supplied runtime findings: [RT-RTE-source-import](runtime.md#rt-rte-source-import), [RT-OBJ-config](runtime.md#rt-obj-config), [RT-RTE-image-analysis](runtime.md#rt-rte-image-analysis). These are not independent semantic audits. |
| Templates and retained examples | `references/article-template.md`, `references/archive-template.md`, `raw/analysis_results.json`, `wiki/log.md` | Supplied boundary findings only. Prevents independent instance-level provenance or factual validation. |

The inspected Python entry points dispatch fixed functions through CLI/main blocks, not registered agent tools or hook evaluators. The enclosing host's hook/tool registry is outside the boundary. This is not a system-complete negative about semantic evaluators. The consequential claims examined are [EPI-CLM-wiki-compounding](#epi-clm-wiki-compounding), [EPI-CLM-history-synthesis](#epi-clm-history-synthesis) and [RT-CLM-raw-immutability](runtime.md#rt-clm-raw-immutability).

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-image-reports](#epi-obj-image-reports) | see record | see record | SRC-1: `scripts/qwen_vlm_analyzer.py` | No verified caption instance or provider trace. |
| [EPI-OBJ-wiki-articles](#epi-obj-wiki-articles) | see record | see record | SRC-1: `AGENTS.md` | Authored claims, source citations and real-world truth remain separate. |
| [EPI-OBJ-history-snapshot](#epi-obj-history-snapshot) | see record | see record | SRC-1: `scripts/reflection_engine.py` | Parsed corpus is not the person's complete history. |
| [EPI-OBJ-history-insights](#epi-obj-history-insights) | see record | see record | SRC-1: `scripts/reflection_engine.py` | Split from counts because semantic extrapolation differs. |
| [EPI-OBJ-work-review](#epi-obj-work-review) | see record | see record | SRC-1: `scripts/work_project_reflection.py` | Project metadata, inferred attention and recommendations have different licenses. |
| [RT-OBJ-config](runtime.md#rt-obj-config) | No truth claim required for enablement/path policy | see record | SRC-1: `scripts/config_utils.py` | Controls selection, not content warrant. |
| [EPI-OBJ-analysis-results](#epi-obj-analysis-results) | see record | see record | SRC-1: `scripts/image_analyzer.py` | Decoder/file properties, not scene understanding. |
| [EPI-OBJ-vlm-analysis](#epi-obj-vlm-analysis) | see record | see record | SRC-1: `scripts/update_vlm_docs.py` | Rewrite target is not the tracked image-report directory; applicability unobserved. |

## Authority-route ledger

Fields owned by a cited declaration are given by that declaration; this overlay separates the consequential functions and their epistemic licenses. No row asserts observed operation.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-source-import](runtime.md#rt-rte-source-import) | content transformation | implemented | Raw source files; see route | truth-apt transformation: acquisition/import | see route | see route; eligibility is not truth evaluation | see route | see route | Copy and manifest | Imported source warrant unknown; copying adds none | see route | see route | SRC-1: `scripts/import_data_sources.py` | none | none | Metadata fingerprint does not authenticate contents. |
| [RT-RTE-image-analysis](runtime.md#rt-rte-image-analysis) | content transformation | implemented | [EPI-OBJ-image-reports](#epi-obj-image-reports) | truth-apt transformation: indeterminate | Image to scene/mood/tag text | Provider model, descriptive domain; no expected answer | see route | see route | Candidate generation | Request supports candidate description only; semantic preservation/entailment unestablished | see route | see route | SRC-1: `scripts/qwen_vlm_analyzer.py` | [EPI-CLM-wiki-compounding](#epi-clm-wiki-compounding) | none | Need image/output pair and reference evidence to classify individual content edges. |
| [RT-RTE-image-analysis](runtime.md#rt-rte-image-analysis) | retention | implemented | [EPI-OBJ-image-reports](#epi-obj-image-reports) | no content change | Returned text to report | Write success/exception, filesystem domain | see route | see route | Unreviewed write | No acceptance criterion for caption truth | see route | see route | SRC-1: `scripts/qwen_vlm_analyzer.py` | none | none | Status success means request/write path, not factual success. |
| [EPI-RTE-image-metadata](#epi-rte-image-metadata) | check/evidence production | implemented | [EPI-OBJ-analysis-results](#epi-obj-analysis-results) | truth-apt transformation: acquisition/import | see record | see record | see record | see record | Evidence recording | License limited to decoder/file properties; source warrant conditional on PIL/filesystem contracts | see record | see record | SRC-1: `scripts/image_analyzer.py` | none | none | Hardcoded timestamp is not measurement time. |
| [EPI-RTE-history-statistics](#epi-rte-history-statistics) | content transformation | implemented | [EPI-OBJ-history-snapshot](#epi-obj-history-snapshot) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | Deterministic measurement | Counts/order follow supplied parsed records, not truth of their assertions | see record | see record | SRC-1: `scripts/reflection_engine.py` | [EPI-CLM-history-synthesis](#epi-clm-history-synthesis) | none | Interpretation and parser fidelity bound the domain. |
| [EPI-RTE-history-interpretation](#epi-rte-history-interpretation) | content transformation | implemented | [EPI-OBJ-history-insights](#epi-obj-history-insights) | truth-apt transformation: ampliative conjecture | see record | see record | see record | see record | Unchecked authored inference | Corpus concentration does not entail single-trip bias; additional diary entries do not entail better advice | see record | see record | SRC-1: `scripts/reflection_engine.py` | [EPI-CLM-history-synthesis](#epi-clm-history-synthesis) | overgeneralization | Concrete countercase in record. |
| [EPI-RTE-work-interpretation](#epi-rte-work-interpretation) | content transformation | implemented | [EPI-OBJ-work-review](#epi-obj-work-review) | truth-apt transformation: ampliative conjecture | see record | see record | see record | see record | Unchecked authored inference | Recent filenames/extensions do not warrant named work domains or attention | see record | see record | SRC-1: `scripts/work_project_reflection.py` | [EPI-CLM-history-synthesis](#epi-clm-history-synthesis) | fixed domain inference | Countercase in record; metadata summaries retain narrower license. |
| [RT-RTE-history-review](runtime.md#rt-rte-history-review), [RT-RTE-work-cycle](runtime.md#rt-rte-work-cycle) | retention | implemented | [EPI-OBJ-history-insights](#epi-obj-history-insights), [EPI-OBJ-work-review](#epi-obj-work-review) | no content change | Generated sections to durable files | see records | see records | see records | Direct write/replace | Retention does not establish acceptance | see records | see records | SRC-1: `scripts/reflection_engine.py` | [EPI-CLM-history-synthesis](#epi-clm-history-synthesis) | none | No observed execution or successful complete cycle. |
| [RT-RTE-work-cycle](runtime.md#rt-rte-work-cycle) | operational admission/selection/consumption | implemented | [EPI-OBJ-work-review](#epi-obj-work-review) | truth-apt transformation: non-ampliative reshaping | Preview subset to sender | see record; config/HTTP domain | see record | see record | Delivery gate, not semantic gate | No endorsement from errcode zero; selection omits evidence | see record | see record | SRC-1: `scripts/wecom_push.py` | none | none | Daily review lacks Chinese preview marker and falls back to first twenty cleaned lines. |
| [RT-RTE-agent-workflow](runtime.md#rt-rte-agent-workflow) | content transformation | doctrine only | [EPI-OBJ-wiki-articles](#epi-obj-wiki-articles) | truth-apt transformation: indeterminate | see record | see record | see record | see record | Requested model authorship | Individual acquisition/reshaping/conjecture edges need actual inputs and outputs | see record | see record | SRC-1: `AGENTS.md` | [EPI-CLM-wiki-compounding](#epi-clm-wiki-compounding) | none | Repository has no inspected executable general compiler. |
| [RT-RTE-agent-workflow](runtime.md#rt-rte-agent-workflow) | retention | doctrine only | [EPI-OBJ-wiki-articles](#epi-obj-wiki-articles) | no content change | see record | see record | see record | see record | Requested writing/linking | Article links and archive requests do not constitute acceptance | see record | see record | SRC-1: `AGENTS.md` | [EPI-CLM-wiki-compounding](#epi-clm-wiki-compounding) | none | No accepted-claim lifecycle integration established by this policy. |
| [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-wiki-articles](#epi-obj-wiki-articles) | truth-apt transformation: indeterminate | see record | see record | see record | see record | Requested source preference | Index relevance/citation does not license truth beyond cited content | see record | see record | SRC-1: `AGENTS.md` | [EPI-CLM-wiki-compounding](#epi-clm-wiki-compounding) | none | Instruction-mediated reliance, not demonstrated answer correctness. |
| [EPI-RTE-disclaimer-rewrite](#epi-rte-disclaimer-rewrite) | check/evidence production | implemented | [EPI-OBJ-vlm-analysis](#epi-obj-vlm-analysis) | no content change | Marker presence in matched report | Fixed substring test; marker domain only | see record | Marker found or absent | Skip or continue rewrite | No evaluation of actual provenance or scene truth | see record | see record | SRC-1: `scripts/update_vlm_docs.py` | [RT-CLM-raw-immutability](runtime.md#rt-clm-raw-immutability) | none | Marker is not provenance evidence. |
| [EPI-RTE-disclaimer-rewrite](#epi-rte-disclaimer-rewrite) | disposition/acceptance | implemented | [EPI-OBJ-vlm-analysis](#epi-obj-vlm-analysis) | truth-apt transformation: ampliative conjecture | Relabel report as simulated | Filename and missing-marker rule, not evidence-consuming acceptance | see record | Simulation warning prefixed | Enforcing file rewrite | Withholds apparent model provenance in text; does not verify simulation attribution | see record | see record | SRC-1: `scripts/update_vlm_docs.py` | [RT-CLM-raw-immutability](runtime.md#rt-clm-raw-immutability) | unverified provenance assignment | No downstream mechanical exclusion or deletion. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-wiki-compounding](#epi-clm-wiki-compounding) | see record | SRC-1: `AGENTS.md`; doctrine/design | see record | [RT-RTE-image-analysis](runtime.md#rt-rte-image-analysis), [RT-RTE-history-review](runtime.md#rt-rte-history-review), [RT-RTE-work-cycle](runtime.md#rt-rte-work-cycle) | None supplied | No comparison; external host owns general model compilation/query | Persistence and deterministic reuse are implementable; instructions request broader model compilation and preference | Compounding content is not demonstrated compounding warrant or capacity. |
| [EPI-CLM-history-synthesis](#epi-clm-history-synthesis) | see record | SRC-1: `README.md`; doctrine/design | see record | [EPI-RTE-history-statistics](#epi-rte-history-statistics), [EPI-RTE-history-interpretation](#epi-rte-history-interpretation), [EPI-RTE-work-interpretation](#epi-rte-work-interpretation) | None supplied | No reference outcomes/user-action comparison; no implemented semantic test in these inspected rules | Snapshot/counts supported over parsed corpus; recommendations are branch-generated | Some interpretations exceed premises; daily/weekly names do not establish date windows. |
| [RT-CLM-raw-immutability](runtime.md#rt-clm-raw-immutability) | see record | SRC-1: `AGENTS.md`; doctrine/design | see record | [RT-RTE-source-import](runtime.md#rt-rte-source-import), [EPI-RTE-disclaimer-rewrite](#epi-rte-disclaimer-rewrite) | None supplied | Policy, not filesystem isolation; generated raw reports differ from original media | Original-media preservation is a convention; derived raw report rewriting exists | Whole raw-tree enforced immutability is unsupported. |

## Bounded conclusion

- Direct image drivers retain model candidates without a content-specific evidence-consuming acceptance decision. Imported files have unknown inherited warrant; provider text does not acquire warrant from successful persistence. Internal parametric inference/update remains uninspected; the [RT-CMP-qwen](runtime.md#rt-cmp-qwen) and [RT-CMP-ide-model](runtime.md#rt-cmp-ide-model) have no supplied immutable weights or mutation traces.
- The measurement routes have narrower positive licenses: [EPI-RTE-image-metadata](#epi-rte-image-metadata) reports file/decoder properties; [EPI-RTE-history-statistics](#epi-rte-history-statistics) derives counts and date order over a parsed corpus. Neither validates source narratives, real-world completeness, media dates or a proposed explanation.
- [EPI-RTE-history-interpretation](#epi-rte-history-interpretation) and [EPI-RTE-work-interpretation](#epi-rte-work-interpretation) produce identifiable non-entailed assertions alongside advisory policy. Fixed rules determine these propositions; a model is not required for conjecture. Their retention and delivery are implemented, but testing, acceptance against named truth/use criteria and post-acceptance lifecycle integration are not established in these inspected paths. The recommendation consumer is a human via Markdown/WeCom, advisory over future action; no human action/compliance is observed. Project pages also reach later deterministic history review and intended host queries through [RT-RTE-work-cycle](runtime.md#rt-rte-work-cycle).
- The provenance helper is a material corrective counterexample to a claim of pure append-only storage: it rewrites epistemic labels. Its marker check is real but only syntactic. It assigns, rather than verifies, simulation provenance and does not mechanically withdraw a report from retrieval. No report-specific truth acceptance follows.
- Host compilation, pattern discovery, archive and preferential query remain doctrine-level routes; the instructions confer requested reliance without specifying a distinct semantic gate. Their actual transformations cannot be classified claim by claim without host traces. The inspected deterministic review code has no content-directed criticism/revision feedback loop; this bounded finding does not adjudicate inaccessible model reasoning. More retained material is not by itself improved future capacity, and the name reflection does not establish bidirectional self-representation. No causal improvement evidence is supplied. Autonomy of the fixed computations is separate from autonomy of the external host workflow and from reliability. No system-wide score or negative about every possible evaluator follows from this partial independent inspection.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-image-reports
Label: Image reports

Part of: [RT-RTE-image-analysis](runtime.md#rt-rte-image-analysis)

This object is the natural-language output part of the enclosing route, not another route. Source-native identity: `vlm_result_{image_path.stem}.md` and single-image report outputs; storage: Markdown files. Content: scene/time/place descriptions, objects, mood and tags, truth-apt only insofar as their referents/scope can be specified. Producer and admission are those of the parent route; there is no source-specific truth verdict. SRC-1: `scripts/qwen_vlm_analyzer.py`; its returned-text/write passages are retained by the parent record.

#### EPI-OBJ-wiki-articles
Label: Wiki articles

Source-native identity: `wiki/` category articles and archives; natural-language bodies with symbolic frontmatter/link conventions on the filesystem. Intended claims describe life events, people, places, projects and patterns. Closest supplied records: [RT-RTE-agent-workflow](runtime.md#rt-rte-agent-workflow), [RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query); distinct object spans their write/read endpoints, not either whole route. Requested source-preferential reliance belongs to the query record. SRC-1: `AGENTS.md`; parent workflow/query quotations supply the writing/preference evidence.

#### EPI-OBJ-history-snapshot
Label: History snapshot

Part of: [RT-RTE-history-review](runtime.md#rt-rte-history-review)

Material output object of that route: natural-language snapshot derived from symbolic counters/date ordering, stored in daily/weekly Markdown. Scope is collected articles, diary files and media entries, not independently observed life history. Different from [EPI-OBJ-history-insights](#epi-obj-history-insights): literal counts/metadata summaries have different warrant from explanatory prose. Evidence: [EPI-RTE-history-statistics](#epi-rte-history-statistics), SRC-1: `scripts/reflection_engine.py`.

#### EPI-OBJ-history-insights
Label: History insights

Part of: [RT-RTE-history-review](runtime.md#rt-rte-history-review)

Material output object, not the entire producer route. Natural-language interpretations and recommendations reside in review Markdown and `latest_brief.json`. Recommendations include imperatives (not truth-apt) and embedded predictions/descriptions (truth-apt). Evidence: [EPI-RTE-history-interpretation](#epi-rte-history-interpretation), SRC-1: `scripts/reflection_engine.py`.

#### EPI-OBJ-work-review
Label: Work review

Part of: [RT-RTE-work-cycle](runtime.md#rt-rte-work-cycle)

Material output object of the producer/delivery container: natural-language project articles and review with symbolic paths, counts and timestamps, stored as Markdown/JSON. Metadata describes selected eligible files, while interpretive prose purports to describe attention/work direction; recommendations are advisory policy. The sender receives a preview subset, not the full source evidence. Evidence: [RT-RTE-work-cycle](runtime.md#rt-rte-work-cycle), [EPI-RTE-work-interpretation](#epi-rte-work-interpretation), SRC-1: `scripts/work_project_reflection.py`, `scripts/wecom_push.py`.

#### EPI-OBJ-analysis-results
Label: Analysis results

Source-native identity: `raw/analysis_results.json`; symbolic JSON on disk, containing dimensions, format, mode, file size/path and errors. Distinct from the semantic image report in [RT-RTE-image-analysis](runtime.md#rt-rte-image-analysis); that supplied container mentions this supporting tool but does not encompass its independent invocation. Its `timestamp` literal is not a clock measurement. SRC-1: `scripts/image_analyzer.py`.

> "timestamp": "2026-05-03",
> --- `scripts/image_analyzer.py`

#### EPI-OBJ-vlm-analysis
Label: VLM analysis documents

Source-native identity: `raw/vlm_analysis/image_*.md` and `video_frame_*.md`, the helper's Markdown targets. Natural-language report/provenance text stored on disk. Distinct from direct Qwen output naming/location in [RT-RTE-image-analysis](runtime.md#rt-rte-image-analysis); existence of matching deployed files is unobserved. Closest supplied account is [RT-CLM-raw-immutability](runtime.md#rt-clm-raw-immutability), which discusses this helper but declares a policy claim, not this object. Evidence: [EPI-RTE-disclaimer-rewrite](#epi-rte-disclaimer-rewrite), SRC-1: `scripts/update_vlm_docs.py`.

### Routes

#### EPI-RTE-image-metadata
Label: Image metadata measurement

Source-native endpoints: image files to PIL attributes/stat results to JSON. Owner: deterministic Python/PIL; context: local files in image/frame directories. This is a distinct executable route from [RT-RTE-image-analysis](runtime.md#rt-rte-image-analysis), which uses a remote semantic model. Target: file/decoder properties; evaluator: PIL open/attributes and filesystem stat, with exception-to-error conversion. Proposer/decider: code; user launches it but does not approve each measurement. No expected-answer oracle or comparison experiment. Persistence is direct JSON overwrite, no truth gate, transaction or rollback.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Dictionary with properties or error; CLI prints results and writes analysis JSON.
- Later read-back: uninspected — no downstream JSON reader established by this tool or supplied runtime.
- Delegated visibility: inapplicable — local synchronous measurement, no model delegation.
- Selection predicate: Direct image files with listed extensions; optional frame directory.
- Invalidation or expiry: Same output JSON is overwritten; no expiry/version check.
- Activation or effect: File property measurement/persistence wired, not executed here.
- Evidence limits: Decoder attributes do not judge scene meaning or validate hardcoded timestamp; PIL internals uninspected.

SRC-1: `scripts/image_analyzer.py` (implementation).

> img = Image.open(image_path)
> width, height = img.size
> format = img.format
> mode = img.mode
> --- `scripts/image_analyzer.py`

> "filesize": image_path.stat().st_size
> --- `scripts/image_analyzer.py`

#### EPI-RTE-history-statistics
Label: History statistics

Part of: [RT-RTE-history-review](runtime.md#rt-rte-history-review)

Endpoints: parsed article/diary records to counters, latest-date selection and snapshot strings. Owner/evaluator: deterministic Python; target/domain: representation-level counts and parseable date ordering. This is a non-overlapping computational part of the parent's generation, not acceptance of source narratives. Imported summaries/titles are relayed, not independently produced truths. Parser handles a limited frontmatter syntax; encoded input and parsing fidelity bound the premises.

Concrete implementation deduction: a hypothetical parsed corpus with one `moment` record and two `travel` tags yields article counter `moment: 1`, tag counter `travel: 2`, and snapshot total one. These follow from iterating each parsed record/tag, not from any model judgment. It would be invalid to infer two trips from those two tag entries. No target code was executed.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Counter/date summary and snapshot strings passed to renderer.
- Later read-back: Parent persists snapshots in reviews; reviews are excluded from this collector, so recursive self-reading is not established.
- Delegated visibility: inapplicable — no delegated execution.
- Selection predicate: Seven category directories, direct Markdown files, dates accepted by `%Y-%m-%d`; diaries handled separately.
- Invalidation or expiry: Recomputed on invocation; parent replaces same-date review paths.
- Activation or effect: Parsed corpus determines numerical report content; real activation unobserved.
- Evidence limits: No source-truth, comprehensive-history or formal parser-verification claim.

SRC-1: `scripts/reflection_engine.py` (implementation).

> article_counter = Counter(record.article_type for record in records)
> tag_counter = Counter(tag for record in records for tag in record.tags)
> --- `scripts/reflection_engine.py`

> snapshot.append(f"当前知识库共有 {len(records)} 篇文章，其中 moments {article_counter.get('moment', 0)} 篇，places {article_counter.get('place', 0)} 篇。")
> --- `scripts/reflection_engine.py`

#### EPI-RTE-history-interpretation
Label: History interpretation

Part of: [RT-RTE-history-review](runtime.md#rt-rte-history-review)

Endpoints: counters/date gaps to interpretive statements and recommendations, then parent's review/brief writer. Owner/proposer/decider: fixed Python branches; input guidance is authored strings and thresholds. Mode: open corpus reporting, no expected-answer oracle, per-content approval or measured benefit criterion. Config can disable invocation; it does not veto a particular inference. Parent overwrites outputs; no content-specific rollback.

Concrete falsifying input: any positive `place_counter` from records of many separate trips enters the same branch asserting the KB is biased toward a single trip. Thus the single-trip proposition does not follow from the condition. The recommendation that more diary samples will make advice markedly more specific is likewise an untested forecast, not a counter result. Its imperative is policy; its forecast is a conjecture. These are source deductions, not observed bad outputs.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Insights and recommendations lists for the parent renderer.
- Later read-back: Stored in reviews/brief; downstream brief reader uninspected, parent collector excludes reviews.
- Delegated visibility: inapplicable — no model or worker call.
- Selection predicate: Positive counters, missing categories, diary-count comparison, latest-date gap; first four recommendations retained.
- Invalidation or expiry: Regenerated and overwritten by parent, not withdrawn after semantic checks.
- Activation or effect: Conditions control emitted prose; users may read advisory output, but action/benefit unobserved.
- Evidence limits: No evidence-consuming acceptance of the single-trip explanation or advice efficacy.

SRC-1: `scripts/reflection_engine.py` (implementation).

> if place_counter:
>     top_places = "、".join(f"{place}({count})" for place, count in place_counter.most_common(3))
>     insights.append(f"地点关联集中在 {top_places}，说明现有知识库还明显偏向单次旅行样本。")
> --- `scripts/reflection_engine.py`

> recommendations.append("日记样本偏少，建议每天补 3 到 5 行，后续晨间建议会明显更具体。")
> --- `scripts/reflection_engine.py`

#### EPI-RTE-work-interpretation
Label: Work interpretation

Part of: [RT-RTE-work-cycle](runtime.md#rt-rte-work-cycle)

Endpoints: project activity list to fixed insight/recommendation strings, then review writer. Owner/proposer/decider: Python; guidance: authored prose with count/name interpolations. The scan imports file metadata/Git text and derives counts over eligible files; those narrower fields are not equivalent to this interpretation. Nonempty activity triggers a claim about knowledge bases, RAG, AUTOSAR or document work, regardless of project contents. A hypothetical active project containing only recent poetry text still emits the named-domain attention claim. This concrete branch counterexample establishes non-entailment, not merely failure to prove entailment. Empty activity returns a different branch; it does not refute the nonempty-case finding.

No semantic evaluator, reference outcome or per-content human gate appears in this inspected function/renderer/main chain. Config controls scan parameters, not acceptance of the attention claim. Mode: routine work reporting; parent owns persistence, partial failure and recovery limits.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Snapshot/insight/recommendation lists used in review rendering.
- Later read-back: Parent sender rereads preview; project pages can be read by history review, while review feedback to this function is not implemented here.
- Delegated visibility: inapplicable — deterministic local code; external sender receives selected prose, not a model delegation.
- Selection predicate: Nonempty selected activity list; ranking and truncation inherited from parent scan.
- Invalidation or expiry: Parent replaces named artifacts, not an evaluation-triggered withdrawal.
- Activation or effect: Input changes names/counts; fixed interpretation/recommendations are persisted and can be sent, with no observed user action.
- Evidence limits: File mtime is an activity proxy; work direction/attention and helpfulness have no supplied validation.

SRC-1: `scripts/work_project_reflection.py` (implementation).

> insights = [
>     "工作痕迹主要集中在 "
>     + "、".join(f"`{item.name}`" for item in activities[:4])
>     + "，说明最近的注意力集中在知识库、RAG、AUTOSAR 或文档沉淀。",
> --- `scripts/work_project_reflection.py`

#### EPI-RTE-disclaimer-rewrite
Label: Disclaimer rewrite

Endpoints: matching analysis Markdown to marker check to prefixed/replaced Markdown. Owner/proposer/decider: fixed Python; principal: launching user. Closest supplied record [RT-CLM-raw-immutability](runtime.md#rt-clm-raw-immutability) describes this behavior as a counterexample but declares a policy claim, not this route. Distinct referent, not a replacement for that claim.

The check target is marker presence, domain is strings, evaluator is substring membership. Result found skips rewriting; missing marker admits a simulation-provenance assertion plus two textual replacements. It is not an evidence-consuming check of whether the report really was simulated. A genuine model report named to match the glob and lacking the marker would receive the same simulation warning. This establishes an ampliative provenance claim, not a valid provenance derivation. Computational admission has no per-file human decision or expected-answer oracle. User can decline to run/edit manually; no transactional rollback or downstream exclusion list is supplied.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Rewritten files and printed updated/skipped names.
- Later read-back: uninspected — no reader of this target directory established by supplied records or helper.
- Delegated visibility: inapplicable — local synchronous rewrite.
- Selection predicate: Two globs in `raw/vlm_analysis`; missing marker permits rewrite.
- Invalidation or expiry: Marker suppresses later rewrites; no expiry/provenance revalidation.
- Activation or effect: Textual provenance warning enforced in matched files; downstream reliance change unobserved.
- Evidence limits: No matching-file instance/run supplied; not a demonstrated correction of tracked `raw/images` analyses.

SRC-1: `scripts/update_vlm_docs.py` (implementation).

> patterns = ["image_*.md", "video_frame_*.md"]
> --- `scripts/update_vlm_docs.py`

> if "⚠️ 模拟分析" in content:
>     print(f"跳过（已有声明）: {doc_file.name}")
>     continue
> --- `scripts/update_vlm_docs.py`

> **注意**: 此文档内容是为了演示目的而创建的模拟分析，不是真实调用 qwen3.5-omni-flash 模型的结果。
> --- `scripts/update_vlm_docs.py`

> new_content = disclaimer + content
> new_content = new_content.replace("文件名: `", "文件名**: `")
> new_content = new_content.replace("## 🤖 VLM 视觉分析", "## 🤖 模拟 VLM 视觉分析")
> --- `scripts/update_vlm_docs.py`

### Claims

#### EPI-CLM-wiki-compounding
Label: Wiki compounding

Claimed operation: model-assisted compilation/maintenance of a persistent personal wiki, with automatic discovery of recurring life patterns. This is broader than the raw-preservation policy in [RT-CLM-raw-immutability](runtime.md#rt-clm-raw-immutability); no duplicate supplied claim declaration. SRC-1: `AGENTS.md`, doctrine/design. The host workflow/query records retain the maintenance and source-preference passages. Persistence does not itself claim or demonstrate infallibility.

> "The VLM wiki is a persistent, compounding artifact of your life."
> --- `AGENTS.md`

> Automatically detect:
> - **Time patterns** (recurring activities)
> - **People patterns** (who you interact with often)
> - **Location patterns** (places visited frequently)
> - **Mood patterns** (emotional trends over time)
> - **Learning patterns** (topics revisited)
> --- `AGENTS.md`

#### EPI-CLM-history-synthesis
Label: History synthesis

Claimed operation: history-derived snapshot, repeated topics/places/diary clues and next-action recommendations. No counterpart claim in supplied runtime: [RT-RTE-history-review](runtime.md#rt-rte-history-review) declares the implementation container, not this public claim. SRC-1: `README.md`, doctrine/design. Work review is a separate shipped implementation comparison, not proof of this history engine's behavior.

> The current MVP produces:
>
> 1. **Snapshot**: what the memory base contains right now
> 2. **What History Says**: repeated topics, places, and diary clues
> 3. **Recommended Next Actions**: what to record or structure next
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
