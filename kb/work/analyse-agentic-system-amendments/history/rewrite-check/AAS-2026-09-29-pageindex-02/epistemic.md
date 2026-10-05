---
type: types/agentic-system-epistemic-report.md
description: "Epistemic routes of PageIndex local mode at d2693d80: which model-written and imported index content is checked or unchecked, and why answers and citations carry no verified warrant"
run-id: AAS-2026-09-29-pageindex-02
reviewed-boundary: "d2693d80791a86345ef78b3234834f5fe53a70a0"
---

# PageIndex epistemic report

## Source-and-claim boundary

**Lens scope.** The frozen boundary and source register are those of `boundary.md` (whole-system, code-grounded, SRC-1 implementation, SRC-2 design, SRC-3 reported operation, SRC-4 unprovenanced outputs); this member does not copy them. The lens covers local mode: what PageIndex imports from a PDF, what models write into the index, what checks and admission rules act on that content, what is retained, and what the chat agent and its citations do with it at query time. Excluded components are those `boundary.md` excludes: the cloud service, the App, host runtimes, model providers, external benchmarks and repository automation.

**Analysis question.** Does PageIndex acquire or produce truth-apt content, check it, grant reliance on it, retain it, and let it affect later behavior, and by which routes?

**Assessed route families.** Index-time structure import (embedded bookmarks, layout detection, standard-mode table-of-contents extraction), index-time model-written text (summaries, document description, expand proposals), index-time admission checks and thresholds (RT-RTE-8, RT-RTE-9), retention in the store (RT-RTE-1), query-time reading and answering (RT-RTE-2), and citation tag resolution.

**Unassessed route families and the conclusions their omission prevents.**

- Cloud-mode routes (RT-RTE-6, RT-BAP-4): no conclusion about cloud-side checking, retrieval, or served instructions.
- Markdown pipeline (RT-RTE-7): read only for its place in the entry paths; no conclusion about its content routes.
- Flash layout heading detection and the pdfium and PyPDF2 text extractors, read only as far as EPI-OBJ-8 and EPI-OBJ-9 state: no conclusion about heading precision or extraction fidelity.
- Host adapter loops (RT-RTE-4) and the Responses and Messages lanes (RT-RTE-5): no conclusion about host-side checking.
- All model behavior: whether summaries are faithful, whether the chat model follows its grounding instructions, and whether answers are correct are not determined by any evidence here.

