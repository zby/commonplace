---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "OpenWiki memory comparison: retained wiki/Claims, resumable assignments, connector evidence, operational-trace documentation and opaque continuation/history alternatives."
run-id: "AAS-2026-10-14-openwiki-8f502f680f75-01"
source-identity: "https://github.com/langchain-ai/openwiki"
reviewed-boundary: "7c469e59584bfac3f97f5c32a67604de46805999"
memory-comparison:
  version: 2
  scope: "Use-derived repository/personal wiki pages; Claim statements, resource/version/envelope and projected metadata; resumable PageJob guidance/queue and coverage manifest; connector raw evidence/state and LangSmith-derived records/documents; persistent chat checkpoints and home-filesystem history offload; their maintenance, requested retrieval, visualization, Git/cache transfer and benchmark verdict/carry consumers. Includes unresolved dependency payload/selection and source-specific connector/evaluator retention alternatives. Excludes static shipped/installed prompts, skills and setup guidance as non-use-derived context; current-only nonchat state, transient search index/snippets, provider weights and external host-owned memory are not retained OpenWiki memory classifications."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Wiki Markdown, Claim parts/envelopes, page manifest, resumable queue and assignment guidance"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-page"
                - "memory.md#mem-obj-claim"
                - "memory.md#mem-obj-evidence"
                - "memory.md#mem-obj-page-claims"
                - "memory.md#mem-obj-page-manifest"
                - "runtime.md#rt-obj-repository-run-state"
                - "runtime.md#rt-obj-page-guidance"
              note: "Local Markdown and JSON files persist across later invocations; ClaimSession also retains process-local working copies. Filesystem is the operative durable substrate."
          records:
            - "memory.md#mem-obj-wiki-page"
            - "memory.md#mem-obj-claim"
            - "memory.md#mem-obj-evidence"
            - "memory.md#mem-obj-page-claims"
            - "memory.md#mem-obj-page-manifest"
            - "runtime.md#rt-obj-repository-run-state"
            - "runtime.md#rt-obj-page-guidance"
          note: "Local Markdown and JSON files persist across later invocations; ClaimSession also retains process-local working copies. Filesystem is the operative durable substrate."
        -
          scope: "Process-local ClaimSession"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-claim"
                - "memory.md#mem-rte-claims-reconciliation"
              note: "Session working copies of retained sidecar Claims participate in reconciliation before persistence."
          records:
            - "memory.md#mem-obj-claim"
            - "memory.md#mem-rte-claims-reconciliation"
          note: "Session working copies of retained sidecar Claims participate in reconciliation before persistence."
        -
          scope: "Repository publication of accumulated wiki and manifest"
          assessment: "known"
          findings:
            -
              value: "repo"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-manifest"
                - "runtime.md#rt-rte-maintenance-admission"
              note: "Scheduled CI proposes retained wiki/manifest changes in Git; actual merging is unobserved."
          records:
            - "memory.md#mem-obj-page-manifest"
            - "runtime.md#rt-rte-maintenance-admission"
          note: "Scheduled CI proposes retained wiki/manifest changes in Git; actual merging is unobserved."
        -
          scope: "Raw connector files/state and compact LangSmith records"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-connector-data"
                - "memory.md#mem-obj-trace"
              note: "Private local JSON retains fetched payloads, recent-run metadata and compact traces."
          records:
            - "memory.md#mem-obj-connector-data"
            - "memory.md#mem-obj-trace"
          note: "Private local JSON retains fetched payloads, recent-run metadata and compact traces."
        -
          scope: "Persistent chat checkpoint database"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-checkpoint"
                - "memory.md#mem-rte-chat-continuation"
              note: "Chat selects disk-backed openwiki.sqlite; nonchat :memory: state alone is not durable read-back memory."
          records:
            - "memory.md#mem-obj-chat-checkpoint"
            - "memory.md#mem-rte-chat-continuation"
          note: "Chat selects disk-backed openwiki.sqlite; nonchat :memory: state alone is not durable read-back memory."
        -
          scope: "Home-directory conversation-history offload"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-conversation-history"
                - "memory.md#mem-rte-history-offload"
              note: "The wired filesystem mount is separate from SQLite; payload opacity does not obscure its substrate."
          records:
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-rte-history-offload"
          note: "The wired filesystem mount is separate from SQLite; payload opacity does not obscure its substrate."
        -
          scope: "LEDGER verdict/carry working state"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-ledger-verdicts"
                - "epistemic.md#epi-rte-ledger-reporting"
                - "memory.md#mem-rte-ledger-evaluation"
              note: "Result and carry objects feed later benchmark evaluation in the continuing runner."
          records:
            - "epistemic.md#epi-obj-ledger-verdicts"
            - "epistemic.md#epi-rte-ledger-reporting"
            - "memory.md#mem-rte-ledger-evaluation"
          note: "Result and carry objects feed later benchmark evaluation in the continuing runner."
        -
          scope: "Optional LEDGER output persistence and DeepSWE cache backing"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-obj-ledger-verdicts"
            - "memory.md#mem-rte-ledger-evaluation"
            - "memory.md#mem-rte-evaluation-transfer"
          note: "Records establish captures, archives and transfers but not a complete classification of their optional backing stores."
        -
          scope: "Connector-specific retained alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-connector-data"
          note: "Individual cursor, expiry and replacement implementations were not inspected; shared file I/O does not enumerate every operative source-specific retained part."
      records:
        - "memory.md#mem-obj-wiki-page"
        - "memory.md#mem-obj-claim"
        - "memory.md#mem-obj-evidence"
        - "memory.md#mem-obj-page-claims"
        - "memory.md#mem-obj-page-manifest"
        - "runtime.md#rt-obj-repository-run-state"
        - "runtime.md#rt-obj-page-guidance"
        - "memory.md#mem-rte-claims-reconciliation"
        - "runtime.md#rt-rte-maintenance-admission"
        - "memory.md#mem-obj-connector-data"
        - "memory.md#mem-obj-trace"
        - "memory.md#mem-obj-chat-checkpoint"
        - "memory.md#mem-rte-chat-continuation"
        - "memory.md#mem-obj-conversation-history"
        - "memory.md#mem-rte-history-offload"
        - "epistemic.md#epi-obj-ledger-verdicts"
        - "epistemic.md#epi-rte-ledger-reporting"
        - "memory.md#mem-rte-ledger-evaluation"
        - "memory.md#mem-rte-evaluation-transfer"
      note: "Files and chat SQLite are established independently of opaque payload semantics. Optional evaluator output/cache persistence and source-specific connector alternatives lack complete substrate coverage."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Wiki prose, Claim statements and persisted PageJob objectives"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-page"
                - "memory.md#mem-obj-claim"
                - "runtime.md#rt-obj-page-guidance"
              note: "Models/humans interpret prose, statements and semantic assignment instructions."
          records:
            - "memory.md#mem-obj-wiki-page"
            - "memory.md#mem-obj-claim"
            - "runtime.md#rt-obj-page-guidance"
          note: "Models/humans interpret prose, statements and semantic assignment instructions."
        -
          scope: "Evidence identities/versions, Claims envelope, queue fields, manifest, verification events and page-source projection"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evidence"
                - "memory.md#mem-obj-page-claims"
                - "runtime.md#rt-obj-repository-run-state"
                - "memory.md#mem-obj-page-manifest"
                - "epistemic.md#epi-obj-verification-events"
                - "epistemic.md#epi-obj-page-sources"
              note: "Fixed rules interpret hashes, IDs, statuses, resource mappings and producer/time fields. Assignment prose and Claim statements are separate units."
          records:
            - "memory.md#mem-obj-evidence"
            - "memory.md#mem-obj-page-claims"
            - "runtime.md#rt-obj-repository-run-state"
            - "memory.md#mem-obj-page-manifest"
            - "epistemic.md#epi-obj-verification-events"
            - "epistemic.md#epi-obj-page-sources"
          note: "Fixed rules interpret hashes, IDs, statuses, resource mappings and producer/time fields. Assignment prose and Claim statements are separate units."
        -
          scope: "Compact LangSmith execution structure"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace"
              note: "IDs, metrics, buckets and execution structure have localized fixed-rule interpretation."
          records:
            - "memory.md#mem-obj-trace"
          note: "IDs, metrics, buckets and execution structure have localized fixed-rule interpretation."
        -
          scope: "Compact LangSmith names/errors at documentation model"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace"
                - "memory.md#mem-rte-trace-documentation"
              note: "Readable names and error feedback are interpreted as evidence by the authoring model."
          records:
            - "memory.md#mem-obj-trace"
            - "memory.md#mem-rte-trace-documentation"
          note: "Readable names and error feedback are interpreted as evidence by the authoring model."
        -
          scope: "Connector access/run metadata"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-connector-data"
              note: "Shared run records and access metadata are consumed by connector code."
          records:
            - "memory.md#mem-obj-connector-data"
          note: "Shared run records and access metadata are consumed by connector code."
        -
          scope: "Inspected source-text branch of connector content"
          assessment: "partial"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-connector-data"
                - "runtime.md#rt-rte-personal-ingestion"
              note: "Source text enters model curation through raw-item reads, but opaque MCP results and source-specific payload meaning remain unresolved."
          records:
            - "memory.md#mem-obj-connector-data"
            - "runtime.md#rt-rte-personal-ingestion"
          note: "Source text enters model curation through raw-item reads, but opaque MCP results and source-specific payload meaning remain unresolved."
        -
          scope: "Opaque MCP and source-specific connector payloads"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-connector-data"
          note: "JSON serialization alone cannot classify payload interpretation."
        -
          scope: "Checkpoint thread/namespace keys and pruning fields"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-checkpoint"
                - "memory.md#mem-rte-chat-continuation"
              note: "Identifiers and SQL retention rules are symbolic, distinct from restored graph payload."
          records:
            - "memory.md#mem-obj-chat-checkpoint"
            - "memory.md#mem-rte-chat-continuation"
          note: "Identifiers and SQL retention rules are symbolic, distinct from restored graph payload."
        -
          scope: "Serialized checkpoint payload delivered to the graph"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-chat-checkpoint"
            - "memory.md#mem-rte-chat-continuation"
          note: "Dependency schema, raw messages, tool results and summary alternatives were not inspected."
        -
          scope: "Actual conversation-history offload payload"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-rte-history-offload"
          note: "A readable Markdown test fixture is not evidence of actual raw/derived/mixed payload form."
        -
          scope: "LEDGER assertions/rationale at benchmark consumers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-ledger-verdicts"
                - "epistemic.md#epi-rte-ledger-judgment"
              note: "Assertions and judgment rationale are interpreted content."
          records:
            - "epistemic.md#epi-obj-ledger-verdicts"
            - "epistemic.md#epi-rte-ledger-judgment"
          note: "Assertions and judgment rationale are interpreted content."
        -
          scope: "LEDGER verdict categories, counts and carry identities"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-ledger-verdicts"
                - "epistemic.md#epi-rte-ledger-reporting"
              note: "Fixed reporting and next-evaluation rules consume verdict fields and watch state."
          records:
            - "epistemic.md#epi-obj-ledger-verdicts"
            - "epistemic.md#epi-rte-ledger-reporting"
          note: "Fixed reporting and next-evaluation rules consume verdict fields and watch state."
      records:
        - "memory.md#mem-obj-wiki-page"
        - "memory.md#mem-obj-claim"
        - "runtime.md#rt-obj-page-guidance"
        - "memory.md#mem-obj-evidence"
        - "memory.md#mem-obj-page-claims"
        - "runtime.md#rt-obj-repository-run-state"
        - "memory.md#mem-obj-page-manifest"
        - "epistemic.md#epi-obj-verification-events"
        - "epistemic.md#epi-obj-page-sources"
        - "memory.md#mem-obj-trace"
        - "memory.md#mem-rte-trace-documentation"
        - "memory.md#mem-obj-connector-data"
        - "runtime.md#rt-rte-personal-ingestion"
        - "memory.md#mem-obj-chat-checkpoint"
        - "memory.md#mem-rte-chat-continuation"
        - "memory.md#mem-obj-conversation-history"
        - "memory.md#mem-rte-history-offload"
        - "epistemic.md#epi-obj-ledger-verdicts"
        - "epistemic.md#epi-rte-ledger-judgment"
        - "epistemic.md#epi-rte-ledger-reporting"
      note: "Interpreted prose and fixed-rule control fields are split. Checkpoint payloads, actual history payloads and some connector content remain unresolved; synthetic offload test text cannot classify deployed material."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Native generated page prose, Claim statements and PageJob guidance"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-page"
                - "memory.md#mem-obj-claim"
                - "runtime.md#rt-obj-page-guidance"
                - "runtime.md#rt-rte-native-generation"
              note: "Model authoring supplies retained semantic artifacts; host authoring is separately evidenced by the host protocol."
          records:
            - "memory.md#mem-obj-wiki-page"
            - "memory.md#mem-obj-claim"
            - "runtime.md#rt-obj-page-guidance"
            - "runtime.md#rt-rte-native-generation"
          note: "Model authoring supplies retained semantic artifacts; host authoring is separately evidenced by the host protocol."
        -
          scope: "Host-authored pages/Claims and assignments"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-page"
                - "memory.md#mem-obj-claim"
                - "runtime.md#rt-obj-page-guidance"
                - "runtime.md#rt-rte-host-generation"
              note: "The shipped protocol consumes host-written prose and proposals; this does not identify a human author."
          records:
            - "memory.md#mem-obj-wiki-page"
            - "memory.md#mem-obj-claim"
            - "runtime.md#rt-obj-page-guidance"
            - "runtime.md#rt-rte-host-generation"
          note: "The shipped protocol consumes host-written prose and proposals; this does not identify a human author."
        -
          scope: "Code-owned evidence versions, envelopes, manifest and queue progression"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evidence"
                - "memory.md#mem-obj-page-claims"
                - "memory.md#mem-obj-page-manifest"
                - "runtime.md#rt-obj-repository-run-state"
                - "memory.md#mem-rte-claims-reconciliation"
              note: "Deterministic resolution, persistence and lifecycle code compile symbolic retained state."
          records:
            - "memory.md#mem-obj-evidence"
            - "memory.md#mem-obj-page-claims"
            - "memory.md#mem-obj-page-manifest"
            - "runtime.md#rt-obj-repository-run-state"
            - "memory.md#mem-rte-claims-reconciliation"
          note: "Deterministic resolution, persistence and lifecycle code compile symbolic retained state."
        -
          scope: "Translated page branch"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-page-translation"
                - "memory.md#mem-obj-wiki-page"
              note: "A direct model call authors replacement prose from retained page text; semantic fidelity is unobserved."
          records:
            - "runtime.md#rt-rte-page-translation"
            - "memory.md#mem-obj-wiki-page"
          note: "A direct model call authors replacement prose from retained page text; semantic fidelity is unobserved."
        -
          scope: "Fetched connector source content"
          assessment: "partial"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-connector-data"
                - "runtime.md#rt-rte-personal-ingestion"
              note: "Shared connector acquisition imports external payloads; source-specific prior provenance is not resolved."
          records:
            - "memory.md#mem-obj-connector-data"
            - "runtime.md#rt-rte-personal-ingestion"
          note: "Shared connector acquisition imports external payloads; source-specific prior provenance is not resolved."
        -
          scope: "Connector run/access metadata"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-connector-data"
              note: "Shared helper derives local run records from acquisition results."
          records:
            - "memory.md#mem-obj-connector-data"
          note: "Shared helper derives local run records from acquisition results."
        -
          scope: "Compact operational trace extraction"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace"
                - "memory.md#mem-rte-trace-documentation"
              note: "External run trees become ordered reduced operational records; originals are external activity traces."
          records:
            - "memory.md#mem-obj-trace"
            - "memory.md#mem-rte-trace-documentation"
          note: "External run trees become ordered reduced operational records; originals are external activity traces."
        -
          scope: "Trace-fed documentation branch"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-documentation"
                - "memory.md#mem-obj-wiki-page"
              note: "Model-curated runtime findings are extracted/authored from operational evidence plus repository research."
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-documentation"
                - "memory.md#mem-obj-wiki-page"
              note: "Model-curated runtime findings are extracted/authored from operational evidence plus repository research."
          records:
            - "memory.md#mem-rte-trace-documentation"
            - "memory.md#mem-obj-wiki-page"
          note: "Model-curated runtime findings are extracted/authored from operational evidence plus repository research."
        -
          scope: "Code-owned whole-file sources and verification projections"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-source-projection"
                - "epistemic.md#epi-rte-verification-projection"
              note: "Finalizers derive retained metadata from existing Claims/resources and durable eligibility."
          records:
            - "epistemic.md#epi-rte-source-projection"
            - "epistemic.md#epi-rte-verification-projection"
          note: "Finalizers derive retained metadata from existing Claims/resources and durable eligibility."
        -
          scope: "Preserved independently authored page-source/verification entries"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-obj-page-sources"
            - "epistemic.md#epi-obj-verification-events"
            - "epistemic.md#epi-rte-source-projection"
            - "epistemic.md#epi-rte-verification-projection"
          note: "Preservation is recorded, but initial authorship/import path is not established for every foreign entry."
        -
          scope: "DeepSWE destination wiki"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-rte-evaluation-transfer"
              note: "The driver imports generated or cached artifacts into the later task workspace; it does not regenerate every cache hit."
          records:
            - "memory.md#mem-rte-evaluation-transfer"
          note: "The driver imports generated or cached artifacts into the later task workspace; it does not regenerate every cache hit."
        -
          scope: "LEDGER model verdicts and fixed result/carry derivation"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-ledger-verdicts"
                - "epistemic.md#epi-rte-ledger-judgment"
                - "epistemic.md#epi-rte-ledger-reporting"
              note: "Model judgment authors verdict/rationale; reporting compiles categories, metrics and watch state."
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-ledger-verdicts"
                - "epistemic.md#epi-rte-ledger-judgment"
                - "epistemic.md#epi-rte-ledger-reporting"
              note: "Model judgment authors verdict/rationale; reporting compiles categories, metrics and watch state."
          records:
            - "epistemic.md#epi-obj-ledger-verdicts"
            - "epistemic.md#epi-rte-ledger-judgment"
            - "epistemic.md#epi-rte-ledger-reporting"
          note: "Model judgment authors verdict/rationale; reporting compiles categories, metrics and watch state."
        -
          scope: "Checkpoint payload and conversation-history production"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-chat-checkpoint"
            - "memory.md#mem-rte-chat-continuation"
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-rte-history-offload"
          note: "Dependency-owned serialization, raw-to-summary lineage and production selection are not inspected; keys/mounts do not resolve these paths."
        -
          scope: "Source-specific connector and evaluator retention alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-connector-data"
            - "memory.md#mem-rte-ledger-evaluation"
          note: "Shared import/runner paths do not establish every initialization and derivation."
      records:
        - "memory.md#mem-obj-wiki-page"
        - "memory.md#mem-obj-claim"
        - "runtime.md#rt-obj-page-guidance"
        - "runtime.md#rt-rte-native-generation"
        - "runtime.md#rt-rte-host-generation"
        - "memory.md#mem-obj-evidence"
        - "memory.md#mem-obj-page-claims"
        - "memory.md#mem-obj-page-manifest"
        - "runtime.md#rt-obj-repository-run-state"
        - "memory.md#mem-rte-claims-reconciliation"
        - "runtime.md#rt-rte-page-translation"
        - "memory.md#mem-obj-connector-data"
        - "runtime.md#rt-rte-personal-ingestion"
        - "memory.md#mem-obj-trace"
        - "memory.md#mem-rte-trace-documentation"
        - "epistemic.md#epi-rte-source-projection"
        - "epistemic.md#epi-rte-verification-projection"
        - "epistemic.md#epi-obj-page-sources"
        - "epistemic.md#epi-obj-verification-events"
        - "memory.md#mem-rte-evaluation-transfer"
        - "epistemic.md#epi-obj-ledger-verdicts"
        - "epistemic.md#epi-rte-ledger-judgment"
        - "epistemic.md#epi-rte-ledger-reporting"
        - "memory.md#mem-obj-chat-checkpoint"
        - "memory.md#mem-rte-chat-continuation"
        - "memory.md#mem-obj-conversation-history"
        - "memory.md#mem-rte-history-offload"
        - "memory.md#mem-rte-ledger-evaluation"
      note: "Known derivations remain local: authoring, imports, compilation and trace extraction coexist. Existing independent metadata, connector alternatives and dependency payload derivation prevent complete lineage classification."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Wiki prose at later authors, retrieval hosts, personal chat and human visualization"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-page"
                - "runtime.md#rt-rte-wiki-retrieval"
                - "runtime.md#rt-rte-personal-ingestion"
                - "memory.md#mem-rte-visualizer-delivery"
              note: "Retained prose supplies evidence/context/reference, not standing host instructions under shipped guidance."
          records:
            - "memory.md#mem-obj-wiki-page"
            - "runtime.md#rt-rte-wiki-retrieval"
            - "runtime.md#rt-rte-personal-ingestion"
            - "memory.md#mem-rte-visualizer-delivery"
          note: "Retained prose supplies evidence/context/reference, not standing host instructions under shipped guidance."
        -
          scope: "Retained wiki text/frontmatter/source hints at retrieval ranker"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-retrieval"
                - "memory.md#mem-obj-wiki-page"
                - "epistemic.md#epi-obj-page-sources"
              note: "Text is scored lexically and source/path metadata affects relative priority; no learned policy is required."
          records:
            - "runtime.md#rt-rte-wiki-retrieval"
            - "memory.md#mem-obj-wiki-page"
            - "epistemic.md#epi-obj-page-sources"
          note: "Text is scored lexically and source/path metadata affects relative priority; no learned policy is required."
        -
          scope: "Deprecated status at search eligibility"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-retrieval"
                - "memory.md#mem-obj-wiki-page"
              note: "Search status excludes deprecated pages from delivery; explicit section reads do not repeat the gate."
          records:
            - "runtime.md#rt-rte-wiki-retrieval"
            - "memory.md#mem-obj-wiki-page"
          note: "Search status excludes deprecated pages from delivery; explicit section reads do not repeat the gate."
        -
          scope: "Claim statements and associated resources at maintenance model/host"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-claim"
                - "memory.md#mem-obj-evidence"
                - "memory.md#mem-rte-claims-reconciliation"
                - "memory.md#mem-bap-claims-maintenance"
              note: "Statements and resource identities supply maintenance evidence; freshness issues do not prove truth."
          records:
            - "memory.md#mem-obj-claim"
            - "memory.md#mem-obj-evidence"
            - "memory.md#mem-rte-claims-reconciliation"
            - "memory.md#mem-bap-claims-maintenance"
          note: "Statements and resource identities supply maintenance evidence; freshness issues do not prove truth."
        -
          scope: "Evidence versions/Claim membership/envelope at reconciliation and durability checks"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evidence"
                - "memory.md#mem-obj-page-claims"
                - "memory.md#mem-rte-claims-reconciliation"
                - "epistemic.md#epi-rte-claim-decisions"
                - "epistemic.md#epi-rte-claims-persistence"
              note: "Retained IDs, versions and state provide admissibility criteria and veto invalid transitions."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evidence"
                - "memory.md#mem-obj-page-claims"
                - "memory.md#mem-rte-claims-reconciliation"
                - "epistemic.md#epi-rte-claim-decisions"
                - "epistemic.md#epi-rte-claims-persistence"
              note: "Retained IDs, versions and state provide admissibility criteria and veto invalid transitions."
          records:
            - "memory.md#mem-obj-evidence"
            - "memory.md#mem-obj-page-claims"
            - "memory.md#mem-rte-claims-reconciliation"
            - "epistemic.md#epi-rte-claim-decisions"
            - "epistemic.md#epi-rte-claims-persistence"
          note: "Retained IDs, versions and state provide admissibility criteria and veto invalid transitions."
        -
          scope: "Queue, manifest and freshness issue state at lifecycle selection"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-repository-run-state"
                - "memory.md#mem-obj-page-manifest"
                - "memory.md#mem-rte-claims-reconciliation"
                - "epistemic.md#epi-rte-evidence-preflight"
              note: "Retained progress/checkpoints and debt select phase, next work, source windows and required page work."
          records:
            - "runtime.md#rt-obj-repository-run-state"
            - "memory.md#mem-obj-page-manifest"
            - "memory.md#mem-rte-claims-reconciliation"
            - "epistemic.md#epi-rte-evidence-preflight"
          note: "Retained progress/checkpoints and debt select phase, next work, source windows and required page work."
        -
          scope: "Persisted PageJob guidance at native worker or resumed host"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-page-guidance"
                - "runtime.md#rt-bap-page-instructions"
              note: "Purpose/instructions supply directions for assigned work across stages/resume."
          records:
            - "runtime.md#rt-obj-page-guidance"
            - "runtime.md#rt-bap-page-instructions"
          note: "Purpose/instructions supply directions for assigned work across stages/resume."
        -
          scope: "Connector run/cursor access metadata at raw selection"
          assessment: "partial"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-connector-data"
                - "runtime.md#rt-rte-personal-ingestion"
              note: "Known run/access fields select retained raw files for reads; detailed source-specific cursor authority is unresolved."
          records:
            - "memory.md#mem-obj-connector-data"
            - "runtime.md#rt-rte-personal-ingestion"
          note: "Known run/access fields select retained raw files for reads; detailed source-specific cursor authority is unresolved."
        -
          scope: "Raw source text at personal curation and compact traces at documentation update"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-connector-data"
                - "memory.md#mem-obj-trace"
                - "runtime.md#rt-rte-personal-ingestion"
                - "memory.md#mem-rte-trace-documentation"
              note: "The authoring model receives source content/execution evidence as context."
          records:
            - "memory.md#mem-obj-connector-data"
            - "memory.md#mem-obj-trace"
            - "runtime.md#rt-rte-personal-ingestion"
            - "memory.md#mem-rte-trace-documentation"
          note: "The authoring model receives source content/execution evidence as context."
        -
          scope: "Retained operational traces at automatic documentation update"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace"
                - "memory.md#mem-rte-trace-documentation"
              note: "Retained experience feeds durable behavior-shaping documents; this is learning force at the update consumer, not measured improved capacity."
          records:
            - "memory.md#mem-obj-trace"
            - "memory.md#mem-rte-trace-documentation"
          note: "Retained experience feeds durable behavior-shaping documents; this is learning force at the update consumer, not measured improved capacity."
        -
          scope: "Checkpoint thread/namespace keys at continuation selector"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-checkpoint"
                - "memory.md#mem-rte-chat-continuation"
              note: "Retained keyed state selects the graph continuation namespace. Opaque content force at the next model is separate."
          records:
            - "memory.md#mem-obj-chat-checkpoint"
            - "memory.md#mem-rte-chat-continuation"
          note: "Retained keyed state selects the graph continuation namespace. Opaque content force at the next model is separate."
        -
          scope: "LEDGER verdict/carry at benchmark reporting and subsequent evaluation"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-ledger-verdicts"
                - "epistemic.md#epi-rte-ledger-reporting"
                - "memory.md#mem-rte-ledger-evaluation"
              note: "Verdicts supply assessment context; obsolete targets and previous artifacts select later evaluation scope. No product-edit gate is established."
            -
              value: "routing"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-ledger-verdicts"
                - "epistemic.md#epi-rte-ledger-reporting"
                - "memory.md#mem-rte-ledger-evaluation"
              note: "Verdicts supply assessment context; obsolete targets and previous artifacts select later evaluation scope. No product-edit gate is established."
          records:
            - "epistemic.md#epi-obj-ledger-verdicts"
            - "epistemic.md#epi-rte-ledger-reporting"
            - "memory.md#mem-rte-ledger-evaluation"
          note: "Verdicts supply assessment context; obsolete targets and previous artifacts select later evaluation scope. No product-edit gate is established."
        -
          scope: "Opaque checkpoint content and actual history payload at later model"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-chat-checkpoint"
            - "memory.md#mem-rte-chat-continuation"
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-rte-history-offload"
          note: "The exact delivered part/effect and automatic replay are unresolved; a known key or backend read capability does not resolve knowledge versus instruction force."
        -
          scope: "Source-specific connectors and optional evaluator consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-connector-data"
            - "memory.md#mem-rte-ledger-evaluation"
          note: "Uninspected source-specific state and output consumers prevent a complete authority inventory."
      records:
        - "memory.md#mem-obj-wiki-page"
        - "runtime.md#rt-rte-wiki-retrieval"
        - "runtime.md#rt-rte-personal-ingestion"
        - "memory.md#mem-rte-visualizer-delivery"
        - "epistemic.md#epi-obj-page-sources"
        - "memory.md#mem-obj-claim"
        - "memory.md#mem-obj-evidence"
        - "memory.md#mem-rte-claims-reconciliation"
        - "memory.md#mem-bap-claims-maintenance"
        - "memory.md#mem-obj-page-claims"
        - "epistemic.md#epi-rte-claim-decisions"
        - "epistemic.md#epi-rte-claims-persistence"
        - "runtime.md#rt-obj-repository-run-state"
        - "memory.md#mem-obj-page-manifest"
        - "epistemic.md#epi-rte-evidence-preflight"
        - "runtime.md#rt-obj-page-guidance"
        - "runtime.md#rt-bap-page-instructions"
        - "memory.md#mem-obj-connector-data"
        - "memory.md#mem-obj-trace"
        - "memory.md#mem-rte-trace-documentation"
        - "memory.md#mem-obj-chat-checkpoint"
        - "memory.md#mem-rte-chat-continuation"
        - "epistemic.md#epi-obj-ledger-verdicts"
        - "epistemic.md#epi-rte-ledger-reporting"
        - "memory.md#mem-rte-ledger-evaluation"
        - "memory.md#mem-obj-conversation-history"
        - "memory.md#mem-rte-history-offload"
      note: "Forces are attached to actual consumers, not JSON/file labels. Supported knowledge, instructions, routing, validation, enforcement, ranking and trace-update learning coexist with unresolved dependency payload consumers."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Native pages, Claims and persisted planner jobs"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-native-generation"
                - "memory.md#mem-rte-claims-reconciliation"
                - "runtime.md#rt-obj-repository-run-state"
                - "runtime.md#rt-obj-page-guidance"
              note: "Models propose and core software admits without a per-content human decision."
          records:
            - "runtime.md#rt-rte-native-generation"
            - "memory.md#mem-rte-claims-reconciliation"
            - "runtime.md#rt-obj-repository-run-state"
            - "runtime.md#rt-obj-page-guidance"
          note: "Models propose and core software admits without a per-content human decision."
        -
          scope: "Evidence/envelope/manifest and projected provenance/events"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evidence"
                - "memory.md#mem-obj-page-claims"
                - "memory.md#mem-obj-page-manifest"
                - "epistemic.md#epi-rte-source-projection"
                - "epistemic.md#epi-rte-verification-projection"
              note: "Deterministic code resolves, validates and persists retained metadata."
          records:
            - "memory.md#mem-obj-evidence"
            - "memory.md#mem-obj-page-claims"
            - "memory.md#mem-obj-page-manifest"
            - "epistemic.md#epi-rte-source-projection"
            - "epistemic.md#epi-rte-verification-projection"
          note: "Deterministic code resolves, validates and persists retained metadata."
        -
          scope: "Personal model writes and deterministic connector acquisition"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-personal-ingestion"
                - "memory.md#mem-obj-connector-data"
              note: "The model/filesystem and connector software admit content; initiating ingestion is not per-item approval."
          records:
            - "runtime.md#rt-rte-personal-ingestion"
            - "memory.md#mem-obj-connector-data"
          note: "The model/filesystem and connector software admit content; initiating ingestion is not per-item approval."
        -
          scope: "Trace-fed documentation and compact trace persistence"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-documentation"
                - "memory.md#mem-obj-trace"
              note: "Code selects/imports traces and model/core admission writes local documents without per-finding human approval."
          records:
            - "memory.md#mem-rte-trace-documentation"
            - "memory.md#mem-obj-trace"
          note: "Code selects/imports traces and model/core admission writes local documents without per-finding human approval."
        -
          scope: "Translation replacement and retry metadata"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-page-translation"
              note: "Code admits checked model output or retry markers, with no per-page human approval."
          records:
            - "runtime.md#rt-rte-page-translation"
          note: "Code admits checked model output or retry markers, with no per-page human approval."
        -
          scope: "Chat state persistence"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-chat-continuation"
              note: "Graph/dependency state persistence is software admission without a human decision for each retained item. Exact restored payload is independently uninspected."
          records:
            - "memory.md#mem-rte-chat-continuation"
          note: "Graph/dependency state persistence is software admission without a human decision for each retained item. Exact restored payload is independently uninspected."
        -
          scope: "Intended middleware history offload admission"
          assessment: "partial"
          findings:
            -
              value: "automatic"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-history-offload"
              note: "The intended middleware producer has direct backend write access without a per-offload human decision. The contract affords automatic admission; dependency production wiring and content policy are not inspected."
          records:
            - "memory.md#mem-rte-history-offload"
          note: "The intended middleware producer has direct backend write access without a per-offload human decision. The contract affords automatic admission; dependency production wiring and content policy are not inspected."
        -
          scope: "Benchmark capture, verdict/cache/carry and DeepSWE artifact replacement"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-ledger-evaluation"
                - "epistemic.md#epi-rte-ledger-judgment"
                - "epistemic.md#epi-rte-ledger-reporting"
                - "memory.md#mem-rte-evaluation-transfer"
              note: "Shipped software selects captures, judgment reuse and workspace/cache replacement."
          records:
            - "memory.md#mem-rte-ledger-evaluation"
            - "epistemic.md#epi-rte-ledger-judgment"
            - "epistemic.md#epi-rte-ledger-reporting"
            - "memory.md#mem-rte-evaluation-transfer"
          note: "Shipped software selects captures, judgment reuse and workspace/cache replacement."
        -
          scope: "Host-written content and external edits"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-host-generation"
            - "memory.md#mem-rte-claims-reconciliation"
          note: "Host identity and editable files do not establish whether a human supplies, edits or approves each admitted item."
        -
          scope: "PR merge into future Git baseline"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-maintenance-admission"
          note: "CI creates a proposal automatically, but deployed merge approver/policy is not inspected; manual merge cannot be inferred."
        -
          scope: "Initial independent sources/foreign verification and source-specific state"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-rte-source-projection"
            - "epistemic.md#epi-rte-verification-projection"
            - "memory.md#mem-obj-connector-data"
          note: "Preserved entries and shared I/O do not establish their original content-control mechanisms."
      records:
        - "runtime.md#rt-rte-native-generation"
        - "memory.md#mem-rte-claims-reconciliation"
        - "runtime.md#rt-obj-repository-run-state"
        - "runtime.md#rt-obj-page-guidance"
        - "memory.md#mem-obj-evidence"
        - "memory.md#mem-obj-page-claims"
        - "memory.md#mem-obj-page-manifest"
        - "epistemic.md#epi-rte-source-projection"
        - "epistemic.md#epi-rte-verification-projection"
        - "runtime.md#rt-rte-personal-ingestion"
        - "memory.md#mem-obj-connector-data"
        - "memory.md#mem-rte-trace-documentation"
        - "memory.md#mem-obj-trace"
        - "runtime.md#rt-rte-page-translation"
        - "memory.md#mem-rte-chat-continuation"
        - "memory.md#mem-rte-history-offload"
        - "memory.md#mem-rte-ledger-evaluation"
        - "epistemic.md#epi-rte-ledger-judgment"
        - "epistemic.md#epi-rte-ledger-reporting"
        - "memory.md#mem-rte-evaluation-transfer"
        - "runtime.md#rt-rte-host-generation"
        - "runtime.md#rt-rte-maintenance-admission"
      note: "Native/model/code admission is automatic even when an operator starts a workflow. Host control, Git merge approval and independent initial entries remain unresolved; no generic caller identity establishes manual admission."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Sparse existing Claim revisions"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-claims-reconciliation"
                - "epistemic.md#epi-rte-claim-decisions"
              note: "Update replaces an existing statement/evidence entry. Retraction deletes current membership rather than proving history-preserving invalidation."
          records:
            - "memory.md#mem-rte-claims-reconciliation"
            - "epistemic.md#epi-rte-claim-decisions"
          note: "Update replaces an existing statement/evidence entry. Retraction deletes current membership rather than proving history-preserving invalidation."
        -
          scope: "Page translation replacement"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-page-translation"
              note: "Accepted translated output rewrites an existing page; no new factual claim or fidelity is inferred."
          records:
            - "runtime.md#rt-rte-page-translation"
          note: "Accepted translated output rewrites an existing page; no new factual claim or fidelity is inferred."
        -
          scope: "Whole-file source projection"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-source-projection"
              note: "Range-specific resources collapse into reduced existing file identities and duplicate identities are removed; independent entries are preserved."
            -
              value: "dedup"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-source-projection"
              note: "Range-specific resources collapse into reduced existing file identities and duplicate identities are removed; independent entries are preserved."
          records:
            - "epistemic.md#epi-rte-source-projection"
          note: "Range-specific resources collapse into reduced existing file identities and duplicate identities are removed; independent entries are preserved."
        -
          scope: "Deprecated page search suppression and producer verification withdrawal"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-retrieval"
                - "epistemic.md#epi-rte-verification-projection"
              note: "Search withdraws reliance while retaining the page; projection removes inactive producer stamps while prose and foreign events remain. This is not universal withdrawal from direct reads/copies."
          records:
            - "runtime.md#rt-rte-wiki-retrieval"
            - "epistemic.md#epi-rte-verification-projection"
          note: "Search withdraws reliance while retaining the page; projection removes inactive producer stamps while prose and foreign events remain. This is not universal withdrawal from direct reads/copies."
        -
          scope: "Checkpoint row pruning and connector recent-run truncation"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-chat-continuation"
                - "memory.md#mem-obj-connector-data"
              note: "Old checkpoint rows/orphan writes and old run-list entries are removed. This does not prove removal of turns inside surviving state or deletion of raw files/history."
          records:
            - "memory.md#mem-rte-chat-continuation"
            - "memory.md#mem-obj-connector-data"
          note: "Old checkpoint rows/orphan writes and old run-list entries are removed. This does not prove removal of turns inside surviving state or deletion of raw files/history."
        -
          scope: "LangSmith compact operational-record transformation"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace"
                - "memory.md#mem-rte-trace-documentation"
              note: "The inspected reduction keeps execution structure/metrics/errors rather than full operational payload, a reduced representation of existing trace content."
          records:
            - "memory.md#mem-obj-trace"
            - "memory.md#mem-rte-trace-documentation"
          note: "The inspected reduction keeps execution structure/metrics/errors rather than full operational payload, a reduced representation of existing trace content."
        -
          scope: "Model creation of code-linked runtime implications"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-trace-documentation"
          note: "Recorded authoring guidance requests supported implications and patterns, but establishes no implemented creation of a claim absent from the inputs. It cannot support a synthesize finding, even with claimed basis."
        -
          scope: "Incremental/additive runtime-document refinement"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-trace-documentation"
          note: "Recorded guidance requests refinement, but does not establish an implemented revision of existing retained documentation. The document-write route alone cannot support an evolve finding for this transformation."
        -
          scope: "Actual model prose transformation beyond inspected replacement operations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-wiki-page"
            - "memory.md#mem-rte-trace-documentation"
            - "runtime.md#rt-rte-personal-ingestion"
          note: "Generated input/output propositions are unavailable, preventing distinction between consolidation and genuinely new-claim synthesis."
        -
          scope: "Dependency history compaction and checkpoint-content maintenance"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-history-offload"
            - "memory.md#mem-rte-chat-continuation"
          note: "A summarization producer label/test does not establish the actual transformation or retained tail."
        -
          scope: "Source-specific connector expiry/replacement and evaluator retirement"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-connector-data"
            - "memory.md#mem-rte-ledger-evaluation"
            - "epistemic.md#epi-rte-ledger-reporting"
          note: "Shared truncation and benchmark carry do not enumerate individual expiry or semantic retirement operations."
      records:
        - "memory.md#mem-rte-claims-reconciliation"
        - "epistemic.md#epi-rte-claim-decisions"
        - "runtime.md#rt-rte-page-translation"
        - "epistemic.md#epi-rte-source-projection"
        - "runtime.md#rt-rte-wiki-retrieval"
        - "epistemic.md#epi-rte-verification-projection"
        - "memory.md#mem-rte-chat-continuation"
        - "memory.md#mem-obj-connector-data"
        - "memory.md#mem-obj-trace"
        - "memory.md#mem-rte-trace-documentation"
        - "memory.md#mem-obj-wiki-page"
        - "runtime.md#rt-rte-personal-ingestion"
        - "memory.md#mem-rte-history-offload"
        - "memory.md#mem-rte-ledger-evaluation"
        - "epistemic.md#epi-rte-ledger-reporting"
      note: "Implemented revisions, reduced projections, deduplication, withdrawal and deletion are retained. Requested runtime implications and refinement establish no curation positives; their transformations, opaque summarization and connector-specific maintenance remain unresolved."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Requested host wiki search/section reads and personal wiki/raw tool reads"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-wiki-retrieval"
                - "runtime.md#rt-rte-personal-ingestion"
                - "memory.md#mem-obj-connector-data"
              note: "Foreground consumers request retained material; ranking and returning the request do not add an unsolicited push."
          records:
            - "runtime.md#rt-rte-wiki-retrieval"
            - "runtime.md#rt-rte-personal-ingestion"
            - "memory.md#mem-obj-connector-data"
          note: "Foreground consumers request retained material; ranking and returning the request do not add an unsolicited push."
        -
          scope: "Requested full page Claim inspection"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-claims-reconciliation"
              note: "Worker/host explicitly requests complete compact current Claims."
          records:
            - "memory.md#mem-rte-claims-reconciliation"
          note: "Worker/host explicitly requests complete compact current Claims."
        -
          scope: "Automatic persisted PageJob guidance and issue Claims in assignments"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-page-guidance"
                - "runtime.md#rt-rte-native-generation"
                - "memory.md#mem-rte-claims-reconciliation"
              note: "At worker construction/resume, core selects retained assignment and attention Claims without a content read request by that worker."
          records:
            - "runtime.md#rt-obj-page-guidance"
            - "runtime.md#rt-rte-native-generation"
            - "memory.md#mem-rte-claims-reconciliation"
          note: "At worker construction/resume, core selects retained assignment and attention Claims without a content read request by that worker."
        -
          scope: "Automatic lifecycle reload of queue, manifest and sidecars"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-repository-run-state"
                - "memory.md#mem-obj-page-manifest"
                - "memory.md#mem-rte-claims-reconciliation"
              note: "Begin/resume loads retained control state to drive the later lifecycle invocation."
          records:
            - "runtime.md#rt-obj-repository-run-state"
            - "memory.md#mem-obj-page-manifest"
            - "memory.md#mem-rte-claims-reconciliation"
          note: "Begin/resume loads retained control state to drive the later lifecycle invocation."
        -
          scope: "Chat continuation thread request"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-chat-continuation"
                - "memory.md#mem-obj-chat-checkpoint"
              note: "Caller supplies a thread for graph continuation; satisfying that keyed continuation request is pull at the request boundary."
          records:
            - "memory.md#mem-rte-chat-continuation"
            - "memory.md#mem-obj-chat-checkpoint"
          note: "Caller supplies a thread for graph continuation; satisfying that keyed continuation request is pull at the request boundary."
        -
          scope: "Checkpoint model-context delivery operations"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-chat-continuation"
            - "memory.md#mem-obj-chat-checkpoint"
          note: "The later graph restore is wired, but dependency selection of opaque retained turns/summaries into model context is uninspected; additional push operations cannot be excluded."
        -
          scope: "Visualizer requested graph projection"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-visualizer-delivery"
              note: "A later visualization request consumes the retained wiki; browser details do not change the inspected requested build."
          records:
            - "memory.md#mem-rte-visualizer-delivery"
          note: "A later visualization request consumes the retained wiki; browser details do not change the inspected requested build."
        -
          scope: "LEDGER automatic carry and artifact supply to next evaluation"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-ledger-evaluation"
                - "epistemic.md#epi-rte-ledger-reporting"
              note: "Runner supplies accumulated previous artifact/watch state to a subsequent evaluator call automatically."
          records:
            - "memory.md#mem-rte-ledger-evaluation"
            - "epistemic.md#epi-rte-ledger-reporting"
          note: "Runner supplies accumulated previous artifact/watch state to a subsequent evaluator call automatically."
        -
          scope: "DeepSWE artifact transfer into downstream task workspace"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-evaluation-transfer"
              note: "Preparation selects generated/cached retained wiki and copies it before a separate task host run; later host section requests remain pull."
          records:
            - "memory.md#mem-rte-evaluation-transfer"
          note: "Preparation selects generated/cached retained wiki and copies it before a separate task host run; later host section requests remain pull."
        -
          scope: "Native history offload reload and cross-worker selection"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-rte-history-offload"
          note: "Backend read affordance is known, but no actual automatic delivery chain or exercised requesting consumer is established. It cannot resolve a direction unit by itself."
        -
          scope: "Source-specific connector and remaining evaluator consumer routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-connector-data"
            - "memory.md#mem-rte-ledger-evaluation"
          note: "Uninspected alternatives prevent complete read-back direction coverage."
      records:
        - "runtime.md#rt-rte-wiki-retrieval"
        - "runtime.md#rt-rte-personal-ingestion"
        - "memory.md#mem-obj-connector-data"
        - "memory.md#mem-rte-claims-reconciliation"
        - "runtime.md#rt-obj-page-guidance"
        - "runtime.md#rt-rte-native-generation"
        - "runtime.md#rt-obj-repository-run-state"
        - "memory.md#mem-obj-page-manifest"
        - "memory.md#mem-rte-chat-continuation"
        - "memory.md#mem-obj-chat-checkpoint"
        - "memory.md#mem-rte-visualizer-delivery"
        - "memory.md#mem-rte-ledger-evaluation"
        - "epistemic.md#epi-rte-ledger-reporting"
        - "memory.md#mem-rte-evaluation-transfer"
        - "memory.md#mem-obj-conversation-history"
        - "memory.md#mem-rte-history-offload"
      note: "Requested retrieval and tool reads coexist with automatic assignment/context and evaluation carry. Dependency payload selection and actual history reload are unresolved rather than converted into pull-only inapplicability."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Persisted guidance selected for assigned job"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-page-guidance"
                - "runtime.md#rt-rte-native-generation"
                - "runtime.md#rt-rte-host-generation"
              note: "Trigger is worker/host assignment or resume; pending job/page identity selects the retained guidance actually delivered."
          records:
            - "runtime.md#rt-obj-page-guidance"
            - "runtime.md#rt-rte-native-generation"
            - "runtime.md#rt-rte-host-generation"
          note: "Trigger is worker/host assignment or resume; pending job/page identity selects the retained guidance actually delivered."
        -
          scope: "Issue Claims selected into assignment"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-claims-reconciliation"
                - "runtime.md#rt-rte-native-generation"
                - "epistemic.md#epi-rte-evidence-preflight"
              note: "Trigger is next page assignment; exact owning page/job selects retained Claims, then stale/unresolved issue status selects the attention subset."
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-claims-reconciliation"
                - "runtime.md#rt-rte-native-generation"
                - "epistemic.md#epi-rte-evidence-preflight"
              note: "Trigger is next page assignment; exact owning page/job selects retained Claims, then stale/unresolved issue status selects the attention subset."
          records:
            - "memory.md#mem-rte-claims-reconciliation"
            - "runtime.md#rt-rte-native-generation"
            - "epistemic.md#epi-rte-evidence-preflight"
          note: "Trigger is next page assignment; exact owning page/job selects retained Claims, then stale/unresolved issue status selects the attention subset."
        -
          scope: "Lifecycle control-state reload"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-repository-run-state"
                - "memory.md#mem-obj-page-manifest"
                - "memory.md#mem-rte-claims-reconciliation"
              note: "Trigger is begin/resume; wiki/page paths select retained run, manifest and sidecar state for code consumers."
          records:
            - "runtime.md#rt-obj-repository-run-state"
            - "memory.md#mem-obj-page-manifest"
            - "memory.md#mem-rte-claims-reconciliation"
          note: "Trigger is begin/resume; wiki/page paths select retained run, manifest and sidecar state for code consumers."
        -
          scope: "LEDGER previous artifact and obsolete watch-state carry"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-ledger-evaluation"
                - "epistemic.md#epi-rte-ledger-reporting"
              note: "Trigger is advancing benchmark checkpoint; availability of continuing carry supplies prior artifact/watch state. No semantic similarity selector is established by the runner."
          records:
            - "memory.md#mem-rte-ledger-evaluation"
            - "epistemic.md#epi-rte-ledger-reporting"
          note: "Trigger is advancing benchmark checkpoint; availability of continuing carry supplies prior artifact/watch state. No semantic similarity selector is established by the runner."
        -
          scope: "DeepSWE generated/cached artifact supply"
          assessment: "partial"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-evaluation-transfer"
              note: "Trigger is task preparation; task base/package digest/model cache identity selects a retained wiki for copying. Compatible older-cache selection is recorded but complete key trust remains unassessed."
          records:
            - "memory.md#mem-rte-evaluation-transfer"
          note: "Trigger is task preparation; task base/package digest/model cache identity selects a retained wiki for copying. Compatible older-cache selection is recorded but complete key trust remains unassessed."
        -
          scope: "Opaque checkpoint delivery selector"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-chat-checkpoint"
            - "memory.md#mem-rte-chat-continuation"
          note: "Thread identifies graph namespace, but that does not identify which opaque retained parts are automatically delivered to the model."
        -
          scope: "History automatic replay selector"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-history-offload"
            - "memory.md#mem-obj-conversation-history"
          note: "Mount prefix is an access mapping, not an established selector for delivered history parts; production trigger/input/budget are unresolved."
        -
          scope: "Requested search, explicit section/Claim/raw reads and visualization builds"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-wiki-retrieval"
            - "memory.md#mem-rte-claims-reconciliation"
            - "runtime.md#rt-rte-personal-ingestion"
            - "memory.md#mem-rte-visualizer-delivery"
          note: "These local units fulfill requests rather than push; lexical ranking of a requested search does not establish inferred-lexical push."
        -
          scope: "Residual connector and evaluator push alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-connector-data"
            - "memory.md#mem-rte-ledger-evaluation"
          note: "Source-specific routes and full evaluator selection were not inventoried in accepted records."
      records:
        - "runtime.md#rt-obj-page-guidance"
        - "runtime.md#rt-rte-native-generation"
        - "runtime.md#rt-rte-host-generation"
        - "memory.md#mem-rte-claims-reconciliation"
        - "epistemic.md#epi-rte-evidence-preflight"
        - "runtime.md#rt-obj-repository-run-state"
        - "memory.md#mem-obj-page-manifest"
        - "memory.md#mem-rte-ledger-evaluation"
        - "epistemic.md#epi-rte-ledger-reporting"
        - "memory.md#mem-rte-evaluation-transfer"
        - "memory.md#mem-obj-chat-checkpoint"
        - "memory.md#mem-rte-chat-continuation"
        - "memory.md#mem-rte-history-offload"
        - "memory.md#mem-obj-conversation-history"
        - "runtime.md#rt-rte-wiki-retrieval"
        - "runtime.md#rt-rte-personal-ingestion"
        - "memory.md#mem-rte-visualizer-delivery"
        - "memory.md#mem-obj-connector-data"
      note: "Signals classify automatic push operations, not lexical ranking of requested search results. Assignment identity and issue filtering are distinct from coarse availability and opaque continuation/history selection."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "LangSmith operational traces to durable runtime documentation and later agents"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-documentation"
                - "memory.md#mem-obj-trace"
                - "memory.md#mem-obj-wiki-page"
                - "runtime.md#rt-rte-wiki-retrieval"
              note: "Automatic trace-fed authoring produces retained behavior-shaping documents available to later requested wiki context. Architectural qualification does not require observed improvement."
          records:
            - "memory.md#mem-rte-trace-documentation"
            - "memory.md#mem-obj-trace"
            - "memory.md#mem-obj-wiki-page"
            - "runtime.md#rt-rte-wiki-retrieval"
          note: "Automatic trace-fed authoring produces retained behavior-shaping documents available to later requested wiki context. Architectural qualification does not require observed improvement."
        -
          scope: "Checkpoint and native history raw-to-derived-to-later-model alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-chat-continuation"
            - "memory.md#mem-obj-chat-checkpoint"
            - "memory.md#mem-rte-history-offload"
            - "memory.md#mem-obj-conversation-history"
          note: "Recorded graph persistence and intended summarization do not resolve an automatic durable summary production/consumption chain; raw storage alone is insufficient."
        -
          scope: "Personal connector trace-like source updates"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-connector-data"
            - "runtime.md#rt-rte-personal-ingestion"
          note: "Individual source contents/transforms were not inspected, preventing classification of session/event-fed derived documentation routes."
        -
          scope: "LEDGER automatic assessment retention and later evaluator reuse"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-rte-ledger-judgment"
            - "epistemic.md#epi-rte-ledger-reporting"
            - "memory.md#mem-rte-ledger-evaluation"
          note: "Verdicts/cache/carry are consequential evaluation state, but accepted records do not establish a qualifying trace-fed behavior-shaping update; no score-to-product revision gate is wired in the inspected runner."
        -
          scope: "Nontrace repository authoring, metadata, queue, translation and transfer operations"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-native-generation"
            - "runtime.md#rt-obj-repository-run-state"
            - "memory.md#mem-obj-page-manifest"
            - "memory.md#mem-rte-claims-reconciliation"
            - "runtime.md#rt-rte-page-translation"
            - "memory.md#mem-rte-evaluation-transfer"
          note: "These bounded ordinary operations are not a qualifying trace-fed update merely because code executes them. The separately scoped trace-documentation branch remains included."
      records:
        - "memory.md#mem-rte-trace-documentation"
        - "memory.md#mem-obj-trace"
        - "memory.md#mem-obj-wiki-page"
        - "runtime.md#rt-rte-wiki-retrieval"
        - "memory.md#mem-rte-chat-continuation"
        - "memory.md#mem-obj-chat-checkpoint"
        - "memory.md#mem-rte-history-offload"
        - "memory.md#mem-obj-conversation-history"
        - "memory.md#mem-obj-connector-data"
        - "runtime.md#rt-rte-personal-ingestion"
        - "epistemic.md#epi-rte-ledger-judgment"
        - "epistemic.md#epi-rte-ledger-reporting"
        - "memory.md#mem-rte-ledger-evaluation"
        - "runtime.md#rt-rte-native-generation"
        - "runtime.md#rt-obj-repository-run-state"
        - "memory.md#mem-obj-page-manifest"
        - "memory.md#mem-rte-claims-reconciliation"
        - "runtime.md#rt-rte-page-translation"
        - "memory.md#mem-rte-evaluation-transfer"
      note: "The external operational-trace to retained documentation to later context chain supports a wired positive without improved-capacity evidence. Opaque state/offload and personal-source alternatives prevent a complete yes/no inventory; no system-wide negative is asserted."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "LangSmith trace-documentation original execution feedback"
          assessment: "known"
          findings:
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trace"
                - "memory.md#mem-rte-trace-documentation"
              note: "Ordered external root/descendant execution records, tool-set/run-shape evidence and truncated errors feed documentation. Inputs/outputs are not fetched; this does not establish session-logs or state-action-outcome trajectories from the trace label alone."
          records:
            - "memory.md#mem-obj-trace"
            - "memory.md#mem-rte-trace-documentation"
          note: "Ordered external root/descendant execution records, tool-set/run-shape evidence and truncated errors feed documentation. Inputs/outputs are not fetched; this does not establish session-logs or state-action-outcome trajectories from the trace label alone."
        -
          scope: "Additional original-content categories within compact operational samples"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-trace"
            - "memory.md#mem-rte-trace-documentation"
          note: "Records describe metrics, structure and errors but do not conclusively establish separate environmental event streams or linked state-action-outcome experience. No extra category is inferred from serialization or ordering."
        -
          scope: "Checkpoint/history qualifying alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-chat-checkpoint"
            - "memory.md#mem-rte-chat-continuation"
            - "memory.md#mem-obj-conversation-history"
            - "memory.md#mem-rte-history-offload"
          note: "Actual retained raw turns, tool results or dependency-derived summaries and their qualifying update consumers are unresolved."
        -
          scope: "Source-specific personal trace-fed alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-connector-data"
            - "runtime.md#rt-rte-personal-ingestion"
          note: "Individual conversational/event sources and downstream transforms were not inspected; imported source text alone cannot establish trace origin."
        -
          scope: "LEDGER possible qualifying trace origin"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-ledger-evaluation"
            - "epistemic.md#epi-rte-ledger-judgment"
            - "epistemic.md#epi-rte-ledger-reporting"
          note: "The recorded benchmark assessment inputs do not settle a qualifying trace-fed write, so its trace source is not declared inapplicable."
        -
          scope: "Nontrace authoring/control/translation/transfer operations"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-native-generation"
            - "runtime.md#rt-obj-repository-run-state"
            - "memory.md#mem-obj-page-manifest"
            - "memory.md#mem-rte-claims-reconciliation"
            - "runtime.md#rt-rte-page-translation"
            - "memory.md#mem-rte-evaluation-transfer"
          note: "Outside the separate qualifying or unresolved trace-fed branches, these operations supply no qualifying write whose trace source needs a positive category."
      records:
        - "memory.md#mem-obj-trace"
        - "memory.md#mem-rte-trace-documentation"
        - "memory.md#mem-obj-chat-checkpoint"
        - "memory.md#mem-rte-chat-continuation"
        - "memory.md#mem-obj-conversation-history"
        - "memory.md#mem-rte-history-offload"
        - "memory.md#mem-obj-connector-data"
        - "runtime.md#rt-rte-personal-ingestion"
        - "memory.md#mem-rte-ledger-evaluation"
        - "epistemic.md#epi-rte-ledger-judgment"
        - "epistemic.md#epi-rte-ledger-reporting"
        - "runtime.md#rt-rte-native-generation"
        - "runtime.md#rt-obj-repository-run-state"
        - "memory.md#mem-obj-page-manifest"
        - "memory.md#mem-rte-claims-reconciliation"
        - "runtime.md#rt-rte-page-translation"
        - "memory.md#mem-rte-evaluation-transfer"
      note: "Original operational execution feedback supports tool-traces on the qualifying documentation route. Opaque continuation/history and source-specific personal routes remain unresolved, so one positive cannot make the whole axis inapplicable."
