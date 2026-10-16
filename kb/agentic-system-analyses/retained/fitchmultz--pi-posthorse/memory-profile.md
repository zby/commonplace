---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Pi Posthorse memory profile: durable notes, retained session content, continuation checkpoints
  and reminder access metadata at the frozen extension boundary.'
run-id: AAS-2026-10-14-pi-posthorse-58b9647d2f29-01
source-identity: https://github.com/fitchmultz/pi-posthorse
reviewed-boundary: 307ef6bf05bc8bd8d718725761ffdf2f2ef72539
memory-comparison:
  version: 2
  scope: Retained note content and revisions; host session-file content, images, IDs, projection/edit
    relationships and explicit/custom/native/legacy checkpoints consumed by Posthorse; retained reminder
    prose and eligibility fingerprints; their admission, maintenance and later-consumer routes. Includes
    unresolved initial notes, external sectional editors and native checkpoint production as named alternatives.
    Excludes external model weights/provider state, transient reset maps, page reservations and caches,
    regenerated static guidance, display-only cards/metadata as an independent memory payload, and development
    evaluator/checker outputs not consumed by production updates.
  axes:
    storage_substrate:
      assessment: known
      units:
      - scope: Durable notes, including pre-existing content and migrated locations
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-notes
          - memory.md#mem-rte-notes-migration
          note: Notes remain plaintext files; Git metadata resolves a shared directory, not a repository-backed
            memory object.
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-rte-notes-migration
        note: Initial authorship uncertainty does not obscure the file substrate.
      - scope: 'Host journal: raw entries, edited versions, images, reminders, explicit/custom/native
          and legacy checkpoints'
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-session-journal
          - memory.md#mem-obj-explicit-handoff
          - memory.md#mem-obj-recovery-record
          - runtime.md#rt-rte-request-guidance
          note: The consumed archive is host session files, including compaction summaries and legacy
            handoff entries.
        records:
        - memory.md#mem-obj-session-journal
        - memory.md#mem-obj-explicit-handoff
        - memory.md#mem-obj-recovery-record
        - runtime.md#rt-rte-request-guidance
        note: The recorded host-file contract covers these retained parts. In-process projections are
          access paths, not additional durable stores; host persistence correctness is unverified.
      records:
      - memory.md#mem-obj-notes
      - memory.md#mem-rte-notes-migration
      - memory.md#mem-obj-session-journal
      - memory.md#mem-obj-explicit-handoff
      - memory.md#mem-obj-recovery-record
      - runtime.md#rt-rte-request-guidance
      note: The accepted inventory identifies notes and host session files as the retained substrates.
        External model weights and transient access state are not this memory boundary.
    representational_form:
      assessment: partial
      units:
      - scope: Note task prose interpreted by the later model
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-notes
          - memory.md#mem-rte-notes-recall
          note: Task-state prose reaches the model as note-tool content.
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-rte-notes-recall
        note: Classifies the recorded prose path, not all arbitrary file bytes.
      - scope: Other arbitrary or pre-existing note content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-notes
        note: The tool imposes no semantic form; no content instances establish all other controlled forms.
      - scope: Journal message, thinking, tool-text and checkpoint prose, including explicit and native
          summaries
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-session-journal
          - memory.md#mem-obj-explicit-handoff
          - memory.md#mem-obj-recovery-record
          - memory.md#mem-rte-history-recall
          note: Normalized prose and summary excerpts are interpreted by the later model.
        records:
        - memory.md#mem-obj-session-journal
        - memory.md#mem-obj-explicit-handoff
        - memory.md#mem-obj-recovery-record
        - memory.md#mem-rte-history-recall
        note: Native-summary fidelity and actual propositions are unknown, but the consumed text form
          is recorded.
      - scope: Journal access metadata and recovery references consumed by fixed selectors
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-session-journal
          - memory.md#mem-obj-recovery-record
          - epistemic.md#epi-rte-recovery-provenance
          note: Entry IDs, parent links, replacement relationships and kinds have localized fixed-rule
            consumers.
        records:
        - memory.md#mem-obj-session-journal
        - memory.md#mem-obj-recovery-record
        - epistemic.md#epi-rte-recovery-provenance
        note: This differs from the natural-language interpretation of the delivered excerpts.
      - scope: Stored image payloads returned by history
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-session-journal
        - memory.md#mem-rte-history-recall
        note: The records establish encoded media delivery, not a controlled representational-form classification
          of the full payload. MIME/count display summaries cannot classify it.
      - scope: Retained reminder prose and eligibility fingerprints
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - runtime.md#rt-obj-context-guidance
          - runtime.md#rt-rte-request-guidance
          note: Reminder directions are model-interpreted.
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-rte-request-guidance
          note: Window/context/reserve fingerprints are matched and filtered by code.
        records:
        - runtime.md#rt-obj-context-guidance
        - runtime.md#rt-rte-request-guidance
        note: Separate prose and fixed-rule metadata consumers are established.
      records:
      - memory.md#mem-obj-notes
      - memory.md#mem-rte-notes-recall
      - memory.md#mem-obj-session-journal
      - memory.md#mem-obj-explicit-handoff
      - memory.md#mem-obj-recovery-record
      - memory.md#mem-rte-history-recall
      - epistemic.md#epi-rte-recovery-provenance
      - runtime.md#rt-obj-context-guidance
      - runtime.md#rt-rte-request-guidance
      note: Prose and fixed-rule metadata are classified. Arbitrary note material and full image payloads
        remain unresolved; no parametric finding follows from media encoding or the external inference
        model.
    lineage:
      assessment: partial
      units:
      - scope: Subsequent caller/model note creation and revision
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-notes
          - runtime.md#rt-rte-note-admission
          note: Callers formulate note content for creation, replacement and append.
        records:
        - memory.md#mem-obj-notes
        - runtime.md#rt-rte-note-admission
        note: Known subsequent authorship does not resolve older content provenance.
      - scope: Initial or imported pre-existing notes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-notes
        note: Pre-existing authorship and import history are unresolved. Possible import is not a supported
          imported finding.
      - scope: Explicit handoff formulation
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-explicit-handoff
          - runtime.md#rt-rte-explicit-reset
          note: Foreground caller/model formulates continuation prose; blankness substitutes a fixed instruction.
        records:
        - memory.md#mem-obj-explicit-handoff
        - runtime.md#rt-rte-explicit-reset
        note: The recorded output derivation is known without assuming human approval.
      - scope: Automatic recovery excerpts, receipt blocks and checkpoint pointers
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-recovery-record
          - epistemic.md#epi-rte-recovery-reshape
          note: Code selects and compresses recorded branch/projection inputs and receipts into a durable
            recovery record.
        records:
        - memory.md#mem-obj-recovery-record
        - epistemic.md#epi-rte-recovery-reshape
        note: Extraction is recorded even though the truth and completeness of inputs are not established.
      - scope: Raw journal contributions and context-edit replacements
        assessment: partial
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-session-journal
          note: The journal retains model outputs and custom messages authored during work.
        records:
        - memory.md#mem-obj-session-journal
        note: External user/tool sources, initial capture and replacement production are not fully individuated.
          The record does not establish a complete authored/imported provenance inventory.
      - scope: Native/manual and legacy nonautomatic checkpoint generation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-recovery-record
        - memory.md#mem-obj-session-journal
        - runtime.md#rt-rte-automatic-recovery
        note: Existing checkpoint text is consumed, but its external production path is not established.
      - scope: Retained reminder text and fingerprints
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - runtime.md#rt-rte-request-guidance
          - runtime.md#rt-obj-context-guidance
          note: Fixed guidance and current configuration/window facts produce retained reminder records.
        records:
        - runtime.md#rt-rte-request-guidance
        - runtime.md#rt-obj-context-guidance
        note: No learned or trace-extracted semantic guidance revision is established by reminder generation.
      records:
      - memory.md#mem-obj-notes
      - runtime.md#rt-rte-note-admission
      - memory.md#mem-obj-explicit-handoff
      - runtime.md#rt-rte-explicit-reset
      - memory.md#mem-obj-recovery-record
      - epistemic.md#epi-rte-recovery-reshape
      - memory.md#mem-obj-session-journal
      - runtime.md#rt-rte-automatic-recovery
      - runtime.md#rt-rte-request-guidance
      - runtime.md#rt-obj-context-guidance
      note: Supported authored, extracted and compiled paths coexist. Initial notes, host journal input
        derivations and native checkpoint generation prevent complete provenance classification.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Retrieved note prose at the foreground model
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-notes
          - memory.md#mem-rte-notes-recall
          - memory.md#mem-bap-recalled-content
          note: Recalled task state supplies context/reference through a tool result.
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-rte-notes-recall
        - memory.md#mem-bap-recalled-content
        note: No standing-preference consumer or executable truth gate is recorded for arbitrary note
          instructions.
      - scope: Journal prose and image payloads at the foreground model
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-session-journal
          - memory.md#mem-rte-history-recall
          - memory.md#mem-bap-recalled-content
          note: Selected history content supplies historical context and evidence, not current-state endorsement.
        records:
        - memory.md#mem-obj-session-journal
        - memory.md#mem-rte-history-recall
        - memory.md#mem-bap-recalled-content
        note: Knowledge force does not imply truth, fresh authorization or actual reliance.
      - scope: Explicit and nonautomatic checkpoint prose at the next model
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-explicit-handoff
          - memory.md#mem-obj-recovery-record
          - memory.md#mem-bap-recalled-content
          note: Continuation/checkpoint content supplies later task context.
        - value: instruction
          basis: wired
          records:
          - memory.md#mem-obj-explicit-handoff
          note: The explicit empty-handoff fallback directs restoration of relevant notes and history.
        records:
        - memory.md#mem-obj-explicit-handoff
        - memory.md#mem-obj-recovery-record
        - memory.md#mem-bap-recalled-content
        note: Instruction is supported for the fixed explicit fallback, not inferred for every native
          or caller-authored claim.
      - scope: Retained traces and checkpoints at the automatic recovery builder
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-obj-recovery-record
          - runtime.md#rt-rte-automatic-recovery
          - epistemic.md#epi-rte-recovery-reshape
          note: Recorded session/tool experience feeds an automatic durable behavior-shaping recovery
            update.
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-recovery-record
          - memory.md#mem-obj-session-journal
          - epistemic.md#epi-rte-recovery-provenance
          note: Checkpoint ancestry, IDs and projection relationships select the input window and source
            versions.
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-session-journal
          - epistemic.md#epi-rte-recovery-provenance
          note: Retained projection/linkage facts determine eligibility of owner-answer inputs.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-session-journal
          - epistemic.md#epi-rte-recovery-provenance
          note: Omitted/projected-away and ineligible owner inputs are excluded by code predicates.
        records:
        - memory.md#mem-obj-recovery-record
        - runtime.md#rt-rte-automatic-recovery
        - epistemic.md#epi-rte-recovery-reshape
        - memory.md#mem-obj-session-journal
        - epistemic.md#epi-rte-recovery-provenance
        note: Update-consumer force is separate from the output's later knowledge and instruction force;
          learning here does not assert improved capacity.
      - scope: Automatic recovery output at the later model
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-recovery-record
          - memory.md#mem-bap-recalled-content
          note: Selected inputs and receipts supply continuation evidence.
        - value: instruction
          basis: wired
          records:
          - memory.md#mem-obj-recovery-record
          - epistemic.md#epi-rte-recovery-reshape
          note: Fixed warnings distinguish owner intent, stale checkpoints and uncertified progress.
        records:
        - memory.md#mem-obj-recovery-record
        - memory.md#mem-bap-recalled-content
        - epistemic.md#epi-rte-recovery-reshape
        note: The model interprets these warnings; there is no enforced truth license.
      - scope: Retained content and metadata at recall selectors
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-rte-notes-recall
          - memory.md#mem-rte-history-recall
          - memory.md#mem-obj-session-journal
          note: File modification order and original-before-recovery priority influence relative order
            of returned retained parts.
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-session-journal
          - memory.md#mem-rte-history-recall
          note: Entry/file IDs, parent membership and cursor anchors choose scope and addressed versions.
        records:
        - memory.md#mem-rte-notes-recall
        - memory.md#mem-rte-history-recall
        - memory.md#mem-obj-session-journal
        note: Fixed ranking code still consumes retained features; it need not be learned ranking policy.
      - scope: Retained reminder prose and fingerprints at later model/eligibility code
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - runtime.md#rt-rte-request-guidance
          - runtime.md#rt-obj-context-guidance
          note: Reminder prose supplies checkpoint directions.
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-rte-request-guidance
          note: Fingerprints determine whether a reminder is eligible for the current window/configuration.
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-rte-request-guidance
          note: Matching fingerprints suppress duplicate reminders; stale/disabled records are filtered
            from active input.
        records:
        - runtime.md#rt-rte-request-guidance
        - runtime.md#rt-obj-context-guidance
        note: The metadata effect is executable while prose compliance remains unobserved.
      - scope: Other arbitrary note content and unrecorded native-checkpoint consumer effects
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-obj-recovery-record
        note: The records do not individuate all possible downstream instructions or other forces of arbitrary
          retained content. No additional force is inferred from possibility alone.
      records:
      - memory.md#mem-obj-notes
      - memory.md#mem-rte-notes-recall
      - memory.md#mem-bap-recalled-content
      - memory.md#mem-obj-session-journal
      - memory.md#mem-rte-history-recall
      - memory.md#mem-obj-explicit-handoff
      - memory.md#mem-obj-recovery-record
      - runtime.md#rt-rte-automatic-recovery
      - epistemic.md#epi-rte-recovery-reshape
      - epistemic.md#epi-rte-recovery-provenance
      - runtime.md#rt-rte-request-guidance
      - runtime.md#rt-obj-context-guidance
      note: Actual recorded consumers support multiple forces. Unknown arbitrary-content effects prevent
        a complete authority inventory; transient page/callback controls and shipped static guidance are
        excluded.
    write_agency:
      assessment: partial
      units:
      - scope: Foreground model note-content admission through notes write/append
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-note-admission
          - memory.md#mem-obj-notes
          note: Model content is admitted without mandatory per-content human approval.
        records:
        - runtime.md#rt-rte-note-admission
        - memory.md#mem-obj-notes
        note: This classifies the evidenced model path, not generic caller identity or physical filesystem
          I/O.
      - scope: Other caller admission and pre-existing note initialization
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-notes
        - runtime.md#rt-rte-note-admission
        note: Generic caller identity and unknown initialization do not establish either explicit human
          content decision or autonomous admission.
      - scope: External sectional note editing
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-notes
        - runtime.md#rt-rte-note-admission
        note: The external writer is afforded, but its implementation and per-content approval policy
          are uninspected.
      - scope: Foreground model explicit-handoff admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-explicit-handoff
          - runtime.md#rt-rte-explicit-reset
          note: The model proposes handoff text and software checks origin/capacity without per-handoff
            human approval.
        records:
        - memory.md#mem-obj-explicit-handoff
        - runtime.md#rt-rte-explicit-reset
        note: A user initiating the task is not a human approval gate for this write.
      - scope: Automatic custom recovery admission and note migration
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-automatic-recovery
          - memory.md#mem-obj-recovery-record
          note: Code constructs and offers the trace-derived checkpoint without per-record human approval.
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-notes-migration
          note: Software relocates retained notes on location resolution without per-note approval.
        records:
        - runtime.md#rt-rte-automatic-recovery
        - memory.md#mem-obj-recovery-record
        - memory.md#mem-rte-notes-migration
        note: Construction/admission and relocation are separate mechanisms, both software-controlled.
      - scope: Reminder record admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-request-guidance
          note: Code selects and queues reminders from usage/policy/fingerprint state.
        records:
        - runtime.md#rt-rte-request-guidance
        note: No per-reminder human content approval is required by the recorded route.
      - scope: Host raw-journal persistence, context-edit replacement and native checkpoint admission
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-session-journal
        - memory.md#mem-obj-recovery-record
        - runtime.md#rt-rte-automatic-recovery
        note: External host generation, capture and replacement controls are not inspected. Reading/selecting
          these checkpoints does not establish their write agency.
      records:
      - runtime.md#rt-rte-note-admission
      - memory.md#mem-obj-notes
      - memory.md#mem-obj-explicit-handoff
      - runtime.md#rt-rte-explicit-reset
      - runtime.md#rt-rte-automatic-recovery
      - memory.md#mem-obj-recovery-record
      - memory.md#mem-rte-notes-migration
      - runtime.md#rt-rte-request-guidance
      - memory.md#mem-obj-session-journal
      note: Model/software admission is positive on inspected routes. No manual finding is established
        merely by optional human authorship or workflow initiation; external and initial controls remain
        unresolved.
    curation_operations:
      assessment: partial
      units:
      - scope: Automatic recovery transformation of retained session/tool content
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-obj-recovery-record
          - epistemic.md#epi-rte-recovery-reshape
          note: The builder selects, compresses and combines retained inputs/receipts into a reduced continuation
            record.
        records:
        - memory.md#mem-obj-recovery-record
        - epistemic.md#epi-rte-recovery-reshape
        note: Truncation can lose qualifiers; that defect does not establish synthesis of a new claim.
          Migration and indexing are not additional curation operations.
      - scope: Note replacement maintenance
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-obj-notes
          - runtime.md#rt-rte-note-admission
          note: Whole replacement revises an existing retained note; append alone need not reconcile its
            claims.
        records:
        - memory.md#mem-obj-notes
        - runtime.md#rt-rte-note-admission
        note: The tool implements replacement, not guaranteed semantic improvement or faithful author
          compliance with concise-note guidance.
      - scope: Projection withdrawal and retained reminder filtering
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records:
          - memory.md#mem-obj-session-journal
          - epistemic.md#epi-rte-recovery-provenance
          note: Projection omission/replacement withdraws current reliance on old entries while originals
            remain in history.
        - value: invalidate
          basis: wired
          records:
          - runtime.md#rt-rte-request-guidance
          note: Stale or disabled reminders leave active input but remain historically retrievable.
        records:
        - memory.md#mem-obj-session-journal
        - epistemic.md#epi-rte-recovery-provenance
        - runtime.md#rt-rte-request-guidance
        note: Classification concerns implemented selection/filtering consequences; production of external
          context edits is not audited.
      - scope: External editor and native checkpoint transformations
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-obj-recovery-record
        - runtime.md#rt-rte-automatic-recovery
        note: Requested sectional editing and native summarization remain external; their implemented
          transformations cannot be fully classified from the accepted records.
      records:
      - memory.md#mem-obj-recovery-record
      - epistemic.md#epi-rte-recovery-reshape
      - memory.md#mem-obj-notes
      - runtime.md#rt-rte-note-admission
      - memory.md#mem-obj-session-journal
      - epistemic.md#epi-rte-recovery-provenance
      - runtime.md#rt-rte-request-guidance
      - runtime.md#rt-rte-automatic-recovery
      note: Consolidation, revision and projection invalidation have local implementation warrants. Opaque
        native/editor paths prevent a complete operation inventory; requested behavior does not establish
        dedup, synthesis, promotion or decay.
    read_back_direction:
      assessment: known
      units:
      - scope: Notes and detailed history recall, including stored images and old checkpoints
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-notes-recall
          - memory.md#mem-rte-history-recall
          note: The foreground consumer explicitly requests a path/query/entry and receives selected pages.
        records:
        - memory.md#mem-rte-notes-recall
        - memory.md#mem-rte-history-recall
        note: Automatic paging/delivery fulfills the request; it is not an additional unsolicited push.
      - scope: Explicit, custom automatic and existing nonautomatic checkpoint delivery
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-explicit-handoff
          - memory.md#mem-obj-recovery-record
          - runtime.md#rt-rte-automatic-recovery
          note: Host projection supplies the admitted continuation to the next model without a retrieval
            request.
        records:
        - memory.md#mem-obj-explicit-handoff
        - memory.md#mem-obj-recovery-record
        - runtime.md#rt-rte-automatic-recovery
        note: The known consumption path includes native/legacy checkpoint material reused by custom recovery;
          its external generation is a separate uncertainty.
      - scope: Retained reminder metadata lookup and model-visible filtering
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-request-guidance
          note: Automatic hook lookup supplies retained fingerprints to eligibility/filtering decisions
            without a model recall request.
        records:
        - runtime.md#rt-rte-request-guidance
        note: Reminder prose is also available through the separately classified history pull route.
      records:
      - memory.md#mem-rte-notes-recall
      - memory.md#mem-rte-history-recall
      - memory.md#mem-obj-explicit-handoff
      - memory.md#mem-obj-recovery-record
      - runtime.md#rt-rte-automatic-recovery
      - runtime.md#rt-rte-request-guidance
      note: The memory report inventory distinguishes requested recall from checkpoint and reminder-metadata
        automatic supply. Host deployment/operation uncertainty does not make the recorded directions
        indeterminate.
    read_back_signal:
      assessment: known
      units:
      - scope: Automatic recovery source selection on compaction hook or threshold fallback
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-recovery-record
          - runtime.md#rt-rte-automatic-recovery
          - epistemic.md#epi-rte-recovery-reshape
          note: 'Trigger: reached automatic boundary. Selector inputs: owner/coordination roles, recency,
            trailing batch, ancestry and capacity. Selected parts: bounded anchors, indices, receipts
            and checkpoints.'
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-obj-recovery-record
          - epistemic.md#epi-rte-recovery-provenance
          note: 'Trigger: the same automatic boundary. Projection IDs and linked call/result identity
            matches select eligible source versions and receipts delivered in recovery.'
        records:
        - memory.md#mem-obj-recovery-record
        - runtime.md#rt-rte-automatic-recovery
        - epistemic.md#epi-rte-recovery-reshape
        - epistemic.md#epi-rte-recovery-provenance
        note: Budget/recency selection and actual provenance identity matching are distinct warrants;
          no semantic embedding or lexical push is recorded.
      - scope: Explicit handoff selected for committed next-window projection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-explicit-handoff
          - runtime.md#rt-rte-explicit-reset
          note: 'Trigger: eligible explicit reset settlement. Selector input: the admitted current handoff
            and capacity. Selected retained part: that continuation summary.'
        records:
        - memory.md#mem-obj-explicit-handoff
        - runtime.md#rt-rte-explicit-reset
        note: Callback ID matches authenticate the newly proposed write; they are not independent identity-targeted
          retrieval of an older retained memory part.
      - scope: Nonautomatic checkpoint carried by automatic ancestry selection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-recovery-record
          note: 'Trigger: recovery construction. Selector input: ancestry and nearest suitable nonautomatic
            checkpoint. Selected retained part: bounded possibly stale checkpoint text.'
        records:
        - memory.md#mem-obj-recovery-record
        note: Unknown external checkpoint generation does not obscure the inspected coarse reuse selector.
      - scope: Retained reminder metadata selected by automatic hook lookup
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-rte-request-guidance
          note: 'Trigger: request/turn eligibility or projection filtering. Selector input: current window/context/reserve
            fingerprint and leaf identity. Selected retained part: matching reminder metadata used to
            suppress/filter reminders.'
        records:
        - runtime.md#rt-rte-request-guidance
        note: An actual fingerprint match affects selection, not merely a catalog ID.
      - scope: Caller-requested note/history pages
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-notes-recall
        - memory.md#mem-rte-history-recall
        note: These units are pull; their literal/path/ID targeting is not a push-selection signal. All
          other direction units have been classified separately.
      records:
      - memory.md#mem-obj-recovery-record
      - runtime.md#rt-rte-automatic-recovery
      - epistemic.md#epi-rte-recovery-reshape
      - epistemic.md#epi-rte-recovery-provenance
      - memory.md#mem-obj-explicit-handoff
      - runtime.md#rt-rte-explicit-reset
      - runtime.md#rt-rte-request-guidance
      - memory.md#mem-rte-notes-recall
      - memory.md#mem-rte-history-recall
      note: Known push units have coarse or identity-matching selectors. Pull units are locally inapplicable,
        not a system-wide pull-only conclusion; no task-relevance inference is attributed to these fixed
        selectors.
    trace_learning:
      assessment: partial
      units:
      - scope: 'Automatic custom recovery: retained session/tool records to durable next-window continuation'
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-obj-recovery-record
          - runtime.md#rt-rte-automatic-recovery
          - epistemic.md#epi-rte-recovery-reshape
          - memory.md#mem-bap-recalled-content
          note: Automatic trace-fed construction produces a retained behavior-shaping artifact consumed
            by the later model.
        records:
        - memory.md#mem-obj-recovery-record
        - runtime.md#rt-rte-automatic-recovery
        - epistemic.md#epi-rte-recovery-reshape
        - memory.md#mem-bap-recalled-content
        note: The wired route meets this axis even though it reshapes existing claims and no improved
          capacity or exercised benefit is observed.
      - scope: Model note maintenance and explicit handoff formulation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-obj-explicit-handoff
        - runtime.md#rt-rte-note-admission
        - runtime.md#rt-rte-explicit-reset
        note: The records establish content writes and later consumption but do not establish which traces
          actually feed model formulation. Requested task-state maintenance alone cannot establish a qualifying
          route or bounded no.
      - scope: Native checkpoint and external note-editor updates
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-recovery-record
        - memory.md#mem-obj-notes
        - runtime.md#rt-rte-automatic-recovery
        note: Their implementations and input-to-update chains are uninspected; custom recovery's positive
          witness cannot resolve them.
      - scope: Raw journal and retained reminder production
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-session-journal
        - runtime.md#rt-rte-request-guidance
        note: Raw capture alone is not trace learning. Fixed reminder generation and retained metadata
          effects do not establish a qualifying trace-fed behavior-shaping update, nor do these records
          warrant a universal bounded negative.
      records:
      - memory.md#mem-obj-recovery-record
      - runtime.md#rt-rte-automatic-recovery
      - epistemic.md#epi-rte-recovery-reshape
      - memory.md#mem-bap-recalled-content
      - memory.md#mem-obj-notes
      - memory.md#mem-obj-explicit-handoff
      - runtime.md#rt-rte-note-admission
      - runtime.md#rt-rte-explicit-reset
      - memory.md#mem-obj-session-journal
      - runtime.md#rt-rte-request-guidance
      note: The custom continuation update supports yes at wired strength. Other included writes remain
        unresolved; no local or system-wide no is asserted without a bounded absence record.
    trace_source:
      assessment: partial
      units:
      - scope: Current-window input and receipt content consumed by custom automatic recovery
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-obj-recovery-record
          - epistemic.md#epi-rte-recovery-reshape
          note: Recorded conversational user/model turns and visible session coordination feed the continuation
            update.
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-obj-recovery-record
          - runtime.md#rt-rte-automatic-recovery
          note: Recorded requests, admitted arguments, linked/orphan results and errors feed receipt construction
            and owner-answer selection.
        records:
        - memory.md#mem-obj-recovery-record
        - epistemic.md#epi-rte-recovery-reshape
        - runtime.md#rt-rte-automatic-recovery
        note: Source classification follows original conversational/tool content, not hook trigger labels.
          No multi-step state/action/outcome training trajectory is established.
      - scope: Native/legacy checkpoint inputs reused by custom automatic recovery
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-recovery-record
        - memory.md#mem-obj-session-journal
        note: Nonautomatic checkpoints are consumed, but their full original generation inputs and mixed
          provenance are not recorded. Known current-window traces do not resolve this included input.
      - scope: Potential trace inputs to note/handoff and external/native updates
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-obj-explicit-handoff
        - runtime.md#rt-rte-note-admission
        - memory.md#mem-obj-recovery-record
        - runtime.md#rt-rte-automatic-recovery
        note: Qualifying trace-learning status is unresolved for these routes, so their original learning
          inputs cannot be completely classified.
      - scope: Raw capture and reminder production as possible qualifying updates
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-session-journal
        - runtime.md#rt-rte-request-guidance
        note: No qualifying trace-fed update chain is established for these writes; without bounded absence
          their trace sources are unresolved, not inapplicable.
      records:
      - memory.md#mem-obj-recovery-record
      - epistemic.md#epi-rte-recovery-reshape
      - runtime.md#rt-rte-automatic-recovery
      - memory.md#mem-obj-session-journal
      - memory.md#mem-obj-notes
      - memory.md#mem-obj-explicit-handoff
      - runtime.md#rt-rte-note-admission
      - runtime.md#rt-rte-request-guidance
      note: Session logs and tool traces are retained positives for the inspected custom update. Opaque
        checkpoint provenance and unresolved other writes prevent complete source coverage; discrete hook
        triggers alone do not warrant event-streams.
