---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Independent verification of IWE's memory comparison classifications at commit 930c184b7cc8508d207e6ca7999ca6e415bc02ac."
run-id: AAS-2026-11-08-iwe-923f804db3b4-01
reviewed-boundary: "930c184b7cc8508d207e6ca7999ca6e415bc02ac"
---

# IWE profile verification

## Verification

I checked all ten axes in the [memory profile](memory-profile.md#comparison-rationale), including their unit scopes, controlled findings, evidence bases and coverage assessments, against the handed runtime, memory, epistemic and workflow records and annotations. I applied the reconciliation's proposal and policy-body supersessions when resolving support. The supplied profile answers are empty. No additional source inspection was needed; this judgment adds no source evidence.

**Storage and form:** The known inventories distinguish durable files from loaded graph/access structures, and natural-language payloads from symbolic control fields. [MEM-OBJ-documents](memory.md#mem-obj-documents), [RT-OBJ-graph](runtime.md#rt-obj-graph), [RT-OBJ-session-record](runtime.md#rt-obj-session-record), [MEM-OBJ-proposal](memory.md#mem-obj-proposal) and [MEM-OBJ-policy-knobs](memory.md#mem-obj-policy-knobs) support these classifications. Grouping the file-backed parts does not hide a differently classified substrate. The graph finding denotes an access structure, not a separate graph database. Excluded host weights and unsaved working copies are not silently classified as retained target memory.

**Lineage and authority:** Partial coverage is justified. Known authoring, installation, trace extraction and software bookkeeping paths do not resolve original user-content provenance. The profile preserves that distinction through [MEM-RTE-memory-enable](memory.md#mem-rte-memory-enable) and [MEM-OBJ-documents](memory.md#mem-obj-documents). Authority findings identify actual consumers: document/inbox context, interpreted policy, deterministic ranking/window selection, and checked schema admission. [RT-RTE-document-retrieval](runtime.md#rt-rte-document-retrieval), [MEM-RTE-inbox-read](memory.md#mem-rte-inbox-read), [RT-BAP-session-policy](runtime.md#rt-bap-session-policy) and [RT-BAP-schema-admission](runtime.md#rt-bap-schema-admission) support those forces without implying universal enforcement or observed host compliance. Feedback's learning authority at a policy-update consumer is distinct from the resulting policy's instruction force; [MEM-OBJ-rejected](memory.md#mem-obj-rejected) supports the afforded update path.

**Write agency and curation:** Software staging/bookkeeping and requested human selection are separate admission mechanisms, not competing descriptions of physical I/O. The automatic wired staging finding and manual afforded final-selection finding are supported by [MEM-OBJ-proposal](memory.md#mem-obj-proposal), [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) and [WF-RTE-inbox-selection](workflow.md#wf-rte-inbox-selection). Generic callers remain unresolved rather than presumed human. Consolidation, deduplication, evolution, invalidation, decay and promotion retain afforded strength. The memory annotation on [RT-RTE-policy-maintenance](runtime.md#rt-rte-policy-maintenance) supplies the policy-dependent curation distinctions, including tombstones and protected classes. [MEM-RTE-graph-restructure](memory.md#mem-rte-graph-restructure) does not upgrade requested semantic curation to wired execution. Partial coverage preserves the unresolved lower-level transformations.

**Read-back direction and signal:** Known pull and push routes are supported within the declared inventory. Requested retrieval, MCP context and inbox responses are pull; independently selected session-start discovery output is push. [RT-RTE-session-index](runtime.md#rt-rte-session-index) and its memory annotation establish conditional metadata/policy output, including the no-groups guard. Its filters, sort and budgets support coarse selection, not task-relevance selection. Requested keys and lexical search in [RT-RTE-document-retrieval](runtime.md#rt-rte-document-retrieval) do not establish identifier or lexical push. External invocation/delivery uncertainty does not obscure the implemented selector's direction or signal.

**Trace learning and source:** The afforded positive has a complete qualifying chain: conversation/tool experience feeds automatic proposal admission, durable proposals survive interruption, and later inbox consumers receive their bodies/evidence as context. [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [MEM-OBJ-proposal](memory.md#mem-obj-proposal) and [MEM-RTE-inbox-read](memory.md#mem-rte-inbox-read) support this before final document admission. A candidate need not be accepted as fact or demonstrate improvement to qualify. Conversely, user-confirmed document/policy writes do not themselves establish automatic trace learning. The profile correctly leaves generic alternatives unresolved, emits no unsupported negative, and keeps both axes partial. The capture annotation supports session-log and tool-trace inputs; serialization alone adds neither event streams nor trajectories.

The records' apparent tensions are preserved rather than flattened: procedural user selection is not an all-write invariant; retained provenance is not necessarily delivered by ordinary retrieval; grouped inbox output is not full evidence; bookkeeping is not authenticated feedback; and helper output is not observed model receipt. These qualifications leave the emitted comparison findings valid. Existing unresolved scopes are faithfully expressed in the profile rather than defects requiring a separate publication limit. I found no materially unsupported value, evidence-strength upgrade or complete-coverage assertion.

## Blockers

none

## Limits

none
