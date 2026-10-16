---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: EAL-Bench memory comparison covering retained authorization payloads, lifecycle/recovery
  state, annotations and closed-loop feedback, with unresolved shipped alternatives.
run-id: AAS-2026-10-15-eal-bench-f9a76e2fa858-01
source-identity: https://github.com/tommasocerruti/eal-bench
reviewed-boundary: 51648690bc52d7a9c7ac080a2c67a784fe9d56cb
memory-comparison:
  version: 2
  scope: Retained authorization profiles and frozen payloads; audit/access/checkpoint metadata used by
    later consumers; event logs and reduced state; saved replay, annotation assessment artifacts, controlled
    variants and closed-loop write-back. Includes unresolved pressure/challenge, hybrid, domain maintenance
    and analysis alternatives. Excludes shipped static policy/corpus as memory by itself, ordinary current-invocation
    messages, and external hosted weights/provider internals not established as retained state changed
    through this workflow.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Inspected authorization payloads, event log/current state, attempts, executor checkpoint
          and saved annotation child runs
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-memory-artifact
          - memory.md#mem-obj-memory-attempt
          - memory.md#mem-obj-event-log
          - memory.md#mem-obj-reduced-state
          - runtime.md#rt-obj-executor-plan
          - epistemic.md#epi-obj-annotation-state
          note: Run-directory JSON/JSONL and checkpoint files retain these products.
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-memory-artifact
          - memory.md#mem-obj-memory-attempt
          - memory.md#mem-obj-event-log
          - memory.md#mem-obj-reduced-state
          - runtime.md#rt-obj-executor-plan
          - epistemic.md#epi-obj-evaluation-results
          note: Python objects, reducer lists/mappings and reconstructed execution state hold operative
            retained products during use.
        records:
        - memory.md#mem-obj-memory-artifact
        - memory.md#mem-obj-memory-attempt
        - memory.md#mem-obj-event-log
        - memory.md#mem-obj-reduced-state
        - runtime.md#rt-obj-executor-plan
        - epistemic.md#epi-obj-annotation-state
        - epistemic.md#epi-obj-evaluation-results
        note: These are object storage locations, not JSON encoding or the repository containing program
          source.
      - scope: Generic public annotation persistence and evaluation exports
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-obj-annotation-state
        - epistemic.md#epi-obj-evaluation-results
        - epistemic.md#epi-rte-annotation-admission
        note: The shipped annotation child run is file-backed; persistence selected by arbitrary public
          callers and export retention is unresolved.
      - scope: Included pressure/challenge reuse, hybrid formation, other domain repair/maintenance and
          diagnostic-analysis routes
        assessment: uninspected
        findings: []
        records: &id001
        - runtime.md#rt-rte-writer-admission
        - runtime.md#rt-rte-event-admission
        - memory.md#mem-rte-saved-replay
        - epistemic.md#epi-rte-memory-assessment
        note: Accepted reports retain these included alternatives without complete selector, producer
          or consumer inspection. Their classification cannot be inferred from the ordinary writer or
          Procurement annotation path.
      records:
      - memory.md#mem-obj-memory-artifact
      - memory.md#mem-obj-memory-attempt
      - memory.md#mem-obj-event-log
      - memory.md#mem-obj-reduced-state
      - runtime.md#rt-obj-executor-plan
      - epistemic.md#epi-obj-annotation-state
      - epistemic.md#epi-obj-evaluation-results
      - epistemic.md#epi-rte-annotation-admission
      - runtime.md#rt-rte-writer-admission
      - runtime.md#rt-rte-event-admission
      - memory.md#mem-rte-saved-replay
      - epistemic.md#epi-rte-memory-assessment
      note: File-backed and process-resident witnesses do not enumerate every included alternative. Hosted
        model internals are not asserted to be memory stores accumulated by this workflow.
    representational_form:
      assessment: partial
      units:
      - scope: Free-text memory and typed JSON at model-interpreted writer/executor consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-memory-artifact
          - runtime.md#rt-bap-memory-evidence
          - runtime.md#rt-bap-profile-update
          note: Prose and serialized authorization JSON supply meaning through model interpretation, not
            fixed authorization rules.
        records:
        - memory.md#mem-obj-memory-artifact
        - runtime.md#rt-bap-memory-evidence
        - runtime.md#rt-bap-profile-update
        note: The typed payload has a separate symbolic consumption unit below; serialization alone does
          not settle form.
      - scope: Typed payload at parsers/evaluators, reducer log and snapshot, checkpoint/access metadata,
          audit state and annotation scoring envelope
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-memory-artifact
          - memory.md#mem-obj-reduced-state
          - memory.md#mem-obj-event-log
          - runtime.md#rt-obj-executor-plan
          - memory.md#mem-obj-memory-attempt
          - epistemic.md#epi-obj-annotation-state
          - epistemic.md#epi-rte-memory-assessment
          note: Localized fields have fixed parsing, lifecycle, identity, consistency or scoring consequences.
        records:
        - memory.md#mem-obj-memory-artifact
        - memory.md#mem-obj-reduced-state
        - memory.md#mem-obj-event-log
        - runtime.md#rt-obj-executor-plan
        - memory.md#mem-obj-memory-attempt
        - epistemic.md#epi-obj-annotation-state
        - epistemic.md#epi-rte-memory-assessment
        note: Includes natural-language audit error text separately as interpreted material, not a second
          authorization guard.
      - scope: Audit error/repair text interpreted by writer
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-memory-attempt
          - runtime.md#rt-rte-writer-admission
          note: Diagnostics can enter model-facing structural repair feedback.
        records:
        - memory.md#mem-obj-memory-attempt
        - runtime.md#rt-rte-writer-admission
        note: Only the repair consumer is established; executors do not receive the audit stream.
      - scope: Included pressure/challenge reuse, hybrid formation, other domain repair/maintenance and
          diagnostic-analysis routes
        assessment: uninspected
        findings: []
        records: *id001
        note: Accepted reports retain these included alternatives without complete selector, producer
          or consumer inspection. Their classification cannot be inferred from the ordinary writer or
          Procurement annotation path.
      records:
      - memory.md#mem-obj-memory-artifact
      - runtime.md#rt-bap-memory-evidence
      - runtime.md#rt-bap-profile-update
      - memory.md#mem-obj-reduced-state
      - memory.md#mem-obj-event-log
      - runtime.md#rt-obj-executor-plan
      - memory.md#mem-obj-memory-attempt
      - epistemic.md#epi-obj-annotation-state
      - epistemic.md#epi-rte-memory-assessment
      - runtime.md#rt-rte-writer-admission
      - runtime.md#rt-rte-event-admission
      - memory.md#mem-rte-saved-replay
      note: 'Natural-language and symbolic paths coexist. Hosted inference components are excluded from
        retained-memory form classification: no scoped parameter update is established, and opaque provider
        state is not silently classified.'
    lineage:
      assessment: partial
      units:
      - scope: Writer profiles and closed-loop descendants
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-memory-artifact
          - runtime.md#rt-rte-closed-feedback
          note: Closed-loop descendants are derived from recorded executor actions and benchmark outcomes
            through seeded writer updates.
        records:
        - memory.md#mem-obj-memory-artifact
        - runtime.md#rt-rte-closed-feedback
        note: This finding covers the feedback-derived branch, not the original provenance of every baseline
          history.
      - scope: Event-derived current state and restored trajectories
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-event-log
          - memory.md#mem-obj-reduced-state
          - memory.md#mem-rte-event-recovery
          note: Fixed lifecycle reduction compiles accepted events into current state and replayed computational
            state.
        records:
        - memory.md#mem-obj-event-log
        - memory.md#mem-obj-reduced-state
        - memory.md#mem-rte-event-recovery
        note: Model-extracted events precede deterministic state reduction; origin of all source history
          is not resolved here.
      - scope: Deliberately widened diagnostic memory
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - epistemic.md#epi-rte-variant-construction
          note: Deterministic code intentionally constructs altered permission claims; this is not endogenous
            extraction error.
        records:
        - epistemic.md#epi-rte-variant-construction
        note: Authored does not imply human authorship or manual admission.
      - scope: Saved replay and restored executor evidence
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-rte-saved-replay
          - runtime.md#rt-rte-checkpoint-resume
          note: A later run or continuation loads already retained evidence without regenerating its content.
        records:
        - memory.md#mem-rte-saved-replay
        - runtime.md#rt-rte-checkpoint-resume
        note: Import describes this transfer path, not the initial creation of every payload.
      - scope: Persisted annotation interpretation
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - epistemic.md#epi-obj-annotation-state
          - epistemic.md#epi-rte-annotation-extraction
          note: A model interprets saved prose into a typed assessment artifact.
        records:
        - epistemic.md#epi-obj-annotation-state
        - epistemic.md#epi-rte-annotation-extraction
        note: This is derived interpretation, not replacement authorization memory.
      - scope: Initial baseline profiles, event input histories and generic caller annotations
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-artifact
        - memory.md#mem-obj-event-log
        - epistemic.md#epi-obj-annotation-state
        - runtime.md#rt-rte-writer-admission
        note: Recorded derivation and lineage IDs do not resolve all initial source origins or generic
          caller provenance.
      - scope: Included pressure/challenge reuse, hybrid formation, other domain repair/maintenance and
          diagnostic-analysis routes
        assessment: uninspected
        findings: []
        records: *id001
        note: Accepted reports retain these included alternatives without complete selector, producer
          or consumer inspection. Their classification cannot be inferred from the ordinary writer or
          Procurement annotation path.
      records:
      - memory.md#mem-obj-memory-artifact
      - runtime.md#rt-rte-closed-feedback
      - memory.md#mem-obj-event-log
      - memory.md#mem-obj-reduced-state
      - memory.md#mem-rte-event-recovery
      - epistemic.md#epi-rte-variant-construction
      - memory.md#mem-rte-saved-replay
      - runtime.md#rt-rte-checkpoint-resume
      - epistemic.md#epi-obj-annotation-state
      - epistemic.md#epi-rte-annotation-extraction
      - runtime.md#rt-rte-writer-admission
      - runtime.md#rt-rte-event-admission
      - epistemic.md#epi-rte-memory-assessment
      note: Known derivation paths do not resolve initial provenance. The annotation object is cited under
        its canonical epistemic declaration after supersession.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Memory payload at executor and prior profile at writer
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - runtime.md#rt-bap-memory-evidence
          - runtime.md#rt-bap-profile-update
          note: Selected authorization contents supply interpreted evidence/context at these model consumers.
        records:
        - runtime.md#rt-bap-memory-evidence
        - runtime.md#rt-bap-profile-update
        note: This is not an enforced organizational permission.
      - scope: Recorded executor request/action/outcome at closed-loop update consumer
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - runtime.md#rt-rte-closed-feedback
          note: Retained experience feeds automatic revision of durable context used by later requests.
        records:
        - runtime.md#rt-rte-closed-feedback
        note: Learning authority here does not assert improved capacity or parameter training.
      - scope: Retained candidates at reviewer and oracle-fidelity selector
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - runtime.md#rt-rte-candidate-selection
          note: Candidate contents and their relative fidelity influence selection priority.
        records:
        - runtime.md#rt-rte-candidate-selection
        note: A model reviewer and symbolic gold comparison are distinct selectors; neither proves zero
          error.
      - scope: Saved execution plan and current chain/state identities at continuation consumers
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-obj-executor-plan
          - runtime.md#rt-rte-checkpoint-resume
          - runtime.md#rt-rte-writer-admission
          note: Retained identities select missing jobs, evidence and the current profile for the next
            update.
        - value: validation
          basis: wired
          records:
          - runtime.md#rt-obj-executor-plan
          - runtime.md#rt-rte-checkpoint-resume
          note: Retained hashes and identities define checkpoint compatibility criteria.
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-obj-executor-plan
          - runtime.md#rt-rte-checkpoint-resume
          note: Incompatible artifacts or identities veto continuation.
        records:
        - runtime.md#rt-obj-executor-plan
        - runtime.md#rt-rte-checkpoint-resume
        - runtime.md#rt-rte-writer-admission
        note: Routing and checkpoint veto concern execution/recovery, not authorization truth.
      - scope: Persisted annotation status, hash and extracted-state agreement at scoring resolver
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - epistemic.md#epi-obj-annotation-state
          - epistemic.md#epi-rte-annotation-admission
          note: Retained status/hash/state define eligibility and consistency checks.
        - value: enforcement
          basis: wired
          records:
          - epistemic.md#epi-obj-annotation-state
          - epistemic.md#epi-rte-annotation-admission
          note: Unaccepted, mismatched or conflicting annotations prevent an estimable prose score.
        records:
        - epistemic.md#epi-obj-annotation-state
        - epistemic.md#epi-rte-annotation-admission
        note: The typed extraction supplies assessment content; eligibility is not semantic endorsement.
      - scope: Annotation and typed authorization fields at preservation/formation assessment
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - epistemic.md#epi-obj-annotation-state
          - epistemic.md#epi-rte-memory-assessment
          note: Retained interpreted or typed state supplies the candidate content being assessed.
        records:
        - epistemic.md#epi-obj-annotation-state
        - epistemic.md#epi-rte-memory-assessment
        note: This consumer computes diagnostic results, not a live execution grant.
      - scope: Retained event log at reducer recovery
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-event-log
          - memory.md#mem-rte-event-recovery
          note: Replayed event-derived records determine compatibility of the saved reducer state.
        records:
        - memory.md#mem-obj-event-log
        - memory.md#mem-rte-event-recovery
        note: Log events are symbolic replay inputs; they are not pushed as standing model instructions.
      - scope: Included pressure/challenge reuse, hybrid formation, other domain repair/maintenance and
          diagnostic-analysis routes
        assessment: uninspected
        findings: []
        records: *id001
        note: Accepted reports retain these included alternatives without complete selector, producer
          or consumer inspection. Their classification cannot be inferred from the ordinary writer or
          Procurement annotation path.
      records:
      - runtime.md#rt-bap-memory-evidence
      - runtime.md#rt-bap-profile-update
      - runtime.md#rt-rte-closed-feedback
      - runtime.md#rt-rte-candidate-selection
      - runtime.md#rt-obj-executor-plan
      - runtime.md#rt-rte-checkpoint-resume
      - runtime.md#rt-rte-writer-admission
      - epistemic.md#epi-obj-annotation-state
      - epistemic.md#epi-rte-annotation-admission
      - epistemic.md#epi-rte-memory-assessment
      - memory.md#mem-obj-event-log
      - memory.md#mem-rte-event-recovery
      - runtime.md#rt-rte-event-admission
      - memory.md#mem-rte-saved-replay
      note: Authority is consumer-specific. Static policy/corpus criteria are outside the accumulated-memory
        inventory, so their enforcing use is not automatically attributed to remembered grants.
    write_agency:
      assessment: partial
      units:
      - scope: LangMem content admission including repair/fallback and seeded feedback
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-writer-admission
          - runtime.md#rt-rte-closed-feedback
          note: Model proposal and software validation decide contents; workflow launch is not per-content
            approval.
        records:
        - runtime.md#rt-rte-writer-admission
        - runtime.md#rt-rte-closed-feedback
        note: Workflow annotations retain empty fallback on terminal failure without prior state.
      - scope: Event delta admission, gate transformation and whole-candidate selection
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-event-admission
          - runtime.md#rt-rte-authority-gate
          - runtime.md#rt-rte-candidate-selection
          note: Software/model mechanisms admit events, filter records or choose complete candidates without
            per-content operator approval.
        records:
        - runtime.md#rt-rte-event-admission
        - runtime.md#rt-rte-authority-gate
        - runtime.md#rt-rte-candidate-selection
        note: Separate mechanisms share this agency value, not a universal validation policy.
      - scope: Procurement annotation extraction/admission and controlled widened-memory production
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - epistemic.md#epi-rte-annotation-extraction
          - epistemic.md#epi-rte-annotation-admission
          - epistemic.md#epi-rte-variant-construction
          note: Models/software supply and admit these artifacts; optional human-validation sample output
            is not completed approval.
        records:
        - epistemic.md#epi-rte-annotation-extraction
        - epistemic.md#epi-rte-annotation-admission
        - epistemic.md#epi-rte-variant-construction
        note: Physical JSONL I/O is not the reason for this classification.
      - scope: Generic public annotations and caller-provided initial content
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-obj-annotation-state
        - epistemic.md#epi-rte-annotation-admission
        - memory.md#mem-obj-memory-artifact
        note: Caller identity alone does not establish human versus computational content admission.
      - scope: Included pressure/challenge reuse, hybrid formation, other domain repair/maintenance and
          diagnostic-analysis routes
        assessment: uninspected
        findings: []
        records: *id001
        note: Accepted reports retain these included alternatives without complete selector, producer
          or consumer inspection. Their classification cannot be inferred from the ordinary writer or
          Procurement annotation path.
      records:
      - runtime.md#rt-rte-writer-admission
      - runtime.md#rt-rte-closed-feedback
      - runtime.md#rt-rte-event-admission
      - runtime.md#rt-rte-authority-gate
      - runtime.md#rt-rte-candidate-selection
      - epistemic.md#epi-rte-annotation-extraction
      - epistemic.md#epi-rte-annotation-admission
      - epistemic.md#epi-rte-variant-construction
      - epistemic.md#epi-obj-annotation-state
      - memory.md#mem-obj-memory-artifact
      - memory.md#mem-rte-saved-replay
      - epistemic.md#epi-rte-memory-assessment
      note: Inspected mechanisms establish automatic admission; manual admission cannot be inferred for
        unresolved public or maintenance paths.
    curation_operations:
      assessment: partial
      units:
      - scope: Compact profile production and seeded model-mediated replacement
        assessment: known
        findings:
        - value: consolidate
          basis: afforded
          records:
          - runtime.md#rt-rte-writer-admission
          - memory.md#mem-obj-memory-artifact
          note: The wrapper affords compression of source history into current-state memory; semantic
            faithfulness of a particular output is not observed.
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-rte-writer-admission
          - runtime.md#rt-rte-closed-feedback
          note: Accepted changed content replaces the existing profile; failed updates preserve the seed
            when present.
        records:
        - runtime.md#rt-rte-writer-admission
        - memory.md#mem-obj-memory-artifact
        - runtime.md#rt-rte-closed-feedback
        note: Consolidation describes the requested compression capacity, while replacement is a wired
          admission effect.
      - scope: Deterministic lifecycle reduction of retained events
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-obj-event-log
          - memory.md#mem-obj-reduced-state
          - runtime.md#rt-rte-event-admission
          note: Cumulative lifecycle history is reduced to compact current state.
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-rte-event-admission
          - memory.md#mem-obj-reduced-state
          note: Patch and replacement events revise existing authorization entries.
        - value: invalidate
          basis: wired
          records:
          - runtime.md#rt-rte-event-admission
          - memory.md#mem-obj-event-log
          - memory.md#mem-obj-reduced-state
          note: Revocation withdraws current reliance while lifecycle history remains retained.
        records:
        - memory.md#mem-obj-event-log
        - memory.md#mem-obj-reduced-state
        - runtime.md#rt-rte-event-admission
        note: The reducer transformation is inspected even though extraction accuracy and live operation
          are not.
      - scope: Cited-source filtering with original and child arms retained
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records:
          - runtime.md#rt-rte-authority-gate
          note: Failed records are removed from the derived current authorization arm while original memory
            remains available.
        records:
        - runtime.md#rt-rte-authority-gate
        note: Bounded withdrawal is not destruction of every saved copy.
      - scope: Deliberate diagnostic widening of existing permission
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - epistemic.md#epi-rte-variant-construction
          note: Code changes existing authorization scope in a separate diagnostic arm.
        - value: synthesize
          basis: wired
          records:
          - epistemic.md#epi-rte-variant-construction
          note: Widening introduces permission not entailed by the restricted input, as the record demonstrates.
        records:
        - epistemic.md#epi-rte-variant-construction
        note: The new claim is intentionally untrusted intervention content, not accepted knowledge or
          faithful consolidation.
      - scope: Semantic transformation of model annotation extraction
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-rte-annotation-extraction
        - epistemic.md#epi-obj-annotation-state
        note: Typed interpretation is established, but semantic preservation versus changed meaning requires
          an output/source comparison; no additional controlled operation is established.
      - scope: Included pressure/challenge reuse, hybrid formation, other domain repair/maintenance and
          diagnostic-analysis routes
        assessment: uninspected
        findings: []
        records: *id001
        note: Accepted reports retain these included alternatives without complete selector, producer
          or consumer inspection. Their classification cannot be inferred from the ordinary writer or
          Procurement annotation path.
      records:
      - runtime.md#rt-rte-writer-admission
      - memory.md#mem-obj-memory-artifact
      - runtime.md#rt-rte-closed-feedback
      - memory.md#mem-obj-event-log
      - memory.md#mem-obj-reduced-state
      - runtime.md#rt-rte-event-admission
      - runtime.md#rt-rte-authority-gate
      - epistemic.md#epi-rte-variant-construction
      - epistemic.md#epi-rte-annotation-extraction
      - epistemic.md#epi-obj-annotation-state
      - memory.md#mem-rte-saved-replay
      - epistemic.md#epi-rte-memory-assessment
      note: Curation findings remain local. Selection alone does not establish promotion, and capacity
        checks/index or checkpoint operations do not establish decay or deduplication.
    read_back_direction:
      assessment: partial
      units:
      - scope: Requested saved replay, shared checkpoint continuation and event restoration
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-saved-replay
          - runtime.md#rt-rte-checkpoint-resume
          - memory.md#mem-rte-event-recovery
          note: A host request loads selected completed evidence, missing-job state or historical events
            for the named consumer.
        records:
        - memory.md#mem-rte-saved-replay
        - runtime.md#rt-rte-checkpoint-resume
        - memory.md#mem-rte-event-recovery
        note: Delivery fulfilling these requests is not separately counted as unsolicited push.
      - scope: Host-built writer/executor/reviewer context and source-authority paired jobs
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - runtime.md#rt-rte-writer-admission
          - runtime.md#rt-bap-memory-evidence
          - runtime.md#rt-rte-candidate-selection
          - runtime.md#rt-rte-authority-gate
          - runtime.md#rt-rte-event-admission
          note: Code automatically supplies current profile, selected frozen payload, candidate pool or
            previous compact state without a foreground model retrieval request.
        records:
        - runtime.md#rt-rte-writer-admission
        - runtime.md#rt-bap-memory-evidence
        - runtime.md#rt-rte-candidate-selection
        - runtime.md#rt-rte-authority-gate
        - runtime.md#rt-rte-event-admission
        note: An upstream operator study choice can feed selection; current raw request/history alone
          is not retained memory.
      - scope: Accepted annotation loaded for later requested assessment
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - epistemic.md#epi-obj-annotation-state
          - epistemic.md#epi-rte-annotation-admission
          - epistemic.md#epi-rte-memory-assessment
          note: The scoring request supplies annotations and resolver selects an eligible interpretation.
        records:
        - epistemic.md#epi-obj-annotation-state
        - epistemic.md#epi-rte-annotation-admission
        - epistemic.md#epi-rte-memory-assessment
        note: This classifies the established assessment chain, not arbitrary external storage behavior.
      - scope: Included pressure/challenge reuse, hybrid formation, other domain repair/maintenance and
          diagnostic-analysis routes
        assessment: uninspected
        findings: []
        records: *id001
        note: Accepted reports retain these included alternatives without complete selector, producer
          or consumer inspection. Their classification cannot be inferred from the ordinary writer or
          Procurement annotation path.
      records:
      - memory.md#mem-rte-saved-replay
      - runtime.md#rt-rte-checkpoint-resume
      - memory.md#mem-rte-event-recovery
      - runtime.md#rt-rte-writer-admission
      - runtime.md#rt-bap-memory-evidence
      - runtime.md#rt-rte-candidate-selection
      - runtime.md#rt-rte-authority-gate
      - runtime.md#rt-rte-event-admission
      - epistemic.md#epi-obj-annotation-state
      - epistemic.md#epi-rte-annotation-admission
      - epistemic.md#epi-rte-memory-assessment
      note: Both requested reuse and automatic model-context supply exist. Their coexistence does not
        resolve other shipped study selectors.
    read_back_signal:
      assessment: partial
      units:
      - scope: Current-chain profile and case/job evidence pushes
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-rte-writer-admission
          - runtime.md#rt-bap-memory-evidence
          - runtime.md#rt-rte-candidate-selection
          - runtime.md#rt-rte-authority-gate
          - runtime.md#rt-rte-event-admission
          note: Update chain/current-memory association, case/job evidence association and candidate-pool
            keys select retained parts for delivery.
        records:
        - runtime.md#rt-rte-writer-admission
        - runtime.md#rt-bap-memory-evidence
        - runtime.md#rt-rte-candidate-selection
        - runtime.md#rt-rte-authority-gate
        - runtime.md#rt-rte-event-admission
        note: Trigger is the scheduled update, executor job or review; selection inputs are chain/case/evidence
          or pool identities, selected products are current payload/state or the matching candidate pool.
          IDs here select delivery, not merely label files.
      - scope: Best-of-k choice feeding selected payload to executor
        assessment: known
        findings:
        - value: inferred-judgment
          basis: wired
          records:
          - runtime.md#rt-rte-candidate-selection
          note: Live reviewer judges source history and candidate contents and its parsed label determines
            the whole delivered candidate.
        records:
        - runtime.md#rt-rte-candidate-selection
        note: Trigger is review-mode preparation; the selected part is one retained candidate. Oracle-only
          comparison is a distinct symbolic selector, not this finding.
      - scope: Oracle-only fidelity selection and all alternate context targeting
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-candidate-selection
        - runtime.md#rt-rte-event-admission
        - memory.md#mem-rte-saved-replay
        note: Gold field-error comparison is inspected but no more specific controlled signal follows
          without conflating it with lexical or model judgment. Event/replay scheduling outside inspected
          selectors and pressure/challenge alternatives remain unresolved.
      - scope: Included pressure/challenge reuse, hybrid formation, other domain repair/maintenance and
          diagnostic-analysis routes
        assessment: uninspected
        findings: []
        records: *id001
        note: Accepted reports retain these included alternatives without complete selector, producer
          or consumer inspection. Their classification cannot be inferred from the ordinary writer or
          Procurement annotation path.
      records:
      - runtime.md#rt-rte-writer-admission
      - runtime.md#rt-bap-memory-evidence
      - runtime.md#rt-rte-candidate-selection
      - runtime.md#rt-rte-authority-gate
      - runtime.md#rt-rte-event-admission
      - memory.md#mem-rte-saved-replay
      - epistemic.md#epi-rte-memory-assessment
      note: Identifier and judgment witnesses cover actual automatic selection, not every operation in
        their surrounding chains. Requested file loads do not independently establish identifier push.
    trace_learning:
      assessment: partial
      units:
      - scope: Closed-loop action/outcome write-back to subsequent request memory
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-closed-feedback
          - memory.md#mem-obj-memory-artifact
          - runtime.md#rt-bap-memory-evidence
          note: Scored executor experience automatically feeds a retained seeded profile revision, and
            accepted output supplies context for later requests.
        records:
        - runtime.md#rt-rte-closed-feedback
        - memory.md#mem-obj-memory-artifact
        - runtime.md#rt-bap-memory-evidence
        note: The route meets the trace-fed artifact definition without requiring new knowledge, improved
          capacity or weight updates. Neutral and rejected-update branches do not erase this positive
          route.
      - scope: Baseline history compression, event extraction and annotation derivation
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-writer-admission
        - runtime.md#rt-rte-event-admission
        - epistemic.md#epi-rte-annotation-extraction
        - memory.md#mem-obj-memory-artifact
        - memory.md#mem-obj-event-log
        note: Durable products and later consumers are established, but records do not fully classify
          original histories as recorded activity rather than static benchmark content. Annotation input
          is derived prose, not itself established as an original trace.
      - scope: Included pressure/challenge reuse, hybrid formation, other domain repair/maintenance and
          diagnostic-analysis routes
        assessment: uninspected
        findings: []
        records: *id001
        note: Accepted reports retain these included alternatives without complete selector, producer
          or consumer inspection. Their classification cannot be inferred from the ordinary writer or
          Procurement annotation path.
      records:
      - runtime.md#rt-rte-closed-feedback
      - memory.md#mem-obj-memory-artifact
      - runtime.md#rt-bap-memory-evidence
      - runtime.md#rt-rte-writer-admission
      - runtime.md#rt-rte-event-admission
      - epistemic.md#epi-rte-annotation-extraction
      - memory.md#mem-obj-event-log
      - memory.md#mem-rte-saved-replay
      - epistemic.md#epi-rte-memory-assessment
      note: One qualifying feedback route supports yes; other included writes remain unresolved. No system-wide
        no is asserted and raw log retention alone is not counted.
    trace_source:
      assessment: partial
      units:
      - scope: Executor request/action/payload/result content consumed in closed-loop write-back
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records:
          - runtime.md#rt-rte-closed-feedback
          note: Recorded native-tool decision/payload and execution-scoring feedback feed the rendered
            outcome update.
        records:
        - runtime.md#rt-rte-closed-feedback
        note: The source is benchmark tool-decision feedback, not an external transaction and not event-streams
          merely because the adapter creates a timestamped conversation turn.
      - scope: Other content in closed-loop updates and initial memories
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-closed-feedback
        - memory.md#mem-obj-memory-artifact
        - runtime.md#rt-rte-writer-admission
        note: Current requests and source histories may accompany the tool feedback; original recorded-session
          or multi-step trajectory provenance is not fully established. Synthetic conversation labels
          alone establish neither session-logs nor event-streams.
      - scope: Other potentially qualifying baseline/event/maintenance writes
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-writer-admission
        - runtime.md#rt-rte-event-admission
        - epistemic.md#epi-rte-annotation-extraction
        - memory.md#mem-rte-saved-replay
        note: Trace-learning coverage for these included routes remains unresolved, so their sources are
          not inapplicable merely because one known feedback source exists.
      records:
      - runtime.md#rt-rte-closed-feedback
      - memory.md#mem-obj-memory-artifact
      - runtime.md#rt-rte-writer-admission
      - runtime.md#rt-rte-event-admission
      - epistemic.md#epi-rte-annotation-extraction
      - memory.md#mem-rte-saved-replay
      note: The known tool-feedback source is retained with its local warrant; mixed original-input provenance
        prevents a complete trace-source inventory.
