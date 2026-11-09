---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Citadel memory comparison: retained source revisions, derived session artifacts, projection/control state and bounded later consumers."
run-id: "AAS-2026-11-09-citadel-de4383eefa4e-01"
source-identity: "https://github.com/masumi-network/citadel"
reviewed-boundary: "749a24014a6cef59499dbe13b6fb4c348f8044a4"
memory-comparison:
  version: 2
  scope: "Included: accumulated lifecycle source/history, personal notes and shared traces, optimization notes, search projections, vault/conflict history, feedback, jobs/receipts, review/rejection state and saved evaluation/control artifacts, with provider and partially inspected capture/connector/repair alternatives retained as unresolved. Excluded: shipped static skills/prompts, provider model weights and enclosing host transcript management as Citadel mechanisms; recorded transcripts remain inputs to Citadel's qualifying derived writes."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Lifecycle retained bytes, heads, jobs and feedback ledger"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-revisions"
                - "memory.md#mem-obj-projection-receipts"
                - "memory.md#mem-obj-feedback-events"
              note: "SQLite contains source BLOBs, symbolic head/job state and feedback events."
          records:
            - "memory.md#mem-obj-source-revisions"
            - "memory.md#mem-obj-projection-receipts"
            - "memory.md#mem-obj-feedback-events"
          note: "Encoding of source bytes does not change their SQLite substrate."
        -
          scope: "Obsidian histories/conflicts and contribution-conflict records"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-obsidian-revisions"
                - "epistemic.md#epi-obj-conflict-record"
              note: "JSON files retain source bodies, revisions and warning state."
          records:
            - "memory.md#mem-obj-obsidian-revisions"
            - "epistemic.md#epi-obj-conflict-record"
          note: "These stores are distinct from lifecycle acceptance."
        -
          scope: "Configured searchable projection parts"
          assessment: "partial"
          findings:
            -
              value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-search-projections"
                - "runtime.md#rt-rte-source-projection"
              note: "Vector chunk stores are called by projection and recall."
            -
              value: "graph"
              basis: "wired"
              records:
                - "memory.md#mem-obj-search-projections"
                - "runtime.md#rt-rte-source-projection"
              note: "Optional graph projection and graph consumption are wired."
            -
              value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-obj-search-projections"
                - "runtime.md#rt-rte-source-projection"
              note: "The relational projection path writes and read-checks retained source material."
          records:
            - "memory.md#mem-obj-search-projections"
            - "runtime.md#rt-rte-source-projection"
          note: "Configuration branches are implemented; deployed backend choice and complete provider state remain unresolved."
        -
          scope: "Saved benchmark artifacts and automation permission receipt"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-benchmark-run"
                - "epistemic.md#epi-obj-evaluation-gate"
              note: "Saved JSON is reloaded for comparison or permission decisions."
          records:
            - "epistemic.md#epi-obj-benchmark-run"
            - "epistemic.md#epi-obj-evaluation-gate"
          note: "These are accumulated evaluation/control objects, not remote model weights."
        -
          scope: "Opaque provider successor and incompletely inspected telemetry, connector checkpoints and restore state"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "memory.md#mem-obj-search-projections"
            - "memory.md#mem-rte-feedback-processing"
            - "memory.md#mem-obj-source-revisions"
          note: "Recorded coverage leaves complete provider-owned structures and additional retained control stores unresolved."
      records:
        - "memory.md#mem-obj-source-revisions"
        - "memory.md#mem-obj-projection-receipts"
        - "memory.md#mem-obj-feedback-events"
        - "memory.md#mem-obj-obsidian-revisions"
        - "epistemic.md#epi-obj-conflict-record"
        - "memory.md#mem-obj-search-projections"
        - "runtime.md#rt-rte-source-projection"
        - "epistemic.md#epi-obj-benchmark-run"
        - "epistemic.md#epi-obj-evaluation-gate"
        - "memory.md#mem-rte-feedback-processing"
      note: "Known local stores do not enumerate every included maintenance/provider object; no model-weights finding follows from embedding writes."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Source/note/vault bodies and downstream host interpretation"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-revisions"
                - "memory.md#mem-obj-node-note"
                - "memory.md#mem-obj-session-trace"
                - "memory.md#mem-obj-optimization-note"
                - "memory.md#mem-obj-obsidian-revisions"
                - "runtime.md#rt-bap-context-delivery"
              note: "Retained prose excerpts, summaries and Markdown supply interpreted context."
          records:
            - "memory.md#mem-obj-source-revisions"
            - "memory.md#mem-obj-node-note"
            - "memory.md#mem-obj-session-trace"
            - "memory.md#mem-obj-optimization-note"
            - "memory.md#mem-obj-obsidian-revisions"
            - "runtime.md#rt-bap-context-delivery"
          note: "Source-code inputs can have distinct fixed-rule consumers; this unit covers prose consumption, not every submitted byte."
        -
          scope: "Access and control parts: heads, receipts, tags, paths, feedback and evaluation fields"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-revisions"
                - "memory.md#mem-obj-projection-receipts"
                - "memory.md#mem-obj-feedback-events"
                - "memory.md#mem-obj-obsidian-revisions"
                - "epistemic.md#epi-obj-evaluation-gate"
                - "epistemic.md#epi-obj-benchmark-run"
              note: "Fixed rules interpret IDs, bindings, scores, flags and revision metadata."
          records:
            - "memory.md#mem-obj-source-revisions"
            - "memory.md#mem-obj-projection-receipts"
            - "memory.md#mem-obj-feedback-events"
            - "memory.md#mem-obj-obsidian-revisions"
            - "epistemic.md#epi-obj-evaluation-gate"
            - "epistemic.md#epi-obj-benchmark-run"
          note: "Separate from natural-language bodies even when serialized together."
        -
          scope: "Embedding projections consumed by recall"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-search-projections"
                - "runtime.md#rt-cmp-embedding-profile"
              note: "Dense numerical representations are retrieval inputs, not trained weight updates."
          records:
            - "memory.md#mem-obj-search-projections"
            - "runtime.md#rt-cmp-embedding-profile"
          note: "The configured embedding projection path establishes this form without immutable model provenance."
        -
          scope: "Full provider graph/global-context-index successor and uninspected maintenance payloads"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "memory.md#mem-obj-search-projections"
            - "memory.md#mem-rte-feedback-processing"
          note: "A display description does not classify the opaque payload or all its consumers."
      records:
        - "memory.md#mem-obj-source-revisions"
        - "memory.md#mem-obj-node-note"
        - "memory.md#mem-obj-session-trace"
        - "memory.md#mem-obj-optimization-note"
        - "memory.md#mem-obj-obsidian-revisions"
        - "runtime.md#rt-bap-context-delivery"
        - "memory.md#mem-obj-projection-receipts"
        - "memory.md#mem-obj-feedback-events"
        - "epistemic.md#epi-obj-evaluation-gate"
        - "epistemic.md#epi-obj-benchmark-run"
        - "memory.md#mem-obj-search-projections"
        - "runtime.md#rt-cmp-embedding-profile"
        - "memory.md#mem-rte-feedback-processing"
      note: "Mixed objects are split by operative part; full provider and maintenance forms remain unresolved."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Deterministically distilled personal notes and transcript-derived shared traces"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-node-note"
                - "memory.md#mem-obj-session-trace"
                - "runtime.md#rt-rte-session-capture"
                - "memory.md#mem-rte-share-session"
              note: "Session turns and tool-use records feed bounded derived artifacts."
          records:
            - "memory.md#mem-obj-node-note"
            - "memory.md#mem-obj-session-trace"
            - "runtime.md#rt-rte-session-capture"
            - "memory.md#mem-rte-share-session"
          note: "Only transcript-derived sharing is covered; supplied compact text is a separate alternative."
        -
          scope: "Imported caller and connector/vault source material"
          assessment: "partial"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-revisions"
                - "memory.md#mem-obj-obsidian-revisions"
                - "memory.md#mem-rte-vault-sync"
                - "runtime.md#rt-rte-ingest-admission"
              note: "External source bytes and vault bodies enter retained stores."
          records:
            - "memory.md#mem-obj-source-revisions"
            - "memory.md#mem-obj-obsidian-revisions"
            - "memory.md#mem-rte-vault-sync"
            - "runtime.md#rt-rte-ingest-admission"
          note: "Import is known at admission; initial authorship and upstream derivation are not thereby resolved."
        -
          scope: "Optimization notes and source-bound projection derivatives"
          assessment: "partial"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-optimization-note"
                - "runtime.md#rt-rte-index-curation"
                - "memory.md#mem-obj-search-projections"
                - "runtime.md#rt-rte-source-projection"
              note: "Labels/tags become parsed optimization notes; retained bytes produce projections."
          records:
            - "memory.md#mem-obj-optimization-note"
            - "runtime.md#rt-rte-index-curation"
            - "memory.md#mem-obj-search-projections"
            - "runtime.md#rt-rte-source-projection"
          note: "This identifies derivation paths, not semantic fidelity or full embedding provenance."
        -
          scope: "Already-authored shared trace input and opaque provider successors"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "memory.md#mem-obj-session-trace"
            - "memory.md#mem-obj-search-projections"
          note: "Supplied-data origin and upstream improve derivation are not established; initial authorship cannot be enumerated."
      records:
        - "memory.md#mem-obj-node-note"
        - "memory.md#mem-obj-session-trace"
        - "runtime.md#rt-rte-session-capture"
        - "memory.md#mem-rte-share-session"
        - "memory.md#mem-obj-source-revisions"
        - "memory.md#mem-obj-obsidian-revisions"
        - "memory.md#mem-rte-vault-sync"
        - "runtime.md#rt-rte-ingest-admission"
        - "memory.md#mem-obj-optimization-note"
        - "runtime.md#rt-rte-index-curation"
        - "memory.md#mem-obj-search-projections"
        - "runtime.md#rt-rte-source-projection"
      note: "Known extraction/import/derivation paths coexist with unresolved initial and provider provenance; no complete lineage union is warranted."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Retained prose delivered to host and document readers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-node-note"
                - "memory.md#mem-obj-session-trace"
                - "memory.md#mem-obj-optimization-note"
                - "memory.md#mem-rte-document-drilldown"
                - "runtime.md#rt-bap-context-delivery"
              note: "Selected source content supplies untrusted context/reference, not binding standing directions."
          records:
            - "memory.md#mem-obj-node-note"
            - "memory.md#mem-obj-session-trace"
            - "memory.md#mem-obj-optimization-note"
            - "memory.md#mem-rte-document-drilldown"
            - "runtime.md#rt-bap-context-delivery"
          note: "Delivery is wired; compliance and actual behavioral change are not observed."
        -
          scope: "Retained source text and embedding features at retrieval selector"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-revisions"
                - "memory.md#mem-obj-search-projections"
                - "runtime.md#rt-rte-task-search"
              note: "Query matching/vector recall and top-k use retained content/features to prioritize hits."
          records:
            - "memory.md#mem-obj-source-revisions"
            - "memory.md#mem-obj-search-projections"
            - "runtime.md#rt-rte-task-search"
          note: "Ranking input does not imply a learned ranking policy."
        -
          scope: "Heads, tombstones and projection receipts at search eligibility consumer"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-bap-current-head"
                - "memory.md#mem-obj-projection-receipts"
                - "epistemic.md#epi-rte-source-withdrawal"
              note: "Current-binding and tombstone checks exclude ineligible candidates."
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-bap-current-head"
                - "memory.md#mem-obj-projection-receipts"
                - "epistemic.md#epi-rte-source-withdrawal"
              note: "Retained binding/receipt criteria determine candidate admissibility."
          records:
            - "memory.md#mem-bap-current-head"
            - "memory.md#mem-obj-projection-receipts"
            - "epistemic.md#epi-rte-source-withdrawal"
          note: "This force is bounded to named lifecycle search branches, not historical-ID denial."
        -
          scope: "Retained jobs/events and automation receipt at maintenance consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-projection-receipts"
                - "memory.md#mem-rte-feedback-processing"
                - "epistemic.md#epi-rte-automation-receipt"
              note: "Job state selects resumable projection work; processing state selects unprocessed feedback."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-projection-receipts"
                - "memory.md#mem-rte-feedback-processing"
                - "epistemic.md#epi-rte-automation-receipt"
              note: "Receipt validity permits or refuses automated improve."
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-projection-receipts"
                - "memory.md#mem-rte-feedback-processing"
                - "epistemic.md#epi-rte-automation-receipt"
              note: "Receipt fields supply conformity criteria for permission."
          records:
            - "memory.md#mem-obj-projection-receipts"
            - "memory.md#mem-rte-feedback-processing"
            - "epistemic.md#epi-rte-automation-receipt"
          note: "Each finding is supported at its actual fixed-code consumer; receipt assertions are not verified measurements."
        -
          scope: "Retained session experience at automatic note-producing consumer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-node-note"
                - "runtime.md#rt-rte-session-capture"
                - "memory.md#mem-obj-session-trace"
                - "memory.md#mem-rte-share-session"
              note: "Recorded experience feeds durable summaries for later host context."
          records:
            - "memory.md#mem-obj-node-note"
            - "runtime.md#rt-rte-session-capture"
            - "memory.md#mem-obj-session-trace"
            - "memory.md#mem-rte-share-session"
          note: "Learning authority at the update consumer is distinct from output knowledge authority and improved capacity."
        -
          scope: "Opaque Cognee improve/QA-cache consumers and incompletely inspected conflict/review uses"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "memory.md#mem-obj-search-projections"
            - "memory.md#mem-rte-feedback-processing"
            - "epistemic.md#epi-rte-conflict-record"
            - "runtime.md#rt-rte-promotion-review"
          note: "The full retained successor and its force are not established; previews do not classify every consumer."
      records:
        - "memory.md#mem-obj-node-note"
        - "memory.md#mem-obj-session-trace"
        - "memory.md#mem-obj-optimization-note"
        - "memory.md#mem-rte-document-drilldown"
        - "runtime.md#rt-bap-context-delivery"
        - "memory.md#mem-obj-source-revisions"
        - "memory.md#mem-obj-search-projections"
        - "runtime.md#rt-rte-task-search"
        - "memory.md#mem-bap-current-head"
        - "memory.md#mem-obj-projection-receipts"
        - "epistemic.md#epi-rte-source-withdrawal"
        - "memory.md#mem-rte-feedback-processing"
        - "epistemic.md#epi-rte-automation-receipt"
        - "runtime.md#rt-rte-session-capture"
        - "memory.md#mem-rte-share-session"
        - "epistemic.md#epi-rte-conflict-record"
        - "runtime.md#rt-rte-promotion-review"
      note: "Local knowledge, ranking, control and trace-update effects are supported; standing instruction authority and opaque effects are not inferred."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "SessionEnd extraction, projection and scheduled optimization-note admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-capture"
                - "runtime.md#rt-rte-source-projection"
                - "runtime.md#rt-rte-index-curation"
              note: "Software/model admission proceeds without a per-content human decision."
          records:
            - "runtime.md#rt-rte-session-capture"
            - "runtime.md#rt-rte-source-projection"
            - "runtime.md#rt-rte-index-curation"
          note: "Starting or configuring these workflows is not manual approval of each result."
        -
          scope: "Known-work promotion and automated event processing"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-promotion-review"
                - "memory.md#mem-rte-feedback-processing"
              note: "Engine thresholds admit known work and code persists event decisions."
          records:
            - "runtime.md#rt-rte-promotion-review"
            - "memory.md#mem-rte-feedback-processing"
          note: "Queued approval is a different admission mechanism."
        -
          scope: "Optional direct-learning transformation and chunk adoption"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-source-enrichment"
              note: "Configured software/model pipeline admits transformed chunks after guards."
          records:
            - "memory.md#mem-rte-source-enrichment"
          note: "Human origin of a source does not make subsequent per-chunk admission manual."
        -
          scope: "Generic API/local capture, supplied-data sharing, vault edits/conflicts and pending promotion approval"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "runtime.md#rt-rte-ingest-admission"
            - "runtime.md#rt-rte-local-access"
            - "memory.md#mem-rte-share-session"
            - "memory.md#mem-rte-vault-sync"
            - "runtime.md#rt-rte-promotion-review"
          note: "Caller credentials and a browser approval opportunity do not establish a human content decision. MCP approval is policy rather than a verified consent gate."
        -
          scope: "Opaque provider changes, connector checkpoint/recovery and backup/restore admission"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "memory.md#mem-obj-search-projections"
            - "memory.md#mem-obj-source-revisions"
          note: "The accepted inventory leaves control of additional included writes unresolved."
      records:
        - "runtime.md#rt-rte-session-capture"
        - "runtime.md#rt-rte-source-projection"
        - "runtime.md#rt-rte-index-curation"
        - "runtime.md#rt-rte-promotion-review"
        - "memory.md#mem-rte-feedback-processing"
        - "memory.md#mem-rte-source-enrichment"
        - "runtime.md#rt-rte-ingest-admission"
        - "runtime.md#rt-rte-local-access"
        - "memory.md#mem-rte-share-session"
        - "memory.md#mem-rte-vault-sync"
        - "memory.md#mem-obj-search-projections"
        - "memory.md#mem-obj-source-revisions"
      note: "Automatic admission has wired witnesses; no universal manual approval or complete admission inventory is established."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Session transcript extraction into personal/shared artifacts"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-node-note"
                - "memory.md#mem-obj-session-trace"
                - "runtime.md#rt-rte-session-capture"
                - "memory.md#mem-rte-share-session"
              note: "Selection and truncation reduce retained session content to excerpts and recaps."
          records:
            - "memory.md#mem-obj-node-note"
            - "memory.md#mem-obj-session-trace"
            - "runtime.md#rt-rte-session-capture"
            - "memory.md#mem-rte-share-session"
          note: "Lossy or misleading labels do not make this synthesis."
        -
          scope: "Private candidate to shared Central"
          assessment: "known"
          findings:
            -
              value: "promote"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-promotion-review"
              note: "Accepted copies raise scope to shared organization memory."
          records:
            - "runtime.md#rt-rte-promotion-review"
          note: "Review/automatic branches differ in admission but share the tier change."
        -
          scope: "Lifecycle/vault source replacement and withdrawal"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-revisions"
                - "memory.md#mem-obj-obsidian-revisions"
                - "memory.md#mem-rte-vault-sync"
                - "epistemic.md#epi-rte-source-withdrawal"
              note: "New revisions replace current entries while history remains."
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source-revisions"
                - "memory.md#mem-obj-obsidian-revisions"
                - "memory.md#mem-rte-vault-sync"
                - "epistemic.md#epi-rte-source-withdrawal"
              note: "Tombstones withdraw current-search reliance while retaining history."
          records:
            - "memory.md#mem-obj-source-revisions"
            - "memory.md#mem-obj-obsidian-revisions"
            - "memory.md#mem-rte-vault-sync"
            - "epistemic.md#epi-rte-source-withdrawal"
          note: "Historical reads remain possible; invalidation is not physical erasure."
        -
          scope: "Contribution warning-store bounded pruning"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-conflict-record"
              note: "Pruning removes retained warnings, preferring resolved before open records."
          records:
            - "epistemic.md#epi-rte-conflict-record"
          note: "This is local warning forgetting, not demonstrated salience decay of source knowledge."
        -
          scope: "Generated enrichment, optimization semantics and upstream Cognee improve"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "memory.md#mem-rte-source-enrichment"
            - "memory.md#mem-obj-optimization-note"
            - "runtime.md#rt-rte-index-curation"
            - "memory.md#mem-obj-search-projections"
          note: "Model requests and new summary-shaped notes do not establish whether changed claims consolidate or synthesize. Opaque improve cannot be classified by its name."
        -
          scope: "Legacy cleanup, connector/repair and backup alternatives"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "epistemic.md#epi-rte-garbage-cleanup"
            - "memory.md#mem-obj-source-revisions"
          note: "Deletion of scaffolds is recorded, but full maintenance semantics and complete operation inventory are not established; primary-key or candidate dedup alone does not prove retained-memory dedup."
      records:
        - "memory.md#mem-obj-node-note"
        - "memory.md#mem-obj-session-trace"
        - "runtime.md#rt-rte-session-capture"
        - "memory.md#mem-rte-share-session"
        - "runtime.md#rt-rte-promotion-review"
        - "memory.md#mem-obj-source-revisions"
        - "memory.md#mem-obj-obsidian-revisions"
        - "memory.md#mem-rte-vault-sync"
        - "epistemic.md#epi-rte-source-withdrawal"
        - "epistemic.md#epi-rte-conflict-record"
        - "memory.md#mem-rte-source-enrichment"
        - "memory.md#mem-obj-optimization-note"
        - "runtime.md#rt-rte-index-curation"
        - "memory.md#mem-obj-search-projections"
        - "epistemic.md#epi-rte-garbage-cleanup"
      note: "Known curation is local; no blanket synthesis, deduplication or complete set is inferred from maintenance labels."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Explicit MCP/HTTP/CLI search, document expansion and vault pull/history"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-task-search"
                - "memory.md#mem-rte-document-drilldown"
                - "runtime.md#rt-rte-local-access"
                - "memory.md#mem-rte-vault-sync"
              note: "Consumer requests return selected retained hits, bodies or revisions."
          records:
            - "runtime.md#rt-rte-task-search"
            - "memory.md#mem-rte-document-drilldown"
            - "runtime.md#rt-rte-local-access"
            - "memory.md#mem-rte-vault-sync"
          note: "Requested delivery is not counted again as push."
        -
          scope: "Task hook automatic supply to enclosing foreground context"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-task-search"
                - "runtime.md#rt-bap-context-delivery"
              note: "Prompt trigger drives automatic selection and stdout context without a foreground search request."
          records:
            - "runtime.md#rt-rte-task-search"
            - "runtime.md#rt-bap-context-delivery"
          note: "The hook's upstream HTTP request is a pull operation; automatic host supply is a distinct push step."
        -
          scope: "Maintenance reloads and selected retained context"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-source-projection"
                - "memory.md#mem-rte-feedback-processing"
                - "runtime.md#rt-rte-index-curation"
              note: "Workers request source bytes and processors request unprocessed events."
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-source-projection"
                - "memory.md#mem-rte-feedback-processing"
                - "runtime.md#rt-rte-index-curation"
              note: "Scheduled optimization selects capped recent retained labels/tags and supplies them to a model."
          records:
            - "runtime.md#rt-rte-source-projection"
            - "memory.md#mem-rte-feedback-processing"
            - "runtime.md#rt-rte-index-curation"
          note: "Request and selector operations are kept separate inside these chains."
        -
          scope: "Opaque provider/global-context-index and incompletely traced client/maintenance consumers"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "memory.md#mem-obj-search-projections"
            - "memory.md#mem-rte-feedback-processing"
            - "memory.md#mem-rte-vault-sync"
          note: "Documented local routes do not resolve every included later consumer or direction."
      records:
        - "runtime.md#rt-rte-task-search"
        - "memory.md#mem-rte-document-drilldown"
        - "runtime.md#rt-rte-local-access"
        - "memory.md#mem-rte-vault-sync"
        - "runtime.md#rt-bap-context-delivery"
        - "runtime.md#rt-rte-source-projection"
        - "memory.md#mem-rte-feedback-processing"
        - "runtime.md#rt-rte-index-curation"
        - "memory.md#mem-obj-search-projections"
      note: "Both request-driven returns and automatic supply exist; incomplete alternative coverage prevents known."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Task-triggered host-context push: query relevance"
          assessment: "known"
          findings:
            -
              value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-task-search"
                - "memory.md#mem-obj-source-revisions"
                - "memory.md#mem-obj-search-projections"
              note: "Cleaned task text selects retained source through lexical retrieval."
            -
              value: "inferred-embedding"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-task-search"
                - "memory.md#mem-obj-source-revisions"
                - "memory.md#mem-obj-search-projections"
              note: "Configured vector recall selects retained chunks against the task query."
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-task-search"
                - "memory.md#mem-obj-source-revisions"
                - "memory.md#mem-obj-search-projections"
              note: "Dataset/session availability and top-k/character caps bound supplied context separately from relevance."
          records:
            - "runtime.md#rt-rte-task-search"
            - "memory.md#mem-obj-source-revisions"
            - "memory.md#mem-obj-search-projections"
          note: "Trigger is UserPromptSubmit; selector inputs are cleaned prompt, scope and budgets; selected parts are short hit descriptions."
        -
          scope: "Scheduled optimization model supply"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-index-curation"
                - "memory.md#mem-obj-optimization-note"
              note: "Recent Central document nodes excluding optimization notes are capped and their labels/tags supplied."
          records:
            - "runtime.md#rt-rte-index-curation"
            - "memory.md#mem-obj-optimization-note"
          note: "Trigger is maintenance; recency/tag exclusion and cap select label/tag input, not full source bodies."
        -
          scope: "Promotion candidate/reviewer handoffs and opaque provider push alternatives"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "runtime.md#rt-rte-promotion-review"
            - "memory.md#mem-obj-search-projections"
            - "memory.md#mem-rte-feedback-processing"
          note: "Full push selectors and provider-consumed payload are unresolved. A queue ID on requested approval does not itself prove identifier-based push."
      records:
        - "runtime.md#rt-rte-task-search"
        - "memory.md#mem-obj-source-revisions"
        - "memory.md#mem-obj-search-projections"
        - "runtime.md#rt-rte-index-curation"
        - "memory.md#mem-obj-optimization-note"
        - "runtime.md#rt-rte-promotion-review"
        - "memory.md#mem-rte-feedback-processing"
      note: "Signals describe automatic selection, not every requested-ID read. No inferred-judgment or identifier signal is inferred merely from model triage or an ID."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Automatic SessionEnd transcript-to-personal-note route"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-session-capture"
                - "memory.md#mem-obj-node-note"
                - "epistemic.md#epi-rte-note-distill"
              note: "Recorded session/tool-use material becomes a retained note returned to later scoped search/document consumers."
          records:
            - "runtime.md#rt-rte-session-capture"
            - "memory.md#mem-obj-node-note"
            - "epistemic.md#epi-rte-note-distill"
          note: "Wired durable behavior-shaping context is sufficient; no capacity gain or weight update is claimed."
        -
          scope: "Transcript-distilled shared trace route"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-share-session"
                - "memory.md#mem-obj-session-trace"
              note: "Deterministic extraction plus software admission retains experience for later reference-only search."
          records:
            - "memory.md#mem-rte-share-session"
            - "memory.md#mem-obj-session-trace"
          note: "Tool approval policy does not make endpoint admission per-content human-controlled."
        -
          scope: "Supplied-data sharing, feedback/QA-cache improve and global-context-index successor"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "memory.md#mem-rte-share-session"
            - "memory.md#mem-obj-session-trace"
            - "memory.md#mem-rte-feedback-processing"
            - "memory.md#mem-obj-search-projections"
            - "runtime.md#rt-rte-index-curation"
          note: "Original supplied-text provenance and precise opaque update/successor/consumer chains are not established."
        -
          scope: "Additional capture, connector and recovery transformations"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "memory.md#mem-obj-source-revisions"
            - "memory.md#mem-obj-search-projections"
          note: "Recorded incomplete coverage prevents a complete qualifying-write inventory; no bounded absence record supports local no."
      records:
        - "runtime.md#rt-rte-session-capture"
        - "memory.md#mem-obj-node-note"
        - "epistemic.md#epi-rte-note-distill"
        - "memory.md#mem-rte-share-session"
        - "memory.md#mem-obj-session-trace"
        - "memory.md#mem-rte-feedback-processing"
        - "memory.md#mem-obj-search-projections"
        - "runtime.md#rt-rte-index-curation"
        - "memory.md#mem-obj-source-revisions"
      note: "A supported yes survives unresolved alternatives; this is trace-fed durable context, not proof of successful learning, reflection or exercised self-improvement."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Personal note production"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-node-note"
                - "runtime.md#rt-rte-session-capture"
                - "epistemic.md#epi-rte-note-distill"
              note: "First user prompt, assistant outcome and marked decisions originate in recorded conversational turns."
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-node-note"
                - "runtime.md#rt-rte-session-capture"
                - "epistemic.md#epi-rte-note-distill"
              note: "Edited file names are extracted from recorded tool-use entries."
          records:
            - "memory.md#mem-obj-node-note"
            - "runtime.md#rt-rte-session-capture"
            - "epistemic.md#epi-rte-note-distill"
          note: "The same qualifying write consumes both source types; successful tool effects are not verified."
        -
          scope: "Transcript-derived shared artifact production"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-trace"
                - "memory.md#mem-rte-share-session"
              note: "Recorded task and approach text feed compact shared context."
            -
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-trace"
                - "memory.md#mem-rte-share-session"
              note: "Recorded commands and error pairs feed command fields and dead-end descriptions."
          records:
            - "memory.md#mem-obj-session-trace"
            - "memory.md#mem-rte-share-session"
          note: "Serialization and author labels do not turn these into event-streams or verified trajectories."
        -
          scope: "Already-authored shared text, opaque provider improve/feedback and additional capture alternatives"
          assessment: "not-determinable"
          findings:
            []
          records:
            - "memory.md#mem-obj-session-trace"
            - "memory.md#mem-rte-share-session"
            - "memory.md#mem-obj-search-projections"
            - "memory.md#mem-rte-feedback-processing"
          note: "Unknown input origin and qualifying update prevent full source classification; telemetry alone does not warrant event-stream learning."
      records:
        - "memory.md#mem-obj-node-note"
        - "runtime.md#rt-rte-session-capture"
        - "epistemic.md#epi-rte-note-distill"
        - "memory.md#mem-obj-session-trace"
        - "memory.md#mem-rte-share-session"
        - "memory.md#mem-obj-search-projections"
        - "memory.md#mem-rte-feedback-processing"
      note: "Session and tool content are wired sources of known qualifying writes; neither linked trajectories nor event-stream-fed learning is established by the accepted inventory."
