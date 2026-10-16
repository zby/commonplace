---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "PageIndex memory comparison: retained documents, navigation, metadata, cache inputs and caller histories, with opaque cloud alternatives."
run-id: AAS-2026-10-15-pageindex-50056ef72767-01
source-identity: https://github.com/VectifyAI/PageIndex
reviewed-boundary: af92d9658a6a9c0ae31171b43198db28951af2f4
memory-comparison:
  version: 2
  scope: >-
    Retained local pages, tree parts, metadata and manifest; alternative builder
    JSON; external heading cache; child summaries consumed by later parent calls;
    caller-held appendable transcripts; notebook outline and page-image reuse;
    and remote document memory exposed by cloud clients. Includes admission,
    maintenance and later-consumer paths. Excludes static shipped instructions,
    fixed optimizer formulae, inference weights without a recorded memory update,
    ordinary transient runner state and diagnostic logs without a later consumer.
    Remote internals, cache initialization and external history control remain
    included uncertainties, not inferred local equivalents.
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Local pages, tree, metadata/manifest, heading-cache file and alternate builder JSON"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-pages, memory.md#mem-obj-tree, memory.md#mem-obj-doc, memory.md#mem-obj-headings-cache, runtime.md#rt-rte-alternate-builders]
              note: "Operative objects are filesystem JSON; tree topology is not a graph-storage backend."
          records: [memory.md#mem-obj-pages, memory.md#mem-obj-tree, memory.md#mem-obj-doc, memory.md#mem-obj-headings-cache, runtime.md#rt-rte-alternate-builders]
          note: "These records identify each included file surface and its persistence boundary."
        - scope: "Summary values between child and parent invocations; caller-held protocol transcript values"
          assessment: known
          findings:
            - value: in-memory
              basis: wired
              records: [runtime.md#rt-rte-tree-refine, runtime.md#rt-rte-protocol-history, epistemic.md#epi-obj-node-summary]
              note: "Summary strings survive into later summary calls; appendable Python/JSON histories survive for caller reuse, without an automatic disk session store."
          records: [runtime.md#rt-rte-tree-refine, runtime.md#rt-rte-protocol-history, epistemic.md#epi-obj-node-summary]
          note: "Known for the supplied interfaces and within-run summary path, not for a host's additional persistence."
        - scope: "Vision notebook retained/fetched tree and PDF page images"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [runtime.md#rt-rte-vision-notebook]
              note: "The notebook maps selected ranges to local PDF/page-image files."
            - value: in-memory
              basis: wired
              records: [runtime.md#rt-rte-vision-notebook]
              note: "Fetched outline and selected node data are notebook variables reused by subsequent calls."
          records: [runtime.md#rt-rte-vision-notebook]
          note: "Source wiring covers notebook files/variables, not cross-session restoration."
        - scope: "Remote document objects and any caller-added transcript persistence"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-cloud-tools, runtime.md#rt-rte-protocol-history]
          note: "Remote IDs do not identify a physical substrate; hosts own any persistence beyond returned transcript values."
      records: [memory.md#mem-obj-pages, memory.md#mem-obj-tree, memory.md#mem-obj-doc, memory.md#mem-obj-headings-cache, runtime.md#rt-rte-alternate-builders, runtime.md#rt-rte-tree-refine, runtime.md#rt-rte-protocol-history, runtime.md#rt-rte-vision-notebook, runtime.md#rt-rte-cloud-tools]
      note: "Local file/value inventory is supported; remote and external persistence prevent a complete system substrate classification."
    representational_form:
      assessment: partial
      units:
        - scope: "Local extracted statements, heading titles, summaries and document descriptions at model consumers"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-pages, memory.md#mem-obj-tree, memory.md#mem-obj-doc, memory.md#mem-obj-headings-cache, epistemic.md#epi-obj-node-summary, epistemic.md#epi-obj-doc-description]
              note: "Models interpret these strings as evidence and navigation descriptions; short summaries may be copied source text."
          records: [memory.md#mem-obj-pages, memory.md#mem-obj-tree, memory.md#mem-obj-doc, memory.md#mem-obj-headings-cache, epistemic.md#epi-obj-node-summary, epistemic.md#epi-obj-doc-description]
          note: "Separates interpreted text from its addressing wrapper and fixed traversal rules."
        - scope: "Local page/node IDs, hierarchy, ranges, marker/metadata fields and heading-cache page/kind filters"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-pages, memory.md#mem-obj-tree, memory.md#mem-obj-doc, memory.md#mem-obj-headings-cache]
              note: "Localized fields drive fixed addressing, traversal, filtering and availability rules."
          records: [memory.md#mem-obj-pages, memory.md#mem-obj-tree, memory.md#mem-obj-doc, memory.md#mem-obj-headings-cache]
          note: "JSON encoding alone is not the warrant; these fields have specified code consumers."
        - scope: "Appendable protocol histories: conversation/tool text and role/tool envelopes"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [runtime.md#rt-rte-protocol-history]
              note: "Earlier conversation and tool evidence are available by value for later model context."
            - value: symbolic
              basis: wired
              records: [runtime.md#rt-rte-protocol-history]
              note: "Protocol items/messages and tool-use structure preserve typed interaction roles, subject to wrapper filtering."
          records: [runtime.md#rt-rte-protocol-history]
          note: "Classifies the exposed raw transcript path, not an unrecorded host summary or provider cache."
        - scope: "Vision notebook outline and selected node/range addressing"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [runtime.md#rt-rte-vision-notebook, epistemic.md#epi-obj-tree-structure]
              note: "The selection model interprets outline titles/descriptions."
            - value: symbolic
              basis: wired
              records: [runtime.md#rt-rte-vision-notebook]
              note: "Returned node IDs and spans control image mapping."
          records: [runtime.md#rt-rte-vision-notebook, epistemic.md#epi-obj-tree-structure]
          note: "Does not classify the consumed images by analogy with provider weights."
        - scope: "Consumed page images, arbitrary caller metadata and opaque remote retained payloads"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-vision-notebook, memory.md#mem-obj-doc, runtime.md#rt-rte-cloud-tools]
          note: "The records do not establish a controlled representational form for image content or arbitrary metadata; remote payload parts are not inventoried."
      records: [memory.md#mem-obj-pages, memory.md#mem-obj-tree, memory.md#mem-obj-doc, memory.md#mem-obj-headings-cache, epistemic.md#epi-obj-node-summary, epistemic.md#epi-obj-doc-description, runtime.md#rt-rte-protocol-history, runtime.md#rt-rte-vision-notebook, runtime.md#rt-rte-cloud-tools]
      note: "Text and fixed-rule fields are separately supported; image/opaque alternatives prevent complete form coverage. No memory-weight update is established."
    lineage:
      assessment: partial
      units:
        - scope: "Local page text acquired from submitted PDF; external cache entering the optimizer"
          assessment: known
          findings:
            - value: imported
              basis: wired
              records: [memory.md#mem-obj-pages, memory.md#mem-obj-headings-cache]
              note: "PDF extraction and cache loading acquire external document material; this says nothing about cache creation."
          records: [memory.md#mem-obj-pages, memory.md#mem-obj-headings-cache]
          note: "Known acquisition edges, distinguished from unresolved upstream provenance."
        - scope: "Generated local tree structure, summaries, metadata description and alternate builder products"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-tree, memory.md#mem-obj-doc, runtime.md#rt-rte-tree-refine, runtime.md#rt-rte-alternate-builders]
              note: "Layout, extraction, symbolic assembly and model transformations compile document inputs into navigation products; raw short-leaf reuse is a separate documented branch."
          records: [memory.md#mem-obj-tree, memory.md#mem-obj-doc, runtime.md#rt-rte-tree-refine, runtime.md#rt-rte-alternate-builders]
          note: "These derivations are document-fed, not extracted from agent experience."
        - scope: "Raw appendable protocol histories"
          assessment: known
          findings:
            - value: imported
              basis: wired
              records: [runtime.md#rt-rte-protocol-history]
              note: "A later invocation accepts caller-supplied earlier interaction material; the wrapper returns raw turns, not extracted standing memory."
          records: [runtime.md#rt-rte-protocol-history]
          note: "Import of raw history does not establish trace-extracted derivation or trace learning."
        - scope: "Initial cache production, caller metadata authorship, cloud-derived objects and notebook image derivation details"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-headings-cache, memory.md#mem-obj-doc, runtime.md#rt-rte-cloud-tools, runtime.md#rt-rte-vision-notebook]
          note: "Initial producers and remote transformations are unresolved; source-image association alone does not enumerate derivation paths."
      records: [memory.md#mem-obj-pages, memory.md#mem-obj-tree, memory.md#mem-obj-doc, memory.md#mem-obj-headings-cache, runtime.md#rt-rte-tree-refine, runtime.md#rt-rte-alternate-builders, runtime.md#rt-rte-protocol-history, runtime.md#rt-rte-cloud-tools, runtime.md#rt-rte-vision-notebook]
      note: "Known imports and document compilation coexist with unknown initial and remote provenance. No authored or trace-extracted lineage is inferred from generic caller identity."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Page text and outline/document descriptions supplied to answering or selection models"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [memory.md#mem-obj-pages, memory.md#mem-obj-tree, memory.md#mem-obj-doc, memory.md#mem-rte-document-readback, runtime.md#rt-rte-vision-notebook]
              note: "Retained content supplies evidence and navigation context; delivery does not prove compliant or correct answers."
            - value: ranking
              basis: wired
              records: [memory.md#mem-obj-tree, memory.md#mem-obj-doc, epistemic.md#epi-obj-doc-description, runtime.md#rt-rte-vision-notebook]
              note: "Descriptions and outline content influence model comparison of documents/sections for relative relevance, without a local numeric relevance scorer."
          records: [memory.md#mem-obj-pages, memory.md#mem-obj-tree, memory.md#mem-obj-doc, memory.md#mem-rte-document-readback, epistemic.md#epi-obj-doc-description, runtime.md#rt-rte-vision-notebook]
          note: "Knowledge and ranking name separate consumer effects of retained descriptive content, not policy authority."
        - scope: "Tree spans/node IDs and heading-cache page/kind data at deterministic selection consumers"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-tree, memory.md#mem-obj-headings-cache, runtime.md#rt-rte-vision-notebook]
              note: "Fields choose reconstruction windows, eligible cached headings and notebook page-image inputs."
          records: [memory.md#mem-obj-tree, memory.md#mem-obj-headings-cache, runtime.md#rt-rte-vision-notebook]
          note: "Addressing effects are separate from the semantic relevance of the chosen material."
        - scope: "Document marker and valid metadata at local store/getter consumers"
          assessment: known
          findings:
            - value: enforcement
              basis: wired
              records: [memory.md#mem-obj-doc, memory.md#mem-rte-store-maintenance]
              note: "Marker existence and recognized metadata gate future managed availability; deletion withdraws reads without recalling copies."
          records: [memory.md#mem-obj-doc, memory.md#mem-rte-store-maintenance]
          note: "The stored marker gates availability; fixed schema code is excluded static machinery rather than retained validation memory."
        - scope: "Child summaries at parent-summary consumer and raw histories at later chat consumer"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [runtime.md#rt-rte-tree-refine, epistemic.md#epi-obj-node-summary, runtime.md#rt-rte-protocol-history]
              note: "Child summaries supply document context for parent generation; reused raw turns supply prior conversational/tool context, not a durable policy update."
          records: [runtime.md#rt-rte-tree-refine, epistemic.md#epi-obj-node-summary, runtime.md#rt-rte-protocol-history]
          note: "No learning authority follows from content reaching an inference call."
        - scope: "Cloud retained parts, arbitrary host histories and caller metadata beyond documented selectors"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-cloud-tools, runtime.md#rt-rte-protocol-history, memory.md#mem-obj-doc]
          note: "Remote internals and additional host effects are unknown. Remote guidance is not shown to be an artifact accumulated through use."
      records: [memory.md#mem-obj-pages, memory.md#mem-obj-tree, memory.md#mem-obj-doc, memory.md#mem-obj-headings-cache, memory.md#mem-rte-document-readback, memory.md#mem-rte-store-maintenance, epistemic.md#epi-obj-doc-description, epistemic.md#epi-obj-node-summary, runtime.md#rt-rte-tree-refine, runtime.md#rt-rte-protocol-history, runtime.md#rt-rte-vision-notebook, runtime.md#rt-rte-cloud-tools]
      note: "Known evidence, priority, addressing and availability paths do not settle opaque alternatives. Static managed instructions and cost criteria are outside this memory scope."
    write_agency:
      assessment: partial
      units:
        - scope: "Managed local derived-document admission, summary/refinement admission and alternate builder JSON production"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-local-submit, runtime.md#rt-rte-tree-refine, runtime.md#rt-rte-alternate-builders, memory.md#mem-obj-doc]
              note: "Software/model decisions admit generated content without per-content human approval after workflow initiation."
          records: [runtime.md#rt-rte-local-submit, runtime.md#rt-rte-tree-refine, runtime.md#rt-rte-alternate-builders, memory.md#mem-obj-doc]
          note: "Caller-selected options do not make subsequent generated-content admission manual."
        - scope: "Local deletion and manifest repair inside the exposed management/store mechanisms"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-rte-store-maintenance]
              note: "Software resolves/validates removal requests and repairs manifest membership without an added per-document human confirmation."
          records: [memory.md#mem-rte-store-maintenance]
          note: "Classifies internal admission; the external actor initiating a deletion remains caller/model dependent."
        - scope: "PDF and metadata initial supply, heading-cache creation, external transcript retention and cloud admission"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-local-submit, memory.md#mem-obj-doc, memory.md#mem-obj-headings-cache, runtime.md#rt-rte-protocol-history, runtime.md#rt-rte-cloud-tools]
          note: "Generic caller identity does not establish an explicit human content decision; cache and remote admission controls are not recorded."
      records: [runtime.md#rt-rte-local-submit, runtime.md#rt-rte-tree-refine, runtime.md#rt-rte-alternate-builders, memory.md#mem-obj-doc, memory.md#mem-rte-store-maintenance, memory.md#mem-obj-headings-cache, runtime.md#rt-rte-protocol-history, runtime.md#rt-rte-cloud-tools]
      note: "Automatic downstream admission is positive evidence; unknown initialization and host/server control prevent a complete agency union."
    curation_operations:
      assessment: partial
      units:
        - scope: "Compression of retained document text and child summaries into navigation summaries/descriptions"
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [memory.md#mem-obj-tree, memory.md#mem-obj-doc, epistemic.md#epi-obj-node-summary, runtime.md#rt-rte-tree-refine]
              note: "Summary transformations reduce existing document content; parent calls also compress already derived child summaries. Short raw-text reuse is not itself compression."
          records: [memory.md#mem-obj-tree, memory.md#mem-obj-doc, epistemic.md#epi-obj-node-summary, runtime.md#rt-rte-tree-refine]
          note: "The implemented reduction is consolidation despite unmeasured faithfulness; no new claim is proven to establish synthesis."
        - scope: "Optimizer revision of an existing tree's decomposition and summary fields"
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [runtime.md#rt-rte-tree-refine, memory.md#mem-obj-tree]
              note: "Accepted children and summaries revise the tree that subsequent summary/retrieval consumers use; direct callers own final persistence."
          records: [runtime.md#rt-rte-tree-refine, memory.md#mem-obj-tree]
          note: "This is document-product revision, not revision of the optimizer's fixed method."
        - scope: "Managed local document removal"
          assessment: known
          findings:
            - value: decay
              basis: wired
              records: [memory.md#mem-rte-store-maintenance]
              note: "Explicit removal forgets the managed document for future lookups. No timed downweighting, history-preserving invalidation or universal erasure is implied."
          records: [memory.md#mem-rte-store-maintenance]
          note: "Best-effort cleanup and marker withdrawal have a bounded later-consumer effect."
        - scope: "Initial cache processing, external histories and remote maintenance alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-headings-cache, runtime.md#rt-rte-protocol-history, runtime.md#rt-rte-cloud-tools]
          note: "Unknown upstream/remote transformations prevent exhaustive curation classification. Raw transcript return and manifest rebuild alone establish no semantic curation."
      records: [memory.md#mem-obj-tree, memory.md#mem-obj-doc, epistemic.md#epi-obj-node-summary, runtime.md#rt-rte-tree-refine, memory.md#mem-rte-store-maintenance, memory.md#mem-obj-headings-cache, runtime.md#rt-rte-protocol-history, runtime.md#rt-rte-cloud-tools]
      note: "Known compression, revision and bounded forgetting coexist with opaque maintenance. Candidate duplicate rejection is not automatically deduplication of retained entries."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Local document tools/getters connected to later QA or framework consumers"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [memory.md#mem-rte-document-readback, runtime.md#rt-rte-document-chat, runtime.md#rt-rte-framework-tools]
              note: "Model/caller requests retained metadata, outline or pages; slicing a requested response is not another push operation."
          records: [memory.md#mem-rte-document-readback, runtime.md#rt-rte-document-chat, runtime.md#rt-rte-framework-tools]
          note: "Known request-led delivery covers the shipped local callbacks; actual framework use is not observed."
        - scope: "Settled child summaries automatically supplied to later parent-summary calls"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [runtime.md#rt-rte-tree-refine, epistemic.md#epi-obj-node-summary]
              note: "Scheduler progression constructs parent inputs from child summaries without a parent model requesting those particular retained strings."
          records: [runtime.md#rt-rte-tree-refine, epistemic.md#epi-obj-node-summary]
          note: "Within-run later invocation qualifies; ordinary unretained current-call state does not."
        - scope: "Vision notebook request for tree followed by automatic outline/image input assembly"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-vision-notebook]
              note: "Notebook code explicitly requests the previously generated cloud tree."
            - value: push
              basis: wired
              records: [runtime.md#rt-rte-vision-notebook]
              note: "Code supplies outline to selection call and selected retained page images to a separate answering call without that answer model requesting them."
          records: [runtime.md#rt-rte-vision-notebook]
          note: "Distinct request, selection and delivery operations are not conflated with managed tool chat."
        - scope: "Cloud client getters and tool returns"
          assessment: partial
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-cloud-tools]
              note: "Previously uploaded IDs can be requested through client getters/tool calls."
          records: [runtime.md#rt-rte-cloud-tools]
          note: "Client request wiring does not enumerate server-side automatic selection or managed-chat delivery."
        - scope: "Caller-selected protocol-history reuse and unspecified alternate JSON consumers"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-protocol-history, runtime.md#rt-rte-alternate-builders]
          note: "Appendable values afford reuse, but external selection/request ownership is unresolved; file persistence alone establishes no later consumer."
      records: [memory.md#mem-rte-document-readback, runtime.md#rt-rte-document-chat, runtime.md#rt-rte-framework-tools, runtime.md#rt-rte-tree-refine, epistemic.md#epi-obj-node-summary, runtime.md#rt-rte-vision-notebook, runtime.md#rt-rte-cloud-tools, runtime.md#rt-rte-protocol-history, runtime.md#rt-rte-alternate-builders]
      note: "Both pull and push exist locally at distinct operations. Remote and caller-owned routes prevent complete direction coverage."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Child-summary supply to parent and full-outline supply to notebook selector"
          assessment: known
          findings:
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-tree-refine, epistemic.md#epi-obj-node-summary, runtime.md#rt-rte-vision-notebook]
              note: "Parent readiness triggers supplying its children's summaries; notebook pipeline progression supplies the fetched text-free outline. These use structural availability, not a semantic match to choose relevant text."
          records: [runtime.md#rt-rte-tree-refine, epistemic.md#epi-obj-node-summary, runtime.md#rt-rte-vision-notebook]
          note: "Names the automatic stage trigger, structural input and retained material entering the next frame."
        - scope: "Vision notebook selection and delivery of retained page images"
          assessment: known
          findings:
            - value: inferred-judgment
              basis: wired
              records: [runtime.md#rt-rte-vision-notebook]
              note: "After the question/outline selector call, model relevance judgment chooses nodes whose page images enter the independent answer frame."
            - value: identifier
              basis: wired
              records: [runtime.md#rt-rte-vision-notebook]
              note: "Code matches the returned node IDs to tree nodes and maps their spans to actual delivered images; identity matching selects parts, rather than merely naming a requested file."
          records: [runtime.md#rt-rte-vision-notebook]
          note: "Judgment and subsequent ID/range mapping are separate selector mechanisms in one automatic delivery chain."
        - scope: "Local request-led discovery/structure/page responses"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-rte-document-readback]
          note: "This completely described local route fulfills requests; its page IDs, ordering and response budgets are not push signals."
        - scope: "Remote automatic delivery and caller history selection"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-cloud-tools, runtime.md#rt-rte-protocol-history]
          note: "Remote policy and external history selection are unknown; known local pull cannot make these alternatives inapplicable."
      records: [runtime.md#rt-rte-tree-refine, epistemic.md#epi-obj-node-summary, runtime.md#rt-rte-vision-notebook, memory.md#mem-rte-document-readback, runtime.md#rt-rte-cloud-tools, runtime.md#rt-rte-protocol-history]
      note: "Inspected automatic frame construction supports coarse and targeted signals; opaque alternatives remain unresolved."
    trace_learning:
      assessment: not-determinable
      units:
        - scope: "Local document-derived trees, summaries and metadata"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-obj-pages, memory.md#mem-obj-tree, memory.md#mem-obj-doc, runtime.md#rt-rte-tree-refine]
          note: "The recorded transformation inputs are document content, not activity/experience traces; these particular writes are not trace-fed learning routes."
        - scope: "Raw protocol transcripts, cache provenance, remote updates and external host reuse"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-protocol-history, memory.md#mem-obj-headings-cache, runtime.md#rt-rte-cloud-tools]
          note: "Raw trace exposure does not establish an automatic durable behavior-shaping write. Unknown cache origin, external retention and server updates prevent either a positive or a complete bounded negative."
      records: [memory.md#mem-obj-pages, memory.md#mem-obj-tree, memory.md#mem-obj-doc, runtime.md#rt-rte-tree-refine, runtime.md#rt-rte-protocol-history, memory.md#mem-obj-headings-cache, runtime.md#rt-rte-cloud-tools]
      note: "No qualifying automatic trace-fed update is established by the accepted records. No absence record closes every included write alternative, so neither a system-wide no nor yes is asserted."
    trace_source:
      assessment: not-determinable
      units:
        - scope: "Document-fed local compilation and summary routes"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-obj-pages, memory.md#mem-obj-tree, runtime.md#rt-rte-tree-refine]
          note: "Source documents are not traces in these routes; there is no qualifying trace-learning write whose input requires classification here."
        - scope: "Potential cache-origin, remote and external-history trace-fed writes"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-headings-cache, runtime.md#rt-rte-cloud-tools, runtime.md#rt-rte-protocol-history]
          note: "No qualifying update or its actual original inputs are established. Conversational/tool transcript content alone does not license session-logs or tool-traces values without a qualifying write."
      records: [memory.md#mem-obj-pages, memory.md#mem-obj-tree, runtime.md#rt-rte-tree-refine, memory.md#mem-obj-headings-cache, runtime.md#rt-rte-cloud-tools, runtime.md#rt-rte-protocol-history]
      note: "Unknown learning alternatives remain unknown source alternatives; local non-trace inputs cannot justify system-wide inapplicability."
---

# PageIndex memory profile

## Comparison rationale

This comparison uses accepted records only. It adds no evidence or records and makes no source reads. Every positive basis is implementation wiring, not observed operation, compliance, benefit or causal support. Caller-owned persistence and unavailable Cloud internals remain included limits across the axes rather than being replaced by the known local store.

The reconciliation supersedes EPI-OBJ-page-text with [MEM-OBJ-pages](memory.md#mem-obj-pages), and EPI-RTE-document-withdrawal with [MEM-RTE-store-maintenance](memory.md#mem-rte-store-maintenance). Citations use these canonical records. Tree and metadata containers remain valid alongside their more specific epistemic parts. The remaining disagreement concerns the memory issue's attribution of a broad heading-check claim to runtime, not the mechanism. Both [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine) and [MEM-OBJ-headings-cache](memory.md#mem-obj-headings-cache) distinguish cache admission from model-proposal occurrence checks. No classification depends on a universal printed-heading guarantee.

### Content and access structures have different effects

[MEM-OBJ-tree](memory.md#mem-obj-tree) separates model-interpreted headings/summaries from fixed-rule spans and node identifiers. The former provide knowledge and affect model relevance priorities; the latter route reconstruction or image selection. [MEM-OBJ-doc](memory.md#mem-obj-doc) similarly separates a descriptive selection cue from an availability marker. This does not turn document statements into instructions. Static managed prompts and fixed cost-policy source are excluded because the records do not show them accumulating or changing through use.

A model's comparison of retained descriptions can support ranking even though [MEM-RTE-document-readback](memory.md#mem-rte-document-readback) explicitly lacks local semantic-search scoring. Ranking here names the descriptions' influence at the model consumer, not a hidden vector index. None of these authority findings establishes factual endorsement or successful answer grounding.

### Reduction and revision are not trace learning

[MEM-OBJ-tree](memory.md#mem-obj-tree), [EPI-OBJ-node-summary](epistemic.md#epi-obj-node-summary) and [RT-RTE-tree-refine](runtime.md#rt-rte-tree-refine) establish compression of document content and later consumption of derived summaries. These support consolidation and tree evolution without establishing new claims, summary fidelity or improved capacity. Generated summaries are not classified as synthesis merely because entailment is unverified. Marker-first removal supports bounded forgetting, not history-preserving invalidation or recall of copies already delivered to callers ([MEM-RTE-store-maintenance](memory.md#mem-rte-store-maintenance)). Manifest repair is structural recovery, not semantic consolidation.

The summary chain qualifies as retained memory across later model invocations, but its inputs are documents, not execution traces. Conversely, [RT-RTE-protocol-history](runtime.md#rt-rte-protocol-history) exposes real raw interaction material without establishing an automatic trace-fed durable update. Unknown cache origin and server/host writes prevent a complete trace-learning negative. The profile therefore retains unresolved trace axes rather than equating lack of recorded learning with absence.

### Requests and automatic frame construction coexist

Local QA tools fulfill explicit document/page requests; response slicing does not add push. The parent-summary scheduler instead supplies already produced child summaries automatically to a later model call. The vision notebook in [RT-RTE-vision-notebook](runtime.md#rt-rte-vision-notebook) also separates requesting the tree from supplying it to a selector and delivering selected page images to a different answer call. Its semantic node selection and concrete ID-to-node mapping support distinct push signals. An ID merely carried in a requested local page response does not.

Returned transcript values support in-memory storage and later-context capability, but the records leave the caller's retention decision and actual later delivery unspecified. Likewise, alternate JSON output is a retained product without a specified later generic file consumer ([RT-RTE-alternate-builders](runtime.md#rt-rte-alternate-builders)). These limitations prevent stronger coverage assessments; they do not erase known local pull or automatic summary/notebook delivery paths.
