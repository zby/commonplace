---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "IWE memory comparison: durable documents, revisable policy, capture inbox and later context routes."
run-id: AAS-2026-11-08-iwe-923f804db3b4-01
source-identity: https://github.com/iwe-org/iwe
reviewed-boundary: "930c184b7cc8508d207e6ca7999ca6e415bc02ac"
memory-comparison:
  version: 2
  scope: >-
    Accumulated workspace documents, revisable MEMORY body and knobs, installed
    schema criteria when maintained, durable proposals, rejection feedback and
    session progress, plus their loaded graph/access structures and later
    CLI/MCP/helper consumers. Includes host-mediated capture and maintenance
    alternatives at their recorded evidence strength. Excludes unchanged shipped
    instructions as memory, ordinary unsaved working context, external host model
    state and host-owned raw transcript storage. Transcripts remain inputs to
    included trace-fed writes. Actual user content, original admissions and some
    lower-level maintenance transformations are unresolved.
  axes:
    storage_substrate:
      assessment: known
      units:
        - scope: "Durable documents, policy body/knobs and installed schema configuration"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-documents, memory.md#mem-rte-memory-enable, epistemic.md#epi-obj-learning-schema]
              note: "Workspace files retain documents and installed policy/schema machinery; no repository-backed memory mechanism is established merely by the source being a Git repository."
          records: [memory.md#mem-obj-documents, memory.md#mem-obj-policy-body, memory.md#mem-obj-policy-knobs, memory.md#mem-rte-memory-enable, epistemic.md#epi-obj-learning-schema]
          note: "The recorded durable object inventory uses filesystem persistence, including caller-supplied policy alternatives."
        - scope: "Session bookkeeping, proposal bodies/evidence and rejection strings"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [runtime.md#rt-obj-session-record, memory.md#mem-obj-proposal, memory.md#mem-obj-rejected]
              note: "YAML session files outside the document graph retain these parts."
          records: [runtime.md#rt-obj-session-record, memory.md#mem-obj-proposal, memory.md#mem-obj-rejected]
          note: "Readable summaries and full proposal evidence share the declared file-backed object, not an opaque provider payload."
        - scope: "Loaded document graph and its key/edge access structures"
          assessment: known
          findings:
            - value: graph
              basis: wired
              records: [runtime.md#rt-obj-graph]
              note: "Parsed document keys and edges form the operative graph access structure."
            - value: in-memory
              basis: wired
              records: [runtime.md#rt-obj-graph]
              note: "CLI reconstructs the graph; MCP retains it in process memory under a lock."
          records: [runtime.md#rt-obj-graph, runtime.md#rt-rte-editor-reload]
          note: "Only the durable-memory access role is included; unsaved editor working copies are not additional retained memory."
      records: [memory.md#mem-obj-documents, memory.md#mem-rte-memory-enable, epistemic.md#epi-obj-learning-schema, runtime.md#rt-obj-session-record, runtime.md#rt-obj-graph]
      note: "Records account for filesystem backing, session bookkeeping and loaded graph structures across the scoped inventory; unknown content does not obscure these substrates."
    representational_form:
      assessment: known
      units:
        - scope: "Document prose, MEMORY body, proposal title/body/evidence and rejection feedback at human/model consumers"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-documents, memory.md#mem-obj-policy-body, memory.md#mem-obj-proposal, memory.md#mem-obj-rejected, memory.md#mem-rte-inbox-read]
              note: "Readable text is retained and exposed for interpretation; this finding concerns content/output, not observed host compliance."
          records: [memory.md#mem-obj-documents, memory.md#mem-obj-policy-body, memory.md#mem-obj-proposal, memory.md#mem-obj-rejected]
          note: "The recorded prose parts have no hidden numerical payload behind their displays."
        - scope: "Parsed keys/edges/fields, session status and progress, policy settings and installed schema predicates"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [runtime.md#rt-obj-graph, runtime.md#rt-obj-session-record, memory.md#mem-obj-policy-knobs, epistemic.md#epi-obj-learning-schema]
              note: "Fixed code consumes localized identities, counters, settings and predicates."
          records: [runtime.md#rt-obj-graph, runtime.md#rt-obj-session-record, memory.md#mem-obj-policy-knobs, epistemic.md#epi-obj-learning-schema]
          note: "Separates symbolic control and access fields from their natural-language payloads."
      records: [memory.md#mem-obj-documents, memory.md#mem-obj-policy-body, memory.md#mem-obj-proposal, memory.md#mem-obj-rejected, runtime.md#rt-obj-graph, runtime.md#rt-obj-session-record, memory.md#mem-obj-policy-knobs, epistemic.md#epi-obj-learning-schema]
      note: "Complete for the declared target-owned memory parts, not a classification of excluded host weights or arbitrary dependency internals."
    lineage:
      assessment: partial
      units:
        - scope: "Caller note authoring and shipped/custom policy installation paths"
          assessment: known
          findings:
            - value: authored
              basis: afforded
              records: [memory.md#mem-obj-documents, runtime.md#rt-rte-cli-document]
              note: "Callers can author retained project notes; authorship does not identify their admission principal."
            - value: imported
              basis: wired
              records: [memory.md#mem-rte-memory-enable, memory.md#mem-obj-policy-body, memory.md#mem-obj-policy-knobs]
              note: "Enable installs shipped or supplied policy and configuration into the workspace."
          records: [memory.md#mem-obj-documents, memory.md#mem-rte-memory-enable]
          note: "Classifies these explicit derivation paths, not every existing document's origin."
        - scope: "Transcript-to-proposal and selected transcript-derived document paths"
          assessment: known
          findings:
            - value: trace-extracted
              basis: afforded
              records: [runtime.md#rt-rte-session-capture, memory.md#mem-obj-proposal, memory.md#mem-obj-documents]
              note: "The host is instructed to extract quotable facts/rules from conversations, stage them and write selected documents."
          records: [runtime.md#rt-rte-session-capture, memory.md#mem-obj-proposal]
          note: "Semantic extraction is afforded, not a server-side model implementation or an observed provenance claim."
        - scope: "Software-derived proposal status, capture/progress and rejection bookkeeping"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [runtime.md#rt-obj-session-record, memory.md#mem-obj-proposal, memory.md#mem-obj-rejected, memory.md#mem-rte-session-adopt]
              note: "Code derives statuses, progress and swept rejection titles from supplied entries and completion/adoption actions."
          records: [runtime.md#rt-obj-session-record, memory.md#mem-obj-rejected, memory.md#mem-rte-session-adopt]
          note: "This derivation does not authenticate an underlying human answer or establish that an adopted session was read."
        - scope: "Preexisting user documents, custom policy/schema content and other maintenance derivations"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-documents, memory.md#mem-rte-memory-enable, memory.md#mem-rte-graph-restructure]
          note: "Original content provenance and lower-level transformation details are not established; known installation does not resolve source authorship."
      records: [memory.md#mem-obj-documents, memory.md#mem-rte-memory-enable, runtime.md#rt-rte-session-capture, runtime.md#rt-obj-session-record, memory.md#mem-obj-rejected, memory.md#mem-rte-graph-restructure]
      note: "Known paths coexist with unresolved original and alternative derivations; no exhaustive lineage union is warranted."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Document and proposal prose/evidence supplied to requested later readers"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [runtime.md#rt-rte-document-retrieval, memory.md#mem-rte-mcp-context, memory.md#mem-rte-inbox-read]
              note: "Bodies and candidate evidence supply reference/context, not certified truth; grouped inbox omits evidence."
          records: [memory.md#mem-obj-documents, memory.md#mem-obj-proposal, memory.md#mem-rte-inbox-read, runtime.md#rt-rte-document-retrieval]
          note: "Wired output is distinct from host receipt or reliance; full resource text is a separate projection."
        - scope: "Retained policy body at proposing, curating and later session-start agents"
          assessment: known
          findings:
            - value: instruction
              basis: afforded
              records: [memory.md#mem-obj-policy-body, runtime.md#rt-bap-session-policy, runtime.md#rt-rte-policy-maintenance]
              note: "Policy supplies standing guidance if the external host delivers and interprets it; helper output alone does not establish deployed model receipt."
          records: [memory.md#mem-obj-policy-body, runtime.md#rt-bap-session-policy]
          note: "Whole-body brief reads and the conditional At session start projection have different delivery coverage."
        - scope: "Retained fields, text and keys at deterministic selection/ranking consumers"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [runtime.md#rt-rte-document-retrieval, runtime.md#rt-rte-session-index, epistemic.md#epi-rte-post-tool]
              note: "Retained text supplies lexical ranking/similarity inputs; retained sort fields determine index priority."
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-policy-knobs, runtime.md#rt-obj-session-record, memory.md#mem-rte-session-adopt, runtime.md#rt-rte-session-index]
              note: "Knobs select input windows and index scope; saved progress selects the next transcript span."
          records: [memory.md#mem-obj-policy-knobs, runtime.md#rt-obj-session-record, runtime.md#rt-rte-document-retrieval, runtime.md#rt-rte-session-index]
          note: "Selection influence is not authorization or semantic endorsement."
        - scope: "Installed/maintained schema criteria at checked pending-write handlers"
          assessment: known
          findings:
            - value: validation
              basis: wired
              records: [epistemic.md#epi-obj-learning-schema, epistemic.md#epi-rte-schema-check, runtime.md#rt-bap-schema-admission]
              note: "Bound schema predicates determine structural conformance."
            - value: enforcement
              basis: wired
              records: [runtime.md#rt-bap-schema-admission, runtime.md#rt-rte-cli-document, runtime.md#rt-rte-mcp-document]
              note: "Violation results veto checked writes; strict CLI is optional and this is not an all-write invariant."
          records: [epistemic.md#epi-obj-learning-schema, runtime.md#rt-bap-schema-admission]
          note: "Only criteria retained for later writes are in scope; unchanged shipped samples alone are not accumulated memory."
        - scope: "Proposals and rejection feedback at durable document/policy update consumers"
          assessment: known
          findings:
            - value: learning
              basis: afforded
              records: [memory.md#mem-obj-proposal, memory.md#mem-obj-rejected, runtime.md#rt-rte-session-capture, runtime.md#rt-rte-policy-maintenance]
              note: "Retained experience and feedback can feed durable fact/rule and standing-policy revisions, under requested user selection/confirmation; no improved capacity is established."
          records: [memory.md#mem-obj-proposal, memory.md#mem-obj-rejected, runtime.md#rt-rte-policy-maintenance]
          note: "Update-consumer force differs from the downstream knowledge/instruction force of resulting artifacts."
        - scope: "Actual custom document/policy/schema content and remaining maintenance consumers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-documents, memory.md#mem-rte-memory-enable, memory.md#mem-rte-graph-restructure]
          note: "Uninspected deployed meanings and lower-level alternate routes prevent exhaustively identifying all content-dependent effects."
      records: [runtime.md#rt-rte-document-retrieval, memory.md#mem-rte-inbox-read, memory.md#mem-obj-policy-body, memory.md#mem-obj-policy-knobs, runtime.md#rt-bap-schema-admission, memory.md#mem-obj-rejected, memory.md#mem-rte-graph-restructure]
      note: "Each force belongs to a named retained part and consumer; supported witnesses do not resolve all deployed content or alternate effects."
    write_agency:
      assessment: partial
      units:
        - scope: "Proposal staging and session completion/adoption bookkeeping"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-obj-proposal, memory.md#mem-obj-rejected, memory.md#mem-rte-session-adopt, runtime.md#rt-rte-session-capture]
              note: "Software admits staged entries and derives status/progress/rejection changes without a per-content human approval test."
          records: [memory.md#mem-obj-proposal, memory.md#mem-obj-rejected, memory.md#mem-rte-session-adopt]
          note: "A user starting capture does not make downstream staging manually admitted."
        - scope: "Selected fact writes and confirmed reflect/policy edits under the shipped host procedure"
          assessment: known
          findings:
            - value: manual
              basis: afforded
              records: [runtime.md#rt-rte-session-capture, runtime.md#rt-rte-policy-maintenance, workflow.md#wf-rte-inbox-selection]
              note: "The procedure requires a named remember instruction, keep/edit choice or confirmation for the retained content; this is not enforced by storage APIs."
          records: [runtime.md#rt-rte-session-capture, runtime.md#rt-rte-policy-maintenance]
          note: "Classifies the human decision in this admission mechanism, not the agent's physical I/O."
        - scope: "Initial content/enable and ordinary CLI/MCP/editor or structural-maintenance caller admissions"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-memory-enable, runtime.md#rt-rte-cli-document, runtime.md#rt-rte-mcp-document, runtime.md#rt-rte-editor-reload, memory.md#mem-rte-graph-restructure]
          note: "Generic caller identity does not distinguish a human supplying content from a model making the admission decision. Schema gates alone do not settle agency."
      records: [memory.md#mem-obj-proposal, memory.md#mem-obj-rejected, memory.md#mem-rte-session-adopt, runtime.md#rt-rte-session-capture, runtime.md#rt-rte-policy-maintenance, memory.md#mem-rte-memory-enable, runtime.md#rt-rte-cli-document, runtime.md#rt-rte-mcp-document]
      note: "Automatic intermediate admission and manual procedural selection coexist with unresolved generic caller control."
    curation_operations:
      assessment: partial
      units:
        - scope: "Host transcript extraction and evidence-preserving inbox merging"
          assessment: known
          findings:
            - value: consolidate
              basis: afforded
              records: [runtime.md#rt-rte-session-capture, workflow.md#wf-rte-inbox-selection, memory.md#mem-obj-proposal]
              note: "The host is asked to compress conversation facts and combine same-target candidates; raw traces need not be deleted."
          records: [runtime.md#rt-rte-session-capture, workflow.md#wf-rte-inbox-selection]
          note: "Instruction supports an afforded transformation, not observed semantic fidelity or a wired model extractor."
        - scope: "Policy-governed semantic maintenance and feedback revision"
          assessment: known
          findings:
            - value: dedup
              basis: afforded
              records: [runtime.md#rt-rte-policy-maintenance, runtime.md#rt-rte-session-capture]
              note: "Same-fact merging and removal are requested after semantic comparison, not established merely by similarity scores."
            - value: evolve
              basis: afforded
              records: [runtime.md#rt-rte-policy-maintenance, memory.md#mem-obj-rejected]
              note: "Confirmed updates revise existing facts and standing capture guidance."
            - value: invalidate
              basis: afforded
              records: [runtime.md#rt-rte-policy-maintenance]
              note: "Tombstones retain entries while directing later curation passes to exclude superseded items; no universal retrieval veto follows."
            - value: decay
              basis: afforded
              records: [runtime.md#rt-rte-policy-maintenance]
              note: "Typed-policy bounded age pruning affords forgetting with protected classes; starter policy does not allow age pruning."
            - value: promote
              basis: afforded
              records: [runtime.md#rt-rte-policy-maintenance]
              note: "Typed-policy topic promotion raises organization/salience through a requested maintenance operation."
          records: [runtime.md#rt-rte-policy-maintenance, memory.md#mem-obj-rejected]
          note: "These are policy-dependent host procedures, not automatic lifecycle guarantees."
        - scope: "Lower-level extract/inline and remaining structural maintenance transformations"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-graph-restructure, epistemic.md#epi-rte-link-cleanup]
          note: "Rename/normalization and link cleanup do not by themselves establish a listed semantic curation value; incomplete lower-level inspection prevents resolving all transformations. Novel claims are not established."
      records: [runtime.md#rt-rte-session-capture, workflow.md#wf-rte-inbox-selection, runtime.md#rt-rte-policy-maintenance, memory.md#mem-rte-graph-restructure, epistemic.md#epi-rte-link-cleanup]
      note: "Supported host operations remain afforded; deterministic structural edits do not upgrade them or establish synthesis."
    read_back_direction:
      assessment: known
      units:
        - scope: "Requested CLI document retrieval, MCP contexts/resources and resumed inbox/brief reads"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-document-retrieval, memory.md#mem-rte-mcp-context, memory.md#mem-rte-inbox-read, memory.md#mem-obj-rejected]
              note: "A consumer requests retained material; server projection and graph expansion fulfill that request rather than adding an independent push."
          records: [runtime.md#rt-rte-document-retrieval, memory.md#mem-rte-mcp-context, memory.md#mem-rte-inbox-read, memory.md#mem-obj-rejected]
          note: "Wired responses establish later-consumer output routes, not model receipt or full evidence delivery in every projection."
        - scope: "Invoked session-start discovery helper"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [runtime.md#rt-rte-session-index, memory.md#mem-obj-policy-knobs, memory.md#mem-obj-policy-body]
              note: "Once triggered, code selects metadata and the policy section without a consumer request for those specific retained items; output requires nonempty groups."
          records: [runtime.md#rt-rte-session-index, memory.md#mem-obj-policy-knobs, memory.md#mem-obj-policy-body]
          note: "Helper selection/output is wired; external plugin invocation and delivery to a host model remain unobserved."
      records: [runtime.md#rt-rte-document-retrieval, memory.md#mem-rte-mcp-context, memory.md#mem-rte-inbox-read, runtime.md#rt-rte-session-index, memory.md#mem-obj-rejected]
      note: "The accepted route inventory covers requested document/candidate/feedback reads and automatic discovery. Host delivery uncertainty does not obscure their direction."
    read_back_signal:
      assessment: known
      units:
        - scope: "Session-start slice metadata and fixed policy-section projection"
          assessment: known
          findings:
            - value: coarse
              basis: wired
              records: [runtime.md#rt-rte-session-index, memory.md#mem-obj-policy-knobs, memory.md#mem-obj-policy-body]
              note: "Trigger is the invoked session-start helper; selector inputs are policy slice filters, retained fields/sort, already-emitted keys and budgets; selected parts are title/key/sort metadata and the fixed At session start section. No task relevance or identity match selects a targeted document for push."
          records: [runtime.md#rt-rte-session-index, memory.md#mem-obj-policy-knobs, memory.md#mem-obj-policy-body]
          note: "Dedup keys prevent repeats, not identity-targeted supply; fixed machinery exclusion and named policy extraction are part of this coarse discovery projection."
      records: [runtime.md#rt-rte-session-index, memory.md#mem-obj-policy-knobs, runtime.md#rt-rte-document-retrieval, memory.md#mem-rte-mcp-context, memory.md#mem-rte-inbox-read]
      note: "Classifies the sole recorded independent push chain; lexical search, explicit keys and graph expansion on requested reads are pull selectors, not additional push signals."
    trace_learning:
      assessment: partial
      units:
        - scope: "Unselected transcript-derived proposal staging followed by later inbox consumption"
          assessment: known
          findings:
            - value: "yes"
              basis: afforded
              records: [runtime.md#rt-rte-session-capture, memory.md#mem-obj-proposal, memory.md#mem-rte-inbox-read, workflow.md#wf-rte-inbox-selection]
              note: "The host can extract conversation/tool experience into durable staged fact/rule candidates without per-candidate human approval; later resumed readers receive their bodies/evidence as context. This qualifies before final user-selected document admission."
          records: [runtime.md#rt-rte-session-capture, memory.md#mem-obj-proposal, memory.md#mem-rte-inbox-read]
          note: "The extraction-to-later-context chain is afforded; staging/persistence and requested read-back are wired. Neither exercised extraction nor improved capacity is inferred."
        - scope: "Selected final-document writes, rejection-ledger-driven policy revisions and generic alternate write paths"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-session-capture, memory.md#mem-obj-rejected, runtime.md#rt-rte-policy-maintenance, runtime.md#rt-rte-cli-document, runtime.md#rt-rte-mcp-document, memory.md#mem-rte-graph-restructure]
          note: "The named host procedure requires human selection/confirmation for final documents and policy edits, so those writes do not establish an automatic trace-fed route. Generic caller paths and actual initial content remain unresolved; no bounded absence record warrants a local no."
      records: [runtime.md#rt-rte-session-capture, memory.md#mem-obj-proposal, memory.md#mem-rte-inbox-read, memory.md#mem-obj-rejected, runtime.md#rt-rte-policy-maintenance, runtime.md#rt-rte-mcp-document]
      note: "A supported automatic staging witness yields yes at afforded strength while unresolved alternate admissions prevent complete coverage; there is no system-wide negative."
    trace_source:
      assessment: partial
      units:
        - scope: "Original input to transcript-derived proposal staging"
          assessment: known
          findings:
            - value: session-logs
              basis: afforded
              records: [runtime.md#rt-rte-session-capture, memory.md#mem-obj-proposal]
              note: "Recorded user/assistant conversational turns, including visible thinking, can feed staged facts/rules via the lossy digest."
            - value: tool-traces
              basis: afforded
              records: [runtime.md#rt-rte-session-capture, memory.md#mem-obj-proposal]
              note: "Recorded tool calls/results and execution errors survive in clipped form as inputs to the same proposing route."
          records: [runtime.md#rt-rte-session-capture, memory.md#mem-obj-proposal]
          note: "JSONL serialization does not add event-streams; recorded conversations with tool observations do not by themselves establish linked state/action/outcome trajectories. Live current-session context is an alternative conversational source, not evidence of a different recorded source class."
        - scope: "Potential qualifying writes through generic document and alternate maintenance admission"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-documents, runtime.md#rt-rte-cli-document, runtime.md#rt-rte-mcp-document, memory.md#mem-rte-graph-restructure]
          note: "Unresolved admission principals and content origin prevent identifying whether additional automatic trace-fed writes exist or what original inputs they consume."
      records: [runtime.md#rt-rte-session-capture, memory.md#mem-obj-proposal, memory.md#mem-obj-documents, runtime.md#rt-rte-mcp-document, memory.md#mem-rte-graph-restructure]
      note: "Both supported sources belong to the qualifying staging chain; unresolved alternate learning inventory remains unresolved here rather than inapplicable."
---

# IWE memory profile

## Comparison rationale

The comparison concerns reusable retained content and access structures, not every
runtime file. The workspace graph is both an in-memory representation and a graph
access structure over file-backed documents. It is not evidence of a separate
graph database. The serialized proposal/rejection store is outside that graph.
See [RT-OBJ-graph](runtime.md#rt-obj-graph),
[MEM-OBJ-documents](memory.md#mem-obj-documents) and
[RT-OBJ-session-record](runtime.md#rt-obj-session-record).

Canonical citations follow the reconciliation's two supersessions: the epistemic
proposal and policy-body declarations resolve to
[MEM-OBJ-proposal](memory.md#mem-obj-proposal) and
[MEM-OBJ-policy-body](memory.md#mem-obj-policy-body). These amendments change no
classification. The narrower injection mapping remains distinct from the broader
[MEM-OBJ-policy-knobs](memory.md#mem-obj-policy-knobs); it is not treated as a
duplicate or an opaque alternative.

Staging is the consequential automatic admission witness. The host is instructed
to extract conversation evidence and software admits proposals without a human
selection test. Durable candidates then return through later inbox invocations.
That chain supports afforded trace learning even if no final document is selected:
a retained continuation context can qualify without successful improvement or a
new scientific claim. Final selected document writes and confirmed policy edits
instead have manual admission at afforded strength. Code persistence is not an
independent automatic semantic extractor. The unresolved generic caller paths
preclude an inventory-wide negative or complete learning assessment. See
[RT-RTE-session-capture](runtime.md#rt-rte-session-capture),
[MEM-RTE-inbox-read](memory.md#mem-rte-inbox-read) and
[WF-RTE-inbox-selection](workflow.md#wf-rte-inbox-selection).

Rejection feedback can influence a durable policy revision and thus has learning
authority at that update consumer. That does not make the user-confirmed revision
an automatic trace-learning write. The edited policy's later force is instruction
at the external interpreter and routing at the symbolic settings consumer.
Neither policy loading nor rejection counts establish actual criticism, genuine
user feedback, or improved capacity. See
[MEM-OBJ-rejected](memory.md#mem-obj-rejected) and
[RT-RTE-policy-maintenance](runtime.md#rt-rte-policy-maintenance).

Curation values classify requested host transformations at afforded strength.
Semantic compression into standing facts supports consolidation without asserting
entailed derivation or novel synthesis. Normalization, rename and graph cleanup
alone do not establish those semantic operations. Uninspected lower-level edits
remain included and unresolved. See
[MEM-RTE-graph-restructure](memory.md#mem-rte-graph-restructure) and
[EPI-RTE-link-cleanup](epistemic.md#epi-rte-link-cleanup).

Read direction and signal are known for the recorded routes even though deployed
host delivery is not observed. Session-start selection is coarse push, conditional
on invocation and nonempty output groups; it emits metadata and a fixed policy
section, not all document bodies. Explicit keys and lexical search serve pull
requests, not identifier or inferred-lexical push. The grouped inbox also omits
candidate evidence, which requires a full session inbox request. See
[RT-RTE-session-index](runtime.md#rt-rte-session-index),
[RT-RTE-document-retrieval](runtime.md#rt-rte-document-retrieval) and
[MEM-RTE-inbox-read](memory.md#mem-rte-inbox-read).

No source files were read for this classification. All warrants come from the
supplied accepted records and their annotations. Unknown deployed content,
initial provenance/control, lower-level maintenance semantics and host receipt
remain beside the affected assessments; no observation or causal benefit is
claimed.