**Missing evidence.** No run was performed (see the runtime report's Execution preflight), so every route has implementation evidence at most. SRC-4 outputs carry no provenance, so no observed candidate state is recorded for any object. SRC-3 figures are reported, not observed, which prevents any causal or accuracy conclusion.

**Knowledge-production or warrant claims.** RT-CLM-1 (relevance by reasoning), RT-CLM-2 (accuracy and cost figures), RT-CLM-3 (FinanceBench accuracy), RT-CLM-5 (traceable and explainable retrieval). RT-CLM-4 states a deployment property and makes no warrant claim.

**Runtime wording corrected here.** The runtime report's Loop 2 says page-level citations are "checked only by `get_citations` and `resolve_citations`". Those functions resolve a cited document name to a document id and rewrite tags; they check nothing about whether a cited page exists or supports the claim (EPI-RTE-3, EPI-ABS-2). The reconciliation amends the wording.

## Epistemic-object inventory

| object ID | candidate truth-apt content or none | claimed role | evidence source ID and local anchor | gap/limit |
|---|---|---|---|---|
| EPI-OBJ-1 | Per-node statements of what a page range covers | Lets the chat model choose page ranges from the outline | SRC-1 `pageindex/utils.py` | Fidelity to the page text never checked (EPI-ABS-1) |
| EPI-OBJ-2 | Embedded PDF bookmark titles and target pages | Frame for the section tree | SRC-1 `pageindex/flash/embedded_toc.py` | Correctness of the PDF author's bookmarks not established |
| EPI-OBJ-3 | One-sentence statement distinguishing the document | Lets the chat model match documents to a question | SRC-1 `pageindex/utils.py` | Not checked (EPI-ABS-1); empty after a 400 |
| EPI-OBJ-4 | Model-proposed child headings with start pages | Refines coarse nodes | SRC-1 `pageindex/tree_optimize.py` | Only printed-heading presence is checked |
| EPI-OBJ-5 | Standard-mode section titles, hierarchy indices and physical pages | The tree for PDFs processed in standard mode | SRC-1 `pageindex/page_index_classic.py` | Verified by the proposing model, not independently |
| EPI-OBJ-6 | Chat answer text with `<cite>` tags | The system's answer to the caller | SRC-1 `pageindex/local_chat.py` | No check or acceptance (EPI-ABS-2) |
| EPI-OBJ-7 | Resolved citation entries `{document, doc_id, page}` | Display-ready links to cited pages | SRC-1 `pageindex/client.py` | Resolve a name to an id only (EPI-RTE-3) |
| EPI-OBJ-8 | Layout-detected section titles and page ranges | Default source of tree structure | SRC-1 `pageindex/flash/main.py` | Detection heuristics not inspected here |
| EPI-OBJ-9 | Index-time page text from pdfium layout parsing | Text on which summaries, expand and checks operate | SRC-1 `pageindex/flash/main.py` | Different extraction from RT-OBJ-2; not retained |
| RT-OBJ-2 | Page text from PyPDF2 | Only text the agent can read | see RT-OBJ-2 | Extraction fidelity uninspected |
| RT-OBJ-1 | Container: titles and ranges (EPI-OBJ-8, EPI-OBJ-2, EPI-OBJ-4, EPI-OBJ-5) and summaries (EPI-OBJ-1) | See split | see RT-OBJ-1 | Split here by producer and check |
| RT-OBJ-3 | Container: the model-written description is EPI-OBJ-3; other fields are symbolic metadata | See split | see RT-OBJ-3 | None beyond the split |
| RT-OBJ-5 | The cost theory of RT-RTE-8 (consumed, not produced) | Admission rule for expansion | see RT-OBJ-5 | See RT-RTE-8 theory route |
| RT-OBJ-4 | none | Instruction text | see RT-OBJ-4 | Prompt-level guidance, not content the system asserts |

## Authority-route ledger

Local tags L1a to L11 label ledger rows only. The status vocabulary is the report type's: architectural status here never carries an observation, and no run was made.

**L1a. Bookmark validation and tiering (EPI-RTE-1), check/evidence production.**
- Architectural status: `implemented`. Object: EPI-OBJ-2. Relation: `no content change` (drops out-of-range and backward entries).
- Target: each bookmark entry's page is in range and does not precede an earlier entry, and the set is not generic or an enumeration. Evaluator: program, on titles and page numbers only.
- Activation: default on (`use_embedded_toc=True`), index time, PDFs with an outline. Result: surviving entries and a tier (`FULL`, `SKELETON`, `IGNORE`). Force: enforcing on the tree frame.
- Epistemic authority: surviving entries are well formed by these rules; nothing about whether the titles name real sections. Operational: permits or blocks the frame. Behavioral-authority path: EPI-BAP-1.
- Anchor: SRC-1 `pageindex/flash/embedded_toc.py`. Claims: none. Mismatch: the module docstring says the feature is opt-in and the default path never imports it, while the SDK and CLI defaults enable it (`pageindex/local_api.py`, `pageindex/flash/main.py`); the docstring is stale, the code is authoritative. Limit: no bookmark set was tested.

**L1b. Bookmark frame admission (EPI-RTE-1), operational admission/selection/consumption.**
- Status: `implemented`. Object: EPI-OBJ-2 into RT-OBJ-1. Relation: `truth-apt transformation: acquisition/import`, source warrant: titles preserved, target-page positions degraded (see EPI-OBJ-2).
- Target: the choice of frame tier. Evaluator: program. Activation: after L1a. Result: `FULL` replaces the detected hierarchy without a page-text check of the bookmark entries; `SKELETON` re-hangs detected nodes and checks deeper sparse entries against page text (L1c).
- Force: enforcing. Epistemic authority: none stated. Operational: bookmark frame becomes the stored tree. Path: EPI-BAP-1. Anchor: SRC-1 `pageindex/flash/embedded_toc.py`. Claims: none. Mismatch: none. Limit: FULL-tier acceptance rests on the bookmark author.

**L1c. Skeleton fill-in verification (EPI-RTE-1), check/evidence production.**
- Status: `implemented`. Object: EPI-OBJ-2. Relation: `no content change` (filters fill-in entries); a same-page title within similarity 0.7 overwrites a detected title (non-ampliative reshaping).
- Target: a deeper bookmark title appears on its target page or a neighbour, in normalized form. Evaluator: program over EPI-OBJ-9 text. Activation: `SKELETON` tier only, and only when page text exists. Result: entry kept or dropped. Force: enforcing on admission.
- Epistemic authority: the title string occurs on or next to the target page; not that it starts a section. Operational: admits the entry. Path: EPI-BAP-1. Anchor: SRC-1 `pageindex/flash/embedded_toc.py`. Claims: none. Mismatch: none. Limit: text extraction quality.

**L2a. Raw-text leaf summary (EPI-RTE-2), content transformation.**
- Status: `implemented`. Object: EPI-OBJ-1. Relation: `truth-apt transformation: non-ampliative reshaping` (a leaf under 200 tokens keeps its own text, stripped).
- Check: none needed for fidelity; the text is the source text of EPI-OBJ-9. Force: advisory, through the outline. Epistemic authority: the text is the page text as extracted. Operational: shown to the chat model. Path: RT-BAP-2. Anchor: SRC-1 `pageindex/utils.py`. Claims: none. Mismatch: none. Limit: extraction fidelity.

**L2b. Model-written summary and description (EPI-RTE-2), content transformation.**
- Status: `implemented`. Objects: EPI-OBJ-1, EPI-OBJ-3. Relation: `truth-apt transformation: indeterminate`; classifications still possible: non-ampliative compression, ampliative conjecture where the model adds or generalizes; evidence needed: a comparison of stored summaries against their page text.
- Target: none; no check runs (EPI-ABS-1). Evaluator: none. Activation: index time, every non-leaf and long leaf node, and once per document. Result: text stored; a failed call stores an empty summary. Force: advisory. Epistemic authority: none licensed. Operational: the chat model chooses documents and page ranges from these texts. Path: RT-BAP-2.
- Anchor: SRC-1 `pageindex/utils.py`. Claims: RT-CLM-1, RT-CLM-5 (indirectly). Mismatch: the prompt asks to summarize "without omitting" content, but nothing tests that instruction. Limit: model behavior uninspected.

**L3. Retention of the tree and pages (RT-RTE-1), retention.**
- Status: `implemented`. Objects: RT-OBJ-1, RT-OBJ-2, RT-OBJ-3. Relation: `no content change`. Target: none. Evaluator: none besides the page-bounds refusal in `pageindex/local_api.py`, which checks ranges, not content.
- Force: none; storage. Epistemic authority: none granted by retention. Operational: makes the tree readable by later runs. Path: RT-BAP-2. Anchor: SRC-1 `pageindex/local_store.py`. Claims: none. Mismatch: none. Limit: lifecycle integration `not reached` for every model-written item, since no acceptance exists.

**L4a. Expand proposal (RT-RTE-8), content transformation.**
- Status: `implemented`. Object: EPI-OBJ-4. Relation: `truth-apt transformation: indeterminate`; classifications still possible: acquisition/import of printed headings, ampliative conjecture about nesting; evidence needed: comparing accepted children with the document's real outline.
- Evaluator: none at this step. Activation: node over 5 pages with no children. Result: candidate list. Force: none until L4b. Path: EPI-BAP-1. Anchor: SRC-1 `pageindex/tree_optimize.py`. Claims: none. Mismatch: none.

**L4b. Printed-heading check (RT-RTE-8), check/evidence production.**
- Status: `implemented`. Object: EPI-OBJ-4. Relation: `no content change` (filters candidates).
- Target: the proposition that a proposed title is printed on its claimed page, with the page in range, order preserved, no duplicate. Evaluator: program over EPI-OBJ-9 text after normalization (substring). Result: candidate kept or dropped. Force: enforcing on candidate admission.
- Epistemic authority: the normalized title string occurs in the index-time text of that page; not that it is a heading, its level, or that it starts a section (a title inside running prose passes). Operational: filters proposals before pricing. Path: EPI-BAP-1. Anchor: SRC-1 `pageindex/tree_optimize.py`. Claims: none. Mismatch: none. Limit: the check uses pdfium text, while the agent reads PyPDF2 text (EPI-OBJ-9, RT-OBJ-2).

**L4c. Cost-rule disposition (RT-RTE-8), operational admission/selection/consumption.**
- Status: `implemented`. Object: EPI-OBJ-4 and RT-OBJ-5. Relation: `no content change` (selects among candidate levels, or keeps the node collapsed).
- Target: which candidate level has the lower modelled search cost. Evaluator: computation over the cost theory in RT-OBJ-5. Result: expand, or keep collapsed and freeze. Force: enforcing on tree shape. Epistemic authority: none about retrieval quality; the theory is untested against retrieval outcomes within the boundary. Operational: sets the stored tree shape. Path: EPI-BAP-1.
- Anchor: SRC-1 `pageindex/tree_optimize.py`. Claims: RT-CLM-2 (effect is README-reported only). Mismatch: none. Limit: no run.

**L5a. Standard-mode structure extraction (RT-RTE-3, RT-RTE-9), content transformation.**
- Status: `implemented`. Object: EPI-OBJ-5. Relation: `truth-apt transformation: indeterminate`; classifications still possible: acquisition/import (titles and pages transcribed from a printed contents list or from body text), ampliative conjecture (hierarchy and page assignment inferred by the model in the no-contents mode); evidence needed: comparison with the printed outline.
- Evaluator: none at this step. Result: entries with physical pages. Force: none until L5b. Path: EPI-BAP-1. Anchor: SRC-1 `pageindex/page_index_classic.py`. Claims: none. Mismatch: none.

**L5b. Title-appearance check (RT-RTE-9), check/evidence production.**
- Status: `implemented`. Object: EPI-OBJ-5. Relation: `no content change`.
- Target: the proposition that a given section title appears or starts in its assigned page's text. Evaluator: the index model (the same RT-CMP-1 that proposed the entry) under a different prompt, with fuzzy matching; not independent of the proposer. A failed call is skipped, and a reply without an `answer` field counts as `no`.
- Result: per-entry yes or no, and an accuracy over answered checks. Force: enforcing (feeds L5c). Epistemic authority: a model judged the title present on that page; no evidence of the judge's error rate. Operational: selects repair or fallback. Path: EPI-BAP-1. Anchor: SRC-1 `pageindex/page_index_classic.py`. Claims: none. Mismatch: none. Limit: model behavior uninspected.

**L5c. Threshold disposition and repair (RT-RTE-9), operational admission/selection/consumption.**
- Status: `implemented`. Object: EPI-OBJ-5. Relation: `truth-apt transformation: indeterminate` for repaired pages (the model proposes a new page, and the same model re-checks it); otherwise `no content change`.
- Target: whether the structure is usable. Evaluator: computation over L5b results. Result: all confirmed accepts; more than 0.6 with mistakes repairs for up to 3 rounds and then returns the tree; otherwise falls back to the next mode; the last mode raises. Force: enforcing.
- Epistemic authority: an accepted tree passed a model check, or was returned with entries still judged incorrect after the repair attempts; the second case carries no residual-error flag in the stored tree. Operational: the tree is stored either way. Path: EPI-BAP-1.
- Anchor: SRC-1 `pageindex/page_index_classic.py`. Claims: none. Mismatch: none. Limit: residual mistakes are logged, not stored (see the quote in EPI-OBJ-5).

**L6. Discovery self-check (RT-RTE-2, RT-OBJ-4), check/evidence production.**
- Status: `implemented` as delivered instruction text; whether the model applies it is unobserved. Object: EPI-OBJ-3 and RT-OBJ-3 metadata. Relation: `no content change`.
- Target: whether the documents that discovery returned match the user's intent. Evaluator: the chat model (RT-CMP-2), by instruction. Activation: every discovery. Result: continue a persistence protocol or proceed. Force: advisory. Epistemic authority: none recorded. Operational: may trigger further browsing. Path: RT-BAP-1. Anchor: SRC-1 `pageindex/agent_tools.py`. Claims: none. Mismatch: none.

**L7. Answer generation (RT-RTE-2), content transformation.**
- Status: `implemented` as the chat lanes. Object: EPI-OBJ-6. Relation: `truth-apt transformation: indeterminate`; classifications still possible: extractive restatement, entailed derivation over page text, ampliative conjecture or unsupported general knowledge; evidence needed: per-answer comparison with the pages read.
- Target: none. Evaluator: none. Activation: each chat call. Result: answer text. Force: advisory to the caller. Epistemic authority: none granted by the system; the grounding instruction asks the model to "state only what was actually read" but is not enforced. Operational: returned to the caller. Path: RT-BAP-1, RT-BAP-3.
- Anchor: SRC-1 `pageindex/local_chat.py`. Claims: RT-CLM-1, RT-CLM-3. Mismatch: see block 5. Limit: no model call was run.

**L8. Citation emission (RT-RTE-2), other: model-written provenance annotation.**
- Status: `implemented` as instruction text (`citations=True`). Object: EPI-OBJ-6. Relation: `truth-apt transformation: indeterminate` (a tag asserts that a page supports a statement; whether it does is unchecked).
- Evaluator: none. Force: advisory. Epistemic authority: none. Operational: gives a reader a page to open. Path: RT-BAP-1. Anchor: SRC-1 `pageindex/agent_tools.py`. Claims: RT-CLM-5. Mismatch: see block 5.

**L9. Citation resolution (EPI-RTE-3), other: reference resolution, not a support check.**
- Status: `implemented`. Object: EPI-OBJ-7. Relation: `truth-apt transformation: non-ampliative reshaping` (tags become numbered links, and each document name becomes a document id or none).
- Target: none about support; only name lookup. Evaluator: program. Result: `{document, doc_id, page}` entries; an unknown document keeps `doc_id: None`. Force: none. Epistemic authority: none about whether the page exists or supports the claim. Operational: display links for the caller.
- Path: none consequential. Anchor: SRC-1 `pageindex/client.py`. Claims: RT-CLM-5. Mismatch: see block 5. Limit: block-level citation lookup is cloud-only.

**L10. Behavior or policy adaptation from evaluation (RT-RTE-8, RT-RTE-9).**
- Architectural status: `no route found within boundary`. Relation: `no content change`. The optimize report and classic `accuracy` are computed and are not read by a later round (RT-ABS-2); no query outcome adapts anything (RT-ABS-1). Scope: `pageindex/` at the frozen commit; cloud and provider-side adaptation are outside it.

**L11. Query-time consumption of the tree (RT-RTE-2), operational admission/selection/consumption.**
- Status: `implemented`. Objects: RT-OBJ-1, RT-OBJ-2, EPI-OBJ-1. Relation: `no content change`. Evaluator: the chat model chooses ranges from the outline. Force: advisory (ranking by model judgment). Result: page reads up to a character budget. Epistemic authority: none. Operational: determines which pages enter the answering context. Path: RT-BAP-2. Anchor: SRC-1 `pageindex/agent_tools.py`. Claims: RT-CLM-1. Mismatch: none. Limit: whether summaries changed answers is not established (RT-RTE-1 activation).

## Per-object lifecycle disposition

No candidate is established as ampliative, so the discovery lifecycle is not applied to any object and no phase is assigned an observed candidate state. Each record below is the indeterminate or non-ampliative form. SRC-4 outputs carry no provenance, which is why no phase is `phase evidenced` for any object.

| candidate object ID | relevant route IDs | transformation | classifications still possible | preserved lineage | implemented checks, retention, or use | current warrant limit | evidence needed to decide |
|---|---|---|---|---|---|---|---|
| EPI-OBJ-1 | EPI-RTE-2 | indeterminate | non-ampliative compression; ampliative where the model adds | Node page range, so the source pages are recoverable | No check (EPI-ABS-1); stored in RT-OBJ-1; shown in the outline | None licensed | Stored summaries compared with their page text |
| EPI-OBJ-3 | EPI-RTE-2 | indeterminate | as EPI-OBJ-1, at document scale | Built from the tree, not from pages | No check; stored in RT-OBJ-3; shown in discovery | None licensed | Descriptions compared with the document |
| EPI-OBJ-4 | RT-RTE-8 | indeterminate | acquisition/import of printed headings; ampliative about nesting | Page number and printed-title match | Printed-heading and order checks, then cost rule | Presence of the title string on the page (pdfium text) | Accepted children compared with the real outline |
| EPI-OBJ-5 | RT-RTE-3, RT-RTE-9 | indeterminate | acquisition/import; ampliative in the no-contents mode | Physical page per entry | Model title-appearance check, threshold, bounded repair | A model judged presence; residual errors possible | Entries compared with the printed outline |
| EPI-OBJ-6 | RT-RTE-2 | indeterminate | extractive; entailed; ampliative; general-knowledge insertion | Optional page-level `<cite>` tags | None; returned to the caller | None granted | Per-answer comparison with the pages read |

| candidate object ID | relevant route IDs | transformation | discovery lifecycle | applicable acquisition, lineage, derivation, or update route and warrant | missing evidence/limit |
|---|---|---|---|---|---|
| EPI-OBJ-2 | EPI-RTE-1 | acquisition/import | not applicable | Bookmarks imported from the PDF with well-formedness rules; title warrant preserved, page-position warrant degraded | Correctness of the PDF author's bookmarks |
| EPI-OBJ-7 | EPI-RTE-3 | non-ampliative reshaping | not applicable | Name-to-id resolution of model-written tags | Support of the cited page for the claim |
| EPI-OBJ-8 | RT-RTE-1 | acquisition/import (layout detection) | not applicable | Symbolic detection over the PDF; source warrant unknown | Detection precision; heuristics not inspected here |
| EPI-OBJ-9 | RT-RTE-1 | acquisition/import | not applicable | pdfium layout text; not retained; warrant unknown | Agreement with the PyPDF2 text the agent reads |

No lifecycle record for RT-OBJ-4: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: none.
No lifecycle record for RT-OBJ-5: no candidate truth-apt output for this object (a consumed cost theory); relevant direct-adaptation or update routes: none (RT-ABS-2).
No lifecycle record for RT-OBJ-2: it is imported page text with source warrant unknown, not a produced candidate; see EPI-OBJ-9 for the text used at index time.

## System-claim versus route comparison

| claim ID | claimed operation or warrant | claim source ID/anchor and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support and design limits | supported conclusion | mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| RT-CLM-1 | Reasoning over a tree replaces vector similarity and finds what is relevant | SRC-2 `README.md`, doctrine/design | README argument that similarity is not relevance | RT-RTE-2, RT-ABS-4, EPI-RTE-2 | none | none; no comparison inside the boundary | Retrieval is model choice over model-written summaries; the routes contain no relevance check | Relevance of returned pages is never checked; whether summaries carry the relevance signal is unknown |
| RT-CLM-2 | Cost, time and accuracy figures on a 62-question benchmark | SRC-3 `README.md`, reported operation | Figures and charts | RT-RTE-1, RT-RTE-2 | none | Benchmark runners not frozen | Only that the README reports them | Cannot be tied to this commit or to a component |
| RT-CLM-3 | 98.7% on FinanceBench, above vector RAG | SRC-3 `README.md`, reported operation | Linked blog for a system named Mafin 2.5 | RT-RTE-2 | none | External benchmark; no contrast varying one component | Only that the README reports it | The linked system may not be this SDK's local mode |
| RT-CLM-5 | Retrieval is traceable and explainable | SRC-2 `README.md`, doctrine/design | Page-level citation tags and `show_process` events | EPI-RTE-3, RT-RTE-2 | none | none | Traceability to a named page exists as a model-written tag plus a name lookup; support of the claim by the page is unchecked | "Traceable to explicit references" holds for the tag's addressability, not for verification of the cited statement |

## Bounded conclusion

- **Import versus production.** PageIndex imports document structure and text: bookmarks (EPI-OBJ-2), layout detection (EPI-OBJ-8) and page text (RT-OBJ-2, EPI-OBJ-9). Source warrant is preserved for bookmark titles, degraded for bookmark page positions, and unknown for detected structure and extracted text. It produces model-written text (EPI-OBJ-1, EPI-OBJ-3, EPI-OBJ-4, EPI-OBJ-5, EPI-OBJ-6) whose relation to its inputs is indeterminate, not established as compression or as ampliation.
- **Checks that exist.** Programs check bookmark well-formedness, expand candidates against printed-heading presence and order, and expand shape against a cost rule. A model checks standard-mode entries against page text, and it is the same model that proposed them. Each check licenses only its stated proposition.
- **Checks that are missing.** No route checks summaries or descriptions against their pages (EPI-ABS-1). No route checks answers, the pages an answer used, or whether a citation is supported (EPI-ABS-2). Citation resolution is a name lookup.
- **Acceptance and integration.** No route records an evidence-consuming acceptance of a truth-apt claim against a criterion, so no ampliative candidate is accepted and lifecycle integration is not reached for any object. Retention (L3) and operational consumption (L11) occur without acceptance.
- **Authority.** Admission checks are enforcing on tree shape (EPI-BAP-1). Summaries, descriptions and instructions are advisory to the chat model (RT-BAP-1, RT-BAP-2). Nothing adapts behavior or policy from evaluation (L10).
- **Text used at index time and at query time differ.** Summaries and heading checks in the flash lane use pdfium layout text while the agent reads PyPDF2 text (EPI-OBJ-9, RT-OBJ-2); only a page-range bound reconciles them.
- **Claims left unsupported.** RT-CLM-1, RT-CLM-2, RT-CLM-3 and RT-CLM-5 lack implementation-level support for their warrant reading, and none has observed-run or causal evidence. The scope is an operational retrieval system for a caller who holds the answer's warrant; this is a scope boundary, not a defect, but it bears on how "traceable" and "explainable" can be read.
- **Not concluded.** Whether the models behave as instructed, whether summaries help, and cloud-side behavior.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-1 — Node summary text

Part of: RT-OBJ-1
- **Source-native identity.** The `summary` field of each tree node, written by `_leaf_summary`, `_parent_summary` and `generate_node_summary` in SRC-1 `pageindex/utils.py`. A leaf under `SUMMARY_RAW_TEXT_TOKENS` (200) reuses its own text. A parent summary sees at most 3 leading uncovered pages plus child summaries. This record owns the scoped part; the container retains its identity.
- **Form and substrate.** Natural language in `tree.json`.
- **Evidence.** SRC-1 `pageindex/utils.py`. The leaf prompt:

> summarizing all its points without omitting any type of content.
>     Keep the description concise
> --- `pageindex/utils.py:981-982` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`
- **Limits.** The instruction to summarize "without omitting" content is prompt-level. `parse_summary` accepts a JSON `summary` field or the raw reply, and an empty reply is stored as an empty summary.

#### EPI-OBJ-2 — Embedded bookmark set
- **Source-native identity.** Entries `{title, level, page}` read with pdfium from the PDF outline and validated by `validate_bookmarks`. SRC-1 `pageindex/flash/embedded_toc.py`.
- **Form and substrate.** Natural-language titles and integer pages, held in memory during indexing; the merged result persists inside RT-OBJ-1.
- **Evidence.** The module states the position limit of a bookmark target:

> a bookmark target carries no reliable
> on-page position
> --- `pageindex/flash/embedded_toc.py:32-33` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

  And the well-formedness rule for a bookmark set:

> Bookmarks must walk forward through the document: an entry whose
>     target page precedes an earlier entry's is dropped.
> --- `pageindex/flash/embedded_toc.py:153-154` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`
- **Limits.** Titles never pass through text extraction, which is why the code repairs garbled detected titles from them. The FULL-tier merge receives no page text, so those entries are not checked against it.

#### EPI-OBJ-3 — Document description

Part of: RT-OBJ-3
- **Source-native identity.** The `description` string produced by `generate_doc_description` from the cleaned tree structure. SRC-1 `pageindex/utils.py`. This record owns the scoped part; the container retains its identity.
- **Form and substrate.** One natural-language sentence in `doc.json`.
- **Evidence.** The prompt:

> Your task is to generate a one-sentence description for the document, which makes it easy to distinguish the document from other documents.
> --- `pageindex/utils.py:1127-1127` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`
- **Limits.** A 400 from the model on the unbounded whole-tree prompt yields an empty description. The sentence is written from the tree, which is itself model-written. The chat model is instructed to judge whether discovered documents match the user's intent (L6), and the instruction is prompt text only:

> Results returned ≠ correct results.
> --- `pageindex/agent_tools.py:1609-1609` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

#### EPI-OBJ-4 — Expand child proposals
- **Source-native identity.** The candidate `subsections` list returned by the model in `propose_children`, before filtering. SRC-1 `pageindex/tree_optimize.py`. Possible duplicate: none; RT-RTE-8 covers the mechanism and RT-OBJ-1 the surviving nodes.
- **Form and substrate.** Natural-language titles with integer pages, transient during indexing.
- **Evidence.** SRC-1 `pageindex/tree_optimize.py`; the printed-heading filter is quoted at RT-RTE-8, not here.
- **Limits.** A proposal filtered out leaves no record.

#### EPI-OBJ-5 — Standard-mode table-of-contents entries
- **Source-native identity.** Entries `{structure, title, physical_index}` built by `toc_transformer`, `generate_toc_init` and related calls, verified by `verify_toc` and repaired by `fix_incorrect_toc`. SRC-1 `pageindex/page_index_classic.py`.
- **Form and substrate.** Natural language plus integers, in memory, then inside RT-OBJ-1.
- **Evidence.** The check prompt:

> Your job is to check if the given section appears or starts in the given page_text.
> --- `pageindex/page_index_classic.py:91-91` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`
- **Limits.** The checker and the proposer are the same configured model. The loop bound leaves entries judged incorrect in the result:

> logger.info("Maximum fix attempts reached")
> --- `pageindex/page_index_classic.py:1057-1057` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

#### EPI-OBJ-6 — Chat answer with citation tags
- **Source-native identity.** The model's final output, returned as `result.final_output` in the chat lanes. SRC-1 `pageindex/local_chat.py`, `pageindex/agent_tools.py`.
- **Form and substrate.** Natural language with optional `<cite doc= page=/>` tags; not stored by PageIndex.
- **Evidence.** The output is returned without post-processing:

> "content": result.final_output or ""},
> --- `pageindex/local_chat.py:990-990` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

  The citation instruction:

> Cite only statements supported by tool outputs: <cite doc="{docName}" page="{pageNumber}"/>
> --- `pageindex/agent_tools.py:1651-1651` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`
- **Limits.** The grounding rules are instruction text; no code enforces them.

#### EPI-OBJ-7 — Resolved citation entries
- **Source-native identity.** Dicts returned by `get_citations` and `resolve_citations`. SRC-1 `pageindex/client.py`.
- **Form and substrate.** Symbolic dicts and rewritten answer text.
- **Evidence.** The entry constructed for each parsed tag:

> entry: dict[str, Any] = {"document": citation["document"],
>                                      "doc_id": ids[0] if ids else None,
>                                      "page": citation["page"]}
> --- `pageindex/client.py:2470-2472` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

  A test shows an unknown document yielding `doc_id: None` with its page kept:

> {"document": "other.pdf", "doc_id": None, "page": 2},
> --- `tests/test_client.py:620-620` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`
- **Limits.** Block-level lookup is cloud-only.

#### EPI-OBJ-8 — Layout-detected section titles and ranges
- **Source-native identity.** The `structure` produced by `extract_toc` from layout statistics before any bookmark merge. SRC-1 `pageindex/flash/main.py`.
- **Form and substrate.** Natural-language titles and integer ranges, symbolic derivation.
- **Evidence.** SRC-1 `pageindex/flash/main.py`, `pageindex/flash/api.py`; the refusal rule `flash_rejection_reason` is described at RT-RTE-1.
- **Limits.** The heuristics were not inspected beyond how their output is consumed. `validate` issues in RT-RTE-8 do not block storing.

