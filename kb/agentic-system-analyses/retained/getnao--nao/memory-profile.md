---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Memory profile of nao: user guidance, continuation checkpoints, retained diagnostic findings and evolving work/context artifacts at the frozen repository boundary."
run-id: "AAS-2026-10-14-nao-f9d36a4b7276-01"
source-identity: "https://github.com/getnao/nao"
reviewed-boundary: "0085625a8fd22e4f404b6a3971d153f6b6699479"
memory-comparison:
  version: 2
  scope: "Retained objects accumulated or changed through use: user-memory content and access controls; conversation/history, compaction summaries and markers; saved files/stories and query evidence caches; usage-derived recommendations, dismissal/status state and proposed edits; changed/imported project context and its later guidance routes; saved evaluation reports with unresolved later consumption. Includes unresolved fork, dynamic-skill, channel, app-state, file-producer/lifecycle, context-provider, feedback and opaque provider-memory alternatives. Excludes unchanged shipped static instructions, initial pretrained weights, ordinary transient grants/credentials and external service internals as evidence. External accumulated provider state remains an unresolved included alternative, not an inferred weight-update route."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "User-memory rows, including content and access/lineage metadata"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memories"
              note: "SQLite memory-table schema and memory queries establish this retained-row implementation."
            -
              value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memories"
              note: "PostgreSQL memory-table schema establishes the relational alternative."
          records:
            - "memory.md#mem-obj-memories"
          note: "Both supported DB implementations store the same scoped row parts; this is a configured alternative, not evidence that both were deployed."
        -
          scope: "Conversation transcript and persisted streaming compaction marker"
          assessment: "known"
          findings:
            -
              value: "rdbms"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-web-chat"
                - "memory.md#mem-obj-compaction"
              note: "Application-DB messages hold transcript and compaction parts for continuation."
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-rte-chat-compaction"
          note: "Settled messages and successful streamed markers persist in the application DB; DB-engine details for these parts are not separately classified."
        -
          scope: "Compaction summary retained between model-step invocations"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction"
                - "memory.md#mem-rte-chat-compaction"
              note: "The retained summary replaces the working message prefix and reaches subsequent model steps."
          records:
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-rte-chat-compaction"
          note: "Working-array replacement establishes process retention, including generate without the streaming persistence channel."
        -
          scope: "Retained recommendations and reconciliation metadata"
          assessment: "known"
          findings:
            -
              value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-recommendation"
                - "epistemic.md#epi-rte-finding-reconciliation"
              note: "Application DB holds recommendations and retained administrative selection state."
          records:
            - "memory.md#mem-obj-context-recommendation"
            - "epistemic.md#epi-rte-finding-reconciliation"
          note: "The DB transaction stores diagnosis, edits, status and fingerprint parts."
        -
          scope: "Permanent saved-file payloads"
          assessment: "partial"
          findings:
            -
              value: "files"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-user-files"
                - "memory.md#mem-rte-saved-files"
              note: "A configured local provider affords retained files through scoped keys."
            -
              value: "service-object"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-user-files"
                - "memory.md#mem-rte-saved-files"
              note: "The configured S3 alternative affords retained service objects; no deployment is observed."
          records:
            - "memory.md#mem-obj-user-files"
            - "memory.md#mem-rte-saved-files"
          note: "Configured local and S3 alternatives are named, but each provider implementation and its durability are uninspected."
        -
          scope: "Changed project context and proposed patch branches"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "runtime.md#rt-bap-project-guidance"
              note: "Synchronization/refresh writes project files subsequently consumed by prompts and reads."
            -
              value: "repo"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-recommendation"
                - "runtime.md#rt-rte-context-delivery"
              note: "Proposed edits enter a Git branch/PR; context refresh also admits repository content."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "runtime.md#rt-rte-context-recommendation"
            - "runtime.md#rt-bap-project-guidance"
          note: "Live filesystem admission and separate disposable Git proposal branches are inspected; merge and deployment are not inferred."
        -
          scope: "Cached query-result evidence and retained tool-result parts"
          assessment: "partial"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-query-results"
                - "epistemic.md#epi-rte-query-results"
              note: "QueryResults map supports subsequent explicit paging."
            -
              value: "rdbms"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-query-results"
                - "runtime.md#rt-rte-web-chat"
              note: "Retained SQL tool-result parts participate in persisted chat replay."
          records:
            - "epistemic.md#epi-obj-query-results"
            - "epistemic.md#epi-rte-query-results"
            - "runtime.md#rt-rte-web-chat"
          note: "Process and transcript paths are classified; the direct-MCP cache substrate is not specified sufficiently in the accepted records."
        -
          scope: "Saved CLI evaluation reports"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-test-answer"
              note: "The workflow annotation on this record establishes report saving under test outputs."
          records:
            - "runtime.md#rt-rte-test-answer"
            - "epistemic.md#epi-rte-test-comparison"
          note: "Workflow inspection establishes timestamped JSON report files; later model consumption is not established."
        -
          scope: "Forked chat/history and copied checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-obj-compaction"
          note: "Fork producer and copied payload were located but not traced; Storage cannot be completed for alternative fork initialization."
        -
          scope: "Dynamic skill loading and channel-specific retained history/memory"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-explore-task"
            - "runtime.md#rt-bap-project-guidance"
            - "runtime.md#rt-rte-web-chat"
          note: "Dynamic load_skill and messaging-specific retention/consumption were not traced; standard web and explore witnesses do not cover these alternatives."
        -
          scope: "Story publication, retained app state and blob lifecycle"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-rte-saved-files"
          note: "Latest story replay is inspected, but publication, opaque app-state payload and cleanup chains are uninspected; a displayed story does not classify its app state."
        -
          scope: "Other saved-file byte producers and provider lifecycle"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-user-files"
            - "memory.md#mem-rte-saved-files"
          note: "Byte/from-disk APIs exist, but their producers, payload interpretation, admission and cleanup are uninspected; converted display text does not classify every stored binary."
        -
          scope: "Provider-specific CLI/API project-context admission"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "The dispatcher and Git delivery paths are inspected; provider outputs and API-upload admission are not fully traced. Changed project content is included, unchanged shipped instructions are excluded."
        -
          scope: "Recommendation feedback fallback and app-DB filtering"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-context-recommendation"
            - "runtime.md#rt-rte-context-recommendation"
            - "epistemic.md#epi-rte-finding-reconciliation"
          note: "Feedback fallback, coverage postprocessing and complete diagnostic query filtering are uninspected; the known reconciliation branch cannot complete this alternative."
        -
          scope: "Opaque external provider retention or adaptation"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-cmp-memory-extractor"
            - "runtime.md#rt-cmp-compaction-model"
            - "runtime.md#rt-cmp-agent-model"
          note: "Provider retention/training internals are outside the frozen evidence. No local parameter-update step is established. Any provider memory accumulated through use remains unresolved; static pretrained weights are not classified as accumulated memory."
      records:
        - "memory.md#mem-obj-memories"
        - "runtime.md#rt-rte-web-chat"
        - "memory.md#mem-obj-compaction"
        - "memory.md#mem-rte-chat-compaction"
        - "memory.md#mem-obj-context-recommendation"
        - "epistemic.md#epi-rte-finding-reconciliation"
        - "memory.md#mem-obj-user-files"
        - "memory.md#mem-rte-saved-files"
        - "runtime.md#rt-rte-context-delivery"
        - "runtime.md#rt-rte-context-recommendation"
        - "runtime.md#rt-bap-project-guidance"
        - "epistemic.md#epi-obj-query-results"
        - "epistemic.md#epi-rte-query-results"
        - "runtime.md#rt-rte-test-answer"
        - "epistemic.md#epi-rte-test-comparison"
        - "runtime.md#rt-rte-explore-task"
        - "memory.md#mem-cmp-memory-extractor"
        - "runtime.md#rt-cmp-compaction-model"
        - "runtime.md#rt-cmp-agent-model"
      note: "Positive retained-object substrates are supported locally. Opaque provider state, file-provider internals, MCP cache and the listed alternative producers prevent a complete substrate inventory; storage is not inferred from encoding."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "User-memory directive/profile content at extractor and analytics consumers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memories"
                - "memory.md#mem-bap-user-memory"
              note: "Profile statements supply context and global rules supply directions through model interpretation."
          records:
            - "memory.md#mem-obj-memories"
            - "memory.md#mem-bap-user-memory"
            - "epistemic.md#epi-obj-personal-fact"
            - "epistemic.md#epi-obj-global-rule"
          note: "The category/content projection is interpreted prose, distinct from row controls."
        -
          scope: "User-memory IDs, categories, timestamps and supersession controls"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memories"
                - "memory.md#mem-rte-memory-extraction"
              note: "Identifier membership and active-row selection use localized fields with code-defined effects."
          records:
            - "memory.md#mem-obj-memories"
            - "memory.md#mem-rte-memory-extraction"
          note: "IDs and active-state metadata have fixed query/filter consumers; not all stored metadata reaches analytics."
        -
          scope: "Compaction summary and checkpoint marker controls"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction"
                - "memory.md#mem-rte-chat-compaction"
              note: "The assistant summary is interpreted context for later model steps."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction"
                - "memory.md#mem-rte-chat-compaction"
              note: "Marker type and validity fields drive deterministic reconstruction."
          records:
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-rte-chat-compaction"
          note: "Split by consumed part: interpreted summary versus part type/nonempty validity and usage/status fields."
        -
          scope: "Recommendation prose delivered in later diagnostic summaries"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-recommendation"
                - "runtime.md#rt-rte-context-recommendation"
              note: "Diagnosis/title/guidance are interpreted prose; the later diagnostic prompt receives the title in a compact summary."
          records:
            - "memory.md#mem-obj-context-recommendation"
            - "runtime.md#rt-rte-context-recommendation"
          note: "Only the displayed title and compact fields are automatically resupplied, not the full stored rationale."
        -
          scope: "Recommendation administrative metadata and patch addressing"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-recommendation"
                - "epistemic.md#epi-rte-finding-reconciliation"
              note: "Code uses fingerprints/status/counts to determine retained actions and references."
          records:
            - "memory.md#mem-obj-context-recommendation"
            - "epistemic.md#epi-rte-finding-reconciliation"
          note: "Fingerprints, statuses, counts and paths have fixed reconciliation/selection consumers."
        -
          scope: "Proposed patch content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-context-recommendation"
            - "runtime.md#rt-rte-context-recommendation"
          note: "Structured paths are classified above, but accepted records do not classify the semantics of every patch payload."
        -
          scope: "Saved-file text and readable conversion path"
          assessment: "partial"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-user-files"
                - "memory.md#mem-rte-saved-files"
              note: "Model-authored text and readable text outputs supply interpreted content at the read tool."
          records:
            - "memory.md#mem-obj-user-files"
            - "memory.md#mem-rte-saved-files"
          note: "Authored text and its interpreted readable presentation are supported; opaque binary/data alternatives lack complete form classification."
        -
          scope: "Query tables, cache values and paging controls"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-query-results"
                - "epistemic.md#epi-rte-query-results"
              note: "Columns, rows, IDs and slice indices have fixed SQL/cache/paging consumers."
          records:
            - "epistemic.md#epi-obj-query-results"
            - "epistemic.md#epi-rte-query-results"
          note: "Tabular symbolic values remain distinct from unrestricted generated prose about their meaning."
        -
          scope: "Retained conversational prose and generated reports"
          assessment: "partial"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-web-chat"
                - "runtime.md#rt-rte-explore-task"
              note: "Stored conversational text and report-only task return enter later model context."
          records:
            - "runtime.md#rt-rte-web-chat"
            - "runtime.md#rt-rte-explore-task"
          note: "Natural-language turns and explore report text reach later history; arbitrary tool payload forms are not completely enumerated."
        -
          scope: "Changed project instructions and reference content at model consumers"
          assessment: "partial"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "runtime.md#rt-bap-project-guidance"
              note: "Delivered project rules and context text are interpreted as directions or reference content."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "runtime.md#rt-bap-project-guidance"
          note: "Known rule/skill prose is interpreted. Provider-specific context data and arbitrary override bodies remain incompletely classified."
        -
          scope: "Saved test report serialization"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-test-answer"
              note: "Saved report fields include structured actual/expected rows, tool calls and verdict data."
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-test-answer"
              note: "Saved answer text and human-readable details retain interpreted prose."
          records:
            - "runtime.md#rt-rte-test-answer"
            - "epistemic.md#epi-rte-test-comparison"
          note: "Structured JSON fields and answer prose are separate parts, neither establishes a later learning route."
        -
          scope: "Forked chat/history and copied checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-obj-compaction"
          note: "Fork producer and copied payload were located but not traced; Form cannot be completed for alternative fork initialization."
        -
          scope: "Dynamic skill loading and channel-specific retained history/memory"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-explore-task"
            - "runtime.md#rt-bap-project-guidance"
            - "runtime.md#rt-rte-web-chat"
          note: "Dynamic load_skill and messaging-specific retention/consumption were not traced; standard web and explore witnesses do not cover these alternatives."
        -
          scope: "Story publication, retained app state and blob lifecycle"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-rte-saved-files"
          note: "Latest story replay is inspected, but publication, opaque app-state payload and cleanup chains are uninspected; a displayed story does not classify its app state."
        -
          scope: "Other saved-file byte producers and provider lifecycle"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-user-files"
            - "memory.md#mem-rte-saved-files"
          note: "Byte/from-disk APIs exist, but their producers, payload interpretation, admission and cleanup are uninspected; converted display text does not classify every stored binary."
        -
          scope: "Provider-specific CLI/API project-context admission"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "The dispatcher and Git delivery paths are inspected; provider outputs and API-upload admission are not fully traced. Changed project content is included, unchanged shipped instructions are excluded."
        -
          scope: "Recommendation feedback fallback and app-DB filtering"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-context-recommendation"
            - "runtime.md#rt-rte-context-recommendation"
            - "epistemic.md#epi-rte-finding-reconciliation"
          note: "Feedback fallback, coverage postprocessing and complete diagnostic query filtering are uninspected; the known reconciliation branch cannot complete this alternative."
        -
          scope: "Opaque external provider retention or adaptation"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-cmp-memory-extractor"
            - "runtime.md#rt-cmp-compaction-model"
            - "runtime.md#rt-cmp-agent-model"
          note: "Provider retention/training internals are outside the frozen evidence. No local parameter-update step is established. Any provider memory accumulated through use remains unresolved; static pretrained weights are not classified as accumulated memory."
      records:
        - "memory.md#mem-obj-memories"
        - "memory.md#mem-bap-user-memory"
        - "epistemic.md#epi-obj-personal-fact"
        - "epistemic.md#epi-obj-global-rule"
        - "memory.md#mem-rte-memory-extraction"
        - "memory.md#mem-obj-compaction"
        - "memory.md#mem-rte-chat-compaction"
        - "memory.md#mem-obj-context-recommendation"
        - "runtime.md#rt-rte-context-recommendation"
        - "epistemic.md#epi-rte-finding-reconciliation"
        - "memory.md#mem-obj-user-files"
        - "memory.md#mem-rte-saved-files"
        - "epistemic.md#epi-obj-query-results"
        - "epistemic.md#epi-rte-query-results"
        - "runtime.md#rt-rte-web-chat"
        - "runtime.md#rt-rte-explore-task"
        - "runtime.md#rt-rte-context-delivery"
        - "runtime.md#rt-bap-project-guidance"
        - "runtime.md#rt-rte-test-answer"
        - "epistemic.md#epi-rte-test-comparison"
        - "memory.md#mem-cmp-memory-extractor"
        - "runtime.md#rt-cmp-compaction-model"
        - "runtime.md#rt-cmp-agent-model"
      note: "Mixed objects retain prose and symbolic parts separately. Opaque binaries, patches, provider memory and untraced consumers prevent a complete form inventory. Pretrained model form is not a positive memory finding."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Automatically extracted user-memory content"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-extraction"
              note: "The extractor derives standing content from recorded conversation text."
          records:
            - "memory.md#mem-obj-memories"
            - "memory.md#mem-rte-memory-extraction"
          note: "Recent recorded user/assistant text feeds derived facts/directives; this does not resolve all preexisting rows."
        -
          scope: "Explicitly edited user-memory content"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-maintenance"
              note: "The user mutation supplies replacement prose."
          records:
            - "memory.md#mem-rte-memory-maintenance"
            - "memory.md#mem-obj-memories"
          note: "Content supplied for a specific user edit has authored lineage independently of the row original producer."
        -
          scope: "Initial user-memory rows"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-memories"
          note: "Schema presence alone does not establish original provenance; known extraction and editing do not close this gap."
        -
          scope: "Compaction summaries"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction"
                - "memory.md#mem-rte-chat-compaction"
              note: "Recorded conversation/tool material is transformed into retained continuation text."
          records:
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-rte-chat-compaction"
          note: "Prepared conversation traces are image-stripped and budget-selected before summarization."
        -
          scope: "Context diagnoses and proposed edits"
          assessment: "partial"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-recommendation"
                - "runtime.md#rt-rte-context-recommendation"
              note: "Retained usage/feedback supplies the diagnostic derivation path; current project files are additional inputs, not proof that the resulting diagnosis was imported."
          records:
            - "memory.md#mem-obj-context-recommendation"
            - "runtime.md#rt-rte-context-recommendation"
            - "epistemic.md#epi-rte-finding-reconciliation"
          note: "Usage/feedback traces and current project files are mixed inputs; full fallback provenance is unresolved."
        -
          scope: "Retained uploads and model-authored file text"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-user-files"
                - "memory.md#mem-rte-saved-files"
              note: "User-chosen external bytes are admitted as uploads."
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-user-files"
                - "memory.md#mem-rte-saved-files"
              note: "Foreground model composes the text admitted by write; automatic agency does not change its authored origin."
          records:
            - "memory.md#mem-obj-user-files"
            - "memory.md#mem-rte-saved-files"
          note: "The identified upload and foreground-write branches are resolved; other byte/from-disk producers remain separate unknown alternatives."
        -
          scope: "Replayed transcript turns and explore report"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-web-chat"
                - "runtime.md#rt-rte-explore-task"
              note: "Recorded turns and child report text are directly authored conversation products."
          records:
            - "runtime.md#rt-rte-web-chat"
            - "runtime.md#rt-rte-explore-task"
          note: "Users and models author prose retained for continuation; raw retention alone is not extraction."
        -
          scope: "Query-result acquisition and presentation"
          assessment: "partial"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-query-results"
              note: "Warehouse rows enter retained query evidence through query adapters."
          records:
            - "epistemic.md#epi-obj-query-results"
            - "epistemic.md#epi-rte-query-results"
          note: "External data acquisition is known. Local derivation/semantic compilation provenance is not fully traced and does not warrant a general compiled-lineage positive."
        -
          scope: "Changed project files admitted by sync/Git"
          assessment: "partial"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
              note: "Repository/provider content is transferred into project context for later use."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "runtime.md#rt-bap-project-guidance"
          note: "The delivery/import path is known; remote initialization, authoring and provider derivation remain unresolved."
        -
          scope: "CLI report assembly"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-test-answer"
              note: "The CLI assembles structured evaluation outputs into a retained report."
          records:
            - "runtime.md#rt-rte-test-answer"
            - "epistemic.md#epi-rte-test-comparison"
          note: "A timestamped JSON report compiles run results and comparison details; it is not thereby learned guidance."
        -
          scope: "Forked chat/history and copied checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-obj-compaction"
          note: "Fork producer and copied payload were located but not traced; Lineage cannot be completed for alternative fork initialization."
        -
          scope: "Dynamic skill loading and channel-specific retained history/memory"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-explore-task"
            - "runtime.md#rt-bap-project-guidance"
            - "runtime.md#rt-rte-web-chat"
          note: "Dynamic load_skill and messaging-specific retention/consumption were not traced; standard web and explore witnesses do not cover these alternatives."
        -
          scope: "Story publication, retained app state and blob lifecycle"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-rte-saved-files"
          note: "Latest story replay is inspected, but publication, opaque app-state payload and cleanup chains are uninspected; a displayed story does not classify its app state."
        -
          scope: "Other saved-file byte producers and provider lifecycle"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-user-files"
            - "memory.md#mem-rte-saved-files"
          note: "Byte/from-disk APIs exist, but their producers, payload interpretation, admission and cleanup are uninspected; converted display text does not classify every stored binary."
        -
          scope: "Provider-specific CLI/API project-context admission"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "The dispatcher and Git delivery paths are inspected; provider outputs and API-upload admission are not fully traced. Changed project content is included, unchanged shipped instructions are excluded."
        -
          scope: "Recommendation feedback fallback and app-DB filtering"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-context-recommendation"
            - "runtime.md#rt-rte-context-recommendation"
            - "epistemic.md#epi-rte-finding-reconciliation"
          note: "Feedback fallback, coverage postprocessing and complete diagnostic query filtering are uninspected; the known reconciliation branch cannot complete this alternative."
        -
          scope: "Opaque external provider retention or adaptation"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-cmp-memory-extractor"
            - "runtime.md#rt-cmp-compaction-model"
            - "runtime.md#rt-cmp-agent-model"
          note: "Provider retention/training internals are outside the frozen evidence. No local parameter-update step is established. Any provider memory accumulated through use remains unresolved; static pretrained weights are not classified as accumulated memory."
      records:
        - "memory.md#mem-obj-memories"
        - "memory.md#mem-rte-memory-extraction"
        - "memory.md#mem-rte-memory-maintenance"
        - "memory.md#mem-obj-compaction"
        - "memory.md#mem-rte-chat-compaction"
        - "memory.md#mem-obj-context-recommendation"
        - "runtime.md#rt-rte-context-recommendation"
        - "epistemic.md#epi-rte-finding-reconciliation"
        - "memory.md#mem-obj-user-files"
        - "memory.md#mem-rte-saved-files"
        - "runtime.md#rt-rte-web-chat"
        - "runtime.md#rt-rte-explore-task"
        - "epistemic.md#epi-obj-query-results"
        - "epistemic.md#epi-rte-query-results"
        - "runtime.md#rt-rte-context-delivery"
        - "runtime.md#rt-bap-project-guidance"
        - "runtime.md#rt-rte-test-answer"
        - "epistemic.md#epi-rte-test-comparison"
        - "memory.md#mem-cmp-memory-extractor"
        - "runtime.md#rt-cmp-compaction-model"
        - "runtime.md#rt-cmp-agent-model"
      note: "Each derivation path keeps its own warrant. Initial rows, provider-generated context, query derivation and opaque alternatives prevent complete lineage coverage; model authorship is not manual admission."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Personal facts at default analytics prompt"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-bap-user-memory"
              note: "Profile prose supplies user context through system instructions."
          records:
            - "memory.md#mem-bap-user-memory"
            - "epistemic.md#epi-obj-personal-fact"
          note: "The model receives category/content as previously established but defeasible context, not evidence or IDs."
        -
          scope: "Global rules at default analytics prompt"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-bap-user-memory"
              note: "Retained global-rule prose supplies standing behavioral directions."
          records:
            - "memory.md#mem-bap-user-memory"
            - "epistemic.md#epi-obj-global-rule"
          note: "Directions have advisory model force; they do not bypass executable grants."
        -
          scope: "Active memories and conversation text at extraction update consumer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-extraction"
                - "memory.md#mem-obj-memories"
              note: "Retained experience/current guidance is consumed to revise durable user-memory content."
          records:
            - "memory.md#mem-obj-memories"
            - "memory.md#mem-rte-memory-extraction"
          note: "Existing rows and recent traces feed automatic durable guidance revision; no improved capacity is inferred."
        -
          scope: "Memory category/timestamp priority at default prompt selector"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-bap-user-memory"
                - "memory.md#mem-obj-memories"
              note: "Rules precede facts and newer rows precede older rows within categories; retained fields influence selection priority."
          records:
            - "memory.md#mem-bap-user-memory"
            - "memory.md#mem-obj-memories"
          note: "Stored category and creation order influence relative delivery priority before token-fit selection."
        -
          scope: "Memory IDs and supersession metadata at write/read gates"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memories"
                - "memory.md#mem-rte-memory-extraction"
              note: "Loaded existing IDs determine admissible supersedes_id references."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memories"
                - "memory.md#mem-rte-memory-extraction"
              note: "Invalid references are withheld; superseded rows are excluded from active delivery."
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-memories"
                - "memory.md#mem-rte-memory-extraction"
              note: "User/chat/category/status metadata selects retained input scope and update targets."
          records:
            - "memory.md#mem-obj-memories"
            - "memory.md#mem-rte-memory-extraction"
          note: "Fixed membership and active-set consumers are distinct from prose guidance."
        -
          scope: "Recorded history at compaction update consumer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-rte-chat-compaction"
              note: "Recorded conversation/tool experience feeds summary production for later model invocation."
          records:
            - "memory.md#mem-rte-chat-compaction"
            - "memory.md#mem-obj-compaction"
          note: "Traces feed a retained continuation artifact, with image and budget omissions."
        -
          scope: "Compaction text and marker at continuation consumers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction"
                - "memory.md#mem-rte-chat-compaction"
              note: "Summary text supplies goals/findings/results/decisions as later model context."
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction"
                - "memory.md#mem-rte-chat-compaction"
              note: "Latest valid marker selects summary and remaining input window."
          records:
            - "memory.md#mem-obj-compaction"
            - "memory.md#mem-rte-chat-compaction"
          note: "Interpreted context and deterministic window control have different forces."
        -
          scope: "Recommendation summaries at future diagnostic model"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-recommendation"
                - "runtime.md#rt-rte-context-recommendation"
              note: "Prior finding summaries supply diagnostic context."
          records:
            - "memory.md#mem-obj-context-recommendation"
            - "runtime.md#rt-rte-context-recommendation"
          note: "Compact titles/status/file/fingerprint summaries, not full stored reasons, inform the next diagnostic pass."
        -
          scope: "Retained usage/feedback and recommendations at diagnostic update consumer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-recommendation"
                - "memory.md#mem-obj-context-recommendation"
                - "epistemic.md#epi-rte-finding-reconciliation"
              note: "Retained experience and prior findings feed revisions of durable diagnostic artifacts."
          records:
            - "runtime.md#rt-rte-context-recommendation"
            - "memory.md#mem-obj-context-recommendation"
            - "epistemic.md#epi-rte-finding-reconciliation"
          note: "The model and reconciler update durable diagnostic state consumed by later runs, without establishing truth or live analytics improvement."
        -
          scope: "Recommendation fingerprint/status/count state at reconciliation and PR selection"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-finding-reconciliation"
              note: "Dismissed fingerprints and current status determine whether candidate actions qualify."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-finding-reconciliation"
              note: "Dismissed matches are suppressed and insertion floors withhold new low-impact findings."
            -
              value: "ranking"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-finding-reconciliation"
                - "memory.md#mem-obj-context-recommendation"
              note: "Retained counts/status and computed impact influence priority and population decisions."
            -
              value: "routing"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-finding-reconciliation"
                - "runtime.md#rt-rte-context-recommendation"
              note: "Existing status/fingerprint and PR state select update, reopen, resolve or eligible PR path."
          records:
            - "memory.md#mem-obj-context-recommendation"
            - "epistemic.md#epi-rte-finding-reconciliation"
            - "runtime.md#rt-rte-context-recommendation"
          note: "Dismissal state is a veto, occurrence/status controls actions, and impact affects priority/admission."
        -
          scope: "Recommendation guidance/edits at PR or manual-fix surfaces"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-context-recommendation"
              note: "Stored fix guidance/fixPrompt affords directions to a manual fixing consumer."
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-recommendation"
                - "memory.md#mem-obj-context-recommendation"
              note: "Proposed edits supply patch content to the PR producer, without semantic endorsement."
          records:
            - "memory.md#mem-obj-context-recommendation"
            - "runtime.md#rt-rte-context-recommendation"
          note: "PR creation consumes proposed edits. Human execution of manual fix instructions is only afforded; live admission is separate."
        -
          scope: "Replayed prose, query evidence and saved readable files at later analytics consumers"
          assessment: "partial"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-web-chat"
                - "epistemic.md#epi-rte-query-results"
                - "memory.md#mem-rte-saved-files"
                - "runtime.md#rt-rte-explore-task"
              note: "Retained turns/reports, cached rows and requested readable files supply evidence/context."
          records:
            - "runtime.md#rt-rte-web-chat"
            - "epistemic.md#epi-rte-query-results"
            - "memory.md#mem-rte-saved-files"
            - "runtime.md#rt-rte-explore-task"
          note: "These establish reference/context supply; binary conversion and complete story/app-state effects remain unresolved."
        -
          scope: "Changed project rules/reference files at subsequent analytics consumers"
          assessment: "partial"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "runtime.md#rt-bap-project-guidance"
              note: "Admitted project rules and skills give later model directions."
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "runtime.md#rt-bap-project-guidance"
              note: "Admitted project reference content supplies analytics context."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "runtime.md#rt-bap-project-guidance"
          note: "Separate live admission is required. The ordinary write tool restriction is not authority of these retained contents."
        -
          scope: "Saved CLI report at later consumer"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-test-answer"
            - "epistemic.md#epi-rte-test-comparison"
          note: "Report saving is inspected, but later report-driven behavior is not; test comparison is not authority of a previously retained report."
        -
          scope: "Forked chat/history and copied checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-obj-compaction"
          note: "Fork producer and copied payload were located but not traced; Authority cannot be completed for alternative fork initialization."
        -
          scope: "Dynamic skill loading and channel-specific retained history/memory"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-explore-task"
            - "runtime.md#rt-bap-project-guidance"
            - "runtime.md#rt-rte-web-chat"
          note: "Dynamic load_skill and messaging-specific retention/consumption were not traced; standard web and explore witnesses do not cover these alternatives."
        -
          scope: "Story publication, retained app state and blob lifecycle"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-rte-saved-files"
          note: "Latest story replay is inspected, but publication, opaque app-state payload and cleanup chains are uninspected; a displayed story does not classify its app state."
        -
          scope: "Other saved-file byte producers and provider lifecycle"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-user-files"
            - "memory.md#mem-rte-saved-files"
          note: "Byte/from-disk APIs exist, but their producers, payload interpretation, admission and cleanup are uninspected; converted display text does not classify every stored binary."
        -
          scope: "Provider-specific CLI/API project-context admission"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "The dispatcher and Git delivery paths are inspected; provider outputs and API-upload admission are not fully traced. Changed project content is included, unchanged shipped instructions are excluded."
        -
          scope: "Recommendation feedback fallback and app-DB filtering"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-context-recommendation"
            - "runtime.md#rt-rte-context-recommendation"
            - "epistemic.md#epi-rte-finding-reconciliation"
          note: "Feedback fallback, coverage postprocessing and complete diagnostic query filtering are uninspected; the known reconciliation branch cannot complete this alternative."
        -
          scope: "Opaque external provider retention or adaptation"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-cmp-memory-extractor"
            - "runtime.md#rt-cmp-compaction-model"
            - "runtime.md#rt-cmp-agent-model"
          note: "Provider retention/training internals are outside the frozen evidence. No local parameter-update step is established. Any provider memory accumulated through use remains unresolved; static pretrained weights are not classified as accumulated memory."
      records:
        - "memory.md#mem-bap-user-memory"
        - "epistemic.md#epi-obj-personal-fact"
        - "epistemic.md#epi-obj-global-rule"
        - "memory.md#mem-obj-memories"
        - "memory.md#mem-rte-memory-extraction"
        - "memory.md#mem-rte-chat-compaction"
        - "memory.md#mem-obj-compaction"
        - "memory.md#mem-obj-context-recommendation"
        - "runtime.md#rt-rte-context-recommendation"
        - "epistemic.md#epi-rte-finding-reconciliation"
        - "runtime.md#rt-rte-web-chat"
        - "epistemic.md#epi-rte-query-results"
        - "memory.md#mem-rte-saved-files"
        - "runtime.md#rt-rte-explore-task"
        - "runtime.md#rt-rte-context-delivery"
        - "runtime.md#rt-bap-project-guidance"
        - "runtime.md#rt-rte-test-answer"
        - "epistemic.md#epi-rte-test-comparison"
        - "memory.md#mem-obj-user-files"
        - "memory.md#mem-cmp-memory-extractor"
        - "runtime.md#rt-cmp-compaction-model"
        - "runtime.md#rt-cmp-agent-model"
      note: "The inventory names actual update, downstream guidance and code-control consumers separately. Knowledge delivery is not compliance or epistemic acceptance; untraced payloads/consumers prevent an exhaustive force classification."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Extraction and supersession admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-extraction"
              note: "Conversation authoring and initiating chat do not approve each derived memory."
          records:
            - "memory.md#mem-rte-memory-extraction"
          note: "Software admits normalized model proposals without per-item human approval."
        -
          scope: "Explicit memory edit/delete/enablement surface"
          assessment: "partial"
          findings:
            -
              value: "manual"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-memory-maintenance"
              note: "The specified human-facing maintenance surface admits the chosen edit/withdrawal."
          records:
            - "memory.md#mem-rte-memory-maintenance"
          note: "The mutation affords an explicit human decision about supplied content or withdrawal; full UI caller wiring is uninspected."
        -
          scope: "Initial user-memory content admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-memories"
          note: "Schema/active-row presence does not resolve initial control."
        -
          scope: "Compaction replacement and streamed checkpoint admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-chat-compaction"
                - "memory.md#mem-obj-compaction"
              note: "Both in-process summary replacement and streamed-marker retention are software admission."
          records:
            - "memory.md#mem-rte-chat-compaction"
            - "memory.md#mem-obj-compaction"
          note: "Budget trigger and model return lead to software replacement/persistence without semantic approval."
        -
          scope: "Transcript and query-cache admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-web-chat"
                - "epistemic.md#epi-rte-query-results"
              note: "Response persistence and query cache writes are software-controlled."
          records:
            - "runtime.md#rt-rte-web-chat"
            - "epistemic.md#epi-rte-query-results"
          note: "Settled model messages and query returns are admitted by callbacks/adapters, not human confirmation of every retained item."
        -
          scope: "Recommendation transaction and configured automatic PR creation"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-recommendation"
                - "epistemic.md#epi-rte-finding-reconciliation"
              note: "Reconciliation and autoCreatePrs admit diagnoses/proposals without per-content approval."
          records:
            - "runtime.md#rt-rte-context-recommendation"
            - "epistemic.md#epi-rte-finding-reconciliation"
          note: "An operator can start/configure analysis but software selects each retained action and eligible PR."
        -
          scope: "Manual recommendation dismissal/status admission"
          assessment: "partial"
          findings:
            -
              value: "manual"
              basis: "afforded"
              records:
                - "epistemic.md#epi-rte-finding-reconciliation"
              note: "A human dismissal supplies retained fingerprint veto state as an afforded choice."
          records:
            - "epistemic.md#epi-rte-finding-reconciliation"
            - "memory.md#mem-obj-context-recommendation"
          note: "Human dismissal is described, but the status-mutation UI/policy is uninspected; do not upgrade that gap from the read-side veto."
        -
          scope: "User-selected file uploads"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records:
                - "memory.md#mem-rte-saved-files"
              note: "User upload chooses the specific retained material."
          records:
            - "memory.md#mem-rte-saved-files"
            - "memory.md#mem-obj-user-files"
          note: "Explicit choice of uploaded bytes establishes manual content admission for this branch."
        -
          scope: "Foreground-model file writes"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-saved-files"
              note: "Software admits the model write to scoped storage."
          records:
            - "memory.md#mem-rte-saved-files"
          note: "Model-selected authored text passes path/size gates, with no per-content approval."
        -
          scope: "Context refresh/sync byte admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
              note: "Software sync/refresh admits selected source bytes."
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "Operator source selection and workflow initiation are not approval of each transferred/generated file."
        -
          scope: "Upstream project source authoring/review"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "The operator selects a source, but per-content human authorship, approval and repository governance are unresolved."
        -
          scope: "Saved CLI evaluation report admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-test-answer"
              note: "CLI software saves assembled test results without report-by-report content approval."
          records:
            - "runtime.md#rt-rte-test-answer"
          note: "Workflow report saving is automatic after run-result collection."
        -
          scope: "Forked chat/history and copied checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-obj-compaction"
          note: "Fork producer and copied payload were located but not traced; Admission control cannot be completed for alternative fork initialization."
        -
          scope: "Dynamic skill loading and channel-specific retained history/memory"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-explore-task"
            - "runtime.md#rt-bap-project-guidance"
            - "runtime.md#rt-rte-web-chat"
          note: "Dynamic load_skill and messaging-specific retention/consumption were not traced; standard web and explore witnesses do not cover these alternatives."
        -
          scope: "Story publication, retained app state and blob lifecycle"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-rte-saved-files"
          note: "Latest story replay is inspected, but publication, opaque app-state payload and cleanup chains are uninspected; a displayed story does not classify its app state."
        -
          scope: "Other saved-file byte producers and provider lifecycle"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-user-files"
            - "memory.md#mem-rte-saved-files"
          note: "Byte/from-disk APIs exist, but their producers, payload interpretation, admission and cleanup are uninspected; converted display text does not classify every stored binary."
        -
          scope: "Provider-specific CLI/API project-context admission"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "The dispatcher and Git delivery paths are inspected; provider outputs and API-upload admission are not fully traced. Changed project content is included, unchanged shipped instructions are excluded."
        -
          scope: "Recommendation feedback fallback and app-DB filtering"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-context-recommendation"
            - "runtime.md#rt-rte-context-recommendation"
            - "epistemic.md#epi-rte-finding-reconciliation"
          note: "Feedback fallback, coverage postprocessing and complete diagnostic query filtering are uninspected; the known reconciliation branch cannot complete this alternative."
        -
          scope: "Opaque external provider retention or adaptation"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-cmp-memory-extractor"
            - "runtime.md#rt-cmp-compaction-model"
            - "runtime.md#rt-cmp-agent-model"
          note: "Provider retention/training internals are outside the frozen evidence. No local parameter-update step is established. Any provider memory accumulated through use remains unresolved; static pretrained weights are not classified as accumulated memory."
      records:
        - "memory.md#mem-rte-memory-extraction"
        - "memory.md#mem-rte-memory-maintenance"
        - "memory.md#mem-obj-memories"
        - "memory.md#mem-rte-chat-compaction"
        - "memory.md#mem-obj-compaction"
        - "runtime.md#rt-rte-web-chat"
        - "epistemic.md#epi-rte-query-results"
        - "runtime.md#rt-rte-context-recommendation"
        - "epistemic.md#epi-rte-finding-reconciliation"
        - "memory.md#mem-obj-context-recommendation"
        - "memory.md#mem-rte-saved-files"
        - "memory.md#mem-obj-user-files"
        - "runtime.md#rt-rte-context-delivery"
        - "runtime.md#rt-rte-test-answer"
        - "runtime.md#rt-rte-explore-task"
        - "runtime.md#rt-bap-project-guidance"
        - "memory.md#mem-cmp-memory-extractor"
        - "runtime.md#rt-cmp-compaction-model"
        - "runtime.md#rt-cmp-agent-model"
      note: "Known software admission coexists with explicit upload/edit/dismissal surfaces. Initial rows, remote source governance, file producers and alternative caller policies remain unresolved; agency is not authorship or physical I/O."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Recent conversation to standing user memories"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-extraction"
              note: "Recorded session messages are reduced to standing facts/directives, even while raw history remains."
          records:
            - "memory.md#mem-rte-memory-extraction"
            - "memory.md#mem-obj-memories"
          note: "Extracting durable facts/directives reduces recorded conversational material; content faithfulness is unobserved."
        -
          scope: "Memory supersession and explicit edits"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-extraction"
                - "memory.md#mem-rte-memory-maintenance"
              note: "Extraction replacements and explicit edits revise an existing memory."
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-extraction"
                - "memory.md#mem-obj-memories"
              note: "supersededBy withdraws active reliance without deleting predecessor history."
          records:
            - "memory.md#mem-rte-memory-extraction"
            - "memory.md#mem-rte-memory-maintenance"
            - "memory.md#mem-obj-memories"
          note: "Existing content can be revised, while superseded predecessors remain retained but inactive."
        -
          scope: "Explicit memory deletion and disablement"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-maintenance"
              note: "Explicit deletion forgets a retained row; no timed/automatic decay is inferred."
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-maintenance"
              note: "Disablement withdraws current use while retaining the rows."
          records:
            - "memory.md#mem-rte-memory-maintenance"
            - "memory.md#mem-obj-memories"
          note: "Deletion removes content; disabling suspends use without erasing remaining rows. Neither automatically restores superseded predecessors."
        -
          scope: "Conversation compaction"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-chat-compaction"
                - "memory.md#mem-obj-compaction"
              note: "Summary replaces a longer retained conversational representation for later invocation."
          records:
            - "memory.md#mem-rte-chat-compaction"
            - "memory.md#mem-obj-compaction"
          note: "Budget-selected traces become reduced continuation prose. Missing input and possible faithfulness defects do not establish synthesis."
        -
          scope: "Recommendation fingerprint reconciliation"
          assessment: "known"
          findings:
            -
              value: "dedup"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-finding-reconciliation"
              note: "Duplicate recordings collapse by fingerprint with last winning."
            -
              value: "evolve"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-finding-reconciliation"
                - "memory.md#mem-obj-context-recommendation"
              note: "Existing findings update/reopen and persisted fields change."
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-finding-reconciliation"
                - "memory.md#mem-obj-context-recommendation"
              note: "Dismissed/resolved administrative state withdraws active treatment while retained history remains."
          records:
            - "epistemic.md#epi-rte-finding-reconciliation"
            - "memory.md#mem-obj-context-recommendation"
          note: "Inspected code, not the diagnostic command name, establishes transformations."
        -
          scope: "Latest story body and duplicate replay"
          assessment: "partial"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-web-chat"
              note: "Historical model-visible story content is replaced with latest DB content."
            -
              value: "dedup"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-web-chat"
              note: "Earlier duplicate story bodies become stubs in prepared history."
          records:
            - "runtime.md#rt-rte-web-chat"
          note: "The prepared-history path refreshes current story versions and suppresses earlier duplicate bodies; full story lifecycle remains uninspected."
        -
          scope: "Cached SQL-result rerun and stale-output suppression"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-query-results"
              note: "Rerun replaces cached/current result under the query ID."
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-query-results"
              note: "Superseded retained tool output ceases current reliance and points to the latest result."
          records:
            - "epistemic.md#epi-rte-query-results"
          note: "Same-ID result replacement is not proof of a semantic correction."
        -
          scope: "Saved text overwrite and live project-context replacement"
          assessment: "partial"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-saved-files"
                - "runtime.md#rt-rte-context-delivery"
              note: "Software overwrites existing output/context content along inspected routes."
          records:
            - "memory.md#mem-rte-saved-files"
            - "runtime.md#rt-rte-context-delivery"
          note: "Named file overwrite and delivered revisions change existing retained entries; provider transformations remain uninspected."
        -
          scope: "Model-selected duplication, new diagnosis and semantic patch transformations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-memory-extraction"
            - "runtime.md#rt-rte-context-recommendation"
            - "memory.md#mem-obj-context-recommendation"
          note: "Model requests and rootCause fields do not establish reliable deduplication, novel claims or synthesis. Accepted records leave actual semantic relation indeterminate."
        -
          scope: "Forked chat/history and copied checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-obj-compaction"
          note: "Fork producer and copied payload were located but not traced; Curation cannot be completed for alternative fork initialization."
        -
          scope: "Dynamic skill loading and channel-specific retained history/memory"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-explore-task"
            - "runtime.md#rt-bap-project-guidance"
            - "runtime.md#rt-rte-web-chat"
          note: "Dynamic load_skill and messaging-specific retention/consumption were not traced; standard web and explore witnesses do not cover these alternatives."
        -
          scope: "Story publication, retained app state and blob lifecycle"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-rte-saved-files"
          note: "Latest story replay is inspected, but publication, opaque app-state payload and cleanup chains are uninspected; a displayed story does not classify its app state."
        -
          scope: "Other saved-file byte producers and provider lifecycle"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-user-files"
            - "memory.md#mem-rte-saved-files"
          note: "Byte/from-disk APIs exist, but their producers, payload interpretation, admission and cleanup are uninspected; converted display text does not classify every stored binary."
        -
          scope: "Provider-specific CLI/API project-context admission"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "The dispatcher and Git delivery paths are inspected; provider outputs and API-upload admission are not fully traced. Changed project content is included, unchanged shipped instructions are excluded."
        -
          scope: "Recommendation feedback fallback and app-DB filtering"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-context-recommendation"
            - "runtime.md#rt-rte-context-recommendation"
            - "epistemic.md#epi-rte-finding-reconciliation"
          note: "Feedback fallback, coverage postprocessing and complete diagnostic query filtering are uninspected; the known reconciliation branch cannot complete this alternative."
        -
          scope: "Opaque external provider retention or adaptation"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-cmp-memory-extractor"
            - "runtime.md#rt-cmp-compaction-model"
            - "runtime.md#rt-cmp-agent-model"
          note: "Provider retention/training internals are outside the frozen evidence. No local parameter-update step is established. Any provider memory accumulated through use remains unresolved; static pretrained weights are not classified as accumulated memory."
      records:
        - "memory.md#mem-rte-memory-extraction"
        - "memory.md#mem-obj-memories"
        - "memory.md#mem-rte-memory-maintenance"
        - "memory.md#mem-rte-chat-compaction"
        - "memory.md#mem-obj-compaction"
        - "epistemic.md#epi-rte-finding-reconciliation"
        - "memory.md#mem-obj-context-recommendation"
        - "runtime.md#rt-rte-web-chat"
        - "epistemic.md#epi-rte-query-results"
        - "memory.md#mem-rte-saved-files"
        - "runtime.md#rt-rte-context-delivery"
        - "runtime.md#rt-rte-context-recommendation"
        - "runtime.md#rt-rte-explore-task"
        - "runtime.md#rt-bap-project-guidance"
        - "memory.md#mem-obj-user-files"
        - "memory.md#mem-cmp-memory-extractor"
        - "runtime.md#rt-cmp-compaction-model"
        - "runtime.md#rt-cmp-agent-model"
      note: "Consolidation, revision, withdrawal, forgetting and deterministic deduplication are local positives. Diagnostic scores are not automatically promotion; root-cause generation is not evidenced synthesis. Uninspected transformations remain included."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "User-memory default prompt injection and extraction-input reload"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-bap-user-memory"
                - "memory.md#mem-rte-memory-extraction"
              note: "Prompt construction and extractor preparation automatically supply selected active memories."
          records:
            - "memory.md#mem-bap-user-memory"
            - "memory.md#mem-rte-memory-extraction"
          note: "Automatic supply is not a foreground request for these retained rows; full overrides can bypass the default route."
        -
          scope: "Conversation continuation request"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-web-chat"
                - "runtime.md#rt-rte-mcp-chat"
              note: "Requested chat continuation reloads retained transcript by identity."
          records:
            - "runtime.md#rt-rte-web-chat"
            - "runtime.md#rt-rte-mcp-chat"
          note: "The consumer requests a specific chat; responding with stored history is pull, not another independent push."
        -
          scope: "Checkpoint and latest-story selection inside continuation"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-chat-compaction"
                - "memory.md#mem-obj-compaction"
                - "runtime.md#rt-rte-web-chat"
              note: "Latest valid summary and current story versions are automatically inserted into model-visible history."
          records:
            - "memory.md#mem-rte-chat-compaction"
            - "memory.md#mem-obj-compaction"
            - "runtime.md#rt-rte-web-chat"
          note: "Within requested reconstruction, automatic narrowing/replacement supplies retained checkpoint/current story parts without a separate request for them."
        -
          scope: "Explicit saved-file and cached-query reads"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-saved-files"
                - "epistemic.md#epi-rte-query-results"
              note: "read and read_query_result request retained content/paged rows."
          records:
            - "memory.md#mem-rte-saved-files"
            - "epistemic.md#epi-rte-query-results"
          note: "The model/host names a retained path/query and requests its contents; delivery fulfills that request."
        -
          scope: "Prior recommendation summaries and reconciliation state"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-recommendation"
                - "memory.md#mem-obj-context-recommendation"
                - "epistemic.md#epi-rte-finding-reconciliation"
              note: "Future diagnostic/reconciliation invocations automatically receive prior retained state."
          records:
            - "runtime.md#rt-rte-context-recommendation"
            - "memory.md#mem-obj-context-recommendation"
            - "epistemic.md#epi-rte-finding-reconciliation"
          note: "Initial diagnostic assembly supplies existing summaries and retained fingerprints/status to update consumers."
        -
          scope: "Admitted evolving project guidance at future prompt/read consumers"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "runtime.md#rt-bap-project-guidance"
              note: "Later standard prompt construction automatically supplies admitted rule/reference content."
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "runtime.md#rt-bap-project-guidance"
              note: "Context-reading tools request retained delivered project material."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "runtime.md#rt-bap-project-guidance"
          note: "Prompt supply and explicit context reads are distinct operations; unchanged shipped static instructions are outside memory scope."
        -
          scope: "Saved evaluation report future consumption"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-test-answer"
            - "epistemic.md#epi-rte-test-comparison"
          note: "Saving is known, but no later model/behavior-shaping read route is established; this is not a bounded absence."
        -
          scope: "Forked chat/history and copied checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-obj-compaction"
          note: "Fork producer and copied payload were located but not traced; Read-back cannot be completed for alternative fork initialization."
        -
          scope: "Dynamic skill loading and channel-specific retained history/memory"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-explore-task"
            - "runtime.md#rt-bap-project-guidance"
            - "runtime.md#rt-rte-web-chat"
          note: "Dynamic load_skill and messaging-specific retention/consumption were not traced; standard web and explore witnesses do not cover these alternatives."
        -
          scope: "Story publication, retained app state and blob lifecycle"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-rte-saved-files"
          note: "Latest story replay is inspected, but publication, opaque app-state payload and cleanup chains are uninspected; a displayed story does not classify its app state."
        -
          scope: "Other saved-file byte producers and provider lifecycle"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-user-files"
            - "memory.md#mem-rte-saved-files"
          note: "Byte/from-disk APIs exist, but their producers, payload interpretation, admission and cleanup are uninspected; converted display text does not classify every stored binary."
        -
          scope: "Provider-specific CLI/API project-context admission"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "The dispatcher and Git delivery paths are inspected; provider outputs and API-upload admission are not fully traced. Changed project content is included, unchanged shipped instructions are excluded."
        -
          scope: "Recommendation feedback fallback and app-DB filtering"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-context-recommendation"
            - "runtime.md#rt-rte-context-recommendation"
            - "epistemic.md#epi-rte-finding-reconciliation"
          note: "Feedback fallback, coverage postprocessing and complete diagnostic query filtering are uninspected; the known reconciliation branch cannot complete this alternative."
        -
          scope: "Opaque external provider retention or adaptation"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-cmp-memory-extractor"
            - "runtime.md#rt-cmp-compaction-model"
            - "runtime.md#rt-cmp-agent-model"
          note: "Provider retention/training internals are outside the frozen evidence. No local parameter-update step is established. Any provider memory accumulated through use remains unresolved; static pretrained weights are not classified as accumulated memory."
      records:
        - "memory.md#mem-bap-user-memory"
        - "memory.md#mem-rte-memory-extraction"
        - "runtime.md#rt-rte-web-chat"
        - "runtime.md#rt-rte-mcp-chat"
        - "memory.md#mem-rte-chat-compaction"
        - "memory.md#mem-obj-compaction"
        - "memory.md#mem-rte-saved-files"
        - "epistemic.md#epi-rte-query-results"
        - "runtime.md#rt-rte-context-recommendation"
        - "memory.md#mem-obj-context-recommendation"
        - "epistemic.md#epi-rte-finding-reconciliation"
        - "runtime.md#rt-rte-context-delivery"
        - "runtime.md#rt-bap-project-guidance"
        - "runtime.md#rt-rte-test-answer"
        - "epistemic.md#epi-rte-test-comparison"
        - "runtime.md#rt-rte-explore-task"
        - "memory.md#mem-obj-user-files"
        - "memory.md#mem-cmp-memory-extractor"
        - "runtime.md#rt-cmp-compaction-model"
        - "runtime.md#rt-cmp-agent-model"
      note: "Both requested access and unsolicited assembly are supported, including different operations in one chain. Unknown report consumption and alternate forks/channels/providers prevent a complete direction inventory."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Default user-memory injection: identity matching"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-bap-user-memory"
                - "memory.md#mem-obj-memories"
              note: "User identity and source-chat identity match/exclusion select category/content delivered in MemoryBlock."
          records:
            - "memory.md#mem-bap-user-memory"
            - "memory.md#mem-obj-memories"
          note: "Trigger is default prompt construction. userId match and current-chat exclusion select delivered active rows; identifiers are actual predicates, not mere labels."
        -
          scope: "Default user-memory injection: availability/order/budget filtering"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-bap-user-memory"
              note: "Category/order and token-fit filters choose retained content without task-targeted inference."
          records:
            - "memory.md#mem-bap-user-memory"
          note: "The same trigger selects by enabled/active state, category priority, recency and 1000-token content budget; no semantic relevance search is established."
        -
          scope: "Existing-memory supply to extractor"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-extraction"
                - "memory.md#mem-obj-memories"
              note: "User/active-row query supplies matching existing memories to the update consumer."
          records:
            - "memory.md#mem-rte-memory-extraction"
            - "memory.md#mem-obj-memories"
          note: "Extraction preparation automatically selects active user rows including IDs for future replacement decisions."
        -
          scope: "Continuation checkpoint selector"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-chat-compaction"
                - "memory.md#mem-obj-compaction"
              note: "Marker type, nonempty validity and latest position choose retained checkpoint content."
          records:
            - "memory.md#mem-rte-chat-compaction"
            - "memory.md#mem-obj-compaction"
          note: "On reconstruction, latest nonempty data-compaction marker selects summary plus recent tail; requesting chat identity is separately pull."
        -
          scope: "Current story replay selector"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-web-chat"
              note: "Identity-linked latest-story lookup selects replacement content delivered to the model."
          records:
            - "runtime.md#rt-rte-web-chat"
          note: "During preparation, referenced story identity selects current DB body; older duplicates are stubbed."
        -
          scope: "Prior recommendation summary assembly"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-recommendation"
                - "runtime.md#rt-rte-context-recommendation"
              note: "Administrative availability/status and window rules supply compact prior-finding summaries."
          records:
            - "memory.md#mem-obj-context-recommendation"
            - "runtime.md#rt-rte-context-recommendation"
          note: "Diagnostic start supplies reconcilable status summaries under the configured period/budget; no task-inferred semantic ranking is established by this initial display."
        -
          scope: "Recommendation state selection for reconciliation"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-finding-reconciliation"
                - "memory.md#mem-obj-context-recommendation"
              note: "Fingerprint identity selects retained status/count/veto parts delivered to reconciliation."
          records:
            - "epistemic.md#epi-rte-finding-reconciliation"
            - "memory.md#mem-obj-context-recommendation"
          note: "Recorded fingerprint matches select existing recommendation state for update/resolve decisions, and dismissed matches select veto state."
        -
          scope: "Changed project guidance supply"
          assessment: "partial"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-project-guidance"
                - "runtime.md#rt-rte-context-delivery"
              note: "Project/provider file selection matches identity to select admitted guidance."
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-project-guidance"
                - "runtime.md#rt-rte-context-delivery"
              note: "Default versus complete override availability determines which retained guidance enters the prompt."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "runtime.md#rt-bap-project-guidance"
          note: "Prompt construction selects project guidance and configured override/provider files. Full provider-specific selectors remain uninspected."
        -
          scope: "Explicit saved-file and query paging pull routes"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-rte-saved-files"
            - "epistemic.md#epi-rte-query-results"
          note: "These units fulfill named requests, so push-selection signal is inapplicable locally; this is not a system-wide pull-only assertion."
        -
          scope: "Saved evaluation reports"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-test-answer"
          note: "Later consumption is not traced, preventing determination of either a push route or its signal."
        -
          scope: "Forked chat/history and copied checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-obj-compaction"
          note: "Fork producer and copied payload were located but not traced; Push selection cannot be completed for alternative fork initialization."
        -
          scope: "Dynamic skill loading and channel-specific retained history/memory"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-explore-task"
            - "runtime.md#rt-bap-project-guidance"
            - "runtime.md#rt-rte-web-chat"
          note: "Dynamic load_skill and messaging-specific retention/consumption were not traced; standard web and explore witnesses do not cover these alternatives."
        -
          scope: "Story publication, retained app state and blob lifecycle"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-rte-saved-files"
          note: "Latest story replay is inspected, but publication, opaque app-state payload and cleanup chains are uninspected; a displayed story does not classify its app state."
        -
          scope: "Other saved-file byte producers and provider lifecycle"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-user-files"
            - "memory.md#mem-rte-saved-files"
          note: "Byte/from-disk APIs exist, but their producers, payload interpretation, admission and cleanup are uninspected; converted display text does not classify every stored binary."
        -
          scope: "Provider-specific CLI/API project-context admission"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "The dispatcher and Git delivery paths are inspected; provider outputs and API-upload admission are not fully traced. Changed project content is included, unchanged shipped instructions are excluded."
        -
          scope: "Recommendation feedback fallback and app-DB filtering"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-context-recommendation"
            - "runtime.md#rt-rte-context-recommendation"
            - "epistemic.md#epi-rte-finding-reconciliation"
          note: "Feedback fallback, coverage postprocessing and complete diagnostic query filtering are uninspected; the known reconciliation branch cannot complete this alternative."
        -
          scope: "Opaque external provider retention or adaptation"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-cmp-memory-extractor"
            - "runtime.md#rt-cmp-compaction-model"
            - "runtime.md#rt-cmp-agent-model"
          note: "Provider retention/training internals are outside the frozen evidence. No local parameter-update step is established. Any provider memory accumulated through use remains unresolved; static pretrained weights are not classified as accumulated memory."
      records:
        - "memory.md#mem-bap-user-memory"
        - "memory.md#mem-obj-memories"
        - "memory.md#mem-rte-memory-extraction"
        - "memory.md#mem-rte-chat-compaction"
        - "memory.md#mem-obj-compaction"
        - "runtime.md#rt-rte-web-chat"
        - "memory.md#mem-obj-context-recommendation"
        - "runtime.md#rt-rte-context-recommendation"
        - "epistemic.md#epi-rte-finding-reconciliation"
        - "runtime.md#rt-rte-context-delivery"
        - "runtime.md#rt-bap-project-guidance"
        - "memory.md#mem-rte-saved-files"
        - "epistemic.md#epi-rte-query-results"
        - "runtime.md#rt-rte-test-answer"
        - "runtime.md#rt-rte-explore-task"
        - "memory.md#mem-obj-user-files"
        - "memory.md#mem-cmp-memory-extractor"
        - "runtime.md#rt-cmp-compaction-model"
        - "runtime.md#rt-cmp-agent-model"
      note: "Identifier and coarse selection are established at named automatic operations. Requested path/chat labels do not alone establish identifier push. No inferred embedding, lexical or judgment selector is asserted for uninspected branches."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Automatic user-memory extraction to future guidance"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-extraction"
                - "memory.md#mem-bap-user-memory"
              note: "Automatic trace-fed writes create retained behavior-shaping content for later invocations."
          records:
            - "memory.md#mem-rte-memory-extraction"
            - "memory.md#mem-bap-user-memory"
            - "memory.md#mem-obj-memories"
          note: "Recent recorded turns feed software-admitted durable facts/directives consumed by later prompts/extraction; improvement is not required or observed."
        -
          scope: "Streaming compaction to persisted continuation summary"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-chat-compaction"
                - "memory.md#mem-obj-compaction"
                - "runtime.md#rt-rte-web-chat"
              note: "Automatic summary write and stored-marker reconstruction form a trace-to-durable-context chain."
          records:
            - "memory.md#mem-rte-chat-compaction"
            - "memory.md#mem-obj-compaction"
            - "runtime.md#rt-rte-web-chat"
          note: "Raw/prepared conversation traces produce a summary persisted in a valid streamed marker and supplied on continuation."
        -
          scope: "Nonstreaming compaction to subsequent in-process model invocation"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-chat-compaction"
                - "memory.md#mem-obj-compaction"
              note: "Automatic trace-fed summary replacement shapes later step invocations within the process horizon."
          records:
            - "memory.md#mem-rte-chat-compaction"
            - "memory.md#mem-obj-compaction"
            - "runtime.md#rt-rte-test-answer"
          note: "generate lacks streamed-marker persistence, but the summary is retained in the working array and consumed by later steps. Cross-session persistence is not asserted."
        -
          scope: "Usage/feedback diagnosis to future diagnostic runs"
          assessment: "partial"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-recommendation"
                - "memory.md#mem-obj-context-recommendation"
                - "epistemic.md#epi-rte-finding-reconciliation"
              note: "Retained trace-derived diagnoses/administrative updates shape later diagnostic input."
          records:
            - "runtime.md#rt-rte-context-recommendation"
            - "memory.md#mem-obj-context-recommendation"
            - "epistemic.md#epi-rte-finding-reconciliation"
          note: "Automatically admitted recommendations are resupplied as compact summaries/state; PR merge/live analytics effect is not necessary for this diagnostic-memory route. Fallback inputs remain unresolved."
        -
          scope: "Raw transcript, query caches, saved files and delivered project revisions beyond qualifying routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "epistemic.md#epi-rte-query-results"
            - "memory.md#mem-rte-saved-files"
            - "runtime.md#rt-rte-context-delivery"
          note: "Storage/authoring/import alone does not establish an automatic trace-to-derived-guidance route. Complete producer coverage is missing, so no bounded no finding is made."
        -
          scope: "Evaluation reports and provider-side adaptation"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-test-answer"
            - "memory.md#mem-cmp-memory-extractor"
          note: "Reports have no established later learning consumer; provider adaptation internals are uninspected. Neither supports a system-wide negative."
        -
          scope: "Forked chat/history and copied checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-obj-compaction"
          note: "Fork producer and copied payload were located but not traced; Trace-fed learning cannot be completed for alternative fork initialization."
        -
          scope: "Dynamic skill loading and channel-specific retained history/memory"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-explore-task"
            - "runtime.md#rt-bap-project-guidance"
            - "runtime.md#rt-rte-web-chat"
          note: "Dynamic load_skill and messaging-specific retention/consumption were not traced; standard web and explore witnesses do not cover these alternatives."
        -
          scope: "Story publication, retained app state and blob lifecycle"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-rte-saved-files"
          note: "Latest story replay is inspected, but publication, opaque app-state payload and cleanup chains are uninspected; a displayed story does not classify its app state."
        -
          scope: "Other saved-file byte producers and provider lifecycle"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-user-files"
            - "memory.md#mem-rte-saved-files"
          note: "Byte/from-disk APIs exist, but their producers, payload interpretation, admission and cleanup are uninspected; converted display text does not classify every stored binary."
        -
          scope: "Provider-specific CLI/API project-context admission"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "The dispatcher and Git delivery paths are inspected; provider outputs and API-upload admission are not fully traced. Changed project content is included, unchanged shipped instructions are excluded."
        -
          scope: "Recommendation feedback fallback and app-DB filtering"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-context-recommendation"
            - "runtime.md#rt-rte-context-recommendation"
            - "epistemic.md#epi-rte-finding-reconciliation"
          note: "Feedback fallback, coverage postprocessing and complete diagnostic query filtering are uninspected; the known reconciliation branch cannot complete this alternative."
        -
          scope: "Opaque external provider retention or adaptation"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-cmp-memory-extractor"
            - "runtime.md#rt-cmp-compaction-model"
            - "runtime.md#rt-cmp-agent-model"
          note: "Provider retention/training internals are outside the frozen evidence. No local parameter-update step is established. Any provider memory accumulated through use remains unresolved; static pretrained weights are not classified as accumulated memory."
      records:
        - "memory.md#mem-rte-memory-extraction"
        - "memory.md#mem-bap-user-memory"
        - "memory.md#mem-obj-memories"
        - "memory.md#mem-rte-chat-compaction"
        - "memory.md#mem-obj-compaction"
        - "runtime.md#rt-rte-web-chat"
        - "runtime.md#rt-rte-test-answer"
        - "runtime.md#rt-rte-context-recommendation"
        - "memory.md#mem-obj-context-recommendation"
        - "epistemic.md#epi-rte-finding-reconciliation"
        - "epistemic.md#epi-rte-query-results"
        - "memory.md#mem-rte-saved-files"
        - "runtime.md#rt-rte-context-delivery"
        - "memory.md#mem-cmp-memory-extractor"
        - "runtime.md#rt-rte-explore-task"
        - "runtime.md#rt-bap-project-guidance"
        - "memory.md#mem-obj-user-files"
        - "runtime.md#rt-cmp-compaction-model"
        - "runtime.md#rt-cmp-agent-model"
      note: "Three transformation families establish qualifying automatic trace-fed memory routes, with streaming and nonstreaming summaries kept separate. Unresolved producers/consumers remain; no unsupported no finding is used to close their coverage. This axis does not assert improved capacity, parametric training or exercised self-improvement."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Original input to user-memory extraction"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-memory-extraction"
              note: "Recorded conversational turns, including user messages, supply the qualifying write."
          records:
            - "memory.md#mem-rte-memory-extraction"
          note: "Only recent user/assistant text is sampled, not tool payloads/images or a verified current answer."
        -
          scope: "Original input to streamed compaction"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-chat-compaction"
                - "runtime.md#rt-rte-web-chat"
              note: "Recorded turns supply conversational experience."
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-rte-chat-compaction"
                - "runtime.md#rt-rte-web-chat"
              note: "Recorded tool requests/results in preserved assistant/tool pairs supply execution experience."
          records:
            - "memory.md#mem-rte-chat-compaction"
            - "memory.md#mem-obj-compaction"
            - "runtime.md#rt-rte-web-chat"
          note: "Prepared conversational messages and assistant/tool pairs feed the summarizer after stripping images and selecting a budget suffix."
        -
          scope: "Original input to nonstreaming compaction"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-chat-compaction"
              note: "Conversation turns feed the retained step-continuation summary."
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-rte-chat-compaction"
              note: "Prepared tool-call/result pairs feed summary production."
          records:
            - "memory.md#mem-rte-chat-compaction"
            - "memory.md#mem-obj-compaction"
            - "runtime.md#rt-rte-test-answer"
          note: "Same content-selection chain, different retention horizon; no trajectory value follows merely from sequential messages."
        -
          scope: "Original usage/feedback input to recommendation updates"
          assessment: "partial"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-recommendation"
                - "epistemic.md#epi-rte-finding-reconciliation"
              note: "Retained chat usage/corrections supply diagnostic experience and trigger references."
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-recommendation"
                - "epistemic.md#epi-rte-finding-reconciliation"
              note: "Recorded tool/query failures inspected as diagnostic symptoms supply execution-feedback experience."
          records:
            - "runtime.md#rt-rte-context-recommendation"
            - "memory.md#mem-obj-context-recommendation"
            - "epistemic.md#epi-rte-finding-reconciliation"
          note: "Chat corrections/feedback and tool-error evidence support local source values. Full feedback fallback/query filtering remains uninspected; imported context files are additional nontrace inputs, not event-streams."
        -
          scope: "Potential other file/context/cache/report/provider update sources"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-saved-files"
            - "runtime.md#rt-rte-context-delivery"
            - "epistemic.md#epi-rte-query-results"
            - "runtime.md#rt-rte-test-answer"
            - "memory.md#mem-cmp-memory-extractor"
          note: "A qualifying automatic trace-fed write is not established or fully assessed on these branches; their source cannot be declared inapplicable from another route positive or negative."
        -
          scope: "Forked chat/history and copied checkpoints"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-obj-compaction"
          note: "Fork producer and copied payload were located but not traced; Trace origin cannot be completed for alternative fork initialization."
        -
          scope: "Dynamic skill loading and channel-specific retained history/memory"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-explore-task"
            - "runtime.md#rt-bap-project-guidance"
            - "runtime.md#rt-rte-web-chat"
          note: "Dynamic load_skill and messaging-specific retention/consumption were not traced; standard web and explore witnesses do not cover these alternatives."
        -
          scope: "Story publication, retained app state and blob lifecycle"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-web-chat"
            - "memory.md#mem-rte-saved-files"
          note: "Latest story replay is inspected, but publication, opaque app-state payload and cleanup chains are uninspected; a displayed story does not classify its app state."
        -
          scope: "Other saved-file byte producers and provider lifecycle"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-user-files"
            - "memory.md#mem-rte-saved-files"
          note: "Byte/from-disk APIs exist, but their producers, payload interpretation, admission and cleanup are uninspected; converted display text does not classify every stored binary."
        -
          scope: "Provider-specific CLI/API project-context admission"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "The dispatcher and Git delivery paths are inspected; provider outputs and API-upload admission are not fully traced. Changed project content is included, unchanged shipped instructions are excluded."
        -
          scope: "Recommendation feedback fallback and app-DB filtering"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-context-recommendation"
            - "runtime.md#rt-rte-context-recommendation"
            - "epistemic.md#epi-rte-finding-reconciliation"
          note: "Feedback fallback, coverage postprocessing and complete diagnostic query filtering are uninspected; the known reconciliation branch cannot complete this alternative."
        -
          scope: "Opaque external provider retention or adaptation"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-cmp-memory-extractor"
            - "runtime.md#rt-cmp-compaction-model"
            - "runtime.md#rt-cmp-agent-model"
          note: "Provider retention/training internals are outside the frozen evidence. No local parameter-update step is established. Any provider memory accumulated through use remains unresolved; static pretrained weights are not classified as accumulated memory."
      records:
        - "memory.md#mem-rte-memory-extraction"
        - "memory.md#mem-rte-chat-compaction"
        - "memory.md#mem-obj-compaction"
        - "runtime.md#rt-rte-web-chat"
        - "runtime.md#rt-rte-test-answer"
        - "runtime.md#rt-rte-context-recommendation"
        - "memory.md#mem-obj-context-recommendation"
        - "epistemic.md#epi-rte-finding-reconciliation"
        - "memory.md#mem-rte-saved-files"
        - "runtime.md#rt-rte-context-delivery"
        - "epistemic.md#epi-rte-query-results"
        - "memory.md#mem-cmp-memory-extractor"
        - "runtime.md#rt-rte-explore-task"
        - "runtime.md#rt-bap-project-guidance"
        - "memory.md#mem-obj-user-files"
        - "runtime.md#rt-cmp-compaction-model"
        - "runtime.md#rt-cmp-agent-model"
      note: "Original conversational and tool activity is supported on named qualifying writes. Source wrappers and fingerprints do not add event-streams or trajectories. Mixed feedback and alternative producers remain unresolved, so trace-source coverage is partial, not inapplicable."
