---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Swamp memory comparison: versioned automation data, issue resources, reports, command audit
  and execution continuation with unresolved alternative consumers.'
run-id: AAS-2026-10-15-swamp-440d19cc0bcc-01
source-identity: https://github.com/swamp-club/swamp
reviewed-boundary: 380e3c307164501c7d705f7707a864f4612b2785
memory-comparison:
  version: 2
  scope: 'Retained material accumulated or revised through Swamp use: versioned resource/file content
    and access metadata; issue plans, feedback, findings, phase and verification state; method/verification
    reports; command audit; workflow checkpoints and evaluated replay forms; task briefs; editable/reloaded
    extension capabilities; retained evaluation outcomes and attestations. Includes unresolved acquisition,
    custom-report, remote-backend, cache, maintenance and later-consumer alternatives identified in the
    accepted records. Excludes static shipped skills/prompts as memory objects, ephemeral scratch state
    without a later invocation, external harness conversation/compaction and model weights, and external
    service internals. Shipped skills remain evidence of instructed consumption of retained objects.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Persistent resource/file content and its access metadata
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-data-content
          - memory.md#mem-rte-resource-storage
          note: Content files, YAML metadata and latest/version directories establish files; ephemeral-only
            working data is excluded from retained memory.
        records:
        - memory.md#mem-obj-data-content
        - memory.md#mem-rte-resource-storage
        note: Content files, YAML metadata and latest/version directories establish files; ephemeral-only
          working data is excluded from retained memory.
      - scope: Issue plan-main
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-plan-main
          - memory.md#mem-rte-plan-iteration
          note: Plan JSON is persisted through the versioned file-backed data repository.
        records:
        - memory.md#mem-obj-plan-main
        - memory.md#mem-rte-plan-iteration
        note: Plan JSON is persisted through the versioned file-backed data repository.
      - scope: Issue feedback-main
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-feedback-main
          - memory.md#mem-rte-plan-iteration
          note: Feedback JSON uses the same inspected persistent resource path.
        records:
        - memory.md#mem-obj-feedback-main
        - memory.md#mem-rte-plan-iteration
        note: Feedback JSON uses the same inspected persistent resource path.
      - scope: Adversarial and conformance findings
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-review-findings
          - memory.md#mem-rte-lifecycle-checks
          note: Both resource families use versioned persistent JSON files.
        records:
        - memory.md#mem-obj-review-findings
        - memory.md#mem-rte-lifecycle-checks
        note: Both resource families use versioned persistent JSON files.
      - scope: Issue phase and verificationResult resources
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-lifecycle-state
          - memory.md#mem-rte-lifecycle-checks
          note: Persistent resource storage is established for phase and verification flags.
        records:
        - memory.md#mem-obj-lifecycle-state
        - memory.md#mem-rte-lifecycle-checks
        note: Persistent resource storage is established for phase and verification flags.
      - scope: Method report Markdown and JSON artifacts
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-method-report
          - memory.md#mem-rte-report-retrieval
          note: Separate persisted report files retain both representations.
        records:
        - memory.md#mem-obj-method-report
        - memory.md#mem-rte-report-retrieval
        note: Separate persisted report files retain both representations.
      - scope: Verification summary Markdown and JSON artifacts
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - epistemic.md#epi-obj-verification-summary
          - epistemic.md#epi-rte-report-summary
          note: The report persistence wrapper saves file artifacts.
        records:
        - epistemic.md#epi-obj-verification-summary
        - epistemic.md#epi-rte-report-summary
        note: The report persistence wrapper saves file artifacts.
      - scope: Command audit records
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-command-audit
          - memory.md#mem-rte-audit-timeline
          note: Date-partitioned JSONL files retain selected command events.
        records:
        - memory.md#mem-obj-command-audit
        - memory.md#mem-rte-audit-timeline
        note: Date-partitioned JSONL files retain selected command events.
      - scope: Workflow run checkpoint
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-obj-workflow-run
          - runtime.md#rt-rte-workflow-run
          note: Atomic YAML run records establish files; evaluated plan repositories are distinct.
        records:
        - runtime.md#rt-obj-workflow-run
        - runtime.md#rt-rte-workflow-run
        note: Atomic YAML run records establish files; evaluated plan repositories are distinct.
      - scope: Task brief
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-obj-task-brief
          - runtime.md#rt-rte-agent-launch
          note: The retained workspace Markdown brief is a file.
        records:
        - runtime.md#rt-obj-task-brief
        - runtime.md#rt-rte-agent-launch
        note: The retained workspace Markdown brief is a file.
      - scope: Editable extension sources, bundles and catalog
        assessment: partial
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-rte-extension-load
          - runtime.md#rt-bap-workflow-execution
          note: Local source and bundled code persist for later type resolution.
        records:
        - runtime.md#rt-rte-extension-load
        - runtime.md#rt-bap-workflow-execution
        note: Code and cached bundle files are established, but the catalog/registry persistence substrate
          is not fully characterized.
      - scope: Attestation hosted state and fetched CI representation
        assessment: partial
        findings:
        - value: files
          basis: wired
          records:
          - epistemic.md#epi-obj-attestation
          - epistemic.md#epi-rte-attestation-build
          - epistemic.md#epi-rte-attestation-ci
          note: CI reads the fetched attestation file.
        records:
        - epistemic.md#epi-obj-attestation
        - epistemic.md#epi-rte-attestation-build
        - epistemic.md#epi-rte-attestation-ci
        note: A fetched JSON file is consumed by CI; server-side persistence and provenance remain outside
          inspected implementation.
      - scope: Retained skill-evaluation outcomes
        assessment: partial
        findings:
        - value: files
          basis: wired
          records:
          - epistemic.md#epi-obj-skill-evals
          - epistemic.md#epi-rte-skill-evals
          - runtime.md#rt-obj-workflow-run
          - runtime.md#rt-rte-workflow-run
          note: Selected outcomes persist through the inspected shell/run file-backed path.
        records:
        - epistemic.md#epi-obj-skill-evals
        - epistemic.md#epi-rte-skill-evals
        note: Shell/run outputs retain selected outcomes; external evaluator storage and optional Actions-summary
          backing storage are not inspected.
      - scope: Evaluated plan/cache repositories, remote data backends and remaining retained acquisition/notification
          outputs
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-data-content
        - memory.md#mem-rte-resource-storage
        - runtime.md#rt-obj-workflow-run
        - runtime.md#rt-rte-workflow-run
        - runtime.md#rt-rte-extension-load
        - runtime.md#rt-bap-workflow-execution
        note: Records retain these alternatives without inspecting their complete persistence; neither
          repo, SQLite, service-object nor another substrate can be supplied from labels.
      records:
      - memory.md#mem-obj-data-content
      - memory.md#mem-rte-resource-storage
      - memory.md#mem-obj-plan-main
      - memory.md#mem-rte-plan-iteration
      - memory.md#mem-obj-feedback-main
      - memory.md#mem-obj-review-findings
      - memory.md#mem-rte-lifecycle-checks
      - memory.md#mem-obj-lifecycle-state
      - memory.md#mem-obj-method-report
      - memory.md#mem-rte-report-retrieval
      - epistemic.md#epi-obj-verification-summary
      - epistemic.md#epi-rte-report-summary
      - memory.md#mem-obj-command-audit
      - memory.md#mem-rte-audit-timeline
      - runtime.md#rt-obj-workflow-run
      - runtime.md#rt-rte-workflow-run
      - runtime.md#rt-obj-task-brief
      - runtime.md#rt-rte-agent-launch
      - runtime.md#rt-rte-extension-load
      - runtime.md#rt-bap-workflow-execution
      - epistemic.md#epi-obj-attestation
      - epistemic.md#epi-rte-attestation-build
      - epistemic.md#epi-rte-attestation-ci
      - epistemic.md#epi-obj-skill-evals
      - epistemic.md#epi-rte-skill-evals
      note: Local retained objects have file-backed witnesses. Backend adapters, hosted persistence and
        some alternative paths remain unresolved; JSON/YAML encoding does not establish SQLite or relational
        storage.
    representational_form:
      assessment: partial
      units:
      - scope: Plan, feedback and finding prose interpreted by agents/humans
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-plan-main
          - memory.md#mem-rte-plan-iteration
          - memory.md#mem-obj-feedback-main
          - memory.md#mem-obj-review-findings
          - memory.md#mem-rte-lifecycle-checks
          note: Descriptions, reasons, criticism and resolution notes require natural-language interpretation.
        records:
        - memory.md#mem-obj-plan-main
        - memory.md#mem-rte-plan-iteration
        - memory.md#mem-obj-feedback-main
        - memory.md#mem-obj-review-findings
        - memory.md#mem-rte-lifecycle-checks
        note: Descriptions, reasons, criticism and resolution notes require natural-language interpretation.
      - scope: Issue versions, finding flags, phases and verification flags at deterministic consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-plan-main
          - memory.md#mem-rte-plan-iteration
          - memory.md#mem-obj-review-findings
          - memory.md#mem-rte-lifecycle-checks
          - memory.md#mem-obj-lifecycle-state
          note: Version equality, severity/resolution predicates and phase fields are localized symbolic
            units.
        records:
        - memory.md#mem-obj-plan-main
        - memory.md#mem-rte-plan-iteration
        - memory.md#mem-obj-review-findings
        - memory.md#mem-rte-lifecycle-checks
        - memory.md#mem-obj-lifecycle-state
        note: Version equality, severity/resolution predicates and phase fields are localized symbolic
          units.
      - scope: Method/verification report narrative at display consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-method-report
          - memory.md#mem-rte-report-retrieval
          - epistemic.md#epi-obj-verification-summary
          - epistemic.md#epi-rte-report-summary
          note: Readable Markdown provides selected natural-language execution accounts, not the underlying
            opaque output.
        records:
        - memory.md#mem-obj-method-report
        - memory.md#mem-rte-report-retrieval
        - epistemic.md#epi-obj-verification-summary
        - epistemic.md#epi-rte-report-summary
        note: Readable Markdown provides selected natural-language execution accounts, not the underlying
          opaque output.
      - scope: Report JSON, tags, schemas and retrieval pointers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-method-report
          - memory.md#mem-rte-report-retrieval
          - epistemic.md#epi-obj-verification-summary
          - epistemic.md#epi-rte-report-summary
          note: Structured fields and identities support fixed-rule access and computation.
        records:
        - memory.md#mem-obj-method-report
        - memory.md#mem-rte-report-retrieval
        - epistemic.md#epi-obj-verification-summary
        - epistemic.md#epi-rte-report-summary
        note: Structured fields and identities support fixed-rule access and computation.
      - scope: Run checkpoints and expanded workflow/cache inputs
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-obj-workflow-run
          - runtime.md#rt-rte-workflow-run
          note: Scheduler progress, dependencies and captured plans have symbolic execution consumers.
        records:
        - runtime.md#rt-obj-workflow-run
        - runtime.md#rt-rte-workflow-run
        note: Scheduler progress, dependencies and captured plans have symbolic execution consumers.
      - scope: Mutable registered extension code and catalog/type identities
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-rte-extension-load
          - runtime.md#rt-bap-workflow-execution
          note: TypeScript, bundle registration and type resolution are symbolic; these are not model
            weights.
        records:
        - runtime.md#rt-rte-extension-load
        - runtime.md#rt-bap-workflow-execution
        note: TypeScript, bundle registration and type resolution are symbolic; these are not model weights.
      - scope: Audit command-event fields and attestation check fields
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-command-audit
          - memory.md#mem-rte-audit-timeline
          - epistemic.md#epi-obj-attestation
          - epistemic.md#epi-rte-attestation-build
          - epistemic.md#epi-rte-attestation-ci
          note: The recorded fields are parsed, filtered or checked by deterministic consumers.
        records:
        - memory.md#mem-obj-command-audit
        - memory.md#mem-rte-audit-timeline
        - epistemic.md#epi-obj-attestation
        - epistemic.md#epi-rte-attestation-build
        - epistemic.md#epi-rte-attestation-ci
        note: The recorded fields are parsed, filtered or checked by deterministic consumers.
      - scope: Task brief prose
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - runtime.md#rt-obj-task-brief
          - runtime.md#rt-rte-agent-launch
          note: The launch asks an external agent to interpret the retained Markdown task.
        records:
        - runtime.md#rt-obj-task-brief
        - runtime.md#rt-rte-agent-launch
        note: The launch asks an external agent to interpret the retained Markdown task.
      - scope: Selected skill-evaluation result parts
        assessment: partial
        findings:
        - value: symbolic
          basis: wired
          records:
          - epistemic.md#epi-obj-skill-evals
          - epistemic.md#epi-rte-skill-evals
          note: Threshold arithmetic consumes scores, labels and counts.
        - value: natural-language
          basis: wired
          records:
          - epistemic.md#epi-obj-skill-evals
          - epistemic.md#epi-rte-skill-evals
          note: Selected failure descriptions are retained in output displays.
        records:
        - epistemic.md#epi-obj-skill-evals
        - epistemic.md#epi-rte-skill-evals
        note: Numeric scores/tool labels are symbolic; failure accounts are readable prose. External judgments
          are not classified as parametric retained memory.
      - scope: Generic file payloads, custom reports and untraced acquisition products
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-data-content
        - memory.md#mem-rte-resource-storage
        - memory.md#mem-obj-method-report
        - memory.md#mem-rte-report-retrieval
        note: Resource serialization alone does not classify semantic form at every actual consumer; binary
          content and custom report internals remain opaque.
      records:
      - memory.md#mem-obj-plan-main
      - memory.md#mem-rte-plan-iteration
      - memory.md#mem-obj-feedback-main
      - memory.md#mem-obj-review-findings
      - memory.md#mem-rte-lifecycle-checks
      - memory.md#mem-obj-lifecycle-state
      - memory.md#mem-obj-method-report
      - memory.md#mem-rte-report-retrieval
      - epistemic.md#epi-obj-verification-summary
      - epistemic.md#epi-rte-report-summary
      - runtime.md#rt-obj-workflow-run
      - runtime.md#rt-rte-workflow-run
      - runtime.md#rt-rte-extension-load
      - runtime.md#rt-bap-workflow-execution
      - memory.md#mem-obj-command-audit
      - memory.md#mem-rte-audit-timeline
      - epistemic.md#epi-obj-attestation
      - epistemic.md#epi-rte-attestation-build
      - epistemic.md#epi-rte-attestation-ci
      - runtime.md#rt-obj-task-brief
      - runtime.md#rt-rte-agent-launch
      - epistemic.md#epi-obj-skill-evals
      - epistemic.md#epi-rte-skill-evals
      - memory.md#mem-obj-data-content
      - memory.md#mem-rte-resource-storage
      note: Known prose and fixed-rule representations coexist. Arbitrary binary payloads and external
        or custom products cannot be classified from their display summaries.
    lineage:
      assessment: partial
      units:
      - scope: Caller-supplied issue plan, feedback and findings
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-plan-main
          - memory.md#mem-rte-plan-iteration
          - memory.md#mem-obj-feedback-main
          - memory.md#mem-obj-review-findings
          - memory.md#mem-rte-lifecycle-checks
          note: Methods retain content authored outside their bodies; this does not authenticate human
            authorship or establish model inference details.
        records:
        - memory.md#mem-obj-plan-main
        - memory.md#mem-rte-plan-iteration
        - memory.md#mem-obj-feedback-main
        - memory.md#mem-obj-review-findings
        - memory.md#mem-rte-lifecycle-checks
        note: Methods retain content authored outside their bodies; this does not authenticate human authorship
          or establish model inference details.
      - scope: Method and verification report projections
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-method-report
          - memory.md#mem-rte-report-retrieval
          - epistemic.md#epi-obj-verification-summary
          - epistemic.md#epi-rte-report-summary
          note: Execution context/status/handles are transformed into retained execution accounts.
        records:
        - memory.md#mem-obj-method-report
        - memory.md#mem-rte-report-retrieval
        - epistemic.md#epi-obj-verification-summary
        - epistemic.md#epi-rte-report-summary
        note: Execution context/status/handles are transformed into retained execution accounts.
      - scope: Command audit append
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-command-audit
          - memory.md#mem-rte-audit-timeline
          note: Selected tool command events are captured directly, rather than authored as standing rules.
        records:
        - memory.md#mem-obj-command-audit
        - memory.md#mem-rte-audit-timeline
        note: Selected tool command events are captured directly, rather than authored as standing rules.
      - scope: Saved workflow progress and gate decisions
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-obj-workflow-run
          - runtime.md#rt-rte-workflow-run
          - runtime.md#rt-rte-gate-resume
          note: Run outcomes and continuation decisions are retained from execution activity.
        records:
        - runtime.md#rt-obj-workflow-run
        - runtime.md#rt-rte-workflow-run
        - runtime.md#rt-rte-gate-resume
        note: Run outcomes and continuation decisions are retained from execution activity.
      - scope: Expanded/evaluated workflow replay input
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - runtime.md#rt-obj-workflow-run
          - runtime.md#rt-rte-workflow-run
          note: Expansion and expression evaluation compile an executable retained form; the authored
            definition is a different input.
        records:
        - runtime.md#rt-obj-workflow-run
        - runtime.md#rt-rte-workflow-run
        note: Expansion and expression evaluation compile an executable retained form; the authored definition
          is a different input.
      - scope: Locally edited and auto-resolved capabilities
        assessment: partial
        findings:
        - value: authored
          basis: wired
          records:
          - runtime.md#rt-rte-extension-load
          - runtime.md#rt-bap-workflow-execution
          note: A local source author can edit code subsequently reloaded.
        - value: imported
          basis: wired
          records:
          - runtime.md#rt-rte-extension-load
          - runtime.md#rt-bap-workflow-execution
          note: Allowed-collective resolution acquires a capability for later registration.
        records:
        - runtime.md#rt-rte-extension-load
        - runtime.md#rt-bap-workflow-execution
        note: Source edits and collective acquisition establish distinct paths; initial source authorship
          and all installation alternatives remain unresolved.
      - scope: Attestation projection
        assessment: partial
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - epistemic.md#epi-obj-attestation
          - epistemic.md#epi-rte-attestation-build
          - epistemic.md#epi-rte-attestation-ci
          note: Recorded run statuses supply the multi-run execution account.
        - value: other-compiled
          basis: wired
          records:
          - epistemic.md#epi-obj-attestation
          - epistemic.md#epi-rte-attestation-build
          - epistemic.md#epi-rte-attestation-ci
          note: The pure projection combines run-derived fields with supplied subject and integrity fields.
        records:
        - epistemic.md#epi-obj-attestation
        - epistemic.md#epi-rte-attestation-build
        - epistemic.md#epi-rte-attestation-ci
        note: The builder compiles supplied runs plus environment/config values; their acquisition and
          authenticity remain incompletely inspected.
      - scope: Task brief initial content, issue acquisition, external evaluation judgments and remaining
          payload origins
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-task-brief
        - runtime.md#rt-rte-agent-launch
        - memory.md#mem-obj-data-content
        - memory.md#mem-rte-resource-storage
        - epistemic.md#epi-obj-skill-evals
        - epistemic.md#epi-rte-skill-evals
        note: The records do not establish every initial provenance path; a write API or nominal human
          feedback label cannot resolve those origins.
      records:
      - memory.md#mem-obj-plan-main
      - memory.md#mem-rte-plan-iteration
      - memory.md#mem-obj-feedback-main
      - memory.md#mem-obj-review-findings
      - memory.md#mem-rte-lifecycle-checks
      - memory.md#mem-obj-method-report
      - memory.md#mem-rte-report-retrieval
      - epistemic.md#epi-obj-verification-summary
      - epistemic.md#epi-rte-report-summary
      - memory.md#mem-obj-command-audit
      - memory.md#mem-rte-audit-timeline
      - runtime.md#rt-obj-workflow-run
      - runtime.md#rt-rte-workflow-run
      - runtime.md#rt-rte-gate-resume
      - runtime.md#rt-rte-extension-load
      - runtime.md#rt-bap-workflow-execution
      - epistemic.md#epi-obj-attestation
      - epistemic.md#epi-rte-attestation-build
      - epistemic.md#epi-rte-attestation-ci
      - runtime.md#rt-obj-task-brief
      - runtime.md#rt-rte-agent-launch
      - memory.md#mem-obj-data-content
      - memory.md#mem-rte-resource-storage
      - epistemic.md#epi-obj-skill-evals
      - epistemic.md#epi-rte-skill-evals
      note: Known derivation paths do not authenticate caller origin or resolve all initial content and
        external alternatives.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Issue plan/feedback/finding prose at requested review and revision readers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-plan-main
          - memory.md#mem-rte-plan-iteration
          - memory.md#mem-obj-feedback-main
          - memory.md#mem-obj-review-findings
          - memory.md#mem-rte-lifecycle-checks
          note: Requested reads provide reference and criticism; retrieval does not prove obedience.
        records:
        - memory.md#mem-obj-plan-main
        - memory.md#mem-rte-plan-iteration
        - memory.md#mem-obj-feedback-main
        - memory.md#mem-obj-review-findings
        - memory.md#mem-rte-lifecycle-checks
        note: Requested reads provide reference and criticism; retrieval does not prove obedience.
      - scope: Approved plan steps at the later implementing agent
        assessment: known
        findings:
        - value: instruction
          basis: claimed
          records:
          - memory.md#mem-obj-plan-main
          - memory.md#mem-rte-plan-iteration
          note: The procedure says to follow the approved plan step by step; this instruction path is
            doctrine, not observed compliance.
        records:
        - memory.md#mem-obj-plan-main
        - memory.md#mem-rte-plan-iteration
        note: The procedure says to follow the approved plan step by step; this instruction path is doctrine,
          not observed compliance.
      - scope: Retained criticism at the instructed plan-revision consumer
        assessment: known
        findings:
        - value: learning
          basis: claimed
          records:
          - memory.md#mem-obj-feedback-main
          - memory.md#mem-rte-plan-iteration
          - memory.md#mem-obj-review-findings
          - memory.md#mem-rte-lifecycle-checks
          - memory.md#mem-obj-plan-main
          note: The skill directs renewed criticism and revision of a durable plan; that update-consumer
            force is separate from the revised plan downstream. No improved capacity is established.
        records:
        - memory.md#mem-obj-feedback-main
        - memory.md#mem-rte-plan-iteration
        - memory.md#mem-obj-review-findings
        - memory.md#mem-rte-lifecycle-checks
        - memory.md#mem-obj-plan-main
        note: The skill directs renewed criticism and revision of a durable plan; that update-consumer
          force is separate from the revised plan downstream. No improved capacity is established.
      - scope: Plan/review versions, severity/resolution flags and verification flags at configured preflight
          checks
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-review-findings
          - memory.md#mem-rte-lifecycle-checks
          - memory.md#mem-obj-lifecycle-state
          - memory.md#mem-bap-retained-checks
          - epistemic.md#epi-rte-issue-clearance
          note: These retained criteria determine admissibility and can veto approval or PR linking on
            the selected local paths.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-review-findings
          - memory.md#mem-rte-lifecycle-checks
          - memory.md#mem-obj-lifecycle-state
          - memory.md#mem-bap-retained-checks
          - epistemic.md#epi-rte-issue-clearance
          note: These retained criteria determine admissibility and can veto approval or PR linking on
            the selected local paths.
        records:
        - memory.md#mem-obj-review-findings
        - memory.md#mem-rte-lifecycle-checks
        - memory.md#mem-obj-lifecycle-state
        - memory.md#mem-bap-retained-checks
        - epistemic.md#epi-rte-issue-clearance
        note: These retained criteria determine admissibility and can veto approval or PR linking on the
          selected local paths.
      - scope: Issue phase at an external agent following the reload procedure
        assessment: known
        findings:
        - value: routing
          basis: claimed
          records:
          - memory.md#mem-obj-lifecycle-state
          - memory.md#mem-rte-lifecycle-checks
          note: The skill asks the later agent to query phase and choose the corresponding next procedure.
        records:
        - memory.md#mem-obj-lifecycle-state
        - memory.md#mem-rte-lifecycle-checks
        note: The skill asks the later agent to query phase and choose the corresponding next procedure.
      - scope: Workflow checkpoint/progress and captured plan at scheduler continuation
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-obj-workflow-run
          - runtime.md#rt-rte-workflow-run
          note: Stored status/dependencies select remaining work; waiting gates refuse ordinary continuation.
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-obj-workflow-run
          - runtime.md#rt-rte-workflow-run
          note: Stored status/dependencies select remaining work; waiting gates refuse ordinary continuation.
        records:
        - runtime.md#rt-obj-workflow-run
        - runtime.md#rt-rte-workflow-run
        note: Stored status/dependencies select remaining work; waiting gates refuse ordinary continuation.
      - scope: Reloaded extension code and type catalog at execution/type resolution
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-rte-extension-load
          - runtime.md#rt-bap-workflow-execution
          note: Retained type identity selects an implementation; registered code determines executable
            effects.
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-rte-extension-load
          - runtime.md#rt-bap-workflow-execution
          note: Retained type identity selects an implementation; registered code determines executable
            effects.
        records:
        - runtime.md#rt-rte-extension-load
        - runtime.md#rt-bap-workflow-execution
        note: Retained type identity selects an implementation; registered code determines executable
          effects.
      - scope: Method/verification reports and audit history at requested display/query consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-method-report
          - memory.md#mem-rte-report-retrieval
          - epistemic.md#epi-obj-verification-summary
          - epistemic.md#epi-rte-report-summary
          - memory.md#mem-obj-command-audit
          - memory.md#mem-rte-audit-timeline
          note: These accounts supply selected reference about execution and command history; they do
            not automatically become host instructions.
        records:
        - memory.md#mem-obj-method-report
        - memory.md#mem-rte-report-retrieval
        - epistemic.md#epi-obj-verification-summary
        - epistemic.md#epi-rte-report-summary
        - memory.md#mem-obj-command-audit
        - memory.md#mem-rte-audit-timeline
        note: These accounts supply selected reference about execution and command history; they do not
          automatically become host instructions.
      - scope: Attestation subject/gate/hash fields at CI admission
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - epistemic.md#epi-obj-attestation
          - epistemic.md#epi-rte-attestation-build
          - epistemic.md#epi-rte-attestation-ci
          note: Retained attestation fields are checked for admissibility; error predicates fail the job.
            Warning-only freshness does not veto.
        - value: enforcement
          basis: wired
          records:
          - epistemic.md#epi-obj-attestation
          - epistemic.md#epi-rte-attestation-build
          - epistemic.md#epi-rte-attestation-ci
          note: Retained attestation fields are checked for admissibility; error predicates fail the job.
            Warning-only freshness does not veto.
        records:
        - epistemic.md#epi-obj-attestation
        - epistemic.md#epi-rte-attestation-build
        - epistemic.md#epi-rte-attestation-ci
        note: Retained attestation fields are checked for admissibility; error predicates fail the job.
          Warning-only freshness does not veto.
      - scope: Remaining data search/ranking, evaluation/adoption and custom payload consumers
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-data-query
        - epistemic.md#epi-obj-skill-evals
        - epistemic.md#epi-rte-skill-evals
        - memory.md#mem-obj-data-content
        - memory.md#mem-rte-resource-storage
        note: Search scoring and downstream adoption/custom behavior were not fully traced. No ranking
          positive, general learning negative or universal authority conclusion follows.
      records:
      - memory.md#mem-obj-plan-main
      - memory.md#mem-rte-plan-iteration
      - memory.md#mem-obj-feedback-main
      - memory.md#mem-obj-review-findings
      - memory.md#mem-rte-lifecycle-checks
      - memory.md#mem-obj-lifecycle-state
      - memory.md#mem-bap-retained-checks
      - epistemic.md#epi-rte-issue-clearance
      - runtime.md#rt-obj-workflow-run
      - runtime.md#rt-rte-workflow-run
      - runtime.md#rt-rte-extension-load
      - runtime.md#rt-bap-workflow-execution
      - memory.md#mem-obj-method-report
      - memory.md#mem-rte-report-retrieval
      - epistemic.md#epi-obj-verification-summary
      - epistemic.md#epi-rte-report-summary
      - memory.md#mem-obj-command-audit
      - memory.md#mem-rte-audit-timeline
      - epistemic.md#epi-obj-attestation
      - epistemic.md#epi-rte-attestation-build
      - epistemic.md#epi-rte-attestation-ci
      - memory.md#mem-rte-data-query
      - epistemic.md#epi-obj-skill-evals
      - epistemic.md#epi-rte-skill-evals
      - memory.md#mem-obj-data-content
      - memory.md#mem-rte-resource-storage
      note: Values name actual retained parts and consumers, not a global force. Uninspected search/ranking,
        custom consumers and adoption routes prevent complete classification.
    write_agency:
      assessment: partial
      units:
      - scope: Automatic method and verification report derivation/persistence
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-method-report
          - memory.md#mem-rte-report-retrieval
          - epistemic.md#epi-obj-verification-summary
          - epistemic.md#epi-rte-report-summary
          note: Software derives and admits nonempty artifacts without per-report human approval.
        records:
        - memory.md#mem-obj-method-report
        - memory.md#mem-rte-report-retrieval
        - epistemic.md#epi-obj-verification-summary
        - epistemic.md#epi-rte-report-summary
        note: Software derives and admits nonempty artifacts without per-report human approval.
      - scope: Hook audit append and scheduler run/checkpoint saves
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-command-audit
          - memory.md#mem-rte-audit-timeline
          - runtime.md#rt-obj-workflow-run
          - runtime.md#rt-rte-workflow-run
          note: Hooks and scheduler save activity records as part of execution.
        records:
        - memory.md#mem-obj-command-audit
        - memory.md#mem-rte-audit-timeline
        - runtime.md#rt-obj-workflow-run
        - runtime.md#rt-rte-workflow-run
        note: Hooks and scheduler save activity records as part of execution.
      - scope: Attestation projection and evaluation result recording
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - epistemic.md#epi-obj-attestation
          - epistemic.md#epi-rte-attestation-build
          - epistemic.md#epi-rte-attestation-ci
          - epistemic.md#epi-obj-skill-evals
          - epistemic.md#epi-rte-skill-evals
          note: Scripts compute projections/results and record outcomes without per-result human approval;
            hosted acquisition alternatives remain separate.
        records:
        - epistemic.md#epi-obj-attestation
        - epistemic.md#epi-rte-attestation-build
        - epistemic.md#epi-rte-attestation-ci
        - epistemic.md#epi-obj-skill-evals
        - epistemic.md#epi-rte-skill-evals
        note: Scripts compute projections/results and record outcomes without per-result human approval;
          hosted acquisition alternatives remain separate.
      - scope: Skill-prescribed human approval of the issue plan
        assessment: known
        findings:
        - value: manual
          basis: claimed
          records:
          - runtime.md#rt-rte-issue-admission
          note: The intended human explicitly decides whether the plan proceeds. This policy does not
            authenticate the actual approve caller.
        records:
        - runtime.md#rt-rte-issue-admission
        note: The intended human explicitly decides whether the plan proceeds. This policy does not authenticate
          the actual approve caller.
      - scope: Actual plan, feedback, findings, verification flags and explicit approval submissions
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-plan-main
        - memory.md#mem-rte-plan-iteration
        - memory.md#mem-obj-feedback-main
        - memory.md#mem-obj-review-findings
        - memory.md#mem-rte-lifecycle-checks
        - memory.md#mem-obj-lifecycle-state
        - runtime.md#rt-rte-issue-admission
        note: Caller identity does not resolve whether each retained content item was supplied, edited
          or approved by a human. Empty approve arguments do not supply conversational consent.
      - scope: Initial brief/definition content, local extension edits and other acquisition/replacement
          alternatives
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-task-brief
        - runtime.md#rt-rte-agent-launch
        - runtime.md#rt-rte-extension-load
        - runtime.md#rt-bap-workflow-execution
        - memory.md#mem-obj-data-content
        - memory.md#mem-rte-resource-storage
        note: Authors and computational validators are identified, but per-content human decision versus
          software/model admission is not established on every route.
      records:
      - memory.md#mem-obj-method-report
      - memory.md#mem-rte-report-retrieval
      - epistemic.md#epi-obj-verification-summary
      - epistemic.md#epi-rte-report-summary
      - memory.md#mem-obj-command-audit
      - memory.md#mem-rte-audit-timeline
      - runtime.md#rt-obj-workflow-run
      - runtime.md#rt-rte-workflow-run
      - epistemic.md#epi-obj-attestation
      - epistemic.md#epi-rte-attestation-build
      - epistemic.md#epi-rte-attestation-ci
      - epistemic.md#epi-obj-skill-evals
      - epistemic.md#epi-rte-skill-evals
      - runtime.md#rt-rte-issue-admission
      - memory.md#mem-obj-plan-main
      - memory.md#mem-rte-plan-iteration
      - memory.md#mem-obj-feedback-main
      - memory.md#mem-obj-review-findings
      - memory.md#mem-rte-lifecycle-checks
      - memory.md#mem-obj-lifecycle-state
      - runtime.md#rt-obj-task-brief
      - runtime.md#rt-rte-agent-launch
      - runtime.md#rt-rte-extension-load
      - runtime.md#rt-bap-workflow-execution
      - memory.md#mem-obj-data-content
      - memory.md#mem-rte-resource-storage
      note: Automatic admission is supported for machine-generated accounts and checkpoints. Caller-authored
        issue content and initial acquisition retain unresolved human control; starting a command is not
        a per-content human decision.
    curation_operations:
      assessment: partial
      units:
      - scope: Caller-supplied replacement plan and finding-resolution updates
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-obj-plan-main
          - memory.md#mem-rte-plan-iteration
          - memory.md#mem-obj-review-findings
          - memory.md#mem-rte-lifecycle-checks
          note: iterate revises an existing plan; resolution annotates retained findings with flags and
            notes while preserving criticism.
        records:
        - memory.md#mem-obj-plan-main
        - memory.md#mem-rte-plan-iteration
        - memory.md#mem-obj-review-findings
        - memory.md#mem-rte-lifecycle-checks
        note: iterate revises an existing plan; resolution annotates retained findings with flags and
          notes while preserving criticism.
      - scope: Version-stale review withdrawal and local type refresh
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records:
          - memory.md#mem-obj-review-findings
          - memory.md#mem-rte-lifecycle-checks
          - runtime.md#rt-rte-extension-load
          - runtime.md#rt-bap-workflow-execution
          note: A changed plan withdraws reliance on the old review for clearance; refresh invalidates
            affected registered types without replacing built-ins.
        records:
        - memory.md#mem-obj-review-findings
        - memory.md#mem-rte-lifecycle-checks
        - runtime.md#rt-rte-extension-load
        - runtime.md#rt-bap-workflow-execution
        note: A changed plan withdraws reliance on the old review for clearance; refresh invalidates affected
          registered types without replacing built-ins.
      - scope: Method and verification summary derivation
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-obj-method-report
          - memory.md#mem-rte-report-retrieval
          - epistemic.md#epi-obj-verification-summary
          - epistemic.md#epi-rte-report-summary
          note: Selected execution facts are compressed into smaller retained Markdown/JSON accounts;
            underlying data can remain.
        records:
        - memory.md#mem-obj-method-report
        - memory.md#mem-rte-report-retrieval
        - epistemic.md#epi-obj-verification-summary
        - epistemic.md#epi-rte-report-summary
        note: Selected execution facts are compressed into smaller retained Markdown/JSON accounts; underlying
          data can remain.
      - scope: Attestation gate derivation over retained verification runs
        assessment: known
        findings:
        - value: synthesize
          basis: wired
          records:
          - epistemic.md#epi-obj-attestation
          - epistemic.md#epi-rte-attestation-build
          - epistemic.md#epi-rte-attestation-ci
          note: The builder creates an aggregate policy claim from recorded steps/counts. This is synthesis
            in the curation sense, not evidence of ampliative conjecture or semantic acceptance.
        records:
        - epistemic.md#epi-obj-attestation
        - epistemic.md#epi-rte-attestation-build
        - epistemic.md#epi-rte-attestation-ci
        note: The builder creates an aggregate policy claim from recorded steps/counts. This is synthesis
          in the curation sense, not evidence of ampliative conjecture or semantic acceptance.
      - scope: Policy-driven expiry, version pruning and orphan cleanup
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-rte-data-cleanup
          note: Mechanical deletion reduces future availability of retained data/history. Infinite duration
            does not defeat a finite version limit.
        records:
        - memory.md#mem-rte-data-cleanup
        note: Mechanical deletion reduces future availability of retained data/history. Infinite duration
          does not defeat a finite version limit.
      - scope: Other report transformations, initial issue acquisition and broader datastore/run-artifact
          maintenance
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-method-report
        - memory.md#mem-rte-report-retrieval
        - epistemic.md#epi-obj-verification-summary
        - epistemic.md#epi-rte-report-summary
        - memory.md#mem-rte-data-cleanup
        - memory.md#mem-obj-data-content
        - memory.md#mem-rte-resource-storage
        note: The reports retain uninspected transformation/cleanup alternatives; complete curation coverage
          and absence of other operations cannot be asserted.
      records:
      - memory.md#mem-obj-plan-main
      - memory.md#mem-rte-plan-iteration
      - memory.md#mem-obj-review-findings
      - memory.md#mem-rte-lifecycle-checks
      - runtime.md#rt-rte-extension-load
      - runtime.md#rt-bap-workflow-execution
      - memory.md#mem-obj-method-report
      - memory.md#mem-rte-report-retrieval
      - epistemic.md#epi-obj-verification-summary
      - epistemic.md#epi-rte-report-summary
      - epistemic.md#epi-obj-attestation
      - epistemic.md#epi-rte-attestation-build
      - epistemic.md#epi-rte-attestation-ci
      - memory.md#mem-rte-data-cleanup
      - memory.md#mem-obj-data-content
      - memory.md#mem-rte-resource-storage
      note: Recorded transformations establish several operations; no deduplication or promotion is inferred
        from primary-key checks, indexing or route names. Custom report, acquisition and maintenance alternatives
        remain unresolved.
    read_back_direction:
      assessment: partial
      units:
      - scope: Requested data query/get and method resource loads
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-data-query
          - memory.md#mem-obj-data-content
          - memory.md#mem-rte-resource-storage
          note: Caller predicates, resource names and optional versions request retained material; concrete
            issue readers establish later consumption.
        records:
        - memory.md#mem-rte-data-query
        - memory.md#mem-obj-data-content
        - memory.md#mem-rte-resource-storage
        note: Caller predicates, resource names and optional versions request retained material; concrete
          issue readers establish later consumption.
      - scope: Requested plan review/iteration/checks and instructed phase reload
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-obj-plan-main
          - memory.md#mem-rte-plan-iteration
          - memory.md#mem-obj-lifecycle-state
          - memory.md#mem-rte-lifecycle-checks
          - memory.md#mem-obj-review-findings
          note: Method consumers request exact resources, and a later agent is instructed to request state-main.
        records:
        - memory.md#mem-obj-plan-main
        - memory.md#mem-rte-plan-iteration
        - memory.md#mem-obj-lifecycle-state
        - memory.md#mem-rte-lifecycle-checks
        - memory.md#mem-obj-review-findings
        note: Method consumers request exact resources, and a later agent is instructed to request state-main.
      - scope: Requested stored report, audit timeline and activity summary
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-obj-method-report
          - memory.md#mem-rte-report-retrieval
          - epistemic.md#epi-obj-verification-summary
          - epistemic.md#epi-rte-report-summary
          - memory.md#mem-obj-command-audit
          - memory.md#mem-rte-audit-timeline
          - memory.md#mem-rte-activity-summary
          note: A report/history request selects surviving retained artifacts or source records; computed
            displays need not themselves be persisted.
        records:
        - memory.md#mem-obj-method-report
        - memory.md#mem-rte-report-retrieval
        - epistemic.md#epi-obj-verification-summary
        - epistemic.md#epi-rte-report-summary
        - memory.md#mem-obj-command-audit
        - memory.md#mem-rte-audit-timeline
        - memory.md#mem-rte-activity-summary
        note: A report/history request selects surviving retained artifacts or source records; computed
          displays need not themselves be persisted.
      - scope: Explicit workflow/task continuation and CI attestation fetch
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-obj-workflow-run
          - runtime.md#rt-rte-workflow-run
          - runtime.md#rt-obj-task-brief
          - runtime.md#rt-rte-agent-launch
          - epistemic.md#epi-obj-attestation
          - epistemic.md#epi-rte-attestation-build
          - epistemic.md#epi-rte-attestation-ci
          note: Resume loads stored state and CI requests the commit-associated attestation. External
            conversation restoration is excluded.
        records:
        - runtime.md#rt-obj-workflow-run
        - runtime.md#rt-rte-workflow-run
        - runtime.md#rt-obj-task-brief
        - runtime.md#rt-rte-agent-launch
        - epistemic.md#epi-obj-attestation
        - epistemic.md#epi-rte-attestation-build
        - epistemic.md#epi-rte-attestation-ci
        note: Resume loads stored state and CI requests the commit-associated attestation. External conversation
          restoration is excluded.
      - scope: Automatic capability resolution and broader custom/serve/dashboard consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-extension-load
        - runtime.md#rt-bap-workflow-execution
        - memory.md#mem-rte-data-query
        - epistemic.md#epi-obj-skill-evals
        - epistemic.md#epi-rte-skill-evals
        note: Records establish later consumption but do not inventory every request/selection/delivery
          operation or alternative injection route. No global absence of push follows.
      records:
      - memory.md#mem-rte-data-query
      - memory.md#mem-obj-data-content
      - memory.md#mem-rte-resource-storage
      - memory.md#mem-obj-plan-main
      - memory.md#mem-rte-plan-iteration
      - memory.md#mem-obj-lifecycle-state
      - memory.md#mem-rte-lifecycle-checks
      - memory.md#mem-obj-review-findings
      - memory.md#mem-obj-method-report
      - memory.md#mem-rte-report-retrieval
      - epistemic.md#epi-obj-verification-summary
      - epistemic.md#epi-rte-report-summary
      - memory.md#mem-obj-command-audit
      - memory.md#mem-rte-audit-timeline
      - memory.md#mem-rte-activity-summary
      - runtime.md#rt-obj-workflow-run
      - runtime.md#rt-rte-workflow-run
      - runtime.md#rt-obj-task-brief
      - runtime.md#rt-rte-agent-launch
      - epistemic.md#epi-obj-attestation
      - epistemic.md#epi-rte-attestation-build
      - epistemic.md#epi-rte-attestation-ci
      - runtime.md#rt-rte-extension-load
      - runtime.md#rt-bap-workflow-execution
      - epistemic.md#epi-obj-skill-evals
      - epistemic.md#epi-rte-skill-evals
      note: Named request-driven routes establish pull. No complete inventory establishes pull-only behavior;
        internal requested loads are not relabelled push because software performs delivery.
    read_back_signal:
      assessment: uninspected
      units:
      - scope: Explicit data, issue, report, audit/activity and continuation requests
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-data-query
        - memory.md#mem-obj-plan-main
        - memory.md#mem-rte-plan-iteration
        - memory.md#mem-obj-lifecycle-state
        - memory.md#mem-rte-lifecycle-checks
        - memory.md#mem-obj-review-findings
        - memory.md#mem-obj-method-report
        - memory.md#mem-rte-report-retrieval
        - epistemic.md#epi-obj-verification-summary
        - epistemic.md#epi-rte-report-summary
        - memory.md#mem-obj-command-audit
        - memory.md#mem-rte-audit-timeline
        - runtime.md#rt-obj-workflow-run
        - runtime.md#rt-rte-workflow-run
        - runtime.md#rt-obj-task-brief
        - runtime.md#rt-rte-agent-launch
        - epistemic.md#epi-obj-attestation
        - epistemic.md#epi-rte-attestation-build
        - epistemic.md#epi-rte-attestation-ci
        note: These operations fulfill requests. Resource IDs, report tags, versions and time windows
          on a pull do not establish an identifier/coarse push signal.
      - scope: Remaining capability/custom/serve/dashboard delivery alternatives
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-extension-load
        - runtime.md#rt-bap-workflow-execution
        - memory.md#mem-rte-data-query
        - epistemic.md#epi-obj-skill-evals
        - epistemic.md#epi-rte-skill-evals
        note: No accepted record fully specifies an unsolicited selector trigger, its input and delivered
          retained part for these alternatives. Push existence and its signal cannot be determined.
      records:
      - memory.md#mem-rte-data-query
      - memory.md#mem-obj-plan-main
      - memory.md#mem-rte-plan-iteration
      - memory.md#mem-obj-lifecycle-state
      - memory.md#mem-rte-lifecycle-checks
      - memory.md#mem-obj-review-findings
      - memory.md#mem-obj-method-report
      - memory.md#mem-rte-report-retrieval
      - epistemic.md#epi-obj-verification-summary
      - epistemic.md#epi-rte-report-summary
      - memory.md#mem-obj-command-audit
      - memory.md#mem-rte-audit-timeline
      - runtime.md#rt-obj-workflow-run
      - runtime.md#rt-rte-workflow-run
      - runtime.md#rt-obj-task-brief
      - runtime.md#rt-rte-agent-launch
      - epistemic.md#epi-obj-attestation
      - epistemic.md#epi-rte-attestation-build
      - epistemic.md#epi-rte-attestation-ci
      - runtime.md#rt-rte-extension-load
      - runtime.md#rt-bap-workflow-execution
      - epistemic.md#epi-obj-skill-evals
      - epistemic.md#epi-rte-skill-evals
      note: The classified routes are requested pulls; they require no push-signal findings. Remaining
        included consumers prevent a boundary-wide inapplicable assessment.
    trace_learning:
      assessment: partial
      units:
      - scope: Automatic method-summary derivation and later report/data retrieval
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-obj-method-report
          - memory.md#mem-rte-report-retrieval
          note: Execution context and handles feed software-produced durable summaries; later report/data
            consumers receive selected reference context. This qualifies without parameter updates, automatic
            push or observed benefit.
        records:
        - memory.md#mem-obj-method-report
        - memory.md#mem-rte-report-retrieval
        note: Execution context and handles feed software-produced durable summaries; later report/data
          consumers receive selected reference context. This qualifies without parameter updates, automatic
          push or observed benefit.
      - scope: Automatic verification-summary derivation and later report retrieval
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - epistemic.md#epi-obj-verification-summary
          - epistemic.md#epi-rte-report-summary
          note: Recorded workflow step feedback feeds persisted summaries exposed to later report search/get
            consumers as execution context. This is not authenticated verification or demonstrated improvement.
        records:
        - epistemic.md#epi-obj-verification-summary
        - epistemic.md#epi-rte-report-summary
        note: Recorded workflow step feedback feeds persisted summaries exposed to later report search/get
          consumers as execution context. This is not authenticated verification or demonstrated improvement.
      - scope: Raw audit and run checkpoints, requested activity projections
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-command-audit
        - memory.md#mem-rte-audit-timeline
        - runtime.md#rt-obj-workflow-run
        - runtime.md#rt-rte-workflow-run
        - memory.md#mem-rte-activity-summary
        note: Raw logging and unchanged execution continuation alone do not establish the qualifying transformation.
          Activity display is not persisted as a replacement summary. No absence record covers every included
          alternative.
      - scope: Issue revision and attestation/evaluation-to-adoption alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-plan-main
        - memory.md#mem-rte-plan-iteration
        - memory.md#mem-obj-feedback-main
        - epistemic.md#epi-obj-attestation
        - epistemic.md#epi-rte-attestation-build
        - epistemic.md#epi-rte-attestation-ci
        - epistemic.md#epi-obj-skill-evals
        - epistemic.md#epi-rte-skill-evals
        note: Issue content comes from callers with unresolved control and trace origin; attestation changes
          operational admission rather than a demonstrated durable behavioral update. Evaluation records
          establish no automatic successor-skill selection, while broader adoption alternatives remain
          uninspected.
      records:
      - memory.md#mem-obj-method-report
      - memory.md#mem-rte-report-retrieval
      - epistemic.md#epi-obj-verification-summary
      - epistemic.md#epi-rte-report-summary
      - memory.md#mem-obj-command-audit
      - memory.md#mem-rte-audit-timeline
      - runtime.md#rt-obj-workflow-run
      - runtime.md#rt-rte-workflow-run
      - memory.md#mem-rte-activity-summary
      - memory.md#mem-obj-plan-main
      - memory.md#mem-rte-plan-iteration
      - memory.md#mem-obj-feedback-main
      - epistemic.md#epi-obj-attestation
      - epistemic.md#epi-rte-attestation-build
      - epistemic.md#epi-rte-attestation-ci
      - epistemic.md#epi-obj-skill-evals
      - epistemic.md#epi-rte-skill-evals
      note: Automatic trace-fed retained reports with later reference/context consumers establish a local
        yes. Raw logs, caller revisions and unresolved adoption alternatives are not thereby classified;
        no system-wide no or improved capacity is inferred.
    trace_source:
      assessment: partial
      units:
      - scope: Method-summary execution-context input
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-obj-method-report
          - memory.md#mem-rte-report-retrieval
          note: Method status, errors and output handles are execution feedback used to produce the retained
            summary; argument values and full conversation are not consumed.
        records:
        - memory.md#mem-obj-method-report
        - memory.md#mem-rte-report-retrieval
        note: Method status, errors and output handles are execution feedback used to produce the retained
          summary; argument values and full conversation are not consumed.
      - scope: Verification-summary step-execution input
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records:
          - epistemic.md#epi-obj-verification-summary
          - epistemic.md#epi-rte-report-summary
          note: Recorded step outcomes supply execution feedback for the retained account; no session
            transcript or linked experience-learning trajectory is established.
        records:
        - epistemic.md#epi-obj-verification-summary
        - epistemic.md#epi-rte-report-summary
        note: Recorded step outcomes supply execution feedback for the retained account; no session transcript
          or linked experience-learning trajectory is established.
      - scope: Audit/checkpoint and issue/verification adoption alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-command-audit
        - memory.md#mem-rte-audit-timeline
        - runtime.md#rt-obj-workflow-run
        - runtime.md#rt-rte-workflow-run
        - memory.md#mem-obj-plan-main
        - memory.md#mem-rte-plan-iteration
        - memory.md#mem-obj-feedback-main
        - epistemic.md#epi-obj-attestation
        - epistemic.md#epi-rte-attestation-build
        - epistemic.md#epi-rte-attestation-ci
        - epistemic.md#epi-obj-skill-evals
        - epistemic.md#epi-rte-skill-evals
        note: Tool commands and run outcomes exist, but their presence does not classify a qualifying
          learning source. Initial caller provenance, automatic admission and later behavior-shaping adoption
          remain unresolved; session logs, event streams and trajectories cannot be inferred.
      records:
      - memory.md#mem-obj-method-report
      - memory.md#mem-rte-report-retrieval
      - epistemic.md#epi-obj-verification-summary
      - epistemic.md#epi-rte-report-summary
      - memory.md#mem-obj-command-audit
      - memory.md#mem-rte-audit-timeline
      - runtime.md#rt-obj-workflow-run
      - runtime.md#rt-rte-workflow-run
      - memory.md#mem-obj-plan-main
      - memory.md#mem-rte-plan-iteration
      - memory.md#mem-obj-feedback-main
      - epistemic.md#epi-obj-attestation
      - epistemic.md#epi-rte-attestation-build
      - epistemic.md#epi-rte-attestation-ci
      - epistemic.md#epi-obj-skill-evals
      - epistemic.md#epi-rte-skill-evals
      note: Inspected summary writes consume execution feedback, supporting tool-traces. Other possible
        learning routes retain unresolved original input and control; serialization as a run/event does
        not add event-streams or trajectories.
