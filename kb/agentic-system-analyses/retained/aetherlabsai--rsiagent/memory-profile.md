---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: RSIAgent memory comparison of the experience bank, continuation products, role-private retained
  state and checkpoint consumers at the frozen revision.
run-id: AAS-2026-10-14-rsiagent-b11225763c0b-01
source-identity: https://github.com/AetherLabsAI/RSIAgent
reviewed-boundary: 4d7ef43770dda341fccd9a5743db92407687c615
memory-comparison:
  version: 2
  scope: Canonical and guest experience-bank trees, frozen copies, bank access inventories, journals/manifests
    and checked recovery checkpoints; Actor WORK LOG/fallback/restart handoffs; Curriculum notes, histories,
    outcomes and Actor diagnosis; Verifier retained substantive history, image attachments and private
    scratch. Includes unresolved initial-bank provenance, other dispatched recovery variants, opaque payloads
    and possible provider-side use-accumulated state. Excludes static shipped prompts/configuration/code,
    provider weights not evidenced as changed through use, ordinary unretained VM state, official score/report
    archives without an adaptive memory consumer and unspecified external API callers as consumer routes.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Canonical bank, guest copies and frozen evaluation copies
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-memory
          - runtime.md#rt-rte-learning-admission
          note: Complete byte trees are installed and uploaded as filesystem copies.
        records:
        - memory.md#mem-obj-memory
        - runtime.md#rt-rte-learning-admission
        note: Filesystem retention is known independently of opaque file content.
      - scope: Bank journal, snapshots and exact-tree recovery checkpoints
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-memory-journal
          note: Journal archives and before/after trees are filesystem objects.
        records:
        - memory.md#mem-obj-memory-journal
        - runtime.md#rt-rte-lineage-recovery
        note: Archives and manifests are retained on the host filesystem.
      - scope: Actor WORK LOG, folded summary and restart handoff
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-work-log
          - memory.md#mem-rte-worklog-fold
          note: Summary and LoopResult.worklog persist in Python state for subsequent invocations.
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-work-log
          note: ArtifactSink saves summary artifacts on the host.
        records:
        - memory.md#mem-obj-work-log
        - memory.md#mem-rte-worklog-fold
        note: Both live summary state and saved artifacts are accounted for.
      - scope: Curriculum notes, role history, latest outcomes and Actor diagnosis
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-curriculum-notes
          - runtime.md#rt-rte-curriculum-search
          note: Session notes and accumulated role history survive Curriculum rounds.
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-curriculum-notes
          - memory.md#mem-obj-learning-diagnosis
          note: Guest notes and archived turns/diagnosis are filesystem-retained.
        records:
        - memory.md#mem-obj-curriculum-notes
        - memory.md#mem-obj-learning-diagnosis
        - runtime.md#rt-rte-curriculum-search
        note: Inspected persistent session and artifact routes retain these separate products.
      - scope: Verifier retained history, replay checkpoints and private scratch
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-verifier-scratch
          - memory.md#mem-rte-verifier-replay
          note: Private scratch archives and raw segment artifacts are saved.
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-rte-verifier-replay
          note: Recovered substantive history and pending observations enter persistent role state.
        records:
        - memory.md#mem-obj-verifier-scratch
        - memory.md#mem-rte-verifier-replay
        note: Scratch payload opacity does not obscure its filesystem substrate.
      - scope: Durable image attachment bytes and identity metadata
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-durable-images
          - memory.md#mem-rte-verifier-replay
          note: Archived messages preserve complete image bytes.
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-durable-images
          - memory.md#mem-rte-verifier-replay
          note: Archived attachments are rehydrated into later message state.
        records:
        - memory.md#mem-obj-durable-images
        - memory.md#mem-rte-verifier-replay
        note: JSON/base64 encoding is not a separate storage substrate.
      - scope: 'Other dispatched recovery variants: unverified practice, post-target learning, ready-target
          replacement and remaining wave recovery'
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-lineage-recovery
        note: Variant bodies were not fully inspected; their retained parts and this axis cannot be completely
          classified.
      - scope: Provider-side state accumulated through use, if any, behind the Actor, Verifier, Curriculum
          and vision endpoints
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-actor
        - runtime.md#rt-cmp-verifier
        - runtime.md#rt-cmp-curriculum
        - runtime.md#rt-cmp-vision-model
        note: Provider internals are inaccessible. Local history does not establish the existence, substrate,
          form or operations of provider-side accumulated state; no positive provider-memory value is
          assigned.
      records:
      - memory.md#mem-obj-memory
      - runtime.md#rt-rte-learning-admission
      - memory.md#mem-obj-memory-journal
      - runtime.md#rt-rte-lineage-recovery
      - memory.md#mem-obj-work-log
      - memory.md#mem-rte-worklog-fold
      - memory.md#mem-obj-curriculum-notes
      - memory.md#mem-obj-learning-diagnosis
      - runtime.md#rt-rte-curriculum-search
      - memory.md#mem-obj-verifier-scratch
      - memory.md#mem-rte-verifier-replay
      - memory.md#mem-obj-durable-images
      - runtime.md#rt-cmp-actor
      - runtime.md#rt-cmp-verifier
      - runtime.md#rt-cmp-curriculum
      - runtime.md#rt-cmp-vision-model
      note: Inspected local retained objects use files and Python state. Static repository code is not
        use-derived repo memory, and remote weights are not evidenced as an updated memory substrate.
        Recovery variants and possible opaque provider-side accumulated state remain unresolved; positives
        establish existence, not complete enumeration.
    representational_form:
      assessment: partial
      units:
      - scope: Bank lessons consumed as Actor advice versus arbitrary bank programs/data
        assessment: partial
        findings:
        - value: natural-language
          basis: afforded
          records:
          - memory.md#mem-obj-memory
          - runtime.md#rt-bap-actor-method
          note: Charters request lessons and later Actors interpret retrieved advice.
        records:
        - memory.md#mem-obj-memory
        - runtime.md#rt-bap-actor-method
        note: Requested prose/advice has a known model-interpreted path. Arbitrary bytes and possible
          scripts have no supplied generated instance or fixed-rule consumer, so their form is not resolved.
      - scope: Journal counts, hashes, timestamps, outcomes and manifests at host admission
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-memory-journal
          - runtime.md#rt-rte-lineage-recovery
          - workflow.md#wf-rte-phase-transition
          note: Fixed code compares manifest/hash/status fields for recovery and phase admission.
        records:
        - memory.md#mem-obj-memory-journal
        - runtime.md#rt-rte-lineage-recovery
        - workflow.md#wf-rte-phase-transition
        note: This unit excludes copied bank payload bytes, whose form follows the bank unit.
      - scope: WORK LOG, deterministic digest, restart handoff and strategy advice at Actor
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-work-log
          - memory.md#mem-rte-worklog-fold
          note: Later Actor calls receive summary or shortened message text and optional advice.
        records:
        - memory.md#mem-obj-work-log
        - memory.md#mem-rte-worklog-fold
        note: All inspected alternatives deliver interpreted text, not parametric updates.
      - scope: Curriculum notes and Actor diagnosis at Curriculum
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-curriculum-notes
          - memory.md#mem-obj-learning-diagnosis
          - runtime.md#rt-rte-curriculum-search
          note: These products supply notes, hypotheses and outcome explanations to later model calls.
        records:
        - memory.md#mem-obj-curriculum-notes
        - memory.md#mem-obj-learning-diagnosis
        - runtime.md#rt-rte-curriculum-search
        note: Free-form notes and concise conclusions are interpreted by Curriculum; no actual claim instance
          is supplied.
      - scope: Retained verdict/status and bank-manifest fields at Curriculum/recovery routing code
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-memory-journal
          - workflow.md#wf-rte-phase-transition
          note: Hashes and terminal status/verdict fields have fixed admission rules.
        records:
        - runtime.md#rt-rte-curriculum-search
        - memory.md#mem-obj-memory-journal
        - workflow.md#wf-rte-phase-transition
        note: Fixed-rule fields are distinct from accompanying report prose.
      - scope: Verifier substantive replay of action JSON, textual observations and reasoning
        assessment: partial
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-rte-verifier-replay
          note: Parsed action categories determine substantive checkpoint and replay inclusion.
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-rte-verifier-replay
          note: Preserved textual results and valid action reasoning reach the next Verifier call.
        records:
        - memory.md#mem-rte-verifier-replay
        note: Parsed Program/Look categories and preserved text are known. Nontext observations have no
          controlled form established here.
      - scope: Image archive identity/schema metadata versus delivered pixels
        assessment: partial
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-durable-images
          note: Archive schema and identity metadata govern rehydration and attachment identity handling.
        records:
        - memory.md#mem-obj-durable-images
        note: Schema, MIME and digest metadata have fixed rules; image pixels are nontext observations,
          not natural-language descriptions or distributed model parameters.
      - scope: Verifier private scratch payload
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-verifier-scratch
        note: Opaque notes/scripts/data are possible; archive preservation cannot classify the consumed
          payload.
      - scope: 'Other dispatched recovery variants: unverified practice, post-target learning, ready-target
          replacement and remaining wave recovery'
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-lineage-recovery
        note: Variant bodies were not fully inspected; their retained parts and this axis cannot be completely
          classified.
      - scope: Provider-side state accumulated through use, if any, behind the Actor, Verifier, Curriculum
          and vision endpoints
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-actor
        - runtime.md#rt-cmp-verifier
        - runtime.md#rt-cmp-curriculum
        - runtime.md#rt-cmp-vision-model
        note: Provider internals are inaccessible. Local history does not establish the existence, substrate,
          form or operations of provider-side accumulated state; no positive provider-memory value is
          assigned.
      records:
      - memory.md#mem-obj-memory
      - runtime.md#rt-bap-actor-method
      - memory.md#mem-obj-memory-journal
      - runtime.md#rt-rte-lineage-recovery
      - workflow.md#wf-rte-phase-transition
      - memory.md#mem-obj-work-log
      - memory.md#mem-rte-worklog-fold
      - memory.md#mem-obj-curriculum-notes
      - memory.md#mem-obj-learning-diagnosis
      - runtime.md#rt-rte-curriculum-search
      - memory.md#mem-rte-verifier-replay
      - memory.md#mem-obj-durable-images
      - memory.md#mem-obj-verifier-scratch
      - runtime.md#rt-cmp-actor
      - runtime.md#rt-cmp-verifier
      - runtime.md#rt-cmp-curriculum
      - runtime.md#rt-cmp-vision-model
      note: Forms are split by operative part and consumption. No generated script or opaque scratch payload
        is classified from its filename; image metadata does not classify pixels. Recovery variants and
        possible opaque provider-side accumulated state remain unresolved; positives establish existence,
        not complete enumeration.
    lineage:
      assessment: partial
      units:
      - scope: Bank downstream distillation and revision versus initial attached content
        assessment: partial
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-memory
          - runtime.md#rt-rte-learning-admission
          note: Same Actor chooses and writes the draft/reconciled tree.
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-rte-learning-admission
          - epistemic.md#epi-rte-memory-proposal
          note: Actor trajectory and terminal evidence feed the admitted later-use bank.
        records:
        - memory.md#mem-obj-memory
        - runtime.md#rt-rte-learning-admission
        - epistemic.md#epi-rte-memory-proposal
        note: Known downstream authorship/extraction does not resolve initial supplied-tree provenance.
      - scope: Exact-tree bank snapshots and journal metadata
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-memory-journal
          note: Host packages admitted bytes and generates counts/hashes/outcome metadata without producing
            new lessons.
        records:
        - memory.md#mem-obj-memory-journal
        note: Copied bank payload provenance remains that of its source tree; this unit classifies snapshot
          construction only.
      - scope: WORK LOG model summary and restart synthesis
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-work-log
          - memory.md#mem-rte-worklog-fold
          note: A model writes the summary/handoff meaning.
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-work-log
          - memory.md#mem-rte-worklog-fold
          note: Actor session history supplies the selected source material.
        records:
        - memory.md#mem-obj-work-log
        - memory.md#mem-rte-worklog-fold
        note: Selected older turns or last 60 messages are the explicit derivation inputs.
      - scope: WORK LOG deterministic fallback
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-work-log
          - memory.md#mem-rte-worklog-fold
          note: Code creates shortened digest lines on empty model output.
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-rte-worklog-fold
          note: Digest source is the selected prior messages.
        records:
        - memory.md#mem-obj-work-log
        - memory.md#mem-rte-worklog-fold
        note: Fallback is separately retained; it is not model authorship.
      - scope: Curriculum notes reasoning path
        assessment: partial
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-curriculum-notes
          - runtime.md#rt-rte-curriculum-search
          note: Curriculum writes free-form notes and host retains audited nonempty replacements.
        records:
        - memory.md#mem-obj-curriculum-notes
        - runtime.md#rt-rte-curriculum-search
        note: Model authorship is known. Particular hypotheses and exact derivation from mixed target/outcome/diagnosis/practice
          inputs are not supplied.
      - scope: Actor learning diagnosis
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-learning-diagnosis
          - runtime.md#rt-rte-learning-admission
          note: Same Actor writes concise conclusions and hypotheses after learning.
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-learning-diagnosis
          - runtime.md#rt-rte-learning-admission
          note: Terminal evidence and Actor experience feed the diagnosis delivered to Curriculum.
        records:
        - memory.md#mem-obj-learning-diagnosis
        - runtime.md#rt-rte-learning-admission
        note: This is a distinct trace-derived product, not the whole bank.
      - scope: Verifier replay checkpoint construction
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-rte-verifier-replay
          note: Host reconstructs substantive action/observation pairs by category.
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-rte-verifier-replay
          note: Previously recorded Verifier activity supplies retained pairs.
        records:
        - memory.md#mem-rte-verifier-replay
        note: Structural extraction is known, without assigning truth to retained observations.
      - scope: Durable image archive and rehydration
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-durable-images
          note: Image observations enter the role history from supplied observations.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-durable-images
          note: Host generates archive schema and attachment identity metadata.
        records:
        - memory.md#mem-obj-durable-images
        note: Imported observation bytes are preserved; their upstream instrument warrant remains unknown.
      - scope: Verifier scratch contents and preexisting archive provenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-verifier-scratch
        note: Export/import preserves opaque bytes but does not reveal their content-level derivation.
      - scope: 'Other dispatched recovery variants: unverified practice, post-target learning, ready-target
          replacement and remaining wave recovery'
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-lineage-recovery
        note: Variant bodies were not fully inspected; their retained parts and this axis cannot be completely
          classified.
      - scope: Provider-side state accumulated through use, if any, behind the Actor, Verifier, Curriculum
          and vision endpoints
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-actor
        - runtime.md#rt-cmp-verifier
        - runtime.md#rt-cmp-curriculum
        - runtime.md#rt-cmp-vision-model
        note: Provider internals are inaccessible. Local history does not establish the existence, substrate,
          form or operations of provider-side accumulated state; no positive provider-memory value is
          assigned.
      records:
      - memory.md#mem-obj-memory
      - runtime.md#rt-rte-learning-admission
      - epistemic.md#epi-rte-memory-proposal
      - memory.md#mem-obj-memory-journal
      - memory.md#mem-obj-work-log
      - memory.md#mem-rte-worklog-fold
      - memory.md#mem-obj-curriculum-notes
      - runtime.md#rt-rte-curriculum-search
      - memory.md#mem-obj-learning-diagnosis
      - memory.md#mem-rte-verifier-replay
      - memory.md#mem-obj-durable-images
      - memory.md#mem-obj-verifier-scratch
      - runtime.md#rt-rte-lineage-recovery
      - runtime.md#rt-cmp-actor
      - runtime.md#rt-cmp-verifier
      - runtime.md#rt-cmp-curriculum
      - runtime.md#rt-cmp-vision-model
      note: Known construction paths do not resolve initial bank provenance, individual Curriculum claim
        derivations or opaque scratch content. Recovery variants and possible opaque provider-side accumulated
        state remain unresolved; positives establish existence, not complete enumeration.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Retained Actor experience and terminal evidence at same-Actor bank/diagnosis update
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - runtime.md#rt-rte-learning-admission
          - memory.md#mem-obj-learning-diagnosis
          - epistemic.md#epi-rte-memory-proposal
          note: Retained activity and feedback feed a durable behavior-shaping bank and Curriculum diagnosis.
        records:
        - runtime.md#rt-rte-learning-admission
        - memory.md#mem-obj-learning-diagnosis
        - epistemic.md#epi-rte-memory-proposal
        note: Learning is the update consumer effect, separate from downstream advice and demonstrated
          improved capacity.
      - scope: Bank advice at fresh Actor and optional Curriculum reader
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-memory
          - runtime.md#rt-bap-actor-method
          - runtime.md#rt-rte-curriculum-search
          note: Selected retained advice/evidence supplies context for task solving or Curriculum decisions.
        records:
        - memory.md#mem-obj-memory
        - runtime.md#rt-bap-actor-method
        - runtime.md#rt-rte-curriculum-search
        note: The inspected advice channel is fallible model-interpreted context, not an enforced lesson
          interpreter.
      - scope: Journal manifests and saved lineage fields at recovery and phase gate
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-memory-journal
          - runtime.md#rt-rte-lineage-recovery
          - workflow.md#wf-rte-phase-transition
          note: Retained hashes and manifests provide comparison criteria for admissible continuation.
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-rte-lineage-recovery
          - workflow.md#wf-rte-phase-transition
          note: Mismatch against retained lineage/hash expectations vetoes recovery or phase progression.
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-rte-lineage-recovery
          - workflow.md#wf-rte-phase-transition
          note: Accepted checkpoints and banks select resumed or subsequent phase inputs.
        records:
        - memory.md#mem-obj-memory-journal
        - runtime.md#rt-rte-lineage-recovery
        - workflow.md#wf-rte-phase-transition
        note: This is authority of retained metadata, not of static admission code.
      - scope: WORK LOG at subsequent Actor and fresh stalled attempt
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-work-log
          - memory.md#mem-rte-worklog-fold
          note: Summary/handoff supplies retained factual and strategic context to later calls.
        records:
        - memory.md#mem-obj-work-log
        - memory.md#mem-rte-worklog-fold
        note: Model interpretation of summary/advice is distinct from code thresholds.
      - scope: Retained older Actor turns/current log at summarizer or restart synthesis
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-obj-work-log
          - memory.md#mem-rte-worklog-fold
          note: Recorded experience feeds automatically retained continuation material for later Actor
            decisions.
        records:
        - memory.md#mem-obj-work-log
        - memory.md#mem-rte-worklog-fold
        note: This is the update side of the summary chain.
      - scope: Curriculum notes, diagnosis and accumulated outcome reports at later Curriculum
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-curriculum-notes
          - memory.md#mem-obj-learning-diagnosis
          - runtime.md#rt-rte-curriculum-search
          note: Later project/readiness choices interpret notes, hypotheses and outcome evidence.
        records:
        - memory.md#mem-obj-curriculum-notes
        - memory.md#mem-obj-learning-diagnosis
        - runtime.md#rt-rte-curriculum-search
        note: Free-form content supplies decision context; it does not itself enforce READY/STALLED.
      - scope: Retained Curriculum experience at private-note update
        assessment: partial
        findings:
        - value: learning
          basis: afforded
          records:
          - memory.md#mem-obj-curriculum-notes
          - runtime.md#rt-rte-curriculum-search
          note: The wired iterative role has outcome-fed notes available to shape future project choice.
        records:
        - memory.md#mem-obj-curriculum-notes
        - runtime.md#rt-rte-curriculum-search
        note: The retained notes are authored over supplied outcomes and practice evidence. Particular
          trace dependence of each note replacement is not evidenced.
      - scope: Verifier retained textual evidence, image observations and reasoning at subsequent calls
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-rte-verifier-replay
          - memory.md#mem-obj-durable-images
          note: Substantive replay and exact image rehydration supply prior inspection evidence.
        records:
        - memory.md#mem-rte-verifier-replay
        - memory.md#mem-obj-durable-images
        note: Delivery is evidence/context supply, not proof of correct reliance.
      - scope: Opaque bank executable/data alternatives and Verifier scratch payload effects
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory
        - memory.md#mem-obj-verifier-scratch
        note: No actual payload or differentiated consumer effect establishes additional authority; potential
          execution is not enforcement, instruction or validation evidence.
      - scope: 'Other dispatched recovery variants: unverified practice, post-target learning, ready-target
          replacement and remaining wave recovery'
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-lineage-recovery
        note: Variant bodies were not fully inspected; their retained parts and this axis cannot be completely
          classified.
      - scope: Provider-side state accumulated through use, if any, behind the Actor, Verifier, Curriculum
          and vision endpoints
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-actor
        - runtime.md#rt-cmp-verifier
        - runtime.md#rt-cmp-curriculum
        - runtime.md#rt-cmp-vision-model
        note: Provider internals are inaccessible. Local history does not establish the existence, substrate,
          form or operations of provider-side accumulated state; no positive provider-memory value is
          assigned.
      records:
      - runtime.md#rt-rte-learning-admission
      - memory.md#mem-obj-learning-diagnosis
      - epistemic.md#epi-rte-memory-proposal
      - memory.md#mem-obj-memory
      - runtime.md#rt-bap-actor-method
      - runtime.md#rt-rte-curriculum-search
      - memory.md#mem-obj-memory-journal
      - runtime.md#rt-rte-lineage-recovery
      - workflow.md#wf-rte-phase-transition
      - memory.md#mem-obj-work-log
      - memory.md#mem-rte-worklog-fold
      - memory.md#mem-obj-curriculum-notes
      - memory.md#mem-rte-verifier-replay
      - memory.md#mem-obj-durable-images
      - memory.md#mem-obj-verifier-scratch
      - runtime.md#rt-cmp-actor
      - runtime.md#rt-cmp-verifier
      - runtime.md#rt-cmp-curriculum
      - runtime.md#rt-cmp-vision-model
      note: Update learning, downstream knowledge and host metadata controls are classified separately.
        No ranking value follows from foreground Actor discretionary searching, and no standing instruction
        value follows merely from fallible advice. Recovery variants and possible opaque provider-side
        accumulated state remain unresolved; positives establish existence, not complete enumeration.
    write_agency:
      assessment: partial
      units:
      - scope: Terminal bank and diagnosis proposal, audit and publication
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-learning-admission
          - memory.md#mem-obj-learning-diagnosis
          note: Actor decides content/readiness; host boundary checks admit or reject without a per-content
            operator decision.
        records:
        - runtime.md#rt-rte-learning-admission
        - memory.md#mem-obj-learning-diagnosis
        note: Human launch is not per-content approval.
      - scope: Journal/checkpoint creation and exact-tree packaging
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-memory-journal
          note: Host writes admitted-tree archives and lineage metadata at configured boundaries.
        records:
        - memory.md#mem-obj-memory-journal
        note: Host snapshot scheduling is a distinct admission mechanism.
      - scope: WORK LOG folding, deterministic fallback, restart handoff and optional strategy advice
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-worklog-fold
          - memory.md#mem-obj-work-log
          note: Thresholds, fallback and restart eligibility admit continuation text without human approval.
        records:
        - memory.md#mem-rte-worklog-fold
        - memory.md#mem-obj-work-log
        note: All documented alternatives are scheduled and admitted by software/model.
      - scope: Curriculum notes nonempty replacement
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-curriculum-notes
          - runtime.md#rt-rte-curriculum-search
          note: Curriculum-authored nonempty notes replace session notes after host audit.
        records:
        - memory.md#mem-obj-curriculum-notes
        - runtime.md#rt-rte-curriculum-search
        note: Authorship is not the admission classification; audited model replacement is software/model
          control.
      - scope: Verifier substantive checkpoint/replay and image archiving
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-verifier-replay
          - memory.md#mem-obj-durable-images
          note: Host retains action-category checkpoints, observations and image identities.
        records:
        - memory.md#mem-rte-verifier-replay
        - memory.md#mem-obj-durable-images
        note: Structural host selection is not human approval.
      - scope: Verifier scratch content edits
        assessment: partial
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-verifier-scratch
          note: Verifier writes private scratch through its executor and host lifecycle retains/exports
            it.
        records:
        - memory.md#mem-obj-verifier-scratch
        note: Verifier production and host retention/export are wired; initial scratch contents and all
          per-file content controls are not supplied.
      - scope: Initial supplied bank and unspecified direct write_memory API caller
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory
        - runtime.md#rt-rte-learning-admission
        note: Initial author/approval control is unknown. Direct replacement is a storage capability with
          no identified caller admission mechanism; neither establishes manual or automatic content admission.
      - scope: 'Other dispatched recovery variants: unverified practice, post-target learning, ready-target
          replacement and remaining wave recovery'
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-lineage-recovery
        note: Variant bodies were not fully inspected; their retained parts and this axis cannot be completely
          classified.
      - scope: Provider-side state accumulated through use, if any, behind the Actor, Verifier, Curriculum
          and vision endpoints
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-actor
        - runtime.md#rt-cmp-verifier
        - runtime.md#rt-cmp-curriculum
        - runtime.md#rt-cmp-vision-model
        note: Provider internals are inaccessible. Local history does not establish the existence, substrate,
          form or operations of provider-side accumulated state; no positive provider-memory value is
          assigned.
      records:
      - runtime.md#rt-rte-learning-admission
      - memory.md#mem-obj-learning-diagnosis
      - memory.md#mem-obj-memory-journal
      - memory.md#mem-rte-worklog-fold
      - memory.md#mem-obj-work-log
      - memory.md#mem-obj-curriculum-notes
      - runtime.md#rt-rte-curriculum-search
      - memory.md#mem-rte-verifier-replay
      - memory.md#mem-obj-durable-images
      - memory.md#mem-obj-verifier-scratch
      - memory.md#mem-obj-memory
      - runtime.md#rt-rte-lineage-recovery
      - runtime.md#rt-cmp-actor
      - runtime.md#rt-cmp-verifier
      - runtime.md#rt-cmp-curriculum
      - runtime.md#rt-cmp-vision-model
      note: Inspected use-derived admission is automatic. Operator launch, selecting a recovery plan or
        choosing an attachment path does not establish manual approval of the retained content. Recovery
        variants and possible opaque provider-side accumulated state remain unresolved; positives establish
        existence, not complete enumeration.
    curation_operations:
      assessment: partial
      units:
      - scope: Actor old-turn folding into retained WORK LOG and restart handoff
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-rte-worklog-fold
          - memory.md#mem-obj-work-log
          note: Prior turns are compressed into smaller continuation text.
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-rte-worklog-fold
          note: Model revises the existing WORK LOG with newly folded turns.
        - value: decay
          basis: wired
          records:
          - memory.md#mem-rte-worklog-fold
          note: Character caps, head/tail elision and replacement remove retained visible detail from
            later context.
        records:
        - memory.md#mem-rte-worklog-fold
        - memory.md#mem-obj-work-log
        note: Implemented model summary and deterministic fallback reduce selected retained trace content;
          a fidelity defect does not make this synthesis.
      - scope: Bank whole-corpus revision and withdrawal
        assessment: partial
        findings:
        - value: evolve
          basis: afforded
          records:
          - memory.md#mem-obj-memory
          - runtime.md#rt-rte-learning-admission
          note: Actor can revise existing files and publish a replacement tree.
        - value: evolve
          basis: claimed
          records:
          - epistemic.md#epi-rte-memory-proposal
          - runtime.md#rt-rte-learning-admission
          note: Whole-corpus instructions request qualification/revision of stale or unsupported claims.
        - value: invalidate
          basis: afforded
          records:
          - runtime.md#rt-rte-learning-admission
          - memory.md#mem-obj-memory-journal
          note: Whole-tree replacement can withdraw active advice while historical snapshots retain removed
            bytes.
        - value: consolidate
          basis: claimed
          records:
          - runtime.md#rt-rte-learning-admission
          - epistemic.md#epi-rte-memory-proposal
          note: Distillation requests reusable reduced lessons from the retained trajectory.
        records:
        - memory.md#mem-obj-memory
        - runtime.md#rt-rte-learning-admission
        - epistemic.md#epi-rte-memory-proposal
        - memory.md#mem-obj-memory-journal
        note: Add/revise/delete capability and requested semantic reconciliation are distinguished. No
          generated bank proves which semantic operation occurred; arbitrary additions do not establish
          synthesis.
      - scope: Curriculum private-note replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-obj-curriculum-notes
          note: The implemented nonempty audited replacement revises session.notes.
        records:
        - memory.md#mem-obj-curriculum-notes
        note: Nonempty notes replace prior notes; semantic content is not supplied.
      - scope: Image attachment identity deduplication
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records:
          - memory.md#mem-obj-durable-images
          note: Host deduplicates repeated image attachment identities while retaining full bytes.
        records:
        - memory.md#mem-obj-durable-images
        note: Identity-based duplicate suppression is local attachment maintenance, not semantic evidence
          ranking.
      - scope: Verifier substantive live replay filtering
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-rte-verifier-replay
          note: Checkpoint/replay excludes actionless pairs from future model-visible context.
        records:
        - memory.md#mem-rte-verifier-replay
        note: Raw artifacts retain excluded pairs; live retained context drops actionless narration/nudges.
      - scope: Opaque bank contents, scratch transformations and initial memory curation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory
        - memory.md#mem-obj-verifier-scratch
        note: No payload instance establishes other semantic curation. Archive/copy operations alone are
          not consolidation, synthesis or promotion.
      - scope: 'Other dispatched recovery variants: unverified practice, post-target learning, ready-target
          replacement and remaining wave recovery'
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-lineage-recovery
        note: Variant bodies were not fully inspected; their retained parts and this axis cannot be completely
          classified.
      - scope: Provider-side state accumulated through use, if any, behind the Actor, Verifier, Curriculum
          and vision endpoints
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-actor
        - runtime.md#rt-cmp-verifier
        - runtime.md#rt-cmp-curriculum
        - runtime.md#rt-cmp-vision-model
        note: Provider internals are inaccessible. Local history does not establish the existence, substrate,
          form or operations of provider-side accumulated state; no positive provider-memory value is
          assigned.
      records:
      - memory.md#mem-rte-worklog-fold
      - memory.md#mem-obj-work-log
      - memory.md#mem-obj-memory
      - runtime.md#rt-rte-learning-admission
      - epistemic.md#epi-rte-memory-proposal
      - memory.md#mem-obj-memory-journal
      - memory.md#mem-obj-curriculum-notes
      - memory.md#mem-obj-durable-images
      - memory.md#mem-rte-verifier-replay
      - memory.md#mem-obj-verifier-scratch
      - runtime.md#rt-rte-lineage-recovery
      - runtime.md#rt-cmp-actor
      - runtime.md#rt-cmp-verifier
      - runtime.md#rt-cmp-curriculum
      - runtime.md#rt-cmp-vision-model
      note: 'Transformation evidence stays local: WORK LOG compression and attachment dedup are wired;
        bank semantic repairs are requested or afforded, not observed. No inferred synthesis is assigned
        to indeterminate model output. Recovery variants and possible opaque provider-side accumulated
        state remain unresolved; positives establish existence, not complete enumeration.'
    read_back_direction:
      assessment: partial
      units:
      - scope: Bank attachment and subsequent Actor-requested content reads
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-task-execution
          - memory.md#mem-obj-memory
          note: Host supplies the chosen complete bank copy and names/sizes inventory without a file-body
            request.
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-bap-actor-method
          - memory.md#mem-obj-memory
          note: Foreground Actor requests selected retained file contents through Programs.
        records:
        - runtime.md#rt-rte-task-execution
        - memory.md#mem-obj-memory
        - runtime.md#rt-bap-actor-method
        note: Automatic snapshot/inventory supply and later requested file returns are separate operations
          in one chain.
      - scope: Optional canonical bank access at Curriculum
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-curriculum-search
          note: Configured mode automatically supplies the bank evidence copy or empty ablation attachment.
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-curriculum-search
          - memory.md#mem-obj-memory
          note: Curriculum can inspect attached canonical memory as evidence.
        records:
        - runtime.md#rt-rte-curriculum-search
        - memory.md#mem-obj-memory
        note: Software selects evidence-bank or empty-tree mode; discretionary file inspection remains
          separate.
      - scope: WORK LOG and restart continuation delivery
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-worklog-fold
          - memory.md#mem-obj-work-log
          note: Code injects WORK LOG plus tail or handoff into subsequent/fresh calls.
        records:
        - memory.md#mem-rte-worklog-fold
        - memory.md#mem-obj-work-log
        note: Later Actor context is automatically assembled from retained summary/handoff.
      - scope: Curriculum private notes, role history, outcomes and diagnosis delivery
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-curriculum-notes
          - memory.md#mem-obj-learning-diagnosis
          - runtime.md#rt-rte-curriculum-search
          note: Host reinserts session notes and latest outcomes/diagnosis into later Curriculum rounds.
        records:
        - memory.md#mem-obj-curriculum-notes
        - memory.md#mem-obj-learning-diagnosis
        - runtime.md#rt-rte-curriculum-search
        note: Repeated charters/context receive retained products without a new content request.
      - scope: Verifier checkpoint, pending observations and image rehydration
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-verifier-replay
          - memory.md#mem-obj-durable-images
          note: Host restores selected substantive history and exact pending observation/pixels.
        records:
        - memory.md#mem-rte-verifier-replay
        - memory.md#mem-obj-durable-images
        note: Recovery state feeds the next provider invocation automatically.
      - scope: Bank checkpoints/manifests at checked phase/recovery consumption
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-lineage-recovery
          - workflow.md#wf-rte-phase-transition
          - memory.md#mem-obj-memory-journal
          note: Host restores accepted saved histories/banks and supplies phase checkpoint trees as later
            invocation inputs.
        records:
        - memory.md#mem-obj-memory-journal
        - runtime.md#rt-rte-lineage-recovery
        - workflow.md#wf-rte-phase-transition
        note: Operator plan choice is upstream selection input, not a request by the later resumed role
          for each retained object.
      - scope: Opaque Verifier scratch content access
        assessment: partial
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-verifier-scratch
          note: Host can restore an exported private scratch archive to the new executor.
        records:
        - memory.md#mem-obj-verifier-scratch
        note: Lifecycle restore is known; no actual scratch reads identify all content read-back paths.
      - scope: 'Other dispatched recovery variants: unverified practice, post-target learning, ready-target
          replacement and remaining wave recovery'
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-lineage-recovery
        note: Variant bodies were not fully inspected; their retained parts and this axis cannot be completely
          classified.
      - scope: Provider-side state accumulated through use, if any, behind the Actor, Verifier, Curriculum
          and vision endpoints
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-actor
        - runtime.md#rt-cmp-verifier
        - runtime.md#rt-cmp-curriculum
        - runtime.md#rt-cmp-vision-model
        note: Provider internals are inaccessible. Local history does not establish the existence, substrate,
          form or operations of provider-side accumulated state; no positive provider-memory value is
          assigned.
      records:
      - runtime.md#rt-rte-task-execution
      - memory.md#mem-obj-memory
      - runtime.md#rt-bap-actor-method
      - runtime.md#rt-rte-curriculum-search
      - memory.md#mem-rte-worklog-fold
      - memory.md#mem-obj-work-log
      - memory.md#mem-obj-curriculum-notes
      - memory.md#mem-obj-learning-diagnosis
      - memory.md#mem-rte-verifier-replay
      - memory.md#mem-obj-durable-images
      - memory.md#mem-obj-memory-journal
      - runtime.md#rt-rte-lineage-recovery
      - workflow.md#wf-rte-phase-transition
      - memory.md#mem-obj-verifier-scratch
      - runtime.md#rt-cmp-actor
      - runtime.md#rt-cmp-verifier
      - runtime.md#rt-cmp-curriculum
      - runtime.md#rt-cmp-vision-model
      note: Direction distinguishes automatic context/attachment delivery from requested file reads. Stored
        journals without a consumer are not counted merely for existing; classified journals have evidenced
        recovery/phase consumers. Recovery variants and possible opaque provider-side accumulated state
        remain unresolved; positives establish existence, not complete enumeration.
    read_back_signal:
      assessment: partial
      units:
      - scope: Host task bank attachment push
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-task-execution
          - memory.md#mem-obj-memory
          note: Configured bank availability selects the full attached tree and names/sizes inventory.
        records:
        - runtime.md#rt-rte-task-execution
        - memory.md#mem-obj-memory
        note: Trigger is task/attempt attachment; configured snapshot and availability select the complete
          bank and inventory, not relevance-ranked bodies.
      - scope: Curriculum bank exposure and note/outcome reinsertion
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-curriculum-search
          - memory.md#mem-obj-curriculum-notes
          - memory.md#mem-obj-learning-diagnosis
          note: Whole configured attachment and role-local accumulated products are supplied, without
            targeted semantic retrieval.
        records:
        - runtime.md#rt-rte-curriculum-search
        - memory.md#mem-obj-curriculum-notes
        - memory.md#mem-obj-learning-diagnosis
        note: Trigger is next Curriculum round; mode selects evidence bank versus empty tree and session
          availability selects retained notes/latest outcome.
      - scope: WORK LOG summary/handoff push
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-worklog-fold
          - memory.md#mem-obj-work-log
          note: Availability and restart eligibility select the retained log/handoff for delivery.
        records:
        - memory.md#mem-rte-worklog-fold
        - memory.md#mem-obj-work-log
        note: Trigger is subsequent call or stalled restart; summary state and eligibility/budget select
          continuation text. Semantic selection happened at writing, not push retrieval.
      - scope: Verifier substantive replay and image delivery
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-verifier-replay
          - memory.md#mem-obj-durable-images
          note: Structural Program/Look checkpoint rules select retained role-local context; image digests
            audit identities, not targeted relevant evidence.
        records:
        - memory.md#mem-rte-verifier-replay
        - memory.md#mem-obj-durable-images
        note: Trigger is decoder/segment recovery; parsed action category and checkpoint boundary select
          substantive history and pending exact observations.
      - scope: Checked lineage and phase-bank push
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-lineage-recovery
          - workflow.md#wf-rte-phase-transition
          - memory.md#mem-obj-memory-journal
          note: Accepted lineage/checkpoint and phase configuration choose entire restored input bundles.
        records:
        - runtime.md#rt-rte-lineage-recovery
        - workflow.md#wf-rte-phase-transition
        - memory.md#mem-obj-memory-journal
        note: Trigger is recovery/phase launch; plan/checkpoint lineage chooses the saved boundary, with
          hashes checking consistency rather than matching relevant content to a query.
      - scope: Verifier private scratch archive restoration selection
        assessment: partial
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-verifier-scratch
          note: Export availability and recovery tolerance choose whether a whole scratch archive is restored.
        records:
        - memory.md#mem-obj-verifier-scratch
        note: Available archive versus fresh scratch is known; contents and finer selection remain opaque.
      - scope: Foreground Actor requested file-body returns only
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-bap-actor-method
        - memory.md#mem-obj-memory
        - runtime.md#rt-rte-task-execution
        note: This operation is pull. A requested filename and Actor relevance judgment do not establish
          an identifier-based or inferred-judgment push selector.
      - scope: 'Other dispatched recovery variants: unverified practice, post-target learning, ready-target
          replacement and remaining wave recovery'
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-lineage-recovery
        note: Variant bodies were not fully inspected; their retained parts and this axis cannot be completely
          classified.
      - scope: Provider-side state accumulated through use, if any, behind the Actor, Verifier, Curriculum
          and vision endpoints
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-actor
        - runtime.md#rt-cmp-verifier
        - runtime.md#rt-cmp-curriculum
        - runtime.md#rt-cmp-vision-model
        note: Provider internals are inaccessible. Local history does not establish the existence, substrate,
          form or operations of provider-side accumulated state; no positive provider-memory value is
          assigned.
      records:
      - runtime.md#rt-rte-task-execution
      - memory.md#mem-obj-memory
      - runtime.md#rt-rte-curriculum-search
      - memory.md#mem-obj-curriculum-notes
      - memory.md#mem-obj-learning-diagnosis
      - memory.md#mem-rte-worklog-fold
      - memory.md#mem-obj-work-log
      - memory.md#mem-rte-verifier-replay
      - memory.md#mem-obj-durable-images
      - runtime.md#rt-rte-lineage-recovery
      - workflow.md#wf-rte-phase-transition
      - memory.md#mem-obj-memory-journal
      - memory.md#mem-obj-verifier-scratch
      - runtime.md#rt-bap-actor-method
      - runtime.md#rt-cmp-actor
      - runtime.md#rt-cmp-verifier
      - runtime.md#rt-cmp-curriculum
      - runtime.md#rt-cmp-vision-model
      note: Inspected push selectors are structural availability/mode/checkpoint choices. No image digest,
        requested filename, or archive catalog alone establishes identifier-based push; model-selected
        compression meaning is not a later push signal. Recovery variants and possible opaque provider-side
        accumulated state remain unresolved; positives establish existence, not complete enumeration.
    trace_learning:
      assessment: partial
      units:
      - scope: Terminal bank distillation and Actor diagnosis
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-learning-admission
          - memory.md#mem-obj-learning-diagnosis
          - memory.md#mem-obj-memory
          note: Recorded Actor experience plus final Verifier evidence feed an automatically admitted
            durable bank and diagnosis for later Actor/Curriculum context.
        records:
        - runtime.md#rt-rte-learning-admission
        - memory.md#mem-obj-learning-diagnosis
        - memory.md#mem-obj-memory
        note: Qualifying automatic write and later consumers are wired; improvement and compliant semantic
          criticism are not observed.
      - scope: Actor folded WORK LOG, fallback and synthesized restart handoff
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-worklog-fold
          - memory.md#mem-obj-work-log
          note: Prior turns feed automatic retained continuation artifacts consumed as later context.
        records:
        - memory.md#mem-rte-worklog-fold
        - memory.md#mem-obj-work-log
        note: Both lossy model text and deterministic digest persist for later Actor invocations.
      - scope: Curriculum private-note update
        assessment: partial
        findings:
        - value: 'yes'
          basis: afforded
          records:
          - memory.md#mem-obj-curriculum-notes
          - runtime.md#rt-rte-curriculum-search
          note: Outcome-fed role reasoning can produce retained notes reinserted in future project decisions.
        records:
        - memory.md#mem-obj-curriculum-notes
        - runtime.md#rt-rte-curriculum-search
        note: Iterative notes use supplied outcomes/diagnosis/practice evidence, but no generated note
          shows each replacement's trace dependence or exact source selection.
      - scope: Verifier substantive replay, raw images and scratch versus derived behavior-shaping update
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-verifier-replay
        - memory.md#mem-obj-durable-images
        - memory.md#mem-obj-verifier-scratch
        note: Replay/image retention preserve selected raw activity, not an evidenced newly extracted
          lesson. Opaque scratch could contain derived notes, but no artifact or qualifying write establishes
          it. No bounded absence record warrants a local no.
      - scope: Journal snapshots and initial bank
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-journal
        - memory.md#mem-obj-memory
        note: Snapshots preserve existing derived memory, rather than establishing another trace-fed learning
          write. Initial content has unknown provenance; no bounded absence supports no.
      - scope: 'Other dispatched recovery variants: unverified practice, post-target learning, ready-target
          replacement and remaining wave recovery'
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-lineage-recovery
        note: Variant bodies were not fully inspected; their retained parts and this axis cannot be completely
          classified.
      - scope: Provider-side state accumulated through use, if any, behind the Actor, Verifier, Curriculum
          and vision endpoints
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-actor
        - runtime.md#rt-cmp-verifier
        - runtime.md#rt-cmp-curriculum
        - runtime.md#rt-cmp-vision-model
        note: Provider internals are inaccessible. Local history does not establish the existence, substrate,
          form or operations of provider-side accumulated state; no positive provider-memory value is
          assigned.
      records:
      - runtime.md#rt-rte-learning-admission
      - memory.md#mem-obj-learning-diagnosis
      - memory.md#mem-obj-memory
      - memory.md#mem-rte-worklog-fold
      - memory.md#mem-obj-work-log
      - memory.md#mem-obj-curriculum-notes
      - runtime.md#rt-rte-curriculum-search
      - memory.md#mem-rte-verifier-replay
      - memory.md#mem-obj-durable-images
      - memory.md#mem-obj-verifier-scratch
      - memory.md#mem-obj-memory-journal
      - runtime.md#rt-rte-lineage-recovery
      - runtime.md#rt-cmp-actor
      - runtime.md#rt-cmp-verifier
      - runtime.md#rt-cmp-curriculum
      - runtime.md#rt-cmp-vision-model
      note: The yes values concern durable trace-fed context/advice writes, not parameter training or
        demonstrated improved capacity. Raw trace retention alone is not upgraded to trace learning, and
        no unsupported system-wide no is asserted. Recovery variants and possible opaque provider-side
        accumulated state remain unresolved; positives establish existence, not complete enumeration.
    trace_source:
      assessment: partial
      units:
      - scope: Bank and diagnosis terminal-learning inputs
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - runtime.md#rt-rte-learning-admission
          - memory.md#mem-obj-learning-diagnosis
          - epistemic.md#epi-rte-memory-proposal
          note: Same-context Actor history contains recorded conversational turns used in learning.
        - value: tool-traces
          basis: wired
          records:
          - runtime.md#rt-rte-learning-admission
          - epistemic.md#epi-rte-memory-proposal
          note: Recorded actions, observations and terminal execution feedback feed terminal learning.
        - value: trajectories
          basis: wired
          records:
          - runtime.md#rt-rte-learning-admission
          - epistemic.md#epi-rte-memory-proposal
          note: Linked Actor decisions/actions/observations and terminal Verifier outcomes are consumed
            as multi-step experience in bank and diagnosis production.
        records:
        - runtime.md#rt-rte-learning-admission
        - memory.md#mem-obj-learning-diagnosis
        - epistemic.md#epi-rte-memory-proposal
        note: Recorded Actor interaction and terminal execution/verification evidence supply conversational
          turns, tool feedback and linked multi-step experience. These overlapping source values describe
          the same terminal-learning input without requiring a separately serialized trajectory object.
      - scope: WORK LOG folding, fallback and restart synthesis inputs
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-rte-worklog-fold
          - memory.md#mem-obj-work-log
          note: Recorded older turns or last 60 history messages supply summary/handoff input.
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-rte-worklog-fold
          - memory.md#mem-obj-work-log
          note: Those histories include recorded Program results and environmental feedback retained in
            continuation text.
        records:
        - memory.md#mem-rte-worklog-fold
        - memory.md#mem-obj-work-log
        note: The ENV/YOU rendering does not change original trace origin.
      - scope: Curriculum private-note qualifying update inputs
        assessment: partial
        findings:
        - value: session-logs
          basis: afforded
          records:
          - memory.md#mem-obj-curriculum-notes
          - runtime.md#rt-rte-curriculum-search
          note: Persistent Curriculum role history can feed retained notes.
        - value: tool-traces
          basis: afforded
          records:
          - memory.md#mem-obj-curriculum-notes
          - runtime.md#rt-rte-curriculum-search
          - memory.md#mem-obj-learning-diagnosis
          note: Practice/target execution feedback and diagnosis can feed the retained note update.
        records:
        - memory.md#mem-obj-curriculum-notes
        - runtime.md#rt-rte-curriculum-search
        - memory.md#mem-obj-learning-diagnosis
        note: Outcomes, diagnosis, role history and practice evidence supply supported trace origins;
          exact note-specific dependencies and other mixed target inputs are not supplied.
      - scope: Verifier raw replay/images/scratch, journals and initial bank without established qualifying
          writes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-verifier-replay
        - memory.md#mem-obj-durable-images
        - memory.md#mem-obj-verifier-scratch
        - memory.md#mem-obj-memory-journal
        - memory.md#mem-obj-memory
        note: These routes have no completely assessed absence or evidenced qualifying derived write here.
          Raw activity origin does not by itself authorize trace_source classification for trace learning.
      - scope: 'Other dispatched recovery variants: unverified practice, post-target learning, ready-target
          replacement and remaining wave recovery'
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-lineage-recovery
        note: Variant bodies were not fully inspected; their retained parts and this axis cannot be completely
          classified.
      - scope: Provider-side state accumulated through use, if any, behind the Actor, Verifier, Curriculum
          and vision endpoints
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-cmp-actor
        - runtime.md#rt-cmp-verifier
        - runtime.md#rt-cmp-curriculum
        - runtime.md#rt-cmp-vision-model
        note: Provider internals are inaccessible. Local history does not establish the existence, substrate,
          form or operations of provider-side accumulated state; no positive provider-memory value is
          assigned.
      records:
      - runtime.md#rt-rte-learning-admission
      - memory.md#mem-obj-learning-diagnosis
      - epistemic.md#epi-rte-memory-proposal
      - memory.md#mem-rte-worklog-fold
      - memory.md#mem-obj-work-log
      - memory.md#mem-obj-curriculum-notes
      - runtime.md#rt-rte-curriculum-search
      - memory.md#mem-rte-verifier-replay
      - memory.md#mem-obj-durable-images
      - memory.md#mem-obj-verifier-scratch
      - memory.md#mem-obj-memory-journal
      - memory.md#mem-obj-memory
      - runtime.md#rt-rte-lineage-recovery
      - runtime.md#rt-cmp-actor
      - runtime.md#rt-cmp-verifier
      - runtime.md#rt-cmp-curriculum
      - runtime.md#rt-cmp-vision-model
      note: Source follows original conversational and execution content, not wrapper labels. Terminal
        bank/diagnosis learning consumes linked Actor states/observations, actions and outcomes as trajectories,
        alongside session logs and tool traces. Journal terminal timestamps and decoder events do not add
        event-streams. Recovery variants and possible opaque provider-side accumulated state remain unresolved;
        positives establish existence, not complete enumeration.
