---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Quicky Wiki's claim admission, confidence, review and downstream reliance routes at its frozen revision."
run-id: AAS-2026-10-15-quicky-wiki-628f7d7cc628-01
reviewed-boundary: cfeecbffce5b6d0f16533b258a1e88edd86f731e
---

# Quicky Wiki epistemic report

## Source-and-claim boundary

The question is how document-derived claims gain reliance, survive criticism and affect later answers. Scope and external exclusions: see [boundary](boundary.md#boundary-and-evidence); evidence identities and layers: see its [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not observed operation or causal experiments. The inspected mechanisms establish automatic graph admission and evidence-like delivery, not calibrated belief or demonstrated knowledge improvement.

The runtime is provisional. Direct reads confirmed the compiler, question answering and consensus account and extended it with chunk-prefix filtering, lint/prune and the model-generated slide path. No supplied runtime fact requires supersession; the runtime's renderer coverage is not a complete epistemic account of slide generation. This member adds that material route. Source-tree searches for hooks/registration in `src/` and `package.json` found no additional hook surface; CLI dispatch, library exports, MCP tool names/handlers and dashboard API branches were checked rather than inferred from that search miss.

| Entry point or operation | Source path (SRC-1) | Coverage and records |
|---|---|---|
| CLI dispatch and library operations | `src/cli.ts`, `src/lib.ts` | Direct complete reads; [RT-RTE-client-access](runtime.md#rt-rte-client-access), [RT-RTE-runtime-setup](runtime.md#rt-rte-runtime-setup). Library exports permit direct store/compiler use. |
| File, URL, directory, watcher and bookmark ingestion | `src/compiler/ingest.ts`, `src/cli/fetch-url.ts`, `src/cli/ingest.ts`, `src/cli/watch.ts`, `src/cli/serve.ts` | Compiler/URL conversion and bookmark branch directly read; driver variants supplied by [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). |
| Comparison, score calculation, resolution, summaries | `src/compiler/diff.ts`, `src/compiler/confidence.ts`, `src/compiler/resolve.ts` | Direct complete reads; [RT-OBJ-knowledge-diff](runtime.md#rt-obj-knowledge-diff), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [EPI-OBJ-page-summaries](#epi-obj-page-summaries). |
| Ordinary query, consensus and save/reingest | `src/graph/query.ts`, `src/compiler/consensus.ts`, `src/cli/save-answer.ts` | Direct complete reads; [RT-RTE-question-answer](runtime.md#rt-rte-question-answer), [RT-RTE-consensus-answer](runtime.md#rt-rte-consensus-answer), [RT-RTE-answer-save](runtime.md#rt-rte-answer-save). |
| MCP read, ingest and metadata tools; dashboard query, edit and deletion | `src/mcp/server.ts`, `src/cli/serve.ts` | Tool/branch inventory searched; MCP ingest/metadata and dashboard mutation branches directly read; other dispatcher details supplied by [RT-RTE-client-access](runtime.md#rt-rte-client-access). Page DELETE is shadowed, unlike claim DELETE. |
| Store confidence, challenge, relations, search and removal | `src/graph/store.ts` | Direct method reads; broader schema/write context supplied by [RT-OBJ-knowledge-store](runtime.md#rt-obj-knowledge-store). |
| Decay, dependency cascade, structural checks | `src/graph/temporal.ts`, `src/graph/cascade.ts`, `src/cli/lint.ts` | Direct complete reads; [RT-RTE-health-review](runtime.md#rt-rte-health-review), [EPI-RTE-lint-prune](#epi-rte-lint-prune). |
| Health, criticism, resurfacing and discovery | `src/metabolism/health.ts`, `src/metabolism/redteam.ts`, `src/metabolism/resurface.ts`, `src/cli/metabolism.ts`, `src/discovery/discover.ts` | Direct complete reads; [RT-RTE-health-review](runtime.md#rt-rte-health-review). Suggestions stop at returned/displayed proposals in these callers. |
| Compile/export and persisted views | `src/cli/compile.ts`, `src/render/markdown.ts`, `src/render/anki.ts`, `src/render/marp.ts`, `src/render/obsidian.ts` | Compile, Markdown, Anki and slides directly read completely; Obsidian write flow and source/index content directly read, remaining page template uninspected. [EPI-RTE-slide-output](#epi-rte-slide-output). Graph/timeline and remaining Obsidian templates rely on runtime coverage, not an exhaustive semantic audit. |
| Setup/model/release machinery | `src/llm/adapter.ts`, `src/cli/context.ts`, `.github/workflows/publish.yml` | Supplied [RT-CMP-llm-adapter](runtime.md#rt-cmp-llm-adapter), [RT-RTE-runtime-setup](runtime.md#rt-rte-runtime-setup), [RT-RTE-package-release](runtime.md#rt-rte-package-release). No graph-driven parameter training or package installation established. |

Missing evidence is local to the conclusions it prevents: no source corpus or model input/output pairs means extraction, summary, answer and critique propositions cannot be individuated or classified semantically beyond their implemented request; no run trace means activation, actual acceptance decisions and acted-on criticism are unobserved; no reference-answer/calibration study means scores and consensus accuracy are unevaluated; no intervention/comparison means benefit, causal component effects and successful improvement are unestablished. External model internals and weight identity remain uninspected. The remaining view templates prevent a system-complete negative about every export's semantics; they do not negate the positively traced routes.

Consequential claims: [EPI-CLM-living-knowledge](#epi-clm-living-knowledge) and [RT-CLM-confidence-citations](runtime.md#rt-clm-confidence-citations).

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-source-content](#epi-obj-source-content) | Document assertions, scope determined by each document | Evidence input | SRC-1 `src/compiler/ingest.ts` | No corpus supplied; truth and original warrant unknown. |
| [EPI-OBJ-claim-statements](#epi-obj-claim-statements) | Extracted and retained factual statements | Atomic, verifiable claims | SRC-1 `src/compiler/ingest.ts` | Prompt does not prove fidelity, atomicity or truth. |
| [EPI-OBJ-confidence-state](#epi-obj-confidence-state) | None as policy state; interpreted as degree of support by consumers | Confidence, provenance, dependencies, events | SRC-1 `src/compiler/confidence.ts` | Numerical derivation is not a calibrated probability or evidential independence test. |
| [EPI-OBJ-page-summaries](#epi-obj-page-summaries) | One-sentence model summaries, potentially asserting facts | Page description and retrieval surface | SRC-1 `src/compiler/resolve.ts` | Preservation/entailment not checked. |
| [RT-OBJ-knowledge-diff](runtime.md#rt-obj-knowledge-diff) | Challenge reasons and gap diagnoses; symbolic action arrays separate from their prose | Comparison result | SRC-1 `src/compiler/diff.ts` | Evaluates semantic relation, not source truth. |
| [EPI-OBJ-query-results](#epi-obj-query-results) | Answer and caveats | Returned answer, optional saved source | SRC-1 `src/graph/query.ts` | Returned IDs and confidence unvalidated. |
| [EPI-OBJ-consensus-result](#epi-obj-consensus-result) | Response statements and synthesis | Consensus categories for CLI | SRC-1 `src/compiler/consensus.ts` | Agreement labels have single-response/failure alternatives. |
| [EPI-OBJ-review-proposals](#epi-obj-review-proposals) | Claim critiques | Advisory red-team output | SRC-1 `src/metabolism/redteam.ts` | No original source evidence or wired acceptance. |
| [EPI-OBJ-resurface-reviews](#epi-obj-resurface-reviews) | Review questions and suggestions; questions need not assert a proposition | Advisory stale/weak review | SRC-1 `src/metabolism/resurface.ts` | No verified diagnosis or revision decision. |
| [EPI-OBJ-discovery-proposals](#epi-obj-discovery-proposals) | Gap, frontier, connection and contradiction diagnoses | Advisory discovery | SRC-1 `src/discovery/discover.ts` | Model-generated relationships and IDs unverified. |
| [EPI-OBJ-slide-content](#epi-obj-slide-content) | Presentation assertions and summary | Persisted slide deck | SRC-1 `src/render/marp.ts` | No post-generation semantic check. |
| [RT-CMP-llm-adapter](runtime.md#rt-cmp-llm-adapter) | Not determinable within opaque parametric state | External generation/evaluation machinery | SRC-1 `src/llm/adapter.ts` | See component for inference-only calls, unpinned weights and mutable endpoints; no claim about inaccessible internal learning. |

## Authority-route ledger

Fields owned by a declaring record are available through the citation; ledger fields below are this member's epistemic assessment. Each repeated route citation selects a different consequential function of its container, not a duplicate declaration. All implemented rows describe wiring, not observed execution.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | content transformation | implemented | [EPI-OBJ-source-content](#epi-obj-source-content) | truth-apt transformation: acquisition/import | File body/converted URL enters extraction | File reader, frontmatter parser and URL conversion; byte/text domain | On ingest; hash match skips extraction | Source body delivered; URL origin metadata retained | Permissive input delivery | Imported warrant unknown; metadata is not authentication | Allows extraction from supplied source | Extractor, user-message body, advisory evidence, current call | SRC-1 `src/compiler/ingest.ts`, `src/cli/fetch-url.ts` | [EPI-CLM-living-knowledge](#epi-clm-living-knowledge) | none | HTML stripping can discard context; source is not an oracle. |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | content transformation | implemented | [EPI-OBJ-claim-statements](#epi-obj-claim-statements) | truth-apt transformation: indeterminate | Source prose to extracted statements | Chat model instructed to extract factual claims | New/changed bytes; chunking above threshold | Parsed candidates, or empty array on parsing failure | Candidate generation | No demonstrated non-ampliative preservation, entailment or acceptance | Candidates proceed to comparison | Comparator, extracted arrays, permissive, current ingest | SRC-1 `src/compiler/ingest.ts` | [EPI-CLM-living-knowledge](#epi-clm-living-knowledge) | none | Need concrete source/output pairs to choose reshaping, derivation or conjecture. |
| [EPI-RTE-chunk-selection](#epi-rte-chunk-selection) | operational admission/selection/consumption | implemented | [EPI-OBJ-claim-statements](#epi-obj-claim-statements) | no content change | Selection of extracted candidates | First occurrence of normalized 80-character prefix | Only chunked extraction; before diff | Later prefix duplicates removed | Enforcing inclusion filter | No equivalence license | Blocks some candidates from graph comparison | Diff, filtered array, enforcing, current ingest | SRC-1 `src/compiler/ingest.ts` | none | Prefix equality is not proposition equality | Distinct negated suffix can be lost; see concrete deduction. |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | check/evidence production | implemented | [RT-OBJ-knowledge-diff](runtime.md#rt-obj-knowledge-diff) | no content change | New/existing semantic relationship | Model compares statement lists; index handling checks addressability | Existing-store comparison | Reinforce/challenge/new/gap classifications | Supplies resolver inputs | Model judgment about relation only | Proposes graph changes | Resolver, diff arrays, permissive semantic decisions, current ingest | SRC-1 `src/compiler/diff.ts` | [EPI-CLM-living-knowledge](#epi-clm-living-knowledge) | none | No source bodies, independent oracle or coverage check; omitted matches can omit candidates. |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | disposition/acceptance | implemented | [EPI-OBJ-confidence-state](#epi-obj-confidence-state) | non-truth-apt policy/content update: assign confidence and action | Admit new claims, reinforce or weaken old ones | Code consumes valid indices/actions; quality scaling and fixed formulas | Empty store admits all; parse failure in diff admits all as new | Stored claim or score/event update | Enforcing store mutations | Operational admission, not evidence-consuming acceptance for a named factual use/scope | Allows future use without per-claim approval; challenge does not remove claim | Store writers then readers, rows/scores, enforcing update and advisory later evidence, cross-command | SRC-1 `src/compiler/diff.ts`, `src/compiler/resolve.ts`, `src/compiler/confidence.ts` | [EPI-CLM-living-knowledge](#epi-clm-living-knowledge) | Scores do not certify truth | Reinforcement can lower confidence; source count is not independence. |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | retention | implemented | [EPI-OBJ-claim-statements](#epi-obj-claim-statements), [EPI-OBJ-confidence-state](#epi-obj-confidence-state) | no content change | Diff to durable graph, source links and events | Store transactions per method | During resolution | Statements/provenance/scores available later | Enforcing retention | Lineage links, not endorsement | Enables later query/comparison/review | Readers, SQLite rows, permissive persistence, cross-command | SRC-1 `src/graph/store.ts`, `src/compiler/resolve.ts` | none | none | No whole-ingest transaction or immutable raw snapshot. |
| [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) | content transformation | implemented | [EPI-OBJ-page-summaries](#epi-obj-page-summaries) | truth-apt transformation: indeterminate | Claims to page summary and page assignment | Model; summary nonempty and length greater than five | Touched or summary-less pages | Stored summary; failures skipped | Permissive write | No factual-summary acceptance | Summary affects page search and views; assignment determines grouping | Search/readers, summary/title text, ranking or advisory, cross-command | SRC-1 `src/compiler/resolve.ts`, `src/graph/query.ts` | none | none | A length check licenses storage, not semantic fidelity; co-citation links are not entailment. |
| [RT-RTE-question-answer](runtime.md#rt-rte-question-answer) | operational admission/selection/consumption | implemented | [EPI-OBJ-claim-statements](#epi-obj-claim-statements) | no content change | Graph to answer context | Lexical prefix-OR search and page fallback | Every ordinary query | Selected statement/confidence lines | Enforcing context selection; advisory evidence | No renewed factual warrant | Excludes unselected claims; supplies selected claims without a factual veto | Answer model, text context, advisory, current call; retained graph crosses calls | SRC-1 `src/graph/query.ts`, `src/graph/store.ts` | [RT-CLM-confidence-citations](runtime.md#rt-clm-confidence-citations) | IDs and original evidence omitted | No confidence minimum gates ordinary retrieval. |
| [RT-RTE-question-answer](runtime.md#rt-rte-question-answer) | content transformation | implemented | [EPI-OBJ-query-results](#epi-obj-query-results) | truth-apt transformation: indeterminate | Selected claims/question to answer | Chat model; permissive JSON parsing | After retrieval | Answer/confidence/IDs or raw-text fallback | Advisory result | No checked entailment, citation correctness or calibrated confidence | Returned to user/client; optionally saved | CLI/dashboard/MCP, result text, advisory, request horizon | SRC-1 `src/graph/query.ts` | [RT-CLM-confidence-citations](runtime.md#rt-clm-confidence-citations) | Requested citations not verified | Concrete answer content not supplied. |
| [RT-RTE-consensus-answer](runtime.md#rt-rte-consensus-answer) | check/evidence production | implemented | [EPI-OBJ-consensus-result](#epi-obj-consensus-result) | truth-apt transformation: indeterminate | Responders' claims and convergence | Primary model comparing successful parsed answers; model-response domain | Two or more successful responses | Agreed/disputed/uncertain arrays and synthesis | Advisory comparison | At most requested agreement judgment, not independent source truth | Changes displayed categorization, not graph | CLI, consensus result, advisory, current request | SRC-1 `src/compiler/consensus.ts` | none | Single-response and failed-comparison paths also label claims agreed | Shared evidence/errors and independence untested; no reference-answer oracle. |
| [RT-RTE-answer-save](runtime.md#rt-rte-answer-save) | retention | implemented | [EPI-OBJ-query-results](#epi-obj-query-results) | truth-apt transformation: non-ampliative reshaping | Answer to generated raw source | User save flag and fixed serializer | Standard query only | Markdown answer with metadata and resolvable cited statements | Permissive retention | Explicit generated origin, not independent corroboration | Permits later re-extraction/manual or watched ingestion | Extractor, raw file, advisory source then automatic admission, cross-command | SRC-1 `src/cli/save-answer.ts` | none | Compounding can recycle prior output | Saving is not factual approval; cited count can include unresolved IDs. |
| [RT-RTE-health-review](runtime.md#rt-rte-health-review) | check/evidence production | implemented | [EPI-OBJ-review-proposals](#epi-obj-review-proposals) | truth-apt transformation: indeterminate | Weakness of high-confidence claims | Model sees up to five strongest claims at least 0.7 and source counts, not original evidence | Requested red-team maintenance | Critiques and suggested adjustments | Advisory only | Candidate criticism; not validated criticism or accepted revision | Caller displays; no automatic score adjustment | Human, report text, advisory, current invocation | SRC-1 `src/metabolism/redteam.ts`, `src/cli/metabolism.ts` | [EPI-CLM-living-knowledge](#epi-clm-living-knowledge) | Review is not challenge application | No observed human action or retained critique loop. |
| [RT-RTE-health-review](runtime.md#rt-rte-health-review) | content transformation | implemented | [EPI-OBJ-resurface-reviews](#epi-obj-resurface-reviews) | truth-apt transformation: indeterminate | Review needs of stale/weak claims | Model receives up to five deduplicated claims, weakest first, selected by age over 14 days or confidence at most 0.5 | Requested resurfacing | Questions/suggestions or fixed fallback | Advisory only | No factual revision license | Displays prompts to verify or update externally | Human, console questions, advisory, current invocation | SRC-1 `src/metabolism/resurface.ts`, `src/cli/metabolism.ts` | none | none | Questions can be non-truth-apt; truth-apt content of actual outputs not supplied. |
| [RT-RTE-health-review](runtime.md#rt-rte-health-review) | check/evidence production | implemented | [EPI-OBJ-discovery-proposals](#epi-obj-discovery-proposals) | truth-apt transformation: indeterminate | Coverage gaps, frontiers, bridges or conflicting statements | Model receives page-grouped statements and mode instruction | Requested discovery | Descriptions, suggested queries, priority, mapped claim IDs | Advisory only | Candidate diagnosis, not accepted relation or factual finding | Returns proposals for display; does not insert contradiction edges | Human, discovery result, advisory, current invocation | SRC-1 `src/discovery/discover.ts` | [EPI-CLM-living-knowledge](#epi-clm-living-knowledge) | Claim indices requested but not explicitly numbered in input | No independent evidence or verified ID mapping. |
| [RT-RTE-health-review](runtime.md#rt-rte-health-review) | operational admission/selection/consumption | implemented | [EPI-OBJ-confidence-state](#epi-obj-confidence-state) | non-truth-apt policy/content update: time decay and damped dependency score propagation | Existing confidence and age/dependency relations | Fixed exponential decay/clamp or damped traversal; numeric policy domain | Decay request or challenge resolution | New scores; dependent traversal only with edges | Enforcing update | No new evidence about statement truth | Changes displayed strength and confidence-selected exports/reviews; claims remain queryable | Store then models/views, confidence numbers, ranking/advisory, cross-command | SRC-1 `src/graph/temporal.ts`, `src/graph/cascade.ts`, `src/graph/store.ts` | [EPI-CLM-living-knowledge](#epi-clm-living-knowledge) | Dependency extraction not wired to edge insertion | Generic confidence update resets last-reinforced, including decay/cascade. |
| [EPI-RTE-lint-prune](#epi-rte-lint-prune) | check/evidence production | implemented | [EPI-OBJ-confidence-state](#epi-obj-confidence-state) | no content change | Empty pages, missing source links, low scores, self-dependency and contradiction records | Deterministic predicates over graph structure/values | User lint request | Error/warning report | Advisory diagnostic | Supports only enumerated structural predicates | Does not veto queries or fix claims | Human, console, advisory, request horizon | SRC-1 `src/cli/lint.ts` | none | Self-loop test is not general cycle detection | No factual truth check; counts depend on populated edges. |
| [EPI-RTE-lint-prune](#epi-rte-lint-prune) | disposition/acceptance | implemented | [RT-OBJ-knowledge-store](runtime.md#rt-obj-knowledge-store) | no content change | Empty-page removal | Caller prune request and zero-claim SQL condition | CLI lint prune or dashboard prune | Empty pages and their links removed | Enforcing deletion | No factual claim rejected | Removes navigation objects, not low-confidence claims | Store/readers, deleted rows, enforcing, subsequent reads | SRC-1 `src/cli/lint.ts`, `src/graph/store.ts` | none | none | Generated files not swept by this operation. |
| [RT-RTE-client-access](runtime.md#rt-rte-client-access) | disposition/acceptance | implemented | [EPI-OBJ-claim-statements](#epi-obj-claim-statements) | truth-apt transformation: acquisition/import | Direct statement replacement | Caller text; dashboard string check; store update | Reachable claim PATCH or library call | Replacement statement | Enforcing mutation | Imported warrant unknown, no factual acceptance criterion | New content available under existing claim identity/source links | Store/readers, statement row, enforcing mutation then advisory context, cross-command | SRC-1 `src/cli/serve.ts`, `src/graph/store.ts` | none | Old provenance can remain attached to changed content | Caller identity does not establish human approval; old rendered content can persist. |
| [RT-RTE-client-access](runtime.md#rt-rte-client-access) | disposition/acceptance | implemented | [EPI-OBJ-confidence-state](#epi-obj-confidence-state) | non-truth-apt policy/content update: caller score or metadata assignment | Confidence assignment and page metadata merge | Dashboard number check or caller metadata object; store methods | Claim PATCH, MCP metadata tool or library call | New confidence or metadata | Enforcing mutation | No measurement or factual license from assignment alone | Changes confidence-guided use or metadata-filtered selection | Store/readers, numeric/JSON rows, enforcing update then ranking/selection, cross-command | SRC-1 `src/cli/serve.ts`, `src/mcp/server.ts`, `src/graph/store.ts` | none | none | Metadata may itself assert facts, but no supplied object individuates them; their truth-apt status is not determinable. |
| [RT-RTE-client-access](runtime.md#rt-rte-client-access) | disposition/acceptance | implemented | [EPI-OBJ-claim-statements](#epi-obj-claim-statements), [EPI-OBJ-confidence-state](#epi-obj-confidence-state) | no content change | Claim withdrawal or direct library page removal | Caller deletion request and store transaction | Reachable claim DELETE; public library deletePage | Removed claim and related rows/events | Enforcing deletion | Caller disposition, not falsification | Deleted claims unavailable to live graph consumers | Store/readers, deleted rows, enforcing, later reads | SRC-1 `src/cli/serve.ts`, `src/graph/store.ts` | none | Dashboard page DELETE shadowed | No retained tombstone/criticism or automatic withdrawal of exported artifacts. |
| [EPI-RTE-slide-output](#epi-rte-slide-output) | content transformation | implemented | [EPI-OBJ-slide-content](#epi-obj-slide-content) | truth-apt transformation: indeterminate | Selected graph claims to slide deck | Model prompted to group/summarize, not an independent checker | Compile slides; default score threshold, topic override | Model text written to slide file | Advisory output with permissive persistence | No checked semantic preservation or acceptance | Presentation artifact available to humans | Renderer/file consumer, Markdown, advisory, persisted file horizon | SRC-1 `src/render/marp.ts`, `src/cli/compile.ts` | none | none | Topic selection bypasses default confidence floor; no factual gate before writing. |

No lifecycle-integration row is asserted: page assignment, links and summaries organize content after operational admission, but no evidence-consuming acceptance decision for factual reliance was established in the inspected paths. The absence of that decision is not an invented evaluator failure. Source-hash recovery and configuration control remain as described in [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-RTE-runtime-setup](runtime.md#rt-rte-runtime-setup): hashes license skipping, not endorsement; configured entity instructions affect extraction policy, not evidence-responsive policy learning.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-living-knowledge](#epi-clm-living-knowledge) | Living confidence-scored knowledge, contradiction surfacing, claim provenance/dependency and cascade | SRC-1 `README.md`; doctrine/design | See claim | [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-health-review](runtime.md#rt-rte-health-review), [EPI-RTE-chunk-selection](#epi-rte-chunk-selection) | None supplied | None; source quality labels and scores do not measure correctness | Claims and scores are automatically maintained; semantic conflict detection is requested and score challenge is applied | Dependency/contradiction edges are not inserted by ordinary compiler; challenge event does not itself populate contradictedBy. Red-team only advises. Automatic comprehensive surfacing and calibrated uncertainty not established. |
| [RT-CLM-confidence-citations](runtime.md#rt-clm-confidence-citations) | Confidence-aware cited answers | SRC-1 `src/mcp/server.ts`; doctrine/design | See claim | [RT-RTE-question-answer](runtime.md#rt-rte-question-answer), [RT-RTE-consensus-answer](runtime.md#rt-rte-consensus-answer) | None supplied | None; model IDs are unvalidated and source evidence omitted | Structured answer/confidence feature is implemented | Ordinary context lacks claim IDs; MCP reduces returned IDs to count; consensus agreement has non-consensus fallback paths. |

## Bounded conclusion

Quicky Wiki imports source text of unknown warrant, requests extraction and semantic comparison, and automatically admits their parseable results to a durable graph. Provenance links identify source records, but neither those links nor quality multipliers constitute factual acceptance. Extraction, summaries, answers, reviews and slides remain semantically indeterminate without actual content pairs: the implementation establishes generation requests, not entailed derivation or evidenced non-entailment. No accepted ampliative claim instance is established by this source-only analysis. See [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [EPI-RTE-slide-output](#epi-rte-slide-output).

Scores have real operational authority. They affect review candidate choice, default slides/Anki inclusion and confidence-bearing model context. They do not enforce factual admissibility in ordinary query retrieval. Decay and damped cascade are deterministic policy updates, not new truth evidence. Reinforcement is a weighted blend and can lower a score: for existing 0.9, new evidence 0.4 and one existing source, weight is 1/1.1 and result about 0.445, within the clamp. This implementation deduction refutes a universal reading that reinforcement necessarily strengthens a claim. No premises about the underlying proposition's truth enter that arithmetic (SRC-1 `src/compiler/confidence.ts`; [EPI-OBJ-confidence-state](#epi-obj-confidence-state)).

Graph-to-answer delivery has advisory evidential force through model interpretation, not enforced obedience. Saving an answer and reingesting it closes a retained-output loop, but adds no independent evidence merely by making a new source file. Prefix filtering can also remove a distinct proposition before comparison. These are lineage/reliance qualifications, not observed failure rates. See [RT-BAP-retained-context](runtime.md#rt-bap-retained-context), [RT-RTE-answer-save](runtime.md#rt-rte-answer-save), [EPI-RTE-chunk-selection](#epi-rte-chunk-selection).

Checking and disposition differ. Structural lint and health calculations evaluate graph predicates; model red-team/discovery evaluates possible weaknesses and connections from restricted context. Those reports do not automatically revise retained claims. Ingestion comparison does automatically change confidence and admission; direct edits and deletion are separate caller-controlled operations without an implemented factual criterion. Prune removes empty pages, not false statements. Removal from the live store does not establish withdrawal from already exported artifacts. See [RT-RTE-health-review](runtime.md#rt-rte-health-review), [EPI-RTE-lint-prune](#epi-rte-lint-prune), [RT-RTE-client-access](runtime.md#rt-rte-client-access).

Retained content and confidence can shape later behavior without model-weight updates. Actual learning as improved future capacity is unestablished; no improvement outcomes or attribution evidence were supplied. Content-directed comparison is implemented, but reliable criticism, accepted factual revision and retained criticism iteration are not established by the review route. Autonomous host sequencing exists within ingestion; it does not prove autonomous theory building. Health statistics represent selected graph properties, but a criticism-driven revision of the system's own method is not established. Configurable extraction instructions are a policy input, not evidence of exercised self-improvement. These are separate limits, not a single system-wide verdict; provider-internal processing remains opaque ([RT-CMP-llm-adapter](runtime.md#rt-cmp-llm-adapter), [RT-RTE-runtime-setup](runtime.md#rt-rte-runtime-setup)).

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-source-content
Label: Source document content

Distinct from [RT-OBJ-knowledge-store](runtime.md#rt-obj-knowledge-store): raw document bodies are read from filesystem paths rather than stored as graph row bodies. Source-native identity is `raw`/`content` in ingestion and Markdown returned by `fetchUrlToMarkdown`. Natural-language assertions occur within text and symbolic frontmatter, on the filesystem and transient strings. Source IDs/hashes identify registered inputs, not immutable evidence snapshots. SRC-1 `src/compiler/ingest.ts`, `src/cli/fetch-url.ts`; implementation.

> const raw = await readFile(filePath, "utf-8");
> const contentHash = createHash("sha256").update(raw).digest("hex");
> --- `src/compiler/ingest.ts`

URL conversion strips navigation and other sections and records source URL/time. Unknown original warrant is further bounded by this lossy conversion; it cannot be treated as authenticated or complete source evidence.

> const mainMatch = content.match(
>     /<(?:main|article)[^>]*>([\s\S]*?)<\/(?:main|article)>/i,
>   );
>   if (mainMatch) {
>     content = mainMatch[1];
>   }
> --- `src/cli/fetch-url.ts`

#### EPI-OBJ-claim-statements
Label: Extracted and retained claim statements

Part of: [RT-OBJ-knowledge-store](runtime.md#rt-obj-knowledge-store)

Source-native identity is retained `Claim.statement`, natural-language text in SQLite claims and transient extracted arrays. This part separates content from its numerical and relational controls. Producer is model extraction or direct caller edit; consumers include comparison, answering, summaries, review and exports. Extraction explicitly requests source-supported factual content but does not check source-to-statement entailment (SRC-1 `src/compiler/ingest.ts`, `src/graph/store.ts`; implementation/design).

> const systemPrompt = `You extract atomic, verifiable claims from source material.
> Each claim should be a single factual statement. Be precise and specific.
> Assign an initial confidence based on how well-supported the claim is by the source.
> --- `src/compiler/ingest.ts`

Store persistence/answer delivery passages are supplied by [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-RTE-question-answer](runtime.md#rt-rte-question-answer). Nothing in those passages demonstrates a claim's truth.

#### EPI-OBJ-confidence-state
Label: Claim confidence and relations

Part of: [RT-OBJ-knowledge-store](runtime.md#rt-obj-knowledge-store)

Source-native identities are claim `confidence`, source quality, source links, dependency/contradiction edges and epistemic event rows. Numerical/symbolic controls live in SQLite and intermediate diffs, with natural-language notes. They are separate from the claim statements whose reliance they affect. Score scaling/clamping and weighted blending are implemented, not calibration measurements (SRC-1 `src/compiler/confidence.ts`, `src/graph/store.ts`).

> const multiplier = QUALITY_MULTIPLIERS[qualityTier] ?? 0.45;
>   const adjusted = rawConfidence * multiplier;
>   return Math.max(0.01, Math.min(1.0, adjusted));
> --- `src/compiler/confidence.ts`

> const weight = 1 / (1 + sourceCount * 0.1);
>   const merged = existing * (1 - weight) + newEvidence * weight;
>   return Math.max(0.01, Math.min(1.0, merged));
> --- `src/compiler/confidence.ts`

The comparison classifies challenges separately from source truth. Its fixed reduction keeps the challenged statement live; the challenge store method records an event, not a new contradiction edge. The complete diff/resolver reads confirm runtime's missing dependency-insertion finding; public store edge methods remain a countercase to any claim that relations cannot exist ([RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); SRC-1 `src/compiler/diff.ts`, `src/compiler/resolve.ts`, `src/graph/store.ts`).

> confidenceAfter: Math.max(0.01, existing.confidence * 0.6),
> --- `src/compiler/diff.ts`

> "UPDATE claims SET confidence = ?, last_reinforced = ? WHERE id = ?",
> --- `src/graph/store.ts:552-558`

The latter generic updater resets age even for decay/cascade changes. Confidence is therefore not a pure timestamp-independent evidence measure. Default export/review predicates give it operational consequences, while ordinary question search does not impose a confidence floor.

#### EPI-OBJ-page-summaries
Label: Page summary text

Part of: [RT-OBJ-knowledge-store](runtime.md#rt-obj-knowledge-store)

Source-native identity is page `summary`, natural-language text retained in SQLite, used by search and views. It differs from claim statements in its producer/check: a summary model receives page claims and scores, then code checks only minimal nonempty length before writing. Semantic fidelity is indeterminate without inputs/outputs (SRC-1 `src/compiler/resolve.ts`, `src/graph/query.ts`; implementation).

> const summary = resp.content.trim().replace(/^["']|["']$/g, "");
>         if (summary && summary.length > 5) {
>           store.updatePageSummary(pageId, summary);
>         }
> --- `src/compiler/resolve.ts`

#### EPI-OBJ-query-results
Label: Ordinary answer result

Part of: [RT-RTE-question-answer](runtime.md#rt-rte-question-answer)

This object is the return value of the parent route, not another declaration of that process. Source-native fields are `answer`, `claimIds` and `confidence`: natural-language answer/caveats, symbolic IDs and numeric score in a transient object. CLI/dashboard/MCP consume it; optional saving serializes it for later extraction. Parsing/fallback is not factual acceptance. SRC-1 `src/graph/query.ts`; implementation.

> return {
>       answer: response.content,
>       claimIds: [],
>       confidence: 0.5,
>     };
> --- `src/graph/query.ts`

#### EPI-OBJ-consensus-result
Label: Consensus result

Part of: [RT-RTE-consensus-answer](runtime.md#rt-rte-consensus-answer)

The object is the parent route's return value: `ConsensusResult`, a transient symbolic category structure carrying natural-language claims/synthesis and numeric confidence. Model comparison or shortcuts produce it; CLI consumes it, not graph ingestion. SRC-1 `src/compiler/consensus.ts`; implementation.

> agreed: modelResponses[0].claims.map((c) => ({
>         statement: c.statement,
>         confidence: c.confidence,
>       })),
> --- `src/compiler/consensus.ts`

This fallback countercase means agreed is not sufficient evidence that multiple responders converged. The single-response shortcut independently has the same limitation.

#### EPI-OBJ-review-proposals
Label: Red-team critiques

Part of: [RT-RTE-health-review](runtime.md#rt-rte-health-review)

This object is a returned output part of the parent route, not its score mutations. `redteamClaims` returns a transient array of natural-language critique with symbolic claim ID and numeric suggested adjustment, based on strongest selected claims and source counts. The CLI/human consumes it; no caller acceptance or persistence is wired. SRC-1 `src/metabolism/redteam.ts`, `src/cli/metabolism.ts`; implementation. The supplied parent route supplies return-only evidence. Red-team proposals name claim indices but do not consume original sources; adjustments are only printed.

> console.log(
>             chalk.dim(
>               `    Suggested adjustment: ${c.suggestedConfidenceAdjustment > 0 ? "+" : ""}${(c.suggestedConfidenceAdjustment * 100).toFixed(0)}%`,
>             ),
>           );
> --- `src/cli/metabolism.ts`

#### EPI-OBJ-resurface-reviews
Label: Resurfacing review prompts

Part of: [RT-RTE-health-review](runtime.md#rt-rte-health-review)

Source-native identity is `resurface` returned reviews: natural-language question/suggestion plus symbolic reference to the selected claim, in a transient array. This is the parent route's review output part. A model generates it from stale/weak statements, with fixed fallback questions on parsing failure; the CLI displays it to a human, without acceptance or persistence. Unlike red-team, the target is a review action rather than a strongest-claim critique. SRC-1 `src/metabolism/resurface.ts`; implementation/design.

> question: `Is this still accurate: "${c.statement}"?`,
>       suggestion: "Review and reinforce or remove this claim.",
> --- `src/metabolism/resurface.ts`

#### EPI-OBJ-discovery-proposals
Label: Discovery proposals

Part of: [RT-RTE-health-review](runtime.md#rt-rte-health-review)

Source-native identity is `Discovery[]`: natural-language description/title/suggested queries plus symbolic priority, mode and related claim IDs, in a transient array returned for display. This is the parent route's discovery output part. The model receives page-grouped claims and a selected mode instruction. It does not receive explicitly numbered claims although it is asked for claim indices; code maps those indices onto the independent claims array, without verifying semantic correspondence. No contradiction-edge insertion or acceptance follows. SRC-1 `src/discovery/discover.ts`; implementation/design.

> relatedClaims: (d.relatedClaimIndices ?? [])
>         .map((i: number) => claims[i]?.id)
>         .filter(Boolean),
> --- `src/discovery/discover.ts`

#### EPI-OBJ-slide-content
Label: Slide deck content

Source-native identity is `renderSlides` response text and `_slides.md`. Natural-language claims/summary plus symbolic Marp formatting live in a transient string and then a filesystem artifact. Distinct from [RT-OBJ-knowledge-store](runtime.md#rt-obj-knowledge-store) and the supplied answer route: a presentation caller generates it and writes a file, rather than returning an ordinary question answer or storing graph claims. SRC-1 `src/render/marp.ts`, `src/cli/compile.ts`; implementation. Evidence passages are in [EPI-RTE-slide-output](#epi-rte-slide-output).

### Routes

#### EPI-RTE-chunk-selection
Label: Chunk prefix selection

Part of: [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

The ingestion code owns a deterministic filter between sequential chunk extraction and diff consumption. This part is distinct from model semantic comparison: lowercased alphanumeric prefix equality determines candidate retention (SRC-1 `src/compiler/ingest.ts`; implementation).

- Immediate return: First candidate for each normalized prefix, as an extracted array.
- Later read-back: inapplicable — filter has no retained state; surviving claims can persist through the parent ingestion route.
- Delegated visibility: Comparator receives survivors, not removed candidates or duplicate reasons.
- Selection predicate: Chunked extraction when body length exceeds 12000; normalized statement prefix of 80 characters; first occurrence wins.
- Invalidation or expiry: Seen set is fresh for each chunked extraction.
- Activation or effect: Candidate omission is wired before diff; actual omissions unobserved.
- Evidence limits: Static text deduction establishes non-equivalence risk, not frequency in a real corpus.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Code decides; neither model nor human vetoes individual filter decisions. No answer oracle; mode is open ingestion. Guidance is a fixed deduplication heuristic; it persists as code, not revised learned policy. No rollback within the filter.

> const key = c.statement
>       .toLowerCase()
>       .replace(/[^a-z0-9]/g, "")
>       .slice(0, 80);
>     if (seen.has(key)) return false;
>     seen.add(key);
>     return true;
> --- `src/compiler/ingest.ts`

Concrete implementation deduction, without target execution: let the shared prefix be the concatenation of four copies of `The recorded system configuration `, followed by `is enabled.` for statement A and `is not enabled.` for B. Together the repeated clauses normalize to more than 80 letters, so the first 80 normalized characters are identical and occur before either differing suffix. If A precedes B, the filter retains A and drops B. The opposite factual polarity is never compared by the diff. This is candidate selection, not a checked non-ampliative semantic deduplication.

#### EPI-RTE-lint-prune
Label: Structural lint and empty-page prune

Part of: [RT-RTE-health-review](runtime.md#rt-rte-health-review)

CLI code reads pages/claims/sources and emits structural warnings; optional pruning delegates to store deletion. This part separates graph predicates and deletion from model review (SRC-1 `src/cli/lint.ts`, `src/graph/store.ts`; implementation).

- Immediate return: Console issues/counts; optional deleted-empty-page count.
- Later read-back: Pruned page/link rows are absent from subsequent store reads; warnings themselves are not persisted by the caller.
- Delegated visibility: Human sees errors/warnings; store receives prune request, not a factual diagnosis.
- Selection predicate: No claims, no source links, confidence below 0.1, self-ID dependency, or stored contradiction relations; prune selects pages with zero claims.
- Invalidation or expiry: Recomputed per call; independent store writes can change results; generated files are not deleted here.
- Activation or effect: Reporting is advisory; prune deletes navigation rows on explicit request. Operation unobserved.
- Evidence limits: Self-dependency check does not establish general graph acyclicity; missing edges cannot establish lack of semantic contradiction.
- implementation conclusion status: wired
- operation conclusion status: uninspected

User initiates lint/prune; code judges only the named structural predicates. No expected factual answer or improvement experiment; errors do not veto answering. Prune admits deletion by empty-page criterion, with no factual rejection and no backup/undo in this caller. Dashboard exposes the same prune method independently.

> if (claim.dependsOn.includes(claim.id)) {
> --- `src/cli/lint.ts`

> const pruned = store.deleteEmptyPages();
> --- `src/cli/lint.ts`

> "SELECT p.id FROM pages p LEFT JOIN claims c ON c.page_id = p.id GROUP BY p.id HAVING COUNT(c.id) = 0",
> --- `src/graph/store.ts`

#### EPI-RTE-slide-output
Label: Claim-to-slide output

No exact route counterpart after comparison with [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-RTE-client-access](runtime.md#rt-rte-client-access): this is a shipped compiler output caller with separate model generation and durable file consumption. CLI owns progression: select claims, request deck, write response. The input is retained natural-language claims plus scores; the output is Marp text (SRC-1 `src/render/marp.ts`, `src/cli/compile.ts`; implementation/design).

- Immediate return: `renderSlides` returns model text or a fixed no-claims deck; CLI writes `_slides.md`.
- Later read-back: Persisted deck is available to external presentation/human consumers; automated graph reimport is not wired by this caller.
- Delegated visibility: Model gets selected statements, percentages and topic, not source bodies or evidence histories.
- Selection predicate: Default claims have confidence at least 0.5; an existing named topic replaces that selection with all claims on the page.
- Invalidation or expiry: Subsequent compilation overwrites the same file; no automatic factual revalidation or deletion on graph change.
- Activation or effect: Model output is written without factual gate; actual output and downstream use are unobserved.
- Evidence limits: Prompt requests grouping and summary, but no deck instance or semantic comparison establishes faithful reshaping rather than additional propositions.
- implementation conclusion status: wired
- operation conclusion status: uninspected

User selects open compile request; code selects inputs and accepts the response for file writing, model proposes output prose. User may decline use externally. No answer oracle, named factual acceptance criterion, improvement trigger or rollback; fixed presentation instructions persist in code.

> if (topic) {
>     const page = store.getPageByTitle(topic);
>     if (page) {
>       claims = store.getClaimsByPage(page.id);
>       pageTitle = page.title;
>     }
>   }
> --- `src/render/marp.ts`

> return response.content;
> --- `src/render/marp.ts`

> const slides = await renderSlides(store, llm, opts.topic);
>         const outPath = join(config.paths.wiki, "_slides.md");
>         await writeFile(outPath, slides, "utf-8");
> --- `src/cli/compile.ts`

### Claims

#### EPI-CLM-living-knowledge
Label: Living confidence-scored knowledge

Distinct from [RT-CLM-confidence-citations](runtime.md#rt-clm-confidence-citations): this public design claim concerns source extraction, temporal changes, contradiction surfacing, provenance/dependencies and cascade rather than query result shape. SRC-1 `README.md`; doctrine/design only. It does not explicitly promise calibrated probability or infallible truth, so those are not attributed promises. The contrast is between its source-native operations and their actual implemented force.

> Quicky Wiki extracts claims from your sources, tracks how confident each claim is, watches for contradictions, and gives you a visual dashboard to explore everything. Think of it as a personal Wikipedia that actually tells you what it's unsure about.
> --- `README.md`

> - **Claim** — An atomic, verifiable statement extracted from a source. Has a confidence score, provenance, and dependency chain.
> --- `README.md`

> - **Cascade** — When a foundational claim is challenged, confidence changes propagate through dependent claims.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; retained context authority is supplied by [RT-BAP-retained-context](runtime.md#rt-bap-retained-context). Output-specific consumers and horizons are recorded in the ledger and slide route.
