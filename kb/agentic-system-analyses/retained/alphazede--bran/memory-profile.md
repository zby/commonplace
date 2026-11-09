---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "BRAN memory comparison: repository evidence, query-use diagnostics, retained connected results, settings and unresolved storage alternatives at the frozen public revision."
run-id: "AAS-2026-11-08-bran-2be75f1c9e69-01"
source-identity: "https://github.com/alphazede/bran"
reviewed-boundary: "7bc428b2ccdfad38e05caa0c0cba2bb19041993a"
memory-comparison:
  version: 2
  scope: "Reusable repository files and documents, existing SCIP evidence, retained query request/access descriptors, CLI connected answers/support and opaque artifacts, effective project settings, admitted source replacements, and optional derived-file/state/custom-result-store alternatives. API-only alternatives retain their unknown later consumers. Excludes ephemeral scan/packet/projection/export/database-extraction buffers as retained memory, static shipped skill instructions, and external host/provider/compressor internals or index production; no opaque local payload is excluded merely because its consumer or meaning is unresolved."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Repository files, native documents and existing SCIP index"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-query-packet"
                - "memory.md#mem-rte-document-selection"
                - "memory.md#mem-rte-symbol-reload"
                - "runtime.md#rt-rte-maintain-apply"
              note: "Query, document and symbol routes reopen on-disk material, including source replacements admitted by maintenance."
          records:
            - "runtime.md#rt-rte-query-packet"
            - "memory.md#mem-rte-document-selection"
            - "memory.md#mem-rte-symbol-reload"
            - "runtime.md#rt-rte-maintain-apply"
          note: "All named source objects are read from repository files; index production and document fidelity do not change this substrate."
        -
          scope: "Recorded query request and access descriptors"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evidence-request"
                - "memory.md#mem-obj-evidence-rankings"
                - "memory.md#mem-rte-evidence-feedback"
              note: "Recording persists escaped requests and symbolic descriptors below .bran/cache/query-evidence."
          records:
            - "memory.md#mem-obj-evidence-request"
            - "memory.md#mem-obj-evidence-rankings"
            - "memory.md#mem-rte-evidence-feedback"
          note: "Both operative parts share the bounded local query-evidence file."
        -
          scope: "CLI connected InlineResult and opaque LosslessArtifact publication"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-result-answer"
                - "memory.md#mem-obj-result-support"
                - "runtime.md#rt-rte-connected-request"
                - "memory.md#mem-obj-lossless-artifact"
              note: "Content-addressed batches under .bran/results retain canonical inline output and separate artifacts."
          records:
            - "memory.md#mem-obj-result-answer"
            - "memory.md#mem-obj-result-support"
            - "runtime.md#rt-rte-connected-request"
            - "memory.md#mem-obj-lossless-artifact"
          note: "Opaque payload meaning does not make its CLI filesystem substrate unknown."
        -
          scope: "Effective project settings"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-settings-apply"
                - "runtime.md#rt-bap-settings-consumption"
              note: ".bran/settings.conf survives across invocations."
          records:
            - "runtime.md#rt-rte-settings-apply"
            - "runtime.md#rt-bap-settings-consumption"
          note: "Apply and later loading establish disk retention."
        -
          scope: "Optional derived-file publication"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-derived-rebuild"
                - "memory.md#mem-obj-derived-index"
                - "memory.md#mem-obj-derived-report"
              note: "Derived-only rebuild can publish a classified target through the supplied repair coordinator; production callers remain unresolved."
          records:
            - "memory.md#mem-rte-derived-rebuild"
            - "memory.md#mem-obj-derived-index"
            - "memory.md#mem-obj-derived-report"
          note: "This unit is the file-publishing helper, not its temporary returned buffers."
        -
          scope: "Generic FileStateStore objects"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-file-state"
              note: "Namespace object files and staged publication implement the storage capability."
          records:
            - "memory.md#mem-obj-file-state"
          note: "The file-backed API substrate is inspected although later agent use is not established."
        -
          scope: "Custom AgentRuntime result-store implementation"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-runtime-port"
          note: "The port receives successful output, but its implementation and retention substrate are unspecified."
      records:
        - "runtime.md#rt-rte-query-packet"
        - "memory.md#mem-rte-document-selection"
        - "memory.md#mem-rte-symbol-reload"
        - "runtime.md#rt-rte-maintain-apply"
        - "memory.md#mem-obj-evidence-request"
        - "memory.md#mem-obj-evidence-rankings"
        - "memory.md#mem-rte-evidence-feedback"
        - "memory.md#mem-obj-result-answer"
        - "memory.md#mem-obj-result-support"
        - "runtime.md#rt-rte-connected-request"
        - "memory.md#mem-obj-lossless-artifact"
        - "runtime.md#rt-rte-settings-apply"
        - "runtime.md#rt-bap-settings-consumption"
        - "memory.md#mem-rte-derived-rebuild"
        - "memory.md#mem-obj-derived-index"
        - "memory.md#mem-obj-derived-report"
        - "memory.md#mem-obj-file-state"
        - "runtime.md#rt-rte-runtime-port"
      note: "The local filesystem inventory is supported; a caller-supplied result-store alternative prevents complete substrate coverage. Ephemeral packet, document-projection, database-extraction and export buffers are not classified as retained in-memory stores."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Repository prose and native-document text at evidence consumers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-context-packet"
                - "memory.md#mem-rte-document-selection"
              note: "Selected bodies and admitted text/excerpts supply interpreted assertions to the evidence consumer."
          records:
            - "runtime.md#rt-obj-context-packet"
            - "memory.md#mem-rte-document-selection"
          note: "This covers the text consumed as evidence, not arbitrary repository replacement bytes."
        -
          scope: "Repository access metadata and SCIP supplement at fixed selectors"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-query-packet"
                - "memory.md#mem-rte-symbol-reload"
              note: "Metadata and symbol IDs/spans/roles control deterministic selection or formatted navigation."
          records:
            - "runtime.md#rt-rte-query-packet"
            - "memory.md#mem-rte-symbol-reload"
          note: "Localized IDs, paths, freshness and ranking fields have fixed code consumers."
        -
          scope: "Retained query request at replay"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evidence-request"
                - "memory.md#mem-rte-evidence-feedback"
              note: "Replay reuses the retained request text."
          records:
            - "memory.md#mem-obj-evidence-request"
            - "memory.md#mem-rte-evidence-feedback"
          note: "The original request remains prose even though an escaped record encodes it."
        -
          scope: "Retained query access descriptors at gap/replay processors"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evidence-rankings"
                - "memory.md#mem-rte-evidence-feedback"
              note: "Fixed comparison and gap rules consume roots, terms, outcomes and ranking fields."
          records:
            - "memory.md#mem-obj-evidence-rankings"
            - "memory.md#mem-rte-evidence-feedback"
          note: "These are selection metadata, not copied document bodies."
        -
          scope: "Retained InlineResult answer and claim/support strings at get/readers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-result-answer"
                - "memory.md#mem-obj-result-support"
                - "runtime.md#rt-rte-connected-request"
              note: "get decodes and returns answer and claim/support text; actual subsequent model reliance remains unobserved."
          records:
            - "memory.md#mem-obj-result-answer"
            - "memory.md#mem-obj-result-support"
            - "runtime.md#rt-rte-connected-request"
          note: "Reader-facing prose is separate from mechanical source associations."
        -
          scope: "Retained InlineResult citation associations at get"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-result-support"
                - "runtime.md#rt-rte-connected-request"
              note: "Fixed decoding and JSON projection preserve source associations."
          records:
            - "memory.md#mem-obj-result-support"
            - "runtime.md#rt-rte-connected-request"
          note: "IDs, locators, digests and flags survive canonical decoding."
        -
          scope: "Settings at packet/connected setup"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-settings-apply"
                - "runtime.md#rt-bap-settings-consumption"
              note: "Consumers decode settings into SQZ and token-limit fields."
          records:
            - "runtime.md#rt-rte-settings-apply"
            - "runtime.md#rt-bap-settings-consumption"
          note: "The persisted text encodes typed executable configuration rather than model advice."
        -
          scope: "Derived index/cache hashes and snapshot/validator framing"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-derived-rebuild"
                - "memory.md#mem-obj-derived-index"
                - "memory.md#mem-obj-derived-snapshot"
                - "memory.md#mem-obj-generated-validator"
              note: "Deterministic keys, lengths and content identities have fixed encoding rules."
          records:
            - "memory.md#mem-rte-derived-rebuild"
            - "memory.md#mem-obj-derived-index"
            - "memory.md#mem-obj-derived-snapshot"
            - "memory.md#mem-obj-generated-validator"
          note: "Only localized framing and hash projections are classified here."
        -
          scope: "Opaque artifact/state payloads, arbitrary replacement bytes, snapshot/validator bodies and report values"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-lossless-artifact"
            - "memory.md#mem-obj-file-state"
            - "memory.md#mem-obj-derived-snapshot"
            - "memory.md#mem-obj-generated-validator"
            - "runtime.md#rt-rte-runtime-port"
            - "runtime.md#rt-rte-maintain-apply"
            - "memory.md#mem-obj-derived-report"
          note: "Byte containers and a readable truncated display do not establish the forms or semantic consumers of their arbitrary input payloads; custom-port representations are likewise unresolved."
      records:
        - "runtime.md#rt-obj-context-packet"
        - "memory.md#mem-rte-document-selection"
        - "runtime.md#rt-rte-query-packet"
        - "memory.md#mem-rte-symbol-reload"
        - "memory.md#mem-obj-evidence-request"
        - "memory.md#mem-rte-evidence-feedback"
        - "memory.md#mem-obj-evidence-rankings"
        - "memory.md#mem-obj-result-answer"
        - "memory.md#mem-obj-result-support"
        - "runtime.md#rt-rte-connected-request"
        - "runtime.md#rt-rte-settings-apply"
        - "runtime.md#rt-bap-settings-consumption"
        - "memory.md#mem-rte-derived-rebuild"
        - "memory.md#mem-obj-derived-index"
        - "memory.md#mem-obj-derived-snapshot"
        - "memory.md#mem-obj-generated-validator"
        - "memory.md#mem-obj-lossless-artifact"
        - "memory.md#mem-obj-file-state"
        - "runtime.md#rt-rte-runtime-port"
        - "runtime.md#rt-rte-maintain-apply"
        - "memory.md#mem-obj-derived-report"
      note: "The text and symbolic parts are classified separately. Opaque retained bytes and alternative port payloads prevent complete enumeration; numerical IDs and digests do not establish distributed-parametric memory."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Repository/document acquisition and existing SCIP consumption"
          assessment: "partial"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-query-packet"
                - "memory.md#mem-rte-document-selection"
                - "memory.md#mem-rte-symbol-reload"
                - "runtime.md#rt-rte-maintain-apply"
              note: "BRAN acquires existing repository bytes and an externally produced index rather than authoring them on read."
          records:
            - "runtime.md#rt-rte-query-packet"
            - "memory.md#mem-rte-document-selection"
            - "memory.md#mem-rte-symbol-reload"
            - "runtime.md#rt-rte-maintain-apply"
          note: "Import is established at BRAN's read boundary; initial authorship, per-file revision provenance and SCIP generation/version remain unresolved."
        -
          scope: "Recorded query request and invocation descriptors"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evidence-request"
                - "memory.md#mem-obj-evidence-rankings"
                - "memory.md#mem-rte-evidence-feedback"
              note: "A query use supplies the request and deterministic outcome/ranking descriptors retained for later diagnostics."
          records:
            - "memory.md#mem-obj-evidence-request"
            - "memory.md#mem-obj-evidence-rankings"
            - "memory.md#mem-rte-evidence-feedback"
          note: "The recording transformation's inputs and projection are specified; this is not a complete raw trace."
        -
          scope: "TUI effective settings"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-settings-apply"
                - "runtime.md#rt-bap-settings-consumption"
              note: "An operator edits and applies the draft."
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-settings-apply"
                - "runtime.md#rt-bap-settings-consumption"
              note: "Capability/policy resolution yields the effective configuration actually persisted."
          records:
            - "runtime.md#rt-rte-settings-apply"
            - "runtime.md#rt-bap-settings-consumption"
          note: "The explicit operator draft and software resolution are separately visible."
        -
          scope: "Derived index/cache, report and framed snapshot/validator outputs"
          assessment: "partial"
          findings:
            -
              value: "other-compiled"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-derived-rebuild"
                - "memory.md#mem-obj-derived-index"
                - "memory.md#mem-obj-derived-report"
                - "memory.md#mem-obj-derived-snapshot"
                - "memory.md#mem-obj-generated-validator"
              note: "Sort, hashing, framing and display truncation compute outputs from caller inputs, without evidence of a learned transformation."
          records:
            - "memory.md#mem-rte-derived-rebuild"
            - "memory.md#mem-obj-derived-index"
            - "memory.md#mem-obj-derived-report"
            - "memory.md#mem-obj-derived-snapshot"
            - "memory.md#mem-obj-generated-validator"
          note: "Deterministic projection is classified, but origin and semantic lineage of supplied keyed bytes remain unresolved."
        -
          scope: "Canonical retained InlineResult encoding"
          assessment: "partial"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-result-answer"
                - "memory.md#mem-obj-result-support"
                - "runtime.md#rt-rte-connected-request"
              note: "Accepted provider fields are serialized into a canonical retained inline product."
          records:
            - "memory.md#mem-obj-result-answer"
            - "memory.md#mem-obj-result-support"
            - "runtime.md#rt-rte-connected-request"
          note: "Canonical encoding is known; provider content's original derivation is not established by exact-support admission or model provenance."
        -
          scope: "LosslessArtifact content, generic state objects and caller-authored replacements"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-lossless-artifact"
            - "memory.md#mem-obj-file-state"
            - "memory.md#mem-obj-derived-snapshot"
            - "memory.md#mem-obj-generated-validator"
            - "runtime.md#rt-rte-runtime-port"
            - "runtime.md#rt-rte-maintain-apply"
          note: "Provider/caller identity and arbitrary bytes do not resolve original content provenance, trace extraction or the nature of authorship."
      records:
        - "runtime.md#rt-rte-query-packet"
        - "memory.md#mem-rte-document-selection"
        - "memory.md#mem-rte-symbol-reload"
        - "runtime.md#rt-rte-maintain-apply"
        - "memory.md#mem-obj-evidence-request"
        - "memory.md#mem-obj-evidence-rankings"
        - "memory.md#mem-rte-evidence-feedback"
        - "runtime.md#rt-rte-settings-apply"
        - "runtime.md#rt-bap-settings-consumption"
        - "memory.md#mem-rte-derived-rebuild"
        - "memory.md#mem-obj-derived-index"
        - "memory.md#mem-obj-derived-report"
        - "memory.md#mem-obj-derived-snapshot"
        - "memory.md#mem-obj-generated-validator"
        - "memory.md#mem-obj-result-answer"
        - "memory.md#mem-obj-result-support"
        - "runtime.md#rt-rte-connected-request"
        - "memory.md#mem-obj-lossless-artifact"
        - "memory.md#mem-obj-file-state"
        - "runtime.md#rt-rte-runtime-port"
      note: "Known acquisition, query-use extraction and deterministic compilation coexist with unresolved initial and opaque-payload provenance. No parameter-training lineage is inferred from a model endpoint."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Repository evidence at outer-agent/provider evidence consumer"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-evidence-supply"
                - "runtime.md#rt-rte-connected-request"
              note: "Connected context supplies selected repository evidence to the provider."
            -
              value: "knowledge"
              basis: "afforded"
              records:
                - "runtime.md#rt-bap-evidence-supply"
              note: "The shipped skill names an outer-agent evidence consumer; deployed uptake is unobserved."
          records:
            - "runtime.md#rt-bap-evidence-supply"
            - "runtime.md#rt-rte-connected-request"
            - "memory.md#mem-rte-document-selection"
            - "memory.md#mem-rte-symbol-reload"
          note: "This is evidence supply, not guaranteed compliance or standing instructions."
        -
          scope: "Retained repository text/metadata at ranking code"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-query-packet"
                - "memory.md#mem-rte-document-selection"
              note: "Terms match paths, bodies and metadata or anchor text and affect relative source order."
          records:
            - "runtime.md#rt-rte-query-packet"
            - "memory.md#mem-rte-document-selection"
          note: "The retained source supplies ranking inputs even though the algorithm itself is fixed."
        -
          scope: "Repository source bytes at grounded completion validator"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-connected-request"
                - "epistemic.md#epi-obj-provider-claims"
              note: "Reopened source digests and support occurrence determine admissible claims."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-connected-request"
              note: "Failure of the grounded-source checks vetoes completion."
          records:
            - "runtime.md#rt-rte-connected-request"
            - "epistemic.md#epi-obj-provider-claims"
          note: "Current source bytes and identities constrain completion, not source truth."
        -
          scope: "Recorded query request at replay selector"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evidence-request"
                - "memory.md#mem-rte-evidence-feedback"
              note: "Replay resubmits stored request and root scope against current files."
          records:
            - "memory.md#mem-obj-evidence-request"
            - "memory.md#mem-rte-evidence-feedback"
          note: "The retained request selects the later evaluation input."
        -
          scope: "Retained query descriptors at diagnostic consumer"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evidence-rankings"
                - "memory.md#mem-rte-evidence-feedback"
                - "memory.md#mem-bap-diagnostic-supply"
              note: "Gap and replay processors use retained descriptors as evidence of past selection and emit advisory diagnostics."
          records:
            - "memory.md#mem-obj-evidence-rankings"
            - "memory.md#mem-rte-evidence-feedback"
            - "memory.md#mem-bap-diagnostic-supply"
          note: "Diagnostic evidence is not a rank-policy update or instruction adoption."
        -
          scope: "Retained answers/support at get evidence-return consumer"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-result-answer"
                - "memory.md#mem-obj-result-support"
                - "runtime.md#rt-rte-connected-request"
              note: "Decoded answer and claims/support become caller-visible reference content."
          records:
            - "memory.md#mem-obj-result-answer"
            - "memory.md#mem-obj-result-support"
            - "runtime.md#rt-rte-connected-request"
          note: "get supplies evidence products; no automatic next-prompt reuse is established."
        -
          scope: "Effective settings at invocation controls"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-settings-apply"
                - "runtime.md#rt-bap-settings-consumption"
              note: "Effective configuration selects compression and connected invocation paths."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-settings-apply"
                - "runtime.md#rt-bap-settings-consumption"
              note: "Retained token/budget configuration constrains later invocation context and execution requests."
          records:
            - "runtime.md#rt-rte-settings-apply"
            - "runtime.md#rt-bap-settings-consumption"
          note: "Classification follows the executable consumers, not the settings file's prose-like encoding."
        -
          scope: "Opaque artifacts, generic state/port payloads, derived output consumers and arbitrary replacements"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-lossless-artifact"
            - "memory.md#mem-obj-file-state"
            - "memory.md#mem-obj-derived-snapshot"
            - "memory.md#mem-obj-generated-validator"
            - "runtime.md#rt-rte-runtime-port"
            - "memory.md#mem-rte-derived-rebuild"
            - "memory.md#mem-obj-derived-index"
            - "memory.md#mem-obj-derived-report"
            - "runtime.md#rt-rte-maintain-apply"
          note: "Unknown payload semantics and missing later consumers prevent assigning learning, instruction, validation or other authority from names such as GeneratedValidator."
      records:
        - "runtime.md#rt-bap-evidence-supply"
        - "runtime.md#rt-rte-connected-request"
        - "memory.md#mem-rte-document-selection"
        - "memory.md#mem-rte-symbol-reload"
        - "runtime.md#rt-rte-query-packet"
        - "epistemic.md#epi-obj-provider-claims"
        - "memory.md#mem-obj-evidence-request"
        - "memory.md#mem-rte-evidence-feedback"
        - "memory.md#mem-obj-evidence-rankings"
        - "memory.md#mem-bap-diagnostic-supply"
        - "memory.md#mem-obj-result-answer"
        - "memory.md#mem-obj-result-support"
        - "runtime.md#rt-rte-settings-apply"
        - "runtime.md#rt-bap-settings-consumption"
        - "memory.md#mem-obj-lossless-artifact"
        - "memory.md#mem-obj-file-state"
        - "memory.md#mem-obj-derived-snapshot"
        - "memory.md#mem-obj-generated-validator"
        - "runtime.md#rt-rte-runtime-port"
        - "memory.md#mem-rte-derived-rebuild"
        - "memory.md#mem-obj-derived-index"
        - "memory.md#mem-obj-derived-report"
        - "runtime.md#rt-rte-maintain-apply"
      note: "Evidence, ranking, replay routing, source-check vetoes and configuration force are supported at distinct consumers. Opaque alternatives and unestablished later derived-state consumers prevent an exhaustive authority union."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Opt-in query recording"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evidence-request"
                - "memory.md#mem-obj-evidence-rankings"
                - "memory.md#mem-rte-evidence-feedback"
              note: "Software admits and persists bounded request/ranking projections without per-content human approval."
          records:
            - "memory.md#mem-obj-evidence-request"
            - "memory.md#mem-obj-evidence-rankings"
            - "memory.md#mem-rte-evidence-feedback"
          note: "Enabling a workflow is not a human decision approving each retained record."
        -
          scope: "Connected output and artifact admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-result-answer"
                - "memory.md#mem-obj-result-support"
                - "runtime.md#rt-rte-connected-request"
                - "memory.md#mem-obj-lossless-artifact"
              note: "Successful validation leads to software publication even when no-session is requested."
          records:
            - "memory.md#mem-obj-result-answer"
            - "memory.md#mem-obj-result-support"
            - "runtime.md#rt-rte-connected-request"
            - "memory.md#mem-obj-lossless-artifact"
          note: "Provider generation and runtime gates admit products without a required human approval step."
        -
          scope: "TUI settings Apply"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-settings-apply"
                - "runtime.md#rt-bap-settings-consumption"
              note: "The operator edits and approves effective retained configuration through Apply."
          records:
            - "runtime.md#rt-rte-settings-apply"
            - "runtime.md#rt-bap-settings-consumption"
          note: "The UI route explicitly makes the operator's draft/Apply choice consequential."
        -
          scope: "Derived-only rebuild helper"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-derived-rebuild"
              note: "Software computes the replacement and can construct derived-rebuild-auto authority; human review is not required by the helper."
          records:
            - "memory.md#mem-rte-derived-rebuild"
          note: "This is the helper's admission mechanism, not the separate fixture-gated CLI."
        -
          scope: "Initial repository/index content, lower-level settings writes, maintain replacements and generic state/port admissions"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-query-packet"
            - "memory.md#mem-rte-document-selection"
            - "memory.md#mem-rte-symbol-reload"
            - "runtime.md#rt-rte-maintain-apply"
            - "runtime.md#rt-rte-settings-apply"
            - "runtime.md#rt-bap-settings-consumption"
            - "memory.md#mem-obj-file-state"
            - "runtime.md#rt-rte-runtime-port"
          note: "Generic caller identity or asserted authority does not establish an explicit human content decision; initial file creation/approval and custom port control remain unresolved."
      records:
        - "memory.md#mem-obj-evidence-request"
        - "memory.md#mem-obj-evidence-rankings"
        - "memory.md#mem-rte-evidence-feedback"
        - "memory.md#mem-obj-result-answer"
        - "memory.md#mem-obj-result-support"
        - "runtime.md#rt-rte-connected-request"
        - "memory.md#mem-obj-lossless-artifact"
        - "runtime.md#rt-rte-settings-apply"
        - "runtime.md#rt-bap-settings-consumption"
        - "memory.md#mem-rte-derived-rebuild"
        - "runtime.md#rt-rte-query-packet"
        - "memory.md#mem-rte-document-selection"
        - "memory.md#mem-rte-symbol-reload"
        - "runtime.md#rt-rte-maintain-apply"
        - "memory.md#mem-obj-file-state"
        - "runtime.md#rt-rte-runtime-port"
      note: "Known automatic admission and operator Apply coexist with unresolved initial and generic-caller control. Physical file writing and a nonblank authority string are not independent evidence of manual admission."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Connected result-store age/capacity eviction"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-connected-request"
              note: "Age and capacity controls remove retained result batches."
          records:
            - "runtime.md#rt-rte-connected-request"
          note: "Memory's annotation supplies expiry/removal and oldest-batch eviction detail on this canonical route."
        -
          scope: "Same-identity query record replacement"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evidence-request"
                - "memory.md#mem-obj-evidence-rankings"
                - "memory.md#mem-rte-evidence-feedback"
              note: "A new record with the same request and ordered roots replaces the prior outcome/descriptors."
          records:
            - "memory.md#mem-obj-evidence-request"
            - "memory.md#mem-obj-evidence-rankings"
            - "memory.md#mem-rte-evidence-feedback"
          note: "This finding concerns replacing retained content, not primary-key deduplication."
        -
          scope: "Effective settings replacement and explicit source replacement"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-settings-apply"
                - "runtime.md#rt-bap-settings-consumption"
                - "runtime.md#rt-rte-maintain-apply"
              note: "Successful Apply replaces effective configuration; admitted maintenance replaces target source bytes."
          records:
            - "runtime.md#rt-rte-settings-apply"
            - "runtime.md#rt-bap-settings-consumption"
            - "runtime.md#rt-rte-maintain-apply"
          note: "These routes revise retained entries; semantic improvement is not implied."
        -
          scope: "Derived-only target replacement"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-derived-rebuild"
              note: "Successful rebuild can replace an existing derived target under coordinator validation."
          records:
            - "memory.md#mem-rte-derived-rebuild"
          note: "The implemented replacement is separated from arbitrary input semantics."
        -
          scope: "Opaque artifact/state/port lifecycle and semantic effects of arbitrary derived inputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-lossless-artifact"
            - "memory.md#mem-obj-file-state"
            - "memory.md#mem-obj-derived-snapshot"
            - "memory.md#mem-obj-generated-validator"
            - "runtime.md#rt-rte-runtime-port"
            - "memory.md#mem-rte-derived-rebuild"
            - "memory.md#mem-obj-derived-index"
            - "memory.md#mem-obj-derived-report"
          note: "Encoding, primary-key checks and report labels alone do not establish consolidation, synthesis, deduplication or a complete transformation inventory. Later consumers and input semantics remain unresolved."
      records:
        - "runtime.md#rt-rte-connected-request"
        - "memory.md#mem-obj-evidence-request"
        - "memory.md#mem-obj-evidence-rankings"
        - "memory.md#mem-rte-evidence-feedback"
        - "runtime.md#rt-rte-settings-apply"
        - "runtime.md#rt-bap-settings-consumption"
        - "runtime.md#rt-rte-maintain-apply"
        - "memory.md#mem-rte-derived-rebuild"
        - "memory.md#mem-obj-lossless-artifact"
        - "memory.md#mem-obj-file-state"
        - "memory.md#mem-obj-derived-snapshot"
        - "memory.md#mem-obj-generated-validator"
        - "runtime.md#rt-rte-runtime-port"
        - "memory.md#mem-obj-derived-index"
        - "memory.md#mem-obj-derived-report"
      note: "Supported replacement and eviction operations do not establish knowledge synthesis or trace learning. Explicit clear removes the query store, but is not classified as invalidate because retained history after withdrawal is not established."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Explicit repository/document/SCIP requests"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-query-packet"
                - "memory.md#mem-rte-document-selection"
                - "memory.md#mem-rte-symbol-reload"
                - "runtime.md#rt-rte-maintain-apply"
              note: "Query/packet and document/symbol reload reread requested repository evidence."
          records:
            - "runtime.md#rt-rte-query-packet"
            - "memory.md#mem-rte-document-selection"
            - "memory.md#mem-rte-symbol-reload"
            - "runtime.md#rt-rte-maintain-apply"
          note: "An explicit evidence request is fulfilled by selected return; delivery is not a second push."
        -
          scope: "Evidence summarize/propose/replay and retained result get"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-evidence-request"
                - "memory.md#mem-obj-evidence-rankings"
                - "memory.md#mem-rte-evidence-feedback"
                - "memory.md#mem-obj-result-answer"
                - "memory.md#mem-obj-result-support"
                - "runtime.md#rt-rte-connected-request"
              note: "Explicit evidence commands load query history; get loads the caller-specified InlineResult."
          records:
            - "memory.md#mem-obj-evidence-request"
            - "memory.md#mem-obj-evidence-rankings"
            - "memory.md#mem-rte-evidence-feedback"
            - "memory.md#mem-obj-result-answer"
            - "memory.md#mem-obj-result-support"
            - "runtime.md#rt-rte-connected-request"
          note: "These routes require a consumer request for the retained material."
        -
          scope: "Effective settings into subsequent invocation setup"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-settings-apply"
                - "runtime.md#rt-bap-settings-consumption"
              note: "Invocation setup automatically loads project settings into execution controls."
          records:
            - "runtime.md#rt-rte-settings-apply"
            - "runtime.md#rt-bap-settings-consumption"
          note: "The caller requests a packet/connected operation, not the retained settings content; setup supplies that configuration automatically."
        -
          scope: "Current retained source into grounded completion checks"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-connected-request"
              note: "Grounded completion reopens cited files and supplies them to digest/support checks."
          records:
            - "runtime.md#rt-rte-connected-request"
          note: "Validation automatically obtains source bytes after provider output; this is not an explicit user request to return those bytes."
        -
          scope: "Generic state store retrieval capability"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-file-state"
              note: "Caller-directed get provides named retained bytes."
          records:
            - "memory.md#mem-obj-file-state"
          note: "Only API capacity is classified, not a wired later agent invocation."
        -
          scope: "Opaque artifacts, custom result stores and derived-file later consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-lossless-artifact"
            - "runtime.md#rt-rte-runtime-port"
            - "memory.md#mem-rte-derived-rebuild"
            - "memory.md#mem-obj-derived-index"
            - "memory.md#mem-obj-derived-report"
            - "memory.md#mem-obj-derived-snapshot"
            - "memory.md#mem-obj-generated-validator"
          note: "Immediate post-publication integrity read-back is not a later invocation; missing consumer/integration facts prevent classifying additional later routes."
      records:
        - "runtime.md#rt-rte-query-packet"
        - "memory.md#mem-rte-document-selection"
        - "memory.md#mem-rte-symbol-reload"
        - "runtime.md#rt-rte-maintain-apply"
        - "memory.md#mem-obj-evidence-request"
        - "memory.md#mem-obj-evidence-rankings"
        - "memory.md#mem-rte-evidence-feedback"
        - "memory.md#mem-obj-result-answer"
        - "memory.md#mem-obj-result-support"
        - "runtime.md#rt-rte-connected-request"
        - "runtime.md#rt-rte-settings-apply"
        - "runtime.md#rt-bap-settings-consumption"
        - "memory.md#mem-obj-file-state"
        - "memory.md#mem-obj-lossless-artifact"
        - "runtime.md#rt-rte-runtime-port"
        - "memory.md#mem-rte-derived-rebuild"
        - "memory.md#mem-obj-derived-index"
        - "memory.md#mem-obj-derived-report"
        - "memory.md#mem-obj-derived-snapshot"
        - "memory.md#mem-obj-generated-validator"
      note: "Supported explicit pulls and automatic configuration/validation supply coexist. Missing later consumers for included storage alternatives prevent a complete direction inventory."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Settings push on packet/connected setup"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-settings-apply"
                - "runtime.md#rt-bap-settings-consumption"
              note: "Setup loads available valid project settings wholesale; no content-targeted identity or semantic relevance match is recorded."
          records:
            - "runtime.md#rt-rte-settings-apply"
            - "runtime.md#rt-bap-settings-consumption"
          note: "Trigger: invocation setup. Input: current project root and fixed settings location. Selected part: effective project configuration."
        -
          scope: "Grounded completion source-check push"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-connected-request"
              note: "Cited source locators select files reopened for digest and exact-support checks; this is an actual file identity match."
          records:
            - "runtime.md#rt-rte-connected-request"
          note: "Trigger: provider result validation. Inputs: admitted citation locators and digests. Selected part: the uniquely cited retained source files."
        -
          scope: "Explicit query/history/get and generic state get pull chains"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-query-packet"
            - "memory.md#mem-rte-document-selection"
            - "memory.md#mem-rte-symbol-reload"
            - "runtime.md#rt-rte-maintain-apply"
            - "memory.md#mem-obj-evidence-request"
            - "memory.md#mem-obj-evidence-rankings"
            - "memory.md#mem-rte-evidence-feedback"
            - "memory.md#mem-obj-result-answer"
            - "memory.md#mem-obj-result-support"
            - "runtime.md#rt-rte-connected-request"
            - "memory.md#mem-obj-file-state"
          note: "Signal classifies push selection, not lexical selection inside a requested query or identity lookup on requested get."
        -
          scope: "Unresolved artifact, custom-port and derived-state later delivery"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-lossless-artifact"
            - "memory.md#mem-obj-file-state"
            - "memory.md#mem-obj-derived-snapshot"
            - "memory.md#mem-obj-generated-validator"
            - "runtime.md#rt-rte-runtime-port"
            - "memory.md#mem-rte-derived-rebuild"
            - "memory.md#mem-obj-derived-index"
            - "memory.md#mem-obj-derived-report"
          note: "No concrete later consumer/selector is established. A pull witness elsewhere cannot make these alternatives inapplicable."
      records:
        - "runtime.md#rt-rte-settings-apply"
        - "runtime.md#rt-bap-settings-consumption"
        - "runtime.md#rt-rte-connected-request"
        - "runtime.md#rt-rte-query-packet"
        - "memory.md#mem-rte-document-selection"
        - "memory.md#mem-rte-symbol-reload"
        - "runtime.md#rt-rte-maintain-apply"
        - "memory.md#mem-obj-evidence-request"
        - "memory.md#mem-obj-evidence-rankings"
        - "memory.md#mem-rte-evidence-feedback"
        - "memory.md#mem-obj-result-answer"
        - "memory.md#mem-obj-result-support"
        - "memory.md#mem-obj-file-state"
        - "memory.md#mem-obj-lossless-artifact"
        - "memory.md#mem-obj-derived-snapshot"
        - "memory.md#mem-obj-generated-validator"
        - "runtime.md#rt-rte-runtime-port"
        - "memory.md#mem-rte-derived-rebuild"
        - "memory.md#mem-obj-derived-index"
        - "memory.md#mem-obj-derived-report"
      note: "Coarse settings availability and citation-identity validation are different push selectors. Lexical query scoring remains on a requested pull route and is not counted as inferred-lexical push."
    trace_learning:
      assessment: "not-determinable"
      units:
        -
          scope: "Query-use record to later gap/proposal/replay diagnostics"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-evidence-request"
            - "memory.md#mem-obj-evidence-rankings"
            - "memory.md#mem-rte-evidence-feedback"
          note: "Automatic recording and later diagnostics are established, but no recorded durable behavior-shaping revision/adoption chain or evidenced-absence record warrants a controlled yes or no."
        -
          scope: "Connected answers/support and opaque artifacts"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-result-answer"
            - "memory.md#mem-obj-result-support"
            - "runtime.md#rt-rte-connected-request"
            - "memory.md#mem-obj-lossless-artifact"
          note: "Retention/get is not a demonstrated automatic trace-fed behavior-shaping update; artifact input semantics and later consumers remain unresolved. No bounded absence record establishes no."
        -
          scope: "Settings/source changes, derived rebuild and generic state/port alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-settings-apply"
            - "runtime.md#rt-bap-settings-consumption"
            - "runtime.md#rt-rte-query-packet"
            - "memory.md#mem-rte-document-selection"
            - "memory.md#mem-rte-symbol-reload"
            - "runtime.md#rt-rte-maintain-apply"
            - "memory.md#mem-rte-derived-rebuild"
            - "memory.md#mem-obj-derived-index"
            - "memory.md#mem-obj-derived-report"
            - "memory.md#mem-obj-lossless-artifact"
            - "memory.md#mem-obj-file-state"
            - "memory.md#mem-obj-derived-snapshot"
            - "memory.md#mem-obj-generated-validator"
            - "runtime.md#rt-rte-runtime-port"
          note: "Settings and source publication do not identify a qualifying trace-fed update; generic inputs and later consumers remain unresolved. No evidenced absence warrants local no."
      records:
        - "memory.md#mem-obj-evidence-request"
        - "memory.md#mem-obj-evidence-rankings"
        - "memory.md#mem-rte-evidence-feedback"
        - "memory.md#mem-obj-result-answer"
        - "memory.md#mem-obj-result-support"
        - "runtime.md#rt-rte-connected-request"
        - "memory.md#mem-obj-lossless-artifact"
        - "runtime.md#rt-rte-settings-apply"
        - "runtime.md#rt-bap-settings-consumption"
        - "runtime.md#rt-rte-query-packet"
        - "memory.md#mem-rte-document-selection"
        - "memory.md#mem-rte-symbol-reload"
        - "runtime.md#rt-rte-maintain-apply"
        - "memory.md#mem-rte-derived-rebuild"
        - "memory.md#mem-obj-derived-index"
        - "memory.md#mem-obj-derived-report"
        - "memory.md#mem-obj-file-state"
        - "memory.md#mem-obj-derived-snapshot"
        - "memory.md#mem-obj-generated-validator"
        - "runtime.md#rt-rte-runtime-port"
      note: "No accepted record establishes a qualifying trace-fed durable update and later behavior-shaping consumer, and no member declares an evidenced-absence record. Thus neither yes nor no is assigned; this is not a whole-system absence claim."
    trace_source:
      assessment: "not-determinable"
      units:
        -
          scope: "Recorded query diagnostics"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-evidence-request"
            - "memory.md#mem-obj-evidence-rankings"
            - "memory.md#mem-rte-evidence-feedback"
          note: "Query-use origin is recorded, but a qualifying learning write is not established. Trace lineage alone does not assign a learning-source value."
        -
          scope: "Connected retained products and opaque artifacts"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-result-answer"
            - "memory.md#mem-obj-result-support"
            - "runtime.md#rt-rte-connected-request"
            - "memory.md#mem-obj-lossless-artifact"
          note: "Repository-grounded input is not automatically a session log or tool trace; opaque artifact derivation and qualifying learning consumer are unresolved."
        -
          scope: "Settings/replacements, derived rebuild and generic state/port alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-settings-apply"
            - "runtime.md#rt-bap-settings-consumption"
            - "runtime.md#rt-rte-query-packet"
            - "memory.md#mem-rte-document-selection"
            - "memory.md#mem-rte-symbol-reload"
            - "runtime.md#rt-rte-maintain-apply"
            - "memory.md#mem-rte-derived-rebuild"
            - "memory.md#mem-obj-derived-index"
            - "memory.md#mem-obj-derived-report"
            - "memory.md#mem-obj-lossless-artifact"
            - "memory.md#mem-obj-file-state"
            - "memory.md#mem-obj-derived-snapshot"
            - "memory.md#mem-obj-generated-validator"
            - "runtime.md#rt-rte-runtime-port"
          note: "Original inputs to a qualifying automatic trace-fed update are not identified. Caller bytes and GeneratedValidator labels establish none of the four controlled sources."
      records:
        - "memory.md#mem-obj-evidence-request"
        - "memory.md#mem-obj-evidence-rankings"
        - "memory.md#mem-rte-evidence-feedback"
        - "memory.md#mem-obj-result-answer"
        - "memory.md#mem-obj-result-support"
        - "runtime.md#rt-rte-connected-request"
        - "memory.md#mem-obj-lossless-artifact"
        - "runtime.md#rt-rte-settings-apply"
        - "runtime.md#rt-bap-settings-consumption"
        - "runtime.md#rt-rte-query-packet"
        - "memory.md#mem-rte-document-selection"
        - "memory.md#mem-rte-symbol-reload"
        - "runtime.md#rt-rte-maintain-apply"
        - "memory.md#mem-rte-derived-rebuild"
        - "memory.md#mem-obj-derived-index"
        - "memory.md#mem-obj-derived-report"
        - "memory.md#mem-obj-file-state"
        - "memory.md#mem-obj-derived-snapshot"
        - "memory.md#mem-obj-generated-validator"
        - "runtime.md#rt-rte-runtime-port"
      note: "Learning-source applicability is unresolved rather than absent: neither a qualifying route nor a bounded complete absence of trace learning is established. Static files and symbolic event-like encodings are not reclassified as experience sources."
