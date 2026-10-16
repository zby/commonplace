---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "Smriti MCP memory comparison: retained Markdown, metadata, raw traces and derived access structures at the frozen revision."
run-id: AAS-2026-10-14-smriti-mcp-14f6928f9817-01
source-identity: "https://github.com/Deepak-Bhardwaj-PS/smriti-mcp"
reviewed-boundary: "8264bf9103477d9521e57b27c81dcc2e943a3230"
memory-comparison:
  version: 2
  scope: "Use-updated Markdown bodies and YAML metadata, NDJSON observations and operation reports, generated Markdown and YAML indexes, and their transient lexical/alias/link access structures; includes caller writes, external-file admission, trace review/consolidation, access reinforcement, lifecycle changes, maintenance and requested reload/delivery. Excludes static server instructions, executable package code, request-local diagnostics, external host/model state and dependency internals. External caller authorship, initial file provenance and eventual host interpretation remain unresolved, not silently excluded alternatives."
  axes:
    storage_substrate:
      assessment: known
      units:
        - scope: "Durable note bodies and metadata"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-memory-body, memory.md#mem-obj-memory-meta, runtime.md#rt-rte-memory-write]
              note: "Bodies and YAML fields persist together in local Markdown files and reload on later calls."
          records: [memory.md#mem-obj-memory-body, memory.md#mem-obj-memory-meta]
          note: "The records identify both operative parts; unknown initial authorship does not obscure their substrate."
        - scope: "Raw observations, remembered-content copies and consolidation operation reports"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-trace-events, runtime.md#rt-rte-trace-consolidation]
              note: "NDJSON files retain events for subsequent loading and grouping."
          records: [memory.md#mem-obj-trace-events]
          note: "The recorded population includes both supplied content and generated bookkeeping; JSON encoding is not a separate substrate."
        - scope: "Saved Markdown index and YAML machine-index export"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-markdown-index, memory.md#mem-obj-machine-index]
              note: "Both generated exports reside on the filesystem; only Markdown has an established reload consumer."
          records: [memory.md#mem-obj-markdown-index, memory.md#mem-obj-machine-index]
          note: "Export storage is established independently of later consumption."
        - scope: "Freshly derived lexical, alias and adjacency access structures"
          assessment: known
          findings:
            - value: in-memory
              basis: wired
              records: [memory.md#mem-obj-machine-index, runtime.md#rt-rte-context-recall]
              note: "Retrieval builds Python dictionaries anew from retained notes."
          records: [memory.md#mem-obj-machine-index]
          note: "Includes the access structure, not ordinary executor state; directed links are fields in dictionaries, not a separate graph storage service."
      records: [memory.md#mem-obj-memory-body, memory.md#mem-obj-memory-meta, memory.md#mem-obj-trace-events, memory.md#mem-obj-markdown-index, memory.md#mem-obj-machine-index, runtime.md#rt-rte-context-recall, runtime.md#rt-rte-trace-consolidation, runtime.md#rt-rte-store-maintenance]
      note: "The object inventory and write/reload/maintenance containers cover the shipped memory surfaces; no included opaque provider store is established. Files and in-memory access structures exhaust this named inventory, not all storage in an enclosing host."
    representational_form:
      assessment: known
      units:
        - scope: "Note prose and displayed titles/descriptions consumed by a human or agent"
          assessment: known
          findings:
            - value: natural-language
              basis: afforded
              records: [memory.md#mem-obj-memory-body, memory.md#mem-obj-memory-meta, epistemic.md#epi-rte-recall-selection]
              note: "Returned prose supplies readable context to an external consumer; actual host interpretation is unobserved."
          records: [memory.md#mem-obj-memory-body, memory.md#mem-obj-memory-meta, epistemic.md#epi-rte-recall-selection]
          note: "Classifies readable content rather than assuming compact snippets expose the complete retained body."
        - scope: "Body wikilinks and fixed-rule consumption of body terms and metadata fields"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-memory-body, memory.md#mem-obj-memory-meta, runtime.md#rt-rte-context-recall]
              note: "Localized strings, statuses, counters and numeric salience enter fixed lexical, filtering and graph rules."
          records: [memory.md#mem-obj-memory-body, memory.md#mem-obj-memory-meta]
          note: "This consumption path differs from prose interpretation; scalar numerical counters are not distributed parameters."
        - scope: "Trace content displayed for review"
          assessment: known
          findings:
            - value: natural-language
              basis: afforded
              records: [memory.md#mem-obj-trace-events, runtime.md#rt-rte-trace-consolidation]
              note: "Readable observations and operation reports are returned to the review caller."
          records: [memory.md#mem-obj-trace-events, runtime.md#rt-rte-trace-consolidation]
          note: "A documented review consumer establishes the form without establishing semantic criticism or compliance."
        - scope: "Trace envelopes, filters and term-based grouping"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-trace-events, epistemic.md#epi-rte-trace-review]
              note: "JSON fields and normalized content terms are selected and grouped by fixed Python rules."
          records: [memory.md#mem-obj-trace-events, epistemic.md#epi-rte-trace-review]
          note: "Generic origin does not make the inspected envelope or grouping opaque."
        - scope: "Generated Markdown index display"
          assessment: known
          findings:
            - value: natural-language
              basis: afforded
              records: [memory.md#mem-obj-markdown-index]
              note: "Titles and descriptions support the shipped human/agent index-review role."
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-markdown-index]
              note: "Rendered navigation links and category organization identify note destinations."
          records: [memory.md#mem-obj-markdown-index]
          note: "Mixed display and navigation are classified separately; index loading is implemented but a successful user review is not observed."
        - scope: "Machine access structures and saved YAML export"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-machine-index]
              note: "Term frequencies, alias mappings and links/backlinks have localized fixed-rule meanings."
          records: [memory.md#mem-obj-machine-index]
          note: "The saved export has no established reload consumer; its structured representation remains inspectable."
      records: [memory.md#mem-obj-memory-body, memory.md#mem-obj-memory-meta, memory.md#mem-obj-trace-events, memory.md#mem-obj-markdown-index, memory.md#mem-obj-machine-index, runtime.md#rt-rte-context-recall, runtime.md#rt-rte-trace-consolidation]
      note: "The complete named text/metadata/index inventory has readable and symbolic paths, not an owned distributed-parametric memory component. Coverage is complete for these forms, while evidence of external interpretation remains afforded."
    lineage:
      assessment: partial
      units:
        - scope: "Supplied note prose and metadata on API writes"
          assessment: known
          findings:
            - value: authored
              basis: afforded
              records: [runtime.md#rt-rte-memory-write, memory.md#mem-obj-memory-body, runtime.md#rt-rte-trace-consolidation]
              note: "The caller authors or supplies final retained prose, including consolidated content; human versus model origin is unresolved."
            - value: imported
              basis: wired
              records: [epistemic.md#epi-rte-content-retention, runtime.md#rt-rte-memory-write]
              note: "Smriti acquires the externally supplied content rather than producing its semantic claims."
          records: [runtime.md#rt-rte-memory-write, epistemic.md#epi-rte-content-retention]
          note: "Authorship at the external production path and import at the Smriti boundary coexist; no source-warrant preservation is implied."
        - scope: "Initial externally edited note bodies and metadata"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-memory-body, memory.md#mem-obj-memory-meta, runtime.md#rt-rte-memory-write]
          note: "Files are reloadable, but their initial derivation/provenance is unresolved; the known API path does not classify this alternative."
        - scope: "Derived descriptions, metadata defaults, repair fields and wikilinks"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-memory-meta, epistemic.md#epi-rte-maintenance-rewrite, runtime.md#rt-rte-store-maintenance]
              note: "Fixed rules derive prefixes, timestamps/defaults and symbolic link associations from supplied or retained text and metadata."
          records: [memory.md#mem-obj-memory-meta, epistemic.md#epi-rte-maintenance-rewrite]
          note: "This derivation is known even when the source file's initial origin is not; compilation does not guarantee semantic preservation."
        - scope: "Caller-supplied observations in raw trace files"
          assessment: partial
          findings:
            - value: imported
              basis: wired
              records: [memory.md#mem-obj-trace-events, epistemic.md#epi-rte-content-retention]
              note: "The event envelope retains supplied external observations."
          records: [memory.md#mem-obj-trace-events]
          note: "The acquisition edge is known; original human/model/application provenance and whether supplied content was extracted from another trace are not."
        - scope: "Remembered-content copies, consolidation bookkeeping and access feedback"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-trace-events, runtime.md#rt-rte-trace-consolidation, memory.md#mem-rte-access-reinforcement]
              note: "Code copies/report-formats write activity and derives durable access timestamps, counts and salience."
          records: [memory.md#mem-obj-trace-events, memory.md#mem-rte-access-reinforcement]
          note: "These local derivations are established; they do not establish automatic extraction of standing prose from experience."
        - scope: "Caller consolidation's relation to selected raw traces"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-trace-consolidation, epistemic.md#epi-rte-content-retention, epistemic.md#epi-rte-trace-review]
          note: "The experience-to-prose route is afforded, but actual supplied prose and support linkage are absent; trace IDs alone do not establish trace-extracted content."
        - scope: "Generated Markdown index and machine index"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-markdown-index, memory.md#mem-obj-machine-index]
              note: "Current note scans generate summaries, navigation, lexical counts and adjacency structures."
          records: [memory.md#mem-obj-markdown-index, memory.md#mem-obj-machine-index]
          note: "Known local derivation does not resolve the initial provenance of the indexed notes."
      records: [memory.md#mem-obj-memory-body, memory.md#mem-obj-memory-meta, memory.md#mem-obj-trace-events, memory.md#mem-obj-markdown-index, memory.md#mem-obj-machine-index, runtime.md#rt-rte-trace-consolidation, memory.md#mem-rte-access-reinforcement, epistemic.md#epi-rte-content-retention]
      note: "Supported authorship, acquisition and deterministic derivation coexist with unresolved external-file origins and unverified trace-to-prose lineage; those alternatives prevent complete lineage coverage."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Retrieved prose, display descriptions and Markdown index at external readers"
          assessment: partial
          findings:
            - value: knowledge
              basis: afforded
              records: [memory.md#mem-obj-memory-body, memory.md#mem-obj-markdown-index, epistemic.md#epi-rte-recall-selection]
              note: "The documented later caller can use returned material as context, reference or advice."
          records: [memory.md#mem-obj-memory-body, memory.md#mem-obj-memory-meta, memory.md#mem-obj-markdown-index, epistemic.md#epi-rte-recall-selection]
          note: "Host interpretation is not supplied. Standing instruction force or other content-specific effects cannot be classified from delivery alone."
        - scope: "Note text, lexical metadata, lifecycle, expiry, counters and derived term/graph features at retrieval selectors"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [memory.md#mem-obj-memory-body, memory.md#mem-obj-memory-meta, memory.md#mem-obj-machine-index, runtime.md#rt-rte-context-recall, memory.md#mem-rte-access-reinforcement]
              note: "Retained terms and fields influence candidate scores, graph-expanded priorities and later affinity."
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-memory-meta, memory.md#mem-obj-machine-index, runtime.md#rt-rte-context-recall]
              note: "Exact scope/filter fields and wikilink identity mappings determine the requested selection scope and expansion destinations."
            - value: enforcement
              basis: wired
              records: [epistemic.md#epi-rte-lifecycle-disposition, runtime.md#rt-rte-context-recall]
              note: "Archived/superseded statuses exclude notes from default recall; this bounded response veto is overrideable and not universal access control."
          records: [memory.md#mem-obj-memory-body, memory.md#mem-obj-memory-meta, memory.md#mem-obj-machine-index, runtime.md#rt-rte-context-recall, epistemic.md#epi-rte-lifecycle-disposition, memory.md#mem-rte-access-reinforcement]
          note: "Fixed selector consumers are inspected. Confidence and verification labels are not truth validation, and unconsumed related/source metadata has no inferred force."
        - scope: "Retained trace fields/content at grouping and review"
          assessment: partial
          findings:
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-trace-events, epistemic.md#epi-rte-trace-review]
              note: "Agent/time/scope and normalized terms select and group the raw material supplied to review."
            - value: ranking
              basis: wired
              records: [runtime.md#rt-rte-trace-consolidation, epistemic.md#epi-rte-trace-review]
              note: "Event counts and salience order groups and influence review/create/update recommendations."
            - value: knowledge
              basis: afforded
              records: [memory.md#mem-obj-trace-events, runtime.md#rt-rte-trace-consolidation]
              note: "Raw observations supply reference material to the documented review caller."
            - value: learning
              basis: afforded
              records: [runtime.md#rt-rte-trace-consolidation, epistemic.md#epi-rte-trace-review]
              note: "The documented agent review role can use retained experience to supply a durable note for later retrieval; this is an afforded update consumer, not inspected autonomous synthesis."
          records: [memory.md#mem-obj-trace-events, runtime.md#rt-rte-trace-consolidation, epistemic.md#epi-rte-trace-review]
          note: "The raw-to-review-to-durable-note route is supported as an affordance; actual semantic update control, resulting content and later host effects remain unresolved. Learning authority here does not establish improved capacity or automatic trace learning."
        - scope: "Persisted YAML machine-index export"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-obj-machine-index]
          note: "The inspected export has no shipped reload consumer, so no authority is assigned to the saved YAML; the freshly derived selector representation is classified separately."
      records: [memory.md#mem-obj-memory-body, memory.md#mem-obj-memory-meta, memory.md#mem-obj-trace-events, memory.md#mem-obj-markdown-index, memory.md#mem-obj-machine-index, runtime.md#rt-rte-context-recall, runtime.md#rt-rte-trace-consolidation, epistemic.md#epi-rte-trace-review, epistemic.md#epi-rte-lifecycle-disposition]
      note: "Fixed retrieval effects and afforded reference/update roles are supported. External content interpretation and review control prevent a complete authority classification; static tool guidance is outside the memory boundary."
    write_agency:
      assessment: partial
      units:
        - scope: "Caller-selected content writes, explicit mutations, trace recording and consolidated-prose submission"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-memory-write, runtime.md#rt-rte-trace-consolidation, epistemic.md#epi-rte-write-admission]
          note: "A generic caller may be human, model or application. No recorded per-content human decision establishes manual agency, and lack of an approval gate alone does not settle who supplied or approved the content."
        - scope: "Raw filesystem admission of initial content"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-memory-body, memory.md#mem-obj-memory-meta, runtime.md#rt-rte-memory-write]
          note: "Reload is inspected but initial admission control is unresolved; API-mediated control cannot be transferred to file editors."
        - scope: "Remember auto successor selection and generated description/default metadata"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [epistemic.md#epi-rte-write-admission, runtime.md#rt-rte-memory-write, epistemic.md#epi-rte-maintenance-rewrite]
              note: "After a request, fixed code chooses the auto branch and derives omitted fields without an individual human decision for those changes."
          records: [epistemic.md#epi-rte-write-admission, runtime.md#rt-rte-memory-write, epistemic.md#epi-rte-maintenance-rewrite]
          note: "Local automatic branch/field admission does not resolve approval of the caller's prose or explicit-mode alternatives."
        - scope: "Selected-ID access reinforcement"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-rte-access-reinforcement]
              note: "Code admits timestamp/count/salience increments after recall selection or a direct request; initiation is not per-update content approval."
          records: [memory.md#mem-rte-access-reinforcement]
          note: "A caller can disable marking, but does not individually determine each numeric update."
        - scope: "Invoked repair, link rewriting, index generation and consolidation bookkeeping"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-store-maintenance, epistemic.md#epi-rte-maintenance-rewrite, runtime.md#rt-rte-trace-consolidation]
              note: "Fixed rules admit generated edits/exports/reports after invocation without per-content human approval."
          records: [runtime.md#rt-rte-store-maintenance, epistemic.md#epi-rte-maintenance-rewrite, runtime.md#rt-rte-trace-consolidation]
          note: "Dry-run/skip options withhold changes; triggering a batch does not make its individual admissions manual."
      records: [runtime.md#rt-rte-memory-write, runtime.md#rt-rte-trace-consolidation, runtime.md#rt-rte-store-maintenance, epistemic.md#epi-rte-write-admission, epistemic.md#epi-rte-maintenance-rewrite, memory.md#mem-rte-access-reinforcement, memory.md#mem-obj-memory-body]
      note: "Automatic code-controlled admissions are wired, while content-supplying callers and initial file editors retain unknown human control. No manual finding is established merely from caller initiation."
    curation_operations:
      assessment: partial
      units:
        - scope: "Replacing/appending existing notes and deterministic metadata/link repair"
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [runtime.md#rt-rte-memory-write, runtime.md#rt-rte-store-maintenance, epistemic.md#epi-rte-maintenance-rewrite]
              note: "Existing entries are revised by update/append, field repair and body-link rewriting; semantic correctness is not guaranteed."
          records: [runtime.md#rt-rte-memory-write, runtime.md#rt-rte-store-maintenance, epistemic.md#epi-rte-maintenance-rewrite]
          note: "These implemented revisions do not establish deduplication or creation of a new semantic claim."
        - scope: "Reduced descriptions and generated Markdown display of retained note claims"
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [epistemic.md#epi-rte-maintenance-rewrite, memory.md#mem-obj-markdown-index, memory.md#mem-obj-memory-meta]
              note: "Descriptions compress existing prose and the Markdown index selects/groups retained summaries into a reduced display; truncation can lose conditions without becoming synthesis."
          records: [epistemic.md#epi-rte-maintenance-rewrite, memory.md#mem-obj-markdown-index, memory.md#mem-obj-memory-meta]
          note: "Only transformations of retained content are classified here; ordinary acquisition and machine-index rebuild alone are not curation."
        - scope: "Archive and supersession with retained history"
          assessment: known
          findings:
            - value: invalidate
              basis: wired
              records: [epistemic.md#epi-rte-lifecycle-disposition, runtime.md#rt-rte-memory-write]
              note: "Status changes withdraw default current recall reliance while preserving historical files and override/get routes."
          records: [epistemic.md#epi-rte-lifecycle-disposition, runtime.md#rt-rte-memory-write]
          note: "Bounded withdrawal is not universal revocation or evidence of factual refutation; permanent deletion is a separate destructive path."
        - scope: "Expiry affinity penalty"
          assessment: known
          findings:
            - value: decay
              basis: wired
              records: [runtime.md#rt-rte-context-recall]
              note: "Expiry subtracts from later retrieval score, downweighting rather than evicting the retained note."
          records: [runtime.md#rt-rte-context-recall]
          note: "This is the recorded time-dependent downweighting route, not automatic deletion or counter decay."
        - scope: "Access-based salience reinforcement"
          assessment: known
          findings:
            - value: promote
              basis: wired
              records: [memory.md#mem-rte-access-reinforcement]
              note: "Selected access raises durable salience by 0.02 up to 1.0, and later affinity consumes it."
            - value: evolve
              basis: wired
              records: [memory.md#mem-rte-access-reinforcement]
              note: "The retained entry's counters, timestamp and salience are revised in place."
          records: [memory.md#mem-rte-access-reinforcement]
          note: "Promotion is an implemented salience change, not demonstrated usefulness or improved capacity."
        - scope: "Semantic transformation of raw traces into caller-supplied consolidated prose"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-trace-consolidation, epistemic.md#epi-rte-trace-review, epistemic.md#epi-rte-content-retention]
          note: "Grouping itself does not compress event claims; the external caller supplies final prose. No actual inputs/output or semantic transformation record distinguishes consolidation, synthesis, deduplication or simple acquisition on that branch."
      records: [runtime.md#rt-rte-memory-write, runtime.md#rt-rte-context-recall, runtime.md#rt-rte-store-maintenance, runtime.md#rt-rte-trace-consolidation, epistemic.md#epi-rte-maintenance-rewrite, epistemic.md#epi-rte-lifecycle-disposition, memory.md#mem-rte-access-reinforcement, memory.md#mem-obj-markdown-index]
      note: "Wired local reduction, revision, withdrawal, downweighting and promotion coexist with unresolved caller semantics. Command names, duplicate-title diagnostics, primary-key rejection and index rebuilding do not establish additional curation operations."
    read_back_direction:
      assessment: known
      units:
        - scope: "Get/list/search/recall of retained notes and fresh access structures"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-context-recall, epistemic.md#epi-rte-recall-selection, memory.md#mem-obj-memory-body]
              note: "A consumer requests an ID, browsing operation or query; ranking and delivery fulfill that request."
          records: [runtime.md#rt-rte-context-recall, epistemic.md#epi-rte-recall-selection]
          note: "Automatic ranking, neighbor expansion and access side effects inside requested recall do not create an unsolicited push."
        - scope: "Raw-event reload/group suggestions"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-trace-consolidation, memory.md#mem-obj-trace-events, epistemic.md#epi-rte-trace-review]
              note: "A review caller requests filtered/grouped retained events."
          records: [runtime.md#rt-rte-trace-consolidation, epistemic.md#epi-rte-trace-review]
          note: "No automatic continuation invokes consolidation or delivers a later recall after the review response."
        - scope: "Saved Markdown index reload"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [memory.md#mem-obj-markdown-index]
              note: "The caller explicitly loads index.md, optionally refreshing it first."
          records: [memory.md#mem-obj-markdown-index]
          note: "Stale saved displays remain request-delivered, not a push channel."
        - scope: "Saved YAML export"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-obj-machine-index]
          note: "No shipped YAML reload consumer is established; persistence alone is not read-back. Fresh machine structures used in requested retrieval are included above."
      records: [runtime.md#rt-rte-context-recall, runtime.md#rt-rte-trace-consolidation, runtime.md#rt-rte-store-maintenance, memory.md#mem-obj-memory-body, memory.md#mem-obj-trace-events, memory.md#mem-obj-markdown-index, memory.md#mem-obj-machine-index, epistemic.md#epi-rte-recall-selection, epistemic.md#epi-rte-trace-review]
      note: "The records cover the shipped note, trace and index delivery inventory, all explicitly requested. External host scheduling is excluded, not an unresolved shipped push route; unknown eventual prompt use does not change request direction."
    read_back_signal:
      assessment: inapplicable
      units:
        - scope: "Requested note retrieval, trace review and Markdown index load; YAML export without read-back"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-context-recall, runtime.md#rt-rte-trace-consolidation, memory.md#mem-obj-markdown-index, memory.md#mem-obj-machine-index]
          note: "All established read-back is pull, and the YAML export lacks read-back. This axis classifies push selectors only; lexical query scoring and requested IDs therefore supply no signal value."
      records: [runtime.md#rt-rte-context-recall, runtime.md#rt-rte-trace-consolidation, runtime.md#rt-rte-store-maintenance, memory.md#mem-obj-markdown-index, memory.md#mem-obj-machine-index, epistemic.md#epi-rte-recall-selection, epistemic.md#epi-rte-trace-review]
      note: "The completely assessed shipped delivery inventory is pull-only. No identifier, lexical or coarse push is inferred from catalog entries, query responses or budget filtering."
    trace_learning:
      assessment: not-determinable
      units:
        - scope: "Raw trace review followed by caller-supplied durable prose and later retrieval"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-trace-consolidation, memory.md#mem-obj-trace-events, epistemic.md#epi-rte-trace-review, epistemic.md#epi-rte-content-retention]
          note: "The experience-to-prose affordance is recorded, but generic human/model/application identity leaves automatic semantic admission unresolved and trace IDs need not support the submitted content. Neither an unconditional yes nor a bounded no follows for this included alternative."
        - scope: "Access timestamp/count/salience update and later ranking"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-access-reinforcement, memory.md#mem-obj-memory-meta]
          note: "Automatic durable use reinforcement is wired, but the records identify selected IDs and prior metadata as inputs, not a recorded trace-fed derivation. The update writes no raw trace. This supports behavior shaping without establishing a controlled trace-learning value."
        - scope: "Ordinary content admission, event persistence and deterministic maintenance/indexing"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-memory-write, runtime.md#rt-rte-trace-consolidation, runtime.md#rt-rte-store-maintenance, memory.md#mem-obj-machine-index]
          note: "Raw event retention, note acquisition and note-derived repair/export do not by themselves establish automatic trace-fed durable behavior shaping. The accepted set supplies no bounded absence record licensing a system-wide no, and externally supplied content origin remains unresolved."
      records: [runtime.md#rt-rte-memory-write, runtime.md#rt-rte-trace-consolidation, runtime.md#rt-rte-store-maintenance, memory.md#mem-obj-trace-events, memory.md#mem-rte-access-reinforcement, epistemic.md#epi-rte-trace-review, epistemic.md#epi-rte-content-retention]
      note: "Inspection establishes retained experience, caller-led review and automatic numerical adaptation, but no fully classified automatic trace-fed write. Missing caller control and source-to-output linkage prevent yes; no scoped absence warrant establishes no. This is not a claim that learning or adaptation is absent."
    trace_source:
      assessment: not-determinable
      units:
        - scope: "Original content feeding any qualifying external trace-review-to-prose write"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-trace-events, runtime.md#rt-rte-trace-consolidation, epistemic.md#epi-rte-trace-review]
          note: "Raw observations can have human/model/application origins and generated reports also exist, but automatic trace-learning qualification and actual consumed source content are unresolved. NDJSON, agent labels and event types cannot establish session-logs, tool-traces, event-streams or trajectories for a qualifying write."
        - scope: "Original input to use reinforcement and other included automatic transformations"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-rte-access-reinforcement, runtime.md#rt-rte-store-maintenance, memory.md#mem-obj-machine-index]
          note: "Selected IDs/prior metadata and note scans are recorded inputs. They do not establish an original trace source feeding a qualifying learning route; timestamps or activity-sensitive outputs alone are insufficient."
      records: [memory.md#mem-obj-trace-events, runtime.md#rt-rte-trace-consolidation, epistemic.md#epi-rte-trace-review, memory.md#mem-rte-access-reinforcement, runtime.md#rt-rte-store-maintenance]
      note: "No qualifying trace-fed route is completely classified, and trace learning is not established absent. Therefore source coverage is unresolved rather than inapplicable; no source category is inferred from storage format."
---

# Smriti MCP memory profile

## Comparison rationale

The memory boundary is the use-updated note, event and access-structure inventory in [MEM-OBJ-memory-body](memory.md#mem-obj-memory-body), [MEM-OBJ-memory-meta](memory.md#mem-obj-memory-meta), [MEM-OBJ-trace-events](memory.md#mem-obj-trace-events), [MEM-OBJ-markdown-index](memory.md#mem-obj-markdown-index) and [MEM-OBJ-machine-index](memory.md#mem-obj-machine-index). Fixed package rules and [RT-OBJ-server-instructions](runtime.md#rt-obj-server-instructions) are not accumulated memory. In particular, their tool schemas do not supply a validation-authority finding for retained content.

The supplied reconciliation resolves the duplicate epistemic body, metadata, trace and access-reinforcement declarations to the corresponding memory records. The profile cites those canonical memory anchors. The runtime containers remain valid alongside distinct epistemic checking, selection, retention, maintenance and lifecycle parts; none of those parts is treated as a second retained payload. Supersession changes citation identity, not evidence strength.

Files are the persistent substrate. Adjacency mappings do not add graph storage, and lexical counts do not add vector storage. Fresh Python access dictionaries receive a separate in-memory finding because they are an access structure derived from retained notes, not merely executor state. Saved YAML has storage and symbolic-form findings but no read-back or behavioral authority: [MEM-OBJ-machine-index](memory.md#mem-obj-machine-index) establishes export rather than reload. The Markdown index has a different, explicitly requested consumer.

Natural-language context and fixed-rule lexical consumption are separate paths through the same body. [EPI-RTE-recall-selection](epistemic.md#epi-rte-recall-selection) supports an afforded reference/advice role at the external reader, not observed instruction compliance. Retained fields and terms have wired ranking force even though the scoring policy itself is fixed code. Default archived/superseded exclusion is bounded enforcement, not authentication or a universal read ban; [EPI-RTE-lifecycle-disposition](epistemic.md#epi-rte-lifecycle-disposition) preserves full-get and override routes. Trace material has an afforded learning role at the review-to-update consumer, distinct from its reference role and from automatic trace-learning qualification.

Local deterministic derivation remains known despite unknown initial file provenance. The missing-description doctrine does not erase the compiled-prefix path: [EPI-RTE-maintenance-rewrite](epistemic.md#epi-rte-maintenance-rewrite) records its implementation and loss-of-condition counterexample. A lossy reduction remains consolidation rather than synthesis merely because it is unfaithful. The machine index's rebuild alone establishes no curation operation. Likewise, the name consolidate_memory does not resolve the external caller's semantic transformation; [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation) records supplied prose, not an owned summarizer, and create/update provenance differs from append.

Write agency is local to admission. The automatic branch decision, repair edits and [MEM-RTE-access-reinforcement](memory.md#mem-rte-access-reinforcement) are code-controlled even after a caller starts them. Generic prose suppliers and external file editors remain unresolved rather than manual by default. Their unknown control prevents a complete write-agency union.

Requested retrieval remains pull even when code ranks, filters, expands neighbors and formats the response. [RT-RTE-context-recall](runtime.md#rt-rte-context-recall), [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation) and the two index records cover the delivery inventory. The read-back signal axis is therefore inapplicable within this shipped boundary. Full retrieval remains available when compact recall omits body content, source references or reasons; no complete-content or actual host-use conclusion is implied.

The trace axes retain a narrower uncertainty than the behavioral-authority axis. An experience-to-prose affordance does not resolve whether a human or model admitted a particular semantic update, and unverified trace identifiers do not establish its input lineage. Automatic access reinforcement is independently wired, but its recorded input is a selected ID and prior metadata, not an established recorded trace derivation. Neither the absence of raw-trace writing on that route nor lack of observed improvement supplies a system-wide trace-learning negative. The accepted records consequently support neither a complete positive classification nor bounded absence, and trace source cannot be declared inapplicable.

Source-read log: none. This classification uses only the supplied accepted records and reconciliation; no frozen-source ambiguity required an additional read. No finding has observed or causally supported basis because the accepted set supplies neither execution traces nor comparative experiments.
