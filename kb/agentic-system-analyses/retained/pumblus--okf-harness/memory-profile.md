---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "OKF Harness memory comparison of retained local sources, wiki claims, access metadata, reconciliation state, graph reports and Git recovery."
run-id: "AAS-2026-10-15-okf-harness-6bf5507fbdbf-01"
source-identity: "https://github.com/pumblus/okf-harness"
reviewed-boundary: "0dd4f806c454a68088c5a3e64b4cbebbe2c216be"
memory-comparison:
  version: 2
  scope: "Retained registered file bytes and URL pointers; source manifest; wiki prose and retrieval/citation fields; reconciliation edge IDs and notes; persisted graph/backlinks reports; Git checkpoint trees and judgments; their admission, maintenance and later-consumer routes. Includes unresolved initial content, opaque captured files and generic caller control. Excludes unchanged shipped guidance provisioning, runtime-version configuration, transient evidence/check/doctor returns, reserved legacy logs as answer memory, external host session/compaction/provider state and model weights. Restored instructions/configuration remain included as checkpoint payload, not newly inferred online instruction learning."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        -
          scope: "Registered raw bytes, URL pointers and manifest"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-bytes"
                - "memory.md#mem-obj-url-metadata"
                - "memory.md#mem-obj-manifest"
              note: "Local raw files and JSONL remain available to later source reading and checks."
          records:
            - "memory.md#mem-obj-source-bytes"
            - "memory.md#mem-obj-url-metadata"
            - "memory.md#mem-obj-manifest"
          note: "Local raw files and JSONL remain available to later source reading and checks."
        -
          scope: "Wiki prose and parsed retrieval fields"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-content"
                - "memory.md#mem-obj-wiki-metadata"
              note: "Markdown files retain both semantic content and access structures."
          records:
            - "memory.md#mem-obj-wiki-content"
            - "memory.md#mem-obj-wiki-metadata"
          note: "Markdown files retain both semantic content and access structures."
        -
          scope: "Reconciliation edge IDs and notes"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-reconciliation-edges"
                - "memory.md#mem-obj-reconciliation-notes"
              note: "Local JSONL retains the two distinct parts."
          records:
            - "memory.md#mem-obj-reconciliation-edges"
            - "memory.md#mem-obj-reconciliation-notes"
          note: "Local JSONL retains the two distinct parts."
        -
          scope: "Persisted backlinks JSON and graph HTML"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-backlinks"
                - "memory.md#mem-rte-graph-report"
              note: "Generated reports are local files; an edge encoding does not make their substrate a graph database."
          records:
            - "memory.md#mem-obj-backlinks"
            - "memory.md#mem-rte-graph-report"
          note: "Generated reports are local files; an edge encoding does not make their substrate a graph database."
        -
          scope: "Checkpoint trees and judgment bodies"
          assessment: "known"
          findings:
            -
              value: "repo"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint-tree"
                - "memory.md#mem-obj-checkpoint-judgment"
                - "runtime.md#rt-rte-workspace-recovery"
              note: "Git retains versioned trees and commit bodies; repo classifies this recovery store, separately from working files."
          records:
            - "memory.md#mem-obj-checkpoint-tree"
            - "memory.md#mem-obj-checkpoint-judgment"
            - "runtime.md#rt-rte-workspace-recovery"
          note: "Git retains versioned trees and commit bodies; repo classifies this recovery store, separately from working files."
      records:
        - "memory.md#mem-obj-source-bytes"
        - "memory.md#mem-obj-url-metadata"
        - "memory.md#mem-obj-manifest"
        - "memory.md#mem-obj-wiki-content"
        - "memory.md#mem-obj-wiki-metadata"
        - "memory.md#mem-obj-reconciliation-edges"
        - "memory.md#mem-obj-reconciliation-notes"
        - "memory.md#mem-obj-backlinks"
        - "memory.md#mem-rte-graph-report"
        - "memory.md#mem-obj-checkpoint-tree"
        - "memory.md#mem-obj-checkpoint-judgment"
        - "runtime.md#rt-rte-workspace-recovery"
      note: "The recorded retained-object inventory uses local files and Git objects. Source encoding opacity does not obscure its disk substrate; external provider/session state and static provisioning are excluded."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Arbitrary registered source bodies and their source-reading path"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-bytes"
          note: "Registration copies bytes without establishing text, binary encoding or the form interpreted by the later agent."
        -
          scope: "URL pointer prose"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-url-metadata"
              note: "Generated pointer prose is readable natural language."
          records:
            - "memory.md#mem-obj-url-metadata"
          note: "Generated pointer prose is readable natural language."
        -
          scope: "URL/date fields and manifest identity fields"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-url-metadata"
                - "memory.md#mem-obj-manifest"
              note: "URL, date, path, hash and source IDs have fixed procedural consumers."
          records:
            - "memory.md#mem-obj-url-metadata"
            - "memory.md#mem-obj-manifest"
          note: "URL, date, path, hash and source IDs have fixed procedural consumers."
        -
          scope: "Manifest title/notes and wiki title/description prose"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-manifest"
                - "memory.md#mem-obj-wiki-metadata"
              note: "Descriptive strings carry readable text, independently of their use by lexical scoring."
          records:
            - "memory.md#mem-obj-manifest"
            - "memory.md#mem-obj-wiki-metadata"
          note: "Descriptive strings carry readable text, independently of their use by lexical scoring."
        -
          scope: "Wiki claims at answering consumer"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-content"
                - "runtime.md#rt-rte-evidence-answer"
              note: "Retrieved claim prose is interpreted as answer context."
          records:
            - "memory.md#mem-obj-wiki-content"
            - "runtime.md#rt-rte-evidence-answer"
          note: "Retrieved claim prose is interpreted as answer context."
        -
          scope: "Wiki identities, tags and citation targets at scanner/selector"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-metadata"
              note: "Fixed parsing and scoring operate on localized fields."
          records:
            - "memory.md#mem-obj-wiki-metadata"
          note: "Fixed parsing and scoring operate on localized fields."
        -
          scope: "Reconciliation edge IDs"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-reconciliation-edges"
              note: "Exact identity equality changes pending-edge computation."
          records:
            - "memory.md#mem-obj-reconciliation-edges"
          note: "Exact identity equality changes pending-edge computation."
        -
          scope: "Reconciliation judgment notes"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-reconciliation-notes"
              note: "Free-text rationale is retained even though its semantic read-back is not established."
          records:
            - "memory.md#mem-obj-reconciliation-notes"
          note: "Free-text rationale is retained even though its semantic read-back is not established."
        -
          scope: "Checkpoint identity/tree structure"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint-tree"
              note: "Git paths and tree/blob identities are symbolic recovery material."
          records:
            - "memory.md#mem-obj-checkpoint-tree"
          note: "Git paths and tree/blob identities are symbolic recovery material."
        -
          scope: "Opaque checkpoint payload alternatives"
          assessment: "partial"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint-tree"
              note: "Snapshots may retain wiki prose and workspace guidance."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint-tree"
              note: "Snapshots may retain manifests and configuration."
          records:
            - "memory.md#mem-obj-checkpoint-tree"
          note: "Restored files preserve text and symbolic forms already identified, but arbitrary captured files prevent a complete encoding inventory."
        -
          scope: "Checkpoint judgment body"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint-judgment"
              note: "History returns readable caller rationale."
          records:
            - "memory.md#mem-obj-checkpoint-judgment"
          note: "History returns readable caller rationale."
        -
          scope: "Graph structure and graph display labels"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-backlinks"
              note: "Node/edge structures have fixed rules. Displayed title strings retain readable text."
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-backlinks"
              note: "Node/edge structures have fixed rules. Displayed title strings retain readable text."
          records:
            - "memory.md#mem-obj-backlinks"
          note: "Node/edge structures have fixed rules. Displayed title strings retain readable text."
      records:
        - "memory.md#mem-obj-source-bytes"
        - "memory.md#mem-obj-url-metadata"
        - "memory.md#mem-obj-manifest"
        - "memory.md#mem-obj-wiki-metadata"
        - "memory.md#mem-obj-wiki-content"
        - "runtime.md#rt-rte-evidence-answer"
        - "memory.md#mem-obj-reconciliation-edges"
        - "memory.md#mem-obj-reconciliation-notes"
        - "memory.md#mem-obj-checkpoint-tree"
        - "memory.md#mem-obj-checkpoint-judgment"
        - "memory.md#mem-obj-backlinks"
      note: "Text and symbolic consumers are resolved, but arbitrary registered bytes and opaque files inside checkpoint trees cannot be completely classified."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Registered file acquisition"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-bytes"
                - "runtime.md#rt-rte-source-ingest"
              note: "Raw input is imported byte-for-byte; imported lineage does not certify its earlier origin."
          records:
            - "memory.md#mem-obj-source-bytes"
            - "runtime.md#rt-rte-source-ingest"
          note: "Raw input is imported byte-for-byte; imported lineage does not certify its earlier origin."
        -
          scope: "Initial provenance of arbitrary external source content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-bytes"
          note: "The caller supplies external bytes; registration does not establish how the original content was produced."
        -
          scope: "URL pointer, manifest and reconciliation edge construction"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-url-metadata"
                - "memory.md#mem-obj-manifest"
                - "memory.md#mem-obj-reconciliation-edges"
              note: "Code generates metadata and exact-pair bookkeeping from supplied fields."
          records:
            - "memory.md#mem-obj-url-metadata"
            - "memory.md#mem-obj-manifest"
            - "memory.md#mem-obj-reconciliation-edges"
          note: "Code generates metadata and exact-pair bookkeeping from supplied fields."
        -
          scope: "Host-authored wiki outputs under ingest/reconcile/write-back"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-wiki-content"
                - "runtime.md#rt-rte-source-ingest"
                - "runtime.md#rt-rte-source-reconcile"
                - "runtime.md#rt-rte-evidence-answer"
              note: "The delivered protocol assigns prose creation and revision to the host agent; no produced semantic page is observed."
          records:
            - "memory.md#mem-obj-wiki-content"
            - "runtime.md#rt-rte-source-ingest"
            - "runtime.md#rt-rte-source-reconcile"
            - "runtime.md#rt-rte-evidence-answer"
          note: "The delivered protocol assigns prose creation and revision to the host agent; no produced semantic page is observed."
        -
          scope: "Historical wiki content and initial retained notes/judgments"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-wiki-content"
            - "memory.md#mem-obj-reconciliation-notes"
            - "memory.md#mem-obj-checkpoint-judgment"
          note: "Scanning and generic caller identity do not establish the original derivation path. Caller-authored text is not evidence that it was never extracted or imported."
        -
          scope: "Backlinks/graph derivation"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-backlinks"
                - "memory.md#mem-rte-graph-report"
              note: "Parsed wiki links and titles are compiled into reports."
          records:
            - "memory.md#mem-obj-backlinks"
            - "memory.md#mem-rte-graph-report"
          note: "Parsed wiki links and titles are compiled into reports."
        -
          scope: "Git snapshot construction"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint-tree"
                - "runtime.md#rt-rte-workspace-recovery"
              note: "Versioned tree structure is compiled from current workspace files, not distilled from a conversation."
          records:
            - "memory.md#mem-obj-checkpoint-tree"
            - "runtime.md#rt-rte-workspace-recovery"
          note: "Versioned tree structure is compiled from current workspace files, not distilled from a conversation."
        -
          scope: "Contained historical checkpoint payload lineage"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-checkpoint-tree"
          note: "Baseline and later trees can retain preexisting content of unresolved origin; snapshotting does not settle it."
      records:
        - "memory.md#mem-obj-source-bytes"
        - "runtime.md#rt-rte-source-ingest"
        - "memory.md#mem-obj-url-metadata"
        - "memory.md#mem-obj-manifest"
        - "memory.md#mem-obj-reconciliation-edges"
        - "memory.md#mem-obj-wiki-content"
        - "runtime.md#rt-rte-source-reconcile"
        - "runtime.md#rt-rte-evidence-answer"
        - "memory.md#mem-obj-reconciliation-notes"
        - "memory.md#mem-obj-checkpoint-judgment"
        - "memory.md#mem-obj-backlinks"
        - "memory.md#mem-rte-graph-report"
        - "memory.md#mem-obj-checkpoint-tree"
        - "runtime.md#rt-rte-workspace-recovery"
      note: "Known acquisition and derivation paths do not resolve initial authorship of external inputs, historical wiki content or every restored file."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Registered bytes to integrity checks"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-bytes"
                - "memory.md#mem-obj-manifest"
                - "memory.md#mem-rte-workspace-check"
              note: "Stored hash/bytes supply byte-identity criteria; this validates integrity, not source truth."
          records:
            - "memory.md#mem-obj-source-bytes"
            - "memory.md#mem-obj-manifest"
            - "memory.md#mem-rte-workspace-check"
          note: "Stored hash/bytes supply byte-identity criteria; this validates integrity, not source truth."
        -
          scope: "Registered inputs to ingest/reconcile agent"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-source-bytes"
                - "memory.md#mem-obj-url-metadata"
                - "runtime.md#rt-rte-source-ingest"
                - "runtime.md#rt-rte-source-reconcile"
              note: "Requested source reading supplies evidence for semantic edits, not privileged directions."
          records:
            - "memory.md#mem-obj-source-bytes"
            - "memory.md#mem-obj-url-metadata"
            - "runtime.md#rt-rte-source-ingest"
            - "runtime.md#rt-rte-source-reconcile"
          note: "Requested source reading supplies evidence for semantic edits, not privileged directions."
        -
          scope: "Wiki prose to answering agent"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-content"
                - "runtime.md#rt-rte-evidence-answer"
                - "runtime.md#rt-bap-evidence-context"
              note: "Selected prose supplies context for later answers. Delivery is wired; dependence and benefit are unobserved."
          records:
            - "memory.md#mem-obj-wiki-content"
            - "runtime.md#rt-rte-evidence-answer"
            - "runtime.md#rt-bap-evidence-context"
          note: "Selected prose supplies context for later answers. Delivery is wired; dependence and benefit are unobserved."
        -
          scope: "Wiki prose/title/description/tags/index at lexical scorer"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-content"
                - "memory.md#mem-obj-wiki-metadata"
                - "runtime.md#rt-rte-evidence-answer"
                - "runtime.md#rt-rte-direct-retrieval"
              note: "Retained strings influence relative retrieval priority under fixed lexical code."
          records:
            - "memory.md#mem-obj-wiki-content"
            - "memory.md#mem-obj-wiki-metadata"
            - "runtime.md#rt-rte-evidence-answer"
            - "runtime.md#rt-rte-direct-retrieval"
          note: "Retained strings influence relative retrieval priority under fixed lexical code."
        -
          scope: "Manifest IDs/paths and wiki parsed fields at lookup and planning"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-manifest"
                - "memory.md#mem-obj-wiki-metadata"
                - "runtime.md#rt-rte-source-ingest"
                - "runtime.md#rt-rte-direct-retrieval"
              note: "Retained identities select references, targets and planning candidates."
          records:
            - "memory.md#mem-obj-manifest"
            - "memory.md#mem-obj-wiki-metadata"
            - "runtime.md#rt-rte-source-ingest"
            - "runtime.md#rt-rte-direct-retrieval"
          note: "Retained identities select references, targets and planning candidates."
        -
          scope: "Manifest uniqueness and stored provenance at admission/integrity consumers"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-manifest"
                - "memory.md#mem-rte-workspace-check"
                - "runtime.md#rt-rte-source-ingest"
              note: "Recorded IDs/paths/hash constrain admissibility and integrity checks; duplicate identities can reject ordinary registration."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-manifest"
                - "memory.md#mem-rte-workspace-check"
                - "runtime.md#rt-rte-source-ingest"
              note: "Recorded IDs/paths/hash constrain admissibility and integrity checks; duplicate identities can reject ordinary registration."
          records:
            - "memory.md#mem-obj-manifest"
            - "memory.md#mem-rte-workspace-check"
            - "runtime.md#rt-rte-source-ingest"
          note: "Recorded IDs/paths/hash constrain admissibility and integrity checks; duplicate identities can reject ordinary registration."
        -
          scope: "Wiki source/citation identities at evidence seal consumer"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-metadata"
                - "runtime.md#rt-rte-evidence-answer"
                - "runtime.md#rt-clm-evidence-boundary"
              note: "Retained links identify concepts excluded from planner delivery when source risk is detected; this is planner-local enforcement, not universal read denial."
          records:
            - "memory.md#mem-obj-wiki-metadata"
            - "runtime.md#rt-rte-evidence-answer"
            - "runtime.md#rt-clm-evidence-boundary"
          note: "Retained links identify concepts excluded from planner delivery when source risk is detected; this is planner-local enforcement, not universal read denial."
        -
          scope: "Reconciliation exact pair at snapshot currency consumer"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-reconciliation-edges"
                - "runtime.md#rt-rte-source-reconcile"
                - "memory.md#mem-clm-currency-evidence"
              note: "Acknowledged pairs select which suspected edges remain pending; they do not validate changed claims or gate evidence merely because currency is false."
          records:
            - "memory.md#mem-obj-reconciliation-edges"
            - "runtime.md#rt-rte-source-reconcile"
            - "memory.md#mem-clm-currency-evidence"
          note: "Acknowledged pairs select which suspected edges remain pending; they do not validate changed claims or gate evidence merely because currency is false."
        -
          scope: "Retained reconciliation note semantics"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-reconciliation-notes"
          note: "Only a nonempty-string criterion and ID-driven filtering are established; no later semantic consumer licenses knowledge or learning authority."
        -
          scope: "Checkpoint identities and tree at restore"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint-tree"
                - "runtime.md#rt-rte-workspace-recovery"
              note: "Selected completion chooses the restored working state used by later commands. Individual restored parts retain their own downstream forces."
          records:
            - "memory.md#mem-obj-checkpoint-tree"
            - "runtime.md#rt-rte-workspace-recovery"
          note: "Selected completion chooses the restored working state used by later commands. Individual restored parts retain their own downstream forces."
        -
          scope: "Checkpoint judgment at history caller"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-checkpoint-judgment"
                - "runtime.md#rt-rte-workspace-recovery"
              note: "History exposes rationale as information for caller interpretation and restore choice, not as a scored learning signal."
          records:
            - "memory.md#mem-obj-checkpoint-judgment"
            - "runtime.md#rt-rte-workspace-recovery"
          note: "History exposes rationale as information for caller interpretation and restore choice, not as a scored learning signal."
        -
          scope: "Persisted graph display to browser reader"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-backlinks"
                - "memory.md#mem-rte-graph-report"
              note: "Generated navigation and labels inform the requested browser reader; actual opening is unobserved."
          records:
            - "memory.md#mem-obj-backlinks"
            - "memory.md#mem-rte-graph-report"
          note: "Generated navigation and labels inform the requested browser reader; actual opening is unobserved."
      records:
        - "memory.md#mem-obj-source-bytes"
        - "memory.md#mem-obj-manifest"
        - "memory.md#mem-rte-workspace-check"
        - "memory.md#mem-obj-url-metadata"
        - "runtime.md#rt-rte-source-ingest"
        - "runtime.md#rt-rte-source-reconcile"
        - "memory.md#mem-obj-wiki-content"
        - "runtime.md#rt-rte-evidence-answer"
        - "runtime.md#rt-bap-evidence-context"
        - "memory.md#mem-obj-wiki-metadata"
        - "runtime.md#rt-rte-direct-retrieval"
        - "runtime.md#rt-clm-evidence-boundary"
        - "memory.md#mem-obj-reconciliation-edges"
        - "memory.md#mem-clm-currency-evidence"
        - "memory.md#mem-obj-reconciliation-notes"
        - "memory.md#mem-obj-checkpoint-tree"
        - "runtime.md#rt-rte-workspace-recovery"
        - "memory.md#mem-obj-checkpoint-judgment"
        - "memory.md#mem-obj-backlinks"
        - "memory.md#mem-rte-graph-report"
      note: "Authority is split by actual retained part and consumer. Reconciliation note semantics have no established later consumer, preventing complete classification."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Registration and manifest admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-source-ingest"
                - "memory.md#mem-obj-source-bytes"
                - "memory.md#mem-obj-url-metadata"
                - "memory.md#mem-obj-manifest"
              note: "Code applies registration checks and writes/reuses entries without per-content human approval; starting source ingestion is not approval of each retained part."
          records:
            - "runtime.md#rt-rte-source-ingest"
            - "memory.md#mem-obj-source-bytes"
            - "memory.md#mem-obj-url-metadata"
            - "memory.md#mem-obj-manifest"
          note: "Code applies registration checks and writes/reuses entries without per-content human approval; starting source ingestion is not approval of each retained part."
        -
          scope: "Ingest/reconcile wiki edit admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-source-ingest"
                - "runtime.md#rt-rte-source-reconcile"
                - "memory.md#mem-obj-wiki-content"
              note: "Guidance assigns proposal and adoption to the agent. The start request and occasional stop contract are not mandatory per-claim human decisions."
          records:
            - "runtime.md#rt-rte-source-ingest"
            - "runtime.md#rt-rte-source-reconcile"
            - "memory.md#mem-obj-wiki-content"
          note: "Guidance assigns proposal and adoption to the agent. The start request and occasional stop contract are not mandatory per-claim human decisions."
        -
          scope: "Conversation answer write-back admission"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-evidence-answer"
              note: "Explicit user yes supplies the decision to retain that answer; no/silence persists nothing under the protocol."
          records:
            - "runtime.md#rt-rte-evidence-answer"
          note: "Explicit user yes supplies the decision to retain that answer; no/silence persists nothing under the protocol."
        -
          scope: "Derived graph report admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-graph-report"
              note: "Fixed code generates reports without a human approving individual nodes or edges."
          records:
            - "memory.md#mem-rte-graph-report"
          note: "Fixed code generates reports without a human approving individual nodes or edges."
        -
          scope: "Reconciliation acknowledgment and note admission control"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-source-reconcile"
            - "memory.md#mem-obj-reconciliation-notes"
          note: "Core rejects invalid IDs/empty notes, but generic caller identity does not establish human approval versus model admission."
        -
          scope: "Baseline/checkpoint/restore admission control"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-workspace-recovery"
            - "memory.md#mem-obj-checkpoint-tree"
            - "memory.md#mem-obj-checkpoint-judgment"
          note: "Caller selects judgment/completion; human-versus-agent content decision is not captured, including replacement by restoration."
        -
          scope: "Existing wiki and initial source-content admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-wiki-content"
            - "memory.md#mem-obj-source-bytes"
          note: "Neither scans nor external input bytes establish the original admission mechanism."
      records:
        - "runtime.md#rt-rte-source-ingest"
        - "memory.md#mem-obj-source-bytes"
        - "memory.md#mem-obj-url-metadata"
        - "memory.md#mem-obj-manifest"
        - "runtime.md#rt-rte-source-reconcile"
        - "memory.md#mem-obj-wiki-content"
        - "runtime.md#rt-rte-evidence-answer"
        - "memory.md#mem-rte-graph-report"
        - "memory.md#mem-obj-reconciliation-notes"
        - "runtime.md#rt-rte-workspace-recovery"
        - "memory.md#mem-obj-checkpoint-tree"
        - "memory.md#mem-obj-checkpoint-judgment"
      note: "Automatic software/model admission and explicit human write-back permission are supported locally. Generic callers, historical content and restoration control remain unresolved."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Agent reconciliation of an existing wiki claim"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-source-reconcile"
                - "memory.md#mem-obj-wiki-content"
              note: "Procedure requires revising affected prose and can withdraw a prior claim while raw sources/history remain. This supports requested evolution and invalidation, not observed execution."
            -
              value: "invalidate"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-source-reconcile"
                - "memory.md#mem-obj-wiki-content"
              note: "Procedure requires revising affected prose and can withdraw a prior claim while raw sources/history remain. This supports requested evolution and invalidation, not observed execution."
          records:
            - "runtime.md#rt-rte-source-reconcile"
            - "memory.md#mem-obj-wiki-content"
          note: "Procedure requires revising affected prose and can withdraw a prior claim while raw sources/history remain. This supports requested evolution and invalidation, not observed execution."
        -
          scope: "Ingest and conversation answer semantic transformation"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-source-ingest"
            - "runtime.md#rt-rte-evidence-answer"
            - "memory.md#mem-obj-wiki-content"
          note: "Source-to-claim meaning is not established by metadata planning or instructions to synthesize. These records do not determine consolidation versus synthesis of a new claim."
        -
          scope: "Registration, graph regeneration and Git recovery as semantic curation"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-source-ingest"
            - "memory.md#mem-rte-graph-report"
            - "runtime.md#rt-rte-workspace-recovery"
          note: "Byte acquisition, index/report construction and tree restoration do not by themselves establish any controlled semantic curation operation; no operation is inferred from names or output retention."
      records:
        - "runtime.md#rt-rte-source-reconcile"
        - "memory.md#mem-obj-wiki-content"
        - "runtime.md#rt-rte-source-ingest"
        - "runtime.md#rt-rte-evidence-answer"
        - "memory.md#mem-rte-graph-report"
        - "runtime.md#rt-rte-workspace-recovery"
      note: "Requested wiki revision and withdrawal retain their claimed layer. Actual semantic transformations in ingest/write-back are indeterminate; compilation and acquisition alone establish no curation operation."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Requested ingest metadata planning"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-source-ingest"
                - "memory.md#mem-obj-manifest"
                - "memory.md#mem-obj-wiki-metadata"
              note: "After a plan request, executable planning consumes retained source/concept metadata and returns recommendations, not source-body or wiki-prose reading by the agent."
          records:
            - "runtime.md#rt-rte-source-ingest"
            - "memory.md#mem-obj-manifest"
            - "memory.md#mem-obj-wiki-metadata"
          note: "The wired finding covers only requested metadata planning and its returned recommendations."
        -
          scope: "Agent source/wiki reading under ingest and reconciliation guidance"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-source-ingest"
                - "runtime.md#rt-rte-source-reconcile"
                - "memory.md#mem-obj-source-bytes"
                - "memory.md#mem-obj-wiki-content"
              note: "The workflows direct the agent to read retained registered inputs and affected wiki prose for requested semantic work; they do not implement or demonstrate the agent's shell-reading behavior."
          records:
            - "runtime.md#rt-rte-source-ingest"
            - "runtime.md#rt-rte-source-reconcile"
            - "memory.md#mem-obj-source-bytes"
            - "memory.md#mem-obj-wiki-content"
          note: "Direction is resolved for the delivered agent protocol, with a claimed basis distinct from executable metadata planning; actual agent compliance is unobserved."
        -
          scope: "Evidence briefs, direct search/read and continuation"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-evidence-answer"
                - "runtime.md#rt-rte-direct-retrieval"
                - "memory.md#mem-obj-wiki-content"
                - "memory.md#mem-obj-wiki-metadata"
              note: "User question leads to a host-issued retrieval request. Lexical selection and delivery within it are not another unsolicited push."
          records:
            - "runtime.md#rt-rte-evidence-answer"
            - "runtime.md#rt-rte-direct-retrieval"
            - "memory.md#mem-obj-wiki-content"
            - "memory.md#mem-obj-wiki-metadata"
          note: "User question leads to a host-issued retrieval request. Lexical selection and delivery within it are not another unsolicited push."
        -
          scope: "History and selected-tree recovery"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-workspace-recovery"
                - "memory.md#mem-obj-checkpoint-judgment"
                - "memory.md#mem-obj-checkpoint-tree"
              note: "Caller requests history or restoration, and later requested workspace operations consume restored files."
          records:
            - "runtime.md#rt-rte-workspace-recovery"
            - "memory.md#mem-obj-checkpoint-judgment"
            - "memory.md#mem-obj-checkpoint-tree"
          note: "Caller requests history or restoration, and later requested workspace operations consume restored files."
        -
          scope: "Graph report browser inspection"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-graph-report"
                - "memory.md#mem-obj-backlinks"
              note: "Caller requests generation/opening; a persisted report affords later requested inspection."
          records:
            - "memory.md#mem-rte-graph-report"
            - "memory.md#mem-obj-backlinks"
          note: "Caller requests generation/opening; a persisted report affords later requested inspection."
        -
          scope: "Requested snapshot/check consumption of manifest/edge state"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-manifest"
                - "memory.md#mem-obj-reconciliation-edges"
                - "memory.md#mem-rte-workspace-check"
              note: "Checks and evidence invocations reload access/bookkeeping state as part of the requested operation."
          records:
            - "memory.md#mem-obj-manifest"
            - "memory.md#mem-obj-reconciliation-edges"
            - "memory.md#mem-rte-workspace-check"
          note: "Checks and evidence invocations reload access/bookkeeping state as part of the requested operation."
        -
          scope: "Semantic consumption of reconciliation note reasons"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-reconciliation-notes"
          note: "Retention and parsing establish no later semantic delivery route; no direction is invented."
      records:
        - "runtime.md#rt-rte-source-ingest"
        - "runtime.md#rt-rte-source-reconcile"
        - "memory.md#mem-obj-source-bytes"
        - "memory.md#mem-obj-manifest"
        - "runtime.md#rt-rte-evidence-answer"
        - "runtime.md#rt-rte-direct-retrieval"
        - "memory.md#mem-obj-wiki-content"
        - "memory.md#mem-obj-wiki-metadata"
        - "runtime.md#rt-rte-workspace-recovery"
        - "memory.md#mem-obj-checkpoint-judgment"
        - "memory.md#mem-obj-checkpoint-tree"
        - "memory.md#mem-rte-graph-report"
        - "memory.md#mem-obj-backlinks"
        - "memory.md#mem-obj-reconciliation-edges"
        - "memory.md#mem-rte-workspace-check"
        - "memory.md#mem-obj-reconciliation-notes"
      note: "Every established delivery is requested pull. Ledger-note semantic read-back remains unresolved; static host skill discovery and external host memory are excluded rather than recast as push."
    read_back_signal:
      assessment: "not-determinable"
      units:
        -
          scope: "All established source/wiki/check/history/graph pull chains"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-source-ingest"
            - "runtime.md#rt-rte-source-reconcile"
            - "runtime.md#rt-rte-evidence-answer"
            - "runtime.md#rt-rte-direct-retrieval"
            - "memory.md#mem-rte-workspace-check"
            - "runtime.md#rt-rte-workspace-recovery"
            - "memory.md#mem-rte-graph-report"
          note: "Within these recorded requested routes there is no push selector to classify. Query words, read IDs and budgets are not push signals."
        -
          scope: "Unestablished reconciliation-note semantic consumer"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-reconciliation-notes"
          note: "Without a later delivery/selection route its direction and any push-selection input cannot be classified."
      records:
        - "runtime.md#rt-rte-source-ingest"
        - "runtime.md#rt-rte-source-reconcile"
        - "runtime.md#rt-rte-evidence-answer"
        - "runtime.md#rt-rte-direct-retrieval"
        - "memory.md#mem-rte-workspace-check"
        - "runtime.md#rt-rte-workspace-recovery"
        - "memory.md#mem-rte-graph-report"
        - "memory.md#mem-obj-reconciliation-notes"
      note: "No established accumulated-memory route is a push, but unresolved note consumption prevents a complete pull-only assessment for the entire inventory."
    trace_learning:
      assessment: "not-determinable"
      units:
        -
          scope: "Deterministic graph generation and Git tree capture"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-graph-report"
            - "memory.md#mem-obj-checkpoint-tree"
            - "runtime.md#rt-rte-workspace-recovery"
          note: "The recorded mechanisms compile links and snapshot current files rather than describing trace distillation, but no accepted bounded absence record supports a controlled no finding."
        -
          scope: "Explicitly accepted conversation write-back"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-evidence-answer"
            - "memory.md#mem-obj-wiki-content"
          note: "This specific delivered protocol requires human approval of retained content, so it is outside automatic trace-fed admission. Its later knowledge route remains supported."
        -
          scope: "Agent ingestion of arbitrary source content and wiki revision"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-bytes"
            - "runtime.md#rt-rte-source-ingest"
            - "runtime.md#rt-rte-source-reconcile"
            - "memory.md#mem-obj-wiki-content"
          note: "Automatic agent adoption is requested, but original source content is arbitrary and actual semantic transformation is unresolved. Records do not establish whether any included input is a qualifying activity trace."
        -
          scope: "Generic caller notes, judgments and initial retained content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-reconciliation-notes"
            - "memory.md#mem-obj-checkpoint-judgment"
            - "memory.md#mem-obj-wiki-content"
            - "runtime.md#rt-rte-workspace-recovery"
          note: "Caller identity and derivation inputs are unresolved; retention of rationale alone establishes neither an automatic trace-fed write nor its qualifying later consumer."
      records:
        - "memory.md#mem-rte-graph-report"
        - "memory.md#mem-obj-checkpoint-tree"
        - "runtime.md#rt-rte-workspace-recovery"
        - "runtime.md#rt-rte-evidence-answer"
        - "memory.md#mem-obj-wiki-content"
        - "memory.md#mem-obj-source-bytes"
        - "runtime.md#rt-rte-source-ingest"
        - "runtime.md#rt-rte-source-reconcile"
        - "memory.md#mem-obj-reconciliation-notes"
        - "memory.md#mem-obj-checkpoint-judgment"
      note: "No qualifying automatic trace-fed write is established, and the accepted set declares no bounded absence record licensing a local no. Arbitrary input content, initial lineage and generic caller control prevent a stronger assessment."
    trace_source:
      assessment: "not-determinable"
      units:
        -
          scope: "Non-trace graph/snapshot construction and human-admitted answer write-back"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-rte-graph-report"
            - "memory.md#mem-obj-checkpoint-tree"
            - "runtime.md#rt-rte-workspace-recovery"
            - "runtime.md#rt-rte-evidence-answer"
          note: "Graph compilation and snapshots are not trace distillation; explicit human answer retention fails automatic admission. Conversation origin alone does not establish a qualifying trace-source finding."
        -
          scope: "Arbitrary source-to-wiki and revision inputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-source-bytes"
            - "runtime.md#rt-rte-source-ingest"
            - "runtime.md#rt-rte-source-reconcile"
            - "memory.md#mem-obj-wiki-content"
          note: "No recorded content/origin establishes session logs, tool traces, event streams or trajectories as the original input to a qualifying write."
        -
          scope: "Generic caller/initial rationale paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-reconciliation-notes"
            - "memory.md#mem-obj-checkpoint-judgment"
            - "runtime.md#rt-rte-workspace-recovery"
          note: "Unknown admission, derivation and later semantic consumption prevent classifying any qualifying trace source."
      records:
        - "memory.md#mem-rte-graph-report"
        - "memory.md#mem-obj-checkpoint-tree"
        - "runtime.md#rt-rte-workspace-recovery"
        - "runtime.md#rt-rte-evidence-answer"
        - "memory.md#mem-obj-source-bytes"
        - "runtime.md#rt-rte-source-ingest"
        - "runtime.md#rt-rte-source-reconcile"
        - "memory.md#mem-obj-wiki-content"
        - "memory.md#mem-obj-reconciliation-notes"
        - "memory.md#mem-obj-checkpoint-judgment"
      note: "No qualifying automatic trace-fed route is positively established. Non-qualifying local routes are inapplicable; unresolved source and admission facts prevent declaring the axis inapplicable as a whole."
