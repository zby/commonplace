---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: Talorys memory comparison of retained personal information, conversation summaries, semantic
  access indexes and routine/approval state
run-id: AAS-2026-10-15-talorys-7bce41ba9401-01
source-identity: https://github.com/rociiu/talorys
reviewed-boundary: c5da440010402ed4c1b9789ae22eab96a8f0f379
memory-comparison:
  version: 2
  scope: Application-retained personal facts and lifecycle/review state; conversation messages, activity
    and generated summary/cutoff; saved tasks, notes and automation instructions/dispatch state; deferred
    action payloads/status; memory/item vectors and their metadata/caches; their admission, maintenance
    and later model/owner/update consumers. Excludes shipped static policy/tool definitions, general runtime
    settings/auth/budget counters, transient active-run controllers, deployment artifacts, external provider
    parameters/private retention and ordinary current-turn tool accumulation. Notifications/receipts are
    included only as owner-readable retained results and recorded action feedback, not assumed recurrent
    model-training inputs.
  axes:
    storage_substrate:
      assessment: known
      units:
      - scope: Personal facts and lifecycle metadata; conflict-review queue
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-tal-memories
          - memory.md#mem-obj-memory-reviews
          note: Fact rows, links, status and review reasons persist in owner-bound Durable Object SQLite.
        records:
        - memory.md#mem-obj-tal-memories
        - memory.md#mem-obj-memory-reviews
        note: Both content and its access metadata have inspected app-level stores.
      - scope: Conversation messages, activity display records, summary and summary cutoff
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-conversation-records
          - memory.md#mem-obj-conversation-summary
          note: Raw and derived conversation parts are separate SQLite content/metadata.
        records:
        - memory.md#mem-obj-conversation-records
        - memory.md#mem-obj-conversation-summary
        note: The summary is retained by value; no alternative app checkpoint is shown.
      - scope: Memory and task/note/automation semantic indexes
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-obj-semantic-vectors
          - memory.md#mem-obj-item-vectors
          note: Normalized Float32 BLOBs and symbolic index metadata persist in SQLite.
        - value: vector
          basis: wired
          records:
          - memory.md#mem-obj-semantic-vectors
          - memory.md#mem-obj-item-vectors
          - memory.md#mem-rte-index-maintenance
          note: The retained numerical stores implement cosine retrieval and neighbor nomination.
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-semantic-vectors
          - memory.md#mem-obj-item-vectors
          note: Decoded per-database caches retain derived vectors for subsequent scans in that instance.
        records:
        - memory.md#mem-obj-semantic-vectors
        - memory.md#mem-obj-item-vectors
        - memory.md#mem-rte-index-maintenance
        note: Vector describes the operative retrieval store, not an inference-model weight update; decoded
          caches are separate from durable rows.
      - scope: Saved tasks, notes, routine prompts/dispatch state, and deferred approval objects
        assessment: known
        findings:
        - value: sqlite
          basis: wired
          records:
          - runtime.md#rt-rte-owner-changes
          - runtime.md#rt-rte-scheduled-work
          - runtime.md#rt-obj-pending-actions
          - runtime.md#rt-rte-action-approval
          note: Owner-bound retained source objects and pending-action records use the application SQLite
            store.
        records:
        - runtime.md#rt-rte-owner-changes
        - runtime.md#rt-rte-scheduled-work
        - runtime.md#rt-obj-pending-actions
        - runtime.md#rt-rte-action-approval
        - memory.md#mem-rte-item-recall
        note: Shipped edit, scheduled, approval and later-read routes cover these additional retained
          surfaces.
      records:
      - memory.md#mem-obj-tal-memories
      - memory.md#mem-obj-memory-reviews
      - memory.md#mem-obj-conversation-records
      - memory.md#mem-obj-conversation-summary
      - memory.md#mem-obj-semantic-vectors
      - memory.md#mem-obj-item-vectors
      - memory.md#mem-rte-index-maintenance
      - runtime.md#rt-rte-owner-changes
      - runtime.md#rt-rte-scheduled-work
      - runtime.md#rt-obj-pending-actions
      - runtime.md#rt-rte-action-approval
      - memory.md#mem-rte-item-recall
      note: The scoped application inventory has SQLite source stores and vector access stores with decoded
        in-memory caches. External service weights, provider-private state, deployment files and runtime-only
        active controllers are excluded, not classified as application memory.
    representational_form:
      assessment: known
      units:
      - scope: Fact wording, review reasons, conversation text, summary, saved note/task wording, automation
          instruction and approval preview
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-tal-memories
          - memory.md#mem-obj-memory-reviews
          - memory.md#mem-obj-conversation-records
          - memory.md#mem-obj-conversation-summary
          - runtime.md#rt-bap-retained-context
          - runtime.md#rt-obj-pending-actions
          note: Owners and models interpret retained prose; routine prompts supply task wording while
            other recalled text supplies data.
        records:
        - memory.md#mem-obj-tal-memories
        - memory.md#mem-obj-memory-reviews
        - memory.md#mem-obj-conversation-records
        - memory.md#mem-obj-conversation-summary
        - runtime.md#rt-bap-retained-context
        - runtime.md#rt-obj-pending-actions
        note: Prose consumption is distinct from fixed metadata rules.
      - scope: Fact lifecycle/category/IDs, message role/origin/status/activity, summary cutoff, approval
          target/hash/payload and routine dispatch fields
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-tal-memories
          - memory.md#mem-obj-conversation-records
          - memory.md#mem-obj-conversation-summary
          - runtime.md#rt-obj-pending-actions
          - runtime.md#rt-rte-action-approval
          - runtime.md#rt-rte-scheduled-work
          note: Localized metadata controls selection, omission, dispatch or commit; structured payload
            content remains separately interpreted as prose.
        records:
        - memory.md#mem-obj-tal-memories
        - memory.md#mem-obj-conversation-records
        - memory.md#mem-obj-conversation-summary
        - runtime.md#rt-obj-pending-actions
        - runtime.md#rt-rte-action-approval
        - runtime.md#rt-rte-scheduled-work
        note: An owner-readable preview does not stand in for the consumed structured approval payload.
      - scope: Dense memory/item vector payloads
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-semantic-vectors
          - memory.md#mem-obj-item-vectors
          note: Distributed dense numerical representations are consumed by cosine scoring, not read as
            natural-language facts.
        records:
        - memory.md#mem-obj-semantic-vectors
        - memory.md#mem-obj-item-vectors
        note: These are derived representations, not learned provider parameters.
      - scope: Vector access metadata
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-semantic-vectors
          - memory.md#mem-obj-item-vectors
          - memory.md#mem-rte-index-maintenance
          note: Model/dimensions/hash/stamp/part IDs govern validity checks, source reload and pending
            repair.
        records:
        - memory.md#mem-obj-semantic-vectors
        - memory.md#mem-obj-item-vectors
        - memory.md#mem-rte-index-maintenance
        note: Numerical payload and localized metadata have separate consumer rules.
      records:
      - memory.md#mem-obj-tal-memories
      - memory.md#mem-obj-memory-reviews
      - memory.md#mem-obj-conversation-records
      - memory.md#mem-obj-conversation-summary
      - runtime.md#rt-bap-retained-context
      - runtime.md#rt-obj-pending-actions
      - runtime.md#rt-rte-action-approval
      - runtime.md#rt-rte-scheduled-work
      - memory.md#mem-obj-semantic-vectors
      - memory.md#mem-obj-item-vectors
      - memory.md#mem-rte-index-maintenance
      note: The inventory contains natural-language, symbolic and distributed numerical parts; prompt
        delivery does not create an additional form.
    lineage:
      assessment: partial
      units:
      - scope: Owner/model-authored current facts, task/note content and stored routines
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-rte-memory-write
          - runtime.md#rt-rte-owner-chat
          - runtime.md#rt-rte-scheduled-work
          note: Owners supply content and models author retained fact/work/routine wording through the
            shipped writes.
        records:
        - memory.md#mem-rte-memory-write
        - runtime.md#rt-rte-owner-chat
        - runtime.md#rt-rte-scheduled-work
        - epistemic.md#epi-obj-generated-text
        note: Authored describes the recorded creation path, not independent truth or complete initial
          provenance.
      - scope: Backup-admitted facts, messages and saved items
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records:
          - runtime.md#rt-rte-owner-changes
          note: Backup merge admits external retained content under schema/timestamp/link fences.
        records:
        - runtime.md#rt-rte-owner-changes
        - memory.md#mem-obj-tal-memories
        - memory.md#mem-obj-conversation-records
        note: Imported path is known. Original authorship and prior derivation inside a selected backup
          remain unresolved.
      - scope: Conversation summary and remembered facts extracted from live conversational input
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-rte-context-window
          - memory.md#mem-obj-conversation-summary
          - memory.md#mem-rte-memory-write
          note: The summary condenses owner/assistant history; remember extracts lasting owner facts from
            conversational input.
        records:
        - runtime.md#rt-rte-context-window
        - memory.md#mem-obj-conversation-summary
        - memory.md#mem-rte-memory-write
        - memory.md#mem-obj-conversation-records
        note: Both raw-to-summary and chat-to-fact derivations are wired; no fidelity or improvement is
          inferred.
      - scope: Vectors, lifecycle/review metadata and approval/dispatch records
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-rte-index-maintenance
          - memory.md#mem-obj-semantic-vectors
          - memory.md#mem-obj-item-vectors
          - memory.md#mem-rte-memory-write
          - memory.md#mem-obj-memory-reviews
          - runtime.md#rt-rte-action-approval
          - runtime.md#rt-rte-scheduled-work
          note: Code/model transformations derive numerical indexes, diagnoses and structured control
            state from admitted content and actions.
        records:
        - memory.md#mem-rte-index-maintenance
        - memory.md#mem-obj-semantic-vectors
        - memory.md#mem-obj-item-vectors
        - memory.md#mem-rte-memory-write
        - memory.md#mem-obj-memory-reviews
        - runtime.md#rt-rte-action-approval
        - runtime.md#rt-rte-scheduled-work
        note: The application derivations are inspected. Embedding producer weight provenance is outside
          the retained-output boundary.
      records:
      - memory.md#mem-rte-memory-write
      - runtime.md#rt-rte-owner-chat
      - runtime.md#rt-rte-scheduled-work
      - epistemic.md#epi-obj-generated-text
      - runtime.md#rt-rte-owner-changes
      - memory.md#mem-obj-tal-memories
      - memory.md#mem-obj-conversation-records
      - runtime.md#rt-rte-context-window
      - memory.md#mem-obj-conversation-summary
      - memory.md#mem-rte-index-maintenance
      - memory.md#mem-obj-semantic-vectors
      - memory.md#mem-obj-item-vectors
      - memory.md#mem-obj-memory-reviews
      - runtime.md#rt-rte-action-approval
      note: Known admission and derivation paths coexist with unknown pre-import provenance. Source tags
        do not reconstruct original claim authors or derivations, so the lineage inventory is partial.
    behavioral_authority:
      assessment: known
      units:
      - scope: Selected fact/note/task text, conversation history/summary and review explanations at information
          consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - runtime.md#rt-bap-retained-context
          - memory.md#mem-rte-memory-recall
          - memory.md#mem-rte-item-recall
          - memory.md#mem-rte-requested-search
          - memory.md#mem-obj-conversation-records
          - memory.md#mem-obj-conversation-summary
          - memory.md#mem-obj-memory-reviews
          note: Later models use selected content as information; owner review displays use saved pair
            text and reasons as advice.
        records:
        - runtime.md#rt-bap-retained-context
        - memory.md#mem-rte-memory-recall
        - memory.md#mem-rte-item-recall
        - memory.md#mem-rte-requested-search
        - memory.md#mem-obj-conversation-records
        - memory.md#mem-obj-conversation-summary
        - memory.md#mem-obj-memory-reviews
        note: Data-not-instructions is intended consumer force, not demonstrated provider compliance.
      - scope: Stored automation message at scheduled model
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - runtime.md#rt-rte-scheduled-work
          - runtime.md#rt-bap-retained-context
          note: The saved routine message becomes the scheduled user task instruction.
        records:
        - runtime.md#rt-rte-scheduled-work
        - runtime.md#rt-bap-retained-context
        note: This is across-run guidance, unlike the informational recall section.
      - scope: Retained session text and prior summary at automatic fact/summary update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - runtime.md#rt-rte-context-window
          - memory.md#mem-obj-conversation-summary
          - memory.md#mem-rte-memory-write
          - memory.md#mem-obj-conversation-records
          note: Recorded conversational experience and prior summary feed automatic durable facts or summary
            text consumed on later turns.
        records:
        - runtime.md#rt-rte-context-window
        - memory.md#mem-obj-conversation-summary
        - memory.md#mem-rte-memory-write
        - memory.md#mem-obj-conversation-records
        note: Learning authority names the update input force; it does not assert improved capacity or
          parameter training.
      - scope: Retained fact text, dates/preferences and semantic payloads at rankers
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-rte-memory-recall
          - memory.md#mem-rte-requested-search
          - memory.md#mem-obj-semantic-vectors
          - memory.md#mem-obj-item-vectors
          - memory.md#mem-rte-item-recall
          note: Lexical text, recency and stored dense representations affect relative retrieval priority.
        records:
        - memory.md#mem-rte-memory-recall
        - memory.md#mem-rte-requested-search
        - memory.md#mem-obj-semantic-vectors
        - memory.md#mem-obj-item-vectors
        - memory.md#mem-rte-item-recall
        note: Fixed scoring code still consumes retained ranking inputs.
      - scope: Lifecycle/status and existence controls at recall; pending status/expiry/hash at approval
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-rte-memory-recall
          - memory.md#mem-rte-item-recall
          - runtime.md#rt-rte-action-approval
          note: Status/live-row predicates suppress delivery, and pending/unexpired/snapshot conditions
            refuse stale or resolved commits.
        - value: validation
          basis: wired
          records:
          - runtime.md#rt-rte-action-approval
          - runtime.md#rt-obj-pending-actions
          note: Stored target/version/status provide criteria against which an approval candidate and
            current target are checked.
        records:
        - memory.md#mem-rte-memory-recall
        - memory.md#mem-rte-item-recall
        - runtime.md#rt-rte-action-approval
        - runtime.md#rt-obj-pending-actions
        note: Eligibility veto is not a universal truth gate or historical-data erasure. Snapshot validation
          applies to approval, not every write.
      - scope: Summary cutoff, successor links, vector metadata and stored routine dispatch fields
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-rte-context-window
          - memory.md#mem-obj-conversation-summary
          - memory.md#mem-rte-memory-recall
          - memory.md#mem-rte-index-maintenance
          - runtime.md#rt-rte-scheduled-work
          note: Cutoff selects the next history window; links select predecessors/successors; metadata
            selects repair/reload work; routine state selects later scheduled work.
        records:
        - runtime.md#rt-rte-context-window
        - memory.md#mem-obj-conversation-summary
        - memory.md#mem-rte-memory-recall
        - memory.md#mem-rte-index-maintenance
        - runtime.md#rt-rte-scheduled-work
        note: Only fields consumed by actual operations are assigned force; inert provenance labels receive
          none.
      records:
      - runtime.md#rt-bap-retained-context
      - memory.md#mem-rte-memory-recall
      - memory.md#mem-rte-item-recall
      - memory.md#mem-rte-requested-search
      - memory.md#mem-obj-conversation-records
      - memory.md#mem-obj-conversation-summary
      - memory.md#mem-obj-memory-reviews
      - runtime.md#rt-rte-scheduled-work
      - runtime.md#rt-rte-context-window
      - memory.md#mem-rte-memory-write
      - memory.md#mem-obj-semantic-vectors
      - memory.md#mem-obj-item-vectors
      - runtime.md#rt-rte-action-approval
      - runtime.md#rt-obj-pending-actions
      - memory.md#mem-rte-index-maintenance
      note: Authority follows each actual consumer. Information, routine guidance, trace-fed update inputs,
        ranking features, eligibility vetoes, approval criteria and routing metadata have different forces.
    write_agency:
      assessment: known
      units:
      - scope: Immediate model memory/task/note/routine writes and model corrections
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-memory-write
          - runtime.md#rt-rte-owner-chat
          - runtime.md#rt-rte-scheduled-work
          note: Software/model admits content without an explicit per-content owner decision; starting
            chat or enabling autoMemory is not approval.
        records:
        - memory.md#mem-rte-memory-write
        - runtime.md#rt-rte-owner-chat
        - runtime.md#rt-rte-scheduled-work
        note: Ordinary model correction can retire a predecessor without an approval card.
      - scope: Owner manual supply/edit/correct/status/review and exact destructive proposal approval
        assessment: known
        findings:
        - value: manual
          basis: wired
          records:
          - memory.md#mem-rte-memory-write
          - memory.md#mem-obj-memory-reviews
          - runtime.md#rt-rte-owner-changes
          - runtime.md#rt-rte-action-approval
          note: The owner supplies or edits a specific item, chooses a review disposition, or approves
            the exact saved proposal body.
        records:
        - memory.md#mem-rte-memory-write
        - memory.md#mem-obj-memory-reviews
        - runtime.md#rt-rte-owner-changes
        - runtime.md#rt-rte-action-approval
        note: The decision is content-specific, even though code performs persistence; actual owner decisions
          are unobserved.
      - scope: Automatic summary, derived index, rule/Clef review and lifecycle maintenance writes
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-context-window
          - memory.md#mem-rte-index-maintenance
          - memory.md#mem-rte-memory-write
          - memory.md#mem-obj-memory-reviews
          note: Overflow/model return, index derivation, diagnosis and confident Clef retirement are admitted
            by code without per-result owner approval.
        records:
        - runtime.md#rt-rte-context-window
        - memory.md#mem-rte-index-maintenance
        - memory.md#mem-rte-memory-write
        - memory.md#mem-obj-memory-reviews
        note: Configuration opt-in does not change subsequent automatic admission.
      - scope: Backup selection and per-field merge
        assessment: known
        findings:
        - value: manual
          basis: wired
          records:
          - runtime.md#rt-rte-owner-changes
          note: The owner explicitly selects the retained-content backup file for import.
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-owner-changes
          note: Software applies schema, timestamp, link and field rules to admit its individual rows
            without individual owner review.
        records:
        - runtime.md#rt-rte-owner-changes
        note: File-level human selection and row-level merge are separate mechanisms, not evidence of
          manual factual review of every row.
      - scope: Raw turn/activity persistence and scheduled receipts
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-owner-chat
          - memory.md#mem-obj-conversation-records
          - runtime.md#rt-rte-scheduled-work
          - runtime.md#rt-rte-action-approval
          note: Host code retains turn/status/activity and scheduled results as consequences of execution.
        records:
        - runtime.md#rt-rte-owner-chat
        - memory.md#mem-obj-conversation-records
        - runtime.md#rt-rte-scheduled-work
        - runtime.md#rt-rte-action-approval
        note: User authorship of a message is separate from automatic host logging admission.
      records:
      - memory.md#mem-rte-memory-write
      - runtime.md#rt-rte-owner-chat
      - runtime.md#rt-rte-scheduled-work
      - memory.md#mem-obj-memory-reviews
      - runtime.md#rt-rte-owner-changes
      - runtime.md#rt-rte-action-approval
      - runtime.md#rt-rte-context-window
      - memory.md#mem-rte-index-maintenance
      - memory.md#mem-obj-conversation-records
      note: The included admission mechanisms separate human content decisions from software/model decisions
        and from physical I/O.
    curation_operations:
      assessment: partial
      units:
      - scope: Repeated current personal-memory wording
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records:
          - memory.md#mem-rte-memory-write
          - memory.md#mem-obj-tal-memories
          note: Case-insensitive matching current wording reuses/refreshes the existing row rather than
            adding another.
        records:
        - memory.md#mem-rte-memory-write
        - memory.md#mem-obj-tal-memories
        note: This is content deduplication, not merely primary-key collision handling.
      - scope: Personal-fact and note revisions
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-rte-memory-write
          - runtime.md#rt-rte-owner-changes
          - runtime.md#rt-rte-action-approval
          note: Owner PATCH changes fact wording; explicit correction supplies a successor; approved rewrite
            changes an existing note.
        records:
        - memory.md#mem-rte-memory-write
        - runtime.md#rt-rte-owner-changes
        - runtime.md#rt-rte-action-approval
        note: History-preserving correction and in-place edit have different retained reasons/history.
      - scope: Historical lifecycle withdrawal
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records:
          - memory.md#mem-rte-memory-write
          - memory.md#mem-obj-tal-memories
          note: Correction, owner historical disposition or confident Clef supersession withdraws ordinary
            current reliance while retaining predecessor text.
        records:
        - memory.md#mem-rte-memory-write
        - memory.md#mem-obj-tal-memories
        - memory.md#mem-rte-memory-recall
        - memory.md#mem-rte-requested-search
        note: Requested search can still expose historical text; invalidation is not universal suppression.
      - scope: Conversation summary and conversational fact extraction
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - runtime.md#rt-rte-context-window
          - memory.md#mem-obj-conversation-summary
          - memory.md#mem-rte-memory-write
          note: The summarizer compresses retained conversation material; remember selects standing facts
            from conversational input.
        records:
        - runtime.md#rt-rte-context-window
        - memory.md#mem-obj-conversation-summary
        - memory.md#mem-rte-memory-write
        note: Implemented reduction supports consolidation. Unverified semantic fidelity does not establish
          synthesis.
      - scope: Permanent removal of retained source memories
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-rte-memory-write
          - epistemic.md#epi-rte-lifecycle-change
          - memory.md#mem-rte-index-maintenance
          note: Owner review replace/discard actions and source-memory deletion forget the selected retained
            fact by removing its primary row; forgetting does not require autonomous aging.
        records:
        - memory.md#mem-rte-memory-write
        - epistemic.md#epi-rte-lifecycle-change
        - memory.md#mem-rte-index-maintenance
        note: Source-fact removal is distinct from historical invalidation and rebuild-only vector maintenance.
          Copies in conversations, summaries, backups or provider services can remain; this is bounded
          forgetting from the source-memory store, not universal erasure.
      - scope: Index rebuild and imported-content merge beyond the classified transformations
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-index-maintenance
        - runtime.md#rt-rte-owner-changes
        note: Index construction/repair and acquisition alone establish no curation value; records do
          not establish additional operations over this included branch.
      records:
      - memory.md#mem-rte-memory-write
      - memory.md#mem-obj-tal-memories
      - runtime.md#rt-rte-owner-changes
      - runtime.md#rt-rte-action-approval
      - memory.md#mem-rte-memory-recall
      - memory.md#mem-rte-requested-search
      - runtime.md#rt-rte-context-window
      - memory.md#mem-obj-conversation-summary
      - memory.md#mem-rte-index-maintenance
      - epistemic.md#epi-rte-lifecycle-change
      note: Deduplication, revision, historical withdrawal, trace consolidation and source-memory forgetting
        are supported. Records do not establish a complete curation enumeration for general model-authored
        saved prose or all remaining maintenance paths; no synthesis or promotion is inferred from route
        names, time sorting or embedding rebuilds.
    read_back_direction:
      assessment: known
      units:
      - scope: Automatic memory and item selection at new chat/scheduled invocations
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-memory-recall
          - memory.md#mem-rte-item-recall
          note: Host selectors supply earlier retained text before the foreground model requests a search.
        records:
        - memory.md#mem-rte-memory-recall
        - memory.md#mem-rte-item-recall
        note: Memory push covers keyword/semantic branches; item push is semantic foreground-only.
      - scope: Conversation summary/history and refreshed approval outcomes
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-context-window
          - memory.md#mem-obj-conversation-records
          - runtime.md#rt-rte-action-approval
          note: The runner automatically loads eligible same-conversation text, summary and current action
            outcomes for a later turn.
        records:
        - runtime.md#rt-rte-context-window
        - memory.md#mem-obj-conversation-records
        - memory.md#mem-obj-conversation-summary
        - runtime.md#rt-rte-action-approval
        note: A request to start chat is not a model request for each retained context part.
      - scope: Stored routine at alarm dispatch
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-scheduled-work
          note: An automatic scheduled callback selects the retained enabled routine and supplies its
            stored message to a fresh model invocation.
        records:
        - runtime.md#rt-rte-scheduled-work
        - runtime.md#rt-bap-retained-context
        note: Reminder/digest deterministic branches remain distinct from the model prompt branch.
      - scope: Explicit tool search/read and owner list/history/search/review reads
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-requested-search
          - memory.md#mem-obj-conversation-records
          - memory.md#mem-obj-memory-reviews
          - runtime.md#rt-rte-owner-changes
          note: Consumers request saved material through registered tools or shipped owner readers; code
            fulfills those requests.
        records:
        - memory.md#mem-rte-requested-search
        - memory.md#mem-obj-conversation-records
        - memory.md#mem-obj-memory-reviews
        - runtime.md#rt-rte-owner-changes
        note: Requested query/ID returns are not an additional push because code delivers them.
      - scope: Automatic maintenance consumption of saved content and indexes
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-memory-write
          - memory.md#mem-rte-index-maintenance
          - runtime.md#rt-rte-context-window
          note: Write/repair/overflow triggers automatically select retained candidates, source text or
            history for diagnosis, reindexing or summarization.
        records:
        - memory.md#mem-rte-memory-write
        - memory.md#mem-rte-index-maintenance
        - runtime.md#rt-rte-context-window
        note: These are update consumers, not additional foreground retrieval requests.
      records:
      - memory.md#mem-rte-memory-recall
      - memory.md#mem-rte-item-recall
      - runtime.md#rt-rte-context-window
      - memory.md#mem-obj-conversation-records
      - memory.md#mem-obj-conversation-summary
      - runtime.md#rt-rte-action-approval
      - runtime.md#rt-rte-scheduled-work
      - runtime.md#rt-bap-retained-context
      - memory.md#mem-rte-requested-search
      - memory.md#mem-obj-memory-reviews
      - runtime.md#rt-rte-owner-changes
      - memory.md#mem-rte-memory-write
      - memory.md#mem-rte-index-maintenance
      note: Both requested and unsolicited later-consumer routes are wired. The inventory includes owner
        readers and automatic maintenance as well as foreground delivery.
    read_back_signal:
      assessment: known
      units:
      - scope: Keyword/hybrid personal-memory push
        assessment: known
        findings:
        - value: inferred-lexical
          basis: wired
          records:
          - memory.md#mem-rte-memory-recall
          note: On chat/scheduled input, keyword matching selects retained fact wording.
        - value: inferred-embedding
          basis: wired
          records:
          - memory.md#mem-rte-memory-recall
          - memory.md#mem-obj-semantic-vectors
          note: Enabled hybrid selection compares the input embedding with retained vectors and can add
            newer numerical neighbors.
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-memory-recall
          note: Recent active preferences fill available slots and history intent/status/budget predicates
            limit the delivered set.
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-rte-memory-recall
          - memory.md#mem-obj-tal-memories
          note: Historical-intent recall follows stored predecessor/successor identity links to select
            related retained facts.
        records:
        - memory.md#mem-rte-memory-recall
        - memory.md#mem-obj-semantic-vectors
        - memory.md#mem-obj-tal-memories
        note: Trigger is a new chat or scheduled prompt; selectors use current text, vectors, lifecycle
          links, recency and limits. Identity-based additions are separate from coarse filtering.
      - scope: Foreground item push
        assessment: known
        findings:
        - value: inferred-embedding
          basis: wired
          records:
          - memory.md#mem-rte-item-recall
          - memory.md#mem-obj-item-vectors
          note: A cached current-message query vector selects best-part task/note/automation hits.
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-item-recall
          note: Current existence/completion filters, top-three limit and separate token budget further
            restrict delivered parts.
        records:
        - memory.md#mem-rte-item-recall
        - memory.md#mem-obj-item-vectors
        note: Trigger is semantic-enabled foreground context assembly; delivered text/excerpts are loaded
          after numerical selection.
      - scope: Conversation history/summary and approval-outcome push
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-rte-context-window
          - memory.md#mem-obj-conversation-records
          - runtime.md#rt-rte-action-approval
          note: The current conversation ID selects its retained history/summary; activity action IDs
            select current pending-action outcomes.
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-context-window
          - memory.md#mem-obj-conversation-summary
          note: Completion/origin rules, summary cutoff, recency suffix and estimated context budget restrict
            selected retained text.
        records:
        - runtime.md#rt-rte-context-window
        - memory.md#mem-obj-conversation-records
        - memory.md#mem-obj-conversation-summary
        - runtime.md#rt-rte-action-approval
        note: A conversation identity actually selects unsolicited context; this is not merely an ID displayed
          in a catalog.
      - scope: Stored routine push
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-rte-scheduled-work
          note: The alarm schedule ID must match the retained automation before its stored prompt is delivered.
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-scheduled-work
          note: Enabled/existing/not-running predicates and request budgets further gate scheduled delivery.
        records:
        - runtime.md#rt-rte-scheduled-work
        note: Trigger is SDK callback; retained matching routine supplies the later prompt.
      - scope: Automatic diagnosis, repair and compaction input selection
        assessment: known
        findings:
        - value: inferred-lexical
          basis: wired
          records:
          - memory.md#mem-rte-memory-write
          note: A changed memory triggers lexical/topic searches over older retained facts for diagnosis.
        - value: inferred-embedding
          basis: wired
          records:
          - memory.md#mem-rte-memory-write
          - memory.md#mem-obj-semantic-vectors
          note: Optional semantic neighbor selection nominates additional retained older facts.
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-rte-index-maintenance
          - runtime.md#rt-rte-context-window
          note: Index keys/source IDs select retained source parts for repair, and conversation identity
            selects history for compaction.
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-index-maintenance
          - memory.md#mem-rte-memory-write
          - runtime.md#rt-rte-context-window
          note: Hash/stamp/model pending checks, age/status limits, batch caps and overflow budget select
            maintenance inputs.
        records:
        - memory.md#mem-rte-memory-write
        - memory.md#mem-obj-semantic-vectors
        - memory.md#mem-rte-index-maintenance
        - runtime.md#rt-rte-context-window
        note: Clef judges nominated pairs after selection; its relationship judgment is not itself a read-back
          selector delivering fact text to the foreground model.
      records:
      - memory.md#mem-rte-memory-recall
      - memory.md#mem-obj-semantic-vectors
      - memory.md#mem-obj-tal-memories
      - memory.md#mem-rte-item-recall
      - memory.md#mem-obj-item-vectors
      - runtime.md#rt-rte-context-window
      - memory.md#mem-obj-conversation-records
      - memory.md#mem-obj-conversation-summary
      - runtime.md#rt-rte-action-approval
      - runtime.md#rt-rte-scheduled-work
      - memory.md#mem-rte-memory-write
      - memory.md#mem-rte-index-maintenance
      note: Each push signal is attached to a trigger, selector input and retained selected part. Tool
        and owner-requested IDs belong to pull, not independent identifier push.
    trace_learning:
      assessment: partial
      units:
      - scope: Automatic conversation compaction to retained later summary
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-context-window
          - memory.md#mem-obj-conversation-summary
          - memory.md#mem-obj-conversation-records
          note: Recorded session turns plus prior summary feed a code-admitted durable summary supplied
            to later model invocations.
        records:
        - runtime.md#rt-rte-context-window
        - memory.md#mem-obj-conversation-summary
        - memory.md#mem-obj-conversation-records
        note: This qualifies without improved capacity, parameter training, verified fidelity or novel
          propositions.
      - scope: Conversational remember to durable personal facts
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-memory-write
          - memory.md#mem-rte-memory-recall
          - runtime.md#rt-rte-owner-chat
          note: The model extracts lasting owner information from chat, code saves it automatically, and
            later memory recall supplies it as context.
        records:
        - memory.md#mem-rte-memory-write
        - memory.md#mem-rte-memory-recall
        - runtime.md#rt-rte-owner-chat
        note: Explicit remember requests do not create per-content human approval of the generated wording.
      - scope: Other model-authored notes/routines, imported provenance and opaque upstream derivations
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-owner-changes
        - runtime.md#rt-rte-scheduled-work
        - epistemic.md#epi-obj-generated-text
        note: Records establish retained authoring/import and later consumption but not every input derivation
          or qualifying trace-fed update for these alternatives; raw result logging alone is insufficient.
      records:
      - runtime.md#rt-rte-context-window
      - memory.md#mem-obj-conversation-summary
      - memory.md#mem-obj-conversation-records
      - memory.md#mem-rte-memory-write
      - memory.md#mem-rte-memory-recall
      - runtime.md#rt-rte-owner-chat
      - runtime.md#rt-rte-owner-changes
      - runtime.md#rt-rte-scheduled-work
      - epistemic.md#epi-obj-generated-text
      note: Qualifying summary and remembered-fact chains are wired. Other retained prose/import origins
        are not completely resolved, so positives do not become a system-wide complete trace-learning
        classification.
    trace_source:
      assessment: partial
      units:
      - scope: Conversation compaction input
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - runtime.md#rt-rte-context-window
          - memory.md#mem-obj-conversation-records
          - memory.md#mem-obj-conversation-summary
          note: Original input is recorded owner/assistant conversational turns, including imported turns
            once used in history.
        - value: tool-traces
          basis: wired
          records:
          - runtime.md#rt-rte-context-window
          - runtime.md#rt-rte-action-approval
          note: Refreshed execution/approval outcomes are synthesized into eligible history text before
            compaction.
        records:
        - runtime.md#rt-rte-context-window
        - memory.md#mem-obj-conversation-records
        - memory.md#mem-obj-conversation-summary
        - runtime.md#rt-rte-action-approval
        note: Tool-activity display metadata is not a guaranteed verbatim provider-tool replay, but the
          used approval/execution feedback is recorded tool experience.
      - scope: Conversational remembered-fact extraction
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-rte-memory-write
          - runtime.md#rt-rte-owner-chat
          note: The original input includes owner statements or remember requests in the chat session,
            not an environmental event stream merely because host code records it.
        records:
        - memory.md#mem-rte-memory-write
        - runtime.md#rt-rte-owner-chat
        note: Fact source flags do not preserve a message-level source citation; the wired live-chat extraction
          input is nevertheless identifiable.
      - scope: Other potentially trace-fed saved prose and imported prehistory
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-owner-changes
        - runtime.md#rt-rte-scheduled-work
        - epistemic.md#epi-obj-generated-text
        note: Original trace content/derivation is unresolved for the same alternatives retained by trace_learning.
          No event-stream or trajectory source is inferred from schedules or result logging alone.
      records:
      - runtime.md#rt-rte-context-window
      - memory.md#mem-obj-conversation-records
      - memory.md#mem-obj-conversation-summary
      - runtime.md#rt-rte-action-approval
      - memory.md#mem-rte-memory-write
      - runtime.md#rt-rte-owner-chat
      - runtime.md#rt-rte-owner-changes
      - runtime.md#rt-rte-scheduled-work
      - epistemic.md#epi-obj-generated-text
      note: Session logs and recorded tool execution/approval feedback support the classified qualifying
        writes; unknown alternative provenance prevents a complete trace-source inventory.
