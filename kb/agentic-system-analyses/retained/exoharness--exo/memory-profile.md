---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: Exo memory comparison of retained artifacts, history, capabilities and opaque native continuation
  state at the frozen revision.
run-id: AAS-2026-10-15-exo-f0905e2cf44b-01
source-identity: https://github.com/exoharness/exo
reviewed-boundary: 423d7d0f4394a1ddc9955d13c73c9f8a9c4d4e7e
memory-comparison:
  version: 2
  scope: 'Retained material accumulated or revised through use: Basic artifact versions and event/recovery
    state; agent facts, conversation plans, skill catalog and payload; installed reusable code; mutable
    managed/local instructions and source changes consumed by later builds; result offloads/previews;
    web cache; scheduler result/pending delivery state; native replay/compaction, warm/resumed state;
    sandbox checkpoint registry and opaque checkpoint contents. Included but unresolved: Claude/Cursor,
    adapter, hosted/UI/evaluator alternatives named in the accepted reports. Excluded: static shipped
    identity/procedures not changed through use, ordinary turn-local RLM variables, credentials/network
    settings as knowledge stores, external model weights/provider internals, and standalone Harbor output
    trajectories without a supported later update consumer. The exporter read of retained journal events
    remains included.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: 'Basic artifact metadata and bytes: facts, todos, skill index/payload, raw result offloads
          and snapshot registry'
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-obj-artifact-versions
          - memory.md#mem-rte-fact-revision
          - memory.md#mem-rte-plan-replacement
          - memory.md#mem-rte-skill-lifecycle
          - memory.md#mem-rte-result-offload
          - memory.md#mem-rte-sandbox-rewind
          note: Version-numbered JSON metadata and bin payloads in the Basic object store establish files,
            independently of JSON encoding. Other storage backends are not thereby classified.
        records: *id001
        note: Version-numbered JSON metadata and bin payloads in the Basic object store establish files,
          independently of JSON encoding. Other storage backends are not thereby classified.
      - scope: Native Basic queued TurnWork
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id002
          - runtime.md#rt-obj-turn-work
          note: Basic serializes the retained queue to turn_queue.json for coordinator recovery.
        records: *id002
        note: Basic serializes the retained queue to turn_queue.json for coordinator recovery.
      - scope: Installed reusable tools, dynamic local profile and guardian outcome files
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id003
          - runtime.md#rt-obj-tool-registry
          - runtime.md#rt-bap-harness-instructions
          - runtime.md#rt-obj-guardian-update
          note: Installed filesystem modules/metadata, reread local profile file and update JSON are separate
            retained file surfaces. Shipped static identity text is excluded.
        records: *id003
        note: Installed filesystem modules/metadata, reread local profile file and update JSON are separate
          retained file surfaces. Shipped static identity text is excluded.
      - scope: Writable Exo source used by guardian rebuild
        assessment: known
        findings:
        - value: repo
          basis: wired
          records: &id004
          - runtime.md#rt-rte-guardian-update
          - runtime.md#rt-bap-rebuilt-services
          note: Retained edits in the source repository enter a later build/module load, conditional on
            writable grants; no executed edit is established.
        records: *id004
        note: Retained edits in the source repository enter a later build/module load, conditional on
          writable grants; no executed edit is established.
      - scope: Web search result cache
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id005
          - epistemic.md#epi-obj-web-result
          - epistemic.md#epi-rte-web-access
          note: Process-local cache retains normalized search results for reuse until TTL/eviction.
        records: *id005
        note: Process-local cache retains normalized search results for reuse until TTL/eviction.
      - scope: Conversation event journal, managed configuration and scheduler retained artifacts across
          host backends
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-managed-turn
        - runtime.md#rt-rte-responses-loop
        - runtime.md#rt-rte-definition-admission
        - runtime.md#rt-rte-background-wakeup
        note: Persistence and later consumers are wired, but these records do not enumerate backend substrates
          for every retained part.
      - scope: Codex warm/resumed/compacted native thread and backend sandbox checkpoint bytes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-codex-compaction
        - memory.md#mem-obj-sandbox-snapshots
        note: Native state persistence and backend checkpoint storage are opaque; their symbolic IDs do
          not establish files, service-object or another substrate.
      - scope: Claude/Cursor memory alternatives; adapter lifecycle and hosted/UI/evaluator selection
          outside the inspected chains
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-native-bridge
        - runtime.md#rt-rte-background-wakeup
        - workflow.md#wf-rte-harbor-trial
        note: Included shipped alternatives are not exhaustively inspected. Storage substrates cannot
          be enumerated from Codex, scheduler and Harbor witnesses; external grading and later trajectory
          consumption are uninspected.
      records:
      - memory.md#mem-obj-artifact-versions
      - memory.md#mem-rte-fact-revision
      - memory.md#mem-rte-plan-replacement
      - memory.md#mem-rte-skill-lifecycle
      - memory.md#mem-rte-result-offload
      - memory.md#mem-rte-sandbox-rewind
      - runtime.md#rt-obj-turn-work
      - runtime.md#rt-obj-tool-registry
      - runtime.md#rt-bap-harness-instructions
      - runtime.md#rt-obj-guardian-update
      - runtime.md#rt-rte-guardian-update
      - runtime.md#rt-bap-rebuilt-services
      - epistemic.md#epi-obj-web-result
      - epistemic.md#epi-rte-web-access
      - runtime.md#rt-rte-managed-turn
      - runtime.md#rt-rte-responses-loop
      - runtime.md#rt-rte-definition-admission
      - runtime.md#rt-rte-background-wakeup
      - memory.md#mem-rte-codex-compaction
      - memory.md#mem-obj-sandbox-snapshots
      - runtime.md#rt-rte-native-bridge
      - workflow.md#wf-rte-harbor-trial
      note: Files, repository edits and a process cache have local witnesses. Native/backend state and
        host-specific alternatives prevent complete storage coverage; external model weights are not accumulated
        Exo memory.
    representational_form:
      assessment: partial
      units:
      - scope: Fact text, todo task text, skill descriptions/procedure text, dynamic local guidance and
          managed instruction bodies
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id006
          - memory.md#mem-obj-exo-memory
          - memory.md#mem-obj-exo-todos
          - memory.md#mem-obj-skills-index
          - memory.md#mem-obj-skill-record
          - runtime.md#rt-bap-harness-instructions
          - runtime.md#rt-rte-definition-admission
          note: These parts receive force through model interpretation. Skill code returned as text is
            not automatically executed by the text reader.
        records: *id006
        note: These parts receive force through model interpretation. Skill code returned as text is not
          automatically executed by the text reader.
      - scope: Artifact IDs/versions, fact IDs/times, todo status, skill membership/paths and snapshot
          registry
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id007
          - memory.md#mem-obj-artifact-versions
          - memory.md#mem-obj-exo-memory
          - memory.md#mem-obj-exo-todos
          - memory.md#mem-obj-skills-index
          - memory.md#mem-obj-sandbox-snapshots
          note: Localized fields have fixed access, status and membership rules; this classifies metadata,
            not opaque payload bytes.
        records: *id007
        note: Localized fields have fixed access, status and membership rules; this classifies metadata,
          not opaque payload bytes.
      - scope: Queue and recovery controls; installed executable modules and registry; guardian status
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id008
          - runtime.md#rt-obj-turn-work
          - runtime.md#rt-rte-managed-turn
          - runtime.md#rt-obj-tool-registry
          - runtime.md#rt-obj-guardian-update
          note: Fixed program rules consume controls and executable modules. Instruction/description strings
            are separate natural-language parts.
        records: *id008
        note: Fixed program rules consume controls and executable modules. Instruction/description strings
          are separate natural-language parts.
      - scope: Retained journal/wakeup/result prose and web text at the later model consumer
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id009
          - runtime.md#rt-rte-responses-loop
          - runtime.md#rt-rte-background-wakeup
          - memory.md#mem-rte-result-offload
          - epistemic.md#epi-obj-web-result
          note: Textual messages, previews and imported page assertions are interpreted by the later model;
            nontext outputs remain separately unresolved.
        records: *id009
        note: Textual messages, previews and imported page assertions are interpreted by the later model;
          nontext outputs remain separately unresolved.
      - scope: Normalized result envelope and replay/access metadata
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id010
          - memory.md#mem-rte-result-offload
          - memory.md#mem-rte-codex-compaction
          note: Call identities, artifact references and chunk/control structure are symbolic; they do
            not reveal the form of all tool payloads or native checkpoints.
        records: *id010
        note: Call identities, artifact references and chunk/control structure are symbolic; they do not
          reveal the form of all tool payloads or native checkpoints.
      - scope: Arbitrary artifact/result payloads and sandbox checkpoint contents
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-artifact-versions
        - memory.md#mem-rte-result-offload
        - memory.md#mem-obj-sandbox-snapshots
        note: Opaque bytes may contain text, symbolic or numerical material. A file substrate and display
          metadata cannot classify their operative form.
      - scope: Codex compacted/warm/resumed payload
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-codex-compaction
        - runtime.md#rt-rte-native-bridge
        note: The bridge exposes no summary representation; neither natural-language nor parametric form
          follows from its compaction request.
      - scope: Claude/Cursor memory alternatives; adapter lifecycle and hosted/UI/evaluator selection
          outside the inspected chains
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-native-bridge
        - runtime.md#rt-rte-background-wakeup
        - workflow.md#wf-rte-harbor-trial
        note: Included shipped alternatives are not exhaustively inspected. Operative forms cannot be
          enumerated from Codex, scheduler and Harbor witnesses; external grading and later trajectory
          consumption are uninspected.
      records:
      - memory.md#mem-obj-exo-memory
      - memory.md#mem-obj-exo-todos
      - memory.md#mem-obj-skills-index
      - memory.md#mem-obj-skill-record
      - runtime.md#rt-bap-harness-instructions
      - runtime.md#rt-rte-definition-admission
      - memory.md#mem-obj-artifact-versions
      - memory.md#mem-obj-sandbox-snapshots
      - runtime.md#rt-obj-turn-work
      - runtime.md#rt-rte-managed-turn
      - runtime.md#rt-obj-tool-registry
      - runtime.md#rt-obj-guardian-update
      - runtime.md#rt-rte-responses-loop
      - runtime.md#rt-rte-background-wakeup
      - memory.md#mem-rte-result-offload
      - epistemic.md#epi-obj-web-result
      - memory.md#mem-rte-codex-compaction
      - runtime.md#rt-rte-native-bridge
      - workflow.md#wf-rte-harbor-trial
      note: Text and fixed-rule metadata/code coexist on distinct consumer paths. Opaque native and backend
        payloads and remaining harnesses prevent complete classification; inference models are external
        dependencies, not a retained-memory parametric witness.
    lineage:
      assessment: partial
      units:
      - scope: Foreground model/caller proposals for facts, task lists and executable tools
        assessment: known
        findings:
        - value: authored
          basis: wired
          records: &id011
          - memory.md#mem-rte-fact-revision
          - memory.md#mem-rte-plan-replacement
          - runtime.md#rt-rte-tool-admission
          note: Inspected paths admit proposed text, plans and source rather than extracting them automatically
            from a transcript. Authored is supported for the proposal path, not authenticated original
            provenance of every submitted byte.
        records: *id011
        note: Inspected paths admit proposed text, plans and source rather than extracting them automatically
          from a transcript. Authored is supported for the proposal path, not authenticated original provenance
          of every submitted byte.
      - scope: Skill payload and local/managed instruction initial provenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-skill-lifecycle
        - runtime.md#rt-bap-harness-instructions
        - runtime.md#rt-rte-definition-admission
        note: Submitted skill text can be user-provided, externally fetched or model-authored. Local-profile
          initial authorship and generic definition caller origin are unresolved; submission alone cannot
          choose authored versus imported for all contents.
      - scope: Web assertions acquired into cached results and journal
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id012
          - epistemic.md#epi-rte-web-access
          - epistemic.md#epi-obj-web-result
          note: Remote search/page text is imported; extraction and truncation do not authenticate its
            source claims.
        records: *id012
        note: Remote search/page text is imported; extraction and truncation do not authenticate its source
          claims.
      - scope: Normalized result envelopes/previews and native replay-derived state
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id013
          - memory.md#mem-rte-result-offload
          - memory.md#mem-rte-codex-compaction
          note: Tool outputs and retained conversational history feed automatic derived representations.
            Trace-extracted names that derivation, not novel knowledge or inspected native summary semantics.
        records: *id013
        note: Tool outputs and retained conversational history feed automatic derived representations.
          Trace-extracted names that derivation, not novel knowledge or inspected native summary semantics.
      - scope: Tool-result offloads, conversation journal and scheduler command-result artifacts
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id014
          - memory.md#mem-rte-result-offload
          - runtime.md#rt-rte-responses-loop
          - runtime.md#rt-rte-background-wakeup
          note: These retain recorded interaction/execution material; the raw trace is kept distinct from
            the derived continuation representation.
        records: *id014
        note: These retain recorded interaction/execution material; the raw trace is kept distinct from
          the derived continuation representation.
      - scope: Raw arbitrary payload antecedents, snapshot contents, source-edit origins and native warm-state
          initial provenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-artifact-versions
        - memory.md#mem-rte-sandbox-rewind
        - runtime.md#rt-rte-guardian-update
        - memory.md#mem-rte-codex-compaction
        note: Capture or storage identifies an immediate route but not all original content provenance.
          Backend/native state and edit authorship are not supplied.
      - scope: Claude/Cursor memory alternatives; adapter lifecycle and hosted/UI/evaluator selection
          outside the inspected chains
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-native-bridge
        - runtime.md#rt-rte-background-wakeup
        - workflow.md#wf-rte-harbor-trial
        note: Included shipped alternatives are not exhaustively inspected. Derivation and initial provenance
          cannot be enumerated from Codex, scheduler and Harbor witnesses; external grading and later
          trajectory consumption are uninspected.
      records:
      - memory.md#mem-rte-fact-revision
      - memory.md#mem-rte-plan-replacement
      - runtime.md#rt-rte-tool-admission
      - memory.md#mem-rte-skill-lifecycle
      - runtime.md#rt-bap-harness-instructions
      - runtime.md#rt-rte-definition-admission
      - epistemic.md#epi-rte-web-access
      - epistemic.md#epi-obj-web-result
      - memory.md#mem-rte-result-offload
      - memory.md#mem-rte-codex-compaction
      - runtime.md#rt-rte-responses-loop
      - runtime.md#rt-rte-background-wakeup
      - memory.md#mem-obj-artifact-versions
      - memory.md#mem-rte-sandbox-rewind
      - runtime.md#rt-rte-guardian-update
      - runtime.md#rt-rte-native-bridge
      - workflow.md#wf-rte-harbor-trial
      note: Known authored proposals, imported web content and trace-derived representations do not settle
        initial contents or opaque alternatives. No inspected compilation of retained semantic claims
        beyond these paths supports other-compiled as an additional value.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Saved facts and plans delivered as standing developer guidance
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id015
          - memory.md#mem-rte-fact-revision
          - memory.md#mem-rte-plan-replacement
          - runtime.md#rt-bap-harness-instructions
          note: The later model is directed to rely on saved facts and maintain the retained plan. This
            is model-interpreted instruction, not truth acceptance or a hard policy gate.
        records: *id015
        note: The later model is directed to rely on saved facts and maintain the retained plan. This
          is model-interpreted instruction, not truth acceptance or a hard policy gate.
      - scope: Skill body/procedure at the model and catalog descriptions requesting relevant body use
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id016
          - memory.md#mem-rte-skill-lifecycle
          - epistemic.md#epi-rte-skills-read
          note: Catalog guidance requests retrieval and the selected procedure requests compliance. Actual
            model compliance is unobserved.
        records: *id016
        note: Catalog guidance requests retrieval and the selected procedure requests compliance. Actual
          model compliance is unobserved.
      - scope: Skill index membership at use_skill
        assessment: known
        findings:
        - value: enforcement
          basis: wired
          records: &id017
          - memory.md#mem-rte-skill-lifecycle
          note: Membership permits/refuses this body-read route. Direct read_skill_file bypasses that
            check, so enforcement is local, not complete revocation.
        records: *id017
        note: Membership permits/refuses this body-read route. Direct read_skill_file bypasses that check,
          so enforcement is local, not complete revocation.
      - scope: Skill index names/paths at body/file lookup and artifact identities at version selection
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id018
          - memory.md#mem-rte-skill-lifecycle
          - memory.md#mem-obj-artifact-versions
          note: Retained access metadata routes fixed lookups to the requested payload/latest version;
            this is not evidence that catalog descriptions are automatically ranked.
        records: *id018
        note: Retained access metadata routes fixed lookups to the requested payload/latest version; this
          is not evidence that catalog descriptions are automatically ranked.
      - scope: Conversation history, tool-result previews, web text and scheduler outputs at later model
          requests
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id019
          - runtime.md#rt-rte-managed-turn
          - runtime.md#rt-rte-responses-loop
          - memory.md#mem-rte-result-offload
          - epistemic.md#epi-rte-web-access
          - runtime.md#rt-rte-background-wakeup
          note: Retained material supplies context or evidence to subsequent answering/action decisions;
            persistence confers no factual warrant.
        records: *id019
        note: Retained material supplies context or evidence to subsequent answering/action decisions;
          persistence confers no factual warrant.
      - scope: Retained tool-result traces at normalization into durable continuation context
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id020
          - memory.md#mem-rte-result-offload
          note: The trace-fed update produces a retained behavior-shaping result envelope/preview for
            later model context. Learning denotes this update consumer, not demonstrated capacity improvement.
        records: *id020
        note: The trace-fed update produces a retained behavior-shaping result envelope/preview for later
          model context. Learning denotes this update consumer, not demonstrated capacity improvement.
      - scope: Retained scheduler execution feedback at continuation-formatting consumer
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id021
          - runtime.md#rt-rte-background-wakeup
          note: Recorded command output/exit feedback feeds a durable formatted wakeup for the later agent
            turn. Learning describes the trace-fed update force, not a correctness check or demonstrated
            improvement.
        records: *id021
        note: Recorded command output/exit feedback feeds a durable formatted wakeup for the later agent
          turn. Learning describes the trace-fed update force, not a correctness check or demonstrated
          improvement.
      - scope: Retained conversational replay at Codex compaction/update consumer
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id022
          - memory.md#mem-rte-codex-compaction
          note: Recorded messages and call/output units feed automatically updated native continuation
            state consumed by a subsequent turn. Native algorithm and semantic payload remain opaque.
        records: *id022
        note: Recorded messages and call/output units feed automatically updated native continuation state
          consumed by a subsequent turn. Native algorithm and semantic payload remain opaque.
      - scope: Retained queue/recovery state, scheduler pending/owner state and native resume metadata
          at progression selectors
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id023
          - runtime.md#rt-rte-managed-turn
          - runtime.md#rt-obj-turn-work
          - runtime.md#rt-rte-background-wakeup
          - runtime.md#rt-rte-native-bridge
          note: State chooses next work, redelivery destination or recovery/replay branch; it does not
            establish an answer oracle.
        records: *id023
        note: State chooses next work, redelivery destination or recovery/replay branch; it does not establish
          an answer oracle.
      - scope: Saved Basic progress/pending-approval state at unresolved-call resumption gate
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id024
          - runtime.md#rt-rte-managed-turn
          - runtime.md#rt-clm-recovery-scope
          note: Runtime checks the retained call/approval correspondence before resumption and can refuse
            unsafe recovery. The retained match supplies a criterion and a veto within Basic only.
        - value: enforcement
          basis: wired
          records: *id024
          note: Runtime checks the retained call/approval correspondence before resumption and can refuse
            unsafe recovery. The retained match supplies a criterion and a veto within Basic only.
        records: *id024
        note: Runtime checks the retained call/approval correspondence before resumption and can refuse
          unsafe recovery. The retained match supplies a criterion and a veto within Basic only.
      - scope: Installed registry identity/module references at subsequent loader
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id025
          - runtime.md#rt-rte-tool-admission
          - runtime.md#rt-bap-installed-code
          note: Retained registry entries select modules/initialization and expose the corresponding capabilities.
            Executable effects are not themselves all classified as permission enforcement.
        records: *id025
        note: Retained registry entries select modules/initialization and expose the corresponding capabilities.
          Executable effects are not themselves all classified as permission enforcement.
      - scope: Managed/local instruction text at later harness/model
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id026
          - runtime.md#rt-rte-definition-admission
          - runtime.md#rt-bap-harness-instructions
          note: Saved definition and dynamic local profile supply standing directions; selected harness/model
            settings separately route execution.
        records: *id026
        note: Saved definition and dynamic local profile supply standing directions; selected harness/model
          settings separately route execution.
      - scope: Retained definition/thread settings and sandbox checkpoint registry at executor/restoration
          selection
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id027
          - runtime.md#rt-rte-definition-admission
          - memory.md#mem-rte-sandbox-rewind
          note: Settings select executor/resources; snapshot IDs select restored state for later commands.
            This does not classify opaque restored file contents.
        records: *id027
        note: Settings select executor/resources; snapshot IDs select restored state for later commands.
          This does not classify opaque restored file contents.
      - scope: Opaque native/snapshot contents, arbitrary tool code effects and guardian changed-source
          semantics
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-codex-compaction
        - memory.md#mem-rte-sandbox-rewind
        - runtime.md#rt-rte-guardian-update
        - runtime.md#rt-rte-tool-admission
        note: Executable behavior and restored bytes can have several forces, but these records do not
          establish every actual retained-content/consumer effect. No ranking or blanket enforcement value
          is inferred from executable authority.
      - scope: Claude/Cursor memory alternatives; adapter lifecycle and hosted/UI/evaluator selection
          outside the inspected chains
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-native-bridge
        - runtime.md#rt-rte-background-wakeup
        - workflow.md#wf-rte-harbor-trial
        note: Included shipped alternatives are not exhaustively inspected. Consumer/effect inventory
          cannot be enumerated from Codex, scheduler and Harbor witnesses; external grading and later
          trajectory consumption are uninspected.
      records:
      - memory.md#mem-rte-fact-revision
      - memory.md#mem-rte-plan-replacement
      - runtime.md#rt-bap-harness-instructions
      - memory.md#mem-rte-skill-lifecycle
      - epistemic.md#epi-rte-skills-read
      - memory.md#mem-obj-artifact-versions
      - runtime.md#rt-rte-managed-turn
      - runtime.md#rt-rte-responses-loop
      - memory.md#mem-rte-result-offload
      - epistemic.md#epi-rte-web-access
      - runtime.md#rt-rte-background-wakeup
      - memory.md#mem-rte-codex-compaction
      - runtime.md#rt-obj-turn-work
      - runtime.md#rt-rte-native-bridge
      - runtime.md#rt-clm-recovery-scope
      - runtime.md#rt-rte-tool-admission
      - runtime.md#rt-bap-installed-code
      - runtime.md#rt-rte-definition-admission
      - memory.md#mem-rte-sandbox-rewind
      - runtime.md#rt-rte-guardian-update
      - workflow.md#wf-rte-harbor-trial
      note: Authority is split by consumer. Instructional reliance and informational context coexist with
        routing, local validation/veto and trace-update learning. No complete authority union or empirical
        effect follows from these wired paths.
    write_agency:
      assessment: partial
      units:
      - scope: Foreground model remember/forget and todowrite admission mechanisms
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id028
          - memory.md#mem-rte-fact-revision
          - memory.md#mem-rte-plan-replacement
          note: Model proposals enter software shape checks without required per-content human approval.
            Generic tool authorization is not approval of each retained byte.
        records: *id028
        note: Model proposals enter software shape checks without required per-content human approval.
          Generic tool authorization is not approval of each retained byte.
      - scope: Foreground model skill and reusable-tool installation/replacement mechanisms
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id029
          - memory.md#mem-rte-skill-lifecycle
          - runtime.md#rt-rte-tool-admission
          note: Software validates and publishes model-proposed contents; initiating a task does not make
            these admissions manual. Generic nonmodel caller control remains a separate unresolved alternative.
        records: *id029
        note: Software validates and publishes model-proposed contents; initiating a task does not make
          these admissions manual. Generic nonmodel caller control remains a separate unresolved alternative.
      - scope: Result normalization/offload, event journaling, scheduler result persistence and native
          replay compaction
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id030
          - memory.md#mem-rte-result-offload
          - runtime.md#rt-rte-responses-loop
          - runtime.md#rt-rte-background-wakeup
          - memory.md#mem-rte-codex-compaction
          note: Software writes/derives retained state without an explicit operator content decision.
            Opaque native transformation details do not erase known host automation.
        records: *id030
        note: Software writes/derives retained state without an explicit operator content decision. Opaque
          native transformation details do not erase known host automation.
      - scope: Web cache insertion and expiry
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id031
          - epistemic.md#epi-rte-web-access
          note: HTTP/search handling admits normalized cached results through software rules.
        records: *id031
        note: HTTP/search handling admits normalized cached results through software rules.
      - scope: Guardian deployment outcome admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id032
          - runtime.md#rt-rte-guardian-update
          - runtime.md#rt-obj-guardian-update
          note: Deferred script records pipeline status without per-outcome human approval; this does
            not settle admission of the source edits being built.
        records: *id032
        note: Deferred script records pipeline status without per-outcome human approval; this does not
          settle admission of the source edits being built.
      - scope: Nonmodel generic API/tool callers; definition changes; local profile/source editing; initial
          skill/fact content and checkpoint replacement control
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-definition-admission
        - runtime.md#rt-bap-harness-instructions
        - runtime.md#rt-rte-guardian-update
        - memory.md#mem-rte-skill-lifecycle
        - memory.md#mem-rte-fact-revision
        - memory.md#mem-rte-sandbox-rewind
        note: Generic caller identity and physical file writes do not establish a human operator decision.
          Capture/rewind requests and reads do not independently prove manual checkpoint replacement.
          These alternative mechanisms remain unresolved.
      - scope: Claude/Cursor memory alternatives; adapter lifecycle and hosted/UI/evaluator selection
          outside the inspected chains
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-native-bridge
        - runtime.md#rt-rte-background-wakeup
        - workflow.md#wf-rte-harbor-trial
        note: Included shipped alternatives are not exhaustively inspected. Admission control cannot be
          enumerated from Codex, scheduler and Harbor witnesses; external grading and later trajectory
          consumption are uninspected.
      records:
      - memory.md#mem-rte-fact-revision
      - memory.md#mem-rte-plan-replacement
      - memory.md#mem-rte-skill-lifecycle
      - runtime.md#rt-rte-tool-admission
      - memory.md#mem-rte-result-offload
      - runtime.md#rt-rte-responses-loop
      - runtime.md#rt-rte-background-wakeup
      - memory.md#mem-rte-codex-compaction
      - epistemic.md#epi-rte-web-access
      - runtime.md#rt-rte-guardian-update
      - runtime.md#rt-obj-guardian-update
      - runtime.md#rt-rte-definition-admission
      - runtime.md#rt-bap-harness-instructions
      - memory.md#mem-rte-sandbox-rewind
      - runtime.md#rt-rte-native-bridge
      - workflow.md#wf-rte-harbor-trial
      note: Automatic model/software routes are wired. No explicit human per-content decision is recorded
        strongly enough to assert manual; unresolved caller/edit alternatives prevent absence or complete
        automatic-only coverage.
    curation_operations:
      assessment: partial
      units:
      - scope: Fact forgetting with historical artifact versions retained
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records: &id033
          - memory.md#mem-rte-fact-revision
          - memory.md#mem-obj-artifact-versions
          - epistemic.md#epi-rte-memory-forget
          note: ID removal withdraws future current-memory reliance while old versions remain. It does
            not establish falsity or erase prior conversation copies.
        records: *id033
        note: ID removal withdraws future current-memory reliance while old versions remain. It does not
          establish falsity or erase prior conversation copies.
      - scope: Fact count cap eviction
        assessment: known
        findings:
        - value: decay
          basis: wired
          records: &id034
          - memory.md#mem-rte-fact-revision
          note: 'Adding beyond 200 keeps newest entries and forgets oldest from current injection: decay
            by capacity, not semantic criticism.'
        records: *id034
        note: 'Adding beyond 200 keeps newest entries and forgets oldest from current injection: decay
          by capacity, not semantic criticism.'
      - scope: Existing plan replacement and same-name skill replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id035
          - memory.md#mem-rte-plan-replacement
          - memory.md#mem-rte-skill-lifecycle
          note: Validated writes revise an existing retained list or skill entry. Unobserved meaning improvement
            is not required for evolve.
        records: *id035
        note: Validated writes revise an existing retained list or skill entry. Unobserved meaning improvement
          is not required for evolve.
      - scope: Skill unlisting with retained payload/history
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records: &id036
          - memory.md#mem-rte-skill-lifecycle
          note: Uninstall withdraws catalog/current use_skill reliance only; direct supporting-file read
            and prior copies survive. Invalidation is bounded to that catalog-mediated path.
        records: *id036
        note: Uninstall withdraws catalog/current use_skill reliance only; direct supporting-file read
          and prior copies survive. Invalidation is bounded to that catalog-mediated path.
      - scope: Tool-result prefix/envelope reduction
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id037
          - memory.md#mem-rte-result-offload
          note: Deterministic preview/pointer representation reduces retained output claims for later
            context while full bytes remain. This is consolidation, not semantic synthesis; mere raw offload
            alone is not the transformation.
        records: *id037
        note: Deterministic preview/pointer representation reduces retained output claims for later context
          while full bytes remain. This is consolidation, not semantic synthesis; mere raw offload alone
          is not the transformation.
      - scope: Web cache TTL and eviction
        assessment: known
        findings:
        - value: decay
          basis: wired
          records: &id038
          - epistemic.md#epi-rte-web-access
          note: Cache forgets entries on expiry/eviction; it does not withdraw claims already copied into
            conversation history.
        records: *id038
        note: Cache forgets entries on expiry/eviction; it does not withdraw claims already copied into
          conversation history.
      - scope: Installed tool replacement/removal
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id039
          - runtime.md#rt-rte-tool-admission
          note: Replacement revises a retained executable capability; removal deletes its store/unlists
            it. Decay is forgetting here, not invalidation with guaranteed retained source history.
        - value: decay
          basis: wired
          records: *id039
          note: Replacement revises a retained executable capability; removal deletes its store/unlists
            it. Decay is forgetting here, not invalidation with guaranteed retained source history.
        records: *id039
        note: Replacement revises a retained executable capability; removal deletes its store/unlists
          it. Decay is forgetting here, not invalidation with guaranteed retained source history.
      - scope: Native compaction transformation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-codex-compaction
        note: A wired request and later continuation state do not expose whether its implemented operation
          consolidates, synthesizes or preserves a different checkpoint. No controlled semantic operation
          is assigned from the command name.
      - scope: Remaining checkpoint, profile/source edits and arbitrary artifact maintenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-sandbox-rewind
        - runtime.md#rt-bap-harness-instructions
        - runtime.md#rt-rte-guardian-update
        - memory.md#mem-obj-artifact-versions
        note: Storage versions, acquisition and requested maintenance alone do not establish controlled
          curation for all retained contents. The transformation and per-part history are missing.
      - scope: Claude/Cursor memory alternatives; adapter lifecycle and hosted/UI/evaluator selection
          outside the inspected chains
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-native-bridge
        - runtime.md#rt-rte-background-wakeup
        - workflow.md#wf-rte-harbor-trial
        note: Included shipped alternatives are not exhaustively inspected. Maintenance transformations
          cannot be enumerated from Codex, scheduler and Harbor witnesses; external grading and later
          trajectory consumption are uninspected.
      records:
      - memory.md#mem-rte-fact-revision
      - memory.md#mem-obj-artifact-versions
      - epistemic.md#epi-rte-memory-forget
      - memory.md#mem-rte-plan-replacement
      - memory.md#mem-rte-skill-lifecycle
      - memory.md#mem-rte-result-offload
      - epistemic.md#epi-rte-web-access
      - runtime.md#rt-rte-tool-admission
      - memory.md#mem-rte-codex-compaction
      - memory.md#mem-rte-sandbox-rewind
      - runtime.md#rt-bap-harness-instructions
      - runtime.md#rt-rte-guardian-update
      - runtime.md#rt-rte-native-bridge
      - runtime.md#rt-rte-background-wakeup
      - workflow.md#wf-rte-harbor-trial
      note: Local evolve, invalidate, decay and deterministic consolidate coexist. No semantic synthesis,
        promotion or near-duplicate merge is inferred from route names, primary-key checks, event conversion
        repair or opaque compaction.
    read_back_direction:
      assessment: partial
      units:
      - scope: Instruction-time facts, open-plan list and skill catalog
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id040
          - memory.md#mem-rte-fact-revision
          - memory.md#mem-rte-plan-replacement
          - memory.md#mem-rte-skill-lifecycle
          note: Assembly automatically supplies retained entries without a foreground request for those
            contents. Exact-path lookup inside that assembly remains part of push, not another consumer-requested
            route.
        records: *id040
        note: Assembly automatically supplies retained entries without a foreground request for those
          contents. Exact-path lookup inside that assembly remains part of push, not another consumer-requested
          route.
      - scope: Later conversation materialization, Codex replay/reuse, registry loading and dynamic guidance
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id041
          - runtime.md#rt-rte-managed-turn
          - runtime.md#rt-rte-responses-loop
          - memory.md#mem-rte-codex-compaction
          - runtime.md#rt-rte-native-bridge
          - runtime.md#rt-rte-tool-admission
          - runtime.md#rt-bap-harness-instructions
          - runtime.md#rt-rte-definition-admission
          note: Harness/runtime automatically brings selected retained history, instructions or capability
            state to a later invocation. No parity is inferred for every native harness.
        records: *id041
        note: Harness/runtime automatically brings selected retained history, instructions or capability
          state to a later invocation. No parity is inferred for every native harness.
      - scope: Scheduler owner-selected wakeup
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id042
          - runtime.md#rt-rte-background-wakeup
          note: Pending result delivery automatically supplies formatted retained output to its owner
            conversation without that consumer requesting retrieval.
        records: *id042
        note: Pending result delivery automatically supplies formatted retained output to its owner conversation
          without that consumer requesting retrieval.
      - scope: Foreground skill/body/file reads and checkpoint rewind
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id043
          - memory.md#mem-rte-skill-lifecycle
          - memory.md#mem-rte-sandbox-rewind
          note: Consumer chooses name/path/snapshot and requests retained material. Checkpoint read-back
            reaches executable filesystem consumers; introspection is a separate afforded described tool
            route below.
        records: *id043
        note: Consumer chooses name/path/snapshot and requests retained material. Checkpoint read-back
          reaches executable filesystem consumers; introspection is a separate afforded described tool
          route below.
      - scope: History introspection description contract
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records: &id044
          - memory.md#mem-clm-history-inspection
          note: Registered model-facing contract affords requested retained telemetry; host-side filtering
            and actual returned records were not independently audited.
        records: *id044
        note: Registered model-facing contract affords requested retained telemetry; host-side filtering
          and actual returned records were not independently audited.
      - scope: Harbor exporter requests recorded event page
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id045
          - workflow.md#wf-rte-harbor-trial
          - workflow.md#wf-obj-trajectory
          note: Later CLI export invocation requests up to 10,000 retained events by type; returning that
            page fulfills pull. External later use of the resulting trajectory is not established.
        records: *id045
        note: Later CLI export invocation requests up to 10,000 retained events by type; returning that
          page fulfills pull. External later use of the resulting trajectory is not established.
      - scope: Search cache hit satisfying model query
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id046
          - epistemic.md#epi-rte-web-access
          note: Reuse returns retained normalized results in fulfillment of an explicit query, not independent
            unsolicited memory supply.
        records: *id046
        note: Reuse returns retained normalized results in fulfillment of an explicit query, not independent
          unsolicited memory supply.
      - scope: General full-result payload reload and opaque backend/native alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-result-offload
        - memory.md#mem-obj-artifact-versions
        - memory.md#mem-rte-codex-compaction
        - memory.md#mem-rte-sandbox-rewind
        note: Artifact APIs establish storage access, not a universal model-facing full-result consumer.
          Native continuation is wired but additional internal requested or automatic routes are opaque.
      - scope: Claude/Cursor memory alternatives; adapter lifecycle and hosted/UI/evaluator selection
          outside the inspected chains
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-native-bridge
        - runtime.md#rt-rte-background-wakeup
        - workflow.md#wf-rte-harbor-trial
        note: Included shipped alternatives are not exhaustively inspected. Read-back alternatives cannot
          be enumerated from Codex, scheduler and Harbor witnesses; external grading and later trajectory
          consumption are uninspected.
      records:
      - memory.md#mem-rte-fact-revision
      - memory.md#mem-rte-plan-replacement
      - memory.md#mem-rte-skill-lifecycle
      - runtime.md#rt-rte-managed-turn
      - runtime.md#rt-rte-responses-loop
      - memory.md#mem-rte-codex-compaction
      - runtime.md#rt-rte-native-bridge
      - runtime.md#rt-rte-tool-admission
      - runtime.md#rt-bap-harness-instructions
      - runtime.md#rt-rte-definition-admission
      - runtime.md#rt-rte-background-wakeup
      - memory.md#mem-rte-sandbox-rewind
      - memory.md#mem-clm-history-inspection
      - workflow.md#wf-rte-harbor-trial
      - workflow.md#wf-obj-trajectory
      - epistemic.md#epi-rte-web-access
      - memory.md#mem-rte-result-offload
      - memory.md#mem-obj-artifact-versions
      note: Both requested pull and independently supplied push have local witnesses. Within a chain the
        requested result return is not counted as an additional push. Full-result reload and alternate
        hosts remain unresolved.
    read_back_signal:
      assessment: partial
      units:
      - scope: Fact injection and skill catalog availability
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id047
          - memory.md#mem-rte-fact-revision
          - memory.md#mem-rte-skill-lifecycle
          note: 'Trigger: instruction assembly. Selector: agent and latest exact-path artifact, then nonempty/readable
            contents. Selected parts: all current facts or indexed names/descriptions. This is coarse
            availability, not topical identity targeting.'
        records: *id047
        note: 'Trigger: instruction assembly. Selector: agent and latest exact-path artifact, then nonempty/readable
          contents. Selected parts: all current facts or indexed names/descriptions. This is coarse availability,
          not topical identity targeting.'
      - scope: Plan injection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id048
          - memory.md#mem-rte-plan-replacement
          note: 'Trigger: assembly. Selector: current conversation/latest list plus any pending/in_progress
            status. Selected part: whole list including closed items when one remains open. Status filtering
            is coarse.'
        records: *id048
        note: 'Trigger: assembly. Selector: current conversation/latest list plus any pending/in_progress
          status. Selected part: whole list including closed items when one remains open. Status filtering
          is coarse.'
      - scope: Conversation history and retained normalized previews
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id049
          - runtime.md#rt-rte-managed-turn
          - runtime.md#rt-rte-responses-loop
          - memory.md#mem-rte-result-offload
          note: 'Trigger: next model request. Selector: conversation scope/cursor and code conversion/length
            budgets. Selected parts: materialized prior messages/results or their fixed prefixes. These
            are coarse scope/budget rules, not inferred relevance.'
        records: *id049
        note: 'Trigger: next model request. Selector: conversation scope/cursor and code conversion/length
          budgets. Selected parts: materialized prior messages/results or their fixed prefixes. These
          are coarse scope/budget rules, not inferred relevance.'
      - scope: Native replay selection and interleaved compaction
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id050
          - memory.md#mem-rte-codex-compaction
          - runtime.md#rt-rte-native-bridge
          note: 'Trigger: failure to reuse a native thread. Selector: replay-eligible history with role
            exclusions and 256,000-character chunk rule. Selected retained parts: call/output-preserving
            chunks. This classifies bridge coarse selection, not opaque internal compaction.'
        records: *id050
        note: 'Trigger: failure to reuse a native thread. Selector: replay-eligible history with role
          exclusions and 256,000-character chunk rule. Selected retained parts: call/output-preserving
          chunks. This classifies bridge coarse selection, not opaque internal compaction.'
      - scope: Scheduler delivery to owner conversation
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records: &id051
          - runtime.md#rt-rte-background-wakeup
          note: 'Trigger: pending fire. Selector input: stored owner conversation/task and pending-delivery
            identity. Match selects that retained result/prompt for the actual destination. This is targeted
            identifier-based push, not merely an address on requested data.'
        records: *id051
        note: 'Trigger: pending fire. Selector input: stored owner conversation/task and pending-delivery
          identity. Match selects that retained result/prompt for the actual destination. This is targeted
          identifier-based push, not merely an address on requested data.'
      - scope: Registry load and dynamic local/managed instruction supply
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id052
          - runtime.md#rt-rte-tool-admission
          - runtime.md#rt-bap-harness-instructions
          - runtime.md#rt-rte-definition-admission
          note: 'Trigger: later registry/request assembly. Selector: installed/enabled entries and configured
            source/path; selected parts: available definitions/modules and standing guidance. Catalog/load
            availability does not establish semantic targeting.'
        records: *id052
        note: 'Trigger: later registry/request assembly. Selector: installed/enabled entries and configured
          source/path; selected parts: available definitions/modules and standing guidance. Catalog/load
          availability does not establish semantic targeting.'
      - scope: Native compacted/warm/resumed internal payload selection
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-codex-compaction
        - runtime.md#rt-rte-native-bridge
        note: Host selection is inspected but the native selector and selected payload are not. No inferred-judgment
          or embedding value follows from a model/native compaction label.
      - scope: Remaining backend checkpoint and source-change internal push consumers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-sandbox-rewind
        - runtime.md#rt-rte-guardian-update
        note: Requested rewind has no independent push-signal finding; subsequent restored-state/module
          consumers are insufficiently decomposed to enumerate all selectors. An upstream requested ID
          alone is not identifier push.
      - scope: Claude/Cursor memory alternatives; adapter lifecycle and hosted/UI/evaluator selection
          outside the inspected chains
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-native-bridge
        - runtime.md#rt-rte-background-wakeup
        - workflow.md#wf-rte-harbor-trial
        note: Included shipped alternatives are not exhaustively inspected. Push selectors cannot be enumerated
          from Codex, scheduler and Harbor witnesses; external grading and later trajectory consumption
          are uninspected.
      records:
      - memory.md#mem-rte-fact-revision
      - memory.md#mem-rte-skill-lifecycle
      - memory.md#mem-rte-plan-replacement
      - runtime.md#rt-rte-managed-turn
      - runtime.md#rt-rte-responses-loop
      - memory.md#mem-rte-result-offload
      - memory.md#mem-rte-codex-compaction
      - runtime.md#rt-rte-native-bridge
      - runtime.md#rt-rte-background-wakeup
      - runtime.md#rt-rte-tool-admission
      - runtime.md#rt-bap-harness-instructions
      - runtime.md#rt-rte-definition-admission
      - memory.md#mem-rte-sandbox-rewind
      - runtime.md#rt-rte-guardian-update
      - workflow.md#wf-rte-harbor-trial
      note: Coarse and owner-identifier push selection are supported locally. Pull-only operations need
        no push signal, but their existence cannot make this partial inventory inapplicable. No inspected
        semantic/embedding/lexical selector is established.
    trace_learning:
      assessment: partial
      units:
      - scope: Automatic result envelope/preview write and later model materialization
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id053
          - memory.md#mem-rte-result-offload
          - runtime.md#rt-rte-responses-loop
          note: Recorded tool output feeds a durable reduced context artifact/envelope and later model
            requests consume it. This qualifies even though reduction is deterministic, no new claim is
            generated and improvement is unobserved.
        records: *id053
        note: Recorded tool output feeds a durable reduced context artifact/envelope and later model requests
          consume it. This qualifies even though reduction is deterministic, no new claim is generated
          and improvement is unobserved.
      - scope: Codex automatic replay compaction and subsequent native turn
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id054
          - memory.md#mem-rte-codex-compaction
          note: Retained session/tool history feeds automatic native-state transformation and later turn
            context. The boundary establishes a durable continuation state route; opaque representation
            limits form/curation, not the wired existence of this trace-fed update.
        records: *id054
        note: Retained session/tool history feeds automatic native-state transformation and later turn
          context. The boundary establishes a durable continuation state route; opaque representation
          limits form/curation, not the wired existence of this trace-fed update.
      - scope: Scheduler result artifact/pending fire to formatted retained wakeup and later agent turn
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id055
          - runtime.md#rt-rte-background-wakeup
          note: Command execution feedback is automatically retained and formatted into subsequent model
            context. This is a trace-fed behavior-shaping continuation route, not an admitted reusable
            lesson or evidence of improvement.
        records: *id055
        note: Command execution feedback is automatically retained and formatted into subsequent model
          context. This is a trace-fed behavior-shaping continuation route, not an admitted reusable lesson
          or evidence of improvement.
      - scope: Foreground remember, plans, skills, reusable-code/source proposals and snapshot contents
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-fact-revision
        - memory.md#mem-rte-plan-replacement
        - memory.md#mem-rte-skill-lifecycle
        - runtime.md#rt-rte-tool-admission
        - runtime.md#rt-rte-guardian-update
        - memory.md#mem-rte-sandbox-rewind
        note: Software/model admission is known, but original trace inputs and a trace-to-durable-update
          relation are not established for every proposal. Experience may inform proposals; generic writes
          alone establish neither yes nor a bounded no.
      - scope: Native warm/resume states apart from inspected replay compaction
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-native-bridge
        - memory.md#mem-rte-codex-compaction
        note: Retention/reuse is known; additional automatic derivation and input details are opaque.
          The replay witness cannot classify all alternative checkpoints.
      - scope: Claude/Cursor memory alternatives; adapter lifecycle and hosted/UI/evaluator selection
          outside the inspected chains
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-native-bridge
        - runtime.md#rt-rte-background-wakeup
        - workflow.md#wf-rte-harbor-trial
        note: Included shipped alternatives are not exhaustively inspected. Qualifying trace-fed writes
          cannot be enumerated from Codex, scheduler and Harbor witnesses; external grading and later
          trajectory consumption are uninspected.
      records:
      - memory.md#mem-rte-result-offload
      - runtime.md#rt-rte-responses-loop
      - memory.md#mem-rte-codex-compaction
      - runtime.md#rt-rte-background-wakeup
      - memory.md#mem-rte-fact-revision
      - memory.md#mem-rte-plan-replacement
      - memory.md#mem-rte-skill-lifecycle
      - runtime.md#rt-rte-tool-admission
      - runtime.md#rt-rte-guardian-update
      - memory.md#mem-rte-sandbox-rewind
      - runtime.md#rt-rte-native-bridge
      - workflow.md#wf-rte-harbor-trial
      note: Three continuation transformations support local yes at wired strength. Raw logs, exported
        trajectories and sequential trials alone are not added learning witnesses. No bounded absence
        record supports a local or system no; unresolved proposal/native routes remain visible.
    trace_source:
      assessment: partial
      units:
      - scope: Tool-result normalization into later context
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records: &id056
          - memory.md#mem-rte-result-offload
          note: Original input is recorded tool result/execution output. Tool-traces describes origin,
            not the JSON serialization of the later event envelope.
        records: *id056
        note: Original input is recorded tool result/execution output. Tool-traces describes origin, not
          the JSON serialization of the later event envelope.
      - scope: 'Codex replay compaction: conversational turns'
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id057
          - memory.md#mem-rte-codex-compaction
          note: Replay consumes retained non-system/developer messages, including prior conversational
            turns.
        records: *id057
        note: Replay consumes retained non-system/developer messages, including prior conversational turns.
      - scope: 'Codex replay compaction: call/output units'
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records: &id058
          - memory.md#mem-rte-codex-compaction
          note: Tool-pair-aware replay chunks retain tool requests/results as input to native compaction.
            These are tool-traces, not trajectories merely because they occur in sequence.
        records: *id058
        note: Tool-pair-aware replay chunks retain tool requests/results as input to native compaction.
          These are tool-traces, not trajectories merely because they occur in sequence.
      - scope: Scheduler command-result formatting into wakeup
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records: &id059
          - runtime.md#rt-rte-background-wakeup
          note: Original stdout/stderr/exit feedback is recorded command execution. Pending-fire wrapping
            does not by itself add event-streams.
        records: *id059
        note: Original stdout/stderr/exit feedback is recorded command execution. Pending-fire wrapping
          does not by itself add event-streams.
      - scope: Additional original content embedded in heterogeneous tool/scheduler outputs and opaque
          native state
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-result-offload
        - runtime.md#rt-rte-background-wakeup
        - memory.md#mem-rte-codex-compaction
        note: Outputs may carry external evidence; these records do not establish calendar/environmental
          events or linked state/action/outcome experience as actual update inputs. Tool-trace origin
          is positive while any additional mixed provenance remains unresolved.
      - scope: 'Other unresolved qualifying writes: proposals, native alternatives, adapters/hosted consumers'
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-fact-revision
        - memory.md#mem-rte-skill-lifecycle
        - memory.md#mem-rte-plan-replacement
        - runtime.md#rt-rte-tool-admission
        - runtime.md#rt-rte-native-bridge
        - runtime.md#rt-rte-background-wakeup
        - workflow.md#wf-rte-harbor-trial
        note: Whether each route qualifies and its original trace content are unresolved. A known continuation
          source cannot make those alternatives inapplicable.
      - scope: Claude/Cursor memory alternatives; adapter lifecycle and hosted/UI/evaluator selection
          outside the inspected chains
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-native-bridge
        - runtime.md#rt-rte-background-wakeup
        - workflow.md#wf-rte-harbor-trial
        note: Included shipped alternatives are not exhaustively inspected. Original trace inputs cannot
          be enumerated from Codex, scheduler and Harbor witnesses; external grading and later trajectory
          consumption are uninspected.
      records:
      - memory.md#mem-rte-result-offload
      - memory.md#mem-rte-codex-compaction
      - runtime.md#rt-rte-background-wakeup
      - memory.md#mem-rte-fact-revision
      - memory.md#mem-rte-skill-lifecycle
      - memory.md#mem-rte-plan-replacement
      - runtime.md#rt-rte-tool-admission
      - runtime.md#rt-rte-native-bridge
      - workflow.md#wf-rte-harbor-trial
      note: Session-logs and tool-traces characterize qualifying inspected continuation writes. No event-streams
        value is inferred from journal/event transport labels and no trajectories value from an export
        file lacking a qualifying later update consumer.
