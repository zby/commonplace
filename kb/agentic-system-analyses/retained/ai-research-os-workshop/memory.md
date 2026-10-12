---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "AI Research OS Workshop memory: topic-local catalog, layered source/wiki retention, criticism and selective downstream exports."
run-id: AAS-2026-10-12-ai-research-os-workshop-1a93869f8e7f-01
source-identity: https://github.com/iusztinpaul/ai-research-os-workshop
reviewed-boundary: dc6660555266239cd36483cf51b5ab39febacf02
---

# AI Research OS Workshop memory report

## Boundary and evidence

The memory boundary is the shipped topic-local research directory and the operations that acquire, transform, maintain and later consume it. It includes alternative source layers, GitHub specifications/cache, query save-back, lint criticism, distill exports and all four render forms. It excludes host conversation retention, provider internals and external source-service storage implementations. These exclusions prevent conclusions about host compaction, numerical adaptation and external service retention. The model components and their opaque parameter provenance remain as described by [RT-CMP-host-model](runtime.md#rt-cmp-host-model) and [RT-CMP-notebooklm-model](runtime.md#rt-cmp-notebooklm-model), not inferred from the filesystem wiki. SRC-1: `plugins/ai-research-os/skills/research/CONVENTIONS.md`; source identity and scope are declared in [boundary](boundary.md#source-register).

HEAD was directly rechecked as dc6660555266239cd36483cf51b5ab39febacf02. Direct reads supply implementation evidence for the index builders, dedup helper, PDF extractor and all mechanical lint scripts including `_lintlib.py`; the YouTube write/metadata/failure branch was read at lines 194–373. Direct prompt reads cover conventions, research routing/query (1–255), construction/cleanup (638–931), builder, source/entity/concept/summary/comparison writers, lint driver/judge, distill and render drivers and all four render writers. Marketplace/plugin manifests were read. File inventories and targeted helper searches add coverage, not execution evidence. Remaining discovery and GitHub orchestration details are supplied runtime findings rather than complete direct reads. No target code, providers, tests or examples were executed; no observed-run evidence is supplied.

### Coverage inventory

“Direct” below means source text inspected in this job. A supplied route is evidence inherited from runtime, not independently exercised behavior. Static shipped guidance and Python source are already declared in [RT-OBJ-skill-instructions](runtime.md#rt-obj-skill-instructions) and [RT-OBJ-python-helpers](runtime.md#rt-obj-python-helpers); they are not accumulated memory.

| Entry point / operation | Source path and inspection | Covering records / unresolved limits |
|---|---|---|
| Plugin discovery and dispatch | SRC-1: `.claude-plugin/marketplace.json`, `plugins/ai-research-os/.claude-plugin/plugin.json` — direct; plugin tree inventoried | [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance). Four research entry skills plus bundled source-CLI guidance; no additional hook/tool registry found in this bounded tree inventory. Actual host installation and tool grants uninspected. |
| Init/append; dedup and deep rounds | SRC-1: `plugins/ai-research-os/skills/research/SKILL.md` routing/build ranges direct; `plugins/ai-research-os/skills/research/scripts/dedup_findings.py` direct; discovery body supplied | [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest), [RT-RTE-deep-discovery](runtime.md#rt-rte-deep-discovery), [MEM-OBJ-index-metadata](#mem-obj-index-metadata), [MEM-OBJ-index-summary](#mem-obj-index-summary). Initial source-service provenance and search completeness cannot be established. |
| Obsidian/Readwise/NLM acquisition, web fallback | SRC-1: `plugins/ai-research-os/skills/research/agents/builder.md` direct; external CLI implementations excluded | [MEM-OBJ-raw-documents](#mem-obj-raw-documents), [MEM-OBJ-key-highlights](#mem-obj-key-highlights). Highlight-only Obsidian is an alternative checkpoint with null full text; NLM note recipe can retain failure text. User-authorship assertions are source contracts, not authenticated origin. |
| PDF, images, YouTube captions | SRC-1: `plugins/ai-research-os/skills/research/scripts/extract_pdf.py` direct; `plugins/ai-research-os/skills/research/scripts/youtube_extract_transcript.py` write range direct; `plugins/ai-research-os/skills/research/scripts/download_assets.py` targeted search plus supplied runtime | [MEM-OBJ-raw-documents](#mem-obj-raw-documents), [MEM-OBJ-raw-assets](#mem-obj-raw-assets), [RT-CLM-raw-policy](runtime.md#rt-clm-raw-policy). Caption fetch internals and complete asset-rewrite logic not independently read here; visual completeness and extraction fidelity unestablished. |
| GitHub target parse/clone/spec delivery | SRC-1: `plugins/ai-research-os/skills/research/scripts/github_parse_targets.py` output/CLI search; `plugins/ai-research-os/skills/research/agents/builder.md` direct; clone/spec body supplied | [RT-RTE-github-ingest](runtime.md#rt-rte-github-ingest), [MEM-OBJ-repo-specifications](#mem-obj-repo-specifications). Parser completeness and resolved copy delivery unestablished; mutable cache is not a durable immutable code snapshot. |
| Source/entity/concept/overview/thesis construction | SRC-1: `plugins/ai-research-os/skills/research/agents/source_writer.md`, `plugins/ai-research-os/skills/research/agents/wiki_page_writer.md`, `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md` — direct | [MEM-OBJ-source-pages](#mem-obj-source-pages), [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages), [MEM-OBJ-synthesis](#mem-obj-synthesis). Bounded reads and current-run propagation prevent claims of complete accumulated-source integration. |
| Comparison writing | SRC-1: `plugins/ai-research-os/skills/research/agents/comparison_writer.md` direct; dispatch references searched in research driver | [MEM-RTE-comparison-writing](#mem-rte-comparison-writing). Writer affordance is explicit; detailed dispatch is missing from the numbered ingest pipeline. |
| Canonical catalog/navigation, all CLI flags | SRC-1: `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`, `plugins/ai-research-os/skills/research/scripts/build_index_md.py` — direct | [RT-RTE-index-build](runtime.md#rt-rte-index-build), [MEM-OBJ-index-md](#mem-obj-index-md). YAML constructor lacks the documented ingest_log; MD neither updates YAML counts nor enumerates wiki/notes. |
| Query/load/filter/drill/compose and fallback/save | SRC-1: `plugins/ai-research-os/skills/research/SKILL.md` Q.1–Q.5 direct; response continuation supplied runtime | [RT-RTE-query-answer](runtime.md#rt-rte-query-answer), [MEM-OBJ-question-pages](#mem-obj-question-pages), [MEM-BAP-retained-knowledge](#mem-bap-retained-knowledge). Contradictory admission scopes prevent a single compliant save-back recipe. |
| Four mechanical checks, three model checks | SRC-1: `plugins/ai-research-os/skills/research-lint/scripts/_lintlib.py`, `plugins/ai-research-os/skills/research-lint/scripts/lint_orphans.py`, `plugins/ai-research-os/skills/research-lint/scripts/lint_missing_hubs.py`, `plugins/ai-research-os/skills/research-lint/scripts/lint_missing_comparisons.py`, `plugins/ai-research-os/skills/research-lint/scripts/lint_broken_links.py`, driver and judge — direct | [RT-RTE-lint-maintenance](runtime.md#rt-rte-lint-maintenance), [MEM-OBJ-contradictions](#mem-obj-contradictions), [MEM-OBJ-open-questions](#mem-obj-open-questions). Flags do not withdraw claims. Fixed checks inspect body wikilinks, not all citations, anchors or source truth. |
| Corpus-relative export | SRC-1: `plugins/ai-research-os/skills/research-distill/SKILL.md` — direct | [RT-RTE-distill-export](runtime.md#rt-rte-distill-export), [MEM-OBJ-research-appendix](#mem-obj-research-appendix). External writer role is documented, deployed delivery unobserved. |
| Marp/brief/chart/canvas | SRC-1: `plugins/ai-research-os/skills/research-render/SKILL.md`, `plugins/ai-research-os/skills/research-render/agents/marp_writer.md`, `plugins/ai-research-os/skills/research-render/agents/brief_writer.md`, `plugins/ai-research-os/skills/research-render/agents/chart_writer.md`, `plugins/ai-research-os/skills/research-render/agents/canvas_writer.md` — direct | [RT-RTE-render-output](runtime.md#rt-rte-render-output), [MEM-OBJ-render-prose](#mem-obj-render-prose), [MEM-OBJ-chart-script](#mem-obj-chart-script), [MEM-OBJ-canvas](#mem-obj-canvas). Consumers differ: interpretation, executable snapshot, fixed display structure plus prose. |
| Logs, scratch, cleanup and deletion | SRC-1: `plugins/ai-research-os/skills/research/CONVENTIONS.md`, `plugins/ai-research-os/skills/research/SKILL.md` Steps 6.8–7; lint driver — direct | [MEM-OBJ-log](#mem-obj-log). Successful-run JSON cleanup loses selection rationales not propagated into wiki. Raw deletion requires deliberate user action; no inspected automatic claim-withdrawal cascade. |
| External service and host memory | SRC-1: boundary exclusions; supplied model/component records | [RT-CMP-notebooklm-model](runtime.md#rt-cmp-notebooklm-model), [RT-CMP-host-model](runtime.md#rt-cmp-host-model). Opaque provider state, service embedding lineage and host context compaction remain uninspected; they cannot be classified from returned summaries. |

## Core ideas

**Memory is a layered filesystem knowledge product, not a retained conversation.** Catalog summaries select what to read; per-source pages compress source material; entity/concept pages aggregate it; synthesis turns it into an argument. Raw source copies remain drill-down evidence but are not ordinary synthesis-writer input. Later invocations request relevant retained content rather than receiving an unsolicited memory push. SRC-1: `plugins/ai-research-os/skills/research/CONVENTIONS.md`; [RT-RTE-query-answer](runtime.md#rt-rte-query-answer).

> - Original conversation transcripts that produced the research (those live in chat history).
> --- `plugins/ai-research-os/skills/research/CONVENTIONS.md`

**Selection has several different meanings.** Seed score 1.0 records user supply, high/medium becomes 0.8/0.5, and dedup keeps the longest summary. None is a truth or quality oracle. Manual highlights are a distinct higher-signal source layer, not an LLM synopsis. Distill then selects for relevance to a provided content corpus, explicitly not by seed importance. These mechanisms concern different consumers and must not be collapsed into a universal relevance ranking. SRC-1: `plugins/ai-research-os/skills/research/scripts/dedup_findings.py`, `plugins/ai-research-os/skills/research/agents/builder.md`, `plugins/ai-research-os/skills/research-distill/SKILL.md`; [RT-CLM-index-contract](runtime.md#rt-clm-index-contract).

**Reasons survive selectively.** Source pages request original framing, citations and short quotes; synthesis requests assumptions and counter-evidence; lint retains opposing claims and why their conflict matters. Those reasons can reach subsequent summary/query consumers. Discovery gap notes, JSON candidate rationales and dispatch traces are not durably retained by default. Question pages are deliberately thin pointers, not self-contained answers; chart programs freeze numerical inputs rather than re-reading changed wiki bodies. SRC-1: writer prompts cited in the object records below; [RT-RTE-deep-discovery](runtime.md#rt-rte-deep-discovery), [RT-RTE-render-output](runtime.md#rt-rte-render-output).

**Human initiation is not claim approval.** Except for explicit supply, overrides, optional discussion and overwrite choices, the model selects and writes knowledge without per-content review. KEEP preservation is an instruction, not an enforced filesystem veto. Lint criticism is additive and does not automatically withdraw an older assertion. Thus later retrieval can still encounter challenged claims alongside criticism. SRC-1: `plugins/ai-research-os/skills/research/agents/wiki_page_writer.md`, `plugins/ai-research-os/skills/research-lint/agents/lint_judge.md`; [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest), [RT-RTE-lint-maintenance](runtime.md#rt-rte-lint-maintenance).

## Shared records

### Components

none declared in this member

### Operative objects

The objects below have no supplied object counterpart after comparison with the two static objects in runtime. Runtime routes mention their production and consumption but do not declare their retained operative parts. They are distinct outputs, not parts of plugin source. The one generated executable object is compared explicitly with static helpers.

#### MEM-OBJ-index-metadata
Label: index.yaml access and selection metadata

Storage: topic-root YAML. Form: symbolic fields for identities, URIs, score/order, origins, dates, source counts and origin-specific IDs/commit metadata. Lineage: seed/discovery JSON and optionally prior YAML, projected by `normalize_source`; the helper does not validate URI targets. Consumers: subsequent ingest dedup, query filters, distill matching, navigation generation and lint. Behavioral force: selectors and pointers, not a truth certificate. Human seed identity selection is direct supply; remaining fields may be model-proposed, service-returned or caller-supplied. Initial authenticity is unresolved. SRC-1: `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`; [RT-RTE-index-build](runtime.md#rt-rte-index-build).

> def normalize_source(entry: dict) -> dict:
>     """Project a discovery-result or seed entry onto the index.yaml source schema."""
> --- `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`

#### MEM-OBJ-index-summary
Label: index.yaml summary and topic text

Storage: natural-language strings inside the same YAML envelope as metadata. Form: natural language when a query, gap or writing model interprets topic/input_summary/source summary/tags; numerical ordering is a separate part above. Lineage: researcher summaries, seed metadata, service descriptions or explicit user input, retained verbatim/projected by the helper rather than independently synthesized by it. The YouTube helper can supply a first-excerpt summary, so summary provenance is not universally LLM-authored. Later query can stop at this layer; summary writers are directed to load it. Source trust is therefore delegated to upstream summaries, not verified by YAML storage. SRC-1: `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`, `plugins/ai-research-os/skills/research/scripts/youtube_extract_transcript.py`, `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`.

> "summary": f"YouTube caption transcript. First excerpt: {first_excerpt(result.snippets)}",
> --- `plugins/ai-research-os/skills/research/scripts/youtube_extract_transcript.py`

#### MEM-OBJ-index-md
Label: index.md navigation display

Storage: generated Markdown at topic root. Form: natural-language topic, shortened summary and titles for browsing/fallback; symbolic wikilinks, groups and file lists for navigation. Lineage: canonical YAML plus enumerated live wiki paths. It is not an independent source of all metadata: `render_source_line` uses `uri_full`, not `uri_source_page`; the summary is first-sentence/truncated display. Query fallback interprets this reduced view and wiki pages with saves disabled. No counterpart to [RT-OBJ-python-helpers](runtime.md#rt-obj-python-helpers): this is their output, not the generating program. SRC-1: `plugins/ai-research-os/skills/research/scripts/build_index_md.py`; [RT-RTE-index-build](runtime.md#rt-rte-index-build), [RT-RTE-query-answer](runtime.md#rt-rte-query-answer).

> uri_full = src.get("uri_full")
> label = title
> if uri_full:
>     link = wikilink(uri_full, label)
> else:
>     link = title  # nothing to link to
> --- `plugins/ai-research-os/skills/research/scripts/build_index_md.py`

#### MEM-OBJ-raw-documents
Label: Raw source documents and extracted text

Storage: `raw/*.md`. Form: natural-language source text, plus citation/timestamp structure. Lineage differs by source: copied vault notes; fetched/stripped web text; CLI document content; complete NLM note or imported-source text; PDF-extracted Markdown; public captions rendered to timestamped Markdown. “Raw” is relative to later wiki synthesis, not a promise of untransformed upstream bytes. Web extraction, PDF conversion and image localization transform it. Captions omit unspoken visual evidence and may be automatically generated. Later query/distill read deeper layers on demand; source writers read a raw file, potentially only an initial 2000-line chunk. Initial source trust is not enforced by the file type. SRC-1: `plugins/ai-research-os/skills/research/agents/builder.md`, `plugins/ai-research-os/skills/research/agents/source_writer.md`, `plugins/ai-research-os/skills/research/scripts/extract_pdf.py`, `plugins/ai-research-os/skills/research/scripts/youtube_extract_transcript.py`; [RT-CLM-raw-policy](runtime.md#rt-clm-raw-policy).

> This raw source contains the public YouTube caption transcript. It is not an LLM summary and may omit visual-only context that is not spoken in the video.
> --- `plugins/ai-research-os/skills/research/scripts/youtube_extract_transcript.py`

The quoted sentence is the string embedded in the generated raw-document body. NLM note acquisition can write an error sentinel and still name a full-content URI; this is a recipe seam, not observed contamination.

> nlm note get <nlm_source_id> > "<research_dir>/raw/nlm-<slug>.md" 2>&1 || echo "nlm note get failed" > "<research_dir>/raw/nlm-<slug>.md"
> --- `plugins/ai-research-os/skills/research/agents/builder.md`

#### MEM-OBJ-key-highlights
Label: Manually curated key highlights

Storage: separate `raw/*-key-highlights.md` copies selected by `uri_highlights`. Form: natural language, inherited manual excerpts/annotations rather than an LLM-created abstraction. Lineage: purported Readwise-synced vault curation. The human selected highlights upstream; the builder admits/copies them without another individual approval. Their actual original editing history is outside the boundary. A Readwise-synced Obsidian note can be highlight-only with `uri_full: null`; a Readwise source recipe instead requests both highlight and full-document files. Later query and distill distinguish this optional layer from the model-derived source page. SRC-1: `plugins/ai-research-os/skills/research/agents/builder.md`.

> Set `uri_highlights: "raw/<slug>-key-highlights.md"`, `uri_full: null`.
> --- `plugins/ai-research-os/skills/research/agents/builder.md`

#### MEM-OBJ-raw-assets
Label: Original PDFs and image assets

Storage: `raw/assets/<slug>/`. Form: image/document evidence interpreted by humans or multimodal models; filenames/manifests are symbolic access metadata, not the payload. Lineage: downloaded image bytes, copied original PDF and extractor-produced raster images. The PDF helper admits writes computationally, flags low text via average extracted chars per page and renames images; low-quality labeling is not an OCR repair. Source writers view selected representative/referenced images, not all assets; completeness of visual interpretation is unestablished. Direct repeated extraction may delete a colliding image filename, so the no-automatic-deletion doctrine is not an invariant of every helper call. SRC-1: `plugins/ai-research-os/skills/research/scripts/extract_pdf.py`, `plugins/ai-research-os/skills/research/agents/source_writer.md`; [RT-CLM-raw-policy](runtime.md#rt-clm-raw-policy).

> # If a file with new_name already exists from a prior run, remove it.
> if new_path.exists():
>     new_path.unlink()
> --- `plugins/ai-research-os/skills/research/scripts/extract_pdf.py`

#### MEM-OBJ-source-pages
Label: Per-source extended wiki summaries

Storage: `wiki/sources/<slug>.md`. Form: natural-language claims, quotes, distinctive contribution and explicit synthesis, with symbolic frontmatter/links. Lineage: one raw source plus metadata, research intent and selected assets. Curation is model authoring; the writer writes without per-claim human approval. Scope requests source-native framing and citation, not authentication or reliable truth checking. These are the ordinary inputs to entity/concept/comparison writers and the intermediate query/distill layer. Replacement is requested on another writer run; raw content can exceed the writer's actual read range. SRC-1: `plugins/ai-research-os/skills/research/agents/source_writer.md`.

> If the file is very long (>2000 lines), read in chunks — start with the first 2000 lines and only read further if your draft is missing critical content from later sections.
> --- `plugins/ai-research-os/skills/research/agents/source_writer.md`

#### MEM-OBJ-wiki-pages
Label: Entity, concept, comparison and overview pages

Storage: mutable Markdown under corresponding wiki paths. Form: natural-language definitions, aggregated claims, trade-offs and navigation; frontmatter counts/aliases and links are symbolic access parts. Lineage: source pages, assigned page set and prior content; comparisons also read both subjects; overview skims catalog/frontmatter plus selected full pages. They are model-admitted knowledge, not summaries certified by code. Human edits are deliberate overrides; KEEP blocks and aliases request preservation. Consumers include query/compose, next writing pass, lint, distill and render. Confidence is a prompted source-count/disagreement heuristic, not a measured confidence estimate. SRC-1: `plugins/ai-research-os/skills/research/agents/wiki_page_writer.md`, `plugins/ai-research-os/skills/research/agents/comparison_writer.md`, `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`.

> You aggregate from per-source wiki pages. **You never read raw files** — every claim you record must already exist on a source page; if it isn't there, it isn't in the wiki yet.
> --- `plugins/ai-research-os/skills/research/agents/wiki_page_writer.md`

#### MEM-OBJ-synthesis
Label: Retained research thesis

Storage: `wiki/synthesis.md`, mutable natural-language argument with linked supporting moves, assumptions, counter-evidence and revision conditions. Lineage: catalog and selected wiki content, previous synthesis/KEEP blocks and rolling criticism; at most five discretionary full-page reads. Its authority at query/compose and render is research knowledge, not a higher-priority execution instruction. Its requested reasons are inspectable headings, not hidden chain-of-thought. It is distinct from navigation/aggregates above and from the static synthesis-writing instruction. Theory properties belong to [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest); no new theory route is declared here. SRC-1: `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`.

> If you find yourself wanting to read more than 5 full bodies, stop — the wiki is too dense for one pass; write what you can confidently say and flag the rest for the next ingest.
> --- `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`

#### MEM-OBJ-repo-specifications
Label: Curated GitHub architecture and module specifications

Storage: intended `wiki/repos/<repo>/ARCHITECTURE.md` plus module Markdown; upstream code in sibling mutable `.github-cache/`, not a raw-directory snapshot. Form: natural-language curated specifications plus symbolic module/code links and pinned commit metadata. Lineage: model reading cloned code/documents at reported HEAD and selected paths; source-reading budgets and scope are supplied by [RT-RTE-github-ingest](runtime.md#rt-rte-github-ingest). Query/distill follow architecture-to-module links, not separately indexed modules. Thus `uri_full` is a curated hub, not complete repository content. Copy destination conflict and mutable cache prevent claiming reliable immutable local delivery; metadata pinning is not locking. SRC-1: `plugins/ai-research-os/skills/research/agents/builder.md`, `plugins/ai-research-os/skills/research/CONVENTIONS.md`; supporting clone/copy passages in [RT-RTE-github-ingest](runtime.md#rt-rte-github-ingest).

#### MEM-OBJ-question-pages
Label: Slim saved-question pointers

Storage: dated `wiki/questions/*.md`, symbolic answer_doc/source pointers wrapped in natural-language verbatim question, significance and brief coverage bullets. Lineage: answered user question plus model save decision. The user can bookmark; alternatively two-source citation count triggers model admission. A page is not itself the substantive answer, which Q.5 asks to enrich elsewhere. Later query and human navigation can follow the pointer; landing scope conflicts prevent claiming a consistent compliant knowledge write. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md`; [RT-RTE-query-answer](runtime.md#rt-rte-query-answer), [RT-CLM-query-safety](runtime.md#rt-clm-query-safety).

> - **Use referencing, not copying.** The question page exists so future agents can ask "what questions has the user asked?" cheaply, not to re-explain answers.
> --- `plugins/ai-research-os/skills/research/SKILL.md`

#### MEM-OBJ-contradictions
Label: Rolling contradiction findings

Storage: append-only requested `wiki/contradictions.md`; natural-language opposing source claims, subject, why resolution matters and explicit synthesis, with symbolic citation links. Lineage: model judge interprets eligible wiki Tensions sections, compares against prior findings and admits nonduplicates automatically. Later summary writer explicitly reads this file; query and brief/render contexts can select it where relevant. It is retained criticism, not a withdrawal of either claim or a measured evaluator score. Reasons can shape later thesis-writing, but actual revision/changed reliance remains unobserved. SRC-1: `plugins/ai-research-os/skills/research-lint/agents/lint_judge.md`; supporting retention passage and theory limits in [RT-RTE-lint-maintenance](runtime.md#rt-rte-lint-maintenance).

#### MEM-OBJ-open-questions
Label: Rolling research gaps

Storage: `wiki/open-questions.md`; natural-language investigations with dates and source/wiki pointers. Lineage: entity/concept writer outputs during ingest, model lint gap synthesis, or an explicitly user-flagged follow-up query. Admission differs: computational automatic append for ingest/lint versus user-requested query append. No routine human per-question approval in the former. Summary writer reads the file; query can inspect it; lint calls these questions seeds for another ingest, but automatic discovery scheduling is not wired by that statement. It keeps criticism/context, not a promise of resolution. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md` Step 6.6 and Q.5; `plugins/ai-research-os/skills/research-lint/agents/lint_judge.md`; [RT-RTE-lint-maintenance](runtime.md#rt-rte-lint-maintenance).

#### MEM-OBJ-log
Label: Operation log and transient findings

The durable part is `log.md`: append-only requested natural-language operation summaries with symbolic date/op prefix and counts. It is derived operational metadata, not the original conversation or a full tool trace. Discovery/round/augment JSONs and lint JSONs are separate temporary symbolic envelopes with natural-language findings; successful ingest deletes top-level JSONs and lint permits deletion after review. Runtime discovery consumers use them within the current run; no inspected automatic log-to-durable-guidance transformation is established in the research/write/lint drivers. Chart guidance allows an ingest-log tally as data, but the canonical YAML constructor does not emit ingest_log, leaving that data path unresolved. This bounded result does not exclude manual log inspection or host trace memory. SRC-1: `plugins/ai-research-os/skills/research/CONVENTIONS.md`, `plugins/ai-research-os/skills/research/SKILL.md` Steps 6.8–7, `plugins/ai-research-os/skills/research-lint/SKILL.md`, `plugins/ai-research-os/skills/research-render/agents/chart_writer.md`, `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`.

> After the research directory is built successfully, delete intermediary JSONs that live alongside the canonical artifacts (top-level only — `raw/` and `wiki/` are recursed into for nothing here):
> --- `plugins/ai-research-os/skills/research/SKILL.md`

#### MEM-OBJ-research-appendix
Label: Corpus-relative research.md appendix

Storage: Markdown beside user content, outside the research directory. Form: natural-language compact claims/quotes/nuances/match reasons, with exact symbolic identity/URI envelope. Lineage: corpus-relative matching against catalog and layered source reads; body construction starts at source pages, then highlights/full/summary fallback. User seeds are not auto-admitted; model selects matches, excludes borderline cases and reports them for human reconsideration. Documented later consumer is a writer agent that can use retained quotations and drill-down pointers; delivery to such a writer is afforded, not observed. The metadata-only missing-body alternative retains pointers without fabricating source content. SRC-1: `plugins/ai-research-os/skills/research-distill/SKILL.md`; [RT-RTE-distill-export](runtime.md#rt-rte-distill-export).

> The output is a working appendix sized for a writer agent's context window, not a verbatim mirror of the research directory.
> --- `plugins/ai-research-os/skills/research-distill/SKILL.md`

#### MEM-OBJ-render-prose
Label: Marp slides and brief prose

Storage: `wiki/renders/marp/*.md` and `wiki/renders/briefs/*.md`; natural-language derivative presentations with symbolic render metadata/configuration. Lineage: all assigned wiki pages and user framing. Models author/admit prose; user chooses format and can veto overwrite, but does not ordinarily approve each claim. Consumers: people viewing slides or pasting brief into a draft; documented further content workflow can use the brief as an idea seed. Grounding is slide footer/brief footer rather than raw evidence. Brief's three new questions are presentation content, not automatic append to rolling gaps. Noop tests prompt and source paths, not refreshed source bodies. SRC-1: `plugins/ai-research-os/skills/research-render/agents/marp_writer.md`, `plugins/ai-research-os/skills/research-render/agents/brief_writer.md`; [RT-RTE-render-output](runtime.md#rt-rte-render-output).

#### MEM-OBJ-chart-script
Label: Chart executable snapshot and PNG

Storage: companion `.py` and `.png` in `wiki/renders/charts/`. Form: symbolic program/data consumed by Python; metadata comments are readable provenance, and PNG is visual display output interpreted by people/models, not an opaque retained numerical memory. Lineage: model selects numerical data from wiki/catalog and embeds it as constants. The Python runtime need not read wiki at re-execution; this is a frozen content snapshot until actual regeneration. Distinct from [RT-OBJ-python-helpers](runtime.md#rt-obj-python-helpers): generated output rather than shipped fixed helper. User chooses render framing/overwrite; model chooses values/program and driver requests execution without separate code review. Effects follow [RT-BAP-helper-execution](runtime.md#rt-bap-helper-execution), not wiki text interpretation. SRC-1: `plugins/ai-research-os/skills/research-render/agents/chart_writer.md`; snapshot passage in [RT-RTE-render-output](runtime.md#rt-rte-render-output).

#### MEM-OBJ-canvas
Label: Canvas structure, text and provenance sidecar

Storage: `.canvas` JSON plus `.canvas.meta.yaml` in `wiki/renders/canvases/`. Symbolic nodes/edges/layout/file references are consumed by Obsidian display rules; node text and relationship labels are natural-language derived knowledge. Lineage: model reads assigned wiki pages and chooses a map; embeds/links can expose existing files while inline text remains a snapshot. Sidecar stores selected paths/prompt/time, not a copy of source evidence or validated dependency graph. The user/viewer is the documented consumer; actual rendering and vault-relative path resolution unobserved. Model authors and admits map relationships; human controls format and overwrite. SRC-1: `plugins/ai-research-os/skills/research-render/agents/canvas_writer.md`.

> - **`file` nodes use vault-relative paths** (e.g., `wiki/concepts/agent-loop.md`). Obsidian resolves them when the canvas is opened from inside a vault that contains the research dir.
> --- `plugins/ai-research-os/skills/research-render/agents/canvas_writer.md`

### Routes

#### MEM-RTE-comparison-writing
Label: Comparison writer admission

Endpoints: requested/detected pair and framing → subject-page reads → shared/source-specific evidence selection → model comparison/refusal → retained comparison Markdown and JSON return. Owner: host-dispatched model writer. The static writer is an afforded operation, not evidence of dispatched production. No supplied route has this exact bounded referent: it overlaps wiki admission in [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest), Q.5 comparison landing in [RT-RTE-query-answer](runtime.md#rt-rte-query-answer) and comparison flags in [RT-RTE-lint-maintenance](runtime.md#rt-rte-lint-maintenance), but is not contained exclusively in one. SRC-1: `plugins/ai-research-os/skills/research/agents/comparison_writer.md`, `plugins/ai-research-os/skills/research-render/SKILL.md`.

- Immediate return: JSON action/counts/verdict and output path, or refusal with reason.
- Later read-back: Comparison page can be selected by query/compose, overview/thesis or render in a later invocation.
- Delegated visibility: Both subjects in full; all shared source pages in full; distinctive/connections sections of nonshared source pages; no raw reads.
- Selection predicate: Pair supplied by caller; shared sources prioritized. Missing subject aborts; no shared sources plus fewer than four nonshared sources requests refusal.
- Invalidation or expiry: Same body ignoring last_updated requests noop; otherwise replacement retaining created and KEEP blocks. No TTL specified.
- Activation or effect: Requested comparison write and later content interpretation; exercised dispatch and changed later decisions unobserved.
- Evidence limits: Driver advertises comparison production, but numbered ingest steps/reference lack explicit comparison-writer dispatch; lint recommends an unsupported render comparison format.
- design conclusion status: claimed
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Admission: caller proposes pair/frame; model decides substance, can refuse thin evidence and physically writes the page. Human initiation or choosing a candidate is not per-claim approval. No answer oracle supplied. Operating mode: open comparison task with evidence/length gates, not scored improvement experiment. Guidance requests trade-offs, use-case fit, source links and honesty when subjects are orthogonal; retained result is sourced content and synthesis verdict, not plugin machinery. Recovery: refusal followed by more sources/rerun; no transaction or rollback specified. This route formulates comparative knowledge but is not independently asserted to satisfy theory-builder conditions; any future theory assessment needs the produced argument and reliance evidence rather than its verdict label.

> - **Refuse rather than fabricate.** If `shared_sources` is empty AND `a_only_sources + b_only_sources < 4`, refuse: the wiki is too thin for this comparison. The orchestrator will retry after more sources are ingested.
> --- `plugins/ai-research-os/skills/research/agents/comparison_writer.md`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-retained-knowledge
Label: Retained research to later model context

Consumer: later query model, wiki writers/judge and distill/render model. Channel: catalog-first requested reads and delegated selected file paths/bodies. Force: knowledge/evidence and prior content to preserve or revise; it does not become a system instruction merely because Markdown enters context. Horizon: later invocations across sessions using the same topic directory. Content inclusion is afforded; reliable influence, improved capacity and truth remain unobserved. Distinct from [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance): accumulated research, not static procedural authority. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md` Q.2–Q.4, `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`, `plugins/ai-research-os/skills/research-lint/agents/lint_judge.md`.

> For any source, read in this order and stop when the user's question is answered:
> --- `plugins/ai-research-os/skills/research/SKILL.md`

#### MEM-BAP-keep-preservation
Label: Human overrides at wiki rewrite

Consumer: later entity/concept, summary and comparison writers. Channel: existing-page read plus KEEP markers and user-added aliases. Force: requested verbatim preservation within model rewriting, not mandatory write interception. Horizon: subsequent eligible page revisions while markers remain. Distinct from [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance): the static instruction grants preservation force to accumulated user edits; the actual override text is retained content. This does not establish every page type preserves edits: source writer separately requests overwrite. SRC-1: `plugins/ai-research-os/skills/research/agents/wiki_page_writer.md`, `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`, `plugins/ai-research-os/skills/research/agents/comparison_writer.md`, `plugins/ai-research-os/skills/research/agents/source_writer.md`; verbatim preservation passage in [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest).

## Annotations

#### On [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest)

Memory curation chain: copied/extracted source → model source page → selected entity/concept aggregation → bounded overview/thesis → catalog/navigation. Storage is filesystem content, not parameter updates. The source writer's desired completeness is constrained by conditional continuation beyond 2000 lines; the entity/concept writer only sees assigned current source-page paths plus prior page. Step 6.4 counts current source-writer outputs, not all historical source pages. Consequently one new mention in an append need not trigger a previously single-mentioned entity, and a rewritten existing page may lean on its old body rather than freshly reread old backing sources. This qualifies compounding coverage without claiming observed loss. Human discussion can stop propagation after source pages already exist, so dropping a source at that checkpoint is not necessarily catalog/source withdrawal. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md` Steps 6.3.5–6.4; `plugins/ai-research-os/skills/research/agents/source_writer.md`, `plugins/ai-research-os/skills/research/agents/wiki_page_writer.md`.

> Source pages that have already been written stay; you just don't propagate their entities/concepts to the wiki layer.
> --- `plugins/ai-research-os/skills/research/SKILL.md`

#### On [RT-RTE-index-build](runtime.md#rt-rte-index-build)

Retained catalog normalization preserves prior sources only when supplied; missing pointers remain null and metadata is not validated against files. The constructor replaces the document and carries sources, not previous ingestion-history entries. Only `rounds_completed` for this invocation is emitted. Markdown reads YAML and selected tree paths, produces navigation, and does not update YAML `total_wiki_pages`; its displayed meta lines omit that count. It also omits the Q.5 `wiki/notes/` catch-all from enumerated subdirs. Thus regeneration can expose questions/renders without refreshing canonical counts, and a cross-cutting knowledge note can be reachable only through links rather than direct navigation. SRC-1: `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`, `plugins/ai-research-os/skills/research/scripts/build_index_md.py`, `plugins/ai-research-os/skills/research/SKILL.md` Q.5.

#### On [RT-RTE-query-answer](runtime.md#rt-rte-query-answer)

Read-back is a requested pull: question/depth/filter inputs select relevant catalog rows or directly named wiki subjects, then progressively deliver summary → source page → manual highlights → full source if needed. There is no fixed global token limit; “top N” source-page load has no specified numerical N. Full depth applies to specified sources, not every retained source. Another skill receives selected YAML-shaped results; ordinary answer delivery is not itself later read-back unless admitted into files. Missing-YAML fallback is a lower-information alternative, with all saves/log/navigation writes disabled. Normal save-back can retain a pointer plus a knowledge doc, but the existing scope conflict blocks a single reliable admission contract. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md` Q.2–Q.5; [RT-CLM-query-safety](runtime.md#rt-clm-query-safety).

#### On [RT-RTE-lint-maintenance](runtime.md#rt-rte-lint-maintenance)

Read-back at the updater is wiki criticism, not raw-source verification: eight full pages maximum, source-count/date/Tensions predicates and previous findings control admission. Contradictions/gaps persist with reasons; stale flags do not rewrite a challenged claim. Direct mechanical inspection narrows evaluation semantics: orphan checks body links to full/highlight/source-page pointers and skips rows with no pointer; missing hubs counts body entity/concept wikilinks, not free-text mentions or candidate JSON; comparisons requires one link each way; broken links drops anchors/labels and tests target file existence. None validates claim truth or anchor existence. SRC-1: all four `plugins/ai-research-os/skills/research-lint/scripts/lint_*.py` files named in coverage and `plugins/ai-research-os/skills/research-lint/scripts/_lintlib.py`; `plugins/ai-research-os/skills/research-lint/agents/lint_judge.md`.

> if not candidates:
>     continue  # No file => can't be orphan in the wiki sense; skip.
> --- `plugins/ai-research-os/skills/research-lint/scripts/lint_orphans.py`

The source writer forbids new links to absent entities/concepts, while the missing-hub checker relies on precisely those links. It therefore cannot recover candidate suggestions erased with JSON cleanup merely from ordinary free-text mentions. This prevents reading “missing hubs” as comprehensive missed-promotion detection. SRC-1: `plugins/ai-research-os/skills/research/agents/source_writer.md`, `plugins/ai-research-os/skills/research-lint/scripts/lint_missing_hubs.py`.

#### On [RT-RTE-distill-export](runtime.md#rt-rte-distill-export)

Selection for matching and selection for body composition differ. Traceable-idea matching prefers highlights, otherwise full text, otherwise summary; composition starts at model-derived source page. Metadata/URI/quote preservation is requested, not guaranteed by a parser. Output reasons explain corpus match, not proof that an author actually used the source. The corpus includes guidelines/outlines as well as finished drafts, so “used in final content” can include an outline-only reference. Budget is roughly 300 words per source, 500 for GitHub; no total appendix cap. Later writer consumption is a documented role, not deployed automatic delivery. SRC-1: `plugins/ai-research-os/skills/research-distill/SKILL.md`.

#### On [RT-RTE-render-output](runtime.md#rt-rte-render-output)

Selected wiki files and framing control derived content. Marp/brief are natural-language snapshots; charts persist executable fixed data and derived pixels; canvas separates structure, interpreted text and access metadata. Navigation includes all render-directory files except chart Python, so canvas metadata sidecars can appear as navigation entries. Renders do not enter the catalog sources array. The identical prompt/path noop predicate cannot detect changed bodies; chart's fresh-rerender guidance is conditional on bypassing that noop. Brief refuses before writing when required coverage exceeds its length gate; canvas targets at most 20 nodes, decks at most 25 slides unless requested, charts disclose thin data. These are prompted budgets, not enforced runtime context limits. SRC-1: `plugins/ai-research-os/skills/research-render/SKILL.md`, all four format prompts; `plugins/ai-research-os/skills/research/scripts/build_index_md.py`.

## Write side

Acquisition starts with user seeds or model-selected discovery findings; it is not a single human-owned write channel. Dedup/scoring is deterministic computational selection, then builder shell recipes perform physical I/O, then models author wiki claims. Human bookmarks, optional discussion redirects and deliberate KEEP overrides have narrower admission scopes. Software helpers accept caller content/paths rather than verifying truth. Initial model/service provenance remains unresolved locally while the subsequent transformations are inspectable. SRC-1: `plugins/ai-research-os/skills/research/scripts/dedup_findings.py`, `plugins/ai-research-os/skills/research/agents/builder.md`; [RT-RTE-deep-discovery](runtime.md#rt-rte-deep-discovery), [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest).

| Write mechanism | Admission control distinct from authorship/I/O | Retained result and later consumer |
|---|---|---|
| Explicit seed ingest | Human supplies source identity/problem; model admission of formulated claims is automatic under writer guidance; helpers copy/transform | [MEM-OBJ-raw-documents](#mem-obj-raw-documents), [MEM-OBJ-source-pages](#mem-obj-source-pages) → subsequent wiki/query/distill. |
| Deep discovery and dedup | User selects mode/depth; researchers select candidates; longest-summary helper picks identity winner; model writers admit knowledge | Catalog and wiki objects → later query/write; intermediate findings/gap reasons cleaned unless propagated. |
| Highlight copies | Human curation asserted upstream; builder copies without renewed per-highlight approval | [MEM-OBJ-key-highlights](#mem-obj-key-highlights) → query/distill; independent full document may be null. |
| PDF/caption/assets conversion | Caller provides source/paths; software admits extraction and writes; model decides later interpretive claims | Raw text/assets → source writer; selected visual reads and caption-only limits retained. |
| GitHub curated specs | Human supplies repo/path scope; model chooses spec content; helper/cache and builder perform I/O | [MEM-OBJ-repo-specifications](#mem-obj-repo-specifications) → architecture-to-module query/distill; delivery seam unresolved. |
| Wiki aggregation/thesis/comparison | Model authors and admits; optional user redirect/KEEP has local preservation force; count/insufficient-evidence gates are guidance | [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages), [MEM-OBJ-synthesis](#mem-obj-synthesis) → subsequent writing/query/render. |
| Query save | Explicit human bookmark OR automatic model two-source trigger; scope conflict unresolved | [MEM-OBJ-question-pages](#mem-obj-question-pages) plus proposed knowledge-doc enrichment → later readers. |
| Maintenance findings | Model admits nonduplicate criticism/gaps; human decides stale-claim/orphan/link resolutions | Rolling findings → summary/query; mechanical JSON is report scratch, not repaired knowledge. |
| Appendix | User supplies corpus; model selects and admits compact source blocks; optional manual additions | [MEM-OBJ-research-appendix](#mem-obj-research-appendix) → documented writer role. |
| Render | User selects format/framing/overwrite; model admits prose/map/program; orchestrator executes chart | Separate render objects → viewer/draft workflow/Python rerun. |

This table relies on the cited route/object records, not successful runs. Raw→derived→later-consumer chains preserve external-source knowledge; they are not automatic learning from agent execution traces. Query save retains a result of an interaction, but deliberately not the original conversation. Logs preserve operational summaries; inspected instructions do not establish an automatic log-driven update to plugin guidance. Criticism reasons can feed synthesis; retaining them does not prove improved future capacity or autonomous correction. SRC-1: `plugins/ai-research-os/skills/research/CONVENTIONS.md`, `plugins/ai-research-os/skills/research/SKILL.md`, `plugins/ai-research-os/skills/research/agents/wiki_summary_writer.md`; theory/learning limits in [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest), [RT-RTE-lint-maintenance](runtime.md#rt-rte-lint-maintenance).

Rejection acts at several stages: known identities skipped; discovery candidates filtered/capped; fetch failures skipped or fall back; entity/concept mentions may not cross propagation threshold; comparison refuses thin inputs; unsaved queries return only; brief requests guidance before writing. Rejection does not imply raw deletion or removal of previously written source pages. Successful ingest deletes intermediate top-level JSONs, including metadata alternatives used to carry URIs, and removes the prior-index snapshot; no durable multi-file rollback checkpoint is specified. Lint appends criticism and explicitly keeps old entries; source withdrawal requires deliberate user deletion/repair and no inspected automatic cascade restores catalog, links and claims together. SRC-1: builder, comparison, brief and cleanup prompts cited above; [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest), [RT-RTE-lint-maintenance](runtime.md#rt-rte-lint-maintenance).

## Read-back

| Later invocation / consumer | Selector input, retained part and delivery | Budget, authority and status |
|---|---|---|
| Append/deep updater | Existing catalog original_path set and created; prior pages/aliases/KEEP; assigned new source-page lists | Dedup identities are symbolic selection; prior content is preservation/knowledge context. Afforded prompt reads; carry-forward code wired when supplied. |
| Query/load/filter/compose | Question, topic match, origin/score/tag/date/author/repo filters and depth select catalog rows/wiki subjects, then pointers | Progressive disclosure; no bulk full reads; unspecified top N. Knowledge context, not procedural authority. Afforded, operation uninspected. |
| Missing-YAML fallback | Topic navigation and displayed summaries in index.md plus wiki overview/thesis | Less metadata; writes disabled. Afforded, no equivalent canonical filtering guarantee. |
| Summary writer | Catalog summaries, source frontmatter and first 40 lines of entity/concept files, full rolling criticism/gaps, selected full pages | Five discretionary full-page reads; new argument uses derived knowledge/criticism. Afforded, actual coverage unobserved. |
| Lint judge/checkers | Wiki body links, Tensions/Open questions, source counts/dates, prior rolling findings | Eight full judge pages and ten new gap questions; fixed mechanical predicates wired; semantic admission afforded. |
| Distill / documented writer | Content corpus matches catalog/source layers → retained compact appendix with match reasons and pointers | Soft per-source cap, not global token cap; exported knowledge for a writer, deployed delivery unobserved. |
| Render/viewer/Python | User prompt and selected wiki paths → derivative prose/map/data snapshot, indexed navigation | Format budgets; chart rerun uses embedded constants, not current wiki. Afforded model generation/execution request; actual consumption unobserved. |

Each row is supported by the corresponding annotations and their source anchors. These are user/skill-requested pulls or within-request derived deliveries. The inspected plugin dispatch/build/query/lint/render paths do not establish independently triggered unsolicited memory supply; static skill loading belongs to [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance), not accumulated read-back. Requests to read rolling findings at a subsequent writing invocation are selectors with a trigger, not an autonomous maintenance scheduler. SRC-1: `plugins/ai-research-os/skills/research/SKILL.md`, `plugins/ai-research-os/skills/research-lint/SKILL.md`, `plugins/ai-research-os/skills/research-render/SKILL.md`.

## Integration issues

1. **Catalog counts/history:** augment [RT-RTE-index-build](runtime.md#rt-rte-index-build), [RT-RTE-query-answer](runtime.md#rt-rte-query-answer), [RT-RTE-render-output](runtime.md#rt-rte-render-output) and [MEM-OBJ-index-metadata](#mem-obj-index-metadata). `build_index_yaml.py` emits current rounds_completed, no ingest_log; `build_index_md.py` neither writes YAML nor computes a live total_wiki_pages. Render Step 5 explicitly claims the latter; query/lint/render regeneration therefore does not implement the conventions' count update by itself. Analytical consequence: catalog page counts/history may be stale/missing; chart ingest-log selection is unresolved, though directory enumeration is implemented. SRC-1: `plugins/ai-research-os/skills/research/scripts/build_index_yaml.py`, `plugins/ai-research-os/skills/research/scripts/build_index_md.py`, `plugins/ai-research-os/skills/research-render/SKILL.md`, `plugins/ai-research-os/skills/research/CONVENTIONS.md`.
2. **Comparison dispatch:** [MEM-RTE-comparison-writing](#mem-rte-comparison-writing) is new and distinct, overlapping three supplied routes rather than duplicating one. Writer exists and render advertises research production, but numbered ingest does not dispatch it; lint's suggestion `/research-render comparison` is not among four supported formats. Consequence: comparison generation is afforded at the writer surface, not a demonstrated integrated route. SRC-1: `plugins/ai-research-os/skills/research/agents/comparison_writer.md`, `plugins/ai-research-os/skills/research/SKILL.md`, `plugins/ai-research-os/skills/research-lint/SKILL.md`, `plugins/ai-research-os/skills/research-render/SKILL.md`.
3. **Query landing and navigation:** retain runtime's write-scope conflict, adding that Q.5 wiki/notes is neither a declared conventional page type nor an enumerated navigation subdir. A question link can still point there; it is not guaranteed absent content. Concerns [RT-CLM-query-safety](runtime.md#rt-clm-query-safety), [MEM-OBJ-question-pages](#mem-obj-question-pages), [MEM-OBJ-index-md](#mem-obj-index-md). SRC-1: `plugins/ai-research-os/skills/research/SKILL.md`, `plugins/ai-research-os/skills/research/CONVENTIONS.md`, `plugins/ai-research-os/skills/research/scripts/build_index_md.py`.
4. **Raw helper scope:** strengthen [RT-CLM-raw-policy](runtime.md#rt-clm-raw-policy) with PDF image-collision deletion and potential NLM note error sentinel. This does not retract post-ingest policy but prevents invariant claims across direct helper/builder calls. Concerns [MEM-OBJ-raw-assets](#mem-obj-raw-assets), [MEM-OBJ-raw-documents](#mem-obj-raw-documents). SRC-1: `plugins/ai-research-os/skills/research/scripts/extract_pdf.py`, `plugins/ai-research-os/skills/research/agents/builder.md`.
5. **Compounding coverage:** current-run source-writer outputs determine mention thresholds, source read continuation is conditional, and missing-hub detection depends on prohibited dangling candidate links. Consequence: known catalog sources do not imply comprehensive cross-run wiki integration or comprehensive promotion repair. Concerns [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest), [RT-RTE-lint-maintenance](runtime.md#rt-rte-lint-maintenance), [MEM-OBJ-source-pages](#mem-obj-source-pages), [MEM-OBJ-wiki-pages](#mem-obj-wiki-pages). SRC-1: `plugins/ai-research-os/skills/research/SKILL.md`, `plugins/ai-research-os/skills/research/agents/source_writer.md`, `plugins/ai-research-os/skills/research-lint/scripts/lint_missing_hubs.py`.
6. **Existing seams retained:** raw-URI augmentation handoff, summary reads before catalog refresh, GitHub copy destination/cache race, query save scope, and render same-path stale noop remain unresolved exactly at their source boundaries. Concerns [RT-RTE-append-ingest](runtime.md#rt-rte-append-ingest), [RT-RTE-index-build](runtime.md#rt-rte-index-build), [RT-RTE-github-ingest](runtime.md#rt-rte-github-ingest), [RT-RTE-query-answer](runtime.md#rt-rte-query-answer), [RT-RTE-render-output](runtime.md#rt-rte-render-output). Their supplied supporting passages suffice; none is promoted to an observed failure.
7. **Duplicate review:** no new record is intended to replace a supplied referent. Retained output objects are distinct from static instructions/helpers; the two memory authority paths differ from static guidance by accumulated content/override channel. Chart execution remains annotated on the supplied render/helper authority rather than duplicated. See [MEM-OBJ-chart-script](#mem-obj-chart-script), [MEM-BAP-retained-knowledge](#mem-bap-retained-knowledge), [MEM-BAP-keep-preservation](#mem-bap-keep-preservation). Later peer objects may overlap these referents; no peer member was supplied for comparison.

## Limitations and checks

The source pin and run identities were rechecked against supplied boundary/runtime. Required type, collection, worker and record contracts were read completely; method identity is the supplied job/type contract, not an inferred engine configuration. No source or coordinator-owned file was mutated, no other worker launched and no prior analysis read. Available uninspected discovery/connector/cache implementation details are not called access gaps or absences. Opaque host/provider state and external source authorship prevent complete lineage/control conclusions there. No execution evidence establishes activation, compliance, improved capacity, quote fidelity, successful rollback or durable citation correctness. Form and quotation validation cannot decide those claims.

Deterministic validation: passed using the supplied validate-output invocation; this checks form, quotation occurrence and invocation identity, not semantic acceptance.
