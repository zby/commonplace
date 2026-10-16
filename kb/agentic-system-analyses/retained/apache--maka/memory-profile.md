---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Apache Maka memory profile: local entries, trace-derived facts, checkpoints, assistant indexes,
  Matters and retained continuation state at the frozen commit.'
run-id: AAS-2026-10-15-maka-4a8b73e41579-01
source-identity: https://github.com/apache/maka
reviewed-boundary: 1751c399239b0f6b717e98e2a5e2b875c3dd11ce
memory-comparison:
  version: 2
  scope: 'Retained local Markdown bodies/proposals and lifecycle metadata; long-term extracted facts and
    access/control structures; durable session/child history, effective projections, text and opaque provider
    checkpoints and tool-result reload; imported sessions; optional assistant index bodies/originals/coverage/progress,
    Matter snapshots/reviews, extraction files and daily archives; goal continuation and child patch artifacts.
    Included unresolved alternatives: remaining Goal/plan/Todo/WorkHub state, Feishu cache, through-use
    changed skill/workspace/plugin content, external-executor retention and client-specific later consumers.
    Excludes unchanged shipped static prompts/skills, ordinary unretained current-run state, serving weights
    not updated by these routes, and the whole runtime permission/storage surface except retained controls
    actually governing scoped memory.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Local entry bodies, pending proposals, bundle metadata and backups
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-obj-local-entries
          - memory.md#mem-obj-bundle-metadata
          note: MEMORY.md, PENDING.md and named backup documents retain the bundle.
        records: *id001
        note: The named Markdown documents and backups establish the local bundle substrate.
      - scope: Long-term facts, keys, lifecycle, cursors and receipts
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records: &id002
          - memory.md#mem-obj-memory-item
          - memory.md#mem-obj-item-index
          note: MemoryItem rows and key/control tables persist in SQLite.
        records: *id002
        note: The retained content and control parts share the inspected SQLite store.
      - scope: Assistant index documents, original-reference/cache records and coverage notes
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records: &id003
          - memory.md#mem-obj-index-documents
          - memory.md#mem-obj-index-cursors
          note: network.sqlite and corpus tables retain the index parts.
        records: *id003
        note: Both text and access metadata persist in the assistant corpus.
      - scope: Matter snapshots, materialized files and review journal
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records: &id004
          - memory.md#mem-obj-matter-state
          - memory.md#mem-obj-matter-reviews
          note: matters.sqlite retains metadata/history and review payloads.
        - value: files
          basis: wired
          records: *id004
          note: File objects and materialized request/state/inbox/change/draft files retain task material.
        records: *id004
        note: SQLite history and file objects are distinct retained parts of the same Matter route.
      - scope: Independent history extraction output and receipt
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id005
          - memory.md#mem-obj-extraction-files
          note: result.md and receipt.json persist under an extraction folder.
        records: *id005
        note: The separate extraction result is not an index row.
      - scope: Text checkpoint and encrypted provider-checkpoint persistence
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-text-checkpoint
        - memory.md#mem-obj-provider-checkpoint
        note: A checkpoint writer is recorded, but physical storage is uninspected for both alternatives.
          Ciphertext is an encoding, not a service-object, model-weight or file substrate finding.
      - scope: Runtime/child history and reload evidence, imported sessions, goal continuation, daily
          archives and patch artifacts
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-context-projection
        - memory.md#mem-rte-archive-read
        - runtime.md#rt-rte-child-graph
        - memory.md#mem-rte-session-import
        - epistemic.md#epi-rte-goal-selection
        - memory.md#mem-obj-review-archive
        - workflow.md#wf-rte-patch-publication
        note: Durability and later readers are recorded, but these records do not establish each physical
          store layout. A runtime event address or artifact name is not a substrate.
      - scope: Remaining included Goal/Todo/plan/WorkHub state, Feishu cache lifecycle, changed skills/workspace
          guidance, plugin state and client-specific retained-state routes
        assessment: uninspected
        findings: []
        records:
        - epistemic.md#epi-rte-goal-selection
        - memory.md#mem-rte-index-maintenance
        - memory.md#mem-bap-local-guidance
        - runtime.md#rt-rte-plugin-admission
        - runtime.md#rt-rte-executor-plugin
        note: The accepted inventory leaves physical storage unresolved for these paths. Goal continuation
          findings below do not resolve every goal or plan store; plugin composition does not expose arbitrary
          plugin state or external executor retention.
      records:
      - memory.md#mem-obj-local-entries
      - memory.md#mem-obj-bundle-metadata
      - memory.md#mem-obj-memory-item
      - memory.md#mem-obj-item-index
      - memory.md#mem-obj-index-documents
      - memory.md#mem-obj-index-cursors
      - memory.md#mem-obj-matter-state
      - memory.md#mem-obj-matter-reviews
      - memory.md#mem-obj-extraction-files
      - memory.md#mem-obj-text-checkpoint
      - memory.md#mem-obj-provider-checkpoint
      - runtime.md#rt-rte-context-projection
      - memory.md#mem-rte-archive-read
      - runtime.md#rt-rte-child-graph
      - memory.md#mem-rte-session-import
      - epistemic.md#epi-rte-goal-selection
      - memory.md#mem-obj-review-archive
      - workflow.md#wf-rte-patch-publication
      - memory.md#mem-rte-index-maintenance
      - memory.md#mem-bap-local-guidance
      - runtime.md#rt-rte-plugin-admission
      - runtime.md#rt-rte-executor-plugin
      note: Files and SQLite are established locally; checkpoint layouts and the remaining retained-state
        inventory prevent complete storage classification. Provider serving weights are not memory accumulated
        by the inspected routes.
    representational_form:
      assessment: partial
      units:
      - scope: Local entry bodies, retained facts, index document bodies and index progress notes
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id006
          - memory.md#mem-obj-local-entries
          - memory.md#mem-obj-memory-item
          - memory.md#mem-obj-index-documents
          - memory.md#mem-obj-index-cursors
          note: Titles/content, derived assertions, free-form index text and checkpoint notes carry interpreted
            meaning.
        records: *id006
        note: These textual parts reach model interpretation, separately from their metadata.
      - scope: Bundle admission metadata; fact keys/cursors/receipts; index coverage and references
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id007
          - memory.md#mem-obj-bundle-metadata
          - memory.md#mem-obj-item-index
          - memory.md#mem-obj-index-cursors
          note: Lifecycle/session IDs, normalized keys, exact cursors and revisions control eligibility
            and continuation.
        records: *id007
        note: These fields have fixed parser, lookup, version and range-check consumers.
      - scope: Text history summary and coverage wrapper
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id008
          - memory.md#mem-obj-text-checkpoint
          - runtime.md#rt-rte-context-projection
          note: The later provider request receives a rendered textual summary.
        - value: symbolic
          basis: wired
          records: *id008
          note: Coverage digests, phase and anchors are checked mechanically for reuse.
        records: *id008
        note: Separate consumption paths distinguish summary meaning from replay validity.
      - scope: Provider checkpoint encrypted payload
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-provider-checkpoint
        note: The consumed encrypted state has no inspected internal representation. Its readable display/coverage
          summary cannot establish natural-language, symbolic or parametric payload form.
      - scope: Provider checkpoint identity wrapper
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id009
          - memory.md#mem-obj-provider-checkpoint
          note: Connection/model/item identities drive compatibility checks before provider-boundary replay.
        records: *id009
        note: Only the visible wrapper is classified here.
      - scope: Matter working text and review feedback
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id010
          - memory.md#mem-obj-matter-state
          - memory.md#mem-obj-matter-reviews
          note: Working state, summaries and feedback require interpretation.
        - value: symbolic
          basis: wired
          records: *id010
          note: Approval flags, fingerprints, submission identities and inbox structures have fixed software
            consumers.
        records: *id010
        note: Natural-language state differs from mechanically checked review identity.
      - scope: Independent extraction product and daily-review sections with receipts/status
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id011
          - memory.md#mem-obj-extraction-files
          - memory.md#mem-obj-review-archive
          note: Model-generated extraction/review sections are interpreted text.
        - value: symbolic
          basis: wired
          records: *id011
          note: Selection, provenance, status, totals and model/range metadata are structured fields.
        records: *id011
        note: The recorded text and metadata paths are distinct.
      - scope: Goal evaluation and durable continuation prompt/control
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id012
          - epistemic.md#epi-obj-goal-evaluation
          - epistemic.md#epi-rte-goal-selection
          note: Reason-derived continuation text reaches the next goal turn.
        - value: symbolic
          basis: wired
          records: *id012
          note: Parsed flags and checkpoint/control identities select the transition.
        records: *id012
        note: The reason steers a later model; flags and lease/checkpoint identities govern code.
      - scope: Imported session payloads, retained tool results and child artifacts
        assessment: partial
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-rte-archive-read
          - runtime.md#rt-rte-child-graph
          note: Serialized tool-result text and bounded committed child model text can return as context.
        - value: symbolic
          basis: wired
          records:
          - workflow.md#wf-rte-patch-publication
          note: The retained text/x-diff patch expresses structured file changes; publication does not
            establish parent application.
        records:
        - memory.md#mem-rte-session-import
        - memory.md#mem-rte-archive-read
        - runtime.md#rt-rte-child-graph
        - workflow.md#wf-rte-patch-publication
        note: Text reload and a diff artifact are inspected, but arbitrary rich payload and imported role
          conversions remain unresolved.
      - scope: Remaining included Goal/Todo/plan/WorkHub state, Feishu cache lifecycle, changed skills/workspace
          guidance, plugin state and client-specific retained-state routes
        assessment: uninspected
        findings: []
        records:
        - epistemic.md#epi-rte-goal-selection
        - memory.md#mem-rte-index-maintenance
        - memory.md#mem-bap-local-guidance
        - runtime.md#rt-rte-plugin-admission
        - runtime.md#rt-rte-executor-plugin
        note: The accepted inventory leaves operative forms and consumers unresolved for these paths.
          Goal continuation findings below do not resolve every goal or plan store; plugin composition
          does not expose arbitrary plugin state or external executor retention.
      records:
      - memory.md#mem-obj-local-entries
      - memory.md#mem-obj-memory-item
      - memory.md#mem-obj-index-documents
      - memory.md#mem-obj-index-cursors
      - memory.md#mem-obj-bundle-metadata
      - memory.md#mem-obj-item-index
      - memory.md#mem-obj-text-checkpoint
      - runtime.md#rt-rte-context-projection
      - memory.md#mem-obj-provider-checkpoint
      - memory.md#mem-obj-matter-state
      - memory.md#mem-obj-matter-reviews
      - memory.md#mem-obj-extraction-files
      - memory.md#mem-obj-review-archive
      - epistemic.md#epi-obj-goal-evaluation
      - epistemic.md#epi-rte-goal-selection
      - memory.md#mem-rte-session-import
      - memory.md#mem-rte-archive-read
      - runtime.md#rt-rte-child-graph
      - workflow.md#wf-rte-patch-publication
      - memory.md#mem-rte-index-maintenance
      - memory.md#mem-bap-local-guidance
      - runtime.md#rt-rte-plugin-admission
      - runtime.md#rt-rte-executor-plugin
      note: Text and symbolic memory parts are established; provider ciphertext, rich/imported payloads
        and uninspected alternatives prevent a complete union. No retained parametric update is established
        by inference-model use.
    lineage:
      assessment: partial
      units:
      - scope: Local bundle bodies and their alternate admission origins
        assessment: partial
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-local-entries
          - memory.md#mem-obj-bundle-metadata
          note: Manual entry text is supplied through the authored-content path; user-labeled metadata
            alone does not authenticate the author.
        records:
        - memory.md#mem-obj-local-entries
        - memory.md#mem-obj-bundle-metadata
        - memory.md#mem-rte-local-memory
        note: Manual/proposal-derived origins are distinguished, but full caller provenance and every
          proposal derivation are unresolved.
      - scope: Long-term extracted fact text
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id013
          - memory.md#mem-rte-fact-extraction
          - memory.md#mem-obj-memory-item
          note: Models propose/localize/canonicalize facts from retained runtime evidence.
        records: *id013
        note: The implemented derivation is from eligible conversational evidence, irrespective of semantic
          fidelity.
      - scope: Text checkpoint summary
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id014
          - memory.md#mem-obj-text-checkpoint
          - runtime.md#rt-rte-context-projection
          note: Covered messages/tool-result history feed the retained continuation summary.
        records: *id014
        note: The summary derives from effective session history, not an initial static prompt.
      - scope: Provider encrypted checkpoint content
        assessment: partial
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-rte-context-projection
          - memory.md#mem-obj-provider-checkpoint
          note: The provider compactor produces retained state from covered effective history; this says
            nothing about its hidden form.
        records:
        - memory.md#mem-obj-provider-checkpoint
        - runtime.md#rt-rte-context-projection
        note: A history-fed compaction route is inspected, but hidden payload composition and any additional
          provenance remain unresolved.
      - scope: Assistant index bodies and progress notes
        assessment: partial
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-index-documents
          - memory.md#mem-rte-index-maintenance
          note: The ordinary agent writes arbitrary index text under chosen keys.
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-rte-index-maintenance
          - memory.md#mem-obj-index-documents
          note: The maintenance route organizes accessible history into retained documents for later body
            reads.
        records:
        - memory.md#mem-obj-index-documents
        - memory.md#mem-obj-index-cursors
        - memory.md#mem-rte-index-maintenance
        note: The agent authors documents from accessible history under a criterion; all original remote-source
          provenance and document-specific derivations are not recorded.
      - scope: External-session independent retained copy
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id015
          - memory.md#mem-rte-session-import
          note: Adapter/importer conversion admits externally recorded session history.
        records: *id015
        note: Import provenance is established at source-session selection; conversion fidelity remains
          a separate uncertainty.
      - scope: Fact access keys/control and index reference/coverage metadata
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id016
          - memory.md#mem-obj-item-index
          - memory.md#mem-obj-index-cursors
          note: Normalized lookup keys, receipts, references and coverage state are constructed by extraction/storage/maintenance
            code.
        records: *id016
        note: This unit concerns constructed access structures, not the origin of their referenced assertions.
      - scope: Matter working snapshots and reviews
        assessment: known
        findings:
        - value: authored
          basis: wired
          records: &id017
          - memory.md#mem-obj-matter-state
          - memory.md#mem-obj-matter-reviews
          - memory.md#mem-rte-matter-state
          note: Agents author working-state text and review feedback.
        - value: trace-extracted
          basis: wired
          records: *id017
          note: Checkpoint/review/resumption retains task experience and execution/inbox evidence for
            continuing work.
        records: *id017
        note: Worker-authored state and reviewer judgments derive from objective, amendments, draft, inbox
          and execution evidence.
      - scope: Independent extraction output and daily-review activity sections
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id018
          - memory.md#mem-rte-history-extract
          - memory.md#mem-obj-extraction-files
          - memory.md#mem-obj-review-archive
          note: Selected original histories and local activity feed generated extraction/review text.
        records: *id018
        note: The recorded generation routes derive retained products from selected history/activity.
      - scope: Goal pending prompt and control state
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id019
          - epistemic.md#epi-rte-goal-selection
          - epistemic.md#epi-rte-goal-judge
          note: Recent conversational evidence yields reason-derived next-turn steering.
        - value: other-compiled
          basis: wired
          records: *id019
          note: Code constructs transition state and continuation identity from parsed judgment flags.
        records: *id019
        note: The durable continuation is constructed from a judgment of recent conversation.
      - scope: Raw runtime/child histories and patch artifacts
        assessment: partial
        findings:
        - value: authored
          basis: wired
          records:
          - runtime.md#rt-rte-child-graph
          note: Committed child model text is produced by the child agent.
        - value: other-compiled
          basis: wired
          records:
          - workflow.md#wf-rte-patch-publication
          note: The worktree executor captures workspace changes into a diff artifact.
        records:
        - runtime.md#rt-rte-child-graph
        - workflow.md#wf-rte-patch-publication
        - runtime.md#rt-rte-context-projection
        note: Selected outputs and patch capture are known; full artifact initialization and event-payload
          provenance are not enumerated.
      - scope: Remaining included Goal/Todo/plan/WorkHub state, Feishu cache lifecycle, changed skills/workspace
          guidance, plugin state and client-specific retained-state routes
        assessment: uninspected
        findings: []
        records:
        - epistemic.md#epi-rte-goal-selection
        - memory.md#mem-rte-index-maintenance
        - memory.md#mem-bap-local-guidance
        - runtime.md#rt-rte-plugin-admission
        - runtime.md#rt-rte-executor-plugin
        note: The accepted inventory leaves initial and transformation provenance unresolved for these
          paths. Goal continuation findings below do not resolve every goal or plan store; plugin composition
          does not expose arbitrary plugin state or external executor retention.
      records:
      - memory.md#mem-obj-local-entries
      - memory.md#mem-obj-bundle-metadata
      - memory.md#mem-rte-local-memory
      - memory.md#mem-rte-fact-extraction
      - memory.md#mem-obj-memory-item
      - memory.md#mem-obj-text-checkpoint
      - runtime.md#rt-rte-context-projection
      - memory.md#mem-obj-provider-checkpoint
      - memory.md#mem-obj-index-documents
      - memory.md#mem-obj-index-cursors
      - memory.md#mem-rte-index-maintenance
      - memory.md#mem-rte-session-import
      - memory.md#mem-obj-item-index
      - memory.md#mem-obj-matter-state
      - memory.md#mem-obj-matter-reviews
      - memory.md#mem-rte-matter-state
      - memory.md#mem-rte-history-extract
      - memory.md#mem-obj-extraction-files
      - memory.md#mem-obj-review-archive
      - epistemic.md#epi-rte-goal-selection
      - epistemic.md#epi-rte-goal-judge
      - runtime.md#rt-rte-child-graph
      - workflow.md#wf-rte-patch-publication
      - memory.md#mem-bap-local-guidance
      - runtime.md#rt-rte-plugin-admission
      - runtime.md#rt-rte-executor-plugin
      note: Known derivation paths do not resolve every initial origin, remote source or opaque component.
        Authored and trace-extracted findings coexist when an agent authors history-derived text; they
        do not imply human admission.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Local active entry text at foreground model
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id020
          - memory.md#mem-obj-local-entries
          - memory.md#mem-rte-local-memory
          note: Eligible entry bodies supply later foreground context.
        records: *id020
        note: The composer labels retained entries untrusted context, not standing permission or higher-priority
          direction.
      - scope: Bundle lifecycle/scope/revision metadata at projection and mutation code
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records: &id021
          - memory.md#mem-obj-bundle-metadata
          - memory.md#mem-rte-local-memory
          note: Policy/status/session gates withhold ineligible entries and reject conflicting writes.
        - value: validation
          basis: wired
          records: *id021
          note: Bundle/document revisions and format constraints determine admissible mutations.
        - value: routing
          basis: wired
          records: *id021
          note: Scope/session identity selects which stored entries reach a given session.
        records: *id021
        note: Eligibility and revision controls differ from the advisory body consumer.
      - scope: Facts and past transcripts at Recall consumer
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id022
          - memory.md#mem-obj-memory-item
          - memory.md#mem-rte-recall-history
          note: The answering model receives fact content/kind/time or historical passages as context.
        records: *id022
        note: Recall returns selected assertions/passages, not stored canonicalization criticism.
      - scope: Fact keys/lifecycle and extraction cursors at lookup/admission consumers
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id023
          - memory.md#mem-obj-item-index
          - memory.md#mem-rte-recall-history
          - memory.md#mem-rte-fact-extraction
          note: Retained keys determine key-search matches; retained transcript text determines lexical
            passage ranking.
        - value: enforcement
          basis: wired
          records: *id023
          note: Inactive fact lifecycle and policy/evidence gates can exclude delivery or admission.
        - value: routing
          basis: wired
          records: *id023
          note: Cursors and receipts select processed ranges and continuation.
        - value: validation
          basis: wired
          records: *id023
          note: Version/cursor/idempotency consistency determines whether a write is admissible.
        records: *id023
        note: The actual consumers use keys for matching, lifecycle for reachability and cursors for update
          windows.
      - scope: Retained history at fact and textual-compaction update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id024
          - memory.md#mem-rte-fact-extraction
          - runtime.md#rt-rte-context-projection
          - memory.md#mem-obj-text-checkpoint
          note: Recorded session experience feeds durable facts and continuation summaries for later consumption.
        records: *id024
        note: Learning authority describes the update input, not a claim of measured improvement.
      - scope: Text checkpoint at later model and replay validator
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id025
          - memory.md#mem-obj-text-checkpoint
          - runtime.md#rt-rte-context-projection
          note: Rendered summary supplies compressed prior context.
        - value: validation
          basis: wired
          records: *id025
          note: Coverage/identity/model compatibility determines checkpoint admissibility.
        - value: routing
          basis: wired
          records: *id025
          note: Accepted coverage determines replay tail and replacement history window.
        records: *id025
        note: The text and its coverage wrapper have different effects.
      - scope: Opaque provider checkpoint at provider-boundary consumer
        assessment: partial
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-provider-checkpoint
          - runtime.md#rt-rte-context-projection
          note: Visible connection/model/coverage fields govern provider-state reuse and replay composition.
        records:
        - memory.md#mem-obj-provider-checkpoint
        - runtime.md#rt-rte-context-projection
        note: Compatibility routing is visible, but the encrypted consumed payload effect is unresolved;
          a knowledge/instruction/learning classification of that payload is not inferred from display
          text.
      - scope: Index bodies, criterion/progress notes and coverage metadata at their distinct consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id026
          - memory.md#mem-obj-index-documents
          - memory.md#mem-obj-index-cursors
          - memory.md#mem-rte-index-maintenance
          note: Requested index bodies and originals supply later reader context.
        - value: instruction
          basis: wired
          records: *id026
          note: Saved organizing criterion and progress notes guide subsequent maintenance tasks.
        - value: learning
          basis: wired
          records: *id026
          note: Accessible history is consumed to update durable index documents.
        - value: routing
          basis: wired
          records: *id026
          note: Exact saved boundaries and ranges choose subsequent maintenance input.
        - value: validation
          basis: wired
          records: *id026
          note: Retained revision/boundary identity checks reject stale checkpoint admission.
        - value: enforcement
          basis: wired
          records: *id026
          note: Stale revisions/ranges and visibility checks block operations.
        records: *id026
        note: Body reads, continued maintenance guidance and structural checkpoint decisions remain separate.
      - scope: Matter state and persisted review/currentness fields
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id027
          - memory.md#mem-obj-matter-state
          - memory.md#mem-obj-matter-reviews
          - memory.md#mem-rte-matter-state
          note: Prior state, summaries and history supply task evidence to the next activation.
        - value: learning
          basis: wired
          records: *id027
          note: Draft/inbox/execution evidence feeds revised durable working snapshots and review products.
        - value: validation
          basis: wired
          records: *id027
          note: Saved review basis, revision and verdict determine admissible settlement/replay.
        - value: enforcement
          basis: wired
          records: *id027
          note: A rejecting verdict/currentness mismatch prevents settlement.
        - value: routing
          basis: wired
          records: *id027
          note: Matter/activation identity and persisted next/wake state select continuing work.
        records: *id027
        note: Later state-file reads, current correction feedback and software replay checks have different
          horizons.
      - scope: Goal continuation prompt and durable checkpoint/lease state
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id028
          - epistemic.md#epi-rte-goal-selection
          - epistemic.md#epi-obj-goal-evaluation
          note: Reason-derived pending prompt steers the next goal turn.
        - value: routing
          basis: wired
          records: *id028
          note: Durable pending continuation and current checkpoint select next admission.
        - value: enforcement
          basis: wired
          records: *id028
          note: Terminal/currentness state can stop the goal loop or prevent stale continuation.
        records: *id028
        note: The retained reason and symbolic state have distinct consumers.
      - scope: Daily-review archive at later client query
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id029
          - memory.md#mem-obj-review-archive
          note: Archived activity sections are available to later querying clients.
        records: *id029
        note: This establishes a reference product for a client, not automatic method revision.
      - scope: Independent extraction files and patch artifacts at future adopter
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-history-extract
        - memory.md#mem-obj-extraction-files
        - workflow.md#wf-rte-patch-publication
        note: A retained file/path or artifact reference does not establish a downstream full-body consumer
          or parent adoption; previews/current returns alone do not settle later authority.
      - scope: External imported histories and changed workspace/skill/plugin content
        assessment: partial
        findings:
        - value: instruction
          basis: afforded
          records:
          - memory.md#mem-bap-local-guidance
          note: The recorded guidance load path affords instruction delivery if a retained skill/workspace
            file has been changed through use.
        records:
        - memory.md#mem-rte-session-import
        - memory.md#mem-bap-local-guidance
        - runtime.md#rt-rte-plugin-admission
        note: Imported role filtering and actual changed-content adoption remain unresolved; no universal
          instruction authority is inferred.
      - scope: Remaining included Goal/Todo/plan/WorkHub state, Feishu cache lifecycle, changed skills/workspace
          guidance, plugin state and client-specific retained-state routes
        assessment: uninspected
        findings: []
        records:
        - epistemic.md#epi-rte-goal-selection
        - memory.md#mem-rte-index-maintenance
        - memory.md#mem-bap-local-guidance
        - runtime.md#rt-rte-plugin-admission
        - runtime.md#rt-rte-executor-plugin
        note: The accepted inventory leaves consumer effects and later behavioral force unresolved for
          these paths. Goal continuation findings below do not resolve every goal or plan store; plugin
          composition does not expose arbitrary plugin state or external executor retention.
      records:
      - memory.md#mem-obj-local-entries
      - memory.md#mem-rte-local-memory
      - memory.md#mem-obj-bundle-metadata
      - memory.md#mem-obj-memory-item
      - memory.md#mem-rte-recall-history
      - memory.md#mem-obj-item-index
      - memory.md#mem-rte-fact-extraction
      - runtime.md#rt-rte-context-projection
      - memory.md#mem-obj-text-checkpoint
      - memory.md#mem-obj-provider-checkpoint
      - memory.md#mem-obj-index-documents
      - memory.md#mem-obj-index-cursors
      - memory.md#mem-rte-index-maintenance
      - memory.md#mem-obj-matter-state
      - memory.md#mem-obj-matter-reviews
      - memory.md#mem-rte-matter-state
      - epistemic.md#epi-rte-goal-selection
      - epistemic.md#epi-obj-goal-evaluation
      - memory.md#mem-obj-review-archive
      - memory.md#mem-rte-history-extract
      - memory.md#mem-obj-extraction-files
      - workflow.md#wf-rte-patch-publication
      - memory.md#mem-rte-session-import
      - memory.md#mem-bap-local-guidance
      - runtime.md#rt-rte-plugin-admission
      - runtime.md#rt-rte-executor-plugin
      note: All authority values describe named retained parts at actual consumers. Update-input learning
        and output knowledge/instruction are separate. No source wiring proves model obedience, benefit
        or universal retained-state authority.
    write_agency:
      assessment: partial
      units:
      - scope: Local bundle approve/manual-save and whole replacement mechanisms
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-local-memory
        - memory.md#mem-obj-bundle-metadata
        note: Explicit review/edit surfaces and producer-written user labels do not establish a human
          decision at every caller. Manual is not asserted from API names or physical file I/O.
      - scope: Fact proposal/canonicalization-to-commit
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id030
          - memory.md#mem-rte-fact-extraction
          - epistemic.md#epi-rte-memory-disposition
          - epistemic.md#epi-rte-memory-commit
          note: Software/model evidence admission and policy rechecks select and commit fact wording.
        records: *id030
        note: Starting remember/extraction does not approve each generated item.
      - scope: Textual and provider compaction checkpoint admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id031
          - runtime.md#rt-rte-context-projection
          - memory.md#mem-obj-text-checkpoint
          - memory.md#mem-obj-provider-checkpoint
          note: Code admits summary/provider-state results through the checkpoint writer.
        records: *id031
        note: Structural/coverage checks admit generated state without per-summary operator approval.
      - scope: Assistant index body edits and coverage/progress checkpoints
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id032
          - memory.md#mem-rte-index-maintenance
          - memory.md#mem-obj-index-cursors
          note: Ordinary agent writes documents and progress while software checks exact ranges/revisions.
        records: *id032
        note: An initiating user criterion is not per-document approval.
      - scope: Matter checkpoint and reviewed settlement
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id033
          - memory.md#mem-rte-matter-state
          - memory.md#mem-obj-matter-reviews
          note: Worker and review model propose/judge; software commits current eligible state.
        records: *id033
        note: Intermediate checkpoint and final settlement gates are separate but both computational.
      - scope: Independent extraction files; daily activity archive
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id034
          - memory.md#mem-rte-history-extract
          - memory.md#mem-obj-review-archive
          note: Code saves model output/receipt or publishes generated/fallback review sections without
            per-content human approval.
        records: *id034
        note: Caller initiation does not change the generated-output admission mechanism.
      - scope: Goal continuation durability and child patch publication
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id035
          - epistemic.md#epi-rte-goal-selection
          - workflow.md#wf-rte-patch-publication
          note: Coordinator records eligible pending steering and finalizer publishes eligible patches
            under code gates.
        records: *id035
        note: Automatic persistence is tied to selection/finalization, not arbitrary physical I/O.
      - scope: External-session source selection and admission control
        assessment: partial
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-session-import
          note: The Host converts and publishes the selected session through staged software admission.
        records:
        - memory.md#mem-rte-session-import
        note: Software conversion/publication is established, while the source-selection caller and per-message
          control are not.
      - scope: Remaining included Goal/Todo/plan/WorkHub state, Feishu cache lifecycle, changed skills/workspace
          guidance, plugin state and client-specific retained-state routes
        assessment: uninspected
        findings: []
        records:
        - epistemic.md#epi-rte-goal-selection
        - memory.md#mem-rte-index-maintenance
        - memory.md#mem-bap-local-guidance
        - runtime.md#rt-rte-plugin-admission
        - runtime.md#rt-rte-executor-plugin
        note: The accepted inventory leaves per-content human versus computational admission unresolved
          for these paths. Goal continuation findings below do not resolve every goal or plan store; plugin
          composition does not expose arbitrary plugin state or external executor retention.
      records:
      - memory.md#mem-rte-local-memory
      - memory.md#mem-obj-bundle-metadata
      - memory.md#mem-rte-fact-extraction
      - epistemic.md#epi-rte-memory-disposition
      - epistemic.md#epi-rte-memory-commit
      - runtime.md#rt-rte-context-projection
      - memory.md#mem-obj-text-checkpoint
      - memory.md#mem-obj-provider-checkpoint
      - memory.md#mem-rte-index-maintenance
      - memory.md#mem-obj-index-cursors
      - memory.md#mem-rte-matter-state
      - memory.md#mem-obj-matter-reviews
      - memory.md#mem-rte-history-extract
      - memory.md#mem-obj-review-archive
      - epistemic.md#epi-rte-goal-selection
      - workflow.md#wf-rte-patch-publication
      - memory.md#mem-rte-session-import
      - memory.md#mem-bap-local-guidance
      - runtime.md#rt-rte-plugin-admission
      - runtime.md#rt-rte-executor-plugin
      note: Known computational transformations remain positive even though local manual/editor callers
        and other initial-content control are unresolved. No manual finding is licensed solely by user-labeled
        metadata.
    curation_operations:
      assessment: partial
      units:
      - scope: Local bundle lifecycle and replacement
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records: &id036
          - memory.md#mem-rte-local-memory
          - memory.md#mem-obj-bundle-metadata
          note: Archive/status changes withdraw subsequent prompt reliance without requiring physical
            erasure.
        - value: evolve
          basis: wired
          records: *id036
          note: Save/replace/restore mechanisms revise the retained document.
        records: *id036
        note: Archive preserves bodies/backups while withdrawing active projection; replacement revises
          retained content.
      - scope: Trace fact extraction
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id037
          - memory.md#mem-rte-fact-extraction
          - epistemic.md#epi-rte-memory-canonicalize
          note: Proposal/localization/canonicalization reduces retained conversational evidence to concise
            assertions.
        records: *id037
        note: The implemented target is durable extraction without added facts; possible semantic defects
          do not establish synthesis.
      - scope: Fact store versioned update/archive/restore capabilities
        assessment: partial
        findings:
        - value: evolve
          basis: afforded
          records:
          - memory.md#mem-obj-item-index
          note: Versioned updates afford revision of an existing MemoryItem.
        - value: invalidate
          basis: afforded
          records:
          - memory.md#mem-obj-item-index
          note: Archive affords withdrawal from active fact lookup while preserving the item.
        records:
        - memory.md#mem-obj-item-index
        note: The mutation capabilities are inspected, but end-to-end edit/withdrawal callers are not.
      - scope: Text summary and tool-body context pruning
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id038
          - runtime.md#rt-rte-context-projection
          - memory.md#mem-obj-text-checkpoint
          - memory.md#mem-rte-archive-read
          note: Covered effective history becomes a reduced retained continuation summary.
        - value: decay
          basis: wired
          records: *id038
          note: Oversized tool bodies/old history leave the effective context while ledger evidence remains
            reloadable.
        records: *id038
        note: Summarization and pruning affect retained effective context, not semantic truth acceptance.
      - scope: Provider-native opaque compaction
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-provider-checkpoint
        - runtime.md#rt-rte-context-projection
        note: The retained hidden representation is uninspected; a compaction name alone does not identify
          its semantic transformation.
      - scope: Index exact edits and body removal
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id039
          - memory.md#mem-rte-index-maintenance
          - memory.md#mem-obj-index-documents
          note: Exact edits and body writes revise existing index documents.
        - value: decay
          basis: wired
          records: *id039
          note: An empty body removes the retained index document.
        records: *id039
        note: Agent writes implement revision/removal; arbitrary free-form output does not by itself establish
          a new claim or faithful consolidation.
      - scope: Matter working-state revisions
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id040
          - memory.md#mem-rte-matter-state
          - memory.md#mem-obj-matter-state
          note: Later checkpoints/settlement revise the existing retained state.
        records: *id040
        note: The agent checkpoints/replaces a continuing task snapshot; review adds an admission gate,
          not a synthesis guarantee.
      - scope: Independent extraction and daily review generation
        assessment: partial
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-obj-review-archive
          note: Generated daily sections summarize retained local activity. With fallback status they
            are not certified complete summaries.
        records:
        - memory.md#mem-rte-history-extract
        - memory.md#mem-obj-review-archive
        note: Summarizing activity is established for daily review; arbitrary extraction requirements
          do not identify every transformation.
      - scope: Goal continuation, imported histories and worktree patch publication
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-rte-goal-selection
        - memory.md#mem-rte-session-import
        - workflow.md#wf-rte-patch-publication
        note: Generation of steering, source conversion and patch capture do not alone establish any controlled
          memory-curation operation. No bounded absence is declared.
      - scope: Remaining included Goal/Todo/plan/WorkHub state, Feishu cache lifecycle, changed skills/workspace
          guidance, plugin state and client-specific retained-state routes
        assessment: uninspected
        findings: []
        records:
        - epistemic.md#epi-rte-goal-selection
        - memory.md#mem-rte-index-maintenance
        - memory.md#mem-bap-local-guidance
        - runtime.md#rt-rte-plugin-admission
        - runtime.md#rt-rte-executor-plugin
        note: The accepted inventory leaves implemented retained-content transformations unresolved for
          these paths. Goal continuation findings below do not resolve every goal or plan store; plugin
          composition does not expose arbitrary plugin state or external executor retention.
      records:
      - memory.md#mem-rte-local-memory
      - memory.md#mem-obj-bundle-metadata
      - memory.md#mem-rte-fact-extraction
      - epistemic.md#epi-rte-memory-canonicalize
      - memory.md#mem-obj-item-index
      - runtime.md#rt-rte-context-projection
      - memory.md#mem-obj-text-checkpoint
      - memory.md#mem-rte-archive-read
      - memory.md#mem-obj-provider-checkpoint
      - memory.md#mem-rte-index-maintenance
      - memory.md#mem-obj-index-documents
      - memory.md#mem-rte-matter-state
      - memory.md#mem-obj-matter-state
      - memory.md#mem-rte-history-extract
      - memory.md#mem-obj-review-archive
      - epistemic.md#epi-rte-goal-selection
      - memory.md#mem-rte-session-import
      - workflow.md#wf-rte-patch-publication
      - memory.md#mem-bap-local-guidance
      - runtime.md#rt-rte-plugin-admission
      - runtime.md#rt-rte-executor-plugin
      note: Consolidation, revision, withdrawal and effective-context forgetting are locally supported.
        Deduplication of static workspace display and key-collision checks are not memory dedup; promotion
        or synthesis is not inferred from route names or arbitrary generation.
    read_back_direction:
      assessment: partial
      units:
      - scope: Local bundle foreground composition
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id041
          - memory.md#mem-rte-local-memory
          note: Composition automatically selects active/session-compatible bodies under policy and budget.
        records: *id041
        note: The model does not request these stored entries; the composer supplies eligible text.
      - scope: Requested fact/transcript/material and archived-tool-result retrieval
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id042
          - memory.md#mem-rte-recall-history
          - memory.md#mem-rte-archive-read
          note: Recall/RecallMore/RecallMaterial and Read return requested retained material.
        records: *id042
        note: Selection and delivery fulfill explicit consumer requests; delivery is not a second push.
      - scope: Checkpoint replay into later provider requests
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id043
          - runtime.md#rt-rte-context-projection
          - memory.md#mem-obj-text-checkpoint
          - memory.md#mem-obj-provider-checkpoint
          note: Replay machinery supplies a compatible retained checkpoint and selected tail without a
            model request for that checkpoint.
        records: *id043
        note: Text and opaque alternatives have different channels but automatic reuse is wired for both.
      - scope: Index navigation/body reads and continuation guidance
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id044
          - memory.md#mem-rte-index-maintenance
          - memory.md#mem-obj-index-cursors
          note: Agents explicitly request directories, keyed/full bodies, links and originals.
        - value: push
          basis: wired
          records: *id044
          note: Maintenance tasks automatically receive saved criterion/range/progress notes.
        records: *id044
        note: Separate operations in one chain need separate directions.
      - scope: Matter state and review replay
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id045
          - memory.md#mem-rte-matter-state
          - memory.md#mem-obj-matter-state
          - memory.md#mem-obj-matter-reviews
          note: MatterRead/file reading requests retained request/state/inbox material.
        - value: push
          basis: wired
          records: *id045
          note: Currentness/replay software automatically reads saved verdict and basis for settlement/recovery.
        records: *id045
        note: Wake paths are not body delivery; the documented workflow explicitly reads files.
      - scope: Goal next-turn continuation
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id046
          - epistemic.md#epi-rte-goal-selection
          note: The next goal admission consumes durable pending prompt/control state.
        records: *id046
        note: Persisted pending steering is selected by continuation machinery.
      - scope: Daily-review archive query, child output and patch artifact listing
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id047
          - memory.md#mem-obj-review-archive
          - runtime.md#rt-rte-child-graph
          - workflow.md#wf-rte-patch-publication
          note: Client archive queries and explicit child/output/artifact listing retrieve prior retained
            results.
        records: *id047
        note: These are recorded later requested reads, distinct from original immediate returns.
      - scope: Independent extraction-file full-body reuse and imported-session downstream history use
        assessment: partial
        findings:
        - value: pull
          basis: afforded
          records:
          - memory.md#mem-obj-extraction-files
          - memory.md#mem-rte-history-extract
          note: Ordinary file reading is afforded for saved extraction output, without a proven automatic
            adopter.
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-session-import
          note: A later Session/catalog read returns the published imported record, not necessarily all
            imported history.
        records:
        - memory.md#mem-rte-history-extract
        - memory.md#mem-obj-extraction-files
        - memory.md#mem-rte-session-import
        note: Files afford reading; imports expose a later catalog but exact history Recall/resume wiring
          is uninspected.
      - scope: Remaining included Goal/Todo/plan/WorkHub state, Feishu cache lifecycle, changed skills/workspace
          guidance, plugin state and client-specific retained-state routes
        assessment: uninspected
        findings: []
        records:
        - epistemic.md#epi-rte-goal-selection
        - memory.md#mem-rte-index-maintenance
        - memory.md#mem-bap-local-guidance
        - runtime.md#rt-rte-plugin-admission
        - runtime.md#rt-rte-executor-plugin
        note: The accepted inventory leaves later request/selection/delivery operations unresolved for
          these paths. Goal continuation findings below do not resolve every goal or plan store; plugin
          composition does not expose arbitrary plugin state or external executor retention.
      records:
      - memory.md#mem-rte-local-memory
      - memory.md#mem-rte-recall-history
      - memory.md#mem-rte-archive-read
      - runtime.md#rt-rte-context-projection
      - memory.md#mem-obj-text-checkpoint
      - memory.md#mem-obj-provider-checkpoint
      - memory.md#mem-rte-index-maintenance
      - memory.md#mem-obj-index-cursors
      - memory.md#mem-rte-matter-state
      - memory.md#mem-obj-matter-state
      - memory.md#mem-obj-matter-reviews
      - epistemic.md#epi-rte-goal-selection
      - memory.md#mem-obj-review-archive
      - runtime.md#rt-rte-child-graph
      - workflow.md#wf-rte-patch-publication
      - memory.md#mem-rte-history-extract
      - memory.md#mem-obj-extraction-files
      - memory.md#mem-rte-session-import
      - memory.md#mem-bap-local-guidance
      - runtime.md#rt-rte-plugin-admission
      - runtime.md#rt-rte-executor-plugin
      note: Both pull and push routes exist, but opaque external executor retention, imported-history
        consumers and other included paths leave the direction inventory incomplete.
    read_back_signal:
      assessment: partial
      units:
      - scope: Local bundle push selection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id048
          - memory.md#mem-rte-local-memory
          - memory.md#mem-obj-bundle-metadata
          note: Availability/policy/active status and prefix character budget filter the delivery.
        - value: identifier
          basis: wired
          records: *id048
          note: A real session-ID match selects session-scoped entries for delivery; this is not just
            an ID on a requested file.
        records: *id048
        note: Trigger is foreground composition; selector receives policy, lifecycle, session ID and a
          character cap, selecting eligible stored entry bodies.
      - scope: Checkpoint automatic reuse selection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id049
          - runtime.md#rt-rte-context-projection
          - memory.md#mem-obj-text-checkpoint
          - memory.md#mem-obj-provider-checkpoint
          note: Budget/prune policy and model/connection compatibility determine availability and reduced
            context.
        - value: identifier
          basis: wired
          records: *id049
          note: Coverage/head/source-prefix identity checks select the checkpoint matching the replay
            history. Hidden payload meaning remains unresolved.
        records: *id049
        note: Trigger is a later provider send; stored coverage/source identity and model compatibility
          select reusable checkpoint state, with context-budget pruning.
      - scope: Index maintenance continuation task
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id050
          - memory.md#mem-rte-index-maintenance
          - memory.md#mem-obj-index-cursors
          note: Index/worker/current range identity binds saved notes and coverage to the next maintenance
            task.
        - value: coarse
          basis: wired
          records: *id050
          note: Incomplete-range status determines whether the saved task continues.
        records: *id050
        note: Trigger is continued maintenance; exact index/range identity selects retained criterion/progress
          notes for that worker.
      - scope: Matter saved-review reuse
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id051
          - memory.md#mem-rte-matter-state
          - memory.md#mem-obj-matter-reviews
          note: Matching operation/submission/review-basis identity selects the saved review used by software.
        records: *id051
        note: Trigger is settlement replay/currentness handling; submission/fingerprint/revision identity
          selects the retained verdict, not every future narrative.
      - scope: Goal pending continuation admission
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id052
          - epistemic.md#epi-rte-goal-selection
          note: Current goal/lane checkpoint identity binds the retained pending prompt to the next turn.
        - value: coarse
          basis: wired
          records: *id052
          note: Active/waiting/terminal state gates continuation.
        records: *id052
        note: Trigger is later goal-turn admission; lane/checkpoint/control identity and current active/wait
          state select stored steering.
      - scope: Inspected requested Recall, archive Read, index body reads and daily/child queries
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-recall-history
        - memory.md#mem-rte-archive-read
        - memory.md#mem-rte-index-maintenance
        - memory.md#mem-obj-review-archive
        - runtime.md#rt-rte-child-graph
        - workflow.md#wf-rte-patch-publication
        note: 'These particular operations are pull: literal/key/address selection satisfies the consumer
          request. Their lexical ranking is not a push signal.'
      - scope: Independent extraction-file reuse and imported-history push alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-history-extract
        - memory.md#mem-rte-session-import
        note: No complete later full-body consumption inventory establishes pull-only use, so these alternatives
          cannot be declared inapplicable.
      - scope: Remaining included Goal/Todo/plan/WorkHub state, Feishu cache lifecycle, changed skills/workspace
          guidance, plugin state and client-specific retained-state routes
        assessment: uninspected
        findings: []
        records:
        - epistemic.md#epi-rte-goal-selection
        - memory.md#mem-rte-index-maintenance
        - memory.md#mem-bap-local-guidance
        - runtime.md#rt-rte-plugin-admission
        - runtime.md#rt-rte-executor-plugin
        note: The accepted inventory leaves automatic push selectors unresolved for these paths. Goal
          continuation findings below do not resolve every goal or plan store; plugin composition does
          not expose arbitrary plugin state or external executor retention.
      records:
      - memory.md#mem-rte-local-memory
      - memory.md#mem-obj-bundle-metadata
      - runtime.md#rt-rte-context-projection
      - memory.md#mem-obj-text-checkpoint
      - memory.md#mem-obj-provider-checkpoint
      - memory.md#mem-rte-index-maintenance
      - memory.md#mem-obj-index-cursors
      - memory.md#mem-rte-matter-state
      - memory.md#mem-obj-matter-reviews
      - epistemic.md#epi-rte-goal-selection
      - memory.md#mem-rte-recall-history
      - memory.md#mem-rte-archive-read
      - memory.md#mem-obj-review-archive
      - runtime.md#rt-rte-child-graph
      - workflow.md#wf-rte-patch-publication
      - memory.md#mem-rte-history-extract
      - memory.md#mem-rte-session-import
      - memory.md#mem-bap-local-guidance
      - runtime.md#rt-rte-plugin-admission
      - runtime.md#rt-rte-executor-plugin
      note: Identifier and coarse selection are established on actual pushes. Recall lexical matching
        is not relabeled inferred-lexical push; remaining branches prevent a system-wide pull-only or
        complete signal assessment.
    trace_learning:
      assessment: partial
      units:
      - scope: Runtime fact extraction to later Recall
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id053
          - memory.md#mem-rte-fact-extraction
          - memory.md#mem-obj-memory-item
          - memory.md#mem-rte-recall-history
          - epistemic.md#epi-rte-memory-disposition
          note: Automatic conversational-evidence extraction commits MemoryItems that later Recall can
            supply to a model.
        records: *id053
        note: Trace-fed model/software writes create durable behavior-shaping fact context and an implemented
          later consumer.
      - scope: Text history compaction to later provider invocation
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id054
          - runtime.md#rt-rte-context-projection
          - memory.md#mem-obj-text-checkpoint
          note: Automatic history summarization persists a checkpoint later replayed as context.
        records: *id054
        note: A generated continuation summary qualifies even within the same run; benefit and new knowledge
          are unnecessary.
      - scope: Provider checkpoint alternative
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-provider-checkpoint
        - runtime.md#rt-rte-context-projection
        note: Automatic durable history-fed production and replay are wired, but hidden payload semantics
          do not establish whether it is a qualifying behavior-shaping artifact rather than opaque transport
          alone.
      - scope: Index maintenance trace-derived documents and progress
        assessment: partial
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-index-maintenance
          - memory.md#mem-obj-index-documents
          - memory.md#mem-obj-index-cursors
          note: Automatic maintenance retains history-derived index text and progress for later agents.
        records:
        - memory.md#mem-rte-index-maintenance
        - memory.md#mem-obj-index-documents
        - memory.md#mem-obj-index-cursors
        note: History-fed document writes and later readers qualify; arbitrary remote sources and other
          authoring paths remain unresolved.
      - scope: Matter revised task state and review loop
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id055
          - memory.md#mem-rte-matter-state
          - memory.md#mem-obj-matter-state
          - memory.md#mem-obj-matter-reviews
          note: Automatic checkpoints/settlement retain experience-shaped task context for a later activation.
        records: *id055
        note: Execution/inbox experience feeds computationally admitted snapshots; later activations read
          state. Review-journal future narrative use remains narrower than state use.
      - scope: Goal reason-derived durable steering
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id056
          - epistemic.md#epi-rte-goal-selection
          - epistemic.md#epi-rte-goal-judge
          note: Recent conversation feeds a judgment whose derived prompt is retained and consumed on
            a later goal turn.
        records: *id056
        note: The inspected continuation path, not all Goal persistence, is classified.
      - scope: Independent extraction files, daily-review archives and patch results
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-history-extract
        - memory.md#mem-obj-extraction-files
        - memory.md#mem-obj-review-archive
        - workflow.md#wf-rte-patch-publication
        note: 'Automatic trace/history generation and retention alone do not establish a durable behavior-shaping
          later consumer for every product: full extraction adoption, archive-to-agent revision and parent
          patch application are uninspected.'
      - scope: Local authored bundle and imported history admission alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-local-memory
        - memory.md#mem-rte-session-import
        note: The records do not establish complete trace-fed proposal origins and later imported-history
          use. Authored/manual labels and raw-log import neither prove qualifying learning nor warrant
          no.
      - scope: Remaining included Goal/Todo/plan/WorkHub state, Feishu cache lifecycle, changed skills/workspace
          guidance, plugin state and client-specific retained-state routes
        assessment: uninspected
        findings: []
        records:
        - epistemic.md#epi-rte-goal-selection
        - memory.md#mem-rte-index-maintenance
        - memory.md#mem-bap-local-guidance
        - runtime.md#rt-rte-plugin-admission
        - runtime.md#rt-rte-executor-plugin
        note: The accepted inventory leaves qualifying automatic trace-fed writes and later consumers
          unresolved for these paths. Goal continuation findings below do not resolve every goal or plan
          store; plugin composition does not expose arbitrary plugin state or external executor retention.
      records:
      - memory.md#mem-rte-fact-extraction
      - memory.md#mem-obj-memory-item
      - memory.md#mem-rte-recall-history
      - epistemic.md#epi-rte-memory-disposition
      - runtime.md#rt-rte-context-projection
      - memory.md#mem-obj-text-checkpoint
      - memory.md#mem-obj-provider-checkpoint
      - memory.md#mem-rte-index-maintenance
      - memory.md#mem-obj-index-documents
      - memory.md#mem-obj-index-cursors
      - memory.md#mem-rte-matter-state
      - memory.md#mem-obj-matter-state
      - memory.md#mem-obj-matter-reviews
      - epistemic.md#epi-rte-goal-selection
      - epistemic.md#epi-rte-goal-judge
      - memory.md#mem-rte-history-extract
      - memory.md#mem-obj-extraction-files
      - memory.md#mem-obj-review-archive
      - workflow.md#wf-rte-patch-publication
      - memory.md#mem-rte-local-memory
      - memory.md#mem-rte-session-import
      - memory.md#mem-bap-local-guidance
      - runtime.md#rt-rte-plugin-admission
      - runtime.md#rt-rte-executor-plugin
      note: Several wired yes routes establish architectural trace learning, not improved capacity or
        exercised behavior. No local or global no is asserted without bounded absence evidence; unresolved
        opaque and alternate writes remain included.
    trace_source:
      assessment: partial
      units:
      - scope: Qualifying fact extraction inputs
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id057
          - memory.md#mem-rte-fact-extraction
          - epistemic.md#epi-rte-memory-evidence
          - epistemic.md#epi-rte-memory-canonicalize
          note: Conversational user/agent text supplies the eligible evidence and interpretation context.
        records: *id057
        note: Canonical evidence is user-authored session quotes; interpretation context is normalized
          conversational history/prior textual checkpoint. RuntimeEvent serialization is not a new source
          category.
      - scope: Qualifying text-checkpoint compaction inputs
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id058
          - runtime.md#rt-rte-context-projection
          - memory.md#mem-obj-text-checkpoint
          note: Covered conversational turns feed the continuation summary.
        - value: tool-traces
          basis: wired
          records: *id058
          note: Recorded tool results in effective history feed compaction.
        records: *id058
        note: Covered effective history includes messages and tool-result bodies; a summary/checkpoint
          wrapper does not change original origin.
      - scope: Provider checkpoint potential trace-fed input
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-provider-checkpoint
        - runtime.md#rt-rte-context-projection
        note: The write has history inputs, but qualification of its hidden result is unresolved; do not
          aggregate a trace-source value for an unestablished qualifying artifact.
      - scope: Qualifying assistant index maintenance inputs
        assessment: partial
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-rte-index-maintenance
          - memory.md#mem-obj-index-documents
          note: Accessible Maka session histories feed index organization and later document reads.
        records:
        - memory.md#mem-rte-index-maintenance
        - memory.md#mem-obj-index-documents
        - memory.md#mem-obj-index-cursors
        note: Maka histories support session origin; all remote original source types and mixed tool/environment
          content remain unclassified.
      - scope: Qualifying Matter state update inputs
        assessment: partial
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-rte-matter-state
          - memory.md#mem-obj-matter-reviews
          note: Recorded task conversation/execution transcript and user amendments feed continuing task-state/review
            updates.
        records:
        - memory.md#mem-rte-matter-state
        - memory.md#mem-obj-matter-state
        - memory.md#mem-obj-matter-reviews
        note: Objective amendments, inbox and execution history participate; precise original types for
          all inbox/other execution evidence are not enumerated.
      - scope: Qualifying goal-continuation inputs
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id059
          - epistemic.md#epi-rte-goal-judge
          - epistemic.md#epi-rte-goal-selection
          note: Recent conversational turns feed the persisted reason-derived steering.
        records: *id059
        note: The judge explicitly uses a six-message user/assistant text projection, not independently
          executed tools.
      - scope: Extraction files, daily archives, local proposals, imported histories and patch products
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-history-extract
        - memory.md#mem-obj-review-archive
        - memory.md#mem-rte-local-memory
        - memory.md#mem-rte-session-import
        - workflow.md#wf-rte-patch-publication
        note: Their qualifying trace-learning routes or exact later behavior-shaping consumers remain
          unresolved; no trace-source union or inapplicability is inferred solely from generation/import.
      - scope: Remaining included Goal/Todo/plan/WorkHub state, Feishu cache lifecycle, changed skills/workspace
          guidance, plugin state and client-specific retained-state routes
        assessment: uninspected
        findings: []
        records:
        - epistemic.md#epi-rte-goal-selection
        - memory.md#mem-rte-index-maintenance
        - memory.md#mem-bap-local-guidance
        - runtime.md#rt-rte-plugin-admission
        - runtime.md#rt-rte-executor-plugin
        note: The accepted inventory leaves original source content of qualifying updates unresolved for
          these paths. Goal continuation findings below do not resolve every goal or plan store; plugin
          composition does not expose arbitrary plugin state or external executor retention.
      records:
      - memory.md#mem-rte-fact-extraction
      - epistemic.md#epi-rte-memory-evidence
      - epistemic.md#epi-rte-memory-canonicalize
      - runtime.md#rt-rte-context-projection
      - memory.md#mem-obj-text-checkpoint
      - memory.md#mem-obj-provider-checkpoint
      - memory.md#mem-rte-index-maintenance
      - memory.md#mem-obj-index-documents
      - memory.md#mem-obj-index-cursors
      - memory.md#mem-rte-matter-state
      - memory.md#mem-obj-matter-state
      - memory.md#mem-obj-matter-reviews
      - epistemic.md#epi-rte-goal-judge
      - epistemic.md#epi-rte-goal-selection
      - memory.md#mem-rte-history-extract
      - memory.md#mem-obj-review-archive
      - memory.md#mem-rte-local-memory
      - memory.md#mem-rte-session-import
      - workflow.md#wf-rte-patch-publication
      - memory.md#mem-bap-local-guidance
      - runtime.md#rt-rte-plugin-admission
      - runtime.md#rt-rte-executor-plugin
      note: Session logs and tool traces are supported on named qualifying writes. Runtime event wrappers
        do not add event-streams; no linked state/action/outcome experience warrant establishes trajectories.
        Mixed originals and unestablished qualifying alternatives prevent complete source coverage.