---

# Pi Posthorse memory profile

## Comparison rationale

The memory boundary is accumulated task content and its operative access metadata, not every stored runtime object. Notes and session files supply the retained substrates. Git common-root resolution does not make notes repository memory. Transient projections, callback maps and page reservations do not add a durable in-memory substrate. Display metadata is not a second model-facing payload. These distinctions follow [MEM-OBJ-notes](memory.md#mem-obj-notes), [MEM-OBJ-session-journal](memory.md#mem-obj-session-journal), [MEM-OBJ-posthorse-display](memory.md#mem-obj-posthorse-display) and [RT-CMP-page-reservations](runtime.md#rt-cmp-page-reservations).

Automatic recovery is consolidation and trace learning under this comparison contract. It compresses retained conversation and tool receipts into a durable continuation that a later model receives. Neither novel claims nor measured improvement are needed for the wired trace-learning finding. Learning authority belongs to the traces at the update consumer; knowledge and fixed-warning instruction belong to the resulting checkpoint at the later model. The epistemic reshaping account does not contradict that classification or establish semantic fidelity. See [MEM-OBJ-recovery-record](memory.md#mem-obj-recovery-record), [EPI-RTE-recovery-reshape](epistemic.md#epi-rte-recovery-reshape) and [MEM-BAP-recalled-content](memory.md#mem-bap-recalled-content).

Requested note/history returns are pull. Checkpoint projection and automatic reminder-metadata lookup are push operations. Literal query/path/entry targeting in requested recall is not inferred-lexical or identifier push. Automatic recovery combines coarse role/recency/budget selection with actual projection/provenance identity matches. Explicit-reset callback identity authenticates admission of a proposed write; it is not targeted retrieval of an older memory object. See [MEM-RTE-notes-recall](memory.md#mem-rte-notes-recall), [MEM-RTE-history-recall](memory.md#mem-rte-history-recall), [RT-RTE-explicit-reset](runtime.md#rt-rte-explicit-reset), [EPI-RTE-recovery-provenance](epistemic.md#epi-rte-recovery-provenance) and [RT-RTE-request-guidance](runtime.md#rt-rte-request-guidance).

The positive automatic write findings cover model/software admission without a required per-content human decision. They do not classify generic callers, pre-existing notes or external editors as autonomous. Optional human authorship is not an evidenced manual admission mechanism. Native/manual checkpoints remain included: their later textual consumption and ancestry selection are recorded, but production control, original inputs and generation fidelity are not. See [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), [MEM-OBJ-notes](memory.md#mem-obj-notes) and [MEM-OBJ-recovery-record](memory.md#mem-obj-recovery-record).

No supersession affects a value. Reconciliation retains valid containers alongside their parts and identifies no cross-report conflict. The profile therefore cites the original canonical declarations. Unresolved units remain local to each axis rather than being removed to obtain complete coverage. In particular, arbitrary note content and actual image payloads prevent complete form classification; imported note provenance and native checkpoint production prevent complete lineage/admission/trace classification. No unsupported absence or inapplicability is substituted for those gaps.

All positive findings concern implementation wiring unless their own basis says otherwise. Host persistence and delivery are external contracts; no supplied run or experiment establishes activation, improved capacity, reliable restoration or task truth. The selected workflow's scripted retrieval and reopening assertions do not upgrade the findings to observed operation: see [EPI-RTE-reset-evaluator](epistemic.md#epi-rte-reset-evaluator) and [RT-CLM-context-continuation](runtime.md#rt-clm-context-continuation).

Source-read log: none. This classification used only the supplied accepted members and contracts; no source ambiguity required reading frozen source files.