---

# EAL-Bench memory profile

## Comparison rationale

All axes are partial because the accepted reports preserve material included alternatives whose write, selection or consumer paths were not exhaustively traced. Positive findings concern their named parts, not an exhaustive system value list. Missing primary execution archives prevent observed and causal classifications; they do not erase inspected wiring.

[MEM-OBJ-memory-artifact](memory.md#mem-obj-memory-artifact) is a valid container, not superseded by its typed and prose parts. The event snapshot and cumulative log remain separate consumer units. The sole object supersession affecting this profile replaces the public annotation object with [EPI-OBJ-annotation-state](epistemic.md#epi-obj-annotation-state). That record adds concrete file-backed Procurement production, while generic public caller control and persistence remain unresolved; the replacement does not resolve those alternatives.

Form follows consumption. JSON state is symbolic at parsers/reducers and interpreted content at models. No parametric finding is imported from the hosted inference components into the accumulated-memory boundary. Static domain criteria are not classified as retained memory merely because they validate generated material.

The feedback finding uses the profile's write-route definition of trace learning, not the separate improved-capacity meaning. [RT-RTE-closed-feedback](runtime.md#rt-rte-closed-feedback) and its memory annotation establish an automatic recorded-action/outcome → seeded update → retained payload → later request chain. The adapter's synthetic actor and timestamp do not establish original session or environmental-event provenance. Tool-decision feedback supplies the positive source; other mixed inputs remain unresolved.

Consolidation, replacement, withdrawal and diagnostic widening have different warrants. The writer affords compression but does not prove faithful output; deterministic reduction and admission provide wired transformations. [EPI-RTE-variant-construction](epistemic.md#epi-rte-variant-construction) explicitly establishes a new non-entailing permission in controlled widening, so synthesis is retained only for that intentionally untrusted branch. Merely erroneous extraction is not relabelled synthesis.

Pull describes requested saved-state reuse; push describes automatic delivery into later model contexts. Identifier findings name an actual chain/case/pool association selecting delivered retained parts, not a filename or an ID printed in a catalog. Whole-candidate model judgment is distinct from symbolic gold-fidelity comparison. Neither is collapsed into a universal retrieval policy.

No new records, quotations or source evidence were added. No target-source reads were performed for this classification; all warrants are the canonical accepted records and their annotations. The supplied reconciliation was used only to resolve identities and compatible coverage limits.
