---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Claude Workstream Kit memory profile: Git-backed work records, model-mediated capture and
  curation, selective reload and requested historical retrieval.'
run-id: AAS-2026-10-15-claude-workstream-kit-103204afa1ab-01
source-identity: https://github.com/ChristopherA/claude-workstream-kit
reviewed-boundary: 15705c38a4fffb206b868b3e6bc5ffb4fd8b9d64
memory-comparison:
  version: 2
  scope: 'Included: accumulated ACTIVE/workstream parts, optional research notes, consumer-edited PROJECT
    selectors, handoff inbox, archive ledger and tagged snapshots, adopted standing-guidance edits, retained
    telemetry and evaluator session output, and their kit write/maintenance/later-consumer routes. Excluded:
    unchanged shipped instructions and empty seeds as such, arbitrary consumer product storage, external
    native Tasks/plan/account memory, host compaction checkpoints, model weights, and transient subagent
    packets or measurement stdout not adopted into retained files.'
  axes:
    storage_substrate:
      assessment: known
      units:
      - scope: Live pointer and workstream parts; optional notes, PROJECT selector, inbox and archive
          ledger
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-obj-active-selector
          - memory.md#mem-obj-active-prose
          - memory.md#mem-obj-workstream-index
          - memory.md#mem-obj-workstream-content
          - memory.md#mem-obj-notes
          - memory.md#mem-obj-project
          - memory.md#mem-obj-handoffs
          - memory.md#mem-obj-archive
          note: These retained objects are local Markdown files.
        records: *id001
        note: The recorded inventory separates side files from live containers; wiring establishes file-oriented
          persistence, not compliance with every requested write.
      - scope: Committed state, handoff arrivals and historical tag snapshots
        assessment: known
        findings:
        - value: repo
          basis: claimed
          records: &id002
          - runtime.md#rt-rte-state-lifecycle
          - memory.md#mem-obj-archive
          - memory.md#mem-obj-handoffs
          note: Git commits and tags provide the prescribed historical retention route.
        records: *id002
        note: Repository retention depends on the instructed commits and tag discipline; a tag existence
          check does not establish snapshot fidelity.
      - scope: Session context telemetry and evaluator raw output
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id003
          - memory.md#mem-obj-context
          - runtime.md#rt-rte-acceptance-driver
          note: Telemetry JSON and saved session text are filesystem records.
        records: *id003
        note: Temporary storage is included because later capture or maintainer invocations can consume
          it; eventual cleanup is external.
      records:
      - memory.md#mem-obj-active-selector
      - memory.md#mem-obj-active-prose
      - memory.md#mem-obj-workstream-index
      - memory.md#mem-obj-workstream-content
      - memory.md#mem-obj-notes
      - memory.md#mem-obj-project
      - memory.md#mem-obj-handoffs
      - memory.md#mem-obj-archive
      - runtime.md#rt-rte-state-lifecycle
      - memory.md#mem-obj-context
      - runtime.md#rt-rte-acceptance-driver
      note: The scoped retained inventory is file-based, with prescribed Git retention. External provider/native
        checkpoints and arbitrary product storage are excluded, not classified as absent.
    representational_form:
      assessment: known
      units:
      - scope: Resume prose, workstream reasoning/plans, optional notes, handoff substance and ledger
          outcomes
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records: &id004
          - memory.md#mem-obj-active-prose
          - memory.md#mem-obj-workstream-content
          - memory.md#mem-obj-notes
          - memory.md#mem-obj-handoffs
          - memory.md#mem-obj-archive
          note: Later models or maintainers interpret these statements, reasons and directions.
        records: *id004
        note: This is the interpreted content path, distinct from parser consumption of the same files.
      - scope: ACTIVE selectors, workstream index and telemetry at executable parser/selector consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id005
          - memory.md#mem-obj-active-selector
          - memory.md#mem-obj-workstream-index
          - memory.md#mem-obj-context
          note: Executable field, marker and numerical rules consume these retained parts.
        records: *id005
        note: This wired finding covers the inspected parser paths only. Numerical telemetry is localized
          symbolic state, not model parameters.
      - scope: PROJECT paths, handoff metadata and archive locators on prescribed status/work/receiver
          and historical-retrieval paths
        assessment: known
        findings:
        - value: symbolic
          basis: claimed
          records: &symbolic_prescribed
          - memory.md#mem-obj-project
          - memory.md#mem-obj-handoffs
          - memory.md#mem-obj-archive
          note: The skills prescribe using named context paths, structured handoff fields and tag locators;
            these localized selectors and metadata are distinct from interpreted prose content.
        records: *symbolic_prescribed
        note: The records establish symbolic parts and prescribed consumption, not executable parsing of
          every field. Hook inbox count/age signals do not wire detailed source/class/about consumption.
      - scope: Adopted standing guidance and evaluator text read by a maintainer
        assessment: known
        findings:
        - value: natural-language
          basis: afforded
          records: &id006
          - memory.md#mem-bap-artifact-adoption
          - epistemic.md#epi-rte-disposition-check
          - runtime.md#rt-rte-acceptance-driver
          note: The included adoption branch is retained guidance; saved session output is interpreted
            text.
        records: *id006
        note: Executable product edits and external model weights are outside this representational inventory.
      records:
      - memory.md#mem-obj-active-prose
      - memory.md#mem-obj-workstream-content
      - memory.md#mem-obj-notes
      - memory.md#mem-obj-handoffs
      - memory.md#mem-obj-archive
      - memory.md#mem-obj-active-selector
      - memory.md#mem-obj-workstream-index
      - memory.md#mem-obj-project
      - memory.md#mem-obj-context
      - memory.md#mem-bap-artifact-adoption
      - epistemic.md#epi-rte-disposition-check
      - runtime.md#rt-rte-acceptance-driver
      note: Mixed files are split by operative consumption path. PROJECT contributes symbolic selectors;
        static listed files are not automatically accumulated memory.
    lineage:
      assessment: partial
      units:
      - scope: Interviewed creation wording and explicitly edited retained plans
        assessment: known
        findings:
        - value: authored
          basis: claimed
          records: &id007
          - runtime.md#rt-rte-state-lifecycle
          - memory.md#mem-obj-workstream-index
          - memory.md#mem-obj-workstream-content
          note: Creation drafts are composed from interviewed intent and approved wording.
        records: *id007
        note: Authored content is distinct from later trace-fed checkpoint derivation.
      - scope: Routine session checkpoint, Decision/Learning and resume derivation
        assessment: known
        findings:
        - value: trace-extracted
          basis: claimed
          records: &id008
          - runtime.md#rt-rte-state-lifecycle
          - epistemic.md#epi-rte-capture-synthesis
          - memory.md#mem-obj-active-selector
          - memory.md#mem-obj-active-prose
          - memory.md#mem-obj-workstream-index
          - memory.md#mem-obj-workstream-content
          note: Capture derives durable state from session conversation and work findings.
        records: *id008
        note: Synthesis instructions do not establish the semantic novelty or truth of an actual output.
      - scope: Receiver inbox claims and adopted incoming backlog content
        assessment: known
        findings:
        - value: imported
          basis: claimed
          records: &id009
          - memory.md#mem-obj-handoffs
          - runtime.md#rt-rte-state-lifecycle
          note: Claims cross from a sender into the receiving project with provenance and separate verification.
        records: *id009
        note: Imported origin does not confer source warrant or prove receiver acceptance.
      - scope: Condensed/rotated state and derived telemetry
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id010
          - runtime.md#rt-rte-rewrite-state
          - memory.md#mem-rte-learning-condense
          - memory.md#mem-rte-state-rotate
          - memory.md#mem-obj-context
          note: Deterministic text selection and numerical derivation produce these retained parts.
        records: *id010
        note: The inspected code establishes these derivation mechanisms, not observed downstream use.
      - scope: Historical tagged snapshots
        assessment: known
        findings:
        - value: other-compiled
          basis: claimed
          records: &id011
          - memory.md#mem-obj-archive
          - runtime.md#rt-rte-state-lifecycle
          note: The closure protocol snapshots retained records into historical Git state.
        records: *id011
        note: Snapshot creation depends on compliance with the lifecycle instructions.
      - scope: Initial optional research notes and consumer-specific PROJECT list contents
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-obj-project
        note: Records leave actual initial authorship/list provenance unavailable. The imported empty
          seed does not establish provenance of accumulated consumer choices.
      records:
      - runtime.md#rt-rte-state-lifecycle
      - memory.md#mem-obj-workstream-index
      - memory.md#mem-obj-workstream-content
      - epistemic.md#epi-rte-capture-synthesis
      - memory.md#mem-obj-active-selector
      - memory.md#mem-obj-active-prose
      - memory.md#mem-obj-handoffs
      - runtime.md#rt-rte-rewrite-state
      - memory.md#mem-rte-learning-condense
      - memory.md#mem-rte-state-rotate
      - memory.md#mem-obj-context
      - memory.md#mem-obj-archive
      - memory.md#mem-obj-notes
      - memory.md#mem-obj-project
      note: Positive derivation paths do not settle initial notes or project-list provenance. Raw evaluator
        logs are trace retention, not independently extracted semantic memory.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Retained claims, notes, inbox substance and historical outcomes at later model readers
        assessment: known
        findings:
        - value: knowledge
          basis: claimed
          records: &id012
          - memory.md#mem-obj-workstream-content
          - memory.md#mem-obj-notes
          - memory.md#mem-obj-handoffs
          - memory.md#mem-obj-archive
          note: Content supplies context or evidence for later work, extraction or intake.
        records: *id012
        note: Reading claims does not semantically accept them.
      - scope: Evaluator logs at the later maintainer reader
        assessment: known
        findings:
        - value: knowledge
          basis: afforded
          records: &id013
          - runtime.md#rt-rte-acceptance-driver
          note: Retained session output supplies evidence for investigation.
        records: *id013
        note: The inspection opportunity does not establish actual investigation or automatic upstream
          updating.
      - scope: Resume directions, retained plans and closure criteria at the foreground model
        assessment: known
        findings:
        - value: instruction
          basis: claimed
          records: &id014
          - memory.md#mem-obj-active-prose
          - epistemic.md#epi-obj-workstream-guidance
          - runtime.md#rt-rte-state-lifecycle
          note: Now/Next, plans and standing constraints direct subsequent work.
        - value: validation
          basis: claimed
          records: *id014
          note: Retained deletion criteria are compared with evidence before closure approval.
        records: *id014
        note: Criteria are model/user-consumed admissibility conditions, not a filesystem-enforced gate.
      - scope: Retained pointer and status/marker state at deterministic selectors
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id015
          - memory.md#mem-obj-active-selector
          - memory.md#mem-obj-workstream-index
          - runtime.md#rt-rte-session-reload
          - runtime.md#rt-rte-rewrite-state
          - memory.md#mem-rte-learning-condense
          - memory.md#mem-rte-state-rotate
          note: Pointers select active detail and markers select rewrite inputs.
        records: *id015
        note: Wiring supports fixed parser/selector consequences, not model obedience.
      - scope: PROJECT list and telemetry at model/user selection consumers
        assessment: known
        findings:
        - value: routing
          basis: claimed
          records: &id016
          - memory.md#mem-obj-project
          - memory.md#mem-obj-context
          note: The list selects requested project framing; telemetry informs the compact/clear decision.
        records: *id016
        note: The scripts wire list/number availability, but their model/user-directed selection effects
          remain prescribed and unobserved.
      - scope: Retained open/gate structure and references at rewrite admission checks
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id017
          - runtime.md#rt-rte-rewrite-state
          - memory.md#mem-rte-learning-condense
          - memory.md#mem-rte-state-rotate
          note: Existing structure and references define candidate-preservation checks.
        - value: enforcement
          basis: wired
          records: *id017
          note: The script refuses its own replacement when those checks fail.
        records: *id017
        note: This force is bounded to the CLI write path. It does not extend to manual edits or certify
          semantic preservation.
      - scope: Session findings and retained experience at capture/extraction update consumers
        assessment: known
        findings:
        - value: learning
          basis: claimed
          records: &id018
          - runtime.md#rt-rte-state-lifecycle
          - epistemic.md#epi-rte-capture-synthesis
          - memory.md#mem-bap-artifact-adoption
          - epistemic.md#epi-rte-disposition-check
          note: Experience feeds requested durable Decisions/Learnings or governed guidance revisions.
        records: *id018
        note: Learning authority at the update consumer is separate from downstream instruction/knowledge
          and from demonstrated improvement.
      - scope: Governed standing-guidance edit at later instruction readers
        assessment: known
        findings:
        - value: instruction
          basis: afforded
          records: &id019
          - memory.md#mem-bap-artifact-adoption
          - epistemic.md#epi-rte-disposition-check
          - runtime.md#rt-bap-skill-guidance
          note: An adopted guidance edit supplies directions through the governed file rather than its
            APPLIED marker.
        records: *id019
        note: Only the standing-guidance branch is included; arbitrary product effects are not generalized
          to instruction authority.
      - scope: Other destination-specific effects of retained adopted guidance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-bap-artifact-adoption
        - epistemic.md#epi-rte-disposition-check
        note: No deployed destination consumer establishes additional forces. The records explicitly require
          destination authority to be established there; no ranking finding follows from a task order
          or marker count alone.
      records:
      - memory.md#mem-obj-workstream-content
      - memory.md#mem-obj-notes
      - memory.md#mem-obj-handoffs
      - memory.md#mem-obj-archive
      - runtime.md#rt-rte-acceptance-driver
      - memory.md#mem-obj-active-prose
      - epistemic.md#epi-obj-workstream-guidance
      - runtime.md#rt-rte-state-lifecycle
      - memory.md#mem-obj-active-selector
      - memory.md#mem-obj-workstream-index
      - runtime.md#rt-rte-session-reload
      - runtime.md#rt-rte-rewrite-state
      - memory.md#mem-rte-learning-condense
      - memory.md#mem-rte-state-rotate
      - memory.md#mem-obj-project
      - memory.md#mem-obj-context
      - epistemic.md#epi-rte-capture-synthesis
      - memory.md#mem-bap-artifact-adoption
      - epistemic.md#epi-rte-disposition-check
      - runtime.md#rt-bap-skill-guidance
      note: Authority follows each retained part to its actual consumer. Positive local forces coexist
        with unresolved destination effects; no universal enforcement or ranking is asserted.
    write_agency:
      assessment: partial
      units:
      - scope: Exact creation wording, substantive restructuring, closure approval and confirmed handoff
          filing
        assessment: known
        findings:
        - value: manual
          basis: claimed
          records: &id020
          - runtime.md#rt-rte-state-lifecycle
          - memory.md#mem-obj-handoffs
          note: A human explicitly approves the retained wording/change, closure or destination/visibility.
        records: *id020
        note: These decisions are specific content/admission gates, unlike merely starting work.
      - scope: Routine capture, checkpoint updates and mechanical review repairs
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records: &id021
          - runtime.md#rt-rte-state-lifecycle
          - epistemic.md#epi-rte-capture-synthesis
          note: Model admission proceeds without per-item human approval.
        records: *id021
        note: Human initiation does not change subsequent model admission to manual.
      - scope: Numerical telemetry replacement and evaluator log retention
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id022
          - memory.md#mem-obj-context
          - runtime.md#rt-rte-acceptance-driver
          note: Callback/script code writes records without a per-content human decision.
        records: *id022
        note: Starting the driver or host session is not approval of each retained result.
      - scope: Direct rewrite admission under --write
        assessment: not-determinable
        findings: []
        records: *id017
        note: The generic caller and write flag authorize physical replacement but do not establish whether
          a human approved that content. Deterministic transformation alone does not resolve admission
          agency.
      - scope: Initial notes and accumulated PROJECT content admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-obj-project
        note: User editing is available and draft confirmation is requested, but actual initial admission
          control in consumer projects is unavailable.
      records:
      - runtime.md#rt-rte-state-lifecycle
      - memory.md#mem-obj-handoffs
      - epistemic.md#epi-rte-capture-synthesis
      - memory.md#mem-obj-context
      - runtime.md#rt-rte-acceptance-driver
      - runtime.md#rt-rte-rewrite-state
      - memory.md#mem-rte-learning-condense
      - memory.md#mem-rte-state-rotate
      - memory.md#mem-obj-notes
      - memory.md#mem-obj-project
      note: The explicit human and model gates are retained separately from CLI caller ambiguity and unavailable
        initialization.
    curation_operations:
      assessment: partial
      units:
      - scope: Records/Decisions/Learnings condensation and live rotation
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: *id017
          note: Code retains selected existing text in a reduced live representation.
        - value: decay
          basis: wired
          records: *id017
          note: Rotation removes spent blocks from the default live reading surface while history may
            remain.
        records: *id017
        note: These are text transformations, not semantic preservation guarantees. Rotation is distinct
          from condensation and protects a different set of structures.
      - scope: Review supersession and existing-entry revision
        assessment: known
        findings:
        - value: invalidate
          basis: claimed
          records: &id023
          - runtime.md#rt-rte-state-lifecycle
          - epistemic.md#epi-rte-still-true
          - epistemic.md#epi-rte-capture-synthesis
          note: Stale Decisions are marked in place to withdraw current reliance.
        - value: evolve
          basis: claimed
          records: *id023
          note: Review and capture revise, extend or supersede existing retained entries.
        records: *id023
        note: Requested operations do not establish execution or correct diagnosis.
      - scope: Resolved standing constraints and note extraction
        assessment: known
        findings:
        - value: promote
          basis: claimed
          records: &id024
          - memory.md#mem-obj-workstream-content
          - memory.md#mem-obj-notes
          - runtime.md#rt-rte-state-lifecycle
          note: Resolved standing constraints move into Decisions, which are read before work.
        - value: consolidate
          basis: claimed
          records: *id024
          note: Notes sections can be summarized into workstream memory.
        records: *id024
        note: Promotion raises the presentation/consumption tier; note summaries reduce existing research
          content.
      - scope: Capture synthesis semantics and incompletely inspected records-condensation shapes
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-rte-capture-synthesis
        - runtime.md#rt-rte-rewrite-state
        note: No actual synthesis input/output establishes a new claim absent from inputs. Exact completion-note
          handling was not fully established. Do not infer synthesize or dedup from a route name or a
          duplicate check.
      records:
      - runtime.md#rt-rte-rewrite-state
      - memory.md#mem-rte-learning-condense
      - memory.md#mem-rte-state-rotate
      - runtime.md#rt-rte-state-lifecycle
      - epistemic.md#epi-rte-still-true
      - epistemic.md#epi-rte-capture-synthesis
      - memory.md#mem-obj-workstream-content
      - memory.md#mem-obj-notes
      note: Implemented and prescribed operations keep separate bases. Semantic indeterminacy prevents
        a complete operation enumeration; loss of a qualification does not reclassify consolidation as
        synthesis.
    read_back_direction:
      assessment: known
      units:
      - scope: SessionStart pointer and derived-signal delivery
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id025
          - runtime.md#rt-rte-session-reload
          note: The host event triggers automatic selection and stdout delivery without a retained-material
            request.
        records: *id025
        note: Only ACTIVE and derived metadata/signals are pushed, not full workstream prose; actual host
          receipt is unobserved.
      - scope: Detailed work/status/review/extract, receiver inbox, Git/tag and telemetry reads
        assessment: known
        findings:
        - value: pull
          basis: claimed
          records: &id026
          - runtime.md#rt-rte-state-lifecycle
          - runtime.md#rt-rte-work-goal
          - memory.md#mem-obj-project
          - memory.md#mem-obj-archive
          - memory.md#mem-obj-context
          note: The consumer requests retained files, history or telemetry.
        records: *id026
        note: Requested delivery is not another push. Historical recoverability does not mean automatic
          delivery of removed detail.
      - scope: Maintainer inspection of evaluator output
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records: *id013
          note: A later maintainer can request saved session output and fixture history.
        records: *id013
        note: The driver retains inspection artifacts but does not establish an actual later read.
      records:
      - runtime.md#rt-rte-session-reload
      - runtime.md#rt-rte-state-lifecycle
      - runtime.md#rt-rte-work-goal
      - memory.md#mem-obj-project
      - memory.md#mem-obj-archive
      - memory.md#mem-obj-context
      - runtime.md#rt-rte-acceptance-driver
      note: The inventory covers the kit routes. External native checkpoints and host compaction are excluded;
        their unknown direction is not inferred from the kit hook.
    read_back_signal:
      assessment: known
      units:
      - scope: SessionStart availability, roster and threshold selection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: *id025
          note: 'Trigger: SessionStart. Inputs: state availability, roster files, statuses, age, size
            and drain predicates. Selected parts: whole ACTIVE plus conditional aggregate warnings/signals.'
        records: *id025
        note: Availability/threshold selection is separate from active identity matching; there is no
          fixed total token-output budget.
      - scope: SessionStart active-workstream detail selection
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id027
          - runtime.md#rt-rte-session-reload
          - memory.md#mem-obj-active-selector
          note: 'Trigger: SessionStart. Selector input: ACTIVE workstream identity. Matching workstream
            supplies active metadata and roster marking delivered with the pointer.'
        records: *id027
        note: The actual identity match selects delivered active detail, not wholesale injection of the
          requested full workstream.
      - scope: Requested full-file, history, inbox, telemetry and log reads
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-state-lifecycle
        - memory.md#mem-obj-project
        - memory.md#mem-obj-archive
        - memory.md#mem-obj-context
        - runtime.md#rt-rte-acceptance-driver
        note: These operations are pull, so their filenames, literal searches and project matching are
          not push-signal findings.
      records:
      - runtime.md#rt-rte-session-reload
      - memory.md#mem-obj-active-selector
      - runtime.md#rt-rte-state-lifecycle
      - memory.md#mem-obj-project
      - memory.md#mem-obj-archive
      - memory.md#mem-obj-context
      - runtime.md#rt-rte-acceptance-driver
      note: All scoped push operations are the inspected reload chain. Coarse availability and targeted
        identity matching coexist; pull selectors do not add push values.
    trace_learning:
      assessment: partial
      units:
      - scope: Routine capture to committed resume state, Decisions/Learnings and later work
        assessment: known
        findings:
        - value: 'yes'
          basis: claimed
          records: &id028
          - runtime.md#rt-rte-state-lifecycle
          - epistemic.md#epi-rte-capture-synthesis
          - runtime.md#rt-bap-resume-state
          note: Session experience automatically admitted by the model produces retained behavior-shaping
            state for later model invocations.
        records: *id028
        note: This is a prescribed trace-fed pathway, not observed operation, improved capacity or parameter
          learning.
      - scope: Experience extraction to governed standing guidance
        assessment: known
        findings:
        - value: 'yes'
          basis: afforded
          records: &id029
          - memory.md#mem-bap-artifact-adoption
          - epistemic.md#epi-rte-disposition-check
          - runtime.md#rt-bap-skill-guidance
          note: Requested extraction/adoption can change durable guidance later consumed as instruction.
        records: *id029
        note: A Learning marker alone does not establish this path; actual governed adoption and later
          use are unobserved.
      - scope: Telemetry, evaluator raw-log retention and their subsequent human decisions
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-context
        - runtime.md#rt-rte-acceptance-driver
        note: Telemetry is access metadata and raw logs afford investigation; neither record establishes
          an automatic trace-fed durable guidance update from these parts. No bounded absence record licenses
          a local no.
      - scope: Initial optional notes and project-list derivation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-notes
        - memory.md#mem-obj-project
        note: No automatic trace-fed initialization route is established for these included parts. Missing
          control/provenance prevents either yes or no.
      records:
      - runtime.md#rt-rte-state-lifecycle
      - epistemic.md#epi-rte-capture-synthesis
      - runtime.md#rt-bap-resume-state
      - memory.md#mem-bap-artifact-adoption
      - epistemic.md#epi-rte-disposition-check
      - runtime.md#rt-bap-skill-guidance
      - memory.md#mem-obj-context
      - runtime.md#rt-rte-acceptance-driver
      - memory.md#mem-obj-notes
      - memory.md#mem-obj-project
      note: Positive local yes findings do not settle other retained parts. Manual gates and automatic
        capture coexist; no system-wide negative is asserted.
    trace_source:
      assessment: partial
      units:
      - scope: Session conversation feeding routine capture checkpoints
        assessment: known
        findings:
        - value: session-logs
          basis: claimed
          records: &id030
          - runtime.md#rt-rte-state-lifecycle
          - epistemic.md#epi-rte-capture-synthesis
          note: Capture consumes the session conversation, user choices and findings as experience.
        records: *id030
        note: This classifies original conversational content, not its eventual Markdown encoding; raw
          transcript copying is not required.
      - scope: Artifact/tool evidence mixed into capture and extracted guidance
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-state-lifecycle
        - memory.md#mem-bap-artifact-adoption
        - epistemic.md#epi-rte-disposition-check
        note: The records name work findings and artifact evidence but do not establish which original
          tool requests/results, linked trajectories or environmental event records a qualifying update
          actually consumes. Do not turn generic work evidence into tool-traces or event-streams.
      - scope: Telemetry/log investigation and optional-note/PROJECT unknown update routes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-context
        - runtime.md#rt-rte-acceptance-driver
        - memory.md#mem-obj-notes
        - memory.md#mem-obj-project
        note: No qualifying automatic update is established for these branches, so original trace inputs
          cannot be classified. Unresolved trace learning prevents declaring their trace source inapplicable.
      records:
      - runtime.md#rt-rte-state-lifecycle
      - epistemic.md#epi-rte-capture-synthesis
      - memory.md#mem-bap-artifact-adoption
      - epistemic.md#epi-rte-disposition-check
      - memory.md#mem-obj-context
      - runtime.md#rt-rte-acceptance-driver
      - memory.md#mem-obj-notes
      - memory.md#mem-obj-project
      note: Recorded conversation supports session-logs locally. Mixed work evidence and unresolved update
        branches prevent complete trace-source coverage; imported static files and hook triggers alone
        do not establish event-streams.
