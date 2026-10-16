---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Sage-wiki truth-apt production, graph evidence checks and output reliance at its frozen revision."
run-id: AAS-2026-10-15-sage-wiki-cc43456fb833-01
reviewed-boundary: d3ef3a1346405c82eac01b4d7c493c94c1c59169
---

# Sage-wiki epistemic report

## Source-and-claim boundary

The question is how Sage-wiki acquires or produces assertions, checks them, and authorizes their later use. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identity is see [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not observed operation or causal experiments. The inspected target is the whole shipped knowledge-state loop; this report is selective, not an exhaustive audit of every adapter. No target execution was performed.

Claims are see [EPI-CLM-graph-grounding](#epi-clm-graph-grounding), [EPI-CLM-output-quarantine](#epi-clm-output-quarantine), [EPI-CLM-edge-contradictions](#epi-clm-edge-contradictions), and [RT-CLM-review-order](runtime.md#rt-clm-review-order). The following additional direct reads use the boundary's existing SRC-1, not new evidence identities. Supplied runtime findings remain provisional; direct reads exposed graph-local/global answering and standalone verification/cleanup not separately traced there. These additions qualify completeness, not the identity of its valid container records.

| Entry point or operation | Source path in SRC-1 | Coverage and evidence basis | Remaining limit |
|---|---|---|---|
| CLI capture, compile, query; embedded/REST/UI alternatives | `cmd/sage-wiki/main.go`, `pkg/engine/methods.go`, `internal/query/query.go` | Supplied [RT-RTE-capture-source](runtime.md#rt-rte-capture-source), [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources), [RT-RTE-query-answer](runtime.md#rt-rte-query-answer) | No invocation trace; cannot establish exercise or benefit |
| MCP dispatch including direct ontology/write/learn and graph query | `internal/mcp/server.go`, `internal/mcp/tools_graph.go` | Direct dispatch/graph-handler reads; supplied [RT-RTE-write-article](runtime.md#rt-rte-write-article); new [EPI-RTE-graph-answer](#epi-rte-graph-answer), [EPI-RTE-global-answer](#epi-rte-global-answer) | Detailed add-ontology handler uninspected; prevents complete enumeration of graph admissions |
| Capture extraction and session scribe | `internal/prompts/templates/capture_knowledge.txt`, `internal/scribe/session.go` | Direct capture guidance; supplied [RT-RTE-capture-knowledge](runtime.md#rt-rte-capture-knowledge), [RT-RTE-scribe-session](runtime.md#rt-rte-scribe-session) | No trace linking candidate prose to extraction and later use |
| Article evidence gate, cleanup, quality and rewrite | `internal/compiler/evidence_gate.go`, `internal/compiler/write.go`, `internal/compiler/confidence.go`, `internal/compiler/fullpipeline.go` | Direct relevant functions; [EPI-RTE-source-count](#epi-rte-source-count), [EPI-RTE-article-cleanup](#epi-rte-article-cleanup), [EPI-RTE-quality-score](#epi-rte-quality-score), [EPI-RTE-quality-rewrite](#epi-rte-quality-rewrite) | Batch-specific realization, dedup, curation and entity-resolution algorithms not fully inspected; prevents uniform equivalence/semantic-preservation conclusions |
| Optional triples and temporal supersession | `internal/compiler/extract_triples.go` | Direct extraction-to-persistence, span and functional-conflict branches; [EPI-RTE-span-check](#epi-rte-span-check), [EPI-RTE-edge-supersession](#epi-rte-edge-supersession) | Backend temporal implementation and post-resolution sweep not independently audited |
| Output hooks, verify, resolve, clean, source withdrawal | `internal/trust/hooks.go`, `internal/trust/consensus.go`, `internal/trust/grounding.go`, `internal/trust/verify.go`, `internal/trust/source_check.go`, `internal/trust/predicate.go`, `cmd/sage-wiki/trust_cmd.go` | Direct reads; [EPI-RTE-answer-agreement](#epi-rte-answer-agreement), [EPI-RTE-grounding-check](#epi-rte-grounding-check), [EPI-RTE-verify-promote](#epi-rte-verify-promote), [EPI-RTE-output-withdrawal](#epi-rte-output-withdrawal) plus supplied [RT-RTE-admit-output](runtime.md#rt-rte-admit-output) | Store/backend and all index failures not audited; no transactional publication or semantic truth guarantee |
| Community retention and global answer | `internal/compiler/communities.go`, `internal/query/globalqa.go` | Direct detection/summary/cache and full global-answer source; [EPI-RTE-community-summary](#epi-rte-community-summary), [EPI-RTE-global-answer](#epi-rte-global-answer) | Detection algorithm and cache backend internals not inspected; prevents claims that every relation/evidence change invalidates cached prose |
| Lint and learning guidance | `internal/linter/runner.go`, `internal/linter/passes.go`, `internal/prompts/prompts.go` | Direct runner and style check/fix, targeted learning-consumer search; [EPI-RTE-style-check](#epi-rte-style-check), [EPI-RTE-style-fix](#epi-rte-style-fix) | Other lint pass bodies and full learning consumers uninspected; template field alone does not prove active feedback into compilation |
| Search/read, federation, packs, parser and restore | `internal/mcp/server.go`, `internal/hub/search.go`, `internal/pack/merge.go`, `internal/extract/external.go`, `internal/mirror/hydrate.go` | Direct dispatch/predicate plus supplied runtime records | Deeper backend/remote/adapter internals uninspected; excludes system-complete semantic or recovery verdict |
| LOCOMO evaluator | `eval/benchmarks/locomo/run.py` | Direct answer/judge consumer code; [EPI-RTE-benchmark-judge](#epi-rte-benchmark-judge) | Other benchmark drivers/results and judge-prompt bodies unassessed; no score or causal benefit inferred |

External providers' parameters, remote services and real host compliance are outside accessible SRC-1 internals. See [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client) and [RT-CMP-embedder](runtime.md#rt-cmp-embedder): inference interfaces and mutable model labels do not establish training, fixed weights or changing weights. Missing execution traces prevent observed acceptance, activation, learning improvement and self-improvement attribution. Missing concrete input/output pairs prevent deciding entailment or non-entailment for most model-produced prose; that uncertainty is not an architectural absence.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source and anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-source-text](#epi-obj-source-text) | See record | Source evidence | SRC-1: `internal/prompts/templates/capture_knowledge.txt` | Origin warrant unknown; model extraction is distinct from raw import |
| [EPI-OBJ-article-text](#epi-obj-article-text) | See record | Compiled knowledge | SRC-1: `internal/compiler/write.go` | Source labels and self-confidence are not checked source truth |
| [EPI-OBJ-output-text](#epi-obj-output-text) | See record | Reusable answers | SRC-1: `internal/trust/hooks.go` | Returned answers precede admission to later retrieval |
| [EPI-OBJ-relation-text](#epi-obj-relation-text) | See record | Relation evidence | SRC-1: `internal/compiler/extract_triples.go` | Span occurrence in summary does not prove relation entailment |
| [EPI-OBJ-relation-state](#epi-obj-relation-state) | See record | Structured graph and temporal selection | SRC-1: `internal/query/graphqa.go` | Confidence is a model-supplied number, not calibrated probability |
| [EPI-OBJ-community-text](#epi-obj-community-text) | See record | Global themes | SRC-1: `internal/compiler/communities.go` | Further summary layer; acceptance not implied by caching |
| [RT-OBJ-compile-items](runtime.md#rt-obj-compile-items) | None individually: scheduling/score state | Compile decisions | SRC-1: `internal/compiler/fullpipeline.go` | Quality score is a proxy, not the propositions scored |
| [RT-OBJ-prompts](runtime.md#rt-obj-prompts), [RT-OBJ-config](runtime.md#rt-obj-config) | Policy guidance and selectors; truth-apt contents not determinable generically | Proposal and admission control | SRC-1: `internal/prompts/prompts.go` | Static instructions/config are not evidence-responsive learning by themselves |
| [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client), [RT-CMP-embedder](runtime.md#rt-cmp-embedder) | Provider-held content not determinable | Proposal, similarity and judgment | SRC-1: `internal/llm/client.go` | Accessible interface cannot individuate provider knowledge/warrant |

## Authority-route ledger

All implemented entries describe code capacity, not observed operation. Generic route fields are see the cited declaring record; this overlay supplies the architectural classification and bounded license. Checking and disposition, and retention and post-acceptance integration, remain separate entries even where they share a container.

Route ID: [RT-RTE-capture-source](runtime.md#rt-rte-capture-source)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [RT-RTE-capture-source](runtime.md#rt-rte-capture-source).
Content/update relation: truth-apt transformation: acquisition/import.
Transition or check target: Caller source text; structural import conditions.
Evaluator/condition and domain: see [RT-RTE-capture-source](runtime.md#rt-rte-capture-source); domain bounded by the target above.
Activation and timing: see [RT-RTE-capture-source](runtime.md#rt-rte-capture-source); operation unobserved.
Possible or observed result: Raw source persistence; enforcing shape gates; possible implementation result, not observed.
Implemented force: see [RT-RTE-capture-source](runtime.md#rt-rte-capture-source).
Epistemic authority and scope: Source warrant unknown; no semantic endorsement.
Operational authority: Compiler source input; persistent until change.
Behavioral-authority path: see [RT-RTE-capture-source](runtime.md#rt-rte-capture-source); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [RT-RTE-capture-source](runtime.md#rt-rte-capture-source) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Path/URL conversions only supplied tracing.
Gap/limit: see [RT-RTE-capture-source](runtime.md#rt-rte-capture-source); no supplied execution or causal evidence.

Route ID: [RT-RTE-capture-knowledge](runtime.md#rt-rte-capture-knowledge)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [RT-RTE-capture-knowledge](runtime.md#rt-rte-capture-knowledge).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: Model extraction from caller prose.
Evaluator/condition and domain: see [RT-RTE-capture-knowledge](runtime.md#rt-rte-capture-knowledge); domain bounded by the target above.
Activation and timing: see [RT-RTE-capture-knowledge](runtime.md#rt-rte-capture-knowledge); operation unobserved.
Possible or observed result: Candidate items or raw fallback; structural admission; possible implementation result, not observed.
Implemented force: see [RT-RTE-capture-knowledge](runtime.md#rt-rte-capture-knowledge).
Epistemic authority and scope: Remaining alternatives: faithful compression, derivation, or new conjecture; needs paired content.
Operational authority: Raw captures become later compile input.
Behavioral-authority path: see [RT-RTE-capture-knowledge](runtime.md#rt-rte-capture-knowledge); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [RT-RTE-capture-knowledge](runtime.md#rt-rte-capture-knowledge) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Guidance/JSON form does not check extracted truth.
Gap/limit: see [RT-RTE-capture-knowledge](runtime.md#rt-rte-capture-knowledge); no supplied execution or causal evidence.

Route ID: [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: Summaries, concepts and articles; independent model passes.
Evaluator/condition and domain: see [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources); domain bounded by the target above.
Activation and timing: see [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources); operation unobserved.
Possible or observed result: Compiled candidate prose and graph material; possible implementation result, not observed.
Implemented force: see [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources).
Epistemic authority and scope: Remaining alternatives: reshaping, derivation, or conjecture; no checked entailment for generic prose.
Operational authority: Later article retrieval/synthesis; persistent.
Behavioral-authority path: see [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Warrant of premises and interpretation unestablished.
Gap/limit: see [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources); no supplied execution or causal evidence.

Route ID: [EPI-RTE-source-count](#epi-rte-source-count)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-source-count](#epi-rte-source-count).
Content/update relation: no content change.
Transition or check target: Declared concept source-list cardinality.
Evaluator/condition and domain: see [EPI-RTE-source-count](#epi-rte-source-count); domain bounded by the target above.
Activation and timing: see [EPI-RTE-source-count](#epi-rte-source-count); operation unobserved.
Possible or observed result: Keep/skip partition; enforcing selection input; possible implementation result, not observed.
Implemented force: see [EPI-RTE-source-count](#epi-rte-source-count).
Epistemic authority and scope: Count criterion only; neither independent evidence nor factual support.
Operational authority: Next manifest/article admission; compile pass.
Behavioral-authority path: see [EPI-RTE-source-count](#epi-rte-source-count); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [EPI-RTE-source-count](#epi-rte-source-count) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Gate can be disabled.
Gap/limit: see [EPI-RTE-source-count](#epi-rte-source-count); no supplied execution or causal evidence.

Route ID: [EPI-RTE-source-count](#epi-rte-source-count)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-source-count](#epi-rte-source-count).
Content/update relation: no content change.
Transition or check target: Concept article eligibility.
Evaluator/condition and domain: see [EPI-RTE-source-count](#epi-rte-source-count); domain bounded by the target above.
Activation and timing: see [EPI-RTE-source-count](#epi-rte-source-count); operation unobserved.
Possible or observed result: Skipped concepts withheld; retained concepts continue; possible implementation result, not observed.
Implemented force: see [EPI-RTE-source-count](#epi-rte-source-count).
Epistemic authority and scope: Operational eligibility, not acceptance of each claim.
Operational authority: Compile writes; current pass and later retained articles.
Behavioral-authority path: see [EPI-RTE-source-count](#epi-rte-source-count); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [EPI-RTE-source-count](#epi-rte-source-count) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Declared count alone supplies no substantive warrant.
Gap/limit: see [EPI-RTE-source-count](#epi-rte-source-count); no supplied execution or causal evidence.

Route ID: [EPI-RTE-article-cleanup](#epi-rte-article-cleanup)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-article-cleanup](#epi-rte-article-cleanup).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: Article body sentence deletion/link rewrite.
Evaluator/condition and domain: see [EPI-RTE-article-cleanup](#epi-rte-article-cleanup); domain bounded by the target above.
Activation and timing: see [EPI-RTE-article-cleanup](#epi-rte-article-cleanup); operation unobserved.
Possible or observed result: Rewritten persisted body; enforcing; possible implementation result, not observed.
Implemented force: see [EPI-RTE-article-cleanup](#epi-rte-article-cleanup).
Epistemic authority and scope: Deletion may alter conditions/meaning; cannot assume mere reshaping.
Operational authority: Write/index pipeline; later article consumers.
Behavioral-authority path: see [EPI-RTE-article-cleanup](#epi-rte-article-cleanup); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [EPI-RTE-article-cleanup](#epi-rte-article-cleanup) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Concrete witness in record; semantics need content-specific review.
Gap/limit: see [EPI-RTE-article-cleanup](#epi-rte-article-cleanup); no supplied execution or causal evidence.

Route ID: [EPI-RTE-quality-score](#epi-rte-quality-score)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-quality-score](#epi-rte-quality-score).
Content/update relation: no content change.
Transition or check target: Article format, lexical overlap, length, links, filler.
Evaluator/condition and domain: see [EPI-RTE-quality-score](#epi-rte-quality-score); domain bounded by the target above.
Activation and timing: see [EPI-RTE-quality-score](#epi-rte-quality-score); operation unobserved.
Possible or observed result: Weighted score; ranking/retry input; possible implementation result, not observed.
Implemented force: see [EPI-RTE-quality-score](#epi-rte-quality-score).
Epistemic authority and scope: Proxy domain only; grounding here means phrase presence.
Operational authority: Quality-rewrite branch and persisted queue score.
Behavioral-authority path: see [EPI-RTE-quality-score](#epi-rte-quality-score); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [EPI-RTE-quality-score](#epi-rte-quality-score) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: No semantic source-entailment test.
Gap/limit: see [EPI-RTE-quality-score](#epi-rte-quality-score); no supplied execution or causal evidence.

Route ID: [EPI-RTE-quality-rewrite](#epi-rte-quality-rewrite)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-quality-rewrite](#epi-rte-quality-rewrite).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: Below-threshold article.
Evaluator/condition and domain: see [EPI-RTE-quality-rewrite](#epi-rte-quality-rewrite); domain bounded by the target above.
Activation and timing: see [EPI-RTE-quality-rewrite](#epi-rte-quality-rewrite); operation unobserved.
Possible or observed result: One fresh write; may still ship low score; possible implementation result, not observed.
Implemented force: see [EPI-RTE-quality-rewrite](#epi-rte-quality-rewrite).
Epistemic authority and scope: Retry is improvement-directed, not accepted knowledge or reliable improvement.
Operational authority: Compiler calls writer again; one pass, later files.
Behavioral-authority path: see [EPI-RTE-quality-rewrite](#epi-rte-quality-rewrite); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [EPI-RTE-quality-rewrite](#epi-rte-quality-rewrite) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: No content-directed criticism supplied to writer.
Gap/limit: see [EPI-RTE-quality-rewrite](#epi-rte-quality-rewrite); no supplied execution or causal evidence.

Route ID: [EPI-RTE-span-check](#epi-rte-span-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-span-check](#epi-rte-span-check).
Content/update relation: no content change.
Transition or check target: Extracted relation evidence versus compiled summary.
Evaluator/condition and domain: see [EPI-RTE-span-check](#epi-rte-span-check); domain bounded by the target above.
Activation and timing: see [EPI-RTE-span-check](#epi-rte-span-check); operation unobserved.
Possible or observed result: Normalized substring match; possible implementation result, not observed.
Implemented force: see [EPI-RTE-span-check](#epi-rte-span-check).
Epistemic authority and scope: Occurrence in summary only; not original source truth/edge entailment.
Operational authority: Triple persistence filter; same compile.
Behavioral-authority path: see [EPI-RTE-span-check](#epi-rte-span-check); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [EPI-RTE-span-check](#epi-rte-span-check) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Entities survive failed edge checks.
Gap/limit: see [EPI-RTE-span-check](#epi-rte-span-check); no supplied execution or causal evidence.

Route ID: [EPI-RTE-span-check](#epi-rte-span-check)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-span-check](#epi-rte-span-check).
Content/update relation: no content change.
Transition or check target: Edges with nonempty occurring evidence.
Evaluator/condition and domain: see [EPI-RTE-span-check](#epi-rte-span-check); domain bounded by the target above.
Activation and timing: see [EPI-RTE-span-check](#epi-rte-span-check); operation unobserved.
Possible or observed result: Missing-span edges removed; enforcing; possible implementation result, not observed.
Implemented force: see [EPI-RTE-span-check](#epi-rte-span-check).
Epistemic authority and scope: Acceptance for quote-occurrence criterion, not relation truth.
Operational authority: persistGraph; later graph/QA consumers.
Behavioral-authority path: see [EPI-RTE-span-check](#epi-rte-span-check); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [EPI-RTE-span-check](#epi-rte-span-check) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: SourceDoc names original document while check reads summary.
Gap/limit: see [EPI-RTE-span-check](#epi-rte-span-check); no supplied execution or causal evidence.

Route ID: [EPI-RTE-edge-supersession](#epi-rte-edge-supersession)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-edge-supersession](#epi-rte-edge-supersession).
Content/update relation: no content change.
Transition or check target: Functional predicate conflict and model confidence.
Evaluator/condition and domain: see [EPI-RTE-edge-supersession](#epi-rte-edge-supersession); domain bounded by the target above.
Activation and timing: see [EPI-RTE-edge-supersession](#epi-rte-edge-supersession); operation unobserved.
Possible or observed result: Old edge invalidation or deferred conflict; possible implementation result, not observed.
Implemented force: see [EPI-RTE-edge-supersession](#epi-rte-edge-supersession).
Epistemic authority and scope: Configured functional-policy reliance only.
Operational authority: Ontology temporal consumers; future queries/as_of.
Behavioral-authority path: see [EPI-RTE-edge-supersession](#epi-rte-edge-supersession); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [EPI-RTE-edge-supersession](#epi-rte-edge-supersession) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Nonfunctional or low-confidence conflicts remain live.
Gap/limit: see [EPI-RTE-edge-supersession](#epi-rte-edge-supersession); no supplied execution or causal evidence.

Route ID: [EPI-RTE-graph-answer](#epi-rte-graph-answer)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-graph-answer](#epi-rte-graph-answer).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: Question plus bounded live subgraph.
Evaluator/condition and domain: see [EPI-RTE-graph-answer](#epi-rte-graph-answer); domain bounded by the target above.
Activation and timing: see [EPI-RTE-graph-answer](#epi-rte-graph-answer); operation unobserved.
Possible or observed result: Model answer and retained edge metadata; possible implementation result, not observed.
Implemented force: see [EPI-RTE-graph-answer](#epi-rte-graph-answer).
Epistemic authority and scope: Entailment/conjecture undecided; prompt is not checker.
Operational authority: MCP caller; current response.
Behavioral-authority path: see [EPI-RTE-graph-answer](#epi-rte-graph-answer); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [EPI-RTE-graph-answer](#epi-rte-graph-answer) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Invalid citations dropped without rejecting answer.
Gap/limit: see [EPI-RTE-graph-answer](#epi-rte-graph-answer); no supplied execution or causal evidence.

Route ID: [EPI-RTE-graph-answer](#epi-rte-graph-answer)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-graph-answer](#epi-rte-graph-answer).
Content/update relation: no content change.
Transition or check target: Citation integers versus supplied edge count.
Evaluator/condition and domain: see [EPI-RTE-graph-answer](#epi-rte-graph-answer); domain bounded by the target above.
Activation and timing: see [EPI-RTE-graph-answer](#epi-rte-graph-answer); operation unobserved.
Possible or observed result: Range/dedup filtering; enforcing metadata; possible implementation result, not observed.
Implemented force: see [EPI-RTE-graph-answer](#epi-rte-graph-answer).
Epistemic authority and scope: Citation points at an available edge; not claim support.
Operational authority: CitedEdge response; current response.
Behavioral-authority path: see [EPI-RTE-graph-answer](#epi-rte-graph-answer); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [EPI-RTE-graph-answer](#epi-rte-graph-answer) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Cannot warrant ONLY-edge answer claim.
Gap/limit: see [EPI-RTE-graph-answer](#epi-rte-graph-answer); no supplied execution or causal evidence.

Route ID: [EPI-RTE-community-summary](#epi-rte-community-summary)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-community-summary](#epi-rte-community-summary).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: Up to forty intra-community live relations.
Evaluator/condition and domain: see [EPI-RTE-community-summary](#epi-rte-community-summary); domain bounded by the target above.
Activation and timing: see [EPI-RTE-community-summary](#epi-rte-community-summary); operation unobserved.
Possible or observed result: Model theme prose; possible implementation result, not observed.
Implemented force: see [EPI-RTE-community-summary](#epi-rte-community-summary).
Epistemic authority and scope: Remaining alternatives: compression, derivation, conjecture.
Operational authority: Community store/files/index; later GlobalQA.
Behavioral-authority path: see [EPI-RTE-community-summary](#epi-rte-community-summary); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [EPI-RTE-community-summary](#epi-rte-community-summary) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Evidence text truncation and selection limit lineage.
Gap/limit: see [EPI-RTE-community-summary](#epi-rte-community-summary); no supplied execution or causal evidence.

Route ID: [EPI-RTE-community-summary](#epi-rte-community-summary)
Route function: retention
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-community-summary](#epi-rte-community-summary).
Content/update relation: no content change.
Transition or check target: Nonempty summary/cache selectors.
Evaluator/condition and domain: see [EPI-RTE-community-summary](#epi-rte-community-summary); domain bounded by the target above.
Activation and timing: see [EPI-RTE-community-summary](#epi-rte-community-summary); operation unobserved.
Possible or observed result: Stored summary/model/member hash; possible implementation result, not observed.
Implemented force: see [EPI-RTE-community-summary](#epi-rte-community-summary).
Epistemic authority and scope: Retention before semantic acceptance.
Operational authority: GlobalQA map calls and search; later invocations.
Behavioral-authority path: see [EPI-RTE-community-summary](#epi-rte-community-summary); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [EPI-RTE-community-summary](#epi-rte-community-summary) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: No lifecycle integration after established epistemic acceptance inferred.
Gap/limit: see [EPI-RTE-community-summary](#epi-rte-community-summary); no supplied execution or causal evidence.

Route ID: [EPI-RTE-global-answer](#epi-rte-global-answer)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-global-answer](#epi-rte-global-answer).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: Community summaries → partials → reduction.
Evaluator/condition and domain: see [EPI-RTE-global-answer](#epi-rte-global-answer); domain bounded by the target above.
Activation and timing: see [EPI-RTE-global-answer](#epi-rte-global-answer); operation unobserved.
Possible or observed result: Global answer/community citations; possible implementation result, not observed.
Implemented force: see [EPI-RTE-global-answer](#epi-rte-global-answer).
Epistemic authority and scope: Remaining alternatives: reshaping, inference, conjecture.
Operational authority: MCP caller; current response.
Behavioral-authority path: see [EPI-RTE-global-answer](#epi-rte-global-answer); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [EPI-RTE-global-answer](#epi-rte-global-answer) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Cited list is relevant partial origins, not checked per-fact support.
Gap/limit: see [EPI-RTE-global-answer](#epi-rte-global-answer); no supplied execution or causal evidence.

Route ID: [RT-RTE-query-answer](runtime.md#rt-rte-query-answer)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [RT-RTE-query-answer](runtime.md#rt-rte-query-answer).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: Selected article prefixes and question.
Evaluator/condition and domain: see [RT-RTE-query-answer](runtime.md#rt-rte-query-answer); domain bounded by the target above.
Activation and timing: see [RT-RTE-query-answer](runtime.md#rt-rte-query-answer); operation unobserved.
Possible or observed result: Returned answer then attempted filing; possible implementation result, not observed.
Implemented force: see [RT-RTE-query-answer](runtime.md#rt-rte-query-answer).
Epistemic authority and scope: No native reference-answer oracle; unknown source warrant.
Operational authority: User/model gets answer immediately; output filing later.
Behavioral-authority path: see [RT-RTE-query-answer](runtime.md#rt-rte-query-answer); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [RT-RTE-query-answer](runtime.md#rt-rte-query-answer) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Citation guidance cannot establish entailment.
Gap/limit: see [RT-RTE-query-answer](runtime.md#rt-rte-query-answer); no supplied execution or causal evidence.

Route ID: [RT-RTE-admit-output](runtime.md#rt-rte-admit-output)
Route function: retention
Architectural status: implemented
Object/candidate ID: see [RT-RTE-admit-output](runtime.md#rt-rte-admit-output).
Content/update relation: no content change.
Transition or check target: Generated or externally supplied answer.
Evaluator/condition and domain: see [RT-RTE-admit-output](runtime.md#rt-rte-admit-output); domain bounded by the target above.
Activation and timing: see [RT-RTE-admit-output](runtime.md#rt-rte-admit-output); operation unobserved.
Possible or observed result: Pending/conflict storage or unrestricted index; possible implementation result, not observed.
Implemented force: see [RT-RTE-admit-output](runtime.md#rt-rte-admit-output).
Epistemic authority and scope: Retention/use before acceptance kept separate.
Operational authority: Future comparison or allowed retrieval; persistent.
Behavioral-authority path: see [RT-RTE-admit-output](runtime.md#rt-rte-admit-output); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [RT-RTE-admit-output](runtime.md#rt-rte-admit-output) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: SaveAnswer and unrestricted paths bypass synthesis/review.
Gap/limit: see [RT-RTE-admit-output](runtime.md#rt-rte-admit-output); no supplied execution or causal evidence.

Route ID: [EPI-RTE-answer-agreement](#epi-rte-answer-agreement)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-answer-agreement](#epi-rte-answer-agreement).
Content/update relation: no content change.
Transition or check target: Similar question and answer-pair sameness.
Evaluator/condition and domain: see [EPI-RTE-answer-agreement](#epi-rte-answer-agreement); domain bounded by the target above.
Activation and timing: see [EPI-RTE-answer-agreement](#epi-rte-answer-agreement); operation unobserved.
Possible or observed result: Embedding/model agreement and chunk-set distance; possible implementation result, not observed.
Implemented force: see [EPI-RTE-answer-agreement](#epi-rte-answer-agreement).
Epistemic authority and scope: Similarity/consensus evidence, not independent truth.
Operational authority: processMatch confirmations/conflict decision; future attempts.
Behavioral-authority path: see [EPI-RTE-answer-agreement](#epi-rte-answer-agreement); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [EPI-RTE-answer-agreement](#epi-rte-answer-agreement) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Different chunk IDs do not establish independent sources.
Gap/limit: see [EPI-RTE-answer-agreement](#epi-rte-answer-agreement); no supplied execution or causal evidence.

Route ID: [EPI-RTE-grounding-check](#epi-rte-grounding-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-grounding-check](#epi-rte-grounding-check).
Content/update relation: no content change.
Transition or check target: Model-extracted claims versus concatenated current source files.
Evaluator/condition and domain: see [EPI-RTE-grounding-check](#epi-rte-grounding-check); domain bounded by the target above.
Activation and timing: see [EPI-RTE-grounding-check](#epi-rte-grounding-check); operation unobserved.
Possible or observed result: Mean 1/0.5/0 score; stored; possible implementation result, not observed.
Implemented force: see [EPI-RTE-grounding-check](#epi-rte-grounding-check).
Epistemic authority and scope: Model judgment of passage support only; no source-truth test.
Operational authority: Verify promotion test; persisted score.
Behavioral-authority path: see [EPI-RTE-grounding-check](#epi-rte-grounding-check); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [EPI-RTE-grounding-check](#epi-rte-grounding-check) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Unreadable files skipped; no-claims yields 1.
Gap/limit: see [EPI-RTE-grounding-check](#epi-rte-grounding-check); no supplied execution or causal evidence.

Route ID: [EPI-RTE-verify-promote](#epi-rte-verify-promote)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-verify-promote](#epi-rte-verify-promote).
Content/update relation: no content change.
Transition or check target: Pending output score and confirmations.
Evaluator/condition and domain: see [EPI-RTE-verify-promote](#epi-rte-verify-promote); domain bounded by the target above.
Activation and timing: see [EPI-RTE-verify-promote](#epi-rte-verify-promote); operation unobserved.
Possible or observed result: Configured auto-promotion; enforcing state/index eligibility; possible implementation result, not observed.
Implemented force: see [EPI-RTE-verify-promote](#epi-rte-verify-promote).
Epistemic authority and scope: Evidence-consuming acceptance for answer reuse under configured proxy criteria.
Operational authority: PromoteOutput and verified-mode retrieval; subsequent invocations.
Behavioral-authority path: see [EPI-RTE-verify-promote](#epi-rte-verify-promote); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [EPI-RTE-verify-promote](#epi-rte-verify-promote) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: No infallibility; manual promotion has a separate criterion.
Gap/limit: see [EPI-RTE-verify-promote](#epi-rte-verify-promote); no supplied execution or causal evidence.

Route ID: [RT-RTE-admit-output](runtime.md#rt-rte-admit-output)
Route function: lifecycle integration
Architectural status: implemented
Object/candidate ID: see [RT-RTE-admit-output](runtime.md#rt-rte-admit-output).
Content/update relation: no content change.
Transition or check target: Policy-accepted answer.
Evaluator/condition and domain: see [RT-RTE-admit-output](runtime.md#rt-rte-admit-output); domain bounded by the target above.
Activation and timing: see [RT-RTE-admit-output](runtime.md#rt-rte-admit-output); operation unobserved.
Possible or observed result: Move/index/ontology links through promotion; possible implementation result, not observed.
Implemented force: see [RT-RTE-admit-output](runtime.md#rt-rte-admit-output).
Epistemic authority and scope: Organization for later use only after scoped acceptance.
Operational authority: Search/context predicate; later answers.
Behavioral-authority path: see [RT-RTE-admit-output](runtime.md#rt-rte-admit-output); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [RT-RTE-admit-output](runtime.md#rt-rte-admit-output) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Not all admissions are evidence-consuming acceptance; ordering exception.
Gap/limit: see [RT-RTE-admit-output](runtime.md#rt-rte-admit-output); no supplied execution or causal evidence.

Route ID: [EPI-RTE-output-withdrawal](#epi-rte-output-withdrawal)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-output-withdrawal](#epi-rte-output-withdrawal).
Content/update relation: no content change.
Transition or check target: Source hash changes or explicit resolve/reject/age cleanup.
Evaluator/condition and domain: see [EPI-RTE-output-withdrawal](#epi-rte-output-withdrawal); domain bounded by the target above.
Activation and timing: see [EPI-RTE-output-withdrawal](#epi-rte-output-withdrawal); operation unobserved.
Possible or observed result: Deindex/demote/reject; enforcing later eligibility; possible implementation result, not observed.
Implemented force: see [EPI-RTE-output-withdrawal](#epi-rte-output-withdrawal).
Epistemic authority and scope: Changed bytes/selected winner/age are not proof of falsehood.
Operational authority: Trust stores and retrieval indexes; future calls.
Behavioral-authority path: see [EPI-RTE-output-withdrawal](#epi-rte-output-withdrawal); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [EPI-RTE-output-withdrawal](#epi-rte-output-withdrawal) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Does not retract delivered answers; clean ignores rejection error.
Gap/limit: see [EPI-RTE-output-withdrawal](#epi-rte-output-withdrawal); no supplied execution or causal evidence.

Route ID: [RT-RTE-write-article](runtime.md#rt-rte-write-article)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: see [RT-RTE-write-article](runtime.md#rt-rte-write-article).
Content/update relation: truth-apt transformation: acquisition/import.
Transition or check target: Caller-authored articles/learning.
Evaluator/condition and domain: see [RT-RTE-write-article](runtime.md#rt-rte-write-article); domain bounded by the target above.
Activation and timing: see [RT-RTE-write-article](runtime.md#rt-rte-write-article); operation unobserved.
Possible or observed result: File/store/index; structural veto; possible implementation result, not observed.
Implemented force: see [RT-RTE-write-article](runtime.md#rt-rte-write-article).
Epistemic authority and scope: External content acquired; source warrant unknown.
Operational authority: Later searches/read or configured consumers.
Behavioral-authority path: see [RT-RTE-write-article](runtime.md#rt-rte-write-article); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [RT-RTE-write-article](runtime.md#rt-rte-write-article) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: No human authorship/per-content review established.
Gap/limit: see [RT-RTE-write-article](runtime.md#rt-rte-write-article); no supplied execution or causal evidence.

Route ID: [RT-RTE-scribe-session](runtime.md#rt-rte-scribe-session)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [RT-RTE-scribe-session](runtime.md#rt-rte-scribe-session).
Content/update relation: truth-apt transformation: indeterminate.
Transition or check target: Filtered transcript → entity definitions.
Evaluator/condition and domain: see [RT-RTE-scribe-session](runtime.md#rt-rte-scribe-session); domain bounded by the target above.
Activation and timing: see [RT-RTE-scribe-session](runtime.md#rt-rte-scribe-session); operation unobserved.
Possible or observed result: Ontology add/update; possible implementation result, not observed.
Implemented force: see [RT-RTE-scribe-session](runtime.md#rt-rte-scribe-session).
Epistemic authority and scope: Remaining alternatives require actual transcript/candidate comparison.
Operational authority: Later ontology consumers; persistent.
Behavioral-authority path: see [RT-RTE-scribe-session](runtime.md#rt-rte-scribe-session); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [RT-RTE-scribe-session](runtime.md#rt-rte-scribe-session) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Definition difference is not correctness.
Gap/limit: see [RT-RTE-scribe-session](runtime.md#rt-rte-scribe-session); no supplied execution or causal evidence.

Route ID: [EPI-RTE-style-check](#epi-rte-style-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-style-check](#epi-rte-style-check).
Content/update relation: no content change.
Transition or check target: Article frontmatter/field presence.
Evaluator/condition and domain: see [EPI-RTE-style-check](#epi-rte-style-check); domain bounded by the target above.
Activation and timing: see [EPI-RTE-style-check](#epi-rte-style-check); operation unobserved.
Possible or observed result: Findings; advisory or fix trigger; possible implementation result, not observed.
Implemented force: see [EPI-RTE-style-check](#epi-rte-style-check).
Epistemic authority and scope: Syntactic presence, not truth/confidence calibration.
Operational authority: Runner fix branch and caller; one lint run.
Behavioral-authority path: see [EPI-RTE-style-check](#epi-rte-style-check); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [EPI-RTE-style-check](#epi-rte-style-check) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Other passes not inferred from this check.
Gap/limit: see [EPI-RTE-style-check](#epi-rte-style-check); no supplied execution or causal evidence.

Route ID: [EPI-RTE-style-fix](#epi-rte-style-fix)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-style-fix](#epi-rte-style-fix).
Content/update relation: non-truth-apt policy/content update: add conventional metadata.
Transition or check target: Missing frontmatter.
Evaluator/condition and domain: see [EPI-RTE-style-fix](#epi-rte-style-fix); domain bounded by the target above.
Activation and timing: see [EPI-RTE-style-fix](#epi-rte-style-fix); operation unobserved.
Possible or observed result: Prefix concept/confidence metadata; possible implementation result, not observed.
Implemented force: see [EPI-RTE-style-fix](#epi-rte-style-fix).
Epistemic authority and scope: Low confidence is code default, not judgment of article claims.
Operational authority: Persisted article; later file consumers.
Behavioral-authority path: see [EPI-RTE-style-fix](#epi-rte-style-fix); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [EPI-RTE-style-fix](#epi-rte-style-fix) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: No evidence-bearing acceptance.
Gap/limit: see [EPI-RTE-style-fix](#epi-rte-style-fix); no supplied execution or causal evidence.

Route ID: [EPI-RTE-benchmark-judge](#epi-rte-benchmark-judge)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-benchmark-judge](#epi-rte-benchmark-judge).
Content/update relation: no content change.
Transition or check target: External answerer result versus LOCOMO reference answer.
Evaluator/condition and domain: see [EPI-RTE-benchmark-judge](#epi-rte-benchmark-judge); domain bounded by the target above.
Activation and timing: see [EPI-RTE-benchmark-judge](#epi-rte-benchmark-judge); operation unobserved.
Possible or observed result: Binary judge label; score in benchmark record; possible implementation result, not observed.
Implemented force: see [EPI-RTE-benchmark-judge](#epi-rte-benchmark-judge).
Epistemic authority and scope: Dataset-answer agreement under judge protocol only.
Operational authority: Result/aggregation consumer; benchmark run.
Behavioral-authority path: see [EPI-RTE-benchmark-judge](#epi-rte-benchmark-judge); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [EPI-RTE-benchmark-judge](#epi-rte-benchmark-judge) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: No native answer attribution or independent causal component effect.
Gap/limit: see [EPI-RTE-benchmark-judge](#epi-rte-benchmark-judge); no supplied execution or causal evidence.

Route ID: [RT-RTE-search-wiki](runtime.md#rt-rte-search-wiki)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: see [RT-RTE-search-wiki](runtime.md#rt-rte-search-wiki).
Content/update relation: no content change.
Transition or check target: Query/trust policy or explicit file path.
Evaluator/condition and domain: see [RT-RTE-search-wiki](runtime.md#rt-rte-search-wiki); domain bounded by the target above.
Activation and timing: see [RT-RTE-search-wiki](runtime.md#rt-rte-search-wiki); operation unobserved.
Possible or observed result: Ranked/delivered content; possible implementation result, not observed.
Implemented force: see [RT-RTE-search-wiki](runtime.md#rt-rte-search-wiki).
Epistemic authority and scope: Retrieval licenses no additional truth.
Operational authority: External host result channel; current/later host context.
Behavioral-authority path: see [RT-RTE-search-wiki](runtime.md#rt-rte-search-wiki); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [RT-RTE-search-wiki](runtime.md#rt-rte-search-wiki) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Direct read bypasses output search predicate.
Gap/limit: see [RT-RTE-search-wiki](runtime.md#rt-rte-search-wiki); no supplied execution or causal evidence.

Route ID: [RT-RTE-apply-pack](runtime.md#rt-rte-apply-pack)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: see [RT-RTE-apply-pack](runtime.md#rt-rte-apply-pack).
Content/update relation: non-truth-apt policy/content update: installed instructions/configuration.
Transition or check target: Caller-selected pack and validation.
Evaluator/condition and domain: see [RT-RTE-apply-pack](runtime.md#rt-rte-apply-pack); domain bounded by the target above.
Activation and timing: see [RT-RTE-apply-pack](runtime.md#rt-rte-apply-pack); operation unobserved.
Possible or observed result: Future prompt/config/skill changes; possible implementation result, not observed.
Implemented force: see [RT-RTE-apply-pack](runtime.md#rt-rte-apply-pack).
Epistemic authority and scope: Installation is not evidence-responsive improvement by itself.
Operational authority: Future provider/host guidance; until replacement.
Behavioral-authority path: see [RT-RTE-apply-pack](runtime.md#rt-rte-apply-pack); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [RT-RTE-apply-pack](runtime.md#rt-rte-apply-pack) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Host instruction precedence/loading unobserved.
Gap/limit: see [RT-RTE-apply-pack](runtime.md#rt-rte-apply-pack); no supplied execution or causal evidence.

Route ID: [RT-RTE-hydrate-workspace](runtime.md#rt-rte-hydrate-workspace)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: see [RT-RTE-hydrate-workspace](runtime.md#rt-rte-hydrate-workspace).
Content/update relation: truth-apt transformation: acquisition/import.
Transition or check target: Selected remote retained generation.
Evaluator/condition and domain: see [RT-RTE-hydrate-workspace](runtime.md#rt-rte-hydrate-workspace); domain bounded by the target above.
Activation and timing: see [RT-RTE-hydrate-workspace](runtime.md#rt-rte-hydrate-workspace); operation unobserved.
Possible or observed result: Verified bytes restored; possible implementation result, not observed.
Implemented force: see [RT-RTE-hydrate-workspace](runtime.md#rt-rte-hydrate-workspace).
Epistemic authority and scope: Integrity/decryption preserves bytes, not semantic warrant.
Operational authority: Workspace consumers; later opens.
Behavioral-authority path: see [RT-RTE-hydrate-workspace](runtime.md#rt-rte-hydrate-workspace); selection/admission is enforcing where stated, model guidance advisory.
Evidence source ID and local anchor: see [RT-RTE-hydrate-workspace](runtime.md#rt-rte-hydrate-workspace) (SRC-1).
Claim IDs: see System-claim versus route comparison.
Mismatch marker: Source warrant unknown; full replay semantics uninspected.
Gap/limit: see [RT-RTE-hydrate-workspace](runtime.md#rt-rte-hydrate-workspace); no supplied execution or causal evidence.

## System-claim versus route comparison

| Claim ID | Claimed operation/warrant | Source/layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support/design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-graph-grounding](#epi-clm-graph-grounding) | See record | SRC-1: `README.md`; doctrine/design | ONLY-edge instruction, citations | [EPI-RTE-graph-answer](#epi-rte-graph-answer), [EPI-RTE-span-check](#epi-rte-span-check) | None supplied | No intervention; quote presence differs from edge entailment | Available-edge citation metadata implemented | Answer prose can survive invalid citations; no semantic grounding enforcement |
| [EPI-CLM-output-quarantine](#epi-clm-output-quarantine) | See record | SRC-1: `README.md`; doctrine/design | Trust workflow | [RT-RTE-admit-output](runtime.md#rt-rte-admit-output), [EPI-RTE-grounding-check](#epi-rte-grounding-check), [EPI-RTE-verify-promote](#epi-rte-verify-promote) | None supplied | No outcome evidence; unrestricted mode/manual admissions differ | Policy-scoped output reuse restriction exists | Not universal quarantine or mandatory evidence-consuming verification |
| [EPI-CLM-edge-contradictions](#epi-clm-edge-contradictions) | See record | SRC-1: `README.md`; doctrine/design | Temporal supersession | [EPI-RTE-edge-supersession](#epi-rte-edge-supersession) | None supplied | No contradiction-free outcome; narrow functional-predicate policy | Selected functional conflicts can invalidate old edges | Low confidence, entity-level contradictions and other predicates deferred; default answers not guaranteed contradiction-free |
| [RT-CLM-review-order](runtime.md#rt-clm-review-order) | See record | SRC-1: `internal/trust/promote.go`; implementation/comment | Local publication order | [RT-RTE-admit-output](runtime.md#rt-rte-admit-output) | None supplied | Earlier hooks state write defeats global invariant | Local explicit function ordering supported | See supplied record; no atomic system-wide guarantee |

## Bounded conclusion

Sage-wiki imports caller sources and finished knowledge, and retains model-generated extraction, compiled articles, graph representations, community summaries and answers. Import does not produce new warranted knowledge. Source warrant is unknown here: filenames, source hashes and quoted spans retain lineage cues, but model summary layers and context selection can omit evidence. See the object records and [RT-RTE-query-answer](runtime.md#rt-rte-query-answer). No source-backed example establishes a new entailed proposition from warranted premises through a checked interpretation; the deterministic deductions below concern code behavior, not a new domain fact. Generic model-produced content remains indeterminate between reshaping, derivation and conjecture. Instructions to explain concepts/themes afford synthesis but do not prove non-entailment for an actual candidate.

Three kinds of checking have different licenses. Source-count and article-quality checks gate eligibility or trigger a rewrite but do not test claim truth. Span checking enforces nonempty normalized quote occurrence in compiled summaries, not original-document entailment. Graph QA validates citation indices, not whether each answer claim follows from the cited edges. See [EPI-RTE-source-count](#epi-rte-source-count), [EPI-RTE-quality-score](#epi-rte-quality-score), [EPI-RTE-span-check](#epi-rte-span-check), and [EPI-RTE-graph-answer](#epi-rte-graph-answer). These positive controls coexist with substantive warrant limits.

The strongest inspected evidence-consuming answer acceptance is conditional auto-promotion: model-estimated passage support reaches a configured threshold, confirmation count passes its configured threshold, and chunk-set distance exceeds 0.3 or count reaches twice threshold. Its intended use is future reuse of the retained answer; scope is pending output identity, not every article. Operational authority is move/index/state eligibility followed by enforcing verified-mode selection on participating retrieval/context consumers. Hooks can reuse a previously stored grounding score; manual promotion/resolve can instead authorize a caller-selected winner without a recorded evidence-consuming criterion, and unrestricted mode admits outputs directly. See [EPI-RTE-grounding-check](#epi-rte-grounding-check), [EPI-RTE-verify-promote](#epi-rte-verify-promote), [EPI-RTE-answer-agreement](#epi-rte-answer-agreement), and [RT-RTE-admit-output](runtime.md#rt-rte-admit-output). Acceptance is thus implemented under a bounded proxy policy, not established source truth or infallibility. No observed accepted ampliative claim is established. Only policy-accepted outputs acquire the inspected promotion integration path; other retained/useful candidates are not relabeled as post-acceptance integration.

Source changes and explicit rejection can withdraw later retrieval eligibility, but do not retroactively retract an answer already delivered or prohibit known-path reads. Functional-edge supersession changes later temporal selection using model confidence and configured predicate assumptions, with ambiguous conflicts left live. See [EPI-RTE-output-withdrawal](#epi-rte-output-withdrawal), [EPI-RTE-edge-supersession](#epi-rte-edge-supersession), and [RT-RTE-search-wiki](runtime.md#rt-rte-search-wiki).

Quality-triggered fresh rewriting is an implemented local response to evaluation. It can change a retained artifact that later shapes synthesis, but a score-triggered rewrite is not content-directed criticism naming a disputed theory, blame and revision. It also can leave a low-scoring article published. Natural-language method instructions and packs affect future proposals or host behavior conditionally; neither their presence nor a learning label demonstrates improved capacity, reflection, autonomous theory building or exercised self-improvement. No actual formulated theory instance or complete theory-builder route is assessed here; provider processing is opaque, not declared absent. See [EPI-RTE-quality-rewrite](#epi-rte-quality-rewrite), [RT-RTE-apply-pack](runtime.md#rt-rte-apply-pack), and [RT-BAP-generated-skill](runtime.md#rt-bap-generated-skill). The first three self-change links have at most a dispositional article-rewrite pathway; subsequent operation causally depending on it is unestablished, so exercised self-improvement is not attributed. Learning benefit and causal component improvement independently remain unestablished.

The shipped benchmark has a reference-answer evaluator, unlike native open Q&A. It judges a separate answerer over retrieved text and records results; its existence neither validates the native production process nor installs a feedback policy into it. See [EPI-RTE-benchmark-judge](#epi-rte-benchmark-judge). No single score, oracle or system-wide epistemic verdict follows from these heterogeneous routes. Uninspected included operations in the coverage table prevent a system-complete negative.

## Shared records

### Operative objects

#### EPI-OBJ-source-text
Label: Raw and capture text

Raw source/capture markdown: natural-language assertions about caller-provided documents, decisions or events; filesystem substrate. Raw reader import is distinct from model-extracted capture items. Closest supplied routes are [RT-RTE-capture-source](runtime.md#rt-rte-capture-source) and [RT-RTE-capture-knowledge](runtime.md#rt-rte-capture-knowledge); neither declares this content object. Producers are callers or extraction providers; later compiler consumes it. Initial truth and extraction fidelity unknown. SRC-1: `internal/prompts/templates/capture_knowledge.txt`; implementation.

> - Each item should be self-contained — understandable without the original conversation.
> --- `internal/prompts/templates/capture_knowledge.txt`

#### EPI-OBJ-article-text
Label: Compiled article prose

Article body, definitions and self-rated confidence are natural-language content retained as concept markdown; later search/read/Q&A and article updates consume it. System-built YAML selectors are a separate symbolic surface. Distinct content object, not the scheduling [RT-OBJ-compile-items](runtime.md#rt-obj-compile-items) or generation [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources). Truth-apt scope depends on the individual article; no actual candidate instance supplied. SRC-1: `internal/compiler/write.go`; implementation.

> articleContent := resp.Content
> --- `internal/compiler/write.go`

#### EPI-OBJ-output-text
Label: Answer prose

Question/answer natural-language strings in pending_outputs and markdown outputs; answers concern the asked question over retrieved context. Later agreement checks and permitted retrieval consume them. Distinct object from [RT-RTE-query-answer](runtime.md#rt-rte-query-answer) and [RT-RTE-admit-output](runtime.md#rt-rte-admit-output) which declare routes. State, hashes and confirmation counts are symbolic controls, not the answer propositions. SRC-1: `internal/trust/hooks.go`; implementation.

> Answer     string
> --- `internal/trust/hooks.go`

#### EPI-OBJ-relation-text
Label: Evidence and entity descriptions

Natural-language entity descriptions and evidence spans retained through ontology entities/relations in the database. They make document/domain claims whose scope follows the asserted edge. Material prose part of graph production, distinct from structured endpoints/predicates. Closest supplied route [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources) is not an object declaration. SRC-1: `internal/compiler/extract_triples.go`; implementation.

> Evidence:   r.Evidence,
> --- `internal/compiler/extract_triples.go`

#### EPI-OBJ-relation-state
Label: Structured relation and provenance state

Symbolic entity IDs, relation predicates, source-document IDs, confidence and valid-time fields in ontology tables; graph serialization and temporal policies use fixed rules. Endpoint/predicate tuples express candidate propositions; numeric confidence alone is not a truth-apt assessment of correctness. Distinct operative part from evidence prose; closest supplied [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources) only declares the aggregate route. SRC-1: `internal/compiler/extract_triples.go`; implementation.

> SourceDoc:  sourceDoc,
> ValidFrom:  validFrom,
> --- `internal/compiler/extract_triples.go`

#### EPI-OBJ-community-text
Label: Community summary prose

Natural-language theme and keyword summaries in community rows, markdown and retrieval indexes; GlobalQA consumes cached summaries. Membership IDs/hash/model are symbolic cache controls, not warranted theme assertions. No supplied object counterpart; related aggregate [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources) includes optional graph passes. SRC-1: `internal/compiler/communities.go`; implementation.

> if err := cs.SetSummary(c.ID, summary, hash, model); err != nil {
> --- `internal/compiler/communities.go`

### Routes

#### EPI-RTE-source-count
Label: Declared source-count gate

Part of: [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources)

Extracted concepts → filterLowEvidence → kept/skipped partition → later manifest/article processing. Model proposes source lists; code decides count eligibility before AddConcept. minSources <= 0 disables rejection. Criterion is declared source count for article generation, not independent-document support. No human per-concept decision or expected-answer oracle; open compilation. Existing source generation guidance shapes candidates. The gate itself writes no artifact; parent persists kept concepts. No rollback required for excluded candidates. SRC-1: `internal/compiler/evidence_gate.go`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Kept/skipped concept slices.
- Later read-back: inapplicable — partition itself is current-pass state; retained results belong to compile route.
- Delegated visibility: inapplicable — local count rule, no delegated call.
- Selection predicate: Configured minimum and len(c.Sources).
- Invalidation or expiry: Recomputed for each candidate list.
- Activation or effect: Enforces continued admission or exclusion in parent compile.
- Evidence limits: Declared paths may be repeated or unsupported; no claim entailment check.

> if len(c.Sources) >= minSources {
> kept = append(kept, c)
> --- `internal/compiler/evidence_gate.go`

#### EPI-RTE-article-cleanup
Label: Article body cleanup

Part of: [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources)

Model response → outer-fence/frontmatter/field stripping → sentence filtering → wikilink canonicalization → rebuilt metadata → write/index. Compiler owns deterministic edits; model proposes prose, structural processing can remove it without human review. Guidance requests precise factual articles and references, not truth-checking. For configured phrase "in conclusion", input "In conclusion, the reactor is safe. Pressure remains high." loses the first sentence and retains " Pressure remains high." because punctuation flush drops matched segments while a nonblank result survives. This implementation deduction proves deletion of a truth-apt sentence, not semantic equivalence. If all content would vanish, original text returns; fenced code is preserved. Result may lose qualifications, so relation is indeterminate rather than automatically non-ampliative. Alternative faithful deletion requires a content-specific proof. No expected-answer oracle; open article writing. Parent persistence/retry supplies recovery, not content rollback. SRC-1: `internal/compiler/write.go`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Cleaned body and payload.
- Later read-back: Parent saves cleaned markdown for later read/search/synthesis and existing-article reuse.
- Delegated visibility: inapplicable — cleanup local; original proposal came from parent provider call.
- Selection predicate: Configured phrases, sentence terminators, fence state and alias map.
- Invalidation or expiry: Later writes can replace content; no preserved deleted-sentence history established.
- Activation or effect: Changes exact prose delivered to later consumers.
- Evidence limits: No observed content instance or semantic-preservation validation.

> if strings.Contains(low, p) {
> return // drop this sentence
> }
> --- `internal/compiler/write.go`

#### EPI-RTE-quality-score
Label: Article proxy quality scoring

Part of: [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources)

On-disk article plus concatenated raw sources/manifest → ScoreArticle → weighted format/phrase/length/link/filler score. Program evaluator targets these textual proxies, not domain claims. Grounding is fraction of selected source three-word windows present; coverage is relative length. Input "The reactor is safe." and article "The reactor is safe. The reactor is not safe." retain all selected source phrases, illustrating that positive overlap does not veto contradiction. Code deduction only. Next consumer is separate rewrite branch. Model proposes article, program computes score; no human judgment or reference-answer oracle. Open compile; no content change or rollback in evaluator itself. SRC-1: `internal/compiler/confidence.go`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: QualityScores including weighted Combined.
- Later read-back: Scores can be stored on source compile_items; later scheduling/lint consumers are bounded by supplied runtime, not all traced here.
- Delegated visibility: inapplicable — zero-LLM scoring.
- Selection predicate: Article/source strings, manifest and normalized weights.
- Invalidation or expiry: Recomputed after rewrite; stored score overwritten.
- Activation or effect: Score selects possible fresh rewrite; not an acceptance veto.
- Evidence limits: Keyword overlap licenses phrase coverage only; input/output deduction not execution.

> Grounding   float64 // fraction of source key phrases present in the article
> --- `internal/compiler/confidence.go`

#### EPI-RTE-quality-rewrite
Label: Low-score fresh rewrite

Part of: [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources)

Score below configured threshold and retry enabled → delete existing article → RetryArticle → score final article → record score/errors. Code decides and can fail before or after deletion; model proposes successor using existing writer guidance. No challenged proposition or blame-bearing criticism is sent by this score branch. One retry in open compile, no answer oracle or human approval. Low-scoring final content still ships; failed retry can leave original file gone. This changes retained work product/possible later synthesis input, but neither success nor exercised self-improvement is established. SRC-1: `internal/compiler/fullpipeline.go`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Retry result, final score or error counts.
- Later read-back: New article and score persist for later retrieval/compile consumers when writes succeed.
- Delegated visibility: Writer provider receives normal article inputs without deleted old article; no sub-agent.
- Selection predicate: opts.ItemStore, readability, threshold, retry flag and manifest concept availability.
- Invalidation or expiry: One rewrite; later source/config drift may schedule more work.
- Activation or effect: Evaluation-responsive fresh proposal replaces retained prose without mandatory threshold acceptance.
- Evidence limits: No observed improvement; deletion lacks complete rollback.

> retryRes := RetryArticle(writeOpts, ExtractedConcept{
> Name:    ar.ConceptName,
> --- `internal/compiler/fullpipeline.go`

#### EPI-RTE-span-check
Label: Summary evidence-span filter

Part of: [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources)

Normalized extracted graph and resolved summary body → verifyEvidenceSpans → filtered relations → persistGraph. Code checks nonempty case/whitespace-normalized substring occurrence; failing relations are rejected before persistence, with event/metric, while entities remain. For summary "Alice founded Acme.", evidence " ALICE  founded Acme. " matches, but an edge claiming Alice owns Acme could still pass this occurrence test: predicate entailment is not checked here. Evidence "Bob founded Acme." fails. These deductions follow normalizeForSpanMatch/evidenceGrounded, without executing target. Model proposes relation/evidence; program can veto span failure. Open compile, no human approval/reference answer; accepted use is edge persistence under occurrence criterion. SourceDoc points to the original document although r.body is the summary. Removal is immediate; other graph writes are best effort. SRC-1: `internal/compiler/extract_triples.go`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Graph with only passing relations.
- Later read-back: Passing edges/evidence persist in ontology; later local/global graph consumers use them.
- Delegated visibility: inapplicable — occurrence check is local, not model judgment.
- Selection predicate: Nonempty normalized evidence substring within resolved compiled summary.
- Invalidation or expiry: Rechecked on extraction; old persisted-state cleanup not inferred from this filter alone.
- Activation or effect: Rejects missing evidence spans before persistGraph.
- Evidence limits: Occurrence is not original-source truth, encoding fidelity or relation entailment.

> g = verifyEvidenceSpans(g, r.body, sink, filepath.Base(projectDir))
> --- `internal/compiler/extract_triples.go`

#### EPI-RTE-edge-supersession
Label: Functional edge supersession

Part of: [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources)

persistGraph adds relation, then optional temporal hooks inspect configured functional predicates/confidence. Model proposes edge and confidence; code invalidates different targets only above configured threshold. Entity-level contradicts edges emit deferred conflict; nonfunctional predicates bypass invalidation; below-threshold functional alternatives remain live and emit review conflict. Domain is caller-configured single-valued predicates, not every contradiction. No human decision or factual answer oracle at automatic edge step. Candidate guidance is extraction; resulting graph validity/conflict records affect later selection. Errors log and later sweep can retry, not atomic rollback. confidenceFloor can raise low extracted confidence before this path; numerical confidence is not external proof. SRC-1: `internal/compiler/extract_triples.go`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Persistence/supersession counters and deferred conflict effects.
- Later read-back: Changed valid-time state is consulted by later graph serialization; conflict records retained for review.
- Delegated visibility: inapplicable — local store operation over model-proposed fields.
- Selection predicate: Enabled hooks, functional predicate and confidence threshold.
- Invalidation or expiry: Old edges retain historical validity; later supersession changes live selection.
- Activation or effect: Can exclude old functional targets from future live subgraphs.
- Evidence limits: Backend invariants/post-resolution sweep not fully inspected; no contradiction-free system guarantee.

> if r.Predicate == ontology.RelContradicts {
> emitEdgeConflict(hooks, sourceDoc,
> --- `internal/compiler/extract_triples.go`

#### EPI-RTE-graph-answer
Label: Local graph answering

Distinct identity: Additional native answer route; overlaps [RT-RTE-query-answer](runtime.md#rt-rte-query-answer) in purpose but GraphQA returns edge-based structured response and does not use that route’s article auto-filing path.

MCP wiki_graph_query local mode → bounded seed search and serialized subgraph → structured model answer/citation integers → dedup/range filtering → CitedEdge response. Code owns progression; model proposes answer/cites. Instruction says ONLY listed edges; code enforces citation range, not claim entailment. Answer acceptance is structural response decoding, not evidence-consuming semantic acceptance. Out-of-range integers drop without rejecting prose; no seeds/edges skips model call. Open questions, no human per-answer judgment or expected-answer oracle. No retention/update by this function; parent ontology supplies state. Invalid schema/model failures return error; already retained graph is unchanged. SRC-1: `internal/query/graphqa.go`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Answer, valid cited-edge metadata, seeds and truncation flag.
- Later read-back: inapplicable — this function returns response without retaining answer.
- Delegated visibility: Provider sees framed question and bounded serialized edges, not all source documents.
- Selection predicate: Hybrid seed matches, hops/edge bounds, temporal AsOf, valid integer cites.
- Invalidation or expiry: Context invocation-local; underlying graph evolves separately.
- Activation or effect: Advisory answer and fixed-rule metadata delivered to external caller.
- Evidence limits: Cannot conclude claims are entailed by cited edges; provider compliance unobserved.

> if n < 1 || n > len(sg.Edges) || seenCite[n] {
> continue
> }
> --- `internal/query/graphqa.go`

#### EPI-RTE-community-summary
Label: Community summary production

Part of: [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources)

Detected graph memberships → summary model over bounded live intra-community edges → nonempty summary stored in database, markdown and indexes. Code chooses members/edges/model; provider proposes themes using ~150-word guidance. Source evidence capped at 200 runes and 40 relations. Nonempty response and cache conditions admit retention; no semantic acceptance decision or reference oracle. Failed summary retries on later compile, failures log; stale/removed/below-min community artifacts can be cleared. Cache checks member hash and model at this layer; complete invalidation for unchanged membership with changed relations depends on uninspected store behavior. This is pre-acceptance retention, not lifecycle integration of an accepted claim. SRC-1: `internal/compiler/communities.go`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Stored/indexed theme prose or logged failure.
- Later read-back: GlobalQA reads summary rows; search can retrieve indexed community content across invocations.
- Delegated visibility: Summary provider sees members and bounded/truncated selected live relations.
- Selection predicate: Communities enabled, stores/client present, minimum members, stale hash/model and nonempty output.
- Invalidation or expiry: Detection replaces membership; stale/small/removed artifacts cleared; summary cache skips matching hash/model.
- Activation or effect: Retained themes supply later model evidence without semantic verification.
- Evidence limits: Detection/cache backend internals uninspected; no evidence theme truth or full source coverage.

> if c.SummaryHash == hash && c.Model == model {
> continue // cached, unchanged
> }
> --- `internal/compiler/communities.go`

#### EPI-RTE-global-answer
Label: Global community answering

Distinct identity: Shipped global mode of wiki_graph_query; distinct from [RT-RTE-query-answer](runtime.md#rt-rte-query-answer) article answering and [EPI-RTE-graph-answer](#epi-rte-graph-answer) edge answering.

Handler enforces communities enabled and rejects as_of in global mode → GlobalQA chooses summarized level/hits → one map call per summary → filter empty/IRRELEVANT partials → reduce → answer with community citations. Code owns selection, providers propose partials/global prose. Model relevance declaration changes which partials reach reduction; no substantive checker follows. Cited communities are origins of retained relevant partials, not claim-by-claim validation of final answer. Open questions with no expected answer/human content approval. Returns errors for no summaries/matches and fixed no-coverage message if no relevant partials; no answer persistence or rollback. SRC-1: `internal/query/globalqa.go`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: GlobalQAResult answer/level/cited communities or errors.
- Later read-back: inapplicable — current partials and final answer are not retained by this function.
- Delegated visibility: Map providers receive selected community summary; reducer receives filtered partials and question, not underlying complete graph.
- Selection predicate: Chosen summarized level, member minimum, retrieval hits/max communities, model relevance text.
- Invalidation or expiry: Invocation-local; later calls consult current cached summaries.
- Activation or effect: Model relevance selection governs reduction; advisory answer reaches external caller.
- Evidence limits: Semantic preservation across two model layers unestablished; community citation is lineage not entailment.

> if p.text == "" || strings.HasPrefix(strings.ToUpper(strings.TrimLeft(p.text, "* ")), "IRRELEVANT") {
> continue
> }
> --- `internal/query/globalqa.go`

#### EPI-RTE-answer-agreement
Label: Recurring answer comparison

Part of: [RT-RTE-admit-output](runtime.md#rt-rte-admit-output)

Similar pending/confirmed question selected by vector cosine → CompareAnswers uses answer embeddings (>=0.9 agree; <0.7 disagree), else model same-core-facts judgment → hooks confirmation or conflict state. Same chunk-ID JSON is idempotent; confirmations use pairwise Jaccard distance. ShouldAutoPromote permits independence >0.3 OR count >= twice threshold, once minimum confirmations attained. Model/software compare and decide; generic initiating caller need not be human. No expected-answer oracle; open recurring questions. Result updates confirmation or conflict state; conflicting candidate persists and old candidate can lose verified retrieval eligibility. Rejection errors/partial state follow parent transaction and post-tx gates. Agreement is not truth and distinct chunks are not independent causal evidence. SRC-1: `internal/trust/consensus.go`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Agreement bool/independence score, consumed by hooks.
- Later read-back: Stored confirmations/state/answer hashes influence subsequent filing/Verify invocations.
- Delegated visibility: Embedding or comparison provider receives answer pair; no source-truth test.
- Selection predicate: Similar question cosine; answer similarity bands/fallback verdict; chunk-ID sets.
- Invalidation or expiry: Repeated identical evidence skipped; later disagreements can mark conflict.
- Activation or effect: Confirms/counts or conflicts candidates and conditions promotion.
- Evidence limits: Chunk metadata collected before final answer-context assembly; source independence unestablished.

> return independence > 0.3 || confirmations >= 2*threshold
> --- `internal/trust/consensus.go`

#### EPI-RTE-grounding-check
Label: Pending answer grounding evaluation

Distinct identity: Standalone verify evaluator not separately declared in runtime; feeds [RT-RTE-admit-output](runtime.md#rt-rte-admit-output) through stored score and promotion, but is not the on-filing agreement check.

CLI verify → pending-output filters/limit → load current files named in SourcesUsed → model ExtractClaims → per-claim model CheckEntailment against concatenated passages → mean score → UpdateGroundingScore. Evaluator targets claimed passage support, not source truth. Grounded=1, inferred=0.5, default ungrounded=0; no factual claims=1. Unreadable paths silently skipped. Claims/extractor output can omit disputed propositions; nil sources do not cause automatic check rejection. Program decides parser/IO failures; model supplies substantive verdict; no human per-claim review or expected-answer oracle. Intended use is auto-promotion evidence; criterion and scope belong to separate disposition. No answer edit/rollback in this check; failed scoring leaves error and skips disposition. SRC-1: `internal/trust/grounding.go`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Verify result/error and persisted grounding score.
- Later read-back: Stored score is consumed by later hooks/Verify promotion policy.
- Delegated visibility: Providers receive answer to extract claims and all loaded passages per claim; not original query-context snapshot.
- Selection predicate: Pending filters/limit; model claims and verdict strings.
- Invalidation or expiry: Verify can recompute; source changes may later demote outputs.
- Activation or effect: Produces scoring evidence for later admission, not independent accepted truth.
- Evidence limits: Inferred claims count half; no claims scores one; source truth/claim completeness unvalidated.

> if len(claims) == 0 {
> return 1.0, nil
> }
> --- `internal/trust/grounding.go`

#### EPI-RTE-verify-promote
Label: Verify-driven answer promotion

Distinct identity: Disposition part of standalone Verify, distinct from [RT-RTE-admit-output](runtime.md#rt-rte-admit-output) on-filing hook; same promotion function is reused, not redeclared.

Verify result → updated score >= configured threshold with AutoPromote → confirmation independence/count test → PromoteOutput with index stores (CLI supplies them), else state-only Promote for nil Stores callers. Program decides/vetoes; models supplied score/evidence indirectly; human approval unnecessary, initiating caller identity unresolved. This records evidence-consuming proxy acceptance for future answer retrieval, conditional on grounding plus consensus policy. No expected-answer oracle; open pending-output maintenance. Index/move/state errors are reported per result; no complete rollback established. Canonical integration and alternate manual/unrestricted admissions remain in runtime container. SRC-1: `internal/trust/verify.go`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Promoted flag or per-output error.
- Later read-back: Confirmation state/indexes condition subsequent verified search/context.
- Delegated visibility: inapplicable — local disposition; provider judgment belongs to grounding check.
- Selection predicate: AutoPromote, score threshold, ShouldAutoPromote, default consensus 3 if unset.
- Invalidation or expiry: Demotion/reject/source change can later remove eligibility.
- Activation or effect: Authorizes promotion/indexing; nil-store branch changes state without this indexing path.
- Evidence limits: Acceptance is bounded proxy policy; defaults/configuration not deployment evidence.

> if opts.AutoPromote && score >= opts.Threshold {
> --- `internal/trust/verify.go`

#### EPI-RTE-output-withdrawal
Label: Output withdrawal and cleanup

Distinct identity: Combines homogeneous local withdrawal controls spanning [RT-RTE-admit-output](runtime.md#rt-rte-admit-output) and omitted CLI resolve/clean, not a duplicate single route; functions have different triggers stated separately.

CheckSourceChanges compares retained source hashes for confirmed outputs and demotes/deindexes changed ones. CLI resolve promotes chosen output then rejects same-question-hash siblings; generic caller supplies winner, no evidence-consuming winner criterion enforced. CLI clean selects old outputs and calls RejectOutput, ignoring rejection errors while advancing cleaned count. Program/caller can remove eligibility; neither source change nor age means falsehood. No factual oracle or mandatory human judgment. Recovery is later re-verification/re-promotion or retry; no cross-operation rollback. These routes alter retained state, not already delivered answers or direct read access. SRC-1: `internal/trust/source_check.go`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Demoted/rejected/cleaned counts or errors; clean count is not deletion success evidence.
- Later read-back: Updated trust/index state affects future participating retrieval consumers.
- Delegated visibility: inapplicable — local file/hash/store operations.
- Selection predicate: Changed source hash; explicit winner and sibling question hash; age cutoff.
- Invalidation or expiry: Stale state persists until later action; rejected file/state can be removed.
- Activation or effect: Deindexes/demotes/rejects candidates; resolve makes chosen answer eligible.
- Evidence limits: Compiler invocation of source checker supplied by runtime; no full rollback/error audit.

> if currentHash != o.SourcesHash {
> --- `internal/trust/source_check.go`

#### EPI-RTE-style-check
Label: Article style presence check

Distinct identity: Additional lint evaluation route; runtime mentions linter but declares no corresponding route.

Lint Runner invokes StylePass on concept markdown → prefix/frontmatter field tests → findings. Code evaluates syntactic presence, not truth or calibrated confidence. Findings reach runner/caller; optional fix is separate. Article authors may be caller/model; code decides warnings, no human per-finding approval or expected-answer oracle. Open lint maintenance; no article mutation by check. Failed pass logs/continues in runner, not semantic rejection of corpus. SRC-1: `internal/linter/passes.go`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Style findings with severity/path/optional fix.
- Later read-back: inapplicable — check results are current-run; report persistence is separate runner functionality.
- Delegated visibility: inapplicable — deterministic filesystem/string checks.
- Selection predicate: Concept markdown entries readable; prefix and first-500-character concept-field tests.
- Invalidation or expiry: Recomputed on later lint.
- Activation or effect: Advisory finding or trigger for explicit --fix branch.
- Evidence limits: Other lint checks cannot inherit this narrow evaluation domain.

> if !strings.HasPrefix(content, "---") {
> --- `internal/linter/passes.go`

#### EPI-RTE-style-fix
Label: Style metadata repair

Distinct identity: Separate mutation consumer of [EPI-RTE-style-check](#epi-rte-style-check); no supplied runtime counterpart.

Runner fix requested + CanAutoFix + findings → StylePass.Fix → prefix frontmatter with filename concept and confidence low. Program chooses proposal/admission; caller opts into repair, identity unresolved. No truth check/reference oracle; defaults are policy metadata. No backing of original content or complete file/index rollback shown. This is direct metadata repair, not accepted domain inference. SRC-1: `internal/linter/passes.go`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Fix returns nil; individual writes can fail without propagated error.
- Later read-back: Changed article is available to future file readers.
- Delegated visibility: inapplicable — local mutation only.
- Selection predicate: Findings with Fix == add frontmatter and readable files.
- Invalidation or expiry: Future edits overwrite metadata.
- Activation or effect: Adds policy metadata in filesystem; no index refresh shown in this function.
- Evidence limits: Write errors ignored; no observed repair or semantic acceptance.

> fm := fmt.Sprintf("---\nconcept: %s\nconfidence: low\n---\n\n", name)
> --- `internal/linter/passes.go`

#### EPI-RTE-benchmark-judge
Label: LOCOMO reference-answer evaluation

Distinct identity: Additional shipped evaluator; closest [RT-RTE-search-wiki](runtime.md#rt-rte-search-wiki) delivers backend retrieval, not native query synthesis.

LOCOMO driver backend.search → separate answerer.generate → _judge(category, question, dataset answer, generated answer) → binary score/reason/parse-error record → run aggregation/persistence. Judge uses category-conditioned reference answer after preprocess_answer; provider identity/config supplied externally. Target is dataset-answer correctness under judge protocol, not compile-process correctness or native Q&A. No human per-answer decision; model supplies verdict and code maps CORRECT to 1. Invalid JSON -> WRONG/0 with parse flag; infrastructure failures separated. Mode is bounded benchmark questions, with explicit expected-answer oracle supplied by dataset. Output is score/evidence record, not knowledge promotion or production-policy change; no inspected feedback consumer installs changes. SRC-1: `eval/benchmarks/locomo/run.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Judgment, scalar score, reason/parse flag and question record.
- Later read-back: Benchmark rows/aggregate outputs retained by driver for later readers, not native output retrieval admission.
- Delegated visibility: Answerer receives retrieved text; judge receives question/reference/generated response via prompt helper.
- Selection predicate: Dataset category/questions; optional top-k cutoffs; binary label.
- Invalidation or expiry: Per-question checkpoints/results persist; no native knowledge rollback.
- Activation or effect: Changes evaluation records and aggregate scores, not implemented native behavior adaptation.
- Evidence limits: Judge prompt internals/results not inspected; no score attribution or causal comparison established.

> correct = str(raw.get("label", "")).upper() == "CORRECT"
> --- `eval/benchmarks/locomo/run.py`

### Claims

#### EPI-CLM-graph-grounding
Label: Graph-only answer grounding

Claim: native local relational answers are grounded only in graph edges and evidenced citations carry document/confidence. SRC-1: `README.md`; doctrine/design. Distinct from [RT-CLM-review-order](runtime.md#rt-clm-review-order), whose claim concerns publication ordering.

> - **Graph memory with citations.** Ask relational questions through `wiki_graph_query` — answers are grounded only in serialized graph edges; with the evidenced graph enabled, each citation carries its source document and confidence.
> --- `README.md`

#### EPI-CLM-output-quarantine
Label: Output quarantine until verification

Claim: query outputs are quarantined until verified. SRC-1: `README.md`; doctrine/design. Related but distinct from [RT-CLM-review-order](runtime.md#rt-clm-review-order): this concerns mandatory disposition, not publication ordering. Runtime already supplies source-supported alternate unrestricted/manual paths.

> - **Trust and provenance.** Query outputs quarantine until verified; every evidenced relation records which document asserted it.
> --- `README.md`

#### EPI-CLM-edge-contradictions
Label: Contradiction-free default answers

Claim: contradictory facts invalidate old edges and default answers are contradiction-free. SRC-1: `README.md`; doctrine/design. No supplied claim counterpart after comparison with [RT-CLM-review-order](runtime.md#rt-clm-review-order).

> Edges are bi-temporal: contradicting a fact invalidates the old edge instead
> of colliding, default answers are contradiction-free, and `as_of` queries
> answer "what did we believe in January?" Ambiguous contradictions still
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

No additional declarations: each new route names its concrete consumer/channel/force/horizon; static synthesis and generated host guidance are see [RT-BAP-query-guidance](runtime.md#rt-bap-query-guidance) and [RT-BAP-generated-skill](runtime.md#rt-bap-generated-skill). No host compliance or actual changed behavior is inferred.