---

# RSIAgent memory profile

## Comparison rationale

All positive bases concern inspected wiring, explicit capacity or requested model behavior. No finding is observed or causally supported. Coverage remains partial on every axis: the accepted inventory includes opaque payloads, partially inspected recovery variants and inaccessible provider internals. Local known units do not close those alternatives. Provider weights are runtime components, not demonstrated use-updated memory; possible use-accumulated provider state is retained as an unresolved unit instead of attributing local history properties to it.

The accepted reconciliation supersedes the epistemic bank object with [MEM-OBJ-memory](memory.md#mem-obj-memory) and the epistemic WORK LOG object with [MEM-OBJ-work-log](memory.md#mem-obj-work-log). Classifications cite these canonical objects. The narrower [EPI-RTE-worklog-fold](epistemic.md#epi-rte-worklog-fold) remains distinct from [MEM-RTE-worklog-fold](memory.md#mem-rte-worklog-fold), which also covers restart synthesis and strategy review. No other supersession changes a value.

The bank's arbitrary bytes do not establish one uniform form or authority. Requested prose has an afforded natural-language advice path through [RT-BAP-actor-method](runtime.md#rt-bap-actor-method); scripts/data and opaque scratch remain unresolved. Image schema/identity metadata is symbolic, while pixels have no established value among the controlled forms. Copied journal payloads retain bank uncertainty; manifest fields are separately symbolic inputs to host validation, enforcement and routing ([MEM-OBJ-memory-journal](memory.md#mem-obj-memory-journal), [MEM-OBJ-durable-images](memory.md#mem-obj-durable-images), [MEM-OBJ-verifier-scratch](memory.md#mem-obj-verifier-scratch)).

Learning authority belongs to retained experience at the update consumer; downstream bank/log/diagnosis products supply knowledge as interpreted context. Neither implies improved future capacity. The same-Actor bank and summary chains qualify for trace learning because automatic trace-fed production, retention and later consumption are wired. Curriculum note-specific derivation remains afforded and partial. Verifier raw replay, snapshots and image preservation alone do not establish an additional extracted behavior-shaping learning product; opaque scratch prevents a negative. No bounded absence records justify a trace-learning no or an inapplicable trace-source axis ([RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission), [MEM-RTE-worklog-fold](memory.md#mem-rte-worklog-fold), [MEM-OBJ-curriculum-notes](memory.md#mem-obj-curriculum-notes), [MEM-RTE-verifier-replay](memory.md#mem-rte-verifier-replay)).

Terminal bank and diagnosis production consumes linked Actor decisions/actions/observations and terminal Verifier outcomes as multi-step experience. Its trace sources therefore include trajectories alongside session logs and tool traces; these values can describe overlapping content. No separately serialized trajectory object or additional learning-unit schema is required. This classification follows the accepted terminal-learning route and its memory annotation, not merely the presence of a tool history. It does not resolve note-specific inputs, other recovery variants or provider-side state ([RT-RTE-learning-admission](runtime.md#rt-rte-learning-admission), [EPI-RTE-memory-proposal](epistemic.md#epi-rte-memory-proposal), [MEM-OBJ-learning-diagnosis](memory.md#mem-obj-learning-diagnosis)).

Curation bases remain separate. WORK LOG folding implements consolidation even if model output loses a negation; indeterminate semantic relation does not establish synthesis. Bank criticism/reconciliation is requested, revisions and history-preserving withdrawal are afforded, and no generated corpus establishes completed semantic repair. Structural replay forgets actionless live-context pairs without deleting raw artifacts; attachment identity deduplication is not relevance ranking ([EPI-RTE-worklog-fold](epistemic.md#epi-rte-worklog-fold), [EPI-RTE-memory-proposal](epistemic.md#epi-rte-memory-proposal), [MEM-RTE-verifier-replay](memory.md#mem-rte-verifier-replay), [MEM-OBJ-durable-images](memory.md#mem-obj-durable-images)).

Bank delivery has both push and pull: host supplies the configured tree/inventory; the Actor requests selected file bodies. Filename requests are not identifier-based push, and foreground relevance judgments are not automatic inferred-judgment retrieval. Summary generation's semantic selection occurs at writing; availability of its retained result selects later delivery. Checkpoint hashes validate whole lineage bundles rather than selecting relevant evidence by identity match. These coarse push routes do not establish reliance or successful delivery on all task paths ([RT-RTE-task-execution](runtime.md#rt-rte-task-execution), [RT-RTE-lineage-recovery](runtime.md#rt-rte-lineage-recovery), [WF-RTE-phase-transition](workflow.md#wf-rte-phase-transition)).

Missing initial-bank authorship/approval, generated bank/note/scratch instances, variant recovery bodies and provider internals prevent stronger inventory and value completeness. Static charters do not become authored instruction memory merely because later calls receive them. Official score archives and cohort reporting remain measurement/reporting rather than an evidenced adaptive memory loop here ([MEM-OBJ-memory](memory.md#mem-obj-memory), [MEM-OBJ-verifier-scratch](memory.md#mem-obj-verifier-scratch), [EPI-RTE-score-report](epistemic.md#epi-rte-score-report)).

Source-read log: none. This profile uses only the supplied accepted members and reconciliation; it adds no records, quotes or source evidence.