---

# BRAN memory profile

## Comparison rationale

The comparison follows operative retained parts and their actual consumers, not the runtime's complete storage surface. Repository evidence, query-use history, local results and settings have different write and read routes. Optional file-state, custom-result-store and derived-file APIs remain visible with capability-level findings or unresolved units; they are not silently promoted to integrated agent memory. Immediate database extraction and Obsidian export/reparse establish no retained later-consumer route, so their temporary buffers add neither an in-memory substrate nor learning findings. See [MEM-CMP-database-evidence](memory.md#mem-cmp-database-evidence), [MEM-CMP-obsidian-export](memory.md#mem-cmp-obsidian-export), [MEM-OBJ-file-state](memory.md#mem-obj-file-state) and [MEM-RTE-derived-rebuild](memory.md#mem-rte-derived-rebuild).

The supplied reconciliation establishes no duplicate supersession. All citations therefore retain their declaring members and canonical IDs. Document and SCIP routes refine the query/packet container; diagnostic summary/replay routes are downstream consumers within the broader feedback chain. Provider claim candidates and retained InlineResult support are different stages, not interchangeable object declarations. [MEM-RTE-document-selection](memory.md#mem-rte-document-selection), [MEM-RTE-symbol-reload](memory.md#mem-rte-symbol-reload), [MEM-RTE-evidence-feedback](memory.md#mem-rte-evidence-feedback), [EPI-RTE-evidence-summary](epistemic.md#epi-rte-evidence-summary), [EPI-RTE-evidence-replay](epistemic.md#epi-rte-evidence-replay), [EPI-OBJ-provider-claims](epistemic.md#epi-obj-provider-claims) and [MEM-OBJ-result-support](memory.md#mem-obj-result-support) keep those distinctions.

### Retention, form and provenance

Files are the supported retained substrate, including opaque result artifacts whose storage is known even though their meaning is not. The custom runtime store port remains unresolved. A versioned local record is still file storage; neither content-addressing nor numeric digests imply a vector store or parametric representation. [RT-RTE-runtime-port](runtime.md#rt-rte-runtime-port) does not identify a concrete alternative store.

Natural-language answers, request text and repository prose are split from symbolic access descriptors, source associations and executable settings. Snapshot/validator framing does not resolve enclosed bytes. The display report's truncation does not classify the raw snapshot or generated-validator payload. Deterministic canonical encoding supports other-compiled lineage only for that encoding step; it does not settle original provider derivation. Initial repository authorship and arbitrary caller payload origins remain unresolved. See [MEM-OBJ-derived-report](memory.md#mem-obj-derived-report), [MEM-OBJ-derived-snapshot](memory.md#mem-obj-derived-snapshot), [MEM-OBJ-generated-validator](memory.md#mem-obj-generated-validator) and [MEM-OBJ-lossless-artifact](memory.md#mem-obj-lossless-artifact).

### Authority and admission

Knowledge supply and ranking are separate consumers of repository material. At grounded completion, retained source bytes additionally supply validation criteria and an enforced veto, without becoming a truth oracle. Query history supplies diagnostic evidence and selects replay inputs; it does not automatically revise ranking policy. Settings route later invocations and constrain budgets through executable consumers. These effects do not establish standing natural-language instructions or learning authority for arbitrary stored bytes. [RT-RTE-query-packet](runtime.md#rt-rte-query-packet), [RT-RTE-connected-request](runtime.md#rt-rte-connected-request), [MEM-RTE-evidence-feedback](memory.md#mem-rte-evidence-feedback) and [RT-BAP-settings-consumption](runtime.md#rt-bap-settings-consumption) support the separate paths.

TUI Apply establishes manual admission for that UI route. Software query/result admission and the derived-only helper establish automatic mechanisms at their respective evidence layers. A generic caller and an asserted maintenance authority do not authenticate human review. Lower-level settings and initial content therefore retain uncertainty independently of the inspected TUI choice. The helper's afforded automatic authority does not override the CLI fixture gate. See [RT-RTE-settings-apply](runtime.md#rt-rte-settings-apply), [RT-RTE-maintain-apply](runtime.md#rt-rte-maintain-apply) and [MEM-RTE-derived-rebuild](memory.md#mem-rte-derived-rebuild).

Replacement supports evolve and result eviction supports decay. Exact identity collisions, canonical encoding and index rebuilding alone do not establish dedup or consolidation. Query clear is removal, not a demonstrated history-preserving invalidate operation. No controlled synthesis value is inferred from advisory proposals whose replacement and authority are null. See [MEM-RTE-evidence-feedback](memory.md#mem-rte-evidence-feedback) and the memory annotation on [RT-RTE-connected-request](runtime.md#rt-rte-connected-request).

### Read-back and learning limits

Explicit query/packet, history commands and get are pulls, including identity-targeted get. They do not become push merely because code delivers the response. Automatic settings loading is coarse push: setup selects the available project configuration without a content-relevance selector. Grounded completion separately selects cited files by locator for validation, an identifier-based automatic supply to its checker. Query's lexical ranking is not a push signal on a requested evidence return. Opaque artifact integrity read-back immediately after publication does not establish a later consumer invocation. These distinctions follow [RT-RTE-query-packet](runtime.md#rt-rte-query-packet), [RT-RTE-connected-request](runtime.md#rt-rte-connected-request), [RT-RTE-settings-apply](runtime.md#rt-rte-settings-apply) and [MEM-RTE-evidence-feedback](memory.md#mem-rte-evidence-feedback).

Trace-extracted query descriptors do not by themselves establish trace learning. The recorded chain ends in advisory diagnostics and replay rather than an established automatic durable behavior-shaping revision. Connected output retention likewise does not establish a trace-fed update, while arbitrary artifacts, derived inputs and custom ports leave provenance and later consumption unresolved. No supplied member declares an evidenced-absence record, so no local or system-wide trace-learning "no" is warranted. Trace source is not-determinable, not inapplicable; no bounded complete absence resolves its applicability. These limits preserve the positive retention and diagnostic mechanisms without asserting improved capacity or successful self-improvement. See [MEM-RTE-evidence-feedback](memory.md#mem-rte-evidence-feedback), [MEM-RTE-derived-rebuild](memory.md#mem-rte-derived-rebuild), [MEM-OBJ-lossless-artifact](memory.md#mem-obj-lossless-artifact) and [RT-RTE-runtime-port](runtime.md#rt-rte-runtime-port).

All positive findings retain wired or afforded evidence at the actual mechanism. No observed execution or causal support is supplied; a wired local route does not resolve an opaque alternative or demonstrate activation or benefit.

### Source-read log

No source checkout files were read. Classification used only the supplied accepted members and contracts; no named record ambiguity required direct source inspection.
