---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Link memory comparison: retained Markdown, access/control caches, captures, handoffs and recovery/export state at the frozen boundary."
run-id: "AAS-2026-10-14-link-595f6f9cba36-01"
source-identity: "https://github.com/gowtham0992/link"
reviewed-boundary: "cc92f3632121b04063b24eaaf3a8c5429eaf2b57"
memory-comparison:
  version: 2
  scope: "Includes accumulated memory claims/procedures and their controls/context; wiki knowledge and links; raw/imported capture/proposal material; dismissal history; handoffs; wiki/FTS/vector access state; usage metadata; ingest ownership manifests; operation journals/checkpoints, Git/team copies and retained exports; their admission, maintenance and later consumers, including uncharacterized digest/auxiliary alternatives. Excludes unchanged shipped instructions, runtime code, external host state/compaction, provider parameters and model caches not updated through Link use, temporary evaluation corpora and unretained current-query packets. Known vector derivation retains unresolved external encoding provenance."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Memory claim, lifecycle/provenance fields, retrieval context and non-memory wiki pages"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-claim"
                - "memory.md#mem-obj-memory-controls"
                - "memory.md#mem-obj-retrieval-context"
                - "memory.md#mem-obj-wiki-pages"
              note: "Local Markdown files retain text, links and symbolic fields."
          records:
            - "memory.md#mem-obj-memory-claim"
            - "memory.md#mem-obj-memory-controls"
            - "memory.md#mem-obj-retrieval-context"
            - "memory.md#mem-obj-wiki-pages"
          note: "Markdown content and frontmatter share a filesystem store but remain distinct operative parts."
        - scope: "Raw capture notes/proposals, dismissal history and handoff packets"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-capture"
                - "epistemic.md#epi-obj-capture-proposal"
                - "memory.md#mem-obj-dismissed-proposals"
                - "memory.md#mem-obj-handoff"
              note: "All three persist as local files; JSON is encoding, not a KV substrate."
          records:
            - "memory.md#mem-obj-session-capture"
            - "epistemic.md#epi-obj-capture-proposal"
            - "memory.md#mem-obj-dismissed-proposals"
            - "memory.md#mem-obj-handoff"
          note: "Markdown captures/handoffs and JSON dismissal history are explicit retained objects."
        - scope: "Wiki index, backlinks, persistent parsed text/FTS and process maps"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-cache"
              note: "Markdown and JSON indexes/cache retain access state and text."
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-cache"
              note: "page-fts-v2.sqlite retains full-text search state."
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-cache"
              note: "Process maps retain parsed graph/search state reused by consumers."
          records:
            - "memory.md#mem-obj-wiki-cache"
          note: "The record names each cache substrate; cached payload is not another authored corpus."
        - scope: "Derived semantic vectors and usage event ring"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-semantic-index"
                - "memory.md#mem-obj-usage-ledger"
              note: "Dense vectors and usage metadata are stored in files, not a vector database."
          records:
            - "memory.md#mem-obj-semantic-index"
            - "memory.md#mem-obj-usage-ledger"
          note: "Both are explicit local JSON stores."
        - scope: "Structured ingest source/output ownership manifest"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-structured-ingest"
                - "epistemic.md#epi-rte-export-rendering"
                - "epistemic.md#epi-rte-staged-disposition"
              note: "The manifest and generated outputs persist locally."
          records:
            - "runtime.md#rt-rte-structured-ingest"
            - "epistemic.md#epi-rte-export-rendering"
            - "epistemic.md#epi-rte-staged-disposition"
          note: "Ownership hashes persist under .link-ingest and are consumed by later apply."
        - scope: "Operation markers, pre-write snapshots and backup archives"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-operation-journal"
                - "runtime.md#rt-rte-local-recovery"
              note: "Markers, snapshots and backup archives are local filesystem objects."
          records:
            - "runtime.md#rt-obj-operation-journal"
            - "runtime.md#rt-rte-local-recovery"
          note: "Recovery retains filesystem checkpoints with distinct metadata and byte payloads."
        - scope: "Git-synchronized workspace and team copies"
          assessment: "known"
          findings:
            - value: "repo"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-workspace-sync"
              note: "Git commits and merges retain workspace versions."
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-workspace-sync"
              note: "Local/team imported Markdown is reparsed for later recall."
          records:
            - "runtime.md#rt-rte-workspace-sync"
          note: "Git history is operative retained recovery/synchronization state, distinct from the Markdown copies."
        - scope: "Exported HTML, manifest and retained audit JSON"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-rte-retained-export"
              note: "Explicit export creates retained files for later documented readers."
          records:
            - "memory.md#mem-rte-retained-export"
          note: "The durable exports are distinct from a live permalink, which does not create another retained store."
        - scope: "Detailed digest and auxiliary output inventory"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-consolidation-plan"
            - "memory.md#mem-obj-wiki-pages"
            - "memory.md#mem-rte-retained-export"
          note: "The memory coverage account leaves digest and auxiliary internals uninspected; their complete retained-object inventory cannot be classified."
      records:
        - "memory.md#mem-obj-memory-claim"
        - "memory.md#mem-obj-memory-controls"
        - "memory.md#mem-obj-retrieval-context"
        - "memory.md#mem-obj-wiki-pages"
        - "memory.md#mem-obj-session-capture"
        - "epistemic.md#epi-obj-capture-proposal"
        - "memory.md#mem-obj-dismissed-proposals"
        - "memory.md#mem-obj-handoff"
        - "memory.md#mem-obj-wiki-cache"
        - "memory.md#mem-obj-semantic-index"
        - "memory.md#mem-obj-usage-ledger"
        - "runtime.md#rt-rte-structured-ingest"
        - "epistemic.md#epi-rte-export-rendering"
        - "epistemic.md#epi-rte-staged-disposition"
        - "runtime.md#rt-obj-operation-journal"
        - "runtime.md#rt-rte-local-recovery"
        - "runtime.md#rt-rte-workspace-sync"
        - "memory.md#mem-rte-retained-export"
        - "memory.md#mem-rte-consolidation-plan"
      note: "The named content, control, cache and checkpoint stores are classified. Detailed digest and auxiliary retained outputs are not inventoried by accepted records; no whole-runtime storage union is asserted."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Claim/procedure text, retrieval context and wiki prose at interpreting agents and human readers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-claim"
                - "memory.md#mem-obj-retrieval-context"
                - "memory.md#mem-obj-wiki-pages"
              note: "Readable claims, procedures and authored explanations use natural language."
          records:
            - "memory.md#mem-obj-memory-claim"
            - "memory.md#mem-obj-retrieval-context"
            - "memory.md#mem-obj-wiki-pages"
          note: "Text is interpreted as context, advice or steps; context is also an undelivered selector input."
        - scope: "Memory lifecycle/project fields and wiki links/frontmatter at code selectors"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-controls"
                - "memory.md#mem-obj-wiki-pages"
              note: "Statuses, dates, project identifiers, links and ownership labels have fixed consumers."
          records:
            - "memory.md#mem-obj-memory-controls"
            - "memory.md#mem-obj-wiki-pages"
          note: "Fixed comparisons and graph resolution consume localized symbolic fields."
        - scope: "Capture notes, candidate text, decision trail and handoff task substance"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-capture"
                - "epistemic.md#epi-obj-capture-proposal"
                - "memory.md#mem-obj-handoff"
              note: "Reviewers/agents interpret notes, candidate claims, reasons and next steps."
          records:
            - "memory.md#mem-obj-session-capture"
            - "epistemic.md#epi-obj-capture-proposal"
            - "memory.md#mem-obj-handoff"
          note: "Text and metadata are split by consumption path."
        - scope: "Capture/proposal metadata, dismissal fingerprints and handoff eligibility fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-capture"
                - "epistemic.md#epi-obj-capture-proposal"
                - "memory.md#mem-obj-dismissed-proposals"
                - "memory.md#mem-obj-handoff"
              note: "Fixed metadata rules select, suppress and expire retained parts."
          records:
            - "memory.md#mem-obj-session-capture"
            - "epistemic.md#epi-obj-capture-proposal"
            - "memory.md#mem-obj-dismissed-proposals"
            - "memory.md#mem-obj-handoff"
          note: "Code uses project/date/type/confidence/expiry fields and fingerprint membership."
        - scope: "Wiki cached article strings at returned-content consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-cache"
              note: "Cached article text reaches later readers through retrieval."
          records:
            - "memory.md#mem-obj-wiki-cache"
          note: "Cached text preserves the readable payload rather than creating new claims."
        - scope: "Wiki graph/search/access indexes and usage ledger"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-cache"
                - "memory.md#mem-obj-usage-ledger"
              note: "Indexes and event metadata are localized selector inputs."
          records:
            - "memory.md#mem-obj-wiki-cache"
            - "memory.md#mem-obj-usage-ledger"
          note: "Graph links, token/FTS structures and event name/time/kind fields have fixed code consumers."
        - scope: "Semantic vectors at cosine/standout ranking"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-semantic-index"
              note: "Dense distributed numerical representations influence later ranking."
          records:
            - "memory.md#mem-obj-semantic-index"
          note: "Dense representation is separate from symbolic model and text-hash metadata."
        - scope: "Semantic cache identity/hash/version fields and ingest manifests"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-semantic-index"
                - "runtime.md#rt-rte-structured-ingest"
              note: "Fixed keys and hashes govern refresh and replacement."
          records:
            - "memory.md#mem-obj-semantic-index"
            - "runtime.md#rt-rte-structured-ingest"
          note: "Hash/model/version and ownership comparisons are symbolic controls."
        - scope: "Journal markers and checkpoint manifests at recovery software"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-operation-journal"
                - "runtime.md#rt-rte-local-recovery"
              note: "Recovery code consumes localized status/path records."
          records:
            - "runtime.md#rt-obj-operation-journal"
            - "runtime.md#rt-rte-local-recovery"
          note: "Status, touched paths and snapshot manifests determine recovery actions."
        - scope: "Checkpoint, Git-copy and export content payloads"
          assessment: "partial"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-operation-journal"
                - "runtime.md#rt-rte-local-recovery"
                - "runtime.md#rt-rte-workspace-sync"
                - "memory.md#mem-rte-retained-export"
                - "memory.md#mem-obj-memory-claim"
                - "memory.md#mem-obj-wiki-pages"
              note: "Snapshots/exports can preserve readable remembered claims and articles."
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-operation-journal"
                - "runtime.md#rt-rte-local-recovery"
                - "runtime.md#rt-rte-workspace-sync"
                - "memory.md#mem-rte-retained-export"
                - "memory.md#mem-obj-memory-controls"
              note: "Copied lifecycle/provenance fields and audit/HTML manifests preserve localized metadata."
          records:
            - "runtime.md#rt-obj-operation-journal"
            - "runtime.md#rt-rte-local-recovery"
            - "runtime.md#rt-rte-workspace-sync"
            - "memory.md#mem-rte-retained-export"
            - "memory.md#mem-obj-memory-claim"
            - "memory.md#mem-obj-wiki-pages"
          note: "Known text/control copies remain included; arbitrary opted-in raw bytes are not fully characterized."
        - scope: "Detailed digest and auxiliary derived payloads"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-consolidation-plan"
            - "memory.md#mem-obj-wiki-pages"
          note: "No accepted record establishes their complete operative forms."
      records:
        - "memory.md#mem-obj-memory-claim"
        - "memory.md#mem-obj-retrieval-context"
        - "memory.md#mem-obj-wiki-pages"
        - "memory.md#mem-obj-memory-controls"
        - "memory.md#mem-obj-session-capture"
        - "epistemic.md#epi-obj-capture-proposal"
        - "memory.md#mem-obj-handoff"
        - "memory.md#mem-obj-dismissed-proposals"
        - "memory.md#mem-obj-wiki-cache"
        - "memory.md#mem-obj-usage-ledger"
        - "memory.md#mem-obj-semantic-index"
        - "runtime.md#rt-rte-structured-ingest"
        - "runtime.md#rt-obj-operation-journal"
        - "runtime.md#rt-rte-local-recovery"
        - "runtime.md#rt-rte-workspace-sync"
        - "memory.md#mem-rte-retained-export"
        - "memory.md#mem-rte-consolidation-plan"
      note: "Natural-language payload, symbolic controls and dense numerical access state are retained separately. Detailed digest and auxiliary payloads remain unresolved; static model parameters are excluded, not reclassified as use-derived memory."
    lineage:
      assessment: "partial"
      units:
        - scope: "Caller-authored memory detail and standalone handoff text on the described authoring paths"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-claim"
                - "memory.md#mem-rte-memory-lifecycle"
                - "memory.md#mem-obj-handoff"
              note: "Caller-supplied claims/updates and standalone relay text are authored inputs."
          records:
            - "memory.md#mem-obj-memory-claim"
            - "memory.md#mem-rte-memory-lifecycle"
            - "memory.md#mem-obj-handoff"
          note: "Authored describes the content path, not authenticated human control."
        - scope: "External vault, project document, structured export and remote workspace transfer paths"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-source-import"
                - "runtime.md#rt-rte-project-seed"
                - "runtime.md#rt-rte-structured-ingest"
                - "epistemic.md#epi-rte-export-rendering"
                - "runtime.md#rt-rte-workspace-sync"
              note: "External Markdown, project content, supported exports and remote copies enter local retained state."
          records:
            - "runtime.md#rt-rte-source-import"
            - "runtime.md#rt-rte-project-seed"
            - "runtime.md#rt-rte-structured-ingest"
            - "epistemic.md#epi-rte-export-rendering"
            - "runtime.md#rt-rte-workspace-sync"
          note: "Imported describes acquisition of preexisting content; subsequent rendering is separate."
        - scope: "Automatic transcript extraction, proposal normalization and recorded use/dismissal/operation history"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-capture"
                - "memory.md#mem-obj-session-capture"
                - "epistemic.md#epi-rte-proposal-normalization"
                - "memory.md#mem-obj-usage-ledger"
                - "memory.md#mem-obj-dismissed-proposals"
                - "runtime.md#rt-obj-operation-journal"
              note: "Transcript-derived notes/proposals and activity-derived event/fingerprint/status records retain extracted experience."
          records:
            - "runtime.md#rt-rte-session-capture"
            - "memory.md#mem-obj-session-capture"
            - "epistemic.md#epi-rte-proposal-normalization"
            - "memory.md#mem-obj-usage-ledger"
            - "memory.md#mem-obj-dismissed-proposals"
            - "runtime.md#rt-obj-operation-journal"
          note: "Trace derivation is local to activity-derived notes, candidates and controls, not every imported instruction."
        - scope: "Wiki indexes, dense vector cache and deterministic structured/project rendering"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-cache"
                - "memory.md#mem-obj-semantic-index"
                - "epistemic.md#epi-rte-export-rendering"
                - "runtime.md#rt-rte-project-seed"
              note: "Parsing/indexing, embedding and deterministic rendering compile retained inputs into access state or source pages."
          records:
            - "memory.md#mem-obj-wiki-cache"
            - "memory.md#mem-obj-semantic-index"
            - "epistemic.md#epi-rte-export-rendering"
            - "runtime.md#rt-rte-project-seed"
          note: "Fixed parsing, rendering and numerical encoding derive new retained representations."
        - scope: "External agent wiki authoring, query filing and research synthesis"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-agent-wiki"
                - "memory.md#mem-obj-wiki-pages"
              note: "External agents are instructed to author source/concept/answer pages from selected material."
          records:
            - "runtime.md#rt-rte-agent-wiki"
            - "memory.md#mem-obj-wiki-pages"
          note: "The source establishes the requested agent-authored path, not an executed semantic synthesis."
        - scope: "Initial provenance of caller/imported claim and handoff content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-memory-claim"
            - "memory.md#mem-obj-retrieval-context"
            - "memory.md#mem-obj-memory-controls"
            - "memory.md#mem-obj-handoff"
            - "runtime.md#rt-rte-workspace-sync"
          note: "Source strings and generic caller identity do not distinguish original authoring, import or trace origin for every payload."
        - scope: "Embedding provenance beyond known memory-text encoding"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-semantic-index"
            - "runtime.md#rt-cmp-model2vec"
            - "runtime.md#rt-cmp-fastembed"
          note: "The derived vector input is known, but exact external weights and their initial provenance are uninspected; known compilation does not resolve it."
        - scope: "Detailed digest and auxiliary derivation paths"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-consolidation-plan"
            - "memory.md#mem-obj-wiki-pages"
          note: "Their lineage is not characterized by accepted records."
      records:
        - "memory.md#mem-obj-memory-claim"
        - "memory.md#mem-rte-memory-lifecycle"
        - "memory.md#mem-obj-handoff"
        - "runtime.md#rt-rte-source-import"
        - "runtime.md#rt-rte-project-seed"
        - "runtime.md#rt-rte-structured-ingest"
        - "epistemic.md#epi-rte-export-rendering"
        - "runtime.md#rt-rte-workspace-sync"
        - "runtime.md#rt-rte-session-capture"
        - "memory.md#mem-obj-session-capture"
        - "epistemic.md#epi-rte-proposal-normalization"
        - "memory.md#mem-obj-usage-ledger"
        - "memory.md#mem-obj-dismissed-proposals"
        - "runtime.md#rt-obj-operation-journal"
        - "memory.md#mem-obj-wiki-cache"
        - "memory.md#mem-obj-semantic-index"
        - "runtime.md#rt-rte-agent-wiki"
        - "memory.md#mem-obj-wiki-pages"
        - "memory.md#mem-obj-retrieval-context"
        - "memory.md#mem-obj-memory-controls"
        - "runtime.md#rt-cmp-model2vec"
        - "runtime.md#rt-cmp-fastembed"
        - "memory.md#mem-rte-consolidation-plan"
      note: "Known production and transfer paths coexist with caller-controlled source labels, unknown initial authorship and unpinned embedding provenance. No known derivation resolves those initial-content gaps."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Memory claims and wiki content at later answering agents/human readers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-claim"
                - "memory.md#mem-obj-wiki-pages"
                - "runtime.md#rt-rte-context-recall"
                - "memory.md#mem-rte-wiki-read"
              note: "Selected claims/articles supply facts, advice and source context."
          records:
            - "memory.md#mem-obj-memory-claim"
            - "memory.md#mem-obj-wiki-pages"
            - "runtime.md#rt-rte-context-recall"
            - "memory.md#mem-rte-wiki-read"
          note: "Focused recall and independent generic wiki selection supply context, not truth acceptance."
        - scope: "Retained procedures, handoff next steps and saved-constraint reminders at host agents"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-claim"
                - "memory.md#mem-obj-handoff"
                - "runtime.md#rt-rte-session-delivery"
                - "memory.md#mem-rte-guard-reminder"
              note: "Procedure steps, priority resume guidance and conflict-confirmation reminders direct later work."
          records:
            - "memory.md#mem-obj-memory-claim"
            - "memory.md#mem-obj-handoff"
            - "runtime.md#rt-rte-session-delivery"
            - "memory.md#mem-rte-guard-reminder"
          note: "Natural-language force is distinct from mechanical permission controls."
        - scope: "Claim/title/TLDR/body/context, dense vectors, graph/search features and reviewed metadata at rankers"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-claim"
                - "memory.md#mem-obj-retrieval-context"
                - "memory.md#mem-obj-semantic-index"
                - "memory.md#mem-obj-wiki-cache"
                - "epistemic.md#epi-rte-review-marking"
                - "runtime.md#rt-rte-context-recall"
              note: "Text, vectors, links and review status influence relative result priority."
          records:
            - "memory.md#mem-obj-memory-claim"
            - "memory.md#mem-obj-retrieval-context"
            - "memory.md#mem-obj-semantic-index"
            - "memory.md#mem-obj-wiki-cache"
            - "epistemic.md#epi-rte-review-marking"
            - "runtime.md#rt-rte-context-recall"
          note: "Ranking includes retained content scored by fixed code; no learned ranking policy is required."
        - scope: "Lifecycle/project fields and dismissal membership at focused selection/proposal admission"
          assessment: "known"
          findings:
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-controls"
                - "memory.md#mem-obj-dismissed-proposals"
                - "memory.md#mem-rte-capture-cleanup"
                - "runtime.md#rt-rte-session-capture"
                - "epistemic.md#epi-rte-memory-withdrawal"
              note: "Inactive/out-of-project records and dismissed proposals are excluded on their respective covered paths."
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memory-controls"
                - "memory.md#mem-obj-dismissed-proposals"
                - "memory.md#mem-rte-capture-cleanup"
                - "runtime.md#rt-rte-session-capture"
                - "epistemic.md#epi-rte-memory-withdrawal"
              note: "Dismissal fingerprints supply the criterion against which future proposal candidates are checked."
          records:
            - "memory.md#mem-obj-memory-controls"
            - "memory.md#mem-obj-dismissed-proposals"
            - "memory.md#mem-rte-capture-cleanup"
            - "runtime.md#rt-rte-session-capture"
            - "epistemic.md#epi-rte-memory-withdrawal"
          note: "These controls can veto their covered code paths; generic wiki delivery bypasses focused lifecycle gates."
        - scope: "Ownership manifests at later structured apply"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-structured-ingest"
                - "epistemic.md#epi-rte-staged-disposition"
              note: "Ownership hashes determine replacement admissibility."
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-structured-ingest"
                - "epistemic.md#epi-rte-staged-disposition"
              note: "Modified or unmanaged output conflicts block replacement unless the permitted alternative is explicitly selected."
          records:
            - "runtime.md#rt-rte-structured-ingest"
            - "epistemic.md#epi-rte-staged-disposition"
          note: "Retained source/output hashes determine managed replacement versus conflict."
        - scope: "Usage event names/times at guard cooldown and optional salience consumer"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-usage-ledger"
                - "memory.md#mem-rte-usage-feedback"
                - "memory.md#mem-rte-guard-reminder"
              note: "Recent guard event identity/time chooses emit versus silence."
          records:
            - "memory.md#mem-obj-usage-ledger"
            - "memory.md#mem-rte-usage-feedback"
            - "memory.md#mem-rte-guard-reminder"
          note: "Live cooldown and optional popularity ranking are distinct consumers."
        - scope: "Usage event counts at optional library salience ranking"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-usage-ledger"
                - "memory.md#mem-rte-usage-feedback"
              note: "Retained retrieval frequency can influence caller-provided ranking boosts."
          records:
            - "memory.md#mem-obj-usage-ledger"
            - "memory.md#mem-rte-usage-feedback"
          note: "The optional boost can be supplied to ranking; inspected ordinary adapters do not wire it."
        - scope: "Capture notes at accept-time re-mining and retained-memory production"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-capture"
                - "runtime.md#rt-rte-session-capture"
                - "runtime.md#rt-rte-memory-admission"
              note: "Stored session material feeds a later durable behavior-shaping memory update."
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-capture"
                - "runtime.md#rt-rte-session-capture"
                - "runtime.md#rt-rte-memory-admission"
              note: "Notes/provenance and decision trail provide reviewer context at inbox/acceptance."
          records:
            - "memory.md#mem-obj-session-capture"
            - "runtime.md#rt-rte-session-capture"
            - "runtime.md#rt-rte-memory-admission"
          note: "Retained conversational experience feeds extraction into durable future-context claims; caller acceptance remains separately controlled."
        - scope: "Journal markers and snapshot manifests at explicit recovery"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-operation-journal"
                - "runtime.md#rt-rte-local-recovery"
              note: "Operation state and manifests choose target paths and recovery actions."
          records:
            - "runtime.md#rt-obj-operation-journal"
            - "runtime.md#rt-rte-local-recovery"
          note: "Recovery uses retained paths/status to choose restoration work; it does not treat markers as agent factual knowledge."
        - scope: "Exported summaries/articles at documented offline readers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-retained-export"
              note: "Offline/security readers can consume exported article and audit context."
          records:
            - "memory.md#mem-rte-retained-export"
          note: "Production of files is wired; the later external reader role is documented rather than deployed."
        - scope: "Detailed digest and auxiliary retained-part consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-consolidation-plan"
            - "memory.md#mem-obj-wiki-pages"
            - "memory.md#mem-rte-retained-export"
          note: "Unknown payload and consumer paths prevent a complete authority inventory."
      records:
        - "memory.md#mem-obj-memory-claim"
        - "memory.md#mem-obj-wiki-pages"
        - "runtime.md#rt-rte-context-recall"
        - "memory.md#mem-rte-wiki-read"
        - "memory.md#mem-obj-handoff"
        - "runtime.md#rt-rte-session-delivery"
        - "memory.md#mem-rte-guard-reminder"
        - "memory.md#mem-obj-retrieval-context"
        - "memory.md#mem-obj-semantic-index"
        - "memory.md#mem-obj-wiki-cache"
        - "epistemic.md#epi-rte-review-marking"
        - "memory.md#mem-obj-memory-controls"
        - "memory.md#mem-obj-dismissed-proposals"
        - "memory.md#mem-rte-capture-cleanup"
        - "runtime.md#rt-rte-session-capture"
        - "epistemic.md#epi-rte-memory-withdrawal"
        - "runtime.md#rt-rte-structured-ingest"
        - "epistemic.md#epi-rte-staged-disposition"
        - "memory.md#mem-obj-usage-ledger"
        - "memory.md#mem-rte-usage-feedback"
        - "memory.md#mem-obj-session-capture"
        - "runtime.md#rt-rte-memory-admission"
        - "runtime.md#rt-obj-operation-journal"
        - "runtime.md#rt-rte-local-recovery"
        - "memory.md#mem-rte-retained-export"
        - "memory.md#mem-rte-consolidation-plan"
      note: "Findings name actual consumers/effects, including ranking by retained text and controls. External compliance/benefit is not observed; unknown auxiliary consumers prevent complete inventory coverage."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Automatic session hook capture, index/vector refresh, usage recording and journal snapshot production"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-capture"
                - "memory.md#mem-obj-session-capture"
                - "memory.md#mem-obj-wiki-cache"
                - "memory.md#mem-obj-semantic-index"
                - "memory.md#mem-obj-usage-ledger"
                - "runtime.md#rt-obj-operation-journal"
                - "runtime.md#rt-rte-local-recovery"
              note: "Hook extraction, cache compilation, accounting and pre-write checkpointing admit content automatically."
          records:
            - "runtime.md#rt-rte-session-capture"
            - "memory.md#mem-obj-session-capture"
            - "memory.md#mem-obj-wiki-cache"
            - "memory.md#mem-obj-semantic-index"
            - "memory.md#mem-obj-usage-ledger"
            - "runtime.md#rt-obj-operation-journal"
            - "runtime.md#rt-rte-local-recovery"
          note: "Software admits these generated records without a per-content human decision."
        - scope: "Project seed content production and software Git/team reconciliation"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-project-seed"
                - "runtime.md#rt-rte-workspace-sync"
              note: "Code selects/renders seed material and admits eligible reconciled/imported copies."
          records:
            - "runtime.md#rt-rte-project-seed"
            - "runtime.md#rt-rte-workspace-sync"
          note: "Caller initiation/options do not approve each generated/imported passage."
        - scope: "Structured rendered-page admission after caller apply and staged code gate"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-structured-ingest"
                - "epistemic.md#epi-rte-staged-disposition"
                - "epistemic.md#epi-rte-export-rendering"
              note: "Software-generated pages are admitted after structural/ownership checks."
          records:
            - "runtime.md#rt-rte-structured-ingest"
            - "epistemic.md#epi-rte-staged-disposition"
            - "epistemic.md#epi-rte-export-rendering"
          note: "Applying a workflow is not a per-claim human approval; code admits generated staged content on its finite conditions."
        - scope: "Agent-authored wiki ingest within workflow authorization"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-agent-wiki"
                - "memory.md#mem-obj-wiki-pages"
              note: "The model/agent is directed to admit authored wiki claims under the ingest request."
          records:
            - "runtime.md#rt-rte-agent-wiki"
            - "memory.md#mem-obj-wiki-pages"
          note: "Shipped procedure delegates claim extraction/authoring to the external agent rather than requiring per-claim assent."
        - scope: "Human-supplied/approved remember, selected capture, review and edit protocol"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-memory-admission"
                - "runtime.md#rt-clm-approved-memory"
                - "epistemic.md#epi-rte-review-marking"
                - "epistemic.md#epi-clm-review-accuracy"
                - "memory.md#mem-rte-consolidation-plan"
              note: "The protocol asks the human to supply/approve remembered content and accuracy review or approve each planned maintenance action."
          records:
            - "runtime.md#rt-rte-memory-admission"
            - "runtime.md#rt-clm-approved-memory"
            - "epistemic.md#epi-rte-review-marking"
            - "epistemic.md#epi-clm-review-accuracy"
            - "memory.md#mem-rte-consolidation-plan"
          note: "The documented human decision qualifies manual at this layer only; core calls do not authenticate its occurrence."
        - scope: "Actual ordinary writer, capture acceptance, lifecycle and handoff caller control"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-memory-admission"
            - "runtime.md#rt-rte-session-capture"
            - "memory.md#mem-rte-memory-lifecycle"
            - "epistemic.md#epi-rte-review-marking"
            - "memory.md#mem-obj-handoff"
          note: "Generic callable caller identity and confirmation flags do not establish a human decision or its absence for each admitted part."
        - scope: "Dismissal/cleanup, direct Markdown adoption and explicit restore replacement control"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-capture-cleanup"
            - "memory.md#mem-obj-dismissed-proposals"
            - "memory.md#mem-obj-memory-claim"
            - "memory.md#mem-obj-wiki-pages"
            - "runtime.md#rt-rte-local-recovery"
          note: "Software I/O and caller selection/confirm alone do not identify whether a human supplied, approved or replaced this retained content."
        - scope: "Detailed digest and auxiliary admission mechanisms"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-consolidation-plan"
            - "memory.md#mem-obj-wiki-pages"
            - "memory.md#mem-rte-retained-export"
          note: "Admission control for these included alternatives is uninspected."
      records:
        - "runtime.md#rt-rte-session-capture"
        - "memory.md#mem-obj-session-capture"
        - "memory.md#mem-obj-wiki-cache"
        - "memory.md#mem-obj-semantic-index"
        - "memory.md#mem-obj-usage-ledger"
        - "runtime.md#rt-obj-operation-journal"
        - "runtime.md#rt-rte-local-recovery"
        - "runtime.md#rt-rte-project-seed"
        - "runtime.md#rt-rte-workspace-sync"
        - "runtime.md#rt-rte-structured-ingest"
        - "epistemic.md#epi-rte-staged-disposition"
        - "epistemic.md#epi-rte-export-rendering"
        - "runtime.md#rt-rte-agent-wiki"
        - "memory.md#mem-obj-wiki-pages"
        - "runtime.md#rt-rte-memory-admission"
        - "runtime.md#rt-clm-approved-memory"
        - "epistemic.md#epi-rte-review-marking"
        - "epistemic.md#epi-clm-review-accuracy"
        - "memory.md#mem-rte-consolidation-plan"
        - "memory.md#mem-rte-memory-lifecycle"
        - "memory.md#mem-obj-handoff"
        - "memory.md#mem-rte-capture-cleanup"
        - "memory.md#mem-obj-dismissed-proposals"
        - "memory.md#mem-obj-memory-claim"
        - "memory.md#mem-rte-retained-export"
      note: "Automatic software/model admission is not made manual by workflow initiation. Explicit human decisions are supported at the protocol layer; generic caller identity, file adoption and replacement control remain unresolved locally."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Session transcript-to-proposal/notes extraction"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-capture"
                - "memory.md#mem-obj-session-capture"
                - "epistemic.md#epi-rte-proposal-normalization"
              note: "Bounded extraction/mining reduces conversational material into retained notes and proposed standing claims."
          records:
            - "runtime.md#rt-rte-session-capture"
            - "memory.md#mem-obj-session-capture"
            - "epistemic.md#epi-rte-proposal-normalization"
          note: "Extracting standing candidates from retained session turns reduces existing content. Speaker/time fidelity defects do not establish synthesis."
        - scope: "Memory append, review/supersession/archive, forget and explicit visibility/lifecycle mutation"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-lifecycle"
                - "epistemic.md#epi-rte-review-marking"
                - "memory.md#mem-obj-memory-controls"
                - "runtime.md#rt-rte-memory-admission"
              note: "Appending detail and changing review/lifecycle fields revises existing entries."
            - value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-lifecycle"
                - "epistemic.md#epi-rte-review-marking"
                - "memory.md#mem-obj-memory-controls"
                - "runtime.md#rt-rte-memory-admission"
              note: "Archive/supersession and expiry withdraw focused current reliance while retaining historical content."
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-lifecycle"
                - "epistemic.md#epi-rte-review-marking"
                - "memory.md#mem-obj-memory-controls"
                - "runtime.md#rt-rte-memory-admission"
              note: "Confirmed forget removes the current retained page."
            - value: "promote"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-lifecycle"
                - "epistemic.md#epi-rte-review-marking"
                - "memory.md#mem-obj-memory-controls"
                - "runtime.md#rt-rte-memory-admission"
              note: "Reviewed metadata supplies a positive ranking boost at its later selector."
          records:
            - "memory.md#mem-rte-memory-lifecycle"
            - "epistemic.md#epi-rte-review-marking"
            - "memory.md#mem-obj-memory-controls"
            - "runtime.md#rt-rte-memory-admission"
          note: "Different effects remain separate; archive is branch-local withdrawal and forget is not all-copy erasure."
        - scope: "Capture redundant-copy cleanup and bounded dismissal history"
          assessment: "known"
          findings:
            - value: "dedup"
              basis: "wired"
              records:
                - "memory.md#mem-rte-capture-cleanup"
                - "memory.md#mem-obj-dismissed-proposals"
              note: "Applied newest-first cleanup removes redundant capture copies."
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-capture-cleanup"
                - "memory.md#mem-obj-dismissed-proposals"
              note: "Redaction edits retained capture content."
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-capture-cleanup"
                - "memory.md#mem-obj-dismissed-proposals"
              note: "Capture deletion and the 500-entry dismissal FIFO forget retained content/control history."
          records:
            - "memory.md#mem-rte-capture-cleanup"
            - "memory.md#mem-obj-dismissed-proposals"
          note: "Dedup removes redundant retained captures, distinct from rejecting a new primary-key collision."
        - scope: "Handoff expiry and usage event retention"
          assessment: "known"
          findings:
            - value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-handoff"
                - "memory.md#mem-obj-usage-ledger"
                - "memory.md#mem-rte-usage-feedback"
              note: "Expired handoffs are withheld from pending delivery while their files remain."
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-obj-handoff"
                - "memory.md#mem-obj-usage-ledger"
                - "memory.md#mem-rte-usage-feedback"
              note: "The bounded usage ring forgets older access events."
          records:
            - "memory.md#mem-obj-handoff"
            - "memory.md#mem-obj-usage-ledger"
            - "memory.md#mem-rte-usage-feedback"
          note: "Expiry leaves handoff history but stops current surfacing; the usage ring discards old events."
        - scope: "Backup count pruning and structured managed update/prune"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-local-recovery"
                - "runtime.md#rt-rte-structured-ingest"
              note: "Backup retention pruning and explicit obsolete-output pruning remove retained copies."
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-local-recovery"
                - "runtime.md#rt-rte-structured-ingest"
              note: "Managed source changes regenerate existing structured outputs."
          records:
            - "runtime.md#rt-rte-local-recovery"
            - "runtime.md#rt-rte-structured-ingest"
          note: "Count retention removes older archives; managed output refresh revises existing pages and explicit prune removes obsolete outputs."
        - scope: "External-agent wiki revision and research-chat synthesis"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-agent-wiki"
                - "memory.md#mem-obj-wiki-pages"
                - "runtime.md#rt-rte-session-capture"
              note: "Agents are instructed to update existing pages with source-linked information."
            - value: "consolidate"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-agent-wiki"
                - "memory.md#mem-obj-wiki-pages"
                - "runtime.md#rt-rte-session-capture"
              note: "Research-chat capture is instructed to extract substance instead of dumping the back-and-forth."
            - value: "synthesize"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-agent-wiki"
                - "memory.md#mem-obj-wiki-pages"
                - "runtime.md#rt-rte-session-capture"
              note: "Authored comparisons, reasonable inferences and speculative claims can add propositions beyond the source statements."
          records:
            - "runtime.md#rt-rte-agent-wiki"
            - "memory.md#mem-obj-wiki-pages"
            - "runtime.md#rt-rte-session-capture"
          note: "Requested operations are classified as doctrine, not an observed or guaranteed semantic transformation."
        - scope: "Read-only consolidation proposals versus unspecified subsequent semantic merge"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-consolidation-plan"
            - "memory.md#mem-rte-memory-lifecycle"
          note: "The planner writes no successor; separately invoked append/archive/delete are known, but no accepted record establishes an additional applied semantic merge."
        - scope: "Detailed digest and auxiliary content-maintenance transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-consolidation-plan"
            - "memory.md#mem-obj-wiki-pages"
          note: "Names alone do not establish synthesis, consolidation or absence of either."
      records:
        - "runtime.md#rt-rte-session-capture"
        - "memory.md#mem-obj-session-capture"
        - "epistemic.md#epi-rte-proposal-normalization"
        - "memory.md#mem-rte-memory-lifecycle"
        - "epistemic.md#epi-rte-review-marking"
        - "memory.md#mem-obj-memory-controls"
        - "runtime.md#rt-rte-memory-admission"
        - "memory.md#mem-rte-capture-cleanup"
        - "memory.md#mem-obj-dismissed-proposals"
        - "memory.md#mem-obj-handoff"
        - "memory.md#mem-obj-usage-ledger"
        - "memory.md#mem-rte-usage-feedback"
        - "runtime.md#rt-rte-local-recovery"
        - "runtime.md#rt-rte-structured-ingest"
        - "runtime.md#rt-rte-agent-wiki"
        - "memory.md#mem-obj-wiki-pages"
        - "memory.md#mem-rte-consolidation-plan"
      note: "Implemented transformations and requested external-agent transformations retain distinct bases. The read-only consolidation planner establishes no applied merge, while unread digest/auxiliary branches remain unresolved."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "CLI/MCP/HTTP focused and generic recall, explain, full context and direct requested files"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-recall"
                - "memory.md#mem-rte-wiki-read"
                - "memory.md#mem-obj-memory-claim"
                - "memory.md#mem-obj-memory-controls"
                - "memory.md#mem-obj-wiki-pages"
              note: "Request fulfillment returns selected memory/wiki content and provenance."
          records:
            - "runtime.md#rt-rte-context-recall"
            - "memory.md#mem-rte-wiki-read"
            - "memory.md#mem-obj-memory-claim"
            - "memory.md#mem-obj-memory-controls"
            - "memory.md#mem-obj-wiki-pages"
          note: "The consumer requests retained material; ranking and delivery inside that request do not add a second push."
        - scope: "Inbox/acceptance, maintenance, sync and explicit recovery consumers"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-capture"
                - "memory.md#mem-obj-session-capture"
                - "memory.md#mem-rte-capture-cleanup"
                - "memory.md#mem-rte-consolidation-plan"
                - "runtime.md#rt-rte-structured-ingest"
                - "runtime.md#rt-rte-workspace-sync"
                - "runtime.md#rt-rte-local-recovery"
              note: "Explicit review, acceptance, maintenance and restoration requests read retained state."
          records:
            - "runtime.md#rt-rte-session-capture"
            - "memory.md#mem-obj-session-capture"
            - "memory.md#mem-rte-capture-cleanup"
            - "memory.md#mem-rte-consolidation-plan"
            - "runtime.md#rt-rte-structured-ingest"
            - "runtime.md#rt-rte-workspace-sync"
            - "runtime.md#rt-rte-local-recovery"
          note: "Requested operations consume prior notes, controls, checkpoints and files."
        - scope: "Startup hooks and first suitable MCP response autobrief"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-delivery"
                - "memory.md#mem-obj-handoff"
                - "memory.md#mem-obj-session-capture"
              note: "Automatic selectors add retained brief, capture-review and handoff material to later host context."
          records:
            - "runtime.md#rt-rte-session-delivery"
            - "memory.md#mem-obj-handoff"
            - "memory.md#mem-obj-session-capture"
          note: "Independent memory/handoff/review supply is not an explicit request for these retained parts."
        - scope: "Per-prompt saved-constraint reminder"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-guard-reminder"
                - "memory.md#mem-rte-usage-feedback"
              note: "The guard supplies one matching saved constraint when overlap and cooldown permit."
          records:
            - "memory.md#mem-rte-guard-reminder"
            - "memory.md#mem-rte-usage-feedback"
          note: "Prompt submission triggers an automatic constraint selector, not an explicit recall request."
        - scope: "Wiki/vector selection state and retained cooldown/dismissal controls at later software invocation"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-cache"
                - "memory.md#mem-obj-semantic-index"
                - "memory.md#mem-obj-usage-ledger"
                - "memory.md#mem-obj-dismissed-proposals"
                - "memory.md#mem-rte-usage-feedback"
                - "memory.md#mem-rte-capture-cleanup"
              note: "Later selectors automatically receive retained indexes and control history without a consumer request for those specific records."
          records:
            - "memory.md#mem-obj-wiki-cache"
            - "memory.md#mem-obj-semantic-index"
            - "memory.md#mem-obj-usage-ledger"
            - "memory.md#mem-obj-dismissed-proposals"
            - "memory.md#mem-rte-usage-feedback"
            - "memory.md#mem-rte-capture-cleanup"
          note: "Code loads access/control state automatically to carry out a later request or host event; this is distinct from the requested content return."
        - scope: "Documented offline export and raw-import reader routes"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-retained-export"
                - "runtime.md#rt-rte-source-import"
              note: "Offline/security readers or an ingesting agent can request retained export/raw content."
          records:
            - "memory.md#mem-rte-retained-export"
            - "runtime.md#rt-rte-source-import"
          note: "Their reader role is afforded; actual later external consumption is unobserved."
        - scope: "Detailed digest and auxiliary later-consumer routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-consolidation-plan"
            - "memory.md#mem-obj-wiki-pages"
            - "memory.md#mem-rte-retained-export"
          note: "The accepted inventory does not characterize these routes completely."
      records:
        - "runtime.md#rt-rte-context-recall"
        - "memory.md#mem-rte-wiki-read"
        - "memory.md#mem-obj-memory-claim"
        - "memory.md#mem-obj-memory-controls"
        - "memory.md#mem-obj-wiki-pages"
        - "runtime.md#rt-rte-session-capture"
        - "memory.md#mem-obj-session-capture"
        - "memory.md#mem-rte-capture-cleanup"
        - "memory.md#mem-rte-consolidation-plan"
        - "runtime.md#rt-rte-structured-ingest"
        - "runtime.md#rt-rte-workspace-sync"
        - "runtime.md#rt-rte-local-recovery"
        - "runtime.md#rt-rte-session-delivery"
        - "memory.md#mem-obj-handoff"
        - "memory.md#mem-rte-guard-reminder"
        - "memory.md#mem-rte-usage-feedback"
        - "memory.md#mem-obj-wiki-cache"
        - "memory.md#mem-obj-semantic-index"
        - "memory.md#mem-obj-usage-ledger"
        - "memory.md#mem-obj-dismissed-proposals"
        - "memory.md#mem-rte-retained-export"
        - "runtime.md#rt-rte-source-import"
      note: "Explicit request and independent automatic supply are distinct operations. Known push/pull routes do not complete the uncharacterized auxiliary route inventory."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Startup/autobrief selection of memory, capture-review and newest handoff substance"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-delivery"
                - "memory.md#mem-obj-handoff"
                - "memory.md#mem-obj-memory-controls"
                - "memory.md#mem-obj-session-capture"
              note: "Availability, lifecycle, type/recency priority, newest pending status and budgets choose brief parts."
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-delivery"
                - "memory.md#mem-obj-handoff"
                - "memory.md#mem-obj-memory-controls"
                - "memory.md#mem-obj-session-capture"
              note: "Project identity comparisons select project-matching memory/handoff parts for project-aware delivery."
          records:
            - "runtime.md#rt-rte-session-delivery"
            - "memory.md#mem-obj-handoff"
            - "memory.md#mem-obj-memory-controls"
            - "memory.md#mem-obj-session-capture"
          note: "Trigger is session start or first eligible JSON response. Active/review/recency/newest-pending eligibility and clipping determine the brief."
        - scope: "Prompt-guard retained constraint selection"
          assessment: "known"
          findings:
            - value: "inferred-lexical"
              basis: "wired"
              records:
                - "memory.md#mem-rte-guard-reminder"
                - "memory.md#mem-obj-memory-claim"
                - "memory.md#mem-rte-usage-feedback"
              note: "Constraint regex and strong lexical prompt overlap select the delivered claim."
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-guard-reminder"
                - "memory.md#mem-obj-memory-claim"
                - "memory.md#mem-rte-usage-feedback"
              note: "Project matching constrains the eligible saved-memory set."
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-guard-reminder"
                - "memory.md#mem-obj-memory-claim"
                - "memory.md#mem-rte-usage-feedback"
              note: "Length/score/confidence eligibility and cooldown decide whether any reminder is supplied."
          records:
            - "memory.md#mem-rte-guard-reminder"
            - "memory.md#mem-obj-memory-claim"
            - "memory.md#mem-rte-usage-feedback"
          note: "Trigger is per-prompt hook/query wrapper; input is current prompt/project plus saved constraint text, with event cooldown."
        - scope: "Automatic supply of cached indexes/vectors and control ledgers to software consumers"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-cache"
                - "memory.md#mem-obj-semantic-index"
                - "memory.md#mem-obj-usage-ledger"
                - "memory.md#mem-obj-dismissed-proposals"
                - "memory.md#mem-rte-usage-feedback"
                - "memory.md#mem-rte-capture-cleanup"
              note: "Fixed cache locations, freshness/version eligibility and available retained history determine the supplied control/access state."
          records:
            - "memory.md#mem-obj-wiki-cache"
            - "memory.md#mem-obj-semantic-index"
            - "memory.md#mem-obj-usage-ledger"
            - "memory.md#mem-obj-dismissed-proposals"
            - "memory.md#mem-rte-usage-feedback"
            - "memory.md#mem-rte-capture-cleanup"
          note: "The later selector loads the available cache/history; hashes/model keys and ring/window eligibility govern reuse. Query similarity is downstream ranking, not selection of this cache supply."
        - scope: "Explicit requested recall, recovery, acceptance and offline content returns"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-context-recall"
            - "memory.md#mem-rte-wiki-read"
            - "runtime.md#rt-rte-local-recovery"
            - "runtime.md#rt-rte-session-capture"
            - "memory.md#mem-rte-retained-export"
          note: "These are pull operations; a request identifier or ranked requested response is not a push signal."
        - scope: "Detailed digest and auxiliary push-selection routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-consolidation-plan"
            - "memory.md#mem-obj-wiki-pages"
            - "memory.md#mem-rte-retained-export"
          note: "Uncharacterized alternatives prevent a complete signal inventory; known pull routes cannot make them inapplicable."
      records:
        - "runtime.md#rt-rte-session-delivery"
        - "memory.md#mem-obj-handoff"
        - "memory.md#mem-obj-memory-controls"
        - "memory.md#mem-obj-session-capture"
        - "memory.md#mem-rte-guard-reminder"
        - "memory.md#mem-obj-memory-claim"
        - "memory.md#mem-rte-usage-feedback"
        - "memory.md#mem-obj-wiki-cache"
        - "memory.md#mem-obj-semantic-index"
        - "memory.md#mem-obj-usage-ledger"
        - "memory.md#mem-obj-dismissed-proposals"
        - "memory.md#mem-rte-capture-cleanup"
        - "runtime.md#rt-rte-context-recall"
        - "memory.md#mem-rte-wiki-read"
        - "runtime.md#rt-rte-local-recovery"
        - "runtime.md#rt-rte-session-capture"
        - "memory.md#mem-rte-retained-export"
        - "memory.md#mem-rte-consolidation-plan"
        - "memory.md#mem-obj-wiki-pages"
      note: "Signals describe actual push selection, not query/file identifiers on requested returns. Startup eligibility/budget and project matches, guard lexical overlap and control/index supply remain distinct; auxiliary pushes are unresolved."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Automatic session-end retained notes/proposals to later review context and accepted-memory consumers"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-capture"
                - "memory.md#mem-obj-session-capture"
                - "runtime.md#rt-rte-session-delivery"
                - "runtime.md#rt-rte-memory-admission"
              note: "Session traces automatically produce retained context/proposals that affect later review and host context."
          records:
            - "runtime.md#rt-rte-session-capture"
            - "memory.md#mem-obj-session-capture"
            - "runtime.md#rt-rte-session-delivery"
            - "runtime.md#rt-rte-memory-admission"
          note: "The hook automatically extracts traces into durable notes/candidates; later startup review supply consumes these and selected accepted claims feed future recall. Approval of final memory is a separate uncertain mechanism."
        - scope: "Automatic usage events to later guard repetition decisions"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-usage-ledger"
                - "memory.md#mem-rte-usage-feedback"
                - "memory.md#mem-rte-guard-reminder"
              note: "Automatically recorded access experience shapes later reminder behavior through durable event history."
          records:
            - "memory.md#mem-obj-usage-ledger"
            - "memory.md#mem-rte-usage-feedback"
            - "memory.md#mem-rte-guard-reminder"
          note: "Returned identity events are retained automatically and later cooldown changes emit/silence decisions; popularity ranking is a separate optional path."
        - scope: "Automatic operation journal/status and snapshot production to later recovery"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-operation-journal"
                - "runtime.md#rt-rte-local-recovery"
              note: "Recorded operation experience automatically shapes later recovery choices through retained markers/manifests."
          records:
            - "runtime.md#rt-obj-operation-journal"
            - "runtime.md#rt-rte-local-recovery"
          note: "Operation activity automatically produces durable recovery records; later confirmed recovery consumes their status/path information. Restored byte content alone is not a learned claim."
        - scope: "Dismissal history and caller-authored accepted claims/handoffs"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-dismissed-proposals"
            - "memory.md#mem-rte-capture-cleanup"
            - "runtime.md#rt-rte-memory-admission"
            - "memory.md#mem-obj-handoff"
            - "memory.md#mem-obj-session-capture"
          note: "The retained rejection experience shapes proposal vetoes, but actual per-content human control and mixed caller origins are unresolved. These paths are not upgraded by the automatic hook witness."
        - scope: "Conditional semantic-cache derivation from trace-origin versus non-trace-origin memory text"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-semantic-index"
            - "memory.md#mem-obj-memory-claim"
            - "runtime.md#rt-rte-session-capture"
          note: "Automatic encoding and later ranking are known; the accepted records do not identify the original trace-fed provenance of every included vector input."
        - scope: "Optional Git-history project seed and imported/manual note alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-project-seed"
            - "runtime.md#rt-rte-source-import"
            - "runtime.md#rt-rte-session-capture"
          note: "The routes include mixed static/history/session inputs, but records do not fully establish every original trace kind and qualifying automatic durable update."
        - scope: "Detailed digest, auxiliary maintenance and checkpoint alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-consolidation-plan"
            - "memory.md#mem-obj-wiki-pages"
            - "runtime.md#rt-rte-local-recovery"
          note: "Uncharacterized transformations and replacement inputs prevent a bounded complete absence of qualifying trace-fed writes."
      records:
        - "runtime.md#rt-rte-session-capture"
        - "memory.md#mem-obj-session-capture"
        - "runtime.md#rt-rte-session-delivery"
        - "runtime.md#rt-rte-memory-admission"
        - "memory.md#mem-obj-usage-ledger"
        - "memory.md#mem-rte-usage-feedback"
        - "memory.md#mem-rte-guard-reminder"
        - "runtime.md#rt-obj-operation-journal"
        - "runtime.md#rt-rte-local-recovery"
        - "memory.md#mem-obj-dismissed-proposals"
        - "memory.md#mem-rte-capture-cleanup"
        - "memory.md#mem-obj-handoff"
        - "memory.md#mem-obj-semantic-index"
        - "memory.md#mem-obj-memory-claim"
        - "runtime.md#rt-rte-project-seed"
        - "runtime.md#rt-rte-source-import"
        - "memory.md#mem-rte-consolidation-plan"
        - "memory.md#mem-obj-wiki-pages"
      note: "Automatic trace extraction and metadata-feedback writes have durable later-consumer paths. This is the profile write-route sense of learning, not demonstrated improved capacity. Generic caller/seed/history and auxiliary alternatives prevent a system-wide negative or complete positive inventory."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Automatic session extraction qualifying write"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-capture"
                - "memory.md#mem-obj-session-capture"
                - "epistemic.md#epi-rte-proposal-normalization"
              note: "Recorded conversational turns from host sessions feed the retained notes/proposals."
          records:
            - "runtime.md#rt-rte-session-capture"
            - "memory.md#mem-obj-session-capture"
            - "epistemic.md#epi-rte-proposal-normalization"
          note: "Automatic mining uses recorded user conversational turns; retained review notes can also contain assistant turns. Wrapping them as captures does not add another trace class."
        - scope: "Usage event/cooldown qualifying write"
          assessment: "known"
          findings:
            - value: "event-streams"
              basis: "wired"
              records:
                - "memory.md#mem-obj-usage-ledger"
                - "memory.md#mem-rte-usage-feedback"
                - "memory.md#mem-rte-guard-reminder"
              note: "Discrete retrieval/reminder events feed retained metadata and later repetition policy."
          records:
            - "memory.md#mem-obj-usage-ledger"
            - "memory.md#mem-rte-usage-feedback"
            - "memory.md#mem-rte-guard-reminder"
          note: "Original input is software surfacing/guard activity: returned names, time and kind, not the tool result body or conversational transcript."
        - scope: "Operation-journal qualifying write"
          assessment: "known"
          findings:
            - value: "event-streams"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-operation-journal"
                - "runtime.md#rt-rte-local-recovery"
              note: "Discrete operation status events produce retained recovery controls."
          records:
            - "runtime.md#rt-obj-operation-journal"
            - "runtime.md#rt-rte-local-recovery"
          note: "Original input is write/failure/recovery activity and touched-path/status information; snapshots preserve associated bytes."
        - scope: "Dismissal, caller claim and handoff source alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-dismissed-proposals"
            - "memory.md#mem-rte-capture-cleanup"
            - "memory.md#mem-obj-memory-claim"
            - "memory.md#mem-obj-handoff"
            - "runtime.md#rt-rte-session-capture"
          note: "Fingerprint text may derive from conversational or imported inputs, and caller text has unspecified original provenance; neither content labels nor confirmation identify all original trace sources."
        - scope: "Trace-origin semantic cache and optional history/project imports"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-semantic-index"
            - "runtime.md#rt-rte-project-seed"
            - "runtime.md#rt-rte-source-import"
            - "runtime.md#rt-rte-session-capture"
          note: "Known derivation/transfer does not resolve original trace content for every qualifying included input; imported static instructions alone establish no trace source."
        - scope: "Detailed digest, auxiliary updates and checkpoint payload origins"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-consolidation-plan"
            - "memory.md#mem-obj-wiki-pages"
            - "runtime.md#rt-rte-local-recovery"
          note: "Their qualifying writes and original sources remain incompletely characterized; absence in another route would not make these inapplicable."
      records:
        - "runtime.md#rt-rte-session-capture"
        - "memory.md#mem-obj-session-capture"
        - "epistemic.md#epi-rte-proposal-normalization"
        - "memory.md#mem-obj-usage-ledger"
        - "memory.md#mem-rte-usage-feedback"
        - "memory.md#mem-rte-guard-reminder"
        - "runtime.md#rt-obj-operation-journal"
        - "runtime.md#rt-rte-local-recovery"
        - "memory.md#mem-obj-dismissed-proposals"
        - "memory.md#mem-rte-capture-cleanup"
        - "memory.md#mem-obj-memory-claim"
        - "memory.md#mem-obj-handoff"
        - "memory.md#mem-obj-semantic-index"
        - "runtime.md#rt-rte-project-seed"
        - "runtime.md#rt-rte-source-import"
        - "memory.md#mem-rte-consolidation-plan"
        - "memory.md#mem-obj-wiki-pages"
      note: "Sources are classified on the original activity content, not serialization or adapter labels. Known session and runtime-event sources coexist with mixed/unresolved caller, embedding, seed and auxiliary origins."