---

# OKF Harness memory profile

## Comparison rationale

The compared memory is retained workspace material, not the enclosing agent's
whole storage or prompt. Local Markdown and JSONL map to files; Git checkpoint
objects map to repo. Parsed graph edges do not imply a graph storage engine.
Opaque source bytes prevent a complete form classification without making their
known filesystem substrate opaque. See [MEM-OBJ-source-bytes](memory.md#mem-obj-source-bytes),
[MEM-OBJ-backlinks](memory.md#mem-obj-backlinks) and
[MEM-OBJ-checkpoint-tree](memory.md#mem-obj-checkpoint-tree).

Requested retrieval is pull even when code chooses excerpts automatically.
Ingest metadata planning has a wired pull finding only for its executable
metadata consumption and recommendation return. Source/wiki reading assigned
to the agent by ingest and reconciliation guidance has a separate claimed
pull finding; neither metadata planning nor pair-validation code establishes
implementation of that agent behavior. See
[RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and
[RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile).
Identifiers on a requested read and lexical matching in an evidence request
therefore establish no push signal. The unresolved semantic consumer of ledger
notes is kept local rather than converted into either an absent route or a
positive authority. See [RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer),
[RT-RTE-direct-retrieval](runtime.md#rt-rte-direct-retrieval) and
[MEM-OBJ-reconciliation-notes](memory.md#mem-obj-reconciliation-notes).

Lexically scored retained text has ranking authority as well as knowledge
authority at the answering agent. Source/citation fields also participate in
planner-local enforcement. Exact ledger pairs instead route bookkeeping:
clearing currency is not validating revised prose or unsealing evidence.
See [MEM-OBJ-wiki-metadata](memory.md#mem-obj-wiki-metadata),
[RT-CLM-evidence-boundary](runtime.md#rt-clm-evidence-boundary) and
[MEM-CLM-currency-evidence](memory.md#mem-clm-currency-evidence).
No learning authority is inferred from retaining a rationale without an update
consumer.

Agent-authored semantic changes retain their claimed evidence layer; executable
registration and retrieval remain wired. In particular, an instruction to
synthesize wiki prose does not decide whether a claim was consolidated or newly
created. Requested revision/withdrawal supports claimed evolution/invalidation,
not demonstrated semantic correctness. The explicit human yes for conversation
write-back establishes manual admission, independently of model authorship and
later knowledge use. It is not truth certification or automatic trace learning.
See [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest),
[RT-RTE-source-reconcile](runtime.md#rt-rte-source-reconcile),
[RT-RTE-evidence-answer](runtime.md#rt-rte-evidence-answer) and
[EPI-OBJ-wiki-page](epistemic.md#epi-obj-wiki-page).

Partial axes retain their unresolved included alternatives: initial provenance,
arbitrary source encodings, generic caller admission and note consumption.
No bounded absence record supports a controlled trace-learning no finding;
non-qualifying local mechanisms do not make all trace-source units inapplicable. External host compaction and model state
are outside this memory boundary, not negative examples. No observed or causal
finding is available from these records.

Reconciliation supersedes the epistemic workspace-check and graph-report routes
with [MEM-RTE-workspace-check](memory.md#mem-rte-workspace-check) and
[MEM-RTE-graph-report](memory.md#mem-rte-graph-report). All profile citations use
those canonical identities. The supersessions preserve predicate-limited checks
and parsed-connectivity derivation; they add no semantic acceptance, synthesis
or trace-learning finding. Mixed source/page/ledger containers remain valid;
this profile uses their narrower operative parts where consumers differ.

Source-read log: none. Classification used only the supplied accepted members
and reconciliation; no frozen-source ambiguity required a source read.