---

# Exo memory profile

## Comparison rationale

All values are classifications of accepted records, not new source findings.
The inventories follow the memory report's inspected and unresolved routes.
No axis is complete: local witnesses do not resolve native payloads, alternate
harnesses, host-specific selection or generic caller control. All positive
implementation findings remain wired unless explicitly marked afforded;
there is no supplied observed operation or causal comparison.

Fact and plan text, symbolic status/membership metadata, executable modules
and opaque checkpoint contents are different operative parts. File storage
does not establish textual form, and a readable ID/preview does not classify
its payload. The local-profile branch includes mutable retained text, not the
shipped static identity prompt. Repository source changes enter the inventory
only through the recorded later rebuild/load path, not as a claim that all
repository files are memory. See [RT-BAP-harness-instructions](runtime.md#rt-bap-harness-instructions),
[RT-RTE-guardian-update](runtime.md#rt-rte-guardian-update),
[MEM-OBJ-sandbox-snapshots](memory.md#mem-obj-sandbox-snapshots) and
[MEM-RTE-codex-compaction](memory.md#mem-rte-codex-compaction).

The fact store's authoritative-context wording gives instructional force,
not verified truth. Skill membership supplies a local read veto, but direct
supporting-file access survives unlisting. Retained approval correspondence
is a criterion and veto on Basic recovery, not an oracle for answer quality.
These consumers explain why instruction, knowledge, routing, validation and
enforcement coexist without implying a universal memory policy. See
[MEM-RTE-fact-revision](memory.md#mem-rte-fact-revision),
[MEM-RTE-skill-lifecycle](memory.md#mem-rte-skill-lifecycle) and
[RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn).

Trace learning here has the profile contract's automatic-write meaning, not
the stronger claim of improved future capacity. Tool-result reduction,
scheduler continuation formatting and native replay compaction have trace-fed
writes and later consumers. Native compaction's opaque algorithm prevents
semantic curation/form classification, not the recorded continuation chain.
The update consumer receives learning authority separately from the later
model's knowledge/context consumption. No presumed reflective criticism,
novel knowledge or improvement is needed for these wired classifications.
Foreground fact/skill/code proposals remain unresolved as trace learning:
software admission alone does not identify their original input. See
[MEM-RTE-result-offload](memory.md#mem-rte-result-offload),
[MEM-RTE-codex-compaction](memory.md#mem-rte-codex-compaction) and
[RT-RTE-background-wakeup](runtime.md#rt-rte-background-wakeup).

Prefix reduction consolidates an existing retained result into less context;
raw offloading or structural validation alone does not. Fact forgetting
invalidates current reliance with version history retained, while capacity
cap eviction forgets old current entries. Skill unlisting is only a bounded
invalidation. No compaction command name establishes synthesis or a semantic
summary. See [MEM-RTE-result-offload](memory.md#mem-rte-result-offload),
[MEM-RTE-fact-revision](memory.md#mem-rte-fact-revision),
[MEM-RTE-skill-lifecycle](memory.md#mem-rte-skill-lifecycle) and
[MEM-RTE-codex-compaction](memory.md#mem-rte-codex-compaction).

Read direction is classified per operation: automatic catalog/context supply
is push; requested skill bodies, event pages and checkpoint restoration are
pull. Ordinary exact-path artifact loading does not establish identifier-based
push targeting. Scheduler owner/task matching does select a retained result
for its destination, unlike coarse availability/status/budget filtering.
Tool and session inputs remain tool-traces/session-logs when serialized as
journal events. An exported trajectory is not a qualifying learning input
without a later automatic update consumer. See
[MEM-RTE-skill-lifecycle](memory.md#mem-rte-skill-lifecycle),
[RT-RTE-background-wakeup](runtime.md#rt-rte-background-wakeup),
[MEM-RTE-codex-compaction](memory.md#mem-rte-codex-compaction) and
[WF-OBJ-trajectory](workflow.md#wf-obj-trajectory).

Reconciliation supersedes the epistemic memory-entry and todo object
identities with [MEM-OBJ-exo-memory](memory.md#mem-obj-exo-memory) and
[MEM-OBJ-exo-todos](memory.md#mem-obj-exo-todos), and the epistemic todo-state
route with [MEM-RTE-plan-replacement](memory.md#mem-rte-plan-replacement).
The profile uses those canonical destinations. These supersessions affect
identity resolution, not a positive value or evidence strength. The combined
epistemic skill object remains a valid container; separate memory catalog and
payload records provide the units. Specialized write/read/forget records
remain valid within the fact-revision lifecycle. No conflict is resolved by
selecting a stronger status.

Source-read log: none. This classification used only the supplied members,
types and contracts; no source ambiguity required a checkout read. No analyst
record was declared, amended or newly evidenced.
