---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Omni-Memory comparison profile for retained claims, context projections, control metadata and their later consumers at the frozen Git boundary."
run-id: "AAS-2026-11-08-omni-memory-09378abbfe6b-01"
source-identity: "https://github.com/singhabhinav04/omni-memory"
reviewed-boundary: "20f9f9ffd7ece0c6514542677ba6a549841f5536"
memory-comparison:
  version: 2
  scope: "Accumulated project/global SQLite claims and lineage/access state; source-derived graph and documentation; managed context and digest; sharing files; activity summaries, feedback, observations, telemetry, cache and capture cursor; write/maintenance and later-consumer routes. Included unresolved alternatives are additional map/retained-flow parts and opaque upstream content/admission provenance. Excludes static shipped instructions alone, transient candidate arrays, ordinary current-call state, external provider weights/internal state and host compaction/transcript-storage policy. Host-retained session text is an input to the target's trace-fed writes, not an additional target-owned transcript store."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Project and global claim rows, row metadata, code topology, events, observation/witness state, savings and extraction cursor"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-text"
                - "memory.md#mem-obj-memory-state"
                - "memory.md#mem-obj-code-graph"
                - "memory.md#mem-obj-event-log"
                - "memory.md#mem-obj-observation-state"
                - "memory.md#mem-obj-savings"
                - "memory.md#mem-rte-transcript-window"
              note: "These retained parts use SQLite columns/tables or meta entries; the global claim store is a separate SQLite instance."
          records:
            - "memory.md#mem-obj-memory-text"
            - "memory.md#mem-obj-memory-state"
            - "memory.md#mem-obj-code-graph"
            - "memory.md#mem-obj-event-log"
            - "memory.md#mem-obj-observation-state"
            - "memory.md#mem-obj-savings"
            - "memory.md#mem-rte-transcript-window"
          note: "Encoding as JSON in a column does not change the substrate."
        -
          scope: "Managed context, digest, generated documents, injection cache and sharing files"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-agents-context"
                - "memory.md#mem-obj-memory-digest"
                - "memory.md#mem-obj-generated-documents"
                - "runtime.md#rt-obj-inject-cache"
                - "runtime.md#rt-rte-shared-import"
              note: "Managed Markdown, digest/API/linkup documents, digest-counter cache and JSON shards/snapshots persist as files."
          records:
            - "memory.md#mem-obj-agents-context"
            - "memory.md#mem-obj-memory-digest"
            - "memory.md#mem-obj-generated-documents"
            - "runtime.md#rt-obj-inject-cache"
            - "runtime.md#rt-rte-shared-import"
          note: "Git transports shared files; it does not make all operative memory a repository substrate."
        -
          scope: "Operative retained-flow and additional map parts beyond the recorded graph and file projections"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-code-graph"
          note: "The graph record identifies a flows schema without an established population/consumer and incompletely inspected maps. It cannot establish an exhaustive operative-object inventory or any additional substrate."
      records:
        - "memory.md#mem-obj-memory-text"
        - "memory.md#mem-obj-memory-state"
        - "memory.md#mem-obj-code-graph"
        - "memory.md#mem-obj-event-log"
        - "memory.md#mem-obj-observation-state"
        - "memory.md#mem-obj-savings"
        - "memory.md#mem-rte-transcript-window"
        - "memory.md#mem-obj-agents-context"
        - "memory.md#mem-obj-memory-digest"
        - "memory.md#mem-obj-generated-documents"
        - "runtime.md#rt-obj-inject-cache"
        - "runtime.md#rt-rte-shared-import"
      note: "SQLite and file witnesses classify the recorded operative parts. Unresolved retained-flow/map inventory prevents complete boundary coverage; external completion weights and host transcript storage are not target-retained memory."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Claim prose, managed guidance, digest, generated explanations and event-summary prose"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-text"
                - "memory.md#mem-obj-agents-context"
                - "memory.md#mem-obj-memory-digest"
                - "memory.md#mem-obj-generated-documents"
                - "memory.md#mem-obj-event-log"
              note: "Human/model interpretation consumes claims, guidance and descriptions; diagrams/code notation in documents does not establish a separate formal consumer."
          records:
            - "memory.md#mem-obj-memory-text"
            - "memory.md#mem-obj-agents-context"
            - "memory.md#mem-obj-memory-digest"
            - "memory.md#mem-obj-generated-documents"
            - "memory.md#mem-obj-event-log"
          note: "The same claim can have symbolic ranking consumers, assessed separately below."
        -
          scope: "Claim text and graph labels at lexical/overlap/identity consumers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-query-ranking"
                - "memory.md#mem-rte-anchor-maintenance"
                - "memory.md#mem-obj-code-graph"
              note: "Fixed lexical overlap, identity and graph traversal rules consume localized text/labels as selectors."
          records:
            - "epistemic.md#epi-rte-query-ranking"
            - "memory.md#mem-rte-anchor-maintenance"
            - "memory.md#mem-obj-code-graph"
          note: "This is a distinct consumption path from interpreting the prose."
        -
          scope: "Lineage/access columns, graph relations/ranges, observations, counters, cache and checkpoint"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-state"
                - "memory.md#mem-obj-code-graph"
                - "memory.md#mem-obj-observation-state"
                - "memory.md#mem-obj-savings"
                - "runtime.md#rt-obj-inject-cache"
                - "memory.md#mem-rte-transcript-window"
              note: "Fixed code rules consume identifiers, digests, tiers, positions, counts and cursor values."
          records:
            - "memory.md#mem-obj-memory-state"
            - "memory.md#mem-obj-code-graph"
            - "memory.md#mem-obj-observation-state"
            - "memory.md#mem-obj-savings"
            - "runtime.md#rt-obj-inject-cache"
            - "memory.md#mem-rte-transcript-window"
          note: "Graph doc prose remains a separate natural-language part."
        -
          scope: "Embedded graph documentation at dashboard/document readers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-code-graph"
                - "memory.md#mem-rte-recall-search"
              note: "Graph doc text can be returned in requested symbol/dashboard material for interpretation."
          records:
            - "memory.md#mem-obj-code-graph"
            - "memory.md#mem-rte-recall-search"
          note: "Requested display is established; automatic host interpretation is not."
        -
          scope: "Unestablished retained-flow payloads and map transformations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-code-graph"
          note: "Schema and partial map coverage do not establish every operative consumed part or form."
      records:
        - "memory.md#mem-obj-memory-text"
        - "memory.md#mem-obj-agents-context"
        - "memory.md#mem-obj-memory-digest"
        - "memory.md#mem-obj-generated-documents"
        - "memory.md#mem-obj-event-log"
        - "epistemic.md#epi-rte-query-ranking"
        - "memory.md#mem-rte-anchor-maintenance"
        - "memory.md#mem-obj-code-graph"
        - "memory.md#mem-obj-memory-state"
        - "memory.md#mem-obj-observation-state"
        - "memory.md#mem-obj-savings"
        - "runtime.md#rt-obj-inject-cache"
        - "memory.md#mem-rte-transcript-window"
        - "memory.md#mem-rte-recall-search"
      note: "No retained embedding or changing model weights are established. That is not an evidenced-absence claim about uninspected alternatives."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Foreground agent/caller-supplied claims and document edits"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-text"
                - "runtime.md#rt-rte-local-edits"
              note: "Explicit text/JSON and edits supply authored content; this does not identify a human author or manual approval."
          records:
            - "memory.md#mem-obj-memory-text"
            - "runtime.md#rt-rte-local-edits"
          note: "The immediate supplied-content path is known; upstream provenance is separate."
        -
          scope: "Shared snapshots/shards and acquired project-document/source inputs"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-shared-import"
                - "runtime.md#rt-rte-build-artifacts"
              note: "External shard/snapshot assertions and repository document/source content enter the target's retained-memory production paths."
          records:
            - "runtime.md#rt-rte-shared-import"
            - "runtime.md#rt-rte-build-artifacts"
          note: "Import preserves selected fields, not original epistemic warrant or a complete store restore."
        -
          scope: "Transcript-derived claims and automatic session feedback"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-capture-admission"
                - "memory.md#mem-rte-transcript-window"
                - "memory.md#mem-obj-event-log"
                - "memory.md#mem-rte-anchor-maintenance"
              note: "Conversation text yields durable claims; citations and activity produce counters, tier changes and event summaries."
          records:
            - "runtime.md#rt-rte-capture-admission"
            - "memory.md#mem-rte-transcript-window"
            - "memory.md#mem-obj-event-log"
            - "memory.md#mem-rte-anchor-maintenance"
          note: "Wired derivation does not show that all transcript text was examined."
        -
          scope: "Graph, generated projections, source bindings and bookkeeping"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-code-graph"
                - "memory.md#mem-obj-agents-context"
                - "memory.md#mem-obj-memory-digest"
                - "memory.md#mem-obj-observation-state"
                - "memory.md#mem-obj-savings"
                - "runtime.md#rt-obj-inject-cache"
              note: "Parser output, automatic rendering, hashes and code-calculated telemetry are compiled derived parts rather than learned parameters."
          records:
            - "memory.md#mem-obj-code-graph"
            - "memory.md#mem-obj-agents-context"
            - "memory.md#mem-obj-memory-digest"
            - "memory.md#mem-obj-observation-state"
            - "memory.md#mem-obj-savings"
            - "runtime.md#rt-obj-inject-cache"
          note: "This finding does not claim semantic novelty."
        -
          scope: "Original provenance of caller/imported prose and particular model-produced explanations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-memory-text"
            - "memory.md#mem-obj-generated-documents"
            - "runtime.md#rt-rte-build-artifacts"
            - "runtime.md#rt-rte-shared-import"
          note: "Immediate authorship/import routes do not resolve initial derivation or whether particular model content preserves, derives or invents claims."
        -
          scope: "Additional map/flow derivation paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-code-graph"
          note: "Available but incompletely inspected transformations prevent a complete lineage inventory."
      records:
        - "memory.md#mem-obj-memory-text"
        - "runtime.md#rt-rte-local-edits"
        - "runtime.md#rt-rte-shared-import"
        - "runtime.md#rt-rte-build-artifacts"
        - "runtime.md#rt-rte-capture-admission"
        - "memory.md#mem-rte-transcript-window"
        - "memory.md#mem-obj-event-log"
        - "memory.md#mem-rte-anchor-maintenance"
        - "memory.md#mem-obj-code-graph"
        - "memory.md#mem-obj-agents-context"
        - "memory.md#mem-obj-memory-digest"
        - "memory.md#mem-obj-observation-state"
        - "memory.md#mem-obj-savings"
        - "runtime.md#rt-obj-inject-cache"
        - "memory.md#mem-obj-generated-documents"
      note: "Known immediate paths coexist with unresolved upstream provenance and map/flow coverage."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Claim/digest/event prose at later agent or dashboard readers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-text"
                - "memory.md#mem-obj-memory-digest"
                - "memory.md#mem-obj-event-log"
                - "memory.md#mem-rte-recall-search"
                - "runtime.md#rt-rte-context-delivery"
              note: "Returned project assertions, digest text and activity warnings supply context/reference, not truth guarantees."
          records:
            - "memory.md#mem-obj-memory-text"
            - "memory.md#mem-obj-memory-digest"
            - "memory.md#mem-obj-event-log"
            - "memory.md#mem-rte-recall-search"
            - "runtime.md#rt-rte-context-delivery"
          note: "Host interpretation and benefit remain unobserved; wired return is distinct from actual use."
        -
          scope: "Generated API/linkup explanations at requested human/agent readers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-generated-documents"
                - "memory.md#mem-rte-recall-search"
              note: "Serving saved explanations affords a later interpretive reader; no automatic re-consumption as model memory is established."
          records:
            - "memory.md#mem-obj-generated-documents"
            - "memory.md#mem-rte-recall-search"
          note: "The file-serving path is wired; the intended interpretive use is an affordance, not deployed model wiring."
        -
          scope: "Managed AGENTS.md retained context at an IDE-loading agent"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-agents-context"
              note: "Retained user/feedback/decision content in the managed standing context supplies guidance to the documented IDE reader; static usage-wrapper instructions alone are excluded."
          records:
            - "memory.md#mem-obj-agents-context"
          note: "The managed writer is wired and the later IDE reader is documented; loading/compliance are unobserved. Static packaged guidance is not accumulated memory."
        -
          scope: "Claim text, citation/tier metadata and code graph at retrieval/retention selectors"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-query-ranking"
                - "memory.md#mem-obj-memory-state"
                - "memory.md#mem-obj-code-graph"
                - "memory.md#mem-rte-anchor-maintenance"
                - "memory.md#mem-rte-memory-withdrawal"
              note: "Retained text, graph proximity, uses and evidence tiers alter relative relevance or retention priority."
          records:
            - "epistemic.md#epi-rte-query-ranking"
            - "memory.md#mem-obj-memory-state"
            - "memory.md#mem-obj-code-graph"
            - "memory.md#mem-rte-anchor-maintenance"
            - "memory.md#mem-rte-memory-withdrawal"
          note: "An empty query without contextual inputs can instead sort by recency; ranking is not universal truth validation."
        -
          scope: "Status/branch/protection/duplicate metadata at admission and active-read gates"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-state"
                - "memory.md#mem-rte-memory-withdrawal"
                - "epistemic.md#epi-rte-merge-disposition"
              note: "Status and scope checks exclude rows from active reads; path-specific guards block selected retirement operations."
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-state"
                - "epistemic.md#epi-rte-merge-disposition"
                - "memory.md#mem-rte-anchor-maintenance"
              note: "Retained peers, tier/use/protection data and anchors supply admissibility/retirement comparison criteria."
          records:
            - "memory.md#mem-obj-memory-state"
            - "memory.md#mem-rte-memory-withdrawal"
            - "epistemic.md#epi-rte-merge-disposition"
            - "memory.md#mem-rte-anchor-maintenance"
          note: "These are local software criteria and vetoes, not enforced control of the host's coding actions. Protection is not a universal deletion veto."
        -
          scope: "Cursor/cache and source-access metadata at maintenance/delivery dispatch"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-rte-transcript-window"
                - "runtime.md#rt-obj-inject-cache"
                - "memory.md#mem-obj-observation-state"
                - "runtime.md#rt-rte-use-check"
              note: "Cursor selects the next extraction window; cache regulates re-emission; source pins/bindings select and qualify later checks."
          records:
            - "memory.md#mem-rte-transcript-window"
            - "runtime.md#rt-obj-inject-cache"
            - "memory.md#mem-obj-observation-state"
            - "runtime.md#rt-rte-use-check"
          note: "No content-truth license follows from matching digests."
        -
          scope: "Retained session text and citation feedback at automatic durable update consumers"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-capture-admission"
                - "memory.md#mem-rte-transcript-window"
                - "memory.md#mem-rte-anchor-maintenance"
                - "epistemic.md#epi-rte-query-ranking"
              note: "Recorded session experience feeds retained claims and durable selector changes later consumed by retrieval/host context."
          records:
            - "runtime.md#rt-rte-capture-admission"
            - "memory.md#mem-rte-transcript-window"
            - "memory.md#mem-rte-anchor-maintenance"
            - "epistemic.md#epi-rte-query-ranking"
          note: "Learning authority here names the update input's force, not demonstrated improvement or model training."
        -
          scope: "Savings telemetry beyond reporting; unestablished flow/map consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-savings"
            - "memory.md#mem-obj-code-graph"
          note: "Savings is reporting, with no automatic revision consumer established. Flow/map consumer completeness is unresolved; no additional behavioral force can be inferred from display or a table schema."
      records:
        - "memory.md#mem-obj-memory-text"
        - "memory.md#mem-obj-memory-digest"
        - "memory.md#mem-obj-event-log"
        - "memory.md#mem-rte-recall-search"
        - "runtime.md#rt-rte-context-delivery"
        - "memory.md#mem-obj-generated-documents"
        - "memory.md#mem-obj-agents-context"
        - "epistemic.md#epi-rte-query-ranking"
        - "memory.md#mem-obj-memory-state"
        - "memory.md#mem-obj-code-graph"
        - "memory.md#mem-rte-anchor-maintenance"
        - "memory.md#mem-rte-memory-withdrawal"
        - "epistemic.md#epi-rte-merge-disposition"
        - "memory.md#mem-rte-transcript-window"
        - "runtime.md#rt-obj-inject-cache"
        - "memory.md#mem-obj-observation-state"
        - "runtime.md#rt-rte-use-check"
        - "runtime.md#rt-rte-capture-admission"
        - "memory.md#mem-obj-savings"
      note: "Each force is local to a named consumer. Natural-language instruction does not imply a host-action lock; telemetry presence alone establishes no adaptation authority."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Capture/model/heuristic batch admission, document generation, graph rebuild and automatic projections"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-capture-admission"
                - "runtime.md#rt-rte-build-artifacts"
                - "memory.md#mem-obj-code-graph"
                - "memory.md#mem-obj-agents-context"
                - "memory.md#mem-obj-memory-digest"
              note: "Software/model gates admit content or replace derived artifacts without a per-content human approval requirement."
          records:
            - "runtime.md#rt-rte-capture-admission"
            - "runtime.md#rt-rte-build-artifacts"
            - "memory.md#mem-obj-code-graph"
            - "memory.md#mem-obj-agents-context"
            - "memory.md#mem-obj-memory-digest"
          note: "Launching a build/capture is not human approval of each resulting item."
        -
          scope: "Automatic import, source-binding, feedback, cache/checkpoint and maintenance writes"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-shared-import"
                - "memory.md#mem-obj-observation-state"
                - "memory.md#mem-obj-event-log"
                - "memory.md#mem-obj-savings"
                - "runtime.md#rt-obj-inject-cache"
                - "memory.md#mem-rte-transcript-window"
                - "memory.md#mem-rte-anchor-maintenance"
                - "memory.md#mem-rte-memory-withdrawal"
              note: "Code admits imported rows, records derived state and changes eligibility/tiers under fixed predicates."
          records:
            - "runtime.md#rt-rte-shared-import"
            - "memory.md#mem-obj-observation-state"
            - "memory.md#mem-obj-event-log"
            - "memory.md#mem-obj-savings"
            - "runtime.md#rt-obj-inject-cache"
            - "memory.md#mem-rte-transcript-window"
            - "memory.md#mem-rte-anchor-maintenance"
            - "memory.md#mem-rte-memory-withdrawal"
          note: "Explicit triggering does not turn code-selected downstream changes into manual admission."
        -
          scope: "Explicit remember/global remember, dashboard text/document edits, trusted import and caller-selected resolve/restore"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-local-edits"
            - "runtime.md#rt-rte-shared-import"
            - "epistemic.md#epi-rte-merge-disposition"
            - "memory.md#mem-rte-memory-withdrawal"
          note: "Generic caller identity is not an authenticated human decision; agent invocation is supported. The recorded manual source label cannot establish controlled manual write agency for these admission mechanisms."
        -
          scope: "Initial upstream content and additional flow/map admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-memory-text"
            - "memory.md#mem-obj-generated-documents"
            - "memory.md#mem-obj-code-graph"
          note: "Initial provenance and unestablished additional operative paths prevent classifying every admission mechanism."
      records:
        - "runtime.md#rt-rte-capture-admission"
        - "runtime.md#rt-rte-build-artifacts"
        - "memory.md#mem-obj-code-graph"
        - "memory.md#mem-obj-agents-context"
        - "memory.md#mem-obj-memory-digest"
        - "runtime.md#rt-rte-shared-import"
        - "memory.md#mem-obj-observation-state"
        - "memory.md#mem-obj-event-log"
        - "memory.md#mem-obj-savings"
        - "runtime.md#rt-obj-inject-cache"
        - "memory.md#mem-rte-transcript-window"
        - "memory.md#mem-rte-anchor-maintenance"
        - "memory.md#mem-rte-memory-withdrawal"
        - "runtime.md#rt-rte-local-edits"
        - "epistemic.md#epi-rte-merge-disposition"
        - "memory.md#mem-obj-memory-text"
        - "memory.md#mem-obj-generated-documents"
      note: "Automatic mechanisms are positively classified. No controlled manual finding is justified solely by the source label manual or an explicit CLI/HTTP request."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Heuristic extraction of standing claims from retained session text"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-capture-admission"
                - "memory.md#mem-rte-transcript-window"
              note: "Selection of concise durable claims reduces retained session messages to reusable project memory; raw input may remain in the host transcript."
          records:
            - "runtime.md#rt-rte-capture-admission"
            - "memory.md#mem-rte-transcript-window"
          note: "This is wired for the inspected extraction path; no model fidelity or complete transcript coverage is implied."
        -
          scope: "Automatic duplicate retirement and explicit merge"
          assessment: "known"
          findings:
            -
              value: "dedup"
              basis: "wired"
              records:
                - "memory.md#mem-rte-anchor-maintenance"
                - "epistemic.md#epi-rte-merge-disposition"
              note: "Overlap predicates retire peer rows; caller merge retains chosen text, unions file lists and archives drops."
          records:
            - "memory.md#mem-rte-anchor-maintenance"
            - "epistemic.md#epi-rte-merge-disposition"
          note: "This is not synthesis of the dropped texts or a logical-equivalence check."
        -
          scope: "Caller edits of existing claims/documents and metadata reanchoring"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-local-edits"
              note: "Update handlers revise retained text/fields in place; document saves replace existing content."
          records:
            - "runtime.md#rt-rte-local-edits"
          note: "Agency of the caller is unresolved independently of the wired editing operation."
        -
          scope: "Evidence-tier graduation and withdrawal"
          assessment: "known"
          findings:
            -
              value: "promote"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-tier-graduation"
              note: "Cited stated rows with fresh nonempty hash maps gain verified tier and ranking/retention salience."
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-tier-withdrawal"
              note: "Drift/loss withdraws the old verified qualification without erasing the claim."
          records:
            - "epistemic.md#epi-rte-tier-graduation"
            - "epistemic.md#epi-rte-tier-withdrawal"
          note: "Citation plus unchanged bytes is not outcome confirmation; these findings concern metadata reliance."
        -
          scope: "Quarantine/archive and age/staleness-based retention scoring"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-withdrawal"
              note: "Quarantine and archive withdraw active reliance while preserving history until explicit deletion."
            -
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-withdrawal"
              note: "Dormancy and uncited staleness age contribute to downweighting/removal from active retrieval."
          records:
            - "memory.md#mem-rte-memory-withdrawal"
          note: "Restore can re-enable rows; already delivered host copies are not retracted."
        -
          scope: "Model extraction/build semantic transformations and additional map/flow maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-capture-admission"
            - "runtime.md#rt-rte-build-artifacts"
            - "memory.md#mem-obj-generated-documents"
            - "memory.md#mem-obj-code-graph"
          note: "Prompts request durable content, but record-specific outputs do not establish every transformation. In particular, no controlled synthesize finding follows from an opaque completion or a route name."
      records:
        - "runtime.md#rt-rte-capture-admission"
        - "memory.md#mem-rte-transcript-window"
        - "memory.md#mem-rte-anchor-maintenance"
        - "epistemic.md#epi-rte-merge-disposition"
        - "runtime.md#rt-rte-local-edits"
        - "epistemic.md#epi-rte-tier-graduation"
        - "epistemic.md#epi-rte-tier-withdrawal"
        - "memory.md#mem-rte-memory-withdrawal"
        - "runtime.md#rt-rte-build-artifacts"
        - "memory.md#mem-obj-generated-documents"
        - "memory.md#mem-obj-code-graph"
      note: "Supported curation operations remain local to their transformations. Acquisition, graph rebuild and counters alone are not curation; incomplete alternatives prevent complete operation coverage."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Explicit inject, recall and dashboard requests for accumulated claims/graphs/documents/history"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "memory.md#mem-rte-recall-search"
                - "memory.md#mem-obj-generated-documents"
              note: "The consumer requests retained material; fulfillment is pull even when code ranks and prints it."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "memory.md#mem-rte-recall-search"
            - "memory.md#mem-obj-generated-documents"
          note: "The requested block is not separately counted as unsolicited push."
        -
          scope: "SessionStart seed/events, auto prompt injection and OpenCode compaction additions"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "memory.md#mem-obj-event-log"
              note: "Hooks select retained material and supply it without a foreground request for that material."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "memory.md#mem-obj-event-log"
          note: "OpenCode's internal inject command fulfills the hook's automatic selection; its compaction-context addition is the push operation."
        -
          scope: "Managed AGENTS.md supplied as standing IDE context"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-agents-context"
              note: "A documented IDE-loading path supplies selected persisted context without an explicit per-memory request."
          records:
            - "memory.md#mem-obj-agents-context"
          note: "The writer is wired; loading is an external documented consumer path rather than an observed delivery."
        -
          scope: "Extraction cursor/cache/metadata reused by later target calls"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-transcript-window"
                - "runtime.md#rt-obj-inject-cache"
                - "memory.md#mem-obj-observation-state"
                - "memory.md#mem-obj-memory-state"
              note: "Later invocation code explicitly reads retained control state for extraction, re-emission, source checks and active queries."
          records:
            - "memory.md#mem-rte-transcript-window"
            - "runtime.md#rt-obj-inject-cache"
            - "memory.md#mem-obj-observation-state"
            - "memory.md#mem-obj-memory-state"
          note: "These internal consumers are distinct from host prompt delivery."
        -
          scope: "Additional retained-flow/map later consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-code-graph"
          note: "The recorded schema/map inspection does not establish all later-consumer routes."
      records:
        - "runtime.md#rt-rte-context-delivery"
        - "memory.md#mem-rte-recall-search"
        - "memory.md#mem-obj-generated-documents"
        - "memory.md#mem-obj-event-log"
        - "memory.md#mem-obj-agents-context"
        - "memory.md#mem-rte-transcript-window"
        - "runtime.md#rt-obj-inject-cache"
        - "memory.md#mem-obj-observation-state"
        - "memory.md#mem-obj-memory-state"
        - "memory.md#mem-obj-code-graph"
      note: "Both consumer-requested returns and unsolicited hook supply exist. Unresolved flow/map routes prevent a pull-only or exhaustive direction conclusion."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "SessionStart recent events and no-query fallback seed"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-event-log"
                - "runtime.md#rt-rte-context-delivery"
              note: "Trigger: session start. Selector: latest-three events and recency/fallback active memories under mode/scope/budget rules. Selected parts: event summaries and seed rows."
          records:
            - "memory.md#mem-obj-event-log"
            - "runtime.md#rt-rte-context-delivery"
          note: "Availability, recency and budget are coarse selection, not identifier targeting."
        -
          scope: "Auto prompt injection lexical query and file/symbol/graph context"
          assessment: "known"
          findings:
            -
              value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "epistemic.md#epi-rte-query-ranking"
              note: "Trigger: prompt hook. Selector: current prompt terms scored against retained textual fields. Selected parts: ranked claim rows."
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "memory.md#mem-obj-code-graph"
              note: "Trigger: prompt-context injection. Selector: file/symbol identity/co-anchor and graph-name matches. Selected parts: matching/proximate claims and linked siblings."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "epistemic.md#epi-rte-query-ranking"
            - "memory.md#mem-obj-code-graph"
          note: "Name collisions soften graph targeting. Appended siblings/global rows can be removed by duplicate suppression or budget."
        -
          scope: "OpenCode compaction additions using no-query CLI selection"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
              note: "Trigger: compaction. Selector: internal inject selection/fallback under the recorded no-query context. Selected part: retained memory block appended to compaction context."
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "No semantic-judgment or embedding selector is established."
        -
          scope: "Managed context projection at documented IDE loading"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-agents-context"
              note: "Trigger: subsequent IDE root-context loading. Selector: active rows, recency and per-kind quotas in the managed projection. Selected parts: inline claim text and standing directions."
          records:
            - "memory.md#mem-obj-agents-context"
          note: "A displayed ID is not itself evidence of an identity-matching push selector."
        -
          scope: "Possible push operations in unestablished retained-flow/map paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-code-graph"
          note: "Unknown direction/consumer prevents classifying their push selectors or declaring this axis inapplicable."
      records:
        - "memory.md#mem-obj-event-log"
        - "runtime.md#rt-rte-context-delivery"
        - "epistemic.md#epi-rte-query-ranking"
        - "memory.md#mem-obj-code-graph"
        - "memory.md#mem-obj-agents-context"
      note: "Signals classify actual push selection, not explicit query-based pull. The digest's reference link and document filenames do not by themselves establish identifier-based push."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Automatic transcript-to-claim writes and later retrieval/context"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-capture-admission"
                - "memory.md#mem-rte-transcript-window"
                - "memory.md#mem-obj-memory-text"
                - "runtime.md#rt-rte-context-delivery"
              note: "Recorded conversational activity automatically yields retained claims that later invocations receive as context/guidance."
          records:
            - "runtime.md#rt-rte-capture-admission"
            - "memory.md#mem-rte-transcript-window"
            - "memory.md#mem-obj-memory-text"
            - "runtime.md#rt-rte-context-delivery"
          note: "Wired qualifies without novel claims or improvement. The cursor/window mismatch limits capture completeness, not existence."
        -
          scope: "Citation-fed durable use/tier/retention state"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-anchor-maintenance"
                - "epistemic.md#epi-rte-tier-graduation"
                - "epistemic.md#epi-rte-query-ranking"
                - "memory.md#mem-rte-memory-withdrawal"
              note: "Session citations update uses; later ranking, graduation and retention consume durable feedback state."
          records:
            - "memory.md#mem-rte-anchor-maintenance"
            - "epistemic.md#epi-rte-tier-graduation"
            - "epistemic.md#epi-rte-query-ranking"
            - "memory.md#mem-rte-memory-withdrawal"
          note: "No outcome-success oracle is required for the write-route classification; improvement remains unestablished."
        -
          scope: "Derived activity/witness warning summaries supplied at later session start"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-event-log"
                - "runtime.md#rt-rte-use-check"
                - "runtime.md#rt-rte-context-delivery"
              note: "Automatic capture/merge/source-use events produce durable orientation/warning text later supplied to the host."
          records:
            - "memory.md#mem-obj-event-log"
            - "runtime.md#rt-rte-use-check"
            - "runtime.md#rt-rte-context-delivery"
          note: "The later context is behavior-shaping material, not a training-weight update."
        -
          scope: "Explicit caller-authored updates and generated document inputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-local-edits"
            - "runtime.md#rt-rte-build-artifacts"
            - "memory.md#mem-obj-generated-documents"
          note: "Whether particular explicit content is trace-derived, and whether generated documents have a qualifying automatic later agent-consumption route, is not established. These alternatives cannot inherit another route's yes or a bounded no."
        -
          scope: "Additional flow/map routes and telemetry-to-behavior paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-code-graph"
            - "memory.md#mem-obj-savings"
          note: "Savings alone is bookkeeping, not qualifying learning; missing additional consumers prevent exhaustive learning-inventory assessment. No bounded evidenced-absence record supports a local no."
      records:
        - "runtime.md#rt-rte-capture-admission"
        - "memory.md#mem-rte-transcript-window"
        - "memory.md#mem-obj-memory-text"
        - "runtime.md#rt-rte-context-delivery"
        - "memory.md#mem-rte-anchor-maintenance"
        - "epistemic.md#epi-rte-tier-graduation"
        - "epistemic.md#epi-rte-query-ranking"
        - "memory.md#mem-rte-memory-withdrawal"
        - "memory.md#mem-obj-event-log"
        - "runtime.md#rt-rte-use-check"
        - "runtime.md#rt-rte-local-edits"
        - "runtime.md#rt-rte-build-artifacts"
        - "memory.md#mem-obj-generated-documents"
        - "memory.md#mem-obj-code-graph"
        - "memory.md#mem-obj-savings"
      note: "Supported yes findings coexist with unresolved included routes. There is no system-wide no, no observed execution, and no claim of improved capacity."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Transcript-derived claim capture"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-transcript-window"
                - "runtime.md#rt-rte-capture-admission"
              note: "Original input is recorded user/assistant conversational text, flattened from host session JSONL."
          records:
            - "memory.md#mem-rte-transcript-window"
            - "runtime.md#rt-rte-capture-admission"
          note: "Text-only flattening does not establish ingestion of arbitrary tool payloads or linked state/action/outcome trajectories."
        -
          scope: "Citation-driven selector feedback"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-capture-admission"
                - "memory.md#mem-rte-anchor-maintenance"
                - "epistemic.md#epi-rte-query-ranking"
              note: "Citation scanning of recorded session text feeds uses, then ranking/tier/retention updates."
          records:
            - "runtime.md#rt-rte-capture-admission"
            - "memory.md#mem-rte-anchor-maintenance"
            - "epistemic.md#epi-rte-query-ranking"
          note: "A uses counter is the retained derivative, not the original trace source."
        -
          scope: "Automatic event-summary memory"
          assessment: "known"
          findings:
            -
              value: "event-streams"
              basis: "wired"
              records:
                - "memory.md#mem-obj-event-log"
                - "runtime.md#rt-rte-use-check"
              note: "Discrete capture/merge/source-use findings yield timestamped retained event summaries later supplied at SessionStart."
          records:
            - "memory.md#mem-obj-event-log"
            - "runtime.md#rt-rte-use-check"
          note: "This finding concerns genuine activity events, not relabelling conversation text as events."
        -
          scope: "Other inputs mixed into event summaries and explicit feedback/content routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-event-log"
            - "runtime.md#rt-rte-capture-admission"
            - "runtime.md#rt-rte-local-edits"
            - "memory.md#mem-obj-observation-state"
          note: "Detailed provenance of every summary/input and explicit caller update is not established. Read digests record access metadata, not retained tool-result bodies; no blanket tool-traces or trajectories finding follows."
        -
          scope: "Opaque/generated and additional flow/map learning alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-generated-documents"
            - "runtime.md#rt-rte-build-artifacts"
            - "memory.md#mem-obj-code-graph"
            - "memory.md#mem-obj-savings"
          note: "Unresolved qualifying writes/later consumers leave their original trace sources unresolved. They are not made inapplicable by a known route."
      records:
        - "memory.md#mem-rte-transcript-window"
        - "runtime.md#rt-rte-capture-admission"
        - "memory.md#mem-rte-anchor-maintenance"
        - "epistemic.md#epi-rte-query-ranking"
        - "memory.md#mem-obj-event-log"
        - "runtime.md#rt-rte-use-check"
        - "runtime.md#rt-rte-local-edits"
        - "memory.md#mem-obj-observation-state"
        - "memory.md#mem-obj-generated-documents"
        - "runtime.md#rt-rte-build-artifacts"
        - "memory.md#mem-obj-code-graph"
        - "memory.md#mem-obj-savings"
      note: "Session logs and discrete events have local warrants. No record supports complete enumeration of qualifying source content or a bounded no-learning inventory."