---

# Talorys memory profile

## Comparison rationale

This profile classifies the accepted application records, not deployment behavior. All positive findings have implementation basis `wired`; the attributed semantic evaluation does not upgrade any classification to observed or causally supported. Missing execution evidence prevents activation, fidelity and benefit conclusions, not inspection of wired storage and consumer routes.

The application memory inventory is established across [MEM-OBJ-tal-memories](memory.md#mem-obj-tal-memories), [MEM-OBJ-memory-reviews](memory.md#mem-obj-memory-reviews), [MEM-OBJ-conversation-records](memory.md#mem-obj-conversation-records), [MEM-OBJ-conversation-summary](memory.md#mem-obj-conversation-summary), [MEM-OBJ-semantic-vectors](memory.md#mem-obj-semantic-vectors), [MEM-OBJ-item-vectors](memory.md#mem-obj-item-vectors), [RT-OBJ-pending-actions](runtime.md#rt-obj-pending-actions), and the source-content, approval and routine paths cited in the units. These stores are not conflated with remote inference parameters. The provider adapters' uninspected internals do not imply an additional application checkpoint or establish model-weight learning; [RT-CMP-workers-embedder](runtime.md#rt-cmp-workers-embedder) distinguishes numerical outputs from their opaque producer.

Reconciliation supersedes the epistemic summary object with [MEM-OBJ-conversation-summary](memory.md#mem-obj-conversation-summary), which is used throughout this profile. Its second amendment supersedes the epistemic semantic-PASS claim with [MEM-CLM-eval-scope](memory.md#mem-clm-eval-scope); that reported threshold result supplies no stronger basis for the memory axes. Other containers and parts remain distinct. No unresolved cross-report conflict requires choosing a stronger finding.

Natural-language data and task instructions have different consumers. Stored routine wording supplies instruction at the scheduled model, whereas selected fact/note/summary text supplies knowledge under the shipped data policy; [RT-BAP-retained-context](runtime.md#rt-bap-retained-context). The raw experience consumed by the summarizer or remember update has learning authority at that update consumer, separately from knowledge authority of the resulting artifact. No model compliance, improved capacity or exercised self-improvement follows. Dense vector payloads provide ranking inputs, not downstream natural-language instructions.

Consolidation describes the implemented reduction in [RT-RTE-context-window](runtime.md#rt-rte-context-window) and [MEM-RTE-memory-write](memory.md#mem-rte-memory-write). It does not claim guaranteed semantic preservation. The indeterminate truth relation retained by the epistemic account does not require calling every compression synthesis. Historical status supports invalidation only for the bounded current-recall consumer: [MEM-RTE-requested-search](memory.md#mem-rte-requested-search) preserves counterpaths that still return past text. Permanent source-fact deletion supports decay as bounded forgetting: owner review replace/discard actions remove an older or newer fact, and source-memory deletion removes its primary row with associated cleanup. [MEM-RTE-memory-write](memory.md#mem-rte-memory-write), [EPI-RTE-lifecycle-change](epistemic.md#epi-rte-lifecycle-change), and [MEM-RTE-index-maintenance](memory.md#mem-rte-index-maintenance) establish that transformation independently of historical invalidation. Remaining copies in conversations or backups limit erasure, not the source-store forgetting classification. Index reconstruction alone establishes no curation operation.

Automatic versus manual admission follows decisions, not authorship. In particular, owner selection of a backup and code admission of its rows are separate mechanisms in [RT-RTE-owner-changes](runtime.md#rt-rte-owner-changes). Exact owner approval of a note rewrite is manual even though a model wrote the proposed body; [RT-RTE-action-approval](runtime.md#rt-rte-action-approval). Neither decision proves factual checking. Unknown pre-import lineage remains local to that branch rather than suppressing known authored, imported, compiled and trace-extracted paths.

The trace-learning union has a wired positive from automatic summaries and remembered facts. Summary inputs are conversational logs with recorded action-outcome feedback, not a fully faithful tool-output replay. This is supported by the memory annotations on [RT-RTE-context-window](runtime.md#rt-rte-context-window) and [RT-RTE-action-approval](runtime.md#rt-rte-action-approval), alongside [MEM-OBJ-conversation-records](memory.md#mem-obj-conversation-records). Other saved prose and imported prehistory lack sufficient input derivation facts for complete trace coverage. No local or system-wide `no` is invented in the absence of bounded absence records.

Push classifications distinguish actual unsolicited selection from requested return. Conversation and alarm identity matches select retained context, while an ID supplied to read_note is part of pull. Keyword and numerical selectors, identity-linked additions, and coarse eligibility/budget filters retain separate findings. Clef's relationship judgment changes disposition after candidate selection; it is not automatically inferred-judgment read-back selection. See [MEM-RTE-memory-recall](memory.md#mem-rte-memory-recall), [MEM-RTE-item-recall](memory.md#mem-rte-item-recall), [MEM-RTE-requested-search](memory.md#mem-rte-requested-search), and [MEM-RTE-memory-write](memory.md#mem-rte-memory-write).

Source-read log: no frozen-source files were read for this classification. All warrants come from the supplied accepted records and annotations. No new records, source evidence or quotations are introduced.