---

# Claude Workstream Kit memory profile

## Comparison rationale

The scope is retained work memory, not every byte the runtime can access. File storage and intended repository retention coexist. The metadata retained for context-budget reporting is symbolic memory, not a dense model representation. Static installed instructions enter this profile only on the branch where experience changes standing guidance for a later consumer. External host memory and compaction are excluded responsibilities, not negative findings about the kit.

Symbolic form has separate consumption warrants. ACTIVE selectors, workstream index and telemetry have executable parser/selector consumers. PROJECT paths, detailed handoff metadata and archive locators instead have prescribed status/work/receiver or historical-retrieval paths, so their symbolic finding retains a claimed basis. Hook inbox count/age signals do not establish executable consumption of all handoff metadata. The known coverage assessment classifies these named forms; it does not upgrade prescribed consumers to wired ones. See [MEM-OBJ-active-selector](memory.md#mem-obj-active-selector), [MEM-OBJ-workstream-index](memory.md#mem-obj-workstream-index), [MEM-OBJ-context](memory.md#mem-obj-context), [MEM-OBJ-project](memory.md#mem-obj-project), [MEM-OBJ-handoffs](memory.md#mem-obj-handoffs) and [MEM-OBJ-archive](memory.md#mem-obj-archive).

The pointer's symbolic fields route selection; its prose directs later planning. Workstream claims supply context, while plans supply instructions and closure criteria supply validation conditions. Rewrite guards consume retained structure as criteria and enforce refusal only on their own replacement path. These forces must not be projected onto all model or shell writes. See [MEM-OBJ-active-selector](memory.md#mem-obj-active-selector), [MEM-OBJ-active-prose](memory.md#mem-obj-active-prose), [EPI-OBJ-workstream-guidance](epistemic.md#epi-obj-workstream-guidance) and [RT-RTE-rewrite-state](runtime.md#rt-rte-rewrite-state).

Creation approval, substantive review approval and routine model admission are different write mechanisms. A generic CLI caller with a write flag does not establish a per-content human decision. Likewise a deterministic condensation of already-derived memory is not, by itself, another trace-learning route. The positive trace-learning findings concern experience-to-durable-checkpoint or governed-guidance pathways, with their claimed/afforded bases preserved. They establish neither parameter change nor demonstrated improvement. See [RT-RTE-state-lifecycle](runtime.md#rt-rte-state-lifecycle) and [MEM-BAP-artifact-adoption](memory.md#mem-bap-artifact-adoption).

Consolidation includes inspected selected-text reduction despite unproven semantic faithfulness. Rotation additionally reduces the default salience of spent content; historical retrieval remains requested, and full recovery depends on a faithful prior commit/tag. The synthesis request does not establish a new claim absent from its inputs. The EXTENDED protection applies to Learning condensation, not shared scoring or rotation. See [MEM-RTE-learning-condense](memory.md#mem-rte-learning-condense), [MEM-RTE-state-rotate](memory.md#mem-rte-state-rotate), [MEM-CLM-marker-reopening](memory.md#mem-clm-marker-reopening) and [EPI-RTE-capture-synthesis](epistemic.md#epi-rte-capture-synthesis).

Reconciliation supersedes the epistemic Learning-condensation declaration with [MEM-RTE-learning-condense](memory.md#mem-rte-learning-condense). All classification citations use that canonical declaration. The parent rewrite container remains valid; the supersession changes no value or evidence strength. The epistemic qualification-loss deduction concerns the same route, not an observed execution.

The automatic hook is one push chain with coarse eligibility/warnings and an identity match for active detail. Requested full-state and historical reads are pull; neither an identifier in a request nor a delivered response adds another push. The pointer is pushed whole, while full workstream prose is requested separately. See [RT-RTE-session-reload](runtime.md#rt-rte-session-reload) and [MEM-OBJ-archive](memory.md#mem-obj-archive).

Coverage remains partial where initial notes/PROJECT admission and provenance, destination-specific effects, exact transformation shapes, or qualifying mixed trace inputs are unresolved in the accepted records. A local positive does not erase those units. No absence record is supplied, so missing trace routes are not classified as no. Conversation origin supports session-logs; artifact evidence alone does not establish recorded tool-traces or trajectories. Raw evaluator logs afford later manual investigation, not automatic upstream learning. See [MEM-OBJ-notes](memory.md#mem-obj-notes), [MEM-OBJ-project](memory.md#mem-obj-project), [RT-RTE-acceptance-driver](runtime.md#rt-rte-acceptance-driver) and [EPI-RTE-capture-synthesis](epistemic.md#epi-rte-capture-synthesis).

Source-read log: no frozen-source reads were needed. Classification used only the supplied accepted reports and reconciliation; no records, quotations or new evidence were added.
