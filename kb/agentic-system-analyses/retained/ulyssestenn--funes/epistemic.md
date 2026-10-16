---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Funes epistemic routes: source preservation, compilation, mechanical gates, editorial fidelity review and later wiki reliance."
run-id: AAS-2026-10-15-funes-a9e6dbb3946a-01
reviewed-boundary: 3fb448b8e0d1ab5f6de3c6de61d8d556dab4ee11
---

# Funes epistemic report

## Source-and-claim boundary

The question is how Funes turns supplied material into content on which later answers may rely, and what warrants that reliance. The frozen source and exclusions are those in the [Source register](boundary.md#source-register). Funes includes the instruction-mediated Librarian loop, not just its Python helpers. Semantic work is assigned to an external agent; executable code supplies extraction and mechanical audits. Public claims are [RT-CLM-library-guarantees](runtime.md#rt-clm-library-guarantees), [EPI-CLM-library-abstraction](#epi-clm-library-abstraction) and [EPI-CLM-compile-depth](#epi-clm-compile-depth).

The following table distinguishes direct inspection for this member from supplied findings. All direct reads use SRC-1 at the reviewed commit. Dispatch was checked against the tracked tree: the four Python main entry points and the CI workflow exhaust the shipped executable operations. No additional registered tools, hooks or model driver were found in that tree; the supplied bounded search is [RT-ABS-model-driver](runtime.md#rt-abs-model-driver).

| Entry point or operation | Source path | Coverage and records |
|---|---|---|
| Agent entry and local scope | `AGENTS.md`, `starter-library/AGENTS.md` | Supplied findings: [RT-OBJ-protocol](runtime.md#rt-obj-protocol), [RT-BAP-librarian-instructions](runtime.md#rt-bap-librarian-instructions). Host delivery remains unobserved. |
| Ingest, compilation, registry status, backlinks | `protocol.md` | Direct complete read: [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile), [EPI-OBJ-raw](#epi-obj-raw), [EPI-OBJ-wiki](#epi-obj-wiki). |
| Wiki Q&A, output retention and filing-back | `protocol.md` | Direct: [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer), [EPI-OBJ-outputs](#epi-obj-outputs). |
| Contradiction, grounding, cleanup and proposed fixes | `protocol.md`, `tools/README.md`, `tools/compile_lint.py` | Direct complete reads: [EPI-RTE-fidelity-review](#epi-rte-fidelity-review), [RT-RTE-health-audit](runtime.md#rt-rte-health-audit). |
| Link, orphan, frontmatter CLI | `tools/check_links.py` | Direct complete read, including exclusions and exit: [EPI-RTE-mechanical-checks](#epi-rte-mechanical-checks), [EPI-RTE-audit-disposition](#epi-rte-audit-disposition). |
| Duplicate, echo, depth CLI and strict mode | `tools/compile_lint.py` | Direct complete read: same two records; [EPI-CLM-compile-depth](#epi-clm-compile-depth). |
| CI caller and syntax checking | `.github/workflows/funes-lint.yml` | Direct complete read: [EPI-RTE-audit-disposition](#epi-rte-audit-disposition). Syntax success concerns Python syntax, not wiki truth. |
| PDF native/OCR selection, partial failure, force and no-header | `tools/pdf_text.py`, `tools/README.md` | Direct complete reads: [RT-RTE-pdf-sidecar](runtime.md#rt-rte-pdf-sidecar), [EPI-OBJ-pdf-text](#epi-obj-pdf-text). |
| Caption list/fetch, track selection, formatting and output overwrite | `tools/youtube_transcript.py`, `tools/README.md` | Direct complete reads: [RT-RTE-caption-fetch](runtime.md#rt-rte-caption-fetch), [EPI-RTE-caption-reshape](#epi-rte-caption-reshape). |
| Provisioning and persistent local instructions | `library.md` | Direct complete read; [RT-RTE-library-setup](runtime.md#rt-rte-library-setup). This creates policy and organization, not verified domain knowledge. |
| Starter indices, source/concept/topic scaffolds, health/output/changelog folders | `starter-library/` | Supplied complete coverage: [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree); no populated library instance. |
| Public design and examples | `README.md` | Direct complete read: [EPI-CLM-library-abstraction](#epi-clm-library-abstraction). Examples are illustrative doctrine, not observed outcomes. |

Excluded host/provider internals prevent a conclusion about the model's internal inference, parameter updates, actual instruction loading or deployment enforcement. External OCR, Poppler and caption-service internals prevent an extraction-fidelity conclusion. No supplied run, populated library or causal experiment establishes actual checking, acceptance, integration, retrieval accuracy or benefit. Linked external examples remain excluded. These are not reasons to erase the implemented wrapper and audit routes. There is no relevant shipped operation left unassessed in the coverage above; semantic content of future arbitrary articles remains not determinable. Evidence: SRC-1, `README.md`, `protocol.md`, `tools/pdf_text.py`, `tools/youtube_transcript.py`; supplied [boundary](boundary.md#boundary-and-evidence).

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-raw](#epi-obj-raw) | Imported assertions, quotations and observations, when present | see record | SRC-1, `protocol.md` | Preservation of a source is not endorsement of its claims. |
| [EPI-OBJ-pdf-text](#epi-obj-pdf-text) | Machine transcription of source propositions; page/method metadata | see record | SRC-1, `tools/pdf_text.py` | Recognition fidelity unknown; original is authoritative. |
| [EPI-OBJ-captions](#epi-obj-captions) | Imported speech transcription; track and timing metadata depending on format | see record | SRC-1, `tools/youtube_transcript.py` | Transcription truth and spoken-claim truth are separate unknowns. |
| [EPI-OBJ-wiki](#epi-obj-wiki) | Source summaries, concepts, evidence/caveats and topic relations | see record | SRC-1, `protocol.md` | No actual populated candidate or semantic trace; relation to source is indeterminate. |
| [EPI-OBJ-outputs](#epi-obj-outputs) | Answers and syntheses may assert propositions; routines/plans can instead prescribe actions | see record | SRC-1, `protocol.md` | Intended reuse does not establish acceptance. |
| [EPI-OBJ-audit-results](#epi-obj-audit-results) | Bounded assertions about paths, text overlap and counts; editorial diagnoses when authored | see record | SRC-1, `tools/check_links.py`, `tools/compile_lint.py`, `protocol.md` | Mechanical and editorial evidence differ. |
| [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree) | Registry and changelog report state/history; navigation mostly selects content | see record | SRC-1, `protocol.md` | `compiled` records workflow status, not a truth certificate. |
| [RT-OBJ-protocol](runtime.md#rt-obj-protocol) | Mostly operating policy, not a candidate domain claim | see record | SRC-1, `protocol.md`, `library.md` | Persistent instruction text has requested operational authority. |
| [RT-CMP-librarian-model](runtime.md#rt-cmp-librarian-model) | Internal truth-apt content not determinable | see record | SRC-1, `README.md` | Distributed-parametric internals inaccessible; fixity and mutation findings belong to supplied component. |

## Authority-route ledger

Each row assesses one function, not one script. Multiple rows may cite a valid container record without superseding it. `see` defers record-owned details; architectural status and the bounded epistemic assessment are this overlay's fields. No row asserts observed operation.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile) — raw ingest | content transformation | doctrine only | [EPI-OBJ-raw](#epi-obj-raw) | truth-apt transformation: acquisition/import | Supplied source to raw record | see route | see route | Requested verbatim acquisition | Instruction only | Source warrant unknown; requested preservation of wording and origin | Agent may save raw material before semantic review | see route and [RT-BAP-librarian-instructions](runtime.md#rt-bap-librarian-instructions) | SRC-1, `protocol.md` | [RT-CLM-library-guarantees](runtime.md#rt-clm-library-guarantees) | none | Actual preservation unobserved |
| [RT-RTE-pdf-sidecar](runtime.md#rt-rte-pdf-sidecar) — extraction | content transformation | implemented | [EPI-OBJ-pdf-text](#epi-obj-pdf-text) | truth-apt transformation: acquisition/import | PDF selected pages to searchable text | see route | see route | Native/OCR text or marked page failure | File write, see route | Warrant unknown; recognition may degrade content; header and original permit checking | Searchable derivative can exist despite exit 1 | see route | SRC-1, `tools/pdf_text.py` | [RT-CLM-library-guarantees](runtime.md#rt-clm-library-guarantees) | fail-fast is not all-or-nothing | Dependency accuracy uninspected |
| [RT-RTE-pdf-sidecar](runtime.md#rt-rte-pdf-sidecar) — text admission | disposition/acceptance | implemented | [EPI-OBJ-pdf-text](#epi-obj-pdf-text) | no content change | Native layer versus OCR; page output versus failure marker | Character threshold, command outcome and nonempty text; see route | Per selected page before final write | Operational admission or fallback/error | Local control flow | No factual acceptance; character count is not accuracy evidence | Native text accepted for output, OCR attempted otherwise; partial output retained | Wrapper branches, enforcing for current command; see route | SRC-1, `tools/pdf_text.py` | none | none | A long erroneous native layer can pass |
| [RT-RTE-caption-fetch](runtime.md#rt-rte-caption-fetch) — track acquisition | content transformation | implemented | [EPI-OBJ-captions](#epi-obj-captions) | truth-apt transformation: acquisition/import | Chosen video and track to fetched snippets | see route | see route | Captions or service/dependency error | see route | Source warrant unknown; manual/generated selection is not truth verification | Caller-selected material can be emitted/saved without claim review | see route | SRC-1, `tools/youtube_transcript.py` | none | none | Listing emits metadata, not speech claims |
| [EPI-RTE-caption-reshape](#epi-rte-caption-reshape) | content transformation | implemented | [EPI-OBJ-captions](#epi-obj-captions) | truth-apt transformation: non-ampliative reshaping | Snippet text to plain-text serialization | see record | see record | Whitespace-normalized lines; optional start timestamps | see record | No new speech-content warrant; timing/provenance reduced in default text | Rendered text available to caller or file consumer | see record | SRC-1, `tools/youtube_transcript.py` | none | none | Domain excludes interpretation of layout-dependent content |
| [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile) — source/concept production | content transformation | doctrine only | [EPI-OBJ-wiki](#epi-obj-wiki) | truth-apt transformation: indeterminate | Raw sources to summaries, concepts and topic explanations | Librarian interpretation; see route | see route | Requested source-specific abstraction | Instruction only | Neither entailment nor non-entailment established for an actual output | Agent authors/merges wiki without per-claim human approval | see route | SRC-1, `protocol.md` | [EPI-CLM-library-abstraction](#epi-clm-library-abstraction) | none | Need actual inputs/outputs to distinguish reshaping, derivation and conjecture |
| [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile) — retention/organization | retention | doctrine only | [EPI-OBJ-wiki](#epi-obj-wiki) | no content change | Compiled material to files, indices, backlinks and registry | see route | During compile | Requested persistent candidate and `compiled` status | Instruction only | Filing and linking confer availability, not acceptance | Later sessions can select content through wiki navigation | see route | SRC-1, `protocol.md` | [RT-CLM-library-guarantees](runtime.md#rt-clm-library-guarantees) | none | Organization before evidenced acceptance is not lifecycle integration |
| [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer) — reliance | operational admission/selection/consumption | doctrine only | [EPI-OBJ-wiki](#epi-obj-wiki) | no content change | Question to wiki-first selection | see route | Later Q&A | Requested retrieved context and explicit noncoverage | Instruction only | Citation supplies traceability, not truth license beyond source support | Wiki can guide answers before any separate acceptance decision | see route | SRC-1, `protocol.md` | [EPI-CLM-library-abstraction](#epi-clm-library-abstraction) | none | Reliance and activation unobserved |
| [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer) — answer production | content transformation | doctrine only | [EPI-OBJ-outputs](#epi-obj-outputs) | truth-apt transformation: indeterminate | Selected wiki to answer/synthesis | see route | At question time | Requested cited outputs | Instruction only | No demonstrated entailed derivation or accepted ampliative claim | Answer/report can reach human and be saved | see route | SRC-1, `protocol.md` | [EPI-CLM-library-abstraction](#epi-clm-library-abstraction) | none | Plans/routines may be non-truth-apt prescriptions instead |
| [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer) — saving/filing | retention | doctrine only | [EPI-OBJ-outputs](#epi-obj-outputs) | no content change | Substantial output to file; durable parts offered for wiki | see route | After answering | Requested persistence and human-facing offer | Instruction only | Durability judgment is not a truth criterion | Human can decline filing offer; saved output already remains available | see route | SRC-1, `protocol.md` | none | none | No evidence-consuming epistemic acceptance specified for filing |
| [EPI-RTE-mechanical-checks](#epi-rte-mechanical-checks) | check/evidence production | implemented | [EPI-OBJ-audit-results](#epi-obj-audit-results) | truth-apt transformation: entailed derivation | Paths/text predicates within inspected parser domain | see record | On audit invocation | Bounded findings/counts | Produces diagnostics; disposition separate | Conditional warrant for computed predicates, not source truth | No article writes; result made available to caller | see record | SRC-1, `tools/check_links.py`, `tools/compile_lint.py` | [EPI-CLM-compile-depth](#epi-clm-compile-depth) | proxy is not semantic extraction proof | File-read fidelity and intended parser interpretation remain premises |
| [EPI-RTE-audit-disposition](#epi-rte-audit-disposition) | disposition/acceptance | implemented | [EPI-OBJ-audit-results](#epi-obj-audit-results) | no content change | Findings to CLI success/failure and CI step status | see record | After checks | Gate failure or success; advisory display | see record | Operational pass only, not epistemic acceptance of articles | CI step can fail; merge veto not established | see record | SRC-1, `tools/compile_lint.py`, `.github/workflows/funes-lint.yml` | [EPI-CLM-compile-depth](#epi-clm-compile-depth) | none | CI omits strict mode |
| [EPI-RTE-fidelity-review](#epi-rte-fidelity-review) — comparison | check/evidence production | doctrine only | [EPI-OBJ-wiki](#epi-obj-wiki), [EPI-OBJ-raw](#epi-obj-raw) | no content change | Compiled article/source fidelity; contradictions and gaps | see record | Editorial review, not a wired pre-write gate | Requested criticism or finding | Instruction/design only | Potential evidence about fidelity; no recorded decision here | Reviewer may recommend correction | see record | SRC-1, `tools/compile_lint.py`, `protocol.md` | [RT-CLM-library-guarantees](runtime.md#rt-clm-library-guarantees) | none | This positive editorial route refutes a blanket no-checking verdict |
| [RT-RTE-health-audit](runtime.md#rt-rte-health-audit) — editorial disposition | disposition/acceptance | doctrine only | [EPI-OBJ-audit-results](#epi-obj-audit-results), [EPI-OBJ-wiki](#epi-obj-wiki) | no content change | Health findings to safe fixes or human proposals | see route | On request/periodically | Requested fixes, proposals and dated report | Instruction only | No universal truth-acceptance criterion or recorded acceptance instance | Librarian decides safe fixes; human can reject proposed remainder | see route | SRC-1, `protocol.md` | none | none | Rejection/withdrawal of a false claim is possible editorially, not automatically traced to all dependent outputs |
| [RT-RTE-health-audit](runtime.md#rt-rte-health-audit) — editorial revision | content transformation | doctrine only | [EPI-OBJ-wiki](#epi-obj-wiki) | truth-apt transformation: indeterminate | Existing claims to revised article | see route | After diagnosis | Requested corrected/merged content | Instruction only | Whether revision preserves, derives or conjectures is undetermined without content | Changed article may guide future Q&A | see route | SRC-1, `protocol.md` | none | none | No observed rejection, rollback or downstream withdrawal |
| [RT-RTE-library-setup](runtime.md#rt-rte-library-setup) | behavior/policy adaptation | doctrine only | [RT-OBJ-protocol](runtime.md#rt-obj-protocol) | non-truth-apt policy/content update: new library scope and deviations | Human conventions to local instructions and structure | see route | Human-requested setup | Requested retained local AGENTS | Instruction only | No domain-truth acceptance | Later agent may follow new scope/conventions | see route and [RT-BAP-librarian-instructions](runtime.md#rt-bap-librarian-instructions) | SRC-1, `library.md` | none | none | Not an evidenced evaluation-fed method improvement |

No separate post-acceptance lifecycle-integration route is established by the inspected `protocol.md`, `library.md`, helpers and CI. Backlinks, index updates and output filing are real prescribed organizational work, but the available evidence places no recorded evidence-consuming truth acceptance before them. This is a boundary on that classification, not a denial of organization or future editorial acceptance. Supplied recovery details, including original preservation, optional force/overwrite, Git history and lack of automatic rollback, remain on [RT-RTE-pdf-sidecar](runtime.md#rt-rte-pdf-sidecar), [RT-RTE-caption-fetch](runtime.md#rt-rte-caption-fetch), [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile) and [RT-RTE-health-audit](runtime.md#rt-rte-health-audit).

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-library-guarantees](runtime.md#rt-clm-library-guarantees) | see record | SRC-1, `protocol.md`, `README.md`; doctrine/design | Raw preservation, relative source links, depth and editorial grounding rules | [RT-RTE-pdf-sidecar](runtime.md#rt-rte-pdf-sidecar), [EPI-RTE-mechanical-checks](#epi-rte-mechanical-checks), [EPI-RTE-audit-disposition](#epi-rte-audit-disposition) provide narrower supports | None supplied | No causal comparison; file capability bypasses protocol; link existence does not check support | A prescribed lineage path, with bounded mechanical detection | Universal immutability and truth grounding are not implemented invariants |
| [EPI-CLM-library-abstraction](#epi-clm-library-abstraction) | see record | SRC-1, `README.md`; doctrine/design | [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile), [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer), [RT-RTE-health-audit](runtime.md#rt-rte-health-audit) | Extraction wrappers and audits, not a semantic compiler | None supplied; README examples illustrative | No retrieval/benefit experiment; model interpretation and source quality unresolved | Coherent requested retained-library workflow | No produced accepted new knowledge instance or demonstrated sustained coherence |
| [EPI-CLM-compile-depth](#epi-clm-compile-depth) | see record | SRC-1, `tools/compile_lint.py`, `tools/README.md`; doctrine/design plus attributed reported operation | Explicit gates/advisory separation and editorial fidelity fallback | [EPI-RTE-mechanical-checks](#epi-rte-mechanical-checks), [EPI-RTE-audit-disposition](#epi-rte-audit-disposition) | Historical failure account only; no inspectable run | Proxies not necessary/sufficient semantic tests; no independent comparison | Can detect selected duplicate/echo patterns and flag thin prose | Distinct fabricated prose can clear duplicate tests without reading a source; editorial fidelity is only doctrine |

## Bounded conclusion

Funes prescribes source acquisition and retention, abstraction into a linked wiki, wiki-first answering, output saving and editorial repair. Raw retention preserves an evidential route if followed; it does not make imported claims true. PDF and caption helpers implement acquisition, selection and serialization, with explicit but defeasible lineage aids. Default caption text loses timing/track context from the content channel; PDF defaults preserve page/method information but permit partial output and optional header omission. Source warrant is unknown, not upgraded by successful extraction. See [RT-RTE-pdf-sidecar](runtime.md#rt-rte-pdf-sidecar), [RT-RTE-caption-fetch](runtime.md#rt-rte-caption-fetch), [EPI-RTE-caption-reshape](#epi-rte-caption-reshape).

Mechanical audits derive bounded propositions from inspected file text and path predicates. Their downstream force is local command/CI status, with advisory-only depth results in the shipped caller. Their intended use is repository-health triage; their scope is exactly the parsed graph/sections/counts. They neither certify source truth nor force branch protection. See [EPI-RTE-mechanical-checks](#epi-rte-mechanical-checks), [EPI-RTE-audit-disposition](#epi-rte-audit-disposition).

Semantic comparison is not absent: the protocol requests contradiction/grounding review, and the linter design explicitly calls for reading source and article together. Its epistemic target is fidelity and its operational path is editorial criticism followed by safe fixes or proposals. But no supplied comparison result, named-use acceptance decision or ensuing accepted-claim integration is observed. Requested summaries and syntheses cannot yet be classified as entailed derivations or ampliative conjectures; neither entailment nor non-entailment has been shown for an actual produced claim. See [EPI-RTE-fidelity-review](#epi-rte-fidelity-review), [RT-RTE-health-audit](runtime.md#rt-rte-health-audit).

The wiki is licensed by the protocol for operational reliance in later answers without an intervening separately recorded truth-acceptance gate. Cross-library approval controls linking, not the truth of each linked claim. Output filing offers human control over reuse, not an explicit evidence-consuming truth test. Persistent instructions created during setup may alter later behavior without a truth-apt update. See [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer), [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile), [RT-RTE-library-setup](runtime.md#rt-rte-library-setup).

No run evidence establishes activation or improved future capacity. Model parameter change remains uninspected, while file-based retention remains a positive independent capacity. Editorial revision is prescribed; content-directed criticism, blame placement and iterative changed reliance for a particular formulated theory are not evidenced here. That limit does not collapse memory, autonomy, reflection or improvement into one system-wide verdict. No exercised evidence-responsive change to Funes's own method and later causally dependent operation is demonstrated. See [RT-CMP-librarian-model](runtime.md#rt-cmp-librarian-model), [RT-BAP-librarian-instructions](runtime.md#rt-bap-librarian-instructions), [EPI-RTE-fidelity-review](#epi-rte-fidelity-review).

## Shared records

### Operative objects

#### EPI-OBJ-raw
Label: Raw source record

Part of: [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree)

Identity: verbatim imported source documents under `raw/`, excluding the mutable registry. Natural-language source content and binary originals live in repository files. Claimed role is immutable evidence for compilation and later checking. Distinct from extracted sidecars: the original remains authoritative. Imported assertions can be truth-apt; factual source warrant is unknown. SRC-1, `protocol.md`, doctrine/design.

> - `raw/` — verbatim sources; **never edit content**.
> --- `protocol.md`

#### EPI-OBJ-pdf-text
Label: PDF extracted text edition

Part of: [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree)

Identity: PDF-derived text sidecar described by the protocol and implemented by the helper. Natural-language transcription with symbolic page/method boundaries and provenance text; filesystem text output. Default lineage includes filename, date, settings and versions; header omission is allowed. Different from the raw binary and compiled wiki. Content is a derivative representation, not independently checked testimony. SRC-1, `tools/pdf_text.py`, implementation; `protocol.md`, doctrine/design. Closest supplied route: [RT-RTE-pdf-sidecar](runtime.md#rt-rte-pdf-sidecar).

> "Machine-generated text; verify critical readings against the PDF.",
> --- `tools/pdf_text.py`

#### EPI-OBJ-captions
Label: Fetched captions and track metadata

Identity: result of [RT-RTE-caption-fetch](runtime.md#rt-rte-caption-fetch), not identical to the entire managed library: output may only go to stdout. Natural-language snippet text, symbolic video/language/generated fields and numerical timestamps live in transient objects or optional output files. JSON preserves a structured provenance envelope; default text does not embed it. Different from PDF transcription, though both are derived source representations. SRC-1, `tools/youtube_transcript.py`, implementation.

> "video_id": transcript.video_id,
> "language": transcript.language,
> "language_code": transcript.language_code,
> "generated": bool(transcript.is_generated),
> "snippets": transcript.to_raw_data(),
> --- `tools/youtube_transcript.py`

#### EPI-OBJ-wiki
Label: Compiled source notes concepts and topics

Part of: [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree)

Identity: `wiki/sources/`, `wiki/concepts/`, `wiki/topics/` content, distinct from source originals and generated outputs. Natural-language summaries/explanations/maps plus symbolic links and frontmatter, stored as Markdown. Semantic content enters through the external Librarian, not a shipped compiler. Claimed role: later question-answering context. SRC-1, `protocol.md`, doctrine/design. Minimum production passage is supplied in [RT-RTE-ingest-compile](runtime.md#rt-rte-ingest-compile); consumption passage in [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer).

#### EPI-OBJ-outputs
Label: Generated outputs

Part of: [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree)

Identity: substantial generated answers/reports/plans/routines saved to `outputs/`; durable portions may be offered for wiki filing. Natural-language prose and prescriptions plus symbolic citation links in Markdown files. Different consumer/admission horizon from wiki articles: initially human-facing, with optional later reuse. Not every prescription is truth-apt. SRC-1, `protocol.md`, doctrine/design; passage and closest route: [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer).

#### EPI-OBJ-audit-results
Label: Mechanical diagnostics and editorial health reports

Identity: audit CLI stdout/status and requested dated `meta/health/` reports. This crosses [RT-RTE-health-audit](runtime.md#rt-rte-health-audit) and [RT-OBJ-library-tree](runtime.md#rt-obj-library-tree), rather than being wholly part of the file tree: CLI status need not persist there. Symbolic findings/counts/status have fixed code consumers; prose editorial reports require model/human interpretation. Storage is stdout/CI logs for mechanical results and requested Markdown for editorial reports. Claimed role is triage, not fact certification. SRC-1, `tools/check_links.py`, `tools/compile_lint.py`, implementation; `protocol.md`, doctrine/design. Consumer details and passages are on the routes below.

### Routes

#### EPI-RTE-mechanical-checks
Label: Mechanical health evidence production

Part of: [RT-RTE-health-audit](runtime.md#rt-rte-health-audit)

Identity: checking phase only, distinct from exit-based disposition. Python reads the selected root/library Markdown and computes findings. The link target/domain is existence of parsed relative destinations, not actual support for cited propositions. Remote URLs and pure anchors are accepted without checking; fences, template files and documented missing-binary cases are excluded as coded. Orphan target is absence of a basename occurrence elsewhere in the library corpus; frontmatter target is opening `---`, not YAML validity.

Compile targets are normalized n-gram overlap in selected source summaries/concept leads, linked takeaway echoes, lead word counts and a selected raw/wiki word ratio. No source-fact oracle is consulted. Code decides matches under caller-selectable numeric thresholds; user or CI selects invocation, not individual findings. Ordinary maintenance mode; triggered by request or push/PR, not a controlled experiment. No product edit is proposed or admitted by this checking phase. SRC-1, `tools/check_links.py`, `tools/compile_lint.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: diagnostic findings and counts, subsequently consumed by the disposition phase.
- Later read-back: inapplicable — the check phase retains no knowledge or policy update for later agent invocation.
- Delegated visibility: inapplicable — local Python computation; no delegated agent or model call.
- Selection predicate: root/library discovery and parser-specific file/section filters, with optional orphan/frontmatter flags.
- Invalidation or expiry: fresh computation on invocation; no persistent certificate or incremental invalidation.
- Activation or effect: diagnostics produced without modifying content; status consumer is [EPI-RTE-audit-disposition](#epi-rte-audit-disposition).
- Evidence limits: no execution; derived findings are conditional on the file contents and coded parser domain, not semantic truth.

> if dest.startswith(("http://", "https://", "mailto:", "#")):
>     return True  # external or pure in-page anchor — not our concern
> --- `tools/check_links.py`

> if not open(p, encoding="utf-8").read().startswith("---"):
>     missing.append(p)
> --- `tools/check_links.py`

> if overlap(items[i][1], items[j][1]) >= pair_threshold:
>     pair_findings.append(sorted([items[i][0], items[j][0]]))
> --- `tools/compile_lint.py`

A deterministic counterexample to semantic certification follows directly from these predicates, without target execution. Two summaries `A cactus is a planet.` and `Whales are made of copper.` tokenize into disjoint short token sequences. `ngrams` returns one joined token string per summary when fewer than eight tokens; overlap is zero. Two items do not activate the five-owner template condition. With no concept-linked lines, these summaries produce no echo hits. Therefore the duplicate/echo gates can clear distinct invented assertions without any source read by the linter. This refutes the literal implication that clearing the template test necessitates reading sources, not the utility of duplicate detection. It licenses no claim about actual writer behavior. Counterevidence considered: strict mode can fail depth advisories, but still adds no source-to-claim comparison.

#### EPI-RTE-audit-disposition
Label: Audit exit and CI disposition

Part of: [RT-RTE-health-audit](runtime.md#rt-rte-health-audit)

Identity: findings to exit-code phase plus the shipped GitHub Actions consumer, not the checking phase. Python decides CLI success/failure. Link findings and compile duplicate/echo findings fail; compile depth advisories fail only with `--strict`. The shipped CI caller requests orphan/frontmatter checks and non-strict compile lint. GitHub consumes the step result within its audit job. This changes operational continuation/status, not truth endorsement or article retention. SRC-1, `tools/check_links.py`, `tools/compile_lint.py`, `.github/workflows/funes-lint.yml`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: CLI exit 0/1 and CI step outcome if invoked by the workflow.
- Later read-back: inapplicable — no automatic retained instruction or article update is written by this phase.
- Delegated visibility: CI checks out repository files and receives subprocess status; no model delegate.
- Selection predicate: counted problems and strict flag; CI selects the non-strict compile policy.
- Invalidation or expiry: rerun on invocation/push/PR; prior result is not a lasting semantic approval.
- Activation or effect: nonzero command status signals a failing audit step; advisories remain visible without failure in ordinary CI.
- Evidence limits: no job trace or branch-protection configuration; no merge veto, rollback or writer compliance is established.

No answer oracle or semantic acceptance criterion exists in this phase. Owner is the code rule and CI runner; a human can change invocation/policy, but there is no per-claim human admission. Trigger is maintenance, with no article-changing proposal, deployment or rollback in these read-only scripts.

> if args.strict:
>     return 1 if (gate_problems or advisory_flags) else 0
> return 1 if gate_problems else 0
> --- `tools/compile_lint.py`

> - name: Check Markdown links, orphans, and frontmatter
>   run: python3 tools/check_links.py --orphans --front
> - name: Check compile depth
>   run: python3 tools/compile_lint.py
> --- `.github/workflows/funes-lint.yml`

#### EPI-RTE-fidelity-review
Label: Editorial source fidelity review

Part of: [RT-RTE-health-audit](runtime.md#rt-rte-health-audit)

Identity: semantic evidence-production part of editorial health review, not automatic mechanical checking or subsequent fix admission. The linter design calls for adversarial LLM comparison of article and source; protocol assigns grounding/contradiction review to editorial work. Target/domain is fidelity of the compiled article to the source, not truth of every source assertion in the world. It supplies a candidate comparator but no fixed gold answer or calibrated oracle. No additional review runtime is shipped. SRC-1, `tools/compile_lint.py`, `tools/README.md`, `protocol.md`, doctrine/design. Closest later disposition is [RT-RTE-health-audit](runtime.md#rt-rte-health-audit).

- instruction conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: requested editorial finding/health report or criticism; no observed result supplied.
- Later read-back: requested dated health report may reach later review; no trace demonstrates reuse or changed reliance.
- Delegated visibility: uninspected — adversarial LLM review is named but no separate context/runner is implemented.
- Selection predicate: health request/periodicity and editorial judgment of duplicates, contradictions, grounding and gaps.
- Invalidation or expiry: inapplicable — no stored fidelity certificate or expiry contract specified.
- Activation or effect: requested findings can guide safe fixes or human proposals, not an enforcing semantic veto.
- Evidence limits: no paired source/article review result, decision record, criterion threshold or downstream acceptance instance.

The agent diagnoses; ordinary safe fixes are admitted by the Librarian, other changes are proposed to the human under the parent route. Proposed content persists only if subsequently edited/saved. Review guidance is source specificity, caveats, source links and repair rather than padding. Git/editorial redo afford recovery, not automatic dependent-claim withdrawal. No supplied theory-specific criticism names a challenged theory, test result and blame placement; the generic review mechanism does not establish those events or iteration.

> Fidelity is the job of an adversarial LLM review that actually reads source and
> article together — a *process* step, not a regex. See tools/README.md.
> --- `tools/compile_lint.py`

> contradiction, grounding, and gap review beyond them remains editorial.
> --- `protocol.md`

#### EPI-RTE-caption-reshape
Label: Caption plain text reshaping

Part of: [RT-RTE-caption-fetch](runtime.md#rt-rte-caption-fetch)

Identity: local plain-text branch after acquisition, not remote selection or extraction. Python normalizes each snippet's whitespace, skips empty snippets, optionally prefixes its start timestamp and joins lines. Input is returned snippet text; output is the text fed to `write_output`, with track metadata separately printed to stderr. Within ordinary prose transcription this is non-ampliative reshaping, not generation of a new speech claim. SRC-1, `tools/youtube_transcript.py`, implementation.

Concrete implementation deduction, not execution: snippet text `Water\n  boils.` becomes `Water boils.` through `split` and join. An all-whitespace snippet is skipped. With timestamps disabled, start/duration do not appear in the text body. Thus the speech wording is reshaped while timing context is removed. JSON instead retains the raw-data envelope; SRT/VTT formatting is delegated to the external package and its exact transformation is uninspected. Layout-sensitive meanings remain outside this bounded preservation claim.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: rendered text passed to stdout/file writer, with separate stderr metadata.
- Later read-back: possible through caller-saved/ingested output; no automatic library registration or later delivery.
- Delegated visibility: inapplicable — this branch is local serialization, not an agent call.
- Selection predicate: text format, nonempty normalized snippets, optional timestamps flag.
- Invalidation or expiry: inapplicable — no retained cache validity rule; caller can refetch/rewrite output.
- Activation or effect: transformed transcript becomes caller-visible content; no factual approval or wiki write.
- Evidence limits: upstream recognition/selection is external and unobserved; formatting cannot validate spoken propositions.

The caller selects format and source; code admits nonempty text without per-snippet human approval or an answer oracle. This is targeted extraction mode. Errors/recovery and overwrite behavior remain as on the supplied parent route, not a second admission policy.

> text = " ".join(snippet.text.split())
> if not text:
>     continue
> --- `tools/youtube_transcript.py`

### Claims

#### EPI-CLM-library-abstraction
Label: Maintained library abstraction and reuse

Claimed operation: preserve raw sources, abstract them into concepts/topics, reuse the wiki for cited outputs and ongoing coherence. SRC-1, `README.md`, doctrine/design. Distinct from [RT-CLM-library-guarantees](runtime.md#rt-clm-library-guarantees), which owns immutable-raw/citation guarantees: this record owns abstraction and later working-memory use. Neither source provides an observed abstraction run or causal efficacy measurement.

> This project preserves the raw record, then abstracts it into concepts, topics, and usable outputs.
> --- `README.md`

> The wiki is not the end product. It is the working memory the Librarian uses to answer questions, generate reports, produce routines, notice gaps, and keep the knowledge base coherent over time.
> --- `README.md`

#### EPI-CLM-compile-depth
Label: Compile depth gates and fidelity limits

Claimed operation/warrant: duplicate/echo gates detect failures of substantive compilation, with a stronger rationale that clearing template reuse requires source reading. The source itself explicitly disclaims automated factual-grounding checks and assigns fidelity to editorial comparison. SRC-1, `tools/compile_lint.py`, `tools/README.md`, doctrine/design. The historical shallow-compile episode is reported operation only. This is a distinct tool-warrant claim, not a duplicate of [RT-CLM-library-guarantees](runtime.md#rt-clm-library-guarantees). Implemented counterexample and bounded supported warrant are on [EPI-RTE-mechanical-checks](#epi-rte-mechanical-checks).

> The only way to clear (a) is
>             to write genuinely distinct summaries, i.e. to read the sources.
> --- `tools/compile_lint.py`

> Deliberately NOT here: an automated *grounding / fidelity* check (does every
> proper noun / date in an article appear in its cited source?).
> --- `tools/compile_lint.py`