---

# Omni-Memory memory profile

## Comparison rationale

### Inventory and evidence strength

The comparison separates retained claim prose from access metadata, code topology, file projections and control state. It does not classify the external completion models as retained memory merely because they produce text. The graph's SQLite tables establish SQLite storage; graph organization alone is not a second storage backend. JSON columns likewise establish symbolic encoding, not a key-value service. [MEM-OBJ-memory-text](memory.md#mem-obj-memory-text), [MEM-OBJ-memory-state](memory.md#mem-obj-memory-state), [MEM-OBJ-code-graph](memory.md#mem-obj-code-graph).

Every axis is partial because the accepted inventory retains unresolved alternatives. The records identify incomplete map/retained-flow consumer coverage, unknown upstream provenance and caller agency, and opaque model transformations. These limits differ by axis; the units name the prevented conclusions rather than treating every known branch as opaque. Parser fidelity alone would not erase the known graph substrate or form. The unresolved operative inventory, rather than a demand for perfect parser accuracy, prevents complete enumeration. [MEM-OBJ-code-graph](memory.md#mem-obj-code-graph), [RT-RTE-local-edits](runtime.md#rt-rte-local-edits), [MEM-OBJ-generated-documents](memory.md#mem-obj-generated-documents).

All findings are implementation wiring or documented affordances. None is observed or causally supported. Classifying automatic admission does not authenticate a human caller, and classifying learning does not establish improved capacity. The source-native manual label is deliberately not mapped to manual write agency. [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission), [RT-RTE-local-edits](runtime.md#rt-rte-local-edits), [RT-RTE-shared-import](runtime.md#rt-rte-shared-import).

### Consumer-specific forces and selection

A retained sentence can be knowledge at the foreground model and a symbolic ranking input at the lexical scorer. Row status and scope enforce active-read membership; source/tier/peer state supplies local admissibility criteria. Those local gates do not enforce the host's coding actions or certify sentence truth. Citation-fed updates have learning force at the update path and ranking force at the later selector. [EPI-RTE-query-ranking](epistemic.md#epi-rte-query-ranking), [MEM-OBJ-memory-state](memory.md#mem-obj-memory-state), [EPI-RTE-merge-disposition](epistemic.md#epi-rte-merge-disposition), [MEM-RTE-memory-withdrawal](memory.md#mem-rte-memory-withdrawal), [RT-RTE-use-check](runtime.md#rt-rte-use-check).

Managed context's instruction finding concerns retained guidance delivered through the documented standing-context path, not the shipped skill or unchanging wrapper by itself. Generated API/linkup explanations have only an afforded interpretive consumer, kept separate from wired claim delivery. [MEM-OBJ-agents-context](memory.md#mem-obj-agents-context), [MEM-OBJ-generated-documents](memory.md#mem-obj-generated-documents), [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery).

Pull describes explicit requests for stored content. Session seeds, automatic prompt hooks and compaction-context additions also push selected memory. Coarse event/recency selection is separate from prompt-term lexical ranking and actual file/symbol/co-anchor identity matches. An ID printed beside a claim, a reference link to MEMORY.md, or a requested document filename alone establishes no identifier-based push. Internal command fulfillment is not an additional push at every step of that chain. [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [MEM-OBJ-event-log](memory.md#mem-obj-event-log), [MEM-RTE-recall-search](memory.md#mem-rte-recall-search), [MEM-OBJ-code-graph](memory.md#mem-obj-code-graph).

### Transformations and trace-fed writes

Heuristic selection of standing claims from session text warrants consolidation. Opaque model output does not warrant synthesis merely because it is generated; the accepted account cannot decide each output's semantic relation from the prompt. Duplicate retirement, edits, tier graduation/withdrawal and quarantine retain their own operation warrants. Hash freshness and citation do not establish successful outcomes. [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission), [MEM-RTE-transcript-window](memory.md#mem-rte-transcript-window), [RT-RTE-build-artifacts](runtime.md#rt-rte-build-artifacts), [MEM-RTE-anchor-maintenance](memory.md#mem-rte-anchor-maintenance), [EPI-RTE-tier-graduation](epistemic.md#epi-rte-tier-graduation), [EPI-RTE-tier-withdrawal](epistemic.md#epi-rte-tier-withdrawal), [MEM-RTE-memory-withdrawal](memory.md#mem-rte-memory-withdrawal).

Automatic session extraction is a qualifying trace-fed write: conversation text produces durable claims that later retrieval supplies as context. Citation feedback changes durable priority/retention state, while activity summaries can orient a later session. These support local yes findings without training weights, new propositions or observed benefit. Session text remains session-logs even when a hook processes it; discrete capture/merge/source-use events support event-streams on their own route. Read-ledger hashes are not full tool-result content, and no linked state/action/outcome trajectory is established. [MEM-RTE-transcript-window](memory.md#mem-rte-transcript-window), [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission), [MEM-OBJ-event-log](memory.md#mem-obj-event-log), [MEM-RTE-anchor-maintenance](memory.md#mem-rte-anchor-maintenance), [MEM-OBJ-observation-state](memory.md#mem-obj-observation-state).

Unresolved explicit-content provenance and additional flow/map consumers remain in both trace inventories. No accepted evidenced-absence record supports a local no. The profile therefore neither invents a negative unit nor makes unresolved sources inapplicable. The known yes witnesses do not establish complete learning/source coverage. [RT-RTE-local-edits](runtime.md#rt-rte-local-edits), [MEM-OBJ-code-graph](memory.md#mem-obj-code-graph), [MEM-OBJ-savings](memory.md#mem-obj-savings).

### Reconciliation and source-read log

Reconciliation supersedes the workflow window-handoff identity with [MEM-RTE-transcript-window](memory.md#mem-rte-transcript-window); its model-prefix/cursor mismatch limits complete capture but does not remove the wired extraction route. It also supersedes the epistemic generated-artifact identity with [MEM-OBJ-generated-documents](memory.md#mem-obj-generated-documents); all document classifications use that canonical memory record. No other overlap is treated as replacement: the broader row container, metadata parts and narrower epistemic maintenance routes keep their own scopes.

No frozen-source files were read for this classification. All warrants come from the supplied accepted records and their annotations; no records, quotes or new evidence were added.