#### EPI-OBJ-9 — Flash index-time page text
- **Source-native identity.** `page_texts` assembled from pdfium layout blocks in `extract_toc`, passed to summaries, expand and heading checks. SRC-1 `pageindex/flash/main.py`, `pageindex/flash/api.py`. Possible duplicate: none; RT-OBJ-2 is the different, stored PyPDF2 text.
- **Form and substrate.** Natural language, in memory, not stored.
- **Evidence.** The store reconciles the two extractions only by range:

> The tree (pdfium) and stored pages (PyPDF2) come from different
>         parsers; a span outside 1..page_count IndexErrors every later read.
> --- `pageindex/local_api.py:193-194` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`
- **Limits.** Agreement between the two texts is unchecked, so a heading confirmed in one may be absent from what the agent reads.

### Routes

#### EPI-RTE-1 — Embedded bookmark validation, tiering and merge

Part of: RT-RTE-1
- **Endpoints and progression.** `extract_toc` → `apply_embedded_toc` → `read_bookmarks` → `validate_bookmarks` → `classify_bookmarks` → `merge_bookmark_tree` (FULL), `merge_bookmark_skeleton` (SKELETON) or unchanged (IGNORE). SRC-1 `pageindex/flash/embedded_toc.py`, `pageindex/flash/main.py`. This record owns the scoped part; the container retains its identity.
- **Owner.** Program code; no model.
- **Effects.** Context: none. State: rewrites the in-memory tree that becomes RT-OBJ-1. Action: none.
- **Implementation conclusion status:** `wired`. **Operation conclusion status:** `uninspected`.
- **Immediate return.** `(structure, source)` with source `bookmarks`, `hybrid` or `detected`.
- **Later read-back.** The merged tree is read by every chat run, as in RT-RTE-1.
- **Delegated visibility.** Not applicable.
- **Selection predicate.** Tier by depth, density, generic-title share and enumeration templates.
- **Invalidation or expiry.** None.
- **Activation or effect.** Not established: no bookmark PDF was processed.
- **Evidence limits.** The module docstring calls the feature opt-in, but the defaults enable it.

#### EPI-RTE-2 — Model summary and description generation
- **Endpoints and progression.** `SummaryScheduler` (`_leaf_summary`, `_parent_summary`) and `generate_doc_description` → stored fields. SRC-1 `pageindex/utils.py`, `pageindex/local_api.py`. Distinct grouping: summary and description generation occurs within RT-RTE-1 and RT-RTE-3. No single parent contains this record across both paths.
- **Owner.** Program code sequences; the index model (RT-CMP-1) writes the text.
- **Effects.** Context: per-call prompt only. State: `summary` and `description` fields. Action: provider calls.
- **Implementation conclusion status:** `wired`. **Operation conclusion status:** `uninspected`.
- **Immediate return.** Text into the tree; an empty string on failure.
- **Later read-back.** Read by every chat run through `get_document_structure` and `browse_documents`; this is the persisted product of indexing, not accumulation through use.
- **Delegated visibility.** Not applicable.
- **Selection predicate.** Leaves under 200 tokens reuse raw text; others get a model summary capped at 150 words by request.
- **Invalidation or expiry.** None.
- **Activation or effect.** Not established.
- **Evidence limits.** No check of the output exists (EPI-ABS-1).

#### EPI-RTE-3 — Citation tag parsing and resolution
- **Endpoints and progression.** `get_citations` → `_parse_citations` (both tag formats, deduplicated) → document name to id lookup → entry; `resolve_citations` rewrites tags as numbered links. SRC-1 `pageindex/client.py`. Possible duplicate: none; the runtime report did not trace it.
- **Owner.** Program code.
- **Effects.** Context: none. State: none. Action: reads the local store, or `get_block` on cloud.
- **Implementation conclusion status:** `wired`. **Operation conclusion status:** `uninspected`.
- **Immediate return.** Entries and rewritten answer.
- **Later read-back.** None.
- **Delegated visibility.** Not applicable.
- **Selection predicate.** Any well-formed tag with a document name and positive page.
- **Invalidation or expiry.** Not applicable.
- **Activation or effect.** Not established.
- **Evidence limits.** A name shared by two documents raises unless `doc_id` disambiguates; no page-range or content check exists.

### Claims

none declared in this member

### Evidenced absences

#### EPI-ABS-1 — No check of model-written summaries or descriptions
- **Searched boundary.** SRC-1 `pageindex/utils.py`, `pageindex/tree_optimize.py`, `pageindex/local_api.py`, `pageindex/flash/api.py`, `pageindex/page_index_classic.py`, `pageindex/local_store.py` at the frozen commit. Query: any code that compares a generated summary or description with its source text, or that rejects or regenerates one on its content. Result: the only tests on a summary are emptiness and JSON shape (`parse_summary`, the all-empty failure in `generate_summaries_for_structure`); `local_api.py` reads summaries only when formatting a tree.
- **Conclusion status:** `absent`.
- **Conclusion supported.** No route in the searched files checks summary or description fidelity. **Conclusion prevented.** Nothing about cloud-side indexing, or about whether the summaries are in fact faithful.

#### EPI-ABS-2 — No check or acceptance of answers or citations
- **Searched boundary.** SRC-1 `pageindex/local_chat.py`, `pageindex/chat_stream.py`, `pageindex/client.py`, `pageindex/agent_tools.py`, `pageindex/integrations/`. Query: any consumer of the final answer or of citation tags other than returning it and `get_citations`/`resolve_citations`; any comparison of a citation's page to page count or to page content. Result: the final output is placed in the return envelope, and citation entries are built from tag text and a name lookup. Distinct absence: RT-ABS-1 concerns store write-back; this record concerns verification of answers with its own searched boundary.
- **Conclusion status:** `absent`.
- **Conclusion supported.** Within the searched files, an answer reaches the caller unchecked, and no acceptance decision exists for it. **Conclusion prevented.** Caller-side or host-side checks, cloud citation behavior, and whether answers are correct.

### Behavioral-authority paths

#### EPI-BAP-1 — Index-construction verdicts govern the stored tree
- **Consumer.** The indexer program (RT-RTE-1, RT-RTE-3). **Channel.** Tier values, kept-or-dropped candidates, expand-or-collapse decisions and accuracy thresholds. **Force.** Enforcing on tree shape and on mode fallback; the chat model later sees only the resulting outline. **Horizon.** One document, persisted in `tree.json`. Anything the checks reject leaves no stored trace, and entries left incorrect after repair are logged, not stored. Conclusion status: `wired`.
- The bounded loop that lets judged-incorrect entries remain is quoted at EPI-OBJ-5.
