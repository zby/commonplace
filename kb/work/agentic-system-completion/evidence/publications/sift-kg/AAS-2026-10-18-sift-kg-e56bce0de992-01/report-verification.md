---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Report verification of sift-kg's document-to-graph, maintenance and external-agent consumption account at the frozen commit."
run-id: AAS-2026-10-18-sift-kg-e56bce0de992-01
reviewed-boundary: "d786991c024f5401f113fc0cb70aee96dd1bd3bf"
---

# sift-kg report verification

## Verification

The pinned reports support a bounded implementation account, with the two local inventory limits below. No material correction is required. I read all five members, their types, the boundary, the empty correction-answer inputs and the structural check. The structural check reports no findings. No earlier objection or analyst answer supplies independent evidence.

### Evidence and record checks

I checked source-dependent claims against SRC-1 at the revision in the [source register](boundary.md#source-register). The checkout HEAD equals that revision and its status was clean. Independent source inspection covered the extraction/cache/parser paths, discovery and domain models/prompts, graph build/support/load/save/postprocessing, both apply callers, review models/I/O/reviewer, resolution batching and cross-type proposals, narrative orchestration/context joins/rewrites, retrieval projections, export dispatch/flattening, view data construction and the complete bundled skill. Tree enumeration and write/call-site searches across `src/`, `.agents/` and `.github/` supplied the omission-search basis. Test assertion scans were source inspection, not passing-test or execution evidence. No target code, examples, tests or services were executed.

I examined every declared record and annotation for referent, evidence layer, source-anchor support, status and dependencies. The runtime's components, three object containers, eight routes, two claims and two behavioral-authority paths retain distinct scopes. The memory objects and export/view routes add persistent products and concrete consumers rather than equating a storage accessor with read-back. The epistemic objects, four finer routes and two claims retain the distinction between structural checks, operational decisions and factual warrant. Workflow declares no additional records; its account and annotations extend the runtime handoffs. None of the reports declares an evidenced absence. No operation or causal support is inferred from code, confidence values, instructions or artifact names.

For the model components, the client passes caller-selected model names without parameter training or artifact pinning; clustering fits KMeans centers without training its encoder. These findings support [RT-CMP-llm-client](runtime.md#rt-cmp-llm-client) and [RT-CMP-sentence-transformer](runtime.md#rt-cmp-sentence-transformer), not conclusions about opaque provider learning. Generated domain reuse supports [RT-OBJ-domain-config](runtime.md#rt-obj-domain-config) and [RT-BAP-domain-guidance](runtime.md#rt-bap-domain-guidance) independently of parameter changes.

### Consequential routes and alternate paths

**Admission and review.** I traced parsing into cache, build into saved graph before flagging, threshold decisions into YAML, and both CLI and library application into graph mutation. This supports [RT-RTE-document-extraction](runtime.md#rt-rte-document-extraction), [RT-RTE-graph-build](runtime.md#rt-rte-graph-build), [EPI-RTE-extraction-check](epistemic.md#epi-rte-extraction-check) and [EPI-RTE-relation-flagging](epistemic.md#epi-rte-relation-flagging). Missing evidence defaults to an empty string; explicitness and quotation instructions are not enforced entailment checks. Automatic confirmation, supported file editing and build pre-deduplication are reachable alternatives to per-item human approval. Conversely, confirmed-only merge selection and rejected-relation deletion have real enforcing consumers. The reports correctly avoid both human-only admission and cosmetic-only review. The threshold-1.0 disable branch and inclusive relation-rejection comparison match [RT-RTE-review-decisions](runtime.md#rt-rte-review-decisions) and the [workflow account](workflow.md#workflow-account). Quit returns to callers that persist prior decisions; it is not rollback. Confirmed variant entries are not insertion instructions in [RT-RTE-apply-decisions](runtime.md#rt-rte-apply-decisions).

**Freshness, cost and recovery.** Cache lookup occurs before source reading and compares configuration rather than document content. A changed same-stem document is a supported countercase, not merely an unchecked type possibility. Single-document and bulk paths support the qualification of [RT-CLM-incremental-extraction](runtime.md#rt-clm-incremental-extraction). The bulk budget test precedes semaphore acquisition; summary/discovery and several narrative phases have other admission paths. Separate pipeline clients do not share a remaining balance. The runtime's best-effort cost conclusion is supported. Reconstruction reads sorted extraction files independently of current input discovery; apply does not revise those files. This supports [MEM-OBJ-document-extraction](memory.md#mem-obj-document-extraction) and the non-inverse recovery account without implying that every rebuild loses every correction.

**Confidence and transformations.** I followed mention append, support normalization on reload, product-complement arithmetic and review flagging. The same-document numerical deduction in [EPI-RTE-support-aggregation](epistemic.md#epi-rte-support-aggregation) is valid under its stated defaults; max/mean and noncanonical alternatives prevent a universal inflation claim. [MEM-OBJ-relation-support](memory.md#mem-obj-relation-support) correctly separates counts, distinct documents and selected evidence. Passive activation, normalization, schema-direction repair and pruning support [EPI-RTE-graph-cleanup](epistemic.md#epi-rte-graph-cleanup): the TRAVELED_FROM mapping changes the label without reversing endpoints, whereas known passive activation reverses them. These are code deductions, not observed errors or evidence of universal semantic preservation. Canonical fallback and unresolved direction branches substantiate the runtime's narrower schema-enforcement account.

**Retained prose and delivered context.** Independent producer/consumer tracing supports [RT-RTE-narrative-generation](runtime.md#rt-rte-narrative-generation), [MEM-OBJ-communities](memory.md#mem-obj-communities), [MEM-OBJ-entity-descriptions](memory.md#mem-obj-entity-descriptions) and [MEM-OBJ-narrative](memory.md#mem-obj-narrative). Name-keyed extraction contexts are independently reloaded; graph rejection does not withdraw them. Nonempty-only description writes and label-based community caching support local stale-sidecar possibilities. Phrase detection checks wording; its rewrite instruction is not a factual evaluator. CLI export can join descriptions, library run_export does not, and JSON bypasses that join. View loads communities relative to its destination and can compute fallback communities before metadata stripping. [MEM-RTE-export-artifacts](memory.md#mem-rte-export-artifacts) and [MEM-RTE-view-artifacts](memory.md#mem-rte-view-artifacts) therefore support distinct delivery routes, not identical projections or universal fidelity.

Query's exact-ID branch bypasses fuzzy type/DOCUMENT filtering, while neighborhood construction separately excludes metadata. Search also admits DOCUMENT matches. I traced those consumers rather than inferring response-wide filtering from a helper. [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval) and memory's annotation retain the supported distinction. Hop depth is not a token cap. [RT-CLM-second-brain](runtime.md#rt-clm-second-brain) and [RT-BAP-host-skill](runtime.md#rt-bap-host-skill) establish prescribed external consumption, not host compliance or better answers.

These checks support the [epistemic bounded conclusion](epistemic.md#bounded-conclusion): arithmetic has a bounded derivation domain; structural validity, confidence triage, storage and retrieval supply no additional factual license. Indeterminate semantic transformations are not silently classified as ampliative conjectures. The README approval and provenance claims in [EPI-CLM-merge-approval](epistemic.md#epi-clm-merge-approval) and [EPI-CLM-source-provenance](epistemic.md#epi-clm-source-provenance) are compared with their actual consumers, without attributing the separate Civic Table verification platform to sift-kg.

### Relations and reconciliation

All explicit `Part of:` relations identify material subsets: domain vocabulary/guidance within DomainConfig, assertion/support fields within graph data, parser admission within extraction, and aggregation/cleanup/flagging within build. Containers retain valid identities and need not be superseded by finer parts. The two amendments in [reconciliation](reconciliation.md#reconciliation) correctly connect extraction candidates to the memory cache object and graph support to the memory support object. Neither replaces the epistemic findings with memory's values. Narrative Markdown and description files can remain separately inventoried alongside a combined prose-warrant record because that record asserts no shared invalidation rule. The export/view/retrieval routes share inputs without being duplicates.

I checked every integration-issue disposition. Search's extra metadata exception and route-specific export enrichment qualify, rather than contradict, the runtime account. Sidecar uncertainty has no opposing fresh-state claim. No unresolved inter-report conflict, missing required part that invalidates a container, or dependent finding rendered false by supersession was identified.

### Omission searches and stopping decision

The selected questions were whether another shipped writer bypasses approval, another caller changes the budget/freshness guarantee, later projections lose support or expose metadata, and included host instructions add routes beyond ordinary question answering. Public exports and source write sites led back to the covered stages; both shipped caller families were inspected. Those searches reinforce the existing bounded conclusions rather than establish an ecosystem-wide absence. Source-native tests and example artifacts do not supply the missing causal comparison or host-session trace.

Two local inventory omissions remain. Build resolves relation endpoint names through a shared lowercase-name dictionary, not a type-qualified lookup. The reports discuss endpoint resolution and uncertain fidelity but do not separately inventory this homonym-selection mechanism. SRC-1, `src/sift_kg/graph/builder.py`:

> name_to_id[entity.name.lower().strip()] = eid
> --- `src/sift_kg/graph/builder.py`

> key = name.lower().strip()
> if key in name_to_id:
>     return name_to_id[key]
> --- `src/sift_kg/graph/builder.py`

The skill also prescribes host-side connection discovery and suggestions, beyond the selected build/review/question workflow. SRC-1, `.agents/skills/sift-kg/SKILL.md`:

> Compare the two subgraphs. Look for:
> --- `.agents/skills/sift-kg/SKILL.md`

> Prefer suggestions grounded in specific entities, communities, or structural features from the topology over generic advice.
> --- `.agents/skills/sift-kg/SKILL.md`

These omissions do not falsify emitted statuses or imply missing target-side execution: source fidelity is already unestablished, the workflow is explicitly representative, and actual external response generation is excluded. They limit finer inventory comparisons as stated below. Further optional expansion stopped because the selected challenges have supported dispositions, no identified material contradiction remains, and the reports do not claim complete algorithm, host-protocol or evaluator coverage. Browser internals, every serializer, provider internals and actual sessions remain outside the demonstrated conclusions; their uninspected behavior is not evidenced absence.

## Blockers

none

## Limits

- [RT-RTE-graph-build](runtime.md#rt-rte-graph-build), [EPI-OBJ-graph-assertions](epistemic.md#epi-obj-graph-assertions) and [EPI-CLM-source-provenance](epistemic.md#epi-clm-source-provenance) do not separately inventory build's name-only endpoint selector. SRC-1, `src/sift_kg/graph/builder.py`, assigns and resolves lowercase names without type qualification; different typed entities sharing a name can compete for that mapping. Withhold comparisons of homonym-safe endpoint attribution or complete lineage-selection coverage. Automatic graph admission and the reports' explicitly unverified source/semantic fidelity remain supported; no emitted safe-attribution value needs correction.
- [RT-BAP-host-skill](runtime.md#rt-bap-host-skill), the [workflow account](workflow.md#workflow-account) and the [epistemic route ledger](epistemic.md#authority-route-ledger) do not fully inventory the bundled skill's connection-discovery and suggestion protocols. SRC-1, `.agents/skills/sift-kg/SKILL.md`, prescribes comparing neighborhoods and proposing connections or work suggestions. Withhold complete comparisons of afforded host ideation routes or their epistemic criteria. The representative workflow and target-side extraction/review/retrieval conclusions remain valid; the instructions establish neither observed host conjectures nor accepted new graph facts.