---

# Citadel memory profile

## Comparison rationale

This profile classifies accepted records, not the whole runtime's storage. All
ten inventories remain partial: known mechanisms coexist with named provider,
capture, connector, repair or consumer uncertainty. A configuration branch's
wired status does not establish deployed configuration or observed operation.
No source files were read for this profile; supplied records contain the
supporting passages.

The reconciled node-note object is
[MEM-OBJ-node-note](memory.md#mem-obj-node-note), not the superseded epistemic
object. The optional direct-learning route is
[MEM-RTE-source-enrichment](memory.md#mem-rte-source-enrichment), not the
superseded epistemic enrichment route. Its generated output remains
[EPI-OBJ-enriched-chunk](epistemic.md#epi-obj-enriched-chunk).
Neither supersession enables enrichment on HTTP ingest. The extraction part
[EPI-RTE-note-distill](epistemic.md#epi-rte-note-distill) remains distinct from
its parent capture route and qualifies note fidelity without defeating
consolidation or the retained trace-fed pathway.

Trace-learning yes applies to automatic production and admission of selected
experience that later consumers can receive, not to training weights or
demonstrated improvement. Its original inputs support session-logs and
tool-traces. Already-supplied shared text and opaque Cognee successors are
separate unresolved units. There is no evidenced-absence record supporting a
local no; missing improvement evidence is not such a warrant. See
[RT-RTE-session-capture](runtime.md#rt-rte-session-capture),
[MEM-RTE-share-session](memory.md#mem-rte-share-session) and
[MEM-OBJ-search-projections](memory.md#mem-obj-search-projections).

The task hook has a request-driven service step and an automatic host-context
supply step. Lexical/vector relevance selects retained text; scope and caps are
separate coarse controls. Explicit document expansion is pull, not
identifier-based push. Maintenance's automatic supply of recent labels/tags
also has a coarse selector. A requested identifier or a model's relevance
verdict alone does not establish an additional push signal. See
[RT-RTE-task-search](runtime.md#rt-rte-task-search),
[MEM-RTE-document-drilldown](memory.md#mem-rte-document-drilldown) and
[RT-RTE-index-curation](runtime.md#rt-rte-index-curation).

SQLite source content, JSON vault history and provider projections are
different objects. Tombstones invalidate current-search reliance while leaving
history; the vault may retain a revision before search admission rejects it.
Accordingly, enforcement and validation are bounded to actual selectors and
gates, not universal erasure or semantic acceptance. See
[MEM-OBJ-source-revisions](memory.md#mem-obj-source-revisions),
[MEM-RTE-vault-sync](memory.md#mem-rte-vault-sync),
[MEM-BAP-current-head](memory.md#mem-bap-current-head) and
[EPI-RTE-automation-receipt](epistemic.md#epi-rte-automation-receipt).

Known automatic admissions do not resolve generic caller identity or queued
approval into manual control. The approval instruction is policy; workflow
details retain software clients as alternatives even where browser confirmation
is offered. Optimization notes are additive outputs, not proven edits to the
original source or proven synthesis of new claims. Provider improve remains
opaque rather than receiving the strongest basis of the explicit note-write
branch. See [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review),
[RT-CLM-explicit-approval](runtime.md#rt-clm-explicit-approval),
[MEM-OBJ-optimization-note](memory.md#mem-obj-optimization-note) and
[MEM-OBJ-search-projections](memory.md#mem-obj-search-projections).