---

# OpenWiki memory profile

## Comparison rationale

The comparison covers accumulated memory and later consumers, not all runtime storage. [MEM-OBJ-wiki-page](memory.md#mem-obj-wiki-page) is the canonical page object: reconciliation supersedes EPI-OBJ-wiki-markdown with it. No other identity amendment changes a value. The mixed epistemic Claim container remains valid alongside [MEM-OBJ-claim](memory.md#mem-obj-claim), [MEM-OBJ-evidence](memory.md#mem-obj-evidence) and [MEM-OBJ-page-claims](memory.md#mem-obj-page-claims); its existence does not justify combining their forms or authorities.

Positive findings retain source-level wiring or the separately afforded middleware admission contract. Requested semantic curation behavior is not an emitted operation. None is observed or causally supported. [RT-RTE-native-generation](runtime.md#rt-rte-native-generation) supplies automatic local admission without per-page approval. [RT-RTE-host-generation](runtime.md#rt-rte-host-generation) leaves human control unresolved. [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission) separates local retention from Git merge: an automatically created PR does not establish manual merging. Optional Git retention is not a substitute for the operative filesystem classification.

The same retained page can supply knowledge to a host and ranking features to the lexical selector. [RT-RTE-wiki-retrieval](runtime.md#rt-rte-wiki-retrieval), with its memory annotation, establishes both, plus search-only deprecated suppression. Requested search remains pull; BM25 does not become a push signal. Conversely, retained [RT-OBJ-page-guidance](runtime.md#rt-obj-page-guidance) supplies instructions at a new worker, and [MEM-RTE-claims-reconciliation](memory.md#mem-rte-claims-reconciliation) supplies automatically selected issue Claims. Those assignment operations have identity and issue-status selection, independently of explicitly requested full Claim inspection.

Curation follows transformations. [EPI-RTE-source-projection](epistemic.md#epi-rte-source-projection) reduces precise resources to file-level provenance and deduplicates it. [RT-RTE-page-translation](runtime.md#rt-rte-page-translation) revises retained pages but does not establish faithful semantics. [MEM-RTE-chat-continuation](memory.md#mem-rte-chat-continuation) deletes older database rows, not necessarily older turns in surviving state. Guidance on [MEM-RTE-trace-documentation](memory.md#mem-rte-trace-documentation) requests patterns, supported implications and incremental refinement, but does not establish creation of a claim absent from its inputs or an implemented revision of existing documentation. These two units retain no positive curation findings; no synthesize value is supported, and evolve remains supported only on the independent Claim-revision and translation routes. The separately wired trace-fed document-write/later-context chain still qualifies for trace_learning, without implying improved capacity, theory criticism or self-improvement.

[MEM-OBJ-conversation-history](memory.md#mem-obj-conversation-history) and [MEM-RTE-history-offload](memory.md#mem-rte-history-offload) establish a durable file channel independently of opaque SQLite graph payloads. Fresh worker graphs and page/Claim snapshot restoration do not erase that channel. The unexecuted test's readable text does not resolve deployed payload form, automatic trace-summary production, reload selection, reasons or cross-worker consumption. Those included alternatives therefore remain unresolved on the relevant axes; one known document chain cannot classify them by analogy.

Benchmark state is a later-consumer surface, not a production revision oracle. [EPI-OBJ-ledger-verdicts](epistemic.md#epi-obj-ledger-verdicts), [EPI-RTE-ledger-judgment](epistemic.md#epi-rte-ledger-judgment) and [EPI-RTE-ledger-reporting](epistemic.md#epi-rte-ledger-reporting) support interpreted judgments, fixed reporting and continuing evaluation scope. [MEM-RTE-ledger-evaluation](memory.md#mem-rte-ledger-evaluation) supplies continuing artifact/carry wiring but leaves optional persistence and detailed evaluator alternatives incomplete. [MEM-RTE-evaluation-transfer](memory.md#mem-rte-evaluation-transfer) supports cache-selected copying before a later host invocation, not observed host reliance or automatic prompt injection of every copied page.

No axis uses an unsupported complete-system absence. Static managed host guidance and shipped skills are excluded because they are not accumulated or changed through use, as distinguished by [RT-BAP-managed-guidance](runtime.md#rt-bap-managed-guidance) and the memory account. Native provider parameters are not an inspected use-derived memory update; [RT-CMP-chat-model](runtime.md#rt-cmp-chat-model) leaves provider-side mutability uninspected. This exclusion does not claim that providers or external hosts have no memory.

Source-read log: no direct source reads. Classifications use only the supplied accepted records and their annotations; no additional evidence or records were added. Named uncertainty follows missing recorded facts, not missing execution alone.
