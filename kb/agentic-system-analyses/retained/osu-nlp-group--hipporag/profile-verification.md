---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Independent verification of HippoRAG's memory profile against the handed accepted records at the frozen revision."
run-id: AAS-2026-10-16-hipporag-2b37edfc7ade-01
reviewed-boundary: d5c8329422e0a0b834a15874545cb6a74b4f9b26
---

# HippoRAG profile verification

## Verification

I checked all ten axes in the [memory profile](memory-profile.md#comparison-rationale), including their unit scopes, positive findings, evidence bases and coverage assessments, against the handed runtime, memory, epistemic and workflow records. I applied the supplied reconciliation: the duplicate epistemic passage object resolves to the memory passage object; the OpenIE container, relation content, normalized strings, vectors and graph remain distinct. The profile uses the canonical passage record and does not turn overlapping routes into duplicate evidence. No refusal or substantive correction answers were supplied. No source reads were needed, and this judgment adds no source evidence.

The compared boundary is retained document/search state and its later consumers, not all runtime state. Excluding static shipped instructions, external model weights, ordinary current-call thoughts and benchmark results without retained consumers is consistent with the records. Including the manifest, response cache and prepared-instance query reuse is also justified: these retained parts affect subsequent operations. The profile preserves unresolved alternative caches and injected implementations rather than extending the default implementation's classifications to them. None of its axes asserts complete system-wide coverage.

### Storage, form and lineage

The default file, process-memory, vector, graph and SQLite findings follow the separated retained objects. The graph's pickle persistence is not confused with its operative graph structure; stored vectors are not classified as updated model weights. The alternate collection finding stays partial and does not infer an additional database category from a backend name. Supporting records include [MEM-OBJ-passage-text](memory.md#mem-obj-passage-text), [MEM-OBJ-passage-embeddings](memory.md#mem-obj-passage-embeddings), [MEM-OBJ-entity-embeddings](memory.md#mem-obj-entity-embeddings), [MEM-OBJ-fact-embeddings](memory.md#mem-obj-fact-embeddings), [MEM-OBJ-graph-state](memory.md#mem-obj-graph-state) and [MEM-OBJ-response-cache](memory.md#mem-obj-response-cache).

Form units distinguish lexical interpretation, fixed-rule identity/schema consumption and distributed numerical representation. In particular, the same normalized labels can have natural-language and symbolic consumption paths without implying two independently retained objects. The cache message is the replayed payload, not a readable proxy for opaque weights. The symbolic metadata unit explicitly covers mapping/identity consumers, not arbitrary payload meaning. See [MEM-OBJ-entity-text](memory.md#mem-obj-entity-text), [MEM-OBJ-fact-text](memory.md#mem-obj-fact-text), [MEM-OBJ-openie-state](memory.md#mem-obj-openie-state), [MEM-OBJ-chunk-metadata](memory.md#mem-obj-chunk-metadata) and [MEM-RTE-response-reuse](memory.md#mem-rte-response-reuse).

Imported passage/metadata lineage and other-compiled search representations are supported as local paths. The known derivation units do not claim known original authorship, trace provenance or immutable encoder identity. Cached model output is not classified as trace-extracted merely because it is logged and replayed. The partial lineage assessment retains these distinctions; see [RT-RTE-index-state](runtime.md#rt-rte-index-state), [RT-RTE-offline-extraction](runtime.md#rt-rte-offline-extraction), [RT-RTE-standard-rag](runtime.md#rt-rte-standard-rag) and [MEM-OBJ-response-cache](memory.md#mem-obj-response-cache).

### Authority, admission and curation

Knowledge, ranking, routing, validation and enforcement findings name supported consumers and effects. Passage context is not an enforced instruction hierarchy; fact/vector/graph ranking does not require a learned ranking policy. Source-ID deletion targeting is routing rather than authorization. The manifest supplies both compatibility criteria and a veto, so its validation and enforcement findings coexist. Host answering remains claimed rather than upgraded from server delivery to host compliance. See [MEM-OBJ-passage-text](memory.md#mem-obj-passage-text), [MEM-OBJ-graph-state](memory.md#mem-obj-graph-state), [MEM-OBJ-chunk-metadata](memory.md#mem-obj-chunk-metadata), [RT-OBJ-index-manifest](runtime.md#rt-obj-index-manifest), [RT-CLM-state-compatibility](runtime.md#rt-clm-state-compatibility) and [RT-BAP-plugin-skills](runtime.md#rt-bap-plugin-skills).

Admission units appropriately separate unresolved generic caller control from automatic downstream extraction, structural admission, encoding and caching. The claimed manual finding is limited to the explicit user confirmation/refresh checkpoint in [WF-RTE-folder-indexing](workflow.md#wf-rte-folder-indexing); it does not make the subsequent model/software writes manual. The automatic findings are supported by [RT-RTE-index-state](runtime.md#rt-rte-index-state), [EPI-RTE-triple-admission](epistemic.md#epi-rte-triple-admission) and [MEM-RTE-response-reuse](memory.md#mem-rte-response-reuse).

The curation mappings follow transformations rather than command names. Extraction reduces retained passage material to source-linked entities/relations, supporting consolidation without establishing semantic faithfulness or synthesis. Explicit tuple duplicate removal supports deduplication independently of primary-key collision checks. Existing metadata replacement supports evolution; removal of source contributions supports forgetting/decay, not retained-history invalidation or secure erasure. The supporting records are [EPI-RTE-openie-generation](epistemic.md#epi-rte-openie-generation), [EPI-RTE-triple-admission](epistemic.md#epi-rte-triple-admission), [EPI-RTE-text-normalization](epistemic.md#epi-rte-text-normalization), [MEM-OBJ-chunk-metadata](memory.md#mem-obj-chunk-metadata) and [RT-RTE-index-state](runtime.md#rt-rte-index-state). The epistemic report's indeterminate entailment assessment does not contradict these implemented curation findings.

### Read-back and trace routes

The established retrieval, QA, maintenance reload and exact-request replay operations fulfill requests for retained material. Internal automatic scoring and delivery do not independently establish unsolicited push. Consequently the known units support pull, while the partial direction axis leaves alternate routes unresolved. Push-signal classifications are locally inapplicable for assessed pull chains, but not globally inapplicable across unresolved alternatives. The profile correctly refrains from assigning inferred-embedding, inferred-judgment or identifier push signals merely from the selectors' implementation. See [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer), [RT-RTE-ircot-retrieval](runtime.md#rt-rte-ircot-retrieval), [RT-RTE-mcp-tools](runtime.md#rt-rte-mcp-tools) and [MEM-RTE-response-reuse](memory.md#mem-rte-response-reuse).

Neither trace axis emits a positive or negative controlled value. The accepted records establish automatic document-derived writes and later consumers, but not qualifying trace origins for arbitrary admitted inputs. Raw response replay alone does not establish a derived trace-fed update. Current-call thoughts and post-generation metric reporting do not provide a retained update consumer. There is no canonical bounded-absence record licensing a controlled trace-learning no or globally inapplicable trace source. The not-determinable assessments therefore preserve the supported architecture without claiming absent learning or demanding observed improvement for a wired classification. See [MEM-OBJ-passage-text](memory.md#mem-obj-passage-text), [MEM-OBJ-openie-state](memory.md#mem-obj-openie-state), [MEM-RTE-response-reuse](memory.md#mem-rte-response-reuse), [RT-RTE-ircot-retrieval](runtime.md#rt-rte-ircot-retrieval) and [EPI-RTE-metric-evaluation](epistemic.md#epi-rte-metric-evaluation).

Some units group objects or calls with the same classification and coverage. I found no grouping that upgrades an unresolved alternative, conceals a materially different emitted value or turns the partial inventories into complete enumeration. Recorded uncertainty about alternative adapters, metadata meaning, initial admission and trace origins is already expressed in the profile's assessments and notes. It is not an additional verification defect. All positive findings remain wired or claimed as supported; none asserts observed operation or causal benefit.

## Blockers

none

## Limits

none