---

# Link memory profile

## Comparison rationale

### Boundary and coverage

The comparison covers accumulated content and its access, control and recovery
parts, not everything Link stores or ships. The operative inventory comes from
[MEM-OBJ-memory-claim](memory.md#mem-obj-memory-claim),
[MEM-OBJ-memory-controls](memory.md#mem-obj-memory-controls),
[MEM-OBJ-retrieval-context](memory.md#mem-obj-retrieval-context),
[MEM-OBJ-session-capture](memory.md#mem-obj-session-capture),
[MEM-OBJ-wiki-pages](memory.md#mem-obj-wiki-pages),
[MEM-OBJ-wiki-cache](memory.md#mem-obj-wiki-cache),
[MEM-OBJ-semantic-index](memory.md#mem-obj-semantic-index),
[MEM-OBJ-handoff](memory.md#mem-obj-handoff),
[MEM-OBJ-usage-ledger](memory.md#mem-obj-usage-ledger) and the cited recovery,
synchronization, ownership and export routes. Their records retain the source
passages; this profile adds neither records nor quotations.

Every axis is partial because the accepted inventory retains local gaps, notably
detailed digest/auxiliary transformations and consumers, generic caller control
and mixed initial provenance. These gaps do not suppress classified parts.
Missing host traces limit operation and benefit, not the wired architectural
findings. Static steering and external provider weights are not use-derived
memory; the numerical vector cache is. Unpinned provider provenance remains a
limit on its known derivation rather than a claim of trained Link parameters.
See [RT-OBJ-link-instructions](runtime.md#rt-obj-link-instructions),
[RT-CMP-model2vec](runtime.md#rt-cmp-model2vec),
[RT-CMP-fastembed](runtime.md#rt-cmp-fastembed) and
[MEM-OBJ-semantic-index](memory.md#mem-obj-semantic-index).

### Forms, lineage and consumers

Markdown and JSON establish files, not graph/vector/KV databases merely because
they encode links, dense vectors or keyed records. SQLite FTS and process maps
have their own substrates. Graph access state is symbolic; dense distributed
vectors are parametric; returned claim/article text is natural language. The
same text can provide knowledge to an agent and ranking input to fixed retrieval
code. Retrieval-only context has ranking force even though slim delivery omits
it. See [MEM-OBJ-wiki-cache](memory.md#mem-obj-wiki-cache),
[MEM-OBJ-retrieval-context](memory.md#mem-obj-retrieval-context) and
[RT-RTE-context-recall](runtime.md#rt-rte-context-recall).

Authored, imported, trace-extracted and other-compiled findings refer to separate
paths, not exclusive labels for the whole corpus. Known extraction or rendering
does not authenticate source strings or resolve initial content provenance.
Structured body escaping is a documented encoding change, not an extra learned
claim. See [EPI-RTE-export-rendering](epistemic.md#epi-rte-export-rendering).

Lifecycle controls enforce focused selection only. Generic wiki delivery remains
an independent consumer of still-present archived, expired or other-project
pages; its compaction omits memory-specific warnings. Thus invalidate is bounded
withdrawal, not universal nondelivery. See
[MEM-RTE-wiki-read](memory.md#mem-rte-wiki-read) and
[EPI-RTE-memory-withdrawal](epistemic.md#epi-rte-memory-withdrawal).
Dismissal membership validates candidates and enforces a veto; ownership hashes
validate replacement and enforce its managed-output gate. Neither supplies
claim truth. Journal state routes recovery rather than becoming factual advice.

### Admission and maintenance

Manual findings describe explicit human decisions requested by the contract,
not a verified universal approval gate. Generic callers, Boolean confirmation
and source strings cannot establish actual human control. Software/model content
admission within an initiated workflow remains automatic. Those findings do not
upgrade unknown explicit replacement mechanisms. See
[RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission),
[EPI-RTE-review-marking](epistemic.md#epi-rte-review-marking),
[RT-RTE-agent-wiki](runtime.md#rt-rte-agent-wiki) and
[RT-RTE-local-recovery](runtime.md#rt-rte-local-recovery).

The read-only planner is not implemented semantic consolidation. Known curation
instead includes transcript reduction, actual capture deduplication, append and
metadata revision, branch-local withdrawal, deletion/FIFO pruning and the
reviewed-state ranking boost. Requested external-agent synthesis retains claimed
basis. A proposal-normalization fidelity defect does not turn consolidation
into synthesis. Query excerpt construction creates no retained successor and is
not another durable consolidation write. See
[MEM-RTE-consolidation-plan](memory.md#mem-rte-consolidation-plan),
[MEM-RTE-memory-lifecycle](memory.md#mem-rte-memory-lifecycle),
[MEM-RTE-capture-cleanup](memory.md#mem-rte-capture-cleanup),
[EPI-RTE-proposal-normalization](epistemic.md#epi-rte-proposal-normalization) and
[EPI-RTE-context-compaction](epistemic.md#epi-rte-context-compaction).

### Read-back and trace-fed writes

Explicit requested recall is pull even when software selects/ranks its response.
Startup, first-response autobrief and prompt reminders independently supply
memory and are push. Within those push chains, coarse eligibility and budget
rules are distinct from actual project matches and guard lexical overlap.
Identifiers on requested files are not counted as identifier push. Automatic
loads of retained access/control state are named separately from requested
content delivery. See [RT-RTE-session-delivery](runtime.md#rt-rte-session-delivery),
[MEM-RTE-guard-reminder](memory.md#mem-rte-guard-reminder) and
[MEM-RTE-usage-feedback](memory.md#mem-rte-usage-feedback).

Automatic conversational extraction produces retained notes/candidates consumed
by later review/startup routes; final claim acceptance is a separate mechanism.
Usage events automatically produce durable history that changes later cooldown
choices, without recording whether the model relied on returned content.
Operation activity automatically produces durable markers/manifests that choose
later recovery actions. These qualifying trace-fed writes have session-logs or
event-streams as their original sources. Merely recording a tool-return identity
does not establish consumption of a tool trace's request/result body. Mixed
imports and optional project history retain unknown origins; no tool-traces or
trajectories finding is invented from a label. No system-wide trace-learning
negative follows from fixed provider parameters, read-only plans or nonadopted
salience. See [RT-RTE-session-capture](runtime.md#rt-rte-session-capture),
[MEM-OBJ-session-capture](memory.md#mem-obj-session-capture),
[MEM-OBJ-usage-ledger](memory.md#mem-obj-usage-ledger),
[MEM-RTE-usage-feedback](memory.md#mem-rte-usage-feedback),
[RT-OBJ-operation-journal](runtime.md#rt-obj-operation-journal) and
[RT-RTE-local-recovery](runtime.md#rt-rte-local-recovery).

These profile findings establish automatic durable behavioral-context/control
paths, not improved future capacity, exercised self-improvement or causal
benefit. Learning authority at the capture-to-memory update consumer is distinct
from knowledge/instruction authority at the later host consumer.

### Canonical records and source reads

The supplied reconciliation supersedes EPI-OBJ-wiki-page with
[MEM-OBJ-wiki-pages](memory.md#mem-obj-wiki-pages), and
EPI-RTE-consolidation-plan with
[MEM-RTE-consolidation-plan](memory.md#mem-rte-consolidation-plan).
All classifications use these canonical destinations. The memory-page container
and its claim/control/context parts remain valid distinct scopes; no invented
split supersession is used. Shared checker and post-authoring completion routes
remain distinct; neither converts static validation code into accumulated memory.

Source reads: none. All classifications derive from the supplied accepted
records and their annotations, resolved through the supplied reconciliation.