---

# Apache Maka memory profile

## Comparison rationale

### Accepted records and scope

This profile classifies the accepted record inventory, not the whole runtime's
storage or capability surface. Each axis is partial because its named inventory
retains unresolved included paths. Known local units do not establish complete
whole-system coverage. Implementation is wired, not observed use or benefit.
The retained-state inventory and its gaps are supplied by
[MEM-RTE-local-memory](memory.md#mem-rte-local-memory),
[MEM-RTE-index-maintenance](memory.md#mem-rte-index-maintenance),
[RT-RTE-executor-plugin](runtime.md#rt-rte-executor-plugin) and
[RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission).

The reconciliation supersedes EPI-RTE-local-memory-use with
[MEM-RTE-local-memory](memory.md#mem-rte-local-memory); all corresponding route
classifications cite that canonical record. It leaves bundle/item containers
alongside their more precise parts. No other supersession changes these values.

### Parts, provenance and admission

[MEM-OBJ-text-checkpoint](memory.md#mem-obj-text-checkpoint) and
[MEM-OBJ-provider-checkpoint](memory.md#mem-obj-provider-checkpoint) are alternative
outputs of [RT-RTE-context-projection](runtime.md#rt-rte-context-projection).
The text branch establishes summary form and consolidation; it cannot classify
the hidden provider payload. Neither checkpoint's writer seam establishes its
physical storage. A visible wrapper can support symbolic compatibility routing
while leaving payload form and downstream force unresolved.

[MEM-OBJ-bundle-metadata](memory.md#mem-obj-bundle-metadata) records manual/editor
surfaces and user-labeled approval, but not a human decision at every caller.
The write-agency unit therefore remains not-determinable, without deleting the
independently automatic fact, checkpoint, index and Matter admissions.
[EPI-RTE-memory-canonicalize](epistemic.md#epi-rte-memory-canonicalize) supplies a
fallible evidence-consuming support criterion; it is not an external truth
oracle. Consolidation follows the implemented extraction target, not a claim
that every output faithfully preserves every source assertion. Arbitrary index
writing supports authored lineage and evolution; it does not alone prove
synthesis of a proposition absent from the inputs.

### Consumers, direction and trace-fed updates

[MEM-RTE-recall-history](memory.md#mem-rte-recall-history) is request-driven even
though its code ranks literal matches. Its lexical selection does not establish
an inferred-lexical push signal. In contrast,
[MEM-RTE-local-memory](memory.md#mem-rte-local-memory) automatically supplies
active/session-matched entries at composition: coarse filtering and actual
session-identity matching both matter. A requested Read address and a Matter
wake's file paths do not by themselves establish identifier-based body push.
Saved review reuse has its own software consumer, distinct from later reading
of the feedback narrative in [MEM-RTE-matter-state](memory.md#mem-rte-matter-state).

Learning authority is attached to recorded experience where it feeds durable
updates; knowledge or instruction describes the downstream retained result.
[MEM-RTE-fact-extraction](memory.md#mem-rte-fact-extraction) and textual
[RT-RTE-context-projection](runtime.md#rt-rte-context-projection) establish
qualifying automatic trace-fed writes and later model consumption without
establishing improved capacity. The narrower
[EPI-RTE-goal-selection](epistemic.md#epi-rte-goal-selection) likewise retains
conversation-derived next-turn steering; it closes part of the memory report's
goal inspection gap, not all Goal/Todo/WorkHub coverage.

[MEM-RTE-history-extract](memory.md#mem-rte-history-extract) saves files and returns
a preview without establishing automatic full-body adoption.
[MEM-OBJ-review-archive](memory.md#mem-obj-review-archive) establishes a later
client query, not autonomous behavior revision.
[WF-RTE-patch-publication](workflow.md#wf-rte-patch-publication) establishes
retained patch publication and later listing, not parent application. These
limits prevent inferring qualifying trace learning for every generated product.
No absence record supports a global no or an absent curation value.

Original content, not serialization, determines trace source. User messages
used by fact canonicalization remain session logs; runtime-event wrappers are
not independent environmental event streams. Text compaction also consumes
recorded tool results. Index and Matter mixed originals retain source uncertainty
rather than acquiring an event-stream or trajectory label from their subsystem
names. See [EPI-RTE-memory-evidence](epistemic.md#epi-rte-memory-evidence),
[RT-RTE-context-projection](runtime.md#rt-rte-context-projection) and
[MEM-RTE-index-maintenance](memory.md#mem-rte-index-maintenance).

### Source reads

No source files were read for this profile. All classifications and limitations
use the supplied accepted records and their retained evidence passages. No new
records, quotations or evidence are introduced.