---

# Swamp memory profile

## Comparison rationale

The comparison is partial because accepted records retain unresolved alternatives,
not because inspected wiring lacks an execution demonstration. File storage,
symbolic checks, requested reads and software report writes are implementation
findings. Agent obedience, actual improvement, human consent and external
persistence are not established by that wiring.

### Objects, forms and consumers

[MEM-OBJ-data-content](memory.md#mem-obj-data-content) distinguishes content
files from YAML access metadata and opaque bytes from interpreted prose.
[MEM-OBJ-method-report](memory.md#mem-obj-method-report) separately describes
Markdown, JSON and underlying output pointers. A readable report cannot classify
the form or force of the payload it points to. Likewise,
[MEM-OBJ-plan-main](memory.md#mem-obj-plan-main) and
[MEM-RTE-plan-iteration](memory.md#mem-rte-plan-iteration) establish that ordinary
review omits rationale-bearing plan fields even when the full resource survives.
The file-backed witness does not resolve every configured backend or imply a
relational substrate from a query API.

[MEM-BAP-retained-checks](memory.md#mem-bap-retained-checks) supports validation
and enforcement at the selected preflight consumers, not universal host control.
[RT-RTE-workflow-run](runtime.md#rt-rte-workflow-run) supports routing and gate
constraints through saved progress. Instruction and learning authority on issue
plans/criticism remain at the skill's claimed agent paths in
[MEM-RTE-plan-iteration](memory.md#mem-rte-plan-iteration). Learning authority at
an instructed revision consumer does not establish an automatic trace-fed write,
improved capacity or a qualifying trace source.

### Derivation and curation

[MEM-RTE-report-retrieval](memory.md#mem-rte-report-retrieval) and
[EPI-RTE-report-summary](epistemic.md#epi-rte-report-summary) describe reduced
retained accounts of execution. Their consolidation differs from the requested,
non-persisted activity display in
[MEM-RTE-activity-summary](memory.md#mem-rte-activity-summary).
[EPI-RTE-attestation-build](epistemic.md#epi-rte-attestation-build) additionally
creates an aggregate gate proposition. Its curation synthesis is entailed within
the supplied symbolic input domain, not epistemic ampliative conjecture.
[MEM-RTE-data-cleanup](memory.md#mem-rte-data-cleanup) supports mechanical decay,
not semantic rejection. Review staleness and extension refresh support bounded
invalidation through [MEM-RTE-lifecycle-checks](memory.md#mem-rte-lifecycle-checks)
and [RT-RTE-extension-load](runtime.md#rt-rte-extension-load).

### Admission, read-back and traces

Human approval is a claimed policy in
[RT-RTE-issue-admission](runtime.md#rt-rte-issue-admission), while actual generic
caller submissions remain unresolved. Automatic summary/checkpoint admission
has a different mechanism and is not made manual by an upstream command.
[MEM-RTE-data-query](memory.md#mem-rte-data-query) and the other requested read
routes establish pull; their names, tags and count budgets do not establish
identifier or coarse push selection. Uninspected alternatives prevent a
pull-only system conclusion and a globally inapplicable signal axis.

Automatic report writes qualify locally: execution feedback becomes a durable
summary delivered as reference/context through a later report/data request in
[MEM-RTE-report-retrieval](memory.md#mem-rte-report-retrieval) and
[EPI-RTE-report-summary](epistemic.md#epi-rte-report-summary). This classification
requires neither novel claims, a standing-policy rewrite nor observed benefit.
Their recorded input supports tool-traces, not conversation learning.
[EPI-RTE-skill-evals](epistemic.md#epi-rte-skill-evals) does not establish an
automatically selected successor skill. Raw audit capture and checkpoint saves
are not additional qualifying updates merely because they retain activity.
No bounded absence record supports a local or global trace-learning "no".

### Canonical identity and inspection log

The reconciliation supersedes the epistemic issue-feedback route with
[MEM-RTE-plan-iteration](memory.md#mem-rte-plan-iteration); this profile uses the
canonical route, including its latest-per-name feedback limitation. Plan and
feedback remain separately classified parts, while the epistemic combined
container is not treated as another memory. Adversarial review/clearance and the
broader memory finding/check records remain distinct scopes. Method and
verification reports also remain distinct products despite shared persistence.
No other supersession changes a value.

No frozen-source files were read for this profile. All classifications use the
supplied accepted records and reconciliation; no source evidence or records
were added. The uninspected units preserve their missing facts instead of
turning a known witness into complete system coverage.
