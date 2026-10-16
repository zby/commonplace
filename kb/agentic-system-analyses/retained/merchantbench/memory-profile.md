---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: MerchantBench memory profile covering run-local notes, foreground history, retained traces
  and the unresolved external Hermes memory branch.
run-id: AAS-2026-10-15-merchantbench-d2f4d78dbe37-01
source-identity: https://github.com/khancold/MerchantBench
reviewed-boundary: d9e5bd7519ab100193c21778aecfb59e30f24651
memory-comparison:
  version: 2
  scope: Includes mutable run-local latest Markdown and its version archive, ReAct accumulated message
    history and maintenance, persisted agent traces and human inspection, and visible Hermes profile/session
    storage with unresolved external memory/update/consumer alternatives. Excludes static shipped scenario
    guidance and tool grants, ordinary simulator/business state, unchanged recovery/idempotency checkpoints,
    terminal evaluation reports without an agent feedback route, and remote provider weights not established
    as through-use memory. Hermes external algorithms remain included as unresolved alternatives, not
    inferred from displayed summaries or counters.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Latest document and full-version archive
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-memory-doc
          - memory.md#mem-obj-memory-history
          - memory.md#mem-rte-document-write
          note: Latest body is overwritten; full versions are appended to an adjacent Markdown file.
        records:
        - memory.md#mem-obj-memory-doc
        - memory.md#mem-obj-memory-history
        - memory.md#mem-rte-document-write
        note: Both retained bodies are UTF-8 filesystem files.
      - scope: ReAct accumulated message history
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-history
          - runtime.md#rt-rte-context-trim
          note: Later requests consume the surviving process-local list.
        records:
        - memory.md#mem-obj-history
        - runtime.md#rt-rte-context-trim
        note: The inspected baseline keeps a Python list, not a restored disk history.
      - scope: MerchantBench per-step trace artifacts
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-step-traces
          - memory.md#mem-rte-trace-inspection
          note: Step records are persisted as atomically replaced JSON files for later inspection.
        records:
        - memory.md#mem-obj-step-traces
        - memory.md#mem-rte-trace-inspection
        note: JSON encoding does not change the file substrate.
      - scope: Hermes run-local home and externally authored session database visible to MerchantBench
        assessment: partial
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-rte-hermes-launch
          note: Software prepares and reuses the run-local home, copied skills and configuration.
        - value: sqlite
          basis: wired
          records:
          - memory.md#mem-rte-trace-inspection
          note: The inspection adapter opens the external session state.db; this does not establish its
            internal update algorithms.
        records:
        - runtime.md#rt-rte-hermes-launch
        - memory.md#mem-rte-trace-inspection
        note: Files and the read-only SQLite session adapter are visible; they do not enumerate external
          native memory stores.
      - scope: Other external Hermes retained parts
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-hermes-launch
        - memory.md#mem-rte-trace-inspection
        note: Native memory storage and opaque alternative payloads are not inspected; known profile and
          display storage cannot resolve them.
      records:
      - memory.md#mem-obj-memory-doc
      - memory.md#mem-obj-memory-history
      - memory.md#mem-rte-document-write
      - memory.md#mem-obj-history
      - runtime.md#rt-rte-context-trim
      - memory.md#mem-obj-step-traces
      - memory.md#mem-rte-trace-inspection
      - runtime.md#rt-rte-hermes-launch
      note: Document, archive, foreground history, persisted traces and visible Hermes storage are classified.
        External Hermes native stores and opaque consumed parts remain unresolved.
    representational_form:
      assessment: partial
      units:
      - scope: Document notes/plans and archived submitted bodies at human/model interpretation
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-memory-doc
          - memory.md#mem-obj-memory-history
          - memory.md#mem-bap-document-guidance
          note: Markdown notes, plans and decisions are interpreted as text.
        records:
        - memory.md#mem-obj-memory-doc
        - memory.md#mem-obj-memory-history
        - memory.md#mem-rte-document-write
        - memory.md#mem-bap-document-guidance
        note: The profile classifies the recorded text consumption route, not the semantics of an unavailable
          real run body.
      - scope: Document access envelope and archive version metadata at handlers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-memory-doc
          - memory.md#mem-obj-memory-history
          - memory.md#mem-rte-document-write
          note: Fixed code interprets success, bytes and version-count markers.
        records:
        - memory.md#mem-obj-memory-doc
        - memory.md#mem-obj-memory-history
        - memory.md#mem-rte-document-write
        note: Byte counts, version markers and step/timestamp metadata are separate from the submitted
          body.
      - scope: Foreground history text at the model
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-history
          - runtime.md#rt-rte-context-trim
          note: Selected historical text is supplied to later model requests.
        records:
        - memory.md#mem-obj-history
        - runtime.md#rt-rte-context-trim
        note: Observations, assistant text and tool-result strings are carried by value, without a new
          summary object.
      - scope: Foreground history roles, call IDs and argument structure at request assembly
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-history
          - runtime.md#rt-rte-context-trim
          note: Code selects message groups and sanitizes argument JSON.
        records:
        - memory.md#mem-obj-history
        - runtime.md#rt-rte-context-trim
        note: The symbolic structure is distinct from textual interpretation.
      - scope: Persisted trace content at human inspection
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-step-traces
          - memory.md#mem-rte-trace-inspection
          note: Humans can inspect recorded observations, assistant content and tool-result text.
        records:
        - memory.md#mem-obj-step-traces
        - memory.md#mem-rte-trace-inspection
        note: The display retains raw message content rather than adopting it as guidance.
      - scope: Trace metadata and message envelopes at endpoints/telemetry
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-step-traces
          - memory.md#mem-rte-trace-inspection
          note: Endpoints and aggregators consume structured trace fields.
        records:
        - memory.md#mem-obj-step-traces
        - memory.md#mem-rte-trace-inspection
        note: Step, turn, cost and role fields have fixed readers.
      - scope: Hermes visible configuration and session display
        assessment: partial
        findings:
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-rte-hermes-launch
          - memory.md#mem-rte-trace-inspection
          note: MerchantBench writes configuration and reads session role/active/compacted fields.
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-rte-trace-inspection
          note: The adapter exposes stored message text for human display, not proof of model delivery.
        records:
        - runtime.md#rt-rte-hermes-launch
        - memory.md#mem-rte-trace-inspection
        note: YAML controls and displayed message fields are known; copied skills and actual external
          model context are not classified by the display.
      - scope: External Hermes skills/native memory at their actual consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-hermes-launch
        - memory.md#mem-rte-trace-inspection
        note: Content representations and later external consumption are uninspected. Remote model parameters
          are outside this through-use memory inventory, not a parametric finding.
      records:
      - memory.md#mem-obj-memory-doc
      - memory.md#mem-obj-memory-history
      - memory.md#mem-rte-document-write
      - memory.md#mem-bap-document-guidance
      - memory.md#mem-obj-history
      - runtime.md#rt-rte-context-trim
      - memory.md#mem-obj-step-traces
      - memory.md#mem-rte-trace-inspection
      - runtime.md#rt-rte-hermes-launch
      note: Readable text and symbolic envelopes are separately classified. A displayed Hermes message
        does not classify opaque external model-consumed payloads.
    lineage:
      assessment: partial
      units:
      - scope: Document foreground/human authorship and optional trace-derived notes
        assessment: partial
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-rte-document-write
          note: The foreground model or human supplies a full replacement body through an inspected authoring
            route.
        - value: trace-extracted
          basis: afforded
          records:
          - runtime.md#rt-rte-context-trim
          - memory.md#mem-rte-document-write
          note: The reminder affords selection of important observations/actions/results into durable
            notes; successful extraction is not compulsory.
        records:
        - memory.md#mem-obj-memory-doc
        - memory.md#mem-obj-memory-history
        - memory.md#mem-rte-document-write
        - memory.md#mem-obj-history
        - runtime.md#rt-rte-context-trim
        note: The routes support authorship and optional trace extraction; no actual initial body, complete
          content lineage or exercised derivation is supplied.
      - scope: Archive bodies and symbolic version markers
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-memory-history
          note: Full submitted bodies are copied verbatim into the archive.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-memory-history
          note: The writer constructs version markers, step, time and byte metadata.
        records:
        - memory.md#mem-obj-memory-history
        - memory.md#mem-rte-document-write
        note: The archive copies accepted submitted content and appends code-generated version metadata;
          it does not certify that content's original provenance.
      - scope: Foreground history and per-step trace assembly
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-history
          - memory.md#mem-obj-step-traces
          note: Recorded observations, proposals and results enter the retained message containers.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-step-traces
          note: Server code constructs step, timing and cost envelopes around recorded messages.
        records:
        - memory.md#mem-obj-history
        - memory.md#mem-obj-step-traces
        - runtime.md#rt-rte-react-loop
        note: This unit covers the immediate recording/assembly path, not ultimate provenance of provider
          text or external historical messages.
      - scope: Hermes profile setup and externally authored session records
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records:
          - runtime.md#rt-rte-hermes-launch
          - memory.md#mem-rte-trace-inspection
          note: Installed skills are copied and externally authored session records are exposed through
            a reader.
        - value: other-compiled
          basis: wired
          records:
          - runtime.md#rt-rte-hermes-launch
          note: MerchantBench generates run-local configuration and manifest material.
        records:
        - runtime.md#rt-rte-hermes-launch
        - memory.md#mem-rte-trace-inspection
        note: The copy/import path and generated settings are visible; original skills and session-production
          provenance remain external.
      - scope: External Hermes subsequent memory derivations
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-hermes-launch
        - memory.md#mem-rte-trace-inspection
        note: Summary, skill-update and initial native-memory provenance are not established by launch
          setup or reader output.
      records:
      - memory.md#mem-obj-memory-doc
      - memory.md#mem-obj-memory-history
      - memory.md#mem-rte-document-write
      - memory.md#mem-obj-history
      - runtime.md#rt-rte-context-trim
      - memory.md#mem-obj-step-traces
      - runtime.md#rt-rte-react-loop
      - runtime.md#rt-rte-hermes-launch
      - memory.md#mem-rte-trace-inspection
      note: The recorded admission and derivation paths are retained without claiming complete initial
        provenance or observed payload history.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Latest document at foreground model and human editor
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-bap-document-guidance
          - memory.md#mem-rte-document-read
          note: Delivered notes supply context and advice; reliance and benefit remain unobserved.
        records:
        - memory.md#mem-bap-document-guidance
        - memory.md#mem-rte-document-read
        note: The text supplies notes/planning advice through a requested tool result or textarea, not
          standing system guidance or an executable grant.
      - scope: Retained foreground observations/actions/results at later model calls
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-history
          - runtime.md#rt-rte-react-loop
          note: Surviving text supplies prior observations, decisions and feedback to later model calls.
        records:
        - memory.md#mem-obj-history
        - runtime.md#rt-rte-react-loop
        note: The ordinary consumer receives selected historical context; no expected-answer oracle is
          created.
      - scope: Foreground trace material at optional durable-note update
        assessment: known
        findings:
        - value: learning
          basis: afforded
          records:
          - runtime.md#rt-rte-context-trim
          - memory.md#mem-rte-document-write
          note: Accumulated experience can shape model-selected durable notes that can later return as
            context. No exercised improvement is asserted.
        records:
        - runtime.md#rt-rte-context-trim
        - memory.md#mem-rte-document-write
        note: This is the afforded update consumer, separate from the resulting document's downstream
          advisory force.
      - scope: Persisted trace text at human inspection
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-step-traces
          - memory.md#mem-rte-trace-inspection
          note: Trace endpoints deliver historical messages to human viewers.
        records:
        - memory.md#mem-obj-step-traces
        - memory.md#mem-rte-trace-inspection
        note: Viewing raw recorded material supplies inspection evidence, not automatic strategy acceptance.
      - scope: Archive version markers at the later archive writer
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-history
        note: The established consumer counts markers to construct the next version number. This metadata
          computation establishes no controlled authority value; it selects no operation, destination,
          scope or input window. No historical-body restore consumer is inferred.
      - scope: External Hermes retained skills, summaries and native memory at external consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-hermes-launch
        - memory.md#mem-rte-trace-inspection
        note: Launch settings and displayed session text do not establish actual external authority paths.
          The static configuration itself is not learned memory.
      records:
      - memory.md#mem-bap-document-guidance
      - memory.md#mem-rte-document-read
      - memory.md#mem-obj-history
      - runtime.md#rt-rte-react-loop
      - runtime.md#rt-rte-context-trim
      - memory.md#mem-rte-document-write
      - memory.md#mem-obj-step-traces
      - memory.md#mem-rte-trace-inspection
      - memory.md#mem-obj-memory-history
      - runtime.md#rt-rte-hermes-launch
      note: Knowledge and conditional learning paths are supported locally. No instruction, permission,
        ranking or validation force is inferred merely from a memory filename or from static runtime controls.
    write_agency:
      assessment: partial
      units:
      - scope: Foreground model document replacement and archive append
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-document-write
          note: Model proposes content and protocol/size checks admit it, then append a version.
        records:
        - memory.md#mem-rte-document-write
        - runtime.md#rt-rte-context-trim
        note: No human approves each model-selected body; optional invocation does not make software admission
          manual.
      - scope: Human editor save of the same document
        assessment: known
        findings:
        - value: manual
          basis: wired
          records:
          - memory.md#mem-rte-document-write
          note: The human can edit and save the retained body through the shipped UI.
        records:
        - memory.md#mem-rte-document-write
        note: The save button supplies the textarea content as an explicit per-content human decision.
      - scope: Other generic document callers and initialization
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-document-write
        - memory.md#mem-obj-memory-doc
        note: The generic API and an unobserved initial payload do not establish whether a human supplies
          or approves each content change.
      - scope: Foreground history admission and server raw trace capture
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-history
          - memory.md#mem-obj-step-traces
          - runtime.md#rt-rte-react-loop
          note: Client code accumulates history and server code writes action/final-step records.
        records:
        - memory.md#mem-obj-history
        - memory.md#mem-obj-step-traces
        - runtime.md#rt-rte-react-loop
        note: These mechanisms record messages without a per-message human admission decision.
      - scope: Hermes initial profile copy and configuration preparation
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-hermes-launch
          note: The registry copies installed skills at first profile creation and rewrites configuration
            on reuse.
        records:
        - runtime.md#rt-rte-hermes-launch
        note: Operator installation provides the source files; run-specific admission is a software copy,
          not per-skill human approval.
      - scope: External Hermes native-memory, summary and skill updates
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-hermes-launch
        - memory.md#mem-rte-trace-inspection
        note: Actual external admission controls and checkpoint replacement routes are not inspected.
      records:
      - memory.md#mem-rte-document-write
      - runtime.md#rt-rte-context-trim
      - memory.md#mem-obj-memory-doc
      - memory.md#mem-obj-history
      - memory.md#mem-obj-step-traces
      - runtime.md#rt-rte-react-loop
      - runtime.md#rt-rte-hermes-launch
      - memory.md#mem-rte-trace-inspection
      note: Admission differs across foreground software, explicit human edits, raw capture and external
        initialization. Generic API caller identity and external updates remain unresolved.
    curation_operations:
      assessment: partial
      units:
      - scope: Latest document full replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-rte-document-write
          note: A later accepted body revises the existing latest entry by full overwrite.
        - value: invalidate
          basis: wired
          records:
          - memory.md#mem-rte-document-write
          - memory.md#mem-obj-memory-history
          note: An empty replacement clears current content while older versions remain archived.
        records:
        - memory.md#mem-rte-document-write
        - memory.md#mem-obj-memory-history
        note: The unit is the implemented revision mechanism, not a claim that every submitted body improves
          or changes a strategy.
      - scope: Optional foreground preservation of important details into notes
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-context-trim
        - memory.md#mem-rte-document-write
        - epistemic.md#epi-rte-memory-document
        note: The reminder requests preservation and the handler admits arbitrary full bodies. Neither
          establishes selection or compression into a reduced representation of existing claims.
          Without content establishing the semantic transformation, no curation value is determined
          for this optional note-production step; replacement is classified separately.
      - scope: Foreground history recency eviction and retry filtering
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-obj-history
          - runtime.md#rt-rte-context-trim
          - runtime.md#rt-rte-react-loop
          note: Old turns are dropped by age/budget; retry filtering can remove tool-result content.
        records:
        - memory.md#mem-obj-history
        - runtime.md#rt-rte-context-trim
        - runtime.md#rt-rte-react-loop
        note: Only the local context copy is forgotten; independent server traces and documents remain.
      - scope: Whole-run removal of retained artifacts
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-rte-run-withdrawal
          note: Successful run-directory removal forgets its documents, versions, traces and profiles.
        records:
        - memory.md#mem-rte-run-withdrawal
        note: Destructive local forgetting is not semantic invalidation with retained local history or
          secure remote erasure.
      - scope: External Hermes compaction, native-memory and skill maintenance
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-hermes-launch
        - memory.md#mem-rte-trace-inspection
        note: Settings and reported counters do not establish consolidation, synthesis, deduplication,
          promotion or any other external implemented transformation.
      records:
      - memory.md#mem-rte-document-write
      - memory.md#mem-obj-memory-history
      - runtime.md#rt-rte-context-trim
      - memory.md#mem-obj-history
      - runtime.md#rt-rte-react-loop
      - memory.md#mem-rte-run-withdrawal
      - runtime.md#rt-rte-hermes-launch
      - memory.md#mem-rte-trace-inspection
      note: Local replacement and eviction are inspected; the optional trace-to-notes semantic transformation
        is not determined by the preservation request or byte admission. External curation is not resolved
        by compaction counters.
    read_back_direction:
      assessment: partial
      units:
      - scope: Explicit latest-document requests, including human editor reads
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-document-read
          note: The model requests read_memory_doc or a human presses read and receives the whole latest
            body.
        records:
        - memory.md#mem-rte-document-read
        - memory.md#mem-bap-document-guidance
        note: Identity addressing fulfills the request; the tool return is not an independent unsolicited
          push.
      - scope: Human historical trace requests and visible Hermes trace adapter
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-trace-inspection
          note: Requested trace endpoints and UI loads expose persisted messages.
        records:
        - memory.md#mem-rte-trace-inspection
        note: A chosen step/all-trace request returns retained material to a viewer, not automatically
          to an agent.
      - scope: ReAct selected history at automatic subsequent request construction
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-history
          - runtime.md#rt-rte-context-trim
          - runtime.md#rt-rte-react-loop
          note: Request assembly supplies a recent surviving historical suffix without a separate request
            to retrieve each prior message.
        records:
        - memory.md#mem-obj-history
        - runtime.md#rt-rte-context-trim
        - runtime.md#rt-rte-react-loop
        note: This is the automatic reuse of retained context, not a second direction assigned to the
          requested document return itself.
      - scope: Archive markers at later version append
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-obj-memory-history
          note: The append writer reads prior markers for version numbering.
        records:
        - memory.md#mem-obj-memory-history
        note: The later writer explicitly reads the archive to count markers; no historical-body reload
          is established.
      - scope: External Hermes actual model-context and skill read-back
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-hermes-launch
        - memory.md#mem-rte-trace-inspection
        note: Active/compacted display filtering is not evidence of what its runtime delivers to a model.
      records:
      - memory.md#mem-rte-document-read
      - memory.md#mem-bap-document-guidance
      - memory.md#mem-rte-trace-inspection
      - memory.md#mem-obj-history
      - runtime.md#rt-rte-context-trim
      - runtime.md#rt-rte-react-loop
      - memory.md#mem-obj-memory-history
      - runtime.md#rt-rte-hermes-launch
      note: Requested document/trace delivery and automatic foreground history selection are distinct
        operations. External model-context read-back remains uninspected.
    read_back_signal:
      assessment: partial
      units:
      - scope: Foreground historical suffix automatically supplied on a later model request
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-history
          - runtime.md#rt-rte-context-trim
          - runtime.md#rt-rte-react-loop
          note: Recency, role boundaries and budget filter availability without semantic targeting.
        records:
        - memory.md#mem-obj-history
        - runtime.md#rt-rte-context-trim
        - runtime.md#rt-rte-react-loop
        note: 'Trigger: request construction/threshold maintenance. Inputs: message order, roles and estimated
          or reported size. Selected part: newest surviving history, with leading orphan tool messages
          removed.'
      - scope: Explicit document and trace requests, plus archive marker read
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-document-read
        - memory.md#mem-rte-trace-inspection
        - memory.md#mem-obj-memory-history
        note: These units fulfill requested reads. Run/agent/step identifiers address those requests;
          they do not establish identifier-based push.
      - scope: External Hermes automatic retained-content selectors
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-hermes-launch
        - memory.md#mem-rte-trace-inspection
        note: The external selectors and their inputs are not inspected. Display filters cannot classify
          model-context push signals.
      records:
      - memory.md#mem-obj-history
      - runtime.md#rt-rte-context-trim
      - runtime.md#rt-rte-react-loop
      - memory.md#mem-rte-document-read
      - memory.md#mem-rte-trace-inspection
      - memory.md#mem-obj-memory-history
      - runtime.md#rt-rte-hermes-launch
      note: The known push uses recency and budget, not task relevance or an identity match. Pull routes
        do not contribute push selector values; external push alternatives remain unresolved.
    trace_learning:
      assessment: partial
      units:
      - scope: Foreground experience saved as durable document and later explicitly recalled
        assessment: known
        findings:
        - value: 'yes'
          basis: afforded
          records:
          - runtime.md#rt-rte-context-trim
          - memory.md#mem-rte-document-write
          - memory.md#mem-rte-document-read
          - memory.md#mem-bap-document-guidance
          note: Accumulated observations/actions/results can feed durable notes that shape later context.
            No new knowledge or demonstrated improvement is required for this route classification.
        records:
        - runtime.md#rt-rte-context-trim
        - memory.md#mem-rte-document-write
        - memory.md#mem-rte-document-read
        - memory.md#mem-bap-document-guidance
        note: Model/software admission is automatic if the foreground agent takes the offered save route.
          Persistence and a later context consumer exist, but successful save/recall in a real run is
          unobserved.
      - scope: Raw history/trace capture, archive duplication and suffix eviction considered alone
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-history
        - memory.md#mem-obj-step-traces
        - memory.md#mem-obj-memory-history
        - memory.md#mem-clm-telemetry-limits
        note: These records establish raw retention, copying and filtering, not a separate qualifying
          durable derived artifact. They do not supply a formal bounded-absence record for a local no
          finding; the qualifying document route is assessed separately.
      - scope: External Hermes summary, skill and native-memory writes
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-hermes-launch
        - memory.md#mem-rte-trace-inspection
        note: Configuration and evolution/compaction counts do not establish or exclude an automatic trace-fed
          durable behavior-shaping write.
      records:
      - runtime.md#rt-rte-context-trim
      - memory.md#mem-rte-document-write
      - memory.md#mem-rte-document-read
      - memory.md#mem-bap-document-guidance
      - memory.md#mem-obj-history
      - memory.md#mem-obj-step-traces
      - memory.md#mem-obj-memory-history
      - memory.md#mem-clm-telemetry-limits
      - runtime.md#rt-rte-hermes-launch
      - memory.md#mem-rte-trace-inspection
      note: The local trace-to-document-to-later-model chain is afforded, not exercised or mandatory.
        Raw capture alone is not trace learning, and external writes remain unresolved.
    trace_source:
      assessment: partial
      units:
      - scope: Recorded conversational and tool material available to the foreground note writer
        assessment: known
        findings:
        - value: session-logs
          basis: afforded
          records:
          - memory.md#mem-obj-history
          - runtime.md#rt-rte-context-trim
          - memory.md#mem-rte-document-write
          note: The optional note update can consume accumulated agent-work conversational turns.
        - value: tool-traces
          basis: afforded
          records:
          - memory.md#mem-obj-history
          - runtime.md#rt-rte-context-trim
          - memory.md#mem-rte-document-write
          note: The same history carries recorded tool calls, results and execution feedback for optional
            preservation.
        records:
        - memory.md#mem-obj-history
        - runtime.md#rt-rte-context-trim
        - memory.md#mem-rte-document-write
        note: The source is the recorded foreground message content, including observation/assistant turns
          and tool requests/results, not the Markdown encoding of the output.
      - scope: Original inputs of external Hermes qualifying writes, if any
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-hermes-launch
        - memory.md#mem-rte-trace-inspection
        - memory.md#mem-clm-telemetry-limits
        note: No external qualifying update or its original input set is established. Session display
          and counters cannot resolve mixed trace origins or make this branch inapplicable.
      records:
      - memory.md#mem-obj-history
      - runtime.md#rt-rte-context-trim
      - memory.md#mem-rte-document-write
      - runtime.md#rt-rte-hermes-launch
      - memory.md#mem-rte-trace-inspection
      - memory.md#mem-clm-telemetry-limits
      note: Source values are scoped to the afforded document-learning route, not to all stored logs.
        External qualifying writes and their original sources remain uninspected.
