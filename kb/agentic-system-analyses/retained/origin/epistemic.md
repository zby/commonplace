---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Origin epistemic routes: capture, lexical citation admission, page-linked entailment judgments, human review and bounded repair authority."
run-id: AAS-2026-10-15-origin-805d03bc599f-01
reviewed-boundary: "61b462ea6adf019b3e27d3f58ac5a0fe055f76b1"
---

# Origin epistemic report

## Source-and-claim boundary

The question is how Origin, branded Wenlan, turns supplied material into reusable content, checks it, and licenses later reliance. The [boundary and Source register](boundary.md#source-register) govern SRC-1; this report adds inspections within that same Git source, not new sources. The whole-system functional scope includes daemon, core, clients, desktop, shipped instructions and optional relay. External host reasoning, provider internals, deployed databases and credentials remain outside the frozen evidence. Boundary exclusions remain unchanged.

The supplied runtime is a valid provisional account, not a complete quality-gate inventory. In particular, its lexical synthesis gate is **not** the only implemented page evaluator. The separate M5 worker extracts sentence claims, judges them against linked evidence, publishes a support state and retracts stale support. This supplements, rather than supersedes, [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh): synthesis admission and subsequent truth promotion have different targets and consumers. Likewise, calling refinement acceptance does not invariably accept a factual correction: accepting a contradiction proposal only resolves its review item. See [EPI-RTE-refinement-decision](#epi-rte-refinement-decision).

Claims assessed are [EPI-CLM-notes-change](#epi-clm-notes-change), [EPI-CLM-reviewed-repair](#epi-clm-reviewed-repair), [EPI-CLM-entailment-judge](#epi-clm-entailment-judge) and the supplied [RT-CLM-ambient-ownership](runtime.md#rt-clm-ambient-ownership). No independent execution or causal experiment was supplied. Source code supports architecture; README illustrations, comments and prompts support attributed intent, not demonstrated improvement.

### Coverage and remaining uncertainty

“Direct” below means source text read in this job. “Supplied” means the runtime's findings, without claiming independent reinspection. All paths are SRC-1 commit-relative paths. Selected coverage is not exhaustive whole-system verification.

| Entry point or operation | Source path | Coverage and records, or limit and conclusion prevented |
| --- | --- | --- |
| CLI dispatch | `crates/wenlan-cli/src/main.rs` | Direct command match: capture, recall/search, brief, pages, sources, curate, lint, entities, export, sweep and outbox. Capture/recall use supplied [RT-RTE-capture-store](runtime.md#rt-rte-capture-store), [RT-RTE-recall-search](runtime.md#rt-rte-recall-search). Other subcommand internals not exhaustively traced; no CLI-wide semantic guarantee. |
| Session-start hook | `plugin/hooks/hooks.json`, `plugin/hooks/check-daemon.sh` | Direct: daemon/version and outbox status warnings; exits successfully rather than blocking. No content acceptance in inspected hook; no inference that other hosts obey guidance. |
| Registered MCP operations | `crates/wenlan-mcp/src/tools.rs` | Direct bounded searches of implementation/registration exposed repair, refinement, confirm, revisions, graph, page, brief and rejection operations beyond ordinary recall/capture. Supplied [RT-RTE-remote-query](runtime.md#rt-rte-remote-query) covers profile refusal, not direct HTTP or filesystem authority. Not every tool implementation read end-to-end. |
| Pre-store quality | `crates/wenlan-core/src/quality_gate.rs` | Direct rule/check branches; [EPI-RTE-quality-check](#epi-rte-quality-check). Supplied store record covers consequence. Config can disable gate; source accuracy is not evaluated here. |
| Synthesis and citations | `crates/wenlan-core/src/synthesis/distill.rs`, `crates/wenlan-core/src/citations.rs`, `crates/wenlan-core/src/faithfulness.rs` | Direct candidate generation, citation cleanup/scoring, admission and annotate guard; [EPI-RTE-citation-check](#epi-rte-citation-check), [EPI-RTE-citation-admission](#epi-rte-citation-admission), [EPI-RTE-citation-backfill](#epi-rte-citation-backfill); surrounding refresh writes supplied by runtime. |
| Page claim extraction, judgment, publication and invalidation | `crates/wenlan-core/src/db/claim_derivation.rs`, `crates/wenlan-core/src/claim_judge.rs` | Direct selected extraction, production policy constants, judge request/parser, promotion, finalization and SQL invalidation; [EPI-RTE-claim-extraction](#epi-rte-claim-extraction), [EPI-RTE-claim-judgment](#epi-rte-claim-judgment), [EPI-RTE-support-publish](#epi-rte-support-publish), [EPI-RTE-support-withdrawal](#epi-rte-support-withdrawal). Candidate ranking, provenance minting and full predicate not exhaustively audited; no claim of source independence or formal soundness. |
| Truth-worker owner | `crates/wenlan-server/src/main/runtime.rs` | Direct spawned task: bounded enqueue/reconciliation and eligible-provider promotion outside the ordinary scheduler account; see [EPI-RTE-claim-judgment](#epi-rte-claim-judgment). |
| Exposure and human page attestation | `crates/wenlan-core/src/truth_contract.rs`, `crates/wenlan-core/src/truth_adapter.rs`, `crates/wenlan-core/src/db/truth_exposure.rs`, `crates/wenlan-core/src/db/presence_review.rs` | Direct pure visibility decision, database wrapper, prose reduction and review mutation; [EPI-RTE-truth-exposure](#epi-rte-truth-exposure), [EPI-RTE-page-attestation](#epi-rte-page-attestation). Presence verification/UI event provenance not audited end-to-end; no authenticated-human guarantee inferred. |
| Hidden server CLI truth cutover | `crates/wenlan-server/src/main.rs`, `crates/wenlan-server/src/cmd_cutover.rs` | Direct dispatch search and complete command body; [EPI-RTE-truth-cutover](#epi-rte-truth-cutover). Core filesystem transaction internals not fully read; no crash-recovery certification. |
| Page revision review and external edits | `crates/wenlan-core/src/post_write/page_revision.rs`, `crates/wenlan-core/src/sources/page_watcher.rs` | Revision-card resolution/acceptance read directly; filesystem route supplied [RT-RTE-filesystem-edit](runtime.md#rt-rte-filesystem-edit). Revision accept is not the separate human-reviewed truth-axis mark. Complete revision SQL and dismissal internals not audited. |
| Refinement resolution | `crates/wenlan-server/src/refinery_routes.rs`, `crates/wenlan-core/src/synthesis/refinement_queue.rs` | Direct accept/reject handlers and action dispatch; [EPI-RTE-refinement-decision](#epi-rte-refinement-decision). Proposal producers and every merge/retype writer remain partly uninspected; no universal acceptance or rollback claim. |
| Lint and repair | `crates/wenlan-core/src/lint/semantic.rs`, `crates/wenlan-core/src/repair.rs`, `crates/wenlan-mcp/src/tools.rs` | Direct typed semantic result, prepare/apply/verify surface, selected apply and verification branches; [EPI-RTE-lint-assessment](#epi-rte-lint-assessment), [EPI-RTE-repair-admission](#epi-rte-repair-admission), [EPI-RTE-repair-verification](#epi-rte-repair-verification). Every deterministic check, writer and atomic verification helper not audited; no general “knowledge is true” conclusion. |
| Lab retrieval evaluation | `crates/wenlan-core/src/eval/runner.rs`, `docs/eval/README.md` | Direct ranking metric/reference construction and eval documentation; [EPI-RTE-retrieval-eval](#epi-rte-retrieval-eval). Answer-generation/judge modes and tracked M5 benchmark results not reconstructed. No measured judge accuracy or component benefit conclusion. |
| Automatic organization, prompts and numerical models | `crates/wenlan-server/src/scheduler.rs`, `crates/wenlan-core/src/prompts/mod.rs`, `crates/wenlan-core/src/llm_provider.rs`, `crates/wenlan-core/src/reranker.rs` | Supplied [RT-RTE-ambient-work](runtime.md#rt-rte-ambient-work), [RT-RTE-prompt-override](runtime.md#rt-rte-prompt-override) and runtime component records. Extraction/reconciliation/maintenance phase internals remain partly uninspected; prevents a system-complete negative on conjecture, criticism or adaptation. |
| Imports, briefs, graph creation, desktop and relay | `crates/wenlan-core/src/sources/`, `crates/wenlan-server/src/`, `app/src/`, `src/`, `relay/src/worker.ts`, `plugin/skills/`, `plugin-codex/` | Included but only partly covered by supplied boundary/runtime or surface searches. Full adapters, brief write/read semantics, graph evidence admission, UI review wiring, generated-skill parity and relay authorization not assessed here. No exhaustive lineage, admission or consumer claim across those operations. |

Missing user content and model outputs prevent identifying an actual ampliative claim, its premises or an exercised acceptance episode. Missing deployment state prevents knowing whether background AI, the eligible M5 snapshot, a nonzero truth generation, or a particular grant was active. Missing provider internals prevent a parametric-learning assessment beyond the runtime's integration findings. Missing comparative runs prevent improvement, reliability, transfer or causal attribution. These are local limits, not evidence that the routes are absent.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [RT-RTE-capture-store](runtime.md#rt-rte-capture-store) input and retained documents | Supplied assertions, corrections or other prose; truth aptitude depends on actual text | see cited record | SRC-1, `crates/wenlan-server/src/memory_routes.rs` | Route cited as supplied object carrier, not a new object declaration. Imported assertions have unknown source warrant. |
| [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh) candidate/page prose | Generated synthesis of retained snippets | see cited record | SRC-1, `crates/wenlan-core/src/synthesis/distill.rs` | Semantic preservation versus novel inference is not determinable without input/output pairs. A generated page need not be ampliative. |
| [EPI-OBJ-page-citation](#epi-obj-page-citation) | Symbolic claim-to-source occurrence records; “verified” is a lexical result | see record | SRC-1, `crates/wenlan-core/src/citations.rs` | Not semantic entailment or source-truth evidence. |
| [EPI-OBJ-derived-claim](#epi-obj-derived-claim) | Canonical sentence text, claim revisions, spans and evidence locators | see record | SRC-1, `crates/wenlan-core/src/db/claim_derivation.rs` | Extractor does not first prove that every sentence is truth apt. |
| [EPI-OBJ-page-truth](#epi-obj-page-truth) | Machine support assertion and separate human-reviewed mark for page version | see record | SRC-1, `crates/wenlan-core/src/db/presence_review.rs` | Machine score and human mark have different warrant; neither certifies the source. |
| [EPI-OBJ-lint-report](#epi-obj-lint-report) | Findings about stored structure, classification or relationships | see record | SRC-1, `crates/wenlan-core/src/lint/semantic.rs` | Finite candidate packet, not whole-store semantic completeness. |
| [EPI-OBJ-repair-manifest](#epi-obj-repair-manifest) | Symbolic permitted mutation, target identity and postconditions | see record | SRC-1, `crates/wenlan-core/src/repair.rs` | Mutation authorization is not acceptance of all propositions in the changed record. |
| [RT-OBJ-prompt-registry](runtime.md#rt-obj-prompt-registry) | Primarily policy/task guidance, not automatically truth-apt assertions | see record | SRC-1, `crates/wenlan-core/src/prompts/mod.rs` | Text may contain claims, but no actual override supplied. |
| [RT-CMP-text-embedding](runtime.md#rt-cmp-text-embedding), [RT-CMP-cross-encoder-reranker](runtime.md#rt-cmp-cross-encoder-reranker) | No individuated proposition established in numerical state | see records | SRC-1, `crates/wenlan-core/src/db.rs`, `crates/wenlan-core/src/reranker.rs` | Numerical relevance operations are not truth acceptance. |
| [RT-CMP-on-device-provider](runtime.md#rt-cmp-on-device-provider), [RT-CMP-api-provider](runtime.md#rt-cmp-api-provider), [RT-CMP-openai-compatible-provider](runtime.md#rt-cmp-openai-compatible-provider), [RT-CMP-claude-cli-provider](runtime.md#rt-cmp-claude-cli-provider) | Weights opaque; request/output prose can carry propositions | see records | SRC-1, `crates/wenlan-core/src/llm_provider.rs` | Internal beliefs, training and reliable compliance not determinable. M5 eligibility narrows the judge route, not every generation route. |

## Authority-route ledger

The ledger is a sparse overlay. The cited declarations own endpoints, timing, conditions, results, consumers, force, horizons and limitations; `see` delegates those fields without copying them. Multiple functions below remain distinct even when one implementation container supplies their evidence. Architectural status is independent of operation: all implemented rows are unobserved in this run.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs | Mismatch marker | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-capture-store](runtime.md#rt-rte-capture-store) | content transformation | implemented | see record | truth-apt transformation: acquisition/import | see record | see [EPI-RTE-quality-check](#epi-rte-quality-check) | see record | see record | see record | Source warrant unknown; imported, not system-produced knowledge | see record | see record | SRC-1, `crates/wenlan-server/src/memory_routes.rs` | none | none | Actual assertion absent |
| [EPI-RTE-quality-check](#epi-rte-quality-check) | check/evidence production | implemented | see record | no content change | see record | see record | see record | see record | see record | Noise/credential/length classification only | see record | see record | SRC-1, `crates/wenlan-core/src/quality_gate.rs` | none | none | Gate can be disabled |
| [RT-RTE-capture-store](runtime.md#rt-rte-capture-store) | disposition/acceptance | implemented | see record | no content change | see record | see record | see record | see record | see record | Operational admission, not factual acceptance | see record | see record | SRC-1, `crates/wenlan-server/src/memory_routes.rs` | none | none | Selective supersession staging, not universal review |
| [RT-RTE-capture-store](runtime.md#rt-rte-capture-store) | retention | implemented | see record | no content change | see record | see record | see record | see record | see record | Retention adds no truth license | see record | see record | SRC-1, `crates/wenlan-server/src/memory_routes.rs` | none | none | Not post-acceptance integration |
| [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh) | content transformation | implemented | see record | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Candidate generation; reshaping, entailed inference or conjecture not distinguished by code alone | see record | see record | SRC-1, `crates/wenlan-core/src/synthesis/distill.rs` | [EPI-CLM-notes-change](#epi-clm-notes-change) | unknown semantic relation | No input/output witness |
| [EPI-RTE-citation-check](#epi-rte-citation-check) | check/evidence production | implemented | see record | no content change | see record | see record | see record | see record | see record | Lexical support only | see record | see record | SRC-1, `crates/wenlan-core/src/citations.rs` | none | lexical/semantic distinction | Concrete counterexample below |
| [EPI-RTE-citation-admission](#epi-rte-citation-admission) | disposition/acceptance | implemented | see record | no content change | see record | see record | see record | see record | see record | Bounded synthesis admissibility, not warranted ampliation | see record | see record | SRC-1, `crates/wenlan-core/src/synthesis/distill.rs` | [EPI-CLM-notes-change](#epi-clm-notes-change) | none | Counts marker occurrences, not all propositions |
| [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh) | retention | implemented | see record | no content change | see record | see record | see record | see record | see record | Page commit/review-card retention does not itself establish factual acceptance | see record | see record | SRC-1, `crates/wenlan-core/src/post_write/page_update.rs` | none | none | Ownership and stale-base controls are separate |
| [EPI-RTE-citation-backfill](#epi-rte-citation-backfill) | lineage/freshness/recovery | implemented | see record | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | Annotation-only preservation guard; lexical citation status | see record | see record | SRC-1, `crates/wenlan-core/src/citations.rs` | none | none | Marker/whitespace normalization domain only |
| [EPI-RTE-claim-extraction](#epi-rte-claim-extraction) | content transformation | implemented | see record | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | Sentence indexing/canonicalization, not new knowledge | see record | see record | SRC-1, `crates/wenlan-core/src/db/claim_derivation.rs` | none | none | Sentence need not be a proposition |
| [EPI-RTE-claim-judgment](#epi-rte-claim-judgment) | check/evidence production | implemented | see record | no content change | see record | see record | see record | see record | see record | Model estimate of linked-evidence entailment | see record | see record | SRC-1, `crates/wenlan-core/src/claim_judge.rs` | [EPI-CLM-entailment-judge](#epi-clm-entailment-judge) | requested vs achieved entailment | Not formal proof or source-truth oracle |
| [EPI-RTE-support-publish](#epi-rte-support-publish) | disposition/acceptance | implemented | see record | no content change | see record | see record | see record | see record | see record | Current bounded evidence-support criterion, not universal truth | see record | see record | SRC-1, `crates/wenlan-core/src/db/claim_derivation.rs` | [EPI-CLM-entailment-judge](#epi-clm-entailment-judge) | none | Acceptance license depends on judge and selected evidence |
| [EPI-RTE-support-publish](#epi-rte-support-publish) | lifecycle integration | implemented | see record | no content change | see record | see record | see record | see record | see record | Supported verdict connects claims to scored evidence and page use | see record | see record | SRC-1, `crates/wenlan-core/src/db/claim_derivation.rs` | none | none | Post-disposition function; edges also exist before page acceptance |
| [EPI-RTE-support-withdrawal](#epi-rte-support-withdrawal) | lineage/freshness/recovery | implemented | see record | no content change | see record | see record | see record | see record | see record | Retracts old warrant; does not infer the opposite proposition | see record | see record | SRC-1, `crates/wenlan-core/src/db/claim_derivation.rs` | none | none | Unevaluated remains readable |
| [EPI-RTE-truth-exposure](#epi-rte-truth-exposure) | operational admission/selection/consumption | implemented | see record | no content change | see record | see record | see record | see record | see record | Visibility is not a new factual endorsement | see record | see record | SRC-1, `crates/wenlan-core/src/truth_contract.rs` | none | none | Generation zero and human/named-page exceptions |
| [EPI-RTE-page-attestation](#epi-rte-page-attestation) | disposition/acceptance | implemented | see record | no content change | see record | see record | see record | see record | see record | Recorded page-version review, no supplied substantive criterion | see record | see record | SRC-1, `crates/wenlan-core/src/db/presence_review.rs` | none | none | Human-reviewed does not mean machine-supported |
| [EPI-RTE-truth-cutover](#epi-rte-truth-cutover) | operational admission/selection/consumption | implemented | see record | non-truth-apt policy/content update: advance exposure regime | see record | see record | see record | see record | see record | No added semantic warrant | see record | see record | SRC-1, `crates/wenlan-server/src/cmd_cutover.rs` | none | none | Operator ceremony not observed |
| [EPI-RTE-refinement-decision](#epi-rte-refinement-decision) | disposition/acceptance | implemented | see record | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Action-dependent operational decision, not one factual criterion | see record | see record | SRC-1, `crates/wenlan-core/src/synthesis/refinement_queue.rs` | none | acceptance-name ambiguity | Contradiction acknowledgment changes no fact |
| [EPI-RTE-lint-assessment](#epi-rte-lint-assessment) | check/evidence production | implemented | see record | no content change | see record | see record | see record | see record | see record | Structural or candidate-bounded semantic finding | see record | see record | SRC-1, `crates/wenlan-core/src/lint/semantic.rs` | [EPI-CLM-reviewed-repair](#epi-clm-reviewed-repair) | none | Advisory is not direct mutation |
| [EPI-RTE-repair-admission](#epi-rte-repair-admission) | disposition/acceptance | implemented | see record | non-truth-apt policy/content update: authorize bounded repair | see record | see record | see record | see record | see record | Target/effect authorization, not world truth | see record | see record | SRC-1, `crates/wenlan-core/src/repair.rs` | [EPI-CLM-reviewed-repair](#epi-clm-reviewed-repair) | none | Human intent partly cooperative |
| [EPI-RTE-repair-verification](#epi-rte-repair-verification) | check/evidence production | implemented | see record | no content change | see record | see record | see record | see record | see record | Repair postcondition/report consistency | see record | see record | SRC-1, `crates/wenlan-core/src/repair.rs` | [EPI-CLM-reviewed-repair](#epi-clm-reviewed-repair) | none | Does not license producing mechanism or transfer |
| [RT-RTE-recall-search](runtime.md#rt-rte-recall-search) | operational admission/selection/consumption | implemented | see record | no content change | see record | see record | see record | see record | see record | Query relevance and scope, not factual correctness | see record | see record | SRC-1, `crates/wenlan-server/src/memory_routes.rs` | none | none | Host compliance/answer effects unobserved |
| [RT-RTE-filesystem-edit](runtime.md#rt-rte-filesystem-edit) | content transformation | implemented | see record | truth-apt transformation: acquisition/import | see record | see record | see record | see record | see record | External replacement prose; source warrant unknown | see record | see record | SRC-1, `crates/wenlan-core/src/sources/page_watcher.rs` | [EPI-CLM-notes-change](#epi-clm-notes-change) | none | Not synthesis-gated |
| [RT-RTE-prompt-override](runtime.md#rt-rte-prompt-override) | behavior/policy adaptation | implemented | see record | non-truth-apt policy/content update: replace task instructions | see record | see record | see record | see record | see record | No evidence-consuming improvement criterion | see record | see record | SRC-1, `crates/wenlan-core/src/prompts/mod.rs` | none | none | Manual configuration, not proved feedback improvement |
| [EPI-RTE-retrieval-eval](#epi-rte-retrieval-eval) | check/evidence production | implemented | see record | no content change | see record | see record | see record | see record | see record | Retrieval performance against seeded references only | see record | see record | SRC-1, `crates/wenlan-core/src/eval/runner.rs` | none | none | Lab output has no traced automatic production update |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-notes-change](#epi-clm-notes-change) | see record | SRC-1, `README.md`; doctrine/design | see record | [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh), [EPI-RTE-support-publish](#epi-rte-support-publish), [RT-RTE-filesystem-edit](runtime.md#rt-rte-filesystem-edit) | None supplied; README labels illustration | No intervention/comparison establishing improved future action | Source-change maintenance, revisions and reuse are implemented capacities | “Improves” is not demonstrated; not all writes share review/citation gates |
| [EPI-CLM-reviewed-repair](#epi-clm-reviewed-repair) | see record | SRC-1, `README.md`; doctrine/design | see record | [EPI-RTE-lint-assessment](#epi-rte-lint-assessment), [EPI-RTE-repair-admission](#epi-rte-repair-admission), [EPI-RTE-repair-verification](#epi-rte-repair-verification) | None supplied | Gate correctness and crash behavior not experimentally established | Separate report, bounded apply and verification paths exist | Not a blanket factuality certificate; every writer not audited |
| [EPI-CLM-entailment-judge](#epi-clm-entailment-judge) | see record | SRC-1, `crates/wenlan-core/src/claim_judge.rs`; doctrine/design prompt and implementation parser | see record | [EPI-RTE-claim-judgment](#epi-rte-claim-judgment), [EPI-RTE-support-publish](#epi-rte-support-publish), [EPI-RTE-truth-exposure](#epi-rte-truth-exposure) | None supplied | Pinned model/prompt and typed numeric contract do not prove semantic correctness | Genuine evidence-consuming support decisions, with bounded model-estimated entailment | Actual accuracy, source truth and activation unknown |
| [RT-CLM-ambient-ownership](runtime.md#rt-clm-ambient-ownership) | see record | SRC-1, `crates/wenlan-server/src/memory_routes.rs`; doctrine/design | see record | [RT-RTE-ambient-work](runtime.md#rt-rte-ambient-work) | None supplied | Request-time enrichment ownership does not describe every inference task | Capture enrichment scheduling is supported | Separate M5 task in `crates/wenlan-server/src/main/runtime.rs` means “all automatic inference uses one scheduler facade” would overstate the supplied finding |

## Bounded conclusion

Origin can acquire assertions and corrections, retain them, generate pages, and return selected material to later clients. Those functions establish import, retention and reuse, not source endorsement. Capture quality controls target noise and credentials; synthesis citation controls target lexical association. Neither establishes source truth. Generated prose is a candidate whose content/update relation remains indeterminate without actual input/output content. No claim of produced accepted ampliative knowledge follows from the route's existence alone. See [RT-RTE-capture-store](runtime.md#rt-rte-capture-store), [EPI-RTE-quality-check](#epi-rte-quality-check), [EPI-RTE-citation-check](#epi-rte-citation-check), [RT-RTE-recall-search](runtime.md#rt-rte-recall-search).

There is nevertheless more than retention and lexical reshaping. M5 implements evidence-consuming acceptance against a named criterion: eligible model-estimated entailment of extracted page claims by selected linked evidence, with current registry thresholds, evidence identity checks and completed-run constraints. Support edges and a page-version verdict can then affect subsequent use. That is a bounded acceptance/integration architecture, not proof that the premises are true, that candidate retrieval is exhaustive, that the semantic judgment is sound, or that a new proposition was ampliative. Missing outputs prevent individuating an actual accepted claim. See [EPI-RTE-claim-extraction](#epi-rte-claim-extraction), [EPI-RTE-claim-judgment](#epi-rte-claim-judgment), [EPI-RTE-support-publish](#epi-rte-support-publish).

Machine rejection has qualified operational force. At nonzero truth generation, judged unsupported and unreviewed pages are hidden from automatic page consumers; collection/named-page grants provide bounded inspection exceptions. At generation zero the adapter passes through, and even after cutover unevaluated pages remain visible. Human-reviewed pages outrank machine support. Withdrawal can therefore revoke a published support assertion without revoking all access. The consumer path is stored truth state → visibility/adapters → page-bearing server/recall results and projection permissions, enforcing only the selected exposure regime. See [EPI-RTE-support-withdrawal](#epi-rte-support-withdrawal), [EPI-RTE-truth-exposure](#epi-rte-truth-exposure), [EPI-RTE-truth-cutover](#epi-rte-truth-cutover), [EPI-RTE-page-attestation](#epi-rte-page-attestation).

Human page review, revision-card acceptance, refinement acknowledgment and repair authorization are not interchangeable. The first marks a particular page version; revision acceptance installs staged prose subject to source/version fencing; contradiction acceptance merely clears a review item; repair acceptance authorizes a named mutation, with separate postcondition verification. None supplies a universal substantive truth criterion. See [EPI-RTE-page-attestation](#epi-rte-page-attestation), [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh), [EPI-RTE-refinement-decision](#epi-rte-refinement-decision), [EPI-RTE-repair-admission](#epi-rte-repair-admission), [EPI-RTE-repair-verification](#epi-rte-repair-verification).

Prompt replacement directly changes future task guidance without a truth-apt acceptance route. Numerical components provide inference/ranking with the mutability limits in the runtime records; M5 further restricts eligible judge snapshots. Retained memory changes do not demonstrate parameter learning. Improved capacity, reflection, autonomous theory building and self-improvement are not inferred from persistence or page revision. No specific theory-bearing content/criticism episode was supplied to assess theory-builder conditions 1–4 individually; uninspected automatic phase internals also preclude a complete architectural negative. Lab retrieval references measure ranking, not successful future reasoning, and no production policy-update consumer was traced for their scores. See [RT-RTE-prompt-override](runtime.md#rt-rte-prompt-override), [EPI-RTE-retrieval-eval](#epi-rte-retrieval-eval) and the coverage limits above. These route-level conclusions do not combine into one system-wide epistemic verdict.

## Shared records

### Operative objects

#### EPI-OBJ-page-citation
Label: PageCitation

Part of: [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh)

This symbolic output part of the supplied refresh route consists of ordered marker occurrences, source kind/locator, score, status and sentence/paragraph scope. The carrier is serialized page citation metadata alongside natural-language page prose. It differs from the whole synthesis route and from M5 claim/support state. SRC-1, `crates/wenlan-core/src/citations.rs`, construction in `process_citation_output`.

> status: if claim_verified {
>     "verified"
> } else {
>     "unverified"
> }
> .to_string(),
> scope: scope.to_string(),
> --- `crates/wenlan-core/src/citations.rs`

#### EPI-OBJ-derived-claim
Label: DerivedClaim

Natural-language canonical sentence text plus symbolic revision IDs, digests and raw-span alignment, retained in the claim/revision/derivation database substrate. This is a distinct later representation of page prose, not another name for the supplied page-refresh route or citation occurrence. SRC-1, `crates/wenlan-core/src/db/claim_derivation.rs`.

> pub(super) struct DerivedClaim {
>     revision_id: String,
>     canonical_text: String,
>     canonical_text_digest: String,
> }
> --- `crates/wenlan-core/src/db/claim_derivation.rs`

#### EPI-OBJ-page-truth
Label: page_truth_state

Symbolic persisted page-version support disposition, evaluation timestamp, reason and separate human-reviewed/version/digest binding. Natural-language reasons explain failures; fixed SQL/visibility rules consume the state. Unlike [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh), this is the later warrant/authority carrier, not the page candidate or ownership flag. SRC-1, `crates/wenlan-core/src/db/claim_derivation.rs`, `crates/wenlan-core/src/db/presence_review.rs`; supporting mutations appear in [EPI-RTE-support-publish](#epi-rte-support-publish) and [EPI-RTE-page-attestation](#epi-rte-page-attestation).

#### EPI-OBJ-lint-report
Label: LintReport

Symbolic typed reports and evidence references, with model/agent semantic findings represented as action, reason, confidence, evidence and counterevidence IDs. MCP caches reports for exact scopes; repair artifacts consume them. Distinct from supplied runtime scheduling and recall records: this object carries diagnostic evidence, not recalled knowledge. SRC-1, `crates/wenlan-core/src/lint/semantic.rs`, `crates/wenlan-mcp/src/tools.rs`; evidence passage in [EPI-RTE-lint-assessment](#epi-rte-lint-assessment).

#### EPI-OBJ-repair-manifest
Label: RepairManifest

Symbolic immutable artifact in the private repair store: manifest digest, target receipt, expected state, writer, allowed effects and verification policy. It licenses a bounded operation, unlike the advisory lint report. No supplied runtime counterpart declares repair artifacts; runtime explicitly deferred them. SRC-1, `crates/wenlan-core/src/repair.rs`; passages in [EPI-RTE-repair-admission](#epi-rte-repair-admission) and [EPI-RTE-repair-verification](#epi-rte-repair-verification).

### Routes

#### EPI-RTE-quality-check
Label: Pre-store quality check

Part of: [RT-RTE-capture-store](runtime.md#rt-rte-capture-store)

The gate is the checking part, distinct from the parent's disposition and durable write. Incoming writer proposes; symbolic rules assess meaningful word count, configured credential/noise patterns and optional similarity. The target/domain is admissible capture text, not truth of the asserted facts. There is no expected-answer oracle. Open ingestion, triggered by store; software can reject, while near-duplicate warnings need not reject. The disabled branch explicitly admits everything, a countercase to an unconditional quality guarantee. Storage consequences belong to the parent route, not a claim that this check itself installs accepted knowledge. SRC-1, `crates/wenlan-core/src/quality_gate.rs`.

- Immediate return: GateResult with admitted flag, reason and scores to the ingest caller.
- Later read-back: inapplicable — this check's return is current-call state; parent route owns retention/rejection logs.
- Delegated visibility: rule code sees incoming content; similarity evaluation can query stored candidates.
- Selection predicate: configuration enabled flag, minimum meaningful words, credential/noise settings; similarity can soft-flag.
- Invalidation or expiry: inapplicable — reevaluated per input; no independent retained verdict established here.
- Activation or effect: parent ingest path consumes admission to permit/refuse storage; no factual endorsement.
- Evidence limits: inspected rules and supplied parent wiring; deployed configuration and false-positive rates unknown.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> // Gate disabled → admit everything
> if !self.config.enabled {
>     return GateResult {
>         admitted: true,
> --- `crates/wenlan-core/src/quality_gate.rs`

#### EPI-RTE-citation-check
Label: Per-claim citation verification

Part of: [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh)

This is the parent's checking part, not its admission decision. The target is a marked sentence, then its enclosing paragraph if needed, against the union of sources cited in that span. Code normalizes spaced/comma markers, strips out-of-range markers, and assigns per-occurrence results. Evaluator is maximum bidirectional lexical overlap with floor 0.5; source text is selected/capped before generation. It supplies a lexical-support estimate, not entailment or premise truth. Model proposes citations, software decides labels; there is no human veto at this check and no answer-key oracle. SRC-1, `crates/wenlan-core/src/citations.rs`, `crates/wenlan-core/src/faithfulness.rs`.

- Immediate return: cleaned body, citation occurrence records and aggregate counts.
- Later read-back: parent writes may retain body/citation JSON; later readers can inspect labels, with no demonstrated answer effect.
- Delegated visibility: checker sees marked body and numbered source snippets, not unrestricted external evidence.
- Selection predicate: markers surviving range cleanup, grouped by sentence; paragraph fallback when sentence fails.
- Invalidation or expiry: source/page refresh rechecks; this pure result has no independent expiry service.
- Activation or effect: counts feed [EPI-RTE-citation-admission](#epi-rte-citation-admission); labels alone do not mutate pages.
- Evidence limits: deterministic counterexample below demonstrates license limits without target execution; M5 is a separate stronger semantic request.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> crate::faithfulness::overlap_fraction(span, source)
>     .max(crate::faithfulness::overlap_fraction(source, span))
> --- `crates/wenlan-core/src/citations.rs`

> let sentence_verified = bidirectional_support(sentence, &union) >= 0.5;
> --- `crates/wenlan-core/src/citations.rs`

> .filter(|t| t.len() >= 4 && !STOPWORDS.contains(&t.as_str()))
> --- `crates/wenlan-core/src/faithfulness.rs`

Concrete implementation deduction: take one numbered source `Backups are encrypted.` and generated body `Backups are not encrypted.[1]`. Marker 1 survives. Marker-free sentence contains the tokens `backups` and `encrypted`; `are` and `not` are shorter than four characters and disappear. Both retained tokens match whole words in the source, so sentence support is 1, the one occurrence is verified, and zero unverified occurrences remain. The synthesis gate below therefore admits the candidate at this stage despite negating the source. This is an implementation-layer trace, not an executed example or a counterexample to the separate M5 judge. It establishes why the lexical badge cannot license semantic entailment. Out-of-range cleanup also removes a bad citation marker, not the associated unsupported prose.

#### EPI-RTE-citation-admission
Label: Synthesis citation gate

Part of: [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh)

Separate disposition part: `synthesize_candidate_body` consumes citation counts, discards when zero occurrences are verified or unverified exceed verified, otherwise returns Verified candidate content/metadata/summary. Intended use is admission to the subsequent canonical page-write/review path, scope the generated body from current selected snippets. This is evidence-consuming operational acceptance under a lexical criterion, not acceptance of an ampliative factual claim. Automatic/manual refresh initiates the open synthesis; provider proposes, code vetoes; subsequent ownership review can still prevent overwrite. No expected answer is supplied. The later M5 route is a countercase to “no semantic checking anywhere,” not a reason to relabel this gate as semantic. SRC-1, `crates/wenlan-core/src/synthesis/distill.rs`.

- Immediate return: Unavailable, Discarded with reason, or Verified candidate to refresh caller.
- Later read-back: accepted candidate may be committed or staged by parent; rejected candidate has no authorized page overwrite through this branch.
- Delegated visibility: consumer receives processed content, citation JSON, summary and stats, not a proven proposition.
- Selection predicate: nonempty sources/output and count rule below.
- Invalidation or expiry: parent compile/source fences can still reject a candidate based on changed state.
- Activation or effect: permits continuation into page mutation or review staging, not unconditional publication.
- Evidence limits: occurrence-majority rule does not cover uncited claims, premises' truth or semantic entailment.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if stats.verified == 0 || stats.unverified > stats.verified {
> --- `crates/wenlan-core/src/synthesis/distill.rs`

#### EPI-RTE-citation-backfill
Label: Annotate-only citation backfill

The independent legacy-page sweep asks a model for markers but compares normalized marker-stripped output with original prose before writing. Unlike refresh, it is not allowed to replace the page's claims. Software vetoes changed prose; zero citations/provider/guard failures retry up to three attempts, then persist an empty citation array with give-up bookkeeping. Successful writes use version, source revision and incarnation fences. This is lineage annotation with a checked text-preservation domain, not new evidence acquisition. No supplied runtime route declares this legacy backfill; it shares citation functions with [EPI-RTE-citation-check](#epi-rte-citation-check) but has different selected objects, gate and failure policy. SRC-1, `crates/wenlan-core/src/citations.rs`.

- Immediate return: sweep selected count; per-page write or recorded failed attempt.
- Later read-back: page citations/changelog or terminal empty array persist for later readers; empty means attempted/given up here, not proof of support.
- Delegated visibility: model sees page and selected numbered evidence; caller receives no added external warrant.
- Selection predicate: legacy annotation workload and bounded batch; normalized marker-free equality; nonempty citation results for success.
- Invalidation or expiry: generation-keyed attempt state and fenced writes; successful terminal commit clears matching attempt metadata.
- Activation or effect: annotates retained prose without approving its truth; rejected outputs do not replace prose through this route.
- Evidence limits: only marker/whitespace preservation is checked; normalization is not a general semantic equivalence proof.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let same =
>     normalize_ws(&strip_markers(&out)) == normalize_ws(&strip_markers(&page.content));
> --- `crates/wenlan-core/src/citations.rs`

A concrete input `Backups are encrypted.[1]` and annotated output `Backups are encrypted.[ 1 ]` do not require a new factual inference. The guard strips only `[N]` without spaces before equality, so the spaced-marker version can fail this guard even though later marker normalization would recognize it. Preservation here is an implementation-specific text condition, not an omniscient semantic evaluator. The simpler output `Backups are encrypted.[1][2]` passes equality against that input after both markers are stripped; citation range/scoring and fences still run.

#### EPI-RTE-claim-extraction
Label: Page claim extraction

The derivation worker turns the leased page version into marker-free sentence cuts, canonical text/digests and aligned revisions. This is deterministic indexing/reshaping; canonicalization collapses whitespace, applies NFC and removes a final period. It does not infer a new proposition or prove every sentence declarative. Distinct from [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh): that generates the page; this later worker enumerates its units for checking. SRC-1, `crates/wenlan-core/src/db/claim_derivation.rs`.

- Immediate return: DerivedClaim list and Written/StaleLease/TooManyClaims disposition to promoter.
- Later read-back: stored claim revisions, alignment and derivation markers feed later support evaluation/reconciliation.
- Delegated visibility: downstream judge receives selected claim text/evidence pairs, not the entire database.
- Selection predicate: leased current page, nonblank sentence spans, maximum 200 claims.
- Invalidation or expiry: page version/content, extractor version and lease/run generation govern reuse/rederivation.
- Activation or effect: creates the claim inventory that makes later completed-support decisions possible; no epistemic acceptance at extraction.
- Evidence limits: sentence splitting is not proposition individuation for all languages/content; no actual page content supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> let cuts: Vec<CutClaim> = crate::faithfulness::sentence_spans(&bare)
> --- `crates/wenlan-core/src/db/claim_derivation.rs`

> let nfc: String = raw.nfc().collect();
> let mut canonical = nfc.split_whitespace().collect::<Vec<_>>().join(" ");
> if canonical.ends_with('.') {
>     canonical.pop();
> }
> --- `crates/wenlan-core/src/db/claim_derivation.rs`

#### EPI-RTE-claim-judgment
Label: Page-linked truth promotion judge

The daemon's separate spawned truth-maintenance task, not the ordinary scheduler slice alone, attempts promotion when background AI and an eligible on-device provider are available. Promoter loads linked chunks, attaches provenance roots, ranks bounded candidates, seals a run inventory, reuses matching cached scores or calls the judge in bounded batches, and persists run judgments. Judgment target/domain is **whether a selected linked evidence span directly entails one extracted claim**. Prompt explicitly asks for negation, modality, quantifier, date and scope sensitivity. It is a model estimate, not an answer oracle supplied by a known external truth label. Exact item IDs and finite [0,1] score syntax are checked; syntax validation cannot establish correctness.

Only an approved production judge snapshot/policy can activate this route; the inspected constants name qwen3-4b, a specific HF commit/file and threshold 0.75. The configured provider must satisfy available on-device/version snapshot requirements, and active policy supplies the operative threshold/generation. This is narrower than [RT-CMP-on-device-provider](runtime.md#rt-cmp-on-device-provider), not a duplicate component or a claim that all installed models share these bytes. No parameter update is implemented by this request/score path; actual loaded artifact and its internal inference remain unobserved. Distinct from lexical synthesis admission and the supplied automatic enrichment route, though both use provider infrastructure. SRC-1, `crates/wenlan-core/src/db/claim_derivation.rs`, `crates/wenlan-core/src/claim_judge.rs`, `crates/wenlan-server/src/main/runtime.rs`.

- Immediate return: Idle, RefusedProvider, Completed, Requeued, Parked or error to the truth-maintenance loop; parsed scores and persisted attempts internally.
- Later read-back: cache keyed to claim/evidence and judge identity, run judgments and support edges feed later publication/reconciliation.
- Delegated visibility: provider gets JSON claim/evidence items and pinned system instructions, bounded to batches of at most 25 items.
- Selection predicate: eligible provider and policy, leased page, linked-evidence candidate inventory and budget ceilings; cache hit or fresh complete valid response.
- Invalidation or expiry: evidence/claim digests, model/prompt version and current eligibility policy bound reuse; lease reclamation separates stale attempts.
- Activation or effect: scores at/above active threshold can write support edges; publication has an additional completed/current-run predicate.
- Evidence limits: not inspected benchmark validation, no execution or actual scores; selected linked evidence is not all possible evidence, and provenance identity is not premise truth.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if !provider.is_available() || provider.backend() != LlmBackend::OnDevice {
>     return None;
> }
> --- `crates/wenlan-core/src/claim_judge.rs`

> pub(super) const M5_PRODUCTION_JUDGE_THRESHOLD: f64 = 0.75;
> --- `crates/wenlan-core/src/db/claim_derivation.rs`

> if *score < threshold {
>     continue;
> }
> --- `crates/wenlan-core/src/db/claim_derivation.rs`

> .run_page_linked_truth_promotion_turn(
>     provider.as_ref(),
>     "wenlan-server-truth-maintenance",
> ) => result,
> --- `crates/wenlan-server/src/main/runtime.rs`

#### EPI-RTE-support-publish
Label: Page support finalization

Promoter's judgment outputs are not themselves the page verdict. `evaluate_support_on` checks the page/claim inventory, current eligible above-threshold support edges, concluded run candidates and resolvable evidence. Incomplete/unaccounted/unresolvable candidates cause NoPublish; never-judged claims yield Unevaluated; judged claims lacking support can yield Refuted. `finalize_page_support` checks exact lease/run/eligibility and recomputes the verdict inside the write transaction. It maps Supported to supported/stamped, Refuted to provisional/stamped, and Unevaluated to provisional/unstamped. Software proposes/decides this disposition; no per-item human approval is required, and machine publication never manufactures human review.

Acceptance criterion/intended use/scope: record **current page-version evidence support** under the eligible-judge/complete-run predicate so later readers and projection policies can use it. Scope is selected linked evidence and extracted claim inventory, not universal validity. This is a distinct disposition part of the M5 pipeline, with post-acceptance integration when the accepted page support is connected to retained support edges and consumed by visibility. Edge retention can precede whole-page acceptance; that ordering is not itself lifecycle integration. Closest supplied [RT-RTE-page-refresh](runtime.md#rt-rte-page-refresh) commits or stages prose, whereas this route commits a later evidential status. SRC-1, `crates/wenlan-core/src/db/claim_derivation.rs`.

- Immediate return: bool publication success or error; promoter reports completed only after successful publication/job completion.
- Later read-back: page_truth_state and linked support/attempt records persist for exposure and later reconciliation.
- Delegated visibility: visibility consumers receive support status, not raw model reasoning or an independently proven source.
- Selection predicate: current page, valid exact lease and eligibility generation, recomputed identical publishable outcome.
- Invalidation or expiry: page/evidence changes, edge withdrawals and policy/extractor drift can demote/requeue support; review marks survive only matching versions.
- Activation or effect: persists machine support and its evidence linkage; enforces status transition, and later exposure may change depending on generation/grant.
- Evidence limits: predicate cannot make a wrong semantic score true; completed selected inventory is not exhaustive world evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if Self::evaluate_support_on(&tx, page_id, page_version).await? != *outcome {
>     return Ok(false);
> }
> --- `crates/wenlan-core/src/db/claim_derivation.rs`

> SupportOutcome::Supported => ("supported", None, Some(now)),
> SupportOutcome::Refuted { reason } => {
>     ("provisional", Some(reason.clone()), Some(now))
> }
> --- `crates/wenlan-core/src/db/claim_derivation.rs`

#### EPI-RTE-support-withdrawal
Label: Support demotion and rederivation

SQL triggers and reconciliation revoke stored support when the page or its supporting memory/chunk changes, is moved or deleted; source rebinding and current-policy reconciliation have related demotion paths. The inspected trigger builders demote supported rows to provisional, clear evaluated_at and enqueue/reset derivation jobs. This retracts the prior support assertion without asserting the page false. Old run generations become inoperative even if attempt rows remain. No newly invented content, expected-answer oracle or human decision is needed for this invalidation. Distinct from supplied refresh staleness: this changes the machine-warrant carrier, not just scheduling a rewrite. SRC-1, `crates/wenlan-core/src/db/claim_derivation.rs`.

- Immediate return: SQL mutation or bounded reconciliation batch result to writer/maintenance caller.
- Later read-back: provisional/unstamped truth state and pending job affect future exposure/rechecking; attempts may remain as inactive history.
- Delegated visibility: later readers see reevaluated truth axes/visibility, not necessarily the full withdrawal cause.
- Selection predicate: affected page/claim-support edges and named trigger events; reconciliation re-proves prior supported verdicts.
- Invalidation or expiry: immediate affected-state change; lease/run reset prevents predecessor conclusions retaining current authority.
- Activation or effect: revokes old support claim and requests fresh evidence checking; does not necessarily hide prose because Unevaluated remains visible.
- Evidence limits: source implementation only, no concurrent/crash execution assurance; every provenance/edge mutation path not audited.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> SET support_status = 'provisional',
>     provisional_reason = '{reason}',
>     evaluated_at = NULL,
> --- `crates/wenlan-core/src/db/claim_derivation.rs`

> CREATE TRIGGER IF NOT EXISTS m5_demote_support_on_chunk_edit
> AFTER UPDATE OF content ON memories
> WHEN NEW.content IS NOT OLD.content
> --- `crates/wenlan-core/src/db/claim_derivation.rs`

#### EPI-RTE-truth-exposure
Label: Truth-grant page visibility

Page-bearing consumers resolve generation, page truth and per-call grant. Generation zero is pass-through. At nonzero generation, human_reviewed, Supported and Unevaluated yield Full; only judged Unsupported without an overriding human mark is hidden automatically. CollectionEntries can expose identity/title/axes without prose; NamedPages can expose full prose/axes only for named IDs. Reduce-to-entry clears body, summary, citation/provenance-bearing fields and other prose. The marker/contract shape controls are code-enforced, but marker authenticity is cooperative; named-page inspection is not factual acceptance. This spans page readers, projection/export/redistill permits and the supplied [RT-RTE-recall-search](runtime.md#rt-rte-recall-search), so it is not part of that single read route. SRC-1, `crates/wenlan-core/src/truth_contract.rs`, `crates/wenlan-core/src/truth_adapter.rs`, `crates/wenlan-core/src/db/truth_exposure.rs`.

- Immediate return: Full, EntryOnly, Hidden, filtered/redacted payload or write permit to page-bearing caller.
- Later read-back: each later read recomputes against durable generation/truth state; this route itself need not retain a new proposition.
- Delegated visibility: external clients get only surviving projections; entry-only is not a hidden full-body attachment.
- Selection predicate: generation, human-reviewed binding, three-state support and route-compatible contract/explicit marker/named IDs.
- Invalidation or expiry: changed truth state, review/version binding, cutover generation or call grant changes subsequent decisions.
- Activation or effect: enforcing delivery/permission change at inspected adapters; no evidence delivered knowledge changed host reasoning.
- Evidence limits: deployed generation/grants unknown; all adapters/callers and projection crash semantics not audited.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if generation == 0 {
>     return Visibility::Full;
> }
> if human_reviewed {
>     return Visibility::Full;
> }
> match support {
>     Support::Supported | Support::Unevaluated => return Visibility::Full,
>     Support::Unsupported => {}
> }
> --- `crates/wenlan-core/src/truth_contract.rs`

> page.summary = None;
> page.content = String::new();
> page.citations = Vec::new();
> --- `crates/wenlan-core/src/truth_adapter.rs`

#### EPI-RTE-page-attestation
Label: Human-reviewed page mark

A separately verified-presence request applies a version/digest-bound page-review receipt, consumes its nonce and sets the human-reviewed axis without manufacturing machine support. This is distinct from revision-card acceptance in `post_write/page_revision.rs`: installing staged prose and attesting review have different effects. The inspected revision accept checks source/version fences and installs staged body; the truth mark is an independent route. No supplied runtime record declares this attestation. Its intended use is human review override of page exposure; a substantive factual acceptance criterion and actual human judgment are not supplied. SRC-1, `crates/wenlan-core/src/db/presence_review.rs`, `crates/wenlan-core/src/post_write/page_revision.rs`.

- Immediate return: recorded PageReviewReceipt or replay/refusal/error through the review operation.
- Later read-back: page_truth_state and presence receipts retain exact page-version/digest approval for later visibility.
- Delegated visibility: downstream code receives a symbolic review mark, not the person's reasons or an entailment proof.
- Selection predicate: bound request/page/version/digest, verified presence and unused nonce within the surrounding protocol.
- Invalidation or expiry: nonce replay refusal and page-version binding; machine publication preserves review only for the matching version.
- Activation or effect: review can override unsupported exposure status; it does not rewrite machine support evidence.
- Evidence limits: presence-verification implementation and UI gesture provenance not traced end-to-end; no actual human acceptance episode.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> // The two axes are independent, and a human saying "I read this" is not
> // evidence about whether the machine found support — inventing `supported`
> // here would collapse the separation the whole rung exists to make.
> --- `crates/wenlan-core/src/db/presence_review.rs`

> ON CONFLICT(page_id) DO UPDATE SET
>      human_reviewed = 1,
>      reviewed_page_version = ?2,
>      reviewed_page_digest = ?3,
> --- `crates/wenlan-core/src/db/presence_review.rs`

#### EPI-RTE-truth-cutover
Label: Operator truth cutover

The hidden server CLI command, omitted from the ordinary runtime account, selects a generation at least one and checks unloaded service/no running daemon plus data-root lock. It plans projection evictions, records dry-run digest, then on apply requires current matching unspent plan and explicit y/Y. It calls the core cutover writer and spends the dry-run digest. Intended effect is changing the enforcing exposure regime and moving affected projection files to archive, not deleting database claims or proving them false. Operator can abort; generation advancement is forward-only, while archived files remain available. Distinct from automatic work and [EPI-RTE-truth-exposure](#epi-rte-truth-exposure): this changes when its policy has force. SRC-1, `crates/wenlan-server/src/cmd_cutover.rs`, `crates/wenlan-server/src/main.rs`.

- Immediate return: dry-run plan/digest, refusal/abort, or applied generation/eviction report.
- Later read-back: durable cutover generation governs later server/adapter/projection behavior; archived files retain old prose separately.
- Delegated visibility: operator sees selected file/page plan before confirmation; later clients do not inherit operator approval of factual content.
- Selection predicate: stopped daemon, valid increasing generation, matching dry run and y/Y confirmation.
- Invalidation or expiry: changed plan invalidates approval; successful apply blanks the stored dry-run digest; generation cannot be rolled back by this command.
- Activation or effect: enables nonzero-generation restrictions and invokes projection archive operation.
- Evidence limits: core cutover filesystem transaction not fully audited and no ceremony executed; live generation unknown.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if !matches!(answer.trim(), "y" | "Y") {
>     println!("Aborted. Nothing was changed.");
>     return Ok(());
> }
> --- `crates/wenlan-server/src/cmd_cutover.rs`

> .run_truth_cutover(&db, generation, &plan.digest)
> --- `crates/wenlan-server/src/cmd_cutover.rs`

#### EPI-RTE-refinement-decision
Label: Refinement action resolution

Daemon accept/reject endpoints feed core action dispatch. Existing proposal producers supply a candidate; a caller decision selects action. Shipped MCP guidance requests unambiguous item-level human decisions, but the inspected handler/core dispatch do not themselves prove the caller was human. Code rejects terminal proposals/invalid shapes and unsupported actions. Accept entity_merge/relation_conflict can change identities/relations; page merge/archive and vocabulary promotion have separate effects; contradiction acceptance validates shape then resolves without mutating either memory. `dedup_merge` and `suggest_entity` have no accept path. Reject resolves Dismissed rather than deleting underlying memory/page. The action family is retained here as dispatch coverage; individual merge writers/producers remain unassessed, so the indeterminate content relation is not a blanket claim of semantic equivalence. Distinct from the runtime's page ownership/revision route. SRC-1, `crates/wenlan-core/src/synthesis/refinement_queue.rs`, `crates/wenlan-server/src/refinery_routes.rs`, `crates/wenlan-mcp/src/tools.rs`.

- Immediate return: applied action/ID, rejection resolution, or validation/error response.
- Later read-back: resolved/dismissed queue status and action-specific mutations affect later review and knowledge readers.
- Delegated visibility: calling client receives selected proposal/action outcome, not evidence that a human applied a factual criterion.
- Selection predicate: named open proposal, supported action/payload and any required destination decision; no expected-answer oracle.
- Invalidation or expiry: terminal statuses refuse retry; action-specific rollback uninspected, not guaranteed.
- Activation or effect: action-dependent mutation or queue acknowledgment; contradiction acceptance grants no factual replacement authority.
- Evidence limits: aggregate dispatch is not full semantic assessment of every action/producer; actual user decisions absent.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> // Validate the proposal shape, then acknowledge-and-resolve below —
> // do NOT mutate either memory. A pure contradiction keeps both facts;
> --- `crates/wenlan-core/src/synthesis/refinement_queue.rs`

> "dedup_merge" => {
>     return Err(WenlanError::Validation(
>         "action 'dedup_merge' has no accept path (deprecated stale-v1 variant)".into(),
>     ));
> }
> --- `crates/wenlan-core/src/synthesis/refinement_queue.rs`

#### EPI-RTE-lint-assessment
Label: Lint evidence production

General is exposed as bounded deterministic checking; Deep adds candidate generation and configured-provider or explicitly consented agent adjudication. Direct inspection establishes that semantic findings retain reason/confidence/evidence/counterevidence, bounded packet coverage and **Advisory** gate effect. Target is a candidate classification/link/relation/evidence issue within an explicit packet, not truth of every stored assertion. Model/agent verdicts are not an independent expected-answer oracle; structural/typed validation supplies a different check from semantic correctness. Operator requests lint; no canonical mutation follows merely from a Finding. Closest supplied runtime explicitly left lint/repair details untraced, so this declares new diagnostic coverage. SRC-1, `crates/wenlan-core/src/lint/semantic.rs`, `crates/wenlan-mcp/src/tools.rs`.

- Immediate return: typed report or prepared work packet/incomplete status to caller; MCP caches qualifying reports.
- Later read-back: exact-scope cached reports can seed repair planning; standalone result does not rewrite knowledge.
- Delegated visibility: bounded referenced records/candidates to model or calling agent, evidence references to report consumer.
- Selection predicate: profile/scope, available prerequisites, consented agent-assist or configured provider; bounded candidate generation.
- Invalidation or expiry: new lint calls/cache generations and consumed planning reports restrict reuse; full daemon snapshot semantics not audited here.
- Activation or effect: advisory diagnostic evidence; separate repair admission supplies mutation force.
- Evidence limits: every deterministic check, semantic candidate producer and submission validation branch not audited; no accuracy/coverage metric established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> verdict.reason_code(),
> verdict.confidence_basis_points(),
> route,
> evidence_ids,
> counterevidence_ids,
> --- `crates/wenlan-core/src/lint/semantic.rs`

> recommendation_code: finding.then_some(LintRecommendationCode::ReviewFinding),
> evidence,
> duration_ms: context.clock().duration_ms(),
> },
> LintGateEffect::Advisory,
> --- `crates/wenlan-core/src/lint/semantic.rs`

#### EPI-RTE-repair-admission
Label: Manifest-bound repair apply

Prepare/planning builds immutable artifacts rather than mutating canonical data. Apply is a separate explicit operation bound to manifest ID/digest/approval string and current target receipt. The core obtains operation locks, refuses cancelled/mismatched manifests, loads rollback material and routes the declared writer through bounded effects/CAS machinery. Cooperating agent instruction/user approval is distinct from authenticated human provenance. Target is authorized mutation of exactly the prepared target, not general acceptance of the content as true. Writer-specific recovery is present but not fully audited; no universal rollback guarantee. No supplied counterpart declares this operation. SRC-1, `crates/wenlan-core/src/repair.rs`, `crates/wenlan-mcp/src/tools.rs`.

- Immediate return: apply receipt or refusal/error, not completed verification.
- Later read-back: manifest, rollback and apply/pending receipts persist; changed canonical state is later read by normal consumers and verification.
- Delegated visibility: apply receives exact prepared artifact/approval and current target state, not arbitrary ambient repair authority.
- Selection predicate: matching approved manifest digest, supported writer, uncancelled artifact, expected target/effect receipts and writer-specific checks.
- Invalidation or expiry: stale target/digest or cancellation can refuse; pending receipt and rollback support recovery with writer-specific limits.
- Activation or effect: enforcing authorization for a specific canonical mutation before a separate verification round.
- Evidence limits: all writer internals and approval parser not audited; external caller's genuine human intent not established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if manifest.manifest_digest() != request.approved_manifest_digest() {
>     return Err(WenlanError::Conflict(
>         "repair_approval_mismatch".to_string(),
>     ));
> }
> --- `crates/wenlan-core/src/repair.rs`

#### EPI-RTE-repair-verification
Label: Post-apply repair verification

After apply, verification consumes manifest, apply receipt and fresh General/applicable Deep reports. It checks report scope, stable snapshot, shared producer and required checks, invokes current-page checks and atomic verification, then publishes completion marker and clears pending apply state. Target is that repair's postconditions and permitted-state change, not global knowledge truth. Human/agent can request verification; code refuses mismatched/incomplete required evidence. Expected baseline/report criteria are an operation-specific reference, not a world-factual answer key. Distinct from both apply authorization and advisory lint. SRC-1, `crates/wenlan-core/src/repair.rs`.

- Immediate return: verification receipt, replayed valid receipt, or refusal/error.
- Later read-back: authenticated completion artifacts and reconciled review completion persist; pending apply linkage is cleared after completion publication.
- Delegated visibility: verifier receives reports and receipts, not all source truth or causal attribution evidence.
- Selection predicate: correct manifest/apply digests, expected effects/writer, current matching reports and writer-dependent postcondition verification.
- Invalidation or expiry: stale/mismatched reports refuse; pending artifact remains available for recovery/retry; completed replay checks its marker.
- Activation or effect: completion receipt/marker and review-state reconciliation; failure does not itself establish rollback of the already applied mutation.
- Evidence limits: atomic helper and every writer-specific postcondition not fully audited; no experimental recovery claim and no inferred improvement/transfer.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> validate_verification_reports(&manifest, request.general_report(), request.deep_report())?;
> --- `crates/wenlan-core/src/repair.rs`

> store.publish_review_completion_marker(&manifest, &receipt)?;
> store.clear_pending_apply_receipt(manifest.manifest_id())?;
> Ok(receipt)
> --- `crates/wenlan-core/src/repair.rs`

#### EPI-RTE-retrieval-eval
Label: Seeded retrieval evaluation

A lab runner seeds an ephemeral database, retrieves ranked IDs and compares them with fixture relevance grades (relevance at least two for the binary relevant set), computing ranking metrics and empty-set similarity diagnostics. This supplies an actual reference outcome in the bounded lab mode, unlike production capture or synthesis. Test fixtures provide that reference; reference correctness/domain representativeness is not independently established. Documentation separates retrieval snapshots from end-to-end answer quality/private caches. Distinct from production recall: its scored results are evaluation output, with no inspected automatic runtime policy-update consumer. SRC-1, `crates/wenlan-core/src/eval/runner.rs`, `docs/eval/README.md`.

- Immediate return: per-case and aggregate metrics/results to evaluation caller.
- Later read-back: uninspected — runner output/report persistence and every benchmark publishing consumer not fully traced; no production adaptation claimed.
- Delegated visibility: rank/grade scorer sees returned IDs and fixture labels; model dependencies are inference, not fitted in this path.
- Selection predicate: fixture queries, seeds, scope and configured retrieval parameters.
- Invalidation or expiry: inapplicable — bounded evaluation result describes its configuration/run; it is not an evergreen production acceptance grant.
- Activation or effect: produces retrieval-quality evidence in lab; no automatic knowledge acceptance or policy installation traced.
- Evidence limits: no evaluation executed, no causal comparison; private answer-quality cache unavailable and M5 accuracy benchmark not reconstructed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> .filter(|s| s.relevance >= 2)
> .map(|s| s.id.as_str())
> .collect();
> --- `crates/wenlan-core/src/eval/runner.rs`

### Claims

#### EPI-CLM-notes-change
Label: Experience improves notes

SRC-1, `README.md`, doctrine/design claims that new experience improves notes while preserving earlier decisions and presents a worked illustrative rule replacement. This is broader than retaining a revision, but the source explicitly bounds illustrations rather than reporting customer/model-test results. Closest supplied [RT-CLM-ambient-ownership](runtime.md#rt-clm-ambient-ownership) concerns work ownership, not improvement; these are distinct claims.

> New experience improves your notes without hiding earlier decisions. This example replaces “tests passed, so the UI is done” with “check tests and the desktop and mobile views,” keeping the reason and evidence for the change.
> --- `README.md`

> The illustration shows a reusable working rule, not customer results or an automated page-generation test.
> --- `README.md`

#### EPI-CLM-reviewed-repair
Label: Reviewed health repairs

SRC-1, `README.md`, doctrine/design separates read-only diagnostics from explicit supported repairs and later verification. Distinct from the supplied scheduler ownership claim; implemented details are the three repair/lint records above, not proof every possible issue is fixable.

> **Health checks and reviewed repairs:** [Doctor](https://wenlan.app/docs/diagnostics-and-issue-reports) and [lint](plugin/skills/lint/SKILL.md) report problems without rewriting knowledge. For supported findings, the app lets you preview and explicitly apply a repair, then verify it.
> --- `README.md`

#### EPI-CLM-entailment-judge
Label: M5 direct-entailment contract

SRC-1, `crates/wenlan-core/src/claim_judge.rs`, doctrine/design prompt requests direct evidential entailment and semantic distinctions rather than lexical overlap. Implementation validates response shape/identity/range; that is support for delivering and consuming this request, not evidence the model reliably fulfills it. No supplied counterpart declares this M5 claim; unlike the supplied synthesis route, this is a later evaluator contract.

> For each input item, score whether its evidence directly entails its claim.
> --- `crates/wenlan-core/src/claim_judge.rs`

> Account for negation, modality, quantifiers, scope, and dates, and do not infer facts beyond the evidence.
> --- `crates/wenlan-core/src/claim_judge.rs`
