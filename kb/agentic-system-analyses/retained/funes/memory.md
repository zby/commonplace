---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Funes memory mechanisms: source-preserving file compilation, wiki-first read-back, output filing and editorial maintenance."
run-id: AAS-2026-10-15-funes-a9e6dbb3946a-01
source-identity: https://github.com/ulyssestenn/funes
reviewed-boundary: 3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11
---

# Funes memory report

## Boundary and evidence

The memory boundary is the complete shipped library lifecycle: instruction loading and setup, raw acquisition and extraction, compilation, navigation, question answering, output filing, editorial repair and mechanical evaluation. The frozen source is SRC-1 at the revision above, registered in [boundary](boundary.md#source-register). Its empty starter library specifies storage locations, not populated memory or successful operation. The external agent, model window, provider state, extraction dependencies and linked example library remain outside this evidence boundary. No target program or example was executed.

I directly read root `AGENTS.md`, `README.md`, `library.md`, `protocol.md`, every tracked starter-library file, all four Python tools, `tools/README.md`, `tools/requirements-youtube.txt` and `.github/workflows/funes-lint.yml` under SRC-1. I checked the tracked tree, HEAD and clean checkout. Runtime findings below are supplied findings, independently checked against those source files where consequential. Implementation evidence establishes helper transformations and audit rules; natural-language instructions establish requested Librarian actions. The historical account in `tools/compile_lint.py` is reported operation, not a supplied trace. There is no added source or expanded boundary.

### Coverage inventory

| Entry point or operation | SRC-1 paths directly inspected | Covering records and limits |
|---|---|---|
| Agent entry and library creation | `AGENTS.md`, `starter-library/AGENTS.md`, `library.md`, `README.md` | [RT-OBJ-protocol](runtime.md#rt-obj-protocol), [RT-RTE-library-setup](runtime.md#rt-rte-library-setup), [RT-BAP-librarian-instructions](runtime.md#rt-bap-librarian-instructions); host instruction loading and model context policy uninspected. |
| Chat ingest, dropped files, URL/paste fallback, image transcription | `protocol.md`, `starter-library/README.md`, `starter-library/raw/assets/README.md`, `starter-library/raw/INDEX.md` | [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile), [MEM-OBJ-raw-originals](#mem-obj-raw-originals), [MEM-OBJ-text-editions](#mem-obj-text-editions), [MEM-OBJ-source-registry](#mem-obj-source-registry); requested writes, not observed acquisition. |
| PDF CLI, public callable extraction functions and flags | `tools/pdf_text.py`, `tools/README.md`, `protocol.md` | [RT-RTE-pdf-sidecar](runtime.md#rt-rte-pdf-sidecar), [MEM-OBJ-text-editions](#mem-obj-text-editions); native/OCR/failed-page variants included. No automatic compile caller in the helper. |
| Caption CLI, list-only mode, serialization and output helper | `tools/youtube_transcript.py`, `tools/requirements-youtube.txt`, `tools/README.md` | [RT-RTE-caption-fetch](runtime.md#rt-rte-caption-fetch), [MEM-OBJ-text-editions](#mem-obj-text-editions); saved captions can be ingested, but no automatic registry or later wiki consumer is wired by this CLI. Track lists are access metadata, not transcript content. |
| Source abstraction, concept merge, topic organization | `protocol.md`, `starter-library/wiki/sources/README.md`, `starter-library/wiki/concepts/README.md`, `starter-library/wiki/topics/README.md` | [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile), [MEM-OBJ-source-notes](#mem-obj-source-notes), [MEM-OBJ-concepts](#mem-obj-concepts), [MEM-OBJ-topics](#mem-obj-topics); no compiled instances supplied. |
| Wiki-first query and deliberate cross-library navigation | `protocol.md`, `starter-library/wiki/INDEX.md` | [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer), [MEM-OBJ-wiki-index](#mem-obj-wiki-index), [MEM-BAP-wiki-evidence](#mem-bap-wiki-evidence); agent chooses files; no fixed token budget or automatic context push. |
| Saved answer and offered filing-back | `protocol.md`, `starter-library/outputs/README.md`, `README.md` | [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer), [MEM-OBJ-outputs](#mem-obj-outputs); wording differs on whether filing is automatic, discussed below. |
| Editorial audit, safe repair, proposals, session closure | `protocol.md`, `starter-library/meta/health/README.md`, `starter-library/meta/CHANGELOG.md` | [RT-RTE-health-audit](runtime.md#rt-rte-health-audit), [MEM-OBJ-health-reports](#mem-obj-health-reports), [MEM-OBJ-changelog](#mem-obj-changelog); retained reports/logs have no specified automatic reload. |
| Mechanical evaluation, strict variant, CI caller | `tools/check_links.py`, `tools/compile_lint.py`, `.github/workflows/funes-lint.yml` | [RT-RTE-health-audit](runtime.md#rt-rte-health-audit); read-only evaluators return findings/status, not knowledge revisions or stored pass certificates. |
| Other model/service/hook/tool drivers | complete tracked tree and executable tools above | [RT-ABS-model-driver](runtime.md#rt-abs-model-driver); no additional registered tool, hook, server or model driver found within that bounded tree. Functions in the helpers expose the same extraction/audit operations, not a separate memory loop. External host integrations remain uninspected. |

## Core ideas

1. **Preserve originals, derive reusable prose.** The original, machine-readable edition, source note and merged concept are different retained parts. A compiled concept can combine sources and material caveats; an extraction sidecar merely makes a binary readable. Treating either as the original would conceal transformation risk. See [MEM-OBJ-raw-originals](#mem-obj-raw-originals), [MEM-OBJ-text-editions](#mem-obj-text-editions), [MEM-OBJ-concepts](#mem-obj-concepts).
2. **Navigation mediates later context.** Later questions trigger agent-selected INDEX → sources → concepts reading, not a vector search service or a passive dump of all retained content. Topic maps, backlinks and advertised cross-library connections guide subsequent choices. Selection is natural-language agent judgment; filenames and status strings do not implement retrieval ranking. See [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer), [MEM-OBJ-wiki-index](#mem-obj-wiki-index).
3. **Knowledge authority is not instruction authority.** Wiki prose is intended evidence for answers and maintenance, while local AGENTS and protocol tell the agent how to operate. Citations provide a route to supporting documents, not entailment checks or guaranteed immunity to source instructions. See [MEM-BAP-wiki-evidence](#mem-bap-wiki-evidence) and [RT-BAP-librarian-instructions](runtime.md#rt-bap-librarian-instructions).
4. **Evaluation does not itself curate the library.** Linters consume selected file content and return diagnostics. The Librarian must interpret findings, redo shallow compilation, merge or fix safe items, or propose changes. Dated health reports and changelog records are retained, but retaining them does not establish an automatic trace-to-method update. See [RT-RTE-health-audit](runtime.md#rt-rte-health-audit), [MEM-OBJ-health-reports](#mem-obj-health-reports).

The load-bearing source instructions for abstraction, grounding and retrieval are quoted in [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile), [RT-CLM-library-guarantees](runtime.md#rt-clm-library-guarantees) and [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer). Their force remains a protocol request, not observed adherence.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-raw-originals
Label: Raw originals

Part of: [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree)

Identity: source documents retained under a library's `raw/`, including binary assets in `raw/assets/`, excluding the mutable registry and derived text editions. Substrate: ordinary repository files, optionally committed to Git. Form: natural-language source text interpreted by agent/human; binary payloads are opaque to Markdown navigation and may require external rendering/extraction. A raw note linking an image is not the image's readable contents. Lineage: human-selected documents, dropped files, pasted text or URL plus pasted text when unfetchable. The human supplies the source; the Librarian is instructed to save it verbatim, without per-file approval of routine ingest. Subsequent raw editing is forbidden by instruction, not a write barrier. Consumer: compilation and editorial source verification; Q&A can follow citation links to source material. Authority: source evidence, not intended operating instructions. Horizon: across sessions through retained files; no expiry. Evidence: SRC-1, `protocol.md`, `starter-library/raw/assets/README.md`, `starter-library/README.md`; [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile).

> For a screenshot/image of
> text, transcribe the text into a sibling `raw/<slug>.md` (keep the image in
> `raw/assets/`) so it's searchable and never needs re-OCR.
> --- `protocol.md`

The original and its transcription have distinct fidelity and recovery properties. This part does not duplicate the container or the edition part below.

#### MEM-OBJ-text-editions
Label: Searchable text editions and caption serializations

Part of: [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree)

Identity: retained readable derivatives beside originals: screenshot transcriptions and extracted `.txt`/`.htm` editions prescribed in `protocol.md`; helper-fetched captions join this part only if saved into a library. These are not additional originals merely because stored in `raw/`. Substrate: repository text files; arbitrary helper output paths may instead be outside the library. Form: natural-language extracted text for later agent interpretation; PDF page labels and optional provenance identify extraction conditions. Caption JSON adds symbolic video/language/generated fields and snippet data; text output collapses whitespace and omits timing by default, while SRT/VTT use provider formatters. Track-list JSON describes available tracks, not source statements. There is no embedding or dense store in these paths. Evidence: SRC-1, `protocol.md`, `tools/pdf_text.py`, `tools/youtube_transcript.py`.

Lineage and admission differ by producer. Image transcription is requested agent work from retained images. PDF output is admitted by software after caller-selected page/option validation and native-text/OCR processing, including labeled failed pages. Caption track selection uses the supplied ID/language/track preferences and external API; serialization is automatic, not human approval of each snippet. A caller need not be human. JSON retains more provenance than default text, whose video/language/generated diagnostics go to stderr rather than into the saved text. Consumers: the prescribed binary sidecar route affords later compilation or source inspection without re-extraction; standalone helper success does not wire later ingestion. Fidelity remains subject to editorial verification. Recovery: retained binary permits comparison/rerun; PDF replacement requires `--force`, caption file writes do not have that guard. No automatic refresh. See [RT-RTE-pdf-sidecar](runtime.md#rt-rte-pdf-sidecar) and [RT-RTE-caption-fetch](runtime.md#rt-rte-caption-fetch), whose endpoints are production routes rather than duplicate object identities.

> Machine-generated text; verify critical readings against the PDF.
> --- `tools/pdf_text.py`

That sentence is emitted in the default header, but `--no-header` removes the header. The source code string includes this exact warning; header presence is therefore conditional, not an invariant.

#### MEM-OBJ-source-notes
Label: Source notes

Part of: [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree)

Identity: one derived Markdown note per raw source under `wiki/sources/`. Substrate: repository files. Form: natural-language summary and key takeaways, with symbolic relative-link targets and frontmatter. Lineage: Librarian compilation under the source-specific-depth rule, with raw-file and original-source references. Source notes are abstractions, not raw interaction traces or copies of every source passage. Consumer: later wiki-first Q&A, concept maintenance and source verification; compile lint mechanically extracts named sections for overlap/echo/depth comparisons. Authority differs: evidence-bearing prose for the Librarian, strings and path patterns for lint. Admissions are routine model-authored edits; source links are required but semantic fidelity is not machine-certified. Persistence: across sessions, mutable through editorial redo; no expiry. Reasons can be retained in substantive takeaways and links, but no required derivation history records why each selection or omission was made. Evidence: SRC-1, `protocol.md`, `starter-library/wiki/sources/README.md`, `tools/compile_lint.py`; [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile).

> Source note (`wiki/sources/<slug>.md`):
> --- `protocol.md`

The template below that marker contains Summary, Key takeaways, Concepts extracted, Raw file and Original fields. It is a prescribed structure, not a populated note.

#### MEM-OBJ-concepts
Label: Concept articles

Part of: [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree)

Identity: atomic articles in `wiki/concepts/`, distinct from source summaries because existing concepts are merged rather than duplicated per source. Substrate: Markdown files. Form: natural-language explanations, applications, evidence and caveats; relative links/frontmatter provide symbolic organization. Lineage: extracted ideas from one or more source notes, plus admitted durable outputs and editorial updates. Consumer: later Q&A and library maintenance; lint consumes selected lead/body text and word counts, not the whole claim's meaning. Authority: reusable domain knowledge, not an enforced command or gold answer. Ordinary revisions are Librarian decisions; cross-library connections have the separate human-approval rule. Retained sources make verification possible, but no required per-revision criticism or rationale field establishes how the merge was justified. Horizon: sessions/problems in a user library, conditional on actual saving/reloading; no supplied use trace. Evidence: SRC-1, `protocol.md`, `starter-library/wiki/concepts/README.md`, `tools/compile_lint.py`; [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile).

> <Clear, atomic explanation; how to apply it, evidence, caveats as warranted.>
> --- `protocol.md`

This is template guidance, not evidence that actual concepts retain those elements. No separate theory-building or improved-capacity conclusion follows from the article label.

#### MEM-OBJ-topics
Label: Topic maps

Part of: [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree)

Identity: `wiki/topics/` articles organizing concepts by theme. Substrate: Markdown files. Form: natural-language scope/relationships and one-line concept descriptions, with symbolic relative links. Lineage: Librarian-created organization during compilation or maintenance, not raw source text. Consumer: navigation by agent/human; link audit checks destinations. Authority: suggestions for where related knowledge lives; not deterministic retrieval or a context-budget allocator. Admission: routine editorial creation for genuinely new themes, plus approved cross-library links where applicable. Mutable as the wiki grows; no expiry. Source excerpts and concept/article distinctions are preserved by the templates, but comprehensive taxonomy quality is unobserved. Evidence: SRC-1, `protocol.md`, `starter-library/wiki/topics/README.md`; [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile).

> Maps of Content (MOCs): higher-level articles that organize related concepts into
> a theme or domain.
> --- `starter-library/wiki/topics/README.md`

#### MEM-OBJ-source-registry
Label: Raw source registry

Part of: [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree)

Identity: `raw/INDEX.md`, not immutable raw document content. Substrate: Markdown table. Form: symbolic ID/status/date/path organization plus natural-language title/description for navigation and agent judgment. Lineage: initialized empty; Librarian adds rows at ingest and changes `raw` to `compiled` after requested compilation. Consumer: ingest/health workflow locates pending sources; the status is an agent-maintained assertion, not an execution checkpoint verified by code. Initial source choice is human-driven; row writing/status admission is model-mediated. Persistence: mutable across sessions, no expiry or transactional link to wiki writes. An ID identifies a source but does not itself rank or select it for a question. Evidence: SRC-1, `starter-library/raw/INDEX.md`, `protocol.md`; [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile).

> Status: raw (saved, not yet compiled) | compiled (digested into wiki).
> --- `starter-library/raw/INDEX.md`

#### MEM-OBJ-wiki-index
Label: Wiki master navigation and connection notices

Part of: [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree)

Identity: `wiki/INDEX.md`, including the conditional Connected libraries note. Substrate: Markdown. Form: natural-language labels/connection descriptions interpreted by the Librarian, with symbolic link destinations checked by link lint. Lineage: seeded empty at setup, updated on article changes and session closure; link creation is not automated by the evaluators. Consumer: first step of later question-driven wiki search. Selection: an agent uses question and index organization to choose sources/concepts, and decides whether to traverse advertised connections; no fixed top-k/token budget. Cross-library metadata does not give an isolation guarantee. Evidence: SRC-1, `starter-library/wiki/INDEX.md`, `protocol.md`; [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer).

> - **Advertise useful connections.** When a library has cross-links, add a short
>   `Connected libraries` note near the top of its `wiki/INDEX.md` so the
>   Librarian can decide whether to follow them.
> --- `protocol.md`

#### MEM-OBJ-outputs
Label: Generated outputs and durable filing candidates

Part of: [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree)

Identity: substantial answers, reports and related generated artifacts under `outputs/`. Substrate: repository files, with Markdown prose as the principal documented form; other artifact formats are allowed but not specified by a generator here. Lineage: agent synthesis from the question and retained wiki, not raw source ingestion. Claims must cite source notes or raw documents. Consumer: human recipient immediately; later Librarian can file durable material back into wiki under the Q&A instruction, after the offered follow-up. There is no output directory scan/cache-hit route for ordinary Q&A. Admission: agent writes substantial outputs and proposes durable filing; the shared protocol asks for an offer, not a software approval interception. This part differs from concepts because saving the answer alone does not install it into the wiki-first selection path. No expiry, withdrawal marker or output invalidation policy is specified. Evidence: SRC-1, `protocol.md`, `starter-library/outputs/README.md`, `README.md`; [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer).

> When
> an output contains durable knowledge, the Librarian files it back into the wiki
> so future queries benefit.
> --- `starter-library/outputs/README.md`

This shorthand is stronger than the protocol's offer-to-file wording; automatic filing and benefit are not established.

#### MEM-OBJ-health-reports
Label: Dated health reports

Part of: [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree)

Identity: `meta/health/YYYY-MM-DD-health.md`, distinct from transient CLI stdout and CI status. Substrate: Markdown files. Form: natural-language diagnoses and proposed repairs; filenames carry symbolic dates. Lineage: requested periodic/on-request Librarian audit, potentially informed by mechanical diagnostics and source/article comparison. The agent writes the report and fixes safe items or proposes the rest. It is not a software-emitted write from the lint CLIs. Consumer: maintainer/agent considering audit findings in that workflow; no specified later invocation automatically reloads previous reports. Content/reasons may be retained as diagnoses, but no fixed schema requires blame, rejected alternatives or outcome linkage. Persistence is afforded by files; repeated consumption remains unobserved and unspecified. Evidence: SRC-1, `protocol.md`, `starter-library/meta/health/README.md`, `tools/check_links.py`, `tools/compile_lint.py`; [RT-RTE-health-audit](runtime.md#rt-rte-health-audit).

> Report filename format: `YYYY-MM-DD-health.md`.
> --- `starter-library/meta/health/README.md`

#### MEM-OBJ-changelog
Label: Library changelog

Part of: [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree)

Identity: `meta/CHANGELOG.md`, separate from raw sources, audit reports and Git history. Substrate: Markdown. Form: natural-language change descriptions, dates and links. Lineage: requested append-only session closure and initialized scaffold entry. It records agent operations, but retaining this trace does not establish automatic extraction of improved procedures or a later model consumer. Human/agent inspection is afforded by the readable file; no reload instruction selects old log entries for future work. Reasons for edits are not mandatory. The append-only label is qualified by the protocol's rename rule, which explicitly repairs historical link entries. Admission is routine Librarian logging and repair, not per-entry human approval. Evidence: SRC-1, `protocol.md`, `starter-library/meta/CHANGELOG.md`; [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile), [RT-RTE-health-audit](runtime.md#rt-rte-health-audit).

> A rename means updating every link,
>   including historical entries in `meta/CHANGELOG.md`, and logging the sweep.
> --- `protocol.md`

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-wiki-evidence
Label: Retained wiki evidence authority

Consumer: later Librarian answering a human question or maintaining the library. Channel: wiki-first file search, navigation and relative citations; source links afford verification against preserved originals. Force: interpreted evidence/content for synthesis, not an executable directive, guaranteed truth or source-entailment proof. Horizon: later invocations across sessions if retained files are reloaded. Requested delivery is explicit; activation and benefit remain unobserved. Evidence: SRC-1, `protocol.md`, `README.md`; supporting passage in [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer).

Distinct from [RT-BAP-librarian-instructions](runtime.md#rt-bap-librarian-instructions), which concerns operating instructions, and from [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer), which describes progression rather than this content's authority. The path spans source notes, concepts and navigation, rather than being a material part of exactly one supplied record. No shipped source-trust scoring, taint separation or prompt-injection filter is established by citation conventions. The trust rule is editorial: preserve originals, cite support, verify critical machine readings and admit noncoverage.

## Annotations

#### On [RT-OBJ-protocol](runtime.md#rt-obj-protocol)

Memory-specific lineage: static shared instructions are not accumulated experience. Setup creates persistent local scope/deviation text from confirmed choices; future agent entry may consume it as instruction. `library.md` prescribes this write, but no subsequent operational-evidence-to-protocol-revision route is prescribed. See SRC-1, `library.md`, `AGENTS.md`, and the instruction-loading passage in [RT-BAP-librarian-instructions](runtime.md#rt-bap-librarian-instructions).

#### On [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile)

The retained chain is originals → searchable editions where needed → source-specific summaries/takeaways → merged concepts and topic maps → question-driven later reading. It is source-fed knowledge curation, not automatically trace-fed agent-method learning. Raw includes more than conversation history; externally supplied documents and pasted text have mixed origins. Narrative source substance and caveats are requested, but full selection/merge rationale is not. Registry and navigation edits make admission discoverable but do not prove it happened. Source and concept consumers can reread linked originals; no requirement makes later Q&A reread every rationale or original. Evidence: SRC-1, `protocol.md`, `starter-library/raw/INDEX.md`; quoted compile instructions in the supplied record and [MEM-OBJ-concepts](#mem-obj-concepts).

#### On [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer)

Read-back is pull-oriented: question → agent selection from index/source/concept content → file-reading context → synthesized cited answer. Cross-library connection notices inform discretionary traversal. No automatic top-k injection, numeric context allocation, window trimming, summary checkpoint or sub-agent frame is specified by these source paths. On-demand files remain reachable even when not loaded; whether old tool results remain in the window is external host behavior. This is external durable file storage plus rereading, not a specified stack-frame/heap management protocol. Output saving preserves synthesis; only filing into wiki supplies the explicitly named ordinary query route. Evidence: SRC-1, `protocol.md`, `README.md`; [MEM-OBJ-wiki-index](#mem-obj-wiki-index), [MEM-OBJ-outputs](#mem-obj-outputs).

#### On [RT-RTE-health-audit](runtime.md#rt-rte-health-audit)

The retained change is agent-authored editorial material, not linter modification. Link audit reads Markdown destinations, basename mentions and leading frontmatter markers; compile lint selects source Summary/Key takeaways and concept lead/body, normalizes text, measures n-gram overlap and word counts, and emits diagnostic/status results. Reports are requested in the protocol, but neither CLI writes `meta/health/` or a learned procedure. CI consumes exit codes; agent/human receives diagnostics. Default CI does not pass `--strict`. Evidence: SRC-1, `tools/check_links.py`, `tools/compile_lint.py`, `.github/workflows/funes-lint.yml`, `protocol.md`; the supplied record retains thresholds and the exit-code quotation.

A high compression advisory does not mean all raw material was measured: `.htm` editions and binary assets are outside `check_depth`'s `.txt`/`.md` count, and a zero wiki-word denominator produces ratio 0. Missing Summary/lead sections can avoid duplicate comparisons. Neither gate success nor the registry's compiled flag establishes fidelity. Safe repair versus proposal has no formal safety classifier. See [MEM-OBJ-health-reports](#mem-obj-health-reports).

#### On [RT-RTE-pdf-sidecar](runtime.md#rt-rte-pdf-sidecar)

Selected pages persist with their native/OCR/failure labels. The default header records source basename, generation date, method and available tool versions, not a content hash or full reproducible configuration. In particular, language, PSM and an explicit selected-page list are not header fields; labels reveal attempted pages, not all unattempted requests after fail-fast. Temporary rendered images are deleted and the temporary directory is discarded; the original PDF remains the verification path. This is deterministic extraction storage, not model-window compaction. `--fail-fast` still reaches final file writing; nonzero status is not withdrawal of the partial edition. Evidence: SRC-1, `tools/pdf_text.py`; [MEM-OBJ-text-editions](#mem-obj-text-editions) and the failure-handling quotation in the supplied route.

#### On [RT-RTE-caption-fetch](runtime.md#rt-rte-caption-fetch)

Readability/provenance depend on format. Default plain text retains normalized snippet words without timing or an in-file video identity; stderr metadata is separate. JSON retains video ID, language, generated flag and raw snippet data. List-only mode retains track availability rather than caption text. No Funes consumer parses saved JSON/SRT/VTT automatically, and no file save alone marks a source compiled. Admission of fetched text into the library remains a subsequent caller/Librarian decision. Evidence: SRC-1, `tools/youtube_transcript.py`, `tools/README.md`; [MEM-OBJ-text-editions](#mem-obj-text-editions).

#### On [RT-RTE-library-setup](runtime.md#rt-rte-library-setup)

Initialization control is partly explicit: the human settles domain/link style unless already specified, then the agent authors scope/deviations and empty navigation/state files. Subsequent source selection and semantic edits use the ordinary Librarian policy, not approval of every article. The future local instruction consumer is documented but not observed. Exact host model version and hidden context state remain unspecified; this does not erase known file transformations. Evidence: SRC-1, `library.md`, `starter-library/AGENTS.md`; the supplied route retains the confirmation and commit passages.

## Write side

### Acquisition and admission

The human supplies sources or requests ingestion of dropped files. The agent saves originals, transcribes images and registers sources; a request to start ingest is not approval of each derived statement. The PDF caller chooses input/output/pages/options, then software admits native text at the threshold or OCR results and labeled page failures. The caption caller chooses a known video and preferences; external track selection and serialization determine returned text, without claim verification. Neither helper registers sources or compiles the wiki. These are distinct write/admission mechanisms, even though all can eventually contribute to [MEM-OBJ-text-editions](#mem-obj-text-editions). Evidence and recovery details are on [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile), [RT-RTE-pdf-sidecar](runtime.md#rt-rte-pdf-sidecar) and [RT-RTE-caption-fetch](runtime.md#rt-rte-caption-fetch).

### Compilation, maintenance and return of outputs

The Librarian authors and admits ordinary source notes, merged concepts, topic maps and metadata. Guidance requires specificity, substantial extraction, caveats, backlinks and source citations. The human is not a mandatory per-article editor. A strong cross-library tie is different: propose it, obtain approval, add reciprocal links and connection notices. Questions produce outputs; durable filing is offered under the shared protocol. Source-specific reasons may survive as prose/caveats and linked sources, but there is no mandatory retained decision trace for abstraction, merging or filing. See [MEM-OBJ-source-notes](#mem-obj-source-notes), [MEM-OBJ-concepts](#mem-obj-concepts), [MEM-OBJ-topics](#mem-obj-topics), [MEM-OBJ-outputs](#mem-obj-outputs).

Health review can feed corrections back into those articles. Mechanical diagnostics are evidence for an agent decision, not a software-admitted replacement. Safe fixes are delegated to the Librarian; other changes are proposals. There is no supplied gold-answer oracle. The source report of a failed shallow compile motivated the current depth lint, but does not establish an automatic runtime method-update chain. The report/log chain is operation → requested dated report/changelog → possible maintainer inspection; an automatic later report/log consumer is unspecified. No alternate agent-summary checkpoint or conversation-compaction producer exists in the inspected shipped drivers. See [RT-ABS-model-driver](runtime.md#rt-abs-model-driver), [RT-RTE-health-audit](runtime.md#rt-rte-health-audit), [MEM-OBJ-health-reports](#mem-obj-health-reports).

### Rejection, cleanup and withdrawal

Shallow compilation is instructed to be redone, not padded. Lint failures return nonzero; CI receives them, but branch protection/merge veto is unknown. A human can decline cross-library proposals or filing follow-up. Helpers reject invalid inputs/dependency failures; PDF existing-output refusal can be overridden and partial writes survive page failures. Caption output may overwrite a file. These controls do not form a universal knowledge-write gate. See [RT-CLM-library-guarantees](runtime.md#rt-clm-library-guarantees).

Concept merging, rename/link repair and stale-index/contradiction review are specified. No inspected instruction defines a tombstone, automatic expiry, cascading retraction of downstream claims, or rollback transaction for multi-file edits. Retained originals support editorial verification; available Git history supports recovery only for committed versions. The starter README says material persists only once committed, whereas file writes can remain on disk before commit. This limits durable/versioned recovery, not the existence of filesystem state. No deletion or rejection result is automatically installed into later question context. Evidence: SRC-1, `protocol.md`, `starter-library/README.md`, helper sources; [RT-RTE-health-audit](runtime.md#rt-rte-health-audit).

> Material persists only
> once committed.
> --- `starter-library/README.md`

## Read-back

| Retained input | Trigger and selector | Delivery and later consumer | Authority, budget and limit |
|---|---|---|---|
| Local AGENTS created at setup | Work in the selected library; host loads or agent is told to read entry instructions | File content to later Librarian invocation | Requested operating authority; not trace-fed experience. Host delivery/context limits unknown. [RT-BAP-librarian-instructions](runtime.md#rt-bap-librarian-instructions). |
| Originals and readable editions | Ingest/compile or fidelity review; agent chooses source, helper chooses pages/track during production | Source files or extracted text to compilation/editorial agent | Source evidence; no mandatory full-source read or token quota. Standalone extraction is production, not proof of a later consumer. [MEM-OBJ-text-editions](#mem-obj-text-editions). |
| Wiki index, source notes, concepts, topics and cross-links | Human question; Librarian follows INDEX → sources → concepts and chooses relevant connections | On-demand file reads into later answer synthesis | Knowledge/context authority, not operating command; no numeric retrieval budget or measured activation. [MEM-BAP-wiki-evidence](#mem-bap-wiki-evidence). |
| Source registry and wiki files | Compilation/health request; agent examines pending sources, stale navigation and content | Editorial context; mechanical files also reach linters/CI | Registry status is an assertion; lint consumes selected symbols/text by fixed rules. No remembered pass certificate. [MEM-OBJ-source-registry](#mem-obj-source-registry), [RT-RTE-health-audit](runtime.md#rt-rte-health-audit). |
| Saved outputs | Offer to file durable material, followed by accepted/requested editorial follow-up | Selected durable substance into wiki, then ordinary later wiki read-back | Saving alone is not adoption; no automatic push or answer-cache consumer. [MEM-OBJ-outputs](#mem-obj-outputs). |
| Health reports and changelog | Report/log writing is requested; subsequent inspection is possible but no later reload trigger/selector specified | Readable files available to maintainer/agent | Retention is established by instructions, automatic later use is not. Prevents a closed trace-learning or method-revision conclusion. [MEM-OBJ-health-reports](#mem-obj-health-reports), [MEM-OBJ-changelog](#mem-obj-changelog). |

Context control is chiefly what the agent elects to read from durable files. It is not a specified policy for preferentially removing old turns, keeping a verbatim tail, isolating a delegated frame, or reloading a compaction summary. The relevant shipped entry instructions and all executable helpers were inspected; external host behavior remains uninspected. Physical PDF temporary-file cleanup is not model-context eviction. SRC-1, `AGENTS.md`, `protocol.md`, `tools/pdf_text.py`; [RT-ABS-model-driver](runtime.md#rt-abs-model-driver).

## Integration issues

1. **Output admission wording remains ambiguous.** SRC-1, `starter-library/outputs/README.md` says the Librarian files durable knowledge back; `protocol.md` says offer. [MEM-OBJ-outputs](#mem-obj-outputs) retains both. [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer) correctly models the offer, but treating the human response as a deployed veto would exceed the evidence. Prevented conclusion: unconditional autonomous output-to-wiki installation. The actual instruction and host behavior are unobserved.
2. **Report retention is not a later consumer.** [RT-RTE-health-audit](runtime.md#rt-rte-health-audit) says reports are available to later review. [MEM-OBJ-health-reports](#mem-obj-health-reports) and [MEM-OBJ-changelog](#mem-obj-changelog) qualify this as storage/inspection affordance, not a specified later reload route. No supplied runtime fact needs deletion, but reconciliation must not promote availability into recurrent trace-fed updating. SRC-1, `protocol.md`, `starter-library/meta/health/README.md`, `starter-library/meta/CHANGELOG.md`.
3. **Append-only and persistence claims need narrow readings.** The rename rule repairs historical changelog entries, so append-only does not mean byte-immutable history. The starter README's committed-only persistence language does not deny precommit filesystem retention; it limits versioned recovery. See [MEM-OBJ-changelog](#mem-obj-changelog), [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree), [RT-RTE-library-setup](runtime.md#rt-rte-library-setup). No universal auto-commit or automatic rollback follows. SRC-1, `protocol.md`, `starter-library/README.md`.
4. **Provenance and evaluator coverage are narrower than labels.** PDF headers are optional and do not encode all extraction options. Default caption text drops metadata that JSON retains. Compile-depth ratio ignores `.htm`/binary content and returns 0 when wiki word count is zero. These qualify completeness/traceability readings of [RT-RTE-pdf-sidecar](runtime.md#rt-rte-pdf-sidecar), [RT-RTE-caption-fetch](runtime.md#rt-rte-caption-fetch) and [RT-RTE-health-audit](runtime.md#rt-rte-health-audit), not their basic route identities. Source-supported details are in their annotations. No reliability or grounding conclusion should depend on a success label alone. SRC-1, `tools/pdf_text.py`, `tools/youtube_transcript.py`, `tools/compile_lint.py`.
5. **Self-improving is a source label, not a demonstrated result.** SRC-1, `starter-library/README.md` uses that label. File curation and optional knowledge reuse are specified, but no operation trace establishes evidence-responsive changes to method instructions, activation of changed organization or improved future capacity. [MEM-BAP-wiki-evidence](#mem-bap-wiki-evidence) records the available knowledge authority without claiming exercised self-improvement. This is not evidence that a deployed host cannot learn or improve.
6. **Identity reconciliation.** Every new operative object above is an explicitly identified part of [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree); none replaces or duplicates that valid container. [MEM-BAP-wiki-evidence](#mem-bap-wiki-evidence) is distinct from the static instruction path and existing answer route as explained there. All supplied route referents were annotated rather than redeclared. No other possible duplicate was found after comparison. No additional correction to supplied facts is asserted.

## Limitations and checks

The empty scaffold and lack of execution evidence prevent conclusions about actual acquisition fidelity, source-grounded answers, host instruction compliance, context usage, repeated report consumption, causal benefit or reliable semantic admission. Provider state, user-library contents, external dependency internals and linked examples were not inspected and are not silently treated as absent. Initialization choices and subsequent known file transformations are retained separately despite those limits.

HEAD was checked as `3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11` with a clean source checkout; the report repeats the supplied boundary/run identities exactly. Governing memory type, worker rules and record contract were read completely, along with the supplied runtime and boundary. All source-dependent additions use SRC-1 at that frozen revision. No target execution, source changes or additional sources were used.

Deterministic validation: passed using the supplied `commonplace-run validate-output` invocation. This establishes structural and quotation checks, not factual correctness, successful operation or acceptance by reconciliation.