---

# MerchantBench memory profile

## Comparison rationale

The local memory mechanism is optional full-document authoring and explicit
recall, alongside process-local historical context and a separately persisted
inspection trace. The document is not automatically reintroduced after eviction.
A requested return is pull; automatic reuse of the surviving historical suffix
is a separate coarse push operation. The archive's only established later
consumer counts version markers. That computation establishes no routing authority:
it constructs output numbering without selecting an operation, destination, scope
or input window. The profile does not invent a model restore route ([MEM-RTE-document-read](memory.md#mem-rte-document-read),
[MEM-OBJ-history](memory.md#mem-obj-history),
[MEM-OBJ-memory-history](memory.md#mem-obj-memory-history),
[RT-RTE-context-trim](runtime.md#rt-rte-context-trim)).

The optional experience-to-note path supports afforded trace learning, not a
wired summarizer, mandatory successful save or observed improvement. It does not
establish consolidation: the reminder requests preservation, while the write
handler accepts arbitrary full bodies. The semantic transformation remains
undetermined without content, as retained in
[EPI-RTE-memory-document](epistemic.md#epi-rte-memory-document). The implemented
replacement and eviction findings remain separate from this unresolved step. A model choosing its own content followed by software admission is
automatic agency; the human editor's explicit save is a separate manual route.
The update consumer's learning force is distinct from the resulting note's
knowledge force at later model calls. Plans in a requested tool result do not
thereby become standing instructions. No semantic admission criterion follows
from the byte limit ([MEM-RTE-document-write](memory.md#mem-rte-document-write),
[MEM-BAP-document-guidance](memory.md#mem-bap-document-guidance),
[RT-RTE-context-trim](runtime.md#rt-rte-context-trim)).

The trace-source findings describe original conversational and tool content
available to that optional write. No independent event-stream origin is inferred
from simulation timestamps or JSON envelopes. No trajectory-training/update route
is established merely by sequential logs. Raw recording and suffix deletion do
not on their own produce a durable derived continuation summary
([MEM-OBJ-history](memory.md#mem-obj-history),
[MEM-OBJ-step-traces](memory.md#mem-obj-step-traces),
[MEM-CLM-telemetry-limits](memory.md#mem-clm-telemetry-limits)).

Reconciliation supersedes the epistemic scratchpad object with
[MEM-OBJ-memory-doc](memory.md#mem-obj-memory-doc). All document classifications
use that canonical object. The combined epistemic admission/retention/recall
container remains valid; the more specific memory routes provide the local
warrants here. No supersession changes a controlled value or upgrades its basis.

Every axis remains partial because actual external Hermes memory transformations
and consumers are uninspected. Visible filesystem setup, SQLite inspection and
readable session display do not classify opaque consumed payloads, establish
skill learning or exclude alternate native memory. Known local findings are not
weakened or promoted by that uncertainty
([RT-RTE-hermes-launch](runtime.md#rt-rte-hermes-launch),
[MEM-RTE-trace-inspection](memory.md#mem-rte-trace-inspection),
[MEM-CLM-telemetry-limits](memory.md#mem-clm-telemetry-limits)).

Source-read log: none. This profile classifies supplied accepted records and
annotations after reconciliation; it adds no source evidence or record
declarations. All positive findings are implementation wiring or explicitly
marked affordances, not observed operation or causal benefit.