---

# nao memory profile

## Comparison rationale

### Boundary and evidence strength

All axes are partial inventories, not complete-value assertions. Inspected
software paths establish local wiring; the accepted set supplies neither runs
nor causal experiments. Configured file-provider alternatives and human-facing
maintenance/fix surfaces retain their afforded basis where their full consumer
or provider implementation is uninspected. Missing behavior evidence does not
make a known architecture unknown, and a known architecture does not establish
activation or benefit.

The scope separates accumulated content from the whole runtime. Initial
pretrained weights and static shipped instructions are not positive memory
values. Opaque provider retention/adaptation remains an unresolved alternative.
Unconsumed credentials and transient ToolContext grants do not become memory
controls merely because code uses them. The retained evidence-valued part is
[EPI-OBJ-query-results](epistemic.md#epi-obj-query-results), not every field of
[RT-OBJ-tool-context](runtime.md#rt-obj-tool-context).

### Content, control and distinct consumers

User-memory prose supplies knowledge for profile statements and instruction for
standing rules through [MEM-BAP-user-memory](memory.md#mem-bap-user-memory).
Its IDs and supersession fields instead supply code-level routing, admission
criteria and exclusion. Content category/order/budget filtering is coarse;
actual user/source-chat matching is identifier selection. The same retained
experience has learning authority at its update consumer, independently of its
output's downstream authority. These paths are preserved in
[MEM-RTE-memory-extraction](memory.md#mem-rte-memory-extraction) and
[MEM-OBJ-memories](memory.md#mem-obj-memories).

Checkpoint text and marker controls also differ. A continuation request pulls
chat history. Automatic latest-valid-marker selection then pushes a summary
and selected tail; it is not another consumer request. The compaction model
can see only image-stripped, budget-selected input, not necessarily the entire
replaced prefix. Streaming persists a marker; generate retains only the
in-process replacement through that channel. Both can feed later model-step
invocations, but only the streamed path establishes stored-marker continuation.
See [MEM-RTE-chat-compaction](memory.md#mem-rte-chat-compaction) and
[MEM-OBJ-compaction](memory.md#mem-obj-compaction).

File-path reads and query-ID paging are pull. Their identifying arguments do
not establish identifier-based push. Converted file display does not resolve
opaque binary payloads or their producers. Saved evaluation reports have known
file retention and structured/prose parts, but their later learning consumer
is unresolved, not absent. See
[MEM-RTE-saved-files](memory.md#mem-rte-saved-files),
[EPI-RTE-query-results](epistemic.md#epi-rte-query-results) and the workflow
annotation on [RT-RTE-test-answer](runtime.md#rt-rte-test-answer).

### Curation and diagnostic memory

Consolidation follows the recorded transformation into reduced standing
content or a continuation summary. Unproven faithfulness does not turn it into
synthesis. Likewise, requested root-cause diagnosis does not establish a new
claim absent from the inputs. Deterministic fingerprint collapse, existing
finding updates and administrative withdrawal have their own wired curation
warrants in
[EPI-RTE-finding-reconciliation](epistemic.md#epi-rte-finding-reconciliation).
Explicit memory deletion is forgetting; supersession and disabling are
withdrawal without deleting retained history. No automatic timed decay,
semantic novelty or score-based promotion is inferred.

Recommendations are diagnostic memory even before any patch becomes live.
The next diagnostic prompt receives compact prior summaries, not automatically
all retained reasons. Reconciliation consumes fingerprint/status/count parts;
dismissed matches supply an enforced veto and an admission criterion. This
creates a qualifying trace-fed write/later diagnostic-consumer route without
proving ordinary analytics improvement. Its mixed usage/tool-feedback input
keeps partial source coverage. See
[MEM-OBJ-context-recommendation](memory.md#mem-obj-context-recommendation),
[RT-RTE-context-recommendation](runtime.md#rt-rte-context-recommendation) and
[EPI-RTE-finding-reconciliation](epistemic.md#epi-rte-finding-reconciliation).

PR creation, applied status and live context delivery remain different
transitions. Applied can follow either reconciliation resolution or PR opening;
it proves neither merge nor live consumption. Imported project revisions can
supply instruction/knowledge only through the separate delivery and later
prompt/read routes. Starting refresh chooses the source/workflow, not human
approval of every admitted byte. See
[RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) and
[RT-BAP-project-guidance](runtime.md#rt-bap-project-guidance).

### Canonical resolution and coverage limits

Reconciliation supersedes EPI-CMP-memory-extractor with
[MEM-CMP-memory-extractor](memory.md#mem-cmp-memory-extractor). That affects
only the canonical citation for opaque extraction-provider state; it upgrades
neither retention knowledge nor trace-learning strength. Other combined
objects/routes remain valid alongside their parts. The current runtime and
memory findings agree about budget-limited compaction input and the two applied
status producers, so no old interpretation controls these classifications.

Every supported local positive survives in the units and derived union.
Unresolved fork copies, dynamic skill/channel routes, story/app-state and file
lifecycle, context providers, feedback filtering and provider memory are not
removed to obtain complete coverage. No accepted bounded-absence record
licenses a global trace-learning no or a trace-source inapplicability claim.
Local pull units alone cannot make the full push-signal axis inapplicable.

Source-read log: none. This classification used only the supplied accepted
members, their types, collection and record/worker contracts. No source file,
incumbent profile or reference profile was read; no records or new evidence
were added.
