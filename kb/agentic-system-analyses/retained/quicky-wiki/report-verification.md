---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Independent report verification of Quicky Wiki's compiler, retained graph, epistemic routes and CLI delivery at its frozen commit."
run-id: AAS-2026-10-15-quicky-wiki-628f7d7cc628-01
reviewed-boundary: cfeecbffce5b6d0f16533b258a1e88edd86f731e
---

# Quicky Wiki report verification

## Verification

The current reports support a bounded implementation account. The prior transaction blocker is repaired, and no material blocker remains. I judged the pinned reports afresh against source text, not against the previous verifier's conclusions or the analysts' reported checks. The supplied structural report-check is `none`. Runtime supplies one correction answer; the other three answer files are empty.

The checkout HEAD matches the reviewed commit and its working tree is clean. Evidence remains SRC-1 implementation and doctrine/design under the [Source register](boundary.md#source-register). No target program, test, example, provider request or service was executed. Static wiring is not observed activation, reliable model compliance or demonstrated benefit.

### Runtime and workflow

I traced setup/load, source ingestion, comparison/resolution, query/save, consensus, client dispatch, maintenance and release against their actual producers and consumers. This covers [RT-CMP-llm-adapter](runtime.md#rt-cmp-llm-adapter), [RT-OBJ-knowledge-store](runtime.md#rt-obj-knowledge-store), [RT-OBJ-knowledge-diff](runtime.md#rt-obj-knowledge-diff), [RT-RTE-runtime-setup](runtime.md#rt-rte-runtime-setup), [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), [RT-RTE-question-answer](runtime.md#rt-rte-question-answer), [RT-RTE-consensus-answer](runtime.md#rt-rte-consensus-answer), [RT-RTE-answer-save](runtime.md#rt-rte-answer-save), [RT-RTE-client-access](runtime.md#rt-rte-client-access), [RT-RTE-health-review](runtime.md#rt-rte-health-review) and [RT-RTE-package-release](runtime.md#rt-rte-package-release).

Source supports code-owned sequencing, text inference through unpinned external model identities, automatic graph admission and source/hash registration before completion. Full compiler reads confirm extraction's empty-array fallback, comparison's all-new fallback, omitted-match loss, missing claim-edge insertion, assignment defaults and noncritical summaries. The CLI prints ingestion success before its rendering tail; an unchanged retry can skip unfinished compilation. These findings preserve the [workflow account](workflow.md#workflow-account) and its annotation: delegated model computations are not autonomous workers, semantic matching is not factual approval, and batch continuation is not recovery (SRC-1, `src/compiler/ingest.ts`, `src/compiler/diff.ts`, `src/compiler/resolve.ts`, `src/cli/ingest.ts`, `src/render/markdown.ts`). No workflow correction is needed.

Ordinary query really selects graph statements/confidence without source bodies, event reasons or model-visible claim IDs. Returned IDs are unvalidated; MCP returns their count. [RT-CLM-confidence-citations](runtime.md#rt-clm-confidence-citations) correctly distinguishes the advertised feature from citation integrity. Consensus has both single-response and comparison-failure alternatives that label claims agreed without multi-model convergence. [RT-BAP-retained-context](runtime.md#rt-bap-retained-context) correctly describes advisory text delivery, separate from enforced updates and configured system-message guidance (SRC-1, `src/graph/query.ts`, `src/compiler/consensus.ts`, `src/mcp/server.ts`, `src/compiler/ingest.ts`, `src/llm/adapter.ts`).

Client findings survive independent inspection: MCP resolves the supplied path without raw-directory containment or schema validation at dispatch; dashboard page DELETE is shadowed by its earlier pathname-only branch; claim edits/deletion and prune remain separate reachable operations. Both HTTP servers listen without an explicit host and expose wildcard CORS, but no actual network exposure or deployment isolation is inferred (SRC-1, `src/mcp/server.ts`, `src/cli/serve.ts`, `src/lib.ts`). Setup/config and release findings likewise retain their implementation-only scope (SRC-1, `src/cli/create.ts`, `src/cli/context.ts`, `package.json`, `.github/workflows/publish.yml`).

### Correction disposition: transaction coverage

I independently reread the store's five transactional methods and complete `deleteEmptyPages`, then checked both direct prune callers. The runtime answer is substantiated: the [guarantee table](runtime.md#guarantees-forcing-cases-and-authority-envelope) now restricts atomicity to writes within `addClaim`, `reinforceClaim`, `challengeClaim`, `deleteClaim` and `deletePage`. [RT-RTE-client-access](runtime.md#rt-rte-client-access) and [RT-RTE-health-review](runtime.md#rt-rte-health-review) explicitly retain the nontransactional prune exception and its partial-deletion consequence. Their source passage shows the deletion sequence. Whole-ingest and filesystem nontransactionality remain intact. The previous blocker is discharged, not converted into a limit (SRC-1, `src/graph/store.ts`, `src/cli/lint.ts`, `src/cli/serve.ts`).

### Memory parts and consumers

I checked each memory declaration against schema, writers, invalidation and actual delivery: [MEM-OBJ-claims](memory.md#mem-obj-claims), [MEM-OBJ-claim-controls](memory.md#mem-obj-claim-controls), [MEM-OBJ-page-summaries](memory.md#mem-obj-page-summaries), [MEM-OBJ-source-register](memory.md#mem-obj-source-register), [MEM-OBJ-epistemic-events](memory.md#mem-obj-epistemic-events), [MEM-OBJ-graph-relations](memory.md#mem-obj-graph-relations) and [MEM-OBJ-rendered-views](memory.md#mem-obj-rendered-views), including their runtime annotations.

Their distinctions hold. Challenge lowers the retained statement's score and records a reason without necessarily retaining the challenger statement. Generic confidence updates reset age without adding an event. Source rows retain metadata rather than raw snapshots; quality labels are not authenticated. Summary text affects search and views, not ordinary answer text. Direct edits, deletion and decay do not invoke summary regeneration. Watch ignores deletion and initially admits only unregistered paths. Database withdrawal does not sweep raw files, saved answers or rendered views; dashboard page reads can expose existing Markdown separately from current rows. Retained reasons are not therefore later model inputs (SRC-1, `src/graph/store.ts`, `src/graph/query.ts`, `src/compiler/resolve.ts`, `src/compiler/diff.ts`, `src/compiler/ingest.ts`, `src/graph/temporal.ts`, `src/graph/cascade.ts`, `src/cli/watch.ts`, `src/cli/save-answer.ts`, `src/cli/serve.ts`, `src/render/markdown.ts`). The annotations do not mistake library storage capability for an observed external consumer or provider opacity for absent memory.

### Epistemic records and evidence strength

I checked the full [inventory](epistemic.md#epistemic-object-inventory), [ledger](epistemic.md#authority-route-ledger) and claim comparison against the transformations and consumer payloads. [EPI-OBJ-source-content](epistemic.md#epi-obj-source-content), [EPI-OBJ-claim-statements](epistemic.md#epi-obj-claim-statements), [EPI-OBJ-confidence-state](epistemic.md#epi-obj-confidence-state) and [EPI-OBJ-page-summaries](epistemic.md#epi-obj-page-summaries) preserve the difference between imported assertions, generated prose, scalar policy and factual warrant. [EPI-OBJ-query-results](epistemic.md#epi-obj-query-results) and [EPI-OBJ-consensus-result](epistemic.md#epi-obj-consensus-result) are transient output objects, not accepted graph claims (SRC-1, `src/compiler/ingest.ts`, `src/compiler/confidence.ts`, `src/graph/store.ts`, `src/compiler/resolve.ts`, `src/graph/query.ts`, `src/compiler/consensus.ts`, `src/cli/fetch-url.ts`).

[EPI-OBJ-review-proposals](epistemic.md#epi-obj-review-proposals), [EPI-OBJ-resurface-reviews](epistemic.md#epi-obj-resurface-reviews) and [EPI-OBJ-discovery-proposals](epistemic.md#epi-obj-discovery-proposals) have separate targets and advisory consumers. The complete functions and CLI callers confirm no automatic adoption/persistence of those suggestions. Discovery's index mapping does not establish semantic correspondence (SRC-1, `src/metabolism/redteam.ts`, `src/metabolism/resurface.ts`, `src/discovery/discover.ts`, `src/cli/metabolism.ts`, `src/cli/discover.ts`).

[EPI-RTE-chunk-selection](epistemic.md#epi-rte-chunk-selection)'s polarity counterexample follows from normalized-prefix equality, not a measured failure rate. The reinforcement counterexample follows from the weighted blend. [EPI-RTE-lint-prune](epistemic.md#epi-rte-lint-prune) correctly separates structural diagnosis from empty-page deletion; neither checks factual truth. [EPI-OBJ-slide-content](epistemic.md#epi-obj-slide-content) and [EPI-RTE-slide-output](epistemic.md#epi-rte-slide-output) identify a separate generation/write path whose matching-topic branch overrides the default confidence floor (SRC-1, `src/compiler/ingest.ts`, `src/compiler/confidence.ts`, `src/cli/lint.ts`, `src/graph/store.ts`, `src/render/marp.ts`, `src/cli/compile.ts`).

[EPI-CLM-living-knowledge](epistemic.md#epi-clm-living-knowledge) faithfully attributes README claims without inventing a calibration promise. The reports' missing-edge and advisory-review qualifications are supported. Semantic indeterminacy without concrete input/output pairs is appropriate; it does not erase implemented generation. Save/reingest supplies no independent corroboration. Learning, reflection, autonomy and self-improvement remain separate bounded conclusions rather than one unsupported verdict (SRC-1, `README.md`, `src/cli/save-answer.ts`, `src/compiler/diff.ts`, `src/compiler/resolve.ts`).

### Relations and reconciliation

Every declared `Part of:` relation was checked for substantive containment. SQLite parts belong to the graph container; query, consensus and review objects are route outputs; chunk selection and lint/prune are suboperations. Cross-kind parents are explained. The combined confidence-state record spans finer memory parts without making their findings wrong.

Both amendments in [reconciliation](reconciliation.md#reconciliation) identify duplicate retained referents: claim statements and page summaries. Transient extraction arrays are lineage, not another durable store. The valid store container, nonidentical confidence grouping and rendered-file/slide overlap need no supersession. Integration dispositions preserve both consumer scopes for Markdown and reasons, conditional cascade capability, unobserved external initialization, and separate delivery milestones. The current transaction discussion accurately reflects the repair. No unresolved inter-report conflict or missing required part was found; no other member depends on the withdrawn broad atomicity wording.

### Omission questions and stopping decision

The frozen tracked tree, complete CLI dispatch, library exports and source-wide searches for model calls, file writes, event writes, claim mutations and claim-edge producers supplied the search basis. I investigated whether an alternate shipped writer or later consumer could overturn automatic admission, reason omission, incomplete withdrawal, advisory criticism or confidence-based selection. Following those dependencies through MCP, dashboard, watch, save-answer, discovery and compilation found no contrary route requiring correction. Edge-adder searches find only store declarations, supporting the bounded shipped-producer finding, not an absence of externally populated edges (SRC-1, `src/cli.ts`, `src/lib.ts`, `src/graph/store.ts`, `src/mcp/server.ts`, `src/cli/serve.ts`).

Additional complete reads of Anki, timeline and Obsidian renderers, health calculations, the decay wrapper and JSON parsing checked alternative confidence selectors, historical-reason display, source export and technical acceptance. They preserve the emitted distinctions: formatting/display is not factual acceptance; export source pages are not raw backups; health is graph calculation rather than an independent truth check (SRC-1, `src/render/anki.ts`, `src/render/timeline.ts`, `src/render/obsidian.ts`, `src/metabolism/health.ts`, `src/metabolism/decay.ts`, `src/llm/parse-json.ts`). These reads extend verification coverage, not the analysts' stated inspection histories.

Further optional omission expansion stopped because the selected consequential questions have supported dispositions and no identified material challenge remains unresolved. Uninspected UI/template details, provider/dependency internals and deployment evidence cannot support exhaustive security, export-correctness, operational recovery or efficacy comparisons. The reports already withhold those conclusions and preserve positively established routes; their faithfully scoped uncertainty requires no additional verification limit.

## Blockers

none

## Limits

none
